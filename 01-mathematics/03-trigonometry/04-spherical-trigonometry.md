---
id: 01-03-04
title: "Spherical Trigonometry and Great-Circle Geometry"
level: intermediate
prereqs: ["01-03-01", "01-03-03"]
estimated_minutes: 75
tags: [spherical-trigonometry, geodesy, great-circle, epicentral-distance, azimuth]
---

# Spherical Trigonometry and Great-Circle Geometry

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a great circle, a spherical angle and a spherical triangle, and say
   how each differs from its plane counterpart.
2. **Derive** the spherical law of cosines from a dot product, and the spherical
   law of sines from the same configuration.
3. **Compute** a great-circle distance three independent ways, and explain which
   formula is numerically safe for which range of separations.
4. **Compute** a forward azimuth and a back-azimuth, and explain why they do not
   differ by exactly $180°$ in general.
5. **Convert** an angular separation into kilometres and into an epicentral
   distance for a spherical Earth.
6. **Quantify** the error introduced by treating the Earth as a sphere, and say
   when that error matters.

## Prerequisites

[01-03-01 Angles, Triangles and the Unit Circle](./01-angles-and-triangles.md)
for the two plane laws, and
[01-03-03 Inverse Trigonometric Functions and Branch Ambiguity](./03-inverse-trig.md)
for `atan2`, without which the azimuth formulas are unusable.

## 1. Why the sphere, and when the sphere is enough

The Earth is not a sphere. It is an oblate ellipsoid, flatter at the poles by
about 21.4 km, and the geoid departs from that ellipsoid by tens of metres. So why
start with spherical trigonometry?

Three reasons, in the order that matters.

**It is closed-form.** Every quantity below has an elementary formula, so you can
compute an answer and, more importantly, check it. Ellipsoidal geodesics require
iteration (Section 6), and a numerical algorithm you cannot check by hand is a
poor first tool.

**The error is bounded and known.** We will measure it, not guess it. For a
10 000 km separation the spherical distance differs from the WGS84 geodesic by
about 0.11 percent, and for a 5 600 km path by about 0.27 percent. When your
tolerance is coarser than that, the sphere is not an approximation you have to
apologise for.

**Most of geophysics uses it.** Epicentral distances are reported in degrees on a
sphere, station azimuths are computed with spherical formulas, gridded
potential-field data are stored on a sphere at a reference radius, and the
spherical-Earth normal modes and ray parameterisation are spherical by
construction.

## 2. Definitions: sphere, great circle, spherical triangle

Fix a sphere of radius $R$. A **great circle** is the intersection of the sphere
with a plane through the centre. It is the largest circle that fits on the
sphere, it has circumference $2\pi R$, and — the property that matters — it is
the *shortest* path between any two of its points, provided the points are not
antipodal.

**Coordinates.** A point is fixed by a co-latitude $\theta$ from the north pole
and a longitude $\lambda$; or, in geodesy, by a latitude
$\varphi = 90° - \theta$ and a longitude. This module uses latitude and longitude
because that is what data files contain:

$$x = R\cos\varphi\cos\lambda, \qquad
y = R\cos\varphi\sin\lambda, \qquad
z = R\sin\varphi .$$

**Angular separation.** The angle $\Delta$ subtended at the centre by two points.
It is the arc length in radians, so the ground distance is $R\Delta$.

**Spherical triangle.** Three points joined by arcs of great circles. Three facts
distinguish it from a plane triangle:

1. Each *side* is an angle — the central angle it subtends — so sides and angles
   are measured in the same units. This is why geophysicists say an "epicentral
   distance of $45°$" without embarrassment.
2. The angle sum exceeds $180°$. The excess $E = A + B + C - \pi$ is called the
   **spherical excess**.
3. The excess is not a rounding effect: the area of the triangle is $ER^{2}$. On
   a sphere of unit radius, excess and area are numerically the same thing.

The demonstration makes (2) and (3) concrete for the octant triangle:

```text
  angle sum = 270.000000000 deg   (flat-plane value: 180)
  excess E  = 1.570796327 rad = 90.000000000 deg
  area E*R^2 = 6.3758e+07 km^2
  exact octant area pi*R^2/2 = 6.3758e+07 km^2
```

An octant has three right angles, so its angle sum is $270°$ and its excess is
$\pi/2$ rad; the area is therefore $\pi R^{2}/2$, one eighth of $4\pi R^{2}$.
The two last lines are the same number computed two different ways, which is the
verification that the excess really is the area.

## 3. The spherical law of cosines, derived

Place the north pole at the top and fix the convention that latitude $\varphi$
runs from $-90°$ to $+90°$ and longitude $\lambda$ increases eastwards. The unit
vector to a point is

$$\mathbf{u}(\varphi, \lambda) = (\cos\varphi\cos\lambda,\
\cos\varphi\sin\lambda,\ \sin\varphi).$$

**Deployment.** Let $C$ be a triangle's vertex, and let $a = \Delta_{BC}$,
$b = \Delta_{AC}$, $c = \Delta_{AB}$ be the sides. The **spherical law of
cosines** states

$$\boxed{\cos c = \cos a\cos b + \sin a\sin b\cos C}.$$

**Derivation by dot product.** Choose the coordinates so that $C$ is at the north
pole, $(\varphi,\lambda) = (90°, 0°)$. Rotate about the polar axis so that vertex
$A$ lies at longitude $0$. Then

$$C = (0, 0, 1), \qquad
A = (\sin b,\, 0,\, \cos b), \qquad
B = (\sin a\cos C,\ \sin a\sin C,\ \cos a),$$

because the colatitude of $A$ is $b$ and that of $B$ is $a$, and the angle
between the meridians at $C$ is the spherical angle $C$. The central angle $c$
satisfies $\cos c = A \cdot B$ because both are unit vectors. Evaluating:

$$A\cdot B = \sin b\,\sin a\cos C + 0 + \cos b\,\cos a,$$

which is the stated formula. **The entire law of cosines for a sphere is one dot
product once the coordinates are chosen well.**

*Check the plane limit.* For small sides, expand
$\cos x \approx 1 - x^{2}/2$ and $\sin x \approx x$:

$$1 - \frac{c^{2}}{2} \approx \left(1 - \frac{a^{2}}{2}\right)\left(1 - \frac{b^{2}}{2}\right)
+ ab\cos C
\ \Longrightarrow\
c^{2} \approx a^{2} + b^{2} - 2ab\cos C,$$

the plane law of cosines. The sphere contains the plane triangle, in the limit of
small triangles. That is a healthy consistency check on any spherical formula you
derive: shrink it and see whether the plane result falls out.

**The polar-triangle case, which is the one you will use daily.** If $C$ is the
north pole, then $a = 90° - \varphi_2$, $b = 90° - \varphi_1$, $c = \Delta$ and
$C = \Delta\lambda$, the difference in longitude. Substituting gives the standard
formula for the angular separation of two points:

$$\boxed{\cos\Delta = \sin\varphi_1\sin\varphi_2
+ \cos\varphi_1\cos\varphi_2\cos\Delta\lambda}.$$

Read that as a triangle with one vertex at the pole: the sides from the pole are
the co-latitudes.

### 3.1 The spherical law of sines

The same configuration gives

$$\boxed{\frac{\sin a}{\sin A} = \frac{\sin b}{\sin B} = \frac{\sin c}{\sin C}},$$

the common ratio being

$$K = \frac{\sin a\,\sin b\,\sin c}
{\sqrt{1 - \cos^{2}a - \cos^{2}b - \cos^{2}c + 2\cos a\cos b\cos c}} .$$

The square root is the determinant of the three unit position vectors — twice
the volume of the tetrahedron they span — so the identity is a statement about
the geometry of the triangle, not a coincidence of the algebra. It is the
spherical analogue of the circumdiameter $2R$ in the plane, in the sense that it
is determined by the three sides alone.

The demonstration tests the cosine rule and the three sine ratios on a triangle
with no convenient corner, constructing it from latitude–longitude vertices and
computing interior angles from tangent directions at each vertex:

```text
vertices (lat, lon): (10.0, 0.0), (60.0, 20.0), (35.0, 95.0)
  side a (opposite A) = 52.933766340 deg
  side b (opposite B) = 88.321490312 deg
  side c (opposite C) = 52.186586316 deg
  angle A = 42.223053436 deg, B = 122.665992756 deg, C = 41.708559287 deg
  angle sum = 206.597605480 deg

spherical law of cosines: cos c = 0.61309202237960, cos a cos b + sin a sin b cos C = 0.61309202237960
difference = 0.000e+00
spherical law of sines: a/sin A = 1.187376772866
spherical law of sines: b/sin B = 1.187376772866
spherical law of sines: c/sin C = 1.187376772866
```

The cosine rule holds to the printed fourteen digits, the three sine ratios agree
to twelve, and the closed form for the common ratio reproduces them to
$4.4\times10^{-16}$:

```text
common ratio from a/sin A                 = 1.187376772866
common ratio from sin a sin b sin c / det = 1.187376772866
difference = 4.441e-16   (det = 0.530674624857)
```

The angle sum exceeds $180°$ by $26.5976°$ — an excess of $0.46422$ rad,
corresponding to an area of $1.884\times10^{7}$ km² on a sphere of radius
6371.0088 km. **A triangle covering that much ground cannot be solved with plane
trigonometry**, which is the practical reason this lesson exists.

## 4. One distance, three formulas — and which to use

The central angle can be computed three ways, all mathematically equivalent and
numerically very different.

**Arccosine form.** $\Delta = \arccos(\sin\varphi_1\sin\varphi_2
+ \cos\varphi_1\cos\varphi_2\cos\Delta\lambda)$.

**Haversine form.** With
$h = \sin^{2}(\Delta\varphi/2) + \cos\varphi_1\cos\varphi_2\sin^{2}(\Delta\lambda/2)$,

$$\Delta = 2\arcsin\sqrt{h}.$$

**Vector form.** Convert both points to unit vectors and compute
$\Delta = \operatorname{atan2}(|\mathbf{u}_1\times\mathbf{u}_2|,
\mathbf{u}_1\cdot\mathbf{u}_2)$.

The demonstration compares them:

```text
pair                                  acos (deg)     haversine        vector
Equator to 90 E on the equator      90.000000000  90.000000000  90.000000000
Same meridian, 10 deg apart         10.000000000  10.000000000  10.000000000
London-ish to New York-ish          50.117438869  50.117438869  50.117438869
Antipodal pair                     180.000000000 180.000000000 180.000000000
```

### 4.1 Where the arccosine form fails

For small separations $\cos\Delta$ is within about $10^{-14}$ of 1, while double
precision carries an absolute resolution of only $2.2\times10^{-16}$ there. The
subtraction $1 - \cos\Delta$ loses most of its significant figures, and
$\arccos$ amplifies whatever is left. The demonstration measures it:

```text
   separation           acos (m)      haversine (m)    acos error
       1.0 m           1.000207           1.000000     2.068e-04
      10.0 m           9.999815          10.000000    -1.849e-05
     100.0 m          99.999999         100.000000    -1.105e-08
    1000.0 m         999.999999        1000.000000    -1.024e-09
   10000.0 m       10000.000000       10000.000000     2.095e-11
```

At 1 m the arccosine form returns 1.000207 m — a 0.02 percent error from a
formula that is algebraically exact. Haversine never forms the difference, so it
is accurate at every scale. **Use haversine.** The arccosine form survives in
textbooks and in legacy code because it is the shortest to write down.

### 4.2 The failure of the vector form

The vector form is the most accurate of the three for short baselines and the
least accurate near the antipode, because it relies on $|\mathbf{u}_1\times
\mathbf{u}_2| = \sin\Delta$, which vanishes as $\Delta \to \pi$. Use it when you
already have Cartesian vectors (see
[01-04-03 Cartesian, Cylindrical and Spherical Coordinates](../04-geometry-and-coordinates/03-cartesian-spherical.md))
and you know the points are not nearly antipodal.

**The habit worth building.** Compute a distance two ways and compare. It costs
three lines and it catches the class of error that is otherwise invisible — a
swapped $\varphi$ and $\lambda$, a sign convention for western longitude, or a
mix-up between colatitude and latitude.

## 5. Azimuth and back-azimuth

The **forward azimuth** — the initial heading of the great-circle path — is

$$\boxed{\theta = \operatorname{atan2}\!\left(
\sin\Delta\lambda\cos\varphi_2,\
\cos\varphi_1\sin\varphi_2 - \sin\varphi_1\cos\varphi_2\cos\Delta\lambda
\right)} .$$

The first argument is the "east" component and the second the "north" component,
so $90°$ is due east and $180°$ due south, matching the surveying convention.

The demonstration checks the four cardinal cases and an oblique pair:

```text
          from             to  azimuth (deg)   back-azimuth
         0N 0E         0N 90E         90.000        270.000
         0N 0E         10N 0E          0.000        180.000
         0N 0E         10S 0E        180.000          0.000
         0N 0E         0N 90W        270.000         90.000
        source        station        230.418         49.505
```

Everything checks by hand in the first four rows. The last row is the point: the
source at $38.00°$N, $25.00°$E and the station at $37.00°$N, $23.50°$E (round
numbers chosen for clarity, not real locations) give a station-to-source azimuth
of $230.418°$ and a source-to-station azimuth of $49.505°$.

### 5.1 Why back-azimuth is not azimuth plus 180°

On a plane, walking east and then reversing means walking due west: the two
headings differ by exactly $180°$. On a sphere this is true only if the path stays
on a meridian. A great circle between two points crosses successive meridians at
changing angles, except when both points share a longitude. So the forward and
reverse azimuths are supplementary only for a north–south path; for any other
path they differ from that by an amount that grows with the latitude span and the
longitude span.

The correct statement is directional: at the receiver, the back-azimuth is the
azimuth *from the receiver to the source*, computed with the same formula and the
arguments swapped. Never subtract $180°$ and hope.

**Terminology.** Seismologists usually quote the back-azimuth from the *station*
to the *event*, and the forward azimuth from the *event* to the *station*. Because
the two differ for oblique paths, a paper's "azimuth" is ambiguous until you know
which end it is measured from. Say which, always.

## 6. The ellipsoid: how much does the sphere cost?

The sphere is an approximation. To measure its price, the demonstration implements
the inverse Vincenty iteration for the geodesic distance on an ellipsoid and
first validates it in a case where the answer is known: setting the flattening to
zero must reproduce the sphere exactly.

```text
Validation: with f = 0 Vincenty must reproduce haversine exactly.
  Equator to 90 E on the equator     vincenty(f=0) = 10007.543398 km   haversine = 10007.543398 km   diff = 1.819e-12 km
  Same meridian, 10 deg apart        vincenty(f=0) =  1111.949266 km   haversine =  1111.949266 km   diff = -2.274e-13 km
  London-ish to New York-ish         vincenty(f=0) =  5572.804939 km   haversine =  5572.804939 km   diff = 0.000e+00 km

Now with the WGS84 flattening, which is the real shape of the Earth:
  Equator to 90 E on the equator     spherical =  10007.5572 km   WGS84 = 10018.7542 km   diff =  +11.1970 km  (+0.1118 percent)
  Same meridian, 10 deg apart        spherical =   1111.9508 km   WGS84 =  1111.3180 km   diff =   -0.6328 km  (-0.0569 percent)
  London-ish to New York-ish         spherical =   5572.8126 km   WGS84 =  5587.8195 km   diff =  +15.0069 km  (+0.2686 percent)
```

Read the second block carefully, because it contains a trap.

- The 10 000 km equatorial path is **longer** on the ellipsoid: the equatorial
  radius exceeds the mean radius.
- The same-meridian path is **shorter**: a meridional path at mid latitudes lies
  inside the mean sphere.
- The oblique path is longer by the largest percentage.

The sphere is a one-parameter model being asked to describe a two-parameter
figure, so the sign of the error depends on the geometry of the path. Precisely
because of this, the parenthetical percentages above are specific to the three
paths printed; do not quote them as universal conversion factors.

**Rule of thumb for the three families of measurement in this curriculum.**

| Scale | Sphere error | Verdict |
|---|---|---|
| Local survey, < 50 km | far below a metre except for the equatorial case | sphere is fine |
| Regional, few hundred km | order 1 km | check before publishing |
| Global, > 1000 km | 10–20 km, i.e. seconds of S-wave time | use an ellipsoidal geodesic |

For an epicentral distance the last row matters: a 15 km error is roughly
2 seconds of $S$-wave travel at 8 km/s, which is comparable to or larger than the
pick uncertainty of a good arrival. If your location or travel-time residual
budget is at the second level, the sphere is not adequate.

## 7. Practical Python demonstration

Run [`code/spherical_geometry_demo.py`](./code/spherical_geometry_demo.py). It
uses only the standard library. The seven sections in order: three-formula
distance comparison; a precision study of the arccosine form; epicentral
distance; azimuth and back-azimuth; spherical excess; the ellipsoidal geodesic
with its sphere-limit validation; and an outright verification of the spherical
cosine and sine rules on a general triangle.

For the illustrative pair, the epicentral distance work reads:

```text
source   (lat, lon) = (38.0000, 25.0000)
station  (lat, lon) = (37.0000, 23.5000)
epicentral distance  = 1.554362 deg
                     = 172.837 km  (sphere of radius 6371.0088 km)
                     = 0.02712874 rad
```

Note the conversion: $1.554362° \times (\pi/180) \times 6371.0088\ \text{km}
= 172.837$ km. An angular distance in degrees is converted to kilometres by
multiplying by $\pi/180$ and then by the radius — two exact factors, no magic. A
useful sanity anchor: near $111$ km per degree of latitude, so $1.55°$ is about
170 km.

## 8. Common mistakes

1. **Using the arccosine form for short baselines.** It is exact in exact
   arithmetic and wrong in the third decimal at 1 m. Use haversine.
2. **Swapping latitude and longitude.** Data files vary. Plot the first few points
   and look at them; a swapped pair puts your survey in the Gulf of Guinea and
   nothing else in the pipeline will complain.
3. **Sign conventions for longitude.** East-positive is the standard in geodesy
   and in most data formats; some legacy products are west-positive. Check with a
   known point.
4. **Subtracting $180°$ to get the back-azimuth.** It is wrong except on a
   meridian. Use the azimuth formula with the arguments reversed.
5. **Treating a spherical triangle like a plane triangle.** The angle sum is
   greater than $180°$; solving for an angle with the plane law of sines gives an
   answer that is wrong by the excess.
6. **Reporting a distance in kilometres without stating the radius.** A spherical
   distance is a central angle; the kilometres depend on which $R$ you chose, and
   $6371.0$, $6371.0088$ and $6378.137$ are all in use for different purposes.
7. **Assuming the sphere is "close enough" for a 10 000 km path.** It is 0.11
   percent in the case above — tens of kilometres, seconds of travel time.

## 9. Real-world applications

- **Epicentral distance.** The single most common spherical calculation in
  seismology: $R\Delta$ from hypocentre and station coordinates, then a travel-time
  lookup on the sphere. Every phase-association and location code begins here.
- **Station azimuths and back-azimuths.** Needed for focal mechanisms, for
  three-component rotation into radial and transverse, and for array beamforming.
- **Global potential fields.** Gravity and magnetic models are stored as
  spherical-harmonic expansions on a reference sphere or ellipsoid, and
  synthesising them requires exactly the great-circle geometry above.
- **GNSS and surveying.** Baseline vectors and reduced distances on regional
  networks use spherical or ellipsoidal formulas, depending on the baseline
  length; the guidance table in Section 6 is the selection criterion.
- **Plate motion and continental reconstruction.** Rotations on a sphere are the
  natural description of plate motion; an Euler pole is a pole of rotation, and
  reconstructing a continental margin is spherical trigonometry applied to a
  geological question.

## 10. Further reading

- **Snyder, J. P. (1987). *Map Projections — A Working Manual*. USGS Professional
  Paper 1395.** Level: intermediate. Chapter on the ellipsoid, geodesics and
  arc lengths; the standard reference for the geometry that Section 6 sketches.
  Available from the USGS as a public-domain report.
- **Torge, W. and Müller, J. (2012). *Geodesy* (4th ed.). De Gruyter.** Level:
  advanced. The rigorous treatment of the ellipsoid, normal sections and geodesics.
- **Vincenty, T. (1975). Direct and inverse solutions of geodesics on the
  ellipsoid with application of nested equations. *Survey Review*, 23(176),
  88–93.** Level: advanced. The source of the inverse iteration implemented in
  the demonstration; the equations are short enough to verify by hand.
- **Aki, K. and Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: advanced. Chapter 4 sets out the spherical
  geometry of rays, epicentral distance and azimuth in the notation the
  literature uses.
- **IUGG.** *Conventional Terrestrial Reference System and mean Earth radius.*
  Level: reference. The definition of the IUGG mean radius used throughout this
  lesson. Cite the current IUGG resolution rather than a secondary source if you
  need the exact wording.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm current availability and editions through your library
> before relying on them.

## 11. Related lessons

- [01-03-01 Angles, Triangles and the Unit Circle](./01-angles-and-triangles.md) —
  the plane laws that the spherical laws reduce to for small triangles.
- [01-03-03 Inverse Trigonometric Functions and Branch Ambiguity](./03-inverse-trig.md) —
  `atan2`, on which every azimuth formula depends.
- [01-04-03 Cartesian, Cylindrical and Spherical Coordinates](../04-geometry-and-coordinates/03-cartesian-spherical.md) —
  the coordinate machinery used in the derivations here.
- [01-04-04 Geographic Coordinates, Datums and Map Projections](../04-geometry-and-coordinates/04-geographic-coordinates.md) —
  the ellipsoid treated properly, and what a projected map does to distances.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md) —
  the calculus of surfaces, of which the spherical excess is the geometric shadow.

## Exercises and self-assessment

Exercises are in
[`exercises/04-spherical-trigonometry-exercises.md`](./exercises/04-spherical-trigonometry-exercises.md),
with solutions in
[`exercises/04-spherical-trigonometry-solutions.md`](./exercises/04-spherical-trigonometry-solutions.md).

Diagnostic anchors: the module
[README](./README.md) quotes the three verified reference results — the triangle
above with its $26.5976°$ excess, the antipodal $180.000000000°$ central angle,
and the $230.418°$ azimuth — so you can check every formula you implement against
numbers this repository has actually computed.

Before moving on, you should be able to:

- [ ] Derive $\cos c = \cos a\cos b + \sin a\sin b\cos C$ from a dot product in
      under ten lines.
- [ ] State which of the three distance formulas you would use at 100 m, at
      1000 km, and near the antipode, with a reason for each.
- [ ] Explain, without algebra, why forward and reverse azimuths differ on a sphere.
- [ ] Convert $1.5°$ to kilometres, both as an equatorial and as a polar arc, and
      say why the two differ.
- [ ] Explain what the spherical excess has to do with the area of a region.
