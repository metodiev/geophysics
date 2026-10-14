---
id: 11-07-04
title: "Case Study: Arid-Region Groundwater Exploration"
level: research
prereqs: ["11-01-03", "11-05-01", "11-05-04"]
tags: [exploration-geophysics, case-studies, groundwater, arid, airborne-em, sustainability, base-rate]
---

# Case Study: Arid-Region Groundwater Exploration

## A statement of what this lesson does and does not assert

This lesson is about **how an arid-region groundwater case is argued and where it
breaks**. It quotes **no site-specific numbers** — no basin, aquifer, borehole,
yield, recharge rate, salinity or success rate for any real area. Every such
number belongs to a specific survey, a specific borehole record and a specific
hydrological assessment, and repeating one from memory would be exactly the
failure this curriculum forbids.

Consequently:

- The setting is described as an **argument archetype**: an arid region, a
  target aquifer, a salinity question and a sustainability question.
- If a real region or aquifer type is named, the naming is illustrative and **no
  factual claim and no site-specific number is made about it**.
- All quantitative content comes from
  `code/case_study_groundwater_demo.py`, whose inputs are **stated SYNTHETIC
  models**.
- Real numbers require the hydrogeological literature and the operator's
  records.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the posterior probability that a geophysical anomaly indicates a
   productive borehole, and **interpret** it as a dry-hole rate.
2. **Design** a staged survey (regional screening then local confirmation) and
   **compute** the cost per productive well of alternate strategies.
3. **Show** why maximising the number of wells found is not the objective, and
   **compute** the net value of each strategy.
4. **Compute** a water balance and a storage-depletion time, and **state** which
   quantity the geophysics does and does not measure.
5. **Compute** the value of information of a screening survey per site and
   **state** the accounting that most reports omit.
6. **Write** an exploration recommendation that separates what was measured, what
   was modelled and what was chosen, including the sustainability caveat.

## Prerequisites

- [11-01-03 Cost, Risk and Value of Information in Exploration](../01-exploration-workflow/03-cost-benefit.md)
  — the decision framework.
- [11-05-01 Geophysical Signatures of Aquifers and Saline Interfaces](../05-groundwater-exploration/01-aquifer-signatures.md)
  — what a conductivity anomaly does and does not mean.
- [11-05-04 Airborne EM for Regional Aquifer Mapping](../05-groundwater-exploration/04-airborne-groundwater.md)
  — the screening tool and its conductance equivalence.
- [14-01 Hydrology Fundamentals](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/01-hydrologic-cycle.md)
  — recharge, storage and the water balance.

> All models and data in this module are **SYNTHETIC**. No real basin, aquifer or
> borehole is used.

## 1. Intuition: the survey selects, the borehole decides, the balance limits

An arid-region groundwater programme has three questions, in order of how often
they are answered badly.

1. **Where is there water?** The geophysics answers this partially: it maps
   conductivity, which correlates with saturation, salinity and clay, and it maps
   structure, which controls where water can be stored. It does not measure
   productivity.
2. **Will a borehole be productive?** Only a borehole can say. The geophysics
   changes the odds, and the honest output of a survey is a *ranked list with an
   error rate*, not a map with targets marked.
3. **For how long?** Recharge, storage and abstraction, none of which a
   geophysical survey measures. A programme that answers (1) and (2) and ignores
   (3) is a mining operation on fossil water, whether or not that is intended.

This lesson builds the decision arithmetic for (1) and (2), and then states
plainly what (3) requires.

## 2. Precise definitions

### 2.1 Base rate and posterior

- **Base rate** $p$: the fraction of drilled sites in the region that prove
  productive, defined by an explicit threshold (a stated minimum yield and water
  quality).
- **Indicator performance**: $\mathrm{TPR} = P(\text{anomaly}\mid\text{productive})$
  and $\mathrm{FPR} = P(\text{anomaly}\mid\text{dry})$ for the survey's target
  criterion.

$$ \mathrm{PPV} = \frac{p\,\mathrm{TPR}}{p\,\mathrm{TPR}+(1-p)\,\mathrm{FPR}}. $$

### 2.2 Screening versus confirmation

- **Screening survey**: cheap, wide coverage, low specificity — airborne EM, or a
  regional gravity and magnetic survey. Its job is to reduce the area.
- **Confirmation survey**: more expensive, higher specificity — ground TDEM or
  ERT over the ranked anomalies, then a borehole.

The pairing matters because the two have different (TPR, FPR) and different
costs, and the optimal strategy is usually to spend money in that order.

### 2.3 Water balance

Over a region, at steady state, abstraction cannot exceed recharge without
drawing down storage:

$$ \text{recharge} = \text{rainfall} \times \text{recharge coefficient}
\times \text{area}, \qquad
t_{\text{depletion}} = \frac{\text{storage}}
{\text{abstraction} - \text{recharge}}. $$

Both the recharge coefficient and the storage are estimated from hydrology and
drilling, not measured by a geophysical survey.

## 3. Derivations

### 3.1 The posterior and the dry-hole rate

With the demonstration's synthetic values ($p = 0.15$, $\mathrm{TPR} = 0.60$,
$\mathrm{FPR} = 0.25$):

$$ \mathrm{PPV} = \frac{0.15(0.60)}{0.15(0.60)+0.85(0.25)}
= \frac{0.09}{0.3025} = 0.298. $$

The survey raises the chance from 15% to 30%, and **about 70% of the holes it
recommends are still dry.** The posterior moves steeply with the prior
(0.112 at $p = 0.05$, 0.615 at $p = 0.40$), which is why the same survey is a
success in one region and a failure in another.

### 3.2 Staged selection: cost per productive well

The demonstration compares three strategies over 100 candidate sites, with
synthetic costs (AEM $0.05$ per site, TDEM $0.5$ per site, a well $10$, a
productive well worth $60$), and with the two indicators conditionally
independent given the state:

| Strategy | Productive wells found | Programme cost | Cost per productive well | Net value |
|---|---|---|---|---|
| Drill blind | 15.00 | 1000.0 | 66.67 | $-100.0$ |
| AEM, then drill anomalies | 9.00 | 307.5 | 34.17 | $+232.5$ |
| AEM + TDEM, then drill | 7.65 | 128.5 | 16.80 | $+330.5$ |

The staged strategy **finds the fewest productive wells and creates the most
value**, because the expensive drilling is concentrated on the best-selected set.
Blind drilling finds the most water and loses money. **Maximising the number of
wells found is not the objective**; the objective is the value of the programme,
which counts the productive wells that the survey screened out as a cost.

### 3.3 What the geophysics cannot measure

The demonstration's synthetic balance uses a rainfall of $200\ \mathrm{mm\,yr^{-1}}$,
a recharge coefficient of $0.05$, and an area of $500\ \mathrm{km^{2}}$:

$$ \text{recharge} = 0.20 \times 0.05 \times 5\times10^{8} = 5.0\times10^{6}\
\mathrm{m^{3}\,yr^{-1}}. $$

At $0.5\times10^{6}\ \mathrm{m^{3}\,yr^{-1}}$ per well, that supports **10 wells
at steady state**. With 20 wells the abstraction is
$10\times10^{6}\ \mathrm{m^{3}\,yr^{-1}}$ and a stated storage of
$100\times10^{6}\ \mathrm{m^{3}}$ is drawn down in

$$ t = \frac{100\times10^{6}}{10\times10^{6}-5\times10^{6}} = 20\ \text{years}. $$

Both the recharge coefficient and the storage are estimates with wide ranges, and
neither is a geophysical product. **A survey that finds water has not established
that the water is renewable**, and the two statements must appear in the same
report or the report is misleading.

### 3.4 Value of information per site

With the demonstration's synthetic values:

$$ \mathbb{E}[\text{drill every site}] = p\,V - C = 0.15(60) - 10 = -1.00, $$

$$ \mathbb{E}[\text{survey, drill anomalies}] = -c_{\text{AEM}}
+ P(\text{anomaly})\left(\mathrm{PPV}\,V - C\right)
= -0.05 + 0.3025\left(0.298(60) - 10\right) = +2.33, $$

$$ \mathrm{VOI} = 2.33 - (-1.00) = +3.33\ \text{units per site}
= 66.5 \times \text{the survey cost}. $$

The accounting includes the productive wells the survey **missed**; a screening
survey's benefit is the change in the expected value of the whole programme, not
the number of holes saved. Most reports quote the latter, which overstates the
benefit because it ignores the missed wells.

## 4. Worked examples

### Example 1 — the same anomaly in two regions

A conductivity anomaly with $\mathrm{TPR} = 0.60$, $\mathrm{FPR} = 0.25$ is found
in a region with a $5\%$ base rate and in one with a $40\%$ base rate.

$$ \mathrm{PPV}_{5\%} = \frac{0.03}{0.03+0.2375} = 0.112, \qquad
\mathrm{PPV}_{40\%} = \frac{0.24}{0.24+0.15} = 0.615. $$

The same survey, the same anomaly: 11% versus 62%. **The prior is the regional
hydrogeology, and the survey only updates it.** A programme that cannot state its
prior has no defensible targeting logic.

### Example 2 — why the staged survey wins

From the table, blind drilling has a net value of $-100$; AEM screening alone
$+232.5$; AEM plus TDEM $+330.5$. The second stage costs $15.1$ units and removes
$21.7$ well-costs of drilling, at the price of forgoing $1.35$ productive wells —
a clear trade while a well costs a sixth of its value. If the well value fell
(from $60$ to, say, $20$), the ordering changes and the cheap screening alone
would win. **The optimal survey design depends on the value ratio, not on the
geophysics.**

### Example 3 — resource versus renewability

A survey identifies 20 drilling targets with a posterior of $0.298$. Drilling all
20 yields about 6 productive wells (Section 3.1). At
$0.5\times10^{6}\ \mathrm{m^{3}\,yr^{-1}}$ each, that is
$3.0\times10^{6}\ \mathrm{m^{3}\,yr^{-1}}$ against a recharge of
$5.0\times10^{6}\ \mathrm{m^{3}\,yr^{-1}}$ — within the balance, *if* the
recharge estimate is right. The recharge coefficient in an arid region is
typically the least certain number in the whole calculation, and it is not a
geophysical measurement. **State it, with its range, in the same report.**

## 5. Assumptions and regime of validity

1. **The base rate applies to the drilled population.** If the targets are
   pre-selected by the same anomaly criterion used as the test, the prior is
   already conditioned and the posterior is inflated.
2. **TPR and FPR are stable across the region.** They depend on target depth,
   salinity, clay content and regolith; a single pair is an average over very
   different ground.
3. **The two survey stages are conditionally independent given the state.** They
   are not if both respond to the same clay (a systematic shared false positive),
   in which case the staged strategy's specificity is overstated.
4. **Costs and values are synthetic.** They stand in for a real programme budget;
   the structure of the calculation is the lesson.
5. **The water balance is a steady-state, single-cell model.** Real aquifers have
   gradients, boundary flows and storage dynamics; the model here bounds the
   question rather than answering it.
6. **Water quality is not measured by the survey.** Salinity affects
   conductivity, so a conductive anomaly may indicate water that is unusable; the
   economic threshold must define "productive" to include quality.

## 6. Python demonstration

`code/case_study_groundwater_demo.py` prints:

1. the posterior and dry-hole rate for an AEM indicator at three base rates;
2. the three-strategy comparison (wells found, cost, cost per productive well,
   net value);
3. the water balance, sustainable well count and storage-depletion time;
4. the value of information per site and the missed-well accounting.

```bash
cd 11-exploration-geophysics/07-exploration-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_groundwater_demo.py
```

Companions:
[`exercises/04-case-study-groundwater-exercises.md`](./exercises/04-case-study-groundwater-exercises.md)
and
[`exercises/04-case-study-groundwater-solutions.md`](./exercises/04-case-study-groundwater-solutions.md).

## Common pitfalls

1. **Reporting a map of anomalies instead of a ranked list with an error rate.**
2. **Quoting the anomaly's detection rate without the FPR.** The posterior needs
   both.
3. **Skipping the prior.** The same anomaly is a 11% and a 62% chance in two
   regions.
4. **Optimising for wells found.** The staged strategy that finds fewer wells can
   create more value.
5. **Reporting water found without the balance.** A survey cannot measure
   recharge, and a borehole cannot measure renewability.

## Mastery checkpoint

Complete this without notes:

> A regional programme has 200 candidate sites, a $10\%$ base rate, and an AEM
> indicator with $\mathrm{TPR} = 0.65$ and $\mathrm{FPR} = 0.20$. A ground TDEM
> follow-up on anomalies has $\mathrm{TPR} = 0.85$ and $\mathrm{FPR} = 0.10$.
> **(a)** Compute the posterior after the AEM alone. **(b)** Compute the number of
> AEM anomalies per 200 sites, and the number of sites the TDEM stage would
> retain (assume conditional independence). **(c)** With a well cost of $10$ and
> a productive well worth $80$, compute the net value of (i) drilling all 200,
> (ii) AEM then drilling anomalies. **(d)** A rainfall of
> $150\ \mathrm{mm\,yr^{-1}}$, a recharge coefficient of $0.04$ and an area of
> $800\ \mathrm{km^{2}}$: compute the recharge in
> $\mathrm{m^{3}\,yr^{-1}}$, and state which part of this is a geophysical
> measurement.

A worked version of (a)-(c) is in the lesson-07-04
[solutions](./exercises/04-case-study-groundwater-solutions.md).

## Related modules

- [11-05 Groundwater Exploration Geophysics](../05-groundwater-exploration/README.md)
  — the methods used as evidence here.
- [11-01-03 Cost, Risk and Value of Information in Exploration](../01-exploration-workflow/03-cost-benefit.md).
- [11-07-01 Case Study: Porphyry Copper District](./01-case-study-porphyry.md),
  [11-07-02 Case Study: Basin Analysis and Play Assessment](./02-case-study-basin.md)
  and [11-07-03 Case Study: Geothermal Field Development](./03-case-study-geothermal.md).
- [14-01 Hydrology Fundamentals](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/01-hydrologic-cycle.md)
  and [14-06 Integrated Catchment Studies](../../14-hydrology-hydrogeophysics/06-integrated-catchment-studies/03-water-resource-assessment.md).

## Self-assessment checklist

- [ ] I can compute a PPV and interpret it as a dry-hole rate.
- [ ] I can design a two-stage survey and compare its cost per productive well.
- [ ] I can explain why the staged strategy can find the fewest wells and be best.
- [ ] I can compute a water balance and a depletion time.
- [ ] I can state which quantities are geophysical and which are hydrological.
- [ ] I can write a recommendation with a rounded error rate and a balance caveat.
