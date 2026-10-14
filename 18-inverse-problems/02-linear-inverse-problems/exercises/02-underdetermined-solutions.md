# Solutions — 18-02-02 Underdetermined Problems and Minimum-Norm Solutions

> **Read after attempting the exercises.** Lesson:
> [02 Underdetermined Problems](../02-underdetermined.md).

---

## ★1 — Feasible set

$\dim\mathcal{N}(G) = M - \operatorname{rank}(G) = 8-3 = 5$. The general solution is
$\mathbf{m} = \mathbf{m}_0 + \mathbf{n}$ with $\mathbf{n}\in\mathcal{N}(G)$ and
$\mathbf{m}_0$ any particular solution, most compactly
$\mathbf{m} = G^{\!\top}(GG^{\!\top})^{-1}\mathbf{d} + Z\mathbf{w}$.

---

## ★2 — Lagrange derivation

$$\mathcal{L} = \tfrac12\mathbf{m}^{\!\top}\mathbf{m}
+ \boldsymbol{\lambda}^{\!\top}(\mathbf{d}-G\mathbf{m}),
\qquad
\nabla_{\mathbf{m}}\mathcal{L} = \mathbf{m}-G^{\!\top}\boldsymbol{\lambda} = \mathbf{0}.$$

So $\mathbf{m} = G^{\!\top}\boldsymbol{\lambda} \in
\operatorname{range}(G^{\!\top})$, which is the orthogonal complement of
$\mathcal{N}(G)$ in $\mathbb{R}^{M}$: the solution has no null-space component by
construction. Substituting into the constraint gives
$GG^{\!\top}\boldsymbol{\lambda} = \mathbf{d}$.

---

## ★3 — Gram matrix and determinant

$$GG^{\!\top} = \begin{pmatrix}4&2&0\\2&4&2\\0&2&4\end{pmatrix},
\qquad
\det = 4(16-4) - 2(8-0) = 48-16 = 32 \neq 0,$$

so $GG^{\!\top}$ is invertible and the rays are linearly independent (rank 3).

---

## ★4 — Norm identity

$\lVert\hat{\mathbf{m}}\rVert^{2} = 0.605434^{2} = 0.366550$.
At $\lVert\mathbf{w}\rVert = 0.2$: $0.366550+0.04 = 0.406550$, and
$\sqrt{0.406550} = 0.637613$ ✔, exactly the printed value. The identity holds
because $\hat{\mathbf{m}}\perp\mathcal{N}(G)$.

---

## ★5 — Identical data, different models

(a) The data discrepancy is *exactly* zero in exact arithmetic; the measured
$\le3.33\times10^{-16}\ \mathrm{s}$ is roundoff on data of size
$\sim1\ \mathrm{s}$, i.e. $3\times10^{-16}$ relative.

(b) Because the minimum-norm model is the member of a 5-dimensional family closest
to the origin, the choice of norm produced the cell values. Different cells move by
$0.31\ \mathrm{s\,km^{-1}}$ at the same null-space amplitude, so the reported
per-cell values are artefacts of the rule; only the ray sums are data-determined.

---

## ★6 — Sparsity versus smallness

(a) The two objectives are different: smallness minimises a quadratic that penalises
any large entry, while $L_{1}$ minimises the *sum of absolute values*, which is
attained at a vertex of the feasible set (a sparse point). The $L_{1}$ solution
concentrates $1.7\ \mathrm{s\,km^{-1}}$ of slowness in three cells, so its Euclidean
norm is larger even though its $L_{1}$ norm is the same ($1.7000$ in both cases).

(b) Use $L_{1}$: a compartmentalised body is sparse, and minimum norm would smear
it across all eight cells. Report (i) the penalty weight or the noise level it was
tuned against, (ii) the fit achieved, and (iii) a synthetic recovery test showing
what sparsity does to a known model — because sparsity also *creates* sharp edges
that may not exist.

---

## ★★★7 — A design that determines all eight cells

**Geometry.** Each ray must sample a *different* combination. Choose eight rays
that form an invertible 8×8 matrix, for instance ray $k$ covering cells
$\{k, k+1\}$ cyclically (a circulant band matrix), plus a direct ray on each single
cell if the physics allows; the simplest complete design is the identity (each ray
in one cell), which is not a ray but a *well log* — the honest answer is that
physical ray sums cannot resolve all eight cells individually, and the design must
add a different *measurement type* (a borehole log).

**Predicted rank.** With $r$ independent sums, the feasible interval width for a
typical cell is of order the ray value divided by the number of cells sharing the
ray: with 4-cell rays, widths $\approx0.9/4 = 0.225\ \mathrm{s\,km^{-1}}$, above the
$0.1$ target. To reach $0.1$ you need sums over at most two cells, or extra
information.

**LP verification.** Solve, for each cell $j$,
$\max m_j - \min m_j$ subject to $G\mathbf{m}=\mathbf{d}$, $0\le m_j\le1$ — the
constructions used in the lesson — and confirm every width is below $0.1$. If any
is not, the design fails regardless of how many rays it has.

---

## ★★★8 — Weighted minimum norm

Minimise $\tfrac12\mathbf{m}^{\!\top}W\mathbf{m}$ subject to $G\mathbf{m}=\mathbf{d}$
with $W = C_m^{-1}$ positive definite. The Lagrangian gives
$W\mathbf{m} = G^{\!\top}\boldsymbol{\lambda}$, hence
$\mathbf{m} = C_mG^{\!\top}\boldsymbol{\lambda}$ and

$$\hat{\mathbf{m}} = C_mG^{\!\top}\left(GC_mG^{\!\top}\right)^{-1}\mathbf{d},$$

the **weighted** minimum-norm solution, which lies in
$\operatorname{range}(C_mG^{\!\top})$ instead of $\operatorname{range}(G^{\!\top})$.

**Physics.** $C_m$ encodes how much model variability you expect, and where: large
prior variance in a cell allows a large value there, small prior variance suppresses
it. Diagonal $C_m$ = independent cell variances (e.g. a depth-dependent prior);
non-diagonal $C_m$ = spatial correlation (smoothness).

**Relation to Bayes.** With a Gaussian prior
$\mathbf{m}\sim\mathcal{N}(\mathbf{0},C_m)$ and likelihood
$\mathbf{d}\sim\mathcal{N}(G\mathbf{m},C_d)$, the posterior mean is

$$\hat{\mathbf{m}} = C_mG^{\!\top}\left(GC_mG^{\!\top}+C_d\right)^{-1}\mathbf{d},$$

which reduces to the expression above in the noise-free limit $C_d\to0$. So
"weighted minimum norm with a prior covariance" *is* Bayesian inversion with a
Gaussian prior: the selection rule and the prior are the same object
([18-05-03](../../05-bayesian-inversion/03-priors.md)).
