# Solutions — 21-05-07 Self-Supervised Learning with Unlabelled Earth Data

> Read after attempting. Lesson:
> [07 Self-Supervised Learning](../07-self-supervised.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — Pretext tasks

A **pretext task** is a supervised-looking problem whose labels are derived from the
data without human annotation, so that solving it requires learning structure that
is useful for a downstream target. Three plausible examples on geophysical data:

1. **Masked reconstruction** — hide a fraction of samples, traces, wells or pixels
   and predict them from the rest. Directly useful for gaps and dead traces.
2. **Contrastive discrimination** — treat two augmented views of the same record as
   a positive pair and other records as negatives, and require the encodings to
   respect that ordering.
3. **Transformation prediction** — apply a known operation (a time shift, a gain
   change, a polarity flip, a rotation) and predict which one, or predict its
   magnitude; this is the standard route to self-supervised seismic velocity or
   azimuth estimation.

A fourth, common in the literature: **temporal or spatial ordering** — predict
whether two patches are in the correct relative order.

---

## ★2 — The InfoNCE loss

$$\mathcal L = -\ln \frac{\exp\big(s(q, k^{+})\big)}
{\exp\big(s(q,k^{+})\big) + \sum_{j}\exp\big(s(q,k_j^{-})\big)} .$$

The argument is the softmax probability that the positive key ranks first among
positive and negatives, so the loss is its negative logarithm. With one positive and
one negative and two equal scores, the probability is $1/2$ and the loss is

$$\ln 2 = 0.69315 .$$

That value is the **chance level** of the objective: a loss near it means the
encoder cannot tell the positive from the negative. The loss is unbounded above, so
a value greater than $\ln 2$ means the positive is usually ranked *below* the
negative — worse than an even comparison, which happens when a hard negative
genuinely looks more like the anchor than the "positive" augmentation does.

---

## ★3 — What a linear probe measures

A linear probe trains a linear model on **frozen** features and measures held-out
performance. It measures how much of the label is recoverable by a linear function
of the representation. It does **not** measure:

- the representation's nonlinear usability — a linear probe can under-report a
  representation whose information is present but entangled;
- the value of the pretraining — the probe's accuracy must be compared with the raw
  features and with a random projection of the same dimension, or it reflects only
  the probe's own capacity;
- robustness or transfer — a probe on the same distribution as the pretraining data
  says nothing about a new basin, sensor or acquisition.

The probe is a **protocol**, and its number is only meaningful next to its
baselines.

---

## ★★4 — Masked reconstruction

$$1 - \frac{0.73590}{5.62434} = 1 - 0.13084 = 86.9\ \% \text{ reduction}.$$

The mean is the right baseline because it is the optimal predictor that uses **no
information about the observed entries at all**: it is the answer a model that
learned nothing about the structure would give. It is also the solution of the same
least-squares problem with a single parameter, so the comparison isolates the value
of the observed entries rather than the value of having parameters.

The $86.9\ \%$ reduction says the synthetic data are strongly redundant — they come
from a rank-6 generator, so $6$ of the $20$ directions carry all the signal, and a
masked entry is largely determined by the rest. On real data the reduction is
smaller and its size is exactly the quantity of interest: near zero means the
pretext task teaches nothing.

---

## ★★5 — Loss against the chance level

$$\ln 2 = 0.69315 .$$

| negative scale | loss | vs $\ln 2$ | accuracy |
|---|---|---|---|
| 2.00 | $0.47832$ | $-0.21483$ | $0.995$ |
| 1.00 | $0.57625$ | $-0.11690$ | $0.985$ |
| 0.50 | $0.65847$ | $-0.03468$ | $0.845$ |
| 0.30 | $0.69198$ | $-0.00117$ | $0.490$ |
| 0.25 | $0.70026$ | $+0.00711$ | $0.340$ |

The scales $0.30$ and $0.25$ lie at and above the chance loss. At $0.25$ the
"negative" is so close to the anchor that the comparison is essentially a coin
toss, and the accuracy of $0.340$ is below $0.5$: with a finite number of trials
per anchor, the winner is decided by sampling noise, so the model is *systematically
wrong* more often than right — a loss above $\ln 2$ and an accuracy below $0.5$ are
two views of the same fact. The sequence of settings is the quantitative version of
the standard advice: easy negatives produce a loss near zero that measures nothing,
and the learning signal lives in the hard negatives.

---

## ★★6 — Probe differences

At $450$ labels: $0.9600 - 0.9133 = +0.0467$ for the raw features.

At $12$ labels: $0.9400 - 0.9133 = +0.0267$ for the raw features.

The frozen representation is **worse** at both budgets, and the gap narrows as
labels become scarce — which is what one expects from a fixed random projection: it
adds no information, and its six features are a lossy linear map of the four raw
ones, so it can only lose. The narrowing gap reflects the raw features' own
estimation error at $12$ labels, not any advantage of the projection.

The lesson is that a probe number alone is uninterpretable. Reported as "the frozen
representation reaches $0.9133$", the result sounds like success. Reported against
the raw-feature baseline it is a **negative** result, correctly identifying that
this encoder learned nothing. Any claimed representation must be reported with
both baselines — raw features and a random projection of the same dimension — and
the honest conclusion here is that random-feature encoders are not
representations.

---

## ★★7 — Does a representation transfer between basins?

**Design.** Pretrain on unlabelled data from basin A only. Fine-tune (or probe) on a
small labelled set from basin B, and compare with the identical downstream model
trained from scratch on the same labelled B data. Basins must be genuinely
different — different depositional setting or different acquisition, not two
neighbouring panels.

**Blocked evaluation.** Split by spatial block within B, and keep the unlabelled
corpus for pretraining **disjoint** from every block used for fine-tuning or
evaluation. Include a second setting in which the pretraining corpus deliberately
*includes* B's validation blocks, so the leakage effect is measured rather than
assumed; the difference between the two settings is the size of the leak.

**Metric.** Held-out accuracy or macro-$F_1$ on B at several label budgets, plus the
label efficiency: the number of B labels the from-scratch model needs to match the
pretrained model's accuracy. Report both — an accuracy gain at a fixed budget and a
label-efficiency ratio answer different questions.

**Controls.** Three arms at each budget: (i) pretrained on A, (ii) random
initialisation, (iii) pretrained on A but with the encoder **frozen** whereas the
scratch model is fully trained — the last isolates feature quality from
fine-tuning capacity. Match the total optimisation budget across arms, and use the
same downstream architecture.

**Criterion for declaring transfer.** The pretrained arm beats the from-scratch arm
on held-out blocks of B, with the improvement exceeding the seed-to-seed spread
(a paired comparison across at least ten seeds), and the improvement grows as B's
label budget shrinks. If the gain is flat in the label budget, or if it survives the
shuffled-pretraining control (pretraining on A with labels permuted), the effect is
regularisation or capacity, not transfer.

---

## ★★8 — Negative-sampling difficulty

**Design.** Fix a contrastive setup on seismic patches. Define the negatives by a
single controlled parameter: the spatial or temporal distance $d$ from the anchor,
with $d$ small meaning hard negatives (nearly the same patch). Sweep
$d \in \{0.25, 0.5, 1, 2, 4, 8\}$ patch widths, and hold everything else fixed — the
encoder, the batch size, the number of negatives per anchor, the optimiser and the
pretraining duration.

**Metric.** The InfoNCE loss at the end of training, the positive-ranked-first
accuracy, and — the number that matters — the linear-probe accuracy on a held-out
labelled task at a fixed small label budget. The first two are diagnostics; the
third is the criterion, because a loss can be low while the representation carries
nothing.

**Replicates.** Ten seeds per $d$, each with its own data draw, reported as mean and
spread with the paired comparison across $d$ (the same seeds must be used for every
$d$ so the difference is within-replicate).

**Predicted ordering.** Loss and ranking accuracy should degrade monotonically as
the negatives get harder — the demonstration shows the loss rising from $0.47832$ to
$0.70026$ and the accuracy falling from $0.995$ to $0.340$ as the negative scale
drops from $2.0$ to $0.25$. The probe accuracy should be **non-monotonic**: it
improves as negatives get harder until the task becomes so hard that the positive
and negative are statistically indistinguishable, after which the pretraining
degrades to noise and the probe accuracy falls back to the from-scratch baseline.
The predicted optimum is at the point where the loss is just below $\ln 2$.

**Collapse detection.** Collapse means the encoder maps everything to nearly one
point, which minimises the loss for the wrong reason. It is detected by three
independent measurements, all required: (a) the effective rank or the participation
ratio of the embedding covariance collapsing towards $1$; (b) the variance of the
embeddings across samples falling by orders of magnitude relative to
initialisation; (c) the probe accuracy falling to the majority-class rate while the
loss stays low. A low loss with a healthy effective rank is a genuinely easy task,
not collapse; a low loss with a rank near $1$ is collapse. Reporting the loss alone
cannot distinguish them, which is why the diagnostics must be reported together.
