---
id: 21-04-05
title: "Decision Trees, Random Forests and Gradient Boosting"
level: graduate
prereqs: ["21-04-02", "21-04-03"]
estimated_minutes: 60
tags: [machine-learning, decision-trees, random-forest, gradient-boosting, ensembles]
---

# Decision Trees, Random Forests and Gradient Boosting

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** how a decision tree partitions feature space and **compute** a
   Gini impurity and the gain from a split.
2. **Measure** the effect of depth on training and test accuracy and **identify**
   the overfitting point.
3. **Describe** bagging and **state** why averaging decorrelated trees reduces
   variance but not bias.
4. **Describe** gradient boosting and **derive** the residual-fitting step for
   squared loss.
5. **Compare** the two ensemble families by what each reduces, and **state** when
   each is preferred.
6. **State** the failure modes of tree ensembles: extrapolation, axis-aligned
   bias and importance misreading.

All data in this lesson are **SYNTHETIC**, generated in the demonstration. No
measured value is used.

## Prerequisites

- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](02-bias-variance.md) —
  the decomposition that distinguishes the two ensemble methods.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](03-model-assessment.md) —
  how tree depth and boosting rounds are chosen.
- [21-04-04 Regularisation: Ridge, Lasso, Early Stopping](04-regularization-ml.md) —
  early stopping, which boosting needs explicitly.

## 1. Intuition: rectangles, then many rectangles

A decision tree partitions the feature space into axis-aligned rectangles and
predicts a constant inside each. It is interpretable, needs no scaling, handles
mixed variable types, and is a universal approximator given enough depth. Its
weakness is variance: a single split depends on the data, so a small change in
the sample can change the tree's structure, and deep trees memorise noise.

Ensembles fix that weakness in two different ways. **Bagging** fits many deep
trees on bootstrap samples and averages them, which reduces variance without
touching the bias of the individual tree. **Boosting** fits many shallow trees
sequentially, each to the residual of the previous ensemble, which reduces bias
by building up an additive model. Choosing between them is choosing which term of
the decomposition is dominant.

## 2. Splitting

At a node holding a fraction $p$ of class-1 labels, the **Gini impurity** is

$$G(p) = 1 - p^{2} - (1-p)^{2} = 2p(1-p),$$

maximal at $p = 0.5$ and zero at $p \in \{0,1\}$. The gain from splitting a node
into left and right children with fractions $w_L, w_R$ is

$$\Delta = G(p) - \big[w_L\,G(p_L) + w_R\,G(p_R)\big],$$

and the tree greedily splits on the feature and threshold maximising $\Delta$.
Two properties are worth stating because they explain the failure modes: the
split is **axis-aligned**, so a diagonal boundary must be approximated by a
staircase; and the criterion is **greedy**, so a split that is only useful after
another split is never found. A circle cannot be represented by one axis cut, and
neither can the XOR function — a point that makes trees poor at exactly the
interactions that are trivial for a linear model with product features.

## 3. Bagging and random forests

Bagging fits $B$ trees on bootstrap resamples and averages their predictions. If
each tree has variance $\sigma^{2}$ and the pairwise correlation of their
predictions is $\rho$, the ensemble variance is

$$\operatorname{Var} = \rho\sigma^{2} + \frac{1-\rho}{B}\sigma^{2}
\;\longrightarrow\; \rho\sigma^{2} \text{ as } B\to\infty .$$

Two consequences follow directly. Averaging attacks only the second term, so with
correlated trees the benefit saturates — which is why a random forest
**decorrelates** the trees by considering only a random subset of features at each
split, reducing $\rho$ and lowering the floor. And bagging leaves the bias
$\rho\sigma^{2}$ untouched: it cannot fix a tree that is systematically wrong.

## 4. Gradient boosting

Boosting builds an additive model
$F_m(x) = F_{m-1}(x) + \nu\,h_m(x)$ where $h_m$ is a small tree fitted to the
negative gradient of the loss. For squared error the negative gradient is the
residual,

$$r_i^{(m)} = y_i - F_{m-1}(x_i), \qquad
F_m = F_{m-1} + \nu\,h_m, \qquad \nu \in (0, 1],$$

so each tree corrects what the ensemble got wrong. For other losses the same
recipe applies with the appropriate pseudo-residual. The **learning rate** $\nu$
trades speed against accuracy: smaller $\nu$ needs more trees but generalises
better, and the pair $(\nu, \text{number of trees})$ is regularised by early
stopping on a validation set, exactly as in
[21-04-04](04-regularization-ml.md) §4.

## 5. Worked example

**Single tree depth.** Data: $400$ points, target $1$ where
$x_1^{2} + x_2^{2} > 2$ — a circular boundary — with $5\ \%$ label noise on
$200$ training and $200$ test points.

| depth | train accuracy | test accuracy |
|---|---|---|
| 1 | 0.6350 | 0.5400 |
| 2 | 0.7850 | 0.7250 |
| 3 | 0.8650 | 0.8000 |
| 5 | 0.9600 | 0.8900 |
| 8 | 0.9900 | 0.8800 |

A stump attains only $0.5400$ because a single axis cut cannot approximate a
circle; accuracy rises steeply to depth $5$, where the test accuracy peaks at
$0.8900$; and at depth $8$ the training accuracy reaches $0.9900$ while test
accuracy **falls** to $0.8800$. The $10\ \%$ train-test gap at depth 8 is the
overfitting signature: the extra splits are cutting around individual noisy
labels.

**Bagging.** A single depth-6 tree scores $0.8900$ and a bag of $100$ such trees
scores $0.8900$ — no measurable improvement. This is the honest result for this
size of data set: with $200$ training points a depth-6 tree is already
low-variance, so the second term of the variance formula is small and there is
little to average away. The bag and the single tree disagree on only $5.0\ \%$ of
test points, which confirms that the trees are highly correlated ($\rho$ close to
one) and that the ensemble floor is set by that correlation.

**Boosting.** A regression target $y = \sin(x) + 0.3x + \mathcal N(0, 0.2^{2})$
with $120$ training points, boosted with stumps at learning rate $\nu = 0.3$:

| rounds | training residual MSE |
|---|---|
| 1 | 1.40289 |
| 10 | 0.07656 |
| 50 | 0.06037 |
| 100 | 0.05972 |
| 200 | 0.05947 |

The residual falls by a factor of $18$ in the first ten rounds, then flattens:
the irreducible noise variance is $0.2^{2} = 0.04$, and the ensemble approaches
$0.0595$ — within a factor of $1.5$ of the floor. Adding rounds beyond $200$
cannot go below the floor, and with more rounds the ensemble would begin to fit
the noise; that is where early stopping intervenes, and it is the reason boosting
requires a validation set.

## Assumptions and regime of validity

1. **Trees do not extrapolate.** Beyond the range of the training data they
   predict the nearest leaf's constant; a tree must never be used for
   extrapolation.
2. **Axis-aligned splits induce a staircase bias.** A smooth diagonal boundary
   needs many splits.
3. **Greedy splitting misses interactions.** XOR-like targets are hard; a feature
   that encodes the interaction solves it instantly, as
   [21-04-06](06-feature-engineering.md) §2 shows.
4. **Importance measures are not causal.** Impurity importance favours
   high-cardinality features and is computed on the training data; permutation
   importance on held-out data is preferable.
5. **Boosting needs early stopping** on a validation set; without it the training
   residual goes below the noise floor and test error rises.
6. **Bagging cannot reduce bias.** With systematically wrong trees the ensemble
   is systematically wrong.

## The honest summary

Trees and ensembles are the workhorse of tabular geophysical prediction, and the
demonstration measures the two families' different jobs. A single tree's test
accuracy rose from $0.5400$ at a stump to $0.8900$ at depth $5$ and then fell to
$0.8800$ at depth $8$ as training accuracy reached $0.9900$ — overfitting made
visible. Bagging $100$ such trees changed nothing ($0.8900$ against $0.8900$)
because the trees were almost perfectly correlated; boosting drove a regression
residual from $1.40289$ to $0.05947$ in $200$ rounds, approaching but not passing
the $0.04$ noise floor. What the demonstration does **not** establish is that
either method extrapolates: both are interpolation machines, and a prediction
outside the training range is a constant chosen by the nearest leaf.

## Python demonstration

[`code/trees_and_ensembles_demo.py`](./code/trees_and_ensembles_demo.py) prints
every number quoted above. It:

1. builds a CART classifier by hand and sweeps the depth;
2. bags $100$ deep trees and compares with a single tree;
3. boosts stumps on a regression target and reports the residual trajectory.

```bash
cd 21-statistics-bayesian-ml/04-machine-learning-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python trees_and_ensembles_demo.py
```

It runs in about a third of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/05-trees-and-ensembles-exercises.md`](./exercises/05-trees-and-ensembles-exercises.md)
with worked solutions in
[`exercises/05-trees-and-ensembles-solutions.md`](./exercises/05-trees-and-ensembles-solutions.md).

## Mastery checkpoint

Without notes, a depth-8 tree reaches training accuracy $0.9900$ and test
accuracy $0.8800$; a bag of $100$ depth-6 trees matches a single tree at
$0.8900$; and boosting reduces the residual MSE from $1.40289$ to $0.05947$ over
$200$ rounds with a noise floor of $0.04$.

1. Compute the Gini impurity of a node with $p = 0.5$ and of a pure node, and
   verify the $p = 0.5$ maximum.
2. Compute the train-test accuracy gap at depth 8 and compare with depth 5.
3. Using $\operatorname{Var} = \rho\sigma^{2} + (1-\rho)\sigma^{2}/B$, compute
   the ensemble variance for $\rho = 0.9$, $B = 100$ and $\sigma^{2} = 1$, and
   state the fraction of the single-tree variance that remains.
4. Compute the ratio of the final boosting MSE to the noise floor.

## Common pitfalls

1. **Reading a low training error as skill.** Training accuracy reached $0.9900$
   while test accuracy had already turned down.
2. **Expecting bagging to fix a biased learner.** It reduces variance only, and
   with correlated trees the floor is $\rho\sigma^{2}$.
3. **Boosting without early stopping.** The training residual passes below the
   noise floor and test error rises.
4. **Extrapolating with a tree.** The prediction outside the training range is a
   constant.
5. **Using impurity importance as a causal statement.** It rewards
   high-cardinality features and uses training data.
6. **Forgetting that a tree is scale-invariant but not distribution-shift
   invariant.** Moving to a new basin changes the leaf constants entirely.

## Where this is used

- **Facies and lithology prediction** from well logs, where trees handle mixed
  variable types without scaling.
- **Prospectivity mapping**: random forests over many correlated evidence layers.
- **Seismic attribute classification**: boosting for tabular attributes.
- **Missing-data problems**: trees split on other variables when one is absent.
- **Baseline models**: a gradient-boosted ensemble is the standard strong baseline
  against which a deep model must be justified.

## Related lessons

- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](02-bias-variance.md) —
  the two terms the ensembles attack.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](03-model-assessment.md) —
  how depth and rounds are chosen.
- [21-04-06 Feature Engineering for Earth Data](06-feature-engineering.md) —
  why a product feature makes an XOR target trivial for a tree.
- [21-04-07 PCA, ICA and Manifold Learning](07-dimensionality-reduction.md) —
  the alternative way to compress many correlated features.
- [21-06-04 Facies and Lithology Prediction from Well Logs](../06-ml-in-geophysics/04-facies-and-lithology.md) —
  the applied version of this lesson.

## Self-assessment checklist

- [ ] I can compute a Gini impurity and a split gain.
- [ ] I can identify the overfitting depth from two accuracy curves.
- [ ] I can explain the bagging variance formula and the role of $\rho$.
- [ ] I can derive the residual-fitting step of gradient boosting.
- [ ] I can say which ensemble reduces which term.
- [ ] I can name the failure modes, starting with extrapolation.
