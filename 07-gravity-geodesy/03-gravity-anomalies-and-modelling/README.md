# Module 07-03 — Gravity Anomalies and Modelling

**Stages:** advanced → research · **Prerequisites:** modules 07-01 and 07-02;
single-variable and vector calculus; NumPy.

This module takes a gravity anomaly — one number per station, on a surface — and
asks what it can and cannot say about the body below. The organising difficulty is
stated once and then measured everywhere: an anomaly constrains a *projection* of a
three-dimensional density distribution, and projections have kernels. A sphere's
depth can be read from the width of its profile only after the shape is assumed; a
figure of 152:1 in mass can be cancelled exactly by two sheets in the right
proportion; a smooth pile of shallow cells fits the same data as a deep block; a
downward-continued map is a picture of the noise.

Every lesson therefore arrives with its ambiguity attached. The interpretation
rules of lesson 01 come with the family of bodies that reproduce the same peak;
the analytical formulas of lesson 02 come with their limits and verifications; the
forward modelling of lesson 03 comes with its measured discretisation error; the
inversion of lesson 04 comes with an admitted set rather than a model; the
derivative and continuation filters of lesson 05 come with a bias-variance table
and an amplification factor; the microgravity lesson comes with a depth
uncertainty from the station spacing; and the time-variable lesson comes with the
leakage that makes every recovered amplitude a lower bound.

All models and data in this module are **SYNTHETIC**. The bodies, densities,
station layouts, noise levels and anomalies are chosen teaching values. No real
survey, site, instrument or published measurement is used, and the only numbers
quoted from outside are standard physical constants.

## Learning objectives

By the end of this module you will be able to:

1. Apply and justify the half-width and derivative depth rules, and state the
   depth error introduced by assuming the wrong body shape.
2. Derive and evaluate the closed-form anomalies of a sphere, a cylinder, an
   infinite sheet, a semi-infinite sheet and a 2-D rectangle, and verify each
   against an independent integration or limit.
3. Build a 3-D model from rectangular prisms, verify it against quadrature, and
   measure the discretisation error of a voxelised body.
4. Formulate and solve a discretised gravity inversion with a smoothness penalty
   and non-negativity, and read the misfit-versus-regularisation trade-off.
5. Interpret a model resolution matrix, construct an exact annihilator, and report
   an admitted set of models rather than a best fit.
6. Verify wavenumber-domain filters against analytic derivatives, split a
   derivative's error into bias and noise, and quantify the amplification of
   downward continuation.
7. Solve the Euler equation in a sliding window, and use its residual to reject
   windows where the single-source assumption has failed.
8. Convert between gravity change and mass change for surface layers, and quantify
   attenuation, leakage and record-length limits.

## Prerequisites

- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../01-gravity-fundamentals/04-gravity-reduction.md) —
  what an anomaly is once the known effects are removed.
- [07-01-05 Units (Gal, mGal), Absolute vs Relative Measurement](../01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md) —
  the practical size of a measurable anomaly.
- [07-02-02 Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex](../02-gravity-instruments-and-surveys/02-relative-gravimeters.md) and
  [07-02-04 Practical Correction Workflow and Processing Sequence](../02-gravity-instruments-and-surveys/04-corrections-workflow.md) —
  the data this module interprets.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the general theory behind lesson 04.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Interpreting Anomalies: Geometry, Depth and Amplitude Rules](01-anomaly-interpretation.md) | advanced | Half-width gives depth *conditional on the body shape*; one peak admits a family of bodies |
| 02 | [Analytical Formulas for Sphere, Cylinder, Sheet and Dyke](02-simple-body-formulas.md) | graduate | Derive the five workhorses; verify each by a limit; sensitivity is twice as strong to radius as to density |
| 03 | [Forward Modelling in 2-D and 3-D](03-forward-modelling-2d3d.md) | graduate | Prisms plus superposition are exact; the discretisation error is a volume error until mass is matched |
| 04 | [Gravity Inversion and Its Severe Non-Uniqueness](04-inversion-gravity.md) | doctoral | A perfect fit is not an answer; resolution decays with depth; an exact annihilator exists |
| 05 | [Derivatives, Upward/Downward Continuation and Euler Deconvolution](05-derivatives-and-filters.md) | doctoral | Every filter multiplies by a power of $k$; downward continuation amplifies noise by $e^{k\Delta z}$ |
| 06 | [Microgravity for Cavities, Tunnels and Archaeology](06-microgravity-applications.md) | advanced | Detection is limited by the covariance of terrain and gravity, and depth by station spacing |
| 07 | [Time-Variable Gravity: Hydrology, Ice and Mass Redistribution](07-time-variable-gravity.md) | research | Mass per unit area is what gravity measures; leakage makes amplitudes lower bounds |

## Suggested path

**If you are new to gravity interpretation:** lessons 01, 02 and 06 in order,
running each demonstration. Lesson 06 is where the rules collide with noise and
station spacing.

**If you already forward-model in 2-D:** read 01 §3 (the trade-off), then 03 and
04 — the same ambiguity approached by modelling and by inverting.

**If you are preparing a research project:** 04 (non-uniqueness and admitted
sets), 05 (filters and Euler, including the failure modes), 07 (conversion,
attenuation and leakage), plus the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-anomaly-interpretation.md`](01-anomaly-interpretation.md) | Lesson 01 |
| [`02-simple-body-formulas.md`](02-simple-body-formulas.md) | Lesson 02 |
| [`03-forward-modelling-2d3d.md`](03-forward-modelling-2d3d.md) | Lesson 03 |
| [`04-inversion-gravity.md`](04-inversion-gravity.md) | Lesson 04 |
| [`05-derivatives-and-filters.md`](05-derivatives-and-filters.md) | Lesson 05 |
| [`06-microgravity-applications.md`](06-microgravity-applications.md) | Lesson 06 |
| [`07-time-variable-gravity.md`](07-time-variable-gravity.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 07-gravity-geodesy/03-gravity-anomalies-and-modelling/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python anomaly_interpretation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simple_body_formulas_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python forward_modelling_2d3d_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python inversion_gravity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python derivatives_and_filters_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python microgravity_applications_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python time_variable_gravity_demo.py
```

Every demo is print-only, prints labelled results with units, uses a fixed random
seed (`np.random.default_rng(20261014)`), runs in well under a second, and exits 0.
They require no network access and no data files. **The numbers in the lessons are
the numbers these scripts print**; if a script is edited, the lesson text should be
checked against it.

## Mastery checkpoint

Complete this without notes:

> A profile over an isolated body has a peak of $1.80\ \mathrm{mGal}$ and a
> half-width of $420\ \mathrm{m}$, sampled at $40\ \mathrm{m}$ spacing over a
> $4\ \mathrm{km}$ line with $0.05\ \mathrm{mGal}$ rms noise and a flat regional.
> **(a)** Give the depth under the cylinder rule and under the sphere rule.
> **(b)** Give the mass for the sphere interpretation at $1.5\ \mathrm{g\,cm^{-3}}$
> density contrast, and check the point-mass approximation.
> **(c)** State the admitted mass range for a $1.5\ \mathrm{km}$ aperture at this
> noise level. **(d)** Name two measurements that would collapse the ambiguity, and
> one number you would refuse to quote without them.

Worked versions of (a) and (b) appear in the lesson-01
[solutions](exercises/01-anomaly-interpretation-solutions.md); the admitted-set
logic is in the lesson-04
[solutions](exercises/04-inversion-gravity-solutions.md).

## Common pitfalls across this module

1. **Reporting a depth from a half-width without naming the body shape.** The two
   standard rules differ by $30\%$.
2. **Dropping the factor of two** between 2-D and 3-D kernels.
3. **Voxel models that do not conserve volume**, so that the error tracks the
   volume error and not the cell size.
4. **Reading a misfit below the stated noise as success.** It is a symptom of
   over-parameterisation.
5. **Presenting a best-fit inversion rather than the admitted set.**
6. **Sharpening without denoising.** A full-band derivative of noisy data is worse
   than the original.
7. **Using a downward continuation deeper than the retained wavelength allows.**
8. **Confusing microgal with mGal**, and **ignoring the Earth tide** in a
   microgravity survey.
9. **Applying the slab constant to a global mass change**, or the shell constant to
   a basin — a factor of two.
10. **Reading a filtered amplitude as the true amplitude.** Smoothing always lowers
    a peak.

## Related modules

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — the physics
  and the reductions behind every anomaly used here.
- [07-02 Gravity Instruments and Surveys](../02-gravity-instruments-and-surveys/README.md) —
  how the numbers are acquired and corrected.
- [07-04 Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md) —
  the coordinate and height framework an anomaly is defined in.
- [07-05 Satellite Gravimetry](../05-satellite-gravimetry/README.md) — the same
  inverse problem with a global, time-variable data set.
- [07-06 Earth Tides and Rotation](../06-earth-tides-and-rotation/README.md) — the
  tidal signal that must be removed before a microgal anomaly is interpretable.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of resolution, regularisation and uncertainty.
