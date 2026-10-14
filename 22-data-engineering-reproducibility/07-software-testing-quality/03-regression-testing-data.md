---
id: 22-07-03
title: "Regression Testing Against Known Results"
level: research
prereqs: ["22-07-01", "22-02-05"]
estimated_minutes: 55
tags: [regression-testing, golden-values, tolerance, float-comparison, invalidation]
---

# Regression Testing Against Known Results

## Learning objectives

By the end of this lesson you will be able to:

1. **Measure** a computation's round-off floor and **place** a comparison tolerance
   between that floor and the smallest error worth catching.
2. **Recognise** when a golden value must not be computed by the formula under test, and
   **state** what to record instead.
3. **Compute** what a code change invalidates from a workflow's dependency graph, and
   **choose** a cache key that invalidates neither too much nor too little.
4. **Compare** bitwise and numerical comparison of results, and **state** the false-alarm
   rate and the blind spot of each.
5. **Record** a golden value with enough provenance that a future maintainer can tell a
   platform shift from a defect.
6. **State** what regression testing cannot establish, and which of the five test types of
   [22-07-01](./01-test-strategy-science.md) supplies it.

The floating-point results here are measured on this platform's IEEE-754 doubles with
`np.random.default_rng(20261014)` and are reproducible there. The workflow in §4 is a
chosen **SYNTHETIC** teaching DAG; the 15.6-hour pipeline and its fan-out are not a
measurement of any real pipeline.

## Prerequisites

- [22-07-01 Test Strategy for Numerical and Data Code](./01-test-strategy-science.md) —
  the five kinds of assertion and why coverage is an upper bound.
- [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md) —
  the identifiers a cache key is built from.

## 1. Intuition: a golden value is a claim about the past

"Regression" means a change that makes the software worse. A regression test is therefore an
assertion about *stability*: this result must not change, or must not change by more than a
stated amount. That framing produces three obligations immediately:

1. **Someone must know what the value should be.** A value recorded from the code's own
   output asserts only that the code is what it was — a tautology if the code was already
   wrong.
2. **The tolerance must be justified by arithmetic**, not by convenience: too tight and the
   test fails on a legitimate refactor or a different machine; too loose and it passes a real
   error.
3. **The value must be invalidated deliberately.** Stale goldens that nobody dares change are
   indistinguishable from no goldens at all; the invalidation rule is part of the test.

## 2. Measuring the round-off floor

The first task is to find out how much a *correct* computation varies. The demonstration sums
$10^6$ values near $10^6$ in two legal orders:

| quantity | value | relative error |
| :--- | ---: | ---: |
| exactly rounded sum (`math.fsum`) | 999 999 999 154.6199 | 0 |
| sequential accumulation | 999 999 999 154.6459 | 2.600e-14 |
| pairwise accumulation (numpy) | 999 999 999 154.6199 | 0 |

Two orderings of the same addition differ by **2.6e-14** relative. That number is the floor
for this computation, and it turns a tolerance from a guess into a choice:

| tolerance | above the floor | below a real error by |
| ---: | ---: | ---: |
| `rtol = 1e-12` | 38× | 10⁹× (a 1e-3 error) |
| `rtol = 1e-9` | 38 460× | 10⁶× (a 1e-3 error) |
| `rtol = 1e-6` | 3.8e7× | 100× (a 1e-4 error) |

The rule that follows: **measure the floor, then set the tolerance two orders of magnitude
above it**, and record the measured floor next to the tolerance in the test. A tolerance
without its justification is an invitation to "just loosen it" the first time a machine
differs. Note also that the floor grows with problem size and falls with precision; both
belong in the test's metadata.

## 3. Golden values that lie: catastrophic cancellation

Tolerances cannot rescue a golden that was computed by a bad formula. The demonstration
computes the variance of $10^6$ values with mean $10^8$ and standard deviation 1 — a
situation that arises whenever data has a large offset, which in geophysics means almost
always (absolute gravity, elevation, time in seconds since an epoch):

| method | variance | error |
| :--- | ---: | ---: |
| two-pass (subtract the mean first) | 1.000131678 | — |
| $\mathbb{E}[x^2] - \mathbb{E}[x]^2$, float64 | −4.000000000 | 500 % |
| $\mathbb{E}[x^2] - \mathbb{E}[x]^2$, float32 | −2 948 661 248.0 | meaningless |

The naive formula loses every significant digit to cancellation: the squares reach $10^{16}$
and the difference of two such numbers is the quantity of interest. In float32 — whose
resolution is 1.2e-07 — the result is a **negative variance**.

Three lessons:

- **A golden recorded from the naive formula rejects the correct answer and accepts the
  wrong one.** This is the worst possible failure of a regression test, and it is common,
  because the fastest way to create a golden is to print what the code produces.
- **Some assertions should not be numerical at all.** The property `variance >= 0` catches
  the float32 failure instantly; symmetry, positivity and conservation properties catch
  whole classes that no stored number can.
- **Offset your data before comparing.** Subtracting a reference value (a mean, a datum,
  a start epoch) is the single most effective way to make a comparison meaningful, and it
  belongs in the test as a documented transformation.

## 4. What a code change invalidates

A regression suite is rarely a single number; it is a set of recorded results spread over a
pipeline. When a stage changes, everything downstream of it is suspect — and everything
upstream is not. The demonstration's SYNTHETIC 12-stage pipeline costs 15.6 hours in total:

| changed stage | stages invalidated | hours | share of the pipeline |
| :--- | ---: | ---: | ---: |
| load | 11 of 12 | 15.6 | 100.0 % |
| qc | 10 of 12 | 15.4 | 98.7 % |
| grid | 9 of 12 | 14.9 | 95.5 % |
| invert | 6 of 12 | 11.6 | 74.4 % |
| migrate | 5 of 12 | 5.6 | 35.9 % |
| attributes | 4 of 12 | 3.1 | 19.9 % |
| figures | 2 of 12 | 0.8 | 5.1 % |
| report | 1 of 12 | 0.4 | 2.6 % |
| export | 1 of 12 | 0.8 | 5.1 % |
| archive | 0 of 12 | 0.2 | 1.3 % |
| training_set | 1 of 12 | 1.1 | 7.1 % |
| metrics | 0 of 12 | 0.3 | 1.9 % |

Read the table as a map of where the work is: a change to the loader is a full rebuild, a
change to the report stage costs 24 minutes. Two design consequences:

- **Invalidate by content, not by touch.** A cache key built from file modification times
  invalidates the whole pipeline when someone touches a file; a key built from content hashes
  of the inputs *and* the code of the stage invalidates exactly the descendants. This is the
  same content-addressing that a workflow manager uses to decide what to rerun
  ([22-02-03](../02-reproducible-workflows/03-workflow-managers.md) §5).
- **Inspect the key's reach.** A change to `load` or `qc` legitimately invalidates 98–100 %
  of the pipeline, so "the cache did not help" there is correct behaviour, not a bug. The
  savings are concentrated in the late, cheap, frequently edited stages (`report`,
  `figures`, `metrics`) — which is exactly where a figure's axis label changes.

## 5. Bitwise versus numerical comparison

Two ways to compare a computed value with a golden:

**Bitwise equality.** Catches every difference, including the last bit; that is also its
defect. The demonstration measures how often a legitimate refactor — reordering sums, which
is what a compiler or a library upgrade does — changes the bits: for perturbations of the
measured floor 2.6e-14,

| tolerance | false alarms | share of legitimate refactors |
| ---: | ---: | ---: |
| 1e-14 | 139 747 | 69.874 % |
| 1e-13 | 25 | 0.013 % |
| 1e-12 | 0 | 0.000 % |
| 1e-9 | 0 | 0.000 % |

Bitwise comparison is the row above 1e-14: **70 % of legitimate refactors alarm**, and the
test is disabled or "fixed" within a month. Bitwise comparison is nevertheless right for
quantities that must be exact — file checksums, integer indices, masks, ordering — and for
quantities produced by integer arithmetic, where there is no round-off to absorb.

**Numerical comparison at a tolerance.** Its sensitivity is the tolerance, and that is also
its limit:

| tolerance | smallest error still caught |
| ---: | :--- |
| 1e-11 | round-off noise only |
| 1e-9 | units, formula and layout bugs of order 1e-8 and larger |
| 1e-6 | large formula and layout bugs |
| 1e-3 | structural changes only |

So a suite needs both halves: exact assertions on counts, indices, flags and hashes, and
tolerance assertions on floating-point arrays with the tolerance stated and justified. The
half that is usually missing is a **property** assertion, which is the only kind that needs
no golden at all.

## 6. Practice: recording a golden value

A golden that a colleague can act on has eight fields, and they cost a few lines of YAML or
a comment block:

1. **The value**, at full precision, in a text format that does not lose it (never a
   screenshot, never a figure).
2. **The tolerance**, as `atol` and `rtol`, with the measured floor that justified it.
3. **The dtype** (`float64`, `float32`, integer) — the tolerance is meaningless without it.
4. **The seed** and the exact input identifier, so the case can be reproduced.
5. **The platform** on which the value was recorded (architecture, compiler, BLAS) — because
   the last digits are a property of the platform.
6. **The code version**, by commit or release, so a future maintainer can see what produced
   it.
7. **The environment**, by lock file hash or container digest.
8. **The reviewer's name and date**, plus one line on *why* this value is the right one
   (a closed-form case, a published dataset, a physically audited result). The "why" is what
   stops the golden from being updated to whatever the code now prints.

Storage and process: keep goldens in the repository (not a local directory), regenerate them
by a script that is itself reviewed (never by hand), and require a pull request that says
which golden changed and why whenever one is reblessed. A golden updated without a reason in
the message is a defect that has been accepted silently.

## 7. Worked example: the golden file everyone edited

A team's repository contains a 40 MB reference-output file used by an end-to-end test. It
fails on a new machine, and the fix is to regenerate it on that machine — which encodes one
platform's round-off into the reference. Six months later it is regenerated again, and the
test now compares two runs of the same machine and catches nothing. The repair has three
parts: (i) replace the 40 MB file with a small, audited case with a known reference value;
(ii) express the end-to-end comparison at a tolerance measured on two platforms, with the
measured floors recorded; (iii) assert properties of the large output (mass balance, finite
values, ranges, the number of records, checksums of the input) rather than its bytes. The
test then answers the question it was meant to answer — did the science change? — instead of
the question it now answers — did this machine produce the same bits?

## Assumptions and regime of validity

- **The round-off figures are platform-specific.** 2.6e-14 and the 500 % cancellation error
  are properties of IEEE-754 double arithmetic and the stated computations on this machine;
  other hardware, compilers and libraries shift them.
- **The DAG is chosen.** The 15.6-hour pipeline is a SYNTHETIC teaching model; the *shape*
  of the fan-out — an early change invalidating almost everything, a late change very little
  — is the general lesson.
- **Independence is assumed in the alarm counts.** The simulated refactors perturb the
  result independently; correlated platform shifts would move the whole distribution and
  require the tolerance to be re-measured rather than widened.
- **A tolerance is not a correctness proof.** It bounds the change of a computed value, not
  its distance from the truth; §3 is the demonstration that a stable value can be a wrong
  value.

## The honest summary

1. Measure the round-off floor and place the tolerance two orders of magnitude above it;
   record both together.
2. Never derive a golden from the formula under test when a cancelling formula is a
   candidate: use an independent implementation and add a property.
3. Invalidate by content hash, and check the key's reach — an early-stage change
   legitimately invalidates almost the whole pipeline.
4. Bitwise comparison alarms on 70 % of legitimate refactors of a floating-point sum;
   tolerance comparison is blind below its tolerance. Use both, for different quantities.
5. A golden has eight fields and a stated reason; the reason is what keeps it from being
   reblessed to whatever the code prints today.
6. Regression tests establish stability, not correctness.

## Python demonstration

[`code/regression_testing_data_demo.py`](./code/regression_testing_data_demo.py) prints,
with `np.random.default_rng(20261014)`:

1. the two orderings of a $10^6$-term sum, differing by 2.6e-14, and the headroom each
   candidate tolerance leaves;
2. the variance computed three ways — 1.000131678 for two-pass, −4.000000000 in float64 and
   −2 948 661 248.0 in float32;
3. the fan-out table for the 12-stage pipeline, from a 100 % invalidation at `load` to 1.3 %
   at `archive`;
4. the false-alarm table for legitimate refactors — 69.874 % at `rtol=1e-14`, 0.013 % at
   `1e-13`, zero at `1e-12` — with the sensitivity classes of each tolerance.

```bash
cd 22-data-engineering-reproducibility/07-software-testing-quality/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python regression_testing_data_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/03-regression-testing-data-exercises.md`](./exercises/03-regression-testing-data-exercises.md)
and
[`exercises/03-regression-testing-data-solutions.md`](./exercises/03-regression-testing-data-solutions.md).

## Mastery checkpoint

Without notes:

1. State how you would measure the round-off floor of a computation whose golden value you
   are about to record.
2. A candidate golden returns a variance of 1.0001 and the code's naive formula prints
   −4.0. State which you record and what else you assert.
3. A stage changes in the middle of a 12-stage pipeline. State what is invalidated, what is
   not, and the cache key you would use.
4. State the false-alarm behaviour of bitwise comparison and one quantity for which it is
   nevertheless correct.
5. State the eight fields of a recordable golden and which one keeps it honest.
6. State the assertion type that needs no golden value, and what it does better.

## Common pitfalls

1. **Recording the code's own output.** A cancelling formula produces a golden that rejects
   the correct answer.
2. **Regenerating on failure.** Re-blessing the golden to make the build green deletes the
   test.
3. **A 40 MB reference file.** Large goldens encode platform noise; assert properties and a
   small audited case instead.
4. **A tolerance without a justification.** The first platform difference invites loosening
   it indefinitely.
5. **Comparing on the wrong dtype.** A `1e-9` tolerance is unreachable for float32 output.
6. **Invalidating everything on any edit.** It makes the pipeline slow and hides which change
   caused the difference.
7. **Invalidating nothing.** A cache key that ignores code changes serves stale results as
   fresh ones, which is worse than a slow pipeline.

## Where this is used

- **Numerical kernels and solvers** — value, convergence and property tests:
  see [22-07-01 Test Strategy for Numerical and Data Code](./01-test-strategy-science.md).
- **Pipeline stage caching** — content-addressed keys and the fan-out of §4:
  see [22-02-03 Workflow Managers](../02-reproducible-workflows/03-workflow-managers.md)
  and [22-03-03 Data Pipelines and Provenance](../03-data-formats-and-engineering/03-data-pipelines.md).
- **Data versioning and identifiers** — what a cache key hashes:
  see [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md).
- **Where the goldens run** — the CI matrix and the measured spread per machine:
  see [22-07-02 Continuous Integration for Research Software](./02-continuous-integration.md).

## Related lessons

- [22-07-01 Test Strategy for Numerical and Data Code](./01-test-strategy-science.md) —
  the assertion types and the floating-point floor.
- [22-07-02 Continuous Integration for Research Software](./02-continuous-integration.md) —
  where goldens execute and what a red build means.
- [22-07-04 Benchmarking, Performance Tracking and Documentation Tests](./04-benchmarking-and-docs.md) —
  measuring performance with the same discipline about noise.
- [22-03-05 Automated Quality Control and Flagging](../03-data-formats-and-engineering/05-data-quality-control.md) —
  the range and consistency assertions that catch bad data before it is compared.

## Self-assessment checklist

- [ ] I can measure a round-off floor and justify a tolerance with it.
- [ ] I can tell when a golden must come from an independent source.
- [ ] I can compute a change's invalidation set from a dependency graph.
- [ ] I can state the false-alarm rate of bitwise comparison and when it is right anyway.
- [ ] I can record a golden with its eight fields and its reason.
- [ ] I can name the assertion type that needs no golden.
