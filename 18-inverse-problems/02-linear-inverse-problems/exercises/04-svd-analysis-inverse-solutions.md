# Solutions — 18-02-04 SVD Analysis: Model Resolution and Data Importance

> **Read after attempting the exercises.** Lesson:
> [04 SVD Analysis](../04-svd-analysis-inverse.md).

---

## ★1 — Triplets and estimator

$\mathbf{v}_i$ is a pattern in model space, $\mathbf{u}_i$ the data pattern it
produces, $\sigma_i$ the gain (data amplitude per unit model amplitude). The
rank-$k$ estimator is

$$\hat{\mathbf{m}}_k = \sum_{i=1}^{k}
\frac{\mathbf{u}_i^{\!\top}\mathbf{d}}{\sigma_i}\,\mathbf{v}_i .$$

---

## ★2 — Importance of duplicates

Measured: exact duplicates split the importance of the duplicated direction evenly,
so rays 1 and 9 carry $0.500$ each, rays 4 and 10 $0.500$ each, rays 8 and 12
$0.500$ each. The half-amplitude copy (ray 11) carries $0.200$ while its twin
(ray 2) keeps $0.800$ (importance is proportional to the squared row scaling
ratio: $0.5^{2}/(1+0.5^{2}) = 0.2$). The full sum is
$8.000000 = \operatorname{rank}(G)$.

---

## ★3 — Noise growth

Ratio $= 7.503\times10^{-3}/5.36\times10^{-4} = 14.0$. The estimator's variance in
direction $i$ is $\sigma^{2}/\sigma_i^{2}$, and the last retained singular value is
$\sigma_8 = 0.269359$ against $\sigma_1 = 2.69260$, a ratio of $0.100$; its squared
reciprocal is $100$, which dominates the sum. Truncating to $k=8$ includes the
noisiest direction the experiment has.

---

## ★4 — Trace and rank

(a) $\operatorname{tr}R = 8$: eight independent model combinations.
(b) $\operatorname{mean}\operatorname{diag}R = 8/12 = 0.6667$.
(c) Adding one independent ray raises the rank to $9$, so $\operatorname{tr}R = 9$,
$\operatorname{mean}\operatorname{diag}R = 0.75$, and
$\dim\mathcal{N}(G)$ falls from $4$ to $3$.

---

## ★5 — Self-resolution versus width

(a) Cell 3: the narrower kernel (2.44 km) means the estimate at cell 3 is a
localised average, so a statement about that neighbourhood is defensible. Cell 0's
4.43 km kernel means any "value at cell 0" is an average reaching 4.4 km into the
model.

(b) $R_{jj}$ measures how much of the true value at cell $j$ survives filtering —
i.e. inverse bias — not how localised the estimate is. Cell 0 has the largest
$R_{jj}$ (0.8182) *and* the widest kernel: a numerically faithful but spatially
smeared estimate. Quoting $R_{jj}$ alone therefore makes the worst-resolved cells
look like the best.

---

## ★6 — Bias versus noise

(a) The bias dominates by a factor $0.368770/0.025992 = 14.2$.

(b) A rough prediction: rms per-cell error
$\approx\sqrt{(0.368770^{2}+0.025992^{2})/12} = \sqrt{(0.135992+0.000676)/12}
= \sqrt{0.011389} = 0.10672\ \mathrm{s}$.

(c) The measured value $0.101661\ \mathrm{s}$ is within $4.7\%$ of that estimate.
The small difference is because the bias is not spread uniformly over cells (it is
larger where the kernel is wide), so an rms over cells is not simply
bias-norm$/\sqrt{12}$; the exact prediction used in the lesson computes the
per-cell bias explicitly and gives $0.101689\ \mathrm{s}$, matching the measurement
to $0.03\%$.

---

## ★★★7 — Choosing k with an estimated sigma

**Estimand.** The noise level $\sigma$, estimated either from repeat measurements
(preferred) or from the residual at a truncation level known to be safely large,
with the caveat that residual-based estimates are biased under correlated noise
([18-02-06 §7](../06-weighting-and-covariance.md)).

**Criterion.** Choose $k$ minimising the *predicted* mean-square error

$$\widehat{\text{MSE}}(k) = \operatorname{mean}_j\left[(R_k\mathbf{m}_0
-\mathbf{m}_0)_j\right]^{2} + \hat{\sigma}^{2}\,\operatorname{mean}_j
\sum_{i\le k}\frac{V_{ji}^{2}}{\sigma_i^{2}},$$

using a reference model $\mathbf{m}_0$ (a smooth prior model) for the bias term, or
alternatively the discrepancy principle
$\lVert G\hat{\mathbf{m}}_k-\mathbf{d}\rVert \approx \sqrt{N}\hat{\sigma}$. State
which criterion you used; they do not always agree.

**Flat curves.** The demonstration's high-noise curve has
$0.114807$ at $k=5$ versus $0.117013$ at $k=6$: within $2\%$. When the curve is
flat, report the *range* of $k$ with errors within, say, $5\%$ of the minimum
(here $k = 4$–$6$), and state that the choice within that range changes nothing
material — that is more informative than a spurious "optimal $k$".

---

## ★★★8 — A five-ray D-optimal addition

**Geometry.** The unresolved structure is cells 10–11 (never sampled) and the
central cells 2–3 (smallest $R_{jj}$). Add rays that (i) cover cells 10–11 and
(ii) add an independent crossing pattern over cells 2–4, e.g.

1. cells 10, 11 with weights $(0.7, 1.0)$;
2. cells 9, 10, 11 with weights $(0.6, 1.0, 0.6)$;
3. cells 2, 3 with weights $(1.0, 0.7)$;
4. cells 1, 2, 3 with weights $(0.6, 1.0, 0.6)$ shifted one cell from the existing
   ray 2;
5. cells 3, 4 with weights $(0.7, 1.0)$.

**Predicted change.** These five rows are linearly independent of the existing
eight (they sample cells 10–11, which currently have zero columns) so the rank rises
from 8 to 13, but the model has only 12 cells, so the rank saturates at 12 and
$\dim\mathcal{N}(G)$ falls from 4 to 0: every cell becomes formally determined.
$\operatorname{tr}R$ rises from $8$ to $12$, i.e. $R = I$, and the mean kernel width
falls sharply.

**Assumption.** That the forward model for a ray over cells 10–11 is the same
weighted-sum operator as for the others — i.e. that the extended geometry is
physically accessible (a source and receiver can be placed to illuminate those
cells). If it is not, the design is a fiction, and the honest conclusion is that
those cells cannot be resolved.
