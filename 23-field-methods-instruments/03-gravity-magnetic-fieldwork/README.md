# Module 23-03 — Gravity and Magnetic Fieldwork

**Stages:** advanced → graduate · **Prerequisites:** modules 23-01 and 23-02;
[07-02-03 Survey Procedures: Loops, Drift, Repeatability and Ties](../../07-gravity-geodesy/02-gravity-instruments-and-surveys/03-survey-procedures.md).

This module is about the four things that stand between a potential-field reading
and an anomaly: **time**, **level**, **position** and **height**. Each lesson takes
one of them, computes its sensitivity, and measures the residual that a stated
correction leaves behind. The organising idea is that a potential-field survey is a
*differential* measurement in both space and time, and that the time derivative of
the field is often comparable with the anomaly it is being used to find.

The module therefore treats the corrections as measurements with residuals rather
than as procedures that either were or were not carried out. A two-tie linear drift
correction leaves 0.0732 mGal RMS of a 0.1230 mGal variation; adding a midpoint tie
cuts it to 0.0160 mGal. A two-tie diurnal correction removes 49 % of a synthetic
magnetic variation; hourly occupations remove 99.8 % of it. A 0.1 m elevation error
is 0.0197 mGal of false anomaly, and a 30 m geoid mistake is 5.9 mGal. Each of
those numbers changes what a survey is allowed to claim, and each is computable
before mobilisation.

The second theme is that **the largest error terms are assumptions, not
instruments**. In the module's error budget the reading repeatability contributes
1.9 % of the variance while the Bouguer density assumption contributes 30 % and the
elevation accuracy 29 %. The practical consequence is a rule for where to spend
field effort: measure the density and the heights before buying a better
gravimeter.

All numbers in this module are **SYNTHETIC**, or derived from standard formulas
whose constants are stated in the lesson (the free-air gradient, the Bouguer
gradient, the latitude gradient, the dipole field). No measured instrument drift,
field reading, published anomaly, geoid model or survey accuracy figure is used or
reproduced.

## Learning objectives

By the end of this module you will be able to:

1. **Distinguish** instrument drift, tidal variation and reading noise, and
   **compute** the residual of a drift correction from base ties.
2. **Compute** the magnetic diurnal residual of a linear and of an hourly base
   correction, and **choose** a looping interval from a target accuracy.
3. **Compute** elevation, latitude and height sensitivities for both gravity and
   magnetics, and **convert** a target anomaly into a positioning specification.
4. **Separate** the random and systematic parts of a GNSS error budget and
   **state** what averaging cannot remove.
5. **Compute** mis-tie statistics, fit a line-level adjustment and **test** the
   residual against the reading noise.
6. **Decompose** airborne cross-over errors into a removable level and an
   irreducible scatter.
7. **Build** an error budget in quadrature, **identify** the dominant term, and
   **state** what it implies for the survey's claims.
8. **Design** the looping, tying and positioning plan of a survey from its target
   accuracy.

## Prerequisites

- [23-01-03 Field Notebooks, Metadata and Data Provenance](../01-field-safety-and-planning/03-field-notebooks.md) —
  the record that makes a drift or levelling correction possible.
- [23-02-01 Seismometers: Broadband, Short-Period, Geophones, MEMS](../02-seismic-instruments-and-fieldwork/01-seismometers.md) —
  the previous module's treatment of instrument response.
- [07-02-03 Survey Procedures: Loops, Drift, Repeatability and Ties](../../07-gravity-geodesy/02-gravity-instruments-and-surveys/03-survey-procedures.md) —
  the gravity survey procedure in context.
- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md) —
  where the elevation sensitivities come from.
- [08-03-01 Magnetic Anomaly Physics and Remanent vs Induced Magnetisation](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/01-magnetic-anomaly-basics.md) —
  what a magnetic survey is measuring.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Gravity Fieldwork: Loops, Drift, Base Stations, Ties](01-gravity-fieldwork.md) | advanced | A two-tie linear correction left 0.0732 mGal RMS; one midpoint tie cut it 4.6× for a few minutes of field time |
| 02 | [Magnetic Fieldwork: Diurnal Variation, Leveling, Gradients](02-magnetic-fieldwork.md) | advanced | A two-tie correction removed 49 % of the diurnal variation; hourly ties removed 99.8 %; mis-tie scatter of 7.5 nT is a levelling problem, not noise |
| 03 | [Positioning and Elevation Determination in the Field](03-positioning-in-field.md) | advanced | 0.1967 mGal/m of elevation sensitivity, a 30 m geoid mistake worth 5.9 mGal, and a magnetic height sensitivity of 0.02 nT/m |
| 04 | [Field Data QC for Potential-Field Surveys](04-field-data-qc-gravmag.md) | graduate | Cross-over RMS 9.123 nT = 8.155 nT removable level + 4.099 nT scatter; the error budget is dominated by assumptions |

## Suggested path

**If you are planning your first gravity survey:** read 01 in full, then 03 §2–§3
for the elevation and latitude specifications, then 04 §6 for what the error budget
will look like.

**If you are planning a magnetic survey:** 02 §§2–4, then 04 §5 for the cross-over
statistics if the survey is airborne.

**If you are processing someone else's survey:** 04 §2 (closures), §4 (leveling)
and §6 (budget) are the three things to reconstruct before interpreting anything.

**If you are preparing a research project:** 01 §6 and 03 §5–§6 for the design
arithmetic, plus the ★★★ exercises of all four lessons, which ask for plans and
audits rather than for calculations.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-gravity-fieldwork.md`](01-gravity-fieldwork.md) | Lesson 01 |
| [`02-magnetic-fieldwork.md`](02-magnetic-fieldwork.md) | Lesson 02 |
| [`03-positioning-in-field.md`](03-positioning-in-field.md) | Lesson 03 |
| [`04-field-data-qc-gravmag.md`](04-field-data-qc-gravmag.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/gravity_fieldwork_demo.py`](code/gravity_fieldwork_demo.py) | Drift and tide model, residual of two-, three- and four-tie corrections, closure versus duration and time of day, repeatability |
| [`code/magnetic_fieldwork_demo.py`](code/magnetic_fieldwork_demo.py) | Diurnal residual of linear and hourly corrections, mis-tie statistics, repeatability, half-width depth estimate |
| [`code/positioning_in_field_demo.py`](code/positioning_in_field_demo.py) | Free-air and Bouguer elevation sensitivity, latitude gradient, magnetic vertical gradient, GNSS accuracy and geoid error |
| [`code/field_data_qc_gravmag_demo.py`](code/field_data_qc_gravmag_demo.py) | Loop closures, pooled repeatability, leveling adjustment, cross-over decomposition, error budget |

## How to run the demos

Use the project virtual environment:

```bash
cd 23-field-methods-instruments/03-gravity-magnetic-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_fieldwork_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_fieldwork_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python positioning_in_field_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_data_qc_gravmag_demo.py
```

Each demo prints labelled results under numbered section banners, starts from
`np.random.default_rng(20261014)`, uses no network and no file I/O, prints a
`SYNTHETIC` provenance line and exits 0. All four run in under 0.2 s.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A microgravity survey targets a 0.02 mGal anomaly over a 1 km² area with a
> gravimeter whose drift is 0.010 mGal/h. **(a)** Compute the elevation accuracy the
> target requires on the Bouguer anomaly, and the north–south position accuracy at
> 45° latitude if that term is allowed half the budget. **(b)** Choose a loop
> duration and the number of base ties, justifying both from the drift rate and a
> 0.10 mGal semi-diurnal tidal amplitude. **(c)** The survey's GNSS provides
> ellipsoidal heights and the geoid undulation is 22 m: compute the error this would
> introduce and state two remedies. **(d)** Compute the total error budget given the
> repeatability you would measure from five repeats and a Bouguer density
> uncertainty of 0.02 mGal, and name the dominant term.
> Worked versions of (a)–(d) appear in the ★★★ solutions.

## Common pitfalls across this module

1. **Calling a drift correction a tidal correction.** A straight line through two
   base occupations removes the linear part and leaves the rest; the residuals are
   0.0732 mGal in gravity and 8.600 nT in magnetics in this module's models.
2. **Quantifying accuracy with one number.** The instrument contributed 1.9 % of an
   error budget whose dominant terms were the density assumption and the elevation.
3. **Rejecting loops by closure value.** It removes evidence about the drift and
   improves only the summary statistic.
4. **Using ellipsoidal heights in a gravity reduction.** A 30 m undulation error is
   5.9 mGal.
5. **Trusting GNSS averaging to converge on the truth.** Averaging removes random
   error only, and a survey can be precisely biased.
6. **Treating mis-tie scatter as noise.** It is usually a levelling error and is
   removable; the test is whether the post-adjustment residual matches the reading
   noise.
7. **Applying a levelling adjustment with implausible offsets.** The adjustment can
   spread a blunder across the whole survey instead of removing it.

## Related modules

- [23-01 Field Safety, Planning and Logistics](../01-field-safety-and-planning/README.md) —
  the planning discipline these surveys inherit.
- [23-02 Seismic Instruments and Fieldwork](../02-seismic-instruments-and-fieldwork/README.md) —
  the time-series side of instrument behaviour.
- [23-04 Electrical and EM Fieldwork](../04-electrical-em-fieldwork/README.md) —
  where coupling and contact resistance replace drift as the dominant nuisance.
- [07-02 Gravity Instruments and Surveys](../../07-gravity-geodesy/02-gravity-instruments-and-surveys/README.md) —
  the instruments and the survey procedure in full.
- [08-03 Magnetic Anomalies and Modelling](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/README.md) —
  what the reduced anomalies become.
