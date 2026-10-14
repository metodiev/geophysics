# Exercises — 02-09-03 Interaction of Radiation with Matter

Attempt these **closed-book** before opening the
[solutions](./03-radiation-interaction-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/radiation_interaction_demo.py`](../code/radiation_interaction_demo.py)
require you to run it and report its actual output. **Every problem that uses an
attenuation coefficient must say whether it is computed from the Compton cross
section or taken from a compilation.** The distinction is the point of the
lesson.

Useful constants: $m_ec^2 = 0.510\,998\,95$ MeV;
$h/m_ec = 2.426$ pm; $1\ \mathrm{barn} = 10^{-24}$ cm²;
$r_e = 2.817\,940\,3 \times 10^{-15}$ m; $N_A = 6.022\,140\,76 \times 10^{23}$
mol⁻¹.

---

## ★ Foundational

**★1.** A narrow beam of 662 keV photons meets a lead absorber with
$\mu = 1.25$ cm⁻¹ (an illustrative value at that energy).

(a) Compute the half-value layer.
(b) Compute the tenth-value layer.
(c) Compute the thickness for a factor of 100 attenuation.
(d) Compute the fraction transmitted through 2.0 cm, and state what the
exponential law neglects.

---

**★2.** Compton kinematics at $E = 1.3325$ MeV (a cobalt-60 line).

(a) Compute $\alpha = E/m_ec^2$.
(b) Compute the backscatter energy $E'$ at $\theta = 180^\circ$.
(c) Compute the deposited energy at that angle, which is the Compton edge.
(d) Compute the scattered energy at $90^\circ$ and state why the Compton edge is
the same as the maximum deposited energy.

---

**★3.** At 662 keV the Klein–Nishina total cross section is 0.25614 barn.

(a) Compute the Compton-only mass attenuation coefficient of water, given
$Z/A = 0.5551$.
(b) Compute the linear attenuation coefficient of water at $\rho = 0.998$
g cm⁻³.
(c) Compute the half-value layer and compare it with the value in the demo's
table of illustrative coefficients.
(d) State why the *measured* total for water at this energy is close to your
answer, and why the measured total for lead is not.

---

## ★★ Applied

**★★4.** Photoelectric scaling.

(a) Compute $\sigma_\mathrm{pe}$(Pb)/$\sigma_\mathrm{pe}$(Fe) at the same energy
for $n = 4$ and $n = 4.5$.
(b) Compute the factor by which $\sigma_\mathrm{pe}$ falls for the same material
between 30 keV and 90 keV.
(c) Explain why an X-ray image of a bone (calcium, $Z = 20$) against soft tissue
(mostly water) has good contrast at 30 keV and poor contrast at 300 keV.
(d) State the two limitations of using these scalings for an absolute
cross section.

---

**★★5.** Alpha particles.

(a) Compute the mass range in g cm⁻² of a 5.486 MeV alpha, given a computed
range of 3.6688 cm in air at 1.205 × 10⁻³ g cm⁻³.
(b) Convert it to a geometric range in rock of density 2.65 g cm⁻³, in µm.
(c) The same computation at 2.743 MeV gives a range smaller by a factor of 3.10.
Compute that range in air, in cm.
(d) Explain why the ratio in (c) is not 2, and what that implies for an alpha
spectrum measured with a thin source.

---

**★★6.** Beta energy deposition.

(a) From the demo's table, take the mean-to-end-point ratio for $Q = 0.156$ MeV
and for $Q = 2.280$ MeV.
(b) Compute the mean energy deposited per decay for each.
(c) Compute the total energy deposited by 10⁶ decays of each, in joules.
(d) State why a beta emitter's "energy" quoted as a single number is always the
end point, and what fraction of the decays carry the top 1 per cent of the
energy range.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/radiation_interaction_demo.py`](../code/radiation_interaction_demo.py)
and report:

(a) the largest and smallest relative differences between the quadrature and the
closed form for the Klein–Nishina total cross section, with the energies;
(b) the computed Thomson limit, the tabulated value and their relative
difference;
(c) the Compton-only $\mu$ for lead at 662 keV and the HVL that follows;
(d) the ratio of the computed alpha range to the commonly tabulated 4 cm, and
the stated reason for the difference;
(e) the range ratio between 5.486 and 2.743 MeV;
(f) two sentences identifying which outputs are exact computations and which are
model results with a stated cutoff.

---

**★★★8.** A lead shield for a 662 keV source.

(a) Using the demo's Compton-only $\mu$ for lead, compute the thickness required
for a factor of 1000 attenuation.
(b) A photon cross-section compilation gives a total $\mu/\rho$ of order
0.1 cm² g⁻¹ at that energy. Convert to $\mu$ and recompute the thickness.
(c) State the ratio between your answers and which one is a lower bound on a real
design.
(d) Explain, in two sentences, why the omission is a *systematic* underestimate
for lead and not a random error.
