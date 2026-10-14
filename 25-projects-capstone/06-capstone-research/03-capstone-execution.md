---
id: 25-06-03
title: "Capstone: Data, Modelling and Uncertainty Analysis"
level: research
prereqs: ["25-06-02", "18-06-01", "21-01-03", "22-02-05"]
estimated_minutes: 260
tags: [capstone, uncertainty-quantification, verification, reproducibility, research]
---

# Capstone: Data, Modelling and Uncertainty Analysis

## Learning objectives

By the end of this lesson you will be able to:

1. **Verify** an estimator against a known answer before using it on data, and
   **check** the calibration of the interval you intend to quote.
2. **Decompose** the uncertainty of a headline number into statistical and systematic
   parts, and **attribute** it to individual inputs with first-order sensitivity
   indices.
3. **Decide**, from the budget, where additional effort would and would not pay.
4. **Keep** a data-and-code provenance log that lets someone else re-run the analysis
   from the query to the figure.
5. **Freeze** the analysis before interpretation, and **record** what changed
   afterwards.
6. **Present** a result with its verification, its uncertainty budget and its
   sensitivity — the three things a capstone's uncertainty section must contain.
7. **Recognise** the failure mode of a statistical error bar on an
   assumption-dominated number.

## Prerequisites

- [25-06-02 Capstone: Proposal, Literature Review and Methods Plan](./02-capstone-proposal.md) —
  the plan this lesson executes, including the validation step.
- [18-06-01 The Taxonomy of Uncertainty](../../18-inverse-problems/06-uncertainty-quantification/01-uncertainty-taxonomy.md) —
  the statistical/systematic distinction used throughout.
- [21-01-03 Resampling and the Bootstrap](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  the empirical route to an uncertainty.
- [22-02-05 Data Versioning](../../22-data-engineering-reproducibility/02-reproducible-workflows/05-data-versioning.md) —
  how the provenance log is made checkable.

## 1. The question

*What is the headline number, how uncertain is it, and which part of that uncertainty
could more work reduce?*

The demonstration takes a capstone-scale headline — a Moho depth inverted from a
measured Ps delay time with an assumed $V_p$, $V_p/V_s$ and ray parameter — and
produces the three products the execution phase owes the write-up:

| product | value |
|---|---|
| headline | $H = 35.04 \pm 2.00$ km (95%: $\pm 3.92$ km) |
| statistical part ($t$ only) | $1.198$ km |
| systematic part ($V_p$, $k$, $p$) | $1.600$ km — **64% of the variance** |
| dominant input | $V_p/V_s$, $S = 0.474$ (systematic) |
| interval calibration | statistical interval covers the truth in 95.1% of replicates |
| value of halving the picking error | total sd falls from 2.001 to 1.709 km (**15%**) |
| systematic floor | 1.600 km = 80% of today's sd |

The verdict is the lesson: **the number is dominated by an assumption, so quoting a
statistical error bar on it would be misleading, and the only way to improve the
result is to measure the assumption.** Halving the measurement noise — the expensive
thing — buys 15%.

## 2. Verification comes first

The plan of [25-06-02](./02-capstone-proposal.md) puts a synthetic validation before
the production run, and this is why: the verification of a *pipeline and an estimator*
is cheap and decisive, while the verification of a *result* is impossible.

Three verifications, in increasing order of strength:

1. **Analytic check.** Substitute the generating parameters back into the estimator
   and confirm it returns the generating value: the demo's inversion returns
   $H = 35.00$ km from the exact $t$, so the algebra and the units are right.
2. **Recovery check (calibration).** Generate many synthetic measurements from known
   parameters and check that (a) the estimator's mean equals the truth and (b) the
   interval it quotes covers the truth at its nominal rate. The demo's statistical-only
   95% interval covers the truth in **95.1%** of 4000 replicates: the interval means
   what it says.
3. **End-to-end check.** Run the *whole* pipeline — query, processing, estimation,
   figure — on a synthetic dataset with a known answer, and require the final figure to
   show that answer. This is the only verification that covers the joins between steps,
   and it is the one that catches the unit change in the processing script.

A quoted interval that has never been checked for coverage is a number, not an
uncertainty. Note also what the demo's third line says: an interval built from the
*whole* budget contains the truth in 95.0% of draws **only because the systematic terms
were drawn from unbiased distributions**. That is the assumption in the error bar, and
the write-up must state it.

## 3. The uncertainty budget

Variance decomposes. With $H = f(t, V_p, k, p)$ and independent input uncertainties,
the first-order sensitivity index of input $i$ is

$$S_i = \frac{\operatorname{Var}_{x_i}\bigl(\mathbb E[H \mid x_i]\bigr)}{\operatorname{Var}(H)},
\qquad \sum_i S_i \le 1,$$

estimated from the same Monte Carlo sample by binning the samples in $x_i$ and taking
the variance of the bin means (a "given-data" estimator that needs no extra model
runs). The demonstration's budget:

| input | type | $S_i$ | contribution to sd (km) |
|---|---|---|---|
| $V_p/V_s$ | systematic | $0.474$ | $1.378$ |
| $t$ (Ps delay) | statistical | $0.356$ | $1.193$ |
| $V_p$ | systematic | $0.143$ | $0.756$ |
| $p$ (ray parameter) | systematic | $0.018$ | $0.271$ |

The indices sum to $0.991$; the remaining $0.9\%$ is interaction between inputs, which
the first-order indices do not capture. **The dominant input is the assumed $V_p/V_s$,
not the measurement** — a systematic term, and one that a different instrument cannot
improve.

**Two arithmetic habits make the budget usable.**

1. **Report contributions as standard deviations, not variances.** "$27\%$ of the
   variance" invites the error of adding contributions; the add-in-quadrature
   convention is immediate if the contributions are quoted in km and squared before
   summing. The demo checks the quadrature sum: $1.998$ km against the sampled
   $2.001$ km — the model is nearly linear here, which is what makes the quadrature
   approximation valid and is itself worth stating.
2. **Separate statistical from systematic *before* quoting a single error bar.** The
   two behave differently: statistical uncertainty falls with more data ($1/\sqrt N$),
   systematic uncertainty does not. The demo makes the consequence concrete:
   halving the picking error reduces the total sd from $2.001$ to $1.709$ km
   ($15\%$), and quartering it only to $1.628$ km ($19\%$), because the systematic
   floor is $1.600$ km. **The statistical term is $36\%$ of the variance and the
   measurement is the only term that can be reduced by measurement effort.**

## 4. What to do when the assumption dominates

Four legitimate responses, in order of cost:

1. **Measure the assumption**, or find someone who has. $V_p/V_s$ is obtainable from
   the same data with a joint inversion, from a nearby borehole, or from a published
   value with a stated uncertainty — the last being the cheapest and the least
   satisfying, and it must then be cited with its own provenance.
2. **Report the result relative to the assumption.** "For $V_p/V_s$ between 1.70 and
   1.80, $H$ lies between 33.7 and 36.4 km" is an honest result even when the
   assumption cannot be improved, and it is more useful than a single number with a
   statistical error bar that hides the dependence.
3. **Propagate it as a prior rather than a number.** A Bayesian formulation with a
   distribution on $V_p/V_s$ returns a posterior that contains the systematic spread
   (this is the point of [25-05-04](../05-doctoral-projects/04-bayesian-inversion-project.md)).
4. **State it as a limitation with a magnitude.** "The result is dominated by the
   assumed $V_p/V_s$; a $0.03$ error in the ratio moves $H$ by $1.4$ km, larger than
   the statistical uncertainty of the measurement."

What is *not* legitimate is quoting $35.04 \pm 1.20$ km — the statistical-only error —
as the result's uncertainty. That number is the uncertainty of a quantity that does not
exist (the depth for the true, unknown $V_p/V_s$), and it is the most common error in
published geophysics.

## 5. Provenance: the log that makes the analysis checkable

The execution phase produces files; the provenance log makes them re-derivable. Minimum
contents, all of them written *as the work happens*:

1. **Data**: the exact query (service, parameters, date), the filter thresholds, the
   resulting record count, and the file hashes or version tags. A count that changes on
   re-query is a finding, not a nuisance.
2. **Environment**: the interpreter version and the package versions (a lock file),
   with the command that was run.
3. **Steps**: every script in the order it was run, with its inputs and outputs — the
   workflow manager of [22-02-03](../../22-data-engineering-reproducibility/02-reproducible-workflows/03-workflow-managers.md)
   does this automatically and is the reason to use one.
4. **Decisions**: every parameter choice not determined by the data (a filter width, a
   damping, a threshold) with the value used and the range tested, since §3 shows the
   headline depends on them.
5. **Freeze point**: the commit and data version at which the analysis was frozen,
   after which changes are recorded as deltas rather than made silently.

The freeze point is the discipline that separates an analysis from a search. Once the
headline number has been seen, every subsequent change to the pipeline is a change made
with knowledge of the answer, and the only defence is to record it, re-run everything
downstream, and report the number before and after.

## 6. Failure modes

1. **No verification step**, so an algebra or unit error survives to the write-up.
2. **A statistical error bar on an assumption-dominated quantity** — the demo's
   $1.198$ km instead of $2.001$ km.
3. **Adding contributions instead of adding them in quadrature**, which overstates the
   budget by up to a factor of two when many terms are comparable.
4. **Reporting variance percentages**, which cannot be combined.
5. **Optimising the cheap term.** Halving the picking error buys $15\%$; measuring
   $V_p/V_s$ would remove $47\%$ of the variance.
6. **A provenance log written at the end.** It will be incomplete in exactly the places
   that matter, because those are the places where something went wrong.
7. **Moving the freeze point** — changing the processing after seeing the result and
   reporting only the final number.

## 7. Rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Verification before production | 25% | analytic check, recovery/coverage check, end-to-end synthetic run |
| Uncertainty budget | 25% | statistical/systematic split, $S_i$ per input, quadrature check |
| Effort-value analysis | 15% | the effect of improving the reducible terms, with the systematic floor |
| Presentation of the result | 15% | assumption-dependence reported, not hidden behind a statistical error bar |
| Provenance log | 20% | query, versions, steps, decisions, freeze point |

## 8. The honest summary

The product of the execution phase is a number, an interval, and the decomposition of
that interval. Here: $H = 35.04 \pm 2.00$ km, of which the statistical part is
$1.198$ km and the systematic part $1.600$ km ($64\%$ of the variance), dominated by
the assumed $V_p/V_s$ ($S = 0.474$) rather than by the measurement ($S = 0.356$);
halving the picking error buys $15\%$, and the systematic floor is $80\%$ of today's
standard deviation. The transferable results are that a verified estimator is worth
more than a large dataset, that an uncertainty budget is what converts an error bar
into a plan for the next study, and that the honest form of an
assumption-dominated result is a dependence on the assumption rather than a single
number with a statistical error.

## Python demonstration

[`code/capstone_execution_demo.py`](./code/capstone_execution_demo.py) prints every
number above: the headline and its inputs, the statistical/systematic split, the
first-order sensitivity indices, the coverage verification, and the value of improved
measurement precision.

```bash
cd 25-projects-capstone/06-capstone-research/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python capstone_execution_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, no network, no files, no
plots, exits 0, runs in about $0.2$ s.

## Exercises

Graded problems and worked solutions are in
[`exercises/03-capstone-execution-exercises.md`](./exercises/03-capstone-execution-exercises.md)
and
[`exercises/03-capstone-execution-solutions.md`](./exercises/03-capstone-execution-solutions.md).
The ★★★ item asks you to redesign the study so that the dominant term becomes the
statistical one, with the sample sizes and costs of doing so.

## Mastery checkpoint

Without notes:

1. State the three verifications, and what each can and cannot catch.
2. Write the first-order sensitivity index and explain why $\sum_i S_i \le 1$.
3. Given two inputs contributing $1.0$ km and $2.0$ km, compute the combined sd and
   say why it is not $3.0$.
4. Explain why a statistical error bar on an assumption-dominated quantity is
   misleading, using the demo's split.
5. List the five contents of a provenance log.

## Common pitfalls

1. Verifying after the production run.
2. Reporting $\pm$ one number, mixing statistical and systematic terms.
3. Quoting the statistical-only interval as the result's uncertainty.
4. Spending effort on the reducible term when the irreducible one dominates.
5. Treating the freeze point as a formality.

## Where this is used

The uncertainty section of the [write-up](./04-capstone-writeup.md) is built from these
three products, and the [defence](./05-capstone-defence.md) will ask which term
dominates and what was done about it. The budget logic is the same as that used in
[25-05-03](../05-doctoral-projects/03-geodynamic-model-data.md) for model error versus
noise and in [21-01-03](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md)
for resampled uncertainty; what is new here is the connection from the budget to the
*decision* about where the next unit of effort goes.

## Related lessons

- [18-06-03 Global Sensitivity Analysis](../../18-inverse-problems/06-uncertainty-quantification/03-sensitivity-analysis.md) —
  the formal treatment of the indices used here.
- [22-02-03 Workflow Managers](../../22-data-engineering-reproducibility/02-reproducible-workflows/03-workflow-managers.md) —
  the tool that keeps the provenance log automatically.
- [25-06-02 Capstone: Proposal, Literature Review and Methods Plan](./02-capstone-proposal.md) —
  the plan, including the validation step executed here.
- [25-06-04 Capstone: Manuscript-Style Write-Up and Code Release](./04-capstone-writeup.md) —
  reporting these numbers.

## Self-assessment checklist

- [ ] I can verify an estimator against a known answer before using it.
- [ ] I can check the coverage of the interval I quote.
- [ ] I can decompose an uncertainty into statistical and systematic parts.
- [ ] I can attribute the variance to individual inputs.
- [ ] I can state what additional effort would buy.
- [ ] I can produce a provenance log that lets someone else re-run me.
