# Solutions — 03-13-07 Consuming APIs and Web Services for Earth Data

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; derived values are shown with the arithmetic
> that produced them. No external service was contacted.

---

## ★1 — Pagination and accounting

**(a)** $\lceil 137/25 \rceil = 6$ pages. The last page carries $137 - 5\times25
= 12$ events, which is the 12 in the demo's output.

**(b)** Two ways a short page truncates the result: (i) a **server-side cap** below
your requested `limit` — the service honours its own maximum, so *every* page is
short and the client stops after one; and (ii) a **transient error or rate limit
mid-sequence** that returns a valid-looking but short page (or an empty one). The
rule that is always correct is to stop when the number of events accumulated
reaches the server's reported `total`, and to treat any other discrepancy as an
error rather than as the end of the data.

**(c)** Because byte counts and status histograms are integers produced by the
program's interaction with the service, and reproduce exactly for the same
sequence of responses. A runtime depends on the network, the server's load, the
client's machine and the time of day. The practical consequence is the same as
elsewhere in this module: the counts can go in a log, be compared between runs,
and be asserted in a test; the runtime cannot.

---

## ★2 — Conditional requests

**(a)** The server sent `ETag: "8efb979a8b909c089a90e7780cccf070"` — a digest of
the body — together with the body. On the repeat request the client sent
`If-None-Match: "8efb979…"`, and the server replied 304 with no body.

**(b)** Because 304 is not 2xx, and `urllib.request` raises `HTTPError` for any
non-2xx status. The client must special-case it *before* the general error
handling, and return the cached payload as a success:

```python
except urllib.error.HTTPError as exc:
    if exc.code == 304:
        return 304, self._cache[path]
    ...
```

Forgetting this converts every cache hit into a crash, so the failure appears on
the *second* run of a script, not the first — a diagnostic pattern worth
recognising.

**(c)** Because waveform requests are two to three orders of magnitude larger.
A catalogue page here is 3729 bytes; a broadband day-file is tens of megabytes,
and a regional study touches thousands of them. Re-downloading unchanged files
dominates the update time, and for an archive operating on an honour system or a
metered link it is a real cost to someone else. The `ETag` exchange turns an
unchanged file into a zero-byte response.

---

## ★3 — Error taxonomy

| error | class | correct response |
|---|---|---|
| `URLError` / `ConnectionRefusedError` | transport | retry with backoff, or fall back to a local copy |
| `HTTPError` 403 | request/credential | do not retry; fix the credential or the request |
| `HTTPError` 429 with `Retry-After: 30` | rate limit | wait 30 s (or the parsed date) and retry, with a bounded attempt count |
| `HTTPError` 503 | server-side transient | retry with exponential backoff |
| `json.JSONDecodeError` | data | log the body and the content type; do not retry blindly — the response was not what you asked for |
| empty `events` with `total: 0` | data | a valid response meaning "the filter matched nothing"; assert it explicitly rather than treating it as absence of data |

The last two rows are the important ones: they are data failures *inside* a
transport success, and they are the class that silently corrupts results.

---

## ★4 — Retry policies

**(a)** Three attempts, delays 0.020 s and 0.040 s before the second and third —
i.e. doubling from a 20 ms base. The third delay, had a fourth attempt been
needed, would have been 0.080 s. Measured ladder: 503 (0.020), 503 (0.040), 200.

**(b)** Production code must honour the server's value: wait the full second, and
apply a ceiling only to protect against a hostile or broken value (e.g. cap at
300 s rather than at 0.5 s). The demo caps at 0.5 s purely so the exercise
finishes in seconds, and the cap is printed in the output — *"asked for 1 s,
capped to 0.5 s"* — precisely so that nobody reads the demonstration as advice to
disobey the header. This is the general principle for teaching code: when a
demonstration deviates from correct practice for a practical reason, the deviation
is announced in the output rather than left for the reader to notice.

**(c)** Three problems, one per class: (i) retrying **4xx** codes is pointless
load — a 403 will fail identically forever, and 50 ms of retries per request
multiplied by thousands of requests is a self-inflicted rate limit; (ii) ignoring
**`Retry-After`** on a 429 is what gets an entire laboratory's IP blocked, and a
fixed delay makes the block more likely rather than less; (iii) a **fixed 50 ms**
delay does not give a struggling server time to recover, so retrying 503s at a
constant rate converts a transient overload into a sustained one. Only transient
statuses deserve retries, and they deserve backoff.

---

## ★5 — Provenance

**(a)** The four items: the **URL including every query parameter**, the
**retrieval date and time (with time zone)**, the **response byte length**, and
the **sha256 of the raw bytes**. Optionally the status code and the service's own
reported total. Those four are enough for another person to re-issue the same
query and check whether the content is the same.

**(b)** Because the byte stream is the artefact. Re-serialising means parsing JSON
into a dict and writing it back, and the output depends on key ordering, float
repr, unicode escaping and whitespace — all implementation details of the parser.
Two *different* byte streams can round-trip to the same text, and two identical
byte streams can round-trip to different text across versions. Hash what you
received:

```python
digest = hashlib.sha256(response.read()).hexdigest()
```

**(c)** An earthquake catalogue is **append-only in time**: a later revision
contains events the earlier one did not, and often revises the magnitudes of
events it already had. So the same URL returns different content next month, and
"the URL determines the content" is false for exactly the datasets this lesson is
about. The hash is what lets a reader distinguish "same data, new analysis" from
"new data, same analysis" — a distinction that no amount of code archiving can
recover.

---

## ★6 — Reporting a $b$-value

**(a)** $\sigma_b = b/\sqrt{N} = 1.016/\sqrt{137} = 0.08680$, i.e. **0.087**.

**(b)** $M_c$ (the completeness magnitude) was **assumed known**: the demo shows
$M_c = 2.5$, which is the generating parameter of the synthetic catalogue, and
reports the estimator's ability to recover $b$ given a correct $M_c$. If $M_c$ is
wrong by 0.1 the estimate moves a great deal: the mean magnitude excess changes
from 0.4277 to 0.3277, and

$$b = \frac{\log_{10} e}{\overline{M} - M_c} = \frac{0.4343}{0.3277} = 1.325 .$$

A 0.1 error in a quantity most analyses *estimate* changes the reported $b$ by
**0.31**, which is 3.6 times the 0.087 statistical standard error. The systematic
error dominates the statistical one, which is the single most important thing to
know about $b$-value estimates and the thing a bare "1.016" conceals.

**(c)** The correct report is the value, the statistical uncertainty, and the
completeness assumption with its own uncertainty:

> "$b = 1.02 \pm 0.09$ (statistical, Aki–Utsu maximum likelihood, $N = 137$
> events above $M_c = 2.5$)."

A reviewer should ask **how $M_c$ was determined, and what the estimate becomes
for $M_c \pm 0.1$** — which is the sensitivity calculation in (b). A paper that
cannot answer it has reported a number whose dominant uncertainty is unstated.

---

## ★7 — A fetch stage for 3000 files

**(a)** Store the payloads content-addressed by their `sha256`, with a small
sidecar JSON per URL recording the `ETag`, the byte length and the fetch time.
On each run, send `If-None-Match` with the stored `ETag`; a 304 means the cached
file is current, and nothing is transferred. Because the files are large and
change rarely, this converts a full re-download of 90–180 GB into 3000
zero-byte responses plus a handful of real transfers. The content-addressed name
also makes the cache self-verifying: if a transfer is truncated, the digest will
not match the name.

**(b)** Retry only `429`, `500`, `502`, `503`, `504` and transport errors; honour
`Retry-After` when present; otherwise exponential backoff from 1 s with 100%
jitter, capped per attempt at 60 s and with a **maximum total wait per file of
10 minutes** (so the whole run cannot hang indefinitely). When the budget is
exceeded, record the URL and the final status in a `failed.txt` and continue —
the job exits non-zero at the end with the count. Concurrency should be a fixed
small number (2–4) rather than "as many as possible", because the rate limit is
per IP and the archive's other users are competing with you.

**(c)** Log, per run: the **status histogram** (200/304/429/503 counts) and the
**total bytes downloaded**, plus the list of failed URLs. Neither is a runtime:
the histogram distinguishes "the archive is throttling us" (a rise in 429) from
"the archive is unhealthy" (a rise in 503) from "our cache stopped working" (a
fall in 304 and a rise in 200), and the byte count says how much load we imposed.
A runtime rise could have any of those causes; the counts localise it.

---

## ★8 — The silent truncation

**(a)** The pipeline conflates **"the query matched nothing"** with **"the client
failed to retrieve what matched"**. The first has causes the second does not: a
genuinely empty region/time window, or a magnitude filter above the catalogue's
completeness level. The second has causes the first does not: a pagination bug, a
rate-limit response the client did not detect, a schema change that moved the
`events` key, or an authentication failure returning an empty document instead of
a 401.

**(b)** The assertion belongs immediately after the fetch, and it asserts the
*server's* accounting rather than the client's:

```python
payload = json.loads(body)
assert payload["total"] >= 0
fetched = fetch_all_pages(...)
assert len(fetched) == payload["total"], (len(fetched), payload["total"])
assert payload["total"] > 0, "empty region: confirm the filter before proceeding"
```

The first two lines catch truncation and schema drift; the third forces the
empty case to be an explicit decision recorded in the pipeline rather than a
default that silently continues.

**(c)** Because the output of a magnitude–frequency fit on $n$ events is a
*plausible* curve for any $n$: $b$ is estimable from 5 events, so the plot looks
like a seismicity result, and the standard error — the thing that would reveal
the small $n$ — is usually not plotted. The failure is invisible in the figure and
visible only in a count, which is why the assertion belongs in the pipeline rather
than in the analysis.

---

## ★9 — The mock server

**(a)** Two differences the lesson does not measure, and how to determine each:
(i) the **real pagination semantics** — some services use `offset`/`limit`, others
use a cursor or a `starttime` window, and some cap `limit` below your request;
determine it by reading the service's specification and by probing with
`?limit=20000` and observing what comes back and what `total` says. (ii) the
**real rate limit and its enforcement** — the documented limit may differ from the
enforced one, and enforcement may be per IP, per token or per day; determine it
from the service's documentation *and* from the status histogram of an actual
run, which is the measurement in Section (b) of the previous exercise.

**(b)** Because a local server is the only way to test a client *deterministically*
and *offline*. It can be made to return 429 on demand, to fail with 503 exactly
twice, and to hold a hostile `ETag`; every assertion about the client's behaviour
then becomes reproducible, and the test suite runs in CI with no network. A test
against a live archive cannot do any of that: it is slow, flaky, rate-limited, and
it cannot produce a 503 on request.

**(c)** It can never verify that the *client's assumptions about a particular
archive* are correct — the mock is our specification, and it is right by
construction. The experiment that would verify it is a **scholarly-catalogue
cross-check**: fetch a small, well-understood region and period from two
independent implementations, and compare the event counts and magnitudes. That is
a validation, in the sense of the testing lesson, and no amount of mock-server
testing substitutes for it.
