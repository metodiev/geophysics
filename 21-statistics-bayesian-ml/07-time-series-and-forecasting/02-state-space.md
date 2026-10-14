---
id: 21-07-02
title: "State-Space Models and Kalman Filtering"
level: research
prereqs: ["21-07-01", "21-01-02", "20-05-01"]
estimated_minutes: 60
tags: [time-series, state-space, kalman-filter, filtering, teaching]
---

# State-Space Models and Kalman Filtering

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a linear Gaussian state-space model as a pair of equations and
   **identify** which quantity is a state, which is an observation and which is a
   nuisance.
2. **Derive** the Kalman recursion — prediction, gain, update — and **state** what
   each step asserts about the state and the observation.
3. **Compute** the steady-state gain in closed form for a local-level model and
   **interpret** it as the model's statement about signal-to-noise ratio.
4. **Measure** the filtered error against the raw measurement error and the
   sample mean, and **state** which regime each estimator suits.
5. **Interpret** the filter's likelihood and the calibration of its own intervals
   as the two diagnostics available when the truth is unknown.
6. **Diagnose** a mis-specified state variance from the gain, the error and the
   likelihood, and **explain** why the likelihood is the only one available in
   practice.
7. **Specify** the report of a state-space model: the equations, the variances
   with their estimation method, the initial condition and its treatment, the
   diagnostics, and the interval calibration.

Every state, observation and error below is **SYNTHETIC**, produced by
[`code/state_space_demo.py`](./code/state_space_demo.py). No recording, instrument
noise level or estimated gain is read or quoted.

## Prerequisites

- [21-07-01 AR, MA, ARIMA and Their Interpretation](./01-arima-models.md) —
  the same processes written as recursions in the observations.
- [21-01-02 Choosing Probability Models for Earth Data](../../21-statistics-bayesian-ml/01-statistics-in-practice/02-probability-models-earth.md) —
  the Gaussian conditioning used in the recursion.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md) —
  what a random walk's growing variance means.
- [21-03-01 The Bayesian Paradigm and Subjective Probability](../../21-statistics-bayesian-ml/03-bayesian-inference/01-bayesian-paradigm.md) —
  the filter as recursive Bayes.

## 1. Intuition: separate the thing you want from the thing you measured

An observation $y_t$ is rarely the quantity of interest. A campaign measures a
distance *with an instrument that has its own noise*; an airgun shot measures a
travel time *that includes a statics term that drifts between shots*; a GPS
position measures a displacement *composed with multipath and clock error*. The
state-space formulation makes the separation explicit:

$$x_t = \varphi\,x_{t-1} + \eta_t \quad\text{(state, unobserved)}, \qquad
y_t = x_t + \varepsilon_t \quad\text{(observation)} .$$

The gain $K_t$ is the answer to "how much of this new number should I believe?" and
it changes with the model, not with the data. If the state moves a lot relative to
the measurement error, the filter follows the data; if the state is nearly
constant, the filter averages. The whole of this lesson is the arithmetic of that
sentence.

## 2. The local-level model and the recursion

The demonstration uses the **local level** (random-walk state, noise-added
observation):

$$x_t = x_{t-1} + \eta_t, \quad \eta_t \sim \mathcal N(0, q), \qquad
y_t = x_t + \varepsilon_t, \quad \varepsilon_t \sim \mathcal N(0, r),$$

with $q = 0.020\ (\text{unit})^2$ per epoch, $r = 1.000\ (\text{unit})^2$ and a
diffuse initial condition $P_0 = 10\ (\text{unit})^2$ over $n = 1000$ epochs.

The recursion, per epoch:

$$x_t^- = x_{t-1}^{+}, \qquad P_t^- = P_{t-1}^{+} + q,$$

$$K_t = \frac{P_t^-}{P_t^- + r}, \qquad
x_t^{+} = x_t^- + K_t\left(y_t - x_t^-\right), \qquad
P_t^{+} = (1 - K_t)P_t^-.$$

Each line is a claim. The prediction step says the state does not change on
average and its uncertainty grows by $q$. The gain line says the fraction of the
innovation $y_t - x_t^-$ to accept is the state uncertainty divided by the total
uncertainty of the innovation. The update shrinks the variance by $1 - K$.

For this model the filter also contributes a likelihood, accumulated as

$$-2\log L = \sum_t\left[\log 2\pi S_t + \frac{(y_t - x_t^-)^2}{S_t}\right],
\qquad S_t = P_t^- + r,$$

which is what makes $q$ and $r$ estimable in practice: they are the parameters
that maximise this sum.

## 3. Measured error

| Estimator | RMSE against the truth | Notes |
|---|---|---|
| raw measurement | $0.9792$ | the generator's observation standard deviation is $1.000$ |
| Kalman-filtered state | $0.3757$ | a $0.616$ reduction relative to the raw data |
| sample mean of the series | $1.4565$ | a constant cannot track a random walk |

The order of the three numbers is the whole point. The state is a random walk whose
variance grows as $qt$, reaching $20\ (\text{unit})^2$ — a standard deviation of
$4.5$ unit — by the last epoch. So:

- a **constant** estimate (the sample mean) becomes progressively wrong as the
  walk departs its initial value, and its error grows without bound with the record
  length;
- the **raw measurement** is unbiased at every epoch but carries the full
  observation noise;
- the **filter** is the only one of the three that is both unbiased and
  low-variance, and it achieves both by trading a little lag for a lot of noise
  removal.

That trade is visible in the gain, and it is why the model, not the data, sets the
balance.

## 4. The steady-state gain

As $t$ grows, $P_t$ converges and so does the gain. Setting $P^- = P^{+} + q$ and
$K = P^-/(P^-+r)$ and eliminating $P$ gives the quadratic

$$K^2 r - K q - q = 0
\;\Longrightarrow\;
K_{\mathrm{ss}} = \frac{-q + \sqrt{q^2 + 4qr}}{2r}
= 0.1318 \quad\text{for } q/r = 0.02.$$

Measured: the gain at the last epoch is $0.1318$ — the closed form to four
decimals — and at the first epoch, with $P_0 = 10$, it is $0.9093$. The filter
*starts* by trusting the data and *converges* to trusting its model, which is
exactly what a diffuse prior implies and exactly what a reader needs to know when
the first few epochs of a filtered series are quoted.

Interpretation: a gain of $0.13$ says the model believes about one seventh of each
innovation is signal and six sevenths is noise. A gain near 1 is a filter that
copies the data (no smoothing); a gain near 0 is a filter that ignores it (no
tracking). The steady-state gain is therefore a compact summary of the
signal-to-noise ratio, and it is *dimensionless*, which is why it can be compared
across instruments where $q$ and $r$ cannot.

## 5. Diagnostics when there is no truth

The demonstration can measure RMSE against the truth because it generated the
state. A real application has two other tools:

1. **The likelihood.** Measured at the true parameters here: $-1473.2$. The
   likelihood is a function of $(q, r)$ alone, so it can be maximised, compared
   across models, and used to test a hypothesis about the state's variability.
2. **The calibration of the filter's own intervals.** The recursion produces
   $P_t^{+}$, hence a predicted interval for $x_t$: the measured coverage of the
   filter's nominal 95% interval is $0.9410$ against a nominal $0.95$, which is a
   direct check that the model's uncertainty statement is honest. A filter whose
   intervals cover 60% of the truth is mis-specified regardless of how small its
   RMSE looks.

Add to these the residual diagnostics: the normalised innovations
$(y_t - x_t^-)/\sqrt{S_t}$ should be white and standard normal, and a
systematic pattern in them — a run of one sign, a seasonal swing — is a
mis-specified state equation.

## 6. Mis-specified state variance, measured

| Case | $q$ used | final gain | RMSE | log-likelihood |
|---|---|---|---|---|
| correct | $0.02000$ | $0.1318$ | $0.3757$ | $-1473.2$ |
| $q$ 100× too large | $2.00000$ | $0.7321$ | $0.7488$ | $-1781.6$ |
| $q$ 100× too small | $0.00020$ | $0.0140$ | $0.7694$ | $-1675.5$ |

Three readings:

1. **Both mis-specifications are worse than the correct model, and by similar
   amounts in RMSE** ($0.7488$ and $0.7694$ against $0.3757$) — a factor of two.
   The error is not a small perturbation of a robust method.
2. **They fail in opposite directions.** Too large a $q$ raises the gain to
   $0.73$: the filter passes most of the measurement noise through and its error
   climbs towards the raw measurement error. Too small a $q$ drops the gain to
   $0.014$: the filter is stiff, removes the noise, and lags the state, so its
   error grows with the walk.
3. **The likelihood separates them from the truth and from each other**, and it
   is the only one of the three columns available in practice: $-1473$ for the
   correct model against $-1782$ and $-1676$. Note the ordering is not the same as
   the RMSE ordering — the too-small-$q$ filter scores better than the
   too-large-$q$ one, while their RMSEs are nearly equal — which is why a single
   diagnostic is never enough.

The RMSE here is *optimistic about the choice under consideration* if it is used
to select $q$: selecting $q$ to minimise the error against a truth you do not have
is impossible, and selecting it to minimise the in-sample residual is not the same
problem. The likelihood is the honest surrogate, and the interval calibration is
its check.

## 7. Assumptions and regime of validity

1. **Linearity and Gaussian errors.** Both are needed for the closed-form
   recursion; a nonlinear observation operator or heavy-tailed noise requires an
   extended or unscented filter, or a particle filter, with no closed form.
2. **$q$ and $r$ are known or estimated.** §6 shows the cost of getting them
   wrong; they are estimated by maximising the likelihood, and their own
   uncertainty should be reported.
3. **The state equation is correct.** The local level assumes no trend, no
   seasonality and no external input; a series with a real trend needs a local
   linear trend (a two-dimensional state) or a regression term.
4. **Independence across epochs** of $\eta_t$ and $\varepsilon_t$, and
   independence between them. Correlated observation errors — the normal case for
   a filtered instrument — violate this and make the filter over-confident.
5. **The initial condition is handled deliberately.** $P_0 = 10$ here is diffuse
   relative to $r = 1$; a small $P_0$ biases the first epochs, and a truly diffuse
   prior requires a modified recursion or the first observations discarded.

## The honest summary

On a $1000$-epoch synthetic local-level model with $q/r = 0.02$, the Kalman filter
reduces the error against the truth from $0.9792$ (the raw measurement) to
$0.3757$, a reduction of $0.616$, while the sample mean is worse than the raw data
at $1.4565$ because a constant cannot track a random walk. The steady-state gain
of $0.1318$ matches the closed form $(-q+\sqrt{q^2+4qr})/2r$, the gain starts at
$0.9093$ under a diffuse prior, the likelihood at the true parameters is
$-1473.2$ and the filter's own 95% interval covers $0.9410$ of the truth. A state
variance wrong by a factor of 100 doubles the error, in one direction by copying
the data and in the other by lagging it, and the likelihood separates all three
cases where the error cannot. The transferable conclusions: the gain is the
model's signal-to-noise statement; the likelihood and the interval coverage are
the diagnostics that survive without a truth; and $q$ and $r$ are model
parameters, not settings.

## Python demonstration

[`code/state_space_demo.py`](./code/state_space_demo.py) prints every number quoted
above. It:

1. generates the state and the observations and prints the model, the
   signal-to-noise ratio and the state variance at the last epoch;
2. runs the filter and prints the RMSE of the raw measurement, the filtered state
   and the sample mean, with the fractional improvement;
3. prints the exact steady-state gain, the empirical final and first gains, the
   likelihood and the measured coverage of the filter's nominal 95% interval;
4. re-runs the filter with $q$ wrong by a factor of 100 in each direction and
   prints the gain, the RMSE and the likelihood for both, then a `SYNTHETIC` line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/07-time-series-and-forecasting/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python state_space_demo.py
```

It runs in under 0.1 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/02-state-space-exercises.md`](./exercises/02-state-space-exercises.md)
and [`exercises/02-state-space-solutions.md`](./exercises/02-state-space-solutions.md).

## Mastery checkpoint

Without notes:

1. Derive $K_{\mathrm{ss}} = (-q+\sqrt{q^2+4qr})/(2r)$ and evaluate it at
   $q/r = 0.02$ and at $q/r = 1$.
2. Explain in two sentences why the sample mean is worse than the raw measurement
   here, using the measured $1.4565$ and $0.9792$.
3. The gain at the first epoch is $0.9093$ and at the last is $0.1318$. State why
   this is a property of $P_0$ rather than of the data, and what to do about it.
4. Both mis-specified filters have RMSE near $0.75$ and likelihoods that differ by
   $106$. Explain why the likelihood is the usable diagnostic, and what its
   ranking implies about the two kinds of error.

## Common pitfalls

1. **Quoting a filtered series without its gain or its variances.** $q$ and $r$
   are the model; the filter is arithmetic.
2. **Assuming the filter beats the data whatever the parameters.** Both
   mis-specified cases are twice as bad as the correct one.
3. **Ignoring the initial condition.** The first epochs are dominated by $P_0$;
   the measured first gain is $0.9093$ against a steady state of $0.1318$.
4. **Using the RMSE to choose $q$.** The truth is unavailable; the likelihood is
   the admissible criterion, and its optimum is not the RMSE optimum.
5. **Treating a low RMSE as proof of honesty.** The interval coverage is the
   separate claim, and it is $0.9410$ against a nominal $0.95$ here.
6. **Over-differencing instead of modelling.** A local level is the state-space
   form of a first difference; combining both double-differences the signal.

## Where this is used

- **Geodetic time series**, where a local level or local linear trend separates
  instrument noise from real deformation
  ([20-08-03](../../20-signal-processing/08-timeseries-analysis-geophysics/03-geodetic-time-series.md)).
- **Inertial and multi-sensor navigation**, where the state-space form fuses
  observations of different types.
- **Reservoir and hydrological monitoring**, where a slowly varying level is
  observed with an uncertain rating curve.
- **Seismic statics and clock-drift correction**, where the nuisance is a smooth
  wander common to many records.
- **Data assimilation in Earth system models**, where the same recursion appears
  with a very large state vector.

## Related lessons

- [21-07-01 AR, MA, ARIMA and Their Interpretation](./01-arima-models.md) —
  the same local level is an ARIMA(0,1,1) with a constrained parameter.
- [21-07-04 Forecast Evaluation, Skill Scores and Calibration](./04-forecast-evaluation.md) —
  how the filter's predictive intervals are scored.
- [21-07-05 Point Processes and Seismicity Rate Models](./05-point-processes.md) —
  the counting-process analogue of a hidden state.
- [21-03-06 Bayesian Workflow and Principled Model Building](../../21-statistics-bayesian-ml/03-bayesian-inference/06-bayesian-workflow.md) —
  the priors and model checking that a state-space fit inherits.
- [20-08-04 Change-Point Detection and Abrupt Change](../../20-signal-processing/08-timeseries-analysis-geophysics/04-change-point-and-detection.md) —
  the diagnostic for the innovation runs the filter reports.

## Self-assessment checklist

- [ ] I can write a linear Gaussian state-space model and name its parts.
- [ ] I can run the recursion by hand for two epochs.
- [ ] I can derive and evaluate the steady-state gain.
- [ ] I can explain the mean-versus-measurement-versus-filter comparison.
- [ ] I can name the two diagnostics available without a truth.
- [ ] I can list the five items a state-space report must contain.
