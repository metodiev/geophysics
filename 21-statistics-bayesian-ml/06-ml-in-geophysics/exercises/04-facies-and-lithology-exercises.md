# Exercises — 21-06-04 Facies and Lithology Prediction from Well Logs

Attempt these before reading the
[solutions](./04-facies-and-lithology-solutions.md). The lesson is
[04 Facies and Lithology](../04-facies-and-lithology.md). All numbers are
**SYNTHETIC** and printed by
[`code/facies_and_lithology_demo.py`](../code/facies_and_lithology_demo.py).

Deep-interval results (test interval below 90 m, 2 100 samples):

| Class | share of interval | nearest-centroid recall | tree recall |
|---|---|---|---|
| sand | 0.089 | 0.608 | 0.597 |
| shale | 0.892 | 0.995 | 0.986 |
| carbonate | 0.019 | 1.000 | 0.975 |

Overall accuracy: shuffled split 0.959 / 0.950, whole-bed split 0.961 / 0.950,
depth split 0.961 / 0.951 (nearest centroid / decision tree).

Class-mean drift from shallow to deep: sand GR $70 \to 90$ API with
$\sigma_{\mathrm{GR}} = 10$ API; sand RHOB $2.32 \to 2.48$ g/cm³ with
$\sigma = 0.050$ g/cm³; sand NPHI $0.24 \to 0.32$ v/v with $\sigma = 0.040$ v/v.

## ★ Foundational

**★1.** Compute the accuracy of a model that predicts "shale" everywhere on the
deep interval. Then verify the reported overall accuracies by computing the
weighted sum $\sum_k \text{share}_k \times \text{recall}_k$ for both models, and
state the discrepancy with the printed values to three decimals.

**★2.** Compute the macro-average (unweighted mean) of the per-class recalls for
both models and compare each with its overall accuracy. State which of the two
numbers a shale-dominated appraisal well should be judged on.

**★3.** Express the shallow-to-deep drift of the sand response in units of the
log noise for each of the three logs. State, in one sentence, why a drift of
this size is systematically harmful while noise of the same standard deviation
is not.

## ★★ Applied

**★★4.** Write the Gaussian maximum-likelihood discriminant with pooled
covariance, show that equal priors and isotropic covariance reduce it to a
nearest-centroid rule, and show that a non-uniform prior enters as an additive
$\ln \pi_k$. Using the training prior for sand (0.392) and the true test share
(0.089), compute the additive shift and the equivalent distance shift in units
of $\sigma$ for an isotropic covariance.

**★★5.** Design the experiment that measures the effect of adding depth as a
feature. State the metric, both splits, the expected direction of the change in
each, the confound, and the control that separates the two effects.

**★★6.** Compute the effective number of independent beds in a 900-sample
shuffled test set given 254 beds over 3 000 samples. Recompute the binomial
standard error of an accuracy of 0.95 using the bed count instead of the sample
count, and state by what factor the naive interval is too narrow.

## ★★★ Research-oriented

**★★★7.** Design the study that decides whether a facies model transfers to a
new well. Name the strata, the metrics, the split, the reference labels and their
uncertainty, and the result that would block deployment. State what the test
cannot establish.

**★★★8.** One of the four facies in the target well does not appear anywhere in
the training interval. Predict what the model does, quantify the recall the
report will show for that class, and specify the diagnostic and the modelling
change that would detect and handle the situation.

**★★★9.** Specify an interval-level evaluation: a predicted sand interval counts
as correct if it overlaps a true sand bed over at least half its length. Define
precision and recall at interval level, explain why they differ from the
sample-level versions, and state the sizing needed to compare two models at a
stated resolution.
