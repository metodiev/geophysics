---
id: 13-06-03
title: "Glacial Isostatic Adjustment: Ice, Viscosity and Sea Level"
level: research
prereqs: ["13-01-02", "13-06-01", "07-04-02"]
tags: [geodynamics, tectonophysics, glacial-isostatic-adjustment, viscosity, sea-level, viscoelasticity]
---

# Glacial Isostatic Adjustment: Ice, Viscosity and Sea Level

> **All models and data in this module are SYNTHETIC.** The ice history below is
> a chosen two-step teaching history, not a reconstruction, and the viscosity is
> a uniform half-space value. Every number is printed by
> [`code/glacial_isostatic_adjustment_demo.py`](code/glacial_isostatic_adjustment_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the relaxation of a harmonic surface deflection on a viscous
   half-space and obtain $\tau = 2\eta/(\rho g k) = 4\pi\eta/(\rho g\lambda)$.
2. **Check** the derivation by evaluating the two boundary conditions and the
   biharmonic equation directly and reporting the residuals.
3. **Compute** relaxation times over a range of viscosity and wavelength and
   **explain** the two-observable structure of a viscosity inversion.
4. **Integrate** a synthetic ice history with a relaxation model and **compute**
   the present-day uplift rate.
5. **Explain** why the present-day rate is non-monotonic in viscosity, and use
   that to show that a single uplift rate constrains neither viscosity nor ice
   thickness.
6. **Decompose** relative sea level into a eustatic term and a local
   solid-surface term, and **quantify** which dominates near a former ice sheet.
7. **State** which additional observable breaks the (viscosity, ice) trade-off.

## Prerequisites

- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](../01-geodynamic-principles/02-rheology-of-earth.md) —
  what a viscosity of $10^{21}$ Pa s means physically.
- [13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength](01-isostasy-flexure-modelling.md) —
  the elastic limit, of which this is the viscous counterpart.
- [07-04-02 Height Systems and Their Reference Surfaces](../../07-gravity-geodesy/04-geodesy-reference-frames/02-height-systems.md) —
  the reference surfaces against which relative sea level is measured.
- [13-03-04 Basin Formation and Subsidence Modelling](../03-plate-tectonics-quantitative/04-basin-geodynamics.md) —
  the same relaxation physics applied to sedimentary basins.

## 1. The relaxation of a harmonic load

Remove a load from a viscous half-space and the surface rises towards its
pre-load position. The rate is set by how fast the mantle can flow, and the
length scale over which the flow must organised is the load's wavelength. For a
deflection $w(x,t) = w_0(t)\cos kx$ on a half-space of viscosity $\eta$ and
density $\rho$, the horizontal flow is confined to a depth of order $1/k$, the
driving stress is the buoyancy of the deflection $\rho g w_0$ and the strain rate
it produces is of order $k\,(w_0/\tau)$, which balances the viscous stress
$\eta k (w_0/\tau)$ against $\rho g w_0$. The bookkeeping gives

$$\frac{\mathrm{d}w_0}{\mathrm{d}t} = -\frac{\rho g k}{2\eta}\,w_0,
\qquad
\tau = \frac{2\eta}{\rho g k} = \frac{4\pi\eta}{\rho g\lambda}.$$

Two minus signs are easy to lose, and both matter. The deflection *decays*, and
a raised surface *subsides*, which is the opposite of the naive reading of
"buoyancy". The factor $2$ comes from the normal-traction boundary condition and
is the part of the algebra most worth checking.

## 2. Checking the algebra instead of asserting it

Write the decaying solution of the biharmonic equation
$(\partial_z^2-k^2)^2\varphi = 0$ as $\varphi(z) = (A+Bz)e^{kz}$, with
$u = \varphi'(z)e^{ikx}$, $w = -ik\varphi(z)e^{ikx}$. The two surface conditions
are zero shear traction and a normal traction equal to minus the buoyancy of the
deflection, $\sigma_{zz}(0) = -\rho g w_0$.

The demonstration evaluates them numerically:

| quantity | measured |
|---|---|
| $B + kA$ (shear condition) | $0.000\times10^{0}$ |
| residual of $(\partial_z^2-k^2)^2\varphi$ at three depths | $4.963\times10^{-8}$ |
| implied $\tau$ from $w(0)/w_0$ at $\eta = 10^{21}$ Pa s, $\lambda = 200$ km | 61503.7 yr |
| $\tau$ from $4\pi\eta/(\rho g\lambda)$ | 61503.7 yr |

The last two agree because they evaluate the same algebra twice. That is the
honest limitation of this check: a residual test catches implementation errors
and sign slips (the $4.963\times10^{-8}$ is the finite-difference truncation in
the fourth derivative, not a physical discrepancy), but it cannot confirm that
the assumed boundary conditions describe the Earth. Verification and validation
are different, and this section is verification.

## 3. Relaxation times, measured

With $\rho = 3300\ \mathrm{kg\,m^{-3}}$ (a chosen value) and $\lambda$ the load
wavelength:

| $\eta$ (Pa s) | $\tau$ at 1000 km (yr) | $\tau$ at 3000 km (yr) | $\tau$ at 10000 km (yr) |
|---|---|---|---|
| $10^{19}$ | 123 | 41 | 12 |
| $10^{20}$ | 1230 | 410 | 123 |
| $10^{21}$ | 12301 | 4100 | 1230 |
| $10^{22}$ | 123007 | 41002 | 12301 |

Two structural facts. First, $\tau$ is *proportional to viscosity and inversely
proportional to wavelength*: short-wavelength loads relax fast. Second, and
consequently, an observation made at two wavelengths gives two constraints
rather than one, which is the entire basis of viscosity-profile inversions. One
wavelength gives a combination of viscosity and the ice history, and nothing
more.

## 4. A synthetic ice history and the present-day uplift

The model is integrated as

$$\frac{\mathrm{d}w}{\mathrm{d}t} = \frac{w_{\text{eq}}(t) - w}{\tau},
\qquad w_{\text{eq}} = \frac{\rho_i}{\rho_m}h_i(t),
\qquad \tau = \frac{4\pi\eta}{\rho_m g\lambda},$$

with $\rho_i = 917\ \mathrm{kg\,m^{-3}}$ (the standard density of ice),
$\rho_m = 3300\ \mathrm{kg\,m^{-3}}$ and a chosen history: 2 km of ice grows
linearly from $-30$ ka to $-20$ ka, is held until $-12$ ka, and is removed
linearly by $-10$ ka. The equilibrium deflection of the full load is
$w_{\text{eq}} = 555.8$ m.

For $\lambda = 3000$ km:

| $\eta$ (Pa s) | $\tau$ (yr) | deflection now (m) | uplift now (mm/yr) |
|---|---|---|---|
| $1.0\times10^{20}$ | 410 | 0.0 | 0.000 |
| $3.0\times10^{20}$ | 1230 | 0.1 | 0.057 |
| $1.0\times10^{21}$ | 4100 | 36.2 | 8.944 |
| $3.0\times10^{21}$ | 12301 | 152.6 | 12.453 |
| $1.0\times10^{22}$ | 41002 | 122.3 | 2.986 |
| $3.0\times10^{22}$ | 123007 | 54.6 | 0.444 |

and at $\eta = 10^{21}$ Pa s for several wavelengths:

| $\lambda$ (km) | 1000 | 2000 | 3000 | 6000 |
|---|---|---|---|---|
| $\tau$ (yr) | 12301 | 6150 | 4100 | 2050 |
| uplift now (mm/yr) | 12.453 | 13.475 | 8.944 | 1.263 |

The present-day rate is the leftover deflection divided by the relaxation time,
and *both* factors depend on the parameters in opposite directions: a low
viscosity leaves a small deflection, and a high viscosity leaves a large one that
decays slowly. The result is a maximum at an intermediate value — here
$\eta \approx 3\times10^{21}$ Pa s at $\lambda = 3000$ km, and
$\lambda \approx 2000$ km at $\eta = 10^{21}$ Pa s. This non-monotonicity is why a
single uplift rate is a poor constraint on viscosity, and it is a robust
prediction of the physics, not a numerical artefact: the demonstration recovers it
in both the viscosity and the wavelength scan.

## 5. Relative sea level at two sites

Relative sea level at a site is the eustatic change minus the local
solid-surface displacement. With the ice sheet taken as $10^{6}$ km² in area and
the ocean area as $0.71$ of the sphere ($4\pi R_\oplus^2$ with
$R_\oplus = 6371$ km, giving $3.6215\times10^{14}$ m²), the eustatic term is a few
metres. Measured at $\eta = 10^{21}$ Pa s, $\lambda = 3000$ km:

| $t$ (ka) | $h_{\text{ice}}$ (m) | eustatic (m) | deflection at the centre (m) | relative sea level (m) |
|---|---|---|---|---|
| $-30$ | 0 | $-0.00$ | 0.0 | $-0.0$ |
| $-20$ | 2000 | $-0.01$ | 348.7 | $-348.7$ |
| $-12$ | 2000 | $-0.01$ | 526.7 | $-526.7$ |
| $-10$ | 0 | $0.00$ | 421.4 | $-421.4$ |
| $-5$ | 0 | $-0.00$ | 123.6 | $-123.6$ |
| $0$ | 0 | $-0.00$ | 36.2 | $-36.2$ |

At a flank site where $\cos kx = 0.5$ the deflection is half, and the present
relative sea-level rate is $-4.472$ mm/yr against $-8.944$ mm/yr at the centre.
The eustatic term never exceeds a few centimetres for this ice area, so the
record is dominated by the local deflection.

The lesson is blunt: **near a former ice sheet a sea-level record is not a proxy
for global ice volume**, and two sites on the same coastline record different
histories of the same global ice volume. A relative sea-level curve can only be
inverted for ice volume with the solid-Earth response modelled, which is why
relative sea level is an *output* of glacial-isostatic-adjustment models rather
than an input. The peripheral (far-field) case, where the deflection can be
opposite in sign, requires a full spherical model with load geometry; what the
local model shows is the mechanism and its dominance.

## 6. Worked example: one uplift rate, many models

*Problem.* An observation gives a present-day uplift rate of 10.0 mm/yr. What
does it constrain?

1. For each trial viscosity, find the ice-sheet scale factor (relative to the
   2 km history of Section 4) that reproduces 10.0 mm/yr. That is a
   one-dimensional root find per viscosity; the demonstration bisects:

| $\eta$ (Pa s) | $\tau$ (yr) | required scale | peak ice (km) |
|---|---|---|---|
| $1.0\times10^{20}$ | 410 | (not reachable) | — |
| $3.0\times10^{20}$ | 1230 | (not reachable) | — |
| $6.0\times10^{20}$ | 2460 | 3.985 | 7.97 |
| $1.0\times10^{21}$ | 4100 | 1.122 | 2.24 |
| $2.0\times10^{21}$ | 8200 | 0.693 | 1.39 |
| $5.0\times10^{21}$ | 20501 | 1.280 | 2.56 |
| $1.0\times10^{22}$ | 41002 | 3.344 | 6.69 |

2. Read the table. A factor of ten in viscosity — from $10^{21}$ to $10^{22}$ Pa s
   — is compensated by a factor of about three in ice thickness, and the required
   thickness has a *minimum* near $2\times10^{21}$ Pa s: two mechanisms fit the
   same uplift rate, a thinner ice sheet on a lower-viscosity mantle or a thicker
   one on a higher-viscosity mantle.

*Answer.* The uplift rate constrains a combination, not a parameter, with two
branches. What breaks the ambiguity is a second observable whose wavelength
dependence differs from the uplift's: the present-day gravity field, the geoid, or
the sea-level history at several sites. It is *not* broken by measuring the same
uplift rate more accurately, because the trade-off is between the parameters and
not between the noise. Below about $10^{21}$ Pa s the target rate is unreachable
with a plausible load, which is a genuine exclusion rather than a degeneracy.

## 7. Assumptions and regime of validity

1. **A uniform-viscosity viscous half-space, no elastic layer.** Real glacial
   isostatic adjustment has a lithosphere, a viscosity increase with depth and
   transient (power-law) rheology; the single-layer model is the reference
   against which those are measured.
2. **The relaxation time is derived for a harmonic load.** A general load is a
   sum of harmonics with different $\tau$; a disc-shaped ice sheet relaxes with a
   mixture of timescales, which is why the response to a step load is not a
   single exponential.
3. **The ice history is prescribed, not inferred.** The trade-off of Section 6
   exists precisely because the history is a second unknown.
4. **Airy-like local equilibrium, $\rho_i/\rho_m$.** The real equilibrium
   involves the water load, the ocean geometry and the self-gravitation of the
   ice and water loads; each changes the long-wavelength response.
5. **Rotation, sea-level and geoid feedbacks are omitted.** A full model solves
   the sea-level equation; here the ocean is a fixed area.
6. **The eustatic term uses a fixed ocean area and a single ice sheet.** Both are
   approximations, and the second is severe for a real ice history.

## Mastery checkpoint

Without notes:

1. Derive $\tau = 4\pi\eta/(\rho g\lambda)$ from the decay of a harmonic
   deflection, stating each physical argument used.
2. Compute $\tau$ for $\eta = 5\times10^{20}$ Pa s at $\lambda = 2500$ km, with
   $g = 9.81$ m/s² and $\rho = 3300\ \mathrm{kg\,m^{-3}}$.
3. Explain why the present-day uplift rate is largest at an intermediate
   viscosity, in two sentences and with the two competing factors named.
4. For a 2 km ice load over $10^{6}$ km², compute the eustatic sea-level change
   with the ocean area given above, and compare it with the isostatic deflection.
5. State which additional observation would discriminate between the two
   branches of the trade-off in Section 6, and why the wavelength dependence is
   the key property.
6. Name two physical processes omitted by the model that would change the
   interpretation of a measured present-day uplift rate.

## Common pitfalls

1. **Sign error in the relaxation.** The deflection decays and a raised surface
   subsides; a model with the opposite sign produces uplift while the ice is
   *growing*.
2. **Reading a viscosity off a single uplift rate.** The measured trade-off spans
   a factor of ten in viscosity and a factor of three in ice thickness.
3. **Assuming the eustatic term dominates relative sea level near an ice sheet.**
   Measured: a few centimetres against hundreds of metres.
4. **Comparing a modelled relaxation time with a reconstruction without
   matching the wavelength.** $\tau$ scales as $1/\lambda$.
5. **Treating a single-exponential response as general.** It is a
   single-harmonic property.
6. **Expecting that better data on the same observable will resolve the
   trade-off.** It is a parameter degeneracy, not a noise limit.

## Related modules

- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](../01-geodynamic-principles/02-rheology-of-earth.md) —
  the constitutive behaviour this model assumes.
- [13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength](01-isostasy-flexure-modelling.md) —
  the elastic limit of the same problem.
- [13-06-02 Volcano Deformation, Magma Chamber Models and InSAR](02-volcano-geodesy.md) —
  a different load, the same half-space and the same trade-off structure.
- [12-03 Geotherms and the Earth's Heat Budget](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/README.md) —
  what sets the viscosity that this lesson infers.
- [15-06 Sea Level Change and the Marine Record](../../15-oceanography-marine/06-sea-level-change-marine/README.md) —
  where relative sea-level records are used.

Companion exercises:
[`exercises/03-glacial-isostatic-adjustment-exercises.md`](exercises/03-glacial-isostatic-adjustment-exercises.md)
and
[`exercises/03-glacial-isostatic-adjustment-solutions.md`](exercises/03-glacial-isostatic-adjustment-solutions.md).
Run the demonstration with

```bash
cd 13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python glacial_isostatic_adjustment_demo.py
```
