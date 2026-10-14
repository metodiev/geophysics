---
id: 01-14-03
title: "Constrained Optimisation and Lagrange Multipliers"
level: advanced
prereqs: ["01-14-01", "01-07-07"]
estimated_minutes: 90
tags: [optimization, lagrange-multipliers, kkt, constraints]
---

# Constrained Optimisation and Lagrange Multipliers

## Learning objectives

By the end of this lesson you will be able to:

1. **Form** the Lagrangian for an equality-constrained problem, derive the KKT
   system, and solve it for a small geophysical example.
2. **Interpret** a Lagrange multiplier as the derivative of the optimal value
   with respect to the constraint, and verify that interpretation numerically.
3. **State** the full KKT conditions for inequality constraints, and use
   complementarity to decide which constraints are active.
4. **Solve** a box-constrained problem two ways — projected gradient descent and
   exhaustive active-set enumeration — and reconcile the answers.
5. **Explain** what a bound buys and what it costs: the model becomes physically
   admissible at the price of misfit, priced by the multiplier.
6. **Diagnose** the penalty method's $1/\mu$ convergence of constraint violation
   and say when to use an exact constraint instead.

## Prerequisites

[01-14-01 Convexity, Stationarity and Optimality Conditions](./01-convexity.md)
for the unconstrained conditions that the KKT conditions generalise, and
[01-07-07 Orthogonality, Projections and Least Squares](../07-linear-algebra/07-orthogonality.md)
for the projection geometry behind feasibility.

## 1. Intuition: constraints are how physics enters an inversion

An unconstrained inversion will happily return a negative density, a negative
layer thickness, or a velocity of $12$ km/s in the mantle. Nothing in the
least-squares misfit knows any physics: the data only test combinations of
parameters, and a model that is physically absurd can fit the data perfectly.
Constraints are how the physics gets in — and the reason this lesson belongs in
the same module as least squares is that *every* practical inversion has them.

Three kinds of constraint appear constantly:

| Type | Example | Mathematical form |
|---|---|---|
| Bounds | density between 2.0 and 3.2 g cm⁻³ | $\ell \le m \le u$ |
| Equality | total mass fixed, or a tie to a well log | $Cm = d$ |
| Inequality | no negative slowness perturbation | $g(m) \le 0$ |

The single most useful fact about a constrained optimum is that the constraint
has a *price*. The Lagrange multiplier $\lambda$ answers the question "if I relax
this constraint by one unit, how much does the misfit improve?" That is not a
mathematical curiosity: it is the sentence you write in an interpretation report
when you say "the well tie costs us 5 per cent in data fit".

A second fact, less intuitive but just as useful: **the solution of a constrained
problem can be read as a modified unconstrained problem.** Adding $\lambda C^{\mathsf{T}}$
to the gradient is the same as changing the misfit's slope in the constrained
direction, so constraints act like an added data set of infinite weight. The
penalty method of Section 4.5 makes that interpretation literal.

## 2. Precise definitions

### 2.1 The general problem

Minimise $f(m)$ subject to

$$h_i(m) = 0,\quad i = 1,\dots,p, \qquad g_j(m) \le 0,\quad j = 1,\dots,q. \tag{2.1}$$

The **Lagrangian** is

$$L(m, \lambda, \mu) = f(m) + \sum_{i=1}^{p}\lambda_i h_i(m)
+ \sum_{j=1}^{q}\mu_j g_j(m). \tag{2.2}$$

The **feasible set** $\mathcal{F} = \{m : h_i(m) = 0,\ g_j(m) \le 0\}$ must be
convex for the strong statements below; the local statements hold regardless.

### 2.2 The KKT conditions

If a constraint qualification holds at a local minimiser $m^{*}$ (linear
independence of the active constraint gradients suffices, and is generically
true in geophysics), then there exist multipliers $\lambda \in \mathbb{R}^{p}$,
$\mu \in \mathbb{R}^{q}$ with

$$\nabla f(m^{*}) + \sum_i \lambda_i \nabla h_i(m^{*})
+ \sum_j \mu_j \nabla g_j(m^{*}) = 0
\qquad\text{(stationarity)}, \tag{2.3}$$

$$h_i(m^{*}) = 0, \qquad g_j(m^{*}) \le 0
\qquad\text{(primal feasibility)}, \tag{2.4}$$

$$\mu_j \ge 0 \qquad\text{(dual feasibility)}, \tag{2.5}$$

$$\mu_j\, g_j(m^{*}) = 0 \qquad\text{(complementary slackness)}. \tag{2.6}$$

Complementary slackness (2.6) is the operational one: a constraint is either
active ($g_j = 0$, price possibly positive) or free ($g_j < 0$, price exactly
zero). There is no third case, and the "exactly zero" is what lets you drop
inactive constraints and solve a smaller problem.

### 2.3 Why the multipliers are derivatives

Consider the perturbed problem
$f^{*}(c) = \min\{f(m) : h(m) = c\}$. Differentiating along the optimal path,
with (2.3) holding, gives

$$\frac{d f^{*}}{d c} = -\lambda. \tag{2.7}$$

So $\lambda$ measures the misfit cost per unit of constraint. Section 4.2 verifies
(2.7) numerically to ten decimal places. The sign convention is the one that
matters: with the Lagrangian written as in (2.2), a positive $\lambda$ means the
constraint is pushing the model *against* the objective's preference.

### 2.4 Two ways to enforce a constraint

**Exact (KKT or active-set).** Solve the KKT system directly. The constraint is
satisfied to round-off, and the multiplier comes out as a by-product.

**Penalty.** Replace the constraint by a weight:

$$\min_m f(m) + \frac{\mu}{2}\|h(m)\|^{2}. \tag{2.8}$$

This is differentiable, easy to implement and always feasible to evaluate, but
the constraint is satisfied only in the limit $\mu \to \infty$, and Section 4.5
measures the approach: violation $\propto 1/\mu$. In exact arithmetic the
sequence of penalty solutions converges to the constrained solution; in floating
point large $\mu$ destroys the conditioning of the system, so the method has a
practical ceiling.

### 2.5 Projected gradient for box constraints

For bounds only, the projected gradient iteration

$$m_{k+1} = \mathcal{P}_{[\ell,u]}\bigl(m_k - \alpha \nabla f(m_k)\bigr),
\qquad \mathcal{P}\ \text{componentwise clamp} \tag{2.9}$$

converges to a KKT point for any $\alpha < 2/L$, where $L$ is the largest
eigenvalue of $\nabla^{2}f$ (assuming that bound). Its KKT verification is
local: at a clamped component the *sign* of the gradient must point outward,
which is the discrete version of (2.5)–(2.6).

**Box constraints and `01-14-02`'s scaling.** Because clamping is applied
componentwise, the effective curvature of the free components is what sets the
step size, and the problem is well conditioned exactly when the free components
have comparable sensitivity.

## 3. Derivations

### 3.1 The KKT system for a quadratic with an equality constraint

Minimise $f(m) = \tfrac12 m^{\mathsf{T}} A m - b^{\mathsf{T}}m$ subject to
$Cm = d$, with $A \succ 0$ and $C$ of full row rank. Then (2.3) reads

$$A m + C^{\mathsf{T}}\lambda = b, \qquad C m = d,$$

which assembles into the symmetric indefinite system

$$\begin{bmatrix} A & C^{\mathsf{T}} \\ C & 0 \end{bmatrix}
\begin{bmatrix} m \\ \lambda \end{bmatrix}
= \begin{bmatrix} b \\ d \end{bmatrix}. \tag{3.1}$$

The system is indefinite but nonsingular when $C$ has full row rank and $A \succ
0$; it is the standard workhorse of constrained inversion. Two properties are
worth memorising:

- **The constrained optimum is never better than the unconstrained one**:
  $f(m_{\text{con}}) \ge f(m_{\text{unc}})$, with equality only if the
  unconstrained minimiser is already feasible.
- **The gap is second order in the violation.** Resolving the unconstrained
  model by projecting it onto the constraint gives a first-order change in $m$
  but only a second-order change in $f$, because the gradient vanishes at the
  unconstrained minimiser. This is why mildly violated constraints are often
  cheap: the misfit they cost grows quadratically.

### 3.2 From the Lagrangian to the price of a constraint

Let $m^{*}$ solve the constrained problem and define the perturbed optimum
$f^{*}(c)$ as in (2.7). Along the optimal path $m(c)$,

$$\frac{d}{dc} f(m(c)) = \nabla f^{\mathsf{T}} m'(c)
= -\bigl(\lambda^{\mathsf{T}} \nabla h\bigr)^{\mathsf{T}} m'(c)
= -\lambda^{\mathsf{T}} h'(m) m'(c) = -\lambda .$$

The third equality uses stationarity (2.3); the last uses $h(m(c)) = c$. The
derivation is three lines, and it is the entire justification for calling
$\lambda$ a price.

### 3.3 Complementarity, by case analysis

For a single constraint $g(m) = -m_1 \le 0$ (i.e. $m_1 \ge 0$) with unconstrained
minimiser $t$:

- If $t > 0$ the constraint is inactive, so $\mu = 0$ and $m_1 = t$.
- If $t < 0$ the constraint must be active, $\mu = -t > 0$ and $m_1 = 0$.

In both cases $\mu\, g(m) = 0$. That is complementarity in its simplest form, and
the demonstration's Section 3 reproduces it with $t = +2$ and $t = -3$, giving
$\mu = 0$ and $\mu = 3$ respectively.

### 3.4 The active-set method

For a box-constrained quadratic with $n$ parameters, enumerate the $3^{n}$ bound
patterns (at a lower bound, free, at an upper bound). For each pattern, solve the
equality-constrained sub-problem on the free coordinates, then test the KKT sign
conditions:

- free coordinate: gradient component zero;
- at a lower bound: gradient component $\ge 0$;
- at an upper bound: gradient component $\le 0$.

Every pattern that passes is a KKT point; the best of them is the global
solution, because the problem is convex. For $n = 3$ that is $27$ patterns — the
demonstration scans all of them and finds exactly one KKT point, so uniqueness is
*reported* rather than assumed. Enumeration is exponential and is used only as a
reference; production codes use the combinatorial structure of the box.

## 4. Numerical results

All numbers come from
[`code/constrained_demo.py`](./code/constrained_demo.py).

### 4.1 An equality-constrained travel-time problem

A two-cell problem with SYNTHETIC path lengths $G = [[1, 0.4], [0.6, 1]]$ km and
residuals $(0.052, 0.061)$ s has unconstrained minimiser
$m = (0.03631579, 0.03921053)$ s/km, misfit $0.0000000000$ (the data were
generated from a model in the kernel's range, so the fit is exact).

Impose the well-log tie $m_1 = m_2$, i.e. $h(m) = m_1 - m_2 = 0$:

| quantity | value |
|---|---|
| constrained minimiser | $(0.03769912,\ 0.03769912)$ s/km |
| $Cm - d$ | $-6.939\times10^{-18}$ |
| stationarity residual $\nabla f + C^{\mathsf{T}}\lambda$ | $(-3.903\times10^{-18}, +3.903\times10^{-18})$ |
| multiplier $\lambda$ | $-0.00036991$ |
| misfit | $0.0000005354$ |
| misfit increase over unconstrained | $0.0000005354$ |

Three things are worth noting. The constraint is satisfied to $7\times10^{-18}$ —
exact arithmetic in practice. Stationarity holds to the same order, which is what
certifies the KKT system rather than a projection was solved. And the misfit went
*up* by $5.4\times10^{-7}$, as it must: a constraint can only remove models from
the feasible set.

### 4.2 The multiplier is a derivative

Perturbing the constraint right-hand side to $d \pm \varepsilon$ and
differencing the optimal values:

| $\varepsilon$ | central difference of $f^{*}$ | $-\lambda$ |
|---|---|---|
| $10^{-2}$ | $0.0003699115$ | $0.0003699115$ |
| $10^{-3}$ | $0.0003699115$ | $0.0003699115$ |
| $10^{-4}$ | $0.0003699115$ | $0.0003699115$ |

The agreement to ten decimal places at three step sizes is as strong a
verification of (2.7) as a numerical experiment can give. The multiplier is
therefore not a bookkeeping device: it is the exchange rate between the
constraint and the misfit, and it has units of misfit per unit of constraint.

### 4.3 Complementarity

For $\min \tfrac12(m_1 - t_1)^{2} + \tfrac12(m_2 + 1)^{2}$ subject to
$m_1 \ge 0$:

| case | $m_1$ | $m_2$ | $\mu$ | $\mu\, g(m^{*})$ |
|---|---|---|---|---|
| $t_1 = +2$ (inactive) | $2.000000$ | $-1.000000$ | $0.000000$ | $0$ |
| $t_1 = -3$ (active) | $0.000000$ | $-1.000000$ | $3.000000$ | $0$ |

The inactive case has $\mu = 0$; the active case has $\mu = 3$ and the
complementarity product is zero in both. Note the sign: $\mu = -t_1 = 3 > 0$,
which is dual feasibility (2.5). A negative multiplier would mean the constraint
was pushing the objective *downhill*, which cannot happen at an optimum.

### 4.4 Box constraints, two ways

A three-cell cross-hole kernel with SYNTHETIC data generated from
$m_{\text{true}} = (0.050, 0.005, 0.022)$ s/km, with bounds
$0 \le m_i \le 0.03$ s/km:

| method | model (s/km) | misfit | iterations/cost |
|---|---|---|---|
| unconstrained | $(0.050000, 0.005000, 0.022000)$ | $4.815\times10^{-35}$ | — (infeasible: cell 1 exceeds $0.03$) |
| projected gradient | $(0.03000000, 0.02218876, 0.02398394)$ | $2.0080321285\times10^{-5}$ | $20\,000$ iterations, last step norm $3.469\times10^{-18}$ |
| active-set scan (27 patterns) | $(0.03000000, 0.02218876, 0.02398394)$ | $2.0080321285\times10^{-5}$ | $1$ KKT pattern found |

The two methods agree to $3.5\times10^{-18}$ — they are the same point. The
active-set scan reports that exactly **one** of the 27 bound patterns satisfies
feasibility and the KKT sign conditions, so the answer is unique, and the scan
says so explicitly rather than assuming it. The cost of the bound is
$2.0\times10^{-5}$ in misfit, up from $4.8\times10^{-35}$.

### 4.5 A physically inadmissible model, and what the bound buys

Data generated from $m_{\text{phys}} = (0.040, -0.010, 0.020)$ s/km:
$d = (0.0300, 0.0330, 0.0320)$ s. The unconstrained solution reproduces
$m_{\text{phys}}$ exactly, including the negative slowness perturbation in cell
2 — a model that is arithmetically perfect and physically meaningless.

Imposing $m_i \ge 0$ gives

$$m_{\text{bounded}} = (0.029510,\ 0.000000,\ 0.020696)\ \text{s/km},$$

with misfit rising from $2.167\times10^{-34}$ to $6.127\times10^{-6}$. The bound
is not free; it is a decision, and the number $6.1\times10^{-6}$ is what the
decision costs in data fit. Reporting the bounded model *with* that number is the
honest form of the result.

### 4.6 The penalty method: measured $1/\mu$ convergence

Minimising $\tfrac12\|Gm - d\|^{2} + \tfrac{\mu}{2}(m_1 + m_2 - 0.02)^{2}$:

| $\mu$ | $m_1$ | $m_2$ | violation | misfit | ratio when $\mu$ grows tenfold |
|---|---|---|---|---|---|
| $1$ | $0.025500$ | $0.012000$ | $1.750\times10^{-2}$ | $1.531\times10^{-4}$ | — |
| $10$ | $0.005455$ | $0.017727$ | $3.182\times10^{-3}$ | $5.062\times10^{-4}$ | $5.500$ |
| $100$ | $0.001485$ | $0.018861$ | $3.465\times10^{-4}$ | $6.004\times10^{-4}$ | $9.182$ |
| $1000$ | $0.001049$ | $0.018986$ | $3.497\times10^{-5}$ | $6.113\times10^{-4}$ | $9.911$ |
| $10\,000$ | $0.001005$ | $0.018999$ | $3.500\times10^{-6}$ | $6.124\times10^{-4}$ | $9.991$ |
| $100\,000$ | $0.001000$ | $0.019000$ | $3.500\times10^{-7}$ | $6.125\times10^{-4}$ | $9.999$ |

The violation ratio tends to exactly $10$, i.e. violation $\propto 1/\mu$, as
theory predicts; the first ratio of $5.5$ is the pre-asymptotic regime, and it is
reported rather than hidden. Note also that increasing $\mu$ by five orders of
magnitude changed the misfit by $0.4$ per cent: the penalty solution is already
close to the constrained one in the objective, even while the constraint
violation is still visible.

### 4.7 Duality: the multiplier is the argmax of a dual problem

The Lagrange dual of the equality-constrained quadratic is

$$q(\lambda) = \min_m \left[ f(m) + \lambda^{\mathsf{T}}(Cm - d) \right],$$

which is concave (a minimum of affine functions), and strong duality holds for
this problem class. A golden-section maximisation of $q$ over
$[-0.005, 0.005]$ finds

| quantity | value |
|---|---|
| $\arg\max q$ | $-0.0003699115$ |
| $q(\lambda^{*})$ | $0.0000005354$ |
| KKT multiplier $\lambda$ | $-0.0003699115$ |
| constrained optimum $f^{*}$ | $0.0000005354$ |
| agreement in $\lambda$ | $2.4\times10^{-11}$ |

Both the multiplier and the optimal value agree, so the KKT solve and the dual
maximisation are two routes to the same answer. The practical value of the dual
view is that *any* admissible $\lambda$ gives a lower bound, which is how one
certifies that a solution cannot be improved much — the same logic that makes
duality useful in [01-14-07](./07-linear-programming.md).

## 5. Physical interpretation

**A bound is a physical statement; a multiplier is its price.** "Density must be
positive" is knowledge; "$0.00036991$ of misfit per unit of well-log tie" is what
that knowledge costs in this dataset. Both belong in a report, and the second is
usually the more informative.

**Constraints redistribute resolution.** Forcing $m_1 = m_2$ made the two cells
identical and moved the misfit up slightly; what it really did was remove one
degree of freedom from a problem whose kernel was nearly degenerate. In the
$G^{\mathsf{T}}G$ language the constraint removes a direction from the model
space, and the remaining directions become better determined — the conditioning
improves even as the misfit worsens.

**Exact versus penalty is a conditioning decision.** The $1/\mu$ rate means that
getting a violation of $10^{-6}$ needs $\mu \sim 10^{6}$, which multiplies the
Hessian by $10^{6}$ and destroys its conditioning. That is why production codes
prefer an exact (KKT or active-set) treatment or an augmented Lagrangian, where
the multiplier is updated instead of the weight being increased indefinitely.

**Bound constraints are how positivity, monotonicity and known lithology enter.**
Velocity increasing with depth, density above the matrix density, conductivity
above the pore-fluid value: all bounds. Every one of them is a KKT point with a
price.

**Projected gradient is the naive method, and it works on boxes.** Clamping is
optimal for separable bounds, which is why the method is so common in
geophysical codes that use bound constraints and so useless as soon as an
equality ties two parameters together.

## 6. Assumptions and regime of validity

1. **Constraint qualification.** The KKT conditions require the active constraint
   gradients to be linearly independent. Duplicated constraints (a tie imposed
   twice, or an equality written as two opposing inequalities) violate this
   strictly but are handled by the solver; the multipliers then are not unique
   even though the model is.
2. **Convexity for global statements.** Everything here is local unless $f$ is
   convex and the feasible set convex, in which case KKT is sufficient as well as
   necessary.
3. **Smooth constraints.** Inequality constraints are handled by their gradients;
   a constraint that is not differentiable where it is active needs a different
   theory.
4. **The price is local.** $d f^{*}/dc = -\lambda$ holds at the current active
   set. Change $c$ enough to activate a new constraint and the derivative
   changes discontinuously.
5. **Penalty weights do not converge in floating point.** The $1/\mu$ rate is a
   mathematical statement about exact arithmetic; at some $\mu$ the round-off in
   the augmented system dominates, and the violation stops decreasing. The
   demonstration's table stops at $\mu = 10^{5}$ for that reason.
6. **Box enumeration does not scale.** The $3^{n}$ scan is a reference method for
   $n = 3$; for realistic $n$ the active set is found by a combinatorial
   algorithm or by an interior-point method.

## 7. Python demonstration

The companion script is
[`code/constrained_demo.py`](./code/constrained_demo.py), with seven sections:
the KKT system, the multiplier as a derivative, complementarity, box constraints
two ways, inadmissible models, the penalty sweep, and duality. All linear algebra
is written out with the standard library.

| Section | Measured | Interpretation |
|---|---|---|
| 1, KKT | $Cm - d = -6.9\times10^{-18}$, stationarity residual $3.9\times10^{-18}$ | the constrained solve satisfies both KKT equalities |
| 2, price | central difference $0.0003699115 = -\lambda$ at three step sizes | the multiplier is a derivative, verified |
| 3, complementarity | inactive $\mu = 0$; active $\mu = 3$; $\mu g = 0$ both times | KKT in its simplest form |
| 4, box | projected gradient and the 27-pattern scan agree to $3.5\times10^{-18}$ | one KKT point, found two ways |
| 5, inadmissible | bounded model $(0.029510, 0, 0.020696)$, misfit rises to $6.127\times10^{-6}$ | the bound is a decision with a price |
| 6, penalty | violation ratio $\to 9.999$ | measured $1/\mu$ convergence |
| 7, duality | $\arg\max q = -0.0003699115$, agreement $2.4\times10^{-11}$ | the multiplier solves a dual problem |

> **Breaking exercise.** In Section 4, tighten the upper bound from $0.03$ to
> $0.025$ s/km and predict, before running: (a) which cells become active, (b)
> whether the active-set scan still finds exactly one KKT point, and (c) whether
> the misfit increase is larger or smaller than the quadratic estimate
> $(\Delta m)^{2}\lambda_{\min}/2$. Then run it and reconcile.

## 8. Exercises

Full set and worked solutions:
[`exercises/03-constrained-exercises.md`](./exercises/03-constrained-exercises.md)
and [`exercises/03-constrained-solutions.md`](./exercises/03-constrained-solutions.md).
Four to start with:

**★1.** Write the KKT system (3.1) for $A = \operatorname{diag}(2, 8)$, $b = (2,
8)^{\mathsf{T}}$ and the single constraint $m_1 + m_2 = 1$, and solve it by hand.

**★2.** State the KKT conditions for $\min m^{2}$ subject to $m \ge 1$ and verify
them at the solution.

**★★3.** For the problem of ★1, compute $d f^{*}/dc$ two ways: from the
multiplier and by re-solving with $c = 1 \pm 0.01$.

**★★4.** A two-cell model has $G = [[1,1],[1,1.02]]$ and $d =
(0.04, 0.0408)$ s. Solve the box-constrained problem with $0 \le m_i \le 0.05$
s/km and report which bounds are active and the misfit cost of each.

## 9. Common mistakes

1. **Projecting onto constraints and calling it a solve.** Clamping is optimal
   for boxes and wrong for equalities; a projected-gradient iterate for a tie
   constraint is not a KKT point.
2. **Reporting a constrained model without its misfit cost.** The bound is a
   decision; the cost is the evidence for the decision.
3. **Using a huge penalty weight.** The violation falls as $1/\mu$ while the
   conditioning degrades as $\mu$; there is an optimum, and beyond it the
   answers get worse.
4. **Assuming the multiplier is positive for an equality constraint.** Equality
   multipliers are unrestricted in sign — Section 4.1's is $-0.00036991$ — only
   inequality multipliers must be non-negative.
5. **Forgetting that a constraint can only increase the objective.** A reported
   constrained misfit below the unconstrained one means a bug.
6. **Ignoring degeneracy.** Constraints that are redundant at the solution make
   the multipliers non-unique, so a "multiplier" quoted from such a problem has no
   price interpretation.
7. **Treating a bound as free information.** A prior that is wrong is worse than
   no prior: it removes the right answer from the feasible set.

## 10. Real-world applications

- **Density and velocity bounds in potential-field and seismic inversion.**
  Positivity, ordering (velocity increasing with depth) and lithological ranges
  are box constraints; their multipliers measure how hard the data are pushing
  against the geology.
- **Well ties and cross-well constraints.** Equal-time or equal-depth ties are
  equality constraints, exactly the KKT form solved in Section 4.1.
- **Minimum-structure inversions with a fixed total mass.** A single equality on
  $\sum_i m_i$ removes the null-space direction that a bounded survey cannot
  resolve.
- **Seismic tomography with ray-path constraints.** The requirement that a ray
  travel time be consistent with the model is itself a constraint on some
  formulations, and the multiplier measures the inconsistency.
- **Geodetic network adjustment with fixed stations.** Fixed coordinates are
  equality constraints; the multipliers are the forces needed to hold those
  stations in place.
- **Machine-learning regularisation.** A soft constraint (a penalty) or a hard
  one (a projection layer) — the same two options as Sections 2.4 and 2.5, with
  the same conditioning trade-off.

## 11. Further reading

- **Nocedal, J., & Wright, S. J. *Numerical Optimization* (2nd ed.). Springer.**
  Chapter 12 (equality and inequality constraints) and Chapter 16 (quadratic
  programming). Level: graduate. The standard reference for the KKT system,
  active sets and penalty methods.
- **Boyd, S., & Vandenberghe, L. *Convex Optimization*. Cambridge University
  Press.** Chapters 4–5. Level: graduate. Duality, the price interpretation and
  the sensitivity theorem (2.7) done rigorously.
- **Nocedal & Wright, Chapter 17**, for the augmented Lagrangian method that
  replaces the penalty sweep of Section 4.6.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory* (4th ed.).
  Academic Press.** Level: intermediate. Constrained inversion written directly
  for geophysicists, including the equality-constrained least-squares system
  (3.1).
- **Tarantola, A. *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: graduate. Priors as constraints, and the
  probabilistic reading of the multiplier.

> Note on citations: bibliographic details above are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text, and you
> should confirm editions and current availability through your library before
> citing them yourself.

## 12. Self-assessment checklist

- [ ] I can write the KKT system for an equality-constrained quadratic and solve
      it.
- [ ] I can state all four KKT conditions and explain what each one excludes.
- [ ] I can compute a multiplier from a KKT solve and verify it by perturbing the
      constraint.
- [ ] I can decide which inequality constraints are active using
      complementarity.
- [ ] I can implement projected gradient for a box problem and check the KKT sign
      conditions at the result.
- [ ] I can explain the $1/\mu$ convergence of a penalty method and its
      conditioning consequence.
- [ ] I can say what a bound costs in misfit and quote that number in a report.

## 13. Related lessons

- [01-14-01 Convexity, Stationarity and Optimality Conditions](./01-convexity.md) —
  the unconstrained conditions that the KKT conditions generalise.
- [01-14-02 Unconstrained Minimisation](./02-unconstrained.md) — the iteration that
  a projected or damped method modifies.
- [01-14-04 Linear and Nonlinear Least Squares](./04-least-squares.md) — the
  misfit used in every constrained example here.
- [01-14-05 Global Optimisation](./05-global-optimization.md) — what bounds do to
  a multi-modal search: they remove basins.
- [01-14-07 Linear Programming](./07-linear-programming.md) — duality and shadow
  prices in the case where the constraints *are* the problem.
- [01-07-07 Orthogonality, Projections and Least Squares](../07-linear-algebra/07-orthogonality.md) —
  projection geometry, of which clamping is the box special case.
- [01-18 Inverse Problems](../../18-inverse-problems/README.md) — priors and
  constraints as extra information.
