# Exercises — 02-09-06 Dosimetry, Radiation Safety and Regulatory Limits

Attempt these **closed-book** before opening the
[solutions](./06-dosimetry-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/dosimetry_demo.py`](../code/dosimetry_demo.py)
require you to run it and report its actual output.

**Two rules apply to every answer in this set.**

1. No **dose limit** may be quoted from memory or from these exercises. Where a
   limit appears, it must enter as a symbol and be sourced from the current IAEA
   or ICRP publication and the national regulation in force on the day of use.
2. Every **conversion coefficient** (fluence-to-dose, weighting factor, dose
   coefficient per unit intake) is a recommendation published by a committee. Say
   where it came from, or present the answer as a function of it.

Tabulated values to use (state them): $T_{1/2}(\mathrm{Cs\text{-}137}) = 30.08$ a,
$M = 136.907$ g mol⁻¹; $1\ \mathrm{Ci} = 3.7 \times 10^{10}$ Bq exactly;
$\ln 2 = 0.693\,147$; $N_A = 6.022\,140\,76 \times 10^{23}$ mol⁻¹.

---

## ★ Foundational

**★1.** (a) Compute the number of atoms in a 1.000 GBq caesium-137 source.
(b) Compute the mass of nuclide, in mg.
(c) Express the activity in curie.
(d) State why the *mass* column of a source inventory is the one that says least
about the hazard.

---

**★2.** A point source of 500 MBq emits 0.85 photons of 662 keV per decay.

(a) Compute the photon fluence rate at 2.00 m, in photons cm⁻² s⁻¹.
(b) Compute it at 4.00 m.
(c) State the factor by which the dose rate changes between (a) and (b) and name
the rule.
(d) State what replaces the $1/r^2$ law for a contaminated floor.

---

**★3.** (a) Compute the half-value layer for $\mu = 1.25$ cm⁻¹.
(b) Compute the tenth-value layer.
(c) Compute the thickness required for a factor of 1000 attenuation.
(d) State whether your answer is a lower or an upper bound on a real design, and
why.

---

## ★★ Applied

**★★4.** A 1.000 GBq source with $y = 0.85$ at $r = 1.00$ m, with a declared
fluence-to-dose coefficient of 4.0 pSv cm² per photon.

(a) Compute the fluence rate in photons m⁻² s⁻¹.
(b) Convert the coefficient to Sv m² per photon and compute the dose rate in
µSv s⁻¹ and in mSv h⁻¹.
(c) Compute the dose rate if the coefficient were 25 per cent larger.
(d) Compute the occupancy time that gives an effective dose equal to a limit $L$
at 1.00 m and at 1.50 m, leaving $L$ symbolic, and evaluate both for
$L = 1.0$ mSv a⁻¹. State what must be cited for $L$ and what must be cited for
the coefficient.

---

**★★5.** Counting statistics. A background is counted for 3600 s at 2.00 s⁻¹; a
sample is counted for 600 s in the same geometry. Detection efficiency 0.05 and
gamma yield 0.85.

(a) Compute $\sigma_\mathrm{net}$.
(b) Compute the minimum detectable activity at three standard deviations.
(c) Compute it for a 3600 s sample count as well.
(d) State the detection limit's floor as $t_s \to \infty$ and say what physical
quantity sets it.

---

**★★6.** Beta shielding. A strontium-90 source has a maximum beta energy near
2.28 MeV, and the radiative yield per beta is approximated by
$ZE_{\max}/3000$.

(a) Compute the yield in aluminium ($Z = 13$) and in lead ($Z = 82$).
(b) Compute the ratio between them.
(c) Explain, in two sentences, why a lead-only shield makes the situation worse
rather than better.
(d) State one assumption of the estimate that fails in a real source.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/dosimetry_demo.py`](../code/dosimetry_demo.py) and
report:

(a) the mass of caesium-137 in a 1 GBq source and the number of atoms;
(b) the fluence rate at 0.3, 1.0 and 4.0 m;
(c) the HVL, tenth-value layer and 100× thickness for each of the four materials;
(d) the required 100× thickness for lead when $\mu$ is 20 per cent larger, and
the percentage change;
(e) the dose rate computed for 1 GBq at 1 m with the declared coefficient, and
the values for coefficient multipliers of 0.5 and 2.0;
(f) the MDA at $t_s = 60$, 3600 and 36 000 s, and the floor;
(g) the occupancy times at 1 m for $L = 1.0$, 5.0 and 20.0 mSv a⁻¹;
(h) state explicitly which of these numbers are computed, which are model inputs
and which are the regulatory limits that the script deliberately leaves symbolic.

---

**★★★8.** Presenting an assessment.

(a) Write the two-line calculation that gives the occupancy time for a limit
$L$, and name every input and its source category.
(b) A colleague writes "the dose is 0.097 mSv/h, well within the limit". List
three reasons the sentence is incomplete.
(c) A uranium-bearing core shed reads a normal external gamma field. Explain why
that is not evidence that the shed is safe, and name the measurement that should
be made.
(d) State the units and the conversion factors you would need to move from an
inhalation intake in becquerel to a committed effective dose in sievert, and
where each comes from.
