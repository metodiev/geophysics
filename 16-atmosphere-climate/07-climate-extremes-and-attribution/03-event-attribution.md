---
id: 16-07-03
title: "Event Attribution Methodology and Its Limits"
level: research
prereqs: ["16-07-02", "16-07-01", "16-04-04"]
tags: [atmosphere, climate, event-attribution, counterfactual, attributable-risk, storyline]
---

# Event Attribution Methodology and Its Limits

> **All models and data in this module are SYNTHETIC.** The factual and
> counterfactual ensembles in `code/event_attribution_demo.py` are draws from
> chosen normal distributions of a made-up daily maximum temperature. No real
> event, station, model ensemble or published attribution result is used, and no
> published fraction of attributable risk is quoted.

Event attribution answers a specific and narrow question: **how did the
probability or the intensity of this class of event change because of a
particular external driver?** The wording matters. "This event" is never a single
realisation — you cannot run the same hurricane twice — so the question is always
asked about a *class* of events defined by a metric and a threshold. And "because
of" requires a **counterfactual**: a parallel world with the driver removed,
which does not exist and must be simulated. The result is therefore a
probabilistic statement about two modelled worlds, reported with its uncertainty,
not a measurement of a cause.

This lesson builds the standard risk-based formulation, then spends most of its
length on the limits, because they are what separate a defensible attribution
statement from an overclaim. Two limits dominate. First, rare events make the
counterfactual tail empirically empty: in the demonstration a 50-member ensemble
finds *zero* counterfactual exceedances, so neither the probability ratio nor the
fraction of attributable risk is estimable from it. Second, thermodynamic and
dynamical contributions do not add: the fraction of attributable risk is a
nonlinear function of tail probabilities, and single-contribution values can
sum to more than one. Both are measured below.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** an event-attribution question as a comparison between factual
   and counterfactual ensembles, and **state** the counterfactual being used.
2. **Define** the probability ratio and the fraction of attributable risk, and
   **derive** the relationship between them.
3. **Estimate** these quantities from a finite ensemble, **compute** interval
   estimates for the underlying probabilities, and **explain** what happens when
   the counterfactual tail is empty.
4. **Quantify** how the answer depends on the event definition, and **demonstrate**
   that the definition is part of the result.
5. **Show** that thermodynamic and dynamical contributions to FAR are not
   additive, and **compute** a case in which they cancel.
6. **Contrast** the probability-based and intensity-based ("storyline")
   framings, and **state** which question each answers.
7. **Distinguish** a statistical attribution statement from a causal one, and
   **write** an attribution claim in a form a reviewer could falsify.

## Prerequisites

- [16-07-02 Detection and Attribution of Climate Change](02-detection-attribution.md) —
  the large-scale attribution framework this specialises.
- [16-07-01 Extreme Events: Statistics and Physical Drivers](01-climate-extremes.md) —
  return periods, tails and the Clausius–Clapeyron scaling.
- [16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](../04-climate-system-and-feedbacks/04-natural-variability.md) —
  the variability that a single event does not sample.

## 1. The counterfactual question

Let $E$ be an event class, defined by a metric and a threshold — for example
"the daily maximum temperature at a stated set of locations reaching at least
$42.0\ ^\circ\mathrm{C}$". Define two worlds:

- the **factual** world, forced as the real world was (all drivers, including the
  driver of interest);
- the **counterfactual** world, identical except that the driver of interest is
  removed.

Then the risk-based attribution statement is about the difference between
$p_1 = \Pr(E \mid \text{factual})$ and $p_0 = \Pr(E \mid \text{counterfactual})$.
Everything in this lesson follows from how those two probabilities are measured
and how their difference is reported.

Two consequences of the construction are worth stating at the outset. The
counterfactual is a **model output**: no one has observed the world without
anthropogenic greenhouse gases, so $p_0$ is modelled, while $p_1$ is modelled
*and* constrained by observations. And the event class $E$ is a **choice**: change
the threshold and the answer changes, as Section 4 measures.

## 2. Two standard summary statistics

The **probability ratio** (also called the risk ratio) is

$$\mathrm{PR} = \frac{p_1}{p_0},$$

and the **fraction of attributable risk** is

$$\boxed{\;\mathrm{FAR} = 1 - \frac{p_0}{p_1} = 1 - \frac{1}{\mathrm{PR}}.\;}$$

FAR is the fraction of the factual event probability that does not occur in the
counterfactual. It lies in $[0,1]$ when $p_1 > p_0$; if the driver made the event
*less* likely, $p_1 < p_0$ and FAR is negative, which is a physically meaningful
result rather than an error to clip away. Its complement $\mathrm{FAR}' = p_0/p_1$
is sometimes called the fraction of attributable risk *reversed*; the two differ
by sign convention and must be stated.

**FAR is not the probability that the event was caused by the driver.** It is a
ratio of modelled event probabilities. The distinction between "this event's
probability was increased" and "this event was caused" is the distinction between
a statistical statement and a causal one, and event attribution supports only the
former.

## 3. Worked example — exact probabilities for a stated model

The demonstration defines a synthetic daily maximum temperature
$T \sim \mathcal{N}(38.0, 2.5^{2})$ (degrees Celsius) in the factual world, and
the same distribution shifted by $-1.5\ ^\circ\mathrm{C}$ in the counterfactual,
with the event threshold at $42.0\ ^\circ\mathrm{C}$. The exact tail
probabilities are

$$p_1 = \Pr\!\left(Z \ge \frac{42.0-38.0}{2.5}\right) = \Pr(Z \ge 1.60) = 0.0548,$$
$$p_0 = \Pr\!\left(Z \ge \frac{42.0-36.5}{2.5}\right) = \Pr(Z \ge 2.20) = 0.0139,$$

giving

$$\mathrm{PR} = \frac{0.0548}{0.0139} = 3.94, \qquad
\mathrm{FAR} = 1 - \frac{0.0139}{0.0548} = 0.746.$$

Read carefully: *in this model*, the event occurs about once every 18 years in
the factual world and once every 72 years in the counterfactual, and $74.6\%$ of
the factual event probability is absent in the counterfactual. These are exact
properties of the chosen distributions — the uncertainty that remains is the
uncertainty of the model and of the ensemble used to estimate it, which is the
subject of the rest of the lesson.

## 4. What a finite ensemble delivers, and when it delivers nothing

Ensembles are finite. The demonstration draws $50$ members from each world and
counts exceedances of the threshold:

| World | exceedances | $\hat p$ | 95% Wilson interval |
|---|---|---|---|
| factual | $2/50$ | $0.040$ | $[0.011, 0.135]$ |
| counterfactual | $0/50$ | $0.000$ | $[0.000, 0.071]$ |

The counterfactual tail is **empty**. $\mathrm{PR}$ is then infinite and
$\mathrm{FAR}$ is not estimable: the Wilson upper limit for $p_0$ is $0.071$,
which exceeds the factual $\hat p_1 = 0.040$, so the data do not even support a
positive lower bound on FAR. This is not a defect of the demonstration; it is the
central practical limit of event attribution. Rare events require ensembles large
enough to populate the counterfactual tail.

Sweeping the ensemble size $n$ (with $400$ replicate experiments at each $n$)
makes the scaling visible:

| $n$ per world | mean FAR | FAR 5th–95th width | P(zero counterfactual exceedances) |
|---|---|---|---|
| 10 | 0.167 | 0.567 | 0.968 |
| 25 | 0.095 | 1.667 | 0.787 |
| 50 | 0.385 | 1.800 | 0.520 |
| 100 | 0.601 | 0.875 | 0.282 |
| 250 | 0.714 | 0.493 | 0.033 |
| 1000 | 0.740 | 0.253 | 0.000 |

Three readings. At $n = 10$ the counterfactual tail is empty in $96.8\%$ of
experiments, so almost every estimate is undefined. The *conditional* mean FAR
(when it exists at all) is badly biased at small $n$ — the surviving estimates
come from the rare experiments in which the counterfactual happened to produce an
exceedance — and only approaches the exact value $0.746$ by $n = 1000$. The width
of the 5–95% interval exceeds $1$ at intermediate $n$, meaning that estimates
often sit at the $[0,1]$ boundary. **A reported FAR without a statement of
ensemble size, and of how many members exceeded the threshold in each world, is
not reproducible.**

## 5. The event definition is part of the answer

Sweeping the threshold on the same two distributions:

| threshold (°C) | $p_1$ | $p_0$ | PR | FAR |
|---|---|---|---|---|
| 39.0 | 0.3446 | 0.1587 | 2.17 | 0.540 |
| 40.0 | 0.2119 | 0.0808 | 2.62 | 0.619 |
| 41.0 | 0.1151 | 0.0359 | 3.20 | 0.688 |
| 42.0 | 0.0548 | 0.0139 | 3.94 | 0.746 |
| 43.0 | 0.0228 | 0.0047 | 4.88 | 0.795 |
| 44.0 | 0.0082 | 0.0013 | 6.07 | 0.835 |

FAR rises from $0.540$ to $0.835$ as the event is made more extreme, because a
fixed shift moves the probability far more in the tail. Two studies of the same
heatwave that define the event at $40\ ^\circ\mathrm{C}$ and at $43\
^\circ\mathrm{C}$ will report $0.619$ and $0.795$ and both be correct. The
*honest* practice is to report the event definition and, where possible, the
sensitivity to it — a curve rather than a number.

## 6. Thermodynamic and dynamic contributions do not add

Write the metric as a sum of contributions,
$T = \text{base} + \delta_{\text{thermo}} + \delta_{\text{dynamic}}$, with
$\delta_{\text{thermo}} = +1.5\ ^\circ\mathrm{C}$ and
$\delta_{\text{dynamic}} = +1.0\ ^\circ\mathrm{C}$ in the factual world (so
$\text{base} = 35.5\ ^\circ\mathrm{C}$). The demonstration computes FAR for the
counterfactual in which different contributions are removed:

| removed contribution | $p_0$ | PR | FAR |
|---|---|---|---|
| thermodynamic only (keep dynamics) | 0.0139 | 3.94 | 0.746 |
| dynamic only (keep thermodynamics) | 0.0228 | 2.41 | 0.585 |
| both (full counterfactual) | 0.0047 | 11.76 | 0.915 |

The single-contribution values are $0.746$ and $0.585$; the combined value is
$0.915$, **not the sum $1.331$**. FAR is a nonlinear function of tail
probabilities, so contributions do not decompose additively. A multiplicative
composition, $\mathrm{FAR}_{\text{tot}} = 1-(1-\mathrm{FAR}_a)(1-\mathrm{FAR}_b)$,
would give $0.965$ here — also not the measured $0.915$. The reason is that the
two contributions add in the *mean* but the tail probability is a nonlinear
function of the mean, so *no* fixed combination rule applies: the right
composition depends on how the physical contributions combine. Any analysis that
adds a thermodynamic FAR to a dynamic FAR is making an arithmetic error, however
careful its physics.

The contributions can also oppose. A circulation change of $-1.0\
^\circ\mathrm{C}$ acting against a $+1.5\ ^\circ\mathrm{C}$ thermodynamic shift
gives $\mathrm{FAR} = 0.344$ ($\mathrm{PR} = 1.53$) — the event is still made
more likely overall, but far less so than the thermodynamic term alone would
suggest. The net sign is a *result*, not an assumption, and it depends on which
circulation patterns the model produces.

## 7. The intensity ("storyline") alternative

A different, and sometimes more robust, question asks how much the *intensity* of
the event changed, conditional on an event of that type having occurred. For the
demonstration's distributions the 1-in-100 daily maximum is

$$T_{100}^{\text{factual}} = 38.0 + 2.5\,z_{0.01} = 43.82\ ^\circ\mathrm{C},$$
$$T_{100}^{\text{counterfactual}} = 36.5 + 2.5\,z_{0.01} = 42.32\ ^\circ\mathrm{C},$$

a difference of exactly $1.50\ ^\circ\mathrm{C}$ — the thermodynamic shift, since
the distributions have the same shape. The **storyline** framing reports this
conditional intensity change. It is less sensitive to the shape of the tail and
to model errors in the variability, because it does not divide two small
probabilities; but it answers a different question. "This event is $1.5\
^\circ\mathrm{C}$ hotter than it would have been" is not "this event is $4$ times
more likely". A study should say which question it is answering, and the two do
not have to agree.

## 8. What event attribution can and cannot claim

**It can claim**, conditional on a stated model and counterfactual, that the
probability of a well-defined event class changed by a stated amount with a
stated uncertainty; that the direction of the change is robust across models and
definitions; and that the change is inconsistent with internal variability alone.

**It cannot claim** that a particular weather event would not have happened
without the driver (the counterfactual tail is often empty); that a single event
was "caused" by the driver in a deterministic sense; that the reported FAR
transfers to other events of superficially similar type; or that a model-based
counterfactual is a measurement.

## 9. Assumptions and regime of validity

1. **Plausibility of the counterfactual.** The model that removes the driver must
   be physically credible; a biased model gives a biased $p_0$.
2. **Stationarity of the applied shift.** Most studies apply a fixed
   thermodynamic shift; if the response is nonlinear or state-dependent the
   shift itself must be modelled.
3. **The event class is well sampled.** With finite ensembles the counterfactual
   tail may be empty (Section 4), in which case no probability-based statement is
   available.
4. **Model independence is not required, but model agreement is not proof.**
   Agreement across models with shared biases is not independent confirmation.
5. **The metric spans the physical driver.** A metric that mixes thermodynamics
   and dynamics (as most do) cannot be cleanly decomposed, and the decomposition
   in Section 6 is illustrative, not generally available.
6. **Observational constraint on $p_1$.** Where the factual probability is
   estimated from a short record rather than a large ensemble, its own sampling
   uncertainty dominates.

## 10. A reporting template

A defensible event-attribution statement names:

1. the **event class** (metric, threshold, region, season, duration) and why;
2. the **factual** and **counterfactual** worlds, and how the counterfactual was
   constructed;
3. the **ensemble** (size, models) and, in each world, the **number of members
   exceeding** the threshold;
4. the **estimator** (PR, FAR, intensity change), its **interval**, and the
   **sensitivity** to the threshold;
5. the **direction of robustness** across models and definitions;
6. the **causal caveat**: a statistical statement about modelled probabilities,
   conditional on the counterfactual.

## 11. Python demonstration

[`code/event_attribution_demo.py`](code/event_attribution_demo.py) performs the
whole calculation and prints labelled results with units. It:

1. defines two synthetic ensembles and computes exact tail probabilities, PR and
   FAR;
2. draws a finite ensemble, reports Wilson intervals, and shows a case where the
   counterfactual tail is empty and FAR is not estimable;
3. measures how the FAR uncertainty depends on ensemble size;
4. sweeps the event threshold;
5. computes thermodynamic, dynamic and combined FARs and shows they do not add;
6. computes the intensity (storyline) change.

Every number in this lesson is printed by that demonstration.

## Mastery checkpoint

> The demonstration's synthetic example has $p_1 = 0.0548$ and $p_0 = 0.0139$.
>
> **(a)** Compute PR and FAR by hand and verify them against $3.94$ and $0.746$.
> **(b)** A 50-member ensemble finds $2$ factual and $0$ counterfactual
> exceedances. State precisely what can and cannot be concluded, using the Wilson
> intervals.
> **(c)** The same shift at threshold $40\ ^\circ\mathrm{C}$ gives
> $\mathrm{FAR}=0.619$ and at $43\ ^\circ\mathrm{C}$ gives $0.795$. Explain to a
> journalist, in two sentences, why two scientists quote different numbers for
> the same heatwave and both are right.
> **(d)** Thermodynamic FAR $=0.746$ and dynamic FAR $=0.585$ give a combined
> FAR of $0.915$. Show that adding them is arithmetically wrong and explain why
> in terms of the tail probabilities.
> **(e)** State the counterfactual and the causal caveat you would attach to the
> sentence "warming made this heatwave more likely".

## Common pitfalls

1. **Saying "caused by climate change".** The defensible claim is a change in the
   probability or intensity of an event *class*, conditional on a stated
   counterfactual.
2. **Not naming the counterfactual.** A probability ratio is meaningless without
   the world it is compared against.
3. **Reporting FAR from a small ensemble with an empty counterfactual tail.**
   The quantity is then not estimable, and a finite number is an artefact.
4. **Adding thermodynamic and dynamic FARs.** FAR is nonlinear in the tail
   probabilities; the parts sum above one in the demonstration.
5. **Treating the threshold as a preamble.** The event definition changes the
   answer by more than the sampling error for moderate shifts.
6. **Quoting a storyline intensity change as a probability change.** They answer
   different questions.
7. **Reading robust model agreement as independent confirmation.** Shared model
   structure produces shared errors.

## Related modules

- [16-07-01 Extreme Events: Statistics and Physical Drivers](01-climate-extremes.md) —
  the return-period and Clausius–Clapeyron background.
- [16-07-02 Detection and Attribution of Climate Change](02-detection-attribution.md) —
  the large-scale, multi-decade counterpart of this event-scale analysis.
- [16-07-04 Impacts, Vulnerability and Risk Assessment](04-impacts-and-risk.md) —
  how an attributable change becomes a risk, and where exposure enters.
- [16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](../04-climate-system-and-feedbacks/04-natural-variability.md) —
  the variability that makes a single event uninformative.
- [16-05-05 CMIP, Model Intercomparison and Ensemble Design](../05-climate-models/05-coupled-model-intercomparison.md) —
  where the ensembles, and their shared biases, come from.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md) —
  a parallel treatment of rare-event probability and its reporting.

## Self-assessment checklist

- [ ] I can state an event-attribution question with its counterfactual.
- [ ] I can compute PR and FAR and state the relationship between them.
- [ ] I can explain why an empty counterfactual tail destroys the estimate.
- [ ] I can explain why thermodynamic and dynamic FARs do not add.
- [ ] I can contrast the probability-based and storyline framings.
- [ ] I can write an attribution claim a reviewer could falsify.
