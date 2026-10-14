# Exercises — 21-04-03 Cross-Validation, Metrics and the Danger of Leakage

Attempt these before reading the [solutions](./03-model-assessment-solutions.md).
The lesson is [03 Model Assessment](../03-model-assessment.md). All data are
**SYNTHETIC**.

## ★ Foundational

**★1.** A single hold-out gives MSE $0.1177$ and 5-fold cross-validation gives
$0.2080 \pm 0.0669$. Compute the percentage by which the hold-out understates the
cross-validated error and state the likely cause.

**★2.** For TP $= 151$, FP $= 0$, FN $= 18$, TN $= 331$, compute the accuracy,
precision and recall directly from the confusion counts and verify them against
the demonstration's values.

**★3.** A leak-free pipeline scores MSE $1.1869$ and a leaking one $0.7021$ on
data with no signal and unit noise variance. State the true expected MSE and what
each number demonstrates.

## ★★ Applied

**★★4.** Explain why the $k$ fold estimates in cross-validation are not
independent, and state the consequence for the naive standard error
$\mathrm{sd}(\hat L_j)/\sqrt k$.

**★★5.** Compute the ROC AUC from ranks for a toy set of five scores and labels,
then state why the demonstration's AUC of $1.0000$ can coexist with a recall of
$0.8935$.

**★★6.** Name the three common forms of leakage, and for each give one
geophysical example and the splitting scheme that would remove it.

## ★★★ Research-oriented

**★★★7.** Specify a **leakage-detection experiment**: a study that measures how
much a candidate pipeline's validation score is inflated by (i) scaling outside
the fold, (ii) feature selection outside the fold, and (iii) random instead of
grouped splitting. State the data, the metric, the replicate count, and the
predicted inflation for each. A specification that could not be executed is a
failed answer.

**★★★8.** Design a **spatial cross-validation study** that compares random,
blocked and leave-one-transect-out splitting for a model predicting a spatially
autocorrelated target, and states the expected ordering of the reported errors
and which one estimates deployment performance.
