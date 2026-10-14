# Solutions — 22-03-03 Designing Robust Data Pipelines for Earth Data

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [03 Designing Robust Data Pipelines](../03-data-pipelines.md).

---

## ★1 — End-to-end success

$$P(\text{success}) = \left(1 - p^{R+1}\right)^{N}.$$

"Independent" assumes that a stage's failure is not caused by the same event that
fails another stage — no shared service, shared credential or shared network path.
When that assumption fails (one catalogue service used by six stages), the product
understates the risk of a correlated outage and the retries multiply a dependency
rather than a flake.

## ★2 — The demonstration's numbers

(a) No retries: $0.98^{8} = 0.8508$, i.e. **85.1 %** end-to-end, matching the printed
0.8508.

(b) With retries: stage success $= 1 - 0.02^{4} = 1 - 1.6 \times 10^{-7} =
0.99999984$; end-to-end $= 0.99999984^{8} = 0.9999987 \approx 0.999999$, the printed
value.

(c) It is not exactly 1 because a stage that fails all four attempts still fails: the
retry policy multiplies the failure probability ($p^{R+1}$) rather than removing it,
and eight stages multiply their (tiny) residuals again.

## ★3 — Idempotence

| Stage | Idempotent? | Why |
|---|---|---|
| download overwriting its target | yes | the same bytes are written to the same place; the second run changes nothing |
| counter increment | no | the value depends on how many times the stage ran |
| table append | no | each run adds a row; two runs add two |
| file overwrite | yes | content is replaced, not accumulated |
| message emission | no | the consumer sees two messages |

## ★★4 — Cost of retries

(a) $\mathbb{E}[\text{attempts}] = 1 + 0.02 + 0.0004 + 0.000008 = 1.020408$,
the printed value.

(b) $8 \times 1.020408 = 8.1633$ stage attempts per run, against an ideal of 8.

(c) Waste $= (8.1633 - 8)/8 = 2.041\ \%$, the printed value. The rule: the cost of a
retry policy is approximately the per-attempt failure probability, to first order,
because the geometric series' first correction term is $p$. Setting retries is
therefore almost always cheap — until $p$ is large, or until the retried stage's
duplicate side effects are expensive rather than merely extra work.

## ★★5 — Duplicate rows from a retried append

(a) Expected duplicates per 10 000 station-days: each attempt fails with
$p = 0.01$ (delivery 99 %), and a failed attempt is retried with a 50 % chance of the
duplicate being delivered:

$$10\,000 \times 0.01 \times 0.5 = 50\ \text{duplicate rows}.$$

The point is the scale, not the exact constant: **50 duplicated rows per 10 000** is
invisible in a table of millions and fatal to any sum, mean or count taken over it.

(b) The schema change: a **primary key** on the natural key (station, day) with an
upsert (replace-by-key) write, so a second delivery overwrites rather than appends.
Alternatively a unique constraint that rejects the duplicate and logs it — either
converts a silent double count into a well-defined state.

(c) Without the change, a reader sees a table whose row count exceeds the station-day
count, whose per-station totals are inflated by an unknown amount, and whose excess
rows are indistinguishable from genuine repeated measurements (which are common in
real archives). Nothing in the table says which rows are duplicates; only a
reconciliation against the source would reveal them.

## ★★6 — A nightly shortfall

(a) The **silently lost record** pattern of §6: a request whose response never
arrived, or a write that failed without raising, gives no error for a retry to act on.
The modelled silent-loss rate (0.00997 of stage-attempts) is the same order as the
duplicate rate, which is exactly why a retry-only reliability strategy misses it.

(b) The gate: at the end of the ingest, compare (i) the number of source records the
service reported for the requested window, (ii) the number of rows written, and
(iii) a checksum or key-set digest over the written rows against the same over the
fetched payload. Fail the job if (i) $\ne$ (ii) or the digests differ, and record
both numbers in the run's provenance record so a repair can be planned.

(c) The modelled 7.71 % of 100 000 runs containing at least one silent loss is a
scaled version of the same phenomenon; for a nightly job that is roughly one night in
thirteen. The gate does not change the frequency of the loss — it changes the
frequency of *noticing* it, from "a user finds it months later" to "the job fails at
03:00 and is rerun".

## ★★★7 — Reliability architecture for 200 stations from three services

**Stage decomposition.** (1) `plan` — enumerate the station-day windows per service;
(2) `fetch_<service>` — one rule per service (three rules), each fetching its windows
into a staging area keyed by window identifier; (3) `validate_<service>` — per-service
count and checksum gate; (4) `normalise` — map each service's records onto the common
station-day schema; (5) `write` — upsert into the archive keyed by (station, day,
channel); (6) `reconcile` — compare the archive's coverage with `plan`'s expected
station-day count per service; (7) `report` — emit the run's provenance record and
gate results.

**Where idempotence or deduplication is required.** `fetch_<service>` writes to a
staging path keyed by the window identifier, so a retry overwrites (idempotent).
`normalise` is a pure function of its input (idempotent). `write` **must** upsert on
the natural key, because it is the stage that a retry would otherwise duplicate — the
one stage where the design decision is unavoidable. `reconcile` and `report` are
read-only or replace-by-name.

**Retry and backoff policy.** Per-request retries with exponential backoff and jitter,
capped at three attempts for the flaky service and fewer for the reliable ones; a
per-service circuit breaker so that a service outage fails its branch quickly instead
of consuming the run's budget; and no retry at all for permanent failures (a malformed
station identifier), which go to a quarantine list with a report.

**Failure semantics promised to users.** The archive is **at-least-once per window**
and, because of the upsert key, **exactly one row per (station, day, channel)** in
the archive; a window that failed every attempt is *absent* and appears in the run
report and in a coverage table, never as a zero or an empty record. Users are told to
treat the coverage table as the authority on what exists.

**The failure the design cannot prevent.** A silent loss inside a service that also
misreports its own record counts: the gate compares against the service's claim, and a
service that is confidently wrong defeats it. The only mitigation is cross-validation
against an independent source or against the station's own metadata expectations — a
check that costs a second data source.

## ★★★8 — Measuring dependence in failures

**Data.** The pipeline's own logs: for each run, the sequence of stage attempts with
timestamps, the stage identity, the service/endpoint called, and the outcome; plus
the service's status timeline if available.

**Statistic.** Compare the observed distribution of **failures per run** with the
independence prediction. Under independence with stage-failure probability $p$ and 8
stages, the number of failures per run is binomial$(8, p)$ — or Poisson-ish with
variance $\approx 8p$ — and, more sharply, failing pairs should be independent
(observed co-failure rate $\approx p^{2}$). Two usable measures:

1. **Over-dispersion**: the variance of the failures-per-run count divided by its
   mean (the index of dispersion). A value near 1 is consistent with independent
   flakiness; a value substantially above 1 indicates clumping.
2. **Excess co-failure**: for each pair of stages, the ratio of observed joint
   failures to $n\,p_i p_j$. A pair whose ratio is far above 1, and whose failures
   share timestamps within a short window, is correlated.

**Pattern that identifies a service outage.** A small number of runs with many
simultaneous failures (high index of dispersion), concentrated in the stages that call
one endpoint, with inter-arrival times clustered rather than exponentially
distributed. Real flakiness produces isolated, independently timed failures; an outage
produces a burst.

**How the policy should change.** With dependence confirmed, per-stage retries do
almost nothing (they all fail together during the outage) and their cost is paid
regardless. The response is to (i) **serialise** the calls to the failing service
rather than hammering it, (ii) **defer** the affected branch with a scheduled retry
after the outage window, (iii) keep the independent branches running so the run still
makes progress, and (iv) require an explicit terminal outcome for the deferred branch
(succeeded later, or recorded as missing coverage) instead of silently dropping it.

## ★★★9 — A rehearsal test for failure handling

**What is injected.** (i) A connection reset before a response is read (to exercise
the retry path and the write-then-rename discipline); (ii) a truncated payload (to
exercise the checksum gate); (iii) a slow response beyond the timeout (to exercise the
timeout and backoff); (iv) a duplicate delivery (to exercise the deduplication key);
and (v) a mid-write process kill (to exercise the temporary-file and recovery logic).

**At which stages.** At the boundary stages — the fetch stage and the write stage —
because that is where partial state lives. Injecting inside a pure computation only
tests the exception path of code that can have no partial state; injecting at the
boundary is the realistic case.

**The observable that means it worked.** For each injection: the run either completes
with the correct data (verified by the reconciliation gate) or fails *loudly* with the
gate's message; the archive contains no partial or duplicated rows; the run report
records the injection and the terminal outcome; and the total time stays within the
retry budget. Success is therefore a combination of "the data are right" and "the
report is honest", not merely "the run exited zero".

**False conclusion the test could give.** If the injection point is not realistic —
for example raising an exception from inside the fetch function rather than dropping
the connection after the server committed — the test exercises a path that never
occurs in production and leaves the actual failure path untested. The test can also
pass because the gate is *too* coarse: a gate that only counts total rows may still
pass when a window is duplicated and another lost.

**What the rehearsal cannot establish.** That the pipeline behaves correctly under
real load, with real latency distributions, partial network partitions, and several
runs overlapping; and — importantly — it cannot establish that the failure modes
enumerated in the rehearsal are the ones that will happen. Production failures are
frequently in the parts nobody injected: an expired credential, a schema change at the
source, a time-zone shift in a service's window semantics.
