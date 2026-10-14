---
id: 01-13-03
title: "Expectation, Variance and Moments"
level: intermediate
prereqs: ["01-13-02", "01-05-05"]
estimated_minutes: 90
tags: [expectation, variance, moments, covariance, standard-error, averaging]
---

# Expectation, Variance and Moments

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the expectation of a discrete and of a continuous random variable
   from its PMF or PDF, and interpret it as a weighted average rather than as the
   most likely value.
2. **Use** the law of the unconscious statistician, $E[g(X)] = \int g(x)f_X(x)\,dx$,
   without first deriving the distribution of $g(X)$.
3. **Prove** that expectation is linear, and demonstrate that linearity requires no
   independence assumption while the corresponding variance rule does.
4. **Derive** $\operatorname{Var}(X) = E[X^2] - (E[X])^2$ and
   $\operatorname{Var}(aX+b) = a^2\operatorname{Var}(X)$, and explain why the
   standard deviation, not the variance, carries the units of the measurement.
5. **Compute** covariance and correlation, and use
   $\operatorname{Var}(X+Y) = \operatorname{Var}X + \operatorname{Var}Y +
   2\operatorname{Cov}(X,Y)$ to decide whether combining two estimates is worth
   doing.
6. **Derive** the standard error of a mean, $\sigma/\sqrt{n}$, state the
   independence assumption on which it rests, and compute the point at which a
   shared systematic error makes further averaging useless.
7. **State** which moments exist for a given distribution, and recognise that a
   missing fourth moment makes even a well-defined variance hard to estimate.

## Prerequisites

[01-13-02 Random Variables, PMFs, PDFs and CDFs](./02-random-variables.md) for
distributions and the probability integral transform, and
[01-05-05 Integration Techniques and Definite Integrals](../05-single-variable-calculus/05-integration.md)
for evaluating the integrals that define continuous moments.

## 1. Expectation is a weighted average

The **expectation** of a random variable is its probability-weighted average:

$$
E[X] = \begin{cases}
\displaystyle \sum_x x\,p_X(x), & X \text{ discrete},\\[2mm]
\displaystyle \int_{-\infty}^{\infty} x\,f_X(x)\,dx, & X \text{ continuous}.
\end{cases}
$$

Three remarks that prevent a great deal of confusion:

- It is an average over the *distribution*, not over a sample, and not over time.
  The sample mean of $n$ observations is a different object — a random variable in
  its own right — and lesson 05 is about how the two are related.
- It is not generally the most probable value. The exponential distribution has
  its maximum density at $0$ and its mean at $1/\lambda$; for a bimodal
  distribution the mean may sit in a region of very low probability.
- It need not exist. If the integral does not converge absolutely, $E[X]$ is
  undefined, not infinite in any useful sense. The Pareto distribution with tail
  exponent $\alpha \le 1$ is the standard example, and lesson 02 showed what a
  divergent mean does to a running average.

For a function of a random variable, the **law of the unconscious statistician**
saves the trouble of deriving the distribution of $g(X)$ first:

$$E[g(X)] = \sum_x g(x) p_X(x) \quad \text{or} \quad
E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x)\,dx.$$

This is why the expectation of $1/V$ in an uncertainty calculation can be
computed without ever writing the density of $1/V$.

### 1.1 Two expectations evaluated

The demonstration computes both integrals directly:

```
  Poisson(3.2): E = 3.200000, Var = 3.200000  (both equal lambda = 3.2)
  Exponential(2): E = 0.500000 (= 1/lambda = 0.500000), Var = 0.250000 (= 1/lambda^2 = 0.250000)
```

The Poisson mean and variance agree with each other, and the exponential moments
with $1/\lambda$ and $1/\lambda^{2}$. Computing a moment from a density by
quadrature and comparing with a closed form is a habit worth forming: it catches
sign errors, missing jacobians, and mis-specified parameters in one gesture.

## 2. Linearity of expectation

For random variables $X$ and $Y$ and constants $a$, $b$,

$$E[aX + bY] = aE[X] + bE[Y],$$

with **no assumption whatsoever about dependence**. The proof for discrete
variables is a rearrangement of a double sum:

$$
E[X + Y] = \sum_x \sum_y (x+y)\,p_{X,Y}(x,y)
= \underbrace{\sum_x x \sum_y p_{X,Y}(x,y)}_{p_X(x)}
+ \underbrace{\sum_y y \sum_x p_{X,Y}(x,y)}_{p_Y(y)}
= E[X] + E[Y].
$$

The inner sums are the marginal PMFs, so the joint distribution collapses and
dependence never enters.

This is the single most useful algebraic fact in the whole of statistics, and it
is worth pausing on why. It means the expectation of a sum of many terms can be
computed from the expectations of the terms even when the terms are correlated,
coupled, or causally entangled. In geophysics it is why a modelled
phase-shift accumulation can be averaged piecewise over a heterogeneous path, why
a stack of correlated traces has an expectation that is the sum of its
expectations, and why the mean of a model output can sometimes be propagated
analytically through a linear forward operator.

The demonstration verifies it on strongly dependent data:

```
  E[X]     = 6.000196
  E[Y]     = 4.801177
  E[X + Y] = 10.801374  (= E[X] + E[Y] = 10.801374)
```

$Y$ here is constructed as $0.8X + \text{noise}$, so $X$ and $Y$ are correlated by
construction, and the identity still holds exactly.

**One caution.** Linearity concerns the *expectation*, not the distribution. The
distribution of $X + Y$ depends entirely on the dependence between $X$ and $Y$;
only its mean is insensitive to it.

## 3. Variance

The **variance** measures spread about the mean:

$$\operatorname{Var}(X) = E\bigl[(X - E[X])^2\bigr].$$

The square makes it non-negative and makes the algebra of independent
combinations simple; the cost is that it is measured in squared units. The
**standard deviation** $\sigma_X = \sqrt{\operatorname{Var}(X)}$ restores the
units, and it, not the variance, is what is quoted with a measurement. An anomaly
of $5.0 \pm 0.6$ mGal has $\sigma = 0.6$ mGal and $\sigma^2 = 0.36\ \mathrm{mGal^2}$.

Two algebraic identities do most of the work:

$$\operatorname{Var}(X) = E[X^2] - (E[X])^2,$$

which is the practical route to a variance because it needs only two raw moments;
and, for constants,

$$\operatorname{Var}(aX + b) = a^2 \operatorname{Var}(X).$$

Adding a constant shifts the distribution without spreading it; scaling by $a$
scales every deviation, and hence the variance by $a^2$. A velocity given in m/s
and the same velocity in km/s have standard deviations differing by $10^3$ and
variances differing by $10^6$.

## 4. Moments, skewness and kurtosis

The $k$-th **raw moment** is $\mu'_k = E[X^k]$ and the $k$-th **central moment**
is $\mu_k = E[(X - E[X])^k]$. The first two are the mean and the variance. The
next two, once standardised, describe the shape:

$$\text{skewness} = \frac{\mu_3}{\sigma^3}, \qquad
\text{excess kurtosis} = \frac{\mu_4}{\sigma^4} - 3.$$

The subtraction of $3$ in the kurtosis sets the Gaussian value to zero, so that a
positive excess kurtosis means heavier tails than a Gaussian. Both are
dimensionless, which is the point of standardising.

The demonstration estimates them for $400\,000$ exponential draws:

```
  skewness          empirical = 2.015070   analytic = 2.000000
  excess kurtosis   empirical = 6.092775   analytic = 6.000000
```

Both agree with the exact values for the exponential distribution. The
interpretation to carry away: the exponential's positive skewness of $2$ says
that its long tail is on the right, so the mean exceeds the median, and its excess
kurtosis of $6$ says its tails are far heavier than a Gaussian's. Any method that
assumes Gaussian errors will be over-confident on exponentially distributed data,
and the diagnostic to check is the kurtosis, not the variance.

**Why the fourth moment matters.** The sampling error of a sample variance depends
on the fourth central moment. For a distribution with excess kurtosis $6$, the
sample variance is a much noisier estimate than the Gaussian intuition suggests.
For a distribution with no fourth moment — any Pareto with tail exponent at or
below $4$ — the sample variance does not converge at all, in the sense that its
own variance is infinite. Lesson 04 demonstrates this numerically: for a tail
exponent of $2.5$ the sample variance is unbiased in expectation yet understates
the true variance in about $79\%$ of samples of size $10\,000$, because its
distribution is so strongly right-skewed.

## 5. Covariance and correlation

The **covariance** of $X$ and $Y$ is

$$\operatorname{Cov}(X,Y) = E\bigl[(X - E[X])(Y - E[Y])\bigr]
= E[XY] - E[X]E[Y],$$

and the **correlation coefficient** is the standardised version,

$$\rho_{XY} = \frac{\operatorname{Cov}(X,Y)}{\sigma_X \sigma_Y},
\qquad -1 \le \rho_{XY} \le 1.$$

The bound follows from the Cauchy–Schwarz inequality. The extremes are attained
when $Y$ is an exact affine function of $X$: $\rho = +1$ when the slope is
positive, $-1$ when negative.

The reason covariance deserves its own definition is the variance of a sum:

$$\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)
+ 2\operatorname{Cov}(X,Y).$$

For independent variables the covariance vanishes and variances add. **For
dependent variables they may add or partially cancel**, and in geophysics they
usually do something in between. The demonstration checks the identity against
simulation for three correlations:

```
  rho =  0.0: Var X = 0.9995, Var Y = 0.9917, Cov = -0.0004, Corr = -0.0004
            Var(X+Y) sample = 1.990306, predicted = 1.990306, analytic = 2.000000
  rho =  0.8: Var X = 0.9995, Var Y = 0.9963, Cov = 0.7993, Corr = 0.8010
            Var(X+Y) sample = 3.594299, predicted = 3.594299, analytic = 3.600000
  rho = -0.5: Var X = 0.9995, Var Y = 0.9941, Cov = -0.5001, Corr = -0.5017
            Var(X+Y) sample = 0.993284, predicted = 0.993284, analytic = 1.000000
```

At $\rho = 0.8$ the sum has almost twice the variance that independence would
suggest ($3.6$ against $2.0$); at $\rho = -0.5$ it has *half* ($1.0$ against
$2.0$). Positive correlation makes averaging less effective, negative correlation
makes it more effective than the naive count would suggest. Neither direction is
a curiosity: in a gravity survey the station elevations used in the Bouguer
correction are spatially correlated, in a seismic array the instrument responses
share a calibration, and in a satellite mission successive orbits share the same
model of the spacecraft's mass distribution.

For several variables, the covariances are collected into a **covariance matrix**
$\mathbf{C}$ with $C_{ij} = \operatorname{Cov}(X_i, X_j)$. It is symmetric and
positive semi-definite, and it is the object propagated through a linear inverse
problem: if $\mathbf{d} = G\mathbf{m}$ then $\mathbf{C}_d = G\mathbf{C}_m
G^{\mathsf T}$. That expression, and the singular-value decomposition of $G$,
are the working content of [01-07-08 Singular Value Decomposition and Rank
Truncation](../07-linear-algebra/08-svd.md) and of
[18 Inverse Problems](../../18-inverse-problems/README.md).

### 5.1 A conditional view: the law of total variance

Covariance also appears in the decomposition of a variance into within-group and
between-group parts. For random variables $X$ and $Y$,

$$\operatorname{Var}(X) = E\bigl[\operatorname{Var}(X \mid Y)\bigr] +
\operatorname{Var}\bigl(E[X \mid Y]\bigr).$$

The two terms are read as follows: the first is the average variability *inside* a
group defined by $Y$, and the second is the variability *between* the group means.
The derivation is a two-line expansion of $E[(X - E[X])^2]$ after adding and
subtracting $E[X \mid Y]$.

The geophysical use is immediate. Suppose $X$ is a seismic velocity and $Y$ is a
lithological facies, and that within each facies the velocity has a known spread.
Then the total velocity variance measured across a borehole or a tomography cell is
the average within-facies variance plus the variance of the facies-conditional
means. A region whose velocity variability is dominated by the first term cannot be
characterised better by more facies classes; one dominated by the second is telling
you that facies classification is the informative variable. Splitting a variance
this way is a standard first step in deciding whether a classification or a
continuous regression is the appropriate model, and it is the analysis behind
hierarchical models in
[21 Statistics, Bayesian Methods and Machine Learning](../../21-statistics-bayesian-ml/README.md).

## 6. Nonlinear functions: expectation does not commute

For a nonlinear $g$, in general

$$E[g(X)] \ne g(E[X]).$$

This is a first-order trap in every uncertainty budget. If $g$ is convex, Jensen's
inequality gives $E[g(X)] \ge g(E[X])$. The reciprocal is the convex function that
appears most often in geophysics, because so many quantities are ratios or
inverses: velocity from travel time, density from mass and volume, resistivity
from resistance and geometry.

The module's error-propagation demonstration quantifies it. Taking
$\rho = m/V$ with $m = 2.50 \pm 0.02$ kg and $V = 1.00 \pm 0.03$ L, the nominal
value is $\rho = 2.500000$, and the Monte Carlo mean of $\rho$ is $2.502376$ —
a displacement of about $0.1\%$, which is the second-order term from the
curvature of $1/V$. At that size of uncertainty the displacement is negligible
against the $3.1\%$ standard deviation; the point is not that the bias is large,
but that it exists, has a sign, and grows as the cube of the relative
uncertainty. When a relative uncertainty is thirty percent rather than three, the
same curvature dominates the answer entirely, as lesson 09 shows.

## 7. Averaging: the standard error of the mean

Let $X_1, \dots, X_n$ be observations of the same quantity with common mean $\mu$
and variance $\sigma^2$. The sample mean is

$$\bar X = \frac{1}{n}\sum_{i=1}^{n} X_i.$$

By linearity, $E[\bar X] = \mu$: the sample mean is unbiased. For its variance,
write the double sum and use covariance:

$$\operatorname{Var}(\bar X) = \frac{1}{n^2}\sum_{i=1}^{n}\sum_{j=1}^{n}
\operatorname{Cov}(X_i, X_j)
= \frac{\sigma^2}{n} + \frac{2}{n^2}\sum_{i<j}\operatorname{Cov}(X_i, X_j).$$

If the observations are uncorrelated the cross terms vanish and

$$\operatorname{Var}(\bar X) = \frac{\sigma^2}{n}, \qquad
\text{standard error} = \frac{\sigma}{\sqrt{n}}.$$

This square-root law is the quantitative content of the instruction "repeat the
measurement". Its consequences are severe and are usually under-appreciated:
to halve the standard error you need **four** times as many observations, to
reduce it by a factor of ten you need a hundred times as many, and the returns
diminish precisely where surveys are already expensive.

When the observations do not have equal variance, the efficient combination weights
each by its inverse variance. For independent $X_i$ with variance $\sigma_i^2$ the
weighted mean is

$$\bar X_w = \frac{\sum_i w_i X_i}{\sum_i w_i}, \qquad w_i = \frac{1}{\sigma_i^2},
\qquad \operatorname{Var}(\bar X_w) = \frac{1}{\sum_i w_i}.$$

The result follows by minimising $\sum_i w_i (X_i - \theta)^2$ over $\theta$, which
is a one-parameter least-squares problem, and it is the scalar case of the
generalised least-squares solution met in
[01-07-07](../07-linear-algebra/07-orthogonality.md). A numerical illustration of
how sharply precision is weighted: combining a terrestrial gravity estimate with
$\sigma = 0.02$ mGal and a satellite estimate of the same quantity with
$\sigma = 0.20$ mGal gives weights in the ratio $100:1$ and a combined standard
deviation of $1/\sqrt{2500 + 25} = 0.0199$ mGal. The satellite estimate improved
the answer by half a per cent. Averaging is only ever as valuable as the precision
of the data being averaged in.

The demonstration confirms the law by simulation, with $5.0$ mGal of true anomaly
and $0.6$ mGal of single-reading noise:

```
       n     SE theory   SE observed        bias
       1      0.600000      0.600765   -0.001411
       4      0.300000      0.301292    0.000902
      16      0.150000      0.150172    0.000554
      64      0.075000      0.075069    0.000166
     256      0.037500      0.037455   -0.000377
```

Theory and simulation agree to well within Monte Carlo error at every $n$, and
the bias column, whose entries are of order $0.001$ mGal, is consistent with zero
at the precision of $20\,000$ replicates with a $0.6$ mGal single-reading
standard deviation.

## 8. When averaging does not work

The derivation above shows exactly where the square-root law comes from: the
cross-covariance terms. If the observations share a component of error, those
terms do not vanish and the variance of the mean has a floor.

Model that explicitly: let each reading be

$$X_i = \mu + B + \varepsilon_i,$$

where $B$ is a shared offset with variance $\sigma_B^2$ — an instrument
calibration error, an uncorrected datum, a shared velocity model — and
$\varepsilon_i$ is independent reading noise with variance $\sigma_\varepsilon^2$.
Then, because $B$ appears in every reading, $\operatorname{Cov}(X_i, X_j) =
\sigma_B^{2}$ for $i \ne j$, and

$$\operatorname{Var}(\bar X) = \sigma_B^2 + \frac{\sigma_\varepsilon^2}{n}.$$

The first term does not shrink. The demonstration makes the consequence concrete
with $\sigma_B = 0.30$ mGal and $\sigma_\varepsilon = 1.00$ mGal:

```
       n     SE theory   SE observed    mean est
       1      1.044031      1.051085   20.000551
      16      0.390512      0.396811   19.997631
     256      0.306441      0.306752   19.998925
    4096      0.300407      0.298843   20.007997
```

Between $n = 1$ and $n = 16$ the standard error falls from $1.044$ to $0.391$, a
factor of $2.7$. Between $n = 256$ and $n = 4096$ — a sixteen-fold increase in
effort — it falls from $0.3064$ to $0.3004$, about $2\%$. Beyond roughly a hundred
readings, additional data buy essentially nothing, because the floor at
$\sigma_B = 0.30$ has been reached. The correct response to that situation is not
more readings; it is a calibration experiment that reduces $\sigma_B$.

This is the most important practical lesson in the lesson, and it is worth
stating as a rule:

> **Random error averages down; systematic error does not. Before acquiring more
> data, decide which kind of error dominates, because only one of them responds.**

The correlated-data case is the general version. If all observations share the
same error, $\rho = 1$ in the double sum and $\operatorname{Var}(\bar X) =
\sigma^2$ regardless of $n$: averaging a quantity with itself many times reveals
nothing. The intermediate case, in which correlations decay with separation
(distance along a profile, time between readings, channel number in a band), is
modelled by replacing $n$ with an **effective sample size**
$n_{\text{eff}} = n/(1 + 2\sum_k \rho_k)$; the practical implication is that a
correlation length of $\ell$ stations reduces a survey of $n$ stations to about
$n/\ell$ independent observations.

## 9. Assumptions and regime of validity

1. **The moments must exist.** $E[X]$ requires $\int |x| f(x)\,dx < \infty$;
   $\operatorname{Var}(X)$ requires the second moment; a usable sample variance
   requires the fourth. Heavy-tailed data violate these silently, and the failure
   is visible only as instability, not as an error message.
2. **$\sigma/\sqrt{n}$ assumes uncorrelated observations with equal variance.**
   Heteroscedastic data — readings with different precisions, as in a mixed
   terrestrial and satellite gravity survey — require weighted averages, and the
   standard error of a weighted mean is $\left(\sum w_i\right)^{-1/2}$ for
   optimal weights $w_i \propto 1/\sigma_i^2$.
3. **Correlation is a physical claim, not a nuisance parameter.** It must be
   estimated from the survey design, from repeat measurements, or from an
   independent dataset. Assuming $\rho = 0$ because no correlation was measured is
   not the same as knowing that it is zero.
4. **Expectation is a linear operation; almost nothing else is.** Any quantity
   built from expectations — a variance, a covariance, a confidence interval, a
   propagated uncertainty — inherits assumptions from the expectations inside it.
5. **Units must be carried.** Variances are in squared units, covariances in the
   product of two units, correlations dimensionless, and the standard error in the
   units of the reading.

## 10. Python demonstration

Run

```
python3 expectation_variance_demo.py
```

from `code/`. Standard library only; the seed is 20240119, with $+1$ to $+4$ for
the four simulation blocks inside the script. Sections: moments from a PMF and a
PDF, linearity under dependence, the variance-of-a-sum identity, the standard
error of a mean, the skewness and kurtosis of the exponential, and the shared-bias
floor. Outputs are quoted verbatim in Sections 1.1, 2, 5, 7 and 8.

**What to notice in the output.** The two tables in Sections 7 and 8 look similar
in construction and tell opposite stories: in the first the observed standard
error tracks theory down to the smallest value tested, and in the second it
flattens at a value set by an input that appears nowhere in the *n* column. A
standard error without a stated correlation model is a conditional statement, and
the condition is the model.

**Breaking exercise.** In the shared-bias section, change `sd_bias` to `0.05` and
predict, before running, the value of $n$ at which the noise term
$\sigma_\varepsilon^2/n$ becomes smaller than $\sigma_B^2$. Then set
`sd_noise = 0.1` and repeat. The crossing point is the sample size at which the
experiment stops being limited by its own randomness.

## 11. Common mistakes

1. **Reporting the variance with the units of the quantity.** A variance of
   $0.36$ is meaningless until it is said to be in mGal².
2. **Using $\sigma/\sqrt{n}$ with correlated data.** This is the most common
   quantitative error in published uncertainty statements.
3. **Assuming $E[g(X)] = g(E[X])$.** True for affine $g$ only.
4. **Confusing the standard deviation of the data with the standard error of the
   mean.** The first is $\sigma$ and does not change with $n$; the second is
   $\sigma/\sqrt{n}$ and does.
5. **Averaging away a bias.** No amount of repetition removes an offset shared by
   every reading.
6. **Treating $\rho = 0$ as the default.** Uncorrelated is a hypothesis, usually
   the less plausible one in spatial data.
7. **Reading a correlation as causation, or as a large effect.** $\rho$ measures
   linear association only, is insensitive to monotone but nonlinear
   relationships, and a modest $\rho$ can correspond to a large systematic
   displacement when both variables have large means.
8. **Estimating skewness and kurtosis from small samples.** Their sampling errors
   are large; skewness and kurtosis need hundreds of observations before they
   stabilise, and the fourth moment must exist for the sample kurtosis to be
   meaningful at all.

## 12. Real-world applications

- **Repeat surveys and instrument precision.** The standard error of the mean is
  the arithmetic behind repeat-reading specifications: a gravimeter quoted at
  $0.01$ mGal repeatability achieves that only by averaging several readings, and
  the quoted figure already includes the averaging convention.
- **Network design.** The effective sample size and the correlated-error floor
  together determine how many stations a survey needs to reach a target
  uncertainty, and whether the limiting factor is station count or calibration.
- **Least-squares fitting.** Weighted least squares minimises a sum of squared
  deviations weighted by reciprocal variances; the covariance matrix of the fitted
  parameters is the inverse of the normal matrix, and its diagonal entries are
  exactly the variances derived in Section 5. See
  [01-07-07 Orthogonality, Projections and Least Squares](../07-linear-algebra/07-orthogonality.md).
- **Time series and geodetic velocities.** The uncertainty of a trend from a GNSS
  time series depends on the temporal correlation of the noise, which is
  strongly coloured by multipath, monument motion and unmodelled loading. Naive
  $n^{-1/2}$ error bars understate the trend uncertainty, sometimes by an order of
  magnitude.
- **Monte Carlo uncertainty budgets.** Sampling an input distribution and
  averaging the output is an estimate of an expectation; its own uncertainty is
  $s/\sqrt{N_{\text{draws}}}$, which is the standard error of Section 7 applied to
  the simulation itself. This is why every Monte Carlo figure in this module
  quotes its standard error.

## 13. Further reading

- **Casella, G. and Berger, R. L. *Statistical Inference*.** Level: advanced.
  Chapters on expectation, variance and covariance; the treatment of conditional
  expectation and of the variance decomposition is the standard reference.
- **Taylor, J. R. (1997). *An Introduction to Error Analysis* (2nd ed.).
  University Science Books.** Level: beginner to intermediate. Chapters 4 and 5
  give the working version of Section 5 for laboratory data, including the
  correlation warning in the form it usually appears in practice.
- **Bevington, P. R. and Robinson, D. K. *Data Reduction and Error Analysis for
  the Physical Sciences*.** Level: intermediate. Fuller treatment of weighted
  means and of the propagation of covariances through a fit.
- **Kennedy, P. (2008). *A Guide to Econometrics*.** Level: intermediate to
  advanced. The chapters on heteroscedasticity and on clustered/correlated errors
  are the clearest short account of why $\sigma/\sqrt{n}$ fails in correlated
  data, and what to use instead.
- **Bendat, J. S. and Piersol, A. G. *Random Data: Analysis and Measurement
  Procedures*.** Level: advanced. The engineering treatment of correlation,
  spectra and the effective number of independent observations, which is the
  language several geophysical subfields use.

> Note on citations: bibliographic details are given so the works can be located.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library.

## 14. Related lessons

- [02 Random Variables, PMFs, PDFs and CDFs](./02-random-variables.md) — the
  distributions whose moments are computed here.
- [04 Common Distributions and Their Earth-Science Roles](./04-distributions.md)
  — which mechanisms produce which moment behaviour, including the divergences.
- [05 Sampling Distributions, Law of Large Numbers and CLT](./05-sampling-and-clt.md)
  — the distribution of $\bar X$, not just its mean and variance.
- [06 Point Estimation, Bias, Consistency and Efficiency](./06-estimation-theory.md)
  — what happens when $\mu$ and $\sigma^2$ are unknown and must be estimated.
- [09 Error and Uncertainty Propagation](./09-error-propagation.md) — the
  engineering use of the covariance algebra of Section 5.
- [01-07-07 Orthogonality, Projections and Least Squares](../07-linear-algebra/07-orthogonality.md)
  and [01-07-08 Singular Value Decomposition and Rank
  Truncation](../07-linear-algebra/08-svd.md) — the linear-algebra setting in
  which covariance matrices do their work.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — model and data
  covariance matrices, weighting and resolution.

## Exercises

[`exercises/03-expectation-variance-exercises.md`](./exercises/03-expectation-variance-exercises.md),
with solutions in
[`exercises/03-expectation-variance-solutions.md`](./exercises/03-expectation-variance-solutions.md).

## Self-assessment checklist

- [ ] I can compute a mean and a variance from a PMF and from a PDF, and check
      the result against a closed form.
- [ ] I can prove that $E[X+Y] = E[X] + E[Y]$ for discrete variables and state
      that no independence assumption was used.
- [ ] I can derive $\operatorname{Var}(aX+b) = a^2\operatorname{Var}(X)$ and say
      why the standard deviation is the quantity to quote.
- [ ] I can compute a covariance and a correlation, and use them to predict
      whether the variance of a sum is larger or smaller than the sum of the
      variances.
- [ ] I can explain in three sentences why $E[m/V] \ne E[m]/E[V]$ and in which
      direction the inequality goes.
- [ ] I can derive $\operatorname{Var}(\bar X) = \sigma^2/n$ under independence
      and identify the term that survives when independence fails.
- [ ] I can compute the sample size beyond which a stated systematic error makes
      further averaging pointless.
- [ ] I have run `code/expectation_variance_demo.py` and can point to the two
      tables that make the random-versus-systematic contrast quantitative.
