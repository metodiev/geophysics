# Exercises — 21-05-03 Recurrent Networks and Temporal Earth Data

Attempt these before reading the
[solutions](./03-rnns-time-series-solutions.md). The lesson is
[03 Recurrent Networks](../03-rnns-time-series.md). All sequences are
**SYNTHETIC**.

## ★ Foundational

**★1.** Write the recurrence of a simple RNN and state what the hidden state is
for.

**★2.** State why backpropagation through time is ordinary backpropagation, and
what the gradient at an early step is a product of.

**★3.** The demonstration's target has variance $0.18570$ and the model reaches a
final training MSE of $0.09385$. Compute the fraction of the variance unexplained
and state what the remaining error consists of.

## ★★ Applied

**★★4.** The MSE falls from $0.13097$ (epoch $1$) to $0.12370$ (epoch $20$) to
$0.09385$ (epoch $120$). Compute the reduction between each pair and state which
part of the training the later epochs are buying.

**★★5.** For $\rho = 0.9$ the gradient norm at a step-$T$ dependence is
$5.90\times10^{-1}$ at $T = 5$, $1.22\times10^{-1}$ at $T = 20$ and
$1.48\times10^{-2}$ at $T = 40$. Verify the decay rate and state the norm policy
concludes for a 40-step dependence.

**★★6.** A plain recurrence keeps $1.478\times10^{-2}$ of a 40-step dependence,
a closed gate $g = 0.6225$ keeps $5.814\times10^{-9}$ and an open gate
$g = 0.9959$ keeps $8.495\times10^{-1}$. Verify the closed and open gate values
from $g^{40}$ and state what makes the gate different from a fixed weight.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that distinguishes "the dependence is not in the
data" from "the dependence is in the data but the optimiser cannot see it", on a
target with a known lag $T$. State the design, the metric, the controls and the
diagnostic that separates the two explanations.

**★★★8.** Specify a study comparing a gated recurrence with a plain RNN as a
function of dependence length $T$, stating the design, the matched controls, the
metric and the replicate count. Include the failure mode you expect if the gated
model is simply given more parameters.
