# Exercises — 21-05-01 Neural Networks: Architecture, Activation, Backpropagation

Attempt these before reading the
[solutions](./01-neural-networks-solutions.md). The lesson is
[01 Neural Networks](../01-neural-networks.md). All data are **SYNTHETIC**.

## ★ Foundational

**★1.** Write the output of a one-hidden-layer network with $d$ inputs, $h$ hidden
units and a scalar output, and state the role of the activation function.

**★2.** On XOR the demonstration reports predictions $0.500, 0.500, 0.500, 0.500$
and loss $0.6931$ with no hidden layer. State why a linear model cannot do better
and identify the constant $0.6931$.

**★3.** State the universal approximation property and one thing it does **not**
guarantee.

## ★★ Applied

**★★4.** The demonstration's XOR losses are $0.6931$ (no hidden layer), $0.3467$
(two hidden units) and $0.0003$ (four hidden units), with predictions
$0.000, 1.000, 1.000, 0.000$ at the last setting. Compute the reduction from the
first to the third and state what the second setting's predictions
($0.000, 0.500, 1.000, 0.500$) reveal about its capacity.

**★★5.** The analytic gradient $\partial\mathcal L/\partial W^{(1)}_{00}$ is
$-0.02516416$ and the central difference gives $-0.02516416$; the largest
discrepancy over all entries is $5.72\times10^{-11}$. Compute the relative error
and state what the central difference's error should scale with.

**★★6.** With the same architecture and optimiser, tanh reaches a training MSE of
$0.00154$ and ReLU $0.00049$. Compute the ratio and state why the comparison does
not show that one activation is universally better.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that tests whether depth or width buys more
accuracy **per parameter** on a synthetic regression problem with a known
interaction structure. State the design, the metric, the budget control, the
replicate count and the predicted ordering.

**★★★8.** Specify a study that determines how many hidden units a target function
needs before the loss stops improving, and state how you would distinguish "the
network cannot represent it" from "the optimiser did not find the solution".
