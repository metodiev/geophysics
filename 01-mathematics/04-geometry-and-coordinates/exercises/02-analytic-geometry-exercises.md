# Exercises — 01-04-02 Analytic Geometry: Lines, Planes and Distances

Attempt these **closed-book**. Solutions are in
[`02-analytic-geometry-solutions.md`](./02-analytic-geometry-solutions.md).
Difficulty: ★ foundational · ★★ applied · ★★★ research-oriented.

Coordinates are $(x, y, z) = (\text{east, north, up})$ in metres unless stated.
State your normal-sign convention wherever a dip azimuth is computed.

---

## ★ Foundational

**★1.** For the points $A = (1200, -300, 145.2)$ and $B = (-400, 850, 88.6)$:

(a) compute the horizontal distance between them;
(b) compute the three-dimensional distance;
(c) compute the bearing (azimuth, clockwise from north) from $A$ to $B$;
(d) compute the mid-point and state whether its elevation is the average of the
two if the two points are survey stations of different quality.

---

**★2.** Find the equation of the plane through $(0, 0, 100)$,
$(1000, 0, -477.3503)$ and $(0, 700, 100)$ in the form
$(\mathbf{p}-\mathbf{p}_0)\cdot\mathbf{n} = 0$, giving $\mathbf{n}$ as a unit
vector with $n_z \ge 0$.

---

**★3.** For the plane of ★2, compute the signed perpendicular distance from the
point $(400, 400, 400)$ and the vertical distance. State the sign convention and
what the sign means physically.

---

## ★★ Applied

**★★4.** Three points on a reflector are $P_1 = (0, 0, 250)$,
$P_2 = (800, 300, 180)$ and $P_3 = (-200, 900, 305)$.

(a) Compute the dip and dip azimuth.
(b) Compute the strike and state why it may be reported in either of two
directions.
(c) Verify the dip by an independent route: write the plane as $z = f(x,y)$,
compute the gradient, and obtain the dip and azimuth from the steepest descent
direction.
(d) Comment on whether the dip azimuth is well determined, given that the dip is
only about $6°$.

---

**★★5.** A bedding plane dips $35°$ towards $130°$ and a dyke dips $75°$ towards
$40°$.

(a) Write the unit normal of each plane.
(b) Compute the direction of their line of intersection.
(c) Convert that direction to a plunge and a trend, and state the opposite sense.
(d) Verify that the intersection direction is perpendicular to both normals.
(e) Give a geological interpretation of the result in one sentence.

---

**★★6.** *(This is the mastery checkpoint of the module README.)* The reflector of
★★4. A borehole is planned at $(400, 400)$ with a surface elevation of $400$ m.

(a) How far vertically below the surface will the borehole intersect the
reflector?
(b) The borehole is deviated so that it follows the direction
$(0.10, 0.05, -0.9937)$ — nearly vertical, with a slight easterly and northerly
lean — starting at $(400, 400, 400)$. Compute the along-hole distance to the
reflector.
(c) Compare (a) and (b), and state which number a driller needs.

---

**★★7.** Shoelace areas.

(a) Compute the area of the quadrilateral with vertices $(0,0)$, $(1200,0)$,
$(1500,900)$, $(300,1400)$ in km by the shoelace formula.
(b) Reverse the vertex order and recompute. What changed?
(c) Two of the vertices are moved onto the line joining the other two, to within
1 m. Compute the area again and comment on the numerical behaviour.
(d) State one quantity in a geophysical workflow that this formula computes
directly.

---

**★★8.** A plane is fitted to three points separated by about 1 km, with
$\pm0.1$ m vertical and $\pm0.3$ m horizontal survey accuracy. The three points
give a dip of $1.5°$ and a dip azimuth of $200°$.

(a) Estimate the uncertainty in the dip and in the dip azimuth, using the
geometric argument that the azimuth uncertainty scales as $\sigma_{\text{dip}} /
\tan\delta$.
(b) Repeat for a dip of $15°$.
(c) State what you would report in each case.

---

## ★★★ Research-oriented

**★★★9.** Verify a dip-and-strike implementation exhaustively.

(a) Implement `dip_and_strike(p1, p2, p3)` from the cross product, forcing
$n_z \ge 0$.
(b) Generate at least $10^4$ random synthetic planes with known dip and dip
azimuth, sample three points on each with realistic horizontal separations, and
recover the dip and azimuth.
(c) Report the worst errors in dip and in azimuth, and the distributions of both.
(d) Identify the regime in which the recovery degrades, and characterise it in
terms of the dip and the point geometry.
(e) Confirm the "downward normal" failure mode explicitly: compute the azimuth
from $-n_z$-forced normal and report the error, then state the test that catches it.
(f) State the limits of your verification.

---

**★★★10.** Error propagation into a plane's attitude.

For the synthetic plane of ★★★9, add independent Gaussian errors of $\sigma_h$ to
each horizontal coordinate and $\sigma_v$ to each elevation.

(a) Map the dip uncertainty and the azimuth uncertainty over a grid of dips from
$1°$ to $60°$, with $\sigma_h = 0.3$ m, $\sigma_v = 0.1$ m and separations of
0.5 km, 1 km and 5 km.
(b) Report the dip above which the azimuth uncertainty falls below $1°$, for each
separation.
(c) Report the dip below which the dip *magnitude* uncertainty exceeds $0.5°$.
(d) Explain the two thresholds geometrically, and state what you would tell an
interpreter whose structure is flatter than the lower threshold.
(e) State what your study does **not** establish.

---

## Extension ideas

- Implement `volume_below_plane(points, plane)` for a gridded horizon, computing
  the rock volume between a reference plane and a mapped surface.
- Implement the two-plane intersection and use it to compute the fold-axis
  orientation of a chevron fold from its two limb attitudes, then check the result
  against a stereonet construction.
