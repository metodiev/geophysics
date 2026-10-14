---
id: 11-06-04
title: "Landfill, Waste and Brownfield Site Assessment"
level: graduate
prereqs: ["11-06-01", "09-05-05", "10-03-01"]
tags: [exploration-geophysics, geotechnical, landfill, leachate, brownfield, electromagnetics, base-rate]
---

# Landfill, Waste and Brownfield Site Assessment

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the low-induction-number apparent conductivity as a weighted
   average of the subsurface conductivity, and **compute** the response of a
   layered waste section.
2. **Show** that the depth of a conductive anomaly cannot be read from its
   amplitude, and **quantify** the effect of a shallow versus a deeper target.
3. **Compute** the equivalence of a cap or plume in both an induction and a DC
   sounding, and **state** which parameter combination the data determine.
4. **Compute** the magnetic anomaly of a buried ferrous drum and of a
   magnetically susceptible soil body, and **show** that the soil is a
   first-order competitor, not noise.
5. **Compute** the false-discovery rate of a "conductive anomaly = contamination"
   rule and **explain** why the base rate dominates the interpretation.
6. **State**, for each method used on a waste site, the failure mode that
   produces a false negative.

## Prerequisites

- [11-06-01 Site Investigation: Objectives and Method Selection](./01-site-investigation.md)
  — the objective-and-method framework.
- [09-05-05 EM Methods in Environmental Studies](../../09-electrical-em-methods/05-em-methods-applications/05-em-environmental.md)
  — the field practice of the methods used here.
- [10-03-01 GPR in Hydrogeology](../../10-gpr-near-surface/03-gpr-applications/01-gpr-hydrogeology.md)
  — the dielectric method for cap and shallow structure.
- [11-05-02 EM and ERT for Groundwater Mapping](../05-groundwater-exploration/02-em-and-ert-groundwater.md)
  — the conductivity forward relations in their hydrogeological setting.

> All models and data in this module are **SYNTHETIC**. No real landfill, waste
> site, permit or monitoring result is used. The induction weighting used in the
> demonstration is an explicitly stated synthetic teaching kernel, not any
> instrument's response.

## 1. Intuition: a landfill is a designed system and a legacy problem

A modern engineered landfill is a structure: a low-permeability **liner**,
a **leachate** collection system, a **cap**, and gas management. Its geophysical
signature is therefore partly *designed*: the cap is often more resistive than
the waste, the leachate is conductive, and the liner is designed to be a barrier.
A legacy or unengineered waste site has no such order, and the survey is looking
for the geometry and the leakage rather than verifying a design.

In both cases the geophysical measurement is a *contrast*, and the interpretation
problem is the same as in
[11-05-01](../05-groundwater-exploration/01-aquifer-signatures.md): conductivity
responds to salinity, water content, clay and metal, and magnetics responds to
ferrous metal and to magnetic minerals. Neither responds to contamination as
such. A conductive plume may be leachate; it may also be a natural saline
groundwater body or a clay-rich unit. A magnetic anomaly may be a drum; it may
also be a pipeline, a fence, or a soil body with an elevated magnetite content.

The lesson derives the forward relations, measures the equivalence and the
clutter, and finishes with the base-rate arithmetic that says how often a flagged
anomaly is actually contamination.

## 2. Precise definitions

### 2.1 The site elements and their expected contrasts

| Element | Expected contrast | Method that sees it |
|---|---|---|
| Cap / cover | resistive, low density | GPR, EM, microgravity |
| Waste body | conductive, heterogeneous | EM, ERT, magnetics |
| Leachate plume | conductive (high TDS) | EM, ERT, SP |
| Gas | resistive, low density | GPR, microgravity (weakly) |
| Liner / clay barrier | resistive to conductive (varies) | ERT, GPR |
| Ferrous metal | strongly magnetic | magnetics, EM, GPR |
| Disturbed fill | mixed conductivity and density | ERT, EM, microgravity |

### 2.2 Apparent conductivity in the low-induction-number limit

A frequency-domain induction system measures a secondary field proportional, in
the **low-induction-number (LIN)** limit, to a depth-weighted integral of the
conductivity:

$$ \sigma_a = \int_0^{\infty}\sigma(z)\,K(z)\,\mathrm{d}z,
\qquad \int_0^{\infty}K(z)\,\mathrm{d}z = 1. $$

The kernel $K$ is a function of the coil geometry and height. In this lesson a
*synthetic* kernel is used explicitly,

$$ K(z) = \frac{z}{D}e^{-z^{2}/(2D)}, \qquad D = h^{2}/2, $$

whose peak is at $z = h$ and whose integral is 1; the demonstration verifies the
normalisation ($0.9998$). The conclusions about weighting and equivalence do not
depend on this particular form, but the numbers do, which is why the choice is
stated.

### 2.3 Clutter

**Clutter** is the population of non-target sources that produce an anomaly above
the threshold. On a brownfield site the clutter includes reinforcing steel,
services, made ground with slag or ash (ferrimagnetic), and magnetic soil.

## 3. Derivations

### 3.1 The reading is a weighted average

Because $\int K\,\mathrm{d}z = 1$, a **uniform** half-space of conductivity
$\sigma_0$ gives $\sigma_a = \sigma_0$ exactly: the kernel is calibrated to
recover the true conductivity when the ground is uniform. For a layer, the
*response* is the fraction of the kernel's weight inside the layer:

$$ \sigma_a = \sigma_{\text{bg}}
+ (\sigma_{\text{layer}}-\sigma_{\text{bg}})
\int_{\text{layer}}K(z)\,\mathrm{d}z. $$

With $h = 1.5\ \mathrm{m}$ (peak at 1.5 m) and a 5 m layer of
$0.30\ \mathrm{S\,m^{-1}}$ in a $0.02\ \mathrm{S\,m^{-1}}$ background, the
demonstration reports:

| Layer top (m) | $\sigma_a$ (S/m) | Kernel fraction in layer |
|---|---|---|
| 0.5 | 0.2733 | 0.9047 |
| 1.5 | 0.1265 | 0.3802 |
| 3.0 | 0.0255 | 0.0196 |
| 6.0 | 0.0200 | 0.0000 |

The reading is dominated by the top few metres: the same layer raises the
apparent value by a factor of 13 when it starts at 0.5 m, by 6 at 1.5 m, and by
1.3 at 3 m, and is invisible below 6 m. **A strong shallow anomaly and a weaker
deeper one produce the same number**, so amplitude alone does not give depth;
depth needs an inversion with its resolution attached, or a second method.

### 3.2 Equivalence: the same conductance, two sections

Consider two layers with the same conductance $S = \sigma h$: 10 m of
$0.05\ \mathrm{S\,m^{-1}}$ ($S = 0.5$ S) and 2.5 m of $0.20\
\mathrm{S\,m^{-1}}$ (also 0.5 S), both starting at 3 m. The demonstration gives

| Kernel peak | $\sigma_a$ for A (S/m) | $\sigma_a$ for B (S/m) | difference |
|---|---|---|---|
| 1.5 m (shallow system) | 0.0206 | 0.0235 | $+14.3\%$ |
| 6.0 m | 0.0432 | 0.0825 | $+91.0\%$ |
| 15.0 m (broad window) | 0.0346 | 0.0355 | $+2.5\%$ |

Whether a thickness is resolvable is a property of the **system and of the target
depth**, not of the ground: with a broad window the two equal-conductance models
are indistinguishable (2.5%, below a typical noise level), while a window peaked
in the layer separates them. For a DC sounding the same ambiguity appears as a
trade between the waste resistivity and the cap thickness: the log-sensitivity
Jacobian for a 150/5 $\Omega\,\mathrm{m}$ cap-over-waste model has singular
values $4.363$ and $2.098$ (condition number $2.08$) with the least-determined
direction $(+0.975, -0.222)$ — a more resistive waste with a thinner cap fits as
well as a more conductive waste with a thicker one.

### 3.3 Magnetic clutter: a drum and a soil body

A compact ferrous object is a dipole (see
[11-06-03](./03-buried-objects-uxo.md)), with $B_z = 2(\mu_0/4\pi)m/z^{3}$.
A magnetically susceptible soil body behaves the same way with
$m = \chi H V$. The demonstration uses a stated drum moment of
$200\ \mathrm{A\,m^{2}}$, a susceptibility $\chi = 10^{-3}$ SI, a field of
$40\ \mathrm{A\,m^{-1}}$ and a $5\times5\times5$ m block, giving a soil moment of
$5\ \mathrm{A\,m^{2}}$:

| Depth (m) | Drum (nT) | Soil block (nT) | Ratio |
|---|---|---|---|
| 1.0 | 40000.0 | 1000.00 | 40 |
| 2.0 | 5000.0 | 125.00 | 40 |
| 4.0 | 625.0 | 15.62 | 40 |

With a $1\ \mathrm{nT}$ threshold, a soil body produces an anomaly of the same
order as small metallic debris at several metres' depth. **The soil is not
noise; it is a target**, and it must be modelled or mapped out before a magnetic
survey can claim to find drums. This is the same point as the
magnetic-soil competition in the UXO lesson, at a larger scale.

### 3.4 From anomaly to contamination: the false-discovery rate

Let $p$ be the prior probability that a conductive anomaly is contamination,
$\mathrm{TPR}$ the probability that contamination produces the anomaly and
$\mathrm{FPR}$ the probability that a natural conductor does. Then

$$ \mathrm{PPV} = \frac{p\,\mathrm{TPR}}
{p\,\mathrm{TPR}+(1-p)\,\mathrm{FPR}},
\qquad \text{FDR} = 1-\mathrm{PPV}. $$

With the demonstration's stated values ($p = 0.15$, $\mathrm{TPR} = 0.90$,
$\mathrm{FPR} = 0.40$):

$$ \mathrm{PPV} = \frac{0.135}{0.135+0.340} = 0.284,
\qquad \mathrm{FDR} = 0.716. $$

**72 of every 100 conductivity anomalies flagged for investigation are natural
conductors.** The survey has raised the probability from 15% to 28% — a genuine
improvement, and still a two-in-three chance of a wasted investigation. The
posterior depends strongly on the prior ($0.106$ at $p = 0.05$, $0.600$ at
$p = 0.40$), and the prior is site history and geology, not the geophysics.

The practical consequence is that the survey's product should be a *ranked* list
with a stated error rate, and the follow-up must include a direct measurement
(pore-water sampling in a piezometer) that settles the question the geophysics
cannot.

## 4. Worked examples

### Example 1 — a cap and a plume in one induction survey

A landfill has a 1.5 m resistive cap ($0.005\ \mathrm{S\,m^{-1}}$) over a
conductive waste body ($0.20\ \mathrm{S\,m^{-1}}$) and a conductive leachate plume
($0.15\ \mathrm{S\,m^{-1}}$) extending 15 m below the waste. Using the
demonstration's kernel, a *shallow* system (peak 1.5 m) reads mostly the cap and
reports a low $\sigma_a$, whereas a *deeper* system (peak 15 m) averages the waste
and plume. Neither system alone separates cap, waste and plume: the cap thickness
and the waste conductivity trade, and the plume's conductance and depth trade.
The survey should therefore report a conductance map with an admitted range, and
a second method (GPR for the cap thickness, ERT for the plume geometry) should be
used to break the trades.

### Example 2 — reading a drum anomaly

A magnetic survey finds a $600\ \mathrm{nT}$ anomaly. From the demonstration's
drum model ($200\ \mathrm{A\,m^{2}}$), $600\ \mathrm{nT}$ corresponds to a depth
of about $4\ \mathrm{m}$:
$B_z = 2\times10^{-7}(200)/z^{3} = 4\times10^{-5}/z^{3}$; setting
$4\times10^{-5}/z^{3} = 600\times10^{-9}$ gives $z^{3} = 66.7$ and
$z = 4.05\ \mathrm{m}$. But a soil body of moment $5\ \mathrm{A\,m^{2}}$ would
give the same $600\ \mathrm{nT}$ at $z = 1.19\ \mathrm{m}$
($z^{3} = 1\times10^{-6}/6\times10^{-7} = 1.667$). The same anomaly is either a
drum at 4 m or a small magnetised soil feature at 1.2 m — and the two require
different responses. The shape of the anomaly over a grid, not its amplitude,
distinguishes them.

### Example 3 — is the flat conduct in the anomaly worth digging?

A site has a prior $p = 0.08$ that a conductivity anomaly is contamination, with
the same $\mathrm{TPR} = 0.90$ and $\mathrm{FPR} = 0.40$:

$$ \mathrm{PPV} = \frac{0.072}{0.072+0.368} = 0.164. $$

If a follow-up investigation costs $c$ and a missed contamination costs $20c$,
the expected cost of investigating every anomaly is
$c + 0.164(20c) = 4.28c$; of investigating none is
$0.08(20c) = 1.6c$. **Investigating every anomaly destroys value at this prior.**
The correct action is to raise the prior with historical records, or to add a
second, cheaper discriminator (for example a soil-gas or water sample at the
ranked top few), before committing to a full investigation.

## 5. Assumptions and regime of validity

1. **LIN approximation.** Valid at low induction numbers (low frequency, moderate
   conductivity). In highly conductive ground or at high frequency the response
   becomes non-linear in $\sigma$ and the simple weighted average fails.
2. **Synthetic kernel.** The demonstration's kernel is a teaching form. A real
   system's kernel differs, so the absolute apparent conductivity values are
   illustrative; the equivalence and weighting conclusions are robust.
3. **1-D interpretation.** Waste sites are three-dimensional and heterogeneous;
   a 1-D model of a 3-D body biases both the conductivity and the depth.
4. **Dipole model for magnetics.** Valid when the source is compact relative to
   its depth. An extended body requires a distributed model.
5. **Fixed TPR/FPR.** These are site- and criterion-specific. If the anomaly
   threshold is chosen after seeing the data, the computed PPV is optimistic.
6. **Contamination is a chemical state, not a physical property.** No method here
   detects it; all detect a property that correlates with it.

## 6. Python demonstration

`code/landfill_and_waste_demo.py` prints:

1. the synthetic kernel, its normalisation and the response of a 5 m layer at six
   depths, with the kernel fraction inside the layer;
2. the conductance equivalence in an induction reading for three kernel widths,
   and the DC-sounding Jacobian for a cap-over-waste model;
3. the magnetic anomaly of a drum and of a magnetised soil body at three depths;
4. the posterior probability and false-discovery rate of a conductive anomaly for
   three priors.

```bash
cd 11-exploration-geophysics/06-geotechnical-and-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python landfill_and_waste_demo.py
```

Companions:
[`exercises/04-landfill-and-waste-exercises.md`](./exercises/04-landfill-and-waste-exercises.md)
and
[`exercises/04-landfill-and-waste-solutions.md`](./exercises/04-landfill-and-waste-solutions.md).

## Common pitfalls

1. **Calling a conductive anomaly contamination.** Clay, saline groundwater and
   mineralisation all qualify; the FDR in Section 3.4 is the number to quote.
2. **Reading depth from amplitude.** A shallow strong and a deep weak anomaly are
   the same reading.
3. **Quoting a layer thickness.** Only the conductance is resolved unless the
   window is comparable to the layer.
4. **Treating magnetic soil as noise to be filtered.** It is a source; filter it
   and you filter real anomalies too.
5. **Surveying without a decision rule.** At a low prior, investigating every
   anomaly may cost more than the contamination it finds.

## Mastery checkpoint

Complete this without notes:

> A brownfield survey reports a $0.12\ \mathrm{S\,m^{-1}}$ apparent conductivity
> anomaly over a $0.03\ \mathrm{S\,m^{-1}}$ background, and a $1500\ \mathrm{nT}$
> magnetic anomaly. **(a)** Using the demonstration's kernel fraction table,
> estimate whether the conductive body is more likely shallow (top 0.5 m) or
> deeper (top 3 m), and state what would change your answer. **(b)** Using the
> drum and soil moments of Section 3.3, compute the depth implied by the magnetic
> anomaly for each source, and state which is more plausible for a brownfield.
> **(c)** With $p = 0.12$, $\mathrm{TPR} = 0.85$, $\mathrm{FPR} = 0.35$, compute
> the posterior probability that the conductivity anomaly is contamination.
> **(d)** State one direct measurement that would settle (c) and why the
> geophysics cannot.

A worked version of (b) and (c) is in the lesson-06-04
[solutions](./exercises/04-landfill-and-waste-solutions.md).

## Related modules

- [11-06-01 Site Investigation: Objectives and Method Selection](./01-site-investigation.md)
  — the decision framework.
- [11-06-02 Geophysics for Tunnels, Dams and Foundations](./02-tunnelling-and-dams.md)
  — seepage monitoring and the temperature tracer.
- [11-06-03 Buried Objects, UXO Detection and Clearance](./03-buried-objects-uxo.md)
  — clutter and the false-negative arithmetic.
- [11-05-02 EM and ERT for Groundwater Mapping](../05-groundwater-exploration/02-em-and-ert-groundwater.md)
  — the conductivity relations and their equivalence.
- [14-04 Contaminant and Environmental Geophysics](../../14-hydrology-hydrogeophysics/04-contaminant-and-environmental/01-contaminant-plumes.md)
  — plumes and their monitoring.
- [09-05-05 EM in Environmental Studies](../../09-electrical-em-methods/05-em-methods-applications/05-em-environmental.md).

## Self-assessment checklist

- [ ] I can derive the LIN weighted average and verify a kernel's normalisation.
- [ ] I can explain why amplitude does not give depth.
- [ ] I can state the conductance equivalence and what the data resolve.
- [ ] I can compute a drum and a soil magnetic anomaly and compare them.
- [ ] I can compute a PPV/FDR for an anomaly at a stated prior.
- [ ] I can name the false-negative mode of each method on a waste site.
