# Exercises — 04-02-02 Divergent, Convergent and Transform Boundaries

Attempt these **closed-book** before opening the
[solutions](./02-plate-boundaries-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/plate_boundaries_demo.py`](../code/plate_boundaries_demo.py) require you
to run it and report its actual output. Use $\mu = 3\times10^{10}$ Pa and
$M_w = \frac23(\log_{10}M_0 - 9.1)$ with $M_0$ in N·m.

---

## ★ Foundational

**★1.** A rupture is 30 km long and 15 km wide and slips 0.8 m.

(a) Compute the rupture area in m².
(b) Compute $M_0 = \mu A D$ in N·m.
(c) Compute $M_w$.
(d) State the magnitude of the rupture if the slip were 1.6 m instead.

---

**★2.** A magnitude 7.5 earthquake.

(a) Compute its seismic moment from
$M_0 = 10^{1.5M_w + 9.1}$.
(b) Compute the fault area needed for a slip of 2.0 m at $\mu = 3\times10^{10}$ Pa.
(c) Express the area in km² and describe a plausible fault that would produce it.
(d) State the factor by which $M_0$ increases from $M_w$ 7 to $M_w$ 8.

---

**★3.** A boundary strikes at azimuth 20° and the relative velocity across it is
45 mm/a toward azimuth 60°.

(a) Compute the boundary-normal unit vector's azimuth.
(b) Compute $v_\perp$ and $v_\parallel$.
(c) Compute the obliquity.
(d) Classify the boundary and state which component produces thrusting.

---

## ★★ Applied

**★★4.** Focal mechanism. A fault strikes at 180°, dips 60° and has a rake of
−90°.

(a) State the fault type.
(b) Compute the plunge of the P axis and of the T axis.
(c) State which is steeper and why that is the rule of thumb.
(d) Repeat (a) to (c) for a strike of 90°, a dip of 45° and a rake of 90°.

---

**★★5.** The moment budget. Recompute the demo's partition with these
illustrative values:

| Type | Length (km) | Seismogenic width (km) | Slip rate (mm/a) |
|---|---|---|---|
| Subduction | 40 000 | 80 | 50 |
| Continental transform | 25 000 | 20 | 25 |
| Spreading ridge | 55 000 | 8 | 45 |

(a) Compute the moment rate for each, in N·m per year.
(b) Compute each type's percentage share.
(c) Compare with the demo's 91 per cent for subduction and explain the
difference.
(d) State whether the conclusion is changed.

---

**★★6.** Aseismic coupling. A margin releases only 60 per cent of its
convergence seismically.

(a) Compute the moment rate of a 1000 km by 150 km megathrust converging at
60 mm/a with full coupling.
(b) Recompute with 60 per cent coupling.
(c) State how the recurrence interval of a given magnitude changes.
(d) State whether the *hazard* changes by the same factor, and why not.

---

## ★★★ Research-oriented

**★★★7.** A smaller margin. A 600 km long megathrust has a 120 km seismogenic
width and converges at 70 mm/a.

(a) Compute its moment rate in N·m per year.
(b) Assuming $b = 1$ between $M_w$ 6.0 and 9.5, find the Gutenberg–Richter
intercept $a$ that balances the moment over that range:

$$10^a = \frac{\tfrac12\,\dot M_0}{\ln 10 \cdot 10^{9.1}
\left(10^{0.5M_\text{max}} - 10^{0.5M_\text{min}}\right)} .$$
(c) Compute the mean interval of $M_w \ge 8$ events.
(d) Recompute (c) with a coupling coefficient of 0.6, and state what the two
numbers bracket.

---

**★★★8.** Run
[`../code/plate_boundaries_demo.py`](../code/plate_boundaries_demo.py) and report:

(a) the P and T plunges and azimuths for the four mechanisms;
(b) the first-motion sign grid for the three canonical mechanisms and the number
of quadrants in each;
(c) the obliquity decomposition for a strike of 0° with velocities at azimuths
90°, 60° and 0°;
(d) $M_0$ and $M_w$ for the 50 km × 20 km and 200 km × 50 km ruptures and the
factor between them;
(e) the moment-rate shares for the four boundary types;
(f) two sentences on which inputs are labelled illustrative and why.

---

**★★★9.** The P/T sign convention. The demo takes the slip vector as the motion
of the footwall.

(a) Recompute the four mechanisms in (8a) with the opposite sign for the slip
vector.
(b) State precisely which pairs of numbers swap.
(c) State which of the two conventions is used in a published moment-tensor
catalogue you can consult, and how you verified it.
(d) State why the first-motion radiation pattern is unaffected by the sign
choice.
