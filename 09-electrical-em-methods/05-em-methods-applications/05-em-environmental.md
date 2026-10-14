---
id: 09-05-05
title: "EM for Contaminant Plumes, Salinity and Leachate"
level: graduate
prereqs: ["09-01-02", "09-02-08", "09-03-04", "09-05-02"]
tags: [electrical-methods, environmental-em, contaminant-plume, salinity, leachate, archie, detectability, equivalence]
---

# EM for Contaminant Plumes, Salinity and Leachate

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a pore-fluid conductivity from a concentration with a stated
   molar-conductivity model, and **state** the assumption it carries.
2. **Compute** a bulk conductivity from Archie's law and a surface-conduction
   term, and **identify** the concentration below which the pore fluid stops
   dominating.
3. **Measure** the EM response of a synthetic plume against concentration and
   thickness, and **state** the detectability threshold for each.
4. **Demonstrate** that the detectable quantity is a conductance, and **quantify**
   how much a thickness error moves a reported concentration.
5. **Explain** where the method saturates and where the petrophysical model, not
   the measurement, sets the answer.
6. **Report** a plume interpretation as an admitted range of
   concentration–thickness pairs.
7. **Specify** an environmental EM survey that supports the interpretation being
   claimed.

## Prerequisites

- [09-01-02 Archie's Law, Porosity and Saturation](../01-electrical-properties-of-earth/02-archies-law.md)
  — the formation factor and the surface-conduction term.
- [09-02-08 ERT Applications: Aquifers, Contamination, Landslides, Archaeology](../02-dc-resistivity/08-ert-applications.md)
  — the resistivity side of the same problem.
- [09-03-04 IP for Sulphides, Clays, Contaminants and Permafrost](../03-induced-polarisation/04-ip-applications.md)
  — what polarisation adds when the conductivity contrast saturates.
- [09-05-02 FEM Conductivity Mapping and Apparent Conductivity](02-fem-conductivity-mapping.md)
  — the calibration and its regime of validity.

**All models and data in this module are SYNTHETIC.** Concentrations,
conductivities, molar conductivities, thicknesses, depths, frequencies and
thresholds are chosen teaching values; nothing here is a measurement of any real
site, plume, leachate or instrument.

---

## 1. Intuition: a plume is a pore-fluid signal, filtered by the pores

An environmental EM survey detects a contaminant plume by its effect on the
electrical conductivity of the ground. Two filters stand between the plume and
the measurement.

1. **The pore geometry.** The bulk conductivity responds to the pore *fluid*
   through the formation factor $F$ and to the grain surfaces through a surface
   conduction term. In a clay-rich or fine-grained soil the surface term can
   dominate, and then the pore fluid is nearly invisible.
2. **The measurement's own averaging.** As in every other method in this folder,
   a datum constrains a *conductance-like* average; the thickness and the
   concentration trade against each other.

The lesson's quantitative aim is to state both filters as numbers, so that a
reported concentration carries the range of models consistent with it.

## 2. Precise definitions

### 2.1 Pore-fluid conductivity

$$\sigma_w = \Lambda\,c,$$

with $c$ the concentration [mol/m³] and $\Lambda$ an assumed molar conductivity
[S m²/mol]. $\Lambda$ depends on the ion species, on the temperature and on the
concentration; the demonstration states one value and treats it as a model
assumption.

### 2.2 Bulk conductivity

$$\sigma_{\text{bulk}} = \frac{\sigma_w\,\phi^{\mathrm{CEM}}}{a}
+ \sigma_s,
\qquad F = \phi^{-\mathrm{CEM}},$$

with porosity $\phi$, Archie cementation exponent $\mathrm{CEM}$, tortuosity
factor $a = 1$ and a lumped **surface conduction** term $\sigma_s$ [S/m] that
carries the clay and grain-surface contribution.

### 2.3 Plume model and response

A plume layer of thickness $t$ and conductivity $\sigma_{\text{bulk}}$ at $5$ m
depth over an uncontaminated half-space of $0.02$ S/m. The **response ratio** is
$|H_s(\text{plume})|/|H_s(\text{background})|$ at a stated frequency and offset,
computed with the same validated kernel as
[09-05-01](01-tem-sounding.md).

## 3. Derivations

### 3.1 From concentration to bulk conductivity

With $\Lambda = 0.0126$ S m²/mol, $\phi = 0.35$, $\mathrm{CEM} = 1.80$ (so
$F = 6.617$) and $\sigma_s = 0.0020$ S/m, the demonstration prints:

| $c$ (mol/m³) | $\sigma_w$ (S/m) | $F$ | $\sigma_{\text{bulk}}$ (S/m) | $\rho$ ($\Omega$ m) |
|---|---|---|---|---|
| 1.0 | 0.01260 | 6.617 | 0.00390 | 256.16 |
| 10.0 | 0.12600 | 6.617 | 0.02104 | 47.52 |
| 50.0 | 0.63000 | 6.617 | 0.09721 | 10.29 |
| 100.0 | 1.26000 | 6.617 | 0.19242 | 5.20 |
| 500.0 | 6.30000 | 6.617 | 0.95413 | 1.05 |

A factor $500$ in concentration changes the bulk conductivity by a factor $15$:
the survey sees the pore fluid *amplified by the pore geometry*, which is why
the same concentration gives different conductivities in different soils.

**Where the fluid stops mattering.** At $c = 1$ mol/m³ the fluid contributes
$0.01260/6.617 = 0.00190$ S/m against $\sigma_s = 0.0020$ S/m, so the surfaces
carry $51.2\%$ of the bulk conductivity. Below that concentration the surface term
dominates and the bulk conductivity stops responding to the pore fluid at all —
which is the quantitative form of the standard caution that conductivity alone
cannot separate salinity from clay content.

### 3.2 The measured response of a plume

Response ratio against the background at $100$ Hz and a $20$ m offset, for four
concentrations and four thicknesses:

| $c$ (mol/m³) | $t = 2$ m | $t = 5$ m | $t = 10$ m | $t = 20$ m |
|---|---|---|---|---|
| 10 | 0.9960 | 0.9921 | 0.9890 | 0.9840 |
| 50 | 0.9924 | 0.9822 | 0.9705 | 0.9504 |
| 200 | 0.9856 | 0.9654 | 0.9397 | 0.8991 |
| 500 | 0.9824 | 0.9587 | 0.9265 | 0.8738 |

(ratios below unity: a conductor *lowers* $|H_s|$ in this geometry, as in
[09-05-02](02-fem-conductivity-mapping.md)). A $2$ m plume at $10$ mol/m³ changes
the response by $0.4\%$, and a $20$ m plume at $500$ mol/m³ by $12.6\%$. The
detectability of a plume is therefore a *joint* statement about concentration and
thickness, and one response cannot separate them — the empirical form of the
equivalence measured in the TEM and FDEM lessons.

### 3.3 Detection thresholds measured against thickness

For each thickness, the concentration whose response differs from the background
by exactly $5\%$ at $100$ Hz and $20$ m offset:

| $t$ (m) | concentration for a $5\%$ response (mol/m³) | conductance $S = \sigma_{\text{bulk}} t$ (S) |
|---|---|---|
| 2.0 | 15.89 | 0.0645 |
| 5.0 | 12.19 | 0.1260 |
| 10.0 | 10.99 | 0.2292 |
| 20.0 | 10.37 | 0.4350 |

The required concentration falls only from $15.9$ to $10.4$ mol/m³ — a factor
$1.5$ — for a factor ten in thickness, while the conductance of the detectable
anomaly grows from $0.065$ to $0.435$ S. **The measurement responds to the
conductance, and it reports a concentration only after a thickness is assumed:** a
factor ten error in thickness moves the reported concentration by only a factor
$1.5$. That factor is the size of the equivalence for this configuration —
bounded, but larger than any honest concentration claim should carry silently.

## 4. Physical interpretation

- **The petrophysical filter dominates the measurement.** A factor $51.2\%$ of
  the bulk conductivity came from surfaces at $c = 1$ mol/m³, and a factor $6.6$
  separates fluid conductivity from bulk conductivity at all concentrations.
- **A plume is a small, broad, conductive anomaly.** Measured response changes are
  a few per cent, which is why surveys use many stations, several separations and
  repeat measurements.
- **The equivalence compresses the answer.** A factor ten in thickness moves the
  reported concentration by only $1.5$, so a wrong geometry produces a *plausible*
  wrong answer — the most dangerous kind.
- **Polarisation is the complement.** Where the conductivity contrast saturates,
  induced polarisation responds to surface chemistry
  ([09-03-04](../03-induced-polarisation/04-ip-applications.md)) and can separate
  a saline plume from a clay layer.

## 5. Assumptions and regime of validity

1. **A single-species, linear pore-fluid model** with a constant $\Lambda$.
   Real leachates are mixtures, and molar conductivity is concentration-dependent.
2. **A constant surface-conduction term.** In reality $\sigma_s$ depends on the
   pore-fluid concentration through the double layer, so the two terms are not
   independent; the model overstates their separability.
3. **Archie's law applies** — a clean, water-saturated granular medium. It is
   least reliable exactly where environmental targets are: clays, organic soils
   and partially saturated waste.
4. **A layered plume.** Real plumes have fingering geometry, gradients of
   concentration and sharp lateral edges; a one-dimensional model gives an upper
   bound on detectability.
5. **No time-lapse change during the survey** and no temperature effect, though
   leachate has a different temperature from the background.
6. **A stated noise threshold** ($5\%$ on $|H_s|$). Every threshold in Section 3.3
   scales with that.
7. **No free-phase or gas content**, which would change both the conductivity and
   the model.

## 6. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| concentration | $c$ | mol/m³ | 1 mol/m³ = 1 mM |
| molar conductivity | $\Lambda$ | S m²/mol | $\mathrm{S\,m^{-1}} / (\mathrm{mol\,m^{-3}})$ |
| formation factor | $F$ | — | $\phi^{-\mathrm{CEM}}$ |
| bulk conductivity | $\sigma_{\text{bulk}}$ | S/m | $\sigma_w/F + \sigma_s$ |
| conductance | $S$ | S | $\mathrm{S\,m^{-1}}\times\mathrm{m}$ |
| response ratio | — | — | unitless |

Check the conductance column of Section 3.3: at $t = 2$ m the required
concentration is $15.89$ mol/m³, so
$\sigma_w = 0.0126 \times 15.89 = 0.2002$ S/m,
$\sigma_{\text{bulk}} = 0.2002/6.617 + 0.0020 = 0.03225$ S/m, and
$S = 0.03225 \times 2.0 = 0.0645$ S — the printed value, so the arithmetic of the
table is checkable from its first column.

## 7. Worked examples

### Example 1 — is this leachate detectable?

A plume of $30$ mol/m³ and $4$ m thickness at $5$ m depth. Then
$\sigma_w = 0.0126 \times 30 = 0.378$ S/m,
$\sigma_{\text{bulk}} = 0.378/6.617 + 0.0020 = 0.0591$ S/m, so the layer's
conductivity is $0.0591$ S/m against a background of $0.02$ S/m — a factor $3.0$
contrast. Interpolating the measured table between the $10$ and $50$ mol/m³
columns at $t = 5$ m gives a response change of about $0.7\%$. **Against a $5\%$
threshold the plume is not detectable; against a $1\%$ threshold it is
marginal.** That is a statement about a stated noise level, not about the
chemistry.

### Example 2 — the same response from two different sites

From Section 3.3, a $5\%$ response can be produced by $15.89$ mol/m³ over $2$ m or
by $10.37$ mol/m³ over $20$ m. Since both give the same datum, a report that
states "$10$ mol/m³" has chosen one member of a family without saying so. The
honest statement is the family, plus whatever independent information (sampling,
hydrology, an IP measurement) selects inside it.

### Example 3 — where the surface term takes over

From Section 3.1 the surface term carries $51.2\%$ of the bulk conductivity at
$c = 1$ mol/m³. Setting the two contributions equal gives the crossover
concentration:

$$\frac{\Lambda c}{F} = \sigma_s
\;\Longrightarrow\;
c = \frac{\sigma_s F}{\Lambda} = \frac{0.0020 \times 6.617}{0.0126}
= 1.05\ \mathrm{mol/m^3}.$$

Below about $1$ mol/m³ of this assumed ion, an EM survey is mapping the soil's
surface chemistry, not the contaminant.

## 8. Python demonstration

`code/em_environmental_demo.py` prints every number in this lesson:

1. the concentration-to-conductivity chain through $\Lambda$, $F$ and
   $\sigma_s$, with the surface fraction at the most dilute concentration;
2. the measured plume response against concentration and thickness at $100$ Hz;
3. the detection threshold in concentration for four thicknesses, with the
   corresponding conductance;
4. the two limits of the model: surface-conduction domination at low
   concentration and conductance saturation at high concentration.

```bash
cd 09-electrical-em-methods/05-em-methods-applications/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_environmental_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/05-em-environmental-exercises.md`](./exercises/05-em-environmental-exercises.md)
and
[`exercises/05-em-environmental-solutions.md`](./exercises/05-em-environmental-solutions.md).

- **★** Compute $\sigma_{\text{bulk}}$ for $c = 25$ mol/m³ with the constants of
  Section 3.1.
- **★** From the response table, state the change produced by a $10$ m plume at
  $200$ mol/m³.
- **★★** Derive the crossover concentration at which the surface term equals the
  fluid term, and evaluate it for $F = 10$ and $\sigma_s = 0.005$ S/m.
- **★★** Using the threshold table, estimate the conductance required for a $5\%$
  response and state how it would scale with the stated threshold.
- **★★★** Design an environmental survey for a $5$ m thick plume at $10$ m depth
  with a $3\%$ detectability target, and state the band, the station spacing,
  the repeat policy and the statistic.

## 10. Common mistakes

1. **Reporting a concentration from a conductivity.** The petrophysical model
   stands between them, and it is not measured.
2. **Ignoring the surface term.** Measured $51.2\%$ of the bulk conductivity at
   $1$ mol/m³ comes from surfaces.
3. **Quoting a thickness from a single-frequency response.** The measured
   equivalence spans a factor ten in thickness at a factor $1.5$ in reported
   concentration.
4. **Choosing a threshold after the survey.** Every detection number in this
   lesson is a function of the stated $5\%$ noise level.
5. **Assuming a layered plume.** A three-dimensional plume has a smaller,
   different anomaly, and the one-dimensional model is optimistic.
6. **Treating conductivity and polarisation as redundant.** They respond to
   different things, which is why they are acquired together.

## 11. Real-world applications

- **Leachate mapping at landfills.** The conductive plume is the target; the
  geometry is the unknown.
- **Salt-water intrusion.** A sharp conductive front is the target, and its depth
  is often better constrained by its lateral continuity than by any single
  sounding.
- **Agricultural salinity.** Airborne and ground FDEM map apparent conductivity
  as a salinity proxy, with the caveats of [09-05-02](02-fem-conductivity-mapping.md).
- **Mine-impact and acid drainage.** The conductive signal is a mixture of
  dissolved solids and alteration, which is where a joint IP measurement helps.

## 12. Related lessons

- [09-05-02 FEM Conductivity Mapping and Apparent Conductivity](02-fem-conductivity-mapping.md) —
  the calibration, its regime and its averaging.
- [09-05-01 TEM Sounding for Aquifers and Mineral Targets](01-tem-sounding.md) —
  the kernel and the conductance equivalence.
- [09-01-02 Archie's Law, Porosity and Saturation](../01-electrical-properties-of-earth/02-archies-law.md) —
  the petrophysical step.
- [09-03-04 IP for Sulphides, Clays, Contaminants and Permafrost](../03-induced-polarisation/04-ip-applications.md) —
  the complementary measurement when the conductivity contrast saturates.
- [09-02-08 ERT Applications: Aquifers, Contamination, Landslides, Archaeology](../02-dc-resistivity/08-ert-applications.md) —
  the resistivity-imaging version of the same survey.

## 13. Self-assessment checklist

- [ ] I can compute $\sigma_w$ and $\sigma_{\text{bulk}}$ with stated constants.
- [ ] I can find the concentration at which surfaces take over from fluid.
- [ ] I can read the response table and state a detectability outcome.
- [ ] I can convert a threshold response into a conductance.
- [ ] I can state the concentration–thickness family for one datum.
- [ ] I can write an environmental EM report with its admitted range and
      threshold.
