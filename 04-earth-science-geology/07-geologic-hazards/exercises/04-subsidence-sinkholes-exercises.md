# Exercises — 04-07-04 Subsidence, Sinkholes and Karst

Attempt these **closed-book** before opening the
[solutions](./04-subsidence-sinkholes-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/subsidence_sinkholes_demo.py`](../code/subsidence_sinkholes_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** A confined aquifer is dewatered by 8 m in a basin where a 25 m thick clay
layer has $m_v = 0.4$ m² MN⁻¹.

(a) Compute the increase in effective stress at the clay.
(b) Compute the compaction of the clay layer.
(c) State the two assumptions about the strain that (2) encodes.
(d) State whether the compaction would be recovered if the aquifer were
recharged, and why.

---

**★2.** Take $g = 9.80665$ m s⁻² and $R = 6.371\times10^6$ m.

(a) Derive and evaluate the free-air gradient $2g/R$ in mGal m⁻¹ and in
µGal cm⁻¹.
(b) Compute the Bouguer gradient for a rock of density 2670 kg m⁻³.
(c) Compute the residual (free-air minus Bouguer) gradient.
(d) State what a borehole gravimeter measures in uniform rock, and what a
departure from that value means.

---

**★3.** A karst catchment has a recharge of 0.6 m a⁻¹ and a dissolved-load
concentration of 80 mg L⁻¹; the rock density is 2700 kg m⁻³.

(a) Compute the denudation rate in mm ka⁻¹.
(b) Compute the time required to remove a 20 m thick void.
(c) State which of the three inputs in (a) is the most uncertain in the field,
and why.
(d) State what quantity a geophysical survey can contribute to sinkhole hazard
that the denudation rate cannot.

---

**★4.** A normally consolidated clay has $C_c = 0.35$, $e_0 = 0.9$, a thickness
of 20 m and an initial effective stress of 120 kPa. The effective stress
increases by 60 kPa.

(a) Compute the compaction using the compression-index form.
(b) Explain what "normally consolidated" means and what changes if the clay is
over-consolidated.
(c) State why the logarithmic form is preferred over a single $m_v$ for a large
stress change.

---

## ★★ Applied

**★★5.** Run the demo's section 1.

(a) Report the compaction for $m_v = 0.1$, $0.5$ and $1.5$ m² MN⁻¹ and the
effective-stress increase used.
(b) Report the compaction for $\sigma'_0 = 50$, 100 and 200 kPa.
(c) Compute the value of $m_v$ that would give exactly 1.0 m of compaction for
this layer and drawdown.
(d) State, in two sentences, what a seismic reflection section could contribute
to this calculation and what it could not.

---

**★★6.** Run the demo's section 6, which uses $\phi = 0.30$ and a 5 m decline.

(a) Report the mass term, the free-air term and their sum.
(b) Recompute the mass term for $\phi = 0.15$ and $\phi = 0.45$.
(c) Compute the ratio of the free-air term to the mass term, and show that it is
independent of the depth of the layer and of the density of the draining fluid.
(d) Compute the smallest water-level decline detectable at a repeatability of
5 µGal for $\phi = 0.30$.

---

**★★7.** Run the demo's section 5 for C-band ($\lambda = 5.56$ cm).

(a) Report the phase change for 1 cm of line-of-sight motion, in radians and in
fringes, and the line-of-sight displacement corresponding to one fringe.
(b) Report $u_\mathrm{LOS}/u_z$ at $\theta = 39^\circ$, and compute the vertical
displacement that produces exactly one fringe at that incidence angle.
(c) An ascending track gives $+2.0$ cm and a descending track $-1.0$ cm of
line-of-sight motion at $\theta = 39^\circ$. Solve for the vertical and
horizontal components.
(d) State what a single track would have reported for the vertical displacement
and by how much it would have been wrong.

---

## ★★★ Research-oriented

**★★★8.** A soil cavity is approximated as a sphere of diameter $D$ whose centre
is 3 m below the surface, in material of density 1800 kg m⁻³. Use the crude roof
model of (10) with $\sigma_t = 20$ kPa for the stability question and the point
sphere formula for the gravity question.

(a) Compute the critical span for a 3 m roof, and state how the critical span
changes if the roof thickness doubles.
(b) Compute the microgravity anomaly at the surface directly above a cavity of
diameter 3 m.
(c) Repeat (b) for a cavity of diameter 1 m, and compare both with a survey
repeatability of 5 µGal.
(d) State what this pair of calculations says about the kind of cavity a
microgravity survey can and cannot find, and name the second method you would
add and why.

---

**★★★9.** A subsidence monitoring programme combines gravity with levelling.

(a) Compute the gravity error introduced by a 1 cm error in the measured
elevation of a benchmark, using the free-air gradient.
(b) Compare it with a gravity repeatability of 5 µGal and state the elevation
precision required to keep the elevation error below the gravity error.
(c) For $\phi = 0.30$, compute the mass term in µGal for a 1 m water-level
decline and compare it with the elevation-induced error from (a).
(d) Explain, in no more than five sentences, why a programme that measures
gravity without elevation cannot detect a mass change at all, and what an
independent measurement of elevation (GNSS, levelling, InSAR) contributes.
