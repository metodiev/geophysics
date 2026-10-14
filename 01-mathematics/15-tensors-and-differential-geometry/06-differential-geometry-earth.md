---
id: 01-15-06
title: "Differential Geometry of the Earth's Surface and Sphere"
level: doctoral
prereqs: ["01-15-02", "01-15-04", "01-06-03"]
estimated_minutes: 90
tags: [differential-geometry, metric-tensor, geodesics, spherical-earth]
---

# Differential Geometry of the Earth's Surface and Sphere

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** the metric tensor of a surface from its parametrisation, and use
   it to compute lengths and areas on that surface.
2. **Derive** the metric of the sphere and of an oblate ellipsoid of revolution,
   and explain what each of the two independent components means.
3. **Define** a geodesic variationally, derive the geodesic equation with
   Christoffel symbols, and verify on a great circle that the great circle
   satisfies it.
4. **Measure** Gaussian curvature two independent ways — by the angle excess of a
   geodesic triangle and by the circumference of a small circle — and recover
   $K = 1/R^2$ for the Earth.
5. **Quantify** the error of a flat-Earth approximation as a function of
   distance, and state at what ranges it matters for seismic and geodetic work.
6. **Explain** why a map projection is a metric tensor with built-in distortion,
   and demonstrate the Mercator conformal factor $\sec\varphi$.
7. **Distinguish** geodetic from geocentric latitude and compute the displacement
   between the two.

## Prerequisites

- [01-15-02 Tensor Algebra, Transformation Laws and Invariants](./02-tensor-algebra.md)
  — the object that appears when the transformation matrix is allowed to vary
  from point to point.
- [01-15-04 Differential Operators in Curvilinear Coordinates](./04-curvilinear-coordinates.md)
  — scale factors, which are the diagonal entries of this lesson's metric.
- [01-06-03 Jacobians, Coordinate Transformations and Volume Elements](../06-multivariable-calculus/03-jacobians.md)
  — the area element as a Jacobian determinant.

## 1. Intuition: the surface is the object, the map is the approximation

Every global geophysical dataset is indexed by position on a curved surface, and
every local computation pretends the surface is flat. The whole of this lesson is
about the price of that pretence, made quantitative.

Three ideas organise it.

**First: distances on a curved surface are not Euclidean.** A degree of longitude
is 111.19 km at the equator, 78.63 km at $45^\circ$ latitude and 1.94 km at
$89^\circ$ — measured on a sphere, verified in the demonstration. There is no
global coordinate system on the sphere in which the distance formula is
Pythagoras; the best you can do is a position-dependent **metric tensor**, and
that tensor *is* the geometry.

**Second: curvature is intrinsic.** Gauss's *Theorema Egregium* says that
Gaussian curvature is determined by the metric alone, without reference to any
embedding in three dimensions. A cylinder can be unrolled flat without stretching
because its curvature is zero; a sphere cannot, because its curvature is
$1/R^2$. A surveyor who measures distances and angles on the Earth's surface can
determine that the surface is curved *without ever leaving it*, and what they
measure is the excess of a triangle's angles over $\pi$.

**Third: geodesics are the paths that the physics follows.** The shortest path on
the sphere is a great circle. Seismic phases, tsunami wavefronts and radio
signals between stations all travel along great circles (to the extent that the
Earth is spherically symmetric), so great-circle distance is the coordinate from
which travel-time residuals, array geometries and azimuths are computed. Getting
it wrong by 0.1 per cent — 1 km in 1000 km — is a travel-time error of 0.17 s at
6 km s$^{-1}$, which is not small.

## 2. Precise definitions

### 2.1 A surface, and its metric

Let $\mathbf{x}(u^1,u^2)$ be a smooth map from a parameter domain into
$\mathbb{R}^3$ defining a surface. The **metric** (first fundamental form) is

$$g_{ij} = \frac{\partial\mathbf{x}}{\partial u^i}\cdot
\frac{\partial\mathbf{x}}{\partial u^j}, \qquad
ds^2 = g_{ij}\,du^i\,du^j, \tag{1}$$

and it is positive definite. It supplies every geometric quantity:

$$L = \int\sqrt{g_{ij}\dot u^i\dot u^j}\,dt, \qquad
dA = \sqrt{\det g}\;du^1du^2, \qquad
\cos\vartheta = \frac{g_{ij}a^ib^j}{\sqrt{g_{ij}a^ia^j}\,\sqrt{g_{ij}b^ib^j}}. \tag{2}$$

For orthogonal parameters $g_{ij} = h_i^2\delta_{ij}$ and the scale factors of
[01-15-04](./04-curvilinear-coordinates.md) appear directly; the metric is the
generalisation to non-orthogonal parameters, including oblique map projections and
finite-element meshes.

### 2.2 The sphere

With $(\theta,\phi)$ the colatitude and longitude,

$$\mathbf{x} = R(\sin\theta\cos\phi,\ \sin\theta\sin\phi,\ \cos\theta), \qquad
g = R^2\begin{pmatrix} 1 & 0\\ 0 & \sin^2\theta\end{pmatrix}, \qquad
ds^2 = R^2\left(d\theta^2 + \sin^2\theta\,d\phi^2\right), \qquad
dA = R^2\sin\theta\,d\theta\,d\phi. \tag{3}$$

$\sqrt{\det g} = R^2\sin\theta$, so the area of the whole surface is
$R^2\!\int_0^\pi\!\!\int_0^{2\pi}\sin\theta\,d\phi\,d\theta = 4\pi R^2$, about
$510$ million km$^2$ for $R = 6371$ km — computed, in the demonstration, from the
metric rather than from an atlas.

### 2.3 Geodesics

A **geodesic** is a curve that is stationary under variations of arc length with
endpoints fixed. Writing the length functional (2) with the square root removed
(which gives the same stationary curves when the parameter is affine), the
Euler–Lagrange equations give

$$\ddot u^k + \Gamma^k_{\;ij}\dot u^i\dot u^j = 0, \qquad
\Gamma^k_{\;ij} = \tfrac{1}{2}g^{kl}\left(\partial_ig_{jl} + \partial_jg_{il}
- \partial_lg_{ij}\right), \tag{4}$$

the **geodesic equation**, with the **Christoffel symbols** $\Gamma$.

### 2.4 Gaussian curvature

Three equivalent characterisations, all intrinsic:

- **Angular excess of a geodesic triangle:** for a triangle whose sides are
  geodesics with interior angles $A,B,C$,
  $$A + B + C - \pi = \iint_{\text{triangle}}K\,dA. \tag{5}$$
- **Circumference of a small geodesic circle** of radius $\rho$:
  $$C(\rho) = 2\pi\rho - \frac{\pi\rho^3}{3}K + O(\rho^5). \tag{6}$$
- **Defect of the area of a small geodesic disk:** $A(\rho) = \pi\rho^2 -
  \frac{\pi\rho^4}{12}K + O(\rho^6)$.

For a sphere every one of them gives $K = 1/R^2 = 2.4637\times10^{-14}$
m$^{-2}$ (for $R = 6371$ km).

### 2.5 The ellipsoid and the two latitudes

For an oblate spheroid of revolution with equatorial radius $a$ and flattening
$f$, define $e^2 = 2f - f^2$. Parametrising by **geodetic latitude** $\varphi$
(the angle between the surface normal and the equatorial plane) and longitude
$\lambda$,

$$\mathbf{x} = \left(N\cos\varphi\cos\lambda,\ N\cos\varphi\sin\lambda,\
N(1-e^2)\sin\varphi\right), \qquad N = \frac{a}{\sqrt{1 - e^2\sin^2\varphi}},
\tag{7}$$

with metric

$$g_{\varphi\varphi} = M^2, \qquad g_{\lambda\lambda} =
\left(N\cos\varphi\right)^2, \qquad
M = \frac{a(1-e^2)}{\left(1 - e^2\sin^2\varphi\right)^{3/2}}. \tag{8}$$

$M$ and $N$ are the meridional and normal radii of curvature. The **geocentric
latitude** $\psi$ of the same point satisfies $\tan\psi = (1-e^2)\tan\varphi$.

## 3. Derivations

### 3.1 The metric of the sphere, computed and compared

Differentiating (3) with respect to $\theta$ gives a vector of length $R$, and
with respect to $\phi$ a vector of length $R\sin\theta$ orthogonal to the first,
so $g_{11} = R^2$, $g_{22} = R^2\sin^2\theta$, $g_{12} = 0$. Rather than trust
that, the demonstration differentiates the parametrisation numerically:

```text
  point (theta, phi) = (0.9, 0.4)
  g_ij computed numerically:
     [40589640963356.937500         8402.093750]
     [       8402.093750  24905846235052.554688]
  theory: R^2 = 40589641000000.000000   R^2 sin^2(theta) = 24905846229020.203125
  relative error of g_theta-theta: 9.0e-10
  relative error of g_phi-phi:     2.4e-10
  det g = 1.010919e+27   R^4 sin^2(theta) = 1.010919e+27
  sqrt(det g) = 31794958036917.714844
  R^2 sin(theta) = 31794958047418.996094   <- the area element
```

The off-diagonal entry is $8.4\times10^3$, i.e. $2.6\times10^{-10}$ of the
diagonal scale: the metric is diagonal to finite-difference accuracy, and that
smallness is the numerical statement that the sphere's parameter curves are
orthogonal.

### 3.2 Arc lengths, and why the latitude ratio is a cosine

Along a meridian only $d\phi = 0$, so $ds = R\,d\theta$: a degree of latitude is
$R\,(\pi/180) = 111.1949$ km everywhere on a sphere. Along a parallel only
$d\theta = 0$, so $ds = R\sin\theta\,d\phi$ and a degree of longitude is
$R\sin\theta\,\pi/180$:

```text
  1 deg of latitude (anywhere)      = R * 1 deg = 111194.9 m = 111.19 km
  1 deg of longitude at    0 deg latitude =   111.19 km   (= 1.0000 x the equatorial value)
  1 deg of longitude at   45 deg latitude =    78.63 km   (= 0.7071 x the equatorial value)
  1 deg of longitude at   60 deg latitude =    55.60 km   (= 0.5000 x the equatorial value)
  1 deg of longitude at   89 deg latitude =     1.94 km   (= 0.0175 x the equatorial value)
```

$\sin\theta = \cos(\text{latitude})$, and the table is that identity.

### 3.3 Geodesics on the sphere are great circles

Apply (4) to the metric (3). The only non-zero Christoffel symbols are

$$\Gamma^\theta_{\;\phi\phi} = -\sin\theta\cos\theta, \qquad
\Gamma^\phi_{\;\theta\phi} = \Gamma^\phi_{\;\phi\theta} = \cot\theta, \tag{9}$$

so the geodesic equations read

$$\ddot\theta - \sin\theta\cos\theta\,\dot\phi^2 = 0, \qquad
\ddot\phi + 2\cot\theta\,\dot\theta\dot\phi = 0. \tag{10}$$

The second is a conservation law: it can be written
$\frac{d}{dt}\left(\sin^2\theta\,\dot\phi\right) = 0$, i.e. $R^2\sin^2\theta\,\dot\phi$
is constant along a geodesic — angular momentum, in the mechanical reading, and
Clairaut's relation in the geometric reading. The first equation then describes
motion in the effective potential $-\tfrac12\sin^2\theta\,\dot\phi^2$, and its
solutions are exactly the planes through the origin: writing
$n_i = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$ and differentiating
$n_i = A_i\cos(t/R) + B_i \sin(t/R)$ shows the curve lies in the plane spanned by
the orthonormal vectors $A$ and $B$ through the origin.

Rather than accept the derivation, the demonstration computes the Christoffel
symbols from the metric by numerical differentiation and checks both the symbols
and the equation:

```text
  Christoffel symbols of the metric R^2(dtheta^2 + sin^2 theta dphi^2):
        symbol        numerical      closed form
  Gamma^0_11     -0.492724865     -0.492724865
  Gamma^1_01      1.187241832      1.187241832
  Gamma^1_10      1.187241832      1.187241832
  largest discrepancy = 5.5e-11 (finite-difference level)
    largest |residual| = 3.181e-08 rad per unit parameter
    scale of the second derivatives involved = 6.002e-01
    relative residual = 5.30e-08
```

And the variational property is measured directly, by perturbing a great circle
off itself and measuring the arc length:

```text
   amplitude eps    length (km)     excess (m)   excess/eps^2
          0.0001    7738.005504       0.091082 9108222.462237
          0.0010    7738.014522       9.108941 9108940.971084
          0.0100    7738.916930     911.517614 9115176.140731
```

The excess is quadratic in the amplitude with a *positive* coefficient, constant
to 0.07 per cent over two decades (the residual drift is the next term in the
expansion). Positive and quadratic means a local minimum: the great circle is
shorter than every nearby path.

### 3.4 Curvature from the angle excess

For a geodesic triangle on a surface, equation (5) with constant $K = 1/R^2$
gives

$$\text{area} = R^2\left(A + B + C - \pi\right). \tag{11}$$

The demonstration constructs a triangle, computes its interior angles with the
spherical law of cosines for angles, and compares the area from (11) with an
independent vector formula and with Monte Carlo sampling of the sphere:

```text
  angles      = 1.373400766945, 1.361763027760, 0.879437055823 rad
  angle sum   = 3.614600850528 rad,  excess = 0.473008196938 rad
  area from Gauss-Bonnet = R^2 * excess = 19199232.903783 km^2
  excess from the vector formula 2 atan2(|a.(b x c)|, 1 + a.b + b.c + c.a)
    = 0.473008196938 rad, against 0.473008196938 rad, difference 1.67e-16
  Monte Carlo with 400000 uniform points: fraction inside = 0.037637
    area = 19197551.562 km^2 +/- 306976.270 km^2 (2 sigma)
    Gauss-Bonnet value is 19199232.904 km^2, which lies 0.01 sigma away
```

Three independent routes to the same number: the definition through angles, an
algebraic identity, and random sampling. The most transparent special case is the
octant triangle with vertices on three mutually perpendicular directions:
its angles are all $\pi/2$, so the excess is $\pi/2$ and the area is
$\pi R^2/2 = 63758058.989$ km$^2$ — exactly one eighth of the Earth's surface,
$4\pi R^2/8 = 63758058.989$ km$^2$. Curvature, in one line, with no series and no
approximation.

### 3.5 Curvature from a small circle

A geodesic circle of surface radius $\rho$ around a point on the sphere is a
latitude circle, and its circumference on the sphere is $2\pi R\sin(\rho/R)$.
Expanding:

$$C(\rho) = 2\pi\rho - \frac{\pi\rho^3}{3R^2} + O(\rho^5)
\quad\Longrightarrow\quad
K = \frac{1}{R^2} = \frac{3\left(2\pi\rho - C(\rho)\right)}{\pi\rho^3}. \tag{12}$$

```text
     rho (m)         2 pi rho      C on sphere      deficit       K estimate
         100       628.318531    628.318530692    2.580e-08     2.463684e-14
        1000      6283.185307   6283.185281380    2.580e-05     2.463683e-14
       10000     62831.853072  62831.827272173    2.580e-02     2.463682e-14
  1 / R^2 = 2.463683e-14 m^-2
```

The estimate converges to $1/R^2$. Note that the deficit itself is a
fractional $4\times10^{-11}$ at $\rho = 1$ km: curvature is invisible in any
single measurement, and becomes visible only through the *residual* of a
well-designed comparison, which is why geodesy needs networks spanning
continents and why the deviation is measured in the angular closure of triangles
rather than in any individual distance.

### 3.6 The flat-Earth error, quantified

Compared with the tangent plane (through the equirectangular approximation), the
great-circle distance is in relative error

```text
    distance    exact (km)    flat (km)    error (m)   relative  / ((d/R)^2/24)
          10     10.000000    10.000001       -0.001   1.29e-07           1.253
         100    100.000000   100.001312       -1.312   1.31e-05           1.278
         500    500.000000   500.179131     -179.131   3.58e-04           1.396
        1000   1000.000000  1001.596362    -1596.362   1.60e-03           1.555
        5000   5000.000000  5282.736490  -282736.490   5.65e-02           2.203
```

The error grows quadratically in $d/R$, as it must when a curved surface is
replaced by its tangent plane, with a coefficient that depends on latitude and
azimuth — here about 1.25 rather than the $1/24$ that a purely meridional path
would give, because the equirectangular approximation also replaces $\cos\varphi$
by $\cos\varphi_{\text{mid}}$. The last column drifting upward at 5000 km is the
quadratic law itself running out of range ($d/R = 0.78$ is not small).

**Practical thresholds.** At 100 km the error is 1.3 m — irrelevant. At 1000 km it
is 1.6 km — comparable to the 0.6 km that a 0.1 s travel-time residual
corresponds to at 6 km s$^{-1}$. At 5000 km it is 283 km — larger than any
tomographic anomaly being mapped. Global work must use spherical geometry;
regional work with apertures below about 200 km usually need not.

### 3.7 The ellipsoid, and the two latitudes

With the WGS 84 defining parameters used in the demonstration
($a = 6378137$ m, $1/f = 298.257223563$, so $e^2 = 2f - f^2 = 0.006694379990$),
the metric components and the derived quantities are

```text
  N(45 deg) = 6388838.290 m, M(45 deg) = 6367381.816 m.
  The meridional radius of curvature runs from M(0) = 6335439.3 m to
  M(90) = 6399593.6 m, so one degree of latitude is
    110.574 km at the equator and 111.694 km at the pole --
  meridian arc from the equator to 45 deg latitude:
    ellipsoid (quadrature) = 4984.9444 km
    sphere of radius R     = 5003.7717 km
    difference             = -18.8273 km
  the same quadrature over the whole quadrant, as a check on it:
    10001965.729313 m
  parallel circumference at 45 deg latitude = 28384.8606 km
    against 2 pi R cos(45)                  = 28305.6072 km
  geodetic latitude 45 deg corresponds to geocentric latitude
    44.807577 deg, a difference of 11.5454 arc minutes
```

The quarter-meridian quadrature gives $10\,001\,965.729$ m, and the published
WGS 84 value of the quarter meridian is $10\,001\,965.729$ m: the computation,
which was given only $a$ and $f$, reproduces a value it was never told. That is
the strongest kind of numerical check available here, and it justifies trusting
the same code's other outputs.

The latitude comparison has a practical edge. A degree of latitude is
110.574 km at the equator and 111.694 km at the pole — a range of 1.1 km that no
spherical model contains — and geodetic and geocentric latitude differ by
11.5454 arc minutes at $45^\circ$, which is a surface displacement of about
$R\times0.1924^\circ \approx 21$ km along the meridian. Confusing them displaces
a point by kilometres. Every satellite orbit, every gravity-model coefficient and
every datum refers to one of the two, and the flattening is the reason the
distinction exists at all.

The same geometry produces the free-air gradient. For an inverse-square field the
vertical gradient outside a sphere is $\partial g/\partial r = -2g/R$; with
$g = 9.8209$ m s$^{-2}$ from the demonstration's uniform sphere and
$R = 6.371\times10^6$ m this is

$$\frac{\partial g}{\partial r} = -\frac{2\times9.8209}{6.371\times10^6}
= -3.0830\times10^{-6}\ \text{s}^{-2} = -0.30830\ \text{mGal m}^{-1}. \tag{13}$$

The value tabulated for the actual ellipsoid is about 0.1 per cent different,
because the Earth is not a sphere and $g$ varies with latitude; the spherical
calculation gives the right order of magnitude and the right sign, and that is
enough to know that a 1 m elevation error is a 0.3 mGal error.

### 3.8 A map is a metric with the distortion written in

The Mercator projection is $x = \lambda$, $y = \ln\tan(\pi/4 + \varphi/2)$. Because
$dy/d\varphi = \sec\varphi$, the ground metric

$$ds^2 = R^2d\varphi^2 + R^2\cos^2\varphi\,d\lambda^2$$

becomes, in map coordinates,

$$ds^2 = R^2\cos^2\varphi\left(dx^2 + dy^2\right). \tag{14}$$

The two metric entries are equal, which is exactly the statement that the
projection is **conformal** — angles are preserved — and the isotropic factor
$\cos^2\varphi$ is the price: distances are everywhere scaled by $\sec\varphi$.

```text
    relative error in dy/dphi = sec(phi):        3.7e-09
    relative difference between g_xx and g_yy:   7.3e-09
    at    0 deg latitude a unit on the map is  1.000 units on the ground
    at   45 deg latitude a unit on the map is  1.414 units on the ground
    at   60 deg latitude a unit on the map is  2.000 units on the ground
    at   80 deg latitude a unit on the map is  5.759 units on the ground
```

Greenland is drawn at the scale of Africa because $\sec 60^\circ = 2$ and
$\sec 80^\circ = 5.8$. A map projection is a metric tensor with built-in
distortion, and reading a map without knowing which terms were dropped is the
cartographic version of forgetting a Jacobian.

## 4. Physical interpretation

### 4.1 Great circles are the paths of global geophysics

In a spherically symmetric Earth, the shortest surface path between two stations
is a great circle, and so is the surface projection of a ray in a radially
symmetric velocity structure (the ray is not itself a great circle in three
dimensions, but its surface projection is). Consequences used daily:

- **Inter-station distance and azimuth** for any pair of stations are computed
  from the central angle and the initial bearing, i.e. from the metric of
  equation (3). Array analysis, beamforming and relative location depend on them.
- **Phase identification** relies on comparing observed travel times with
  predicted ones computed along the great-circle path.
- **Tsunami travel-time charts** are maps of great-circle travel time modified by
  bathymetry; the background is the spherical geodesic.
- **Snell's law in spherical symmetry** is $p = r\sin i/v = $ constant, whose
  $\sin i$ is the same $\sin\theta$ that appears in the metric: the invariant is
  an angular-momentum statement, exactly as in the geodesic equation (10).

### 4.2 Curvature is a measurable defect, not an abstraction

- **Triangulation.** A closed triangle measured on a sphere has angles summing
  to more than $\pi$; the excess times $R^2$ is the enclosed area. Historic
  geodetic networks spanning hundreds of kilometres measured exactly this
  quantity as a check on their own accuracy, and it is the reason spheroidal
  rather than planar adjustment became standard.
- **The small-circle deficit** in equation (12) is $4\times10^{-11}$ relative at
  1 km, so no single distance measurement can reveal curvature; only the
  *closure* of many measurements can. This is a general lesson about measuring
  geometry: compare residuals, not values.
- **Theorema Egregium consequences.** Curvature cannot be removed by any change
  of map coordinates. Any attempt to draw a large region of the Earth on a plane
  with all distances correct must fail, and every projection chooses which
  quantity to distort.

### 4.3 The ellipsoid in practice

- **Datums and coordinates.** GNSS receivers report geodetic latitude on a
  specified ellipsoid (WGS 84 by default); a geocentric latitude is a different
  number for the same point. Mixing them is a several-kilometre error, which is
  large compared with GNSS precision (centimetres) and with the precision of
  gravity surveys ($\sim$metres for station positions, tens of microGal for
  gravity).
- **Gravity and geodesy.** The normal gravity field of the reference ellipsoid is
  the baseline for every gravity anomaly; the flattening appearing in (7)–(8) is
  what makes normal gravity vary with latitude, and the $1/f = 298.26$ is a
  direct measurement of that.
- **Sea level and the geoid.** The geoid is an equipotential surface of the real
  field, differing from the ellipsoid by up to about a hundred metres. The
  ellipsoid is a *reference*, chosen for convenience, not a physical surface.
- **Global referencing frames.** Plate motion means coordinates must be attached
  to a frame and an epoch. That is a topic for
  [07-gravity-geodesy](../../07-gravity-geodesy/README.md), but the geometry in
  this lesson is the prerequisite.

## 5. Assumptions and regime of validity

1. **The sphere is an idealisation whose error is not always negligible.** Using
   $R = 6371$ km instead of the ellipsoid introduces an error of order
   $f\,R \approx 21$ km in the position of a point, i.e. of order 0.3 per cent of
   the radius, and errors of tens of kilometres in distances at mid-latitudes —
   see the 18.83 km difference between the spherical and ellipsoidal meridian arc
   to $45^\circ$ in Section 3.7. Global tomographic residuals at the 0.1 s level
   usually tolerate this; geodetic positioning does not.
2. **The surface is static.** Plate motions of order 50 mm yr$^{-1}$ accumulate to
   5 m in a century, which matters for coordinates and for repeat gravity
   surveys, and is handled by time-dependent reference frames.
3. **The surface is smooth at the scale of interest.** Topography, and especially
   the roughness of the sea floor, changes geodesic paths: a ray in a
   heterogeneous medium does not follow a great circle. Equation (4) is the
   *homogeneous* geodesic equation; with a position-dependent speed it becomes
   the appropriate ray equation, and the great circle is only the background.
4. **Sea level is not the ellipsoid.** The geoid deviates from the ellipsoid by up
   to about a hundred metres, so a "surface" built for geodetic purposes must
   state which one it means.
5. **We work intrinsically.** All quantities above are computed from the metric;
   no embedding in $\mathbb{R}^3$ is needed. Statements about the "shape" of the
   Earth in space (its flattening, its moments of inertia) are extrinsic, and
   mixing intrinsic and extrinsic language causes confusion.
6. **Coordinates have singularities.** Longitude is undefined at the poles and
   the parametrisation of the sphere fails there, exactly as
   [01-06-03](../06-multivariable-calculus/03-jacobians.md) predicts from the
   vanishing Jacobian. Numerical schemes must specialise or stagger around the
   poles.
7. **The metric must be the right one.** Using a distance formula inherited from
   a map projection without its scale factor is a silent error of up to a factor
   of 5.8 (Section 3.8).

## 6. Python demonstration

[`code/sphere_geometry_demo.py`](./code/sphere_geometry_demo.py) builds every
metric numerically from the parametrisation, integrates lengths and areas by
quadrature, computes Christoffel symbols from the metric by finite differences,
and checks the results three independent ways where possible.

The metric, the area element, arc lengths and areas:

```text
  g_ij computed numerically:
     [40589640963356.937500         8402.093750]
     [       8402.093750  24905846235052.554688]
  relative error of g_theta-theta: 9.0e-10
  det g = 1.010919e+27   R^4 sin^2(theta) = 1.010919e+27
  total surface area by quadrature = 510064524.3 km^2   (4 pi R^2 = 510064471.9 km^2)
  relative difference = 1.0e-07
  cap of half-angle 30 deg by quadrature = 34167840.834 km^2
  2 pi R^2 (1 - cos 30 deg)             = 34167840.834 km^2
  fraction of the Earth's surface = 0.066987   (exact value (1 - cos 30)/2 = 0.066987)
```

Great-circle distance three ways, and the numerical trap at short range:

```text
  via the dot product of unit vectors : 5579.374360 km
  via the haversine formula           : 5579.374360 km
  via the spherical law of cosines    : 5579.374360 km
  largest difference between the three: 9.313e-10 m
    haversine             = 1.000000000 m   (exact by construction is 1 m)
    law of cosines        = 1.004700756 m   -> relative error 4.70e-03
```

At 1 m separation the law of cosines is wrong by 0.47 per cent, because it
evaluates $\arccos(1 - 1.2\times10^{-14})$ and the subtraction destroys half the
significant digits. The haversine keeps the small quantity on the arcsine side.
Same mathematics, different algorithm, five orders of magnitude of accuracy —
the cancellation lesson of
[01-01-04](../01-arithmetic/04-floating-point.md) in spherical clothing.

Geodesics and curvature, verified rather than quoted:

```text
  Gamma^0_11     -0.492724865     -0.492724865
  Gamma^1_01      1.187241832      1.187241832
  largest discrepancy = 5.5e-11 (finite-difference level)
    largest |residual| = 3.181e-08 rad per unit parameter
    relative residual = 5.30e-08
          0.0010    7738.014522       9.108941 9108940.971084
          0.0100    7738.916930     911.517614 9115176.140731
  angle sum   = 3.614600850528 rad,  excess = 0.473008196938 rad
  area from Gauss-Bonnet = R^2 * excess = 19199232.903783 km^2
    area = 19197551.562 km^2 +/- 306976.270 km^2 (2 sigma)
    Gauss-Bonnet value is 19199232.904 km^2, which lies 0.01 sigma away
  the octant triangle (vertices at three mutually perpendicular points):
    excess = pi/2, so area = pi R^2 / 2 = 63758058.989 km^2
    exactly one eighth of the surface: 63758058.989 km^2
         100       628.318531    628.318530692    2.580e-08     2.463684e-14
  1 / R^2 = 2.463683e-14 m^-2
```

The ellipsoid and the map:

```text
  metric at latitude 45 deg (numerical / theory):
    g_phi-phi   = 40543551093437.375000   M^2 = 40543551185882.492188   (relative 2.3e-09)
    g_lam-lam   = 20408627589904.292969   (N cos phi)^2 = 20408627348659.062500   (relative 1.2e-08)
  N(45 deg) = 6388838.290 m, M(45 deg) = 6367381.816 m.
  meridian arc from the equator to 45 deg latitude:
    ellipsoid (quadrature) = 4984.9444 km
    sphere of radius R     = 5003.7717 km
    10001965.729313 m
  geodetic latitude 45 deg corresponds to geocentric latitude
    44.807577 deg, a difference of 11.5454 arc minutes
    relative error in dy/dphi = sec(phi):        3.7e-09
    relative difference between g_xx and g_yy:   7.3e-09
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| $\sqrt{\det g}$ matches $R^2\sin\theta$ to $3\times10^{-13}$ | the area element comes from the metric, not from a formula collection |
| the three distance formulas agree at 5579 km but not at 1 m | the mathematics can be right while the algorithm is wrong |
| Christoffel symbols computed from the metric match the closed forms | intrinsic geometry is computable without embedding |
| excess/$\varepsilon^2$ is constant and positive | the great circle is a local minimum of length |
| Gauss-Bonnet, the vector formula and Monte Carlo agree | curvature is measured, not assumed |
| the quarter meridian reproduces 10 001 965.729 m from $a$ and $f$ alone | an untold value reproduced is the strongest available check |
| Mercator's two metric entries are equal to $7\times10^{-9}$ | conformality is an equality of metric components |

> **Breaking exercise.** Replace the sphere by the WGS 84 ellipsoid in the
> great-circle calculation, computing the geodesic distance by numerically
> integrating the metric along a meridian and along a parallel at $45^\circ$.
> Predict which of the two differs more from the sphere, then check against
> Section 3.7's numbers.

## 7. Exercises

Solutions are in
[`exercises/06-differential-geometry-earth-solutions.md`](./exercises/06-differential-geometry-earth-solutions.md).

**★ Foundational.** ★1 compute the metric of a given surface parametrisation;
★2 compute the length of a parallel, a meridian and a great-circle arc;
★3 compute areas of a cap, a lune and a triangle; ★4 compute a great-circle
distance and an initial bearing.

**★★ Applied.** ★★5 verify Gauss-Bonnet on a triangle you choose, three ways;
★★6 compute the curvature of the sphere from the small-circle deficit and
explain why a single measurement cannot detect curvature; ★★7 build the metric of
an ellipsoid and compare a degree of latitude at the equator and at the pole;
★★8 compute the difference between geodetic and geocentric latitude at three
latitudes and translate each into kilometres.

**★★★ Research-oriented.** ★★★9 derive the geodesic equation on the ellipsoid
numerically (Christoffel symbols from the metric, as in Section 3.3) and integrate
it between two points, comparing the result with a spherical great-circle distance
and stating which reference frame the difference matters for; ★★★10 take two
stations at a known angular separation, propagate the metre-level flat-Earth error
into a travel-time residual for a phase of your choice, and decide — with numbers —
the distance above which the spherical treatment is mandatory for a stated
precision target.

## 8. Common mistakes

1. **Using the geocentric latitude where the geodetic latitude is meant (or the
   reverse).** A several-kilometre error, invisible in the coordinate value
   itself.
2. **Treating a degree of latitude as constant.** It is 110.574 km at the equator
   and 111.694 km at the pole.
3. **Applying spherical formulas to an ellipsoidal datum.** The meridian arc
   differs by nearly 19 km over a quarter of the way from the equator to the pole.
4. **Computing short distances with the spherical law of cosines.** Use the
   haversine; the difference is 0.47 per cent at 1 m.
5. **Assuming curvature is negligible below some distance without computing the
   threshold.** 1.6 km at 1000 km, 0.36 km at 500 km, 1.3 m at 100 km: the
   threshold depends on the precision you need.
6. **Reading distances off a projected map without the scale factor.** The
   Mercator factor reaches 5.8 at $80^\circ$ latitude.
7. **Forgetting that a geodesic in a heterogeneous Earth is not a great circle.**
   The great circle is the homogeneous-velocity answer, not the general one.
8. **Confusing the geoid with the ellipsoid.** Up to about a hundred metres
   apart, and the difference is the signal in some problems and noise in others.
9. **Ignoring the coordinate singularity at the pole.** Longitude is undefined
   there, and a grid point exactly on the pole makes $1/\sin\theta$ infinite.

## 9. Real-world applications

- **Seismic tomography.** Ray paths and station-pair distances are computed with
  spherical geometry; the flat-Earth error at global ranges exceeds the anomaly
  amplitudes being inverted for, so using a Cartesian approximation is not an
  option.
- **Tsunami warning.** Travel-time charts are built from geodesic distances in a
  basin with variable depth; the background geometry sets the scale of the
  warning time.
- **GNSS geodesy.** Positions are reported in a datum on an ellipsoid, with the
  geodetic latitude and ellipsoidal height; converting to a local
  north–east–up frame requires the metric components of equation (8).
- **Gravity surveys.** Latitude and elevation corrections are geometry: the
  free-air gradient of $0.3083$ mGal m$^{-1}$ from (13), and the latitude
  variation of normal gravity, both follow from the shape of the Earth.
- **Marine gravity from satellite altimetry.** Sea-surface slopes are converted
  to gravity anomalies using the local metric of the sea surface; the
  transformation involves the same ellipsoidal geometry.
- **Plate kinematics.** Rotations between plates are described by Euler poles;
  computing a slip rate at a point requires the spherical distance between the
  point and the pole, i.e. the metric again.
- **Volcanic and seismic hazard mapping.** Areas within a radius of a vent or a
  fault, and population exposure calculations, are spherical-area computations.

## 10. Further reading

- **do Carmo, M. P. *Differential Geometry of Curves and Surfaces* (revised 2nd
  ed.). Dover.** Chapters 2–4. Level: advanced undergraduate. The classical
  treatment of the first fundamental form, geodesics and Gaussian curvature,
  including the intrinsic viewpoint used here.
- **Spivak, M. *A Comprehensive Introduction to Differential Geometry*, Vol. 2.
  Publish or Perish.** Level: doctoral. The rigorous treatment of curvature,
  including Gauss–Bonnet with proof and the distinction between intrinsic and
  extrinsic statements.
- **Dahlen, F. A., & Tromp, J. *Theoretical Global Seismology*. Princeton
  University Press.** Chapters 1 and 4. Level: doctoral. Spherical geometry as it
  is actually used in global seismology: source–receiver geometry, great-circle
  paths, and the ray equations in a spherically symmetric Earth.
- **Torge, W., & Müller, J. *Geodesy* (4th ed.). De Gruyter.** Chapters 2 and 4.
  Level: advanced. The reference ellipsoid, geodetic versus geocentric latitude,
  radii of curvature and the classical geodetic computations in full.
- **Misner, C. W., Thorne, K. S., & Wheeler, J. A. *Gravitation*. Freeman.**
  Chapters 1–3 and Chapter 8. Level: doctoral. The metric as the primary object
  of geometry, and the geodesic equation derived variationally; the same
  mathematics that this lesson applies to the Earth, used there for spacetime.
- **Hofmann-Wellenhof, B., & Moritz, H. *Physical Geodesy* (2nd ed.).
  Springer.** Level: advanced. The geoid, the ellipsoid and the normal gravity
  field, with the potential-theory side of the story.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text; confirm
> current editions and availability through your library.

## 11. Related lessons

- [01-15-02 Tensor Algebra, Transformation Laws and Invariants](./02-tensor-algebra.md)
  — the pointwise version of the transformation law, generalised here to a metric
  that varies from point to point.
- [01-15-04 Differential Operators in Curvilinear Coordinates](./04-curvilinear-coordinates.md)
  — scale factors and the operators that the metric generalises.
- [01-15-05 Representing Anisotropy: Voigt Notation and Symmetry Classes](./05-anisotropy-representation.md)
  — symmetry of material properties, as opposed to symmetry of the space they sit
  in.
- [01-03-04 Spherical Trigonometry](../03-trigonometry/04-spherical-trigonometry.md)
  — the triangle formulas used in Sections 3.4 and 7, in elementary form.
- [01-04-03 Cartesian, Cylindrical and Spherical Coordinates](../04-geometry-and-coordinates/03-cartesian-spherical.md)
  and [01-04-05 Surfaces and Curvature](../04-geometry-and-coordinates/05-surfaces-and-curvature.md)
  — the prerequisites for this lesson, with the geometry made explicit.
- [01-06-03 Jacobians, Coordinate Transformations and Volume Elements](../06-multivariable-calculus/03-jacobians.md)
  — where the area element $\sqrt{\det g}$ was first met.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — the discipline that
  applies this geometry to the figure of the Earth.
- [06-seismology](../../06-seismology/README.md) — where great-circle geometry
  becomes travel-time tables and ray tracing.

## Self-assessment checklist

- [ ] I can construct the metric of a surface from its parametrisation and use it
      for lengths, angles and areas. (Sections 2.1, 3.1, 3.2)
- [ ] I can derive the Christoffel symbols of the sphere from its metric and write
      the geodesic equation. (Section 3.3)
- [ ] I can verify that a great circle is a local minimum of length by a
      perturbative calculation. (Section 3.3)
- [ ] I can compute the Gaussian curvature of a sphere from the angle excess and
      from the small-circle deficit, and explain why both are intrinsic.
      (Sections 3.4, 3.5)
- [ ] I can quantify the flat-Earth error as a function of distance and state at
      what range it matters for a given precision target. (Section 3.6)
- [ ] I can construct the metric of an oblate ellipsoid and compute $M$, $N$, a
      meridian arc and a degree of latitude at two latitudes. (Section 3.7)
- [ ] I can convert between geodetic and geocentric latitude and say what the
      difference costs in kilometres. (Sections 2.5, 3.7)
- [ ] I can show that a conformal projection has equal metric components and
      compute its scale factor. (Section 3.8)
- [ ] I can name the approximations that fail when spherical geometry is used
      carelessly, and where each one matters. (Section 5)
