---
id: 23-03-02
title: "Magnetic Fieldwork: Diurnal Variation, Leveling, Gradients"
level: advanced
prereqs: ["08-03-01", "23-03-01"]
estimated_minutes: 100
tags: [magnetics, fieldwork, diurnal, levelling, gradients, quality-control]
---

# Magnetic Fieldwork: Diurnal Variation, Leveling, Gradients

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** the diurnal variation, the secular field and instrument
   effects as the three time-varying terms a magnetic survey must remove.
2. **Compute** the residual left by a linear base-loop correction and by an
   hourly correction, and **choose** a looping interval for a stated target.
3. **Compute** line-to-line mis-tie statistics and the correction they justify,
   and **state** what levelling cannot remove.
4. **Compute** the repeatability of a reading and the standard error of a station
   value in nanotesla.
5. **Estimate** a source depth from an anomaly's half-width, and **state** the
   model dependence of the factor.
6. **Design** a magnetic survey's base-looping and tie-line plan for a stated
   accuracy, and **state** what it cannot detect.

All diurnal amplitudes, reading noises, line shifts and model parameters in this
lesson are **SYNTHETIC** teaching values printed by the demonstration. No measured
diurnal curve, field reading or published anomaly is used or reproduced.

## Prerequisites

- [08-03-01 Magnetic Anomaly Physics and Remanent vs Induced Magnetisation](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/01-magnetic-anomaly-basics.md) —
  what the survey is measuring.
- [23-03-01 Gravity Fieldwork: Loops, Drift, Base Stations, Ties](01-gravity-fieldwork.md) —
  the same looping discipline applied to a different field.

## 1. Intuition: magnetics is a differential measurement of a varying field

A magnetometer measures the total field (or its components) in nanotesla. The
field it measures varies in time as well as in space, and the two variations are
comparable in size: an anomaly of interest may be 50–500 nT while the diurnal
variation over a working day reaches tens of nanotesla. Unlike gravity, the
variation is also **large and irregular**, driven by ionospheric current systems
and by magnetospheric activity, so it cannot be modelled well enough to be removed
without measurement.

Three terms must be separated:

- **Diurnal variation** — a smooth, quasi-periodic variation with a daily cycle
  and faster harmonics, of order a few to a few tens of nanotesla at mid-latitudes,
  and much larger during magnetic storms.
- **Secular variation** — the slow change of the main field, of order tens of
  nanotesla per year, which matters for comparing surveys of different epochs but
  not within a single campaign.
- **Instrument and procedural effects** — sensor drift, heading error on a
  moving platform, and the effect of the operator and vehicle on the field.

The field method that removes the diurnal term is the **base-station loop**: a
recording magnetometer (or a repeated reading) at a fixed base, whose variation is
subtracted from the roving readings.

## 2. The diurnal correction, and what a linear one misses

Let $B(\mathbf{x})$ be the anomaly, $D(t)$ the diurnal variation and $\epsilon$ the
noise. A roving reading is $r(t, \mathbf{x}) = B(\mathbf{x}) + D(t) + \epsilon$.
The base measures $D(t)$ (plus the local field, which is constant), so the
correction is to subtract the base reading interpolated to the roving time.

The critical question is how well a *linear* interpolation between two base
occupations represents $D(t)$. The demonstration's synthetic diurnal model is

$$D(t) = 22\sin\!\left(\frac{2\pi t}{24}\right)
+ 7\sin\!\left(\frac{2\pi t}{8}\right)\ \mathrm{nT},$$

with values over a 12 h span

| $t$ (h) | 0 | 2 | 4 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|---|---|
| $D$ (nT) | 0.000 | 18.000 | 19.053 | 15.000 | 19.053 | 18.000 | 0.000 |

For 40 stations read over an 8 h day, with the station anomaly set to zero so that
the residual is the uncorrected variation, the demonstration reports

| Correction | RMS residual (nT) | maximum residual (nT) |
|---|---|---|
| none | 16.720 | 20.508 |
| two base ties (0 h, 8 h) | 8.600 | 13.902 |
| nine ties (hourly) | 0.278 | 0.606 |

The comparison is the lesson. A two-tie linear correction removes only **49 %** of
the variation, because the 8 h harmonic makes the diurnal curve non-monotonic: the
correction assumes the variation is a straight line and it is not. Hourly
occupations reduce the residual by a further factor of **31**, to 0.278 nT — far
below the reading noise, which is the point at which more looping stops helping.

The practical rules:

1. **A continuously recording base magnetometer is worth more than any number of
   roving occupations at the base.** It removes the interpolation error entirely
   (leaving only the instrument difference and the base's own anomaly), and it costs
   one instrument.
2. **If a base recorder is not available, occupy the base at least hourly** and
   discard readings taken during a magnetic disturbance (see below). Interpolating
   linearly over a longer interval is an unbounded error.
3. **A linear two-tie correction is not a diurnal correction.** It is a drift
   correction, and it removes about half the problem.

## 3. Leveling: mis-ties and what they mean

Survey lines cross the tie lines at **tie points**. Two lines measured at different
times give different values at the same tie point; the difference is the **mis-tie**,
and it contains the residual diurnal error, the line-to-line levelling error, and
the reading noise.

The demonstration's synthetic set: 5 lines crossing 12 tie points, with a
line-to-line shift of 6.0 nT standard deviation and a 1.5 nT reading noise. It
reports

| Statistic | Value |
|---|---|
| mean mis-tie | −0.096 nT |
| standard deviation | 7.534 nT |
| 95 % of mis-ties within | 14.767 nT |
| largest \|mis-tie\| | 15.379 nT |
| mis-ties exceeding 15 nT | 1 of 60 |

Three things follow.

- **The mean is not the problem.** A non-zero mean is a levelling offset that can
  be removed; the *scatter* is what limits the interpretation, and here it is
  7.5 nT.
- **The scatter is not noise.** It is dominated by the 6.0 nT line-to-line shift
  injected into the model, which is a levelling error, not measurement error. A
  mis-tie scatter much larger than the reading noise is evidence of a levelling
  problem, and the fix is a levelling correction, not more readings.
- **A 7.5 nT shift is 7.5 % of a 100 nT target anomaly, and it appears as a step
  along the tie line** — which no filter can distinguish from a geological
  boundary running along that line. This is the reason levelling is done before
  interpretation and is reported as a processing step.

## 4. Repeatability, and the effect of the operator

Repeat one station and compute the standard deviation of the readings; the standard
error of a three-reading station value is $s/\sqrt{3}$. The demonstration's fifteen
repeats (reading noise 1.5 nT) give $s = 1.266$ nT and a standard error of
0.731 nT, so a 100 nT anomaly is 137 times the standard error of a station value.

Two cautions specific to magnetics:

- **The repeat is only a repeat if the geometry is identical.** The operator's
  position, the instrument's height above the ground, the orientation of the sensor
  and the presence of the vehicle all change the measured field by more than the
  reading noise on some instruments. The repeat test measures the *procedure*, and
  a procedure that leaves the operator's rucksack 0.5 m from the sensor may pass one
  day and fail the next.
- **Heading error.** On a moving platform (airborne, or a walking survey with a
  vector sensor) the field depends on the sensor's orientation relative to the
  field. A total-field instrument is largely immune; a component instrument is not,
  and the heading error must be characterised by flying or walking the same line in
  opposite directions and comparing.

## 5. Gradients, and a field depth estimate

Two sensors separated vertically (a **gradient** configuration), or two sensors
separated horizontally, measure the field's spatial derivative. The gradient has
three practical uses:

1. **Removing the diurnal variation by co-measurement.** Two sensors a metre apart
   see almost the same diurnal variation while seeing different anomalies (the
   shallow source is much stronger at the lower sensor), so the *difference* is
   nearly free of the diurnal term. This is the same common-mode-rejection argument
   as a gradiometer in gravity.
2. **Emphasising shallow sources.** A first derivative multiplies the anomaly by a
   factor of order $k = 2\pi/\lambda$; halving the wavelength doubles the gradient
   response while leaving regional fields largely untouched.
3. **A field depth estimate.** For an isolated, sphere-like induced source the
   anomaly profile's **half-width** — the distance from the peak to the point where
   the anomaly has fallen to half its peak value — is proportional to the depth.
   The demonstration computes the profile of a synthetic sphere at 40 m depth with
   a 25 m radius and measures

| Quantity | Value |
|---|---|
| half-width (x at half the peak) | 18.07 m |
| full width at half maximum | 36.14 m |
| depth / half-width | 2.214 |
| depth from $2.2 \times$ half-width | 39.75 m (−0.62 %) |

The factor is a property of the **model**, not a constant of nature: for this
induced-dipole (sphere) model it is 2.2, and a horizontal cylinder, a thin sheet or
a contact gives a different number. Quote the model with the rule, treat the result
as a siting aid, and remember that the estimate assumes an isolated source, an
induced (not remanent) magnetisation, and a flat regional field.

## 6. Assumptions and regime of validity

1. **The base station is representative.** The diurnal variation has a spatial
   scale, and a base 50 km away does not measure exactly the same variation; the
   instrument difference and the local anomaly at the base must be removed.
2. **No magnetic storm.** During a storm the variation reaches hundreds of
   nanotesla with a rapid, spatially varying structure that no base loop can
   correct. The remedy is to monitor an activity index and to re-observe the day's
   lines, not to correct them.
3. **The anomaly is induced and the field direction is constant.** A strong
   remanent magnetisation or a changing field direction (`dI/dt`) invalidates
   reduction to the pole and the simple depth rules.
4. **The sensors' geometry is repeatable.** A gradient configuration is only a
   gradient if the separation is known and constant, and a walking survey's sensor
   height must be held.
5. **The levelling correction is a line-level adjustment, not a physical model.**
   It removes a systematic per-line offset; it cannot restore information, and it
   can absorb a genuine anomaly trend that happens to align with a line.
6. **Reading noise is stationary.** Repeatability measured at one station on one
   day is not the survey's noise; magnetic noise varies with geology (magnetic
   soils), culture and time of day.

## 7. The honest summary

- The diurnal variation cannot be modelled; it must be measured.
- A two-tie linear correction removed 49 % of it here; hourly base occupations cut
  the residual by a further factor of 31, to 0.278 nT.
- A continuously recording base magnetometer removes the interpolation error
  entirely and is the single most valuable item in a magnetic survey.
- Mis-tie scatter above the reading noise is a levelling problem, measured here at
  7.5 nT, which is 7.5 % of a 100 nT anomaly and appears as a step along a line.
- Repeatability is a test of the *procedure*, including the operator's geometry.
- The half-width depth rule works to about 1 % for its own model, and only for its
  own model.

## 8. Python demonstration

[`code/magnetic_fieldwork_demo.py`](./code/magnetic_fieldwork_demo.py) prints every
number quoted above. It:

1. evaluates a synthetic two-harmonic diurnal variation and the residual left by
   no correction, two ties and hourly ties;
2. computes mis-tie statistics for five lines crossing twelve tie points;
3. computes the repeatability from fifteen repeats and the ratio of a 100 nT
   anomaly to the standard error;
4. computes a synthetic sphere anomaly, measures its half-width and recovers the
   depth with the half-width rule.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/03-gravity-magnetic-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_fieldwork_demo.py
```

## 9. Exercises

Worked problem sets are in
[`exercises/02-magnetic-fieldwork-exercises.md`](./exercises/02-magnetic-fieldwork-exercises.md)
and
[`exercises/02-magnetic-fieldwork-solutions.md`](./exercises/02-magnetic-fieldwork-solutions.md).

## 10. Mastery checkpoint

Without notes:

1. The diurnal variation has a 22 nT amplitude at 24 h and 7 nT at 8 h. Compute
   its value at $t = 2$ h and at $t = 4$ h, and state why a linear correction over
   an 8 h day cannot represent it.
2. A two-tie correction left an RMS residual of 8.600 nT. Compute the residual as
   a fraction of the uncorrected 16.720 nT, and state the correction that would
   leave 0.278 nT.
3. Mis-ties have a mean of 0.0 nT and a standard deviation of 7.5 nT. State what
   fraction of a 150 nT anomaly that is, and what the mis-tie scatter above the
   reading noise indicates.
4. An anomaly has a half-width of 12 m. Using the sphere rule, estimate the depth
   and state the two assumptions.
5. State the one instrument that makes base looping unnecessary.

## 11. Common pitfalls

1. **Calling a two-tie linear correction a diurnal correction.** It is a drift
   correction and removes about half the variation.
2. **Interpolating over hours.** The 8 h harmonic makes the curve non-monotonic;
   the interpolated value can be wrong in either direction.
3. **Correcting data from a magnetic storm.** The spatial structure of a storm's
   variation is not removed by a single base.
4. **Levelling a real anomaly away.** A line-level adjustment absorbs any anomaly
   trend aligned with the line.
5. **Repeating a station with a different sensor height or orientation.** The test
   then measures geometry, not repeatability.
6. **Applying the sphere half-width factor to a dyke or a contact.** The factor is
   model-specific; the wrong model gives a depth wrong by tens of per cent.
7. **Ignoring the difference between the base and the survey area.** The diurnal
   variation has a spatial gradient.

## 12. Where this is used

- Mineral exploration and geological mapping, where magnetic anomalies are the
  primary reconnaissance dataset.
- Environmental and engineering surveys for buried drums, tanks, pipes and
  archaeology, where small anomalies and therefore careful levelling matter.
- Airborne and drone magnetics, where the diurnal correction, the heading error and
  the tie-line levelling are the three dominant data-quality issues.
- Volcanology and geothermal exploration, where repeat surveys compare a network
  against itself.
- Any survey whose product is a grid: mis-ties and levelling are visible in the map
  as line-correlated stripes.

## 13. Related lessons

- [01 Gravity Fieldwork: Loops, Drift, Base Stations, Ties](01-gravity-fieldwork.md) —
  the same looping and tying discipline for gravity.
- [03 Positioning and Elevation Determination in the Field](03-positioning-in-field.md) —
  the positioning that the reductions require.
- [04 Field Data QC for Potential-Field Surveys](04-field-data-qc-gravmag.md) —
  loop closures, repeats, mis-ties and cross-overs as statistics.
- [08-01-07 Rock Magnetism: Remanence, Susceptibility and Magnetic Mineralogy](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/07-rock-magnetism.md) —
  why an anomaly may not be induced.
- [05-06-05 Gridding, Merging and Levelling of Survey Data](../../05-core-geophysics/06-data-processing-principles/05-merge-and-regularisation.md) —
  what happens to the levelled data next.

## 14. Self-assessment checklist

- [ ] I can describe the three time-varying terms and how each is removed.
- [ ] I can compute the residual of a linear and of an hourly base correction.
- [ ] I can compute mis-tie statistics and interpret their scatter.
- [ ] I can compute a repeatability and a station standard error.
- [ ] I can estimate a depth from a half-width and state the model assumption.
- [ ] I can design a base-loop and tie-line plan for a stated accuracy.
