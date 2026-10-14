# Solutions — 18-08-04 Reporting Inversion Results Responsibly

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC**.

Lesson: [04 Reporting Inversion Results Responsibly](../04-reporting-inversion.md).

---

## ★1 — Misfit versus error

Smallest error: 0.1228 at $\lambda = 30$ (chi = 0.939).
Largest error: 2.3229 at $\lambda = 10^{-3}$ (chi = 0.618, the smallest misfit).
At the largest $\lambda$ tested ($10^{3}$ scale, $\lambda = 300$): error 0.1523,
chi 1.253.

Conclusion: the model that fits the data best is about nineteen times further
from the truth than the model chosen by the discrepancy principle, so the misfit
alone is not a quality measure.

---

## ★2 — The eight lines, labelled

| line | value | kind |
|---|---|---|
| data | 15 observations, $\sigma = 0.25$ | measured (or assumed, then stated) |
| misfit | chi per datum 0.94 | measured |
| weight | $\lambda = 3.0\times10^{1}$ | chosen (by a stated criterion) |
| complexity | $\operatorname{tr}R = 4.94$ of 40 | modelled (prior-dependent) |
| resolution | 0 of 40 cells with $\operatorname{diag}R>0.5$; PSF 4.00 km | modelled |
| admitted range | per-depth 95% interval | modelled (from the posterior) |
| worst depth | $z = 19.75$ km, range 0.5468 | modelled |
| null space | 40 of 40 cells fail the resolution test | modelled |

Only the data count, the noise level and the misfit are measured; everything
else is a model or a choice, and a report should say so.

---

## ★3 — Discrepancy principle

Choose the regularisation weight for which the data misfit equals the level the
stated noise requires, i.e. chi per datum $\approx 1$; among the candidates,
prefer the smoothest (largest weight) that achieves it.

It needs a **stated noise level**. The L-curve needs none, which is its
advantage and its weakness: without a noise level there is no test of whether the
result under- or over-fits.

---

## ★4 — Rewriting the 12.25 km statement

Unsupported: "the inversion found a body at 12.25 km with amplitude 0.22".

Supported: "at 12.25 km the model is 0.2241 with a 95% admitted range
0.0448–0.4034; the data require a positive value there but do not determine it to
better than about a factor of nine between the ends of the range (0.40/0.04)."

Added: the **uncertainty**, and with it the information that the amplitude is
determined only to within a range wider than the value itself. A reader can now
decide whether the claim matters at that precision.

---

## ★5 — Why agreement is not proof

The discrepancy principle selects $\lambda$ from the **misfit** alone; the
best-error $\lambda$ minimises $\|\hat{\mathbf{m}}(\lambda)-\mathbf{m}_{\text{true}}\|$,
which requires the truth. They agree on this grid because the synthetic truth's
smoothness happens to be well matched by the chosen prior. Nothing in the method
guarantees this: the discrepancy principle can select a model whose error is much
larger than the best achievable, in particular when the prior is mis-specified
(a rougher truth, or a wrong smoothness operator).

Test that would expose failure: repeat the sweep with a **rougher truth** (for
example a layered model with sharp steps, or the truth from the spike family).
The discrepancy choice will still land at chi $\approx 1$, but the best-error
$\lambda$ will move to a much smaller value, and the gap between the two model
errors will open. Reporting that gap, on a synthetic family that resembles the
target, is the honest way to advertise the risk.

---

## ★6 — Four review questions

1. **"What noise level was assumed for chi, and how was it obtained?"** Needed
   answer: a number, and whether it came from repeat measurements, instrument
   specifications, or a residual-based estimate.
2. **"What is the misfit of the reported model, per datum, against that noise?"**
   Needed answer: a chi value near 1; a chi far from 1 invalidates the choice of
   weight in either direction.
3. **"What is the resolution length at the depth of the interpretation?"** Needed
   answer: a length in metres or kilometres (PSF half-width, or the result of a
   spike/checkerboard test), not the grid spacing.
4. **"What is the admitted range of the reported quantity?"** Needed answer: an
   interval. If the authors cannot produce one, the model is being reported
   without a measure of what the data determine.

---

## ★7 — A reporting standard for trans-dimensional inversion

Trans-dimensional (reversible-jump) sampling infers the number of parameters
itself, so "complexity" is not a fixed $\operatorname{tr}R$. Replacements:

- **misfit:** unchanged — chi per datum at the MAP or at the posterior mean.
- **weight:** replaced by the **prior specification** (the birth/death
  proposal and the prior on layer properties), which plays the same role and must
  be stated in full.
- **complexity:** replaced by the **posterior distribution of $k$**, the number of
  layers, reported as a histogram with its mode and its 95% interval.
- **resolution:** replaced by a **marginal resolution** — the probability, as a
  function of depth, that a layer boundary exists within a stated distance — plus
  a spike-recovery test on samples.
- **admitted range:** replaced by **pointwise credible intervals** from the
  posterior samples, with the caveat that near-identical models are visited with
  correlated frequency (the chain's mixing), so intervals must be checked for
  convergence.
- **null space:** replaced by a statement of which structural hypotheses are
  never visited (for example layers thinner than the sampler's proposal scale),
  which is a statement about the prior, not the data.

Naive translation fails because the model dimension is a random variable: an
interval on a parameter is meaningless when the parameter may not exist in a
given sample, and resolution must be defined per structural question rather than
per cell.

---

## ★8 — A misleading report that satisfies the template

Construction: report a model and a per-depth 95% admitted range computed from a
**linearised posterior at a single point** for a nonlinear problem whose true
posterior is multimodal. Every line of the template is present and arithmetically
correct: chi $\approx 1$, $\operatorname{tr}R$ from the local Hessian, PSF from
the local resolution matrix, and an admitted range from the local covariance.
The report is misleading because the data admit a second, structurally different
model elsewhere in the space, and the local interval says nothing about it.

Additional test to demand: a **multi-start or sampling check** — invert from
several very different starting models and report whether they converge to the
same model within the admitted range. If they do not, the local interval is not a
description of what the data determine, and the alternatives must be reported
alongside it.
