# Module 25-01 — Beginner Projects

**Stages:** beginner · **Prerequisites:** folders
[01 Mathematics](../../01-mathematics/README.md),
[03 Scientific Computing](../../03-scientific-computing/README.md) and the
introductory parts of [05 Core Geophysics](../../05-core-geophysics/README.md)
and [07 Gravity and Geodesy](../../07-gravity-geodesy/README.md).

This module is where the curriculum stops teaching methods and starts asking for
**artefacts**. Each of its four lessons specifies a small project with a stated
question, a stated data source, a deliverable, a success criterion, a list of
failure modes and a rubric. Nothing here is new theory: units, plotting, shell
theory, Gutenberg-Richter statistics and the S−P distance have all appeared
earlier. What is new is that each is now the *whole* of a deliverable, judged on
whether it survives a reader who checks the units and the assumptions.

The organising idea is that **a beginner project is a specification, not an
example**. A specification says what to produce, what the pass condition is, and
how the work fails — and it does not show a finished answer. So every lesson
gives the derivation of the one formula the project needs, a worked numerical
example of that formula from the accompanying demonstration, and then a project
in which the reader applies it to their own data. The three failure modes listed
in each lesson are the ones that actually occur: mixing mGal with
$\mathrm{m\,s^{-2}}$, fitting a $b$-value below the completeness magnitude,
reporting a magnitude from a single record.

Provenance is stated per lesson and is deliberately mixed. The **real** projects
query an open archive — the USGS ANSS Comprehensive Earthquake Catalog through
the FDSN event service, and waveforms through the IRIS/EarthScope FDSN
dataselect service — and every number quoted in the prose comes from a
**SYNTHETIC** demonstration instead, so that the reader can reproduce the
arithmetic exactly without a network. The demonstrations are print-only, seeded
with `np.random.default_rng(20261014)`, run in under a second each and exit 0.

## Learning objectives

By the end of this module you will be able to:

1. **Convert** a field-sheet table to SI and **defend** every factor and unit in
   it.
2. **Derive and compute** the free-air gradient $2g/R$ and the Bouguer slab
   gradient $2\pi G\rho$ in mGal per metre.
3. **Query** an open catalogue or waveform archive and **record** the query so
   that another reader obtains the same rows.
4. **Estimate** a Gutenberg-Richter $b$-value with its magnitude of completeness
   and its standard error, and **measure** its sensitivity to the completeness
   assumption.
5. **Compute** gravity through a spherically layered Earth from the shell
   theorem, and **locate** the radius of maximum $g$.
6. **Describe** a seismogram by the five quantities one record determines, and
   **name** the four it does not.
7. **Grade** your own artefact against a rubric that requires a unit, an
   uncertainty and a stated assumption for every number.

## Prerequisites

- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md) —
  the factor table and the dimensional-homogeneity rule.
- [01-04-04 Geographic Coordinates, Datums and Map Projections](../../01-mathematics/04-geometry-and-coordinates/04-geographic-coordinates.md) —
  what a map projection does to a density.
- [03-04-06 Case Study: Earthquake Catalogue Wrangling](../../03-scientific-computing/04-pandas/06-earthquake-catalog-pandas.md) —
  catalogues as tables.
- [03-05-01 Matplotlib Figure/Axes Model and Anatomy of a Plot](../../03-scientific-computing/05-plotting-and-visualisation/01-matplotlib-basics.md)
  and
  [03-05-02 Line, Scatter and Error-Bar Plots with Correct Uncertainty](../../03-scientific-computing/05-plotting-and-visualisation/02-line-scatter-plots.md) —
  the figure anatomy and the error bar.
- [03-10-02 Reading MiniSEED/SAC: Trace and Stream](../../03-scientific-computing/10-obspy-and-seismic-data/02-reading-waveforms.md) —
  how a real waveform arrives.
- [05-02-02 Units and Conventions for Gravity, Magnetic and EM Fields](../../05-core-geophysics/02-geophysical-fields-and-observables/02-field-measurement-units.md) —
  why mGal and nT exist.
- [07-01-01 Newtonian Gravitation, Field and Acceleration](../../07-gravity-geodesy/01-gravity-fundamentals/01-newtonian-gravity.md) —
  the field the shell theorem computes.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Project: Units, Conversions and First Scientific Plots](01-units-and-plotting.md) | beginner | Two gradients — $0.3083$ and $0.1120\ \mathrm{mGal\,m^{-1}}$ — and a figure whose caption matches its axes |
| 02 | [Project: Mapping Global Seismicity from a Real Catalogue](02-earthquake-map.md) | beginner | $\hat b = 1.0005 \pm 0.0183$ at $M_c = 4.0\ \mathrm{M_w}$; refitting at $M_c = 4.5$ gives $0.9672$ |
| 03 | [Project: Computing Gravity Through a Layered Earth](03-gravity-of-earths-layers.md) | beginner | $g$ peaks at $10.7881\ \mathrm{m\,s^{-2}}$ near the CMB, and a uniform sphere is wrong by a factor of two there |
| 04 | [Project: Reading and Describing a Real Seismogram](04-reading-a-seismogram.md) | beginner | One record gives S−P, PGV and duration — and no magnitude, depth or mechanism |

## Suggested path

**If you are starting the whole curriculum's project track:** do 01 → 02 → 03 →
04 in order. Lesson 01's unit audit and figure checklist are reused by the other
three, and lesson 03's shell theorem is the reference field that lesson 04's and
module 25-02's anomalies are defined against.

**If you already write Python but have never converted a field sheet:** start at
01, and do not skip §4–§5, where the two gradients are derived rather than
looked up. Then go straight to 04, which is the most transferable of the four.

**If you are here for seismology:** 01 (units and figures), then 02 and 04. The
$b$-value of 02 and the S−P distance of 04 are the two numbers you will compute
in every subsequent seismological project.

**If you are preparing to supervise a beginner:** read the rubrics in each
lesson. They are written to be usable as marking schemes, and the failure-mode
lists are the three defects most often seen in first submissions.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-units-and-plotting.md`](01-units-and-plotting.md) | Project 01 |
| [`02-earthquake-map.md`](02-earthquake-map.md) | Project 02 |
| [`03-gravity-of-earths-layers.md`](03-gravity-of-earths-layers.md) | Project 03 |
| [`04-reading-a-seismogram.md`](04-reading-a-seismogram.md) | Project 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every project |
| [`code/`](code) | Four runnable demonstrations |

| Script | What it prints |
|---|---|
| [`code/units_and_plotting_demo.py`](code/units_and_plotting_demo.py) | SI conversion table, free-air and Bouguer gradients, dimensional checks, profile summary statistics |
| [`code/earthquake_map_demo.py`](code/earthquake_map_demo.py) | Synthetic catalogue statistics, MLE $b$-value with its error, $M_c$ sensitivity, density and depth statistics |
| [`code/layered_earth_gravity_demo.py`](code/layered_earth_gravity_demo.py) | Layer masses, $g(r)$ at every boundary, the maximum's location, uniform-sphere contrast, density sensitivity by Monte Carlo |
| [`code/reading_seismogram_demo.py`](code/reading_seismogram_demo.py) | Sampling and noise level, STA/LTA picks with errors, S−P distance, PGV, spectral peak, coda duration |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 25-projects-capstone/01-beginner-projects/code

/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python units_and_plotting_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python earthquake_map_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python layered_earth_gravity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reading_seismogram_demo.py
```

Each script prints labelled results with units, states its **SYNTHETIC**
provenance, reads no files, uses no network, draws no plots and exits 0. Each
runs in well under a second.

## Mastery checkpoint

Produce one artefact that uses all four projects:

> Take a six-row field table of your own choosing. **(a)** Convert it to SI with
> the factor for each row (§01). **(b)** Compute one gravity correction in mGal
> and one distance or time, checking each dimensionally. **(c)** Build a map or
> profile from the table, labelled with units, an uncertainty and the plotted
> range. **(d)** For whichever row is a measurement of a physical field, state
> its noise level and the window over which it was measured. **(e)** For each
> number, label it **measured**, **modelled** or **chosen**, and name the one
> additional observation that would most reduce the largest remaining
> uncertainty.

Worked versions of the individual pieces appear in the lesson solutions: the
conversion and gradient arithmetic at ★ in
[01](./exercises/01-units-and-plotting-solutions.md), the $b$-value and its
sensitivity at ★★ in
[02](./exercises/02-earthquake-map-solutions.md), the shell-theorem checks at ★★
in [03](./exercises/03-gravity-of-earths-layers-solutions.md), and the pick
budget at ★★★ in
[04](./exercises/04-reading-a-seismogram-solutions.md).

## Common pitfalls across this module

1. **A number without a unit.** It is the most common defect and the cheapest to
   fix; every rubric in this module fails it.
2. **A measurement without an uncertainty.** A $b$-value without $\sigma_b$, a
   distance without a pick error, a density without a window — all three are
   assertions rather than measurements.
3. **Treating a real archive as if it were complete or uniform.** A catalogue is
   a record of detected events; a waveform archive is a record of instrumented
   stations. Both imprint on the result.
4. **Assuming the surface value validates the model.** Lesson 03 shows two models
   agreeing to $0.00\%$ at the surface and disagreeing by a factor of two at the
   core-mantle boundary.
5. **Reporting what the data cannot give.** A magnitude from one station, a depth
   from one S−P time, a period from a window shorter than a few cycles.

## Related modules

- [25-02 Intermediate Projects](../02-intermediate-projects/README.md) — the
  same project discipline with a modelling step added.
- [05 Core Geophysics](../../05-core-geophysics/README.md) — the field
  definitions and units that project 01 converts.
- [07 Gravity and Geodesy](../../07-gravity-geodesy/README.md) — reductions,
  normal gravity and anomaly interpretation behind project 03.
- [06 Seismology](../../06-seismology/README.md) — travel times, magnitudes and
  source parameters behind projects 02 and 04.
- [22 Data Engineering and Reproducibility](../../22-data-engineering-reproducibility/01-research-software-engineering/README.md) —
  how the archive queries and unit audits of this module become a reproducible
  pipeline.
