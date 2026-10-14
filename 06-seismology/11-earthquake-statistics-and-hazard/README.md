# Module 06-11 — Earthquake Statistics and Hazard

**Stages:** graduate → research · **Prerequisites:** modules 06-03, 06-04 and
06-05; the probability and statistics foundations of module 01-13.

This module is about what can and cannot be said from a catalogue of earthquakes.
It is built around one honest difficulty: **every number in it is a property of a
population and a model, never of the next event.** A b-value describes how many
events of each size to expect; a hazard curve is a rate of exceedance; an
aftershock forecast is a rate ratio that decays. None of them says where or when,
and the module spends as much effort on the limits of the statistics as on the
statistics themselves.

The second thread is bookkeeping. The magnitude of completeness $M_c$ is a
detectability statement, not a data property; declustering is a model choice that
moves the b-value by amounts comparable to the statistical error; the aleatory
scatter of a ground-motion model is irreducible while the median is estimable; and
the choice of a ground-motion relation outside its calibrated range is an
extrapolation that in-range data cannot arbitrate. Every lesson therefore states
which part of its answer is measurement, which is estimator, and which is a
modelling decision — and several lessons measure how large each part is in a
controlled synthetic experiment where the truth is known.

**All models and data in this module are SYNTHETIC.** The catalogues are simulated
from chosen Gutenberg-Richter, Omori-Utsu and ETAS parameters; the source models
and ground-motion relations are teaching forms with transparent coefficients; no
real catalogue, station, strong-motion record or published hazard model is used,
and no published parameter value is quoted as a measurement.

## Learning objectives

By the end of this module you will be able to:

1. Derive the Gutenberg-Richter law from an exponential magnitude density, estimate
   $b$ by maximum likelihood with its bin-width correction and its
   $b/\sqrt N$ standard error, and measure how much of the answer belongs to the
   completeness decision.
2. Write the ETAS conditional intensity, derive the branching ratio
   $K b/(b-\alpha)$, predict the offspring count of a mainshock inside a stated
   window, and fit the Omori-Utsu decay with the correct normalisation.
3. State, with arithmetic, why deterministic prediction is considered unattainable:
   memorylessness, the sampling distribution of b-value differences, the Bayes
   requirement on a false-alarm probability, and the inflation of significance by
   retrospective search.
4. Derive and evaluate the PSHA total-probability integral, verify it against its
   own total rate, convert between return period and probability exactly, and
   deaggregate the hazard into its contributing magnitudes and distances.
5. Decompose ground-motion scatter into within-event and between-event components,
   derive the lognormal identities used in hazard, and demonstrate that two
   relations can be indistinguishable inside their range and differ by a factor of
   more than 1.5 outside it.
6. Derive the SH site transfer function, explain why amplification requires a band
   and a damping, apply a site factor to a hazard curve, and solve the nonlinear
   site problem by fixed-point iteration.
7. Implement window and nearest-neighbour declustering, derive the
   nearest-neighbour metric from a rate ratio, and quantify what the choice does to
   the b-value and to the interevent-time statistics of the residual catalogue.

## Prerequisites

- [06-03 Earthquake Sources](../03-earthquake-sources/README.md) — moment, source
  spectra and rupture kinematics.
- [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  the magnitude scales every statistic here is built on.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  the physics that a ground-motion relation approximates.
- [01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md) —
  distributions, maximum likelihood, Bayes and uncertainty propagation.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Gutenberg-Richter, b-Value and Magnitude of Completeness](01-gutenberg-richter.md) | advanced | $b$ is an exponential's rate: derive the MLE, and measure how much of $b$ is the $M_c$ decision |
| 02 | [Aftershock Sequences: Omori, ETAS and Triggering](02-aftershocks.md) | doctoral | Branching ratio $Kb/(b-\alpha)$; the largest aftershock is a model output, not a constant |
| 03 | [Why Deterministic Prediction Is Considered Unattainable](03-earthquake-prediction-limits.md) | graduate | Bayes bounds the posterior; retrospective search manufactures significance |
| 04 | [Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic](04-psha.md) | doctoral | The total-probability integral, its verification, and its epistemic spread |
| 05 | [Ground-Motion Prediction Equations and Their Uncertainty](05-ground-motion-models.md) | doctoral | Aleatory versus epistemic; two fits agree inside the range and differ by 1.7 outside |
| 06 | [Hazard Maps, Site Amplification and Design Codes](06-hazard-mapping.md) | graduate | Resonance, damping, band and nonlinearity; a map is an interpolation rule |
| 07 | [Declustering, Completeness and Catalogue Physics](07-catalog-declustering.md) | graduate | The rule moves the b-value as much as the truth does |

## Suggested path

**If you are new to earthquake statistics:** lessons 01, 02 and 03 in order,
running every demonstration. Lesson 01 establishes the estimator bookkeeping that
the rest of the module reuses.

**If you come from engineering seismology:** start at 04 and 05, then read 06 for
the site chain, and finish with 07 — the declustering choice is what makes the
Poisson assumption in 04 defensible or not.

**If you are preparing a research project:** 01 §4 (completeness), 02 §5 (window
normalisation), 04 §7 (epistemic branches), 05 §7 (extrapolation) and 07 §5–6
(the declustering spread), plus the exercises at ★★★ level.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-gutenberg-richter.md`](01-gutenberg-richter.md) | Lesson 01 — frequency-magnitude statistics |
| [`02-aftershocks.md`](02-aftershocks.md) | Lesson 02 — Omori, ETAS and triggering |
| [`03-earthquake-prediction-limits.md`](03-earthquake-prediction-limits.md) | Lesson 03 — the limits of prediction |
| [`04-psha.md`](04-psha.md) | Lesson 04 — probabilistic hazard analysis |
| [`05-ground-motion-models.md`](05-ground-motion-models.md) | Lesson 05 — ground-motion relations and scatter |
| [`06-hazard-mapping.md`](06-hazard-mapping.md) | Lesson 06 — maps, site response and design |
| [`07-catalog-declustering.md`](07-catalog-declustering.md) | Lesson 07 — declustering and catalogue physics |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and Matplotlib:

```bash
cd 06-seismology/11-earthquake-statistics-and-hazard/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gutenberg_richter_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python aftershocks_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python earthquake_prediction_limits_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python psha_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ground_motion_models_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hazard_mapping_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python catalog_declustering_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), runs in a few seconds, needs no network
access, and exits 0. Each one prints the checks that make its numbers auditable —
the rate check in `psha_demo.py`, the total-offspring prediction in
`aftershocks_demo.py`, and the ground-truth scoring in
`catalog_declustering_demo.py` are examples.

## Mastery checkpoint

Complete this without notes:

> A SYNTHETIC catalogue of $N = 1200$ events above $M_c = 1.0$ (grid $0.1$) has
> mean reported magnitude $\bar m = 1.4207$, largest event $M\,4.6$, and a
> coefficient of variation of interevent times of $1.7$. **(a)** Compute $\hat b$
> and its standard error, and state the expected largest event as a function of
> $N$. **(b)** A second window of 200 events gives $\hat b = 0.75$. Decide whether
> the two b-values are consistent, showing the arithmetic. **(c)** Using $K = 0.02$,
> $\alpha = 0.9$, $p = 1.10$, $c = 0.05$ d, compute the expected number of direct
> offspring of a $M6.0$ mainshock inside 30 days. **(d)** State what the CV of 1.7
> implies for a hazard calculation that converts rates with $1-e^{-\lambda t}$, and
> name the operation that would be applied to the catalogue first.

A worked version of (a)–(c) appears in the lesson-01
[solutions](exercises/01-gutenberg-richter-solutions.md).

## Common pitfalls across this module

1. **Quoting a statistic without its conditioning.** A b-value needs $M_c$, $N$ and
   the declustering rule; a hazard curve needs its source model, its ground-motion
   model and its site condition.
2. **Confusing a rate with a prediction.** Every quantity in this module is a rate
   or a probability, and none of them names an event.
3. **Treating a model choice as a measurement.** Completeness, declustering, the
   ground-motion relation and the site factor are all decisions.
4. **Using the mean where the tail is the question.** Lognormal means are 1.2–1.4
   times the median, and hazard lives beyond both.
5. **Reporting a single number where the spread is the result.** The module's own
   measurements give factors of 4 between epistemic branches and factors of 2
   between equally well-fitting ground-motion forms outside their range.
6. **Assuming that more data settles a question it cannot.** In-range records
   cannot choose between two forms that agree in range; short windows cannot be
   made probable by any test with a finite false-alarm rate.

## Related modules

- [06-12 Induced and Triggered Seismicity](../12-induced-and-triggered-seismicity/README.md) —
  the same statistics where the triggering is the subject rather than a nuisance.
- [06-08 Receiver Functions and Crustal Structure](../08-receiver-functions-and-crustal-structure/README.md) —
  the layered-medium response used in lesson 06, measured from real conversions.
- [04-07 Geologic and Geophysical Hazards](../../04-earth-science-geology/07-geologic-hazards/README.md) —
  how hazard, exposure and vulnerability combine into risk.
- [21-01 Statistics in Geophysical Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  estimation, resampling and extreme-value theory.
- [18-05 Bayesian Inversion and Inference](../../18-inverse-problems/05-bayesian-inversion/README.md) —
  the formal treatment of epistemic uncertainty and logic trees.
- [13-04 Tectonophysics and Deformation](../../13-geodynamics-tectonics/04-tectonophysics-deformation/README.md) —
  the mechanics behind triggering and recurrence.
