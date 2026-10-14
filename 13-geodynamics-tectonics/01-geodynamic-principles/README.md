# Module 13-01 — Geodynamic Principles

**Stages:** graduate → doctoral · **Prerequisites:** conservation laws and the
diffusion equation; continuum mechanics; basic plate-tectonic geology.

This module builds the machinery that every later part of folder 13 uses: the
balance laws, the rheology, the strength of the lithosphere, and the buoyancy
forces that move plates. It is deliberately organised around three
nondimensionalisations rather than three sets of formulae. The Reynolds number
decides that the mantle's momentum equation is a *force balance*, not an equation
of motion; the Péclet number decides whether heat is carried or conducted at a
given scale; and the Deborah number decides whether the same rock is an elastic
solid or a viscous fluid. Nothing in the module is asserted without a number
behind it.

The second theme is non-uniqueness, stated honestly and early. A single Stokes
velocity cannot give both a viscosity and a density contrast. A deflection profile
cannot give both $T_e$ and the load. A single measured delay (elsewhere in this
curriculum) cannot give both a depth and a velocity ratio. Here that theme is made
quantitative: each lesson reports not only a value but the *admitted range* of
values consistent with the data, and the assumption that would have to be relaxed
to narrow it.

The third theme is that the solid Earth is a scaling subject. Every lesson derives
its dimensionless group and states the regime in which the resulting expression is
valid. A formula quoted outside its regime is worse than no formula, and the
exercises are written to reward students who check.

All models and data in this module are **SYNTHETIC**. No measurement, dataset,
station, catalogue or published model value is used or quoted; the parameters are
chosen teaching values, and every number in the lessons is printed by the
demonstration that accompanies it.

## Learning objectives

By the end of this module you will be able to:

1. **Nondimensionalise** the mass, momentum and energy balances of a deforming
   solid Earth and derive the Reynolds, Prandtl and Péclet numbers from them.
2. **Justify** the Stokes approximation from a measured order-of-magnitude
   comparison, and state its regime of validity.
3. **Assemble** a global thermal budget and report a Urey ratio and a cooling time
   with their dominant uncertainties.
4. **Derive** the Maxwell relaxation time, the effective viscosity of a power-law
   creep law and the Arrhenius temperature sensitivity.
5. **Locate** the brittle–ductile transition from a friction law and a creep law
   and state how it moves with the geotherm.
6. **Derive** the flexural rigidity and flexural parameter, verify the isostatic
   area identity, and invert a deflection profile for an admitted range of $T_e$.
7. **Compute** $T_e$ from a yield strength envelope self-consistently and explain
   why $T_e$ is a thermometer rather than a material property.
8. **Compute** ridge push and slab pull as first moments of density anomalies and
   show that the result is independent of the compensation depth.
9. **Close** the plate force balance and distinguish a consistency check from a
   prediction.

## Prerequisites

- [02-01-04 Conservation Laws as the Engine of Physical Modelling](../../02-physics/01-measurement-and-physical-reasoning/04-conservation-laws.md) —
  how a balance law becomes an equation.
- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md) —
  the parabolic equation and its $\sqrt{t}$ scalings.
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md) —
  the rheological models used quantitatively here.
- [04-01-02 Lithosphere, Asthenosphere and the Rheological Definition](../../04-earth-science-geology/01-earth-structure/02-lithosphere-asthenosphere.md) —
  the geological vocabulary this module makes mechanical.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Momentum, Mass and Energy Balances in the Solid Earth](01-momentum-mass-energy.md) | graduate | $Re\sim10^{-22}$: the momentum equation is a force balance; $Pe$ decides who carries heat |
| 02 | [Rheology: Elastic, Viscous, Plastic and Power-Law Creep](02-rheology-of-earth.md) | doctoral | $\eta$ is a law, not a number; stress and temperature each move it by decades |
| 03 | [Lithospheric Strength, Effective Elastic Thickness and Flexure](03-lithospheric-strength.md) | doctoral | $T_e$ is a bending-moment equivalence, and a thermometer |
| 04 | [Driving Forces, Stress Fields and Intraplate Stress](04-forces-and-stresses.md) | doctoral | Slab pull is ten times ridge push; the balance closes but the viscosity is chosen |

## Suggested path

**If you are new to geodynamics:** lessons 01–02 in order, running each
demonstration, then 03 §2–3 only (the flexure basics) and 04 §2–4 (the two
integrals). That route gives the balances, the rheology and the forces without the
yield-strength envelope and the GPE algebra.

**If you already know plate tectonics descriptively:** read 01 §3 and §8 (the
dimensionless groups and the Péclet number), then 04 in full. Lesson 04 is where
the descriptive "driving forces" diagram becomes a number.

**If you are preparing a research project:** 02 §3–7 (the creep-law algebra and
what is resolvable), 03 §4–6 (the inversion and the envelope), and the ★★★
exercises. The complete route from flow law to $T_e$ is the one you will reuse.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-momentum-mass-energy.md`](01-momentum-mass-energy.md) | Lesson 01 |
| [`02-rheology-of-earth.md`](02-rheology-of-earth.md) | Lesson 02 |
| [`03-lithospheric-strength.md`](03-lithospheric-strength.md) | Lesson 03 |
| [`04-forces-and-stresses.md`](04-forces-and-stresses.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and SymPy:

```bash
cd 13-geodynamics-tectonics/01-geodynamic-principles/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python momentum_mass_energy_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rheology_of_earth_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python lithospheric_strength_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python forces_and_stresses_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), produces no figures, needs no network access,
and exits 0. All four run in under two seconds each.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC plate has $E = 70$ GPa, $\nu = 0.25$, $\Delta\rho = 2300\
> \mathrm{kg\,m^{-3}}$ and carries a 2 km high, 100 km wide load of density
> $2800\ \mathrm{kg\,m^{-3}}$. A deflection profile gives a central amplitude of
> 2200 m; a strength envelope built from a 20 K/km geotherm and a synthetic
> power-law creep law gives $T_e = 50$ km.
> **(a)** Invert the deflection for $T_e$ and state the admitted range you would
> report. **(b)** Compute the ratio of your amplitude to the Airy prediction and
> say whether the load is narrow or wide. **(c)** Give two reasons why the
> envelope estimate could exceed the flexure estimate, and one measurement that
> would discriminate. **(d)** If the load density were 5% larger than assumed,
> in which direction and by roughly how much would your $T_e$ from (a) move?

Worked versions of the individual steps appear in the
[solutions](exercises/03-lithospheric-strength-solutions.md).

## Common pitfalls across this module

1. **Quoting a viscosity, a $T_e$ or a driving force without its regime.** Each is
   conditional on a stress, a curvature or a thermal model.
2. **Believing the compensation depth matters.** Proving it does not is the
   standard numerical check on GPE integrals.
3. **Reading the Stokes approximation as a convenience.** It is a quantitative
   consequence of $Re\ll1$ and it makes the momentum equation linear.
4. **Treating a scaling coefficient as derivable.** Boundary-layer and
   plume scalings give exponents, not prefactors.
5. **Using an $O(\Delta t)$ measurement without its $\Delta t$.** Explicit
   advection contaminates growth rates and fluxes.
6. **Reporting a bound as a measurement.** $\Delta\mathrm{GPE}/h$ is an upper
   bound on a mean deviatoric stress, not a stress.
7. **Forgetting that two forces in the same direction add.** Ridge push and slab
   pull both drive a plate away from its ridge.

## Related modules

- [13-02-01 Rayleigh-Benard Convection Applied to the Mantle](../02-mantle-convection/01-rayleigh-benard-mantle.md) —
  the dimensionless group that decides whether the mantle convects at all.
- [13-03-01 Plate Kinematic Models and Euler Pole Inversion](../03-plate-tectonics-quantitative/01-plate-kinematics-models.md) —
  what the plates actually do with these forces.
- [13-04-01 Crustal Deformation from GNSS and Strain Rates](../04-tectonophysics-deformation/01-crustal-deformation-gps.md) —
  the modern measurement of the stresses estimated here.
- [02-04-03 Constitutive Laws and Generalised Hooke's Law](../../02-physics/04-elasticity-and-continuum-mechanics/03-constitutive-laws.md) —
  the elastic relations behind the flexure equation.
- [04-04-01 Stress, Strain and the Rock Constitutive Law](../../04-earth-science-geology/04-structural-geology/01-stress-strain-rocks.md) —
  the geological statement of rock strength.
