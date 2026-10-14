# Module 12-02 — Composition and Mineral Physics

**Stages:** doctoral → research · **Prerequisites:** modules 12-01 (seismic structure),
02-04 (elasticity), 02-05 (thermodynamics), 02-11 (physics of the Earth's interior);
comfort with partial derivatives, logarithms and numerical root finding.

> **All models and data in this module are SYNTHETIC.** Every density, elastic
> constant, pressure, temperature, tensor component and heat flow in these lessons is
> a chosen teaching value, printed by a demonstration in `code/`. Layer names and
> depths such as "CMB 2891 km" or "olivine" are used as conventional labels, in the
> way a map uses named towns. No measurement, experiment, equation-of-state fit,
> computation or published tensor is reproduced here.

This module answers a question that seismology can pose but cannot settle: *what is
the Earth made of?* A reference model returns velocity and density as functions of
radius, and nothing in the data carries a composition label. The bridge is mineral
physics, and it is built out of three routes to the same numbers — natural and
experimental samples, high-pressure experiments, and ab initio computation. Each
route is developed as a method in its own right: what it measures, what it assumes,
and how large the residual ambiguity is. The recurring object is the **assemblage**:
a rock is a mixture of phases, each with its own elastic tensor and equation of
state, and the aggregate's properties are an average that depends on the averaging
scheme chosen.

The second discipline is that **a deficit is a number and a composition is a model**.
An outer core 8 % lighter than pure iron at the same pressure and temperature is a
measurement-derived number; converting it to "10 % light elements" requires an
assumed density contrast, and the same deficit spans a factor of three in the
inferred fraction. Every lesson therefore separates the observable from the
inversion, and states the assumption that closes the gap.

The third is that **uncertainty has structure**. An ab initio elastic tensor is
useless until it passes a Born-stability test; a mixing model's answer depends on
which average (Voigt, Reuss, Hill) it uses; a diamond-anvil pressure inherits the
uncertainty of its pressure scale; an inner-core age is a ratio of assumed
quantities and diverges as conduction consumes the heat budget. Where a single number
would be comforting, the module gives the range and says what would narrow it.

## Learning objectives

By the end of this module you will be able to:

1. **Build** an isotropic-equivalent model of a multi-phase assemblage from
   single-crystal moduli and volume fractions, and **explain** why the result
   brackets between the Reuss and Voigt bounds.
2. **Construct and read** a diamond-anvil pressure–volume dataset, use a pressure
   scale, and **quantify** how a scale's uncertainty propagates into an inferred
   equation of state.
3. **Compute** the elastic constants of a crystal from a stiffness tensor — Voigt,
   Reuss and Hill moduli, the Christoffel speeds, the Born stability criteria — and
   **connect** a single-crystal anisotropy to a seismic splitting measurement.
4. **Compute** the density deficit of the core against a pure-iron reference state at
   the same pressure and temperature, and **convert** it to a light-element mass
   fraction under an explicit, testable mixing assumption.
5. **Derive and evaluate** the adiabatic gradient of the core, the heat conducted down
   the adiabat, the cooling rate and the inner-core age, and **state** which assumed
   quantity dominates each one.
6. **Justify** the geodynamo from the magnetic Reynolds number and **explain** the
   compositional buoyancy released by inner-core growth.
7. **State**, for any result in this module, which inputs are assumed, which are
   derived, and how much the conclusion changes if an assumption is relaxed.

## Prerequisites

- [12-01 Seismic Structure of the Earth](../01-seismic-structure-of-the-earth/README.md) —
  the velocity and density profiles this module interprets.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md) —
  the stiffness tensor, anisotropy and the Christoffel equation.
- [02-05 Thermodynamics](../../02-physics/05-thermodynamics/README.md) —
  equations of state, the Grüneisen parameter and adiabatic gradients.
- [02-11 Physics of the Earth's Interior and Atmosphere](../../02-physics/11-physics-of-earths-interior-and-atmosphere/README.md) —
  pressure–density relations and the seismic parameter.
- [04-01 Earth Structure](../../04-earth-science-geology/01-earth-structure/README.md) —
  the geological framing of a layered planet.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Mantle Composition and Peridotite Models](01-mantle-composition.md) | doctoral | An assemblage is an average: the same phases give different moduli under Voigt, Reuss and Hill, and the ordering of the bounds is itself a check |
| 02 | [High-Pressure Experiments and Diamond Anvil Cells](02-high-pressure-experiments.md) | research | Pressure is not measured in a diamond cell, it is *assigned* by a scale; the scale's error becomes the equation of state's error |
| 03 | [Ab Initio Mineral Physics and Elastic Constants](03-ab-initio-mineral-physics.md) | research | A computed tensor is only usable after a Born-stability test; the anisotropy a seismologist sees is crystal anisotropy *times* alignment |
| 04 | [Core Composition, Light Elements and the Geodynamo](04-core-composition.md) | research | A density deficit is a number, a composition is a model; the inner-core age is a ratio of assumed quantities |

## Suggested path

**If you are new to mineral physics:** lesson 01 first — it establishes the two ideas
everything else uses, namely that an assemblage is an average and that the average is
not unique without an assumption.

**If you know the mantle already:** 02 and 03 in either order, running each
demonstration and reproducing the sensitivity tables by editing the input constants.
The two lessons are deliberately complementary: one is the experimental route to an
equation of state, the other the computational route to a tensor.

**If you are preparing research:** 03 for the computation-to-seismology workflow
(and the alignment/degeneracy arithmetic), then 04 for a worked example of an
inverse problem in which the uncertainty is dominated by the assumptions, not the
data. The ★★★ exercises in each companion set are written as research designs.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-mantle-composition.md`](01-mantle-composition.md) | Lesson 01 |
| [`02-high-pressure-experiments.md`](02-high-pressure-experiments.md) | Lesson 02 |
| [`03-ab-initio-mineral-physics.md`](03-ab-initio-mineral-physics.md) | Lesson 03 |
| [`04-core-composition.md`](04-core-composition.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations, one per lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 12-global-geophysics-interior/02-composition-and-mineral-physics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mantle_composition_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python high_pressure_experiments_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ab_initio_mineral_physics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python core_composition_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0. Each one
runs in about a second. They are print-only: no plots are produced, so the output can
be compared line by line with the tables in the lessons.

## Mastery checkpoint

Complete this without notes:

> An assumed pure-iron equation of state with $\rho_0 = 8.00$ g cm$^{-3}$,
> $K_0 = 160$ GPa, $K_0' = 5.0$ and $\alpha = 10^{-5}$ K$^{-1}$ gives
> $\rho_\text{Fe} = 10.794$ g cm$^{-3}$ at 126 GPa and 4000 K. The seismological
> density at the top of the outer core is 9.900 g cm$^{-3}$.
> **(a)** Compute the density deficit.
> **(b)** With an assumed light-element density of 5.0 g cm$^{-3}$, compute the
> light-element mass fraction, and state the assumption that makes the number
> meaningful.
> **(c)** State what the fraction becomes at 6.5 g cm$^{-3}$, and explain why the
> deficit alone cannot decide between the two.
> **(d)** The same reference EOS gives 12.874 g cm$^{-3}$ at the ICB; the model
> density there is 12.150 g cm$^{-3}$. State whether the deficit grows or shrinks
> with depth, and what that implies about a uniformly mixed core.

Worked versions appear in the lesson-04 solutions
([04](exercises/04-core-composition-solutions.md)).

## Common pitfalls across this module

1. **Comparing a computed quantity with a measured one without stating the averaging
   scheme or the reference state.** Voigt, Reuss and Hill differ by 7 % in the shear
   modulus of a typical mineral.
2. **Quoting an anisotropy percentage without its definition.** Extremal and axial
   measures of the same crystal differ by a factor of 2.2.
3. **Treating a pressure as a measured quantity in a diamond cell.** It is assigned
   by a scale; the scale is an assumption.
4. **Using an unthermalised equation of state.** The thermal correction is 4–5 % at
   core conditions, larger than most of the effects being discussed.
5. **Reading a light-element fraction without its density contrast.** The same deficit
   gives 4 % or 14 % depending on that one input.
6. **Turning a product into a quotient.** Seismology measures (crystal anisotropy ×
   alignment), and the core's density deficit is (composition × temperature); reporting
   either factor alone is an overclaim.
7. **Reporting an age, a depth or a temperature as a measurement when it is a ratio
   of assumed quantities.** The inner-core age is the clearest example, and it
   diverges as conduction consumes the heat budget.

## Related modules

- [Module 12-01 Seismic Structure of the Earth](../01-seismic-structure-of-the-earth/README.md) —
  the observations this module interprets.
- [06-06 Seismic Tomography](../../06-seismology/06-seismic-tomography/README.md) —
  what the velocity anomalies and their amplitudes do and do not constrain.
- [05-09 Geothermal and Heat Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md) —
  the measurement side of the core's heat budget.
- [08-01-05 The Geodynamo: Mechanism and Evidence](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/05-dynamo-theory.md) —
  the induction equation and the numerical dynamo in full.
- [13-02 Mantle Convection](../../13-geodynamics-tectonics/02-mantle-convection/README.md) —
  the convective framework that delivers the core's heat to the surface.
- [07-01 Gravity Fundamentals](../../07-gravity-geodesy/01-gravity-fundamentals/README.md) —
  the mass and moment of inertia that every radial model must satisfy.
- [02-11 Physics of the Earth's Interior and Atmosphere](../../02-physics/11-physics-of-earths-interior-and-atmosphere/README.md) —
  the equations of state and seismic parameter relations used throughout.
