# Solutions — 19-03-03 Assembly, Sparsity and Linear System Structure

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [03 Assembly, Sparsity and Linear System Structure](../03-fem-assembly.md).

---

## ★1 — Storage at $n = 64$

With homogeneous Dirichlet data on all four sides the unknowns are the interior
nodes: $(n-1)^2 = 63^2 = 3969$.

The measured non-zero count at $n=64$ is $34969$, i.e. $8.81$ per row
(nnz/row $\to 9$). Storage: $34969\times 8$ bytes $= 279752$ bytes $= 0.28$ MB.

Dense: $3969^2\times 8 = 1.260\times10^{8}$ bytes $= 126.0$ MB, a ratio

$$\frac{126.0\ \text{MB}}{0.28\ \text{MB}} = 450.$$

The ratio grows as $\mathrm{ndof}$ (here by a factor of about $n^2/9$), so at
$n = 128$, where the measured ndof is $16129$ and nnz is $143641$, the same
comparison reads $1.1$ MB against $2081$ MB — a factor $1812$.

---

## ★2 — Smallest eigenvalue against mesh spacing

The lesson measures $\lambda_{\min}(K) \approx 2\pi^2h^2$. At $n = 32$,
$h = 1/32$:

$$2\pi^2h^2 = 2(9.869604)(0.03125)^2 = 1.92767\times10^{-2},$$

against the measured $1.923\times10^{-2}$ — a difference of 0.24%, consistent with
the $h^2$ correction to the leading term. The reading of the formula is in the
lesson: the smallest *generalised* eigenvalue of the unit square (Dirichlet) is
$2\pi^2$, and the Rayleigh quotient $v^{\mathsf{T}}Mv/v^{\mathsf{T}}v$ of a smooth
nodal vector is $h^2$ because each node stands for an area $h^2$.

---

## ★3 — Why $\lambda_{\max}$ is mesh-independent

The entries of $K$ are $\int\nabla\varphi_i\cdot\nabla\varphi_j\,\mathrm{d}A$: the
gradients carry $1/h$ each, the area carries $h^2$, and the product carries
$h^0$. So the entries do not depend on $h$ at all (measured agreement with the
closed form $1.1\times10^{-16}$ at $h = 0.25$), and neither, therefore, does the
largest eigenvalue: measured 3.805, 3.949, 3.985, 3.988 for $n = 8, 16, 32, 64$,
approaching a constant near 4.

This is a *featuring* of the finite-element matrix, not of the operator: the
finite-difference form of the same operator is $h^{-2}$ times this matrix, so its
largest eigenvalue grows as $h^{-2}$. The physically meaningful, mesh-independent
statement is about the generalised problem, and the mesh-dependent quantity that
governs solver cost is the ratio — the condition number.

---

## ★4 — Predicting the condition number and the iteration growth

Measured law: $\mathrm{cond}(K) = O(h^{-2})$ with fitted exponent $2.004$, and
the measured value at $n = 64$ is $8.281\times10^{2}$. Going to $n = 256$
multiplies $1/h$ by 4, so

$$\mathrm{cond}(256) \approx 8.281\times10^{2}\times 4^{2.004}
= 1.325\times10^{4}.$$

For unpreconditioned CG the iteration count scales as
$\sqrt{\mathrm{cond}}$, so the growth factor is $4^{2.004/2} = 4.01$. The
measured counts are more direct: 46 iterations at $n=32$ and 93 at $n=64$, a
factor $2.02$ for a doubling of $n$, i.e. $h^{-1.01}$ — consistent with the
fitted exponent $1.072$ from the full sequence.

(The estimate above is a two-step extrapolation: the exponent is measured, the
$h^{-2}$ law is measured, and the prediction is arithmetic on those.) 

---

## ★5 — Why Jacobi is exactly a no-op on a uniform Q1 mesh

Diagonal preconditioning replaces the system $Ku = b$ by
$D^{-1}Ku = D^{-1}b$ with $D = \operatorname{diag}(K)$. For a uniform structured
Q1 mesh every interior node belongs to exactly four cells, each contributing the
same diagonal entry $\tfrac23$ (the closed-form diagonal of
$\tfrac16[4,-1,-2,-1;\dots]$), so

$$D = \operatorname{diag}(8/3, 8/3, \dots, 8/3) = \tfrac83 I .$$

The preconditioned matrix $D^{-1}K = \tfrac38K$ is a *scalar multiple* of $K$.
CG builds its iterates from the Krylov space
$\mathrm{span}\{b, Ab, A^2b, \dots\}$, and multiplying $A$ by a scalar does not
change that space; only the convergence metric is rescaled. The measured result
is therefore exactly identical iteration counts (10, 22, 46, 93).

The smallest change that makes the diagonal informative is a non-uniform mesh or
a heterogeneous coefficient. The lesson measures the graded-mesh case: with cell
widths growing geometrically by 1.10 the diagonal spread is $3.684\times10^{2}$
and the iteration count falls from 144 to 63; at a grading of 1.25 the spread is
$1.020\times10^{6}$ and the count falls from 479 to 63.

---

## ★6 — Dense storage, and one algorithmic consequence

At $n = 128$: $\mathrm{ndof} = 16129$,
$\mathrm{nnz} = 143641$. Dense storage is
$16129^2\times 8 = 2.081\times10^{9}$ bytes $= 2.08$ GB against
$143641\times8 = 1.15$ MB — a ratio of $1812$.

**The further reason:** a dense matrix loses the *structure* that makes the
sparse problem tractable, not merely the storage. Two consequences follow, and
both are algorithmic rather than economic:

1. A matrix-vector product costs $O(\mathrm{ndof}^2)$ instead of
   $O(\mathrm{nnz}) = O(\mathrm{ndof})$ — a factor 1812 per Krylov iteration at
   this size, and worse at every larger size.
2. A direct factorisation fills in. Even sparse, the measured fill at $n=64$ is
   $507906$ non-zeros from $34969$ with natural ordering and $319782$ with
   COLAMD — 9 to 15 times the original. Dense, all
   $\mathrm{ndof}(\mathrm{ndof}+1)/2$ entries exist whether or not they are
   needed.

So the dense choice does not merely cost more memory; it changes which algorithms
are available.

---

## ★7 — Repairing the pure-Neumann system

The degenerate system is $Ku = b$ with $\mathbf{e} = (1,\dots,1)$ in the null
space. The repair is two lines: project the right-hand side and add a rank-one
term,

$$b \leftarrow b - \bar{b}\,\mathbf{e}, \qquad
\tilde{K} = K + \frac{1}{N}\mathbf{e}\mathbf{e}^{\mathsf{T}}.$$

**Why this removes the null space.** The null vector satisfies
$\tilde{K}\mathbf{e} = K\mathbf{e} + \tfrac1N\mathbf{e}\,\mathbf{e}^{\mathsf{T}}
\mathbf{e} = 0 + \tfrac{N}{N}\mathbf{e} = \mathbf{e}$, so
$\mathbf{e}$ is no longer a null vector — it is an eigenvector with eigenvalue
exactly $1$.

**Why nothing else changes.** If $v \perp \mathbf{e}$ then
$\mathbf{e}^{\mathsf{T}}v = 0$, so $\tilde{K}v = Kv$: every eigenvalue of $K$ on
the mean-zero subspace is unchanged, exactly in exact arithmetic. At $N = 289$
the formerly-zero eigenvalue moves to $1/289 = 3.4602\times10^{-3}$, while the
smallest non-zero eigenvalue ($2\pi^2 = 1.9739\times10^{1}$ for the unit square)
is unchanged — a relative change of $0.0002\%$, which is round-off. The
demonstration measures exactly this: converged CG, $\mathrm{info} = 0$,
$\mathrm{mean}(x) = 9.2\times10^{-18}$.

**The point.** The repair fixes the *representation* of the non-uniqueness (the
solution is still only determined up to a constant; the rank-one term fixes the
mean to zero) rather than pretending the non-uniqueness is not there.

---

## ★8 — Is the growth governed by the condition number or by $h$?

**Matrices to compare.** Two one-parameter families, each solved to the same
relative residual with unpreconditioned CG:

- $A_1(h)$: the 2-D Q1 Laplacian on a uniform mesh, whose condition number grows
  as $h^{-2}$ and whose *spectrum* is fixed in shape.
- $A_2(\kappa)$: a 1-D tridiagonal model problem with a *prescribed, variable*
  condition number at fixed size — for example $K$ with a diagonal weighting
  $d_i = \kappa^{(2i-N)/N}$ chosen so that $\mathrm{cond}$ equals a target
  $\kappa$ independent of $h$, and with the same size as $A_1$.

**Metric.** Iterations to a relative residual of $10^{-10}$, against (i) $h$ and
(ii) $\mathrm{cond}$. Fit both.

**What each outcome means.**

- If iterations track $\sqrt{\mathrm{cond}}$ in both families, the growth is
  governed by the condition number, and mesh refinement is one way — not the only
  way — to raise it. The design conclusion is that any change raising
  $\mathrm{cond}$ costs the same.
- If the 1-D family needs far fewer iterations at the same $\mathrm{cond}$, then
  the *dimension* and the *spectral distribution* matter, not only the ratio of
  extremes. CG's rate depends on the whole spectrum, not just its endpoints, so
  that outcome would say the $h^{-1}$ scaling is a property of the mesh
  distribution and not of the condition number alone.
- If iterations in $A_1$ track $h^{-1}$ but not $\sqrt{\mathrm{cond}}$, then some
  part of the mesh effect is not captured by $\mathrm{cond}$ at all, and the
  lesson's $h^{-2}$ law is being used as a proxy for something else.

The experiment is decisive because it *decouples* $h$ from $\kappa$: the lesson's
measurement confounds them, since refining the mesh raises both.
