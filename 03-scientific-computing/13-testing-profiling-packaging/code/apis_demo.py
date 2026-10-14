"""Consuming an HTTP API without a network: a local FDSN-style test server.

Run:  python apis_demo.py
Requires: standard library only

The lesson is about REST APIs for Earth data, and the honest way to teach one
offline is to run a server that behaves like one. This script starts a
``ThreadingHTTPServer`` on 127.0.0.1 with an ephemeral port and implements four
behaviours that every real data service has and every naive client ignores:

  /fdsnws/event/1/query   a paginated catalogue with an ETag and a 304 path
  /v1/flaky               503 twice, then 200       (transient failure)
  /v1/limited             429 with Retry-After       (rate limiting)
  /v1/slow                sleeps, for timeout demos (not called here)

The client side then demonstrates, with measured numbers: byte counts with and
without a conditional request, the retry ladder actually taken, the attempts
needed to get past a rate limit, what a connection to a dead port raises, and
how to turn a downloaded catalogue into a citation-ready checksum plus a
derived scientific quantity (a Gutenberg-Richter b-value).

Nothing leaves the machine; the sockets are loopback only.
"""

from __future__ import annotations

import hashlib
import json
import math
import socket
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

SEED = 20260714
N_EVENTS = 137


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --------------------------------------------------------------------------
# A deterministic synthetic catalogue
# --------------------------------------------------------------------------

def build_catalogue(n: int = N_EVENTS) -> list[dict]:
    """A reproducible synthetic earthquake catalogue (no network, no data file).

    Magnitudes follow a Gutenberg-Richter law with b = 1.0 down to Mc = 2.5, so
    the b-value computed at the end of the script has a known answer to compare
    against.
    """
    import random
    rng = random.Random(SEED)
    events = []
    t0 = 1_700_000_000.0
    for i in range(n):
        # Inverse-CDF sampling of the GR law: m = Mc - log10(U)/b
        magnitude = 2.5 - math.log10(rng.random()) / 1.0
        events.append({
            "id": f"syn{i:06d}",
            "time": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime(t0 + i * 3600.0)),
            "latitude": round(38.0 + rng.uniform(-1.5, 1.5), 4),
            "longitude": round(23.0 + rng.uniform(-1.5, 1.5), 4),
            "depth_km": round(rng.uniform(2.0, 25.0), 2),
            "magnitude": round(magnitude, 2),
            "magnitude_type": "Mw",
        })
    return events


CATALOGUE = build_catalogue()

COUNTERS: dict[str, int] = {"flaky": 0, "limited": 0}


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *_args) -> None:      # keep the demo output readable
        pass

    def _send(self, code: int, body: bytes, ctype: str = "application/json",
              extra: dict[str, str] | None = None) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        for key, value in (extra or {}).items():
            self.send_header(key, value)
        self.end_headers()
        if body:
            self.wfile.write(body)

    def do_GET(self) -> None:                   # noqa: N802 - http.server API
        from urllib.parse import parse_qs, urlparse
        parsed = urlparse(self.path)

        if parsed.path == "/fdsnws/event/1/query":
            params = parse_qs(parsed.query)
            limit = int(params.get("limit", ["25"])[0])
            offset = int(params.get("offset", ["0"])[0])
            page = CATALOGUE[offset:offset + limit]
            body = json.dumps(
                {"events": page, "total": len(CATALOGUE),
                 "limit": limit, "offset": offset},
                separators=(",", ":"),
            ).encode()
            etag = '"' + hashlib.md5(body).hexdigest() + '"'
            if self.headers.get("If-None-Match") == etag:
                self._send(304, b"", extra={"ETag": etag})
                return
            self._send(200, body, extra={
                "ETag": etag,
                "Cache-Control": "public, max-age=60",
                "X-Total-Count": str(len(CATALOGUE)),
            })
            return

        if parsed.path == "/v1/flaky":
            COUNTERS["flaky"] += 1
            if COUNTERS["flaky"] <= 2:
                # no Retry-After: the client must choose its own backoff
                self._send(503, b'{"error":"service unavailable"}')
                return
            self._send(200, json.dumps({"ok": True,
                                        "attempt": COUNTERS["flaky"]}).encode())
            return

        if parsed.path == "/v1/limited":
            COUNTERS["limited"] += 1
            if COUNTERS["limited"] <= 3:
                self._send(429, b'{"error":"too many requests"}',
                           extra={"Retry-After": "1"})
                return
            self._send(200, json.dumps({"ok": True,
                                        "attempt": COUNTERS["limited"]}).encode())
            return

        if parsed.path == "/v1/slow":
            time.sleep(2.0)
            self._send(200, b'{"ok":true}')
            return

        self._send(404, b'{"error":"not found"}')


# --------------------------------------------------------------------------
# The client
# --------------------------------------------------------------------------

class Session:
    """A tiny client with retries, backoff, an ETag cache and byte accounting."""

    RETRY_STATUS = {429, 500, 502, 503, 504}

    def __init__(self, base_url: str, max_attempts: int = 6,
                 base_delay: float = 0.02, max_delay: float = 0.5) -> None:
        self.base_url = base_url
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay          # capped so the demo finishes quickly
        self.bytes_downloaded = 0
        self.bytes_saved = 0
        # path, status, delay the server asked for, delay actually used
        self.attempts: list[tuple[str, int, float, float]] = []
        self._etags: dict[str, str] = {}
        self._cache: dict[str, bytes] = {}

    def etag_for(self, path: str) -> str | None:
        """The ETag most recently seen for a path, if any."""
        return self._etags.get(path)

    def get(self, path: str, conditional: bool = True,
            timeout: float = 5.0) -> tuple[int, bytes]:
        url = self.base_url + path
        for attempt in range(1, self.max_attempts + 1):
            request = urllib.request.Request(url, headers={"Accept": "application/json"})
            if conditional and path in self._etags:
                request.add_header("If-None-Match", self._etags[path])
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    body = response.read()
                    self.bytes_downloaded += len(body)
                    self.attempts.append((path, response.status, 0.0, 0.0))
                    if response.status == 304:
                        self.bytes_saved += len(self._cache.get(path, b""))
                        return response.status, self._cache[path]
                    if "ETag" in response.headers:
                        self._etags[path] = response.headers["ETag"]
                    self._cache[path] = body
                    return response.status, body
            except urllib.error.HTTPError as exc:
                if exc.code == 304:
                    # urllib raises HTTPError for 304 even though it is a
                    # success. Every conditional-GET client must special-case
                    # this; forgetting it turns a cache hit into a crash.
                    self.attempts.append((path, 304, 0.0, 0.0))
                    cached = self._cache.get(path, b"")
                    self.bytes_saved += len(cached)
                    return 304, cached
                requested, delay = self._backoff_delay(exc, attempt)
                self.attempts.append((path, exc.code, requested, delay))
                if exc.code not in self.RETRY_STATUS or attempt == self.max_attempts:
                    raise
                time.sleep(delay)
            except (urllib.error.URLError, socket.timeout) as exc:
                requested = self.base_delay * 2 ** (attempt - 1)
                delay = min(requested, self.max_delay)
                self.attempts.append((path, 0, requested, delay))
                if attempt == self.max_attempts:
                    raise
                time.sleep(delay)
        raise RuntimeError("unreachable")

    def _backoff_delay(self, exc: urllib.error.HTTPError,
                       attempt: int) -> tuple[float, float]:
        """Return (delay the server asked for, delay actually used)."""
        retry_after = exc.headers.get("Retry-After") if exc.headers else None
        if retry_after is not None:
            try:
                requested = float(retry_after)
                print(f"    server sent Retry-After: {requested:g} s")
                return requested, min(requested, self.max_delay)
            except ValueError:
                pass
        requested = self.base_delay * 2 ** (attempt - 1)
        return requested, min(requested, self.max_delay)


def fetch_all_events(session: Session, page_size: int = 25) -> list[dict]:
    """Follow the pagination to completion, using offset/limit."""
    events: list[dict] = []
    offset = 0
    while True:
        status, body = session.get(
            f"/fdsnws/event/1/query?format=json&limit={page_size}&offset={offset}"
        )
        payload = json.loads(body)
        events.extend(payload["events"])
        print(f"    page offset={offset:>4} status={status} "
              f"events={len(payload['events']):>3} total={payload['total']}")
        offset += page_size
        if offset >= payload["total"]:
            return events


# --------------------------------------------------------------------------
# Demonstrations
# --------------------------------------------------------------------------

def demo_conditional_get(session: Session) -> None:
    section("1. One request, then a conditional request: what the cache saves")
    path = "/fdsnws/event/1/query?format=json&limit=25&offset=0"
    status, body = session.get(path)
    print(f"  first request : status {status}, {len(body):>5} bytes, "
          f"ETag {session.etag_for(path)}")
    before = session.bytes_downloaded
    status2, body2 = session.get(path)
    print(f"  second request: status {status2}, {len(body2):>5} bytes of body")
    print(f"  bytes on the wire for the second request: "
          f"{session.bytes_downloaded - before}")
    print(f"  identical payload: {body == body2}")
    print("\n  The second exchange still costs a round trip, but the body is not")
    print("  transferred. For a 30 MB waveform day-file over a metered link, that")
    print("  is the difference between re-running an analysis and not. Note that a")
    print("  304 must be handled as a SUCCESS: the payload you want is in your")
    print("  cache, not in the response.")
    del body, body2


def demo_pagination(session: Session) -> None:
    section("2. Pagination: 137 events in pages of 25")
    events = fetch_all_events(session, page_size=25)
    print(f"  events fetched: {len(events)} "
          f"(server total {len(CATALOGUE)})   equal: {len(events) == len(CATALOGUE)}")
    print("\n  Pagination is not an implementation detail. A client that reads only")
    print("  the first page gets a silently truncated catalogue, and every statistic")
    print("  computed from it is wrong by an unknown amount. Use the server's own")
    print("  `total`, not a failed page, to decide when to stop.")


def demo_retry_ladder(session: Session) -> None:
    section("3. Transient failures: the retry ladder that was actually taken")
    status, body = session.get("/v1/flaky")
    print(f"  final status {status}: {body.decode()}")
    print(f"  {'path':>12} {'status':>7} {'backoff chosen (s)':>19}")
    for path, code, _requested, delay in session.attempts[-3:]:
        print(f"  {path:>12} {code:>7} {delay:>19.4f}")
    print("  No Retry-After header was sent, so the client had to choose: it")
    print("  doubled the delay each attempt, starting from 20 ms.")
    print("\n  503 is 'try again'; a client that raises on the first one converts a")
    print("  two-second server hiccup into a failed analysis. The retry policy is a")
    print("  scientific decision: retrying a POST that charges money, or that")
    print("  submits a job, is not the same as retrying a GET.")


def demo_rate_limit(session: Session) -> None:
    section("4. Rate limiting: honouring Retry-After instead of hammering")
    before = len(session.attempts)
    status, body = session.get("/v1/limited")
    print(f"  final status {status}: {body.decode()}")
    ladder = session.attempts[before:]
    print(f"  attempts needed: {len(ladder)}")
    for _path, code, requested, used in ladder:
        note = "" if requested == used else f"  (asked for {requested:g} s, capped to {used:g} s)"
        print(f"    status {code}  waited {used:.3f} s{note}")
    total_wait = sum(u for _p, _c, _r, u in ladder)
    print(f"  total time spent waiting politely: {total_wait:.3f} s")
    print("  The cap is a demo convenience; production code should honour the")
    print("  server's value, with a ceiling only to protect against a hostile one.")
    print("\n  A client that ignores 429 gets blocked, and the block is usually by")
    print("  IP, so it is the whole laboratory that loses access. Retry-After is")
    print("  the server telling you the cheapest legitimate schedule.")


def demo_dead_endpoint(host: str) -> None:
    section("5. What a connection to a dead service raises")
    dead = f"http://{host}:9"          # port 9 (discard) is not listening
    try:
        urllib.request.urlopen(dead + "/fdsnws/event/1/query", timeout=2.0)
    except urllib.error.URLError as exc:
        print(f"  urlopen({dead}/fdsnws/...) raised URLError")
        print(f"  reason: {exc.reason!r}")
    print("  This is the exception to catch, not Exception: a URLError covers DNS")
    print("  failure, refused connection and TLS problems, and is unambiguously a")
    print("  transport failure rather than a bug in your parsing code. Distinct")
    print("  exceptions let a pipeline decide whether to retry, to fail, or to fall")
    print("  back to a local copy.")


def demo_provenance_and_science(session: Session) -> None:
    section("6. From bytes to a citation and a number")
    status, body = session.get("/fdsnws/event/1/query?format=json&limit=500&offset=0")
    digest = hashlib.sha256(body).hexdigest()
    print(f"  payload: status {status}, {len(body)} bytes")
    print(f"  sha256  : {digest}")
    print("  Record that hash, the URL that produced it and the retrieval date.")
    print("  A catalogue query without them is unreproducible even if the service")
    print("  is still up, because the service's content changed underneath you.")

    events = json.loads(body)["events"]
    magnitudes = [e["magnitude"] for e in events]
    mc = 2.5
    n = len(magnitudes)
    n_above = sum(1 for m in magnitudes if m >= mc)
    mean_excess = sum(m - mc for m in magnitudes if m >= mc) / max(n_above, 1)
    b_value = math.log10(math.e) / mean_excess
    print(f"\n  events: {n}   Mc = {mc}   events above Mc: {n_above}")
    print(f"  mean magnitude excess: {mean_excess:.4f}")
    print(f"  Aki/Utsu maximum-likelihood b-value: {b_value:.3f}")
    print("  Synthetic data drawn with b = 1.0, so the estimate should be near 1.0;")
    print("  the sampling error on ~137 events is large enough that 'near' is all")
    print("  that can be claimed. Quoting b = 1.000 would be a lie about precision.")
    print(f"  Standard error estimate b/sqrt(N): "
          f"{b_value / math.sqrt(max(n_above, 1)):.3f}")


def main() -> int:
    build_catalogue()                            # warm the module-level catalogue
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    host, port = server.server_address
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://{host}:{port}"
    print(f"local test service listening on {base_url} (loopback only)")
    try:
        session = Session(base_url)
        demo_conditional_get(session)
        demo_pagination(session)
        demo_retry_ladder(session)
        demo_rate_limit(session)
        demo_dead_endpoint(host)
        demo_provenance_and_science(session)

        section("Accounting for the whole session")
        print(f"  successful/attempted requests: {len(session.attempts)}")
        print(f"  bytes actually downloaded    : {session.bytes_downloaded:,}")
        print(f"  bytes saved by the cache     : {session.bytes_saved:,}")
        by_status: dict[int, int] = {}
        for _path, code, _requested, _used in session.attempts:
            by_status[code] = by_status.get(code, 0) + 1
        for code in sorted(by_status):
            print(f"    status {code:>3}: {by_status[code]}")
        print("  Byte counts and status histograms are the two measurements that make")
        print("  an API-dependent pipeline reviewable. Both are machine-independent.")
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2.0)
    section("Summary")
    print("The transport is HTTP; the science is in what you do when it misbehaves.")
    print("Retry transient codes with backoff, honour Retry-After, follow the")
    print("server's pagination to its own total, cache with ETag, hash the payload")
    print("you used, and state the uncertainty of the number you computed from it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
