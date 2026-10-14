# Exercises — 04-01-03 Rock-Forming Minerals and Their Physical Properties

Attempt these **closed-book** before opening the
[solutions](./03-mineralogy-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/mineralogy_demo.py`](../code/mineralogy_demo.py) require you to run it
and report its actual output. Use $N_A = 6.02214076\times10^{23}$ mol⁻¹ and
1 Å³ = $10^{-24}$ cm³.

---

## ★ Foundational

**★1.** A mineral has $Z = 4$ formula units per cell, a triclinic cell volume of
664.5 Å³ and a formula mass of 262.223 g/mol.

(a) Compute its density in g/cm³.
(b) Compare with the measured density of albite, 2.62 g/cm³.
(c) State what the calculation verifies and what it does not.

---

**★2.** A mineral has $v_p = 7.20$ km/s, $v_s = 3.90$ km/s and
$\rho = 2750$ kg/m³.

(a) Compute $G = \rho v_s^2$ in GPa.
(b) Compute $K = \rho(v_p^2 - \frac43v_s^2)$ in GPa.
(c) Compute Poisson's ratio $\nu = (3K-2G)/(2(3K+G))$.
(d) State whether the value is typical for a silicate.

---

**★3.** Mean atomic number.

(a) Compute $\bar Z$ for anorthite, $\mathrm{CaAl_2Si_2O_8}$, with atomic
numbers Ca 20, Al 13, Si 14, O 8.
(b) Compute $\bar Z$ for dolomite, $\mathrm{CaMg(CO_3)_2}$, with Mg 12 and C 6.
(c) State which of anorthite, dolomite, calcite ($\bar Z = 10$) and quartz
($\bar Z = 10$) a photoelectric log separates least well.

---

## ★★ Applied

**★★4.** A measured velocity pair is uncertain.

Take $v_p = 8.10$ km/s, $v_s = 4.70$ km/s and $\rho = 5010$ kg/m³ (pyrite).

(a) Compute $K$ and $G$ in GPa.
(b) Recompute $K$ with $v_s$ increased by 5 per cent and everything else
unchanged.
(c) Report the percentage change in $K$ and explain why it is larger than 5 per
cent.

---

**★★5.** Porosity.

A sandstone has a dry bulk density of 2.35 g/cm³ and a grain density of
2.68 g/cm³.

(a) Compute its porosity as a fraction and as a percentage.
(b) Compute its bulk density when the pores are saturated with water.
(c) Compute its bulk density when the pores are saturated with gas
($\rho = 0.10$ g/cm³).
(d) State which contrast a gravity survey would see if the reservoir were
depleted.

---

**★★6.** Two minerals are indistinguishable on one log.

(a) Compute the density contrast between quartz (2.65) and calcite (2.71)
g/cm³ as a percentage.
(b) Compute the density contrast between quartz and forsterite (3.22) g/cm³.
(c) State which of the three pairs a photoelectric log can separate and which it
cannot, with the mean atomic numbers.
(d) Name one field situation in which the ambiguity of (c) would matter.

---

## ★★★ Research-oriented

**★★★7.** Error propagation in a density calculation.

Take forsterite: $M = 140.693$ g/mol, $V = 290.30$ Å³, measured
$\rho = 3.22$ g/cm³.

(a) Compute the density with $Z = 4$.
(b) Compute it with $Z = 3$ and with $Z = 5$.
(c) Report the percentage errors and state what a 25 per cent error in a
computed density would tell you about the structural input.
(d) Now recompute (a) with $V$ increased by 2 per cent, which is the effect of a
few GPa of compression, and state whether a laboratory cell volume can be used
for a mineral at 100 km depth.

---

**★★★8.** Run [`../code/mineralogy_demo.py`](../code/mineralogy_demo.py) and
report:

(a) the computed and measured densities of all six minerals and the percentage
differences;
(b) the $G$, $K$, $E$ and $\nu$ values for quartz and for calcite, and the
contrast that produces their different seismic responses;
(c) the mean atomic numbers of all six minerals and the three that share the
value 10.00;
(d) the electron densities and their range;
(e) the bulk density at $\phi = 0.30$ for a dry and a water-saturated quartz
framework;
(f) two sentences on which output values are computed and which are tabulated.

---

**★★★9.** Design a discrimination. You have a rock that is either a pure
quartz sandstone or a pure limestone, both with the same porosity.

(a) State what each measurement below would return and whether it separates
them: bulk density; P velocity; $v_p/v_s$; photoelectric mean atomic number.
(b) Rank the four by how well they separate the two.
(c) Propose a two-measurement combination that separates them with the greatest
margin, and state the physical reason each measurement was chosen.
