# Module 10-02 — GPR Acquisition and Processing

**Stages:** graduate → research · **Prerequisites:** module 10-01 (GPR
principles); basic signal processing and linear algebra.

This module turns the physics of module 10-01 into data and back again. Its
organising question is the one every GPR practitioner faces in the field: *what
do the acquisition numbers buy?* Trace spacing buys unaliased dips, line spacing
buys between-line resolution, offsets buy velocity, and the time window buys the
multiples you would otherwise not see. Those are four different purchases with
four different prices, and the module quantifies each one rather than listing
them as rules of thumb.

The lessons follow a survey from design to inversion. Lesson 01 derives the
sampling rules from the Nyquist condition and sizes a grid, a time window and a
common-midpoint programme, including the cross-hole geometry where coverage — not
ray count — decides what can be resolved. Lesson 02 is the processing sequence:
dewow, time zero, gain, filtering, migration and background removal, each
measured by what it does to a synthetic trace, with the amplitude-destroying
effect of AGC and the resolution cost of a band-pass shown numerically. Lesson 03
is the velocity analysis that the offsets were bought for: semblance, the
resolution of a moveout velocity, the collapse of that resolution at short
offset, Dix inversion with its error amplification, and a slant-stack cross-check
that uses no curvature at all. Lesson 04 extends everything to three dimensions,
where the time slice is the interpreter's instrument and where aliasing along the
line direction can reverse an apparent dip. Lesson 05 is the research frontier: a
convolutional model, an FDTD wave model with a grid-convergence test, an
adjoint-state gradient verified against finite differences, full-waveform
inversion with its cycle-skipping limit, and an honest report of how little of the
true amplitude a gradient method recovers.

**All models and data in this module are SYNTHETIC.** The survey dimensions,
velocities, conductivities, noise levels, filter cut-offs and inversion
parameters are chosen teaching values; no field survey, instrument, dataset or
published number is quoted. Every number in the lessons is printed by a
demonstration in [`code/`](./code), and where two independent routes to the same
quantity disagree — as they do for velocity resolution and for $\alpha$ — both
numbers are reported.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the sampling rules for trace and line spacing from the Nyquist
   condition and **design** a grid, a time window and a CMP offset range from a
   stated objective.
2. **Compute** the detection probability of a target against line spacing, and
   **distinguish** it from the resolution requirement.
3. **Evaluate** a cross-hole geometry from its ray coverage and angular aperture,
   and **state** where a tomogram's answer is not trustworthy.
4. **Measure** the effect of each processing step — dewow, gain, filter,
   migration, background removal — on picks, amplitudes and pulse width, and
   **order** the sequence from the assumptions each step makes.
5. **Derive** the apparent-dip relation $\tan\theta_{\text{app}} = \sin\theta$
   and the imaged-dip relation
   $\sin\theta_{\text{mig}} = (v_{\text{mig}}/v)\sin\theta$, and **verify** both
   on synthetic sections.
6. **Compute** a semblance surface, **define** a velocity resolution from it, and
   **compare** that resolution with analytic error propagation.
7. **Apply** the Dix relation and **propagate** pick errors through it.
8. **Interpret** 3-D time slices, **recover** a dip from slice motion, and
   **predict** the aliased apparent dip of an under-sampled grid.
9. **Verify** a finite-difference forward model against analytic travel times and
   by grid convergence, and **validate** an adjoint gradient against finite
   differences.
10. **Report** an inversion result with its misfit reduction, its amplitude
    shortfall and the spread of the answer under noise and starting-model change.

## Prerequisites

- [10-01 GPR Principles](../01-gpr-principles/README.md) — the speed, the
  reflection coefficient, the attenuation and the resolution limits this module
  assumes.
- [05-05-03 Spatial Sampling Theory](../../05-core-geophysics/05-survey-design-and-acquisition/03-spatial-sampling-theory.md) —
  the general sampling framework.
- [05-06-02 Noise Suppression](../../05-core-geophysics/06-data-processing-principles/02-noise-suppression.md) —
  the general treatment of coherent and incoherent noise.
- [18-01-01 Foundations of Inverse Problems](../../18-inverse-problems/01-inverse-problem-foundations/README.md) —
  misfit, gradient and ill-posedness.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Survey Design: Profile, Grid, CMP and Transillumination](01-gpr-survey-design.md) | graduate | Every acquisition number buys a specific capability, and detection spacing is not resolution spacing |
| 02 | [Processing Steps: Dewow, Gain, Filtering, Migration](02-gpr-processing.md) | graduate | Each step is an assumption; AGC destroys amplitudes and a filter buys signal-to-noise with resolution |
| 03 | [Velocity Analysis and Common-Midpoint Sounding](03-gpr-velocity-analysis.md) | doctoral | The semblance peak's *width* is the answer, and non-hyperbolic moveout sets it |
| 04 | [3-D GPR Imaging and Time Slices](04-gpr-3d-imaging.md) | doctoral | A time slice measures dip directly, and a coarse grid can reverse it |
| 05 | [GPR Modelling and Full-Waveform Inversion](05-gpr-modelling-and-inversion.md) | research | A verified adjoint is what separates inversion from assertion |

## Suggested path

**If you are new to GPR processing:** lessons 01–02 in order, running each
demonstration. Lesson 02 §3 is where the amplitude trap appears.

**If you already process GPR data:** read 03 (velocity resolution and Dix
amplification), 04 §4 (aliasing in the line direction), then 05 §3–4 (adjoint
verification and what FWI actually recovers).

**If you are preparing a research project:** 03 §3–4, 04 §5–6, and all of 05,
with the ★★★ exercises in each lesson.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-gpr-survey-design.md`](01-gpr-survey-design.md) | Lesson 01 |
| [`02-gpr-processing.md`](02-gpr-processing.md) | Lesson 02 |
| [`03-gpr-velocity-analysis.md`](03-gpr-velocity-analysis.md) | Lesson 03 |
| [`04-gpr-3d-imaging.md`](04-gpr-3d-imaging.md) | Lesson 04 |
| [`05-gpr-modelling-and-inversion.md`](05-gpr-modelling-and-inversion.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable, print-only demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 10-gpr-near-surface/02-gpr-acquisition-and-processing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_survey_design_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_processing_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_velocity_analysis_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_3d_imaging_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_modelling_and_inversion_demo.py
```

Every demonstration prints labelled results with units, uses the fixed seed
`np.random.default_rng(20261014)`, requires no network access, and exits 0. The
FDTD and inversion demonstration takes a few seconds; the others finish in about
a second.

## Mastery checkpoint

Complete this without notes:

> A $200\ \mathrm{MHz}$ survey over ground with $\varepsilon_r = 9$ targets an
> interface at $2.0\ \mathrm{m}$ that dips $25^\circ$, and a deeper one at
> $3.5\ \mathrm{m}$. The program is a $30\ \mathrm{m} \times 10\ \mathrm{m}$ grid
> plus one CMP sounding.
> **(a)** Compute the required trace and line spacing for unaliased $25^\circ$
> dips, and the Fresnel diameter at $2.0\ \mathrm{m}$.
> **(b)** Compute the detection probability at your line spacing and state
> whether it is a detection or a resolution spacing.
> **(c)** Compute the CMP offset range that determines the velocity to $3\%$ with
> a $0.25\ \mathrm{ns}$ pick error.
> **(d)** Design the processing order and name the step that must not be used
> before an amplitude analysis.
> **(e)** Predict the apparent dip of the $25^\circ$ interface if the line
> spacing were two wavelengths and the wavelength in the wet part of the site
> were $0.4\ \mathrm{m}$.
> **(f)** State one quantity an FDTD inversion would and one it would not
> determine.

Parts (a)–(e) are worked across the five lesson solution files in
[`exercises/`](./exercises).

## Common pitfalls across this module

1. **Designing the grid by trace count rather than by the alias limit.** Aliased
   dips are wrong dips, and a coarse line spacing can reverse a dip's sign.
2. **Confusing detection with resolution.** The two requirements give different
   spacings, differing by the Fresnel diameter.
3. **Using AGC before amplitude work.** The gain, not the ground, is then being
   measured.
4. **Reporting a filter's signal-to-noise gain without its resolution cost.**
   They are two sides of one operation.
5. **Quoting a semblance peak as a velocity.** Its width is the resolution, and
   non-hyperbolic moveout usually sets it.
6. **Believing a dip from time slices is geology.** It is geology divided by the
   assumed velocity — and a $10\%$ error moves an interface by half a metre.
7. **Running an inversion on an unverified gradient.** The finite-difference test
   takes minutes and prevents months of confusion.
8. **Reporting one inversion run.** Noise and the starting model change the
   answer by a few per cent of the signal, which is comparable with the
   recovered amplitude itself.

## Related modules

- [10-01 GPR Principles](../01-gpr-principles/README.md) — the physics this
  module applies.
- [10-03 GPR Applications](../03-gpr-applications/README.md) — where these
  methods are used.
- [05-06 Processing Principles](../../05-core-geophysics/06-data-processing-principles/README.md) —
  the discipline of processing transparency.
- [06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md) —
  the same sequence of ideas at exploration scale, with the same failure modes.
- [18-04 Nonlinear Inversion and Optimisation](../../18-inverse-problems/04-nonlinear-inversion/README.md) —
  the optimisation theory behind lesson 05.
- [23-04 Electrical and EM Fieldwork](../../23-field-methods-instruments/04-electrical-em-fieldwork/README.md) —
  the field practice that makes or breaks a GPR program.
