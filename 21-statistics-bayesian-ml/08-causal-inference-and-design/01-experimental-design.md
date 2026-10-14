---
id: 21-08-01
title: "Experimental and Survey Design for Earth Studies"
level: research
prereqs: ["21-01-04", "21-07-04", "20-08-03"]
estimated_minutes: 60
tags: [experimental-design, survey-design, power, aliasing, teaching]
---

# Experimental and Survey Design for Earth Studies

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the standard error of a fitted linear trend as
   $\sigma/\sqrt{\sum(t_i-\bar t)^2}$ and **state** that only the spread of the
   sampling times enters it.
2. **Compare** sampling designs by their precision, **compute** the efficiency
   ratio, and **express** it as the factor by which the required sample size
   changes.
3. **Compute** the sample size needed for a stated power and effect size, and
   **state** the four quantities the calculation requires.
4. **Distinguish** a design that is inefficient from one that is biased, and
   **diagnose** aliasing as a third failure mode.
5. **Explain** why a seasonal cycle sampled at its own period is unidentifiable,
   and **state** what it does and does not do to a trend estimate.
6. **Design** a campaign that trades visits, instruments and duration against one
   another, and **report** the design with its precision rather than with its
   point estimate alone.
7. **Specify** a design report: the target quantity, the measurement model and its
   scatter, the sampling geometry, the power calculation, the aliasing analysis,
   and the confounders the design does not address.

Every number below is **SYNTHETIC**, produced by
[`code/experimental_design_demo.py`](./code/experimental_design_demo.py). No
monument, network, instrument specification or published rate is used.

## Prerequisites

- [21-01-04 Linear, Multiple and Robust Regression](../../21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md) —
  the estimator whose precision the design controls.
- [21-07-04 Forecast Evaluation, Skill Scores and Calibration](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/04-forecast-evaluation.md) —
  the view that a number is meaningless without its precision.
- [20-08-03 Geodetic Time Series](../../20-signal-processing/08-timeseries-analysis-geophysics/03-geodetic-time-series.md) —
  the trends, steps and seasonal signals a geodetic campaign must resolve.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  the uncertainty machinery used when the design is irregular.

## 1. Intuition: the design is a term in the error budget

A measurement campaign is usually planned around logistics — where the
instruments are, when the crew is free — and then analysed as if the geometry
were neutral. It is not. For the simplest useful problem, a linear trend with
independent measurement scatter $\sigma$,

$$\hat\beta = \frac{\sum_i (t_i-\bar t)(y_i-\bar y)}{\sum_i (t_i-\bar t)^2},
\qquad
\operatorname{se}(\hat\beta) = \frac{\sigma}{\sqrt{\sum_i (t_i-\bar t)^2}} ,$$

so the design enters only through $\sum_i(t_i-\bar t)^2$ — the **spread of the
sampling times**. Three consequences follow immediately:

- concentrating sampling in a short interval destroys the lever arm and inflates
  the slope's error, however many observations are taken;
- the number of observations matters only through that sum, so $n$ points placed
  at the extremes beat $3n$ points clustered in the middle;
- the noise $\sigma$ and the design multiply, so a factor of two in either is
  worth a factor of four in sample size.

The demonstration measures these statements on four sampling geometries, and the
spread of the resulting sample-size requirements is a factor of $67$ — much larger
than the differences most studies argue about.

## 2. The synthetic problem

| Property | Value |
|---|---|
| measurement scatter | $5.0$ mm (1 s.d.) |
| true rate | $1.0$ mm/yr |
| seasonal signal | $3.0$ mm amplitude, $12$-month period |
| interval | $5.0$ years |
| points per campaign design | $24$ |
| detection target | 80% power, two-sided 5% level, for a rate of $1.0$ mm/yr |

The power factor is $z_{1-\alpha/2} + z_{1-\beta} = 1.959964 + 0.841621 = 2.8016$,
so the design requirement is

$$\frac{\sigma}{\mathrm{sd}(t)\sqrt{n}} \le \frac{\beta_{\text{target}}}{2.8016}
\;\Longrightarrow\;
n \ge \left(\frac{2.8016\,\sigma}{\beta_{\text{target}}\,\mathrm{sd}(t)}\right)^2 .$$

## 3. Four designs, measured

| Design | $\mathrm{sd}(t)$ (yr) | $\mathrm{se}(\hat\beta)$ (mm/yr) | $n$ for power | efficiency |
|---|---|---|---|---|
| even, 24 monthly points | $1.480$ | $0.690$ | $89.6$ | $0.66$ |
| first year only, 24 points | $0.276$ | $3.699$ | $2578.1$ | $0.12$ |
| two campaigns, 12 at each end | $2.255$ | $0.453$ | $38.6$ | $1.00$ |
| three campaigns of 8 months | $1.644$ | $0.621$ | $72.6$ | $0.73$ |

Reading:

1. **The best design puts half its points at each end of the interval.** Its
   $\mathrm{sd}(t) = 2.255$ years is the largest achievable with the interval
   fixed, and the resulting $\mathrm{se}$ of $0.453$ mm/yr is $34\%$ better than
   the evenly spaced design with the same 24 points.
2. **Clustering inside one season is catastrophic.** The first-year design has
   $24$ points and an $\mathrm{se}$ $8.2$ times worse than the two-campaign
   design: the efficiency is $0.12$, so it needs $67$ times as many observations
   for the same precision. If the science question is a five-year rate, the
   first-year design cannot answer it at any plausible sample size
   ($2\,578$ points).
3. **Campaigns in the middle are only slightly worse than even spacing.**
   Three campaigns of eight consecutive months reach efficiency $0.73$ because
   their centres (0, 2 and 4 years) still span the interval; the within-campaign
   clustering costs little.
4. **The requirement spans a factor of $67$ in sample size** — from $39$ to
   $2\,578$ points — for the same estimator and the same noise. This is the single
   most useful number in the lesson: the geometry, not the arithmetic, decides
   whether the study is feasible.

The efficiency column is the ratio of the best standard error to the design's, so a
design with efficiency $0.66$ needs $1/0.66^2 = 2.3$ times the observations of the
best design; the first-year design needs $1/0.12^2 = 69$ times as many. Quoting the
ratio of standard errors and the factor in sample size together is what makes a
design comparison legible.

## 4. Aliasing: sampling at the period of the signal

The seasonal cycle is a real part of the signal and a real threat to the trend if
the sampling is chosen carelessly. Two measurements:

| Sampling | Recovered seasonal amplitude | Recovered trend | $\mathrm{se}(\hat\beta)$ |
|---|---|---|---|
| monthly, 60 epochs, seasonal term fitted | $3.802 \pm 0.934$ mm | $+0.783 \pm 0.458$ mm/yr | $0.458$ mm/yr |
| annual, 5 epochs | aliased to a constant $+1.933$ mm | $+2.042 \pm 1.581$ mm/yr | $1.581$ mm/yr |

Three readings:

1. **Monthly sampling recovers both.** The amplitude estimate $3.802 \pm 0.934$ mm
   is consistent with the generator's $3.0$ mm, and the trend
   $+0.783 \pm 0.458$ mm/yr is consistent with $1.0$ mm/yr. The broad interval is
   the demonstration's own message: a 3 mm seasonal against 5 mm scatter with 60
   epochs is *detectable but not precisely estimated*.
2. **Annual sampling aliases the seasonal term onto the intercept.** Every epoch
   has the same seasonal phase, so the seasonal contribution is a constant
   $A\sin\varphi = +1.933$ mm that the intercept absorbs. The aliased term does not
   bias the slope: the recovered $+2.042$ mm/yr is $0.66$ standard errors from the
   truth. What it costs is precision — the slope's standard error rises from
   $0.458$ to $1.581$ mm/yr, a factor of $3.45$ — and interpretability: no seasonal
   claim is possible.
3. **With a drifting phase, the aliasing biases the slope.** If the seasonal phase
   advances (a lengthening or shortening season), the "constant" becomes a slowly
   varying term that is indistinguishable from a trend. The demonstration holds
   the phase fixed precisely so that this second failure is visible as a
   possibility rather than hidden inside the numbers.

The general rule: **sample at a rate that resolves every periodic component you
are not prepared to model**, and if you do not resolve it, state that you have
folded it into the intercept — or into the trend, if its phase drifts.

## 5. What the design fixes and what it cannot

The design can:

- set the precision of a trend, a rate, or a difference between sites;
- convert a target effect size into a required sample size, before data are
  collected;
- make a periodic component identifiable or deliberately aliased.

The design cannot:

- remove a **bias** in the measurement. A monument that is unstable, an antenna
  that is remeasured higher after snowmelt, an instrument with a calibration
  scale error — none of these is helped by more points. Bias is addressed by
  measurement protocol, not by geometry.
- substitute for **randomisation** in an experiment. If a treatment (an injection,
  a change of land use, a monitoring policy) is assigned by convenience, the design
  is observational and no amount of sampling fixes the confounding — the subject
  of [21-08-02](./02-causal-inference-methods.md).
- make a sparse network dense. A design that needs 2 578 campaigns has told you the
  question requires continuous instrumentation, not more visits.

## 6. Assumptions and regime of validity

1. **Independent measurement errors of constant variance.** Real campaign scatter
   grows with the time since the last observation (a monument decays), and
   irregular designs then need weighted least squares; the $\sigma/\sqrt{\sum}$ formula
   holds only when the variance is constant.
2. **A linear trend is the right model.** A nonlinear (decelerating) deformation
   makes the slope depend on the window, and the design must then be judged on the
   parameter actually of interest.
3. **The interval is fixed by the science.** Choosing $5$ years because it is
   convenient, then reporting a rate, puts the arbitrary part of the choice into
   the answer.
4. **$z$ rather than $t$.** The power calculation uses normal quantiles; with small
   $n$ the $t$ correction inflates the requirement, which the demonstration's exact
   least-squares standard errors include and the $n$-for-power formula does not.
5. **One quantity at a time.** A design optimised for a trend is not optimal for a
   seasonal amplitude or a step; a multi-objective design must state the weights.

## The honest summary

On a synthetic five-year geodetic problem with $5.0$ mm scatter and a $3.0$ mm
seasonal signal, the standard error of the fitted rate ranges from $0.453$ mm/yr
(two campaigns at the interval's ends) to $3.699$ mm/yr (all observations in the
first year) — a design efficiency of $1.00$ against $0.12$, and a required sample
size of $39$ against $2\,578$ points for 80% power against a $1.0$ mm/yr trend.
Monthly sampling recovers the seasonal amplitude as $3.802 \pm 0.934$ mm and the
trend as $+0.783 \pm 0.458$ mm/yr; annual sampling aliases the seasonal term onto
the intercept as $+1.933$ mm, leaves the slope unbiased ($+2.042 \pm 1.581$
mm/yr, $0.66$ standard errors from the truth) and costs a factor of $3.45$ in
precision. The transferable conclusions: compute the trend standard error from the
sampling geometry before collecting data; put observations where the lever arm is;
expect a factor of tens between good and careless geometry; and remember that no
geometry repairs a biased measurement or a confounded comparison.

## Python demonstration

[`code/experimental_design_demo.py`](./code/experimental_design_demo.py) prints
every number quoted above. It:

1. prints the measurement model, the scatter, the seasonal signal and the
   detection target, and states the slope standard error formula;
2. evaluates four sampling designs and prints $\mathrm{sd}(t)$, the slope standard
   error, the sample size for 80% power and the efficiency of each;
3. fits a monthly-sampled series with an explicit seasonal term and an annual-sampled
   series, printing the recovered amplitude and trend with their standard errors,
   the aliased constant and the precision ratio;
4. prints the spread of the design efficiencies and of the sample-size requirement,
   then a `SYNTHETIC` provenance line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/08-causal-inference-and-design/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python experimental_design_demo.py
```

It runs in under 0.1 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/01-experimental-design-exercises.md`](./exercises/01-experimental-design-exercises.md)
and [`exercises/01-experimental-design-solutions.md`](./exercises/01-experimental-design-solutions.md).

## Mastery checkpoint

Without notes:

1. Derive $\operatorname{se}(\hat\beta)$ for a simple linear trend and explain why
   $\sigma$ and $\mathrm{sd}(t)$ enter symmetrically.
2. Compute the sample size for 80% power against a $0.5$ mm/yr trend with $5$ mm
   scatter and an evenly spaced five-year campaign, and state what changes if the
   interval is doubled.
3. The annual design's slope is unbiased but $3.45$ times less precise. State the
   two mechanisms and which one is absent when the seasonal phase is fixed.
4. A colleague proposes a design with excellent precision and no randomisation.
   State the claim the design can support and the claim it cannot.

## Common pitfalls

1. **Clustering observations in time and calling it replication.** 24 points in one
   year give a $3.699$ mm/yr standard error against $0.453$ for the same 24 points
   at the interval's ends.
2. **Reporting a rate without its design's precision.** The same estimator gives
   errors that span a factor of $8.2$ across the four designs here.
3. **Sampling at the period of a signal you care about.** The seasonal amplitude
   becomes a constant; the trend stays unbiased but loses a factor of $3.45$ in
   precision.
4. **Confusing precision with validity.** More points cannot fix a monument, a
   calibration or a confounder.
5. **Ignoring the survey design in the analysis.** A non-random sampling geometry
   needs weights, strata or a model of the sampling process; an unweighted mean of
   a convenience sample estimates the sample, not the population.
6. **Optimising the design for the easy parameter.** A geometry that is best for a
   long-term rate is usually poor for a seasonal amplitude or a step.

## Where this is used

- **Geodetic campaign design**, where visits are expensive and the trend's error
  is set by the campaign dates
  ([20-08-03](../../20-signal-processing/08-timeseries-analysis-geophysics/03-geodetic-time-series.md)).
- **Microseismic and induced-seismicity monitoring**, where array geometry sets the
  detection threshold and the location precision.
- **Environmental and hydrological surveys**, where sampling dates and sites are the
  design and the aliasing of a seasonal cycle is the classic failure.
- **Repeat gravity, levelling and GNSS networks**, where the network geometry and
  the epoch schedule together set the resolvable signal.
- **Any observational study of an "experiment" you did not run**, where the design
  is fixed and its consequences must be measured rather than chosen.

## Related lessons

- [21-08-02 Causal Inference Methods and Counterfactuals](./02-causal-inference-methods.md) —
  what a design without randomisation can and cannot establish.
- [21-08-03 Attribution in Climate and Hazard Science](./03-attribution-methods.md) —
  the design of a factual–counterfactual comparison.
- [21-07-01 AR, MA, ARIMA and Their Interpretation](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/01-arima-models.md) —
  the correlation that makes a campaign's points less independent than they look.
- [21-07-04 Forecast Evaluation, Skill Scores and Calibration](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/04-forecast-evaluation.md) —
  the precision discipline applied to forecasts.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  the uncertainty of an irregular design.

## Self-assessment checklist

- [ ] I can derive the trend standard error and identify the design's term.
- [ ] I can compare designs by efficiency and convert it to a sample size.
- [ ] I can compute the sample size for a stated power and effect size.
- [ ] I can diagnose aliasing and state its two effects.
- [ ] I can separate a precision problem from a bias problem.
- [ ] I can list the five items a design report must contain.
