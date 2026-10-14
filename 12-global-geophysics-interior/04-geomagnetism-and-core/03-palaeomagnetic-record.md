---
id: 12-04-03
title: "Palaeomagnetic Record and Reversal Frequency"
level: doctoral
prereqs: ["08-01-06", "12-04-02", "12-03-03"]
tags: [global-geophysics, earth-interior, palaeomagnetism, reversals, geodynamo, timescale]
---

# Palaeomagnetic Record and Reversal Frequency

**All models and data in this module are SYNTHETIC.** The polarity chronology
used below is generated from an invented rate function. It is not the geomagnetic
polarity timescale or any published chronology, and no measured reversal age,
palaeointensity, site or superchron boundary appears anywhere. Every number is
printed by
[`code/palaeomagnetic_record_demo.py`](./code/palaeomagnetic_record_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Generate** a synthetic reversal chronology from a prescribed rate function
   and **compute** the interval statistics a real record would show.
2. **Test** a reversal sequence against a Poisson model using the coefficient of
   variation, the skewness and a Kolmogorov–Smirnov statistic, and **state** what
   a non-rejection does and does not prove.
3. **Compute** the probability of a superchron under a constant rate and
   **invert** it for the rate a given gap requires.
4. **Quantify** the one-sided bias that a finite sampling resolution imposes on a
   reversal count.
5. **Test** a rate trend against a stationary null using a parametric bootstrap,
   and **report** the trend in units of the null's standard deviation.
6. **Explain** how a detection threshold in a palaeointensity database biases a
   time-averaged field estimate.
7. **State** which aspects of the reversal record constrain the core's thermal
   history and which do not.

## Prerequisites

- [08-01-06 Palaeomagnetism, Reversals and Magnetostratigraphy](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/06-palaeomagnetism.md) —
  how a reversal is recorded, Fisher statistics, virtual geomagnetic poles and the
  magnetostratigraphic method. This lesson assumes all of it.
- [02 Numerical Geodynamo Models](02-geodynamo-numerical.md) — what a model can
  and cannot predict about reversals.
- [12-03-03 Thermal Evolution and Secular Cooling](../03-geotherms-and-heat-budget/03-thermal-evolution.md) —
  the core heat flux that controls the dynamo's regime.

## 1. The record, and the three questions one can ask of it

A polarity chronology is a list of times at which the field reversed. From such a
list only three questions can be answered without additional assumptions:

- **Is the sequence consistent with a stationary random process?** If it is, the
  intervals are exponential and the reversal "rate" is the only parameter.
- **How does the rate vary with time?** This requires a test against a stationary
  null, because a fluctuating record looks like a trend to the eye.
- **Is the apparent record the true record?** A coarse sampling merges short
  intervals and therefore under-counts.

Everything else — the cause of a reversal, the state of the core at a given
time, the existence of a periodicity — requires a model. This lesson keeps that
boundary explicit, because the palaeomagnetic literature contains many claims
that crossed it silently.

## 2. A synthetic chronology and its statistics

The demonstration's adopted rate function falls linearly from 5.0 reversals per
Myr at the present to 1.0 reverse per Myr at 300 Ma, with a zero-rate window
between 120 and 160 Ma to represent a superchron. Drawing from it produces

$$\text{790 reversals over } 300\ \mathrm{Myr},\qquad
\bar{\Delta t} = 0.380\ \mathrm{Myr},\qquad
\text{median} = 0.215\ \mathrm{Myr},$$

with quantiles 0.034, 0.085, 0.215, 0.425 and 0.767 Myr at 10, 25, 50, 75 and
90%, a shortest interval of 0.0005 Myr and a longest of **40.967 Myr**.

Three observations follow immediately.

- **The mean and the median differ by a factor of 1.8.** For an exponential
  distribution the mean is $1/\lambda$ and the median is $\ln 2/\lambda$, a ratio
  of exactly 1.44 — so 1.8 is already a hint that the pooled record is not a
  single exponential. Publishing only the mean interval discards that hint.
- **The shortest interval is 0.5 kyr.** A Poisson process assigns non-zero
  probability to arbitrarily short intervals; any claim that "reversals take at
  least $X$ to complete" is a physical statement that the Poisson model does not
  contain.
- **The longest interval is the superchron itself (41.0 Myr).** One interval
  dominates the mean, which is why robust statistics matter here.

## 3. Is the sequence Poisson?

Restricting to the non-superchron intervals (which removes the deliberately
inserted gap), the demonstration measures

$$\text{CV} = 1.177,\qquad \text{skewness} = 3.054,$$

against the exponential values of **1** and **2**. The Kolmogorov–Smirnov test
against the fitted exponential gives

$$D_{KS} = 0.0433,\qquad p = 0.1006 .$$

The honest reading is subtle and worth stating carefully.

- The CV and the skewness **are** larger than the exponential values, and the
  direction of the excess is diagnostic: a mixture of exponentials with different
  rates is over-dispersed, with CV > 1 and skewness > 2. That is exactly what a
  varying rate produces.
- The KS test **does not reject** a single exponential at 5%. With roughly 750
  intervals, the test has low power against a modest rate variation: a
  non-rejection is not evidence of stationarity, it is evidence that this test on
  this record cannot tell the difference.

The lesson generalises: **in the reversal literature, a failed rejection is
frequently reported as a confirmation.** The correct statement is that the record
is consistent with a Poisson process to within the power of the test, and the
diagnostics that do move (CV, skewness, and a rate trend test in §6) are the ones
that carry information.

## 4. Superchrons: not an unusual gap, but a different process

For a stationary Poisson process of rate $\lambda$, the probability that a given
interval exceeds $G$ Myr is

$$P(\Delta t \ge G) = e^{-\lambda G}.$$

The demonstration prints

| Rate (Myr⁻¹) | $P(\ge 10)$ | $P(\ge 20)$ | $P(\ge 30)$ | $P(\ge 40)$ |
|---|---|---|---|---|
| 5.0 | $1.9\times10^{-22}$ | $3.7\times10^{-44}$ | $7.2\times10^{-66}$ | $1.4\times10^{-87}$ |
| 2.0 | $2.1\times10^{-9}$ | $4.2\times10^{-18}$ | $8.8\times10^{-27}$ | $1.8\times10^{-35}$ |

Its own 41.0-Myr gap would occur with probability $1.1\times10^{-89}$ at the
recent rate. Inverting for the rate at which a 41-Myr gap is a 5% fluctuation,

$$\lambda_{5\%} = \frac{\ln(1/0.05)}{G} = \frac{2.996}{41.0}
= 0.0731\ \mathrm{Myr^{-1}},$$

that is, a factor of **68 below** the recent rate and below even the oldest rate
in the adopted function.

The argument is decisive and worth memorising in this form: **a superchron cannot
be explained by fluctuation of a stationary process, whatever the rate; it
requires the rate itself to have changed, and by nearly two orders of
magnitude.** That is the observational basis for the claim that the geodynamo
switches between regimes, and it is why superchrons are used as constraints on
the thermal evolution of the core
([12-03-03](../03-geotherms-and-heat-budget/03-thermal-evolution.md) §6).

## 5. What a magnetostratigraphy actually sees

Sampling the synthetic record on a uniform grid and counting polarity changes
gives the observed count as a function of resolution:

| Resolution (Myr) | Reversals seen | Fraction of 790 |
|---|---|---|
| 0.05 | 682 | 0.863 |
| 0.10 | 576 | 0.729 |
| 0.25 | 400 | 0.506 |
| 0.50 | 236 | 0.299 |
| 1.00 | 116 | 0.147 |
| 2.00 | 64 | 0.081 |

The bias is **one-sided and enormous**: a 1-Myr sampling sees 15% of the
reversals. The mechanism is obvious once stated — intervals shorter than the
sampling resolution are merged into their neighbours, and no mechanism invents an
interval that is not there. The consequences are not obvious:

1. **Every coarse record under-estimates the rate**, so a rate from a poorly
   resolved section is a lower bound, not an estimate.
2. **The bias is age-dependent** wherever the true rate is, so a comparison of
   rates between two intervals measured at different resolutions (different
   sedimentation rates, different core recovery) can manufacture a trend that is
   entirely an artefact.
3. **The bias flattens the record's variability.** A record that sees 15% of the
   events still sees most of the *long* intervals, so it preserves the
   superchrons while destroying the short-interval structure — which is why
   superchrons are more robust observables than rates.

## 6. Testing a rate trend

Binning the chronology into 15 windows of 20 Myr gives the rates (Myr⁻¹) printed
by the demonstration:

$$5.10,\ 4.05,\ 4.85,\ 4.25,\ 3.95,\ 3.70,\ 0.00,\ 0.00,\ 2.85,\ 2.30,\ 2.40,\
1.60,\ 2.00,\ 1.15,\ 1.30 .$$

A least-squares fit over the non-superchron windows gives a slope of

$$-0.01371\ \mathrm{Myr^{-1}\,per\,Myr}.$$

The crucial step is the **null**. Using *stationary* Poisson sequences at the
record's mean rate (2.633 Myr⁻¹), 200 bootstrap realisations give a slope
standard deviation of 0.00105 and a $p$-value of 0.000:

$$\text{observed slope} = 13.0\ \text{standard deviations of the null}.$$

Two methodological points:

- **The null must be stationary.** An earlier version of this test drew the null
  from the same time-varying rate function and produced $p = 0.355$ — a perfectly
  correct computation that tested nothing, because the null contained the effect
  it was supposed to exclude.
- **The trend is detectable because it is large.** The adopted rate falls by a
  factor of five. A record with a 20% rate change over the same interval would
  give roughly a 4-standard-deviation trend, and a real one over a shorter or
  more sparsely sampled interval may not be detectable at all.

## 7. The time-averaged field, and the bias of a threshold

Reversal frequency is one palaeomagnetic observable; the field's past *strength*
is another. Draw 400 synthetic palaeointensities from a lognormal distribution
with median $8.0\times10^{22}\ \mathrm{A\,m^2}$ and $\sigma_{\ln} = 0.45$:

$$\bar{M}_{\text{all}} = 8.985\times10^{22}\ \mathrm{A\,m^2}.$$

Now impose a detection threshold at $3.2\times10^{22}\ \mathrm{A\,m^2}$ — which
is what every real palaeointensity determination does, since weak signals cannot
be measured reliably — and average the 391 survivors:

$$\bar{M}_{\text{kept}} = 9.125\times10^{22}\ \mathrm{A\,m^2},
\qquad\text{bias} = +1.6\%.$$

For a threshold that keeps 98% of the samples the bias is small (+1.6%), but it is
**one-sided and it grows rapidly** as the threshold rises:

| Threshold (A m²) | Kept | Mean of kept (10²² A m²) | Bias |
|---|---|---|---|
| $1.60\times10^{22}$ | 400 | 8.985 | +0.0% |
| $3.20\times10^{22}$ | 391 | 9.125 | +1.6% |
| $4.80\times10^{22}$ | 352 | 9.689 | +7.8% |
| $6.40\times10^{22}$ | 281 | 10.690 | +19.0% |

Doubling the threshold quadruples the bias. The general statement:

> **a mean of accepted results is not a mean of results, and the difference is
> system-dependent and invisible in the database.**

This is the palaeomagnetic face of a general problem: the selection function must
be modelled, not ignored, and it is the same argument that governs the
completeness of a magnitude catalogue in seismology.

## 8. What the reversal record constrains

With the statistics of §3–§7 in hand, here is a defensible list.

**Constrained by the record:**

- The **rate** of reversals over an interval, as a lower bound, with the sampling
  resolution quoted.
- The **existence and duration of superchrons**, because these are long enough to
  survive any realistic sampling.
- The **change of regime** implied by superchrons: §4 shows that a stationary
  process cannot produce one.
- The **approximate dipole strength history**, once the selection function of the
  palaeointensity database is modelled.

**Not constrained by the record:**

- **Individual reversal times** as a prediction of any model: §3 of
  [02](02-geodynamo-numerical.md) showed that a low-order model reproduces rates
  but not chronologies, and that the same parameters support metastable states.
- **A periodicity.** A rate that fluctuates on several timescales can always be
  fitted by a superposition of sinusoids, and the number of free periods grows
  with the number of windows.
- **The core's temperature at a given time** without an independent heat-flux
  model; the record constrains the *dynamo's regime*, not its energy budget.
- **The mechanism of a reversal.** The record shows what the field did, not what
  the flow did.

## 9. Assumptions and regime of validity

1. **The chronology is a point process.** Each reversal is assigned a time; the
   real record has lock-in depths, delayed acquisition and, in sediments,
   smoothing over centimetres to metres. Those effects act exactly like a coarse
   sampling (§5).
2. **The rate function is adopted.** No claim is made that the synthetic rates
   correspond to any real interval; the arithmetic is what transfers.
3. **Intervals are independent.** The tests assume it; long-range correlations in
   a real record would inflate the apparent significance of a trend.
4. **The Poisson model is the null, not the truth.** Rejecting it is informative;
   failing to reject it is weak evidence, as §3 shows.
5. **Lognormal palaeointensities are an adopted model.** Real distributions are
   skewed and, more importantly, their selection function is not a sharp
   threshold.
6. **The bootstrap null uses the record's mean rate.** A null built from a
   smoothly varying rate would be more conservative and require a stronger test
   statistic to reject.

## 10. Mastery checkpoint

Without notes:

> A synthetic polarity chronology has 500 reversals in 200 Myr, with a longest
> gap of 25 Myr. **(a)** Compute the mean interval and the mean rate.
> **(b)** Compute the probability of a 25-Myr gap under a constant rate equal to
> the mean, and state your conclusion about the process. **(c)** Compute the rate
> at which a 25-Myr gap would be a 5% fluctuation, and express it as a fraction of
> the mean rate. **(d)** Explain why a 0.5-Myr sampling resolution biases the
> count downward, and estimate the factor for a rate of 5 Myr⁻¹.
> **(e)** State one claim about the geodynamo that this chronology supports and
> one that it does not.

## 11. Common pitfalls

1. **Reporting a mean interval without the median.** For a super-Poissonian
   process they differ by more than the exponential factor of 1.44.
2. **Treating a failed Poisson test as confirmation of stationarity.** It is a
   statement about the test's power.
3. **Testing a trend against a null that contains the trend.** The bootstrap must
   be stationary, and getting this wrong is silent.
4. **Comparing rates measured at different resolutions.** The bias differs, so
   the trend is manufactured.
5. **Quoting an average palaeointensity without the selection function.** A
   +1.6% bias here becomes arbitrarily large as the threshold rises.
6. **Reading a periodicity into a fluctuating rate.** With enough windows a
   sinusoid fits anything.

## 12. Related modules

- [01 Observations of the Core Field and Secular Variation](01-core-field-observations.md) —
  the present-day field, which is one point on the record this lesson covers.
- [02 Numerical Geodynamo Models](02-geodynamo-numerical.md) — why individual
  reversal times are unpredictable and rates are not.
- [08-01 The Earth's Magnetic Field](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/README.md) —
  the palaeomagnetic method, reversals and magnetostratigraphy.
- [12-03 Geotherms and the Earth's Heat Budget](../03-geotherms-and-heat-budget/README.md) —
  the thermal evolution that a superchron constrains.
- [12-02 Composition and Mineral Physics](../02-composition-and-mineral-physics/README.md) —
  the core composition and transport properties behind the dynamo's regime.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) — the
  bootstrap, hypothesis-testing power and selection functions in general.
