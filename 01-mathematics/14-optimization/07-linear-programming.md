---
id: 01-14-07
title: "Linear Programming and Geophysical Applications"
level: graduate
prereqs: ["01-14-03", "01-14-04"]
estimated_minutes: 90
tags: [linear-programming, simplex, l1-norm, robust-fitting]
---

# Linear Programming and Geophysical Applications

## Learning objectives

By the end of this lesson you will be able to:

1. **State** a linear program in standard form, recognise which geophysical
   problems cast into it, and explain why the optimum lies at a vertex.
2. **Implement** a two-phase simplex method in exact rational arithmetic, and
   explain what the two phases certify.
3. **Cast** L1 and Chebyshev (minimax) regression as linear programs and compare
   them with least squares on data containing a blunder.
4. **Use** duality to certify optimality and to read shadow prices as the
   marginal cost of a specification or a bound.
5. **Verify** a shadow price by direct differentiation of the optimal value, and
   say what the sign convention means.
6. **Decide** when an L1 formulation is worth the loss of smoothness, and when
   least squares remains the right choice.

## Prerequisites

[01-14-03 Constrained Optimisation and Lagrange Multipliers](./03-constrained.md)
for constraints, multipliers and complementarity, and
[01-14-04 Linear and Nonlinear Least Squares](./04-least-squares.md) for the L2
benchmark every robust fit is compared against.

## 1. Intuition: when the constraint is the problem

Linear programming (LP) is optimisation with a linear objective and linear
constraints. Its mathematical speciality is that the feasible set is a polytope
(a bounded polyhedron, or an unbounded one), and the optimum — if it exists —
occurs at a **vertex**. That single fact is why LP is fast and why it comes with
certificates: a vertex is described by a set of active constraints, so an LP
solution is a *list of decisions* ("use end member 1 at 40 per cent, the density
specification is binding, the velocity specification is not") rather than a vector
of numbers to be interpreted.

Geophysics uses LP in three distinct ways, and it is worth keeping them separate:

| Use | Objective | Typical example |
|---|---|---|
| Resource allocation | minimise cost or maximise yield | blending rock-physics end members to a specification |
| Robust fitting | minimise $\sum|r_i|$ or $\max|r_i|$ | fitting a trend to data containing a blunder |
| Bound-constrained inversion | minimise a linear misfit with known bounds | extremal models consistent with gravity data |

The second is the one that changes how you do least squares. Section 4.2 measures
it: one blunder moves a least-squares slope by $+0.88$ and an L1 slope by
$+0.10$, a factor of $8.8$. That difference is not a numerical curiosity; it is
the reason gravity profiles, magnetic traverses and arrival-time datasets are
routinely fitted with L1 norms. The cost is that $\sum|r_i|$ is not
differentiable at $r_i = 0$, so the smooth machinery
of [01-14-04](./04-least-squares.md) does not apply — and the L1 problem becomes
an LP instead.

**The duality is the second half of the lesson.** Every LP has a dual, the two
optimal values are equal for feasible bounded problems (strong duality), and the
dual variables are the marginal costs of the constraints. That is the same
statement as the Lagrange multiplier of
[01-14-03](./03-constrained.md), now with a combinatorial flavour: the optimum of
an LP is a price list.

## 2. Precise definitions

### 2.1 Standard forms

The form used for computation in this lesson is

$$\min\ c^{\mathsf{T}}x \quad\text{subject to}\quad Ax \le b,\quad x \ge 0,
\tag{2.1}$$

and the equality or $\ge$ forms are converted to (2.1) by splitting free
variables ($x = x^{+} - x^{-}$ with $x^{\pm} \ge 0$) and multiplying rows by
$-1$. A problem in **standard form** has only equalities and non-negative
variables; the two-phase simplex of Section 3.1 works there.

Three outcomes are possible: **optimal** (a finite minimum is attained),
**infeasible** (no $x$ satisfies the constraints) and **unbounded** (the objective
can be made arbitrarily negative within the feasible set). A solver must
distinguish all three, and it must say which one it returned.

### 2.2 Vertices, basic solutions and the simplex idea

A vertex of the feasible polytope is a point where $n$ linearly independent
constraints are active, $n$ being the number of variables. Algebraically: choose
a basis of $n$ columns of $[A\ I]$, set the other variables to zero, and solve.
If the resulting basic solution is feasible, it is a vertex. The simplex method
moves from vertex to vertex along edges, always decreasing the objective, until
no edge improves — the **optimality certificate** is that all reduced costs are
non-negative.

This is exactly why LP is fast in practice (the number of vertices visited is
usually a small multiple of $n$, though the worst case is exponential) and why
degeneracy — a vertex where extra constraints are active — causes the
complications discussed in Section 6.

### 2.3 L1 regression as an LP

Minimise $\sum_{i=1}^{n} |a + b x_i - y_i|$ over $(a,b) \in \mathbb{R}^{2}$. Introduce
residual variables $r_i$ and split each into $r_i = r_i^{+} - r_i^{-}$:

$$\min \sum_{i=1}^{n} (r_i^{+} + r_i^{-})
\quad\text{s.t.}\quad a + bx_i - y_i = r_i^{+} - r_i^{-},
\quad r_i^{\pm} \ge 0, \tag{2.2}$$

with $a$ and $b$ themselves split into non-negative parts. At the optimum at most
one of $r_i^{\pm}$ is non-zero (otherwise both could be reduced), so the LP
objective equals $\sum|r_i|$. Variables: $4 + 2n$; constraints: $2n$.
The problem is an LP, so any LP algorithm solves it, and the solution is a vertex
of that polytope — which is why L1 fits have a combinatorial character
(“the fit interpolates some of the data exactly”).

### 2.4 Chebyshev (minimax) regression as an LP

Minimising $\max_i |r_i|$ becomes

$$\min t \quad\text{s.t.}\quad -t \le a + bx_i - y_i \le t . \tag{2.3}$$

This is the smallest box of vertical half-width $t$ containing the fitted line's
residuals. It is an LP with one extra variable and $2n$ constraints, and its
solution is decided by the extreme points — the opposite robustness behaviour to
L1, as Section 4.3 shows.

### 2.5 Duality and shadow prices

The dual of (2.1) is

$$\min\ b^{\mathsf{T}}y \quad\text{s.t.}\quad -A^{\mathsf{T}}y \le c,\quad y \ge 0,
\tag{2.4}$$

whose optimal value equals minus the primal optimum. Writing (2.4) as
$\max\ (-b^{\mathsf{T}}y)$ makes the usual statement: the dual feasible set gives
*lower bounds* on the primal optimum, and strong duality says the best such bound
is attained. The practical reading is the same as in
[01-14-03](./03-constrained.md): if a constraint $a_i^{\mathsf{T}}x \le b_i$ is
written with right-hand side $b_i$, then

$$\frac{d\,z^{*}}{d b_i} = -y_i , \tag{2.5}$$

where $y_i \ge 0$ is that constraint's dual variable. A binding constraint with
$y_i > 0$ has a price; a slack constraint has $y_i = 0$. Section 4.5 verifies
(2.5) by central differences on both an equality-like pair of constraints and a
bound.

## 3. Derivations

### 3.1 The two-phase simplex

*Phase 1.* Add a slack variable to each $\le$ constraint. Rows with negative
right-hand sides are multiplied by $-1$, which makes their slack coefficient
$-1$ and prevents it from serving as a basis variable; for those rows add an
**artificial** variable with coefficient $+1$. Minimise the sum of the artificial
variables subject to the resulting equalities. The minimum is zero if and only if
the original problem is feasible, and a positive minimum is a proof of
infeasibility. This phase is where a solver earns the right to say "infeasible"
rather than "failed".

*Phase 2.* Drive any artificial variable out of the basis (rows that cannot be
driven out are redundant and are dropped), restore the real objective, and
continue the pivoting until no reduced cost is negative. The result is a vertex
where every edge is non-improving, which is the optimality certificate.

*Pivoting and cycling.* With an arbitrary choice of entering variable the method
can cycle on degenerate problems. Bland's rule — always choose the entering
variable with the smallest index among those with negative reduced cost, and
break ties in the ratio test by the smallest index — provably terminates. The
demonstration uses Bland's rule, which is slower than Dantzig's rule but cannot
loop; the measured iteration counts of $4$ to $11$ in Section 4 are therefore
upper bounds on a real solver's count, and that trade is stated rather than
hidden.

*Exact arithmetic.* Every tableau entry here is a `Fraction`. The dividends are
that "optimal" is exact (an exact zero duality gap), that infeasibility is
proved rather than inferred from a tolerance, and that the shadow-price
verification of Section 4.5 can be compared to ten decimal places. The cost is
that the arithmetic is slow and the numbers can grow, which is why production
codes use floating-point simplex or interior-point methods with tolerances — and
why an exact solve is the right tool for a lesson and for a small verification
problem.

### 3.2 Why L1 is robust, in one calculation

Let $r_i = a + bx_i - y_i$ and consider the derivative of the objective with
respect to a single datum $y_k$ for the two norms:

$$\frac{\partial}{\partial y_k}\sum_i r_i^{2} = 2 r_k \frac{\partial r_k}{\partial y_k}
= -2r_k, \qquad
\frac{\partial}{\partial y_k}\sum_i |r_i| = -\operatorname{sign}(r_k). \tag{3.1}$$

The L2 sensitivity to a datum is *proportional to its residual*, so a blunder
with a large residual pulls the fit hard. The L1 sensitivity is $\pm1$ regardless
of magnitude: every datum, blunder or not, pulls with equal force, and the fit
settles where the pulls balance. That is why the L1 solution ignores the
magnitude of the outlier and why several residuals come out exactly zero — at a
kink, the subgradient can balance without moving.

### 3.3 The L1 fit interpolates at least as many data as parameters

Move the line until two residuals hit zero; each zero residual removes one degree
of freedom from the “pull” system. Formally, at any L1 optimum at least one
subset of residuals equal to zero provides the $p$ conditions that pin down the
$p$ parameters, so the fit passes exactly through at least $p$ data points
(generically exactly $p$). Section 4.2 measures $3$ of $5$ residuals zero for a
two-parameter fit — more than the minimum, which happens here because the data
are nearly collinear. This “interpolation” property explains both the robustness
and the occasional sensitivity: which $p$ points are interpolated depends on the
data, and changing one datum can change the active set.

### 3.4 A blending problem

Choosing fractions $x_j \ge 0$ of $m$ end members to meet $k$ specifications
exactly at least cost is

$$\min \sum_j c_j x_j \quad\text{s.t.}\quad
\sum_j x_j = 1,\quad A x = s,\quad x \ge 0, \tag{3.2}$$

with $A$ the property matrix and $s$ the target specifications. Feasibility alone
is a linear-algebra question — if $A$ has more independent rows than the model
can satisfy, the LP is infeasible and no mixture works. When it is feasible, the
dual variables of the $A x = s$ rows are the marginal costs of the specifications:
the price, in cost units, of demanding one more unit of density or velocity. That
is the sentence a petrophysicist wants from the calculation.

## 4. Numerical results

All numbers are from
[`code/linear_programming_demo.py`](./code/linear_programming_demo.py), which
implements the two-phase simplex, the L1 and Chebyshev models and the dual LP in
exact rational arithmetic with the standard library alone.

### 4.1 A blending problem solved exactly

Three end members with densities $(2.60, 2.70, 2.75)$ g cm⁻³, velocities
$(5.8, 5.2, 4.4)$ km/s and costs $(1, 3, 2)$; target density $2.6725$ g cm⁻³ and
velocity $5.24$ km/s, with the fractions summing to $1$:

| quantity | exact value | decimal |
|---|---|---|
| solution $x$ | $(2/5,\ 7/20,\ 1/4)$ | $(0.4000000000, 0.3500000000, 0.2500000000)$ |
| objective | $39/20$ | $1.9500000000$ |
| achieved density | $1069/400$ | $2.6725000000$ |
| achieved velocity | $131/25$ | $5.2400000000$ |
| simplex iterations | $4$ | — |
| dual LP optimum | $-39/20$ | — |
| primal $+$ dual | $0$ | exactly |

The data were generated from the rational solution $(2/5, 7/20, 1/4)$, so the LP
recovered it exactly — including the fractions, which is what exact arithmetic
buys. The dual variables of the six inequality rows are

$$(136.6,\ 0,\ 0,\ 44.0,\ 0,\ 4.0),$$

where rows 3 and 4 are the two halves of the density equality and rows 5 and 6
the velocity equality. The pattern is instructive: the *upper* halves are slack
(zero price) and the *lower* halves carry the price, which is the degenerate
signature of an equality written as two inequalities.

### 4.2 L1 against L2 with a blunder

Data $y = (1, 2, 2, 4, 9)$ at $x = 0,1,2,3,4$, where the last datum is a blunder;
the "clean" data replace $9$ by $4.6$.

| fit | intercept | slope | L1 cost | max $\lvert r\rvert$ |
|---|---|---|---|---|
| L1, blundered data | $1.000000$ | $1.000000$ | $5.000000$ | $4.000000$ |
| L2, blundered data | $0.000000$ | $1.800000$ | $6.000000$ | $1.800000$ |
| L2, clean data | $0.880000$ | $0.920000$ | $5.840000$ | $4.440000$ |
| L1, clean data | $1.000000$ | $0.900000$ | $5.600000$ | $4.400000$ |

Further measured facts:

- Simplex iterations for the L1 problem: $11$ (variables $14$, constraints $10$).
- Exact L1 objective: $5$ — an integer, as exact arithmetic allows.
- Residuals of the L1 fit: $(0,\ 0,\ 1,\ 0,\ -4)$; **three of five are exactly
  zero**, the interpolation property of Section 3.3.
- Slope shifts caused by the blunder: L1 $+0.100000$, L2 $+0.880000$ — ratio
  $8.8$.

Note that the *L2 cost* of the L1 solution ($6.000000$) is larger than the L2
optimum, as it must be: the two methods optimise different functionals, and each
is worse than the other by the other's measure. The relevant comparison is the
shift induced by the blunder, and there L1 wins by almost an order of magnitude.

### 4.3 Chebyshev (minimax) fitting

For the same blundered data, minimising $\max_i |r_i|$:

| quantity | value |
|---|---|
| intercept | $-1/2$ |
| slope | $2$ |
| minimax value | $3/2 = 1.500000$ |
| residuals | $(-1.500000, -0.500000, +1.500000, +1.500000, -1.500000)$ |
| residuals attaining the maximum | $4$ |
| simplex iterations | $8$ |

Four of five residuals attain the maximum, in both signs. The minimax fit is
therefore determined entirely by the extreme data: it is *maximally sensitive* to
the blunder, which is the exact opposite of L1. The three norms form a scale:

- L∞ cares only about the worst datum (robust to nothing, sensitive to one point);
- L2 cares about all data proportional to their residuals;
- L1 cares about all data equally (robust to outliers, insensitive to their
  magnitude).

Choosing a norm is choosing which data you trust, and reporting which one you
chose is part of reporting the fit.

### 4.4 Strong duality, exactly

For the L1 fit of Section 4.2 as an LP with $14$ variables and $10$ constraints:

| quantity | value |
|---|---|
| primal optimum (exact) | $5$ |
| dual optimum (exact) | $-5$ |
| primal $+$ dual | $0$ |
| simplex iterations | primal $11$, dual $9$ |
| non-zero primal variables | $4$ of $14$ |

Primal $+$ dual $= 0$ *exactly*, not to a tolerance. In a floating-point solver
the same statement would be an inequality $\text{primal} + \text{dual} < 10^{-8}$
or similar, and the difference matters when the claim being made is "this is
optimal": exact arithmetic turns the claim into a certificate.

### 4.5 Shadow prices, verified by differentiation

For the blending problem, perturbing the density target by $\pm10^{-4}$ and
differencing the optimal cost gives

$$\frac{d\,z^{*}}{d(\text{density target})} = 44 = 44.000000$$

while the dual variables of the two density rows are $0.000000$ and $44.000000$.
The rule (2.5) explains both the magnitude and which row carries it:

$$(-y_{2})(+1) + (-y_{3})(-1) = y_3 - y_2 = 44 - 0 = 44 .$$

For the bound-constrained fit of Section 4.6 the same check is cleaner still,
because there is only one perturbed row:

| constraining the slope from below | value |
|---|---|
| `d(cost)/d(bound right-hand side)` by central difference | $-1.000000$ |
| rule $-y$ for that row's dual variable | $-1.000000$ |

The economics of LP and the multiplier of
[01-14-03](./03-constrained.md) are the same object, computed two ways.

### 4.6 Constrained fitting: what a bound costs

Fitting the model $a + bx$ to the blundered data with the slope bounded below by
$1.5$ (an independent regional constraint):

| fit | intercept | slope | L1 cost |
|---|---|---|---|
| unbounded | $1.000000$ | $1.000000$ | $5.000000$ |
| bounded $b \ge 1.5$ | $0.500000$ | $1.500000$ | $5.500000$ |

The bound costs $0.500000$ in L1 misfit and moves the intercept by $-0.5$: the
constraint is active and the whole line pivots. Its dual variable is $1.000000$
per unit of right-hand side, i.e. the constraint would cost one unit of misfit
for every extra $0.5$ of enforced slope — the exchange rate between the data and
the prior.

### 4.7 Exact arithmetic versus perturbations

Perturbing every datum by a relative $10^{-12}$ and re-solving the L1 problem
exactly, the worst change in the objective is $8.202\times10^{-12}$. Three of the
five residuals are kinked at the optimum, so the objective is not differentiable
there, yet its *value* is stable: the extremal residual belongs to the blunder,
whose magnitude does not determine the fit (Section 3.2). This is the numerical
counterpart of the robustness statement, and it is why L1 fits are used for data
whose outliers are numerous and whose magnitudes untrustworthy.

## 5. Physical interpretation

**An LP optimum is a decision list.** The active constraints *are* the answer:
“40 per cent end member 1, the density specification is binding, the velocity
specification has slack”. In a mixture or allocation problem this is more
informative than the objective value, and it is what the dual variables summarise.

**Shadow prices are the language of specification.** The price $44$ per unit of
target density says the mixture is density-limited; had the velocity row carried
the price, the design conversation would be about velocity instead. In inversion
the same number is "the misfit cost of imposing this bound", as in Section 4.6
and in [01-14-03](./03-constrained.md).

**Robustness is a norm choice, not an algorithm.** L1, L2 and L∞ are three
statements about measurement error. If the error is Gaussian, L2 is the
maximum-likelihood choice and L1 throws away efficiency for nothing. If a few
data are grossly wrong (a mistied pick, a mislocated station, a spike in a
profile), L2 propagates the error and L1 contains it — measured as $8.8$ to one
in Section 4.2.

**Non-differentiability is a feature, not a defect.** The kinks in $\sum|r_i|$
are where L1 gets its insensitivity: at a kink the subgradient can absorb a
change in one datum without moving the solution. That is why one cannot use
Newton-like methods and why the LP formulation is the natural algorithm.

**Exactness is a diagnostic.** The zero duality gap and the rational solutions of
Section 4.4 are not merely aesthetic: they let a textbook example be checked
completely, which is how the modelling errors of an LP formulation get caught in
practice (a wrong slack sign, a missing bound) before it is applied to data.

## 6. Assumptions and regime of validity

1. **Linearity of the objective and constraints.** Linearity is a modelling
   assumption; approximating a nonlinear specification by a tangent LP is
   legitimate but the tangent must be re-formed as the solution moves — that is
   sequential linear programming, and it is only as good as the tangent.
2. **Determinism of the data.** L1 and L∞ fits treat each datum as exact except
   through the residual. If the data have *known* variances, the correct analogue
   is weighted L1 (or a generalised LP), and the unweighted version is a
   different, biased estimator.
3. **Existence, boundedness, feasibility.** A solver must report infeasible and
   unbounded cases separately; a returned "solution" from an infeasible problem
   is a programming error, and the two-phase construction is what prevents it.
4. **Degeneracy.** Ties in the ratio test make some vertices over-determined; the
   multipliers are then non-unique, and the shadow price of a redundant
   constraint has no economic meaning. Section 4.1's equality-as-two-inequalities
   is exactly this situation.
5. **Cycling.** Bland's rule terminates but is slow; production floating-point
   codes accept a small cycling risk or use a lexicographic ratio test. A quoted
   iteration count is an upper bound under Bland's rule and depends on the rule
   used.
6. **Interior-point alternatives.** Modern LP solvers use interior-point methods,
   which are faster on large problems but do not produce a vertex or a basis
   directly; the certificates of this lesson are the reason simplex remains
   instructive.
7. **L1 and outliers, not L1 and leverage.** L1 protects against a datum with a
   large residual; it does not protect against a datum with large *leverage*,
   where the fit pivots through it. A marginal outlier (high leverage, moderate
   residual in L2 terms) can still mislead an L1 fit.

## 7. Python demonstration

The companion script is
[`code/linear_programming_demo.py`](./code/linear_programming_demo.py), with six
sections: the blending problem and its dual, L1 regression, Chebyshev
regression, strong duality, a bound-constrained fit with a verified shadow price,
and a perturbation study. All arithmetic is exact rational, and the simplex is
implemented from scratch.

| Section | Measured | Interpretation |
|---|---|---|
| 1, blending | $x = (2/5, 7/20, 1/4)$, cost $39/20$, primal $+$ dual $= 0$ in $4$ iterations | the rational solution is recovered exactly |
| 2, L1 vs L2 | slope shifts $+0.100000$ (L1) and $+0.880000$ (L2); residuals $(0,0,1,0,-4)$ | one blunder moves L2 almost nine times further |
| 3, Chebyshev | minimax $3/2$, four residuals at the maximum | the worst datum decides the line |
| 4, duality | primal $5$, dual $-5$, sum exactly $0$; $4$ of $14$ variables non-zero | optimality as a certificate |
| 5, shadow price | d(cost)/d(density target) $= 44 = y_3 - y_2$ | the multiplier is a price, verified |
| 6, bound | $b \ge 1.5$ costs $0.5$ in L1 misfit; d(cost)/d(rhs) $= -1.000000 = -y$ | constraints have exchange rates |
| 7, perturbation | worst objective change $8.2\times10^{-12}$ for $10^{-12}$ data perturbations | the L1 objective value is stable |

> **Breaking exercise.** In Section 2, replace the intercept and slope by a single
> parameter (fit $y = bx$, i.e. force the line through the origin) and predict,
> before running: (a) whether the L1 solution still interpolates exactly one
> datum, (b) how many residuals become negative, and (c) whether the dual problem
> still attains the same optimum. Then run it. The number of interpolated points
> is the mechanism that makes an L1 fit what it is.

## 8. Exercises

Full set and worked solutions:
[`exercises/07-linear-programming-exercises.md`](./exercises/07-linear-programming-exercises.md)
and
[`exercises/07-linear-programming-solutions.md`](./exercises/07-linear-programming-solutions.md).
Four to start with:

**★1.** Convert $\max\ 3x_1 + 2x_2$ subject to $x_1 + x_2 \le 4$,
$x_1 + 3x_2 \le 6$, $x \ge 0$ into the form (2.1) and solve it by enumerating
vertices.

**★2.** Write down the LP for an L1 fit of three data by a constant (no slope),
and solve it by hand.

**★★3.** For ★1, write the dual, solve it, and verify strong duality. Interpret
both dual variables.

**★★4.** A gravity profile is fitted by a trend with a stated bound on the
gradient. Set up the LP, solve it, and report the shadow price of the bound in
units of $\sum|r|$ per unit of gradient.

## 9. Common mistakes

1. **Confusing the L1 and L2 objectives when comparing models.** Each method is
   worse than the other by the other's measure (Section 4.2); compare the
   *sensitivity to the blunder*, not the raw cost.
2. **Using a smooth solver on $\sum|r_i|$.** The objective is non-differentiable
   at the solution; use an LP (or a smooth approximation and accept the bias).
3. **Reading a shadow price without checking the sign convention.** See (2.5):
   the derivative is $-y$, and equality-as-two-inequalities splits the price
   between the two rows.
4. **Reporting a solution from an infeasible problem.** Distinguish the three
   outcomes (Section 2.1) or you will publish a mixture that does not exist.
5. **Ignoring degeneracy.** Ties make the multipliers non-unique, so a quoted
   price may be one of many. Section 4.1's zero-price upper rows are the
   symptom.
6. **Assuming L1 protects against all bad data.** It protects against large
   residuals; high-leverage points still control the fit (Section 6.7).
7. **Treating an LP as a general nonlinear solver.** A nonlinear specification
   has to be linearised, and sequential LP needs a trust region or it will
   oscillate.
8. **Believing that exact arithmetic is only for teaching.** Rational arithmetic
   is the right tool for verifying a formulation before trusting a
   floating-point implementation of it.

## 10. Real-world applications

- **Rock-physics blending and mixture design.** Meeting density, velocity and
  mineralogy specifications at least cost is an LP; the duals price each
  specification (Section 4.1).
- **Robust trend fitting.** Gravity, magnetic and geochemical profiles with
  suspect stations are fitted with L1 objectives, often as part of a larger
  processing chain where a Gaussian assumption would be untenable.
- **Extremal models in potential-field inversion.** Linear programming produces
  the model with the largest or smallest value of a linear functional among all
  models fitting the data within bounds — the classical way to bound an
  interpretation before committing to a regularised inversion.
- **Seismic statics and network adjustment.** Minimum L1-norm corrections on
  residual maps, cast as an LP or as a network flow.
- **Production and scheduling problems in energy geoscience.** Well placement,
  crew routing and survey scheduling are integer or linear programs, usually
  solved by dedicated solvers; the structure is the same simplex/dual structure.
- **Portfolio-style resource allocation in exploration.** Budget allocation
  across targets subject to constraints is an LP, and shadow prices tell you
  which constraint is actually binding.

## 11. Further reading

- **Dantzig, G. B. *Linear Programming and Extensions*. Princeton University
  Press.** Level: advanced. The original formulation, including the simplex
  method and its economics.
- **Luenberger, D. G., & Ye, Y. *Linear and Nonlinear Programming* (4th ed.).
  Springer.** Level: graduate. Simplex, duality and sensitivity analysis, with the
  proofs this lesson only sketches.
- **Boyd, S., & Vandenberghe, L. *Convex Optimization*. Cambridge University
  Press.** Chapters 4–5. Level: graduate. Duality done rigorously, and how LP
  sits inside convex optimisation.
- **Nocedal, J., & Wright, S. J. *Numerical Optimization* (2nd ed.). Springer.**
  Chapter 13. Level: graduate. Linear programming in the context of the
  constrained methods of [01-14-03](./03-constrained.md).
- **Claerbout, J. F., & Muir, F. (1973). Robust modeling with erratic data.
  *Geophysics*, 38(5), 826–844.** Level: intermediate. The classical geophysical
  argument for L1 and its relatives; confirm access through your library.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory* (4th ed.).
  Academic Press.** Level: intermediate. Includes LP formulations of extremal
  models, written for geophysicists.
- **Tarantola, A. *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: graduate. Why the choice of norm is a statement
  about the error distribution.

> Note on citations: bibliographic details above are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text, and you
> should confirm editions and current availability through your library before
> citing them yourself.

## 12. Self-assessment checklist

- [ ] I can state an LP in standard form and convert a given problem into it.
- [ ] I can implement a two-phase simplex with Bland's rule and explain what each
      phase proves.
- [ ] I can cast L1 and Chebyshev regression as LPs and explain the extra
      variables.
- [ ] I can compute a dual optimum and verify strong duality numerically.
- [ ] I can read a shadow price from a dual variable and check it by
      differentiation.
- [ ] I can explain why L1 is robust and L∞ is not, with measured numbers.
- [ ] I can decide whether an L1 formulation is warranted for a given dataset,
      and say what it costs.

## 13. Related lessons

- [01-14-03 Constrained Optimisation and Lagrange Multipliers](./03-constrained.md) —
  the same multipliers in the continuous setting.
- [01-14-04 Linear and Nonlinear Least Squares](./04-least-squares.md) — the L2
  benchmark and the machinery L1 replaces.
- [01-14-05 Global Optimisation](./05-global-optimization.md) — what to do when
  the feasible set is not convex and the LP guarantee is lost.
- [01-14-02 Unconstrained Minimisation](./02-unconstrained.md) — why a kinked
  objective needs different methods.
- [01-07-07 Orthogonality, Projections and Least Squares](../07-linear-algebra/07-orthogonality.md) —
  the geometry of the L2 fit that L1 abandons.
- [01-18 Inverse Problems](../../18-inverse-problems/README.md) — extremal models
  and bounded inversion in the wider inverse-theory context.
