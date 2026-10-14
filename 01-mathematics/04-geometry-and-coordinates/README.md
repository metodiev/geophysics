# Module 01-04 — Geometry and Coordinate Systems

**Stages:** beginner → advanced · **Prerequisites:** [01-01 Arithmetic](../01-arithmetic/README.md),
[01-03 Trigonometry](../03-trigonometry/README.md)

Every number in geophysics carries a position. A gravity reading without
coordinates is an anecdote; a travel-time residual binned by distance is a
velocity model; a magnetic anomaly contoured on the wrong projection is a false
trend. This module supplies the geometry and the coordinate machinery that turn
measurements into located, comparable, map-able quantities, and it is explicit
about where each coordinate system breaks down and by how much.

## Learning objectives

By the end of this module you will be able to:

1. Reason with similar triangles, angle sums, polygons and circles, and use the
   area formulas — including Heron's — with confidence in their derivations.
2. Work analytically with lines, planes and distances in three dimensions, and
   obtain dip and dip azimuth of a plane from three points.
3. Transform freely between Cartesian, cylindrical and spherical coordinates,
   and write down the correct volume and solid-angle elements without looking
   them up.
4. Compute geocentric (ECEF) coordinates from geodetic latitude, and explain the
   difference between geodetic and geocentric latitude, with numbers.
5. Explain what a datum is, compute meridian arcs and radii of curvature on an
   ellipsoid, and quantify the distortion of a conformal map projection.
6. Parametrise a surface, compute its first and second fundamental forms, and
   obtain its Gaussian and mean curvature.
7. State, for each of the above, the situation in which the approximation is
   inadequate and the size of the error it introduces.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Euclidean Geometry and Geometric Reasoning](./01-euclidean-geometry.md) | beginner | Similarity and area do most of the work in practice |
| 02 | [Analytic Geometry: Lines, Planes and Distances](./02-analytic-geometry.md) | beginner | Coordinates turn geometry into arithmetic you can check |
| 03 | [Cartesian, Cylindrical and Spherical Coordinates](./03-cartesian-spherical.md) | intermediate | The right coordinate system removes the singularity from the problem |
| 04 | [Geographic Coordinates, Datums and Map Projections](./04-geographic-coordinates.md) | intermediate | A datum is a definition; a projection is a deliberate distortion |
| 05 | [Surfaces, Parametrisation and Curvature](./05-surfaces-and-curvature.md) | advanced | Curvature is intrinsic, and the Earth's is a signal |

## Suggested path

**If you are starting out:** lessons 01 and 02 in order, then 03. Lesson 01 is
elementary but not trivial — the derivation habits matter later. Skip 05 on a
first pass.

**If you already work with coordinates daily:** start at
[01-04-03](./03-cartesian-spherical.md), and check yourself with exercise ★★6 of
that lesson (the geodetic-versus-geocentric latitude table). Practitioners very
often have a latent convention error there, and it is worth an hour to rule it
out. Then work
[01-04-04](./04-geographic-coordinates.md) exercise ★★★9 on projection
distortion.

**If you are heading into potential fields, geodesy or modelling:** work
[01-04-05](./05-surfaces-and-curvature.md) carefully. The machinery there — the
first and second fundamental forms — is the same machinery as the surface
Laplacian and the boundary conditions of a potential-field solution.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-euclidean-geometry.md`](./01-euclidean-geometry.md) | Lesson 01 — triangles, similarity, circles, area |
| [`02-analytic-geometry.md`](./02-analytic-geometry.md) | Lesson 02 — lines, planes, distances, the three-point problem |
| [`03-cartesian-spherical.md`](./03-cartesian-spherical.md) | Lesson 03 — coordinate transforms, Jacobians, ECEF, direction cosines |
| [`04-geographic-coordinates.md`](./04-geographic-coordinates.md) | Lesson 04 — datums, ellipsoid geometry, map projections |
| [`05-surfaces-and-curvature.md`](./05-surfaces-and-curvature.md) | Lesson 05 — parametrisation and curvature |
| [`exercises/`](./exercises) | Graded exercises and full solutions for every lesson |
| [`code/coordinate_systems_demo.py`](./code/coordinate_systems_demo.py) | Round-trip transforms, ECEF, cap areas, chord identity |
| [`code/geodesy_projection_demo.py`](./code/geodesy_projection_demo.py) | WGS84 parameters, meridian arcs, Mercator and transverse Mercator distortion |
| [`code/dip_strike_demo.py`](./code/dip_strike_demo.py) | Three-point planes, distances, plane intersections, curvature |

All three demonstrations use only the Python standard library.

## Verified reference results

These numbers were produced by the demonstrations in this module. Use them to
check any implementation you write.

| Quantity | Value | Where |
|---|---|---|
| Triangle $b=4$, $c=5$, $A=60°$: area by Heron and by $\tfrac12bc\sin A$ | $8.660254037844$ both ways | lesson 01 |
| Spherical cap of half-angle $30°$ on $R = 6371.0088$ km | $3.4167935\times10^{7}$ km² | lesson 01, lesson 03 |
| Solid-angle element integrated over a sphere of radius 10 | volume $4188.790312$ vs exact $4188.790205$ (rel. $2.6\times10^{-8}$) | lesson 03 |
| Point $(40°\text{N}, 20°\text{E})$: geodetic minus geocentric latitude | $0.189389°$ | lesson 03 |
| Same point on WGS84: ECEF | $(4597.641227, 1673.404555, 4077.985572)$ km | lesson 03 |
| Geodetic latitude recovered from ECEF | $40.000000000°$ (error $0$) | lesson 03 |
| Max geodetic minus geocentric latitude at $45°$ | $0.192423° = 21.3843$ km | lesson 03 |
| Meridian arc per degree, equator to pole | $110.574276$ to $111.693980$ km | lesson 04 |
| Quarter meridian, WGS84 | $10001.966$ km | lesson 04 |
| Mercator scale factor at $60°$N | $2.000000$, area inflation $4.0000$ | lesson 04 |
| Spherical transverse Mercator scale at $45°$N, $6°$ from central meridian | $1.002342$ | lesson 04 |
| Three-point plane: dip/dip azimuth, round trip | $30.000000°$ towards $090.000000°$ | lesson 02 |
| Two planes: plunge/trend of the intersection line | $34.535731°$ / $299.373700°$ | lesson 02 |
| Earth curvature drop over 10 km | $7.848049$ m (parabolic $7.848051$ m) | lesson 05 |
| Gaussian curvature of a sphere, numeric vs $1/R^{2}$ | agree to 8 significant figures | lesson 05 |

Coordinates, anomalies and depths quoted in the lessons are marked SYNTHETIC or
ILLUSTRATIVE. Ellipsoidal quantities use WGS84 with $a = 6378137$ m and
$1/f = 298.257223563$, both exact by definition of the datum.

## Mastery checkpoint

Work this without notes.

> A buried planar reflector is picked at three points on a surface grid, in
> (east, north, up) metres: $(0, 0, 250)$, $(800, 300, 180)$ and $(-200, 900, 305)$.
> **(a)** Find its dip and dip azimuth, and verify your answer by a second method.
> **(b)** A borehole is planned at $(400, 400, 400)$. How far below the surface
> will it intersect the reflector, measured vertically?
> **(c)** The same reflector is to be mapped on a UTM grid. At $45°$N, $6°$ from
> the zone's central meridian, the projection scale factor is $1.002342$. By how
> much would a 10 km grid spacing be mis-stated, and would that change your
> interpretation of (a)?
> **(d)** State one quantity computed above whose value would change if the Earth
> were treated as an ellipsoid instead of a sphere of radius $6371.0088$ km, and
> estimate the size of the change.

Worked versions of (a) and (b) are in the
[lesson 02 solutions](./exercises/02-analytic-geometry-solutions.md), exercise
★★6.

## Common pitfalls across this module

1. **Swapping latitude and longitude, or east and north.** Every downstream
   number looks plausible; only a plot reveals it.
2. **Confusing geodetic with geocentric latitude.** Up to $0.19°$, which is 21 km.
3. **Using geocentric coordinates when the data are on an ellipsoid**, or the
   reverse. State the datum.
4. **Assuming a projected map preserves distance.** It preserves angles, and the
   scale factor varies with position.
5. **Forgetting that curvature enters area quadratically and length linearly.** A
   1 percent length error is a 2 percent area error.
6. **Treating "flat" as the default for long baselines.** At 100 km the Earth
   drops 785 m below its tangent plane, which is larger than most targets.

## Related modules

- [01-03 Trigonometry and Periodic Phenomena](../03-trigonometry/README.md) —
  the spherical geometry and azimuth conventions this module relies on.
- [01-06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md) —
  gradients, Jacobians and surface integrals, of which lesson 05 is the geometric
  foundation.
- [01-09 Partial Differential Equations](../09-partial-differential-equations/README.md) —
  Laplace's equation in curvilinear coordinates, which needs the metric of lesson 05.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — geoids, reference
  ellipsoids and spherical harmonics in practice.
- [17-remote-sensing-gis](../../17-remote-sensing-gis/README.md) — projections,
  reprojection and coordinate reference systems as working tools.
