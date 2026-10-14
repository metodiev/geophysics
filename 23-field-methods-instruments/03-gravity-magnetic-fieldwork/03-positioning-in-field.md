---
id: 23-03-03
title: "Positioning and Elevation Determination in the Field"
level: advanced
prereqs: ["23-03-01", "07-04-03"]
estimated_minutes: 95
tags: [positioning, gnss, elevation, levelling, gravity, magnetics, fieldwork]
---

# Positioning and Elevation Determination in the Field

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the free-air and Bouguer elevation sensitivities of a gravity
   survey and the elevation accuracy a stated anomaly target requires.
2. **Compute** the latitude correction and the north–south position accuracy a
   stated target requires.
3. **Compute** the vertical gradient of the main magnetic field from a dipole model
   and **compare** the height sensitivity of magnetics with that of gravity.
4. **Distinguish** the random and systematic parts of a GNSS error budget, and
   **state** what averaging can and cannot remove.
5. **Compute** the anomaly error produced by confusing ellipsoidal and orthometric
   heights.
6. **Choose** a positioning method for a stated survey, and **state** the check
   that verifies it in the field.

All accuracies, densities and undulation magnitudes in this lesson are
**SYNTHETIC** teaching values, or derived from stated standard formulas. No
measured survey accuracy, real geoid model or field position is used or
reproduced.

## Prerequisites

- [01 Gravity Fieldwork: Loops, Drift, Base Stations, Ties](01-gravity-fieldwork.md) —
  the survey whose reductions need these quantities.
- [07-04-03 GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution](../../07-gravity-geodesy/04-geodesy-reference-frames/03-gnss-positioning.md) —
  the positioning technology.

## 1. Intuition: position and height are part of the measurement

In a potential-field survey the quantity that reaches the interpretation is not
the reading; it is the reading after reduction, and the reduction needs the
station's latitude and elevation. Those come from a positioning system, and their
errors enter the anomaly directly.

The two sensitivities behave very differently:

- **Gravity is extremely height-sensitive.** The free-air gradient is
  $0.3086\ \mathrm{mGal/m}$, so a decimetre of elevation error is already a
  measurable anomaly.
- **Magnetics is almost height-insensitive.** The main field changes by a few
  hundredths of a nanotesla per metre, so height accuracy matters to magnetics
  mostly through the *terrain* correction and through sensor height for
  near-surface sources.

And both are latitude-sensitive, through the normal-gravity gradient for gravity
and through the direction and strength of the main field for magnetics.

## 2. Elevation: the free-air and Bouguer sensitivities

Reducing a gravity reading to a datum requires (among other terms) the **free-air**
correction, which accounts for the change of $g$ with height at the observation
point, and the **Bouguer** correction, which accounts for the attraction of the
rock slab removed or added between the station and the datum:

$$\frac{\partial g_{\text{FA}}}{\partial h} = 0.3086\ \mathrm{mGal/m}, \qquad
\frac{\partial g_{\text{B}}}{\partial h} = 0.0419\,\rho\ \mathrm{mGal/m},$$

with $\rho$ in $\mathrm{g/cm^3}$. For $\rho = 2.67\ \mathrm{g/cm^3}$ the Bouguer
gradient is $0.1119\ \mathrm{mGal/m}$ and the *net* sensitivity of a Bouguer
anomaly to elevation is

$$\frac{\partial g_{\text{BA}}}{\partial h} = 0.3086 - 0.1119
= 0.1967\ \mathrm{mGal/m}.$$

The demonstration's table:

| Elevation error (m) | free-air term (mGal) | Bouguer anomaly (mGal) |
|---|---|---|
| 0.02 | 0.0062 | 0.0039 |
| 0.05 | 0.0154 | 0.0098 |
| 0.10 | 0.0309 | 0.0197 |
| 0.20 | 0.0617 | 0.0393 |
| 0.50 | 0.1543 | 0.0984 |
| 1.00 | 0.3086 | 0.1967 |

Read the second column against a target: a microgravity survey aiming at
0.01 mGal needs elevation to about **5 cm**, which is optical-levelling or
RTK-GNSS territory. A regional survey aiming at 0.1 mGal needs about 0.5 m, which
a consumer-grade GNSS with a geoid model can deliver. **The target anomaly, not
the instrument, sets the levelling specification.**

## 3. Latitude and position

Normal gravity varies with latitude at approximately

$$\frac{\partial g}{\partial (\text{north})} \approx 0.811\sin(2\varphi)\
\mathrm{mGal/km},$$

so the sensitivity is largest at 45° and zero at the equator and the poles. The
demonstration's table:

| Latitude $\varphi$ | gradient (mGal/km) | 20 m N–S error (mGal) | 100 m N–S error (mGal) |
|---|---|---|---|
| 0° | 0.0000 | 0.0000 | 0.0000 |
| 30° | 0.7023 | 0.0140 | 0.0702 |
| 45° | 0.8110 | 0.0162 | 0.0811 |
| 60° | 0.7023 | 0.0140 | 0.0702 |
| 90° | 0.0000 | 0.0000 | 0.0000 |

At mid-latitudes a 20 m north–south position error contributes 0.016 mGal — close
to a microgravity survey's whole budget — while a 100 m error (a mis-georeferenced
base map, a wrong coordinate system, a station plotted on the wrong side of a
track) contributes 0.081 mGal, which is a large fraction of any small anomaly. The
practical rule: **position accuracy in the north–south direction is a survey
specification, not an administrative detail.**

## 4. Height and magnetics

The main field's magnitude changes with height because the field is that of a
source at the centre of the Earth: it *decreases* upward. Modelling the field as a
centred dipole, the demonstration computes

| Latitude | $\lvert B\rvert$ (nT) | $\partial\lvert B\rvert/\partial z$ (nT/m) |
|---|---|---|
| 0° | 30162.81 | −0.0142 |
| 30° | 39901.65 | −0.0188 |
| 45° | 47691.59 | −0.0225 |
| 60° | 54376.78 | −0.0256 |
| 90° | 60325.62 | −0.0284 |

So a 1 m height error changes the field by about 0.02 nT at mid-latitudes —
compared with a reading noise of a few nanotesla. **Height is not the magnetic
survey's problem.** The two places where height still matters are (i) the *terrain
correction* for a survey over steep topography, where the magnetisation of the
hills contributes more than the height effect, and (ii) micro-magnetic surveys of
shallow targets, where the sensor must be held at a reproducible height, a
requirement on *repeatability* rather than on absolute accuracy.

## 5. GNSS: random, systematic and what averaging buys

Every positioning method has an error budget with two parts:

- **Random error**, which falls as $1/\sqrt{N}$ with the number of independent
  observations (epochs, satellites, baselines).
- **Systematic error**, which does not fall at all: a wrong reference frame, a
  mis-specified antenna height, a baseline-length-dependent bias, an uncorrected
  ionospheric delay, or a coordinate-system mistake.

The demonstration's SYNTHETIC table:

| Method | $\sigma$ (m) | 1 epoch | 10 epochs | 100 epochs |
|---|---|---|---|---|
| autonomous, single receiver | 5.000 | 5.000 | 1.581 | 0.500 |
| differential (DGPS) | 0.500 | 0.500 | 0.158 | 0.050 |
| RTK, short baseline | 0.020 | 0.020 | 0.006 | 0.002 |

and a baseline-dependent term of 1 ppm over 20 km gives 0.020 m. The lesson is
visible in the row for autonomous positioning: 100 epochs brings the random part to
0.5 m, but no number of epochs removes the systematic part, and the autonomous
solution is *biased* relative to the reference frame in a way that depends on the
satellite geometry and the broadcast orbits. Averaging a biased measurement makes it
precisely wrong.

Operationally:

1. **Always record the antenna height and the measurement method** in the field
   notes, and measure the antenna height with a tape rather than reading it from a
   previous occupation. An antenna-height mistake is a pure vertical offset that
   looks like a real anomaly.
2. **Tie the survey to a known mark** — a benchmark, a published CORS station, a
   permanent base — and check the tie against the published coordinates. This
   catches the systematic errors that averaging cannot.
3. **Run a base station** for differential and RTK work, and check the base's
   coordinates against published values, not just against its own average.
4. **Compute the anomaly at one repeat station immediately after processing the
   first day** and compare it with the value expected from the previous campaign or
   from a map. A systematic coordinate error is invisible until that comparison is
   made.

## 6. Ellipsoidal versus orthometric height

A GNSS receiver returns an **ellipsoidal** height: the distance above a reference
ellipsoid. The gravity reduction needs an **orthometric** height: the distance
above the geoid, which is an equipotential surface approximating mean sea level.
The two differ by the **geoid undulation** $N$, which reaches tens of metres.

If the difference is ignored, the elevation error is $N$ itself, and the anomaly
error is $0.1967\,N$ mGal:

| Undulation error $N$ (m) | Bouguer anomaly error (mGal) |
|---|---|
| 1 | 0.197 |
| 5 | 0.984 |
| 10 | 1.967 |
| 30 | 5.902 |
| 50 | 9.836 |

A 30 m error is **5.9 mGal** — larger than almost any target anomaly in a
microgravity survey, and larger than many regional anomalies. The remedies, in
order of preference for accuracy:

1. **Use a geoid model** to convert ellipsoidal to orthometric heights, record the
   model's name and version, and state its uncertainty over the survey area. Modern
   regional geoid models are accurate to a few centimetres over well-surveyed
   countries; the accuracy away from the model's control data is not guaranteed.
2. **Carry orthometric height by optical levelling** from a known benchmark, which
   avoids the geoid model entirely at the cost of field time.
3. **Use a common vertical datum across the survey** — even if it is arbitrary —
   and state it. A constant vertical offset cancels in a *relative* anomaly map,
   but not in an anomaly that is to be compared with a regional field or another
   survey.

## 7. Assumptions and regime of validity

1. **The gradients are those of the standard formulas.** The free-air gradient is a
   normal-gravity approximation; over large elevation ranges, or in a strongly
   anomalous field, the local gradient differs and a measured vertical gradient
   (`d g/d h` at a tall building or a tower, or a repeat occupation at different
   heights) is better.
2. **The Bouguer density is known.** The Bouguer gradient depends on the chosen
   density, and the assumption contaminates every anomaly: changing $\rho$ from
   2.67 to 2.40 changes the gradient from 0.1119 to 0.1006 mGal/m.
3. **The latitude gradient is a smooth approximation** of the normal-gravity
   difference; it is adequate at the metre-per-kilometre scale of survey accuracy.
4. **The magnetic vertical gradient is that of the main field only**, from a dipole
   model; over a magnetic anomaly the local gradient is larger and the geometry of
   the source matters.
5. **The GNSS error budget is what the method promises**, not what a particular day
   delivered: multipath in a forest, an ionospheric disturbance or a poor satellite
   geometry can degrade a solution by an order of magnitude. The *measured* check —
   repeat occupations and a comparison of independent methods — is what establishes
   the actual accuracy.
6. **The geoid model applies to the survey area.** A model's formal accuracy is a
   statement about its control network, not a guarantee at a station 50 km from the
   nearest control point.

## 8. The honest summary

- The Bouguer anomaly responds to elevation at 0.1967 mGal/m: 5 cm of height for
  0.01 mGal.
- The latitude gradient peaks at 0.811 mGal/km at 45°: a 100 m north–south error is
  0.081 mGal.
- Magnetic height sensitivity is a few hundredths of a nanotesla per metre —
  negligible against a reading noise of nT.
- Averaging removes random error only; the systematic part must be controlled by
  tying to a known mark and checking it.
- Confusing ellipsoidal and orthometric heights can cost 5.9 mGal at a 30 m
  undulation.
- The target anomaly sets the positioning specification.

## 9. Python demonstration

[`code/positioning_in_field_demo.py`](./code/positioning_in_field_demo.py) prints
every number quoted above. It:

1. computes the free-air, Bouguer and combined elevation sensitivities and the
   anomaly error for six elevation errors;
2. tabulates the latitude gradient and the anomaly error from 20 m and 100 m
   north–south position errors;
3. computes the main field and its vertical gradient from a centred-dipole model at
   five latitudes;
4. tabulates three GNSS methods' accuracy at 1, 10 and 100 epochs and a
   baseline-dependent term;
5. converts five geoid undulation errors into Bouguer anomaly errors.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/03-gravity-magnetic-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python positioning_in_field_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/03-positioning-in-field-exercises.md`](./exercises/03-positioning-in-field-exercises.md)
and
[`exercises/03-positioning-in-field-solutions.md`](./exercises/03-positioning-in-field-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. Compute the free-air, Bouguer (at $\rho = 2.67$) and combined elevation
   gradients, and the elevation accuracy a 0.02 mGal target requires.
2. Compute the north–south position error that contributes 0.02 mGal at 40°
   latitude.
3. State the magnetic vertical gradient at mid-latitudes and compare it with the
   reading noise.
4. An autonomous GNSS solution is averaged over 200 epochs, giving a 0.35 m
   random error. State what the residual error is and why.
5. Compute the anomaly error from a 25 m geoid undulation error.

## 12. Common pitfalls

1. **Using ellipsoidal heights as orthometric heights.** The error reaches
   milligals.
2. **Assuming GNSS averaging converges to truth.** It converges to the biased
   solution.
3. **Reading the antenna height from the previous occupation.** A pure vertical
   offset that mimics an anomaly.
4. **Ignoring the north–south position specification.** At 45° a 100 m error is
   0.081 mGal.
5. **Using a single Bouguer density across a survey with varying geology.** The
   gradient, and therefore the anomaly, changes with the assumed density.
6. **Not recording the geoid model and its version.** The conversion cannot be
   reproduced.
7. **Levelling to the wrong datum.** A constant offset is harmless in a relative
   map and fatal in a comparison with another survey.

## 13. Where this is used

- Every gravity survey, at every scale from microgravity to regional.
- Airborne gravity and magnetics, where the positioning is the dominant error
  source and the height is measured by radar, laser or GNSS.
- Ground magnetic surveys over rough terrain, where the sensor height must be
  reproducible even though the absolute height matters little.
- Any survey that will be merged with existing data or with a regional grid, where
  the datum and the coordinate system must agree.
- Geodetic and geophysical monitoring networks, where repeated occupations compare
  positions rather than anomalies.

## 14. Related lessons

- [01 Gravity Fieldwork: Loops, Drift, Base Stations, Ties](01-gravity-fieldwork.md) —
  where the elevation sensitivity enters the accuracy budget.
- [02 Magnetic Fieldwork: Diurnal Variation, Leveling, Gradients](02-magnetic-fieldwork.md) —
  the survey whose height sensitivity is small.
- [04 Field Data QC for Potential-Field Surveys](04-field-data-qc-gravmag.md) —
  the statistics that reveal a positioning blunder.
- [07-04-02 Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](../../07-gravity-geodesy/04-geodesy-reference-frames/02-height-systems.md) —
  the height systems in full.
- [05-05-04 Positioning with GNSS/DGPS and Static Corrections](../../05-core-geophysics/05-survey-design-and-acquisition/04-positioning-gnss.md) —
  the survey-design treatment.

## 15. Self-assessment checklist

- [ ] I can compute the free-air, Bouguer and combined elevation gradients.
- [ ] I can convert a target anomaly into an elevation specification.
- [ ] I can compute the latitude gradient and a position specification.
- [ ] I can state the magnetic height sensitivity and its insignificance.
- [ ] I can separate random from systematic GNSS error.
- [ ] I can compute the anomaly error from a geoid mistake.
