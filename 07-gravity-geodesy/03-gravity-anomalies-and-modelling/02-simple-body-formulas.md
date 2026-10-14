---
id: 07-03-02
title: "Analytical Formulas for Sphere, Cylinder, Sheet and Dyke"
level: graduate
prereqs: ["07-03-01", "07-01-02"]
tags: [gravity, geodesy, forward-modelling, analytical-formulas, dyke]
---

# Analytical Formulas for Sphere, Cylinder, Sheet and Dyke

All models and data in this module are SYNTHETIC. The bodies, densities and
profiles used below are chosen teaching shapes and values.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the vertical-gravity field of a point mass, a line mass and an
   infinite sheet from the volume integral of the Newtonian kernel.
2. **Derive** the anomaly of a semi-infinite sheet (the fault step) by
   integrating the thin-sheet kernel over depth.
3. **Derive** the closed form for a 2-D rectangle of arbitrary cross-section and
   **verify** it against a numerical double integral.
4. **Evaluate** the limits in which the rectangle becomes a slab or a
   semi-infinite sheet, and the sphere becomes a point mass.
5. **Apply** the correct depth rule for each geometry, including the derivative
   rule for the step model.
6. **Quantify** the sensitivity of the anomaly to each parameter and explain why
   width, not amplitude, carries the depth information.
7. **State** when a 2-D formula may replace a 3-D calculation, and the error in
   doing so.

## Prerequisites

- [01 Interpreting Anomalies: Geometry, Depth and Amplitude Rules](01-anomaly-interpretation.md) —
  the rules of thumb these formulas justify.
- [07-01-02 Gravitational Potential, Equipotentials and the Geoid](../01-gravity-fundamentals/02-gravity-potential.md) —
  the potential and the field it generates.

## 1. Why closed forms still matter

Every inversion, every grid-based forward model and every interpretation code
eventually calls a closed form or its discrete equivalent. A closed form is a
formula you can differentiate, differentiate twice, integrate and check at a
limit; it is also the only kind of forward model whose error you can bound
exactly. This lesson builds the four workhorses — sphere, cylinder, sheet and
rectangle — from one integral, and verifies each against an independent
quadrature.

The unifying statement is that all of them are the same integral with different
limits:

$$
g_z(P) = G\iiint_{V} \Delta\rho
\frac{z'}{\left[(x-x')^{2}+(y-y')^{2}+z'^{2}\right]^{3/2}}\,\mathrm{d}x'\mathrm{d}y'\mathrm{d}z',
$$

where the observation point is at the origin of the horizontal coordinates, $z'$
is depth below it, and the vertical component of the attraction is the only
component a gravimeter measures.

## 2. From the integral to the four formulas

### 2.1 Point mass and sphere

For a point mass $M$ at depth $z$ the integral collapses to a single term:

$$g_z = \frac{G M z}{r^{3}}, \qquad r^{2} = x^{2}+y^{2}+z^{2},$$

and by the shell theorem a homogeneous sphere of density contrast $\Delta\rho$ is
exactly a point mass $M = \tfrac{4}{3}\pi R^{3}\Delta\rho$ for every external
point. Its half-width rule, $z = 1.3048\,x_{1/2}$, was derived in
[01](01-anomaly-interpretation.md).

### 2.2 Line mass and 2-D cylinder

Integrating along an infinite strike replaces the volume integral by an area
integral with a factor 2:

$$g_z(x) = 2G\Delta\rho\iint_{A}\frac{z'}{(x-x')^{2}+z'^{2}}\,\mathrm{d}x'\mathrm{d}z'.$$

For a line mass $\lambda$ (a point in cross-section) this gives
$g_z = 2G\lambda z/(x^{2}+z^{2})$ and $g_{z,\max} = 2G\lambda/z$, and for a
circular cylinder $\lambda = \pi R^{2}\Delta\rho$. **The factor of two is the
whole difference between 2-D and 3-D gravity**, and forgetting it is a factor-2
error that survives every check except a dimensional or limit test.

### 2.3 Infinite sheet (Bouguer slab)

For an infinite horizontal sheet of thickness $t$ the integral is elementary and
gives the famous result

$$g_z = 2\pi G \Delta\rho\, t,$$

independent of depth and of the observation point. The demonstration prints
$2.5162\ \mathrm{mGal}$ for $\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$ and
$t = 200\ \mathrm{m}$ at every station on the profile. This is why the slab term
in the Bouguer reduction is a constant, and why it is the term that must be
removed before any shape is interpretable.

### 2.4 Semi-infinite sheet: the fault step

Let the sheet fill $x > 0$ with top at depth $z_1$ and bottom at $z_2$. The
kernel of a surface element at depth $z$ is
$\mathrm{d}g = 2G\Delta\rho\left(\tfrac{\pi}{2} + \arctan\frac{x}{z}\right)\mathrm{d}z$
(a standard half-plane result), so

$$
g_z(x) = 2G\Delta\rho\left[
\frac{\pi}{2}(z_2-z_1) + z_2\arctan\frac{x}{z_2} - z_1\arctan\frac{x}{z_1}
+ \frac{x}{2}\ln\frac{x^{2}+z_2^{2}}{x^{2}+z_1^{2}}
\right].
$$

Three properties make this formula worth memorising:

- $g_z(\pm\infty)$ gives $0$ and the full slab $2\pi G\Delta\rho t$;
- $g_z(0) = \pi G\Delta\rho t$, exactly half the slab, **whatever the thickness**;
- the horizontal derivative peaks at $x = 0$ with
  $\left(\mathrm{d}g_z/\mathrm{d}x\right)_{\max} = 2G\Delta\rho\ln(z_2/z_1)$.

The demonstration verifies the first property against the rectangle formula to
$4.8\times10^{-10}\ \mathrm{m\,s^{-2}}$, and uses the third to invert for the top
depth: from the measured $\left(\mathrm{d}g/\mathrm{d}x\right)_{\max}$ it recovers
$\ln(z_2/z_1) = 0.33647$ and, with the thickness known,
$z_1 = t/[\exp(0.33647)-1] = 500.0\ \mathrm{m}$ against a true $500.0\ \mathrm{m}$.

### 2.5 The 2-D rectangle (a dyke of finite depth extent)

Integrating the 2-D kernel over $x'\in[x_1,x_2]$, $z'\in[z_1,z_2]$ is
elementary but tedious. With the antiderivative
$P(u,a) = u\ln(u^{2}+a^{2}) - 2u + 2a\arctan(u/a)$, whose derivative is
$\ln(u^{2}+a^{2})$, define

$$J(u) = \tfrac{1}{2}\left[P(u,z_2) - P(u,z_1)\right],
\qquad
g_z(x) = 2G\Delta\rho\left[J(x-x_1) - J(x-x_2)\right].$$

The demonstration checks this closed form against a Gauss-Legendre double
integral of the defining integral at four offsets, for two different
rectangles, and finds differences of $10^{-20}$ to $10^{-18}\
\mathrm{m\,s^{-2}}$ — round-off, not quadrature error, because an
$n$-point Gauss rule on a smooth integrand is exact to machine precision here.

*Numerical example.* A rectangle $500\ \mathrm{m}$ wide, from $300\ \mathrm{m}$ to
$2000\ \mathrm{m}$ depth, with $\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$, gives
$3.6088\ \mathrm{mGal}$ directly above its centre, and the closed form and the
quadrature agree to $10^{-18}\ \mathrm{m\,s^{-2}}$. Widening the rectangle to
$2\ \mathrm{km}$ and thinning it to $200\ \mathrm{m}$ at $500\!-\!700\
\mathrm{m}$ depth gives $2.51519\ \mathrm{mGal}$, which is $99.96\%$ of the
infinite-slab value $2.51615\ \mathrm{mGal}$: the slab limit is reached quickly
once the width exceeds a few times the depth.

## 3. Worked numeric example

Take $\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$, $G = 6.67430\times10^{-11}\
\mathrm{m^{3}kg^{-1}s^{-2}}$, and compare the four bodies on one profile. Peak
values from the demonstration, converted with $1\ \mathrm{mGal} = 10^{-5}\
\mathrm{m\,s^{-2}}$:

| body | geometry | peak (mGal) |
|---|---|---|
| sphere | $R = 500\ \mathrm{m}$, $z = 1000\ \mathrm{m}$ | 1.0484 |
| cylinder | $R = 200\ \mathrm{m}$, $z = 500\ \mathrm{m}$ | 1.0065 |
| infinite sheet | $t = 200\ \mathrm{m}$ | 2.5162 (at every $x$) |
| semi-infinite sheet | $t = 200\ \mathrm{m}$, top $500\ \mathrm{m}$ | 1.2581 (at the edge) |
| rectangle (dyke) | $500\ \mathrm{m} \times 1700\ \mathrm{m}$, top $300\ \mathrm{m}$ | 3.6088 |

Check the slab by hand:
$2\pi G\Delta\rho t = 2\pi(6.67430\times10^{-11})(300)(200) = 2.51615\times10^{-5}
\ \mathrm{m\,s^{-2}} = 2.5162\ \mathrm{mGal}$. ✔

Check the semi-infinite sheet: it must be exactly half the slab at $x = 0$, and
$1.25808\ \mathrm{mGal}$ is exactly $2.51615/2$. ✔

## 4. Summary of the five formulas

| body | geometry | $g_z$ | limits and notes |
|---|---|---|---|
| point mass / sphere | mass $M$ at depth $z$ | $GMz/r^{3}$ | exact outside the sphere; $g_{\max}=GM/z^{2}$ |
| line mass / cylinder | $\lambda=\pi R^{2}\Delta\rho$ at depth $z$ | $2G\lambda z/(x^{2}+z^{2})$ | per unit strike; $g_{\max}=2G\lambda/z$ |
| infinite sheet | thickness $t$ | $2\pi G\Delta\rho t$ | independent of $z$ and of position |
| semi-infinite sheet | top $z_1$, bottom $z_2$, edge at $x=0$ | $2G\Delta\rho[\tfrac{\pi}{2}t + z_2\arctan(x/z_2) - z_1\arctan(x/z_1) + \tfrac{x}{2}\ln\tfrac{x^{2}+z_2^{2}}{x^{2}+z_1^{2}}]$ | $\tfrac{1}{2}$ slab at $x=0$; derivative rule $2G\Delta\rho\ln(z_2/z_1)$ |
| 2-D rectangle (dyke) | $x\in[x_1,x_2]$, $z\in[z_1,z_2]$ | $2G\Delta\rho[J(x-x_1)-J(x-x_2)]$, $J(u)=\tfrac{1}{2}[P(u,z_2)-P(u,z_1)]$ | contains the slab and the step as limits; needs a grading test |

Every row except the sheet carries a *depth* signature: an amplitude that depends
on $z$ and a width that scales with $z$. The sheet is the one body with no depth
information at all, which is exactly why the Bouguer slab term has to be removed
before a shape can be interpreted, and why the removal leaves the residual
sensitive to whatever the slab model got wrong.

## 5. Limits and their use as tests

1. **Rectangle → infinite slab.** Widen the rectangle; the demonstration's
   $2\ \mathrm{km}$-wide, $200\ \mathrm{m}$-thick rectangle reaches
   $0.999618$ of the slab value.
2. **Rectangle → semi-infinite sheet.** Push one side to $+\infty$; the closed
   form matches the semi-infinite formula at the edge, at $-3\ \mathrm{km}$ and
   at $+3\ \mathrm{km}$, to $4.8\times10^{-10}\ \mathrm{m\,s^{-2}}$.
3. **Sphere → point mass.** At $100\ \mathrm{km}$ the demonstration's sphere and
   its equivalent point mass agree to six decimals
   ($1.05\times10^{-4}\ \mathrm{mGal}$ both).
4. **3-D prism → 2-D formula.** A rectangular prism of long strike must approach
   the 2-D rectangle value; this test is performed in
   [03](03-forward-modelling-2d3d.md), where the ratio moves from $0.899$ at a
   $2\ \mathrm{km}$ strike length to $1.00000$ at $2000\ \mathrm{km}$.

Every one of these limits is a *verification*, not a validation: it proves the
formula is internally right, not that the body is the Earth.

## 6. Sensitivity

The demonstration perturbs each parameter of the cylinder by $1\%$ and records
the change in the on-axis anomaly:

| parameter perturbed by $+1\%$ | change in $g_z$ |
|---|---|
| density contrast $\Delta\rho$ | $+1.00\%$ |
| radius $R$ | $+2.01\%$ |
| depth $z$ | $-0.99\%$ |

The amplitude is **twice as sensitive to radius as to density**, because the
line mass goes as $R^{2}$; and it is exactly as sensitive to depth as to density,
because $g \propto 1/z$. That symmetry is the reason a single amplitude cannot
separate the three; only the profile's shape, which depends on $z$ alone, adds
independent information.

## 7. Assumptions and regime of validity

1. **Homogeneous density contrast.** A layered or graded body must be
   subdivided; the formulas are linear, so subdivision is exact but the
   interpretation of the sub-blocks is not unique.
2. **Uniform half-space above the body**, flat observation surface.
3. **2-D treatment** requires a strike length much larger than the
   source-to-observation distance. At a $2\ \mathrm{km}$ strike length and a
   $\sim 800\ \mathrm{m}$ depth the demonstration finds a $10\%$ error; the rule
   of thumb is strike length $\gtrsim 5$–$10\times$ depth.
4. **Vertical sides** for the rectangle and the slab. Tapered bodies need
   polygons or prisms.
5. **Newtonian, non-relativistic gravity**; $G$ constant, the body's own field
   negligible. Both hold at every scale encountered in geophysics.

## 8. Python demonstration

`code/simple_body_formulas_demo.py` prints:

1. a profile table for all five bodies, in mGal;
2. the closed-form rectangle against Gauss-Legendre quadrature, with the
   differences;
3. the slab, semi-infinite and point-mass limits with their ratios;
4. the half-width and derivative depth rules, including the recovery of the top
   depth of the step model;
5. the $\pm1\%$ sensitivity table.

Every number quoted in this lesson comes from that output; the script prints
units on every line and exits 0.

## 9. Exercises

See
[`exercises/02-simple-body-formulas-exercises.md`](./exercises/02-simple-body-formulas-exercises.md)
and
[`exercises/02-simple-body-formulas-solutions.md`](./exercises/02-simple-body-formulas-solutions.md).

- **★** Evaluate the slab formula by hand for $\Delta\rho = 250\
  \mathrm{kg\,m^{-3}}$, $t = 100\ \mathrm{m}$, and express the answer in mGal.
- **★** Show that the 2-D kernel $\iint z'/(u^{2}+z'^{2})$ has the dimensions of
  a length, and hence that $2G\Delta\rho \times$ (length) is an acceleration.
- **★★** Differentiate the semi-infinite sheet formula and verify that the
  horizontal derivative peaks at $x = 0$.
- **★★** Derive $J(u)$ from the inner depth integral and confirm
  $J'(u) = \ln$ form.
- **★★★** Show that a rectangle's anomaly at its own centre approaches the slab
  value as the width grows, and estimate the width at which the error falls
  below $1\%$ for a $200\ \mathrm{m}$-thick body at $500\ \mathrm{m}$ depth.

## Mastery checkpoint

Without notes:

> A dyke has a rectangular cross-section $800\ \mathrm{m}$ wide, extending from
> $400\ \mathrm{m}$ to $4\ \mathrm{km}$ depth, with
> $\Delta\rho = 350\ \mathrm{kg\,m^{-3}}$.

**(a)** State the 2-D kernel and the closed form you would use.
**(b)** Compute the anomaly directly above the centre and compare it with the
infinite-slab value for the same thickness.
**(c)** Compute the anomaly at an offset of $2\ \mathrm{km}$.
**(d)** State two limits you would use to verify an implementation, and one
reason the answer would still be wrong about the Earth.

## Common pitfalls

1. **Dropping the factor of two** between the 2-D and 3-D kernel.
2. **Using $g = 2\pi G\Delta\rho t$ for a finite sheet** and reporting no depth
   dependence where there is some.
3. **Applying the slab formula to a narrow body.** The demonstration's
   $2\ \mathrm{km}$-wide sheet is within $0.04\%$ of the slab; a $200\ \mathrm{m}$
   wide body is not.
4. **Confusing half-width with depth for a dyke.** The rectangle's profile is not
   that of a cylinder; only the step's own derivative rule applies.
5. **Forgetting $\ln$ and $\arctan$ arguments are dimensionless.** Feeding metres
   into a bare logarithm hides a normalisation error that will not show up in
   the units of the result.

## 10. Applications

- **Forward modelling engines.** The rectangular prism of
  [03](03-forward-modelling-2d3d.md) is the 3-D counterpart of the rectangle
  here, and is what most commercial and open codes actually compute.
- **Bouguer reduction.** The slab term is the middle term of the standard
  reduction chain ([07-01-04](../01-gravity-fundamentals/04-gravity-reduction.md)).
- **Dyke and fault interpretation.** The step formula is the classic tool for
  locating a fault or a dyke edge from a gravity profile.
- **Verification suites.** A forward-modelling code is accepted only after it
  reproduces these closed forms; see
  [12-01-04 Verification vs Validation: Benchmarks and Convergence Tests](../../03-scientific-computing/12-numerical-simulation-python/04-verification-and-validation.md).

## Related modules

- [01 Interpreting Anomalies: Geometry, Depth and Amplitude Rules](01-anomaly-interpretation.md).
- [03 Forward Modelling in 2-D and 3-D](03-forward-modelling-2d3d.md) — prisms,
  superposition and voxelisation.
- [04 Gravity Inversion and Its Severe Non-Uniqueness](04-inversion-gravity.md) —
  what these formulas cannot tell you.
- [02-08-02 Laplace's Equation and Harmonic Functions](../../02-physics/08-potential-theory/02-laplace-equation.md) —
  why these kernels are all related.

## 11. Self-assessment checklist

- [ ] I can write down the 2-D kernel and say where the factor 2 comes from.
- [ ] I can derive the slab formula in three lines.
- [ ] I can write the semi-infinite sheet formula and its derivative rule.
- [ ] I can implement the rectangle closed form from $P(u,a)$.
- [ ] I can name three limits and use them as tests.
- [ ] I can quote the sensitivity of the anomaly to $\Delta\rho$, $R$ and $z$.
- [ ] I can state the strike-length condition for a 2-D interpretation.
