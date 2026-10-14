---
id: 21-01-04
title: "Linear, Multiple and Robust Regression"
level: advanced
prereqs: ["01-13-06", "01-13-07"]
estimated_minutes: 60
tags: [statistics, regression, least-squares, robust-regression, leverage, collinearity]
---

# Linear, Multiple and Robust Regression

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the ordinary least-squares estimator from the normal equations and
   **write** its covariance matrix.
2. **Compute** coefficient standard errors, $R^2$ and the residual variance, and
   **state** the assumption each rests on.
3. **Compute** the leverage $h_{ii}$ of each observation and Cook's distance,
   and **decide** which observations drive a fitted model.
4. **Explain** how collinearity inflates coefficient standard errors through the
   variance-inflation factor, and **diagnose** it.
5. **Formulate** a Huber M-estimator and **solve** it by iteratively reweighted
   least squares.
6. **Compare** OLS and a robust fit on the same data and **state** which
   coefficients each one is estimating.

All data in this lesson are **SYNTHETIC**: a gravity-like profile generated as
$y = 2.0 + 0.5x$ plus Gaussian noise, with one outlying observation added by
hand. No measured gravity value is used, and the fitted numbers constrain only
the demonstration's model.

## Prerequisites

- [01-13-06 Point Estimation, Bias, Consistency and Efficiency](../../01-mathematics/13-probability-and-statistics-foundations/06-estimation-theory.md) —
  the estimator theory behind least squares.
- [01-13-07 Confidence Intervals and Their Correct Interpretation](../../01-mathematics/13-probability-and-statistics-foundations/07-confidence-intervals.md) —
  the coefficient intervals in Section 3.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](01-descriptive-statistics.md) —
  the robustness language this lesson extends to models.

## 1. Intuition: a regression is a weighted average of the data

A straight-line fit is easiest to understand as a competition between
observations. Each point pulls the line towards itself, and the strength of the
pull is its **leverage**: how far its $x$-value sits from the centre of the
design. A point at the edge of the $x$-range has a long lever arm and can rotate
the line; a point in the middle can only translate it. When a point has both
high leverage and a large residual, it can move the line arbitrarily, and the
ordinary least-squares residual it leaves behind is *small* — which is why no
residual plot will find it for you.

The rest of the lesson makes these statements quantitative and then introduces
the alternative: replace the squared error, which lets one residual dominate,
with a loss that grows linearly beyond a threshold.

## 2. Ordinary least squares

Write the model $y = X\beta + \varepsilon$ with $X$ an $n\times p$ design matrix
(including a column of ones) and $\mathbb E[\varepsilon] = 0$,
$\operatorname{Cov}(\varepsilon) = \sigma^2 I$. Minimising
$J(\beta) = \|y - X\beta\|^2$ gives the **normal equations**
$X^{\mathsf T}X\hat\beta = X^{\mathsf T}y$, hence

$$\hat\beta = (X^{\mathsf T}X)^{-1}X^{\mathsf T}y, \qquad
\operatorname{Cov}(\hat\beta) = \sigma^{2}(X^{\mathsf T}X)^{-1}.$$

With $p$ parameters the unbiased estimate of $\sigma^{2}$ is
$s^{2} = \mathrm{RSS}/(n - p)$, where $\mathrm{RSS} = \sum_i (y_i - \hat y_i)^2$,
so the standard error of $\hat\beta_j$ is $s$ times the square root of the
$j$-th diagonal entry of $(X^{\mathsf T}X)^{-1}$. The coefficient of
determination is

$$R^{2} = 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}}, \qquad
\mathrm{TSS} = \sum_i (y_i - \bar y)^2,$$

and $R^{2}$ never decreases when a predictor is added, which is why the adjusted
$R^{2}$ is reported for comparisons.

## 3. Leverage, influence and Cook's distance

The fitted values are $\hat y = Hy$ with the hat matrix
$H = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}$. Its diagonal entries

$$h_{ii} = x_i^{\mathsf T}(X^{\mathsf T}X)^{-1}x_i, \qquad
\sum_i h_{ii} = p, \qquad \frac1n \le h_{ii} \le 1,$$

are the **leverages**. The average is $p/n$, so in the demonstration's
$p = 2$, $n = 101$ fit the average is $2/101 = 0.0198$ and a common rule of
thumb flags $h_{ii} > 2p/n = 0.0396$.

Leverage alone is not influence: a high-leverage point that lies on the trend
changes nothing. **Cook's distance** combines leverage with the residual,

$$D_i = \frac{r_i^{2}}{p\,s^{2}}\cdot\frac{h_{ii}}{(1 - h_{ii})^{2}},$$

and measures how far $\hat\beta$ moves when observation $i$ is deleted. The
conventional threshold is $4/n$; in the demonstration one point exceeds it by
a factor of $82$.

## 4. Collinearity and the variance-inflation factor

If predictor $j$ is well explained by the other predictors, with $R_j^{2}$ the
$R^{2}$ of that auxiliary regression, then

$$\operatorname{Var}(\hat\beta_j)
= \frac{\sigma^{2}}{(1-R_j^{2})\sum_i (x_{ij}-\bar x_j)^{2}}, \qquad
\mathrm{VIF}_j = \frac{1}{1 - R_j^{2}} .$$

Collinearity does not bias the point estimates; it inflates their standard
errors by $\sqrt{\mathrm{VIF}}$, and it makes the individual coefficients
unstable because the design cannot separate their contributions. The remedy is
to remove or combine the redundant predictor, or to reparameterise, not to hope
that a bigger sample will help — the VIF is a property of the design.

## 5. Robust regression

The least-squares estimator has an unbounded influence function, for the same
reason the mean does. A robust alternative minimises a loss $\rho$ that is
quadratic near zero and linear beyond:

$$\hat\beta = \arg\min_\beta \sum_i \rho\!\left(\frac{r_i}{s}\right), \qquad
\rho(u) = \begin{cases} u^{2}/2, & |u| \le c,\\[2pt]
c|u| - c^{2}/2, & |u| > c,\end{cases}$$

Huber's loss with tuning constant $c = 1.345$, which gives $95\ \%$ efficiency
at the Gaussian. Setting the derivative to zero gives the estimating equation
$\sum_i \psi(r_i/s)\,x_i = 0$ with
$\psi(u) = \operatorname{sign}(u)\min(|u|, c)$, which is a **weighted** least
squares problem with weights $w_i = \psi(r_i/s)/(r_i/s)$. The weights depend on
the residuals, so the solution is found by **iteratively reweighted least
squares**: fit, form weights from the residuals and a robust scale (here
$s = 1.4826\,\mathrm{MAD}$), refit, repeat until the coefficients stop moving.

## 6. Worked example: the synthetic gravity profile

The profile is $y = 2.0 + 0.5x$ with $x = 0,\dots,99\ \mathrm{km}$ and
$\mathcal N(0, 1^2)\ \mathrm{mGal}$ noise, plus one point at
$(120\ \mathrm{km}, 20\ \mathrm{mGal})$.

**Clean OLS.** Intercept $1.975 \pm 0.193\ \mathrm{mGal}$, slope
$0.4989 \pm 0.0034\ \mathrm{mGal/km}$, $R^{2} = 0.9956$, residual variance
$s^{2} = 0.944\ \mathrm{mGal^{2}}$. The slope's standard error is $0.0034$, i.e.
$0.7\ \%$ of the value, as expected from $\sigma/\sqrt{\sum(x_i-\bar x)^2}$.

**One point.** Adding the single observation gives intercept
$3.222 \pm 0.820\ \mathrm{mGal}$ and slope $0.4658 \pm 0.0141\ \mathrm{mGal/km}$.
The slope is now wrong by $6.8\ \%$ of the truth, against $0.22\ \%$ for the
clean fit, and its standard error has inflated by a factor of $4.1$. The
residual of the added point is *not* the largest in the fit — which is why
residual inspection misses it — but its leverage $h_{ii} = 0.0651$ is $3.3$
times the average and its Cook's distance is $3.263$ against a threshold of
$0.0396$. The largest Cook's distance among the other $100$ points is $0.0192$.

**Robust fit.** Huber's estimator on the same $101$ points gives intercept
$2.078\ \mathrm{mGal}$ and slope $0.4967\ \mathrm{mGal/km}$ — an error of
$0.7\ \%$, ten times smaller than OLS. It down-weights exactly one point, the
injected one, to a weight of $0.0348$.

**Collinearity.** With $n = 200$, $x_1$ standard normal, the truth
$y = 1 + 2x_1 + 3x_2 + \mathcal N(0, 0.5^2)$: an independent $x_2$ gives
$\hat\beta_1 = 2.002 \pm 0.032$, $\hat\beta_2 = 3.015 \pm 0.035$, and
$\mathrm{VIF} = 1.0$. Making $x_2 = x_1 + 0.05\,\eta$ raises the correlation to
$0.9987$, the VIF to $375.5$, and the standard errors to $0.682$ and $0.684$ —
large enough that neither coefficient is distinguishable from zero, even though
$R^{2} = 0.9903$.

## Assumptions and regime of validity

1. **Linearity.** The model is a straight line (or a stated basis); a curvature
   error appears as a pattern in the residuals and is not fixed by robustness.
2. **Independent errors.** Autocorrelated residuals invalidate the standard
   errors and the leverage arithmetic; use a block bootstrap
   ([21-01-03](03-resampling.md)) or generalised least squares.
3. **Exogeneity.** $X$ is fixed or independent of $\varepsilon$; correlated
   predictors and errors bias $\hat\beta$ itself, not only its variance.
4. **Common $\sigma^{2}$.** Heteroscedasticity makes $s^2$ and Cook's distance
   wrong; use robust or weighted least squares.
5. **The Huber constant is a choice.** $c = 1.345$ targets $95\ \%$ Gaussian
   efficiency; a smaller $c$ is more resistant and less efficient.
6. **$R^{2}$ is not a validation.** A model can have $R^{2}$ close to one and be
   wrong out of sample; see
   [21-04-02 Bias-Variance](../04-machine-learning-fundamentals/02-bias-variance.md).

## The honest summary

Ordinary least squares is the efficient estimator under exactly Gaussian
errors, and a single outlying observation can destroy it while leaving a
residual plot clean. The demonstration is a controlled case: one point at
$120\ \mathrm{km}$ moved the slope by $6.8\ \%$ and inflated its standard error
by $4.1$, and a Huber fit recovered the slope to $0.7\ \%$. Collinearity is the
second failure mode, and it is invisible in the point estimates: the
coefficients looked plausible while their standard errors grew by a factor of
$21$. What these numbers do **not** establish is that any particular field data
set is Gaussian, independent or linear — those are the assumptions that must be
argued before the intervals mean anything.

## Python demonstration

[`code/regression_demo.py`](./code/regression_demo.py) prints every number
quoted above. It:

1. fits OLS with and without the outlying point;
2. solves the Huber M-estimator by IRLS and reports the weights;
3. fits a collinear and an independent multiple regression and prints the VIF;
4. computes leverages and Cook's distances.

```bash
cd 21-statistics-bayesian-ml/01-statistics-in-practice/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python regression_demo.py
```

It runs in well under a second and prints only text.

## Exercises

Graded problems are in
[`exercises/04-regression-exercises.md`](./exercises/04-regression-exercises.md)
with worked solutions in
[`exercises/04-regression-solutions.md`](./exercises/04-regression-solutions.md).
The ★★★ problems ask you to design the influence and cross-validation
experiments.

## Mastery checkpoint

Without notes, for a simple linear fit with $n = 25$ points and $p = 2$
parameters: the slope is $\hat\beta_1 = 0.4989$ with standard error $0.0034$,
and one observation has $h_{ii} = 0.42$ and a standardised residual of $-2.5$.

1. Compute Cook's distance for that observation.
2. Decide whether it exceeds the conventional threshold and say what you would
   do next.
3. State whether the leverage alone motivates action.
4. Give the ratio of the coefficient standard errors if a VIF of $375.5$ were
   introduced.

## Common pitfalls

1. **Judging influence by the residual size.** A high-leverage point absorbs its
   own residual, so the largest residual is often not the influential point.
2. **Deleting points because they are influential.** Influence is a question,
   not a verdict; a genuine outlier can be the most informative observation.
3. **Reporting $R^{2}$ as fit quality.** Adding predictors raises it without
   improving prediction.
4. **Interpreting collinear coefficients.** Individually they are unstable and
   individually meaningless; their sum is what the data support.
5. **Using standard errors from a wrong model.** Autocorrelation and
   heteroscedasticity inflate them beyond the printed values.
6. **Assuming robustness overcomes nonlinearity.** Huber's estimator is still a
   linear model; it is robust to outliers, not to curvature.

## Where this is used

- **Potential-field interpretation**: linear and multilinear regressions of
  gravity or magnetic anomalies against a regional trend.
- **Geothermics**: heat-flow versus heat-production regression with its
  characteristic correlated errors.
- **Petrophysics**: multi-log regressions to predict porosity or permeability,
  where collinear logs are the norm.
- **Deformation monitoring**: velocity estimation from a linearised time series
  with robust weights.
- **Calibration**: instrument response fitted to reference values, where a
  single bad calibration point otherwise dominates.

## Related lessons

- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](01-descriptive-statistics.md) —
  the scalar robust statistics behind the vector estimator.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](03-resampling.md) —
  uncertainty for regression under dependence.
- [21-04-02 Bias-Variance Trade-Off](../04-machine-learning-fundamentals/02-bias-variance.md) —
  why in-sample fit is not predictive skill.
- [21-04-04 Regularisation: Ridge, Lasso, Early Stopping](../04-machine-learning-fundamentals/04-regularization-ml.md) —
  what to do when collinearity cannot be removed.
- [18-02-03 The Generalised Inverse and Its Properties](../../18-inverse-problems/02-linear-inverse-problems/03-generalized-inverse.md) —
  the same estimator seen from inverse theory.

## Self-assessment checklist

- [ ] I can derive $\hat\beta$ and write $\operatorname{Cov}(\hat\beta)$.
- [ ] I can compute $R^{2}$, adjusted $R^{2}$ and the residual variance.
- [ ] I can compute a leverage and Cook's distance and act on them.
- [ ] I can compute and interpret a VIF.
- [ ] I can set up and iterate a Huber M-estimator.
- [ ] I can state which assumptions no robustness property removes.
