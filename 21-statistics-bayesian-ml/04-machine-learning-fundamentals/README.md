# Module 21-04 — Machine Learning Fundamentals

**Stages:** advanced → research · **Prerequisites:**
[21-01 Statistics in Geophysical Practice](../01-statistics-in-practice/README.md)
and [01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md).

Machine learning is statistics with the emphasis moved from explanation to
prediction, and this module is the bridge between the two. It starts from the
taxonomy — supervised, unsupervised, reinforcement — and then works through the
questions that decide whether a predictor is any good: how complexity trades bias
against variance, how a score is estimated honestly, how models are constrained,
how structure in features changes what is learnable, how dimensionality is
reduced, and how unlabelled data are grouped. Every method is presented as a
statistical estimator with assumptions, not as an algorithm with parameters.

The organising idea is that **every number a learner reports is an estimate of
something outside the training set**, and the module measures how easily that
estimate is corrupted. A single hold-out came out $43\ \%$ below the
cross-validated error; a pipeline that selected features on the full data beat an
honest one by $40.8\ \%$ **on data with no signal at all**; a target-derived
feature lifted hold-out accuracy from $0.8167$ to a perfect $1.0000$. The
validation machinery of lesson 03 exists because the training error cannot warn
about any of this.

A second thread is the **bias-variance ledger**, which recurs in every lesson from
a different angle. Regularisation moves an estimator along the curve by design;
bagging reduces variance and leaves bias untouched; boosting attacks bias
directly; feature construction removes bias at the cost of nothing; and
dimensionality reduction discards the directions in which the model had variance
but no signal. The module's numbers are chosen so that these movements are
visible: bias² of $0.36$ against variance of $293.87$ at degree 9, a bag that
changes accuracy by nothing because its trees are $95\ \%$ correlated, and a
silhouette that peaks at the true three clusters while the $k$-means objective
cannot choose $k$ at all.

All data in this module are **SYNTHETIC**. Every demonstration generates its own
data from stated parameters, trains its models from scratch with NumPy, and prints
the numbers the lessons quote. The demonstrations are print-only, seeded with
`np.random.default_rng(20261014)`, need no network, create no files, and each runs
in under a second.

## Learning objectives

By the end of this module you will be able to:

1. **Classify** a learning problem into one of the three paradigms and **state**
   what can validate each.
2. **Derive** the bias-variance decomposition and **measure** all three terms.
3. **Estimate** generalisation error with cross-validation, **choose** a metric
   that matches the decision, and **detect** leakage.
4. **Write** the ridge and lasso objectives, **select** a penalty, and
   **interpret** early stopping.
5. **Explain** and **measure** what bagging and boosting each reduce.
6. **Construct** features that make a problem learnable and **audit** them for
   leakage.
7. **Reduce** dimensionality with PCA, ICA or a manifold method according to the
   structure assumed, and **state** what is discarded.
8. **Cluster** data with a method whose cluster definition is stated, and
   **validate** the result externally.

## Prerequisites

- [21-01-04 Linear, Multiple and Robust Regression](../01-statistics-in-practice/04-regression.md) —
  the estimator this module regularises and cross-validates.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../01-statistics-in-practice/03-resampling.md) —
  the resampling behind cross-validation.
- [01-13-06 Point Estimation, Bias, Consistency and Efficiency](../../01-mathematics/13-probability-and-statistics-foundations/06-estimation-theory.md) —
  bias and variance as estimator properties.
- [21-03-06 Bayesian Workflow and Principled Model Building](../03-bayesian-inference/06-bayesian-workflow.md) —
  the model-checking discipline this module inherits.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [ML Taxonomy: Supervised, Unsupervised, Reinforcement](01-ml-taxonomy.md) | advanced | Gradient descent reproduced the closed form to four decimals; a clustering objective cannot choose $k$ |
| 02 | [Bias-Variance Trade-Off, Underfitting and Overfitting](02-bias-variance.md) | advanced | At degree 9, variance is $99.85\ \%$ and bias² $0.12\ \%$ of the error; the test MSE minimum is at degree 5 |
| 03 | [Cross-Validation, Metrics and the Danger of Leakage](03-model-assessment.md) | graduate | A hold-out came out $43\ \%$ low; leakage improved a noise-only task by $40.8\ \%$ |
| 04 | [Regularisation: Ridge, Lasso, Early Stopping](04-regularization-ml.md) | advanced | Ridge never zeroes a coefficient, lasso took the non-zero count from $18$ to $4$, early stopping halted at iteration $363$ |
| 05 | [Decision Trees, Random Forests and Gradient Boosting](05-trees-and-ensembles.md) | graduate | Depth 8 raised training accuracy to $0.9900$ and lowered test accuracy to $0.8800$; bagging changed nothing; boosting reached $1.49\times$ the noise floor |
| 06 | [Feature Engineering for Earth Data](06-feature-engineering.md) | graduate | Scaling lifted 5-NN from $0.5067$ to $0.8333$; a product feature lifted logistic regression from $0.4667$ to $0.9733$ |
| 07 | [PCA, ICA and Manifold Learning](07-dimensionality-reduction.md) | research | PCA explained $97.44\ \%$ of variance; ICA recovered source kurtoses to $0.02$; a parabola left $99.77\ \%$ curvature in the residual |
| 08 | [Clustering and Unsupervised Structure Discovery](08-clustering.md) | graduate | Silhouette $0.6841$ found the three clouds; $k$-means captured only $74.40\ \%$ of a crescent where density clustering got $100.00\ \%$ |

## Suggested path

**If you are new to machine learning:** lessons 01 → 02 → 03, running every
demonstration. Lesson 02 is the conceptual core; lesson 03 is the discipline
without which nothing else is trustworthy.

**If you are fitting models already:** lesson 03 in full, then lesson 04, then
lesson 06. Leakage and penalty selection are the two mistakes that most often
invalidate an applied result.

**If you work with many correlated variables:** lessons 07 → 08 → 05, in that
order. The kurtosis comparison in lesson 07 §3 and the crescent example in lesson
08 §5 are the two results that change practice.

**If you are preparing a paper:** lesson 03 §5 and §6, lesson 06 §4, and the
★★★ exercises; each describes an audit your own pipeline should pass before
submission.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-ml-taxonomy.md`](01-ml-taxonomy.md) | Lesson 01 |
| [`02-bias-variance.md`](02-bias-variance.md) | Lesson 02 |
| [`03-model-assessment.md`](03-model-assessment.md) | Lesson 03 |
| [`04-regularization-ml.md`](04-regularization-ml.md) | Lesson 04 |
| [`05-trees-and-ensembles.md`](05-trees-and-ensembles.md) | Lesson 05 |
| [`06-feature-engineering.md`](06-feature-engineering.md) | Lesson 06 |
| [`07-dimensionality-reduction.md`](07-dimensionality-reduction.md) | Lesson 07 |
| [`08-clustering.md`](08-clustering.md) | Lesson 08 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Eight runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/ml_taxonomy_demo.py`](code/ml_taxonomy_demo.py) | Gradient descent against the closed form, logistic accuracy, $k$-means objective, bandit regret |
| [`code/bias_variance_demo.py`](code/bias_variance_demo.py) | Train and test error by degree, Monte-Carlo bias-variance decomposition |
| [`code/model_assessment_demo.py`](code/model_assessment_demo.py) | Hold-out versus $k$-fold, classification metrics and AUC, leakage inflation |
| [`code/regularization_ml_demo.py`](code/regularization_ml_demo.py) | Ridge and lasso paths, cross-validated penalty, early stopping |
| [`code/trees_and_ensembles_demo.py`](code/trees_and_ensembles_demo.py) | Tree depth sweep, bagging, boosting residual trajectory |
| [`code/feature_engineering_demo.py`](code/feature_engineering_demo.py) | Scaling effect, product feature, target-derived leakage |
| [`code/dimensionality_reduction_demo.py`](code/dimensionality_reduction_demo.py) | PCA explained variance, ICA source recovery, manifold residual |
| [`code/clustering_demo.py`](code/clustering_demo.py) | $k$-means with silhouette, density clustering with noise, single-linkage heights |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 21-statistics-bayesian-ml/04-machine-learning-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ml_taxonomy_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python bias_variance_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python model_assessment_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python regularization_ml_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python trees_and_ensembles_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python feature_engineering_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python dimensionality_reduction_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python clustering_demo.py
```

Every demo prints labelled results with units, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access, creates no files and
exits 0. All run in under a second; the longest, `model_assessment_demo.py`, takes
about half a second because of its repeated refitting.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A colleague predicts lithology from eight well logs with a gradient-boosted
> ensemble. **(a)** They report a training accuracy of $0.99$ and a test accuracy
> of $0.88$ and describe the model as "highly accurate". State the two numbers you
> would ask for instead, and why. **(b)** Their cross-validation uses a random
> split over log intervals from the same wells. State the error and the scheme
> that fixes it. **(c)** They add a feature defined as the interval's produced-water
> cut and the accuracy rises to $0.999$. State the diagnosis and the check that
> would prove it. **(d)** They penalise with a ridge penalty applied to unscaled
> logs whose ranges differ by two orders of magnitude. State the error. **(e)** A
> clustering of the same logs peaks at $k = 3$ with a silhouette of $0.68$, and
> they name the three clusters as facies. State what is missing before that step
> is defensible.

Worked versions of (a)–(e) appear in the lesson solutions at ★★★ level.

## Common pitfalls across this module

1. **Reporting the training score.** Training accuracy reached $0.9900$ while test
   accuracy had already fallen to $0.8800$.
2. **One hold-out as the model's error.** It came out $43\ \%$ below the
   cross-validated mean, with a fold spread of $32\ \%$.
3. **Leakage through a target-derived feature.** It produced a perfect hold-out
   score, and a $40.8\ \%$ improvement on data with no signal.
4. **Selecting the penalty or the features outside the fold.** Both inflate the
   score; both are avoided by wrapping the pipeline.
5. **Penalising unscaled predictors.** The penalty is a different constraint on
   each feature unless they share a scale.
6. **Expecting bagging to fix a biased learner.** With trees $95\ \%$ correlated,
   the variance floor is $\rho\sigma^{2}$ and $100$ trees changed nothing.
7. **Naming a cluster a class.** A silhouette of $0.6841$ measures geometry;
   validation against core or a generative model is what licenses a name.

## Related modules

- [21-01 Statistics in Geophysical Practice](../01-statistics-in-practice/README.md) —
  the estimation and robustness tools this module builds on.
- [21-03 Bayesian Inference](../03-bayesian-inference/README.md) — where
  regularisation is a prior and the ELBO is a training loss.
- [21-05 Deep Learning](../05-deep-learning/README.md) — the same principles with
  far larger model classes.
- [21-06 Machine Learning in Geophysics](../06-ml-in-geophysics/README.md) — the
  applied versions of these methods on real Earth data.
- [21-02 Geostatistics](../02-geostatistics/README.md) — spatial structure and the
  blocking that cross-validation must respect.
- [18-09 Machine Learning in Inversion](../../18-inverse-problems/09-machine-learning-inversion/README.md) —
  learners embedded in inverse problems.
