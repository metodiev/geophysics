# Solutions — 22-07-01 Test Strategy for Numerical and Data Code

> Read after attempting. Numbers use the lesson's SYNTHETIC model. Lesson:
> [01 Test Strategy for Numerical and Data Code](../01-test-strategy-science.md).

---

## ★1 — Five kinds of claim

1. **Exact equality** — the number of model cells in the recovered grid, the ordering of
   the station identifiers, the value of a boolean mask.
2. **A value within tolerance** — the anomaly at a station, asserted against a
   hand-computed half-space value.
3. **A property** — the sensitivity matrix is symmetric for a self-adjoint
   parametrisation; the predicted field is positive for a positive density contrast.
4. **A metamorphic relation** — multiplying the density contrast by 2 doubles the anomaly;
   translating the source and the stations together leaves the anomaly unchanged.
5. **A regression golden** — the misfit for one archived, published dataset at a stated
   tolerance.

## ★2 — A third strategy

Costs: $0.40 \times 1 + 0.30 \times 3 + 0.20 \times 10 + 0.10 \times 60
= 0.40 + 0.90 + 2.00 + 6.00 = 9.30$ units. The strong unit suite is 7.30, so this strategy
is **worse by 2.00 units per defect** — despite having a *higher* combined unit+integration
discovery rate (0.70 vs 0.80 for the strong suite? it does not: 0.40+0.30 = 0.70 against
0.55+0.25 = 0.80). The reason for the difference is the field term: 10 % of defects at 60×
costs 6.00 units, against 8 % at 4.80 for the strong suite.

## ★3 — Why coverage is an upper bound

A defect can only be detected if the code containing it **executes** and an assertion
**observes** the consequence. Coverage measures only the first condition, so
detection probability = coverage × observation, and observation ≤ 1 in every case. The
gap is the suite's missing assertion strength — the model calls it the difference between
coverage and the kill rate, which the demonstration measures as **0.946 against 0.751**,
19.5 points.

## ★★4 — A central difference

(a) The error has two competing terms: truncation $C h^2$ and round-off
$\varepsilon |f| / h$. At $h = 10^{-2}$ the truncation term dominates (it is proportional
to $h^2$ and $h$ is large); at $h = 10^{-12}$ the round-off term dominates (it is
proportional to $h^{-1}$).

(b) Setting the two terms equal — $h^2 = \varepsilon / h$, so $h^3 = \varepsilon$, hence
$h = \varepsilon^{1/3} \approx 6\times10^{-6}$ — gives both terms of order
$\varepsilon^{2/3} \approx 3.7\times10^{-11}$. The optimum is therefore about
$h = 6\times10^{-6}$ with an error near $10^{-11}$, one power of $h$ better than the
forward difference of the lesson (which needs $h = \sqrt{\varepsilon}$ and gives an error
near $10^{-8}$).

(c) At the optimum, a quantity of magnitude 1 can be asserted to about
$10^{-10}$ — two orders of magnitude above the error order $3.7\times10^{-11}$ — so
`rtol=1e-10` with `atol=1e-11` is defensible. At $h = 10^{-12}$ the round-off term is
$\varepsilon/h = 2.2\times10^{-4}$, so an assertion of $10^{-10}$ there would fail on
correct code; the honest options are to assert $10^{-3}$ at that step or to change the step.
The demonstration's forward-difference table shows exactly this pattern: 4.207e-05 at
$h=10^{-4}$ falling to 1.407e-08 at $h=10^{-8}$ and rising again to 3.707e-03 at
$h=10^{-14}$.

## ★★5 — Coverage, assertions and kill rates

(a) Statement-deletion mutants die only if an assertion observes the *effect* of the deleted
statement. The 40 assert-free tests raise the coverage of the lines they call but contribute
**nothing** to the kill rate; the model's assertion strength for that class is the lowest in
the table (0.55), which is exactly the class those tests cannot help. Expect the class kill
rate to stay near the coverage × 0.55 product.

(b) Two changes: (i) add assertions to the 40 tests — assert on returned values, array
shapes, invariants and expected errors rather than on "it did not raise"; (ii) add boundary
tests around the thresholds of the branch conditions, which is the second-weakest class
(0.638), by asserting on both sides of each comparison.

(c) You would not chase 100 % coverage. The demonstration shows a 100 %-coverage suite with
weak assertions scoring 0.600, below every class it covers; and the marginal return on
suite size is tiny — 50 tests buy 0.9502 of the detectable defects while 200 tests quadruple
the runtime to buy the remaining 0.0498. Time spent adding coverage-only tests is time not
spent on assertions.

## ★★6 — Raising the tolerance to $10^{-4}$

(a) Two causes: (i) the computation genuinely differs across platforms — a different BLAS,
vectorisation order or FMA contraction changes the last digits, so the round-off floor
differs; (ii) the suite wrongly compares values that should not be compared at all — an
uninitialised element, a hash or an ordering that is not deterministic. Distinguish them by
measuring: print the two values and their difference, and check whether the difference is at
the round-off floor of the magnitudes involved (cause (i)) or orders of magnitude larger
(cause (ii), a real bug or a non-deterministic comparison).

(b) A tolerance of $10^{-4}$ would stop detecting anything smaller than 0.01 %: a units
error in a factor, a wrong constant in the third decimal, an off-by-one in an interpolation
index that shifts the result by $10^{-5}$, a formula error of order $10^{-5}$. The
demonstration's headline cancellation case is worse: the naive variance formula is wrong by
**500 %** and its value is negative, so a *property* test (`variance >= 0`) catches it
while no tolerance setting would have saved a golden derived from the same formula.

(c) The change that keeps both: measure the floor, choose the tolerance two orders of
magnitude above it (the lesson's suggestion is `atol=1e-12, rtol=1e-9`, with the *measured*
spread reported in the test docstring), and — critically — check the dtype. A `1e-9`
tolerance is unreachable for float32 code, whose own resolution is 1.2e-7; that is a
statement about the dtype, not about the machine, and it should be fixed by computing in
float64 or by setting a dtype-appropriate tolerance.

## ★★★7 — A suite for a 1-D variable-coefficient diffusion solver

**Exact assertions (3).**

1. For a uniform coefficient and a single Fourier mode, the amplification factor after one
   step equals the analytically known value.
2. The number of unknowns, the sparsity pattern and the symmetry of the assembled matrix
   (counts and structure, asserted exactly).
3. The discrete operator applied to a constant field returns zero (the steady-state
   solution for uniform coefficients), with an assertion of exact zero up to the assembled
   matrix's row-sum tolerance — better, assert that the row sums are exactly those produced
   by the assembly formulas.

**Property tests (2).**

1. **Maximum principle**: for a positive initial condition and positive coefficients, the
   solution stays between the initial max and min.
2. **Mass conservation**: the change in total mass per step equals the boundary flux, for
   randomly drawn coefficients and initial conditions.

**Metamorphic relation (1).** Linearity: running with initial condition $2u_0 + v_0$ gives
$2u + v$ for the same coefficients, to within the (much larger) linear-solver tolerance.

**Convergence test (1).** Refining the grid by 2 reduces the error against a manufactured
solution by approximately $2^p$ for the scheme's order $p$; assert the *ratio* is within a
factor of the expected one over three refinements, which is stronger than any single value.

**Golden regression test (1).** One small case (say 100 cells, fixed coefficients) with the
solution recorded; tolerance $10^{-9}$ relative with an absolute floor of $10^{-12}$,
justified by measuring the spread between two orderings of the same solve (the
demonstration measures 2.6e-14 on a 10⁶-term sum) and multiplying by 100. The golden file
records the solver version, dtype, platform and the tolerance's justification.

**The defect class this suite cannot detect.** A physically wrong but internally consistent
discretisation — for example the wrong interface condition between two layers, which
satisfies conservation and the maximum principle while solving the wrong problem. Only a
manufactured solution derived from the *correct* interface physics, or validation against
analytical two-layer solutions, addresses that class.

## ★★★8 — Post-mortem for a bug that reached a publication

**Establish the facts.**

1. **Was the path executed?** Run the covering test subset with coverage enabled and check
   line and branch coverage of the defective statement, including the *configuration* under
   which the field project's run took place (offshore branch, specific dtype, specific grid
   size). Record whether any test used that configuration.
2. **Was it asserted on?** For the tests that executed the line, inspect whether they make
   any assertion whose failure would depend on that line's value. Distinguish "executed",
   "asserted", and "asserted on a quantity downstream of the defect" — interpolation,
   rounding and masking can hide a wrong value in an aggregate statistic.
3. **Was the class in the mutation set?** Check whether the defect is of a class the mutation
   operators can generate (an operator swap, a boundary change, a constant change, a deleted
   statement). If it is a class the operators cannot generate, the mutation score was
   structurally blind to it, which is a finding about the metric rather than about the suite.
4. **Would a property have caught it?** Try the candidate properties (positivity,
   monotonicity, an independent reference value at an audited case) and record which one
   fails on the buggy code — that is the test to add.

**The two outcomes.**

- **Executed and asserted-for but the mutation set was blind.** Action: extend the operator
  set (e.g. unit-conversion mutations, conditional-direction mutations) so the class is
  measured in future — otherwise the score keeps reporting a strength the suite does not
  have.
- **Executed but not asserted on.** Action: add the assertion, at a value or a property
  level, and add the class to the mutant set so the gap cannot reappear silently. This is
  the case the demonstration's 0.547 statement-deletion class predicts, and it is the more
  common of the two.

## ★★★9 — "Goldens catch everything"

**What goldens catch well.** Behaviour changes to code that runs on the recorded input:
refactors, formula edits, unit errors, dtype changes, library upgrades, threading changes —
with a sensitivity set by the tolerance.

**What they cannot catch.** (i) Defects in code paths the golden's input does not reach; a
golden is one point, and a suite of goldens is a finite sample of an infinite input space.
(ii) Bugs present when the golden was recorded — a golden derived from a wrong formula
freezes the error; the demonstration's cancelling formula is a value 500 % off with a
*negative* variance, and any tolerance wide enough to accept it also accepts a real bug.
(iii) Platform-independent properties: the golden passes until the machine changes, then
fails on a correct refactor.

**Why a golden cannot distinguish a correct refactor from a wrong one.** Both change the
number; the tolerance decides which is accepted. A reordered sum shifts the result by the
round-off floor (2.6e-14 in the demonstration), and a 0.01 % formula error shifts it by
1e-4. With an `rtol` of $10^{-9}$ the first passes and the second fails — but with an `rtol`
of $10^{-3}$ both pass. A property (or an independent reference value) is needed to decide
*which* change is legitimate, because it encodes the mathematics rather than a past output.

**The change that turns a golden suite into an alarm generator.** A new BLAS, a different
compiler with FMA contraction, a change of dtype or a different thread count: the
demonstration's table gives 69.9 % false alarms at `rtol=1e-14`, 0.013 % at `1e-13` and 0 %
at `1e-12` for refactors whose shift is the measured floor. Successive "just raise the
tolerance" responses destroy the detection power exactly as the argument claims — which is
why the tolerance must be tied to a measured floor and the test must state it.

**One afternoon's evidence.** Take the group's five most-edited modules and, for each,
measure the round-off floor (two orderings, two dtypes, two thread counts); record the false
alarm rate at a range of tolerances; then introduce one deliberate unit error in each module
and record the smallest error each test type catches (golden at the current tolerance, value
test against a closed-form case, property test). The table that results — sensitivity versus
false-alarm rate per test type — settles the argument with the group's own code.
