# Solutions — 17-07-02 Cloud Platforms: GEE, Copernicus, NASA Earthdata

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All values are **SYNTHETIC** teaching numbers.

Lesson: [02 Cloud Platforms](../02-cloud-platforms.md).

---

## ★1 — Reducer

A reducer is any function mapping a stack of observations to an output array. In
the lesson the temporal **median** is the reducer. Reducing at source differs in
that the *reducer runs where the data lives*, so the mask, compositor and
resampler are executed by the platform on your behalf and become part of your
method — they must be recorded to make the result reproducible.

---

## ★2 — Version shift

$$
\Delta = 0.2901 - 0.2801 = +0.0100, \qquad
\frac{0.0100}{0.2801} \times 100\% = +3.57\%.
$$

---

## ★3 — Clear counts

True clouds $= 0.25 \times 60 = 15$. Detected (flagged) clouds
$= 0.80 \times 15 = 12$. Flagged clear $= 60 - 12 = 48$. Actually clear
$= 60 - 15 = 45$. The mask over-counts clear looks by $48 - 45 = 3$
observations.

---

## ★4 — Volumes

Full stack $= 5000^2 \times 100 \times 4 \times 2
= 2.0\times10^{10}$ bytes $= 20.0$ GB (decimal).

Summary $= 5000^2 \times 2 = 5.0\times10^{7}$ bytes $= 50.0$ MB.

Ratio $= 2.0\times10^{10} / 5.0\times10^{7} = 400:1$.

---

## ★5 — How much does the mask help?

Bias: $(0.0397 - 0.0211)/0.0397 = 0.469$, i.e. a **$46.9\%$** reduction.

RMS: $(0.0743 - 0.0600)/0.0743 = 0.192$, i.e. a **$19.2\%$** reduction.

The mask removes nearly half the *bias* but only a fifth of the *RMS* error,
because the residual RMS is dominated by the persistently cloudy corner where
the mask's false negatives let bright clouds through. Reporting only "the mask
halves the error" would overstate it; both numbers are needed.

---

## ★6 — Why a median fails past 50%

The median is the middle **order statistic**: it equals a clean value as long as
fewer than half the samples are outliers, so it tolerates a *fraction* of
contamination below $0.5$. Once cloud cover exceeds $50\%$, a majority of
samples are bright, and the middle sample is itself a cloud; no order-statistic
choice recovers the truth without an accurate mask.

---

## ★7 — Download versus reduce (specification)

- **Task.** Produce a monthly surface-reflectance composite for a stated region
  at a stated grid.
- **Quantities.** For *download*: bytes moved, plus the number of times the whole
  stack must be re-fetched while the mask or compositor is tuned (call it $m$).
  For *reduce*: bytes returned, plus the platform's per-request cost and the
  loss of ability to vary the reducer without re-running.
- **Break-even.** Choose download when
  $m \times \text{full-bytes}$ is affordable and interactive mask tuning is
  required; choose reduce when the reducer is fixed and
  full-bytes $\times m$ exceeds quota or budget.
- **Confounds.** Quota and rate limits; latency of a large local download;
  the fact that a fixed reducer may be wrong and need re-running; and governance
  (who may see the pixels). A specification that ignores these is not
  executable.

---

## ★8 — Floating-point order dependence

Floating-point addition is not associative: $(a+b)+c$ can differ from
$a+(b+c)$ in the last bits, and a distributed mean sums chunks in an order that
may vary with scheduling. The result is a difference at the round-off level
(relative error of order $10^{-16}$ per operation, growing with the number of
terms), not a scientific difference. A reproducible study should report the
result to an appropriate precision, fix the reduction where possible (a
deterministic reducer), record the platform and version, and check that the
conclusion is insensitive to a change smaller than the round-off —
otherwise the study is reporting noise in the last digits as a result.
