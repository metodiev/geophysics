# Exercises — 21-05-04 Attention and Transformers for Geophysical Sequences

Attempt these before reading the
[solutions](./04-transformers-solutions.md). The lesson is
[04 Transformers](../04-transformers.md). All tensors are **SYNTHETIC**.

## ★ Foundational

**★1.** Write the scaled dot-product attention formula and state in one sentence
what the softmax is doing.

**★2.** The demonstration's sequence has $T = 6$ and $d = 4$. The attention
matrix's rows sum to $1.000000$. State why that must be true for **any** input,
not just this one.

**★3.** State why the scaling by $\sqrt d$ is applied and what happens to the
softmax and the gradient without it.

## ★★ Applied

**★★4.** The causal-masked attention matrix has rows
$[1.000, 0, 0, 0, 0, 0]$ and $[0.884, 0.116, 0, 0, 0, 0]$. Compute the output of
position $2$ if the value rows are $v_1 = (2, 0)$ and $v_2 = (0, 2)$, and state
which positions contribute.

**★★5.** The attention row entropies are $1.420, 1.313, 1.444, 1.485, 1.678,
1.444$ nats and the maximum is $\ln 6 = 1.792$. Compute each as a fraction of the
maximum and state what the second row is doing compared with the fifth.

**★★6.** With $d = 64$ the demonstration reports attention score operations
$4\,096$, $65\,536$, $1\,048\,576$, $16\,777\,216$ and RNN operations
$32\,768$, $131\,072$, $524\,288$, $2\,097\,152$ for $T = 8, 32, 128, 512$.
Compute the ratio at each length, state the crossover length, and give the
general rule.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that measures whether attention's advantage over
a recurrence grows with the **distance** of the dependence, on synthetic sequences
with a controlled dependency length. State the design, the metric, the replicate
count and the predicted ordering. A specification that could not be executed is a
failed answer.

**★★★8.** Specify a study testing whether **attention weights can be used as
attributions** on a sequence task with a known ground-truth dependency. State how
you would construct the ground truth, the two attribution methods compared, the
metric, and the outcome that would falsify the use of attention weights as
explanations.
