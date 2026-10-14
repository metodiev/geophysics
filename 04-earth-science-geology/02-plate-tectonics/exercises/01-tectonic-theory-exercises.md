# Exercises — 04-02-01 Continental Drift to Plate Tectonics: The Evidence Trail

Attempt these **closed-book** before opening the
[solutions](./01-tectonic-theory-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/tectonic_theory_demo.py`](../code/tectonic_theory_demo.py) require you
to run it and report its actual output. Use $\kappa = 10^{-6}$ m²/s,
$k = 3.2$ W m⁻¹ K⁻¹, $\alpha = 3\times10^{-5}$ K⁻¹, $\Delta T = 1300$ K,
$\rho_m = 3300$, $\rho_w = 1000$ kg/m³ and the Julian year
$3.15576\times10^7$ s.

---

## ★ Foundational

**★1.** A magnetic anomaly profile at a ridge has a normal-polarity stripe of
age interval 0.70 Ma.

(a) Compute its width at a half-spreading rate of 25 mm/a, in km.
(b) Compute the distance from the ridge of a stripe that is 2.2 Ma old.
(c) State why the two flanks should carry the same sequence.
(d) State what the pattern would look like if the spreading rate changed midway.

---

**★2.** Subsidence.

(a) Compute the subsidence coefficient
$C = [2\rho_m\alpha\Delta T/(\rho_m-\rho_w)]\sqrt{\kappa/\pi}$, in
m/$\sqrt{\text{s}}$.
(b) Compute the subsidence at 50 Ma, in metres.
(c) Compare with the empirical form $2500 + 350\sqrt{t}$ at the same age.
(d) State the physical origin of the coefficient's dependence on
$\alpha\Delta T$.

---

**★3.** Heat flow.

(a) Compute $q(t) = k\Delta T/\sqrt{\pi\kappa t}$ at 25 Ma, in mW/m².
(b) Compute it at 100 Ma.
(c) State the two ways in which (b) differs from (a) — one in the value and one
in the model's validity.

---

## ★★ Applied

**★★4.** Inversion. A marine magnetic survey finds a stripe 40 km wide that
matches a reversal interval of 0.90 Ma.

(a) Compute the half-spreading rate in mm/a.
(b) Compute the full spreading rate.
(c) Compute how far from the ridge the crust of that interval is at its far
edge.
(d) State what independent information the reversal interval's duration
represents, and why that independence matters.

---

**★★5.** Symmetry. The east flank of a ridge has stripes at distances
15, 27, 45 and 80 km from the axis.

(a) State the expected west-flank distances.
(b) State the correlation the demo reports for its synthetic profile.
(c) State what a correlation of about 0.2 between the flanks would imply.

---

**★★6.** Age limit. A plate moves at 60 mm/a and its ridge-to-trench distance is
9000 km.

(a) Compute the maximum age of the ocean floor it carries.
(b) Recompute for a plate at 30 mm/a with the same ridge-to-trench distance.
(c) State why the *finiteness* of the maximum age is a stronger argument than
its value.

---

## ★★★ Research-oriented

**★★★7.** A rate change within the pattern. Suppose the half-spreading rate is
25 mm/a for the first 5 Ma of the pattern and 40 mm/a thereafter.

(a) Compute the half-width of the crust created during the first 5 Ma.
(b) Compute the age at a distance of 240 km from the ridge.
(c) State which stripes have widths set by 25 mm/a and which by 40 mm/a, and by
how much the later ones are wider.
(d) State what an inversion that assumed a constant rate would recover.

---

**★★★8.** Run
[`../code/tectonic_theory_demo.py`](../code/tectonic_theory_demo.py) and report:

(a) the number of polarity intervals and the age span of the synthetic sequence;
(b) the misfit at 24, 25 and 26 mm/a and the recovered rate;
(c) the flank correlation;
(d) the computed subsidence coefficient and the subsidence at 100 Ma next to the
empirical value;
(e) the computed and empirical heat flow at 1, 20 and 150 Ma;
(f) the three maximum-age estimates;
(g) three sentences on which numbers in the output are computed, which are
tabulated, and which are an input the inversion is asked to recover.

---

**★★★9.** Critique. For each statement, say whether it is an observation, an
inference, or an assumption, and what could falsify it.

(a) Continental coastlines fit together.
(b) The two flanks of a ridge carry mirror-image magnetic stripes.
(c) The reversal timescale is globally synchronous.
(d) The ocean floor is destroyed at trenches.
(e) The half-space cooling model describes ocean floor younger than 70 Ma.
