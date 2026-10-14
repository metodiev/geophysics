---
id: 18-03-07
title: "Regularisation of Nonlinear Problems"
level: research
prereqs: ["18-03-02", "18-03-03", "18-04-01"]
tags: [inverse-problems, regularization, nonlinear-inversion, gauss-newton, irls]
---

# Regularisation of Nonlinear Problems

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the regularised functional for a nonlinear forward operator and
   **derive** the Gauss–Newton update that solves it locally.
2. **Explain** why the linearisation changes the meaning of the regularisation
   parameter, and why the parameter and the starting model are entangled.
3. **Verify** an analytic Jacobian against finite differences and **measure** the
   optimal difference step.
4. **Measure** the convergence behaviour of a damped Gauss–Newton iteration and
   **state** what the step-norm contraction implies.
5. **Measure** the bias of the misfit minimum, and the set of alternative models
   whose misfit lies within the noise level.
6. **Apply** iteratively reweighted least squares to an $\ell_1$ roughness penalty
   inside the nonlinear loop, and **state** the double role of its smoothing
   constant.

All models and data in this module are **SYNTHETIC**. The forward physics is the
exact 2-D line-mass gravity formula; the geometry, the depths, the densities, the
station grid and the noise are chosen teaching values. The only physical
constant is $G = 6.67430\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$.

## Prerequisites

- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](02-tikhonov.md) —
  the linear theory this lesson extends one linearisation at a time.
- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](03-parameter-choice.md) —
  parameter choice, which becomes harder without a fixed operator.
- [18-04-01 Local Linearisation, Jacobians and Iteration](../04-nonlinear-inversion/01-local-linearization.md) —
  the mechanics of the iteration; here we add the penalty.

## 1. What changes when the operator is nonlinear

For a nonlinear forward map $F:\mathbb R^{m}\to\mathbb R^{n}$ the regularised
problem is

$$\min_{u}\ \|F(u)-d\|_2^2 + \alpha\,\Omega(u),$$

and it is solved by repeatedly linearising. At the current iterate $u_k$,

$$F(u_k+\delta) \approx F(u_k) + J_k\delta, \qquad J_k = \frac{\partial F}{\partial u}\Big|_{u_k},$$

so the Gauss–Newton step solves

$$\min_\delta\ \|J_k\delta - r_k\|_2^2 + \alpha\,\Omega(u_k+\delta),
\qquad r_k = d - F(u_k).$$

Three differences from the linear case matter, and each is measured below.

1. **$\alpha$ no longer filters a fixed spectrum.** The filter factors
   $f_i = \sigma_i^2/(\sigma_i^2+\alpha)$ of [18-03-02](02-tikhonov.md) apply to
   $J_k$, which changes at every iteration. A quoted $\alpha$ is therefore a
   property of the algorithm *and* of its trajectory, not of the problem alone.
2. **The parameter and the starting model are entangled.** A large $\alpha$ can
   make the local problem convex and take the iteration to a different basin than
   a small $\alpha$ from the same start. The two choices are made jointly whether
   or not the analyst admits it.
3. **The objective's minimum is not the truth, and the gap is not visible.**
   Non-uniqueness plus a prior produce a model that fits the data perfectly and
   is wrong; the residual cannot say by how much.

Damping is standard: replace $J^{\mathsf T}J + \alpha I$ by
$J^{\mathsf T}J + (\alpha+\lambda)I$ and adapt $\lambda$ by the usual
Levenberg–Marquardt rule (halve on success, multiply by ten on failure). The
demonstration uses $\lambda$ starting at $10^{-3}$ with a factor-of-3 decrease
and a factor-of-10 increase.

## 2. The synthetic nonlinear problem

The model vector is $u = (z/1\ \mathrm{km},\ a/(10^{9}\ \mathrm{kg\,m^{-1}}))$:
12 depths and 12 line densities, dimensionless and $O(1)$ by construction. The
forward map is the exact attraction of line masses,

$$F_i(u) = \sum_{j=1}^{12} C\,\frac{a_j z_j}{(x_i-\xi_j)^2+z_j^2},$$

which is **linear in $a$ and nonlinear in $z$**: a depth change moves the kernel
as well as scaling it. Geometry: 12 sources every $2\ \mathrm{km}$ over a
$22\ \mathrm{km}$ profile, 48 stations, true depths a Gaussian ridge from
$1.01$ to $3.09\ \mathrm{km}$, true density $2.50$ everywhere.

Data: peak $54.546\ \mathrm{mGal}$, $\|d\| = 310.102\ \mathrm{mGal}$, noise
$\sigma = 0.2727\ \mathrm{mGal}$ ($0.50\%$ of the peak), so a well-fitting model
has data term $n\sigma^2 = 3.7127\times10^{-5}$ in the normalised units used
throughout (data divided by $\|d\|$).

### The analytic Jacobian, verified

The Jacobian is available in closed form:

$$\frac{\partial F_i}{\partial a_j} = C\,\frac{z_j}{(x_i-\xi_j)^2+z_j^2},
\qquad
\frac{\partial F_i}{\partial z_j} = C\,a_j\,\frac{(x_i-\xi_j)^2-z_j^2}
{\left((x_i-\xi_j)^2+z_j^2\right)^2}
\ \text{(times }10^3\text{ for the km units)} .$$

Central differences reproduce it with a deviation that falls as $h^2$ until
round-off takes over:

| step $h$ (km) | max relative deviation |
|---|---|
| $10^{-2}$ | $8.920\times10^{-3}$ |
| $10^{-3}$ | $8.920\times10^{-5}$ |
| $10^{-4}$ | $8.920\times10^{-7}$ |
| $10^{-5}$ | $1.073\times10^{-8}$ |
| $10^{-6}$ | $4.974\times10^{-8}$ |
| $10^{-7}$ | $5.835\times10^{-7}$ |

The measured optimum is near $h = 10^{-5}\ \mathrm{km}$, in agreement with the
classical estimate $h^\star \approx \epsilon^{1/3}$ for central differences with
machine epsilon $\epsilon \approx 2\times10^{-16}$, which gives
$h^\star \approx 6\times10^{-6}$ in units where the function values are $O(1)$.
A finite-difference Jacobian at $h = 10^{-3}$ would introduce a $10^{-4}$ relative
error into every iteration; that is usually tolerable, and the table says so
quantitatively rather than by assertion.

## 3. Convergence: what a damped Gauss–Newton actually does

Starting from all depths $3.00\ \mathrm{km}$ and all densities $1.00$ with
$\alpha = 10^{-6}$, the objective evolves as follows (selected iterations):

| iteration | objective | step norm | rel. error (all) | depths | densities |
|---|---|---|---|---|---|
| 1 | 0.003541 | 6.698 | 0.45601 | 0.63915 | 0.30403 |
| 4 | 0.001434 | 3.193 | 0.11807 | 0.11277 | 0.12101 |
| 8 | 0.000124 | 0.1258 | 0.21968 | 0.29717 | 0.15872 |
| 12 | 0.000124 | $1.147\times10^{-4}$ | 0.21997 | 0.29739 | 0.15912 |
| 23 | 0.000124 | $7.1\times10^{-45}$ | 0.21997 | 0.29739 | 0.15912 |

Two things are visible and both matter.

**The model error improves and then worsens.** It falls to $0.118$ at iteration
4 and rises to $0.220$ by iteration 8, while the *objective* falls
monotonically. The algorithm minimises the objective, and the objective's
minimum is not the truth. At iteration 4 the model happened to be closer to the
truth than at convergence. **There is no stopping rule based on the data that
would have stopped at iteration 4**, and a practitioner who reports the model
after a fixed number of iterations is reporting a different estimator whose
properties are not analysed here.

**Convergence is linear, not quadratic.** The measured step-norm ratios over
iterations 6–15 settle at a nearly constant value near $0.3$:

| ratio | $\|\delta_7\|/\|\delta_6\|$ | $\|\delta_8\|/\|\delta_7\|$ | $\|\delta_{12}\|/\|\delta_{11}\|$ | $\|\delta_{14}\|/\|\delta_{13}\|$ | $\|\delta_{15}\|/\|\delta_{14}\|$ |
|---|---|---|---|---|---|
| value | 0.394 | 0.317 | 0.298 | 0.300 | 0.311 |

A constant ratio below one is linear convergence. Undamped Gauss–Newton near a
zero-residual solution shows a ratio collapsing towards zero (superlinear); the
damping $\lambda$ is what settles the ratio, and it buys robustness against a bad
start — a fair trade, but one that changes the iteration's character. Reporting
"I used Gauss–Newton, which converges quadratically" while damping is on is a
statement about a different algorithm.

## 4. The bias of the misfit minimum, measured

Sweeping $\alpha$ with the same start and data:

| $\alpha$ | data term | $\chi^2/n\sigma^2$ | rel. error | depths | densities |
|---|---|---|---|---|---|
| $10^{-10}$ | $2.0\times10^{-5}$ | 0.550 | 0.29821 | 0.27381 | 0.31140 |
| $10^{-8}$ | $2.0\times10^{-5}$ | 0.550 | 0.28417 | 0.27033 | 0.29184 |
| $10^{-6}$ | $2.3\times10^{-5}$ | 0.620 | **0.21997** | 0.29739 | 0.15912 |
| $10^{-4}$ | $4.0\times10^{-4}$ | 10.841 | 0.30707 | 0.46873 | 0.14855 |
| $10^{-2}$ | $1.9\times10^{-1}$ | 5238 | 0.59436 | 0.75930 | 0.47400 |
| $10^{-1}$ | $7.6\times10^{-1}$ | 20365 | 0.89177 | 0.90485 | 0.88415 |
| $10^{0}$ | $9.6\times10^{-1}$ | 25961 | 0.95646 | 0.90485 | 0.98496 |
| $10^{1}$ | $9.96\times10^{-1}$ | 26827 | 0.96529 | 0.90485 | 0.99845 |

Readings:

- **The best achievable error is $0.21997$** — an oracle value, since it uses the
  truth. Even at the optimum, the model is 22% wrong in the dimensionless
  parameter vector: 30% in the depths and 16% in the densities. Regularisation
  does not make this problem easy; it makes it solvable, which is different.
- **The error splits into two blocks that move in opposite directions.** From
  $\alpha = 10^{-10}$ to $10^{-6}$, the density error improves
  ($0.311 \to 0.159$) while the depth error worsens ($0.274 \to 0.297$). That is
  the depth–density trade-off: the two blocks trade accuracy with each other as
  the prior changes. A single "model error" hides it, and a report that quotes
  one number has hidden the physics.
- **The discrepancy principle lands within a factor of two.** Bisecting
  $\chi^2 = n\sigma^2$ gives $\alpha = 6.392\times10^{-6}$ with error $0.24095$,
  against the oracle's $10^{-6}$ and $0.21997$. A rule that uses only the data
  came within 10% in error here — a measured agreement on this problem, not a
  guarantee; [18-03-03](03-parameter-choice.md) shows the rule failing by four
  orders of magnitude when $\sigma$ is mis-specified.
- **Over-regularisation is silent.** At $\alpha = 10^{1}$ the model is flattened
  to a single depth near the lower clamp and the residual is $26827\,n\sigma^2$:
  the fit is visibly terrible. The dangerous regime is the middle, where
  $\chi^2$ is a factor of 10–500 above the noise level and the model still looks
  plausible.

## 5. Multiplicity: one basin, many answers

Two measurements, because they answer different questions.

**Random starts.** With 30 starts whose depths are uniform in $[0.4,4.0]$ and
densities uniform in $[0.5,4.0]$, and 40 Gauss–Newton iterations each:

| $\alpha$ | distinct minima (tolerance $10^{-3}$) | spread of model errors | median final depth range (km) |
|---|---|---|---|
| $10^{-10}$ | 1 | $5\times10^{-5}$ | 1.743 |
| $10^{-8}$ | 1 | 0 | 1.650 |
| $10^{-6}$ | 1 | 0 | 0.993 |
| $10^{-4}$ | 1 | 0 | 0.358 |
| $10^{-2}$ | 1 | 0 | 0.103 |
| $10^{-1}$ | 3 | $1.6\times10^{-4}$ | 0.000 |

So this objective has essentially **one basin of attraction** here: every start
reached a model of the same quality. That is a measurement about this problem and
it is reported as one — multimodality is not a general property of nonlinear
inversion, and claiming it without measuring it is as bad as denying it. Note
also the last column: with $\alpha$ rising, the recovered ridge amplitude
collapses from $1.74\ \mathrm{km}$ to $0$, which is the bias seen from another
angle.

**Equivalence class.** The complementary question is: given the solution and the
data, how much can the model change while the misfit stays within the noise? Take
the singular vectors of $J/\|d\|$ with the smallest singular values and move along
them until the data term reaches $n\sigma^2$. The spectrum has
$\sigma_{\max}/\sigma_{\min} = 180$ and, at the $\alpha = 10^{-6}$ solution, the
data term is $2.30\times10^{-5} = 0.620\,n\sigma^2$, leaving
$1.41\times10^{-5}$ of admissible extra misfit:

| direction (smallest singular value first) | step size | max $\|\delta z\|$ (km) | max $\|\delta a\|$ | $\chi^2/n\sigma^2$ |
|---|---|---|---|---|
| $v_{-1}$ | 1.231 | 0.2435 | 0.6290 | 1.000 |
| $v_{-2}$ | 1.020 | 0.2967 | 0.6697 | 1.000 |
| $v_{-3}$ | 0.776 | 0.3836 | 0.3852 | 1.000 |
| $v_{-4}$ | 0.803 | 0.3333 | 0.4204 | 1.000 |
| $v_{-5}$ | 1.239 | 0.6479 | 0.4683 | 1.000 |
| $v_{-6}$ | 0.643 | 0.1714 | 0.3810 | 1.000 |
| $v_{-7}$ | 0.396 | 0.1196 | 0.2637 | 1.000 |
| $v_{-8}$ | 0.375 | 0.1376 | 0.2403 | 1.000 |

Each row is an alternative model that fits the data **exactly as well as the
noise allows**, differing from the reported solution by up to $0.65\ \mathrm{km}$
of depth and $0.67$ in density — against a ridge whose amplitude is
$2.2\ \mathrm{km}$. This is what "the solution is not unique" means in numbers.
Regularisation removed the wild oscillations that would otherwise appear along
these directions; it did not remove the directions. **The ambiguity is a property
of the data; the oscillation is the symptom of trying to resolve it without a
prior.**

## 6. IRLS for an $\ell_1$ roughness penalty inside the nonlinear loop

The natural extension of [18-03-05](05-total-variation.md) to a nonlinear
operator is

$$\min_u\ \|F(u)-d\|^2 + \alpha\sum_k |(Dz)_k| + \beta\|u\|^2,$$

solved by iteratively reweighted least squares: after each Gauss–Newton solve,
recompute the weights $w_k = 1/\sqrt{(Dz)_k^2+\epsilon}$ and re-solve. The
$\epsilon$ makes the penalty differentiable and is the algorithm's smoothing
constant; the penalty is approximately
$\alpha\sum_k\sqrt{(Dz)_k^2+\epsilon}$.

Measured, with $\epsilon = 10^{-6}$ (so $\sqrt{\epsilon} = 1.0\times10^{-3}\ \mathrm{km}$
is the scale below which a difference is driven to zero, against a ridge of
$2.09\ \mathrm{km}$):

| $\alpha$ | rel. error | depths | densities | max $|Dz|$ (km) | $\chi^2/n\sigma^2$ |
|---|---|---|---|---|---|
| $10^{-8}$ | 0.33132 | 0.49464 | 0.17914 | 0.0000 | 17.66 |
| $10^{-6}$ | 0.33133 | 0.49464 | 0.17914 | 0.0000 | 17.66 |
| $10^{-4}$ | 0.33133 | 0.49464 | 0.17914 | 0.0000 | 17.66 |
| $10^{-2}$ | 0.33135 | 0.49441 | 0.17958 | 0.0000 | 17.72 |
| $10^{-1}$ | 0.39683 | 0.51161 | 0.31213 | 0.0000 | 73.41 |
| $10^{0}$ | 0.50542 | 0.71275 | 0.33165 | 0.0000 | 117.9 |

The prior is wrong — the true depth profile is a smooth ridge, and "piecewise
constant" applied to a ridge means *constant*. The result is a flat sheet, with
every depth difference **exactly** zero, at every $\alpha$ tested; the model error
rises from the Tikhonov oracle's $0.21997$ to $0.3313$ and the residual rises to
$17.7\,n\sigma^2$.

Two honest observations:

- **The data did detect this failure**, because the prior was strong enough to
  break the fit by a factor of 18 in $\chi^2$, and because $\sqrt{\epsilon}$ is
  far below the structure the model actually has. A weaker wrong prior — a
  mildly wrong $\alpha$, or a larger $\epsilon$ — would produce a plausible model
  with a residual closer to the noise level, and nothing in the data would
  object.
- **The $\epsilon$ is a hidden parameter with the same units as a model
  difference.** Reporting the result without it means a reader cannot reproduce
  or criticise the effective penalty. This is the nonlinear counterpart of the
  L-curve smoothing parameter in [18-03-03](03-parameter-choice.md).

## 7. A fully worked numeric example

**Problem.** One iteration of damped Gauss–Newton on a single-parameter problem:
$F(u) = e^{-u}$, $d = 0.5$, $u_0 = 0$, $\alpha = 0$, $\lambda = 0$.

**Step 1 — residual and Jacobian.** $F(0) = 1$, so $r = 0.5-1 = -0.5$ and
$J = -e^{-u}\big|_{0} = -1$. The Gauss–Newton equation is
$J^{\mathsf T}J\,\delta = J^{\mathsf T}r$, i.e. $1\cdot\delta = (-1)(-0.5) = 0.5$,
so $\delta = 0.5$ and $u_1 = 0.5$.

**Step 2 — check the true optimum.** $F(u) = 0.5$ gives $u^\star = \ln 2 =
0.6931$. One step moved $0.5$ of the needed $0.6931$: the linearisation $\delta$
overshoots the local derivative change, which is why iteration is needed.

**Step 3 — second iteration from $u_1 = 0.5$.** $F = 0.6065$, $r = -0.1065$,
$J = -0.6065$; $J^{\mathsf T}J = 0.3679$ and $J^{\mathsf T}r = 0.06459$, so
$\delta = 0.1756$ and $u_2 = 0.6756$: error $0.0175$.

**Step 4 — third iteration.** $F = 0.508831$, $r = -0.008831$, $J = -0.508831$;
$J^{\mathsf T}J = 0.258909$, $J^{\mathsf T}r = 0.004493$, $\delta = 0.017355$,
$u_3 = 0.692995$: error $1.52\times10^{-4}$. The error sequence
$0.693147, 0.193147, 0.017508, 0.000152$ has ratios
$0.279, 0.0906, 0.0087$ — collapsing towards zero, i.e. **superlinear** here, as
undamped Gauss–Newton should be on a problem with zero residual at the solution.

**Step 5 — what the demonstration measures instead.** With damping and a nonzero
residual (the data have noise), the same diagnostic gives a ratio near $0.3$ that
does *not* collapse. The contrast is the point: the textbook quadratic rate is a
statement about the undamped, zero-residual, well-started case, and the
demonstration reports the rate it actually achieved.

## 8. Assumptions and regime of validity

1. **The starting model is inside a basin where the linearisation is valid.**
   Measured here: all 30 random starts reached the same minimum, so this problem
   is forgiving. That is not general, and
   [18-04-07 Convergence Diagnosis and Local-Minimum Traps](../04-nonlinear-inversion/07-convergence-and-local-minima.md)
   is about the cases where it fails.
2. **The Jacobian is correct.** A finite-difference Jacobian with $h$ too large
   injects a relative error of order $h^2$ per iteration; the measured table in
   Section 2 quantifies it.
3. **The penalty is applied to the linearised problem, not the true one.**
   $\Omega(u_k+\delta)$ is used with the *current* $\Omega$; for a nonlinear
   $\Omega$ (such as IRLS weights) the weights must be updated, and each update
   changes the effective penalty.
4. **$\alpha$ keeps its meaning only along the trajectory.** Comparing two
   inversions with the same $\alpha$ but different starts is not a controlled
   comparison.
5. **The smoothing constants of the algorithm are reported.** $\lambda$ for
   damping, $\epsilon$ for IRLS: both act like $\alpha$ and both are usually
   omitted.
6. **The residual test is necessary but weak.** A wrong prior whose misfit cost
   is a factor of two is undetectable; the measured factor of 18 was.
7. **The model vector is scaled so that the penalty is meaningful.** Here depths
   are in km and densities in $10^{9}\ \mathrm{kg\,m^{-1}}$; a penalty on the raw
   vector would weight the two blocks unequally by construction, and that choice
   is another unreported parameter.

## 9. The honest summary

- Regularisation of a nonlinear problem is a sequence of regularised *linear*
  problems, and the filter-factor intuition survives one iteration at a time.
- The parameter and the starting model are chosen jointly; a report that names
  the first and not the second is incomplete.
- Damping makes the iteration robust and linear; the quadratic rate of the
  textbooks is a statement about the undamped, zero-residual case.
- The misfit minimum is biased, and the bias is known only in units: 22% in the
  parameter vector here, split differently between depths and densities.
- The ambiguity that regularisation suppresses is not removed: the measured
  equivalence class reaches $0.65\ \mathrm{km}$ of depth change at an unchanged
  $\chi^2$.
- Wrong priors are caught only when they are strong. The $\ell_1$ roughness
  experiment was caught ($\chi^2 = 17.7$); a mild version would not be.

## 10. Python demonstration

`code/nonlinear_regularization_demo.py` prints: the synthetic problem; the
analytic Jacobian verified against central differences across six step sizes;
the damped Gauss–Newton history with step-norm contraction ratios and per-block
errors; the $\alpha$ sweep with the discrepancy $\alpha$ and the oracle; the
random-start experiment; the equivalence-class sampling in the eight
least-observed directions; and the IRLS $\ell_1$ roughness experiment with its
hidden $\epsilon$.

```bash
cd 18-inverse-problems/03-regularization/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nonlinear_regularization_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, under a second.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/07-nonlinear-regularization-exercises.md`](exercises/07-nonlinear-regularization-exercises.md)
and
[`exercises/07-nonlinear-regularization-solutions.md`](exercises/07-nonlinear-regularization-solutions.md).

- **★** Reproduce the first three iterations of Section 7 by hand and tabulate
  the error ratios.
- **★★** Derive the IRLS weight $w_k = 1/\sqrt{(Dz)_k^2+\epsilon}$ from the
  derivative of $\sqrt{(Dz)_k^2+\epsilon}$, and state what the weights do as
  $\epsilon\to0$.
- **★★★** Design an experiment that measures how the depth–density error split
  depends on the penalty operator (magnitude only, depth-only roughness, both),
  and predict which block degrades in each case.

## 12. Mastery checkpoint

Complete this without notes:

> A nonlinear inversion with $\alpha = 10^{-6}$ reports a model with 30% depth
> error and 16% density error, a data term of $0.62\,n\sigma^2$, and a converged
> objective. **(a)** State the oracle error and whether the reported one is
> close. **(b)** An alternative model differs along $v_{-5}$ by $0.65\
> \mathrm{km}$ of depth with $\chi^2 = 1.000$. Is the reported solution "the"
> answer? **(c)** The analyst's colleague re-runs from a different start with the
> same $\alpha$ and gets the same model. What does that prove, and what does it
> not prove? **(d)** The analyst then imposes a piecewise-constant prior and
> obtains $\chi^2 = 17.7$. Should the prior be kept, and on what evidence?

A worked version of (a)–(c) appears in
[`exercises/07-nonlinear-regularization-solutions.md`](exercises/07-nonlinear-regularization-solutions.md).

## 13. Common pitfalls

1. **Reporting the parameter without the start and the damping.** The estimator
   is the triple $(\alpha,\lambda,u_0)$.
2. **Stopping when the objective stops improving.** The model error rose from
   0.118 to 0.220 after the objective had effectively converged.
3. **Claiming quadratic convergence with damping on.** The measured contraction
   was a constant $0.3$.
4. **Reading the residual as a bias estimate.** $0.62\,n\sigma^2$ co-exists with
   a 22% model error.
5. **Treating non-uniqueness as multimodality.** The random starts found one
   basin; the ambiguity showed up as a flat valley, which is a different
   measurement.
6. **Forgetting small constants.** $\lambda$ and $\epsilon$ both act as extra
   regularisation parameters and both must be stated.
7. **Comparing runs with different starts at equal $\alpha$.** The comparison is
   not controlled; the trajectories differ.

## 14. Where this is used

- **Traveltime and waveform tomography.** Gauss–Newton or its matrix-free
  relatives with a smoothing penalty on the velocity model; the trade-off is
  between resolving shallow detail and keeping the update stable.
- **Potential-field depth inversion.** The depth–density trade-off measured here
  is the standard ambiguity of basin and intrusion modelling.
- **Joint inversion of nonlinear data sets.** Each data set supplies its own
  Jacobian and its own misfit weight; see
  [18-07-01 Joint Inversion: Concepts and Weighting](../07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md).
- **Machine learning with non-convex losses.** Damping and early stopping play
  the roles of $\lambda$ and $\alpha$; the entanglement of parameter choice with
  the starting point is identical; see
  [21-04-04 Regularisation: Ridge, Lasso, Early Stopping](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/04-regularization-ml.md).

## 15. Related modules

- [18-04-02 Gradient, Gauss-Newton and Full Newton Methods](../04-nonlinear-inversion/02-gradient-and-newton.md) —
  the methods whose rates are quoted here, without the penalty.
- [18-04-03 Conjugate Gradient and Large-Scale Inversion](../04-nonlinear-inversion/03-conjugate-gradient-inverse.md) —
  what to do when $J^{\mathsf T}J$ cannot be formed.
- [18-04-07 Convergence Diagnosis and Local-Minimum Traps](../04-nonlinear-inversion/07-convergence-and-local-minima.md) —
  diagnosing the failure modes that this problem happened not to exhibit.
- [18-06-02 Monte Carlo Propagation and Its Convergence](../06-uncertainty-quantification/02-monte-carlo-uq.md) —
  turning the equivalence class of Section 5 into an uncertainty statement.
- [18-08-02 Synthetic Testing, Checkerboards and Recovery Tests](../08-practical-inversion-workflow/02-synthetic-testing.md) —
  how to design the synthetic experiment that produced every number above.

## 16. Self-assessment checklist

- [ ] I can write the Gauss–Newton step for a penalised nonlinear problem.
- [ ] I can verify an analytic Jacobian and choose a difference step.
- [ ] I can read a step-norm contraction ratio and say what it means.
- [ ] I can measure an equivalence class from the Jacobian's small singular
      vectors.
- [ ] I can implement IRLS for an $\ell_1$ roughness penalty and state its
      smoothing constant.
- [ ] I can name the five or six numbers a nonlinear inversion must report.
