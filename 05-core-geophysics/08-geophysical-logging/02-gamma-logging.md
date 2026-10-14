---
id: 05-08-02
title: "Natural Gamma and Spectral Gamma Logging"
level: advanced
prereqs: ["02-09-04", "05-08-01", "12-03-01"]
tags: [gamma-ray, spectral-gamma, potassium, uranium, thorium, heat-production, volume-of-investigation]
---

# Natural Gamma and Spectral Gamma Logging

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what a natural-gamma measurement physically is: a count rate of
   gamma photons from the decay of $^{40}$K, the $^{238}$U and $^{232}$Th
   series, and their daughters.
2. **Derive** the volume of investigation of a gamma tool from an attenuation
   kernel, and explain why it is a decimetre rather than a metre.
3. **Compute** the vertical-resolution loss of a thin bed by convolving a layer
   model with a stated tool kernel, and state the bias it introduces.
4. **Derive** the specific heat production of natural K, U and Th from isotope
   abundance, half-life and decay energy, and check it against the conventional
   coefficient set.
5. **Explain** the API unit as a calibration convention rather than a physical
   quantity, and state what follows for interpretation.
6. **Use** the natural-gamma and spectral-gamma logs for shale volume, clay typing
   and heat-flow work, and state the assumption each use requires.

## Prerequisites

- [02-09-04 Gamma-Ray Spectrometry and Natural Radioelements](../../02-physics/09-radiation-and-atomic-physics/04-gamma-spectrometry.md)
  — the detector physics, the spectrum and the three windows.
- [05-08-01 The Borehole Environment and Invasion Profiles](./01-borehole-environment.md)
  — why the borehole is part of the measurement.
- [12-03-01 Radiogenic Heat Production and Mantle Geotherms](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md)
  — what the derived heat production is used for.

## 1. Intuition: the oldest log, and the least invasive

The natural-gamma log measures a count rate of photons that the rock emits by
itself. Nothing is fired into the formation, so there is no source, no
irradiation, no activation and no borehole-fluid attenuation problem of the kind
that dominates the nuclear porosity tools. That is why it is the cheapest, the
most repeatable and the most widely run log in the industry — and why it is run
first in essentially every well.

What it measures is *radioelement concentration*, and the interpretation step is
the familiar one: **the log never measures clay, or a shale volume, or a
lithology.** It measures gamma photons, and the leap from photons to clay is an
empirical correlation that holds in some basins and fails in others. The failure
modes are well known and specific:

- **Potassium feldspar and mica** are radioactive and not clay.
- **Heavy minerals** (zircon, monazite, apatite) carry thorium and uranium and can
  make a clean sand look radioactive.
- **Organic-rich mudstones** are frequently uranium-enriched by a completely
  different mechanism (reducing conditions, not clay content).
- **Evaporites and carbonates** are typically very low, so the *shale baseline*
  and the *clean baseline* must both come from the same well and the same
  lithology.

Spectral gamma logging separates the three contributions, which turns one
ambiguous number into three interpretable ones and, as Section 3.4 shows, into a
direct measurement of radiogenic heat production.

## 2. Precise definitions

### 2.1 Total (natural) gamma

A single count rate over an energy window chosen to include the main photopeaks of
K, U and Th decay. Reported in **API units**, where the unit is defined by a
calibration facility: a reference pit with a stated concentration of K, U and Th
gives a stated API value, and the tool's scale is set so that it reads those
values. The API is therefore a *photons-per-second convention*, not an energy and
not a mass.

### 2.2 Spectral gamma

Three (or more) windows isolate:

| Element | Source | Typical photopeak region |
|---|---|---|
| K | $^{40}$K, 1.46 MeV gamma | high energy, isolated |
| U | $^{214}$Bi in the $^{238}$U series, 1.76 MeV | needs a daughter in equilibrium |
| Th | $^{208}$Tl in the $^{232}$Th series, 2.62 MeV | needs a daughter in equilibrium |

The U and Th determinations assume **secular equilibrium** within each series.
Uranium is mobile under oxidising conditions, and radon (a gas) can migrate out of
the formation, so disequilibrium is real and the "uranium" reading is a
*proxy for a daughter*, not an assay.

### 2.3 Volume of investigation

For an exponential attenuation kernel of length $\lambda$, the fraction of the
count rate originating within depth $d$ of the wall is

$$F(d) = 1 - e^{-d/\lambda}. \tag{1}$$

The **90 per cent depth** is $d_{90} = 2.303\lambda$. $\lambda$ depends on photon
energy and formation density, so it is quoted as a range, not a constant.

### 2.4 Shale volume indices

The **gamma-ray index** is

$$I_{\mathrm{GR}} = \frac{\mathrm{GR} - \mathrm{GR}_{\min}}
{\mathrm{GR}_{\max} - \mathrm{GR}_{\min}}, \tag{2}$$

with the baselines taken from the same interval. $I_{\mathrm{GR}}$ is a
normalised *reading*; the conversion to $V_{\mathrm{sh}}$ is a separate, chosen
relation (linear, Stieber, Clavier, Larionov, …), each of which is a different
model. Stating the relation is mandatory.

## 3. Derivations

### 3.1 Volume of investigation, derived

Equation (1) is elementary, and its consequence is not: the tool reads a shell of
formation a few decimetres thick. The demonstration computes, for three stated
attenuation lengths:

| $\lambda$ (cm) | 50 per cent within | 90 per cent within |
|---|---|---|
| 5 | 3.5 cm | 11.5 cm |
| 10 | 6.9 cm | 23.0 cm |
| 20 | 13.9 cm | 46.1 cm |

So $\lambda = 10$ cm — a mid-range SYNTHETIC value — gives a 23 cm investigation
depth. Compare that with the *bed thicknesses* of interest, which are metres, and
with the *anomaly footprints* of the surface methods in module 07, which are
hundreds of metres. **The borehole measures a rock volume four orders of magnitude
smaller than a surface survey resolves**, which is the scale gap of
[05-07-04 §3.3](../07-interpretation-and-integration/04-ground-truthing.md) in
another guise.

### 3.2 Vertical resolution, computed

Convolve a layered concentration model with a stated tool kernel — a Gaussian of
half-width 0.50 m, SYNTHETIC and stated because the answer depends on it. The
measured attenuation of a single high bed in a low background:

| Bed thickness (m) | Logged peak | Attenuation | Apparent thickness (m) |
|---|---|---|---|
| 0.25 | 45.7 | $-69.6$ % | 0.00 |
| 0.50 | 69.8 | $-53.5$ % | 0.00 |
| 1.00 | 108.7 | $-27.5$ % | 0.95 |
| 2.00 | 144.1 | $-3.9$ % | 2.00 |
| 4.00 | 150.0 | $-0.0$ % | 4.00 |

Two conclusions. First, the kernel's integral is conserved (an arithmetic check:
the normalised kernel sums to 1.000000), so a thick bed is reproduced exactly — the
loss is a resolution effect, not a gain error. Second, **a thin bed is
systematically under-read**, so a shale-volume calculation in a thinly
interbedded sequence is biased, always in the direction of under-calling shale.

### 3.3 Bed thickness from the half-amplitude point, and when it fails

A common shortcut is to take bed thickness as the width at half the bed's
amplitude. The table shows the trap: below about one kernel half-width the
apparent thickness never reaches the true one (0.00 m reported for beds of 0.25
and 0.50 m at the 85-API half-amplitude level used there) while the *peak* falls
by half. The shortcut assumes the peak is correct; when the bed is thin, the peak
is precisely the thing that is wrong.

### 3.4 Radiogenic heat production, derived from decay data

This is the most useful quantitative content of a spectral gamma log, and it can
be derived rather than remembered. The specific heat production of one kilogram of
a natural element is

$$\frac{P}{m} = \underbrace{\frac{a N_A}{M}}_{\text{atoms per kg}}
\;\times\; \underbrace{\frac{\ln 2}{T_{1/2}}}_{\lambda} \;\times\;
\underbrace{E}_{\text{J per decay}}, \tag{3}$$

with $a$ the nuclide's abundance in the natural element, $M$ its molar mass,
$N_A$ Avogadro's number, and $E$ the energy released per parent decay including
the daughter chain.

Stated inputs, and the results:

| Element | Nuclide | Abundance | $T_{1/2}$ (yr) | $E$ (MeV) | $P/m$ (W kg⁻¹) |
|---|---|---|---|---|---|
| K | $^{40}$K | $1.17\times10^{-4}$ | $1.248\times10^{9}$ | 0.71 | $3.608\times10^{-9}$ |
| U | $^{238}$U | 0.99274 | $4.468\times10^{9}$ | 51.7 | $1.023\times10^{-4}$ |
| Th | $^{232}$Th | 1.0 | $1.405\times10^{10}$ | 42.6 | $2.769\times10^{-5}$ |

Expressed as the conventional coefficients

$$A\ [\mu\mathrm{W\,m^{-3}}] = 10^{-5}\,\rho\,
\left(c_K \mathrm{K}_{\mathrm{wt\%}} + c_U \mathrm{U}_{\mathrm{ppm}}
+ c_{\mathrm{Th}} \mathrm{Th}_{\mathrm{ppm}}\right), \tag{4}$$

the derivation gives $c_K = 3.61$, $c_U = 10.23$, $c_{\mathrm{Th}} = 2.77$
against the conventional set $3.48$, $9.52$, $2.56$ — differences of
$+3.7$, $+7.4$ and $+8.2$ per cent. **That agreement is a transcription check,
not a refinement**: the conventional values rest on the same decay data. The
residual difference is dominated by the energy per decay, part of which (the
neutrino fraction of the $\beta$ decays) escapes the Earth and part of which is
uncertain.

Worked values at $\rho = 2700$ kg m⁻³ with **stated synthetic** concentrations:

| Lithology | K (wt%) | U (ppm) | Th (ppm) | $A$ (µW m⁻³) |
|---|---|---|---|---|
| shale | 2.7 | 3.7 | 12.0 | 2.182 |
| clean sand | 0.8 | 0.6 | 1.7 | 0.371 |
| granite | 4.0 | 3.0 | 15.0 | 2.340 |
| basalt | 0.8 | 0.5 | 2.0 | 0.366 |

The granite and the shale have almost the same heat production for very different
element mixes — which is the reason a *total* gamma log cannot substitute for a
spectral one in heat-flow work.

### 3.5 The API unit, and why a "standard" tool value is not a fact

The API unit is defined by physical reference pits maintained for the purpose. A
tool is calibrated so that it reads a specified value in a specified pit, and the
result is a scale factor. Consequences:

- The API is **convention-dependent**. Two tools calibrated in different pits are
  interconvertible only through their stated calibrations.
- A count rate in counts per second is **not** convertible to API without the
  calibration, and the conversion changes with tool, crystal, hole size and mud.
- Therefore **no API-per-wt%K, API-per-ppm-U value may be quoted as universal.**
  Calibrate, or use spectral windows with stated sensitivities that you report.

## 4. Worked examples

### 4.1 A shale volume, with its assumptions listed

**Problem.** A sand/shale sequence reads 22 API in the cleanest sand and 110 API in
the purest shale. A point reads 62 API. Compute $I_{\mathrm{GR}}$ and $V_{\mathrm{sh}}$.

*Step 1 — index.* $I_{\mathrm{GR}} = (62-22)/(110-22) = 0.455$.

*Step 2 — relation.* The demonstration uses a stated non-linear form
$V_{\mathrm{sh}} = 0.33(2^{2I_{GR}} - 1)$, giving $V_{\mathrm{sh}} = 0.290$.
A linear relation would give 0.455; the choice is a model and it changes the
answer by 57 per cent relative.

*Step 3 — assumptions, stated.* Both baselines are from this well and this
lithology; the radioactivity is clay-borne (no feldspar, mica, heavy minerals or
organic matter); the bed is thick compared with the kernel of §3.2; the hole is in
gauge.

*Step 4 — report.* "$V_{\mathrm{sh}} = 0.29$, using a non-linear index relation and
an intra-well baseline pair, and assuming the radioactivity is clay-borne."

### 4.2 Why a uranium spike is not more clay

An organic-rich mudstone reads a high *uranium* window and a modest K and Th
window. The interpretation is a reducing depositional environment concentrating
uranium, not an increase in clay content. A single total-gamma log cannot
distinguish the two; the spectral log can, and this is one of its clearest
practical uses.

### 4.3 Heat production from a spectral log, and its uncertainty

Given a spectral log over a 2 km interval, the heat production is computed by
Equation (4) *at each depth*, then integrated over the interval to give a column
heat-production budget. The uncertainty is dominated by three terms: the
elemental calibration (a stated percentage), the disequilibrium assumption of
§2.2, and the assumed density. Report all three; a heat-flow model built on an
uncalibrated spectral log inherits an error that is invisible in the log itself
and shows up as an unexplained heat-flow deficit.

## 5. Assumptions

1. **Radioactivity is clay-borne** for $V_{\mathrm{sh}}$ work. List the exceptions
   from §1 explicitly in any report.
2. **Secular equilibrium** for the U and Th windows.
3. **Baselines and calibration from the same tool, hole and mud.**
4. **Beds thick compared with the tool kernel** for a peak amplitude to be
   meaningful.
5. **A stated index-to-$V_{\mathrm{sh}}$ relation.**
6. **A formation density** for the heat-production conversion, with its own
   uncertainty.
7. **No casing or cement attenuation unaccounted for**, if the log is run after
   completion.

## 6. Units and dimensional analysis

- API: a calibration convention. Never write "API = wt% K"; write the calibration.
- Count rate: s⁻¹. Conversion to API requires a stated sensitivity.
- $I_{\mathrm{GR}}$ and $V_{\mathrm{sh}}$: dimensionless, bounded $[0,1]$ by
  construction.
- Equation (3): atoms kg⁻¹ × s⁻¹ × J = W kg⁻¹ ✓. The factor $10^{9}$ between
  W kg⁻¹ and nW kg⁻¹ (or pW g⁻¹) is the commonest error in this calculation; check
  it against a known lithology.
- Equation (4): $\rho$ in kg m⁻³, K in wt%, U and Th in ppm; the $10^{-5}$ carries
  the conversion. Using ppm for K instead of wt% is a factor of $10^4$.
- The attenuation length $\lambda$ is in cm or m; $d_{90} = 2.303\lambda$ is then
  in the same unit.

## 7. Python demonstration

`code/gamma_demo.py` derives the heat-production coefficients, computes the volume
of investigation and measures the bed attenuation.

```python
atoms = d["abundance"] * NA / d["molar_mass"]
lam = LN2 / (d["half_life_yr"] * YR_S)
spec = atoms * lam * d["energy_MeV"] * MEV_J
```

Measured output, abridged:

```
lambda =  5.0 cm -> 50 per cent within    3.5 cm, 90 per cent within   11.5 cm
lambda = 10.0 cm -> 50 per cent within    6.9 cm, 90 per cent within   23.0 cm
lambda = 20.0 cm -> 50 per cent within   13.9 cm, 90 per cent within   46.1 cm

bed (m)   true API   logged peak   attenuation   apparent thickness (m)
 0.25      150.0         45.7       -69.6 %             0.00
 0.50      150.0         69.8       -53.5 %             0.00
 1.00      150.0        108.7       -27.5 %             0.95
 2.00      150.0        144.1        -3.9 %             2.00
 4.00      150.0        150.0        -0.0 %             4.00

specific heat production of natural K  (40K  ) = 3.6080e-09 W per kg of element
specific heat production of natural U  (238U ) = 1.0228e-04 W per kg of element
specific heat production of natural Th (232Th) = 2.7693e-05 W per kg of element

coefficient   derived   conventional   difference
         K      3.61           3.48         +3.7 per cent
         U     10.23           9.52         +7.4 per cent
        Th      2.77           2.56         +8.2 per cent
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| $d_{90} = 2.303\lambda$ gives 23 cm for $\lambda = 10$ cm | The tool reads a decimetre; quote $\lambda$ with the number |
| Kernel sums to 1.000000 and a 4 m bed is reproduced exactly | The thin-bed loss is resolution, not a gain error |
| A 0.5 m bed loses 53.5 per cent of its amplitude | Thin-bed shale volumes are biased, always the same way |
| Derived coefficients match the conventional set to 3.7–8.2 per cent | The derivation is a check on transcription, and it is honest about its residual |
| Granite and shale give 2.340 and 2.182 µW m⁻³ | A total-gamma reading is not a heat-production measurement |

> **Breaking exercise.** Change the tool kernel half-width to 0.25 m and predict,
> before running, the new attenuation for the 0.5 m bed. Then check whether the
> *thick* beds are still reproduced exactly, and explain why they must be.

## 8. Exercises

[`exercises/02-gamma-logging-exercises.md`](./exercises/02-gamma-logging-exercises.md)
and
[`exercises/02-gamma-logging-solutions.md`](./exercises/02-gamma-logging-solutions.md).

### ★ Foundational

**★1.** State what a natural-gamma tool physically measures and three rock
properties it does *not* measure.

**★2.** For $\lambda = 8$ cm, compute the 50 and 90 per cent investigation depths.

**★3.** Given clean baseline 25 API and shale baseline 130 API, compute
$I_{\mathrm{GR}}$ for a reading of 74 API and $V_{\mathrm{sh}}$ under both the
linear and the 0.33(2^{2I}−1) relations.

### ★★ Applied

**★★4.** Run `code/gamma_demo.py`. Report the derived coefficients, and compute
the heat production of a rock with 3.0 wt% K, 2.0 ppm U and 8.0 ppm Th at
$\rho = 2650$ kg m⁻³ using both the derived and the conventional coefficients.

**★★5.** A 0.6 m bed of 140 API sits in a 25 API background. Using the
demonstration's kernel, estimate the logged peak, and state the shale volume error
it would cause if the reading were used directly.

**★★6.** Explain why sodium iodide and bismuth-germanate detectors give different
K/U/Th sensitivities for the same formation.

### ★★★ Research-oriented

**★★★7.** Uranium-series disequilibrium is common in organic-rich mudstones.
Construct a two-box model (U in the rock, Rn expelled) and compute the bias in the
"uranium" window reading as a function of the expelled fraction. State what
measurement would detect the disequilibrium, and how you would report it.

**★★★8.** Using the derived coefficient set, compute the heat production of a
layered crustal column from a synthetic spectral log you define, integrate it, and
compare the resulting surface heat flow with the value obtained from a heat-flow
measurement. State every assumption and quantify the largest one.

## 9. Common mistakes

1. **Calling the reading a "clay volume".** State the relation and the
   clay-borne assumption.
2. **Using baselines from another well or another lithology.**
3. **Quoting an API-to-element conversion as universal.** It is
   calibration-specific.
4. **Forgetting thin-bed attenuation** when a shale volume is computed bed by bed.
5. **Ignoring disequilibrium** in the uranium window.
6. **Treating a total-gamma reading as a heat-production proxy.** Section 3.4
   shows granite and shale are indistinguishable in total gamma and different in
   origin.
7. **Mixing nW kg⁻¹ and nW m⁻³** in the heat-production calculation.

## 10. Real-world applications

- **Shale volume and lithology.** The most common use, and the one most often
  over-claimed.
- **Clay typing.** K-dominated illite, Th-dominated kaolinite/montmorillonite,
  U-rich organic matter — a real discrimination that a total-gamma log cannot make.
- **Heat-flow and geotherm modelling.** Radiogenic heat production comes from the
  spectral log or from core, and it enters the geotherm directly
  ([12-03-01](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md)).
- **Unconventional reservoirs.** Spectral gamma identifies organic-rich intervals
  through their uranium content, which is a genuine exploration indicator.
- **Geothermal exploration.** Radiogenic heat production from a well constrains the
  resource model
  ([05-09-03](../09-geothermal-and-heat-flow-methods/03-geothermal-exploration.md)).
- **Environmental and mining logging.** Potassium and uranium are measured for
  potash grade control and for radiological assessment, with the same physics.

## 11. Further reading

- **Ellis, D. V. & Singer, J. M. (2007). *Well Logging for Earth Scientists*
  (2nd ed.). Springer.** Chapters 11–12. Level: intermediate to advanced. Detector
  physics, spectral windows, calibrations and environmental corrections.
- **Serra, O. (1984). *Fundamentals of Well-Log Interpretation*, Vol. 1.
  Elsevier.** Level: intermediate. The classical treatment of gamma-ray
  interpretation, including the $V_{\mathrm{sh}}$ relations.
- **Rybach, L. (1988). Determination of heat production rate. In *Handbook of
  Terrestrial Heat-Flow Density Determination*, Kluwer.** Level: advanced. The
  conventional coefficient set of §3.4 and its derivation.
- **IAEA (2003). *Guidelines for Radioelement Mapping Using Gamma Ray
  Spectrometry Data*. IAEA-TECDOC-1363.** Level: advanced. Calibration, spectral
  processing and disequilibrium, from the airborne and ground side.
- **Hearst, J. R., Nelson, P. H. & Paillet, F. L. (2000). *Well Logging for
  Physical Properties*. Wiley.** Level: advanced. Tool physics and the
  volume-of-investigation formalism.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-08-03 Resistivity, Induction and Laterolog Tools](./03-resistivity-logging.md)
  — the other "first run" log, and the one that depends on the borehole fluid.
- [05-08-07 Log Interpretation, Petrophysics and Uncertainty](./07-log-interpretation.md)
  — where $V_{\mathrm{sh}}$ from this log enters a full workflow and carries its
  uncertainty.
- [05-09-02 Thermal Conductivity Measurement and Corrections](../09-geothermal-and-heat-flow-methods/02-thermal-conductivity.md)
  — the other half of a heat-flow model.
- [12-03-01 Radiogenic Heat Production and Mantle Geotherms](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md)
  — where the derived heat production is used.
- [02-09-05 Neutron Interactions and Borehole Nuclear Measurements](../../02-physics/09-radiation-and-atomic-physics/05-neutron-interaction.md)
  — the nuclear tools that *do* irradiate the formation.

## Self-assessment checklist

- [ ] I can state what the natural-gamma log measures and three things it does
      not. (§1)
- [ ] I can derive the volume of investigation and the 2.303 rule. (§3.1)
- [ ] I can compute the thin-bed attenuation from a stated kernel. (§3.2)
- [ ] I can derive the specific heat production of K, U and Th and check the
      conventional coefficients. (§3.4)
- [ ] I can explain the API unit as a convention and say what follows. (§3.5)
- [ ] I can compute a shale volume with its assumptions listed. (§4.1)
- [ ] I can explain a uranium anomaly without invoking clay. (§4.2)
- [ ] I can run the demonstration and interpret every printed number. (§7)
