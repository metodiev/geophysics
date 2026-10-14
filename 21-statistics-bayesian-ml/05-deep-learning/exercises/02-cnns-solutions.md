# Solutions — 21-05-02 Convolutional Networks for Seismic and Image Data

> Read after attempting. Lesson:
> [02 Convolutional Networks](../02-cnns.md). Numbers quoted from the demonstration
> reproduce its output.

---

## ★1 — A convolutional layer

$$y_{f}(i,j) = b_f + \sum_{c=1}^{C}\sum_{u,v} K_f(u,v)\,x_c(i+u,\,j+v),$$

producing $F$ feature maps. The two economies are **weight sharing** — the same
$k^{2}$ weights are applied at every position, so the count is
$C\cdot F\cdot k^{2} + F$ and is independent of the image size — and **locality**,
since each output depends on a $k\times k$ neighbourhood rather than the whole
image. Sharing encodes a stationarity assumption; locality keeps the depth
tractable.

---

## ★2 — Which rows respond

The kernel is the row-to-row difference (bottom row minus top row). Over the band,
its top three rows look at $0$ and its bottom three at $1$, so the response is

$$-1\cdot 0 + 1\cdot 1 = +1 \times 3 \text{ per column} = +3,$$

placed where the kernel has just crossed into the band; one row later the kernel is
inside the band and the response is still $+3$; two rows further on the kernel
straddles the **exit** of the band and the response is $-3$. The demonstration
reports the maximum $3.0$ at rows $1$ and $2$ of the $6\times6$ output, with
$-3.0$ at rows $3$ and $4$. In the flat interior both the top and the bottom rows
of the kernel see the same value, so the difference is exactly $0$ — this is why a
derivative kernel responds only to boundaries.

---

## ★3 — Equivariance against invariance

**Equivariance:** shifting the input shifts the output by the same amount and
changes nothing else, $\mathrm{conv}(\tau_s x) = \tau_s\,\mathrm{conv}(x)$.
**Invariance:** the output does not change at all. A convolution with stride 1 is
equivariant, and the demonstration shows it exactly — the maximum moves from
$[[6,6],[6,7]]$ to $[[6,9],[6,10]]$ under a three-cell shift, with the same
magnitude $3.0$.

Invariance is not gratuitous: for a *detection* or *classification* target the
absolute position is irrelevant and global pooling is wanted, while for *mapping*
and *inversion* targets the position is part of the answer and equivariance is the
property that is actually needed. Using an invariant architecture for a mapping
task destroys the signal.

---

## ★★4 — Parameter counts

Convolution: $1\times16\times3^{2} = 144$ weights plus $16$ biases $= 160$. ✓

Fully connected: each of the $32\times32\times16 = 16\,384$ outputs connects to all
$32\times32\times1 = 1\,024$ inputs, giving $16\,384\times1\,024 = 16\,777\,216$
weights plus $16\,384$ biases,

$$16\,777\,216 + 16\,384 = 16\,793\,600. \quad ✓$$

$$\text{ratio} = \frac{16\,793\,600}{160} = 104\,960\times .$$

The ratio grows as the image size: the convolutional count is
$\mathcal O(k^{2}CF)$ while the dense count is $\mathcal O(C F H^{2}W^{2})$, so the
saving is quadratic in the side length.

---

## ★★5 — A wider and more numerous kernel

$$C\cdot F\cdot k^{2} + F = 1\times32\times5^{2} + 32 = 800 + 32 = 832
\text{ parameters}.$$

That is $832/160 = 5.2$ times the $3\times3$ version: the count scales with $k^{2}$
and with $F$, while the dense alternative would grow as $F k^{2}$ times the square
of the input size *per output pixel*. Even a $5\times5$ kernel with twice the
filters remains four orders of magnitude smaller than the fully connected layer of
★★4.

---

## ★★6 — Receptive field

| $L$ | $1 + 2L$ | cells |
|---|---|---|
| 1 | $3$ | $3$ |
| 2 | $5$ | $5$ |
| 3 | $7$ | $7$ |
| 6 | $13$ | $13$ |
| 12 | $25$ | $25$ |

At a $4\ \mathrm m$ sample interval a $13\times13$ field spans
$12\times4 = 48\ \mathrm m$ (or $13\times4 = 52\ \mathrm m$ if counted
inclusively) — the scale of a thin bed or a channel, not of a reservoir. The growth
is linear in depth while the parameter count is linear too, so a $50\times50$
context needs roughly $25$ layers or, far more cheaply, dilation or pooling.

---

## ★★7 — Does accuracy transfer across an amplitude change?

**Design.** Take one survey with a known lateral acquisition or gain difference and
split it **spatially** into area A and area B, so that no patch from A appears in B.
Train on A and evaluate on B, and vice versa; measure how much the accuracy drops
relative to an in-area cross-validation on the same data.

**Controls.** Three arms: (i) train on A, test on B; (ii) train on B, test on A;
(iii) train on the union and test on held-out patches inside each area — the
*larger-baseline* that isolates the effect of the domain shift from the effect of
training-set size. Normalising amplitudes per window is a fourth arm, to test
whether the loss is caused by the scale change alone.

**Metric.** Held-out accuracy and macro-$F_1$ in each area, plus the difference
between the cross-area and within-area numbers with a confidence interval across
spatial blocks.

**What would show stationarity has failed.** A large cross-area drop that survives
per-window amplitude normalisation and disappears when the two areas are pooled
into the training set. That pattern means the filter that works in A is genuinely
wrong in B, not merely mis-scaled — the stationarity assumption of weight sharing
has failed, and the remedy is per-area normalisation, test-time adaptation or
retraining with data from both areas.

---

## ★★8 — Dilated versus deeper stacks

**Design.** Construct a target whose output depends on two samples a known
distance $D$ apart, with $D \in \{8, 16, 32, 64, 128\}$ samples, embedded in noise.
Compare two families at **equal parameter count**: (i) a stack of $3\times3$
convolutions with $L$ layers giving a receptive field $1+2L$, and (ii) a stack with
dilations $1, 2, 4, \dots$ so the same number of layers reaches a field of
exponential size. Match the parameter count by varying channel width.

**Metric.** Held-out accuracy or MSE as a function of $D$, and the *effective*
receptive field measured empirically by perturbing an input sample at distance $d$
and recording the change in the output — the measured field, not the theoretical
one.

**Controls.** Identical optimiser, schedule, data and tuning budget; the same number
of measured-perturbation probes for both families.

**Predicted ordering.** Below the $3\times3$ stack's field ($D \le 1+2L$) the two
families should tie, since the deeper stack already sees the dependency. Above it,
the dilated stack should win decisively, because the deeper stack would need
$\mathcal O(D)$ layers and the matched-parameter constraint forbids that many
channels. The claim is falsified if the measured receptive field of the dilated
stack is much smaller than the theoretical one — a known failure mode caused by
dilation artefacts and non-uniform gradient flow — or if widening the shallow stack
recovers the same accuracy, which would show the task was not really long-range.
