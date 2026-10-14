# Module 05-01 — What Geophysics Measures and Why

**Stages:** intermediate → advanced · **Prerequisites:** modules 01 and 02
(mathematics, physics), especially
[02-01-04 Conservation Laws](../../02-physics/01-measurement-and-physical-reasoning/04-conservation-laws.md)
and [01-01-03 Units and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md).

This module is the entry point to the core of the curriculum. It answers the
question every later method module assumes has been answered: *what is it that
geophysics actually measures, and why does that make some targets easy and
others impossible?*

It is deliberately conceptual but quantitative. Every claim is either derived
in the lesson, computed in a demonstration, or stated as a range with a source.
No "typical values" appear without qualification.

## Learning objectives

By the end of this module you will be able to:

1. Explain why a property *contrast*, not a property, produces a signal, and
   say which property dominates each major method.
2. Classify any method by source, field type, measurement domain and target
   property, and state what each choice costs in resolution.
3. Derive the anomaly-width law for potential fields and the skin depth for
   diffusive fields, and use both to state achievable resolution and depth.
4. Explain non-uniqueness, construct a null-space vector for a linear
   discretised operator, and state what selects one model from an equivalence
   class.
5. Produce an auditable method-selection decision with a computed
   contrast-to-noise ratio.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [The Central Idea: Property Contrasts Produce Signals](./01-physical-property-contrast.md) | intermediate | Only contrasts produce anomalies |
| 02 | [Taxonomy of Methods: Active/Passive, Source/Receiver Geometry](./02-method-taxonomy.md) | intermediate | Four questions sort every method |
| 03 | [Resolution, Penetration Depth and the Fundamental Trade-Off](./03-resolution-depth-tradeoff.md) | advanced | Width tracks depth; EM penetration tracks period |
| 04 | [Non-Uniqueness of Geophysical Models](./04-ambiguity-and-nonuniqueness.md) | advanced | The data constrain the field, not the source |
| 05 | [Choosing a Method: A Decision Framework](./05-choosing-a-method.md) | intermediate | Contrast, depth, noise, cost — in that order |

## Suggested path

**New to geophysics:** all five lessons in order, then the exercises. Budget
six to ten hours; lesson 03 and lesson 04 are the two that repay rereading.

**Already know a method or two:** start with lesson 04. Non-uniqueness is the
concept most often missing from practice-oriented training, and it explains why
interpretation is a modelling exercise rather than a lookup.

**Preparing to design a survey:** lesson 05 last, and do the CNR calculation by
hand for your own target before trusting any of it.

## Materials

| Path | Contents |
|---|---|
| [`01-physical-property-contrast.md`](./01-physical-property-contrast.md) | Lesson 01 |
| [`02-method-taxonomy.md`](./02-method-taxonomy.md) | Lesson 02 |
| [`03-resolution-depth-tradeoff.md`](./03-resolution-depth-tradeoff.md) | Lesson 03 |
| [`04-ambiguity-and-nonuniqueness.md`](./04-ambiguity-and-nonuniqueness.md) | Lesson 04 |
| [`05-choosing-a-method.md`](./05-choosing-a-method.md) | Lesson 05 |
| [`exercises/`](./exercises/) | Graded problem sets and worked solutions for every lesson |
| [`code/property_contrast_demo.py`](./code/property_contrast_demo.py) | Contrast → signal → detectability, with units |
| [`code/resolution_depth_demo.py`](./code/resolution_depth_demo.py) | Measured width law and resolvable-separation law |

## How to run the demonstrations

From this module's directory, using the project virtual environment:

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python code/property_contrast_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python code/resolution_depth_demo.py
```

Both scripts run offline, print labelled results with SI and field units, and
exit 0. They use no downloaded data and no wall-clock timings.

The non-uniqueness demonstration lives in the forward-modelling module, because
it belongs to both:

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ../03-forward-modelling-principles/code/annihilator_nonuniqueness_demo.py
```

## Mastery checkpoint

Without notes: a 60 m radius sphere with 500 kg/m³ density contrast sits at
200 m depth under a survey where the gravimeter repeatability is 0.01 mGal and
the Bouguer-density uncertainty alone contributes 0.2 mGal.

**(a)** Compute the peak anomaly. **(b)** Compute a defensible signal-to-noise
ratio. **(c)** State whether the body is detectable, and on what the answer
turns. **(d)** Repeat for a body at 100 m and state the ratio of the two
answers. **(e)** Explain in two sentences why improving the gravimeter to
0.001 mGal does not change your conclusion.

Lesson 01 Section 6.1 and the demonstration contain the numbers needed for (a)
and (d); the rest is yours.

## Common pitfalls across this module

1. **Treating a method name as an answer.** "We should run magnetics" is an
   answer to no question.
2. **Using a remembered property value.** Ranges and sources, always.
3. **Assuming resolution can be bought.** For potential fields it cannot.
4. **Reporting a model without its selection criterion.** A model is a choice.
5. **Confusing a good data fit with a meaningful model.** The
   non-uniqueness demonstration prints five models that all fit equally well.

## Related modules

- [05-02 Geophysical Fields and Observables](../02-geophysical-fields-and-observables/README.md)
  — the units, noise and reductions this module refers to.
- [05-03 Forward Modelling Principles](../03-forward-modelling-principles/README.md)
  — turning a contrast distribution into a predicted data set.
- [05-04 Rock Physics](../04-rock-physics/README.md) — where the contrasts come
  from.
- [18-inverse-problems](../../18-inverse-problems/README.md) — how a model is
  estimated once the forward problem is understood.
