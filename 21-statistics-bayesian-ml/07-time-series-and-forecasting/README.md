# Module 21-07 — Time-Series Modelling and Forecasting

**Stages:** research · **Prerequisites:** modules 21-01 and 21-04;
[20-05-01 Stochastic Processes](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md).

This module takes the statistics of correlated sequences and turns it into
forecasting practice. Each lesson adds one piece of machinery — an ARIMA model, a
hidden state, a spectral test, a verification table, a point-process rate — and
each ends with a measurement of what the machinery does *not* fix: the ARMA moment
estimator's fragility, the gain's dependence on two variances, the multiplicity of
frequencies, the cost of a bias to an interval, and the factor of 36 between two
forecasts from one catalogue.

The organising idea is that **a time-series model is a statement about what is
stationary, and every forecast is a comparison against a named reference.** The
differencing order is read from the autocorrelation function rather than chosen to
improve a fit; the state-space model separates what is unobserved from what was
measured; the spectral test distinguishes a pre-specified frequency from a
searched one; the verification table separates accuracy from calibration; and the
point-process lesson shows that a rate forecast requires the *state* as an input,
not just a long-run average.

All models and data in this module are **SYNTHETIC**. Every demonstration generates
its own series or catalogue, seeds `np.random.default_rng(20261014)`, prints
labelled results with units, and reads nothing from disk or network. No record,
catalogue, published parameter, spectrum or skill score is quoted anywhere; where a
real-world quantity is mentioned it is described as varying by source and to be
checked.

## Learning objectives

By the end of this module you will be able to:

1. Write the AR, MA and ARMA recursions, sketch their autocorrelation functions, and
   identify the family from the shape of the ACF.
2. Estimate AR and MA parameters from the moments, state where the equations become
   ill-conditioned, and report the estimates with standard errors.
3. Read the order of differencing from the ACF and justify it as a statement about
   stationarity rather than a fitting choice.
4. Write a linear Gaussian state-space model, run the Kalman recursion, and derive
   the steady-state gain in closed form.
5. Diagnose a state-space model without a known truth, using the likelihood and the
   coverage of the filter's own intervals.
6. Compute the per-frequency and family-wise significance levels for a periodogram
   and state which one a claim requires.
7. Measure the effect of segment averaging on both the variance of an ordinate and
   the multiplicity problem, and state the resolution it costs.
8. Compute a skill score against a named reference, derive the horizon at which a
   reference stops being useful, and report interval calibration beside accuracy.
9. Fit a conditional rate model to an event catalogue, measure the dispersion of
   the counts, and convert a rate into a window probability as a separate, stated
   assumption.

## Prerequisites

- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../01-statistics-in-practice/03-resampling.md) —
  the ensembles and bootstrap units used for every uncertainty in this module.
- [21-01-04 Linear, Multiple and Robust Regression](../01-statistics-in-practice/04-regression.md) —
  the estimation vocabulary used for time-series parameters.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md) —
  stationarity, autocorrelation and the integrated correlation time.
- [20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper](../../20-signal-processing/02-fourier-and-spectral-analysis/02-spectral-estimation.md) —
  the estimators whose statistics lesson 03 quantifies.
- [20-08-01 Detrending and Deseasonalising](../../20-signal-processing/08-timeseries-analysis-geophysics/01-detrending-seasonality.md) —
  what must precede a stationary model.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](../06-ml-in-geophysics/09-ml-pitfalls-geophysics.md) —
  the trending-series trap that differenceing exists to fix.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [AR, MA, ARIMA and Their Interpretation](01-arima-models.md) | research | Yule-Walker recovers $\varphi = 0.7106$ against $0.70$; the MA has two roots and the invertible one is a convention |
| 02 | [State-Space Models and Kalman Filtering](02-state-space.md) | research | A gain of $0.1318$ cuts the error from $0.9792$ to $0.3757$; $q$ wrong by $100\times$ doubles it |
| 03 | [Statistical Spectral Analysis and Significance Testing](03-spectral-analysis-statistical.md) | research | One level, two meanings: $0.030$ false alarms at a chosen frequency, $1.000$ at the largest peak |
| 04 | [Forecast Evaluation, Skill Scores and Calibration](04-forecast-evaluation.md) | research | Persistence beats climatology for $h \le 3$ and loses from $h = 4$; a bias leaves the widths identical and cuts coverage to $0.669$ |
| 05 | [Point Processes and Seismicity Rate Models](05-point-processes.md) | research | One catalogue, two 30-day forecasts: $1.126$ events from the mean rate, $40.770$ conditional on the mainshock |

## Suggested path

**If you are new to time series:** lessons 01, 02 and 04, in that order. Lesson 01
supplies the processes, lesson 02 the state-space view, and lesson 04 the only
reason to build either — a verifiable forecast.

**If you analyse spectra:** go straight to lesson 03, then read lesson 01 §3 for the
autocovariance it tests and lesson 04 §4 for the calibration vocabulary that its
detection claims need.

**If your data are event times:** lesson 05, preceded by lesson 04 for the
verification framework, and followed by
[06-11-02](../../06-seismology/11-earthquake-statistics-and-hazard/02-aftershocks.md)
for the seismological context.

**If you are preparing a research project:** lesson 04 plus the ★★★ exercises of
every lesson; each specifies an experiment with the sizing needed to resolve the
effect being claimed, which is the part most often missing from a study design.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-arima-models.md`](01-arima-models.md) | Lesson 01 — AR, MA and ARMA |
| [`02-state-space.md`](02-state-space.md) | Lesson 02 — state space and Kalman filtering |
| [`03-spectral-analysis-statistical.md`](03-spectral-analysis-statistical.md) | Lesson 03 — spectral significance |
| [`04-forecast-evaluation.md`](04-forecast-evaluation.md) | Lesson 04 — skill scores and calibration |
| [`05-point-processes.md`](05-point-processes.md) | Lesson 05 — point processes and rates |
| [`exercises/`](exercises) | Graded exercises and worked solutions for all five lessons |
| [`code/`](code) | Five runnable demonstrations, one per lesson |

| Script | What it prints |
|---|---|
| [`code/arima_models_demo.py`](code/arima_models_demo.py) | Five sample autocorrelations per family against theory, moment estimates with both roots, one-step-ahead MSE, and the random-walk differencing check |
| [`code/state_space_demo.py`](code/state_space_demo.py) | Filter recursions, RMSE against three estimators, steady-state gain, likelihood, interval coverage, and two mis-specified cases |
| [`code/spectral_analysis_statistical_demo.py`](code/spectral_analysis_statistical_demo.py) | Per-frequency versus maximum false-alarm rates, the empirical percentile of the maximum, and the segment-averaging comparison |
| [`code/forecast_evaluation_demo.py`](code/forecast_evaluation_demo.py) | RMSE, MAE, bias, skill and correlation for four forecasts at six horizons, plus interval coverage and width |
| [`code/point_processes_demo.py`](code/point_processes_demo.py) | Background and aftershock counts, dispersion index, two 30-day forecasts with probabilities, and the Omori fit with its standard error |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and pandas:

```bash
cd 21-statistics-bayesian-ml/07-time-series-and-forecasting/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python arima_models_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python state_space_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spectral_analysis_statistical_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python forecast_evaluation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python point_processes_demo.py
```

Every demonstration is print-only: no plots, no files, no network. Each seeds
`np.random.default_rng(20261014)`, prints labelled results with units under a
numbered-section banner, prints a `SYNTHETIC` provenance line, and exits 0. The
slowest is `spectral_analysis_statistical_demo.py` at about 0.7 s; the rest take
under 0.1 s.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A colleague reports four results from one 512-sample geophysical series.
> **(a)** They fit an AR(1) and an ARMA(1,1) and quote the ARMA $\theta$ to two
> decimals with no interval; state what you would ask for and why the same
> estimator's error is three to eight times larger on a 200-sample record.
> **(b)** They report a "highly significant" spectral peak found by scanning the
> band, with a nominal $p = 0.001$; compute the level they should have used for a
> 512-sample record and state whether the peak survives. **(c)** They filter the
> series with a Kalman filter tuned by choosing the $q$ that minimises the error
> against a spline they trust; state why that criterion is not admissible and what
> to use instead. **(d)** They verify a forecast with a correlation of 0.80 and
> claim skill; explain why three different forecasts in this module share that
> correlation exactly, and state the two columns you would add to the table.
>
> Worked versions of (a)–(d) appear in the ★★★ exercises of lessons 01, 03, 02 and
> 04 respectively.

## Common pitfalls across this module

1. **Reading a slowly decaying ACF as memory.** A random walk's $\rho_1 = 0.996$ is
   non-stationarity; one difference renders it white (measured $\rho_1 = 0.005$).
2. **Reporting time-series parameters without standard errors.** The ARMA moment
   errors rise from $+0.0024$ and $+0.0098$ at $n = 4000$ to $-0.0327$ and
   $+0.0798$ at $n = 200$.
3. **Applying a per-frequency significance level to the largest peak.** Measured
   false-alarm rate $1.000$ against a nominal $0.05$.
4. **Believing averaging solves multiplicity.** Segment averaging halves the
   ordinate scatter and still leaves $0.963$ of records with a spurious maximum at
   the per-frequency level.
5. **Quoting an RMSE, a skill score or a coverage without its reference,
   horizon or nominal level.** The same three forecasts swap places between $h = 1$
   and $h = 10$; a $1.5$ K bias leaves widths identical and drops 80% coverage from
   $0.802$ to $0.669$.
6. **Assuming Poisson for event counts.** The measured dispersion index is $3.708$,
   and the long-run rate understates a post-mainshock forecast by a factor of $36$.

## Related modules

- [21-01 Statistics in Geophysical Practice](../01-statistics-in-practice/README.md) —
  the estimation, resampling and extreme-value machinery this module applies.
- [21-03 Bayesian Inference](../03-bayesian-inference/README.md) —
  the posterior view of a state-space model and its parameters.
- [21-06 Machine Learning in Geophysics](../06-ml-in-geophysics/README.md) —
  the learning-based forecasts that these models benchmark against.
- [20-08 Time-Series Analysis in Geophysics](../../20-signal-processing/08-timeseries-analysis-geophysics/README.md) —
  the detrending, tidal and change-point methods that precede this module.
- [16-atmosphere-climate](../../16-atmosphere-climate/README.md) —
  the verification and downscaling practice of lesson 04 in its home setting.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md) —
  the seismicity-rate models of lesson 05.
