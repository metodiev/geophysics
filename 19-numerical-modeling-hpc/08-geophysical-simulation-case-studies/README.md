# Module 19-08 — Geophysical Simulation Case Studies

**Stages:** doctoral → research · **Prerequisites:** module
[19-07](../07-verification-validation-uncertainty/README.md), and the
discretisation modules [19-01](../01-numerical-foundations/README.md) and
[19-02](../02-finite-difference-methods/README.md).

This module is where the machinery meets the subject. Five simulations are built
from the equations up — a seismic wavefield, potential-field responses, EM diffusion,
mantle convection and a simple climate model — and each one is presented as a
*claim* with its evidence attached: what is exact, what was measured, what was
chosen, and what remains unestablished. The lessons are not surveys of what
simulation can do; they are worked examples of how to tell whether a simulation is
right.

The organising principle is the one from module 19-07, applied five times: **a
simulation is a scientific claim only if it has been verified against an exact
solution and validated against an independent model, and numerical error is not
uncertainty.** Each case study therefore has exact benchmarks wherever the physics
provides them — the shell theorem for gravity, the analytic half-space impedance and
the error-function solution for diffusion, the exact critical Rayleigh number for
convection, the Stefan-Boltzmann equilibrium for the climate model — and each lesson
states precisely which of its numbers are benchmarks, which are measurements by a
demonstration you can run, and which are choices of the modeller.

Two of the five lessons end with an explicit confession, because that is what the
subject requires. The convection case study reproduces the exact stability threshold
at second order, verifies its time integration against exact linear theory, and then
declines to report a Nusselt number: the grid dependence of its short run is larger
than the effect. The climate case study computes exact equilibria, hysteresis and
relaxation times, and states that a calibrated model of its class cannot be
validated by the record it was tuned to. A case study that cannot say what it has
not established is not a case study.

All models and data in this module are **SYNTHETIC**. Every exact value is an
analytic result of the stated equations, every other number is printed by a
demonstration in `code/`, and no result is a measurement of the Earth.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the discrete dispersion relation, stability limits and group velocity
   of an explicit wave scheme, and **measure** them against a simulation.
2. **Derive** exact potential-field benchmarks (sphere, slab, dipole) and **verify**
   a volume-quadrature code against them.
3. **Quantify** the error of a compact-body approximation as a function of offset,
   and **state** the offsets at which it is usable.
4. **Derive** the EM diffusion equation, the exact half-space impedance and the
   constant $503.29$, and **verify** time-domain and layered solvers against exact
   references.
5. **Measure** how a discretisation choice at an interface changes the order of
   accuracy, and **state** the choice a benchmark must fix.
6. **Derive** the marginal-stability problem of Rayleigh-Bénard convection and the
   exact critical Rayleigh number $27\pi^{4}/4$.
7. **Verify** a convection solver against a conduction benchmark, a discrete
   stability eigenvalue problem and exact linear growth rates.
8. **Compute** the unstable wavenumber band and **state** the resolution a
   supercritical simulation requires.
9. **Derive** the zero-dimensional and one-layer radiative equilibria and the
   relaxation time constant of a climate model, and **verify** a time integrator
   against them.
10. **Compute** the multiple equilibria of a model with an ice-albedo feedback and
    **demonstrate** that their number changes with the solar constant.
11. **Distinguish**, for every number in a simulation study, what is exact, what is
    measured, what is chosen and what is model-form error.
12. **State** plainly what a simulation has *not* established, and design the study
    that would establish it.

## Prerequisites

- [19-07 Verification, Validation and Numerical Uncertainty](../07-verification-validation-uncertainty/README.md)
  — the discipline every lesson here applies.
- [19-01 Numerical Foundations for Simulation](../01-numerical-foundations/README.md)
  and [19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md)
  — discretisation, truncation error, dispersion and stability.
- [19-06 High-Performance and Parallel Computing](../06-hpc-and-parallel-computing/README.md)
  — helpful for the cost arithmetic, not essential for the physics.
- Domain familiarity with at least one of the five subjects (seismology, potential
  fields, EM, geodynamics, climate); the lessons introduce each equation set
  briefly and link out for the science.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Simulating a 2-D/3-D Seismic Wavefield](01-simulate-seismic-wavefield.md) | research | The scheme's dispersion is a depth error; the stability limit is a cliff at $1$ and $1/\sqrt{2}$ |
| 02 | [Simulating Gravity and Magnetic Responses](02-simulate-gravity-response.md) | doctoral | Quadrature is verifiable; the body is not; the same mass looks identical from far away |
| 03 | [Simulating EM Diffusion in Conductive Media](03-simulate-em-diffusion.md) | research | There is no wavefront; the recursion is an independent reference; conductance is what long periods measure |
| 04 | [Simulating Mantle Convection](04-simulate-mantle-convection.md) | research | An exact stability threshold, an exact growth rate, and a Nusselt number this demonstration refuses to report |
| 05 | [Running a Simple Climate Model](05-simulate-climate-model.md) | research | Exact equilibria and hysteresis, and a calibrated model that cannot be validated by its own target |

## Suggested path

**If you want to write a simulation code:** lesson 01, then lesson 04 — the two
lessons with the most machinery (a time-stepping scheme, an eigenvalue benchmark and
a linear-growth verification) and the clearest statements of what can be verified.

**If you interpret potential-field data:** lesson 02, with lesson 03 for the
diffusive case: both are about what a smooth kernel does and does not determine.

**If you are interested in climate or geodynamic modelling:** lessons 04 and 05,
which are deliberately paired — one shows a code verified up to the point where the
answer becomes grid-dependent, the other shows a model whose parameters are choices.

**If you have one hour:** read lesson 02 §5 and lesson 05 §5. They are the two
places where the measurement contradicts the natural narrative, and both end in an
explicit statement of what has not been established.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-simulate-seismic-wavefield.md`](01-simulate-seismic-wavefield.md) | Lesson 01 |
| [`02-simulate-gravity-response.md`](02-simulate-gravity-response.md) | Lesson 02 |
| [`03-simulate-em-diffusion.md`](03-simulate-em-diffusion.md) | Lesson 03 |
| [`04-simulate-mantle-convection.md`](04-simulate-mantle-convection.md) | Lesson 04 |
| [`05-simulate-climate-model.md`](05-simulate-climate-model.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulate_seismic_wavefield_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulate_gravity_response_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulate_em_diffusion_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulate_mantle_convection_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulate_climate_model_demo.py
```

Four of the five run in well under a second; the convection demonstration takes
about eight seconds because it time-steps a two-dimensional flow. Every demo prints
labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access, writes no files and
exits 0. They are print-only: no figures, no interactive windows.

## Mastery checkpoint

Complete this without notes:

> Choose one of the five case studies and produce a complete verification statement
> for its solver. **(a)** Name the exact benchmark you used and state the measured
> error and convergence order against it. **(b)** State the discretisation choice
> that a competing implementation is most likely to make differently, and the size
> of the resulting difference. **(c)** Name the model-form error your chosen
> physical approximation carries, with a number for the regimes in which it is
> negligible and the regimes in which it is not. **(d)** State the one measurement
> that would be needed to turn your verification into a validation. **(e)** Label
> every number you have used as **exact**, **measured**, **chosen** or
> **model-form**.

A worked version of (a)–(d) for the gravity case study appears in
[`exercises/02-simulate-gravity-response-solutions.md`](exercises/02-simulate-gravity-response-solutions.md).

## Common pitfalls across this module

1. **Judging a simulation by its picture.** Wavefield dispersion, diffusion tails
   and convection planforms all look plausible when they are wrong; the
   demonstrations measure the numbers instead.
2. **Confusing an exact benchmark with a validation.** The sphere, the slab, the
   half-space impedance and $27\pi^{4}/4$ are exact statements about *equations*,
   not about the Earth.
3. **Using a far-field approximation in the near field.** The point-mass and dipole
   models fail exactly where the anomaly is largest (lesson 02).
4. **Reporting a grid-dependent number as a result.** The convection demonstration
   declines to report a Nusselt number because refining the grid moves it by the
   size of the effect (lesson 04).
5. **Describing a calibrated model as validated.** The climate demonstration's
   emissivity, heat capacity, feedback parameter and albedo threshold are all chosen
   (lesson 05).
6. **Forgetting the direction of the error.** A scheme that propagates waves too
   slowly makes reflectors too deep; a point-mass model under-predicts the anomaly
   above the centre. Both signs are measurable and both matter for interpretation.

## Related modules

- [19-07 Verification, Validation and Numerical Uncertainty](../07-verification-validation-uncertainty/README.md)
  — the mother module; read it before or alongside this one.
- [19-01 Numerical Foundations](../01-numerical-foundations/README.md),
  [19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md),
  [19-03 Finite Element and Finite Volume](../03-finite-element-and-volume/README.md),
  [19-04 Spectral and Pseudospectral](../04-spectral-and-pseudospectral/README.md)
  — the discretisations these case studies use and compare.
- [19-06 High-Performance and Parallel Computing](../06-hpc-and-parallel-computing/README.md)
  — the cost of the resolutions every lesson computes.
- [06-seismology](../../06-seismology/README.md),
  [07-gravity-geodesy](../../07-gravity-geodesy/README.md),
  [09-electrical-em-methods](../../09-electrical-em-methods/README.md),
  [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md),
  [16-atmosphere-climate](../../16-atmosphere-climate/README.md) — the science
  behind each case study.
- [25-projects-capstone](../../25-projects-capstone/README.md) — where a study of
  this kind becomes a project.
