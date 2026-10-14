---
id: 18-08-03
title: "Assessing a Model: Resolution, Artifacts, Alternatives"
level: research
prereqs: ["18-08-01", "18-08-02", "18-02-05"]
tags: [inverse-problems, workflow, resolution, artifacts, uncertainty]
---

# Assessing a Model: Resolution, Artifacts, Alternatives

> All models and data in this module are **SYNTHETIC**. The kernels, noise level
> and prior below are chosen teaching ingredients; no number is a measurement of
> the Earth.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the resolution matrix and the point-spread function of a produced
   model and **state** the resolution length at a chosen depth.
2. **Run** a perturbation test to decide which features the data require, using
   the data signature and the posterior norm as the two criteria.
3. **Generate** alternative models that fit the data equally well and **report**
   the admitted range as a function of position.
4. **Recognise** the two ways an inversion image misleads: a feature the data do
   not require, and a feature the data cannot place.
5. **Produce** a five-item assessment (misfit, complexity, resolution,
   admissibility, alternatives) with numbers, and **state** what each item would
   change in an interpretation.

## Prerequisites

- [18-08-01 Setting Up a Solvable Inverse Problem](01-problem-setup.md).
- [18-08-02 Synthetic Testing, Checkerboards and Recovery Tests](02-synthetic-testing.md) —
  measuring resolution before the fact; this lesson does it after.
- [18-02-05 Resolution and Information Matrices in Interpretation](../02-linear-inverse-problems/05-resolution-matrices.md).

## 1. The produced model is not the answer

An inversion returns one member of a set. Assessment means describing the set and
the operator that produced it, at the location of interest:

- the **misfit**, as chi per datum against a stated noise level;
- the **complexity**, $\operatorname{tr}R$ effective parameters out of $n$;
- the **resolution**, the point-spread half-width at depth;
- the **admissibility** of a claimed feature, by a perturbation test;
- the **alternatives**, the range of models that fit the data equally well.

None of these is optional decoration: each one can change the interpretation.

## 2. Worked example: a model and its assessment

`code/model_assessment_demo.py` inverts 15 observations ($\sigma = 0.25$) for a
40-cell model over 20 km with smoothness weight $\lambda = 30$.

| item | value |
|---|---|
| chi per datum | 0.939 |
| error against the synthetic truth | 0.1228 |
| $\operatorname{tr}R$ | 4.94 of 40 |
| cells with $\operatorname{diag}R > 0.5$ | 0 of 40 |
| PSF at $z = 6.25$ km: peak | 0.1183 |
| PSF at $z = 6.25$ km: half-width | 4.00 km |
| PSF at $z = 6.25$ km: most negative sidelobe | $-0.0167$ |

The model fits the data at the noise level and carries about five effective
parameters. A reader given only the picture would not know either fact.

## 3. Which features do the data require?

The perturbation test adds a localised feature of amplitude 0.1 and reports two
numbers: the rms change in the forward data divided by $\sigma$ (does the *data*
notice?) and $\sqrt{\Delta\mathbf{m}^{T}C^{-1}\Delta\mathbf{m}/n}$ (is the
perturbation *admissible* under the posterior?).

| width (km) | signature ($\sigma$) | posterior norm | verdict |
|---|---|---|---|
| 0.25 | 0.109 | 0.224 | not required |
| 0.50 | 0.212 | 0.201 | not required |
| 1.00 | 0.407 | 0.274 | not required |
| 3.00 | 0.953 | 0.587 | not required |
| 8.00 | 1.501 | 0.919 | required |

Features much narrower than the PSF width move the data far less than the noise,
so the data cannot require them: whether such a feature appears in the image is
decided by the regularisation, not by the measurements. Reporting one as a
resolved layer is the commonest artifact in inversion interpretation.

## 4. Alternatives: the admitted range

Draw 2000 samples from the posterior $C$ and tabulate the 95% admitted range at
each depth (4 standard deviations for a Gaussian). The demo's samples all have
chi between 0.89 and 1.39 — they are equally acceptable explanations.

| $z$ (km) | 2.25 | 6.25 | 10.25 | 15.25 | 18.25 |
|---|---|---|---|---|---|
| 95% admitted range | 0.3402 | 0.3580 | 0.3571 | 0.3552 | 0.3622 |

The range varies with depth by a factor of 1.6, widest at the edge cell
(19.75 km, 0.5468) where no observation sits, narrowest at 2.25 km (0.3402). **The
model is not one model but a distribution**, and its width is the honest score of
any claim made from it: an admitted width larger than the claimed value means the
claim is not supported by the data at that depth.

## 5. Two ways an inversion image misleads

- **A feature the data do not require.** Section 3. The regularisation may place
  a thin layer or a weak contrast that no observation demands; the fix is the
  perturbation test, and the honest report says so.
- **A feature the data cannot place.** A body wider than the PSF but located at a
  depth where the admitted range is wide will appear in the image at whatever
  depth the prior prefers. The fix is to report the admitted range, not the
  central value alone.

Both are properties of the experiment. Neither is a bug in the code, and neither
is visible in the misfit.

## 6. Numeric demonstration

```bash
cd 18-inverse-problems/08-practical-inversion-workflow/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python model_assessment_demo.py
```

Five sections: the model and its misfit; resolution and the PSF; the perturbation
test; posterior alternatives; the five-item summary. Print-only, seeded, exits 0
in under a second.

## 7. Assumptions and regime of validity

1. **The posterior must be the one you mean.** The admitted range is computed
   from $C = (G^{T}C_d^{-1}G + P_0)^{-1}$; if another regularisation was used in
   practice, the range is wrong.
2. **Gaussian errors and a linear operator.** For nonlinear problems the
   alternatives must be sampled in nonlinear directions (MCMC), and the
   perturbation test is local.
3. **The noise level is stated, not fitted.** chi and the admitted range both
   scale with it.
4. **The perturbation test is local.** It answers "does the data require this
   change"; it does not prove that no other structure is required.
5. **Resolution is position-dependent.** A single number for the whole model
   hides the factor-of-1.6 spread measured here.

## Mastery checkpoint

Without notes: **(a)** List the five assessment items and the quantity that
represents each. **(b)** From the perturbation table, state the largest width
whose feature the data do not require, and the criterion used. **(c)** Explain
why 2000 posterior samples can all be "equally acceptable" while differing from
each other. **(d)** Given a claimed 0.3-km layer at 6.25 km and an admitted range
of 0.3580, state whether the claim is supported.

## Common pitfalls

1. **Reporting a model without its resolution.** The PSF width, not the grid
   spacing, is the resolution.
2. **Interpreting a feature thinner than the PSF.** Section 3.
3. **Quoting one number per depth.** Report the admitted range.
4. **Assuming a uniformly good model.** Resolution and admitted range vary with
   position.
5. **Treating the misfit as an assessment.** It is only one of five items.

## Related modules

- [Reporting Inversion Results Responsibly](04-reporting-inversion.md) — the
  report format these items feed.
- [Setting Up a Solvable Inverse Problem](01-problem-setup.md).
- [Synthetic Testing, Checkerboards and Recovery Tests](02-synthetic-testing.md).
- [18-06-05 Visualising and Communicating Uncertainty](../06-uncertainty-quantification/05-uncertainty-visualisation.md).

Code: [`code/model_assessment_demo.py`](code/model_assessment_demo.py).
Exercises: [`exercises/03-model-assessment-exercises.md`](exercises/03-model-assessment-exercises.md).
