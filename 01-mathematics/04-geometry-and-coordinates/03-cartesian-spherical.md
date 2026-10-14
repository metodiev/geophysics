---
id: 01-04-03
title: "Cartesian, Cylindrical and Spherical Coordinates"
level: intermediate
prereqs: ["01-04-02", "01-03-04"]
estimated_minutes: 75
tags: [coordinates, spherical, jacobian, ecef, direction-cosines]
---

# Cartesian, Cylindrical and Spherical Coordinates

## Learning objectives

By the end of this lesson you will be able to:

1. **Transform** freely between Cartesian, cylindrical and spherical coordinates,
   and verify any transformation by round trip.
2. **Write down** the volume element and the solid-angle element from the Jacobian
   of the transformation, rather than recalling them.
3. **Compute** the area of a spherical zone or cap, and check the result against a
   case whose answer is known exactly.
4. **Convert** geodetic latitude, longitude and height into geocentric rectangular
   coordinates (ECEF) on an ellipsoid, and recover the latitude.
5. **Explain**, with numbers, the difference between geodetic and geocentric
   latitude and why it matters for locating a measurement.
6. **Use** direction cosines for a ray or a take-off angle, and check that they
   describe a unit vector.
7. **Recognise** the coordinate singularity at the origin and on an axis, and
   choose a system that does not put a singularity where the physics is
   interesting.

## Prerequisites

[01-04-02 Analytic Geometry: Lines, Planes and Distances](./02-analytic-geometry.md)
for vectors and dot products, and
[01-03-04 Spherical Trigonometry and Great-Circle Geometry](../03-trigonometry/04-spherical-trigonometry.md)
for the spherical geometry that motivates the transformation into Cartesian form.

## 1. Why coordinate systems are a modelling choice

A coordinate system is a way of labelling points. Nothing about the Earth changes
when you relabel it, so the choice is purely a matter of convenience — but the
convenience is enormous, and it is not only aesthetic.

**Choose the system that matches the symmetry of the problem.** The temperature
field of a cooling sphere is a function of $r$ and $t$ alone in spherical
coordinates, and of $(x, y, z, t)$ with no useful structure in Cartesian ones.
The gravity field of a spherical Earth is a $1/r^{2}$ law in spherical
coordinates, and it has a square root in its Cartesian expression.

**Choose the system in which the boundary conditions are coordinate surfaces.**
This is the deeper reason. A differential equation is solved by separating
variables when the boundaries coincide with coordinate surfaces, which is why
Laplace's equation is separable in exactly eleven coordinate systems in three
dimensions and why those eleven appear again and again in physics.

**Choose the system that puts no singularity where the physics lives.** All
curvilinear systems have coordinate singularities — places where the Jacobian
vanishes or the coordinates are not unique. The origin is singular in both
cylindrical and spherical coordinates; the polar axis is singular in spherical
coordinates. If your survey straddles the pole, spherical coordinates will hurt.

## 2. The three systems, defined

Take a right-handed Cartesian frame $(x, y, z)$ with $z$ upwards. Three systems
are in constant use.

**Cartesian.** $(x, y, z)$. The metric is the identity:

$$ds^{2} = dx^{2} + dy^{2} + dz^{2}, \qquad dV = dx\,dy\,dz .$$

**Cylindrical.** $(\rho, \phi, z)$ with

$$x = \rho\cos\phi, \qquad y = \rho\sin\phi, \qquad z = z,$$

$\rho \ge 0$ the distance from the $z$-axis and $\phi$ the azimuth.

**Spherical.** $(r, \theta, \phi)$ with

$$x = r\sin\theta\cos\phi, \qquad y = r\sin\theta\sin\phi, \qquad z = r\cos\theta,$$

$r \ge 0$ the distance from the origin and $\theta$ the **colatitude**, measured
from the $+z$ axis. The inverse is

$$r = \sqrt{x^{2}+y^{2}+z^{2}}, \qquad
\theta = \operatorname{atan2}\!\left(\sqrt{x^{2}+y^{2}},\ z\right), \qquad
\phi = \operatorname{atan2}(y,\ x).$$

> **Convention warning, and it is the expensive one.** Geodesy and geomagnetism
> use **latitude**, $\varphi = 90° - \theta$, not colatitude. A formula written in
> the physics literature often means colatitude; the same symbol in a geodesy
> paper often means latitude. **Convert once, early, and keep the symbol names
> distinct** — use $\theta$ for colatitude and $\varphi$ for latitude throughout
> your code, as this module does. A latitude/colatitude mix-up at $60°$N is a
> $30°$ error, which relocates a station from Norway to the Sahara.

### 2.1 Round trips are the test

The demonstration transforms three points both ways and prints the original
alongside the recovered values:

```text
       x        y        z          r   theta (deg)   phi (deg)       rho               back (x,y,z)
   1.000    1.000    0.000    1.41421     90.000000   45.000000   1.41421  (   1.000,   1.000,   0.000)
   0.000    0.000    5.000    5.00000      0.000000    0.000000   0.00000  (   0.000,   0.000,   5.000)
  -3.000    4.000  -12.000   13.00000    157.380135  126.869898   5.00000  (  -3.000,   4.000, -12.000)
```

Every round trip returns its input to the printed precision. **Do this in your own
code**: a coordinate routine without a round-trip test is an untested routine, and
the failures are silent sign errors that look like geological anomalies.

Note the second row: on the polar axis ($x = y = 0$) the azimuth is *undefined*,
and `atan2(0, 0)` returns 0. The value is arbitrary — any azimuth would describe
the same point. That is a coordinate singularity, and it is not a bug in `atan2`.

## 3. Volume and solid-angle elements from the Jacobian

The Jacobian matrix of the spherical transformation is the matrix of partial
derivatives $\partial(x,y,z)/\partial(r,\theta,\phi)$:

$$J = \begin{pmatrix}
\sin\theta\cos\phi & r\cos\theta\cos\phi & -r\sin\theta\sin\phi \\
\sin\theta\sin\phi & r\cos\theta\sin\phi & \phantom{-}r\sin\theta\cos\phi \\
\cos\theta & -r\sin\theta & 0
\end{pmatrix}.$$

Its determinant is the local volume scale factor. Expanding (the algebra is
mechanical; the result is the standard one):

$$\det J = r^{2}\sin\theta, \qquad
dV = r^{2}\sin\theta\,dr\,d\theta\,d\phi .$$

Separating the angular part defines the **solid-angle element**

$$d\Omega = \sin\theta\,d\theta\,d\phi, \qquad
\int_{\text{sphere}} d\Omega
= \left(\int_0^{\pi}\sin\theta\,d\theta\right)\left(\int_0^{2\pi}d\phi\right)
= 2 \cdot 2\pi = 4\pi,$$

which is the definition of the steradian and the reason $4\pi$ appears in
spherically symmetric formulae everywhere.

The demonstration checks the volume element by integrating it over a full sphere
and comparing with the closed form:

```text
  integral of sin(theta) dtheta over [0, pi] = 2.0000000514   (exact 2)
  integral of r^2 dr over [0, R]             = 333.3333333333
  volume from the element                    = 4188.790312
  exact 4 pi R^3 / 3                         = 4188.790205
  relative difference                        = 2.570e-08
```

with $R = 10$. The residual $2.6\times10^{-8}$ is the discretisation error of the
midpoint rule on the $\theta$ integral — note that the quadrature gave
$2.0000000514$ rather than exactly 2, and that this same relative error propagates
straight through to the volume. **The error in an integral is the error in its
worst factor**, which is a useful habit when estimating the accuracy of a
numerical model.

**Why the factorisation matters physically.** That $\int_0^\pi \sin\theta\,d\theta$
and $\int_0^{2\pi}d\phi$ separate — that the angular part does not depend on $r$ —
is what lets you write the gravitational potential of a spherical body as a
one-dimensional radial integral times a constant. It is the reason spherical
harmonics are the natural basis for global fields, and it is the reason the Earth
being *almost* spherical is such a productive approximation: the coupling between
$r$ and the angles is small, so it can be treated as a perturbation.

### 3.1 Surface areas

Integrating the solid-angle element over a cap of half-angle $\alpha$ about the
pole gives the area

$$A = R^{2}\int_0^{2\pi}\!\!\int_0^{\alpha}\sin\theta\,d\theta\,d\phi
= 2\pi R^{2}(1 - \cos\alpha) .$$

The demonstration evaluates this and the corresponding numerical integral:

| $\alpha$ | Closed form (km²) | Numeric (km²) | Difference (km²) |
|---|---|---|---|
| $1°$ | 38842.752116 | 38842.752116 | $9.2\times10^{-9}$ |
| $5°$ | 970477.335101 | 970477.335102 | $7.7\times10^{-7}$ |
| $30°$ | 34167935.223338 | 34167935.224313 | $9.8\times10^{-4}$ |
| $90°$ | 255032940.486436 | 255032940.551984 | $6.6\times10^{-2}$ |

At $\alpha = 90°$ the cap is the northern hemisphere, $2\pi R^{2}$; the closed form
gives $255032940.486$ km², which is exactly half of $4\pi R^{2} = 510065880.973$
km². **Always check a general formula against a case whose answer you know
independently** — here, half the surface area of a sphere.

### 3.2 The chord identity, and the bridge to vector geometry

For two points separated by central angle $\Delta$ on a sphere of radius $R$, the
straight-line (chord) distance is

$$d_{\text{chord}} = 2R\sin\frac{\Delta}{2} .$$

This follows from the isosceles triangle whose equal sides are $R$ and whose apex
angle is $\Delta$: dropping the perpendicular bisects the apex angle and gives
$\sin(\Delta/2) = (d/2)/R$.

This single identity is what lets you compute great-circle distances with ordinary
three-dimensional vector arithmetic: convert both points to Cartesian, take the
difference, and use the identity to convert the chord length to a surface distance.
The demonstration verifies both routes:

```text
node (lat 45.0 N, lon 10.0 E, r 6371.0088 km) -> (4436.542703, 782.282180, 4504.983525) km
chord from Cartesian components  = 67.993045778 km
chord from 2 R sin(Delta/2)      = 67.993045778 km
difference                       = 5.649e-11 km
```

Agreement to $5.6\times10^{-8}$ m over a 68 km chord — the printed difference is
$5.6\times10^{-11}$ km, i.e. 56 nanometres. **Storing coordinates in Cartesian
form and using vector arithmetic is the numerically safest way to do
great-circle work**, which is why geodesy libraries keep three representations of
every point.

## 4. Geocentric rectangular coordinates from geodetic position

Now the practical case: a GNSS receiver reports **geodetic** latitude, longitude
and height above the ellipsoid. To combine that with a potential-field model, a
satellite orbit, or a geometric kernel, you need **geocentric** rectangular
coordinates (often called ECEF, for Earth-Centred Earth-Fixed).

**On a sphere of radius $a$** the transformation is immediate:

$$X = a\cos\varphi\cos\lambda, \qquad
Y = a\cos\varphi\sin\lambda, \qquad
Z = a\sin\varphi .$$

**On an ellipsoid with semi-major axis $a$ and first eccentricity squared
$e^{2}$**, the surface is not at constant distance from the centre, and the local
vertical does not pass through the centre. The correct transformation introduces
the **prime vertical radius of curvature**

$$N(\varphi) = \frac{a}{\sqrt{1 - e^{2}\sin^{2}\varphi}},$$

$$X = (N+h)\cos\varphi\cos\lambda, \qquad
Y = (N+h)\cos\varphi\sin\lambda, \qquad
Z = \left(N(1-e^{2}) + h\right)\sin\varphi .$$

The demonstration evaluates these for an ILLUSTRATIVE point at $40°$N, $20°$E,
$h = 0$:

```text
sphere of radius a = 6378.137 km:
  X = 4591.278387 km, Y = 1671.088670 km, Z = 4099.787436 km, |r| = 6378.137000 km

WGS84 ellipsoid, e^2 = 0.006694379990:
  prime-vertical radius N = 6386.976166 km
  X = 4597.641227 km, Y = 1673.404555 km, Z = 4077.985572 km
  geocentric radius = 6369.344863 km
  geocentric latitude = 39.810611 deg
  geodetic minus geocentric latitude = 0.189389 deg
```

Three things to take from this.

**The two latitudes differ.** The geodetic latitude is the angle of the local
vertical, which is what a level or a GNSS receiver measures. The geocentric
latitude is the angle of the radius vector, which is what a spherical model
naturally uses. They differ at $40°$N by $0.189389°$ — over 21 km of ground
distance. The relation between them follows from the transformation above:

$$\tan\varphi_{\text{geocentric}} = (1-e^{2})\tan\varphi_{\text{geodetic}} .$$

*Check at $45°$:* $(1-0.0066944)\times 1 = 0.9933056$, whose arctangent is
$44.807577°$ — $0.192423°$ below the geodetic value. The demonstration's table
confirms the pattern:

| geodetic latitude | geocentric latitude | difference | ground distance |
|---|---|---|---|
| $0°$ | 0.000000 | 0.000000 | 0.0 m |
| $15°$ | 14.904067 | 0.095933 | 10.61 km |
| $30°$ | 29.833636 | 0.166364 | 18.44 km |
| $45°$ | 44.807577 | 0.192423 | 21.38 km |
| $60°$ | 59.833076 | 0.166924 | 18.60 km |
| $75°$ | 74.903507 | 0.096493 | 10.77 km |
| $90°$ | 90.000000 | 0.000000 | 0.00 km |

The difference vanishes at the equator and the poles, and peaks near $45°$ at
$0.192423°$, which is $21.384$ km of ground. **That is a location error, not a
precision error**, and it is systematic in latitude, so it will not average away
in a survey.

**The geocentric radius varies.** At $40°$N the point on the ellipsoid is
$6369.345$ km from the centre, versus the equatorial $6378.137$ km and the polar
$6356.752$ km. If your potential-field code assumes a constant reference radius,
that assumption is wrong by 8.8 km at $40°$N — the difference between
$6378.137$ and $6369.345$.

**The inverse transformation is available in closed form.** Given $X$, $Y$, $Z$,
the geodetic latitude can be recovered iteratively or by a closed-form expression
involving an auxiliary angle. The demonstration uses the closed form and reports

```text
  geodetic latitude recovered by closed-form iteration = 40.000000000 deg
  recovery error = 0.000e+00 deg
```

An exact round trip is the standard acceptance test for an ECEF implementation.
Test it at a high latitude too, where the ill-conditioning of the inverse is worst:
near the pole the longitude becomes arbitrary and the latitude recovery becomes
sensitive.

## 5. Direction cosines and take-off angles

A direction in space is fixed by a unit vector, and its components are the cosines
of the angles it makes with the coordinate axes — hence **direction cosines**. For
a ray leaving a source with take-off angle $i$ from the downward vertical and
azimuth $A$ (clockwise from north), the horizontal unit vector is
$(\text{east},\ \text{north}) = (\sin A,\ \cos A)$, so in the
$(x, y, z) = (\text{east, north, up})$ frame

$$(l, m, n) = (\sin i\,\sin A,\ \sin i\,\cos A,\ -\cos i) .$$

Check the limits before trusting it, because the sine and cosine of the azimuth are
easy to swap: $i = 0$ gives $(0, 0, -1)$, straight down ✓; $i = 90°$ with $A = 0$
gives $(0, 1, 0)$, horizontally due **north** ✓; $i = 90°$ with $A = 90°$ gives
$(1, 0, 0)$, horizontally due **east** ✓. A swapped sine and cosine rotates every
direction by $90°$, which in seismology rotates radial into transverse and produces
an apparently reversed first motion. The demonstration tabulates the components for
a ray heading north and confirms $l^{2}+m^{2}+n^{2} = 1$ at every take-off angle:

```text
  take-off (deg)            l            m            n       sum sq
             0.0     0.000000     0.000000    -1.000000     1.000000
            30.0     0.000000     0.500000    -0.866025     1.000000
            45.0     0.000000     0.707107    -0.707107     1.000000
            60.0     0.000000     0.866025    -0.500000     1.000000
            89.0     0.000000     0.999848    -0.017452     1.000000
```

**The check that catches mistakes is the unit norm.** An error in a sign, a
degree/radian mix-up, or a mis-transcribed formula almost always breaks
$l^{2}+m^{2}+n^{2} = 1$, and the check costs nothing. Note that the magnitude of
the take-off angle controls only the split between $(l, m)$ and $n$; the azimuth is
carried in the ratio of the two horizontal components, which is again an `atan2`
problem.

## 6. Coordinate singularities: where the system lies to you

Both curvilinear systems in this lesson are singular somewhere, and the
singularities are not numerical curiosities — they are places where the
coordinates stop being a valid labelling.

| System | Singular set | Symptom |
|---|---|---|
| cylindrical | the $z$-axis ($\rho = 0$) | azimuth undefined; $dV \to 0$ |
| spherical | the origin ($r = 0$) | $\theta$ and $\phi$ both undefined |
| spherical | the polar axis ($\sin\theta = 0$) | azimuth undefined; $d\Omega \to 0$ |

**What the singularity does to a computation.**

- A grid in spherical coordinates becomes pathologically fine near the pole,
  because equal steps in $\phi$ correspond to vanishingly small distances. This is
  the *pole problem* of global grid design, and it is why operational
  weather and climate models use reduced grids, cubed spheres or spectral
  representations rather than a regular latitude–longitude grid.
- A differential equation solved in spherical coordinates acquires terms with
  $\sin\theta$ or $r$ in a denominator, whose limits must be evaluated separately
  at the axis.
- An interpolation in $(\theta, \phi)$ is anisotropic near the pole, because the
  physical spacing of grid points differs by a factor of $\sin\theta$ between the
  two directions.

**The remedy is the same in every case: change coordinates near the singularity.**
Use a local Cartesian frame for the polar cap, a Cartesian kernel for a
near-source calculation, or a harmonic basis that has no preferred axis. Choosing
a coordinate system badly does not merely make the code less elegant; it
introduces a scale-dependent error that grows exactly where the grid is finest.

## 7. Common mistakes

1. **Latitude versus colatitude.** The expensive one. Use distinct symbols and
   convert once.
2. **Forgetting that geodetic and geocentric latitude differ.** Up to $0.19°$, or
   21 km, near $45°$.
3. **Using the spherical radius where the ellipsoidal one is required**, or the
   reverse. At $40°$N the two differ by 8.8 km.
4. **Dividing by $\sin\theta$ or $r$ without checking the axis.** The stored
   $\sin\theta$ at the pole is about $6.1\times10^{-17}$, not zero, so the division
   "succeeds" and returns an enormous number.
5. **Assuming azimuth is defined on the polar axis.** It is not, and `atan2(0,0)`
   returning 0 is a convention, not an answer.
6. **Degenerate round trips.** Testing a transformation only at points on the
   coordinate axes, or only in the first octant, misses the sign errors that
   matter. Include negative coordinates and a point near each singularity.
7. **Mixing up the handedness.** Cartesian $(x, y, z)$ with $z$ up is right-handed
   only if $(x, y) = (\text{east, north})$ is taken in that order. The reverse
   gives a left-handed frame and reverses every cross product, which flips every
   normal and hence every dip azimuth.

## 8. Real-world applications

- **Gravity and magnetic modelling.** Spherical-harmonic synthesis is evaluated in
  geocentric coordinates at a reference radius, then rotated to geodetic for
  comparison with surface data. Section 4 is that conversion.
- **GNSS positioning and crustal deformation.** Every GNSS solution is in ECEF;
  velocities, strain rates and rotations are then expressed in a local east–north–up
  frame defined by the geodetic latitude.
- **Seismology.** Source and receiver coordinates are converted to Cartesian for
  close-in work and to spherical for global work; the take-off angle and direction
  cosines of Section 5 are the link to ray theory.
- **Global grids of any kind.** Ocean, atmosphere, gravity and magnetic grids all
  face the pole problem, and the choice of grid is a choice about which coordinate
  singularity to accept.
- **Orbit determination and satellite geodesy.** The equations of motion are
  Cartesian, the observables are geodetic, and the transformation between them is
  used in both directions at every epoch.
- **Radar and seismic interferometry.** Direction cosines convert a measured
  slowness vector into an incidence angle and an azimuth; getting the sign of $n$
  wrong reverses the apparent propagation direction.

## 9. Further reading

- **Arfken, G. B., Weber, H. J. and Harris, F. E. (2012). *Mathematical Methods
  for Physicists* (7th ed.). Academic Press.** Level: advanced. The curvature,
  scale factors and differential operators in the eleven separable coordinate
  systems, derived rather than tabulated.
- **Torge, W. and Müller, J. (2012). *Geodesy* (4th ed.). De Gruyter.** Level:
  advanced. Geodetic and geocentric coordinates, the ellipsoid and the
  transformations between them, with the conventions stated where the physics
  literature is ambiguous.
- **Hofmann-Wellenhof, B., Lichtenegger, H. and Wasle, E. (2008). *GNSS — Global
  Navigation Satellite Systems*. Springer.** Level: intermediate. The ECEF frame
  and coordinate transformations as they are actually implemented in positioning
  software.
- **Bomford, G. (1980). *Geodesy* (4th ed.). Oxford University Press.** Level:
  intermediate. A classic treatment of the prime vertical radius and the
  geodetic/geocentric distinction; editions and availability vary widely, so check
  a library.

> Note on citations: bibliographic details above are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> relying on them.

## 10. Related lessons

- [01-04-02 Analytic Geometry: Lines, Planes and Distances](./02-analytic-geometry.md) —
  the vector algebra that the transformations here use.
- [01-04-04 Geographic Coordinates, Datums and Map Projections](./04-geographic-coordinates.md) —
  the ellipsoid treated properly, with the datum and projection definitions.
- [01-03-04 Spherical Trigonometry and Great-Circle Geometry](../03-trigonometry/04-spherical-trigonometry.md) —
  the same geometry done without coordinates.
- [01-06-03 Jacobians, Coordinate Transformations and Volume Elements](../06-multivariable-calculus/03-jacobians.md) —
  the systematic theory of the Jacobian used in Section 3.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — where the reference
  ellipsoid and the geocentric/geodetic distinction become working infrastructure.

## Exercises and self-assessment

Exercises are in
[`exercises/03-cartesian-spherical-exercises.md`](./exercises/03-cartesian-spherical-exercises.md),
with solutions in
[`exercises/03-cartesian-spherical-solutions.md`](./exercises/03-cartesian-spherical-solutions.md).

Before moving on, you should be able to:

- [ ] Convert a point between all three systems in both directions, and state
      which conversion is ambiguous and at which points.
- [ ] Write the spherical volume element from the Jacobian, and evaluate the
      integral of $d\Omega$ over a sphere.
- [ ] Compute a spherical cap area and check it against the hemisphere value.
- [ ] Transform a geodetic position to ECEF without notes, and invert it.
- [ ] Quote the geodetic-minus-geocentric latitude at $45°$ and its equivalent
      ground distance.
- [ ] State a coordinate singularity and one way to avoid it.
