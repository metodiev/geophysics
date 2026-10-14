# Module 13-07 — Tectonics, Surface Processes and Climate Coupling

**Stages:** research · **Prerequisites:** modules
[13-04](../04-tectonophysics-deformation/README.md) and
[13-06](../06-crustal-and-lithospheric-dynamics/README.md); climate and
palaeoclimate ([16-04](../../16-atmosphere-climate/04-climate-system-and-feedbacks/README.md),
[16-06](../../16-atmosphere-climate/06-palaeoclimate/README.md)).

This module closes the folder by following the boundary between the solid Earth
and the atmosphere: erosion, river incision and the carbon cycle. A thermochronometer
records cooling, and cooling records exhumation (13-07-01); a river profile records
the ratio of uplift to erodibility (13-07-02); and silicate weathering consumes
CO$_2$, so the erosion of fresh rock is a climate forcing on million-year
timescales (13-07-03). The chain from tectonics to climate runs through the surface
processes in the first two lessons, and the third asks how much of a climate
history that chain can explain.

The central honest difficulty is that in every step of the chain the interesting
quantity enters as part of a *ratio or a product*, and the surface record contains
no internal evidence about how the product is divided. An age–elevation slope gives
$1/E$ only in a steady state, and gives a different number when the exhumation
rate has changed. A steepness index gives $U/K$ exactly and $U$ not at all. A
palaeo-temperature gives a combination of the weathering law's two exponents. Each
lesson measures the size of the degeneracy, states which independent observation
breaks it, and reports the answer conditional on the assumptions that remain.

All models and data in this module are **SYNTHETIC**. The closure temperatures,
exhumation histories, drainage networks, erosion parameters and carbon-cycle
parameters are chosen teaching values with units; no measured age, mapped river
or published carbon-cycle model is used, and every printed number comes from the
demonstration in the lesson that uses it.

## Learning objectives

By the end of this module you will be able to:

1. **Distinguish** rock uplift, surface uplift and exhumation, and state which of
   them a thermochronometer measures.
2. **Derive** the steady geotherm with exhumation and **compute** the Péclet
   number and the closure depth.
3. **Show** that the age–elevation slope is exactly $1/E$ in steady state and
   that the closure temperature cancels from it.
4. **Quantify** the bias a transient exhumation history puts into a steady-state
   inference, and recognise the break in slope that reveals it.
5. **Compute** the topographic perturbation of the closure isotherm and the age
   shift it produces.
6. **Derive** the steady stream-power profile, its concavity and its steepness
   index.
7. **Perform** a $\chi$ transform and **interpret** the residual curvature as
   signal.
8. **Demonstrate** the exact $U/K$ degeneracy and **state** which observation
   breaks it.
9. **Solve** the transient stream-power equation and **compute** a knickpoint
   propagation speed.
10. **Formulate** a carbonate–silicate box model and **derive** its
    steady-state sensitivity and equilibration time.
11. **Quantify** the degeneracy between weathering-law parameters that the
    present-day state leaves open.
12. **Distinguish** a tectonic-forcing explanation of a climate trend from a
    feedback explanation, and name the observation that separates them.

## Prerequisites

- [13-07-01 Erosion, Uplift and Thermochronology](01-erosion-and-uplift.md) —
  the first lesson of this module; lessons 02 and 03 build on it.
- [13-04-01 Crustal Deformation from GNSS and Strain Rates](../04-tectonophysics-deformation/01-crustal-deformation-gps.md) —
  the geodetic uplift rates that complement exhumation.
- [13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength](../06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md) —
  the vertical motions that set surface elevation.
- [02-05-04 Heat Conduction](../../02-physics/05-thermodynamics/04-heat-conduction.md) —
  the thermal physics of lesson 01.
- [16-04 Climate System and Feedbacks](../../16-atmosphere-climate/04-climate-system-and-feedbacks/README.md) —
  the climate sensitivity used in lesson 03.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Erosion, Uplift and Thermochronology](01-erosion-and-uplift.md) | research | The age–elevation slope is exactly $1/E$ in steady state, and the closure temperature cancels from it |
| 02 | [River Profiles, Steepness Indices and Uplift Inference](02-river-profile-tectonics.md) | doctoral | Only $U/K$ is measurable; the knickpoint speed is the one escape |
| 03 | [Tectonic-Climate Feedbacks on Geological Timescales](03-tectonics-climate-feedback.md) | research | The present-day state constrains no weathering parameter; the direction is robust, the magnitude is not |

## Suggested path

**If you are new to the subject:** lessons 01 and 02 in order. They answer the same
question — how fast is this landscape rising — with two independent methods, and
the comparison between them is the point.

**If you work on palaeoclimate or the carbon cycle:** lesson 03, after reading
01 §3 for the timescale language; the box model of 03 §2 is deliberately minimal.

**If you are preparing a research project:** 01 §4–5 (what a slope does and does
not measure), 02 §4–6 (the exact degeneracy and the transient escape) and 03 §5
(the parameter degeneracy), plus the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-erosion-and-uplift.md`](01-erosion-and-uplift.md) | Lesson 01 |
| [`02-river-profile-tectonics.md`](02-river-profile-tectonics.md) | Lesson 02 |
| [`03-tectonics-climate-feedback.md`](03-tectonics-climate-feedback.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 13-geodynamics-tectonics/07-geomorphology-tectonics-climate/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python erosion_and_uplift_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python river_profile_tectonics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tectonics_climate_feedback_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), is print-only (no figures, no network) and
exits 0; each takes under two seconds.

## Mastery checkpoint

Complete this without notes:

> A range has an age–elevation relation that is linear over 3 km of relief, with a
> slope of 4 Ma/km, and a river network whose steepness index in the headwaters is
> twice that near the outlet at the same concavity. **(a)** Convert the slope to an
> exhumation rate and state the assumption the conversion needs. **(b)** Explain
> what the steepness-index contrast can and cannot mean. **(c)** Name the two
> independent observations that would convert each into an uplift rate, and state
> what each measures. **(d)** State one way in which the two could be consistent
> with each other, and one way in which they could differ, and which you would
> believe.

A worked version of (a)–(c) appears in the lesson-01 and lesson-02
[solutions](exercises/01-erosion-and-uplift-solutions.md).

## Common pitfalls across this module

1. **Reporting surface uplift from a thermochronological slope.** It measures
   exhumation; separating the two needs a surface datum.
2. **Quoting an uplift rate from a steepness index.** A $K$ was assumed, and the
   demonstration's degeneracy is exact.
3. **Fitting a single age–elevation line through a two-stage history.** The
   measured bias reaches a factor of five.
4. **Trusting the $R^2$ of a $\chi$ plot to pin the concavity.** $R^2 = 0.999$
   admits concavity errors that change $k_s$ by a factor of four.
5. **Reading the weathering-law parameters off the present state.** Three sets
   that agree today disagree by a factor of 6.3 about the past.
6. **Attributing a climate trend to tectonics without an outgassing history.**
   Forcing and feedback are degenerate in the same way as $U$ and $K$.

## Related modules

- [13-04 Tectonophysics and Deformation](../04-tectonophysics-deformation/README.md) —
  the deformation these surface processes record.
- [13-06 Crustal and Lithospheric Dynamics](../06-crustal-and-lithospheric-dynamics/README.md) —
  the vertical motions that set the boundary conditions.
- [16-atmosphere-climate](../../16-atmosphere-climate/README.md) — the climate
  system the last lesson couples to.
- [04-earth-science-geology](../../04-earth-science-geology/README.md) —
  geomorphology and Quaternary geology in their own right.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general theory
  of the degeneracies measured in all three lessons.
