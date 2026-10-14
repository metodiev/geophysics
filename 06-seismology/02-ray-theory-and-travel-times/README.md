# Module 06-02 — Ray Theory and Travel Times

**Stages:** advanced → doctoral · **Prerequisites:** module 06-01; multivariable
calculus, vector calculus and numerical differentiation.

This module is the geometric backbone of seismology. It takes the wave equation
of [06-01](../01-elastic-wave-propagation/README.md), reduces it in the
high-frequency limit to the eikonal equation, and follows the consequences all the
way to the tables and curves that real interpretations are built on: rays, Snell's
law in layers, the travel-time curve, the $\tau$-$p$ transform, numerical ray
tracing, shadow zones, triplications and grid eikonal solvers. Six lessons, six
runnable demonstrations, and one thread — the ray parameter and the travel time —
connective through all of them.

The module's central honest difficulty is that **ray theory computes times and
nothing else**. It is exact in its own limit and silent outside it: it gives no
amplitudes, so it cannot say how loud a caustic is; it gives no answer at all in a
shadow, so the energy observed there is evidence for a different mechanism, not
for a small ray amplitude; and it carries no uncertainty, so every error bar
attached to a ray result has to be carried in from the data or the model. A second
difficulty compounds the first: the relationship between a travel-time curve and
the structure beneath it is *not unique*. A low-velocity layer leaves no arrival
to invert, and a triplication gives several arrivals for one distance. Each lesson
states which of these it is dealing with, and the demonstrations measure the
non-uniqueness rather than describing it.

A third theme runs through the code: **agreement is not accuracy**. Two solvers
sharing a discretisation agree to machine precision and disagree with the truth by
tens of milliseconds; a tracer agrees with an independent engine to $10^{-4}$ and
degrades visibly where the model is discontinuous; a Monte-Carlo ensemble shows a
1 % velocity error producing a 2 % travel-time scatter. Every lesson therefore
reports what was compared with what, and never quotes a residual without saying
what the reference was.

**All models and data in this module are SYNTHETIC.** The velocity models,
thicknesses and gradients are chosen teaching values, not measurements, and no
station, event or waveform from the real Earth appears in this module. Where a
demonstration compares against a standard reference model that ships with the
software (ObsPy's `iasp91`, used in lessons 03–05), that model is named; it is not
data collected for this repository, and every number quoted in the lessons is
printed by a demonstration in `code/` when it runs.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the eikonal equation from the wave equation, obtain the ray
   equations as its characteristics, and state the frequency regime in which the
   reduction is valid.
2. **Derive** $p = \sin i/v$ as a conservation law, build the travel-time curve of
   a layered stack, and invert its slopes and intercepts while stating the
   velocity assumptions each depth depends on.
3. **Transform** travel times into intercept functions, use Benndorf's relation,
   and quantify the noise amplification that differentiating introduces.
4. **Trace** rays numerically in one dimension, validate a tracer against both a
   closed form and an independent engine, and identify where and why agreement
   degrades.
5. **Predict and measure** the shadow zone produced by a velocity decrease with
   depth, locate the core–mantle boundary from it, and count the arrivals in a
   triplication.
6. **Solve** the eikonal equation on a grid with marching and sweeping, measure the
   convergence order of both, and rank discretisation error against model error.
7. **State** what ray theory cannot do — amplitudes, shadows, later arrivals,
   error bars — and name the method that covers each gap.

## Prerequisites

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the wave equation, P and S speeds, and the body-wave arrival nomenclature used
  throughout this module.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../../01-mathematics/06-multivariable-calculus/01-partial-derivatives.md)
  — the gradient and directional derivative.
- [01-09-03 The Wave Equation and Its Physical Content](../../01-mathematics/09-partial-differential-equations/03-wave-equation.md)
  — hyperbolic equations and characteristics.
- [01-12-03 Numerical Differentiation and Finite-Difference Stencils](../../01-mathematics/12-numerical-methods/03-numerical-differentiation.md)
  — truncation error, which every measurement in this module reports.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Eikonal Equation, Rays and Fermat's Principle](01-eikonal-and-rays.md) | graduate | Rays are the characteristics of $\lvert\nabla T\rvert = 1/v$; the derivation drops the term that carries amplitudes |
| 02 | [Snell's Law, Layered Media and the Travel-Time Curve](02-snell-and-layering.md) | advanced | $p = \sin i/v$ is conserved, so a branch's slope is a velocity and its intercept is a weighted thickness sum — never a depth alone |
| 03 | [The tau-p Transform and Intercept Time](03-tau-p.md) | graduate | $\tau(p)$ is the Legendre transform of $T(X)$; it linearises layering and amplifies picking noise in inverse proportion to the $p$-spacing |
| 04 | [Ray Tracing in Laterally Varying Media](04-ray-tracing.md) | graduate | The two-point problem is a root-finding problem with more than one root; a validated tracer and an honest error budget |
| 05 | [Shadow Zones, Triplications and the Low-Velocity Zone](05-shadow-zones.md) | graduate | A velocity decrease deletes a ray family: non-detection is not absence |
| 06 | [Wavefront Tracking and the Fast Marching Method](06-wavefront-tracking.md) | doctoral | The viscosity solution gives the first arrival everywhere — including where it means nothing |

## Suggested path

**If you are new to ray theory:** lessons 01–03 in order, running each
demonstration. Lesson 02 is where the geometry becomes practical; lesson 03 is
where its instability appears.

**If you already know Snell's law and travel-time curves:** read 01 §5 (the
validity condition $\varepsilon = f^{-1}\lvert\mathrm{d}v/\mathrm{d}z\rvert$),
then 03 §6 (the price of differentiation) and 05 in full — the shadow and the
triplication are the two places where the standard machinery runs out.

**If you are preparing a research project:** 04 §5 (what breaks in two and three
dimensions), 06 §§4–5 (error budgets and what a first-arrival solver cannot see),
plus the ★★★ exercises of every lesson.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-eikonal-and-rays.md`](01-eikonal-and-rays.md) | Lesson 01 |
| [`02-snell-and-layering.md`](02-snell-and-layering.md) | Lesson 02 |
| [`03-tau-p.md`](03-tau-p.md) | Lesson 03 |
| [`04-ray-tracing.md`](04-ray-tracing.md) | Lesson 04 |
| [`05-shadow-zones.md`](05-shadow-zones.md) | Lesson 05 |
| [`06-wavefront-tracking.md`](06-wavefront-tracking.md) | Lesson 06 |
| [`code/`](code) | Six runnable demonstrations, one per lesson |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and ObsPy. Each
demonstration is print-only (no plots, no files written), prints labelled results
with units, uses the fixed seed `np.random.default_rng(20261014)` wherever it
samples, and exits 0 in well under twenty seconds.

```bash
cd 06-seismology/02-ray-theory-and-travel-times/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python eikonal_and_rays_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python snell_and_layering_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tau_p_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ray_tracing_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python shadow_zones_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python wavefront_tracking_demo.py
```

The demonstrations require no network access. Two of them import
`obspy.taup` to use the `iasp91` reference model that is distributed with ObsPy.

## Mastery checkpoint

Complete this without notes:

> A station at 60° records a $P$ arrival at 608.28 s. **(a)** State what the ray
> parameter means and compute it from the travel-time curve if a second station at
> 61° records 613.52 s. **(b)** Convert the ray parameter to
> $\mathrm{s\,rad^{-1}}$. **(c)** For a first arrival that bottoms at 1548 km
> depth, state whether the ray passed below or above the low-velocity zone and why
> you cannot tell from the arrival time alone. **(d)** Give the two mechanisms by
> which a velocity decrease with depth removes arrivals, and the observable that
> distinguishes them. **(e)** State one quantity that a grid eikonal solver
> returns and a ray tracer cannot, and one that a ray tracer returns and a grid
> solver cannot.

The method for (a)–(b) is the numerical differentiation of the travel-time curve
verified in lesson 03 Section 4.2 and lesson 04 Section 3.2; (c)–(e) are answered
in lessons 05 and 06.

## Common pitfalls across this module

1. **Quoting a depth without the velocity model that produced it.** Every depth in
   lessons 02–05 is conditional; the trade-off is the physics, not a caveat.
2. **Reading a ray-theoretic zero as a measurement.** Inside a shadow the correct
   prediction is "no ray", and observed energy there is evidence for diffraction.
3. **Treating non-detection as absence.** A hidden layer produces no arrival at
   any offset, and that silence is only a one-sided constraint.
4. **Refining a grid past the model error.** Once the velocity field dominates the
   budget, smaller $h$ buys digits and not accuracy.
5. **Reading solver-versus-solver agreement as validation.** Two solvers sharing a
   stencil share its error; a closed form or an independent implementation is the
   reference that counts.
6. **Forgetting that a first-arrival solver cannot represent a later branch.** A
   triplication is invisible to it by construction.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the wave equation this module approximates.
- [06-03 Earthquake Sources](../03-earthquake-sources/README.md) and
  [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  where these travel times are used to locate events.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  the amplitudes ray theory deliberately sets aside.
- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) — many ray paths
  combined to localise what one path cannot.
- [06-08 Receiver Functions and Crustal Structure](../08-receiver-functions-and-crustal-structure/README.md) —
  uses the ray parameter derived here as its starting point.
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) and
  [06-10 Refraction and Near-Surface Seismology](../10-refraction-and-near-surface-seismology/README.md) —
  the layered-media results applied at exploration scale.
- [18-inverse-problems](../../18-inverse-problems/README.md) — non-uniqueness,
  regularisation and the unstable derivatives met in lesson 03.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  discretisation, convergence order and error budgets in general.
