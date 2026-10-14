# Exercises — 04-06-02 Mineral Deposit Types and Their Geophysical Signatures

Attempt these **closed-book** before opening the
[solutions](./02-mineral-deposits-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/mineral_deposits_demo.py`](../code/mineral_deposits_demo.py) require you
to run it and report its actual output. **For every deposit discussed, state the
property contrast and the method; for every anomaly, state the geometry assumed.
No grade, tonnage or contained-metal figure may be quoted.**

Values to use: $\mu_0 = 4\pi\times10^{-7}$ H m⁻¹;
$G = 6.674\times10^{-11}$ m³ kg⁻¹ s⁻²; $1$ mGal $= 10^{-5}$ m s⁻².

---

## ★ Foundational

**★1.** A magnetite-rich body is modelled as a sphere of radius $a = 150$ m with
its centre at $z = 300$ m depth, in an inducing field of $B = 52\,000$ nT and with
a bulk susceptibility of $k = 0.05$ SI.

(a) Compute the inducing field strength $H = B/\mu_0$ in A m⁻¹.
(b) Compute the induced dipole moment $m = kH(4/3)\pi a^{3}$.
(c) Compute the peak vertical-field anomaly above the centre, in nT.
(d) Compute the position of the anomaly zero crossing and state whether it
depends on $k$ or on $a$.

---

**★2.** Using the same geometry, compute the gravity anomaly for a density
contrast of 800 kg m⁻³.

(a) Compute the anomaly at the surface above the centre, in mGal.
(b) Recompute it if the body were at 600 m instead of 300 m.
(c) State the ratio of (a) to (b) and the power of $z$ involved.
(d) State why an exploration programme cannot compensate for depth by using a
more sensitive instrument alone.

---

**★3.** A massive sulphide body has $\rho = 4000$ kg m⁻³ and
$v_P = 5800$ m s⁻¹; the host volcanic rock has $\rho = 2700$ kg m⁻³ and
$v_P = 5400$ m s⁻¹.

(a) Compute both acoustic impedances.
(b) Compute the normal-incidence reflection coefficient.
(c) Compute the energy reflection coefficient as a percentage.
(d) State whether the reflection is a peak or a trough on a normal-polarity
section, and why.

---

## ★★ Applied

**★★4.** A rock has a host conductivity of $10^{-3}$ S m⁻¹ and contains
sulphide of conductivity $10^{3}$ S m⁻¹.

(a) Compute the Hashin–Shtrikman lower and upper bounds for a sulphide volume
fraction of 0.05.
(b) Recompute for 0.30.
(c) Convert each bound to a resistivity in Ω m.
(d) State why the two bounds differ by orders of magnitude and which bound a real
disseminated deposit approaches.

---

**★★5.** A placer sand has a porosity of 0.35 and is saturated. Its framework is
quartz ($\rho = 2650$ kg m⁻³) with a heavy-mineral fraction $f$ of ilmenite
($\rho = 4600$ kg m⁻³); pore water is 1000 kg m⁻³.

(a) Compute the bulk density for $f = 0$ and for $f = 0.10$.
(b) Compute the density contrast between them.
(c) Compute the Bouguer-slab gravity anomaly of a 10 m thick layer with that
contrast.
(d) State which other physical property the ilmenite changes, and therefore which
second method would be used.

---

**★★6.** A magnetic anomaly has its half-maximum at 200 m from its centre, and
its shape is consistent with a sphere.

(a) Use the half-width rule $z = 1.997\,x_{1/2}$ to compute the depth to the
centre.
(b) Compute the position of the zero crossing for that depth.
(c) State the range of depths over which the dipole approximation used by the rule
is acceptable.
(d) Explain why the depth estimate does not require the magnetisation to be known.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/mineral_deposits_demo.py`](../code/mineral_deposits_demo.py)
and report:

(a) the dipole moment, the peak anomaly and the zero crossing for the reference
sphere;
(b) the half-width parameter $u$ and the resulting depth rule, and the check that
it recovers the input depth;
(c) the gravity anomaly for the four density contrasts;
(d) the gravity and magnetic anomalies at 300, 500, 1000 and 2000 m;
(e) the impedances and reflection coefficients for the four ore types;
(f) the Hashin–Shtrikman bounds at the five sulphide fractions;
(g) the placer densities, density contrasts and slab anomalies.

(h) In three sentences, say which outputs are exact consequences of the stated
formulas, which are variational bounds, and which are nominal literature values
entering as inputs.

---

**★★★8.** Interpretation and its limits.

(a) A porphyry system is surveyed with magnetics, radiometrics and IP. Describe
the expected *pattern* of the three responses across the potassic core, the
phyllic shell and the propylitic outer zone, and state which single anomaly would
be most misleading if interpreted alone.
(b) A massive sulphide body is 20 m thick and 100 m across at 150 m depth. Explain
which of EM, gravity and seismic is most likely to detect it, and why the other
two may fail — quantify where you can.
(c) An aeromagnetic survey identifies a strong dipole anomaly with a *reversed*
apparent polarity. Give two explanations and state the observation that would
discriminate.
(d) A laterite profile is mapped with gravity and resistivity. Explain the sign of
each anomaly with depth and state which part of the profile is the exploration
target for nickel.
