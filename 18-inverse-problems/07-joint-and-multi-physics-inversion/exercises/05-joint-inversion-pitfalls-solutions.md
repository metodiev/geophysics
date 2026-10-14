# Solutions — 18-07-05 Pitfalls: Inconsistent Physics, Weighting, Over-Coupling

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC**.

Lesson: [05 Pitfalls: Inconsistent Physics, Weighting, Over-Coupling](../05-joint-inversion-pitfalls.md).

---

## ★1 — Discarded data set

With $w_1 = 10^{-3}$ and $w_2 = 1$ the joint solution effectively ignores **data
set 1**. Evidence: the distance to the $G_2$-only solution is 0.0001 (four
decimals), while the distance to the $G_1$-only solution is 0.0582 — an order of
magnitude of the model scale (the truth has unit amplitude). Meanwhile chi 2 is
0.39, well below 1, while chi 1 sits at 1.70, the value the $G_2$-only model
achieves.

---

## ★2 — Chi per datum

$$\chi = \frac{1}{\sqrt{p}}\left\|\mathbf{d}-\mathbf{g}(\mathbf{m})\right\|/\sigma
= \sqrt{\frac{1}{p}\sum_{i=1}^{p}\left(\frac{d_i-g_i(\mathbf{m})}{\sigma}\right)^2}.$$

Expected value when the model explains the data at the stated noise level:
$\chi \approx 1$ (one standard deviation per datum on average). $\chi \ll 1$
means the noise is over-stated or the model is over-fitted; $\chi \gg 1$ means
something is missing — often an assumption rather than a parameter.

---

## ★3 — Reading the over-coupling table

Both chi below 2: $\mu = 0$ (1.03, 0.53), $\mu = 0.1$ (1.01, 0.58),
$\mu = 1$ (1.46, 0.93). At $\mu = 10$ chi 1 is 8.92, far above 2.

Model error below the uncoupled 0.0371: $\mu = 0.1$ (0.0321) and $\mu = 1$
(0.0281). At $\mu = 10$ it is 0.0670, already worse.

So there is a narrow window ($\mu \lesssim 1$) in which the coupling is both
mildly beneficial and acceptable by chi; outside it, the coupling is either
pointless or harmful.

---

## ★4 — Two optima

Model error: minimum 0.0371 at $w_1 = 1$.
Closest to both chi = 1: also $w_1 = 1$ (chi 1.03, chi 2 = 0.53 — chi 2 is low,
suggesting $w_2$ could be increased slightly).

They agree on this grid. If they did not, the correct action is to trust the chi
criterion for choosing the weight (it uses only the stated noise), and to report
the model-error optimum *afterwards* as a check on a synthetic test — never to
tune the weight against the truth, which would be fitting the answer.

---

## ★5 — Why separate can fit and joint cannot

Each separate inversion minimises its own term, with a full $n$-dimensional model
available. The joint inversion minimises the **sum** with a *single* model, so it
must find a compromise that cannot reduce both residuals to their individual
minima simultaneously. Formally, if $\mathbf{m}_1^{\ast}$ and
$\mathbf{m}_2^{\ast}$ differ, then for any single $\mathbf{m}$,

$$\|G_1\mathbf{m}-\mathbf{d}_1\|^2 + \|G_2\mathbf{m}-\mathbf{d}_2\|^2
\;\ge\;
\min_{\mathbf{m}}\|G_1\mathbf{m}-\mathbf{d}_1\|^2
+ \min_{\mathbf{m}}\|G_2\mathbf{m}-\mathbf{d}_2\|^2 ,$$

with equality only when the two minimisers coincide. The gap is exactly the
measured inconsistency: chi 7.24 and 5.87 rather than 1 and 1.

---

## ★6 — Two interpretations of a lower error with a higher chi

(i) **Shrinkage.** The wrong reference still reduces variance, and on this
particular synthetic truth the bias it adds is smaller than the variance it
removes. The lower error is a real property of the estimator for *this* truth.

(ii) **Bias.** The model is being pulled towards a known-wrong value; the chi
rise measures the resulting inability to fit the data.

Which can be tested on real data? Only (ii): chi is computable without the truth,
and a chi that grows with $\mu$ shows the model is being pulled away from the
data. Interpretation (i) requires the truth and therefore cannot be used to
justify the coupling in practice.

---

## ★7 — Minimal experiment to test a published joint inversion

Run, with the authors' stated weights and noise:

1. **Chi table** at the published solution: per-datum chi for each data set.
   Decision rule: if any chi $> 2$, the hypothesis "over-coupling or
   inconsistency" is live; if all chi $\approx 1$, weighting dominance is unlikely.
2. **Weight sweep** of $w_1/w_2$ over $10^{-3}$ to $10^{3}$, tracking chi 1,
   chi 2 and the distance to each single-data-set solution. Decision rule: if a
   small change in the weight changes the model by more than its own admitted
   range, the result is dominated by weighting.
3. **Separate inversions** of the two data sets. Decision rule: if the separate
   models disagree by more than their combined uncertainty, the inconsistency is
   in the physics and the joint result is a compromise, not an answer.

Outputs: two tables and a number (the disagreement). Any of the three hypotheses
is falsified by a chi table alone if the chi is at 1, and all three are
distinguishable within one afternoon of compute.

---

## ★8 — Compensating mis-specification

Construction: over-state the noise of the data set that is hard to fit (this
lowers its chi mechanically), under-state the coupling weight at the same time
(this keeps the model from being pulled too far), and choose the coupling
reference to be the *uncoupled* solution of the other data set (which is
consistent with the data by construction). The chi table then shows two values
near 1 while the model is a compromise between two inconsistent data sets.

The diagnostic that still exposes it: the **distance between the separate
inversions**. Compensation can make the joint model look well-fitting, but it
cannot make two inconsistent data sets yield one model — the disagreement
between the separate solutions is independent of the weights chosen in the joint
objective, and it is the number that must be reported.
