# Module 16-09 — Geophysics Applied to Climate Science

**Stages:** research · **Prerequisites:** module 16-09 draws on the measurement
foundations of folders 05–08 and on modules 16-07 and 16-08 in this folder.

This module is the return journey. Folders 05–14 use geophysics to measure the
solid Earth; here the same instruments — seismometers, gravimeters, GNSS
receivers, boreholes — are pointed at the climate system, and the question changes
from "what is down there?" to "what is happening, and how sure are we?" The
geophysics itself is unchanged: a receiver function is still a receiver function,
a gravity difference is still a gravity difference. What changes is the
**target**, which is dynamic, and the **reporting obligation**, which is a
monitoring and verification statement rather than a subsurface image.

The module is built around one honest difficulty, stated once and then met five
times: **every observable here is a proxy for a quantity the study actually
wants.** A seismic event count is a statement about a detector's threshold and
band before it is a statement about a glacier. A coda stretch is a change in
elastic properties, which four different mechanisms can produce. A gravity
anomaly is a mass, but turning it into an ice or groundwater attribution requires
a GIA model, a leakage operator and a density contrast — none of which the gravity
data measure. A borehole profile is a surface temperature history passed through a
low-pass filter whose inverse is ill posed. A reflectivity change is a saturation
and a geometry, tangled together.

Each lesson therefore separates **detection** from **quantification** and measures
the gap. That is this module's version of the curriculum's recurring theme, and it
is why every lesson ends with a statement of what is measured, what is inferred
and what is assumed.

**All models and data in this module are SYNTHETIC.** The seismic records, coda
waveforms, sea-level budget components, borehole profiles, rock properties,
plume geometries and hazard distributions are chosen teaching values, anchored
where appropriate on standard physical constants. No real station, glacier, tide
gauge, satellite mission, borehole, storage site, slope or published measurement
is used, and no published number is presented as a measurement.

## Learning objectives

By the end of this module you will be able to:

1. **Implement** a seismic event detector, **measure** its detection and
   false-alarm rates, and **state** why a catalogue is an operating point rather
   than a property of the target.
2. **Derive** the relation between a relative velocity change and a coda stretch,
   **measure** the change by a stretch search, and **report** its noise floor from
   the coda signal-to-noise ratio.
3. **Write** the sea-level budget, **test** its closure against the stated
   uncertainty, and **quantify** the bias from unmeasured vertical land motion and
   from a GIA correction.
4. **Compute** the record length required for a trend to be detectable, and
   **explain** why a trend's standard error falls as $n^{-3/2}$.
5. **Derive** the conductive Green's function for a surface temperature history,
   **quantify** the diffusion low-pass filter with depth, and **invert** a
   synthetic borehole profile with a stated truncation.
6. **Demonstrate** the ill-posedness of that inversion from its singular values,
   and **quantify** the practical amplification and the null direction.
7. **Apply** Gassmann fluid substitution to compute the seismic signature of CO2
   in a brine reservoir, including impedance and a reflectivity polarity flip.
8. **Compute** the gravity anomaly of a plume's mass deficit, and **quantify** how
   a geometry error propagates into an inferred mass.
9. **Compute** compound-hazard exceedance probabilities with a stated dependence,
   and **quantify** the return-period change under a sea-level rise.
10. **Compute** permafrost thaw settlement and an infinite-slope factor of safety,
    and **locate** the threshold crossing that makes each a hazard.
11. **State** the counterfactual behind any climate statement built on a
    geophysical observable.
12. **Write** a monitoring statement that separates measurement, inference and
    assumption, and reports the detection threshold alongside every estimate.

## Prerequisites

- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) —
  porosity, density and velocity relations, Gassmann and effective media.
- [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md) —
  the gravity products and error models behind the mass estimates.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md) —
  the catalogue, completeness and hazard-curve logic.
- [16-07 Extremes, Impacts and Attribution](../07-climate-extremes-and-attribution/README.md) —
  the attribution and risk framing these hazards feed.
- [16-08 Climate Observations and Data Products](../08-climate-observation-and-data/README.md) —
  the observational record and its processing.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Seismic and Geodetic Monitoring of Cryosphere Change](01-seismic-monitoring-climate.md) | research | A catalogue is an operating point; a velocity change is a state variable, not a mass |
| 02 | [Geodesy for Sea Level, Ice Mass and Water Storage](02-geodesy-climate.md) | research | Budget closure is judged against its uncertainty; corrections are not measurements |
| 03 | [Borehole Temperature Records of Past Climate](03-geothermal-climate-records.md) | doctoral | Diffusion is a low-pass filter and its inverse is ill posed; report a family of histories |
| 04 | [Geophysics for Carbon Capture and Storage Monitoring](04-geophysics-carbon-storage.md) | research | Detection is robust, quantification is assumption-laden; a $10\%$ depth error is a $21\%$ mass error |
| 05 | [Climate-Geohazard Interactions (Sea Level, Permafrost, Slopes)](05-climate-geohazards.md) | research | Climate enters as a boundary condition and the hazard is a threshold crossing |

## Suggested path

**If you are new to environmental geophysics:** lessons 01 and 02 in order,
running each demonstration. Lesson 02's budget arithmetic is the one you will
reuse most often.

**If you already work in exploration or global geophysics:** read 04 first — it is
the closest to familiar practice and it states the detection/quantification split
most sharply — then 03, which is the most mathematical, then 05.

**If you are preparing a monitoring or verification study:** 01 §2–4 (detector
operating points and noise floors), 02 §2–3 (land motion and correction
uncertainty), 04 §4 (depth-error amplification), and 05 §5 (counterfactuals),
plus the ★★★ exercises in every lesson.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-seismic-monitoring-climate.md`](01-seismic-monitoring-climate.md) | Lesson 01 |
| [`02-geodesy-climate.md`](02-geodesy-climate.md) | Lesson 02 |
| [`03-geothermal-climate-records.md`](03-geothermal-climate-records.md) | Lesson 03 |
| [`04-geophysics-carbon-storage.md`](04-geophysics-carbon-storage.md) | Lesson 04 |
| [`05-climate-geohazards.md`](05-climate-geohazards.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and xarray:

```bash
cd 16-atmosphere-climate/09-geophysics-and-climate/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_monitoring_climate_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geodesy_climate_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geothermal_climate_records_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geophysics_carbon_storage_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_geohazards_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), is print-only, requires no network access and
exits 0. Each runs in under two seconds.

## Mastery checkpoint

Complete this without notes:

> The demonstration's synthetic cryosphere is monitored by a detector with a
> stated threshold and by a coda-based velocity measurement, and the same planet
> has a sea-level budget and a permafrost column. **(a)** A detector finds
> $36/40$ events with $0$ false alarms on a noise-only record at one threshold,
> and $40/40$ with $15$ false alarms at another: state which operating point you
> would publish and why the choice must be declared. **(b)** A coda stretch of
> $0.05\%$ is recovered with a standard deviation of $2.9\times10^{-4}$ at high
> noise: decide whether the measurement resolves a seasonal cycle, and say what
> would improve it. **(c)** A budget has a residual of $+0.285\ \mathrm{mm\,yr^{-1}}$
> with $\sigma = 0.788\ \mathrm{mm\,yr^{-1}}$: decide whether it closes and give
> your criterion. **(d)** A gauge trends at $+4.504\ \mathrm{mm\,yr^{-1}}$ over
> land subsiding at $-1.50\ \mathrm{mm\,yr^{-1}}$: compute the absolute trend.
> **(e)** A plume-like mass deficit of $-1.173\times10^{10}\ \mathrm{kg}$ sits at
> $1800\ \mathrm{m}$: compute the gravity anomaly and state its depth scaling.
> **(f)** With $30\%$ excess ice and $0.8\ \mathrm{m}$ of new thaw, compute the
> settlement. **(g)** For each of (a)–(f), label the quantity as measured,
> inferred or assumed, and name the single observation that would most reduce the
> largest remaining uncertainty.

Parts (c) and (d) are worked in the lesson-02
[solutions](exercises/02-geodesy-climate-solutions.md); part (e) is worked in the
lesson-04 [solutions](exercises/04-geophysics-carbon-storage-solutions.md).

## Common pitfalls

1. **Publishing a detection catalogue without its operating point.** Threshold,
   band and window lengths decide the count.
2. **Quoting a velocity change without its noise floor.** The resolution is a
   ratio to the coda signal-to-noise ratio, not an absolute sensitivity.
3. **Judging a budget by its residual instead of its uncertainty.** Closure is a
   ratio, not a zero.
4. **Treating a correction as a measurement.** GIA and land motion carry their own
   modelled or measured errors, and they widen the budget.
5. **Inverting a borehole profile without regularisation or a truncation
   statement.** Unregularised inversion returned $31.8\ \mathrm{K}$ bins from a
   $2.75\ \mathrm{K}$ truth.
6. **Applying Gassmann outside its low-frequency, well-mixed regime.**
7. **Reporting a gravity-derived mass without the geometry assumption.** A $10\%$
   depth error became a $21\%$ mass error.
8. **Reading "the risk doubles" without the metric.** Joint and union
   probabilities changed by different factors.
9. **Omitting the counterfactual.** A climate statement about a hazard requires
   the world it is compared against.

## Related modules

- [16-07 Extremes, Impacts and Attribution](../07-climate-extremes-and-attribution/README.md) —
  what the monitoring results are used for: attribution and risk.
- [16-08 Climate Observations and Data Products](../08-climate-observation-and-data/README.md) —
  the calibration, homogenisation and uncertainty discipline this module inherits.
- [05 Core Geophysics](../../05-core-geophysics/README.md) — the property
  contrasts and interpretation practice underlying every observable here.
- [07 Gravity and Geodesy](../../07-gravity-geodesy/README.md) — the potential-field
  and reference-frame foundations of the mass measurements.
- [06 Seismology](../../06-seismology/README.md) — the detection, catalogue and
  inverse-theory practice the seismic monitoring applies.
- [13 Geodynamics and Tectonics](../../13-geodynamics-tectonics/README.md) — the
  longer-timescale surface processes behind the geohazards.
- [14 Hydrology and Hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) —
  the groundwater systems that complicate every gravity and pore-pressure
  interpretation here.
