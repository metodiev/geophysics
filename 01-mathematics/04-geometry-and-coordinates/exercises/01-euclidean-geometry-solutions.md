# Solutions — 01-04-01 Euclidean Geometry and Geometric Reasoning

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed; spherical quantities use $R = 6371.0088$ km. The
> Eratosthenes exercise is deliberately conditional, because the unit conversion is
> not known exactly — see the lesson, Section 6.

---

## ★1 — Angles and polygons

**(a)** Let $ABC$ be a triangle. Draw the line through $A$ parallel to $BC$. The
angle between this line and $AB$, on the far side of $A$ from $BC$, equals $B$,
because it is an alternate interior angle with the transversal $AB$. Likewise the
angle between the line and $AC$ equals $C$. The two transferred angles plus $A$
itself lie on one side of a straight line, so

$$B + A + C = 180° .$$

The result uses the **parallel postulate** (or an equivalent): in a geometry without
it, the angle sum need not be $180°$, and on a sphere it is not.

**(b)** For a convex $n$-gon, choose one vertex and draw the $n-3$ diagonals to the
non-adjacent vertices. This partitions the polygon into $n-2$ triangles, each
contributing $180°$, so the interior-angle sum is $(n-2)\times180°$. The
construction requires convexity so that the diagonals stay inside; for a
non-convex polygon the *signed* angle sum is still $(n-2)\times180°$, but the
individual interior angles include reflex angles.

**(c)** Pentagon: $(5-2)\times180°/5 = 108°$. Hexagon:
$(6-2)\times180°/6 = 120°$. Only the hexagon tiles the plane because a tiling
requires a whole number of interior angles to meet at each vertex and sum to
$360°$: with $120°$ three meet exactly ($3\times120 = 360$), with $108°$ it would
take $360/108 = 3.33$ of them, which is not an integer, so pentagons cannot tile
without gaps or overlaps.

**Why this is not trivia.** The same counting argument governs the sphere: a
regular spherical tiling needs the excess shared among the vertices, which is why
only five regular polyhedra exist. The counting is a curvature argument in
disguise, and it is the discrete form of the statement that the Earth's curvature
forces distortion in any map.

---

## ★2 — Similar triangles in the field

**(a)** Both objects are vertical on level ground, and the Sun's rays are parallel,
so each object and its shadow form a right triangle, and the two right triangles
have a common acute angle (the solar elevation). Therefore they are similar by
**AA** (two angles equal).

**(b)** Corresponding sides are in proportion:

$$\frac{h_{\text{tower}}}{40.0\ \text{m}} = \frac{2.00\ \text{m}}{3.50\ \text{m}}
\ \Longrightarrow\
h_{\text{tower}} = 40.0 \times \frac{2.00}{3.50} = \boxed{22.857\ \text{m}} .$$

**(c)** Two realistic failures:

1. **The ground is not level.** A shadow cast on sloping ground is shorter or
   longer than the horizontal projection, and the triangle is no longer similar to
   the pole's. Detection: measure the slope along the shadow, or repeat the
   measurement from the other side and compare.
2. **The shadows are not simultaneous.** The solar elevation changes with time, so
   the two triangles have different acute angles. Detection: measure both shadows
   within a minute or two, or measure the solar elevation directly at each by a
   clinometer and confirm it is the same.

A third failure worth naming: **penumbra**. The Sun is an extended source, so a
shadow has a fuzzy edge whose width grows with distance; on a 40 m shadow the
penumbra can be tens of centimetres wide, which sets the precision of the
measurement. Report the height to the precision the shadow edge supports —
$22.9$ m, not $22.857$ m.

---

## ★3 — Triangle areas, three ways

**(a) Heron.** With $a = 7$, $b = 9$, $c = 11$:

$$s = \frac{7+9+11}{2} = 13.5,$$

$$A = \sqrt{13.5 \times (13.5-7) \times (13.5-9) \times (13.5-11)}
= \sqrt{13.5 \times 6.5 \times 4.5 \times 2.5} = \sqrt{987.1875}
= \boxed{31.4195400985} .$$

**(b) Half-product.** The angle opposite the longest side, taken as $C$ with $c =
11$, comes from the law of cosines:

$$\cos C = \frac{a^{2}+b^{2}-c^{2}}{2ab}
= \frac{49+81-121}{126} = \frac{9}{126} = 0.0714286,$$

$$C = 85.9039562°,$$

$$A = \tfrac12 ab\sin C = \tfrac12(7)(9)(0.9974455)
= \boxed{31.4195400985} .$$

The two agree to all printed digits. **This is the expected outcome, not a
coincidence**: Heron's formula is *derived* from the half-product form, as the
lesson shows in Section 5.1.

**(c)** (i) Three sides measured → **Heron** (or the half-product with an angle
found from the law of cosines; both are available). (ii) Two sides and the
included angle measured → **half-product**, directly and without a square root of a
difference.

The reason to prefer the half-product when the angle is available is numerical.
Heron's formula multiplies four factors, and if the triangle is nearly degenerate
one of those factors is nearly zero: a flat triangle has an area that is a small
product of small numbers, so its relative error is amplified. The half-product
form has one multiplication and one sine, and its relative error is that of the
inputs. **When both routes are available, compute the one that avoids a
difference.**

---

## ★4 — Thickness relations

**(a)** The vertical thickness is $V = 400$ m and the true (perpendicular)
thickness is the projection onto the bed normal:

$$t = V\cos 25° = 400 \times 0.9063078 = \boxed{362.523\ \text{m}} .$$

**(b)** For a borehole inclined at angle $i$ from the vertical in the plane
perpendicular to strike, the thickness measured along the hole is the projection of
the same perpendicular thickness onto the hole direction. The angle between the
hole and the bed normal is $(25° - 20°) = 5°$, so

$$t_{\text{hole}} = \frac{t}{\cos 5°} = \frac{362.523}{0.9961947}
= \boxed{363.908\ \text{m}} .$$

A sanity check: the hole is steeper than the bed's dip by $5°$, so it crosses the
bed at a slightly oblique angle and must travel slightly further to cover the same
perpendicular thickness. $363.9 > 362.5$ ✓.

**(c)** They differ because each is a *projection of the same perpendicular
thickness onto a different direction*: a stratigrapher wants the perpendicular
(true) thickness, because that is the property of the rock, while the log records
the along-hole length, which is a property of the drilling. **The conversion
between them needs the relative angle between the hole and the bed, not merely the
dip** — which is why a directional survey is essential for a deviated well: without
knowing the hole's orientation you cannot convert the log to a thickness.

---

## ★★5 — Spherical cap areas

**(a)** $A = 2\pi R^{2}(1-\cos\alpha)$ with $\alpha = 45°$:

$$A = 2\pi (6371.0088)^{2}(1 - 0.7071068)
= 2\pi \times 40\,589\,753.1 \times 0.2928932
= \boxed{7.4697419\times10^{7}\ \text{km}^{2}} .$$

**(b)** At $\alpha = 5°$:

$$A = 2\pi \times 40\,589\,753.1 \times (1-0.9961947)
= \boxed{9.7047734\times10^{5}\ \text{km}^{2}} .$$

The whole sphere is $4\pi R^{2} = 5.1006588\times10^{8}$ km², so the fraction is

$$\frac{9.7047734\times10^{5}}{5.1006588\times10^{8}} = 1.9027\times10^{-3},$$

i.e. **0.19 percent** of the Earth's surface. A "5 degree" region sounds small and
is nearly a fifth of a percent of the globe — about $9.7\times10^{5}$ km², or
roughly the area of Egypt and Libya together.

**(c)** At $\alpha = 90°$: $\cos 90° = 0$, so $A = 2\pi R^{2}$, exactly half of
$4\pi R^{2}$. The limit is a **hemisphere**, and the fact that the formula returns
exactly half the sphere is the strongest available check on it.

**(d)** The region above $2°$N inside a $5°$ cap is a cap of half-angle $3°$ (since
$5 - 2 = 3$), so the fraction is

$$\frac{1-\cos 3°}{1-\cos 5°}
= \frac{0.0013704652}{0.0038053019} = 0.360146,$$

i.e. **36.01 percent** of the region.

The approximation: the cap is taken as spherical about its own centre, so the
"above $2°$N" boundary is treated as a small circle at $3°$ from the centre. For a
cap at the equator this is exact to the order of the curvature corrections
involved — but the region's *shape* is not a disc in longitude–latitude
coordinates, and if you compute the fraction by counting grid cells you will get a
slightly different answer that depends on your grid's latitude weighting. **Say
which you computed.**

---

## ★★6 — Flat versus spherical area

**(a) Spherical, from the excess.** For an equilateral spherical triangle of side
$d$, the interior angle $A$ satisfies
$\cos d = \cos^{2}d + \sin^{2}d\cos A$, so
$\cos A = \cos d/(1+\cos d)$ and the excess is $E = 3A - \pi$. Numerically:

| $d$ | angle $A$ | excess $E$ (rad) | spherical area (km²) |
|---|---|---|---|
| $1°$ | 60.0025193° | $1.31908\times10^{-4}$ | 5354.1 |
| $10°$ | 60.2528797° | $1.324075\times10^{-2}$ | 537438.8 |
| $30°$ | 62.3479044° | $0.122935987$ | 4989941.3 |
| $60°$ | 70.5287794° | $0.551285598$ | 22376546.3 |

**(b) Planar, from the chords.** The chord for side $d$ is
$2R\sin(d/2)$, and Heron's formula on three equal chords of length $\ell$ gives
$\left(\sqrt{3}/4\right)\ell^{2}$:

| $d$ | chord $2R\sin(d/2)$ (km) | planar area (km²) |
|---|---|---|
| $1°$ | 111.1937 | 5353.8 |
| $10°$ | 1110.5400 | 534034.2 |
| $30°$ | 3297.8768 | 4709442.5 |
| $60°$ | 6371.0088 | 17575878.7 |

**(c)** Ratios (planar/spherical):

| $d$ | ratio | discrepancy |
|---|---|---|
| $1°$ | 0.9999 | 0.01 percent |
| $10°$ | 0.9937 | 0.63 percent |
| $30°$ | 0.9438 | 5.62 percent |
| $60°$ | 0.7855 | 21.45 percent |

The discrepancy grows roughly as $d^{2}$: from $1°$ to $10°$ it grows by about
$10^{2}$, from $10°$ to $30°$ by about $3^{2} \times 1.4$. Exercise ★★★10 fits the
exponent properly.

**(d)** Solving the ratio for a 1 percent discrepancy numerically gives
**$d = 12.5705°$**, i.e. $12.5705 \times 111.2 = 1398$ km. **So a "flat-Earth"
area calculation is good to 1 percent out to an equilateral triangle roughly
1400 km across** — larger than many users expect, and exactly why the error is
usually invisible until it is large.

---

## ★★7 — A conditional Eratosthenes

**(a)** $d = 5000 \times 157.5\ \text{m} = 787.5$ km, and
$\Delta\theta = 7.2° = 0.12566371$ rad, so

$$R = \frac{d}{\Delta\theta} = \frac{787.5}{0.12566371}
= \boxed{6266.73\ \text{km}} .$$

**(b)** Against $R = 6371.0088$ km the difference is
$-104.28$ km, i.e. $\boxed{-1.637\ \text{percent}}$.

**(c) Conditional table:**

| assumed stadion | distance (km) | implied $R$ (km) | difference from mean |
|---|---|---|---|
| 148 m | 740.0 | 5889.35 | $-7.6$ percent |
| 157.5 m | 787.5 | 6266.73 | $-1.64$ percent |
| 185 m | 925.0 | 7361.70 | $+15.5$ percent |

**(d)** The accuracy of the ancient measurement cannot be separated from the
assumed length of the unit, because a stadion is not defined by any surviving
artefact or physical standard; different Greek cities used different values, and
the range of plausible values (roughly 148 m to 185 m) spans an implied radius from
about 5900 km to 7400 km. Therefore any quoted "error" is a statement about the
conversion factor the modern author chose, not about the ancient observer's skill.
What *is* defensible is the method: a shadow angle, a distance along a meridian,
and one proportion, all of which are geometrically correct.

**A note on the discipline.** This is a case where a number *can* be computed but
its uncertainty is dominated by an external convention. The correct treatment is to
report the conditional table, as above, rather than to quote a single figure. The
same discipline applies to any historical measurement expressed in units that have
not survived — and to modern measurements expressed in datums that have been
superseded.

---

## ★★8 — Setting out and levelling

**(a)** Exact sagitta for a chord $L$ on a circle of radius $R$:

$$s = R - \sqrt{R^{2} - (L/2)^{2}}
= 6371 - \sqrt{6371^{2} - 0.5^{2}}\ \text{km} .$$

With $6371^{2} = 40589641$ and $0.5^{2} = 0.25$, the square root is
$\sqrt{40589640.75} = 6370.99998037$ km, so

$$s = 6371 - 6370.99998037 = 1.962\times10^{-5}\ \text{km}
= \boxed{19.62\ \text{mm}} .$$

The parabolic approximation $L^{2}/(8R)$ gives

$$\frac{1.000^{2}\ \text{km}^{2}}{8 \times 6371\ \text{km}} = 1.9620\times10^{-5}
\ \text{km} = 19.62\ \text{mm},$$

agreeing to all printed digits. **Two expressions agreeing here is worth noting**:
the drop-below-the-tangent formula $d^{2}/(2R)$ and the sagitta $L^{2}/(8R)$ are
different quantities — one is the maximum deviation from the tangent at the
midpoint of a *chord*, the other from the tangent at one end — and they differ by a
factor of four. Confusing them is a classic survey error. Here the chord is 1 km, so
the sagitta is 19.62 mm; the drop at the *end* of a 1 km horizontal line relative
to the tangent at the *start* would be $1000^{2}/(2\times 6371000) = 78.5$ mm.

**(b)** Each half of the straight drive is $5.000$ km from the vertex, so the chord
is $10.000$ km and the maximum offset at its mid-point is the sagitta

$$s = \frac{L^{2}}{8R} = \frac{10.000^{2}}{8 \times 6371.0088}
= 1.9620\times10^{-3}\ \text{km} = \boxed{1.962\ \text{m}} .$$

**(c)** The offset scales as $L^{2}$, so at the same geometry:

| chord $L$ | sagitta |
|---|---|
| 100 m | 0.196 mm |
| 500 m | 4.905 mm |
| 1 km | 19.62 mm |
| 10 km | 1.962 m |

A 100 m foundation is $0.2$ mm out of true — far below any construction tolerance,
which is why nobody applies the correction. A pipeline or tunnel with a 10 km
straight run is nearly 2 m out, and 2 m is comparable to the design offset between
the bore and the surrounding infrastructure. **The correction matters because the
deviation grows as $L^{2}$ while tolerances are roughly constant**, so there is a
crossover length beyond which the geometry, not the construction, sets the error.
Note also that the *cumulative* effect across a long route is larger than any single
chord: a sequence of straight chords each deviating a couple of metres produces a
systematic lengthening of the route as well as a lateral offset.

---

## ★★★9 — Verifying the area formulas

**(a)–(b)** Sampling $10^{4}$ triangles from the unit square and computing all
three areas, the worst absolute discrepancy between the shoelace/cross-product
formula and Heron's is of order $10^{-13}$ in unit-square coordinates, and the
shoelace and half-product forms agree to about $10^{-15}$.

**The reason the cross-product and half-product forms agree most closely** is that
they are, algebraically, the *same expression*: the cross product of two edge
vectors has magnitude $ab\sin C$ for the included angle $C$, so
$\tfrac12|\mathbf{u}\times\mathbf{v}|$ and $\tfrac12ab\sin C$ differ only in which
route the sine is computed by. Their agreement therefore tests the arithmetic and
not the formula.

**The check with real content is Heron's**, because it starts from three side
lengths and reconstructs an area without ever forming an angle. That it agrees with
the cross product to $10^{-13}$ is evidence that the derivation of Heron's formula
is correctly implemented — but note again that it is a *derived* result, so
agreement is expected in exact arithmetic and the test is really about
implementation.

**(c)** Heron's formula is worst for **nearly degenerate triangles** — three nearly
collinear points. Then one of the factors $s - (\text{longest side})$ becomes a
difference of nearly equal numbers, and beyond a threshold the subtraction returns
exactly zero, so the computed area is zero instead of small. Measured on a family
of isosceles triangles with base $L$ and apex height $h$, comparing Heron's formula
with the cross-product area:

| base $L$ | height $h$ | aspect $L/h$ | Heron area | cross-product area | Heron/cross |
|---|---|---|---|---|---|
| 100 m | 0.02 m | $5.0\times10^{3}$ | 1.0000000010 | 1.0000000000 | 1.000000 |
| $10^{4}$ m | 2 m | $5.0\times10^{3}$ | 10000.000005 | 10000.000000 | 1.000000 |
| $10^{5}$ m | 2 m | $5.0\times10^{4}$ | 100000.01695 | 100000.00000 | 1.0000002 |
| $10^{6}$ m | $2\times10^{-4}$ m | $5.0\times10^{9}$ | **0.0** | 100.0000000 | **0.0** |
| $10^{8}$ m | $2\times10^{-8}$ m | $5.0\times10^{15}$ | **0.0** | 1.0000000000 | **0.0** |

At an aspect ratio of $5\times10^{3}$ the relative error is around $10^{-9}$; at
$5\times10^{4}$ it is $1.7\times10^{-7}$; and once the aspect ratio approaches the
reciprocal of double precision the result collapses to zero while the
cross-product formula remains exact. **The remedy is to compute the area from the
coordinates with a cross product**, which never forms the difference
$s - \text{longest side}$.

**A note on realism.** Bases of $10^{6}$ m with micrometre-scale lateral offsets are
extreme, but the mechanism is not: any workflow that forms areas from side lengths —
a closed traverse, a polygonal claim, a cell of a triangulated surface — is exposed
to it, and the error grows smoothly with the aspect ratio rather than appearing
suddenly. Report areas from coordinates whenever you have coordinates.

**(d)** What the test would **not** catch: an error in the *side lengths* shared by
all three methods. If the coordinates were, say, in a rotated or scaled frame with
a systematic error, all three areas would be wrong together and their mutual
agreement would be perfect. The test checks the *area formulas*, not the
*coordinates*. A separate check is needed for the coordinates — for instance,
verify that a known-distance pair of vertices reproduces its distance, or check a
polygon whose area is known independently.

---

## ★★★10 — How the flat-versus-spherical error scales with size

**(a)–(b)** Computing the ratio $r(d)$ of the planar chord-triangle area to the
spherical area for equilateral triangles with $d$ from $0.1°$ to $80°$ and fitting
a power law to $1 - r(d)$ gives an exponent close to **2** — the fit slope on
log–log axes is approximately $2.0$, with the deviation from 2 growing for the
largest triangles.

**(c)** The theoretical expectation is consistent with an exponent of 2. The leading
correction to the spherical law of cosines is
$a_{\text{sph}}^{2} = a_{\text{pl}}^{2} - \tfrac13(bc\sin A)^{2} + \cdots$, and
since area scales as the square of a side, a relative area correction of order
$d^{2}$ follows immediately: $(1-r) \propto d^{2}$. That the measured exponent is
close to 2, and that it drifts above 2 as $d$ grows, is exactly what a series with a
leading $d^{2}$ term and a positive $d^{4}$ term would produce — **the drift is
evidence for the higher-order term, not against the leading one.**

**(d)** **Shape dependence.** The exponent is a *leading-order* statement and is
shape-independent, because at leading order the correction comes from the local
curvature and every small triangle looks locally like every other. At large $d$ the
ratio does depend on shape: an equilateral triangle of side $60°$ has a ratio of
0.7855, while a thin triangle with the same maximum side can have a markedly
different ratio, because the excess depends on the enclosed area rather than on the
side length alone. **Evidence to quote:** compute $1-r$ for a thin triangle and an
equilateral one with the same longest side at $d = 30°$ and $60°$; the values differ
in the second digit, whereas at $d = 1°$ they agree to four. So the statement "the
error scales as $d^{2}$" should be read as a *local* statement, valid while the
triangle is small compared with the radius of curvature, and its validity limit is
precisely what the drift in the exponent measures.
