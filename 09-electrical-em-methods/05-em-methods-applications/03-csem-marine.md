---
id: 09-05-03
title: "Marine CSEM for Hydrocarbon and Gas Hydrate Exploration"
level: research
prereqs: ["08-04-02", "08-05-04", "09-05-01", "09-01-02"]
tags: [electrical-methods, marine-em, csem, controlled-source, resistive-target, diffusion-depth, detectability, uncertainty]
---

# Marine CSEM for Hydrocarbon and Gas Hydrate Exploration

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why marine EM looks for a *resistor* in a conductive
   environment, and how that differs from a mineral conductor.
2. **Compute** the normalised magnitude (MVO) of a seafloor response and
   **interpret** its offset dependence for a stated target.
3. **Derive** the diffusive range limit of the water column and **state** the
   offsets at which the path is down 20 dB and 40 dB.
4. **Demonstrate** that the target's signature is non-monotone in offset and that
   the design frequency is set by the competition between the target response and
   the water attenuation.
5. **Measure** how little a single offset constrains a reservoir's resistivity and
   thickness, and **state** what the measurement does establish.
6. **State** the model's omissions — in particular the reflecting upper boundary
   of the water column — and why a two-sided layered solution is needed.
7. **Report** a marine EM anomaly as a detectability statement with its offset,
   frequency band and assumed section.

## Prerequisites

- [08-04-02 Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/02-magnetotellurics.md)
  — the layered impedance formulation that marine EM shares.
- [08-05-04 EM Inversion and Dimensionality](../../08-geomagnetism-electromagnetism/05-controlled-source-em/04-em-inversion.md)
  — what an inverted conductivity model can and cannot carry.
- [09-05-01 TEM Sounding for Aquifers and Mineral Targets](01-tem-sounding.md)
  — the diffusive window logic and the conductance equivalence.
- [09-01-02 Archie's Law, Porosity and Saturation](../01-electrical-properties-of-earth/02-archies-law.md)
  — why a hydrocarbon-filled or hydrate-bearing interval is resistive.

**All models and data in this module are SYNTHETIC.** Conductivities, water
depths, layer thicknesses, offsets, frequencies and thresholds are chosen
teaching values; no real prospect, vessel, reservoir or instrument is modelled.

---

## 1. Intuition: looking for a resistor through a conductor

Marine EM is the inverse of mineral EM. A hydrocarbon-bearing or hydrate-bearing
interval is electrically **resistive** (the pore fluid is non-conductive), while
the surrounding seawater-saturated section and the water column above it are
conductive. The measurement therefore asks a hard question: can a resistor hidden
below hundreds of metres of conductor be detected at all?

Two physics facts frame the answer.

- **The path through the water is a diffusion path.** Its amplitude falls as
  $\exp(-r/\delta)$ with $\delta = \sqrt{2/(\omega\mu_0\sigma_w)}$, which is
  *exact* and depends only on the water and the frequency. It sets the maximum
  offset, independent of the target.
- **The target's response is not monotone in offset.** Sensitivity to a resistor
  at a given depth peaks where the diffusion depth in the section is comparable
  to that depth, and falls on both sides. A survey is therefore designed around a
  transition, and the transition moves with target depth.

## 2. Precise definitions

### 2.1 The geometry modelled here

A horizontal loop on the sea surface (a vertical magnetic dipole at height
$h = 0.5$ m) over a layered **seafloor**, with the receiver at the same height and
offset $r$. The stack used throughout is
$1.0\ \mathrm{S/m}$ sediment of $100$ m, a reservoir layer, then a
$1.0\ \mathrm{S/m}$ basement; the reservoir is either $100$ m of
$0.02\ \mathrm{S/m}$ (**with**) or absent (**without**).

### 2.2 Normalised magnitude (MVO)

$$\mathrm{MVO}(r) = \frac{\left|H_s(r)\right|}{\left|H_p(r)\right|},
\qquad H_p = -\frac{1}{4\pi r^{3}}$$

per unit moment — the free-space (direct-path) field, which does not enter the
earth at all. The MVO is the standard display because it removes the geometric
spreading that both paths share.

### 2.3 The water-column attenuation

$$\frac{A(r)}{A(0)} = \exp\!\left(-\frac{r}{\delta}\right),
\qquad \delta = \sqrt{\frac{2}{\omega\mu_0\sigma_w}} .$$

## 3. Derivations

### 3.1 The response, with its kernel validation

The seafloor response is the same integral as in
[09-05-01](01-tem-sounding.md), with the stack declared in Section 2.1:

$$H_s = \frac{m}{4\pi}\int_0^{\infty}\lambda^{2}R(\lambda)
e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda ,$$

validated there to $1.21\times10^{-15}$ against a closed form and
$6.81\times10^{-13}$ against a stack-reduction test. Every number in this lesson
inherits that validation, and the truncation sweep in lesson 01 applies here too.

### 3.2 The measured signature of a reservoir

At $0.25$ Hz, with the reservoir at $200$ m depth:

| offset (m) | MVO without | MVO with | relative change |
|---|---|---|---|
| 500 | 0.071003 | 0.057511 | $-19.002\%$ |
| 1000 | 0.690248 | 0.669833 | $-2.958\%$ |
| 2000 | 2.958473 | 2.860091 | $-3.325\%$ |
| 4000 | 12.750447 | 12.763486 | $+0.102\%$ |
| 8000 | 76.313640 | 76.344389 | $+0.040\%$ |
| 16 000 | 190.971115 | 191.811429 | $+0.440\%$ |

The signature is $19.0\%$ at $500$ m, $3.0\%$ at $1$ km, $3.3\%$ at $2$ km, then
$0.1\%$ or less beyond. **It is not monotone in offset.** The naive expectation —
"longer offsets see deeper" — is wrong here, because the sensitivity to a
*resistive* layer is a competition between the diffusion depth in the section and
the layer's depth: at too short an offset the currents have not reached the
layer, at too long an offset the response is dominated by the deep section as a
whole.

### 3.3 The water column: an exact range limit

With $\sigma_w = 3.0$ S/m:

| $f$ (Hz) | $\delta$ (m) | $r$ at $-20$ dB (m) | $r$ at $-40$ dB (m) |
|---|---|---|---|
| 0.10 | 918.9 | 2116 | 4232 |
| 0.25 | 581.2 | 1338 | 2676 |
| 1.00 | 290.6 | 669 | 1338 |
| 4.00 | 145.3 | 335 | 669 |

(The $-20$ dB offset is $\delta\ln 10$ and the $-40$ dB offset is
$2\delta\ln 10$, both exact.) The range limit is set by the water and the
frequency and is **independent of the target**: at $0.1$ Hz the path is down
$20$ dB at $1.3$ km and $40$ dB at $2.7$ km, and at $4$ Hz the same landmarks are
at $0.2$ km and $0.3$ km. A marine survey therefore works at frequencies and
offsets far smaller than a land survey of the same target depth.

**An omission, stated.** The water column is not in the layered stack; its effect
enters only through this attenuation. The *upper* boundary of the water reflects,
which in reality adds a guided path that does not decay as $\exp(-r/\delta)$ and
which requires a two-sided layered solution. Every number in this lesson is a
one-sided (down-going) response, and the omission is a real limitation of the
model, not a detail.

### 3.4 The design frequency

The two effects move in opposite directions with frequency, so their product has
a maximum. At $2$ km offset:

| $f$ (Hz) | reservoir signature (%) | water attenuation at 2 km (dB) |
|---|---|---|
| 0.05 | $+0.983$ | $-26.74$ |
| 0.10 | $+0.623$ | $-37.81$ |
| 0.25 | $-0.295$ | $-59.78$ |
| 1.00 | $+0.018$ | $-119.57$ |
| 4.00 | $-0.000$ | $-239.14$ |

The measured entries put the optimum in the $0.05$–$0.1$ Hz range for this target
and offset, and it moves to lower frequencies as the offset grows, because the
water attenuation depends on $r/\delta$ while the target response does not. The
*sign* of the signature also changes across the band, which is a reminder that the
secondary field is a vector sum over the section: an interpretation must be made
against a model, not against a template.

### 3.5 What a single offset constrains

Replacing the reservoir's conductivity by a factor $200$ more resistive, at
$0.05$ Hz and $2$ km offset, changes the response by less than $0.1\%$ at every
thickness from $50$ to $400$ m:

| thickness (m) | response change for a $\times200$ resistivity change |
|---|---|
| 50 | $-0.028\%$ |
| 100 | $-0.050\%$ |
| 200 | $-0.078\%$ |
| 400 | $-0.073\%$ |

So the equivalence of a thin and a thick reservoir **cannot be resolved at this
offset and frequency**: the data establish that a resistor is present, and the
conductance they report is bounded only within tens of per cent. Resolving it
requires many offsets and several frequencies — one equation per datum against
three unknowns (depth, thickness, resistivity) — or an independent measurement
such as a seismic travel time that fixes the depth.

## 4. Physical interpretation

- **A marine EM anomaly is a detectability statement.** It says "a resistor of at
  least this conductance, at this depth, would be visible in this band at this
  offset", not "there is a reservoir".
- **The water column dominates the design.** Frequency and offset are chosen from
  the water, not from the target.
- **The signature's sign is model-dependent.** A band in which the target's
  contribution changes sign cannot be interpreted by a template.
- **The equivalence is the honest output.** A conductance with an admitted range
  of thickness–resistivity pairs is the report; a resistivity is not.

## 5. Assumptions and regime of validity

1. **One-dimensional (layered) seafloor.** Real prospects are three-dimensional;
   a 3-D resistor's anomaly is smaller and differently shaped.
2. **One-sided response.** The reflecting sea surface is omitted (Section 3.3).
3. **Quasi-static diffusion.** No displacement currents; valid for seawater at
   these frequencies.
4. **A loop source at a stated height**, with the receiver at the same depth.
   Real systems tow a horizontal electric dipole; the diffusive window logic is
   shared, the geometry is not.
5. **No anisotropy.** Resistivity anisotropy in shale-prone sections is common
   and changes the response.
6. **No noise model.** The detectability thresholds used are structural
   ($1\%$–$5\%$); a real survey's noise enters on top.
7. **The petrophysical step is separate.** A resistivity is not a saturation;
   the conversion needs Archie's law and its own assumptions.

## 6. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| diffusion depth | $\delta$ | m | $\sqrt{\mathrm{s}/(\mathrm{H\,m^{-1}\,S\,m^{-1}})}$ |
| MVO | $H_s/H_p$ | — | unitless |
| attenuation | $\exp(-r/\delta)$ | — | $r/\delta$ unitless |
| dB | — | — | $20\log_{10}A$; $-20$ dB corresponds to $\delta\ln 10$ |

Check the dB relation used in the table: $-20\ \mathrm{dB} = 10^{-1}$ in
amplitude, so $\exp(-r/\delta) = 0.1$ gives $r = \delta\ln 10 = 2.3026\,\delta$,
and the table's $918.9$ m against $2116$ m confirms it.

## 7. Worked examples

### Example 1 — the maximum useful offset in 300 m of water

At $0.25$ Hz, $\delta = 581.2$ m (measured). The offset at which the water path is
down $20$ dB is $\delta\ln 10 = 1338$ m. So a target whose signature is a few per
cent must be sought inside roughly a kilometre, and the exact limit scales as
$1/\sqrt{\sigma_w f}$: halving the water conductivity extends it by $\sqrt2$.

### Example 2 — the design frequency moves with offset

From Section 3.4 the optimum for a $200$ m deep target at $2$ km offset lies in
$0.05$–$0.1$ Hz. Moving to $4$ km, the water attenuation at fixed frequency
doubles in dB, so the optimum moves to a lower frequency by roughly a factor
$(\text{offset ratio})^{2}$ — i.e. about a factor $4$. **The optimal frequency
scales approximately as $1/r^{2}$**, which is the statement that a fixed number of
skin depths in the water column is the design rule.

### Example 3 — how much can be claimed from one offset

At $2$ km and $0.05$ Hz a factor $200$ change in reservoir resistivity moves the
response by $\le0.1\%$ (Section 3.5). At a stated $1\%$ noise level the datum
therefore cannot distinguish any of the four thicknesses from each other or from
their factor-$200$ resistivity variations. The only defensible claim is:
"the response is consistent with a resistive interval whose conductance is
approximately $S = \sigma h$ within a factor of a few, at a depth fixed by the
band". That is a real geophysical result; it is simply not a reservoir
characterisation.

## 8. Python demonstration

`code/csem_marine_demo.py` prints every number in this lesson:

1. the layered seafloor model, the direct-path primary field and the response;
2. the MVO against offset with and without the reservoir, showing the
   non-monotone signature;
3. the water-column attenuation table with the exact $-20$ dB and $-40$ dB
   offsets;
4. the reservoir signature against frequency at fixed offset, with the competing
   water attenuation;
5. the sensitivity of the response to a factor-$200$ change in reservoir
   resistivity at four thicknesses.

```bash
cd 09-electrical-em-methods/05-em-methods-applications/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python csem_marine_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-csem-marine-exercises.md`](./exercises/03-csem-marine-exercises.md)
and
[`exercises/03-csem-marine-solutions.md`](./exercises/03-csem-marine-solutions.md).

- **★** Compute $\delta$ at $0.1$ Hz for $\sigma_w = 3$ S/m and the offset at
  $-40$ dB.
- **★** From the MVO table, state the offset at which the reservoir signature is
  largest and its value.
- **★★** Derive the $-20$ dB offset $\delta\ln 10$ from
  $\exp(-r/\delta) = 0.1$, and evaluate it in $500$ m of water at $0.25$ Hz.
- **★★** Using the signature table at $2$ km, estimate the frequency that
  maximises the *product* of the signature and the amplitude attenuation, and
  state the approximation you used.
- **★★★** Design a multi-offset acquisition that constrains the reservoir's
  conductance to within $25\%$, given the sensitivity measured in Section 3.5,
  and state the statistic.

## 10. Common mistakes

1. **Assuming longer offsets always see deeper.** The measured signature is
   non-monotone, with a maximum at a few hundred metres.
2. **Ignoring the water column when choosing a frequency.** It sets the range
   limit and is independent of the target.
3. **Reading an MVO anomaly as a reservoir.** It is a detectability statement
   about a conductance.
4. **Treating a sign change across the band as noise.** It is the vector sum of
   the section's contributions.
5. **Quoting a reservoir resistivity from a single offset.** The measured
   sensitivity is under $0.1\%$ for a factor-$200$ change.
6. **Forgetting the reflecting sea surface.** A one-sided model omits a real
   guided path.

## 11. Real-world applications

- **Hydrocarbon exploration.** Marine CSEM is used as a *risk-reduction* tool,
  acquired jointly with seismic, precisely because it detects a resistor rather
  than a structure.
- **Gas hydrates.** Hydrate-bearing sediment is resistive in the same way, and
  the same window logic applies with a shallower target.
- **Salinity and groundwater discharge.** The same measurement maps conductive
  pore fluids where the target is a conductor, and it shares all the design
  constraints above.
- **Monitoring.** Time-lapse marine EM has been proposed for reservoir
  surveillance; the detectability question is exactly Section 3.5's.

## 12. Related lessons

- [09-05-01 TEM Sounding for Aquifers and Mineral Targets](01-tem-sounding.md) —
  the kernel, the validation and the conductance equivalence.
- [09-05-02 FEM Conductivity Mapping and Apparent Conductivity](02-fem-conductivity-mapping.md) —
  the calibration logic of the frequency-domain measurement.
- [08-04-02 Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/02-magnetotellurics.md) —
  the layered impedance formulation.
- [08-05-04 EM Inversion and Dimensionality](../../08-geomagnetism-electromagnetism/05-controlled-source-em/04-em-inversion.md) —
  how a conductivity model is obtained from the data.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the framework for
  the equivalence measured here.

## 13. Self-assessment checklist

- [ ] I can compute $\delta$ and a $-20$ dB offset in the water column.
- [ ] I can read an MVO table and state the measured signature of a target.
- [ ] I can explain why the signature is non-monotone in offset.
- [ ] I can state what a single offset does and does not constrain.
- [ ] I can state the model's omissions and what replaces them.
- [ ] I can write a detectability report for a marine target.
