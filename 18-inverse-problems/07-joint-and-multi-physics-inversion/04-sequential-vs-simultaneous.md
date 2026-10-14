---
id: 18-07-04
title: "Sequential vs Simultaneous Inversion"
level: research
prereqs: ["18-07-01", "18-05-01"]
tags: [inverse-problems, joint-inversion, sequential-updating, bayesian-updating, workflow]
---

# Sequential vs Simultaneous Inversion

> All models and data in this module are **SYNTHETIC**. The two operators, the
> noise levels and the prior are chosen teaching ingredients; no number below is
> a measurement of the Earth.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** Gaussian sequential updating and **prove** that for independent
   data errors and a shared linear model it is algebraically identical to the
   simultaneous (joint) inversion.
2. **Verify** that identity numerically and **state** the conditions under which
   the ordering of the stages has no effect.
3. **Identify** the three practical changes that make sequential workflows differ
   from the joint answer: a different parameterisation, a different
   linearisation, and a stage-1 prior that is not the stage-1 posterior.
4. **Measure** the over-confidence produced by treating a stage-1 model as more
   certain than its own posterior, and **state** the diagnostic (rms error
   divided by reported sigma).
5. **Compute** the chi-per-datum of a frozen first stage and **interpret** it as
   propagated error.
6. **Choose** between sequential and simultaneous for a stated problem, giving
   the criterion (cost, parameterisation, or uncertainty accounting).

## Prerequisites

- [18-07-01 Why Joint Inversion: Complementary Sensitivities](01-joint-inversion-concepts.md).
- [18-05-01 Bayes' Theorem as an Inverse-Problem Formulation](../05-bayesian-inversion/01-bayes-inverse-formulation.md) —
  the posterior and the way a prior is updated.
- [18-02-06 Data Weighting and Error Covariance Specification](../02-linear-inverse-problems/06-weighting-and-covariance.md).

## 1. The algebra of sequential updating

Let the prior be $\mathbf{m}\sim\mathcal{N}(\mathbf{0},P_0^{-1})$ and the two
data sets have independent Gaussian errors with precisions
$P_a = G_1^{T}C_1^{-1}G_1$ and $P_b = G_2^{T}C_2^{-1}G_2$ (the *information*
matrices). The simultaneous posterior precision is

$$P_{\text{joint}} = P_a + P_b + P_0 .$$

Now do it in two stages. Stage 1 uses data set 2 only:

$$P^{(1)} = P_b + P_0, \qquad
\mathbf{m}^{(1)} = \left(P^{(1)}\right)^{-1}G_2^{T}C_2^{-1}\mathbf{d}_2 .$$

Stage 2 adds data set 1, using the stage-1 posterior as its prior:

$$P^{(2)} = P_a + P^{(1)} = P_a + P_b + P_0 = P_{\text{joint}},$$

$$\mathbf{m}^{(2)} = \left(P^{(2)}\right)^{-1}
\left(P^{(1)}\mathbf{m}^{(1)} + G_1^{T}C_1^{-1}\mathbf{d}_1\right).$$

Since $P^{(1)}\mathbf{m}^{(1)} = G_2^{T}C_2^{-1}\mathbf{d}_2$, this is

$$\mathbf{m}^{(2)} = P_{\text{joint}}^{-1}
\left(G_1^{T}C_1^{-1}\mathbf{d}_1 + G_2^{T}C_2^{-1}\mathbf{d}_2\right)
= \mathbf{m}_{\text{joint}} .$$

**The two-stage Gaussian update is the joint update.** The proof needs only the
independence of the data errors and the fact that both stages act on the same
model. Nothing was approximated.

## 2. Verification, and where the content actually is

`code/sequential_vs_simultaneous_demo.py` realises this numerically with
$n = 20$ cells, a poorly conditioned operator $G_1$ (8 broad kernels, condition
number $3.098\times10^3$) and a well-conditioned $G_2$ (16 localised kernels,
$1.107\times10^2$), both with $\sigma = 0.05$, plus a smoothness prior. Over 300
noise realisations:

| quantity | $G_1$ only | $G_2$ only | joint |
|---|---|---|---|
| prior-averaged risk $\operatorname{tr}C/N$ | 6.0483 | 1.3060 | **0.7777** |
| realised MSE against this fixed truth | 0.2841 | 0.1434 | 0.1794 |

and

$$\max|\mathbf{m}_{\text{sequential}} - \mathbf{m}_{\text{joint}}| = 3.175\times10^{-10},$$

$$ \max|\mathbf{m}_{\text{sequential, reversed}} - \mathbf{m}_{\text{joint}}| = 4.404\times10^{-10} .$$

The residual is round-off amplified by the condition number of $G_1$; the two
orderings agree to the same precision, so ordering is irrelevant **for a linear
problem with a shared model and a correct stage-1 posterior**.

Note the two rows do not order the methods the same way. Adding data strictly
reduces the prior-averaged risk (the covariance trace falls from 6.0483 and
1.3060 to 0.7777), but the realised error at *this* fixed truth is best for
$G_2$ alone. The guarantee is a statement averaged over the prior; a specific
Earth is not a typical sample, and the weak operator adds noise where the strong
one was already adequate. Report both numbers, or you have chosen the one that
supports your conclusion.

## 3. Where sequential workflows really differ

The identity fails, and the ordering acquires content, in three situations.

**(a) Different parameterisations.** "Invert the geometry from survey 1, then
invert for properties inside the frozen geometry" is not the same problem: the
second stage has fewer unknowns and no access to the geometry's uncertainty.
The bias this introduces is measured by the chi of section 5.

**(b) Nonlinearity.** Each stage is linearised about its own starting model, so
the two stages are not two orderings of one normal-equation system. Order
matters, and a fixed-point iteration is needed.

**(c) A prior that is not the stage-1 posterior.** This is the most common and
the most damaging, and it is measurable even in a linear problem.

## 4. Over-confidence: a prior tighter than the evidence

Suppose the workflow reuses the stage-1 prior, or claims the stage-1 model is
$\alpha$ times more certain than its own posterior says:
$P^{(2)} = \alpha P^{(1)} + P_a$. Reported sigma and realised error:

| $\alpha$ | mean reported $\sigma$ | realised rms error | ratio |
|---|---|---|---|
| 1 | 0.8471 | 0.4236 | 0.50 |
| 2 | 0.6039 | 0.4220 | 0.70 |
| 4 | 0.4324 | 0.4197 | 0.97 |
| 10 | 0.2812 | 0.4134 | 1.47 |

The reported sigma falls by a factor of three while the realised error moves by
2%. The ratio rms/$\sigma$ rises from 0.50 to 1.47: the intervals stop tracking
the error. The model becomes no more accurate and much more confident — a narrow
interval around an answer the data do not support, which is the worst
combination of the two failure modes.

## 5. Error propagation: the frozen first stage leaves a signature

Use the stage-1 model ($G_2$ only) to predict data set 1 and compute chi per
datum:

$$\chi = \frac{\left\|\mathbf{d}_1 - G_1\mathbf{m}^{(1)}\right\|/\sqrt{p}}{\sigma}
= 2.346, \qquad\text{versus}\qquad 0.991 \ \text{for the joint model}.$$

A chi near 1 means the model explains the data at the stated noise level. The
frozen-stage-1 model leaves a residual 2.3 times the noise, and that residual is
the honest diagnosis of a transferred error — provided the noise level is stated
*before* the residual is seen, and not chosen after it. In a nonlinear workflow
this residual is often the only evidence that the first stage was not good
enough to be frozen.

## 6. Numeric demonstration

```bash
cd 18-inverse-problems/07-joint-and-multi-physics-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sequential_vs_simultaneous_demo.py
```

Five sections: setup and conditioning; the joint reference with both risk
measures; the sequential identity in both orders; the over-confidence table; the
frozen-stage chi. Print-only, seeded, exits 0, under a second.

## 7. Assumptions and regime of validity

1. **Linear forward models.** The identity is exact only for linear $G$ with
   Gaussian errors. Nonlinear problems inherit order dependence.
2. **Same model in both stages.** Different parameterisations break the identity
   (section 3a) and require an explicit transfer operator, which is a model.
3. **Independent data errors.** Correlated errors do not break the identity —
   the exact update still holds — but they change the size of the gain, as
   lesson 01 measured.
4. **A correct stage-1 posterior.** If the first stage used an ad-hoc
   regularisation and the second stage treats its output as a posterior, the
   uncertainty is mis-stated.
5. **Cost is not the whole story.** For linear problems the two approaches solve
   the same system, so sequential offers no saving; savings appear for nonlinear
   problems and for very large stages solved by iterative methods.

## Mastery checkpoint

Without notes: **(a)** Derive $\mathbf{m}^{(2)} = \mathbf{m}_{\text{joint}}$ from
the two-stage update. **(b)** State the three situations in which the identity
fails. **(c)** Given $\alpha = 4$, compute the shortfall of the reported interval
against the realised error and state the calibration failure in one sentence.
**(d)** A colleague inverts resistivity inside a seismic depth model and reports
chi = 3 for the resistivity data. State what has gone wrong and what to do.

## Common pitfalls

1. **Believing sequential is an approximation.** For linear Gaussian problems it
   is an identity; the danger is in what the workflow does to the prior.
2. **Freezing a stage-1 model and not re-checking its data.** Chi is the alarm.
3. **Reusing a stage-1 prior in stage 2.** That is $\alpha > 1$, and it is
   over-confidence by construction.
4. **Reporting the risk measure that flatters the method.** Report both the
   prior-averaged risk and the realised error at a synthetic truth.
5. **Assuming order-independence in nonlinear problems.** It does not hold.

## Related modules

- [Why Joint Inversion: Complementary Sensitivities](01-joint-inversion-concepts.md).
- [Pitfalls: Inconsistent Physics, Weighting, Over-Coupling](05-joint-inversion-pitfalls.md).
- [05 Bayesian Inversion and Inference](../05-bayesian-inversion/README.md) — the
  full Bayesian treatment of the updating used here.
- [06 Uncertainty Quantification](../06-uncertainty-quantification/README.md).

Code: [`code/sequential_vs_simultaneous_demo.py`](code/sequential_vs_simultaneous_demo.py).
Exercises: [`exercises/04-sequential-vs-simultaneous-exercises.md`](exercises/04-sequential-vs-simultaneous-exercises.md).
