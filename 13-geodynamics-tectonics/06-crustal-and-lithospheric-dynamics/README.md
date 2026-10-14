# Module 13-06 — Crustal and Lithospheric Dynamics

**Stages:** advanced → research · **Prerequisites:** modules
[13-01](../01-geodynamic-principles/README.md) and
[13-05](../05-geodynamic-modelling/README.md); gravity and geodesy
([07-03](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/README.md),
[07-04](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md)).

This module is about the solid Earth's response to a load, at the length scales
and timescales where the response is what we can actually measure. Three loads
with three different response laws: a topographic or tectonic load on an elastic
plate (flexure, module 13-06-01), a pressure source in an elastic half-space
(volcano geodesy, 13-06-02), and an ice load on a viscous mantle (glacial
isostatic adjustment, 13-06-03). In all three, the observation is a surface
displacement or a gravity field, and the inference is a *parameter of the
sub-surface*: an effective elastic thickness, a source depth and volume change,
or a mantle viscosity.

The central honest difficulty is the same in all three lessons and is worth
naming once: **the parameter you want is not the quantity you measure.** The
measured surface pattern depends on a product of a rigidity and a load geometry
(13-06-01), of a depth and a volume change (13-06-02), and of a viscosity and an
ice history (13-06-03). In each case the trade-off is broken by the *shape* of the
data — the wavelength dependence of the admittance, the profile of the
deformation field, the wavelength dependence of the relaxation — and not by the
precision of any single number. Every lesson measures the trade-off, reports the
admitted set, and states which additional observable would close it.

All models and data in this module are **SYNTHETIC**. The densities, elastic
thicknesses, source parameters and ice histories are chosen teaching values with
units; no measured lithosphere, volcano or ice sheet is used, and every printed
number comes from the demonstration in the lesson that uses it.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the Airy compensation condition and **compute** crustal roots and
   the gravity effect of a compensated load.
2. **Derive** the flexural plate equation, the rigidity $D$, the flexural
   parameter $\alpha$ and the wavelength-dependent reduction factor.
3. **Derive** the gravity admittance of a compensated load and **measure** the
   $(T_e, t)$ trade-off it leaves open.
4. **Report** an effective elastic thickness as an admitted set with its load
   model stated.
5. **Compute** the Mogi surface displacement and **verify** its exact ratios.
6. **Project** displacements onto ascending and descending look vectors and
   **quantify** the conditioning and the neglected-component leak.
7. **Invert** line-of-sight data for source depth and volume change and **state**
   the admitted range from a $\chi^2$ criterion.
8. **Show** which source shapes surface geodesy can and cannot resolve.
9. **Derive** the relaxation time of a harmonic load on a viscous half-space and
   **compute** present-day uplift for a synthetic ice history.
10. **Decompose** relative sea level into eustatic and solid-surface terms and
    **explain** why near-field records are not ice-volume proxies.
11. **Quantify** the (viscosity, ice history) trade-off given by a single uplift
    rate.

## Prerequisites

- [13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure](../01-geodynamic-principles/03-lithospheric-strength.md) —
  the concept of $T_e$ used throughout.
- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](../01-geodynamic-principles/02-rheology-of-earth.md) —
  the constitutive laws of the elastic and viscous limits.
- [13-05 Geodynamic Modelling Practice](../05-geodynamic-modelling/README.md) —
  the numerical and verification habits these lessons use.
- [07-03 Gravity Anomalies and Modelling](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/README.md) —
  the gravity observations of lesson 01.
- [07-04 Geodesy and Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md) —
  the displacement measurements of lessons 02 and 03.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Isostasy and Flexure: Modelling Lithospheric Strength](01-isostasy-flexure-modelling.md) | doctoral | Compensation reduces an anomaly without removing it; $T_e$ and the compensation depth trade off |
| 02 | [Volcano Deformation, Magma Chamber Models and InSAR](02-volcano-geodesy.md) | research | The depth–volume degeneracy is broken by profile shape, not by amplitude; shape itself is barely constrained |
| 03 | [Glacial Isostatic Adjustment: Ice, Viscosity and Sea Level](03-glacial-isostatic-adjustment.md) | research | The present-day uplift rate is non-monotonic in viscosity, so it constrains neither parameter alone |

## Suggested path

**If you are new to the lithosphere's response:** lesson 01 in full, then lesson
03. Lesson 01's admittance derivation and lesson 03's relaxation derivation are
the same physics with a different constitutive law, and reading them together is
worth more than either alone.

**If you work with volcano or earthquake geodesy:** lesson 02, then lesson 03 §4–6
for the time-dependent analogue and its uncertainties.

**If you are preparing a research project:** the error-budget and admitted-set
sections of all three lessons (01 §6, 02 §5, 03 §6) plus the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-isostasy-flexure-modelling.md`](01-isostasy-flexure-modelling.md) | Lesson 01 |
| [`02-volcano-geodesy.md`](02-volcano-geodesy.md) | Lesson 02 |
| [`03-glacial-isostatic-adjustment.md`](03-glacial-isostatic-adjustment.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python isostasy_flexure_modelling_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python volcano_geodesy_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python glacial_isostatic_adjustment_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), is print-only (no figures, no network) and
exits 0; each takes one to three seconds.

## Mastery checkpoint

Complete this without notes:

> A gravity admittance is measured over $100 \le \lambda \le 800$ km with 1%
> noise. **(a)** Write the admittance of a surface load with a single
> compensation interface at depth $t$ and explain which combination of $T_e$ and
> $t$ the data constrain. **(b)** Given that $T_e = 25$ km fits with $t = 34.7$ km
> at 1.01% rms and $T_e = 20$ km fits with $t = 41.0$ km at 4.10%, state which
> models the data admit and why a single $T_e$ cannot be quoted. **(c)** Name the
> observation that would break the trade-off and explain which wavelength band it
> must constrain.

A worked version of (a)–(b) appears in the lesson-01
[solutions](exercises/01-isostasy-flexure-modelling-solutions.md).

## Common pitfalls across this module

1. **Quoting a depth, thickness or viscosity without the trade-off partner.**
   Every lesson in the module measures one.
2. **Treating an amplitude fit as a parameter measurement.** In 02 the peak
   displacement is matched by a factor of 400 range in volume.
3. **Forgetting the neglected component.** In 02 the ignored north motion leaks
   14.06% into the solved vertical.
4. **Assuming compensation removes an anomaly.** In 01 it reduced it to 66.7% at
   a 200 km wavelength.
5. **Reading relative sea level as ice volume.** In 03 the eustatic term is
   hundreds of times smaller than the solid-surface term near the load.
6. **Expecting more precision to resolve a parameter degeneracy.** It does not;
   only a different observable does.

## Related modules

- [13-01 Geodynamic Principles](../01-geodynamic-principles/README.md) — the
  rheology and strength concepts used here.
- [13-05 Geodynamic Modelling Practice](../05-geodynamic-modelling/README.md) —
  verification, error budgets and inverse-problem structure.
- [13-07 Tectonics, Surface Processes and Climate Coupling](../07-geomorphology-tectonics-climate/README.md) —
  the surface response that follows the vertical motions inferred here.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — the observations.
- [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md) —
  the deeper structure that sets the parameters being inverted.
