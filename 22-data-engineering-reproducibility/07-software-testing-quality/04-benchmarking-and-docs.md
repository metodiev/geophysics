---
id: 22-07-04
title: "Benchmarking, Performance Tracking and Documentation Tests"
level: research
prereqs: ["22-07-01", "22-06-03"]
estimated_minutes: 55
tags: [benchmarking, performance-tracking, noise-floor, doctests, documentation]
---

# Benchmarking, Performance Tracking and Documentation Tests

## Learning objectives

By the end of this lesson you will be able to:

1. **Measure** a benchmark's noise floor and **compute** the number of repeats needed to
   detect a stated change at a stated confidence.
2. **Convert** a fixed alert threshold into an expected number of false alarms per year, and
   **choose** a threshold and a reporting rule that keep the signal.
3. **Use** operation counts as a noiseless measurement, and **state** what they cannot see.
4. **Design** a performance-tracking regime that survives staff changes, machine changes and
   the temptation to ignore it.
5. **Decide** what documentation tests should assert, and **compute** what they cost and
   what they catch.
6. **State** which performance and documentation claims a repository can and cannot
   substantiate.

Everything here is **SYNTHETIC**: the timing noise, the commit rate, the operation counts and
the documentation statistics are chosen teaching values, simulated with
`np.random.default_rng(20261014)`. No machine was benchmarked, no provider or CI service was
used, and no documentation suite was run.

## Prerequisites

- [22-07-01 Test Strategy for Numerical and Data Code](./01-test-strategy-science.md) —
  the assertion types, and why a tolerance is a measurement.
- [22-06-03 Cost, Scaling and Practical Efficiency](../06-high-performance-and-cloud/03-cost-and-scaling.md) —
  why performance is a cost decision rather than a virtue.

## 1. Intuition: a benchmark is an experiment with a noise floor

"Make it faster" is unmeasurable until it is a comparison: *this code, on this machine, with
these inputs, is slower than that code by more than the measurement noise*. Three quantities
are therefore inseparable:

1. **The effect** to be detected — a percentage change in runtime, memory, or operations.
2. **The noise** — run-to-run variation from CPU frequency, contention, caches, page faults
   and I/O. It is a property of the machine and the workload, not a constant.
3. **The decision rule** — a threshold and a number of repeats, chosen so that the false
   alarm rate and the detection power are both acceptable.

Most teams fix (1) as "faster is better", ignore (2), and inherit (3) implicitly as "if the
CI is red, something regressed". Sections 2 and 3 show what that costs.

## 2. The noise floor, and how many repeats it demands

Model a measurement as $\text{true} \times (1 + \mathcal{N}(0,\sigma))$ and ask how many
repeats are needed to see a +10 % change at 95 % confidence with 80 % power. The
demonstration simulates it and compares the empirical power with the closed form
$n = [(z_{0.95} + z_{0.80})\,\sigma / \Delta]^2$:

| noise $\sigma$ | repeats | 95 % threshold | power to see +10 % |
| ---: | ---: | ---: | ---: |
| 0.10 | 1 | 0.1618 | 0.334 |
| 0.10 | 5 | 0.0735 | 0.660 |
| 0.10 | 10 | 0.0522 | 0.857 |
| 0.10 | 25 | 0.0328 | 0.991 |
| 0.03 | 1 | 0.0496 | 0.881 |
| 0.01 | 5 | 0.0074 | 1.000 |

Read the first row carefully: at 10 % noise a *single* measurement has a 95 % decision
threshold of 0.1618 — **larger than the effect you are trying to detect** — and the power is
0.334. One measurement on a noisy machine cannot see a 10 % regression; it can only see
something above 16 %.

The repeat counts from the closed form:

| change | repeats at $\sigma = 0.10$ | at $\sigma = 0.01$ |
| ---: | ---: | ---: |
| 10 % | 7 | 1 |
| 5 % | 25 | 1 |
| 3 % | 69 | 1 |
| 1 % | 619 | 7 |

Two conclusions that change practice:

- **Reduce the noise before adding repeats.** At $\sigma = 0.10$ a 1 % change needs 619
  repeats; at $\sigma = 0.01$ it needs 7. Pinning the core, using an exclusive machine,
  warming the cache and taking the best of a few runs buys an order of magnitude more
  sensitivity than repeating on a busy laptop.
- **Track a coarse threshold loudly and a fine one quietly.** A 10 % change is detectable
  with 7 repeats; a 2 % change (155 repeats) is a research project in itself, and should be
  reported as a trend rather than as a gate.

## 3. Alarms per year: what a fixed threshold costs

Suppose the team keeps a threshold of "alert if the benchmark is 5 % slower" and records one
measurement per push. At $\sigma = 0.10$, $P(\text{alarm}) = 0.30695$ under the null
(no change), so with 5 000 comparisons a year (20 pushes a day, 250 days):

| noise $\sigma$ | repeats | threshold | P(false alarm) | alarms per year |
| ---: | ---: | ---: | ---: | ---: |
| 0.10 | 1 | 0.05 | 0.306 95 | 1 535 |
| 0.10 | 10 | 0.05 | 0.056 88 | 284 |
| 0.03 | 10 | 0.05 | 0.000 00 | 0 |
| 0.01 | 10 | 0.05 | 0.000 00 | 0 |

Four alarms a day is a dashboard nobody reads; the correct diagnosis is not "the dashboard is
noisy" but "the threshold is below the machine's noise floor". With 10 repeats at 10 % noise
the alarm rate is 284 a year — still a false alarm most days a regression is not real.

The demonstration also shows why **best-of-N must never be mixed with other rules**:

| estimator | mean | spread |
| :--- | ---: | ---: |
| single run | 1.0000 | 0.1000 |
| best of 5 | 0.8837 | 0.0667 |

Best-of-5 reduces the spread by a third (0.1000 → 0.0667) but **biases the result low by
0.116** — it reports the machine at its best rather than its typical, and the bias depends on
$N$. Switching from best-of-5 to best-of-10 mid-project produces a step change in the trend
line that has nothing to do with the code. The rule is: choose the estimator once, document
it, and never change it without a discontinuity note in the record.

A tracking regime that survives:

1. **A dedicated machine or an exclusive allocation**, with the CPU governor and thread count
   fixed, and the container digest recorded.
2. **A fixed estimator** (median of $N$, or best of $N$, stated) and a fixed $N$.
3. **A threshold derived from the measured floor** — noise × 3, or a number of repeats chosen
   from §2 for the smallest effect worth acting on.
4. **Alert on a run of consecutive points** (three in a row above the threshold), not on a
   single point: this converts a per-comparison false-alarm rate into a much smaller one.
5. **Report the floor with every number**, so a reader knows a 2 % difference is not
   detectable on this machine.
6. **Keep timing out of the merge gate.** Measure, record, and review in a weekly pass; a
   timing gate blocks unrelated work and trains people to ignore it.

## 4. Operation counts: the measurement with no noise

Benchmarking is hard because runtime is a noisy proxy for the thing you actually care about,
which is usually *work*. Counts are exact integers: floating-point operations, memory
allocations, bytes read, iterations, convergence steps, matrix-vector products, model
evaluations. Their consequences:

- **A 3 % change in the operation count is detected exactly by one run**, where the same
  3 % change in runtime needs 69 repeats at 10 % noise.
- **The scaling exponent is exact.** The demonstration's table gives 9 966 operations at
  $n = 10^3$ and 19 931 569 at $n = 10^6$ for an $O(n\log n)$ kernel; a log-log fit returns a
  slope of **1.100**. For an $O(n^2)$ kernel the slope is **2.000**. A complexity regression
  is therefore detectable from two problem sizes with no repetition at all — a change from
  $n\log n$ to $n^2$ moves the slope to 2, which no amount of machine noise can hide.

What counts cannot see: cache behaviour, vectorisation width, thread contention, network
latency and I/O — all of which change the *rate*, not the count. So report **both**: the count
(what the algorithm does) and the achieved rate (how well the machine does it). A change in
the count is an algorithmic change; a change in the rate at a fixed count is a machine,
layout or compiler change. Attributing a slowdown to the right one is only possible if both
series are recorded.

## 5. Documentation tests

Documentation is the part of a research repository that decides whether anyone can use the
work, and it is checkable. The demonstration's SYNTHETIC example: 400 public functions, 340
with a docstring (85 %), of which 136 (40 %) have an executable example:

- **Cost**: 136 examples at 0.05 s each = **6.8 s**, which is **0.13 %** of a 90-minute suite.
- **What they catch**: a renamed or moved function is caught immediately for the 34 % of the
  public API that has an example — and silently for the rest. A changed default parameter is
  caught only where the example prints that parameter: 0.30 of the examples, about **40 of
  400** functions.
- **What they do not catch**: whether the prose is true, whether the description matches the
  behaviour, or whether the numbers are right. An example is an interface test, not a science
  test.

What to assert, in increasing order of value:

1. **Every example runs** — catches syntax drift, renames and signature changes.
2. **Every example's output matches** — catches behaviour change in the documented path.
3. **The README's quick-start runs verbatim** in CI, in a clean environment: this is the
   single highest-value documentation test, because it is the path every new user takes.
4. **The metadata is consistent**: the version in the code matches the tag, the citation file
   parses, the licence is present, and the documentation references resolve
   ([22-01-05](../01-research-software-engineering/05-licensing-and-citation.md)).
5. **A numeric claim in the prose is generated, not typed** — if the README states a
   benchmark number or a dataset size, generate it.

Treat measures as targets with names, not as verdicts: "85 % of public functions have a
docstring" is a statement about the API surface; "136 examples run in CI in 6.8 s" is a
statement about what is verified. Only the second is a test.

## 6. Practice: a performance record that outlives its authors

A performance record is data. Keep it as such:

1. **A machine-readable trend file** (JSON or CSV) appended by the benchmark job, with the
   timestamp, commit, estimator, $N$, the floor, the mean and spread, and the operation
   counts — one row per run per benchmark.
2. **The benchmark definitions in the repository**, versioned with the code, each with a
   stated input size, a warm-up policy, and how many repetitions it performs.
3. **A noise-floor job** that runs the benchmark $N$ times without changing code and records
   the observed spread — so a drift in the machine is distinguishable from a drift in the
   code.
4. **A discontinuity note** whenever the estimator, the machine or the input size changes: a
   line in the record explaining that comparisons across this point are not valid.
5. **A quarterly review** that reads the trend rather than the alerts: the value of the record
   is in the slope over months, not in any single point.

## 7. Worked example: the dashboard nobody trusted

A team instruments a nightly benchmark, alerts on any 5 % slowdown, and within a month the
channel is full of alerts. A developer checks one: the code did not change, the machine was
busy. The team responds by loosening the threshold to 15 %, and the next real regression — a
20 % slowdown from an accidental $O(n^2)$ loop — is caught a month later, after an
interactive workflow had been painful for weeks. The repair is cheap: the operation count
would have caught the complexity change exactly on the first run (slope 1.100 → 2.000 in
§4); the timing alert should have been a three-consecutive-points rule with a threshold from
the measured floor; and the alert would have carried the floor with the number, so the
reader could see that a 4 % difference was not measurable. The lesson: an alert whose
threshold was never measured is a decision to stop reading alerts.

## Assumptions and regime of validity

- **The noise model is simple.** Independent Gaussian noise per run is a teaching
  approximation; real timing distributions are right-skewed with occasional large outliers,
  which is exactly why a median or a minimum is a better estimator than a mean, and why
  removing interleaved outliers must be documented.
- **The thresholds and rates are chosen.** 5 %, 20 pushes a day, $\sigma = 0.10$ and
  $\sigma = 0.01$ are teaching values; the arithmetic and the ordering are what transfer.
- **Operation counts are deterministic only for a fixed code path.** A data-dependent branch
  count (an iterative solver that stops early) makes counts input-dependent too, so record the
  input alongside the count.
- **Documentation tests verify the example, not the claim.** A passing example does not make
  the surrounding prose true.
- **Not all performance work is worth tracking.** A one-off script that runs for an hour a
  year does not need a benchmark; the effort belongs on the code that runs thousands of times.

## The honest summary

1. Measure the noise floor before any comparison; at 10 % noise one measurement cannot see a
   10 % change.
2. Compute repeats from the effect, the noise and the confidence you want; 7 repeats at 10 %
   noise for a 10 % effect, 619 for a 1 % effect.
3. A fixed threshold below the noise floor produces 1 535 false alarms a year in the
   demonstration's setting; alert on consecutive points and print the floor next to every
   number.
4. Count the work as well as the time: counts are exact, expose complexity changes at two
   problem sizes, and separate algorithmic change from machine change.
5. Documentation examples are a cheap interface test (6.8 s for 136 examples) that catch
   renames for the documented 34 % of the API and nothing about the science.
6. Keep timing out of the merge gate, and keep a machine-readable record with the estimator,
   the machine and the floor.

## Python demonstration

[`code/benchmarking_and_docs_demo.py`](./code/benchmarking_and_docs_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. the noise/repeat table — at 10 % noise, one repeat has a threshold of 0.1618 and a power of
   0.334 — with the closed-form repeat counts 7/25/69/619;
2. the false-alarm table for a fixed 5 % threshold (1 535 alarms a year at one repeat, 284 at
   ten) and the best-of-5 bias (mean 0.8837, spread 0.0667 against 0.1000);
3. the operation-count table with fitted log-log slopes of 1.100 and 2.000, and the repeat
   counts the same 3 % change would need in runtime;
4. the documentation statistics — 340 docstrings, 136 examples, 6.8 s of CI time, 40 of 400
   functions with a caught default-value change.

```bash
cd 22-data-engineering-reproducibility/07-software-testing-quality/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python benchmarking_and_docs_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/04-benchmarking-and-docs-exercises.md`](./exercises/04-benchmarking-and-docs-exercises.md)
and
[`exercises/04-benchmarking-and-docs-solutions.md`](./exercises/04-benchmarking-and-docs-solutions.md).

## Mastery checkpoint

Without notes:

1. A benchmark has 8 % run-to-run noise. Compute the repeats needed to detect a 10 % change
   at 95 % confidence and 80 % power, and the repeats needed for 3 %.
2. A team alerts on any 3 % slowdown measured once per push, 5 000 times a year. Compute the
   expected number of false alarms.
3. State why a 3 % operation-count change is detectable in one run and what a 3 % *runtime*
   change would need.
4. State what operation counts cannot see and what to record alongside them.
5. State what a documentation example test catches, with the fraction of the API covered in
   the demonstration's setting.
6. State three features of a performance record that let a future maintainer interpret a
   change.

## Common pitfalls

1. **Comparing single runs.** The threshold at 10 % noise is 16 %, larger than the effect.
2. **A threshold below the floor.** It produces thousands of false alarms and the dashboard is
   abandoned.
3. **Changing the estimator mid-project.** Best-of-5 is biased low by 0.116 in the
   demonstration; changing $N$ moves the trend line without changing the code.
4. **Timing gates in the merge queue.** They block unrelated work and teach people to rerun.
5. **Reporting time without work.** A slowdown needs attribution to an algorithmic or a
   machine cause, which needs the count and the rate.
6. **Treating documentation coverage as a quality measure.** The number proves the API
   surface, not the truth of the prose.
7. **No floor recorded.** A table of times without the noise floor invites false conclusions.

## Where this is used

- **Performance regressions in numerical libraries** — counts and scaling slopes:
  see [19-06 HPC and Parallel Computing](../../19-numerical-modeling-hpc/06-hpc-and-parallel-computing/README.md).
- **Cost and scaling decisions** — the price of the wall time you decide to buy:
  see [22-06-03 Cost, Scaling and Practical Efficiency](../06-high-performance-and-cloud/03-cost-and-scaling.md).
- **Regression tests for values** — the same discipline applied to correctness:
  see [22-07-03 Regression Testing Against Known Results](./03-regression-testing-data.md).
- **Software release notes and docs** — what the version string and citation metadata promise:
  see [22-01-05 Licensing, Citation and Software Credit](../01-research-software-engineering/05-licensing-and-citation.md).

## Related lessons

- [22-07-01 Test Strategy for Numerical and Data Code](./01-test-strategy-science.md) —
  the assertion types and the cost of late detection.
- [22-07-02 Continuous Integration for Research Software](./02-continuous-integration.md) —
  where benchmarks and documentation tests run, and what belongs outside the gate.
- [22-07-03 Regression Testing Against Known Results](./03-regression-testing-data.md) —
  tolerances, goldens and invalidation.
- [22-06-03 Cost, Scaling and Practical Efficiency](../06-high-performance-and-cloud/03-cost-and-scaling.md) —
  turning a wall time into a budget.

## Self-assessment checklist

- [ ] I can measure a noise floor and compute the repeats an effect needs.
- [ ] I can convert a threshold into an expected false-alarm count and choose a rule.
- [ ] I can use operation counts and scaling slopes to detect complexity changes.
- [ ] I can state what counts cannot see and what to record with them.
- [ ] I can decide what a documentation test should assert and what it costs.
- [ ] I can design a performance record a future maintainer can interpret.
