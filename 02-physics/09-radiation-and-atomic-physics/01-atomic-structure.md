---
id: 02-09-01
title: "Atomic Structure and Energy Levels"
level: intermediate
prereqs: ["02-07-01", "02-03-01", "01-05-04"]
estimated_minutes: 90
tags: [atomic-physics, energy-levels, x-rays, spectroscopy, gamma-rays]
---

# Atomic Structure and Energy Levels

Almost every gamma ray that a geophysicist measures arrives with a companion
that no one planned for: the X-rays of the daughter atom. A caesium-137 source
emits a 661.7 keV gamma from the barium nucleus, and the barium atom that is
left behind relaxes its electrons by emitting K X-rays near 32 keV. A
high-purity germanium detector records both, and the low-energy end of the
spectrum is therefore a directory of atomic structure rather than of nuclear
structure. Reading it correctly requires knowing where atomic energies come
from.

There is a second reason this material belongs in a geophysics curriculum. The
same binding energies that produce the X-rays also produce the **absorption
edges** of an absorber. Lead stops a 60 keV photon about ten times more
effectively than it stops an 88 keV one, and the abruptness of that change is a
property of the lead atom, not of the nucleus. Shielding, X-ray fluorescence,
photoelectric logging and the photoelectric factor of a formation all sit on
the same atomic physics.

This lesson builds the energy-level structure from the Coulomb force and the
quantisation of angular momentum, derives the Rydberg formula that the resulting
model produces, checks it against the measured hydrogen spectrum to one part in
ten thousand, and then does the same thing for the inner shells of heavy atoms —
where the model is deliberately much worse, and where understanding *why* it is
worse is the point.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Bohr radius and the hydrogen energy levels from the Coulomb
   force, the centripetal condition and the quantisation of angular momentum,
   and state which of the three is not classical.
2. **Compute** the energy of any hydrogen-like level from
   $E_n = -13.6\,\mathrm{eV}\,Z_\mathrm{eff}^2/n^2$, and say what
   $Z_\mathrm{eff}$ replaces and why.
3. **Derive** the Rydberg formula from the energy-level expression and use it
   to predict the wavelengths of the Lyman, Balmer and Paschen series.
4. **Explain** the reduced-mass correction and compute the hydrogen–deuterium
   isotope shift, and state why the tabulated wavelengths of lines below 200 nm
   are quoted in vacuum while longer ones are quoted in air.
5. **Distinguish** a binding energy (an absorption edge) from a transition
   energy (a characteristic line), and show that the latter must be the
   smaller.
6. **Compute** the characteristic X-ray energy of a given element with the
   screened one-electron model, state its accuracy, and explain why the residual
   is largest for light elements.
7. **Apply** Moseley's law, state what it is linear in and why, and say what it
   demonstrated historically.
8. **Identify** which features of a measured gamma-ray spectrum come from the
   nucleus and which from the atom.

## Prerequisites

- [02-07-01 Electrostatics, Coulomb's Law and Electric Potential](../07-electromagnetism/01-electrostatics.md)
  — the $1/r^2$ force and the potential energy it implies. Everything in §1 is
  this force plus a quantisation rule.
- [02-03-01 Simple Harmonic Motion and Small-Oscillation Approximation](../03-oscillations-and-waves/01-simple-harmonic-motion.md)
  — the language of restoring forces and bound states, and what "an energy
  level" means for a system that cannot escape.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../../01-mathematics/05-single-variable-calculus/04-taylor-series.md)
  — used in §6 to expand the screened-energy expression and in §4 for the
  reduced-mass expansion.

## 1. The Bohr model, derived

Take the simplest bound system in physics: one electron of charge $-e$ and mass
$m_e$ in the field of a nucleus of charge $+Ze$. Two classical statements and
one quantum statement are enough to fix the whole spectrum.

**Statement 1 (force balance).** For a circular orbit of radius $r$ and speed
$v$, the Coulomb attraction provides the centripetal force:

$$\frac{m_e v^2}{r} = \frac{1}{4\pi\varepsilon_0}\frac{Ze^2}{r^2} . \tag{1}$$

**Statement 2 (energy).** The total energy is kinetic plus potential,

$$E = \tfrac12 m_e v^2 - \frac{1}{4\pi\varepsilon_0}\frac{Ze^2}{r}
= -\tfrac12 m_e v^2 = -\frac{1}{4\pi\varepsilon_0}\frac{Ze^2}{2r} , \tag{2}$$

where the two equalities use (1). Note the result before going further: the
total energy is negative, it is half the potential energy, and it is minus the
kinetic energy. This is a general property of a $1/r$ potential and it is why
every bound Coulomb system has $E = -T$.

**Statement 3 (quantisation).** Bohr's postulate is that the angular momentum
comes in units of $\hbar = h/2\pi$:

$$m_e v r = n\hbar, \qquad n = 1, 2, 3, \dots \tag{3}$$

This is the only non-classical ingredient, and it is the one that a classical
calculation cannot supply. It is also, strictly speaking, wrong — the modern
statement is that $L^2 = \hbar^2\ell(\ell+1)$ with $\ell$ an integer and that
the *radial* motion is a standing wave — but for the hydrogen energy levels it
reproduces the correct answer.

Eliminate $v$ between (1) and (3). From (3), $v = n\hbar/(m_e r)$; substituting
into (1) gives

$$\frac{m_e}{r}\left(\frac{n\hbar}{m_e r}\right)^2
= \frac{1}{4\pi\varepsilon_0}\frac{Ze^2}{r^2}
\ \Longrightarrow\
r_n = \frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}\frac{n^2}{Z}
\equiv a_0\frac{n^2}{Z} . \tag{4}$$

The length $a_0 = 4\pi\varepsilon_0\hbar^2/(m_e e^2) = 5.291\,772\,109 \times
10^{-11}$ m is the **Bohr radius**, evaluated here from measured CODATA
constants for $m_e$ and the exact SI constants $h$, $e$, $\varepsilon_0$. It is
an **atomic unit of length**: the size of a hydrogen atom, and the scale that
every cross section in this module is built on.

Substituting (4) into (2) gives the energies:

$$E_n = -\frac{1}{2}\frac{m_e e^4}{(4\pi\varepsilon_0)^2\hbar^2}\frac{Z^2}{n^2}
= -\frac{E_h}{2}\frac{Z^2}{n^2}, \tag{5}$$

with $E_h = m_e e^4/((4\pi\varepsilon_0)^2\hbar^2) = 27.2114$ eV the **hartree**.
The physical constants group into a single energy, and only the integers remain
in the spectrum. Writing $R_\infty = E_h/(2hc)$ turns (5) into the Rydberg
form

$$E_n = -\frac{R_\infty h c\, Z^2}{n^2} . \tag{6}$$

## 2. The Rydberg formula and the measured hydrogen spectrum

A transition from level $n_u$ to a lower level $n_l$ emits a photon of energy
$hc/\lambda = E_{n_u} - E_{n_l}$, so from (6)

$$\frac{1}{\lambda} = R_\infty Z^2\left(\frac{1}{n_l^2}
- \frac{1}{n_u^2}\right). \tag{7}$$

This is the **Rydberg formula**. It is the whole observable content of the
model: one constant and integer arithmetic. Everything else in atomic
spectroscopy is a correction to it.

Two corrections matter immediately, and they are of different kinds.

**The finite nuclear mass.** The derivation above treated the nucleus as fixed.
In reality electron and nucleus orbit their common centre of mass, which
replaces $m_e$ by the reduced mass $\mu = m_e M/(m_e + M)$ and therefore
$R_\infty$ by

$$R_M = \frac{R_\infty}{1 + m_e/M} . \tag{8}$$

For hydrogen, $m_e/M_p = 1/1836$ and $R_\mathrm{H} = 109\,677.58$ cm⁻¹ against
$R_\infty = 109\,737.32$ cm⁻¹ — a fractional shift of $2.7 \times 10^{-4}$.
For deuterium the shift is half as large. The difference between the two is
observable: it is the **isotope shift**, and it is why hydrogen and deuterium
have measurably different line wavelengths even though they have identical
electronic structure.

**The medium.** A wavelength quoted "in air" is shorter than the vacuum value by
a factor $1/n_\mathrm{air} \approx 1 - 2.8 \times 10^{-4}$. Below about 200 nm
air is opaque and conventionally has no quoted index, so ultraviolet lines are
always quoted in vacuum and visible lines are conventionally quoted in air. A
calculation that compares a vacuum wavelength with a tabulated air wavelength
and finds a 0.03 per cent discrepancy has found its own error.

The tabulated hydrogen lines are reproduced by equation (7) with $R_M$ from (8)
at the level of parts in $10^5$; [`code/atomic_structure_demo.py`](./code/atomic_structure_demo.py)
does exactly this and reports the residuals (§7).

## 3. Energy levels, shells and the two kinds of X-ray energy

For a one-electron atom the level spacing is set by $Z^2$. That single scaling
has two consequences that a geophysicist uses constantly.

**Absorption edges.** To remove an electron from the $n=1$ shell of an atom of
atomic number $Z$ costs an energy of order $13.6\,Z^2$ eV — 9.2 keV for iron,
88 keV for lead. Below that energy the 1s electron is simply not available as a
target, so a photon cannot be absorbed by ionising the K shell. The
photoelectric cross section therefore drops abruptly as the photon energy falls
below the **K edge**, by a factor of five to ten over a few keV. This is the
reason a lead shield behaves very differently at 60 keV and at 90 keV, and the
reason radiography of steel uses a source whose energy sits just above the iron
K edge.

**Characteristic lines.** When a vacancy exists in the K shell — from
photoelectric absorption, from internal conversion, or from electron capture —
an electron from a higher shell falls in and the energy difference leaves as a
photon (or as an Auger electron). The energy is a **transition energy**, and it
is the difference between two binding energies:

$$E_{K\alpha} = B_K - B_{L}, \tag{9}$$

so a characteristic line is always *less* energetic than the corresponding
absorption edge. For barium the K edge is a little under 40 keV and the Kα line
is at 32.2 keV; the gap is the L-shell binding energy. Conflating the two is the
single most common error in this part of the subject, and it is a factor that
appears directly in an energy calibration.

## 4. Multi-electron atoms: screening and Moseley's law

Nothing so far has mentioned the other electrons, and for hydrogen that is
correct. In a heavy atom the K-shell electron sees a nucleus screened by all
the others, most effectively by the other K electron. The standard
one-parameter replacement is to write

$$E_K \approx -\frac{13.6\ \mathrm{eV}\,(Z - \sigma)^2}{1^2}, \tag{10}$$

where $\sigma$ is an empirical **screening constant** of order 1 to 2 for the K
shell. For a transition from the L shell to the K shell the corresponding
expression is

$$E_{K\alpha} \approx \tfrac34 \times 13.6\ \mathrm{eV}\,(Z - \sigma)^2, \tag{11}$$

because the electron ends in $n=1$ and starts in $n=2$ and the factor is
$(1/1^2 - 1/2^2) = 3/4$. Rearranged, (11) says

$$\sqrt{\frac{E_{K\alpha}}{hc}} \propto (Z - \sigma), \tag{12}$$

which is **Moseley's law**: the square root of the Kα frequency is linear in
the atomic number. It is a scaling law, not a precision formula, and it is worth
being clear about what it does and does not deliver:

- It predicts the *existence and ordering* of the Kα, Kβ, Lα series and the
  approximate Z² dependence of their energies.
- It predicts the slope of the straight line to within about ten per cent
  (the demo measures 8 per cent).
- It does not predict an absolute energy to better than tens of per cent for
  light elements, because $\sigma$ is not a constant.

Moseley's historical importance was not spectroscopic precision. By showing
that the X-ray frequencies order by integer $Z$ rather than by atomic weight, it
settled the ordering principle of the periodic table — and hence the meaning of
atomic number — a decade before the nucleus was understood.

## 5. Physical interpretation

Three readings of the same formulas.

**An energy level is a standing wave.** The reason $r_n \propto n^2$ is that a
bound electron must fit an integer number of half-wavelengths into the region
where it is trapped. Larger $n$ means a longer wavelength, which means a larger
orbit, which means a shallower potential well and hence a smaller binding
energy. The inverse-square force sets the *scale*; the integer sets the
*ladder*.

**$Z^2$ is a factor of ten thousand.** Going from $Z=6$ (carbon) to $Z=82$
(lead) multiplies atomic binding energies by about $1.9 \times 10^2$ in energy
units and reduces atomic radii by a factor of about 14. That is why the
characteristic lines of a lead absorber sit in the same decade as the gammas of
interest while those of carbon sit a factor of a hundred lower — and why the
photoelectric effect is a heavy-element phenomenon.

**The atom is where the low-energy spectrum comes from.** A nuclear gamma line
identifies a nuclide; an atomic K X-ray identifies an *element*, and the same
element appears in the spectrum of every nuclide that decays to it. Barium
X-rays appear in the spectra of caesium-137 and of barium-133 alike; lead
X-rays appear in every spectrum recorded behind a lead shield. A spectrum read
without this distinction generates spurious nuclide identifications, and this
is the origin of the "unidentified peaks" that fill the early literature on
airborne spectrometry.

## 6. Assumptions and regime of validity

The Bohr model is *not* a correct theory of the atom. It is a one-dimensional
recipe that reproduces the hydrogen energy levels exactly and most other
quantities badly. The correct framework is quantum mechanics, and its exact
solution for a one-electron Coulomb problem produces the same $1/n^2$ energy
ladder — so the energies in §1 are right, but for reasons the derivation does
not contain. Be precise about what can and cannot be trusted:

| Quantity | Bohr model | Correct treatment |
|---|---|---|
| Hydrogen $E_n$ ($1/n^2$ ladder) | Correct | Correct (Schrödinger), with fine structure from the Dirac equation |
| Hydrogen radii, orbital size | Correct order of magnitude | Correct mean radius is $\langle r\rangle = a_0 n^2[3/2 - 1/(2n^2)]$, not $a_0n^2$ |
| Angular momentum of a state | Wrong ($L = n\hbar$ rather than $\sqrt{\ell(\ell+1)}\hbar$, and no $\ell$ at all) | Schrödinger |
| Multi-electron atoms | Only as a screened one-parameter model | Hartree–Fock and beyond |
| Any transition **intensity** | Not predicted | Needs the wavefunctions |

Quantitative limits to state whenever you use the model:

1. **The screened model is interpolative.** The screening constant fitted to
   real K-edge energies is not constant: from the demo, $\sigma$ falls from
   about 3.1 at iron to about 1.6 at lead. Quoting a single $\sigma$ for all
   elements is a statement about a trend, not a prediction of an energy.
2. **Relativistic corrections grow as $Z^4$.** For lead the K-shell electron
   moves at a large fraction of $c$, and a non-relativistic model is
   systematically wrong by per cent-level amounts even after screening. The
   demo's unscreened estimate is 4 per cent high for lead and 29 per cent high
   for iron, and the residual for lead is largely unaccounted-for screening and
   relativity interacting.
3. **Weak transitions are absent from the model.** Selection rules, forbidden
   lines, Auger and Coster–Kronig transitions, and the whole intensity
   structure of a spectrum require matrix elements the model does not have.
4. **The medium is not vacuum.** In a solid, atomic levels shift with chemical
   environment by a few eV — enough to matter for X-ray absorption
   spectroscopy and not enough to matter for gamma-ray spectrometry.

## 7. Units and dimensional analysis

Work in electronvolts for atomic energies and in nanometres or keV for
wavelengths, but derive the conversion once so that it is never guessed:

$$\lambda\,[\mathrm{nm}] = \frac{hc}{E} = \frac{1239.841984}{E\,[\mathrm{eV}]} .
\tag{13}$$

The numerator is the numerical value of $hc$ in eV·nm from the **exact** SI
values $h = 6.626\,070\,15 \times 10^{-34}$ J s and $c = 299\,792\,458$ m/s.
Since $h$ and $c$ are exact and $e$ is exact, so is this number; it is not a
measurement and must not be quoted with an uncertainty. The Rydberg constant
$R_\infty = 109\,737.315\,681\,60$ cm⁻¹ and the electron mass are different:
they are **measured** CODATA quantities, and a calculation that depends on them
inherits their uncertainty. Cite them with their source, as the
[constant handbook](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
requires.

Two dimensional checks worth doing once, by hand.

**The fine-structure constant is dimensionless.** Form
$\alpha = e^2/(4\pi\varepsilon_0 \hbar c)$ from the constants above:
$e^2/(4\pi\varepsilon_0) = 2.307 \times 10^{-28}$ J m,
$\hbar c = 3.1615 \times 10^{-26}$ J m, so $\alpha = 7.297 \times 10^{-3} =
1/137.036$, with no unit. This is the statement that the Coulomb coupling
constant is a pure number, and it is why atomic energies can be written as
$\tfrac12 m_e c^2 \alpha^2$. Check the hydrogen ground state this way:

$$\tfrac12 m_e c^2 \alpha^2 = \tfrac12 (511\,000\ \mathrm{eV})
(7.297 \times 10^{-3})^2 = 13.60\ \mathrm{eV}. \tag{14}$$

The same 13.6 eV, from a completely different-looking route — mass, the speed of
light and a pure number. Agreement between two trivial-looking calculations
that share no constants except the fundamental ones is exactly the kind of check
a careless factor of 2 cannot survive.

**The Bohr radius is a Compton wavelength divided by $\alpha$.** Since
$a_0 = \hbar/(m_e c\,\alpha)$, and $\hbar/(m_e c) = 386$ fm is the reduced
Compton wavelength, $a_0 = 386\ \mathrm{fm}/7.297\times10^{-3} = 52.9$ pm. A
factor of $\alpha$ converts a quantum-electrodynamic length into an atomic one,
which is the quantitative statement of why atoms are large and nuclei are small.

## 8. Python demonstration

[`code/atomic_structure_demo.py`](./code/atomic_structure_demo.py) builds the
hydrogen spectrum from $R_\infty$ and the electron-to-proton mass ratio,
compares it with the tabulated air and vacuum wavelengths of seven lines,
recovers the screening constant from six tabulated K-edge energies, fits
Moseley's law, and computes the barium Kα energy. Every tabulated input is
labelled in the output. Run it; do not read it.

The level ladder and the spectrum:

```text
   n      E_n (eV)     E_n (a.u. of R_H)   radius (nm)
   1    -13.598287              1.000000       0.05292
   2     -3.399572              0.250000       0.21167
   3     -1.510921              0.111111       0.47626
   4     -0.849893              0.062500       0.84668
   5     -0.543931              0.040000       1.32294
   6     -0.377730              0.027778       1.90504

  Ionisation energy of hydrogen: 13.598287 eV. The tabulated
  measured value is 13.598434 eV; the difference is the finite
  nuclear mass (already included) plus relativistic, Lamb-shift and
  hyperfine corrections (not included, ~1e-4 eV).
```

```text
line                   quoted in   model (nm)  tabulated  diff (nm)   rel diff
Ly-alpha (2->1)           vacuum    121.56845   121.5670     0.0014   1.19e-05
Ly-beta  (3->1)           vacuum    102.57338   102.5720     0.0014   1.34e-05
H-alpha  (3->2)              air    656.28781   656.2790     0.0088   1.34e-05
H-beta   (4->2)              air    486.13912   486.1330     0.0061   1.26e-05
H-gamma  (5->2)              air    434.05279   434.0470     0.0058   1.33e-05
H-delta  (6->2)              air    410.17988   410.1740     0.0059   1.43e-05
Paschen-alpha (4->3)         air   1875.10804  1875.1000     0.0080   4.29e-06
```

Two features of that table are the physics. The residuals are all the same sign
and are smallest for the longest wavelength, which is the signature of using a
single refractive index for a dispersive quantity — the model error is in the
comparison, not in the Rydberg formula. And the absolute agreement, 0.006 nm on
a 486 nm line, is 1.3 parts in 10⁵: the model has earned its place.

The isotope shift, from the same script:

```text
  The isotope shift is resolvable: H-alpha for deuterium is at
  656.1093 nm against 656.2878 nm for hydrogen, a shift of
  0.1785 nm = 178.53 pm.
```

The screened one-electron model against six tabulated K edges:

```text
element     Z   E_K model (keV)   K edge (keV)  model/measured  fitted sigma
Fe         26            9.1974         7.1120          1.2932         3.137
Cu         29           11.4424         8.9790          1.2743         3.311
Mo         42           24.0004        20.0000          1.2000         3.660
Ag         47           30.0550        25.5140          1.1780         3.696
W          74           74.5048        69.5250          1.0716         2.516
Pb         82           91.4847        88.0050          1.0395         1.575
```

And Moseley's law, fitted rather than asserted:

```text
  Least-squares slope     = 0.109308 keV^0.5 per unit Z
  Least-squares intercept = -0.362665 keV^0.5
  Implied screening constant sigma = 3.3178
  rms residual in sqrt(E) = 4.86e-02 keV^0.5 (9.53e-01 per cent of the mean)

  The model's slope is sqrt((3/4) x 13.6057 eV / 1000) = 0.101016
  keV^0.5 per unit Z, against the fitted 0.109308: agreement to
  8.21 per cent.
```

### What to observe

- The fitted slope is 8 per cent above the unscreened model's, and the residuals
  change sign three times across six elements: the relation is linear to under
  1 per cent rms but it is not exactly a straight line. A trend law that fits to
  1 per cent and predicts to 30 per cent is a normal and useful object, as long
  as it is described that way.
- The screening constant recovered from the *binding* energies varies from 3.1
  to 1.6 while the constant recovered from the *transition* line is 3.32. One
  number cannot describe both, because a transition energy is a difference of
  two screened levels and most of the screening cancels.
- The final section's barium check: for barium ($Z = 56$) the model gives a
  K-shell binding energy of 42.67 keV but a Kα transition energy of 32.00 keV,
  against a tabulated Kα1 of about 32.19 keV — agreement to 0.6 per cent for the
  transition, against 10 to 30 per cent for the binding energy. Use the model
  for differences, not for absolute binding energies.

## 9. Common mistakes

1. **Confusing an absorption edge with a characteristic line.** The Kα energy
   is *less* than the K-edge energy by the L-shell binding energy. Any
   calibration curve that treats them as the same number is wrong by 10 to
   20 per cent, which is larger than most calibration errors.
2. **Comparing a vacuum wavelength with an air wavelength.** A 0.03 per cent
   discrepancy on a 500 nm line is 0.15 nm — visible on a good spectrograph, and
   entirely an artefact of the medium.
3. **Using $Z$ where $Z_\mathrm{eff}$ belongs, or vice versa.** The unscreened
   $13.6\,Z^2$ eV is not a K-edge energy, and it is 29 per cent wrong for iron.
   State which you are using and why.
4. **Quoting the Bohr model as physics.** The energies are right; the angular
   momentum, the intensity and the orbital shape are not. Write "the
   one-electron model gives..." rather than "the electron orbits at...".
5. **Reporting $hc = 1240$ eV nm as a measurement.** It follows from exact
   constants and is exact.
6. **Forgetting the isotope shift when comparing hydrogen and deuterium data.**
   A 0.18 nm shift on the Hα line is 30 times larger than a typical modern
   measurement's precision and cannot be attributed to instrument error.
7. **Assuming a characteristic X-ray energy is a nuclear gamma energy.** The
   energies are atomic and identify elements; treating them as gammas generates
   spurious nuclide identifications in a spectrum.
8. **Ignoring the chemical shift when the application is X-ray absorption.**
   A few eV is negligible for a 662 keV gamma and decisive for an absorption
   edge in a mineral.
9. **Using relativistic formulas to high $Z$ without saying so.** A per cent
   correction at $Z = 82$ is larger than the accuracy of most geological
   inference.
10. **Quoting $R_\infty$ to eight figures without its source.** It is measured;
    the source belongs in the sentence.

## 10. Real-world applications

- **Gamma-ray spectrometry.** Every low-energy spectrum is dominated by the
  K X-rays of the daughter element. Identifying them, and knowing they are
  atomic, is what separates a real nuclide inventory from a list of spurious
  lines. The barium X-rays near 32 keV and the lead X-rays at 75 to 85 keV are
  the two that every practitioner meets first
  ([04](./04-gamma-spectrometry.md)).
- **Shielding design.** The K edge sets where an absorber stops being an
  absorber. Half-value layers change by a factor of several across an edge, so a
  shield specification without an energy is not a specification
  ([03](./03-radiation-interaction.md)).
- **X-ray fluorescence and portable XRF.** The technique is characteristic-line
  spectroscopy: excite with a source above the K edge, identify the emitted
  lines. Its sensitivity to an element depends on the fluorescence yield, which
  is the branching between radiative and Auger filling of the vacancy — high for
  transition metals, low for light elements, which is why a portable XRF
  struggles with, say, sodium.
- **Photoelectric absorption logging.** The Pe measurement in a borehole is a
  Z-dependent absorption measurement, and its ability to separate quartz,
  calcite and dolomite follows directly from the $Z^{3.6}$ scale of the
  photoelectric cross section ([05](./05-neutron-interaction.md) §7).
- **Internal conversion and electron capture.** Both create K-shell vacancies
  and hence characteristic X-rays, and their relative probabilities are
  tabulated per nuclide. Reading them tells you the decay mode, which is how a
  spectrometer distinguishes a nuclide from its daughters
  ([02](./02-radioactive-decay.md)).
- **Radon progeny and the "unidentified" 32 keV peak.** The barium X-rays from
  caesium-137 are the standard example, and the corresponding Pb X-rays from a
  lead shield are the reason low-energy backgrounds in a shielded detector are
  dominated by the shield material itself.

## 11. Further reading

- **Bethe, H. A., & Salpeter, E. E. *Quantum Mechanics of One- and Two-Electron
  Atoms* (Springer).** The definitive treatment of the hydrogen problem
  including the reduced-mass, relativistic and radiative corrections that this
  lesson lists but does not compute. Level: graduate.
- **Herzberg, G. *Atomic Spectra and Atomic Structure* (Dover).** The classical
  account of the spectra, the series and the isotope shift, written for
  spectroscopists. Level: advanced.
- **Moseley, H. G. J. (1913–1914). "The high-frequency spectra of the
  elements." *Philosophical Magazine*.** The original papers on the
  $Z$-ordering of X-ray frequencies, worth reading for how a scaling law
  becomes a structural discovery. Level: intermediate, historical.
- **NIST, *X-Ray Transition Energies* database, and the *XCOM* photon
  cross-section database.** The compiled K, L and M energies, K edges and
  attenuation coefficients used as tabulated inputs here. Level: reference.
  Confirm both the transition energies and the edge energies in the current
  release; they are revised.
- **NIST, *CODATA Internationally Recommended Values of the Fundamental Physical
  Constants*.** The source of $m_e$, $m_p$, $R_\infty$ and every other measured
  constant used in this lesson. Distributed at
  <https://physics.nist.gov/cuu/Constants/>. Level: reference.
- **Knoll, G. F. *Radiation Detection and Measurement* (Wiley).** The standard
  text on detectors, and the place to read how K X-rays and escape peaks appear
  in a measured spectrum. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [02 Radioactive Decay, Half-Life and Dating](./02-radioactive-decay.md) — what
  the nucleus does, and why the atomic part of a decay is a separate
  calculation.
- [03 Interaction of Radiation with Matter](./03-radiation-interaction.md) — the
  photoelectric process whose edges this lesson's binding energies set.
- [04 Gamma-Ray Spectrometry and Natural Radioelements](./04-gamma-spectrometry.md)
  — where the X-rays and escape peaks actually appear in a measured spectrum.
- [02-07-01 Electrostatics, Coulomb's Law and Electric Potential](../07-electromagnetism/01-electrostatics.md)
  — the force used in §1.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../../01-mathematics/05-single-variable-calculus/04-taylor-series.md)
  — the expansions behind the reduced-mass and screening approximations.
- [26-02-03 Physical Constants and Earth Parameters with Sources](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the exact-versus-measured classification used throughout §7.

Exercises:
[`exercises/01-atomic-structure-exercises.md`](./exercises/01-atomic-structure-exercises.md)
and
[`exercises/01-atomic-structure-solutions.md`](./exercises/01-atomic-structure-solutions.md).

## Self-assessment checklist

- [ ] I can derive $r_n = a_0 n^2/Z$ and $E_n = -13.6\,Z^2/n^2$ eV from (1)–(3),
      and I can say which of the three statements is not classical. (§1)
- [ ] I can compute the wavelength of any hydrogen line from the Rydberg formula
      without looking it up. (§2)
- [ ] I can explain the isotope shift and compute it for hydrogen against
      deuterium. (§2)
- [ ] I can state why Lyman wavelengths are quoted in vacuum and Balmer
      wavelengths in air, and correct for the difference. (§2)
- [ ] I can distinguish a binding energy from a transition energy and say which
      is larger. (§3)
- [ ] I can compute a Kα energy from $Z$ and a stated screening constant, and
      state the model's accuracy for light and heavy elements. (§4)
- [ ] I can state Moseley's law, what it is linear in, and what it demonstrated.
      (§4)
- [ ] I can check a Coulomb-model energy against $\tfrac12 m_e c^2\alpha^2$ and
      against $hc/\lambda$. (§7)
- [ ] I can list three features of a gamma-ray spectrum that are atomic rather
      than nuclear. (§10)
- [ ] I can name the compilation I would use for a K-edge energy and say when
      I last confirmed it. (§11)
