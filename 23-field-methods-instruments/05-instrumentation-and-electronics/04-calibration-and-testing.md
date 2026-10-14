---
id: 23-05-04
title: "Calibration, Testing and Traceability"
level: research
prereqs: ["23-05-01", "03-13-02"]
estimated_minutes: 100
tags: [calibration, traceability, uncertainty, metrology, testing]
---

# Calibration, Testing and Traceability

## Learning objectives

By the end of this lesson you will be able to:

1. **Fit** a linear calibration to reference values, and **compute** the residuals and
   their statistics.
2. **Compute** the standard errors of the slope and the intercept from the residual
   scatter, and **state** which one a quantitative measurement inherits.
3. **Build** an uncertainty budget for a calibrated measurement, **identify** the
   dominant term, and **state** what would improve the result.
4. **Compute** a re-calibration interval from a drift rate and a tolerance, and
   **state** what must be measured to justify it.
5. **Describe** a traceability chain and the contribution of each link.
6. **Design** the acceptance tests that verify an instrument before and after a
   campaign.

All reference values, readings, uncertainties and drift rates in this lesson are
**SYNTHETIC** teaching values, combined with the standard least-squares relations
quoted in the text. No laboratory standard, manufacturer figure or measured
calibration is used or reproduced.

## Prerequisites

- [01 Sensors and Transducers: Principles and Selection](01-sensors-and-transducers.md) —
  the sensor whose sensitivity is being established.
- [03-13-02 Testing Numerical Code Against Analytic Solutions](../../03-scientific-computing/13-testing-profiling-packaging/02-testing-scientific-code.md) —
  the verification discipline this lesson applies to hardware.

## 1. Intuition: a calibration is a measurement of the instrument

A sensor's specification is a statement about a typical device under stated
conditions. A **calibration** is a measurement of *this* device under *these*
conditions, against a reference whose own uncertainty is documented. Everything else
in this lesson is the arithmetic of that comparison:

- the **calibration function** maps the raw reading to a physical value;
- the **residuals** are what the function cannot explain, and they set the
  uncertainty of the parameters;
- the **uncertainty budget** combines the fit's uncertainty with the reference's,
  the repeatability and the drift;
- **traceability** is the documented chain that makes the reference's value
  defensible;
- **testing** is how you find out whether the calibration still holds.

The idea that makes the arithmetic honest is the distinction between the **scale** and
the **offset**. A measurement's *relative* accuracy is set by the scale and is usually
what matters; the offset matters for absolute values and can move unnoticed if only
relative comparisons are made.

## 2. A five-point least-squares calibration

With reference values $y_i$ measured at raw readings $x_i$, the least-squares fit
$y = a x + b$ has

$$a = \frac{\sum (x_i - \bar x)(y_i - \bar y)}{\sum (x_i - \bar x)^{2}},
\qquad b = \bar y - a\bar x .$$

The demonstration uses five evenly spaced readings and reports

$$y = 0.099970\,x + 0.027000 ,$$

| Raw | Reference | Fitted | Residual |
|---|---|---|---|
| 100 | 10.050 | 10.0240 | +0.0260 |
| 200 | 19.980 | 20.0210 | −0.0410 |
| 300 | 30.030 | 30.0180 | +0.0120 |
| 400 | 40.010 | 40.0150 | −0.0050 |
| 500 | 50.020 | 50.0120 | +0.0080 |

with an RMS residual of **0.02276** over the five points and a residual standard
deviation of **0.02938** with $n-2 = 3$ degrees of freedom.

Two arithmetic details matter. First, the two statistics differ because the RMS
divides by $n$ and the standard deviation by $n-2$; with five points the ratio is
$\sqrt{5/3} = 1.29$, and it is the $n-2$ version that feeds the parameter
uncertainties. Using the RMS there understates the uncertainties by 29 % at five
points and by less as the count grows. Second, the residuals are *structured*
(+ − + − +): a perfect linear calibration leaves residuals with random signs, so a
systematic run of signs — or curvature — means the model is wrong, not that the
instrument is noisy. **Plot them.**

## 3. Uncertainties of the calibration parameters

The standard errors follow from the residual scatter $\hat\sigma$ and the calibration
design:

$$\mathrm{se}(a) = \frac{\hat\sigma}{\sqrt{\sum (x_i-\bar x)^{2}}}, \qquad
\mathrm{se}(b) = \hat\sigma\sqrt{\frac{1}{n} + \frac{\bar x^{2}}
{\sum (x_i-\bar x)^{2}}} .$$

The demonstration's values, with $\sum(x_i-\bar x)^{2} = 100\,000$, $n = 5$ and
$\bar x = 300$:

$$\mathrm{se}(a) = \frac{0.02938}{\sqrt{100\,000}} = 9.2916\times10^{-5}
\;\Rightarrow\; \frac{\mathrm{se}(a)}{a} = 0.0929\ \% ,$$

$$\mathrm{se}(b) = 0.02938\sqrt{0.2 + 0.9} = 0.03082 .$$

So the scale is known to **0.093 %** and the offset to **0.031 value units** at one
standard error. Three design consequences:

1. **The scale uncertainty falls as $1/\sqrt{\sum(x-\bar x)^{2}}$** — that is, by
   spreading the calibration points over a *wide range* and by using *more* points.
   A calibration confined to the middle of the range, even with many points, cannot
   constrain the scale well.
2. **The offset uncertainty is reduced by centring** the calibration points around
   the working value: $\bar x$ appears in $\mathrm{se}(b)$, so a calibration whose
   mean is far from the working range has a poorly determined offset.
3. **Beware extrapolation.** The fit's uncertainty outside the calibrated range grows
   rapidly, and the linear model itself is least likely to be valid there.

## 4. The uncertainty budget

A calibration's parameters are only one term in the measurement's uncertainty:

| Component | Value | Share of variance |
|---|---|---|
| fit residual | 0.02938 | 62.2 % |
| reference standard | 0.02000 | 28.8 % |
| repeatability of a check | 0.01000 | 7.2 % |
| drift since calibration | 0.00500 | 1.8 % |
| **total (quadrature)** | **0.03726** | 100 % |

The dominant term is the **fit residual** — the calibration's own scatter — and it is
four times more important than the reference's accuracy. The actionable conclusion:
**adding calibration points (or improving their repeatability) improves the
measurement more than obtaining a better reference**, which is the opposite of the
intuition most people bring to metrology. The reference's own uncertainty sets a
floor, but it is rarely the binding term.

Two further points. The budget must be in the *same units* as the deliverable, and if
the deliverable is a difference between two stations the offset cancels and the scale
is what propagates. Second, the quadrature sum assumes independence: the fit residual
and the check's repeatability are *not* independent, so the total is a lower bound —
correlated terms should be added linearly.

## 5. Drift and the re-calibration interval

Calibrations drift through ageing, temperature cycling, mechanical shock and
component changes. If the drift rate $r$ and the tolerance $\tau$ are known, the
re-calibration interval is

$$T_{\text{cal}} = \frac{\tau}{r} .$$

With a synthetic $r = 0.005$ value units per day and $\tau = 0.05$:

| Days since calibration | Drift | Within tolerance? |
|---|---|---|
| 1 | 0.005 | yes |
| 5 | 0.025 | yes |
| 10 | 0.050 | yes (at the limit) |
| 20 | 0.100 | no |
| 50 | 0.250 | no |

so the interval is **10 days**. Here $\tau = 0.05$ is set by the deliverable's
requirement and is deliberately *larger* than the calibration's own quadrature budget
of 0.03726: the tolerance is the biggest *change* the science accepts, while the
budget is the uncertainty of a *single* value. The interval depends on two *measured*
numbers: the tolerance, from the science requirement, and the drift rate, from the
before-and-after difference of successive calibrations.

The practical rules:

1. **Calibrate before and after every campaign** and use the difference to measure
   the drift rate; this doubles the information for a small extra cost.
2. **Check a working standard** in every calibration session, so that a change in the
   reference (rather than in the device) is detected.
3. **Record the interval and the environment** with every calibration: drift rates
   are environment-dependent.
4. **Do not extend the interval because nothing has gone wrong** — absence of
   evidence is not evidence of stability.

## 6. Traceability

A measurement is **traceable** when its value can be related to a national or
international standard through an unbroken chain of calibrations, each with a stated
uncertainty:

| Link | Contribution |
|---|---|
| definition (SI unit) | exact by definition |
| national standard realisation | stated by the national institute |
| laboratory reference | from the calibration certificate |
| working standard | from the before-and-after check |
| field instrument | from this calibration |

Three practical requirements follow. Each link needs a **documented uncertainty**
(a certificate, a report or a recorded check), and each transfer a **record of its
conditions**. The measurement's uncertainty is the **quadrature sum down the chain**,
not the last link's alone — which is why a careful calibration against an
uncalibrated working standard is worth less than a rough calibration against a
traceable one.

Traceability is usually required for anything legal or regulatory, anything compared
across institutions (absolute gravity, geomagnetic field values, geodetic
coordinates), and laboratory properties that will be published. For most relative
surveys, traceability to a working standard with a documented history suffices —
provided the report says so.

## 7. Verification and acceptance testing

A calibration establishes the scale; **testing** establishes that the instrument
works as the calibration says. The minimum set for a field instrument:

1. **Before deployment**: the calibration, a repeatability check (repeated readings
   of one input) and a linearity check (a sweep, not just two points).
2. **During the campaign**: a check standard repeated at intervals shorter than the
   re-calibration interval, plus a comparison with a second instrument if possible.
3. **After deployment**: the calibration repeated, so the drift is measured for that
   deployment.
4. **A functional test** of what the calibration does not cover: the clock against a
   reference, the anti-alias filter with a sweep, the dynamic range near full scale,
   an injection into every channel.
5. **A record** of all of the above, beside the calibration coefficients.

## 8. Assumptions and regime of validity

1. **A linear model.** Two-point calibrations assume linearity between the points,
   and a least-squares line assumes it everywhere; a residual plot with curvature
   is the evidence that the assumption fails.
2. **Independent, homoscedastic residuals.** The standard-error formulas assume
   equal-variance, independent errors. A drift *during* the calibration run, or a
   repeated reading reused several times, violates both.
3. **The reference is correct.** The chain's value is taken as the truth; a wrong
   certificate propagates silently through everything calibrated against it.
4. **The drift is linear in time.** Real drift is often a step (a shock, a repair)
   plus a slow trend; a linear interval rule cannot protect against a step, which is
   why the *during-campaign* check exists.
5. **The environment matches.** A calibration at 20 °C does not transfer to a device
   at −10 °C unless the temperature coefficient is known and small.
6. **The instrument is the same instrument.** Identical models are not
   interchangeable: the calibration belongs to a serial number, and swapping
   sensors without swapping calibrations is one of the most common field errors.

## 9. The honest summary

- A calibration is a measurement: it has a function, residuals and an uncertainty.
- The residual standard deviation uses $n-2$ degrees of freedom; the RMS uses $n$,
  and they differ by 29 % at five points.
- The scale was known to 0.093 % here; the offset to 0.031 value units.
- The fit residual dominated the uncertainty budget (62 %), ahead of the reference
  standard (29 %): more calibration points beat a better reference.
- A 0.005/day drift against a 0.05 tolerance gives a 10-day re-calibration interval,
  and both numbers must be measured.
- Traceability is the documented chain, and its uncertainty is summed down the chain.

## 10. Python demonstration

[`code/calibration_demo.py`](./code/calibration_demo.py) prints every number quoted
above. It:

1. evaluates a five-point calibration, its residuals and their RMS and standard
   deviation;
2. computes the standard errors of the slope and the intercept and the relative
   scale uncertainty;
3. builds a four-term uncertainty budget and reports the share of each term;
4. computes the drift and the re-calibration interval for five elapsed times;
5. prints a five-link traceability chain.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/05-instrumentation-and-electronics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python calibration_demo.py
```

## 11. Exercises

Worked problem sets are in
[`exercises/04-calibration-and-testing-exercises.md`](./exercises/04-calibration-and-testing-exercises.md)
and
[`exercises/04-calibration-and-testing-solutions.md`](./exercises/04-calibration-and-testing-solutions.md).

## 12. Mastery checkpoint

Without notes:

1. A calibration has a residual standard deviation of 0.04 value units from 7 points
   spread over a raw range of 0 to 600 with a mean of 300. Compute
   $\sum(x-\bar x)^{2}$ for evenly spaced points, then $\mathrm{se}(a)$ and
   $\mathrm{se}(b)$.
2. Express the answer to (1) as a relative scale uncertainty, given $a = 0.5$.
3. A drift rate of 0.02 value units per day and a tolerance of 0.1: compute the
   re-calibration interval.
4. State which term in an uncertainty budget you would attack first, given a fit
   residual twice the reference's contribution.
5. State the difference between calibration and testing.

## 13. Common pitfalls

1. **Quoting the RMS residual as the parameter uncertainty.** It uses $n$, not
   $n-2$.
2. **Not plotting the residuals.** Structure in them means the model is wrong.
3. **Calibrating over too narrow a range.** The scale uncertainty depends on the
   spread, not on the number of points alone.
4. **A working standard that is never checked.** A change in the reference is
   invisible.
5. **Extending the interval because nothing has failed.** Absence of evidence is not
   evidence of stability.
6. **Swapping instruments without swapping calibrations.** The calibration belongs
   to a serial number.
7. **A budget that adds correlated terms in quadrature.** It understates the total.

## 14. Where this is used

- Every geophysical instrument before and after a campaign: gravimeters,
  magnetometers, seismometers, loggers, thermistors and pressure sensors.
- Laboratory apparatus, where published rock properties require a traceable
  measurement chain — see
  [23-06-08 Laboratory Uncertainty Budgets and Reporting](../06-laboratory-measurements/08-lab-data-uncertainty.md).
- Absolute measurements with regulatory or cross-institutional significance:
  absolute gravity, geomagnetic field values, geodetic coordinates, radiological
  monitoring.
- Sensor networks, where a common scale across stations is the requirement and a
  single mis-calibrated station biases every derived map.
- Any archived dataset: the calibration coefficients and their uncertainty belong in
  the metadata.

## 15. Related lessons

- [01 Sensors and Transducers: Principles and Selection](01-sensors-and-transducers.md) —
  the sensitivity being calibrated.
- [02 Amplification, Filtering and Analog-Digital Conversion](02-signal-conditioning.md) —
  the chain whose ENOB must be measured, not assumed.
- [03 Timing, GNSS Disciplining and Clock Accuracy](03-timing-and-gnss-instruments.md) —
  the clock, which needs its own calibration against a reference.
- [23-02-01 Seismometers: Broadband, Short-Period, Geophones, MEMS](../02-seismic-instruments-and-fieldwork/01-seismometers.md) —
  where the instrument response must be established by calibration.
- [23-06-08 Laboratory Uncertainty Budgets and Reporting](../06-laboratory-measurements/08-lab-data-uncertainty.md) —
  the same budget arithmetic applied to laboratory data.

## 16. Self-assessment checklist

- [ ] I can fit a linear calibration and compute its residuals.
- [ ] I can compute the standard errors of the slope and intercept.
- [ ] I can build and interpret an uncertainty budget.
- [ ] I can compute a re-calibration interval from a drift rate.
- [ ] I can describe a traceability chain and its contributions.
- [ ] I can design before-, during- and after-campaign acceptance tests.
