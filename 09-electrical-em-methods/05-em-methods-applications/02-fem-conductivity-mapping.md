---
id: 09-05-02
title: "FEM Conductivity Mapping and Apparent Conductivity"
level: advanced
prereqs: ["08-05-01", "09-01-01", "09-01-02", "09-05-01"]
tags: [electrical-methods, frequency-domain-em, apparent-conductivity, induction-number, low-induction-number, depth-of-exploration, equivalence]
---

# FEM Conductivity Mapping and Apparent Conductivity

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the in-phase and quadrature response of a coil pair over a
   homogeneous half-space and **state** the induction number that normalises it.
2. **Measure** the low-induction-number (LIN) power laws for the two channels and
   **explain** why a mapper recovers conductivity from the quadrature only.
3. **Quantify** where the LIN approximation fails and what that failure does to a
   reported conductivity.
4. **Define** apparent conductivity by a stated rule and **show**, with measured
   numbers, that a layered ground's apparent conductivity is a sensitivity-weighted
   average that corresponds to no layer.
5. **Measure** a median depth of exploration against coil separation and **state**
   why no fixed fraction of the separation is a depth rule.
6. **Demonstrate** that grounds differing by a factor of forty in both thickness
   and conductivity give apparent conductivities inside a narrow band.
7. **Report** an FDEM survey as an apparent conductivity with its geometry,
   frequency, calibration and admitted model family.

## Prerequisites

- [08-05-01 Frequency-Domain EM (FDEM) Systems and Responses](../../08-geomagnetism-electromagnetism/05-controlled-source-em/01-frequency-domain-em.md)
  — the coil systems and their responses.
- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../01-electrical-properties-of-earth/01-resistivity-conductivity.md)
  — the quantity being mapped.
- [09-01-02 Archie's Law, Porosity and Saturation](../01-electrical-properties-of-earth/02-archies-law.md)
  — why apparent conductivity is a proxy, not a porosity.
- [09-05-01 TEM Sounding for Aquifers and Mineral Targets](01-tem-sounding.md)
  — the same kernel and the same equivalence in the time domain.

**All models and data in this module are SYNTHETIC.** Conductivities, coil
separations, heights, frequencies and thresholds are chosen teaching values, not
measurements of any real ground or instrument.

---

## 1. Intuition: a number that means an average

A frequency-domain EM system reports two numbers per station: the in-phase and
the quadrature component of the secondary field, in parts per million of the
primary. Field practice converts one of them — the quadrature — into an
**apparent conductivity**, and the result is displayed as a map. The whole of
this lesson is about what that map is.

Two structural facts do the work.

- **The quadrature is linear in conductivity at low induction number.** That is
  what makes a single multiplicative calibration possible, and it is why a mapper
  can report conductivity rather than a dimensionless response.
- **The linearity holds only within a range of induction numbers, and the
  quantity it recovers is an average over a depth range set by the geometry.**
  Outside the range the calibration is wrong; inside it, the number is an average
  with a kernel to be stated.

## 2. Precise definitions

### 2.1 Response and induction number

For a coil pair of separation $r$ at height $h$ over a layered earth the complex
secondary-to-primary ratio is $H_s/H_p$, with $H_p = -1/(4\pi r^{3})$ per unit
moment (the free-space field on the coil plane). The conventional normalisation is

$$\theta = \frac{\omega\mu_0\sigma r^{2}}{4}.$$

### 2.2 Apparent conductivity, stated as a rule

**Definition used here:** the apparent conductivity is the conductivity of the
homogeneous half-space that reproduces the measured quadrature at the same
frequency, separation and height. Because the LIN quadrature is linear in $\sigma$,
this is a single scaling from a reference model.

### 2.3 Depth of exploration, stated as a rule

**Definition used here:** scale the conductivity of the top $z$ metres by $10\%$,
form the cumulative relative change in the quadrature, and take the depth at which
it reaches half of its saturated value. This is the same definition used for the
time-domain sounding in [09-05-01](01-tem-sounding.md), so the two are comparable.

## 3. Derivations

### 3.1 The response and the LIN channels

The kernel is the same validated integral as in lesson 01,

$$H_s = \frac{m}{4\pi}\int_0^{\infty}\lambda^{2}R(\lambda)
e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda ,$$

so every numerical statement inherits the validation recorded there
($1.21\times10^{-15}$ against a closed form, $6.81\times10^{-13}$ for a
stack-reduction test). For $\sigma = 0.05$ S/m, $r = 20$ m, $h = 0.5$ m:

| $f$ (Hz) | $\theta$ | in-phase (ppm) | quadrature (ppm) |
|---|---|---|---|
| 100 | 0.0039 | $-340.04$ | $-3570.75$ |
| 1000 | 0.0395 | $-8775.58$ | $-27\,943.77$ |
| 3162 | 0.1248 | $-38\,801.54$ | $-62\,912.78$ |
| 10 000 | 0.3948 | $-137\,551.98$ | $-83\,468.69$ |
| 31 620 | 1.2483 | $-292\,499.35$ | $+104\,591.47$ |

The quadrature is negative by the secondary-field convention (total minus
primary); the sign flips as the induction number passes unity, and the
*quadrature stops being monotone in conductivity* — which is the failure mode
discussed in Section 3.3.

### 3.2 The LIN power laws, measured

Over $10^{-4} \le \theta \le 10^{-2}$ the demonstration fits power laws:

$$\text{quadrature} \propto \theta^{0.9701}, \qquad
\text{in-phase} \propto \theta^{1.4723}.$$

The quadrature exponent is unity to within $3\%$ — the LIN statement that
conductivity is recoverable from that channel by a single calibration. The
in-phase channel rises faster, so it is **insensitive to conductivity at low
induction number** and only becomes informative as $\theta$ approaches unity.

### 3.3 Where the LIN calibration fails

The same fit extrapolated beyond its range:

| $\theta$ | quadrature (ppm) | LIN prediction (ppm) | error |
|---|---|---|---|
| 0.01 | $-8494.74$ | $-8494.74$ | $-0.00\%$ |
| 0.10 | $-55\,053.27$ | $-79\,301.61$ | $-44.05\%$ |
| 0.50 | $-72\,619.59$ | $-377\,898.38$ | $-420.38\%$ |
| 1.00 | $+36\,346.92$ | $-740\,310.32$ | $+2136.79\%$ |

The error passes $10\%$ well below $\theta = 1$, and beyond $\theta \approx 1$ the
sign flips: a LIN calibration applied there reports not merely a wrong number but
one of the wrong sign. **A large apparent conductivity is a warning, not an
achievement:** it means the datum sits outside the calibration's regime, and the
remedy is a lower frequency or a shorter separation, not a bigger
multiplicative factor.

### 3.4 What apparent conductivity is an average of

With the calibration fixed at $\sigma_{\text{ref}} = 0.05$ S/m, $f = 100$ Hz and
$r = 20$ m, the demonstration applies the rule to five grounds:

| ground | apparent $\sigma$ (S/m) | error against the top layer |
|---|---|---|
| homogeneous 0.05 S/m | 0.0500 | $+0.00\%$ |
| homogeneous 0.02 S/m | 0.0208 | $+3.81\%$ |
| 2 m of 0.5 S/m over 0.05 | 0.0635 | — |
| 10 m of 0.05 S/m over 0.01 | 0.0242 | — |
| 20 m of 0.02 S/m over 0.05 | 0.0318 | — |

The reference ground is recovered exactly by construction and a factor 2.5 change
in homogeneous conductivity to within $3.81\%$ — that residual *is* the LIN
nonlinearity at $\theta = 0.01$. Every layered ground is then reported as a single
number that corresponds to no layer: the $2$ m conductor over a resistive
half-space reads $0.0635$ S/m, and the $20$ m layer reads $0.0318$ S/m. **The
apparent conductivity is a sensitivity-weighted average, and it must never be
read as the conductivity of the top layer.**

### 3.5 Depth of exploration against separation

| separation (m) | frequency (Hz) | median depth (m) | depth / separation |
|---|---|---|---|
| 20 | 100 | 13.19 | 0.659 |
| 40 | 100 | 21.94 | 0.549 |
| 80 | 100 | 31.89 | 0.399 |

The depth of exploration grows with separation but **not proportionally**: the
measured ratio falls from $0.659$ to $0.399$ as the separation quadruples. So no
fixed fraction of the separation is a depth rule; the measured numbers, quoted
with the definition and the frequency, are the rule. Any remembered constant is a
coincidence of one survey.

### 3.6 Fortyfold changes, one narrow band of answers

| two-layer ground | apparent $\sigma$ (S/m) | quadrature (ppm) |
|---|---|---|
| 1 m of 1.0 S/m over 0.01 | 0.0211 | $-1508.39$ |
| 5 m of 0.2 S/m over 0.01 | 0.0361 | $-2580.30$ |
| 20 m of 0.05 S/m over 0.01 | 0.0352 | $-2514.69$ |
| 40 m of 0.025 S/m over 0.01 | 0.0231 | $-1647.16$ |

The four grounds differ by a factor of forty in both thickness and conductivity,
yet their apparent conductivities all fall inside a band spanning only $71\%$
($0.0211$ to $0.0361$ S/m). A single-frequency datum therefore reports a narrow
range of numbers for a wide family of grounds: **it constrains a conductance-like
average, and separating thickness from conductivity requires several separations
or several frequencies.** This is the same equivalence measured in the time
domain in [09-05-01](01-tem-sounding.md), seen from the frequency-domain side.

## 4. Physical interpretation

- **The map is an average over a depth kernel.** Two surveys with different
  separations at the same station produce different numbers; neither is "the"
  conductivity.
- **Linearity is a calibration, not a law.** It holds where $\theta \ll 1$; the
  measured error table gives the margin.
- **The in-phase channel is the diagnostic of a conductive ground.** It is
  uninformative in the LIN regime and informative exactly where the LIN
  calibration is failing, so a pair of channels carries more information than two
  calibrations of the same quantity.
- **Depth of exploration is a definition.** Stating it is what makes a
  comparison between two surveys meaningful.

## 5. Assumptions and regime of validity

1. **A horizontally layered, isotropic earth.** Lateral variation invalidates the
   half-space calibration in a way no single-frequency number can detect.
2. **The LIN regime** for the conductivity calibration: measured error $0\%$ at
   $\theta = 0.01$ and $-44\%$ at $0.1$.
3. **A loop (vertical magnetic dipole) approximation** for the coils, at a stated
   height; real coils have finite radius and orientation errors.
4. **No induced polarisation.** A polarisable ground adds a phase that a mapper
   reads as conductivity; [09-03-02](../03-induced-polarisation/02-ip-models.md)
   quantifies that.
5. **Quasi-static physics.** No displacement currents, so the dielectric
   properties of dry or frozen ground play no role here.
6. **The height is known.** It sets the near-surface sensitivity; a survey whose
   coil height varies reports a varying conductivity.
7. **The calibration reference is stated.** "Apparent conductivity" without the
   reference model and the LIN factor is not reproducible.

## 6. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| induction number | $\theta$ | — | $\mathrm{s^{-1}}\times\mathrm{H\,m^{-1}}\times\mathrm{S\,m^{-1}}\times\mathrm{m^{2}}$ |
| response | $H_s/H_p$ | — | pure ratio; ppm is $\times10^{6}$ |
| apparent conductivity | $\sigma_a$ | S/m | linear scaling of the quadrature at fixed geometry |
| separation, height, depth | $r$, $h$, $z$ | m | |

Check the ppm convention: $1\ \mathrm{ppm} = 10^{-6}$ of the primary. If a
quadrature is reported as $0.05$, the report is in fractions, not ppm, and every
calibration factor is off by a million.

## 7. Worked examples

### Example 1 — the induction number of a survey

A mapper with a $r = 20$ m separation at $f = 10$ kHz over ground of
$\sigma = 0.05$ S/m:

$$\theta = \frac{2\pi\times10^4 \times 4\pi\times10^{-7} \times 0.05 \times 400}{4}
= 0.3948 .$$

From the error table, $\theta = 0.3948$ sits between the $0.10$ and $0.50$
entries, so the LIN calibration is in error by more than $44\%$. The measured
quadrature at that entry is $-83\,468.69$ ppm, while the LIN prediction is
$-377\,898.38$ ppm — a factor $4.5$ apart. **The instrument is not faulty; the
calibration is out of its regime.**

### Example 2 — a factor of two in depth for a factor of four in separation

From Section 3.5, a $20$ m separation reaches $13.19$ m and an $80$ m separation
$31.89$ m. A factor four in geometry buys a factor $2.42$ in depth — a
$\sqrt{\text{geometry}}$ behaviour, which is the diffusive signature, not a
geometric one. Compare with the time-domain result of [09-05-01](01-tem-sounding.md),
where a factor $31.6$ in $\delta$ bought only a factor $1.45$ in median depth:
**the two methods trade geometry and band for depth in different ways, and both
fall short of the naive diffusion-depth estimate.**

### Example 3 — the honest answer for a two-layer ground

A survey reports $\sigma_a = 0.0361$ S/m at one station. From the measured family
of Section 3.6, that value is produced by a $5$ m layer of $0.2$ S/m over
$0.01$ S/m, but it is also within $71\%$ of three other grounds with thicknesses
from $1$ to $40$ m. The defensible report is: "apparent conductivity $0.0361$ S/m
at $100$ Hz and a $20$ m separation, consistent with a conductive layer whose
conductance lies between $0.021$ and $0.036$ S and whose thickness is unconstrained
by this single datum". That is less satisfying and more useful than a thickness.

## 8. Python demonstration

`code/fem_conductivity_mapping_demo.py` prints every number in this lesson:

1. the in-phase and quadrature response against the induction number, over the
   LIN regime and beyond;
2. the measured LIN exponents ($0.9701$ and $1.4723$) and the error table where
   the LIN calibration fails;
3. the apparent-conductivity rule applied to two homogeneous and three layered
   grounds;
4. the median depth of exploration for three separations;
5. the fortyfold-structure equivalence band.

```bash
cd 09-electrical-em-methods/05-em-methods-applications/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fem_conductivity_mapping_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/02-fem-conductivity-mapping-exercises.md`](./exercises/02-fem-conductivity-mapping-exercises.md)
and
[`exercises/02-fem-conductivity-mapping-solutions.md`](./exercises/02-fem-conductivity-mapping-solutions.md).

- **★** Compute $\theta$ for $r = 10$ m, $f = 25$ kHz and $\sigma = 0.02$ S/m,
  and state whether the LIN calibration applies.
- **★** From the measured response table, what is the quadrature at 100 Hz in ppm
  and in fractions of the primary?
- **★★** Using the two measured LIN exponents, state which channel a mapper
  should use and why, and what the other channel is useful for.
- **★★** Using the error table, estimate the induction number at which the LIN
  calibration error reaches $10\%$ by interpolation, and convert it into a
  maximum conductivity for a stated geometry and frequency.
- **★★★** Design a two-separation survey that separates two members of the
  equivalence family of Section 3.6, and state the statistic that decides.

## 10. Common mistakes

1. **Reading apparent conductivity as a layer conductivity.** It is a weighted
   average with a depth kernel.
2. **Using a single LIN calibration outside its regime.** Measured error $-44\%$
   at $\theta = 0.10$ and a sign flip beyond $\theta \approx 1$.
3. **Quoting a depth of exploration as a fixed fraction of the separation.**
   Measured $0.659$, $0.549$ and $0.399$ for the same frequency.
4. **Ignoring the coil height.** It sets the near-surface sensitivity.
5. **Treating the two channels as two independent conductivities.** They are two
   functionals of one response.
6. **Forgetting the polarisation contribution.** A polarisable ground adds phase
   that the calibration reads as conductivity.

## 11. Real-world applications

- **Soil salinity and agriculture.** Apparent conductivity is the standard proxy
  for salinity, with the caveat of Section 3.4.
- **Buried utilities and archaeology.** Small-separation systems map the shallow
  section where the depth of exploration is a few metres.
- **Mineral exploration from the air or by hand.** Conductors are mapped where
  the LIN regime does not hold, so the in-phase channel and a conductivity model
  are used instead of a calibration.
- **Permafrost and contamination.** Both are resistivity contrasts under a thin
  cover — the regime where an FDEM mapper is at its most quantitative.

## 12. Related lessons

- [09-05-01 TEM Sounding for Aquifers and Mineral Targets](01-tem-sounding.md) —
  the same kernel and equivalence in the time domain.
- [09-05-03 Marine CSEM for Hydrocarbon and Gas Hydrate Exploration](03-csem-marine.md) —
  the same response with a conductive water column above it.
- [08-05-01 Frequency-Domain EM (FDEM) Systems and Responses](../../08-geomagnetism-electromagnetism/05-controlled-source-em/01-frequency-domain-em.md) —
  the systems this lesson calibrates.
- [09-03-02 IP Models: Cole-Cole, Debye, Constant-Phase Element](../03-induced-polarisation/02-ip-models.md) —
  the polarisation phase that contaminates a conductivity calibration.
- [09-07-01 EM Noise, Coupling and Cultural Effects](../07-em-data-processing-and-qc/01-em-noise-and-coupling.md) —
  what else moves an apparent conductivity.

## 13. Self-assessment checklist

- [ ] I can compute an induction number and say whether LIN applies.
- [ ] I can state the measured LIN exponents and their meaning.
- [ ] I can apply a stated apparent-conductivity rule to a layered ground.
- [ ] I can measure a depth of exploration with a stated definition.
- [ ] I can state the equivalence band for a single-frequency datum.
- [ ] I can write an apparent-conductivity report with its geometry and
      calibration.
