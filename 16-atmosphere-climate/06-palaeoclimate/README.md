# Module 16-06 — Palaeoclimate

**Stages:** doctoral → research · **Prerequisites:** module 16-02 (radiation and
energy balance), module 16-04 (feedbacks and the carbon cycle); the climate-model
material of module 16-05.

Palaeoclimate is the part of climate science in which nothing can be measured
directly. Every number in a reconstruction is the output of a model: a
fractionation law, a calibration regression, a dating algorithm or a dynamical
model. This module is built around that fact rather than around a narrative of
past climates. Its subject is the *inference* — how a proxy becomes a
temperature, how a model becomes a comparison, how a threshold becomes a tipping
point, and how a periodic forcing becomes a cycle — and its recurring result is
that the dominant uncertainty is usually the modelling assumption rather than the
measurement noise.

Three structural ideas run through the four lessons. The first is **degeneracy**:
one isotope value is consistent with a curve of source-composition and
temperature pairs (measured in lesson 01 at about $8.3\ \mathrm{K}$ of implied
temperature per per mil of source uncertainty), so a single proxy constrains a
set, not a point. The second is **calibration transport**: a relationship fitted
in one climate regime carries an implicit claim that it holds in another, and
when the claim fails the error appears as a bias that the calibration's own
scatter cannot detect. The third is **nonlinearity**: a threshold turns a weak,
quasi-periodic forcing into an abrupt, asymmetric response, and it also turns a
model's closure parameters into controls on the answer rather than nuisances in
it.

All models and data in this module are **SYNTHETIC**. The fractionation factor,
the proxy system model, the box model and the ice model are chosen teaching
constructions; the climate fields and the "proxies" are generated. No real
ice-core, sediment, speleothem or isotope record is used, and no published
calibration, period, threshold or spectral peak is quoted. Where a threshold or a
period appears, it is either printed by a demo in this module or an exact
standard constant stated with its unit.

## Learning objectives

By the end of this module you will be able to:

1. **Define** a proxy system model and **state** the three links a calibration
   must bridge between climate and measurement.
2. **Derive** the Rayleigh distillation equations and **measure** the
   $\mathrm{d}\delta/\mathrm{d}T$ slope of the resulting calibration.
3. **Quantify** the structural uncertainty of a fractionation parameterisation
   and the degeneracy between source composition and temperature.
4. **Write** a proxy system model including an unmodelled local factor, and
   **distinguish** the errors that appear as bias from those that appear as
   scatter.
5. **Derive** the scalar optimal-interpolation update, **interpret** the gain, and
   **demonstrate** that the update cannot remove a proxy's systematic bias.
6. **Distinguish** abruptness of forcing from abruptness of response, and
   **define** bistability, a fold bifurcation and hysteresis.
7. **Measure** a hysteresis loop in a two-box circulation model and **classify**
   the multiple steady solutions by stability.
8. **Quantify** how a tipping threshold moves when one closure parameter changes.
9. **Measure** the spectral signature of a threshold response and **explain** why
   a nonlinear response can concentrate variance at a period the forcing barely
   contains.
10. **State** the assumptions under which each of these model results is
    defensible, and the observations that would falsify them.

## Prerequisites

- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  the greenhouse effect and the energy budget the models solve.
- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  feedbacks, sensitivity, internal variability and the carbon cycle.
- [16-05 Climate Models](../05-climate-models/README.md) — closures, ensembles,
  evaluation and the model hierarchy used throughout.
- [18-05 Bayesian Inversion and Inference](../../18-inverse-problems/05-bayesian-inversion/README.md) —
  the prior/likelihood/posterior structure of lesson 02 in general form.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Palaeoclimate Proxies: Ice Cores, Sediments, Isotopes](01-paleoclimate-proxies.md) | doctoral | A proxy is a process; one value constrains a curve, not a temperature |
| 02 | [Model-Data Comparison in Palaeoclimate](02-paleoclimate-model-data.md) | research | The update reduces scatter and cannot see bias |
| 03 | [Abrupt Climate Change and Tipping Elements](03-abrupt-climate-change.md) | research | Thresholds are properties of the model and its closures |
| 04 | [Pleistocene Glacial Cycles and Orbital Forcing](04-pleistocene-cycles.md) | doctoral | A threshold moves variance to a period the forcing barely contains |

## Suggested path

**New to palaeoclimate:** lessons 01 and 02 in order. Lesson 01 establishes what a
proxy measures and why the calibration is a model; lesson 02 shows what goes
wrong when that model is used in a different climate.

**Interested in abrupt change:** start with 03, then read 04 as its spectral
counterpart — the same nonlinearity, measured in the frequency domain rather than
in the phase plane.

**Preparing research:** 01 §5–6 (structural uncertainty and degeneracy), 02 §5
(the biased-proxy experiment), 03 §6 (closure dependence of thresholds) and 04
§6–7 (what a mechanism demonstration does and does not show).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-paleoclimate-proxies.md`](01-paleoclimate-proxies.md) | Lesson 01 |
| [`02-paleoclimate-model-data.md`](02-paleoclimate-model-data.md) | Lesson 02 |
| [`03-abrupt-climate-change.md`](03-abrupt-climate-change.md) | Lesson 03 |
| [`04-pleistocene-cycles.md`](04-pleistocene-cycles.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and xarray:

```bash
cd 16-atmosphere-climate/06-palaeoclimate/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python paleoclimate_proxies_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python paleoclimate_model_data_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python abrupt_climate_change_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python pleistocene_cycles_demo.py
```

Every demo prints labelled results with units, uses the fixed random seed
`np.random.default_rng(20261014)`, requires no network access, and exits 0. Each
one is print-only: there is no plotting, and every number quoted in a lesson can
be reproduced by running its demo.

## Mastery checkpoint

Complete this without notes.

> **(a)** An isotope value of $-25$ per mil is calibrated to a temperature under
> two defensible fractionation parameterisations that differ by $5.07\
> \mathrm{K}$. State which uncertainty this is, and why more samples of the same
> proxy cannot reduce it. **(b)** The same value is also consistent with a
> family of source compositions, with a measured sensitivity of about
> $8.3\ \mathrm{K}$ per per mil. State what a defensible uncertainty statement
> looks like. **(c)** In a two-box circulation model, three steady states exist
> for a range of freshwater forcing. State which is unstable and how you would
> demonstrate it numerically. **(d)** A threshold ice model with a
> $100\ \mathrm{ka}$ modulation in its forcing produces a response whose dominant
> period is $100\ \mathrm{ka}$ while the forcing's is $23.1\ \mathrm{ka}$. State
> what this establishes and what it does not.

Worked versions of (a)–(b) appear in the lesson-01
[solutions](exercises/01-paleoclimate-proxies-solutions.md), and of (c)–(d) in
the lesson-03 and lesson-04
[solutions](exercises/03-abrupt-climate-change-solutions.md).

## Common pitfalls across this module

1. **Treating a proxy as an instrument.** A proxy records a process; the
   calibration is a model of that process.
2. **Quoting a regression standard error as the total uncertainty.** Structural
   uncertainty dominates and does not shrink with more data.
3. **Transporting a calibration across a change of regime.** The error appears as
   a bias and is invisible to the residual scatter.
4. **Reporting a posterior spread as the answer's accuracy.** The update reduces
   scatter and cannot detect bias.
5. **Quoting a model threshold as an Earth threshold.** The threshold is
   conditional on closures that the demonstration measures.
6. **Taking the mean of a bistable system.** The mean lies between the branches
   and describes neither.
7. **Reading a mechanism demonstration as an explanation.** It shows what is
   possible; identifying what happened needs independent evidence.

## Related modules

- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md).
- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md).
- [16-05 Climate Models](../05-climate-models/README.md) — the model hierarchy and
  evaluative framework applied here.
- [16-09 Geophysics Applied to Climate Science](../09-geophysics-and-climate/README.md) —
  borehole, seismic and geodetic records of past climate.
- [13-07 Tectonics, Surface Processes and Climate Coupling](../../13-geodynamics-tectonics/07-geomorphology-tectonics-climate/README.md) —
  the long-timescale coupling of solid Earth and climate.
- [15-06 Sea Level Change and Marine Records](../../15-oceanography-marine/06-sea-level-change-marine/README.md) —
  marine archives of the same history.
- [18-inverse-problems](../../18-inverse-problems/README.md) — degeneracy,
  regularisation and uncertainty, of which these lessons are worked examples.
