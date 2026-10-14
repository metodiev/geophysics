# Module 02-06 — Fluid Mechanics

**Stages:** intermediate → doctoral · **Prerequisites:**
[02-01 Measurement, Units and Physical Reasoning](../01-measurement-and-physical-reasoning/README.md)
(units, dimensional analysis and scaling), [02-02 Classical Mechanics](../02-classical-mechanics/README.md)
(Newton's laws, rotation), [02-04 Elasticity and Continuum Mechanics](../04-elasticity-and-continuum-mechanics/README.md)
(the stress tensor, the momentum balance and the creep laws that give a rock its
effective viscosity), [01-06 Multivariable and Vector Calculus](../../01-mathematics/06-multivariable-calculus/README.md)
(divergence, the divergence theorem, index notation).

This module is the **fluid half of geophysics**. The solid half — stress, strain
and the elastic moduli — is module 04; here the same conservation laws are
combined with a *rate*-based constitutive law and applied to water, air, magma
and mantle rock. Everything downstream that involves transport rather than
elastic wave propagation rests on this module: groundwater, ocean and atmosphere,
mantle convection, and the pore-pressure coupling that triggers earthquakes.

Two features distinguish it from a standard fluid-mechanics text:

- **Every approximation carries its regime, and its cost.** The module is
  organised around one table (lesson 02, §4) that records, for each geophysical
  regime, exactly which terms of the Navier–Stokes equation are dropped, what the
  error is, and under what condition the approximation fails. Reading a paper and
  identifying which row of that table is in force is the transferable skill.
- **The numbers are computed, and their uncertainty is stated.** Every Rayleigh
  number, Reynolds number, permeability and Rossby number in this module is
  produced by a runnable script from inputs that are labelled nominal or
  measured. Where an input is uncertain by orders of magnitude — and the mantle
  viscosity is — the module says so and reports a range rather than a value.

## Learning objectives

By the end of this module you will be able to:

1. Compute hydrostatic pressure in a layered crust and ocean, derive Archimedes'
   principle from the pressure field, and solve isostasy as a buoyancy balance,
   stating when compensation is a good model.
2. Derive the continuity and momentum equations and obtain the Navier–Stokes
   equation from a Newtonian constitutive law; nondimensionalise it and use the
   Reynolds number to decide which terms survive in a given geophysical flow.
3. Solve the canonical viscous flows, compute Reynolds numbers for a fracture and
   a borehole, decide whether Darcy's law can possibly apply, and compute
   boundary-layer scales — including checking whether the laminar formula is
   even in its regime.
4. Perform Reynolds averaging, state the closure problem precisely, verify the
   $-5/3$ spectral slope, and demonstrate that an eddy diffusivity is a
   modelling assumption rather than a property of the fluid.
5. Derive Darcy's law from the Stokes limit, define permeability and hydraulic
   conductivity without ambiguity, state its range of validity in terms of a
   pore-scale Reynolds number, and derive the pore-pressure diffusion equation
   that connects hydrogeology to induced seismicity.
6. Derive the Rayleigh–Bénard marginal-stability condition for stress-free
   boundaries, compute the critical value $27\pi^4/4$, compute the mantle's
   Rayleigh number from stated inputs, and identify the viscosity as the
   quantity that dominates the uncertainty.
7. Derive the rotating-frame momentum equation, compute the Coriolis parameter
   and the Rossby number, use geostrophic balance and thermal wind, derive Ekman
   transport, and state why the ocean and atmosphere are rotation-dominated while
   a bathtub is not.
8. Explain, for any flow in this module, which dimensionless group governs it,
   what the competing terms are, and what observation would falsify the model.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Fluid Statics, Pressure and Buoyancy](./01-fluid-statics.md) | intermediate | Pressure depends on depth, not shape; buoyancy is a density contrast |
| 02 | [Continuity and Momentum Equations; Navier–Stokes](./02-conservation-fluid.md) | advanced | Four terms, one nonlinearity, and a table of what to drop where |
| 03 | [Viscous Flow, Reynolds Number and Boundary Layers](./03-viscous-flow.md) | advanced | Viscosity sets the profile; the boundary layer sets the drag |
| 04 | [Turbulence, Mixing and Eddy Diffusivity](./04-turbulence.md) | graduate | The closure problem, and the honesty it demands |
| 05 | [Flow in Porous Media: Darcy's Law and Permeability](./05-porous-media-flow.md) | advanced | The Stokes limit, volume-averaged, and the diffusion that triggers earthquakes |
| 06 | [Mantle Convection and Rayleigh–Bénard Instability](./06-mantle-convection.md) | doctoral | A $10^{7}$ Rayleigh number and a threshold at 657.5 |
| 07 | [Rotating Fluids, Coriolis Effect and Geostrophic Balance](./07-geophysical-fluids.md) | doctoral | Why the ocean is not a bathtub: the Rossby number |

## Suggested path

**If you are working through the physics folder in order:** all seven lessons in
numeric order. Lessons 01–03 are the required spine; 04–07 each extend it into a
distinct regime.

**If you work in hydrogeology or environmental geophysics:** [01](./01-fluid-statics.md)
(head and hydrostatic pressure), [02](./02-conservation-fluid.md) §4 (the
approximation table), [03](./03-viscous-flow.md) (the cubic law and the
hydraulic aperture), [04](./04-turbulence.md) §3.5 (dispersion in porous media
is advective and diffusive), and [05](./05-porous-media-flow.md) in full — the
last is the core.

**If you work in geodynamics:** [03](./03-viscous-flow.md) (Stokes flow),
[02](./02-conservation-fluid.md) §3.5 and §6 (the Prandtl number), and
[06](./06-mantle-convection.md) in full, followed by lesson 07 §3.7 for the
rotating-convection contrast with the outer core.

**If you work in oceanography or the atmosphere:** [02](./02-conservation-fluid.md)
(Boussinesq), [04](./04-turbulence.md) (boundary-layer and mixing
parameterisations), and [07](./07-geophysical-fluids.md) in full.

**If you already have a fluid-mechanics background:** attempt ★★★9–10 of
lessons [05](./05-porous-media-flow.md), [06](./06-mantle-convection.md) and
[07](./07-geophysical-fluids.md) first. If those come out cleanly, use the rest
as reference.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-fluid-statics.md`](./01-fluid-statics.md) … [`07-geophysical-fluids.md`](./07-geophysical-fluids.md) | The seven lessons |
| [`exercises/01-fluid-statics-exercises.md`](./exercises/01-fluid-statics-exercises.md) | Hydrostatic pressure, buoyancy, isostasy |
| [`exercises/02-conservation-fluid-exercises.md`](./exercises/02-conservation-fluid-exercises.md) | Continuity, the material derivative, the term-balance table, hydrostatic validity |
| [`exercises/03-viscous-flow-exercises.md`](./exercises/03-viscous-flow-exercises.md) | Poiseuille flow, the cubic law, boundary layers, Stokes settling |
| [`exercises/04-turbulence-exercises.md`](./exercises/04-turbulence-exercises.md) | Kolmogorov scales, the log law, Richardson number, gradient-diffusion failure |
| [`exercises/05-porous-media-flow-exercises.md`](./exercises/05-porous-media-flow-exercises.md) | Darcy's law, permeability conversion, Thiem, pressure diffusion, triggering |
| [`exercises/06-mantle-convection-exercises.md`](./exercises/06-mantle-convection-exercises.md) | Rayleigh numbers and critical values, boundary layers, viscosity sensitivity |
| [`exercises/07-geophysical-fluids-exercises.md`](./exercises/07-geophysical-fluids-exercises.md) | Coriolis, Rossby number, geostrophy, Ekman, potential vorticity |
| [`code/fluid_statics_demo.py`](./code/fluid_statics_demo.py) | Layered hydrostatic profiles, gradient check, buoyancy, Airy and Pratt isostasy, ocean pressure |
| [`code/navier_stokes_demo.py`](./code/navier_stokes_demo.py) | Exact Poiseuille solution and its residual, nondimensionalisation, term-magnitude table, limiting balances |
| [`code/viscous_flow_demo.py`](./code/viscous_flow_demo.py) | Reynolds numbers for a fracture and a borehole, cubic law, boundary-layer regimes, diffusion times |
| [`code/turbulence_demo.py`](./code/turbulence_demo.py) | Kolmogorov microscales, log-law closure, closure non-uniqueness, $-5/3$ spectrum regression, mixing times |
| [`code/darcy_flow_demo.py`](./code/darcy_flow_demo.py) | Bundle-of-tubes permeability, $k \to K$ conversions, Thiem solution, Darcy validity, pressure diffusion vs erfc |
| [`code/mantle_convection_demo.py`](./code/mantle_convection_demo.py) | Mantle Rayleigh number, free-slip and rigid critical values by finite-difference eigen-solution, boundary layers, $Nu$ |
| [`code/rotating_fluids_demo.py`](./code/rotating_fluids_demo.py) | Coriolis parameter, Rossby numbers, geostrophic conversions, Ekman and Rossby radii, thermal wind, the bathtub test |

Every script requires only the Python standard library and prints its own
verification residuals. Run them; do not read them. Every value quoted as a
demo output in the lessons is the actual output of these scripts.

## The approximation table, as a reference

This is the module's organising idea. Each row is a balance that a geophysical
flow obeys, the terms of the Navier–Stokes equation that are dropped to obtain
it, and the condition under which it holds. Lesson [02](./02-conservation-fluid.md) §4
develops it; every later lesson applies one row.

| Regime | Balance | Dropped | Valid when | This module |
|---|---|---|---|---|
| Hydrostatic | $-\nabla p + \rho\mathbf{g} = 0$ | inertia, viscosity | vertical accelerations $\ll g$ | 01, 07 |
| Stokes | $-\nabla p + \eta\nabla^2\mathbf{u} + \rho\mathbf{g} = 0$ | inertia | $Re \lesssim 0.1$ | 03, 05, 06 |
| Euler | $\rho\,\mathrm{D}\mathbf{u}/\mathrm{D}t = -\nabla p + \rho\mathbf{g}$ | viscosity | $Re \gg 1$, away from walls | 04, 07 |
| Boundary layer | full, anisotropic scaling | streamwise diffusion | $\delta/L \ll 1$ | 03, 04, 07 |
| Boussinesq | full, with buoyancy from $T'$ | density variation elsewhere | $\alpha\Delta T \ll 1$ | 06, 07 |
| Geostrophic | $f\hat{z}\times\mathbf{u} = -\nabla p/\rho$ | inertia, friction | $Ro \ll 1$ | 07 |
| Darcy | $\mathbf{q} = -(k/\mu)(\nabla p - \rho\mathbf{g})$ | pore-scale inertia | pore-scale $Re \lesssim 1$–$10$ | 05 |

## Mastery checkpoint

Complete this without notes, with a calculator and no code. It links every
lesson in the module.

> A sedimentary basin is 4 km thick with a uniform density of
> $2500\ \mathrm{kg\,m^{-3}}$ and a hydrostatic pore-pressure gradient of
> $10\ \mathrm{kPa\,m^{-1}}$. A 2 km deep borehole of radius 0.1 m is drilled
> into it. **(a)** Compute the lithostatic and the pore pressure at 2 km.
> **(b)** A sandstone layer at 2 km has permeability $10^{-13}$ m². Compute the
> hydraulic conductivity for water, the specific discharge at a hydraulic
> gradient of 0.01, and the pore-scale Reynolds number with a grain size of
> 0.2 mm. Is Darcy's law valid? **(c)** Compute the Reynolds number for flow in
> the borehole at a mean velocity of $1\ \mathrm{m\,s^{-1}}$, state whether the
> Poiseuille solution applies, and say what you would use instead. **(d)** A
> fracture of aperture 0.5 mm intersects the well. Compute its permeability and
> compare it with the sandstone's. Which controls the flow? **(e)** Using
> $S_s = 10^{-5}\ \mathrm{m^{-1}}$, compute the pore-pressure diffusion length in
> one year for the sandstone, and state how far an injection-induced pressure
> change could reach in a decade. **(f)** State, in one sentence each, which
> approximation from the table above you used in each part and what would falsify
> it.

**Worked answer for parts (a)–(b) as a check:**

Lithostatic at 2 km: $2500\times9.81\times2000 = 4.91\times10^7$ Pa
$= 49.1$ MPa. Pore pressure: $10^4\times2000 = 2.0\times10^7$ Pa $= 20.0$ MPa
(so the effective vertical stress is 29.1 MPa).
$K = k\rho g/\mu = 10^{-13}\times1000\times9.81/10^{-3} = 9.81\times10^{-7}$
m s⁻¹; $q = Ki = 9.81\times10^{-9}$ m s⁻¹; with $d = 2\times10^{-4}$ m,
$Re_p = \rho qd/\mu = 1000\times9.81\times10^{-9}\times2\times10^{-4}/10^{-3}
= 1.96\times10^{-6}$ — six orders inside the Darcy range, so Darcy's law is
valid by a wide margin (the demo of lesson 05 prints the same threshold,
$q^\ast = 5\times10^{-3}$ m s⁻¹ for this grain size).

## Common pitfalls across this module

1. **Quoting a dimensionless number without its scales.** $Re$, $Ro$ and $Ra$ are
   all meaningless without the length, velocity and property values that formed
   them. Every table in this module prints them.
2. **Confusing permeability with hydraulic conductivity.** $k$ (m²) is the
   medium; $K$ (m s⁻¹) includes the fluid. They differ by about $10^{7}$ for water
   in SI units.
3. **Applying an approximation outside its regime.** The Stokes solution at
   $Re = 100$, the laminar boundary layer at $Re_x = 10^{10}$, Darcy's law in a
   karst conduit, geostrophy at the equator: each is an error of *regime*, not of
   arithmetic, and each produces plausible-looking numbers.
4. **Treating a parameterisation as a result.** An eddy diffusivity, a Manning
   coefficient, a Kozeny–Carman constant and a Nusselt coefficient are all
   calibrated, not derived. Say so.
5. **Quoting a nominal value to several figures.** Mantle viscosity, magma
   density and typical permeability are ranges. The relevant Rayleigh number is
   $10^{7}$–$10^{9}$, not 5.867 × 10⁷.
6. **Forgetting the sign convention or the hemisphere.** Compression-positive
   stress, the direction of Coriolis deflection and the sign of a geostrophic
   current all flip with convention, and a single sign error changes a
   conclusion.
7. **Confusing a threshold with a description.** $Ra_c = 657.5$ says whether
   convection starts, not what it looks like. The same caution applies to every
   critical value in the module.
8. **Assuming the mantle is turbulent because it is chaotic.** At
   $Re \sim 10^{-20}$ there is no cascade; chaotic advection by a laminar flow is
   a different mechanism with different mixing laws.
9. **Assuming isostasy or hydrostatic pore pressure without checking.** Both are
   models with regimes; both fail where they are most interesting.

## Related modules

- [02-04 Elasticity and Continuum Mechanics](../04-elasticity-and-continuum-mechanics/README.md)
  — the same conservation laws with a strain-based constitutive law; the source
  of the creep viscosity used in lesson 06.
- [02-05 Thermodynamics and Heat Transfer](../05-thermodynamics/README.md) — heat
  conduction, the thermal diffusivity and the geotherm that convection perturbs.
- [02-07 Electromagnetism and Electromagnetic Induction](../07-electromagnetism/README.md)
  — magnetohydrodynamics, where the Lorentz force joins the momentum balance.
- [01-06 Multivariable and Vector Calculus](../../01-mathematics/06-multivariable-calculus/README.md)
  — the divergence theorem behind every derivation here.
- [05-core-geophysics](../../05-core-geophysics/README.md) — where these laws
  become measurement methods.
- [06-seismology](../../06-seismology/README.md) — including
  [induced and triggered seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md),
  where pore-pressure diffusion meets fault mechanics.
- [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) — mantle
  convection and its tectonic expression.
- [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) —
  the discipline built on Darcy's law.
- [15-oceanography-marine](../../15-oceanography-marine/README.md) and
  [16-atmosphere-climate](../../16-atmosphere-climate/README.md) — the rotating
  fluids of lesson 07.
- [26-reference-library](../../26-reference-library/README.md) — the constants
  handbook, whose exact / measured / nominal classification is respected
  throughout this module.
