# Module 25-02 — Intermediate Projects

**Stages:** intermediate · **Prerequisites:** module
[25-01 Beginner Projects](../01-beginner-projects/README.md) and the
method lessons of [05 Core Geophysics](../../05-core-geophysics/README.md),
[06 Seismology](../../06-seismology/README.md),
[07 Gravity and Geodesy](../../07-gravity-geodesy/README.md) and
[20 Signal Processing](../../20-signal-processing/README.md).

This module keeps the project format of 25-01 and adds the ingredient that makes
a project *intermediate*: a **model that must be fitted, and whose conditioning
must be measured**. Every lesson here ends with the same question in a different
guise — which parameter does the data determine, which one does the assumption
determine, and how big is the difference. A travel-time slope determines a
velocity; the intercept determines a depth only if the overburden velocity is
known, and the demonstration measures the resulting $\pm 12\%$ swing. A gravity
profile's half-width determines a depth; its amplitude determines only a product,
and the demonstration produces five depth–radius pairs that fit one peak equally
well. A refraction survey determines the velocities that increase with depth and
nothing else, and the demonstration shows a real 2 m layer that leaves no trace
in the first arrivals.

The organising idea is therefore **accounting, not modelling**. Each lesson's
deliverable is a table: parameter, value, statistical uncertainty, systematic
uncertainty, and the assumption that produced the systematic term. Where the two
terms differ by an order of magnitude — as they do for the well-log porosity of
lesson 05, where a matrix-density change is worth $2.92\ \mathrm{p.u.}$ against a
random term of $0.30\ \mathrm{p.u.}$ — the lesson says so in the summary, because
a result quoted to the statistical precision alone is misleading even when every
number in it is correct.

Provenance is stated per lesson. Real archives are named where the project
genuinely needs them — the USGS FDSN event service for travel times, the NOAA
global gravity database for anomalies, the NOAA land-based station archive for
series — and every number quoted in the prose comes from a **SYNTHETIC**
demonstration that the reader can run without a network. Each demonstration is
print-only, seeded with `np.random.default_rng(20261014)`, finishes in under a
second and exits 0.

## Learning objectives

By the end of this module you will be able to:

1. **Derive and invert** the travel-time branches of a layered Earth, and
   **quantify** how the recovered thickness depends on the assumed overburden
   velocity.
2. **Write and evaluate** the closed-form anomaly of a sphere, a cylinder and a
   slab, and **use** half-width rules to separate depth from size.
3. **Demonstrate** the amplitude degeneracy of potential-field bodies and
   **identify** the observation that breaks it.
4. **Compute** a normalised power spectral density, **verify** it with Parseval's
   theorem, and **measure** leakage and detection thresholds rather than assuming
   them.
5. **Interpret** a refraction survey with the intercept-time method and
   **demonstrate** that a hidden layer is invisible to first arrivals.
6. **Propagate** log uncertainties through the porosity relations, **combine**
   two estimators by inverse-variance weighting, and **measure** the systematic
   error from a wrong matrix assumption.
7. **Report** any result from this module as a value with a random term, a
   systematic term and the assumption that produced the latter.

## Prerequisites

- [25-01-04 Project: Reading and Describing a Real Seismogram](../01-beginner-projects/04-reading-a-seismogram.md) —
  the measurements this module inverts.
- [05-04-01 Porosity, Density and Velocity Relationships](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  the mixing equations behind project 05.
- [05-05-02 Array Geometry, Fold, Offsets and Spatial Sampling](../../05-core-geophysics/05-survey-design-and-acquisition/02-geometry-and-coverage.md) —
  how geometry sets the depth of investigation in project 04.
- [06-02-02 Snell's Law, Layered Media and the Travel-Time Curve](../../06-seismology/02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  the branch structure of project 01.
- [06-10-01 Refraction Survey Geometry and Travel-Time Interpretation](../../06-seismology/10-refraction-and-near-surface-seismology/01-refraction-basics.md) —
  the shallow survey of project 04.
- [07-03-02 Analytical Formulas for Sphere, Cylinder, Sheet and Dyke](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/02-simple-body-formulas.md) —
  the closed forms of project 02.
- [20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper](../../20-signal-processing/02-fourier-and-spectral-analysis/02-spectral-estimation.md) —
  the estimator of project 03.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Project: Travel-Time Curves and 1-D Velocity Structure](01-travel-time-curves.md) | intermediate | A $0.6\ \mathrm{km\,s^{-1}}$ change in the assumed crustal velocity moves the inferred Moho from 28.9 to 36.0 km |
| 02 | [Project: Gravity Anomaly of Simple Bodies](02-simple-gravity-model.md) | intermediate | Five depth–radius pairs fit one peak; the half-width breaks the tie |
| 03 | [Project: Fourier Analysis of a Geophysical Signal](03-fourier-analysis-signals.md) | intermediate | Parseval to $2\%$, a lobe-sum amplitude within $2\%$, and $-9.6$ vs $-30.9\ \mathrm{dB}$ leakage |
| 04 | [Project: Interpreting a Refraction Survey](04-refraction-interpretation.md) | intermediate | A hidden 2 m layer produces a $17.5\%$ depth error and leaves no trace |
| 05 | [Project: Porosity from Well Logs with Uncertainty](05-reservoir-porosity-quantitative.md) | intermediate | A $6.3\sigma$ estimator discrepancy and a systematic term 9.8× the random one |

## Suggested path

**If you are working through the folder in order:** 01 → 02 → 03 → 04 → 05. The
accounting habit established in 01 (statistical versus model uncertainty) is used
by all four later projects.

**If you are a seismologist:** 01 and 04 together, then 02 for the potential-field
counterpart. The hidden-layer demonstration of 04 is the one result most often
missing from a shallow-site report.

**If you work with potential fields:** 02, then 01 for the travel-time analogue of
the same conditioning argument, then
[25-03-06 Advanced: gravity inversion with uncertainty quantification](../03-advanced-projects/06-gravity-inversion-uq.md).

**If you come from petrophysics or reservoir work:** 05 in full, then
[25-04-05 Joint gravity-seismic inversion](../04-graduate-projects/05-joint-inversion-project.md),
where the matrix assumption of 05 becomes the prior of the inversion.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-travel-time-curves.md`](01-travel-time-curves.md) | Project 01 |
| [`02-simple-gravity-model.md`](02-simple-gravity-model.md) | Project 02 |
| [`03-fourier-analysis-signals.md`](03-fourier-analysis-signals.md) | Project 03 |
| [`04-refraction-interpretation.md`](04-refraction-interpretation.md) | Project 04 |
| [`05-reservoir-porosity-quantitative.md`](05-reservoir-porosity-quantitative.md) | Project 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every project |
| [`code/`](code) | Five runnable demonstrations |

| Script | What it prints |
|---|---|
| [`code/travel_time_curves_demo.py`](code/travel_time_curves_demo.py) | Branch table, crossover, least-squares inversion with uncertainties, velocity–depth trade-off |
| [`code/simple_gravity_model_demo.py`](code/simple_gravity_model_demo.py) | Three peaks against closed forms, half-width depth rules, slab depth-independence, degeneracy table |
| [`code/fourier_analysis_signals_demo.py`](code/fourier_analysis_signals_demo.py) | PSD with units, Parseval ratio, peak and lobe amplitudes, leakage in dB, noise-null threshold |
| [`code/refraction_interpretation_demo.py`](code/refraction_interpretation_demo.py) | Three branches with crossovers, inverted velocities and thicknesses, hidden-layer demonstration |
| [`code/porosity_well_logs_demo.py`](code/porosity_well_logs_demo.py) | Two porosity estimators, inverse-variance combination, matrix sensitivity, uncertainty budget |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 25-projects-capstone/02-intermediate-projects/code

/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python travel_time_curves_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simple_gravity_model_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fourier_analysis_signals_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python refraction_interpretation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python porosity_well_logs_demo.py
```

Each script prints labelled results with units, states its **SYNTHETIC**
provenance, reads no files, uses no network, draws no plots and exits 0. Each
runs in under a second.

## Mastery checkpoint

Produce one accounting table for a model you have fitted:

> **(a)** Choose one project of this module and state its forward model and its
> parameters. **(b)** Fit the parameters and report each with its statistical
> uncertainty from the fit covariance. **(c)** For each parameter, identify the
> *assumed* quantity it depends on, perturb that quantity by a plausible amount,
> and record the resulting change. **(d)** Tabulate the statistical and
> systematic terms side by side and state which dominates. **(e)** Name the single
> additional observation that would reduce the dominant term, and estimate what
> it would cost. Worked examples appear in the ★★ and ★★★ solutions of every
> lesson; the closest complete template is
> [05's ★★5](./exercises/05-reservoir-porosity-quantitative-solutions.md) and
> [01's ★★4](./exercises/01-travel-time-curves-solutions.md).

## Common pitfalls across this module

1. **Reporting the statistical uncertainty when the systematic term is ten times
   larger.** Lessons 01 and 05 both measure this ratio; it is the module's central
   defect.
2. **Fitting a model over a range where it does not apply** — a branch past its
   crossover, a slab model on a compact body, a Wyllie relation in a vuggy
   interval.
3. **Reading a number off a figure instead of integrating or fitting it** — the
   peak PSD bin is $20\%$ low; the visual half-width is $10\%$ uncertain.
4. **Assuming two estimators of one quantity must agree.** A $6.3\sigma$
   disagreement is a result, not a nuisance.
5. **Quoting a depth or a size without the assumption that produced it** — the
   overburden velocity, the density contrast, the matrix mineralogy.

## Related modules

- [25-01 Beginner Projects](../01-beginner-projects/README.md) — the measurement
  and unit discipline this module builds on.
- [25-03 Advanced Projects](../03-advanced-projects/README.md) — the same
  accounting with an inversion and an explicit resolution assessment.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the theory of the
  conditioning arguments used here informally.
- [20 Signal Processing](../../20-signal-processing/README.md) — windows,
  leakage and detection, applied in project 03.
- [22 Data Engineering and Reproducibility](../../22-data-engineering-reproducibility/01-research-software-engineering/README.md) —
  how the tables of this module become a reproducible pipeline.
