---
id: 18-08-04
title: "Reporting Inversion Results Responsibly"
level: doctoral
prereqs: ["18-08-03", "18-06-05"]
tags: [inverse-problems, workflow, reporting, uncertainty, reproducibility]
---

# Reporting Inversion Results Responsibly

> All models and data in this module are **SYNTHETIC**. The weights, noise level
> and truths below are chosen teaching ingredients; no number is a measurement of
> the Earth.

## Learning objectives

By the end of this lesson you will be able to:

1. **Demonstrate** that the minimum-misfit model is not the model with the
   smallest error, and **state** why the misfit is an incomplete objective.
2. **Apply** the discrepancy principle to choose a regularisation weight from a
   stated noise level, and **state** what the choice buys and what it assumes.
3. **Report** a model with the per-position admitted range, the resolution
   length and the effective parameter count.
4. **Identify** the three sentences that must not appear in an inversion report,
   and **rewrite** each into a supported form.
5. **Assemble** a report template whose every number is either measured with its
   uncertainty or explicitly labelled as a choice.
6. **State** the reproducibility requirements — weights, noise levels, code,
   seeds — that make an inversion auditable.

## Prerequisites

- [18-08-03 Assessing a Model: Resolution, Artifacts, Alternatives](03-model-assessment.md) —
  the assessment that a report must contain.
- [18-06-05 Visualising and Communicating Uncertainty](../06-uncertainty-quantification/05-uncertainty-visualisation.md) —
  how uncertainty is shown without hiding it.
- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](../03-regularization/03-parameter-choice.md) —
  the parameter-choice methods used here.

## 1. The minimum misfit is not the best model

`code/reporting_inversion_demo.py` inverts 15 observations ($\sigma=0.25$) for a
40-cell model and sweeps the smoothness weight.

| $\lambda$ | chi per datum | model error | $\operatorname{tr}R$ |
|---|---|---|---|
| $10^{-3}$ | 0.618 | 2.3229 | 11.17 |
| $10^{-2}$ | 0.681 | 0.7737 | 10.00 |
| $0.1$ | 0.738 | 0.2729 | 8.72 |
| $1$ | 0.775 | 0.1619 | 7.30 |
| $3$ | 0.793 | 0.1446 | 6.57 |
| $10$ | 0.844 | 0.1277 | 5.73 |
| **$30$** | **0.939** | **0.1228** | **4.94** |
| $100$ | 1.085 | 0.1352 | 4.05 |
| $300$ | 1.253 | 0.1523 | 3.26 |

The smallest model error (0.1228) is at $\lambda = 30$, not at the smallest
$\lambda$ (chi 0.618, error 2.3229). Chasing the smallest misfit fits noise and
moves the model away from the truth. **The misfit is the wrong objective on its
own**; the regularisation is what makes it a model-selection problem.

## 2. Choosing the weight from the stated noise

The discrepancy principle asks for the model whose misfit is no better than the
noise requires: choose the $\lambda$ at which chi per datum is closest to 1. On
this grid the closest is $\lambda = 30$ (chi = 0.939), giving model error 0.1228
and $\operatorname{tr}R = 4.94$.

On this grid the discrepancy choice coincides with the best-error choice, which
is **luck, not a guarantee**: the two are computed from different information.
What matters is that the discrepancy choice uses only the stated noise level, so
it is available on real data, where the truth is not. It also fixes the degrees
of freedom: at $\lambda=30$ the model carries fewer than five effective
parameters, so a $2\times2$ grid search over $\lambda$ is enough.

## 3. The admitted range is part of the model

| $z$ (km) | model value | 95% admitted range | width/claim |
|---|---|---|---|
| 4.25 | 0.3382 | 0.1592 – 0.5173 | 1.06 |
| 6.25 | 0.3884 | 0.2094 – 0.5674 | 0.92 |
| 8.25 | 0.2703 | 0.0869 – 0.4537 | 1.36 |
| 12.25 | 0.2241 | 0.0448 – 0.4034 | 1.60 |
| 16.25 | 0.2403 | 0.0606 – 0.4200 | 1.50 |

The last column is the honest score of a claim: an admitted width larger than the
claimed value means the claim is not supported by the data at that depth,
whatever the inversion produced there. At 12.25 km the range is 1.6 times the
model value, so the statement "the model is 0.22 at 12.25 km" is not a
measurement; "the data admit 0.04 to 0.40" is.

## 4. The report template

```
data            : 15 observations, sigma = 0.25 (stated before inversion)
misfit          : chi per datum = 0.94
weight          : lambda = 3.0e+01, chosen by the discrepancy principle
complexity      : trace(R) = 4.94 effective parameters out of 40
resolution      : 0 of 40 cells with diag(R) > 0.5; PSF half-width 4.00 km
admitted range  : per-depth 95% interval reported with the model
worst depth     : z = 19.75 km, widest 95% range 0.5468
null space      : 40 of 40 cells fail the diag(R) > 0.5 test
```

Every line is a number or a task. Nothing in the template requires the truth, and
nothing in it can be omitted without making the model unauditable.

## 5. The three sentences that must not be written

| unsupported | why | supported rewrite |
|---|---|---|
| "the inversion resolved the target at 6 km" | resolution is a length, not an achievement; here 0 of 40 cells pass $\operatorname{diag}R>0.5$ and the PSF half-width is 4.00 km | "the target is imaged with a resolution length of 4.00 km; structure finer than that is not resolved" |
| "the model is accurate to 0.01" | accuracy requires the noise level, the misfit and the admitted range together | "the model is 0.39 at 6.25 km with a 95% admitted range of 0.21–0.57, at chi per datum 0.94" |
| "additional layers improve the fit" | the fit is not the objective; section 1 shows the smallest misfit has the largest error | "the weight was chosen by the discrepancy principle; adding parameters beyond $\operatorname{tr}R\approx5$ does not change the model within its admitted range" |

## 6. Numeric demonstration

```bash
cd 18-inverse-problems/08-practical-inversion-workflow/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reporting_inversion_demo.py
```

Five sections: the weight sweep; the discrepancy-principle choice; the admitted
range; the filled report template; the three sentences. Print-only, seeded,
exits 0 in under a second.

## 7. Assumptions and regime of validity

1. **The noise level is honest and stated first.** Everything in the report is
   scaled by it; a chosen-after-the-fact noise makes chi unfalsifiable.
2. **The posterior is the production one.** An admitted range computed with a
   different weight is a different claim.
3. **Gaussian, linear approximation.** The range is a Gaussian interval; for
   skewed posteriors report quantiles from sampling instead.
4. **The report is for a reader who will not see the code.** Every number must
   carry its unit, its provenance and its uncertainty.
5. **Responsibility is not a formatting convention.** A report can satisfy the
   template and still mislead; the template removes the most common omissions,
   not the need for judgement.

## Mastery checkpoint

Without notes: **(a)** From the sweep, state the smallest and largest model
errors and the corresponding chi values, and draw the conclusion about the
misfit. **(b)** Choose $\lambda$ by the discrepancy principle and state the two
assumptions it needs. **(c)** Rewrite "the model resolves a 0.5-km layer at
12.25 km" using the admitted range. **(d)** List the eight lines of the report
template.

## Common pitfalls

1. **Reporting a minimum of the misfit as an achievement.** Section 1.
2. **Quoting a model value with no admitted range.** The range is the measurement.
3. **Tuning the weight with the synthetic truth and reporting it as a criterion.**
   The discrepancy principle exists to avoid this.
4. **Omitting the noise level or the weight.** Nothing in the report can then be
   checked.
5. **Letting a figure stand in for the numbers.** A colour map cannot carry a
   chi value, a resolution length or an admitted range.

## Related modules

- [Assessing a Model: Resolution, Artifacts, Alternatives](03-model-assessment.md).
- [Synthetic Testing, Checkerboards and Recovery Tests](02-synthetic-testing.md).
- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](../03-regularization/03-parameter-choice.md).
- [18-06-05 Visualising and Communicating Uncertainty](../06-uncertainty-quantification/05-uncertainty-visualisation.md).
- [24 Research Papers and Writing](../../24-research-papers-writing/README.md) — the
  publication context for these conventions.

Code: [`code/reporting_inversion_demo.py`](code/reporting_inversion_demo.py).
Exercises: [`exercises/04-reporting-inversion-exercises.md`](exercises/04-reporting-inversion-exercises.md).
