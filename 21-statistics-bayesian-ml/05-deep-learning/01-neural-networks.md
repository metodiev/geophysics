---
id: 21-05-01
title: "Neural Networks: Architecture, Activation, Backpropagation"
level: doctoral
prereqs: ["21-04-04", "01-06-02"]
estimated_minutes: 70
tags: [deep-learning, neural-networks, backpropagation, activation-functions, universal-approximation]
---

# Neural Networks: Architecture, Activation, Backpropagation

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the forward pass of a multilayer perceptron and **state** the role
   of the activation function.
2. **Derive** the backpropagation recursion from the chain rule and **verify** an
   implementation by finite differences.
3. **Explain** the universal-approximation property and **state** what it does
   not promise.
4. **Demonstrate** with numbers why a linear model cannot represent an
   interaction and a single hidden layer can.
5. **Compare** activation functions by their gradient behaviour and **state** why
   the choice affects optimisation more than representation.
6. **State** what a trained network's parameters do and do not mean physically.

All data in this lesson are **SYNTHETIC**, generated in the demonstration. No
measured value is used and no accuracy below transfers to real data.

## Prerequisites

- [21-04-04 Regularisation: Ridge, Lasso, Early Stopping](../04-machine-learning-fundamentals/04-regularization-ml.md) —
  how a network's effective complexity is controlled.
- [01-06-02 Partial Derivatives](../../01-mathematics/06-multivariable-calculus/01-partial-derivatives.md) —
  the chain rule that backpropagation implements.
- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](../04-machine-learning-fundamentals/02-bias-variance.md) —
  the trade a network's width and depth move along.

## 1. Intuition: a stack of linear maps separated by kinks

A single layer computes $Wx + b$, a linear map. Stacking linear maps gives
another linear map, so depth alone buys nothing. The activation function is what
breaks the linearity: applied elementwise after each affine map, it lets the
composition represent curved functions. A network is therefore a **sum of
parameterised basis functions** whose shape is set by the activations, and
"training" is the search for the coefficients.

The consequence to keep in mind throughout: a network is a **universal
approximator** in the sense that it can represent any continuous function on a
compact set to any accuracy, given enough units. That is a statement about
representability, not about learnability, generalisation or data efficiency — and
in geophysics those three, not representability, are the binding constraints.

## 2. The forward pass

For $L$ layers with activations $\phi_\ell$,

$$z^{(0)} = x, \qquad
a^{(\ell)} = W^{(\ell)}z^{(\ell-1)} + b^{(\ell)}, \qquad
z^{(\ell)} = \phi_\ell\big(a^{(\ell)}\big), \qquad \ell = 1,\dots,L,$$

and the prediction is $z^{(L)}$ (linear or with a task-appropriate final
activation). Common choices and their derivatives:

| activation | $\phi(u)$ | $\phi'(u)$ | note |
|---|---|---|---|
| logistic | $1/(1+e^{-u})$ | $\phi(1-\phi)$ | saturates; output in $(0,1)$ |
| tanh | $\tanh u$ | $1-\tanh^{2}u$ | zero-centred; saturates |
| ReLU | $\max(u,0)$ | $\mathbf 1\{u>0\}$ | no saturation for $u>0$; dead units |
| softmax | $e^{u_j}/\sum_k e^{u_k}$ | — | used for classification outputs |

Saturation is the recurring problem: where $\phi' \approx 0$ the gradient
vanishes, and a unit that is saturated for every training example receives no
gradient at all and stops learning. This is why ReLU replaced the logistic unit
in deep networks, and why the demonstration's ReLU run reaches a slightly lower
training MSE than the tanh run at the same width.

## 3. Backpropagation

Let $\delta^{(\ell)} = \partial \mathcal L/\partial a^{(\ell)}$. The chain rule
gives the recursion

$$\delta^{(\ell)} = \big(\delta^{(\ell+1)}W^{(\ell+1)\mathsf T}\big)
\odot \phi_\ell'\big(a^{(\ell)}\big), \qquad
\frac{\partial \mathcal L}{\partial W^{(\ell)}} = \delta^{(\ell)}
z^{(\ell-1)\mathsf T}, \qquad
\frac{\partial \mathcal L}{\partial b^{(\ell)}} = \delta^{(\ell)},$$

with $\delta^{(L)} = \partial\mathcal L/\partial z^{(L)}$ for the chosen loss. It
is the chain rule applied once per layer, and it computes **all** gradients in
one backward sweep at a cost comparable to the forward pass. Two properties make
it the only practical algorithm: the intermediate activations $z^{(\ell)}$ are
reused rather than recomputed, and the cost is linear in the number of layers
rather than exponential in the number of paths.

An implementation should always be checked numerically:
$(\mathcal L(\theta+\varepsilon) - \mathcal L(\theta-\varepsilon))/(2\varepsilon)$
against the analytic gradient.

## 4. Worked example

The demonstration implements everything in NumPy and prints the checks.

**The XOR problem.** With the four input pairs $(0,0),(0,1),(1,0),(1,1)$ and
targets $0,1,1,0$:

| architecture | loss | predictions |
|---|---|---|
| no hidden layer (logistic) | $0.6931$ | $0.500, 0.500, 0.500, 0.500$ |
| $2$ hidden units | $0.3467$ | $0.000, 0.500, 1.000, 0.500$ |
| $4$ hidden units | $0.0003$ | $0.000, 1.000, 1.000, 0.000$ |

The linear model returns $0.5$ everywhere with loss $\ln 2 = 0.6931$: the target
has no marginal signal in either coordinate, so no linear function beats chance.
Two hidden units halve the loss but leave two predictions at $0.5$ — they give
the model a basis in which XOR is *expressible*, but the optimiser found a
symmetric saddle. Four hidden units reach $0.0003$, recovering the target exactly.
The progression is the lesson: capacity is necessary, and it is not sufficient.

**The gradient check.** With random weights, the analytic
$\partial\mathcal L/\partial W^{(1)}_{00}$ is $-0.02516416$ and the central
difference is $-0.02516416$; the largest absolute discrepancy over all entries is
$5.72\times10^{-11}$. That is the expected agreement at $\varepsilon = 10^{-6}$
(truncation error $\mathcal O(\varepsilon^{2})$ plus round-off
$\mathcal O(\epsilon_{\text{mach}}/\varepsilon)$), and it is the only cheap way to
confirm a backpropagation implementation.

**Activations.** On a smooth regression target with $20$ hidden units and the same
optimiser, tanh reaches a training MSE of $0.00154$ and ReLU $0.00049$ — a factor
of $3.1$. Both are adequate representations; the difference is in the gradient,
not in the function class, which is exactly the point of §2.

## Assumptions and regime of validity

1. **Representability is not learnability.** A universal approximator may be
   unlearnable from a finite sample with a given optimiser.
2. **i.i.d. sampling and held-out validation** still apply; a network inherits
   every assumption of [21-04-03](../04-machine-learning-fundamentals/03-model-assessment.md).
3. **The loss must match the task.** Cross-entropy for labels, squared error for
   regression, and a physically motivated term where one exists.
4. **Scaling matters.** Unscaled inputs make the effective learning rate
   different for every weight.
5. **Saturation kills gradients.** A unit whose pre-activation is large in
   magnitude for every example learns nothing.
6. **Parameters are not physics.** A weight in a trained network is a fitted
   coefficient; interpreting it as a physical sensitivity requires an independent
   argument.

## The honest summary

A neural network is a parameterised function whose flexibility comes from
elementwise nonlinearities between linear maps, and backpropagation computes its
gradients exactly and cheaply. The demonstration's numbers make the two halves of
that statement concrete. On XOR, a linear model sat at the $\ln 2 = 0.6931$ floor
however long it trained, two hidden units reached $0.3467$ and four reached
$0.0003$ — capacity first, optimisation second. The gradient check agreed to
$5.72\times10^{-11}$, which is the standard of evidence for a hand-written
implementation. What the numbers do **not** establish is that a network will
generalise: XOR has four data points and no noise, so it tests expressibility
only. Everything about sample size, regularisation and validation is the previous
module's business.

## Python demonstration

[`code/neural_networks_demo.py`](./code/neural_networks_demo.py) prints every
number quoted above. It:

1. trains networks on XOR with $0$, $2$ and $4$ hidden units;
2. verifies backpropagation by central finite differences;
3. compares tanh and ReLU hidden activations on a regression target.

```bash
cd 21-statistics-bayesian-ml/05-deep-learning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python neural_networks_demo.py
```

It runs in about two thirds of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/01-neural-networks-exercises.md`](./exercises/01-neural-networks-exercises.md)
with worked solutions in
[`exercises/01-neural-networks-solutions.md`](./exercises/01-neural-networks-solutions.md).

## Mastery checkpoint

Without notes, a linear model on XOR gives loss $0.6931$ and predictions
$0.5$ everywhere; four hidden units give loss $0.0003$; and a finite-difference
check agrees with the analytic gradient to $5.72\times10^{-11}$.

1. Compute $\ln 2$ and state why the linear model's loss equals it.
2. State why two hidden units are representable but did not solve the problem
   here.
3. State the order of the finite-difference truncation error and the round-off
   error at $\varepsilon = 10^{-6}$.
4. State the assumption a network inherited from supervised learning that is
   unrelated to its architecture.

## Common pitfalls

1. **Believing universal approximation implies success.** The four-unit run
   solved XOR; the two-unit run, equally representable, did not.
2. **Skipping the gradient check.** A subtle backpropagation error produces a
   slowly converging model rather than an exception.
3. **Forgetting to scale inputs.** The effective step size differs per weight.
4. **Using a saturating output for a regression task.** Logistic units cannot
   represent values outside $(0,1)$.
5. **Reporting training loss.** It says nothing about generalisation.
6. **Reading weights as physical sensitivities.** They are fitted coefficients of
   a non-identifiable parameterisation.

## Where this is used

- **Seismic attribute inversion**: regression from attributes to rock
  properties.
- **Facies classification** from logs, where a small network is a strong
  baseline.
- **Denoising**: networks trained on paired noisy and clean synthetic data.
- **Physics-informed learning**: a network augmented with a residual term from a
  differential equation.
- **Surrogate models**: fast approximations of an expensive forward solver.

## Related lessons

- [21-04-04 Regularisation: Ridge, Lasso, Early Stopping](../04-machine-learning-fundamentals/04-regularization-ml.md) —
  weight decay and early stopping, the network's regularisers.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../04-machine-learning-fundamentals/03-model-assessment.md) —
  the validation a network needs.
- [21-05-02 Convolutional Networks for Seismic and Image Data](02-cnns.md) —
  architecture that encodes spatial structure.
- [21-05-05 Autoencoders for Compression and Denoising](05-autoencoders.md) —
  networks trained without labels.
- [01-06-02 Partial Derivatives](../../01-mathematics/06-multivariable-calculus/01-partial-derivatives.md) —
  the calculus backpropagation applies.

## Self-assessment checklist

- [ ] I can write a forward pass and name the activation derivatives.
- [ ] I can derive and implement the backpropagation recursion.
- [ ] I can verify gradients by finite differences.
- [ ] I can state what universal approximation does and does not promise.
- [ ] I can explain why activation choice affects optimisation.
- [ ] I can say what a network's weights do not mean.
