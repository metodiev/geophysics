# Exercises — 21-04-06 Feature Engineering for Earth Data

Attempt these before reading the
[solutions](./06-feature-engineering-solutions.md). The lesson is
[06 Feature Engineering](../06-feature-engineering.md). All data are
**SYNTHETIC**.

## ★ Foundational

**★1.** State which of these learners need feature scaling and which do not:
$k$-nearest neighbours, a decision tree, ridge regression, a neural network,
$k$-means.

**★2.** A 5-NN classifier scores $0.5067$ raw and $0.8333$ standardised. Compute
the improvement in percentage points and as a percentage of the raw value, and
state what the raw value represents.

**★3.** Logistic regression scores $0.4667$ on $(x_1, x_2)$ and $0.9733$ on
$(x_1, x_2, x_1x_2)$. Compute the improvement and state why the first value is
below chance.

## ★★ Applied

**★★4.** Explain, using the geometry of the two features, why a raw distance
metric dominated by a nuisance feature with $500$ times the informative feature's
scale reduces a 5-NN classifier to chance.

**★★5.** A target-derived feature correlates $0.9948$ with the target and raises
hold-out accuracy from $0.8167$ to $1.0000$. Explain why the hold-out did not
detect the leak, and give the diagnostic that would.

**★★6.** Derive two physically motivated features for a well-log lithology
classifier and state the assumption each encodes.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that measures how much of a model's accuracy comes
from feature construction versus model complexity for a stated nonlinear target.
State the data, the feature sets, the model classes, the metric, the replicate
count, and the predicted outcome at low and high complexity. A specification that
could not be executed is a failed answer.

**★★★8.** Design a **leakage-audit protocol** for a published machine-learning
study in geophysics: a sequence of checks, each with a pass criterion, that a
reviewer could apply from the paper's description alone.
