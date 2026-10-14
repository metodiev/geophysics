# Exercises — 04-02-04 Plate Motion Frames, Euler Poles and Global Models

Attempt these **closed-book** before opening the
[solutions](./04-plate-motion-frames-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/plate_motion_frames_demo.py`](../code/plate_motion_frames_demo.py)
require you to run it and report its actual output. Use $R = 6371$ km and the
unit equality 1 km/Ma = 1 mm/a.

---

## ★ Foundational

**★1.** An Euler vector has an angular rate of 0.50 °/Ma.

(a) Convert the rate to rad/Ma.
(b) Compute the speed at a site 40° from the pole.
(c) Compute the speed at the pole and at 90° from it.
(d) State the general expression for the speed and the name of the curve the
motion follows.

---

**★2.** A pole is at (50° N, 120° W) with a rate of 0.70 °/Ma, and a site is at
(20° N, 130° W).

(a) Compute the angular distance from the pole to the site.
(b) Compute the site's speed.
(c) Compute the east and north components of the velocity, given that the demo
reports `east 39.18, north -8.69` mm/a.
(d) State the azimuth of motion and whether it is consistent with a small circle
about the pole.

---

**★3.** A rotation is sustained for 30 Ma at 0.70 °/Ma.

(a) Compute the total rotation angle.
(b) State whether the rotation is "small" in the sense in which finite rotations
may be added as vectors.
(c) State the number of independent parameters needed to describe a *relative*
instantaneous plate motion.
(d) State the number needed for a finite rotation.

---

## ★★ Applied

**★★4.** A pole at the north geographic pole. Take $\omega = (0, 0, 6.981\times
10^{-3})$ rad/Ma.

(a) Compute the velocity at the equator, in mm/a, and its azimuth.
(b) Compute it at 40° N and at 40° S.
(c) Invert: given only the three speeds 44.48, 34.07 and 34.07 mm/a at latitudes
0°, 40° and −40°, recover the pole and the rate.
(d) State what feature of the geometry made (c) easy and what would make it hard.

---

**★★5.** Rank deficiency.

(a) Compute the rank of the design matrix for sites at (40° N, 0°) and
(60° N, 0°), and state the singular values.
(b) Compute it for sites at (40° N, 0°) and (40° S, 180°).
(c) Explain (b) in one sentence from the geometry of $[\mathbf{r}]_\times$.
(d) State the practical rule for siting a network that is meant to determine a
pole.

---

**★★6.** The frame problem. A site at (30° N, 60° W) has a plate-pair velocity of
`east 20.00, north 5.00` mm/a in one frame.

(a) Compute the velocity contribution of an additional rigid rotation of
0.30 °/Ma about a pole at (0°, 0°), using the demo's value of
`east -8.34, north -28.89` mm/a for that rotation at this site.
(b) Compute the site velocity in the shifted frame.
(c) State what happens to the *relative* velocity between the two plates.
(d) Name the three kinds of frame convention used in practice.

---

## ★★★ Research-oriented

**★★★7.** Closure error growth.

The demo's circuit has a vector-sum error of 1.22 per cent for rotations of a few
degrees. Measured across a family of scaled circuits, the relative closure error
is 0.16 per cent at a maximum rotation of 0.7°, 0.81 per cent at 3.4°,
1.62 per cent at 6.9° and 3.25 per cent at 13.8°.

(a) Show that the relative error is approximately proportional to the rotation
angle.
(b) State the physical reason for the proportionality.
(c) Estimate the relative error for a reconstruction spanning 60°.
(d) State what a plate reconstruction spanning 100 Ma therefore has to do
instead of adding rotation vectors.

---

**★★★8.** Run
[`../code/plate_motion_frames_demo.py`](../code/plate_motion_frames_demo.py) and
report:

(a) the speed and azimuth at the six sites, and whether the two speed columns
agree;
(b) the three rotation vectors of the circuit and the vector sum with its
relative error;
(c) the recovered pole, rate, errors and design-matrix rank from the eight-site
inversion;
(d) the RMS horizontal residual and how it compares with the added noise;
(e) the singular values and rank for one site and for two sites, and the
unconstrained direction for one site;
(f) the frame-shift difference at the site;
(g) three sentences on what the demo verifies about the *method* and what it
does not verify about the Earth.

---

**★★★9.** Units. For each combination below, state the unit of
$\boldsymbol\omega \times \mathbf{r}$ and whether it is a velocity a geodesist
would quote:

(a) $\mathbf{r}$ in km, $\boldsymbol\omega$ in rad/Ma.
(b) $\mathbf{r}$ in m, $\boldsymbol\omega$ in rad/a.
(c) $\mathbf{r}$ in m, $\boldsymbol\omega$ in rad/Ma.
(d) $\mathbf{r}$ in km, $\boldsymbol\omega$ in °/Ma.

Then state the one conversion you need to remember to make all four usable.
