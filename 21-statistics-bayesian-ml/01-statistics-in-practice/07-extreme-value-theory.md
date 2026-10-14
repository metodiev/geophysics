---
id: 21-01-07
title: "Extreme Value Theory for Geohazards"
level: research
prereqs: ["01-13-04", "21-01-02"]
estimated_minutes: 70
tags: [statistics, extreme-values, gev, gpd, return-levels, hazard]
---

# Extreme Value Theory for Geohazards

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the Fisher-Tippett-Gnedenko theorem and **explain** why only one
   three-parameter family can describe block maxima.
2. **Interpret** the GEV shape parameter as a domain of attraction, and
   **classify** a tail as Gumbel, Fréchet or Weibull from a fitted $\hat\xi$.
3. **Compute** a return level and **state** precisely what a $T$-block return
   period does and does not mean.
4. **Fit** a generalised Pareto distribution to threshold exceedances and
   **choose** the threshold with the mean-excess and parameter-stability
   diagnostics.
5. **Quantify** the uncertainty of a return level and **explain** why it grows
   with the return period.
6. **Diagnose** the failures of extreme-value analysis: non-stationarity,
   dependence, and extrapolation from too few extremes.

All data in this lesson are **SYNTHETIC**: i.i.d. draws from a Fréchet law with a
stated tail index. No measured hazard value is used, and no number here is a
return level for any real place.

## Prerequisites

- [01-13-04 Common Distributions and Their Earth-Science Roles](../../01-mathematics/13-probability-and-statistics-foundations/04-distributions.md) —
  the heavy-tailed families whose extremes are studied here.
- [21-01-02 Choosing Probability Models for Earth Data](02-probability-models-earth.md) —
  how a body distribution is chosen and why its tail is extrapolation.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](03-resampling.md) —
  the bootstrap used for return-level intervals.

## 1. Intuition: the hazard lives in the extreme, not in the average

A design engineer does not care about the average flood, wind or ground motion.
They care about the largest value in the next $T$ years, and that value is
controlled by the **tail** of the distribution — the part of the sample with the
fewest observations. Extreme value theory exists to make that part quantitative,
and it does so with a remarkable result: however different the body
distributions of rainfall, river discharge, wind speed or significant wave height
may be, the distribution of their block maxima, once suitably normalised, can
only be one of three types. That universality is the theory's power and the
reason it is used far beyond its data.

It is also the theory's danger. The universality is asymptotic in the block
size, and a finite sample of extremes is exactly the situation in which the
asymptotics are least controlled. Everything in this lesson is therefore paired
with a diagnostic: the mean-excess plot, the parameter-stability plot, and the
bootstrap interval.

## 2. Block maxima and the generalised extreme value family

Let $X_1, X_2, \dots$ be i.i.d. with distribution $F$, and let
$M_n = \max(X_1,\dots,X_n)$. If there exist sequences $a_n > 0$ and $b_n$ such
that $(M_n - b_n)/a_n$ converges in distribution to a non-degenerate limit
$G$, then $G$ is the **generalised extreme value** distribution

$$G(z) = \exp\!\left\{-\Big[1 + \xi\,\frac{z - \mu}{\sigma}\Big]^{-1/\xi}\right\},
\qquad 1 + \xi\frac{z-\mu}{\sigma} > 0,$$

with location $\mu$, scale $\sigma > 0$ and shape $\xi$. The three cases are the
three domains of attraction:

- $\xi = 0$ (interpreted as the limit): **Gumbel**, an exponentially decaying
  tail. The Gaussian, exponential and gamma bodies belong here.
- $\xi > 0$: **Fréchet**, a power-law tail $1 - G(z) \sim z^{-1/\xi}$. Lognormal,
  Pareto and $t$ bodies belong here, and this is the case that matters for
  hazards.
- $\xi < 0$: **Weibull**, a bounded upper tail. A body with a hard maximum, such
  as a bounded physical quantity, belongs here.

The shape parameter is therefore not a nuisance: it is the statement about how
the tail decays, and every return level depends on it.

**A sign convention worth stating once.** `scipy.stats.genextreme` parameterises
the shape as $c = -\xi$; a fitted $c = -0.63$ means $\xi = +0.63$. Reading
`genextreme`'s output as $\xi$ directly inverts Fréchet and Weibull, and it is a
common and silent error.

## 3. Return levels

The $T$-block **return level** $z_T$ solves $G(z_T) = 1 - 1/T$:

$$z_T = \mu + \frac{\sigma}{\xi}\Big[\big(-\ln(1 - 1/T)\big)^{-\xi} - 1\Big]
\quad (\xi \neq 0), \qquad
z_T = \mu - \sigma\ln\!\big(-\ln(1 - 1/T)\big) \quad (\xi = 0).$$

The return period is a statement of **rate**, not of waiting: a $T$-block return
level is the value exceeded by one block maximum in every $T$ blocks on average.
It is not "the value that occurs once every $T$ blocks", and it is certainly not
a safe upper bound — in any $T$ consecutive blocks the probability that $z_T$ is
exceeded at least once is $1 - (1 - 1/T)^{T} \to 1 - e^{-1} = 0.632$, not zero.

## 4. Peaks over threshold and the generalised Pareto family

Blocking throws away all but one observation per block. The threshold approach
keeps every large value. For $X$ with distribution $F$ and a threshold $u$, the
**excess** $Y = X - u$ conditioned on $X > u$ has, as $u$ rises, a
**generalised Pareto** distribution

$$H(y) = 1 - \Big(1 + \xi\,\frac{y}{\beta}\Big)^{-1/\xi}, \qquad y > 0,
\qquad 1 + \xi y/\beta > 0,$$

with the **same shape** $\xi$ as the GEV of the block maxima and a
threshold-dependent scale $\beta(u) = \sigma + \xi(u - \mu)$.

**Choosing the threshold.** Two diagnostics are standard and both are visual in
practice. The **mean-excess function** is linear in $u$ for a GPD:

$$e(u) = \mathbb E[X - u \mid X > u] = \frac{\beta + \xi u}{1 - \xi},
\qquad \frac{\mathrm de}{\mathrm du} = \frac{\xi}{1 - \xi},$$

so a plot of mean excess against $u$ should be a straight line above the
threshold — a flat line means a light ($\xi \le 0$) tail. The **parameter
stability** plot refits the GPD over a range of thresholds and selects the lowest
$u$ above which $\hat\xi$ and the **modified scale** $\beta - \xi u$ are
approximately constant. Too low a threshold violates the asymptotics; too high a
threshold leaves too few exceedances.

**Return levels from a threshold model.** With $\lambda_u$ the mean number of
exceedances per block, the return level is

$$z_T = u + \frac{\beta}{\xi}\Big[(T\lambda_u)^{\xi} - 1\Big]
\quad (\xi \neq 0).$$

## 5. Estimation and uncertainty

Both families are fitted by maximum likelihood, which is consistent and
asymptotically normal but biased at small sample sizes; a common small-sample
correction shifts $\hat\xi$ by $O(1/n_{\text{exceed}})$. The uncertainty of a
return level is **not** read off a standard-error column: the level is a
nonlinear function of $(\mu, \sigma, \xi)$ and its distribution is markedly
asymmetric. The practical route is the **profile likelihood** or the
**bootstrap**, and the key fact is that the interval's width grows with the
return period because $z_T$ is increasingly a function of the least-certain
parameter, $\xi$.

## 6. Worked example

The demonstration draws $N = 20\,000$ i.i.d. Fréchet$(\alpha = 1.5)$ values, so
the true block-maxima shape is exactly $\xi = 1/\alpha = 0.6667$.

**Block maxima.** With $20$ values per block there are $1000$ maxima and the
sample maximum is $316.25$. The fitted GEV has $\hat\xi = +0.6297$ against the
true $0.6667$, location $\hat\mu = 7.6615$ and scale $\hat\sigma = 4.9415$. The
$0.037$ gap between $\hat\xi$ and the truth is the estimator's finite-sample bias
and spread at $1000$ blocks — visible, and of the size the theory predicts for
this count.

**Return levels.** With a $200$-replicate bootstrap:

| period | return level | 95 % interval |
|---|---|---|
| 10 blocks | 32.184 | [29.180, 35.127] |
| 50 blocks | 91.391 | [76.398, 109.148] |
| 100 blocks | 141.957 | [114.264, 175.512] |

The relative width of the interval grows from $18\ \%$ at $T = 10$ to $43\ \%$ at
$T = 100$ — a direct measurement of the statement that long-period levels are
model statements.

**Threshold fit.** The $95$th percentile is $u = 7.664$, leaving $1000$
exceedances. The fitted GPD has $\hat\xi = +0.5831$ and $\hat\beta = 5.1507$;
the GEV and GPD shape estimates agree to $0.0466$, as they should, since they
estimate the same tail index.

**Mean excess.** The threshold and mean-excess table is

| threshold | mean excess | slope | implied $\xi$ |
|---|---|---|---|
| 4.630 | 7.6961 | — | — |
| 6.000 | 9.3542 | +1.2099 | +0.5475 |
| 7.664 | 11.1478 | +1.0780 | +0.5188 |
| 10.651 | 14.7350 | +1.2010 | +0.5457 |
| 21.675 | 25.2752 | +0.9561 | +0.4888 |

The mean excess rises roughly linearly, as the GPD requires, with slopes around
$1.0$–$1.2$. Inverting $\xi = \text{slope}/(1 + \text{slope})$ gives $0.49$–$0.55$,
somewhat below the true $0.6667$ — a reminder that a mean-excess slope is a first
difference of two noisy heavy-tailed averages. The **flat alternative** is worth
contrasting: a Gumbel tail would give a zero slope, and the table is emphatically
not flat.

## Assumptions and regime of validity

1. **Asymptotic blocks.** The GEV is the limit for large blocks; with $20$ values
   per block it is an approximation whose error is comparable to $\hat\xi$'s own
   bias.
2. **i.i.d. observations.** Serial dependence reduces the effective block size
   and inflates the variance of $\hat\xi$; declustering is needed for storms and
   earthquake sequences.
3. **Stationarity.** A trend or regime shift changes $\theta$ through time;
   non-stationary extremes require covariates in the parameters.
4. **A threshold exists.** The GPD requires a $u$ above which the asymptotic
   regime holds; a smoothly varying body may have no such $u$.
5. **Fitted, not known, shape.** The return levels are functions of $\hat\xi$,
   the least-certain parameter; the bootstrap interval is part of the result.
6. **The model extrapolates.** A $100$-block return level from $1000$ blocks is
   an extrapolation whose credibility rests on the fitted family, not on the
   sample.

## The honest summary

Extreme value theory gives hazards the only distribution they can have in the
limit, and then asks you to trust an asymptotic limit that finite samples never
reach. In the demonstration the shape parameter is recovered to $0.04$ from
$1000$ blocks, the GEV and GPD estimates agree to $0.05$, and the return-level
interval widens from $18\ \%$ to $43\ \%$ over a tenfold increase in the return
period. Those numbers describe a *well-behaved synthetic case* — $20\,000$ i.i.d.
draws, no trend, no clustering, a known power-law tail. Real hazard records are
shorter, dependent and non-stationary, and every one of those properties moves
the answer. What the numbers here do **not** establish is any real return level:
that requires a data-specific study of the diagnostics, not a fitted shape
parameter alone.

## Python demonstration

[`code/extreme_value_demo.py`](./code/extreme_value_demo.py) prints every number
quoted above. It:

1. fits a GEV to block maxima and prints the shape against the truth;
2. bootstraps return levels for three periods;
3. fits a GPD above the $95$th percentile;
4. tabulates the mean-excess function and its slope.

```bash
cd 21-statistics-bayesian-ml/01-statistics-in-practice/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python extreme_value_demo.py
```

It runs in about four seconds and prints only text.

## Exercises

Graded problems are in
[`exercises/07-extreme-value-theory-exercises.md`](./exercises/07-extreme-value-theory-exercises.md)
with worked solutions in
[`exercises/07-extreme-value-theory-solutions.md`](./exercises/07-extreme-value-theory-solutions.md).
The ★★★ problems ask you to design threshold-selection and non-stationarity
studies.

## Mastery checkpoint

Without notes, a GEV fit to block maxima gives $\hat\mu = 7.66$,
$\hat\sigma = 4.94$ and $\hat\xi = +0.63$, and a $100$-block return level of
$141.96$ with interval $[114.26, 175.51]$.

1. Classify the tail and state the domain of attraction.
2. Compute the probability that the $100$-block return level is exceeded at least
   once in $100$ blocks, and state why it is not zero.
3. State in one sentence why the interval widens with the return period.
4. Your colleague reports the level as $141.96$ with no interval and no shape
   parameter. What is missing, and what would you ask for?

## Common pitfalls

1. **Reading `genextreme`'s $c$ as $\xi$.** The package uses $c = -\xi$; the sign
   error inverts Fréchet and Weibull.
2. **Quoting a return level without its interval.** The interval is the largest
   part of the answer at long periods.
3. **Blocking too small.** With small blocks the GEV limit is not reached and
   $\hat\xi$ is biased.
4. **Choosing the threshold by eye.** Use the mean-excess and stability plots and
   report the threshold.
5. **Treating a return period as a warranty.** The exceedance probability over
   $T$ blocks is $63\ \%$, not zero.
6. **Fitting a stationary GEV to a trending series.** Climate and land-use change
   put a trend in the parameters, and ignoring it biases every level.

## Where this is used

- **Flood and rainfall frequency**: the standard application, with national
  guidelines built on GEV and GPD fits.
- **Seismic hazard**: ground-motion and recurrence extremes, with the
  non-stationarity of aftershock sequences as a central difficulty.
- **Coastal engineering**: significant wave height and storm surge return levels.
- **Geohazards**: landslide, rockfall and debris-flow magnitude-frequency
  relations.
- **Climate attribution**: changes in return periods as a function of a forcing
  covariate.

## Related lessons

- [21-01-02 Choosing Probability Models for Earth Data](02-probability-models-earth.md) —
  the body distributions whose extremes these families describe.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](03-resampling.md) —
  the bootstrap behind the return-level intervals.
- [21-07-05 Point Processes and Seismicity Rate Models](../07-time-series-and-forecasting/05-point-processes.md) —
  the rate side of hazard, beyond the magnitude side here.
- [21-08-03 Attribution in Climate and Hazard Science](../08-causal-inference-and-design/03-attribution-methods.md) —
  how non-stationary extremes enter attribution.
- [01-13-04 Common Distributions and Their Earth-Science Roles](../../01-mathematics/13-probability-and-statistics-foundations/04-distributions.md) —
  the heavy-tailed bodies in the Fréchet domain.

## Self-assessment checklist

- [ ] I can state the Fisher-Tippett-Gnedenko theorem and the three domains.
- [ ] I can read a GEV shape parameter as a tail classification.
- [ ] I can compute a return level and state what a return period means.
- [ ] I can fit a GPD and choose a threshold with the mean-excess plot.
- [ ] I can obtain and interpret a return-level interval.
- [ ] I can name the assumptions that no asymptotic result removes.
