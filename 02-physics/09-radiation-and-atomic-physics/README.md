# Module 02-09 — Radiation, Atomic Physics and Radioactivity

**Stages:** intermediate → graduate · **Prerequisites:**
[02-07-01 Electrostatics, Coulomb's Law and Electric Potential](../07-electromagnetism/01-electrostatics.md)
for the Coulomb force that fixes every atomic energy in lesson 01,
[02-07-05 Electromagnetic Waves, Impedance and Polarisation](../07-electromagnetism/05-em-waves.md)
for the photon, [01-08-01 First-Order ODEs](../../01-mathematics/08-ordinary-differential-equations/01-first-order-odes.md)
for the decay law, and
[02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](../01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
for the counting statistics that decide what a radiometric measurement can
actually report.

Radioactivity is the one physical process in geophysics that has its own clock
built in, and radiometric methods are the only ones that can put an absolute
date or an absolute concentration on a rock without a calibration to a reference
sample. That power comes with a distinctive failure mode: the *physics* of the
decay law is exact and essentially untestable in the field, so when a
radiometric number is wrong it is almost always wrong in the **model attached to
it** — an assumed initial isotope ratio, an assumed secular equilibrium, an
assumed matrix, an assumed closure temperature, an assumed dose coefficient.

Three features distinguish this module from a general nuclear physics course:

- **The distinction between an age and a model age runs through everything.**
  Lesson 02 derives the isochron equation rather than quoting it, precisely so
  that the reader can see which quantity is fitted and which is assumed. The
  same distinction reappears as "equivalent uranium" in lesson 04 and as the
  assumed matrix in lesson 05.
- **Provenance of every constant is part of the constant.** Half-lives,
  branching ratios, decay constants, thermal-neutron cross sections, heat
  generation coefficients and dose coefficients are all *tabulated* quantities
  that differ between compilations. Lesson 02 requires the reader to state which
  compilation a half-life came from and by how much another differs; lesson 05
  requires the same for a cross section; lesson 06 goes further and states that
  no dose *limit* may be quoted from memory at all, because limits are
  jurisdiction-specific legal instruments.
- **What is computed and what is looked up is stated in every calculation.**
  The Klein–Nishina cross section, the decay law, the isochron equation, the
  collision kinematics and the Poisson statistics are computed. The
  photoelectric and pair-production cross sections, the total attenuation
  coefficients, every nuclear datum and every conversion coefficient are looked
  up. The demos label each output so that the two categories cannot be confused,
  and the exercise solutions label every attenuation coefficient as *computed*
  or *tabulated*.

The anchor geophysics, in the order it appears: **gamma-ray spectrometry** for K,
U and Th mapping; **borehole nuclear logging**, both natural-gamma and
neutron–density; **radiometric dating** and the closure-temperature concept;
**radiation interaction and shielding**; **dosimetry and regulatory limits**;
and **radiogenic heat production**, which is what connects a radiometric map to
geodynamics rather than only to mineral exploration.

## Learning objectives

By the end of this module you will be able to:

1. Derive the Bohr radius and the hydrogen energy levels from the Coulomb force
   and one quantisation rule, derive the Rydberg formula from them, and state
   precisely which parts of the model are correct and which are not.
2. Distinguish an atomic absorption edge from a characteristic X-ray transition
   energy, compute both with a screened one-electron model, and state the model's
   accuracy for light and heavy elements.
3. **Derive** the decay law from a constant probability of decay per unit time,
   and derive $\tau = T_{1/2}/\ln 2$ and the specific activity from it.
4. **Derive** the Bateman solution for a two-member chain and the secular
   equilibrium condition, and explain why one gamma line reports a whole series.
5. **Derive** the isochron equation from the decay law, invert a fitted slope
   into an age, and distinguish an age from a model age with its stated
   assumption.
6. Explain closure temperature, solve the Dodson equation, and say why two
   chronometers in one rock record two ages.
7. Compute a stopping power and a range from the Bethe formula, state the cutoff
   below which the formula is unphysical, and explain the Bragg peak.
8. **Derive** the Compton wavelength shift and the exponential attenuation law,
   and compute a half-value layer.
9. Explain the $Z$ and $E$ scaling of the photoelectric, Compton and pair
   production processes and decide which dominates for a given photon and
   material.
10. Explain energy resolution in terms of carrier statistics, identify every
    feature of a NaI gamma-ray spectrum, and invert the three-window stripping
    system.
11. Compute a depth of investigation from an attenuation coefficient, and a
    radiogenic heat production from K, U and Th concentrations.
12. Derive the average logarithmic energy decrement and the moderating ratio,
    compute a hydrogen index, and explain why a neutron log measures porosity.
13. Distinguish activity, absorbed dose, equivalent dose and effective dose, and
    present a dose assessment in which computed, model and sourced quantities are
    separately labelled.
14. Compute a detection limit and its floor from Poisson statistics, and state
    why it requires a counting time, a background and an efficiency.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Atomic Structure and Energy Levels](./01-atomic-structure.md) | intermediate | The Bohr ladder derived, the Rydberg formula checked against the measured spectrum, and the difference between a binding energy and a transition energy |
| 02 | [Radioactive Decay, Half-Life and Dating](./02-radioactive-decay.md) | intermediate | **The mastery lesson**: the decay law and the isochron equation derived, and the difference between an age and a model age quantified |
| 03 | [Interaction of Radiation with Matter (Alpha, Beta, Gamma)](./03-radiation-interaction.md) | advanced | Three particles, three coupling mechanisms, and an explicit boundary between what is computed and what is looked up |
| 04 | [Gamma-Ray Spectrometry and Natural Radioelements](./04-gamma-spectrometry.md) | advanced | Resolution, spectral landmarks, the three-window inversion, the depth of investigation and radiogenic heat production |
| 05 | [Neutron Interactions and Borehole Nuclear Measurements](./05-neutron-interaction.md) | graduate | Moderation, the moderating ratio, why a neutron log reads hydrogen and therefore porosity, and the density–neutron–Pe suite |
| 06 | [Dosimetry, Radiation Safety and Regulatory Limits](./06-dosimetry.md) | intermediate | The quantities and their units, fluence-to-dose, shielding, counting statistics, and a dose assessment with every limit symbolic |

## Suggested path

**If you are working through the physics folder in order:** lessons 01 to 06 in
numeric order. Lesson 02 is the one that is used most often downstream and must
be worked, not read. Lesson 06 can be read at any point, but do not skip §6 of
it — the counting-statistics material is what makes every radiometric
measurement quotable.

**If you are here for geochronology and isotope geology:** read
[01](./01-atomic-structure.md) §3 and §4 (edges and lines), then
[02](./02-radioactive-decay.md) in full, then
[06](./06-dosimetry.md) §6 (counting statistics and detection limits). Then
[04-03-03 Radiometric Dating Methods and Their Assumptions](../../04-earth-science-geology/03-geologic-time-and-stratigraphy/03-radiometric-dating.md).

**If you are here for mining, exploration or airborne surveying:** read
[02](./02-radioactive-decay.md) §2 and §3 (equilibrium and the isochron, which
is where the equilibrium assumption comes from), [03](./03-radiation-interaction.md)
§2.4 and §4 (the attenuation law and its limits), and
[04](./04-gamma-spectrometry.md) in full. Then
[11-02-05 Radiometrics and Alteration Mapping](../../11-exploration-geophysics/02-mineral-exploration/05-radiometrics-for-minerals.md).

**If you are here for borehole geophysics and petrophysics:** read
[03](./03-radiation-interaction.md) §2 and §4, [04](./04-gamma-spectrometry.md)
§1 to §3, and [05](./05-neutron-interaction.md) in full. Then
[05-08-04 Density, Neutron and Sonic Porosity Logs](../../05-core-geophysics/08-geophysical-logging/04-porosity-logs.md).

**If you are here for geodynamics and crustal thermal structure:** read
[02](./02-radioactive-decay.md) §2 and §7 (chain equilibrium and the
conversion factors) and [04](./04-gamma-spectrometry.md) §5 (radiogenic heat
production) with its cross-check. Then
[02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../05-thermodynamics/06-geotherms.md).

**If you are here for radiation safety or for field practice:** read
[03](./03-radiation-interaction.md) §1 and §4 (what stops what, and
bremsstrahlung), then [06](./06-dosimetry.md) in full. Then confirm every
regulatory number in the current IAEA and ICRP publications and in the national
regulation that applies to you.

**If you already have a nuclear physics background:** attempt ★★★7 of
[02](./02-radioactive-decay.md), ★★★7 and ★★★8 of
[03](./03-radiation-interaction.md) and ★★★7 of
[04](./04-gamma-spectrometry.md) first. If those close cleanly, use lessons 01
and 06 as reference.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-atomic-structure.md`](./01-atomic-structure.md) … [`06-dosimetry.md`](./06-dosimetry.md) | The six lessons |
| [`exercises/01-atomic-structure-exercises.md`](./exercises/01-atomic-structure-exercises.md) and [`-solutions.md`](./exercises/01-atomic-structure-solutions.md) | Energies, edges, Moseley's law |
| [`exercises/02-radioactive-decay-exercises.md`](./exercises/02-radioactive-decay-exercises.md) and [`-solutions.md`](./exercises/02-radioactive-decay-solutions.md) | **The mastery lesson's problem set**, including the isochron and the closure-temperature problems |
| [`exercises/03-radiation-interaction-exercises.md`](./exercises/03-radiation-interaction-exercises.md) and [`-solutions.md`](./exercises/03-radiation-interaction-solutions.md) | Attenuation, Compton kinematics, ranges, shielding |
| [`exercises/04-gamma-spectrometry-exercises.md`](./exercises/04-gamma-spectrometry-exercises.md) and [`-solutions.md`](./exercises/04-gamma-spectrometry-solutions.md) | Conversion factors, stripping, depth of investigation, heat production |
| [`exercises/05-neutron-interaction-exercises.md`](./exercises/05-neutron-interaction-exercises.md) and [`-solutions.md`](./exercises/05-neutron-interaction-solutions.md) | Moderation, moderating ratio, hydrogen index, Pe, chlorine |
| [`exercises/06-dosimetry-exercises.md`](./exercises/06-dosimetry-exercises.md) and [`-solutions.md`](./exercises/06-dosimetry-solutions.md) | Fluence, shielding, dose rate, counting statistics — with every limit symbolic |
| [`code/atomic_structure_demo.py`](./code/atomic_structure_demo.py) | Hydrogen spectrum versus tabulated wavelengths, K-edge screening constants, Moseley fit, barium Kα |
| [`code/radioactive_decay_demo.py`](./code/radioactive_decay_demo.py) | **The module's verification script**: Euler/RK4 against the closed-form decay law, half-life by bisection, specific activities, Bateman, isochron fit, radiocarbon, Dodson |
| [`code/radiation_interaction_demo.py`](./code/radiation_interaction_demo.py) | Klein–Nishina quadrature versus the closed form, Compton kinematics, attenuation, pair production, Bethe stopping power and range, beta spectrum |
| [`code/gamma_spectrometry_demo.py`](./code/gamma_spectrometry_demo.py) | Synthetic NaI spectrum, three-window stripping and its condition number, radiogenic heat production with a cross-check, depth of investigation |
| [`code/neutron_interaction_demo.py`](./code/neutron_interaction_demo.py) | Thermal conventions, moderation, macroscopic cross sections, moderating ratios, hydrogen index and the gas effect, chlorine share, Pe |
| [`code/dosimetry_demo.py`](./code/dosimetry_demo.py) | Activity and mass, fluence, shielding sensitivity, bremsstrahlung, Poisson statistics and detection limits, occupancy time with the limit symbolic |

Every script uses only the Python standard library, so they run in any Python 3
installation with no packages. Run them; do not read them.

## Mastery checkpoint

Complete this without notes, with a calculator and no code.

> A granite contains 3.5 % K, 4.0 ppm U and 15 ppm Th, and its density is
> 2650 kg m⁻³. **(a)** Compute its radiogenic heat production in µW m⁻³ from the
> tabulated coefficient form, and state which of the coefficients you used and
> where it came from. **(b)** Compute the percentage contribution of each of the
> three elements. **(c)** Compute the specific activity of 1 ppm of natural
> uranium in secular equilibrium, from the half-life and the abundance rather
> than from a table, and compare it with the figure of 12.4 Bq kg⁻¹ used in
> gamma-ray surveying; explain the difference. **(d)** A whole-rock Rb–Sr
> isochron for this granite gives a slope of $4.97 \times 10^{-3}$. Compute the
> age with $\lambda = 1.42 \times 10^{-11}$ a⁻¹ and state the compilation
> convention you are using. **(e)** A single sample from the same granite gives a
> model age 40 per cent younger. Give two entirely different reasons that could
> be true, and say which is testable with the isochron and which is not.

Parts (a) and (b) are lesson [04](./04-gamma-spectrometry.md) §5; part (c) is
lesson [02](./02-radioactive-decay.md) §7; parts (d) and (e) are lesson
[02](./02-radioactive-decay.md) §3 and §6.

**Worked answer for (a) and (c).**

$$A = \rho \times 10^{-5}\left(9.52\,C_\mathrm{U} + 2.56\,C_\mathrm{Th}
+ 3.48\,C_\mathrm{K}\right) = 2650 \times 10^{-5}(38.08 + 38.40 + 12.18)
= 2.35\ \mu\mathrm{W\,m^{-3}},$$

from the tabulated coefficient form of lesson 04 §5, with the coefficients
labelled as tabulated quantities that differ between compilations. The three
terms contribute 43.0 per cent (U), 43.3 per cent (Th) and 13.7 per cent (K).

For (c): $N = 0.992\,745 \times 10^{-6} \times 6.022\,140\,76 \times 10^{23}
\times 10^{3}/238.051 = 2.5116 \times 10^{18}$ atoms per kg, and
$\lambda = \ln 2/(4.468 \times 10^9 \times 3.155\,76 \times 10^7) =
4.915\,96 \times 10^{-18}$ s⁻¹, so $A = \mathbf{12.3472}$ Bq kg⁻¹. The
difference from 12.4 is 0.4 per cent and is entirely in the tabulated half-life
and abundance — which is why the conversion factor must be recomputed from the
compilation cited rather than copied.

## Common pitfalls across this module

1. **Quoting a half-life, a branching ratio, a cross section or a heat-generation
   coefficient without its compilation.** These are measured or evaluated
   quantities that differ between sources in their last digits. The difference is
   not academic: the Rb–Sr half-life changed by 2 per cent in 1977 and every age
   published before that changed with it.
2. **Quoting a dose limit from memory.** Limits are jurisdiction-specific legal
   instruments, revised periodically. Nothing in this module states one, and no
   calculation should embed one without a citation to the regulation in force and
   its date.
3. **Confusing an age with a model age.** If the initial isotopic ratio was
   assumed rather than fitted, the result is a model age and the assumption
   belongs in the sentence that states the number.
4. **Confusing an absorption edge with a characteristic line.** They differ by
   the L-shell binding energy and the error is 10 to 20 per cent for light
   elements.
5. **Using a Compton-only attenuation coefficient for a heavy element.** The
   photoelectric term is not negligible for lead at energies a geophysicist
   actually uses, and the error is a *systematic* underestimate of the
   attenuation.
6. **Treating an exponential attenuation law as exact in a broad geometry.** The
   build-up factor can exceed 2 for a thick shield.
7. **Assuming secular equilibrium.** Radon loss, uranium-series disequilibrium in
   young rocks and industrial processing all break it, and "equivalent uranium"
   is an activity converted through that assumption.
8. **Reading a neutron or density porosity as a true porosity.** Both are
   apparent quantities calibrated against a stated matrix and fluid; a shale, a
   gas, a heavy mineral or a saline fluid all shift them.
9. **Quoting a detection limit without a counting time, a background and an
   efficiency.** It is not a property of the instrument alone, and it has a floor
   set by the background counting time.
10. **Reporting more significant figures than the model supports.** A
    $^{14}$C age of "19 034.6 years" and a concentration quoted from a one-second
    count are both false precision.

## Related folders

- [02-physics/01 Measurement, Units and Physical Reasoning](../01-measurement-and-physical-reasoning/README.md)
  — the uncertainty discipline this module applies to counting statistics.
- [02-physics/05 Thermodynamics and Heat Transfer](../05-thermodynamics/README.md)
  — where the radiogenic heat production of lesson 04 becomes a geotherm.
- [02-physics/07 Electromagnetism and Electromagnetic Induction](../07-electromagnetism/README.md)
  — the Coulomb force and the photon.
- [04-earth-science-geology/03 Geologic Time and Stratigraphy](../../04-earth-science-geology/03-geologic-time-and-stratigraphy/README.md)
  — the geological use of the chronometers of lesson 02.
- [05-core-geophysics/08 Geophysical Logging](../../05-core-geophysics/08-geophysical-logging/README.md)
  — where lessons 04 and 05 become borehole measurements.
- [10-gpr-near-surface/05 Other Near-Surface Methods](../../10-gpr-near-surface/05-other-near-surface-methods/README.md)
  — radiometric and nuclear methods at the surface.
- [11-exploration-geophysics/02 Mineral Exploration](../../11-exploration-geophysics/02-mineral-exploration/README.md)
  — radiometrics for alteration mapping.
- [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)
  — radiogenic heat production in the global thermal budget.
- [26-reference-library/02 Constants and Units](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the exact/measured/nominal classification that this module applies to
  half-lives, cross sections and dose coefficients.
