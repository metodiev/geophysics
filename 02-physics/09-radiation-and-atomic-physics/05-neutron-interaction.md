---
id: 02-09-05
title: "Neutron Interactions and Borehole Nuclear Measurements"
level: graduate
prereqs: ["02-09-03", "02-09-04", "02-09-02"]
estimated_minutes: 90
tags: [neutrons, moderation, neutron-porosity, density-log, photoelectric-factor, borehole]
---

# Neutron Interactions and Borehole Nuclear Measurements

A neutron log measures porosity. That statement is remarkable when you unpack
it: the tool emits fast neutrons into a rock, and what comes back is a number
that tracks the pore volume, even though the rock contains no hydrogen and the
pore fluid does. The reason is the collision kinematics of §2 — a neutron
loses half its energy on average in a head-on collision with a hydrogen nucleus
and almost none in a collision with silicon — so the thermal-neutron population
near the tool is controlled by the hydrogen *number* density in the formation.
Porosity enters through the pore fluid, and the measurement is really a hydrogen
measurement that is calibrated as a porosity.

This is the graduate lesson of the module and it is where the largest number of
tabulated inputs enters. Thermal-neutron cross sections are tabulated at a
reference speed and differ between evaluated compilations; the hydrogen values
are bound-atom values, which differ from free-atom values; the tool's calibration
in API units is an instrument convention. The lesson keeps those three categories
separate, and the demo labels every input in its output.

The lesson also assembles the **density–neutron–Pe** suite that every
petrophysical interpretation uses: the neutron measurement of hydrogen, the
gamma–gamma measurement of electron density, and the photoelectric factor that
identifies the matrix — three measurements from two different particles, which
together solve for porosity and lithology at once.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a neutron has no Coulomb barrier and what that implies for
   cross sections and for shielding, in contrast with charged particles.
2. **Compute** the conventional thermal energy at 2200 m/s and the Maxwellian
   mean at a stated temperature, and state which convention a quoted cross
   section uses.
3. **Derive** the average logarithmic energy decrement $\xi$ from collision
   kinematics, compute the maximum fractional energy loss, and compute the mean
   number of collisions to thermalise.
4. **Compute** macroscopic cross sections and mean free paths from tabulated
   microscopic cross sections and a number density.
5. **Define** the moderating ratio, compute it for water, heavy water, graphite
   and rock, and explain why it, and not $\xi$ alone, decides a moderator.
6. **Explain** the hydrogen index and compute it for water, oil and gas, and
   derive the gas effect that makes the neutron and density porosity readings
   diverge.
7. **Derive** the chlorine-log response from capture competition, and compute the
   fraction of captures on chlorine as a function of salinity.
8. **Compute** the electron density index and the photoelectric factor from a
   mineral formula, and state the definition dependence of the effective atomic
   number.
9. **State** which quantities in a nuclear-log interpretation are tabulated,
   which are model inputs and which are tool conventions, and cite the tabulated
   ones.

## Prerequisites

- [02-09-03 Interaction of Radiation with Matter](./03-radiation-interaction.md)
  — cross sections, mean free paths and the contrast with charged particles.
- [02-09-04 Gamma-Ray Spectrometry and Natural Radioelements](./04-gamma-spectrometry.md)
  — detectors, windows and the calibration logic shared with the density log.
- [02-09-02 Radioactive Decay, Half-Life and Dating](./02-radioactive-decay.md)
  — sources, activities and the decay of an activation product.

## 1. Why neutrons are different, and where they come from

A charged particle entering matter is slowed by every electron it passes, and
its range is a few micrometres to a few centimetres. A neutron has no charge, so
it feels no electric field and passes the electron cloud without noticing. It
interacts only with nuclei, and only when it comes within a few femtometres of
one. Two consequences follow, and they govern everything here:

- **Cross sections are small and strongly material-specific.** A thermal neutron
  sees a cross section of 0.00019 barn on oxygen and 33.5 barn on chlorine — a
  factor of $10^5$ between two elements of similar mass. The response of any
  neutron measurement is set by the strongest absorber and the best moderator
  present, not by the average composition.
- **Shielding is moderation, not thickness.** Heavy material stops photons; a
  neutron needs *hydrogen* (or another light nucleus) to slow down and an
  absorber to be caught. The two requirements are different and often need
  different parts of the shield.

**Sources.** Three kinds matter in geophysics.

- **Radioisotope sources.** An americium–beryllium source mixes an alpha emitter
  with beryllium; the $\alpha$ + $^9$Be reaction yields neutrons with a broad
  spectrum reaching tens of MeV, and a mean of order 4 to 5 MeV that is source
  specific and must be taken from the source datasheet. A common choice in
  logging is a source of this type with a declared output in neutrons per
  second. Californium-252 is a spontaneous-fission source whose spectrum is
  described by a Watt or Maxwellian form whose mean follows from its one
  temperature parameter — a **tabulated** parameter that differs between
  evaluations.
- **Accelerator sources.** A deuterium–tritium generator produces essentially
  monoenergetic 14 MeV neutrons from the D–T reaction. The high energy and the
  associated penetration are why these are used for the "pulsed neutron" tools
  of §6.
- **Activation.** Any neutron source activates the material around it. Induced
  activity is a real operational constraint on source handling and on logging
  following a run, and it is dosimetry rather than petrophysics
  ([06](./06-dosimetry.md)).

**What "thermal" means.** Thermal-neutron cross sections are tabulated at a
reference speed of 2200 m/s, and a thermalised neutron gas has a Maxwellian
energy distribution rather than a single energy. The demo computes both:

```text
  Cross sections are tabulated at v = 2200 m/s, the
  conventional reference speed. That corresponds to
    E = m v^2 / 2 = 4.053325e-21 J = 0.025299 eV.

  A thermalised neutron gas at T = 293.6 K (20.45 C) has
    <E> = 3 k T / 2 = 0.037951 eV,

  Ratio 1.5 k T / (m v_ref^2 / 2) = 1.500097
  Ratio of mean speeds to 2200 m/s = 1.224784
```

The reference speed is the *most probable* speed of a gas at about 20 °C, not the
mean speed, and the mean energy is 1.5 times the reference energy. Since most
nuclides follow the $1/v$ law in the thermal range, an effective cross section
averaged over a Maxwellian spectrum is about 0.9 times the tabulated value for a
$1/v$ absorber — a 10 per cent systematic that must be stated whenever a thermal
cross section is used as though it were a single number. This is the neutron
analogue of the half-life-compilation problem, and it has the same remedy: say
which convention and which compilation.

## 2. Slowing down, derived

**Collision kinematics.** In an elastic collision of a neutron of mass 1 with a
nucleus of mass $A$ at rest, the energy after the collision is

$$E' = E\,\frac{1 + A^2 + 2A\cos\theta}{(1+A)^2}, \tag{1}$$

where $\theta$ is the scattering angle in the centre-of-mass frame. Two limits
are worth memorising: a grazing collision ($\cos\theta = 1$) leaves $E' = E$, and
a head-on collision ($\cos\theta = -1$) gives

$$\frac{E'}{E} = \left(\frac{A - 1}{A + 1}\right)^2,
\qquad\text{so}\qquad
\frac{\Delta E}{E}\bigg|_{\max} = \frac{4A}{(1+A)^2}. \tag{2}$$

For hydrogen ($A = 1$) the maximum loss is 100 per cent — the neutron can stop
dead and the proton takes everything. For carbon ($A = 12$) it is 28 per cent,
and for iron ($A = 56$) it is 7 per cent. Everything about neutron moderation
follows from equation (2).

**The average logarithmic decrement.** Averaging $\ln(E/E')$ over the
isotropically distributed scattering angles gives the standard result

$$\xi = 1 + \frac{(A-1)^2}{2A}\ln\left(\frac{A-1}{A+1}\right)
\quad (A > 1), \qquad \xi = 1 \quad (A = 1), \tag{3}$$

and the mean number of collisions to slow from $E_0$ to $E_\mathrm{th}$ is

$$n = \frac{\ln(E_0/E_\mathrm{th})}{\xi}. \tag{4}$$

The demo evaluates (3) and (4) for a 4.5 MeV source neutron slowing to 25 meV:

```text
nuclide        A        xi  n to thermalise  ln(E0/Eth)
H           1.01   0.99982             19.0     19.0085
D           2.01   0.72193             26.3     19.0085
C          12.01   0.15763            120.6     19.0085
O          16.00   0.11995            158.5     19.0085
Si         28.09   0.06955            273.3     19.0085
Ca         40.08   0.04908            387.3     19.0085
Fe          55.84   0.03539            537.1     19.0085
```

Hydrogen needs 19 collisions and silicon needs 273. That ratio is why a
hydrogen-bearing pore fluid controls the thermal-neutron population near a tool,
and therefore why a neutron log reads porosity. Note the exact statement of the
$A = 1$ limit: $\xi = 1$ only for a nucleus of exactly unit mass, whereas a real
proton has $A \approx 1.008$ and $\xi = 0.99982$. Small, but the sort of detail a
graduate should state rather than round away.

**Per collision is not the whole story.** The quantity that describes how
effectively a material slows neutrons per unit path length is the
**slowing-down power** $\xi\Sigma_s$, and the quantity that describes how well it
does so *before absorbing the neutron* is the **moderating ratio**

$$\text{moderating ratio} = \frac{\xi\Sigma_s}{\Sigma_a}. \tag{5}$$

The demo computes it:

```text
medium                rho   xi (eff)    Sigma_s    Sigma_a     ratio
light water H2O     1.000    0.91714     1.5054    0.02220      62.2
heavy water D2O     1.107    0.49100     0.3672    0.00004    4476.6
graphite C          1.700    0.15763     0.4040    0.00030     213.5
quartz rock         2.650    0.10971     0.2822    0.00455       6.8
```

Water's moderating ratio of 62 is the commonly quoted figure and it falls out of
tabulated cross sections with no fitting. Heavy water beats it by two orders of
magnitude and the reason is *entirely* in $\Sigma_a$: deuterium absorbs about 650
times less strongly than hydrogen at the same speed, and it needs only 26
collisions against 19 to slow down. Water is the best moderator per unit path
length and a mediocre one per neutron captured; that is why reactor designers
who care about both use heavy water or graphite.

The rock row is the punch line for the borehole. A quartz rock has a moderating
ratio an order of magnitude below water's, so a neutron entering the matrix is
far more likely to be absorbed before it thermalises than one entering the pore
fluid. Increasing water content increases the thermal-neutron population near the
tool, and it is that population, seen through the count rate at a detector, that
is reported as porosity.

## 3. Macroscopic cross sections and mean free paths

The bridge from tabulated microscopic cross sections to a measurement is

$$\Sigma = N\sigma, \qquad N = \frac{\rho N_A}{M}, \qquad
\text{mean free path} = \frac{1}{\Sigma}. \tag{6}$$

The demo computes it for water and for a quartz rock:

```text
Water, rho = 1.00 g/cm^3:
nuclide        N (1/cm3)   sigma_a (b)   Sigma_a (1/cm)   Sigma_s (1/cm)
H            6.68570e+22         0.332          0.02220           1.3642
O            3.34285e+22       0.00019          0.00001           0.1415
total                                           0.02220           1.5054
  Absorption mean free path = 45.0 cm; scattering mean
  free path = 0.66 cm.
```

Two facts to read off. The absorption mean free path in water is 45 cm and the
scattering mean free path is 0.66 cm — so a thermal neutron is scattered hundreds
of times before it is captured. That ratio, not the individual cross sections, is
what makes a diffusion description of neutron transport workable in a borehole
geometry. And the whole of the absorption in water is on hydrogen: oxygen
contributes $10^{-3}$ of it.

Adding a small concentration of a strong absorber changes everything, which is
why boron and gadolinium appear in neutron shielding and in tracers:

```text
nuclide      sigma_a (b)   Sigma in water at 1 g/L
B                    767               4.27248e-05
Cd                  2520               1.35004e-05
Gd                 49000               1.87653e-04
Cl                  33.5               5.69088e-07
```

A gram per litre of boron contributes about twice the absorption of all the
water it is dissolved in. This is also the warning for interpretation: **a
formation's neutron response is set by its strongest absorber**, so a few hundred
ppm of boron or a few ppm of gadolinium in a pore fluid can dominate a log whose
porosity is being read from the count rate.

## 4. Neutron porosity, the hydrogen index, and the gas effect

The neutron log is calibrated so that a water-filled limestone of porosity
$\phi$ reads $\phi$ (the calibration is by definition, in API units, against a
standard limestone block). What the tool actually responds to is the **hydrogen
index**,

$$\mathrm{HI} = \frac{\text{number of hydrogen atoms per unit volume}}
{\text{number of hydrogen atoms per unit volume in fresh water}} , \tag{7}$$

so HI(water) = 1 by construction and HI(quartz) = 0. The demo computes HI from
the composition and density of each fluid:

```text
fluid                   rho (g/cm3)  n_H per molecule      HI
water                         1.000                 2   1.000
methane, gas @ 0.10           0.100                 4   0.225
methane, gas @ 0.20           0.200                 4   0.449
methane, liquid               0.420                 4   0.943
octane-like oil               0.750                18   1.065
```

Liquid hydrocarbons have HI within a few per cent of unity, which is why the
neutron log reads liquid-filled porosity without a fluid correction. Gas does
not: at 0.2 g cm⁻³ its hydrogen index is 0.45, and a gas-filled pore therefore
looks like a pore of half the size to the neutron log.

**The gas effect, derived.** Let the density log measure bulk density and report
a *density porosity*

$$\phi_D = \frac{\rho_\mathrm{ma} - \rho_b}{\rho_\mathrm{ma} - \rho_f}, \tag{8}$$

and let the neutron tool report a reading proportional to the hydrogen index
(this proportionality is a model, and a crude one — real tools have their own
calibration and corrections). For a sandstone with matrix density 2.65, fresh
water at 1.00, true porosity 0.25 and gas density 0.10:

```text
   S_g    rho_b    phi_D  phi_N (model)  phi_D - phi_N
   0.0   2.2375   0.2500         0.2500         0.0000
   0.4   2.1475   0.3045         0.1725         0.1321
   1.0   2.0125   0.3864         0.0561         0.3302
```

The two readings are equal for a water-filled rock and diverge steadily as gas
replaces water, in **opposite directions**: the density log over-reads because
gas is light, and the neutron log under-reads because gas has little hydrogen.
The separation — not the value of either curve — is the standard gas indicator,
and it is why a gas-bearing sand is recognised by two logs that disagree with
each other rather than by either one alone. What is model here is the magnitude
at a given saturation, which depends on the gas density and hence on pressure and
temperature; the sign and the monotonicity are physics.

## 5. The density log and the photoelectric factor

The density tool is a gamma–gamma backscatter measurement, so it responds to
**electron density**. The electron density index is

$$\rho_e = \frac{2Z}{A}\rho, \tag{9}$$

and because $2Z/A$ is between 0.99 and 1.11 for nearly everything that matters in
a sedimentary sequence, the tool is very nearly a bulk-density measurement with a
constant scaling — which is why it can be calibrated with two points and why it
works without any knowledge of the mineralogy. The demo computes the column:

```text
matrix        rho    Z_eff    2Z/A    rho_e  Pe computed  Pe published   diff %
water        1.00    7.428  1.1102   1.1102        0.343          0.36     -4.8
quartz       2.65   11.582  0.9986   2.6463        1.697          1.81     -6.3
calcite      2.71   15.142  0.9991   2.7077        4.453          5.08    -12.3
dolomite     2.87   13.123  0.9978   2.8638        2.660          3.14    -15.3
```

The **photoelectric factor** is the same measurement's low-energy channel,
familiar to this module from lesson 01: the photoelectric cross section scales as
$Z^{3.6}$ or so, so a ratio of a low-energy window to a high-energy window is a
matrix identifier. It is conventionally written

$$\mathrm{Pe} = \left(\frac{Z_\mathrm{eff}}{10}\right)^{3.6}, \qquad
Z_\mathrm{eff} = \left(\frac{\sum_i n_iZ_i^4}{\sum_i n_iZ_i}\right)^{1/3},
\tag{10}$$

with the sums over the atoms of the formula unit and the denominator the electron
count — the electron-fraction-weighted definition. This is stated explicitly
because **several definitions are in use**: weighting by atom fraction, by
electron fraction or by mass, with exponents of 4 or 3.6 or 3.1. The comparison
in the table above is the evidence that equation (10) is the intended one: the
computed values are 5 to 15 per cent below the commonly published matrix
values, in the right order, with the right ratios. The important point is not
the agreement but what it demonstrates — the *ordering and ratios* of the matrix
Pe values follow from the compositions alone, with no calibration input. Pe is a
lithology measurement, and its absolute scale is a tool convention that must be
quoted.

**Why the suite is three logs and not one.** Density alone cannot distinguish a
quartz-porous rock from a calcite-porous rock at different porosity: two
unknowns, one equation. Pe identifies the matrix, supplying the second
constraint, and the neutron log supplies hydrogen, which is a third and largely
independent quantity. The standard interpretation is therefore a simultaneous
solve, not a sequence of separate readings.

## 6. Capture, activation and the chlorine log

Once a neutron is thermal, it wanders until it is captured. Capture is usually
radiative — $(n,\gamma)$ — and the resulting gamma rays have energies
characteristic of the capturing nucleus. Two applications follow.

**The chlorine log.** Formation water contains dissolved NaCl, so it contains two
absorbers, hydrogen and chlorine. Which one captures is set by
$\Sigma = N\sigma$ for each, and $\Sigma$ for chlorine rises with salinity. The
demo computes the capture share:

```text
 salinity (g/L) Sigma_H (1/cm)  Sigma_Cl (1/cm)  Cl share
            0.0        0.02220          0.00000    0.0000
           10.0        0.02220          0.00345    0.1346
           50.0        0.02220          0.01726    0.4375
          100.0        0.02220          0.03452    0.6086
          300.0        0.02220          0.10356    0.8235
```

For seawater at about 35 g L⁻¹ roughly 35 per cent of captures happen on
chlorine. Because the capture gamma rays of chlorine have different energies from
those of hydrogen, a gamma detector that counts only the chlorine lines sees
salinity directly. That is the chlorine log, and its physical content is exactly
the table above.

**Pulsed-neutron and activation tools.** A pulsed source turns the neutron output
on and off, and the decay of the thermal-neutron population between pulses is
measured; that decay time is a function of the formation's capture cross section,
which is the same $\Sigma_a$ of §3. The same idea in the geochemical direction is
**neutron activation analysis**: the capture or inelastic reaction transmutes a
nucleus into a radioactive one, and the delayed gamma rays that follow identify
the element. Oxygen activation is used to detect water flow behind casing, which
is one of the few borehole measurements that is unambiguously about *movement*
rather than about composition.

## 7. Physical interpretation

**The tool measures hydrogen, and reports porosity through a calibration that
assumes a matrix.** Every number on a neutron log is an apparent limestone
porosity, which is to say a hydrogen index converted by a convention that
includes a matrix assumption. Change the matrix and the same count rate means a
different porosity. This is not a defect of the instrument; it is the reason Pe
is measured at the same time.

**Cross sections are nuclear, not chemical.** A neutron does not care about
oxidation state, mineralogy or the fluid's salinity except through the number
densities of the nuclei involved. That is what makes the measurement robust in
one sense — it cannot be fooled by chemistry — and fragile in another, because
the presence of a few ppm of a strong absorber silently changes the answer.

**The two-neutron-category structure.** Every neutron tool separates the
population into "fast" and "thermal" and measures a ratio between two detectors
at different distances. The near detector sees mostly fast neutrons and the far
detector mostly thermal ones; the ratio is far less sensitive to the borehole and
to the source strength than either count rate alone. This is a compensated
measurement, and it is the same idea as a ratio measurement in any other
geophysical method: measuring a ratio cancels the parts of the response that are
common to both channels.

## 8. Assumptions and regime of validity

1. **The cross sections are tabulated and conventionally defined.** Thermal
   values are at 2200 m/s; effective values over a Maxwellian spectrum differ by
   about 10 per cent for $1/v$ absorbers; the hydrogen values are bound-atom
   values and differ measurably from free-atom ones. State the compilation and
   the convention.
2. **Cross sections vary with energy above thermal.** The values in §3 apply to
   thermal neutrons. Fast-neutron reactions have their own cross sections, and a
   14 MeV source probes a different set.
3. **Diffusion theory is an approximation.** The relation between count rate and
   porosity is computed with a transport code and calibrated against standards,
   not derived from §2 and §3 in closed form. The physics in this lesson explains
   the response; it does not predict the calibration.
4. **The hydrogen index model ignores matrix hydrogen.** Clays, micas and
   hydrated minerals contain hydrogen in their crystal structures, which is why
   shales read high porosity on a neutron log and why the correction needs an
   independent clay indicator.
5. **The density tool's assumptions.** Short source–detector spacing, a
   known tool standoff, and the absence of heavy minerals: a baryte-weighted mud
   or an ore mineral invalidates the electron-density calibration. The
   photoelectric channel is more robust here, which is one reason it is recorded.
6. **Borehole environment.** Mudcake, casing, cement, invasion and hole size all
   contribute to the count rate, and the environmental corrections are part of
   the measurement, not a refinement
   ([05-08-01 The Borehole Environment and Invasion Profiles](../../05-core-geophysics/08-geophysical-logging/01-borehole-environment.md)).
7. **Tool conventions.** API neutron units and Pe units are conventions defined
   against physical standards. A reading without its tool model and calibration
   is not interpretable.

## 9. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| Microscopic cross section | barn = 10⁻²⁸ m² = 10⁻²⁴ cm² | At 2200 m/s unless stated |
| Macroscopic cross section | cm⁻¹ | $\Sigma = N\sigma$ |
| Mean free path | cm | $1/\Sigma$ |
| $\xi$ | dimensionless | Mean of $\ln(E/E')$ |
| Moderating ratio | dimensionless | $\xi\Sigma_s/\Sigma_a$ |
| Hydrogen index | dimensionless | Relative to water at 1 g cm⁻³ |
| Bulk density | g cm⁻³ | Density log |
| Electron density index $\rho_e$ | g cm⁻³ | $(2Z/A)\rho$ |
| Pe | barnes per electron, conventionally dimensionless | $(Z_\mathrm{eff}/10)^{3.6}$ |
| Neutron porosity | % or p.u. | Apparent limestone porosity by convention |

Three checks.

**The barn conversion is the commonest error in this material.** One barn is
$10^{-28}$ m², which is $10^{-24}$ cm². A number density in cm⁻³ multiplied by a
cross section in b must be multiplied by $10^{-24}$ to give cm⁻¹; using
$10^{-28}$ gives an answer $10^4$ too small, which is exactly the kind of error
that turns a 45 cm mean free path into 0.0045 cm and looks like a physical
result. Check one entry by hand: $6.6857 \times 10^{22}\ \mathrm{cm^{-3}} \times
0.332 \times 10^{-24}\ \mathrm{cm^2} = 0.0222\ \mathrm{cm^{-1}}$, a mean free
path of 45 cm.

**$\xi$ must lie between 0 and 1.** The maximum energy loss in a head-on
collision is $4A/(1+A)^2$, which is 1 for hydrogen and 0.07 for iron; the average
logarithmic decrement is correspondingly bounded by 1. A value above 1 or below 0
means the formula has been mistranscribed.

**The moderating ratio is dimensionless and must be asserted as such.** $\xi$ has
no unit, $\Sigma_s/\Sigma_a$ is a ratio of two macroscopic cross sections in the
same unit, and the result is a pure number. Water giving 62 and heavy water 4477
are checkable against widely published values; a result of 62 000 or 0.06 means a
unit or a number-density error.

## 10. Python demonstration

[`code/neutron_interaction_demo.py`](./code/neutron_interaction_demo.py)
computes the thermal-energy conventions, $\xi$ and the number of collisions,
macroscopic cross sections and mean free paths, the moderating ratio, the
hydrogen index and the gas effect on the two porosity logs, the chlorine capture
share, and the electron density and Pe of four matrices. Nuclear data are
labelled TABULATED, the tool response is labelled MODEL, and the collision
kinematics are exact.

### What to observe

- The moderating ratio reproduces the commonly quoted 62 for light water and is
  within a few per cent of the published figure for heavy water, from tabulated
  cross sections alone. Its ordering — D₂O, then graphite, then water, then rock
  — is the quantitative statement of the whole lesson.
- The hydrogen index of liquid hydrocarbons is within 5 per cent of unity while
  that of gas at 0.2 g cm⁻³ is 0.45. That one column is the gas effect.
- The Pe values are 5 to 15 per cent below the published matrix values and in
  the correct order. A definition-dependent quantity agreeing to 15 per cent with
  the right ratios is a successful cross-check; claiming better agreement would
  be claiming more than the definitions support.
- The chlorine capture share passes 35 per cent at seawater salinity. Nothing in
  that table is fitted; it is $\Sigma = N\sigma$ twice.

## 11. Common mistakes

1. **Using a barn as $10^{-28}$ cm².** It is $10^{-24}$ cm². The error is a
   factor of $10^4$ and it looks plausible.
2. **Quoting a thermal cross section without the 2200 m/s convention or the
   effective-value correction.** The two differ by about 10 per cent.
3. **Comparing a bound-atom and a free-atom hydrogen cross section.** They are
   different quantities, and the difference is larger than most of the effects
   being discussed.
4. **Reading a neutron porosity as a true porosity.** It is an apparent
   limestone porosity; matrix, shale, gas and salinity all shift it.
5. **Forgetting matrix hydrogen.** Clays make a shale read high, and the
   correction needs a separate clay indicator.
6. **Treating the density log as a porosity in the presence of heavy minerals.**
   Baryte, siderite and ore minerals break the electron-density calibration.
7. **Using one definition of $Z_\mathrm{eff}$ and comparing with Pe values quoted
   under another.** State the definition, the weights and the exponent.
8. **Ignoring the borehole environment.** Casing, cement, mudcake, invasion and
   hole size are part of the measurement.
9. **Forgetting the induced activity.** A neutron source activates the tool, the
   borehole and the formation; the dosimetry is not an afterthought.
10. **Quoting a log value without the tool model and calibration.** The API
    conventions are defined against physical standards, and a bare number is
    meaningless.

## 12. Real-world applications

- **Porosity and lithology interpretation.** The density–neutron–Pe suite is the
  standard petrophysical triple, and its logic is the logic of this lesson: three
  measurements from two particles, solved simultaneously
  ([05-08-04 Density, Neutron and Sonic Porosity Logs](../../05-core-geophysics/08-geophysical-logging/04-porosity-logs.md)).
- **Gas detection.** The divergence of the density and neutron readings in a
  gas-bearing interval is one of the most-used qualitative indicators in the
  industry.
- **Salinity and water saturation.** The chlorine log, and the pulsed-neutron
  capture measurement, give formation-water salinity and saturation independent of
  resistivity.
- **Neutron shielding and dosimetry.** Moderation plus absorption is the design
  principle, and the same cross sections give the dose rate
  ([06](./06-dosimetry.md)).
- **Neutron activation for geochemistry and for flow.** The same reaction
  physics in a laboratory or behind casing.
- **Planetary neutron spectroscopy.** Orbital neutron instruments map hydrogen
  (as water ice) on Mars and the Moon using the moderating power of hydrogen —
  this lesson's §2 at a planetary scale.

## 13. Further reading

- **Ellis, D. V., & Singer, J. M. *Well Logging for Earth Scientists*
  (Springer).** The standard reference for nuclear logs, with the tool responses,
  the calibration standards and the environmental corrections. Level: graduate.
- **Serra, O. *Fundamentals of Well-Log Interpretation* (Elsevier).** The
  petrophysical interpretation view, including the density–neutron–Pe
  cross-plots. Level: professional.
- **Knoll, G. F. *Radiation Detection and Measurement* (Wiley).** Detector
  physics for the neutron detectors themselves. Level: graduate.
- **Lamarsh, J. R., & Baratta, A. J. *Introduction to Nuclear Engineering*
  (Prentice Hall).** Where $\xi$, the moderating ratio and diffusion theory are
  derived properly, and the standard source for the formulas of §2 and §3.
  Level: advanced.
- **Mughabghab, S. F. *Atlas of Neutron Resonances* (Elsevier).** The evaluated
  thermal cross sections and resonance parameters used as tabulated inputs here.
  Level: reference. Confirm the current edition.
- **IAEA, *Radiation Protection in the Oil and Gas Industry* and the associated
  NORM guidance.** For the induced-activity and source-handling constraints on
  nuclear logging. Level: professional reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 14. Related lessons

- [03 Interaction of Radiation with Matter](./03-radiation-interaction.md) — the
  charged-particle and photon cases that this lesson contrasts with.
- [04 Gamma-Ray Spectrometry and Natural Radioelements](./04-gamma-spectrometry.md)
  — the natural-gamma log and the detector principles shared here.
- [06 Dosimetry, Radiation Safety and Regulatory Limits](./06-dosimetry.md) — the
  source handling and induced-activity constraints.
- [02-09-01 Atomic Structure and Energy Levels](./01-atomic-structure.md) — the
  atomic physics behind the capture gamma rays and the photoelectric factor.
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../05-thermodynamics/06-geotherms.md)
  — the thermal context of a borehole measurement.
- [05-08-01 The Borehole Environment and Invasion Profiles](../../05-core-geophysics/08-geophysical-logging/01-borehole-environment.md)
  — the environmental corrections this lesson assumes are available.

Exercises:
[`exercises/05-neutron-interaction-exercises.md`](./exercises/05-neutron-interaction-exercises.md)
and
[`exercises/05-neutron-interaction-solutions.md`](./exercises/05-neutron-interaction-solutions.md).

## Self-assessment checklist

- [ ] I can explain why a neutron has no Coulomb barrier and what that implies
      for shielding. (§1)
- [ ] I can compute the 2200 m/s energy and the Maxwellian mean and say which
      convention a cross section uses. (§1)
- [ ] I can derive the maximum fractional energy loss $4A/(1+A)^2$ and the
      average logarithmic decrement, and compute the collisions to thermalise.
      (§2)
- [ ] I can compute a macroscopic cross section and a mean free path, with the
      barn conversion correct. (§3, §9)
- [ ] I can define and compute a moderating ratio, and explain why heavy water
      beats light water. (§2)
- [ ] I can compute a hydrogen index and derive the gas effect on the density and
      neutron porosity logs. (§4)
- [ ] I can compute the electron density index and Pe from a mineral formula, and
      state the definition dependence. (§5)
- [ ] I can derive the chlorine capture share from $\Sigma = N\sigma$. (§6)
- [ ] I can say which of these numbers are tabulated, which are model inputs and
      which are tool conventions, and name the compilation. (§8, §13)
