# Exercises — 02-04-03 Constitutive Laws and Generalised Hooke's Law

Attempt these **closed-book** before opening the
[solutions](./03-constitutive-laws-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/constitutive_laws_demo.py`](../code/constitutive_laws_demo.py) require
you to run it and report its actual output.

---

## ★ Foundational

**★1.** With $\lambda = 20$ GPa and $\mu = 25$ GPa:

(a) Write the full $6\times6$ Voigt stiffness matrix.
(b) Compute $K$ and $M$.
(c) Compute the strain energy density for
$\varepsilon_{11} = 10^{-3}$, all other components zero.
(d) Compute the strain energy density for a pure shear
$\varepsilon_{12} = \varepsilon_{21} = 10^{-3}$ and verify the ratio to (c).

---

**★2.** For the same material, a strain state has
$\varepsilon_{11} = 2\times10^{-3}$, $\varepsilon_{22} = -1\times10^{-3}$,
$\varepsilon_{33} = -1\times10^{-3}$, all shear components zero.

(a) Compute $\sigma_{11}$, $\sigma_{22}$, $\sigma_{33}$ using equation (3) of the
lesson.
(b) Compute the mean stress and the deviatoric stress tensor.
(c) Verify that the deviatoric stress is proportional to the deviatoric strain
with constant $2\mu$.
(d) State why the proportionality constant is $2\mu$ rather than $\mu$.

---

**★3.** Show that a symmetric $6\times6$ matrix has 21 independent components.

(a) Count the components of a general fourth-rank tensor with the two minor
symmetries.
(b) Show that major symmetry reduces $36$ to $21$.
(c) State which physical principle provides major symmetry.
(d) State the number of independent constants for cubic and hexagonal symmetry and
name one mineral of each.

---

**★4.** A strain vector in Voigt notation is
$(1, 0, 0, 1, 0, 0)\times10^{-3}$ (engineering shear convention).

(a) Write the corresponding fourth-rank strain tensor.
(b) Compute the stress six-vector.
(c) Recompute the strain vector using the *tensor* convention
($\varepsilon_{23}$ instead of $2\varepsilon_{23}$) and report what changes in the
resulting stress.
(d) State how you would detect this error in a numerical implementation.

---

## ★★ Applied

**★★5.** Run the demo and use its printed values.

(a) Report both symmetry residuals.
(b) Report the strain energy from both routes and the difference.
(c) Report the compliance's first entry and the value of $1/E$.
(d) Report the round-trip error and state what it certifies.

---

**★★6.** A laboratory measures the following elastic constants on a sandstone:
$v_p = 3200$ m s⁻¹, $v_s = 1900$ m s⁻¹, $\rho = 2350\ \mathrm{kg\,m^{-3}}$.

(a) Compute $\mu$ and $M$, then $\lambda$ and $K$.
(b) Verify that $K = \lambda+2\mu/3$ and that $M = K+4\mu/3$.
(c) Compute the isotropy test $C_{11}-C_{12}-2C_{44}$ in GPa.
(d) Explain why the test cannot be applied to this measurement set at all.

---

**★★7.** A rock core is tested twice: once drained (slow, pore pressure
equilibrated) and once undrained (fast, ultrasonic).

(a) Explain which moduli each test determines.
(b) For a sandstone with a dry bulk modulus of 12 GPa, a mineral modulus of
36 GPa, a fluid modulus of 2.2 GPa and porosity 0.15, compute the saturated bulk
modulus from the Gassmann relation quoted in lesson 02-04-04 or derive it if you
prefer, and report the difference from the dry value.
(c) Compute the two P-wave velocities assuming $\mu = 9$ GPa,
$\rho_{\text{dry}} = 2100$ and $\rho_{\text{sat}} = 2250\ \mathrm{kg\,m^{-3}}$.
(d) State how a laboratory could distinguish the two regimes experimentally.

---

**★★8.** Three averaging bounds for a two-component composite with bulk moduli
$K_1 = 10$ GPa, $K_2 = 40$ GPa and volume fractions 50/50.

(a) Compute the Voigt (arithmetic) bound.
(b) Compute the Reuss (harmonic) bound.
(c) State the Hashin–Shtrikman bounds qualitatively (no need to derive them) and
explain why they are tighter.
(d) Explain the physical geometry that attains each of the Voigt and Reuss bounds.

---

## ★★★ Research-oriented

**★★★9.** A general anisotropic compliance.

(a) Write the general $6\times6$ compliance for an orthorhombic material and
state how many independent constants it has.
(b) Show that for an orthorhombic material, a uniaxial stress applied along one
axis produces shear strains in the other two planes, but no shear in the plane of
symmetry.
(c) Derive the expression for $\varepsilon_{11}$ in terms of the stresses for the
orthorhombic case.
(d) Explain why Gassmann's fluid substitution is not simply a statement about
$K$ in an anisotropic rock, and what additional information is required.

---

**★★★10.** Adiabatic versus isothermal moduli.

(a) Using the thermodynamic identity for the difference between the adiabatic and
isothermal bulk moduli,
$K_S - K_T = K_T^2\alpha^2TV/C_V$ (or the equivalent form), compute the difference
for water: $K_T = 2.2$ GPa, $\alpha = 2.1\times10^{-4}$ K⁻¹ (at 25 °C),
$T = 298$ K, $\rho = 997\ \mathrm{kg\,m^{-3}}$, $C_p = 4182\ \mathrm{J\,kg^{-1}\,K^{-1}}$;
state any approximation you make in converting to $C_V$.
(b) Compare the result with the observed difference between the ultrasonic sound
speed in water and the value obtained from isothermal compressibility (ultrasonic
sound speed at 25 °C is about 1497 m s⁻¹; the isothermal compressibility implies
about 1478 m s⁻¹ — verify both numbers from the moduli and densities you use,
and state their sources).
(c) Compute the fractional difference and compare with your prediction in (a).
(d) State why the difference is negligible for most rocks but important for
fluids, and how this affects the interpretation of a saturated rock's moduli.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
