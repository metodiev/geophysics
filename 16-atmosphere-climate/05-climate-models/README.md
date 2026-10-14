# Module 16-05 — Climate Models and Simulation

**Stages:** graduate → research · **Prerequisites:** module 16-02 (radiation and
energy balance), module 16-04 (the climate system and feedbacks); basic numerical
methods and linear algebra.

This module is about the instruments rather than the climate. A climate model is
a set of equations, a grid, and a collection of closures that stand in for
physics the grid cannot see. Every lesson here asks the same two questions of a
model: *what does it resolve, and what does it assume?* The answers are always
paired — the resolution buys detail and the closure buys back an assumption — and
the module is organised so that the pairing stays visible.

The honest difficulty at the centre of the module is that **a model's output is
conditional on choices that are not measurements**. A linear outgoing-longwave
coefficient, a diffusivity, a grid spacing, a convective mixing rule, a
calibration period, an ensemble weighting, a kernel length scale: each is a
decision, each moves the answer, and none of them is in the data. Rather than
treat this as a caveat to be mentioned at the end, each lesson measures the
sensitivity and reports it as a number. The discipline that emerges is not
"trust the model less" but "state the closure, the design and the regime of
validity, and quantify what each contributes".

The module also develops the tools that make the reporting possible: verification
metrics and their blind spots, the double penalty of squared-error scores,
variance decompositions that separate internal variability from structural
spread, and emulators that make large ensembles affordable while introducing a
new and different kind of error. All models and data in this module are
**SYNTHETIC**: the "models" are chosen response coefficients or one-dimensional
teaching constructions, no real model output is used, and no published score,
ensemble size or intercomparison number is quoted anywhere.

## Learning objectives

By the end of this module you will be able to:

1. **Classify** a climate model by its prognostic state and its closures rather
   than by its name, and **state** what each level of the hierarchy can and
   cannot constrain.
2. **Measure** the numerical diffusion of a first-order advection scheme,
   **compare** it with its analytic modified-equation value, and **state** how it
   scales with grid spacing.
3. **Construct** an energy-conserving convective adjustment and **demonstrate**
   that two such closures disagree on the final state.
4. **Compute and interpret** bias, RMSE, anomaly correlation, the centered RMS
   difference and a skill score, and **verify** the Taylor identity numerically.
5. **Demonstrate** the double penalty and **correct** a significance statement for
   serial correlation.
6. **Rank** downscaling methods by measured error, and **explain** why a
   statistically downscaled product assumes stationarity of its calibration.
7. **Derive** and **measure** the ensemble-mean error law, and **decompose** total
   spread into structural and internal parts.
8. **Quantify** the overconfidence of a single-model large ensemble and **state**
   what a multi-model archive is a sample of.
9. **Fit** a Gaussian-process emulator, **measure** its interpolation and
   extrapolation error, and **state** the difference between emulator uncertainty
   and structural model error.

## Prerequisites

- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  the absorbed flux, the greenhouse effect and the energy-balance models this
  module parameterises.
- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  feedbacks, sensitivity and internal variability, which the ensembles here
  estimate.
- [01-12 Numerical Methods for Mathematical Problems](../../01-mathematics/12-numerical-methods/README.md) —
  discretisation, truncation error and stability, used in lesson 02.
- [03-12 Building Numerical Simulation Code in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md) —
  the practical CFL and verification habits the demos assume.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Model Hierarchy: EBMs, EMICs, GCMs, ESMs](01-climate-model-hierarchy.md) | graduate | Classify by state and closure; the 1-D mean must equal the 0-D answer |
| 02 | [GCMs, Resolution and Parameterisation](02-gcms-and-parameterisation.md) | research | Discretisation generates diffusion; two energy-conserving closures disagree |
| 03 | [Model Evaluation, Skill and Benchmarking](03-model-evaluation.md) | research | Every score is a choice; RMSE rewards smoothing |
| 04 | [Downscaling: Statistical and Dynamical](04-downscaling.md) | research | A regression cannot add structure; stationarity is an assumption |
| 05 | [CMIP, Model Intercomparison and Ensemble Design](05-coupled-model-intercomparison.md) | research | Members reduce internal error; only models reduce structural spread |
| 06 | [Emulators and Surrogate Models for Climate](06-emulation-and-surrogates.md) | research | Predictive variance is distance from data, not disagreement with physics |

## Suggested path

**New to climate modelling:** lessons 01 and 02 in order, running both demos.
Lesson 02 is where the distinction between resolved and parameterised becomes
concrete, and where the numerical diffusion is measured rather than asserted.

**Already comfortable with EBMs:** start at 02 (the modified equation), then 03
(how the output is scored) and 05 (how the spread is decomposed). Those three
supply the vocabulary the research literature assumes.

**Preparing a research project:** 03 §5–6 (double penalty and effective sample
size), 04 §5 (the stationarity failure), 05 §5–6 (structural spread and
weighting) and 06 §6 (emulators that are confidently wrong).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-climate-model-hierarchy.md`](01-climate-model-hierarchy.md) | Lesson 01 |
| [`02-gcms-and-parameterisation.md`](02-gcms-and-parameterisation.md) | Lesson 02 |
| [`03-model-evaluation.md`](03-model-evaluation.md) | Lesson 03 |
| [`04-downscaling.md`](04-downscaling.md) | Lesson 04 |
| [`05-coupled-model-intercomparison.md`](05-coupled-model-intercomparison.md) | Lesson 05 |
| [`06-emulation-and-surrogates.md`](06-emulation-and-surrogates.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and xarray:

```bash
cd 16-atmosphere-climate/05-climate-models/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_model_hierarchy_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gcms_and_parameterisation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python model_evaluation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python downscaling_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python coupled_model_intercomparison_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python emulation_and_surrogates_demo.py
```

Every demo prints labelled results with units, uses the fixed random seed
`np.random.default_rng(20261014)`, requires no network access, and exits 0. Each
one is print-only: there is no plotting, and every number quoted in a lesson can
be reproduced by running its demo.

## Mastery checkpoint

Complete this without notes.

> A one-dimensional energy-balance model with diffusion has been tuned so that
> its equator-minus-pole contrast matches an observation. **(a)** State what has
> been calibrated and what has been assumed, and give one diagnostic that would
> test the assumption. **(b)** The model's grid is refined without changing the
> diffusion coefficient; state what happens to the numerical diffusion and why.
> **(c)** The model is scored against a reanalysis and reports a correlation of
> $0.95$ with a standard-deviation ratio of $0.55$. Say which of the two numbers
> hides a defect and what that defect is. **(d)** A five-member perturbation
> ensemble gives a standard error of $0.1\ \mathrm{K}$ for the response, while
> three alternative models span $1.2\ \mathrm{K}$. State which uncertainty is
> being estimated by the standard error and which is omitted.

Worked versions of (a)–(c) appear in the lesson-03
[solutions](exercises/03-model-evaluation-solutions.md) and the lesson-01
[solutions](exercises/01-climate-model-hierarchy-solutions.md).

## Common pitfalls across this module

1. **Reporting a model's output without its closure.** The closure is part of the
   answer, not a footnote.
2. **Treating numerical diffusion as a bug.** It is a predictable truncation
   error; the remedy is resolution, and the diagnosis is the modified equation.
3. **Reporting one verification score.** Correlation hides bias; RMSE hides
   displacement; a skill score hides its reference.
4. **Assuming a statistical downscaling can add information.** It cannot exceed
   what its predictors contain.
5. **Reading a multi-model mean as a best estimate.** It is an average of
   opinions, and the models are not exchangeable.
6. **Confusing emulator uncertainty with model uncertainty.** The first measures
   distance from training data.
7. **Reporting a spread without saying which uncertainty it measures.**

## Related modules

- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  the physics parameterised here.
- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  the sensitivity and internal variability that ensembles estimate.
- [16-06 Palaeoclimate](../06-palaeoclimate/README.md) — the same models used
  against proxy records.
- [16-07 Extremes, Impacts and Attribution](../07-climate-extremes-and-attribution/README.md) —
  where evaluation choices become decision-relevant.
- [16-08 Climate Observations and Data](../08-climate-observation-and-data/README.md) —
  the observational side of every comparison in this module.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  discretisation, parallelism and verification in depth.
- [18-inverse-problems](../../18-inverse-problems/README.md) — regularisation,
  uncertainty quantification and model assessment.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) —
  regression, kernels and inference.
