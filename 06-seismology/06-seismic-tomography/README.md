# Module 06-06 — Seismic Tomography

**Stages:** graduate → research · **Prerequisites:** modules 06-01 and 06-02;
linear algebra and an inverse-problems course.

This module is about the step from "we measured some travel times" to "here is a
picture of the interior", and about the two things that step destroys. The first
is uniqueness: a travel time is an average of slowness along a path, so a finite
set of paths samples only a subspace of the possible Earth, and inside the
complement of that subspace every answer is equally consistent with the data. The
second is resolution: even in the sampled subspace the answer is a smoothed
version of the truth, and the smoothing has a direction. Neither can be removed
by a better algorithm, and both can be quantified — which is what every lesson
here does.

The module therefore follows one honest difficulty through seven lessons. Lesson
01 writes the datum as a path integral and exhibits two models that fit the same
data to machine precision. Lesson 02 shows that the parametrisation — grid,
basis, damping — is a hypothesis, and measures what refining the grid does to the
answer (it makes it worse). Lesson 03 makes resolution and covariance into
matrices and checks them against known-model tests. Lessons 04 and 05 move to
waveforms: why the misfit surface has a chain of local minima, how frequency
continuation navigates it, and how the adjoint computes a gradient for the price
of one extra propagation. Lessons 06 and 07 apply all of it where the stakes are
highest — the global mantle — and quantify why two published models of the same
region can differ by more than either model's formal uncertainty.

Every number in this module is produced by a demonstration in `code/`, on
**SYNTHETIC** models. The surveys, velocity profiles, anomalies, noise levels and
conversion factors are chosen teaching values, stated in each file; no real
station, event, catalogue, survey or published Earth model is used, and no
published measurement is quoted.

## Learning objectives

By the end of this module you will be able to:

1. Derive a tomographic datum as a path integral and linearise it about a
   reference model, stating and measuring the two neglected terms.
2. Build a Jacobian for a stated parametrisation and solve the resulting inverse
   problem both directly and iteratively, with a stated parameter-choice rule.
3. Compute and interpret the resolution matrix, the null space and the model
   covariance of a tomographic problem, and design a known-model test for it.
4. Explain cycle skipping as a property of the objective function and the
   frequency band, and design a frequency-continuation schedule from measured
   basin widths.
5. Derive the discrete adjoint of a wave-equation solver, verify it with a
   dot-product test, and explain what a finite-frequency sensitivity kernel is
   and is not.
6. Explain what a global mantle model is a filtered and damped version of, and
   propagate the resulting uncertainties into a geodynamic interpretation.
7. Compare two tomographic models of the same region with a reproducible
   protocol, and decide which differences are supported by the data.

## Prerequisites

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  P and S waves and the elastic wave equation.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  the ray parameter, Snell's law and ray tracing.
- [18-01 Foundations of Inverse Problems](../../18-inverse-problems/01-inverse-problem-foundations/README.md) —
  well-posedness, null space and discretisation.
- [03-02 NumPy and Array Computing](../../03-scientific-computing/02-numpy/README.md) —
  the linear algebra used in every demonstration.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [The Tomography Principle: Data as Path Integrals](01-tomography-principle.md) | graduate | A datum is an average along a path; two models can fit the same data to $10^{-15}$ |
| 02 | [Travel-Time Tomography: Parametrisation and Inversion](02-travel-time-tomography.md) | doctoral | The grid, the basis and the damping are hypotheses; refining the grid makes the image worse |
| 03 | [Resolution, Null Space and Model Covariance](03-resolution-and-nullspace.md) | doctoral | Resolution is a matrix with a direction; errors in neighbouring cells are correlated |
| 04 | [Full-Waveform Inversion: Objective Functions and Reliability](04-full-waveform-inversion.md) | research | Cycle skipping is measured in periods; a smaller misfit can mean a worse model |
| 05 | [The Adjoint Method for Efficient Sensitivity Computation](05-adjoint-methods.md) | research | One extra propagation gives every derivative; the kernel is one wavelength wide |
| 06 | [Global Mantle Tomography and Its Geodynamic Interpretation](06-global-mantle-tomography.md) | doctoral | Depth and amplitude trade off; temperature anomalies are derived, not observed |
| 07 | [Resolving Discrepancies Between Tomographic Models](07-tomography-controversies.md) | research | Disagreement concentrates where coverage is poor; agreement is not accuracy |

## Suggested path

**If you are new to tomography:** lessons 01-03 in order, running each
demonstration and reading its tables rather than its conclusions. Lesson 03 is
where the practical limits become numbers.

**If you already run inversions:** read 01 §4-5 (null space and aperture), then
02 §4-5 (grid and regularisation), then 07 — the comparison protocol at the end
is the part that is usually missing from a published disagreement.

**If you are preparing a waveform project:** 04 §3-4 (cycle skipping and
continuation), 05 in full (the adjoint, its verification and the kernel), and
then 06 §3 (the trade-off that amplitudes are supposed to break).

**If you are preparing a research project:** 03 §5-6 (trade-off and known-model
tests), 05 §6 (how far a gradient can be trusted) and the ★★★ exercises
throughout.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-tomography-principle.md`](01-tomography-principle.md) | Lesson 01 |
| [`02-travel-time-tomography.md`](02-travel-time-tomography.md) | Lesson 02 |
| [`03-resolution-and-nullspace.md`](03-resolution-and-nullspace.md) | Lesson 03 |
| [`04-full-waveform-inversion.md`](04-full-waveform-inversion.md) | Lesson 04 |
| [`05-adjoint-methods.md`](05-adjoint-methods.md) | Lesson 05 |
| [`06-global-mantle-tomography.md`](06-global-mantle-tomography.md) | Lesson 06 |
| [`07-tomography-controversies.md`](07-tomography-controversies.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable, print-only demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 06-seismology/06-seismic-tomography/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tomography_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python travel_time_tomography_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resolution_and_nullspace_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python full_waveform_inversion_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python adjoint_methods_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python global_mantle_tomography_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tomography_controversies_demo.py
```

`tomography_demo.py` is the module's original demonstration and covers lessons
01-03 in five sections. The other six are the companions of lessons 02-07
respectively. Every demo prints labelled results with units, uses a fixed random
seed (`np.random.default_rng(20261014)`), needs no network, and exits 0; none
plots anything.

## Mastery checkpoint

Complete this without notes.

> A cross-hole survey over $16\ \mathrm{km}\times5.5\ \mathrm{km}$ is recorded
> with 144 rays, discretised into $16\times12$ cells, and inverted with damping
> chosen to reach a misfit of $5.5\times10^{-2}\ \mathrm{s}$ at a stated noise of
> 5 ms.
>
> **(a)** State the two numbers the inversion must report for the image to be
> reproducible, and explain what each one controls.
> **(b)** The resolution matrix has $\operatorname{tr}R = 109.3$ and a median
> diagonal of 0.618. Give the effective parameter count and the typical
> point-spread length in $x$ and $z$, and say which direction is worse.
> **(c)** A waveform inversion of the same region reaches a final misfit that is
> 0.07 times the expected noise misfit over the full record. Say whether that is
> evidence of overfitting, and state what you would compute to decide.
> **(d)** Your result differs from a published model by 1 per cent in a cell with
> $|R_{kk}| = 0.25$. Write the two sentences you would report.

A worked version of (b) is in the lesson-03
[solutions](exercises/03-resolution-and-nullspace-solutions.md), and of (c) in
the lesson-04 [solutions](exercises/04-full-waveform-inversion-solutions.md).

## Common pitfalls across this module

1. **Quoting a model without its resolution.** Every table in this module that
   looks like a result is a statement about a parametrisation and a damping.
2. **Reading a small data misfit as accuracy.** A finer grid fits the data better
   and is further from the truth; a continuation schedule reached misfit zero.
3. **Treating the null space as a technicality.** It is where the honest
   uncertainty lives, and it is why two published models can differ without
   either being wrong.
4. **Believing amplitudes.** They carry the information that breaks the
   depth-velocity trade-off and are the least reliable part of a real seismogram.
5. **Comparing models without comparing coverages.** Disagreement measured here:
   correlation 0.050 in the worst-covered quarter, 0.447 in the best.
6. **Reporting "the adjoint method" as if it were a verification.** The gradient
   must be tested, node by node, against finite differences and by a dot-product
   test.
7. **Presenting a derived quantity as an observation.** A temperature anomaly is
   a damped, filtered velocity anomaly divided by an assumed conversion factor.
8. **Forgetting that the reference model is part of the answer.** Changing it
   changes the rays, the Jacobian and the neglected second-order term.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) and
  [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  the physics this module inverts.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  the same inversion machinery applied to amplitude and $t^*$.
- [06-07 Ambient Noise and Interferometry](../07-ambient-noise-and-interferometry/README.md) —
  an independent data type with the same resolution questions.
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) — the same
  wave equation with a dense controlled-source geometry.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of every idea used here.
