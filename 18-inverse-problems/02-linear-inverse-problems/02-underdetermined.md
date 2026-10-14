---
id: 18-02-02
title: "Underdetermined Problems and Minimum-Norm Solutions"
level: advanced
prereqs: ["18-02-01", "18-01-03", "01-07-08"]
tags: [inverse-problems, underdetermined, minimum-norm, selection-rule, sparsity, tomography]
---

# Underdetermined Problems and Minimum-Norm Solutions

## Learning objectives

By the end of this lesson you will be able to:

1. **Recognise** the underdetermined regime from the dimensions and the rank, and
   **state** what is and is not determined.
2. **Derive** the minimum-norm solution
   $\hat{\mathbf{m}} = G^{\!\top}(GG^{\!\top})^{-1}\mathbf{d}$ and explain why it
   is the projection of the origin onto the feasible set.
3. **Verify** the two defining properties: membership in
   $\operatorname{range}(G^{\!\top})$ and minimality of the norm.
4. **Show** that the feasible set is an affine subspace of dimension
   $M-\operatorname{rank}(G)$ and **measure** how its members differ.
5. **Compare** three selection rules — minimum norm, minimum roughness, sparsity —
   on the same data, and **state** the physical assumption each encodes.
6. **Report** a resolved combination or a feasible interval instead of a bare
   parameter value.

## Prerequisites

- [18-02-01 Overdetermined Problems and Least Squares](01-overdetermined.md) —
  the projection geometry and the covariance language used again here.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../01-inverse-problem-foundations/03-null-space.md) —
  the equivalence class this lesson selects from.
- [01-07-08 Singular Value Decomposition](../../01-mathematics/07-linear-algebra/08-svd.md) —
  the basis in which the minimum-norm solution is written.

## 1. The underdetermined case

With $N<M$ and full row rank, the system

$$G\mathbf{m} = \mathbf{d},\qquad G\in\mathbb{R}^{N\times M},\ N<M$$

has **infinitely many exact solutions** as soon as it has one: the solution set is

$$\mathcal{M}(\mathbf{d}) = \mathbf{m}_0 + \mathcal{N}(G),
\qquad \dim\mathcal{N}(G) = M - \operatorname{rank}(G) > 0 .$$

Nothing in the data chooses among them. An algorithm must add a **selection
rule**, and every selection rule is an assumption about the Earth. This lesson
treats the most common rule — minimum norm — derives it, tests its properties, and
then compares it with two others to make the point that the rule, not the data,
produces the picture.

The demonstration is a SYNTHETIC transmission problem: $M = 8$ cells, each holding
one slowness value in $\mathrm{s\,km^{-1}}$, and $N = 3$ rays whose measurement is
the sum of the cells they cross.

| ray | cells |
|---|---|
| R1 | 0, 1, 2, 3 |
| R2 | 2, 3, 4, 5 |
| R3 | 4, 5, 6, 7 |

The data are generated from a chosen model and are noise-free, so all
non-uniqueness below is exact:

$$\mathbf{d} = (0.900,\ 0.760,\ 0.800)\ \mathrm{s},\qquad
\sigma(G) = (2.6131,\ 2.0000,\ 1.0824),$$

with $\operatorname{rank}(G) = 3$ and $\dim\mathcal{N}(G) = 5$.

All models and data in this module are **SYNTHETIC**.

## 2. Deriving the minimum-norm solution

Minimise $\lVert\mathbf{m}\rVert^{2}$ subject to $G\mathbf{m}=\mathbf{d}$. Introduce
a Lagrange multiplier $\boldsymbol{\lambda}\in\mathbb{R}^{N}$:

$$\mathcal{L}(\mathbf{m},\boldsymbol{\lambda})
= \tfrac12\mathbf{m}^{\!\top}\mathbf{m}
+ \boldsymbol{\lambda}^{\!\top}(\mathbf{d}-G\mathbf{m}),$$

$$\nabla_{\mathbf{m}}\mathcal{L} = \mathbf{m} - G^{\!\top}\boldsymbol{\lambda}
= \mathbf{0}\quad\Longrightarrow\quad \mathbf{m} = G^{\!\top}\boldsymbol{\lambda},$$

so **the minimiser lies in $\operatorname{range}(G^{\!\top})$** — that is the first
defining property, and it is visible in the derivation rather than asserted.
Substituting into the constraint,

$$G G^{\!\top}\boldsymbol{\lambda} = \mathbf{d}
\quad\Longrightarrow\quad
\boldsymbol{\lambda} = (GG^{\!\top})^{-1}\mathbf{d}
\quad\Longrightarrow\quad
\boxed{\;\hat{\mathbf{m}} = G^{\!\top}(GG^{\!\top})^{-1}\mathbf{d}\;}$$

with $GG^{\!\top}$ invertible precisely when $G$ has full row rank. In singular
value terms $\hat{\mathbf{m}} = \sum_{i=1}^{N} (\mathbf{u}_i^{\!\top}\mathbf{d}/\sigma_i)
\,\mathbf{v}_i$, the same truncated-SVD formula used everywhere else in this folder.

Measured in the demonstration:

$$\hat{\mathbf{m}} = (0.2475,\ 0.2475,\ 0.2025,\ 0.2025,\ 0.1775,\ 0.1775,\
0.2225,\ 0.2225)\ \mathrm{s\,km^{-1}},$$

$$\lVert\hat{\mathbf{m}}\rVert = 0.605434\ \mathrm{s\,km^{-1}},\qquad
\lVert G\hat{\mathbf{m}}-\mathbf{d}\rVert_{\infty} = 2.220\times10^{-16}\ \mathrm{s},$$

and the two constructions agree:
$\lVert G^{\!\top}(GG^{\!\top})^{-1}\mathbf{d}-\hat{\mathbf{m}}\rVert_{\infty}
= 8.327\times10^{-17}$. The projection test
$\lVert\hat{\mathbf{m}} - P_{\text{row}}\hat{\mathbf{m}}\rVert
= 2.272\times10^{-16}$ confirms property 1 numerically.

## 3. Minimality, verified rather than assumed

Property 2 is that no feasible model has a smaller norm. Because every feasible
model is $\hat{\mathbf{m}}+Z\mathbf{w}$ with $Z$ an orthonormal basis of
$\mathcal{N}(G)$ and $\hat{\mathbf{m}}\perp Z$,

$$\lVert\hat{\mathbf{m}}+Z\mathbf{w}\rVert^{2}
= \lVert\hat{\mathbf{m}}\rVert^{2} + \lVert\mathbf{w}\rVert^{2}
\ \ge\ \lVert\hat{\mathbf{m}}\rVert^{2},$$

with equality only at $\mathbf{w}=\mathbf{0}$. The demonstration sweeps the
amplitude and confirms the identity numerically:

| $\lVert\mathbf{w}\rVert$ | measured $\lVert\mathbf{m}\rVert$ | $\sqrt{\lVert\hat{\mathbf{m}}\rVert^{2}+\lVert\mathbf{w}\rVert^{2}}$ |
|---|---|---|
| 0.00 | 0.605434 | 0.605434 |
| 0.01 | 0.605516 | 0.605516 |
| 0.05 | 0.607495 | 0.607495 |
| 0.20 | 0.637613 | 0.637613 |
| 0.50 | 0.785207 | 0.785207 |

Two things follow that are easy to get wrong:

- the **norm is not a discriminating statistic** among feasible models: it is
  fixed by $\lVert\mathbf{w}\rVert$ alone, so two very different models can have
  identical norms;
- the minimum is attained exactly at $\mathbf{w}=\mathbf{0}$, i.e. the estimate is
  the point of the feasible set closest to the origin — a *geometric* statement
  about the origin, not a physical preference for small slowness.

## 4. What varies inside the feasible set

Fix the null-space amplitude at $\lVert\mathbf{w}\rVert = 0.2\ \mathrm{s\,km^{-1}}$
and draw 2000 members of the feasible set:

| quantity | min | max | spread |
|---|---|---|---|
| $m_0$ | 0.0922 | 0.4027 | 0.3105 |
| $m_1$ | 0.0920 | 0.4030 | 0.3110 |
| $m_2$ | 0.0481 | 0.3560 | 0.3079 |
| $m_3$ | 0.0487 | 0.3561 | 0.3074 |
| $m_0+m_1+m_2+m_3$ (ray 1) | 0.9000 | 0.9000 | **0.0000** |
| $\lVert\mathbf{m}\rVert$ | 0.6376 | 0.6376 | **0.0000** |

Every member satisfies $G\mathbf{m}=\mathbf{d}$ to $\le3.33\times10^{-16}\ \mathrm{s}$.
Individual cells move by $0.31\ \mathrm{s\,km^{-1}}$ — comparable to the data
values themselves — while the ray sum is pinned to $0.9000\ \mathrm{s}$ and the
norm is constant by construction. The interpretation that survives is about the
**sums along the rays**, because those are the measurements.

Solving the linear programmes over $0\le m_j\le1$ gives the honest per-cell
report:

| cells | feasible interval | width |
|---|---|---|
| 0, 1 | $[0.0000,\ 0.9000]$ | 0.9000 |
| 2, 3, 4, 5 | $[0.0000,\ 0.7600]$ | 0.7600 |
| 6, 7 | $[0.0000,\ 0.8000]$ | 0.8000 |
| ray-1 sum | $[0.9000,\ 0.9000]$ | 0.0000 |

Every cell has lower bound zero: each shares its rays with partners that can carry
the whole load, so no unit of slowness is *required* in any particular cell.

## 5. Three selection rules, one identical fit

The same three numbers can be explained by very different fields. With
$D$ the first-difference operator and an $L_{1}$ penalty solved as a linear
programme:

| rule | $\lVert\mathbf{m}\rVert_2$ | $\lVert D\mathbf{m}\rVert_2$ | $\lVert\mathbf{m}\rVert_1$ | non-zero cells | $\lVert G\mathbf{m}-\mathbf{d}\rVert_\infty$ |
|---|---|---|---|---|---|
| minimum norm | 0.6054 | 0.0684 | 1.7000 | 8 | $2.22\times10^{-16}$ |
| minimum roughness | 0.6060 | 0.0541 | 1.7000 | 8 | $1.11\times10^{-16}$ |
| sparse ($L_{1}$) | 1.1786 | 1.4030 | 1.7000 | 3 | $0.00\times10^{0}$ |

and the actual models:

$$\mathbf{m}_{\text{norm}} = (0.2475, 0.2475, 0.2025, 0.2025, 0.1775, 0.1775,
0.2225, 0.2225),$$
$$\mathbf{m}_{\text{rough}} = (0.2607, 0.2434, 0.2089, 0.1870, 0.1780, 0.1861,
0.2116, 0.2243),$$
$$\mathbf{m}_{\text{sparse}} = (0.9000, 0, 0, 0, 0.7600, 0, 0.0400, 0).$$

All three fit the data to machine precision and they are physically different
pictures: a broadly spread field, a gently varying field, and a field confined to
three cells. The $L_{1}$ solution has the *largest* two-norm ($1.95\times$ the
minimum-norm value) — sparsity is not smallness. What separates the rules is the
assumption they encode:

- **minimum norm** says "structure is spread out and small" — appropriate when
  anomalies are diffuse, and the reason it is the default;
- **minimum roughness** says "the field is smooth" — appropriate for a continuous
  medium, and the discrete ancestor of Tikhonov regularisation
  ([18-03-02](../03-regularization/02-tikhonov.md));
- **$L_{1}$ sparsity** says "few cells are anomalous" — appropriate for
  compartmentalised or interface-dominated targets
  ([18-03-04](../03-regularization/04-sparsity.md)).

## 6. Fully worked example: the arithmetic of §2

*(a) Build $GG^{\!\top}$.* Each ray covers four cells (unit weights), so

$$GG^{\!\top} = \begin{pmatrix} 4 & 2 & 0\\ 2 & 4 & 2\\ 0 & 2 & 4\end{pmatrix},
\qquad \det = 4(16-4) - 2(8-0) = 48-16 = 32 \neq 0 .$$

*(b) Solve for the multipliers.*
$\boldsymbol{\lambda} = (GG^{\!\top})^{-1}\mathbf{d}
= (0.2475,\ -0.0450,\ 0.2225)$ for $\mathbf{d} = (0.9,0.76,0.8)$, and

$$\hat{\mathbf{m}} = G^{\!\top}\boldsymbol{\lambda}
= (\lambda_1,\lambda_1,\lambda_1{+}\lambda_2,\lambda_1{+}\lambda_2,
\lambda_2{+}\lambda_3,\lambda_2{+}\lambda_3,\lambda_3,\lambda_3)$$

gives exactly the vector printed in §2: cells 0–1 are $\lambda_1 = 0.2475$,
cells 2–3 are $\lambda_1+\lambda_2 = 0.2025$, cells 4–5 are
$\lambda_2+\lambda_3 = 0.1775$, and cells 6–7 are $\lambda_3 = 0.2225$. Note that
$\lambda_2$ is *negative*: the multipliers are bookkeeping variables, not
physical cell values.

*(c) Check the fit.* $G\hat{\mathbf{m}} = (0.9, 0.76, 0.8)$ to
$2.2\times10^{-16}\ \mathrm{s}$, i.e. exact.

*(d) Interpret honestly.* Because $m_0$ and $m_1$ appear only in ray 1, only their
sum is measured; the split is pure assumption. A defensible sentence is: "the
ray-1 travel-time residual is $0.900\ \mathrm{s}$, distributed over cells 0–3 with
individual weights determined only by the norm-minimising rule."

## 7. Assumptions and regime of validity

- **Exact, consistent data.** With noise the feasible set becomes a set of
  near-solutions, and the minimum-norm rule becomes a regularised estimator whose
  bias grows with the noise ([18-03-02](../03-regularization/02-tikhonov.md)).
- **A stated norm.** "Minimum norm" is meaningless without the norm; the
  demonstration uses the Euclidean norm on slowness values. Weighting cells by
  volume changes which model is "small"
  ([18-02-06](06-weighting-and-covariance.md)).
- **Full row rank.** $GG^{\!\top}$ must be invertible. Otherwise use
  $G^{+}$ ([18-02-03](03-generalized-inverse.md)), which handles rank deficiency
  and reduces to this formula when the rank condition holds.
- **A linear forward operator.** For nonlinear problems the feasible set is a
  curved manifold and the selection rule must be applied iteratively
  ([18-04-02](../04-nonlinear-inversion/02-gradient-and-newton.md)).
- **Model parameters as independent cells.** If the physics constrains admissible
  fields (bounds, smoothness, entropy), the constrained minimum is the right
  object, as the interval table of §4 shows.

## 8. Running the demonstration

The demonstration for this lesson is [`code/underdetermined_demo.py`](code/underdetermined_demo.py) — print-only, no network access, fixed seed
`np.random.default_rng(20261014)`.

```bash
cd 18-inverse-problems/02-linear-inverse-problems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python underdetermined_demo.py
```

It prints the system, the two properties of the minimum-norm solution, the sampled
feasible set, the three selection rules and the interval table, all with units.
Runtime is under a second. Companion problems are in
[`exercises/02-underdetermined-exercises.md`](exercises/02-underdetermined-exercises.md).

## Mastery checkpoint

Without notes:

> Three rays measure sums over eight cells. **(a)** State the dimension of the
> feasible set and the general form of every solution. **(b)** Derive
> $\hat{\mathbf{m}} = G^{\!\top}(GG^{\!\top})^{-1}\mathbf{d}$ and explain why the
> answer contains no null-space component. **(c)** A reviewer objects that the
> minimum-norm model has "smeared the anomaly". Give the correct response in two
> sentences. **(d)** You believe the target is a single compartment. Which
> selection rule would you use, and what must you report alongside the resulting
> model?

Worked solutions are in
[`exercises/02-underdetermined-solutions.md`](exercises/02-underdetermined-solutions.md).

## Common pitfalls

1. **Reporting the minimum-norm model as "the" model.** It is the model closest to
   the origin in the chosen norm — a rule, not a measurement.
2. **Assuming sparsity is a form of minimum norm.** The $L_{1}$ solution here has
   twice the two-norm.
3. **Comparing models by their norms.** Feasible models with the same data can
   share norms exactly.
4. **Quoting a cell value whose feasible interval spans zero.** Check the interval.
5. **Forgetting the units of the norm.** Slowness per cell is not a physical
   measure unless cells are equal in size.
6. **Confusing exact fit with good model.** Every member of an $M-N$ dimensional
   family fits exactly.

## Related modules

- [18-02-01 Overdetermined Problems and Least Squares](01-overdetermined.md) —
  the complementary regime.
- [18-02-03 The Generalised (Moore-Penrose) Inverse](03-generalized-inverse.md) —
  one operator for both regimes.
- [18-03-04 L1 Regularisation, Sparsity and Compressive Sensing](../03-regularization/04-sparsity.md) —
  the sparse rule in full.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../01-inverse-problem-foundations/03-null-space.md) —
  intervals and resolved combinations.
- [18-05-03 Priors: Informative, Reference and Their Influence](../05-bayesian-inversion/03-priors.md) —
  the same selection rules expressed as prior distributions.
