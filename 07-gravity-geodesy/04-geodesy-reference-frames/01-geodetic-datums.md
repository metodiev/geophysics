---
id: 07-04-01
title: "Geodetic Datums, Ellipsoids and Coordinate Frames"
level: advanced
prereqs: ["07-01-03", "07-01-04"]
tags: [gravity, geodesy, datums, ellipsoid, coordinates, transformation]
---

# Geodetic Datums, Ellipsoids and Coordinate Frames

All models and data in this module are SYNTHETIC, with one exception: the WGS 84
ellipsoid parameters used below are the defining and derived constants of that
standard, quoted exactly. Every other ellipsoid, station, transformation and
shift in this module is a chosen teaching value; no real survey network is
referenced.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the derived constants of an ellipsoid from $a$ and $f$, and
   **evaluate** the principal radii of curvature at any latitude.
2. **Convert** between geodetic coordinates and geocentric Cartesian coordinates
   and **verify** the inverse to round-off.
3. **Derive** the relation between geodetic and geocentric latitude and
   **compute** their maximum separation.
4. **Quantify** the coordinate change produced by changing the ellipsoid without
   transforming the datum.
5. **Implement** the seven-parameter Helmert transformation, apply it, and
   **recover** its parameters from coordinate pairs.
6. **Relate** ellipsoidal height, orthometric height and geoid undulation, and
   **compute** the error introduced by using a single mean undulation.
7. **State** what a datum is, and why mixing coordinates from two datums is a
   defect rather than an approximation.

## Prerequisites

- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../01-gravity-fundamentals/03-normal-gravity.md) —
  the ellipsoid as the surface on which normal gravity is defined.
- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../01-gravity-fundamentals/04-gravity-reduction.md) —
  where station heights enter a gravity reduction.

## 1. What a datum is

A **geodetic datum** is a definition: an ellipsoid (two parameters), an origin
and orientation for the Cartesian frame attached to it, and a height reference.
Coordinates without a datum are numbers without units. Two consequences follow
immediately and are the substance of this lesson:

- **A coordinate is meaningless without its datum.** Converting a latitude by
  half a metre because you crossed a datum boundary is a real failure mode that
  has produced surveying disasters.
- **Changing the ellipsoid is not a coordinate change.** If you reinterpret the
  same numbers on a different ellipsoid, points move by hundreds of metres; if
  you transform the coordinates properly, they do not.

## 2. Ellipsoid geometry

An ellipsoid of revolution is fixed by two numbers. The standard pair is the
semi-major axis $a$ and the flattening $f$, from which

$$b = a(1-f), \qquad e^{2} = 2f - f^{2}, \qquad
e'^{2} = \frac{e^{2}}{1-e^{2}} .$$

For **WGS 84**, $a = 6378137.0\ \mathrm{m}$ and
$f = 1/298.257223563$ are defining constants, giving

| quantity | value | unit |
|---|---|---|
| $b$ | $6356752.3142$ | m |
| $e^{2}$ | $6.694379990141\times10^{-3}$ | — |
| $e'^{2}$ | $6.739496742276\times10^{-3}$ | — |
| $a-b$ | $21384.686$ | m |

The two principal radii of curvature at latitude $\varphi$ are the
**prime-vertical** and **meridional** radii

$$N(\varphi) = \frac{a}{\sqrt{1-e^{2}\sin^{2}\varphi}}, \qquad
M(\varphi) = \frac{a\,(1-e^{2})}{\left(1-e^{2}\sin^{2}\varphi\right)^{3/2}} .$$

| $\varphi$ (deg) | $N$ (m) | $M$ (m) | $\sqrt{MN}$ (m) |
|---|---|---|---|
| 0 | 6378137.0000 | 6335439.3273 | 6356752.3142 |
| 45 | 6388838.2901 | 6367381.8156 | 6378101.0302 |
| 90 | 6399593.6258 | 6399593.6258 | 6399593.6258 |

$N$ exceeds $M$ at every latitude below the pole, where the two become equal;
their difference is largest at the equator, $42697.7\ \mathrm{m}$. The third
column, the Gaussian radius $\sqrt{MN}$, is the one to use when a single radius
must stand in for the ellipsoid.

## 3. Geodetic to Cartesian and back

With latitude $\varphi$, longitude $\lambda$ and ellipsoidal height $h$,

$$X = (N+h)\cos\varphi\cos\lambda,\quad
Y = (N+h)\cos\varphi\sin\lambda,\quad
Z = \left(N(1-e^{2})+h\right)\sin\varphi .$$

The demonstration evaluates this for four synthetic points and inverts it by the
standard iteration (start from $\varphi = \arctan\left[Z/(p(1-e^{2}))\right]$ with
$p = \sqrt{X^{2}+Y^{2}}$, then
$\varphi \leftarrow \arctan\left[Z/(p(1-e^{2}N/(N+h)))\right]$). The round trip
returns latitude and height with errors of $0$ and $\le 1.4\times10^{-14}$ in
longitude — i.e. the inverse is exact to double precision after eight
iterations. **Always test an implementation this way**: a sign or quadrant error
in the inverse is otherwise invisible.

## 4. Geodetic versus geocentric latitude

The **geocentric** latitude is $\psi = \arctan(Z/p)$; the geodetic latitude is
normal to the ellipsoid. Eliminating the coordinates gives the exact relation

$$\tan\psi = \left(1-e^{2}\right)\tan\varphi,$$

so the two agree at the equator and the poles and differ by a maximum of

$$\varphi - \psi \approx \frac{e^{2}}{2}\ \text{rad}
= 0.003347\ \text{rad} = 11.5\ \text{arcmin}$$

at $\varphi = 45^{\circ}$ — about **21.4 km on the surface**, as the
demonstration's table shows ($11.545$ arcmin, $21.42\ \mathrm{km}$). This is the
single largest difference between two "latitudes" in geodesy, and it is why
gravity formulae that use $\sin^{2}\psi$ and maps that use $\varphi$ must never be
mixed.

## 5. Changing the ellipsoid without transforming

Take a synthetic datum B with $a = 6378000\ \mathrm{m}$, $f = 1/297$. Reinterpret
the same three coordinates on it and then express them on WGS 84:

| $\varphi$ (deg) | latitude shift (m) | height change (m) | longitude shift (deg) |
|---|---|---|---|
| 0 | 0.00 | $-137.00$ | $-3.6\times10^{-15}$ |
| 30 | $-78.26$ | $-159.46$ | 0 |
| 45 | $-90.37$ | $-181.95$ | $-3.6\times10^{-15}$ |
| 60 | $-78.26$ | $-204.49$ | $-3.6\times10^{-15}$ |
| 80 | $-30.91$ | $-224.34$ | $-3.6\times10^{-15}$ |

Latitude moves by up to $90\ \mathrm{m}$, height by more than $200\ \mathrm{m}$,
and **longitude does not move at all** — a change of rotationally symmetric
ellipsoid cannot displace a point east or west, and the $10^{-15}$ entries are
round-off. A datum is a definition, not a preference: reinterpreting numbers on
another ellipsoid is a coordinate *error* of hundreds of metres unless a proper
transformation accompanies it.

## 6. The seven-parameter Helmert transformation

To convert coordinates between two datums, use

$$\mathbf{X}' = \mathbf{T} + (1+s)\,\mathbf{R}\,\mathbf{X},$$

where $\mathbf{T}$ is a translation in metres, $s$ a dimensionless scale
difference of order $10^{-6}$ to $10^{-5}$, and $\mathbf{R}$ a rotation built
from three small angles in radians. For small angles the linearised model is

$$\mathbf{X}' - \mathbf{X} = \mathbf{T} + s\,\mathbf{X}
+ \boldsymbol{\varepsilon}\times\mathbf{X},$$

which is **linear in the seven parameters**, so they can be estimated from
coordinate pairs by ordinary least squares.

*Numerical example (SYNTHETIC).* With
$\mathbf{T} = (120,-80,200)\ \mathrm{m}$, rotations
$(0.5,-0.3,1.2)$ arcsec and $s = 2.0\times10^{-6}$, a point at
$\varphi = 45^{\circ}$, $\lambda = 16^{\circ}$, $h = 100\ \mathrm{m}$ shifts by
$254.654\ \mathrm{m}$; the shift varies from $249.005\ \mathrm{m}$ at the equator
to $257.541\ \mathrm{m}$ near the pole. Solving the linearised system from five
point pairs recovers

- $\mathbf{T} = (120.0000, -80.0000, 200.0000)\ \mathrm{m}$ (true exactly that),
- $s = 2.0000\times10^{-6}$ (true $2.0\times10^{-6}$),
- rotations $(0.5000, -0.3000, 1.2000)$ arcsec (true $(0.50,-0.30,1.20)$),

and re-applying the fitted parameters reproduces the transformed points to
$7.1\times10^{-5}\ \mathrm{m}$. The residual is the linearisation error of the
small-angle model, and it is eight orders of magnitude smaller than the
displacement.

## 7. Heights: $h = H + N$

Ellipsoidal height $h$ (from GNSS, relative to the ellipsoid), orthometric height
$H$ (from levelling, relative to the geoid) and geoid undulation $N$ are related
by

$$h = H + N .$$

Because $N$ is a surface, not a constant, the relation must be applied
point-by-point. The demonstration walks a $40\ \mathrm{km}$ line with a synthetic
geoid slope of $30\ \mathrm{mm\,km^{-1}}$:

| $x$ (km) | $H$ (m) | $N$ (m) | $h = H+N$ (m) |
|---|---|---|---|
| 0 | 100.00 | 45.000 | 145.00 |
| 20 | 121.05 | 45.600 | 166.65 |
| 40 | 145.20 | 46.200 | 191.40 |

The levelled rise is $45.20\ \mathrm{m}$ but the ellipsoidal rise is
$46.40\ \mathrm{m}$; the $1.200\ \mathrm{m}$ difference is exactly $\Delta N$.
Converting with a single mean undulation instead of the local value leaves an
error of up to **$600\ \mathrm{mm}$** at the ends of the line — ten times the
precision of a modern GNSS height. Height systems are the subject of
[02 Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](02-height-systems.md).

## 8. Assumptions and regime of validity

1. **The ellipsoid is a definition.** Changing $a$ or $f$ changes everything
   derived from it; no physical measurement chooses the ellipsoid.
2. **The Helmert model is a similarity transformation**: rigid translation,
   rotation and scale. Real datum differences include distortions that no
   seven-parameter set removes.
3. **Small-angle rotations.** The linearised form is valid to well below
   $1\ \mathrm{arcsec}$ of rotation; for larger angles use the exact rotation
   matrix and a non-linear solve.
4. **A geoid model for $N$.** The undulations used here are synthetic; a real
   conversion needs a published geoid model and its stated accuracy, which is
   usually the dominant error term.
5. **Coordinates are three-dimensional.** Converting only latitude and longitude
   and keeping the old height is a common and unnecessary error.
6. **Time.** A frame is defined at an epoch; velocities matter at the
   millimetre level, treated in
   [05 ITRF, Plate Motion Models and Frame Transformations](05-itrf-and-plate-models.md).

## 9. Physical interpretation

- The ellipsoid is a mathematical surface chosen to approximate the geoid. It has
  no physical existence, which is why a coordinate is only as meaningful as the
  datum it is attached to.
- The radii of curvature are what make geodesy non-Euclidean at the kilometre
  scale: a degree of latitude spans $110.6\ \mathrm{km}$ at the equator and
  $111.7\ \mathrm{km}$ near the poles, and a degree of longitude spans almost
  nothing at the poles.
- The geocentric/geodetic discrepancy is the same $e^{2}$ that controls the
  flattening of the gravity field: normal gravity changes by about
  $5186\ \mathrm{mGal}$ from equator to pole, and the geometric and gravitational
  flattenings are linked by Clairaut's theorem
  ([07-01-03](../01-gravity-fundamentals/03-normal-gravity.md)).
- Integration of a precise GNSS height with a national levelling network is
  impossible without a geoid model, and the geoid model, not the GNSS, is the
  limiting error.

## 10. Python demonstration

`code/geodetic_datums_demo.py` prints:

1. the derived ellipsoid constants and the curvature radii at three latitudes;
2. the geodetic-to-Cartesian table and the inverse round-trip errors;
3. the geodetic-versus-geocentric latitude table in arcminutes and kilometres;
4. the ellipsoid-change table;
5. the seven-parameter transformation, applied and inverted;
6. the $h = H + N$ line with the geoid-gradient error.

All output carries units; the script uses `np.random.default_rng(20261014)` and
exits 0.

## 11. Exercises

See
[`exercises/01-geodetic-datums-exercises.md`](./exercises/01-geodetic-datums-exercises.md)
and
[`exercises/01-geodetic-datums-solutions.md`](./exercises/01-geodetic-datums-solutions.md).

- **★** Compute $b$, $e^{2}$ and $e'^{2}$ for an ellipsoid with
  $a = 6378000\ \mathrm{m}$ and $f = 1/297$.
- **★** Compute $N$ and $M$ at $\varphi = 60^{\circ}$ on WGS 84.
- **★★** A point at $\varphi = 50^{\circ}$, $\lambda = 10^{\circ}$,
  $h = 500\ \mathrm{m}$: give its Cartesian coordinates and verify the inverse.
- **★★** Show that $\tan\psi = (1-e^{2})\tan\varphi$ and find the latitude at
  which the difference is maximal.
- **★★★** You have coordinates in datum B and a seven-parameter set to WGS 84.
  Estimate the error in a $10\ \mathrm{km}$ baseline from ignoring the scale term
  alone, and state whether it is detectable with GNSS.

## Mastery checkpoint

Without notes:

> A station has $\varphi = 45^{\circ}$, $\lambda = 15^{\circ}$,
> $h = 250\ \mathrm{m}$ on WGS 84, with $N = 44.0\ \mathrm{m}$ at the site.

**(a)** Compute $N(\varphi)$ and $M(\varphi)$ for WGS 84 at that latitude.
**(b)** Compute the Cartesian coordinates.
**(c)** Compute the orthometric height and state the datum it belongs to.
**(d)** The station's coordinates are reinterpreted on a synthetic ellipsoid with
$a$ smaller by $137\ \mathrm{m}$. Estimate the latitude and height error, and say
whether longitude changes.

## Common pitfalls

1. **Mixing datums.** A latitude without a datum is not a coordinate.
2. **Confusing geodetic and geocentric latitude.** Up to $11.5\ \mathrm{arcmin}$
   — 21 km.
3. **Treating $N$ as a constant.** The demonstration's line loses
   $600\ \mathrm{mm}$ at its ends.
4. **Ignoring the height in a horizontal conversion.** $N$ and $h$ both enter
   $X$, $Y$, $Z$.
5. **Applying a transformation in the wrong order or the wrong direction.**
   Inverse parameters are not the negatives of the forward ones.
6. **Assuming a seven-parameter transformation absorbs network distortion.** It
   does not; distortions need a grid or a full deformation model.

## 12. Applications

- **GNSS positioning and navigation.** Every fix is expressed in a datum; the
  broadcast datum differs from the survey datum in many countries.
- **Gravity reduction.** Free-air and Bouguer corrections use station heights,
  and the height system must be known
  ([07-01-04](../01-gravity-fundamentals/04-gravity-reduction.md)).
- **Map production and GIS.** Projections assume an ellipsoid; a wrong one
  misfits a basemap by tens of metres.
- **Datum modernisation.** Moving a country's coordinates to a global frame is a
  Helmert transformation plus a geoid model, and the geoid is the harder half
  ([07-07-02 Vertical Datum Modernisation and National Height Systems](../07-geoid-and-height-modern/02-vertical-datum-modernisation.md)).

## Related modules

- [02 Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](02-height-systems.md).
- [03 GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution](03-gnss-positioning.md).
- [05 ITRF, Plate Motion Models and Frame Transformations](05-itrf-and-plate-models.md).
- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../01-gravity-fundamentals/03-normal-gravity.md).
- [02-08-05 Equipotential Surfaces, Geoid and Level Surfaces](../../02-physics/08-potential-theory/05-equipotentials.md).

## 13. Self-assessment checklist

- [ ] I can compute $b$, $e^{2}$, $N(\varphi)$ and $M(\varphi)$.
- [ ] I can convert coordinates both ways and test the round trip.
- [ ] I can derive the geodetic/geocentric latitude relation.
- [ ] I can quantify the effect of reinterpreting coordinates on a new ellipsoid.
- [ ] I can apply and invert a seven-parameter transformation.
- [ ] I can assemble $h = H + N$ along a line and compute the error from using a
      mean $N$.
