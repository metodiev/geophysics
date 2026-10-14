---
id: 18-07-01
title: "Why Joint Inversion: Complementary Sensitivities"
level: research
prereqs: ["18-02-04", "18-03-01"]
tags: [inverse-problems, joint-inversion, multi-physics, resolution, null-space]
---

# Why Joint Inversion: Complementary Sensitivities

> All models and data in this module are **SYNTHETIC**. The operators, truth
> models, noise levels and weights below are chosen teaching ingredients. No
> number is quoted from a published survey or a real data set.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** joint inversion as the simultaneous solution of two or more data
   sets for models that are linked by a stated assumption, and **separate** that
   assumption from the data.
2. **Quantify** complementarity from singular-value spectra and model resolution
   matrices, and **state** what each method resolves alone.
3. **Explain why** combining two operators cannot exceed the union of their
   model-space spans, and **compute** the rank and mean resolution the union buys.
4. **Derive** the joint posterior for a linear problem and **show** how an
   equivalence curve of a single datum is removed by a second datum.
5. **Measure** how the error correlation between two data sets changes the gain,
   and **state** that independence is an assumption, not a measurement.
6. **Distinguish** three coupling philosophies — same-parameter, structural and
   petrophysical — and say which one a given implementation is using.

## Prerequisites

- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../02-linear-inverse-problems/04-svd-analysis-inverse.md) —
  singular values, model resolution, data importance.
- [18-03-01 Why Regularisation Is Physically and Statistically Justified](../03-regularization/01-why-regularize.md) —
  why every inversion needs a prior or a penalty.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../01-inverse-problem-foundations/03-null-space.md) —
  the equivalence classes a single datum leaves.

## 1. What "joint" means, and what it does not

Two surveys measure different physics over the same volume. Method 1 might be a
potential field whose kernel is broad and peaks at depth; method 2 might be a
sounding whose kernel is localised and decays quickly. Writing the two forward
problems separately,

$$\mathbf{d}_1 = G_1\mathbf{m} + \boldsymbol{\epsilon}_1, \qquad
\mathbf{d}_2 = G_2\mathbf{m} + \boldsymbol{\epsilon}_2,$$

*separate* inversion solves each for its own model. *Joint* inversion solves

$$\mathbf{m}^{\ast} = \arg\min_{\mathbf{m}}\;
\|\mathbf{d}_1 - G_1\mathbf{m}\|^2_{C_1^{-1}}
+ \|\mathbf{d}_2 - G_2\mathbf{m}\|^2_{C_2^{-1}}
+ \alpha\,\mathcal{R}(\mathbf{m}),$$

where $\mathcal{R}$ is the prior or coupling term. The two data sets must be
linked to the *same* unknowns, or to unknowns tied by an explicit relation; if
they are not, the word "joint" is decoration. Three linkages are used in
practice, and this module treats them in order:

- **same parameter** (this lesson): both methods see the identical model;
- **structural** (lesson 02): two different properties, forced to share
  geometry;
- **petrophysical** (lesson 03): two different properties, tied by a rock-physics
  relation.

The honest claim for joint inversion is narrow: it exploits the fact that two
different operators have different **null spaces**. It cannot create information;
it can only apply the second operator's constraints to the directions the first
operator leaves free.

## 2. Complementarity, measured

For a linear operator $G$ ($p\times n$), the singular-value decomposition
$G = U\Sigma V^{T}$ gives the model-space directions $V$ ordered by how strongly
the data see them. The rank at a relative cut $t$,

$$r(t) = \#\{i : \sigma_i > t\,\sigma_1\},$$

counts resolved directions, and the model resolution matrix with a prior
$C = (G^{T}C_d^{-1}G + P_0)^{-1}$,

$$R = C\,G^{T}C_d^{-1}G, \qquad R_{jj} \in [0,1],$$

says how much of cell $j$ is recovered rather than smeared into its neighbours.
$\operatorname{tr}R$ is the number of **effective parameters**; $\operatorname{diag}R$
near 0 means the cell is an average.

## 3. Worked example: two operators, one model

`code/joint_inversion_concepts_demo.py` constructs a 40-cell model over
0–19.75 km, a 20-data gravity-like operator

$$G_1[i,j] = \Delta z\,\frac{z_j}{\left(r_i^2+z_j^2\right)^{3/2}},$$

which is the vertical attraction of a horizontal slice of thickness $\Delta z$
(the point-mass result $z/(r^2+z^2)^{3/2}$ times $\Delta z$), and a 10-channel
localised operator $G_2[i,j] = \exp[-(z_j-z_i)^2/2w^2]$ with $w = 1.2$ km.

| quantity | $G_1$ alone | $G_2$ alone | joint |
|---|---|---|---|
| data / model | 20 / 40 | 10 / 40 | 30 / 40 |
| rank at $10^{-3}$ | 6 | 10 | 14 |
| condition number | $2.75\times10^{17}$ | 4.59 | $1.13\times10^{16}$ |
| mean $\operatorname{diag}R$ | 0.1500 | 0.2500 | 0.3500 |
| cells with $\operatorname{diag}R<0.5$ | 37 | 40 | 35 |

Mean $\operatorname{diag}R$ by depth band (km):

| band | $G_1$ | $G_2$ | joint |
|---|---|---|---|
| 0.25–2.25 | 0.4696 | 0.2576 | 0.7637 |
| 2.75–4.75 | 0.2176 | 0.2720 | 0.3424 |
| 5.25–9.75 | 0.1104 | 0.2581 | 0.2696 |
| 10.25–14.75 | 0.0628 | 0.2687 | 0.2706 |
| 15.25–19.75 | 0.0832 | 0.2084 | 0.3067 |

The gravity operator resolves only six directions and concentrates them near
the surface, where its sensitivity is largest; the localised operator resolves
its ten channels and nothing between them. Their union resolves **fourteen** —
more than either, and far less than forty. Complementarity is real and bounded:
both operators are smooth, their spans overlap at low order, and most of the
model remains unresolved even jointly. A joint inversion does not make an
underdetermined problem determined; it makes it less underdetermined.

## 4. Worked example: one datum, an equivalence curve

The same demo studies a two-parameter problem with an exact answer. A single
gravity-like datum measures the product

$$d_1 = H\,\Delta\rho,$$

so it fixes the hyperbola $\Delta\rho = d_1/H$ exactly:

| $H$ (km) | 2.00 | 3.00 | 4.00 | 5.00 | 6.00 |
|---|---|---|---|---|---|
| $\Delta\rho$ (g cm$^{-3}$) | 0.6000 | 0.4000 | 0.3000 | 0.2400 | 0.2000 |
| $H\Delta\rho$ | 1.20000 | 1.20000 | 1.20000 | 1.20000 | 1.20000 |

At the truth $(H,\Delta\rho) = (4.00\ \mathrm{km}, 0.30\ \mathrm{g\,cm^{-3}})$
with $\sigma_1 = 0.020$, the tangent direction is
$(\mathrm{d}H,\mathrm{d}\Delta\rho) \propto (H,-\Delta\rho)$; a step of 0.05 in
that direction changes the product only to second order ($1.19981$, i.e.
$-1.9\times10^{-4}$).

Adding a depth datum $d_2 = H$ with $\sigma_2 = 0.10$ km gives, for
$G = \left(\begin{smallmatrix}\Delta\rho & H\\ 1 & 0\end{smallmatrix}\right)$ and
$C_d = \operatorname{diag}(\sigma_1^2,\sigma_2^2)$,

$$C_{\text{post}} = \left(G^{T}C_d^{-1}G\right)^{-1},\qquad
\sigma_H = 0.1000\ \mathrm{km},\quad
\sigma_{\Delta\rho} = 0.0090\ \mathrm{g\,cm^{-3}},\quad
\rho_{H\Delta\rho} = -0.832 .$$

Note what changed and what did not. $\sigma_H$ is still $0.1000$ km — the second
datum does not improve the quantity it already measures. What it removes is the
**ambiguous combination**: gravity alone leaves $\Delta\rho$ with no finite
standard deviation, and once $H$ is known, the product pins $\Delta\rho$ to
$0.0090$. That is the archetype of what a second datum does.

## 5. The gain depends on an assumption you cannot check

The result above used independent errors. Repeat with
$C_d = \sigma_1\sigma_2\left(\begin{smallmatrix}1&\rho\\ \rho&1\end{smallmatrix}\right)$:

| $\rho$ | $-0.9$ | $-0.6$ | $-0.3$ | 0 | 0.3 | 0.6 | 0.9 |
|---|---|---|---|---|---|---|---|
| $\sigma_{\Delta\rho}$ | 0.0122 | 0.0112 | 0.0102 | 0.0090 | 0.0077 | 0.0060 | 0.0037 |

The reported uncertainty moves by a factor of 3.3 across a plausible range, and
it can move in either direction. $\rho = 0$ is a **choice**, not a measurement:
a wrong datum, a wrong wavelet or a shared structural error enters both data
sets with the same sign. This is the standing warning of the module — the joint
gain is conditional on the error model, and the error model is the weakest part
of most published joint inversions.

## 6. Numeric demonstration

```bash
cd 18-inverse-problems/07-joint-and-multi-physics-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python joint_inversion_concepts_demo.py
```

Printed sections: (1) kernels and depth sensitivity; (2) singular-value spectra,
showing rank 6, 10 and 14; (3) resolution diagonals by band; (4) the joint
operator; (5) the $H\Delta\rho$ equivalence curve and the joint posterior;
(6) the $\rho$ table above. The demo is print-only, seeded with
`np.random.default_rng(20261014)` and exits 0.

## 7. Assumptions and regime of validity

1. **Identical parameterisation.** All operators act on the same $\mathbf{m}$.
   If method 2 sees a different grid, the coupling requires an interpolation
   operator, and that operator is a model.
2. **Known error covariance.** The gain statements are conditional on $C_d$.
   Additivity of information requires independent errors; section 5 measures how
   much a correlation changes the answer.
3. **Linear forward models.** The rank and resolution statements are linear
   algebra. For nonlinear problems they hold locally, about the current model.
4. **A fixed prior.** $R$ and $\operatorname{tr}R$ depend on $P_0$. Two studies
   with different penalties are not comparable.
5. **No new physics.** The joint operator's span is contained in the sum of the
   individual spans. Nothing in this lesson confers information the individual
   operators do not carry.

## Mastery checkpoint

Without notes: **(a)** Write the joint objective for two linear data sets and
state the three coupling philosophies. **(b)** A method alone has rank 6 out of
40 cells; a second has rank 10; explain why the joint rank cannot be 16 in
general and what it was measured to be. **(c)** For the two-parameter problem,
show that the null direction of $d_1 = H\Delta\rho$ is
$(H,-\Delta\rho)$, and compute the product change for a step of 0.20.
**(d)** Compute $C_{\text{post}}$ for $\rho = 0.6$ and state whether the
reported $\sigma_{\Delta\rho}$ is now larger or smaller than at $\rho=0$.

## Common pitfalls

1. **Calling any two-step workflow "joint".** If the two inversions share neither
   parameters, structure nor relations, they are two inversions.
2. **Claiming joint inversion resolves the target.** Report
   $\operatorname{diag}R$ and the admitted ranges, not the picture.
3. **Quoting a gain without the error correlation.** Section 5 is the witness.
4. **Forgetting the prior in the resolution matrix.** $R$ is prior-dependent.
5. **Reading a ridge or a peak as a new structure.** A joint model can add
   apparent structure purely through the coupling term; lesson 05 measures it.

## Related modules

- [07 Joint and Multi-Physics Inversion](README.md) — this module.
- [Structural (Cross-Gradient) Coupling](02-structural-joint-inversion.md) —
  the two-property version, with the coupling term derived.
- [02 Linear Inverse Problems](../02-linear-inverse-problems/README.md) — the
  SVD and resolution machinery used here.
- [06 Uncertainty Quantification](../06-uncertainty-quantification/README.md) —
  propagating the error model that the gain depends on.
- [11 Exploration Geophysics](../../11-exploration-geophysics/README.md) — where
  multi-method surveys are actually designed.

Code: [`code/joint_inversion_concepts_demo.py`](code/joint_inversion_concepts_demo.py).
Exercises: [`exercises/01-joint-inversion-concepts-exercises.md`](exercises/01-joint-inversion-concepts-exercises.md).
