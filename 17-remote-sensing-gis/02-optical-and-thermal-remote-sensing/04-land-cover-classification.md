---
id: 17-02-04
title: "Land Cover Classification: Supervised and Unsupervised"
level: advanced
prereqs: ["17-02-01", "21-04-03", "21-04-08"]
tags: [remote-sensing, gis, classification, maximum-likelihood, k-means, accuracy-assessment]
---

# Land Cover Classification: Supervised and Unsupervised

Classification turns a reflectance measurement into a label. It is the step where
remote sensing most often substitutes a number for a judgement, and it is
therefore the step that most needs its error stated. This lesson builds the two
standard families — **supervised** Gaussian maximum-likelihood classification and
**unsupervised** k-means clustering — derives what each actually optimises, and
then measures the three ways a classification result misleads.

The failures are quantitative and all are demonstrated on the same synthetic
four-class scene:

- **A single accuracy number hides the error.** The demonstration's classifier
  reaches an overall accuracy of $0.8706$ ($\kappa = 0.8275$), and *all* of the
  error is in one pair of classes: recall $0.690$ for the bright-soil class and
  $0.802$ for the spectrally similar altered-rock class, against $0.990$ and
  $1.000$ for the other two. The map is good except exactly where the
  discrimination is physically hard.
- **More dimensions can make it worse.** Adding features that carry *no* class
  information degrades accuracy monotonically once the parameter count outruns
  the training set: $0.8521$ with two features, $0.8578$ with three, and
  $0.6625$ with sixteen at a fixed $20$ training pixels per class. This is the
  **Hughes phenomenon**, and it follows from arithmetic: a $d$-dimensional
  quadratic classifier estimates $d + d(d+1)/2$ parameters per class, which is
  $152$ at $d = 16$ against $20$ samples.
- **Imbalance makes a useless map look accurate.** With one class at $1.32\%$
  prevalence, the overall accuracy is $0.9867$ while that class's recall is
  $0.0467$: the classifier misses $95\%$ of the very class the study was about.

A fourth result is specific to the unsupervised side: k-means minimises a
non-convex objective, so its answer depends on the initialisation. The
demonstration's agreement with the true labels is $0.8655$ for four of five seeds
and $0.6255$ for the fifth — a spread of $0.2405$ produced entirely by where the
algorithm started.

All models and data in this module are **SYNTHETIC**. The class means,
covariances, proportions and dimensionality are chosen teaching values in
`code/land_cover_classification_demo.py`. No real scene, land-cover product,
sensor or training dataset is represented, and no classifier library is used: the
Gaussian discriminant and k-means are implemented in the demonstration so that
every quantity can be traced.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the quadratic Gaussian discriminant from the class-conditional
   likelihood and the prior, and **explain** the role of each term.
2. **Define** and compute a confusion matrix, per-class recall and precision,
   overall accuracy and Cohen's $\kappa$.
3. **Compute** a Mahalanobis separability between two classes and **convert** it
   to a two-class error rate.
4. **Quantify** how classification accuracy depends on training-sample size, and
   **state** where the marginal value of more training data lies.
5. **Explain and quantify** the Hughes phenomenon from the parameter count
   $d + d(d+1)/2$ per class.
6. **Describe** the k-means objective, its two alternating steps, and why its
   result depends on the initialisation.
7. **Demonstrate** with numbers why overall accuracy is insufficient under class
   imbalance, and **report** the assessment that is.

## Prerequisites

- [17-02-01 Multispectral Imaging, Band Ratios and Indices](01-multispectral-imaging.md)
  — the band features a classifier is built from.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md)
  — the general treatment of splitting, metrics and leakage.
- [21-04-08 Clustering and Unsupervised Structure Discovery](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/08-clustering.md)
  — the general treatment of clustering objectives and their non-convexity.

---

## 1. Intuition: labelling a continuum

Reflectance is continuous and labels are discrete, so classification draws
boundaries through a continuous feature space. Two things follow immediately.

**Where you draw the boundary depends on how much training data you have and what
class proportions you assume.** A boundary that is optimal for equal priors is not
optimal for a rare class, and the difference is not a detail: it is the
difference between a $95\%$ miss rate and a usable map.

**Accuracy is a property of the boundary, not of the physics.** The demonstration's
hard pair (bright soil versus altered rock) has a Mahalanobis separability of only
$1.445$ while every other pair exceeds $4.6$. No classifier will fix that: the
information is not in the two bands. The honest response is either more bands,
more context, or a reported error map — not a larger training set, which
saturates at $0.879$ overall accuracy by $250$ pixels per class.

The unsupervised side has a different character. k-means makes no use of labels,
so its output is a *partition of the data density*, not a map of materials. When
the density structure happens to match the classes, agreement is high
($0.8655$ here); when the initialisation lands in a different local optimum, it is
not ($0.6255$). **Agreement with truth is not accuracy**, because a clustering
answer is untethered to the labels: relabelling the clusters changes nothing
about the partition.

## 2. Precise definitions and units

| Quantity | Symbol | Definition |
|---|---|---|
| feature vector | $\mathbf{x}$ | $d$ reflectances or derived indices, dimensionless |
| class labels | $k = 1,\dots,K$ | discrete |
| class prior | $p_k$ | $\Pr(\text{class} = k)$ |
| class-conditional density | $f_k(\mathbf{x})$ | assumed Gaussian, with mean $\boldsymbol\mu_k$, covariance $\mathbf{C}_k$ |
| discriminant | $g_k(\mathbf{x})$ | $\ln[p_k f_k(\mathbf{x})]$; classify to $\arg\max_k g_k$ |
| confusion matrix | $\mathbf{N}$ | $N_{tk}$ = count of truth $t$ classified as $k$ |
| recall (producer's accuracy) | — | $N_{kk}/\sum_k N_{tk}$ |
| precision (user's accuracy) | — | $N_{kk}/\sum_t N_{tk}$ |
| overall accuracy | $p_o$ | $\sum_k N_{kk}/\sum N$ |
| chance agreement | $p_e$ | $\sum_k\left(\sum_tN_{tk}\right)\left(\sum_tN_{kt}\right)/n^2$ |
| Cohen's $\kappa$ | — | $(p_o-p_e)/(1-p_e)$ |
| Mahalanobis separability | $d_M$ | $\sqrt{\Delta^{\!\top}\mathbf{C}^{-1}\Delta}$ |

A note on what $\kappa$ means. It compares the classifier's agreement with chance
agreement computed from the *marginals of the confusion matrix*. It is therefore
not a measure of physical correctness, and it is not comparable between studies
with different class schemes — a two-class and a ten-class map can have the same
$\kappa$ and completely different information content.

## 3. Derivations

### 3.1 The quadratic Gaussian discriminant

Assume $\mathbf{x}\mid k \sim \mathcal{N}(\boldsymbol\mu_k,\mathbf{C}_k)$:

$$f_k(\mathbf{x}) = \frac{1}{(2\pi)^{d/2}|\mathbf{C}_k|^{1/2}}
\exp\left[-\tfrac{1}{2}(\mathbf{x}-\boldsymbol\mu_k)^{\!\top}
\mathbf{C}_k^{-1}(\mathbf{x}-\boldsymbol\mu_k)\right].$$

The Bayes rule assigns the class maximising the posterior
$p_kf_k(\mathbf{x})/\sum_jp_jf_j(\mathbf{x})$; because the denominator is common,
the decision is

$$\boxed{\;g_k(\mathbf{x}) = -\tfrac{1}{2}(\mathbf{x}-\boldsymbol\mu_k)^{\!\top}
\mathbf{C}_k^{-1}(\mathbf{x}-\boldsymbol\mu_k)
-\tfrac{1}{2}\ln|\mathbf{C}_k| + \ln p_k\;}$$

and we choose $\hat k = \arg\max_kg_k$. The first term is the squared Mahalanobis
distance to the class mean (a quadratic in $\mathbf{x}$ — hence "quadratic
discriminant analysis", QDA); the second penalises classes with a larger
covariance volume; the third is the prior. If all $\mathbf{C}_k$ were equal, the
second term would drop out and the boundaries would be hyperplanes (linear
discriminant analysis, LDA).

*Numerical check.* In the demonstration, with $100$ training pixels per class, the
estimated means are
$\boldsymbol\mu_A = (0.3663, 0.4197)$,
$\boldsymbol\mu_B = (0.1154, 0.4502)$,
$\boldsymbol\mu_C = (0.0576, 0.0304)$,
$\boldsymbol\mu_D = (0.3315, 0.3470)$ — each within about $0.01$ of the true
generating mean. The expected per-component sampling error is
$\sigma/\sqrt{n} = 0.055/10 = 0.0055$, so the largest deviation
($-0.0098$ on the second component of the vegetation-like class) is about
$1.8$ standard errors — ordinary, not a sign of a problem.

### 3.2 Separability and the two-class error rate

For two classes with a common covariance $\mathbf{C}$, the optimal boundary is at
the midpoint and the probability of error is

$$P_e = \Phi\!\left(-\frac{d_M}{2}\right),
\qquad
d_M = \sqrt{\left(\boldsymbol\mu_1-\boldsymbol\mu_2\right)^{\!\top}
\mathbf{C}^{-1}\left(\boldsymbol\mu_1-\boldsymbol\mu_2\right)},$$

where $\Phi$ is the standard normal CDF.

*Numerical check.* The demonstration's class pairs have

| pair | $d_M$ | $P_e$ (equal covariance, equal priors) |
|---|---|---|
| 0–1 | 5.130 | $5.16\times10^{-3}$ |
| 0–2 | 9.974 | $3.07\times10^{-7}$ |
| 0–3 | 1.445 | $0.235$ |
| 1–2 | 10.118 | $2.11\times10^{-7}$ |
| 1–3 | 4.673 | $9.73\times10^{-3}$ |
| 2–3 | 10.041 | $2.58\times10^{-7}$ |

The $0$–$3$ pair alone predicts a $23.5\%$ error rate for those two classes,
which accounts for the observed recalls $0.690$ and $0.802$: **the classifier is
performing exactly as the geometry allows.** This is the single most useful
diagnostic in the lesson, because it distinguishes a classifier problem from an
information problem.

### 3.3 Confusion matrix, accuracy and $\kappa$

For a $K\times K$ confusion matrix with entries $N_{tk}$,

$$p_o = \frac{\sum_kN_{kk}}{n},
\qquad
p_e = \frac{1}{n^{2}}\sum_k\left(\sum_tN_{tk}\right)
\left(\sum_tN_{kt}\right),
\qquad
\kappa = \frac{p_o-p_e}{1-p_e}.$$

$p_e$ is the agreement two classifiers would reach if each assigned labels
independently with the observed marginals. $\kappa = 0$ means "no better than
chance", $\kappa = 1$ means "perfect".

*Numerical check.* The demonstration's matrix at $100$ training pixels per class:

| truth $\backslash$ pred | 0 | 1 | 2 | 3 | recall |
|---|---|---|---|---|---|
| 0 (bright soil) | 276 | 2 | 0 | 122 | 0.690 |
| 1 (vegetation) | 4 | 396 | 0 | 0 | 0.990 |
| 2 (water) | 0 | 0 | 400 | 0 | 1.000 |
| 3 (altered rock) | 79 | 0 | 0 | 321 | 0.802 |
| **precision** | 0.769 | 0.995 | 1.000 | 0.725 | |

$$p_o = \frac{276+396+400+321}{1600} = 0.8706,\qquad
p_e = 0.25,\qquad
\kappa = \frac{0.8706-0.25}{1-0.25} = 0.8275 .$$

$p_e = 0.25$ exactly because the test set is balanced and the predicted marginals
are nearly equal. Note that the *precision* of classes 0 and 3 ($0.769$, $0.725$)
is much worse than their recall: the classifier both misses them and confuses them
with each other, which a single accuracy number conceals completely.

### 3.4 Training-sample size and its saturation

Parameter estimation error falls as $n^{-1/2}$ per parameter, so accuracy improves
with training size and saturates when the estimation error falls below the
irreducible Bayes error from class overlap. The demonstration:

| training pixels/class | overall accuracy | $\kappa$ | recall of the 0–3 pair |
|---|---|---|---|
| 2 | 0.1973 | $-0.0703$ | 0.000 |
| 3 | 0.5448 | 0.3930 | 0.462 |
| 5 | 0.7444 | 0.6593 | 0.671 |
| 10 | 0.8276 | 0.7701 | 0.665 |
| 20 | 0.8635 | 0.8181 | 0.747 |
| 50 | 0.8650 | 0.8200 | 0.732 |
| 100 | 0.8750 | 0.8333 | 0.751 |
| 250 | 0.8790 | 0.8387 | 0.760 |

Two features of this table matter. First, at two or three pixels per class the
covariance estimate is nearly singular, the classifier is dominated by its own
estimation error, and $\kappa$ is *negative* at $n = 2$ — worse than chance.
Second, from $20$ pixels per class onward almost nothing improves: the
$1.445$-separability pair caps the achievable accuracy, and the residual is
Bayes error, not estimation error. **Extra training data beyond that point buys
nothing, and no amount of it fixes the pair.**

### 3.5 The Hughes phenomenon

A $d$-dimensional quadratic classifier estimates, per class,
$d$ mean components and $d(d+1)/2$ distinct covariance entries:

$$n_{\rm params} = d + \frac{d(d+1)}{2}.$$

At fixed training size per class, increasing $d$ increases the numerator of the
estimation error without adding information. The demonstration appends pure-noise
features (standard deviation $0.055$, the same as the real classes) at a fixed 20
training pixels per class:

| $d$ | parameters/class | overall accuracy | $\kappa$ |
|---|---|---|---|
| 2 | 5 | 0.8521 | 0.8028 |
| 3 | 9 | 0.8578 | 0.8104 |
| 4 | 14 | 0.8583 | 0.8111 |
| 6 | 27 | 0.8427 | 0.7903 |
| 10 | 65 | 0.7755 | 0.7007 |
| 16 | 152 | 0.6625 | 0.5500 |

Accuracy rises slightly to $d = 4$ (the noise dimensions happen to sharpen the
estimated boundaries by chance) then collapses: at $d = 16$ there are $152$
parameters to estimate from $20$ samples, i.e. $7.6$ samples per parameter. **The
practical rule is to keep the number of training samples per class well above the
parameter count; a common heuristic of "10–30 samples per parameter" is a
statement about exactly this ratio.** Compression before classification is
therefore a supervised decision: it must be justified by held-out accuracy, not by
aesthetics.

### 3.6 k-means: objective, steps, and non-convexity

k-means minimises the within-cluster sum of squares

$$J(\{\mathcal{C}_j\},\{\boldsymbol m_j\})
= \sum_{j=1}^{K}\sum_{\mathbf{x}\in\mathcal{C}_j}
\left\|\mathbf{x}-\boldsymbol m_j\right\|^{2},
\qquad
\boldsymbol m_j = \frac{1}{|\mathcal{C}_j|}\sum_{\mathbf{x}\in\mathcal{C}_j}\mathbf{x}.$$

Lloyd's algorithm alternates two exact steps: (i) assign each point to its nearest
centre (minimises $J$ over the partition), and (ii) move each centre to its
cluster mean (minimises $J$ over the centres). Each step cannot increase $J$, so
$J$ decreases monotonically and the algorithm converges — but $J$ is **non-convex**
in the joint variables, so it converges to a *local* optimum that depends on the
initialisation.

*Numerical check.* Over five initialisations the demonstration's agreement with
the true labels is $0.8655$, $0.6255$, $0.8655$, $0.8660$, $0.8660$: a spread of
$0.2405$. The failing seed is not a bug; it is the objective's landscape.

Two further cautions. k-means uses Euclidean distance, so it is **not invariant to
feature scaling** — a band with a larger variance dominates the partition unless
the features are standardised, and standardising changes the answer. And a
clustering is a partition: the labels are arbitrary, so agreement must be measured
after finding the best label matching, as the demonstration does.

### 3.7 The accuracy paradox and the prior

With unequal priors the discriminant's $\ln p_k$ term shifts every boundary toward
the rare class. The shift is large. For two classes with equal covariances the
boundary between classes $A$ and $D$ sits where

$$g_A(\mathbf{x}) - g_D(\mathbf{x}) = 0
\;\Longrightarrow\;
\frac{d_A^{2}}{2} - \frac{d_D^{2}}{2} = \ln\frac{p_A}{p_D} .$$

*Numerical check.* With $p_A = 0.3289$ and $p_D = 0.0132$,
$\ln(p_A/p_D) = 3.216$, so a point must be favoured by
$\sqrt{2\times3.216} = 2.54$ in Mahalanobis distance for $D$ to win. Since the
$A$–$D$ separation is only $1.445$, almost no $D$ pixels survive: the measured
recall is $0.0467$ with a precision of $0.4118$, while the overall accuracy is
$0.9867$. **A "98.7% accurate" map that finds $5\%$ of the target class is worse
than useless if the target was the point of the exercise.**

The remedy is not to remove the prior but to change what is reported: a
**per-class** table (recall, precision, $F_1$), a **balanced** accuracy
($\tfrac{1}{K}\sum_k\text{recall}_k$), and an explicitly chosen decision threshold
driven by the cost of the two error types. All three are statements about the
application, and all three belong in the documentation of the map.

## 4. Physical interpretation

- **Classification error is mostly geometry.** In this scene $23.5\%$ of the hard
  pair is expected to be confused from the class statistics alone; the classifier
  is not the limitation.
- **Accuracy saturates at Bayes error.** From 20 to 250 training pixels per class
  the overall accuracy moves from $0.8635$ to $0.8790$.
- **Dimension is a parameter-count decision.** $152$ parameters from $20$ samples
  per class is the arithmetic behind the collapse to $0.6625$.
- **Unsupervised partitions are not maps.** They describe density structure, and
  they inherit the objective's non-convexity and its dependence on scaling.
- **Assessment is part of the product.** A confusion matrix with per-class
  metrics, the sampling design, and the priors used are not administrative
  details; they determine whether the map answers the question asked.

## 5. Assumptions and regime of validity

1. **Gaussian class-conditional densities.** The quadratic discriminant is exactly
   optimal only under this assumption; real reflectance distributions are often
   skewed or multimodal, and a classifier can then be confidently wrong. Check
   with per-class histograms, and consider a non-parametric classifier if the
   assumption fails.
2. **Independent, identically distributed pixels.** Spatially autocorrelated
   training and test sets violate this; the standard fix is spatially disjoint
   blocks or a leave-one-region-out design
   ([21-04-03](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md)).
3. **A training set representative of the scene**, in *both* spectral and
   proportional terms. Section 3.7 shows the cost of getting the proportions
   wrong, and a spectrally biased training set is worse.
4. **Features on comparable scales** for k-means (Euclidean distance is
   scale-dependent) and a stated standardisation for any Euclidean-based method.
5. **Atmospheric and geometric consistency** between training and application
   data. A classifier trained on one atmosphere is a classifier for that
   atmosphere; applying it elsewhere changes the label, not the material
   ([17-01-03](../01-remote-sensing-physics/03-atmospheric-effects.md)).
6. **The class scheme is the analyst's.** Classes are definitions, not natural
   kinds; "bright soil" and "altered rock" are useful labels only relative to a
   purpose.
7. **The synthetic parameters are teaching values**, as listed above: the means,
   covariances, dimensionality, noise dimensions, training sizes and prevalence
   are parameters of the demonstration, and no external library is used to hide
   the arithmetic.

## 6. Units and dimensional analysis

| Expression | Unit arithmetic | Result |
|---|---|---|
| $g_k(\mathbf{x})$ | ($\mathrm{1/dimensionless}$)·dimensionless² | dimensionless |
| Mahalanobis $d_M$ | $(\mathrm{1}\cdot\mathrm{1})^{1/2}$ | dimensionless |
| recall, precision, $p_o$, $p_e$, $\kappa$ | counts/counts | dimensionless |
| $\ln|\mathbf{C}_k|$ | $\ln(\mathrm{1})$ | dimensionless |
| $n_{\rm params} = d + d(d+1)/2$ | counts | dimensionless |

The reflectances are dimensionless, which makes feature scaling invisible in the
algebra and consequential in practice: a classifier trained on reflectances
$\times 10^{4}$ (digital numbers) makes exactly the same decisions as one trained
on reflectances, but a **k-means** solution on the two does **not**, because the
Euclidean distance that defines its objective scales with the data. This is the
one place in the module where the unit choice changes the answer.

## 7. Worked examples

### Example 1 — is the classifier or the physics at fault?

The bright-soil and altered-rock classes in the demonstration:

1. Means $(0.360, 0.420)$ and $(0.330, 0.345)$; average covariance with
   within-class standard deviations $0.055$ and $0.055$.
2. Mahalanobis distance $d_M = 1.445$.
3. Expected two-class error rate $\Phi(-1.445/2) = \Phi(-0.7225) = 0.235$.
4. Observed recalls $0.690$ and $0.802$ imply a combined error of about $0.25$,
   slightly worse than the equal-covariance prediction because the covariance
   estimates add their own error.

Conclusion: the error is **physical**, not algorithmic. More training data will
not help (Section 3.4 plateaus at $0.879$ overall); a better answer requires
additional bands that separate the two materials, or an explicit statement that
they are not separable in this data.

### Example 2 — computing $\kappa$ by hand

From the demonstration's matrix: $n = 1600$, correct $= 276+396+400+321 = 1393$.

$$p_o = 1393/1600 = 0.8706,$$
marginals: truth $400$ per class, predictions $359, 398, 400, 443$ (columns), so

$$p_e = \frac{1}{1600^{2}}\left(400\times359 + 400\times398 + 400\times400
+ 400\times443\right) = \frac{1600\times1600}{1600^{2}} = 0.25,$$
$$\kappa = \frac{0.8706 - 0.25}{0.75} = 0.8275 .$$

$p_e = 0.25$ because the design is balanced; with an unbalanced design $p_e$
rises and $\kappa$ falls for the same $p_o$ — which is the sense in which $\kappa$
corrects accuracy for composition.

### Example 3 — the Hughes arithmetic

At $d = 16$ with 20 training pixels per class:

1. Parameters per class: $d + d(d+1)/2 = 16 + 136 = 152$.
2. Samples per parameter: $20/152 = 0.13$ — fewer than one sample per parameter.
3. Measured overall accuracy $0.6625$ against $0.8521$ at $d = 2$.

To hold the same parameter-to-sample ratio at $d = 16$ that is achieved at $d = 2$
(5 parameters from 20 samples, i.e. 4 samples per parameter) one would need
$152\times4 = 608$ training pixels per class — thirty times as many. **That is the
cost of a dimension, and it is why feature selection precedes classification.**

### Example 4 — the prior shift

Rare class $D$ at $p_D = 0.0132$, common class $A$ at $p_A = 0.3289$:

1. $\ln(p_A/p_D) = \ln(24.9) = 3.216$.
2. Required Mahalanobis advantage for $D$: $\sqrt{2\times3.216} = 2.54$.
3. Actual $A$–$D$ separation: $1.445$.
4. Consequence: measured recall $0.0467$, precision $0.4118$, overall accuracy
   $0.9867$.

The overall accuracy is dominated by the three common classes, each of which is
classified at $\ge0.99$. **The number that matters — finding the altered rock — is
the one the headline number buries.**

## 8. Python demonstration

`code/land_cover_classification_demo.py` prints, with units:

1. the four synthetic classes, their means and within-class standard deviations,
   and the six pairwise Mahalanobis separabilities from $1.445$ to $10.118$;
2. the QDA discriminant and its estimated means;
3. the confusion matrix, recalls, precisions, $p_o = 0.8706$, $p_e = 0.25$,
   $\kappa = 0.8275$;
4. accuracy versus training size, from $\kappa = -0.0703$ at 2 pixels per class to
   $0.8387$ at 250, with the hard-pair recall column;
5. the Hughes table, $0.8521$ at $d = 2$ down to $0.6625$ at $d = 16$;
6. the k-means cluster means and agreement over five seeds ($0.8655$, $0.6255$,
   $0.8655$, $0.8660$, $0.8660$);
7. the imbalance experiment: overall accuracy $0.9867$ with a rare-class recall of
   $0.0467$ and precision $0.4118$;
8. a verification of $\kappa$ by an independent recomputation and the
   majority-class baseline ($p_o^{\rm base} = 0.25$, $\kappa = 0.0000$).

Everything is generated in code; there is no file input, no network access, and no
machine-learning library.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/04-land-cover-classification-exercises.md`](./exercises/04-land-cover-classification-exercises.md)
and
[`exercises/04-land-cover-classification-solutions.md`](./exercises/04-land-cover-classification-solutions.md).

- **★** Compute recall, precision, $p_o$, $p_e$ and $\kappa$ for a stated $3\times3$
  matrix.
- **★** Compute the Mahalanobis distance for two classes given means and a shared
  covariance.
- **★★** Derive the two-class error rate and evaluate it for $d_M = 2.0$.
- **★★** Compute the parameter count per class at $d = 4, 8, 12$ and state the
  required training size for four samples per parameter.
- **★★★** Redesign the assessment of the imbalance experiment so that the rare
  class is reported meaningfully, and state the decision rule you would adopt for
  a mineral-exploration application.

## Mastery checkpoint

Without notes, for the confusion matrix
$N = \begin{pmatrix}45 & 5\\ 10 & 40\end{pmatrix}$: **(a)** compute the recall
and precision of both classes; **(b)** compute $p_o$, $p_e$ and $\kappa$;
**(c)** compute the parameter count of a quadratic classifier at $d = 6$ and the
training size needed at four samples per parameter; **(d)** state two different
reasons a $98\%$ accurate map can be useless.

## 10. Common pitfalls

1. **Reporting one accuracy number.** Here it is $0.8706$ overall with
   $0.690$/$0.802$ recall on the pair that matters.
2. **Adding features for completeness.** $152$ parameters from $20$ samples
   produced a collapse to $0.6625$.
3. **Assuming more training data always helps.** Accuracy saturates at the Bayes
   error set by class overlap.
4. **Reporting a rare-class result as a headline accuracy.** The map is $98.67\%$
   accurate and misses $95\%$ of the target class.
5. **Treating clustering as classification.** k-means optimises a non-convex
   within-cluster sum of squares and its result depends on initialisation
   (spread $0.2405$ here) and on feature scaling.
6. **Ignoring spatial autocorrelation** when splitting into training and test.
7. **Applying a classifier outside its atmospheric and geometric regime.**
8. **Using a Gaussian classifier without checking for multimodality** in the
   class distributions.

## 11. Real-world applications

- **Land-cover and land-use mapping.** The standard product, whose accuracy
  statement is the subject of this lesson.
- **Mineral exploration.** A rare target class is the norm, so the imbalance
  problem of Section 3.7 is the central practical difficulty
  ([17-08-01](../08-remote-sensing-applications-geophysics/01-mineral-mapping-rs.md)).
- **Change detection.** Two classifications differenced inherit *both* confusion
  matrices, so a $13\%$ per-map error can become a much larger change error
  ([05 Change Detection and Time-Series Analysis](05-change-detection.md)).
- **Operational monitoring and calibration.** Reported accuracies drive downstream
  decisions, which is why per-class metrics and the sampling design are part of
  the deliverable.
- **Machine-learning classification.** The same assessment logic applies to any
  classifier; the modern treatment, including cross-validation and leakage, is in
  [21-06-08 ML for Remote Sensing Classification](../../21-statistics-bayesian-ml/06-ml-in-geophysics/08-remote-sensing-ml.md).

## 12. Further reading

- *Remote Sensing and Image Interpretation* (Lillesand and Kiefer) — the classical
  supervised and unsupervised workflows.
- *Physical Principles of Remote Sensing* (Rees) — the features and their physical
  meaning.
- [21-04-03 Cross-Validation, Metrics and the Danger of
  Leakage](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md)
  — the rigorous treatment of accuracy assessment.
- [21-04-08 Clustering and Unsupervised Structure
  Discovery](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/08-clustering.md)
  — clustering objectives beyond k-means.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related modules

- [02 Hyperspectral Sensing and Spectral Unmixing](02-hyperspectral.md) — the soft
  (fractional) alternative to hard labels.
- [03 Thermal Infrared: Land Surface Temperature and Heat Flow](03-thermal-infrared.md) —
  LST as an additional classifying feature.
- [05 Change Detection and Time-Series Analysis](05-change-detection.md) — what a
  pair of classifications can and cannot reveal.
- [06 Vegetation Indices, Geobotany and Mineral Alteration Mapping](06-vegetation-and-geobotany.md) —
  the rare-class problem in its application setting.

## 14. Self-assessment checklist

- [ ] I can derive the quadratic discriminant and explain its three terms.
- [ ] I can compute a confusion matrix, recall, precision, $p_o$, $p_e$ and $\kappa$.
- [ ] I can compute a Mahalanobis separability and predict the error rate from it.
- [ ] I can state where additional training data stops helping and why.
- [ ] I can compute the parameter count of a quadratic classifier and judge the training ratio.
- [ ] I can explain why k-means results depend on initialisation and scaling.
- [ ] I can demonstrate why overall accuracy fails under class imbalance.
