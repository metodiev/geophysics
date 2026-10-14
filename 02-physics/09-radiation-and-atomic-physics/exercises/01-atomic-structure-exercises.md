# Exercises — 02-09-01 Atomic Structure and Energy Levels

Attempt these **closed-book** before opening the
[solutions](./01-atomic-structure-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/atomic_structure_demo.py`](../code/atomic_structure_demo.py) require
you to run it and report its actual output. Where a tabulated value is needed,
state the compilation you would look it up in — an answer that quotes a K-edge
energy without a source is incomplete.

---

## ★ Foundational

**★1.** (a) Compute the Bohr radius from
$a_0 = 4\pi\varepsilon_0\hbar^2/(m_ee^2)$ using $m_e = 9.109\,383\,7 \times
10^{-31}$ kg and the exact SI constants, and give the answer in pm.
(b) Compute the hydrogen ground-state energy from
$E_1 = -\tfrac12 m_ec^2\alpha^2$ with $\alpha = 1/137.036$ and state it in eV.
(c) Compute the photon wavelength that corresponds to a transition from
$n = 2$ to $n = 1$ in hydrogen using $hc = 1239.841984$ eV nm, and compare with
the tabulated Lyman-alpha wavelength of 121.567 nm, stating why they differ.
(d) State which of the three quantities in (a)–(c) is a measured constant and
which follow from exact ones.

---

**★2.** Hydrogen lines. Using $R_\mathrm{H} = 109\,677.58$ cm⁻¹ for hydrogen:

(a) Compute the vacuum wavelength of Hβ, the $n = 4 \to 2$ transition.
(b) Divide by a nominal air index of 1.000277 and compare with the tabulated
486.133 nm.
(c) Compute the **Balmer limit**, the wavelength of the series limit
$n \to \infty$ at $n_l = 2$.
(d) Compute the energy of an Hα photon in eV.

---

**★3.** Energy levels and shells. For a hydrogen-like ion with a single
electron:

(a) Compute the K-shell binding energy of an ion with $Z = 26$ in keV.
(b) Compute the energy of the Kα transition in the same ion.
(c) State in one sentence why the Kα energy must be less than the K-shell
binding energy, and what the difference is physically.
(d) The tabulated K-edge energy of iron is 7.112 keV. Compare it with your
answer to (a), state whether the real atom binds its 1s electron more or less
strongly than the bare Coulomb model predicts, and explain the sign of the
difference in terms of the other electrons.

---

## ★★ Applied

**★★4.** The isotope shift.

(a) Compute $R_\mathrm{H}$ and $R_\mathrm{D}$ from
$R_M = R_\infty/(1 + m_e/M)$ with $R_\infty = 109\,737.3157$ cm⁻¹, and give the
fractional shift.
(b) Compute the Hα wavelength for hydrogen and for deuterium in air, and the
shift in pm.
(c) Compute the same for tritium and state whether the H–D shift is larger or
smaller than the D–T shift, and why.
(d) A student says the shift is a relativistic effect. Correct the statement.

---

**★★5.** Moseley's law. Using the tabulated Kα₁ energies 6.4038 keV (Fe,
$Z = 26$), 8.0478 keV (Cu, $Z = 29$) and 74.9694 keV (Pb, $Z = 82$):

(a) Compute $\sqrt E$ for each.
(b) Compute the slope of $\sqrt E$ against $Z$ between Fe and Pb and compare
with the model's $\sqrt{\tfrac34 \times 13.6057\ \mathrm{eV}/1000}$.
(c) Compute the screening constant $\sigma$ implied by the Fe–Pb line, from
$\sigma = Z - \sqrt{E/13.6057\ \mathrm{eV}}$.
(d) State what Moseley's law demonstrated historically, and say what it does
*not* predict.

---

**★★6.** Edges and lines. A spectroscopist measures a K-edge at 7.112 keV in
an iron-bearing sample and infers a Kα line energy by treating the edge as the
transition energy.

(a) Compute the Kα energy that follows from the hydrogen-like model for
$Z = 26$ and compare with the tabulated 6.4038 keV.
(b) Compute the fractional error made by using the edge energy as the line
energy.
(c) State what the difference between the two measured energies is physically.
(d) Explain, using the difference in (c), why the error in (b) is larger for
light elements than for heavy ones.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/atomic_structure_demo.py`](../code/atomic_structure_demo.py)
and report:

(a) the model and tabulated wavelengths and the relative difference for Hδ;
(b) the fitted screening constant recovered from the six tabulated K-edge
energies, and the largest and smallest values in the table;
(c) the fitted Moseley slope and the model's slope, with the percentage
difference;
(d) the model's Kα transition energy for barium and the commonly tabulated
32.19 keV, with the percentage difference;
(e) a two-sentence statement of which of these model applications is usable for
interpolation and which is not.

---

**★★★8.** The screening constant is not constant.

(a) From the tabulated K-edge energies 7.112 keV (Fe, $Z = 26$) and 88.005 keV
(Pb, $Z = 82$), compute $\sigma$ for each.
(b) Compute the K-edge energy that the one-electron model with a single
constant $\sigma = 2$ would predict for both elements, and give both fractional
errors.
(c) Explain physically why $\sigma$ falls as $Z$ rises, in terms of where the
screening electrons sit relative to the K shell.
(d) A report states "the K edge of an element is at $13.6Z^2$ eV". Identify the
two things wrong with the statement.
