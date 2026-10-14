---
id: 21-07-04
title: "Forecast Evaluation, Skill Scores and Calibration"
level: research
prereqs: ["21-07-01", "21-01-03", "21-06-09"]
estimated_minutes: 60
tags: [time-series, forecasting, skill-scores, calibration, verification, teaching]
---

# Forecast Evaluation, Skill Scores and Calibration

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** RMSE, MAE, bias, correlation and a skill score against a named
   reference forecast, and **state** what each one measures and what it hides.
2. **Compute** the analytic mean-square errors of climatology, persistence and an
   AR(1) forecast as a function of horizon, and **derive** the horizon at which
   persistence stops beating climatology.
3. **Explain** why the ranking of three forecasts changes along the horizon axis,
   and why a single-horizon report is not a verification.
4. **Distinguish** accuracy from calibration: **measure** coverage and sharpness of
   prediction intervals and **interpret** what a biased forecast does to each.
5. **Diagnose** a forecast that is sharp and wrong, and one that is honest and
   useless, from the same table.
6. **Choose** the reference forecast that makes a skill score meaningful, and
   **state** the effect of choosing a weak one.
7. **Specify** a verification report: the reference, the horizons, the metrics, the
   interval calibration, the sample size with its effective count, and the
   pairing between forecast and observation.

Every series, forecast and metric below is **SYNTHETIC**, produced by
[`code/forecast_evaluation_demo.py`](./code/forecast_evaluation_demo.py). No
forecast archive, observation record or published skill score is read or quoted.

## Prerequisites

- [21-07-01 AR, MA, ARIMA and Their Interpretation](./01-arima-models.md) —
  the process whose forecasts are being scored.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  the machinery for putting an interval on a skill score.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](../../21-statistics-bayesian-ml/06-ml-in-geophysics/09-ml-pitfalls-geophysics.md) —
  the non-stationarity that destroys a verification computed in-sample.
- [20-08-05 Climate Time Series](../../20-signal-processing/08-timeseries-analysis-geophysics/05-climate-timeseries.md) —
  the seasonal and trend handling that precedes any verification.

## 1. Intuition: a metric is a comparison, and the reference is the claim

An RMSE of $2.0$ K means nothing on its own. Three questions decide its meaning:

- **Against what?** A number is a *skill score* only relative to a stated
  reference. Climatology (the long-run mean) is the standard reference because it
  is free; persistence (tomorrow = today) is the natural reference for a
  geophysical series with memory.
- **At what horizon?** Skill decays with lead time, and the ranking of two methods
  can reverse along that axis.
- **With what uncertainty?** An RMSE computed from $n$ temporally correlated pairs
  has far fewer independent samples than $n$.

This lesson measures all three on one series, and the result is a table in which
the same three forecasts swap places between horizon 1 and horizon 10.

## 2. The synthetic series and the four forecasts

| Property | Value |
|---|---|
| truth | AR(1), $\varphi = 0.80$, $\sigma_w = 1.8$ K, $\mu = 12.0$ K, $n = 2000$ |
| stationary standard deviation | $3.0000$ K theoretical, $2.9476$ K measured |
| horizons | $h = 1, 2, 3, 4, 6, 10$ epochs |
| forecasts | climatology, persistence, AR(1), AR(1) + 1.5 K bias |
| reference for the skill score | climatology, using the mean estimated from the first 1000 epochs: $11.6282$ K |

The reference is estimated from a *training* half so that the skill score has a
fair baseline; note that the estimated mean is $0.372$ K below the generator's
$12.0$ K, which is the sampling error of a mean of a correlated series and is
itself a source of the climatology forecast's bias (measured $-0.154$ K).

## 3. Accuracy metrics as a function of horizon

| $h$ | forecast | RMSE (K) | MAE (K) | bias (K) | skill | corr |
|---|---|---|---|---|---|---|
| 1 | climatology | 2.9515 | 2.3700 | $-0.1539$ | $0.0000$ | $0.0000$ |
| 1 | persistence | 1.8763 | 1.4975 | $-0.0025$ | $+0.5959$ | $0.7973$ |
| 1 | AR(1) | 1.7794 | 1.4324 | $-0.0328$ | $+0.6366$ | $0.7973$ |
| 1 | AR(1)+bias | 2.3060 | 1.8689 | $+1.4672$ | $+0.3896$ | $0.7973$ |
| 3 | persistence | 2.9422 | 2.3451 | $-0.0056$ | $+0.0072$ | $0.5019$ |
| 3 | AR(1) | 2.5518 | 2.0366 | $-0.0784$ | $+0.2532$ | $0.5019$ |
| 4 | persistence | 3.2270 | 2.5788 | $-0.0050$ | $-0.1941$ | $0.4010$ |
| 4 | AR(1) | 2.7033 | 2.1536 | $-0.0927$ | $+0.1620$ | $0.4010$ |
| 10 | persistence | 3.9327 | 3.1025 | $+0.0039$ | $-0.7742$ | $0.1112$ |
| 10 | AR(1) | 2.9335 | 2.3531 | $-0.1315$ | $+0.0128$ | $0.1112$ |

(The table is abridged; the demonstration prints all four forecasts at all six
horizons.)

Four readings:

1. **The AR(1) forecast wins at every horizon.** That is not automatic: it is the
   correct model for this generator, and its mean-square error is
   $\sigma^2(1-\varphi^{2h})$, which is always below $\sigma^2$.
2. **Persistence beats climatology only while $\varphi^h > 0.5$.** Its error
   variance is $2\sigma^2(1-\varphi^h)$, which is below $\sigma^2$ exactly when
   $\varphi^h > 0.5$ — for $\varphi = 0.80$ that is $h < 3.11$, i.e. $h \le 3$.
   Measured, the crossing happens between $h = 3$ (persistence RMSE $2.9422$
   against climatology $2.9528$) and $h = 4$ ($3.2270$ against $2.9531$): the
   analytic threshold and the measurement agree.
3. **The correlation is a property of the forecast, not of its quality.** All
   three unbiased forecasts have *identical* correlations at every horizon
   ($0.7973$ at $h = 1$, decaying to $0.1112$ at $h = 10$), because correlation is
   invariant to an affine transformation and all three are
   $\mu + a(x_t - \mu)$ with different $a$. The correlation cannot therefore rank
   them — which is precisely why a report that quotes only the correlation has
   said nothing about skill.
4. **A 1.5 K bias is expensive at short horizons and cheap at long ones.** At
   $h = 1$ the biased forecast's RMSE rises from $1.7794$ to $2.3060$ — it loses
   the contest — because the bias is a large fraction of the forecast error. At
   $h = 10$ its RMSE is $3.2343$ against climatology's $2.9525$: still worse, but
   the bias is now a smaller fraction of a larger error. A bias costs what it costs
   relative to the *other* error terms, so its importance is a function of horizon.

## 4. Calibration: coverage and sharpness

Accuracy measures the centre of a forecast; a probabilistic forecast makes two
further claims, and they are independent.

| $h$ | forecast | 80% coverage | 90% coverage | 90% width (K) |
|---|---|---|---|---|
| 1 | climatology | 0.808 | 0.913 | 9.8694 |
| 1 | persistence | 0.798 | 0.898 | 6.2420 |
| 1 | AR(1) | 0.802 | 0.903 | 5.9216 |
| 1 | AR(1)+bias | 0.669 | 0.790 | 5.9216 |
| 4 | AR(1) | 0.811 | 0.906 | 9.0035 |
| 4 | AR(1)+bias | 0.755 | 0.865 | 9.0035 |
| 10 | AR(1) | 0.803 | 0.913 | 9.8123 |
| 10 | AR(1)+bias | 0.774 | 0.873 | 9.8123 |

Reading:

1. **The correctly specified forecasts are calibrated.** Coverage matches the
   nominal level at every horizon (0.80–0.81 against 0.80; 0.90–0.91 against
   0.90). This is a genuine achievement of the model, not a tautology: the
   forecast variance $\sigma^2(1-\varphi^{2h})$ had to be right.
2. **The biased forecast has identical sharpness and worse coverage.** Its widths
   are the same to four decimals — a bias does not change the *spread* of the
   error — while coverage falls to $0.669$ at $h = 1$ and $0.774$ at $h = 10$.
   The interval is as informative as the good one and wrong: a combination that
   every accuracy table misses and the coverage column catches.
3. **Sharpness alone is not a virtue.** Persistence has the second-narrowest
   interval at $h = 1$ ($6.2420$ against climatology's $9.8694$) *and* the
   second-best accuracy, but its width grows without bound
   ($13.1868$ at $h = 10$) while its coverage stays near nominal — the interval is
   honest about an increasingly useless forecast. Only coverage *and* width
   together describe a probabilistic forecast.

## 5. What a verification report needs

| Item | Why |
|---|---|
| the reference forecast | a skill score is meaningless without it |
| the horizons, all of them | the ranking reverses; the axis is part of the result |
| RMSE and MAE together | MAE is less sensitive to outliers and is the metric of a decision made in absolute error |
| bias, per horizon | separates a mis-centred forecast from a noisy one |
| correlation, if quoted, labelled as a shape measure | it cannot rank affine-related forecasts |
| coverage and width, per horizon | calibration is independent of accuracy |
| sample size and effective count | correlated pairs inflate significance; report $\tau_{\text{int}}$ and $n_{\text{eff}}$ |
| the pairing of forecast and observation | a verification with mismatched spatial or temporal support measures the mismatch, not the model |

## 6. Assumptions and regime of validity

1. **The verifying truth is what it claims to be.** An analysis, a reanalysis or a
   gridded product used as truth carries its own error, which sets a floor on the
   measurable RMSE.
2. **The process is stationary.** The demonstration's generator is; a skill score
   computed across a regime change measures the change, not the forecast.
3. **The forecast is calibrated as a probability statement.** The intervals here
   use the model's own variance; a machine-learned forecast needs either a
   distributional assumption or an empirical calibration step.
4. **Errors are serially correlated.** The $n$ pairs are not independent; the
   effective count is $n/\tau_{\text{int}}$, and a naive interval can be several
   times too narrow.
5. **The reference is honest.** Climatology estimated from the same period that
   includes the verification targets flatters the reference and deflates the skill
   score; it must come from a training period, as here.

## The honest summary

On 2000 epochs of an AR(1) process with $\varphi = 0.80$ and $\sigma = 3.0$ K,
the correct forecasting model reaches RMSE $1.7794$ K at one epoch and $2.9335$ K
at ten, with skill scores $+0.6366$ and $+0.0128$ against a climatology estimated
from a training half. Persistence beats climatology for $h \le 3$ and loses from
$h = 4$, exactly where $\varphi^h = 0.5$ — the analytic threshold, confirmed by
measurement. All three unbiased forecasts have identical correlations at every
horizon, so correlation cannot rank them. A 1.5 K bias raises the RMSE from
$1.7794$ to $2.3060$ K at $h = 1$, leaves the interval widths identical to four
decimals, and drops the 80% coverage from $0.802$ to $0.669$. The transferable
conclusions: quote the reference and the horizon; report accuracy and calibration
separately; distrust a single-horizon number; and remember that the same
forecasts reverse their ranking along the horizon axis.

## Python demonstration

[`code/forecast_evaluation_demo.py`](./code/forecast_evaluation_demo.py) prints
every number quoted above. It:

1. generates the AR(1) truth, prints the stationary standard deviation and the
   training-period climatological mean, and names the four forecasts;
2. prints RMSE, MAE, bias, skill and correlation for all four forecasts at six
   horizons;
3. prints the best and worst forecast at each horizon, so the ranking reversal is
   visible, with the analytic crossing condition;
4. prints the 80% and 90% interval coverage and the 90% width for every forecast at
   every horizon, then a `SYNTHETIC` provenance line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/07-time-series-and-forecasting/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python forecast_evaluation_demo.py
```

It runs in under 0.1 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/04-forecast-evaluation-exercises.md`](./exercises/04-forecast-evaluation-exercises.md)
and [`exercises/04-forecast-evaluation-solutions.md`](./exercises/04-forecast-evaluation-solutions.md).

## Mastery checkpoint

Without notes:

1. Derive the horizon at which persistence stops beating climatology for
   $\varphi = 0.8$ and for $\varphi = 0.6$, and compare the first with the
   measurement.
2. Compute the theoretical RMSE of the AR(1) forecast at $h = 1$ and $h = 10$ and
   compare with the measured $1.7794$ and $2.9335$ K.
3. All three unbiased forecasts have correlation $0.7973$ at $h = 1$. Explain why
   and state the consequence for a report that quotes only correlation.
4. A forecast has 90% interval coverage of 0.65 and the narrowest intervals in the
   comparison. State the two claims it fails and which table entry reveals each.

## Common pitfalls

1. **Quoting an RMSE without a reference.** $2.0$ K is excellent against a
   climatological spread of $3.0$ K and useless against $0.5$ K.
2. **Verifying at one horizon.** Persistence is second-best at $h = 1$ and worst at
   $h = 10$.
3. **Using correlation to rank forecasts.** Affine-related forecasts share it
   exactly.
4. **Reporting sharpness without coverage.** The biased forecast has identical
   widths and 0.669 coverage at $h = 1$.
5. **Ignoring the serial correlation of the verification pairs.** The effective
   count is $n/\tau_{\text{int}}$, not $n$.
6. **Estimating the reference on the verification period.** It flatters the
   reference and shrinks every skill score.

## Where this is used

- **Weather and climate verification**, where the reference hierarchy
  (climatology, persistence, a previous model version) and the horizon dependence
  are standard practice
  ([16-05-06](../../16-atmosphere-climate/05-climate-models/06-emulation-and-surrogates.md)).
- **Hydrological forecasting**, where the decision metric is in absolute error and
  the reference is the seasonal climatology of the basin.
- **Geodetic and seismic hazard updates**, where the forecast is a probability and
  calibration is the whole claim
  ([06-11-04](../../06-seismology/11-earthquake-statistics-and-hazard/04-psha.md)).
- **Machine-learned surrogate models**, where coverage of the predicted interval is
  the property most often missing from a report.

## Related lessons

- [21-07-01 AR, MA, ARIMA and Their Interpretation](./01-arima-models.md) —
  the forecasting model scored here.
- [21-07-02 State-Space Models and Kalman Filtering](./02-state-space.md) —
  the same predictive distributions produced recursively.
- [21-07-05 Point Processes and Seismicity Rate Models](./05-point-processes.md) —
  verification when the forecast is a rate rather than a value.
- [21-07-03 Statistical Spectral Analysis and Significance Testing](./03-spectral-analysis-statistical.md) —
  the frequency-domain view of the same series.
- [21-09-02 Honest Reporting of Uncertainty and Limitations](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/02-reporting-uncertainty-ethics.md) —
  the reporting standard this verification table implements.

## Self-assessment checklist

- [ ] I can define a skill score against a named reference.
- [ ] I can derive the persistence-versus-climatology crossing horizon.
- [ ] I can explain why correlation cannot rank affine forecasts.
- [ ] I can compute coverage and sharpness and interpret each.
- [ ] I can name the two failure modes a coverage table reveals.
- [ ] I can list the eight items a verification report must contain.
