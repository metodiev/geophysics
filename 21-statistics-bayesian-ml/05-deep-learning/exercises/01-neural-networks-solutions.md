# Solutions — 21-05-01 Neural Networks: Architecture, Activation, Backpropagation

> Read after attempting. Lesson:
> [01 Neural Networks](../01-neural-networks.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — A one-hidden-layer network

$$\hat y = w^{\mathsf T}\sigma(Wx + b) + c,$$

with $W \in \mathbb R^{h\times d}$, $b \in \mathbb R^{h}$, $w \in \mathbb R^{h}$
and a scalar $c$. The activation $\sigma$ is applied element-wise and is what makes
the composition nonlinear: without it the whole expression collapses to a single
linear map $w^{\mathsf T}W x + (w^{\mathsf T}b + c)$, so depth would buy nothing.

---

## ★2 — XOR with no hidden layer

XOR is not linearly separable: the two positive examples lie on one diagonal and
the two negative examples on the other, so no hyperplane separates them. A logistic
model without hidden units can only place a hyperplane, so the best it can do is
assign the same probability to all four points. The optimum of that constrained
problem is $\hat p = 0.5$ everywhere, giving the loss

$$-\frac{1}{4}\big[0\ln 0.5 + 1\ln 0.5 + 1\ln 0.5 + 0\ln 0.5\big] = \ln 2
= 0.6931,$$

which is the entropy of a fair coin — the value the demonstration reports. The
number is a **floor imposed by the hypothesis class**, not an optimisation failure.

---

## ★3 — Universal approximation and its limit

A feedforward network with one hidden layer of sufficient width and a
non-polynomial activation can approximate any continuous function on a compact
domain to any accuracy. It says nothing about:

- **how many units** are required — the bound is existential and can be enormous;
- **whether gradient descent finds** the approximating parameters — the objective
  is non-convex;
- **generalisation** — fitting the target on the training set is not the same as
  predicting new samples.

The theorem describes representability, and representability is only the first of
the three conditions for a useful model.

---

## ★★4 — The capacity ladder on XOR

$$\frac{0.6931 - 0.0003}{0.6931} = 0.99957, \quad\text{i.e. } 99.96\ \% \text{ of
the loss removed}.$$

Two hidden units reach the loss floor for XOR in principle — XOR needs two
half-space features, one per positive example — but the predictions
$0.000, 0.500, 1.000, 0.500$ show that it has committed to neither of the negative
cases confidently: one prediction is exactly $0.5$, so the model is undecided on
half the negative class and pays a loss of $0.3467$. Four hidden units have the
redundancy to put a margin on both negative examples and reach $0.0003$, with
predictions that reproduce the target. Capacity is therefore not a threshold but a
gradient: enough units to represent the function is not the same as enough units to
make the optimisation easy.

---

## ★★5 — Gradient-check accuracy

$$\frac{5.72\times10^{-11}}{0.02516416} = 2.3\times10^{-9}.$$

A central difference $(f(x+\varepsilon) - f(x-\varepsilon))/2\varepsilon$ has a
truncation error of order $\varepsilon^{2}$ and a round-off error of order
$\epsilon_{\text{mach}}/\varepsilon$. At $\varepsilon = 10^{-6}$ the truncation term
is about $10^{-12}$ and the round-off term about $10^{-16}/10^{-6} = 10^{-10}$, so
the total should be of order $10^{-10}$ — which is exactly the observed
$5.72\times10^{-11}$. An agreement much better than that would be suspicious rather
than better; an agreement far worse indicates a bug in the backward pass. The
recommended practice is to check at several $\varepsilon$ and confirm the
characteristic V-shape of the error.

---

## ★★6 — Activation comparison

$$\frac{0.00154}{0.00049} = 3.14 .$$

ReLU is about three times more accurate here, but the comparison holds only for
this target, this width, this initialisation and this optimiser. The two functions
span the same class of continuous functions when width is unlimited — the
difference is in the optimisation landscape and the gradient, not in
representability. ReLU's constant positive-side derivative keeps gradients from
saturating and is usually faster; tanh is smooth and bounded, which sometimes helps
on small data and loses less to exploding activations. A claim that one activation
is better in general is not supported by a single target; it would need a sweep
over targets, widths and seeds, with the spread reported.

---

## ★★7 — Depth against width per parameter

**Design.** Fix a synthetic target that requires an interaction of order $r$:
for example $y = \prod_{j=1}^{r} x_j$ on $x \in [-1,1]^{r}$ with $r \in \{2, 4, 8\}$.
Train a grid of networks whose **parameter count is held constant** — for example
near $5\,000$ — by trading layers against width: $(1, 2048)$, $(2, 512)$, $(4, 128)$,
$(8, 32)$, $(16, 8)$ hidden units per layer. Keep the activation, the optimiser, the
schedule and the training-set size identical.

**Metric.** Held-out MSE, converted to a fraction of the target's variance so it is
dimensionless, and reported per $1\,000$ parameters as well as in total.

**Budget control.** Equal parameter count, equal training examples, equal epochs
and equal tuning effort. Tuning one arm harder than another invalidates the
comparison; use the same random search budget for every arm.

**Replicates.** Ten seeds per cell, reported with the spread, since depth converts
a representational advantage into an optimisation difficulty that is
seed-dependent.

**Predicted ordering.** At $r = 2$ the shallow wide model wins or ties, because the
target has no hierarchical structure to exploit. As $r$ grows, depth wins on
accuracy per parameter, because a product of $r$ terms is built recursively and
each layer can multiply a partial product by one more factor; the wide shallow
model needs exponentially many units for the same job. The claim is falsified if
the advantage does not grow with $r$.

---

## ★★8 — How many hidden units are enough?

**Design.** Fix the target, the optimiser and the data, and sweep the width
$h = 1, 2, 4, 8, \dots, 256$. At each width, train to **convergence** — not to a
fixed epoch count — and with **several restarts**, since a single run confounds
width with initialisation. Record both the training and the held-out loss.

**Distinguishing the two explanations.** Trainability is tested directly:

1. **Several restarts.** If some restarts reach a much lower loss at the same width,
   the obstacle was optimisation, not capacity.
2. **A supervised fit to the target's own outputs** on a dense grid, with the loss
   taken to machine precision. If the network cannot even fit the target points, it
   cannot represent the function.
3. **A longer schedule and a lower learning rate.** If the training loss is still
   falling when training stops, the run was not converged and the width conclusion
   is void.

**Criterion.** The width is declared sufficient when the training loss stops
decreasing beyond the spread across restarts; the curve of training loss against
width should show a knee. If the loss instead keeps falling in the width, the
target's required width had not been reached; if it plateaus well above zero while
the loss on the target points themselves is small, the remaining error is
optimisation, not capacity.
