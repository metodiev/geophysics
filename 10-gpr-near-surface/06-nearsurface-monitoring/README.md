# Module 10-06 — Near-Surface Monitoring and Time-Lapse

**Stages:** doctoral · **Prerequisites:** the other modules of this folder,
[10-05](../05-other-near-surface-methods/README.md) in particular, plus
[05-02-03](../../05-core-geophysics/02-geophysical-fields-and-observables/03-noise-and-drift.md)
and the DC-resistivity module
[09-02](../../09-electrical-em-methods/02-dc-resistivity/README.md).

This module is about the difference between two surveys of the same ground. It is
written at doctoral level because that difference is where the difficulty of
near-surface geophysics concentrates: the signal is one or two per cent, the
repeatability is one per cent, and the environment changes in between. Every lesson
therefore ends in a **number that decides something** — a detection threshold, a
survey interval, a false-alarm rate, or a passage duration — rather than in an
interpretation.

The central honest difficulty is that a change is never measured in isolation. A
monitoring survey measures the sum of the target change, the environmental change
(temperature, moisture, water table) and the change in the measurement itself
(coupling, geometry, instrument drift). The lessons separate them by design rather
than by assertion: a reference site, an independent measurement of the confounder,
a reciprocity check, and a repeatability figure measured at each epoch rather than
inherited from the baseline. Where a separation is impossible — a target and a
confounder that respond at the same depth and the same timescale — the lesson says
so, and quantifies what it costs.

A second theme is that **the statistics is part of the physics**. A permanent array
makes hundreds or thousands of measurements, so a threshold applied to each one
individually generates false anomalies with near-certainty; a plume that passes
between two surveys is not measured as small but as nothing; a detection claim at
the threshold is wrong half the time. These are not caveats appended to the
interpretation — they determine whether the interpretation is possible at all.

All models and data in this module are **SYNTHETIC**. The velocities, path lengths,
conductivities, front depths, electrode spacings, porosities, dispersivities, noise
levels and survey intervals are chosen teaching values. They are not measurements,
not site parameters and not calibrations, and no field site is modelled.

## Learning objectives

By the end of this module you will be able to:

1. **Measure** repeatability as an NRMS between independent repeats, and **state**
   the detection threshold it implies for a given observable.
2. **Derive** the resolution of a relative velocity change from a travel-time
   measurement and from a coda-wave stretching measurement, and **compute** both
   for a stated geometry.
3. **Quantify** the environmental aliasing between a target change and a
   temperature or moisture change, and **design** the defence for it.
4. **Show**, with a computed rejection rate, that separating a distributed change
   from a localised one is governed by depth coverage.
5. **Verify** a two-dimensional DC-resistivity forward model against the analytic
   half-space array factor, and **use** it to compute the anomaly of a wetting
   front at a stated depth.
6. **Choose** an electrode spacing from the depth of the feature to be watched, and
   **quantify** the cost of choosing it too small or too large.
7. **Compute** the family-wise false-alarm rate of a threshold applied to many
   measurements, and the amplitude penalty of correcting for it.
8. **Predict** the arrival time and passage duration of a contaminant plume, and
   **state** the survey interval that samples it without aliasing.
9. **State** a detection claim with its power, and **name** the measurements that
   convert a conductivity change into a concentration or a safety statement.

## Prerequisites

- [10-05 Other Near-Surface Methods](../05-other-near-surface-methods/README.md) —
  the properties being monitored, and the petrophysical relations that convert
  them into state variables.
- [10-04 Near-Surface Seismic and Geotechnical Methods](../04-near-surface-seismic-and-geotechnical/README.md) —
  what an engineer does with a $v_s$ profile.
- [05-02-03 Noise and Drift](../../05-core-geophysics/02-geophysical-fields-and-observables/03-noise-and-drift.md) —
  the random-versus-systematic distinction that decides everything in this module.
- [09-02 DC Resistivity](../../09-electrical-em-methods/02-dc-resistivity/README.md) —
  arrays, apparent resistivity and ERT inversion.
- [14-05 Time-Lapse and Monitoring Hydrogeophysics](../../14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/README.md) —
  the hydrological counterpart.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Time-Lapse Near-Surface Geophysics](01-time-lapse-nearsurface.md) | doctoral | Repeatability is a design quantity; coda stretching beats picking by two orders of magnitude; coverage — not precision — separates distributed from localised change |
| 02 | [Monitoring Dams, Embankments and Foundations](02-geotechnical-monitoring.md) | doctoral | The spacing chooses the depth you defend; multiplicity turns noise into findings unless the threshold is corrected |
| 03 | [Monitoring Contaminant Transport with Geophysics](03-contaminant-monitoring.md) | doctoral | The physics of transport sets the survey interval; conductivity is a mixture of plume, background and calibration; a null result needs a detection limit |

## Suggested path

**If you are new to monitoring:** lesson 01 in full, running the demonstration.
It contains the framework (repeatability, threshold, aliasing) that the other two
apply, and every number in it is reproduced by the code.

**If you work on embankments or dams:** lesson 02, with its forward model. It is
the only lesson in this curriculum that verifies a Wenner array factor by hand and
numerically, and it is the one whose design tables an engineer will ask for.

**If you work on contaminated sites or hydrogeology:** lesson 03, which is the only
lesson here whose target is *designed* and therefore predictable. Read it together
with [14-04](../../14-hydrology-hydrogeophysics/04-contaminant-and-environmental/README.md).

**If you are preparing a monitoring project:** read 01 §3.3–3.5 and then the
design sections of whichever of 02 and 03 matches the site, and write the
feasibility table (detectable change versus depth, and the number of tests) before
installing anything.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-time-lapse-nearsurface.md`](01-time-lapse-nearsurface.md) | Lesson 01 |
| [`02-geotechnical-monitoring.md`](02-geotechnical-monitoring.md) | Lesson 02 |
| [`03-contaminant-monitoring.md`](03-contaminant-monitoring.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 10-gpr-near-surface/06-nearsurface-monitoring/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python time_lapse_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geotechnical_monitoring_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python contaminant_monitoring_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0. The
geotechnical demo is the slowest at about seven seconds, because it assembles and
solves a sparse finite-difference system for each of several models.

## Mastery checkpoint

Complete this without notes:

> A monitoring programme has a 25 m path in a $400\ \mathrm{m\,s^{-1}}$ medium, a
> coda of 2 s, a picking error of $0.4\ \mathrm{ms}$, a repeatability of
> $\mathrm{NRMS} = 15\%$, and a conductivity array with 250 quadrupoles per epoch
> at a $1\%$ measurement error. **(a)** Compute the picking-based velocity-change
> resolution and state whether a $0.2\%$ target change is detectable by picking.
> **(b)** Estimate the coda-based resolution and state the assumption that makes it
> applicable. **(c)** Compute the per-measurement and family-wise thresholds for
> the conductivity data, and the change amplitude the corrected threshold demands.
> **(d)** State one confounder that affects both the seismic and the electrical
> measurement, and the measurement that identifies it. **(e)** State the survey
> interval you would choose for a plume expected to pass a well over three months,
> and why.

A worked version of (a)–(c) appears in the lesson-01 and lesson-02 exercise
solutions.

## Common pitfalls across this module

1. **A change without a repeatability.** Every detection claim needs the
   repeatability of the *same epoch's* measurement, not of the baseline's.
2. **A threshold without a multiplicity count.** Hundreds of measurements at
   $2\sigma$ produce false anomalies with near-certainty.
3. **A survey interval chosen by budget rather than by the passage duration.** The
   resulting under-estimate is a bias, and it is invisible in the data.
4. **Designing for amplitude only.** Depth coverage and spatial coherence decide
   whether a change can be *located*, not merely detected.
5. **Reporting a concentration or a factor of safety from a property change.**
   Geophysics measures a property; a water sample, a background station and a
   mechanical model supply the rest.
6. **Monitoring one depth.** Two interleaved spacings cost little more than one and
   make the difference between detecting a change and localising it.

## Related modules

- [10-05 Other Near-Surface Methods](../05-other-near-surface-methods/README.md) —
  the properties and the petrophysical relations this module monitors over time.
- [10-02 GPR Acquisition and Processing](../02-gpr-acquisition-and-processing/README.md) —
  what a time-lapse GPR survey adds (and why its repeatability is usually worse).
- [10-01 GPR Principles](../01-gpr-principles/README.md) — the same physics, one
  epoch at a time.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — 4-D inversion,
  regularisation and the resolution of a change model.
- [14-05 Time-Lapse and Monitoring Hydrogeophysics](../../14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/README.md) —
  the hydrological interpretation of a monitored change.
