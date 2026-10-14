---
id: 01-04-05
title: "Surfaces, Parametrisation and Curvature"
level: advanced
prereqs: ["01-04-03", "01-04-04", "01-05-02"]
estimated_minutes: 75
tags: [differential-geometry, curvature, surfaces, geodesics, geoid]
---

# Surfaces, Parametrisation and Curvature

## Learning objectives

By the end of this lesson you will be able to:

1. **Parametrise** a surface, compute its tangent vectors and its unit normal, and
   say what makes a parametrisation regular.
2. **Compute** the first fundamental form, and use it to write arc length and area
   elements without deriving them again.
3. **Compute** the second fundamental form, normal curvature, principal curvatures,
   Gaussian curvature and mean curvature — by hand in simple cases and
   numerically in general.
4. **State** Gauss's Theorema Egregium and explain why it forbids a map that
   preserves both angles and areas.
5. **Explain** what a geodesic is, and why the great circle is the geodesic of a
   sphere — the reason great-circle paths are shortest.
6. **Use** the local curvature of the Earth quantitatively: the drop below a
   tangent plane, horizon distance, and levelling corrections.
7. **Choose** a numerical step length for computing curvature from data, and
   explain the truncation-versus-round-off trade-off that fixes it.

## Prerequisites

[01-04-03 Cartesian, Cylindrical and Spherical Coordinates](./03-cartesian-spherical.md)
and [01-04-04 Geographic Coordinates, Datums and Map Projections](./04-geographic-coordinates.md)
for the surfaces being studied, and
[01-05-02 Derivatives and Rates of Change](../05-single-variable-calculus/02-derivatives.md)
for differentiation. Partial derivatives are used informally; the systematic
treatment is in
[01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md).

## 1. Why curvature is not decoration

Four things in geophysics are statements about curvature.

**The geoid is a surface, and its curvature is a measured quantity.** A deflection
of the vertical is the slope of the geoid; the curvature of the geoid is what
couples gravity gradients to topographic loads. Curvature is a second derivative of
the same field, so it is noisier than the slope, which is why curvature maps are
used for lineament detection and why they need care.

**Map distortion is curvature.** A sphere has Gaussian curvature $1/R^{2}$; a plane
has zero. That difference is why no map can preserve both angles and areas, and the
statement is a theorem about curvature, not a limitation of drafting.

**Ray paths in a heterogeneous Earth are geodesic-like curves.** In a
spherically-symmetric Earth the rays are planar curves governed by Snell's law in
radius, and the great circle is the limiting case of a uniform medium. The
language of geodesics is the language of ray geometry.

**Boundary conditions in potential fields are curvature.** The normal derivative
on a surface requires the surface normal, which requires the first fundamental
form. A modelling code that assumes a flat surface where the topography has
curvature of the same scale as the target depth will produce a systematically
wrong result, and the size of the error is set by the curvature.

## 2. Parametrising a surface

A **parametrised surface** is a map from two parameters to three-dimensional space:

$$\mathbf{X}(u, v) = \left(x(u,v),\ y(u,v),\ z(u,v)\right).$$

The parameters $u$ and $v$ are coordinates *on* the surface — they are not
distances. The tangent vectors are

$$\mathbf{X}_u = \frac{\partial\mathbf{X}}{\partial u}, \qquad
\mathbf{X}_v = \frac{\partial\mathbf{X}}{\partial v},$$

and the surface is **regular** where these are linearly independent, i.e. where
$\mathbf{X}_u \times \mathbf{X}_v \neq \mathbf{0}$. The unit normal is

$$\mathbf{n} = \frac{\mathbf{X}_u\times\mathbf{X}_v}
{\lvert\mathbf{X}_u\times\mathbf{X}_v\rvert} .$$

**Two parametrisations of the Earth's surface**, both used in this curriculum:

$$\mathbf{X}(\varphi,\lambda) = R\left(\cos\varphi\cos\lambda,\
\cos\varphi\sin\lambda,\ \sin\varphi\right)
\quad\text{(latitude–longitude, $\varphi$ = latitude),}$$

$$\mathbf{g}(x, y) = \left(x,\ y,\ h(x,y)\right) \quad\text{(topographic height).}$$

The first is regular except at the poles, where the tangent vector in the longitude
direction vanishes — the coordinate singularity of
[01-04-03 Section 6](./03-cartesian-spherical.md), now visible as a geometric fact:
the latitude–longitude grid is not a regular parametrisation on the polar axis.

The second is the **graph parametrisation**, regular everywhere, and it is the
right choice for gridded topographic or horizon surfaces because $x$ and $y$ are
already grid coordinates.

## 3. The first fundamental form: the metric on the surface

Define

$$E = \mathbf{X}_u\cdot\mathbf{X}_u, \qquad
F = \mathbf{X}_u\cdot\mathbf{X}_v, \qquad
G = \mathbf{X}_v\cdot\mathbf{X}_v .$$

Then an infinitesimal displacement on the surface has squared length

$$ds^{2} = E\,du^{2} + 2F\,du\,dv + G\,dv^{2},$$

and an infinitesimal area element is

$$dA = \sqrt{EG - F^{2}}\;du\,dv .$$

These are worth memorising in this form, because they *generate* every arc length
and every area on the surface. If you can write $E$, $F$ and $G$, you have the
geometry.

**Example: the sphere.** With $\mathbf{X}(\varphi,\lambda)$ as above and $u =
\varphi$, $v = \lambda$,

$$\mathbf{X}_\varphi = R\left(-\sin\varphi\cos\lambda,\
-\sin\varphi\sin\lambda,\ \cos\varphi\right), \qquad
\mathbf{X}_\lambda = R\cos\varphi\left(-\sin\lambda,\ \cos\lambda,\ 0\right),$$

$$E = R^{2}, \qquad F = 0, \qquad G = R^{2}\cos^{2}\varphi .$$

Hence $ds^{2} = R^{2}d\varphi^{2} + R^{2}\cos^{2}\varphi\,d\lambda^{2}$ — the
familiar statement that a degree of longitude is $\cos\varphi$ times a degree of
latitude — and

$$dA = \sqrt{R^{4}\cos^{2}\varphi}\;d\varphi\,d\lambda
= R^{2}\cos\varphi\,d\varphi\,d\lambda,$$

which is the area element used for the cap areas of
[01-04-03 Section 3.1](./03-cartesian-spherical.md). **The spherical-cap formula
is just $\int\!\!\int\sqrt{EG-F^{2}}\,du\,dv$**, so there is nothing to remember
separately.

**Example: a graph.** For $\mathbf{g}(x,y) = (x, y, h(x,y))$,

$$E = 1 + h_x^{2}, \qquad F = h_xh_y, \qquad G = 1 + h_y^{2},$$

$$EG - F^{2} = \left(1+h_x^{2}\right)\left(1+h_y^{2}\right) - h_x^{2}h_y^{2}
= 1 + h_x^{2} + h_y^{2},$$

$$dA = \sqrt{1 + h_x^{2} + h_y^{2}}\;dx\,dy .$$

That square root is the **slope-area correction** applied to every topographic or
horizon surface: a steep slope has more surface area than its map footprint. On a
slope of $45°$, $h_x = 1$ gives $\sqrt{2} = 1.414$, so the true surface area is 41
percent larger than the planimetric area.

## 4. The second fundamental form: how the surface bends

The second fundamental form measures the component of the second derivative along
the normal:

$$L = \mathbf{X}_{uu}\cdot\mathbf{n}, \qquad
M = \mathbf{X}_{uv}\cdot\mathbf{n}, \qquad
N = \mathbf{X}_{vv}\cdot\mathbf{n} .$$

For a curve on the surface whose tangent makes a direction in parameter space
$(du, dv)$, the **normal curvature** is the ratio of the two forms:

$$\kappa_n = \frac{L\,du^{2} + 2M\,du\,dv + N\,dv^{2}}
{E\,du^{2} + 2F\,du\,dv + G\,dv^{2}} .$$

The **principal curvatures** $\kappa_1$ and $\kappa_2$ are the extreme values of
$\kappa_n$ over directions, obtained as the eigenvalues of the shape operator
$\mathrm{I}^{-1}\mathrm{II}$:

$$\kappa_{1,2} = H \pm \sqrt{H^{2} - K},$$

where the two invariants are

$$K = \kappa_1\kappa_2 = \frac{LN - M^{2}}{EG - F^{2}}
\quad\text{(Gaussian curvature)},$$

$$H = \frac{\kappa_1 + \kappa_2}{2} = \frac{EN - 2FM + GL}{2(EG - F^{2})}
\quad\text{(mean curvature)} .$$

**Signs.** The sign of $H$ depends on which side the normal points; $K$ does not.
Where the two principal curvatures have the same sign the surface is locally
dome-like or bowl-like ($K > 0$); where they have opposite signs it is
saddle-shaped ($K < 0$). **The sign of $K$ tells you whether the surface is
elliptic, parabolic or hyperbolic at that point**, and that classification is
intrinsic.

### 4.1 Gauss's Theorema Egregium

> **Gauss's theorem.** The Gaussian curvature $K$ of a surface depends only on the
> first fundamental form — the metric — and not on how the surface sits in space.

The consequence is immediate and important: **$K$ is invariant under any
deformation that does not stretch the surface.** A sheet of paper has $K = 0$
everywhere; bending it into a cylinder leaves $K = 0$, and so does any rolling,
while trying to wrap it onto a sphere forces stretching or tearing. The
latitude–longitude rectangle on a sphere has $K = 1/R^{2} \ne 0$, so it cannot be
laid flat without distortion.

That is the theorem behind
[01-04-04 Section 5](./04-geographic-coordinates.md): a map preserves angles
(isometry up to scale, hence conformal) or areas (isometry of area), but a
curvature-preserving flattening would have to preserve $K$, and the plane has $K =
0$ while the Earth does not. **No projection can be simultaneously conformal and
equal-area, and the reason is that the two quantities are different functions of
the same two invariants.**

## 5. Worked examples

### 5.1 The sphere, by hand and numerically

For $\mathbf{X}(\varphi,\lambda)$ with $R$ constant, use the convention in which
the outward unit normal is $\mathbf{n} = \mathbf{X}/R$. Then

$$\mathbf{X}_{\varphi\varphi} = -R\left(\cos\varphi\cos\lambda,\
\cos\varphi\sin\lambda,\ \sin\varphi\right) = -\mathbf{X},$$

so $L = \mathbf{X}_{\varphi\varphi}\cdot\mathbf{n} = -R$. Similarly

$$N = \mathbf{X}_{\lambda\lambda}\cdot\mathbf{n} = -R\cos^{2}\varphi, \qquad
M = 0 .$$

And, from Section 3, $E = R^{2}$, $F = 0$, $G = R^{2}\cos^{2}\varphi$. Therefore

$$K = \frac{(-R)\left(-R\cos^{2}\varphi\right) - 0}
{R^{2}\cdot R^{2}\cos^{2}\varphi - 0} = \frac{1}{R^{2}}, \qquad
H = \frac{-2R^{3}\cos^{2}\varphi}{2R^{4}\cos^{2}\varphi} = -\frac{1}{R} .$$

$K = 1/R^{2} > 0$ everywhere, as it must be, and $|H| = 1/R$ with a sign set by
the choice of normal.

The demonstration recovers this from the parametrisation by finite differences,
using a step length chosen from the study in Section 7:

```text
  u (deg)   v (deg)         K numeric             1/R^2   relative error
     30.0       0.0 2.463682808750e-08 2.463682790395e-08        7.450e-09
     60.0      45.0 2.463682812484e-08 2.463682790395e-08        8.966e-09
     90.0     120.0 2.463682780043e-08 2.463682790395e-08        4.202e-09
```

Agreement to eight significant figures at three different points, which is the
strongest verification available for a curvature implementation: **a sphere has
constant $K$, so any position dependence in your computed $K$ is a bug.**

Because $K$ is constant and positive, the sphere is a surface of *constant positive
curvature*, the only such closed surface — a classical result worth knowing because
it explains why the Earth's shape is so nearly determined by a single number.

### 5.2 The paraboloid: curvature that varies

Near a station the geoid or a horizon surface is often modelled as a paraboloid,
$h(x,y) = \left(x^{2}+y^{2}\right)/(2R)$, with $R$ the local radius of curvature.
For a graph surface, the Gaussian curvature has a compact form:

$$K = \frac{h_{xx}h_{yy} - h_{xy}^{2}}
{\left(1 + h_x^{2} + h_y^{2}\right)^{2}} .$$

For the paraboloid, $h_{xx} = h_{yy} = 1/R$ and $h_{xy} = 0$, and
$h_x^{2}+h_y^{2} = \rho^{2}/R^{2}$ with $\rho^{2} = x^{2}+y^{2}$, so

$$K = \frac{1}{R^{2}}\frac{1}{\left(1 + \rho^{2}/R^{2}\right)^{2}} .$$

At the apex $K = 1/R^{2}$, matching a sphere of the same radius of curvature, and
it *decreases* away from the apex — the surface flattens. The demonstration
confirms this against its numerical differentiation:

| $r$ (km) | $K$ numeric (km$^{-2}$) | $K$ closed form (km$^{-2}$) | difference |
|---|---|---|---|
| 0.0 | $2.463682790395\times10^{-8}$ | $2.463682790395\times10^{-8}$ | $3.3\times10^{-24}$ |
| 100.0 | $2.462469292287\times10^{-8}$ | $2.462469292286\times10^{-8}$ | $6.8\times10^{-21}$ |
| 1000.0 | $2.346631342667\times10^{-8}$ | $2.346631342759\times10^{-8}$ | $9.2\times10^{-19}$ |
| 3000.0 | $1.650567469994\times10^{-8}$ | $1.650567470058\times10^{-8}$ | $6.5\times10^{-19}$ |
| 6371.0 | $6.159206895443\times10^{-9}$ | $6.159206975987\times10^{-9}$ | $8.1\times10^{-17}$ |

At $r = R = 6371$ km the curvature has fallen to a quarter of its apex value. In SI
units, $K = 2.4637\times10^{-14}\ \mathrm{m^{-2}}$ at the apex — **curvature
quantities are tiny numbers, and this is why gravity gradients, which are curvature
of the potential, are measured in eötvös units**, a scale chosen to make those
numbers readable.

### 5.3 The curvature of the Earth in everyday quantities

Two formulas from this geometry are used constantly in surveying.

**Drop below the tangent plane.** Over a horizontal distance $d$ on a sphere of
radius $R$, the surface falls below the tangent plane by

$$h_{\text{drop}} = R\left(1 - \cos\frac{d}{R}\right) \approx \frac{d^{2}}{2R}
\quad\text{for } d \ll R .$$

**Distance to the geometric horizon** from height $H$ above the sphere:

$$d_{\text{horizon}} = \sqrt{2RH + H^{2}} .$$

The demonstration evaluates both:

| $d$ | $d^{2}/(2R)$ (m) | exact (m) | ratio |
|---|---|---|---|
| 0.1 km | 0.000785 | 0.000785 | 0.999999978 |
| 1 km | 0.078481 | 0.078481 | 0.999999996 |
| 10 km | 7.848051 | 7.848049 | 0.999999795 |
| 100 km | 784.805069 | 784.788956 | 0.999979470 |
| 500 km | 19620.126722 | 19610.058448 | 0.999486840 |

| height $H$ | horizon (km) |
|---|---|
| 1 m | 3.569596 |
| 2 m | 5.048172 |
| 10 m | 11.288059 |
| 100 m | 35.696103 |
| 1000 m | 112.884975 |

**Read the numbers, not the formulas.**

- The parabolic approximation is good to better than 1 part in $10^{5}$ out to
  about 100 km, and to about 5 parts in $10^{4}$ at 500 km. It is not valid for a
  global baseline.
- Over **1 km** of level line the far end is **0.078 m** below the tangent plane.
  Over 100 km it is **785 m**. Since most geophysical targets are shallower than
  785 m, **at 100 km the curvature of the Earth is larger than the target** — a
  statement worth making explicitly, because "flat Earth" is the default assumption
  in much interpretation software.
- The horizon distances are **geometric**: they assume straight-line propagation in
  a vacuum. Atmospheric refraction typically extends the visible horizon by a few
  percent, so treat the table as a lower bound.

## 6. Geodesics: the shortest path on a surface

A **geodesic** is a curve on a surface whose geodesic curvature — the component of
its curvature tangent to the surface — vanishes. Equivalently, it is locally the
shortest path, and equivalently it is the curve traced by "walking straight ahead"
without turning left or right.

On a sphere every great circle is a geodesic, and conversely every geodesic is an
arc of a great circle. That is the deep reason the great-circle distance of
[01-03-04](../03-trigonometry/04-spherical-trigonometry.md) is the shortest
surface path: it is not a property of the distance formula but of the surface.

**Three consequences.**

- **Rays and geodesics.** In a uniform medium a seismic ray is a straight line; on
  a spherical Earth the ray path between two surface points is a chord, and the
  corresponding surface path is the great circle. When the medium varies, the ray
  bends and is no longer a geodesic of the surface — which is exactly what makes
  the problem interesting.
- **Geodesics on an ellipsoid are not the great circles.** The ellipsoidal geodesic
  wiggles in latitude relative to the great circle between the same points, which is
  why Vincenty's iteration exists and why the geodesic distance differs from the
  spherical one by the amounts measured in
  [01-03-04 Section 6](../03-trigonometry/04-spherical-trigonometry.md).
- **Curvature and geodesic deviation.** Two nearby geodesics on a surface separate
  at a rate governed by $K$: on a sphere they converge (positive curvature), on a
  saddle they diverge (negative curvature). This is the geometric content of
  "curvature is a force" in general relativity, and the same mathematics describes
  the spreading of surface-wave rays across a region.

## 7. Computing curvature from data: the step-length problem

Real curvature is computed from gridded data by finite differences, and the choice
of step length is a genuine trade-off. Differentiating twice amplifies noise, so a
large step smooths but truncates; a small step resolves but subtracts nearly equal
numbers and loses digits.

The demonstration measures the total relative error of $K$ on a sphere as a
function of the step:

```text
  step h (rad)           K numeric   relative error       regime
         1e-01  2.476037213620e-08        5.015e-03   truncation
         1e-02  2.463805978126e-08        5.000e-05   truncation
         1e-03  2.463684022357e-08        5.000e-07   truncation
         1e-04  2.463682812484e-08        8.966e-09    round-off
         1e-05  2.463680788859e-08        8.124e-07    round-off
```

The error falls as $h^{2}$ — from $5.015\times10^{-3}$ to $5.000\times10^{-5}$ when
$h$ falls by a factor of ten, and again to $5.000\times10^{-7}$ — and then turns
around and grows as round-off takes over. **The best step is near $10^{-4}$ rad,
which is about 0.6 km on the Earth's surface here**, and the U-shaped error curve is
universal: it appears in every numerical derivative, and no care in the rest of the
code removes it.

Two practical consequences.

- **Choose the step from the physics, not by trial and error in production.** A
  fixed step in a projected grid is a fixed step in distance, which is what the
  curvature calculation wants; a fixed step in latitude–longitude degrees is a
  *varying* step in distance, by a factor of $\cos\varphi$, and it therefore gives
  a latitude-dependent smoothing that looks like a real curvature trend.
- **Check convergence.** Compute $K$ at two step lengths that differ by a factor of
  two and confirm the answer has stabilised. If it has not, you are on the
  truncation or the round-off branch of the curve, and you cannot tell which
  without the comparison.

## 8. Python demonstration

Run [`code/dip_strike_demo.py`](./code/dip_strike_demo.py). Its final two sections
are the ones for this lesson: the curvature of the Earth's surface (drop, horizon,
levelling) and numerically computed Gaussian and mean curvature for a sphere and a
paraboloid, including the step-length study. Only the standard library is required.

Write your own `gaussian_curvature(params)` from the graph formula of Section 5.2
and check it against the closed form $1/R^{2}$ at the apex — an exact test that
catches errors in the formula, in the normalisation, and in the sign convention all
at once.

## 9. Common mistakes

1. **Confusing the two fundamental forms.** The first is the metric (lengths and
   areas); the second is the bending (curvature). The first is needed for the
   second, but they are not interchangeable.
2. **Sign of the mean curvature.** It flips with the direction of the normal; $K$
   does not. Compare $|H|$ when verifying against a published value.
3. **Assuming $K$ depends on the embedding.** It does not — that is Gauss's
   theorem, and it is why a projection cannot fix distortion by "shaping" the map.
4. **Using a fixed step in degrees for a curvature calculation on a geographic
   grid.** The physical step varies as $\cos\varphi$, so the effective smoothing
   varies with latitude and mimics a real signal.
5. **Forgetting the slope-area correction.** Surface area on a $45°$ slope is
   $\sqrt2$ times the map area; terrain statistics that ignore this overstate
   roughness at low slopes and understate it at high ones.
6. **Treating a small dip or slope as negligible everywhere.** A nearly flat
   surface has a poorly determined dip *direction* and a well determined magnitude —
   the conditioning problem of
   [01-04-02 Section 7](./02-analytic-geometry.md), restated for curvature.
7. **Quoting Gaussian curvature in $\mathrm{km^{-2}}$ and $\mathrm{m^{-2}}$
   interchangeably.** The units differ by $10^{6}$, and both appear in print.

## 10. Real-world applications

- **Gravity gradients and eötvös tensors.** The second derivatives of the
  gravitational potential are curvature-like quantities; curvature attributes of
  the geoid and of gravity grids are used for structural interpretation and for
  airborne gravity gradiometry targets.
- **Seismic horizon attributes.** Dip, azimuth, curvature (most-positive,
  most-negative, Gaussian) are standard attributes in seismic interpretation and
  standard inputs to facies classification. Section 4 is the mathematics those
  attributes implement.
- **Terrain analysis.** Slope, aspect, profile and plan curvature, and the
  slope-area correction of Section 3, are the basics of digital terrain analysis
  used in hydrology, geomorphology and landslide susceptibility.
- **Levelling and engineering surveys.** The curvature and refraction corrections of
  Section 5.3 are applied to every long sight, and the horizon table decides whether
  a target is visible from a given instrument height.
- **Surface-wave ray tracing and tomography.** Geodesic deviation on a
  heterogeneous surface is the framework for treating path effects in regional
  tomography.
- **Potential-field modelling with topography.** Boundary-element and
  finite-difference codes must mesh a curved surface; the local curvature sets the
  accuracy of a flat-boundary approximation.

## 11. Further reading

- **do Carmo, M. P. (1976). *Differential Geometry of Curves and Surfaces*.
  Prentice-Hall.** Level: advanced undergraduate. The standard introduction; the
  treatment of the fundamental forms and Gauss's Theorema Egregium in Chapters 2–4
  is exactly this lesson's material with proofs.
- **Pressley, A. (2010). *Elementary Differential Geometry* (2nd ed.). Springer.**
  Level: intermediate. A gentler route to the same content, with many worked
  examples and the shape-operator viewpoint used in Section 4.
- **Struik, D. J. (1988). *Lectures on Classical Differential Geometry* (2nd ed.).
  Dover.** Level: advanced. Compact and geometric; useful for the intuition behind
  curvature invariants.
- **Florinsky, I. V. (2016). *Digital Terrain Analysis in Soil Science and
  Geology* (2nd ed.). Academic Press.** Level: intermediate. Curvature attributes
  for gridded data, with the finite-difference step-length question treated head-on
  as in Section 7.

> Note on citations: bibliographic details above are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> relying on them.

## 12. Related lessons

- [01-04-03 Cartesian, Cylindrical and Spherical Coordinates](./03-cartesian-spherical.md) —
  the parametrisations and the area elements used here.
- [01-04-04 Geographic Coordinates, Datums and Map Projections](./04-geographic-coordinates.md) —
  the operational consequences of $K \ne 0$.
- [01-04-02 Analytic Geometry: Lines, Planes and Distances](./02-analytic-geometry.md) —
  the flat-surface limit of everything in this lesson.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md) —
  the derivative machinery used informally here.
- [01-06-05 Line and Surface Integrals; Flux and Circulation](../06-multivariable-calculus/05-line-surface-integrals.md) —
  where $\sqrt{EG-F^{2}}$ becomes the surface measure in a flux integral.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — the geoid and its
  curvature as measured quantities.

## Exercises and self-assessment

Exercises are in
[`exercises/05-surfaces-and-curvature-exercises.md`](./exercises/05-surfaces-and-curvature-exercises.md),
with solutions in
[`exercises/05-surfaces-and-curvature-solutions.md`](./exercises/05-surfaces-and-curvature-solutions.md).

Before moving on, you should be able to:

- [ ] Compute $E$, $F$, $G$ for a sphere and for a graph, and write the area
      element from them.
- [ ] Derive $K = 1/R^{2}$ for a sphere from the two fundamental forms.
- [ ] Quote the graph formula for $K$ and use it on a paraboloid.
- [ ] State Gauss's Theorema Egregium and one consequence for map projections.
- [ ] Compute the drop below the tangent plane at 10 km and the horizon distance
      from a 2 m height.
- [ ] Explain, in two sentences, why a numerical second derivative has an optimal
      step length.
