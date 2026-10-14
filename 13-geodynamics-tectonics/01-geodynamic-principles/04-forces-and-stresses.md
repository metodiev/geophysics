---
id: 13-01-04
title: "Driving Forces, Stress Fields and Intraplate Stress"
level: doctoral
prereqs: ["13-01-03", "04-02-03", "02-06-06"]
tags: [geodynamics, tectonophysics, plate-driving-forces, gravitational-potential-energy, intraplate-stress]
---

# Driving Forces, Stress Fields and Intraplate Stress

> All models and data in this module are **SYNTHETIC**. The thermal model and all
> parameters below are chosen teaching values, and every number quoted here is
> printed by `code/forces_and_stresses_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** gravitational potential energy (GPE) per unit area and **derive**
   it as a double integral of the density structure.
2. **Show** that for isostatically balanced columns the GPE difference is
   independent of the depth chosen for the integration, and **verify** it
   numerically.
3. **Compute** ridge push from a cooling-plate model and **state** why the answer
   is finite and geometry-independent.
4. **Compute** slab pull from the same integral applied to a subducting slab, and
   **compare** its magnitude with ridge push.
5. **Close the force balance** with a drag law, **derive** the resulting plate
   speed, and **state** precisely why this is a consistency check rather than a
   prediction.
6. **Translate** a GPE difference into an upper bound on intraplate deviatoric
   stress, and **explain** why it is a bound and not a measurement.
7. **Rank** the driving forces of plate tectonics by magnitude on a quantitative
   inventory, with uncertainty attached.

## Prerequisites

- [13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure](03-lithospheric-strength.md) —
  where the loads that generate these forces are quantified.
- [04-02-03 Driving Forces of Plate Motion](../../04-earth-science-geology/02-plate-tectonics/03-driving-forces.md) —
  the geological statement of the force inventory.
- [02-06-06 Mantle Convection and Rayleigh-Benard Instability](../../02-physics/06-fluid-mechanics/06-mantle-convection.md) —
  the convective framework in which these forces are boundary tractions.
- [13-01-01 Momentum, Mass and Energy Balances in the Solid Earth](01-momentum-mass-energy.md) —
  the balances that make a force balance the whole momentum equation.

## 1. Intuition: no engine, only buoyancy

Textbooks used to ask what "drives" plate tectonics, as if a torque were applied
somewhere. The modern answer is deflationary: plates are the cold upper boundary
layer of a convecting fluid, and they move because their own density structure
makes one configuration of the surface energetically cheaper than another. The
forces are not external; they are the horizontally integrated consequences of
buoyancy differences *within* the plate and *within* its attached slab.

There are exactly two large forces, and one of them is easy to underestimate:

- **Slab pull.** Subducted lithosphere is cold, therefore dense, therefore heavy.
  A slab hanging from a plate pulls it. In the model below this is
  $42.0\ \mathrm{TN\,m^{-1}}$, roughly ten times the second force.
- **Ridge push.** Young lithosphere is hot, therefore light, therefore buoyant.
  It pushes away from the ridge. The model gives $4.11\ \mathrm{TN\,m^{-1}}$.

Everything else is either a resistance (basal drag, mantle wedge suction, friction
on the megathrust, bending) or a second-order modulation. The reason "ridge push"
was long considered a small effect and is now known to be the second largest is
simply that its integral is easy to botch; doing it carefully is one of the two
technical goals of this lesson.

The second goal is to make the *signs* and the *directions* explicit. Slab pull
pulls the plate towards the trench; ridge push pushes it away from the ridge. On
the same plate those are the *same* direction, which is why the plate speeds
correlate with slab length and why the two forces add.

## 2. Gravitational potential energy per unit area

### 2.1 Definition

For a lithospheric column the GPE per unit area (J m$^{-2}$) is the vertical
integral of the vertical normal stress. With $\zeta$ measured *upward* from a
chosen compensation depth,

$$\mathrm{GPE} = \int \sigma_{zz}\,\mathrm{d}z = g\int \zeta\,\rho(\zeta)\,
\mathrm{d}\zeta .$$

The absolute value is enormous — hundreds of gigajoules per square metre,
because it includes the whole lithostatic load — so it is only ever *differences*
between columns that carry information. That is not a defect of the definition;
it is the reason the calculation is stable.

### 2.2 Why the answer does not depend on the compensation depth

Consider two columns in isostatic equilibrium: their mass per unit area down to
any depth below the compensation level is equal. That is the meaning of isostasy,

$$\int_0^{D}\left[\rho_a(\zeta) - \rho_b(\zeta)\right]\mathrm{d}\zeta = 0
\quad\text{for any } D ,$$

so the zeroth moment of the density difference vanishes. The GPE difference is
the *first* moment,

$$\Delta\mathrm{GPE} = g\int_0^{D}\zeta\left[\rho_a - \rho_b\right]\mathrm{d}\zeta
= g\int_0^{D}(\zeta - D)\left[\rho_a - \rho_b\right]\mathrm{d}\zeta ,$$

and the second form shows the $D$-dependence explicitly: it multiplies the zeroth
moment, which is zero. **The GPE difference is independent of the compensation
depth.** The demonstration verifies this by repeating the ridge-push integral
with $D = 200$, $400$ and $800$ km:

| $D$ (km) | $F_{RP}$ (N m$^{-1}$) |
|---|---|
| 200 | $-4.1172\times10^{12}$ |
| 400 | $-4.1251\times10^{12}$ |
| 800 | $-4.1128\times10^{12}$ |

The spread across an eightfold change in $D$ is $3.0\times10^{-3}$ relative. In
practice this identity is *the* test that an implementation of these integrals is
right; an implementation that violates it has a mass-balance error that no amount
of care with the integrand will hide.

### 2.3 Reading the sign

$F = g\int\zeta\,\Delta\rho\,\mathrm{d}\zeta$ with $\Delta\rho = \rho_{\text{old}}
- \rho_{\text{ridge}}$ came out *negative*: the old plate is dense relative to the
ridge column, so the ridge column has the larger GPE, so material flows *away*
from the ridge. The magnitude is the force; the sign tells you the direction of
the resulting pressure gradient. Reporting a driving force without its direction
is reporting half the physics, and it is the half that determines whether the
plate speeds predicted later have the right sign.

## 3. Ridge push from a cooling plate

### 3.1 The thermal model

A cooling half-space has (SYNTHETIC parameters $T_m = 1300$ K,
$\kappa = 10^{-6}$ m$^{2}$ s$^{-1}$, $\alpha = 3\times10^{-5}$ K$^{-1}$,
$\rho_m = 3300$ kg m$^{-3}$)

$$T(z,t) = T_m\,\mathrm{erf}\!\left(\frac{z}{2\sqrt{\kappa t}}\right),
\qquad
\Delta\rho(z,t) = \rho_m\alpha\left[T_m - T(z,t)\right] .$$

The subsidence follows from requiring the column mass to be unchanged while the
water column above the plate thickens:

$$s(t) = \frac{2\rho_m\alpha T_m}{\rho_m - \rho_w}\sqrt{\frac{\kappa t}{\pi}} .$$

Measured with $\rho_w = 1030$ kg m$^{-3}$:

| age (Myr) | subsidence (m) | depth of the 600 K isotherm (km) |
|---|---|---|
| 10 | 1136.5 | 15.5 |
| 50 | 2541.2 | 34.6 |
| 100 | 3593.8 | 48.9 |

Both scalings are $\sqrt{t}$: the plate thickens as $\sqrt{\kappa t}$ and the
subsidence grows as the same $\sqrt{t}$. Thermal subsidence is the most precisely
predicted observable in tectonics, and its $\sqrt{t}$ law is a direct signature of
conduction.

### 3.2 The force

Integrating §2.1 over the difference between the ridge column (uniform
$\rho_m$) and a 100 Myr old column (cold anomaly *plus* the water layer above the
subsided surface) gives

$$F_{RP} = 4.11\times10^{12}\ \mathrm{N\,m^{-1}} = 4.11\ \mathrm{TN\,m^{-1}},
\qquad \text{spread over } D = 200\text{–}800\ \mathrm{km}: 3.0\times10^{-3}.$$

That ridge push is *finite* is worth pausing on: a half-space cooling model has
no base, yet the dense-anomaly integral converges because $\mathrm{erfc}$
decays faster than $\zeta$ grows. The force is set by the top few hundred
kilometres, not by the plate's eventual thickness.

## 4. Slab pull from the same integral

### 4.1 The integral

For a slab of thickness $h$ and down-dip length $L$ (age at subduction $t$), the
force per unit trench length is the double integral of the density anomaly over
the slab's cross-section:

$$F_{SP} = gL\int_0^{h}\Delta\rho(y,t)\,\mathrm{d}y .$$

Measured for $h = 100$ km, $L = 600$ km, $t = 100$ Myr:

$$\int_0^{h}\Delta\rho\,\mathrm{d}y = 7.1423\times10^{6}\ \mathrm{kg\,m^{-2}},
\qquad
\langle\Delta\rho\rangle = 71.42\ \mathrm{kg\,m^{-3}},$$

$$F_{SP} = 4.2039\times10^{13}\ \mathrm{N\,m^{-1}} = 42.04\ \mathrm{TN\,m^{-1}} .$$

The thickness dependence is instructive:

| slab thickness (km) | $F_{SP}$ (TN m$^{-1}$) |
|---|---|
| 50 | 28.67 |
| 75 | 36.87 |
| 100 | 42.04 |

Sub-linear in $h$ because the deeper part of a cooling slab is less anomalous: the
first 50 km contributes 68% of the force of the first 100 km.

### 4.2 A crude estimate, as a check

Replacing the $\mathrm{erf}$ profile by its mean over the slab,
$\rho_m\alpha T_m/2 = 64.35$ kg m$^{-3}$, gives

$$F_{\text{block}} = g\,\frac{\rho_m\alpha T_m}{2}\,hL
= 3.7876\times10^{13}\ \mathrm{N\,m^{-1}},$$

low by **9.9%**. A physical estimate that is right to 10% is *good* in this
subject, and it is worth internalising the block formula as a mental calculator —
with the knowledge that it is systematically low because the real profile is
bottom-heavy.

The ratio of the two great forces is

$$\frac{|F_{SP}|}{|F_{RP}|} = \frac{42.04}{4.11} = 10.2 .$$

That number, not a diagram, is why plate speeds correlate most strongly with the
length of subducting slab attached to a plate.

## 5. Closing the balance: the plate speed

### 5.1 The drag law

Take the plate as a sheet of length $L_p$ sheared over an asthenospheric channel
of thickness $d$ with viscosity $\eta$ (SYNTHETIC: $\eta = 10^{21}$ Pa s,
$d = 200$ km, $L_p = 5000$ km). The basal shear stress is
$\tau = \eta u/d$ and the total resisting force per unit length is
$\tau L_p$:

$$u = \frac{(|F_{SP}| + |F_{RP}|)\,d}{\eta L_p} .$$

### 5.2 The numbers

$$|F_{SP}| + |F_{RP}| = 4.6152\times10^{13}\ \mathrm{N\,m^{-1}},
\qquad
u = \frac{(4.6152\times10^{13})(2\times10^{5})}{(10^{21})(5\times10^{6})}
= 1.8461\times10^{-9}\ \mathrm{m\,s^{-1}} = 58.3\ \mathrm{mm\,yr^{-1}},$$

$$\tau = \frac{\eta u}{d} = 9.2304\times10^{6}\ \mathrm{Pa} = 9.23\ \mathrm{MPa} .$$

Two things are being demonstrated and one is not.

- **Demonstrated:** the force balance *closes*. Two independently computed
  buoyancy integrals, divided by a drag law, land within a factor of about two of
  observed plate speeds. Forces of order $10^{13}$ N m$^{-1}$, stresses of order
  10 MPa and speeds of order $10^{-9}$ m s$^{-1}$ are mutually consistent.
- **Demonstrated:** the basal shear stress required is a few MPa, comparable to
  the strength of the lithosphere derived in
  [13-01-03](03-lithospheric-strength.md). That is the quantitative statement
  that mantle drag is neither negligible nor dominant.
- **Not demonstrated:** the *value* of the speed. $\eta$ and $d$ were chosen;
  changing $\eta$ by a factor of 10 changes $u$ by a factor of 10. A figure of
  58 mm/yr carries no more information than the ratio of a chosen force to a
  chosen viscosity. The honest phrasing is "the observed speeds are consistent
  with these forces and an upper-mantle viscosity of order $10^{21}$ Pa s", and
  the honest follow-up is that this is one of the constraints used to *infer*
  mantle viscosity, with all the non-uniqueness that entails.

## 6. Intraplate stress from GPE differences

### 6.1 Thickened crust

Take a normal crustal column ($h_1 = 35$ km) and a plateau column ($h_2 = 70$ km),
both in Airy isostasy with $\rho_c = 2800$, $\rho_m = 3300$ kg m$^{-3}$. The
plateau's elevation is

$$e = (h_2 - h_1)\frac{\rho_m - \rho_c}{\rho_m}
= (35\ \mathrm{km})\frac{500}{3300} = 5303\ \mathrm{m}.$$

The GPE difference, computed by direct integration between the two columns, is

$$\Delta\mathrm{GPE} = 7.6483\times10^{12}\ \mathrm{J\,m^{-2}}
= 7.65\ \mathrm{TN\,m^{-1}},$$

and there is a closed form to check it against:

$$\Delta\mathrm{GPE} = \frac{g}{2}\left(h_2^{2} - h_1^{2}\right)
(\rho_m - \rho_c)\frac{\rho_c}{\rho_m} = 7.6473\times10^{12}\ \mathrm{J\,m^{-2}},$$

agreeing to $1.3\times10^{-4}$ relative — the numerical double integral is
correct. (Deriving that closed form is exercise ★★2; the route is to write
$\mathrm{GPE}$ as a function of crustal thickness, as in §2.1, and difference it.)

### 6.2 From GPE to stress

The plateau has *higher* GPE than its surroundings, so the horizontal deviatoric
stress inside it is *extensional*. A bound on the mean deviatoric stress follows
by dividing the excess by the layer that must carry it:

$$\langle\sigma_{xx} - \sigma_{zz}\rangle \lesssim
\frac{\Delta\mathrm{GPE}}{h_2}
= \frac{7.6483\times10^{12}}{7\times10^{4}}
= 1.093\times10^{8}\ \mathrm{Pa} = 109\ \mathrm{MPa} .$$

**This is an upper bound, and the distinction matters.** The derivation assumes
the excess GPE is carried uniformly over the full thickness of the thickened
crust and that no part of it is relaxed by flow. Real plateaus relax their deep
loads viscously over millions of years, and the stress that a fault actually
experiences is set by local structure, not by an average. The correct use of such
a number is to ask whether the implied stress exceeds the frictional strength
(§[13-01-02 §5](02-rheology-of-earth.md)) — if it does, the plateau cannot be
supported — rather than to report it as an observed stress.

## 7. The force inventory

| force | magnitude (TN m$^{-1}$) | direction |
|---|---|---|
| ridge push | $-4.11$ | away from the ridge |
| slab pull | $+42.04$ | towards the trench |
| basal drag (resistance) | $+46.15$ | opposing plate motion |
| plateau GPE excess (thick crust) | $+7.65$ | extensional within the plateau |

Read the table as a budget, then read it again as a warning. The numbers are
quoted to three significant figures but are uncertain at the tens-of-per-cent
level, because they are integrals of a thermal model, a density contrast and a
viscosity, each of which is itself a model. The rank ordering — slab pull,
then basal drag, then a group containing ridge push and crustal GPE — is robust;
the individual values are not. Reporting a force inventory without a sense of
which inputs dominate the error budget is a common failure in the literature and
an easy one to avoid: perturb each input by a plausible factor and watch which
output changes.

## 8. Assumptions and regime of validity

| assumption | effect if violated |
|---|---|
| local isostasy for each column | long-wavelength support changes the elevation; see [13-01-03 §3](03-lithospheric-strength.md) |
| half-space cooling, no plate model | overestimates subsidence and force at old ages |
| constant $\alpha$, $\rho_m$ | mantle phase changes and compressibility modify the buoyancy |
| slab retains its thermal anomaly | heating removes slab pull with depth (§[13-02-04](../02-mantle-convection/04-subduction-dynamics.md)) |
| Newtonian, uniform-viscosity drag | power-law rheology changes the effective drag by an order of magnitude |
| 2-D force balance | torques, and hence plate rotation, need the full vector balance |
| no trench suction or wedge dynamics | both are first-order in some margins |
| rigid plates | plates deform internally at the MPa level (this lesson's §6) |

The direction of the largest systematic error deserves a sentence. Half-space
cooling keeps thickening forever, so ridge push and the associated subsidence
grow without bound; a plate model with a fixed thickness caps them. The demo's
$4.11\ \mathrm{TN\,m^{-1}}$ at 100 Myr is therefore an overestimate of the
geological force, and the reason the literature's ridge-push estimates cluster
below it is not that the integral is wrong but that the thermal model is
simplified.

## 9. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| thermal subsidence | $s$ | m | $\rho\alpha\Delta T/(\Delta\rho)$ dimensionless $\times\sqrt{\kappa t}$ |
| GPE per unit area | | J m$^{-2}$ = N m$^{-1}$ | force per unit length |
| driving force | $F$ | N m$^{-1}$ | $g\times$(kg m$^{-2}$)$\times$m |
| line-load equivalent | $V_0$ | N m$^{-1}$ | same units as a driving force |
| shear stress | $\tau$ | Pa | $\eta u/d$ |
| plate speed | $u$ | m s$^{-1}$ | $F d/(\eta L)$ |

Convenience conversion used throughout this module:
$1\ \mathrm{TN\,m^{-1}} = 10^{12}\ \mathrm{N\,m^{-1}}$, and
$10^{-9}\ \mathrm{m\,s^{-1}} = 31.557\ \mathrm{mm\,yr^{-1}}$.

## 10. The demonstration

`code/forces_and_stresses_demo.py` prints every number above:

```bash
cd 13-geodynamics-tectonics/01-geodynamic-principles/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python forces_and_stresses_demo.py
```

It computes the half-space cooling subsidence and 600 K depth; the ridge push by
direct double integration and verifies its independence of the compensation
depth; the slab-pull integral with a crude cross-check; the force balance and the
implied plate speed; the GPE of thickened crust against its closed form; and the
force inventory. Fixed seed, print-only, no network, exits 0.

Exercises:
[`exercises/04-forces-and-stresses-exercises.md`](exercises/04-forces-and-stresses-exercises.md)
and
[`exercises/04-forces-and-stresses-solutions.md`](exercises/04-forces-and-stresses-solutions.md).

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC model gives $\rho_m = 3300\ \mathrm{kg\,m^{-3}}$,
> $\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$, $T_m = 1300$ K,
> $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, $\rho_w = 1030\ \mathrm{kg\,m^{-3}}$.
> **(a)** Compute the thermal subsidence at 50 Myr and state how it scales with
> age. **(b)** Explain in two sentences why the ridge-push integral converges
> even though the cooling model has no base. **(c)** A colleague reports a ridge
> push of $4\times10^{14}$ N m$^{-1}$. Give two independent checks that would
> reveal the error, and state in each case what the check would show.
> **(d)** Explain why adding a thicker crust to a plate increases its GPE, and
> what sign of intraplate deviatoric stress that implies.

A worked version appears in the
[solutions](exercises/04-forces-and-stresses-solutions.md).

## Common pitfalls

1. **Choosing the compensation depth carefully.** It does not matter, and
   proving that it does not matter is the principal numerical check on the whole
   calculation.
2. **Integrating only the density anomaly and forgetting the water.** The
   subsided surface must be filled, or the columns are not in isostatic balance
   and the GPE difference drifts with $D$.
3. **Adding slab pull and ridge push with opposite signs.** They act in the same
   direction on a plate.
4. **Treating the implied plate speed as a prediction.** It is a ratio of chosen
   quantities; see §5.2.
5. **Reporting $\Delta\mathrm{GPE}/h$ as a stress.** It is an upper bound on a
   mean.
6. **Comparing forces at different trench lengths per unit length.** All the
   numbers here are per unit trench or ridge length; multiplying by a plate width
   changes the units to N and invites a factor-of-1000 error.
7. **Ignoring that slab pull decays as the slab warms.** A slab that has
   equilibrated thermally has lost its driving force, so slab pull is a function
   of depth.

## Related modules

- [13-01-01 Momentum, Mass and Energy Balances in the Solid Earth](01-momentum-mass-energy.md) —
  the balance laws these forces enter.
- [13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure](03-lithospheric-strength.md) —
  how the same loads are carried.
- [13-02-04 Subduction Dynamics, Slab Geometry and Slab Pull](../02-mantle-convection/04-subduction-dynamics.md) —
  the slab pull computed here as a full dynamical problem.
- [13-03-01 Plate Kinematic Models and Euler Pole Inversion](../03-plate-tectonics-quantitative/01-plate-kinematics-models.md) —
  what the plates actually do with these forces.
- [12-03-03 Thermal Evolution of the Earth and Secular Cooling](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/03-thermal-evolution.md) —
  the same buoyancy sources in the global budget.
