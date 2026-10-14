---
id: 21-04-06
title: "Feature Engineering for Earth Data"
level: graduate
prereqs: ["21-04-03", "21-04-01"]
estimated_minutes: 55
tags: [machine-learning, feature-engineering, scaling, leakage, domain-features]
---

# Feature Engineering for Earth Data

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why feature scaling changes the behaviour of distance-based and
   gradient-based learners and **demonstrate** the effect with numbers.
2. **Construct** features that make a non-separable problem separable and
   **state** what the construction assumes.
3. **Identify** target leakage and **measure** the inflation it produces.
4. **Derive** physically motivated features for Earth data and **state** the
   constraint each encodes.
5. **Decide** when feature engineering is preferable to a more complex model.
6. **State** what a feature does and does not carry about the physics.

All data in this lesson are **SYNTHETIC**, generated in the demonstration. No
measured value is used.

## Prerequisites

- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](03-model-assessment.md) —
  the leakage that feature engineering most often introduces.
- [21-04-01 ML Taxonomy: Supervised, Unsupervised, Reinforcement](01-ml-taxonomy.md) —
  the learners whose behaviour depends on the features.
- [21-01-06 Spatial and Directional Statistics in Earth Science](../01-statistics-in-practice/06-spatial-statistics-geo.md) —
  the directional and spatial variables that need their own encoding.

## 1. Intuition: the learner only sees the features

A model cannot use information that is not in its inputs, and it must use every
input it is given. That asymmetry is the whole subject. Features that carry the
physics make a hard problem easy; features that carry noise, or that carry the
answer, make an easy problem misleading. The demonstration's three examples are
one of each:

- a nuisance variable with $500$ times the scale of the informative one destroys a
  distance-based learner unless the features are standardised;
- a product term makes an XOR target linearly separable without changing the
  model;
- a feature derived from the target lifts accuracy from $0.8167$ to $1.0000$ on a
  problem where nothing real has changed.

## 2. Scaling

Distance-based methods (k-nearest neighbours, kernel methods, k-means,
hierarchical clustering), gradient-based methods (neural networks, penalised
regression), and any method using a common penalty are sensitive to the units of
the features.

- **Standardisation**: $x' = (x - \bar x)/s$ — mean zero, unit variance.
- **Min–max scaling**: $x' = (x - x_{\min})/(x_{\max} - x_{\min})$ — bounded in
  $[0,1]$, sensitive to outliers.
- **Robust scaling**: subtract the median, divide by the MAD — for spiky data.

Tree-based methods are invariant to monotone transformations and need no scaling;
that invariance is one of their practical advantages. The rule is therefore not
"always scale" but "scale if the learner uses distances, dot products or a common
penalty".

**The demonstration's measurement.** A 5-nearest-neighbour classifier on two
features — one informative with unit scale, one pure noise with scale $500$ —
achieves an accuracy of $0.5067$ on raw features and $0.8333$ after
standardisation. The raw accuracy is at the chance level: the Euclidean distance
is dominated by the noise coordinate, so the classifier's "neighbours" carry no
information about the label. Scaling recovers the entire signal, and it is a
$64\ \%$ improvement obtained by no change to the model.

## 3. Constructing features

The XOR target $y = \mathbf 1\{x_1 > 0\} \oplus \mathbf 1\{x_2 > 0\}$ has no
marginal signal: the best axis-aligned or linear split attains chance. Adding the
product $x_1 x_2$ makes the classes linearly separable, because the sign of the
product is exactly the XOR. The demonstration fits logistic regression twice:

| features | test accuracy |
|---|---|
| $(x_1, x_2)$ | $0.4667$ |
| $(x_1, x_2, x_1 x_2)$ | $0.9733$ |

The model, the optimiser and the data are identical; only the feature set changed.
The lesson generalises: **when a model fails, the first question is whether the
relationship is representable in the features you supplied**, and the cheapest fix
is a feature, not a bigger network.

For Earth data the standard constructions are:

- **ratios and logs** for positive quantities spanning decades — permeability,
  resistivity, element concentration;
- **differences between channels** for spectral or multichannel data, since a
  difference cancels a common gain;
- **wavelength or frequency** rather than index, so that the model's smoothness
  assumptions apply on the physical scale;
- **lagged and window statistics** for time series — rolling mean, variance,
  spectral centroid — which encode the local regime;
- **spatial coordinates and distance-to-feature** for maps, which encode position
  and proximity rather than raw easting and northing;
- **physics-derived invariants**: impedances, Poisson's ratio, Vp/Vs, density
  contrasts — quantities whose definition already encodes the physics.

Each construction carries an assumption. A ratio asserts proportionality; a log
asserts multiplicative structure; a lag asserts that the past predicts the
present over that interval. Stating the assumption is what makes the feature
auditable.

## 4. Leakage

The demonstration's third example builds a feature from the target itself, with
only $0.05$ of noise, and correlates $0.9948$ with it. On a random train-test
split:

| feature set | hold-out accuracy |
|---|---|
| two honest features | $0.8167$ |
| with the target-derived feature | $1.0000$ |

Holding out data does **not** protect against this: the leaked feature carries the
target for the test points as well, and only its numerical values, not its
identity, are what the model reads. The remedies are structural rather than
statistical — exclude any variable recorded after the outcome, any variable
derived from a field measurement that was itself used to define the label, and
any aggregate computed with knowledge of the test period. The diagnostic is the
one from [21-04-03](03-model-assessment.md) §5: replace the target with noise and
check that the pipeline scores at chance.

## 5. Worked example

The demonstration measures all three effects:

**Scaling.** raw $0.5067$, standardised $0.8333$ — a $64\ \%$ improvement from
scaling alone. The chance level for the balanced binary target is $0.50$, so the
raw result is indistinguishable from a coin.

**Construction.** $(x_1, x_2)$ gives $0.4667$ — *below* chance, which is what a
logistic fit on a target with no marginal signal produces — and adding $x_1x_2$
gives $0.9733$. The remaining $2.7\ \%$ error is the irreducible part of the
synthetic labels' noise.

**Leakage.** Two honest features give $0.8167$; adding the target-derived feature
raises this to a perfect $1.0000$, with a Pearson correlation of $0.9948$ between
the feature and the target. A perfect score on a noisy synthetic problem is the
signature, and it is exactly the score a careless analysis would report as a
success.

## Assumptions and regime of validity

1. **Scaling statistics must be computed on the training fold.** Standardising
   with the full-data mean leaks the validation distribution.
2. **Constructed features must be computable at prediction time.** A rolling
   statistic that uses future values is unavailable in deployment.
3. **Physics-based features encode assumptions.** A ratio assumes
   proportionality; applying it where that fails introduces a systematic error.
4. **Leakage is structural, not statistical.** No split protects against a
   feature derived from the target.
5. **More features are not free.** Each adds variance and a multiple-comparison
   burden; selection must be inside the fold.
6. **A feature that helps in one basin may mislead in another.** Distribution
   shift affects constructed features as much as raw ones.

## The honest summary

Feature engineering is where domain knowledge enters a machine-learning model, and
the demonstration measures both directions of its effect. Standardising two
features with wildly different scales raised 5-NN accuracy from $0.5067$ to
$0.8333$; adding a product feature raised a logistic fit from $0.4667$ to
$0.9733$ without touching the model; and adding a target-derived feature produced a
perfect $1.0000$ on a problem where nothing real had changed. The last number is
the warning: the same mechanism that encodes the physics can encode the answer,
and no validation scheme distinguishes them. What the demonstration does **not**
establish is that any particular physical feature generalises to a new region;
that is a hypothesis about the geology, tested by spatial validation and not by
the feature's performance in-sample.

## Python demonstration

[`code/feature_engineering_demo.py`](./code/feature_engineering_demo.py) prints
every number quoted above. It:

1. compares k-NN with and without standardisation;
2. shows that a product feature makes XOR linearly separable;
3. measures the accuracy inflation from a target-derived feature.

```bash
cd 21-statistics-bayesian-ml/04-machine-learning-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python feature_engineering_demo.py
```

It runs in under a tenth of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/06-feature-engineering-exercises.md`](./exercises/06-feature-engineering-exercises.md)
with worked solutions in
[`exercises/06-feature-engineering-solutions.md`](./exercises/06-feature-engineering-solutions.md).

## Mastery checkpoint

Without notes, k-NN scores $0.5067$ raw and $0.8333$ standardised; logistic
regression scores $0.4667$ on $(x_1, x_2)$ and $0.9733$ on
$(x_1, x_2, x_1x_2)$; and a target-derived feature raises a hold-out accuracy
from $0.8167$ to $1.0000$ with a correlation of $0.9948$.

1. Compute the improvement from scaling and from feature construction as
   percentages.
2. State why a raw accuracy of $0.5067$ is not evidence that the learner "worked
   slightly".
3. State what would have to be true of the leaked feature for its use to be
   legitimate.
4. Give one physically motivated feature for a well-log lithology classifier and
   state the assumption it encodes.

## Common pitfalls

1. **Not scaling for a distance-based learner.** Accuracy was at chance with the
   noise feature dominating the distance.
2. **Computing scaling statistics on all the data.** Leakage.
3. **Using a target-derived or future-derived feature.** It produces perfect
   scores on noise.
4. **Adding features without a hypothesis.** Each feature is a multiple
   comparison.
5. **Assuming a feature that helps in one area helps everywhere.** Distribution
   shift applies to constructed features too.
6. **Preferring a complex model to a good feature.** The product feature solved an
   unsolvable problem for a model that was already there.

## Where this is used

- **Well-log lithology prediction**: ratios and differences such as
  $\ln(R_{\text{deep}}/R_{\text{shallow}})$.
- **Seismic attribute classification**: instantaneous frequency, envelope and
  curvature, which encode physical properties rather than raw amplitudes.
- **Geochemistry**: log-ratios and normalised element concentrations, with the
  closure constraint handled explicitly.
- **Time-series monitoring**: rolling statistics and calendar coordinates.
- **Prospectivity mapping**: distance-to-fault and distance-to-contact, which
  encode the geological controls.

## Related lessons

- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](03-model-assessment.md) —
  the leakage this lesson measures.
- [21-04-01 ML Taxonomy: Supervised, Unsupervised, Reinforcement](01-ml-taxonomy.md) —
  the learners whose behaviour depends on scale.
- [21-04-05 Decision Trees, Random Forests and Gradient Boosting](05-trees-and-ensembles.md) —
  methods that need no scaling but do need interaction features.
- [21-05-07 Self-Supervised Learning with Unlabelled Earth Data](../05-deep-learning/07-self-supervised.md) —
  learning features from data instead of constructing them.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](../06-ml-in-geophysics/09-ml-pitfalls-geophysics.md) —
  where leakage appears in practice.

## Self-assessment checklist

- [ ] I can state which learners need scaling and which do not.
- [ ] I can construct a feature that makes a problem separable.
- [ ] I can detect leakage and name its structural remedies.
- [ ] I can derive a physics-based feature and state its assumption.
- [ ] I can decide between a feature and a more complex model.
- [ ] I can name what a feature does not encode.
