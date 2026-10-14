---
id: 18-07-03
title: "Petrophysically Coupled Joint Inversion"
level: research
prereqs: ["18-07-01", "18-07-02"]
tags: [inverse-problems, joint-inversion, petrophysics, rock-physics, coupling]
---

# Petrophysically Coupled Joint Inversion

> All models and data in this module are **SYNTHETIC**. The relation
> $m_2 = 0.70\,m_1 + 0.20$ is a chosen teaching relation, not a laboratory law,
> and no number below is quoted from a published rock-physics study.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** a joint objective with a petrophysical penalty
   $\lambda_p\|m_2 - f(m_1)\|^2$ and **write** the normal equations it implies.
2. **Measure** the reduction in a weakly observed property's model error as a
   function of $\lambda_p$, and **identify** the weight at which it is minimal.
3. **Explain** why the error is not monotonically decreasing: the relation is
   information, and a relation that is only approximately true also destroys
   real structure.
4. **Quantify** the bias produced by a wrong relation and **state** the residual
   signature that reveals it.
5. **Compare** known-relation coupling with clustering-based coupling
   (fuzzy $c$-means) and **state** why estimating the relation from the models
   themselves is circular.
6. **Derive** the three-parameter trade-off among data misfit, prior strength and
   coupling strength for a two-property problem.

## Prerequisites

- [18-07-01 Why Joint Inversion: Complementary Sensitivities](01-joint-inversion-concepts.md) —
  what information a second data set can add.
- [18-07-02 Structural (Cross-Gradient) Coupling](02-structural-joint-inversion.md) —
  the amplitude-blind alternative, whose weakness this lesson repairs.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../03-regularization/02-tikhonov.md).

## 1. Coupling different properties through physics

Structural coupling (lesson 02) ties two properties by their *geometry*. It is
amplitude-blind, so it cannot decide how large a density contrast is. A
petrophysical relation ties them by *values*:

$$m_2 = f(m_1) + \delta, \qquad \delta \sim \mathcal{N}(0,\sigma_p^2),$$

where $f$ comes from laboratory calibration, from well logs, or from a
statistical model of an ensemble. The joint objective becomes

$$\Phi(\mathbf{m}_1,\mathbf{m}_2) =
\|\mathbf{d}_1-G_1\mathbf{m}_1\|^2
+ \|\mathbf{d}_2-G_2\mathbf{m}_2\|^2
+ \lambda_s\left(\|\nabla\mathbf{m}_1\|^2+\|\nabla\mathbf{m}_2\|^2\right)
+ \lambda_p\| \mathbf{m}_2 - a\mathbf{m}_1 - b\|^2 .$$

For a linear $f$ the objective is quadratic and the normal equations are a
$2n\times2n$ linear system; the demo solves it with `numpy.linalg.lstsq`.
Nonlinear $f$ needs an outer linearisation, which is what the clustering variant
does.

## 2. Worked example: the gain, and its optimum

`code/petrophysical_coupling_demo.py` builds 30 cells with a well-observed
property 1 (15 samples, blur 1.2 cells, 1% noise) and a poorly observed property
2 (8 samples, blur 2.5 cells, 20% noise). The truth satisfies
$m_2 = 0.70\,m_1 + 0.20$ **plus** a deviation of rms $0.1061$ — real structure
that no linear relation knows about.

Uncoupled: property 1 error $0.0118$, property 2 error $0.0599$; the
petrophysical residual is $0.1336$.

| $\lambda_p$ | error 1 | error 2 | misfit 1 | misfit 2 | petro residual |
|---|---|---|---|---|---|
| 0 | 0.0118 | 0.0599 | 0.0042 | 0.0082 | 0.1336 |
| **0.05** | 0.0113 | **0.0423** | 0.0082 | 0.0277 | 0.0928 |
| 0.2 | 0.0157 | 0.0575 | 0.0156 | 0.0521 | 0.0513 |
| 0.5 | 0.0217 | 0.0728 | 0.0206 | 0.0668 | 0.0276 |
| 1.0 | 0.0255 | 0.0810 | 0.0233 | 0.0743 | 0.0157 |
| 2.0 | 0.0280 | 0.0860 | 0.0249 | 0.0788 | 0.0084 |
| 5.0 | 0.0298 | 0.0895 | 0.0261 | 0.0819 | 0.0035 |
| 20.0 | 0.0307 | 0.0913 | 0.0267 | 0.0836 | 0.0009 |

Three facts to read off:

1. The error of the weak property falls by 29% at $\lambda_p = 0.05$ — a real
   gain, exactly the kind of transfer lesson 01 promised.
2. Property 2's misfit rises to $0.0277$, which is $0.67$ of its own stated noise
   level ($0.0411$, i.e. $20\%$ of the data rms): the relation is used while that
   data set's fit stays inside what its noise allows. Property 1's misfit also
   rises, to $0.0082$ against a noise level of $0.0031$ (chi $2.65$), because the
   coupling drags the well-observed property towards the relation. Both numbers
   must be reported together — the gain is paid for out of the better data set.
3. Beyond $\lambda_p \approx 0.1$ the misfit exceeds the noise level
   ($0.0521/0.0411 = 1.27$ at $\lambda_p = 0.2$) and the model error rises again,
   because the deviation is being erased.

## 3. Why the optimum is finite

The deviation has rms $0.1061$; as $\lambda_p \to \infty$ the recovered
property 2 converges onto the relation and its error converges to a plateau of
$0.0918$, with the excess over the deviation-free model falling to
$0.0219$. A relation that is 90% right still imposes its 10% error at full
weight. The trade-off is bias versus variance of exactly the Tikhonov kind, with
the relation playing the role of the prior:

$$\underbrace{\|\mathbf{m}_2 - f(\mathbf{m}_1)\|^2}_{\text{bias bought}}
\quad\text{versus}\quad
\underbrace{\sigma_2^2\,\|\text{model freedom}\|^2}_{\text{variance bought}} .$$

There is a best weight. It is not zero, and it is not infinity.

## 4. Failure mode: a wrong relation

Assume $m_2 = 1.10\,m_1 - 0.10$ (truth $0.70$, $0.20$):

| $\lambda_p$ | error 1 | error 2 | misfit 1 | misfit 2 | residual to truth |
|---|---|---|---|---|---|
| 0 | 0.0118 | 0.0599 | 0.0042 | 0.0082 | 0.1336 |
| 0.2 | 0.0413 | 0.0918 | 0.0405 | 0.0788 | 0.0884 |
| 1.0 | 0.0640 | 0.1331 | 0.0592 | 0.1129 | 0.1229 |
| 5.0 | 0.0717 | 0.1467 | 0.0654 | 0.1241 | 0.1373 |
| 20.0 | 0.0734 | 0.1496 | 0.0667 | 0.1265 | 0.1405 |

The wrong relation is imposed just as effectively as the right one: error 2 grows
from $0.0599$ to $0.1496$, and property 2's misfit rises to $0.1265$, about
three times its noise level of $0.0411$. **The rising misfit is the only warning
the inversion gives, and it is a good one** — but it fires only if the relation is
tested against independent data. A relation believed because it was calibrated
once, elsewhere, produces a confident and systematically wrong model.

## 5. Clustering-based coupling and its circularity

When no single relation is defensible, the standard refinement is to let the
relation be *piecewise*: cluster the model cells in property space with fuzzy
$c$-means, fit one line per cluster, and penalise deviations from the local line:

$$u_{ic} = \frac{1}{\sum_{j}\left(d_{ic}/d_{jc}\right)^{2/(\nu-1)}},\qquad
\nu_c = \frac{\sum_i u_{ic}^{\,\nu}\mathbf{x}_i}{\sum_i u_{ic}^{\,\nu}},\qquad
\Phi_p = \lambda_p\sum_i\sum_c u_{ic}^{\,\nu}\left(m_{2i}-a_c m_{1i}-b_c\right)^2 .$$

Iterating {cluster, fit lines, solve for $(\mathbf{m}_1,\mathbf{m}_2)$} is the
classical petrophysically coupled scheme. Its honest difficulty: the clusters
and the lines are estimated **from the models being inverted**, so if the
uncoupled models are scattered the fitted relations are wrong, and the coupling
then imposes them. The number of clusters is an assumed prior over rock units; a
wrong number is a systematic error the data misfit will not reveal unless the
relation is tested against independent data.

## 6. Numeric demonstration

```bash
cd 18-inverse-problems/07-joint-and-multi-physics-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python petrophysical_coupling_demo.py
```

Five sections: the two properties and their noise levels; separate inversions;
the true-relation sweep; the approximate-relation optimum; the wrong-relation
failure. Print-only, seeded, exits 0.

## 7. Assumptions and regime of validity

1. **The relation is a model.** It has a provenance (lab, logs, ensemble) and an
   error bar; neither is in the penalty unless you put it there.
2. **One-to-one relations only.** Real rocks can have two units with the same
   $m_1$ and different $m_2$; a single-valued $f$ then biases the result. Use
   clustering, and test the cluster count.
3. **Linear penalty, linear data.** The quadratic optimum statement is for
   linear $G$ and linear $f$; nonlinear cases inherit local-minimum behaviour.
4. **The misfit of the coupled property must be watched.** In both sweeps it is
   the diagnostic that distinguishes "relation is helping" from "relation is
   overriding".
5. **Property units.** $\lambda_p$ depends on the units of the residual; normalise
   or state them.

## Mastery checkpoint

Without notes: **(a)** Write the normal equations of the coupled linear problem
and identify the block that the coupling adds. **(b)** From the sweep, state the
optimal $\lambda_p$, the error reduction achieved, and the misfit cost.
**(c)** Explain, with the deviation rms, why the error plateaus at $0.0918$ rather
than going to zero. **(d)** You are given a relation calibrated on 12 cores from
another basin. State the two diagnostics you would run before using it, and what
each would show.

## Common pitfalls

1. **Reporting the coupled model as "constrained by rock physics"** without
   saying whose rock physics, from where, and with what residual.
2. **Increasing $\lambda_p$ until the picture looks geological.** That is
   choosing the answer.
3. **Estimating the relation inside the inversion and then quoting it as
   evidence.** Circular.
4. **Forgetting the amplitude units.** The same $\lambda_p$ is a different
   statement for different units.
5. **Ignoring the property that was NOT coupled.** Its misfit may be at the noise
   floor while the coupled one has been pushed far above it.

## Related modules

- [Why Joint Inversion: Complementary Sensitivities](01-joint-inversion-concepts.md).
- [Structural (Cross-Gradient) Coupling](02-structural-joint-inversion.md).
- [Pitfalls: Inconsistent Physics, Weighting, Over-Coupling](05-joint-inversion-pitfalls.md).
- [05 Core Geophysics](../../05-core-geophysics/README.md) — where rock-physics
  relations come from and how uncertain they are.
- [08 Practical Inversion Workflow](../08-practical-inversion-workflow/README.md).

Code: [`code/petrophysical_coupling_demo.py`](code/petrophysical_coupling_demo.py).
Exercises: [`exercises/03-petrophysical-joint-inversion-exercises.md`](exercises/03-petrophysical-joint-inversion-exercises.md).
