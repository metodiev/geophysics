---
id: 18-01-05
title: "Model Space, Data Space and Mappings Between Them"
level: graduate
prereqs: ["18-01-01", "18-01-03", "01-16-02"]
tags: [inverse-problems, model-space, data-space, projections, range, rank-nullity]
---

# Model Space, Data Space and Mappings Between Them

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** model space and data space for a given experiment, including their
   dimensions, norms and units.
2. **Decompose** the model space into the data-informed subspace and the effective
   null space, and the data space into $\operatorname{range}(G)$ and its
   orthogonal complement.
3. **Construct** the orthogonal projector $P = GG^{+}$ and **verify** its
   idempotence, symmetry and trace-to-rank identity numerically.
4. **Predict** the fraction of white noise that no model can fit, and **measure**
   it, distinguishing the exact expectation from a single noisy realisation.
5. **Demonstrate** that the forward map is many-to-one and **quantify** how
   different two models with identical data can be.
6. **Explain** and **measure** the difference between the operator $G$ and the
   model-space operator $G^{\!\top}G$: identical null space, squared condition
   number, and loss of resolvable directions.
7. **Choose** the appropriate numerical route (SVD or QR, not normal equations)
   and **justify** the choice with condition numbers.

## Prerequisites

- [18-01-01 Forward vs Inverse Problems](01-forward-and-inverse.md) — the linear
  model, the notation, the units in the kernel.
- [18-01-03 Null Space and Non-Uniqueness](03-null-space.md) — equivalence classes
  and rank-nullity.
- [01-16-02 Hilbert Spaces and Orthogonal Expansions](../../01-mathematics/16-functional-analysis/02-hilbert-spaces.md) —
  orthogonality, projections and the geometry used here.

## 1. Two spaces, one map

Everything in this lesson is geometry in two finite-dimensional inner-product
spaces.

- The **model space** $\mathcal{M} = \mathbb{R}^{M}$ holds the parameters. Its
  inner product defines the norm $\lVert\mathbf{m}\rVert$ with which model
  magnitudes are compared — and *which norm you choose is a physical statement*
  ([18-02-02](../02-linear-inverse-problems/02-underdetermined.md)).
- The **data space** $\mathcal{D} = \mathbb{R}^{N}$ holds the measurements, again
  with a norm. Absolute units differ from model units; the operator carries the
  conversion, as in the gravity kernel
  $G_{ik} = G_N z_k/(x_i^{2}+z_k^{2})^{3/2}$ in
  $\mathrm{mGal\,kg^{-1}}$.

The forward map is linear, $G:\mathcal{M}\to\mathcal{D}$. Its action is not
invertible in either direction in general, and the useful question is not "what is
the inverse" but "**which parts of each space does the map connect**". The answer
is the pair of subspaces

$$\operatorname{range}(G)\subseteq\mathcal{D},\qquad
\mathcal{N}(G)\subseteq\mathcal{M},$$

with the rank-nullity identity
$\dim\operatorname{range}(G) + \dim\mathcal{N}(G) = M$. The complementary
subspace in the data space is significant too:
$\dim\operatorname{range}(G)^{\perp} = N - r$. The data space is thus split into a
part the model can produce and a part it cannot, and the model space into a part
the data see and a part they do not.

All models and data in this module are **SYNTHETIC**.

## 2. The demonstration's geometry

The demonstration uses twelve point masses $50\ \mathrm{m}$ apart inside a
$550\ \mathrm{m}$ interval at about $2\ \mathrm{km}$ depth, observed at twenty
surface stations spread over $\pm9\ \mathrm{km}$. So $M = 12$, $N = 20$. The
relative singular values of $G$ are

$$1,\ 4.206\times10^{-2},\ 1.546\times10^{-3},\ 4.428\times10^{-5},\
8.471\times10^{-7},\ 1.024\times10^{-8},\ 7.795\times10^{-11},\ 3.689\times10^{-13},\
1.030\times10^{-15},\ 5.717\times10^{-17},\ 2.176\times10^{-17},\ 1.083\times10^{-17}.$$

At a relative tolerance of $10^{-10}$ the rank is $6$, so

$$\dim\operatorname{range}(G) = 6,\qquad \dim\mathcal{N}(G) = 12-6 = 6,\qquad
\dim\operatorname{range}(G)^{\perp} = 20-6 = 14 .$$

The spectrum decays smoothly, with no gap, which is characteristic of a
discretised compact kernel: as [18-01-02 §6](02-hadamard-well-posedness.md) showed,
the boundary between "resolved" and "unresolved" is set by the tolerance you
declare, not by the physics.

## 3. The unfittable part of the data

For any data vector $\mathbf{d}\in\mathcal{D}$ the residual of the best
least-squares fit is the component orthogonal to $\operatorname{range}(G)$:

$$\mathbf{r}_{\min} = (I-P)\mathbf{d},\qquad P = GG^{+}.$$

For white noise, the energies split in proportion to the dimensions. Measured over
$2000$ random draws:

$$\text{fit fraction} = 0.3017,\qquad \text{unfittable fraction} = 0.6983,$$

against the exact expectations

$$\frac{r}{N} = \frac{6}{20} = 0.3000,\qquad
\frac{N-r}{N} = \frac{14}{20} = 0.7000 .$$

A single realisation, of course, fluctuates: the first draw in the demonstration
gave $10.937\%$ fit / $89.063\%$ unfittable, which is normal for $N = 20$ and a
reminder that these are *expected* fractions.

The practical rule: **the misfit floor of a linear inversion is
$\sqrt{(N-r)/N}$ times the noise norm.** If that floor is a large fraction of
$\lVert\mathbf{d}\rVert$, no amount of inversion will reduce it; the residual is
noise, and reporting it as a measure of model quality is a mistake.

## 4. The projector, and what its accuracy costs

The demonstration verifies the projector identities with the pseudo-inverse
truncated at a relative tolerance $10^{-10}$:

$$\lVert P^{2}-P\rVert_{\infty} = 2.930\times10^{-9},\qquad
\lVert P^{\!\top}-P\rVert_{\infty} = 3.141\times10^{-9},\qquad
\operatorname{tr}P = 6.000000 = r,$$

$$\lVert PG - G\rVert_{\infty} = 1.321\times10^{-22}.$$

Note the second and third entries: $P$ is symmetric and idempotent, so it is an
*orthogonal* projector, and its trace equals the rank — two checks that catch sign
and transpose errors in an implementation. But the identities hold only to
$\sim3\times10^{-9}$, not machine precision, and the demonstration shows why:

| truncation tolerance | rank | $\kappa$ of retained part | measured $\lVert P^{2}-P\rVert$ | $\varepsilon\kappa$ |
|---|---|---|---|---|
| $10^{-10}$ | 6 | $9.764\times10^{7}$ | $2.930\times10^{-9}$ | $2.2\times10^{-8}$ |
| $10^{-8}$ | 6 | $9.764\times10^{7}$ | $2.930\times10^{-9}$ | $2.2\times10^{-8}$ |
| $10^{-6}$ | 4 | $2.259\times10^{4}$ | $1.740\times10^{-13}$ | $5.0\times10^{-12}$ |
| $10^{-4}$ | 3 | $6.470\times10^{2}$ | $2.828\times10^{-14}$ | $1.4\times10^{-13}$ |

The projector error tracks $\varepsilon\kappa_{\text{retained}}$: an inverse you
can actually use is *not* an exactly orthogonal projector, and a tolerance that
makes the projector exact throws away most of the data. There is no free lunch
between the two.

## 5. The model-space split

Given any model $\mathbf{m}$ the demonstration writes
$\mathbf{m} = \mathbf{m}_{\text{row}} + \mathbf{m}_{\text{null}}$ using the
retained right singular vectors for the first part. Measured for a chosen
$\mathbf{m}_1$:

$$\lVert\mathbf{m}_1\rVert = 3.5525\times10^{10}\ \mathrm{kg},\qquad
\lVert\mathbf{m}_{\text{row}}\rVert = 3.4804\times10^{10}\ \mathrm{kg},\qquad
\lVert\mathbf{m}_{\text{null}}\rVert = 7.1186\times10^{9}\ \mathrm{kg},$$

$$\lVert G\mathbf{m}_{\text{null}}\rVert_\infty = 8.932\times10^{-14}\ \mathrm{mGal},
\qquad \frac{\lVert G\mathbf{m}_{\text{null}}\rVert}{\lVert\mathbf{d}\rVert}
= 3.4\times10^{-13},$$

$$\lVert\mathbf{m}_1\rVert^{2} - \lVert\mathbf{m}_{\text{row}}\rVert^{2}
- \lVert\mathbf{m}_{\text{null}}\rVert^{2} = -5.193\times10^{-16}\
\text{(relative)},$$

the last line being Pythagoras, which holds because the two parts are orthogonal.
So a component carrying $20\%$ of the model norm produces data at
$3.4\times10^{-13}$ of the data norm: a large change in the model that the
experiment cannot see. The comparison with the tolerance is worth doing
explicitly: the truncated directions have relative singular values up to
$7.8\times10^{-11}$, and the measured ratio $1.64\times10^{-12}$ is comfortably
inside that bound, as it must be.

## 6. Many-to-one, measured

Take one fixed data vector $\mathbf{d} = G\mathbf{m}_1$ and generate $500$ models
$\mathbf{m} = \mathbf{m}_1 + Z\mathbf{w}$ with null-space directions $Z$ and
$\lVert\mathbf{w}\rVert$ fixed at $10\%$ of $\lVert\mathbf{m}_1\rVert$:

| quantity | measured |
|---|---|
| worst data discrepancy over the 500 | $1.997\times10^{-12}\ \mathrm{mGal}$ |
| relative discrepancy | $7.556\times10^{-12}$ |
| as a fraction of a $0.1\%$ data error | $1.3\times10^{-8}$ |
| model displacement for every member | $10.0\%$ of $\lVert\mathbf{m}_1\rVert$ |

The forward map is many-to-one and the inverse map is **set-valued**. Every
inversion algorithm therefore contains a selection rule — minimum norm, minimum
roughness, sparsity, a prior distribution — and that rule is an assumption about
the Earth, not a consequence of the data. Module
[18-03](../03-regularization/README.md) is about choosing it honestly and module
[18-05](../05-bayesian-inversion/README.md) about expressing the choice as a prior.

## 7. Fully worked example: $G^{\!\top}G$ versus $G$

For a square operator there is no room for confusion; for a rectangular one there
is. The **normal-equations operator** $G^{\!\top}G$ acts on the model space, and
the demonstration compares it with $G$:

*(a) eigenvalues.* The first four eigenvalues of $G^{\!\top}G$ are
$5.833458\times10^{-23},\ 1.031904\times10^{-25},\ 1.393487\times10^{-28},\
1.143584\times10^{-31}$, matching $\sigma_i^{2}$ for the same four directions to a
maximum relative difference of $1.451\times10^{-8}$. That residual is not
roundoff noise in the comparison: the fourth eigenvalue is only
$(\sigma_4/\sigma_1)^{2} = 2.0\times10^{-9}$ of the first, so *forming* the product
$G^{\!\top}G$ has already discarded about half the significant digits.

*(b) conditioning.* The exact identity is

$$\kappa(G^{\!\top}G) = \kappa(G)^{2}.$$

Measured: $\kappa(G) = 9.764092\times10^{7}$,
$\kappa(G^{\!\top}G) = 8.808476\times10^{15}$, while
$\kappa(G)^{2} = 9.533748\times10^{15}$; the ratio of the measured to the exact
value is $0.923926$. The disagreement is the same effect: the sixth eigenvalue of
$G^{\!\top}G$ is $(\sigma_6/\sigma_1)^{2} \approx 1.0\times10^{-16}$ of the first,
which is at the level of $\varepsilon$, so the identity cannot be *measured* more
accurately than this even though it is exact.

*(c) rank.* The numerical rank of $G^{\!\top}G$ at $10^{-10}$ is $4$, against $6$
for $G$. Forming the normal equations destroys two directions the SVD resolves.

*(d) consequence.* Use the SVD (or a QR factorisation of $G$) for any inverse
problem in this curriculum. The normal equations are an algebraic identity, not a
numerical algorithm.

## 8. Assumptions and regime of validity

- **Linear, discretised, real.** The subspaces above are finite-dimensional. For
  the continuum version see
  [01-16-02](../../01-mathematics/16-functional-analysis/02-hilbert-spaces.md).
- **Unweighted Euclidean norms.** The decomposition
  $\mathcal{D} = \operatorname{range}(G)\oplus\operatorname{range}(G)^{\perp}$ is
  orthogonal in the *unweighted* inner product. With a data covariance
  $C_d \ne \sigma^{2}I$ the orthogonal complement must be taken in the
  $C_d^{-1}$ inner product ([18-02-06](../02-linear-inverse-problems/06-weighting-and-covariance.md)).
- **A declared truncation tolerance.** All rank statements here use $10^{-10}$.
- **Data generated by a model.** The consistency checks (residual $\sim10^{-16}$)
  hold because $\mathbf{d} = G\mathbf{m}_1$; with real data the residuals are set
  by the noise projection of §3.
- **Two-dimensional projections of a $\mathbb{R}^{12}$ problem.** The "spread" and
  "fraction" statements are ensemble or subspace statements; individual
  components vary.

## 9. Running the demonstration

The demonstration for this lesson is [`code/model_space_data_space_demo.py`](code/model_space_data_space_demo.py) — print-only, no network access, fixed seed
`np.random.default_rng(20261014)`.

```bash
cd 18-inverse-problems/01-inverse-problem-foundations/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python model_space_data_space_demo.py
```

It prints the spectrum, the projector checks and tolerance table, the noise-split
statistics, the model-space split, the many-to-one experiment and the
$G^{\!\top}G$ comparison, all with units. Runtime is under half a second.
Companion problems are in
[`exercises/05-model-space-data-space-exercises.md`](exercises/05-model-space-data-space-exercises.md).

## Mastery checkpoint

Without notes:

> A linear experiment has $N = 30$ data, $M = 50$ parameters and numerical rank
> $r = 10$ at the declared tolerance. **(a)** Give the dimensions of
> $\operatorname{range}(G)$, $\mathcal{N}(G)$ and
> $\operatorname{range}(G)^{\perp}$. **(b)** What fraction of white noise can no
> model fit, and what misfit floor does that imply in terms of the noise norm?
> **(c)** State two numerical checks you would apply to a claimed projector $P$
> for this problem. **(d)** A colleague reports the same fit using the normal
> equations. Give two reasons to use their $G$ instead.

Worked solutions are in
[`exercises/05-model-space-data-space-solutions.md`](exercises/05-model-space-data-space-solutions.md).

## Common pitfalls

1. **Calling the residual "model error".** A large part of it is unfittable noise
   by construction.
2. **Using an unweighted orthogonal decomposition when the errors are
   correlated.** The geometry changes with the metric.
3. **Expecting a projector to be exact.** Its accuracy is $\varepsilon\kappa$ of
   the retained part.
4. **Reading a single noise realisation as the expected split.** Use ensemble
   statistics.
5. **Solving normal equations because they are square.** They square the
   condition number and lose resolvable directions.
6. **Forgetting that the selection rule is an assumption.** The data leave an
   entire affine subspace open.

## Related modules

- [18-01-03 Null Space and Non-Uniqueness](03-null-space.md) — same subspaces,
  phrased as feasible intervals.
- [18-01-04 Discretisation and Model Choice](04-discretisation-reality.md) — what
  happens to the geometry when $M$ grows.
- [18-02-03 The Generalised (Moore-Penrose) Inverse](../02-linear-inverse-problems/03-generalized-inverse.md) —
  $G^{+}$ constructed and its properties proved.
- [18-02-05 Resolution and Information Matrices](../02-linear-inverse-problems/05-resolution-matrices.md) —
  practical interpretation of $GG^{+}$ and $G^{+}G$.
- [01-07-08 Singular Value Decomposition](../../01-mathematics/07-linear-algebra/08-svd.md) —
  the algebra in the background.
