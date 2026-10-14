---
id: 02-06-03
title: "Viscous Flow, Reynolds Number and Boundary Layers"
level: advanced
prereqs: ["02-06-02"]
estimated_minutes: 90
tags: [viscosity, reynolds-number, boundary-layer, poiseuille]
---

# Viscous Flow, Reynolds Number and Boundary Layers

## Learning objectives

By the end of this lesson you will be able to:

1. **Solve** the two canonical viscous flows — Couette and Poiseuille — and
   extract from them the flow rate, the maximum velocity and the equivalent
   permeability.
2. **Compute** the Reynolds number for flow in a fracture and in a borehole, and
   state whether Darcy's law can possibly apply to each.
3. **Derive** the Blasius scaling for a laminar boundary layer and its turbulent
   counterpart, and state the transition criterion in terms of a local Reynolds
   number.
4. **Compute** Stokes drag, terminal velocity and the self-consistency condition
   under which the Stokes solution is valid.
5. **Explain** the lubrication approximation and use it to justify the cubic law
   for a fracture, including the range of aperture over which it holds.
6. **Compare** momentum and thermal diffusion times and use the comparison to
   classify a flow.

## Prerequisites

- [02-06-02 Continuity and Momentum Equations; Navier–Stokes](./02-conservation-fluid.md)
  — the equation being solved, and the Reynolds number introduced there.
- [02-06-01 Fluid Statics, Pressure and Buoyancy](./01-fluid-statics.md) — the
  hydrostatic pressure that a conduit flow is measured against.

## 1. Why viscosity matters at all

The viscosity of water is about $10^{-3}$ Pa s. That is a small number, and it is
tempting to conclude that viscosity never matters. It does, for three reasons
that together determine the structure of this lesson:

- **It sets the profile, not just the total flow.** In a conduit, viscosity
  determines *how* the velocity is distributed across the section, and therefore
  the flow rate, the shear at the wall, and the heat generation.
- **It acts in thin layers even when the bulk flow is inviscid.** In a
  high-Reynolds-number flow the viscous term is negligible in the interior and
  dominant in a boundary layer of thickness $\delta \sim L/\sqrt{Re}$. Without
  that layer there is no drag at all — and a model with no drag cannot close an
  energy budget.
- **It is the only dissipative term.** Remove it and the kinetic energy of a
  flow is conserved exactly; the flow can never come to rest.

The practical question is never "is viscosity important?" but "at which scale,
and over which distance, is it important?" That question is answered by the
Reynolds number computed with the *right* length scale.

## 2. Precise definitions

**Shear viscosity $\mu$.** Defined by the Newtonian stress, lesson 02 equation
(3): shear stress equals $\mu$ times the shear rate.

**Kinematic viscosity $\nu = \mu/\rho$.** The momentum diffusivity, with units
m² s⁻¹ — the same units as a diffusion coefficient, which is exactly what it is.

**No-slip condition.** The fluid in contact with a solid boundary moves with the
boundary. This is an empirical condition, established for ordinary liquids and
gases at ordinary pressures; it fails for rarefied gases, for some polymer
melts, and for superhydrophobic surfaces. It is the boundary condition that makes
boundary layers exist.

**Laminar flow.** A flow whose streamlines are smooth and whose velocity field
is deterministic and reproducible. Governed by viscous stresses.

**Turbulent flow.** A flow with chaotic, three-dimensional, time-dependent
motion over a wide range of scales. Governed by a balance of inertia and viscous
stresses (lesson 04).

**Boundary layer.** The thin region next to a solid boundary in which the
velocity changes from zero (no-slip) to the interior value.

**Lubrication approximation.** The limit in which a flow is thin compared with
its extent, so that the pressure is essentially uniform across the thin
direction and the momentum balance reduces to a balance between pressure and
viscous shear. It is the approximation behind Poiseuille flow and, with a
volume average, behind Darcy's law.

## 3. Derivations

### 3.1 Couette flow

Consider fluid between two parallel plates: the lower fixed, the upper moving at
$U$ in the $x$ direction, with no pressure gradient. The momentum equation with
$\partial_x = 0$ reduces to $\mathrm{d}^2u/\mathrm{d}y^2 = 0$, so $u$ is linear:

$$u(y) = U\frac{y}{h}, \qquad \tau = \mu\frac{\mathrm{d}u}{\mathrm{d}y} =
\frac{\mu U}{h}. \tag{1}$$

The shear stress is constant across the gap. This is the simplest possible
viscous flow and the standard reference for a rotational viscometer: the torque
on the cylinder gives $\mu$ directly.

### 3.2 Plane Poiseuille flow and the cubic law

Let a pressure gradient $G = -\mathrm{d}p/\mathrm{d}x$ drive flow between plates
at $y = 0$ and $y = h$ with no-slip at both. The $x$-momentum balance is

$$\mu\frac{\mathrm{d}^2u}{\mathrm{d}y^2} = -G, \qquad u(0) = u(h) = 0, \tag{2}$$

with solution

$$u(y) = \frac{G}{2\mu}y(h-y), \qquad u_{\text{max}} =
\frac{Gh^2}{8\mu}, \qquad u_{\text{mean}} = \frac{Gh^2}{12\mu}. \tag{3}$$

The volume flux per unit width is

$$q = h u_{\text{mean}} = \frac{Gh^3}{12\mu}. \tag{4}$$

Equation (4) is the **cubic law**. Written in the Darcy form $q =
(k/\mu)G$, it defines an equivalent permeability

$$k = \frac{h^2}{12}. \tag{5}$$

This is where lesson 05's permeability comes from for a fracture: it is not a
property of a rock but of the *geometry* of a single conduit. A 1 mm aperture
gives $k = 8.33\times10^{-8}$ m², about 84 000 darcy — a number large enough that
a single open fracture can dominate the permeability of an otherwise tight rock
mass.

The same analysis in a circular pipe of radius $R$ gives

$$Q = \frac{\pi G R^4}{8\mu}, \qquad u_{\text{mean}} =
\frac{G R^2}{8\mu}. \tag{6}$$

Note the different dependence on the length scale: fourth power of radius for a
pipe, third power of aperture for a slot.

### 3.3 Reynolds number and the transition

The Reynolds number for a conduit flow is formed with the scale that matters:

$$Re = \frac{\rho U L}{\mu}, \qquad
L = \begin{cases} 2R & \text{circular pipe (diameter)} \\
4A/P & \text{arbitrary duct (hydraulic diameter)} \\
h & \text{aperture} \\
d & \text{grain size in a porous medium.}
\end{cases} \tag{7}$$

For a circular pipe the transition to turbulence is observed at $Re \approx
2000$–$4000$, with the exact value depending on the inlet conditions and the
roughness. For a **fracture**, the relevant transition is at a much larger
Reynolds number (of order 1000–2000 for a smooth parallel-plate cell), because
the flow is more constrained. For a **porous medium** the relevant criterion is a
pore-scale Reynolds number $Re_p = \rho q d/\mu$ with $q$ the specific discharge
and $d$ the grain size, and Darcy's law is trusted only while $Re_p \lesssim
1$–$10$.

### 3.4 Boundary layers

Consider uniform flow $U$ past a flat plate. The no-slip condition forces a
layer of thickness $\delta(x)$ to grow downstream. Scaling the streamwise
inertia against the cross-stream viscous term over the layer gives

$$U\frac{\partial u}{\partial x} \sim \frac{U^2}{x}, \qquad
\nu\frac{\partial^2 u}{\partial y^2} \sim \frac{\nu U}{\delta^2},
\qquad\Longrightarrow\qquad
\delta(x) \sim \sqrt{\frac{\nu x}{U}}. \tag{8}$$

The exact Blasius solution gives the numerical coefficient: the layer thickness
at which the velocity reaches 99 per cent of $U$ is

$$\delta(x) \approx 5.0\,\sqrt{\frac{\nu x}{U}} = \frac{5.0\,x}{\sqrt{Re_x}},
\qquad Re_x = \frac{Ux}{\nu}. \tag{9}$$

Once $Re_x \gtrsim 5\times10^5$ the layer becomes turbulent and

$$\delta(x) \approx 0.37\,x\,Re_x^{-1/5}. \tag{10}$$

Two derived thicknesses are used in transport problems: the **displacement
thickness** $\delta^* = \int_0^\infty(1-u/U)\,\mathrm{d}y \approx 1.72
\sqrt{\nu x/U}$, which is the distance the outer flow is displaced outwards, and
the **momentum thickness** $\theta = \int_0^\infty (u/U)(1-u/U)\,\mathrm{d}y
\approx 0.664\sqrt{\nu x/U}$, which gives the drag: $D = \rho U^2\theta$ per unit
width. The factor between them, $H = \delta^*/\theta \approx 2.59$, is a shape
factor used to diagnose separation.

### 3.5 Stokes flow and drag

For $Re \ll 1$ the inertia term is negligible and the momentum equation becomes
linear. The drag on a sphere of radius $a$ moving at velocity $U$ through a fluid
at rest is

$$F_D = 6\pi\mu a U, \tag{11}$$

and balancing it against the submerged weight gives the terminal velocity

$$w = \frac{2(\rho_s-\rho_f)ga^2}{9\mu}. \tag{12}$$

Equation (12) is valid only while $Re = \rho_f w(2a)/\mu$ is small; the
self-consistency check is not optional, and it is the reason the demo prints $Re$
next to every settling velocity.

### 3.6 Diffusion times

Viscosity is a diffusion coefficient for momentum, so the time for momentum to
diffuse a distance $L$ is $t_\nu \sim L^2/\nu$. Heat diffuses with $\kappa$, so
$t_\kappa \sim L^2/\kappa$. Their ratio is the Prandtl number $Pr = \nu/\kappa$.
For water $Pr \approx 7$; for air $Pr \approx 0.7$; for the mantle $Pr \approx
10^{23}$. The last figure is the reason mantle convection is a Stokes flow whose
stability parameter must be built on the *thermal* diffusivity, not on the
momentum diffusivity.

## 4. Physical interpretation

**The cubic law is a powerful amplifier.** $q \propto h^3$: doubling an aperture
multiplies the flow by eight. A factor of ten in aperture changes the flow by a
thousand. This is why fracture permeability in the crust is so variable, why
in-situ stress (which opens and closes fractures) changes aquifer behaviour so
sharply, and why hydraulic conductivity in the crust spans so many orders of
magnitude — the handbook quotes crustal hydraulic diffusivity as $10^{-2}$ to
$10^0\ \mathrm{m^2\,s^{-1}}$, a range set by fracture aperture and spacing.

**Boundary-layer thickness is what sets the drag.** For the ocean surface layer,
the boundary layer is metres thick for a laminar estimate and hundreds of metres
for the turbulent one; the momentum flux into the ocean that a weather model must
represent is that thickness times a velocity scale. The laminar Blasius formula
is only applicable below $Re_x \approx 5\times10^5$, which for a 100 km fetch is
reached at velocities of millimetres per second. **Every real geophysical
boundary layer at geophysical fetch is turbulent**, and the number that enters a
climate model is a parameterisation, not equation (9).

**Rotation and stratification bound boundary layers in the ocean.** The
flat-plate result assumes no rotation, no depth limit and no stratification.
Real ocean boundary layers are limited by the Ekman depth (lesson 07) and by the
mixed-layer depth; the flat-plate thicknesses quoted in the demo are upper bounds
from an idealisation.

## 5. Assumptions and regime of validity

| Assumption | Valid when | Fails when | What breaks |
|---|---|---|---|
| No-slip at the wall | Ordinary liquids and gases, ordinary pressures | Rarefied gas; superhydrophobic surfaces | A slip length must be introduced |
| Laminar, steady Poiseuille solution | $Re$ below the transition for that geometry | $Re \gtrsim 2000$ (pipe), $\gtrsim 10^3$ (slot) | Flow rate no longer follows the fourth or third power; turbulent friction law needed |
| Constant viscosity | Isothermal flow | Strong temperature gradients | $\mu(T)$ must be carried; the profile changes shape |
| Lubrication (thin film) | Aperture $\ll$ length and width | Wide conduits, entrance regions | The pressure is no longer uniform across the section |
| Smooth walls | Roughness $\ll$ aperture | Rough fractures, gravel | An effective aperture (hydraulic aperture) replaces $h$, usually smaller |
| Stokes drag | $Re \ll 1$ | $Re \gtrsim 0.1$–$1$ | Drag law must be corrected (Schiller–Naumann and similar) |
| Blasius boundary layer | Flat plate, zero pressure gradient, $Re_x < 5\times10^5$ | Adverse pressure gradient, roughness, higher $Re_x$ | Separation or transition to turbulence |

The most consequential entry in this table for hydrogeology is the **hydraulic
aperture**. A real fracture is not a pair of parallel smooth plates; its
aperture varies in space, and the flow is dominated by the widest patches. The
permeability that reproduces the measured flow is the *hydraulic* aperture, which
is smaller than the mean mechanical aperture and cannot be computed from
geometry alone — it must be measured by a flow test. The cubic law gives the
functional form; the aperture is an empirical parameter.

## 6. Units and dimensional analysis

$$[\mu] = \mathrm{Pa\,s} = \mathrm{kg\,m^{-1}s^{-1}}, \qquad [\nu] =
\mathrm{m^2\,s^{-1}}. \tag{13}$$

Check the cubic law dimensionally:
$[h^3/(12\mu)\cdot G] = \mathrm{m^3}\cdot\mathrm{m^{-1}s\,kg^{-1}}\cdot
\mathrm{kg\,m^{-2}s^{-2}} = \mathrm{m^2\,s^{-1}}$, which is a volume flux per
unit width. Correct.

Useful orders of magnitude for $\mu$ at room conditions: water $10^{-3}$ Pa s;
air $1.8\times10^{-5}$ Pa s; olive oil $10^{-1}$ Pa s; basaltic magma
$10$–$10^3$ Pa s (strongly temperature- and crystal-dependent, hence nominal);
upper mantle $10^{19}$–$10^{22}$ Pa s (handbook Sec. 3.4). The span from air to
mantle is 27 orders of magnitude, which is why the same equation is solved with
inertia retained in one case and dropped in the other.

The dimensionless groups used in this lesson, all formed from the same four
quantities $\rho$, $U$, $L$, $\mu$ or $\nu$:

| Group | Definition | Threshold | Meaning at the threshold |
|---|---|---|---|
| $Re_L$ | $UL/\nu$ | $\sim 2000$ (pipe), $5\times10^5$ (plate) | Laminar/turbulent transition |
| $Re_p$ | $qd/\nu$ | 1–10 | Darcy validity limit |
| $Re_\delta$ | $u_*\delta/\nu$ | $\sim 5$ | Laminar sublayer thickness |
| $Pr$ | $\nu/\kappa$ | 1 | Momentum and heat diffuse equally |

## 7. Python demonstration

[`code/viscous_flow_demo.py`](./code/viscous_flow_demo.py) computes Reynolds
numbers for a fracture and a borehole, verifies the cubic law against a numerical
quadrature, and tabulates boundary layers and diffusion times. Its actual output
includes:

```text
   U (m/s)   Re(fracture, b=1mm)        regime   Re(borehole, d=0.1m)        regime
     1e-04             1.000e-01       laminar              1.000e+01       laminar
     1e-02             1.000e+01       laminar              1.000e+03       laminar
     1e-01             1.000e+02       laminar              1.000e+04     turbulent
     1e+00             1.000e+03       laminar              1.000e+05     turbulent
```

```text
aperture b = 1.0 mm, mu = 0.001 Pa s, -dp/dx = 1.0e+04 Pa/m
  q (cubic law)  = b^3 dp/dx/(12 mu) = 8.333333e-04 m^2/s
  q (quadrature)                       = 8.333333e-04 m^2/s  relative error 1.25e-11
  equivalent permeability k = b^2/12   = 8.3333e-08 m^2 = 84.4375 x 10^3 darcy
```

```text
borehole radius R = 0.050 m, length L = 100 m, head loss 1 m (dp = 9810.0 Pa)
  Hagen-Poiseuille Q = pi dp R^4/(8 mu L) = 2.407736e-01 m^3/s
  mean velocity ubar                      = 30.6563 m/s
  Re = rho ubar (2R)/mu                   = 3.066e+06  -> turbulent
```

```text
                    flow  U (m/s)    x (m)       Re_x  delta_l (m)  delta_t (m)   applicable
          water, x = 1 m     0.05    1e+00  5.000e+04   2.2361e-02   4.2502e-02      laminar
      air over a glacier     2.00    1e+03  1.333e+08   4.3301e-01   8.7743e+00    turbulent
   ocean surface current     0.10    1e+05  1.025e+10   4.9386e+00   3.6818e+02    turbulent
```

```text
          medium   nu (m^2/s)  kappa (m^2/s)      L (m)         t_mom       t_therm
     water, 1 mm    1.000e-06      1.400e-07      1e-03     1.000e+00     7.143e+00
 mantle, 1000 km    3.030e+17      1.000e-06      1e+06     3.300e-06     1.000e+18
```

### What to observe

| Observation | Consequence |
|---|---|
| At $U = 0.01\ \mathrm{m\,s^{-1}}$ the fracture is laminar ($Re=10$) while the borehole is still laminar at $Re=10^3$ | The transition is a property of the geometry as much as the fluid: at $U = 0.1\ \mathrm{m\,s^{-1}}$ the borehole is already turbulent at $Re=10^4$ |
| The quadrature matches the cubic law to $1.3\times10^{-11}$ | The closed form and the numerical integral are the same physics; the check is that no algebraic slip was made |
| $k = b^2/12 = 8.33\times10^{-8}$ m² is 84 000 darcy | One millimetre of aperture gives a permeability larger than almost any rock matrix; fracture flow dominates where fractures are open |
| The borehole solution gives 30.7 m s⁻¹ at $Re = 3.1\times10^6$ | The *formula* is exact but the *regime* has failed: a real borehole would deliver far less, because turbulent friction replaces the laminar wall law |
| The laminar boundary-layer estimate for the 100 km ocean fetch gives 4.9 m, while the turbulent estimate gives 368 m | Quoting the laminar value would be a regime error of a factor of 75; the ocean boundary layer is turbulent |
| Mantle momentum diffuses in $3.3\times10^{-6}$ s but heat needs $10^{18}$ s | The Prandtl number is enormous; the mantle is in Stokes balance but never in thermal equilibrium, which is exactly what makes it convect |

> **Breaking exercise.** Predict, before running, the change in fracture $q$ if
> the aperture is halved (eightfold reduction) and the change in borehole $Q$ if
> the radius is halved (sixteenfold reduction). Then predict what happens to
> the Reynolds number in each case, and note that the two answers move in
> *opposite* directions relative to the laminar threshold.

## 8. Common mistakes

1. **Applying the cubic law with the mechanical aperture.** The hydraulic
   aperture is smaller and must be measured; using the visible aperture
   overestimates flow, sometimes by an order of magnitude.
2. **Using the pipe formula for a fracture.** The mean-to-maximum ratio differs
   ($1/2$ versus $2/3$), so the flow rate at the same maximum velocity differs by
   33 per cent.
3. **Forgetting the no-slip condition.** It is the origin of every boundary layer
   and of all wall drag; a model without it predicts zero drag on a solid.
4. **Quoting a laminar boundary-layer thickness at a turbulent $Re_x$.** The demo
   prints both columns and flags the applicable one for this reason.
5. **Using Stokes drag outside its regime.** Always compute $Re$ from the
   predicted velocity and check.
6. **Treating Darcy's law as valid to any velocity.** It is a porous-medium
   statement with a pore-scale $Re \lesssim 1$–$10$ limit, and it does not apply
   to an open conduit at all.
7. **Assuming viscosity is constant.** For magma, $\mu$ changes by orders of
   magnitude over tens of kelvin near the glass transition.
8. **Confusing the momentum and thermal diffusion times.** They differ by the
   Prandtl number, which is 0.7 for air and $10^{23}$ for the mantle.
9. **Ignoring entrance effects.** Both Poiseuille solutions assume fully
   developed flow; the entrance length is of order $0.05\,Re\,d$.

## 9. Real-world applications

- **Aquifer and fracture hydrology.** The cubic law and its hydraulic aperture
  are the basis of discrete-fracture flow models. See
  [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md).
- **Borehole and pipe flow.** Laminar turbulent transition sets the pressure
  losses in drilling and production; the friction factor replaces the wall law.
- **Dike and conduit dynamics.** Magma ascent is a lubrication flow whose
  resistance is the competition between viscous stress and buoyancy.
- **Sedimentology.** The settling velocity and the Shields criterion for the
  onset of motion are both Stokes-based.
- **Ocean and atmosphere boundary layers.** Turbulent boundary layers control
  the fluxes of momentum, heat and gas between the fluid and the surface; every
  climate model parameterises them.
- **Microfluidics and rock physics.** At pore scale, the lubrication limit is
  how permeability is computed from pore geometry.

## 10. Further reading

- **Batchelor, G. K. *An Introduction to Fluid Dynamics* (Cambridge University
  Press).** The definitive treatment of Poiseuille and Stokes flows and of the
  lubrication approximation. Level: advanced.
- **Schlichting, H., & Gersten, K. *Boundary-Layer Theory* (Springer).** The
  reference for boundary layers in all their regimes, laminar and turbulent.
  Level: graduate.
- **Tritton, D. J. *Physical Fluid Dynamics* (Oxford University Press).**
  Excellent on the laminar/turbulent transition with experimental data.
  Level: advanced.
- **Zimmerman, R. W., & Bodvarsson, G. S. (1996). Hydraulic conductivity of rock
  fractures. *Transport in Porous Media*.** The canonical reference for the
  cubic law, its corrections and the hydraulic aperture. Level: graduate.
- **Bear, J. *Dynamics of Fluids in Porous Media* (Dover).** Includes the
  derivation of Darcy's law from the lubrication limit and the Reynolds-number
  limits of validity. Level: graduate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (Cambridge University Press).**
  Stokes flow applied to the mantle and to magma, with the parameter values.
  Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 Continuity and Momentum Equations; Navier–Stokes](./02-conservation-fluid.md)
  — where the $1/Re$ term and the meaning of the Reynolds number were derived.
- [04 Turbulence, Mixing and Eddy Diffusivity](./04-turbulence.md) — what happens
  above the transition.
- [05 Flow in Porous Media: Darcy's Law and Permeability](./05-porous-media-flow.md)
  — the lubrication limit, volume-averaged.
- [06 Mantle Convection and Rayleigh–Bénard Instability](./06-mantle-convection.md)
  — the Stokes limit on the largest scale in the solid Earth.
- [07 Rotating Fluids, Coriolis Effect and Geostrophic Balance](./07-geophysical-fluids.md)
  — Ekman layers, the rotating analogue of the boundary layer.
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../04-elasticity-and-continuum-mechanics/07-viscoelasticity.md)
  — the same diffusion mathematics applied to a solid.

Exercises:
[`exercises/03-viscous-flow-exercises.md`](./exercises/03-viscous-flow-exercises.md)
and [`exercises/03-viscous-flow-solutions.md`](./exercises/03-viscous-flow-solutions.md).

## Self-assessment checklist

- [ ] I can solve Couette and Poiseuille flow from the momentum equation.
      (Section 3)
- [ ] I can derive the cubic law and the equivalent permeability $h^2/12$.
      (Section 3.2)
- [ ] I can compute a Reynolds number with whichever length scale the geometry
      requires, and say which. (Sections 3.3, 7)
- [ ] I can compute $Re$ for a fracture and a borehole and say whether Darcy's
      law can apply. (Sections 3.3, 7)
- [ ] I can derive the boundary-layer thickness scaling and state the transition
      criterion. (Section 3.4)
- [ ] I can compute a settling velocity and check its self-consistency.
      (Section 3.5)
- [ ] I can compare momentum and thermal diffusion times and say what the ratio
      implies. (Sections 3.6, 7)
- [ ] I can state what the hydraulic aperture is and why it is not the geometric
      aperture. (Section 5)
