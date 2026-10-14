# Solutions — 21-04-06 Feature Engineering for Earth Data

> Read after attempting. Lesson:
> [06 Feature Engineering](../06-feature-engineering.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — Which learners need scaling

| learner | needs scaling? | why |
|---|---|---|
| $k$-nearest neighbours | **yes** | distances are Euclidean, so units set the metric |
| decision tree | no | splits are on single features and are invariant to monotone rescaling |
| ridge regression | **yes** | a common penalty $\lambda\|\beta\|_2^{2}$ is a different constraint on each unscaled predictor |
| neural network | **yes** | gradient descent and initialisation are scale-sensitive |
| $k$-means | **yes** | distances to centroids are Euclidean |

The rule is: scale when the learner uses distances, dot products, or a common
penalty across features. Trees and other rank-based methods are invariant and need
no scaling, which is a genuine practical advantage.

---

## ★2 — Scaling improvement

$$\text{improvement} = 0.8333 - 0.5067 = 0.3266 = 32.66 \text{ percentage points},$$

$$\frac{0.3266}{0.5067} = 64.5\ \%\ \text{relative improvement}.$$

The raw value $0.5067$ is the **chance level** for a balanced binary target (the
theoretical value is $0.50$), so the unscaled classifier carries **no
information**. It is not "working slightly"; it is a coin flip that happens to land
$0.7$ percentage points above $0.50$ because of sampling. Scaling recovers the
entire signal, and no change was made to the model.

---

## ★3 — Feature construction

$$0.9733 - 0.4667 = 0.5066 = 50.66 \text{ percentage points}.$$

The first value is **below chance** because on XOR data neither feature carries
any marginal information: the label depends only on the *combination* of signs,
and a logistic regression on $(x_1, x_2)$ can do no better than a random guess. The
slight deficit from $0.50$ is the sampling noise of a $150$-point test set. Adding
$x_1x_2$ — whose sign *is* the XOR — makes the classes linearly separable and the
same model reaches $0.9733$; the residual $2.7\ \%$ is the irreducible part of the
label noise in this synthetic target.

---

## ★★4 — Why the nuisance feature destroys the classifier

A 5-NN classifier assigns a point the majority label among its five nearest
neighbours under Euclidean distance. With two features of scales $1$ and $500$,

$$d^2 = (x_1 - x_1')^{2} + (x_2 - x_2')^{2},$$

and a typical difference in the nuisance coordinate, of order $500$, contributes
$2.5\times10^{5}$ to $d^{2}$ while a typical difference in the informative
coordinate contributes of order $1$. Any two points are therefore "nearest" iff
they are close **in the nuisance coordinate only** — the informative feature is
numerically invisible. Since the nuisance coordinate is independent of the label,
the neighbours carry no information and the classifier is at chance. Standardising
both coordinates to unit variance makes the two contributions comparable and
restores the signal.

---

## ★★5 — Why the hold-out missed the leak

The hold-out test asks whether the model generalises to **points it has not seen**.
The leaked feature is not a property of the training set; it is a property of the
data table, and it carries the target value for every row — training and test
alike. The correlation of $0.9948$ applies to the hold-out rows just as much as to
the training rows, so the model predicts the hold-out labels from the leaked
feature and scores perfectly. The hold-out is doing its job correctly; the problem
is that the feature is inadmissible, not that the estimate is wrong.

**The diagnostic:** replace the target column with pure noise, refit the whole
pipeline, and score it. An honest pipeline returns the chance level
(accuracy $\approx$ base rate, MSE $\approx$ the variance of the noise); a leaking
one returns a better-than-chance score, because it is reading the noise through the
leaked path. In the demonstration on pure noise the leak-free pipeline scored
$1.1869$ and the leaking one $0.7021$, both against a true expected MSE of $1.0$ —
which is the same test applied to a different leak.

---

## ★★6 — Two physically motivated well-log features

**Feature 1: the deep-to-shallow resistivity ratio,**
$\ln(R_{\text{deep}}/R_{\text{shallow}})$.
*Assumption:* the two curves share a common mud-filtrate and formation-water
resistivity scaling, so their **ratio** isolates the movable-hydrocarbon effect and
cancels the common gain. It also asserts multiplicative (log-scale) structure,
which is why a log is taken rather than a difference.

**Feature 2: the ratio of compressional to shear slowness,**
$V_p/V_s$ (equivalently Poisson's ratio).
*Assumption:* the two slownesses respond to the same rock but with different
sensitivity to fluid saturation and lithology, so their ratio is a
fluid-independent lithology indicator. It is a **physics-derived invariant** whose
definition already encodes the elastic theory, which is exactly what makes it more
transferable than the raw slownesses.

Both features assert proportionality and shared scaling; both fail if the two
curves were acquired by different tools with different calibrations, and the
assumption belongs in the report.

---

## ★★★7 — Feature construction versus model complexity

**Data.** A target with a genuine interaction: $y = \mathbf 1\{x_1x_2 > 0\}$
(XOR) with $5\ \%$ label noise, $n = 1000$, two features $x_1, x_2 \sim U(-2,2)$.

**Feature sets.** (i) raw $(x_1, x_2)$; (ii) with the product $x_1x_2$; (iii) with
all products and squares $(x_1, x_2, x_1^{2}, x_2^{2}, x_1x_2)$.

**Model classes.** Logistic regression (linear in the features), a decision tree
with depth $d \in \{1, 2, 3, 5, 8\}$, and a $2$-layer neural network with
$h \in \{2, 8, 32\}$ hidden units.

**Metric.** Held-out accuracy on $2000$ independent points, with $M = 200$
replicates so the mean accuracy has a standard error of about $1\ \%$ at
$p = 0.95$.

**Prediction.** With raw features, the linear model is at chance ($\approx 0.50$)
at every complexity; the tree needs depth $\ge 5$ to approach $0.9$ because XOR
requires two successive axis-aligned splits; the network with $h \ge 8$ reaches
$\approx 0.95$ if trained long enough. Adding the product feature makes the
**linear** model reach $\approx 0.95$ immediately. Adding all quadratic terms does
not help further and slightly hurts at small $n$ through variance.

The headline is the comparison at matched accuracy: a single constructed feature
achieves what a deeper tree or network achieves with far more parameters, so the
study quantifies the trade between engineering a feature and buying one with
capacity.

---

## ★★★8 — A leakage-audit protocol

A reviewer can run the following checks from the paper's description alone, each
with an explicit pass criterion:

1. **Noise-target test.** Replace the target with pure noise, rerun the *entire*
   pipeline exactly as described, and check that the score is at chance (accuracy
   equal to the base rate, AUC $0.5$, MSE equal to the target variance). *Fail* if
   the score is better than chance, which proves a leak.
2. **Fold-containment check.** List every preprocessing step — scaling,
   imputation, feature selection, dimensionality reduction, hyper-parameter
   tuning — and verify that each is described as fitted **inside** the training
   fold. *Fail* if any is fitted on the full data set.
3. **Split-validity check.** Verify that the split respects group structure (well,
   station, event, field) and temporal or spatial adjacency. *Fail* if a random
   split is used on grouped, spatial or time-series data without justification.
4. **Feature-provenance check.** For every feature that dominates the importance
   ranking, ask whether it is recorded before, and computed independently of, the
   outcome. *Fail* on any feature derived from the target, from the label-defining
   measurement, or from a period that includes the test interval.
5. **Baseline check.** Verify that a trivial baseline — the majority class, the
   mean, or a single physical variable — is reported. *Fail* if it is absent, since
   without it the reported skill cannot be placed on a scale.
6. **Shift check.** If the model is applied outside the training region or period,
   verify that a blocked or forward-chained validation is reported. *Fail* if only
   a random-split score is given for a transfer claim.

Each check has a binary outcome and can be evaluated from the methods section; a
study passing all six is not thereby correct, but a study failing any one has a
demonstrable problem that the numbers alone would not reveal.
