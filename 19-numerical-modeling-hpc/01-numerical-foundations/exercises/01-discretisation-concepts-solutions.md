# Solutions — 19-01-01 Discretisation: Grids, Nodes, Cells and Degrees of Freedom

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand, where arithmetic beyond two significant figures was needed.

Lesson: [01 Discretisation](../01-discretisation-concepts.md).

---

## ★1 — Counts on a line

$h = L/N = 800/160 = 5$ m. Cell centres: 160. Nodes: 161. DOF: 160
cell-centred, 161 node-centred. The relative difference is $1/161 = 0.62\,\%$.

---

## ★2 — Two fields in 2-D

Unknowns: $400\times250 = 100\,000$ per field, so $200\,000$ for two fields.
Storage: $200\,000\times8$ bytes $= 1.6\times10^{6}$ bytes
$= 1.526$ MiB.

---

## ★3 — Quadrature errors for $x^{2}$

Exact integral: $\int_0^1 x^{2}\mathrm dx = 1/3 = 0.3333333333$.

Midpoint, $N = 50$, $h = 0.02$:

$$h\sum_{i=0}^{49}(x_{i+1/2})^{2}
= \frac{1}{3} - \frac{h^{2}}{12} = \frac{1}{3} - 3.3333\times10^{-5}
= 0.3333000000,$$

error $-3.333\times10^{-5}$. Trapezoid:

$$h\left[\tfrac12 g(0)+\sum_{i=1}^{49}g(x_i)+\tfrac12 g(1)\right]
= \frac{1}{3} + \frac{h^{2}}{6} = 0.3334000000,$$

error $+6.667\times10^{-5}$. The trapezoid error is exactly twice the midpoint
error and of opposite sign, for this integrand and any $N$.

---

## ★4 — A 3-D acoustic state

Cells: $480\times480\times200 = 4.608\times10^{7}$. Pressure: $4.608\times10^{7}$
DOF. Velocity: $3\times4.608\times10^{7} = 1.3824\times10^{8}$ DOF. Total
$1.8432\times10^{8}$ DOF.

Memory at 8 bytes: $1.4746\times10^{9}$ bytes $= 1406$ MiB $\approx 1.37$ GiB.

An explicit second-order-in-time scheme needs the current and previous states
plus at least one work array, i.e. three copies: about $4.1$ GiB. This is the
number that decides whether the run is possible, and it is available before a
line of code is written.

---

## ★5 — Series column with two averaging rules

Exact: $\kappa_{\text{eff}} = 1.2\big/(0.45/2.0 + 0.75/6.0)
= 1.2/(0.225 + 0.125) = 1.2/0.35 = 3.428571\ \mathrm{W\,m^{-1}\,K^{-1}}$.
Exact flux: $q = \Delta T/(0.225+0.125) = 80/0.35 = 228.571429\
\mathrm{W\,m^{-2}}$.

Cell-centred, harmonic face conductivity at the jump:
$2(2)(6)/(2+6) = 3.0$, which reproduces the series argument exactly, so the
computed flux equals $228.571429\ \mathrm{W\,m^{-2}}$ to round-off (the
demonstration measures $-2.8\times10^{-13}\,\%$ on its own column).

Node-centred, arithmetic averaging: the face sees $0.5(2+6) = 4.0$, i.e.
$33\,\%$ too large, and the flux is correspondingly too large — the measured
example in the lesson gave $+2.804\,\%$; for the two-value column here the error
is larger because the contrast is bigger. The exact magnitude depends on the
grid, which is the point: the error does not vanish under refinement.

---

## ★6 — The discrete-norm bias

Squared discrete norm: $h\sum_i (x_{i+1/2})^{4}$, the midpoint rule for
$\int_0^1 x^{4}\mathrm dx$ with error
$\dfrac{h^{2}}{24}\left[g'(1)-g'(0)\right]$, $g = x^{4}$,
$g'(1)-g'(0) = 4$: error $= h^{2}/6$.

Taking square roots: $\|f_h\| - \|f\| \approx \dfrac{h^{2}/6}{2\|f\|}
= \dfrac{h^{2}}{12\sqrt{1/5}} = 0.1863390\,h^{2}$.

Sign: positive, because the squared norm is biased high and the square root
preserves the sign. The measured values are $0.1863400$ at $N = 80$ and
$0.1863391$ at $N = 320$ — the last two digits are still moving towards
$0.1863390$ because the next Euler–Maclaurin term is $O(h^{4})$.

---

## ★7 — Three materials in series

**Placement.** Unknowns (temperature) at cell centres; conductivities also at
cell centres, with the two interfaces placed exactly on cell faces by choosing
$N$ with $0.3N$ and $0.7N$ integers (for example $N = 40$). Face conductivity
between two adjacent cells $A$, $B$: harmonic mean
$2\kappa_A\kappa_B/(\kappa_A+\kappa_B)$; faces inside a single material inherit
that material's value.

**Exact reference.** For unit area,
$q = \Delta T\big/\sum_i t_i/\kappa_i$ with
$t_1 = 0.3L$, $t_2 = 0.4L$, $t_3 = 0.3L$. With $L = 1$ m and
$\Delta T = 1$ K:
$q = 1/(0.3/1 + 0.4/4 + 0.3/20) = 1/(0.3+0.1+0.015) = 1/0.415 = 2.409639$.

**Verification.** (i) Solve the discrete steady problem with the wall conditions
imposed at half a cell; (ii) compute the flux from the first pair of cells;
(iii) compare with $2.409639$. The claim is that the agreement is at round-off
level. A second check is to refine by a factor of two (keeping the interfaces on
faces) and confirm the flux does not change.

**When interfaces miss cell faces.** The interface then lies inside a cell whose
conductivity is ambiguous; the natural choice (assign the cell to the material
containing its centre) produces an effective material boundary displaced by up to
$h/2$ and an $O(h)$ error in the layer thickness — a *first-order* error in the
flux, not a second-order one. The measured remedy is to snap the interface to the
nearest face, which restores the exactness of the series argument at the cost of
a grid that is not exactly on the requested geometry.

---

## ★8 — Is the coarsest acceptable grid the best one?

**Where it is right.** If the only cost considered is the linear solve, refining
does worsen the conditioning ($\kappa \propto h^{-2}$) and the iteration count
($O(h^{-1})$ for CG). On a fixed accuracy budget there is indeed an optimum
resolution, and it is not the finest one.

**Where it is wrong.** (i) The discretisation error is the *accuracy* the user
asked for; making it worse to speed up the solve is a different trade, not a
free optimisation. (ii) The claim ignores accuracy *per unit time*: at fixed
tolerance CG's total cost is
(iterations) $\times$ (work per iteration) $= O(h^{-1})\times O(N\log N)$, which
still grows with $N$, but the right-hand side of the trade is the *error*
achieved, so the comparison must be cost-versus-error and not cost alone.
(iii) Preconditioning changes the exponent; a multigrid-preconditioned CG
converges in $O(1)$ iterations and the whole argument disappears.

**The deciding quantity.** The quantity that decides it is the *solver's cost at
fixed accuracy*, i.e. the product of the iteration count and the error, not
either alone. The demonstration supplies the ingredients: the measured constant
$\pi^{2}/12$ converts resolution into error, and the measured exponents (1.013
for CG, 1.957 for Jacobi) convert resolution into iterations. With those two
numbers a practitioner can compute the optimum; without them, the claim is
unfalsifiable.
