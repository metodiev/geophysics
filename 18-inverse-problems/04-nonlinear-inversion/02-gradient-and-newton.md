---
id: 18-04-02
title: "Gradient, Gauss-Newton and Full Newton Methods"
level: graduate
prereqs: ["18-04-01", "18-03-02", "01-14-02"]
tags: [inverse-problems, nonlinear-inversion, gauss-newton, newton, optimization]
---

# Gradient, Gauss-Newton and Full Newton Methods

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the steepest-descent, Gauss–Newton, full-Newton and
   Levenberg–Marquardt steps, and **state** the per-iteration cost of each.
2. **Verify** the textbook rate $1-1/\kappa$ of steepest descent against a
   measured rate on a problem with a prescribed spectrum.
3. **Compare** conjugate gradients with steepest descent in iteration count and
   **explain** why the measured ratio exceeds $\sqrt\kappa$.
4. **Derive** the exact Hessian of a nonlinear least-squares objective and
   **measure** where it differs from $J^{\mathsf T}J$, including where it becomes
   indefinite.
5. **Explain** why a full Newton step can be worse than a Gauss–Newton step when
   the residual is large.
6. **Choose** a method from the measured cost and the properties of the problem.

All models and data in this module are **SYNTHETIC**: a quadratic model with a
prescribed spectrum and a chosen exponential-decay forward model, with chosen
noise. Nothing is measured.

## Prerequisites

- [18-04-01 Local Linearisation, Jacobians and Iteration](01-local-linearization.md) —
  the Jacobian and the linearised subproblem.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../03-regularization/02-tikhonov.md) —
  the damped normal equations that a Gauss–Newton step solves.
- [01-14-02 Unconstrained Minimisation: Gradient, Newton, Quasi-Newton](../../01-mathematics/14-optimization/02-unconstrained.md) —
  the classical algorithms in the optimisation setting.

## 1. Four step rules

All four methods minimise the same objective
$\phi(u) = \tfrac12\|F(u)-d\|_2^2$ but differ in how they use curvature.

| method | step $\delta$ | cost per iteration |
|---|---|---|
| steepest descent | $-\nabla\phi/L$, $L=\|J^{\mathsf T}J\|_2$ | one Jacobian, no solve |
| Gauss–Newton | $-(J^{\mathsf T}J)^{-1}\nabla\phi$ | one Jacobian, one $m\times m$ solve |
| full Newton | $-\left(\nabla^2\phi\right)^{-1}\nabla\phi$ | one Jacobian, one Hessian, one solve |
| Levenberg–Marquardt | $-(J^{\mathsf T}J+\lambda I)^{-1}\nabla\phi$ | one Jacobian, one solve per trial $\lambda$ |

with

$$\nabla\phi = J^{\mathsf T}(F-d), \qquad
\nabla^2\phi = J^{\mathsf T}J + \sum_i (F-d)_i\,\nabla^2F_i .$$

The last identity is the whole story of this lesson. Gauss–Newton *drops* the
second-derivative sum; Newton keeps it; Levenberg–Marquardt keeps the
$J^{\mathsf T}J$ approximation and adds damping to stay inside the region where
the linearisation is valid ([18-04-01](01-local-linearization.md) measured that
region).

**Convergence-rate theory.** For a quadratic objective with Hessian eigenvalues
in $[\lambda_{\min},\lambda_{\max}]$ and $\kappa = \lambda_{\max}/\lambda_{\min}$,
steepest descent with the optimal constant step has worst-case rate
$1-1/\kappa$, and conjugate gradients has rate
$(\sqrt\kappa-1)/(\sqrt\kappa+1)$. Newton's method on a quadratic converges in one
step. Both bounds are *worst case*, and the demonstration measures how the worst
case compares with what actually happens.

## 2. The rates, measured on a quadratic problem

The demonstration builds a $15\times15$ Hessian with a **prescribed** spectrum,
eigenvalues $\log$-spaced from $1.0$ to $100$, so $\kappa = 100$ exactly, and
minimises $\tfrac12u^{\mathsf T}Hu-b^{\mathsf T}u$ with $b = Hu_\star$.

| method | predicted rate | measured asymptotic ratio |
|---|---|---|
| steepest descent | $1-1/\kappa = 0.990000$ | $0.989999$ |
| conjugate gradients | $(\sqrt\kappa-1)/(\sqrt\kappa+1) = 0.81818$ | — (see below) |

The steepest-descent rate is reproduced to six decimal places. That is not a
coincidence: once the component of the error along the *smallest* eigenvector
dominates, the iteration's ratio is exactly $1-\lambda_{\min}/\lambda_{\max}$.
Measuring the rate therefore also identifies *which* direction is holding the
iteration back.

| method | error after 10 | after 100 | after 1000 | iterations to $10^{-6}$ |
|---|---|---|---|---|
| steepest descent | $2.778$ | $0.4287$ | $1.781\times10^{-5}$ | 1287 (predicted 1375) |
| conjugate gradients | $0.1455$ | — | — | **17** (bound 69) |

Conjugate gradients reaches the same tolerance in 17 iterations against steepest
descent's 1287, a ratio of $75.7$. Two honest observations:

1. **The measured ratio exceeds $\sqrt\kappa = 10$.** The CG bound is a worst case
   over matrices with that condition number; on this matrix CG beat its own bound
   by a factor of four (17 versus 69). Quoting "CG is $\sqrt\kappa$ times faster"
   as a prediction is therefore conservative, and quoting the bound as the
   expected cost would badly overestimate it.
2. **The steepest-descent prediction is accurate (1287 measured, 1375
   predicted).** Worst-case bounds for steepest descent are, for this problem,
   descriptive rather than pessimistic.

## 3. The same five methods on a nonlinear problem

Now $d(t) = Ae^{-\alpha t}$, 25 samples on $[0,10]$, truth $(3.0,0.5)$, noise
$0.50\%$ of the peak, start $(1.0,0.10)$, and a common stopping rule (relative
objective change below $10^{-12}$):

| method | iterations | final objective | $\|u-u_{\mathrm{true}}\|$ |
|---|---|---|---|
| steepest descent | 348 | $2.523485\times10^{-3}$ | $2.337\times10^{-2}$ |
| Gauss–Newton | 5 | $2.523485\times10^{-3}$ | $2.336\times10^{-2}$ |
| full Newton | 8 | $2.523485\times10^{-3}$ | $2.336\times10^{-2}$ |
| Levenberg–Marquardt | 5 | $2.523485\times10^{-3}$ | $2.336\times10^{-2}$ |

Three measurements and their explanations:

1. **All four reach the same point** — the least-squares solution, with the same
   final model error. For a two-parameter problem with a unique minimum, the
   method affects only the route.
2. **Steepest descent is 70 times more expensive than Gauss–Newton.** The
   measured $\kappa$ of the final $J^{\mathsf T}J$ is of order $10^{3}$ here, and
   the steepest-descent rate $1-1/\kappa$ predicts exactly this kind of gap.
3. **Full Newton needs *more* iterations than Gauss–Newton (8 versus 5).** This
   looks like a contradiction of the textbook and it is not: the Newton step is
   taken undamped and un-line-searched, so when the Hessian is indefinite or the
   step is long — as it is at the start, where the residual is large — the step can
   *increase* the objective. The demonstration's Newton loop has no safeguard, so
   it wastes iterations. A damped Newton method is the Levenberg–Marquardt
   variant, which ties Gauss–Newton at 5 iterations here.

**The conclusion is not "Newton is worse"** — on the exact-data problem below it
is quadratically better — but that **a curvature model without a global
safeguard is not automatically an improvement**, and the safeguard is a measured
part of the algorithm, not a detail.

### With exact data

| method | errors per iteration | measured orders |
|---|---|---|
| Gauss–Newton | $7.3\times10^{-1}$, $2.0\times10^{-2}$, $2.45\times10^{-4}$, $9.4\times10^{-8}$, $8.3\times10^{-15}$ | 2.13, 1.95, 2.00 |
| full Newton | $1.41$, $0.710$, $0.257$, $5.62\times10^{-2}$, $4.18\times10^{-3}$, $2.97\times10^{-5}$ | 2.12, 1.90, 1.90 |

Both are superlinear once the iterates are close, and both stop at machine
precision because the residual can reach zero. With noise (Section 3) neither can
do better than linear convergence to the noise floor, and the order distinction
disappears — which is why the cost comparison on real data is about robust
descent, not about the asymptotic order.

## 4. A fully worked numeric example: three steps, one start

**Problem.** With $t = (0,1)$ and $d = (3.0,1.8)$, take $u_0 = (2.0,0.5)$ and
compute the steepest-descent, Gauss–Newton and Newton steps.

**Step 1 — residual and Jacobian.**
$F(u_0) = (2.0,\,1.213061)$, so $F-d = (-1.0,\,-0.586939)$ and

$$J = \begin{pmatrix}1 & 0\\ 0.606531 & -1.213061\end{pmatrix},
\qquad
\nabla\phi = J^{\mathsf T}(F-d) = \begin{pmatrix}-1.355996\\ 0.711993\end{pmatrix}.$$

**Step 2 — curvature.**

$$J^{\mathsf T}J = \begin{pmatrix}1.367879 & -0.735759\\ -0.735759 &
1.471518\end{pmatrix}, \qquad \lambda = (0.682117,\ 2.157280), \quad
\kappa = 3.163 .$$

The exact Hessian adds the residual-curvature term

$$\sum_i (F-d)_i\nabla^2F_i = \begin{pmatrix}0 & 0\\ 0 & 0.711993\end{pmatrix},
\qquad
\nabla^2\phi = \begin{pmatrix}1.367879 & -0.735759\\ -0.735759 &
2.183510\end{pmatrix}.$$

**Step 3 — the three steps and what they achieve.**

| step | $\delta$ | new $\alpha$ | objective |
|---|---|---|---|
| start | — | 0.500000 | 0.672249 |
| steepest descent, $1/L$ | $(0.628568,\ -0.330042)$ | 0.169958 | 0.156227 |
| Gauss–Newton | $(1.000000,\ 0.016151)$ | 0.516151 | $4.6\times10^{-5}$ |
| full Newton | $(0.996540,\ 0.009719)$ | 0.509719 | $6.0\times10^{-6}$ |

**Interpretation.** Steepest descent moves $\alpha$ in the *wrong direction* and
by twenty times too much, because the raw gradient is dominated by the amplitude
coordinate: the gradient is $(-1.36,+0.71)$ while the objective's curvature
across those directions differs by a factor of $3.2$. Multiplying by
$(J^{\mathsf T}J)^{-1}$ — Gauss–Newton — rescales the badly conditioned direction
and lands within $3\%$ of the best possible objective in one step. Newton's extra
term improves the step further (objective $6.0\times10^{-6}$ versus
$4.6\times10^{-5}$, a factor of 7.7) because the residual at the start is large:
the objective is $0.672$, so the curvature correction is a first-order effect and
not a detail.

This is the quantitative answer to "why not just use the gradient": the gradient
ignores curvature, and curvature is what makes a nonlinear inverse problem
nonlinear.

## 5. Where Gauss–Newton and Newton differ, measured

| point $(A,\alpha)$ | $\lambda_{\min}(J^{\mathsf T}J)$ | $\lambda_{\min}(\nabla^2\phi)$ | objective |
|---|---|---|---|
| $(3.00,0.50)$ | $1.7183$ | $1.7017$ | $3.2086\times10^{-3}$ |
| $(1.00,0.10)$ | $4.2527$ | $6.9621$ | $5.0627$ |
| $(5.00,0.10)$ | $4.3888$ | $7.5606$ | $82.165$ |
| $(0.20,2.00)$ | $2.4569\times10^{-3}$ | $\mathbf{-0.17826}$ | $12.265$ |

- $J^{\mathsf T}J$ is positive semi-definite **everywhere** — by construction, for
  any $J$. A Gauss–Newton step is therefore always a descent direction, which is
  why it needs no safeguard.
- The exact Hessian is **indefinite** at $(0.20,2.00)$, where the residual is
  large ($\phi = 12.265$). A Newton step there is not guaranteed to decrease the
  objective, and the undamped run in Section 3 is exactly the case in point.
- At the solution the two matrices nearly coincide ($1.7183$ versus $1.7017$,
  a $1\%$ difference): when the residual is small the curvature correction is
  negligible, which is why Gauss–Newton converges quadratically there
  ([18-04-01 §5](01-local-linearization.md)).

## 6. Assumptions and regime of validity

1. **The objective is a least-squares misfit.** Gauss–Newton's cheap curvature is
   $J^{\mathsf T}J$; for a general objective (an $\ell_1$ misfit, a
   robust loss, a penalty term) the structure changes and the method must be
   re-derived.
2. **The parameters are scaled comparably.** The worked example shows the
   curvature across the two coordinates differing by a factor of $3.2$; with worse
   scaling, an unscaled steepest-descent step becomes useless rather than slow.
3. **A safeguard is present whenever the curvature model is not positive
   definite.** The measured indefinite Hessian is the evidence; Levenberg–Marquardt
   or a line search is the remedy.
4. **The rate bounds are worst-case.** Measured: the steepest-descent bound was
   accurate to $0.001\%$, the CG bound was pessimistic by a factor of four. Both
   numbers should be *measured* on the problem at hand before being used to plan.
5. **Iteration counts, not floating-point time, are the honest cost unit.** Each
   iteration here is one Jacobian plus one small solve; in large problems the
   relative costs change and the comparison must be redone.
6. **The stopping rule is part of the method.** The Newton run's 8 iterations were
   caused by the absence of a safeguard, not by the curvature model.

## 7. The honest summary

- Four step rules, one objective. Their differences are the curvature model and
  the safeguard, both measurable.
- The steepest-descent rate $1-1/\kappa$ is reproducible to six decimals on a
  controlled spectrum, which makes it a usable planning tool.
- The CG bound is pessimistic by a factor of four here; the measured iteration
  count is what a practitioner should quote.
- $J^{\mathsf T}J$ is always positive semi-definite; the true Hessian need not be,
  and the demonstration exhibits an indefinite point with a measured negative
  eigenvalue.
- On noisy data all methods end at the same noise floor; the differences are in
  the number of iterations and in the robustness, not in the answer.
- A full Newton step without a safeguard can be worse than Gauss–Newton. Any
  claim that a higher-order method is faster must come with the safeguard that
  was used.

## 8. Python demonstration

`code/gradient_newton_demo.py` prints: the quadratic model with a prescribed
spectrum and the measured steepest-descent rate against $1-1/\kappa$; the CG
comparison with predicted and measured iteration counts; the five-method race on
the nonlinear problem; the exact-data error histories with measured orders; and
the eigenvalue table for $J^{\mathsf T}J$ against the full Hessian.

```bash
cd 18-inverse-problems/04-nonlinear-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gradient_newton_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, under a second.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/02-gradient-and-newton-exercises.md`](exercises/02-gradient-and-newton-exercises.md)
and
[`exercises/02-gradient-and-newton-solutions.md`](exercises/02-gradient-and-newton-solutions.md).

- **★** From Section 4, compute the objective after the steepest-descent step
  with the step halved, and state whether the halved step is closer to the
  Gauss–Newton step's result.
- **★★** Derive the optimal constant step for quadratic steepest descent and show
  that the worst-case rate over a spectrum with condition number $\kappa$ is
  $1-1/\kappa$.
- **★★★** Design an experiment that measures the iteration count of Gauss–Newton
  and Levenberg–Marquardt as a function of the condition number of
  $J^{\mathsf T}J$, and predict which method wins at large $\kappa$.

## 10. Mastery checkpoint

Complete this without notes:

> On the exponential-decay problem a colleague reports: "Gauss–Newton converged
> in 5 iterations, full Newton in 8, so Newton's method is slower — the quadratic
> rate is a myth." **(a)** State what is missing from the Newton implementation.
> **(b)** Give the measured evidence that $J^{\mathsf T}J$ is always a safe
> curvature model while the exact Hessian is not. **(c)** On the quadratic
> problem the measured steepest-descent ratio was $0.989999$ against a bound of
> $0.990000$; state what that tells you about the bound. **(d)** Write the two
> numbers you would report for a method comparison, and why the iteration count
> is the honest one here.

A worked version of (a)–(c) appears in
[`exercises/02-gradient-and-newton-solutions.md`](exercises/02-gradient-and-newton-solutions.md).

## 11. Common pitfalls

1. **Assuming the higher-order method is faster.** Measured: undamped Newton
   needed 8 iterations against Gauss–Newton's 5.
2. **Using the raw gradient for a poorly scaled problem.** In the worked example
   it moved the parameter in the wrong direction entirely.
3. **Quoting a rate bound as a prediction.** The CG bound was pessimistic by a
   factor of four; measure instead.
4. **Treating $J^{\mathsf T}J$ as the Hessian near a large residual.** The
   measured $1\%$ agreement at the solution becomes a $7\times$ error in the step
   at the start.
5. **Comparing methods with different stopping rules.** The iteration counts are
   only comparable when the rule is identical.
6. **Forgetting that $J^{\mathsf T}J$ being PSD does not make the objective
   convex.** It makes each Gauss–Newton step a descent direction, which is weaker.

## 12. Where this is used

- **Traveltime tomography.** Gauss–Newton with damping is the standard solver;
  the damping parameter is set by the same trade-off as a Tikhonov $\alpha$.
- **Full-waveform inversion.** Matrix-free Gauss–Newton and limited-memory
  quasi-Newton methods are used because the Hessian cannot be formed; the
  curvature question of Section 5 is the reason quasi-Newton works.
- **Curve fitting in rock physics and well logging.** Two- and three-parameter
  problems exactly like this one, where a hand-coded Jacobian and Gauss–Newton
  suffice.
- **Optimisation in machine learning.** Steepest descent, momentum and quasi-Newton
  methods are the same family; the condition-number analysis carries over
  unchanged; see
  [01-14-02 Unconstrained Minimisation: Gradient, Newton, Quasi-Newton](../../01-mathematics/14-optimization/02-unconstrained.md).

## 13. Related modules

- [18-04-03 Conjugate Gradient and Large-Scale Inversion](03-conjugate-gradient-inverse.md) —
  the large-scale version of the normal-equation solve used here.
- [18-04-06 Multi-Start, Hybrid and Memetic Strategies](06-multi-start-and-hybrid.md) —
  what to do when the local method converges to the wrong minimum.
- [18-03-07 Regularisation of Nonlinear Problems](../03-regularization/07-nonlinear-regularization.md) —
  adding a penalty changes the curvature model and the damping.
- [01-14-01 Convexity, Stationarity and Optimality Conditions](../../01-mathematics/14-optimization/01-convexity.md) —
  the theory behind the definiteness arguments.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../../19-numerical-modeling-hpc/01-numerical-foundations/02-convergence-and-error.md) —
  how to measure and report a convergence order.

## 14. Self-assessment checklist

- [ ] I can write all four step rules and their costs.
- [ ] I can compute $\nabla^2\phi$ exactly for a least-squares objective.
- [ ] I can explain and verify the $1-1/\kappa$ rate.
- [ ] I can say when $J^{\mathsf T}J$ is a safe curvature model and when it is not.
- [ ] I can show with numbers why an unsafeguarded Newton step can lose.
- [ ] I can choose a method from measured cost rather than from reputation.
