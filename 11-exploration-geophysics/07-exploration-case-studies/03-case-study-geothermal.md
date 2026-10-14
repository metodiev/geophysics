---
id: 11-07-03
title: "Case Study: Geothermal Field Development"
level: research
prereqs: ["11-01-03", "11-04-01", "11-04-02"]
tags: [exploration-geophysics, case-studies, geothermal, magnetotellurics, resource-estimation, induced-seismicity]
---

# Case Study: Geothermal Field Development

## A statement of what this lesson does and does not assert

This lesson is about **how a geothermal development case is argued and where it
breaks**. It quotes **no site-specific numbers** — no field, resource, capacity,
temperature, flow rate, permeability or seismicity rate for any real area. Every
such number belongs to a specific field, a specific operator and a specific
reporting convention, and repeating one from memory would be exactly the failure
this curriculum forbids.

Consequently:

- A geothermal field is described here as an **argument archetype**: a thermal
  anomaly, a permeable reservoir, a working fluid and a seal or cap.
- If a real field or region is named, the naming is illustrative and **no
  factual claim and no site-specific number is made about it**.
- All quantitative content comes from
  `code/case_study_geothermal_demo.py`, whose inputs are **stated SYNTHETIC
  models**.
- Real numbers require the operator's reports and the primary literature.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a stored-heat resource estimate with an explicit distribution and
   **report** it as a P90/P50/P10 range rather than a single number.
2. **Show** that the resource uncertainty is dominated by geometric and thermal
   parameters, not by the geophysics.
3. **Compute** the number of wells implied by a flow-rate distribution and
   **explain** the distinction between resource and reserve.
4. **Compute** the posterior probability that a magnetotelluric conductor
   indicates a productive reservoir, and **state** what the method cannot
   distinguish.
5. **Compute** the probability of exceeding a magnitude threshold from a
   Gutenberg-Richter relation, and **relate** it to a traffic-light decision.
6. **Write** a geothermal assessment that separates measurement, model and
   choice, including the two different uncertainties (resource and seismicity).

## Prerequisites

- [11-01-03 Cost, Risk and Value of Information in Exploration](../01-exploration-workflow/03-cost-benefit.md)
  — the decision framework.
- [11-04-01 Geophysical Signatures of Geothermal Reservoirs](../04-geothermal-exploration-geophysics/01-geothermal-signatures.md)
  — the target signatures used here.
- [11-04-02 Magnetotellurics for Geothermal Resource Assessment](../04-geothermal-exploration-geophysics/02-mt-for-geothermal.md)
  — the method whose ambiguity is quantified in Section 3.3.
- [06-12-05 Documented Case Studies: Attribution](../../06-seismology/12-induced-and-triggered-seismicity/05-case-studies-induced.md)
  — the same archetype discipline for induced seismicity.

> All models and data in this module are **SYNTHETIC**. No real field, well,
> resource estimate or seismicity catalogue is used.

## 1. Intuition: two different uncertainties in one project

A geothermal development carries two uncertainties that are usually reported
separately and should be reported together.

- **The resource uncertainty**: how much heat is in place, and how much of it can
  be produced. This is a *geological and engineering* uncertainty, dominated by
  the reservoir's volume, temperature and permeability.
- **The induced-seismicity uncertainty**: what the operation does to the rock's
  state of stress. This is a *decision* uncertainty, because it is governed by
  which wells are drilled, at what injection pressure and rate, and for how long.

The two are coupled through the same reservoir: a permeable, fractured reservoir
is both the target of the development and the medium that transmits pore-pressure
changes to faults. The geophysical contribution differs for each. For the
resource it is MT (the clay cap and the resistivity structure), gravity and
microseismic imaging of the fracture network. For the seismicity it is a
monitoring network, and the honest statement is that detection capability and
traffic-light thresholds are choices, not measurements.

## 2. Precise definitions

### 2.1 The geothermal argument archetype

| Element | Evidence | False positive |
|---|---|---|
| Heat source | Regional heat flow, volcanic or extensional setting | A hot but impermeable and dry basement |
| Permeable reservoir | Microseismicity, MT structure, well tests | A conductive clay alteration zone with no permeability |
| Working fluid | Water chemistry, well testing | Fluid present but at an uneconomic temperature or salinity |
| Cap / seal | Conductive clay layer on MT | Conductive brine or graphitic rock, not clay |
| Access | Distance, land status, infrastructure | (non-geophysical) |

### 2.2 Stored heat

The heat in place above a reference temperature is

$$ H = \rho c\,V\,(T - T_{\text{ref}}), $$

with $\rho c$ the volumetric heat capacity of the rock-plus-fluid system
($\mathrm{J\,m^{-3}\,K^{-1}}$), $V$ the reservoir volume, and $T$ the reservoir
temperature. The **recoverable** heat multiplies by a recovery factor, which is
an engineering parameter, not a geological one.

### 2.3 Resource, reserve and the flow-rate constraint

- **Resource**: heat in place, or recoverable heat, with a distribution.
- **Reserve**: the part that can be produced economically, which requires a
  **flow rate**. A reservoir with enormous stored heat and negligible permeability
  has no reserve.

The chain is: heat in place → recoverable heat → wells needed → flow rate →
power → revenue. Each link has its own uncertainty, and the *last* one (the flow
rate) usually dominates the economic outcome.

### 2.4 Seismicity from a magnitude-frequency relation

For a Gutenberg-Richter relation $\log_{10}N(\ge M) = a - bM$, the conditional
probability that an event exceeds $m$ given it exceeds $m_0$ is

$$ P(M \ge m \mid M \ge m_0) = 10^{-b(m-m_0)}, $$

so the expected number of events above $m$ in a sequence of $N$ events is
$N\,10^{-b(m-m_0)}$. The **traffic-light threshold** is a decision about which
tail risk to accept, expressed as an action, not a physical constant.

## 3. Derivations

### 3.1 Stored heat with a distribution

The demonstration samples three parameters from triangular distributions
(synthetic teaching values): area $5$-$40\ \mathrm{km^{2}}$, thickness
$0.3$-$2.0\ \mathrm{km}$, and temperature above reference $40$-$150\ \mathrm{K}$,
with $\rho c = 2.5\times10^{6}\ \mathrm{J\,m^{-3}\,K^{-1}}$, and reports

| Percentile | Heat in place |
|---|---|
| P90 (conservative) | $2.17\ \mathrm{EJ}$ ($602\ \mathrm{TWh_{thermal}}$) |
| P50 | $4.77\ \mathrm{EJ}$ ($1325\ \mathrm{TWh_{thermal}}$) |
| P10 | $9.33\ \mathrm{EJ}$ ($2591\ \mathrm{TWh_{thermal}}$) |

The ratio P10/P90 is $4.3$. With a stated recovery factor of $0.10$ the
recoverable heat is $0.22\ \mathrm{EJ}$ (P90) to $0.93\ \mathrm{EJ}$ (P10).

Two things are worth noting. First, the range comes almost entirely from the
**area, thickness and temperature** — the parameters that geophysics constrains
only indirectly — not from the instrument. Second, the convention that **P90 is
the conservative estimate** (a 90% probability of *exceeding* it) means a report
that quotes "the P90 resource" is quoting the low case in that convention. State
the convention, because the same words mean the opposite in some industries.

### 3.2 Resource is not reserve

The demonstration samples a well flow rate (triangular, $20$-$80\
\mathrm{kg\,s^{-1}}$, synthetic) and converts it to electric power with a
conversion factor and a wellhead temperature drop:

$$ P_{\text{well}} = \frac{\dot m\,c_p\,\Delta T_{\text{wh}}\,\eta}{10^{6}}
\ \mathrm{MWe}, $$

with $c_p = 4200\ \mathrm{J\,kg^{-1}\,K^{-1}}$ and $\eta = 0.10$ (stated teaching
values). The result:

| Percentile of well output | Power per well (MWe) | Wells for 30 MWe |
|---|---|---|
| P10 | 1.30 | 23.1 |
| P50 | 1.90 | 15.8 |
| P90 | 2.71 | 11.1 |

The well count spans a factor of two between the P10 and P90 flow outcomes. **A
stored-heat number with no flow-rate distribution cannot size a plant**, which is
the operational content of the sentence "resource is not reserve".

### 3.3 The MT conductor: what it does and does not say

A conductive layer is the classic MT signature of the clay cap above a
geothermal reservoir — and also of conductive brine, graphite, or a
clay-rich sedimentary unit with no reservoir at all. As a test, with the
demonstration's synthetic values ($P(\text{productive}) = 0.30$,
$P(\text{conductor}\mid\text{productive}) = 0.85$,
$P(\text{conductor}\mid\text{dry}) = 0.55$):

$$ \mathrm{PPV} = \frac{0.30(0.85)}{0.30(0.85)+0.70(0.55)}
= \frac{0.255}{0.640} = 0.398. $$

The conductor raises the chance from 30% to 40%, and **60% of conductors still
overlie a non-productive target**. The posterior depends steeply on the prior
(0.147 at $p = 0.10$, 0.699 at $p = 0.60$).

MT provides structure and a **conductance**, not permeability and not
temperature directly. Distinguishing a smectite clay cap (a seal, and therefore
favourable) from a saline conductor (which could be productive or not) requires
something else: a temperature-gradient well, a fluid sample, or a resistivity
spectrum that separates clay conduction from electrolytic conduction.

### 3.4 Seismicity from the sequence

With the demonstration's stated $b = 1.0$ and a synthetic sequence of $2000$
events above $M = 0$:

| $m$ | $P(M \ge m \mid M \ge 0)$ | Expected number in the sequence |
|---|---|---|
| 1.0 | 0.100 | 200.0 |
| 2.0 | 0.010 | 20.0 |
| 3.0 | 0.001 | 2.0 |
| 4.0 | $10^{-4}$ | 0.2 |

$P(M \ge 2.5) = 0.0032$, so **6.3 events of $M \ge 2.5$ are expected per 2000
catalogued events** at $b = 1$. The probability of a large event is set by the
$b$-value and the number of events, not by the operator's intent. A traffic-light
threshold at $M = 2.5$ is therefore a decision to accept about 6 such events per
2000, and the response action (reduce rate, stop injection) is what the threshold
buys. **Report the expected event count at the threshold, not just the
threshold.**

Two honest caveats: the $b$-value is estimated from a catalogue whose
completeness magnitude is itself estimated, and induced sequences often have
$b$-values above the tectonic value, so extrapolating from a tectonic $b$ to an
induced sequence is a model choice.

## 4. Worked examples

### Example 1 — a stored-heat estimate and what it is worth

A reservoir has (all stated synthetic values) an area of $15\ \mathrm{km^{2}}$, a
thickness of $1.0\ \mathrm{km}$ and a temperature $100\ \mathrm{K}$ above the
reference:

$$ V = 15\times10^{6}\,\mathrm{m^{2}} \times 10^{3}\,\mathrm{m}
= 1.5\times10^{10}\ \mathrm{m^{3}}, $$
$$ H = (2.5\times10^{6})(1.5\times10^{10})(100) = 3.75\times10^{18}\ \mathrm{J}
= 3.75\ \mathrm{EJ}. $$

At a recovery factor of $0.10$, the recoverable heat is
$0.375\ \mathrm{EJ} = 1.04\times10^{5}\ \mathrm{GWh_{thermal}}$. Dividing by a
plant life (say 30 years) and a conversion efficiency ($\eta = 0.10$) gives an
order-of-magnitude electrical average of

$$ \frac{0.375\times10^{18} \times 0.10}{30 \times 3.156\times10^{7}\ \mathrm{s}}
\approx 39.6\ \mathrm{MWe}, $$

which is *not* a reserve: it is the average that the stored heat would support if
all of it could be produced, which requires wells that have not been tested.
**The number to report is the range and the flow-rate constraint, not this
quotient.**

### Example 2 — the prior decides whether to drill

An MT conductor has PPV $0.398$ at a prior of $0.30$. If a slim hole costs $C$
and a confirmed resource is worth $20C$, the expected value of drilling is
$0.398(20C) - C = 6.96C$ — strongly positive. But at a prior of $0.10$ the
posterior is $0.147$ and the expected value is $0.147(20C) - C = 1.94C$ — still
positive, though far weaker. The calculation is dominated by the value ratio, not
by the MT resolution; the useful question is whether the *prior* is well
established, because that is what moves the answer by a factor of three.

### Example 3 — a traffic-light threshold as a decision

At $b = 1$ and a forecast sequence of 2000 events, the expected count above
$M = 2.5$ is 6.3 (Section 3.4). A protocol that stops injection after any $M \ge
2.5$ will therefore stop the operation several times in a typical sequence,
regardless of any fault-specific concern. Whether that is acceptable is an
operator and regulator decision; what the geophysics supplies is the detection
capability (can the network locate a $M = 1.5$ event, and how far?) and the
catalogue's completeness, so that the forecast sequence length is not itself
cooked.

## 5. Assumptions and regime of validity

1. **Stored heat** assumes a single temperature, a uniform volumetric heat
   capacity, and a definable volume. Real reservoirs are heterogeneous and have a
   temperature distribution; the range in the estimate usually underestimates the
   structural uncertainty.
2. **Recovery factor** is an engineering assumption, highly site-specific, and
   the single largest multiplier on the resource number.
3. **Flow rate** is not predicted by any surface geophysical method. It comes
   from well testing; the distribution used here is a placeholder.
4. **MT posterior** assumes the prior and the two likelihoods are known. In
   practice they are elicited or borrowed from analogue fields, and the FPR is
   the least well known.
5. **Gutenberg-Richter extrapolation** assumes a constant $b$-value and a
   catalogue complete to $m_0$. Induced sequences violate both to some degree;
   the forecast should be presented with its catalogue and its completeness
   assumption.
6. **Two uncertainties, one decision.** A development decision requires both the
   resource distribution and the seismicity risk profile, and the two are coupled
   through the injection scenario.

## 6. Python demonstration

`code/case_study_geothermal_demo.py` prints:

1. the stored-heat distribution (P90/P50/P10) with its recoverable fractions;
2. the well-output distribution and the well count implied by a target capacity;
3. the MT conductor posterior for three priors;
4. the Gutenberg-Richter exceedance probabilities, expected counts and the
   $M \ge 2.5$ expectation.

```bash
cd 11-exploration-geophysics/07-exploration-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_geothermal_demo.py
```

Companions:
[`exercises/03-case-study-geothermal-exercises.md`](./exercises/03-case-study-geothermal-exercises.md)
and
[`exercises/03-case-study-geothermal-solutions.md`](./exercises/03-case-study-geothermal-solutions.md).

## Common pitfalls

1. **Reporting a single resource number.** The distribution is the answer; a
   P50 hides a factor of four.
2. **Confusing resource with reserve.** Without a flow rate there is no reserve.
3. **Treating an MT conductor as a well location.** The conductor maps a cap or
   a brine; permeability is not measured.
4. **Quoting a traffic-light threshold without the expected event count.** The
   threshold implies a number of stoppages, and the number is the decision.
5. **Reporting the resource and the seismicity risk separately.** They share the
   reservoir and the injection scenario, and the coupling is the project.

## Mastery checkpoint

Complete this without notes:

> A geothermal prospect has (all synthetic) an area of $10\ \mathrm{km^{2}}$, a
> reservoir thickness of $0.8\ \mathrm{km}$ and a temperature $120\ \mathrm{K}$
> above reference, with $\rho c = 2.5\times10^{6}\ \mathrm{J\,m^{-3}\,K^{-1}}$,
> recovery factor $0.08$. **(a)** Compute the heat in place and the recoverable
> heat. **(b)** If a well yields $40\ \mathrm{kg\,s^{-1}}$ at
> $\Delta T = 90\ \mathrm{K}$ with $c_p = 4200\
> \mathrm{J\,kg^{-1}\,K^{-1}}$ and $\eta = 0.10$, compute the wells needed for
> $25\ \mathrm{MWe}$. **(c)** An MT conductor has
> $P(\text{conductor}\mid\text{productive}) = 0.8$ and
> $P(\text{conductor}\mid\text{dry}) = 0.5$; with a prior of $0.2$, compute the
> posterior. **(d)** At $b = 1$ and a forecast of 5000 events above $M = 0$,
> compute the expected number of $M \ge 2.0$ events and state how it enters a
> traffic-light decision.

A worked version of (a)-(c) is in the lesson-07-03
[solutions](./exercises/03-case-study-geothermal-solutions.md).

## Related modules

- [11-04 Geothermal Exploration Geophysics](../04-geothermal-exploration-geophysics/README.md)
  — the methods used as evidence here.
- [11-01-03 Cost, Risk and Value of Information in Exploration](../01-exploration-workflow/03-cost-benefit.md).
- [11-07-01 Case Study: Porphyry Copper District](./01-case-study-porphyry.md) and
  [11-07-02 Case Study: Basin Analysis and Play Assessment](./02-case-study-basin.md).
- [06-12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md)
  — the monitoring and protocol side.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/02-monte-carlo-uq.md)
  — the Monte Carlo machinery used here.

## Self-assessment checklist

- [ ] I can compute a stored-heat estimate and report it as a distribution.
- [ ] I can state the convention for P90 and why it matters.
- [ ] I can convert a flow-rate distribution into a well count.
- [ ] I can compute an MT conductor posterior and name its ambiguity.
- [ ] I can compute expected event counts from a $b$-value.
- [ ] I can state the two uncertainties and how they couple.
