---
id: 18-07-05
title: "Pitfalls: Inconsistent Physics, Weighting, Over-Coupling"
level: research
prereqs: ["18-07-01", "18-07-02", "18-07-03", "18-07-04"]
tags: [inverse-problems, joint-inversion, weighting, consistency, diagnostics]
---

# Pitfalls: Inconsistent Physics, Weighting, Over-Coupling

> All models and data in this module are **SYNTHETIC**. The truth models, the
> assumed reference model and every weight below are chosen teaching
> ingredients; no number below is a measurement of the Earth.

## Learning objectives

By the end of this lesson you will be able to:

1. **Sweep** a relative data weight and **state** where the joint solution
   collapses onto a single-data-set solution, using a distance to the
   single-data-set models as the measure.
2. **Compute** the per-datum chi of every data set at the joint solution and
   **interpret** a chi far above 1 as inconsistent physics rather than a solver
   failure.
3. **Detect** inconsistency by comparing separate inversions: two models that fit
   their own data and disagree are evidence about the physics, not about either
   inversion.
4. **Distinguish** over-coupling from numerical instability and **quantify** it
   by the divergence of the chi as the coupling weight grows.
5. **Design** a diagnostic set — chi table, weight sweep, separate inversions —
   that would catch each of the three pitfalls before publication.
6. **State** the reporting requirements that make a joint inversion auditable:
   weights, chi values, and the assumption that links the data sets.

## Prerequisites

- [18-07-01 Why Joint Inversion: Complementary Sensitivities](01-joint-inversion-concepts.md).
- [18-07-02 Structural (Cross-Gradient) Coupling](02-structural-joint-inversion.md).
- [18-07-03 Petrophysically Coupled Joint Inversion](03-petrophysical-joint-inversion.md).
- [18-07-04 Sequential vs Simultaneous Inversion](04-sequential-vs-simultaneous.md).

## 1. Pitfall 1 — relative weighting

The joint objective with weights $w_1, w_2$,

$$\Phi = w_1\|G_1\mathbf{m}-\mathbf{d}_1\|^2 + w_2\|G_2\mathbf{m}-\mathbf{d}_2\|^2
+ \lambda_s\|\nabla\mathbf{m}\|^2,$$

looks harmless: surely the weights are $1/\sigma_i^2$ and the matter is settled.
They are — if the noise is known. When it is not (and it usually is assumed
rather than measured), the weight is a *claim*, and the demo measures what the
claim does.

Two data sets: $G_1$ with 8 broad kernels, $G_2$ with 16 localised kernels,
$\sigma = 0.05$ for both, truth a unit sine on 20 cells. Single-data-set
solutions: error 0.0553 ($G_1$ only) and 0.0415 ($G_2$ only); the $G_1$-only
model fits $G_2$ at chi = 2.06 per datum and the $G_2$-only model fits $G_1$ at
chi = 1.70. With $w_2 = 1$:

| $w_1$ | chi 1 | chi 2 | error | dist to $G_1$-only | dist to $G_2$-only |
|---|---|---|---|---|---|
| $10^{-3}$ | 1.70 | 0.39 | 0.0415 | 0.0582 | **0.0001** |
| $10^{-2}$ | 1.65 | 0.39 | 0.0410 | 0.0578 | 0.0012 |
| $10^{-1}$ | 1.38 | 0.41 | 0.0385 | 0.0559 | 0.0085 |
| $1$ | 1.03 | 0.53 | **0.0371** | 0.0575 | 0.0232 |
| $10$ | 0.87 | 0.80 | 0.0479 | 0.0699 | 0.0443 |
| $100$ | 0.83 | 1.34 | 0.0497 | 0.0509 | 0.0348 |
| $1000$ | 0.79 | 4.05 | 0.1608 | 0.1348 | 0.1348 |

At $w_1 = 10^{-3}$ the "joint" model is the $G_2$-only model to four decimals —
data set 1 has been discarded. At $w_1 = 10^3$ the roles reverse. In between,
both chi values are near 1 and the model error is smallest (0.0371 at $w_1=1$).
**The weight is a claim about the data errors, and a sweep is how you find out
whether the claim matters.** A joint inversion published without the weights and
without the chi table is not reproducible.

## 2. Pitfall 2 — inconsistent physics

Now generate data set 1 from the sine and data set 2 from a phase-shifted sine
(0.9 rad). Two different Earths, by construction — a situation that arises in
practice from a wrong datum, a mis-tied refraction static, or a physical
assumption that does not hold in that geology.

| quantity | separate inversions | joint inversion |
|---|---|---|
| chi data 1 | 0.82 | 7.24 |
| chi data 2 | 0.48 | 5.87 |

The two separate models differ by 0.2420 rms, which is **4.4 times** the error of
the better one. The joint inversion cannot make both chi equal 1: the
inconsistency is in the physics, not in the noise.

The lesson is about interpretation, not arithmetic. A joint inversion with
residuals left unexplained is not a failure of the solver; **it is a measurement
of a real inconsistency that must be reported**. The wrong responses are (i) to
increase $w_1$ until chi 1 looks acceptable, which simply discards the other data
set, and (ii) to add free parameters until both fit, which converts the
inconsistency into structure.

## 3. Pitfall 3 — over-coupling

Over-coupling means a coupling weight that makes the model express the
assumption rather than the data. It is not the same as numerical instability, and
it is normally reached without any warning from the optimiser. Coupling the model
to an assumed reference $\mathbf{m}_{\text{ref}}$ with weight $\mu$,

$$\Phi = w_1\|G_1\mathbf{m}-\mathbf{d}_1\|^2 + w_2\|G_2\mathbf{m}-\mathbf{d}_2\|^2
+ \lambda_s\|\nabla\mathbf{m}\|^2 + \mu\|\mathbf{m}-\mathbf{m}_{\text{ref}}\|^2,$$

with $\mathbf{m}_{\text{ref}} = \mathbf{m}_{\text{true}} + 0.25$:

| $\mu$ | error | distance to reference | chi 1 | chi 2 |
|---|---|---|---|---|
| 0 | 0.0371 | 0.2513 | 1.03 | 0.53 |
| 0.1 | 0.0321 | 0.2493 | 1.01 | 0.58 |
| 1 | 0.0281 | 0.2406 | 1.46 | 0.93 |
| 10 | 0.0670 | 0.1938 | 8.92 | 3.50 |
| 100 | 0.1841 | 0.0682 | 30.96 | 11.00 |
| 1000 | 0.2411 | 0.0091 | 41.45 | 14.58 |

Two honest observations.

- A small pull ($\mu = 0.1$–$1$) *lowers* the model error, because a wrong
  reference still acts as shrinkage towards the prior mean. The chi values rise
  while the error falls: a lower error against a synthetic truth is not a licence
  to believe the model, and on real data no such check is available.
- As $\mu$ grows the model converges onto the reference and its error converges
  to the reference's systematic error (0.25), while both chi values grow without
  bound — 41.45 and 14.58 against a target of 1.

Every chi above 1 is a gate. A coupling that pushes chi far above 1 has stopped
inverting and started asserting.

## 4. The diagnostic set

Before any joint inversion is reported, compute and print:

1. **The chi table.** Per-datum chi for every data set at the joint solution,
   against noise levels stated in advance.
2. **The weight sweep.** Model error or misfit versus $w_1/w_2$ over at least
   four orders of magnitude, with the distances to the single-data-set solutions
   so that collapse is visible.
3. **The separate inversions.** Two models that fit their own data and disagree
   are evidence about the physics; report the disagreement as a number.
4. **The weight used, and its provenance.** Measured noise, assumed noise, or
   chosen by a discrepancy criterion — the reader must be able to tell.

None of these four is expensive. All four are absent from many published joint
inversions, which is why the pitfalls above keep being rediscovered.

## 5. Numeric demonstration

```bash
cd 18-inverse-problems/07-joint-and-multi-physics-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python joint_inversion_pitfalls_demo.py
```

Three sections, one per pitfall, each printing the tables above. Print-only,
seeded, exits 0.

## 6. Assumptions and regime of validity

1. **Linear, shared-model examples.** The pitfalls are illustrated on the
   simplest case; in nonlinear problems the same three failures appear, with a
   local-minimum flavour added.
2. **Synthetic truth available.** The demonstration can compute model error
   because the truth is known. On real data, chi and the weight sweep are the
   available diagnostics — which is precisely why they must be reported.
3. **Chi requires a stated noise level.** Without it, chi is uninterpretable, and
   choosing the noise after seeing the residual makes the test unfalsifiable.
4. **The reference model is wrong by construction.** Real references are wrong by
   unknown amounts; the demonstration's 0.25 is a magnitude, not a prediction.

## Mastery checkpoint

Without notes: **(a)** From the weight table, state the $w_1$ at which the joint
model is indistinguishable from a single-data-set model, and the distance that
demonstrates it. **(b)** Explain why chi = 7.24 with $\sigma$ stated in advance is
information about the Earth rather than a solver bug. **(c)** Explain why the
model error can fall while the chi values rise in the over-coupling table, and
why that pattern is dangerous on real data. **(d)** List the four diagnostics and
state, for each, the pitfall it would catch.

## Common pitfalls

1. **Reporting the joint model without the weights.** Non-reproducible by
   construction.
2. **Treating a high chi as a numerical problem.** It is usually an assumption
   problem.
3. **Excluding the inconvenient data set quietly.** The distance-to-single-model
   column is how a reader catches it.
4. **Reading the loss of a synthetic error as evidence for the model.** Only the
   chi is available on real data.
5. **Choosing the noise level last.** That destroys the only diagnostic you have.

## Related modules

- [Why Joint Inversion: Complementary Sensitivities](01-joint-inversion-concepts.md).
- [Structural (Cross-Gradient) Coupling](02-structural-joint-inversion.md).
- [Petrophysically Coupled Joint Inversion](03-petrophysical-joint-inversion.md).
- [Assessing a Model: Resolution, Artifacts, Alternatives](../08-practical-inversion-workflow/03-model-assessment.md) —
  the assessment discipline this lesson applies to multi-physics results.

Code: [`code/joint_inversion_pitfalls_demo.py`](code/joint_inversion_pitfalls_demo.py).
Exercises: [`exercises/05-joint-inversion-pitfalls-exercises.md`](exercises/05-joint-inversion-pitfalls-exercises.md).
