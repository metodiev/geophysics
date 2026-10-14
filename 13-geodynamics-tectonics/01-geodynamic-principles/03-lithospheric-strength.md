---
id: 13-01-03
title: "Lithospheric Strength, Effective Elastic Thickness and Flexure"
level: doctoral
prereqs: ["13-01-02", "04-01-02", "02-04-03"]
tags: [geodynamics, tectonophysics, flexure, effective-elastic-thickness, yield-strength-envelope, isostasy]
---

# Lithospheric Strength, Effective Elastic Thickness and Flexure

> All models and data in this module are **SYNTHETIC**. The loads, the deflection
> profile and the creep laws below are chosen teaching models, and every number
> quoted here is printed by `code/lithospheric_strength_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the flexural rigidity $D$ and the flexural parameter $\alpha$ from
   the plate equation, and **explain** what each controls.
2. **Solve** the line-load deflection of a broken and a continuous plate and
   **verify** the isostatic-area identity that both must satisfy.
3. **Demonstrate** with a measured example that narrow loads are supported by
   flexure while wide loads are compensated locally, and **state** the transition
   criterion in terms of $\alpha$.
4. **Invert** a noisy synthetic deflection profile for $T_e$ and **report** an
   admitted range rather than a point value.
5. **Compute** $T_e$ from a yield strength envelope self-consistently, including
   the neutral-axis condition and the curvature dependence.
6. **Quantify** how $T_e$ responds to the geotherm and **explain** why $T_e$ is a
   thermometer rather than a material property.
7. **Assess** which of two $T_e$ estimates to trust when they disagree, and name
   the assumption that would have to be relaxed.

## Prerequisites

- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](02-rheology-of-earth.md) —
  the flow laws integrated here.
- [04-01-02 Lithosphere, Asthenosphere and the Rheological Definition](../../04-earth-science-geology/01-earth-structure/02-lithosphere-asthenosphere.md) —
  the layer being flexed.
- [02-04-03 Constitutive Laws and Generalised Hooke's Law](../../02-physics/04-elasticity-and-continuum-mechanics/03-constitutive-laws.md) —
  the elastic relations behind $D$.
- [13-01-01 Momentum, Mass and Energy Balances in the Solid Earth](01-momentum-mass-energy.md) —
  the force balance in which flexure sits.

## 1. Intuition: how a load is shared

Put a volcano on a plate. Part of its weight is carried by the buoyancy of the
displaced mantle directly beneath it, and part is carried by the *bending* of the
plate, which spreads the support kilometres to either side. Which mechanism
dominates depends on comparing the load's width with a single length scale
$\alpha$, and $\alpha$ depends on the plate's stiffness through $T_e$, the
**effective elastic thickness**.

Two things make $T_e$ intellectually interesting rather than merely convenient.

First, it is not the thickness of anything. The plate's real strength is
distributed: frictional near the surface, creep-limited below, brittle again in
the mantle if it is cold enough. $T_e$ is the thickness of the *elastic plate
that would bend the same way*, and it is defined by an equivalence of bending
moments, not by a boundary.

Second, the equivalence is a proxy for temperature. Increase the heat flow and
the creep strength collapses at shallower depth, so the layer that can hold
elastic stress thins, so $T_e$ falls. A flexure measurement is therefore a
thermometer, and a weak one: deflection depends on $T_e^{3}$ through $D$, so a
$T_e$ retrieval from a deflection profile is well conditioned, but the map from
$T_e$ to temperature inherits every uncertainty in the flow laws.

## 2. The plate equation and its two scales

### 2.1 The governing equation

For a thin elastic plate of thickness $T_e$ and deflection $w(x)$ resting on a
substrate of density contrast $\Delta\rho$, the vertical force balance is

$$D\frac{\mathrm{d}^{4}w}{\mathrm{d}x^{4}} + \Delta\rho\,g\,w = q(x),$$

$$D = \frac{E\,T_e^{3}}{12(1-\nu^{2})} .$$

Here $q(x)$ is the load per unit area (Pa), $g$ gravity (9.81 m s$^{-2}$,
standard), $E$ Young's modulus and $\nu$ Poisson's ratio. The term
$\Delta\rho g w$ is the buoyancy of the displaced substrate: it is a *restoring*
force, proportional to the deflection, which is why the equation has the
character of a beam on an elastic foundation.

### 2.2 The flexural parameter

Dividing by $\Delta\rho g$ puts the equation in the form

$$\alpha^{4}\frac{\mathrm{d}^{4}w}{\mathrm{d}x^{4}} + w = \frac{q}{\Delta\rho g},
\qquad
\boxed{\;\alpha \equiv \left(\frac{D}{\Delta\rho g}\right)^{1/4}\;}.$$

$\alpha$ has units of length and is the distance over which the bending response
decays: the plate's "reach". With $E = 70$ GPa, $\nu = 0.25$ and
$\Delta\rho = 2300\ \mathrm{kg\,m^{-3}}$ (SYNTHETIC), the demonstration measures

| $T_e$ (km) | $D$ (N m) | $\alpha$ (km) | flexural wavelength $2\pi\alpha$ (km) |
|---|---|---|---|
| 10 | $6.2222\times10^{21}$ | 22.9 | 144.0 |
| 25 | $9.7222\times10^{22}$ | 45.56 | 286.3 |
| 40 | $3.9822\times10^{23}$ | 64.8 | 407.3 |

Note how weak the dependence is: a fourfold change in $T_e$ changes $D$ by a
factor of 64 but $\alpha$ only by a factor of $\sqrt[4]{64} = 2.8$. This is why a
deflection profile constrains $T_e$ far better than it constrains $\alpha$, and
why flexure is a good $T_e$ estimator.

### 2.3 The line-load solution and the isostatic identity

For a line load of strength $V_0$ (N m$^{-1}$) on an infinite continuous plate,
the solution of $\alpha^{4}w'''' + w = 0$ with symmetry at $x = 0$ is

$$w(x) = \frac{V_0\alpha^{3}}{2D}\,e^{-|x|/\alpha}
\left[\cos\!\left(\frac{|x|}{\alpha}\right) +
\sin\!\left(\frac{|x|}{\alpha}\right)\right],$$

a damped oscillation whose first root is at $x = 3\pi\alpha/4$ — the **forebulge**
that surrounds a load. A broken plate (a free hinge at the load) deflects twice as
much at the origin: $w(0) = V_0\alpha^{3}/D$.

The solution has an exact identity worth checking, because it tests the physics
rather than the algebra. Integrating $w$ over the whole plate and using
$\alpha^{4} = D/(\Delta\rho g)$:

$$\int_{-\infty}^{\infty} w(x)\,\mathrm{d}x
= \frac{V_0\alpha^{4}}{D} = \frac{V_0}{\Delta\rho g} .$$

The area under the deflection is the load divided by the substrate's buoyancy
gradient: the plate does not change *how much* material is displaced, only
*where*. That is **isostasy**, recovered as a consequence of the equation rather
than imposed on it. The demonstration verifies it numerically to

$$\left|\int w\,\mathrm{d}x - \frac{V_0}{\Delta\rho g}\right|\bigg/
\frac{V_0}{\Delta\rho g} = 2.09\times10^{-8},$$

which is trapezoidal-integration round-off on a 2 km grid.

### 2.4 Worked example: a 2 km high, 100 km wide load on a $T_e = 25$ km plate

Load cross-section $A = (2000\ \mathrm{m})(10^{5}\ \mathrm{m}) = 2\times10^{8}$
m$^{2}$; with $\rho_{\text{load}} = 2800\ \mathrm{kg\,m^{-3}}$,

$$V_0 = \rho_{\text{load}}gA = (2800)(9.81)(2\times10^{8})
= 5.4936\times10^{12}\ \mathrm{N\,m^{-1}} .$$

With $\alpha = 45.56$ km and $D = 9.7222\times10^{22}$ N m:

$$w(0) = \frac{V_0\alpha^{3}}{2D}
= \frac{(5.4936\times10^{12})(9.457\times10^{13})}{1.9444\times10^{23}}
= 2672\ \mathrm{m},$$

and a broken plate would give 5344 m. The area identity gives
$V_0/(\Delta\rho g) = 2.434783\times10^{8}$ m$^{2}$, matched by the numerical
integral to $2.09\times10^{-8}$ relative.

## 3. Narrow versus wide loads: where Airy meets flexure

The Airy isostatic prediction for a *locally* compensated load of thickness
$h_{\text{load}}$ is

$$w_{\text{Airy}} = \frac{\rho_{\text{load}}\,h_{\text{load}}}{\Delta\rho}
= \frac{(2800)(2000)}{2300} = 2435\ \mathrm{m}.$$

Convolving the measured Green's function with plateau loads of increasing
half-width $a$ (SYNTHETIC, all with the same 2 km thickness):

| $a$ (km) | $w(0)$ (m) | $w(0)/w_{\text{Airy}}$ | area check |
|---|---|---|---|
| 10 | 578 | 0.24 | 1.0000 |
| 25 | 1235 | 0.51 | 1.0000 |
| 50 | 2088 | 0.86 | 1.0000 |
| 100 | 2595 | 1.07 | 1.0000 |
| 300 | 2432 | 1.00 | 1.0000 |

The physics in one line: **the transition is set by $a/\alpha$.** For
$a = 10$ km with $\alpha = 45.6$ km the load is narrow, the plate carries it by
bending, and the deflection is a quarter of what local compensation would give.
At $a = 300$ km the load is wide relative to $\alpha$, the plate bends very
little locally, and Airy's assumption becomes accurate to a per cent. The "area
check" column is the isostatic identity of §2.3, which holds for every load
regardless of width — as it must, because the plate only redistributes, never
changes, the displaced mass.

This is a template for a whole class of geophysical arguments: a *local* model
(Airy) is the correct limit of a *non-local* one (flexure) at long wavelengths,
and the crossover is a dimensionless ratio you can compute before modelling.

## 4. Inverting a deflection profile: the answer is a range

The demonstration generates a synthetic deflection profile for a known load,
$T_{e}^{\text{true}} = 25$ km, adds 5% noise, and grid-searches $T_e$:

| $T_e$ (km) | rms misfit (m) | ratio to minimum |
|---|---|---|
| 5 | 257.2 | 5.46 |
| 10 | 180.0 | 3.82 |
| 15 | 113.7 | 2.41 |
| 20 | 67.4 | 1.43 |
| 25 | 47.1 | 1.00 |
| 30 | 60.5 | 1.28 |
| 40 | 129.2 | 2.74 |
| 60 | 275.1 | 5.84 |

The best fit is $T_e = 25$ km, recovering the true value exactly, and the
admitted set at 1.5× the minimum misfit is **20–31 km**. Two comments:

- The misfit function is asymmetric: it rises faster towards small $T_e$ than
  towards large $T_e$. A symmetric error bar on $T_e$ is therefore a modelling
  choice, not a property of the data.
- The recovery is clean *because the load is known*. In nature the load is the
  dominant uncertainty, and an error in the load amplitude biases $T_e$ almost
  one-for-one in $D$ (and hence as the cube root in $T_e$). Reporting $T_e$
  without the load model is reporting a partial calculation.

## 5. $T_e$ from a yield strength envelope

The physically motivated way to get $T_e$ is to build the strength envelope of
[13-01-02 §5](02-rheology-of-earth.md) and ask what bending moment it can carry.

**Construction.** For a plate bent with curvature $\kappa$, the fibre stress at
depth $z$ is $\sigma(z) = -E\kappa(z - z_n)$, capped by the yield strength
$\sigma_y(z)$:

$$\sigma(z) = \mathrm{clamp}\!\left(-E\kappa(z-z_n),\;-\sigma_y(z),\;
+\sigma_y(z)\right).$$

The **neutral depth** $z_n$ is not the mid-plane; it is fixed by the condition of
zero net axial force,

$$\int \sigma(z)\,\mathrm{d}z = 0 ,$$

which is why yielding on one side of the plate shifts the neutral axis towards
the elastic remainder. The bending moment follows,

$$M = \int \sigma(z)\,(z - z_n)\,\mathrm{d}z ,$$

and $T_e$ is defined by matching that moment to the elastic plate that would
produce it:

$$M = \frac{E\kappa T_e^{3}}{12(1-\nu^{2})}
\;\;\Longrightarrow\;\;
T_e = \left[\frac{12(1-\nu^{2})|M|}{E\kappa}\right]^{1/3} .$$

**Measured** with the SYNTHETIC envelope (maximum yield strength 589 MPa at
$z = 38.5$ km):

| $\kappa$ (m$^{-1}$) | neutral depth (km) | $T_e$ (km) | $M$ (N) |
|---|---|---|---|
| $10^{-8}$ | 49.4 | 83.8 | $-3.6614\times10^{16}$ |
| $10^{-7}$ | 44.5 | 49.5 | $-7.5637\times10^{16}$ |
| $10^{-6}$ | 42.1 | 24.4 | $-9.0220\times10^{16}$ |

Read the table as a warning and a result at once. The *result* is that a strength
envelope yields a definite $T_e$ once you specify the curvature; the *warning* is
that $T_e$ depends on the curvature by a factor of three across the range
tested, because a more tightly bent plate yields more of its envelope and loses
moment. There is no such thing as "the $T_e$ of this lithosphere" without a
loading amplitude. In practice the bending moment is nearly saturated at high
curvature, and $M$ changes by only a factor of 1.2 between $\kappa = 10^{-7}$ and
$10^{-6}$ while $T_e$ halves — the elastic equivalence is a poor bookkeeping
device for a plastic plate.

## 6. $T_e$ as a thermometer

Recomputing the envelope and $T_e$ at $\kappa = 10^{-7}$ m$^{-1}$ for three
geotherms:

| geotherm (K/km) | $T_e$ (km) | neutral depth (km) |
|---|---|---|
| cold 10/6 (crust/mantle) | 104.8 | 74.3 |
| reference 20/12 | 49.5 | 44.5 |
| hot 30/18 | 30.6 | 13.6 |

The cold end is not physical as an *elastic* thickness — 105 km of elastic
lithosphere is more than the thermal boundary layer — but that is the point: the
envelope calculation says the material is strong enough to carry the moment, and
the discrepancy with thermal arguments is exactly what the literature argues
about. The hot end, 30.6 km, is the right order for a young or rifted region.

Because $D\propto T_e^{3}$ and $\alpha \propto T_e^{3/4}$, a $T_e$ difference of a
factor of three between cold and hot lithosphere is a $D$ difference of a factor
of 27 and an $\alpha$ difference of a factor of 5.2. Flexure is therefore a
sensitive thermometer of the *strength* of the lithosphere even when it is only a
mediocre thermometer of its temperature.

## 7. Assumptions and regime of validity

| assumption | where it fails |
|---|---|
| thin elastic plate | deflections comparable to $T_e$; short wavelengths |
| deflection $\ll$ load thickness | large loads, deep basins (small-deflection theory) |
| $T_e$ constant in space and time | real plates have inherited weak zones |
| 2-D (line) loads | isolated seamounts need the axisymmetric solution |
| no in-plane forces | compression or tension changes the effective stiffness |
| known load | the dominant real uncertainty |
| single elastic layer | a decoupled upper crust and mantle give a bimodal response |
| Airy compensation at depth | narrow loads, as measured in §3 |

A remark on the small-deflection assumption, because it is quantitative rather
than qualitative. The plate equation keeps $w$ linear in $q$ only while slopes
stay small: $\max|\mathrm{d}w/\mathrm{d}x|\ll1$. The solutions above have slopes
of order $w_0/\alpha$; for $w_0 = 2.7$ km and $\alpha = 45.6$ km that is 0.06, so
the linear theory is comfortable. A 10 km deflection on the same plate would not
be.

## 8. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| flexural rigidity | $D$ | N m | Pa $\times$ m$^{3}$ |
| flexural parameter | $\alpha$ | m | $(D/\Delta\rho g)^{1/4}$: (N m / (N m$^{-3}$))$^{1/4}$ |
| line load | $V_0$ | N m$^{-1}$ | $\rho g \times$ area |
| deflection | $w$ | m | $V_0\alpha^{3}/D$ |
| curvature | $\kappa$ | m$^{-1}$ | |
| bending moment | $M$ | N | N m $\times$ m$^{-1}$ ... N m m$^{-1}$ = N |

The check on $M$ is the one that catches errors: the *moment per unit length*
of a plate has units of N (equivalently N m m$^{-1}$), while $D\kappa$ has units
of N m $\times$ m$^{-1}$ = N. Consistent.

## 9. The demonstration

`code/lithospheric_strength_demo.py` prints every number above:

```bash
cd 13-geodynamics-tectonics/01-geodynamic-principles/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python lithospheric_strength_demo.py
```

It tabulates $D$ and $\alpha$; verifies the isostatic-area identity; convolves
the Green's function with loads of five widths; inverts a noisy synthetic
deflection for $T_e$ with an admitted range; and computes $T_e$ from the yield
strength envelope with a self-consistent neutral axis, for three curvatures and
three geotherms. Fixed seed, print-only, no network, exits 0.

Exercises:
[`exercises/03-lithospheric-strength-exercises.md`](exercises/03-lithospheric-strength-exercises.md)
and
[`exercises/03-lithospheric-strength-solutions.md`](exercises/03-lithospheric-strength-solutions.md).

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC oceanic plate has $E = 70$ GPa, $\nu = 0.25$, and is loaded by a
> 3 km high, 200 km wide ridge of density $2800\ \mathrm{kg\,m^{-3}}$
> ($\Delta\rho = 2300\ \mathrm{kg\,m^{-3}}$).
> **(a)** Compute $D$ and $\alpha$ for $T_e = 20$ km. **(b)** Compute $V_0$ and
> the continuous-plate deflection at the load. **(c)** Compute the Airy
> compensation depth and say, with a number, whether the load is "narrow" or
> "wide". **(d)** The measured deflection is 30% larger than your answer to (b).
> Give two adjustments to the model that could explain it and state which single
> additional measurement would discriminate between them.

A worked version appears in the
[solutions](exercises/03-lithospheric-strength-solutions.md).

## Common pitfalls

1. **Reading $\alpha$ as a wavelength.** The flexural *wavelength* is
   $2\pi\alpha$; $\alpha$ itself is the decay length. Mixing them puts $T_e$ out
   by a factor of about 2.5.
2. **Using the load's density instead of the density contrast.** For a
   subaerial load on ocean floor the infill is water, so
   $\Delta\rho = \rho_m - \rho_w$, not $\rho_m$.
3. **Quoting $T_e$ to three significant figures.** The admitted range in §4 is
   20–31 km; report the range.
4. **Ignoring the load.** With a free amplitude the fit is degenerate: $T_e$ and
   the load trade off.
5. **Assuming $T_e$ is a physical layer thickness.** It is a bending-moment
   equivalence (§5) and it depends on curvature.
6. **Comparing $T_e$ from flexure with $T_e$ from a strength envelope without
   matching the curvature and the geotherm.**
7. **Forgetting that bending produces a forebulge.** The first zero of $w$ is at
   $x = 3\pi\alpha/4$; a nearby region of *uplift* is a prediction, not noise.

## Related modules

- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](02-rheology-of-earth.md) —
  the envelope integrated here.
- [13-01-04 Driving Forces, Stress Fields and Intraplate Stress](04-forces-and-stresses.md) —
  the loads and their isostatic consequences.
- [13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength](../06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md) —
  the applied modelling counterpart.
- [07-03-01 Gravity Anomalies and Their Interpretation](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/01-anomaly-interpretation.md) —
  the anomaly signature of the same loads.
- [18-03-01 Regularization and the Resolution Matrix](../../18-inverse-problems/03-regularization/01-why-regularize.md) —
  the trade-offs the $T_e$ inversion exemplifies.
