---
id: 22-03-03
title: "Designing Robust Data Pipelines for Earth Data"
level: research
prereqs: ["22-03-02", "22-02-03"]
estimated_minutes: 50
tags: [data-pipelines, reliability, idempotency, retries, data-engineering]
---

# Designing Robust Data Pipelines for Earth Data

## Learning objectives

By the end of this lesson you will be able to:

1. **Model** a pipeline as stages with failure probabilities, and **compute**
   end-to-end success with and without retries.
2. **Compute** the expected attempts and the wasted fraction that a retry policy
   costs, and **state** why the cost is small relative to the failure it removes.
3. **Distinguish** at-least-once from exactly-once delivery, and **compute** the
   duplicate and loss rates a retry policy produces.
4. **Decide** which stages must be idempotent, and **design** a deduplication key for
   the stages that cannot be.
5. **Diagnose** the four classic pipeline failures — partial write, duplicate row,
   silently lost record, and time-dependent output — from their symptoms.
6. **Specify** the validation gates that make a pipeline fail loudly rather than
   produce plausible wrong data.

Failure probabilities, costs and delivery rates in this lesson are **SYNTHETIC**
and chosen for teaching. The simulation of duplicates and losses is a Monte Carlo run
by the demonstration; no pipeline was executed and no service was called.

## Prerequisites

- [22-03-02 Format Trade-Offs: Access Patterns, Compression, Portability](./02-format-design-tradeoffs.md) —
  the objects the pipeline writes and their write patterns.
- [22-02-03 Workflow Managers: Snakemake, Make, Dask, Prefect](../02-reproducible-workflows/03-workflow-managers.md) —
  the scheduling and caching layer beneath the reliability questions here.

## 1. Intuition: pipelines fail probabilistically, and silently

A pipeline is not a program that either works or does not; it is a system of stages
that succeed with some probability each, and whose failures are often partial. The
network drops a response after the server committed the write; a stage with a
half-written output file looks complete to the next stage; a retry re-delivers a
record that a downstream sum has already counted. None of these produces an
exception that says "your data are wrong".

The engineering response has three parts: **make failures visible** (validation
gates), **make repeats safe** (idempotence or deduplication), and **make failures
rare** (retries with backoff). This lesson measures the second and third and shows
why the first is the one that decides whether you notice.

## 2. End-to-end success with and without retries

Model $N$ stages, each of which fails independently on an attempt with probability
$p$. Without retries:

$$P(\text{success}) = (1-p)^{N},$$

and with up to $R$ retries per stage, a stage succeeds if *any* of its $R+1$
attempts succeeds:

$$P(\text{stage success}) = 1 - p^{R+1}, \qquad
P(\text{pipeline success}) = \left(1 - p^{R+1}\right)^{N}.$$

For the demonstration's **SYNTHETIC** pipeline — $N = 8$ stages, $p = 0.02$,
$R = 3$ — the measurements are:

| Policy | Stage success | End-to-end success | Failures per 10 000 runs |
|---|---|---|---|
| no retries | 0.9800 | 0.8508 (85.1 %) | 1492 |
| 3 retries | 0.999999 | 0.999999 (99.9999 %) | 0.0 |

The arithmetic of the first row is instructive: eight stages at 98 % each give
$0.98^{8} = 0.8508$. A per-stage reliability that sounds acceptable (98 %) becomes
an unacceptable pipeline reliability (85 %) purely by multiplication, which is why
long pipelines need either fewer stages or retries. Note also the honest limit: the
retried version's success is **0.999999**, not 1 — the failure probability is
multiplied, not removed, and a run that fails all four attempts of a stage still
fails.

## 3. What retries cost

The expected number of attempts for a stage with failure probability $p$ and up to
$R$ retries is

$$\mathbb{E}[\text{attempts}] = \sum_{k=0}^{R} p^{k} = 1 + p + p^{2} + \cdots + p^{R}
= 1.020408 \ \text{for } p = 0.02, R = 3.$$

So the pipeline executes $8 \times 1.020408 = 8.1633$ stage attempts per run against
an ideal of 8, a waste of **2.041 %**. The general statement is that the cost of the
retry policy equals the per-attempt failure probability to first order: a 2 % flake
rate costs 2 % more work, which is trivial next to converting a 15 % pipeline failure
rate into a rare event. The conclusion holds until $p$ is large enough that the
geometric sum stops being small, or until a retried stage is expensive enough that
its duplicates dominate the budget.

## 4. At-least-once, duplicates and silent losses

Real delivery is not atomic: a request can succeed while its acknowledgement is lost,
and a message can be lost without any error being reported. The demonstration
simulates 100 000 runs of the 8-stage pipeline with a 99 % per-attempt delivery
probability and a retry on every failure:

| Quantity | Measured |
|---|---|
| stage-attempts delivered twice | 7989 |
| stage-attempts lost without an error | 7979 |
| duplicate rate | 0.00999 |
| silent loss rate | 0.00997 |
| runs containing at least one duplicate | 7.71 % |
| runs containing at least one silent loss | 7.71 % |

Two consequences. First, **a retry policy converts failures into duplicates**: the
same input is delivered again, and a stage that appends rather than replaces will
double-count. This is the defining difference between *at-least-once* delivery (which
retries give you) and *exactly-once* semantics (which require deduplication or a
transaction). Second, **silent losses are as common as duplicates**, and no retry
removes them because nothing raised an error. This is why a pipeline needs an
independent count check on what arrived.

## 5. Idempotence, or a deduplication key

A stage is **idempotent** if running it twice with the same input produces the same
state as running it once. The demonstration's table of stage kinds:

| Stage kind | Idempotent by construction? | Harm if retried |
|---|---|---|
| download to a file | yes — same bytes overwritten | none |
| append to a table | no | duplicated rows |
| increment a counter | no | inflated totals |
| write a whole output | yes — replaced | none |
| emit a message | no | duplicate downstream work |
| delete then write, keyed by id | yes | none |

The design rule that follows is: where a stage cannot be made idempotent, give it a
**deduplication key** — a deterministic identifier (station, channel, start time, or
a content hash) that the write path uses to replace or ignore an existing record
rather than append. Schema-level support is what makes this practical: a primary key
or a unique constraint turns a duplicate into a rejected write instead of a wrong
number.

## 6. The four failures and their symptoms

| Failure | How it appears | What detects it |
|---|---|---|
| partial write | a file that is truncated or unreadable | write to a temporary name and rename; validate the row count |
| duplicate row | totals slightly too high, drifting with retries | deduplication key; a count check against the source |
| silently lost record | totals slightly too low, no error | reconciliation counts; checksums of the expected set |
| time-dependent output | results differ between runs on different days | no wall-clock or "latest" inputs; pin the query window |

Every one of these is quiet. The mitigation is a **validation gate** at the end of
each stage: an expected row count, a checksum over the delivered set, a null and range
check on the key columns, and a comparison of the count delivered against the count
expected from the source. A gate that fails loudly is worth more than any amount of
retry tuning, because it converts silent corruption into a scheduled rerun.

## 7. Practice: rules for pipelines that carry data

1. **Write to a temporary path and rename.** A reader then never sees a partial file.
2. **Make every write either replace-by-key or idempotent.** Appends need a key.
3. **Validate after every stage.** Counts, checksums and key uniqueness at minimum.
4. **Record the input set of each run.** Which files, which versions, which query
   window — so a rerun can be explained after the fact
   ([22-02-05](../02-reproducible-workflows/05-data-versioning.md)).
5. **Retry with backoff, and cap the retries.** An unbounded retry loop against a
   failing service is an outage.
6. **Distinguish transient from permanent failures.** A malformed record will fail
   every attempt; retrying it three times is waste, and the record belongs in a
   quarantine table with a report.
7. **Reconcile against the source.** The only evidence that nothing was lost is an
   independent count.

## 8. Worked example: a pipeline that loses one record a week

A group's nightly ingest writes 4 million rows and occasionally has to be rerun. Over
a year the table is 40 rows short of the source, with no error anywhere.

1. **Classify.** Twenty shortfalls of a few rows each, with no error, is the
   *silently lost record* pattern of §6, whose modelled rate here is 0.997 % of
   stage-attempts. The absence of an error is expected: nothing failed.
2. **Why retries do not fix it.** Retries fire on errors; a loss with no error never
   triggers one. The measured silent-loss rate (0.00997) and duplicate rate
   (0.00999) are of the same order, so the retry policy is not helping this failure
   at all.
3. **What would have caught it.** A reconciliation gate: at the end of the ingest,
   compare the row count written with the row count the source reported, and fail the
   job on a mismatch. The modelled magnitude — 7.71 % of runs containing at least one
   silent loss — means such a gate would have fired about 28 times a year.
4. **The repair.** Add the gate, then back-fill: since the pipeline records the input
   set of each run (§7.4), the missing windows can be identified and re-ingested with
   a deduplication key so that the repair cannot add duplicates.

## Assumptions and regime of validity

1. **Independent stage failures.** Real failures correlate: a service outage fails
   every stage that calls it, so the product formula flatters a pipeline that depends
   on one service repeatedly.
2. **A constant failure probability.** Rates drift with load, and a pipeline can pass
   from "2 % flaky" to "broken" without a code change; the model's constant $p$ is a
   local description.
3. **Uniform delivery probability.** The 99 % delivery figure is a chosen constant
   applied uniformly; real systems have per-endpoint and per-size behaviour.
4. **Retries are safe to repeat.** The cost calculation assumes retrying is harmless;
   where a stage is not idempotent, the "cost" is corrupted data, not extra work — the
   central point of §5.
5. **No queueing or rate limits.** The model has no backpressure, so it understates
   the cost of retry storms and says nothing about how long a run takes under load.

## The honest summary

A pipeline's reliability multiplies across its stages: eight 98 % stages give 85.1 %
end-to-end success, and three retries per stage raise it to 99.9999 % for a measured
cost of 2.041 % extra stage attempts, which is the per-attempt failure rate to first
order. Retries buy at-least-once delivery, and the demonstration measures what that
means: 0.999 % duplicates and 0.997 % silent losses among stage-attempts, with 7.71 %
of runs containing at least one of each. The engineering that follows is explicit —
write-then-rename, replace-by-key or idempotent stages, validation gates with counts
and checksums, and reconciliation against the source — because the failures that cost
data are precisely the ones that raise no error.

## Python demonstration

[`code/data_pipelines_demo.py`](./code/data_pipelines_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. end-to-end success with and without retries (85.1 % against 99.9999 %);
2. the expected-attempts arithmetic (1.020408 per stage, 8.1633 per run, 2.041 %
   waste);
3. a 100 000-run Monte Carlo of duplicates and silent losses, with per-run rates;
4. the idempotence table for six stage kinds.

```bash
cd 22-data-engineering-reproducibility/03-data-formats-and-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_pipelines_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/03-data-pipelines-exercises.md`](./exercises/03-data-pipelines-exercises.md)
and
[`exercises/03-data-pipelines-solutions.md`](./exercises/03-data-pipelines-solutions.md).

## Mastery checkpoint

Without notes: a pipeline has 14 stages, each failing with probability 0.03.

1. Compute the end-to-end success without retries, and with two retries per stage.
2. Compute the expected stage attempts per run with two retries, and the waste.
3. State which of the following must be idempotent, and how: a download, a counter
   update, a table append, a file overwrite.
4. A nightly run is 3 rows short of the source with no error. Name the failure, the
   gate that would catch it, and why adding retries would not help.

## Common pitfalls

1. **Reading a per-stage reliability as a pipeline reliability.** 98 % per stage is
   85.1 % over eight stages.
2. **Assuming retries remove failures.** They multiply the failure probability; the
   modelled success is 0.999999, not 1.
3. **Retrying a non-idempotent stage.** The retry converts a transient error into
   duplicated data, which no error message reports.
4. **Relying on errors to detect losses.** The silent-loss rate matches the duplicate
   rate in the model; nothing raised an error.
5. **Appending without a key.** A deduplication key is what makes at-least-once
   delivery tolerable.
6. **No reconciliation gate.** Without an independent count, corruption is discovered
   by a user months later, and the cause is unrecoverable.

## Where this is used

- **Ingest of catalogues and sensor streams** — duplicates and silent losses are the
  operational realities of network delivery: see
  [22-04-03 Time-Series Databases for Sensor Networks](../04-databases-and-large-data/03-timeseries-databases.md).
- **Data quality control** — the validation gates here are the rule decisions of
  [22-03-05 Automated Quality Control and Flagging](05-data-quality-control.md).
- **Workflow managers** — the stage graph is the same DAG as
  [22-02-03](../02-reproducible-workflows/03-workflow-managers.md) §2, viewed through
  reliability.
- **Cloud and cluster ingestion** — request limits and backpressure shape the retry
  policy: see
  [22-03-04 Programmatic Access to Earth Data](04-getting-earth-data.md).

## Related lessons

- [22-03-04 Programmatic Access to Earth Data (FDSN, Earthdata, Copernicus)](04-getting-earth-data.md) —
  the fetch layer whose failures these retries absorb.
- [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md) —
  recording the input set that makes a repair possible.
- [22-07-03 Regression Testing Against Known Results](../07-software-testing-quality/03-regression-testing-data.md) —
  testing the pipeline against a known reference.
- [22-04-04 Big-Data Patterns: Partitioning, Chunking, Out-of-Core](../04-databases-and-large-data/04-big-data-patterns.md) —
  the same reliability questions at partition scale.

## Self-assessment checklist

- [ ] I can compute end-to-end success from per-stage probabilities.
- [ ] I can compute the cost of a retry policy.
- [ ] I can explain at-least-once versus exactly-once delivery.
- [ ] I can decide which stages need idempotence and design a key.
- [ ] I can name the four classic failures and their symptoms.
- [ ] I can specify validation gates for a pipeline.
