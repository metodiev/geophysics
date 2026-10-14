# Exercises — 01-03-04 Spherical Trigonometry and Great-Circle Geometry

Attempt these **closed-book**. Solutions are in
[`04-spherical-trigonometry-solutions.md`](./04-spherical-trigonometry-solutions.md).
Difficulty: ★ foundational · ★★ applied · ★★★ research-oriented.

Use the IUGG arithmetic mean radius $R = 6371.0088$ km unless told otherwise.
Latitudes are degrees north (negative for south) and longitudes degrees east
(negative for west). Where a calculation requires coordinates, say whether they
are ILLUSTRATIVE.

---

## ★ Foundational

**★1.** Compute the central angle $\Delta$ between each pair:

(a) $(0°\text{N}, 0°\text{E})$ and $(0°\text{N}, 90°\text{E})$
(b) $(40°\text{N}, 0°\text{E})$ and $(50°\text{N}, 0°\text{E})$
(c) $(0°\text{N}, 0°\text{E})$ and $(0°\text{N}, 180°\text{E})$
(d) $(60°\text{N}, 0°\text{E})$ and $(60°\text{N}, 10°\text{E})$

For each, state which of the three formulas (arccosine, haversine, vector) is
safest and why.

---

**★2.** Convert each central angle from ★1 into kilometres. State the radius you
used.

---

**★3.** Compute the central angle between $(0°\text{N}, 0°\text{E})$ and
$(0°\text{N}, 90°\text{E})$ by hand with the haversine formula, showing every
substitution. Then verify with the arccosine form and explain why the two agree
here even though the arccosine form is dangerous at small separations.

---

**★4.** Compute the azimuth from the first point to the second for each pair:

(a) $(0°\text{N}, 0°\text{E})$ to $(0°\text{N}, 90°\text{E})$
(b) $(0°\text{N}, 0°\text{E})$ to $(10°\text{N}, 0°\text{E})$
(c) $(0°\text{N}, 0°\text{E})$ to $(10°\text{S}, 0°\text{E})$
(d) $(0°\text{N}, 0°\text{E})$ to $(0°\text{N}, 90°\text{W})$

---

## ★★ Applied

**★★5.** A spherical triangle has sides $b = 60°$ and $c = 50°$ with included
angle $A = 40°$.

(a) Use the spherical law of cosines to find $a$.
(b) Solve the same numbers with the *plane* law of cosines, treating the degrees
as lengths in a common unit.
(c) Compare. Which is larger, and by how much in degrees and as a percentage?
(d) The leading correction for small triangles is
$a_{\text{sph}}^{2} = a_{\text{pl}}^{2} - \tfrac13(bc\sin A)^{2} + \cdots$
(unverified in this exercise — check it yourself on a small triangle). Evaluate
the leading correction for this case and state whether it explains the difference.
(e) State the physical meaning of the discrepancy: which geometry should you use
for a triangle spanning $60°$ of the Earth?

---

**★★6.** For the triangle with vertices at $(10°\text{N}, 0°\text{E})$,
$(60°\text{N}, 20°\text{E})$ and $(35°\text{N}, 95°\text{E})$, the interior angles
are $A = 42.223053436°$, $B = 122.665992756°$ and $C = 41.708559287°$.

(a) Compute the spherical excess in degrees and radians.
(b) Compute the area of the triangle from the excess, and state the radius used.
(c) Compute the lengths of the three chords between the vertices (each chord is
$2R\sin(\Delta/2)$ for that side), form the planar triangle through those three
chords, and compute its area with Heron's formula. Compare with your answer to (b)
and explain the direction of the discrepancy.
(d) Explain, in one sentence, why the excess *is* the area on a unit sphere.

---

**★★7.** The ellipsoidal correction. For the three paths

- $(0°\text{N}, 0°\text{E})$ to $(0°\text{N}, 90°\text{E})$,
- $(40°\text{N}, 0°\text{E})$ to $(50°\text{N}, 0°\text{E})$,
- $(51.5°\text{N}, -0.1°\text{E})$ to $(40.7°\text{N}, -74.0°\text{E})$,

the module's demonstration reports spherical distances of $10007.5572$ km,
$1111.9508$ km and $5572.8126$ km, and WGS84 geodesic distances of
$10018.7542$ km, $1111.3180$ km and $5587.8195$ km.

(a) Compute the difference and the percentage difference for each.
(b) The signs are not all the same. Explain why, using the equatorial and polar
radii and the shape of each path.
(c) For a $P$-wave speed of $8.0$ km/s, convert each difference into a travel-time
difference in seconds.
(d) State, in one sentence, the criterion you would use to decide whether the
spherical approximation is adequate for a given study.

---

**★★8.** The arccosine distance formula fails at short range.

(a) Show that for two points separated by 1 m the arccosine form returns
$1.000207$ m and haversine returns $1.000000$ m, and compute the relative error.
(b) Repeat for 5 m.
(c) Explain the mechanism in terms of the magnitude of $1 - \cos\Delta$ compared
with double-precision resolution.
(d) At what separation does the arccosine form become accurate to 1 part in
$10^{6}$? Estimate it from the mechanism, then check numerically.

---

## ★★★ Research-oriented

**★★★9.** Verify the spherical cosine and sine rules on random triangles.

(a) Write code that builds $N \ge 200$ random spherical triangles from uniformly
distributed unit vectors, computes the three sides as central angles and the three
interior angles from tangent directions at each vertex, and then checks
$\cos c = \cos a\cos b + \sin a\sin b\cos C$ and the three sine ratios.
(b) Report the worst absolute discrepancy for each check.
(c) Identify the triangles for which the checks degrade, and characterise them
geometrically (nearly degenerate? nearly antipodal? very large?).
(d) Confirm the closed form
$K = \sin a\sin b\sin c / \det$, where
$\det = \sqrt{1 - \cos^{2}a - \cos^{2}b - \cos^{2}c + 2\cos a\cos b\cos c}$,
reproduces the common sine ratio, and state where it fails.
(e) State the limits of the verification — specifically, whether your interior
angle computation could be systematically wrong in a way your own checks would not
reveal.

---

**★★★10.** Sphere versus ellipsoid, systematically.

(a) Choose at least five coordinate pairs spanning: a short baseline ($<50$ km), a
medium one ($\sim500$ km), a long equatorial path, a long meridional path and a
long oblique path. State where the coordinates come from — if they are invented,
label them ILLUSTRATIVE.
(b) Compute the spherical central angle, the spherical distance on $R = 6371.0088$
km, and the WGS84 geodesic distance with an inverse Vincenty iteration or an
equivalent method.
(c) Validate your ellipsoidal code by setting the flattening to zero and checking
that it reproduces haversine; report the worst discrepancy.
(d) Tabulate the sign and magnitude of the difference for each pair and look for a
pattern relating it to path azimuth and latitude.
(e) Convert each difference to a $P$-wave travel-time difference at 8 km/s, and
state for which of your paths the spherical approximation would corrupt a
location to worse than a 0.5 s residual.
(f) State what your comparison does **not** establish: in particular, whether the
same conclusion holds for an S-wave or a surface-wave arrival, and why.

---

## Extension ideas

- Implement the spherical-excess area formula and compute the area of a
  quadrangle (split it into two triangles) — the natural shape of a grid cell in a
  regional potential-field survey.
- Implement a `back_azimuth` function and test that it agrees with
  `azimuth + 180` exactly only on a meridian; then measure the deviation as a
  function of the longitude span for a fixed latitude band.
