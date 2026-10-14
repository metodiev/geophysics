# Solutions — 19-05-03 Numerical Green's Functions and Their Computation

> **Read after attempting the exercises.** Numbers are computed from the printed
> demonstration outputs. All models are **SYNTHETIC**.

Lesson: [03 Numerical Green's Functions and Their Computation](../03-greens-function-numerics.md).

---

## ★1 — The tent function at five nodes

With $L = 1$ and $x_0 = 0.5$: for $x \le x_0$, $G = x(1-x_0)/1 = 0.5x$; for
$x > x_0$, $G = x_0(1-x) = 0.5(1-x)$.

| $x$ | 0.1 | 0.3 | 0.5 | 0.7 | 0.9 |
|---|---|---|---|---|---|
| $G$ | 0.05 | 0.15 | **0.25** | 0.15 | 0.05 |

The value at the source is $0.25 = x_0(1-x_0)/L$, and the function is symmetric
about it. The discrete operator applied at $x = 0.5$ with $h = 0.2$ gives
$(0.15 - 2(0.25) + 0.15)/h^{2} = (-0.2)/0.04 = -5$, so
$-G'' \to +5 = 1/h$ at the source node with $h = 0.2$, i.e. the source strength
$1/h$ ✔.

---

## ★2 — The self integral

$$\int_{0}^{1}\ln\left|t-\tfrac12\right|\mathrm{d}t
= 2\int_{0}^{1/2}\ln t\,\mathrm{d}t
= 2\left[\frac12\ln\frac12 - \frac12\right]
= \ln\frac12 - 1 = -1.6931 .$$

The sign is negative, as it must be: $\ln|t-\tfrac12| < 0$ almost everywhere on
$(0,1)$. In the general-length form this is $L(\ln(L/2)-1)$, the expression used
for $G_{ii}$ in [02 Boundary Element Methods](../02-boundary-element.md); the
$-1$ term is what keeps the result finite.

---

## ★3 — Why 1-D is exact and 2-D is not

In 1-D, the exact Green's function of $-u''$ is piecewise linear, and the space of
functions that are linear between nodes is closed under the second-difference
operator: the operator annihilates every such function except at the kink, where
it produces $1/h$. The exact solution therefore lies in the discrete space.

In 2-D, the exact kernel is $\ln r$, which is *not* annihilated by the five-point
Laplacian. Applying the stencil to $\ln r$ leaves a non-zero residual of order
$h^{2}$ times the fourth derivative, so the discrete solution differs from the
continuous one at $O(h^{2})$. The exactness in 1-D is a coincidence of the
one-dimensional stencil, not a general property of Green's functions.

---

## ★4 — The lumped-source error law

$h_{128} = 1/129 = 7.752\times10^{-3}$, $h_{512} = 1/513 = 1.949\times10^{-3}$.

$$C = \frac{E}{h} = \frac{1.923\times10^{-3}}{7.752\times10^{-3}} = 0.2481,
\qquad \frac{4.864\times10^{-4}}{1.949\times10^{-3}} = 0.2495 .$$

The constant is stable at about $0.2495$ and converging to $0.25$, so
$E \approx 0.25\,h$. The interpretation: lumping places the source half a cell
away from its true position on average, and the tent function's response to a
source displacement $\delta$ is linear in $\delta$ — hence a first-order error
with the $\tfrac14$ coefficient coming from the average offset. The demo's printed
ratio column shows this convergence explicitly.

---

## ★5 — The monopole estimate

$$\frac{M_0}{|y-c|} = \frac{404.726574}{2.5 - 0.498564} = \frac{404.726574}{2.001436}
= 202.218080,$$

matching the printed $202.2180799309$ to ten figures ✔. The relative error against
the exact $205.6370151508$ is

$$\frac{|202.218080 - 205.637015|}{205.637015} = 1.663\times10^{-2},$$

the printed $1.663\times10^{-2}$: the entire discrepancy is the dipole and
quadrupole of a source distribution spanning $0.99$ km seen from $2.0$ km.

---

## ★6 — Order and prediction

Error ratio $7.124\times10^{-2}/1.764\times10^{-2} = 4.038$ for a halving of $h$,
so the order is $\log_{2}4.038 = 2.01$.

At $h = 0.0625$ km, $h$ falls by another factor of $4$ from $0.25$ km, so the
error should fall by $4^{2} = 16$:
$1.764\times10^{-2}/16 = 1.1\times10^{-3}$. The demonstration reports
$4.399\times10^{-3}$ at $h = 0.125$ km, and $4.399\times10^{-3}/4 =
1.1\times10^{-3}$ at $h = 0.0625$ km ✔ consistent with the order $2.00$ measured
at the finest pair.

---

## ★7 — Why the increments converge from below

The measured increments $0.10959$, $0.11017$, $0.11043$ increase towards
$0.110318$? No — they increase towards a value *slightly above*
$0.11032$: $0.11043 > 0.110318$. The sequence is rising and the limit is the
analytic increment $\frac{1}{2\pi}\ln2$ plus a grid-error correction.

Since the grid error on $G$ is $O(h^{2})$ with some sign, and $h = L/1024$ grows
with $L$ in this experiment, the correction scales as $L^{2}$: it is *larger* for
larger $L$, which is why the increments rise above the analytic value and would
fall back as the grid is refined at fixed $L$. The sign of the deviation is thus
a statement about the sign of the $O(h^{2})$ constant for $\ln r$ under this
stencil — measured here as positive — and an experimenter who wants the clean
constant must refine at fixed $L$ instead of varying $L$.

---

## ★8 — Mass normalisation or symbol?

- **Source-mass normalisation:** the whole kernel scales by a constant factor, so
  every *value* changes but every *difference* and every *ratio of values* does
  not. Observable: compare $G$ with $10^{3}\times$ the kernel; the ratio is
  constant in $r$ if the mass is wrong.
- **Grid symbol:** the error is $r$-dependent and vanishes as $h\to0$; it changes
  differences and ratios.

The experiment: (i) check the mass by comparing the far-field monopole
$G(r) \approx \frac{1}{2\pi}\ln(1/r)$ against the lattice value at a fixed large
$r$, where the symbol error is negligible; (ii) refine $h$ at fixed physical
$r$: if the error falls at second order, it is the symbol; if it is unchanged, it
is a constant factor and the mass is the suspect. The lesson's screened table is
exactly test (ii), and the mass test is saved by the cell-mass convention
$1/h^{2}$, whose omission produces a *first-order-looking* convergence because
the kernel scales with $h^{2}$.
