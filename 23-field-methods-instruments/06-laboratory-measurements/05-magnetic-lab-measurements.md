---
id: 23-06-05
title: "Laboratory Magnetic Susceptibility and Remanence (IRM, ARM)"
level: research
prereqs: ["23-06-01", "23-03-02"]
estimated_minutes: 115
tags: [laboratory, magnetics, susceptibility, remanence, IRM, ARM, rock-magnetism]
---

# Laboratory Magnetic Susceptibility and Remanence (IRM, ARM)

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** between SI and cgs susceptibility, and between volume- and
   mass-specific values, and **state** the two bases a quoted number needs.
2. **Explain** why an apparent susceptibility depends on the measuring field amplitude,
   and **compute** the dependence for a given suppression field.
3. **Evaluate** a log-Gaussian IRM acquisition curve and **compute** an S-ratio for a
   two-component mixture.
4. **Interpret** an ARM susceptibility ratio as a grain-size proxy, and **state** what it
   separates that SIRM alone cannot.
5. **Compute** the holder-background error and the minimum specimen size for a tolerance.
6. **State** which magnetic quantities are intrinsic and which are measurement-dependent.

All susceptibilities, remanences, coercivities and holder volumes here are **SYNTHETIC**
teaching values combined with the standard relations quoted in the text (the mass and
volume definitions of susceptibility, the $\kappa_{\text{SI}} = 4\pi\kappa_{\text{cgs}}$
conversion, the log-Gaussian IRM acquisition law, the S-ratio, the ARM ratio, the
holder-background correction). No instrument specification or measured rock property is
reproduced.

## Prerequisites

- [01 Sample Preparation, Coring and Drying Protocols](01-sample-preparation.md) —
  the specimen masses and volumes every magnetic measurement is normalized by.
- [23-03-02 Magnetic Fieldwork: Base Stations, Diurnal Variation and Gradients](../03-gravity-magnetic-fieldwork/02-magnetic-fieldwork.md) —
  the field measurements these laboratory values are used to interpret.

## 1. Intuition: three magnetic measurements, three different things

Rock magnetism in the laboratory is three measurements that are often confused:

| Measurement | What is applied | What is measured | What it reveals |
|---|---|---|---|
| Susceptibility | a small alternating field (a few to a few hundred A/m) | the *induced* magnetization | the amount of magnetic material, and its grain size when combined with others |
| IRM (isothermal remanent magnetization) | a steady field, then switched off | the *remaining* magnetization | the coercivity spectrum: which minerals can carry remanence |
| ARM (anhysteretic remanence) | a steady bias field superposed on a decaying alternating field | the remanence acquired in the bias field | the fine, single-domain-like fraction, which is the palaeomagnetic carrier |

The three are not interchangeable, and the reason is that a rock's magnetic
mineralogy has at least three independent properties — *how much*, *what kind* and *what
grain size* — and each measurement mixes them differently. That is why the standard
laboratory practice is to measure a **suite**: susceptibility, IRM acquisition, back-field
demagnetization, ARM and often temperature dependence, then interpret the set jointly. A
single susceptibility number identifies almost nothing.

## 2. Susceptibility: which number is being quoted?

The SI volume susceptibility $\kappa$ is dimensionless; the mass-specific value divides by
density, and the cgs system differs by $4\pi$:

$$\chi_{\text{mass}} = \frac{\kappa}{\rho}, \qquad
\kappa_{\text{cgs}} = \frac{\kappa_{\text{SI}}}{4\pi}, \qquad
\chi_{\text{cgs,mass}} = \frac{\kappa_{\text{cgs}}}{\rho[\mathrm{g/cm^{3}}]} .$$

For a synthetic $\kappa = 1.0\times10^{-3}$ and $\rho = 2650$ kg/m³ (and a bridge
calibrated at a synthetic 2.0 mV per unit SI $\kappa$, giving 2.0000 mV):

| Quantity | Value |
|---|---|
| mass-specific $\chi$ | $3.7736\times10^{-7}$ m³/kg |
| $\kappa_{\text{cgs}}$ | $7.9577\times10^{-5}$ emu/cm³ |
| $\chi_{\text{cgs,mass}}$ | $3.0029\times10^{-5}$ cm³/g |
| error if the $4\pi$ is omitted | a factor of **12.57** |

Two bases must therefore be stated for every susceptibility: the **system** (SI or cgs) and
the **normalization** (per volume or per mass). A number quoted as "0.001" without them is
ambiguous by a factor of 12.57 *and* by the density — and rock-magnetic literature still
contains both systems, so the confusion is not hypothetical.

## 3. Field dependence: the measurement is not intrinsic

Susceptibility is measured in an alternating field whose amplitude the instrument chooses.
For an ideal paramagnetic or diamagnetic material the response is linear and the amplitude
does not matter. For a rock containing ferrimagnetic grains it matters a great deal,
because the grains' response saturates: a synthetic model
$\kappa_{\text{app}} = \kappa_0/(1 + H/H_s)$ with $H_s = 200$ A/m gives

| Measuring field $H$ | $\kappa_{\text{app}}$ | Ratio to $\kappa_0$ |
|---|---|---|
| 10 A/m | $9.5238\times10^{-4}$ | 0.9524 |
| 50 A/m | $8.0000\times10^{-4}$ | 0.8000 |
| 100 A/m | $6.6667\times10^{-4}$ | 0.6667 |
| 200 A/m | $5.0000\times10^{-4}$ | 0.5000 |
| 400 A/m | $3.3333\times10^{-4}$ | 0.3333 |
| 1000 A/m | $1.6667\times10^{-4}$ | 0.1667 |

So the *same specimen* can be reported as $1.0\times10^{-3}$ or $1.7\times10^{-4}$ depending
only on the instrument, and both reports can be correct. The design rules:

1. **Quote the measuring field or the instrument's amplitude** with every value.
2. **Compare only like with like.** Two datasets from instruments with different amplitudes
   are not comparable without a cross-calibration on shared specimens.
3. **The measurement's field should be the field the science cares about.** A susceptibility
   intended to interpret a 50 000 nT ($\approx 40$ A/m) field measurement should be measured
   in a comparable amplitude, not at the top of the instrument's range.
4. **Both the low-field and the high-field values carry information**: the *drop* with
   amplitude is itself a grain-size and mineralogy indicator, which is why multi-amplitude
   susceptibility is a measurement in its own right.

## 4. IRM acquisition and the S-ratio

Applying a steady field and switching it off leaves an isothermal remanent magnetization
whose acquisition with field is described, in practice, by a cumulative log-Gaussian
distribution in the coercivity:

$$\frac{\text{IRM}(H)}{\text{SIRM}} = \frac{1}{2}\left[1 +
\mathrm{erf}\left(\frac{\ln(H/H_{1/2})}{\sqrt{2}\,\sigma}\right)\right] ,$$

with $H_{1/2}$ the field at half saturation and $\sigma$ the spread in $\ln H$. For a
low-coercivity (magnetite-like) component with $H_{1/2} = 30$ mT and
$\sigma = \ln(10)/2 = 1.1513$:

| $H$ | IRM/SIRM |
|---|---|
| 10 mT | 0.1700 |
| 20 mT | 0.3624 |
| 30 mT | 0.5000 |
| 60 mT | 0.7264 |
| 100 mT | 0.8522 |
| 300 mT | 0.9772 |
| 1000 mT | 0.9988 |

The shape is the measurement: a *steep* curve that saturates by 300 mT indicates a
low-coercivity mineral (magnetite-like), a *slow* curve that is still rising at 1 T
indicates a high-coercivity one (hematite-like), and a curve with two steps indicates both.

The **S-ratio** compresses the shape into one number,

$$S = \frac{\text{IRM}(-300\ \mathrm{mT})}{\text{SIRM}} ,$$

and for a two-component mixture with a hard fraction $f$ it is linear in $f$:

| Hard fraction | $S$ |
|---|---|
| 0.00 | 0.9772 |
| 0.25 | 0.7532 |
| 0.50 | 0.5292 |
| 0.75 | 0.3051 |

The decrement is 0.224 per 0.25 of hard fraction, i.e. **0.896 per unit**. Three caveats:

1. **The S-ratio is a ratio of two measurements**, so its uncertainty is at least
   $\sqrt{2}$ times the uncertainty of one — often more, because the back-field value is
   small.
2. **It is not a mineral percentage.** It maps the *coercivity* mixture, which depends on
   grain size and on oxidation state as well as on the mineral.
3. **It needs the back-field step in the protocol.** $S$ quoted at −100 mT, −300 mT or −1 T
   are different numbers; the field must be stated.

## 5. ARM and grain size

An anhysteretic remanence is acquired in a small steady bias field superposed on a decaying
alternating field. Its great virtue is that it is acquired by the *fine* (single-domain and
pseudo-single-domain) fraction, so its normalization separates concentration from grain
size. Using the same ARM for three synthetic specimens with different SIRM:

| Sample | SIRM (Am²/kg) | ARM (Am²/kg) | ARM/SIRM | $\chi_{lf}$ (m³/kg) | $\chi_{\text{ARM}}/\chi$ |
|---|---|---|---|---|---|
| fine SSD | 0.20 | 0.040 | 0.2000 | $1.0\times10^{-4}$ | 6.00 |
| coarse MD | 2.00 | 0.040 | 0.0200 | $8.0\times10^{-4}$ | 0.50 |
| mixed | 0.80 | 0.040 | 0.0500 | $4.0\times10^{-4}$ | 2.00 |

The coarse-multi-domain specimen carries **ten times** the SIRM of the fine one — so ten
times the magnetic material — yet acquires the *same* ARM, and its ARM susceptibility ratio
is **twelve times lower**. SIRM alone cannot distinguish these two rocks; the ratio can.

The ARM measurement's practical requirements:

1. **State the bias field, the alternating-field decay and the peak AF**, because the ARM
   depends on all three, and the ratio $\chi_{\text{ARM}}/\chi$ is only comparable between
   datasets measured with the same protocol.
2. **Measure the ARM after AF demagnetization**, so that the pre-existing remanence does not
   contaminate the acquired one.
3. **Use the ARM/SIRM and $\chi_{\text{ARM}}/\chi$ ratios rather than the ARM alone**, for
   the same reason the S-ratio is used: a ratio cancels the concentration term.

## 6. The holder and the specimen size

Every magnetic measurement includes the specimen *holder* and the space around it. A
correction is possible only if the holder's contribution is measured identically — empty,
in the same position, in the same session — and it is otherwise a systematic error that
scales as the inverse specimen volume:

$$\kappa_{\text{app}} = \kappa\left(1 + \frac{V_{\text{holder}}}{V_{\text{sample}}}\right) .$$

With a synthetic holder equivalent volume of 0.50 cm³:

| Sample volume | Apparent / true |
|---|---|
| 0.50 cm³ | 2.0000 |
| 1.00 cm³ | 1.5000 |
| 2.00 cm³ | 1.2500 |
| 5.00 cm³ | 1.1000 |
| 10.00 cm³ | 1.0500 |
| 20.00 cm³ | 1.0250 |

So a **1 % tolerance requires more than 50 cm³** of specimen — larger than most core plugs
cut for other measurements. Three resolutions: measure the holder empty every session and
subtract; use a holder geometry (a closed, filled tube) that minimizes the empty volume;
or accept a larger uncertainty for small specimens *and say so*, which is the honest option
for a chip or a fragment.

The same argument applies to the **mass normalization**: a measurement is reported per unit
mass, so the mass must be that of the measured specimen, including any non-magnetic matrix
and excluding any coating or mounting material. A 2 % mass error is a 2 % susceptibility
error, and it is the kind of error that survives every subsequent check.

## 7. Assumptions and regime of validity

1. **The induced magnetization is small compared with the measuring field's own effect.** A
   strongly magnetic specimen changes the field inside itself, so the measured value depends
   on the geometry — a demagnetization effect that is specimen-shape dependent and worse for
   elongated specimens.
2. **The measurement is in the linear regime of the instrument's calibration.** Both the
   bridge and the magnetometer have ranges over which the calibration is valid; a specimen
   that saturates the sensor produces a wrong number, not an error message.
3. **The remanence is stable over the measurement.** Viscous acquisition and thermal
   decay change an IRM while it is being measured, so the time between magnetizing and
   measuring is part of the protocol.
4. **The coercivity distribution is a property of the mineral assemblage**, not of the
   measurement; this fails when the field is applied at a rate or temperature that alters
   the assemblage, and for goethite-bearing samples which can acquire remanence while
   drying.
5. **The specimen is homogeneous at the measurement scale.** A magnetometer measures the
   *net* moment of the whole specimen, so a single magnetic inclusion, a fracture coating or
   a migrated grain can dominate the result — which is why the raw moment, the mass and the
   specimen description must be archived together.
6. **The laboratory values transfer to the field measurement.** They do, only if the
   amplitude, the grain size population and the temperature are comparable; a field
   susceptibility map inverted with a laboratory value measured at ten times the field
   amplitude is biased, systematically and invisibly.

## 8. The honest summary

- Susceptibility needs two bases: the system (SI, cgs) and the normalization (volume, mass);
  omitting the $4\pi$ is a 12.57× error, and omitting the density is up to a factor of 3.
- A quoted susceptibility is only meaningful with the field amplitude: the same specimen
  gave $9.5238\times10^{-4}$ at 10 A/m and $1.6667\times10^{-4}$ at 1000 A/m in the synthetic
  model.
- IRM acquisition is a shape: saturated by 300 mT (0.9772 of SIRM) means low coercivity; the
  S-ratio falls linearly with a hard-component fraction, 0.896 per unit.
- The coarse specimen carried 10× the SIRM with the same ARM and a 12× lower ARM
  susceptibility ratio: grain size, not concentration.
- A 0.50 cm³ holder equivalent volume is a 100 % error on a 0.50 cm³ specimen and a 5 %
  error at 10 cm³; 1 % needs more than 50 cm³.
- Measure the suite, report the protocols, and archive the raw moment with the mass.

## 9. Python demonstration

[`code/magnetic_lab_demo.py`](./code/magnetic_lab_demo.py) prints every number quoted
above: the susceptibility conversions with the 4π factor, the field-amplitude table, the
log-Gaussian IRM acquisition with the S-ratio of four mixtures, the ARM grain-size table,
and the holder-background table with the specimen volume a tolerance requires.

```bash
cd 23-field-methods-instruments/06-laboratory-measurements/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_lab_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/05-magnetic-lab-measurements-exercises.md`](./exercises/05-magnetic-lab-measurements-exercises.md)
and
[`exercises/05-magnetic-lab-measurements-solutions.md`](./exercises/05-magnetic-lab-measurements-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. Convert $\kappa = 2.5\times10^{-3}$ SI with $\rho = 2700$ kg/m³ into mass-specific SI,
   $\kappa_{\text{cgs}}$ and $\chi_{\text{cgs,mass}}$.
2. With $H_s = 100$ A/m, compute $\kappa_{\text{app}}/\kappa_0$ at 25, 100 and 400 A/m.
3. For $H_{1/2} = 100$ mT and $\sigma = 1.1513$, compute IRM/SIRM at 100 and 300 mT, and
   state what a value of 0.5 at 300 mT would tell you.
4. Two specimens have the same SIRM but ARM values differing by a factor of 5. State which
   is the finer-grained and why.
5. A holder has a 0.30 cm³ equivalent volume. Compute the minimum specimen volume for a 2 %
   tolerance.

## 12. Common pitfalls

1. **Quoting a susceptibility without the system, the normalization and the field.** Three
   ambiguities in one number.
2. **Mixing datasets from instruments with different amplitudes.** The values differ by a
   factor of several and both are "right".
3. **Treating the S-ratio as a mineral percentage.** It is a coercivity mixture index.
4. **Measuring ARM without stating the bias field and the AF peak.** The ratio is not
   comparable across protocols.
5. **Ignoring the holder.** It scales as $1/V$ and dominates small specimens.
6. **Normalizing by the wrong mass.** The measured mass is the normalization.
7. **One susceptibility number standing for a magnetic mineralogy.** It cannot.

## 13. Where this is used

- Palaeomagnetic and environmental-magnetic studies, where IRM, ARM and the ratios between
  them are the primary data.
- Interpretation of field magnetic surveys, where laboratory susceptibility ties the
  anomaly to the rock — see
  [23-03-02 Magnetic Fieldwork](../03-gravity-magnetic-fieldwork/02-magnetic-fieldwork.md).
- Basin and provenance studies, where a magnetic mineralogy discriminates source areas.
- Rock-physics programmes, where the magnetic properties accompany the elastic, electrical
  and thermal ones on the same specimens — see
  [08 Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md).

## 14. Related lessons

- [01 Sample Preparation, Coring and Drying Protocols](01-sample-preparation.md) —
  the masses and volumes that normalize these measurements.
- [03 Laboratory Density, Porosity and Permeability Measurement](03-density-porosity-lab.md) —
  the density used in the mass-specific conversion.
- [04 Laboratory Resistivity, IP and Dielectric Measurements](04-electrical-lab-measurements.md) —
  the electrical analogue, with the same holder problem.
- [08 Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md) —
  how these systematic terms are reported.

## 15. Self-assessment checklist

- [ ] I can convert between SI and cgs and between volume- and mass-specific values.
- [ ] I can compute a field-amplitude dependence and state why it matters.
- [ ] I can evaluate a log-Gaussian IRM curve and an S-ratio.
- [ ] I can interpret an ARM ratio as a grain-size proxy.
- [ ] I can compute a holder-background error and the volume a tolerance requires.
- [ ] I can list what must accompany every magnetic number.
