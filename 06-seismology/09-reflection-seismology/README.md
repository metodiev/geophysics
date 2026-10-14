# Module 06-09 — Reflection Seismology

**Stages:** advanced → research · **Prerequisites:** modules 06-01 and 06-02;
basic digital signal processing.

Reflection seismology is the applied end of seismology: a controlled source, a
line of receivers, and a processing flow that turns a set of noisy traces into an
image of the subsurface. This module follows that flow from the physics of a
reflection coefficient to the uncertainty of a mapped depth, and it insists on
one habit throughout — **every processing step is an approximation, and the
module measures what each one costs.**

That is the central honest difficulty. Normal-incidence data measure only the
product $\rho v$, so a velocity–density trade is invisible (lesson 01). Stacking
suppresses random noise as $\sqrt{N}$ and barely touches coherent noise
(lesson 02). Stacking velocities are biased by $1/\cos\theta$ wherever a reflector
dips, coupling dip and velocity into a single wrong number (lesson 03).
Migration focuses only with the right velocity, and the focus — not the
position — is the criterion (lesson 04). AVO adds an angle, but the angle buys a
gradient and leaves a one-parameter family of models that fit the same curve
(lesson 05). Multiple attenuation removes part of the primary along with the
multiple, and the traded amounts are numbers, not adjectives (lesson 06).
Resolution and detection are different questions (lesson 07), 4-D detection is a
repeatability problem rather than an amplitude problem (lesson 08), and a fault
throw is a measurement with a resolution scale attached (lesson 09).

All models and data in this module are **SYNTHETIC**. No real survey, log, well
or waveform is used, and no number is quoted from a published measurement.

## Learning objectives

By the end of this module you will be able to:

1. Compute impedances, reflection and transmission coefficients, and two-way
   times with units, and explain why normal-incidence data cannot separate
   velocity from density.
2. Derive the NMO hyperbola from the mirror-image geometry, quantify where the
   hyperbolic approximation fails, and state what stacking does and does not
   suppress.
3. Measure velocity resolution as a function of cable length and bandwidth,
   and compute the dip bias $v_{\text{NMO}} = v/\cos\theta$.
4. Write and apply Kirchhoff diffraction-sum migration, and use the image focus
   (not the position) to estimate the migration velocity.
5. Compute the Aki–Richards intercept and gradient, perform a fluid
   substitution, and construct two members of the AVO equivalence class.
6. Compute the curvature separation of a primary and a multiple, measure the
   price of a Radon mute, and choose between Radon, SRME-style prediction and
   predictive deconvolution.
7. Compute $\lambda/4$, the tuning curve, the Widess limit and the Fresnel
   radius, and distinguish detection from resolution with numbers.
8. Compute NRMS, derive the $\sqrt{2}$ detection factor, and test whether a 4-D
   signal is detectable given a repeatability budget.
9. Convert a fault throw to depth, attach the resolution scale and the picking
   uncertainty, and state when a throw should not be published as a number.

## Prerequisites

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  body waves, reflection and transmission at interfaces.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  travel-time curves, stacking and the ray parameter.
- [03-03-05 scipy.signal: Filters, Windows and Spectral Estimation](../../03-scientific-computing/03-scipy/05-signal.md) —
  convolution, correlation and spectral estimation as used in the demos.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Acoustic Impedance, Reflection Coefficients and the Convolution Model](01-reflection-principle.md) | advanced | The convolutional model reproduces $R$ exactly (ratio $1.00000$); a $\rho v$-preserving trade is invisible at normal incidence |
| 02 | [Reflection Processing Flow: Deconvolution, NMO, Stack, Migration](02-processing-flow.md) | graduate | The hyperbola drifts by $12.2\ \mathrm{ms}$ at $4\ \mathrm{km}$ offset; stacking gives $4.48\times$ on random noise and only $0.916$ on coherent |
| 03 | [Velocity Analysis and Moveout Interpretation](03-velocity-analysis.md) | graduate | Semblance width falls from $350$ to $40\ \mathrm{m\,s^{-1}}$ with cable length; a $30^\circ$ dip biases velocity by $+15.5\%$ |
| 04 | [Migration and Imaging: Time vs Depth, Kirchhoff and RTM](04-migration-imaging.md) | research | The migrated peak amplitude is $100\%$ at the correct velocity and $14$-$32\%$ otherwise: focus is the velocity criterion |
| 05 | [AVO/AVA Analysis and Its Assumptions](05-amplitude-vs-offset.md) | doctoral | $A$ and $B$ fix the near-angle curve; a whole family of $(v_p,v_s,\rho)$ fits it, separated only by the third term at $3.39\sigma$ |
| 06 | [Multiple Attenuation: SRME, Radon and Deconvolution](06-multiple-elimination.md) | doctoral | A curvature mute removes $16\%$ of the multiple and costs $15\%$ of the primary — quote both numbers |
| 07 | [Seismic Attributes and Quantitative Interpretation](07-seismic-attributes.md) | graduate | The measured tuning maximum is $20\ \mathrm{m}$, not the $\lambda/4=25\ \mathrm{m}$ rule; detection is contrast, resolution is wavelength |
| 08 | [Time-Lapse (4-D) Seismic and Reservoir Monitoring](08-4d-seismic.md) | doctoral | The difference noise is $\sqrt{2}$ times each survey's; detectability is a repeatability budget, and localisation ($6.02$) is the discriminator |
| 09 | [Structural and Stratigraphic Interpretation](09-interpretation-reflection.md) | graduate | A $40\ \mathrm{m}$ throw is $1.6\times\lambda/4$ and is picked as $55\ \mathrm{m}$ at noise $0.10$: report the throw with its scale and uncertainty |

## Suggested path

**If you are new to reflection seismology:** lessons 01 → 03 in order, running
each demonstration. Lesson 02 is where the data-processing vocabulary appears and
lesson 03 is where velocity — the only unknown that matters — is measured.

**If you come from earthquake seismology:** start with 01 §3.5 (the
impedance trade) and 03, then 05 and 06, which have no counterpart in
source-side seismology.

**If you are preparing a reservoir project:** 05 (AVO), 06 (multiples), 07
(attributes) and 08 (4-D) in order, plus the ★★★ exercises, which are written as
specifications rather than as calculations.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-reflection-principle.md`](01-reflection-principle.md) | Lesson 01 |
| [`02-processing-flow.md`](02-processing-flow.md) | Lesson 02 |
| [`03-velocity-analysis.md`](03-velocity-analysis.md) | Lesson 03 |
| [`04-migration-imaging.md`](04-migration-imaging.md) | Lesson 04 |
| [`05-amplitude-vs-offset.md`](05-amplitude-vs-offset.md) | Lesson 05 |
| [`06-multiple-elimination.md`](06-multiple-elimination.md) | Lesson 06 |
| [`07-seismic-attributes.md`](07-seismic-attributes.md) | Lesson 07 |
| [`08-4d-seismic.md`](08-4d-seismic.md) | Lesson 08 |
| [`09-interpretation-reflection.md`](09-interpretation-reflection.md) | Lesson 09 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Nine runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 06-seismology/09-reflection-seismology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reflection_principle_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python processing_flow_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python velocity_analysis_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python migration_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python avo_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multiple_elimination_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python attributes_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python four_d_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python interpretation_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed, and
exits 0. The slowest (migration, multiple elimination) takes about three
seconds. They require no network access.

## Mastery checkpoint

Complete this without notes:

> **(a)** An interface separates $\rho_1 = 2.30\ \mathrm{g\,cm^{-3}}$,
> $v_1 = 2.80\ \mathrm{km\,s^{-1}}$ from $\rho_2 = 2.45\ \mathrm{g\,cm^{-3}}$,
> $v_2 = 3.20\ \mathrm{km\,s^{-1}}$. Compute $Z_1$, $Z_2$, $R$ and $T$, and state
> whether the reflection is hard or soft.
> **(b)** A reflector at $t_0 = 1.4251\ \mathrm{s}$,
> $v_{\text{rms}} = 2848.1\ \mathrm{m\,s^{-1}}$ is picked at $3000\ \mathrm{m}$
> offset. Compute the hyperbolic moveout and state the sign of the exact-minus-
> hyperbolic residual.
> **(c)** The reflector's true dip is $30^\circ$ and the picked stacking velocity
> is $3200\ \mathrm{m\,s^{-1}}$. Compute the true velocity and the depth error
> from ignoring the dip.
> **(d)** A migrated point diffractor reaches its maximum amplitude
> $89.954$ at $v_{\text{mig}}/v_{\text{true}} = 1.00$ and $25.3$ at $0.95$. State
> which quantity is the velocity criterion and why the position is a weaker one.
> **(e)** A fault throws a marker by $15\ \mathrm{ms}$ at
> $v = 3200\ \mathrm{m\,s^{-1}}$. Compute the throw, compare it with $\lambda/4$
> for $30\ \mathrm{Hz}$, and write the throw as a measurement.

A worked version of (a)-(d) appears in the solutions:
[01](exercises/01-reflection-principle-solutions.md),
[02](exercises/02-processing-flow-solutions.md),
[03](exercises/03-velocity-analysis-solutions.md),
[04](exercises/04-migration-imaging-solutions.md),
[09](exercises/09-interpretation-reflection-solutions.md).

## Common pitfalls across this module

1. **Reading a depth from a time section.** Every depth carries the velocity model
   used to convert it, and the velocity error dominates (lesson 09: $\pm144\
   \mathrm{m}$ from a $4\%$ velocity error versus $\pm4\ \mathrm{m}$ from
   picking).
2. **Expecting stacking to remove coherent noise.** The measured $0.916$ is the
   demonstration; coherent energy needs a moveout-based or model-based method.
3. **Treating the stacking velocity as a rock velocity.** Dips inflate it by
   $1/\cos\theta$ and anisotropy inflates it further; the number is a processing
   parameter first.
4. **Quoting an AVO intercept as the reflection coefficient.** They differ at
   second order, and the difference is stated in the demonstration.
5. **Confusing detection with resolution.** A thin, high-contrast bed is
   detectable long after its thickness becomes unreadable — and the reverse.
6. **Reporting a 4-D anomaly without its localisation.** Random noise can pass any
   amplitude threshold in a large survey; a spatially coherent anomaly cannot.

## Related modules

- [06-07 Ambient Noise and Seismic Interferometry](../07-ambient-noise-and-interferometry/README.md) —
  the same reflection coefficients measured passively.
- [06-08 Receiver Functions and Crustal Structure](../08-receiver-functions-and-crustal-structure/README.md) —
  the same layering measured with conversions.
- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) — velocity
  estimation as an inverse problem.
- [18-inverse-problems](../../18-inverse-problems/README.md) — regularisation,
  resolution and uncertainty quantification.
- [11-exploration-geophysics](../../11-exploration-geophysics/README.md) — where
  these measurements sit in a field programme.
