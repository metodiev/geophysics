---
id: 09-05-04
title: "EM for Geothermal Systems and Permafrost"
level: doctoral
prereqs: ["08-04-05", "09-01-05", "09-01-02", "09-05-01"]
tags: [electrical-methods, geothermal, permafrost, temperature-dependence, clay-cap, monitoring, detectability, non-uniqueness]
---

# EM for Geothermal Systems and Permafrost

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** an Arrhenius-type temperature model for rock conductivity and
   **state** the assumed constants it needs.
2. **Compute** the conductivity and resistivity of a synthetic section from
   $0$ to $300$ °C and identify the factor by which it changes.
3. **Measure** the EM response of a frozen layer over unfrozen ground and
   **state** the detection limit as a function of the stated noise.
4. **Demonstrate** that a conductive clay cap dominates the response and saturates
   in thickness, and **explain** what that does to the geothermal interpretation.
5. **Compute** the temperature change a monitoring survey can resolve, and
   **explain** why it is larger at low temperature in this model.
6. **State** precisely which parts of a geothermal or permafrost interpretation
   are measurement and which are petrophysical assumption.
7. **Report** a temperature or ice-content claim with the model it depends on.

## Prerequisites

- [08-04-05 MT Interpretation: Conductors, Fluids, Melts and Frontiers](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/05-mt-interpretation.md)
  — what a conductivity model means in a geothermal setting.
- [09-01-05 Temperature, Pressure and Frequency Dependence](../01-electrical-properties-of-earth/05-temperature-and-pressure-effects.md)
  — the material physics behind this lesson's model.
- [09-01-02 Archie's Law, Porosity and Saturation](../01-electrical-properties-of-earth/02-archies-law.md)
  — how pore fluid and ice fraction enter conductivity.
- [09-05-01 TEM Sounding for Aquifers and Mineral Targets](01-tem-sounding.md)
  — the kernel, its validation and the window logic.

**All models and data in this module are SYNTHETIC.** Temperatures, activation
energies, conductivities, thicknesses, frequencies and thresholds are chosen
teaching values; nothing here is a measurement of a real field, well, ice body or
instrument.

---

## 1. Intuition: temperature and ice both write on the same channel

Conductivity in the shallow crust is carried mostly by ions in pore water. Two
changes to that water dominate: **heating** it, which raises its ionic mobility
(and hence the conductivity), and **freezing** it, which removes the liquid
pathway almost entirely. Both act on the same measured quantity, and both are
therefore "seen" by an EM survey — but neither is *measured* directly; what is
measured is a conductivity profile, and the temperature or ice content is a
petrophysical interpretation on top of it.

Two structural consequences organise the lesson.

- **The map from temperature to conductivity is exponential and model-dependent.**
  Its slope depends on an assumed activation energy, which no EM survey
  constrains.
- **A conductive cap hides what is below it.** In geothermal systems the clay cap
  produced by hydrothermal alteration is far more conductive than the reservoir
  and dominates the response, saturating once it is thick. The response then
  reports the cap, not the heat source.

## 2. Precise definitions

### 2.1 The Arrhenius temperature model

$$\sigma(T) = \sigma_{25}\exp\!\left[\frac{E_a}{R}
\left(\frac{1}{298.15} - \frac{1}{T}\right)\right],$$

with $R = 8.314462618\ \mathrm{J\,mol^{-1}\,K^{-1}}$ (exact by definition),
$E_a$ the activation energy of the conducting process (an assumed model
parameter) and $\sigma_{25}$ the conductivity at $25$ °C.

### 2.2 Frozen ground and the clay cap

- **Frozen layer:** a resistive layer of conductivity $\sigma_f$ and thickness
  $t$ over an unfrozen half-space of $\sigma_u > \sigma_f$; in the synthetic model
  $\sigma_f = 0.002$ S/m and $\sigma_u = 0.05$ S/m.
- **Clay cap:** a conductive layer of $\sigma_c = 0.2$ S/m and thickness $t$ over
  a resistive reservoir of $0.001$ S/m (200 m) over a basement of $0.02$ S/m.
- **Response ratio:** $|H_s(\text{model})| / |H_s(\text{reference})|$, the same
  quantity as in [09-05-01](01-tem-sounding.md), computed with the same validated
  kernel.

### 2.3 Monitoring resolution

The **resolved temperature change** is the $\Delta T$ that produces a stated
response change (taken as $1\%$), given the model of Section 2.1. In the
linear-response regime a $1\%$ change in $|H_s|$ corresponds to a $0.5\%$ change
in conductivity.

## 3. Derivations

### 3.1 Conductivity against temperature

Differentiating the Arrhenius model gives the *relative* sensitivity

$$\frac{1}{\sigma}\frac{\mathrm{d}\sigma}{\mathrm{d}T}
= \frac{E_a}{R\,T^{2}},$$

which falls as $T^{-2}$: the same temperature change matters less in a hot rock
than in a cold one. With $\sigma_{25} = 0.05$ S/m and $E_a = 15.0$
kJ/mol (assumed), the demonstration prints:

| $T$ (°C) | $T$ (K) | $\sigma$ (S/m) | $\rho$ ($\Omega$ m) | $\sigma/\sigma_{25}$ |
|---|---|---|---|---|
| 0 | 273.15 | 0.02874 | 34.80 | 0.5748 |
| 25 | 298.15 | 0.05000 | 20.00 | 1.0000 |
| 50 | 323.15 | 0.07985 | 12.52 | 1.5970 |
| 100 | 373.15 | 0.16871 | 5.93 | 3.3743 |
| 200 | 473.15 | 0.46873 | 2.13 | 9.3746 |
| 300 | 573.15 | 0.91168 | 1.10 | 18.2336 |

So the conductivity rises by a factor $5.87$ from $0$ to $100$ °C and by
$31.7$ from $0$ to $300$ °C, and the resistivity falls from $34.80$ to
$1.10\ \Omega$ m. **The activation energy is the dominant uncertainty**: doubling
$E_a$ squares the ratio, and $E_a$ is a property of the pore fluid and the
mineral surfaces that the survey does not measure.

### 3.2 A frozen layer: measured response and detection limit

| $t$ (m) | $f = 10$ Hz | $f = 100$ Hz | $f = 1000$ Hz | $f = 10$ kHz |
|---|---|---|---|---|
| 2 | 0.9718 | 0.9708 | 0.9708 | 0.9650 |
| 5 | 0.8790 | 0.8734 | 0.8637 | 0.8504 |
| 10 | 0.6945 | 0.6795 | 0.6477 | 0.6047 |
| 20 | 0.4465 | 0.4202 | 0.3658 | 0.2964 |
| 40 | 0.2510 | 0.2201 | 0.1658 | 0.1193 |

Each entry is the response ratio against the unfrozen half-space. A $2$ m frozen
layer is a $2.9\%$ change at $1000$ Hz, and a $20$ m layer is a factor $2.4$ at
$100$ Hz. At a $1\%$ response threshold the detection limit is about $2$ m
across the whole band, and the response keeps growing with thickness
($0.4202$ at $20$ m against $0.2201$ at $40$ m at $100$ Hz), so the method
**trades thickness resolution against noise rather than saturating**.

### 3.3 A clay cap: dominant and saturating

| cap thickness (m) | $f = 1$ Hz | $f = 10$ Hz | $f = 100$ Hz | $f = 1000$ Hz |
|---|---|---|---|---|
| 10 | 34.4712 | 38.1667 | 47.5938 | 59.2602 |
| 50 | 88.0725 | 97.5692 | 118.7431 | 113.5782 |
| 100 | 98.3053 | 108.5453 | 126.3128 | 112.2835 |
| 200 | 103.4897 | 113.1780 | 126.0967 | 112.3075 |

The cap's influence is large everywhere in the band (a factor $34$ to $126$), and
its maximum moves from $1000$ Hz for a $10$ m cap to $100$ Hz for a $50$–$200$ m
cap: the sensitivity tracks the cap diffusively. **Once the cap is thick the
response saturates** ($126.31$ for $100$ m against $126.10$ for $200$ m at
$100$ Hz), so a thick cap cannot be separated from a thicker one. Two
consequences follow: the response reports the cap rather than the reservoir
$100$ m below it, and the map from response to cap thickness is many-to-one.
This is the classical geothermal problem, and it is why an EM survey is
*inverted for a conductivity model* and then interpreted jointly with temperature
and alteration data, never read as a temperature.

### 3.4 Monitoring: the resolved temperature change

| $T$ (°C) | relative $\mathrm{d}\sigma/\mathrm{d}T$ per K | $\Delta T$ for a $0.5\%$ $\sigma$ change |
|---|---|---|
| 0 | 0.024180 | 0.21 K |
| 25 | 0.020295 | 0.25 K |
| 100 | 0.012957 | 0.39 K |
| 200 | 0.008059 | 0.62 K |

At a $1\%$ response threshold the resolved temperature change is $0.21$ K at
$0$ °C and $0.62$ K at $200$ °C. Note the direction: in this Arrhenius model the
*relative* sensitivity is **largest at low temperature**, so monitoring is easier
in a cool system than in a hot one — the opposite of the naive expectation, and a
direct consequence of the assumed model. A temperature change resolved by the
resistivity is also not a temperature *at* a depth: converting one into the other
needs Section 2.1's model, which is exactly the assumption a monitoring survey
cannot check.

## 4. Physical interpretation

- **Two mechanisms, one channel.** Heating raises $\sigma$; freezing lowers it.
  A survey cannot separate them without independent temperature or hydrological
  information.
- **Caps dominate; reservoirs hide.** The measured saturation of Section 3.3 is
  the quantitative form of the standard geothermal caution.
- **Monitoring resolution is a model statement.** The measured $\Delta T$ values
  are only as good as $E_a$.
- **Ice detection is a geometry question.** The frozen layer's base is resolved
  when the diffusion depth of the window matches its thickness, and the measured
  table shows the transition.

## 5. Assumptions and regime of validity

1. **A single Arrhenius process** with a stated $E_a$. Real rocks have a
   distribution of activation energies, and near the freezing point the
   unfrozen-water fraction makes the temperature dependence strongly non-Arrhenius.
2. **No ice dielectric relaxation.** At high frequencies ice has its own
   relaxation; in the diffusive band modelled here it appears as conductivity only.
3. **No pressure dependence**, no salinity change with temperature (which is
   itself a petrophysical model), and no melting latent-heat effects.
4. **A layered, isotropic section**; the same limitations as
   [09-05-01](01-tem-sounding.md).
5. **A stated noise level** ($1\%$ in the monitoring calculation). Every
   detection limit quoted is a function of that assumption.
6. **The petrophysical map is not measured.** The lesson converts temperature to
   conductivity only in the forward direction; the inverse direction needs the
   same model and carries its error.

## 6. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| activation energy | $E_a$ | J/mol | 15 kJ/mol = 1.5e4 J/mol |
| $E_a/R$ | — | K | 1.5e4/8.3145 = 1804 K |
| relative sensitivity | $\frac{1}{\sigma}\frac{\mathrm{d}\sigma}{\mathrm{d}T}$ | $\mathrm{K^{-1}}$ | 1804 K / T² |
| conductivity, thickness, depth | $\sigma, t, z$ | S/m, m, m | |
| response ratio | — | — | $|H_s|_{\text{model}}/|H_s|_{\text{ref}}$ |

Check the relative sensitivity at $0$ °C: $1804/273.15^{2} = 0.02418$ per K,
which is the printed first entry; at $200$ °C it is $1804/473.15^{2} = 0.00806$,
also printed. A useful rule: a $1$ K change at room temperature moves the
conductivity by about $2\%$ at this activation energy.

## 7. Worked examples

### Example 1 — the conductivity of a 150 °C section

$T = 423.15$ K; $\frac{1}{298.15} - \frac{1}{423.15} = 3.3540\times10^{-3} -
2.3632\times10^{-3} = 9.908\times10^{-4}$ K⁻¹; $E_a/R = 1804.1$ K; the exponent
is $1.7877$, so $\sigma = 0.05 \times e^{1.7877} = 0.05 \times 5.976 =
0.2988$ S/m and $\rho = 3.35\ \Omega$ m. Interpolating the printed table between
$100$ °C ($0.16871$) and $200$ °C ($0.46873$) gives $\sim0.30$ S/m at $150$ °C,
consistent.

### Example 2 — the thinnest detectable frozen layer

At $100$ Hz the response ratios are $0.9708$ (2 m), $0.8734$ (5 m), $0.6795$
(10 m) and $0.4202$ (20 m), against a $1\%$ threshold. The 2 m entry is a $2.9\%$
change, so the layer is detected; extrapolating towards thinner layers, the $1\%$
threshold is reached at about $0.7$ m. **The detection limit is therefore far
below the resolution limit**: a frozen layer thinner than a metre may be
detectable while its thickness is uncertain by tens of per cent.

### Example 3 — a temperature claim from a monitored change

A repeat survey resolves a $2\%$ change in $|H_s|$ between two epochs in a section
at $100$ °C. From Section 3.4 that is a $1\%$ conductivity change, and
$\Delta T = 0.01/0.012957 = 0.77$ K. The defensible statement is: "a $0.8$ K
temperature change if the ground is the assumed Arrhenius material with
$E_a = 15$ kJ/mol; between $0.4$ and $1.6$ K if $E_a$ is uncertain by a factor of
two (since the sensitivity is linear in $E_a$)". **The model uncertainty dominates
the measurement**, which is why a monitoring program pairs EM with temperature
observation where it can.

## 8. Python demonstration

`code/em_geothermal_permafrost_demo.py` prints every number in this lesson:

1. the Arrhenius conductivity table from $0$ to $300$ °C with the exact ratio
   $\sigma/\sigma_{25}$;
2. the measured response of a frozen layer at four thicknesses and four
   frequencies, with the detection limit at a $1\%$ threshold;
3. the clay-cap response against thickness and frequency, showing the saturation;
4. the resolved temperature change for a $1\%$ response threshold at four
   temperatures.

```bash
cd 09-electrical-em-methods/05-em-methods-applications/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_geothermal_permafrost_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/04-em-geothermal-permafrost-exercises.md`](./exercises/04-em-geothermal-permafrost-exercises.md)
and
[`exercises/04-em-geothermal-permafrost-solutions.md`](./exercises/04-em-geothermal-permafrost-solutions.md).

- **★** Compute $\sigma$ at $60$ °C for $\sigma_{25} = 0.03$ S/m and
  $E_a = 20$ kJ/mol.
- **★** From the frozen-layer table, state the frequency at which a $5$ m layer
  produces the largest response change.
- **★★** Derive $\frac{1}{\sigma}\frac{\mathrm{d}\sigma}{\mathrm{d}T} = E_a/RT^{2}$
  and evaluate it at $50$ and $250$ °C; state the trend and its consequence for
  monitoring.
- **★★** Explain, with the measured cap table, why a thick cap cannot be
  distinguished from a thicker one, and what that implies for an inversion.
- **★★★** Design a monitoring programme to resolve a $1$ K temperature change at
  $20$ °C in a section whose conductivity is $0.05$ S/m, stating the band, the
  repeat interval, the statistic and the assumption you are accepting.

## 10. Common mistakes

1. **Reporting a temperature from a resistivity.** The map is exponential and
   model-dependent; only a conductivity was measured.
2. **Quoting a permafrost thickness from one frequency.** The depth of
   investigation is a window, not a boundary.
3. **Assuming a hot anomaly is always more conductive.** A dry, hot rock has a
   pore-fluid-controlled conductivity that the Arrhenius model may understate.
4. **Forgetting the cap.** Measured response ratios of $34$–$126$ mean the cap,
   not the reservoir.
5. **Treating the detection limit as the resolution limit.** Example 2 shows the
   two differ by more than a factor of ten.
6. **Ignoring the monitoring noise level.** Every $\Delta T$ quoted is a function
   of the stated response threshold.

## 11. Real-world applications

- **Geothermal exploration.** MT and EM map the clay cap and the deep conductor;
  the interpretation is a temperature and alteration map built jointly with
  geology.
- **Permafrost monitoring.** Time-lapse EM tracks the active layer and the
  permafrost base; the detectability limits of Section 3.2 apply directly.
- **Frozen ground engineering.** Foundations, pipelines and roadbed stability
  depend on ice content, which is inferred from the conductivity with the
  petrophysical model of this lesson.
- **Volcanic and hydrothermal monitoring.** Magma and hydrothermal fluids are
  conductors; time-lapse MT is used to track them, with the monitoring resolution
  of Section 3.4.

## 12. Related lessons

- [09-05-01 TEM Sounding for Aquifers and Mineral Targets](01-tem-sounding.md) —
  the kernel, its validation and the window logic used here.
- [09-01-05 Temperature, Pressure and Frequency Dependence](../01-electrical-properties-of-earth/05-temperature-and-pressure-effects.md) —
  the material physics behind the Arrhenius model.
- [09-03-04 IP for Sulphides, Clays, Contaminants and Permafrost](../03-induced-polarisation/04-ip-applications.md) —
  what induced polarisation adds to a frozen-ground measurement.
- [08-04-05 MT Interpretation: Conductors, Fluids, Melts and Frontiers](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/05-mt-interpretation.md) —
  how a conductivity model is read in a geothermal context.
- [09-05-05 EM for Contaminant Plumes, Salinity and Leachate](05-em-environmental.md) —
  the same layered logic for pore-fluid chemistry.

## 13. Self-assessment checklist

- [ ] I can compute $\sigma(T)$ from the Arrhenius model with stated constants.
- [ ] I can state the relative sensitivity $E_a/RT^{2}$ and its consequence.
- [ ] I can read a frozen-layer response table and give a detection limit.
- [ ] I can explain the cap saturation from measured numbers.
- [ ] I can convert a monitored response change into a $\Delta T$ with its range.
- [ ] I can separate what was measured from what was assumed in a claim.
