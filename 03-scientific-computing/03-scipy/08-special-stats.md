---
id: 03-03-08
title: "scipy.special and scipy.stats in Practice"
level: advanced
prereqs: ["03-03-01", "03-03-03", "01-13-06", "01-13-08"]
estimated_minutes: 90
tags: [special-functions, statistics, distributions, goodness-of-fit, error-function]
---

# scipy.special and scipy.stats in Practice

Two subpackages, two kinds of number. `scipy.special` supplies the named
functions that appear in analytical solutions — the error function, the gamma
function, Bessel functions, the incomplete integrals — computed accurately
over their whole range, including the ranges where the naive expression
underflows. `scipy.stats` supplies distributions and the inference that goes
with them: fitting, testing, correlation, intervals.

The lesson treats them together because they meet in exactly the place
geophysics needs them. A diffusion solution is an error function evaluated at
a depth of several diffusion lengths, where `erfc` underflows and its scaled
form does not. And a magnitude–frequency relation is an exponential
distribution fitted to a truncated sample, where the estimator, the standard
error and the goodness-of-fit test each have a trap that produces a
plausible-looking wrong answer.

Run the demonstration before reading on:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/special_stats_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Evaluate** the error-function family (`erf`, `erfc`, `erfcx`, `ndtr`,
   `erfinv`) and pick the member that is accurate over the argument range in
   front of you.
2. **Recognise** the two failure modes at large argument — cancellation in
   $1-\mathrm{erf}(x)$ and underflow of $\mathrm{erfc}(x)$ — and state where
   each one bites.
3. **Use** the asymptotic form of `erfc` and quantify its relative error as a
   function of $x$.
4. **Fit** a Gutenberg–Richter magnitude distribution by maximum likelihood,
   and explain why the cumulative least-squares alternative that dominates the
   literature is biased.
5. **Compute** a goodness-of-fit p-value that accounts for estimated
   parameters, and **explain** why the naive Kolmogorov–Smirnov p-value does
   not.
6. **Interpret** correlation coefficients together with their sample size,
   and use the $t$ distribution rather than the normal for a small regression.
7. **Choose** between a normal and a lognormal model from the data, using a
   likelihood and a test rather than a habit.

## Prerequisites

- [03-03-01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — the subpackage map.
- [03-03-03 scipy.optimize](./03-optimize.md) — fitting, and what an error bar
  means.
- [01-13-06 Estimation Theory](../../01-mathematics/13-probability-and-statistics-foundations/06-estimation-theory.md)
  — maximum likelihood and the standard error of an estimator.
- [01-13-08 Hypothesis Testing](../../01-mathematics/13-probability-and-statistics-foundations/08-hypothesis-testing.md)
  — what a p-value is and how a test statistic's null distribution is
  constructed.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
  — the diffusion solution evaluated in §2.

## 1. The diffusion solution, and the error-function family

The temperature response of a half-space to a step change $\Delta T$ at the
surface is

$$\frac{T(z,t)}{\Delta T} = \mathrm{erfc}\!\left(\frac{z}{2\sqrt{\kappa t}}\right) , \tag{1}$$

with $\kappa$ the thermal diffusivity. For a nominal rock with
$\kappa = 1.2\times10^{-6}$ m² s⁻¹ and $\Delta T = 12$ K:

```
       t (yr)   z (m)   z/(2 sqrt(kappa t))       T/dT     T (K)
          100      50              0.406254   0.565609    6.7873
          100      200              1.625015   0.021555    0.2587
          100      1000              8.125075   0.000000    0.0000
         1000      50              0.128469   0.855832   10.2700
         1000      1000              2.569374   0.000279    0.0034
        10000      1000              0.812508   0.250532    3.0064
```

Read the argument column: it is the depth in units of the diffusion length
$2\sqrt{\kappa t}$, so $\mathrm{erfc}$ is being asked for values at arguments
from 0.04 to **8.13**. At 8.125, $\mathrm{erfc}$ is $1.47\times10^{-30}$ and the
temperature is $1.8\times10^{-29}$ K, printed as 0.0000 — the physics is
"nothing has arrived yet", and the number confirms it.

The surface heat-flow perturbation is the same solution differentiated, and it
is one of the few geophysical quantities that can be computed from a closed
form without any numerical step at all:

$$q(t) = \frac{k\,\Delta T}{\sqrt{\pi\kappa t}} . \tag{2}$$

At $t = 1000$ yr with $k = 2.5$ W m⁻¹ K⁻¹ the demo reports
**86.9769 mW m⁻²**, and at 10 000 yr **27.5045 mW m⁻²**, exactly $1/\sqrt{10}$
of it. That first number is worth pausing on: a 12 K surface step produces a
terrestrial-heat-flow-scale perturbation at 1000 yr, which is why borehole
palaeoclimate corrections matter and why the $\Delta T$ in a palaeoclimate
study must be small to be consistent with the measured present-day heat flow.

### 1.1 Three functions, one value

```
          x             erfc(x)    2*ndtr(-x sqrt2)            1-erf(x)   difference
       0.00  1.0000000000000000  1.0000000000000000  1.0000000000000000     0.00e+00
       0.50  0.4795001221869535  0.4795001221869534  0.4795001221869535     1.11e-16
       1.00  0.1572992070502852  0.1572992070502851  0.1572992070502852     1.11e-16
       3.00  0.0000220904969986  0.0000220904969986  0.0000220904969986     8.81e-20
```

The identity is $\mathrm{erfc}(x) = 2\Phi(-x\sqrt2)$, where $\Phi$ is the
standard normal CDF that `scipy.special.ndtr` computes — the error function is
a normal probability in disguise. The three expressions agree to round-off
**for small $x$**. As $x$ grows they stop agreeing, and the difference is
not round-off but representation:

```
        x         erfc(x)      1 - erf(x)        erfcx(x)   asymptotic erfc  relative error
      1.0    1.572992e-01    1.572992e-01    4.275836e-01      2.075537e-01        3.19e-01
      4.0    1.541726e-08    1.541726e-08    1.369995e-01      1.587279e-08        2.95e-02
      8.0    1.122430e-29    0.000000e+00    6.998517e-02      1.131067e-29        7.69e-03
     16.0   2.328486e-113    0.000000e+00    3.519338e-02     2.333016e-113        1.95e-03
     26.0   5.663192e-296    0.000000e+00    2.168358e-02     5.667375e-296        7.39e-04
     30.0    0.000000e+00    0.000000e+00    1.879589e-02      0.000000e+00             nan
```

Three regimes, and they overlap:

- **Small argument ($x \lesssim 3$).** `erf`, `erfc` and `ndtr` are all safe;
  use whichever reads most naturally.
- **Moderate argument ($3 \lesssim x \lesssim 26$).** $\mathrm{erfc}(x)$ is
  representable down to $10^{-296}$, but $1 - \mathrm{erf}(x)$ is **exactly
  zero** from $x = 8$ onward, because subtracting two numbers that agree to
  sixteen digits leaves nothing. This is *cancellation*, and it is silent:
  the routine returns 0.0, not an error.
- **Large argument ($x \gtrsim 26$).** $\mathrm{erfc}(x)$ itself underflows to
  zero between $x = 26$ and $x = 30$. The scaled form
  $\mathrm{erfcx}(x) = e^{x^2}\mathrm{erfc}(x)$ remains finite — it is
  $1.88\times10^{-2}$ at $x = 30$ — and the asymptotic form
  $e^{-x^2}/(x\sqrt\pi)$ is a good approximation with a *quantified* error:
  7.7 parts in $10^3$ at $x = 8$, 1.95 parts in $10^3$ at $x = 16$ and
  7.4 parts in $10^4$ at $x = 26$.

> **The rule for the whole family.** If you need $\mathrm{erfc}$ at a large
> argument, ask for `erfcx` and multiply by $e^{-x^2}$ yourself, or use the
> asymptotic form and state its relative error. If you are tempted to write
> `1 - erf(x)`, write `erfc(x)` instead — the two are the same mathematically
> and not the same numerically.

In a diffusion problem the large-argument regime is the *interesting* one:
$z/2\sqrt{\kappa t} = 6$ means the temperature has fallen to $2\times10^{-17}$
of the surface step, and a model that reports exactly zero there cannot be
inverted for a small $\kappa$ or a small time, because the information has been
rounded away.

## 2. A magnitude distribution, fitted three ways

The Gutenberg–Richter relation states that the number of events above
magnitude $m$ decays as $N(m) \propto 10^{-bm}$. Equivalently, magnitudes above
a completeness threshold $m_c$ are **exponentially distributed** with scale
$1/(b\ln 10)$:

$$p(m \mid m_c) = \beta e^{-\beta(m-m_c)}, \qquad \beta = b\ln 10 . \tag{3}$$

The demo draws 1500 synthetic magnitudes with $m_c = 2.0$ and $b = 1.0$:

```
  1500 SYNTHETIC magnitudes, completeness threshold Mc = 2.0,
  true b-value = 1.00 (exponential scale 1/(b ln10) = 0.434294).
  Sample: min 2.000, mean 2.442, max 5.595
```

### 2.1 Maximum likelihood, in closed form

For the exponential the maximum-likelihood estimator is an explicit formula —
the *Aki–Utsu* estimator:

$$\hat\beta = \frac{1}{\bar m - m_c}, \qquad \hat b = \frac{\hat\beta}{\ln 10},
\qquad \mathrm{SE}(\hat b) = \frac{\hat b}{\sqrt n} . \tag{4}$$

```
    b_hat          = 0.981599
    standard error = b_hat/sqrt(n) = 0.025345
    truth          = 1.000000   difference = -0.726 standard errors
    stats.expon.fit(floc=0) gives scale = 0.442436 -> b = 0.981599
    the two agree to 4.441e-16: the closed form is the fit.
```

The general-purpose `stats.expon.fit` reproduces the closed form to
$4.4\times10^{-16}$, which is the useful confirmation: **the numerical
optimiser and the analytics agree, so the estimator is implemented correctly
and the remaining uncertainty is statistical.** The estimate is 0.73 standard
errors from the truth, which is what a well-behaved estimator should give.

### 2.2 Cumulative least squares, and its measured bias

Most published b-value maps do not use equation (4). They bin the catalogue,
compute $\log_{10}N$ for $N$ events with $M \ge m$, and fit a straight line to
that cumulative curve. The demo does the same:

```
    slope = -0.852307 -> b = 0.852307 (standard error 0.017304, r^2 = 0.986180)
    bias against the MLE: -0.129293, i.e. -13.17%
```

A **13.2% underestimate** of $b$ on 1500 well-behaved events, with an $r^2$ of
0.986 and a quoted standard error of 0.017 — an error bar that is wrong by a
factor of seven and points the wrong way. Both defects have the same cause:
**the cumulative counts are not independent.** Each event appears in every bin
below its magnitude, so the "data" being fitted are 1500-times-repeated
counts of the same events, and the least-squares formula that assumes
independent errors is not applicable.

The moral is not that least squares is wrong. It is that **a routine which
assumes independent errors will not tell you when they are not independent.**
The fit converged, the $r^2$ is high, and the answer is 13% low.

### 2.3 Goodness of fit, and the p-value that is not valid

Comparing an empirical CDF with a fitted one is a Kolmogorov–Smirnov test, and
`stats.kstest` computes it:

```
    D against the *fitted* exponential      = 0.015415, naive p = 0.863
    D against the *true* distribution       = 0.020755, p = 0.531  (no parameters estimated: valid)
    Monte-Carlo calibration of the fitted case: D = 0.015415, p = 0.728
```

The first line is the trap. The KS null distribution is the distribution of
$D$ **when the parameters are known** — it assumes the CDF you compare against
was specified in advance. When the parameters are estimated from the same data,
the fitted distribution is pulled towards the data by construction, so $D$ is
systematically too small and the naive p-value is systematically too large.
Here 0.863 against a properly calibrated 0.728: not catastrophic, but wrong,
and it is the *optimistic* direction.

Two valid routes:

- **Compare against a distribution whose parameters are known.** The second
  line does this, and needs no calibration.
- **Calibrate by simulation.** Draw many samples of the same size from the
  fitted distribution, refit each one, compute $D$, and see where the observed
  $D$ falls in that distribution. The demo implements this in about ten lines
  (`ks_calibrated`) and obtains 0.728.

SciPy offers `stats.goodness_of_fit`, which does the same Monte-Carlo
calibration internally; its interface and reliability vary between versions, so
check the returned statistic against your own simulation before relying on it.

### 2.4 What the test is for

The demo closes §2 by fitting the same machinery to data that are not
Gutenberg–Richter at all — a Weibull sample with a similar mean:

```
    n = 1500, mean magnitude 2.3668 (a GR sample would have 2.4343)
    D = 0.113479, calibrated p = 0.0005
    fitted b = 1.1840
```

A **plausible-looking b-value of 1.184 with a tiny calibrated p-value.** A
fitted parameter is not evidence that the model is right. The b-value answers
"if this is exponential, what is the slope?"; the goodness-of-fit test answers
"is it exponential?". They are different questions, and a paper that reports
only the first has answered only the first.

## 3. Correlation, sample size and p-values

The same distinction — parameter against evidence — appears in every
correlation. The demo draws one bivariate normal sample with true
$\rho = 0.35$ and reports the statistics computed on its first $n$ pairs:

```
          n         r   p (Pearson)   p (Spearman)          95% CI for rho
         10    0.7929     6.216e-03      3.815e-03        [+0.326, +0.949]
         30    0.5779     8.239e-04      7.796e-03        [+0.275, +0.777]
        100    0.4929     1.895e-07      1.605e-05        [+0.328, +0.628]
       1000    0.3805     8.298e-36      1.302e-32        [+0.326, +0.432]
      20000    0.3525     0.000e+00      0.000e+00        [+0.340, +0.365]
```

The point estimate moves with $n$ — 0.79 at ten pairs, 0.35 by twenty thousand
— because ten pairs is not many. The **p-value** moves by hundreds of orders of
magnitude on the same data, from $6.2\times10^{-3}$ to below the resolution of
double precision. And the **confidence interval** narrows from
$[+0.326, +0.949]$ to $[+0.340, +0.365]$ — it narrows as $n^{-1/2}$, and it
stays meaningful at every $n$.

> **A p-value answers "could this have arisen by chance?", not "is this
> important?"** With enough data every non-zero correlation is significant, and
> a p-value reported without an effect size and an interval is not a result.

The Pearson confidence interval is computed on the Fisher $z$ transform;
`stats.pearsonr(...).confidence_interval()` returns it, and SciPy warns that it
assumes approximate bivariate normality, which is why the Spearman p-value is
worth reporting alongside.

### 3.1 Small-sample regression: t, not z

A 25-sample synthetic regression of $\log_{10}k$ on porosity:

```
    slope = 11.0264 +/- 0.9019 (log10 mD per unit porosity)
    intercept = -2.8149, r^2 = 0.8666, p = 1.521e-11
    t(0.975, 23) = 2.0687 against the normal quantile 1.9600
    95% interval from t: [9.1607, 12.8921]   width 3.7313
    95% interval from z: [9.2587, 12.7941]   width 3.5353
    The z-interval is 5.25% too narrow and
    its actual coverage is 93.78%, not 95%.
```

Using 1.96 where $t(0.975, 23) = 2.0687$ is required makes the interval 5.25%
too narrow, and its true coverage is 93.78% rather than the 95% claimed. For a
25-sample measurement that is the difference between the claim and the data,
and it is the reason every regression routine that returns a standard error
expects you to multiply by a $t$ quantile with the right degrees of freedom.

## 4. A distribution fit that should be rejected

Permeability spans orders of magnitude and is conventionally treated as
lognormal. The demo draws 400 values from a lognormal (so the answer is known)
and fits both a normal and a lognormal:

```
  400 SYNTHETIC permeabilities, log10(k) drawn from a normal with
  mu = -1.0 and sigma = 1.2, so k is lognormal by construction.
  Range 3.524e-05 to 92.6 mD.
    sample mean 1.783, median 0.08821, skewness 8.9341

    model                               KS D     naive p    log-likelihood
    normal(mu, sigma), fitted        0.40656   2.903e-60           -1375.7
    lognormal(s, 0, scale), fitted     0.02651   9.341e-01              41.1
```

The normal fit is rejected at any reasonable level ($D = 0.41$,
$p = 2.9\times10^{-60}$); the lognormal fit is not ($p = 0.93$); and the
log-likelihood difference is 1417. Both models were fitted by the same routine
by maximum likelihood. **The model, not the optimiser, decided the answer.**
Here the naive KS p-values are defensible because they are interpreted
comparatively — the same caveat as §2.3 applies to the quoted numbers.

The section's real content is the last three lines:

```
    mean k   = 1.783 mD   (what a normal-model summary reports)
    median k = 0.08821 mD   (the population value is 10^mu = 0.1)
    geometric mean = 0.07779 mD, the sample estimate of that median
    the arithmetic mean is 20.2 times the median, and the gap grows
```

A lognormal variable's arithmetic mean is $\exp(\mu + \sigma^2/2)$: it is a
statement about the tail, not about a typical value, and it grows without
bound as $\sigma$ grows. Any statement of the form "the average permeability
is 1.8 mD" is dominated by the largest few samples. Two consequences that
matter in practice:

- **Report the geometric mean (or the median) when the variable is
  lognormal.** The arithmetic mean is not a typical value.
- **A linear average of a lognormal quantity is a different physical
  quantity.** Effective permeability in layered media, for example, averages
  arithmetically across layers and harmonically along them — the arithmetic
  mean overestimates flow across the layering and the harmonic mean
  underestimates it along the layering, and both are statements about the
  distribution's tails.

## Worked code

The two workhorse patterns, complete:

```python
import math
import numpy as np
from scipy import special, stats

# --- 1. a diffusion solution that stays accurate at depth
def T_step(z, t, kappa, dT):
    u = z / (2.0 * np.sqrt(kappa * t))
    if u < 26.0:
        return dT * special.erfc(u)
    # large argument: erfcx is finite, exp(-u^2) is not
    return dT * math.exp(-u * u) * special.erfcx(u)

print(T_step(1000.0, 1000.0 * 3.15576e7, 1.2e-6, 12.0))   # 0.0034 K

# --- 2. a b-value with an honest error bar and a calibrated test
def b_value(m, mc):
    beta = 1.0 / (m.mean() - mc)                 # Aki-Utsu MLE
    b = beta / math.log(10.0)
    return b, b / np.sqrt(m.size)

b, se = b_value(magnitudes, 2.0)
print("b = %.4f +/- %.4f" % (b, se))

d = stats.kstest(magnitudes - 2.0,
                 stats.expon(0.0, magnitudes.mean() - 2.0).cdf)
print("KS D = %.6f  (calibrate this by simulation, not with the naive p)"
      % d.statistic)

# --- 3. correlation with an interval rather than a verdict
res = stats.pearsonr(phi, logk)
lo, hi = res.confidence_interval(confidence_level=0.95)
print("r = %.3f  95%% CI [%.3f, %.3f]  n = %d"
      % (res.statistic, lo, hi, phi.size))
```

The three habits: **branch on the argument range** for special functions,
**quote an error bar** for an estimated parameter, and **quote an interval**
rather than a p-value for an effect.

## Physical interpretation

Equation (1) is the entire physics of borehole palaeoclimatology: a surface
temperature history is recovered by inverting a temperature log for the
$\Delta T(t)$ that best explains it, and the forward model is exactly this
error function. Equation (2) gives the corresponding heat-flow perturbation,
and its $t^{-1/2}$ decay is the reason a palaeoclimate correction to a heat-flow
measurement is large for recent perturbations and negligible for old ones.

The Gutenberg–Richter relation is the single most-used empirical law in
earthquake statistics, and $b \approx 1$ is so robust that its *variations*
are the signal: a region with $b \approx 0.7$ is usually interpreted as
indicating high differential stress, and one with $b \gtrsim 1.3$ as
indicating a swarm-like, fluid-driven process. Since the variations of interest
are of order 10–20%, **a 13% estimator bias (as measured in §2.2) is of the
same size as the effect being studied.** This is where the lesson stops being
about SciPy and starts being about which published maps are comparable.

The lognormal permeability result is the quantitative version of a statement
every reservoir geologist knows by experience: a few high-permeability streaks
carry the flow, and the arithmetic mean is a poor description of the rock. The
skewness of 8.93 measured in §4 is the number behind that intuition.

## Assumptions and limits

- **`erfc`'s accuracy is not uniform in its argument.** Underflow and
  cancellation are silent; check the argument range, not the result. (§1.1)
- **The asymptotic form $e^{-x^2}/(x\sqrt\pi)$ has a quantified relative
  error** — 7.4 parts in $10^4$ at $x = 26$ — and that error is a
  *relative* error on a number that may itself be $10^{-296}$. Multiplying an
  accurate `erfcx` by an underflowed $e^{-x^2}$ gives zero; the logarithm of
  the solution is the quantity to work with.
- **The Aki–Utsu estimator assumes $m_c$ is exact and the sample is
  complete above it.** A catalogue with a magnitude-dependent detection
  probability (which is the normal case at the low end) violates both, and the
  estimated $b$ inherits a bias that no error bar from equation (4) includes.
- **`SE(b) = b/\sqrt n` is the asymptotic standard error**; it assumes
  independent events. Aftershocks are not independent, and treating them as
  such understates the error by the clustering factor.
- **The KS test assumes a continuous distribution and a fully specified null.**
  Magnitudes are rounded to 0.1, which technically breaks continuity; with
  n = 1500 and this D, the effect is far below the calibration noise, but it is
  not zero.
- **Pearson's confidence interval assumes bivariate normality**, and its
  breakdown with heavy tails or outliers is the reason to report Spearman as
  well.
- **A p-value is not a posterior probability.** "$p = 0.0005$ that these data
  are exponential" is a statement about a test statistic, not about the
  hypothesis.

## Python demonstration

[`code/special_stats_demo.py`](./code/special_stats_demo.py) prints all the
tables above. Experiments worth running:

- Evaluate `erfc` at $x = 27$ through all three routes and watch two of them
  give zero. Then compute $\ln(\mathrm{erfc}(x))$ from `erfcx` — the identity
  $\ln\mathrm{erfc}(x) = \ln\mathrm{erfcx}(x) - x^2$ holds to full precision
  and is the form to use in a fit.
- Raise the completeness threshold in §2 from 2.0 to 3.0 and re-run. With
  fewer events the standard error grows, and the least-squares bias grows as
  well, because the cumulative curve spans fewer decades.
- Change the synthetic $b$ to 1.5 and re-run. Both estimators move, and the
  *ratio* of their biases stays near 1.13: the bias is a property of the
  cumulative least-squares method, not of the particular sample.
- Replace the Weibull in §2.4 with a **truncated** GR sample (draw GR
  magnitudes but discard everything below $m_c + 0.3$) and re-run. The fitted
  b-value is then badly biased even though the underlying law is correct: the
  estimator assumes completeness at $m_c$.
- In §4, change `sigma` from 1.2 to 0.5 and re-run. The arithmetic mean moves
  closer to the median and the log-likelihood gap narrows, but the normal fit
  is still rejected.

## Common mistakes

- **Writing `1 - erf(x)` for a large argument.** It returns exactly zero from
  $x = 8$; that is not a small number, it is a lost one. (§1.1)
- **Using `erfc` where `erfcx` is needed**, and losing the answer to underflow
  between $x = 26$ and 30. (§1.1)
- **Fitting a b-value by cumulative least squares and quoting its standard
  error.** Both the estimate and the error are wrong (§2.2), by 13% and by a
  factor of seven respectively.
- **Quoting the naive KS p-value after estimating parameters from the same
  data.** It is optimistic; calibrate by simulation. (§2.3)
- **Reporting a fitted parameter as evidence for a model.** The Weibull of
  §2.4 gives $b = 1.184$ with a calibrated p of 0.0005.
- **Reading a p-value as an effect size.** §3 is one sample at five sample
  sizes with p-values spanning 300 orders of magnitude.
- **Using the normal quantile 1.96 for a small-sample regression.** It costs
  5.25% of the interval width and 1.2% of the coverage. (§3.1)
- **Reporting an arithmetic mean for a lognormal variable.** It is 20 times
  the median in §4 and grows with $\sigma$.
- **Treating `stats.expon.fit`'s output as an estimate of $b$ directly.** It
  returns the scale $1/\beta$; the conversion $b = 1/(\text{scale}\ln 10)$ is
  where a factor-of-$\ln 10$ error creeps in.

## Real-world applications

- **Borehole palaeoclimatology and heat-flow correction.** Equation (1) is the
  forward model, and its large-argument accuracy is what limits how far back a
  temperature log can be inverted.
- **Earthquake statistics and seismic hazard.** b-values, magnitude–frequency
  relations, completeness estimation and their (frequent) estimator biases.
- **Aftershock forecasting.** Omori decay and Reasenberg–Jones aftershock
  probabilities are fits with small-sample intervals, where §3.1 decides
  whether the quoted width is honest.
- **Rock physics and reservoir characterisation.** Lognormal permeability and
  the distinction between a mean and a typical value; the same argument applies
  to porosity–permeability transforms and to saturation functions.
- **Geochemical and isotopic data.** Trace-element concentrations are
  lognormal for the same multiplicative-process reason and are tested and
  summarised the same way.
- **Instrument calibration and detection limits.** The error-function family
  is the basis of probit analysis, which is how a detection limit or a
  magnitude of completeness is estimated from a detection–amplitude curve.

## Further reading

- **Abramowitz, M., & Stegun, I. A. *Handbook of Mathematical Functions*
  (National Bureau of Standards, 1964).** The reference tables and asymptotic
  expansions for the error-function family, including the one used in §1.1.
  Level: reference.
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P.
  *Numerical Recipes* (3rd ed., Cambridge University Press, 2007).** §6.2 on
  the incomplete gamma and error functions, with the numerical warnings that
  §1.1 measures. Level: intermediate to advanced.
- **Aki, K. "Maximum likelihood estimate of b in the formula log N = a - bM and
  its confidence limits," *Bulletin of the Earthquake Research Institute*,
  1965.** The original derivation of the estimator in equation (4). Level:
  advanced; the closed form is reproduced in every later reference.
- **Gubbins, D. *Time Series Analysis and Inverse Theory for Geophysicists*
  (Cambridge University Press, 2004).** Statistics for geophysical data
  including magnitude distributions and regression with honest intervals.
  Level: graduate.
- **Utsu, T. "Representation and analysis of the earthquake size
  distribution," in *International Handbook of Earthquake and Engineering
  Seismology*, 2002.** The completeness problem and the estimators that
  handle it. Level: graduate.
- **Bevington, P. R., & Robinson, D. K. *Data Reduction and Error Analysis for
  the Physical Sciences* (3rd ed., McGraw-Hill, 2003).** What a p-value, an
  interval and an error bar each mean, at the level needed to avoid every
  mistake in the list above. Level: intermediate.
- **The SciPy project's documentation at [scipy.org](https://scipy.org)** —
  the `scipy.special` and `scipy.stats` references, including the notes on
  which routines are accurate over which range.

> Note on citations: bibliographic details are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text;
> confirm editions and availability through your library before citing them
> yourself.

## Related lessons

- [01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — where `special` and `stats` sit in the map.
- [03 scipy.optimize](./03-optimize.md) — the fitting machinery, and the
  covariance matrix whose interpretation §3.1 qualifies for small samples.
- [05 scipy.signal](./05-signal.md) — spectral estimation, which is a
  statistical estimate of a spectrum with the same bias-variance structure.
- [01-13-07 Confidence Intervals](../../01-mathematics/13-probability-and-statistics-foundations/07-confidence-intervals.md)
  — the interval that survives a change in $n$.
- [01-13-06 Estimation Theory](../../01-mathematics/13-probability-and-statistics-foundations/06-estimation-theory.md)
  — maximum likelihood, and why the Aki–Utsu estimator is the closed-form
  optimum.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
  — the physics of equation (1).
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) —
  where the fitting and testing of this lesson become inference about the
  Earth.
- [06-seismology](../../06-seismology/README.md) — the catalogues the
  statistics of §2 are computed from.

Exercises:
[`exercises/08-special-stats-exercises.md`](./exercises/08-special-stats-exercises.md)
and
[`exercises/08-special-stats-solutions.md`](./exercises/08-special-stats-solutions.md).

## Self-assessment checklist

- [ ] I can state the identity linking `erfc`, `ndtr` and the normal CDF.
      (§1.1)
- [ ] I can say where $1 - \mathrm{erf}(x)$ returns exactly zero. (§1.1)
- [ ] I can say where `erfc` underflows, and what to use instead. (§1.1)
- [ ] I can quote the relative error of the asymptotic `erfc` at a stated
      argument. (§1.1)
- [ ] I can compute a b-value by maximum likelihood and give its standard
      error. (§2.1)
- [ ] I can state the measured bias of cumulative least squares on 1500
      events. (§2.2)
- [ ] I can explain why a naive KS p-value is invalid after fitting. (§2.3)
- [ ] I can calibrate a goodness-of-fit p-value by simulation. (§2.3)
- [ ] I can give an example of a plausible fitted parameter from a wrong
      model. (§2.4)
- [ ] I can explain what p-values do and do not say as $n$ grows. (§3)
- [ ] I can quote a regression interval using $t$ rather than $z$. (§3.1)
- [ ] I can state why an arithmetic mean is the wrong summary of a lognormal
      variable, with the measured factor. (§4)
