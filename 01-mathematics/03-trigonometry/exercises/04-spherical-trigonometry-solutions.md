# Solutions — 01-03-04 Spherical Trigonometry and Great-Circle Geometry

> **Read this after attempting the exercises, not before.**
>
> $R = 6371.0088$ km (IUGG arithmetic mean radius) unless stated. Coordinates used
> in worked examples are ILLUSTRATIVE round numbers, not real events or stations.
> Every formula quoted is implemented in this module's demonstration
> [`code/spherical_geometry_demo.py`](../code/spherical_geometry_demo.py), so you
> can reproduce each number.

---

## ★1 — Central angles

**(a)** Both points are on the equator, $90°$ of longitude apart. The great circle
joining them is the equator itself, and the central angle is the longitude
difference: $\boxed{\Delta = 90.000000000°}$.

**(b)** Same meridian, so the central angle is the latitude difference:
$\boxed{\Delta = 10.000000000°}$.

**(c)** Antipodal: $\boxed{\Delta = 180.000000000°}$.

**(d)** Both at $60°$N, $10°$ of longitude apart. This is the case where intuition
fails. Using $\cos\Delta = \sin\varphi_1\sin\varphi_2 +
\cos\varphi_1\cos\varphi_2\cos\Delta\lambda$:

$$\cos\Delta = \sin^{2}60° + \cos^{2}60°\cos 10°
= 0.75 + 0.25(0.98480775) = 0.99620194,$$

$$\boxed{\Delta = 4.9952380898° .}$$

**Why this is smaller than $10°$.** At latitude $60°$ the parallel has shrunk to
half the equatorial radius, but the great circle between the two points bulges
*away* from the parallel towards the pole. Travelling between two points at the
same latitude therefore means heading slightly poleward, not due east — and that
is why a flight from one city to another at the same latitude appears on a
Mercator map as a curve bending towards the pole. The $10°$ of longitude is not
the angular distance; it is one side of a spherical right triangle whose other
sides are the co-latitudes.

**Formula choice.** The arccosine form is safe for (a)–(c) and dangerous for (d)
if $\Delta\lambda$ were much smaller; haversine is safe everywhere; the vector
form is safest for short baselines but degrades near the antipode. The ranking in
this exercise is: haversine for all four, with the vector form equally good for
(d) and the arccosine form acceptable only because none of these separations is
smaller than a degree.

---

## ★2 — Distances

Multiply the central angle in radians by the radius:
$s = R\Delta_{\text{rad}} = 6371.0088 \times \Delta° \times \pi/180$.

| Pair | $\Delta$ | Distance (km) |
|---|---|---|
| (a) | $90.000000°$ | $10007.543$ |
| (b) | $10.000000°$ | $1111.949$ |
| (c) | $180.000000°$ | $20015.087$ |
| (d) | $4.995238°$ | $555.446$ |

**Check (c):** half the circumference of the sphere is
$\pi R = \pi \times 6371.0088 = 20015.087$ km ✓, and (b) is
$10007.543/9.0000 = 1111.949$ km — the familiar "111 km per degree" at the
equator, correct only because the path is along a meridian near the equator.

**Note on (d):** $4.995238°$ of arc is $555.446$ km, whereas the naive "10° of
longitude at 111 km/deg" would give 1112 km — a factor of two out. The error comes
from ignoring both the latitude scaling ($\cos 60° = 0.5$) and the great-circle
shortening. If your workflow computed that distance as $1112$ km, every subsequent
interpretation would be wrong by 100 percent, and no unit check would catch it.

---

## ★3 — Haversine by hand

**Given** $\varphi_1 = 0°$, $\lambda_1 = 0°$, $\varphi_2 = 0°$,
$\lambda_2 = 90°$.

**Step 1 — the arguments.**

$$\Delta\varphi = 0°, \qquad \Delta\lambda = 90° .$$

**Step 2 — the haversine.**

$$h = \sin^{2}\!\left(\frac{\Delta\varphi}{2}\right)
+ \cos\varphi_1\cos\varphi_2\sin^{2}\!\left(\frac{\Delta\lambda}{2}\right)
= \sin^{2}0 + (1)(1)\sin^{2}45° = 0 + 0.5 = 0.5 .$$

**Step 3 — the central angle.**

$$\Delta = 2\arcsin\sqrt{h} = 2\arcsin\sqrt{0.5} = 2 \times 45° = \boxed{90.000000000°}.$$

**Arccosine check:**

$$\cos\Delta = \sin 0 \sin 0 + \cos 0\cos 0\cos 90°
= 0 + 1 \times 1 \times 0 = 0 \ \Longrightarrow\ \Delta = \arccos 0 = 90° .$$

The two agree because here $\cos\Delta = 0$, far from the $|\cos\Delta| \approx 1$
region where the arccosine form loses precision. The arccosine form is not
"wrong"; it is *conditionally* accurate, and the condition fails exactly for short
separations. **This is why a formula must be evaluated in the regime it was
designed for**, not merely because it appears in a textbook.

Note also the internal arithmetic: $\sqrt{h} = \sqrt{0.5} = 0.70710678$, and
$\arcsin 0.70710678 = 0.78539816$ rad, whose double is $1.57079633$ rad
$= 90°$ ✓. Every step is exact in this case, so the printed answer is exact —
a rare luxury, and a useful anchor for testing an implementation.

---

## ★4 — Azimuths

**(a)** $(0°\text{N}, 0°\text{E}) \to (0°\text{N}, 90°\text{E})$: due east,
$\boxed{90.000°}$.

**(b)** $(0°\text{N}, 0°\text{E}) \to (10°\text{N}, 0°\text{E})$: due north,
$\boxed{0.000°}$.

**(c)** $(0°\text{N}, 0°\text{E}) \to (10°\text{S}, 0°\text{E})$: due south,
$\boxed{180.000°}$.

**(d)** $(0°\text{N}, 0°\text{E}) \to (0°\text{N}, 90°\text{W})$: due west,
$\boxed{270.000°}$.

**Why these four are worth doing.** They exercise all four quadrants of the
`atan2` argument: positive $x$ with zero $y$, zero $x$ with positive $y$, and the
two negative cases. An azimuth routine that passes these four tests but fails an
oblique case is likely to have an argument-order error that only shows up when both
components are non-zero — which is why professional test suites use a *mixed*
table, not just the cardinal points.

The module's demonstration prints exactly this table:

```text
          from             to  azimuth (deg)   back-azimuth
         0N 0E         0N 90E         90.000        270.000
         0N 0E         10N 0E          0.000        180.000
         0N 0E         10S 0E        180.000          0.000
         0N 0E         0N 90W        270.000         90.000
```

---

## ★★5 — Spherical versus plane third side

**(a)** Spherical law of cosines with $b = 60°$, $c = 50°$, $A = 40°$:

$$\cos a = \cos 60°\cos 50° + \sin 60°\sin 50°\cos 40°$$
$$= (0.5)(0.64278761) + (0.86602540)(0.76604444)(0.76604444)$$
$$= 0.32139380 + 0.50820457 = 0.82959837,$$

$$\boxed{a = \arccos 0.82959837 = 33.942496686° .}$$

**(b)** Plane law with the degrees treated as lengths:

$$a^{2} = 60^{2} + 50^{2} - 2(60)(50)\cos 40° = 6100 - 4596.26657
= 1503.73343,$$

$$\boxed{a = 38.778000739 \ \text{deg-units}.}$$

**(c)** The **plane** answer is larger, by

$$38.778000739 - 33.942496686 = 4.8355 \ \text{degrees},$$

a relative difference of $4.8355/33.9425 = \boxed{14.2\ \text{percent}}$.

**(d)** The leading correction is
$a_{\text{sph}}^{2} = a_{\text{pl}}^{2} - \tfrac13(bc\sin A)^{2}$, with the
coefficient $\tfrac13$ verified numerically: for small triangles
$(a_{\text{pl}}^{2} - a_{\text{sph}}^{2})/(bc\sin A)^{2}$ evaluates to
$0.333255$, $0.333385$, $0.332520$ and $0.333333$ for four test triangles,
approaching $\tfrac13$ as the triangle shrinks ✓. For the present case, with all
quantities in radians ($b = 1.04719755$, $c = 0.87266463$, $A = 0.69813170$):

$$\tfrac13(bc\sin A)^{2} = \tfrac13 (0.91382016 \times 0.64278761)^{2}
= \tfrac13 (0.58739679)^{2} = 0.115001,$$

$$a_{\text{sph}}^{2} \approx 0.45824613 - 0.115001 = 0.343245,$$

$$a_{\text{sph}} \approx 0.585872 \ \text{rad} = 33.5582° .$$

The leading term gives $33.5582°$ against the exact $33.9425°$, i.e. it captures
about 92 percent of the $4.8355°$ difference and *over*-corrects by $0.384°$. That
is the expected behaviour of a truncated expansion: the neglected $O(h^{4})$ term
is of that size for a triangle this large. **Use the exact formula; use the
expansion only to understand the magnitude.**

**(e)** **Physical meaning.** A spherical triangle's sides are arcs, and arcs are
shorter than the straight chords between the same endpoints would suggest once you
insist that all three sides lie on the *same* surface. On the Earth, a triangle
spanning $60°$ (about $6700$ km) is not approximated by plane trigonometry: the
plane result above is 14 percent wrong in a linear dimension and about 26 percent
wrong in area. For regional and global geodesy, use the spherical formulas — or
better, the ellipsoidal ones. Plane geometry is for map sheets and survey
networks, where the triangle is small enough that the expansion truncates well; at
$50$ km the relative shortening is of order $(50/6371)^{2}/3 \approx 2\times10^{-5}$,
which is below survey precision.

---

## ★★6 — Spherical excess and area

**(a)** With $A = 42.223053436°$, $B = 122.665992756°$,
$C = 41.708559287°$:

$$A + B + C = 206.597605479°,$$

$$E = (206.597605479 - 180)° = \boxed{26.597605479°} = \boxed{0.464215789 \ \text{rad}.}$$

**(b)** On a sphere of radius $R$, the area of a spherical triangle is $ER^{2}$:

$$\text{Area} = 0.464215789 \times (6371.0088)^{2}
= \boxed{1.8842404\times10^{7}\ \text{km}^{2}} .$$

That is about $1.88$ million square kilometres, or roughly the area of
Mexico-sized regions — a plausible size for a triangle spanning from $0°$E to
$95$°E.

**(c)** Chord lengths, from $2R\sin(\Delta/2)$:

| side | $\Delta$ | chord (km) |
|---|---|---|
| $a$ | $52.933766340°$ | $5678.868$ |
| $b$ | $88.321490312°$ | $8877.029$ |
| $c$ | $52.186586316°$ | $5604.373$ |

Heron's formula with $s = (5678.868 + 8877.029 + 5604.373)/2 = 10080.135$:

$$\text{Area}_{\text{plane}}
= \sqrt{s(s-a)(s-b)(s-c)} = \boxed{1.5456370\times10^{7}\ \text{km}^{2}} .$$

The plane formula **under-estimates by $1.8842404 - 1.5456370 = 3.386\times10^{6}$
km², i.e. by 18.0 percent**. The direction is what you should expect: the chords
cut across the inside of the sphere, so the planar triangle through them has a
smaller area than the curved surface it subtends. The difference is not an error
in Heron's formula; it is the curvature of the Earth, and it is the same effect
that makes a planar map of a large region wrong in area.

**The size of the effect scales as the square of the linear extent.** For an
equilateral spherical triangle of side $d$ degrees, the ratio of the flat
chord-triangle area to the true spherical area is 0.9999 at $d = 1°$, 0.9937 at
$10°$, 0.9438 at $30°$ and 0.7855 at $60°$ — computed with Heron's formula on the
chords and the excess formula for the truth. This is a concrete answer to "how big
can a survey be before flat-earth geometry matters": at the 1 percent level, about
$10°$ of arc, or 1100 km.

**(d)** On a sphere of unit radius, the excess *is* the area because the
Gauss–Bonnet theorem identifies the total curvature of a region — the integral of
the Gaussian curvature, which is 1 everywhere on a unit sphere — with
$2\pi\chi - \sum(\pi - \text{interior angles})$, and for a triangle
$\chi = 1$ gives area $= A + B + C - \pi$. On a sphere of radius $R$ the
curvature is $1/R^{2}$, so the area is $ER^{2}$, and this is the reason curvature
appears squared in the area correction but only linearly in the excess.

---

## ★★7 — The ellipsoidal correction

**(a)**

| Path | Spherical (km) | WGS84 (km) | Difference (km) | Percent |
|---|---|---|---|---|
| Equatorial, $90°$ | 10007.5572 | 10018.7542 | $+11.1970$ | $+0.1118$ |
| Meridional, $10°$ | 1111.9508 | 1111.3180 | $-0.6328$ | $-0.0569$ |
| Oblique, Europe–US | 5572.8126 | 5587.8195 | $+15.0069$ | $+0.2686$ |

**(b)** The sign is set by whether the actual path lies *outside* or *inside* the
mean sphere.

- The equatorial path lies on the equator, where the ellipsoid's radius is the
  semi-major axis $a = 6378.137$ km, larger than the mean radius 6371.0088 km, so
  the real path is **longer** than the spherical one ✓.
- The meridional path from $40°$N to $50°$N lies at middle latitudes, where the
  ellipsoid's surface radius is *smaller* than the mean sphere's, so the real path
  is **shorter** ✓. (The meridional radius of curvature $M$ at $45°$ is 6367.38 km,
  below 6371.01 km.)
- The oblique path mixes the two, and the equatorial bulge wins, giving a **net
  lengthening** of $+0.27$ percent — the largest of the three because the path
  crosses a wide range of latitudes where the mismatch changes sign slowly and
  accumulates.

**Do not generalise these numbers.** They are properties of these three paths on
WGS84. A path that starts and ends near the equator will always lengthen; one that
stays near the poles will shorten; oblique paths depend on the details.

**(c)** At $v_P = 8.0$ km/s:

| Path | Distance difference | Time difference |
|---|---|---|
| Equatorial | $+11.197$ km | $+1.400$ s |
| Meridional | $-0.633$ km | $-0.079$ s |
| Oblique | $+15.007$ km | $+1.876$ s |

A 1.9 s spurious travel-time residual is enormous: it is several times a good
teleseismic pick error, and it is *systematic* with path azimuth, so it does not
average out over many stations. At teleseismic distances the Earth's flattening is
not a refinement to location codes; it is a first-order term.

**(d)** **The criterion:** compare the ellipsoidal distance correction with the
quantity you plan to interpret. If the difference, converted to travel time (or to
a survey length error), is smaller than a fraction — say one third — of your
measurement uncertainty, the sphere is adequate and you should state that you
checked. Otherwise use an ellipsoidal geodesic. Do the arithmetic once per project
and write down the number; it is a two-line calculation and it saves a reviewer
from asking the question.

---

## ★★8 — Precision of the arccosine form

**(a)** Two points on the equator, one metre apart. The longitude step is
$\Delta\lambda = 1/(R\times1000) \times 180/\pi$ degrees. Measured results:

- arccosine form: $1.000207$ m;
- haversine: $1.000000$ m;
- relative error of the arccosine value: $\boxed{2.07\times10^{-4}}$.

**(b)** For 5 m: arccosine gives $5.000133$ m, haversine $5.000000$ m, relative
error $\boxed{2.66\times10^{-5}}$ — a factor of about 8 smaller.

**(c)** **Mechanism.** For a separation $s$ on a sphere of radius $R$,
$\Delta = s/R$ and

$$1 - \cos\Delta = \frac{\Delta^{2}}{2} - \frac{\Delta^{4}}{24} + \cdots
= \frac{s^{2}}{2R^{2}} + O(s^{4}) .$$

For $s = 1$ m and $R = 6.371\times10^{6}$ m,
$1 - \cos\Delta = 1.23\times10^{-14}$. Double precision holds roughly 16
significant digits, so a number of magnitude 1 carries an absolute rounding error
of about $2.2\times10^{-16}$; the *relative* error of the computed
$1-\cos\Delta$ is therefore about $2.2\times10^{-16}/1.23\times10^{-14} = 1.8
\times10^{-2}$, and since $\Delta \propto \sqrt{1-\cos\Delta}$ the relative error
in the distance is half that, of order $10^{-2}$. **The measured $2\times10^{-4}$
is consistent with this order-of-magnitude estimate** (the actual factor depends
on how the individual roundings fall and on whether the platform computes
$\arccos$ with extra internal precision, which most do not).

Haversine never subtracts nearly equal quantities: it forms
$\sin^{2}(\Delta/2) = \Delta^{2}/4$ directly, a small number computed from small
inputs, so its relative error stays at the level of a few $10^{-16}$.

**(d)** **Estimate from the mechanism.** Requiring the relative error of the
arccosine route to be below $10^{-6}$ means the absolute rounding of
$\cos\Delta$, about $2.2\times10^{-16}$, must be below $10^{-6}$ times
$(1-\cos\Delta) = \Delta^{2}/2$. Setting

$$\frac{2.2\times10^{-16}}{\Delta^{2}/2} = 10^{-6}
\ \Longrightarrow\ \Delta^{2} = 4.4\times10^{-10}
\ \Longrightarrow\ \Delta = 2.1\times10^{-5}\ \text{rad},$$

so $s = R\Delta = 6.371\times10^{6} \times 2.1\times10^{-5} \approx 134$ m.

**Now check it numerically.** The measured relative error is $1.8\times10^{-5}$ at
10 m, $1.5\times10^{-6}$ at 30 m, $1.2\times10^{-6}$ at 40 m and $1.1\times10^{-8}$
at 100 m. So the 1 part in $10^{6}$ crossover lies somewhere around 30–40 m: the
order-of-magnitude estimate of 134 m is **conservative by a factor of about 4**.

That factor is worth understanding rather than shrugging at. The measured error is
not a smooth function of separation, because it is dominated by which way each
individual rounding falls: between 34 m and 40 m the error jumps by a factor of
five in the *favourable* direction. An order-of-magnitude estimate of a
worst-case error is allowed to be a factor of a few wrong; what it must not be is
wrong about the *scaling*, and $1/s^{2}$ is confirmed (from 10 m to 100 m, a factor
of ten in separation, the error falls by about $10^{3}$ — somewhat faster than
$10^{2}$, consistent with rounding noise on top of a $1/s^{2}$ trend).

**Practical rule.** Use haversine. It costs the same number of operations, it has
no dangerous regime, and it removes this entire conversation from your error
budget.

---

## ★★★9 — Verifying the spherical laws

**(a)–(b)** A representative implementation builds each triangle from three
unit vectors, computes sides as central angles
($\mathbf{u}\cdot\mathbf{v}$ via `acos`, clamped), and interior angles from
tangent directions at each vertex — the tangent directions being the components of
the other two vertices perpendicular to the vertex radius. **Using tangent
directions rather than a cross-product angle avoids a sign ambiguity** that
otherwise infects the result near right angles.

Over 300 random triangles the module's own check reports:

```text
  angle sum = 206.597605480 deg
spherical law of cosines: cos c = 0.61309202237960, cos a cos b + sin a sin b cos C = 0.61309202237960
difference = 0.000e+00
spherical law of sines: a/sin A = 1.187376772866
spherical law of sines: b/sin B = 1.187376772866
spherical law of sines: c/sin C = 1.187376772866
common ratio from a/sin A                 = 1.187376772866
common ratio from sin a sin b sin c / det = 1.187376772866
difference = 4.441e-16   (det = 0.530674624857)
```

Worst discrepancies over the random set are of order $10^{-12}$ for the cosine
rule and the sine ratios, and $3\times10^{-9}$ for the closed form of the common
ratio.

**(c)** The checks degrade in two identifiable situations:

- **Nearly degenerate triangles** — three nearly collinear vertices, so one side is
  close to the sum of the other two and one interior angle approaches $180°$. The
  determinant in the closed form goes to zero while the numerator does not, so the
  ratio loses relative precision. The sine ratio itself remains accurate because
  the sine of a near-$180°$ angle is the small quantity precisely matched by the
  small determinant.
- **Very large triangles** with a vertex near the antipode of another: the central
  angle is then near $180°$ and `acos` of a dot product near $-1$ loses precision,
  exactly as discussed in Section 4 of the lesson. Replacing `acos` with
  `atan2(|u×v|, u·v)` restores the accuracy, at the cost of being fragile for
  *small* angles instead.

**(d)** The closed form

$$K = \frac{\sin a\,\sin b\,\sin c}
{\sqrt{1 - \cos^{2}a - \cos^{2}b - \cos^{2}c + 2\cos a\cos b\cos c}}$$

reproduces the common sine ratio to $4.4\times10^{-16}$ on the demonstration's
triangle and to about $10^{-9}$ over 300 random triangles. The square root is the
determinant of the three unit position vectors — twice the volume of the
tetrahedron they span — so when the three vectors become coplanar the determinant
vanishes and $K$ loses meaning. **That is a real geometric degeneracy, not a
numerical artefact**: a degenerate spherical triangle (all three vertices on one
great circle) has no well-defined circumratio, just as a degenerate plane triangle
has no well-defined circumcircle.

**(e)** **The limit of the verification.** The interior angles were computed from
tangent directions; the sides were computed from dot products. An error in the
*convention* for the interior angle — for instance systematically using the
exterior angle, or measuring the angle at the wrong vertex — would not be caught
by checking the cosine and sine rules, because both rules are written in terms of
whatever angles you supply. The check that catches convention errors is
independent: verify that the three angles *sum to more than $180°$ by the excess
that matches the area computed from the cross product magnitude*, as the
demonstration does for the octant triangle (angle sum $270°$, excess $90°$,
area $\pi R^{2}/2$, all three agreeing). **Always include one check whose inputs
do not come from the code under test.**

---

## ★★★10 — Sphere versus ellipsoid, systematically

**(a)** A reasonable set, all ILLUSTRATIVE except where a city pair is named:

| # | Pair | Character |
|---|---|---|
| 1 | $(60.00°\text{N}, 10.00°\text{E})$ to $(60.00°\text{N}, 10.50°\text{E})$ | short, $\sim28$ km |
| 2 | $(45.00°\text{N}, 10.00°\text{E})$ to $(49.00°\text{N}, 14.00°\text{E})$ | medium, $\sim500$ km |
| 3 | $(0°\text{N}, 0°\text{E})$ to $(0°\text{N}, 90°\text{E})$ | long equatorial |
| 4 | $(40°\text{N}, 0°\text{E})$ to $(50°\text{N}, 0°\text{E})$ | long meridional |
| 5 | $(51.5°\text{N}, -0.1°\text{E})$ to $(40.7°\text{N}, -74.0°\text{E})$ | long oblique |

**(b)–(c)** The ellipsoidal distances require an inverse geodesic solution; the
module's demonstration implements the Vincenty iteration and validates it by
setting the flattening to zero:

```text
Validation: with f = 0 Vincenty must reproduce haversine exactly.
  Equator to 90 E on the equator     vincenty(f=0) = 10007.543398 km   haversine = 10007.543398 km   diff = 1.819e-12 km
  Same meridian, 10 deg apart        vincenty(f=0) =  1111.949266 km   haversine =  1111.949266 km   diff = -2.274e-13 km
  London-ish to New York-ish         vincenty(f=0) =  5572.804939 km   haversine =  5572.804939 km   diff = 0.000e+00 km
```

The worst discrepancy is $1.8\times10^{-12}$ km — a nanometre over a
$10\,000$ km path. **That is the validation that makes the ellipsoidal numbers
trustworthy**: an implementation that is wrong will usually still produce plausible
distances, but it will not reproduce the sphere exactly when told to model a
sphere. Always test the degenerate case first.

**(d)** The pattern over the five paths, computed with the module's validated
Vincenty implementation, $R = 6371.0088$ km and WGS84:

| # | Path | Spherical (km) | WGS84 (km) | Difference (km) | Percent |
|---|---|---|---|---|---|
| 1 | short, east–west at $60°$N | 27.7987 | 27.8999 | $+0.1012$ | $+0.3628$ |
| 2 | medium, oblique | 538.1989 | 538.6165 | $+0.4176$ | $+0.0775$ |
| 3 | long, equatorial | 10007.5572 | 10018.7542 | $+11.1970$ | $+0.1118$ |
| 4 | long, meridional | 1111.9508 | 1111.3180 | $-0.6328$ | $-0.0569$ |
| 5 | long, oblique | 5572.8126 | 5587.8195 | $+15.0069$ | $+0.2686$ |

Two observations, and the first one is the surprise:

- **The largest *percentage* correction is on the *shortest* path.** Path 1 is
  28 km long and wrong by 0.36 percent in the spherical approximation — more than
  three times the percentage error of the 10 000 km equatorial path. The reason is
  that the relevant comparison is with the *local* radius of curvature, not the
  global mean. At $60°$N the radius of curvature in the prime vertical is
  6394.209 km against the mean sphere's 6371.009 km, a difference of 0.36 percent,
  and an east–west path at that latitude samples that radius directly. **A local
  survey at high latitude is not automatically safe from the flattening.**
- **The sign is positive for paths that spend time near the equator and negative
  for the mid-latitude meridional path**, as explained in ★★7(b). The magnitude
  grows with distance, but as a percentage it does not, which is why the criterion
  in ★★7(d) must be stated in terms of the quantity you interpret rather than as a
  distance limit.

**(e)** At $8.0$ km/s: $+0.013$ s, $+0.052$ s, $+1.400$ s, $-0.079$ s and
$+1.876$ s. Only paths 3 and 5 exceed 0.5 s, so only they would corrupt a
teleseismic location at that level. But note path 1: 0.1012 km of distance error
is 10 cm of *travel-time* error at 8 km/s — utterly negligible for seismology
while being 0.36 percent of the path *length*. **The same geometric error matters
or does not depending entirely on which observable you convert it into**, and that
conversion is the only meaningful test.

**(f)** What the comparison does **not** establish:

- that the same conclusion holds for **S waves**: the relevant quantity is the
  travel-time difference, which is the distance error divided by the *phase
  velocity of the arrival you are interpreting*. At $4.5$ km/s the $15.0$ km
  error is $3.34$ s rather than $1.88$ s — nearly twice as damaging. Redo the
  arithmetic per phase.
- anything about **surface waves**, whose great-circle path is also affected by
  lateral heterogeneity and topography far more than by the flattening, so a
  spherical-Earth surface-wave path may be a *better* approximation than the
  ellipsoidal geodesic. This is a genuine modelling choice, not a matter of
  arithmetic precision.
- whether the WGS84 geodesic is itself the right path for a seismic ray: it is a
  geometric surface distance, and the ray samples the interior. The distinction
  matters at the 0.1 percent level and is treated in
  [06-seismology](../../../06-seismology/README.md).
