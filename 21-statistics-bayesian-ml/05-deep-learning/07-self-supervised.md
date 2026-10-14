---
id: 21-05-07
title: "Self-Supervised Learning with Unlabelled Earth Data"
level: research
prereqs: ["21-05-05", "21-04-06"]
estimated_minutes: 55
tags: [deep-learning, self-supervised-learning, pretext-tasks, contrastive-learning, linear-probe]
---

# Self-Supervised Learning with Unlabelled Earth Data

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a pretext task and **explain** how a label is manufactured from the
   data itself.
2. **Compute** masked reconstruction performance from observed entries and
   **state** what the reduction measures.
3. **Write** the InfoNCE loss and **interpret** its value relative to $\ln 2$ and
   to the difficulty of the negatives.
4. **Evaluate** a frozen representation with a linear probe and **state** why the
   probe's labels do not invalidate the measurement.
5. **State** the failure modes: trivial pretext tasks, representation collapse and
   leakage between the pretext and the downstream data.
6. **Decide** when pretraining on unlabelled data is worth its cost.

All data in this lesson are **SYNTHETIC**, generated in the demonstration. No
measured value is used.

## Prerequisites

- [21-05-05 Autoencoders for Compression and Denoising](05-autoencoders.md) —
  the reconstruction objective the pretext tasks generalise.
- [21-04-06 Feature Engineering for Earth Data](../04-machine-learning-fundamentals/06-feature-engineering.md) —
  the hand-built alternative to a learned representation.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../04-machine-learning-fundamentals/03-model-assessment.md) —
  the discipline a pretraining pipeline must respect.

## 1. Intuition: invent the labels

Earth data are abundant and labelled Earth data are scarce: there are many
seismic records and few interpreted horizons, many well logs and few cored
intervals. Self-supervised learning exploits that asymmetry by **manufacturing the
supervision** from the data. Hide part of a signal and predict it; take two
different views of the same record and require them to map to similar
representations; predict the transformation that was applied. The network learns
structure because the pretext task cannot be solved without it.

The method then has to be *evaluated*, and the standard device is a **linear
probe**: freeze the representation, fit a simple linear model on a few labels, and
measure. A representation that carries the relevant information makes even a
linear model succeed.

## 2. Masked modelling

The pretext task hides a fraction of the entries and predicts them from the rest.
It is the spatiotemporal analogue of a masked-language task, and in geophysics it
is directly useful: a seismic record with a dead trace, a well log with a gap or a
remote-sensing image with a cloud are all masking problems.

The demonstration generates $400$ samples of $20$ features from a rank-6 generator
plus noise, hides $20\ \%$ of the entries, and predicts them with a ridge model
fitted on the other half of the data:

| predictor | MSE on the masked entries |
|---|---|
| feature mean | $5.62434$ |
| ridge on the observed entries | $0.73590$ |

The reduction is **$86.9\ \%$**. The mean is the honest baseline — it is what a
model that learned nothing would achieve — and the gap quantifies how much
structure the observed entries carry. A pretext task whose reduction over the
baseline is near zero carries no learning signal.

## 3. Contrastive learning

Contrastive methods require a positive pair (two views of the same thing) to be
closer than any negative pair, measured by a softmax over similarities:

$$\mathcal L_{\text{InfoNCE}} = -\ln
\frac{\exp\big(s(q, k^{+})\big)}{\exp\big(s(q,k^{+})\big)
+ \sum_{j}\exp\big(s(q,k_j^{-})\big)} .$$

The loss is the negative log probability that the positive is ranked first. With
one positive and one negative it equals $\ln 2 = 0.69315$ when the two are
indistinguishable and falls towards zero as the positive becomes separable.

The demonstration varies how close the negatives are to the anchor:

| negative scale | InfoNCE loss | positive ranked first |
|---|---|---|
| 2.00 | $0.47832$ | $0.995$ |
| 1.00 | $0.57625$ | $0.985$ |
| 0.50 | $0.65847$ | $0.845$ |
| 0.30 | $0.69198$ | $0.490$ |
| 0.25 | $0.70026$ | $0.340$ |

As the negatives approach the anchor the task becomes harder, the loss rises
towards $\ln 2$, and the ranking accuracy falls from $0.995$ to $0.340$ — below
chance, because at the smallest scale the "negative" is nearly indistinguishable
from the positive and the comparison is a coin toss. The demonstration quantifies
the standard advice that **hard negatives carry the learning signal**: easy
negatives produce a loss near zero that measures nothing.

Note also that the loss exceeds $\ln 2$ at the hardest setting: $\ln 2$ is the
value at an even comparison, not an upper bound, and a loss above it means the
positive is being ranked below the negative more often than not.

## 4. Evaluation by linear probe

A frozen representation is evaluated by fitting a linear classifier on a few
labelled examples and measuring held-out accuracy. The demonstration uses a
$600$-sample two-class problem with four raw features and a fixed nonlinear
"pretrained" encoder producing six features:

| labelled samples | raw features | frozen features |
|---|---|---|
| 450 | $0.9600$ | $0.9133$ |
| 40 | $0.9600$ | $0.9000$ |
| 12 | $0.9400$ | $0.9133$ |

The frozen representation is *slightly worse* than the raw features at every label
budget — an honest and important result. The encoder here is a fixed random
projection, not a representation learned from data, so it adds no information and
costs a little. The probe's value is as a **protocol**: it measures how much of
the label a representation carries, and it is the comparison a genuinely pretrained
encoder must win. Reporting a probe accuracy without the raw-feature baseline is
uninformative.

## Assumptions and regime of validity

1. **The pretext task must be non-trivial.** A task solvable by interpolation of
   neighbouring samples teaches nothing transferable.
2. **Augmentations must preserve the label.** For contrastive methods, a positive
   pair that differs in the property being predicted teaches the wrong invariance
   — a gain change is not the same record for amplitude classification.
3. **Collapse must be prevented.** Without a negative term or a variance
   constraint the encoder can map everything to one point and minimise the loss.
4. **No leakage between pretext and downstream data.** The unlabelled corpus must
   not include the validation records; otherwise the probe measures memory.
5. **The probe has its own bias.** A linear probe can under-report a nonlinear
   representation; report the probe type with the result.
6. **Pretraining costs compute.** The gain must be measured against training from
   scratch on the labelled data alone.

## The honest summary

Self-supervised learning turns unlabelled data into supervision by inventing a
task, and the demonstration shows both what that buys and what it costs. Masked
reconstruction cut the prediction MSE on hidden entries from $5.62434$ to
$0.73590$, an $86.9\ \%$ reduction over the mean baseline, because the observed
entries genuinely constrain the hidden ones. Contrastive learning behaved exactly
as the theory predicts: as negatives approached the anchor the InfoNCE loss rose
from $0.47832$ to $0.70026$ and the ranking accuracy fell from $0.995$ to $0.340$,
so hard negatives are what carry the signal. And the linear probe delivered the
necessary caution — a fixed random "representation" was *worse* than the raw
features at every label budget ($0.9133$ against $0.9600$ at $450$ labels), which
is why a pretrained encoder must always be reported against the raw-feature
baseline. What none of these numbers establishes is transfer: a representation
pretrained on one basin, acquisition or sensor may carry nothing usable to
another, and only a blocked evaluation can show it.

## Python demonstration

[`code/self_supervised_demo.py`](./code/self_supervised_demo.py) prints every
number quoted above. It:

1. performs masked reconstruction with a ridge predictor and the mean baseline;
2. computes the InfoNCE loss for four negative scales;
3. evaluates frozen features with a linear probe at three label budgets.

```bash
cd 21-statistics-bayesian-ml/05-deep-learning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python self_supervised_demo.py
```

It runs in under two tenths of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/07-self-supervised-exercises.md`](./exercises/07-self-supervised-exercises.md)
with worked solutions in
[`exercises/07-self-supervised-solutions.md`](./exercises/07-self-supervised-solutions.md).

## Mastery checkpoint

Without notes, masked reconstruction reduces the MSE on hidden entries from
$5.62434$ to $0.73590$; the InfoNCE loss rises from $0.47832$ to $0.70026$ as
negatives approach the anchor; and a frozen random projection scores $0.9133$
against $0.9600$ for the raw features at $450$ labels.

1. Compute the percentage reduction of the masked reconstruction and state the
   baseline it is measured against.
2. Compute $\ln 2$ and state the two scales at which the loss lies on either side
   of it.
3. State why the frozen representation's deficit is a useful result rather than a
   failed experiment.
4. State two augmentations that must **not** be used as positives for a task
   predicting instrument gain.

## Common pitfalls

1. **A trivial pretext task.** Interpolating a smooth signal teaches nothing.
2. **Augmentations that destroy the label.** Wrong invariances are learned
   silently.
3. **Collapse.** Without negatives or a variance term the loss goes to zero for
   the wrong reason.
4. **Probe without a baseline.** A probe accuracy alone is not evidence of a good
   representation.
5. **Leakage into the unlabelled corpus.** Validation records must be excluded.
6. **Assuming transfer.** Pretraining on one acquisition does not guarantee
   anything on another without a blocked test.

## Where this is used

- **Seismic representation learning** from large unlabelled volumes, fine-tuned
  for facies or faults.
- **Well-log pretraining** across basins, with a small labelled set per target.
- **Remote sensing**: pretraining on unlabelled imagery for classification with
  few labels.
- **Anomaly detection**: a pretext task learned on normal data, with anomalies as
  the high-error cases.
- **Denoising**: masked modelling is itself a denoising pretext.

## Related lessons

- [21-05-05 Autoencoders for Compression and Denoising](05-autoencoders.md) —
  the reconstruction objective and its denoising variant.
- [21-04-06 Feature Engineering for Earth Data](../04-machine-learning-fundamentals/06-feature-engineering.md) —
  the hand-built alternative.
- [21-05-04 Attention and Transformers for Geophysical Sequences](04-transformers.md) —
  the architecture usually pretrained in this way.
- [21-05-06 GANs, VAEs and Diffusion Models](06-generative-models.md) —
  the generative use of unlabelled data.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](../06-ml-in-geophysics/09-ml-pitfalls-geophysics.md) —
  why transfer must be tested, not assumed.

## Self-assessment checklist

- [ ] I can define a pretext task and say what makes it non-trivial.
- [ ] I can compute masked-reconstruction performance against a baseline.
- [ ] I can write and interpret the InfoNCE loss.
- [ ] I can run a linear probe and report it against a raw-feature baseline.
- [ ] I can name the three failure modes.
- [ ] I can state what pretraining does not guarantee.
