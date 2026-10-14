# Exercises — 21-05-07 Self-Supervised Learning with Unlabelled Earth Data

Attempt these before reading the
[solutions](./07-self-supervised-solutions.md). The lesson is
[07 Self-Supervised Learning](../07-self-supervised.md). All data are
**SYNTHETIC**.

## ★ Foundational

**★1.** Define a pretext task and give three examples that are plausible on
geophysical data.

**★2.** Write the InfoNCE loss and state what value it takes when the positive and
the negative are indistinguishable.

**★3.** State what a linear probe measures and what it does not.

## ★★ Applied

**★★4.** Masked reconstruction reduces the MSE on hidden entries from $5.62434$
(feature mean) to $0.73590$ (ridge on the observed entries). Compute the reduction
and state why the mean is the right baseline.

**★★5.** The InfoNCE losses at negative scales $2.0, 1.0, 0.5, 0.3, 0.25$ are
$0.47832, 0.57625, 0.65847, 0.69198, 0.70026$ with ranking accuracies
$0.995, 0.985, 0.845, 0.490, 0.340$. Compute $\ln 2$, state which settings lie
above it, and explain the accuracy below $0.5$ at the smallest scale.

**★★6.** The linear probe gives $0.9600$ for raw features and $0.9133$ for frozen
features at $450$ labels, and $0.9400$ against $0.9133$ at $12$ labels. Compute the
two differences and state what the pattern means for the value of reporting a probe
without a raw-feature baseline.

## ★★★ Research-oriented

**★★★7.** Specify a study that measures whether a representation pretrained on one
basin **transfers** to another. State the design, the blocked evaluation, the
metric, the controls, and the criterion for declaring transfer.

**★★★8.** Specify an experiment on the difficulty of negative sampling for a
contrastive seismic task. State the design, the metric, the replicate count, the
predicted ordering, and how representation collapse would be detected and
distinguished from a genuinely easy task.
