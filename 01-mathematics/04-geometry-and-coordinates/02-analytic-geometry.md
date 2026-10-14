---
id: 01-04-02
title: "Analytic Geometry: Lines, Planes and Distances"
level: beginner
prereqs: ["01-04-01", "01-03-01"]
estimated_minutes: 75
tags: [analytic-geometry, planes, dip-strike, distances, vectors]
---

# Analytic Geometry: Lines, Planes and Distances

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** distances and mid-points in two and three dimensions, and write
   the equation of a line and of a plane in each of their standard forms.
2. **Obtain** the perpendicular distance from a point to a plane, and use it to
   answer the borehole-depth question that field interpretation actually asks.
3. **Determine** the dip, dip azimuth and strike of a plane from three points,
   and verify the result by a second, independent route.
4. **Find** the plunge and trend of the intersection line of two planes.
5. **Compute** the area of a polygon from its vertex coordinates, and explain why
   the shoelace formula works.
6. **State** the sign and convention decisions that make a normal-based
   calculation reproducible by someone else.

## Prerequisites

[01-04-01 Euclidean Geometry and Geometric Reasoning](./01-euclidean-geometry.md)
for the triangle and area results, and
[01-03-01 Angles, Triangles and the Unit Circle](../03-trigonometry/01-angles-and-triangles.md)
for the trigonometric functions that convert a normal vector into an angle.

## 1. Coordinates: geometry you can check

Synthetic geometry gives understanding; analytic geometry gives arithmetic. Once a
point has coordinates, every construction becomes a formula, and every formula can
be evaluated and cross-checked. In field and interpretation work the coordinates
are real survey numbers, so analytic geometry is what you actually use.

Everything below rests on three vector operations.

| Operation | Formula | Geometric meaning |
|---|---|---|
| dot product | $\mathbf{u}\cdot\mathbf{v} = u_xv_x + u_yv_y + u_zv_z$ | tests perpendicularity; gives projection |
| cross product | $\mathbf{u}\times\mathbf{v}$ | gives a vector perpendicular to both |
| norm | $\lvert\mathbf{u}\rvert = \sqrt{\mathbf{u}\cdot\mathbf{u}}$ | length |

The identities that earn their keep:

- $\mathbf{u}\cdot\mathbf{v} = \lvert\mathbf{u}\rvert\lvert\mathbf{v}\rvert\cos\theta$,
  where $\theta$ is the angle between them;
- $\lvert\mathbf{u}\times\mathbf{v}\rvert = \lvert\mathbf{u}\rvert\lvert\mathbf{v}\rvert\sin\theta$,
  so the cross-product magnitude is the area of the parallelogram they span;
- $\mathbf{u}\times\mathbf{v}$ is perpendicular to both, with a handedness fixed
  by the right-hand rule.

**Convention, stated once.** This module uses $(x, y, z) = (\text{east, north,
up})$,
a right-handed system, with azimuth measured clockwise from north and dip measured
downwards from the horizontal. Every result below is reproducible only if the
reader knows these three choices. **Write them down at the top of your own
working**; a large fraction of professional disagreement about a dip direction is
a convention disagreement.

## 2. Lines

A line in the plane through the point $(x_0, y_0)$ with direction vector
$(d_x, d_y)$ can be written

$$y - y_0 = m(x - x_0), \qquad m = \frac{d_y}{d_x},$$

or, avoiding the vertical-line special case,

$$a x + b y = c, \qquad (a, b) = \text{normal}, \qquad
d = \frac{\lvert a x_0 + b y_0 - c\rvert}{\sqrt{a^{2}+b^{2}}}$$

for the perpendicular distance from a point to the line.

**Why the normal form is the more useful one.** The "slope-intercept" form is
infinite for a vertical line, and its slope becomes ill-conditioned for a nearly
vertical one: a tiny change in $d_x$ produces an enormous change in $m$. The normal
form has no such singularity — the normal of a vertical line is simply horizontal
— and it is the form that generalises to planes in three dimensions. **Prefer the
form that has no special case**, especially in code.

## 3. Planes, and the three-point problem

A plane through a point $\mathbf{p}_0$ with unit normal $\mathbf{n}$ is the set of
$\mathbf{p}$ with

$$(\mathbf{p} - \mathbf{p}_0)\cdot\mathbf{n} = 0 .$$

Given three non-collinear points $\mathbf{p}_1, \mathbf{p}_2, \mathbf{p}_3$, the
normal is their cross product:

$$\mathbf{n} = \frac{(\mathbf{p}_2-\mathbf{p}_1)\times(\mathbf{p}_3-\mathbf{p}_1)}
{\lvert(\mathbf{p}_2-\mathbf{p}_1)\times(\mathbf{p}_3-\mathbf{p}_1)\rvert} .$$

### 3.1 From a normal to dip and dip azimuth

Convert $\mathbf{n} = (n_x, n_y, n_z)$ to a dip and a dip azimuth as follows.

1. **Force $n_z \ge 0$** by negating $\mathbf{n}$ if necessary. The plane has two
   normals, and this choice fixes which is used; with $n_z \ge 0$ the *upward*
   normal has a horizontal projection pointing **down-dip**.
2. **Dip** is the angle between the plane and the horizontal, which equals the
   angle between the normal and the vertical:

   $$\delta = \arccos(n_z) .$$
3. **Dip azimuth**, measured clockwise from north, is the azimuth of that
   horizontal projection:

   $$\theta = \operatorname{atan2}(n_x, n_y) \bmod 360° .$$
4. **Strike** is the line of intersection with the horizontal, perpendicular to
   the dip azimuth, and is conventionally reported in $[0°, 180°)$:

   $$\text{strike} = (\theta + 90°) \bmod 180° .$$

> **The 180° trap.** Using the *downward* normal ($n_z \le 0$) gives
> $\theta = \operatorname{atan2}(-n_x, -n_y)$, i.e. the dip azimuth rotated by
> exactly $180°$. The result is a plane dipping the wrong way, which in
> interpretation is not a small error: it moves the updip closure of a trap from
> one side of a structure to the other. **The fix is trivial and the consequence
> is not, so do the step-1 sign convention explicitly and test it on a synthetic
> plane** — which is exactly what the demonstration does.

### 3.2 Worked example with verification

Construct a plane with dip $30°$ towards azimuth $90°$: it descends to the east,
so $z$ decreases with increasing $x$. With the surface at $z = 100$ m at the
origin,

$$z = 100 - x\tan 30° .$$

Choose three points on it:

$$\mathbf{p}_1 = (0,\ 0,\ 100), \qquad
\mathbf{p}_2 = (1000,\ 0,\ -477.3503), \qquad
\mathbf{p}_3 = (0,\ 700,\ 100).$$

The demonstration recovers

```text
recovered: dip = 30.000000 deg, dip azimuth = 90.000000 deg, strike = 0.000000 deg
errors:    dip 3.553e-15 deg, azimuth 0.000e+00 deg
```

The dip error is four round-off units in the last place. The strike of $0°$ is
correct for an east-dipping plane: its strike line runs north–south, reported as
$000°$ (equivalently $180°$).

**Then do it again on a case with no axis alignment**, because synthetic tests
aligned with the axes hide sign errors:

$$\mathbf{q}_1 = (0,\ 0,\ 250), \quad
\mathbf{q}_2 = (800,\ 300,\ 180), \quad
\mathbf{q}_3 = (-200,\ 900,\ 305).$$

Two independent routes:

- cross product of two edge vectors →
  $\mathbf{n} = (0.101323616,\ -0.038235327,\ 0.994118496)$, giving
  dip $6.2172°$ and dip azimuth $110.6744°$;
- write the plane as $z = f(x, y)$ and take the direction of steepest descent of
  $f$, i.e. $(-\partial f/\partial x, -\partial f/\partial y)$, giving the same
  dip $6.2172°$ and the same azimuth $110.6744°$.

**Use two routes whenever the answer matters.** The cross-product route and the
gradient route share no intermediate quantity, so agreement is genuine evidence.
The next section uses these three points again, so their dip and azimuth are worth
remembering: **about $6.2°$ towards $110.7°$**, a nearly flat plane, which means its
dip azimuth is poorly determined (see Section 7).

## 4. Distance from a point to a plane

For a plane with unit normal $\mathbf{n}$ through $\mathbf{p}_0$, the signed
perpendicular distance from a point $\mathbf{p}$ is

$$D_{\perp} = (\mathbf{p} - \mathbf{p}_0)\cdot\mathbf{n} .$$

The sign tells you which side of the plane the point lies on — which is why the
$n_z \ge 0$ convention is worth fixing. With that convention, a positive
$D_{\perp}$ means the point is *above* the plane.

**The vertical distance** — how deep a borehole must go, or how far a well
missses a reflector — is the perpendicular distance divided by the vertical
component of the normal:

$$D_{\text{vert}} = \frac{D_{\perp}}{n_z} = \frac{D_{\perp}}{\cos\delta} .$$

Check the algebra: $\mathbf{p} - \mathbf{p}_0$ displaced purely downwards by $D$
has $z$-component $-D$, and $(\mathbf{p}-\mathbf{p}_0)\cdot\mathbf{n} = -D n_z$,
so $D_{\perp}/n_z = -D$, negative as it should be for a point below the plane.

**Do not divide by $\sin\delta$.** The vertical direction is related to the plane's
normal, not to its slope along the surface, so the factor is $\cos\delta$, i.e.
$n_z$ itself. This is the single most common dip-thickness error, and it is the
three-dimensional version of the thickness confusion in
[01-04-01 Section 3.1](./01-euclidean-geometry.md).

**Worked example**, continuing with the oblique plane
$\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3$ (dip $6.2172°$, azimuth $110.6744°$):

| test point $(x, y, z)$ | perpendicular distance (m) | vertical distance (m) |
|---|---|---|
| $(400, 400, 400)$ | $174.3531$ | $175.3846$ |
| $(0, 0, 100)$ | $-149.1178$ | $-150.0000$ |
| $(1000, 2000, 0)$ | $-223.6767$ | $-225.0000$ |

Read the third row as an interpretation: a proposed well at $(1000, 2000)$ with a
surface elevation of 0 m would meet the plane 225.0000 m below the surface, or the
plane lies 225 m *below* the well's top, depending on the sign convention you
established. Notice how close $D_{\text{vert}}$ is to $D_{\perp}$ here — because
$\cos 6.2172° = 0.994118$, so the two differ by 0.6 percent. **On a steep plane
the difference is large and the mistake is obvious; on a flat plane it is small and
the mistake is invisible.** That asymmetry is why the convention must be part of
your habit rather than something you re-derive when it looks wrong.

## 5. Two planes: the intersection line, plunge and trend

Geological structures are surfaces of different orientations, and the interesting
features are often where they meet: a fold axis where bedding and axial-plane
cleavage intersect, a lineation where a dyke cuts a bedding plane, the hinge line
of a fault-bounded block.

The intersection direction of two planes with unit normals $\mathbf{n}_1$ and
$\mathbf{n}_2$ is perpendicular to both:

$$\mathbf{L} = \frac{\mathbf{n}_1\times\mathbf{n}_2}
{\lvert\mathbf{n}_1\times\mathbf{n}_2\rvert} .$$

Convert a line direction to **plunge** (from the horizontal, positive downwards)
and **trend** (azimuth of the horizontal projection):

$$\text{plunge} = \arcsin\lvert L_z\rvert, \qquad
\text{trend} = \operatorname{atan2}(L_x, L_y)\bmod 360° .$$

For bedding dipping $35°$ towards $130°$ cut by a dyke dipping $75°$ towards $40°$,
the demonstration reports:

```text
bedding plane normal = (0.439385042, -0.368687826, 0.819152044)  [dip 35 towards 130]
dyke plane normal    = (0.620885153, 0.739942112, 0.258819045)  [dip 75 towards 40]
intersection line    = (-0.717867791, 0.404063693, 0.566920070)
plunge = 34.535731 deg, trend = 299.373700 deg (or 119.373700 deg for the opposite sense)
```

and verifies the result by checking that the line is perpendicular to both normals:

```text
validation: line dot bed normal  = 2.776e-17  (must be 0)
validation: line dot dyke normal = 2.776e-17  (must be 0)
```

Both dot products are round-off zero, which is the check that the cross product
was computed and normalised correctly.

**A trend is not unique.** A line has two opposite senses, so $299.373700°$ and
$119.373700°$ describe the same lineation. Convention: report the trend in
$[0°, 360°)$ from the computed direction and note the opposite sense if it matters.
For a fold axis it usually does not; for a shear-sense indicator it does.

## 6. Area from coordinates: the shoelace formula

For a polygon with vertices $(x_1, y_1), \dots, (x_n, y_n)$ in order around the
boundary, the signed area is

$$A = \frac12\left|\sum_{i=1}^{n}(x_i y_{i+1} - x_{i+1} y_i)\right|,
\qquad (x_{n+1}, y_{n+1}) = (x_1, y_1).$$

**Why it works.** Triangulate the polygon from the origin. Each triangle
$(0,0), (x_i, y_i), (x_{i+1}, y_{i+1})$ has signed area
$\tfrac12(x_i y_{i+1} - x_{i+1} y_i)$, using the cross product of the two edge
vectors. Triangles that fall outside the polygon are counted with the opposite
sign, and they cancel. The shoelace formula is therefore the cross-product area
formula from Section 1, summed.

This is how a lease boundary, a claim, or a grid-cell footprint is measured from
survey coordinates, and it is trivially implementable — the sign tells you whether
the vertices were listed clockwise or anticlockwise, which is a free check on the
data.

## 7. Conditioning: when an analytic answer is formally right and practically useless

The dip azimuth of the oblique plane above is $110.6744°$. Is that number
meaningful?

Suppose the three points are surveyed with $\pm0.1$ m vertical accuracy and
$\pm 0.3$ m horizontally — realistic for a differential GNSS survey. The plane's dip
is $6.2172°$, and the vertical scatter of the three points around the fitted plane
is of the order of
$\sqrt{(0.1)^{2} + (0.3\tan 6.2172°)^{2}} \approx 0.1$ m. Over a baseline of order
1000 m, an out-of-plane error of 0.1 m tilts the inferred normal by roughly
$0.1/1000$ rad $= 0.0057°$ — small for the dip, but the *azimuth* inherits the
error divided by the dip itself. For a plane of dip $\delta$, the azimuth
uncertainty behaves like $\sigma_\delta/\tan\delta$ for a dip uncertainty
$\sigma_\delta$, so at $\delta = 6.2°$ ($\tan\delta = 0.109$) it is amplified by a
factor of nine relative to the dip uncertainty.

**The lesson, stated without a formula.** A structure with a small dip has a
well-determined dip *magnitude* and a poorly determined dip *direction*, because
the direction of the steepest descent of a nearly flat surface is dominated by
noise. This is a genuine property of the geometry, not of your instrument or your
code. The same phenomenon appeared as the ill-conditioning of the apparent-dip
inversion in
[01-03-01](../03-trigonometry/01-angles-and-triangles.md) and as the conditioning
of $\arcsin$ in
[01-03-03](../03-trigonometry/03-inverse-trig.md). **If your structure is nearly
flat, constrain the direction from regional strike or from a map, and use the
three-point calculation for the magnitude only.**

## 8. Python demonstration

Run [`code/dip_strike_demo.py`](./code/dip_strike_demo.py). It uses only the
standard library and contains five sections: the three-point plane with its
round-trip validation and its independent gradient check; point-to-plane
distances; the two-plane intersection with plunge and trend; the curvature of the
Earth's surface; and numerically computed Gaussian and mean curvature.

Run it after writing your own implementation of `dip_and_strike` and compare the
two on the same three points. If your numbers agree to six figures on the oblique
case, your conventions match the ones stated in Section 1.

## 9. Common mistakes

1. **Using the downward normal.** Dip azimuth is $180°$ wrong, and nothing else in
   the arithmetic looks suspicious. Force $n_z \ge 0$ and test on a synthetic
   plane.
2. **Dividing by $\sin\delta$ instead of $\cos\delta$** when converting a
   perpendicular distance to a vertical one. At small dip the error is invisible;
   at $60°$ it is a factor of two.
3. **Assuming three points are non-collinear.** If they are, the cross product is
   zero and the normal is undefined. Check the magnitude against the point
   spacing, not against zero.
4. **Reporting a strike without saying it is a line.** Strike $020°$ and $200°$ are
   the same plane; the dip azimuth is the vector that has a direction.
5. **Treating a geometric distance as a drilling distance.** A deviated well
   follows a curve, not a perpendicular; the geometric answer is the minimum, and
   the actual intersection depends on the trajectory.
6. **Quoting a dip azimuth for a nearly flat plane without an uncertainty.** The
   azimuth is ill-conditioned there by construction.
7. **Mixing east/north with north/east in `atan2`.** A $90°$ rotation of the whole
   answer, easily mistaken for a geological result.

## 10. Real-world applications

- **Seismic interpretation and mapping.** Horizon grids are fitted planes and
  higher-order surfaces; dip, azimuth and curvature attributes are exactly the
  quantities of this lesson and the next.
- **Structural geology.** The three-point problem is the standard field method for
  obtaining an attitude from outcrop or borehole data, and the intersection of
  bedding with cleavage is the standard fold-axis construction.
- **Mineral exploration and mine planning.** Orebody boundaries, bench designs and
  grade-shell triangulations are polyhedra built from coordinate lists, with the
  shoelace formula and its three-dimensional equivalents doing the volume work.
- **Borehole targeting.** Section 4 is the calculation behind "how deep will this
  well intersect the target", and the sign convention decides whether you drill.
- **Geodesy and crustal deformation.** Fitting planes and lines to GNSS velocity
  fields recovers tilts and block rotations, and it has the same conditioning
  problem as Section 7.
- **Attributes for machine learning.** Dip and azimuth volumes are standard inputs
  to seismic facies classification, so the conventions of this lesson propagate
  into every downstream model.

## 11. Further reading

- **Coxeter, H. S. M. (1969). *Introduction to Geometry* (2nd ed.). Wiley.**
  Level: intermediate. Analytic and synthetic geometry side by side, which is
  useful when a formula looks arbitrary.
- **Groshong, R. H. (2006). *3-D Structural Geology* (2nd ed.). Springer.**
  Level: advanced. The three-point problem, plunge and trend, and the
  plunging-fold constructions, developed for interpretation work with the
  conventions stated explicitly.
- **Allmendinger, R. W., Cardozo, N. and Fisher, D. (2012). *Structural Geology
  Algorithms*.** Level: intermediate. Short, implementable algorithms for the
  attitude and intersection problems, with the mathematics exposed; open-access
  versions have been circulated, so verify the current source.
- **Marshak, S. and Mitra, G. (1988). *Basic Methods of Structural Geology*.
  Prentice-Hall.** Level: beginner to intermediate. The field procedures and the
  graphical constructions that the analytic formulas replace.

> Note on citations: bibliographic details above are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> relying on them.

## 12. Related lessons

- [01-04-01 Euclidean Geometry and Geometric Reasoning](./01-euclidean-geometry.md) —
  the synthetic results that these formulas implement.
- [01-04-03 Cartesian, Cylindrical and Spherical Coordinates](./03-cartesian-spherical.md) —
  the coordinate transformations that your survey data will need before Section 3
  can be applied.
- [01-03-03 Inverse Trigonometric Functions and Branch Ambiguity](../03-trigonometry/03-inverse-trig.md) —
  why the `atan2` in the dip-azimuth formula is not optional.
- [01-04-05 Surfaces, Parametrisation and Curvature](./05-surfaces-and-curvature.md) —
  the generalisation from planes to curved horizons.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md) —
  the gradient route used as the independent check in Section 3.2.

## Exercises and self-assessment

Exercises are in
[`exercises/02-analytic-geometry-exercises.md`](./exercises/02-analytic-geometry-exercises.md),
with solutions in
[`exercises/02-analytic-geometry-solutions.md`](./exercises/02-analytic-geometry-solutions.md).

Before moving on, you should be able to:

- [ ] Write the plane through three points with a cross product, and state the
      normal's sign convention you adopted.
- [ ] Convert a normal to dip, dip azimuth and strike, and check the result on a
      plane you constructed yourself.
- [ ] Compute the vertical distance from a point to a plane, and say why the
      divisor is $\cos\delta$ and not $\sin\delta$.
- [ ] Compute the plunge and trend of the intersection of two planes.
- [ ] Compute a polygon area from coordinates and state what the sign tells you.
- [ ] Explain why the dip azimuth of a nearly flat surface is poorly determined.
