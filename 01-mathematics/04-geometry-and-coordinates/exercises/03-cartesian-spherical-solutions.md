# Solutions — 01-04-03 Cartesian, Cylindrical and Spherical Coordinates

> **Read this after attempting the exercises, not before.**
>
> Spherical coordinates are $(r,\theta,\phi)$ with $\theta$ the colatitude from
> $+z$ and $\phi$ the azimuth anticlockwise from $+x$. Earth-scale quantities use
> $R = 6371.0088$ km (sphere) or WGS84 (ellipsoid), stated in each case. All numbers
> were computed; the ECEF inverse is the closed form implemented in
> [`code/coordinate_systems_demo.py`](../code/coordinate_systems_demo.py).

---

## ★1 — Conversions and round trips

| point | $r$ | $\theta$ | $\phi$ | cylindrical $(\rho, \phi, z)$ |
|---|---|---|---|---|
| $(3,4,0)$ | 5 | $90.0000°$ | $53.1301°$ | $(5,\ 53.1301°,\ 0)$ |
| $(-3,4,-12)$ | 13 | $157.3801°$ | $126.8699°$ | $(5,\ 126.8699°,\ -12)$ |
| $(0,0,-7)$ | 7 | $180.0000°$ | undefined | $(0,\ \text{undefined},\ -7)$ |

**Worked detail for the second point.** $r = \sqrt{9+16+144} = \sqrt{169} = 13$;
$\rho = \sqrt{9+16} = 5$;
$\theta = \operatorname{atan2}(\rho, z) = \operatorname{atan2}(5, -12) = 157.3801°$
(the point is below the equator, so the colatitude exceeds $90°$ ✓);
$\phi = \operatorname{atan2}(4, -3) = 126.8699°$ (second quadrant, north-west ✓).

**Round trips.** Converting each answer back with
$x = r\sin\theta\cos\phi$, $y = r\sin\theta\sin\phi$, $z = r\cos\theta$ returns the
inputs to the printed precision. For the second point:
$\sin(157.3801°) = 0.384615$, $\cos(126.8699°) = -0.6$, giving
$x = 13 \times 0.384615 \times (-0.6) = -3.0$ ✓, and so on.

**The undefined azimuth.** For $(0, 0, -7)$ the point lies on the $z$-axis, so
$\rho = 0$ and every azimuth describes the same point. `atan2(0, 0)` returns 0 by
convention. **This is not a bug and not a numerical accident: the azimuth genuinely
does not exist there**, because a coordinate system that uses an angle about an axis
cannot label points *on* that axis. Any code that divides by $\rho$ will fail; any
code that returns an azimuth will return an arbitrary one. Handle the axis
explicitly.

---

## ★2 — Volume and solid angle

**(a)** Cartesian as a function of $(r, \theta, \phi)$:

$$J = \begin{pmatrix}
\sin\theta\cos\phi & r\cos\theta\cos\phi & -r\sin\theta\sin\phi \\
\sin\theta\sin\phi & r\cos\theta\sin\phi & \phantom{-}r\sin\theta\cos\phi \\
\cos\theta & -r\sin\theta & 0
\end{pmatrix}.$$

**(b)** $\det J = r^{2}\sin\theta$, so $dV = r^{2}\sin\theta\,dr\,d\theta\,d\phi$.

A quick way to remember the factor without expanding: the spherical shell element is
$dr$, the meridional element is $r\,d\theta$, and the longitudinal element is
$r\sin\theta\,d\phi$; the volume is their product.

**(c)**

$$\int_0^{2\pi}\!\!\int_0^{\pi}\sin\theta\,d\theta\,d\phi
= 2\pi \times \left[-\cos\theta\right]_0^{\pi} = 2\pi \times 2 = 4\pi .$$

The value $4\pi$ is the definition of the total solid angle of a sphere, and it is
the reason $4\pi$ appears in every spherically symmetric formula — from the inverse
square law to Gauss's law.

**(d)** For $R = 10$:

$$\int_0^{R} r^{2}\,dr = \frac{R^{3}}{3} = 333.3333333333, \qquad
V = 333.3333333333 \times 4\pi = 4188.790312,$$

against the exact $4\pi R^{3}/3 = 4188.790205$. The relative disagreement is

$$\frac{4188.790312 - 4188.790205}{4188.790205} = 2.57\times10^{-8}.$$

**The origin of the disagreement is not the transformation.** The demonstration
evaluated $\int_0^{\pi}\sin\theta\,d\theta$ by a midpoint rule with 4000 intervals,
obtaining $2.0000000514$ instead of exactly 2 — a relative error of $2.6\times10^{-8}$,
which is exactly the relative error in the volume. **The error of a product is the
error of its worst factor**, and here one factor was computed numerically while the
others were exact. Recognising which factor limits an accuracy is the practical
skill; the arithmetic is trivial.

---

## ★3 — Spherical caps

**(a)** $A = 2\pi R^{2}(1-\cos\alpha)$ with
$2\pi R^{2} = 255032940.486$ km²:

- $\alpha = 5°$: $255032940.486 \times (1-0.9961947) = 255032940.486 \times
  0.0038053 = \boxed{9.7047734\times10^{5}\ \text{km}^{2}}$;
- $\alpha = 30°$: $255032940.486 \times (1-0.8660254) = 255032940.486 \times
  0.1339746 = \boxed{3.4167935\times10^{7}\ \text{km}^{2}}$.

**(b)** $\alpha = 90°$ gives $1 - \cos 90° = 1$, so
$A = 2\pi R^{2} = \boxed{2.5503294\times10^{8}\ \text{km}^{2}}$, exactly half of
$4\pi R^{2} = 5.1006588\times10^{8}$ km². **That is a hemisphere**, and the exact
factor of two is the strongest available check on the formula.

**(c)** The $5°$ cap is
$9.7047734\times10^{5} / 5.1006588\times10^{8} = \boxed{1.9027\times10^{-3}}$, i.e.
**0.19 percent** of the sphere.

**(d)** A $0.1° \times 0.1°$ cell at latitude $\varphi$ has area

$$A_{\text{cell}} = \left(0.1° \times \frac{\pi}{180} \times R\right)^{2}\cos\varphi
= (11.11949\ \text{km})^{2}\cos\varphi = 123.643\cos\varphi\ \text{km}^{2}.$$

| latitude | cell area (km²) |
|---|---|
| $10°$N | $121.765$ |
| $80°$N | $21.470$ |

The ratio is $121.765/21.470 = \boxed{5.671} = \cos 10°/\cos 80°$ exactly ✓.

**What the ratio implies.** A fixed physical area needs $5.67$ times as many cells
at $80°$N as at $10°$N to be sampled at the same resolution. Across a full global
grid from the equator to $85°$ the ratio reaches $1/\cos 85° = 11.5$, and it
diverges at the pole. **A regular latitude–longitude grid therefore over-samples
the pole and under-samples low latitudes at fixed cell count, or does the reverse at
fixed resolution** — which is the pole problem of Section 8 in the lesson, and the
reason operational global grids use other layouts.

---

## ★★4 — Geocentric rectangular coordinates

**(a) Sphere of radius $a = 6378.137$ km:**

$$X = a\cos\varphi\cos\lambda = \boxed{4591.278387\ \text{km}},$$
$$Y = a\cos\varphi\sin\lambda = \boxed{1671.088670\ \text{km}},$$
$$Z = a\sin\varphi = \boxed{4099.787436\ \text{km}},$$

with $\lvert\mathbf{r}\rvert = 6378.137000$ km — equal to $a$ by construction, since
a sphere has constant radius.

**(b) WGS84 ellipsoid.** With $e^{2} = f(2-f) = 0.006694379990$,

$$N(\varphi) = \frac{a}{\sqrt{1-e^{2}\sin^{2}\varphi}} = \frac{6378.137}
{\sqrt{1-0.00669438 \times 0.4131759}} = \frac{6378.137}{0.9986159}
= \boxed{6386.976166\ \text{km}},$$

$$X = N\cos\varphi\cos\lambda = \boxed{4597.641227\ \text{km}}, \qquad
Y = N\cos\varphi\sin\lambda = \boxed{1673.404555\ \text{km}},$$

$$Z = N(1-e^{2})\sin\varphi = \boxed{4077.985572\ \text{km}} .$$

**(c)**

- sphere: $\lvert\mathbf{r}\rvert = 6378.137000$ km;
- ellipsoid: $\lvert\mathbf{r}\rvert = \boxed{6369.344863}$ km.

Difference: $8.792$ km. **That is the size of the error introduced by using a
spherical reference radius at $40°$N in a potential-field or orbit calculation** —
and it is a *systematic* function of latitude, largest where the ellipsoid departs
most from the mean sphere.

**(d)** The geocentric latitude is the angle of the radius vector:

$$\varphi_{\text{geocentric}} = \operatorname{atan2}(Z, \sqrt{X^{2}+Y^{2}})
= \boxed{39.810611°},$$

so the geodetic-minus-geocentric difference is
$40 - 39.810611 = \boxed{0.189389°}$ — which is about $21.0$ km of ground distance
at that latitude.

**(e)** The closed-form inverse recovers

$$\varphi_{\text{recovered}} = \boxed{40.000000000°}, \qquad
\text{error} = 0.000e+00° .$$

An exact round trip is the acceptance test for an ECEF implementation. **Test it at a
high latitude as well as a mid one**: the closed form is stable there, as exercise
★★★10 shows, but an iterative inverse that is not well initialised will struggle.

---

## ★★5 — Geodetic versus geocentric latitude

**(a)** Writing the ellipsoidal transformation as

$$X = N\cos\varphi\cos\lambda, \qquad
Y = N\cos\varphi\sin\lambda, \qquad
Z = N(1-e^{2})\sin\varphi,$$

the horizontal distance from the axis is $p = \sqrt{X^{2}+Y^{2}} = N\cos\varphi$, so

$$\tan\varphi_{\text{geocentric}} = \frac{Z}{p}
= \frac{N(1-e^{2})\sin\varphi}{N\cos\varphi} = (1-e^{2})\tan\varphi .$$

The prime vertical radius $N$ cancels, so the relation is exact and depends only on
the flattening. **That cancellation is worth noticing**: it means the
latitude difference is a property of the ellipsoid's *shape*, not of its size.

**(b)–(c)**

| geodetic latitude | geocentric latitude | difference | ground distance |
|---|---|---|---|
| $0°$ | 0.000000° | 0.000000° | 0.00 km |
| $15°$ | 14.904067° | 0.095933° | 10.61 km |
| $30°$ | 29.833636° | 0.166364° | 18.44 km |
| $45°$ | 44.807577° | 0.192423° | 21.38 km |
| $60°$ | 59.833076° | 0.166924° | 18.60 km |
| $75°$ | 74.903507° | 0.096493° | 10.77 km |
| $90°$ | 90.000000° | 0.000000° | 0.00 km |

The ground distances use the meridional radius of curvature
$M(\varphi)$, and they **peak near $45°$ at $21.38$ km**. The difference vanishes at
the equator and at the pole, where the local vertical and the radius vector coincide.

**(d)** A workflow that mixes the two: **comparing a GNSS-derived position with a
spherical-harmonic gravity model.** The GNSS gives geodetic latitude; the model is
naturally evaluated in geocentric coordinates. Passing the geodetic latitude
directly into a geocentric expression misplaces the evaluation point by up to
$21.4$ km, which for a gravity model is a change in the mass-anomaly field far larger
than the anomalies being interpreted. The same confusion affects satellite orbit
geometry, geomagnetic field models and any conversion between a geocentric frame and
a map grid.

---

## ★★6 — Direction cosines

**(a)** With azimuth $A$ clockwise from north, the horizontal unit vector is
$(\text{east}, \text{north}) = (\sin A, \cos A)$, so

$$(l, m, n) = (\sin i\,\sin A,\ \sin i\,\cos A,\ -\cos i) .$$

**(b)**

| $i$ | $A = 0°$: $(l, m, n)$ | $A = 135°$: $(l, m, n)$ |
|---|---|---|
| $0°$ | $(0, 0, -1)$ | $(0, 0, -1)$ |
| $30°$ | $(0, 0.500000, -0.866025)$ | $(0.353553, -0.353553, -0.866025)$ |
| $60°$ | $(0, 0.866025, -0.500000)$ | $(0.612372, -0.612372, -0.500000)$ |
| $90°$ | $(0, 1.000000, 0)$ | $(0.707107, -0.707107, 0)$ |

For $A = 135°$, $\sin 135° = 0.7071068$ and $\cos 135° = -0.7071068$. Since $A$ is
measured clockwise from north, $135°$ lies between $90°$ (east) and $180°$ (south),
so the direction is south-east; the components
$(\text{east}, \text{north}) = (0.7071, -0.7071)$ are a positive easting and a
negative northing, which is exactly south-east ✓.

**(c)** $l^{2}+m^{2}+n^{2} = \sin^{2}i(\sin^{2}A+\cos^{2}A) + \cos^{2}i = 1$ at every
row, identically. **This is the check to implement**, because a sign error, a
swapped sine/cosine, or a degree/radian confusion breaks it — and nothing else in a
ray-geometry calculation will complain.

**(d)** The vector $(\cos A\sin i,\ \sin A\sin i,\ -\cos i)$ has the same
*downward component* $- \cos i$, so **the take-off angle is correct**, but the
horizontal direction is $(\cos A, \sin A)$ in (east, north), whose azimuth is
$\operatorname{atan2}(\cos A, \sin A) = 90° - A$.

So the implementation describes a ray whose azimuth is **mirrored about $45°$**:
azimuths $0°$ and $90°$ are interchanged — north becomes east and east becomes
north. The error vanishes when $90° - A = A \bmod 360°$, i.e. at $A = 45°$ and
$A = 225°$, and is largest at $A = 0°, 90°, 180°, 270°$ where the error is exactly
$90°$.

**The practical trap.** The cardinal directions are the *worst* cases for this bug,
and they are exactly the cases people test first — so a test suite of due-north and
due-east rays would flag it, while a suite of oblique rays might not. Conversely, an
implementation tested only at $45°$ would pass perfectly and be wrong everywhere
else.

---

## ★★7 — The chord identity

**(a)** In the triangle formed by the two points $P$, $Q$ and the centre $O$, the two
radii $OP = OQ = R$ are equal and the apex angle is $\Delta$. Drop the perpendicular
from $O$ to the chord; it bisects both the apex angle and the chord, giving a right
triangle with hypotenuse $R$, one acute angle $\Delta/2$, and the opposite side
$d_{\text{chord}}/2$. Hence

$$\sin\frac{\Delta}{2} = \frac{d_{\text{chord}}/2}{R}
\ \Longrightarrow\
d_{\text{chord}} = 2R\sin\frac{\Delta}{2} .$$

**(b)** For $(45°\text{N}, 10°\text{E})$ on $R = 6371.0088$ km:

$$x = R\cos\varphi\cos\lambda = 6371.0088 \times 0.7071068 \times 0.9848078
= \boxed{4436.542703\ \text{km}},$$

$$y = R\cos\varphi\sin\lambda = 6371.0088 \times 0.7071068 \times 0.1736482
= \boxed{782.282180\ \text{km}},$$

$$z = R\sin\varphi = 6371.0088 \times 0.7071068 = \boxed{4504.983525\ \text{km}} .$$

**(c)** For $(45.5°\text{N}, 10.5°\text{E})$ the same formulas give
$(4390.723896, 813.772573, 4544.124888)$ km, so

$$d_{\text{chord}} = \sqrt{(4390.723896-4436.542703)^{2}
+ (813.772573-782.282180)^{2}
+ (4544.124888-4504.983525)^{2}}$$

$$= \sqrt{2099.2918 + 991.6105 + 1532.1768} = \sqrt{4623.0791}
= \boxed{67.993046\ \text{km}} .$$

**(d)** The central angle between the two points, from the spherical law of cosines,
is $\Delta = 0.611478209° = 0.010672308$ rad, so the chord identity gives

$$d_{\text{chord}} = 2 \times 6371.0088 \times \sin(0.305739104°)
= 12742.0176 \times 0.005335674 = 67.993046\ \text{km},$$

which agrees with (c) to the printed precision (the two routes differ by
$5.6\times10^{-11}$ km, i.e. 56 nanometres). **In production, use the Cartesian
route when your data are already Cartesian or when the separation is small**, because
it involves no trigonometric functions of nearly equal arguments and it can be
vectorised. Use the chord identity when you have a central angle and need a distance,
or when you want the shortest-path (surface) distance rather than the straight-line
one — they differ by the factor $\sin(\Delta/2)/(\Delta/2)$, which is 0.4 percent at
$10°$ of arc.

---

## ★★8 — The pole problem

**(a)** One degree of north–south arc on $R = 6371.0088$ km is
$R \times \pi/180 = 111.194927$ km at every latitude. One degree of east–west arc is
$111.194927\cos\varphi$ km:

| latitude | north–south | east–west | ratio |
|---|---|---|---|
| $60°$ | 111.194927 km | 55.597450 km | 2.000 |
| $80°$ | 111.194927 km | 19.308792 km | 5.759 |
| $89.9°$ | 111.194927 km | 0.194072 km | 572.96 |

**(b)** As a regular latitude–longitude grid approaches the pole, the number of
cells per unit area grows as $1/\cos\varphi$, because each cell's east–west extent
shrinks while its north–south extent does not. At $89.9°$N a cell is 573 times longer
north–south than east–west, and the cell count per unit area is 573 times the
equatorial value. The grid is **anisotropic and over-dense** near the pole, and at
the pole itself the azimuth is undefined and the cells degenerate to points.

**(c)** An interpolated or contoured dipole anomaly on such a grid shows a
**bullseye artefact at the pole**: a spurious concentration of contours, and
sometimes an apparent anomaly, because equal-value contours must crowd into a
region where the sampling is extremely dense in longitude and where the
interpolation stencil is effectively a long thin strip. The cause is the grid, not
the field: the same data on a cubed-sphere or equal-area grid do not show it. **The
remedy is either to regrid to an equal-area or locally Cartesian layout before
contouring, or to contour in three dimensions and project the result.** Note that
this is a *sampling* artefact layered on top of the genuine $1/\cos\varphi$
amplification that any poleward calculation inherits.

---

## ★★★9 — Ill-conditioning near the polar axis

**(a)**

- from $(89.9999°\text{N}, 0°\text{E})$ to $(89.9999°\text{N}, 90°\text{E})$:
  azimuth $= \boxed{45.000000°}$;
- from $(89.9999°\text{N}, 0°\text{E})$ to $(89.9999°\text{N}, 180°\text{E})$:
  azimuth $= \boxed{0.000000°}$, i.e. **due north**.

The second result is the geometric point: the shortest path from one point near the
pole to the antipodal meridian **passes over the pole**, so the initial heading is
due north regardless of the longitude difference. Any formula that returns "due
south" or "east" here is using a plane-geometry intuition on a sphere.

**(b)** Perturbing the starting latitude upward:

| perturbation | azimuth change (case 1, $90°$ of longitude) |
|---|---|
| $10^{-6}°$ | $0.2879°$ |
| $10^{-5}°$ | $3.0128°$ |
| $10^{-4}°$ | $45.0000°$ |

**(c)** The amplification is enormous: an input change of $10^{-6}°$ produces an
output change of $0.29°$, a factor of $2.9\times10^{5}$; and $10^{-4}°$ produces
$45°$, a factor of $4.5\times10^{5}$. **An azimuth measured within a fraction of a
degree of the pole is meaningless**: it is determined by position errors that are
thousands of times smaller than the azimuth itself, and it changes discontinuously
as the path flips across the pole.

**(d)** The same calculation at lower latitudes, again perturbing the starting
latitude by $10^{-6}°$ and using a $90°$ longitude span:

| starting latitude | azimuth | azimuth change | amplification |
|---|---|---|---|
| $89.9999°$N | $45.000000°$ | $0.287916°$ | $2.88\times10^{5}$ |
| $89.9°$N | $45.000044°$ | $0.000286°$ | $2.87\times10^{2}$ |
| $89.0°$N | $45.004364°$ | $0.000029°$ | $2.86\times10^{1}$ |

The azimuth itself stays near $45°$ while the longitude span is $90°$; what changes
is the *sensitivity*, which falls by three orders of magnitude as the starting point
moves from $0.0001°$ to $1°$ from the pole. The amplification scales as
$1/\sin(\text{colatitude})$, the same factor that governs the shrinking of a
parallel — **so the conditioning degrades continuously as the geometry approaches
the singular set, and there is no threshold at which it suddenly "breaks".** **The conditioning is a function of how close the
geometry is to the singular set, and it degrades continuously.**

**(e)** What to do near the pole:

- **Do not report an azimuth within roughly a degree of the pole** without stating
  the position uncertainty, because the azimuth uncertainty is that uncertainty
  amplified by $1/\sin(\text{colatitude})$.
- **Switch to a local Cartesian frame** (a polar stereographic projection, or a
  tangent-plane ENU frame) for all metric work near the pole. In such a frame there
  is no singularity: distances, azimuths and areas are all well defined, and the
  only cost is that the frame is local.
- The general principle: **a coordinate singularity is a place where the coordinate
  system lies, not where the physics does.** Choose a different system.

---

## ★★★10 — Verifying an ECEF implementation globally

**(a)–(b)** Round-tripping over a grid of latitudes $-89°$ to $89°$ in $2°$ steps,
longitudes $-180°$ to $170°$ in $10°$ steps, and heights of $0$ and $5000$ m —
about $16\,000$ points — the worst errors are:

| quantity | worst error | location of worst case |
|---|---|---|
| latitude | $2.9\times10^{-7}°$ ($\sim3$ cm) | $(-55°,\ -180°,\ h = 5000\ \text{m})$ |
| longitude | $0.0°$ | — |
| height | $8.3\times10^{-5}$ m | $(-55°,\ -180°,\ h = 5000\ \text{m})$ |

**Absolute, not relative, errors are the right measure here**, because latitude and
longitude are angles whose numerical scale is unrelated to metres. Convert:
$2.9\times10^{-7}° \times 111.2$ km $= 3.2$ cm. So the closed-form inverse is
accurate to centimetres in position and a tenth of a millimetre in height over this
grid — far better than any geodetic observation.

**(c)** A restricted grid reaching $89.9999°$N gives **zero** error in the recovered
latitude, at every longitude, for every height tested. The inverse does not degrade
at the pole.

**(d)** The reason is that the closed-form inverse determines the latitude from the
ratio $Z/p$, where $p = \sqrt{X^{2}+Y^{2}}$, and near the pole $Z$ is large while $p$
is small and *well determined by the two horizontal coordinates* — there is no
cancellation. The azimuth $\operatorname{atan2}(Y, X)$, by contrast, is undefined
there, because both $X$ and $Y$ approach zero and the angle they define becomes
arbitrary.

**This is the distinction worth carrying away: an *undefined* coordinate and an
*inaccurate* one are different things.** The polar azimuth is undefined — no amount
of precision helps, because any value describes the same point. The polar latitude is
perfectly well determined. A routine that returns an arbitrary value for an
undefined quantity is behaving correctly; a routine that returns an inaccurate value
for a defined quantity is not. **Know which of the two you are dealing with, and
document it.**

**(e)** What the verification does **not** detect:

- **A wrong datum.** If both the forward and inverse transformations use the same
  wrong $a$ and $f$, every round trip is exact and every answer is displaced by tens
  of metres relative to WGS84. Round trips test *internal consistency*, never
  correctness of the constants.
- **A longitude convention error**, if applied symmetrically in both directions.
- **A sign error in the height** that happens to commute with the sign of $Z$.
- **Degenerate points on the polar axis or at the centre**, which round-trip
  trivially (the azimuth is arbitrary on both legs) and must be tested separately by
  asserting behaviour rather than accuracy.

The fix for the first two is a *third-party check*: compare against a point whose
WGS84 coordinates are published, or against an independent implementation.
**Internal consistency is necessary and never sufficient.**
