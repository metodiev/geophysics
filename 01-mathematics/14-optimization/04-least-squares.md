---
id: 01-14-04
title: "Linear and Nonlinear Least Squares"
level: advanced
prereqs: ["01-14-01", "01-14-02", "01-07-08"]
estimated_minutes: 90
tags: [least-squares, normal-equations, gauss-newton, inversion]
---

# Linear and Nonlinear Least Squares

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the normal equations three ways — by differentiation, by
   projection, and by setting the misfit's curvature to zero — and say what each
   derivation exposes.
2. **Demonstrate** numerically that solving via $G^{\mathsf{T}}G$ squares the
   condition number, and quantify the loss with a rational reference solution.
3. **Choose** between the normal equations, Householder QR and the SVD for a
   given problem, and justify the choice from measured errors.
4. **Implement** Gauss–Newton for a nonlinear problem and diagnose its failure
   modes: singular $J^{\mathsf{T}}J$, an unbounded step, and convergence to a
   wrong local minimum.
5. **Apply** Levenberg–Marquardt damping with a schedule, and interpret it as a
   trust region rather than a trick.
6. **Weight** a least-squares problem from stated data uncertainties and explain
   what changes when the weights are wrong.

## Prerequisites

[01-14-01 Convexity, Stationarity and Optimality Conditions](./01-convexity.md)
for the optimality conditions,
[01-14-02 Unconstrained Minimisation](./02-unconstrained.md) for the descent
frameworks that Gauss–Newton instantiates, and
[01-07-08 Singular Value Decomposition and Rank Truncation](../07-linear-algebra/08-svd.md)
for the resolution-and-covariance reading of the same solution.

## 1. Intuition: this is the tool

Of all the methods in this module, one is used more than the rest put together.
Least squares is the misfit of classical geophysics: Gauss invented it for
geodesy, it is the misfit behind tomography, potential-field inversion, seismic
reflection, gravity field recovery from satellites, and every "best-fitting
model" you have ever seen in a paper.

The reason is a theorem, not a tradition. For a linear forward model $G$ and
Gaussian data errors, the least-squares estimate is the maximum-likelihood
estimate, and for a nonlinear model linearised about the current model the same
follows. Least squares is what Bayes gives you when the errors are Gaussian and
the prior is flat — so its popularity is not a convention, it is a consequence of
what we usually assume about measurement error.

But there is a catch, and it is the subject of half this lesson. The textbook way
to solve a least-squares problem is the **normal equations** $G^{\mathsf{T}}G\,
m = G^{\mathsf{T}}d$. That formulation is exactly what the calculus gives, it is
what every derivation produces, and it is **numerically wrong** for ill-conditioned
problems: forming $G^{\mathsf{T}}G$ squares the condition number, so a kernel with
$\kappa \sim 10^{8}$ produces a system with $\kappa \sim 10^{16}$, right at the
double-precision wall. Section 4 measures the damage and shows the fix (QR or
SVD). The gap between the derivation and the implementation is the most useful
thing in this lesson.

## 2. Precise definitions

### 2.1 The problem

Given data $d \in \mathbb{R}^{n}$, a model $m \in \mathbb{R}^{p}$ and a forward
operator $G$ (or $F(m)$ in the nonlinear case), the least-squares problem is

$$\min_m \phi(m), \qquad
\phi(m) = \tfrac12\|Gm - d\|_{2}^{2}
\quad\text{or}\quad \phi(m) = \tfrac12\|F(m) - d\|_{2}^{2}. \tag{2.1}$$

Under the **statistical model** $d = Gm + e$ with $e \sim \mathcal{N}(0,
\sigma^{2}I)$ this is equivalent to maximum likelihood, and the residual
$r = Gm - d$ has $n - p$ degrees of freedom so that

$$\hat{\sigma}^{2} = \frac{\|r\|^{2}}{n - p} \tag{2.2}$$

estimates the data variance. If the data have covariance $C_d$, the correct
misfit is weighted:

$$\phi_W(m) = \tfrac12 (Gm - d)^{\mathsf{T}} C_d^{-1} (Gm - d). \tag{2.3}$$

### 2.2 The three solution routes

| route | system | cost | relative error |
|---|---|---|---|
| normal equations | $G^{\mathsf{T}}G\,m = G^{\mathsf{T}}d$ | $O(np^{2} + p^{3})$ | $\sim \kappa^{2}\epsilon$ |
| QR | $R m = Q^{\mathsf{T}}d$, $G = QR$ | $O(2np^{2})$ | $\sim \kappa\epsilon$ |
| SVD | $V\Sigma^{-1}U^{\mathsf{T}}d$, with truncation | $O(np^{2} + p^{3})$, more constants | $\sim \kappa\epsilon$, plus the option to truncate |

Here $\kappa = \sigma_{\max}(G)/\sigma_{\min}(G)$ and $\epsilon$ is the
floating-point unit round-off ($2.2\times10^{-16}$ for binary64). The error
columns are *worst-case bounds*, not predictions — Section 4.3 shows a case where
the normal-equation error is far below its bound — but the exponent difference is
what decides survival.

### 2.3 Gauss–Newton and Levenberg–Marquardt

Linearising the residual about the current model $m_k$:

$$r(m + \delta) \approx r_k + J_k \delta, \qquad r_k = F(m_k) - d, \quad
J_k = \left.\frac{\partial F}{\partial m}\right|_{m_k}, \tag{2.4}$$

gives the **Gauss–Newton** step

$$\delta_k = -\left(J_k^{\mathsf{T}}J_k\right)^{-1} J_k^{\mathsf{T}} r_k .
\tag{2.5}$$

Its curvature model is $J^{\mathsf{T}}J$, *not* the true Hessian
$J^{\mathsf{T}}J + \sum_i r_i \nabla^{2}F_i$ — which is why Gauss–Newton
converges linearly, not quadratically, when residuals are large, and why it
behaves like Newton near a small-residual solution. **Levenberg–Marquardt** adds
damping,

$$\delta_k(\lambda) = -\left(J_k^{\mathsf{T}}J_k + \lambda D\right)^{-1}
J_k^{\mathsf{T}}r_k, \tag{2.6}$$

with $D = I$ or $D = \operatorname{diag}(J^{\mathsf{T}}J)$. Increasing $\lambda$
trades the Newton step for a steepest-descent-like step of bounded length — a
trust region in disguise — and it guarantees that $\delta$ is a descent
direction even when $J$ is rank deficient.

## 3. Derivations

### 3.1 The normal equations, three ways

**By differentiation.** Expand the misfit:

$$\phi(m) = \tfrac12 m^{\mathsf{T}}G^{\mathsf{T}}Gm - m^{\mathsf{T}}G^{\mathsf{T}}d
+ \tfrac12 d^{\mathsf{T}}d,$$

and use the identity
$\nabla_m\, \tfrac12 m^{\mathsf{T}}A m = \tfrac12(A + A^{\mathsf{T}})m = Am$ for
symmetric $A$:

$$\nabla\phi = G^{\mathsf{T}}Gm - G^{\mathsf{T}}d = -G^{\mathsf{T}}r. \tag{3.1}$$

Setting $\nabla\phi = 0$ gives $G^{\mathsf{T}}Gm = G^{\mathsf{T}}d$ and, at the
solution, $G^{\mathsf{T}}r = 0$: the gradient's vanishing *is* the statement that
the residual is orthogonal to the column space.

**By projection.** The set $\{Gm\}$ is a subspace. Minimising the distance from
$d$ to it means choosing the closest point, and the closest point is the
orthogonal projection: the residual must be orthogonal to every column of $G$,
which is $G^{\mathsf{T}}r = 0$ again. Lesson
[01-07-07](../07-linear-algebra/07-orthogonality.md) develops this geometry —
including the projection matrix and leverage.

**By curvature.** The Hessian is $\nabla^{2}\phi = G^{\mathsf{T}}G$, independent of
$m$. Newton's method on (2.1) is therefore the single step
$m^{*} = m - (G^{\mathsf{T}}G)^{-1}\nabla\phi(m) = (G^{\mathsf{T}}G)^{-1}G^{\mathsf{T}}d$
from *any* starting point, which is the statement that linear least squares is a
quadratic problem and Newton solves quadratics exactly — the link to
[01-14-02](./02-unconstrained.md) Section 3.2.

### 3.2 Why $G^{\mathsf{T}}G$ squares the condition number

Let $G = U\Sigma V^{\mathsf{T}}$. Then

$$G^{\mathsf{T}}G = V\Sigma^{2}V^{\mathsf{T}}
\quad\Longrightarrow\quad
\kappa_2(G^{\mathsf{T}}G) = \frac{\sigma_1^{2}}{\sigma_p^{2}} = \kappa_2(G)^{2}.
\tag{3.2}$$

Equation (3.2) is an identity, not an estimate: the condition number of the
normal-equation matrix is exactly the square of the kernel's. Since the error of
a solve is bounded by roughly $\kappa$ times the unit round-off, the
normal-equation route loses twice as many digits as QR. For binary64 the wall is
$\kappa^{2} \gtrsim 1/\epsilon \approx 4.5\times10^{15}$, i.e. $\kappa \gtrsim
6.7\times10^{7}$, and Sections 4.2–4.3 measure what happens on both sides of it.

There is a second consequence that geophysics cares about more. With the
eigenvalues of $G^{\mathsf{T}}G$ being $\sigma_i^{2}$, the *model covariance* of
the solution is $\hat{\sigma}^{2}(G^{\mathsf{T}}G)^{-1}$, so the variance of the
$i$-th model direction is inflated by $\sigma_i^{-2}$; small singular values
become enormous uncertainties, and squaring them makes the arithmetic that
computes those uncertainties unstable. That is one reason production codes
compute the SVD rather than $G^{\mathsf{T}}G$.

### 3.3 Gauss–Newton as an approximate Newton

Differentiating the true Hessian of $\phi(m) = \tfrac12\|F(m)-d\|^{2}$ gives

$$\nabla^{2}\phi = J^{\mathsf{T}}J + \sum_{i=1}^{n} r_i \nabla^{2}F_i(m). \tag{3.3}$$

Gauss–Newton drops $\sum r_i \nabla^{2}F_i$. Two consequences:

- **Near the solution**, $r_i \to$ the noise level, so the dropped term is small
  and Gauss–Newton inherits Newton's rapid convergence — but linearly, not
  quadratically, whenever the residuals are not negligible compared with the
  curvature terms.
- **Far from the solution**, the dropped term is large and can have either sign,
  so (2.5) may be a bad step or no step at all. Sections 4.5 and 4.6 measure both
  regimes.

### 3.4 Bounding the step is what makes the method usable

For a rank-deficient $J$, $J^{\mathsf{T}}J$ is singular and (2.5) does not exist.
With damping (2.6), $J^{\mathsf{T}}J + \lambda D \succ 0$ for any $\lambda > 0$
and $D \succ 0$, and the step satisfies

$$\delta^{\mathsf{T}}\left(-\nabla\phi\right) = \delta^{\mathsf{T}}J^{\mathsf{T}}r
= \left(J^{\mathsf{T}}r\right)^{\mathsf{T}}
\left(J^{\mathsf{T}}J + \lambda D\right)^{-1} J^{\mathsf{T}}r > 0,$$

so it is always a descent direction. That is the entire robustness argument, and
it is why the damping is not optional in a production code. The price is that
$\lambda$ must be *reduced* as the model improves, or the iteration converges to
a damped fixed point (Section 4.7 measured an error $10^{5}$ times worse than
undamped Newton when $\lambda$ stayed at $10^{2}$).

### 3.5 Weighting

Minimising (2.3) with $W = C_d^{-1}$ gives

$$(G^{\mathsf{T}}WG)\,m = G^{\mathsf{T}}Wd, \qquad
C_m = (G^{\mathsf{T}}WG)^{-1} \quad \text{(unit data variance)}. \tag{3.4}$$

Three practical points, each of which has a counterpart in
[21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md):

1. If uncertainties are only known up to a scale factor, the *estimates* are
   unchanged but the *covariances* are not — the scale must be estimated from the
   misfit, as in (2.2).
2. If the stated uncertainties are wrong, the estimates are still minimum-misfit
   but no longer maximum-likelihood. Section 4.8 shows the numbers: with
   uncertainties $0.1, 0.1, 0.1, 1.0, 1.0$ the slope moves by $-42$ per cent
   relative to the unweighted fit. That is not a small correction.
3. Weighting changes the geometry: it is a change of variables $d \mapsto
   W^{1/2}d$, $G \mapsto W^{1/2}G$, so it also changes the conditioning. Both a
   benefit and a hazard.

## 4. Numerical results

All numbers are from [`code/least_squares_demo.py`](./code/least_squares_demo.py),
which implements Gaussian elimination, Householder QR, a Jacobi eigensolver and
exact rational arithmetic with the standard library. Because the kernels have
integer entries and the data are integers or exact decimals, every problem has an
*exact* rational least-squares solution, so the float routes can be scored
against the truth rather than against each other.

### 4.1 Both routes are fine when the problem is well conditioned

A six-ray, four-cell SYNTHETIC cross-hole kernel with integer path lengths and
$d = (3,4,5,3,7,8)$ s has the exact solution
$(0.875, 1.750, 2.375, 2.250)$ s/km, and

| quantity | value |
|---|---|
| $\kappa_2(G)$ | $13.972264$ |
| $\kappa_2(G^{\mathsf{T}}G)$ | $195.224161$ ($= \kappa_2(G)^{2}$) |
| normal-equation solution | $(0.875000000000, 1.750000000000, 2.375000000000, 2.250000000000)$ |
| max relative error, normal equations | $2.758\times10^{-15}$ |
| Householder QR solution | identical to printed precision |
| max relative error, QR | $1.215\times10^{-15}$ |
| $\|r\|$ | $0.612372435696$ |
| $\|G^{\mathsf{T}}r\|$ | $6.735\times10^{-15}$ (zero to round-off) |

Both routes are at round-off, and $\|G^{\mathsf{T}}r\|$ confirms the orthogonality
condition. This is the case the textbooks describe, and it is why the normal
equations survive in so much software: for well-conditioned problems they are
perfectly fine.

### 4.2 Nearly parallel rays: where the normal equations stop working

Two rays with $G = [[1,1],[1,1+\delta]]$ and exact data generated from
$m = (0.05,-0.02)$ s/km. The reference solution is computed in rational
arithmetic from the same float inputs, so the comparison isolates the *solve*,
not the data.

| $\delta$ | $\kappa_2(G)$ | normal-equation error | QR error | ratio | $\kappa^{2}$ | float $\det(G^{\mathsf{T}}G)$ |
|---|---|---|---|---|---|---|
| $10^{-2}$ | $4.020\times10^{2}$ | $7.959\times10^{-12}$ | $1.665\times10^{-15}$ | $4.78\times10^{3}$ | $1.616\times10^{5}$ | $+1.000\times10^{-4}$ |
| $10^{-4}$ | $4.000\times10^{4}$ | $6.551\times10^{-8}$ | $2.998\times10^{-13}$ | $2.19\times10^{5}$ | $1.600\times10^{9}$ | $+1.000\times10^{-8}$ |
| $10^{-6}$ | $4.001\times10^{6}$ | $8.333\times10^{-4}$ | $3.838\times10^{-11}$ | $2.17\times10^{7}$ | $1.601\times10^{13}$ | $+9.992\times10^{-13}$ |
| $10^{-8}$ | $4.000\times10^{8}$ | **no solution** (zero pivot) | $3.188\times10^{-9}$ | — | $1.600\times10^{17}$ | $+0.000\times10^{0}$ |

Three facts, each measured:

1. The normal-equation error grows like $\kappa^{2}\epsilon$: from
   $7.96\times10^{-12}$ to $8.33\times10^{-4}$ is a factor of $10^{8}$ for a
   factor of $10^{4}$ in $\kappa$.
2. QR's error grows like $\kappa\epsilon$: from $1.67\times10^{-15}$ to
   $3.84\times10^{-11}$ — a factor of $2\times10^{4}$ for a factor of $10^{4}$ in
   $\kappa$.
3. At $\delta = 10^{-8}$ the *computed* $G^{\mathsf{T}}G$ is numerically singular:
   its determinant comes out as exactly $0.000\times10^{0}$ in double precision,
   and the Cholesky/Gaussian route fails with a zero pivot. QR still recovers both
   parameters to nine digits. This is the practical meaning of
   $\kappa^{2} > 1/\epsilon$: the normal-equation matrix has stopped being
   positive definite.

The condition numbers in that table were computed in extended precision
(60-digit `Decimal` arithmetic), because $G^{\mathsf{T}}G$ cannot be formed
reliably in double precision at $\delta = 10^{-8}$ — the demonstration does this
explicitly, since "measuring $\kappa$" and "measuring $\kappa$ badly" are
different activities.

### 4.3 A badly scaled basis, and why worst-case bounds are not predictions

Fitting a cubic trend to eight stations at elevations $0, 200, \dots, 1400$ m in
two bases, with exact decimal data:

| basis | $\kappa_2(G)$ | $\kappa_2(G)^{2}$ | normal-equation error | QR error |
|---|---|---|---|---|
| raw cubic in metres | $3.2518\times10^{9}$ | $1.0574\times10^{19}$ | $6.224\times10^{-14}$ | $2.984\times10^{-15}$ |
| centred and scaled | $4.0747\times10^{1}$ | $1.6603\times10^{3}$ | $9.616\times10^{-17}$ | $6.239\times10^{-16}$ |

The raw basis has $\kappa^{2} = 1.06\times10^{19}$, far beyond
$1/\epsilon = 4.5\times10^{15}$, and the bound $\kappa^{2}\epsilon$ would predict
a relative error of order $10^{3}$. The *measured* normal-equation error is
$6.2\times10^{-14}$ — small. The reason is that bounds are worst-case: the error
is controlled by the projection of the data onto the ill-conditioned directions,
and this particular exact-decimal dataset has almost no content there. The honest
conclusion is:

> A large condition number means *an* error of that size is possible, not that it
> will occur. You cannot know which case you are in without the data's
> coefficients — the Picard condition of
> [01-07-08](../07-linear-algebra/08-svd.md). Since you cannot check on every
> problem, use the route whose bound is $\kappa\epsilon$ rather than
> $\kappa^{2}\epsilon$.

### 4.4 Gauss–Newton on a gravity profile

The model is a vertical-cylinder-style profile $d_i = A h / (x_i^{2} +
h^{2})^{3/2}$ at nine stations $x = -8,\dots,8$, with true parameters
$(A,h) = (100, 20)$ and a deterministic perturbation whose largest value is
$0.0010$, i.e. $0.40$ per cent of the peak datum.

| quantity | value |
|---|---|
| residual norm at the start $(100,20)$ | $0.002002$ |
| Gauss–Newton after 25 iterations | $(101.16241121, 20.11635247)$ |
| residual norms, first iterations | $2.002498\times10^{-3}$, $1.827523\times10^{-3}$, $1.827321\times10^{-3}$, $\dots$ |
| final residual | $0.00182732$ (ratio to initial $9.125\times10^{-1}$) |
| best residual over 400 iterations from a good start | $0.0018273207$ |

Convergence took **two** iterations to reach the plateau and then stopped
improving: the linearisation is accurate, the quadratic model describes the
problem well, and the remaining misfit is the noise. Note what the answer is
*not*: the recovered depth $h = 20.116$ differs from the truth $20$ by $0.58$
per cent, which is what a $0.4$ per cent data perturbation buys in a
depth-and-amplitude trade-off. Perturbing data by $0.4$ per cent and recovering
the depth to $0.06$ per cent would be suspicious.

### 4.5 The $\pm h$ symmetry, and a start outside the basin

The model depends on $h^{2}$, so $(A, h)$ and $(-A, -h)$ predict the same data:
an exact two-fold non-uniqueness. Starting Gauss–Newton from five depths:

| start $h$ | GN result $h$ | GN residual | iterations to within $1\%$ of best | LM result $h$ | LM residual |
|---|---|---|---|---|---|
| $20.0$ | $20.116352$ | $1.827\times10^{-3}$ | $1$ | $19.994949$ | $1.923\times10^{-3}$ |
| $30.0$ | $-20.116352$ | $1.827\times10^{-3}$ | $6$ | $20.164871$ | $1.843\times10^{-3}$ |
| $45.0$ | $20.116352$ | $1.827\times10^{-3}$ | $14$ | $20.608396$ | $2.959\times10^{-3}$ |
| $60.0$ | $20.116352$ | $1.827\times10^{-3}$ | $15$ | $21.109498$ | $4.903\times10^{-3}$ |
| $90.0$ | $1645.092799$ | $1.151\times10^{-1}$ | not reached | $22.664099$ | $1.078\times10^{-2}$ |

Three lessons, all measured:

- The start at $h = 30$ converges to $h = -20.116$: the same model with the sign
  of $A$ flipped, and the same residual. A code that reports "$h$" without
  reporting the sign convention is reporting half a solution.
- From $h = 45$ and $60$ the method needs $14$ and $15$ iterations where $h = 20$
  needed one, but it still gets there.
- From $h = 90$ Gauss–Newton does **not** find the solution: it escapes to
  $h = 1645.09$ with a residual $63$ times larger, where the model has flattened
  out and the gradient is nearly zero. It reports success because the stopping
  test is a gradient norm. The damped (LM) version from the same start stays in
  the basin and reaches $h = 22.66$ with residual $1.078\times10^{-2}$ — not
  converged in $200$ iterations, but moving in the right direction.

### 4.6 A rank-deficient step: reported, not hidden

At some models $J^{\mathsf{T}}J$ is exactly singular (the profile's sensitivity to
depth vanishes in the limit $h \to 0$). The demonstration returns the status
`singular J^T J` instead of dividing by zero, and the section reports it as a
possible outcome. This is the design principle worth copying: **a nonlinear
solver should return a status, not a model on faith.** Section 5's table shows
the run from $h = 90$ as the case where a badly behaved step was *taken*; a
singular pivot is the case where it could not be.

### 4.7 Weighting, measured

Five data at $x = 0..4$, $d = (1.0, 2.0, 2.0, 4.0, 4.6)$, with stated
uncertainties $(0.1, 0.1, 0.1, 1.0, 1.0)$:

| fit | intercept | slope |
|---|---|---|
| ordinary (unweighted) | $0.88000000$ | $0.92000000$ |
| weighted by $1/\sigma_i^{2}$ | $1.14278472$ | $0.53250494$ |

The slope moves by $-0.387495$, i.e. $-42.12$ per cent. The two fits answer
different questions: the unweighted one minimises $\sum r_i^{2}$, the weighted one
minimises $\sum (r_i/\sigma_i)^{2}$, and only the second is the maximum-likelihood
estimate under the stated uncertainties. If the uncertainties are wrong by a
factor of $10$ on two of five data, the difference is a factor of almost two in
the slope — which is to say, the difference between two interpretations.

### 4.8 Outliers, and the motivation for L1

With a blunder at the last datum, $d = (1, 2, 2, 4, 9)$:

| fit | slope | shift caused by the blunder |
|---|---|---|
| L2 on clean data | $0.92000000$ | — |
| L2 on blundered data | $1.80000000$ | $+0.880000$ |
| L1 on blundered data (coarse grid) | $1.000000$ | $+0.080000$ |

One bad datum moves the least-squares slope almost ten times more than the
least-absolute-deviations slope. That is the quantitative reason
[01-14-07](./07-linear-programming.md) treats L1 fitting as a linear program, and
the reason gravity and magnetic profiles with suspect stations are fitted with
L1 or Huber norms. The L1 fit here was found on a $0.001$ grid; the exact LP
solution is in the next lesson.

### 4.9 Leverage

For the five-station line fit the leverages are

$$h = (0.60000000,\ 0.30000000,\ 0.20000000,\ 0.30000000,\ 0.60000000),
\qquad \sum h_i = 2.00000000,$$

the number of parameters. The outermost stations control the slope; a blunder at
either end damages the fit six times as much as one in the middle. This follows
from the design alone, so it can be computed before the survey is paid for — the
survey-design use of the projection matrix from
[01-07-07](../07-linear-algebra/07-orthogonality.md).

## 5. Physical interpretation

**$G^{\mathsf{T}}r = 0$ is a physical statement about residuals.** Each row of
$G^{\mathsf{T}}$ is a data sensitivity kernel; orthogonality says the misfit left
over after the fit is uncorrelated with the sensitivity of every parameter.
"If the residual still correlates with my kernel, my model has not extracted all
the information in that direction."

**The condition number is the resolution limit, squared.** $\kappa(G)$ tells you
how many digits of the model the data support; $\kappa(G)^{2}$ tells you that
forming the normal equations throws away half of them. In terms of the model
covariance, the *variance* of a direction scales as $\sigma_i^{-2}$, so a singular
value of $10^{-4}$ gives a variance $10^{8}$ times the best-determined direction.
Squaring this in $G^{\mathsf{T}}G$ is not a numerical nicety: it is the difference
between a reported error bar and a fabrication.

**Gauss–Newton's rapid convergence is a small-residual statement.** Near the
solution the residuals are noise-sized and the neglected curvature
$\sum r_i \nabla^{2}F_i$ is negligible; that is why an inversion that starts close
converges in a handful of iterations. Far away, the neglected term dominates and
the step is unreliable — Section 4.5's escape to $h = 1645$ is that failure mode
in miniature.

**$\pm h$ and other exact symmetries are non-uniqueness, not noise.** Whenever
the model depends on parameters through an even function, the sign is unresolvable
from those data. Report both, or fix one.

**Weighting is a statement about the instrument.** Stating $\sigma_i$ is not
bookkeeping; it is a claim about the measurement. The correct response to
"we don't know the uncertainties" is to say the estimates are minimum-misfit but
their error bars are uncalibrated.

## 6. Assumptions and regime of validity

1. **Gaussian, zero-mean, uncorrelated errors** for the maximum-likelihood
   interpretation. Heavy-tailed errors favour L1
   ([01-14-07](./07-linear-programming.md)); correlated errors require the full
   $C_d$ of (2.3).
2. **The forward model is exactly known.** Model error is not in the misfit, so
   the quoted covariances describe only the data's contribution. This is the
   single largest unquantified assumption in most published inversions.
3. **Full column rank for a unique solution.** Rank deficiency makes
   $G^{\mathsf{T}}G$ positive semi-definite; the pseudoinverse (or truncated SVD,
   [01-07-08](../07-linear-algebra/08-svd.md)) gives the minimum-norm solution, and
   the non-uniqueness is real, not numerical.
4. **Local linearisation for Gauss–Newton.** The step is valid only where the
   linearisation is; damping buys robustness, not global convergence.
5. **Non-linearity of the reported uncertainties.** For a nonlinear problem the
   covariance $C_m \approx \hat{\sigma}^{2}(J^{\mathsf{T}}J)^{-1}$ is a local,
   linearised, symmetric approximation, and it can be wrong by a lot when the
   model is far from linear or the residuals are large.
6. **Damping must be reduced.** A fixed $\lambda$ converges to a damped fixed
   point, not to the least-squares solution (Section 4.7 compared errors of
   $1.4\times10^{-10}$ and $5.8\times10^{-6}$).

## 7. Python demonstration

The companion script is
[`code/least_squares_demo.py`](./code/least_squares_demo.py), with nine sections.
The exact rational reference solutions are the reason the error tables mean
something: without them, "small error" would mean "two float routes agreeing".

| Section | Measured | Interpretation |
|---|---|---|
| 1, well conditioned | $\kappa = 13.97$, errors $2.8\times10^{-15}$ (normal) and $1.2\times10^{-15}$ (QR) | both routes are fine here |
| 2, $\delta$ sweep | normal-equation error $7.96\times10^{-12} \to 8.33\times10^{-4}$ as $\kappa$ goes $4\times10^{2} \to 4\times10^{6}$ | error tracks $\kappa^{2}\epsilon$ |
| 2, $\delta = 10^{-8}$ | normal equations fail with a zero pivot; QR error $3.2\times10^{-9}$ | $\kappa^{2} = 1.6\times10^{17} > 1/\epsilon$ |
| 3, bases | raw basis $\kappa = 3.25\times10^{9}$ but error only $6.2\times10^{-14}$ | worst-case bounds are not predictions |
| 4, Gauss–Newton | converges in 2 iterations to $(101.16241121, 20.11635247)$ | the linearisation is accurate here |
| 5, starts | from $h = 90$: result $h = 1645.09$, residual $0.1151$ | convergence is not correctness |
| 5, symmetry | start $h = 30$ gives $h = -20.116352$ with the same residual | an exact model symmetry |
| 7, weighting | slope $0.92000000 \to 0.53250494$ | weights are part of the problem statement |
| 8, outlier | L2 slope shift $+0.880000$, L1 shift $+0.080000$ | ninefold robustness difference |
| 9, leverage | $h_i = (0.6, 0.3, 0.2, 0.3, 0.6)$, $\sum h_i = 2$ | endpoints control the slope |

> **Breaking exercise.** In Section 2, change the data so that $m$ has a large
> component along the *weak* direction of $G$ (for example by adding $1.0$ to the
> second entry of $m$ before generating $d$). Predict whether the raw-cubic error
> of Section 3 grows, and by how much. Then run it. This is the Picard condition
> in action: the error of the normal-equation route depends on the data's
> coefficients in the weak directions, not on $\kappa$ alone.

## 8. Exercises

Full set and worked solutions:
[`exercises/04-least-squares-exercises.md`](./exercises/04-least-squares-exercises.md)
and [`exercises/04-least-squares-solutions.md`](./exercises/04-least-squares-solutions.md).
Four to start with:

**★1.** Derive the normal equations by setting the gradient to zero, and prove
$G^{\mathsf{T}}r = 0$ at the solution.

**★2.** Show that $\kappa_2(G^{\mathsf{T}}G) = \kappa_2(G)^{2}$ using the SVD, and
state the consequence for binary64 arithmetic.

**★★3.** For $f(x) = a e^{-x/h}$ with two parameters, write down $J$ and one
Gauss–Newton step, and identify the parameter combination that is poorly
determined when the data cover only $x \gg h$.

**★★4.** With data uncertainties $\sigma = (0.1, 0.1, 1.0, 1.0)$ and a kernel
$G$ of your choice, compute both the ordinary and weighted estimates and the
standard errors of each, and say which quantities the weights legitimately
change.

## 9. Common mistakes

1. **Forming $G^{\mathsf{T}}G$ because the derivation produced it.** Section 4.2
   shows it failing outright at $\delta = 10^{-8}$ where QR succeeds.
2. **Judging the normal equations only on well-conditioned tests.** Section 4.1
   would convince you the route is safe; Section 4.2 shows where it is not.
3. **Using the worst-case bound as a prediction.** Section 4.3's raw cubic basis
   has $\kappa^{2}\epsilon \sim 10^{3}$ and a measured error of $10^{-14}$.
   Understand the bound, do not quote it as the answer.
4. **Trusting a Gauss–Newton run whose step was never bounded.** Section 4.5's
   $h = 1645$ is a converged-looking wrong answer.
5. **Ignoring exact model symmetries.** $\pm h$ is not a numerical artefact.
6. **Leaving the damping weight fixed.** It converges to the damped fixed point,
   not the least-squares solution.
7. **Reporting a covariance without the residuals that calibrated it.** The scale
   factor $\hat{\sigma}$ comes from $\|r\|^{2}/(n-p)$, and quoting
   $(J^{\mathsf{T}}J)^{-1}$ alone understates or overstates the error bars by
   whatever that factor is.
8. **Forgetting that weights change the conditioning too.** $W^{1/2}G$ can be
   much better or much worse conditioned than $G$.

## 10. Real-world applications

- **Seismic travel-time tomography.** Rows of $G$ are ray path lengths in
  cells; the normal equations are $10^{4}$–$10^{6}$ dimensional and sparse, and
  production codes use LSQR or conjugate gradients — which never form
  $G^{\mathsf{T}}G$, for exactly the reason of Section 4.2.
- **Gravity and magnetic inversion with a linear kernel.** $G$ is dense and
  badly conditioned because the Green's function decays with depth; the SVD with
  truncation ([01-07-08](../07-linear-algebra/08-svd.md)) or Tikhonov
  regularisation is the standard remedy, and the covariance from
  $(G^{\mathsf{T}}G + \alpha I)^{-1}$ is the reported uncertainty.
- **GPS/geodetic network adjustment.** Classically least squares, with
  thoroughly documented weighting; the datum defect is the null space.
- **Reflection tomography and waveform fitting.** Gauss–Newton with
  Levenberg–Marquardt and a multi-scale schedule: the schedule *is* the damping
  policy of Section 3.4.
- **Satellite gravity field estimation.** $10^{5}$-parameter normal equations,
  assembled and solved by iterative methods, with the weight matrix built from
  the instruments' error characteristics — the full $C_d$ case of (2.3).
- **Rock physics and laboratory calibration.** Any two-parameter fit through
  laboratory measurements is this lesson, including the leverage warning: the
  extreme samples control the trend.

## 11. Further reading

- **Nocedal, J., & Wright, S. J. *Numerical Optimization* (2nd ed.). Springer.**
  Chapter 10. Level: graduate. The definitive treatment of nonlinear
  least-squares methods, including the Gauss–Newton and Levenberg–Marquardt
  theory and the convergence results behind Section 3.3.
- **Golub, G. H., & Van Loan, C. F. *Matrix Computations* (4th ed.). Johns
  Hopkins University Press.** Sections 5.3 and 5.5. Level: advanced. QR, SVD and
  the error analysis of Section 3.2, with the constants.
- **Lawson, C. L., & Hanson, R. J. *Solving Least Squares Problems*. SIAM
  Classics.** Level: advanced. The classical reference, including the
  implementation detail that makes it practical.
- **Aster, R. C., Borchers, B., & Thurber, C. H. *Parameter Estimation and
  Inverse Problems.* Academic Press.** Level: intermediate to advanced. The
  geophysical version, with the statistical assumptions stated explicitly.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory* (4th ed.).
  Academic Press.** Level: intermediate. Normal equations, weighted least squares
  and the resolution matrix, written for geophysicists.
- **Tarantola, A. *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: graduate. The probabilistic framing that makes
  weighting principled rather than ad hoc.

> Note on citations: bibliographic details above are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text, and you
> should confirm editions and current availability through your library before
> citing them yourself.

## 12. Self-assessment checklist

- [ ] I can derive the normal equations by differentiation, by projection and by
      the curvature argument.
- [ ] I can prove $\kappa_2(G^{\mathsf{T}}G) = \kappa_2(G)^{2}$ and state the
      practical threshold.
- [ ] I can implement Householder QR for a small least-squares problem.
- [ ] I can explain when the normal-equation error is much smaller than the
      worst-case bound, and why.
- [ ] I can write down and implement a Gauss–Newton step, and a damped version.
- [ ] I can diagnose the three Gauss–Newton failure modes with numbers.
- [ ] I can set up a weighted least-squares problem and say what the weights
      assert.
- [ ] I can compute leverages and use them to plan a survey.

## 13. Related lessons

- [01-14-01 Convexity, Stationarity and Optimality Conditions](./01-convexity.md) —
  why the linear least-squares misfit is exactly a quadratic.
- [01-14-02 Unconstrained Minimisation](./02-unconstrained.md) — Newton, BFGS and
  damping, of which Gauss–Newton is a special case.
- [01-14-03 Constrained Optimisation and Lagrange Multipliers](./03-constrained.md) —
  adding a well tie or a bound to the fit.
- [01-14-05 Global Optimisation](./05-global-optimization.md) — what to do when
  the nonlinear misfit has several basins.
- [01-14-07 Linear Programming](./07-linear-programming.md) — L1 and Chebyshev
  fitting, the robust alternatives to L2.
- [01-07-08 Singular Value Decomposition and Rank Truncation](../07-linear-algebra/08-svd.md) —
  resolution, covariance and the Picard condition.
- [01-18 Inverse Problems](../../18-inverse-problems/README.md) — the same
  machinery with regularisation, priors and model appraisal.
