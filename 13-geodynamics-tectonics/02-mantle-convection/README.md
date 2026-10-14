# Module 13-02 — Mantle Convection

**Stages:** doctoral → research · **Prerequisites:** module 13-01; the
heat equation; numerical solution of PDEs.

This module takes the balances and the rheology of module 13-01 and asks the
question they were assembled for: how does a mantle convect, and how would you
know? It is organised as a sequence of *derivations you can check*. The
Rayleigh–Bénard lesson derives the critical Rayleigh number $27\pi^{4}/4$ and then
verifies it by solving the linear stability problem numerically rather than
trusting the algebra. The next lesson is a convection solver that reproduces the
same onset to half a per cent, measures the Nusselt number, and reports its own
grid and time-step errors. The two applied lessons then follow the cold and hot
ends of the circulation — slabs and plumes — where the same buoyancy integrals
produce the forces that move plates.

The intellectual centre of the module is the relationship between exponents and
coefficients. Scaling theory gives $Nu\sim Ra^{1/3}$ and $\delta\sim Ra^{-1/3}$;
it does not give the prefactor, and the measured prefactor here is 1.9, not 1. A
module that reported only the exponent would be teaching a slogan. Every lesson
therefore states which part of its result is derived, which part is measured, and
which part is chosen — and the verification sections exist to make that separation
unambiguous.

The second recurring theme is resolution and convergence. A numerical solution is
an approximation with a measurable error, and reporting $Nu$ without its grid
study, its time-step extrapolation and its energy-balance residual is reporting a
number without its uncertainty. The exercises in this module are written so that a
student must produce those diagnostics, not merely the flux.

All models and data in this module are **SYNTHETIC**. No planetary dataset,
tomographic model, hotspot catalogue or published benchmark value is used; the
parameters are chosen teaching values, and every number in the lessons is printed
by the demonstration that accompanies it.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the Rayleigh number by nondimensionalising the Boussinesq equations
   and compute it for several planetary parameter sets.
2. **Derive** and **verify** $Ra_c = 27\pi^{4}/4$ for free-slip boundaries, and
   show how no-slip boundaries change $Ra_c$ and the planform.
3. **Implement** a streamfunction–vorticity convection solver and verify its
   Poisson solve against an analytic field.
4. **Measure** the onset of convection and compare it with linear theory, stating
   the discretisation error.
5. **Quantify** the time-step error of an explicit-advection scheme by
   extrapolation to $\Delta t\to0$.
6. **Measure** $Nu(Ra)$ with local logarithmic slopes and explain why a global fit
   is not the asymptotic exponent.
7. **Check** a solution's energy balance with a flux profile that must be
   independent of depth, and interpret the residual's location.
8. **Compute** plume buoyancy, conduit flux, melt column and hotspot-track
   kinematics, and state each non-uniqueness.
9. **Compute** slab pull, sinking speed, bending length and thermal equilibration
   depth, and explain why slab dip is kinematic.

## Prerequisites

- [13-01-01 Momentum, Mass and Energy Balances in the Solid Earth](../01-geodynamic-principles/01-momentum-mass-energy.md) —
  the balances and the Péclet number.
- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](../01-geodynamic-principles/02-rheology-of-earth.md) —
  the temperature-dependent viscosity that produces lids.
- [03-12-01 A 1-D Finite-Difference Solver from Scratch](../../03-scientific-computing/12-numerical-simulation-python/01-finite-difference-1d.md) —
  discretisation vocabulary.
- [03-12-02 Numerical Stability, CFL Conditions and Convergence Testing](../../03-scientific-computing/12-numerical-simulation-python/02-stability-and-cfl.md) —
  the stability constraints used for the time step.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Rayleigh-Benard Convection Applied to the Mantle](01-rayleigh-benard-mantle.md) | research | $Ra$ decides whether; boundary conditions and viscosity contrast decide how |
| 02 | [Numerical Modelling of Mantle Convection](02-convection-numerical.md) | research | A solver is only useful with its verification, convergence and error budget attached |
| 03 | [Mantle Plumes, Hotspots and Large Igneous Provinces](03-mantle-plumes.md) | doctoral | Buoyancy flux is measurable; excess temperature and volume flux are not separable from it |
| 04 | [Subduction Dynamics, Slab Geometry and Slab Pull](04-subduction-dynamics.md) | research | Slab pull is ten times ridge push; a slab's strength is a thin shell, and its dip is kinematics |

## Suggested path

**If you are new to convection:** lessons 01 and 02 in order, running both
demonstrations. Lesson 01 §3 (the derivation of $Ra_c$) and lesson 02 §3 (the
onset measurement) are the pair to study together.

**If you already know the theory:** 01 §4–5 (boundary-layer and lid scalings),
then 02 §3–6 (what a measurement can and cannot pin down), then 04.

**If you are preparing a research project:** 02 in full (verification,
convergence, energy balance), 03 §5–7 (the blob criterion, the melt column and the
track kinematics), and 04 §4–7 (bending, force balance and dip as kinematics).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-rayleigh-benard-mantle.md`](01-rayleigh-benard-mantle.md) | Lesson 01 |
| [`02-convection-numerical.md`](02-convection-numerical.md) | Lesson 02 |
| [`03-mantle-plumes.md`](03-mantle-plumes.md) | Lesson 03 |
| [`04-subduction-dynamics.md`](04-subduction-dynamics.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations, including a complete 2-D convection solver |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 13-geodynamics-tectonics/02-mantle-convection/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rayleigh_benard_mantle_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python convection_numerical_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mantle_plumes_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python subduction_dynamics_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), produces no figures, needs no network access,
and exits 0. The convection solver is the most expensive at about 15 seconds; the
other three run in under 6 seconds.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC planet has $\rho_0 = 3400\ \mathrm{kg\,m^{-3}}$,
> $\alpha = 2.5\times10^{-5}\ \mathrm{K^{-1}}$, $\kappa = 10^{-6}\
> \mathrm{m^{2}\,s^{-1}}$, $d = 2500$ km, $\Delta T = 1300$ K,
> $\eta = 3\times10^{21}\ \mathrm{Pa\,s}$, with free-slip boundaries and
> bottom heating.
> **(a)** Compute $Ra$, the supercriticality, the boundary-layer thickness and the
> predicted Nusselt number. **(b)** Explain in two sentences why the Nusselt number
> you computed must be treated as an order-of-magnitude estimate, and say how you
> would improve it. **(c)** The planet's lid is observed to be immobile and
> conductive. Give the single physical mechanism responsible and estimate the
> viscosity contrast required. **(d)** State which two of your inputs would have to
> change most to explain a factor-of-two discrepancy between the predicted and
> observed heat flux.

Worked versions of the individual steps appear in the
[solutions](exercises/01-rayleigh-benard-mantle-solutions.md).

## Common pitfalls across this module

1. **Quoting $Ra$ without the layer depth and temperature difference.** The same
   planet gives values differing by decades depending on what you call the layer.
2. **Treating $Ra_c = 657.5$ as universal.** It is the free-slip value; no-slip
   boundaries give 1707.8.
3. **Reading a scaling exponent as a law.** $Nu\propto Ra^{1/3}$ has an
   undetermined prefactor and a heating-mode dependence.
4. **Reporting a numerical flux without its errors.** Grid study, time-step
   extrapolation and energy-balance residual are all required.
5. **Fitting one exponent across a crossover.** The measured local slope falls
   from 0.57 to 0.31 over the range tested.
6. **Inverting a buoyancy flux for a temperature.** Only the product
   $\Delta\rho\,g\,Q$ is measured.
7. **Treating a slab as a thick elastic plate.** The elastic core that can bend at
   trench radii is a few kilometres thick.
8. **Reading slab dip as a force measurement.** Rollback steepens slabs with no
   change in force.

## Related modules

- [13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure](../01-geodynamic-principles/03-lithospheric-strength.md) —
  the bending stiffness used in the subduction lesson.
- [13-01-04 Driving Forces, Stress Fields and Intraplate Stress](../01-geodynamic-principles/04-forces-and-stresses.md) —
  the force inventory that slab pull and ridge push dominate.
- [13-05-03 Benchmarking Geodynamic Codes](../05-geodynamic-modelling/03-benchmarking-geodynamics.md) —
  the discipline that turns the solver here into a trustworthy tool.
- [12-03-03 Thermal Evolution of the Earth and Secular Cooling](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/03-thermal-evolution.md) —
  the global budget these scalings feed into.
- [06-06-01 Seismic Tomography: Principles](../../06-seismology/06-seismic-tomography/01-tomography-principle.md) —
  how the cold slabs computed here are imaged.
