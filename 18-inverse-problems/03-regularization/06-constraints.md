---
id: 18-03-06
title: "Physical Constraints, Bounds and Feasible Model Sets"
level: graduate
prereqs: ["18-03-02", "18-02-06"]
tags: [inverse-problems, regularization, constraints, convex-sets, isotonic-regression]
---

# Physical Constraints, Bounds and Feasible Model Sets

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** a constrained inverse problem as a convex program over a
   feasible set, and **derive** its Karush–Kuhn–Tucker conditions.
2. **Explain** why a constraint is a prior with infinite confidence, and why that
   makes it more dangerous than a soft penalty, not safer.
3. **Measure** what an inactive constraint does (nothing), what a false
   non-negativity constraint costs, and how a bound that excludes the truth
   reveals itself in the residual.
4. **Project** onto a box and onto the monotone cone, and **verify** a projection
   by idempotence and by the variational inequality.
5. **Apply** alternating projections to an intersection of two convex sets and
   **decide**, by an exact test, whether the intersection is non-empty.
6. **Report** a constrained inversion with the residual, the active set and the
   constraint that was imposed.

All models and data in this module are **SYNTHETIC**. The kernel is the exact
2-D line-mass gravity formula; the density distributions, station grid, depth and
noise are chosen teaching values. The only physical constant is
$G = 6.67430\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$.

## Prerequisites

- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](02-tikhonov.md) —
  the unconstrained reference problem every experiment here is compared against.
- [18-02-06 Data Weighting and Error Covariance Specification](../02-linear-inverse-problems/06-weighting-and-covariance.md) —
  what $\chi^2$ means and how the target level is obtained.
- [01-14-03 Constrained Optimisation and Lagrange Multipliers](../../01-mathematics/14-optimization/03-constrained.md) —
  the KKT conditions used below.

## 1. What a constraint is, in the language of the previous lessons

A physical constraint removes models from the feasible set:

$$\min_{m}\ \|Km-d\|_2^2 + \alpha\|Lm\|_2^2
\quad\text{subject to}\quad m \in \mathcal C,$$

with $\mathcal C$ a convex set: a box $[m_{\mathrm{lo}}, m_{\mathrm{hi}}]$, the
non-negative orthant, a monotone cone, a ball, or an intersection of these.

The Bayesian reading is the important one. A hard constraint is the limit of a
prior whose density is uniform inside $\mathcal C$ and **zero** outside. It
therefore expresses *infinite* confidence. A soft penalty, by contrast, is a
prior with finite variance that can be overruled by the data. Three consequences
follow, and all three are measured in this lesson:

1. **An inactive constraint changes nothing** — it is a prior that never
   contradicts the data.
2. **An active false constraint biases the answer and inflates the residual**,
   and if it is only mildly false the residual inflation can be small enough to
   overlook.
3. **Constraints couple the model.** Forcing one cell to a bound changes the
   optimal value of others, so "the constraint only affects the violating cells"
   is usually false.

## 2. Derivation: KKT, projections and alternating projections

### 2.1 Karush–Kuhn–Tucker conditions for a box

For the box-constrained regularised least-squares problem, the KKT conditions
are, for each component $i$,

$$\left(K^{\mathsf T}(Km-d) + \alpha L^{\mathsf T}Lm\right)_i
\begin{cases}
= 0, & m_{\mathrm{lo},i} < m_i < m_{\mathrm{hi},i}, \\[2pt]
\le 0, & m_i = m_{\mathrm{hi},i}, \\[2pt]
\ge 0, & m_i = m_{\mathrm{lo},i}.
\end{cases}$$

In words: either the gradient vanishes (an **inactive** component, treated
exactly as in the unconstrained problem), or it points out of the feasible set
and the component sits on a bound (an **active** component). The set of active
indices is called the active set, and it is the honest output of a constrained
inversion: it says *where the data were overruled*.

### 2.2 Projection onto a box and onto the monotone cone

Projection onto a box is componentwise clipping,
$P_{\mathcal C}(y)_i = \min(\max(y_i,m_{\mathrm{lo},i}),m_{\mathrm{hi},i})$.

Projection onto the non-increasing cone $\{m : m_1 \ge m_2 \ge \dots \ge m_n\}$
is isotonic regression, computed exactly by the pool-adjacent-violators algorithm
(PAVA): scan left to right, push each value as a block, and whenever the previous
block mean is smaller than the current one, merge them and replace both by their
weighted mean. The algorithm is $O(n)$ up to the merges, and it returns the
*exact* projection — not an approximation.

A projection can be verified without solving anything else, by two properties
the demonstration checks:

- **idempotence**: $P(P(y)) = P(y)$;
- **the variational inequality**: $\langle y - P(y),\, z - P(y)\rangle \le 0$ for
  every $z$ in the cone.

The second is the definition of a projection, and it is testable by sampling
feasible points.

### 2.3 Alternating projections (POCS)

For an intersection $\mathcal A \cap \mathcal B$ of two convex sets, the iteration

$$m^{k+1} = P_{\mathcal A}\!\left(P_{\mathcal B}(m^k)\right)$$

converges to a point of the intersection whenever the intersection is non-empty,
with a linear rate governed by the angle between the sets. When the intersection
is **empty** the iterates converge to a cycle in the gap between the sets and the
distance between consecutive iterates plateaus at a positive value. That plateau
is the honest signal that the problem has no solution — but it is slow to appear
and easily mistaken for slow convergence, which is why the demonstration tests
non-emptiness exactly instead:

$$\min_{m\in\mathcal B}\ \|K_jm-d_j\|_2$$

is a small quadratic program whose optimal value is zero exactly when the
hyperplane and the box intersect.

## 3. What is measured

### 3.1 The synthetic problem and the reference

48 cells over a $24\ \mathrm{km}$ profile ($510.6\ \mathrm{m}$ spacing), line-mass
sources at $800\ \mathrm{m}$ depth, 48 stations. The true model is $+3.00$ (units
of $10^{9}\ \mathrm{kg\,m^{-1}}$) at $x = +5\ \mathrm{km}$ and $-1.20$ at
$x = -4\ \mathrm{km}$: it has a **density deficit**, deliberately, because that is
what tests non-negativity. Anomaly peak $184.340\ \mathrm{mGal}$, noise
$\sigma = 0.9217\ \mathrm{mGal}$ ($0.50\%$ of the peak),
$n\sigma^2 = 6.9773\times10^{-3}$.

The unconstrained reference is Tikhonov with $L=I$ and $\alpha$ chosen by the
discrepancy principle, $\alpha = 6.3888\times10^{-3}$, giving
$\chi^2/(n\sigma^2) = 1.0000$ and RMS model error $0.0538$. **Every constrained
run below uses that same $\alpha$**, so the only change is the feasible set.

### 3.2 Inactive bounds change nothing

With bounds $\pm29.9$ (ten times the model range), no cell is near a bound:

| quantity | value |
|---|---|
| $\max_i |m_i - m_i^{\text{unconstrained}}|$ | $2.798\times10^{-14}$ |
| RMS model error, constrained | 0.053842 |
| RMS model error, unconstrained | 0.053842 |
| cells at a bound | 0 |

The two solutions agree to solver accuracy. A constraint that is not active
carries no information about the model; the corollary is that **adding a
constraint that the data already satisfy cannot improve the estimate**, only the
estimate's reputation.

### 3.3 Non-negativity against a model with a negative lobe

With bounds $[0, +\infty)$:

| quantity | measured |
|---|---|
| cells forced to the bound | 30 of 48 |
| bound active on the truly negative cells | 18 of 18 |
| RMS error over the negative lobe | 0.7591 (unconstrained 0.0543) |
| RMS error over the positive lobe | 0.1369 (unconstrained 0.0535) |
| RMS error, whole model | 0.4773 (unconstrained 0.0538) |
| $\chi^2/(n\sigma^2)$ | 1121.4 (unconstrained 1.000) |

Two of these rows repay attention.

- **The error is 14 times worse over the negative lobe and 2.6 times worse over
  the positive lobe.** The damage is *not* local to the violating cells: the
  bound changes the fit of the whole profile, so every cell's optimal value
  moves. A practitioner who checks only the constrained region will
  underestimate the harm.
- **The residual rises by three orders of magnitude.** This is the available
  warning. A physically imposed constraint that produces
  $\chi^2 = 1121\,n\sigma^2$ is positively rejected by the data — and yet the
  "non-negativity is always safe" habit persists because in many problems the
  constraint is only weakly active and the residual inflation is a factor of two
  or three, which nobody notices.

### 3.4 Bounds that exclude the truth

With bounds $[0, 2.0]$ while the truth peaks at $2.99$:

| quantity | measured |
|---|---|
| cells pinned to the upper bound | 12 of 48 |
| mean bias where the truth exceeds the bound | $-0.2153$ |
| distance from the truth peak to the bound | 0.9924 |
| RMS error, whole model | 0.5806 (unconstrained 0.0538) |
| $\chi^2/(n\sigma^2)$ | 1311.8 (unconstrained 1.000) |

The bias at the pinned cells is $-0.2153$ on average, i.e. the estimate sits on
the bound, not at the truth; the discrepancy between the truth and the bound is
$0.9924$ and it is **not recoverable from the data** because the feasible set
excludes it. Two signatures of a wrong bound appear together: an error that
saturates at the distance to the bound, and a residual that cannot reach the
noise level. The second is the one available without knowing the truth, and it is
the reason $\chi^2$ must always be quoted with a constrained inversion.

### 3.5 A monotonicity constraint with a *true* prior

The same machinery applied when the prior is right. Data are generated from a
monotone-decreasing depth-style model; the discrepancy $\alpha$ for that data set
is $1.3103\times10^{-3}$.

| quantity | unconstrained | constrained |
|---|---|---|
| monotonicity violations (of 47 intervals) | 21 | 0 |
| $\chi^2/(n\sigma^2)$ | 1.000 | 1.485 |
| RMS model error | 0.1675 | 0.0447 |

The constrained solution fits the data *worse* (1.485 versus 1.000) and is 3.7
times more accurate. That is the trade in its purest form: a slice of data
fidelity exchanged for a large gain in model accuracy, made knowingly, at a
measured price. The variational-inequality check on 2000 random feasible points
gives $\min_y\langle\nabla f(m), y-m\rangle = -5.7\times10^{-15}$, so the returned
point is optimal to machine precision and the comparison is between constraints,
not solvers.

### 3.6 Two sets at once: POCS, and a test for an empty intersection

Two constraints are imposed: one data hyperplane $K_jm = d_j$ (for the datum
with the smallest $|d_j|$, $d_j = 2.088\times10^{-2}$) and a box.

| box | exact $\min_{\mathcal B}\|K_jm-d_j\|$ | verdict | POCS agreement to $10^{-10}$ at iteration | contraction per iteration |
|---|---|---|---|---|
| $[-3, 3]$ | $6.9\times10^{-18}$ | intersection **non-empty** | 4 | — |
| $[-6, -1]$ | $1.051$ | intersection **empty** | not reached in 400 | $0.99187$ |

For the non-empty case the POCS limit satisfies both constraints (hyperplane
residual $3.5\times10^{-18}$, zero cells outside the box) and agrees with the
exact feasible point only to $12.25$ in model units — which measures the *size*
of the intersection, not an error. Two very different models satisfy the same
constraint exactly: **a constraint does not make the answer unique.**

For the empty case the iterate distance contracts by a factor of $0.99187$ per
iteration — so slow that 400 iterations leave it at $1.7\times10^{-2}$ — and the
exact test shows why: the nearest feasible point is $1.051$ from the hyperplane.
No amount of iteration fixes an over-constrained problem, and the exact test
costs one small quadratic program.

## 4. A fully worked numeric example

**Problem (a).** Minimise $f(m) = (m-5)^2$ subject to $0 \le m \le 3$, and
identify the active set.

**Solution.** The unconstrained minimiser is $m = 5$, outside the box. On the
upper bound the gradient is $2(3-5) = -4$, which points outward (the objective
would decrease by increasing $m$). The KKT condition for the upper bound is
"gradient $\le 0$", so it is satisfied with a multiplier $\lambda = 4 > 0$: the
solution is $m^\star = 3$, active at the upper bound. The estimate is biased by
$5-3 = 2$, and **no data can reduce that bias** once the bound is imposed.

**Problem (b).** Project $y = (3,1,2)$ onto the non-increasing cone, by hand.

**Solution (PAVA).** Push 3 as a block: $\{(3),1\}$. Push 1: the block means are
$3 \ge 1$, no violation. Push 2: now the last two means are $1$ and $2$, and
$1 < 2$ violates non-increase, so merge them:

$$\text{block mean} = \frac{1+2}{2} = 1.5, \qquad
P(y) = (3,\ 1.5,\ 1.5).$$

**Check by brute force.** Minimise $(3-a)^2+(1-b)^2+(2-c)^2$ over
$a \ge b \ge c$: a grid search over $a \in [0,4]$, $b \in [0,a]$,
$c \in [0,b]$ gives $(a,b,c) = (3.0, 1.5000, 1.5000)$ with objective $0.500$, and
the PAVA answer gives the same objective. The projection is exact, not
approximate — as it must be, because the algorithm *is* the solution of the
projection problem.

**Problem (c).** Compute the cost of a false constraint. The measured bias at
pinned cells is $-0.2153$ while the truth exceeds the bound by up to $0.9924$;
explain the difference.

**Solution.** The bias is the *mean* over the pinned cells, and only some of them
have truth far above the bound; the others are near it. The bound is the binding
quantity: no pinned cell can exceed $2.0$, so the error of the pinned set is at
least $0$ and at most $0.9924$, with mean $0.2153$. The maximum error is set by
the distance from the truth to the bound, which is a *model* quantity known only
because the model is synthetic.

## 5. Assumptions and regime of validity

1. **The feasible set is convex.** Projections and KKT arguments need convexity.
   Constraints such as "exactly three layers" or "the interface is a single
   polygon" are non-convex and require combinatorial search, not projection.
2. **The constraint is true, or nearly so.** A false constraint produces a bias
   that saturates at the boundary of the feasible set and cannot be detected from
   the data if the misfit inflation is small. Section 3.3 shows both the bias and
   the $\chi^2$ signal when the constraint is badly wrong.
3. **The noise level is known**, because the only general-purpose detection test
   is $\chi^2/(n\sigma^2) \approx 1$. Without $\sigma$, a constrained inversion
   has no available quality check beyond the residual's absolute size.
4. **The constraint does not already follow from the data.** If it does, it is
   inactive and changes nothing (measured: $2.8\times10^{-14}$).
5. **The intersection of several constraints is non-empty.** With more than two
   constraints this must be tested, not assumed; Section 3.6 gives the test.
6. **The active set is reported.** It is the part of the answer that came from
   the prior rather than from the measurement, and a reader cannot reconstruct it
   from the model plot.

## 6. The honest summary

- Constraints are priors with infinite confidence; the choice to impose one is a
  model choice of the strongest kind.
- An inactive constraint is free and useless. An active true constraint buys
  accuracy at a measurable cost in misfit (here $\chi^2$ from 1.00 to 1.49 for a
  3.7-fold error reduction). An active false constraint costs accuracy and
  inflates the residual, sometimes by orders of magnitude.
- The residual ratio $\chi^2/(n\sigma^2)$ is the only general audit available
  without the truth, and it is weak when the constraint is only mildly false.
- Constraints couple the model: the measured damage of a false non-negativity
  constraint was 2.6 times worse over the region where it was *not* active.
- A constraint shrinks the feasible set but does not make the answer unique: two
  models satisfying the same hyperplane and box were $12.25$ apart.
- Report the active set, the constraint, the residual and the parameter. A
  constrained inversion without those four numbers is not reproducible.

## 7. Python demonstration

`code/constraints_demo.py` prints: the synthetic problem and the
discrepancy-chosen reference; the inactive-bound comparison; the non-negativity
experiment with per-region errors; the tight-bound experiment with the bias and
the residual; the PAVA projection with its idempotence check and the
monotonicity experiment with the variational-inequality verification; and the
POCS experiment with the exact non-emptiness test in both the feasible and the
infeasible case.

```bash
cd 18-inverse-problems/03-regularization/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python constraints_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, under a second.

## 8. Exercises

Full sets with worked solutions are in
[`exercises/06-constraints-exercises.md`](exercises/06-constraints-exercises.md)
and [`exercises/06-constraints-solutions.md`](exercises/06-constraints-solutions.md).

- **★** Project $y = (2, 0.5, 1.5)$ onto the non-increasing cone by PAVA, and
  check the result by evaluating the objective at one feasible alternative.
- **★★** Write the KKT conditions for the box-constrained problem and determine
  the active set for the one-dimensional problem $\min (m-4)^2$ subject to
  $m \ge 1$; state the multiplier.
- **★★★** Design an experiment that measures how large a false non-negativity
  constraint can be before $\chi^2/(n\sigma^2)$ detects it, and predict the
  detection threshold as a function of the noise level.

## 9. Mastery checkpoint

Complete this without notes:

> An inversion with bounds $[0, 5]$ reports 14 cells pinned at $0$, and
> $\chi^2/(n\sigma^2) = 950$. **(a)** Is the constraint active, and how can you
> tell from the reported numbers alone? **(b)** State two consequences for the
> rest of the model. **(c)** A colleague removes the bound and obtains
> $\chi^2/(n\sigma^2) = 1.02$ with a model whose minimum is $-0.4$. Which model
> should be reported, and what does the answer depend on? **(d)** For the
> two-sample step of Section 4(b), compute $P(y)$ for $y = (3,1,2)$ and state
> which of the two properties (idempotence or the variational inequality) you
> would use to prove optimality to a referee.

A worked version of (a)–(c) appears in
[`exercises/06-constraints-solutions.md`](exercises/06-constraints-solutions.md).

## 10. Common pitfalls

1. **"Non-negativity is harmless."** Measured: 0.4773 against 0.0538 RMS, with
   the damage extending to the unconstrained region.
2. **Judging the damage by the violating cells.** The positive lobe's error rose
   by a factor of 2.6.
3. **Not reporting the active set.** The reader cannot tell which values are
   measurements and which are the prior speaking.
4. **Omitting $\chi^2$.** With a constraint, the residual is the only available
   test of the constraint.
5. **Assuming an intersection is non-empty because the iteration "converges
   slowly".** The exact test costs one quadratic program; the contraction factor
   was $0.992$ per iteration, indistinguishable from slow convergence by eye.
6. **Treating a constraint as a substitute for a penalty.** Hard constraints
   cannot be traded against the data; a slightly false constraint biases the
   answer with no way to soften it.

## 11. Where this is used

- **Density and susceptibility bounds** in potential-field inversion: strictly
  positive or bounded contrasts, often derived from rock physics.
- **Velocity and slowness positivity, monotone compaction trends.** Monotone
  velocity-depth profiles are the standard example of isotonic regression in
  geophysics.
- **Feasibility in petrophysics.** Porosity, saturation and mineral fractions
  satisfy sum-to-one and bound constraints, and joint inversion often solves a
  projection problem at each iteration.
- **Seismic and EM inversion with total-variation or box constraints**; the
  projection tools of Section 2 are the inner loop of those solvers; see
  [18-03-05 Total Variation and Edge-Preserving Inversion](05-total-variation.md).

## 12. Related modules

- [18-03-07 Regularisation of Nonlinear Problems](07-nonlinear-regularization.md) —
  constraints inside a linearisation loop, where the feasible set is linearised
  along with the data.
- [18-05-03 Priors: Informative, Reference and Their Influence](../05-bayesian-inversion/03-priors.md) —
  the same choice made probabilistically rather than geometrically.
- [18-08-03 Assessing a Model: Resolution, Artifacts, Alternatives](../08-practical-inversion-workflow/03-model-assessment.md) —
  reporting the active set as part of the answer.
- [01-14-03 Constrained Optimisation and Lagrange Multipliers](../../01-mathematics/14-optimization/03-constrained.md) —
  the multipliers behind the KKT conditions.
- [21-03-01 The Bayesian Paradigm and Subjective Probability](../../21-statistics-bayesian-ml/03-bayesian-inference/01-bayesian-paradigm.md) —
  why "infinite confidence" is a statement about the analyst, not the Earth.

## 13. Self-assessment checklist

- [ ] I can write the KKT conditions for a box-constrained problem.
- [ ] I can project onto a box and onto the monotone cone.
- [ ] I can verify a projection by idempotence and by the variational inequality.
- [ ] I can state the two signatures of a wrong bound.
- [ ] I can test whether an intersection of convex sets is non-empty.
- [ ] I can name the four numbers a constrained inversion must report.
