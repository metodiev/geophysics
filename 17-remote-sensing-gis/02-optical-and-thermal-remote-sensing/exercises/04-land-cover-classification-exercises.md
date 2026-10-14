# Exercises — 17-02-04 Land Cover Classification: Supervised and Unsupervised

Attempt these before reading the
[solutions](./04-land-cover-classification-solutions.md). The lesson is
[04 Land Cover Classification: Supervised and Unsupervised](../04-land-cover-classification.md).
All scenes and classifiers are **SYNTHETIC**.

Reference values from the lesson: class $A$–$D$ Mahalanobis separability $1.445$;
overall accuracy $0.8706$ with $\kappa = 0.8275$ at $100$ training pixels per
class; rare-class prevalence $0.0132$ with recall $0.0467$.

## ★ Foundational

**★1.** For the confusion matrix (rows = truth, columns = prediction)

$$N = \begin{pmatrix}40 & 5 & 5\\ 10 & 45 & 5\\ 0 & 10 & 80\end{pmatrix},$$

compute the per-class recall, the per-class precision, the overall accuracy
$p_o$, the chance agreement $p_e$ and Cohen's $\kappa$.

**★2.** Two classes have means $(0.30, 0.40)$ and $(0.20, 0.30)$ with a common
covariance $\mathbf{C} = \begin{pmatrix}0.0025 & 0.0005\\ 0.0005 & 0.0025\end{pmatrix}$.
Compute the Mahalanobis separability $d_M$.

**★3.** State the two quantities a quadratic classifier estimates per class in
$d$ dimensions, and write the total parameter count.

## ★★ Applied

**★★4.** Derive the two-class error rate
$P_e = \Phi(-d_M/2)$ for equal covariances and equal priors, and evaluate it for
$d_M = 2.0$.

**★★5.** Compute the parameter count per class for $d = 4$, $8$ and $12$, and the
training size needed at four samples per parameter.

**★★6.** A rare class has prevalence $0.02$ and the three common classes split the
remainder evenly. Compute the prior-induced shift $\ln(p_{\rm common}/p_{\rm
rare})$, the Mahalanobis advantage the rare class needs, and compare it with the
class separation of $1.445$. Interpret the result.

**★★7.** Explain with a numerical example why k-means is not invariant to feature
scaling: take two features with standard deviations $0.05$ and $0.50$ and describe
what the Euclidean objective does to the partition.

## ★★★ Research-oriented

**★★★8.** Redesign the assessment of the lesson's imbalance experiment so that
the rare class is reported meaningfully: state the metrics, the sampling design,
the decision threshold you would choose for a mineral-exploration application
(where missing a deposit is costly and a false positive is only expensive), and
the single number you would put in an executive summary. Justify the threshold
with a cost argument.

**★★★9.** Design a supervised classification experiment with a stated parameter
budget: choose the dimensionality, training size, validation design and accuracy
metric for a target with $1\%$ prevalence and 12 candidate bands, and state the
prediction your design implies for achievable per-class recall. A specification
that could not be executed is a failed answer.
