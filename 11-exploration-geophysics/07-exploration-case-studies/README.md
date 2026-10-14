# Module 11-07 — Exploration Case Studies

**Stages:** research · **Prerequisites:** modules
[11-01](../01-exploration-workflow/README.md), [11-02](../02-mineral-exploration/README.md),
[11-03](../03-hydrocarbon-exploration/README.md), [11-04](../04-geothermal-exploration-geophysics/README.md),
[11-05](../05-groundwater-exploration/README.md) and
[11-06](../06-geotechnical-and-engineering/README.md); the probability and
decision material of [11-01-03](../01-exploration-workflow/03-cost-benefit.md).

This module closes the folder by doing the thing the earlier modules only
promised: taking a whole exploration decision apart. Each lesson is a **case
study** of one target class — a porphyry district, a sedimentary play, a
geothermal field, an arid-region groundwater programme — and each is written as
an **argument archetype** rather than as a report on a real place. The lesson
states its target, its evidence suite, its claimed link and, most importantly,
the alternatives for every indicator; then it does the probability and expected
value arithmetic that converts the evidence into a drilling decision.

The discipline that holds the module together is stated at the top of every
lesson: **no site-specific numbers are quoted.** A grade, a reserve, a
permeability, a recharge rate or a success ratio belongs to a specific report
under a specific convention, and repeating one from memory would be exactly the
failure this curriculum forbids. All quantitative content therefore comes from
the demonstrations, whose inputs are stated SYNTHETIC models, and the lessons say
what you must retrieve from the primary literature to attach real numbers to a
real place.

Across the four archetypes the same three failure modes recur, which is the
module's real lesson. First, **the base rate dominates**: the same anomaly is a
1% and a 50% chance in two different settings, and a survey that cannot state its
prior has no defensible targeting logic. Second, **independence is assumed and
rarely true**: correlated indicators inflate a posterior multiplicatively, and
correlated play elements move a joint chance by a factor of two. Third, **the
decision is not the anomaly**: a survey earns its cost only by changing an
action, and the value of information is a property of the decision, not of the
instrument.

**All models and data in this module are SYNTHETIC.** No real deposit, basin,
field, aquifer, borehole or operation is used, and no site-specific number is
quoted or implied.

## Learning objectives

By the end of this module you will be able to:

1. **Decompose** any exploration case into target, evidence, claimed link and
   alternatives, and say which part each data set addresses.
2. **Compute** positive predictive values and targets-per-discovery from a base
   rate and indicator performance.
3. **Demonstrate** and quantify the bias from treating correlated indicators or
   correlated play elements as independent.
4. **Quantify** the model error in a depth estimate (source shape) and show that
   it exceeds the measurement error.
5. **Compute** expected monetary value with an uncertain resource, and
   **distinguish** probability of success from probability of profit.
6. **Compute** a value of information and explain why it is non-monotonic in the
   prior.
7. **Compute** a stored-heat resource as a distribution, and **state** which
   parameters dominate its range.
8. **Convert** a resource into a well count through a flow-rate distribution, and
   explain the resource/reserve distinction.
9. **Compute** an exceedance probability from a Gutenberg-Richter relation and
   relate it to a protocol decision.
10. **Design** a staged survey and compare strategies by net value rather than by
    the number of targets found.
11. **Compute** a water balance and a depletion time, and state which quantities
    are not geophysical.
12. **Write** a recommendation that separates measurement, model and choice, with
    a stated error rate.

## Prerequisites

- [11-01 The Exploration Workflow](../01-exploration-workflow/README.md),
  especially [11-01-03 Cost, Risk and Value of Information](../01-exploration-workflow/03-cost-benefit.md).
- [11-02 Mineral Exploration Geophysics](../02-mineral-exploration/README.md).
- [11-03 Hydrocarbon Exploration Geophysics](../03-hydrocarbon-exploration/README.md).
- [11-04 Geothermal Exploration Geophysics](../04-geothermal-exploration-geophysics/README.md).
- [11-05 Groundwater Exploration Geophysics](../05-groundwater-exploration/README.md).
- [11-06 Geotechnical and Engineering Geophysics](../06-geotechnical-and-engineering/README.md).
- [18-05 Bayesian Inversion](../../18-inverse-problems/05-bayesian-inversion/01-bayes-inverse-formulation.md)
  and [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md).

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Case Study: Porphyry Copper District](01-case-study-porphyry.md) | research | Base rates, correlated indicators, shape ambiguity, break-even drilling |
| 02 | [Case Study: Basin Analysis and Play Assessment](02-case-study-basin.md) | research | Play chance with a shared factor, DHI as a test, success versus profit, VOI |
| 03 | [Case Study: Geothermal Field Development](03-case-study-geothermal.md) | research | Stored heat as a distribution, resource versus reserve, MT ambiguity, seismicity |
| 04 | [Case Study: Arid-Region Groundwater Exploration](04-case-study-groundwater.md) | research | The base rate, staged selection by net value, and the water balance the survey cannot measure |

## Suggested path

**If you have completed modules 11-01 to 11-06:** read 01 → 02 → 03 → 04 in
order, running each demonstration. They are deliberately parallel: the same four
questions are asked of four different targets, and the fourth lesson reuses the
first's arithmetic.

**If you want only the decision logic:** read 11-01-03, then §3 of lessons 01 and
02, then §3.2 and §3.4 of lesson 04.

**If you are preparing a research project:** read all four lessons' "what this
lesson does and does not assert" statements first — they are the template for how
to write about a real case without quoting numbers you cannot support — then
lesson 03 §3 and lesson 02 §3.4 for the two uncertainty types.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-case-study-porphyry.md`](01-case-study-porphyry.md) | Lesson 01 |
| [`02-case-study-basin.md`](02-case-study-basin.md) | Lesson 02 |
| [`03-case-study-geothermal.md`](03-case-study-geothermal.md) | Lesson 03 |
| [`04-case-study-groundwater.md`](04-case-study-groundwater.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises with worked solutions for every lesson |
| [`code/`](code) | Four runnable, print-only demonstrations |

## How to run the demos

Use the project virtual environment, from the module's `code/` directory:

```bash
cd 11-exploration-geophysics/07-exploration-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_porphyry_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_basin_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_geothermal_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_groundwater_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.
Each demo's printed numbers are the ones quoted in its lesson.

**A note on the demos.** Because this module quotes no real numbers, the
demonstrations carry the entire quantitative content. Their inputs are chosen
teaching values — indicator performances, costs, values, resource distributions —
and the structure of the calculation, not the digits, is the transferable result.
Where a number in a lesson appears to come from nowhere, it is printed by the
demo in that lesson's `code/` directory.

## Mastery checkpoint

Complete this without notes:

> Choose one of the four archetypes. Using only SYNTHETIC inputs that you state
> yourself, produce a one-page exploration case: **(a)** the target, and the
> threshold that defines success; **(b)** the evidence suite, with the false
> positive of each indicator and an argument for which pairs are conditionally
> dependent and which are independent; **(c)** the base rate, its source, and the
> posterior after one indicator and after two; **(d)** the expected value of the
> first hole, using a stated cost and value; **(e)** the value of information of
> the *next* survey, with the decision it would change; and **(f)** a statement
> of what you would have to retrieve from the primary literature to make the case
> about a real place, and one sentence that a reviewer could use to falsify your
> argument.

The point of the checkpoint is the accounting: every number labelled as measured,
modelled or chosen, and every probability attached to a base rate.

## Common pitfalls

1. **Reporting anomalies instead of probabilities.** The product of a survey is a
   ranked list with an error rate.
2. **Omitting the base rate.** The same anomaly is a 1% and a 50% chance in two
   settings.
3. **Assuming independence for correlated evidence.** It inflates the posterior
   multiplicatively, and it is the largest single error in targeting.
4. **Confusing the chance of success with the chance of profit**, and the
   resource with the reserve.
5. **Believing a survey is valuable because it is informative.** Its value is the
   change it makes to a decision.
6. **Quoting a remembered number.** Where a number is needed, it is either
   printed by a demo in this module or retrieved from the primary literature.

## Related modules

- [11-01 The Exploration Workflow](../01-exploration-workflow/README.md) — the
  lifecycle, targeting and cost-benefit framing these cases apply.
- [11-02](../02-mineral-exploration/README.md), [11-03](../03-hydrocarbon-exploration/README.md),
  [11-04](../04-geothermal-exploration-geophysics/README.md),
  [11-05](../05-groundwater-exploration/README.md) and
  [11-06](../06-geotechnical-and-engineering/README.md) — the evidence suites.
- [06-12-05 Documented Case Studies: Attribution](../../06-seismology/12-induced-and-triggered-seismicity/05-case-studies-induced.md)
  — the same archetype discipline applied to induced seismicity.
- [18-05 Bayesian Inversion](../../18-inverse-problems/05-bayesian-inversion/01-bayes-inverse-formulation.md),
  [18-06 Decision Under Uncertainty](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md)
  and [21-08 Causal Inference and Experimental Design](../../21-statistics-bayesian-ml/08-causal-inference-and-design/02-causal-inference-methods.md).
- [23-07 Field Campaign Case Studies](../../23-field-methods-instruments/07-field-campaign-case-studies/01-case-study-seismic-array.md)
  — the acquisition side of a real campaign.
