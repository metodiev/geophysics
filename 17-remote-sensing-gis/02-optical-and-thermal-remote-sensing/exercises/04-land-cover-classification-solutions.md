# Solutions — 17-02-04 Land Cover Classification: Supervised and Unsupervised

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All scenes and classifiers are **SYNTHETIC**.

Lesson: [04 Land Cover Classification: Supervised and Unsupervised](../04-land-cover-classification.md).

---

## ★1 — Confusion matrix, accuracy and kappa

$$N = \begin{pmatrix}40 & 5 & 5\\ 10 & 45 & 5\\ 0 & 10 & 80\end{pmatrix},
\qquad n = 200 .$$

**Recall** (rows): $40/50 = 0.800$, $45/60 = 0.750$, $80/90 = 0.889$.
**Precision** (columns): $40/50 = 0.800$, $45/60 = 0.750$, $80/90 = 0.889$.

The symmetry is a coincidence of the chosen row and column sums, not a property.

$$p_o = \frac{40+45+80}{200} = \frac{165}{200} = 0.825,$$
$$p_e = \frac{50\times50 + 60\times60 + 90\times90}{200^{2}}
= \frac{2500+3600+8100}{40000} = \frac{14200}{40000} = 0.355,$$
$$\kappa = \frac{p_o-p_e}{1-p_e} = \frac{0.825-0.355}{1-0.355}
= \frac{0.470}{0.645} = 0.7287 .$$

**Interpretation.** $82.5\%$ of pixels are correct, but a classifier with the same
marginals would be $35.5\%$ correct by chance, so the skill above chance is
$72.9\%$ of the available headroom. Reporting only $0.825$ overstates the
information; reporting only $\kappa$ hides the absolute error rate. Report both.

---

## ★2 — Mahalanobis separability

$$\Delta = \boldsymbol\mu_1-\boldsymbol\mu_2 = (0.10, 0.10)^{\!\top},$$
$$\det\mathbf{C} = 0.0025^{2}-0.0005^{2} = 6.25\times10^{-6}-2.5\times10^{-7}
= 6.00\times10^{-6},$$
$$\mathbf{C}^{-1} = \frac{1}{6.00\times10^{-6}}
\begin{pmatrix}0.0025 & -0.0005\\ -0.0005 & 0.0025\end{pmatrix}
= \begin{pmatrix}416.67 & -83.33\\ -83.33 & 416.67\end{pmatrix},$$
$$d_M^{2} = \Delta^{\!\top}\mathbf{C}^{-1}\Delta
= 0.10^{2}\left(416.67 - 83.33 - 83.33 + 416.67\right)
= 0.01\times666.68 = 6.6668,$$
$$d_M = \sqrt{6.6668} = 2.582 .$$

Note how the correlation reduces the effective distance: had $\mathbf{C}$ been
isotropic with variance $0.0025$, $d_M$ would be
$\sqrt{(0.10^{2}+0.10^{2})/0.0025} = \sqrt{8} = 2.828$. Correlation between the
features "hides" part of the separation that the marginal distributions appear to
show.

---

## ★3 — Quadratic classifier parameters

Per class: a mean vector ($d$ parameters) and a covariance matrix
($d(d+1)/2$ distinct entries; a symmetric $d\times d$ matrix has $d$ diagonal and
$d(d-1)/2$ off-diagonal entries, i.e. $d + d(d-1)/2 = d(d+1)/2$). Total per class:

$$n_{\rm params} = d + \frac{d(d+1)}{2} = \frac{d(d+3)}{2}.$$

For $K$ classes: $K\,d(d+3)/2$ (plus $K-1$ free priors, which sum to one).

---

## ★4 — Two-class error rate

For two classes with means $\boldsymbol\mu_1,\boldsymbol\mu_2$ and equal covariance
$\mathbf{C}$ and equal priors, the discriminant is a linear function and the
optimal boundary is the set of points equidistant in Mahalanobis metric. Project
onto the discriminant axis $\mathbf{w} = \mathbf{C}^{-1}(\boldsymbol\mu_1-
\boldsymbol\mu_2)$. Each class projects to a one-dimensional Gaussian whose means
are separated by $d_M$ and whose common standard deviation is $1$ (by construction
of the Mahalanobis metric). The boundary sits at the midpoint, so each class loses
the tail beyond $d_M/2$:

$$P_e = \Pr\left(z < -\frac{d_M}{2}\right) = \Phi\!\left(-\frac{d_M}{2}\right).$$

For $d_M = 2.0$: $P_e = \Phi(-1) = 0.1587$, i.e. **about $16\%$ of the two classes
are confused**.

Consequence for the lesson: the $1.445$-separability pair predicts
$\Phi(-0.7225) = 0.235$ error for those two classes, which explains the observed
recalls ($0.690$, $0.802$) without invoking any algorithmic deficiency.

---

## ★5 — Parameters and training size

$$n_{\rm params} = d + \frac{d(d+1)}{2}
\qquad\text{and}\qquad n_{\rm train} = 4\,n_{\rm params}.$$

| $d$ | $n_{\rm params}$ | training size at 4 samples/parameter |
|---|---|---|
| 4 | $4+10 = 14$ | 56 |
| 8 | $8+36 = 44$ | 176 |
| 12 | $12+78 = 90$ | 360 |

For a 12-band scene with, say, 6 classes, the total parameter count is
$6\times90 = 540$ (plus priors), so an adequate training set is of order
$2$–$4\times10^{3}$ labelled pixels — and that is *before* any per-class
complication such as the rare class of ★6, which needs a minimum absolute count
independent of the aggregate budget.

---

## ★6 — Prior-induced shift for a rare class

Common classes share $1-0.02 = 0.98$ evenly, so $p_{\rm common} = 0.98/3 = 0.3267$.

$$\ln\frac{p_{\rm common}}{p_{\rm rare}} = \ln\frac{0.3267}{0.02} = \ln 16.33 = 2.793 .$$

The boundary shift (for equal covariances, from the lesson's Section 3.7) requires

$$\sqrt{2\times2.793} = 2.364$$

of Mahalanobis advantage for a pixel to be labelled rare. The actual class
separation is $1.445 < 2.364$. Quantitatively, the discriminant difference is

$$g_A - g_D = \frac{d_A^{2} - d_D^{2}}{2} - \ln\frac{p_A}{p_D},$$

and the largest value the first term can take in favour of $D$ is
$d_M^{2}/2 = 1.445^{2}/2 = 1.044$, which is **less than the prior term $2.793$**.
So $g_A > g_D$ everywhere: even a pixel lying exactly at the rare class's mean
satisfies $d_A^{2}/2 = 1.044 < 2.793$ and is classified as common.

**Interpretation.** With a rare class, the *default* maximum-posterior decision
does not merely perform poorly; it can refuse the class outright. This is the
mechanism behind the lesson's measured rare-class recall of $0.0467$, and it is
why detection needs an explicit decision rule — a cost-weighted threshold, or a
detection statistic such as a matched filter at a stated false-alarm rate — rather
than a "better" classifier.

---

## ★7 — Why k-means is scale-dependent

Feature 1 has standard deviation $0.05$, feature 2 has $0.50$ — a factor of ten.
k-means minimises

$$J = \sum_j\sum_{\mathbf{x}\in\mathcal{C}_j}
\left\|\mathbf{x}-\boldsymbol m_j\right\|^{2}
= \sum_j\sum_{\mathbf{x}\in\mathcal{C}_j}
\left[\left(x_1-m_{j1}\right)^{2} + \left(x_2-m_{j2}\right)^{2}\right].$$

A difference of $0.5$ in feature 2 contributes the same $0.25$ to $J$ as a
difference of $0.5$ in feature 1 — but $0.5$ is ten standard deviations of feature
1 and only one of feature 2. **The objective's "distance" is measured in the
units of the data, so the feature with the larger variance dominates the
partition**: clustering a scene in these raw units effectively ignores feature 1.

Standardising each feature to unit variance before clustering removes the
arbitrary unit weighting, but it is itself a modelling choice (it imposes equal
importance on each feature, which may not be the physical importance). Either way,
the choice must be stated, and the result re-checked under the alternative —
because the partition is expected to change. This is in contrast to the Gaussian
classifier of Sections 3.1–3.3, which is invariant to rescaling features, since
the covariance matrix in the discriminant absorbs the scaling exactly.

---

## ★8 — Assessing a rare class in a mineral-exploration setting

**Metrics.** Report, for the target class: the confusion matrix restricted to the
target versus everything else (a $2\times2$ table), the **recall** (proportion of
true target pixels detected), the **precision** (proportion of detections that are
true), the **false-alarm rate** (false positives per unit area, which is what an
exploration team converts into follow-up cost), and the **area under the ROC or
precision–recall curve**, which summarises the threshold trade-off independently
of the operating point. Do **not** report overall accuracy or $\kappa$ as the
headline: as the lesson shows, a $98.67\%$ accurate map detected $4.7\%$ of the
target.

**Sampling design.** Stratified sampling with a **minimum** number of target
pixels (at least a few hundred, and enough that the recall's confidence interval
is useful: with $150$ target test pixels a recall of $0.5$ has a $95\%$ interval of
about $\pm0.08$). Target pixels are usually rare in the scene, so they must be
deliberately over-sampled for validation and the over-sampling reported; the
*classifier* may still use area-proportional priors, but the *assessment* must be
stratified. Spatially disjoint blocks, not random pixels, to avoid
autocorrelation inflating the score.

**Decision threshold from cost.** Let $C_{\rm FN}$ be the cost of missing a target
pixel (a missed deposit, weighted by the area of the missed anomaly) and
$C_{\rm FP}$ the cost of a false positive (a follow-up field visit). The expected
cost of threshold $\theta$ is

$$E[C(\theta)] = C_{\rm FN}N_{\rm FN}(\theta) + C_{\rm FP}N_{\rm FP}(\theta).$$

Minimising it gives a threshold at the point where the *marginal* trade equals the
cost ratio, i.e. where

$$\frac{\mathrm{d}N_{\rm FN}}{\mathrm{d}\theta} = \frac{C_{\rm FP}}{C_{\rm FN}}
\frac{\mathrm{d}N_{\rm FP}}{\mathrm{d}\theta}.$$

Since $C_{\rm FN} \gg C_{\rm FP}$ in exploration (a missed deposit costs orders of
magnitude more than a site visit), the optimal rule is deliberately
**recall-oriented**: flag widely, accept many false positives, and let the
follow-up programme filter them. That is a decision about money and risk, and it
must be documented as such — the classifier does not make it.

**Headline number for an executive summary.** The honest single number is
**recall at the chosen operating point, together with the false-alarm rate** —
e.g. "detects $70\%$ of known targets at a false-alarm rate of $1$ pixel in
$200$" — because it is the pair that determines the follow-up workload. A single
accuracy figure is not a summary of this system; it is a summary of a different
(and irrelevant) question.

---

## ★9 — Designing the experiment

**Target and prevalence.** A class at $1\%$ prevalence, $12$ candidate bands.

**Dimensionality.** Do **not** use all 12 bands. With a quadratic classifier the
parameter count per class is $d + d(d+1)/2$: $12+78 = 90$ per class, which for, say,
4 classes is $360$ parameters plus priors, and for a rare class the *absolute*
target training count dominates anyway. Instead: (i) reduce with a *supervised*
transform (e.g. Fisher/linear discriminant directions, or select bands whose
class-conditional means differ most), justified by cross-validated accuracy; (ii)
target $d \le 6$, giving $d + d(d+1)/2 \le 27$ parameters per class, which is
comfortably below a target-class training count of a few hundred.

**Training size.** At $4$ samples per parameter and $27$ parameters, $108$ target
training pixels are the statistical minimum; take at least $300$ to make the
covariance estimate stable and to allow a held-out validation block. Common
classes can use the same absolute count (stratified training), but the priors
used at decision time must be set from the *scene* prevalence ($0.01$ for the
target), not from the stratified training set — the lesson's Section 3.7 shows the
difference is worth an order of magnitude in recall.

**Validation design.** Spatially blocked, preferably leave-one-region-out so that
each fold's test pixels come from a spatially independent area; random pixel
splitting leaks information through autocorrelation. Stratified so that every fold
contains target pixels. Report the confusion matrix per fold, not only the mean,
to expose fold-to-fold variability.

**Accuracy metric.** Per-class recall and precision for the target at a stated
operating point, plus the precision–recall curve's area; balanced accuracy
$\frac{1}{K}\sum_k\text{recall}_k$ as a secondary summary; overall accuracy and
$\kappa$ reported for completeness only, with the prevalence stated.

**Predicted achievable recall.** From the geometry, if the target's Mahalanobis
separation from its nearest common class is $d_M$, the equal-cost operating point
gives $P_e = \Phi(-d_M/2)$ for that pair. With a recall-oriented threshold
(justified by the cost argument of ★8) one can push recall well above $1-P_e$ at
the price of precision; the *bound* on recall at any threshold is set by the
overlap, so the design should state the achievable range, e.g. "$d_M = 2$ gives
$\Phi(-1) = 15.9\%$ base confusion, so at a threshold chosen for $80\%$ precision
the expected recall is of order $0.5$–$0.7$, and no threshold exceeds
$1-P_{\rm overlap, target} = 0.84$". A design that predicts a recall above the
overlap bound has mis-specified its geometry and will not deliver it.
