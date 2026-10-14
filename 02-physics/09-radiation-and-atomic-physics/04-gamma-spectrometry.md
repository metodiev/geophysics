---
id: 02-09-04
title: "Gamma-Ray Spectrometry and Natural Radioelements"
level: advanced
prereqs: ["02-09-02", "02-09-03", "02-01-02"]
estimated_minutes: 90
tags: [gamma-spectrometry, nai, hpge, airborne-survey, radiogenic-heat, stripping]
---

# Gamma-Ray Spectrometry and Natural Radioelements

A gamma-ray spectrometer measures three things about the ground beneath it, and
it is worth being blunt about which measurement is which. It measures the
**count rate** in each of three energy windows, which through a calibration
becomes the **concentration** of potassium, uranium and thorium. The
concentrations are not what the instrument reports directly, and the conversion
involves two things that are easy to forget: a **secular-equilibrium
assumption** for the two chains, and a **depth of investigation** of a few tens
of centimetres. A radiometric map is therefore a map of the topsoil, not of the
rock, and it is a map of assumed equilibrium, not of the elements themselves.

This lesson builds the instrument response, the three-window inversion that
turns count rates into concentrations, the depth of investigation derived from
the attenuation coefficients of lesson 03, and the conversion of concentrations
into **radiogenic heat production** — which is the quantity that makes
radiometric mapping matter to geodynamics and not only to mineral exploration.

Two warnings about numbers, applied throughout. The **detector parameters** used
here — energy resolution, efficiency, the overlap between windows — are declared
model inputs, because they belong to a particular instrument and nothing about
them is universal. The **half-lives, abundances and heat-generation
coefficients** are tabulated, differ between compilations, and must be cited. The
demo's output labels every one of them.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why energy resolution improves in relative terms as the square
   root of energy, and compute the FWHM of a line from one calibration point.
2. **Identify** every feature of a NaI gamma-ray spectrum — photopeak, Compton
   continuum, Compton edge, backscatter peak, annihilation line, escape peaks,
   daughter K X-rays — and say where each comes from.
3. **Derive** the Compton continuum's shape from the Klein–Nishina distribution,
   and explain why it is nearly flat in deposited energy up to the edge.
4. **Compute** the specific activity of natural K, U and Th per unit
   concentration and compare it with the published survey conversion factors.
5. **Derive** the three-window stripping equations, invert them, and quantify how
   an error in one stripping coefficient propagates.
6. **Derive** the depth of investigation from the attenuation coefficient and
   compute it for each of the three natural radioelements.
7. **Compute** a radiogenic heat production from K, U and Th concentrations, and
   cross-check the conversion coefficients against the specific activities.
8. **State** which quantities in a radiometric survey are measured, which are
   model inputs, and which are tabulated, and cite the tabulated ones.

## Prerequisites

- [02-09-02 Radioactive Decay, Half-Life and Dating](./02-radioactive-decay.md) —
  chain equilibrium, activity, and why one line reports a whole series.
- [02-09-03 Interaction of Radiation with Matter](./03-radiation-interaction.md) —
  the attenuation coefficients, the Compton edge and the depth of investigation.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](../01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
  — a count rate without a counting time and a background is not a measurement.

## 1. Detectors, resolution and why resolution scales as $1/\sqrt E$

Two detector types dominate the subject, and the difference between them decides
which questions can be answered.

**Scintillation detectors (NaI(Tl)).** A gamma ray deposits energy in a thallium-
doped sodium iodide crystal, which emits light in proportion to the energy
deposited. A photomultiplier tube converts the light into an electrical pulse.
The detector is dense and cheap enough to build in large volumes, which is what
airborne surveying needs. Its weakness is resolution.

**Semiconductor detectors (HPGe).** A gamma ray creates electron–hole pairs in
germanium; the number of pairs is proportional to the deposited energy and is
much larger than the number of photoelectrons in a scintillator. The statistical
limit on the resolution is therefore much better. High-purity germanium delivers
0.2 to 0.3 per cent FWHM at 1 MeV against several per cent for NaI, and it must
be cooled to liquid-nitrogen or mechanical temperatures to suppress thermal
leakage current. It is the detector for identifying lines; NaI is the detector
for counting them quickly.

**Why the resolution improves with energy.** Energy resolution is limited by the
statistics of the carrier generation. If a deposit of energy $E$ creates on
average $\bar N = E/w$ carriers of a fixed quantum $w$, then

$$\frac{\sigma_E}{E} = \frac{\sqrt{F\bar N}}{\bar N}
= \sqrt{\frac{Fw}{E}} \quad\Longrightarrow\quad
\mathrm{FWHM} = 2.355\,\sigma_E = 2.355\,E\sqrt{\frac{Fw}{E}}, \tag{1}$$

where $F$ is the Fano factor, a number less than one that expresses the fact
that the generation events are not independent. In relative terms
$\mathrm{FWHM}/E \propto 1/\sqrt E$: the resolution gets *better* with energy,
which is why the potassium line at 1.46 MeV is resolved better than the caesium
line at 662 keV, and why the thorium line at 2.61 MeV is resolved best of all.

The practical form of (1), used in the demo, is to fit one constant to one
measured point. With a NaI detector specified as 7.00 per cent FWHM at 662 keV:

```text
  662 keV line: FWHM = 46.3 keV, sigma = 19.68 keV
    at   662.0 keV: FWHM =   46.3 keV ( 7.00 per cent)
    at  1460.8 keV: FWHM =   68.8 keV ( 4.71 per cent)
    at  2614.5 keV: FWHM =   92.1 keV ( 3.52 per cent)
```

The absolute width grows with energy while the relative width shrinks. The
consequence that matters for a survey is quantitative: at 92 keV FWHM, a NaI
detector cannot separate the 583 keV line of $^{208}$Tl from the 609 keV line of
$^{214}$Bi, so the two series' lines must be chosen far apart — which is exactly
why the standard windows are at 1.76 and 2.61 MeV.

## 2. What a spectrum actually contains

A gamma-ray spectrum is a record of deposited energy, and every feature in it
has an identifiable origin. Reading the list in order of energy is the fastest
way to learn it.

| Feature | Energy | Origin |
|---|---|---|
| K X-rays of the daughter | 10–90 keV | Atomic relaxation after internal conversion or electron capture |
| Lead K X-rays (shield) | 75–85 keV | The same, in the shield |
| Photopeak of a line | $E_\gamma$ | Full energy deposition, usually by several interactions |
| Compton continuum | 0 to $E_\mathrm{edge}$ | One or more Compton scatters with the electron escaping |
| Compton edge | $E_\mathrm{edge} = E_\gamma^2/(m_ec^2 + 2E_\gamma)$ | Maximum energy transferable in a single scatter |
| Backscatter peak | $\approx 200$–255 keV | Compton scattering in the material around the detector |
| Annihilation line | 511 keV | Positron annihilation (in pair production, or a $\beta^+$ emitter) |
| Single-escape peak | $E_\gamma - 511$ keV | One annihilation photon escapes (lines above 1.022 MeV) |
| Double-escape peak | $E_\gamma - 1022$ keV | Both annihilation photons escape |

The two features most often misidentified are the backscatter peak and the
escape peaks. Neither is a line from the source. The backscatter peak's position
is a property of the scattering geometry and the electron mass — it tends to
$m_ec^2/2 = 255.5$ keV as the incident energy rises, so a peak near 200 keV in a
spectrum recorded through a wall is not evidence of a 200 keV emitter. Escape
peaks appear only above 1.022 MeV and are always 511 or 1022 keV below a real
line of the same nuclide; a thorium-series spectrum therefore shows the 2614.5
keV line with a 2103 keV single-escape companion, and the ratio of the two peak
areas is an efficiency measurement.

**The Compton continuum.** The demo computes the deposited-energy distribution
by mapping the Klein–Nishina angular distribution onto electron energy, and the
result is nearly flat from zero up to the Compton edge:

```text
   205.2 keV |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
   244.9 keV |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
   350.9 keV |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
   470.0 keV |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
   483.3 keV |------------------------------|
   496.5 keV |                              |
```

The flatness is not an accident and it is worth understanding: a uniform
distribution of *scattering angles* produces a non-uniform distribution of
recoil energies, and the two effects combine to give a plateau in electron
energy. The sharp upper terminus is the Compton edge at 477.65 keV for a 662 keV
photon ([03](./03-radiation-interaction.md) §2.2). Because the continuum carries
a large fraction of the total counts, the chance of a 662 keV photon depositing
its full energy in a small detector is modest — the **peak-to-total ratio**,
typically 0.2 to 0.4 for NaI at that energy. Everything that is not in the
photopeak is background in the sense of not carrying the line's full energy, and
it is partly for that reason that low-energy windows in a survey are harder to
interpret than high-energy ones.

**Calibration.** Convert channel numbers to energy with two or more known lines.
A caesium-137 source gives 661.7 keV and potassium-40 gives 1460.8 keV; those
two points fix a straight line, and thorium series lines above 2.6 MeV check the
linearity. Gain drift with temperature is the dominant systematic in a
field instrument, and the potassium peak itself is the standard *in-situ*
reference because potassium is present nearly everywhere.

## 3. From count rate to concentration: the three windows

Three energy windows are conventional, chosen around lines that are strong,
well-separated and unambiguous:

| Window | Range (TABULATED convention) | Line |
|---|---|---|
| K | 1.37–1.57 MeV | $^{40}$K at 1460.8 keV |
| U | 1.66–1.86 MeV | $^{214}$Bi at 1764.5 keV ($^{238}$U series) |
| Th | 2.41–2.81 MeV | $^{208}$Tl at 2614.5 keV ($^{232}$Th series) |

Only the potassium window is dominated by a single line. The uranium window sits
inside the Compton continuum of the 2614.5 keV thorium line, and the potassium
window sits inside the continuum of both. Counting a window therefore does not
count an element, and the overlap must be removed. With $\alpha$ the thorium
contribution to the uranium window, $\beta$ the thorium contribution to the
potassium window and $\gamma$ the uranium contribution to the potassium window,

$$c_\mathrm{Th} = t_\mathrm{Th}, \qquad
c_\mathrm{U} = t_\mathrm{U} + \alpha t_\mathrm{Th}, \qquad
c_\mathrm{K} = t_\mathrm{K} + \beta t_\mathrm{Th} + \gamma t_\mathrm{U}, \tag{2}$$

a lower-triangular system that inverts from the top down. The demo uses
$\alpha = 0.36$, $\beta = 0.52$, $\gamma = 0.74$ as **declared model
coefficients** — the real values are instrument- and geometry-specific and are
determined by flying over calibration pads of known composition:

```text
  True counts: {'K': 850.0, 'U': 420.0, 'Th': 260.0}
  Measured   : K=1296.0, U=513.6, Th=260.0
  Stripped   : K=850.000000, U=420.000000, Th=260.000000
  Recovery error: 0.00e+00, 0.00e+00, 0.00e+00 counts
```

Exact recovery verifies the inverse. The interesting question is what happens
when the coefficients are wrong, which they always slightly are:

```text
perturbed        K recovered   U recovered  Th recovered    K error
alpha +1%             850.69        419.06        260.00       0.69
beta +1%              848.65        420.00        260.00      -1.35
gamma +1%             846.89        420.00        260.00      -3.11
all +1%               846.24        419.06        260.00      -3.76
```

Thorium is untouched by construction, because it is the last window and nothing
is subtracted from it. Uranium moves only when $\alpha$ moves. Potassium absorbs
every error, being at the bottom of the sequential subtraction. The matrix itself
is well conditioned — the infinity-norm condition number of the triangular
stripping matrix is 4.51, computed in the demo — so the limiting factor in a real
survey is not the linear algebra but the **counting statistics** of a low-count
thorium window, and the accuracy of the calibration pads.

**Concentration conversion.** The stripped count rates are converted to
concentrations through sensitivities obtained from the calibration pads, and the
concentrations are reported as per cent K, ppm equivalent uranium (eU) and ppm
equivalent thorium (eTh). The word "equivalent" is the honest part of the
notation: a spectrometer measures a gamma line, not an element, and the
conversion assumes secular equilibrium.

## 4. Depth of investigation, derived

A gamma ray emitted at depth $z$ must escape to be counted, and it is attenuated
along the way. For a plane-parallel geometry the emergent flux from depth $z$ is
proportional to $\exp(-\mu z)$, so the fraction of the total signal originating
above depth $d$ is

$$F(d) = 1 - e^{-\mu d} \quad\Longrightarrow\quad
z(f) = -\frac{\ln(1-f)}{\mu}. \tag{3}$$

$\mu$ comes from the Compton cross section at the line energy and the soil
density; the demo computes it and takes the 90 per cent depth:

```text
series      line (keV)  mu/rho (cm2/g)  mu (1/cm)  z(0.5) (cm)  z(0.9) (cm)
K               1460.8         0.05230    0.08369         8.28        27.51
U (Bi-214)      1764.5         0.04720    0.07552         9.18        30.49
Th (Tl-208)      2614.5         0.03761    0.06018        11.52        38.26
```

Three things follow, and all three are standard practice:

1. **The quoted "top 30 cm" is one window and one soil density.** It is the
   potassium $z(0.9)$ entry. The thorium window reaches 40 per cent deeper, and a
   wet or snow-covered soil shortens all three.
2. **Moisture and snow change the window *ratios* without changing the
   concentrations.** Water attenuates the low-energy windows more than the
   high-energy ones, so rain moves the K/Th and U/Th ratios. Every airborne
   survey needs a height and moisture correction, and comparing two surveys
   flown in different weather is a comparison of weather unless the correction is
   documented.
3. **Radon escape moves the uranium window independently of uranium.** $^{222}$Rn
   is a gas and escapes from the top few metres, breaking the equilibrium between
   $^{226}$Ra and the rest of the chain. A radiometric uranium anomaly is
   therefore a *lead*, not an assay, and confirming it means measuring more than
   one chain member.

The model used for $\mu$ is Compton-only and is therefore an underestimate,
exactly as in lesson 03: the photoelectric term matters at the low end, so the
absolute depths are model values. The **ratios** between the three elements are
insensitive to that omission, and the ratios are what a survey compares.

## 5. Radiogenic heat production from K, U and Th

Radiometric mapping matters beyond mineral exploration because U, Th and K are
what heat the crust. The standard conversion is a bracketed coefficient form,

$$A\ [\mu\mathrm{W\,m^{-3}}] = \rho\,[\mathrm{kg\,m^{-3}}] \times 10^{-5}
\times \left(9.52\,C_\mathrm{U} + 2.56\,C_\mathrm{Th} + 3.48\,C_\mathrm{K}\right),
\tag{4}$$

with $C_\mathrm{U}$ and $C_\mathrm{Th}$ in ppm and $C_\mathrm{K}$ in per cent.
The coefficients are **tabulated** and differ slightly between compilations;
state the one you use. Applying (4):

```text
rock                   rho    K %   U ppm  Th ppm   A (uW/m3)
granite               2650   3.50    4.00   15.00      2.3495
basalt                2900   1.00    0.60    2.40      0.4447
shale                 2400   3.00    3.70   12.00      1.8332
limestone             2600   0.30    2.00    1.70      0.6353
quartz sand           1650   0.50    0.50    1.00      0.1495
mantle peridotite     3300   0.02    0.02    0.08      0.0153
```

These are the right orders of magnitude: a granite with 3.5 % K, 4 ppm U and
15 ppm Th is a hot granite at 2.3 µW m⁻³, the mantle is two orders of magnitude
lower, and the
[constant handbook](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
quotes a crustal radiogenic heat production of about 1 µW m⁻³ with a range of
0.1 to 5.

**The coefficients can be checked, and should be.** The coefficient for an
element divided by its specific activity per unit concentration returns the
average energy deposited per decay, which must be a physical number. The demo
computes it:

```text
element     A_s (Bq/kg per unit)  implied energy/decay (MeV)
U                        12.3472                      48.124
Th                        4.0573                      39.381
K                       317.1654                       0.685
```

The uranium figure is of order 50 MeV per decay, which is right for a series
emitting eight alpha particles of a few MeV each plus betas and gammas; thorium
is of order 40 MeV for six alphas; potassium is 0.7 MeV, the average energy
retained per $^{40}$K decay once the escaping 1.46 MeV gamma and the always-
escaping neutrino are removed. Three numbers of the right order, from three
independent tabulated half-lives and three tabulated coefficients, is the
consistency check. It is not a proof — a coefficient and a half-life could be
wrong in compensating ways — but a coefficient wrong by a factor of ten would
show here immediately.

**Which element dominates.** Per kilogram of the element itself:

```text
element     A_s (Bq per kg)  energy/decay (MeV)   heat (W/kg)
U                1.2347e+07              48.124    9.5200e-05
Th               4.0573e+06              39.381    2.5600e-05
K                3.1717e+04               0.685    3.4800e-09

  Natural uranium generates 27356 times more heat
  per kilogram than natural potassium
```

Because uranium is 27 000 times more productive per kilogram, its contribution
depends entirely on the concentration ratio. In the granite row above the three
terms contribute 43.0 per cent (U), 43.3 per cent (Th) and 13.7 per cent (K). The
lesson is not which element wins but that a single "radiogenic heat production"
number hides the fact that three elements are measured separately, decay at
different rates, and can be in or out of equilibrium independently.

## 6. Physical interpretation

**The measurement is a shallow, integral one.** A radiometric survey averages the
top few tens of centimetres over a footprint that is tens to hundreds of metres
across from an aircraft. It responds to soil, not rock, and it responds to
whatever has happened to the soil — weathering, eluviation, contamination,
agriculture. This is why radiometric anomalies are *broad* relative to the
structures that cause them and why they correlate with landscape and vegetation
maps.

**The windows are a three-channel inversion with an assumption built in.** Two of
the three measured activities belong to decay chains, so the inversion from
count rate to concentration contains a physical assumption (secular equilibrium)
as well as a calibration. This is a different kind of assumption from the
stripping coefficients: the stripping is instrumental and can be calibrated, and
the equilibrium is geological and must be argued.

**Heat production is the bridge to geodynamics.** Equation (4) is what makes a
radiometric map an input to a thermal model rather than a curiosity. Crustal heat
production is a first-order control on crustal temperature, on the depth of the
brittle–ductile transition, on metamorphic grade, and on whether a granite
intrusion generates a hydrothermal system. The mapping is a proxy for the
geophysics, not an end in itself.

## 7. Assumptions and regime of validity

1. **Secular equilibrium for the U and Th series.** Broken by radon loss,
   uranium-series disequilibrium in young rocks, and by industrial redistribution.
   The measurement is an activity, the reported quantity is eU/eTh, and the
   difference is an assumption.
2. **A single calibration valid over a survey area.** Sensitivities depend on
   detector geometry, altitude, temperature and the spectral shape of the
   background. An airborne survey is a set of overlapping strips, each with its
   own calibration and its own levelling correction.
3. **A homogeneous half-space.** The $z(f)$ formula of §4 assumes a uniform soil;
   a layered or overhanging geometry changes the effective depth. So does a lot
   of snow, which is a low-density layer and therefore surprisingly transparent in
   mass-thickness terms.
4. **Declared detector parameters.** Resolution, peak-to-total and stripping
   ratios are model inputs here. In a report they are instrument specifications
   and calibration results, and they must be given.
5. **Tabulated nuclear data.** Half-lives, abundances and heat-generation
   coefficients differ between compilations. The specific activities computed here
   are 12.3472 Bq/kg per ppm of U, 4.0573 Bq/kg per ppm of Th and 317.17 Bq/kg
   per per cent of K, against widely quoted factors of 12.4, 4.1 and 313. A 1 to
   2 per cent discrepancy is what honest compilation differences look like;
   state which values you used.
6. **Line energies and yields.** The window definitions and the line energies in
   this lesson are conventional values. Confirm them in the current evaluated
   nuclear data before using them to define a calibration.

## 8. Units and dimensional analysis

| Quantity | Unit | Note |
|---|---|---|
| Count rate | s⁻¹ or cps | Per second per channel or per window |
| Window sensitivity | cps per % K, cps per ppm eU/eTh | Instrument and geometry specific |
| Concentration | % K, ppm U, ppm Th | Mass fractions; 1 % = 10⁴ ppm |
| Specific activity | Bq kg⁻¹ per unit concentration | From $\lambda N_A/M$ |
| Stripping coefficients | dimensionless ratios | Window overlaps |
| Depth of investigation | cm or g cm⁻² | Mass depth is the portable one |
| Heat production | µW m⁻³ | Equivalently µW per kg × density |

Three checks.

**The conversion factor.** 1 ppm is a mass fraction of $10^{-6}$, so per
kilogram of rock it is $10^{-6}$ kg of the element, i.e. $10^{-3}$ g. With
$N = N_A/238.03$ atoms per gram and $\lambda = 4.915\,960 \times 10^{-18}$ s⁻¹,
the activity is 12.3472 Bq per kg of rock. Every step is a unit conversion and
all of them are checkable. Note also that 1 ppm = 1 µg g⁻¹ = 1 mg kg⁻¹, which is
the same number and is why geochemists use ppm and g t⁻¹ interchangeably.

**Activity versus concentration.** A count rate is per second; a concentration is
a mass fraction. The bridge is a specific activity, which carries s⁻¹, and a
sensitivity, which is a count rate per unit concentration. A sensitivity quoted
without its units — "0.9 for potassium" — is unusable; the unit is the whole
content of the statement.

**The window overlap is dimensionless.** $c_\mathrm{K} = t_\mathrm{K} + \beta
t_\mathrm{Th} + \gamma t_\mathrm{U}$ is only consistent if $\beta$ and $\gamma$
are ratios of count rates in the same units. If one coefficient is derived from
an experiment in counts per minute and another in counts per second, the
inversion is wrong by the ratio, and the resulting concentrations look plausible
and are not.

## 9. Python demonstration

[`code/gamma_spectrometry_demo.py`](./code/gamma_spectrometry_demo.py) computes
the specific activities of K, U and Th, builds a synthetic NaI spectrum with its
Compton continuum, inverts the three-window stripping system and perturbs the
coefficients, computes the radiogenic heat production with its consistency check,
and computes the depth of investigation for each window. Detector parameters are
labelled MODEL, nuclear data TABULATED, and computations COMPUTED, in the output
itself.

The conversion factors, which are the numbers a survey report quotes:

```text
nuclide      concentration    N (atoms/kg)     A (Bq/kg)
238U               1 ppm U    2.511649e+18       12.3472
235U           1 ppm nat U    1.821603e+16        0.5685
232Th             1 ppm Th    2.595329e+18        4.0573
40K                  1 % K    1.802100e+19      317.1654
```

### What to observe

- The computed factors differ from the widely quoted 12.4, 4.1 and 313 by 1 to
  2 per cent. That difference is the compilation difference in the half-lives and
  abundances and nothing else; it is the reason a conversion factor must be
  recomputed rather than copied ([02](./02-radioactive-decay.md) §7).
- The stripping inversion is exact on clean data and amplifies a 1 per cent
  coefficient error into a 0.4 per cent error in potassium. The condition number
  is 4.5, so the linear algebra is not the problem; the counting statistics of a
  low-count window are.
- The heat-production coefficients imply 48.1 MeV per $^{238}$U decay and
  0.685 MeV per $^{40}$K decay, both physically sensible. This cross-check is the
  one that catches a wrong coefficient.
- The depth of investigation is 27.5 cm for potassium, 30.5 cm for uranium and
  38.3 cm for thorium, so the three windows sample genuinely different depths
  and respond differently to moisture.

## 10. Common mistakes

1. **Reporting eU as uranium.** It is a chain activity converted through an
   equilibrium assumption. Disequilibrium is common and is the interesting
   geochemistry.
2. **Comparing surveys with different window definitions, heights or moisture
   corrections.** The count rates are then not comparable, regardless of how
   well each survey was flown.
3. **Treating the backscatter peak or an escape peak as a source line.** Their
   energies are set by electron mass and detector geometry.
4. **Quoting a detection limit without a counting time and background.** A count
   rate has a Poisson uncertainty; a limit without it is a guess
   ([06](./06-dosimetry.md) §5).
5. **Assuming the sensitivity is a property of the element.** It is a property of
   the instrument, the geometry and the spectrum.
6. **Confusing the depth of investigation for the three windows.** They differ by
   40 per cent, and the low-energy windows are the ones that a centimetre of
   snow changes.
7. **Using a heat-production coefficient without checking it against a specific
   activity.** The check is two lines of arithmetic and it catches a factor of
   ten.
8. **Forgetting that a radiometric anomaly in a soil-covered area maps the soil.**
   A K anomaly over granite can be a weathering product, not the granite.
9. **Treating the potassium peak as fixed.** Gain drift moves it, and the peak
   channel is the instrument's own check on itself.
10. **Quoting a concentration to three significant figures from a one-second
    count.** The uncertainty is $\sqrt N/N$ and for a thorium window that is often
    per cent-level at best.

## 11. Real-world applications

- **Airborne radiometric surveying.** Regional K, eU and eTh maps for mineral
  exploration, geological mapping and environmental baseline. The three-window
  inversion and the height correction of §3 and §4 are the entire data-reduction
  chain, and the results feed alteration mapping and prospectivity analysis
  ([11-02-05 Radiometrics and Alteration Mapping](../../11-exploration-geophysics/02-mineral-exploration/05-radiometrics-for-minerals.md)).
- **Ground and borehole gamma logging.** The same physics with a different
  geometry: a natural-gamma log is a clay and potassium indicator, and the
  spectral version separates K, U and Th in the borehole
  ([05-08-02](../../05-core-geophysics/08-geophysical-logging/02-gamma-logging.md)).
- **Environmental monitoring.** Mapping of NORM, of legacy mining contamination
  and of the distribution of caesium-137 from atmospheric fallout — all with the
  same windows and the same assumptions, and all needing the equilibrium caveat
  ([10-05-04](../../10-gpr-near-surface/05-other-near-surface-methods/04-nuclear-and-radiometric-nearsurface.md)).
- **Heat-flow and geodynamic modelling.** Equation (4) is the input, and the
  crustal heat production is a first-order control on crustal temperature and
  metamorphism ([02-05-06 Geotherms](../05-thermodynamics/06-geotherms.md)).
- **Radon hazard assessment.** A uranium anomaly in soil is a radon source, and
  the disequilibrium between $^{226}$Ra and $^{222}$Rn is exactly what makes the
  mapping difficult and necessary ([06](./06-dosimetry.md)).
- **Planetary science.** Gamma-ray and neutron spectrometers in orbit measure
  surface K, Th, U, Fe and hydrogen with the same three-window logic and the same
  equilibrium caveats, at a depth of tens of centimetres.

## 12. Further reading

- **IAEA, *Guidelines for Radioelement Mapping Using Gamma Ray Spectrometry
  Data* (TECDOC series).** The standard practical reference for airborne
  spectrometry: windows, stripping ratios, calibration pads, height correction
  and levelling. Level: professional reference. Confirm the current edition.
- **IAEA, *Airborne Gamma Ray Spectrometer Surveying* (Technical Reports
  Series).** The complementary operational document. Level: professional
  reference.
- **Knoll, G. F. *Radiation Detection and Measurement* (Wiley).** Detector
  physics, resolution, efficiency and spectrum interpretation. Level: graduate.
- **Rybach, L. (1988). Determination of heat production rate. In *Handbook of
  Terrestrial Heat Flow Density Determination*.** The origin of the coefficient
  form in equation (4), with the alternative sets of coefficients that have been
  used. Level: graduate.
- **Bodó, B., & others on NORM and environmental spectrometry** — the applied
  literature on mapping artificial and natural radionuclides in the environment,
  including the caesium-137 fallout applications. Level: advanced.
- **NNDC, *ENSDF/NuDat* evaluated nuclear structure data.** Line energies,
  intensities and branching ratios; confirm the current evaluation. Level:
  reference.
- **IUPAC, *Isotopic Compositions of the Elements* (current report).** The
  abundances behind every conversion factor in §3. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [02 Radioactive Decay, Half-Life and Dating](./02-radioactive-decay.md) — the
  equilibrium assumption, and the specific-activity arithmetic used throughout.
- [03 Interaction of Radiation with Matter](./03-radiation-interaction.md) — the
  Compton continuum, the escape peaks and the attenuation coefficient.
- [05 Neutron Interactions and Borehole Nuclear Measurements](./05-neutron-interaction.md)
  — the other nuclear log, and the detector that shares its calibration logic.
- [06 Dosimetry, Radiation Safety and Regulatory Limits](./06-dosimetry.md) —
  counting statistics, detection limits and the radon problem.
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../05-thermodynamics/06-geotherms.md)
  — where the heat production of §5 is used.
- [26-02-03 Physical Constants and Earth Parameters with Sources](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the crustal heat-production anchor used to sanity-check §5.
- [11-02-05 Radiometrics and Alteration Mapping](../../11-exploration-geophysics/02-mineral-exploration/05-radiometrics-for-minerals.md)
  — the exploration interpretation of the maps this lesson produces.

Exercises:
[`exercises/04-gamma-spectrometry-exercises.md`](./exercises/04-gamma-spectrometry-exercises.md)
and
[`exercises/04-gamma-spectrometry-solutions.md`](./exercises/04-gamma-spectrometry-solutions.md).

## Self-assessment checklist

- [ ] I can explain why $\mathrm{FWHM}/E \propto 1/\sqrt E$ and compute a line
      width from one calibration point. (§1)
- [ ] I can identify every feature in a gamma-ray spectrum and say where it comes
      from. (§2)
- [ ] I can explain why the Compton continuum is flat up to the edge. (§2)
- [ ] I can compute a specific activity per ppm or per % and compare it with a
      published conversion factor. (§3, §8)
- [ ] I can write and invert the three-window stripping system, and say which
      element absorbs an error in which coefficient. (§3)
- [ ] I can derive the depth of investigation and compute it for the three
      windows. (§4)
- [ ] I can explain how moisture and radon break the survey assumptions. (§4)
- [ ] I can compute a heat production from K, U and Th and cross-check the
      coefficients against specific activities. (§5)
- [ ] I can state which numbers in this lesson are measured, which are model
      inputs and which are tabulated. (§7)
- [ ] I can name the compilation I would use for the nuclear data and for the
      heat-generation coefficients. (§12)
