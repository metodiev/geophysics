---
id: 01-04-04
title: "Geographic Coordinates, Datums and Map Projections"
level: intermediate
prereqs: ["01-04-03", "01-03-04"]
estimated_minutes: 75
tags: [geodesy, datum, ellipsoid, map-projection, utm, distortion]
---

# Geographic Coordinates, Datums and Map Projections

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** what a geodetic datum is, and why a latitude and longitude without
   a datum name is an incomplete coordinate.
2. **Derive and evaluate** the WGS84 ellipsoid parameters from the two defining
   constants, and compute derived quantities correctly rather than quoting them.
3. **Compute** meridian arc lengths by integrating the radius of curvature, and
   state the length of a degree of latitude as a function of latitude.
4. **Quantify** the distortion of a conformal map projection, and explain the
   trade-off between preserving angles, distances and areas.
5. **State** the defining parameters of UTM and compute the scale factor at a
   given latitude and distance from the central meridian.
6. **Choose** a projection for a task, and state the projection and datum in every
   deliverable.

## Prerequisites

[01-04-03 Cartesian, Cylindrical and Spherical Coordinates](./03-cartesian-spherical.md)
for the coordinate transformations and the prime vertical radius, and
[01-03-04 Spherical Trigonometry and Great-Circle Geometry](../03-trigonometry/04-spherical-trigonometry.md)
for what the spherical approximation costs.

## 1. A datum is a definition, not a fact

A **geodetic datum** specifies:

1. an **ellipsoid**: a semi-major axis $a$ and a flattening $f$;
2. an **origin and orientation**: where the ellipsoid sits relative to the Earth's
   centre of mass and how its axes are aligned;
3. for a modern datum, a **realisation**: the actual coordinates of a set of
   physical stations that define the frame in practice.

Two consequences follow, and both are routinely ignored.

**The same physical point has different coordinates in different datums.** The
difference can reach hundreds of metres for older national datums, because their
origin was chosen to fit the local geoid rather than to be geocentric. Consequently
a latitude and longitude *without a datum name* is not a position; it is a number
awaiting a definition.

**A datum can change between survey epochs** because the stations move. Modern
global frames are plate-fixed or plate-motion-corrected, and a coordinate quoted
in a frame that has been superseded is systematically offset from current
coordinates by the accumulated motion. **Always record the datum and the epoch in
your data files**, and record them in the file's metadata rather than in a
colleague's memory.

This lesson uses **WGS84** throughout, because it is the datum most often
encountered in global data products, and it is defined by two exact constants.

## 2. The ellipsoid, built from two numbers

WGS84 is defined by a semi-major axis and an inverse flattening, both exact by
definition of the datum:

$$a = 6378137\ \text{m} = 6378.137\ \text{km}, \qquad
\frac{1}{f} = 298.257223563 .$$

Everything else is derived. The demonstration prints the chain:

```text
a  (semi-major axis)        = 6378.137 km      (exact by definition)
1/f (inverse flattening)    = 298.257223563      (exact by definition)
f  (flattening)             = 3.352810664747480e-03
e^2 (first eccentricity^2)  = 0.006694379990
b  (semi-minor axis, = a(1-f)) = 6356.752314 km
e'^2 (second eccentricity^2)   = 0.006739497
a - b (polar flattening)    = 21.384686 km
```

The relations used:

$$f = \frac{1}{298.257223563} = 3.3528106647\times10^{-3}, \qquad
e^{2} = f(2-f) = 6.694379990\times10^{-3},$$

$$b = a(1-f) = 6356.752314\ \text{km}, \qquad
e'^{2} = \frac{a^{2}-b^{2}}{b^{2}} = 6.739497\times10^{-3},$$

$$a - b = 21.384686\ \text{km} .$$

**The flattening is a small number and its effect is not.** The polar radius is
21.4 km shorter than the equatorial one — about 0.34 percent. That is the
difference between a sphere of radius 6371.009 km (the arithmetic mean) and the
real shape, and Section 6 shows what it costs in map distortion and in geodesic
distance.

**Quote which quantities are definitions.** $a$ and $1/f$ are exact; $b$, $e^{2}$,
$e'^{2}$ and the mean radius are computed. If a published value disagrees with
yours in the seventh digit, the cause is an assumed mean radius or a different
ellipsoid, not a different Earth.

## 3. Meridian arcs: how long is a degree of latitude?

The Earth's surface curves least along a meridian near the poles and most near the
equator, so a degree of latitude is not a constant length. The radius of curvature
in the meridian is

$$M(\varphi) = \frac{a(1-e^{2})}{\left(1 - e^{2}\sin^{2}\varphi\right)^{3/2}},$$

and the meridian distance from the equator to latitude $\varphi$ is

$$\text{Arc}(\varphi) = \int_0^{\varphi} M(\varphi')\,d\varphi' .$$

There is no elementary closed form for this integral, but the integrand is smooth
and a Simpson rule converges quickly. The demonstration integrates with 200 000
intervals and reports:

| latitude | $dM/d\varphi$ (km per degree) | cumulative arc from equator (km) |
|---|---|---|
| $0°$ | 110.574276 | 0.000 |
| $15°$ | 110.648696 | 1658.990 |
| $30°$ | 110.852442 | 3320.113 |
| $45°$ | 111.131777 | 4984.944 |
| $60°$ | 111.412287 | 6654.073 |
| $75°$ | 111.618384 | 8326.938 |
| $90°$ | 111.693980 | **10001.966** |

**Three readings of that table.**

- A degree of latitude grows from $110.574276$ km at the equator to $111.693980$
  km at the pole — a spread of 1 percent. **Any conversion that uses a single
  number of kilometres per degree has a 1 percent error, i.e. 1 km per 100 km
  travelled**, and it is systematic in latitude, so it does not average out.
- The quarter meridian is **10001.966 km** (measured from the equator to the pole
  along a meridian). The historical definition of the metre was one ten-millionth
  of that distance, which by the modern ellipsoid is

  $$\frac{10001966\ \text{m}}{10^{7}} = 1000.196573\ \text{m},$$

  i.e. about 0.20 m longer than the metre as now defined. **State this carefully**:
  it says that the *meridian definition* corresponds to a unit 0.02 percent longer
  than today's metre. It says nothing about the accuracy of the 18th-century
  measurement, which was a separate exercise with its own errors.
- The integral is the only honest way to get a meridian distance. The series
  expansions that appear in textbooks are accurate to a stated order, and their
  truncation error is the same size as the 1 percent latitude variation you are
  trying to capture if you keep too few terms — so either keep enough terms or
  integrate.

### 3.1 Radii of curvature, and why one number cannot describe the Earth

The curvature of the ellipsoid differs in the north–south and east–west
directions:

$$M(\varphi) = \frac{a(1-e^{2})}{\left(1 - e^{2}\sin^{2}\varphi\right)^{3/2}}
\quad\text{(meridional)}, \qquad
N(\varphi) = \frac{a}{\left(1 - e^{2}\sin^{2}\varphi\right)^{1/2}}
\quad\text{(prime vertical)} .$$

| latitude | $M$ (km) | $N$ (km) | $\sqrt{MN}$ (km) | $N - M$ (km) |
|---|---|---|---|---|
| $0°$ | 6335.439327 | 6378.137000 | 6356.752314 | 42.697673 |
| $30°$ | 6351.377104 | 6383.480918 | 6367.408778 | 32.103814 |
| $45°$ | 6367.381816 | 6388.838290 | 6378.101030 | 21.456475 |
| $60°$ | 6383.453857 | 6394.209174 | 6388.829252 | 10.755317 |
| $90°$ | 6399.593626 | 6399.593626 | 6399.593626 | 0.000000 |

Three facts worth carrying away.

- **$N - M$ reaches 42.7 km at the equator** and vanishes at the poles. The two
  curvatures differ by more than half a percent, which is why an east–west survey
  and a north–south survey at the same place do not have the same scale.
- **$N$ at the equator equals $a$** ($6378.137000$ km) and **$M$ at the pole equals
  $a^{2}/b$** ($6399.593626$ km, the polar radius of curvature). Both are exact
  identities you can use as unit tests.
- **$\sqrt{MN}$ is the geometric mean radius**, $6356.752314$ km at the equator —
  exactly the semi-minor axis there. This is the radius of the conformal sphere
  that a spherical transverse Mercator uses as its first approximation, which is
  why the Gaussian mean radius appears in projection software.

## 4. Longitude: one degree is not a fixed distance

A degree of longitude spans

$$\Delta\lambda\text{ in km} = \frac{2\pi a}{360°}\cos\varphi
\approx 111.3195\cos\varphi\ \text{km},$$

using the equatorial radius. So:

| latitude | 1° of longitude |
|---|---|
| $0°$ | 111.32 km |
| $30°$ | 96.41 km |
| $45°$ | 78.71 km |
| $60°$ | 55.66 km |
| $80°$ | 19.33 km |

(Compute each as $111.3195\cos\varphi$; at $80°$, for example,
$111.3195 \times 0.1736482 = 19.33$ km.)

**This is the single most common source of factor-of-two errors in regional work**,
because it is invisible in a north–south survey and enormous in an east–west one.
The exact factor also depends on $N(\varphi)$ rather than $a$, which is why the
$1.5$ percent difference between the equatorial and prime-vertical radii appears
in precise work.

## 5. Map projections: choosing which lie to tell

A projection maps the ellipsoid to a plane. Since the sphere (let alone the
ellipsoid) has positive Gaussian curvature and the plane has zero, **no projection
can preserve all distances, all areas and all angles**. This is a theorem, not a
limitation of cartography, and any projection *must* lie about at least one of
them.

| Class | Preserves | Sacrifices | Typical use |
|---|---|---|---|
| conformal | angles, locally the shape of small features | area and distance | survey networks, navigation, UTM |
| equal-area | area exactly | angles and shape | regional statistics, gridded potential fields |
| equidistant | distance from one or two lines/points | everything else | special-purpose displays |

### 5.1 Mercator, and how bad it gets

The spherical Mercator projection is

$$x = R\lambda, \qquad y = R\ln\tan\!\left(\frac{\pi}{4} + \frac{\varphi}{2}\right) .$$

It is conformal, and its local scale factor at latitude $\varphi$ is exactly

$$k = \sec\varphi = \frac{1}{\cos\varphi},$$

with the area scale factor $k^{2} = \sec^{2}\varphi$. The demonstration measures
this by finite differences rather than quoting it:

| latitude | $1/\cos\varphi$ | measured scale | area inflation |
|---|---|---|---|
| $0°$ | 1.000000 | 1.000000 | 1.0000 |
| $30°$ | 1.154701 | 1.154701 | 1.3333 |
| $45°$ | 1.414214 | 1.414214 | 2.0000 |
| $60°$ | 2.000000 | 2.000000 | 4.0000 |
| $75°$ | 3.863703 | 3.863703 | 14.9282 |
| $80°$ | 5.758770 | 5.758770 | 33.1634 |
| $85°$ | 11.473713 | 11.473713 | 131.6461 |

The measured and analytic columns agree to six decimals, which is the check that
the projection is conformal with the stated scale. **At $60°$ every length is
doubled and every area quadrupled; at $80°$ every area is inflated by a factor of
33; at $85°$ by 132.** The familiar complaint that "Greenland looks as big as
Africa" is a complaint about area, and it is quantitatively correct.

**Practical rule.** Mercator is excellent for navigation — a straight line of
constant bearing is a straight line on the map — and useless for area statistics
poleward of about $60°$. Use an equal-area projection there.

### 5.2 Transverse Mercator and UTM

The transverse Mercator is the same construction applied to a meridian instead of
the equator: the central meridian is a straight line of true scale times a chosen
central scale factor $k_0$, and distortion grows with distance from it. On the
sphere it is

$$x = k_0R\,\operatorname{atanh}(\cos\varphi\sin\lambda), \qquad
y = k_0R\,\operatorname{atan2}(\tan\varphi,\ \cos\lambda),$$

with $\lambda$ measured from the central meridian, and on the ellipsoid the algebra
is longer but has the same structure: exact scale $k_0$ on the central meridian,
growing with distance from it, and conformal everywhere.

**UTM** (Universal Transverse Mercator) is the standard global realisation:

- 60 zones, each **6° of longitude** wide, so a zone's central meridian is at most
  **3° from any point inside it**;
- a central scale factor of **$k_0 = 0.9996$** — deliberately less than 1;
- a **false easting of 500 000 m**, so that all eastings inside a zone are positive;
- a **false northing of 0 m in the northern hemisphere** and
  **10 000 000 m in the southern hemisphere**, for the same reason.

**Why $k_0 = 0.9996$ rather than 1.** The demonstration measures the scale factor
of the spherical transverse Mercator along the equator and the central meridian:

| latitude | $\lambda$ from CM | $k$ along meridian | $k$ along parallel | scale error (percent) |
|---|---|---|---|---|
| $0°$ | $0°$ | 0.999600000 | 0.999600000 | $-0.040000$ |
| $0°$ | $3°$ | 1.000971797 | 1.000971823 | $+0.097180$ |
| $30°$ | $0°$ | 0.999600000 | 0.999600000 | $-0.040000$ |
| $30°$ | $3°$ | 1.000628318 | 1.000628338 | $+0.062832$ |
| $60°$ | $3°$ | 0.999942420 | 0.999942427 | $-0.005758$ |
| $80°$ | $3°$ | 0.999641282 | 0.999641283 | $-0.035872$ |

Three observations.

- **The two columns agree at every row.** The transverse Mercator is conformal, so
  a single number describes the local distortion in every direction.
- **On the central meridian the scale is exactly $k_0$.** This is by construction,
  and it is the test that a projection implementation is right.
- **Choosing $k_0 = 0.9996$ balances the error.** At the central meridian the map
  is 0.04 percent too small; at the equator near the zone edge it is about 0.097
  percent too large. With $k_0 = 1$ the error would only ever be positive and would
  reach $+0.137$ percent at the zone edge at the equator. Balancing the sign of the
  error halves the worst case, and that is the entire purpose of the 0.9996.

**Be precise about what was computed.** The table above is the *spherical*
transverse Mercator; real UTM is defined on the ellipsoid, where the numbers differ
slightly and the structure is identical. Also confirm the UTM parameters against
the current official specification for the datum you are using before quoting them
in a deliverable — the parameters above are the standard ones, but standards are
revised.

### 5.3 What distortion means for your data

A scale error of 0.1 percent is 1 m in 1 km. That sounds harmless, and for many
purposes it is. But:

- a **10 km** grid spacing mis-stated by 0.1 percent is 10 m of station position,
  which is larger than the accuracy of many surveys;
- an **area** mis-stated by 0.1 percent in linear scale is 0.2 percent in area,
  because area scales as the square;
- a **strain rate** computed by differencing projected coordinates inherits the
  *gradient* of the scale factor, not its value, and the gradient is what
  accumulates across a zone.

**The habit that prevents all of this.** State, in every deliverable: the datum,
the projection and its parameters, the area of interest, and the expected
distortion at the edge of that area. Four items, one sentence, and it makes your
work reproducible and your errors bounded.

## 6. Sphere or ellipsoid? A decision procedure

The question is quantitative, and the numbers are in this module.

| Quantity | Difference |
|---|---|
| Earth radius: equatorial $a$ vs mean $R$ | 7.1 km |
| Earth radius: mean $R$ vs polar $b$ | 14.3 km |
| Geodetic vs geocentric latitude at $45°$ | $0.192° = 21.4$ km |
| Degree of latitude: equator vs pole | 1.12 km |
| $N - M$ at the equator | 42.7 km |
| Ellipsoidal vs spherical distance, oblique 5 600 km path | 15.0 km |
| Ellipsoidal vs spherical distance, meridional 10° path | $-0.63$ km |

**Decision procedure.**

1. Convert the difference into the quantity you will interpret (a travel time, a
   strain, an area, a survey length).
2. Compare with your measurement uncertainty.
3. If the difference is more than a third of that uncertainty, use the ellipsoid;
   otherwise state that you checked, and proceed on the sphere.

This is the same question as
[01-03-04 Section 6](../03-trigonometry/04-spherical-trigonometry.md), asked with
the ellipsoidal machinery now available to answer it properly. Note the trap
identified there: **the largest percentage correction can occur on the shortest
path**, because what matters is the local radius of curvature rather than the
global mean.

## 7. Python demonstration

Run [`code/geodesy_projection_demo.py`](./code/geodesy_projection_demo.py). It has
six sections: WGS84 parameters; meridian arcs and the quarter meridian; the
meridional and prime-vertical radii of curvature; Mercator conformality and the
secant blow-up; the transverse Mercator scale table and the UTM parameters; and a
summary of what a projection preserves. It uses only the standard library, and it
computes every number quoted above rather than printing a table from a file.

## 8. Common mistakes

1. **Quoting coordinates without a datum.** A position without a datum is not a
   position. This is the most consequential habit in the lesson.
2. **Using one number of kilometres per degree of latitude.** The error is 1
   percent, reaching 1.12 km per degree between equator and pole.
3. **Forgetting the $\cos\varphi$ in longitude.** A degree of longitude is 111.32
   km at the equator and 19.33 km at $80°$N.
4. **Believing a projected map preserves distance.** Conformal projections preserve
   angles; distance is preserved only on the lines of true scale.
5. **Comparing areas measured on a Mercator map.** At $60°$ the area inflation is a
   factor of 4; at $85°$ it is 132.
6. **Assuming a datum is a fact rather than a definition.** The same point has
   different coordinates in different datums, by up to hundreds of metres for older
   national systems.
7. **Mixing datums within a dataset.** Two surveys in different datums, merged
   without transformation, produce a systematic offset that looks like a geological
   trend.
8. **Forgetting that $k_0$ is not 1 in UTM.** All UTM distances are 0.04 percent
   short on the central meridian by construction.

## 9. Real-world applications

- **Any GIS deliverable.** Projection and datum are metadata requirements, and the
  reason a "reprojection" step exists in every workflow.
- **Global gravity and magnetic models.** Spherical-harmonic coefficients are
  referenced to a specific ellipsoid and a specific normal field; synthesising them
  onto a projected grid requires both the datum transformation and the projection,
  in that order.
- **Marine and airborne surveys.** Navigation and positioning are geodetic; the
  survey's internal geometry is usually projected. Crossing between the two is
  where the errors enter, and Section 5.3 quantifies them.
- **GNSS-based deformation monitoring.** Velocities are computed in a plate-fixed
  frame and reported in a projection or in local east–north–up coordinates; the
  choice determines whether a real strain signal is visible.
- **Seismic network geometry.** Array design, beamforming and back-azimuth
  determination all depend on the correct great-circle or geodesic separations, and
  the sphere-versus-ellipsoid decision of Section 6 is made exactly here.
- **Cartographic products for the public.** Every web map is in a projected frame
  — commonly a variant of Mercator — and the resulting area distortion is present
  in every published figure even if the authors never mention it.

## 10. Further reading

- **Snyder, J. P. (1987). *Map Projections — A Working Manual*. USGS Professional
  Paper 1395.** Level: intermediate. The standard reference for projection formulas
  and their distortion; a public-domain USGS report.
- **Torge, W. and Müller, J. (2012). *Geodesy* (4th ed.). De Gruyter.** Level:
  advanced. Datums, reference frames, ellipsoid geometry and the geodetic
  boundary-value problem.
- **Bomford, G. (1980). *Geodesy* (4th ed.). Oxford University Press.** Level:
  intermediate. The classical treatment of arc measurement, meridional curvature
  and the history of the meridian definition of the metre.
- **Iliffe, J. (2000). *Datums and Map Projections for Remote Sensing, GIS and
  Surveying*. Whittles.** Level: intermediate. A practical, example-driven account
  aimed at users rather than geodesists. Verify the current edition.
- **BIPM.** *The International System of Units (SI)*, current edition. Level:
  reference. The modern definition of the metre, which superseded the meridian
  definition discussed in Section 3.

> Note on citations: bibliographic details above are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> relying on them.

## 11. Related lessons

- [01-04-03 Cartesian, Cylindrical and Spherical Coordinates](./03-cartesian-spherical.md) —
  the geodetic-to-geocentric transformation and the prime vertical radius $N$ used
  throughout this lesson.
- [01-03-04 Spherical Trigonometry and Great-Circle Geometry](../03-trigonometry/04-spherical-trigonometry.md) —
  the sphere-versus-ellipsoid comparison, with the Vincenty validation.
- [01-04-05 Surfaces, Parametrisation and Curvature](./05-surfaces-and-curvature.md) —
  why a projection cannot preserve both angles and areas: curvature is intrinsic.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — the geoid, normal
  gravity fields and the reference ellipsoids in operational use.
- [17-remote-sensing-gis](../../17-remote-sensing-gis/README.md) — coordinate
  reference systems, reprojection and georeferenced raster handling.

## Exercises and self-assessment

Exercises are in
[`exercises/04-geographic-coordinates-exercises.md`](./exercises/04-geographic-coordinates-exercises.md),
with solutions in
[`exercises/04-geographic-coordinates-solutions.md`](./exercises/04-geographic-coordinates-solutions.md).

Before moving on, you should be able to:

- [ ] Derive $f$, $e^{2}$, $b$ and $a-b$ from $a$ and $1/f$, and compute them.
- [ ] State the length of a degree of latitude at the equator and at the pole, and
      explain the 1 percent variation.
- [ ] Compute the meridian arc to a given latitude by numerical integration, and
      check it against the quarter meridian.
- [ ] State the Mercator scale factor at $60°$ and the resulting area inflation.
- [ ] List the four standard UTM parameters and explain the purpose of $k_0 = 0.9996$.
- [ ] Reproduce the decision procedure of Section 6 for a specific measurement.
