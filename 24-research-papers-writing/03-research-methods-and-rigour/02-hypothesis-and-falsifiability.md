---
id: 24-03-02
title: "Hypotheses, Falsifiability and Testing in Earth Science"
level: doctoral
prereqs: ["24-03-01", "02-01-02"]
estimated_minutes: 60
tags: [research, hypotheses, falsifiability, p-values, multiplicity, testing]
---

# Hypotheses, Falsifiability and Testing in Earth Science

A hypothesis is falsifiable when it forbids something: when there is an
observation that would count against it. Earth science makes this harder than
laboratory science in specific ways — the system cannot be reset, the record is
finite, and the number of defensible processing decisions is large. This lesson
quantifies the consequence of the last of those, because it is the one under the
researcher's control.

The organising idea is that **flexibility substitutes for falsifiability**. A
hypothesis that can be tested in many defensible ways is, in practice, a
hypothesis that will be confirmed: each choice is defensible on its own, and
together they act like repeated draws until something crosses the threshold. The
demonstration measures how quickly that happens under the null.

> **Data provenance.** All numbers are **SYNTHETIC**. Experiments are simulated
> from the normal model with chosen sample sizes and effect sizes, and the
> flexibility calculation uses independent uniform draws, which is the definition
> of a null $p$-value. No real dataset is analysed.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the null and alternative hypotheses for a geophysical comparison and
   **identify** what an observation would have to be to falsify the alternative.
2. **Measure** the false-positive rate of a calibrated test and **state** why the
   calibration is the baseline for everything else.
3. **Compute** power as a function of effect size at a fixed sample size, and
   **explain** why sample size chooses the question that can be answered.
4. **Quantify** the effect of researcher degrees of freedom under the null, and
   **explain** why the individual choices remain defensible.
5. **Compute** the family-wise error rate for a set of tests and **state** what a
   correction costs.
6. **Write** a pre-analysis plan that removes the flexibility in advance.

## Prerequisites

- [24-03-01 Formulating Answerable Research Questions](01-research-questions.md) —
  the question a hypothesis specialises.
- [02-01-02 Measurement Uncertainty](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md) —
  what an error bar asserts.

## 1. Hypotheses that forbid something

Write the pair explicitly:

- $H_0$: the shear-wave velocity in the northern block equals that in the southern
  block within measurement uncertainty.
- $H_1$: it does not, and the difference exceeds the measurement uncertainty.

Then write the **prediction** and the **falsifier**:

> If $H_1$ holds, the difference persists when the inversion is repeated with a
> different starting model and a different station subset. A difference that
> vanishes under either change would falsify $H_1$ as stated.

The falsifier is a sentence, not a statistic, and it is what distinguishes a
hypothesis from a hope. Note that it can be written before any data exist.

## 2. Calibration: what the null produces

The demonstration runs $4000$ null experiments with $n = 32$ per group:

| Quantity | Measured | Nominal |
|---|---|---|
| $P(p < 0.05)$ | $4.67\% \pm 0.34\%$ (1 s.e.) | $5\%$ |
| $P(p < 0.01)$ | $0.92\%$ | $1\%$ |
| median $p$ | $0.509$ | $0.5$ |

The test is calibrated. Everything that follows is a departure from this baseline,
and the departure is never in the test itself — it is in what happens around it.

## 3. Power at a fixed sample size

At $n = 32$ per group:

| True effect | Power | Median $p$ | $P(p < 0.001)$ |
|---|---|---|---|
| $0.00$ | $5.2\%$ | $0.4932$ | $0.10\%$ |
| $0.20$ | $13.2\%$ | $0.3436$ | $0.68\%$ |
| $0.50$ | $52.4\%$ | $0.0440$ | $10.80\%$ |
| $0.80$ | $88.8\%$ | $0.0014$ | $46.38\%$ |
| $1.20$ | $99.7\%$ | $0.0000$ | $93.65\%$ |

Read the table as a statement about which hypotheses this design can test. A
$0.20$-standard-deviation effect — a realistic size for many geophysical
comparisons — will be missed $87\%$ of the time, and a study that reports "no
significant difference" at this $n$ has said almost nothing. The design chooses the
question, not the reverse; see
[24-02-04 Writing Results and Discussion Without Overclaiming](../02-scientific-writing/04-writing-results-discussion.md)
for the reporting consequence.

## 4. Flexibility: how a null result becomes a positive one

Researcher degrees of freedom are the choices that are individually defensible: the
processing band, the time window, the station subset, the taper, whether to
detrend, which outlier rule, which model comparison. If each choice gives an
independent chance to cross the threshold under the null, then

$$\mathbb{P}(\text{at least one significant}) = 1 - (1 - \alpha)^{k}$$

for $k$ equivalent choices. The demonstration confirms the formula:

| Defensible choices $k$ | Measured $P(\text{at least one } p < 0.05)$ | Prediction |
|---|---|---|
| $1$ | $4.7\%$ | $5.0\%$ |
| $4$ | $17.6\%$ | $18.5\%$ |
| $16$ | $55.5\%$ | $56.0\%$ |
| $64$ | $96.0\%$ | $96.2\%$ |

With $64$ defensible choices, a genuinely null result is reported as significant in
$96\%$ of experiments. Nothing here is fraud: each of the $64$ analyses is
defensible when considered alone. The failure is that the *set* was searched
without being reported.

## 5. Multiplicity in a family of tests

For $20$ independent null tests:

$$1 - 0.95^{20} = 64.2\%$$

family-wise error rate, measured as $64.2\%$ by the simulation. The Bonferroni
threshold $\alpha/m = 0.0025$ brings it to $4.9\%$ (exact $4.9\%$), at the cost of
power: at $n = 32$ a $0.5$-sigma effect has $52.4\%$ power uncorrected and much
less at $\alpha = 0.0025$. The expected number of significant results under the
complete null is $20 \times 0.05 = 1.00$ — one per experiment, every time.

Which correction to use is a statistical decision with a literature; the
requirement here is only that the *search* be reported: the number of tests, the
selection rule, the threshold and the correction. A reader who has those can
reconstruct the error rate; a reader who has only the winning $p$-value cannot.

## 6. Removing the flexibility in advance

A pre-analysis plan is a short document written before the analysis that fixes:

1. The hypotheses and, for each, the falsifier.
2. The primary outcome and its unit.
3. The sample size justification: the effect size, the level and the power.
4. The primary test, and the family of secondary tests with its correction.
5. The processing decisions that would otherwise be free: bands, windows, outlier
   rules, model comparisons.
6. The stopping rule: what would make you stop collecting, and what would not.

Points 5 and 6 are the ones that remove flexibility. A plan that fixes only the
test still leaves $64$ ways to reach it.

## Assumptions and regime of validity

1. **The simulations use the normal model with equal variances and independent
   samples.** Real geophysical series are autocorrelated; the qualitative results
   hold, the arithmetic changes, and an effective sample size replaces $n$.
2. **The flexibility model assumes independent, equivalent choices.** Real choices
   are correlated; the failure can be worse or better, and the number $k$ is
   rarely known.
3. **Bonferroni is conservative.** With correlated tests, a false-discovery-rate
   procedure is usually preferable; see
   [21-01-03 Resampling and Multiple Comparisons](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md).
4. **A pre-analysis plan does not make a study exploratory.** Exploratory work
   remains legitimate; what changes is that it is labelled and its results are
   treated as hypotheses for a new study.
5. **Falsifiability is necessary, not sufficient.** A falsifiable hypothesis can
   still be wrong for years, and confirmation in one region is not confirmation
   everywhere.

## The honest summary

A calibrated test recovers its nominal rate, and everything interesting happens
around it: at $n = 32$ a $0.2$-sigma effect is detected $13\%$ of the time, and
with $64$ defensible analysis choices a null result becomes significant $96\%$ of
the time. The remedy is not better statistics but fewer unstated choices: state the
hypotheses, the falsifier, the primary test and the free decisions before the data
arrive.

## Python demonstration

[`code/hypothesis_and_falsifiability_demo.py`](./code/hypothesis_and_falsifiability_demo.py)
prints four labelled sections: null calibration; power against effect size at fixed
$n$; flexibility versus the independence prediction; and multiplicity with and
without a correction.

```bash
cd 24-research-papers-writing/03-research-methods-and-rigour/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hypothesis_and_falsifiability_demo.py
```

## Exercises

Problems are in
[`exercises/02-hypothesis-and-falsifiability-exercises.md`](./exercises/02-hypothesis-and-falsifiability-exercises.md),
worked answers in
[`exercises/02-hypothesis-and-falsifiability-solutions.md`](./exercises/02-hypothesis-and-falsifiability-solutions.md).

## Mastery checkpoint

For a hypothesis you are currently testing:

1. Write $H_0$, $H_1$, the prediction and the falsifier.
2. State the primary outcome, its unit and the sample size justification.
3. List every analysis decision you have made since receiving the data, and count
   the ones that could have gone the other way.
4. Compute $1 - 0.95^{k}$ for that count.
5. Write the pre-analysis plan you would file for the next study, including the
   stopping rule.

## Common pitfalls

1. **A hypothesis that predicts everything.** If no observation would count
   against it, it is a framework, not a hypothesis.
2. **Testing after seeing the data.** The flexibility table is the reason the order
   matters.
3. **Reporting a single $p$-value from an unstated search.** With $20$ tests, one
   significant result is the expected outcome.
4. **Correcting for tests you did not run.** Bonferroni on a family that does not
   exist destroys power for nothing.
5. **Confusing a null result with no effect.** At low power, "not significant" is
   the expected outcome of a real effect.
6. **Calling exploratory analysis invalid.** It is valid and useful; label it and
   treat its findings as hypotheses.

## Where this is used

- **Pre-registration and registered reports:** the six points of §6 are the
  template.
- **Field campaigns:** the decisions in §5 are the ones a field plan must fix,
  because in the field they become irreversible; see
  [23-01 Field Safety, Planning and Logistics](../../23-field-methods-instruments/01-field-safety-and-planning/README.md).
- **Modelling studies:** parameter sweeps are a search over hypotheses; report the
  sweep; see
  [24-03-03 Designing Observational, Experimental and Modelling Studies](03-study-design.md).
- **Manuscript review:** asking for the search and not just the winner is the
  highest-yield referee question; see [05 Peer Review Practice](05-peer-review-practice.md).

## Related lessons

- [24-03-03 Designing Observational, Experimental and Modelling Studies](03-study-design.md) —
  what the design must fix for the tests to be meaningful.
- [24-02-04 Writing Results and Discussion Without Overclaiming](../02-scientific-writing/04-writing-results-discussion.md) —
  how to report a test without overclaiming.
- [21-08-02 Causal Inference Methods](../../21-statistics-bayesian-ml/08-causal-inference-and-design/02-causal-inference-methods.md) —
  what causal language requires beyond a significant test.
- [21-01-03 Resampling and Multiple Comparisons](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  the correction procedures this lesson only quantifies.

## Self-assessment checklist

- [ ] I can write a falsifier for any hypothesis I state.
- [ ] I can compute power for a given $n$ and effect size.
- [ ] I can compute the flexibility error rate for $k$ choices.
- [ ] I can compute a family-wise error rate and the cost of correction.
- [ ] I can list the free decisions in my own analysis.
- [ ] I can write a pre-analysis plan with a stopping rule.
