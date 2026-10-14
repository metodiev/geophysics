# Exercises — 01-04-01 Euclidean Geometry and Geometric Reasoning

Attempt these **closed-book**. Solutions are in
[`01-euclidean-geometry-solutions.md`](./01-euclidean-geometry-solutions.md).
Difficulty: ★ foundational · ★★ applied · ★★★ research-oriented.

Use $R = 6371.0088$ km where a sphere is needed. Label any invented coordinates
ILLUSTRATIVE.

---

## ★ Foundational

**★1.** Angles and polygons.

(a) Prove that the interior angles of a triangle sum to $180°$, stating which
postulate you use.
(b) State and justify the interior-angle sum of a convex $n$-gon.
(c) Give the interior angle of a regular pentagon and of a regular hexagon, and
explain why only the hexagon tiles the plane.

---

**★2.** A vertical pole $2.00$ m tall casts a shadow $3.50$ m long. At the same
time, a tower casts a shadow $40.0$ m long on level ground.

(a) Which criterion of similarity justifies the calculation?
(b) Compute the height of the tower.
(c) State two ways the conclusion would fail in the field, and how you would
detect each.

---

**★3.** A triangular claim has sides $7$, $9$ and $11$ (in appropriate units).

(a) Compute its area by Heron's formula.
(b) Compute the same area using $\tfrac12 ab\sin C$, finding the angle from the
law of cosines.
(c) State which formula you would prefer if (i) the three sides were measured,
(ii) two sides and the included angle were measured, and why.

---

**★4.** Thickness relations. A bed dips at $25°$ and a vertical borehole
intersects $400$ m of it.

(a) Compute the true (perpendicular) thickness.
(b) Compute the thickness measured along a borehole inclined $20°$ from the
vertical, in the plane perpendicular to strike.
(c) Explain, in one sentence, why (a) and (b) differ and which one a
stratigrapher wants.

---

## ★★ Applied

**★★5.** Spherical cap areas on $R = 6371.0088$ km.

(a) Compute the area of a cap of half-angle $45°$ with the closed form.
(b) Compute the area of the cap of half-angle $5°$ and express it as a fraction of
the whole sphere.
(c) Verify that the closed form reduces to $2\pi R^{2}$ at $\alpha = 90°$ and
explain what that limit is.
(d) A satellite altimeter measures a circular region of $5°$ radius at the
equator. Estimate the fraction of its area that lies above $2°$N, and state your
approximation.

---

**★★6.** Flat versus spherical area.

For an equilateral spherical triangle of side $d$:

(a) Compute the area from the spherical excess for $d = 1°, 10°, 30°, 60°$.
(b) Compute the planar triangle area through the three chords with Heron's
formula for the same four cases.
(c) Tabulate the ratio and state the scaling of the discrepancy with $d$.
(d) State the largest $d$ for which the plane approximation is good to 1 percent,
and translate it into kilometres.

---

**★★7.** A conditional Eratosthenes.

A source reports that the Sun was $7.2°$ from the vertical at a place $5000$
stadia from a place where it was overhead.

(a) If the stadion is taken as $157.5$ m, compute the implied Earth radius.
(b) Compare with the mean radius and give the percentage difference.
(c) Repeat (a) for a stadion of $185$ m and of $148$ m, and tabulate the implied
radius against the assumed unit.
(d) Write two sentences explaining why no single accuracy figure for this
measurement can be quoted honestly.

---

**★★8.** Setting out and levelling.

(a) A straight survey line closes a loop of radius $6371$ km with a chord of
$1.000$ km. Compute the sagitta — the maximum deviation of the line from the arc
— by the exact expression and by the parabolic approximation, and compare.
(b) A tunnel is driven straight between two points each $250$ m from a vertex of
a circular curve of radius $6371$ km. Compute the maximum offset of the straight
drive from the intended arc.
(c) State why this correction is applied to tunnels and long pipelines but not to
a 100 m building foundation.

---

## ★★★ Research-oriented

**★★★9.** Verify the area formulas.

(a) Generate at least $10^{4}$ random triangles by choosing three random points in
the unit square, and compute each area three ways: the shoelace/cross-product
formula, Heron's formula from the three side lengths, and the half-product form
using one angle from the law of cosines.
(b) Report the worst absolute discrepancy between the three, and which pair agrees
most closely.
(c) Find the configuration in which Heron's formula is worst, and characterise it
geometrically.
(d) State what your test would not detect — in particular, whether a shared error
in the side-length computation could pass all three checks.

---

**★★★10.** The dependence of flat-versus-spherical error on size.

(a) For equilateral spherical triangles with sides $d$ from $0.1°$ to $80°$,
compute the ratio of the planar chord-triangle area to the spherical area.
(b) On log–log axes, plot $(1 - \text{ratio})$ against $d$ and fit a power law.
Report the exponent.
(c) Compare the exponent with the theoretical expectation from the leading
curvature correction, and say whether the data support it.
(d) State the limits of the conclusion: does the exponent depend on the *shape* of
the triangle, or only on its size? Give evidence.

---

## Extension ideas

- Derive the sagitta relation and use it to estimate how far a straight line
  deviates from a great circle over 100 km, comparing with the drop below the
  tangent plane computed in
  [01-04-05](../05-surfaces-and-curvature.md).
- Compute the interior angle sums of the spherical triangles in
  [01-03-04 exercise ★★★9](../../03-trigonometry/exercises/04-spherical-trigonometry-exercises.md)
  and confirm that the excess matches the area you obtain from a solid-angle
  integral.
