# Exercises — 04-02-03 Mantle Convection, Slab Pull and Ridge Push

Attempt these **closed-book** before opening the
[solutions](./03-driving-forces-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/driving_forces_demo.py`](../code/driving_forces_demo.py) require you to
run it and report its actual output. Use $\kappa = 10^{-6}$ m²/s,
$\alpha = 3\times10^{-5}$ K⁻¹, $\Delta T = 1300$ K, $\rho_m = 3300$,
$\rho_w = 1000$ kg/m³, $g = 9.81$ m/s² and $3.15576\times10^7$ s per year.

---

## ★ Foundational

**★1.** Slab buoyancy. A slab that cooled for 80 Ma before subduction has a mass
excess per unit area of $6.637\times10^6$ kg/m² over a 100 km thick section.

(a) Compute the force per unit length of trench for a slab segment 800 km long.
(b) Compute it for a segment 660 km long.
(c) State the ratio and what it means about quoting "the" slab pull.
(d) State which of the two numbers is closer to the value usually quoted in the
literature, and why.

---

**★2.** Ridge push. The ridge stands 3547 m above 100 Ma ocean floor.

(a) Compute the pressure difference at the base of the plate,
$g(\rho_m-\rho_w)\Delta h$, in Pa.
(b) Compute the ridge-push force per unit length for $h = 70$ km.
(c) State which input the answer is most sensitive to.
(d) State the order of magnitude of ridge push relative to slab pull.

---

**★3.** Basal drag.

(a) Compute the shear traction $\tau = \eta v/d$ for $\eta = 5\times10^{19}$ Pa·s,
$v = 30$ mm/a and $d = 150$ km.
(b) Compute the force per unit length of margin over a plate 8000 km long.
(c) State the two things a traction magnitude does not tell you.

---

## ★★ Applied

**★★4.** The required viscosity. Take the slab pull of a 100 Ma slab counted to
660 km as $4.624\times10^{13}$ N/m and an asthenospheric thickness of 200 km.

(a) Compute the viscosity required to balance it for $v = 40$ mm/a over an
8000 km plate.
(b) Recompute for $v = 60$ mm/a over a 12 000 km plate.
(c) Compare both with the range inferred from post-glacial rebound.
(d) State why this comparison is the strongest evidence that the force
estimates are right.

---

**★★5.** The Rayleigh number.

(a) Compute $\mathrm{Ra} = \rho g\alpha\Delta T d^3/(\eta\kappa)$ for
$\eta = 3\times10^{20}$ Pa·s and $d = 2890$ km.
(b) Compute it for $d = 700$ km and the same viscosity.
(c) Compare both with $\mathrm{Ra}_\text{crit} \approx 10^3$.
(d) State what a Rayleigh number of this size settles and what it does not.

---

**★★6.** Age dependence of slab pull. The mass excess per unit area is
$3.642\times10^6$ kg/m² at 20 Ma and $7.870\times10^6$ kg/m² at 140 Ma.

(a) Compute the ratio of the forces.
(b) State the physical reason for the direction of the ratio.
(c) State the observable prediction it makes about plate speeds.
(d) State how strongly that prediction is supported.

---

## ★★★ Research-oriented

**★★★7.** Dip and the useful force.

The slab-pull force acts down the dip of the slab.

(a) For a slab pull of $5.0\times10^{13}$ N/m, compute the horizontal component
for dips of 30°, 45° and 60°.
(b) State which dip gives the largest horizontal drive and why.
(c) State what other property of the slab changes with dip, and whether it acts
in the same direction.
(d) Write two sentences on why a steep slab can be both strongly pulled and
weakly effective at driving its plate.

---

**★★★8.** Run
[`../code/driving_forces_demo.py`](../code/driving_forces_demo.py) and report:

(a) the mass excess per unit area and the scale depth for slab ages 20, 60, 100
and 140 Ma;
(b) the force for $L = 660$ km and $L = 2900$ km at 100 Ma, and their ratio;
(c) the ridge-push range over $h = 40$ to 100 km;
(d) the basal traction and force for $\eta$ from $10^{19}$ to $10^{21}$ Pa·s;
(e) the viscosity required for four combinations of plate speed and length;
(f) the Rayleigh numbers for two viscosities and two layer thicknesses;
(g) three sentences on which of the outputs are robust conclusions and which are
definition-dependent.

---

**★★★9.** Ranking and its limits. Write a short assessment (200 to 300 words)
that:

(a) ranks slab pull, ridge push and basal drag by order of magnitude;
(b) states for each what its dominant uncertainty is;
(c) states which part of the ranking is robust to changing the inputs by a
factor of two and which is not;
(d) names one observation that would, in principle, settle the sign of basal
drag, and says why it is hard to make.
