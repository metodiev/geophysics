---
id: 01-03-01
title: "Angles, Triangles and the Unit Circle"
level: beginner
prereqs: ["01-01-03", "01-02-02"]
estimated_minutes: 75
tags: [trigonometry, geometry, triangles, angles, rays]
---

# Angles, Triangles and the Unit Circle

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** between degrees and radians fluently, and explain why every
   formula in physics and geophysics uses radians.
2. **Read** the unit circle as a definition rather than a table: state the sine,
   cosine and tangent of any angle, with the correct sign, from its location.
3. **Derive** the law of cosines from coordinates, and the law of sines from the
   circumcircle, without looking them up.
4. **Solve** a triangle given the three standard input combinations, and state
   which combination is ambiguous.
5. **Apply** the laws to a real geophysical measurement: an apparent dip, a ray
   parameter, or an epicentral distance expressed as an angle.
6. **Estimate** the error made by replacing $\sin x$ with $x$, and say when that
   approximation is legitimate.

## Prerequisites

- [01-01-03 Units, SI Conventions and Dimensional Analysis](../01-arithmetic/03-units-and-dimensional-analysis.md),
  because an angle in radians is dimensionless and that fact matters when you
  check an equation.
- [01-02-02 Functions, Graphs and Transformations](../02-algebra/02-functions-and-graphs.md),
  for the idea of a function and its graph.

## 1. Angles: the natural variable, and the two units we use

An **angle** measures rotation between two rays from a common point. It is a
ratio of two lengths — the arc length on a circle divided by its radius — so it
has no units in the SI sense. We nevertheless attach two units to it, and the
difference matters.

**Degrees.** One full turn is $360°$, a convention inherited from Babylonian
sexagesimal arithmetic. A degree is subdivided into 60 arcminutes, and an
arcminute into 60 arcseconds, so

$$1° = 60' = 3600''.$$

**Radians.** One radian is the angle that subtends an arc equal in length to the
radius. A full turn is therefore $2\pi$ radians, and

$$1\ \text{rad} = \frac{180°}{\pi} \approx 57.2958°, \qquad
1° = \frac{\pi}{180}\ \text{rad} \approx 1.7453\times10^{-2}\ \text{rad}.$$

**Why radians win in every formula.** On a circle of radius $r$, an arc
subtending angle $\theta$ has length $r\theta$ — *provided* $\theta$ is in
radians. In degrees the same statement needs a factor of $\pi/180$, and that
factor appears again in every derivative:

$$\frac{d}{d\theta}\sin\theta = \cos\theta \quad (\theta\ \text{in radians}),
\qquad
\frac{d}{dx}\sin(x°) = \frac{\pi}{180}\cos(x°) .$$

The example that will matter to you most: the small-angle approximation
$\sin\theta \approx \theta$ is only true in radians. A deflection of 1 m over a
beam length of 1 km is an angle of $10^{-3}$ rad, not $10^{-3}$ degrees — a
factor of 57.

> **Working rule for this curriculum.** Store angles in radians. Convert to
> degrees only at the point where a human reads them, and convert back
> immediately. Half of all trigonometric bugs are degree/radian mix-ups.

## 2. The unit circle

Draw a circle of radius 1 centred at the origin. Start at $(1,0)$ and rotate
anti-clockwise by angle $\theta$, measured from the positive $x$-axis. The
coordinates of the point you reach *define* the cosine and the sine:

$$\cos\theta = x(\theta), \qquad \sin\theta = y(\theta).$$

This is not a mnemonic; it is the definition, and everything else follows from
it. In particular:

- $\cos^2\theta + \sin^2\theta = 1$, because the point lies on the unit circle.
- The functions are defined for *all* real $\theta$, including negative and
  greater-than-$2\pi$ values, by continuing to go round.
- They are periodic: $\sin(\theta + 2\pi) = \sin\theta$, and likewise for cosine.
- The tangent is the slope of the radius line, $\tan\theta = \sin\theta/\cos\theta$,
  so it is *undefined* where $\cos\theta = 0$, at odd multiples of $\pi/2$.

Values your should be able to reproduce from geometry rather than memory:

| $\theta$ | rad | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|---|---|---|---|---|
| $0°$ | 0 | 0 | 1 | 0 |
| $30°$ | $\pi/6$ | $1/2$ | $\sqrt3/2$ | $1/\sqrt3$ |
| $45°$ | $\pi/4$ | $\sqrt2/2$ | $\sqrt2/2$ | 1 |
| $60°$ | $\pi/3$ | $\sqrt3/2$ | $1/2$ | $\sqrt3$ |
| $90°$ | $\pi/2$ | 1 | 0 | undefined |
| $180°$ | $\pi$ | 0 | $-1$ | 0 |
| $270°$ | $3\pi/2$ | $-1$ | 0 | undefined |

The companion demonstration
[`code/trig_foundations_demo.py`](./code/trig_foundations_demo.py) prints these,
and the last column is the honest one:

```text
  deg          rad          sin          cos              tan
    0   0.00000000   0.00000000   1.00000000     0.0000000000
   30   0.52359878   0.50000000   0.86602540     0.5773502692
   45   0.78539816   0.70710678   0.70710678     1.0000000000
   60   1.04719755   0.86602540   0.50000000     1.7320508076
   90   1.57079633   1.00000000   0.00000000   undefined
  120   2.09439510   0.86602540  -0.50000000    -1.7320508076
  180   3.14159265   0.00000000  -1.00000000    -0.0000000000
  270   4.71238898  -1.00000000  -0.00000000   undefined
  360   6.28318531  -0.00000000   1.00000000    -0.0000000000
```

Two features of that printout are worth more than the table itself.

**The sign pattern.** Quadrant I ($0$–$90°$) is all positive. Quadrant II
($90$–$180°$) has positive sine. Quadrant III ($180$–$270°$) has both negative.
Quadrant IV ($270$–$360°$) has positive cosine. "All Students Take Calculus" is
the usual mnemonic; the reflection identities are the honest statement:

$$\sin(\pi-\theta) = \sin\theta, \quad
\sin(-\theta) = -\sin\theta, \quad
\cos(\pi-\theta) = -\cos\theta, \quad
\cos(-\theta) = \cos\theta.$$

**The zeros are not zero.** At $90°$ the printed cosine is 0.00000000, but the
stored value is $6.123233995736766\times10^{-17}$ — the round-off in the stored
value of $\pi$. If you divide by $\cos\theta$, or take $\arccos$ of something
near 1, that residue is amplified. The demonstration makes this explicit rather
than hiding it behind a format string.

## 3. Triangles: three laws and what each is for

Take a triangle with vertices $A$, $B$, $C$, sides $a$, $b$, $c$ opposite the
corresponding vertices, and interior angles $A$, $B$, $C$.

### 3.1 The angle sum

$$A + B + C = \pi \quad (\text{radians}), \qquad A + B + C = 180° .$$

This is not a definition; it follows from the parallel postulate, proved by
drawing a line through one vertex parallel to the opposite side and using the
equality of alternate angles. On a *sphere* it fails, and quantifying the
failure is the subject of
[01-03-04 Spherical Trigonometry and Great-Circle Geometry](./04-spherical-trigonometry.md).

### 3.2 The law of cosines

$$a^{2} = b^{2} + c^{2} - 2bc\cos A .$$

Read it as the Pythagorean theorem plus a correction. When $A = 90°$ the
cosine term vanishes and you recover $a^2 = b^2 + c^2$.

### 3.3 The law of sines

$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R,$$

where $R$ is the radius of the circumscribed circle — the unique circle through
all three vertices. The common value is the circumdiameter.

### 3.4 Which one to use

| You know | Use | Note |
|---|---|---|
| Two sides and the included angle (SAS) | law of cosines for the third side, then the law of sines | unambiguous |
| Three sides (SSS) | law of cosines for each angle | unambiguous |
| Two angles and a side (AAS/ASA) | law of sines | unambiguous |
| Two sides and a *non-included* angle (SSA) | law of sines | **ambiguous**: two triangles usually fit |

The SSA ambiguity is the geometric root of the branch ambiguity that
[01-03-03 Inverse Trigonometric Functions and Branch Ambiguity](./03-inverse-trig.md)
treats systematically. When you are given $a$, $b$ and $A$ rather than the
included angle, the triangle you draw may be the obtuse or the acute one; the
data do not tell you which.

## 4. Derivations and worked reasoning

### 4.1 The law of cosines, derived in four lines

Place vertex $A$ at the origin, vertex $B$ at $(c, 0)$ on the $x$-axis, and
vertex $C$ at distance $b$ from $A$ making angle $A$ with the $x$-axis, so

$$C = (b\cos A,\ b\sin A).$$

The side $a$ is the distance from $B$ to $C$:

$$a^{2} = (b\cos A - c)^{2} + (b\sin A - 0)^{2}.$$

Expand:

$$a^{2} = b^{2}\cos^{2}A - 2bc\cos A + c^{2} + b^{2}\sin^{2}A
       = b^{2}(\cos^{2}A + \sin^{2}A) + c^{2} - 2bc\cos A.$$

The bracket is 1, giving

$$\boxed{a^{2} = b^{2} + c^{2} - 2bc\cos A}.$$

The only two ingredients are Pythagoras and the Pythagorean identity. This is
why the law of cosines is sometimes called *the* generalisation of Pythagoras.

### 4.2 The law of sines, derived from the circumcircle

Let the circumcentre be $O$ and the circumradius $R$. The inscribed-angle
theorem says that an angle at the circumference subtends the same arc as the
central angle, and that the central angle is twice the inscribed one. Chord $BC$
has length $a$ and subtends angle $A$ at $A$, therefore it subtends $2A$ at $O$
(taking the appropriate arc when $A$ is obtuse). A chord subtending central
angle $2A$ on a circle of radius $R$ has length

$$a = 2R\sin A .$$

Applying the same argument to the other two sides gives
$a/\sin A = b/\sin B = c/\sin C = 2R$.

> **Why this matters beyond the identity.** The converse is also useful: the
> circumdiameter $2R$ characterises the triangle's "size" independently of which
> side you happen to know. The demonstration computes the ratio three ways and
> gets the same number three times:

```text
law of sines: a/sin A = 5.291502622129, b/sin B = 5.291502622129, c/sin C = 5.291502622129
```

The agreement of three independently computed quantities is the cheapest
verification available to you whenever you implement a geometric formula.

### 4.3 A completely worked triangle

**Problem.** A triangle has $b = 4$, $c = 5$, and included angle $A = 60°$.
Find $a$, $B$, $C$, the circumdiameter, and the area.

**Step 1 — third side, law of cosines.** Since $\cos 60° = 1/2$,

$$a^{2} = 16 + 25 - 2(4)(5)(0.5) = 41 - 20 = 21,
\qquad a = \sqrt{21} = 4.582575694956.$$

**Step 2 — the remaining angles, law of cosines.** Solving the law of cosines
for the angle rather than the side:

$$B = \arccos\!\left(\frac{a^{2} + c^{2} - b^{2}}{2ac}\right) = 49.1066053509°.$$

Note the discipline: $B$ is the angle *opposite* $b$, so it is $b$ that appears
as the subtracted term. Getting that correspondence wrong is the second most
common trigonometry error after a degree/radian mix-up. Then

$$C = \arccos\!\left(\frac{a^{2} + b^{2} - c^{2}}{2ab}\right) = 70.8933946491°.$$

**Step 3 — the internal check.** $60° + 49.1066° + 70.8934° = 180.0000000000°$.
The demonstration prints exactly this, and if the sum had come to anything but
180 the arithmetic would be wrong.

**Step 4 — circumdiameter.**

$$2R = \frac{a}{\sin A} = \frac{4.582575694956}{0.8660254038} = 5.291502622129.$$

**Step 5 — area, two ways.**

$$\text{Area} = \tfrac12 bc\sin A = \tfrac12(4)(5)(0.8660254038) = 8.660254037844,$$

and independently, by Heron's formula with semi-perimeter
$s = (a+b+c)/2 = 6.7912878475$,

$$\text{Area} = \sqrt{s(s-a)(s-b)(s-c)} = 8.660254037844.$$

The two agree to every printed digit. Heron's formula is not independent
information; it is the law of cosines in disguise, which is why it can be
derived from it and why agreement is evidence of correct arithmetic rather than
of a new physical fact.

### 4.4 Applying the laws: true dip from two apparent dips

This is the first genuinely geophysical use, and it is exactly where students
new to the field get it wrong, so we do it slowly.

**The setting.** A planar geological boundary (a bedding plane, a coal seam, a
reflecting interface) is not necessarily vertical or horizontal. Suppose it dips
at angle $\delta$ towards azimuth $\theta$, where azimuth is measured clockwise
from north. You cannot see the plane; you can only measure its *apparent* dip in
the vertical sections you happen to have — a north–south section and an
east–west section, say. The apparent dip is always smaller than or equal to the
true dip, because a section across the steepest direction understates the slope.

**The relation.** For a vertical section whose horizontal trace points along
azimuth $\varphi$, the measured apparent dip $\alpha$ obeys

$$\tan\alpha = \tan\delta \cdot |\sin(\varphi - \theta)| .$$

*Check the limiting cases.* If the section faces down the dip direction,
$\varphi = \theta$, so $\tan\alpha = \tan\delta$ and $\alpha = \delta$: the
maximum. If the section runs along the strike, $\varphi = \theta \pm 90°$, the
sine vanishes, so $\alpha = 0$: a section along strike shows a horizontal line.
Both limits are what a field geologist expects.

**The two sections.** For the north–south section $\varphi = 0$ and for the
east–west section $\varphi = 90°$, so

$$\tan\alpha_{N} = \tan\delta\,|\sin\theta|, \qquad
\tan\alpha_{E} = \tan\delta\,|\cos\theta| .$$

Squaring and adding eliminates $\theta$:

$$\tan\delta = \sqrt{\tan^{2}\alpha_{N} + \tan^{2}\alpha_{E}} .$$

Dividing gives the dip direction:

$$\tan\theta = \frac{\tan\alpha_{N}}{\tan\alpha_{E}}
\quad\Longrightarrow\quad
\theta = \operatorname{atan2}(\tan\alpha_{N},\ \tan\alpha_{E}) .$$

**The worked case.** Apparent dips of $20°$ in the north–south section and $30°$
in the east–west section:

$$\tan 20° = 0.3639702, \qquad \tan 30° = 0.5773503,$$

$$\tan\delta = \sqrt{0.3639702^{2} + 0.5773503^{2}} = \sqrt{0.4658125}
= 0.6825042,$$

$$\delta = 34.3136°, \qquad
\theta = \operatorname{atan2}(0.3639702, 0.5773503) = 32.2279° .$$

The demonstration reports "true dip = 34.3136 deg, dip azimuth = 32.2279 deg,
strike = 122.2279 deg or 302.2279 deg". Note that the strike is quoted as a line,
not a direction, so both ends are correct.

**The two traps, both demonstrated numerically.** First, the formula returns a
dip azimuth in the *first quadrant only*. Feeding in $\theta = 131°$ or
$\theta = 275°$ returns $49°$ or $85°$ instead, because the two apparent dips
depend on $|\sin\theta|$ and $|\cos\theta|$ and so cannot distinguish a
north-east dip from its mirror image. You must know from other evidence — where
the beds get deeper, which way a nearby outcrop faces — which quadrant is real.
Second, when the dip is due east the north–south apparent dip is exactly zero,
and any inversion written as $\theta = \arctan(\tan\alpha_N/\tan\alpha_E)$
divides by zero. Using `atan2` removes the division but not the ambiguity.

### 4.5 Applying the laws: the ray parameter

Snell's law at an interface between two media of wave speeds $v_1$ and $v_2$
states that the angle from the normal changes so that

$$\frac{\sin i_1}{v_1} = \frac{\sin i_2}{v_2} = p,$$

and $p$ is called the **ray parameter**. It is conserved along a ray, not just
across one boundary, which is what makes it the natural variable for travel-time
curves.

The demonstration uses $v_1 = 1.5$ km/s (sediment) over $v_2 = 5.5$ km/s
(crystalline rock) and finds

$$\sin i_c = \frac{v_1}{v_2} = 0.2727273, \qquad i_c = 15.826620°,$$

where $i_c$ is the critical angle above which the ray cannot be transmitted at
all. For $i_1 = 10°$ it reports $i_2 = 39.546927°$ and confirms that
$\sin i_2/v_2$ still equals $\sin i_1/v_1 = 0.11576545$. Above $i_c$ the
transmitted angle has no solution: the code prints "evanescent", which is the
numerical signature of total internal reflection.

## 5. The small-angle approximation, and its price

For small $x$ (radians), $\sin x \approx x$ and $\tan x \approx x$. The
demonstration measures the error directly:

```text
 angle (deg)          sin x      x - sin x   rel. error          x^3/6
        0.10   0.0017453284      8.861e-10    5.077e-07      8.861e-10
        1.00   0.0174524064      8.861e-07    5.077e-05      8.861e-07
        5.00   0.0871557427      1.107e-04    1.270e-03      1.108e-04
       10.00   0.1736481777      8.847e-04    5.095e-03      8.861e-04
       20.00   0.3420201433      7.046e-03    2.060e-02      7.089e-03
       30.00   0.5000000000      2.360e-02    4.720e-02      2.392e-02
       45.00   0.7071067812      7.829e-02    1.107e-01      8.075e-02
```

Read the last two columns together. The error $x - \sin x$ is matched almost
exactly by $x^{3}/6$, the leading term of the Taylor series, which is the
subject of
[01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../05-single-variable-calculus/04-taylor-series.md).
At $1°$ the relative error is $5\times10^{-5}$ — better than any field
measurement. At $20°$ it is 2 percent, which is worse than a good survey. The
approximation is not "roughly right for small angles"; it has a number, and you
should know it before you use it.

## 6. Python demonstration

Run [`code/trig_foundations_demo.py`](./code/trig_foundations_demo.py). It uses
only the standard library, so it runs anywhere. Section 3 verifies six
trigonometric identities at 10 000 random arguments and reports the worst
absolute discrepancy for each:

```text
  pythagorean      2.220e-16
  addition         4.441e-16
  double-angle     3.331e-16
  half-angle       4.154e-14
  product-to-sum   2.359e-16
  sum-to-product   6.661e-16
```

Every discrepancy is at the level of double-precision round-off
($\varepsilon \approx 2.2\times10^{-16}$), and the half-angle line is the
instructive one: it is ten times larger because the half-angle formula uses a
square root and a sign that must be chosen from the quadrant. Numerical
verification does not prove an identity, but a discrepancy far above these
numbers would have told you the algebra was wrong.

## 7. Common mistakes

1. **Degrees where radians are required.** `sin(x)` in every programming
   language takes radians. Passing degrees gives an answer that is wrong but
   plausible, and it usually survives a sanity check.
2. **Mismatching a side with the wrong angle.** In $a^2 = b^2 + c^2 - 2bc\cos A$,
   the angle $A$ is opposite the side $a$. This is not a convention you can
   renegotiate.
3. **Believing the printed zero.** $\cos 90°$ is stored as $6.1\times10^{-17}$.
   Guard divisions, and prefer `atan2` to `atan` plus a special case.
4. **Treating the SSA case as if it were SAS.** Two sides and a non-included
   angle usually admit two triangles. Ask which one the physics allows.
5. **Using $\sin\theta \approx \theta$ with degrees, or beyond its range.**
   In radians the error is $x^{3}/6$; in degrees the approximation is not merely
   inaccurate, it is dimensionally meaningless.
6. **Reporting an apparent dip as a true dip.** The apparent dip is always
   smaller unless your section happens to face straight down the dip azimuth.
7. **Forgetting that a strike is a line.** Strike $020°$ and strike $200°$
   describe the same plane; the dip azimuth is what has a direction.

## 8. Real-world applications

- **Refraction seismology.** The critical angle and the ray parameter in
  Section 4.5 are how a two-layer survey is inverted for the deeper velocity,
  and the reason a refraction survey has a maximum useful offset.
- **Structural geology and seismic interpretation.** True dip from apparent dips
  is a daily calculation in the field and in interpretation software; get the
  quadrant wrong and a prospect is mapped on the wrong limb of a fold.
- **Focal mechanisms and moment tensors.** Take-off angles and azimuths to
  stations are all trigonometric constructions of the kind built here; the
  branch ambiguity of Section 4.4 reappears as the nodal-plane ambiguity.
- **Geodesy.** Angles are the primary observable. A theodolite measures angles,
  an epicentral distance is reported in degrees, and GNSS baselines are reduced
  with the spherical trigonometry of
  [01-03-04](./04-spherical-trigonometry.md).
- **Surveying and setting out.** Turning angles, offsets and closing errors are
  all elementary triangle problems, and the error budget is a trigonometric sum.

## 9. Further reading

- **Gelfand, I. M. and Saul, M. (2001). *Trigonometry*. Birkhäuser.** Level:
  beginner. Unusually conceptual for a school-level topic: it derives the
  addition formulas from rotations and does not shy away from the unit circle's
  role as the definition. Chapters 1–5 cover this lesson.
- **Bronshtein, I. N. and Semendyayev, K. A. *Handbook of Mathematics*.**
  Level: reference. A compact and reliable lookup for identities and triangle
  formulas. Editions vary; confirm the edition and page before citing.
- **Aki, K. and Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: advanced. The ray parameter and Snell's law
  treatment in Chapter 4 is the canonical development of Section 4.5; useful
  here as a target, not as prerequisite reading.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm current availability and editions through your library
> before relying on them.

## 10. Related lessons

- [01-03-02 Trigonometric Identities and Their Uses](./02-trig-identities.md) —
  the algebra that turns one trigonometric form into another.
- [01-03-03 Inverse Trigonometric Functions and Branch Ambiguity](./03-inverse-trig.md) —
  the SSA ambiguity of Section 3.4 treated properly.
- [01-03-04 Spherical Trigonometry and Great-Circle Geometry](./04-spherical-trigonometry.md) —
  what happens when the triangle is drawn on a sphere.
- [01-04-01 Euclidean Geometry and Geometric Reasoning](../04-geometry-and-coordinates/01-euclidean-geometry.md) —
  the synthetic-geometry view of the same facts.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../05-single-variable-calculus/04-taylor-series.md) —
  why $\sin x \approx x - x^{3}/6$ and what the next term is.

## Exercises and self-assessment

The exercises for this lesson are in
[`exercises/01-angles-and-triangles-exercises.md`](./exercises/01-angles-and-triangles-exercises.md),
with worked solutions in
[`exercises/01-angles-and-triangles-solutions.md`](./exercises/01-angles-and-triangles-solutions.md).

Check yourself before moving on. You should be able to say yes to all of these:

- [ ] I can convert $47°$ to radians and $0.9$ rad to degrees without a calculator,
      to two significant figures.
- [ ] I can state the sign of $\sin$, $\cos$ and $\tan$ in each quadrant and say
      which of them is undefined at $90°$ and why.
- [ ] I can derive the law of cosines from coordinates on a blank page.
- [ ] I can decide, from the given data, whether a triangle problem is ambiguous.
- [ ] I can compute a true dip from two apparent dips and state which extra
      information I need to resolve the quadrant.
- [ ] I can quote the relative error of $\sin x \approx x$ at $10°$ to one
      significant figure.
