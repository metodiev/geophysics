# Solutions — 21-06-08 ML for Remote Sensing Classification

> Read after attempting. Lesson:
> [08 Remote Sensing ML](../08-remote-sensing-ml.md). Numbers are **SYNTHETIC**,
> printed by [`code/remote_sensing_ml_demo.py`](../code/remote_sensing_ml_demo.py).

---

## ★1 — Reconstructing kappa

Cohen's kappa is

$$\kappa = \frac{p_o - p_e}{1 - p_e},$$

where $p_o$ is the observed agreement (the overall accuracy) and $p_e$ the
agreement expected by chance from the marginal distributions. Using the true
class shares as a proxy for the predicted shares — valid here because the
classifier's predicted proportions closely track the true ones —

$$p_e = 0.200^2 + 0.400^2 + 0.150^2 + 0.250^2
= 0.0400 + 0.1600 + 0.0225 + 0.0625 = 0.2850 ,$$

$$\kappa = \frac{0.962 - 0.285}{1 - 0.285} = \frac{0.677}{0.715} = 0.947 .$$

The printed value is $0.946$; the difference is the third decimal of the accuracy
and the small difference between the predicted and true proportions. The
reconstruction shows what kappa removes: **28.5% agreement is free**, so kappa
reports the fraction of the remaining 71.5% that the map actually gets.

---

## ★2 — The constant classifier

Predicting "forest" everywhere gives $p_o = 0.400$, the forest share. Its
predicted marginals are (0, 1, 0, 0), so

$$p_e = 0\times0.200 + 1\times0.400 + 0\times0.150 + 0\times0.250 = 0.400,$$

$$\kappa = \frac{0.400 - 0.400}{1 - 0.400} = 0 .$$

Kappa is 0 by construction for any classifier whose marginals match its
predictions — which is the property that makes it useful: it scores a
proportion-driven map at zero no matter how high its raw accuracy.

---

## ★3 — Which configuration costs more, and who pays

| configuration | $\Delta$ accuracy | $\Delta$ kappa |
|---|---|---|
| three visible bands | $0.962 - 0.748 = 0.214$ | $0.946 - 0.637 = 0.309$ |
| cropland thinned | $0.962 - 0.960 = 0.002$ | $0.003$ |
| haze on the test scene | $0.962 - 0.900 = 0.062$ | $0.946 - 0.862 = 0.084$ |

Dropping half the spectrum costs more than three times as much kappa as an
uncorrected radiometric shift. The class that pays:

- **three bands: water** (recall $1.000 \rightarrow 0.354$), because water is dark
  in every visible band and is identified mainly by near-zero NIR/SWIR
  reflectance;
- **thinning: cropland** ($0.938 \rightarrow 0.848$), the class whose training
  share fell below its true share;
- **haze: forest** ($0.944 \rightarrow 0.772$), the class whose separation from
  cropland depends on the red-to-NIR contrast that a visible-band offset
  distorts.

In each case the aggregate number understates the damage to the class that
matters, which is why the per-class table is the reportable object.

---

## ★4 — The prior's effect, expressed in reflectance

**Discriminant.** With pooled covariance $\Sigma$ and class means $\mu_k$,

$$\delta_k(x) = -\tfrac{1}{2}(x-\mu_k)^{\mathsf T}\Sigma^{-1}(x-\mu_k)
+ \ln \pi_k .$$

**The prior term.** Changing cropland's prior from $0.250$ to $0.052$ changes its
discriminant *relative to the other classes* by the additive constant

$$\Delta \ln \pi = \ln\frac{0.250}{0.052} = \ln 4.808 = 1.570 ,$$

subtracted from cropland's score. Cropland must therefore be more attractive on
spectral grounds by $1.570$ before it is predicted.

**Offsetting it in NIR.** For a diagonal covariance, a shift $\Delta$ in the NIR
value changes the difference between the cropland and forest discriminant values
by

$$\Delta \cdot \frac{\mu_{c,\mathrm{NIR}} - \mu_{f,\mathrm{NIR}}}
{\sigma_{\mathrm{NIR}}^2}
= \Delta \cdot \frac{0.05}{0.035^2} = 40.8\,\Delta .$$

Setting $40.8\,\Delta = 1.570$ gives

$$\Delta = 0.0385\ \text{reflectance} = 1.10\,\sigma_{\mathrm{NIR}} .$$

So the prior change is worth about **one standard deviation of the NIR band**. A
pixel 1.1 NIR standard deviations more vegetation-like than cropland's mean now
has to be that much greener before it is called cropland. That is the entire
mechanism behind the measured cropland deficit, and it is a modelling choice
hidden inside the training-set sampling.

---

## ★★★5 — Spatially blocked validation of a map

**Block size rule.** Estimate the spatial autocorrelation range of the spectral
bands (variogram range, or the distance at which the semivariance plateaus) and
set the validation block to at least twice that range, so that a held-out block's
pixels have no near-duplicate neighbours in training. Report the metric at two
block sizes to show the sensitivity.

**Edge effect.** When scoring a held-out block, exclude a buffer of one
correlation length at its perimeter, or accept that the boundary pixels are
partly informed by training data and report them separately. The same buffer
argument applies at the scene edge, where the blocks are incomplete.

**Metric.** The full confusion matrix per block — not a pooled matrix — because
pooling across blocks can mask a block where a class fails completely. Report
per-class recall and user's accuracy with the block as the resampling unit.

**Class-proportion uncertainty for area estimates.** The area of class $k$ is
estimated from the *proportion* of class $k$ in the scene, and that proportion is
estimated from the validation sample. Its standard error is

$$\mathrm{SE}(\hat p_k) = \sqrt{\frac{\hat p_k(1-\hat p_k)}{n_{\text{eff}}}},
\qquad n_{\text{eff}} = \text{number of independent validation units},$$

with $n_{\text{eff}}$ the number of *blocks or clusters*, not pixels (see ★6). For
a stratified design, weight each stratum by its area share and combine the
variances in the usual stratified estimator. Report the interval on the area, in
km², not on the classification accuracy.

---

## ★★6 — Pixel count versus patch count

Binomial standard error at $p = 0.9$:

$$\text{pixels: } \sqrt{\frac{0.9\times0.1}{1000}} = \sqrt{9\times10^{-5}} = 0.0095,$$
$$\text{patches: } \sqrt{\frac{0.9\times0.1}{100}} = \sqrt{9\times10^{-4}} = 0.0300 .$$

The pixel-based interval is too narrow by a factor of $0.0300/0.0095 = 3.16$,
which is $\sqrt{10}$ — the square root of the average number of pixels per patch.
Reporting $\pm1.9\%$ (two standard errors on 1 000 pixels) when the honest figure
is $\pm6\%$ (two standard errors on 100 patches) is the difference between claiming
a precise map and having a vague one.

The assumptions must be stated: "100 independent patches" came from an assumed
$10 \times 10$-pixel patch size, which must be justified from the scene's
autocorrelation range, not chosen to make the arithmetic convenient. Under a
blocked validation with block-level resampling (bootstrap over blocks), the
inflation appears automatically.

---

## ★★★7 — Validating domain adaptation

**Data required.** Labelled samples from the **target** scene — even a small
number. Adaptation without any target labels is untestable against target truth,
so the honest design always reserves some.

**Split.** Three-way: source-only training; adaptation fitted on *unlabelled*
target data (or a labelled subset); evaluation on *held-out labelled* target
samples that participated in neither. Spatial blocking applies within the target
scene as in ★5.

**Metric.** Target-scene confusion matrix: per-class recall and user's accuracy,
overall accuracy, kappa, and the *predicted class proportions* against the known
or independently estimated target proportions. The proportion comparison is what
detects a residual prior mismatch, which accuracy hides.

**Control separating adaptation from retraining.** A model trained directly on the
labelled target subset of the same size. If the adapted model does not beat it,
the adaptation has added nothing that the labels did not; if the adapted model
wins, the gain came from the unlabelled target data, and the control quantifies it
fairly.

**What it cannot establish.** That performance holds on another scene with a
different atmosphere or sensor (adaptation fits the target scene it saw), and
whether the improvement survives when the target labels are drawn from a different
part of the target scene — which is exactly the transfer the adaptation is
supposed to buy.

---

## ★★★8 — Correcting a mapped area

**Derivation.** Partition the scene into the $K$ mapped classes, with $N_j$ pixels
mapped to class $j$ and $\sum_j N_j = N$. Let $p_{jk}$ be the fraction of the
pixels **truly** in class $k$ among those mapped to class $j$ — the *columns* of
the confusion matrix normalised by the mapped (row) totals. Then the true number
of pixels in class $k$ is

$$\hat N_k^{\text{true}} = \sum_{j=1}^{K} N_j\,p_{jk}, \qquad
\hat A_k = A_{\text{scene}}\,\frac{\hat N_k^{\text{true}}}{N} .$$

The estimator is a weighted average of the error rates, with the mapped class
counts as weights; it is unbiased for the true area when the validation sample is
probability-sampled within strata, which is why area-estimation protocols
stratify by the mapped class.

**Applying it to cropland.** The mapped cropland fraction is $0.250$. The
correction needs $p_{\text{cropland},\text{cropland}}$ — the fraction of pixels
mapped as cropland that are truly cropland, which is the *user's accuracy*.

**What the demonstration reports and what it does not.** It reports *recall*
(producer's accuracy): of the truly cropland pixels, what fraction were mapped as
cropland — $0.938$ in the six-band case, $0.848$ after thinning. It does **not**
report the user's accuracy for any class, because computing it requires the
columns of the confusion matrix, and the demonstration prints only the per-class
recall. Producer's and user's accuracy are different quantities and only the
second corrects a mapped area.

**What an area study must therefore add.** The full confusion matrix (or at least
the column-normalised entries $p_{jk}$ for every $j$), sampled with a probability
design within mapped strata, with the sample size chosen to control the area
interval rather than the accuracy interval. Without it, an area reported from a
map with 0.95 accuracy can be biased by several per cent of the scene, in a
direction set by the class that is over-mapped.

---

## ★★★9 — Band selection for a rare alteration class

**Search procedure.** Do not search all $2^{12}$ subsets against the validation
score. Instead: (i) state the *physics* first — the absorption features the
alteration mineral has, and therefore which two or three band ratios carry the
information; (ii) form a small candidate set of band sets: the physics-motivated
one, the full set, a principal-component set, and one deliberately weak set as a
control; (iii) evaluate all candidates on the same folds.

**Metric.** Per-class recall and user's accuracy for the alteration class, with
the confusion matrix printed, plus the predicted proportion of the class. Because
the class is rare, overall accuracy is useless: a classifier that never predicts
the class scores near 1.0 overall, so the metric is the class's own recall and the
area it maps.

**Sizing.** With a rare class, the count of positive validation pixels is what
limits resolution. For a recall near $p = 0.6$ and a target half-width of $0.10$ at
three standard errors, the number of true-class validation pixels must satisfy
$\sqrt{p(1-p)/n} \le 0.0333$, i.e.
$n \ge 0.24/1.11\times10^{-3} \approx 216$ true-class pixels. With a $1\%$ class
prevalence that means about 21 600 validation pixels — and they must be spatially
separated, or clustered (as in ★6), so the number of independent units is what
must reach 216.

**Control against overfitting the validation set.** Split the candidate evaluation
from the reported result: compare band sets on a *selection* fold set, then report
the winner's performance on a held-out set it never touched. With four candidate
sets and a rare class, selection on the reported set inflates the winner by
roughly the maximum of four noisy estimates — enough to manufacture a $0.05$
recall difference out of nothing, which is why the physics-motivated candidate
should be chosen before the numbers are seen.
