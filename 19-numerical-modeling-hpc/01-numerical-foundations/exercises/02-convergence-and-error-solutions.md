# Solutions — 19-01-02 Truncation Error, Order of Accuracy and Convergence Rates

> **Read after attempting the exercises.** Numeric answers were computed, not
> estimated; where a spread of defensible answers exists it is said so.

Lesson: [02 Convergence and Error](../02-convergence-and-error.md).

---

## ★1 — Truncation terms

| operator | leading term | order $p$ |
|---|---|---|
| central $f'$ | $-\dfrac{h^{2}}{6}f'''$ | 2 |
| central $f''$ | $+\dfrac{h^{2}}{12}f''''$ | 2 |
| forward $f'$ | $+\dfrac{h}{2}f''$ | 1 |

---

## ★2 — Observed order

$$p = \frac{\ln(4.0\times10^{-3}/5.0\times10^{-4})}{\ln 2}
     = \frac{\ln 8}{\ln 2} = 3.00.$$

The scheme is third order on this evidence. (Two grids only: a third grid is
needed before the estimate can be trusted as the asymptotic order.)

---

## ★3 — Two errors

The **local truncation error** is the residual obtained by substituting the exact
solution into the discrete operator: $\tau_h = L_h u - Lu$, an $O(h^{p})$ quantity
per step. The **global discretisation error** is
$e_h = u_h - u$, the accumulated difference over the whole solution.

A first-order scheme has a global error of the same order because there are
$O(h^{-1})$ steps, each contributing $O(h)$ of local error under a stable
amplification: $(h^{-1})(h) = O(1)$ would be the naive sum, and the extra factor
of $h$ supplied by the local truncation error leaves $O(h)$ — the mechanism
formalised by Lax equivalence.

---

## ★4 — The predicted constant

$e \approx -\dfrac{h^{2}\pi^{2}}{12}u$, so $\max|e|/h^{2} \to \pi^{2}/12$.

$$\frac{\pi^{2}}{12} = 0.8224670334,$$

measured $0.822483$ at $n = 160$: relative difference
$(0.822483-0.822467)/0.822467 = 1.9\times10^{-5}$, i.e. agreement to two parts in
$10^{5}$.

---

## ★5 — Order, extrapolation and GCI

Observed order from the two errors:
$p = \ln(5.14\times10^{-4}/1.29\times10^{-4})/\ln 2
= \ln(3.9845)/\ln 2 = 1.994$.

Richardson, treating the fine solution's own error:
$e_{\text{fine}} \approx |u_{\text{fine}} - u_{\text{coarse}}|/(2^{p}-1)
= (5.14\times10^{-4}-1.29\times10^{-4})/(2^{1.994}-1)
= 3.85\times10^{-4}/2.98 = 1.29\times10^{-4}$ — identical to the measured fine
error, as it must be when the error is a clean $h^{2}$ term.

GCI: with $F_s = 1.25$ and the difference referred to the fine solution,
$1.25\times3.85\times10^{-4}/2.98 = 1.61\times10^{-4}$ on the same scale as the
error — i.e. the estimator is the fine error inflated by exactly $F_s$ whenever
the expansion is clean.

---

## ★6 — The optimal step

Balance truncation $h^{2}/12$ against round-off $c\,\varepsilon/h^{2}$ with
$c = 0.1121$:

$$h_{\text{opt}} = \left(12\,c\,\varepsilon\right)^{1/4}
= \left(12\times0.1121\times2.220\times10^{-16}\right)^{1/4}
= \left(2.987\times10^{-16}\right)^{1/4} = 1.315\times10^{-4}.$$

Measured optimum $1.081\times10^{-4}$ — a factor $1.22$ smaller, which is within
the accuracy of the fit because the round-off term is a random walk rather than a
deterministic bound.

---

## ★7 — A verification protocol

**Spatial order.** Manufactured solution
$u = \sin(\pi x)e^{-\pi^{2}\alpha t}$ on $(0,1)$ with Dirichlet data and
$f$ added as a source; integrate to a fixed small time with a time step small
enough that the temporal error is two orders of magnitude below the spatial one
(that is itself measured in step 3). Grids $n = 40, 80, 160, 320$; metric
$L^{\infty}$ at $t = 0.01$; acceptance: observed order between 1.9 and 2.1 and
error$/h^{2}$ constant to three figures.

**Temporal order.** Compare against the exact solution of the space-discretised
system (eigen-decomposition of the discrete Laplacian) so that the spatial error
cancels identically. Steps $dt$ and $dt/2$ for four levels; metric $L^{2}$;
acceptance: observed order within $2\,\%$ of the design order.

**Stability limit.** Initialise the grid-Nyquist mode on a periodic grid, run
200 steps for $r = 0.45, 0.48, 0.50, 0.52$; metric the measured growth per step;
acceptance: growth $\le1$ below the predicted limit and equal to $|1-4r|$ above
it to three figures. (This is exactly the experiment the demonstration performs.)

**Record.** State the grids, steps, metric, measured numbers and the exact
constants they were compared with; a verification claim without the numbers is
not reproducible.

---

## ★8 — Why the extrapolation gain is not $2^{p}$

Write the error as $e_h = C_2h^{2} + C_4h^{4} + \cdots$. Richardson with the
correct $p = 2$ removes the $C_2$ term exactly; what remains is $C_4h^{4}$. The
gain is therefore

$$\frac{e_{\text{fine}}}{e_{\text{extrap}}} = \frac{C_2h^{2}}{C_4h^{4}}
= \frac{C_2}{C_4h^{2}}.$$

To obtain $3242$ with $h = 0.00625$:

$$\frac{C_2}{C_4} = 3242\times h^{2} = 3242\times3.906\times10^{-5} = 0.1267,
\qquad C_4 = \frac{0.822467}{0.1267} = 6.49,$$

so the $h^{4}$ coefficient is about $6.5$ against $0.82$ for $h^{2}$ — the
expansions' coefficients differ by a factor of eight, and it is $h$, not the
order, that turns that into a factor of thousands at this grid.

**Consequence.** Anyone who assumes the improvement is $2^{p} = 4$ will
*overestimate* the extrapolated error here by a factor of $800$, and will
over-refine as a result. The improvement factor must be measured, or the ratio
of the two coefficients quoted; the order alone does not determine it.
