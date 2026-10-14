# Exercises — 04-04-05 Reading Geological Maps and Constructing Cross-Sections

Attempt these **closed-book** before opening the
[solutions](./05-geologic-maps-sections-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/05-maps_and_sections_demo.py`](../code/05-maps_and_sections_demo.py)
require you to run it and report its actual output.

**Conventions.** Map coordinates are (east, north) in metres with elevation $z$
positive upwards. Strike is clockwise from north, dip is to the right of strike.
A planar surface is $z = ax + by + c$.

---

## ★ Foundational

**★1.** A plane has $a = -0.375$ and $b = -0.055556$.

(a) Compute the dip.
(b) Compute the dip azimuth.
(c) Compute the strike.
(d) State which direction the dip azimuth corresponds to, and why a sign error here
produces an answer that looks plausible.

---

**★2.** A unit has a vertical thickness of 100 m in a borehole and dips 60°.

(a) Compute its true thickness.
(b) Compute the ratio of vertical to true thickness.
(c) Repeat for a dip of 30°.
(d) State what an isopach map shows and what a borehole measures.

---

**★3.** Three points on a plane are $(0, 0, 400)$, $(1200, 0, -50)$ and
$(400, 900, 200)$.

(a) Write down the design matrix for a least-squares fit of $z = ax + by + c$.
(b) State how many unknowns there are and whether the system is over- or
under-determined.
(c) Compute the triangle area formed by the three points in map coordinates.
(d) State why that area is a diagnostic of the solution's quality.

---

## ★★ Applied

**★★4.** Run [`../code/05-maps_and_sections_demo.py`](../code/05-maps_and_sections_demo.py).

(a) Report the fitted coefficients from both solution methods and the largest
difference between them.
(b) Report the residuals of the three points against the fitted plane.
(c) Report the recovered attitude and the error against the input.
(d) State what the agreement of the two methods verifies and what it does not.

---

**★★5.** The demo runs a round trip over eight synthetic attitudes.

(a) Report the worst strike and dip errors over the suite.
(b) Report the triangle area used and state why it was held fixed.
(c) Report the worst errors for the near-collinear test at triangle areas of
25 000 m², 500 m² and 0.5 m².
(d) State what the failure mode is and why it is dangerous.

---

**★★6.** A marker horizon is determined from three boreholes to have
$z = -0.375x - 0.055556y + 400$, and a fourth location is at $(1500, 600)$ with a
collar elevation of 500 m.

(a) Compute the marker elevation at the fourth location.
(b) Compute the depth to the marker below the collar.
(c) Explain how the demo checks that the prediction is on the plane.
(d) State the outcrop trace direction and why it must equal the strike.

---

## ★★★ Research-oriented

**★★★7.** You must site a fourth borehole and the three existing collars are at
$(0,0)$, $(1200,0)$ and $(400,900)$ with marker depths of 100 m, 550 m and 300 m.

(a) Compute the plane through the three points and its attitude.
(b) Compute the triangle area and express it as a fraction of the area of the
smallest rectangle containing the three collars.
(c) You may add a fourth shallow borehole anywhere within 2 km of the origin to
improve the solution. State where you would place it, and show by computing the
new triangle area(s) and the implied improvement how it helps. State what
determines the improvement and why adding a point *inside* the existing triangle
contributes nothing to a plane that is already exactly determined.
(d) State the two independent sources of error in a four-hole solution and how you
would estimate each.

---

**★★★8.** A bed with $z = -0.375x - 0.055556y + 400$ is cut by a fault with
$z = 0.866025x + 1.5y$ (strike 120°, dip 60°).

(a) Subtract the two plane equations and show that the result is a line in the map
plane.
(b) Compute the direction of that line and its azimuth.
(c) Find a point on the intersection and verify that it satisfies both plane
equations.
(d) State what this line represents on a map, what the offset of the bed across
the fault in a cross-section is called, and why it is not the slip.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
