---
id: 17-07-04
title: "Satellite Time Series and Trend Analysis"
level: doctoral
prereqs: ["17-07-01", "21-07-01", "20-08-01"]
tags: [remote-sensing, earth-observation, time-series, trend-analysis, aliasing, autocorrelation]
---

# Satellite Time Series and Trend Analysis

## Learning objectives

By the end of this lesson you will be able to:

1. **Model** a satellite index series as a linear trend plus seasonality plus
   noise, and **estimate** the trend by least squares with a stated design.
2. **Compute** the naive standard error of a trend and **state** the
   independence assumption it hides.
3. **Measure** the lag-1 autocorrelation of the residuals and **derive** an
   effective sample size and a corrected standard error from it.
4. **Explain** aliasing as a beat between the sampling interval and a periodic
   signal, and **demonstrate** that a spurious trend can appear when the
   sampling is too sparse or phase-biased.
5. **Distinguish** a break (a step change) from a trend, and **show** that a
   single-trend model absorbs a step as model error rather than noise.
6. **State** which of noise model, seasonal model and sampling design dominates
   the uncertainty in a given series.
7. **Report** a trend with its corrected interval and the sampling design that
   produced it.

## Prerequisites

- [17-07-01 Landsat, Sentinel and MODIS Data Products](01-landsat-sentinel.md)
  — the index values a trend is computed on.
- [21-07-01 ARIMA Models](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/01-arima-models.md)
  — the time-series toolkit this lesson applies.
- [20-08-01 Detrending and Seasonality](../../20-signal-processing/08-timeseries-analysis-geophysics/01-detrending-seasonality.md)
  — removing trend and season before analysis.

> All models and data in this module are **SYNTHETIC**. The series, its
> seasonality, noise, revisit interval and break below are chosen teaching
> values. No time series of any real sensor or site is used, and no number is a
> measurement of the Earth.

## 1. A series is a sampling, not a curve

A satellite does not return a curve; it returns samples at the times the
spacecraft happened to look, through whatever atmosphere happened to be there.
Everything we call a "trend" or a "seasonal cycle" is a *model fitted to those
samples*, and the fitted numbers depend on the model as much as on the Earth.
This lesson makes the dependence explicit three times: through autocorrelation
(which inflates apparent significance), through aliasing (which invents
periodicity and trend), and through breaks (which a smooth trend hides).

The single most common error in remote-sensing trend studies is to divide a
fitted slope by the standard error that assumes independent samples. Satellite
residuals are **not** independent: a wet year, a persistent atmospheric bias or
a slowly changing sensor geometry leaves a correlated residual, and correlation
reduces the *information* in the series even while the sample count is large.

## 2. Definitions and the model

Let the observed index at day $t$ be

$$
y(t) = \beta_0 + \beta_1\,\frac{t}{365.25}
+ A\sin\!\left(\frac{2\pi t}{365.25}\right)
+ B\cos\!\left(\frac{2\pi t}{365.25}\right) + \varepsilon(t),
$$

with $\varepsilon$ the residual. The trend is $\beta_1$ **per year**. Write the
model as $y = X\beta + \varepsilon$ with the design matrix

$$
X = \left[\;\mathbf{1},\; \frac{t}{365.25},\;
\sin\!\left(\frac{2\pi t}{365.25}\right),\;
\cos\!\left(\frac{2\pi t}{365.25}\right)\;\right],
$$

so that a single annual harmonic is absorbed by the $\sin/\cos$ pair. The least
squares estimate is $\hat\beta = (X^{\mathsf T}X)^{-1}X^{\mathsf T}y$, and under
**independent, homoscedastic** residuals

$$
\operatorname{Cov}(\hat\beta) = \sigma^{2}\,(X^{\mathsf T}X)^{-1},
\qquad
\hat\sigma^{2} = \frac{\lVert y - X\hat\beta\rVert^{2}}{n - p}.
$$

The square root of the $(2,2)$ entry of the covariance is the **naive standard
error** of the trend. Every term here is a choice: the degree of the trend, the
number of harmonics, and the independence assumption.

## 3. Worked example 1 — a trend with a naive error

The synthetic series of [`code/time_series_satellite_demo.py`](code/time_series_satellite_demo.py)
has a true trend of $\beta_1 = 0.0200$ per year, a seasonal amplitude of
$0.080$, and AR(1) noise with standard deviation $0.030$ and lag-1 correlation
$0.55$. It is sampled every $16$ days for five years: $115$ observations.

Fitting the design above gives

$$
\hat\beta_1 = 0.0184\ \text{per year}, \qquad
\hat\sigma = 0.0275, \qquad
\mathrm{SE}_{\text{naive}}(\hat\beta_1) = 0.0018\ \text{per year},
$$

and the naive $95\%$ interval is

$$
[\,0.0149,\; 0.0218\,]\ \text{per year}.
$$

The estimate is close to the truth and the true value lies inside the interval —
which is what we should expect *if* the interval is honest. Sections 4 shows it
is not.

## 4. Autocorrelation and the effective sample size

For residuals with lag-1 correlation $\rho$, the variance of the sample mean is
inflated by roughly $(1+\rho)/(1-\rho)$, so the **standard-error inflation
factor** is

$$
\gamma = \sqrt{\frac{1+\rho}{1-\rho}},
$$

and the **effective sample size** is

$$
n_{\text{eff}} = n\,\frac{1-\rho}{1+\rho}.
$$

The demonstration measures $\rho = 0.5159$ from the residuals. Then

$$
\gamma = \sqrt{\frac{1.5159}{0.4841}} = 1.769,
\qquad
n_{\text{eff}} = 115 \times \frac{0.4841}{1.5159} = 36.7.
$$

**One hundred and fifteen observations contain the information of about
thirty-seven independent ones.** The corrected standard error is
$0.0018 \times 1.769 = 0.0032$, and the corrected $95\%$ interval is

$$
[\,0.0122,\; 0.0245\,]\ \text{per year},
$$

almost twice as wide as the naive interval. The conclusion "the trend is
detected" survives here, because the true trend is large relative to the noise;
but a study with a smaller trend and the same autocorrelation could find a
"significant" trend that is not, purely by ignoring $\rho$.

### 4.1 Where the inflation factor comes from

For a stationary AR(1) residual with variance $\sigma^{2}$ and lag-1 correlation
$\rho$, the variance of the sample mean of $n$ observations is

$$
\operatorname{Var}(\bar{x}) = \frac{\sigma^{2}}{n}
\left[\,1 + 2\sum_{k=1}^{n-1}\left(1 - \frac{k}{n}\right)\rho^{k}\,\right]
\;\xrightarrow[\;n \to \infty\;]{}\;
\frac{\sigma^{2}}{n}\,\frac{1+\rho}{1-\rho}.
$$

The correction factor $(1+\rho)/(1-\rho)$ is the **variance inflation**, so its
square root $\gamma = \sqrt{(1+\rho)/(1-\rho)}$ is the standard-error inflation
used above. The derivation shows why the factor depends on $\rho$ and *not* on
$n$: adding observations helps only in proportion to the independent information
they carry. Defining $n_{\text{eff}} = n(1-\rho)/(1+\rho)$ is the convention that
reproduces this, since then
$\operatorname{Var}(\bar{x}) = \sigma^{2}/n_{\text{eff}}$. With the measured
$\rho = 0.5159$ the variance factor is

$$
\frac{1+\rho}{1-\rho} = \frac{1.5159}{0.4841} = 3.13,
$$

and $\gamma = \sqrt{3.13} = 1.769$, as used in §4.

### 4.2 Why the corrected interval is bigger, not just wider

Two different regressions with the same residuals have the same point estimate
but different stated precision. The point is not that one is "pessimistic"; the
point is that the naive interval is *wrong* — it describes the variability you
would see if the residuals were independent draws, and they are not. Reporting
the naive interval is not a conservative choice; it is a false statement about
precision.

## 5. Aliasing: sparse sampling invents a trend

Sampling can create signal that is not in the process. A purely periodic signal
of period $T$ is resolved only if the sampling interval $\Delta$ satisfies
$\Delta < T/2$. If $\Delta$ exceeds that, the true frequency folds onto a lower
one, leaving an **alias** at $|f - k f_s|$ for integer $k$.

The demonstration samples a pure annual sinusoid (amplitude $0.100$, **no
trend**) at day indices $0, 400, 800, 1200, 1600$ — an interval of $400$ days,
well beyond the $182.6$-day Nyquist limit for an annual cycle. Fitting a
straight line to those five samples returns a slope of

$$
+0.0162\ \text{per year}
$$

from a signal that has no trend at all. The samples beat against the cycle, and
the beat looks exactly like a trend. Two practical consequences: a **revisit
interval** is a design parameter that must be compared with the periods of
interest, and **phase-biased sampling** (always looking in the same season) can
remove the season from the data while importing its long-term changes into the
trend.

## 6. Breaks: what a smooth trend hides

A single trend assumes the process changed smoothly. When it *stepped*, a trend
absorbs the step as a systematic misfit and reports it as large residuals. The
demonstration adds a step of $+0.060$ at year $3.0$ to the series:

| Model | Residual sd | Step recovered |
|---|---|---|
| trend + seasonal (no step) | 0.0314 | — |
| trend + seasonal + step | 0.0276 | $+0.0593$, SE $0.0103$ |

The single-trend model's residual sd is $0.0314$ — *larger* than the true noise
because the step is folded into it; the step model recovers the step as
$+0.0593$, within one standard error of the true $0.060$. The honest workflow is
therefore: **fit the trend, inspect the residuals, and test a break** — because a
break that is reported as scatter will corrupt both the trend and its error bar.

## 7. Assumptions and regime of validity

1. **The trend is linear in time.** A trend that itself accelerates is fitted by
   a line with a plausible slope and a misleading significance; plot the
   residuals against time before believing the slope.
2. **One annual harmonic suffices.** Semi-annual and phenology-driven structure
   leaks into the trend if omitted; add harmonics and check that the slope
   stabilises.
3. **Residuals are stationary.** If the noise process changes (a sensor
   degradation, a reprocessing break), a single $\rho$ is insufficient and a
   state-space model is required.
4. **The AR(1) correction is adequate.** The factor $(1+\rho)/(1-\rho)$ is exact
   only for an AR(1) process; for longer memory, a Newey–West or block
   bootstrap estimate is safer.
5. **The index is comparable over time.** A change in the product version, the
   mask or the atmospheric model within the record creates a *spurious* step;
   this is the single largest contamination of real satellite trends.
6. **Sampling is not phase-biased.** Otherwise seasonality and trend are
   entangled in ways the model cannot separate.

## 8. Worked example 2 — is a trend detected?

Suppose a study reports $\hat\beta_1 = 0.0040$ per year with a naive standard
error of $0.0015$ and $\rho = 0.5$.

1. Inflation factor: $\gamma = \sqrt{1.5/0.5} = \sqrt{3} = 1.732$.
2. Corrected standard error: $0.0015 \times 1.732 = 0.0026$.
3. Naive $t$: $0.0040/0.0015 = 2.67$ — "significant" at $5\%$.
4. Corrected $t$: $0.0040/0.0026 = 1.54$ — not significant.

The same data support opposite headlines, and only the corrected number is
honest. If the study needs to defend "detected", it must shorten the revisit
interval, lengthen the record, or reduce the autocorrelation (for example by
compositing to a longer cadence that averages out short-lived atmosphere). The
design, not the arithmetic, is what buys significance.

## Mastery checkpoint

Complete this without notes.

> A five-year series has $200$ observations, an estimated trend of
> $+0.050$ per year, a naive standard error of $0.010$, and a residual lag-1
> autocorrelation of $\rho = 0.6$. **(a)** Compute the inflation factor and the
> corrected standard error. **(b)** Give the corrected $95\%$ interval and state
> whether the trend is detected. **(c)** State the sampling interval below which
> an annual cycle is resolved, and explain why a revisit near that limit is
> dangerous. **(d)** The residuals show a single large excursion; state the next
> model you would fit and why.

A worked version appears in the
[solutions](exercises/04-time-series-satellite-solutions.md).

## Common pitfalls

1. **Dividing by the naive standard error.** It assumes independence the data do
   not have.
2. **Reporting the number of observations as the information content.** Report
   $n_{\text{eff}}$.
3. **Ignoring the revisit interval.** It sets the Nyquist limit and the
   aliasing.
4. **Sampling always in one season.** It entangles seasonality with trend.
5. **Fitting a line through a step.** The step becomes inflated "noise".
6. **Letting a product-version change masquerade as a break.** Check the
   provenance timeline before interpreting a step.
7. **Trusting a significance test as a physical result.** Significance is a
   statement about the noise model, not about the Earth.

## Related modules

- [17-07-01 Landsat, Sentinel and MODIS Data Products](01-landsat-sentinel.md)
  — the index values and their calibration.
- [17-07-02 Cloud Platforms](02-cloud-platforms.md) — the reducer that produces
  the samples a trend consumes.
- [17-02-05 Change Detection and Time-Series Analysis](../02-optical-and-thermal-remote-sensing/05-change-detection.md)
  — the same series machinery applied to change.
- [21-07-01 ARIMA Models](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/01-arima-models.md)
  — the systematic treatment of correlated residuals.

## Materials

- Demonstration: [`code/time_series_satellite_demo.py`](code/time_series_satellite_demo.py)
  — trend fit, autocorrelation correction, aliasing and break detection.
- Exercises: [`exercises/04-time-series-satellite-exercises.md`](exercises/04-time-series-satellite-exercises.md)
  with [solutions](exercises/04-time-series-satellite-solutions.md).
