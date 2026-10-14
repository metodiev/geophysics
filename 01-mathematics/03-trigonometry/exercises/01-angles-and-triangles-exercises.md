# Exercises — 01-03-01 Angles, Triangles and the Unit Circle

Attempt these **closed-book**, on paper, before opening the
[solutions](./01-angles-and-triangles-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Use radians unless a question states otherwise. Numerical answers should carry
only the significant figures the inputs justify.

---

## ★ Foundational

**★1.** Convert, showing the exact factor you used:

(a) $60°$ to radians
(b) $0.75$ rad to degrees
(c) $2.5$ rad to degrees
(d) $12°30'$ to radians

---

**★2.** For each angle, state the sign of the sine, cosine and tangent and give
their values, without using a calculator:

(a) $120°$
(b) $225°$
(c) $300°$

Then state which of the three angles has an undefined tangent and why.

---

**★3.** Arc length.

(a) A circular arc has radius 3.2 km and subtends $12°$ at the centre. Give its
length in metres.
(b) An arc of 250 m lies on a circle of radius 6371 km. Give the subtended angle
in radians, in degrees, and in arcseconds.

---

**★4.** Solve the triangle with $b = 7$, $c = 9$ and included angle
$A = 42°$. Find $a$, the remaining two angles, the circumdiameter $2R$, and the
area. State which law you used at each step and why.

---

## ★★ Applied

**★★5.** A planar bed has apparent dips of $25°$ in the north–south vertical
section and $40°$ in the east–west vertical section.

(a) Compute its true dip and dip azimuth.
(b) State its strike, and explain why a strike is a line rather than a direction.
(c) The same two apparent dips would also be produced by a plane dipping in the
opposite quadrant. State the alternative solution and explain what additional
field evidence would distinguish them.
(d) Why does the formula fail completely if the north–south apparent dip is
zero, and what should you use instead of $\arctan$?

---

**★★6.** Snell's law. A sediment of $v_1 = 2.0$ km/s overlies rock of
$v_2 = 6.0$ km/s.

(a) Compute the critical angle.
(b) A ray arrives at the interface with $i_1 = 20°$. Compute the ray parameter
$p = \sin i_1 / v_1$ and determine whether a transmitted ray exists. If it does,
give $i_2$.
(c) Explain, in terms of your answer to (b), why a refraction survey has a
maximum useful offset.

---

**★★7.** The small-angle approximation.

(a) Compute the relative error of $\sin x \approx x$ at $x = 4°$.
(b) Find the largest angle (in degrees) for which the relative error stays below
1 percent. Do this numerically, by bisection or by scanning, and state how you
checked your answer.
(c) Would the approximation be usable at that angle for a survey that needs
amplitudes good to 1 percent? Answer with a sentence, not a number alone.

---

**★★8.** A survey triangulation. Two stations are 1200 m and 900 m from a
reference mark, with an included angle of $65°$ between them.

(a) Compute the distance between the two stations.
(b) Compute the two remaining angles and check that the three angles sum to
$180°$.
(c) If each of the two lengths is known to $\pm0.5$ m and the angle to
$\pm0.05°$, estimate the uncertainty in the computed distance. State which
contribution dominates.

---

## ★★★ Research-oriented

**★★★9.** The apparent-dip relation was presented as
$\tan\alpha = \tan\delta\,|\sin(\varphi - \theta)|$ for a vertical section whose
horizontal trace points along azimuth $\varphi$. Do not take it on trust.

(a) Write a function that builds a plane from a given dip $\delta$ and dip azimuth
$\theta$, then measures the apparent dip in the vertical section along azimuth
$\varphi$ by intersecting the plane with that vertical plane and taking the angle
of the resulting line.
(b) Sweep $\delta \in \{10°, 30°, 60°\}$, $\theta \in \{0°, 45°, 130°, 275°\}$ and
$\varphi \in \{0°, 30°, 90°, 150°\}$ and report the worst absolute discrepancy
between your measured apparent dip and the formula.
(c) Report and explain any systematic pattern in the discrepancies: which
combinations are worst, and does the pattern depend on $\theta$ or on $\varphi$?
(d) State the limits of your verification: what class of error would it *not*
detect?

---

**★★★10.** Error propagation through an inverse trigonometric function.

A refraction survey measures an apparent dip of $25°$ in the north–south section
with an uncertainty of $\pm0.5°$, and $40°$ in the east–west section with an
uncertainty of $\pm0.5°$, both assumed independent.

(a) Propagate the uncertainty into the true dip $\delta$ and the dip azimuth
$\theta$, using partial derivatives and combining in quadrature.
(b) Repeat by Monte Carlo with at least $10^{5}$ samples and report the standard
deviations of $\delta$ and $\theta$.
(c) Compare (a) and (b). If they disagree, say why, and say which you would
report.
(d) Find the apparent-dip pair in the range $0°$–$90°$ for which the uncertainty
in $\theta$ is worst, and explain the result geometrically. This is a genuine
ill-conditioning question, and the framework for it is in
[01-01-05 Absolute vs Relative Error, Conditioning and Stability](../../01-arithmetic/05-error-and-conditioning.md).

---

## Extension ideas

- Rewrite ★4 as a function `solve_sas(b, c, A)` returning the complete triangle,
  and test it against a right-angled case where $A = 90°$ and the answer must
  reduce to Pythagoras.
- For ★6, plot the transmitted angle $i_2$ against $i_1$ from $0°$ to the critical
  angle and describe what happens to the slope of the curve as $i_1 \to i_c$.
  This is the ill-conditioning that
  [01-03-03](../03-inverse-trig.md) quantifies with the derivative of
  $\arcsin$.
