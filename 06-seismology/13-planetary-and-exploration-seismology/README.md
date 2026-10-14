# Module 06-13 — Planetary and Applied Seismology Frontiers

**Stages:** doctoral → research · **Prerequisites:** modules 06-01, 06-02 and
06-10; basic statistical inference.

This module is about doing seismology where a seismologist does not get to choose
the experiment. On a planetary surface there is one station, or a handful, and no
second chance; on an ice sheet the material is a slow, noisy waveguide that moves
while you measure it; on a volcano the source is a resonator whose properties
change between events and the deliverable is a decision, not a number; in a
fibre the sensor measures a spatial derivative of displacement along one
direction and nothing else. Each of the four lessons takes one of those settings
and derives what its geometry permits — and, more importantly, what it forbids.

The module's central honest difficulty is that **in every one of these settings
the observable is conditional on a model**, and the conditioning is not a caveat
but the dominant error term. A single-station hypocentre is a curve unless the
velocity model is known, and a 1% error in $V_p/V_s$ moves the distance by about
2.3%. An inverted ice thickness is a velocity assumption, because the dispersion
curve constrains thickness and layer velocity together. An LP event's $Q$ is a
path-averaged quantity unless the path and the other modes are accounted for. A
DAS amplitude is a phase velocity in disguise. Every lesson therefore forces the
same question: *which measurement would make this answer independent of the
assumption I just made?* — and, where no such measurement exists, states that
explicitly rather than quoting a number.

All models and data in this module are **SYNTHETIC**. No real station, event,
waveform, glacier, volcano, fibre or planetary dataset is used, and no published
number is quoted. The missions named in lesson 01 are named because the lesson
exists to explain the method they use, not as sources of data.

## Learning objectives

By the end of this module you will be able to:

1. Derive the range–depth trade-off of a single station, quantify the velocity
   dependence of the resulting location, and construct the family of models that
   fit one record exactly.
2. Compute the fractional polarisation sensitivity $2/\sin 2i$, identify the
   geometry in which it is weak, and explain why a second station acts through
   coverage rather than count.
3. Compute ice velocities from its elastic moduli, and derive the Love-wave
   dispersion relation for a slow layer over a fast half-space.
4. Measure a thickness–velocity trade-off on a synthetic dispersion curve and
   state the band, substrate assumption and tolerance under which it holds.
5. Derive the spectral signature of a damped oscillator, and recover $Q$ from a
   measured bandwidth with its bias regime stated.
6. Quantify an RSAM detector's latency–false-alarm trade-off and design a
   monitoring rule whose performance is stated at the relevant base rate.
7. Derive the DAS gauge-length response, directivity and aliasing relations, and
   specify the three sampling parameters of a deployment for a stated target.
8. State, for each setting, which quantity is a measurement and which is a model
   assumption.

## Prerequisites

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  elastic moduli, P and S waves, surface-wave dispersion.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  ray geometry and slowness, used in the straight-ray limit in lesson 01.
- [06-10 Refraction and Near-Surface Seismology](../10-refraction-and-near-surface-seismology/README.md) —
  array dispersion measurements, the terrestrial version of lessons 02 and 04.
- [04-08 Planetary Science and Comparative Planetology](../../04-earth-science-geology/08-planetary-science/README.md) —
  the bodies and missions whose interiors these methods target.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Planetary Seismology: InSight and Lunar Seismic Experiments](01-planetary-seismology.md) | doctoral | One station measures a range, not a location; a 1% velocity error moves the distance by 2.3% |
| 02 | [Glacial and Cryoseismology: Icequakes and Calving](02-glacial-seismology.md) | doctoral | Ice is a waveguide; the dispersion constrains thickness and velocity jointly — and the joint constraint is tighter than the folklore |
| 03 | [Volcano Seismology: LP Events, Tremor and Eruption Forecasting](03-volcano-seismology.md) | doctoral | An LP is a resonance with two parameters; a precursor's skill is precision at a base rate, not recall |
| 04 | [Distributed Acoustic Sensing: A New Observational Regime](04-distributed-acoustic-sensing.md) | research | DAS measures axial strain over a gauge along one direction: a wavenumber filter with a $\cos^{2}\theta$ directivity and a hard aliasing limit |

## Suggested path

**If you are new to these settings:** lessons 01–04 in order. Lesson 01 is the
cleanest statement of the module's theme because its geometry is the simplest;
lesson 04 is the most mechanical and the easiest to verify.

**If you work on hazard or monitoring:** 03 in full, then 01 §4–§6 (detection and
geometry limits) and 02 §6 (repeating sources and differential monitoring).

**If you are preparing a research project:** 02 §4 (what a trade-off measurement
actually says) and 04 §6 (why a gauge-length choice depends on the detector, not
on the site) are the two results most likely to change a published workflow.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-planetary-seismology.md`](01-planetary-seismology.md) | Lesson 01 |
| [`02-glacial-seismology.md`](02-glacial-seismology.md) | Lesson 02 |
| [`03-volcano-seismology.md`](03-volcano-seismology.md) | Lesson 03 |
| [`04-distributed-acoustic-sensing.md`](04-distributed-acoustic-sensing.md) | Lesson 04 |
| [`exercises/01-planetary-seismology-exercises.md`](exercises/01-planetary-seismology-exercises.md) | Exercises, lesson 01 |
| [`exercises/01-planetary-seismology-solutions.md`](exercises/01-planetary-seismology-solutions.md) | Worked solutions, lesson 01 |
| [`exercises/02-glacial-seismology-exercises.md`](exercises/02-glacial-seismology-exercises.md) | Exercises, lesson 02 |
| [`exercises/02-glacial-seismology-solutions.md`](exercises/02-glacial-seismology-solutions.md) | Worked solutions, lesson 02 |
| [`exercises/03-volcano-seismology-exercises.md`](exercises/03-volcano-seismology-exercises.md) | Exercises, lesson 03 |
| [`exercises/03-volcano-seismology-solutions.md`](exercises/03-volcano-seismology-solutions.md) | Worked solutions, lesson 03 |
| [`exercises/04-distributed-acoustic-sensing-exercises.md`](exercises/04-distributed-acoustic-sensing-exercises.md) | Exercises, lesson 04 |
| [`exercises/04-distributed-acoustic-sensing-solutions.md`](exercises/04-distributed-acoustic-sensing-solutions.md) | Worked solutions, lesson 04 |
| [`code/planetary_single_station_demo.py`](code/planetary_single_station_demo.py) | Single-station trade-off, polarisation, coverage, azimuth |
| [`code/ice_dispersion_demo.py`](code/ice_dispersion_demo.py) | Ice moduli, Love dispersion, thickness–velocity inversion |
| [`code/volcano_tremor_forecast_demo.py`](code/volcano_tremor_forecast_demo.py) | LP resonance, RSAM trade-off, base-rate experiment |
| [`code/das_interrogation_demo.py`](code/das_interrogation_demo.py) | Gauge response, directivity, aliasing, strain–velocity, SNR |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 06-seismology/13-planetary-and-exploration-seismology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python planetary_single_station_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ice_dispersion_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python volcano_tremor_forecast_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python das_interrogation_demo.py
```

Every demo prints labelled results **with units** and exits 0. The two demos
written for lessons 03 and 04, and the planetary demo, use the fixed seed
`20261014`; the ice-dispersion demo is deterministic and needs no seed. They are
print-only — no plots — and require no network access. Three finish in seconds;
the ice dispersion demo solves the dispersion relation for every point of a
two-parameter search grid and takes about two minutes, so start it before reading
lesson 02.

## Mastery checkpoint

Complete this without notes:

> A single station on a planetary surface records an S−P time of
> $3.50\ \mathrm{s}$ and an incidence angle of $50^{\circ}$, with
> $V_p = 6.00\ \mathrm{km\,s^{-1}}$, $V_s = 3.50\ \mathrm{km\,s^{-1}}$ and a pick
> uncertainty of $0.05\ \mathrm{s}$. **(a)** Compute the slant range and its
> uncertainty, with units. **(b)** Compute $\Delta$ and $h$ and state which of the
> two the S−P time alone determines. **(c)** Estimate the distance error caused by
> a $2\%$ error in $V_p/V_s$, and compare it with the pick-limited uncertainty.
> **(d)** A fibre nearby measures Rayleigh waves from $2$ to $20\ \mathrm{Hz}$ at
> $250$ to $1200\ \mathrm{m\,s^{-1}}$: specify the channel spacing and gauge length
> you would use, with the arithmetic. **(e)** For one of the four lessons in this
> module, state the single measurement that would remove its main assumption.

Worked arithmetic for (a)–(c) is in the
[lesson-01 solutions](exercises/01-planetary-seismology-solutions.md), and for
(d) in the
[lesson-04 solutions](exercises/04-distributed-acoustic-sensing-solutions.md);
the underlying derivations are in the lesson-01 and lesson-04 §8 examples.

## Common pitfalls across this module

1. **Quoting an answer whose dominant error is an unstated model assumption** —
   the velocity model, the substrate, the coupling, the path.
2. **Treating a geometry-limited answer as a precision-limited one.** Pick
   quality is rarely the limit in this module.
3. **Assuming a trade-off without measuring it.** Lesson 02 measures a trade-off
   that does *not* absorb a 5% velocity error in its stated configuration.
4. **Reporting recall where precision is what an operator experiences.**
5. **Choosing a DAS gauge length, or an RSAM window, by habit** rather than
   against a stated band, detector and cost.
6. **Reading an aliased branch as a slow wave**, in either space or time.
7. **Forgetting that the sources in this module are the experiment**: repeating
   sources, calving events and LP resonators each determine what can be measured.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the mechanics behind ice velocities, LP resonances and DAS strain.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  the path effects that masquerade as source or material properties.
- [06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md) —
  the statistical machinery behind lesson 03's base-rate analysis.
- [06-07 Ambient Noise and Seismic Interferometry](../07-ambient-noise-and-interferometry/README.md) —
  the technique that turns a permanent fibre or a single station into a
  monitoring instrument.
