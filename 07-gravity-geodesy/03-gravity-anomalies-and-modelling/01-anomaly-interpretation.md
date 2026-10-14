---
id: 07-03-01
title: "Interpreting Anomalies: Geometry, Depth and Amplitude Rules"
level: advanced
prereqs: ["07-01-04", "07-01-05"]
tags: [gravity, geodesy, anomalies, interpretation, non-uniqueness]
---

# Interpreting Anomalies: Geometry, Depth and Amplitude Rules

All models and data in this module are SYNTHETIC. The densities, depths and
stations used below are chosen teaching values, not measurements of any real
body.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the half-width of the anomaly of a buried sphere and of a
   horizontal cylinder, and show that each gives a depth rule.
2. **Compute** the peak anomaly of a sphere and of a 2-D cylinder from the
   density contrast and the geometry, with units carried through.
3. **Measure** how the amplitude scales with depth and **state** the exponent for
   a sphere, a cylinder and an infinite sheet.
4. **Locate** the maximum of the horizontal derivative analytically and use it as
   a second, independent depth rule.
5. **Explain** why one anomaly ordinate cannot determine depth, size and density
   together, and **quantify** the family of bodies that fit it.
6. **Estimate** the depth bias introduced by interpreting an anomaly with the
   wrong body shape.
7. **State** the assumptions under which each rule is valid and the regime in
   which it fails.

## Prerequisites

- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../01-gravity-fundamentals/04-gravity-reduction.md) —
  what an anomaly is, and why the reduction matters before interpretation.
- [07-01-05 Units (Gal, mGal), Absolute vs Relative Measurement](../01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md) —
  the practical size of a measurable anomaly.

## 1. The question interpretation actually answers

A gravity anomaly is a map of one number: the vertical component of the
attraction of an unknown density distribution, sampled on a surface. The
distribution is three-dimensional and continuous, so the map is a projection: an
enormous number of dimensions squeezed into one. Interpretation is the art of
recovering a small number of parameters from that projection, and the honest
version of it always states which parameters were *assumed* and which were
*measured*.

The rules of thumb in this lesson are the traditional toolkit: a sphere's depth
from the width of its anomaly, a cylinder's depth from the same, an amplitude
that falls off as a known power of depth. They are useful, and they are also the
place where most overclaims begin, because each rule silently fixes the shape of
the body. A single anomaly has a half-width, and the half-width converts to a
depth only after you have decided what the body is.

## 2. Precise definitions

### 2.1 The anomaly of a sphere

For a homogeneous sphere of radius $R$, density contrast $\Delta\rho$ and centre
at depth $z$, the field outside the sphere is identical to that of a point mass
$M = \tfrac{4}{3}\pi R^{3}\Delta\rho$ at its centre, so

$$
g_z(x) = \frac{G M z}{\left(x^{2}+z^{2}\right)^{3/2}}
\qquad (\mathrm{m\,s^{-2}}),
$$

with $x$ the horizontal offset from above the centre. The peak sits at $x = 0$:

$$g_{z,\max} = \frac{G M}{z^{2}}.$$

### 2.2 The anomaly of an infinite horizontal cylinder

For a cylinder of radius $R$ whose axis is horizontal, at depth $z$, extending
infinitely along the strike, the anomaly per unit length is that of a line mass
$\lambda = \pi R^{2}\Delta\rho$:

$$
g_z(x) = \frac{2 G \lambda z}{x^{2}+z^{2}},
\qquad
g_{z,\max} = \frac{2 G \lambda}{z}.
$$

### 2.3 Half-width

The **half-width** $x_{1/2}$ is the horizontal distance at which the anomaly has
fallen to half its peak value. It is a width, and widths are where depth hides in
a potential-field anomaly: amplitudes are controlled by mass, widths by geometry.

## 3. Derivations

### 3.1 The half-width of a sphere

Set $g_z(x_{1/2}) = \tfrac{1}{2}g_{z,\max}$:

$$\frac{z}{\left(x_{1/2}^{2}+z^{2}\right)^{3/2}} = \frac{1}{2z^{2}}
\;\Longrightarrow\;
x_{1/2}^{2}+z^{2} = 2^{2/3} z^{2}
\;\Longrightarrow\;
x_{1/2} = z\sqrt{2^{2/3}-1}.$$

Numerically $\sqrt{2^{2/3}-1} = 0.766421$, so

$$\boxed{\;z = \frac{x_{1/2}}{0.766421} = 1.3048\,x_{1/2}\;}\qquad
\text{(sphere, point-mass regime).}$$

The demonstration prints $x_{1/2}/z = 0.766421$ for a synthetic sphere with
$R = 500\ \mathrm{m}$, $\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$,
$z = 1000\ \mathrm{m}$: the profile half-width is $766.4\ \mathrm{m}$ and the
rule returns exactly $1000.0\ \mathrm{m}$.

### 3.2 The half-width of a cylinder

The same operation on $z/(x^{2}+z^{2})$:

$$\frac{z}{x_{1/2}^{2}+z^{2}} = \frac{1}{2z}
\;\Longrightarrow\;
x_{1/2}^{2}+z^{2} = 2z^{2}
\;\Longrightarrow\;
x_{1/2} = z.$$

For a 2-D body the half-width **is** the depth, with no scale factor. The
demonstration measures $500.00\ \mathrm{m}$ for a cylinder of radius
$200\ \mathrm{m}$ at $500\ \mathrm{m}$ depth, and the peak is
$1.0065\ \mathrm{mGal}$.

*Units.* $G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$\Delta\rho$ in $\mathrm{kg\,m^{-3}}$, lengths in metres give
$g_z$ in $\mathrm{m\,s^{-2}}$; the demonstration divides by
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ to print mGal. The widths are
ratios of lengths and are dimensionless in the rule.

### 3.3 Amplitude versus depth

Hold the mass fixed and vary $z$: the sphere gives $g \propto z^{-2}$, because
$g_{\max} = GM/z^{2}$. The cylinder with fixed $\lambda$ gives
$g \propto z^{-1}$. The infinite sheet gives no dependence at all,
$g = 2\pi G \Delta\rho\,t$, a result this module derives properly in
[02](02-simple-body-formulas.md). A log-log fit of the demonstration's peaks
over $z = 200$ to $3200\ \mathrm{m}$ returns slopes $-2.0000$ and $-1.0000$ for
the two bodies; the exponents are exact, not fitted artefacts.

| body | peak amplitude | half-width | depth rule |
|---|---|---|---|
| sphere (point mass) | $G M / z^{2}$ | $0.7664\,z$ | $z = 1.3048\,x_{1/2}$ |
| horizontal cylinder | $2G\lambda / z$ | $1.0000\,z$ | $z = x_{1/2}$ |
| infinite sheet | $2\pi G \Delta\rho t$ | none | no depth information |

### 3.4 A second, independent depth rule: the horizontal derivative

Widths are not the only geometry in the profile. The maximum of the horizontal
derivative sits at a fixed fraction of the depth. For the sphere,

$$\frac{\mathrm{d}g_z}{\mathrm{d}x} \propto
\frac{-3xz}{\left(x^{2}+z^{2}\right)^{5/2}},$$

whose magnitude is maximised where $x^{2}+z^{2} - 5x^{2} = 0$, that is at
$x = z/2$. For the cylinder,

$$\frac{\mathrm{d}g_z}{\mathrm{d}x} \propto \frac{2xz}{\left(x^{2}+z^{2}\right)^{2}},
\qquad x = \frac{z}{\sqrt{3}} = 0.5774\,z.$$

The demonstration measures $|x|/z = 0.5000$ and $0.5772$ on a numerical gradient
of the profiles, agreeing with the analytic values $0.5$ and
$1/\sqrt{3} = 0.57735$ to the grid resolution. **Two features of the same
profile, the half-width and the derivative maximum, give the same depth only if
the assumed body shape is right** — which is precisely what makes the pair a
useful consistency test.

### 3.5 Excess mass and the depth–amplitude trade-off

For a compact body the anomaly contains one more usable number: the **excess
mass**, obtained (for a 2-D body) by integrating the anomaly across the profile.
But the peak alone, $g_{z,\max}$, gives only

$$M = g_{z,\max} z^{2}/G \qquad \text{(sphere)},$$

which is one equation in two unknowns, $M$ and $z$. The demonstration fixes a
target peak of $0.30\ \mathrm{mGal}$ and prints the sphere family that reproduces
it:

| $z$ (m) | required $M$ (kg) | required $R$ (m) | $R/z$ | half-width (m) |
|---|---|---|---|---|
| 500 | $1.124\times10^{10}$ | 207.6 | 0.415 | 383.2 |
| 1000 | $4.495\times10^{10}$ | 329.5 | 0.329 | 766.4 |
| 2000 | $1.798\times10^{11}$ | 523.0 | 0.262 | 1532.8 |
| 4000 | $7.192\times10^{11}$ | 830.2 | 0.208 | 3065.7 |

Every row reproduces the measured number at $x = 0$ identically. They differ
only in their *shape*: the deeper body is wider, so the profile still
discriminates — but only through its width, and only if the width is well
sampled on both flanks. This is the first appearance of the non-uniqueness that
[04 Gravity Inversion and Its Severe Non-Uniqueness](04-inversion-gravity.md)
quantifies.

### 3.6 The price of assuming the wrong shape

Treat a 2-D cylinder's anomaly with the sphere rule and the depth comes out
$1/0.766421 = 1.3048$ times too large. For the demonstration's cylinder at
$500\ \mathrm{m}$ the sphere rule returns $652.4\ \mathrm{m}$: a **$+30.5\%$**
depth error with a perfect, noise-free profile. No amount of care with the
arithmetic recovers the depth when the shape assumption is wrong.

## 4. Worked example

*A survey line crosses an isolated anomaly. The peak is $2.40\ \mathrm{mGal}$,
the half-width is $640\ \mathrm{m}$, and the stations are $50\ \mathrm{m}$ apart.*

1. **Depth under the cylinder assumption:**
   $z = x_{1/2} = 640\ \mathrm{m}$.
2. **Depth under the sphere assumption:**
   $z = 640/0.766421 = 835.1\ \mathrm{m}$.
3. **Mass if it is a sphere at $835.1\ \mathrm{m}$:** using
   $g = 6.67430\times10^{-11}\ \mathrm{m^{3}kg^{-1}s^{-2}}$ and
   $2.40\ \mathrm{mGal} = 2.40\times10^{-5}\ \mathrm{m\,s^{-2}}$,
   $$M = \frac{g z^{2}}{G} =
   \frac{2.40\times10^{-5}\times (835.1)^{2}}{6.67430\times10^{-11}}
   = 2.51\times10^{11}\ \mathrm{kg}.$$
   At $\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$ this is
   $R = \left(3M/4\pi\Delta\rho\right)^{1/3} = 585\ \mathrm{m}$, consistent with
   $R/z = 0.70$ — too large for the point-mass approximation to be comfortable,
   which is itself information (the body is not compact).
4. **Line mass if it is a cylinder at $640\ \mathrm{m}$:** from
   $g_{\max} = 2G\lambda/z$,
   $$\lambda = \frac{g_{\max} z}{2G} =
   \frac{2.40\times10^{-5}\times 640}{2\times 6.67430\times10^{-11}}
   = 1.151\times10^{8}\ \mathrm{kg\,m^{-1}},$$
   so $R = \sqrt{\lambda/(\pi\Delta\rho)} = 349\ \mathrm{m}$.
5. **Conclusion.** The two interpretations differ in depth by $195\ \mathrm{m}$
   ($30.5\%$) and imply different bodies. Report the range and the assumption;
   do not report a number.

## 5. Assumptions and regime of validity

1. **Isolated body.** Overlapping sources superpose, and a half-width measured on
   a composite anomaly is meaningless. [05](05-derivatives-and-filters.md) treats
   separation by derivatives and continuation.
2. **Point-mass (or line-mass) regime.** For the sphere, $R \lesssim z/2$; for the
   cylinder, $R \lesssim z$. Outside this the body's own size distorts the
   profile and the rules degrade — the demonstration of the excess-mass family
   prints $R/z$ for exactly this reason.
3. **Vertically-sided geometry.** The rules are derived for a sphere and a
   circular cylinder. A dyke, a sill or a finite sheet has different rules; see
   [02](02-simple-body-formulas.md).
4. **Flat, uniform overburden.** The density contrast is assumed constant and
   the observation surface flat; topography and variable cover bias the
   amplitude.
5. **No regional field.** The half-width requires a referred level. A sloping
   regional tilts the flanks and widens the apparent anomaly; the residual must be
   isolated first (demonstrated in
   [06 Microgravity for Cavities, Tunnels and Archaeology](06-microgravity-applications.md)).
6. **Noise smaller than the curvature.** The rules read a shape; noise that
   flattens the peak changes the half-width. Section 6 of the microgravity lesson
   measures the trade-off.

## 6. Physical interpretation

- Widths are geometric, amplitudes are mass-weighted. This is why the two are
  worth measuring separately: one constrains depth, the other constrains mass,
  and neither alone constrains both.
- The half-width rules are *scaling* rules: they follow from the self-similar
  form of the kernel, $g = z^{-n}F(x/z)$. Every self-similar anomaly profile
  has a half-width proportional to the depth; the constant of proportionality is
  the only thing that changes between shapes.
- The horizontal derivative sharpens the edges of a body because
  differentiation multiplies the spectrum by wavenumber; the derivative maximum
  sits over the flank. This is the intuition behind the derivative-based depth
  rules and behind the filters of [05](05-derivatives-and-filters.md).
- The trade-off in §3.5 is not a defect of gravity: it is the statement that a
  potential field on a *surface* is a projection of a *volume*. Making it visible
  with numbers, as the demonstration does, is the point.

## 7. Python demonstration

`code/anomaly_interpretation_demo.py` computes all of the above and prints
labelled results with units. It:

1. builds a synthetic sphere profile and prints the peak, the measured
   half-width and the ratio $x_{1/2}/z$, confirming the analytic value
   $0.766421$;
2. does the same for a horizontal cylinder, where the ratio is exactly $1$;
3. tabulates peak amplitude against depth and measures the log-log slopes
   ($-2.0000$ and $-1.0000$);
4. locates the maximum of the horizontal derivative and compares it with
   $z/2$ and $z/\sqrt{3}$;
5. prints the sphere family that reproduces one peak value, with $R/z$ shown;
6. quantifies the $+30.5\%$ depth error from interpreting a cylinder with the
   sphere rule.

Note the amplitude of a compact body: the demonstration's sphere gives
$1.0484\ \mathrm{mGal}$, a geologically plausible figure for a body of
$1.57\times10^{11}\ \mathrm{kg}$ at $1\ \mathrm{km}$. Gravity anomalies of
economic interest are often a few tenths of a mGal, which is why
[07-01-05](../01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md)
spends time on units and instrument resolution.

## 8. Exercises

Full sets with worked solutions are in
[`exercises/01-anomaly-interpretation-exercises.md`](./exercises/01-anomaly-interpretation-exercises.md)
and
[`exercises/01-anomaly-interpretation-solutions.md`](./exercises/01-anomaly-interpretation-solutions.md).

- **★** Derive $x_{1/2}/z = \sqrt{2^{2/3}-1}$ for the sphere and evaluate it to
  six decimal places.
- **★** A cylinder anomaly has a half-width of $300\ \mathrm{m}$; give the depth
  under the cylinder and under the sphere rule.
- **★★** A sphere of radius $400\ \mathrm{m}$ and $\Delta\rho = 250\
  \mathrm{kg\,m^{-3}}$ lies at $900\ \mathrm{m}$. Compute the peak anomaly, the
  half-width and the maximum horizontal derivative.
- **★★** Using the family table, find the mass of a body that would give
  $0.30\ \mathrm{mGal}$ at $8\ \mathrm{km}$ and comment on whether it is
  plausible as a single body.
- **★★★** Design a field procedure that would distinguish a cylinder at
  $500\ \mathrm{m}$ from a sphere at $652\ \mathrm{m}$ with the same peak
  amplitude, and state the measurement that decides it.

## Mastery checkpoint

Without notes:

> A profile has a peak of $1.80\ \mathrm{mGal}$ and a half-width of
> $420\ \mathrm{m}$; the stations are $40\ \mathrm{m}$ apart and the regional
> field is flat.

**(a)** Give the depth under the cylinder rule and under the sphere rule.
**(b)** Compute the line mass for the cylinder interpretation.
**(c)** Compute the mass for the sphere interpretation and the corresponding
radius at $\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$; is the point-mass
approximation self-consistent at the depth you derived?
**(d)** State in one sentence why you cannot report a single depth, and name one
additional measurement that would break the ambiguity.

## Common pitfalls

1. **Quoting a depth from a half-width without naming the body.** The difference
   between the two rules here is $30.5\%$.
2. **Forgetting the point-mass restriction.** A body with $R \sim z$ is not a
   point mass, and its own geometry perturbs the profile.
3. **Measuring a half-width relative to a guessed level.** A regional tilt or a
   wrong datum shifts the level and widens or narrows the anomaly.
4. **Reading the amplitude as mass only.** Amplitude is mass divided by a power
   of depth; the same amplitude can be twice the mass at twice the depth.
5. **Assuming the depth rule survives overlap.** Two bodies produce a composite
   anomaly whose half-width belongs to neither.

## 9. Applications

- **Mineral and groundwater exploration.** Half-width depth rules give a first
  estimate of target depth for drilling decisions, immediately qualified by the
  assumed shape.
- **Microgravity surveys.** The same rules apply at metre scale, where the
  bodies are cavities and the units are microgal —
  [06](06-microgravity-applications.md).
- **Crustal-scale studies.** At hundreds of kilometres the rules still work, but
  the anomaly is no longer isolated from isostasy
  ([07-01-06](../01-gravity-fundamentals/06-isostasy.md)).
- **Teaching inversion.** The trade-off of §3.5 is the simplest possible
  demonstration that a perfect fit is not an answer; it prepares
  [04](04-inversion-gravity.md) and
  [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md).

## Related modules

- [02 Analytical Formulas for Sphere, Cylinder, Sheet and Dyke](02-simple-body-formulas.md) —
  the closed forms behind every rule here.
- [03 Forward Modelling in 2-D and 3-D](03-forward-modelling-2d3d.md) — how to
  compute the anomaly of a body that has no closed form.
- [04 Gravity Inversion and Its Severe Non-Uniqueness](04-inversion-gravity.md) —
  the trade-off, quantified.
- [05 Derivatives, Upward/Downward Continuation and Euler Deconvolution](05-derivatives-and-filters.md) —
  separating what the profile hides.
- [06 Microgravity for Cavities, Tunnels and Archaeology](06-microgravity-applications.md) —
  the same rules at engineering scale.

## 10. Self-assessment checklist

- [ ] I can derive both half-width rules without notes.
- [ ] I can carry units through a peak-amplitude calculation to mGal.
- [ ] I can state the depth exponent of the amplitude for sphere, cylinder and
      sheet, and why the sheet has none.
- [ ] I can locate the horizontal-derivative maximum analytically.
- [ ] I can construct the family of bodies that reproduces one peak ordinate.
- [ ] I can state the depth error from using the wrong shape, as a number.
- [ ] I can list the assumptions that must hold before any rule applies.
