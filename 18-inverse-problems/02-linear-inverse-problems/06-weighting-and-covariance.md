---
id: 18-02-06
title: "Data Weighting and Error Covariance Specification"
level: graduate
prereqs: ["18-02-01", "01-13-09", "01-13-03"]
tags: [inverse-problems, weighting, covariance, generalized-least-squares, whitening, ar1]
---

# Data Weighting and Error Covariance Specification

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** generalised least squares
   $\hat{\mathbf{m}} = (G^{\!\top}C_d^{-1}G)^{-1}G^{\!\top}C_d^{-1}\mathbf{d}$
   and its covariance, and **state** when it is the minimum-variance unbiased
   estimator.
2. **Recognise** correlated error structures produced by processing, and
   **construct** a covariance matrix for them.
3. **Write** the AR(1) precision matrix in closed form and **verify** it
   numerically.
4. **Show** that generalised least squares is ordinary least squares on whitened
   data, and **use** whitening to reuse standard diagnostics.
5. **Measure** what ignoring a known covariance costs: in efficiency of the
   estimate and — more seriously — in the reported uncertainty.
6. **Interpret** a reduced $\chi^{2}$ under correlated noise, and **explain** why
   residual-based variance estimates cannot replace a stated error model.

## Prerequisites

- [18-02-01 Overdetermined Problems and Least Squares](01-overdetermined.md) —
  the unweighted estimator, its covariance and the $\chi^{2}$ discussion.
- [01-13-09 Error and Uncertainty Propagation](../../01-mathematics/13-probability-and-statistics-foundations/09-error-propagation.md) —
  how covariance matrices propagate through linear maps.
- [01-13-03 Expectation, Variance and Moments](../../01-mathematics/13-probability-and-statistics-foundations/03-expectation-variance.md) —
  the moment language used for the estimator.

## 1. The error model is part of the model

Least squares minimises an unweighted sum of squares, which is the right thing to
do only when the errors are independent and have a **common** variance. Both halves
of that assumption fail routinely in geophysics:

- **instrument and terrain effects** give different variances to different data
  (heteroscedasticity);
- **processing** — filtering, gridding, removing a regional field, drift
  correction, stacking — combines neighbouring measurements, so their errors become
  **correlated**.

A covariance matrix $C_d = \mathbb{E}[\mathbf{e}\mathbf{e}^{\!\top}]$ encodes both.
Treating $C_d$ as an optional refinement is the central mistake this lesson is
about: ignoring a known $C_d$ costs efficiency in the estimate and, more damagingly,
produces error bars that can be wrong by more than an order of magnitude.

The demonstration uses a SYNTHETIC regional-trend problem: $N = 24$ stations evenly
spaced over $\pm6\ \mathrm{km}$ (spacing $0.52\ \mathrm{km}$), a quadratic trend in
$x$ with $M = 3$ parameters, and errors drawn from a stationary **AR(1)** model

$$C_d[i,j] = \sigma^{2}\rho^{\lvert i-j\rvert},\qquad
\sigma = 0.020\ \mathrm{mGal},\quad \rho = 0.70 .$$

So the marginal variance is $\sigma^{2} = 4.000000\times10^{-4}\ \mathrm{mGal^{2}}$
and the first-lag covariance is $2.800000\times10^{-4}\ \mathrm{mGal^{2}}$.
$\kappa(C_d) = 29.39$, so the covariance itself is benign.

All models and data in this module are **SYNTHETIC**.

## 2. The most useful AR(1) fact

For a stationary AR(1) covariance the **inverse** is tridiagonal:

$$C_d^{-1} = \frac{1}{\sigma^{2}(1-\rho^{2})}
\begin{pmatrix}
1 & -\rho & & \\
-\rho & 1+\rho^{2} & -\rho & \\
& \ddots & \ddots & \ddots \\
& & -\rho & 1
\end{pmatrix},$$

with $1+\rho^{2}$ on the interior diagonal and $1$ at both corners. The
demonstration verifies this closed form against the numerically inverted matrix:

$$\max\left\lvert C_d^{-1} - C_d^{-1}\big|_{\text{analytic}}\right\rvert
= 8.185\times10^{-12},$$

which is roundoff for entries of order $7\times10^{3}$. Two consequences:

- the weight matrix $W = C_d^{-1}$ is **sparse**, so generalised least squares costs
  almost nothing extra in memory or time;
- for $\rho>0$ the weights are **negative off the diagonal**: a datum that is above
  the trend makes its immediate neighbours' being also above the trend less
  surprising, so they are down-weighted relative to the naive case. Positive
  correlation is information, and the estimator uses it.

## 3. Generalised least squares, derived

Minimise the $C_d^{-1}$-weighted misfit

$$J(\mathbf{m}) = (\mathbf{d}-G\mathbf{m})^{\!\top}C_d^{-1}(\mathbf{d}-G\mathbf{m}),$$

whose gradient is $-2G^{\!\top}C_d^{-1}(\mathbf{d}-G\mathbf{m})$. Stationarity gives

$$\boxed{\;G^{\!\top}C_d^{-1}G\,\hat{\mathbf{m}}
= G^{\!\top}C_d^{-1}\mathbf{d}\;},\qquad
\hat{\mathbf{m}} = (G^{\!\top}C_d^{-1}G)^{-1}G^{\!\top}C_d^{-1}\mathbf{d},$$

with

$$\operatorname{Cov}(\hat{\mathbf{m}}) = (G^{\!\top}C_d^{-1}G)^{-1},
\qquad \mathbb{E}\hat{\mathbf{m}} = \mathbf{m}.$$

By the Gauss–Markov theorem this is the minimum-variance estimator among linear
unbiased estimators **whenever $C_d$ is the true covariance**: the weighting is what
makes it optimal, and a wrong $C_d$ makes it merely unbiased.

Because $C_d$ is positive definite it has a square root; taking
$L = \operatorname{chol}(C_d)$ (so $C_d = LL^{\!\top}$) and

$$\tilde{G} = L^{-1}G,\qquad \tilde{\mathbf{d}} = L^{-1}\mathbf{d},$$

the weighted problem becomes an ordinary one in the whitened variables. Verified:

$$\lVert\hat{\mathbf{m}}_{\text{GLS}} - \hat{\mathbf{m}}_{\text{whitened}}\rVert_\infty
= 4.441\times10^{-15},$$

$$\hat{\mathbf{m}} = (7.989787,\ -0.599922,\ 0.020348) .$$

**Whitening is the practical recommendation** of this lesson: transform the
problem once and then use every unweighted tool — QR, SVD, residual analysis,
diagnostics — knowing that the transformed noise is unit-variance and
uncorrelated.

## 4. What weighting buys: efficiency

Measured over 2000 realisations:

| parameter | sd (unweighted) | sd (generalised) | variance ratio |
|---|---|---|---|
| $m_1$ | 0.013189 | 0.012904 | 1.045 |
| $m_2$ | 0.002177 | 0.002039 | 1.140 |
| $m_3$ | 0.000598 | 0.000540 | 1.228 |

Predicted GLS sd from $(G^{\!\top}C_d^{-1}G)^{-1}$:
$(0.012751,\ 0.002069,\ 0.000545)$ against measured
$(0.012904,\ 0.002039,\ 0.000540)$ — the covariance formula is validated.

Be honest about the size of the gain: here it is $4.5\%$ to $23\%$ of variance. The
reason is that a polynomial trend is determined mostly by the **low-frequency**
content of the data, and correlated noise does not confuse low frequencies. When
the model has structure at scales comparable to the correlation length the gain is
much larger. Measure it for your own design rather than assuming either way.

## 5. What ignoring correlation costs: the reported error

This is where the damage is done. If the analyst assumes independence, the quoted
covariance is $\hat{\sigma}^{2}(G^{\!\top}G)^{-1}$. The true covariance of the
unweighted estimator is

$$\operatorname{Cov}(\hat{\mathbf{m}}_{\text{OLS}})
= (G^{\!\top}G)^{-1}G^{\!\top}C_d\,G\,(G^{\!\top}G)^{-1}.$$

Measured for the same design:

| parameter | true sd of OLS | sd assuming white noise | understatement factor |
|---|---|---|---|
| $m_1$ | 0.012983 | 0.000391 | **33.2** |
| $m_2$ | 0.002211 | 0.000072 | **30.7** |
| $m_3$ | 0.000594 | 0.000022 | **26.6** |

and the direct check against the simulated scatter: the measured OLS sd divided by
the independence-assuming sd for $m_3$ is $26.756$ — matching the analytic factor
$26.6$.

The estimate itself is still unbiased; it is the **uncertainty** that is wrong,
by a factor of nearly thirty. Two sentences follow, and they should be in every
reporting checklist:

1. a parameter value with an independence-assuming error bar under correlated noise
   is not a conservative statement — it is an over-confident false one;
2. the correction is not a fudge factor but a matrix: write $C_d$ down, whiten, and
   let the algebra propagate.

## 6. Reduced $\chi^{2}$ under correlated noise

With the *true* $\sigma$ and $N-M = 21$ degrees of freedom, but the statistic
computed as if the noise were white:

$$\chi^{2}_{\text{reduced}} = 0.5789 \pm 0.2541
\qquad(\text{chi}^{2}\text{-based sd } 0.3086).$$

The mean is far from 1 — and *below* it, because positive correlation lets the
trend absorb part of the noise, so the residual sum is smaller than the white-noise
expectation. The diagnostic is therefore not "wrong by a bias" but
**uninterpretable**: it measures the mismatch between the assumed and the true
error model, not the quality of the fit. The same statistic computed on whitened
residuals, where the noise is unit-variance by construction, gives

$$\overline{\chi^{2}_{\text{reduced}}} = 0.9918 \pm 0.3011 ,$$

so whitening repairs the diagnostic along with the estimator.

The general rule stands: **a reduced $\chi^{2}$ near 1 is not evidence that your
error model is right; it is evidence that you have stopped being able to detect
that it is wrong.** Only the correct $C_d$ makes the statistic meaningful.

## 7. Fully worked example: a covariance you can defend

*(a) Marginal variance.* From instrument specifications and repeat measurements,
$\sigma = 0.020\ \mathrm{mGal}$; the demonstration uses this as
$C_d[i,i] = 4.0\times10^{-4}\ \mathrm{mGal^{2}}$.

*(b) Correlation.* A Gaussian smoothing with length $\ell$ applied to independent
noise of spacing $\Delta x$ gives approximately
$\rho = \exp(-\Delta x^{2}/(4\ell^{2}))$. With $\Delta x = 0.52\ \mathrm{km}$ and
$\ell = 0.35\ \mathrm{km}$, $\rho = \exp(-0.2704/0.49) = \exp(-0.5518) = 0.576$. A
measured correlation length is better; either way the *functional form* (exponential
decay) is the modelling assumption, and it must be stated.

*(c) Checking invertibility and conditioning.* Measured $\kappa(C_d) = 29.39$ for
$\rho=0.70$; the analytic expression shows $\kappa$ degrades rapidly as
$\rho\to1$ (the matrix approaches rank 1 + a boundary term). Before using $C_d^{-1}$,
look at $\kappa(C_d)$; if it is enormous, either shorten the correlation or work with
$C_d^{-1}$ analytically (as in §2) rather than inverting.

*(d) Two checks after whitening.* (i) Verify numerically that the whitened noise
has unit variance: $\operatorname{diag}(L^{-1}CL^{-\!\top}) = 1$ to roundoff; (ii)
verify that the weighted and whitened estimates agree to roundoff, as measured in
§3 ($4.4\times10^{-15}$). Both are one-line tests that catch a transposed or
mis-ordered covariance matrix.

## 8. Assumptions and regime of validity

- **$C_d$ is known.** If it is estimated, its uncertainty propagates into the model
  covariance and the quoted errors are optimistic
  ([21-01-03](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md)).
- **Errors are Gaussian.** GLS needs only second moments to be BLUE; the
  $\chi^{2}$ and the confidence interpretation need the Gaussian shape.
- **$G$ is correct and linear.** A wrong kernel biases the estimate and cannot be
  repaired by weighting.
- **Stationary, parameterised covariance.** AR(1) is a model, chosen for
  tractability; real processing may need several correlation lengths or a
  non-stationary $C_d$ (e.g. gridding artefacts near data gaps).
- **Positive definiteness.** $C_d$ must be invertible; adding structure that
  violates this produces a singular weight matrix.
- **The numbers are design-specific.** The measured efficiency gain (1.05–1.23) and
  the understatement factors (27–33) belong to this geometry and correlation; they
  are demonstrations, not constants.

## 9. Running the demonstration

The demonstration for this lesson is [`code/weighting_and_covariance_demo.py`](code/weighting_and_covariance_demo.py) — print-only, no network access, fixed seed
`np.random.default_rng(20261014)`.

```bash
cd 18-inverse-problems/02-linear-inverse-problems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python weighting_and_covariance_demo.py
```

It prints the covariance, the analytic AR(1) check, the whitening equivalence, the
efficiency table, the true-versus-assumed error table, both $\chi^{2}$ statistics
and the residual-variance bias. Runtime is about a second. Companion problems are
in
[`exercises/06-weighting-and-covariance-exercises.md`](exercises/06-weighting-and-covariance-exercises.md).

## Mastery checkpoint

Without notes:

> A gravity profile of 40 points, spacing $0.5\ \mathrm{km}$, was low-pass
> filtered, giving errors with $\sigma = 0.03\ \mathrm{mGal}$ and
> $\rho = 0.8$ between neighbours. **(a)** Write down $C_d$ and its inverse in
> closed form. **(b)** Derive the weighted estimator and its covariance.
> **(c)** A colleague fits a 4-parameter trend with ordinary least squares and
> reports errors from $\hat{\sigma}^{2}(G^{\!\top}G)^{-1}$. What is wrong with the
> reported errors, and in which direction? **(d)** Give two numerical checks you
> will run after whitening. **(e)** Their reduced $\chi^{2}$ is 0.62 — is the model
> good?

Worked solutions are in
[`exercises/06-weighting-and-covariance-solutions.md`](exercises/06-weighting-and-covariance-solutions.md).

## Common pitfalls

1. **Treating the error model as a detail.** The quoted uncertainty can be wrong by
   a factor of thirty.
2. **Using unweighted least squares and calling the result "conservative".** It is
   over-confident, not conservative.
3. **Assuming $\chi^{2}\approx1$ validates the error model.** It only means the
   mismatch is undetectable in that statistic.
4. **Estimating $\sigma$ from residuals.** With correlated noise the residual-based
   estimate is biased low: measured $0.014890\ \mathrm{mGal}$ against a true
   marginal $0.020000$, a ratio of $0.7445$.
5. **Inverting a nearly singular $C_d$.** For strong correlation use the analytic
   inverse.
6. **Forgetting that weights change the metric, not just the numbers.** Whitening is
   a coordinate change; the covariance and the diagnostics must be transformed too.

## Related modules

- [18-02-01 Overdetermined Problems and Least Squares](01-overdetermined.md) —
  the unweighted case derived and measured.
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](04-svd-analysis-inverse.md) —
  run the SVD on the whitened operator, not the raw one.
- [18-02-05 Resolution and Information Matrices in Interpretation](05-resolution-matrices.md) —
  the information matrix formed with $C_d^{-1}$.
- [21-01-04 Linear, Multiple and Robust Regression](../../21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md) —
  regression diagnostics and robustness.
- [19-07-03 Model Validation Against Observations](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/03-model-validation.md) —
  what validation can and cannot test.
