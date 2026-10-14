---
id: 18-07-02
title: "Structural (Cross-Gradient) Coupling"
level: research
prereqs: ["18-07-01"]
tags: [inverse-problems, joint-inversion, cross-gradient, structural-coupling, regularization]
---

# Structural (Cross-Gradient) Coupling

> All models and data in this module are **SYNTHETIC**. The truth models, the
> blur operators and every weight below are chosen teaching ingredients. No
> number is quoted from a published study or a real data set.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the 2-D cross-gradient $t = \nabla m_1 \times \nabla m_2$ and
   **explain** why $t = 0$ is the definition of "shared geometry".
2. **Construct** a joint objective with a cross-gradient penalty and **compute**
   its gradient for a Gauss–Newton or quasi-Newton solver.
3. **Measure** how much structural consistency the penalty buys, and **state**
   the price paid in data misfit.
4. **Derive** the scaling identity $t(\alpha m_1,\beta m_2) = \alpha\beta\,t(m_1,m_2)$
   and **explain** why the penalty sees orientation, not amplitude.
5. **Demonstrate** that a constant model satisfies the penalty exactly, and
   **state** the consequence for weakly constrained models.
6. **Measure** the bias the coupling produces when the two truths are
   structurally different, and **state** the hypothesis the coupling encodes.

## Prerequisites

- [18-07-01 Why Joint Inversion: Complementary Sensitivities](01-joint-inversion-concepts.md) —
  what joint inversion is allowed to claim.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../03-regularization/02-tikhonov.md) —
  the penalty/objective pattern this lesson extends.

## 1. The coupling term

Structural coupling is used when two surveys measure *different properties* that
are believed to share **geometry**: a density contrast and a resistivity contrast
that mark the same body, for example. The properties are different numbers, so
there is nothing to equate; what can be equated is the *direction of change*.

For a 2-D model, the cross-gradient of two property models is

$$\mathbf{t}(\mathbf{m}_1,\mathbf{m}_2) =
\nabla m_1 \times \nabla m_2 =
\left(\partial_x m_1\, \partial_y m_2 - \partial_y m_1\, \partial_x m_2\right)\hat{\mathbf z},$$

and the scalar

$$t = \partial_x m_1\,\partial_y m_2 - \partial_y m_1\,\partial_x m_2
= |\nabla m_1|\,|\nabla m_2|\sin\theta$$

vanishes exactly where the two gradients are parallel — including where either
gradient vanishes. The penalty $\lambda_x\sum t_i^2$ is added to

$$\Phi = \|G_1\mathbf{m}_1-\mathbf{d}_1\|^2 + \|G_2\mathbf{m}_2-\mathbf{d}_2\|^2
+ \lambda_s\left(\|\nabla\mathbf{m}_1\|^2+\|\nabla\mathbf{m}_2\|^2\right)
+ \lambda_x\sum_i t_i^2 .$$

## 2. The gradient of the penalty

Write $t = (D_x\mathbf{m}_1)\odot(D_y\mathbf{m}_2) - (D_y\mathbf{m}_1)\odot(D_x\mathbf{m}_2)$
with finite-difference matrices $D_x,D_y$ and Hadamard product $\odot$. Then

$$\frac{\partial}{\partial\mathbf{m}_1}\sum_i t_i^2
= 2\left(D_x^{T}\operatorname{diag}(D_y\mathbf{m}_2)
        - D_y^{T}\operatorname{diag}(D_x\mathbf{m}_2)\right)\mathbf{t},$$

$$\frac{\partial}{\partial\mathbf{m}_2}\sum_i t_i^2
= 2\left(D_y^{T}\operatorname{diag}(D_x\mathbf{m}_1)
        - D_x^{T}\operatorname{diag}(D_y\mathbf{m}_1)\right)\mathbf{t}.$$

Adding the linear data and smoothness gradients gives an analytic gradient
suitable for L-BFGS. The demo does exactly this: 20x20 cells, two properties,
two anisotropic blur-and-subsample operators of 140 data each.

## 3. Worked example: what the coupling buys

Truth: model 1 is a dipping band; model 2 is the same band with a different
amplitude plus a constant offset, so the gradients are parallel and
$\mathrm{rms}\,|t| = 8.2\times10^{-18}$. Method 1 blurs strongly in $x$ (band
resolved only vertically); method 2 blurs strongly in $y$ and carries 15% noise.
With $\lambda_s = 0.02$:

| $\lambda_x$ | $\mathrm{rms}\,|t|$ | misfit 1 | misfit 2 | error 1 | error 2 |
|---|---|---|---|---|---|
| 0 | $3.337\times10^{-3}$ | 0.0147 | 0.0155 | 0.0851 | 0.0772 |
| 0.3 | $2.997\times10^{-3}$ | 0.0147 | 0.0156 | 0.0851 | 0.0766 |
| **1.0** | $\mathbf{2.452\times10^{-3}}$ | 0.0148 | 0.0158 | **0.0847** | **0.0764** |
| 3.0 | $5.455\times10^{-3}$ | 0.0160 | 0.0162 | 0.0929 | 0.0765 |
| 10.0 | $7.914\times10^{-3}$ | 0.0237 | 0.0221 | 0.1081 | 0.0987 |
| 30.0 | $7.305\times10^{-3}$ | 0.0642 | 0.0564 | 0.1591 | 0.1355 |

At $\lambda_x=1$ the structural disagreement falls by 27% and both model errors
fall slightly (0.0851 → 0.0847, 0.0772 → 0.0764) for misfits that rise by 0% and
2%. That is the *whole* measured gain in this experiment — real, modest, and
paid for in misfit. Beyond $\lambda_x = 3$ both misfits and both model errors
rise steeply: the data are now fighting the penalty.

## 4. What the penalty constrains — and the flat-model loophole

Two exact properties make the term's limits visible.

*Scaling.* $t(\alpha\mathbf{m}_1,\beta\mathbf{m}_2) = \alpha\beta\,t(\mathbf{m}_1,\mathbf{m}_2)$.
The demo verifies this on its own solutions,
$\max|t(2\mathbf{s}_1,0.5\mathbf{s}_2) - 1.0\,t(\mathbf{s}_1,\mathbf{s}_2)| = 0.000$
to double precision. The penalty therefore measures **orientation**; it says
nothing about amplitude, and it cannot pin an amplitude ambiguity.

*Flatness.* For two constant models, $\nabla m_1 = \nabla m_2 = 0$ and
$\mathrm{rms}\,|t| = 0.000$ exactly — the penalty's global minimum includes the
least informative models in the space. In the sweep the model variances barely
move (model 1: 0.0884 → 0.0890; model 2: 0.0282 → 0.0233) while the misfits rise
to 0.0642/0.0564. The penalty does not flatten the model; it relocates and
suppresses structure where the data resist it. Either way, **it cannot create
structure that neither data set supports.**

## 5. Failure mode: coupling two different structures

Now model 2 is a blob away from the band: the hypothesis is false.

| $\lambda_x$ | error 1 | error 2 | misfit 1 | misfit 2 |
|---|---|---|---|---|
| 0 | 0.0837 | 0.0222 | 0.0151 | 0.0107 |
| 1 | 0.0841 | 0.0285 | 0.0150 | 0.0112 |
| 10 | 0.1015 | 0.0678 | 0.0210 | 0.0203 |
| 100 | 0.1654 | 0.0753 | 0.0526 | 0.0315 |

Error 2 rises monotonically with the weight: the penalty forces the blob towards
the band's geometry, which the second method's data do not support. Both misfits
rise. Cross-gradient coupling is a **physical hypothesis — shared geometry — and
an unexamined hypothesis is a systematic bias.** The residual is the only
alarm, and it is a good one.

## 6. Numeric demonstration

```bash
cd 18-inverse-problems/07-joint-and-multi-physics-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python structural_cross_gradient_demo.py
```

Five sections: the two truths; separate inversions; the weight sweep; the
scaling and flatness checks; the inconsistent-truth failure. The full script runs
in about five seconds. Print-only, seeded, exits 0.

## 7. Assumptions and regime of validity

1. **Shared geometry is a hypothesis about the Earth**, not a property of the
   data. Test it before trusting it (section 5).
2. **Regularisation balance.** The result is a function of $\lambda_s$ and
   $\lambda_x$ jointly; changing the smoothing changes the "optimum" coupling.
   Report both.
3. **Differentiability.** The term assumes smooth property fields; it is poorly
   defined for models with jump discontinuities unless the derivative operators
   are chosen carefully.
4. **Scale invariance limits it.** Because $t$ is amplitude-blind, structural
   coupling cannot fix an amplitude ambiguity — use a petrophysical relation
   (lesson 03) for that.
5. **The flat minimum is global.** Any report must show that the coupled model
   retains the structure the data support, not just that $t$ is small.

## Mastery checkpoint

Without notes: **(a)** Derive $t = |\nabla m_1||\nabla m_2|\sin\theta$ from the
component form. **(b)** Write the two gradient expressions of section 2 and
verify the sign of the second term. **(c)** Given the sweep, choose
$\lambda_x$ for a study that must keep both misfits within 10% of their
uncoupled values, and justify the choice with numbers. **(d)** Explain, using the
scaling identity, why a joint inversion with cross-gradient coupling cannot
determine the amplitude of either property.

## Common pitfalls

1. **Reporting the coupled model as more reliable without the misfits.** Every
   row of the sweep is a trade; show the trade.
2. **Tuning $\lambda_x$ against a synthetic truth.** Tune it against the misfit
   level, then verify on the truth once.
3. **Assuming zero cross-gradient means correct structure.** Flat models have
   zero cross-gradient.
4. **Forgetting that the hypothesis can be false.** Section 5 is why.
5. **Applying 3-D intuition to a 2-D scalar.** In 3-D the cross-gradient is a
   vector; the vanishing condition is different and the penalty needs care.

## Related modules

- [Why Joint Inversion: Complementary Sensitivities](01-joint-inversion-concepts.md).
- [Petrophysically Coupled Joint Inversion](03-petrophysical-joint-inversion.md) —
  the amplitude-aware alternative.
- [Pitfalls: Inconsistent Physics, Weighting, Over-Coupling](05-joint-inversion-pitfalls.md) —
  the weight trade-off in full.
- [03 Regularisation and Stabilisation](../03-regularization/README.md).

Code: [`code/structural_cross_gradient_demo.py`](code/structural_cross_gradient_demo.py).
Exercises: [`exercises/02-structural-joint-inversion-exercises.md`](exercises/02-structural-joint-inversion-exercises.md).
