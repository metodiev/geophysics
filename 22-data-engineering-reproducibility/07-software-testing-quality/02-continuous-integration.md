---
id: 22-07-02
title: "Continuous Integration for Research Software"
level: research
prereqs: ["22-07-01", "22-02-02"]
estimated_minutes: 55
tags: [continuous-integration, flaky-tests, test-matrix, sharding, build-automation]
---

# Continuous Integration for Research Software

## Learning objectives

By the end of this lesson you will be able to:

1. **Size** a build matrix — jobs, machine-minutes and the wall-time floor — and
   **choose** the runner count that actually helps.
2. **Compute** the suite-level failure rate from a per-test flake rate, and **state** the
   posterior probability that a red build signals a real defect.
3. **Choose** a retry and quarantine policy that removes noise without hiding real
   intermittent failures.
4. **Shard** a suite so the wall time falls without changing the machine-minutes, and
   **state** the imbalance floor that sharding cannot cross.
5. **Decide** what a research CI must check beyond passing tests: environment build,
   numerical tolerance, data fixtures, documentation and citation metadata.
6. **State** when a research project should not run CI on every push, and what it should
   run instead.

All job counts, durations, flake rates and runner counts are **SYNTHETIC** chosen teaching
values in arbitrary units. No CI service was contacted, no provider quota is quoted, and no
real build was measured.

## Prerequisites

- [22-07-01 Test Strategy for Numerical and Data Code](./01-test-strategy-science.md) —
  what the suite asserts, and why a passing suite is not the same as a correct one.
- [22-02-02 Pinning Environments and Managing Dependencies](../02-reproducible-workflows/02-environment-pinning.md) —
  the lock file a CI job installs from.

## 1. Intuition: CI is an executable definition of "it works"

Continuous integration is a promise with a mechanical form: *every change is built and
tested in a clean environment, and the result decides whether the change may be merged.*
Its value does not come from running tests — developers already do that — but from three
properties a shared service provides and a laptop cannot:

1. **A clean environment.** Dependencies installed from the lock file
   ([22-02-02](../02-reproducible-workflows/02-environment-pinning.md)), not from the
   developer's already-working machine.
2. **A shared definition of the commit.** Two people can disagree about whether their
   laptop's failure is real; they cannot disagree about the build's log.
3. **Behaviour under concurrency.** Ten changes a week arriving into one branch is the
   situation where integration problems appear, and the only way to see them early is to
   integrate early.

Everything else in this lesson is about the failure modes that turn the promise into
noise — a matrix nobody waits for, a red build that usually means nothing, a suite that
fails on one machine and passes on another.

## 2. The matrix: jobs, machine-minutes and the wall-time floor

A scientific package often supports several operating systems, several interpreter
versions and several dependency sets. In the demonstration's SYNTHETIC example, a
$3 \times 4 \times 2$ matrix is 24 jobs, each costing 0.5 min of setup, 2.0 min of
installation and 6.0 min of tests — **8.5 min** per job, or 6.7 min with a warm dependency
cache. The totals:

| quantity | cold cache | warm cache |
| :--- | ---: | ---: |
| machine-minutes | 204 | 161 |
| saving from caching | — | 43 machine-minutes |
| wall time, 1 runner | 204.00 min | — |
| wall time, 5 runners | 42.50 min | — |
| wall time, 24 runners | 8.50 min | — |
| wall time, 48 runners | 8.50 min | — |

Three readings:

- **Machine-minutes are conserved; wall time is not.** Every runner count consumes 204
  machine-minutes; what changes is how many are spent in parallel.
- **The floor is one job.** Beyond 24 runners the wall time cannot fall: it is the
  *duration* of a job that limits the build, so a job that takes 8.5 min makes the build
  8.5 min long no matter the fleet.
- **The fast lane is the response.** Run one system and the newest interpreter on every
  push (6.7 min) and the full matrix nightly; the developer's feedback loop is then
  governed by the fast lane, and the matrix catches portability problems within a day.

Note also that the 5-runner row has a utilization of 96 % rather than 100 % — with 24 jobs
and 5 slots, the last wave is partly idle. Scheduling arithmetic, not something to fix by
buying runners.

## 3. Flakiness destroys the signal

A flaky test fails without a code change. Its effect is multiplicative over the suite: with
$N$ independent tests and a per-test flake rate $p$, the probability that at least one fails
is $1 - (1 - p)^N$. For a 600-test suite (chosen), and a prior probability of 0.10 that a
push is genuinely broken:

| per-test flake rate | P(suite red) | P(push is broken \| red) |
| ---: | ---: | ---: |
| 0.000 1 | 0.0582 | 0.6561 |
| 0.001 | 0.4514 | 0.1975 |
| 0.005 | 0.9506 | 0.1047 |
| 0.010 | 0.9976 | **0.1002** |
| 0.020 | 1.0000 | 0.1000 |

The last column is Bayes' rule with the red build as evidence. At a 1 % per-test flake rate
the suite is red on **99.76 %** of pushes, and a red build implies a real defect with
probability **0.100** — that is, **90 % of red builds are noise**. Over 5 000 pushes a year,
about 4 988 red builds, roughly 4 489 of them spurious. A dashboard in that state is not a
signal; it is a ritual, and the response it trains is "rerun it", which is precisely the
behaviour that lets a real defect through.

Two quantitative points worth carrying:

- **The suite is red even when flakiness is rare.** At a 0.01 % per-test rate the suite is
  red on 5.8 % of pushes — one build in seventeen.
- **Bayes punishes weak evidence.** The posterior saturates at the prior (0.10) as the red
  rate goes to 1: if the build is always red, the build tells you nothing.

## 4. Retries: what they buy and what they hide

The standard mitigation is to rerun a failed test or job. With independent attempts, a
spurious red needs every attempt to fail, so the rate becomes $1 - (1 - p^k)^N$:

| attempts | spurious red per push | per year (5 000 pushes) |
| ---: | ---: | ---: |
| 1 | 0.997 595 | 4 988 |
| 2 | 0.058 238 | 291 |
| 3 | 0.000 600 | 3 |

Two attempts reduce spurious reds **17-fold**; three reduce them to single digits per year.
That is a large, cheap win — and it has a cost that must be paid explicitly.

**Retries hide real intermittent failures.** A genuine 5 % failure rate in one test makes
the suite red with certainty on one attempt, but with three attempts the bug looks green in
**92.8 %** of pushes: a race condition that will fire in production is exactly as hidden as
a flaky assertion. The policy that keeps both benefits:

1. **Never retry silently.** A retry opens a record with the test name, the commit and the
   logs.
2. **Measure the failure rate.** Run the suspect test in a loop (100–1 000 repetitions) to
   distinguish "fails 1 in 1 000 under load" (infrastructure) from "fails 1 in 20" (a real
   bug).
3. **Fix or quarantine with a deadline.** A quarantined test is skipped in the merge gate
   and tracked in the issue register
   ([22-05-02](../05-collaboration-and-project-management/02-issue-tracking.md)) with an
   owner and a date; an unowned quarantine is a deleted test with extra steps.
4. **Never let a flaky test be "fixed" by loosening its assertion** unless the assertion was
   actually wrong — that converts a real defect into a permanent blind spot
   ([22-07-01](./01-test-strategy-science.md) §4).

## 5. Sharding: the same machine-minutes, a different wall clock

When the suite itself is the bottleneck, split it across runners. The demonstration models
60 test files (2 443 tests, 2 291 s of work on one runner) with chosen lognormal file
costs; the slowest file takes 129.1 s and the median 25.5 s.

| strategy | shard times (s) | wall time (s) |
| :--- | :--- | ---: |
| contiguous quarter of the file list | 642.2, 686.8, 544.4, 417.6 | 686.8 |
| longest file first | 572.3, 571.8, 572.5, 574.4 | 574.4 |

Choosing the assignment by descending file cost shortens the wall time by **16.4 %** at
identical machine-minutes, because the naive split leaves one shard with the expensive
files. Two rules follow:

- **Shard by measured cost, not by count.** Order by a recorded duration (a previous run's
  timings, cached in the CI artifacts) and assign greedily longest-first. Sharding by test
  *count* is optimal only if all tests cost the same, which is never true.
- **The floor is the largest file.** Here 129.1 s is irreducible by sharding; only
  splitting that file (or caching what it recomputes) moves it. If one file is 40 % of the
  suite, the wall time cannot fall below 40 % of the suite's runtime.

## 6. What a research CI must check

A scientific build has obligations a software-only build does not. A defensible pipeline
checks, in increasing cost:

1. **Install from the lock file** in a clean environment — the only check that the
   published environment actually builds
   ([22-02-02](../02-reproducible-workflows/02-environment-pinning.md)).
2. **Run the unit tests** on the fast lane, with the failures attributable to a file and a
   test name.
3. **Run the numerical goldens** at their stated tolerances, recording the measured spread
   on the CI machine — a golden that passes only at a loose tolerance is telling you the
   platform is the variable ([22-07-03](./03-regression-testing-data.md)).
4. **Check the data fixtures**, not the full datasets: a small, audited fixture in the
   repository for logic, and an optional nightly job that fetches the versioned real data
   ([22-02-05](../02-reproducible-workflows/05-data-versioning.md)).
5. **Check the metadata**: the citation file parses, the version string matches the tag, the
   documentation examples run
   ([22-07-04](./04-benchmarking-and-docs.md),[22-01-05](../01-research-software-engineering/05-licensing-and-citation.md)).
6. **Check the numbers that matter**: a short benchmark run whose result is recorded, so a
   performance regression is visible (§5 of [22-07-04](./04-benchmarking-and-docs.md)).

Two things to keep *out* of the merge gate: long-running benchmarks (measure, do not gate)
and tests that need network access or a large dataset (a gate that fails when a remote
service is down teaches people to ignore red).

## 7. Worked example: the build that was green and the paper that did not compile

A group's CI runs 700 tests in 11 minutes and is green for months. A journal submission
fails because the LaTeX document that generated every figure will not build on the
reviewer's machine: the figures were produced by a script that reads an untracked file from
a colleague's home directory, and the document includes it by absolute path. Nothing in the
CI pipeline touches the figure generation or the document. The fix is four lines of
configuration — a job that runs the figure script against the fixture and then compiles the
document — and it takes three minutes on the nightly lane. The general lesson: a CI that
tests the *library* and not the *publication path* verifies the part of the project that was
never at risk.

## Assumptions and regime of validity

- **Independence of tests.** The suite-level formula $1-(1-p)^N$ assumes independent
  failures; correlated flakes (a shared network or a loaded runner) make the suite red more
  often than the formula predicts.
- **Chosen constants.** Job durations, flake rates, prior and runner counts are teaching
  values; the arithmetic is what transfers, not the numbers.
- **Machine-minutes are conserved only for fixed work.** Caching and test selection change
  the work, and a cached run is not measuring the same thing as a cold one.
- **A green build is not correctness.** It means the checks that exist passed on the commit;
  the coverage and kill-rate caveats of
  [22-07-01](./01-test-strategy-science.md) §4 apply unchanged.
- **Every gate costs attention.** A gate that fires on noise is worse than no gate, because
  it trains the response "rerun" — §3's 90 % figure is the measure of that damage.

## The honest summary

1. Count jobs and machine-minutes before choosing a fleet; the wall-time floor is one job,
   and the fast lane is what makes the loop quick.
2. Compute the suite-level failure rate from the per-test flake rate; at 600 tests, 1 %
   flakes make the suite red 99.76 % of the time and 90 % of red builds meaningless.
3. Retry to remove noise, but always record the retry, measure the failure rate, and fix or
   quarantine with a deadline: three attempts hide a 5 % real failure in 92.8 % of pushes.
4. Shard by measured cost; the largest file is the sharding floor.
5. Check the publication path, not only the library.
6. Keep long benchmarks and network-dependent tests out of the merge gate.

## Python demonstration

[`code/continuous_integration_demo.py`](./code/continuous_integration_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. the 24-job matrix, its 204 cold and 161 warm machine-minutes, the wall time against
   runner count and the 8.5-minute floor;
2. the flake-rate table with the Bayes posterior — 0.100 at a 1 % rate — and the 4 988 red
   builds of 5 000 pushes;
3. the retry table (4 988, 291, 3 spurious reds) and the 92.8 % masking of a real 5 %
   failure;
4. the sharding comparison — 686.8 s contiguous against 574.4 s longest-file-first, with a
   129.1 s single-file floor.

```bash
cd 22-data-engineering-reproducibility/07-software-testing-quality/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python continuous_integration_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/02-continuous-integration-exercises.md`](./exercises/02-continuous-integration-exercises.md)
and
[`exercises/02-continuous-integration-solutions.md`](./exercises/02-continuous-integration-solutions.md).

## Mastery checkpoint

Without notes:

1. A matrix has 40 jobs of 5 minutes each. Compute the machine-minutes and the wall time at
   8 and at 64 runners, and state the floor.
2. A suite has 400 tests and a per-test flake rate of 0.002. Compute the probability that a
   push is red, and state the change that most reduces it.
3. State the two-sided cost of retrying a failed test twice.
4. State the sharding rule and the floor it cannot cross.
5. State three things a research CI must check that are not unit tests.

## Common pitfalls

1. **A matrix nobody waits for.** Developers disable it and run the tests locally, which is
   the situation CI was introduced to fix.
2. **Ignoring the flake rate.** A single 1 %-flaky test in a 600-test suite makes the build
   red on nearly every push.
3. **Silent retries.** Without a record, a real intermittent failure disappears behind the
   retry policy.
4. **Sharding by count.** The wall time is set by the most expensive shard, not the fullest.
5. **Gating merges on long benchmarks.** Timing noise then blocks work unrelated to it.
6. **Testing the library, not the paper.** Figure generation, document builds and citation
   metadata are part of the research output.
7. **Fixing a flaky test by loosening the assertion.** Usually it converts a defect into a
   blind spot.

## Where this is used

- **Scientific libraries** — the matrix is the portability statement, and the goldens are
  the correctness statement:
  see [22-07-03 Regression Testing Against Known Results](./03-regression-testing-data.md).
- **Reproducibility of published results** — the pipeline that runs on a clean machine is
  the artifact a reader executes:
  see [22-02-03 Workflow Managers](../02-reproducible-workflows/03-workflow-managers.md).
- **Team collaboration** — the merge gate is the shared definition of "working":
  see [22-01-03 Code Review and Collaborative Development](../01-research-software-engineering/03-code-review.md).
- **Software releases and citation** — version strings and metadata checked by the tag
  build:
  see [22-01-05 Licensing, Citation and Software Credit](../01-research-software-engineering/05-licensing-and-citation.md).

## Related lessons

- [22-07-01 Test Strategy for Numerical and Data Code](./01-test-strategy-science.md) —
  what the suite asserts and why coverage is an upper bound.
- [22-07-03 Regression Testing Against Known Results](./03-regression-testing-data.md) —
  tolerances, goldens and invalidation.
- [22-07-04 Benchmarking, Performance Tracking and Documentation Tests](./04-benchmarking-and-docs.md) —
  performance measurement with a noise floor.
- [22-02-06 Containers for Computational Reproducibility](../02-reproducible-workflows/06-containers-reproducibility.md) —
  the environment a CI job builds and a reviewer runs.

## Self-assessment checklist

- [ ] I can size a matrix and identify its wall-time floor.
- [ ] I can compute a suite-level failure rate and the posterior of a red build.
- [ ] I can design a retry and quarantine policy with records and deadlines.
- [ ] I can shard a suite by measured cost and state the floor.
- [ ] I can list the checks a research CI needs beyond unit tests.
- [ ] I can say which checks belong outside the merge gate.
