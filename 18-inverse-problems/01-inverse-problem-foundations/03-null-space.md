---
id: 18-01-03
title: "Null Space, Non-Uniqueness and Equivalence Classes"
level: graduate
prereqs: ["18-01-02", "01-07-04", "01-07-08"]
tags: [inverse-problems, null-space, non-uniqueness, equivalence-class, tomography, rank]
---

# Null Space, Non-Uniqueness and Equivalence Classes

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the null space $\mathcal{N}(G)$, the range
   $\operatorname{range}(G)$ and the equivalence class of a solution, and
   **state** the rank-nullity relation.
2. **Derive** an explicit null-space basis from the singular value decomposition
   and **verify** $G\mathbf{n}=0$ to machine precision.
3. **Construct** two models that fit one data vector to machine precision and
   **quantify** how far apart they are.
4. **Solve** for the exact feasible interval of a single model parameter over the
   constrained equivalence class, and **interpret** interval width as the honest
   uncertainty of that parameter.
5. **Distinguish** the structural null space (cells no measurement visits) from
   the trade-off null space (exchanges inside a measurement's footprint).
6. **Identify** which linear combinations of parameters the data do determine,
   and **phrase** an interpretation in terms of those combinations.
7. **Explain** why forming the normal equations neither removes the null space
   nor preserves the conditioning.

## Prerequisites

- [18-01-02 Hadamard's Conditions](02-hadamard-well-posedness.md) — the failure
  of uniqueness in its exact form, and the tolerance problem in rank counting.
- [01-07-04 Rank, Null Space and Solvability](../../01-mathematics/07-linear-algebra/04-rank-and-nullspace.md) —
  the four fundamental subspaces.
- [01-07-08 Singular Value Decomposition](../../01-mathematics/07-linear-algebra/08-svd.md) —
  the basis in which $G$ is diagonal.

## 1. The statement, and why "non-unique" is too coarse

For $\mathbf{d} = G\mathbf{m}$, call any $\mathbf{m}$ with $G\mathbf{m}=\mathbf{d}$
a solution. If $\mathbf{n}\in\mathcal{N}(G)$ then $\mathbf{m}+\mathbf{n}$ is also a
solution, with **exactly** the same data. The set of all solutions of one data set
is an **equivalence class**:

$$\mathcal{M}(\mathbf{d}) = \bigl\{\mathbf{m}_0+\mathbf{n}:\
\mathbf{n}\in\mathcal{N}(G)\bigr\}
= \mathbf{m}_0 + \mathcal{N}(G),$$

an affine subspace of $\mathbb{R}^{M}$ whose dimension is $\dim\mathcal{N}(G)$.
Because the geometry of the subspaces is most transparent in the singular value
decomposition ([01-16-02](../../01-mathematics/16-functional-analysis/02-hilbert-spaces.md)),
let $G = U\Sigma V^{\!\top}$ with singular values
$\sigma_1\ge\dots\ge\sigma_r>0$ and $r = \operatorname{rank}(G)$. Then

$$\operatorname{range}(G) = \operatorname{span}\{\mathbf{u}_1,\dots,\mathbf{u}_r\},
\qquad
\mathcal{N}(G) = \operatorname{span}\{\mathbf{v}_{r+1},\dots,\mathbf{v}_{M}\},$$

and the **rank-nullity theorem** states

$$\dim\operatorname{range}(G) + \dim\mathcal{N}(G) = r + (M-r) = M .$$

Saying "the problem is non-unique" is therefore too coarse to be useful. The
useful statements are: *how many* directions are missing, *which* directions they
are, and *how far* a physically meaningful quantity can move along them. This
lesson answers all three with numbers.

All models and data in this module are **SYNTHETIC**.

## 2. The experiment

The demonstration uses a deliberately simple transmission experiment: a
$4\times4$ grid of square cells, each holding one scalar (a slowness anomaly),
and five rays whose measurement is the **sum** of the cell values along the ray.

| ray | cells visited |
|---|---|
| R1 | 0, 1, 2, 3 (row 0) |
| R2 | 4, 5, 6, 7 (row 1) |
| R3 | 12, 13, 14, 15 (row 3) |
| R4 | 1, 5, 9, 13 (column 1) |
| R5 | 0, 5, 10, 15 (diagonal) |

So $G$ is $5\times16$ with entries $0$ or $1$ (path lengths), $M = 16$,
$N = 5$. Data come from a chosen SYNTHETIC model:

$$\mathbf{d} = (0.4,\;0.3,\;0.3,\;0.4,\;1.2),$$

computed exactly from $\mathbf{m}_{\text{true}}$ with $m_{0}=m_{5}=m_{10}=m_{15}=0.30$
and $m_{1} = 0.10$. No noise is added: this lesson is about exact ambiguity, not
about noise.

## 3. Rank, nullity and an explicit null basis

The measured singular values are

$$\sigma = (2.6458,\;2.0000,\;2.0000,\;1.7321,\;1.4142),$$

so $r = 5$ and

$$\dim\mathcal{N}(G) = 16-5 = 11,\qquad 5+11 = 16 = M .$$

The last $11$ right singular vectors span $\mathcal{N}(G)$; the demonstration
verifies

$$\max|GZ| = 4.996\times10^{-16},\qquad
\lVert Z^{\!\top}Z - I_{11}\rVert_\infty = 2.290\times10^{-16},$$

where the columns of $Z$ form an orthonormal basis of the null space. Both are
machine precision, so the null space is not an approximation.

Two physically distinct kinds of null vector appear, and the distinction matters
in practice.

**Structural null space.** Cells $8$ and $11$ are visited by no ray at all, so
their unit vectors $\mathbf{e}_8$ and $\mathbf{e}_{11}$ satisfy
$G\mathbf{e}_j = 0$ trivially. Nothing about them is measured. This is the
cheapest form of non-uniqueness to detect: look for empty columns of $G$.

**Trade-off null space.** Cells 2 and 3 lie in the same row 0, and every ray
that visits one visits the other with the same weight, so
$\mathbf{e}_2-\mathbf{e}_3$ is a null vector: the demonstration verifies
$G\mathbf{n} = 0.000\times10^{0}$ exactly. The data see the *sum* of the two cells
but never the split between them. This is the form that survives even in a fully
covered model, and it is why tomographic interpretations must be phrased in terms
of resolved combinations rather than cells.

## 4. Two models, one data set

Take the minimum-norm solution $\mathbf{m}_{\min} = G^{+}\mathbf{d}$ and any
null-space direction, for instance the first right singular vector with index
$r+1$:

$$\mathbf{m}_{\text{alt}} = \mathbf{m}_{\min} + 0.5\,\mathbf{v}_{6}.$$

Measured:

$$\lVert G\mathbf{m}_{\min}-\mathbf{d}\rVert_\infty = 6.661\times10^{-16},
\qquad
\lVert G\mathbf{m}_{\text{alt}}-\mathbf{d}\rVert_\infty = 4.441\times10^{-16},$$

$$\lVert\mathbf{m}_{\min}\rVert = 0.6038,\qquad
\lVert\mathbf{m}_{\text{alt}}\rVert = 0.7839,\qquad
\frac{\lVert\mathbf{m}_{\text{alt}}-\mathbf{m}_{\min}\rVert}{\lVert\mathbf{m}_{\min}\rVert}
= 0.8281 .$$

Both models reproduce the five measurements to machine precision; they differ by
$83\%$ in norm. An inversion program that returns $\mathbf{m}_{\min}$ has returned
one member of an $11$-dimensional family and has not been told which.

## 5. What the data *do* determine: exact feasible intervals

The equivalence class is infinite, so "the" uncertainty of a parameter is not an
interval unless you bound the class. Impose the physically natural bound
$0\le m_j\le1$ and ask: over all $\mathbf{m}$ with $G\mathbf{m}=\mathbf{d}$ and
$0\le m_j\le1$, what are $\min m_j$ and $\max m_j$? Each of those is a **linear
program**, solved exactly by the demonstration:

| cell | interval | width | visited by a ray? |
|---|---|---|---|
| 0 | $[0.0000,\ 0.4000]$ | 0.4000 | yes |
| 1 | $[0.0000,\ 0.4000]$ | 0.4000 | yes |
| 2 | $[0.0000,\ 0.4000]$ | 0.4000 | yes |
| 3 | $[0.0000,\ 0.4000]$ | 0.4000 | yes |
| 4 | $[0.0000,\ 0.3000]$ | 0.3000 | yes |
| 5 | $[0.0000,\ 0.3000]$ | 0.3000 | yes |
| 6 | $[0.0000,\ 0.3000]$ | 0.3000 | yes |
| 7 | $[0.0000,\ 0.3000]$ | 0.3000 | yes |
| 8 | $[0.0000,\ 1.0000]$ | 1.0000 | **no** |
| 9 | $[0.0000,\ 0.4000]$ | 0.4000 | yes |
| 10 | $[0.2000,\ 1.0000]$ | 0.8000 | yes |
| 11 | $[0.0000,\ 1.0000]$ | 1.0000 | **no** |
| 12 | $[0.0000,\ 0.3000]$ | 0.3000 | yes |
| 13 | $[0.0000,\ 0.3000]$ | 0.3000 | yes |
| 14 | $[0.0000,\ 0.3000]$ | 0.3000 | yes |
| 15 | $[0.0000,\ 0.3000]$ | 0.3000 | yes |

Read the table as a map of what the experiment can and cannot say:

- cells 8 and 11 have width $1.0000$: the whole allowed range. Nothing is known
  about them beyond the bound you imposed;
- cells 0–3 reach up to $0.4000$ because their row sum is fixed at $0.4$: any one
  of them could hold the entire row value, with the others at zero;
- cell 10 is the interesting case. Its interval is $[0.2000,\;1.0000]$, a
  *non-zero lower bound*. The diagonal reading (1.2) forces
  $m_{0}+m_{5}+m_{10}+m_{15}=1.2$; because cells 0, 5 and 15 are capped by their
  own row sums at $0.4$, $0.3$ and $0.3$, cell 10 must be at least
  $1.2-0.4-0.3-0.3 = 0.2$. A *lower bound* on a cell is real information, and it
  came from combining measurements;
- measured summary: **0 cells are pinned exactly, 2 span the entire bound, and
  the median interval width is 0.3500**.

This is what an honest non-uniqueness report looks like: not "the model is
non-unique", but a per-parameter interval derived from the data, the parameterisation
and the imposed bounds.

## 6. Determined combinations versus undetermined ones

Individual cells are badly determined. Some *combinations* are determined
exactly, because a combination lying in the row space of $G$ is fixed by the
data. The demonstration computes four intervals:

| target combination | interval | width |
|---|---|---|
| $m_0+m_1+m_2+m_3$ (row 0, = R1) | $[0.4000,\ 0.4000]$ | **0.0000** |
| $m_3+m_7+m_{11}+m_{15}$ (column 3) | $[0.0000,\ 2.0000]$ | 2.0000 |
| $m_0-m_3$ | $[-0.4000,\ 0.4000]$ | 0.8000 |
| $\sum_{j=0}^{15} m_j$ | $[1.3000,\ 4.4000]$ | 3.1000 |

The first row is pinned exactly — of course, it *is* the measurement $d_1 = 0.4$.
The column-3 sum is worth $2.0000$ wide, because only one cell of that column
(cell 15) lies in a measured row. The grand total is constrained only to
$[1.3, 4.4]$, a width of $3.1$: the data do not determine the total.

The operational rule: **an interpretation is defensible exactly to the extent
that the quantity you report lies in $\operatorname{range}(G^{\!\top})$.** Before
writing "the anomaly is concentrated in the lower right", check whether that
statement is a resolved combination.

## 7. Fully worked example: the minimum-norm solution and one null direction

*(a) Minimum-norm solution.* With $G=U\Sigma V^{\!\top}$ and full column rank not
assumed, the minimum-norm solution of $G\mathbf{m}=\mathbf{d}$ is

$$\mathbf{m}_{\min} = G^{+}\mathbf{d} = \sum_{i=1}^{r}
\frac{\mathbf{u}_i^{\!\top}\mathbf{d}}{\sigma_i}\,\mathbf{v}_i ,$$

which contains no component along $\mathbf{v}_{r+1},\dots,\mathbf{v}_M$ by
construction; hence $\lVert\mathbf{m}_{\min}\rVert$ is minimal over the class.
For this problem the demonstration reports $\lVert\mathbf{m}_{\min}\rVert = 0.6038$
with residual $6.661\times10^{-16}$ — machine precision, because the data were
generated from a model and are therefore consistent.

*(b) One null direction.* Adding $0.5\,\mathbf{v}_6$ changes the model by
$\lVert 0.5\,\mathbf{v}_6\rVert = 0.5$ and changes the data by
$\sigma_6\times0.5 = 0$ to machine precision. The relative model change is
$0.5/0.6038 = 0.828$, which matches the measured $0.8281$.

*(c) A number you cannot report.* The true model has $m_{10}=0.30$. The feasible
interval is $[0.2000,\ 1.0000]$. Reporting "$m_{10}=0.30$" is a statement about
the prior used by the inversion, not about the data; reporting
"$m_{10}\in[0.2,1.0]$ given $0\le m\le1$" is a statement about the data.

## 8. The normal equations: no cure, and a cost

A common first implementation solves $G^{\!\top}G\mathbf{m} = G^{\!\top}\mathbf{d}$.
This is legitimate algebra — every solution set of the two systems is the same —
but the square matrix is worse conditioned. Measured:

$$\kappa(G) = \frac{2.6458}{1.4142} = 1.8708,\qquad
\kappa(G^{\!\top}G) = \frac{7.0000}{2.0000} = 3.5000,$$

$$\frac{\kappa(G^{\!\top}G)}{\kappa(G)^{2}} = 1.000000,\qquad
\text{rank}(G^{\!\top}G) = 5,\qquad \dim\mathcal{N}(G^{\!\top}G) = 11 .$$

The exact identity $\kappa(G^{\!\top}G) = \kappa(G)^{2}$ is confirmed to six digits;
the null space is unchanged, because
$\mathcal{N}(G^{\!\top}G)=\mathcal{N}(G)$; and the condition number is squared, so
three digits of accuracy in $G$ become six lost in $G^{\!\top}G$. For this small
problem that is harmless; for a matrix with $\kappa = 10^{8}$ it is fatal. Use the
SVD or a QR factorisation.

## 9. Assumptions and regime of validity

- **Noiseless, exact data.** The equivalence class here is exact. With noise, the
  class is replaced by a set of models consistent within the error bars, which
  *widens* it.
- **A sum-along-ray kernel with unit weights.** Real transmission kernels weight
  cells by path length in metres; the geometry of the null space is similar but
  the numbers change.
- **An imposed bound.** Intervals in §5 and §6 depend on $0\le m_j\le1$. A
  different bound changes the intervals, so the bound must be reported with them.
- **Linear programming as the interval solver.** Exact for this problem; for large
  models, interval bounds are usually approximated by sampling
  ([18-06-02](../06-uncertainty-quantification/02-monte-carlo-uq.md)).
- **Fixed parameterisation.** Cells are presumed known; the null space due to a
  wrong *choice* of cells is a different problem
  ([18-01-04](04-discretisation-reality.md)).

## 10. Running the demonstration

The demonstration for this lesson is [`code/null_space_demo.py`](code/null_space_demo.py) — print-only, no network access, fixed seed
`np.random.default_rng(20261014)`.

```bash
cd 18-inverse-problems/01-inverse-problem-foundations/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python null_space_demo.py
```

It prints the singular spectrum, the null-space basis checks, the two equivalent
models, both interval tables and the normal-equation comparison. Runtime is
under a second. Companion problems are in
[`exercises/03-null-space-exercises.md`](exercises/03-null-space-exercises.md).

## Mastery checkpoint

Without notes:

> A $6\times6$ model with a rank-4 kernel is fitted to consistent data. **(a)**
> State the dimension of the equivalence class and the number of independent data
> the experiment actually provided. **(b)** Write down the general form of every
> solution. **(c)** A colleague reports the value of cell 3 with two decimals.
> Give the two questions you must ask before accepting it. **(d)** Why does
> $\kappa(G^{\!\top}G) = \kappa(G)^{2}$, and what is the practical consequence?

Worked solutions are in
[`exercises/03-null-space-solutions.md`](exercises/03-null-space-solutions.md).

## Common pitfalls

1. **Reporting "the" solution of an underdetermined problem.** Report the class,
   or state the selection rule that reduced it to one member.
2. **Confusing structural and trade-off null space.** Empty columns are found by
   inspection; exchange directions are not.
3. **Giving per-parameter intervals without the imposed bounds.** The bound is
   part of the answer.
4. **Interpreting cells instead of resolved combinations.** Only combinations in
   $\operatorname{range}(G^{\!\top})$ are data-determined.
5. **Forming the normal equations.** Same null space, squared condition number.
6. **Assuming extra model parameters add resolution.** They add null space unless
   independent data grow too.

## Related modules

- [18-01-02 Hadamard's Conditions](02-hadamard-well-posedness.md) — uniqueness
  failure as a checklist item, and the tolerance issue in rank counting.
- [18-01-05 Model Space and Data Space](05-model-space-data-space.md) — the same
  subspaces seen as projections, with the unfittable part of the data quantified.
- [18-02-02 Underdetermined Problems and Minimum-Norm Solutions](../02-linear-inverse-problems/02-underdetermined.md) —
  selection rules that pick one member of the class.
- [06-06-03 Resolution, Null Space and Model Covariance](../../06-seismology/06-seismic-tomography/03-resolution-and-nullspace.md) —
  null-space analysis in tomography.
- [05-01-04 Non-Uniqueness of Geophysical Models](../../05-core-geophysics/01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md) —
  the qualitative account this lesson makes exact.
