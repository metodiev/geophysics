---
id: 01-13-06
title: "Point Estimation, Bias, Consistency and Efficiency"
level: advanced
prereqs: ["01-13-05"]
estimated_minutes: 90
tags: [estimation, bias, consistency, efficiency, maximum-likelihood, mean-squared-error]
---

# Point Estimation, Bias, Consistency and Efficiency

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** a parameter from an estimator of it, and describe an estimator
   by its sampling distribution rather than by the single number it returns.
2. **Compute** the bias of an estimator, including Bessel's correction for the
   sample variance, and explain where the bias comes from.
3. **Decompose** the mean squared error as $\text{MSE} = \operatorname{Var} +
   \text{bias}^2$, and give an example in which the biased estimator has the
   smaller MSE.
4. **Define** consistency precisely, give sufficient conditions for it, and
   construct a biased estimator that is nevertheless consistent.
5. **Compare** estimators by variance and state the Cramér–Rao lower bound,
   including the regularity conditions under which it applies.
6. **Derive** the maximum likelihood estimator for the exponential rate and for
   the Gaussian mean and variance, and state the invariance property.
7. **Choose** between mean-like and median-like estimators on the basis of the
   assumed noise distribution, and justify the choice quantitatively.

## Prerequisites

[01-13-05 Sampling Distributions, Law of Large Numbers and CLT](./05-sampling-and-clt.md)
for sampling distributions and convergence, and
[01-13-03 Expectation, Variance and Moments](./03-expectation-variance.md) for
the moment algebra used throughout.

## 1. Parameters, statistics and estimators

A **parameter** $\theta$ is a fixed, unknown property of the population or of the
physics: the true anomaly of a body, the true velocity of a layer, the true rate
of seismicity. An **estimator** $\hat\theta$ is a function of the data, hence a
random variable, constructed to approximate the parameter. The value it returns
for a particular dataset is an **estimate**.

The distinction is not pedantic. Every statement about an estimator's quality —
unbiased, consistent, efficient — is a statement about its sampling distribution,
and none of them can be evaluated from a single estimate. A useful discipline is
to write $\hat\theta$ as an explicit function of the data, so that its randomness
is visible.

Everything in this lesson is aimed at a single practical question: given several
defensible ways to estimate the same quantity, which should be reported, and why?

## 2. Bias

The **bias** of an estimator is

$$\text{bias}(\hat\theta) = E[\hat\theta] - \theta.$$

An estimator with zero bias for every admissible $\theta$ is **unbiased**.

### 2.1 Bessel's correction

The sample variance illustrates bias, and its correction, in the cleanest possible
way. Define

$$s_n^2 = \frac{1}{n}\sum_{i=1}^{n}(X_i - \bar X)^2, \qquad
s_{n-1}^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar X)^2,$$

for i.i.d. $X_i$ with mean $\mu$ and variance $\sigma^2$. To find $E[s_n^2]$, expand
about the true mean:

$$\sum_{i=1}^{n}(X_i - \bar X)^2 = \sum_{i=1}^{n}(X_i - \mu)^2
- n(\bar X - \mu)^2,$$

using $\sum (X_i - \bar X)^2 = \sum (X_i - \mu)^2 - n(\bar X - \mu)^2$, which
follows from $\sum(X_i - \mu) = n(\bar X - \mu)$. Taking expectations,

$$E\left[\sum_{i=1}^{n}(X_i - \bar X)^2\right] = n\sigma^2 - n\frac{\sigma^2}{n}
= (n-1)\sigma^2,$$

so

$$E[s_n^2] = \frac{n-1}{n}\sigma^2, \qquad E[s_{n-1}^2] = \sigma^2.$$

The bias of $s_n^2$ is exactly $-\sigma^2/n$. Its origin is that deviations are
measured from $\bar X$, which is itself fitted to the data; the fit absorbs one
degree of freedom and the residuals are systematically too small. Dividing by
$n-1$ instead of $n$ is **Bessel's correction**.

The demonstration verifies both expectations by simulation with $\sigma^2 = 4$,
$n = 5$, $100\,000$ replicates and seed 20240122:

```
  parent variance sigma^2 = 4.0, n = 5, reps = 100,000
  E[sum (x-m)^2 / n]     analytic = 3.200000  simulated = 3.202382
  E[sum (x-m)^2 / (n-1)] analytic = 4.000000  simulated = 4.002977
  relative bias of the n-divisor estimator = -0.199405 (theory -0.200000)
```

Both agree with theory, and the relative bias is $-20\%$ at $n = 5$: a substantial
understatement in a small sample. At $n = 100$ the same bias is $-1\%$, which is
why the choice between the two divisors matters more in a five-station survey than
in a hundred-station one — and why the correction is applied by convention rather
than by judgement.

### 2.2 Where bias comes from

Three sources, and they behave differently:

- **Finite-sample bias**, as above. It vanishes as $n$ grows and is computable.
- **Nonlinearity bias.** If $\hat\theta$ is a nonlinear function of an unbiased
  estimator, it is generally biased (lesson 03, Section 6). The exponential rate
  estimator $\hat\lambda = 1/\bar X$ is the standard example: $\bar X$ is unbiased
  for $1/\lambda$ but $1/\bar X$ is biased for $\lambda$, with
  $E[\hat\lambda] = n\lambda/(n-1)$.
- **Model bias.** If the estimator is derived under a model that does not hold —
  a Gaussian likelihood for heavy-tailed noise, an isotropic prior for a layered
  medium — the resulting bias does *not* vanish as $n$ grows. It is the most
  dangerous kind, because more data make the wrong answer more precise.

## 3. Variance, mean squared error, and the trade-off

An estimator is judged by how close it typically lands, and the natural summary is
the **mean squared error**:

$$\text{MSE}(\hat\theta) = E\left[(\hat\theta - \theta)^2\right]
= \operatorname{Var}(\hat\theta) + \text{bias}(\hat\theta)^2.$$

The decomposition follows from adding and subtracting $E[\hat\theta]$ inside the
square and using $E[\hat\theta - E\hat\theta] = 0$:

$$
E\left[(\hat\theta - \theta)^2\right]
= E\left[\left((\hat\theta - E\hat\theta) + (E\hat\theta - \theta)\right)^2\right]
= \operatorname{Var}(\hat\theta) + \text{bias}^2,
$$

the cross term vanishing because the first factor has mean zero.

**The trade-off is real.** Because the two terms enter additively, it can be worth
accepting a bias in exchange for a larger reduction in variance. The sample
variance is the canonical example, and the demonstration quantifies it:

```
       estimator      variance        bias^2           MSE
             1/n      5.092418      0.639060      5.731479
         1/(n-1)      7.956904      0.000001      7.956904
  theory: Var(1/(n-1)) = 2 sigma^4/(n-1) = 8.000000
          Var(1/n)     = 2 sigma^4 (n-1)/n^2 = 5.120000
```

The biased estimator has the **smaller** mean squared error — $5.73$ against
$7.96$ — because its variance is lower by more than the square of its bias. For
Gaussian data the ratio of the MSEs is $(n-1)^2/n^2 \cdot$ (a correction):
explicitly, $\text{MSE}(s_n^2)/\sigma^4 = 2(n-1)/n^2 + 1/n^2$, which is less than
$2/(n-1)$ whenever $n > 1$. So for a Gaussian parent, dividing by $n$ gives a
better estimator of $\sigma^2$ in the MSE sense than dividing by $n-1$, at every
sample size.

**What to do with that fact.** It does not mean Bessel's correction is wrong. It
means that unbiasedness is one criterion among several, and that the criterion must
be stated before the estimator is chosen. Unbiasedness is valuable when the
estimator will be *averaged* over many independent problems — an unbiased estimator
makes that average converge to the right thing, and no such guarantee exists without
it. MSE is valuable when the accuracy of one estimate is what matters. State the
loss function, then choose.

## 4. Consistency

An estimator is **consistent** for $\theta$ if

$$\hat\theta_n \xrightarrow{P} \theta, \qquad \text{that is} \qquad
P\left(\left|\hat\theta_n - \theta\right| > \varepsilon\right) \to 0
\quad \text{for every } \varepsilon > 0.$$

A **sufficient** condition, and the one used in practice, is that both the bias and
the variance go to zero:

$$\text{bias}(\hat\theta_n) \to 0 \quad \text{and} \quad
\operatorname{Var}(\hat\theta_n) \to 0 \quad \Longrightarrow \quad
\text{consistency}.$$

This follows from Chebyshev's inequality applied to $\hat\theta_n - E[\hat\theta_n]$
together with $|E\hat\theta_n - \theta| \to 0$.

**A biased estimator can be consistent.** Consistency is a statement about the
limit, and bias is a property at fixed $n$. The demonstration makes this concrete
with an estimator of a mean equal to the sample mean plus a deliberately
introduced bias that decays as $3/n$:

```
       n    sd(mean) sim     sd theory   mean of biased est
       4        0.498092      0.500000             5.749089
      16        0.249306      0.250000             5.186389
      64        0.124213      0.125000             5.046410
     256        0.062105      0.062500             5.011930
    1024        0.031220      0.031250             5.002845
```

The spread follows $\sigma/\sqrt n$ exactly, and the mean of the biased estimator
falls from $5.749$ to $5.003$ as the bias $3/n$ decays. Both terms vanish, so the
estimator is consistent, and it is biased at every finite $n$.

The converse warning also matters: an unbiased estimator need not be consistent.
Take $\hat\theta = X_1$, the first observation, as an estimator of the mean. It is
unbiased for any $n$, because $E[X_1] = \mu$, and its variance is $\sigma^2$ for
every $n$, so it never converges. **Unbiased and consistent are independent
properties.**

## 5. Efficiency and the Cramér–Rao bound

Among unbiased estimators, the natural comparison is variance. The **relative
efficiency** of two unbiased estimators is the ratio of their variances, and an
estimator is **efficient** if its variance attains the lowest possible value.

For regular parametric families there is a floor. Let $f(x \mid \theta)$ be the
density and define the **Fisher information** for one observation,

$$I(\theta) = E\left[\left(\frac{\partial \ln f(X \mid \theta)}
{\partial \theta}\right)^2\right].$$

Then, under regularity conditions — the density is differentiable in $\theta$, the
support does not depend on $\theta$, and differentiation under the integral sign is
permitted — every unbiased estimator satisfies the **Cramér–Rao lower bound**:

$$\operatorname{Var}(\hat\theta) \ge \frac{1}{n\,I(\theta)}.$$

The regularity conditions are not decorative. The uniform distribution on
$(0, \theta)$ has a support that depends on $\theta$, so the bound does not apply,
and in fact the estimator $\hat\theta = \max_i X_i$ has variance of order
$\theta^2/n^2$ — far below the bound one would compute by differentiating anyway.
That example is a useful reminder that a bound is only as good as its hypotheses.

### 5.1 Information in the Laplace and Gaussian models

For the Gaussian $\mathcal{N}(\mu, 1)$, $\ln f = -\tfrac12(x-\mu)^2 + \text{const}$,
so $\partial_\mu \ln f = x - \mu$ and $I(\mu) = E[(X-\mu)^2] = 1$. The bound for $n$
observations is $\operatorname{Var}(\hat\mu) \ge 1/n$, and the sample mean attains
it. The mean is efficient.

For the Laplace distribution with density $f(x) = \frac{1}{2b}e^{-|x - \mu|/b}$,
the log-density is $-\ln(2b) - |x-\mu|/b$, whose derivative with respect to $\mu$ is
$\operatorname{sgn}(x - \mu)/b$ wherever $x \ne \mu$. Hence

$$I(\mu) = E\left[\frac{1}{b^2}\right] = \frac{1}{b^2},
\qquad \operatorname{Var}(\hat\mu) \ge \frac{b^2}{n}.$$

The sample median attains this bound asymptotically, since for any density the
sample median satisfies $\sqrt n(\tilde X - \mu) \to \mathcal{N}(0,
1/(4f(\mu)^2))$ and here $f(\mu) = 1/(2b)$, giving variance $b^2/n$. The sample
mean, by contrast, has variance $2b^2/n$. So in the Laplace model **the mean has
relative efficiency one half**: it wastes half of the information in the data.

This is a clean and useful result. For an exponential-tailed noise distribution —
Laplace is a two-sided exponential — the median is a better estimator of location
than the mean, and not by a small margin.

## 6. Comparing estimators on simulation

The demonstration compares four location estimators for $n = 25$ with $20\,000$
replicates: the mean, the median, the midrange $(X_{(1)} + X_{(n)})/2$, and a
$10\%$ trimmed mean. The target is location $0$ with $n = 25$:

```
  Gaussian(0,1), n = 25, reps = 20,000   (MSE against the true location 0)
    mean       MSE = 0.039033   variance = 0.039032   bias = +0.001791
    median     MSE = 0.060781   variance = 0.060783   bias = +0.001041
    midrange   MSE = 0.134035   variance = 0.134041   bias = +0.000969
    trim 10%   MSE = 0.040500   variance = 0.040499   bias = +0.001934
    most efficient: mean

  Laplace(0,1) , n = 25, reps = 20,000   (MSE against the true location 0)
    mean       MSE = 0.081046   variance = 0.081035   bias = -0.003908
    median     MSE = 0.054396   variance = 0.054396   bias = -0.001670
    midrange   MSE = 0.828168   variance = 0.827930   bias = -0.016712
    trim 10%   MSE = 0.064476   variance = 0.064473   bias = -0.002445
    most efficient: median
    MSE(mean)/MSE(median) = 1.4899 at n = 25 (asymptotic value 2)
```

Four conclusions, each of them checkable against theory:

- **The Gaussian case matches the Cramér–Rao bound.** The mean's MSE is $0.03903$
  against $1/25 = 0.04000$, and its bias is $0.0018$, comparable to the Monte Carlo
  standard error of an estimated mean with $20\,000$ replicates. The simulation and
  the bound agree.
- **The Gaussian median matches its asymptotic variance.** Theory gives
  $1/(4nf(0)^2) = 2\pi/(4n) = 0.0628$; the simulation returns $0.0608$.
- **The Laplace case confirms the efficiency loss.** The mean's MSE is $0.0810$
  against the predicted $2b^2/n = 0.0800$; the median's is $0.0544$ against the
  bound of $0.0400$. The median wins, but by a factor of $1.49$ rather than the
  asymptotic $2$. The asymptotic result is a *large-sample* statement and $n = 25$
  is not large for a Laplace parent: the median's own standard error is of order
  $1/\sqrt{2n}$ in relative terms, so the shortfall is expected.
- **The midrange is a disaster for heavy tails.** For the Laplace parent its MSE of
  $0.828$ is fifteen times the median's. The midrange uses only the two extreme
  order statistics, and extremes of a heavy-tailed distribution are exactly the
  observations that carry the least information about the centre. It performs
  respectably for the uniform parent — where the extremes do bound the range —
  which is why the midrange is a reasonable estimator in some contexts and a trap
  in others.

**Which estimator is efficient is a statement about the noise model, not a
universal fact.** There is no "best estimator of a location parameter"; there is
only the best estimator given an assumed distribution.

## 7. Maximum likelihood

The **likelihood** of a parameter given data is the joint density evaluated at the
observed data, viewed as a function of the parameter:

$$L(\theta) = \prod_{i=1}^{n} f(x_i \mid \theta).$$

The **maximum likelihood estimator (MLE)** $\hat\theta_{\text{MLE}}$ maximises $L$,
equivalently maximises the log-likelihood $\ell(\theta) = \sum_i \ln f(x_i \mid
\theta)$. Two examples, derived rather than quoted.

**Exponential rate.** With $f(x \mid \lambda) = \lambda e^{-\lambda x}$ for
$x \ge 0$,

$$\ell(\lambda) = n\ln\lambda - \lambda\sum_{i=1}^{n} x_i,
\qquad \frac{d\ell}{d\lambda} = \frac{n}{\lambda} - \sum_i x_i = 0
\ \Longrightarrow\ \hat\lambda = \frac{1}{\bar X}.$$

The second derivative $-n/\lambda^2 < 0$ confirms a maximum. The estimator is
**biased**: $\bar X$ is gamma distributed, and $E[1/\bar X] = n\lambda/(n-1)$ for
$n > 1$. It is nevertheless **consistent**, since the bias is of order
$\lambda/n$ and the variance is of order $\lambda^2/n$; both vanish. Its
asymptotic variance is $\lambda^2/n$, matching the Cramér–Rao bound
$1/(nI(\lambda))$ with $I(\lambda) = 1/\lambda^2$. This is the typical MLE
pattern: finite-sample bias, asymptotic efficiency.

**Gaussian mean and variance.** With
$\ell(\mu, \sigma^2) = -\tfrac{n}{2}\ln(2\pi\sigma^2)
- \frac{1}{2\sigma^2}\sum_i (x_i - \mu)^2$, differentiating gives

$$\hat\mu = \bar X, \qquad \hat\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar X)^2.$$

The MLE of the variance is the biased $n$-divisor estimator of Section 2 — a
neat illustration that maximum likelihood does not promise unbiasedness, only
efficiency in the large-sample sense.

### 7.1 Properties worth stating

- **Invariance.** If $\hat\theta$ is the MLE of $\theta$, then $g(\hat\theta)$ is
  the MLE of $g(\theta)$ for any function $g$. So the MLE of the variance is the
  square of the MLE of the standard deviation, and the MLE of a ratio is the ratio
  of the MLEs. This is not true of unbiased estimators, and it is the practical
  reason to prefer MLE when a derived quantity is the object of interest.
- **Asymptotic normality and efficiency.** Under regularity, $\hat\theta_{\text{MLE}}$
  is approximately $\mathcal{N}(\theta, 1/(nI(\theta)))$ for large $n$: it attains
  the Cramér–Rao bound asymptotically. This is what makes standard errors from a
  likelihood machinery automatic.
- **Parameterisation dependence.** MLEs are invariant under reparameterisation;
  the *bias* is not, and neither is the shape of the sampling distribution.
- **Failure modes.** With a small sample, a flat or multi-modal likelihood, or a
  parameter on the boundary of its range, the asymptotic properties say nothing,
  and the MLE can be badly biased or even inconsistent.

## 8. Robustness, and the choice of estimator

The comparison in Section 6 shows that the mean is best when the noise is
Gaussian and the median is best when it is Laplace. Real data are neither, and the
honest question is: **how much is lost by choosing the wrong one?**

- Against the Gaussian, using the median instead of the mean costs a factor of
  about $1.57$ in variance — real, but modest.
- Against the Laplace, using the mean instead of the median costs a factor of
  about $1.5$ at $n = 25$ and $2$ asymptotically — the same order.
- Against a heavy-tailed contamination — say $1\%$ of observations drawn from a
  distribution with ten times the spread — the mean's variance can increase by an
  order of magnitude while the median's hardly moves at all.

This asymmetry in the *consequences* of getting the model wrong is what motivates
robust estimation. The **breakdown point** of an estimator is the smallest
fraction of contaminated observations that can make it arbitrarily wrong; the mean
has breakdown point $0$ (one arbitrarily large observation moves it arbitrarily),
while the median has $0.5$. The trimmed mean interpolates: trimming $10\%$ gives a
breakdown point of $10\%$ while retaining almost the Gaussian efficiency of the
mean, which is why the trimmed mean's MSE of $0.0405$ in Section 6 is so close to
the mean's $0.0390$ in the Gaussian case and so much better in the Laplace case.

**Practical guidance.** Report the mean when the noise model is defensible and the
sample has been screened for gross errors; report the median when outliers are
expected, when the tail is heavy, or when a breakdown point of $0.5$ is worth the
efficiency loss. In either case, report both when they disagree materially, and
treat the disagreement as evidence about the tail rather than as a nuisance to be
resolved by preference.

## 9. Assumptions and regime of validity

1. **The model must hold.** Bias and efficiency are properties relative to a
   specified family. An estimator that is efficient under the wrong model is
   precisely wrong.
2. **The moment must exist for the estimator to have a variance.** For heavy-tailed
   data, quoting an efficiency comparison based on variances is meaningless.
3. **Cramér–Rao needs regularity.** Differentiability in the parameter and a
   support that does not move with it. Boundary and truncation problems are
   routinely encountered in geophysics — a non-negative velocity, a bounded
   magnitude — and the bound must not be applied to them without checking.
4. **Consistency is asymptotic.** Every finite dataset has some bias. Consistency
   says the bias will eventually be small; it does not say it is small now.
5. **Efficiency comparisons assume a fixed model for the data.** They say nothing
   about robustness to model error. The two criteria can point in opposite
   directions, as Sections 6 and 8 show.
6. **The estimator's sampling distribution must be known to report an
   uncertainty.** For the mean this is the CLT; for the median it is the
   quantile asymptotics; for a ratio it is the delta method. An estimator without a
   known sampling distribution can still be reported, but not with a defensible
   error bar.

## 10. Python demonstration

Run

```
python3 estimation_theory.py
```

from `code/`. Standard library only; seed 20240122, with $+1$ to $+4$ for the
internal blocks. Four sections: the bias of the sample variance, consistency with
a biased estimator, efficiency of four location estimators under two parents, and
the MSE decomposition for the two variance estimators. Outputs are quoted in
Sections 2.1, 3, 4 and 6.

**A note on Monte Carlo resolution.** The efficiency table's differences between
the mean and the $10\%$ trimmed mean in the Gaussian case ($0.03903$ against
$0.04050$) are of the same order as the Monte Carlo standard error of the MSE
estimates — roughly $s^2\sqrt{2/\text{reps}}$ — so the ordering is meaningful but
the gap is not resolved to three digits. Reporting "the mean is 3.6 % more
efficient" from that table would over-read the simulation. The Laplace contrast,
by contrast, is a 50 % effect and is unambiguous.

**Breaking exercise.** Add a contaminated-Gaussian case: with probability $0.99$
draw $\mathcal{N}(0,1)$ and with probability $0.01$ draw $\mathcal{N}(0,10^2)$.
Predict, before running, which estimator loses the most MSE, then check. Then
compute the theoretical variance of the contaminated distribution,
$\sigma^2 = 1 + 0.01(100 - 1)$, and compare the mean's observed MSE with
$\sigma^2/25$.

## 11. Common mistakes

1. **Confusing an estimate with an estimator.** "The mean is 5.3" is an estimate;
   "the mean is an unbiased estimator of $\mu$" is a property of the estimator.
2. **Assuming unbiased means accurate.** Unbiasedness says nothing about variance;
   the ratio of two unbiased estimators is generally biased.
3. **Applying Bessel's correction everywhere.** It corrects the variance for
   deviations from a *fitted* mean. If the true mean is known, dividing by $n$ is
   correct; if a nonlinear model with $p$ parameters has been fitted, the
   appropriate divisor is $n - p$.
4. **Reporting an efficiency comparison without stating the model.** Efficiency is
   relative to a family; the sentence "$A$ is more efficient than $B$" is
   incomplete without "under the Gaussian model".
5. **Ignoring the effect of rounding or censoring.** Both change the effective
   likelihood and hence the efficiency ranking.
6. **Quoting a standard error for an estimator whose variance does not exist.**
   The MLE of a Pareto exponent is a case in point.
7. **Treating a large-sample result as valid at your sample size.** Section 6 shows
   the asymptotic ratio of $2$ appearing as $1.49$ at $n = 25$.
8. **Using the mean on skewed raw data.** For lognormal permeability, the
   arithmetic mean is not the parameter of a multiplicative process; the median or
   the geometric mean is.

## 12. Real-world applications

- **Anomaly amplitudes.** Averaging repeat gravity readings estimates the anomaly
  with standard error $\sigma/\sqrt n$; the choice of trimmed mean versus mean
  determines sensitivity to a single bad reading at a station.
- **Velocity estimation from travel times.** The MLE of a slowness from noisy
  picks is a weighted mean for Gaussian errors and a median-like statistic for
  Laplace errors; choosing the wrong one costs a factor of two in variance.
- **Seismicity rate estimation.** The MLE for a Poisson rate is the count divided
  by the exposure, with standard error from the CLT; catalogue incompleteness
  introduces a model bias that does not vanish with more data.
- **Lognormal petrophysics.** The MLE of a lognormal mean is not the exponential of
  the MLE of the log-mean, in the sense that the two differ in bias; the invariance
  property says the MLE of the median is $e^{\hat\mu}$, and reporting that is both
  simpler and more robust.
- **Sensor calibration.** If the calibration curve is nonlinear, the estimator of a
  physical quantity from an instrument reading is biased by the curvature, and the
  bias must be corrected from the calibration's known systematic behaviour.
- **Combining datasets.** Weighted means with weights proportional to inverse
  variances are the efficient combination under independence; under correlation,
  the covariance matrix replaces the variance vector and the optimal weights solve
  a linear system.

## 13. Further reading

- **Casella, G. and Berger, R. L. *Statistical Inference*.** Level: advanced.
  Point estimation, sufficiency, the Cramér–Rao inequality and maximum likelihood
  are all treated here in the conventional order, with exercises.
- **Lehmann, E. L. and Casella, G. *Theory of Point Estimation*.** Level: doctoral.
  The comprehensive reference, including the decision-theoretic framing of the
  bias-variance trade-off.
- **Huber, P. J. and Ronchetti, E. M. *Robust Statistics*.** Level: graduate. The
  classical source on breakdown points, influence functions and trimmed estimators.
- **Efron, B. and Hastie, T. *Computer Age Statistical Inference*.** Level:
  advanced. Connects the classical estimator comparisons here with resampling and
  regularised estimation, where bias is deliberately introduced.
- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: graduate. Maximum likelihood and least squares as
  special cases of a general inverse formulation, which is the form in which these
  ideas appear in geophysics.

> Note on citations: bibliographic details are given so the works can be located.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library.

## 14. Related lessons

- [03 Expectation, Variance and Moments](./03-expectation-variance.md) — variance,
  covariance and the shared-error floor.
- [05 Sampling Distributions, Law of Large Numbers and CLT](./05-sampling-and-clt.md)
  — the machinery that makes consistency and asymptotic normality work.
- [07 Confidence Intervals and Their Correct Interpretation](./07-confidence-intervals.md)
  — the interval version of the sampling distribution computed here.
- [08 Hypothesis Testing, p-Values and Power](./08-hypothesis-testing.md) — the
  decision-theoretic counterpart of estimation.
- [09 Error and Uncertainty Propagation](./09-error-propagation.md) — how the
  variance of an estimator propagates into a derived quantity.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — maximum likelihood
  and least squares in the setting where they are actually used.

## Exercises

[`exercises/06-estimation-theory-exercises.md`](./exercises/06-estimation-theory-exercises.md),
with solutions in
[`exercises/06-estimation-theory-solutions.md`](./exercises/06-estimation-theory-solutions.md).

## Self-assessment checklist

- [ ] I can define bias, variance, MSE and consistency, and state which are
      properties of the estimator rather than of an estimate.
- [ ] I can derive $E[s_n^2] = (n-1)\sigma^2/n$ from the expansion about the true
      mean.
- [ ] I can decompose an MSE and give an example where the biased estimator wins.
- [ ] I can construct a biased estimator that is consistent, and an unbiased
      estimator that is not.
- [ ] I can compute Fisher information for the Gaussian and Laplace models, state
      the Cramér–Rao bound, and name the regularity condition that the uniform
      family violates.
- [ ] I can derive the MLE for the exponential rate and for the Gaussian mean and
      variance, and state the invariance property.
- [ ] I can choose between the mean, the median and a trimmed mean for a stated
      noise model, and give the efficiency cost in each direction.
