---
id: 26-03-06
title: "Formula Sheet: Inverse Theory and Statistics"
level: advanced
prereqs: []
estimated_minutes: 35
tags: [reference, formulas, inverse-theory, statistics]
---

# Formula Sheet: Inverse Theory and Statistics

The formulas that turn data into estimates, and — more importantly — into
statements about how much the data actually determined. Estimation, uncertainty
propagation, resolution, regularisation and model comparison, with the
assumptions each one needs.

## How to use this page

The sheet is ordered the way an analysis is normally written: probability, then
estimation, then uncertainty, then resolution and comparison. Anything that is a
*choice* rather than a theorem (norm, prior, damping parameter, rank cut-off) is
labelled as such, because those choices must appear in a methods section.
Numbers quoted in the worked example come from
`code/formulas_inverse_statistics_demo.py`.

*Provenance:* no measured data. The worked example is **SYNTHETIC** — the data
are drawn from a seeded generator with a stated true model.

## 1. Probability

| Formula | Statement | Notes |
|---|---|---|
| Bayes | $p(m\lvert d) = \dfrac{p(d\lvert m)p(m)}{p(d)}$ | posterior $\propto$ likelihood $\times$ prior |
| Conditional probability | $p(A\lvert B) = p(A\cap B)/p(B)$ | $p(B) > 0$ |
| Total probability | $p(A) = \sum_k p(A\lvert B_k)p(B_k)$ | partition of the sample space |
| Independence | $p(A\cap B) = p(A)p(B)$ | a model assumption, not a default |
| Expectation | $E[X] = \sum_k x_kp(x_k)$ or $\int xp(x)dx$ | discrete or continuous |
| Variance | $\operatorname{Var}X = E[X^{2}] - (E[X])^{2}$ | units squared |
| Covariance | $\operatorname{Cov}(X,Y) = E[XY] - E[X]E[Y]$ | zero does not imply independence |
| Correlation | $\rho = \operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)$ | $\lvert\rho\rvert \le 1$ |

| Distribution | Density | Mean / variance |
|---|---|---|
| Gaussian | $\dfrac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^{2}/(2\sigma^{2})}$ | $\mu$, $\sigma^{2}$ |
| Multivariate Gaussian | $(2\pi)^{-n/2}\lvert C\rvert^{-1/2}e^{-\frac{1}{2}(\mathbf{x}-\boldsymbol\mu)^{T}C^{-1}(\mathbf{x}-\boldsymbol\mu)}$ | $\boldsymbol\mu$, $C$ |
| Poisson | $\lambda^{k}e^{-\lambda}/k!$ | $\lambda$, $\lambda$ (mean = variance) |
| Exponential | $\lambda e^{-\lambda x}$ | $1/\lambda$, $1/\lambda^{2}$ |
| Uniform | $1/(b-a)$ on $[a,b]$ | $(a+b)/2$, $(b-a)^{2}/12$ |
| $\chi^{2}_k$ | sum of $k$ squared standard normals | $k$, $2k$ |

## 2. Estimation

| Estimator | Formula | Notes |
|---|---|---|
| Sample mean | $\bar{x} = \tfrac{1}{N}\sum x_i$ | standard error $\sigma/\sqrt{N}$ |
| Weighted mean | $\bar{x}_w = \sum w_i x_i/\sum w_i$, $w_i = 1/\sigma_i^{2}$ | minimum-variance for known Gaussian errors |
| Standard error of the weighted mean | $1/\sqrt{\sum w_i}$ | the 1σ uncertainty of the combined value |
| Sample variance | $s^{2} = \tfrac{1}{N-1}\sum(x_i-\bar{x})^{2}$ | unbiased with $N-1$ |
| Median | middle value of the ordered sample | robust to outliers |
| Chi-square | $\chi^{2} = \sum_i (d_i - f_i)^{2}/\sigma_i^{2}$ | reduced: divide by the degrees of freedom |
| Maximum likelihood | $\hat{m}$ maximising $p(d\lvert m)$ | for Gaussian noise this is least squares |
| Gaussian log-likelihood | $-\tfrac{1}{2}(\mathbf{d}-A\mathbf{m})^{T}C_d^{-1}(\mathbf{d}-A\mathbf{m}) + \text{const}$ | the objective actually minimised |
| Linear MLE with covariance | $\mathbf{m} = (A^{T}C_d^{-1}A)^{-1}A^{T}C_d^{-1}\mathbf{d}$ | Gauss–Markov estimate |
| Posterior covariance | $C_m = (A^{T}C_d^{-1}A)^{-1}$ | model uncertainty from data noise only |

## 3. Regularisation and resolution

| Formulation | Solution | What it controls |
|---|---|---|
| Zeroth-order Tikhonov | $\mathbf{m} = (A^{T}A + \alpha I)^{-1}A^{T}\mathbf{d}$ | model norm |
| General-order Tikhonov | $\mathbf{m} = (A^{T}A + \alpha L^{T}L)^{-1}A^{T}\mathbf{d}$ | roughness through $L$ |
| Truncated SVD | keep $\sigma_i > \tau$ | rank / effective dimensionality |
| Damped SVD | divide by $(\sigma_i^{2} + \alpha)/\sigma_i$ | smooth spectral filter |
| Resolution matrix | $R = (A^{T}C_d^{-1}A + \alpha L^{T}L)^{-1}A^{T}C_d^{-1}A$ | how much of each true parameter is seen |
| Model covariance | $C_m = (A^{T}C_d^{-1}A + \alpha L^{T}L)^{-1}$ | how uncertain each estimate is |
| Trade-off | $\operatorname{tr}R$ falls as $\alpha$ rises | resolution and variance cannot both be improved |
| Generalised cross-validation | $\text{GCV}(\alpha)$ | data-driven damping choice |
| L-curve elbow | plot $\lVert A\mathbf{m}-\mathbf{d}\rVert$ vs $\lVert L\mathbf{m}\rVert$ | heuristic, not an optimum |

Two structural facts worth memorising. $\operatorname{tr}R$ estimates the
number of parameters the data actually resolve, and it is always less than the
nominal number of parameters when damping is used. And resolution and covariance
move in opposite directions with $\alpha$: improving one always degrades the
other.

## 4. Sampling and model comparison

| Method | Quantity produced | Cost |
|---|---|---|
| Metropolis–Hastings | posterior samples | acceptance $\min[1, p(m')q(m\lvert m')/(p(m)q(m'\lvert m))]$ |
| Sample importance resampling | weighted posterior samples | needs a good proposal |
| Gaussian process emulator | surrogate likelihood | expensive forward models |
| Akaike information criterion | $\text{AIC} = 2k - 2\ln\hat{L}$ | penalises parameters, not complexity |
| Bayesian information criterion | $\text{BIC} = k\ln N - 2\ln\hat{L}$ | stronger penalty, larger $N$ |
| Evidence (marginal likelihood) | $p(d) = \int p(d\lvert m)p(m)dm$ | exact model comparison; usually intractable |
| Bootstrap | resampled estimator distribution | only valid if the sample is representative |
| Jackknife | leave-one-out estimate | cheap bias and variance estimate |
| Monte Carlo standard error | $\propto \sigma/\sqrt{N_\text{samples}}$ | the reason MCMC chains are long |

## 5. Error propagation and intervals

| Quantity | Formula | Conditions |
|---|---|---|
| Function of one variable | $\sigma_f = \lvert df/dx\rvert\,\sigma_x$ | first order |
| Sum | $\sigma_{f}^{2} = \sum_i\sigma_i^{2}$ | independent inputs |
| Linear combination | $\sigma_f^{2} = \sum_i (\partial f/\partial x_i)^{2}\sigma_i^{2}$ | independent inputs |
| Correlated inputs | $\sigma_f^{2} = \mathbf{g}^{T}C\mathbf{g}$ with $g_i = \partial f/\partial x_i$ | general case |
| Ratio | $\sigma_f/f = \sqrt{(\sigma_x/x)^{2} + (\sigma_y/y)^{2}}$ | independent inputs |
| Standard error of the mean | $\sigma_{\bar{x}} = \sigma/\sqrt{N}$ | independent samples |
| 95 % interval, Gaussian | $\bar{x} \pm 1.96\,\sigma_{\bar{x}}$ | known $\sigma$ |
| 95 % interval, small $N$ | $\bar{x} \pm t_{0.975,N-1}\,s/\sqrt{N}$ | uses the $t$ distribution |
| Effective $N$ | $N_{\text{eff}} = N\,(1-\rho_1)/(1+\rho_1)$ approx. | for autocorrelated series |

The distinction between 1.96 and the $t$ quantile matters in real surveys, where
$N$ is small: at $N = 5$ the $t$ value is 2.776, so a "95 %" interval using 1.96
is far too narrow.

## Worked example (numbers from the verification script)

Given five measurements with stated uncertainties
(10.2 ± 0.30, 9.7 ± 0.45, 10.4 ± 0.20, 9.9 ± 0.50, 10.1 ± 0.35):

| Quantity | Value |
|---|---|
| Unweighted mean | 10.060000 |
| Sample standard deviation | 0.270185 |
| Weighted mean ± 1σ | $10.209669 \pm 0.137086$ |
| $\chi^{2}$ with 4 dof | 2.671225 (reduced 0.667806) |
| Normal 95 % coverage factor | 1.959964 |
| $t$ quantile, 95 %, 4 dof | 2.776445 |

A linear fit with 15 data points, $\sigma_d = 0.10$ and true parameters
$[1.5,\ 0.8]$:

| Quantity | Value |
|---|---|
| Estimated parameters | $[1.5277,\ 0.7248]$ |
| Parameter 1σ | $[0.0492,\ 0.0837]$ |
| Parameter correlation | $-0.850963$ |
| Residual RMS | 0.124819 |
| $\chi^{2}/\text{dof}$ | 1.797678 |
| Standard errors rescaled by $\sqrt{\chi^{2}/\text{dof}}$ | $[0.0659,\ 0.1122]$ |

Damped inversion of a small linear problem:

| Damping $\alpha$ | $\lVert m\rVert$ | $\lVert d - Am\rVert$ | $m$ |
|---|---|---|---|
| 0 | 1.41414 | 0.01000 | $[1.0001,\ 0.9998]$ |
| $10^{-4}$ | 1.41407 | 0.01000 | $[1.0001,\ 0.9997]$ |
| $10^{-2}$ | 1.40716 | 0.01407 | $[1.0000,\ 0.9900]$ |
| 1 | 0.99999 | 0.63250 | $[0.8000,\ 0.6000]$ |

Monte Carlo check of the $1/\sqrt{N}$ law:

| $N$ | Sample mean | Standard error | Sample std (true 2.0) |
|---|---|---|---|
| 100 | $-0.20553$ | 0.17743 | 1.77432 |
| 400 | $-0.04688$ | 0.10409 | 2.08190 |
| 1600 | $-0.01822$ | 0.04917 | 1.96677 |

The fraction of standard normal draws inside $\pm 1.96$ is 0.9508, against the
theoretical 0.95. The resolution matrix for the damped problem is
$[[0.9160, 0.0763], [0.0763, 0.8397]]$ with trace 1.755757, so the data resolve
about 1.76 of the two nominal parameters.

Three readings of this table are worth carrying away. The weighted mean carries
0.137086 as its standard error while the unweighted spread is 0.270185 — using
the spread as an error estimate would overstate the uncertainty by a factor of
two here. $\chi^{2}/\text{dof} = 1.80$ means either the stated $\sigma_d$ is too
small or the model is incomplete; both possibilities must be reported, and the
honest response is to rescale the errors (the last row) rather than to ignore
the value. And the correlation of $-0.851$ between the two fitted parameters is a
statement about the *design*, not about the physics: with a shorter offset range
it would approach $\pm 1$ and the parameters would become effectively
unresolvable.

## Assumptions and regime of validity

- Gaussian error propagation is a first-order (linearised) approximation; it
  fails for strongly non-linear functionals and for skewed posteriors.
- The Gauss–Markov estimate is minimum-variance only for the stated data
  covariance; misspecified correlation between data biases the result.
- Resolution and covariance matrices characterise the **linearised** problem;
  they are not the true posterior spread for a non-linear problem.
- $\chi^{2}$ intervals assume the errors are independent and correctly scaled;
  correlated data require the full covariance and reduced degrees of freedom.
- AIC and BIC compare models on the same data with the same likelihood
  definition; changing the noise model invalidates the comparison.
- Bootstrap inference assumes the sample is representative of the population.
  In spatial geophysics, samples are almost never independent, and the
  block-bootstrap is the minimum correction.

## Verification script

[`code/formulas_inverse_statistics_demo.py`](./code/formulas_inverse_statistics_demo.py) —
print-only, seeded with `default_rng(20261014)`, under a second, exit 0. It
prints the weighted mean, the linear fit with covariance, the damping
trade-off, the Monte Carlo convergence and the resolution matrix quoted above.

## Related pages

- [Formula Sheet: Linear Algebra, SVD and Numerics](./02-formulas-linear-algebra-numerics.md)
- [Formula Sheet: Waves, Elasticity and Seismology](./03-formulas-waves-seismology.md)
- [18-inverse-problems folder overview](../../18-inverse-problems/README.md)
- [21-statistics-bayesian-ml folder overview](../../21-statistics-bayesian-ml/README.md)
