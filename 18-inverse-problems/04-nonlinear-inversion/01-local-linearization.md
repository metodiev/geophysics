---
id: 18-04-01
title: "Local Linearisation, Jacobians and Iteration"
level: graduate
prereqs: ["18-03-02", "18-01-01", "01-07-10"]
tags: [inverse-problems, nonlinear-inversion, jacobian, linearization, gauss-newton]
---

# Local Linearisation, Jacobians and Iteration

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** a nonlinear inverse problem as a sequence of linearised
   subproblems, and **state** precisely what the linearisation assumes.
2. **Derive** the Jacobian of a simple geophysical forward model and **derive**
   the Gauss–Newton step from the normal equations of the linearised problem.
3. **Verify** an analytic Jacobian against finite differences, and **measure**
   the step size that minimises the difference.
4. **Measure** the order of the linearisation error and **explain** why it sets
   the convergence rate of the iteration.
5. **Measure** the basin of attraction of a Gauss–Newton iteration and
   distinguish a basin-boundary failure from a flat-region failure.
6. **Explain** why the quadratic convergence of the textbook results is not
   available when the data are noisy.

All models and data in this module are **SYNTHETIC**. The forward physics used
here is a chosen exponential-decay model, $d(t) = A\,e^{-\alpha t}$; the
parameters and the noise are teaching values, and nothing is measured.

## Prerequisites

- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../03-regularization/02-tikhonov.md) —
  the linear inverse problem that each linearised step solves.
- [18-01-01 Forward vs Inverse Problems and the Practical Asymmetry](../01-inverse-problem-foundations/01-forward-and-inverse.md) —
  why the forward map is easy and the inverse map is not.
- [01-07-10 Matrix Calculus and Sensitivity Derivatives](../../01-mathematics/07-linear-algebra/10-matrix-calculus.md) —
  the calculus used to build Jacobians.

## 1. Why iterate at all

A nonlinear forward map $F:\mathbb R^{m}\to\mathbb R^{n}$ produces data that are
not a linear function of the model. Writing the residual as

$$r(u) = d - F(u), \qquad \text{objective } \phi(u) = \tfrac12\|r(u)\|_2^2,$$

the stationarity condition $\nabla\phi = -J(u)^{\mathsf T}r(u) = 0$ is a
nonlinear system in $u$ that has no closed-form solution in general. The standard
response is to *replace the problem by a sequence of linear ones*:

$$F(u_k+\delta) \approx F(u_k) + J_k\delta, \qquad
J_k = \frac{\partial F}{\partial u}\Big|_{u_k},$$

and to choose the step that best fits the residual *under that approximation*:

$$\delta_k = \arg\min_\delta\ \tfrac12\|J_k\delta - r_k\|_2^2
\;\Rightarrow\;
J_k^{\mathsf T}J_k\,\delta_k = J_k^{\mathsf T}r_k .$$

This is Gauss–Newton. Everything in this lesson follows from the single fact that
the approximation is valid only nearby: **the iteration is a local method, and the
word "local" is a quantitative statement that can be measured.**

## 2. The model used throughout

$$d(t) = A\,e^{-\alpha t}, \qquad u = (A,\alpha),$$

with $t$ on $[0,10]\ \mathrm{s}$ in 20 samples and a synthetic truth
$A = 3.0$, $\alpha = 0.5\ \mathrm{s^{-1}}$. The derivative with respect to the
decay constant is the one that carries the nonlinearity:

$$J = \frac{\partial d}{\partial u} =
\begin{pmatrix}
e^{-\alpha t_1} & -A\,t_1e^{-\alpha t_1}\\
\vdots & \vdots\\
e^{-\alpha t_n} & -A\,t_ne^{-\alpha t_n}
\end{pmatrix}.$$

The model is linear in $A$ and *bilinear* in $(A,\alpha)$: doubling both $A$ and
$\alpha$ is not a symmetry, but scaling $A$ alone is. That asymmetry is what
makes the two parameters recoverable at different rates, and it is visible in
every measurement below.

## 3. Verifying the Jacobian

An analytic Jacobian is a piece of algebra and is worth checking. With central
differences,

$$J^{\mathrm{fd}}_{ij} = \frac{F_i(u+he_j)-F_i(u-he_j)}{2h},$$

the truncation error is $O(h^2)$ and the round-off error is
$O(\epsilon/h)$, so the optimal step is $h^\star\sim\epsilon^{1/3}$ with
$\epsilon$ the machine epsilon. The demonstration measures:

| step $h$ | max relative deviation |
|---|---|
| $10^{-2}$ | $1.668\times10^{-3}$ |
| $10^{-3}$ | $1.667\times10^{-5}$ |
| $10^{-4}$ | $1.667\times10^{-7}$ |
| $10^{-5}$ | $1.664\times10^{-9}$ |
| $10^{-6}$ | $3.100\times10^{-10}$ (best) |
| $10^{-7}$ | $3.889\times10^{-9}$ |
| $10^{-8}$ | $3.448\times10^{-8}$ |

The deviation falls by exactly a factor of 100 per decade of $h$ — the $O(h^2)$
law — until $h = 10^{-6}$, where round-off takes over and it *rises* again. The
measured best step is $h = 10^{-6}$ with a deviation of $3.100\times10^{-10}$,
against the classical estimate $\epsilon^{1/3} = 6.0\times10^{-6}$. The
factor-of-six agreement is as good as the $O(1)$ constant in that estimate
allows. The practical conclusion: a
finite-difference Jacobian is adequate if the step is chosen in the right decade,
and hopeless if it is chosen four decades away.

## 4. How large is the linearisation error?

Take a fixed direction $p = (0.6,-0.8)$ and measure

$$\text{res}(h) = \left\|F(u_\star+hp) - F(u_\star) - J(u_\star)\,hp\right\|_2 .$$

| $h$ | res | res$/h^2$ | fitted order |
|---|---|---|---|
| 0.400 | 2.303 | 14.39 | — |
| 0.200 | 0.3882 | 9.706 | 2.568 |
| 0.100 | 0.08296 | 8.296 | 2.226 |
| 0.050 | 0.019322 | 7.729 | 2.102 |
| 0.025 | 0.0046699 | 7.472 | 2.049 |

The fitted order converges to 2: the linearisation error is $O(\|hp\|^2)$, so
**halving the step quarters the error**. Two consequences:

- The approximation is accurate to first order and no better. A single
  Gauss–Newton step therefore removes only a fraction of the error when the
  residual is large.
- Near a zero-residual solution, errors of size $e$ produce a *linear* model
  error of size $e^2$, which is why the iteration can gain two digits per step
  there and only one digit per step elsewhere.

## 5. The iteration, measured

From a start with $\alpha$ wrong by a factor of five,
$(A,\alpha) = (1.0,0.10)$, with damped Gauss–Newton on noisy data (noise $0.50\%$
of the peak):

| iteration | objective | $\|u-u_{\mathrm{true}}\|$ |
|---|---|---|---|
| 1 | $8.388\times10^{-1}$ | $7.021\times10^{-1}$ |
| 2 | $1.065\times10^{-2}$ | $1.627\times10^{-2}$ |
| 3 | $6.014\times10^{-3}$ | $1.724\times10^{-3}$ |
| 4 | $6.012\times10^{-3}$ | $1.285\times10^{-3}$ |
| 9 | $6.012\times10^{-3}$ | $1.292\times10^{-3}$ (no descent step: stopped) |

Three measured facts:

1. **The objective reaches the noise floor in four iterations.** With
   $\sigma^2 n \approx 6.0\times10^{-3}$ of residual variance, the objective cannot
   fall further; the remaining model error, $1.3\times10^{-3}$ in the Euclidean
   parameter norm, is the noise-driven part.
2. **The model error plateaus with the objective.** The two stop together because
   both are functions of the same residual.
3. **Convergence on a nonzero-residual problem is linear.** With noisy data the
   classic quadratic rate is unavailable: the Hessian of the objective at the
   solution is $J^{\mathsf T}J$ (nonzero), and Gauss–Newton behaves as a linearly
   convergent fixed-point iteration. This is not a defect of the implementation
   and no step-size rule repairs it.

The same experiment with **exact** data, from the same start:

| iteration | objective | error | measured order |
|---|---|---|---|
| 1 | $8.415\times10^{-1}$ | $7.071\times10^{-1}$ | — |
| 2 | $4.415\times10^{-3}$ | $1.742\times10^{-2}$ | — |
| 3 | $8.308\times10^{-7}$ | $2.133\times10^{-4}$ | 2.087 |
| 4 | $5.437\times10^{-14}$ | $7.270\times10^{-8}$ | 1.945 |
| 5 | $4.134\times10^{-25}$ | $5.210\times10^{-13}$ | 1.721 |
| 6 | 0 | 0 | — |

The measured order is about 2 — quadratic — exactly where the theory says it
should be. **The difference between the two tables is the difference between
"nonlinear least squares" (linear convergence, noise floor) and the textbook
quadratic Newton behaviour (zero residual).** Reporting the second when the data
are noisy is a common and consequential error.

## 6. The basin of attraction, measured

Gauss–Newton from a grid of 49 starts with $A\in\{0.5,\dots,6.0\}$ and
$\alpha\in\{0.1,\dots,1.5\}$: **49 of 49 reached the true model** (relative error
below $10^{-3}$ in both parameters), with the largest converging start at a
parameter distance of $3.162$ from the truth. Remote starts
$(50,5)$, $(-5,0.5)$, $(0.001,0.001)$ and $(100,0.001)$ also converged.

The single measured failure is instructive. From $(1000,1000)$ the iteration
stalls at $(2.9929, 1000.0000)$ with objective $13.0386$, against
$6.0171\times10^{-3}$ at the truth. The reason is not a competing minimum: at
$\alpha = 1000$ the model $e^{-1000t}$ underflows to zero, so the Jacobian column
$\partial d/\partial\alpha = -At\,e^{-\alpha t}$ is numerically zero, the
gradient vanishes, and the iteration is at a **stationary point of a flat
region** rather than at a solution. A stopping rule based on $\|\nabla\phi\|$
accepts it. This failure mode — gradient zero, objective large — is the subject of
[07 Convergence Diagnosis and Local-Minimum Traps](07-convergence-and-local-minima.md).

Measured conclusion: for this problem the basin *boundary* was not reached by any
tested start; the observed failure was numerical flatness. That distinction
matters, because the remedies are different (better starting models versus better
parameter scaling).

## 7. A fully worked numeric example

**Problem.** One Gauss–Newton step for $d(t) = Ae^{-\alpha t}$ with a
two-sample data set: $t = (0,1)$, $d = (3.0, 1.8)$, from
$u_0 = (2.0, 0.5)$.

**Step 1 — evaluate the model and residual.**
$F(u_0) = (2.0,\ 2.0e^{-0.5}) = (2.0,\ 1.2131)$; so
$r = d - F = (1.0,\ 0.5869)$.

**Step 2 — build the Jacobian.**

$$J = \begin{pmatrix} 1 & 0\\ e^{-0.5} & -A\cdot 1\cdot e^{-0.5}\end{pmatrix}
= \begin{pmatrix} 1 & 0\\ 0.6065 & -1.2131\end{pmatrix}.$$

**Step 3 — normal equations.**

$$J^{\mathsf T}J = \begin{pmatrix} 1.3679 & -0.7358\\ -0.7358 & 1.4716\end{pmatrix},
\qquad
J^{\mathsf T}r = \begin{pmatrix} 1.3561\\ -0.7121\end{pmatrix}.$$

**Step 4 — solve.** $\det(J^{\mathsf T}J) = 1.367879\times1.471518 -
0.735759^2 = 2.012905-0.541341 = 1.471564$, so

$$\delta = \frac{1}{1.471564}
\begin{pmatrix} 1.471518 & 0.735759\\ 0.735759 & 1.367879\end{pmatrix}
\begin{pmatrix} 1.355996\\ -0.711993\end{pmatrix}
= \begin{pmatrix} 1.000000\\ 0.016151\end{pmatrix},$$

giving $u_1 = (3.0,\ 0.516151)$. The amplitude is *exactly* right after one step
(the model is linear in $A$: the first column of $J$ does not involve $A$), while
the decay constant lands $0.0053$ above the value
$\alpha = \ln(3.0/1.8) = 0.510826$ that fits the second sample exactly.

**Step 5 — why the second parameter overshoots and then converges quadratically.**
The linearisation in $\alpha$ uses the derivative at $\alpha = 0.5$, and the true
relation is exponential, so the step overshoots. Iterating: $u_1 = (3,0.516151)$
with $\alpha$ error $5.3\times10^{-3}$; $u_2 = (3,0.510811)$ with error
$1.5\times10^{-5}$; $u_3 = (3,0.510826)$ with error $1.8\times10^{-10}$. The
error sequence $5.3\times10^{-3}, 1.5\times10^{-5}, 1.8\times10^{-10}$ has
ratios $2.8\times10^{-3}$ and $1.2\times10^{-5}$ — collapsing, i.e. **quadratic**
convergence, because this two-sample problem can be fit exactly.

## 8. Assumptions and regime of validity

1. **The forward map is differentiable with a computable Jacobian.** If the
   Jacobian is only available by finite differences, the accuracy table of
   Section 3 applies to every iteration.
2. **The linearisation is used inside a region where it is valid.** The
   $\mathcal O(\|hp\|^2)$ measurement in Section 4 quantifies the error, but only
   *after* the step has been taken; a step-size control is needed to stay in the
   region.
3. **The data are finite and the Jacobian is not rank-deficient.** A rank-deficient
   $J_k$ makes the normal equations singular; the standard cure is damping, which
   changes the method (see [02](02-gradient-and-newton.md)).
4. **The parameters are scaled comparably.** Section 4's direction $p$ mixes
   amplitude and decay; with unscaled parameters the linearisation error is
   measured in whichever unit is largest, and the step is correspondingly
   unbalanced.
5. **The stopping rule is meaningful.** "No descent step" stopped the iteration in
   Section 5; that is a statement about the damping, not about convergence to a
   solution.
6. **Noise makes the exact-zero-residual theory inapplicable.** The measured
   linear rate on noisy data is the honest rate for real inversions.

## 9. The honest summary

- A nonlinear inverse problem is solved as a sequence of linear ones, and the
  linearisation error is $O(\|hp\|^2)$ — measured, not asserted.
- The Jacobian can be checked, and the check has an optimal step around
  $\epsilon^{1/3}$.
- On noisy data Gauss–Newton converges **linearly** to the noise floor; the
  quadratic rate belongs to zero-residual problems and is demonstrated separately.
- The basin of attraction is measurable; for this problem it was large, and the
  one observed failure was a flat region with a vanishing gradient, not a
  competing minimum.
- Reporting a nonlinear inversion requires the start, the linearisation used, the
  stopping rule and the residual; the model alone is not reproducible.

## 10. Python demonstration

`code/local_linearization_demo.py` prints: the synthetic problem; the analytic
Jacobian against central differences at seven step sizes; the linearisation
residual with its fitted order; the damped Gauss–Newton history on noisy data and
the exact-data history with measured convergence orders; and the basin-of-attraction
grid with the measured flat-region failure.

```bash
cd 18-inverse-problems/04-nonlinear-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python local_linearization_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, well under a second.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/01-local-linearization-exercises.md`](exercises/01-local-linearization-exercises.md)
and
[`exercises/01-local-linearization-solutions.md`](exercises/01-local-linearization-solutions.md).

- **★** Reproduce the one-step calculation of Section 7 for
  $t = (0,1)$, $d = (4.0, 2.0)$, $u_0 = (2.0,0.5)$.
- **★★** Derive the exact Hessian of $\tfrac12\|F(u)-d\|^2$ for this model and
  show that only the $\alpha\alpha$ entry differs from $J^{\mathsf T}J$.
- **★★★** Design a synthetic experiment that measures the basin boundary of a
  Gauss–Newton iteration in two parameters, and state how you would distinguish a
  boundary failure from a flat-region failure.

## 12. Mastery checkpoint

Complete this without notes:

> A colleague inverts $d(t) = Ae^{-\alpha t}$ with $0.5\%$ noise from
> $u_0 = (1.0,0.10)$ and reports that the iteration "converges quadratically in
> four iterations". **(a)** State what is wrong with that sentence, using the
> measured history. **(b)** The same code with synthetic noise-free data does
> converge quadratically; give the measured orders. **(c)** A second run from
> $(1000,1000)$ reports a model with objective $13.04$ and a gradient norm that
> the stopping rule accepted as zero. Explain why, and name the failure mode.
> **(d)** Write the four numbers you would require in a report before believing
> any of the three runs.

A worked version of (a)–(c) appears in
[`exercises/01-local-linearization-solutions.md`](exercises/01-local-linearization-solutions.md).

## 13. Common pitfalls

1. **Claiming quadratic convergence on noisy data.** The measured order is 1
   (linear) there; quadratic needs a zero residual.
2. **Trusting a hand-derived Jacobian.** The check costs one loop and exposes
   sign errors that otherwise masquerade as slow convergence.
3. **Choosing the difference step by taste.** Two decades away from the optimum
   costs four orders of magnitude in Jacobian accuracy.
4. **Assuming a large residual means a bad start.** It can also mean a local
   minimum or a flat region; the diagnostics differ.
5. **Stopping on a small step.** "No further descent" is a statement about the
   damping, and in the measured case the objective was still far from the truth.
6. **Forgetting that the model error plateaus with the objective.** At the noise
   floor, more iterations do not improve the model.

## 14. Where this is used

- **Traveltime and waveform tomography**, where the Jacobian is the ray or
  sensitivity kernel and each iteration solves a large linear system.
- **Potential-field depth inversion**, where the depth–density product makes the
  Jacobian nearly rank-deficient and damping essential.
- **Curve fitting and parameter estimation** in rock physics, where the model is
  a closed-form function of two or three parameters as in this lesson.
- **Machine learning.** Gradient descent on a non-convex loss is the same
  iteration without the Gauss–Newton structure; the local-versus-global question
  is identical; see
  [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/02-bias-variance.md).

## 15. Related modules

- [18-04-02 Gradient, Gauss-Newton and Full Newton Methods](02-gradient-and-newton.md) —
  the three step rules and their measured costs.
- [18-04-03 Conjugate Gradient and Large-Scale Inversion](03-conjugate-gradient-inverse.md) —
  what to do when $J^{\mathsf T}J$ is too large to form.
- [18-04-07 Convergence Diagnosis and Local-Minimum Traps](07-convergence-and-local-minima.md) —
  detecting the flat-region failure measured here.
- [18-03-07 Regularisation of Nonlinear Problems](../03-regularization/07-nonlinear-regularization.md) —
  the same iteration with a penalty added.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../../19-numerical-modeling-hpc/01-numerical-foundations/02-convergence-and-error.md) —
  how convergence orders are measured and reported.

## 16. Self-assessment checklist

- [ ] I can derive the Gauss–Newton step from the linearised normal equations.
- [ ] I can verify a Jacobian and choose the difference step.
- [ ] I can measure the order of the linearisation error.
- [ ] I can distinguish linear from quadratic convergence in a history.
- [ ] I can explain why noise removes the quadratic rate.
- [ ] I can name the four quantities required to reproduce a nonlinear inversion.
