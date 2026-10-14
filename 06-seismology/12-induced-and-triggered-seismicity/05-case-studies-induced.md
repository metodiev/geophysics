---
id: 06-12-05
title: "Documented Case Studies: Basel, Oklahoma, Groningen, Pohang"
level: graduate
prereqs: ["06-12-01", "06-12-02", "06-12-03", "06-12-04"]
tags: [case-studies, attribution, discrimination, statistics, reservoir]
---

# Documented Case Studies: Basel, Oklahoma, Groningen, Pohang

## Learning objectives

By the end of this lesson you will be able to:

1. **Decompose** any induced-seismicity case study into its four components —
   operation, observation, claimed link, and alternatives — and say which
   component each piece of evidence addresses.
2. **Define** the four standard discriminating statistics and state what each can
   and cannot establish.
3. **Derive** the exceedance and coincidence probabilities that any attribution
   argument implicitly uses, and compute the false-positive rate of a stated
   decision rule.
4. **Demonstrate** that a natural swarm sited near an operation, at the same
   depth, and coincident in time is statistically indistinguishable from an
   induced sequence, and quote the measured false-positive rate.
5. **State** the epistemic status of each named case study, including which
   numbers you would have to retrieve from the primary literature before
   repeating them.
6. **Write** an attribution statement that separates measurement, model and
   interpretation.

## Prerequisites

- [06-12-01 Causes of Induced Seismicity](./01-induced-seismicity-causes.md)
- [06-12-02 Pore-Pressure Diffusion and Triggering Mechanisms](./02-pore-pressure-triggering.md)
- [06-12-03 Rate-and-State Friction and the Dieterich Seismicity Model](./03-rate-state-triggering.md)
- [06-12-04 Traffic-Light Protocols, Monitoring and Mitigation](./04-monitoring-and-mitigation.md)
- [06-11-07 Catalog Declustering](../11-earthquake-statistics-and-hazard/07-catalog-declustering.md)
  — the step that most changes the answers below.

## A statement of what this lesson does and does not assert

This lesson is about **how attribution arguments are structured and how they
fail**. It deliberately quotes **no** site-specific numbers — no magnitude, no
rate, no injection volume, no diffusivity, no depth for any named case. That is
not an oversight: every one of those numbers comes from a specific operator
report, a specific network configuration and a specific magnitude convention, and
quoting one from memory would be exactly the failure this curriculum forbids.

Consequently:

- The named cases below are described as **argument archetypes** — each with the
  same skeleton as the others and the same vulnerabilities.
- All quantitative content comes from
  `code/natural_vs_induced_demo.py`, whose inputs are **stated SYNTHETIC models**.
- To attach real numbers to a named case you must retrieve the primary literature
  and the operator's own reports. The links in §11 are the places to start.

Writing this lesson any other way would mean presenting remembered constants as
fact, which is worse than writing a shorter lesson.

## 1. Intuition: every case study is the same argument

Strip away the geography and every induced-seismicity case study says the same
four things:

1. **Operation.** Here is what was done, where, when, and how much (volume, rate,
   pressure, depth).
2. **Observation.** Here is the catalogue: locations, times, magnitudes, and the
   completeness magnitude $M_c$ through the sequence.
3. **Claimed link.** Here is why the second is attributed to the first.
4. **Alternatives.** Here is why the link is not something else.

Steps 3 and 4 are where cases differ and where they succeed or fail. Step 3 is
almost always a correlation of some kind — in space, in time, or both. Step 4 is
almost always the hardest, because the alternative is *natural seismicity*, and
natural seismicity is spatially clustered, temporally clustered and
magnitude-distributed in exactly the way induced seismicity is.

The measured result below is blunt: **the standard spatial and depth criteria
have a false-positive rate of 1.000 against a natural swarm that shares the
operation's location and depth.** Everything that remains of the argument then
rests on time, and the time test has a coincidence problem.

## 2. Precise definitions

### 2.1 The four standard statistics

| Statistic | Null hypothesis tested | What a positive result means |
|---|---|---|
| Spatial association | Seismicity is distributed like the regional background; distance to operation is a label-free quantity | Events are nearer the operation than background events are |
| Depth distribution | Depths are drawn from the regional depth distribution | Depth pattern is unlike the regional one |
| Temporal association | Event times are a homogeneous Poisson process, and the rate is unrelated to the operation | Rate correlates with the operation's time history |
| Magnitude distribution | The $b$-value equals the regional $b$-value | The population is unlike the regional population |

Each has a p-value, and each p-value answers only its own question. **None of
them tests a mechanism.** A p-value of $10^{-9}$ on a spatial test says that the
events are close together and close to the well. It does not say why.

### 2.2 Attribution versus association

- **Association**: the events are related in space or time to the operation.
  Statistical, testable, and frequently all that is available.
- **Attribution**: the operation caused the events, through a stated physical
  mechanism, with a quantified stress or pressure change on a specified fault.

Attribution requires the physics of
[06-12-01](./01-induced-seismicity-causes.md) and
[06-12-02](./02-pore-pressure-triggering.md) *plus* the statistics. A case study
that reports only statistics has established association.

### 2.3 The statistics of a test

- **True-positive rate (TPR)** or power: the fraction of genuinely induced
  sequences that the rule calls induced.
- **False-positive rate (FPR)**: the fraction of natural sequences that the rule
  calls induced.
- **AUC**: the probability that a randomly chosen induced sequence scores more
  "induced-like" than a randomly chosen natural one. AUC = 0.5 means the
  statistic carries **no** information.

### 2.4 Declustering

Aftershocks are not independent samples. Declustering removes them, and it
changes the count, the $b$-value, the rate and the $b$-value uncertainty
simultaneously. **Any two studies that decluster differently are not comparable**,
and the difference is large enough to reverse a conclusion.

## 3. Derivations

### 3.1 The coincidence probability that every time test assumes

For a time test based on the correlation between an event rate and an operational
history, the relevant question is not "does the correlation exist" but "how often
would it exist anyway". Model the operation as an active window of length $T_o$
inside a catalogue of length $T_c$, and natural swarms as occurring uniformly in
time. Then

$$P(\text{a randomly placed natural swarm overlaps the window})
= \frac{T_o}{T_c}\quad\text{(for } T_o \ll T_c\text{)}.$$

With $T_o = 487$ days and $T_c = 20$ years:

$$P = \frac{487}{7305} = 0.0667.$$

For $S$ independent operations windows in the same region, the probability that a
given swarm overlaps at least one is

$$P_S = 1 - \left(1 - \frac{T_o}{T_c}\right)^S .$$

The demonstration computes $P_S = 0.067, 0.292, 0.498, 0.874$ for $S = 1, 5, 10,
30$. **In a mature basin with tens of operations windows, a natural swarm
overlapping an operation is the expected case, not the surprising one.**

The corollary is the one that matters operationally: a time-correlation test
applied across a whole basin is testing coincidence, and coincidence is
guaranteed at basin scale.

### 3.2 The discriminability of two populations: the measured demonstration

Run

```text
<repo>/.venv/bin/python code/natural_vs_induced_demo.py
```

All inputs are MODEL: $M_c = 0.5$, both populations generated with $b = 1.0$, a
regional depth distribution $\mathcal N(7, 2.5)$ km, injection at 3 km, swarm
radius 1.5 km, location error 0.5 km, and 24 months of injection with roughly
487 days of actual activity.

**The paired example.** One induced sequence (400 events) and one natural swarm
(400 events) deliberately sited at the well, at the injection depth, and during
the operations window:

| Quantity | Induced (MODEL) | Natural (MODEL) |
|---|---|---|
| Median distance from well (km) | 1.93 | 1.86 |
| Median depth (km) | 2.95 | 3.00 |
| Depth KS p-value | $2.5\times10^{-167}$ | $2.7\times10^{-169}$ |
| Rate–injection Pearson $r$ | 0.948 | 0.195 |
| Rate–injection p-value | $2.1\times10^{-12}$ | 0.362 |
| $b$-value $\pm$ s.e. | $0.873 \pm 0.044$ | $0.899 \pm 0.045$ |

The spatial and depth diagnostics agree to within their scatter. **A study
relying on them would report this natural swarm as induced.** Only the time
correlation separates the two — and it separates them only because the induced
population was *constructed* to track the injection.

**Population results.** 600 sequences of each kind:

| Statistic | Induced vs ordinary natural (AUC) | Induced vs adversarial natural (AUC) |
|---|---|---|
| Median distance from well | 0.965 | 0.745 |
| Depth KS against regional | 1.000 | 0.496 |
| Time correlation with injection | 1.000 | 1.000 |
| $b$-value versus regional | 0.479 | 0.465 |

"Adversarial" means: swarm centre within 3 km of the well, swarm depth at the
injection depth, and a mainshock time inside the operations window.

Two of the four statistics collapse to AUC $\approx 0.5$, i.e. **no information**.
The $b$-value statistic was never informative in this model, because both
populations were built with the same $b$ — and that is a real point, not an
artefact: a $b$-value difference can only discriminate if a difference exists, and
reported $b$-value differences between induced and natural populations are small
and contested.

**The operating point of a realistic rule.** Rule A: *induced if median
distance $<$ 4 km and depth KS $p < 0.05$*.

| | Value |
|---|---|
| Induced sequences correctly called induced | 600/600 = **1.000** |
| Adversarial natural swarms wrongly called induced | 600/600 = **1.000** |
| Rule B = Rule A **and** time-correlation $p<0.05$: induced correct | 600/600 = 1.000 |
| Rule B: adversarial natural wrongly called | 50/600 = **0.083** |

Rule A has a **100 % false-positive rate** against a co-located, co-depth natural
population. Rule B's discriminating power sits entirely in its last clause, which
is a coincidence test, priced in §3.1.

### 3.3 Why "the stress change was positive" is not a resolution

From [06-12-01](./01-induced-seismicity-causes.md), the measured sign-flip rate of
the Coulomb stress change against receiver-plane uncertainty was 0.073 at $\pm15°$,
0.174 at $\pm45°$ and 0.514 at $\pm90°$, with half of all orientations positive at
every friction coefficient tested. So a modelling study that reports a positive
Coulomb stress change at a hypocentre has reported something that depends on an
assumed receiver plane, and the sensitivity of the sign to that assumption can be
measured. **The honest form of the claim is a pair**: the value, and the flip rate
over the stated uncertainty in the receiver geometry.

## 4. The four named cases as argument archetypes

Each row states the *structure* of the argument, not its numbers. For each, the
last column is the question that most often decides the case.

### 4.1 An urban deep-crystalline stimulation (Basel-type)

- **Operation**: high-pressure stimulation of a deep crystalline reservoir in a
  populated area, over a period of days, followed by shut-in and flowback.
- **Observation**: a catalogue with events during and shortly after the
  stimulation; a small number of events large enough to be felt.
- **Claimed link**: the events track the stimulation in time and are clustered
  near the well at the stimulation depth.
- **Structure of the argument**: a **time-domain** argument. The background rate
  in such settings is low, which is what makes the temporal coincidence
  informative; the whole case rests on a quantitative background rate.
- **The deciding question**: *what was the natural background rate before the
  stimulation, with a stated $M_c$, over a window long enough to estimate it?*
  Without that number, the coincidence cannot be priced.

### 4.2 Regional disposal into a sedimentary basin (Oklahoma-type)

- **Operation**: long-term disposal of large volumes of fluid into deep
  sedimentary formations, distributed across many wells over years.
- **Observation**: a regional rate increase, from a level that had been stable for
  decades, expressed as a change (usually in the rate of events above $M_c$) and a
  spatial association with the disposal wells.
- **Claimed link**: a basin-scale rate increase correlated in time with injection
  volumes, and spatially concentrated near the wells, with hypocentres at or below
  the injection interval.
- **Structure of the argument**: a **regional, decadal** argument. It is the
  strongest kind of case, because a stable background rate over decades plus a
  step change coincident with operations is hard to explain naturally — provided
  the rate estimate and its $M_c$ history are handled properly.
- **The deciding questions**: *is the regional rate increase unique to the
  injection region, and does it survive declustering and a correction for the
  changing $M_c$?* An $M_c$ that falls over the same period (because the
  population and the network grew) produces a spurious increase in the low-magnitude
  rate.

### 4.3 Depleting a large gas field (Groningen-type)

- **Operation**: decades of gas extraction from a large, flat, porous reservoir.
- **Observation**: seismicity concentrated at the field margin rather than within
  the field, with magnitudes that increase as depletion proceeds, plus measurable
  surface subsidence.
- **Claimed link**: reservoir compaction as the pore pressure falls, producing
  shear stress concentration at the reservoir margin.
- **Structure of the argument**: a **physics-led** argument. The mechanism
  (lesson 1, §3.4) predicts where the events go — the margin — and the subsidence
  is an independent measurement of the volume change driving it.
- **The deciding question**: *does the seismicity outline the field margin in the
  way the compaction model requires, and is the subsidence quantitatively
  consistent with the modelled volume change?* This is a case where the physics
  makes a falsifiable spatial prediction, which is what separates it from a
  correlation-only claim.

### 4.4 Enhanced geothermal stimulation in a tectonic setting (Pohang-type)

- **Operation**: stimulation of an engineered geothermal reservoir, in a region
  with a non-negligible natural earthquake rate.
- **Observation**: a moderate-size event in the days-to-months after stimulation,
  close to the well.
- **Claimed link**: the perturbed stress state brought the fault closer to
  failure, with a delay set by diffusion (lesson 2) or by rate-and-state
  relaxation (lesson 3).
- **Structure of the argument**: a **delay** argument, which is inherently weaker
  than a rate-change argument, because a delay is a single number fitted to a
  single event, and the time since the last natural earthquake is not known.
- **The deciding questions**: *what is the natural rate at that magnitude near
  that location, so that the probability of a natural event there in that window
  can be computed? And is the stress change positive on the causative fault under
  a defensible receiver-plane assumption?* The second question is exactly §3.3.

### 4.5 What the four have in common

| Feature | Implication |
|---|---|
| A stable pre-operation background rate is the most valuable single datum | It is what prices coincidence |
| $M_c$ history is a first-order control | It can manufacture or hide a rate change |
| The spatial and depth tests are weak against co-located natural seismicity | Measured FPR of 1.000 |
| Falsifiable spatial prediction (as in the compaction case) is stronger than correlation | Physics constrains where the events go |
| A single delayed event is weak evidence; a rate change with a decaying tail is stronger | Lesson 3 gives the tail a specific functional form |

## 5. Assumptions and their consequences

| Assumption | Consequence if violated |
|---|---|
| Background rate stationary before operations | A naturally varying background makes the "step change" assertion weaker |
| $M_c$ known and constant | Rate changes are misattributed |
| Poisson occurrence for the coincidence arithmetic | Clustering inflates variability and changes the effective number of independent swarms |
| Location errors random | They average out; a velocity-model bias does not (lesson 2, §7.3) |
| Catalogues comparable across studies | Different declustering, magnitude conventions and networks make them not comparable |
| The mechanism is stated | Without it, the argument is association dressed as attribution |
| Damage thresholds are physical | They are political and asset-dependent (lesson 4) |

## 6. Units and dimensional analysis

Case studies mix quantities with different dimensions, and the mixing is a common
source of error. Keep the following strictly separate:

| Quantity | Dimension | Typical presentation |
|---|---|---|
| Magnitude $M$ | 1 (dimensionless, conventional) | Rounded to 0.1 |
| Moment $M_0$ | N·m | Powers of ten |
| Rate | events/time | "per year" — state it |
| Volume | m³ | "barrels" or "mm³" — convert explicitly |
| Pressure, stress | Pa | "psi", "bar", "MPa" — three different factors of ten |
| Subsidence | m | mm |
| Diffusivity | m²/s | — |
| $b$-value | 1 | per magnitude unit |

Two invariants worth checking in any case study:

- $M_0$ and $M_w$ are related by $\log_{10}M_0 = 1.5M_w + 9.1$ (SI, N·m);
  a factor-of-ten error in $M_0$ is 0.67 magnitude units.
- A rate ratio is dimensionless: $10^{-b\Delta M}$ needs $\Delta M$ in the same
  magnitude convention as the $b$-value it is paired with.

## 7. Worked examples

### 7.1 Pricing a coincidence

**Problem.** A swarm of 200 events occurs 2 km from a well that injected for 14
months inside a 25-year catalogue. Compute the coincidence probability.

**Step 1 — horizon.** $14\ \text{months} = 427$ days. $25\ \text{yr} = 9131$ days.

**Step 2 — probability.**
$$P = \frac{427}{9131} = 0.0468.$$

**Step 3 — interpretation.** About 4.7 % of randomly placed swarms would land in
the window. So a single spatial-plus-temporal coincidence of this kind is a
roughly 1-in-21 event. **That is not negligible**, and it is why a single case
needs corroboration — for example, a rate change confined to the operations
period and absent before it.

**Step 4 — multiple windows.** With 8 operations windows in the region,
$1-(1-0.0468)^8 = 0.321$. Nearly a third of randomly placed swarms coincide with
*some* operation.

### 7.2 The measured false-positive rate of the standard rule

From §3.2, the realistic spatial+depth rule has a false-positive rate of
**1.000** against a co-located, co-depth natural population, and **1.000** is not
a rounding artefact: 600 of 600 adversarial swarms were called induced.

**Problem.** If the false-positive rate is 1.0, what is the posterior probability
that a sequence called induced really is induced?

**Bayes.** Let $\pi$ be the prior probability that a given sequence is induced.
Then
$$P(\text{induced}\mid\text{called}) =
\frac{\pi\times1.0}{\pi\times1.0 + (1-\pi)\times1.0} = \pi.$$

The rule carries **no** information: the posterior equals the prior. That is the
cleanest way to state why spatial and depth criteria alone cannot support an
attribution.

### 7.3 Where the evidence does live

From the same run, Rule B (adding the time-correlation clause) has TPR 1.000 and
FPR 0.083. Applying Bayes with the same prior:

$$P(\text{induced}\mid\text{called}) = \frac{\pi\times1.0}{\pi\times1.0 +
(1-\pi)\times0.083}.$$

For $\pi = 0.5$: $0.5/(0.5+0.0415) = \mathbf{0.923}$. For $\pi = 0.1$:
$0.1/(0.1 + 0.0747) = \mathbf{0.572}$.

So the same evidence supports a 92 % or a 57 % attribution depending entirely on
how often sequences in that region are induced anyway — the **base rate**. A case
study that reports a false-positive rate but not a base rate has reported half the
argument.

## 8. Python demonstration

`code/natural_vs_induced_demo.py`:

1. builds injection history, induced and natural populations from stated models;
2. computes the four statistics with proper tests (two-sample KS, Pearson with a
   p-value, $b$-value with the Shi–Bolt standard error);
3. measures AUC and TPR at a 5 % FPR for each statistic, against both an ordinary
   and an adversarial natural population;
4. measures the operating point of a realistic two-clause rule and of a
   three-clause rule;
5. computes the coincidence arithmetic.

Exercises against the output: set `B_INDUCED = 0.85` and check whether the
$b$-value statistic becomes informative; set the adversarial swarm offset
`rc = rng.uniform(0, 8e3)` and watch the spatial AUC recover.

## 9. Exercises

### ★ Foundational

**★1.** List the four components of a case study and, for each of the four
archetypes in §4, say which component is weakest.

**★2.** Compute $P_S$ for $T_o = 200$ days, $T_c = 30$ years and $S = 4$.

**★3.** State the dimensions of magnitude, rate, pressure and diffusivity.

### ★★ Applied

**★★4.** A study reports "the rate increased by a factor of 10 coincident with
injection". List the five questions from §5 you would ask, and say what answer to
each would most weaken the claim.

**★★5.** Using §3.2's measured AUCs, state which statistic you would trust for a
case in which the natural seismicity is regional and deep (7 km) and the injection
is at 3 km, and why the answer changes if the natural seismicity is shallow.

**★★6.** With the Rule B numbers (§7.3), compute the posterior probability of
attribution for base rates $\pi = 0.01, 0.1, 0.5, 0.9$ and plot the result by
hand. State the base rate at which the evidence is uninformative.

**★★7.** A case study reports a positive Coulomb stress change at a hypocentre
without stating the receiver plane. Using lesson 1's measured flip rates, state
the range of models in which the sign reverses and what you would request.

### ★★★ Research

**★★★8.** Design the observation that would most reduce the ambiguity in the
Basel-type case. It must be feasible with a realistic budget, and you must state
what it would change quantitatively (which statistic, what AUC).

**★★★9.** For the Oklahoma-type case, write the declustering sensitivity analysis
you would require before accepting the headline rate change. Include at least two
declustering algorithms and a statement of how the conclusion could reverse.

**★★★10.** Construct a scenario in which an operation genuinely induces
seismicity and the standard tests all fail to detect it. Then construct a scenario
in which no seismicity is induced and all the tests fire. State, for each, which
single additional measurement would resolve it, and whether that measurement
exists.

## 10. Common mistakes

1. **Reporting a correlation as a mechanism.** Measured: the spatial+depth rule
   has FPR 1.000 against a co-located natural population.
2. **Quoting a case study's numbers from memory.** Retrieve them from the primary
   literature and the operator's reports.
3. **Ignoring the base rate.** A posterior probability needs both the test's FPR
   and the prior frequency of induced sequences.
4. **Ignoring the $M_c$ history.** A falling $M_c$ manufactures a rate increase.
5. **Comparing studies that decluster differently.** The counts, $b$-values and
   rates all change together.
6. **Treating a single delayed event as strong evidence.** It is one number; the
   natural base rate at that magnitude and location is the comparison.
7. **Presenting a positive Coulomb stress change as decisive.** Measured sign-flip
   rate 0.514 for an unconstrained receiver plane.
8. **Assuming a protocol's thresholds are physical.** They are policy (lesson 4).
9. **Assuming the largest event is bounded.** The 5–95 spread of $M_{\max}$ is
   constant at about 1.77 magnitude units regardless of catalogue size.
10. **Confusing association with attribution in the abstract of a report.** The
    distinction must survive into the summary.

## 11. Real-world applications

- **Regulatory review.** The four-component decomposition is the standard shape of
  a review document.
- **Litigation and insurance.** The association/attribution distinction is the
  difference between a compensable claim and a coincidence.
- **Operator decision-making.** The base-rate problem is why operators invest in
  pre-operation baseline monitoring: it is the only way to establish $\pi$ and the
  background rate.
- **Public communication.** Reporting exceedance probabilities and honest
  uncertainty is the defensible form of a public statement.
- **Data sources for a real study.** The
  [USGS FDSN event service](https://earthquake.usgs.gov/fdsnws/event/1/query) and
  [ComCat](https://earthquake.usgs.gov/data/comcat/) for the catalogue, the
  [International Seismological Centre](https://www.isc.ac.uk) for historical
  completeness, [EarthScope](https://www.earthscope.org) for waveform and station
  metadata, and the [FDSN web services specification](https://www.fdsn.org/webservices/)
  for the access protocol.

## 12. Further reading

- **McGarr, A., et al. *Coping with earthquakes induced by fluid injection*,
  Science (2015).** A short synthesis of the policy and physical issues, including
  the maximum-magnitude question.
- **Ellsworth, W. L. *Injection-induced earthquakes*, Science (2013).** The
  framing review for the disposal-injection archetype.
- **Segall, P., & Lu, S. *Injection-induced seismicity: poroelastic and
  earthquake nucleation effects*, J. Geophys. Res. (2015).** The poroelastic
  mechanism in the form used in §3.3.
- **van Thienen-Visser, K., & Breunese, J. N. *Induced seismicity of the
  Groningen gas field: history and recent developments*, The Leading Edge (2015).**
  The compaction archetype, from the operator's side.
- **Grigoli, F., et al. *The November 2017 Mw 5.5 Pohang earthquake: a possible
  case of induced seismicity in South Korea*, Science (2018).** The geothermal
  archetype, including the mechanism argument.
- **Utsu, T., Ogata, Y., & Matsu'ura, R. S. *The centenary of the Omori formula
  for a decay law of aftershock activity*, J. Phys. Earth (1995).** The rate-decay
  formalism behind the time test.
- **USGS Earthquake Hazards Program at <https://earthquake.usgs.gov>** and the
  **[International Seismological Centre](https://www.isc.ac.uk).** Primary
  catalogue sources; the numbers in §3 of this lesson must be replaced with theirs
  before any real case is discussed.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself. The
> named cases above are described only as argument structures; no site-specific
> value is asserted here, and the primary sources must be consulted.

## 13. Related lessons

- [06-12-01 Causes of Induced Seismicity](./01-induced-seismicity-causes.md) —
  the mechanisms the archetypes invoke.
- [06-12-02 Pore-Pressure Diffusion and Triggering Mechanisms](./02-pore-pressure-triggering.md)
  — the front argument, and its degeneracy.
- [06-12-03 Rate-and-State Friction and the Dieterich Seismicity Model](./03-rate-state-triggering.md)
  — the shape a genuine rate response has.
- [06-12-04 Traffic-Light Protocols, Monitoring and Mitigation](./04-monitoring-and-mitigation.md)
  — what operators did in these cases.
- [06-11-07 Catalog Declustering](../11-earthquake-statistics-and-hazard/07-catalog-declustering.md)
  — the step that most changes a rate conclusion.

Exercises:
[`exercises/05-case-studies-induced-exercises.md`](./exercises/05-case-studies-induced-exercises.md)
and
[`exercises/05-case-studies-induced-solutions.md`](./exercises/05-case-studies-induced-solutions.md).

## Self-assessment checklist

- [ ] I can decompose any case study into four components. (§1)
- [ ] I can state what each of the four standard statistics does and does not
      establish. (§2.1)
- [ ] I can compute a coincidence probability and $P_S$. (§3.1, §7.1)
- [ ] I can quote the measured false-positive rate of the spatial+depth rule and
      explain why the posterior equals the prior when it is 1.0. (§3.2, §7.2)
- [ ] I can compute a posterior attribution probability from a base rate. (§7.3)
- [ ] I can describe the four archetypes and name each one's deciding question.
      (§4)
- [ ] I can say which numbers I must retrieve before discussing a named case.
      (§"A statement of what this lesson does and does not assert")
- [ ] I can state why the $b$-value statistic was uninformative in the
      demonstration and when it would not be. (§3.2)
- [ ] I can list the assumptions of an attribution argument. (§5)
