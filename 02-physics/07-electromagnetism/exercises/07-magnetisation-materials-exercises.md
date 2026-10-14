# Exercises — 02-07-07 Magnetisation, Susceptibility and Magnetic Materials

Attempt these **closed-book** before opening the
[solutions](./07-magnetisation-materials-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/magnetisation_materials_demo.py`](../code/magnetisation_materials_demo.py)
require you to run it and report its actual output. **Every susceptibility and
remanent magnetisation you are given is a nominal order-of-magnitude value** unless
the question says it is a measurement; say so in your answers. Use
$\mu_0 = 1.256\,637\,062\,12\times10^{-6}$ N/A².

---

## ★ Foundational

**★1.** The geomagnetic field at a site has $B = 50$ µT.

(a) Compute $H = B/\mu_0$ in A/m, and state the units of $\mathbf B$, $\mathbf H$
and $\mathbf M$.
(b) For $\chi = 10^{-3}$, $10^{-2}$ and $10^{-1}$, compute $M = \chi H$,
$B = \mu_0(1+\chi)H$ and the anomaly $B-B_{\text{ambient}}$ in nT.
(c) Compute $\mu_r$ for each.
(d) Explain why the phrase "the anomaly is 500 nT" must be accompanied by the
ambient field, and why $B$ and $H$ cannot be added.

---

**★2.** Curie depth.

(a) Compute the depth at which a linear geotherm reaches 580 °C for surface
temperature 10 °C and gradients of 15, 25 and 40 °C/km.
(b) State every assumption in that calculation.
(c) Explain what physically happens at that depth and what the observable
consequence is for a long-wavelength magnetic anomaly.
(d) State why the answer is a model output rather than a measurement, and what
measurement would test it.

---

**★3.** Demagnetising factors.

(a) For $\chi = 0.05$ and $N = 0$, $1/3$ and $1$, compute $\chi_{\text{eff}} =
\chi/(1+N\chi)$.
(b) Compute the same for $\chi = 5$ and explain the difference in the pattern.
(c) State the upper bound on $\chi_{\text{eff}}$ for each $N$ and prove it from
the formula.
(d) Explain why this is a first-order effect for magnetite-rich rock and negligible
for weakly magnetic sediments.

---

**★4.** Induced versus remanent.

(a) For a basalt with $\chi = 0.05$ (nominal) in a 50 µT field, compute the
induced magnetisation.
(b) For a remanent magnetisation of 5 A/m (nominal), compute the Koenigsberger
ratio $Q$.
(c) Repeat for a sediment with $\chi = 10^{-4}$ and $M_r = 10^{-3}$ A/m.
(d) State what the two $Q$ values imply about what a magnetic survey of each rock
type actually maps.

---

## ★★ Applied

**★5.** Buried dipole anomalies.

(a) Compute the surface anomaly directly above a vertically magnetised body of
volume 1 km³ and magnetisation 1 A/m at a depth of 2 km.
(b) Compute the moment required for a 100 nT anomaly at 3 km depth.
(c) Compute the volume of rock with $M = 1$ A/m that would be needed for that
moment.
(d) Explain why a body of the same volume but twice the depth produces an anomaly
eight times smaller, and what that implies for depth estimation from magnetic data.

---

**★6.** SI and cgs susceptibility.

(a) State the conversion for volume susceptibility and derive the factor $4\pi$
from $\mathbf B = \mu_0(\mathbf H + \mathbf M)$ in SI and
$\mathbf B = \mathbf H + 4\pi\mathbf M$ in cgs.
(b) Convert $\chi = 0.001$, 0.01 and 1 (cgs) to SI.
(c) For each, compute the induced magnetisation in a 50 µT field and the anomaly
in nT.
(d) State which of the three is achievable by a natural rock, and what error a
$4\pi$ slip causes in an estimate of magnetite content from susceptibility.

---

**★7.** How magnetised is the core?

(a) Compute the geomagnetic dipole moment from a nominal equatorial surface field
of 30 000 nT and $R = 6.371\times10^{6}$ m.
(b) Compute the outer-core volume with $R_{\text{core}} = 3.48\times10^{6}$ m and
the implied mean magnetisation.
(c) Compute the implied mean field $B = \mu_0M$ inside the core and the ratio to
the surface field.
(d) Classify each input as measured, inferred or nominal, and state what the result
is therefore entitled to claim.

---

**★8.** Blocking and the thermal remanent magnetisation.

(a) For a cooling igneous body in a 25 °C/km geotherm, compute the depth interval
over which the temperature passes from 500 °C to 580 °C (the blocking range of
magnetite, nominal).
(b) Explain what is fixed during that interval and what therefore constitutes the
palaeomagnetic record.
(c) Explain why a rapidly cooled lava and a slowly cooled pluton record the field
with different fidelity, in terms of the blocking interval and the field's
stability.
(d) State the observational evidence that the remanence direction is *not* the
present field direction in some rocks, and why that fact is the foundation of
palaeomagnetism.

---

## ★★★ Research-oriented

**★9.** Demagnetisation and the non-uniqueness of magnetic inversion.

(a) For a uniformly magnetised ellipsoid, derive that $N_x+N_y+N_z = 1$ (state the
physical argument rather than a full tensor calculation), and give $N$ for a sphere
and for a very flat disc.
(b) Show that the external field of a uniformly magnetised body depends on the
*product* of shape and susceptibility through $\chi_{\text{eff}}$, and hence that
the anomaly alone cannot separate them.
(c) For a sphere of $\chi = 1$ and a thin sheet of the same volume and $\chi = 1$,
compute both $\chi_{\text{eff}}$ values and the ratio of their anomalies at the same
distance.
(d) Explain how this ambiguity is resolved in practice (independent constraints),
and why the resolution requires information the magnetic data do not contain.

---

**★10.** Anisotropy of magnetic susceptibility.

(a) Write the tensor relation $M_i = \chi_{ij}H_j$ and explain why $\chi_{ij}$ is
symmetric for a reversible (induced) magnetisation.
(b) Diagonalise the tensor, define the three principal susceptibilities
$k_1\ge k_2\ge k_3$, the anisotropy degree $P = k_1/k_3$ and the shape parameter

$$U = \frac{2k_2-k_1-k_3}{k_1-k_3} ,$$

and check that $U$ is dimensionless and bounded in $[-1,1]$.
(c) For $k_1 = 1.20\times10^{-3}$, $k_2 = 1.15\times10^{-3}$ and
$k_3 = 1.00\times10^{-3}$, compute the mean susceptibility, $P$ and $U$, and
classify the fabric.
(d) Explain why anisotropy of susceptibility is a *petrofabric* measurement, and
state the two rock-magnetic mechanisms (preferred orientation of grains, and
magnetocrystalline or shape anisotropy of individual grains) that produce it.
