---
id: 01-04-01
title: "Euclidean Geometry and Geometric Reasoning"
level: beginner
prereqs: ["01-03-01"]
estimated_minutes: 75
tags: [geometry, triangles, similarity, area, eratosthenes]
---

# Euclidean Geometry and Geometric Reasoning

## Learning objectives

By the end of this lesson you will be able to:

1. **Reason** from the elementary properties of angles, parallels, triangles and
   circles, and know *why* the standard facts are true rather than only that they
   are.
2. **Use** similar triangles to obtain unknown lengths from known ones, which is
   the geometric core of every scaling argument in geophysics.
3. **Derive** the three area formulas for a triangle — base-times-height,
   half-the-product-with-the-included-angle, and Heron's — and know when each is
   the convenient one.
4. **Apply** the inscribed-angle theorem to justify the extended law of sines.
5. **Estimate** lengths and thicknesses from a cross-section or a field sketch,
   with an explicit statement of which length is vertical, which is
   perpendicular, and which is along the bed.
6. **Recognise** when plane geometry is the wrong tool, and hand over to the
   spherical geometry of [01-03-04](../03-trigonometry/04-spherical-trigonometry.md).

## Prerequisites

[01-03-01 Angles, Triangles and the Unit Circle](../03-trigonometry/01-angles-and-triangles.md)
for the trigonometric functions and the two triangle laws. This lesson is the
synthetic counterpart of that analytic development.

## 1. Why synthetic geometry still earns its place

You have already met the analytic machinery: sines, cosines and the law of
cosines will solve any triangle you can describe with numbers. So why begin the
geometry module with points, parallels and similar triangles?

**Because most field reasoning is ratio reasoning, and ratios are easier to see
than to compute.** A geologist looking at a cross-section says "that bed is about
twice as thick on the east limb" and is right, without measuring anything. An
interpreter comparing an anomaly's width with its source depth uses a ratio
argument. A surveying assistant holding a stadia rod and reading a level uses
similar triangles by construction.

Synthetic geometry is the algebra of ratios, done with a diagram. Its results are
the ones you can carry in your head at a field site, and its hypotheses — flat,
straight, non-Euclidean-not — are exactly the hypotheses you will later have to
check, when the survey is 100 km long and the Earth's curvature is no longer
negligible.

## 2. The elementary facts, and where they come from

**Angle.** Two rays from a common point divide the plane into two regions; the
angle is the rotation between them. Rotations add, so angles are additive in the
way lengths are.

**Parallel lines.** Two distinct lines in a plane are parallel if they never meet.
The decisive consequence, and the one that generates all of plane geometry, is
that a transversal cutting two parallel lines makes the alternate interior angles
equal.

**The angle sum of a triangle, proved.** Let $ABC$ be a triangle. Draw the line
through $A$ parallel to $BC$. The two angles that this line makes with $AB$ and
$AC$, on the side of $A$ away from $BC$, are equal to $B$ and $C$ respectively,
because they are alternate interior angles. The three angles at $A$ — the two
transferred ones and $A$ itself — lie on a straight line, so they sum to $180°$:

$$A + B + C = 180° .$$

**Everything follows from that.** The exterior angle of a triangle equals the sum
of the two opposite interior angles. The interior angles of a convex $n$-gon sum
to $(n-2)\times 180°$, because the polygon can be cut into $n-2$ triangles from a
single vertex. An equilateral triangle has three $60°$ angles; a regular hexagon
tiles the plane because its interior angles are $120°$, and three of them make
$360°$.

**Why this matters more than it looks.** The proof uses the parallel postulate,
and on a sphere there are no parallels in this sense. The failure of the angle sum
is therefore not a small correction; it is the signature of a different geometry,
and it is measurably large: the spherical triangle in
[01-03-04](../03-trigonometry/04-spherical-trigonometry.md) has an angle sum of
$206.5976°$, exceeding $180°$ by the area of the triangle in appropriate units.
**On a sphere, a triangle's angle sum tells you its area.** That is the beginning
of differential geometry, and it is available to you from a field measurement with
a plane table.

## 3. Similarity: the workhorse

Two triangles are **similar** if their angles are equal. Similarity is weaker than
congruence: shape is preserved, size is not. The fundamental consequence is that
corresponding sides are in a fixed ratio:

$$\frac{a}{a'} = \frac{b}{b'} = \frac{c}{c'} = k .$$

The standard sufficient conditions are AA (two angles equal), SAS (two sides in
proportion with the included angle equal) and SSS (all three sides in proportion).

**Why similarity is so useful.** It converts a *measurement problem* into a *ratio
problem*. If you can see two triangles in your diagram that share an angle and lie
across a pair of parallels, you can write down a proportion without knowing any
trigonometry, and the unknown length follows by multiplication. This is how
heights of inaccessible objects are measured, how scale models transfer to full
size, and how a cross-section is converted from millimetres on paper to metres in
the ground.

### 3.1 Worked example: thickness versus vertical separation

A bed dips at $30°$ and a borehole passes through $250$ m of it, measured along the
borehole which is vertical.

The vertical thickness is $V = 250$ m. The **true thickness** — measured
perpendicular to the bedding planes — is the projection of $V$ onto the bed normal:

$$t_{\text{true}} = V\cos\delta = 250\cos 30° = 250 \times 0.8660254
= \boxed{216.506\ \text{m}} .$$

This is a similar-triangle statement in disguise: the vertical, the perpendicular
and the along-bed directions form a right triangle whose angle at the bed is
$\delta$, so the perpendicular leg is the vertical hypotenuse times $\cos\delta$.

**The trap.** Many field notes record a *vertical* thickness, because that is what
a vertical borehole measures, and then compare it with a *true* thickness from a
map or a model. The two differ by $\cos\delta$, which is 13 percent at $30°$ and
29 percent at $45°$. Write down which you have. The general relation between
vertical thickness $V$, true thickness $t$ and dip $\delta$ is

$$V = \frac{t}{\cos\delta}, \qquad t = V\cos\delta .$$

Note the complementary formula that students reach for wrongly:
$t = V\sin\delta$ is **not** a thickness relation; it is the horizontal offset
relation that appears when the bed is cut by a fault, discussed next.

### 3.2 Worked example: a fault offset and a river width

Both are the same triangle. A fault dips $60°$ and the beds across it are offset
by $100$ m vertically. The **horizontal separation** of the two truncated bed
edges is a *heave* of

$$h = \frac{100}{\tan 60°} = \frac{100}{1.7320508} = \boxed{57.735\ \text{m}} .$$

Equivalently: standing $100$ m from a river, you sight a marker on the far bank at
$30°$ from the line straight across the river and pace off a $100$ m baseline,
finding the marker subtends $30°$. The width is then
$100\tan 30° = \boxed{57.735\ \text{m}}$, the same number, because the two
triangles are the same triangle with the labels permuted. **Recognising that two
field problems are one geometry problem is most of the value of this lesson.**

## 4. Circles

Four facts about circles do the work in geophysics.

**Inscribed angle.** An angle subtended at the circumference by a chord is half the
angle the same chord subtends at the centre. Two immediate corollaries:

- angles in the same segment are equal;
- an angle subtended by a diameter is a right angle, because the central angle is
  $180°$.

**Extended law of sines.** The inscribed-angle theorem applied to the circumcircle
gives $a = 2R\sin A$ for a triangle with side $a$ opposite angle $A$ and
circumradius $R$ — the derivation is in
[01-03-01 Section 4.2](../03-trigonometry/01-angles-and-triangles.md). The common
ratio $a/\sin A$ is therefore not an arbitrary constant but the circumdiameter.

**Chord and sagitta.** A chord of length $L$ in a circle of radius $R$ leaves a
sagitta (the depth of the circular segment) of
$s = R - \sqrt{R^{2} - (L/2)^{2}}$. This is the geometry of a mine tunnel driven
straight through a curved tunnel, and of the deviation of a straight survey line
from a curved one.

**Tangent.** A tangent touches at exactly one point and is perpendicular to the
radius there. That perpendicularity is the basis of the deflection-angle method of
setting out a circular curve in road and tunnel engineering.

### 4.1 Beyond the plane: the area of a spherical cap

The first genuinely geophysical use of elementary geometry is the area of a
region on a sphere. For a cap of half-angle $\alpha$ on a sphere of radius $R$,

$$A = 2\pi R^{2}(1 - \cos\alpha) .$$

The derivation is a solid-angle integral, which belongs to
[01-04-03](./03-cartesian-spherical.md), but the *form* is worth having now
because it is the plane-geometry formula's curved counterpart. On
$R = 6371.0088$ km the demonstration in this module integrates the solid-angle
element numerically and finds:

| Half-angle $\alpha$ | Area from the closed form (km²) | Numeric integration (km²) | Difference (km²) |
|---|---|---|---|
| $1°$ | 38842.752116 | 38842.752116 | $9.2\times10^{-9}$ |
| $5°$ | 970477.335101 | 970477.335102 | $7.7\times10^{-7}$ |
| $30°$ | 34167935.223338 | 34167935.224313 | $9.8\times10^{-4}$ |
| $90°$ | 255032940.486436 | 255032940.551984 | $6.6\times10^{-2}$ |

At $\alpha = 90°$ the cap is a hemisphere, and the area is
$2\pi R^{2} = 255032940.486$ km² — half of $4\pi R^{2}$, as it must be, which is
the check that validates the whole formula. Notice how the numerical-integration
error grows with the cap size: the midpoint rule is exact to the order of its
step, and the integration covers more curvature as $\alpha$ grows. **The
closed form is the result; the integral is the verification.**

## 5. Areas: three formulas for one triangle

For a triangle with sides $a$, $b$, $c$, angles $A$, $B$, $C$ and semi-perimeter
$s = (a+b+c)/2$:

$$A_{\triangle} = \tfrac12 \times \text{base} \times \text{height}
= \tfrac12 ab\sin C
= \sqrt{s(s-a)(s-b)(s-c)} .$$

The first is the definition; the second follows immediately by choosing $a$ as the
base and using $h = b\sin C$; the third is Heron's formula.

### 5.1 Derivation of Heron's formula from the law of cosines

Start from the half-product form with $C$ as the included angle:

$$A_{\triangle} = \tfrac12 ab\sin C
= \tfrac12 ab\sqrt{1 - \cos^{2}C} .$$

Substitute $\cos C = (a^{2}+b^{2}-c^{2})/(2ab)$:

$$1 - \cos^{2}C
= 1 - \frac{(a^{2}+b^{2}-c^{2})^{2}}{4a^{2}b^{2}}
= \frac{4a^{2}b^{2} - (a^{2}+b^{2}-c^{2})^{2}}{4a^{2}b^{2}}
= \frac{4a^{2}b^{2} - \left[(a^{2}+b^{2}) - c^{2}\right]^{2}}{4a^{2}b^{2}} .$$

The numerator is a difference of squares. Factor it:

$$4a^{2}b^{2} - \left[(a^{2}+b^{2}) - c^{2}\right]^{2}
= \left(2ab - a^{2} - b^{2} + c^{2}\right)\left(2ab + a^{2} + b^{2} - c^{2}\right),$$

and recognise both factors as differences of squares again:

$$c^{2} - (a-b)^{2} = (c - a + b)(c + a - b), \qquad
(a+b)^{2} - c^{2} = (a + b - c)(a + b + c).$$

Assembling, and writing each bracket in terms of $s$ — for instance
$a + b - c = 2(s - c)$ — gives

$$A_{\triangle}^{2} = s(s-a)(s-b)(s-c),$$

which is Heron's formula. **The square root in Heron's formula is not a
coincidence: it is the square root of $1 - \cos^{2}C$, that is, of a sine.**

### 5.2 Numerical verification

Take the triangle used in [01-03-01](../03-trigonometry/01-angles-and-triangles.md):
$b = 4$, $c = 5$, included angle $A = 60°$, so $a = \sqrt{21} = 4.582575694956$
and $s = 6.7912878475$. Then

$$\tfrac12 bc\sin A = \tfrac12(4)(5)(0.8660254038) = 8.660254037844,$$

$$\sqrt{s(s-a)(s-b)(s-c)} = 8.660254037844 .$$

The first differs from the second in the last printed digit by one unit in the
sixteenth decimal. Two formulas derived from different starting points agree,
which is the strongest verification available to you without an independent
measurement — and it is why **the half-product form should be your default**. It is
shorter, it needs no semi-perimeter, and it fails gracefully (a triangle with a
$90°$ angle is a special case, not a degenerate one).

**Where Heron's formula does better.** When you are given the three sides and no
angle — as when an area is computed from a closed traverse — Heron is the only one
of the three that can be used directly. When one side is very much larger than the
others, Heron's formula loses precision through the subtraction
$s - c \approx 0$ if $a + b \approx c$, because a nearly flat triangle has
essentially zero area computed as a product of nearly zero factors. In that regime,
compute the height instead.

## 6. Eratosthenes, and the honest statement of an ancient result

The classic demonstration that the Earth is round and its size measurable uses
nothing but the geometry of this lesson.

**The observation.** Eratosthenes compared the noon elevation of the Sun at two
places roughly on the same meridian. At one, the Sun stood directly overhead at
the summer solstice, casting a shadow of zero length in a deep well. At the other,
several thousand stadia to the south, the Sun's rays made an angle of about $7.2°$
with the vertical.

**The geometry.** Sunlight arrives effectively parallel, so the two vertical
directions at the two places are separated by the same angle as the rays — an
alternate-interior-angle argument, exactly the one used to prove the triangle angle
sum. That angle is the central angle between the two places. Hence

$$\frac{\Delta\theta}{360°} = \frac{d}{2\pi R}
\ \Longrightarrow\
R = \frac{360° d}{2\pi \Delta\theta} = \frac{d}{\Delta\theta\ \text{in rad}} .$$

Note the form: the radius is the arc distance divided by the central angle in
radians, which is the definition of a radian rearranged. No trigonometry, no
approximation, one proportion.

**What you can and cannot say.** Every modern account of this result quotes a
percentage error for Eratosthenes, and every such figure depends on a conversion
from the ***stadion*** — the unit he used — to metres. The length of the stadion
varied between Greek cities and is not known to modern precision; the commonly
quoted figures assume a particular one. **Therefore any accuracy claim about his
result is a claim about the assumed conversion factor, not about his measurement.**
What is beyond doubt is the *method*: an angle measured with a shadow, a distance
estimated by pacing or by professional bematists, and one proportion. The
mathematics is a single similar-triangle argument, and it is correct.

If you want a defensible number, state it conditionally: "if the stadion is taken
as $x$ metres, then the implied radius is $y$ kilometres, which differs from the
modern mean radius by $z$ percent." That is honest, complete, and checkable.

## 7. Python demonstration and the plane-to-sphere handover

The demonstrations for this module are
[`code/coordinate_systems_demo.py`](./code/coordinate_systems_demo.py),
[`code/geodesy_projection_demo.py`](./code/geodesy_projection_demo.py) and
[`code/dip_strike_demo.py`](./code/dip_strike_demo.py). The third one opens with
the three-point plane problem, which is a direct application of the area and
similar-triangle reasoning of this lesson to a three-dimensional question, and it
validates itself by constructing a plane with a known dip and recovering it:

```text
synthetic plane with known dip 30.000 deg towards azimuth 90.000 deg:
  P1 =     0.000,     0.000,   100.0000
  P2 =  1000.000,     0.000,  -477.3503
  P3 =     0.000,   700.000,   100.0000
recovered: dip = 30.000000 deg, dip azimuth = 90.000000 deg, strike = 0.000000 deg
```

That is the pattern to adopt in your own work: build a case whose answer you know
from the construction, then check that the method returns it. No amount of testing
on unknown data gives you that assurance.

**The handover.** Plane geometry is the right tool while the region is small
compared with the radius of curvature. Part (c) of exercise ★★6 in the lesson-04
exercise set measures the criterion: an equilateral spherical triangle of side
$1°$ has a flat-triangle area 0.01 percent too small, at $10°$ the error is 0.6
percent, at $30°$ it is 5.6 percent, and at $60°$ it is 21 percent. **So "small"
means a few degrees, and the errors grow as the square of the size.** For anything
larger, use [01-04-04](./04-geographic-coordinates.md), where the sphere and the
ellipsoid take over.

## 8. Common mistakes

1. **Confusing vertical, true and along-hole thickness.** They differ by factors
   of $\cos\delta$ and $\sec\delta$, which are 13 percent and 15 percent at $30°$.
   Label every length in a field sketch with which one it is.
2. **Applying the triangle angle sum on a sphere.** It exceeds $180°$; the excess
   *is* the area, and at continental scale it is degrees, not arcseconds.
3. **Assuming two triangles are similar from a sketch.** Similarity requires equal
   angles, and in a perspective field sketch it is very easy to draw them equal
   without them being equal. State the criterion you are using.
4. **Using Heron's formula for a nearly flat triangle.** The product
   $s(s-a)(s-b)(s-c)$ becomes a difference of nearly equal numbers and the square
   root amplifies the loss — the same mechanism as the arccosine distance formula
   of [01-03-04](../03-trigonometry/04-spherical-trigonometry.md).
5. **Treating a surveyed area as planar without checking.** At the 1 percent level
   a plane approximation is good to about $10°$ of arc, i.e. 1100 km; beyond that
   the area is systematically under-estimated, as the chord construction in the
   lesson-04 exercises shows.
6. **Forgetting which angle an inscribed-angle relation refers to.** The inscribed
   angle is half the central angle subtending the *same* chord, and the wrong arc
   gives $180°$ minus the answer.

## 9. Real-world applications

- **Geological cross-sections and thickness maps.** Section 3.1 is the calculation
  that converts a borehole intersection into a stratigraphic thickness, and it is
  done thousands of times a day in basin analysis.
- **Fault heave and throw.** Throw is vertical, heave is horizontal, and the two
  are related through the dip by the tangent — the same triangle as a river width.
- **Surveying and setting out.** Traverses, offsets, circular curves and the
  closing error of a closed traverse are all elementary geometry; the deflection
  angle and the tangent-to-radius perpendicularity are used directly.
- **Focal-mechanism plots and stereonets.** The equal-angle and equal-area
  projections used to display orientation data are circle geometry — the
  stereographic projection maps circles to circles — which is why an angle
  measured off a stereonet is a real angle.
- **Anomaly-width-to-depth estimates.** The simplest interpretation rule of thumb
  for a gravity or magnetic profile — a half-width roughly equal to the depth for
  a tabular body — is a similarity argument: the anomaly's shape scales with depth
  because the physics is scale-free away from the boundaries.
- **Radial and dip-section construction for potential fields.** Drawing a
  perpendicular from a station to a trend line, and measuring the perpendicular
  distance, is plane geometry and it is the first step of many profile
  interpretations.

## 10. Further reading

- **Hilbert, D. and Cohn-Vossen, S. (1952). *Geometry and the Imagination*.
  Chelsea.** Level: intermediate. Geometry as a visual and physical subject;
  unusually good at making theorems obvious rather than merely true.
- **Coxeter, H. S. M. (1969). *Introduction to Geometry* (2nd ed.). Wiley.**
  Level: intermediate. A rigorous and elegant treatment of exactly the material in
  this lesson, including a careful treatment of similarity and the circle theorems.
- **Euclid. *Elements*, Book I (and Book III for circles).** Level: beginner, with
  patience. Any modern translation; public-domain editions exist. Reading the
  original propositions is the fastest way to see how a deductive structure is
  built from postulates.
- **Rich, B. (1963). *Principles and Applications of Mathematics for Surveying*.
  American Congress on Surveying and Mapping.** Level: applied. Field geometry
  from the practitioner's side, including curve setting-out. Check the current
  availability and edition through a library.

> Note on citations: bibliographic details above are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> relying on them. The Eratosthenes discussion deliberately avoids a numerical
> accuracy claim, because the conversion from the stadion is not agreed.

## 11. Related lessons

- [01-03-01 Angles, Triangles and the Unit Circle](../03-trigonometry/01-angles-and-triangles.md) —
  the analytic version of the triangle results used here.
- [01-03-04 Spherical Trigonometry and Great-Circle Geometry](../03-trigonometry/04-spherical-trigonometry.md) —
  what happens to the angle sum when the triangle is drawn on a sphere.
- [01-04-02 Analytic Geometry: Lines, Planes and Distances](./02-analytic-geometry.md) —
  the same problems solved with coordinates, which is what you will actually do.
- [01-04-03 Cartesian, Cylindrical and Spherical Coordinates](./03-cartesian-spherical.md) —
  where the spherical cap formula of Section 4.1 is derived.
- [01-04-05 Surfaces, Parametrisation and Curvature](./05-surfaces-and-curvature.md) —
  curvature as the generalisation of everything in this lesson.

## Exercises and self-assessment

Exercises are in
[`exercises/01-euclidean-geometry-exercises.md`](./exercises/01-euclidean-geometry-exercises.md),
with solutions in
[`exercises/01-euclidean-geometry-solutions.md`](./exercises/01-euclidean-geometry-solutions.md).

Before moving on, you should be able to:

- [ ] Prove the triangle angle sum from the parallel postulate, in five lines.
- [ ] State the interior-angle sum of a convex $n$-gon and justify it by
      triangulation.
- [ ] Convert between vertical, true and along-hole thickness given a dip.
- [ ] Derive Heron's formula from the law of cosines.
- [ ] Explain what the spherical excess of a triangle measures, without calculus.
- [ ] State why an accuracy claim for Eratosthenes depends on a unit conversion
      that is itself uncertain.
