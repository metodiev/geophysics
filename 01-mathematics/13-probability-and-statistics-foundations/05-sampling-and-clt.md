---
id: 01-13-05
title: "Sampling Distributions, Law of Large Numbers and CLT"
level: intermediate
prereqs: ["01-13-04"]
estimated_minutes: 90
tags: [central-limit-theorem, law-of-large-numbers, sampling-distribution, heavy-tails, convergence]
---

# Sampling Distributions, Law of Large Numbers and CLT

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** a statistic from the data that produced it, and describe the
   *sampling distribution* of a statistic as the distribution of its values over
   repeated experiments.
2. **State** the law of large numbers with its hypothesis, and prove the
   finite-variance case with Chebyshev's inequality.
3. **Show** that a finite mean is required, and demonstrate the failure of the
   law for the Cauchy distribution numerically.
4. **State** the central limit theorem, standardise a sum correctly, and derive
   the Gaussian limit for the uniform parent by expanding the moment generating
   function.
5. **Quantify** the approach to normality as a function of skewness and sample
   size, and explain why the familiar threshold $n \approx 30$ is a heuristic
   about skewness rather than a theorem.
6. **Recognise** a heavy-tailed parent as a situation in which the CLT does not
   apply at all, and state the correct scaling for the fluctuation of the mean
   when the variance does not exist.
7. **Compute** the uncertainty of a Monte Carlo estimate, and decide how many
   draws a reported figure needs.

## Prerequisites

[01-13-04 Common Distributions and Their Earth-Science Roles](./04-distributions.md)
for the families whose sampling behaviour is studied here, and
[01-13-03 Expectation, Variance and Moments](./03-expectation-variance.md) for
the mean, variance and covariance algebra used in the derivations.

## 1. Statistics are random variables

The distinction this lesson rests on is easy to state and easy to forget.

The **data** $X_1, \dots, X_n$ are observed values. The **statistic** $T =
T(X_1, \dots, X_n)$ is a function of them: a mean, a median, a variance, a slope,
a maximum. A statistic is a random variable, because a different experiment would
have produced different data. Its distribution — over an imagined repetition of the
whole experiment — is the **sampling distribution** of the statistic.

This is the concept that makes uncertainty statements possible. When you report
$750 \pm 26$ m, the $\pm 26$ is a summary of the sampling distribution of your
depth estimator, not a property of the depth. The depth has one value (or, if
model uncertainty is included, a distribution over defensible values); the
*estimator* has a spread.

Three questions structure everything that follows:

- Does the sampling distribution concentrate on the truth as $n$ grows?
  (Section 2: the law of large numbers.)
- What is its shape, and how fast does it become approximately Gaussian?
  (Sections 4 and 5.)
- What happens when the parent distribution violates the hypotheses?
  (Sections 3.3 and 6.)

## 2. The law of large numbers

### 2.1 Statement

Let $X_1, X_2, \dots$ be independent and identically distributed with finite mean
$\mu = E[X_1]$. Write $\bar X_n$ for the sample mean of the first $n$. Then for
every $\varepsilon > 0$,

$$P\left(\left|\bar X_n - \mu\right| > \varepsilon\right) \to 0
\qquad \text{as } n \to \infty.$$

This is the **weak law**. The strong law makes the stronger claim that
$\bar X_n \to \mu$ almost surely, meaning the set of outcomes on which the sample
mean fails to converge has probability zero. For finite-variance variables the
weak law has a two-line proof, which is worth carrying around.

### 2.2 Proof by Chebyshev's inequality

Chebyshev's inequality states that for a random variable $Y$ with finite mean and
variance, $P(|Y - E[Y]| \ge \varepsilon) \le \operatorname{Var}(Y)/\varepsilon^2$.
It follows from the elementary observation that
$\operatorname{Var}(Y) \ge \varepsilon^2 P(|Y - E[Y]| \ge \varepsilon)$.

Apply it to $\bar X_n$, which has mean $\mu$ and variance $\sigma^2/n$ when the
observations are independent:

$$P\left(\left|\bar X_n - \mu\right| \ge \varepsilon\right)
\le \frac{\sigma^2}{n\varepsilon^2} \xrightarrow[n \to \infty]{} 0.$$

The bound is loose — for a Gaussian parent with $n = 100$ and
$\varepsilon = 0.2\sigma$ it gives $0.25$ where the true value is $0.045$ — but it
is distribution-free and it makes the mechanism plain: **the variance of the mean
shrinks as $n^{-1}$, so the mean concentrates on its expectation.**

### 2.3 The hypothesis is a hypothesis

The finite-mean requirement is doing real work and can fail. The demonstration runs
the sample mean for three parents, one million terms each, with seed 20240121:

```
  running sample mean (true values: Exp(1) 1.0, Pareto(1.5) 3.0)
             n          Exp(1)     Pareto(1.5)
         1,000        1.051983        6.412197
        10,000        1.022037        3.225375
       100,000        1.000303        3.111711
     1,000,000        0.999809        3.029064
```

Both converge. The Pareto approaches its mean of $3$ far more slowly — at $n =
10^{6}$ it is still $0.97\%$ high, where the exponential is within $0.02\%$ — which
is the rate effect of Section 3.3. Now the same experiment for the standard
Cauchy distribution, which has no mean:

```
  Same experiment for the standard Cauchy distribution, whose mean does not exist.
  Five independent runs, two sample sizes:
           n            run 1           run 2           run 3           run 4           run 5
       1,000         0.466251        0.333072        9.819017        0.273343       -0.307867
     100,000        10.774186        2.719472       -0.673174       -0.359920        2.097003
```

The five averages at $n = 100\,000$ range from $-0.67$ to $10.77$ and are no more
mutually consistent than the five averages at $n = 1\,000$. Increasing $n$ by a
factor of a hundred does not make the answers agree, and it never will: the sample
mean of a Cauchy sample is itself Cauchy, with the same spread regardless of $n$.
Averaging a Cauchy variable does not reveal a centre, because there is not one.
The visual signature of this failure is an average that wanders, with occasional
large jumps as an extreme observation enters or leaves the cumulative sum.

## 3. The rate of convergence

### 3.1 Rate under finite variance

With the standard error $\sigma/\sqrt{n}$, reducing the uncertainty of a mean by a
factor of ten requires a hundredfold increase in the number of observations. The
demonstration measures the rate using the interquartile range of the mean over
$1000$ independent runs, which is a robust scale:

```
    Exp(1)   : IQR of the mean = 0.140210 (n=100), 0.042905 (n=1,000), 0.012930 (n=10,000)
      IQR * n^(1/2 for Exp, 1/3 for Pareto) = 1.4021, 1.3568, 1.2930
      fitted exponent 100 -> 10 000 = 0.5176
```

The fitted exponent is $0.5176$ where theory says $0.5000$; the normalised column
is roughly constant at $1.4$, $1.36$, $1.29$. Both are what one expects from
$1000$ runs with a scale estimated from quantiles, whose own relative standard
error is a few per cent.

### 3.2 Why it is worth measuring rather than quoting

The point of measuring the exponent rather than asserting $n^{-1/2}$ is that the
measurement is falsifiable and its error is quantifiable. A convergence rate that
comes out of an experiment is evidence; a convergence rate asserted from a formula
is an assumption wearing a formula's clothes. The same discipline applies to the
other rate measurements in this lesson.

### 3.3 Rate under heavy tails: the exponent is not $\tfrac12$

When the variance is infinite but the mean exists — the Pareto family with
$1 < \alpha < 2$ — the sample mean still converges, but more slowly, and the
correct exponent is **not** $1/2$. The fluctuation is governed by the largest
observations: the largest of $n$ Pareto draws is of order $n^{1/\alpha}$, so its
contribution to the mean $\bar X_n$ is of order $n^{1/\alpha - 1} =
n^{-(1 - 1/\alpha)}$, and the whole fluctuation follows that scale. For
$\alpha = 1.5$ the exponent is $1 - 1/1.5 = 1/3$:

```
    Pareto1.5: IQR of the mean = 0.727458 (n=100), 0.362077 (n=1,000), 0.169708 (n=10,000)
      IQR * n^(1/2 for Exp, 1/3 for Pareto) = 3.3766, 3.6208, 3.6562
      fitted exponent 100 -> 10 000 = 0.3161
```

The fitted exponent $0.3161$ is close to $1/3 = 0.3333$, and the normalised column
is approximately constant. The practical consequence is stark: for a tail exponent
of $1.5$, a hundredfold increase in sample size buys only a factor of about $4.6$
in precision for the mean, where the same hundredfold increase would buy a factor
of $10$ with a finite variance.

The general statement is that $n^{1-1/\alpha}(\bar X_n - \mu)$ converges in
distribution to a **stable law** with index $\alpha$, not to a Gaussian. Stable
laws have index in $(0,2]$; the Gaussian is the extreme case $\alpha = 2$, and it
is the only one with a finite variance. This single fact is the source of the
failure in Section 6, and it is worth stating as a slogan:

> **The law of large numbers needs a finite mean; the central limit theorem needs
> a finite variance. They are different hypotheses.**

## 4. The central limit theorem

### 4.1 Statement

Let $X_1, X_2, \dots$ be independent and identically distributed with mean $\mu$
and finite variance $\sigma^2 > 0$. Define the standardised sum

$$Z_n = \frac{\bar X_n - \mu}{\sigma/\sqrt{n}}.$$

Then $Z_n$ converges in distribution to the standard normal:

$$P(Z_n \le z) \to \Phi(z) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{z}
e^{-t^2/2}\,dt.$$

### 4.2 Derivation sketch by moment generating functions

Let $M_X(t) = E[e^{tX}]$ and assume it exists in a neighbourhood of zero. For the
standardised single observation $Y = (X - \mu)/\sigma$, expand
$M_Y(t) = 1 + t^2/2 + O(t^3)$, the linear term vanishing because $E[Y] = 0$ and
the quadratic coefficient being $E[Y^2]/2 = 1/2$. Then

$$M_{Z_n}(t) = \left[M_Y\left(\frac{t}{\sqrt n}\right)\right]^{n}
= \left[1 + \frac{t^2}{2n} + O\left(n^{-3/2}\right)\right]^{n}
\xrightarrow[n\to\infty]{} e^{t^2/2},$$

which is the moment generating function of the standard normal. The convergence to
$e^{t^2/2}$ rests on the limit $(1 + a/n)^n \to e^{a}$ with $a = t^2/2$; the
$O(n^{-3/2})$ terms vanish because they are raised to the power $n$.

The assumption that the moment generating function exists is stronger than
necessary — the theorem holds for any finite variance, and characteristic functions
supply the general proof — but the expansion shows the mechanism clearly: **only
the first two moments matter in the limit**, which is why the Gaussian limit is
universal and why distributions with the same mean and variance have
indistinguishable sample means for large $n$.

### 4.3 Rate of approach, and why it is not free

The **Berry–Esseen** bound makes the rate quantitative: there is a constant $C$
(known to be below $0.5$ by the sharpest elementary arguments) such that

$$\sup_z \left|P(Z_n \le z) - \Phi(z)\right| \le
\frac{C\,E\left|X - \mu\right|^{3}}{\sigma^{3}\sqrt n}.$$

The bound scales as $n^{-1/2}$ but its constant is the **standardised third
absolute moment**, a dimensionless measure of skewness. Distributions that are
symmetric have a small constant; strongly skewed distributions have a large one.
That is why "the CLT applies" is not a statement about $n$ alone.

## 5. The central limit theorem in practice

### 5.1 Two parents, five sample sizes

The demonstration standardises the mean at $n = 1, 2, 5, 30, 300$ using $20\,000$
replicates and reports the maximum vertical distance between the empirical CDF and
the standard normal CDF. With $20\,000$ replicates the Monte Carlo noise floor on
that statistic is about $0.0071$, so values at or below that floor are
indistinguishable from exact normality.

```
  Uniform(0,1) (bounded, symmetric): max |F_emp - Phi| of the standardised mean
       n        KS gap
       1      0.059014
       2      0.017615
       5      0.012021
      30      0.006823
     300      0.007529

  Exponential(1) (skewed): max |F_emp - Phi| of the standardised mean
       n        KS gap
       1      0.158665
       2      0.094046
       5      0.057374
      30      0.027362
     300      0.013241
```

Three observations:

- **Symmetry beats everything else.** For the uniform parent the gap is already at
  the noise floor by $n = 30$, and it is small even at $n = 2$. The uniform's third
  central moment is exactly zero, so the leading Berry–Esseen term vanishes and
  what remains converges very fast.
- **Skewness is expensive.** For the exponential parent the gap is $0.1587$ at
  $n = 1$, still $0.0574$ at $n = 5$, and only reaches the noise floor somewhere
  between $n = 300$ and $n = 1000$.
- **The heuristic "$n > 30$ is enough" is a statement about skewness.** It is a
  reasonable rule for approximately symmetric data and a bad one for the
  exponential, where the gap at $n = 30$ is $0.027$ — a fourfold excess over the
  noise floor, corresponding to a real, visible departure from normality in the
  tails of the standardised mean.

### 5.2 Why the tail matters more than the middle

Kolmogorov–Smirnov measures a vertical distance in the CDF and is dominated by the
point of largest discrepancy, often in the tail. For constructing confidence
intervals the tail is exactly the part that matters: a nominal $95\%$ interval
requires the $2.5\%$ and $97.5\%$ quantiles to be right, and a distribution whose
mean is nearly normal but whose tails are too heavy produces intervals that
undercover. Section 6.2 quantifies this for a heavy-tailed parent, and lesson 07
measures coverage directly.

## 6. When the central limit theorem fails

### 6.1 The failure is total, not gradual

Take the Pareto parent with tail exponent $\alpha = 1.5$. The mean exists, so the
law of large numbers holds and the sample mean converges to $3$. The variance does
not exist, so the standardisation $\sqrt n(\bar X - \mu)/\sigma$ is undefined; the
correct standardisation uses the sample standard deviation, $Z = \sqrt n(\bar X -
\mu)/s$, and no Gaussian limit exists. The limit is a stable law with index
$1.5$. The demonstration measures the tails of $Z$ with $20\,000$ replicates at
$n = 10$ and $n = 100$, $5\,000$ at $n = 1000$ and $2\,000$ at $n = 10\,000$:

```
         n     reps   P(|Z|>1.96)     P(|Z|>5)     P(|Z|>20)
        10   20,000      0.421550     0.177150      0.005850
       100   20,000      0.293600     0.051400      0.000000
     1,000    5,000      0.247200     0.016400      0.000000
    10,000    2,000      0.224000     0.011000      0.000000
```

Under a Gaussian limit the first column would be $0.050$ at every $n$. It is
$0.42$ at $n = 10$ and still $0.22$ at $n = 10\,000$. Dividing the sample size by
a thousand reduced the excess tail probability by less than a factor of two. The
distribution is not slowly becoming normal; it is converging to something else.

The absence of the extreme tail entries at large $n$ ($P(|Z| > 20)$ is zero for
$n \ge 100$) is a sample-size artefact: with $2000$ replicates a probability below
about $5\times10^{-4}$ cannot be resolved. The intermediate column tells the real
story — at $n = 10\,000$, $1.1\%$ of standardised means exceed $5$ in absolute
value, against a Gaussian prediction of about $6\times10^{-7}$.

### 6.2 What to do instead

1. **Check whether the variance exists.** Estimate the tail exponent. If
   $\hat\alpha \lesssim 2$, no finite-variance error bar is meaningful.
2. **Use the correct scaling for the mean.** The fluctuation of $\bar X$ is of
   order $n^{-(1-1/\alpha)}$, which is much slower than $n^{-1/2}$. For
   $\alpha = 1.5$ the exponent is $1/3$ — measured as $0.3161$ in Section 3.3.
3. **Prefer quantiles to moments.** Medians and other quantiles have Gaussian
   sampling distributions under much weaker conditions, because they are local
   functionals of the density rather than integrals against it. The demonstration
   of lesson 04 showed medians matching theory to four digits where variances were
   meaningless.
4. **Use resampling with an eye on the tail.** The bootstrap estimates the
   sampling distribution without assuming a parametric form, but it inherits the
   sample's tail: for heavy-tailed data bootstrap intervals for a mean can be
   badly miscalibrated, while bootstrap intervals for a median behave far better.
5. **Report the sample size honestly.** If the extreme quantile of interest would
   require $10^{4}$ times more data than you have, say so, and give the model-based
   estimate with its model-dependence stated.

## 7. Beyond the mean: other sampling distributions

The sample mean is the simplest statistic and the one with the cleanest theory, but
it is not the only one used, and the others have their own sampling distributions.

- **The sample variance.** With Gaussian data, $(n-1)s^2/\sigma^2$ has a
  chi-squared distribution with $n-1$ degrees of freedom; its spread depends on the
  fourth moment, and for non-Gaussian data the chi-squared result is only a
  large-sample approximation. This is the origin of the Student-t interval of
  lesson 07.
- **The sample maximum.** Its distribution is the extreme-value family of lesson
  04, not the Gaussian. Confidence intervals for a return level come from that
  family.
- **A ratio of sample means.** Its distribution is not Gaussian even for large
  $n$ in a practically useful sense, because the denominator can approach zero; the
  delta method linearises the ratio and gives a Gaussian approximation whose
  adequacy depends on the coefficient of variation of the denominator.
- **A fitted model parameter.** In a linear least-squares problem the parameter
  covariance is available in closed form, and the parameter estimates are Gaussian
  when the data errors are. In a nonlinear problem the sampling distribution must be
  obtained by simulation or asymptotics, and the delta method or a Monte Carlo
  ensemble is the usual recourse.

A useful test of understanding: for each statistic you report, ask what its
sampling distribution is and how it was obtained. An uncertainty statement whose
sampling distribution is unknown is a guess with decimal places.

## 8. Monte Carlo: the CLT applied to simulation

The reason lessons in this module quote "Monte Carlo standard error" is that the
CLT applies to simulation output. If $N$ independent draws are averaged, the
sample mean of the draws has standard error $s/\sqrt{N}$ where $s$ is the standard
deviation of the simulated quantity. Hence:

- To halve a Monte Carlo error you need four times as many draws.
- Quoting a Monte Carlo result to more digits than $s/\sqrt N$ supports is
  fabrication.
- When the simulated quantity has infinite variance — as in the energy example of
  lesson 02 — the Monte Carlo mean does not converge and the standard error is
  undefined. The correct response is to report a quantile, and to check that the
  quantile has stabilised.

Every figure in this module's demonstrations is accompanied by either an analytic
value, a Monte Carlo standard error, or both, and the agreement is quoted in units
of that standard error. This is the standard to which a numerical result should be
held.

## 9. Assumptions and regime of validity

1. **Independence.** The derivations assume i.i.d. data. Correlated data reduce the
   effective sample size: with correlation length $\ell$, $n$ observations behave
   like $n/\ell$ independent ones, and the CLT applies with that replacement, which
   is the correct statement but requires $\ell$ to be estimated.
2. **Identical distribution.** Heteroscedastic observations can still be averaged,
   but the correct variance is a weighted sum, and the CLT needs a condition such
   as Lindeberg's to prevent a single observation from dominating the total
   variance.
3. **Finite variance.** The CLT's hypothesis, and the one most often violated in
   the Earth sciences.
4. **Finite mean for the LLN.** A weaker but indispensable hypothesis.
5. **$n$ large enough for the actual distribution.** Berry–Esseen says the error is
   proportional to the standardised third absolute moment, so skewness converts
   directly into required sample size. A parent with skewness $10$ needs roughly
   a hundred times the $n$ of a symmetric parent for the same accuracy.
6. **The CLT is a statement about the mean, not about the sample.** A sample from a
   heavy-tailed distribution is not approximately Gaussian; its *mean* may be, when
   the variance exists. Two different claims, often conflated.

## 10. Python demonstration

Run

```
python3 sampling_and_clt_demo.py
```

from `code/`. Standard library only; seed 20240121, with offsets for the internal
blocks. Three sections: the law of large numbers and its Cauchy failure, the
approach to normality for a bounded and a skewed parent, and the heavy-tail
failure together with a rate measurement. Outputs are quoted in Sections 2.3, 3.1,
3.3 and 5.1, 6.1.

**One correction worth noticing.** The rate measurement in Section 3.3 is a case
where a numerical experiment corrected a mistake in the author's own reasoning.
The first version of the script labelled the Pareto scaling as $n^{-1/\alpha}$
rather than $n^{-(1 - 1/\alpha)}$, which predicts $0.667$ where the experiment
returned $0.32$. The experiment was right and the label was wrong: the fluctuation
of an average is driven by the largest term, whose size relative to the number of
terms gives $1 - 1/\alpha$. This is the value of measuring a rate instead of
quoting one — the measurement is falsifiable and the formula is not.

**Breaking exercise.** Change the Pareto exponent in Section 3 from $1.5$ to
$2.5$. The variance now exists, so the classical CLT applies. Predict the fitted
exponent before running, and check how much more precision a hundredfold increase
in $n$ buys compared with the $\alpha = 1.5$ case.

## 11. Common mistakes

1. **Believing the CLT says data are normal.** It says a *standardised mean* is
   approximately normal, and only when the variance is finite.
2. **Using $n > 30$ as a licence.** Adequacy depends on skewness; for strongly
   skewed data $n = 30$ can be far too few, and for symmetric data $n = 5$ can be
   plenty.
3. **Quoting a standard error for a heavy-tailed mean.** Without a finite variance
   there is no standard error to quote.
4. **Assuming averaging fixes everything.** It fixes independent random error only.
   The systematic-error floor of lesson 03 does not move, and neither does the
   bias of a miscalibrated instrument.
5. **Confusing the sample size with the effective sample size.** Ten thousand
   correlated observations may contain fewer than a hundred independent ones.
6. **Reporting Monte Carlo output to more digits than its own uncertainty
   supports.** The simulation is itself a sampling experiment.
7. **Testing convergence by looking at a running mean over a short trace.** Heavy
   tails produce long apparent plateaus that break; the rate measurement of Section
   3.3 is a better diagnostic than visual inspection.
8. **Ignoring the dependence between statistics.** The sample mean and the sample
   variance of the same data are dependent, and so are successive values of a
   running mean; treating them as independent affects every downstream interval.

## 12. Real-world applications

- **How many measurements is enough?** Survey design is a CLT calculation: the
  standard error $\sigma/\sqrt n$ converts a precision requirement into a station
  count, as the power calculation in lesson 08 does for a detection.
- **Uncertainty of tomographic averages.** Regional averages of velocity or
  attenuation are means over spatially correlated samples; the effective sample
  size, not the number of cells, sets the uncertainty.
- **Monte Carlo uncertainty propagation.** Every ensemble estimate in lessons 06
  and 09 is a mean over draws, and its own error is the CLT applied to the
  ensemble.
- **Extreme-value and return-period estimation.** Here the relevant statistic is a
  maximum, not a mean, and the Gaussian approximation is replaced by the
  extreme-value family; the CLT is not the right tool and applying it understates
  return levels.
- **Aggregation of heterogeneous datasets.** Combining gravity measurements from
  different instruments requires weighting by variance, and the CLT for
  non-identically distributed variables is what justifies the weighted mean.
- **Convergence of iterative solvers and sampling algorithms.** Markov chain Monte
  Carlo and iterative inversion both rely on averages over a growing number of
  iterations; diagnosing non-convergence is a heavy-tail problem as often as it is
  a numerical one.

## 13. Further reading

- **Feller, W. *An Introduction to Probability Theory and Its Applications*,
  Volume II.** Level: advanced. The definitive treatment of the law of large
  numbers, the central limit theorem and stable laws; the discussion of why the
  variance must be finite is the one to read.
- **Casella, G. and Berger, R. L. *Statistical Inference*.** Level: advanced.
  Chapters on convergence in probability and distribution, with the standard
  proofs; the treatment of the delta method is directly applicable to ratio
  statistics.
- **Nolan, J. P. *Stable Distributions: Models for Heavy Tailed Data*.** Level:
  graduate. Openly available monograph covering the limit laws that replace the
  Gaussian when the variance is infinite.
- **Taleb, N. N. *Statistical Consequences of Fat Tails*.** Level: intermediate to
  advanced. Wide-ranging and opinionated; the chapters on the pre-asymptotics of
  heavy-tailed means make the practical consequences of Section 6 vivid.
- **Efron, B. and Tibshirani, R. J. *An Introduction to the Bootstrap*.** Level:
  advanced. The resampling approach to sampling distributions, and the chapters on
  the limitations of the bootstrap for heavy-tailed statistics.
- **Embrechts, P., Klüppelberg, C. and Mikosch, T. *Modelling Extremal Events*.**
  Level: graduate. Insurance and finance oriented, but the mathematics of sums and
  maxima of heavy-tailed variables is the same and is treated carefully.

> Note on citations: bibliographic details are given so the works can be located.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library.

## 14. Related lessons

- [03 Expectation, Variance and Moments](./03-expectation-variance.md) — the
  standard error whose sampling properties are studied here.
- [04 Common Distributions and Their Earth-Science Roles](./04-distributions.md) —
  the Pareto family that defeats the CLT, and the extreme-value family that
  replaces it for maxima.
- [06 Point Estimation, Bias, Consistency and Efficiency](./06-estimation-theory.md)
  — consistency formalised, and the efficiency of estimators under different
  parents.
- [07 Confidence Intervals and Their Correct Interpretation](./07-confidence-intervals.md)
  — what happens to interval coverage when the CLT is invoked but does not apply.
- [09 Error and Uncertainty Propagation](./09-error-propagation.md) — Monte Carlo
  propagation, whose own error is computed with the results of this lesson.
- [01-12-04 Numerical Integration](../12-numerical-methods/04-numerical-integration.md)
  — quadrature, which appears in this module whenever an integral must be
  evaluated numerically.

## Exercises

[`exercises/05-sampling-and-clt-exercises.md`](./exercises/05-sampling-and-clt-exercises.md),
with solutions in
[`exercises/05-sampling-and-clt-solutions.md`](./exercises/05-sampling-and-clt-solutions.md).

## Self-assessment checklist

- [ ] I can define a statistic and its sampling distribution, and distinguish both
      from the data.
- [ ] I can state the law of large numbers with its hypothesis and prove the
      finite-variance case with Chebyshev's inequality.
- [ ] I can explain why a Cauchy sample mean never converges, in terms of a missing
      mean.
- [ ] I can state the central limit theorem and derive the Gaussian limit for the
      uniform parent from the moment generating function.
- [ ] I can explain why $n > 30$ is a heuristic and compute the Berry–Esseen
      factor for a stated parent.
- [ ] I can state the correct scaling for the fluctuation of the mean when the
      variance does not exist, and give the value for $\alpha = 1.5$.
- [ ] I can compute the number of Monte Carlo draws needed to report a figure to a
      stated number of significant figures.
- [ ] I have run `code/sampling_and_clt_demo.py` and can explain why the exponent
      in the second row of the rate table is $0.32$ rather than $0.67$.
