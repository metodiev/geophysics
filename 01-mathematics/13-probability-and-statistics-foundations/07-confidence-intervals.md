---
id: 01-13-07
title: "Confidence Intervals and Their Correct Interpretation"
level: advanced
prereqs: ["01-13-06"]
estimated_minutes: 90
tags: [confidence-intervals, coverage, student-t, interval-estimation, interpretation]
---

# Confidence Intervals and Their Correct Interpretation

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** a confidence interval from a *pivot* — a statistic whose
   distribution does not depend on the unknown parameter — and explain why that
   property is what makes the interval valid.
2. **Derive** the known-$\sigma$ $z$ interval from the central limit theorem and
   the unknown-$\sigma$ $t$ interval from the Student-$t$ pivot, and state the
   degrees of freedom.
3. **Define coverage** and demonstrate it by simulation for both intervals.
4. **State the correct interpretation** of a confidence interval, distinguish it
   from the common misinterpretation, and explain the difference between a
   confidence interval and a credible interval.
5. **Quantify** the ways coverage fails: a misspecified noise model, a heavy-tailed
   parent, and a systematic offset — including the case in which more data make
   the coverage *worse*.
6. **Compute** the sample size required for a stated interval width, and invert
   the relationship when the sample size is given.
7. **Choose** between an analytic interval, a bootstrap interval and a Monte Carlo
   interval for a derived quantity.

## Prerequisites

[01-13-06 Point Estimation, Bias, Consistency and Efficiency](./06-estimation-theory.md)
for estimators and their sampling distributions, and
[01-13-05 Sampling Distributions, Law of Large Numbers and CLT](./05-sampling-and-clt.md)
for the normal approximation on which the intervals rest.

## 1. The problem, and two answers to it

A point estimate without an uncertainty is incomplete. The natural next step is an
interval:

> Given data, give a range of values for the parameter that is compatible with
> what was observed.

There are two standard answers, and they are different objects with different
guarantees. Being able to say which one you are using, and what it guarantees, is
the whole content of this lesson.

- A **confidence interval** is defined by a coverage property over repeated
  sampling: the procedure produces intervals that contain the true parameter with
  probability $1 - \alpha$ before the data are seen.
- A **credible interval** is a statement about the posterior distribution of the
  parameter given the data and a prior: the parameter lies in the interval with
  posterior probability $1 - \alpha$.

They often produce numerically similar intervals — and for a location parameter
with a flat prior they are identical — but they are answers to different questions.
A confidence interval is a statement about the *procedure*; a credible interval is
a statement about the *parameter*. Section 6 makes the distinction operational.

## 2. Pivots, and the construction of intervals

The construction rests on one idea. Let $T(X_1, \dots, X_n; \theta)$ be a function
of the data and the parameter. If the distribution of $T$ is the same for every
value of $\theta$, then $T$ is a **pivot**, and probability statements about $T$
can be inverted into statements about $\theta$ with guaranteed coverage.

### 2.1 The known-$\sigma$ interval

Suppose $X_1, \dots, X_n$ are independent with mean $\mu$ and *known* variance
$\sigma^2$. By the central limit theorem, for large $n$,

$$Z = \frac{\bar X - \mu}{\sigma/\sqrt n} \quad \text{is approximately }
\mathcal{N}(0,1),$$

which is a pivot, because the distribution of $Z$ does not depend on $\mu$. Write
$z_{1-\alpha/2}$ for the $1 - \alpha/2$ quantile of the standard normal, so that
$P(-z_{1-\alpha/2} \le Z \le z_{1-\alpha/2}) = 1 - \alpha$. Substituting $Z$ and
rearranging the inequalities for $\mu$ gives

$$P\left(\bar X - z_{1-\alpha/2}\frac{\sigma}{\sqrt n} \le \mu \le
\bar X + z_{1-\alpha/2}\frac{\sigma}{\sqrt n}\right) = 1 - \alpha.$$

The random quantities are the endpoints; $\mu$ is fixed. At $\alpha = 0.05$,
$z_{0.975} = 1.959964$, and for $\sigma = 2$, $n = 16$ the half-width is

$$1.959964 \times \frac{2}{4} = 0.979982.$$

### 2.2 The unknown-$\sigma$ interval

In practice $\sigma$ is unknown, and $\bar X$'s standard error must itself be
estimated. Replace $\sigma$ by the sample standard deviation $s$, giving

$$T = \frac{\bar X - \mu}{s/\sqrt n}.$$

This is *not* normal, because the numerator and the denominator are both random and
correlated. It is, however, still a pivot when the data are Gaussian: then
$T \sim t_{n-1}$, the Student-$t$ distribution with $n - 1$ **degrees of freedom**.
The reason is the definition of $t$ as the ratio of an independent standard normal
to the square root of an independent chi-squared variable divided by its degrees of
freedom. With Gaussian data, $\bar X$ is normal, $(n-1)s^2/\sigma^2$ is
chi-squared with $n-1$ degrees of freedom, and the two are independent — and
$\sigma$ cancels in the ratio.

Inverting the same way gives

$$\bar X \pm t_{n-1, 1-\alpha/2}\,\frac{s}{\sqrt n}.$$

The demonstration computes the $t$ quantiles from the definition rather than
reading them from a table, and checks the routine against two independent
reference values:

```
  95 % two-sided critical values t(0.975, df):
    df =        1: t = 12.706205
    df =        2: t = 4.302653
    df =        5: t = 2.570582
    df =       15: t = 2.131450
    df =       30: t = 2.042272
    df =      100: t = 1.983972
    df =  1000000: t = 1.959966
```

Two checks confirm the routine. As the degrees of freedom grow, the value tends to
the normal $1.959964$ — at $df = 10^{6}$ it is $1.959966$. And at $df = 1$ the $t$
distribution is the Cauchy distribution, whose $0.975$ quantile is $\tan(0.475\pi)
= 12.706205$, which the routine reproduces exactly. Verifying a numerical routine
against analytic limits it must satisfy is a discipline worth keeping: it costs
one line and prevents a class of silent errors.

**The penalty for not knowing $\sigma$.** At $n = 16$, $t = 2.131450$ against
$z = 1.959964$: the interval is $8.7\%$ wider than the known-$\sigma$ interval.
The penalty is severe only for very small samples — at $df = 5$ the ratio is
$1.31$, at $df = 30$ it is $1.04$ — and it vanishes as $n^{-1}$.

## 3. Coverage, measured

**Coverage** is the probability, over repeated experiments, that the interval
contains the true parameter. For the intervals above it is $1-\alpha$ *by
construction*, but only under the model assumptions; measuring it by simulation is
both a check on the construction and a way to see how it degrades when the model is
wrong.

The demonstration runs $100\,000$ independent experiments with $\mu = 10$,
$\sigma = 2$, $n = 16$:

```
  mu = 10.0, sigma = 2.0 (known), n = 16, reps = 100,000
  half-width = 1.96 sigma/sqrt(n) = 0.979982
  nominal coverage  = 0.950000
  observed coverage = 0.950050  (binomial standard error 0.000689)
```

$0.950050$ against $0.950000$, with a binomial standard error of $0.000689$: the
observed coverage is $0.07$ standard errors from nominal. The construction is
correct, and the simulation resolves the coverage to the fourth decimal place.

The unknown-$\sigma$ interval behaves similarly for Gaussian data:

```
  n = 16, df = 15, t(0.975, 15) = 2.131450 (against 1.95996 for known sigma)
  observed coverage, Gaussian(10,2) = 0.950400
  observed coverage, Laplace(10,2)  = 0.953320
```

Both are close to $0.95$. The Laplace value is slightly *above* nominal, which is
worth understanding rather than passing over: symmetric heavy tails inflate the
sample standard deviation often enough to buy back the coverage that the occasional
outlier costs. The effect is small, and it is not a licence to assume that heavy
tails are harmless. Section 7 shows the case where the same reasoning fails
catastrophically.

## 4. What a confidence interval means

The statement

$$\bar X \pm 1.96\frac{\sigma}{\sqrt n}$$

is a claim about the *procedure*: **if the experiment were repeated many times, and
an interval constructed each time by this rule, then $95\%$ of those intervals would
contain $\mu$.**

It is not a claim that the particular interval you computed has a $95\%$ chance of
containing $\mu$. After the data are in, the interval is fixed and $\mu$ is fixed,
so either $\mu$ is inside it or it is not; the probability is $0$ or $1$, and it is
the *endpoints* that were random, not $\mu$.

The demonstration makes this concrete by showing twelve realised intervals:

```
    [  8.8954,  10.8554]  covers
    [  8.3136,  10.2736]  covers
    [  8.6890,  10.6490]  covers
    [  8.8838,  10.8437]  covers
    [ 10.0706,  12.0306]  MISSES
    [  8.7376,  10.6976]  covers
    [  8.3299,  10.2899]  covers
    [  8.7310,  10.6910]  covers
    [  8.5643,  10.5242]  covers
    [  8.9982,  10.9582]  covers
    [  9.5627,  11.5227]  covers
    [  9.3798,  11.3397]  covers
```

Eleven of twelve cover $\mu = 10$; the fifth misses because its sample mean happened
to land high. Each interval is a fixed object. Nothing about the *fourth* interval
tells you whether it covers.

### 4.1 Consequences that follow from getting this right

- **A confidence interval is a precision statement, not a belief.** It says how
  well the experiment determined the parameter under the assumed model.
- **The width, not the coverage, is the useful output.** $1 - \alpha$ is a design
  choice, conventionally $0.95$; the half-width $\sigma/\sqrt n$ times a constant is
  the information the data carry.
- **"Not significant" is not "no effect".** An interval containing zero is an
  interval of values that remain compatible with the data; if the interval is wide,
  the experiment was uninformative, which is a different statement from the effect
  being absent. Lesson 08 develops this as the power discussion.
- **Do not compare overlapping intervals as a test.** Two independent $95\%$
  intervals can overlap substantially while their difference is significant, and
  can barely overlap while it is not. To test a difference, compute the interval
  for the difference.
- **Rounding the interval is part of the result.** Quoting $750.0 \pm 26.1$ m
  implies the uncertainty itself is known to a tenth of a metre, which it is not.
  Report the width to one or two significant figures, and the estimate to the same
  decimal place.

## 5. Where the guarantee comes from, and where it does not

Coverage is guaranteed by the pivot's parameter-free distribution, and by nothing
else. Three implications:

1. **The model must be right.** The $t$ pivot requires Gaussian data. For
   non-Gaussian data the statistic $\bar X \pm t s/\sqrt n$ still has a sampling
   distribution, but it is not $t_{n-1}$ and the nominal coverage is not achieved —
   Section 7 measures how far off it can be.
2. **The data must be independent.** Positive correlation inflates the true
   standard error relative to $s/\sqrt n$, so intervals are too narrow and
   coverage falls below nominal, often silently.
3. **The parameter must be the one the pivot addresses.** The interval
   $\bar X \pm t s/\sqrt n$ is an interval for the *mean of the measured
   distribution*. If the measured distribution is biased for the physical target —
   an offset, a miscalibration, a wrong velocity — the interval is a correct
   interval for the wrong quantity. This is the failure of Section 7.2, and it is
   the most serious of the three because no diagnostic inside the data can detect
   it.

## 6. Confidence versus credible intervals

The frequentist and Bayesian constructions answer different questions, and the
difference is worth stating once, precisely.

| | Confidence interval | Credible interval |
|---|---|---|
| Statement | $P(\text{interval covers } \theta) = 1-\alpha$ over repeats | $P(\theta \in I \mid \text{data}) = 1-\alpha$ |
| Depends on a prior | No | Yes |
| Random quantity | The interval | The parameter |
| Guarantee fails when | Model is wrong, data correlated | Prior is wrong, or model is wrong |
| For flat prior, Gaussian model | Numerically equal to the credible interval | Numerically equal |

The numerical coincidence in the last row causes much of the confusion. For a
location parameter with a flat prior and Gaussian noise, the two intervals
coincide; for a scale parameter with a flat prior on the standard deviation they do
not coincide at all, because a flat prior on $\sigma$ is not flat on $\sigma^2$ or
on $1/\sigma$. Interval endpoints are not invariant under reparameterisation in the
Bayesian case, and they are also not invariant in the frequentist case if the
interval is chosen by a rule other than the pivot.

**When to use which.** A confidence interval is the right tool when the question is
about the performance of a measurement procedure, when the sampling distribution is
known, and when no prior information is available or desired. A credible interval
is the right tool when prior information genuinely exists — regional geology,
previous surveys, physical bounds — and when the question is about the parameter
itself. Bayesian intervals and their computation are developed in
[21 Statistics, Bayesian Methods and Machine Learning](../../21-statistics-bayesian-ml/README.md).

## 7. Measuring failure

### 7.1 A wrong noise model, and a heavy tail

The demonstration applies the $t$ interval to three parents with the sample
standard deviation used throughout, evaluated against each parent's true mean:

```
                    parent       n    coverage   mean half-width
   Gaussian(0,1)                16    0.949800          0.524676
   Gaussian(0,1)               256    0.952350          0.122967
   Laplace(0,1)                 16    0.954950          0.725149
   Laplace(0,1)                256    0.951450          0.173554
   Pareto(1.5) mean 3           16    0.633600          3.489186
   Pareto(1.5) mean 3          256    0.735700          0.930509
```

The Gaussian and Laplace cases are within a percentage point of nominal at both
sample sizes. The Pareto case is not close: coverage is $0.634$ at $n = 16$ and
$0.736$ at $n = 256$, against a nominal $0.95$. Increasing the sample size by a
factor of sixteen improves coverage by only ten percentage points, and the
interval is still wrong by twenty points.

Two features of that failure are instructive. First, the interval is not simply too
narrow: its mean half-width at $n = 16$ is $3.49$, enormous compared with the
Gaussian case's $0.52$, because the sample standard deviation is inflated by the
occasional huge draw. Second, its failure mode is not systematic undercoverage in
one direction — the interval is far too wide in most samples and far too narrow in
the minority of samples that contain an extreme value and hence a large sample mean.
That is exactly the instability of a variance estimate when the fourth moment does
not exist (lesson 04, Section 6.2): the interval's width is itself a random variable
with no finite variance.

**The diagnostic.** Compute the interval for the *median* rather than the mean, or
use a bootstrap interval for the median; both behave far better for tail exponents
below two. Report the tail exponent, or at least the sample size and a quantile
plot, alongside the interval.

### 7.2 A systematic offset

Now introduce a bias and see what the interval does:

```
  Systematic error is worse than any distributional misspecification.
  Target 0, every reading offset by +0.5 mGal, sigma = 1.0 mGal:
       n   half-width    coverage
      16     0.524364    0.529150
      64     0.248880    0.023850
     256     0.122961    0.000000
    1024     0.061310    0.000000
```

With a fixed offset of $0.5$ mGal, coverage is $0.529$ at $n = 16$ — the
half-width of about $0.53$ is comparable with the offset, so the interval covers
roughly half the time — and then **collapses towards zero as the sample grows**. At
$n = 256$ not one of $20\,000$ intervals contained the target. The interval narrows
as $n^{-1/2}$ while the offset does not move, so more data make the answer
confidently wrong.

This is the most important practical warning in the lesson, and it inverts the
intuition that more data is always better:

> **A confidence interval converges on the mean of the measured distribution, not
> on the physical truth. If the two differ by a systematic error, the interval
> becomes a precise statement of the systematic error.**

The remedy is not statistical. It is an independent check: a calibration against a
known standard, a cross-over tie between surveys, a comparison with an independent
method, or a repeat measurement with a different instrument. None of these can be
replaced by better error bars on the original data.

## 8. Intervals for quantities that are not means

Most quantities a geophysicist reports are not means: a depth from a travel time, a
density from mass and volume, a ratio of two fitted parameters, a return period.
Three approaches are available, in increasing order of generality.

**The delta method.** For a smooth function $g(\hat\theta)$ of an asymptotically
normal estimator, a first-order Taylor expansion gives

$$\operatorname{Var}\bigl(g(\hat\theta)\bigr) \approx
\bigl[g'(\theta)\bigr]^2 \operatorname{Var}(\hat\theta),$$

so an interval is $g(\hat\theta) \pm z \sqrt{\widehat{\operatorname{Var}}}$ with
the variance evaluated at $\hat\theta$. This is exactly the linearised propagation
of lesson 09, and it fails in the same way: for strong nonlinearity or large
relative uncertainty it understates the spread.

**Monte Carlo.** Sample the inputs from their distributions, compute the derived
quantity for each sample, and take the empirical quantiles. This handles arbitrary
nonlinearity and any distributional shape, at the cost of requiring the input
distributions to be specified; it is the method of lesson 09 and the one to use
when the analytic route is unreliable.

**The bootstrap.** Resample the data with replacement, recompute the estimator many
times, and take the empirical quantiles of the replicates (the *percentile*
interval) or a bias-corrected variant. The bootstrap requires no parametric
assumption about the noise, but it inherits the sample's tail: for heavy-tailed data
the bootstrap interval for a *mean* is miscalibrated in much the same way the $t$
interval is, while bootstrap intervals for a *median* or another quantile behave
well. The diagnostic is the same as everywhere else in this lesson: check coverage
by simulation on a synthetic dataset with a known answer before trusting an
interval in production.

**A caution on ratio intervals.** The interval for a ratio of two estimated
quantities is not obtained by dividing the endpoints of two intervals. When the
denominator can be near zero the ratio's distribution is heavy-tailed and the delta
method fails; Fieller's method or a Monte Carlo interval is required. In geophysics
this appears whenever a velocity ratio, a Poisson's ratio, or a normal-moveout
parameter is reported.

## 9. Sample size from a target width

Because the half-width of a $z$ interval is $z_{1-\alpha/2}\sigma/\sqrt n$,
rearranging gives the sample size needed for a target half-width $w$:

$$n = \left(\frac{z_{1-\alpha/2}\,\sigma}{w}\right)^{2}.$$

For $\sigma = 0.6$ mGal, a target half-width of $0.1$ mGal and $\alpha = 0.05$,

$$n = \left(\frac{1.959964 \times 0.6}{0.1}\right)^{2} = (11.76)^2 = 138.3,$$

so $139$ readings. Halving the target width to $0.05$ mGal requires
$(1.96 \times 0.6/0.05)^2 = 553.2$, that is $554$ readings — a fourfold increase,
as the square-root law demands.

The design step is where this calculation belongs. Deciding the interval width in
advance, and deriving the survey size from it, converts an aspiration ("we would
like a reliable result") into a plan, and it also makes explicit the assumption
about $\sigma$ on which the plan rests — an assumption that should come from a
pilot survey, never from optimism. Note also that the formula ignores the systematic
error floor of Section 7.2; where that floor exists, no value of $n$ delivers the
target width of *accuracy*, only of *precision*.

## 10. Assumptions and regime of validity

1. **Independence of the observations.** Without it the standard error is wrong,
   usually too small.
2. **The correct noise model.** The $t$ interval needs approximate normality of
   the estimator; that is weaker than normality of the data but still a real
   assumption, and it fails for heavy tails in a way that grows with the severity
   of the tail.
3. **A finite variance, in practice a finite fourth moment.** The interval is
   built from a sample variance and inherits its instability.
4. **No systematic error.** The guarantee concerns the measured distribution's
   mean. Systematic offsets are outside the interval's reach entirely.
5. **Asymptotics, or exactness.** The $t$ interval is exact for Gaussian data at
   every $n$; the $z$ interval is asymptotic unless $\sigma$ is known, in which
   case it is exact for Gaussian data.
6. **The right quantile.** For a one-sided claim, use a one-sided interval; a
   two-sided $95\%$ interval corresponds to a one-sided $97.5\%$ bound, and
   conflating them changes the answer.

## 11. Python demonstration

Run

```
python3 confidence_intervals.py
```

from `code/`. Standard library only — the Student-$t$ quantile routine is
implemented in the script from the definition — with seed 20240123 and offsets for
the internal blocks. Five sections: verification of the $t$ quantile against known
limits, the known-$\sigma$ $z$ interval, the unknown-$\sigma$ $t$ interval, coverage
breakdown (wrong parent and systematic offset), and the interpretation of a
realised interval. Outputs are quoted verbatim in Sections 2.2, 3, 4, 7.1 and 7.2.

**A note on the Laplace result.** The coverage of $0.953320$ in Section 3 is above
nominal, and it would be a mistake to describe heavy tails as harmless on that
basis. The same script's Section 7 measures $0.6336$ for a Pareto parent. The
difference between the two is the existence of a variance, and it is the reason
the Pareto case also fails the interval's assumption of a finite fourth moment —
which the demonstration can be extended to check by examining the width of the
Pareto intervals, whose own spread does not stabilise.

**Breaking exercise.** Reduce $\alpha$ from $0.05$ to $0.01$ in the coverage
section and predict, before running, both the wider half-width and the new observed
coverage. Then apply the same interval to a parent with $\sigma$ equal to one tenth
of the mean, so that Gaussian tails place negligible mass at negative values, and
compare coverage with the case where $\sigma$ equals the mean.

## 12. Common mistakes

1. **Saying "there is a 95 % probability that $\mu$ is in this interval".** That is
   a posterior statement; the confidence interval makes a pre-data statement about
   the procedure.
2. **Believing more data always tightens the truth.** With a systematic error the
   interval tightens on the wrong value — measurably, from coverage $0.529$ at
   $n = 16$ to zero at $n = 256$ in Section 7.2.
3. **Comparing two overlapping intervals as a test of difference.** Compute the
   interval for the difference.
4. **Ignoring correlation.** Spatial and temporal correlation inflates the true
   standard error, so the interval is too narrow and the coverage is below nominal
   without any visible symptom.
5. **Using the symmetric interval for a ratio.** When the denominator is uncertain
   and can approach zero, the ratio's distribution is asymmetric and the interval
   must be obtained by propagation, Monte Carlo, or Fieller's method.
6. **Quoting the coverage to more digits than the interval is worth.** Interval
   endpoints should be rounded to the precision the data support.
7. **Treating the interval as a decision rule.** The interval describes
   compatible values; a threshold decision requires a loss function, which is what
   hypothesis testing formalises.
8. **Assuming that a bootstrap interval always beats an analytic one.** It beats a
   wrong analytic one, and it is no better than the sample's ability to represent
   the tail.

## 13. Real-world applications

- **Reporting an anomaly.** A gravity anomaly of $2.04 \pm 0.21$ mGal, with the
  interval constructed from repeat stations and a stated $\sigma$, is a claim about
  the survey's precision that a reader can compare against a detection threshold.
- **Depth and thickness estimates.** The two-way time to depth conversion of
  lesson 09 gives an interval whose dominant term is the velocity uncertainty, not
  the timing.
- **Seismicity rates.** Counts are Poisson, and the interval for a rate is the
  standard error of a Poisson mean; the systematic component from catalogue
  incompleteness usually dominates the statistical one.
- **Trends in geodesy and climate.** Velocities from GNSS or trends from tide
  gauges are estimated with intervals whose coverage depends on the correlated
  noise model; the naive $n^{-1/2}$ interval is the classic understatement.
- **Machine-learning performance bounds.** A metric on a held-out set has an
  interval from the binomial or the bootstrap, and comparing two models requires the
  interval for the *difference*, paired on the same test items.
- **Survey design.** The formula in Section 9 is the standard planning calculation
  for precision-driven acquisition.

## 14. Further reading

- **Casella, G. and Berger, R. L. *Statistical Inference*.** Level: advanced.
  Interval estimation via pivots, the $t$ and chi-squared pivots, and the
  distinction from Bayesian intervals, in the conventional treatment.
- **Efron, B. and Tibshirani, R. J. *An Introduction to the Bootstrap*.** Level:
  advanced. The percentile and bias-corrected intervals of Section 8, with coverage
  studies that mirror the simulations here.
- **Brown, L. D., Cai, T. T. and DasGupta, A. (2001). Interval estimation for a
  binomial proportion. *Statistical Science*, 16(2), 101–133.** Level: graduate.
  The standard reference for the many ways a simple interval can fail to cover;
  directly relevant to detection fractions and success rates.
- **Neyman, J. (1937). Outline of a theory of statistical estimation based on the
  classical theory of probability. *Philosophical Transactions of the Royal Society
  A*, 236, 333–380.** Level: doctoral. The original definition of confidence
  intervals, and still the clearest statement of what the coverage property claims.
- **Morey, R. D., Hoekstra, R., Rouder, J. N., Lee, M. D. and Wagenmakers,
  E.-J. (2016). The fallacy of placing confidence in confidence intervals.
  *Psychonomic Bulletin and Review*, 23(1), 103–123.** Level: advanced. A
  careful analysis of the interpretations confidence intervals do and do not
  support; locate through your library.

> Note on citations: bibliographic details are given so the works can be located.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library.

## 15. Related lessons

- [06 Point Estimation, Bias, Consistency and Efficiency](./06-estimation-theory.md)
  — the estimators these intervals describe.
- [08 Hypothesis Testing, p-Values and Power](./08-hypothesis-testing.md) — the
  decision-theoretic companion; a $95\%$ interval corresponds to the set of
  parameter values not rejected at $5\%$.
- [09 Error and Uncertainty Propagation](./09-error-propagation.md) — intervals for
  derived quantities, including the Monte Carlo route of Section 8.
- [05 Sampling Distributions, Law of Large Numbers and CLT](./05-sampling-and-clt.md)
  — why the $z$ interval works and when it does not.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — model-space
  confidence regions, resolution and trade-off surfaces.
- [21 Statistics, Bayesian Methods and Machine Learning](../../21-statistics-bayesian-ml/README.md)
  — credible intervals, priors and the comparison with the frequentist guarantees
  measured here.

## Exercises

[`exercises/07-confidence-intervals-exercises.md`](./exercises/07-confidence-intervals-exercises.md),
with solutions in
[`exercises/07-confidence-intervals-solutions.md`](./exercises/07-confidence-intervals-solutions.md).

## Self-assessment checklist

- [ ] I can explain what a pivot is and construct an interval by inverting one.
- [ ] I can derive the known-$\sigma$ interval from the CLT and write down the
      unknown-$\sigma$ interval with its degrees of freedom.
- [ ] I can state the coverage property exactly, and explain why a realised
      interval does not have a $95\%$ probability of containing the parameter.
- [ ] I can distinguish a confidence interval from a credible interval and say
      which question each answers.
- [ ] I can describe the three ways coverage fails and give a measured example of
      each.
- [ ] I can compute the sample size needed for a stated interval width.
- [ ] I can choose between an analytic, bootstrap and Monte Carlo interval for a
      stated quantity.
- [ ] I have run `code/confidence_intervals.py` and can explain how, in the
      presence of a fixed offset, the interval becomes a *precise* statement of
      the systematic error as the sample grows.
