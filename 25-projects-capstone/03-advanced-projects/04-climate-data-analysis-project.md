---
id: 25-03-04
title: "Project: Climate Data Analysis and Trend Attribution"
level: advanced
prereqs: ["25-02-03", "20-05-01", "20-08-01", "21-01-04"]
estimated_minutes: 180
tags: [projects, climate, time-series, trend, autocorrelation, detection, teaching]
---

# Project: Climate Data Analysis and Trend Attribution

## Learning objectives

By the end of this project you will be able to:

1. **Fit** a linear trend and a seasonal cycle simultaneously by least squares and
   **report** the trend with its unit and period.
2. **Measure** the residual lag-1 autocorrelation and **convert** it into an
   integrated time and an inflation factor for the trend's standard error.
3. **Compute** the naive and the autocorrelation-corrected error bars and **state**
   the ratio between them.
4. **Measure** the false-positive rate of both tests on a red-noise surrogate
   ensemble, and **compare** each with the nominal 5%.
5. **Show** what annual averaging does to the autocorrelation and to the error bar,
   and **state** what it does not remove.
6. **Distinguish** a detected trend from an attributed cause, and **state** the
   three further conditions an attribution requires.
7. **Report** a trend as an estimate with a noise model, an error bar that
   reflects that model, and an explicit statement of what the number does not
   establish.

All data in this project are **SYNTHETIC**: a 50-year monthly series generated
from a chosen trend, a chosen seasonal cycle and a chosen AR(1) process by
[`code/climate_trend_demo.py`](./code/climate_trend_demo.py). A real station
record for the project itself is available from the NOAA land-based station
archive at <https://www.ncei.noaa.gov/products/land-based-station>; no number
below comes from it.

## Prerequisites

- [25-02-03 Project: Fourier Analysis of a Geophysical Signal](../02-intermediate-projects/03-fourier-analysis-signals.md) —
  the spectra and windows that a climate series also needs.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md) —
  the integrated time $\tau_\text{int}$ used here as an inflation factor.
- [20-08-01 Detrending, Deseasonalising and Anomalies](../../20-signal-processing/08-timeseries-analysis-geophysics/01-detrending-seasonality.md) —
  the preprocessing this project formalises as a joint fit.
- [21-01-04 Linear, Multiple and Robust Regression](../../21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md) —
  least squares, the design matrix and the residual degrees of freedom.

## 1. The question

*Is there a trend in this record, and how much of the answer is the trend and how
much is the noise model?*

The second clause is the project, because in a climate-style series the noise is
red and the error bar on a trend depends almost entirely on how red it is. The
demonstration makes the point in one number: the naive standard error on the trend
is $0.001936\ \mathrm{^\circ C\,yr^{-1}}$ and the autocorrelation-corrected error
is $0.004366\ \mathrm{^\circ C\,yr^{-1}}$ — a factor of **2.26** — and the naive
test's false-positive rate on a no-trend surrogate is **43.8%** against a nominal
5%.

## 2. The data

**Synthetic series (SYNTHETIC).** 600 monthly samples (50 years) built from

$$y(t) = a + b\,t + c_1\cos 2\pi t + c_2 \sin 2\pi t + \eta(t),$$

with $t$ in years, $b = +0.020\ \mathrm{^\circ C\,yr^{-1}}$, seasonal amplitudes
$8.0$ and $-1.5\ \mathrm{^\circ C}$, and $\eta$ an AR(1) process with monthly
lag-1 coefficient $\phi = 0.70$ and innovation standard deviation
$\sigma = 0.50\ \mathrm{^\circ C}$, hence a stationary standard deviation of
$0.700\ \mathrm{^\circ C}$. The realised series runs from $-8.88$ to
$+10.19\ \mathrm{^\circ C}$, with a first-year mean of $0.20$ and a last-year mean
of $1.10\ \mathrm{^\circ C}$.

**Real data for the project itself.** Station series are distributed by national
services and compiled at <https://www.ncei.noaa.gov/products/land-based-station>;
the statistical structure of a real series differs from this synthetic
one, which is exactly why the procedure — not the numbers — is the transferable
part.

**Provenance.** SYNTHETIC. The series was generated **with** a trend, so the only
question the analysis can answer is whether the trend is *detectable*, not whether
it is *real*; §7 keeps that distinction.

## 3. The project specification

**Steps.**

1. State the sampling, the record length and the imposed components; report the
   series' first-year and last-year means.
2. Fit the trend, intercept and two seasonal harmonics in one least-squares
   design, and report the trend with its naive standard error and its $t$-statistic.
3. Compute the residual lag-1 autocorrelation, the integrated time
   $\tau_\text{int} = \Delta t(1+\rho)/(1-\rho)$ and the inflation
   $\sqrt{\tau_\text{int}/\Delta t}$; report the corrected standard error.
4. Generate 500 no-trend surrogates with the same noise process, and measure the
   false-positive rate of the naive and the corrected test at $|t| > 1.96$.
5. Average to annual means, refit, and report the residual autocorrelation, the
   inflation and the corrected error; compare with the monthly result.
6. Write the report: the trend with both error bars, the measured error rates, and
   a paragraph on what the analysis does not establish.

**Deliverable.** The fitted model, the two error bars and their ratio, the
measured false-positive rates, the annual-mean comparison, and the limitations
paragraph.

**Success criterion.** The trend is quoted with the error bar implied by a stated
noise model; the noise model is supported by a measured autocorrelation; the
detection threshold's error rate is measured rather than assumed.

## 4. Why the naive error bar is wrong

Least squares assumes independent errors. For dependent errors the estimator is
still unbiased but its variance is larger:

$$\operatorname{Var}(\hat b)_{\text{corrected}}
\approx \operatorname{Var}(\hat b)_{\text{naive}}\times\frac{\tau_\text{int}}{\Delta t},
\qquad
\tau_\text{int} = \Delta t\,\frac{1+\rho}{1-\rho},$$

with $\rho$ the lag-1 autocorrelation. The demonstration measures
$\rho = 0.6713$, giving

$$\tau_\text{int} = \frac{1}{12}\times\frac{1.6713}{0.3287} = 0.4237\ \mathrm{yr}
\;(5.08\ \text{samples}),
\qquad
\text{inflation} = \sqrt{5.08} = 2.255,$$

so the standard error grows from $0.001936$ to $0.004366\ \mathrm{^\circ C\,yr^{-1}}$
and the $t$-statistic falls from $12.27$ to $5.44$. The trend is still detected —
the synthetic series really does contain one — but the margin is less than half
what the naive calculation claims.

Two cautions. First, the formula assumes the trend's estimator sees a
**red-noise** background; the integration over the record's finite length is
approximate, and the correction is a good approximation only while
$\tau_\text{int} \ll T$. Second, the correction applies to the *trend*; the
seasonal coefficients have their own inflation, and reporting one uncorrected
seasonal amplitude next to a corrected trend is inconsistent.

## 5. Measuring the error rate rather than assuming it

The decisive test is not the formula but the measured false-positive rate.
500 surrogates with the same noise model and **no trend** give

| test | false positives (of 500) | rate | nominal |
|---|---|---|---|
| naive $t$ | 219 | $43.8\%$ | $5\%$ |
| corrected $t$ | 39 | $7.8\%$ | $5\%$ |

The naive test fires in nearly half of records that contain no trend at all: with
50 years of red noise, a $|t| > 1.96$ trend is the *expected* outcome, not
evidence. The correction reduces the rate by a factor of 5.6, from $43.8\%$ to
$7.8\%$ — still above the nominal 5%, and the residual excess is itself
informative: the lag-1-based inflation ignores the higher-lag structure and the
seasonal design's effect, so it under-corrects by about $2.8\%$ in rate. The
honest report quotes the **measured** rate ($7.8\%$) rather than the nominal one.

## 6. Annual means, and what averaging buys

Averaging the 600 months into 50 annual means gives

| quantity | monthly | annual means |
|---|---|---|
| residual lag-1 $\rho$ | $0.6713$ | $0.1575$ |
| inflation | $2.255$ | $1.172$ |
| corrected standard error ($\mathrm{^\circ C\,yr^{-1}}$) | $0.004366$ | $0.004445$ |

Averaging removes most of the month-to-month correlation, as expected: the
inflation collapses from $2.26$ to $1.17$. But the **corrected error on the trend
is essentially unchanged** ($0.004366$ against $0.004445$, a ratio of 0.982),
because there are now twelve times fewer data. The two effects cancel.

This is the single most useful result in the project: **averaging does not reduce
the uncertainty of a trend; it only changes which part of the series' information
you use.** What averaging *does* achieve is interpretability — an annual series is
comparable between stations and free of the seasonal design's assumptions — and
that is a legitimate reason to use it, provided the error bar is not quoted as if
it were a gain.

## 7. Detection versus attribution

The analysis above answers one question: is $b$ distinguishable from zero under a
stated noise model? It does **not** answer why. Attribution requires three
additional things, none of which a single station's trend provides:

1. **A physical model** connecting the candidate cause to the expected pattern —
   the spatio-temporal fingerprint, not just a sign.
2. **A spatial pattern test.** A forced response has a structure (latitude
   dependence, land–sea contrast, seasonal timing); a single trend is one number
   and cannot distinguish it from any other cause with the same sign.
3. **A treatment of spatial correlation.** Stations are not independent; the
   *regional* uncertainty is larger than the average of the station uncertainties,
   and it is the regional number that an attribution statement needs.

Failing to separate these three from "the trend is significant" is the standard
error in non-specialist climate analysis, and it is a labelling error rather than
an arithmetic one.

## 8. Failure modes and how to detect them

1. **A trend with a naive error bar on red noise.** *Detect:* measure the
   false-positive rate on surrogates; $43.8\%$ here.
2. **A seasonal cycle removed by monthly means when the trend must be preserved.**
   *Detect:* the joint fit of §4 and the monthly-mean approach differ; the
   monthly-mean approach biases the trend if the series is unbalanced.
3. **A correction applied to the trend and not to the other coefficients.**
   *Detect:* check that every quoted parameter has the same noise model behind it.
4. **A significance test without a multiplicity statement.** *Detect:* state the
   number of stations, lags or frequencies searched; a regional map of trends
   tests many hypotheses at once.
5. **A detection reported as an attribution.** *Detect:* §7; the absence of a
   fingerprint and a spatial test.
6. **A trend fitted to a series with a step or an inhomogeneity.** *Detect:*
   residual plots and a change-point test such as
   [20-08-04](../../20-signal-processing/08-timeseries-analysis-geophysics/04-change-point-and-detection.md);
   a station move or an instrument change is a step, not a trend.

## 9. Rubric

| Criterion | 4 — exemplary | 3 — competent | 2 — developing | 1 — incomplete |
|---|---|---|---|---|
| Model | Trend and seasonality fitted jointly, unit stated | Trend fitted | Trend by eye | None |
| Noise model | $\rho$, $\tau_\text{int}$ and its assumption stated | $\rho$ measured | Assumed white | Absent |
| Error bars | Both quoted with the ratio | Corrected value | Naive value | None |
| Error rate | Measured on surrogates, compared with nominal | Stated | Mentioned | Assumed 5% |
| Limitations | Detection versus attribution separated | Caveat | Generic | Absent |

## 10. Assumptions and regime of validity

1. **The trend is linear.** A curvature, an acceleration or a regime shift is
   absorbed into "noise" and inflates the residual variance; a quadratic term is
   the minimal test.
2. **The noise is AR(1) and stationary.** Long-memory series need a different
   (larger) inflation; a variance change breaks the stationarity the whole
   calculation rests on.
3. **The seasonal cycle is two harmonics.** Higher harmonics, a moving seasonal
   cycle or a leap-year convention leave structure that inflates $\rho$.
4. **The record is homogeneous.** A site move, an instrument change or a
   time-of-observation change produces a step that a linear trend misreads.
5. **One location.** Nothing in a single-station analysis constrains a region;
   spatial correlation is an independent inflation.

## The honest summary

The project's answer is a procedure, not a number. On a synthetic 50-year monthly
series with an imposed $+0.020\ \mathrm{^\circ C\,yr^{-1}}$ trend, the fit returns
$+0.023746\ \mathrm{^\circ C\,yr^{-1}}$ with a residual lag-1 autocorrelation of
$0.6713$, an integrated time of $0.4237\ \mathrm{yr}$ and an inflation of
$2.255$: the error bar is $0.001936$ naive and $0.004366$ corrected, and the
$t$-statistic falls from $12.27$ to $5.44$. The naive test's false-positive rate,
measured on 500 no-trend surrogates, is $43.8\%$ against a nominal 5%; the
corrected test achieves $7.8\%$. Annual averaging cuts the inflation to $1.172$
but leaves the trend's error bar unchanged at $0.004445\ \mathrm{^\circ C\,yr^{-1}}$.
The transferable statement is that **a trend is only as meaningful as the noise
model behind its error bar**, and that a detected trend is not an attributed one.

## Python demonstration

[`code/climate_trend_demo.py`](./code/climate_trend_demo.py) prints every number
quoted above. It:

1. prints the series' components and its first-year and last-year means;
2. fits the trend with seasonal harmonics and prints $b = +0.023746\
   \mathrm{^\circ C\,yr^{-1}}$, $\rho = 0.6713$, $\tau_\text{int} = 0.4237\
   \mathrm{yr}$, both error bars and both $t$-statistics;
3. runs 500 no-trend surrogates and prints the measured false-positive rates
   ($43.8\%$ naive, $7.8\%$ corrected);
4. refits on annual means and prints the reduced autocorrelation ($0.1575$), the
   inflation ($1.172$) and the essentially unchanged corrected error
   ($0.004445\ \mathrm{^\circ C\,yr^{-1}}$);
5. prints the five things the analysis does not establish.

Run it with the project virtual environment:

```bash
cd 25-projects-capstone/03-advanced-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_trend_demo.py
```

The script prints only, writes no files, uses no network and exits 0. It runs in
under a second (the surrogates are generated with `scipy.signal.lfilter`).

## Exercises

Graded problems and worked solutions are in
[`exercises/04-climate-data-analysis-project-exercises.md`](./exercises/04-climate-data-analysis-project-exercises.md)
and
[`exercises/04-climate-data-analysis-project-solutions.md`](./exercises/04-climate-data-analysis-project-solutions.md).
The ★★★ item asks you to design a regional attribution test, not to refit one
station.

## Mastery checkpoint

Without notes:

1. State why the ordinary least-squares standard error of a trend is too small
   when the residuals are autocorrelated.
2. Compute $\tau_\text{int}$ and the inflation factor for $\rho = 0.5$ and
   $\Delta t = 0.25\ \mathrm{yr}$.
3. A colleague reports a trend of $+0.30\ \mathrm{^\circ C\,per\ decade} \pm
   0.05$ from 40 years of monthly data. State the two things you would ask for.
4. Explain in one sentence why annual averaging did not improve the trend's error
   bar in the demonstration.

## Common pitfalls

1. **A white-noise error bar on red-noise data.** The error rate was $43.8\%$
   against a nominal 5%.
2. **Ignoring the seasonal cycle's effect on the residual autocorrelation.** It
   is part of the noise model.
3. **Assuming annual averaging buys precision.** It changes the question, not the
   uncertainty.
4. **Calling a significant trend an attribution.** Fingerprints and spatial tests
   are missing.
5. **Fitting a linear trend through a step.** Station moves and instrument
   changes are inhomogeneities, not trends.

## Where this is used

The same inflation factor appears in every geophysical trend estimate: in geodetic
series ([20-08-03](../../20-signal-processing/08-timeseries-analysis-geophysics/03-geodetic-time-series.md)),
in sea-level and tide analysis, and in the climate attribution literature
([16-07-02 Detection and Attribution of Climate Change](../../16-atmosphere-climate/07-climate-extremes-and-attribution/02-detection-attribution.md)).
In professional practice a trend quoted without its noise model is returned for
revision, and the surrogate-measured error rate of §5 is the standard defence
against a reviewer's question about multiplicity.

## Related lessons

- [20-08-05 Climate Time-Series Analysis and Modes of Variability](../../20-signal-processing/08-timeseries-analysis-geophysics/05-climate-timeseries.md) —
  the modes (ENSO, NAO) that a station trend must not be confused with.
- [16-08-03 Homogenisation, Bias Adjustment and Uncertainty](../../16-atmosphere-climate/08-climate-observation-and-data/03-climate-data-homogenisation.md) —
  the inhomogeneity problem behind pitfall 5.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  the block-bootstrap alternative to the $\tau_\text{int}$ correction.
- [25-05-03 Project: Geodynamic Model-Data Comparison](../05-doctoral-projects/03-geodynamic-model-data.md) —
  the model-versus-data discipline that attribution requires.

## Self-assessment checklist

- [ ] I can fit a trend and seasonality jointly with a stated design.
- [ ] I can measure a residual autocorrelation and convert it to an inflation.
- [ ] I can quote both error bars and their ratio.
- [ ] I can measure a test's false-positive rate on surrogates.
- [ ] I can explain what annual averaging does and does not buy.
- [ ] I can separate detection from attribution in three sentences.
