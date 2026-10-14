---
id: 21-01-03
title: "Resampling: Bootstrap, Jackknife, Permutation Tests"
level: graduate
prereqs: ["01-13-05", "01-13-07"]
estimated_minutes: 60
tags: [statistics, resampling, bootstrap, jackknife, permutation-test, uncertainty]
---

# Resampling: Bootstrap, Jackknife, Permutation Tests

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the plug-in principle and **construct** a bootstrap resample of a
   sample for any statistic.
2. **Compute** a percentile bootstrap interval and **explain** which quantity it
   is an interval for.
3. **Derive** the jackknife bias and variance estimators and **show** that the
   jackknife bias of a sample mean is identically zero.
4. **Run** a permutation test for a two-sample difference and **state** the
   exchangeability assumption it rests on.
5. **Diagnose** the situations in which the bootstrap fails — extreme order
   statistics, dependent data, very small samples.
6. **Distinguish** the Monte-Carlo error of a resampling estimate from the
   statistical uncertainty it is estimating.

Every sample in this lesson is **SYNTHETIC**: $100$ draws from a standard
lognormal, plus two Gaussian groups for the permutation test. No measured value
enters, and no number quoted below constrains a real data set.

## Prerequisites

- [01-13-05 Sampling Distributions, Law of Large Numbers and CLT](../../01-mathematics/13-probability-and-statistics-foundations/05-sampling-and-clt.md) —
  the sampling distribution the bootstrap estimates.
- [01-13-07 Confidence Intervals and Their Correct Interpretation](../../01-mathematics/13-probability-and-statistics-foundations/07-confidence-intervals.md) —
  what an interval is an interval **for**.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](01-descriptive-statistics.md) —
  the estimators whose uncertainty is being measured.

## 1. Intuition: substitute the sample for the population

Every classical interval needs a formula for the standard error, and every
formula assumes a distribution. The bootstrap removes that need by one
substitution: **use the empirical distribution in place of the unknown
population**. If the sample is a good stand-in for the population, then
resampling from the sample imitates sampling from the population, and the
scatter of the statistic across resamples estimates its scatter across
populations.

That is the entire idea, and it is powerful: it gives an uncertainty for
statistics that have no closed-form error, such as a median, a ratio of means,
or a variogram range. It is also fragile in exactly the places where the
substitution is poor — extremes, dependent samples, and very small $n$ — and
those failures are the substance of Section 5.

## 2. The bootstrap

Given a sample $x_1,\dots,x_n$, draw a **resample** $x^*_1,\dots,x^*_n$ by
sampling $n$ times **with replacement** from the original values, and recompute
the statistic:

$$\hat\theta^{*}_b = T(x^{*}_1,\dots,x^{*}_n), \qquad b = 1,\dots,B .$$

The bootstrap estimate of the standard error is the sample standard deviation of
the $B$ replicates, $\widehat{\mathrm{se}}^* = \mathrm{sd}(\hat\theta^{*}_b)$.
The **percentile interval** at level $1-\alpha$ is the pair of order statistics
matching the $\alpha/2$ and $1-\alpha/2$ quantiles of $\{\hat\theta^{*}_b\}$.
This interval is asymmetric whenever the bootstrap distribution is skewed, which
is one of its advantages over the symmetric formula
$\hat\theta \pm z_{1-\alpha/2}\,\widehat{\mathrm{se}}^*$.

The Monte-Carlo error of the interval endpoints is separate from the statistical
uncertainty: with $B$ replicates the endpoint quantile has an error of order
$\sqrt{p(1-p)/B}$ divided by the density of the bootstrap distribution at that
point, so $B = 10^4$ is enough for two-decimal reporting and $B = 10^3$ is not.

## 3. The jackknife

The jackknife omits one observation at a time and measures the change. Let
$\hat\theta_{(i)}$ be the statistic computed with observation $i$ removed, and
$\bar\theta_{(\cdot)} = \frac1n\sum_i \hat\theta_{(i)}$. Then

$$\widehat{\text{bias}}_{\text{jack}}
= (n-1)\big(\bar\theta_{(\cdot)} - \hat\theta\big), \qquad
\widehat{\mathrm{se}}_{\text{jack}}^2
= \frac{n-1}{n}\sum_{i=1}^{n}\big(\hat\theta_{(i)} - \bar\theta_{(\cdot)}\big)^2 .$$

The bias estimate targets the $\mathcal O(1/n)$ bias of $\hat\theta$. For the
sample mean the estimate is **exactly zero**, because the mean is linear in the
data: leaving out $x_i$ changes the mean by $({\bar x} - x_i)/(n-1)$, and the sum
of those changes cancels. This is why the demonstration prints $+0.000e+00$ for
the mean and $\approx 10^{-14}$ (numerical zero) for the median.

The jackknife is cheap — $n$ evaluations — and it fails for non-smooth
statistics such as the median in small samples, where the leave-one-out values
are coarse. Its median standard error is therefore not comparable with the
bootstrap's, as Section 6 shows.

## 4. Permutation tests

A permutation test asks how surprising the observed difference is under the
sharp null that the two groups are **exchangeable**. Pool the $n_A + n_B$
observations, split them at random into groups of the original sizes, and record
the statistic. The $p$-value is

$$p = \frac{1 + \#\{b : |T^{*}_b| \ge |T_{\text{obs}}|\}}{B + 1},$$

the $+1$ in numerator and denominator making the test valid at any $B$ (it can
never report $p = 0$). Permutation tests require no distributional assumption
beyond exchangeability, but they are **not** assumption-free: a difference in
dispersion between groups violates exchangeability just as a difference in level
does, and the test then answers the wrong question.

## 5. Where resampling fails

1. **Extreme order statistics.** The maximum of a resample is either the sample
   maximum or smaller. Its bootstrap distribution has an atom of size
   $1-(1-1/n)^n \to 1-e^{-1} \approx 0.632$ at the sample maximum, so the upper
   endpoint of any percentile interval is pinned to the largest observation. For
   $n = 100$ the atom is exactly $1-(1-1/100)^{100} = 0.634$.
2. **Dependent data.** Resampling individual points destroys the correlation
   structure. The correct resample blocks (moving-block or stationary bootstrap)
   or model-based residuals.
3. **Small $n$.** The empirical distribution is a coarse stand-in; with ten
   observations the bootstrap has ten distinct values to draw from and badly
   misstates the tail.
4. **Parameters at a boundary.** Quantile estimates near $0$ or $1$, or any
   statistic whose sampling distribution is non-regular, need the $m$-out-of-$n$
   bootstrap or a different device.

## 6. Worked example

The demonstration draws $n = 100$ standard-lognormal values and uses $B = 10^4$.

**Percentile intervals.** The mean is $\bar x = 1.4339$ a.u. with bootstrap
standard error $0.1404$ and interval $[1.1688, 1.7151]$ (width $0.5463$). The
median is $\tilde x = 0.8558$ a.u. with standard error $0.1478$ and interval
$[0.6877, 1.2108]$ (width $0.5231$). The widths differ by only $4\ \%$, but the
bootstrap distributions do not: the mean's skewness is $+0.111$ and the median's
$+0.905$. The median's interval is visibly asymmetric about the point estimate
(it is not $0.8558 \pm 0.26$), which is exactly the case a symmetric formula
misreports.

**Jackknife.** The bias estimate is $+0.000$ for the mean and $+1.099\times
10^{-14}$ for the median — numerical zero in both cases at this sample size. The
jackknife standard errors are $0.1412$ for the mean, within $0.6\ \%$ of the
bootstrap's $0.1404$, and $0.3056$ for the median, more than **twice** the
bootstrap's $0.1478$. The mean's smoothness makes the jackknife reliable; the
median's non-smoothness makes it not.

**Permutation test.** Two groups of $30$ have observed mean difference
$-0.5086$ a.u.; $5000$ shuffles give $p = 0.0480$, and Welch's $t$ test on the
same data gives $t = -2.0108$, $p = 0.0491$. The two $p$-values agree to
$0.001$, which is the expected behaviour when the Gaussian approximation is
adequate at $n_A = n_B = 30$; the permutation value is the one that does not
depend on that adequacy.

**Failure.** The sample maximum is $7.0013$ a.u. Its bootstrap interval is
$[4.8647, 7.0013]$, and $63.5\ \%$ of the $10\,000$ bootstrap maxima equal the
sample maximum exactly — the $0.634$ atom predicted in Section 5. The upper
endpoint can never exceed $7.0013$, so the interval is one-sided and understates
the uncertainty; it must not be reported as a confidence interval.

## Assumptions and regime of validity

1. **The sample is i.i.d. from the population of interest.** The plug-in
   substitution fails the moment the observations are correlated or the sample
   is biased.
2. **The statistic is a smooth functional of the empirical distribution,**
   except where a special method (block, subsampling, $m$-out-of-$n$) is used.
3. **$n$ is not tiny.** Below about $n = 20$ the empirical CDF is too coarse for
   the body, let alone the tail.
4. **$B$ is large enough that Monte-Carlo error is small compared with
   statistical uncertainty** — reported separately.
5. **Exchangeability for permutation tests.** The null hypothesis is that the
   labels carry no information about the values.

## The honest summary

Resampling replaces a distributional assumption with computation, and it is
honest about what it does: the interval it produces is an interval for the
statistic under repeated sampling from **the empirical distribution**, which is
only as good a stand-in for the population as the sample is. On the skewed
synthetic sample above it recovers the mean's standard error to within a per
cent and exposes the median's skewed sampling distribution, which no symmetric
formula would show. It fails visibly and predictably at the extremes, where the
answer is pinned to the largest observation. What the demonstration does **not**
establish is that any of these intervals is correct for real data: that requires
the i.i.d. assumption, which resampling takes as given.

## Python demonstration

[`code/resampling_demo.py`](./code/resampling_demo.py) prints every number
quoted above. It:

1. builds percentile bootstrap intervals for the mean and the median and prints
   their widths and skewness;
2. computes jackknife bias and standard error for both;
3. runs a $5000$-shuffle permutation test beside a Welch $t$ test;
4. shows the bootstrap's failure on the sample maximum.

```bash
cd 21-statistics-bayesian-ml/01-statistics-in-practice/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resampling_demo.py
```

It runs in about half a second and prints only text.

## Exercises

Graded problems are in
[`exercises/03-resampling-exercises.md`](./exercises/03-resampling-exercises.md)
with worked solutions in
[`exercises/03-resampling-solutions.md`](./exercises/03-resampling-solutions.md).
The ★★★ problems ask you to design a block bootstrap and a coverage study.

## Mastery checkpoint

Without notes, a sample of $n = 50$ shear-wave speeds has mean
$3.20\ \mathrm{km/s}$, bootstrap standard error $0.08\ \mathrm{km/s}$ and
bootstrap skewness $+1.4$, with a percentile interval
$[3.05, 3.44]\ \mathrm{km/s}$.

1. State the interval's endpoints and explain why it is not symmetric about the
   point estimate.
2. Compute the implied jackknife bias if the leave-one-out mean is
   $3.199\ \mathrm{km/s}$.
3. Give the exact bootstrap atom at the sample maximum for $n = 50$.
4. A colleague reports $3.20 \pm 0.16\ \mathrm{km/s}$. What is wrong, and what
   would you ask for?

## Common pitfalls

1. **Reporting a bootstrap interval for an extreme.** The upper endpoint is
   glued to the largest observation.
2. **Resampling dependent data pointwise.** It destroys the autocorrelation that
   carries the information.
3. **Confusing $B$ with $n$.** Increasing $B$ reduces Monte-Carlo error only; it
   does not buy statistical precision.
4. **Treating the percentile interval as exact.** It has a coverage error of
   order $n^{-1/2}$; the basic and BCa intervals correct parts of it.
5. **Using a permutation test to compare dispersions.** Exchangeability fails
   under a dispersion difference, and the test then has the wrong null.
6. **Quoting a jackknife standard error for a non-smooth statistic.** For the
   median it overestimated the bootstrap value by a factor of $2.07$ here.

## Where this is used

- **Seismic hazard**: bootstrap intervals for $b$-values and recurrence times.
- **Geochemistry**: resampling assays to propagate sampling and analytical
  error into a resource statement.
- **Regression in geophysics**: block bootstrap for autocorrelated residuals in
  potential-field and time-series fits.
- **Machine learning evaluation**: the bootstrap is the basis of out-of-bag and
  .632 estimates of generalisation error.
- **Model comparison**: permutation tests for whether one model's residuals
  differ from another's.

## Related lessons

- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](01-descriptive-statistics.md) —
  the robust estimators whose uncertainty is measured here.
- [21-01-04 Linear, Multiple and Robust Regression](04-regression.md) — the
  bootstrap applied to fitted coefficients.
- [21-01-05 Nonparametric Statistics and Kernel Density Estimation](05-nonparametric-methods.md) —
  the rank-based alternative to resampling.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../04-machine-learning-fundamentals/03-model-assessment.md) —
  resampling for model assessment, where dependence matters most.
- [01-13-08 Hypothesis Testing, p-Values and Power](../../01-mathematics/13-probability-and-statistics-foundations/08-hypothesis-testing.md) —
  the framework the permutation $p$-value belongs to.

## Self-assessment checklist

- [ ] I can construct a bootstrap resample and compute its statistic.
- [ ] I can build and interpret a percentile interval.
- [ ] I can compute a jackknife bias and standard error and say when each fails.
- [ ] I can run and interpret a permutation test.
- [ ] I can state the three conditions under which resampling fails.
- [ ] I can separate Monte-Carlo error from statistical uncertainty.
