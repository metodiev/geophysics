---
id: 02-06-02
title: "Continuity and Momentum Equations; Navier-Stokes"
level: advanced
prereqs: ["02-06-01", "02-04-01", "02-04-03", "01-06-06"]
estimated_minutes: 90
tags: [navier-stokes, continuity, momentum, dimensional-analysis]
---

# Continuity and Momentum Equations; Navier-Stokes

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the continuity equation from a balance of mass on a control
   volume and on a material parcel, and state the difference between the two
   routes.
2. **Derive** the momentum equation $\rho\,\mathrm{D}\mathbf{u}/\mathrm{D}t =
   -\nabla p + \nabla\cdot\boldsymbol{\tau} + \rho\mathbf{g}$ from Newton's
   second law applied to a fluid parcel.
3. **Obtain** the Navier–Stokes equation by specifying a Newtonian stress and
   stating the Stokes hypothesis for the bulk viscosity.
4. **Nondimensionalise** the momentum equation and identify the Reynolds number
   as the ratio of the advective-inertia term to the viscous term.
5. **State, for each geophysical regime, exactly which terms are dropped**, and
   quantify the error that dropping them incurs.
6. **Verify** an exact solution of the equation numerically, and check that
   continuity is satisfied to round-off.

## Prerequisites

- [02-06-01 Fluid Statics, Pressure and Buoyancy](./01-fluid-statics.md) — the
  pressure field and the hydrostatic balance this lesson modifies.
- [02-04-01 Stress: Traction, Cauchy Stress Tensor and Equilibrium](../04-elasticity-and-continuum-mechanics/01-stress.md)
  — the stress tensor, its symmetry and the divergence form of the momentum
  balance; a fluid is a continuum with $\sigma_{ij} = -p\delta_{ij} +
  \tau_{ij}$.
- [02-04-03 Constitutive Laws and Generalised Hooke's Law](../04-elasticity-and-continuum-mechanics/03-constitutive-laws.md)
  — what a constitutive relation is, and why it must be supplied separately from
  the conservation laws.
- [01-06-06 Gauss, Stokes and Green Theorems](../../01-mathematics/06-multivariable-calculus/06-integral-theorems.md)
  — the divergence theorem, used in every derivation here.

## 1. From statics to motion

Fluid statics balances two terms: the pressure gradient and gravity. Motion adds
two more: the rate of change of momentum, and viscous stress. The whole of fluid
mechanics is the bookkeeping of those four terms, and the whole of *geophysical*
fluid mechanics is a set of principled decisions about which of them may be
neglected in which regime.

The equations are

$$\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\mathbf{u}) = 0
\qquad\text{(continuity)}, \tag{1}$$

$$\rho\left(\frac{\partial\mathbf{u}}{\partial t} +
\mathbf{u}\cdot\nabla\mathbf{u}\right) = -\nabla p +
\nabla\cdot\boldsymbol{\tau} + \rho\mathbf{g}
\qquad\text{(momentum)}, \tag{2}$$

$$\tau_{ij} = \mu\left(\partial_i u_j + \partial_j u_i\right) +
\left(\zeta - \tfrac23\mu\right)(\nabla\cdot\mathbf{u})\,\delta_{ij}
\qquad\text{(Newtonian fluid)}. \tag{3}$$

Substituting (3) for a fluid of **constant** viscosity and **constant** density
gives the Navier–Stokes equation

$$\rho\left(\frac{\partial\mathbf{u}}{\partial t} +
\mathbf{u}\cdot\nabla\mathbf{u}\right) = -\nabla p +
\mu\nabla^2\mathbf{u} + \rho\mathbf{g}. \tag{4}$$

Four equations — (1) and the three components of (4) — for four unknowns $p$,
$u_x$, $u_y$, $u_z$, given $\rho$, $\mu$ and $\mathbf{g}$. The count is the
reason the system is closed, and the reason *compressible* and
*temperature-dependent-viscosity* flows need an equation of state and an energy
equation before they can be solved.

## 2. Precise definitions

**Material (substantive) derivative.** The rate of change seen by an observer
moving with the fluid:

$$\frac{\mathrm{D}}{\mathrm{D}t} = \frac{\partial}{\partial t} +
\mathbf{u}\cdot\nabla . \tag{5}$$

The two terms are the *local* rate of change at a fixed point and the
*advective* rate of change from being carried to a place where the field is
different. The distinction is the source of most of the difficulty in fluid
mechanics: a steady flow ($\partial/\partial t = 0$) still accelerates its
parcels.

**Incompressible.** $\nabla\cdot\mathbf{u} = 0$. This is an approximation about
the *flow*, not about the material: it is valid when the Mach number
$U/c$ is small and when density changes from other causes (temperature,
composition) are dynamically negligible. In the ocean, $\nabla\cdot\mathbf{u}=0$
is used to better than 0.1 per cent even though water is slightly compressible.

**Viscosity.** The dynamic viscosity $\mu$ (Pa s) relates shear stress to shear
rate; the kinematic viscosity $\nu = \mu/\rho$ (m² s⁻¹) is the diffusivity of
momentum. Two fluids can have the same $\nu$ and utterly different behaviour if
their densities differ.

**Bulk viscosity.** $\zeta$, the resistance to volumetric (not shear)
deformation. For monatomic gases $\zeta = 0$; for water and for most fluids
$\zeta$ is comparable to $\mu$, but because it multiplies $\nabla\cdot\mathbf{u}$
it is negligible in incompressible flows. The choice $\zeta = 0$ is the **Stokes
hypothesis**; it is an approximation, valid in those same flows, and it is
falsified by sound attenuation measurements, which is one way to measure $\zeta$.

**The stress tensor of a fluid.** In the mechanics module the stress tensor was
decomposed into hydrostatic and deviatoric parts. For a fluid at rest only the
hydrostatic part survives; for a moving Newtonian fluid the deviatoric part is
(3). Equation (3) is *the* definition of a Newtonian fluid, and it is an ideal
case: polymer solutions, suspensions, melts near the glass transition and
granular materials are not Newtonian. Magma is Newtonian only while its crystal
content is low; above roughly 30 per cent crystals it becomes a yield-stress
fluid, and the constitutive relation of (3) fails.

## 3. Derivations

### 3.1 Continuity from a control volume

Consider a fixed volume $V$ with surface $S$. The rate of change of the mass
inside is the negative of the mass flux out:

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_V \rho\,\mathrm{d}V = -\oint_S
\rho\mathbf{u}\cdot\mathbf{n}\,\mathrm{d}S. \tag{6}$$

Using the divergence theorem, and commuting the derivative through the integral
because $V$ is fixed,

$$\int_V\!\left[\frac{\partial\rho}{\partial t} +
\nabla\cdot(\rho\mathbf{u})\right]\mathrm{d}V = 0 . \tag{7}$$

Since $V$ is arbitrary, the bracket vanishes pointwise, giving equation (1).
The same equation follows from a material parcel, where the mass is constant and
the volume changes at the rate $\nabla\cdot\mathbf{u}$; the control-volume route
is used here because it makes clear that equation (1) contains no assumption
about the material — only about mass.

### 3.2 Incompressible continuity

If $\rho$ is constant following the motion, equation (1) reduces to
$\nabla\cdot\mathbf{u} = 0$, or, written in the material derivative,

$$\frac{1}{\rho}\frac{\mathrm{D}\rho}{\mathrm{D}t} = -\nabla\cdot\mathbf{u}.
\tag{8}$$

The right-hand side is the fractional rate of change of a parcel's volume. The
incompressible approximation therefore says: *parcels do not change volume*.
This is a statement about the flow, and it holds even for a compressible fluid
when the pressure changes are small compared with the bulk modulus. For water,
$K \approx 2.2$ GPa, so a pressure change of 1 MPa changes the density by about
0.05 per cent — negligible for almost every purpose. For a gas, the relevant
comparison is the Mach number, and the approximation fails above about
$M \sim 0.3$ if sound transmission matters.

### 3.3 Momentum for a fluid parcel

Newton's second law for a parcel of volume $V$:

$$\int_V \rho\frac{\mathrm{D}\mathbf{u}}{\mathrm{D}t}\,\mathrm{d}V =
\oint_S \boldsymbol{\sigma}\mathbf{n}\,\mathrm{d}S +
\int_V \rho\mathbf{g}\,\mathrm{d}V . \tag{9}$$

Applying the divergence theorem to the surface term and shrinking the volume
gives

$$\rho\frac{\mathrm{D}\mathbf{u}}{\mathrm{D}t} =
\nabla\cdot\boldsymbol{\sigma} + \rho\mathbf{g}. \tag{10}$$

Writing $\boldsymbol{\sigma} = -p\mathbf{I} + \boldsymbol{\tau}$ with
$\boldsymbol{\tau}$ the deviatoric (viscous) stress gives equation (2). This is
the same derivation as
[02-04-05](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md), with
one change: for a solid the constitutive relation relates stress to *strain*,
for a fluid to *strain rate*. That single substitution turns the elastodynamic
equation into Navier–Stokes and explains why seismic waves and mantle flow are
described by the same momentum balance.

### 3.4 Newtonian stress and the Navier–Stokes equation

Inserting (3) into (2), with $\mu$ constant and the Stokes hypothesis:

$$\rho\frac{\mathrm{D}\mathbf{u}}{\mathrm{D}t} = -\nabla p +
\mu\nabla^2\mathbf{u} + \mu\nabla(\nabla\cdot\mathbf{u}) +
\rho\mathbf{g}, \tag{11}$$

and for an incompressible flow the third term vanishes, leaving (4). Two
features of (4) are worth naming:

- **It is nonlinear**, through $\mathbf{u}\cdot\nabla\mathbf{u}$. That
  nonlinearity is the entire content of turbulence (lesson 04).
- **It is second order in space and first order in time**, so it needs one
  initial condition and either two velocity conditions (or one velocity and one
  stress condition) per boundary.

### 3.5 Nondimensionalisation

Choose a length $L$, a velocity $U$, a pressure scale $\rho U^2$ and a time
scale $L/U$, and write $\mathbf{u} = U\mathbf{u}^*$, $\nabla = \nabla^*/L$, etc.
The steady incompressible momentum equation becomes

$$\mathbf{u}^*\cdot\nabla^*\mathbf{u}^* = -\nabla^*p^* +
\frac{1}{Re}\nabla^{*2}\mathbf{u}^* + \frac{1}{Fr^2}\,\hat{g}, \qquad
Re = \frac{\rho UL}{\mu} = \frac{UL}{\nu}. \tag{12}$$

Three consequences follow, and they structure the rest of the module:

- **$Re$ multiplies the viscous term.** When $Re \ll 1$ the viscous term
  dominates and the equation is linear (Stokes flow). When $Re \gg 1$ it is
  negligible except in thin boundary layers (lesson 03) and turbulence
  (lesson 04).
- **A dimensionless number is only as meaningful as its scales.** "Reynolds
  number 10" means nothing without $L$. The demo prints the scales in every
  table for this reason.
- **The Froude number $Fr = U/\sqrt{gL}$** measures the importance of gravity;
  it is the relevant parameter for lake seiches and for the distinction between
  subcritical and supercritical open-channel flow.

## 4. Physical interpretation: the approximation ladder

This table is the central reference of the lesson. Each row is a regime, the
terms dropped to obtain it, and what the approximation costs.

| Regime | Retained balance | Dropped terms | Error introduced | Validity |
|---|---|---|---|---|
| Hydrostatic | $-\nabla p + \rho\mathbf{g} = 0$ | all inertia, all viscosity | No motion at all; cannot predict flow, only pressure | $|\mathbf{u}|/gL \ll 1$ and slow evolution |
| Stokes (creeping) | $-\nabla p + \mu\nabla^2\mathbf{u} + \rho\mathbf{g} = 0$ | $\rho\,\mathrm{D}\mathbf{u}/\mathrm{D}t$ | $O(Re)$ relative error in velocity | $Re \lesssim 0.1$; magma, mantle, fine sediment, groundwater |
| Euler (inviscid) | $\rho\,\mathrm{D}\mathbf{u}/\mathrm{D}t = -\nabla p + \rho\mathbf{g}$ | $\mu\nabla^2\mathbf{u}$ | No boundary layer, no drag, no dissipation | $Re \gg 1$ away from walls; large-scale atmosphere and ocean |
| Boundary layer | full, but with $\partial_x \sim 1/L$, $\partial_y \sim 1/\delta$ | streamwise diffusion | Scales as $(\delta/L)^2$ | Thin layer, $\delta/L \ll 1$ |
| Boussinesq | full, with $\rho = \rho_0[1-\alpha(T-T_0)]$ and $\rho_0$ constant except in the buoyancy term | density variations in inertia and continuity | $O(\alpha\Delta T)$, typically $10^{-2}$ | Mantle convection, ocean and atmosphere interiors |
| Geostrophic | $\rho f\hat{z}\times\mathbf{u} = -\nabla p$ | inertia, viscosity | Fails near the equator and at small scales | $Ro \ll 1$ (lesson 07) |
| Darcy | $\mathbf{q} = -(k/\mu)(\nabla p - \rho\mathbf{g})$ | inertia, and viscosity replaced by a drag | Fails above pore-scale $Re \sim 1\text{–}10$ | Porous media (lesson 05) |

Three of these deserve an explicit statement of the cost.

**The hydrostatic approximation** is the one geophysicists use most and
examine least. It is *not* a statement that the fluid is at rest; it is the
statement that vertical accelerations are negligible compared with gravity. It
is used in oceanography for flows with horizontal scales of kilometres or more
and in the atmosphere for synoptic scales, and it breaks down in convection
plumes, in internal-wave breaking and in atmospheric thunderstorms.

**The Boussinesq approximation** is subtler than it looks. It assumes that
density variations, though large enough to drive motion through buoyancy, are
too small to matter in the inertia, except in the gravitational term. For the
mantle, $\alpha\Delta T \approx 3\times10^{-5}\times2500 \approx 0.075$, which is
comfortably small; for a lake heated to $25$ °C, it is of order $10^{-2}$; for a
boiling hydrothermal system, it is not valid at all.

**Neglecting viscosity in an inviscid model** removes the only mechanism of
energy dissipation. An inviscid model conserves energy exactly and therefore
cannot predict the final state of a turbulent flow; it can only describe the
early stages. This is why weather and climate models are formulated with
parameterised friction rather than zero friction (lesson 04).

## 5. Assumptions and regime of validity

| Assumption | Valid when | Fails when | What breaks |
|---|---|---|---|
| Continuum hypothesis | Mean free path $\ll$ smallest scale of interest | Rarefied gas; also, in a porous medium, at scales below the pore size | Fields are not defined pointwise; use a volume average |
| Newtonian stress, equation (3) | Strain rates small enough that stress is linear in rate | Magma with $>30$ per cent crystals, mudflows, polymer solutions | Requires a non-Newtonian constitutive law |
| Constant $\mu$ | Temperature and composition uniform | Large temperature contrasts (mantle, magma chambers) | $\mu\nabla^2\mathbf{u}$ no longer valid; keep $\nabla\cdot\boldsymbol{\tau}$ with $\mu(\mathbf{x})$ |
| Stokes hypothesis $\zeta = 0$ | Incompressible or weakly compressible flow | Strong compressions; sound attenuation studies | Error in the dissipation and in acoustic attenuation |
| Incompressible | $M \ll 1$, or pressure changes $\ll K$ | Gas flows at $M > 0.3$, explosive volcanism, the outer core's dynamo at large scale | Continuity becomes a prognostic equation for $\rho$ |
| Boussinesq | $\alpha\Delta T \ll 1$ | Boiling systems, strong stratification | Buoyancy and inertia are no longer separable |

## 6. Units and dimensional analysis

Checking dimensions of equation (4) term by term:

$$[\rho\,\mathrm{D}\mathbf{u}/\mathrm{D}t] =
\mathrm{kg\,m^{-3}}\cdot\mathrm{m\,s^{-2}} = \mathrm{N\,m^{-3}},$$

$$[\nabla p] = \mathrm{Pa\,m^{-1}} = \mathrm{N\,m^{-3}}, \qquad
[\mu\nabla^2\mathbf{u}] = \mathrm{Pa\,s}\cdot\mathrm{m\,s^{-1}\,m^{-2}} =
\mathrm{Pa\,m^{-1}} = \mathrm{N\,m^{-3}}.$$

Every term has the dimensions of force per unit volume. This is the fastest
consistency check available on any fluid equation: if one term differs, the
derivation is wrong.

The dimensionless groups that appear in this module:

| Group | Definition | Meaning | Geophysical value |
|---|---|---|---|
| Reynolds $Re$ | $\rho UL/\mu$ | inertia / viscous | $10^{-20}$ (mantle) to $10^{10}$ (atmosphere) |
| Froude $Fr$ | $U/\sqrt{gL}$ | inertia / gravity | $\sim 1$ for river rapids |
| Rossby $Ro$ | $U/(fL)$ | inertia / Coriolis | $10^{-3}$ for ocean gyres (lesson 07) |
| Ekman $Ek$ | $\nu/(fL^2)$ | viscous / Coriolis | $\ll 1$ in the ocean interior |
| Prandtl $Pr$ | $\nu/\kappa$ | momentum / heat diffusion | $\sim 7$ for water, $\sim 0.7$ for air, $\sim 10^{23}$ for the mantle |
| Rayleigh $Ra$ | $\rho g\alpha\Delta T L^3/(\kappa\mu)$ | buoyancy drive / diffusion | $\sim 10^7$ for the mantle (lesson 06) |

The Prandtl number of the mantle deserves a sentence. With $\nu = \mu/\rho
\approx 3\times10^{17}\ \mathrm{m^2\,s^{-1}}$ and $\kappa \approx
10^{-6}\ \mathrm{m^2\,s^{-1}}$, $Pr \approx 10^{23}$. Momentum diffuses
essentially instantaneously on geological timescales while heat does not. That
is why mantle convection is a Stokes flow — and why the appropriate stability
parameter is a Rayleigh number built on the *thermal* diffusivity.

## 7. Python demonstration

[`code/navier_stokes_demo.py`](./code/navier_stokes_demo.py) constructs an exact
solution, verifies it, nondimensionalises the equation, and tabulates the term
magnitudes for five geophysical flows. Its actual output includes:

```text
gap h = 1.0 mm, -dp/dx = 1.000e+04 Pa/m, mu = 0.001 Pa s
  u_max  = G h^2 / (8 mu)  = 1.250000e+00 m/s
  u_mean = G h^2 / (12 mu) = 8.333333e-01 m/s
  u_mean / u_max = 0.666667  (exact value 2/3)
  flow rate per unit width, trapezoidal/numeric Q = 8.333333e-04 m^2/s
  analytic  Q = h u_mean = 8.333333e-04 m^2/s   relative error 1.25e-11
```

```text
   y/h    mu*d2u/dy2 (Pa/m)    -dp/dx (Pa/m)    residual (Pa/m)
  0.10        -10000.000000     10000.000000          4.551e-08
  0.50        -10000.000000     10000.000000          1.565e-07
  worst residual = 1.565e-07 Pa/m, i.e. round-off at the finite-difference step 1e-6 m
```

```text
                        flow      rho        mu    L (m)    U (m/s)         Re  inertia/viscous
    water in a 1 mm fracture   1000.0  1.00e-03    0.001   1.00e-02  1.000e+01        1.000e+01
   water in a 0.1 m borehole   1000.0  1.00e-03      0.1   1.00e+00  1.000e+05        1.000e+05
             air, sea breeze      1.2  1.80e-05    1e+03   5.00e+00  3.333e+08        3.333e+08
    basaltic magma in a dike   2500.0  1.00e+02        1   1.00e-01  2.500e+00        2.500e+00
           mantle convection   3300.0  1.00e+21    1e+06   1.00e-09  3.300e-21        3.300e-21
```

```text
                          flow     inertia     viscous    pressure  inertia/vis           kept balance
          slow magma in a dike   2.500e-03   1.000e-01   1.000e+05    2.500e-02  Stokes (drop inertia)
     groundwater in a fracture   1.000e+02   1.000e+01   1.000e+04    1.000e+01     full Navier-Stokes
                    river flow   1.000e+02   1.000e-05   1.000e+02    1.000e+07 Euler (drop viscosity)
             mantle convection   3.300e-21   1.000e+00   1.000e-02    3.300e-21  Stokes (drop inertia)
ocean western boundary current   1.025e-02   1.000e-13   1.000e-01    1.025e+11 Euler (drop viscosity)
```

### What to observe

| Observation | Consequence |
|---|---|
| The measured flow rate matches the analytic $h u_{\text{mean}}$ to $1.3\times10^{-11}$ | The quadrature and the analytic expression agree; the 2/3 ratio of mean to maximum velocity is recovered |
| The steady x-momentum residual is at most $1.6\times10^{-7}$ Pa m⁻¹ against terms of $10^4$ | Poiseuille flow is an *exact* solution, not a numerical approximation; the residual is the finite-difference truncation |
| $du/dx + dv/dy + dw/dz = 0$ exactly for $\mathbf{u} = (u(y),0,0)$ | Continuity for this flow is an identity; it is the reason the nonlinear term vanishes and the equation is linear |
| The mantle's inertia/viscous ratio is $3.3\times10^{-21}$ | The Stokes approximation is not a convenience for the mantle; it is accurate to twenty digits. Retaining inertia in a mantle model is a modelling error, not a conservative choice |
| The river and the western boundary current give ratios of $10^7$ and $10^{11}$ | Viscosity is negligible *in the interior*; it must still be retained in a boundary layer or the model predicts no drag at all |
| The fracture and the borehole differ in $Re$ by four orders of magnitude at the same velocity | $Re$ without a length scale is meaningless; the demo prints $L$ in every row |

> **Breaking exercise.** In the Poiseuille section, change the driving gradient
> by a factor of ten and predict, before running, the change in $u_{\text{max}}$
> and in the residual. Then change the gap $h$ by a factor of two and predict
> the change in flow rate. The first is linear, the second cubic — and both
> predictions should be checkable against the printed formulas.

## 8. Common mistakes

1. **Quoting a Reynolds number without its length scale.** Every $Re$ in this
   module is accompanied by $U$ and $L$ for that reason.
2. **Confusing incompressible with constant density.** Incompressible means
   $\nabla\cdot\mathbf{u} = 0$; the density may still vary in space (the ocean
   does), and buoyancy may still drive motion.
3. **Dropping inertia in a flow that is not creeping.** $Re = 10$ is not
   creeping; the Stokes solution may be qualitatively wrong.
4. **Keeping inertia but dropping viscosity.** This gives a model with no
   dissipation and no drag, and it fails at the boundary of any real domain.
5. **Applying the Boussinesq approximation to a strongly stratified or boiling
   system.** Check $\alpha\Delta T$ before using it.
6. **Forgetting that the material derivative contains advection.** A steady
   flow can accelerate parcels; setting $\partial\mathbf{u}/\partial t = 0$ does
   not make the flow linear.
7. **Treating the Stokes hypothesis as exact.** It is an approximation about
   bulk viscosity and it is measurably false for many fluids.
8. **Assuming a Newtonian rheology for magma with abundant crystals.** The
   constitutive relation (3) is an idealisation; at high crystal content a yield
   stress appears.
9. **Using the Navier–Stokes equation in a porous medium at the pore scale.**
   Below the representative elementary volume the fields are not defined; use
   Darcy's law, derived in lesson 05.

## 9. Real-world applications

- **Groundwater flow.** The derivation of Darcy's law in
  [05](./05-porous-media-flow.md) begins from the Stokes limit of (4), which is
  why the preceding paragraph about $Re$ matters to hydrogeology.
- **Mantle convection.** Buoyancy-driven flow at $Re\sim10^{-20}$ is governed by
  (4) with inertia dropped; the resulting balance is the subject of
  [06](./06-mantle-convection.md).
- **Ocean and atmosphere.** Large-scale flow has $Re\sim10^{8}$–$10^{10}$ and
  $Ro \ll 1$: viscous terms are negligible, Coriolis is not (lesson 07).
- **Volcanology.** Magma in a conduit is a Stokes flow with a
  temperature-dependent viscosity, and the transition from Newtonian to
  yield-stress rheology is where the physics becomes hard.
- **Sediment transport.** The threshold of motion follows from the balance of
  the Stokes drag on a grain against its submerged weight, both of which come
  from (4).
- **Turbulence modelling.** Climate and weather models solve (4) on a grid far
  coarser than the Kolmogorov scale, and represent the unresolved stress with a
  parameterisation — the honesty about which is the subject of lesson 04.

## 10. Further reading

- **Batchelor, G. K. *An Introduction to Fluid Dynamics* (Cambridge University
  Press).** The definitive careful derivation of the stress tensor of a
  Newtonian fluid and the approximations that follow. Level: advanced.
- **Landau, L. D., & Lifshitz, E. M. *Fluid Mechanics* (Pergamon).** Concise and
  exacting; the place to look for the bulk-viscosity and Boussinesq arguments.
  Level: graduate.
- **Tritton, D. J. *Physical Fluid Dynamics* (Oxford University Press).** Uses
  geophysical examples throughout and is unusually explicit about regimes.
  Level: advanced.
- **Pedlosky, J. *Geophysical Fluid Dynamics* (Springer).** The standard
  derivation of the Boussinesq and geostrophic approximations. Level: graduate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (Cambridge University Press).**
  The Stokes limit and its use for the mantle, with the parameter values.
  Level: advanced.
- **Acheson, D. J. *Elementary Fluid Dynamics* (Oxford University Press).** A
  compact introduction to the inviscid and viscous balances, with worked
  examples. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [01 Fluid Statics, Pressure and Buoyancy](./01-fluid-statics.md) — the
  balancing terms, before motion was added.
- [03 Viscous Flow, Reynolds Number and Boundary Layers](./03-viscous-flow.md) —
  what the $1/Re$ term does when $Re$ is large.
- [04 Turbulence, Mixing and Eddy Diffusivity](./04-turbulence.md) — what the
  nonlinear term does when $Re$ is large.
- [05 Flow in Porous Media: Darcy's Law and Permeability](./05-porous-media-flow.md)
  — the Stokes limit, volume-averaged.
- [06 Mantle Convection and Rayleigh–Bénard Instability](./06-mantle-convection.md)
  — the Boussinesq limit, with buoyancy from a temperature field.
- [07 Rotating Fluids, Coriolis Effect and Geostrophic Balance](./07-geophysical-fluids.md)
  — the additional term that rotation adds to (4).
- [02-04-05 The Elastodynamic Equation of Motion](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — the same momentum balance with a strain-based constitutive law.

Exercises:
[`exercises/02-conservation-fluid-exercises.md`](./exercises/02-conservation-fluid-exercises.md)
and
[`exercises/02-conservation-fluid-solutions.md`](./exercises/02-conservation-fluid-solutions.md).

## Self-assessment checklist

- [ ] I can derive continuity from a control-volume mass balance and explain
      why it needs no constitutive assumption. (Section 3.1)
- [ ] I can derive the momentum equation from Newton's second law for a parcel.
      (Section 3.3)
- [ ] I can state the definition of a Newtonian fluid and the Stokes
      hypothesis, and say when each fails. (Section 2, 5)
- [ ] I can nondimensionalise the momentum equation and define the Reynolds
      number in terms of the terms it compares. (Section 3.5)
- [ ] I can name, for any geophysical flow, which terms are dropped and what the
      error is. (Section 4)
- [ ] I can check any fluid equation dimensionally in one step. (Section 6)
- [ ] I can compute a Prandtl number and say why the mantle's is extraordinary.
      (Section 6)
- [ ] I can verify an exact solution numerically and distinguish truncation
      error from a physics error. (Section 7)
