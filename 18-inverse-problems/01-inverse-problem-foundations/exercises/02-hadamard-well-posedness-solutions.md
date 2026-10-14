# Solutions — 18-01-02 Hadamard's Conditions: Existence, Uniqueness, Stability

> **Read after attempting the exercises.** Lesson:
> [02 Hadamard's Conditions](../02-hadamard-well-posedness.md).

---

## ★1 — The three conditions

1. **Existence** — fails when the data contain structure the parameterisation
   cannot express (e.g. a deep source interpreted with shallow blocks, or 3-D
   structure inverted with a 1-D model).
2. **Uniqueness** — fails when the model has directions to which the experiment is
   blind (e.g. vertical density distribution from surface gravity alone; a
   low-velocity zone traded against layer thickness in travel-time inversion).
3. **Stability** — fails when the inverse map is unbounded (e.g. differentiating
   potentials or travel times; downward continuation of potential fields).

---

## ★2 — Rank of the layered kernel

Each layer contributes $c\rho_k h$ and the single reading is
$c\sum_k\rho_k$: every row of $G$ is the constant vector $c$, so
$\operatorname{rank}(G) = 1$ and

$$\dim\mathcal{N}(G) = 12-1 = 11.$$

Adding $5$ independent borehole levels gives $6$ rows and the demonstration
measures rank $6$, so $\dim\mathcal{N}(G) = 12-6 = 6$.

---

## ★3 — Two stacks with the same gravity

Uniform: $g = c\sum_k \rho_k = 0.04193586\times12\times100
= 50.323036\ \mathrm{mGal}$.

Alternating: $\sum_k \rho_k = 6\times(150) + 6\times(50) = 1200$, the same sum,
so $g = 50.323036\ \mathrm{mGal}$ again — **identical**. The difference vector is
$\pm50\ \mathrm{kg\,m^{-3}}$ in every layer with total sum zero, i.e. a null-space
vector. This is the arithmetic behind
[18-01-03 §5](../03-null-space.md).

---

## ★4 — Existence

(a) $\lVert\mathbf{r}\rVert/\lVert\mathbf{e}\rVert = 1.537876\times10^{-3} /
8.4\times10^{-6} = 183.1$ (the demonstration printed $182.3$ using the exact noise
norm of that realisation; either way it is of order $2\times10^{2}$).

(b) No. A misfit $183$ times the noise means the best model in the space is
inadequate, not merely noisy: $\mathbf{d}\notin\operatorname{range}(G)$ at any
tolerable error level.

(c) Two options: (i) extend the model space to include the depths of the true
source ($8$ and $12\ \mathrm{km}$); (ii) change the experiment so the data have
shorter-wavelength information that only the deep structure can produce.

---

## ★5 — Differentiation error

(a) $h = 10^{-1}$: truncation dominates ($9.005\times10^{-4}$ against a noise term
$10^{-5}$). $h = 10^{-2}$: the two are comparable ($9.0\times10^{-6}$ against
$10^{-4}$) and the measured $1.425\times10^{-5}$ sits near the crossover.
$h = 10^{-3}$: noise dominates ($10^{-3}$ against a truncation
$9.0\times10^{-8}$).

(b) Setting $\cos(1)h^{2}/6 = \varepsilon/h$ with $\varepsilon = 10^{-6}$ and
$\cos 1 = 0.5403023$:

$$h^{3} = \frac{6\varepsilon}{\cos 1} = \frac{6\times10^{-6}}{0.5403023}
= 1.1105\times10^{-5},\qquad h = 0.0223 .$$

Observed minimum: between $10^{-2}$ and $3\times10^{-2}$ — consistent.

---

## ★6 — Non-monotonicity at the finest grid

$\kappa$ grows while $\sigma_{\min}$ remains resolvable. At $M = 64$ the smallest
singular value is $1.5579\times10^{-34}$, which is *below*
$\varepsilon\sigma_{\max} = 1.357\times10^{-27}$: the value is at the rounding
floor of the computation, and the reported ratio is not a property of the
discretised problem. The correct statement is that the growth continues until it
becomes unrepresentable; the checker at $M=64$ cannot resolve it.

---

## ★7 — Specification for a tolerance-dependent null space

**Report:** the singular spectrum (relative values), the numerical rank at the
declared tolerance, and the number of directions below it — not "the null space".

**Tolerance:** the relative singular value below which a direction carries less
information than the data error. With data accurate to a relative level $\tau$,
the model error contributed by direction $i$ scales as
$\lVert\mathbf{e}\rVert/(\sigma_i\lVert\mathbf{d}\rVert)$, so a workable rule is
$\sigma_i/\sigma_1 > \tau$; the demonstration of
[18-01-02 §6](../02-hadamard-well-posedness.md) used $10^{-10}$ for essentially
noise-free algebra and $10^{-4}$–$10^{-6}$ for percent-level data.

**Sensitivity statement:** the rank is $1+4=5$ directions above $\tau = 10^{-6}$
(those $\ge 10^{-6}$: $1, 10^{-1}, 10^{-2.5}, 10^{-4}$; $10^{-6}$ at the
boundary) and 6 above $\tau = 10^{-10}$, so the unresolved dimension is between 2
and 3. A conclusion that changes between these two is a conclusion you cannot
defend; report it as conditional on the tolerance.

---

## ★★★8 — A measurement plan with null space at most 2

**Rows of $G$** (using $z_c$ = layer centres, slab convention of the lesson):

1. surface gravity: $G_{1k} = c$ for all $k$;
2. borehole gravity at a depth in each layer boundary for $k = 2,\dots,11$, giving
   rows $G_{jk} = c\,\operatorname{sign}(z_{k} - d_j)$;
3. a vertical gravity gradient reading at a single depth, which weights layers by
   their distance from the sensor and so is linearly independent of the sign rows.

Ten distinct borehole depths plus the surface reading give $11$ rows; add the
gradient and there are $12$ rows for $12$ layers. Rank $=12$ if all rows are
independent, so the null space would be $0$; a design with $10$ rows gives rank
$10$ and null dimension $2$, the target.

**Invalidating assumption:** that the layers are *exactly* horizontal and
infinite. Any finite lateral extent or dip makes the slab rows wrong, and the
count — which depends on the sign pattern being exactly $\pm c$ — collapses. The
second candidate assumption: that the sensor depths are known exactly; unknown
depths make the kernel nonlinear and the counting argument inapplicable.
