---
id: 23-03-01
title: "Gravity Fieldwork: Loops, Drift, Base Stations, Ties"
level: advanced
prereqs: ["07-02-03", "23-01-03"]
estimated_minutes: 100
tags: [gravity, fieldwork, drift, base-station, loops, quality-control]
---

# Gravity Fieldwork: Loops, Drift, Base Stations, Ties

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** instrument drift, tidal variation and reading noise as the
   three time-varying terms a relative gravity survey must remove.
2. **Compute** a drift correction from repeated base-station occupations and
   **measure** the residual it leaves.
3. **Compare** a two-tie and a multi-tie correction and **state** the cost and the
   benefit of each.
4. **Compute** a loop closure error, and **explain** why the acceptance tolerance
   must be stated with the loop duration and the time of day.
5. **Compute** the repeatability of a station reading, the standard error of a
   station value, and the elevation equivalent of a stated gravity error.
6. **Design** a looping schedule for a stated accuracy target, and **state** what
   the design cannot distinguish.

All drift rates, tidal amplitudes, reading noises and loop durations in this
lesson are **SYNTHETIC** teaching values printed by the demonstration. No measured
instrument drift, no tidal model and no field reading is used or reproduced.

## Prerequisites

- [07-02-03 Survey Procedures: Loops, Drift, Repeatability and Ties](../../07-gravity-geodesy/02-gravity-instruments-and-surveys/03-survey-procedures.md) —
  the survey procedure this lesson makes quantitative.
- [23-01-03 Field Notebooks, Metadata and Data Provenance](../01-field-safety-and-planning/03-field-notebooks.md) —
  the record that makes a drift correction possible after the fact.

## 1. Intuition: a gravity reading is a difference in time as well as space

A relative gravimeter does not measure $g$; it measures the change in $g$ between
where it was zeroed and where it now stands. That change is small: a 1 mGal
anomaly corresponds to a relative change of about $10^{-6}$. Over such a small
range, the instrument itself is a significant source of change.

Three time-varying terms contaminate every reading:

- **Instrument drift** — a slow, roughly monotonic change from spring relaxation,
  thermal equilibration, or electronic ageing, of order hundredths to tenths of a
  milligal per hour.
- **Tidal variation** — the solid Earth tide changes $g$ by a fraction of a
  milligal with periods near 12.4 h and 24 h, plus longer-term components. It is
  *not* linear over a working day.
- **Reading noise** — repeatability of a single reading, typically a few
  thousandths of a milligal.

The survey design question is how to separate the geology from these three, using
only the fact that at a **base station** the value does not change.

## 2. Drift, tide and the base station

Let the true anomaly at a station be $A(\mathbf{x})$, the instrument and tidal
variation be $d(t)$, and a noise term $\epsilon$. A reading is

$$r(t,\mathbf{x}) = A(\mathbf{x}) + d(t) + \epsilon .$$

At the base station $A = 0$ by definition, so a base reading measures $d(t)$
directly. The demonstration's synthetic model is

$$d(t) = 0.008\,t + 0.10\sin\!\left(\frac{2\pi t}{12.4}\right)
+ 0.04\sin\!\left(\frac{2\pi t}{24}\right)\ \mathrm{mGal},$$

with $t$ in hours: a linear instrument term of **0.008 mGal/h** plus two tidal
harmonics. Its values over a 6 h loop are

| $t$ (h) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $d$ (mGal) | 0.0000 | 0.0669 | 0.1209 | 0.1522 | 0.1564 | 0.1358 | 0.0981 |

and the total change over the loop is 0.0981 mGal — small compared with a
milligal, and large compared with the hundredth-of-a-milligal accuracy a
microgravity survey claims. Note also that $d(6) < d(3)$: the tidal term has
turned the drift curve over, so a "drift rate" estimated from the two end
readings understates the variation in the middle.

## 3. What a drift correction leaves behind

Two base occupations bracket the loop, and the correction is the straight line
through them. Since the true anomaly is zero at every station in this synthetic
test, the *residual* after correction is exactly the part of $d(t)$ a straight line
cannot represent. The demonstration reports

| Correction | RMS residual (mGal) | maximum residual (mGal) |
|---|---|---|
| none | 0.1230 | 0.1579 |
| two base ties (0 h, 6 h) | 0.0732 | 0.1026 |
| three ties (0, 3, 6 h) | 0.0160 | 0.0237 |
| four ties (0, 2, 4, 6 h) | 0.0073 | 0.0127 |

Three results follow, all of which generalise beyond these numbers.

1. **A linear correction removes the instrument term but not the tide.** The
   residual after two ties, 0.0732 mGal, is 60 % of the uncorrected 0.1230 mGal,
   because the linear part was never the whole of $d(t)$.
2. **Adding a midpoint tie is dramatically effective.** The residual falls from
   0.0732 to 0.0160 mGal: a factor of 4.6 for one extra base occupation. The extra
   occupation costs perhaps 20 minutes of field time; there is no other intervention
   in a gravity survey with that return.
3. **The returns diminish.** A fourth tie reduces the residual by a further factor
   of 2.2, and beyond a certain point the base occupation time is better spent
   elsewhere.

The design rule: **tie often enough that the residual is below the survey's
accuracy target, and no more often.** With the numbers above and a target of
0.02 mGal, three ties per 6 h loop suffice; a target of 0.01 mGal needs four.

## 4. Loop closure as a quality-control statistic

The **closure error** of a loop is the difference between the last and first base
readings, before any correction:

$$e_{\text{closure}} = r_{\text{base}}(t_1) - r_{\text{base}}(t_0) = d(t_1) - d(t_0).$$

It is a measure of how much $d$ changed over the loop, and it is therefore
predictable from the loop duration *and* the time of day. The demonstration's worst
closure over four start times:

| Loop duration (h) | worst closure over the four starts (mGal) |
|---|---|
| 2.0 | 0.1209 |
| 4.0 | 0.1564 |
| 6.0 | 0.1871 |
| 8.0 | 0.1684 |

Two things are worth noticing. First, the closure does **not** grow monotonically
with duration: an 8 h loop that starts when the tide is turning can close better
than a 4 h loop that starts on its steepest part. Second, the reading noise on a
difference of two readings is $0.005\sqrt{2} = 0.0071$ mGal, negligible compared
with the tidal term at these durations.

Consequences for the acceptance criterion:

- State the tolerance **as a function of loop duration and season**, not as a
  single number.
- A closure error larger than the expected $d(t_1) - d(t_0)$ indicates something
  other than drift and tide: a mis-read station number, a wrong base value entered,
  a disturbed instrument, or a reading taken without allowing the sensor to settle.
- Conversely, an *unusually small* closure is not necessarily good: it can mean the
  two base readings were taken close together while the instrument was still in
  the same state, and it says nothing about the middle of the loop.

## 5. Repeatability and the accuracy of a station value

Repeat one station $n$ times and compute the sample standard deviation $s$ of the
readings. That $s$ is the **single-reading repeatability**, and the standard error
of the station value when three readings are averaged is $s/\sqrt{3}$. The
demonstration's ten repeats (reading noise 0.005 mGal) give $s = 0.0056$ mGal, a
95 % repeatability of 0.0124 mGal, and a standard error of 0.0032 mGal for a
three-reading station.

Convert that to a physical scale, because the number is otherwise meaningless: with
the free-air gradient of $0.3086\ \mathrm{mGal/m}$,

$$\delta h = \frac{\delta g}{0.3086\ \mathrm{mGal/m}} = \frac{0.01}{0.3086}
= 0.0324\ \mathrm{m},$$

so a 0.01 mGal gravity error is equivalent to a 3.2 cm elevation error. This is why
a microgravity survey needs levelling to centimetres and GNSS positions to
decimetres, and it is the calculation that sets the specification for the
positioning work of
[03 Positioning and Elevation Determination in the Field](03-positioning-in-field.md).

## 6. Designing a looping schedule

Given a target accuracy $\sigma_{\text{target}}$, a drift rate $r$ and a tidal
amplitude $A_{\text{tide}}$ at period $T$:

1. **Set the loop duration from the instrument term** so that $r\,\Delta t$ is a
   fraction of the target: for $r = 0.008\ \mathrm{mGal/h}$ and a 0.02 mGal target,
   $\Delta t \le 2.5\ \mathrm{h}$ *if only the linear term mattered*.
2. **Then account for the tide**, which the linear correction cannot remove. For a
   single sinusoid of amplitude $A$ and period $T$, the worst-case maximum residual
   of a straight-line fit over an interval $\Delta t$ grows faster than linearly in
   $\Delta t$. Evaluated for $A = 0.10\ \mathrm{mGal}$ and $T = 12.4\ \mathrm{h}$:

   | $\Delta t$ (h) | 1 | 2 | 3 | 4 | 6 |
   |---|---|---|---|---|---|
   | worst max residual (mGal) | 0.0021 | 0.0084 | 0.0183 | 0.0314 | 0.0636 |
   | as a fraction of $A$ | 0.021 | 0.084 | 0.183 | 0.314 | 0.636 |

   A residual target of 0.02 mGal therefore allows intervals of about 3 h at this
   tidal amplitude — consistent with the three-tie result of Section 3, whose two
   3 h intervals left an RMS residual of 0.0160 mGal.
3. **Choose the number of ties** so the remaining residual is below target.
4. **Convert to stations per loop** using the access and measurement time, which is
   usually the binding constraint: the number of stations is set by how far the
   vehicle can travel between ties, not by the drift.

## 7. Assumptions and regime of validity

1. **The base station does not change.** A base on a concrete floor of a building
   with a varying water table, or in a field that receives irrigation, changes
   slowly and silently; the correction then imports that change into every station.
   Bases are re-occupied between campaigns precisely to detect this.
2. **The drift is the same at the base and at the station.** Instrument drift is a
   property of the instrument, but *tidal* and environmental effects depend on the
   location, so a base 30 km away does not measure the tide at the station
   exactly. For microgravity surveys the tidally induced difference is
   computed and applied, rather than inferred from a distant base.
3. **The instrument behaves linearly.** A gravimeter that has been transported,
   tilted excessively, or is still thermally equilibrating violates this, and the
   violation appears as a closure error.
4. **The reading noise is stationary.** $s$ from ten repeats measures the noise in
   the conditions of those repeats; a windy ridge or a busy road later in the
   survey has different noise.
5. **The residual is unbiased.** A drift correction that interpolates between ties
   removes the *linear* part of the true variation; any curvature left is a bias
   correlated with the loop position, not random error. It propagates into the
   anomaly map as a pattern aligned with the looping.

## 8. The honest summary

- Three time-varying terms — instrument drift, tide and noise — must be removed.
- A two-tie linear correction left 0.0732 mGal RMS here; a midpoint tie cut it to
  0.0160 mGal, a factor of 4.6 for a few minutes of work.
- Closure error depends on loop duration *and* time of day; a single tolerance is
  not a criterion.
- A 0.01 mGal gravity error is a 3.2 cm elevation error.
- The residual of a drift correction is a *bias* aligned with the looping, not
  random noise.

## 9. Python demonstration

[`code/gravity_fieldwork_demo.py`](./code/gravity_fieldwork_demo.py) prints every
number quoted above. It:

1. evaluates a synthetic drift (linear instrument term plus two tidal harmonics);
2. computes the RMS and maximum residual left by no correction, two ties, three
   ties and four ties;
3. tabulates the closure error for four loop durations over four start times;
4. computes the repeatability from ten repeats and the free-air equivalent of a
   0.01 mGal error.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/03-gravity-magnetic-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_fieldwork_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/01-gravity-fieldwork-exercises.md`](./exercises/01-gravity-fieldwork-exercises.md)
and
[`exercises/01-gravity-fieldwork-solutions.md`](./exercises/01-gravity-fieldwork-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A gravimeter drifts at 0.012 mGal/h and a loop lasts 4 h. Compute the drift
   accumulated, and the residual if only the linear term is corrected while a
   tidal term of 0.08 mGal amplitude at a 12.4 h period is present.
2. A loop's base readings are 1000.000 and 1000.150 mGal. Compute the closure
   error and state whether it is plausible for a 3 h loop with the drift and tide
   of Section 2.
3. Ten repeats give a standard deviation of 0.004 mGal. Compute the standard error
   of a three-reading station value and its free-air equivalent in metres.
4. State why a drift correction's residual is a bias rather than random noise.

## 12. Common pitfalls

1. **Correcting drift linearly over a long loop.** The tide turns over; the linear
   fit is then wrong in the middle by more than the target accuracy.
2. **A single closure tolerance for all loops.** The expected closure depends on
   the loop duration and the time of day.
3. **A base station that changes.** Water table, traffic, construction or a
   seasonal soil-moisture cycle will all appear as drift.
4. **Inferring tide from a distant base.** Tidal acceleration differs with
   position; compute it rather than infer it where the accuracy matters.
5. **Reporting the repeatability as the survey accuracy.** Repeatability is one
   term; drift residual, positioning error and reduction errors are others.
6. **Ignoring the elevation sensitivity.** A 3 cm elevation error is a 0.01 mGal
   anomaly, which is the size of the target in many microgravity surveys.

## 13. Where this is used

- Microgravity surveys for cavities, tunnels, voids and archaeology, where the
  anomaly of interest is a few tens of microgal.
- Engineering and geotechnical gravity surveys for void detection and foundation
  investigations.
- Regional and exploration gravity surveys, where the same loop discipline is used
  at a coarser accuracy target.
- Volcanology and geodesy, where repeated campaigns compare a network against
  itself and the base-station stability is the limiting systematic error.
- Any survey that will be levelled, gridded and interpreted: the residual of the
  drift correction becomes a pattern in the map.

## 14. Related lessons

- [02 Magnetic Fieldwork: Diurnal Variation, Leveling, Gradients](02-magnetic-fieldwork.md) —
  the same looping and tying discipline for a different field.
- [03 Positioning and Elevation Determination in the Field](03-positioning-in-field.md) —
  the positioning that the elevation sensitivity requires.
- [04 Field Data QC for Potential-Field Surveys](04-field-data-qc-gravmag.md) —
  the statistics of loops, repeats and cross-overs.
- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md) —
  what the reduced reading becomes.
- [07-02-02 Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex](../../07-gravity-geodesy/02-gravity-instruments-and-surveys/02-relative-gravimeters.md) —
  why the instrument drifts at all.

## 15. Self-assessment checklist

- [ ] I can name and rank the three time-varying contaminants.
- [ ] I can compute a drift correction from base ties and its residual.
- [ ] I can explain the return from adding a midpoint tie.
- [ ] I can compute a closure error and say what it evidences.
- [ ] I can convert a gravity error into an elevation error.
- [ ] I can design a looping schedule for a stated accuracy.
