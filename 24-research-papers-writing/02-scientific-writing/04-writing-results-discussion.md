---
id: 24-02-04
title: "Writing Results and Discussion Without Overclaiming"
level: doctoral
prereqs: ["24-02-02", "24-01-03"]
estimated_minutes: 60
tags: [writing, results, discussion, effect-size, p-values, overclaiming]
---

# Writing Results and Discussion Without Overclaiming

Overclaiming is almost never a lie. It is a sentence that is true of the
statistic and false of the world: a $p$-value quoted as if it measured
importance, a small effect reported as a discovery, a winner selected from many
tests reported as if it were the only test. This lesson makes the gap visible by
measurement — how the $p$-value falls while the effect stays fixed, how much the
effects of "significant" studies are inflated, and what multiplicity does to a
claim — and then states the sentence patterns that keep a paper inside its
evidence.

The organising idea is that **the Results section reports two numbers, not one**:
the size of the effect and the precision of the estimate. The $p$-value is a
third object, a statement about the null, and it moves with sample size in a way
that has nothing to do with importance.

> **Data provenance.** All numbers are **SYNTHETIC**. The demonstration simulates
> two-group comparisons from the normal model with chosen effect sizes and sample
> sizes; no real dataset is analysed and no published result is reproduced. The
> multiplicity calculation uses uniform draws, which is the definition of a null
> $p$-value distribution.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** statistical significance, effect size and precision, and
   **state** what each does and does not measure.
2. **Demonstrate** that the $p$-value shrinks with sample size while the effect
   size does not, using a simulated experiment.
3. **Quantify** the winner's curse: the inflation of effect size among results
   declared significant, as a function of sample size.
4. **Compute** the family-wise error rate of a set of tests and **state** what a
   correction costs in power.
5. **Write** Results sentences that pair every estimate with its uncertainty and
   every comparison with its sample size.
6. **Write** Discussion sentences that mark speculation as speculation and state
   what would falsify the conclusion.

## Prerequisites

- [24-02-02 Paper Structure: IMRaD and Its Variants](02-paper-structure.md) — why
  these two sections have different licences.
- [24-01-03 Critiquing Methods, Data and Inference](../01-reading-research-literature/03-critiquing-methods.md) —
  the inferential axis this lesson writes to.

## 1. Three objects, three sentences

| Object | What it says | What it does not say |
|---|---|---|
| Effect size | How large the difference is, in stated units | Whether it matters physically |
| Precision | How tightly the data fix it (a standard error or interval) | Whether the estimate is unbiased |
| $p$-value or test statistic | How surprising the data are under a stated null | Size, importance or the probability the claim is true |

A Results section that reports only the third has told the reader how surprised to
be and nothing about what happened.

## 2. What a null effect produces

The demonstration simulates $1000$ two-group comparisons with a true effect of
zero and reports the false-positive rate at $\alpha = 0.05$:

| Group size $n$ | False positives | 1 s.e. | Mean observed $d$ |
|---|---|---|---|
| $20$ | $5.3\%$ | $0.7\%$ | $+0.0078$ |
| $200$ | $6.1\%$ | $0.7\%$ | $+0.0016$ |
| $2000$ | $4.5\%$ | $0.7\%$ | $-0.0002$ |

All three are consistent with the nominal $5\%$, and the mean observed effect is
zero to within its own scatter. That is the calibration that makes the next table
interpretable: any excess of significance in real literature is an excess over
these numbers.

## 3. The $p$-value falls while the effect stays put

With a true effect of $d = 0.20$ within-group standard deviations:

| Group size $n$ | Power at $\alpha = 0.05$ | Median $p$ | $p < 0.001$ in | Mean observed $d$ |
|---|---|---|---|---|
| $20$ | $10.6\%$ | $3.89\times10^{-1}$ | $0.6\%$ | $0.200 \pm 0.330$ |
| $200$ | $49.9\%$ | $5.03\times10^{-2}$ | $9.3\%$ | $0.200 \pm 0.098$ |
| $2000$ | $100.0\%$ | $2.83\times10^{-10}$ | $100.0\%$ | $0.200 \pm 0.031$ |

Three facts to carry into the writing:

1. **The effect size is constant at $0.20$** in every row. The size of what was
   found did not change; only the precision did.
2. **The median $p$-value falls by nine orders of magnitude** from $n = 20$ to
   $n = 2000$. A reported $p = 10^{-10}$ therefore says almost nothing about the
   effect being large.
3. **The scatter of the estimate falls as $1/\sqrt{n}$**, from $\pm 0.330$ to
   $\pm 0.031$. Precision is the quantity that sample size actually buys.

The writing consequence is direct: to claim importance you need the effect in
physical units and a comparison with the variability that matters in the
application — not a smaller $p$-value. A velocity change of $0.2\%$ can be
detected with a sufficiently large survey and still be irrelevant to the
interpretation, and the sentence must say which of those it is.

## 4. The winner's curse

If a paper's result is selected because it crossed a threshold, the selection
distorts the estimate. Among the studies the demonstration declares significant:

| Group size $n$ | Declared significant | Mean $d$ among them | Inflation | Replication expected to report |
|---|---|---|---|---|
| $20$ | $96$ of $1000$ | $0.752$ | $3.76\times$ | $0.20$, i.e. $73.4\%$ lower |
| $200$ | $521$ of $1000$ | $0.279$ | $1.39\times$ | $0.20$, i.e. $28.3\%$ lower |
| $2000$ | $1000$ of $1000$ | $0.200$ | $1.00\times$ | $0.20$, i.e. $0.2\%$ lower |

At $n = 20$ the published effect is nearly four times the truth, and a replication
will fail to reproduce it by construction — not because anyone cheated, but
because the threshold selected the lucky draws. The practical rules are:

- Report all the estimates you computed, not only the significant one.
- For any threshold-based selection, state the threshold and the number of tests.
- Prefer an interval to a verdict: "$d = 0.20\ [0.06, 0.34]$" is honest at every
  sample size.

## 5. Multiplicity

Twenty independent null tests per experiment, over $1000$ experiments, give a
family-wise error rate of $63.6\%$ — the probability of at least one significant
result by chance alone. The Bonferroni threshold $\alpha/m = 0.05/20 = 0.0025$
brings that to $4.3\%$, and the expected number of "significant" results per
experiment before correction is $20 \times 0.05 = 1.00$.

Two consequences for writing:

- **Report the search.** "We tested 20 candidate predictors and report all of
  them" is a different paper from one that reports a single unannounced test, even
  with identical numbers.
- **Say what the correction cost.** Bonferroni holds the family-wise rate at the
  price of power; a less conservative procedure such as a false-discovery-rate
  control is often preferable, and the choice belongs in the Methods (see
  [21-01-03 Resampling and Multiple Comparisons](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md)).

## 6. Sentence patterns

**Results.**

- *Weak:* "There is a significant difference in velocity (p < 0.05)."
- *Strong:* "The mean velocity is $2.45\ \mathrm{km\,s^{-1}}$ in the northern
  block and $2.28\ \mathrm{km\,s^{-1}}$ in the southern block, a difference of
  $0.17\ \mathrm{km\,s^{-1}}$ (95% CI $[0.04, 0.30]$; $n = 96$ per block;
  two-sided $p = 0.01$)."

The strong version contains the estimate, the unit, the interval, the sample size
and the $p$-value, in that order of prominence. A reader who disagrees with the
$p$-value can still use the estimate.

**Discussion.**

- *Weak:* "This proves that the fault is unlocked."
- *Strong:* "The low $b$-value is consistent with a partly unlocked fault, provided
  the catalogue is complete above $M_c$; a complete catalogue with the same
  $b$-value would falsify the alternative that the apparent decrease is a
  detection artefact."

The strong version names the assumption, states the inference as one of several
consistent readings, and names the observation that would falsify it.

## 7. A submission check for the two sections

1. Does every number in Results carry a unit and an uncertainty?
2. Is every comparison accompanied by its sample size?
3. Is the number of tests reported, with the threshold and any correction?
4. Does any Results sentence contain causal language that the design cannot
   support?
5. Does every Discussion claim trace to a specific result sentence?
6. Does each Discussion claim state what would falsify it?
7. Is speculation marked, and is the marking consistent?

## Assumptions and regime of validity

1. **The simulations use the normal model with equal variances.** Real data have
   skew, outliers, autocorrelation and heteroscedasticity; the qualitative
   behaviour of $p$-values and intervals is the same, the arithmetic is not.
2. **The $p$-values are computed with a normal approximation.** At the sample
   sizes used the difference from a $t$ distribution is negligible; it is not
   negligible at $n < 10$.
3. **The tests are independent.** Real candidate predictors correlate strongly, so
   a Bonferroni correction is conservative and a permutation or resampling
   procedure is usually better.
4. **The winner's-curse table assumes selection on significance only.** Selecting
   on significance plus a size threshold, as journals and authors often do, makes
   the inflation worse.
5. **No sentence pattern repairs a bad design.** These rules make a result honest
   about its strength; they cannot make an unidentifiable quantity identifiable.

## The honest summary

Statistical significance moves with sample size, effect size does not, and
selecting on significance inflates the effect by a factor of $3.76$ at the
smallest sample size simulated here. Reporting the estimate, its interval and the
number of tests is not a stylistic preference: it is the difference between a
result a reader can use and a result a reader must reinterpret.

## Python demonstration

[`code/writing_results_discussion_demo.py`](./code/writing_results_discussion_demo.py)
prints four labelled sections: the calibration of a null effect at three sample
sizes; power, median $p$ and effect size at the same sizes; the winner's-curse
table; and the multiplicity calculation with and without a Bonferroni threshold.

```bash
cd 24-research-papers-writing/02-scientific-writing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python writing_results_discussion_demo.py
```

## Exercises

Problems are in
[`exercises/04-writing-results-discussion-exercises.md`](./exercises/04-writing-results-discussion-exercises.md),
worked answers in
[`exercises/04-writing-results-discussion-solutions.md`](./exercises/04-writing-results-discussion-solutions.md).

## Mastery checkpoint

Take your last results paragraph and:

1. mark every quantitative claim and check it for a unit and an uncertainty;
2. state the sample size supporting each comparison;
3. state the number of tests you ran to produce the paragraph;
4. rewrite each claim as an estimate with an interval;
5. do the same for the corresponding Discussion sentence, and add the observation
   that would falsify it.

## Common pitfalls

1. **Using $p$ as a measure of size.** The demonstration's $p$ falls nine orders of
   magnitude while the effect stays at $0.20$.
2. **Reporting only the significant candidates.** It converts a search into a
   claim; see §5.
3. **Treating "not significant" as "no effect".** Absence of evidence at a given
   precision is not evidence of absence; report the interval.
4. **Causal verbs from observational designs.** "Causes", "drives" and "controls"
   need a design that supports them; see
   [21-08-02 Causal Inference Methods](../../21-statistics-bayesian-ml/08-causal-inference-and-design/02-causal-inference-methods.md).
5. **Unmarked speculation.** A hypothesis stated without a marker is read as a
   conclusion.
6. **Round-tripping the abstract.** Loosening the claim in the Discussion but
   keeping the tight version in the abstract reintroduces the overclaim; see
   [05 Abstracts, Titles and the Art of the Concrete Claim](05-writing-abstracts-titles.md).

## Where this is used

- **Writing any paper with a statistical result:** the estimate-plus-interval
  pattern is portable across fields.
- **Peer review:** the same checks in reverse; see
  [24-03-05 Peer Review Practice](../03-research-methods-and-rigour/05-peer-review-practice.md).
- **Reports and policy documents:** uncertainty language must survive
  compression; see
  [24-04-04 Communicating Uncertainty to Non-Specialists](../04-presentation-and-communication/04-communicating-uncertainty.md).
- **Pre-registration and registered reports:** stating the tests and the threshold
  in advance removes most of §5's problem.
- **Machine-learning results:** the same selection effects appear when a model is
  chosen on a validation set; see
  [21-04-03 Model Assessment](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md).

## Related lessons

- [24-02-03 Writing Methods Sections That Can Be Reproduced](03-writing-methods.md) —
  the decisions these results depend on.
- [24-03-02 Hypotheses, Falsifiability and Testing in Earth Science](../03-research-methods-and-rigour/02-hypothesis-and-falsifiability.md) —
  the falsifiability framing used in the Discussion.
- [24-01-03 Critiquing Methods, Data and Inference](../01-reading-research-literature/03-critiquing-methods.md) —
  how a reader detects the overclaim you are trying to avoid.
- [21-09-02 Reporting Uncertainty: Statistical Ethics](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/02-reporting-uncertainty-ethics.md) —
  the ethical frame for the same rules.

## Self-assessment checklist

- [ ] I can name the three objects and what each measures.
- [ ] I can demonstrate the $p$-value/effect-size separation with numbers.
- [ ] I can compute the winner's curse for a given sample size and threshold.
- [ ] I can compute a family-wise error rate and state the cost of correction.
- [ ] I can write a Results sentence with estimate, interval and sample size.
- [ ] I can write a Discussion sentence with a falsification condition.
