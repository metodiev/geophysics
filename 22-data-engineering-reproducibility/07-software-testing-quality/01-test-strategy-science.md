---
id: 22-07-01
title: "Test Strategy for Numerical and Data Code"
level: research
prereqs: ["22-01-01", "22-02-01"]
estimated_minutes: 55
tags: [testing, floating-point, mutation-testing, verification, numerical-code]
---

# Test Strategy for Numerical and Data Code

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** the defects a scientific code carries — interface, unit, formula, data and
   numerical — and **say** which test type can detect each.
2. **Place** a floating-point tolerance between the computation's round-off floor and the
   smallest error worth catching, and **state** why an absolute tolerance cannot be used
   across scales.
3. **Explain** why line coverage is an upper bound on a suite's detection power, and
   **use** mutation kill rates by operator class to say where assertions are missing.
4. **Choose** among example-based, property-based, metamorphic, invariant and regression
   tests for a stated piece of numerical code, and **justify** the choice.
5. **Estimate** the cost of finding a defect at each stage of a project and **state** what
   that estimate implies for where testing effort belongs.
6. **State** the limits of a test suite: which defects it cannot find, and what
   verification has to carry instead.

The cost multipliers, discovery fractions, coverage and assertion strengths used here are
**SYNTHETIC** chosen teaching values. The floating-point results are measured on this
platform's IEEE-754 doubles and are reproducible there; the mutation kill rates are
simulated with `np.random.default_rng(20261014)` and match the stated products.

## Prerequisites

- [22-01-01 Designing Software for Scientific Research](../01-research-software-engineering/01-software-design-science.md) —
  the module structure that makes a function testable at all.
- [22-07-02 Continuous Integration for Research Software](./02-continuous-integration.md) —
  where these tests run and what a red build has to mean.

## 1. Intuition: a test asserts a property, not a feeling

A test is a claim that survives execution: *this input produces that output*, *this
invariant holds*, *this transformation leaves the answer unchanged*. For numerical and
data code the difficulty is that "that output" is a floating-point number, a large array,
or a file, so the interesting question is not how to write a test but **what can be
asserted** about such an object. There are only five answers, and a strategy is mostly a
matter of matching the claim to the object:

1. **Exact equality** on quantities that must be exact — counts, indices, flags, integer
   identifiers, set membership, schema fields.
2. **A value within a tolerance**, where the tolerance is derived from a measured
   round-off floor (§3).
3. **A property**: symmetry, conservation, monotonicity, positivity, a bound that must
   hold for every input, checked on randomly drawn inputs.
4. **A relation between two computations** (metamorphic testing): doubling the amplitude
   doubles the output, translating the input shifts the answer, refining the mesh changes
   it by less than the discretisation error.
5. **A value recorded from a previous run** (a regression golden), which is a claim about
   the past and must be re-derived when the platform changes (§4 of
   [22-07-03](./03-regression-testing-data.md)).

Most weak suites use only (2) and (5), with a tolerance guessed rather than measured.

## 2. Where a defect is found: the shift-left cost model

A defect's cost is dominated by how late it is found. In the demonstration's SYNTHETIC
model, discovery fractions and repair multipliers are chosen as:

| stage | strong unit suite | no unit tests | repair multiplier |
| :--- | ---: | ---: | ---: |
| unit | 55 % | 20 % | 1 |
| integration | 25 % | 30 % | 3 |
| acceptance | 12 % | 18 % | 10 |
| field | 8 % | 32 % | 60 |

The expected cost per defect is $\sum_i d_i m_i$:

- strong unit suite: $0.55 + 0.75 + 1.20 + 4.80 = 7.30$ units;
- no unit tests: $0.20 + 0.90 + 1.80 + 19.20 = 22.10$ units.

That is **3.03×** per defect, and at 120 defects a year, 1 776 units. The model is crude
and the multipliers are conventions; the structural point is not. The field term dominates
because it is multiplied by 60, so *moving 10 % of the defects from field to unit* saves
$0.10 \times 59 \times 120 = 708$ units a year by itself. Effort spent on the cheapest
detection mechanism available — a unit test that runs in milliseconds — buys more than
effort spent on a faster end-to-end suite.

## 3. What a numerical test can assert

Consider the most elementary numerical trap: a forward-difference derivative of
$\sin x$ at $x = 1$, where $f'(1) = \cos 1 = 0.5403023058681398$. The truncation error
falls as $O(h)$ and the round-off error grows as $O(\varepsilon/h)$, so the measured error
has a minimum:

| $h$ | absolute error | relative error |
| ---: | ---: | ---: |
| $10^{-1}$ | 4.294e-02 | 7.947e-02 |
| $10^{-4}$ | 4.207e-05 | 7.787e-05 |
| $10^{-8}$ | 1.407e-08 | 2.604e-08 |
| $10^{-11}$ | 1.169e-06 | 2.163e-06 |
| $10^{-14}$ | 3.707e-03 | 6.861e-03 |
| $10^{-16}$ | 5.403e-01 | 1.000e+00 |

The smallest error is 1.407e-08 at $h = 10^{-8}$, close to
$\sqrt{\varepsilon} = 1.49\times10^{-8}$. Three consequences:

- **The tolerance must be at the floor, not below it.** An `atol` of $10^{-8}$ passes at
  $h=10^{-8}$ and fails at $h=10^{-14}$ — where the *same* correct code produces an error
  of 3.7e-03. A test that asserts $10^{-8}$ at $h=10^{-14}$ asserts that the code is
  broken.
- **An absolute tolerance does not transfer across scales.** A value of $9.0\times10^{-10}$
  is 11× smaller than an `atol` of $10^{-8}$: the tolerance would accept a 1 100 % error.
  Use a relative tolerance with an absolute floor — the demonstration's suggestion is
  `atol=1e-12, rtol=1e-9` — and state both.
- **A tolerance is a measurement, not a convention.** Take the difference between two
  orderings of the same sum, or between two dtypes, and set the tolerance two orders of
  magnitude above it ([22-07-03](./03-regression-testing-data.md) §2 does exactly that).

## 4. Coverage is an upper bound

Line coverage answers "was this line executed?". A defect is only *found* if the line was
executed **and** some assertion observed its effect. The demonstration models this per
mutation operator class with a coverage $c$ and an assertion strength $a$:

| operator class | coverage $c$ | assertion $a$ | simulated killed | $c\,a$ |
| :--- | ---: | ---: | ---: | ---: |
| arithmetic operator | 0.98 | 0.92 | 0.902 | 0.902 |
| condition or boundary | 0.86 | 0.74 | 0.638 | 0.636 |
| constant or unit | 0.95 | 0.88 | 0.836 | 0.836 |
| statement deletion | 0.99 | 0.55 | 0.547 | 0.544 |

The simulated kill rates agree with the product, as they must by construction, and give
the two readings that matter:

- weighted coverage is **0.946** while the kill rate is **0.751** — the suite *looks*
  94.6 % complete and is 19.5 points weaker;
- a suite at **100 % coverage** whose assertions observe only 60 % of what executes scores
  **0.600**, below every class here.

So coverage is an upper bound, and a *reported* upper bound at that: the actionable number
is the kill rate **per operator class**, because the weakest class names the missing
assertion. In the table, condition/boundary mutants (0.638) and deleted statements (0.547)
are the gaps — which is a concrete instruction: add assertions on both sides of each
threshold and assert on return values instead of calling functions for their side effects.

## 5. Choosing the test type

| defect class | example | test type that finds it |
| :--- | :--- | :--- |
| interface | argument order swapped, renamed field | example-based unit test; a docstring example |
| unit | metres used where feet were promised | property test on a *known* conversion; assertion on physical bounds |
| formula | wrong sign, missing factor | value test against an independent implementation at a reference point |
| data | wrong reference system, wrong units in the file | schema and range checks on load; a fixture with an audited answer |
| numerical | cancellation, insufficient iterations | tolerance test at the measured floor; convergence-rate test |
| regression | a refactor changed the answer | golden test with a stated tolerance and provenance |
| emergent | wrong answer only in the coupled workflow | metamorphic or end-to-end test on a small, audited case |

Two of these deserve emphasis because they are what a numerical suite usually lacks.

**Independent reference values.** A value test is only as good as its source. Prefer a
closed-form solution, a hand-computed small case, or an independent implementation; a value
copied from the code's own output tests nothing. The demonstration's §2 shows the failure
mode at full strength: a golden value computed with a cancelling formula would *reject* the
correct answer.

**Properties and metamorphic relations.** They are the only assertion types that scale to
an infinite input space: `energy(rotated_input) == energy(input)`,
`f(2x) == 2f(x)` for a linear operator, `error(n/2) / error(n) ≈ 2` for a first-order
scheme. They need no golden value, they survive a platform change, and they fail loudly
when a "harmless" refactor is not.

## 6. Practice: what to test in a numerical core

A workable checklist, in the order a reviewer will look for it:

1. **The interface**: every public function called once with valid input, once with the
   documented edge case (zero, empty, single element), and once with invalid input
   expecting a stated exception.
2. **Units and bounds**: a test that a physical quantity has the magnitude its units
   imply (a gravity anomaly of $10^{12}$ m/s² is a unit bug), and that outputs are finite.
3. **A known answer**: one small case with a hand-derived value, at a tolerance derived
   from the floor.
4. **A property**: conservation, symmetry, positivity, or a monotonicity that the physics
   guarantees.
5. **Convergence**: for a discretisation, check the order — halve the step and assert the
   error falls by the expected factor, which is a far stronger statement than one value.
6. **A regression golden**: one representative case, with `atol`, `rtol`, dtype, seed,
   platform and code version recorded next to the value.
7. **Determinism**: two runs with the same seed give identical output; a run with a
   different seed gives a statistically consistent result.

## 7. Worked example: the suite that was green for two years

A library converts depths between a measured depth and a true vertical depth. Its test
suite has 96 % line coverage and 214 tests, all passing. A field project reports misfits of
a few per cent. The cause: one function takes a mean-sea-level correction and, in a branch
taken only for offshore wells, adds it with the wrong sign. The branch is *executed* by the
suite (coverage includes it) but no test asserts the returned number — the mutant analysis
of §4 puts statement mutants in exactly this class at 0.547. Two assertions would have
caught it: a value test at a known offshore well, and a property test that an increasing
depth difference produces an increasing correction. The lesson is not "increase coverage";
coverage was already 96 %. It is that *executed* and *asserted* are different, and the
mutation table says which of the two your suite is short of.

## Assumptions and regime of validity

- **The cost multipliers are conventions.** The 3.03× ratio is an artefact of the chosen
  numbers; the ordering (later detection costs more) is the robust part.
- **Mutation scores depend on the operator set.** A kill rate is relative to the mutations
  you inject; comparing two suites requires the same operators.
- **The floating-point floor is platform-specific.** The measured 2.6e-14 spread and the
  $\sqrt{\varepsilon}$ minimum are properties of IEEE-754 double arithmetic and this
  computation; other hardware, compilers and libraries shift the last digits.
- **Properties can be wrong too.** A conservation test that encodes the wrong conservation
  law passes forever; properties inherit the same need for review as code.
- **Tests are necessary, not sufficient.** Verification and validation
  ([19-07](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/README.md))
  decide whether the equations are the right ones; testing decides whether the code
  implements them.

## The honest summary

1. Match the assertion to the object: exact for counts and indices, toleranced for floats,
   properties for infinite input spaces, goldens for the past.
2. Set tolerances from a measured round-off floor; absolute tolerances do not transfer
   across scales.
3. Coverage is an upper bound; per-operator-class kill rates tell you where the assertions
   are missing.
4. Independent reference values and metamorphic relations are the two most valuable and
   most commonly missing test types.
5. Effort spent on cheap early detection outperforms effort spent polishing end-to-end
   suites — 10 % of the field defects moved to unit tests is worth 708 units a year in the
   demonstration's model.
6. State what your suite cannot detect, and which other activity covers it.

## Python demonstration

[`code/test_strategy_science_demo.py`](./code/test_strategy_science_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. the discovery fractions, the 7.30 vs 22.10 units per defect and the 3.03× ratio;
2. the forward-difference error table from $h = 10^{-1}$ to $10^{-16}$, the minimum at
   $h = 10^{-8}$, and the two tolerance failures;
3. the mutation table by operator class, with 0.946 coverage against a 0.751 kill rate;
4. the diminishing returns of suite size — 50 tests buy 0.9502 of the detectable defects,
   200 tests cost four times the runtime to buy the last 0.0498.

```bash
cd 22-data-engineering-reproducibility/07-software-testing-quality/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python test_strategy_science_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/01-test-strategy-science-exercises.md`](./exercises/01-test-strategy-science-exercises.md)
and
[`exercises/01-test-strategy-science-solutions.md`](./exercises/01-test-strategy-science-solutions.md).

## Mastery checkpoint

Without notes, for a function that computes a discrete Laplacian and returns a float array:

1. Name four defect classes it can carry and the test type that finds each.
2. Explain why a coverage figure alone cannot tell you whether the suite would catch a sign
   error, using the executed-versus-asserted distinction.
3. State where the round-off floor for its output comes from and how you would measure it.
4. Write down one property and one metamorphic relation it must satisfy.
5. State one defect class your tests cannot find and the activity that covers it.

## Common pitfalls

1. **A tolerance picked by habit.** An `atol` of $10^{-8}$ is 11× the value it is checking
   in the demonstration's example.
2. **Comparing against the code's own output.** A golden derived from a cancelling formula
   rejects the correct answer.
3. **Treating coverage as a target.** 94.6 % coverage and a 0.751 kill rate are the same
   suite.
4. **Testing only the happy path.** Whole parameter regimes — the offshore branch above —
   are executed and never asserted.
5. **No independent reference.** Without a closed-form or hand-derived case, every test
   compares the code with itself.
6. **Assuming a green suite means correct science.** Testing addresses implementation;
   validation addresses the model.
7. **Asserting on printed text.** Format changes then fail tests that have nothing to do
   with the physics.

## Where this is used

- **Numerical libraries and kernels** — the tolerance and convergence tests of §3:
  see [19-07 Verification, Validation and Uncertainty](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/README.md).
- **Data ingestion and QC code** — schema, range and unit assertions:
  see [22-03-05 Automated Quality Control and Flagging](../03-data-formats-and-engineering/05-data-quality-control.md).
- **Regression goldens in a pipeline** — how the recorded value is produced and blessed:
  see [22-07-03 Regression Testing Against Known Results](./03-regression-testing-data.md).
- **Where the suite runs** — the matrix, flakes and sharding:
  see [22-07-02 Continuous Integration for Research Software](./02-continuous-integration.md).

## Related lessons

- [22-07-02 Continuous Integration for Research Software](./02-continuous-integration.md) —
  running the suite and keeping its signal meaningful.
- [22-07-03 Regression Testing Against Known Results](./03-regression-testing-data.md) —
  tolerances, goldens and invalidation.
- [22-07-04 Benchmarking, Performance Tracking and Documentation Tests](./04-benchmarking-and-docs.md) —
  the performance half of quality assurance.
- [22-01-01 Designing Software for Scientific Research](../01-research-software-engineering/01-software-design-science.md) —
  the structure that makes this testing possible.

## Self-assessment checklist

- [ ] I can match a defect class to a test type without looking it up.
- [ ] I can measure a round-off floor and place a tolerance above it.
- [ ] I can explain why coverage is an upper bound and use kill rates by operator class.
- [ ] I can write a property test and a metamorphic relation for a numerical kernel.
- [ ] I can derive a golden value from an independent source and record its provenance.
- [ ] I can state what my suite cannot detect.
