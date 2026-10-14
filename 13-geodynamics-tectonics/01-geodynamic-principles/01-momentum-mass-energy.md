---
id: 13-01-01
title: "Momentum, Mass and Energy Balances in the Solid Earth"
level: graduate
prereqs: ["02-01-04", "01-09-02", "12-03-01"]
tags: [geodynamics, tectonophysics, conservation-laws, stokes-flow, nondimensionalisation, thermal-budget]
---

# Momentum, Mass and Energy Balances in the Solid Earth

> All models and data in this module are **SYNTHETIC**. The parameters below are
> chosen teaching values, not measurements, and every number quoted in this
> lesson is printed by `code/momentum_mass_energy_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the mass, momentum and energy balances for a deforming solid Earth
   and **identify** which terms survive at geodynamic timescales.
2. **Derive** the Reynolds, Prandtl and Péclet numbers by nondimensionalising
   the equations, and **justify** the Stokes (infinite-Prandtl) approximation
   from a measured order-of-magnitude comparison.
3. **Compute** a Stokes settling velocity and check the Reynolds number at which
   it is valid, stating the regime of validity explicitly.
4. **Verify** incompressibility numerically from a divergence-free analytic
   field and **state** the level at which mass balance holds on a grid.
5. **Estimate** viscous dissipation in a shear zone and compare it with the
   surface heat flux.
6. **Solve** the one-dimensional steady heat equation with radiogenic heating and
   **interpret** the two heat fluxes and the radiogenic share.
7. **Assemble** a global thermal budget and **quantify** the Urey ratio and the
   cooling time implied by it, with uncertainty stated.

## Prerequisites

- [02-01-04 Conservation Laws as the Engine of Physical Modelling](../../02-physics/01-measurement-and-physical-reasoning/04-conservation-laws.md) —
  how a balance law becomes an equation.
- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md) —
  the parabolic equation and its $\sqrt{t}$ scalings.
- [12-03-01 Radiogenic Heat Production and Mantle Geotherms](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md) —
  where the heat sources and the geotherm come from.
- [04-01-02 Lithosphere, Asthenosphere and the Rheological Definition](../../04-earth-science-geology/01-earth-structure/02-lithosphere-asthenosphere.md) —
  the geological vocabulary this lesson quantifies.

## 1. Intuition: a planet that flows, slowly

Geodynamics is the branch of geophysics that treats the solid Earth as a fluid
— not because rock is soft, but because the timescale is long. Hold a piece of
mantle rock for a second and it is an elastic solid; hold it for ten million
years and it is a fluid with a viscosity of $\sim 10^{21}\ \mathrm{Pa\,s}$,
about $10^{24}$ times that of water. Everything in this module follows from
taking that statement seriously and asking what the numbers imply.

Three balances do almost all the work:

- **Mass**: material is neither created nor destroyed, so the velocity field of
  an incompressible flow is divergence-free.
- **Momentum**: at mantle viscosities the inertia of the flow is so small that
  the momentum balance reduces to a *force balance* between pressure, viscous
  stress and buoyancy. The flow adjusts instantaneously to whatever buoyancy is
  available.
- **Energy**: heat is transported by conduction *and* by the flow; which of the
  two dominates is decided by one dimensionless number, the Péclet number, and
  it changes with the length scale you look at.

The instructive surprise of this lesson is in that last clause. At 100 km, the
mantle is on the advective side of the Péclet number; at a global scale it is
overwhelmingly advective. Heat is not "conducted up" through the mantle by a
steady geotherm; it is *carried* by the flow, and the conductive boundary layers
at the top and bottom are thin interfaces where the two mechanisms hand over.
Recognising which balance controls which scale is the core skill of
geodynamics, and it is a skill in nondimensionalisation, not in algebra.

## 2. The three balances, precisely

### 2.1 Mass

For a material of density $\rho$ and velocity $\mathbf{u}$, conservation of mass
is

$$\frac{\partial \rho}{\partial t} + \nabla\cdot(\rho \mathbf{u}) = 0 .$$

Mantle flow is extremely close to incompressible: the density varies by a few
per cent over the whole mantle while velocities are $10^{-9}\ \mathrm{m\,s^{-1}}$,
so the advective term $\mathbf{u}\cdot\nabla\rho$ is negligible compared with
$\partial_t\rho$ over the relevant times. The balance therefore reduces to the
**incompressibility condition**

$$\nabla\cdot\mathbf{u} = 0 .$$

This is an exact statement in the Boussinesq approximation used below: density
variations are carried *only* in the buoyancy term of the momentum equation,
and nowhere else.

### 2.2 Momentum

The momentum balance for a compressible Newtonian fluid is the Navier–Stokes
equation. For a mantle with constant dynamic viscosity $\eta$, negligible
inertia and density variations retained only in buoyancy,

$$\underbrace{\rho_0\frac{D\mathbf{u}}{Dt}}_{\text{inertia}}
= \underbrace{-\nabla p}_{\text{pressure}}
+ \underbrace{\eta\nabla^{2}\mathbf{u}}_{\text{viscous}}
+ \underbrace{\rho_0 g\alpha\,\theta\,\hat{\mathbf{z}}}_{\text{buoyancy}} ,$$

where $\theta = T - T_{\text{ref}}$ is the temperature anomaly, $\alpha$ the
thermal expansivity and $g$ gravity. The mass, momentum and energy equations are
coupled through $\theta$ alone: temperature differences create buoyancy, buoyancy
drives flow, flow transports heat.

### 2.3 Energy

For the same material, with thermal conductivity $k$, specific heat $c_p$ and a
volumetric heat production rate $H$,

$$\rho_0 c_p\left(\frac{\partial T}{\partial t} + \mathbf{u}\cdot\nabla T\right)
= k\nabla^{2}T + H + \underbrace{\Phi}_{\text{viscous dissipation}} .$$

The left-hand side is the material derivative of the heat content; the first
right-hand term is conduction, the second radiogenic (or other) production, and
the third the mechanical work converted to heat by viscosity — the term this
lesson quantifies in §4.

## 3. Nondimensionalisation: the three numbers that decide everything

Take characteristic length $L$, velocity $U$, time $L/U$, temperature difference
$\Delta T$ and pressure scale $\eta U/L$. Substituting into the momentum balance
divides it by the viscous term and produces two groups:

$$Re \equiv \frac{\rho_0 U L}{\eta}, \qquad
Pr \equiv \frac{\eta}{\rho_0 \kappa}, \qquad \kappa \equiv \frac{k}{\rho_0 c_p},$$

the **Reynolds** number (inertia over viscosity) and the **Prandtl** number
(viscous over thermal diffusion). The product is the Péclet number of momentum,
and the energy balance produces

$$Pe \equiv \frac{UL}{\kappa} = Re\,Pr .$$

Two structural consequences follow:

1. If $Re\ll 1$, dropping the inertia term is not an approximation of
   convenience but an enormous simplification: the momentum equation becomes
   *linear in the velocity*. There is no equation of motion, only an
   instantaneous force balance. That is why mantle convection is solved as a
   Stokes problem (see [13-02-02](../02-mantle-convection/02-convection-numerical.md)).
2. If $Pe\ll 1$, conduction wins; if $Pe\gg 1$, advection wins. Because
   $Pe = UL/\kappa$ carries $L$ explicitly, the same fluid can be diffusive at
   one scale and advective at another.

The demonstration measures each of these. With a 100 km buoyant blob of density
contrast $50\ \mathrm{kg\,m^{-3}}$ in a $10^{21}\ \mathrm{Pa\,s}$ mantle, the
Stokes settling speed is

$$u = \frac{2\,\Delta\rho\,g\,a^{2}}{9\eta} = 1.0900\times10^{-9}\ \mathrm{m\,s^{-1}}
= 34.40\ \mathrm{mm\,yr^{-1}},$$

and then

$$Re = \frac{\rho_0 u a}{\eta} = 3.597\times10^{-22},$$

a number so small that it is best read as "inertia is $10^{22}$ times smaller
than viscosity". A 1000 km blob is ten times faster per unit size (the speed
scales as $a^2$: $1.090\times10^{-7}\ \mathrm{m\,s^{-1}} = 3439.7\ \mathrm{mm\,yr^{-1}}$)
yet still has $Re = 3.597\times10^{-19}$.

The term-by-term comparison at $L = 100$ km makes the balance explicit:

| term | magnitude | units |
|---|---|---|
| inertia $\rho_0 u^{2}/L$ | $3.92\times10^{-20}$ | Pa m$^{-1}$ |
| viscous $\eta u/L^{2}$ | $1.09\times10^{2}$ | Pa m$^{-1}$ |
| buoyancy drive $\rho_0 g\,\Delta\rho/\rho_0$ | $1.62\times10^{6}$ | Pa m$^{-1}$ |
| inertia / viscous | $3.597\times10^{-22}$ | — |
| viscous / buoyancy | $6.734\times10^{-5}$ | — |

The pressure gradient required to balance buoyancy is far larger than the
viscous term, which is exactly why the Stokes approximation is so accurate: the
velocity adjusts until viscous stresses *almost* cancel the pressure gradient,
leaving a tiny residual to drive the flow. In a real numerical model that
residual is what you solve for, and it is why Stokes solvers are delicate.

## 4. Worked example: Stokes settling and its regime of validity

**Problem.** A spherical blob of density contrast $50\ \mathrm{kg\,m^{-3}}$ and
radius $100\ \mathrm{km}$ is embedded in a fluid of density
$3300\ \mathrm{kg\,m^{-3}}$ and viscosity $10^{21}\ \mathrm{Pa\,s}$. How fast
does it rise, and is the Stokes result valid?

**Buoyancy force.** With $\Delta\rho$ the density difference,

$$F_b = \frac{4}{3}\pi a^{3}\Delta\rho\,g .$$

**Drag.** For a rigid sphere at $Re\ll1$, Stokes' law gives
$F_d = 6\pi\eta a u$.

**Balance.** Setting $F_b = F_d$:

$$\frac{4}{3}\pi a^{3}\Delta\rho g = 6\pi\eta a u
\;\;\Longrightarrow\;\;
\boxed{\,u = \frac{2\Delta\rho\,g\,a^{2}}{9\eta}\,}.$$

**Numbers.**

$$u = \frac{2(50)(9.81)(10^{5})^{2}}{9(10^{21})}
= \frac{9.81\times10^{12}}{9\times10^{21}}
= 1.090\times10^{-9}\ \mathrm{m\,s^{-1}} .$$

Converting with $1\ \mathrm{yr} = 3.1557\times10^{7}\ \mathrm{s}$:
$u = 34.40\ \mathrm{mm\,yr^{-1}}$.

**Validity.** $Re = \rho_0 u a/\eta = 3.597\times10^{-22}\ll1$, so Stokes' law
is valid with an enormous margin: any inertial correction is of order $Re$, i.e.
beyond double precision. The real caveats are physical, not numerical:

- the blob must not deform or change size while it rises;
- the viscosity must be uniform (with temperature-dependent viscosity the blob
  develops an internal circulation and the coefficient changes);
- the blob must be far from boundaries compared with $a$.

That last point is the interesting one. A 100 km blob takes
$2.9\ \mathrm{Gyr}/34.4\ \mathrm{mm\,yr^{-1}}$… which is easier to read as
"$2900\ \mathrm{km}/34.4\ \mathrm{mm\,yr^{-1}} = 84\ \mathrm{Myr}$" — long
enough that the blob's own thermal anomaly would have conducted away. The
demonstration's §7 shows why: the diffusive time at 100 km is 317 Myr. Buoyancy
anomalies of that size do not survive; the ones that do are either much larger
or continuously replenished. This interplay — buoyancy versus diffusion — is the
subject of [13-02-01](../02-mantle-convection/01-rayleigh-benard-mantle.md).

## 5. Mass balance in practice: how exactly is $\nabla\cdot\mathbf{u} = 0$?

Incompressibility is a constraint, not an equation to be solved: any velocity
field you use must satisfy it. A convenient way to guarantee that is a
**streamfunction**. In two dimensions, define $\mathbf{u} = (\psi_z, -\psi_x)$;
then

$$\nabla\cdot\mathbf{u} = \frac{\partial^{2}\psi}{\partial z\,\partial x}
- \frac{\partial^{2}\psi}{\partial x\,\partial z} = 0$$

identically. The demonstration takes the analytic field
$\psi = \sin(kx)\sin(mz)$ and measures the divergence of its analytical
derivatives with central differences on a $129^{2}$ grid:

$$\max|\nabla\cdot\mathbf{u}|\big/\big(\max|\mathbf{u}|/L\big) = 5.77\times10^{-14}.$$

That residual is truncation error of the difference operator and round-off, not
physics. It matters because a solver that does *not* use a streamfunction or a
projection step will slowly accumulate a divergent component, and a divergent
velocity field spurious-heats or cools the domain. The example solver in
[13-02-02](../02-mantle-convection/02-convection-numerical.md) is built on a
streamfunction for exactly this reason.

## 6. Energy balance I: viscous dissipation

Mechanical work done against viscosity is not lost; it becomes heat at the rate
$\Phi = \eta(\partial u_i/\partial x_j + \partial u_j/\partial x_i)^{2}/2$ per
unit volume ($\tfrac{1}{2}$ for a symmetric strain rate). For simple shear
across a layer of thickness $d$ with velocity difference $u$,

$$\Phi = \eta\left(\frac{u}{d}\right)^{2}
\;\;\Longrightarrow\;\;
q_{\text{diss}} = \Phi d = \frac{\eta u^{2}}{d} .$$

With $u = 50\ \mathrm{mm\,yr^{-1}}$, $\eta = 10^{21}\ \mathrm{Pa\,s}$ and
$d = 100\ \mathrm{km}$:

$$q_{\text{diss}} = \frac{(10^{21})(1.584\times10^{-9})^{2}}{10^{5}}
= 2.510\times10^{-2}\ \mathrm{W\,m^{-2}} = 25.1\ \mathrm{mW\,m^{-2}} .$$

Three measured variants make the scaling clear:

| configuration | strain rate ($\mathrm{s^{-1}}$) | $\Phi$ ($\mathrm{W\,m^{-3}}$) | column total |
|---|---|---|---|
| 50 mm/yr over 100 km | $1.584\times10^{-14}$ | $2.510\times10^{-7}$ | 25.1 mW m$^{-2}$ |
| 50 mm/yr over 10 km | $1.584\times10^{-13}$ | $2.510\times10^{-5}$ | 251.0 mW m$^{-2}$ |
| 100 mm/yr over 100 km | $3.169\times10^{-14}$ | $1.004\times10^{-6}$ | 100.4 mW m$^{-2}$ |

Because $\Phi \propto 1/d$, *localising* shear raises the dissipation violently.
A 10 km shear zone dissipating 251 mW m$^{-2}$ would dominate a continental heat
flux, which is why shear heating is invoked as a candidate for localising
deformation — and why it must be carefully justified rather than assumed: it
requires that the strain localise first.

## 7. Energy balance II: the conducting crust as a boundary-value problem

Steady one-dimensional conduction with uniform radiogenic heating $H$ obeys

$$k\frac{\mathrm{d}^{2}T}{\mathrm{d}z^{2}} = -H,
\qquad T(0) = T_s,\quad T(h) = T_{\text{Moho}} .$$

Integrating twice and applying both temperatures:

$$T(z) = T_s + \left[\frac{T_{\text{Moho}} - T_s}{h}
+ \frac{Hh}{2k}\right]z - \frac{H}{2k}z^{2},$$

$$q_s = k\left[\frac{T_{\text{Moho}} - T_s}{h} + \frac{Hh}{2k}\right],
\qquad q_{\text{Moho}} = q_s - Hh .$$

With $h = 35$ km, $T_{\text{Moho}} = 600\ ^\circ\mathrm{C}$,
$k = 3.0\ \mathrm{W\,m^{-1}\,K^{-1}}$ and $H = 10^{-6}\ \mathrm{W\,m^{-3}}$
(SYNTHETIC values):

$$q_s = 0.0689\ \mathrm{W\,m^{-2}} = 68.9\ \mathrm{mW\,m^{-2}},
\qquad q_{\text{Moho}} = 33.9\ \mathrm{mW\,m^{-2}},$$

and the radiogenic share of the surface flux is $Hh/q_s = 50.8\%$. The measured
profile:

| $z$ (km) | 0 | 8.8 | 17.5 | 26.2 | 35.0 |
|---|---|---|---|---|---|
| $T$ ($^\circ$C) | 0.0 | 188.3 | 351.0 | 488.3 | 600.0 |

The profile is not linear: radiogenic heating bends it concave-down. This matters
because the *curvature* is the datum — a measured geotherm that is straight
implies $H\approx0$, while the real continental geotherm tells you how much heat
is being generated between the surface and the Moho. The half of the surface
flux that comes from crustal radiogenic heating here is a chosen number, but the
structure of the argument is general.

## 8. Energy balance III: advection versus diffusion

For a conduction-only problem the perturbation from a boundary diffuses a
distance $\sim\sqrt{\kappa t}$, so the time to diffuse over $L$ is
$t_{\text{diff}} = L^{2}/\kappa$ and the advective time is
$t_{\text{adv}} = L/u$. Their ratio is the Péclet number:

$$Pe = \frac{UL}{\kappa} = \frac{t_{\text{diff}}}{t_{\text{adv}}} .$$

Measured, with $u = 1.090\times10^{-9}\ \mathrm{m\,s^{-1}}$:

| scale $L$ | $t_{\text{diff}} = L^{2}/\kappa$ | $t_{\text{adv}} = L/u$ | $Pe$ |
|---|---|---|---|
| 100 km | 316.9 Myr | 2.907 Myr | 109.0 |
| 2900 km (whole mantle) | 266 502 Myr | 84.3 Myr | 3161 |

Two readings matter.

- At *every* mantle scale listed, advection is faster than diffusion by two to
  three orders of magnitude. The mantle is not a conducting slab; it is a
  conveyor with thin conductive skins.
- The diffusive time at the 100 km scale, 317 Myr, is comparable to the age of
  the ocean floor and to the convective overturn time. That coincidence is why
  lithospheric thickness and plate age are so tightly linked, and it is the
  quantitative content of "cooling plate" models
  ([13-01-04](04-forces-and-stresses.md)).

## 9. Energy balance IV: a global budget with an honest uncertainty

Assembling the three balances into a single budget requires only multiplications,
but the result is where the modelling assumptions show up:

| quantity | value (SYNTHETIC) |
|---|---|
| mantle volume $V$ | $9.067\times10^{20}\ \mathrm{m^{3}}$ |
| heat content above the CMB $\rho c_p V\Delta T$ | $4.862\times10^{30}\ \mathrm{J}$ |
| surface area $4\pi R^{2}$ ($R = 6371$ km) | $5.101\times10^{14}\ \mathrm{m^{2}}$ |
| heat loss at $q_{\text{avg}} = 87\ \mathrm{mW\,m^{-2}}$ | $4.438\times10^{13}\ \mathrm{W} = 44.4\ \mathrm{TW}$ |
| radiogenic production (chosen) | 20.0 TW |
| Urey ratio $=$ production/loss | 0.451 |
| heat content / net loss | $1.995\times10^{17}\ \mathrm{s} = 6.32\ \mathrm{Gyr}$ |

Three lessons, all about uncertainty rather than arithmetic:

1. The **Urey ratio** — radiogenic production divided by surface heat loss —
   decides whether the mantle is cooling now. At 0.451 it is: roughly half the
   heat leaving is being supplied, the rest is drawn from stored heat. A Urey
   ratio above 1 would mean the Earth is heating up, which is incompatible with
   its thermal evolution, so this ratio is a *consistency constraint* on
   radiogenic inventories.
2. The **cooling time** $\sim 6\ \mathrm{Gyr}$ is not a prediction of the Earth's
   lifetime: it is the statement that the present rate of loss cannot be
   sustained for much longer than the age of the Earth, so the rate must have
   declined (or the supply been larger) in the past.
3. Both conclusions rest on a single chosen average flux and a single chosen
   production rate. Reporting a Urey ratio without its uncertainty is the most
   common way to make a global budget look stronger than it is. The honest
   statement is "the ratio is of order one half, with the dominant uncertainty
   in how much of the surface flux is from the mantle at all".

## 10. Assumptions and the regime of validity

| assumption | what it means | where it fails |
|---|---|---|
| Boussinesq | density variations only in buoyancy | whole-mantle compressibility, phase transitions |
| constant viscosity | one number for $\eta$ | the real mantle spans $>10^{20}$ in $\eta$; see [13-01-02](02-rheology-of-earth.md) |
| $Re\ll1$ | no inertia | not anywhere in the mantle (measured $10^{-22}$) |
| incompressible | $\nabla\cdot\mathbf{u}=0$ | planetary-scale density stratification |
| no rotation, no magnetic field | Lorentz and Coriolis neglected | outer core; see [12-04-02](../../12-global-geophysics-interior/04-geomagnetism-and-core/02-geodynamo-numerical.md) |
| uniform $H$, $k$ | closed-form geotherm | strong crustal heat-production contrasts |
| steady conduction in the crust | $\partial_t T = 0$ | rifted, young or magmatically active crust |

The Boussinesq approximation deserves one sentence more. It replaces the full
compressible momentum balance with a constant-density one, yet keeps $\Delta\rho$
in the buoyancy term. That is legitimate only when the density variations are
small compared with the background — true in the mantle (few per cent) and not
true in an atmosphere.

## 11. Units and dimensional analysis

| quantity | symbol | SI unit | check |
|---|---|---|---|
| dynamic viscosity | $\eta$ | Pa s | stress $\times$ time |
| velocity | $u$ | m s$^{-1}$ | |
| thermal diffusivity | $\kappa$ | m$^{2}$ s$^{-1}$ | $(k)/(\rho c_p)$ |
| Rayleigh number | $Ra$ | dimensionless | $\rho g\alpha\Delta T L^{3}/(\kappa\eta)$ |
| Reynolds number | $Re$ | dimensionless | $\rho uL/\eta$ |
| Péclet number | $Pe$ | dimensionless | $uL/\kappa$ |
| dissipation per volume | $\Phi$ | W m$^{-3}$ | Pa s $\times$ s$^{-2}$ |
| heat flux | $q$ | W m$^{-2}$ | |

A quick check that catches most errors: $\eta u$ has units of
$\mathrm{Pa\,m}$, so $\eta u/L$ is a stress ($\mathrm{Pa}$) and $\eta u/L^{2}$ is
a force per unit volume ($\mathrm{Pa\,m^{-1}}$), as used in §3. If a term you
have written does not reduce to those, a length or a time has been misplaced.

## 12. The demonstration

`code/momentum_mass_energy_demo.py` performs every calculation in this lesson:

```bash
cd 13-geodynamics-tectonics/01-geodynamic-principles/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python momentum_mass_energy_demo.py
```

It prints, in order: the Stokes velocities and Reynolds numbers of §3; the
momentum-term table; the measured divergence of an analytic incompressible field;
the dissipation table of §6; the geotherm and heat fluxes of §7; the Péclet
numbers of §8; and the global budget of §9. It uses a fixed seed
(`np.random.default_rng(20261014)`), prints labelled results with units, needs no
network and no plotting, and exits 0.

Exercises and worked solutions:
[`exercises/01-momentum-mass-energy-exercises.md`](exercises/01-momentum-mass-energy-exercises.md)
and
[`exercises/01-momentum-mass-energy-solutions.md`](exercises/01-momentum-mass-energy-solutions.md).

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC model has a density contrast of $40\ \mathrm{kg\,m^{-3}}$, a body
> radius of $80\ \mathrm{km}$, $\eta = 10^{21}\ \mathrm{Pa\,s}$,
> $\rho_0 = 3300\ \mathrm{kg\,m^{-3}}$, $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$.
> **(a)** Compute the Stokes velocity and the Reynolds number, and state in one
> sentence why the Stokes result is valid. **(b)** Compute the Péclet number at
> the body scale and say whether advection or diffusion dominates. **(c)** Compute
> the diffusive time at that scale and compare it with the time the body needs to
> rise 500 km. **(d)** State two physical reasons why the actual rise speed could
> differ from (a) by a factor of 3, and one reason the error is not numerical.

A worked version appears in the
[solutions](exercises/01-momentum-mass-energy-solutions.md).

## Common pitfalls

1. **Quoting a velocity without its regime.** Every Stokes estimate must come
   with its $Re$; a formula valid at $Re\ll1$ is not a general velocity law.
2. **Using inertia "just to be safe".** Including it when $Re\sim10^{-20}$
   changes nothing numerically but hides the structure of the problem, and in a
   numerical model adds a stiff, unnecessary term.
3. **Treating the Péclet number as a property of the Earth rather than of a
   scale.** The same mantle is advective at 100 km and diffusive at 1 m.
4. **Ignoring viscous heating by assumption.** Compute it first
   ($\Phi = \eta u^{2}/d$): it is negligible at plate scale and dominant in a
   narrow shear zone, and which one you have depends on $d$.
5. **Reporting a Urey ratio without uncertainty.** The ratio's value is set by
   the poorly known partition between mantle and crustal heat production.
6. **Confusing the diffusive time with the cooling time.** $L^{2}/\kappa$ at the
   mantle scale is 267 Gyr; the mantle has not had that long, which is *why* it
   convects rather than conducting.

## Related modules

- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](02-rheology-of-earth.md) —
  where $\eta$ comes from and why a single value is a fiction.
- [13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure](03-lithospheric-strength.md) —
  the elastic limit of the same material.
- [13-01-04 Driving Forces, Stress Fields and Intraplate Stress](04-forces-and-stresses.md) —
  the buoyancy integrals that the momentum balance here makes quantitative.
- [13-02-01 Rayleigh-Benard Convection Applied to the Mantle](../02-mantle-convection/01-rayleigh-benard-mantle.md) —
  the dimensionless group that decides whether the mantle convects at all.
- [12-03-03 Thermal Evolution of the Earth and Secular Cooling](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/03-thermal-evolution.md) —
  the same budget run through geological time.
