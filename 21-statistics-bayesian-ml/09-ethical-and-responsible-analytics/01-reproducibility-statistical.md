---
id: 21-09-01
title: "Statistical Reproducibility, p-Hacking and Multiple Comparisons"
level: graduate
prereqs: ["21-01-03", "21-07-03", "21-06-09"]
estimated_minutes: 60
tags: [reproducibility, multiplicity, p-hacking, statistics, teaching]
---

# Statistical Reproducibility, p-Hacking and Multiple Comparisons

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the family-wise error rate of $m$ independent tests and **explain**
   why it grows with the number of tests rather than with the science.
2. **Apply** the Bonferroni and Benjamini-Hochberg procedures, and **state** the
   error rate each one controls.
3. **Measure** the power and the false-discovery rate of both procedures when some
   hypotheses are true, and **choose** between them for a stated purpose.
4. **Quantify** the inflation of the error rate produced by optional stopping, and
   the effect-size inflation that accompanies it.
5. **Distinguish** a pre-specified analysis from a garden of forking paths, and
   **identify** the three decisions that most often hide the multiplicity.
6. **Explain** why a reported $p$-value cannot distinguish a pre-specified test from
   a selected one.
7. **Specify** a reproducible analysis: the hypotheses and their number, the
   planned sample size or stopping rule, the correction (or the reason for none),
   the data and code, and the decisions taken after seeing the data.

Every test statistic, error rate and effect below is **SYNTHETIC**, produced by
[`code/reproducibility_statistical_demo.py`](./code/reproducibility_statistical_demo.py).
No study, data set or published p-value is used or quoted.

## Prerequisites

- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  the Monte Carlo machinery used to measure every rate here.
- [21-07-03 Statistical Spectral Analysis and Significance Testing](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/03-spectral-analysis-statistical.md) —
  the same multiplicity problem in a spectral setting, where a "peak" is a test.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](../../21-statistics-bayesian-ml/06-ml-in-geophysics/09-ml-pitfalls-geophysics.md) —
  selection leakage, of which p-hacking is the reporting-side form.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md) —
  the same arithmetical structure seen from the modelling side.

## 1. Intuition: the arithmetic of looking many times

A $p$-value is a probability about the test, not about the hypothesis: under the
null, $\Pr(p \le 0.05) = 0.05$. That statement holds **per test**. If you run $m$
independent tests, the probability that *at least one* reaches 0.05 is

$$\mathrm{FWER} = 1 - (1-\alpha)^m ,$$

which for $m = 20$ and $\alpha = 0.05$ is $0.6415$. The demonstration measures
$0.6280$ over 4000 synthetic experiments against the analytic $0.6415$ — the
arithmetic is exact, and it is a property of the number of tests rather than of the
subject matter.

Two consequences frame the whole lesson:

- **An unremarkable result becomes remarkable by repetition.** Twenty null
  hypotheses produce a significant one two thirds of the time, so "we found a
  significant relationship" carries no information unless the number of tests that
  produced it is stated.
- **The reported number cannot show this.** A $p$-value of 0.03 from the single
  pre-specified test and a $p$-value of 0.03 selected from twenty are identical
  numbers with different meanings.

The three ways the multiplicity enters an analysis: testing many hypotheses
explicitly, choosing among many analyses (the garden of forking paths), and looking
at the data repeatedly (optional stopping).

## 2. Corrections and what they control

**Bonferroni** compares each $p$-value with $\alpha/m$. It controls the
family-wise error rate at $\alpha$ from above, regardless of dependence between the
tests, and it is conservative when $m$ is large or the tests are correlated.

**Benjamini-Hochberg** orders the $p$-values $p_{(1)} \le \dots \le p_{(m)}$ and
rejects the largest $k$ for which $p_{(k)} \le qk/m$. It controls the **false
discovery rate** — the expected *proportion* of wrong findings among the findings —
rather than the probability of any error. When all hypotheses are null the two
coincide:

| Procedure (all 20 null, 4000 experiments) | measured error rate |
|---|---|
| none | $0.6280$ |
| Bonferroni ($\alpha/m$) | $0.0410$ |
| Benjamini-Hochberg ($q = 0.05$) | $0.0425$ |

Both are at or below the nominal 0.05, and the small differences are Monte-Carlo
error ($\sqrt{0.05 \times 0.95/4000} = 0.0034$).

**With true effects present** (15 nulls, 5 alternatives with mean $z = 2.5$, 400
experiments):

| Procedure | power | false discoveries per experiment | FDR | findings per experiment |
|---|---|---|---|---|
| Bonferroni | $0.292$ | $0.05$ | $0.033$ | $1.51$ |
| Benjamini-Hochberg | $0.413$ | $0.14$ | $0.066$ | $2.21$ |

The trade is visible: BH finds $46\%$ more findings and $1.4$ times the power, at
the cost of three times the false discoveries per experiment — while keeping the
*proportion* of false findings near $q$. The choice is about what a wrong finding
costs: for an exploratory screen that will be followed by independent
confirmation, FDR control is the right target; for a regulatory decision on twenty
candidate sites, the family-wise rate is.

## 3. Optional stopping

Look at accumulating data and stop when the result is significant, and the error
rate is no longer $\alpha$. With up to five interim looks at $n = 20, 40, 60, 80,
100$ on **null** data:

| Quantity | Value |
|---|---|
| measured rate of a "significant" result | $0.1485$ |
| inflation over the nominal 0.05 | $2.97\times$ |
| mean reported effect among the significant results | $0.3724\ \sigma$ |
| true effect | $0$ |

Both columns are the same phenomenon. The error rate nearly triples because each
look is another chance to cross the threshold; and the *effects* that survive are
those that happened to wander far, so the reported effect is $0.37$ standard errors
from the truth when the truth is zero. This is the mechanism behind the failure of
early "significant" findings to replicate: the number was never an estimate of the
effect — it was the maximum of a random walk.

The remedies are structural, not analytical: a pre-registered sample size; or a
sequential design with a stated spending function (a group-sequential boundary, a
Pocock or O'Brien-Fleming rule) that sets the thresholds so the overall level holds;
or, for a purely exploratory analysis, reporting the results as exploratory with no
$p$-values at all.

## 4. The garden of forking paths

Optional stopping is the visible half of the problem. The invisible half is the
sequence of analytic choices made after seeing the data — which is not dishonest
and usually not even conscious:

| Decision | Multiplicity it creates |
|---|---|
| which outcome variable to report | one test per candidate outcome |
| which time window or magnitude range to analyse | one test per window |
| which processing variant or correction to apply | one per variant |
| which covariates to include | one per specification |
| which spatial scale or smoothing to use | one per scale |
| which subregion or station subset to present | one per subset |

The demonstration's third reporting protocol (see
[21-09-02](./02-reporting-uncertainty-ethics.md)) is the arithmetic of one of these:
selecting the most favourable of five processing variants shifts the reported value
by about a third of a millimetre — more than its own interval's half-width — and
drops the interval's coverage from $0.95$ to $0.45$.

The practical defence is a **pre-analysis plan**, which need not be elaborate: state
the hypotheses and their count, the target quantity, the sample size or stopping
rule, the primary specification and the secondary ones, and the correction if any.
Decisions taken afterwards are permitted and often necessary; what matters is that
they are *reported as decisions*, so that a reader can multiply the tests by
themselves.

## 5. Assumptions and regime of validity

1. **Independence.** The formula $1-(1-\alpha)^m$ assumes independent tests. Real
   tests are correlated (nested models, adjacent windows, nearby sites), which makes
   the formula an **upper bound**: correlated tests overlap and the effective number
   is smaller. Bonferroni remains valid; BH needs modification.
2. **The null p-values are uniform.** Calibration assumes the test statistic's null
   distribution is right; a badly specified model makes even a corrected analysis
   invalid.
3. **The corrections are about errors, not about truth.** A corrected test controls
   a long-run error rate; it does not make a single finding reproducible. Replication
   in an independent sample is the only direct evidence.
4. **The stopping rule is known.** The measured $2.97\times$ inflation depends on
   five looks; more looks inflate more, and any reader who does not know the rule
   cannot compute the correction.
5. **The synthetic statistics are exact.** Real data add model misspecification,
   measurement error and dependence, all of which can only enlarge the problems
   quantified here.

## The honest summary

On 4000 synthetic experiments of 20 independent null hypotheses, the family-wise
error rate without correction is measured at $0.6280$ against the analytic
$0.6415$; Bonferroni and Benjamini-Hochberg both bring it below $0.05$
($0.0410$ and $0.0425$). With five true effects, Bonferroni reaches power $0.292$
with an FDR of $0.033$ and BH reaches $0.413$ with $0.066$. Optional stopping with
five looks inflates the nominal level by a factor of $2.97$ and returns a mean
effect of $0.3724\sigma$ when the truth is exactly zero. The transferable
conclusions: multiplicity is arithmetic, not misconduct; state the number of tests
and the stopping rule; choose the error rate you are controlling and say which;
and remember that a single $p$-value cannot reveal how many tests produced it.

## Python demonstration

[`code/reproducibility_statistical_demo.py`](./code/reproducibility_statistical_demo.py)
prints every number quoted above. It:

1. measures the family-wise error rate for 20 null tests with no correction, with
   Bonferroni and with Benjamini-Hochberg, and prints the analytic value beside them;
2. repeats the experiment with five true effects and prints the power, the false
   discoveries per experiment and the realised FDR for both procedures;
3. simulates null trials with five interim looks, printing the measured error rate,
   its inflation factor, and the mean reported effect among the significant results;
4. prints the three reporting rules side by side — one test, twenty tests, twenty
   tests with stopping — and a `SYNTHETIC` provenance line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproducibility_statistical_demo.py
```

It runs in about 0.9 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/01-reproducibility-statistical-exercises.md`](./exercises/01-reproducibility-statistical-exercises.md)
and [`exercises/01-reproducibility-statistical-solutions.md`](./exercises/01-reproducibility-statistical-solutions.md).

## Mastery checkpoint

Without notes:

1. Derive $1-(1-\alpha)^m$ and evaluate it for $m = 5$, $20$ and $100$ at
   $\alpha = 0.05$. State what the limit is as $m$ grows.
2. Apply BH by hand to the $p$-values $0.001, 0.008, 0.039, 0.041, 0.042, 0.06,
   0.074, 0.205, 0.212, 0.216$ at $q = 0.05$ and state the number of rejections.
3. State the difference between controlling the family-wise rate and controlling the
   false discovery rate, and give a decision context for each.
4. Optional stopping gives a measured rate of $0.1485$ and a mean effect of
   $0.3724\sigma$ under the null. Explain in two sentences why the second number is
   the more damaging of the two for the literature.

## Common pitfalls

1. **Reporting the smallest of many $p$-values as if it were pre-specified.** The
   measured error rate is $0.6280$.
2. **Comparing a corrected and an uncorrected analysis as if the correction were a
   different result.** Both are the same data; the correction changes the question.
3. **Stopping when the result is significant.** The rate triples and the reported
   effect is a maximum of a random walk.
4. **Assuming correlation saves you.** Correlated tests reduce the effective count;
   they do not remove the multiplicity, and they make BH's assumptions harder to
   verify.
5. **Treating a pre-analysis plan as a bureaucratic artefact.** It exists to make
   the number of tests countable, which is the only defence against the arithmetic.
6. **Concluding that exploratory analysis is illegitimate.** It is not; reporting
   exploratory findings as confirmatory is.

## Where this is used

- **Multi-station or multi-parameter geophysical analyses**, where hundreds of
  correlations are computed and the strongest reported.
- **Hazard and precursor studies**, where the search for a precursory signal over
  many stations, windows and variables is the classic garden of forking paths.
- **Survey and campaign processing**, where the choice among processing variants is
  a hidden test (see [21-09-02](./02-reporting-uncertainty-ethics.md)).
- **Machine-learning benchmarks**, where model selection on a test set is the same
  multiplicity with a different name
  ([21-06-08](../../21-statistics-bayesian-ml/06-ml-in-geophysics/08-remote-sensing-ml.md)).
- **Environmental and health studies of geophysical exposure**, where the outcome
  and window choices multiply the analyses.

## Related lessons

- [21-09-02 Honest Reporting of Uncertainty and Limitations](./02-reporting-uncertainty-ethics.md) —
  what a selected result does to a reported interval.
- [21-09-03 Data Ethics, Indigenous Data Sovereignty and Geoscience](./03-data-ethics-geoscience.md) —
  the governance questions that sit alongside the statistical ones.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  the Monte Carlo measurement of every rate here.
- [21-07-03 Statistical Spectral Analysis and Significance Testing](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/03-spectral-analysis-statistical.md) —
  multiplicity over frequencies, with the same arithmetic.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md) —
  multiplicity inside a cross-validation loop.

## Self-assessment checklist

- [ ] I can compute the family-wise error rate for $m$ tests.
- [ ] I can apply Bonferroni and BH by hand and say what each controls.
- [ ] I can compare them by power and FDR when effects are present.
- [ ] I can measure the inflation from optional stopping.
- [ ] I can list the six decisions that create hidden multiplicity.
- [ ] I can list the five items a reproducible analysis must state.
