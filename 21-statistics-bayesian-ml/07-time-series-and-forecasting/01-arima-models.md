---
id: 21-07-01
title: "AR, MA, ARIMA and Their Interpretation"
level: research
prereqs: ["21-01-04", "20-05-01", "21-06-09"]
estimated_minutes: 60
tags: [time-series, arima, autocorrelation, stationarity, teaching]
---

# AR, MA, ARIMA and Their Interpretation

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the AR(1), MA(1) and ARMA(1,1) recursions and **state** what each
   parameter does to the autocorrelation function.
2. **Derive** the AR(1) autocovariance, the integrated correlation time and the
   one-step-ahead prediction error in closed form.
3. **Estimate** the AR(1) coefficient by Yule-Walker and the MA(1) coefficient by
   the method of moments, and **explain** why the MA(1) has two roots of which
   only one is admissible.
4. **Identify** an ARMA(1,1) from $\rho_1$ and $\rho_2$, and **state** why the
   moment equations become ill-conditioned as $\varphi \to \theta$.
5. **Choose** the order of differencing from the autocorrelation function rather
   than from an in-sample fit.
6. **Interpret** a fitted ARIMA model physically: which coefficient is a
   memory, which is a noise-shaping term, and which is a trend.
7. **Report** a model as a tuple of estimated coefficients with standard errors,
   the innovation variance, the sample size, and the diagnostic residuals.

Every series and every estimate below is **SYNTHETIC**, produced by
[`code/arima_models_demo.py`](./code/arima_models_demo.py). No record, catalogue
or published parameter estimate is read or quoted.

## Prerequisites

- [21-01-04 Linear, Multiple and Robust Regression](../../21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md) —
  the estimation vocabulary reused here for time-series parameters.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md) —
  stationarity, the autocorrelation function and the integrated time.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](../../21-statistics-bayesian-ml/06-ml-in-geophysics/09-ml-pitfalls-geophysics.md) —
  the trending-series trap that differencing exists to fix.
- [20-08-01 Detrending and Deseasonalising](../../20-signal-processing/08-timeseries-analysis-geophysics/01-detrending-seasonality.md) —
  what to do before fitting a stationary model.

## 1. Intuition: memory and noise shaping

A time series model answers one question: **how much of today carries into
tomorrow?** Three elementary answers, and everything in the ARIMA family is a
combination of them.

- **AR(1)**: $x_t = \varphi x_{t-1} + w_t$. Today is a fraction $\varphi$ of
  yesterday plus fresh noise. The memory decays geometrically, $\rho_k =
  \varphi^k$, and the process is *persistent*: a high value today predicts a high
  value tomorrow.
- **MA(1)**: $x_t = w_t + \theta w_{t-1}$. There is no memory of *values* at all;
  the correlation comes from the noise being shared between adjacent
  observations. It dies after one lag exactly: $\rho_1 = \theta/(1+\theta^2)$,
  $\rho_k = 0$ for $k \ge 2$.
- **ARMA(1,1)**: both, and the autocorrelation then decays geometrically *from*
  its lag-one value — the same shape as an AR(1) for $k \ge 2$, which is the
  identifiability problem of §5.

The distinction matters physically. A persistent series is one where a *state*
evolves (a groundwater level, a deformation trend, a slowly drifting instrument
bias); an MA series is one where a *shock* is smeared over a few epochs (a
processing artefact, a moving-average filter, a multi-epoch measurement). Fitting
a persistent model to a shock-smeared series, or the reverse, gives a model that
forecasts, but the coefficients no longer mean anything.

## 2. The synthetic series and their autocorrelations

Four thousand samples, unit innovation standard deviation, seed 20261014.
Measured autocorrelations against theory:

| lag | AR(1) $\rho_k$ | theory $\varphi^k$ | MA(1) $\rho_k$ | theory | ARMA(1,1) $\rho_k$ |
|---|---|---|---|---|---|
| 1 | $+0.7106$ | $+0.7000$ | $+0.4028$ | $+0.4000$ | $+0.7565$ |
| 2 | $+0.5066$ | $+0.4900$ | $+0.0134$ | $0.0000$ | $+0.4521$ |
| 3 | $+0.3595$ | $+0.3430$ | $+0.0127$ | $0.0000$ | $+0.2611$ |
| 4 | $+0.2569$ | $+0.2401$ | $+0.0110$ | $0.0000$ | $+0.1449$ |
| 5 | $+0.1824$ | $+0.1681$ | $-0.0026$ | $0.0000$ | $+0.0777$ |

The sampling error of a sample autocorrelation at lag $k$ is roughly
$1/\sqrt{n} = 0.016$, so every measured value is consistent with its theory and
the MA(1) tail ($0.013$, $0.013$, $0.011$, $-0.003$) is the null distribution in
action.

The reading rules that follow from this table:

1. **Geometric decay from lag 1** → an autoregressive memory. Read off
   $\varphi \approx \rho_1$.
2. **A sharp cut-off after lag 1** → a moving-average term. The MA(1) signature is
   the only one that is *exactly* zero further out.
3. **Decay starts at a value below its lag-0 level and then decays
   geometrically** → ARMA, and the AR and MA parameters cannot be separated from
   the ACF alone (see §5).

## 3. AR(1): everything in closed form

For $x_t = \varphi x_{t-1} + w_t$ with $|w|$ white of variance $\sigma_w^2$ and
$|\varphi| < 1$:

$$\sigma^2 = \frac{\sigma_w^2}{1-\varphi^2}, \qquad
\rho_k = \varphi^{|k|}, \qquad
\tau_{\text{int}} = \Delta t\,\frac{1+\varphi}{1-\varphi}, \qquad
\operatorname{Var}(\hat x_{t+1}) = \sigma_w^2 .$$

The last identity is the useful one: **the one-step-ahead prediction error is the
innovation variance, not the process variance.** With $\varphi = 0.70$ and
$\sigma_w = 1$:

$$\sigma^2 = \frac{1}{1-0.49} = 1.9608\ (\text{std } 1.4003), \qquad
\tau_{\text{int}} = \frac{1.70}{0.30} = 5.67\ \text{samples}.$$

Measured on the realisation: the unconditional variance estimate is used to
predict with the sample mean, giving MSE $2.0019$; the one-step prediction
$\hat x_{t+1} = 0.70 x_t$ gives MSE $0.9913$ against the theoretical $1.0000$.
The variance reduction is $0.5048$, and the theoretical $R^2$ is
$\varphi^2 = 0.49$ — the two differ by sampling error, and their near-agreement
is the check that the model is doing what it claims.

**Estimation.** Yule-Walker sets $\hat\varphi = \hat\rho_1$:

$$\hat\varphi = +0.7106 \quad\text{against } +0.70 \quad (\text{error } +0.0106).$$

The error is $0.66$ of the $\pm1/\sqrt{n}$ scale, which is what an efficient
estimator should show.

## 4. MA(1): two roots, one admissible

For $x_t = w_t + \theta w_{t-1}$,

$$\rho_1 = \frac{\theta}{1+\theta^2}, \qquad \rho_k = 0\ (k \ge 2),$$

and inverting for $\theta$ gives a quadratic with two roots, $\theta$ and
$1/\theta$. Measured on the realisation, $\hat\rho_1 = +0.4028$, giving

$$\hat\theta = +0.5058 \quad (\text{error } +0.0058), \qquad
\text{the other root } 1/\hat\theta = +1.9771 .$$

Both roots reproduce the same autocorrelation function — the ACF cannot tell them
apart — and the **invertibility** convention chooses the one with $|\theta| < 1$,
which is the representation in which the current value depends on past *shocks*
rather than on a growing sum of future ones. The convention is not a physical
law; it is the statement that the model can be used to forecast from the observed
history. Reporting the two roots, and which one was chosen, is therefore part of
the report.

## 5. ARMA(1,1): identifiable in principle, fragile in practice

For $\text{ARMA}(1,1)$ the autocorrelation satisfies $\rho_k = \varphi\,\rho_{k-1}$
for $k \ge 2$, so the AR parameter is recoverable from the ratio of two lags:

$$\hat\varphi = \frac{\hat\rho_2}{\hat\rho_1} = +0.5976
\quad\text{against } +0.60 \quad (\text{error } -0.0024),$$

and $\theta$ then follows from $\rho_1$ by solving

$$\theta^2(\rho_1 - \varphi) + \theta(2\rho_1\varphi - 1 - \varphi^2)
+ (\rho_1 - \varphi) = 0,$$

whose two roots here are $+2.4400$ and $+0.4098$; the invertible root is
$+0.4098$, against a true $+0.40$ (error $+0.0098$).

Two cautions. The equations **divide by $\rho_1$ and by $(\rho_1 - \varphi)$**, so
they degrade as $\varphi$ approaches $\theta$ (the two roots collide) and on short
records. The same two equations on a 200-sample realisation of the same process
give $\hat\varphi = +0.5673$ (error $-0.0327$) and $\hat\theta = +0.4798$ (error
$+0.0798$) — three to eight times the errors of the long record, from the same
estimator. That fragility is the practical reason ARMA models are fitted by
maximising a likelihood rather than by matching moments, and it is why a reported
ARMA fit must carry standard errors.

## 6. Ordering and differencing

Differencing is not a fitting choice; it is a statement about stationarity. A
random walk (integration of order 1) has an autocorrelation that does not decay:

| series | $\rho_1$ | $\rho_2$ | $\rho_3$ | $\rho_4$ | $\rho_5$ |
|---|---|---|---|---|---|
| levels of a random walk | $+0.996$ | $+0.993$ | $+0.989$ | $+0.986$ | $+0.982$ |
| first differences | $+0.005$ | $-0.022$ | $+0.009$ | $+0.022$ | $+0.005$ |

The variance of the first half of the walk is $261.5$ and of the second half
$92.4$ — its amplitude wanders, which is the definition of non-stationarity. One
difference renders the series white, and the $d = 1$ is *read* from the ACF, not
discovered by trying models until the residual looks small. Fitting a stationary
ARMA to the levels would produce a $\varphi$ near 1 and a spuriously good
in-sample fit — the same trap as the spurious correlation of
[21-06-09](../../21-statistics-bayesian-ml/06-ml-in-geophysics/09-ml-pitfalls-geophysics.md).

## 7. Assumptions and regime of validity

1. **Linearity.** ARMA models are linear recursions; a series whose dynamics
   depend on the regime (a threshold, a saturation) needs a different family.
2. **Stationarity after differencing.** $d$ is finite and the differenced series
   has constant variance; a series with a changing variance needs a
   transformation first.
3. **Gaussian innovations.** Needed for the standard errors and the likelihood as
   commonly reported; the point forecasts need only the second moments.
4. **No seasonality.** A seasonal cycle must be differenced or modelled
   explicitly, otherwise the ACF shows spikes at the seasonal lags that the
   ARMA order cannot capture.
5. **The parameters are constant over the record.** A drifting $\varphi$ — a
   changing memory — is a regime change, and it violates the model; see
   [20-08-04](../../20-signal-processing/08-timeseries-analysis-geophysics/04-change-point-and-detection.md).

## The honest summary

On four thousand synthetic samples, Yule-Walker recovers an AR(1) coefficient of
$+0.7106$ against a true $+0.70$, a moment estimator recovers an MA(1)
coefficient of $+0.5058$ against $+0.50$ (choosing the invertible root of a
quadratic pair), and the ARMA(1,1) moment equations recover $+0.5976$ and
$+0.4098$ against $+0.60$ and $+0.40$ — but three to eight times worse on a
200-sample record from the same process. The one-step-ahead prediction error is
$0.9913$ against a theoretical innovation variance of $1.0000$, a variance
reduction of $0.5048$ against a theoretical $R^2$ of $0.49$. The transferable
conclusions: the ACF shape identifies the family; the MA has two roots and the
invertible one is a convention, not a discovery; ARMA moment estimates are
fragile and need standard errors; and the differencing order is a statement about
stationarity, read from the ACF before any model is fitted.

## Python demonstration

[`code/arima_models_demo.py`](./code/arima_models_demo.py) prints every number
quoted above. It:

1. simulates the AR(1), MA(1) and ARMA(1,1) series and prints five sample
   autocorrelations beside their theoretical values;
2. recovers each parameter from the moments, printing both roots where the
   equation has two, and repeating the ARMA estimate on a 200-sample record;
3. prints the unconditional variance, the one-step-ahead MSE, the
   mean-prediction MSE and the variance reduction;
4. differences a random walk and prints the autocorrelations of the levels and
   the increments beside the split-half variances, then a `SYNTHETIC` line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/07-time-series-and-forecasting/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python arima_models_demo.py
```

It runs in under 0.1 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/01-arima-models-exercises.md`](./exercises/01-arima-models-exercises.md)
and [`exercises/01-arima-models-solutions.md`](./exercises/01-arima-models-solutions.md).

## Mastery checkpoint

Without notes:

1. From the measured $\rho_1$ of the AR(1) series, compute $\varphi$, $\sigma^2$,
   $\tau_{\text{int}}$ and the one-step-ahead prediction standard error, and state
   each unit.
2. The MA(1) has roots $0.5058$ and $1.9771$. Explain why the ACF cannot choose
   between them and what the invertibility convention asserts.
3. State the two equations that identify an ARMA(1,1) and the condition under
   which they fail.
4. A colleague fits an ARMA(2,2) to a series whose ACF decays linearly to zero
   over the whole record. State the diagnosis and the first step.

## Common pitfalls

1. **Reading a slowly decaying ACF as high persistence.** A random walk's
   $\rho_1 = 0.996$ is non-stationarity, not memory.
2. **Reporting one MA root.** Both reproduce the ACF; the choice is a convention.
3. **Quoting ARMA coefficients without standard errors.** The short-record errors
   here are three to eight times the long-record ones.
4. **Choosing the differencing order to improve the fit.** $d$ is a statement
   about stationarity and is read from the ACF.
5. **Ignoring seasonality.** A seasonal spike in the ACF cannot be absorbed by a
   non-seasonal ARMA order.
6. **Treating the one-step error as the forecast error at all horizons.** It is
   $\sigma_w^2$ at $h = 1$ and approaches $\sigma^2$ as $h$ grows.

## Where this is used

- **Geodetic and hydrological series**, where the persistence is physical and its
  integrated time sets the error bar of a trend
  ([20-08-03](../../20-signal-processing/08-timeseries-analysis-geophysics/03-geodetic-time-series.md)).
- **Climate and ocean series**, where seasonal differencing is a prerequisite
  rather than an option
  ([20-08-05](../../20-signal-processing/08-timeseries-analysis-geophysics/05-climate-timeseries.md)).
- **Instrument-drift modelling**, where an AR(1) describes the wander of a
  calibration offset.
- **Forecast baselines**, where the AR model is the reference that any larger
  model must beat ([21-07-04](./04-forecast-evaluation.md)).

## Related lessons

- [21-07-02 State-Space Models and Kalman Filtering](./02-state-space.md) —
  the same processes written as a state evolving with noise.
- [21-07-03 Statistical Spectral Analysis and Significance Testing](./03-spectral-analysis-statistical.md) —
  the frequency-domain view of the same autocovariance.
- [21-07-04 Forecast Evaluation, Skill Scores and Calibration](./04-forecast-evaluation.md) —
  how to compare the forecasts these models produce.
- [21-07-05 Point Processes and Seismicity Rate Models](./05-point-processes.md) —
  what to do when the observation is an event time rather than a sample.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md) —
  the underlying process theory.

## Self-assessment checklist

- [ ] I can write the three recursions and sketch their ACFs.
- [ ] I can derive $\sigma^2$, $\rho_k$ and the one-step error for AR(1).
- [ ] I can invert $\rho_1$ for an MA(1) and state both roots.
- [ ] I can identify an ARMA(1,1) from two lags and say when it fails.
- [ ] I can read the differencing order from an ACF.
- [ ] I can list the five items an ARIMA report must contain.
