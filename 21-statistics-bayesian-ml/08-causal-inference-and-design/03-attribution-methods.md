---
id: 21-08-03
title: "Attribution in Climate and Hazard Science"
level: research
prereqs: ["21-08-02", "21-01-07", "16-07-03"]
estimated_minutes: 60
tags: [attribution, climate, hazard, counterfactual, probability-ratio, teaching]
---

# Attribution in Climate and Hazard Science

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the factual and counterfactual worlds, and **state** that every
   attribution statement is a comparison between them rather than a measurement of
   one world.
2. **Compute** the probability ratio, the attributable fraction and the change in
   return period from two sets of event frequencies, and **show** that the three
   are algebraic restatements of one number.
3. **Distinguish** a marginal probability ratio from a conditional risk ratio, and
   **state** which scientific claim each supports.
4. **Estimate** the probability ratio from counts and from a logistic regression,
   and **interpret** the fitted world coefficient correctly for a purely
   distributional shift.
5. **Measure** how the uncertainty of an attribution statement grows as the event
   becomes rarer, and **explain** why it is set by the smaller of the two worlds.
6. **State** what an attribution result cannot establish: causation without a model,
   the effect of a change in the response, and the frequency of events outside the
   fitted range.
7. **Report** an attribution study: the event definition, the covariate and its
   scale, the model producing the counterfactual, the method and its intervals, and
   the sensitivity to each of those choices.

Every season, probability and interval below is **SYNTHETIC**, produced by
[`code/attribution_methods_demo.py`](./code/attribution_methods_demo.py). No
observed climate series, event catalogue or published attribution result is used.

## Prerequisites

- [21-08-02 Causal Inference Methods and Counterfactuals](./02-causal-inference-methods.md) —
  the counterfactual logic that attribution applies at the level of an event class.
- [21-01-07 Extreme Value Theory for Geohazards](../../21-statistics-bayesian-ml/01-statistics-in-practice/07-extreme-value-theory.md) —
  the tail probabilities and return periods used here.
- [16-07-03 Event Attribution Methodology and Its Limits](../../16-atmosphere-climate/07-climate-extremes-and-attribution/03-event-attribution.md) —
  the climate-science framing and its standard methods.
- [21-08-01 Experimental and Survey Design for Earth Studies](./01-experimental-design.md) —
  the design reasoning that determines what can be estimated.

## 1. Intuition: two worlds, one event definition

Attribution asks a counterfactual question: *how often would this event have
occurred without the change we are attributing?* It requires three ingredients, and
the result is only as good as the weakest of them:

1. an **event definition** — a threshold on a variable over a region and a season,
   fixed before the analysis;
2. a **covariate** that carries the change (a regional temperature index, a sea
   surface temperature, an emission-related forcing);
3. a **model for the counterfactual world** — usually a large ensemble of
   climate-model simulations with and without the forcing, or a statistical
   reweighting of the observed covariate distribution.

The output is a ratio of probabilities. The demonstration computes it on synthetic
worlds where the truth is known, so that the statements below can be checked rather
than believed. Its headline: the event is $2.116$ times more frequent in the factual
world, the attributable fraction is $0.527$, the return period falls from $5.3$ to
$2.5$ seasons — and at a fixed covariate value the event's probability is
*unchanged* ($\exp(c) = 0.865$, interval containing $1$), because this generator's
world differs only in the distribution of the covariate.

## 2. The synthetic worlds

| Element | Definition |
|---|---|
| seasons per world | $2000$ |
| counterfactual covariate | $X \sim \mathcal N(0,1)$ |
| factual covariate | $X \sim \mathcal N(1,1)$ |
| event probability | $\Pr(\text{event}\mid X) = \mathrm{sigmoid}(-2.0 + 1.5X)$ |
| exact marginal probabilities | $0.19005$ (counterfactual), $0.41240$ (factual) |
| measured frequencies | $378/2000 = 18.90\%$, $800/2000 = 40.00\%$ |

The event probability is a *probabilistic* function of the covariate, not a
threshold on it: a threshold would make the event a deterministic function of $X$
and the logistic route of §4 would suffer perfect separation. Real attribution
studies have the same structure — the event is defined on a local variable (rainfall,
storm surge, fire weather) and the covariate is a large-scale index, so the two are
related but not identical.

## 3. PR, FAR and return period: one number, three forms

| Quantity | Value | 95% bootstrap |
|---|---|---|
| probability ratio $\mathrm{PR} = p_{\text{fact}}/p_{\text{cf}}$ | $2.116$ | $1.903$ to $2.346$ |
| attributable fraction $\mathrm{FAR} = 1 - 1/\mathrm{PR}$ | $0.527$ | $0.475$ to $0.574$ |
| return period, counterfactual | $5.3$ seasons | — |
| return period, factual | $2.5$ seasons | — |

The three statements are algebraically identical:

$$\mathrm{FAR} = 1 - \frac{1}{\mathrm{PR}}, \qquad
\frac{T_{\text{cf}}}{T_{\text{fact}}} = \mathrm{PR}, \qquad
T = \frac{1}{p} .$$

Two practical cautions:

1. **The FAR is the form most easily misread.** "53% of the events are attributable
   to the shift" is a statement about a *class* of events, not about any one event,
   and it says nothing about how rare the event is: a high FAR on a very rare event
   still describes a very rare event. Always report the frequency alongside the
   fraction.
2. **Report the interval on the ratio, not on the difference.** The bootstrap
   interval on the PR is asymmetric ($1.903$ to $2.346$) and the one on the FAR is
   not; converting one to the other requires care, and quoting "±0.1" hides the
   asymmetry.

## 4. The conditional risk ratio, and what the world coefficient means

Fitting $\mathrm{logit}\,\Pr(\text{event}\mid X, \text{World})
= a + bX + c\,\text{World}$ on the pooled sample gives

$$a = -1.994 \pm 0.145, \qquad b = +1.545 \pm 0.113, \qquad
c = -0.145 \pm 0.180,$$

so the conditional risk ratio at fixed $X$ is

$$\exp(c) = 0.865 \quad (95\%\ 0.723\ \text{to}\ 1.036),$$

which contains $1$. This is the **correct answer for this generator**: the world
changes only the distribution of $X$, not the event's response to $X$, so at a
fixed covariate value the probability is unchanged. The marginal PR of $2.116$
arises entirely from $X$ being shifted.

The pair of numbers is the informative report:

| Statement | Value | What it supports |
|---|---|---|
| conditional risk ratio | $0.87$ ($0.72$–$1.04$) | no change in the event's sensitivity to the covariate |
| marginal probability ratio | $2.12$ ($1.90$–$2.35$) | the event is about twice as frequent, because the covariate moved |

A study that reports only the marginal ratio can claim that the frequency changed;
only the conditional ratio can claim that the *response* changed. In real
attribution work both are reported, and their difference is what the physical
discussion is about — a world that changed the response as well would show
$\exp(c)$ away from 1, and that is the falsifiable content of the claim.

## 5. Rarer events, wider intervals

Repeating the analysis with rarer event definitions (a lower intercept $a$):

| $a$ | counterfactual events | factual events | PR | 95% interval | width |
|---|---|---|---|---|---|
| $-2.0$ | $374$ | $811$ | $2.17$ | $1.95$ to $2.42$ | $0.46$ |
| $-3.5$ | $123$ | $385$ | $3.13$ | $2.60$ to $3.80$ | $1.21$ |
| $-4.5$ | $56$ | $188$ | $3.36$ | $2.55$ to $4.58$ | $2.03$ |

The point estimate moves modestly, but the interval **widens by a factor of 4.4**
as the counterfactual count falls by a factor of 6.7. The mechanism is
arithmetic: the ratio is a ratio of counts, and its relative uncertainty is
dominated by the *smaller* world. With $n_{\text{cf}}$ events in the counterfactual
world and $n_{\text{fact}}$ in the factual one, the relative standard error of the
ratio is approximately

$$\frac{\sigma_{\mathrm{PR}}}{\mathrm{PR}} \approx
\sqrt{\frac{1}{n_{\text{cf}}} + \frac{1}{n_{\text{fact}}}} ,$$

so at $n_{\text{cf}} = 56$ the counterfactual alone contributes
$1/\sqrt{56} = 13.4\%$ and the total is about $16\%$ — matching the measured
interval width of $\pm2.03/3.36 = 60\%$ at $95\%$ (a bootstrap interval is wider
than the delta-method approximation because the counts are small and the ratio's
distribution is skewed).

The practical implication: **the cost of attributing a rare event is set by the
number of rare events in the counterfactual ensemble**, which is why attribution
studies of extreme events use very large model ensembles and why they report the
event count in each world rather than only the ratio.

## 6. What attribution cannot establish

1. **Causation without a model.** The counterfactual is produced by a model
   (climate or statistical), so the attribution inherits every model error. The
   demonstration's counterfactual is exact by construction; a real one is not, and
   the uncertainty of the model is usually larger than the sampling uncertainty
   computed here.
2. **A change in the response.** A marginal ratio cannot separate "the covariate
   moved" from "the event's sensitivity to the covariate changed"; only the
   conditional ratio can, and it needs the covariate to be measured in both worlds.
3. **Events outside the fitted range.** An event more extreme than anything in
   either ensemble is an extrapolation, and its probability ratio is a statement
   about the fitted tail — usually an extreme-value model — not about the data.
4. **A single event's cause.** Attribution is a statement about a class of events
   with a stated definition; a particular storm was made more likely by the shift
   only in the sense that events of its type were.
5. **The size of the human contribution.** The counterfactual is defined by a
   forcing scenario; different scenarios give different ratios, so "the human
   contribution" is a scenario-dependent quantity that must be named.

## 7. Assumptions and regime of validity

1. **The event definition is fixed in advance and identical in both worlds.**
   Moving the threshold after seeing the ratio is the multiplicity problem of
   [21-07-03](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/03-spectral-analysis-statistical.md)
   in another guise.
2. **The covariate is measured consistently in both worlds.** A reanalysis used for
   observations and a model output used for the counterfactual introduce a
   covariate-definition mismatch that can dominate the answer.
3. **The two worlds differ only in the forcing.** If the ensemble has a drift, a
   different resolution, or a different land surface, the ratio mixes those
   differences with the forcing.
4. **The event counts are independent draws.** Seasons within one ensemble member
   are correlated; the effective sample size is set by the number of members and by
   the autocorrelation, not by the number of seasons.
5. **The covariate scale is stated.** A shift of "1 K" depends on the index, its
   spatial averaging and its season; the same PR can be obtained from different
   shifts of different indices.

## The honest summary

On two synthetic worlds of 2000 seasons each, with a covariate shifted from
$\mathcal N(0,1)$ to $\mathcal N(1,1)$ and a probabilistic event definition, the
event frequency rises from $18.90\%$ to $40.00\%$, giving a probability ratio of
$2.116$ (95% $1.903$ to $2.346$), an attributable fraction of $0.527$ and a return
period falling from $5.3$ to $2.5$ seasons. Fitting the event on the covariate and
the world gives a conditional risk ratio of $0.865$, interval containing $1$, which
is the correct answer because this world changed only the covariate distribution:
the entire frequency change comes from the covariate moving, and none from a change
in the event's sensitivity. Making the event rarer moves the ratio modestly but
widens its interval by a factor of $4.4$, because the ratio's precision is set by the
smaller of the two worlds. The transferable conclusions: report the covariate, the
event definition and both ratios; report the event counts in each world; and state
the model that produced the counterfactual, because that model's error is not in
any interval computed here.

## Python demonstration

[`code/attribution_methods_demo.py`](./code/attribution_methods_demo.py) prints
every number quoted above. It:

1. generates the two worlds and prints the covariate distributions, the event
   probability model and the exact marginal probabilities computed by quadrature;
2. prints the event counts, the probability ratio and the attributable fraction with
   bootstrap intervals, and the two return periods;
3. fits the logistic model on the pooled sample, prints the three coefficients with
   intervals, the conditional risk ratio $\exp(c)$ and the comparison with the
   marginal ratio;
4. repeats the analysis for two rarer event definitions and prints the counts, the
   ratio and the interval width for each, then a `SYNTHETIC` provenance line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/08-causal-inference-and-design/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python attribution_methods_demo.py
```

It runs in under 0.3 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/03-attribution-methods-exercises.md`](./exercises/03-attribution-methods-exercises.md)
and [`exercises/03-attribution-methods-solutions.md`](./exercises/03-attribution-methods-solutions.md).

## Mastery checkpoint

Without notes:

1. Show that $\mathrm{FAR} = 1 - 1/\mathrm{PR}$ and compute the FAR for
   $\mathrm{PR} = 2.116$, $5$ and $1.2$. State the limit as the PR approaches 1.
2. Explain in two sentences why the conditional risk ratio is $0.87$ while the
   marginal ratio is $2.12$ in this generator, and which claim each supports.
3. Compute the relative standard error of a ratio of counts with $n_{\text{cf}} = 56$
   and $n_{\text{fact}} = 188$, and compare with the measured interval width.
4. A study reports a PR of 12 with no interval for an event observed three times in
   the counterfactual ensemble. State the two reasons the number is unusable.

## Common pitfalls

1. **Reporting the FAR without the frequency.** A $90\%$ attributable fraction on a
   rare event still describes a rare event.
2. **Confusing the marginal and conditional ratios.** They answer different
   questions; here they differ by a factor of $2.4$.
3. **Quoting a ratio without its event counts.** The precision is set by the smaller
   world, as the interval widths $0.46$, $1.21$ and $2.03$ show.
4. **Choosing the threshold after the analysis.** The event definition must be fixed
   in advance.
5. **Treating the model's counterfactual as exact.** The model error is absent from
   every interval computed from the samples.
6. **Extrapolating beyond either ensemble.** The ratio of two fitted tails is not a
   measurement.

## Where this is used

- **Extreme-event attribution**, where a specific flood, heatwave or storm is
  assessed for the role of the change
  ([16-07-03](../../16-atmosphere-climate/07-climate-extremes-and-attribution/03-event-attribution.md)).
- **Climate change detection and attribution**, where the covariate is a forcing
  fingerprint and the "event" is a trend
  ([16-07-02](../../16-atmosphere-climate/07-climate-extremes-and-attribution/02-detection-attribution.md)).
- **Hazard and risk assessment**, where the return period of a design event is
  revised in the light of a shifting distribution
  ([06-11-04](../../06-seismology/11-earthquake-statistics-and-hazard/04-psha.md)).
- **Wildfire, drought and compound-event studies**, where the event definition and
  the covariate scale are the most contested parts of the analysis.
- **Insurance and adaptation planning**, where a probability ratio must be converted
  into a load or a design change — with its interval.

## Related lessons

- [21-08-02 Causal Inference Methods and Counterfactuals](./02-causal-inference-methods.md) —
  the general logic and the identification assumptions.
- [21-08-01 Experimental and Survey Design for Earth Studies](./01-experimental-design.md) —
  the design that determines the ensemble size needed.
- [21-01-07 Extreme Value Theory for Geohazards](../../21-statistics-bayesian-ml/01-statistics-in-practice/07-extreme-value-theory.md) —
  the tail model an extreme attribution uses.
- [21-07-05 Point Processes and Seismicity Rate Models](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/05-point-processes.md) —
  the counting-process version of a frequency ratio.
- [21-09-02 Honest Reporting of Uncertainty and Limitations](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/02-reporting-uncertainty-ethics.md) —
  how to report a ratio whose model error exceeds its interval.

## Self-assessment checklist

- [ ] I can define the three ingredients of an attribution study.
- [ ] I can convert between PR, FAR and return period.
- [ ] I can distinguish the marginal from the conditional ratio.
- [ ] I can estimate a ratio from counts and from a logistic regression.
- [ ] I can explain how the rarity of the event sets the precision.
- [ ] I can list the five items an attribution report must contain.
