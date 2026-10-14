---
id: 03-13-07
title: "Consuming APIs and Web Services for Earth Data"
level: intermediate
prereqs: ["03-01-06", "03-13-06"]
estimated_minutes: 95
tags: [apis, http, json, fdsn, earth-data, caching, provenance, rate-limiting]
---

# Consuming APIs and Web Services for Earth Data

Almost every modern Earth-science dataset arrives over HTTP. Earthquake
catalogues come from the FDSN event services, waveforms from the dataselect
services, elevation and gravity grids from national archives, and reanalysis
fields from cloud object stores. The transport is unglamorous and largely
invisible when it works — which is the problem, because it fails in ways that
are silent, and a silently truncated catalogue produces a magnitude–frequency
curve that is wrong by an unknown amount.

This lesson teaches the transport by building a server. A local
`ThreadingHTTPServer` on the loopback interface implements the four behaviours
every real data service has and every naive client ignores: pagination, an
`ETag`/304 cache path, transient `503`s, and rate limiting with `Retry-After`.
The client that talks to it is measured on every axis that matters: bytes on the
wire, attempts, status histogram, and the provenance of the payload it finally
used. Because the server is local, nothing in this lesson touches the network —
and because it behaves like the real thing, everything in it transfers.

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** an HTTP request for an FDSN-style query and parse the JSON
   response, with the request parameters that determine the answer recorded.
2. **Follow** a service's pagination to its own reported total, and explain what
   a client that reads only the first page gets wrong.
3. **Implement** a conditional request with `ETag`/`If-None-Match`, measure the
   bytes it saves, and handle the 304 as a success.
4. **Retry** transient status codes with backoff, honour `Retry-After`, and say
   why the retry policy differs between a GET and a POST.
5. **Hash** a payload and record the URL, parameters and date, so that a derived
   result is reproducible even after the service's content changes.
6. **Distinguish** transport failures from data failures, and catch each with the
   right exception.

## Prerequisites

- [03-01-06 Files, I/O and Data Formats](../01-python-fundamentals/06-files-and-io.md)
  — reading and writing the payloads you download.
- [03-13-06 Git for Scientific Collaboration](./06-git-workflow.md) — why data
  belongs in an archive and the *fetch script* belongs in the repository.

## 1. What an Earth-data API is

The FDSN **event** service answers a query such as "all events with magnitude
≥ 4.5 between two dates in a bounding box" with a list of origin times,
hypocentres and magnitudes — in JSON, QuakeML XML, or plain text. The FDSN
**dataselect** service answers "give me the raw waveforms for these channels
between these times" with miniSEED. The FDSN **station** service answers "what
channels existed at this station in this window" with StationXML. The
specification is at the [FDSN](https://www.fdsn.org); well-known
implementations include the [USGS event service](https://earthquake.usgs.gov/fdsnws/event/1/),
the IRIS/EarthScope services at [service.iris.edu](https://service.iris.edu/fdsnws/event/1/)
and [ds.iris.edu](https://ds.iris.edu), and the client that most seismologists
actually use, [ObsPy](https://docs.obspy.org).

The shape of every one of them is the same: a URL with query parameters, a
paged response, an optional freshness token, and a documented rate limit. That
sameness is why a local mock server can teach the real thing.

### 1.1 The four behaviours that break naive clients

| Behaviour | Naive client's outcome |
|---|---|
| pagination with a `total` | silently truncated result; every statistic wrong by an unknown amount |
| `ETag` / 304 | either re-downloads everything, or crashes on a "304 error" |
| transient 503 | whole analysis fails on a two-second server hiccup |
| 429 with `Retry-After` | client hammering until the *laboratory's IP* is blocked |

Each of the four is implemented in the demonstration's eight-handler server, and
each is measured.

## 2. Requests and provenance

A request is a URL. A *reproducible* request is a URL plus the retrieval date
plus a hash of what came back. The demonstration fetches the whole synthetic
catalogue in one call and measures:

```
  payload: status 200, 20215 bytes
  sha256  : 408c5bf42ede503fc049449096cbe6ebd6e42d05f03c84a5fbfd471a62a1fd63
```

Record those three, and the derived result can be checked even if the service has
since changed — which it will have, because an earthquake catalogue is
append-only in time. This is the same argument as a commit hash in
[03-13-06](./06-git-workflow.md), applied to data you do not control:
**a URL is a query, not a dataset.**

`hashlib.sha256` over the raw response bytes is the right primitive. Hashing a
re-serialised JSON object is not: the key order, the float formatting and the
whitespace are all implementation details of the parser, and two byte-identical
responses can round-trip to different text. Hash the bytes you received.

## 3. Pagination: the failure that looks like success

The demonstration's catalogue has 137 events, served 25 at a time. Following the
pagination with `offset`/`limit` produced:

```
    page offset=   0 status=304 events= 25 total=137
    page offset=  25 status=200 events= 25 total=137
    page offset=  50 status=200 events= 25 total=137
    page offset=  75 status=200 events= 25 total=137
    page offset= 100 status=200 events= 25 total=137
    page offset= 125 status=200 events= 12 total=137
  events fetched: 137 (server total 137)   equal: True
```

Six requests, the last one short. The first page returned **304** because the
`ETag` cache from Section 2's fetch was still valid — a detail worth noticing,
because a client that treats 304 as an error would fail on its *second* pass
over the same query and not its first.

Two rules make pagination safe:

1. **Stop on the server's own `total`, not on an empty page or a short page.**
   A short page is usually the last, but a server-side limit, a filter, or a
   transient error can produce a short page mid-sequence. The `total` is the
   contract.
2. **Record the query, not the page.** The scientific unit is "all events
   matching this filter"; the page size is a transport detail that must not
   appear in a methods section.

The cost of getting this wrong is not a crash. It is a b-value computed from 25
events instead of 137, with a standard error five times too small, reported as a
result. Silent truncation is the single most damaging failure mode in
data-driven geophysics, and it is invisible in every plot.

## 4. Conditional requests: `ETag` and 304

Measured, for one 3729-byte catalogue page:

| exchange | status | bytes of body on the wire |
|---|---|---|
| first request | 200 | 3729 |
| second request with `If-None-Match` | 304 | **0** |

The server computes a digest of the body, sends it as `ETag`, and on a repeat
request with that value in `If-None-Match` replies `304 Not Modified` with no
body. The client's job is to serve its cached copy.

The trap is in the client library, not the protocol: measured with the standard
library,

```python
except urllib.error.HTTPError as exc:
    if exc.code == 304:
        # urllib raises HTTPError for 304 even though it is a success.
        return 304, self._cache[path]
```

`urllib.request` raises `HTTPError` for 304. That is defensible — it is not 2xx —
and it converts every cache hit into a crash unless special-cased. `requests`
(with `allow_redirects` and a session) has the same shape of problem via status
codes. **A 304 is a success and the payload is in your cache.**

Why it matters at the scale of geophysics: a waveform day-file for a single
broadband channel is tens of megabytes, and a regional study touches thousands.
Re-downloading files that have not changed is the difference between a
ten-minute and a ten-hour update, and for a metered or honour-system archive it is
a courtesy with a cost attached.

## 5. Transient failures and backoff

A `503` is the server saying "not now, try again". The demonstration's flaky
endpoint fails twice and then succeeds; the measured ladder, with no
`Retry-After` header sent (so the client had to choose):

| attempt | status | backoff chosen (s) |
|---|---|---|
| 1 | 503 | 0.020 |
| 2 | 503 | 0.040 |
| 3 | 200 | — |

The client starts at 20 ms and doubles. That is *exponential backoff*, and the
reason it is standard is that a server under load is made worse by clients that
retry immediately: a fixed 1 ms retry from a thousand clients is a denial of
service. Doubling spreads the load and gives the server time to recover.

Three details decide whether a retry policy is safe:

- **Which statuses to retry.** Retry `429`, `500`, `502`, `503`, `504` and
  transport errors. Never retry `400`, `401`, `403` or `404`: they will fail
  identically forever, and retrying them is just load.
- **How many attempts and how long.** An infinite retry with exponential backoff
  is a hang; a finite ladder with a cap (the demonstration caps at 0.5 s to keep
  the run short; production code should honour the server's value) is a policy
  you can state in a methods section.
- **Whether the request is idempotent.** A `GET` may be retried freely. A `POST`
  that starts a cluster job or charges a credit card must not be retried without
  an idempotency key, because a retry is a second job. This is a scientific
  decision about money and cluster time, not a style preference.

## 6. Rate limiting and `Retry-After`

The demonstration's limited endpoint returns `429 Too Many Requests` with
`Retry-After: 1`. Measured:

```
    server sent Retry-After: 1 s      (three times)
  final status 200: {"ok": true, "attempt": 4}
  attempts needed: 4
    status 429  waited 0.500 s  (asked for 1 s, capped to 0.5 s)
    status 429  waited 0.500 s  (asked for 1 s, capped to 0.5 s)
    status 429  waited 0.500 s  (asked for 1 s, capped to 0.5 s)
  total time spent waiting politely: 1.500 s
```

`Retry-After` is the server telling you the cheapest legitimate schedule. Two
things about the response shape are worth knowing: the value may be an integer
number of seconds or an HTTP date, so a client must parse both; and a client that
ignores it is not merely slow, it is likely to be blocked by IP — which means one
careless script takes out the whole laboratory's access, including the person who
wrote it.

The cap in the demonstration (0.5 s instead of 1 s) is a demo convenience and is
labelled as such in the output, because silently disobeying `Retry-After` would
be the wrong lesson. Production code should honour the value and apply a ceiling
only to protect against a hostile or broken server.

## 7. Errors: transport versus data

A connection to a port with nothing listening, measured:

```
  urlopen(http://127.0.0.1:9/fdsnws/...) raised URLError
  reason: ConnectionRefusedError(61, 'Connection refused')
```

[`urllib.error.URLError`](https://docs.python.org/3/library/urllib.request.html)
covers DNS failure, refused connections, timeouts and TLS problems. It is
unambiguously a *transport* failure and it is the exception to catch. The
distinctions that matter:

| exception | meaning | correct response |
|---|---|---|
| `URLError`, `socket.timeout` | transport | retry with backoff, or fall back to a local copy |
| `HTTPError` 4xx (except 429) | your request is wrong | fix the request; never retry |
| `HTTPError` 429 | too fast | honour `Retry-After` |
| `HTTPError` 5xx | server-side | retry with backoff |
| `json.JSONDecodeError` | the response is not what you asked for | log the body, do not retry blindly |
| `KeyError` on a parsed field | the schema is not what you assumed | fail loudly; the API changed |

The last two rows are data failures inside a transport success, and they are the
ones that silently corrupt results. An empty `events` list is a perfectly valid
JSON response that means "your filter matched nothing" — and a pipeline that
treats it as "no data available" and continues will happily fit a magnitude–
frequency curve to zero earthquakes. Assert the expected shape: a non-empty
list, a `total` that matches what you fetched, and the presence of the fields you
will read.

## 8. From bytes to a number, with its uncertainty

The demonstration ends where the science begins. From the fetched catalogue:

```
  events: 137   Mc = 2.5   events above Mc: 137
  mean magnitude excess: 0.4277
  Aki/Utsu maximum-likelihood b-value: 1.016
  Standard error estimate b/sqrt(N): 0.087
```

The estimator is the Aki–Utsu maximum-likelihood form

$$b = \frac{\log_{10} e}{\overline{M} - M_c}, \qquad
\sigma_b \approx \frac{b}{\sqrt{N}} ,$$

with $\overline{M}$ the mean magnitude of the events at or above the
completeness magnitude $M_c = 2.5$. The synthetic catalogue was generated with
$b = 1.0$ exactly, so the estimate 1.016 differs from the truth by 0.016 — well
inside the 0.087 standard error, which is the only honest way to report it.

Two points, both about honesty rather than method:

- **The standard error is the result.** "b = 1.016 ± 0.087" is a claim; "b =
  1.016" implies a precision that 137 events cannot deliver.
- **$M_c$ is estimated, not known.** Here it is the generation parameter, so the
  demonstration is a check of the estimator and not of the completeness analysis.
  In practice $M_c$ comes from the catalogue itself and carries its own
  uncertainty, which propagates into $b$. Stating which of the two you did is
  part of the methods section.

## 9. Python demonstration

```bash
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/apis_demo.py
```

Runs in about two seconds. It starts a `ThreadingHTTPServer` bound to
`127.0.0.1` on an ephemeral port, serves the synthetic catalogue and the three
failure-mode endpoints, and prints every table above plus the session accounting:

```
  successful/attempted requests: 16
  bytes actually downloaded    : 40,718
  bytes saved by the cache     : 7,458
    status 200: 9
    status 304: 2
    status 429: 3
    status 503: 2
```

A byte count and a status histogram are the two measurements that make an
API-dependent pipeline reviewable, and both are machine-independent — unlike a
runtime. Recording them per run turns "the update job sometimes hangs" into "the
histogram shows 400 responses this week where last week there were none".

### 9.1 What was not done

No external service was contacted. No real FDSN query was issued, no waveform
downloaded, no authentication performed, no DOI registered. Everything above is a
measurement of a local server with the same protocol behaviour. The FDSN URLs in
Section 1 are cited as documented endpoints; the lesson claims nothing about
their current content, availability or rate limits.

## 10. Assumptions and limits

- **A mock server is a specification, not an observation.** It implements the
  behaviours I chose to teach. It does not tell you what any particular archive
  does today.
- **`Retry-After` may be absent, integer or a date.** Handle all three.
- **Timeouts must be set explicitly.** The default is no timeout, which turns a
  hung server into a hung pipeline; an explicit timeout is a design decision.
- **Credentials are not covered here.** An API key does not belong in
  `git`-tracked code; it belongs in an environment variable documented in the
  README, with the failure mode (a clear error rather than a `None`) tested.
- **A hash proves identity, not correctness.** The same hash guarantees you
  analysed the same bytes as last time, not that those bytes are right.
- **Caching can hide updates.** An `ETag` cache is only correct while the
  server's `ETag` is a real content digest; a server that sends a constant one
  makes every client stale forever.

## 11. Common mistakes

1. Reading only the first page and computing a statistic from it.
2. Treating 304 as an error, so the second run of a script fails.
3. Hashing a re-serialised JSON object instead of the received bytes.
4. Retrying 4xx responses, which cannot succeed.
5. Retrying a non-idempotent POST and starting the job twice.
6. Catching `Exception` rather than `URLError`/`HTTPError`, which hides a
   `JSONDecodeError` that means the API changed.
7. Quoting a fitted parameter without the standard error, and without saying
   whether $M_c$ was assumed or estimated.
8. Committing the downloaded catalogue to the repository instead of the fetch
   script and the hash.
9. Leaving the timeout at its default, so a hung service becomes a hung cluster
   job.

## 12. Real-world applications

- **Regional seismicity studies.** Catalogue queries drive completeness analysis
  and magnitude–frequency statistics; pagination errors change $b$ and $M_c$
  without any visible symptom.
- **Waveform processing.** Dataselect requests are large, cacheable and
  rate-limited; a fetch stage that honours `ETag` and `Retry-After` is the
  difference between a maintainable pipeline and a nightly incident.
- **Reference models and grids.** Global relief, gravity and magnetic grids are
  published as versioned archive files with checksums. The repository should hold
  the download script, the URL, the version and the checksum — not the grid.
- **Cloud-hosted analysis.** The same protocol reasoning applies to object
  stores, with signed URLs and ranged GETs in place of `ETag`s; the failure modes
  and the provenance requirement are unchanged.

## 13. Further reading

- **FDSN.** <https://www.fdsn.org> Level: reference. The web-service
  specifications for event, station and dataselect, including the `offset`/`limit`
  and `nodata` semantics behind Section 3.
- **USGS Earthquake Hazards Program, FDSN event service.**
  <https://earthquake.usgs.gov/fdsnws/event/1/> Level: reference. The
  best-documented public catalogue endpoint.
- **IRIS/EarthScope.**
  [event service](https://service.iris.edu/fdsnws/event/1/) and
  [dataselect](https://service.iris.edu/fdsnws/dataselect/1/), with bulk
  archives at [ds.iris.edu](https://ds.iris.edu). Level: reference.
- **ObsPy.** <https://docs.obspy.org> Level: library. The FDSN clients
  (`obspy.clients.fdsn`) implement pagination, retries and StationXML parsing so
  that you rarely hand-roll them — and reading their source is the fastest way to
  learn the details.
- **Python standard library.**
  [`urllib.request`](https://docs.python.org/3/library/urllib.request.html),
  [`http.server`](https://docs.python.org/3/library/http.server.html),
  [`hashlib`](https://docs.python.org/3/library/hashlib.html),
  [`json`](https://docs.python.org/3/library/json.html). Level: reference.
- **Aki, K. (1965). Maximum likelihood estimate of b in the formula log N = a − bM
  and its confidence limits. *Bull. Earthquake Res. Inst. Univ. Tokyo*, 43,
  237–239.** Level: advanced. The source of the estimator in Section 8.
- **Utsu, T. (1965). A method for determining the value of b in a formula
  log n = a − bM showing the magnitude–frequency relation for earthquakes.
  *Geophys. Bull. Hokkaido Univ.*, 13, 99–103.** Level: advanced. The
  independent derivation of the same estimator.

> Note on citations: bibliographic details are given so you can locate the
> works. This repository does not host or reproduce copyrighted text.

## 14. Related lessons

- [03-13-06 Git for Scientific Collaboration](./06-git-workflow.md) — what
  belongs in the repository, and why a fetch script is the right artefact.
- [03-13-08 Reproducible Environments](./08-reproducible-environment.md) —
  recording the versions under which a fetched payload was analysed.
- [03-13-02 Testing Numerical Code Against Analytic Solutions](./02-testing-scientific-code.md)
  — the estimator in Section 8 is checked against its generating parameter, the
  verification pattern of that lesson.
- [03-13-01 pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons](./01-pytest-basics.md)
  — a mock server makes a network client testable offline, which is the point of
  this lesson's construction.
- [03-10-08 FDSN Clients and Web Services](../10-obspy-and-seismic-data/08-fdsn-clients.md)
  — the ObsPy-level treatment of the services introduced here.

## 15. Self-assessment checklist

- [ ] I can construct an FDSN-style query and state why the parameters must be
      recorded with the result. (§2)
- [ ] I can follow pagination to the server's total, and explain the failure mode
      of stopping early. (§3)
- [ ] I can implement a conditional request and handle 304 as a success. (§4)
- [ ] I can choose a retry policy per status class, and say which requests must
      not be retried. (§5)
- [ ] I can honour `Retry-After` in both its formats. (§6)
- [ ] I can distinguish a transport failure from a data failure and catch each
      with the right exception. (§7)
- [ ] I can record the provenance of a payload so a derived result is checkable.
      (§2, §9)
- [ ] I can report a fitted parameter with its standard error and say whether the
      completeness magnitude was assumed. (§8)
