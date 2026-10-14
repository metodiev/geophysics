# Solutions — 05-03-01 The Forward Problem: From Model to Data

> Numbers marked *verified* were computed.

---

## ★1

$\mathbf{d} = F[\mathbf{m}] + \boldsymbol{\eta}$, linear case
$\mathbf{d} = \mathbf{G}\mathbf{m} + \boldsymbol{\eta}$. $\mathbf{m}$: model
parameters (kg m⁻³ for density). $\mathbf{d}$: data (m s⁻²). $\mathbf{G}$:
kernel matrix (m³ s⁻² kg⁻¹). $\boldsymbol{\eta}$: noise (m s⁻²).

---

## ★2

$G_{ij} = G\,\Delta V_j\,(z_i-z_j)/|\mathbf{r}_i-\mathbf{r}_j|^3$.
Dimensions: $\mathrm{m^3kg^{-1}s^{-2}\cdot m^3\cdot m\,m^{-3}} =
\mathrm{m^3s^{-2}kg^{-1}}$. ✓

---

## ★3

The forward map integrates; integration is smoothing and stable, so small model
changes produce small data changes and the answer is unique for a given model.
Integration destroys high-wavenumber information, so the inverse map is not
unique: many models give the same data (see the non-uniqueness demonstration).

---

## ★★4 *(verified)*

$G_{11} = G\,\Delta V\,(z_1-z_0)/|\mathbf{r}_1-\mathbf{r}_0|^3$ with
$\Delta V = 200\cdot200\cdot200 = 8\times10^6$ m³ and the cell at
$(0,0,150)$ m (centre): $|\mathbf{r}| = 150$ m, $z_1-z_0 = 150$ m. Then
$G_{11} = (6.6743\times10^{-11})(8\times10^{6})(150)/(150^3)
= (6.6743\times10^{-11})(8\times10^{6})/150^2 = 2.373\times10^{-8}$
m³s⁻²kg⁻¹. Times $\Delta\rho = 500$: $1.1866\times10^{-5}$ m/s²
$= 1.1866$ mGal.

This point-mass approximation overestimates the prism value (1.021214 mGal) by
16%, because the prism is not compact relative to its depth (200 m across at
150 m depth). **The discrepancy is modelling error, not a numerical error**: the
kernel is exact for the approximation, and refining the cell count toward a
finer model would converge to the correct prism value, not to 1.1866.

---

## ★★5

By superposition the total is unchanged for a homogeneous prism — the sum of the
parts equals the whole, exactly. What changes is the *resolution of the model*:
subdividing lets the inversion vary the density cell by cell, which increases
the null space and the ambiguity but does not alter the forward prediction for a
uniform density.

---

## ★★6

The kernel decays as $1/r^2$ and varies smoothly in $x$; two adjacent cells
differ by one cell width, so the change in the kernel is a small fraction of its
value. Hence the corresponding columns of $\mathbf{G}$ are nearly parallel, the
matrix is nearly rank-deficient, and $\mathrm{cond}(\mathbf{G})$ is large — the
mathematical statement of non-uniqueness.

---

## ★★★7

Expected: $\mathrm{cond}(\mathbf{G})$ of order $10^{3}$–$10^{10}$ depending on
the depth-to-spacing ratio, with singular values decaying roughly geometrically.
The number below $10^{-6}\sigma_\text{max}$ is a practical estimate of the
*effective* number of independent parameters: singular values below the noise
level contribute nothing to a stable solution. Report both the count and the
threshold used, and note that the count depends on the noise level, not only on
the geometry.

---

## ★★★8 *(verified)*

Measured relative errors against an $n=200$ reference: $1.19\times10^{-2}$ at
$n=4$, $1.51\times10^{-4}$ at 8, $3.55\times10^{-8}$ at 16, then
$8.46\times10^{-15}$ and $3.98\times10^{-15}$ at 32 and 64. The round-off floor
is $\approx10^{-15}$ relative (double precision), reached between $n = 16$ and
$n = 32$.

Tolerance: adopt $10^{-6}$, two orders of magnitude above the floor and far
below any physical uncertainty. Justification: a tolerance below the floor
cannot be achieved by any implementation, and a tolerance above the physical
uncertainty cannot detect a meaningful error. With a deliberate 2% error
injected, the measured relative error becomes $2.000\times10^{-2}$, which fails
$10^{-6}$ by four orders of magnitude — the test has demonstrated its own
sensitivity.
---

## ★★★9

**Measured values** for $n_o = 120$ observations over 12 km, $n_s = 400$ cells
($\Delta x \approx 30$ m) at 300 m depth:

| quantity | value |
|---|---|
| diagonal $R_{ii}$ at the central cell | **0.2834** |
| row sum $\sum_j R_{ij}$ | 3.53 cells $= 106$ m |
| largest off-diagonal $\lvert R_{ij}\rvert$, $j\ne i$ | 0.9304 |
| resolution width / depth | $106/300 = 0.35$ |

**How much is recovered, and where the rest goes.** The diagonal is 0.28, so the
estimate of the central cell is only 28% of its true value; the remaining 72% is
distributed over the neighbouring cells, dominated by the two adjacent cells
(0.93 of the cell's own value each, before normalisation). The estimate is
therefore a *weighted average of about 3.5 cells' worth of true model*, centred on
the cell of interest — a smeared value, not a local one.

**Why the resolution width is narrower than the anomaly half-width.** The anomaly
half-width is $1.532842\,d = 460$ m, whereas the resolution width is
$0.35\,d = 106$ m — a factor of 4.3 narrower. The reason is that $\mathbf{R}$ is a
property of the *inverse operator*, not of the forward kernel: the pseudoinverse
inverts the (band-limited) forward mapping as far as the data's conditioning
allows, sharpening the averaging kernel below the anomaly width. It cannot
sharpen it below the noise-limited resolution, which is why the improvement is a
factor of a few rather than orders of magnitude.

**Which change raises the diagonal most — argued from structure.** $R_{ii}$
decreases as the columns of $\mathbf{G}$ become more parallel, and Section 3.2
measured $1-\cos\theta \approx 0.25(\Delta x/d)^2$. Two structural levers follow:

1. **Coarser model cells** raise $R_{ii}$ (fewer, more distinguishable columns)
   but lose spatial detail — the classic resolution/parameterisation trade.
2. **Observations off the source footprint** separate the columns more than
   observations directly above, because the kernel's dependence on cell position
   varies faster at large horizontal offset.

Of the two, adding off-edge observations raises the diagonal without coarsening the
model, so it is the better change — and that conclusion comes from the structure of
$\mathbf{G}$ (the angle between columns) rather than from a sweep of parameters.
