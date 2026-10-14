---
id: 01-16-06
title: "Tikhonov Regularisation and the L-Curve"
level: graduate
prereqs: ["01-16-05", "01-14-04"]
estimated_minutes: 90
tags: [tikhonov-regularisation, l-curve, regularization-parameter, ridge-regression, inverse-problems]
---

# Tikhonov Regularisation and the L-Curve

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Tikhonov estimator $m_\alpha = (F^{\mathsf T}F +
   \alpha I)^{-1}F^{\mathsf T}d$ from the penalised misfit, from the normal
   equations, and from the augmented least-squares system.
2. **Write** the estimator in the singular-value basis, identify the filter
   factors $\lambda_k^2/(\lambda_k^2+\alpha)$, and explain the two limits
   $\alpha\to0$ and $\alpha\to\infty$ in terms of bias and variance.
3. **Interpret** $\alpha$ as a ratio of noise variance to prior variance, and
   therefore as a statement of belief rather than a numerical knob.
4. **Compute** the L-curve, locate its corner by the curvature of the log-log
   plot, and state precisely what the corner does and does not optimise.
5. **Compute** the discrepancy principle's $\alpha$, compare it with the
   generalised cross-validation choice and with the L-curve corner, and say which
   assumptions each rule needs.
6. **Quantify** the sensitivity of the recovered model to the choice of $\alpha$
   and state the range over which the answer is defensible.
7. **Explain** why regularisation is a statement of prior information, with the
   Bayesian reading of $\alpha$ as the ratio of the two variances.

## Prerequisites

- [01-16-05 Ill-Posedness in the Sense of Hadamard](./05-ill-posedness.md) —
  the failures this lesson repairs, and the truncation experiment that is the
  crude version of the filter derived here.
- [01-14-04 Linear and Nonlinear Least Squares](../14-optimization/04-least-squares.md)
  — the normal equations, the residual and the Jacobian, and the geometric picture
  of least squares.
- [01-16-04 Spectral Theory of Operators and Eigenfunction Bases](./04-spectral-theory.md)
  — the resolution matrix $R_\alpha$ and its trace as the effective number of
  resolved parameters.

## 1. What regularisation is

The unregularised least-squares solution of a first-kind problem is dominated by
the small singular values: lesson 01-16-05 measured an amplification of
$2.4\times10^4$ and a model error of 235 per cent for 0.01 per cent data noise.
No algorithm can repair that, because the information is not in the data. What an
algorithm *can* do is add information that is not in the data and make the
trade-off explicit. That is regularisation, and it has two distinct jobs:

- **Uniqueness.** Adding a penalty makes the functional strictly convex, so the
  minimiser exists and is unique even when $F^{\mathsf T}F$ is singular. The
  penalty is the mathematical form of a prior belief.
- **Stability.** The penalty bounds the amplification of the small singular
  values, converting an unbounded inverse into a Lipschitz map with an explicit
  constant — at the cost of a bias that is also explicit.

Both are needed, and both are quantified below. The essential point is that
regularisation does not recover information; it chooses one member of an
equivalence class and states which one.

## 2. Derivation

### 2.1 The penalised functional

Minimise

$$J_\alpha(m) = \lVert Fm - d\rVert_2^2 + \alpha\lVert m\rVert_2^2 ,
\qquad \alpha > 0. \tag{1}$$

Expanding and differentiating with respect to $m$:

$$\nabla J_\alpha = 2F^{\mathsf T}(Fm - d) + 2\alpha m = 0
\ \Longrightarrow\
(F^{\mathsf T}F + \alpha I)m = F^{\mathsf T}d ,$$

so

$$\boxed{\ m_\alpha = (F^{\mathsf T}F + \alpha I)^{-1}F^{\mathsf T}d\ } \tag{2}$$

The matrix $F^{\mathsf T}F + \alpha I$ is symmetric positive definite for any
$\alpha > 0$, with eigenvalues $\lambda_k + \alpha \ge \alpha$ in the eigenbasis of
$F^{\mathsf T}F$. **The minimum eigenvalue is bounded below by $\alpha$, so the
inverse is bounded by $1/\alpha$: this single observation is the whole stability
argument.**

### 2.2 The augmented-system form

Equation (1) is also the ordinary least-squares problem

$$\min_m \left\lVert \begin{pmatrix} F \\ \sqrt{\alpha}\,I\end{pmatrix} m -
\begin{pmatrix} d \\ 0\end{pmatrix}\right\rVert^2 , \tag{3}$$

which is the observation that $\alpha\lVert m\rVert^2 =
\lVert\sqrt{\alpha}m\rVert^2$. This form is not a curiosity: it is how
regularised problems are solved in practice when the code already has a
least-squares solver, and it makes the interpretation of $\alpha$ transparent —
$\alpha$ is the ratio of the *weight* of the prior equations to the weight of the
data equations. Replacing $I$ in (3) by a roughening operator $L$ (a first or
second difference) turns (1) into $\lVert Fm-d\rVert^2 + \alpha\lVert Lm\rVert^2$,
which is the form used in potential-field and seismic inversion; the derivation is
identical with $F$ and $I$ substituted by $F$ and $\sqrt\alpha L$.

### 2.3 Spectral form and filter factors

Let $F = U\Sigma V^{\mathsf T}$ be the singular value decomposition, with singular
values $\sigma_k$. Then $F^{\mathsf T}F = V\Sigma^2V^{\mathsf T}$, and (2) becomes

$$m_\alpha = \sum_k \frac{\sigma_k^2}{\sigma_k^2+\alpha}\frac{\langle d,u_k\rangle}
{\sigma_k}v_k
= \sum_k \frac{\sigma_k}{\sigma_k^2+\alpha}\langle d,u_k\rangle v_k . \tag{4}$$

Two ways to read (4), and they are both useful:

- **As a filtered expansion.** Each mode is multiplied by the **filter factor**
  $$f_k = \frac{\sigma_k^2}{\sigma_k^2+\alpha} = \frac{1}{1+\alpha/\sigma_k^2}, \tag{5}$$
  which is 1 for $\sigma_k^2\gg\alpha$ and $\alpha/\sigma_k^2$ for
  $\sigma_k^2\ll\alpha$ — a high-pass-to-low-pass transition with knee at
  $\sigma_k = \sqrt\alpha$.
- **As a truncated-like inverse.** The coefficient
  $\sigma_k/(\sigma_k^2+\alpha)$ behaves like $1/\sigma_k$ for
  $\sigma_k \gg \sqrt\alpha$ and like $\sigma_k/\alpha$ for
  $\sigma_k \ll \sqrt\alpha$. The first is the unregularised inverse, and the
  second is a gentle damping, so the estimator **interpolates smoothly between
  the unregularised inverse and zero** — the continuous version of the hard
  truncation of lesson 01-16-05.

Note the two internal frequencies: the *filter* factor (5) is a function of
$\sigma_k$, and the *operator* being applied is
$\sigma_k/(\sigma_k^2+\alpha)$. Confusing the two is the most common algebra slip
in this subject.

### 2.4 The two limits, and why the estimator is a compromise

- $\alpha\to0$: $m_\alpha\to$ the unregularised least-squares solution (or the
  minimum-norm solution when $F$ is rank-deficient). Unbiased in the limit, but the
  variance is $\sigma_d^2\sum_k\sigma_k^{-2}$, which diverges as the smallest
  $\sigma_k\to0$.
- $\alpha\to\infty$: $m_\alpha\to0$. Zero variance, infinite bias (unless the
  truth happens to be zero).

The demonstration confirms both ends on the gravity-kernel problem
($\lVert m_{\text{true}}\rVert = 0.376565$):

```text
           alpha     model error                              note
           1e-14       82.439717         essentially unregularised
           1e-12       81.631991
           1e-10       45.666811
           1e+02        0.374573                 essentially m = 0
           1e+04        0.376545
    as alpha -> 0 the error tends to the unregularised noise-driven
    value; as alpha -> infinity it tends to ||m_true|| = 0.376565
```

The error at $\alpha = 10^{-14}$ is 82.4 against a true model norm of 0.38 — over
two hundred times the truth. **That is what "the regularisation parameter is not a
free knob" means**: the range of $\alpha$ that produces a physically sensible model
is five or six decades wide, and outside it the answer is meaningless at one end
and empty at the other.

## 3. The filter factors and the effective number of parameters

The demonstration tabulates (5) for the gravity kernel:

```text
         alpha         k=1         k=8        k=16        k=32        k=64
         1e-01    0.889882    0.498286    0.081406    0.000685    0.000000
         1e-02    0.987777    0.908523    0.469833    0.006811    0.000000
         1e-03    0.998764    0.990032    0.898600    0.064174    0.000004
         1e-06    0.999999    0.999990    0.999887    0.985627    0.003602
         1e-08    1.000000    1.000000    0.999999    0.999854    0.265532
```

and the trace of the resolution matrix of lesson 01-16-04, which is the sum of
the filter factors:

```text
         alpha    trace(R_alpha)    of
         1e-01            7.7976    80
         1e-02           15.1262    80
         1e-03           22.6895    80
         1e-04           30.2546    80
         1e-06           45.3051    80
         1e-08           60.2445    80
```

$\operatorname{tr}R_\alpha = \sum_k f_k$ is the **effective number of parameters**
the data determine at that $\alpha$. It is the honest answer to "how many
parameters did we resolve?", and it makes the regularisation visible as a trade of
parameter count for stability: $\alpha = 10^{-1}$ resolves 7.8 of 80,
$\alpha = 10^{-8}$ resolves 60.2. Note that the filter at $\alpha = 10^{-2}$
already damps mode 32 to 0.0068 — the data never constrained it.

## 4. The L-curve

### 4.1 What it is, and why it bends

For each $\alpha$ compute the pair

$$\big(R(\alpha), M(\alpha)\big) = \big(\lVert Fm_\alpha - d\rVert_2,\
\lVert m_\alpha\rVert_2\big),$$

and plot $\log M$ against $\log R$. The curve has two arms:

- **Small $\alpha$: the steep vertical arm.** $m_\alpha$ chases the noise, so
  $R$ is small and $M$ is large and grows rapidly as $\alpha$ decreases.
- **Large $\alpha$: the flat horizontal arm.** $m_\alpha\to0$, so $M$ is small and
  $R$ approaches $\lVert d\rVert$, changing slowly with $\alpha$.

The bend between them is the **corner**. The heuristic is that the corner is the
$\alpha$ where the solution stops being dominated by noise and starts being
dominated by the penalty.

### 4.2 Locating the corner

Curvature is computed numerically in the $(\log R, \log M)$ plane, treating
$\log\alpha$ as the parameter:

$$\kappa = \frac{x'y'' - y'x''}{\big((x')^2+(y')^2\big)^{3/2}} .$$

The demonstration evaluates 69 values of $\alpha$ from $10^{-14}$ to $10^{3}$ and
reports the neighbourhood of the maximum:

```text
           alpha        ||Km-d||           ||m||       curvature     model error
        1.00e-06        0.001588        0.640078          0.2471        0.518083
        3.16e-06        0.001679        0.480045          1.6156        0.298596
        1.00e-05        0.001770        0.415102          7.1729        0.176161
        3.16e-05        0.001867        0.389301         15.7501        0.101477  <- corner
        1.00e-04        0.001966        0.380079         11.4822        0.057133
        3.16e-04        0.002068        0.376917          3.9845        0.032619
```

with $\delta = \lVert\text{noise}\rVert = 2.749\times10^{-3}$ and
$\lVert m_{\text{true}}\rVert = 0.376565$. The corner is at
$\alpha_c = 3.162\times10^{-5}$, where the residual is $1.867\times10^{-3}$
(below the noise level), $\lVert m\rVert = 0.389301$ (close to the truth's norm)
and the model error is $0.101477$.

### 4.3 Three honest caveats about the corner

**It is not sharp.** The demonstration reports that only 2 of the 69 grid values
have curvature within 10 per cent of the maximum, spanning
$3.16\times10^{-5}$ to $5.62\times10^{-5}$ — a factor of 1.8. So the corner is
located to within a factor of about 2 on this problem, and quoting it to more than
one significant figure is not defensible.

**It is not the minimiser of the model error.** The sensitivity table below shows
the error continuing to fall as $\alpha$ increases past the corner.

**It balances the wrong pair.** The corner balances the residual against the model
norm. The quantity we would like to minimise is the distance to the true model, and
that quantity is not in the functional the curve balances. On this problem it lies
two decades away.

## 5. Sensitivity of the answer to $\alpha$

```text
           alpha  alpha / alpha_corner      ||Km-d||         ||m||     model error
        3.16e-07                 1e-02      0.001478      1.024667        0.953229
        3.16e-06                 1e-01      0.001679      0.480045        0.298596
        3.16e-05                 1e+00      0.001867      0.389301        0.101477
        3.16e-04                 1e+01      0.002068      0.376917        0.032619
        3.16e-03                 1e+02      0.003045      0.372401        0.012961
        3.16e-02                 1e+03      0.018091      0.345439        0.042837
```

Reading across: the error falls by roughly a factor of 3.1 per decade of $\alpha$
on the low side, reaches a minimum of $0.012961$ at $\alpha = 3.162\times10^{-3}$
— **one hundred times the L-curve corner** — and then rises again as the penalty
begins to dominate. The residual grows steadily and finally crosses the noise
level between $\alpha = 10^{-3}$ and $10^{-2}$.

So the practical statement is a range, not a number:

- The model error varies by a factor of 3 or so over one decade of $\alpha$ near
  the optimum. Choosing $\alpha$ within a factor of ten of the optimum is
  acceptable and changes the answer by less than a factor of three.
- The L-curve corner sits low by two decades on this problem. It is a useful
  *order-of-magnitude* device and a poor absolute rule.
- Any $\alpha$ that drives the residual *far below* the noise level is wrong,
  whatever curve it came from.

## 6. Choosing $\alpha$: the discrepancy principle

### 6.1 The rule

If the noise norm $\delta = \lVert d - d_{\text{true}}\rVert$ is known, choose
$\alpha$ so that the residual equals it:

$$R(\alpha) = \delta . \tag{6}$$

The rationale is that a fit better than the noise is fitting noise. $R(\alpha)$ is
continuous and increasing in $\alpha$ (with $R(0) = $ the unregularised residual
and $R(\infty) = \lVert d\rVert$), so (6) has a solution for any
$\delta \in (R(0), \lVert d\rVert)$ and it can be found by bisection on
$\log\alpha$ — 200 iterations of bisection reach machine precision in $\log\alpha$.

### 6.2 The measurement, and the comparison

```text
                        choice         alpha      residual   model error
                L-curve corner     3.162e-05      0.001867      0.101477
         discrepancy principle     2.474e-03      0.002749      0.013530
    smallest error on the grid     3.162e-03      0.003045      0.012961
```

with $\delta = 2.749465\times10^{-3}$. So:

- The discrepancy principle gives $\alpha = 2.474\times10^{-3}$, **78 times the
  L-curve corner**, and only 0.78 times the $\alpha$ that minimises the model
  error. Its model error, $0.013530$, is $1.04$ times the achievable minimum —
  essentially optimal on this problem.
- The L-curve corner is off by a factor of 7.8 in error.

**The discrepancy principle is not a theorem either.** It assumes $\delta$ is
known (rarely exactly true), that the noise is white and additive, and that the
model can fit the data at the noise level — the last fails when no admissible model
is close to the truth, which is exactly the existence failure of lesson 01-16-05.
If the true model cannot reproduce the data, the rule will choose an $\alpha$ far
too small while reporting a comfortable residual.

## 7. Choosing $\alpha$: generalised cross-validation

GCV requires no noise estimate. It estimates the predictive error of the
regularised inverse by leave-one-out cross-validation, whose closed form is

$$\mathrm{GCV}(\alpha) = \frac{\lVert Fm_\alpha - d\rVert_2^2}
{\big(m - \operatorname{tr}R_\alpha\big)^2} , \tag{7}$$

where $m$ is the number of data and $\operatorname{tr}R_\alpha$ the effective
number of parameters from Section 3. The denominator is the penalty for using too
many degrees of freedom, and the numerator for fitting too poorly. The
demonstration evaluates it on the same grid:

```text
                        choice         alpha     model error  vs error minimum
                L-curve corner     3.162e-05        0.101477              7.83
         discrepancy principle     2.474e-03        0.013530              1.04
                   GCV minimum     5.623e-04        0.025002              1.93
            true error minimum     3.162e-03        0.012961              1.00
```

All three rules land within a factor of eight of the model-error minimum, and the
last row — the true minimum — is the only quantity unavailable in practice. GCV
needs no $\delta$ but assumes independent errors with constant variance and that
the leave-one-out structure is meaningful; it is known to under-smooth when the
errors are correlated, which is the common case in geophysics.

**The recommendation that follows is not "use rule X".** It is: compute two or
three of them, and treat their disagreement as the honest uncertainty in
$\alpha$; then check that the residual is not far below the estimated noise level
and that the model is physically admissible.

## 8. $\alpha$ as a statement about belief

Write the noise as $d = Fm + \eta$ with $\eta$ independent and of variance
$\sigma_d^2$, and put a zero-mean Gaussian prior on the model with variance
$\sigma_m^2$. The negative log posterior is, up to constants,

$$\frac{1}{2\sigma_d^2}\lVert Fm-d\rVert^2 + \frac{1}{2\sigma_m^2}\lVert m\rVert^2 ,$$

which is proportional to (1) with

$$\alpha = \frac{\sigma_d^2}{\sigma_m^2} . \tag{8}$$

So $\alpha$ is the ratio of the data variance to the prior variance — a statement
of belief, not a numerical knob. Three consequences:

- **A larger $\alpha$ means less trust in the data or a stronger belief that the
  model is small.** Both increase the damping.
- **Scaling the model parameters changes $\alpha$.** If the model is measured in
  different units, or parameterised in a different basis, the same $\alpha$ means
  something different. This is the most common practical error in comparing
  inversions.
- **Equation (8) gives a starting value.** Estimating $\sigma_d$ from the data
  repeatability and $\sigma_m$ from the range of plausible model values gives an
  order-of-magnitude $\alpha$ before any curve is plotted. Here,
  $\sigma_d/\lVert d\rVert = 10^{-2}$ and a plausible
  $\sigma_m/\lVert m\rVert \sim 0.3$ would give
  $\alpha \sim (0.01\times0.274947)^2/(0.3\times0.376565)^2
  = 5.9\times10^{-4}$ — a factor of four below the discrepancy-principle value of
  $2.474\times10^{-3}$ and a factor of nineteen above the L-curve corner of
  $3.16\times10^{-5}$.

### Physical interpretation

The filter factor $\sigma_k^2/(\sigma_k^2+\alpha)$ has a direct physical reading as
a **sensitivity-weighted attenuation**: modes the physics transmits strongly
($\sigma_k^2 \gg \alpha$) pass through unaltered, modes it transmits weakly are
attenuated in proportion to their transmission, and the parameter $\alpha$ sets the
transition. Because the knee sits at $\sigma_k = \sqrt\alpha$, and because for a
depth-controlled kernel $\sigma_k \approx e^{-2\pi zk}$, choosing $\alpha$ is
choosing a **depth-dependent resolution length**: the regularised model cannot
contain features shorter than the wavelength at which the sensitivity has fallen to
$\sqrt\alpha$. That is the physical form of the bias floor measured in Section 5 —
the model is smooth on the scale the data can see, and no amount of arithmetic
sharpens it further. It is also why $\alpha$ must be tied to the noise: a noisier
data set is sensitive over a shorter range of wavenumbers, and the model must be
smooth accordingly.

## 9. Assumptions and regime of validity

1. **Linearity and a fixed operator.** $\alpha$ is a property of $(F,d)$; for a
   nonlinear problem it must be re-chosen at each iteration, and the linearisation
   error is not included in the bias–variance analysis.
2. **The penalty defines the prior.** $\lVert m\rVert^2$ asserts that the model is
   small; $\lVert Lm\rVert^2$ asserts that it is smooth (or that a derivative is
   small). A wrong penalty produces a wrong model with a small residual — the
   dangerous case, because the diagnostics look healthy.
3. **$\alpha$ depends on scaling.** Equation (8). Always state the units or the
   normalisation of $m$ with $\alpha$.
4. **The L-curve needs a corner.** For some problems the curve is smooth and the
   curvature maximum is nearly flat; on this problem only 2 of 69 grid points are
   within 10 per cent of the maximum.
5. **The discrepancy principle needs $\delta$.** It is biased low when the model
   cannot fit the data, and biased high when the noise is correlated and $\delta$
   is estimated from a covariance rather than measured.
6. **Regularisation does not improve resolution.** It selects a band of singular
   values; the number of resolved parameters is $\operatorname{tr}R_\alpha$ and it
   does not exceed what the data carry.
7. **The optimum $\alpha$ is not the corner and not a universal multiple of it.**
   On this problem the best $\alpha$ was 100 times the corner; the ratio depends on
   the problem and on the noise level, as the demonstration's noise sweep shows
   (corner $\alpha$ of $3.16\times10^{-3}$, $3.16\times10^{-5}$ and
   $3.16\times10^{-7}$ for $\varepsilon = 10^{-1}, 10^{-2}, 10^{-3}$).

## 10. Common mistakes

- **Quoting $\alpha$ without the units or normalisation of the model.** By (8) a
  change of model scaling changes $\alpha$ by the square of the scale factor.
- **Using $\lVert m\rVert^2$ when the prior is smoothness.** The two give
  different models with different resolution; the honest choice is the one that
  encodes the belief you actually hold.
- **Trusting a residual below the noise level.** It is evidence of over-fitting,
  not of a better inversion; measured in lesson 01-16-07, where a residual at the
  noise level coexists with a *smaller* model error than a residual well below it.
- **Reading the L-curve corner as the optimum.** It balances the wrong pair, and
  here is low by two decades.
- **Assuming one method's $\alpha$ is "the" answer.** Three standard rules
  disagreed by a factor of 78 on the same data.
- **Forgetting that the regularised solution is biased and reporting it as
  unbiased.** $\hat m_\alpha = R_\alpha m_{\text{true}} +$ noise: the bias is the
  part of the truth outside the retained band.
- **Applying $\lVert m\rVert^2$ penalty to a model with a non-zero mean.** The
  penalty then drives the mean to zero; either remove the mean or penalise only
  the deviation from a reference model $m_{\text{ref}}$ through
  $\lVert m - m_{\text{ref}}\rVert^2$.

## 11. Real-world applications

- **Potential-field inversion.** Tikhonov with a roughening operator is the
  standard tool; the depth–wavenumber trade-off of lesson 01-16-05 shows up as the
  requirement that $\alpha$ increase with the depth extent of the model.
- **Seismic and electromagnetic inversion.** The regulariser is the mathematical
  form of the geological prior; Occam inversion is the special case of
  penalising roughness with an appropriate $L$ and choosing $\alpha$ by the
  discrepancy principle.
- **Palaeoclimate reconstruction from boreholes.** A severely ill-posed diffusive
  inverse problem solved by Tikhonov with a smoothness penalty, and one of the
  clearest cases where the corner and the discrepancy principle disagree.
- **Machine learning.** Ridge regression is (2); the equivalence between ridge and
  a Gaussian prior is (8); weight decay is the same statement in a neural network,
  where the penalty's scaling relative to the data term is a known source of
  reproducibility problems.
- **Image and data reconstruction.** The L-curve and GCV are the standard
  parameter-choice devices, with GCV preferred when no noise estimate exists and
  the L-curve when the noise is non-white.
- **Operational uncertainty reporting.** $\operatorname{tr}R_\alpha$ and the
  posterior covariance $\sigma_d^2(F^{\mathsf T}F+\alpha I)^{-1}F^{\mathsf T}F
  (F^{\mathsf T}F+\alpha I)^{-1}$ are the numbers that make a model report honest.

## 12. Python demonstration

`code/regularization_theory.py` performs, in order:

1. the filter factors (5) for six values of $\alpha$ and the effective number of
   parameters $\operatorname{tr}R_\alpha$;
2. the L-curve on 69 values of $\alpha$ with the curvature formula, the corner,
   and its neighbourhood printed as a table;
3. the sensitivity table over seven decades of $\alpha$ around the corner, with
   the location of the model-error minimum;
4. the discrepancy principle by bisection on $\log\alpha$, with the comparison
   table against the corner and the true minimum;
5. the GCV curve (7) and its minimiser, with all three rules in one table;
6. the two limits and the corner's dependence on the noise level for
   $\varepsilon = 10^{-1}, 10^{-2}, 10^{-3}$.

It uses the standard library only and runs in about one second, evaluating every
$\alpha$ exactly from a single eigendecomposition of the symmetric kernel.

> **Breaking exercise.** Before running the GCV section, predict which of the three
> rules will be closest to the true error minimum and why. Then change the noise
> level to $\varepsilon = 10^{-3}$, rerun, and report whether the ranking of the
> three rules changes. A ranking that changes with the noise level is evidence that
> the comparison is not a property of the rule.

## 13. Further reading

- **Tikhonov, A. N., & Arsenin, V. Y. (1977). *Solutions of Ill-Posed Problems*.
  Wiley.** Level: graduate. The origin of the method and the classical theory.
- **Hansen, P. C. (2010). *Discrete Inverse Problems: Insight and Algorithms*.
  SIAM.** Level: graduate. The L-curve, GCV and the discrepancy principle, with
  the algorithms actually used and their failure modes.
- **Hansen, P. C. (1992). Analysis of discrete ill-posed problems by means of the
  L-curve. *SIAM Review*, 34, 561–580.** Level: graduate. The paper that
  established the L-curve, including the curvature computation.
- **Engl, H. W., Hanke, M., & Neubauer, A. (1996). *Regularization of Inverse
  Problems*. Kluwer.** Level: doctoral. Convergence rates for spectral
  regularisation, the discrepancy principle as a theorem with hypotheses, and
  parameter-choice rules in the continuous setting.
- **Aster, R. C., Borchers, B., & Thurber, C. H. (2018). *Parameter Estimation
  and Inverse Problems* (3rd ed.). Academic Press.** Level: graduate. Tikhonov
  regularisation in geophysical form, including the augmented-system
  implementation.
- **Menke, W. (2018). *Geophysical Data Analysis: Discrete Inverse Theory*
  (4th ed.). Academic Press.** Level: graduate. The same material with a strong
  emphasis on the geometry of the solution.
- **Golub, G. H., Heath, M., & Wahba, G. (1979). Generalized cross-validation as a
  method for choosing a good ridge parameter. *Technometrics*, 21, 215–223.**
  Level: graduate. The original GCV paper.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 14. Exercises

Solutions are in
[`exercises/06-regularization-theory-solutions.md`](./exercises/06-regularization-theory-solutions.md),
and the problems are in
[`exercises/06-regularization-theory-exercises.md`](./exercises/06-regularization-theory-exercises.md).

**★1.** Derive (2) from (1) by differentiation, and again from the augmented
system (3). State the eigenvalue bound that proves stability.

**★2.** Write the estimator in the singular-value basis, define the filter
factors, and state the limits of the filter factor and of the coefficient
$\sigma_k/(\sigma_k^2+\alpha)$ as $\sigma_k^2/\alpha\to0$ and $\to\infty$.

**★★3.** Show that $\operatorname{tr}R_\alpha = \sum_k\sigma_k^2/(\sigma_k^2+
\alpha)$ is decreasing in $\alpha$, with limits $n$ (full rank) as
$\alpha\to0$ and 0 as $\alpha\to\infty$. Evaluate it by hand for the separable
kernel of lesson 01-16-04 with $a = (1, 0.4, 0.1, 0.02)$ at $\alpha = 0.1$ and
$\alpha = 0.01$, and check the second against the value computed in that
lesson's exercise set.

**★★4.** Derive the L-curve curvature formula from the parametric definition
$x(t) = \log R(\alpha(t))$, $y(t) = \log M(\alpha(t))$ and show that it is
invariant under a change of parameterisation.

**★★5.** Using the lesson's sensitivity table, compute the ratio of model errors
at $\alpha = 0.1\alpha_c$ and $\alpha = 10\alpha_c$ and state whether the error
decreases or increases towards larger $\alpha$ in that range. Explain the sign.

**★★6.** Verify (8) numerically: with $\sigma_d = 0.01\lVert d\rVert$,
$\lVert d\rVert = 0.274947$, and a plausible prior $\sigma_m$ equal to
$\lVert m_{\text{true}}\rVert/\sqrt{3}$, compute the implied $\alpha$ and compare
with $\alpha_{\text{disc}} = 2.474\times10^{-3}$.

---

**★★★7.** Implement the discrepancy principle, the L-curve corner and GCV for
noise levels $\varepsilon = 10^{-1}, 10^{-2}, 10^{-3}$, and tabulate the three
$\alpha$ and the three model errors at each level. Report which rule is most
stable across the three noise levels and which is most accurate at each level.

**★★★8.** Replace the penalty $\lVert m\rVert^2$ by $\lVert Lm\rVert^2$ with $L$
the first-difference operator, redo the L-curve and the discrepancy-principle
comparison, and report how the model error and the number of resolved parameters
change. Explain the difference in terms of which singular directions are damped.

**★★★9.** For the same problem, compute the posterior covariance
$C_m = \sigma_d^2(F^{\mathsf T}F+\alpha I)^{-1}F^{\mathsf T}F(F^{\mathsf T}F+
\alpha I)^{-1}$ at $\alpha = \alpha_{\text{disc}}$ and at $\alpha = \alpha_c$,
and compare the diagonal entries. Report the ratio of the largest to the smallest
diagonal, and interpret it as a spatially varying uncertainty.

## 15. Self-assessment checklist

- [ ] I can derive the Tikhonov estimator three ways and state the stability bound.
- [ ] I can write it in the singular basis and interpret the filter factors.
- [ ] I can explain the two limits of $\alpha$ and why the useful range is finite
      and narrow.
- [ ] I can compute and interpret $\operatorname{tr}R_\alpha$ as the effective
      number of resolved parameters.
- [ ] I can compute an L-curve, locate its corner, and state what the corner does
      not optimise.
- [ ] I can implement the discrepancy principle by bisection and state its
      assumptions.
- [ ] I can implement GCV and say when it is preferable to the other two rules.
- [ ] I can quantify the sensitivity of the model to $\alpha$ and give a
      defensible range rather than a single number.
- [ ] I can give the Bayesian interpretation of $\alpha$ and explain why it
      depends on model scaling.

## Related lessons

- [01-16-05 Ill-Posedness in the Sense of Hadamard](./05-ill-posedness.md) — the
  failures addressed here, and the truncation experiment this lesson generalises.
- [01-16-04 Spectral Theory of Operators and Eigenfunction Bases](./04-spectral-theory.md)
  — the resolution matrix whose trace is the effective number of parameters.
- [01-16-03 Linear Operators, Adjoints and Compactness](./03-operators.md) — the
  singular spectrum and the adjoint used to form $F^{\mathsf T}d$.
- [01-14-04 Linear and Nonlinear Least Squares](../14-optimization/04-least-squares.md)
  — the normal equations that the augmented system (3) reduces to.
- [01-16-07 Discretisation, Convergence and Regularisation Discrepancy](./07-discretization-convergence.md)
  — what happens to $\alpha$ and to the answer as the grid is refined.
- [01-13-xx Probability and Statistics Foundations](../13-probability-and-statistics-foundations/README.md)
  — the Gaussian prior and likelihood behind (8).
- [18-inverse-problems](../../18-inverse-problems/README.md) — the operational
  treatment: covariance, parameter choice and uncertainty reporting.
