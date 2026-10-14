# Solutions — 21-06-04 Facies and Lithology Prediction from Well Logs

> Read after attempting. Lesson:
> [04 Facies and Lithology](../04-facies-and-lithology.md). Numbers are
> **SYNTHETIC**, printed by
> [`code/facies_and_lithology_demo.py`](../code/facies_and_lithology_demo.py).

---

## ★1 — Decomposing the reported accuracy

Predicting shale everywhere scores exactly the shale share of the interval:
**0.892**.

Weighted sum over classes, $\sum_k \text{share}_k \times \text{recall}_k$:

| Class | share | centroid recall | contribution | tree recall | contribution |
|---|---|---|---|---|---|
| sand | 0.089 | 0.608 | 0.05411 | 0.597 | 0.05313 |
| shale | 0.892 | 0.995 | 0.88754 | 0.986 | 0.87951 |
| carbonate | 0.019 | 1.000 | 0.01900 | 0.975 | 0.01853 |
| **total** | 1.000 | | **0.96065** | | **0.95117** |

Both reproduce the printed values 0.961 and 0.951 to three decimals, which
confirms that the printed accuracy is the class-weighted recall and nothing
else. The constant-prediction baseline (0.892) is within 0.07 of a model that
gets the sand class 60% right — that is the whole problem with the headline
number.

---

## ★2 — Macro-average recall

$$\text{centroid: } \frac{0.608 + 0.995 + 1.000}{3} = 0.868, \qquad
\text{tree: } \frac{0.597 + 0.986 + 0.975}{3} = 0.853 .$$

Both macro values sit about $0.09$–$0.10$ *below* the corresponding overall
accuracy, and the gap is the imbalance penalty: the majority class props up the
weighted number. A shale-dominated appraisal well is judged on the macro value
(or on the minority-class recall directly), because the decision it supports —
where to place a completion, whether a reservoir is present — concerns the
minority class. Reporting only accuracy here means reporting 0.961 for a model
that misses 40% of the sand.

---

## ★3 — Drift in units of the noise

| Log | drift | noise (1 s.d.) | drift in $\sigma$ |
|---|---|---|---|
| GR | $20$ API | $10.0$ API | $2.0$ |
| RHOB | $0.16$ g/cm³ | $0.050$ g/cm³ | $3.2$ |
| NPHI | $0.08$ v/v | $0.040$ v/v | $2.0$ |

A drift of 2–3$\sigma$ is a *displacement of the class mean*, not scatter around
it: it moves the decision boundary relative to the data and produces a
misclassification with a definite sign in the shifted interval. Noise of the
same size is zero-mean, so it averages out over a bed and over a well; the drift
does not, and adding data from the shallow interval cannot correct it.

---

## ★4 — From the Gaussian discriminant to the prior shift

**Discriminant.** For class $k$ with mean $\mu_k$ and shared covariance
$\Sigma$,

$$\delta_k(x) = -\tfrac{1}{2}(x-\mu_k)^{\mathsf T}\Sigma^{-1}(x-\mu_k)
+ \ln \pi_k .$$

For equal $\Sigma$ the quadratic terms in $x$ cancel between classes, leaving a
linear rule:

$$\delta_k(x) = x^{\mathsf T}\Sigma^{-1}\mu_k
- \tfrac{1}{2}\mu_k^{\mathsf T}\Sigma^{-1}\mu_k + \ln \pi_k .$$

With $\Sigma = \sigma^2 I$ and equal priors this is
$-\frac{1}{2\sigma^2}\lVert x - \mu_k\rVert^2$ up to a constant, i.e. exactly the
**nearest-centroid** rule used in the demonstration.

**Prior shift.** Comparing sand ($s$) against shale ($h$), sand is chosen when

$$\lVert x-\mu_h\rVert^2 - \lVert x-\mu_s\rVert^2
> 2\sigma^2 \ln\!\left(\frac{\pi_s}{\pi_h}\right),
\qquad
\ln\!\left(\frac{0.392}{0.089}\right) = \ln 4.404 = 1.482 ,$$

so $2\sigma^2 \times (-1.482)$: the *shale* centroid is favoured by
$-2.96\sigma^2$, equivalently the sand must be

$$\sqrt{2.96} = 1.72\ \sigma$$

closer to the sand centroid than to the shale centroid before it is predicted.
That is the quantitative meaning of "the rule inherits its training prior": a
1.7$\sigma$ handicap imposed by the interval's class proportions rather than by
any measurement.

---

## ★5 — Depth as a feature

**Design.** Two feature sets — (A) GR, RHOB, NPHI; (B) GR, RHOB, NPHI, depth —
crossed with two splits — shuffled samples and the depth split — with the same
folds, model family and seed for every cell.

**Metric.** Overall accuracy *and* per-class recall, plus the predicted class
proportions (sum of predicted labels), so that a prior effect can be separated
from an improved class boundary.

**Expected directions.**

- *Shuffled split:* accuracy rises, often by several points, because depth
  encodes the local class proportions: the model can learn "deep $\Rightarrow$
  shale" without any log information. The per-class recall of the minority class
  may *fall* even as accuracy rises, which is the tell.
- *Depth split:* no improvement, and usually a degradation: the test interval's
  depths lie beyond every depth threshold the model fitted, so the depth term is
  extrapolation, not information.

**Confound.** The shuffled-split gain mixes (i) a genuine improvement in the log
response model — the sand response really does move with depth — with (ii) a
class-prior shortcut. Only the first is desirable.

**Controls.** (1) Report the predicted class proportions; if sand predictions
collapse while accuracy rises, the model is exploiting the prior. (2) Replace
raw depth with a within-zone depth or a depth-normalised log, which removes the
shortcut while keeping the drift correction. (3) Shuffle the depth column among
test samples as a null test: if performance collapses to the feature-set-A
level, the depth information was prior, not response.

---

## ★6 — Effective sample size of a shuffled split

Mean bed length $= 3000 / 254 = 11.8$ samples, so a 900-sample test set contains
approximately

$$\frac{900}{11.8} \approx 76\ \text{independent beds}.$$

Binomial standard errors at $p = 0.95$:

$$\text{sample count: } \sqrt{\frac{0.95 \times 0.05}{900}} = 0.00726, \qquad
\text{bed count: } \sqrt{\frac{0.95 \times 0.05}{76}} = 0.0250 .$$

The naive interval is **$3.4\times$ too narrow**. This is why the demonstration's
three splits gave the same accuracy to two decimals: differences of 0.002–0.009
sit far inside a $\pm0.025$ interval once the samples are counted as beds. Two
models "differing by 0.008" at this well are indistinguishable, and the correct
comparison is paired over beds, not over samples.

---

## ★★★7 — Does the model transfer to a new well?

**Strata.** Report every metric within: the well; the depth or stratigraphic
interval; the log suite and tool vintage; and the class. A class present in the
new well but absent or rare in training must be reported separately, because its
recall will be near zero and the average will hide it.

**Metrics.** Per-class recall and the full confusion matrix (rows = reference,
columns = predicted); the predicted class proportions; and interval-level
precision and recall when the decision is geometric. Alongside them, the
*inter-logger agreement* of the reference labels, measured by double description
of a subset: it is the floor below which no model can be measured.

**Split.** Well-disjoint: train on some wells, test on the held-out well, with
time/depth honesty inside each. Then repeat with the held-out well's *scheme*
translated to the training scheme by a geologist before scoring, otherwise the
transfer test measures scheme mismatch rather than model performance.

**Reference labels.** Core descriptions by two independent loggers on a subset,
with disagreement reported; and a statement of the depth-matching procedure and
its own uncertainty.

**Deployment-blocking result.** A class whose recall falls below the level the
decision requires while carrying a material share of the interval — for example
sand recall of 0.60 on a well where sand is the target. Also blocking: a
systematic shift of predicted proportions that reveals a prior transfer problem,
or a disagreement with the logger floor that is not explained by label noise.

**What it cannot establish.** It cannot establish performance in another basin,
with another tool vendor, or under a different description scheme; and it cannot
separate a genuine physical drift from a change in how the new well was logged
unless both are measured independently.

---

## ★★★8 — A class that does not appear in training

**Prediction.** The classifier has no centroid for the missing class, so every
sample of it is assigned to whichever existing class is nearest in feature
space. Which class that is depends on the log responses: a carbonate absent from
training will typically be absorbed by sand or shale. The missing class's recall
is therefore **0.000**, and if the confusion matrix is built from the *predicted*
labels it may not even show a row for it — the failure is entirely silent.

**Quantification.** If the missing class is 8% of the target interval, the
reported overall accuracy drops by at most a few points, and the class-proportion
report shows a compensating surplus in whichever class absorbed it. Those two
signatures — an empty recall for a described class and a surplus elsewhere — are
the detection.

**Diagnostic.**

1. Build the confusion matrix over the *union* of the two schemes, so the
   unrepresented class appears as a row with zero correct entries.
2. Monitor the distance from each sample to the nearest class centroid (or the
   maximum discriminant value). Samples of an unrepresented class sit
   systematically further away; a threshold on that distance turns the failure
   into a measurable out-of-distribution signal.
3. Compare the class inventory of the core description with the training label
   inventory *before* training.

**Modelling change.** Add an explicit reject/unknown class: assign samples whose
nearest-centroid distance exceeds a threshold to "unknown", report the rejected
fraction, and treat the threshold as an operating point (with its own
false-reject rate on known classes). Alternatively, re-label the training wells
under the union scheme so the missing class gets support.

---

## ★★★9 — Interval-level evaluation

**Definitions.** A *predicted interval* is a maximal run of contiguous samples
labelled sand; a *true bed* is a maximal run in the reference series. A
predicted interval $P$ is matched to a true bed $T$ if
$\lvert P \cap T\rvert \ge 0.5\lvert P\rvert$; require the symmetric condition
$\lvert P \cap T\rvert \ge 0.5\lvert T\rvert$ as well when merging is as
important as fragmenting. Then

$$\text{precision}_{\text{int}} = \frac{\#\text{matched predicted intervals}}
{\#\text{predicted intervals}}, \qquad
\text{recall}_{\text{int}} = \frac{\#\text{matched true beds}}
{\#\text{true beds}} .$$

**Why they differ from the sample-level versions.** The sample-level metrics
count *volume*; the interval-level ones count *objects*. A fragmented prediction
that labels half of every bed correctly can score 0.5 at sample level but has a
precision of roughly $1/(\text{fragments per bed})$, because each fragment is a
separate unmatched interval. A smoothed prediction that merges two beds scores
well at sample level and loses one bed of recall. Downstream decisions —
perforation intervals, flow-unit definition, seismic tie points — concern
objects, so the interval-level numbers are the ones that match the decision.

**Sizing.** With $p \approx 0.6$ at interval level, a half-width of $0.05$ at
three standard errors needs

$$n \ge \frac{p(1-p)}{(0.05/3)^2} = \frac{0.24}{2.78\times10^{-4}} \approx 864
\ \text{true beds}.$$

An interval 300 m thick with 254 beds has only tens of sand beds, so a single
well cannot resolve the comparison. Either state a coarser resolution
(0.10 half-width needs about 216 beds) or pool many wells, and in either case
resample *beds*, not samples, in the bootstrap so that the fragmentation
correlation is carried into the interval.
