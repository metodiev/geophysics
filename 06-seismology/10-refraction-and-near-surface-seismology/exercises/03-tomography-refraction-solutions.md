# Solutions — 06-10-03 Refraction Tomography and First-Arrival Inversion

**Read after attempting the exercises.** Numbers were computed, not estimated.
Lesson: [03 Refraction Tomography and First-Arrival Inversion](../03-tomography-refraction.md).
All models are SYNTHETIC.

---

## ★1 — Path integral and units

$$t = \frac{20}{600} + \frac{15}{1800} + \frac{20}{600}
= 0.033333 + 0.008333 + 0.033333 = 0.075\ \mathrm{s} = 75.0\ \mathrm{ms}.$$

In $\mathbf{A}\mathbf{s} = \mathbf{t}$: $A_{ij}$ is a **length** (m), $s_j$ is a
**slowness** ($\mathrm{s\,m^{-1}}$), and $t_i$ is a **time** (s). The product is
$\mathrm{m}\times\mathrm{s\,m^{-1}} = \mathrm{s}$, which is the check that catches a
model stored as velocity instead of slowness. Most tomography code failures whose
residual will not fall are a units inconsistency of exactly this kind.

---

## ★2 — Zero-coverage cells

$62.5\%$ of $120$ cells is $0.625 \times 120 = 75$ cells, so
$120 - 75 = 45$ cells contain no ray.

For those cells the column of $\mathbf{A}$ is zero, the diagonal entry of
$\mathbf{A}^{\mathsf T}\mathbf{A}$ is zero, and the damped normal equations give the
update

$$\delta s_j = 0 \quad\text{for a column of zeros,}$$

so the cell keeps **its starting value**. That value is not an estimate of the
ground: it is the analyst's prior, printed with the same font as the cells that were
measured. This is the reason the coverage map is part of the result.

---

## ★3 — The starting gradient

| row centre $z$ (m) | $v = 400 + 60z$ (m/s) |
|---|---|
| 0 | 400 |
| 5 | 700 |
| 10 | 1000 |
| 15 | 1300 |
| 20 | 1600 |
| 25 | 1900 |

A ray in a homogeneous medium is straight, and a ray launched from the surface of a
homogeneous half-space has no reason to leave the surface: the shortest path to a
surface receiver runs along the surface. Adding a velocity that increases with depth
bends rays downward (Snell's law at each infinitesimal interface), so rays dive,
sample depth and populate the rows of $\mathbf{A}$. Without a dive, every row below
the first has a zero column, and Gauss–Newton cannot repair that in a later
iteration because the sensitivity it would need is exactly what is missing.

---

## ★★4 — The residual floor

$$\text{reduction} = \frac{15.0693}{0.7208} = 20.9, \qquad
\frac{0.7208}{0.4473} = 1.61.$$

The first number is the linearisation working. The second is the interesting one:
the inversion stops at $1.61\times$ the noise level, not at it. A residual above the
noise floor means the prediction cannot reproduce the data to within the noise, and
the cause is **model error**, not convergence: 5 m cells and a damped update cannot
represent a sharp interface, so some of the observed travel time is systematically
unfittable. The companion statement is in the recovered model itself — rows 15–20 m
and 20–25 m (where the rays run along the refractor) come back at 1757 and
1806 $\mathrm{m\,s^{-1}}$, within 2.4% of the truth, while the deepest row comes
back at $1999\ \mathrm{m\,s^{-1}}$, 11% too fast, because it is damped toward the
starting model.

---

## ★★5 — Depth of investigation of a 60 m spread

$$h_{\max} = \frac{L}{2}\sqrt{\frac{v_2-v_1}{v_2+v_1}}
= \frac{60}{2}\sqrt{\frac{1800-600}{1800+600}}
= 30\sqrt{0.5} = 21.21\ \mathrm{m}.$$

The estimate comes from putting the *crossover* of a **two-layer** model at the end
of the spread. Its assumptions are therefore: two homogeneous layers, a horizontal
interface, a single dominant refractor, and first arrivals that are head waves
rather than diving rays. In the demonstration's model, which has a gradient start
plus a fast surface layer, the formula's $h_{\max}$ and the deepest row with mean
coverage above one half agree only in order of magnitude — the demo's table has
$10.61$ m against $5.0$ m at $L = 30$ m and $28.28$ m against $30.0$ m at
$L = 80$ m. The robust statement is the monotone one: the deepest sampled row grows
with the spread.

---

## ★★6 — Spread requirement and the role of the contrast ratio

For $v_1 = 1200$, $v_2 = 3600\ \mathrm{m\,s^{-1}}$ ($v_2/v_1 = 3$),
$h = 20\ \mathrm{m}$:

$$x_c = 2 \times 20\sqrt{\frac{3600+1200}{3600-1200}} = 40\sqrt{2}
= 56.5685\ \mathrm{m}, \qquad L = 3x_c = 169.71\ \mathrm{m}.$$

For $v_1 = 1000$, $v_2 = 3000\ \mathrm{m\,s^{-1}}$ ($v_2/v_1 = 3$), same depth:

$$x_c = 2 \times 20\sqrt{\frac{3000+1000}{3000-1000}} = 40\sqrt{2}
= 56.5685\ \mathrm{m}, \qquad L = 169.71\ \mathrm{m}.$$

**The two are identical**, and they must be: the crossover formula contains the
velocities only through the ratio $v_2/v_1$. **What governs survey cost and depth
reach is the velocity *contrast*, not the absolute velocity.** This is why a
refraction survey over soft ground with a strong contrast can be cheap, and why the
same survey over stiff ground with a weak contrast can be hopeless — a fact worth
remembering before quoting a spread length that was designed at another site.

---

## ★★★7 — Damping, the box constraint, and what a model class means

With $\lambda = 0$ the normal equations are $\mathbf{A}^{\mathsf T}\mathbf{A}\,
\delta s = \mathbf{A}^{\mathsf T}\delta t$. For a cell with no ray, row and column
$j$ of $\mathbf{A}^{\mathsf T}\mathbf{A}$ are zero, so the system is singular and the
$j$-th equation reads $0 \cdot \delta s_j = 0$: **any** $\delta s_j$ is a solution,
and an iterative solver returns whatever the numerical round-off and the
preconditioner produce. Since a falling residual does not require $\delta s_j$ to be
sensible in an unconstrained cell (the data contain no information about it), the
solver is free to move it anywhere — including to negative slowness. Physically that
is a negative rigidity; numerically it is a negative edge weight in the
shortest-path solver, whose Dijkstra iteration then returns nonsense.

So the box constraint $150 \le v \le 4000\ \mathrm{m\,s^{-1}}$ is not a cosmetic
guard. It says: **the model class is "physically admissible velocities", not "any
array of 120 numbers"**. It converts an unbounded non-uniqueness into a bounded one
and keeps the forward operator well posed. The damping has a different and
complementary job: it selects, among the infinitely many admissible models that fit
the data, the one closest to the starting model — which is a statement of preference,
and the reason the deep rows read as they do.

Two further notes belong in any honest answer. First, the choice $\lambda = 15$ was
made, not derived: a different value gives a visibly different model with almost the
same residual, so the experiment should report both. Second, the box bounds are
themselves information: they exclude velocities that the survey cannot distinguish
but that a geologist would, and reporting a model without stating the model class is
reporting half of it.

---

## ★★★8 — Measuring the resolution matrix diagonal

**Perturbation.** For each cell $j$ in turn, add a small slowness perturbation
$\delta s_j$ far below the noise sensitivity (e.g. $10^{-4}$ of the background
slowness) to a *synthetic* model, regenerate exact forward data with the eikonal
solver, and invert with the full geometry and the production $\lambda$. The
recovered $\delta\hat{s}_i / \delta s_j$ over all $i$ is column $j$ of
$\mathbf{R}$.

**Metric.** The diagonal entry $R_{jj}$ (how much of a cell's own perturbation
returns in that cell), the largest off-diagonal entry (how much leaks elsewhere),
and the row sum $\sum_i R_{ij}$ (whether the inversion conserves the perturbation at
all). For a full-rank, undamped system $R_{jj} = 1$; with damping and limited
coverage $R_{jj} < 1$.

**Control.** The same perturbation applied to a cell of known full coverage, and a
perturbation applied to a *homogeneous* background so that the answer is not
contaminated by the model the rays traverse.

**Expected outcome.** In a well-covered cell (the demonstration's row 15–20 m, where
rays run along the refractor) $R_{jj}$ is close to 1 and the row sum close to 1: the
perturbation returns where it was put, so a velocity read there is essentially a
measurement. In a zero-coverage cell (below the deepest ray) $R_{jj}$ is close to 0
and the returned perturbation is identically zero, because the data are unchanged:
the inversion's answer is the starting model, however much it is displayed as a
result. The experiment is complete when the two numbers are reported together; a
single $R_{jj}$ without a coverage map does not say which regime the cell is in.
