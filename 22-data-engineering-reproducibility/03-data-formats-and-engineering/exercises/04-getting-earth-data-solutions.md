# Solutions — 22-03-04 Programmatic Access to Earth Data (FDSN, Earthdata, Copernicus)

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [04 Programmatic Access to Earth Data](../04-getting-earth-data.md).

---

## ★1 — Query versus file

1. **The result depends on when it is asked.** A service returns what it currently
   holds, processed by the software version it currently runs, so the same query
   returns different bytes after a reprocessing. Without a retrieval timestamp and the
   service's processing version, a later discrepancy cannot be attributed.
2. **Completeness is not implied by success.** A response that contains part of the
   requested window is delivered without error and is indistinguishable from a
   complete one unless the plan states what was expected and a gate compares. Without
   the request list, nothing can be reconciled.

## ★2 — The 7-day window plan

(a) Requests $= \lceil 365/7 \rceil = 53$. Latency $= 53 \times 1.0 = 53.0$ s.
Transfer $= (365 \times 40)/5 = 2920.0$ s.

(b) Total $= 53.0 + 2920.0 = 2973.0$ s, matching the printed value. The 1-day plan
takes $365 \times 1.0 + 2920.0 = 3285.0$ s, so the 7-day window saves 312 s of pure
overhead for identical data.

(c) The window length controls the **request count and therefore the latency term**;
the transfer term is fixed by the volume. At the 30-day cap the latency term falls to
13.0 s and the saving reaches 352 s.

## ★3 — Five fields of a reproducible fetch

| Field | Question it answers |
|---|---|
| the plan (windows, extents, channels, level) | what exactly was asked for |
| the service identity, including its processing version | what the service was, and which processing produced the response |
| the retrieval timestamp (UTC) | when it was asked, so a difference can be dated |
| a checksum per response | whether the bytes you hold are the bytes that arrived |
| the failure and retry log | which windows failed and their terminal outcome |

A checksum answers "is this the response?"; only the first three answer "what was
asked, of what, and when?" — the questions that decide whether a difference is your
bug or the service's reprocessing.

## ★★4 — A 500-day fetch at the 10-day cap

(a) Requests $= \lceil 500/10 \rceil = 50$. Latency $= 50 \times 2 = 100.0$ s.
Transfer $= (500 \times 20)/4 = 2500.0$ s. Total $= 2600.0$ s.

(b) With 1-day windows: 500 requests $\times 2$ s $= 1000.0$ s of latency, the same
2500.0 s of transfer, total 3500.0 s. The cap saves $1000 - 100 = 900$ s, i.e. 26 % of
the plan's time.

(c) The assumption: that a 10-day response is **homogeneous and complete** — the same
channels, sampling and processing level across the window, and no gaps. If the service
occasionally returns a partial window, a large window hides the gap inside a
successful response, which is worse than many small failures that can be counted. Note
also the rate limit: 50 requests is trivially within any plausible limit, so the
latency term here is genuinely latency, not throttling.

## ★★5 — Failure probability of a multi-request fetch

(a) $P(\text{at least one failure}) = 1 - (1-0.06)^{25} = 1 - 0.94^{25} =
1 - 0.2129 = 0.7871$.

(b) Expected attempts per request $= 1 + 0.06 + 0.0036 = 1.0636$. Extra attempts
$= 0.0636$ per request, so $25 \times 0.0636 = 1.59$ extra requests; at 1.2 s each
that is 1.9 s of extra latency — negligible against a plan whose transfer dominates.

(c) The check is a **completeness gate against the plan**: the plan knows how many
windows were requested and what each should contain (a row count, a byte size, a
station-day count), and the pipeline asserts that every window arrived. Retries are
insufficient because a request that failed all attempts raises no error by the end of
the run — the fetch simply lacks that window — and because a response can be
delivered while being *incomplete* (a truncated body), which no retry logic can detect
without a content check.

## ★★6 — Two runs, 0.8 % different

Three consistent explanations:

1. **Service-side reprocessing.** The archive's magnitudes, station metadata or
   calibrations changed between the two months, so the query returns different data.
2. **Service-side completeness.** New stations, newly digitised records or late
   arrivals changed the data set for the same period.
3. **Different selection on your side.** A query that used "latest" metadata, a
   moving availability window, or an unpinned list of stations returns a different
   subset.

The distinguishing record: the **service's processing version identifier and the
retrieval timestamps** for both runs, plus the **response checksums**. If the checksums
of the responses (per window) differ, the data changed at the service; if the plan or
the station list differs, the change is yours. Without those fields, the 0.8 % cannot
be attributed, and the analysis cannot claim which version of the world it used.

## ★★★7 — Fetch layer for three services

**Assumptions to state up front** (chosen, since real limits must be read): waveform
service with a 1-day cap and 5 MB/s at 1 s latency, 12 MB/day/station; catalogue
service with a 30-day cap, negligible payload; reanalysis service with granule-level
objects of 400 MB each, 20 MB/s.

**Waveform plan.** 120 stations × 540 days $\approx 64\,800$ station-days. With a
1-day cap and per-station requests, requests $= 64\,800$; latency $= 64\,800$ s
(18 h); volume $= 64\,800 \times 12\ \text{MB} = 777.6$ GB at 5 MB/s $= 43.2$ h.
Total $= 61.2$ h of serial fetching — so **the plan must be parallelised**: at 8
concurrent streams the wall time falls to about 7.7 h (subject to the rate limit),
which is the same worker-count arithmetic as
[22-02-03](../../02-reproducible-workflows/03-workflow-managers.md) §5. The correct
fetch unit is one station-day, so that failures are re-runnable at that granularity.

**Catalogue plan.** 18 months at the 30-day cap: 18 requests, negligible payload;
fetch, then check the event count against the service's reported total for the query.

**Reanalysis plan.** Granule-level fetch by identifier, 18 months of daily fields: at
400 MB per granule and, say, 550 granules, 220 GB at 20 MB/s $= 3.1$ h. Identifiers
make this the most reproducible of the three: the plan lists granules, not a query.

**Adapters.** One thin module per service, each translating a single request
specification (window, channels, level) into the service's parameters and returning a
response plus metadata; tested with recorded fixtures so the adapter's behaviour can be
checked without calling the service.

**Caching and archive.** Raw responses are archived content-addressed
([22-02-05](../../02-reproducible-workflows/05-data-versioning.md)) with the fetch record
of §5 beside them; derived products are regenerated from the archive, never from a
re-query. Staging is per station-day so a retry is a small write.

**Completeness gate per service.** Waveforms: station-days expected vs station-days
archived, plus a per-file byte-size sanity range. Catalogue: event count and a
checksum over the event identifiers. Reanalysis: the granule list from the plan vs the
granules archived, and a per-granule checksum.

**What you cannot control.** The service's processing version and its future changes:
a reprocessing over the study period will make the archived bytes and the live service
disagree, which is why the archive (not the service) is the reference for the figure.

## ★★★8 — Characterising a real service's limits

**What you probe.** A small sequence of requests varying one factor at a time on a
harmless target (a short window, a tiny station): (i) request size — window length and
payload — to find the *cap*; (ii) request rate — a short burst at increasing
frequencies, stopping at the first throttle response, to find the *sustainable rate*
and the backoff behaviour; (iii) recovery — how long until the throttle lifts; and
(iv) concurrency — whether several parallel connections share one limit or each get
their own.

**Statistic.** The maximum window that returns a complete response (the effective
cap); the request rate at which the first 429-type throttle appears, and the largest
rate that sustains for several minutes without throttling (a conservative operating
point); and the recovery time constant after a throttle. Record the timing of every
probe — with a date — because limits change.

**Cost of the probe.** A few dozen to a few hundred small requests: minutes, and
negligible data. The cost that matters is social: probing a public service is a guest's
behaviour, and it should be done once, gently, with an identifying contact string, not
by every member of a group independently.

**Two ways the measurement could mislead.**

1. **Probing an empty service.** Limits and latencies measured on a quiet service
   (2 a.m., off-season) are not the limits at peak; the effective cap can be tighter
   and the latency longer.
2. **Assuming the limit is yours.** Rate limits are often enforced per key or per
   address, so a measurement made from a laptop does not describe what the group's
   cluster nodes can do — and a shared institutional address may already be near a
   limit set by other users' traffic.

**What to do with the result.** Record it in the fetch record and, better, in the
adapter's configuration with the date and the probe method, use a conservative
fraction of the measured sustainable rate (say half), implement backoff that respects
throttle responses rather than a fixed rate, and re-measure when fetches start failing
or slowing — limits change, and an old measurement is a hypothesis.

## ★★★9 — Surviving a service reprocessing

**Repository practice.** For every archived ingest, record the five fields of §5 —
plan, service and **processing version**, retrieval timestamp, per-response checksums,
failure log — and keep the ingested bytes themselves (not only the derived products)
so a figure can be regenerated from the exact data. Tag each published result with the
ingest identifier (a hash of the fetch record) so that a paper's figure names the
exact ingest, and record the service's announced change in a changelog entry that
points at the ingest records it affects.

**What this costs per year for a 2 TB/year ingest.** Storage of 2 TB/year (plus the
derived products already kept), the checksum and metadata records which are small
relative to the data, and the operational cost of keeping the archive readable. Over
ten years an uncompressed 20 TB is a real but ordinary figure for a group with a data
plan; the alternative — re-querying and not knowing what changed — costs a
re-analysis at best. Note that the *derived* products can be regenerated, so the
irreplaceable part is the raw fetch: keeping only the derived products is the choice
that makes the practice impossible.

**What the practice cannot guarantee.** That the reader will be able to *interpret* the
old processing — if the service's change log is vague ("improved calibration") the
difference between old and new data is not fully explainable, and the honest report is
then "the result used the pre-reprocessing ingest, which differs from the current
service in ways the service documents only approximately". It also cannot preserve the
bytes if the archive is lost: the practice needs a backup and a retention commitment
([22-05-04](../../05-collaboration-and-project-management/04-research-data-management-plan.md)).
