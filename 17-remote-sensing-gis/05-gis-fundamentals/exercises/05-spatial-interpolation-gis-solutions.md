# Solutions — 17-05-05 Spatial Interpolation: IDW, Kriging, Splines

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [05 Spatial Interpolation](../05-spatial-interpolation-gis.md).

---

## ★1 — IDW with three samples

Weights $w_i = d_i^{-2}$:

$$w = (1.0,\ 0.25,\ 0.0625), \qquad \sum w = 1.3125,$$
$$z^* = \frac{1.0(10) + 0.25(14) + 0.0625(16)}{1.3125}
= \frac{10 + 3.5 + 1.0}{1.3125} = \frac{14.5}{1.3125} = \mathbf{11.05}.$$

The weights are inverse square kilometres (km⁻²), so they are **not**
dimensionless; only their ratio is. That is why the normalised form
$w_i/\sum w_j$ is the one to write down.

---

## ★2 — Spherical variogram

$$\gamma(h) = c_0 + c\left(\frac{3h}{2a} - \frac{h^3}{2a^3}\right),\qquad h < a;$$

* $h = 0$: $\gamma = c_0 = \mathbf{0.3}$.
* $h = 3$ km, $a = 6$ km, $h/a = 0.5$:
  $3(0.5)/2 - 0.5^3/2 = 0.75 - 0.0625 = 0.6875$, so
  $\gamma = 0.3 + 1.2(0.6875) = \mathbf{1.125}$.
* $h = 9$ km $> a$: $\gamma = c_0 + c = \mathbf{1.5}$ (the sill).

---

## ★3 — Expectations

$$E[C] = 1, \qquad E[I] = -\frac{1}{n-1} = -\frac{1}{249} = -0.004016.$$

Both are expectations under no autocorrelation *with the stated weights*; the
weights must accompany the statistic.

---

## ★4 — Two standard deviations from one variogram

Sill $= c_0 + c = 0.25 + 2.0 = 2.25\ (\mathrm{mg/kg})^2$, so the stationary
standard deviation is $\sqrt{2.25} = \mathbf{1.5\ mg/kg}$.

At 8 km, beyond the 5 km range, $\gamma(h) = c_0 + c = 2.25$ for every sample, and
with a single dominant neighbour the ordinary-kriging variance tends to

$$\sigma^2_{OK} \to c_0 + c = 2.25\ (\mathrm{mg/kg})^2
\qquad\Longrightarrow\qquad \sigma_{OK} = \mathbf{1.5\ mg/kg}.$$

The ratio is 1.0: beyond the range the estimator reports the mean with the
stationary standard deviation, which is the honest statement "no information
here". Inside the range the variance is smaller, and it is exactly zero at a
sample because $\gamma(0) = 0$ in this convention.

---

## ★5 — Two models, similar fits

Sills: $0.1 + 0.9 = 1.0$ and $0.3 + 0.75 = 1.05$ — within 5 %. The nugget differs
by a factor of 3 and the range by 1.75×.

The variogram alone cannot resolve the difference: the demonstration measured a
similar pair at a misfit ratio of 1.17 and found their kriged surfaces differing
by up to 0.64 of a residual standard deviation, with validation errors against a
known truth differing by 12 % and kriging variances by 19 %. What resolves it is
**independent validation** — a withheld subset, a known truth, or an independent
measurement — not a better fit to the same variogram.

---

## ★6 — Declustering a clustered survey

Thirty of forty samples inside a 2 km box means most pairs are short-lag pairs, so
the empirical variogram is a weighted average dominated by the cluster. At short
lags the bias depends on whether the cluster sits in a locally high-variance area:
if it does, short-lag $\gamma$ is biased **high** and the fitted nugget plus
partial sill is inflated for that scale; if it sits in a locally smooth area, the
short-lag $\gamma$ is biased **low**. The general effect is a *distortion of the
shape* rather than a consistent sign, which is why the correction is applied
before fitting rather than to the fitted parameters.

Correction: **cell declustering** — weight each sample by the inverse of the number
of samples sharing its declustering cell, normalised to sum to the sample count.
The experiment in the lesson used 1.5 km cells, giving a weight range of
[0.1595, 9.0909] for 400 samples at a maximum of 57 per cell.

One reported number: the ratio of the declustered to the evenly-sampled variogram
at the long-lag bins. In the lesson these ratios fell from 1.443 to 1.063 across
the long-lag bins after correction (the last bin, 0.799, had only 1 339 pairs and
is dominated by sampling error), showing the correction moving the clustered curve
towards the reference.

---

## ★7 — Halving the kriging variance

For ordinary kriging with a single dominant neighbour at distance $d$, the
kriging variance is approximately

$$\sigma^2_{OK} \approx 2\gamma(d) - \gamma(0) - \text{(a term from the Lagrange
multiplier)} \approx 2\gamma(d)\ \text{for a far-field target,}$$

so halving $\sigma^2$ means reducing $\gamma(d)$ by a factor of two. For a
spherical model with range $a$, that is achieved by placing a sample at a distance
$d'$ satisfying

$$\gamma(d') = \tfrac12 \gamma(d)
\quad\Longrightarrow\quad
d' \approx 0.35\,a\ \text{for a nugget-free model}
\ \left(\text{solving } \tfrac{3x}{2} - \tfrac{x^3}{2} = 0.5\right),$$

i.e. $d' \approx 0.35 \times 5\ \mathrm{km} = 1.75$ km for the lesson's model.
Cost: **one sample placed at the target region's edge**, not a new campaign,
provided the target is within a range of the existing network. If the target is
beyond $a$, no finite number of samples inside the old network helps; samples must
be placed around the target, and the cost is the number needed to cover the
neighbourhood within $a$ at the desired spacing, roughly
$(\pi (0.35 a)^2)/(\text{target spacing})^2$ samples.

---

## ★8 — A range without an uncertainty

The response should specify that a variogram range is usable only with: (i) the
**model family** (spherical, exponential, Matérn with its smoothness parameter),
(ii) the **other parameters** — nugget $c_0$ and partial sill $c$ — because the
three are jointly non-unique, (iii) the **fitting criterion** (pair-weighted least
squares, maximum likelihood, binned ordinates) and the lag binning, (iv) the
**sampling design**, because clustering biases the variogram, (v) the **misfit
surface**, or at least the set of parameter combinations within a stated
tolerance of the best fit.

The experiment that puts a range on the range: fit the model on many bootstrap or
block-resampled subsets of the samples, or on many conditional simulations drawn
from the fitted model, and report the 5–95 % interval of the range. The lesson's
valley measurement is the deterministic version of the same statement: parameter
sets 23 % worse in misfit differed in range by more than a factor of two, so the
interval is wide, and reporting a point value hides it.
