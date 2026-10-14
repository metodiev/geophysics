---
id: 21-02-02
title: "Variograms, Covariance and Model Fitting"
level: doctoral
prereqs: ["21-02-01", "01-13-06"]
estimated_minutes: 70
tags: [geostatistics, variogram, covariance-models, model-fitting, robust-estimation]
---

# Variograms, Covariance and Model Fitting

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the experimental semivariogram, stating the lag binning, the lag
   tolerance and the number of pairs behind each point.
2. **Derive** the classical and Cressie-Hawkins estimators and **explain** which
   is robust to outliers and why.
3. **Write** the spherical, exponential and Gaussian models, and **convert**
   between the effective-range and e-folding conventions.
4. **Fit** a model by weighted least squares with a stated weight, and **compare**
   candidate models by a weighted residual sum of squares.
5. **Explain** why an arbitrary function is not a valid variogram and **state**
   the conditional-negative-definiteness requirement.
6. **Diagnose** the artefacts of fitting: the sill-range trade-off, the nugget,
   anisotropy and nesting.

All fields in this lesson are **SYNTHETIC**: generated from a stated exponential
covariance plus a stated nugget. No measured value is used, and the fitted
parameters below constrain only the demonstration's field.

## Prerequisites

- [21-02-01 Regionalised Variables and Spatial Continuity](01-regionalized-variables.md) —
  the random-function model and the stationarity hierarchy.
- [01-13-06 Point Estimation, Bias, Consistency and Efficiency](../../01-mathematics/13-probability-and-statistics-foundations/06-estimation-theory.md) —
  what a fitting criterion optimises.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](../01-statistics-in-practice/01-descriptive-statistics.md) —
  the robust-estimation ideas used in the Cressie-Hawkins estimator.

## 1. Intuition: fitting continuity instead of a curve

A variogram is a description of how quickly a property forgets its own value.
At short lags the difference between two samples is small, so the semivariance
is small; at long lags they are unrelated, so the semivariance reaches the
variance of the field. Between those limits lies a shape, and the shape — not the
individual points — is what enters kriging.

The reason a *model* is fitted rather than the raw points read off is not
cosmetic. Kriging requires the semivariance at arbitrary lags and, more
importantly, requires a function that is a valid semivariance: one for which
every kriging system is positive definite. An experimental variogram estimated
from a few hundred pairs will violate that requirement routinely, and the
kriging variance computed from it can be negative. The model is the constraint
that makes the estimator well posed.

## 2. Estimating the semivariance

The classical estimator bins the pairs by lag:

$$\hat\gamma(h) = \frac{1}{2N(h)}\sum_{i=1}^{N(h)}
\big(z(x_i) - z(x_i + h)\big)^{2},$$

and its sampling variance is large because the squares of correlated
differences are themselves strongly correlated. Consequences used everywhere:

- **State $N(h)$.** A lag with fewer than about $30$ pairs carries little
  information and should be pooled or dropped.
- **Lag tolerance matters.** With irregular samples, pairs are binned into
  intervals $[h - \delta, h + \delta]$; a narrow tolerance gives noisy points, a
  wide one smears the short-lag shape.
- **The estimator is not robust.** One outlier among $N(h)$ pairs contributes a
  squared difference to the sum, so a single large value inflates every bin it
  touches.

The **Cressie-Hawkins** estimator replaces the mean of squares by a fourth power
of the mean of roots:

$$\hat\gamma_{CH}(h) = \frac{1}{2}\cdot
\frac{\Big(\frac{1}{N(h)}\sum |z(x_i) - z(x_i+h)|^{1/2}\Big)^{4}}
{0.457 + \dfrac{0.494}{N(h)}} ,$$

which is resistant to a small number of large differences and nearly as
efficient as the classical estimator on clean data.

## 3. The standard models

With nugget $C_0$, sill $C$ (so that the total sill is $C_0 + C$) and effective
range $a$:

$$\gamma_{\text{sph}}(h) = C_0 + C\Big[\frac{3h}{2a} -
\frac{1}{2}\Big(\frac{h}{a}\Big)^{3}\Big], \quad h \le a, \qquad
\gamma_{\text{sph}}(h) = C_0 + C, \quad h > a,$$

$$\gamma_{\text{exp}}(h) = C_0 + C\big(1 - e^{-3h/a}\big), \qquad
\gamma_{\text{gauss}}(h) = C_0 + C\big(1 - e^{-3h^{2}/a^{2}}\big).$$

The spherical model reaches its sill **exactly** at $a$ and is the default in
mining geostatistics; the exponential approaches it asymptotically, and the
e-folding length $\lambda = a/3$ is the natural parameter when the covariance is
written $C(h) = C e^{-h/\lambda}$; the Gaussian is extremely smooth at the
origin, which makes kriging with it numerically unstable and produces over-smooth
interpolants. A **nested** model is a sum,
$\gamma(h) = \gamma_1(h) + \gamma_2(h) + \cdots$, used when two scales of
structure are visible.

**Validity.** A function is a valid semivariance only if it is conditionally
negative definite: for every set of locations and every set of weights summing to
zero, $\sum_i\sum_j w_i w_j \gamma(x_i - x_j) \le 0$. The three models above are
valid in one, two and three dimensions; the Gaussian is valid in every dimension,
the exponential in one and two but not in higher dimensions in the form given,
and an arbitrary smooth curve through the points is almost surely invalid.

## 4. Fitting

Weighted least squares minimises

$$W(\theta) = \sum_{k} w_k \big(\hat\gamma(h_k) - \gamma(h_k;\theta)\big)^{2},
\qquad w_k = \frac{N(h_k)}{\gamma(h_k;\theta)^{2}}$$

as the default, because the variance of $\hat\gamma(h_k)$ grows roughly as
$\gamma^{2}/N(h_k)$: the weights make each point contribute inversely to its own
variance and down-weight the long lags where the semivariance is large. Ordinary
least squares ignores that and lets the far lags dominate. Maximum likelihood and
restricted maximum likelihood fit the covariance model to the data directly —
they use every pair, give valid standard errors, and are the choice when the
model is to be compared formally — at a much higher computational cost.

Two artefacts are worth knowing before fitting:

- **The sill-range trade-off.** A larger range with a smaller sill fits almost as
  well as the converse; the two parameters are strongly correlated in the fit,
  and only lags beyond the range break the degeneracy.
- **The nugget absorbs everything short.** Measurement error, support mismatch
  and structure below the sampling interval all appear as a nugget, and they
  cannot be separated from a variogram alone.

## 5. Worked example

The demonstration generates $600$ points every $1\ \mathrm m$ from a field with
sill $1.0$, nugget $0.2$ and effective range $15\ \mathrm m$ in the exponential
convention.

**The experimental variogram.** Selected lags:

| lag (m) | $\hat\gamma$ | pairs | model |
|---|---|---|---|
| 1 | 0.3604 | 599 | 0.3813 |
| 2 | 0.5209 | 598 | 0.5297 |
| 5 | 0.8474 | 595 | 0.8321 |
| 10 | 0.8940 | 590 | 1.0647 |
| 20 | 1.0255 | 580 | 1.1817 |
| 60 | 1.0522 | 540 | 1.2000 |

The short lags track the model closely; the long lags are low, giving an observed
sill of $1.0553$ against the model's $1.2000$. That gap is finite-sample scatter,
not a failure of the model: with a correlation length of about a fifth of the
record the effective sample size is about $30$, and the sample variance of such a
series has a large spread. This is the single most common misreading of a
variogram — treating the sample's variance as the true sill.

**Fitting three models.** Weighted least squares with $w_k = N(h_k)/\hat\gamma_k^{2}$:

| model | nugget $C_0$ | sill $C$ | range $a$ (m) | weighted SSE |
|---|---|---|---|---|
| spherical | 0.3392 | 0.7178 | 13.88 | 178.30 |
| exponential | 0.2357 | 0.8325 | 15.42 | 109.24 |
| Gaussian | 0.3873 | 0.6578 | 9.34 | 204.59 |

The exponential wins with an SSE of $109.24$, half the Gaussian's, and recovers
the true range to within $3\ \%$. The spherical and Gaussian fits achieve
similar total sills ($1.057$ and $1.045$) with quite different nuggets — the
sill-range trade-off made visible. Note too that every fitted total sill
($1.068$, $1.057$, $1.045$) is close to the *observed* sill $1.055$, not to the
true $1.200$: the fit reports the field it was given.

**Robustness.** Adding eight large values spread along the record and refitting
the exponential:

| fit | nugget $C_0$ | sill $C$ | range $a$ (m) |
|---|---|---|---|
| clean data | 0.2357 | 0.8325 | 15.42 |
| classical, with outliers | 0.6091 | 0.7959 | 10.76 |
| Cressie-Hawkins | 0.3213 | 0.9021 | 15.63 |

The classical nugget is inflated by $158\ \%$ and the range shortened by
$30\ \%$, because an outlier contaminates every lag. The Cressie-Hawkins fit
moves the nugget by only $36\ \%$ and the range by $1\ \%$. A nugget that appears
and disappears with a handful of samples is an outlier artefact.

## Assumptions and regime of validity

1. **Stationarity over the fitted region.** A trend makes the variogram rise
   without bound; the fix is a drift model, not a longer range.
2. **Enough pairs per lag.** Under about $30$ pairs, report the count and treat
   the point as weak.
3. **A support that matches the use.** The fitted model describes the data's
   support; using it for another support requires regularisation
   ([21-02-01](01-regionalized-variables.md) §3).
4. **Isotropy, unless tested.** Anisotropy requires a lag vector; a single curve
   is an average over directions.
5. **A valid model form.** Direct estimates are not conditionally negative
   definite; kriging from them can give negative variances.
6. **The nugget is not measurement error alone.** It absorbs short-scale
   structure, and the two cannot be separated without independent error
   information.

## The honest summary

A variogram is an estimate with a large variance, a strong parameter correlation
and a sensitivity to outliers, and it is the object on which every kriging
prediction depends. In the demonstration the exponential model was recovered to
within $3\ \%$ in range, the observed sill was $12\ \%$ below the true one purely
through sampling, and eight injected values inflated the classical nugget by
$158\ \%$ while the robust estimator moved by $36\ \%$. What the numbers do
**not** establish is that a real field is stationary or isotropic: that is
geological reasoning, and the variogram can only fail to contradict it.

## Python demonstration

[`code/variograms_demo.py`](./code/variograms_demo.py) prints every number quoted
above. It:

1. computes and tabulates the experimental semivariogram with pair counts;
2. fits spherical, exponential and Gaussian models by weighted least squares and
   prints the weighted SSE;
3. compares the classical and Cressie-Hawkins estimators with outliers present.

```bash
cd 21-statistics-bayesian-ml/02-geostatistics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python variograms_demo.py
```

It runs in well under a second and prints only text.

## Exercises

Graded problems are in
[`exercises/02-variograms-exercises.md`](./exercises/02-variograms-exercises.md)
with worked solutions in
[`exercises/02-variograms-solutions.md`](./exercises/02-variograms-solutions.md).
The ★★★ problems ask you to design the model-selection and robustness studies.

## Mastery checkpoint

Without notes, an experimental variogram has $\hat\gamma(5) = 0.85$,
$\hat\gamma(20) = 1.03$ and $\hat\gamma(60) = 1.05$, with more than $500$ pairs
at every lag, and an exponential fit gives $C_0 = 0.24$, $C = 0.83$,
$a = 15.4\ \mathrm m$.

1. State the observed sill and explain why it differs from the truth.
2. Convert the fitted range to the e-folding length.
3. Compute the ratio $\hat\gamma(60)/\hat\gamma(5)$ and say what it measures.
4. A colleague fits the Gaussian model instead and reports $a = 9.3\ \mathrm m$.
   State why the shorter range is expected and which model you would trust.

## Common pitfalls

1. **Reading the sample variance as the sill.** Finite-sample scatter is large;
   the observed sill here was $12\ \%$ low.
2. **Fitting strongly correlated parameters and reporting them independently.**
   Sill and range trade off, and the reported pair can be far from the optimum
   ridge.
3. **Using the classical estimator on data with spikes.** It inflated the nugget
   by $158\ \%$.
4. **Treating the nugget as instrument error.** It also contains structure below
   the sampling interval.
5. **Kriging from the raw variogram.** It is not conditionally negative definite
   and can produce negative kriging variances.
6. **Fitting with an isotropic model to anisotropic data.** The fitted range is
   then an average of directions and fits none of them.

## Where this is used

- **Mining and resource estimation**: the variogram is a statutory input to the
  block model.
- **Reservoir modelling**: nested variograms represent depositional and
  diagenetic scales.
- **Soil and precision agriculture**: range sets the sampling interval.
- **Environmental monitoring**: variograms of contaminant concentration decide
  network density.
- **Meteorology and air quality**: spatial covariance models for data
  assimilation.

## Related lessons

- [21-02-01 Regionalised Variables and Spatial Continuity](01-regionalized-variables.md) —
  the stationarity assumptions the estimator needs.
- [21-02-03 Kriging: Simple, Ordinary, Universal, Indicator](03-kriging.md) —
  the estimator that consumes the fitted model.
- [21-02-04 Conditional Simulation and Uncertainty Realisations](04-simulation-geostatistics.md) —
  how a model error propagates into simulated reality.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../01-statistics-in-practice/03-resampling.md) —
  uncertainty for a fitted model.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](../01-statistics-in-practice/01-descriptive-statistics.md) —
  the robustness ideas behind Cressie-Hawkins.

## Self-assessment checklist

- [ ] I can compute an experimental semivariogram and report pair counts.
- [ ] I can write the three standard models and convert range conventions.
- [ ] I can fit by weighted least squares with a stated weight.
- [ ] I can state the conditional-negative-definiteness requirement.
- [ ] I can diagnose the sill-range trade-off and the nugget.
- [ ] I can choose between the classical and robust estimators.
