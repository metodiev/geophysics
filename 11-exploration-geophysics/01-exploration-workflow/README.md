# Module 11-01 — The Exploration Workflow

**Stages:** intermediate → doctoral · **Prerequisites:** modules 05-01, 05-05 and
04-06; basic probability.

This module is about the decisions that surround geophysical measurements in
exploration, rather than the measurements themselves. Its central honest
difficulty is that **the number everyone wants — a reserve tonnage — is not a
measurement.** It is the output of a chain of choices: a target model, a detection
threshold, a cut-off grade, a price deck and a discount rate. Each link is made by
a person, each one moves the answer, and none of them is checkable by the data.
The three lessons here make that chain explicit and quantitative, so that the
geophysical contribution can be located inside it rather than credited with the
whole result.

The chain has a characteristic order. First, **staging**: reconnaissance narrows
$10^{4}\ \mathrm{km^2}$ to a drill pad through a sequence of irreversible
spending decisions, and the arithmetic of the funnel (a geometric series, not a
sum of budgets) determines what a discovery costs before anyone asks whether the
geology is right. Second, **targeting**: a target model — size, depth and property
contrasts — is followed by a detectability calculation, and the ranking of methods
changes with depth and with the model. Third, **valuation**: the measurement is
priced by what the *decision* would do differently with it, which is a
decision-theoretic quantity, expressible in closed form, and usually much smaller
than intuition suggests.

A second theme runs through all three lessons: **information is worth only what it
changes.** A perfectly accurate survey that never alters an action is worth
exactly zero, and this is a theorem, not a caveat — the demonstration verifies it
numerically. A survey for a prospect whose prior probability is far from the
indifference point is nearly worthless however good it is, and a survey whose
positives merely move a posterior from 2% to 6% is worth nothing at all because no
action changes. The corollary is uncomfortable and is stated in every lesson:
where the geophysics is cheapest (regional, low prior), its value is hardest to
demonstrate; where it is most valuable, it typically costs the most.

All models and data in this module are **SYNTHETIC**. Stage probabilities, costs,
distributions, metal prices, discount rates, target properties, detection
thresholds and payoffs are chosen teaching values. No number here is a published
statistic for any real belt, deposit, company or contract, and no dataset is
invented and presented as measured.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** the probability funnel and expected spend of a staged exploration
   program, and **explain** why the expected spend is a geometric series.
2. **Compute** tonnage, head grade and contained metal above a cut-off grade for a
   lognormal grade distribution, and **derive** the marginal break-even cut-off
   $c^{*}=C/(rP)$.
3. **Quantify** how mill capacity and a discount rate move the optimal cut-off, and
   **state** which inputs of a reserve statement are choices rather than
   measurements.
4. **Derive** the anomaly of a buried body for gravity, magnetics and EM, and
   **compute** the depth at which two methods' signal-to-noise ratios cross.
5. **Convert** an anomaly and a noise level into a detection probability, and
   **rank** candidate methods for a stated target model and depth.
6. **Derive** the expected value of perfect information
   $\mathrm{EVPI} = \min(pW,(1-p)K)$ and the expected value of sample information,
   and **price** a survey and the optimal number of repeats.
7. **Demonstrate** that $E[V(p)] \ne V(E[p])$ for a convex value function, and
   **state** why a value-of-information study is itself a model.

## Prerequisites

- [05-01-01 The Central Idea: Property Contrasts Produce Signals](../../05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md)
  and [05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off](../../05-core-geophysics/01-what-geophysics-measures/03-resolution-depth-tradeoff.md).
- [05-05-01 Survey Planning: Objectives, Target Resolution, Budget](../../05-core-geophysics/05-survey-design-and-acquisition/01-survey-planning.md).
- [04-06-02 Mineral Deposit Types and Their Geophysical Signatures](../../04-earth-science-geology/06-petroleum-and-mineral-systems/02-mineral-deposits.md).
- [21-03-01 The Bayesian Paradigm](../../21-statistics-bayesian-ml/03-bayesian-inference/01-bayesian-paradigm.md)
  and [18-06-06 Decision Under Uncertainty](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md)
  for the probability and decision theory used in lesson 03.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Exploration Lifecycle: Reconnaissance to Reserve Definition](01-exploration-lifecycle.md) | intermediate | The expected spend is a geometric series; a reserve is a price-dependent plan, not a measurement |
| 02 | [Targeting Strategy and Method Selection](02-targeting-and-strategy.md) | advanced | Detection depth and method ranking follow from a target model, and the ranking reverses with depth and with the property contrast |
| 03 | [Cost, Risk and Value of Information in Exploration](03-cost-benefit.md) | doctoral | $\mathrm{EVPI}=\min(pW,(1-p)K)$ peaks at the indifference probability; information is worth only what it changes |

## Suggested path

**If you are new to exploration:** lessons 01 and 02 in order, running each
demonstration. Lesson 01's cut-off arithmetic is the part that most repays
careful reading, because it separates what was found from what was decided.

**If you come from geophysics and want the decision side:** start with 02 §5–§6
(detection probability and the crossover), then 03 in full.

**If you are preparing a research project or a proposal:** 01 §5–§6 (cut-off,
capacity and discounting), 03 §4 and §9 (EVSI, its assumptions and the flaw of
averages), plus the ★★★ exercises, which ask for specifications rather than
calculations.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-exploration-lifecycle.md`](01-exploration-lifecycle.md) | Lesson 01 |
| [`02-targeting-and-strategy.md`](02-targeting-and-strategy.md) | Lesson 02 |
| [`03-cost-benefit.md`](03-cost-benefit.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 11-exploration-geophysics/01-exploration-workflow/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python exploration_lifecycle_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python targeting_strategy_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cost_benefit_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access and exits 0.

## Mastery checkpoint

Complete this without notes:

> A SYNTHETIC program has three stages costing $2$, $12$ and $80$ MUSD with
> advance probabilities $0.50$, $0.20$ and $0.40$. **(a)** Compute the overall
> probability of success and the expected spend per discovery. **(b)** A discovered
> deposit grades lognormally with median $0.32\%$ Cu and $\sigma_g = 0.50$, over
> $60\ \mathrm{Mt}$ of rock; compute the ore tonnage and head grade above a
> $0.20\%$ cut-off, and the metal. **(c)** Compute the break-even cut-off for
> $C = 13\ \mathrm{USD/t}$, $r = 0.85$, $P = 8000\ \mathrm{USD/t}$, and state the
> one input you would test first. **(d)** A gravity survey gives $d' = 2.5$ at the
> target depth against a magnetic $d' = 12$; the magnetic method costs a quarter as
> much per km². State which to buy and the assumption on which that depends.
> **(e)** With $W = 300$ MUSD and $K = 40$ MUSD at $p = 0.10$, compute $p^{*}$,
> EVPI and the EMV of drilling.

Worked versions appear in the lesson-01 and lesson-03 solutions.

## Common pitfalls across this module

1. **Summing stage budgets.** The expected spend is a geometric series; the
   unconditional sum overstates committed capital by an order of magnitude.
2. **Reporting a cut-off or a reserve without its price deck.** Both are decisions
   in disguise.
3. **Ranking methods by anomaly alone.** Cost per unit area and the noise level are
   half of the ranking, and the ranking reverses with depth and target type.
4. **Buying accuracy rather than value.** A test with $\mathrm{TPR} = \mathrm{FPR}$
   has exactly zero value whatever its accuracy.
5. **Plugging a mean probability into a convex value function.** The measured bias
   in this module's example is $+42\%$.
6. **Treating a VOI figure as a property of a survey.** It is a property of a
   decision, and it does not transfer between projects.
7. **Forgetting the shared failure mode.** Twenty independent targets do not
   diversify a wrong regional concept, and the probability of total failure rises
   faster than the expected value falls.

## Related modules

- [11-02 Mineral Exploration Geophysics](../02-mineral-exploration/README.md) —
  target models for deposit classes and the methods that see them.
- [05-07 Interpretation and Integration](../../05-core-geophysics/07-interpretation-and-integration/README.md)
  — reporting results with uncertainty, which these lessons' numbers must satisfy.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md)
  — the general theory of decision under uncertainty.
- [21-03 Bayesian Inference](../../21-statistics-bayesian-ml/03-bayesian-inference/README.md)
  — priors, likelihoods and the update used in lesson 03.
