---
id: 21-02-03
title: "Kriging: Simple, Ordinary, Universal, Indicator"
level: research
prereqs: ["21-02-02", "01-13-03"]
estimated_minutes: 70
tags: [geostatistics, kriging, best-linear-unbiased-prediction, uncertainty, kriging-variance]
---

# Kriging: Simple, Ordinary, Universal, Indicator

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the ordinary-kriging system from the unbiasedness constraint and
   the minimum-variance objective, and **state** what each row enforces.
2. **Compute** kriging weights, prediction and variance, and **interpret** the
   Lagrange multiplier.
3. **Distinguish** simple, ordinary, universal and indicator kriging by the
   assumption each makes about the mean.
4. **Explain** exactness, the screen effect, negative weights and the behaviour
   of the kriging variance, with numbers.
5. **State** why the kriging variance is a model-dependent quantity and not a
   measured error.
6. **Diagnose** misapplication: extrapolation into a drift, a nugget-free model
   on noisy data, and the use of kriging for a non-Gaussian target.

All data in this lesson are **SYNTHETIC**: twelve values from a stated smooth
function, with a stated variogram model. No measured value is used, and the
predictions below constrain only the demonstration's model.

## Prerequisites

- [21-02-02 Variograms, Covariance and Model Fitting](02-variograms.md) —
  the fitted model that kriging consumes.
- [01-13-03 Expectation, Variance and Moments](../../01-mathematics/13-probability-and-statistics-foundations/03-expectation-variance.md) —
  the moment algebra used in the derivation.
- [21-01-04 Linear, Multiple and Robust Regression](../01-statistics-in-practice/04-regression.md) —
  least squares, of which kriging is the spatially correlated generalisation.

## 1. Intuition: a weighted average chosen to be optimal

Kriging is a weighted average of the data with weights chosen so that the
predictor is **unbiased** and has **minimum variance** under the assumed
variogram. Nothing more. It is a best linear unbiased predictor: *linear*
because it is a weighted sum, *unbiased* because the weights are constrained,
and *best* because the weights minimise a variance computed from the model.

That description is worth holding onto, because it tells you exactly what
kriging is not. It is not a physical model, it is not distribution-free beyond
the first two moments, and its output variance is a property of the assumed
variogram rather than of the data. Change the model and the map changes; the
weights are optimal only for the model you supplied.

## 2. The ordinary-kriging system

Let $z_1,\dots,z_n$ be data at locations $x_1,\dots,x_n$ and let $\gamma$ be the
fitted semivariance. The predictor is
$\hat Z(x_0) = \sum_i w_i z_i$. Unbiasedness against an unknown constant mean
requires $\sum_i w_i = 1$. Minimising
$\operatorname{Var}\hat Z(x_0) - Z(x_0)$ subject to that constraint, with the
Lagrange multiplier $2\mu$ (the factor of two is a convention), gives the
$(n+1)\times(n+1)$ system

$$\begin{bmatrix} \Gamma & \mathbf 1 \\ \mathbf 1^{\mathsf T} & 0
\end{bmatrix}
\begin{bmatrix} \mathbf w \\ \mu \end{bmatrix}
=
\begin{bmatrix} \boldsymbol\gamma_0 \\ 1 \end{bmatrix}, \qquad
\Gamma_{ij} = \gamma(x_i - x_j), \quad
(\boldsymbol\gamma_0)_i = \gamma(x_i - x_0),$$

and the **kriging variance** is

$$\sigma^{2}_{K} = \mathbf w^{\mathsf T}\boldsymbol\gamma_0 + \mu .$$

Every row of $\Gamma$ says that the weighted semivariance between the data must
reproduce the semivariance to the target; the last row is the unbiasedness
constraint. The multiplier $\mu$ is the marginal increase in the kriging
variance per unit relaxation of that constraint, and it is what makes
$\sigma^{2}_{K}$ non-negative even when individual weights are negative.

**Simple kriging** replaces the constraint with a known mean $\mu_0$ and
predicts $\hat Z(x_0) = \mu_0 + \mathbf c_0^{\mathsf T}C^{-1}(\mathbf z -
\mu_0\mathbf 1)$ where $C$ is the covariance matrix and $\mathbf c_0$ the
covariance to the target, with
$\sigma^{2}_{SK} = C(0) - \mathbf c_0^{\mathsf T}C^{-1}\mathbf c_0$. The system is
smaller, the estimator is smoother, and it requires a mean the analyst must
supply.

## 3. The properties, with numbers

**Exactness.** Ordinary kriging reproduces the data exactly, whether or not the
variogram has a nugget, because $\mathbf w = \mathbf e_j$ solves the system at
$x_0 = x_j$. The demonstration confirms it twice: at $x = 20\ \mathrm m$ the
prediction is $4.4312\ \mathrm{mGal}$ against a datum of $4.4312$, and the
kriging standard deviation is $0.00000$, with and without a nugget of $0.10$.
Adding a **measurement-error variance** to the diagonal is different: it makes
the estimator a filter, and the residual at a datum becomes $-0.0137\ \mathrm{mGal}$
for an error variance of $0.05$. Exactness is a property of the variogram
formulation, not a universal virtue — over-fitting noisy data is the cost.

**The screen effect.** A cluster of points close together carries the information
of roughly one point, because each is screened by its neighbours. Adding three
points $1\ \mathrm m$ apart near $x = 53\ \mathrm m$ changed the prediction at
$x = 64\ \mathrm m$ from $5.7003$ to $5.7031\ \mathrm{mGal}$ and reduced the
kriging variance from $0.6334$ to $0.6297$ — a $0.6\ \%$ reduction from three
samples. The cluster's combined weight is $0.1177$: real, but far below the
weight three independent samples would carry.

**The kriging variance.** At $x_0 = 62\ \mathrm m$ it is
$0.6483\ \mathrm{mGal^{2}}$, i.e. $0.805\ \mathrm{mGal}$ — the same between the
paired points at $92\ \mathrm m$. Between data it is largest, at the data it is
zero, and a nugget raises it between the data while leaving the exactness
untouched ($0.5993$ to $0.7067\ \mathrm{mGal}$ at $x = 35\ \mathrm m$).

**The weights.** At $x_0 = 62\ \mathrm m$ the two nearest points carry $0.4403$
and $0.3857$, distant points carry $0.0069$–$0.0287$, and the sum is exactly
$1.000000$. No weight is negative here, but they need not be positive in general.

## 4. The variants and when each applies

- **Simple kriging**: the mean is known. Use it when the mean is genuinely known
  from a larger population; on the demonstration's trended profile it differs
  from ordinary kriging by up to $0.03\ \mathrm{mGal}$, because it is given only
  the global mean $5.384\ \mathrm{mGal}$.
- **Ordinary kriging**: the mean is unknown but constant. The default.
- **Universal kriging**: the mean is a low-order drift, $m(x) = \sum_k a_k f_k(x)$;
  the unbiasedness constraint is applied to each basis function. Use it when the
  variogram rises without bound, which is the signature of a trend.
- **Indicator kriging**: krige the indicator $\mathbf 1\{Z(x) \le z_c\}$ to
  estimate $P(Z(x) \le z_c)$; the result need not satisfy the axioms of
  probability and must be order-corrected. Use it for thresholds and for
  strongly non-Gaussian variables.
- **Cokriging**: krige a variable with the help of a correlated, better-sampled
  one, using a cross-covariance model. Use it when a dense secondary
  measurement exists.
- **Block kriging**: predict the mean over a support rather than at a point; the
  right-hand side becomes the average semivariance from the block to each datum
  and to itself.

## 5. Worked example

The demonstration samples $z(x) = 3 + 0.04x + 0.8\sin(x/22)$ at twelve locations
between $0$ and $130\ \mathrm m$, with an exponential variogram model of unit
sill, effective range $40\ \mathrm m$ and a nugget of $0.10$ where stated.

At $x_0 = 62\ \mathrm m$ the prediction is $5.6878\ \mathrm{mGal}$ with kriging
variance $0.6483\ \mathrm{mGal^{2}}$, weights summing to $1.000000$, and the four
largest weights on the neighbouring samples:

| $x_i$ (m) | weight | $z_i$ (mGal) |
|---|---|---|
| 55 | $+0.4403$ | 5.679 |
| 70 | $+0.3857$ | 5.768 |
| 85 | $+0.0287$ | 5.871 |
| 40 | $+0.0277$ | 5.376 |

The two nearest points carry $83\ \%$ of the weight. At the data the prediction
reproduces the value exactly with a zero variance; halfway between two samples
$40\ \mathrm m$ apart the kriging standard deviation is $0.805\ \mathrm{mGal}$,
which is $0.81$ of the total sill standard deviation — that is what "no nearby
data" looks like in the model's own units.

**A caution the table makes visible.** The prediction $5.6878$ lies between the
two neighbouring values $5.679$ and $5.768$, which is what a well-behaved
interpolant should do. Ordinary kriging does not guarantee it: with a variogram
that admits negative weights the interpolant can overshoot, and near the edge of
the data it can extrapolate a local trend. Always check the predictions against
the data range.

## Assumptions and regime of validity

1. **A valid variogram model.** Kriging from a raw experimental variogram can
   produce a negative kriging variance.
2. **Stationary mean over the neighbourhood.** Ordinary kriging is exactly wrong
   across a trend; universal kriging is needed there.
3. **The kriging variance is model-based.** It measures the spread of the
   *assumed* random function, not the spread of the observed errors; if the
   variogram is wrong, so is the variance.
4. **Only first and second moments enter.** Kriging is the best **linear**
   predictor; with non-Gaussian data it is not the best predictor, and the
   Gaussian confidence interval built from $\sigma_K$ is not calibrated.
5. **The support matters.** Point kriging for a block target understates the
   smoothing; use block kriging.
6. **The nugget is not filtered unless modelled as error.** Ordinary kriging is
   exact even with a nugget, so noisy data are interpolated unless an explicit
   error variance is used.

## The honest summary

Kriging is a linear system whose solution is determined entirely by the fitted
variogram, and the demonstration makes both sides of that statement concrete. On
the favourable side, the weights sum to one to six decimals, the estimator is
exact at the data with zero variance, the two nearest samples carry $83\ \%$ of
the weight, and three clustered samples reduce the variance by only $0.6\ \%$ —
the screen effect, measured. On the unfavourable side, the prediction at
$x = 62\ \mathrm m$ is $5.6878$ only because the model says the field has range
$40\ \mathrm m$; a different fitted range gives a different number, and the
kriging variance $0.805\ \mathrm{mGal}$ is a property of that model, not a
measured error. What the numbers do **not** establish is that the confidence
level attached to $\pm 2\sigma_K$ is nominal: that requires approximate
Gaussianity, which the model assumes and the data cannot confirm here.

## Python demonstration

[`code/kriging_demo.py`](./code/kriging_demo.py) prints every number quoted
above. It:

1. builds the ordinary-kriging system and prints the weights at one target;
2. checks exactness with and without a nugget, and the filtering effect of a
   measurement-error variance;
3. measures the screen effect from three clustered samples;
4. compares ordinary kriging with simple kriging and inverse distance weighting.

```bash
cd 21-statistics-bayesian-ml/02-geostatistics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python kriging_demo.py
```

It runs in well under a second and prints only text.

## Exercises

Graded problems are in
[`exercises/03-kriging-exercises.md`](./exercises/03-kriging-exercises.md)
with worked solutions in
[`exercises/03-kriging-solutions.md`](./exercises/03-kriging-solutions.md).
The ★★★ problems ask you to design cross-validation and screen-effect studies.

## Mastery checkpoint

Without notes, sixteen samples give a kriging system with weights
$0.44, 0.39, 0.03, 0.03, \dots$ summing to $1.000000$, a prediction of
$5.69\ \mathrm{mGal}$ and a kriging variance of $0.6483\ \mathrm{mGal^{2}}$.

1. Compute the kriging standard deviation and compare it with the total sill
   standard deviation $\sqrt{1.10}$.
2. State what the Lagrange multiplier would be if the unbiasedness constraint
   were dropped, and what estimator the result would be.
3. Explain why adding three samples $1\ \mathrm m$ apart changed the variance by
   only $0.6\ \%$.
4. A colleague reports the prediction as $5.69 \pm 2(0.805)\ \mathrm{mGal}$ as a
   $95\ \%$ confidence interval. State the two assumptions they have added
   without saying so.

## Common pitfalls

1. **Reading $\sigma_K$ as a measured error.** It is a model quantity; the
   demonstration's value depends on a stated range and nugget.
2. **Treating negative weights as a bug.** They are a legitimate feature of the
   optimal predictor and a signal of clustered or unevenly spaced data.
3. **Kriging across a trend with an ordinary system.** The prediction is then
   biased and the variance too small.
4. **Using an exact interpolant on noisy data.** Ordinary kriging honours a
   nugget-free model exactly, including its noise.
5. **Reporting weights without the constraint check.** $\sum w_i = 1$ is the only
   cheap self-test of the system.
6. **Assuming Gaussian intervals.** The $\pm 2\sigma_K$ interval is calibrated
   only for a Gaussian random function.

## Where this is used

- **Resource estimation**: grade interpolation and its conditional variance.
- **Environmental mapping**: soil, groundwater and contaminant surfaces with
  uncertainty.
- **Meteorology**: optimal interpolation in data assimilation.
- **Geodesy**: least-squares collocation of gravity and geoid data, which is
  kriging under another name.
- **Reservoir modelling**: the kriged trend of a property before simulation adds
  the texture.

## Related lessons

- [21-02-02 Variograms, Covariance and Model Fitting](02-variograms.md) —
  the input model and its uncertainty.
- [21-02-04 Conditional Simulation and Uncertainty Realisations](04-simulation-geostatistics.md) —
  why a kriged map plus a variance is not a set of plausible reality.
- [21-02-05 Geostatistics Combined with Geophysical Inversion](05-geostatistics-inversion.md) —
  kriging expressed as a Bayesian inverse problem.
- [18-02-06 Data Weighting and Error Covariance Specification](../../18-inverse-problems/02-linear-inverse-problems/06-weighting-and-covariance.md) —
  the inverse-theory view of the same weighted system.
- [21-01-04 Linear, Multiple and Robust Regression](../01-statistics-in-practice/04-regression.md) —
  the uncorrelated-noise special case.

## Self-assessment checklist

- [ ] I can write the ordinary-kriging system and the kriging variance.
- [ ] I can explain the unbiasedness constraint and the Lagrange multiplier.
- [ ] I can state the difference between simple, ordinary and universal kriging.
- [ ] I can demonstrate exactness and the screen effect with numbers.
- [ ] I can state why the kriging variance is model-dependent.
- [ ] I can name the assumptions behind a Gaussian confidence interval on a
      kriged prediction.
