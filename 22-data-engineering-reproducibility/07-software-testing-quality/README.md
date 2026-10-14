# Module 22-07 — Testing and Quality Assurance for Scientific Code

**Stages:** research · **Prerequisites:** module 22-01 (software design and review) and
module 22-02 (environments and workflows), or equivalent experience maintaining a numerical
code with a test suite.

This module is about the part of research software that decides whether a result can be
trusted and a pipeline can be changed safely: **tests, integration, goldens, benchmarks and
documentation, each with a measured floor**. The organising idea is that every quality claim
is a measurement, and that a measurement has a noise floor. A floating-point tolerance, an
alert threshold, a coverage figure and a documentation percentage are all statements that
can be placed between two numbers — the floor below which nothing is detectable and the
error above which the claim is false.

The first thread is **what a test can assert about a number**. A forward-difference
derivative has a minimum error of 1.407e-08 at $h = 10^{-8}$, near $\sqrt{\varepsilon}$:
assert $10^{-8}$ at $h = 10^{-14}$ and the test declares correct code broken. The same
arithmetic, applied to a variance with a large offset, gives −4.000 000 000 in float64 and
−2 948 661 248.0 in float32 — a golden recorded from that formula rejects the correct answer
and accepts the wrong one.

The second thread is **what a suite is worth**. Coverage is an upper bound on detection: the
module's model gives 0.946 weighted coverage and a 0.751 mutation kill rate, and a
100 %-coverage suite with weak assertions scores 0.600. The gap names the missing assertion,
which is what makes the per-operator-class table actionable where the aggregate number is
not.

The third thread is **the cost of noise**. A 600-test suite with a 1 % per-test flake rate is
red on 99.76 % of pushes, and a red build then implies a real defect with probability 0.100 —
90 % of red builds are noise. A benchmark measured once at 10 % run-to-run noise has a 95 %
decision threshold of 0.1618, larger than the 10 % regression it is meant to catch. A
performance alert with a threshold below the floor produces 1 535 false alarms a year.

The fourth thread is **where the measurements come from**. Operation counts are exact and
expose a complexity change through a fitted slope (1.100 for $O(n\log n)$ against 2.000 for
$O(n^2)$); content-addressed cache keys limit invalidation to a change's descendants; and a
golden value carries eight fields, the most important of which is the reason it is the right
value.

All numbers in this module are **SYNTHETIC** or **measured on this platform's IEEE-754
arithmetic and stated as such**. Cost multipliers, flake rates, job durations, mutation
strengths, noise levels and documentation statistics are chosen teaching values; no CI
service, cluster or real benchmark was used.

## Learning objectives

By the end of this module you will be able to:

1. Classify the defects a scientific code carries and choose the test type — exact, value,
   property, metamorphic, convergence, golden — that detects each.
2. Measure a computation's round-off floor and place a tolerance between that floor and the
   smallest error worth catching.
3. Use mutation kill rates by operator class to say where assertions are missing, and explain
   why coverage is only an upper bound.
4. Size a CI matrix, compute suite-level failure rates from flake rates, and choose a retry
   and quarantine policy that removes noise without hiding real intermittent failures.
5. Record a golden value with its provenance, compute what a code change invalidates from a
   dependency graph, and choose between bitwise and numerical comparison with the
   false-alarm rate known.
6. Compute the repeats a performance comparison needs, convert a threshold into an expected
   alarm rate, and use operation counts to separate algorithmic change from machine change.
7. Decide what documentation tests should assert and state what they cost and what they
   cannot prove.

## Prerequisites

- [22-07-01 Test Strategy for Numerical and Data Code](01-test-strategy-science.md) is the
  entry point; the later lessons assume its assertion vocabulary and its tolerance discipline.
- [22-02-02 Pinning Environments and Managing Dependencies](../02-reproducible-workflows/02-environment-pinning.md) —
  the lock file a clean CI job installs from.
- [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md) —
  the identifiers a golden and a cache key are built from.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Test Strategy for Numerical and Data Code](01-test-strategy-science.md) | research | A defect found in the field costs 22.10 units against 7.30 in a unit test; 0.946 coverage hides a 0.751 kill rate; the forward-difference floor is 1.407e-08 at $h = 10^{-8}$ |
| 02 | [Continuous Integration for Research Software](02-continuous-integration.md) | research | 24 jobs of 8.5 min are 204 machine-minutes with an 8.5-minute floor; 600 tests at 1 % flake are red on 99.76 % of pushes, and 90 % of red builds are noise |
| 03 | [Regression Testing Against Known Results](03-regression-testing-data.md) | research | Reordered sums differ by 2.6e-14; a naive variance is −4.000 000 000 in float64; a change to `load` invalidates 100 % of a 15.6-hour pipeline, a change to `report` 2.6 % |
| 04 | [Benchmarking, Performance Tracking and Documentation Tests](04-benchmarking-and-docs.md) | research | One run at 10 % noise has a threshold of 0.1618 for a 10 % effect; counts expose slopes of 1.100 and 2.000 exactly; 136 docstring examples cost 6.8 s |

## Suggested path

**If you are fixing a suite that nobody trusts:** read 01 §4 for the coverage/kill-rate
distinction, then 02 §3–4 for flakes and retries. Those two sections explain most of the
frustration.

**If you are writing the first tests for a new code:** read 01 in full, then 03 §2–3 to set
tolerances, then 02 §6 for what the pipeline must check beyond unit tests.

**If you own a pipeline or a benchmark:** read 03 §4–6 for invalidation and goldens, then 04
in full for timing and documentation.

**If you are here for the measurements:** every demo is self-contained, prints labelled
values with their units and their noise, and runs in under a second; the ★★★ exercises ask
you to design measurements on your own code.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-test-strategy-science.md`](01-test-strategy-science.md) | Lesson 01 |
| [`02-continuous-integration.md`](02-continuous-integration.md) | Lesson 02 |
| [`03-regression-testing-data.md`](03-regression-testing-data.md) | Lesson 03 |
| [`04-benchmarking-and-docs.md`](04-benchmarking-and-docs.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/test_strategy_science_demo.py`](code/test_strategy_science_demo.py) | Shift-left defect costs, the forward-difference error table, mutation kill rates by operator class, the diminishing returns of suite size |
| [`code/continuous_integration_demo.py`](code/continuous_integration_demo.py) | Matrix jobs and machine-minutes, wall-time floors, flake rates and the Bayes posterior, retries and masking, sharding and its imbalance floor |
| [`code/regression_testing_data_demo.py`](code/regression_testing_data_demo.py) | Round-off floor of a reordered sum, three variance formulas, workflow fan-out invalidation, false-alarm rates of comparison tolerances |
| [`code/benchmarking_and_docs_demo.py`](code/benchmarking_and_docs_demo.py) | Repeats needed per effect and noise level, false alarms per year, estimator bias, operation-count slopes, documentation-test cost |

## How to run the demos

```bash
cd 22-data-engineering-reproducibility/07-software-testing-quality/code

/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python test_strategy_science_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python continuous_integration_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python regression_testing_data_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python benchmarking_and_docs_demo.py
```

Every demo prints labelled results with units, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access, writes no files and exits 0. Each
runs in well under a second. The floating-point numbers they print are measured on the
machine running them; the last digits may differ elsewhere, which is itself the point of
lesson 03.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A group maintains a 500-test suite for a numerical library, run on every push (20 pushes a
> day, 250 days), with a CI matrix of 3 systems × 3 interpreters and a benchmark job.
> **(a)** One test is flaky 1 % of the time. Compute the probability that a push is red, and
> the posterior that a red build is a real defect for a prior of 0.1. **(b)** Compute the
> false alarms per year if the benchmark alerts on a 5 % slowdown measured once, with 10 %
> noise, and state the rule change you would prefer. **(c)** The suite's assertion tolerance
> is `rtol=1e-14` and it fails on a second machine; state the measurement that decides
> whether this is round-off or a defect. **(d)** The team's documented API is 300 functions,
> 80 % with docstrings, 40 % of those with an example; compute the CI cost of running the
> examples at 0.05 s each and state what the examples catch. **(e)** A change to the QC stage
> of their 20-hour pipeline invalidates 9 of 14 stages; state the cache key you would use and
> one reason "the cache is not helping" is correct behaviour. **(f)** State the one quality
> figure you would stop reporting, and what you would report instead.

Worked versions of (a)–(f) appear in the lesson solutions at ★★ and ★★★ level.

## Common pitfalls across this module

1. **A tolerance picked by habit.** An `atol` of $10^{-8}$ is 11× the value it checks in
   lesson 01's example.
2. **Treating coverage as a target.** 94.6 % coverage with a 0.751 kill rate is the same
   suite; the per-class table says what is missing.
3. **A red build that usually means nothing.** 90 % of red builds are noise at a 1 % flake
   rate in a 600-test suite.
4. **Silent retries.** Three attempts hide a real 5 % intermittent failure in 92.8 % of
   pushes.
5. **Recording a golden from the code's own output.** A cancelling formula makes the test
   reject the correct answer.
6. **Re-blessing a golden to make the build green.** It deletes the test.
7. **A benchmark threshold below the noise floor.** 1 535 false alarms a year in lesson 04's
   setting; the response is to stop reading alerts.
8. **Comparing single runs.** At 10 % noise one measurement cannot see a 10 % change.

## Related modules

- [22-01 Research Software Engineering](../01-research-software-engineering/README.md) —
  the design, review and documentation practices these tests verify.
- [22-02 Reproducible Computational Workflows](../02-reproducible-workflows/README.md) —
  environments, workflows and data versions that the pipeline checks.
- [22-03 Data Formats and Engineering](../03-data-formats-and-engineering/README.md) —
  the schemas, QC rules and pipelines that the data tests assert on.
- [19-07 Verification, Validation and Uncertainty](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/README.md) —
  the activity that testing cannot replace.
