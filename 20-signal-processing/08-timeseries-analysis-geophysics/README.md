# Module 20-08 — Time-Series Analysis in Geophysics

**Stages:** graduate → research · **Prerequisites:** modules 20-02 and 20-05;
basic regression and probability.

This module is about records that are long in time and short in information. A
geophysical series of a few thousand samples looks like an embarrassment of data
and behaves like a handful of independent numbers: autocorrelation inflates every
standard error, a trend is a model statement rather than a measurement, and two
different noise models turn the same velocity into a 138-sigma result or an
8.8-sigma one. Each lesson here measures that inflation rather than asserting it,
because the numbers that matter — how much a standard error is wrong, how often a
peak search fires by chance, how many change points a ramp looks like — are
properties of a model and can be brought into the open.

The module's organising question is the one every lesson's assumptions section
answers: **which part of this analysis is the Earth and which part is my model of
it?** The trend, the seasonal cycle, the tidal constituent set, the offsets, the
noise colour and the change-point penalty are all models. Each one is stated,
each one is measured against a synthetic truth where a truth exists, and each one
is shown failing in a controlled experiment: a trend fitted to a random walk, a
semidiurnal constituent fitted to daily data, an oscillation that clears a
white-noise null and not a red-noise one.

The module ends at the frontier rather than at a method. Lessons 04 and 05 are
about the two ways that searching over many hypotheses — epochs and frequencies —
inflates false positives, and both land on the same remedy: state the error rate
you want, calibrate the threshold that achieves it on your own null, and report
the threshold with the result.

All models and data in this module are **SYNTHETIC**. No real station, gauge,
catalogue, climate index or published number is used.

## Learning objectives

By the end of this module you will be able to:

1. **Decompose** a geophysical series into trend, seasonal and irregular
   components, and **state** which of the three is the most model-dependent.
2. **Measure** the bias introduced by omitting a seasonal term and **show** how
   it scales with record length.
3. **Analyse** a tidal record by harmonic least squares, **compute** Rayleigh
   separation times and **compute** the alias of any constituent for any sampling
   interval.
4. **Distinguish** a fit residual from an out-of-sample prediction error, and
   **justify** a record length with the latter.
5. **Generate** and **identify** power-law noise, and **quantify** how a
   white-noise covariance misstates the uncertainty of a trend.
6. **Model** offsets explicitly and **measure** the trend bias caused by omitting
   one.
7. **Solve** a change-point problem exactly, and **choose** the penalty from a
   measured per-series false-positive rate.
8. **Detect** when a gradual change has been misrepresented as a sequence of
   abrupt ones, and **state** how to tell the difference.
9. **Compute** effective sample size under autocorrelation and **adjust** a
   standard error accordingly.
10. **Test** a spectral peak against a red-noise null, and **correct** the
    threshold for the number of frequencies searched.
11. **Derive** empirical orthogonal functions from an SVD and **report** their
    explained variance with the sampling error that a second realisation would
    produce.
12. **Identify**, in any time-series result, which numbers are measured, which
    are modelled and which are chosen, and **write** the analysis so a reader can
    tell.

## Prerequisites

- [20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper](../02-fourier-and-spectral-analysis/02-spectral-estimation.md)
  — frequencies, resolution and the bias–variance trade.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../05-noise-and-random-signals/01-stochastic-processes.md)
  — the formal meaning of stationarity, which every lesson here tests.
- [20-05-03 Colour of Noise: White, Pink, Red and Geophysical Examples](../05-noise-and-random-signals/03-noise-colour.md)
  — spectral index and the language of coloured noise.
- [21-01-03 Resampling](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md)
  — the machinery for calibrating a threshold against a measured error rate.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Detrending, Deseasonalising and Anomalies](01-detrending-seasonality.md) | graduate | A seasonal term left in a trend is a bias of −6.1 mm/yr at 3 years; a white-noise $t$-test passes 93 % of random walks |
| 02 | [Tidal Harmonic Analysis and Prediction](02-spectral-analysis-tides.md) | doctoral | The frequencies are astronomy; the record length decides separability, and daily sampling destroys the semidiurnal band |
| 03 | [Geodetic Time Series: Trends, Offsets, Noise Models](03-geodetic-time-series.md) | research | The noise colour sets the uncertainty, not the data volume: 10.5× and 21× understatement measured |
| 04 | [Change-Point Detection and Regime Shifts](04-change-point-and-detection.md) | research | The penalty is an error rate; a ramp is four steps if you ask a step detector |
| 05 | [Climate Time-Series Analysis and Modes of Variability](05-climate-timeseries.md) | research | Every red-noise series produces a "significant" peak; the null is the result |

## Suggested path

**If you are new to time-series analysis:** lessons 01 and 03 in order, running
each demonstration. Lesson 03 is where the standard-error arithmetic becomes a
practical skill.

**If you work with tidal or sea-level data:** 02 in full, then 01 §3–§4 for the
seasonal machinery that the same design matrix provides.

**If you are preparing a research project:** 03 §3–§5, 04 §3 and 05 §2–§3, plus
the ★★★ exercises. Those sections are about the error rates a paper has to
declare.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-detrending-seasonality.md`](01-detrending-seasonality.md) | Lesson 01 |
| [`02-spectral-analysis-tides.md`](02-spectral-analysis-tides.md) | Lesson 02 |
| [`03-geodetic-time-series.md`](03-geodetic-time-series.md) | Lesson 03 |
| [`04-change-point-and-detection.md`](04-change-point-and-detection.md) | Lesson 04 |
| [`05-climate-timeseries.md`](05-climate-timeseries.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 20-signal-processing/08-timeseries-analysis-geophysics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python detrending_seasonality_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tidal_harmonics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geodetic_timeseries_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python change_point_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_timeseries_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access and exits 0.

## Mastery checkpoint

Complete this without notes:

> A 40-year monthly series of a groundwater level is offered to you, and you are
> asked for the trend and its uncertainty. **(a)** Write the model you would fit,
> labelling each parameter as measured, nuisance or assumed, and state the value
> you would need for the seasonal terms and the offsets. **(b)** The residual
> lag-1 autocorrelation is 0.55. Compute $n_{\text{eff}}$ and explain what you
> would do to the trend uncertainty. **(c)** State the two statistics you would
> compute to decide whether the noise is flicker or a random walk, and why the
> first alone is insufficient. **(d)** A colleague reports a "significant step"
> in 1998 with no penalty stated. State the two questions you would ask and the
> numbers you would require. **(e)** For each number in (a)–(d), label it as
> **measured**, **modelled** or **chosen**.

A worked version of (a)–(c) appears in the lesson-03
[solutions](exercises/03-geodetic-time-series-solutions.md).

## Common pitfalls across this module

1. **Fitting a line to raw monthly data.** The seasonal bias is the largest error
   term at short record lengths, and it has a sign.
2. **Quoting a standard error that assumes independent samples.** Every
   uncertainty in this module is inflated by autocorrelation, measured at up to
   21× for a random walk.
3. **Judging a model by its fit residual.** The tidal demonstration's residual
   was identical for a 7-day and a 60-day record; the prediction error differed
   by a factor of 8.
4. **Reading a spectral peak against a flat null.** 22 bins cleared the
   white-noise level and the injected oscillation did not clear the red-noise
   level.
5. **Reporting a change point without its penalty.** $K$ is not a property of the
   process.
6. **Treating an unmodelled offset as noise.** It is a bias in every parameter
   the design shares with it, and two offsets can cancel and hide it.
7. **Assuming a noise colour.** It is cheap to measure and it changes the
   answer by an order of magnitude.

## Related modules

- [20-02 Fourier and Spectral Analysis](../02-fourier-and-spectral-analysis/README.md)
  — the spectral estimates whose significance this module calibrates.
- [20-05 Noise and Random Signals](../05-noise-and-random-signals/README.md) —
  the stochastic-process language used throughout, and the Wiener–Khinchin
  relation behind the power-law noise of lesson 03.
- [21-07 Time-Series Modelling and Forecasting](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/README.md)
  — the statistical treatment of the same problems, including state-space
  formulations and forecast evaluation.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md)
  — where the same counting and declustering logic meets a catalogue instead of a
  gauge.
