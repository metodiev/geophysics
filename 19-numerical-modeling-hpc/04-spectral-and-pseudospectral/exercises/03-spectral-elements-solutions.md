# Solutions — 19-04-03 Spectral Element Methods and Their Geophysical Use

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [03 Spectral Element Methods and Their Geophysical Use](../03-spectral-elements.md).

---

## ★1 — Exactness of the two rules

With $p+1$ nodes, Gauss-Lobatto-Legendre integrates polynomials of degree
$\le 2p-1$ exactly; Gauss-Legendre with the same node count integrates degree
$\le 2(p+1)-1 = 2p+1$. The GLL rule is therefore **two degrees behind** a
Gauss rule of the same size.

The lesson's measurements show both halves: the GLL weights sum to 2 to
$2.2\times10^{-16}$ and the degree-$(2p-1)$ error is round-off
($0.0$ to $6.9\times10^{-18}$), while the degree-$2p$ error is non-zero
($2.667\times10^{-1}$ at $p=2$, $1.988\times10^{-7}$ at $p=12$). The lost degrees
are exactly where the mass integrand of an order-$p$ element sits, which is the
origin of the lumping error of ★2.

---

## ★2 — Why the mass matrix is diagonal, and what it costs

With GLL quadrature the nodes *are* the interpolation nodes, so
$\varphi_i(x_q) = \delta_{iq}$ and

$$\tilde{M}_{ij} = \sum_q w_q\,\varphi_i(x_q)\varphi_j(x_q) = \delta_{ij}w_i .$$

That is exact algebra, so the off-diagonal entries are not small — they are
identically zero. Measured: $\max|\text{off-diagonal}| = 0.000\times10^{0}$ at
every order $p = 2, 4, 6, 8$.

**The cost:** the diagonal entries differ from the exact integrals, because the
mass integrand has degree $2p$ and the rule is exact only to $2p-1$. Measured:
$2.667\times10^{-1}$ at $p=2$, $7.90\times10^{-2}$ at $p=4$,
$3.75\times10^{-2}$ at $p=6$, $2.19\times10^{-2}$ at $p=8$ — a factor 12
improvement over a factor 4 in $p$.

**What it buys:** a diagonal mass matrix makes an explicit time step require no
linear solve for the mass operator, which is decisive for time-domain wave
propagation. So the price is a quadrature error, and the purchase is
algorithmic simplicity and parallelism.

---

## ★3 — Timestep limit at $p = 6$

$$\Delta t \le \frac{2}{\sqrt{\lambda_{\max}}}
= \frac{2}{\sqrt{3245.7555}} = 0.035105\ \text{s},$$

matching the lesson's measured $0.035105$.

---

## ★4 — Growth from $p = 4$ to $p = 8$

$$\frac{\lambda_{\max}(8)}{\lambda_{\max}(4)}
= \frac{9397.6063}{766.9212} = 12.2537 .$$

For $p^n$ scaling over the factor 2 in $p$,

$$n = \frac{\log 12.2537}{\log 2} = 3.6151 .$$

That is consistent with — and slightly above — the fitted exponent 3.469 over
$p = 2\dots10$; the local slope between two adjacent orders is steeper than the
global fit, which is expected when a single power law is an approximation.

Timestep at $p = 8$: $\Delta t \le 2/\sqrt{9397.6063} = 0.020631$ s, i.e. 0.286 of
the $p=4$ limit — doubling the order costs a factor 3.5 in the number of steps.

---

## ★5 — Prediction at $p = 12$, $h = 0.125$

$$\lambda_{\max} \approx 766.9212 \times (12/4)^{3.469} \times (0.5/0.125)^{2.009}
= 5.6159\times10^{5},$$

$$\Delta t \le \frac{2}{\sqrt{5.6159\times10^{5}}}
= 2.67\times10^{-3}\ \text{s}.$$

**Why it will be approximate:** three reasons, all of them visible in the lesson's
tables.

1. A single power law in $p$ does not describe the data exactly — the measured
   local exponent between $p = 4$ and $p = 8$ is 3.6151 against the global fit's
   3.469, so the prediction inherits roughly a 10% error at $p=12$.
2. The two scalings are not strictly independent: the element size enters the
   quadrature and the node distribution, so the exponents multiply only
   approximately.
3. The fitted constants come from five points over a factor 2.5 in $p$ each; an
   extrapolation beyond the measured range is an estimate with a stated method,
   which is the honest way to present it.

---

## ★6 — The $h$-refinement rate at $p = 4$

The theoretical $\mathrm{L}^2$ rate for an order-$p$ Galerkin method is $p+1$, so
$5$ here, and the measured sequential orders are 4.995, 4.999, 5.000, 5.000. The
$\mathrm{H}^1$ rate is $p = 4$ (measured 3.981, 3.995, 3.999, 4.000).

**Why the first value is low:** it is the transition from a two-element mesh to a
four-element mesh, where the asymptotic constant has not been established. The
leading error coefficient $C$ in $E \approx Ch^{p+1}$ has its own $O(h^2)$
correction, so the measured local order approaches $p+1$ from below. Reporting
the per-step orders rather than a single fitted number is what makes this
visible — a two-point fit would have returned 4.995 for $p = 5$ and looked
puzzling.

---

## ★7 — Which refinement is cheaper

**Target:** a fixed accuracy, in the lesson's own measured terms. From
Section 4.1, at fixed $h = 0.5$ (two elements) the $\mathrm{L}^2$ error was
$1.076\times10^{-4}$ at $p=4$ and $7.961\times10^{-10}$ at $p=8$ — a factor
$1.35\times10^{5}$ improvement for the same number of *elements*.

**Cost in timesteps.**

- (i) $p: 4 \to 8$ at fixed $h$: the measured $\lambda_{\max}$ grows by 12.2537,
  so $\Delta t$ shrinks by $\sqrt{12.2537} = 3.50$.
- (ii) $h: 0.5 \to 0.25$ at $p = 4$: the measured $\lambda_{\max}$ grows from
  $766.9212$ to $3128.3967$, a factor 4.079, so $\Delta t$ shrinks by
  $\sqrt{4.079} = 2.02$. But halving $h$ improves the error only by $2^{5} = 32$,
  not by $1.35\times10^{5}$.

**Which is cheaper.** Compare the cost of reaching the *same* error:

- (i) $p: 4\to8$: factor $3.50$ in timesteps for a factor $1.35\times10^{5}$ in
  error.
- (ii) $h$-refinement to gain the same factor $1.35\times10^{5}$ at order 5
  requires $2^{n} = 1.35\times10^{5}$, i.e. $n = 17.0$ halvings, each costing a
  factor 2.02 in timesteps: a factor $2.02^{17} \approx 1.55\times10^{5}$ in
  timesteps.

So on this smooth problem, **raising $p$ is roughly $4\times10^{4}$ times cheaper
in timesteps** than refining $h$ to the same accuracy. The conclusion is
conditional and the condition is stated: the solution must be smooth inside the
element. At an interface or a discontinuity the $p$-refinement rate collapses and
the comparison reverses — which is why an $hp$ code refines each element according
to its own local smoothness.

---

## ★8 — Separating lumping from discretisation in the SEM spectrum

**Configurations.** Same mesh, same order, same boundary conditions, same
$K$ (built with the element's own GLL rule, as the lesson does):

- **A — consistent mass:** $M$ evaluated with a high-order Gauss rule, i.e. the
  *exact* mass integrals for the GLL basis.
- **B — GLL (lumped) mass:** $M$ evaluated with the element's own nodes and
  weights, hence diagonal with entries $w_i$.

**Metric.** The generalised eigenvalues of $(K,M)$, reported as the relative error
of the first few $\lambda_k$ against their exact values, and the *difference*
between A and B.

**Predictions.**

1. **At fixed mesh** the difference between A and B isolates the quadrature error,
   because $K$, the mesh and the boundary conditions are identical. If A and B
   agree at fixed $h$, lumping is not what limits the run.
2. **Under $h$-refinement at fixed $p$** both A and B converge to the exact
   eigenvalues at the same rate ($h^{2p}$-ish for eigenvalue errors of a
   symmetric problem), and their *difference* must shrink; a difference that does
   not shrink indicates an implementation error rather than a quadrature choice.
3. **Under $p$-refinement at fixed $h$** the lumping error shrinks only
   algebraically (measured $2.7\times10^{-1} \to 2.2\times10^{-2}$ from $p = 2$
   to $p = 8$ for the mass diagonal), while the discretisation error shrinks much
   faster. So at high $p$ the *lumping* may become the dominant term — the
   opposite of the usual intuition that a higher order fixes everything. This is
   the phenomenon already visible in the lesson's consistent-versus-lumped table
   for P1–P3 elements, where the lumped error at $p=3$ was four orders of
   magnitude worse than the consistent one.
4. **The distinguishing signature** is therefore the *scaling* of the A–B
   difference at fixed $h$: if it falls fast in $p$, the discretisation dominates
   and A ≈ B; if it plateaus, the quadrature dominates and the run is reporting
   the lumping.
