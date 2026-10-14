# Exercises — 03-13-07 Consuming APIs and Web Services for Earth Data

Attempt these **closed-book** before opening the
[solutions](./07-apis-and-web-data-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems marked **[demo]** refer to
[`../code/apis_demo.py`](../code/apis_demo.py), which runs a local mock FDSN
service — **no network access is used or required**:

```
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/apis_demo.py
```

The lesson is [`../07-apis-and-web-data.md`](../07-apis-and-web-data.md).

---

## ★ Foundational

**★1. [demo]** The pagination and accounting output is

```
    page offset=   0 status=304 events= 25 total=137
    page offset= 125 status=200 events= 12 total=137
  events fetched: 137 (server total 137)   equal: True
  bytes actually downloaded    : 40,718
  bytes saved by the cache     : 7,458
    status 200: 9
    status 304: 2
    status 429: 3
    status 503: 2
```

(a) The catalogue has 137 events at 25 per page. How many pages are required, and
how many events does the last page carry?
(b) A client stops when a page returns fewer than `limit` events. State two
circumstances in which that rule truncates the result, and the rule that is
always correct.
(c) State why the byte count and the status histogram are reviewable measurements
while a runtime is not.

**★2. [demo]** The conditional-request measurements are

```
  first request : status 200,  3729 bytes, ETag "8efb979a8b909c089a90e7780cccf070"
  second request: status 304,  3729 bytes of body
  bytes on the wire for the second request: 0
```

(a) State what the server sent in the first response that enables the second
exchange, and what the client sent back.
(b) Explain why `urllib.request` raises an exception on a 304 and what a client
must do about it.
(c) State the scientific reason an `ETag` cache matters for waveform requests
rather than only for catalogues.

**★3.** Classify each and state the correct response: (a) `URLError` with
`ConnectionRefusedError`; (b) `HTTPError` 403; (c) `HTTPError` 429 with
`Retry-After: 30`; (d) `HTTPError` 503; (e) `json.JSONDecodeError`;
(f) an empty `events` list with `total: 0`.

---

## ★★ Applied

**★★4. [demo]** The retry and rate-limit ladders are

```
  /v1/flaky   503   backoff 0.0200 s
  /v1/flaky   503   backoff 0.0400 s
  /v1/flaky   200

    status 429  waited 0.500 s  (asked for 1 s, capped to 0.5 s)   x3
  total time spent waiting politely: 1.500 s
```

(a) State the retry policy for the flaky endpoint, in terms of attempt count and
delay sequence, and say what the third delay would have been.
(b) The rate-limited endpoint sent `Retry-After: 1`. The demo waited 0.5 s. State
what production code must do instead and why the demo's cap is labelled in the
output.
(c) A colleague's fetch stage retries every status code twice with a fixed 50 ms
delay. State three distinct problems with that policy, one per status class.

**★★5. [demo]** The demo's payload provenance is

```
  payload: status 200, 20215 bytes
  sha256  : 408c5bf42ede503fc049449096cbe6ebd6e42d05f03c84a5fbfd471a62a1fd63
```

(a) Write the four-item provenance record a methods section needs for this
payload.
(b) Explain why hashing a re-serialised JSON object is the wrong primitive.
(c) A colleague argues that the hash is unnecessary because the endpoint URL
determines the content. Refute that in two sentences, referring to a property of
an earthquake catalogue.

**★★6.** The b-value estimate is `b = 1.016` with standard error
`b/sqrt(N) = 0.087` from 137 events.

(a) Recompute the standard error from the measured b and N.
(b) State which of the two components of the estimate — $b$ or $M_c$ — was
assumed known in the demo, and how the estimate changes if $M_c$ is wrong by 0.1.
(c) State the correct way to report the result, and what a reviewer should ask
about $M_c$.

---

## ★★★ Research-oriented

**★★★7.** You must build a fetch stage for 3000 broadband day-files, each 30–60 MB,
from an archive that returns 429s under load and 503s occasionally.

(a) Design the caching strategy, naming the header exchange and the storage layout.
(b) Design the retry policy, including the maximum total wait and what happens
when it is exceeded.
(c) State the two measurements you would log per run so that a later slowdown is
diagnosable, and explain why neither is a runtime.

**★★★8.** A pipeline treats an empty `events` list as "no data available" and
continues to the next region.

(a) Explain the two defect classes this conflates, and for each give a cause that
the other does not cover.
(b) State the assertion that distinguishes them, and where it belongs in the
pipeline.
(c) State why this defect is invisible in every plot the pipeline produces.

**★★★9.** The lesson's mock server is a specification of four behaviours, not an
observation of any archive.

(a) State two ways in which a real FDSN service differs from the mock in ways the
lesson does not measure, and how you would determine each.
(b) Explain why teaching with a local server is nevertheless the right choice, in
terms of what a test suite can assert.
(c) State the one thing a mock server can never verify, and the experiment that
would.
