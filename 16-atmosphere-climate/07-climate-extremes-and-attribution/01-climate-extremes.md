---
id: 16-07-01
title: "Extreme Events: Statistics and Physical Drivers"
level: doctoral
prereqs: ["16-04-04", "21-01-01", "21-01-07"]
tags: [atmosphere, climate, extremes, extreme-value-theory, return-level, clausius-clapeyron]
---

# Extreme Events: Statistics and Physical Drivers

> **All models and data in this module are SYNTHETIC.** The rainfall series,
> return levels and trends below are drawn from chosen distributions in the
> demonstration `code/climate_extremes_demo.py`. No real station, reanalysis,
> catalogue or published return level is used, and no published number is
> quoted as a measurement.

An extreme is not a big ordinary event. It is a **question asked of a
distribution's tail** — "how often is this exceeded?" — and the answer depends
on three things that are usually quoted as one: the *definition* of the event,
the *statistical model* fitted to it, and the *physical driver* that moves the
distribution. This lesson separates those three. The statistics half derives the
extreme-value laws and shows, with measured numbers, how much the answer moves
when only the method changes. The physics half derives what warming does to the
moisture supply and states precisely how far that takes us.

Two honest difficulties run through the lesson. First, a return level is an
extrapolation: a "100-year" value is estimated from records that are typically
shorter than 100 years, so its uncertainty is not a footnote but often most of
the answer. Second, a non-stationary world makes the classical return period an
ambiguous quantity; the same word can mean the level for next year, for the
record mean, or for a fixed reference climate, and those differ.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Fisher–Tippett–Gnedenko limit distributions from the block-maxima
   construction, and **state** the domain-of-attraction condition that selects
   between them.
2. **Translate** between the GEV and peak-over-threshold representations, and
   **derive** the parameter correspondence between the two.
3. **Estimate** return levels and their uncertainty, and **quantify** how the
   choice of method, threshold and record length change the reported number.
4. **Diagnose** non-stationarity in a block-maxima series, fit a non-stationary
   location parameter, and **state** which question a stationary fit answers and
   which it does not.
5. **Derive** the Clausius–Clapeyron scaling of saturation vapour pressure from
   the constants, and **distinguish** that thermodynamic scaling from an observed
   trend in extremes.
6. **Decompose** an extreme event into thermodynamic and dynamical contributions,
   and **state** the counterfactual that each attribution statement requires.
7. **Report** a return level with its definition, method, threshold, sample length
   and interval, and **label** each input as measured, modelled or chosen.

## Prerequisites

- [16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](../04-climate-system-and-feedbacks/04-natural-variability.md) —
  why a single event is not evidence about a distribution.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md) —
  the summaries an extreme-value fit replaces.
- [21-01-07 Extreme Value Theory for Geohazards](../../21-statistics-bayesian-ml/01-statistics-in-practice/07-extreme-value-theory.md) —
  the general theory this lesson specialises to climate.

## 1. What an "extreme" is, and why the definition comes first

Every extreme-value statement is *conditional on an event definition*. A
description of the event fixes four things before any statistics begin:

- the **variable** (daily maximum temperature, 3-day rainfall, peak wind);
- the **location** (a point, an area average, a river catchment);
- the **threshold or block** that turns a time series into "extremes";
- the **duration** (a single day, or a spell).

Change any of them and the distribution changes. Two analysts can use the same
data, disagree by a factor of two on the once-in-50-year rainfall, and both be
right, because they answered different questions. The discipline this lesson
imposes is: **state the event definition before stating a number.**

For a univariate series $X_1, X_2, \dots$ there are two standard ways to extract
extremes:

- **Block maxima.** Divide time into blocks (typically years) and keep the
  maximum $M_n = \max(X_1,\dots,X_n)$ of each block, where $n$ is the number of
  observations per block.
- **Peaks over threshold (POT).** Choose a high threshold $u$ and keep the
  exceedances $X - u$ for every $X > u$.

Each route has its own limit law, derived next.

## 2. The block-maxima limit law: Fisher–Tippett–Gnedenko

Suppose there exist sequences $a_n>0$ and $b_n$ such that the normalised block
maximum converges in distribution,

$$\Pr\!\left(\frac{M_n - b_n}{a_n} \le z\right) \xrightarrow[n\to\infty]{} H(z),$$

with $H$ non-degenerate. The **Fisher–Tippett–Gnedenko theorem** states that
$H$ must be one of three types — Gumbel, Fréchet or Weibull — and that all three
are special cases of the single **generalised extreme value (GEV)** distribution

$$H(z) = \exp\!\left\{-\left[1 + \xi\,\frac{z-\mu}{\sigma}\right]^{-1/\xi}\right\},
\qquad 1 + \xi\,\frac{z-\mu}{\sigma} > 0,$$

with location $\mu$, scale $\sigma>0$ and shape $\xi$. The case $\xi = 0$ is
Gumbel (light upper tail, exponential-like), $\xi>0$ is Fréchet (heavy,
power-law tail, unbounded), and $\xi<0$ is Weibull (bounded above). The shape
$\xi$ is selected by the **tail of the underlying distribution**, not by the
data length: if the parent decays like $x^{-\alpha}$ then $\xi = 1/\alpha$.

The shape is the whole difficulty. A negative $\xi$ says the variable has a hard
ceiling; a positive $\xi$ says it does not; and the return level at long periods
is extremely sensitive to which it is. That sensitivity is measurable, and
Section 5 measures it.

## 3. Return levels and return periods

The **return level** $z_T$ associated with return period $T$ (in blocks, usually
years) solves $H(z_T) = 1 - 1/T$:

$$\boxed{\;z_T = \mu + \frac{\sigma}{\xi}\left[\left(-\ln\left(1-\frac{1}{T}\right)\right)^{-\xi} - 1\right].}$$

For $\xi \to 0$ the limit is $z_T = \mu - \sigma \ln(-\ln(1-1/T))$. The
interpretation is exact and often misstated: $z_T$ is the level exceeded by the
block maximum **in any given block** with probability $1/T$. It is *not* the
level that is exceeded once every $T$ years — exceedances may cluster — and it
is not a promise about the next $T$ years.

## 4. The peak-over-threshold limit law and the parameter link

For a threshold $u$ high in the tail, the conditional excess
$X-u \mid X>u$ converges to the **generalised Pareto distribution (GPD)**

$$\Pr(X - u \le y \mid X > u) = 1 - \left(1 + \xi\,\frac{y}{\tilde\sigma}\right)^{-1/\xi},
\qquad y > 0,$$

with the **same shape** $\xi$ as the GEV but a threshold-dependent scale
$\tilde\sigma = \sigma + \xi(u-\mu)$. Writing $\lambda$ for the mean number of
exceedances per block, the equivalent return level is

$$z_T = u + \frac{\tilde\sigma}{\xi}\left[\left(\lambda T\right)^{\xi} - 1\right].$$

The identity of the shapes is what makes the two routes comparable, and it is
why the shape can be estimated from the *largest few values per block* instead
of only the single annual maximum — a gain in effective sample size. The price
is the threshold choice, which Section 6 measures.

## 5. Worked example — one process, three method choices

The demonstration generates a synthetic daily rainfall series from a GEV with
shape $c = 0.10$, location $35.0\ \mathrm{mm\,day^{-1}}$ and scale
$9.6\ \mathrm{mm\,day^{-1}}$, blocks it into $300$ years of $365$ days, and
computes the process's own 100-year daily level. The numbers below are the
demonstration's output, printed with units; they are **SYNTHETIC**.

*The truth.* The population 100-year daily level — the daily value whose annual
exceedance probability is $1/100$ — is

$$z_{100}^{\text{pop}} = 213.34\ \mathrm{mm\,day^{-1}}.$$

The $300$ sample annual maxima range from $82.9$ to
$285.7\ \mathrm{mm\,day^{-1}}$, so no year in the record actually reaches the
100-year level, yet the level is well defined.

*Block-maxima fit.* The maximum-likelihood GEV fit recovers
$\hat\xi = +0.111$ against the daily truth $0.10$ (the block maximum of a daily
GEV is not exactly GEV, so agreement is expected to be approximate), with
$\hat\mu = 111.67$ and $\hat\sigma = 17.51\ \mathrm{mm\,day^{-1}}$. The fitted
return levels are

| $T$ (yr) | $z_T$ (mm/day) |
|---|---|
| 2 | 118.22 |
| 10 | 156.42 |
| 50 | 197.11 |
| 100 | 216.67 |

The point estimate of the 100-year level, $216.67\ \mathrm{mm\,day^{-1}}$, is
$1.6\%$ above the population truth. A non-parametric bootstrap of $300$ resamples
gives a 95% interval $[193.6,\,244.1]\ \mathrm{mm\,day^{-1}}$, a width of
$50.5\ \mathrm{mm\,day^{-1}}$ — **23% of the estimate**. Reporting $217$ without
the interval would be reporting the least certain part of the calculation as if
it were the most certain.

*Method.* Three defensible sampling strategies applied to the same daily series
give:

| Strategy | $z_{100}$ (mm/day) | vs truth |
|---|---|---|
| Population truth | 213.34 | — |
| Block-maxima GEV (3 parameters) | 216.67 | $+1.6\%$ |
| Block-maxima Gumbel ($\xi = 0$ forced) | 197.17 | $-7.6\%$ |
| Peak-over-threshold GPD | 220.87 | $+3.5\%$ |

The spread across the three *methods* is $23.70\ \mathrm{mm\,day^{-1}}$, or
$11\%$ of the truth — comparable to the statistical uncertainty of a single fit.
Setting the shape to zero removes the tail's curvature and lowers the level; the
POT fit sees the largest values several times a year rather than once and returns
the heaviest answer. **The method is a modelling choice and belongs in the
report.**

## 6. Worked example — sample length and threshold

*Record length.* Repeating the whole estimation on 200 independent synthetic
records of length $n$ gives the distribution of the 100-year estimate:

| $n$ (yr) | median (mm/day) | 5th pct | 95th pct | interval width |
|---|---|---|---|---|
| 50 | 213.4 | 177.6 | 283.7 | 106.1 |
| 100 | 211.1 | 184.1 | 250.6 | 66.6 |
| 300 | 213.0 | 197.7 | 235.5 | 37.7 |
| 1000 | 214.0 | 203.6 | 223.2 | 19.7 |

The median is essentially unbiased, but the *width* of the 5–95% interval falls
from $106$ to $20\ \mathrm{mm\,day^{-1}}$ as the record lengthens. From 50 to
300 years the width drops by a factor $2.8$ against the $1/\sqrt{n}$ expectation
of $2.45$; from 300 to 1000 years by $1.91$ against $1.83$. So a 30-year
observational record cannot deliver a 100-year level to better than perhaps a
factor of two, and **the honest product is an interval, not a number.**

*Threshold.* Varying the POT threshold $u$ over the synthetic daily series gives:

| $u$ (mm/day) | exceedances/yr | GPD shape | GPD scale | $z_{100}$ (mm/day) |
|---|---|---|---|---|
| 77.29 | 9.13 | 0.118 | 13.59 | 219.72 |
| 80.33 | 7.30 | 0.117 | 13.99 | 219.42 |
| 84.40 | 5.48 | 0.115 | 14.53 | 218.85 |
| 90.21 | 3.65 | 0.091 | 15.86 | 214.22 |
| 101.61 | 1.83 | 0.116 | 16.27 | 217.97 |
| 118.47 | 0.73 | 0.135 | 16.91 | 216.69 |

Here the shape is stable and the level moves by only about
$5\ \mathrm{mm\,day^{-1}}$ across the range — good behaviour, because the parent
is genuinely GEV and the tail is well resolved. That is not guaranteed: for a
short record or a mixture of processes the threshold can move the answer more
than the whole statistical uncertainty, which is why the mean-residual-life and
parameter-stability plots are part of the method, not optional extras.

## 7. Non-stationarity: the return period of a moving target

Add a linear trend to the location, $\mu(t) = \mu_0 + \beta t$. The
demonstration uses $\beta = 0.20\ \mathrm{mm\,day^{-1}\,yr^{-1}}$ over $300$
years, so the true 100-year level itself moves:

| Reference climate | true $z_{100}$ (mm/day) |
|---|---|
| Start of record | 91.07 |
| Record midpoint | 120.97 |
| Present (end of record) | 150.87 |
| **Stationary fit to the whole record** | **241.56** |

The stationary fit returns $241.56\ \mathrm{mm\,day^{-1}}$ — $60.1\%$ above the
true present-day level and $165\%$ above the start-of-record level. It is
*greater* than any year's true value. The reason is visible in the fitted scale:
the stationary model reads the drift as extra variability and inflates
$\hat\sigma$ to $26.88\ \mathrm{mm\,day^{-1}}$ against a daily truth of
$9.60$. The trend and the variability are not separable in a stationary model,
so the single number answers no year's question.

A non-stationary fit that allows the location to drift recovers
$\hat\beta = +0.186\ \mathrm{mm\,day^{-1}\,yr^{-1}}$ against the true $0.200$ —
the trend is estimable and is the signal, not a nuisance parameter to average
away. Once a trend is admitted, "the 100-year event" is ambiguous. The honest
phrasing names the reference climate: *"the level with a $1/100$ annual
exceedance probability in the climate of year $t$"*.

## 8. The physical driver: Clausius–Clapeyron, from constants

Warm air holds more water. The saturation vapour pressure $e_s(T)$ obeys the
Clausius–Clapeyron relation

$$\frac{\mathrm{d}e_s}{e_s} = \frac{L_v}{R_v}\,\frac{\mathrm{d}T}{T^{2}},
\qquad\text{so}\qquad
\frac{e_s(T_2)}{e_s(T_1)} = \exp\!\left[\frac{L_v}{R_v}
\left(\frac{1}{T_1}-\frac{1}{T_2}\right)\right],$$

with the standard constants $L_v = 2.5\times10^{6}\ \mathrm{J\,kg^{-1}}$,
$R_v = 461.5\ \mathrm{J\,kg^{-1}\,K^{-1}}$ and a reference
$T_1 = 288.15\ \mathrm{K}$. The demonstration evaluates this exactly:

| $\Delta T$ (K) | $e_s(T_2)/e_s(T_1)$ | scaling (%/K) |
|---|---|---|
| 1.0 | 1.0672 | 6.72 |
| 2.0 | 1.1384 | 6.92 |
| 4.0 | 1.2936 | 7.34 |

At fixed relative humidity the moisture-holding capacity of the atmosphere rises
by about $7\%$ per kelvin, and the scaling itself is slightly temperature
dependent. **This is a thermodynamic statement about the moisture supply, not a
prediction about extremes.** Whether a rainfall extreme rises, and by how much,
depends additionally on the dynamics (where and how fast air converges), on the
duration of the event, and on whether the moisture is actually available — all
of which can damp or amplify the thermodynamic scaling. The correct use of the
$7\%$ figure is as a *reference scaling to compare against an observed trend*,
not as a prediction.

## 9. Assumptions and regime of validity

Every result above rests on assumptions that must be stated with it.

1. **Independent, identically distributed blocks.** The GEV limit is a statement
   about maxima of i.i.d. variables (or weakly dependent ones under mixing
   conditions). Serial correlation inside a block narrows the effective sample
   size; the fit does not know this, and the uncertainty is understated unless
   it is corrected (block bootstrap, or an effective-sample-size factor).
2. **The tail is in the domain of attraction, and the record is long enough for
   the limit to apply.** A 30-year annual-maximum series is used to estimate the
   edge of a distribution reached once in 100 years. The limit law is an
   asymptotic result invoked far from its asymptote.
3. **The GPD threshold is high enough** that the excess distribution has
   converged, and **low enough** that enough exceedances survive to estimate the
   shape. Both failure modes are visible in the threshold table.
4. **A single process dominates the tail.** A mixture (rain from two different
   synoptic regimes in one series) violates the single-distribution assumption;
   the fitted shape then has no physical meaning.
5. **Spatial dependence.** A regional return level is not the average of point
   return levels. Areal extremes raise the effective-sample-size problem, because
   the same storm produces dependent maxima at many sites.
6. **The Clausius–Clapeyron scaling assumes fixed relative humidity and constant
   $L_v$.** Both are approximations; the release of latent heat by condensation
   and changes in relative humidity modify the effective scaling.

## 10. What a defensible extreme-event statement looks like

Collecting the lesson, a statement that another analyst could reproduce names:

1. the **event definition** (variable, location, duration, threshold);
2. the **data** and its coverage;
3. the **statistical model** (GEV, Gumbel, GPD), the **threshold** if POT, and
   the **stationarity assumption**;
4. the **estimate with units** and an **uncertainty interval**;
5. the **reference climate** for a non-stationary series;
6. for any causal claim, the **counterfactual** — the world against which the
   event is compared (see [16-07-03 Event Attribution](03-event-attribution.md));
7. a **label** on each ingredient: *measured*, *modelled* or *chosen*.

## 11. Python demonstration

[`code/climate_extremes_demo.py`](code/climate_extremes_demo.py) performs the
whole calculation and prints labelled results with units. It:

1. builds a synthetic daily rainfall series and its annual maxima;
2. fits the GEV by maximum likelihood with a fast vectorised likelihood, and
   bootstraps the 100-year level;
3. measures the return-level distribution against record length;
4. compares block-maxima GEV, Gumbel and POT/GPD on the same process;
5. fits a stationary and a non-stationary model to a trending series;
6. sweeps the POT threshold and measures the drift in the estimate;
7. evaluates the Clausius–Clapeyron scaling from the physical constants.

Every number in this lesson is printed by that demonstration or is one of the
standard constants $L_v$, $R_v$ or $T_1$ named above.

## Mastery checkpoint

> A synthetic daily-rainfall series has a fitted block-maxima GEV with
> $\hat\xi = +0.111$, $\hat\mu = 111.67\ \mathrm{mm\,day^{-1}}$ and
> $\hat\sigma = 17.51\ \mathrm{mm\,day^{-1}}$.
>
> **(a)** Compute the 10-year and 100-year return levels by hand and compare with
> the demonstration's $156.42$ and $216.67\ \mathrm{mm\,day^{-1}}$.
> *(Hand values from the rounded parameters: $-\ln(0.9) = 0.105361$, so
> $z_{10} = 111.67 + 157.75\,(0.105361^{-0.111}-1) = 156.43$; and
> $-\ln(0.99) = 0.0100503$, so $z_{100} = 216.78$. The $0.01$ and
> $0.1\ \mathrm{mm\,day^{-1}}$ differences are rounding of the fitted
> parameters, not disagreement.)*
> **(b)** The bootstrap 95% interval for the 100-year level is
> $[193.6, 244.1]\ \mathrm{mm\,day^{-1}}$. State in one sentence why quoting
> `217 mm/day` alone is a misreport.
> **(c)** The same process fitted with the shape forced to zero gives
> $197.17\ \mathrm{mm\,day^{-1}}$. Explain the direction of the change from
> $\xi = 0.111$.
> **(d)** A stationary fit to a trending record returns a 100-year level
> *higher* than the true present-day level. Explain why, using the fitted scale.
> **(e)** State the counterfactual you would need before claiming that a
> particular observed extreme was made *more likely* by warming.

## Common pitfalls

1. **Reporting a return level without its event definition.** "The 100-year
   flood" is not a number; it is a number *given* a variable, a location and a
   duration.
2. **Treating the return level as a countdown.** $z_T$ has a $1/T$ chance of
   being exceeded *each* block, independently of how long it has been since the
   last one.
3. **Reporting a point estimate without the interval.** From a short record the
   interval is the answer; the point estimate is the least certain part of it.
4. **Choosing the shape by convenience.** Forcing $\xi=0$ (Gumbel) removes the
   curvature that controls the far tail, and lowered the level by $8\%$ here.
5. **Ignoring non-stationarity, or absorbing it into the scale.** A stationary
   fit to trending data inflates $\hat\sigma$ and returns a level that belongs to
   no year.
6. **Reading $7\%/\mathrm{K}$ as a rainfall prediction.** It is a moisture-supply
   scaling; dynamics and duration decide the actual response.
7. **Comparing point extremes and areal extremes.** They are different
   variables with different distributions.

## Related modules

- [16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](../04-climate-system-and-feedbacks/04-natural-variability.md) —
  the internal variability that sets the width of every interval here.
- [16-07-02 Detection and Attribution of Climate Change](02-detection-attribution.md) —
  whether a forced change is detectable above that variability.
- [16-07-03 Event Attribution Methodology and Its Limits](03-event-attribution.md) —
  the counterfactual reasoning that turns a return level into an attribution
  statement.
- [16-07-04 Impacts, Vulnerability and Risk Assessment](04-impacts-and-risk.md) —
  what the return level is used for, and how it becomes a risk.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md) —
  the same extreme-value and hazard logic applied to a different physical
  system; read it for the shared bookkeeping of return period and exceedance.
- [21-01-07 Extreme Value Theory for Geohazards](../../21-statistics-bayesian-ml/01-statistics-in-practice/07-extreme-value-theory.md) —
  the general theory behind Sections 2 and 4.

## Self-assessment checklist

- [ ] I can state the Fisher–Tippett–Gnedenko theorem and what the shape
      parameter selects.
- [ ] I can convert between GEV and POT parameters using
      $\tilde\sigma = \sigma + \xi(u-\mu)$.
- [ ] I can compute a return level from GEV parameters and state its units and
      its meaning.
- [ ] I can explain why a stationary fit to a trending series inflates the scale.
- [ ] I can derive the Clausius–Clapeyron scaling and state what it does *not*
      predict.
- [ ] I can name every ingredient a defensible extreme-event statement needs.
