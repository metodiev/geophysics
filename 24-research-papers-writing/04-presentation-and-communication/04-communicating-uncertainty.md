---
id: 24-04-04
title: "Communicating Uncertainty to Non-Specialists"
level: research
prereqs: ["24-04-01", "24-03-02"]
estimated_minutes: 50
tags: [communication, uncertainty, decisions, likelihood, risk]
---

# Communicating Uncertainty to Non-Specialists

Uncertainty communication is a design problem with three parts: how to turn a
number into a statement, which words to use when a number is not possible, and what
the audience will do with it. This lesson measures each. It contrasts a point
estimate with an interval, quantifies the ambiguity of standard likelihood phrases,
shows how a decision rule changes when the loss ratio changes, and treats framing as
a variable to be tested rather than a stylistic preference.

The organising idea is that **a decision, not a probability, is what an audience
needs**. A credible interval is only useful once the reader knows the threshold at
which they would act and what a mistake costs; without those, the interval is a
decorative hedge. The lesson's decision table shows the threshold moving while the
estimate stays fixed — which is the honest picture.

> **Data provenance.** All numbers are **SYNTHETIC**. The estimate, interval,
> loss values and misinterpretation rates are chosen teaching values. The
> likelihood phrases and their probability ranges follow the convention used in
> IPCC assessment reports and are quoted as a stated scale, not as measurements.

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** a credible interval into a statement that names what it does and does
   not support.
2. **Compute** the interval implied by a different confidence level and **state**
   what changes in the claim.
3. **Quantify** the ambiguity of a likelihood phrase and **decide** when a phrase or
   a number is appropriate.
4. **Analyse** a decision as a loss comparison and **compute** the probability
   threshold above which acting is optimal.
5. **Demonstrate** that the same estimate leads to different recommendations under
   different loss ratios.
6. **Treat** framing as a design variable and **state** how to test a sentence's
   reading.

## Prerequisites

- [24-04-01 Conference Talks: Structure, Pacing, Visuals](01-conference-talks.md) —
  the talk format in which uncertainty must fit.
- [24-03-02 Hypotheses, Falsifiability and Testing in Earth Science](../03-research-methods-and-rigour/02-hypothesis-and-falsifiability.md) —
  the statistical objects being communicated.

## 1. From interval to statement

The demonstration's estimate is a point value of $3.6$ with a $90\%$ credible
interval $[2.4, 4.8]$. The interval's width is

$$4.8 - 2.4 = 2.4\ \text{units}, \qquad
\frac{2.4}{3.6} \times 100 = 67\%\ \text{of the point estimate}.$$

Changing the level changes the interval, not the data:

| Level | Half-width | Interval |
|---|---|---|
| $90\%$ | $1.20$ | $[2.40, 4.80]$ |
| $95\%$ | $1.43$ | $[2.17, 5.03]$ |
| $99\%$ | $1.88$ | $[1.72, 5.48]$ |

The decision threshold in this example is $3.0$, which lies **inside** the $90\%$
interval. That single fact governs the communication: the data are consistent both
with acting and with not acting, so a statement of the form "the value is $3.6$"
discards the only part of the result the audience needs. The sentence to say is:

> The best estimate is $3.6$, with a $90\%$ range of $2.4$ to $4.8$. The action
> threshold is $3.0$, so the data do not settle whether to act.

## 2. Likelihood words: the width of each phrase

When a probability cannot be given, standard phrases are used. Their ranges, as used
in IPCC assessment reports:

| Phrase | Range | Width |
|---|---|---|
| Virtually certain | $[99\%, 100\%]$ | $1$ point |
| Extremely likely | $[95\%, 100\%]$ | $5$ points |
| Very likely | $[90\%, 100\%]$ | $10$ points |
| Likely | $[66\%, 100\%]$ | $34$ points |
| About as likely as not | $[33\%, 66\%]$ | $33$ points |
| Unlikely | $[0\%, 33\%]$ | $33$ points |
| Very unlikely | $[0\%, 10\%]$ | $10$ points |
| Extremely unlikely | $[0\%, 5\%]$ | $5$ points |

The narrowest phrase spans $5$ points and the widest $34$ — a ratio of

$$\frac{34}{5} = 6.8 .$$

"Likely" therefore carries a third of the probability range: it is a statement
about ordering, not about probability. Two rules follow:

1. **Pair the phrase with the number** when the number exists: "very likely
   (90–100%), and our estimate is 93%".
2. **Do not use a phrase where the distinction matters.** If the decision threshold
   is at $80\%$, the difference between "likely" and "very likely" is the decision,
   and only the number can express it.

## 3. Decisions: what actually determines the recommendation

Let acting when the truth is below the threshold cost $L_{\text{wrong}}$, and not
acting when it is above cost $L_{\text{missed}}$. Acting is optimal when the
posterior probability of being above the threshold exceeds

$$p^{*} = \frac{L_{\text{wrong}}}{L_{\text{wrong}} + L_{\text{missed}}} .$$

The demonstration's posterior has a standard error of $0.729$ units, implied by its
$90\%$ interval, and the decision depends on the loss pair:

| Estimate | $P(\text{above})$ | Optimal with $(10, 6)$ | Optimal with $(20, 6)$ |
|---|---|---|---|
| $3.0$ | $0.500$ | wait | wait |
| $3.2$ | $0.608$ | wait | wait |
| $3.4$ | $0.708$ | **act** | wait |
| $3.6$ | $0.795$ | **act** | **act** |
| $4.0$ | $0.915$ | act | act |

With losses $(10, 6)$ the threshold is $p^{*} = 10/16 = 0.625$; with $(20, 6)$ it is
$0.769$. At an estimate of $3.4$ — the same number, the same interval — the
recommendation differs between the two loss pairs. The table's expected losses make
the cost of a fixed rule visible: at $3.4$ with losses $(20,6)$, acting because the
point estimate exceeds the threshold costs $5.835$ units against $4.250$ for
waiting.

**The communication consequence.** The loss ratio is a value judgement, and it
belongs in the document, stated by the authors and negotiable with the audience.
"Assuming a mistake costs twice as much as a missed opportunity, the recommendation
is to wait" is a sentence a decision-maker can engage with; "the model says $3.4$" is
not.

## 4. Framing is a variable

The same quantity has several correct framings, and they are not equally understood.
The demonstration's chosen misinterpretation rates:

| Framing | Misinterpretation rate |
|---|---|
| "a $10\%$ chance of exceeding the threshold" | $11\%$ |
| "a 1 in 10 chance of exceeding the threshold" | $28\%$ |

$$\text{ratio} = \frac{0.28}{0.11} = 2.55,$$

which in an audience of $200$ is a difference of about $34$ people misreading the
same number.

The rates are chosen teaching values, not measurements — but the variable is real
and testable, which is the point. Before publishing a sentence that carries a
consequence, show it to two people outside the field and ask them to restate it. If
their restatements differ from each other, the sentence is the problem, not the
audience.

Three framing practices that survive the test:

1. **Give a range and a reference class.** "2–5 m of subsidence by 2050, relative to
   the 2020 level" is checkable; "significant subsidence" is not.
2. **State the threshold and the action.** "We recommend action if the estimated
   subsidence exceeds 3 m; the estimate is 3.6 m with a range of 2.4–4.8 m."
3. **Avoid single-number simplification of a decision.** A point estimate plus a
   recommendation hides the interval that determines whether the recommendation is
   robust.

## Assumptions and regime of validity

1. **The estimate and interval are synthetic.** The arithmetic of interval width,
   loss thresholds and the decision table is the transferable content.
2. **The likelihood ranges are a published convention.** Other institutions use
   different words and ranges; state the scale you are using, because the phrases
   are not self-defining.
3. **The loss values are chosen.** Real loss ratios are political and economic, and
   different stakeholders hold different ones; a communication should say whose
   values it uses.
4. **Misinterpretation rates are modelled.** Real comprehension depends on numeracy,
   language and context; the framing difference is the robust part.
5. **A decision analysis is not a decision.** It structures the choice; it does not
   make it, and it should not be presented as if it did.

## The honest summary

An interval whose range contains the decision threshold cannot support a
recommendation, and that is a property of the interval, not of the wording. Standard
likelihood phrases span up to $34$ probability points, so they are used alongside
numbers or not at all. The recommendation changes with the loss ratio at the same
estimate, and framing changes comprehension by a factor of $2.55$ in the modelled
rates. State the threshold, the losses and the range — and test the sentence.

## Python demonstration

[`code/communicating_uncertainty_demo.py`](./code/communicating_uncertainty_demo.py)
prints four labelled sections: the interval at three levels; the width of each
likelihood phrase; the decision table for two loss pairs; and the framing
comparison.

```bash
cd 24-research-papers-writing/04-presentation-and-communication/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python communicating_uncertainty_demo.py
```

## Exercises

Problems are in
[`exercises/04-communicating-uncertainty-exercises.md`](./exercises/04-communicating-uncertainty-exercises.md),
worked answers in
[`exercises/04-communicating-uncertainty-solutions.md`](./exercises/04-communicating-uncertainty-solutions.md).

## Mastery checkpoint

1. Take a result of yours with an interval and write the three sentences of §1.
2. State the decision threshold your audience would use, and whether it lies inside
   your interval.
3. Write the loss ratio you are assuming and where it comes from.
4. Replace every likelihood phrase in one document with a number, or keep the phrase
   and add the number.
5. Test your key sentence on two non-specialists and record their restatements.

## Common pitfalls

1. **Reporting the point estimate as the result.** It removes the decision.
2. **Hiding the interval in an appendix.** The interval is the finding for a decision
   audience.
3. **Using "likely" as if it were a probability.** It spans a third of the range.
4. **Burying the loss ratio.** The recommendation depends on it; state it.
5. **Assuming the audience misreads.** Test the sentence instead of the audience.
6. **Presenting a decision analysis as a decision.** It structures a choice that
   people, not models, make.

## Where this is used

- **Hazard and risk communication:** thresholds and loss ratios are the substance;
  see [24-04-05 Public Engagement, Media and Policy Communication](05-public-and-media.md).
- **Policy briefings:** the three framing practices are the standard for a briefing
  note.
- **Reports to stakeholders:** the loss ratio is usually the negotiable part, and
  naming it changes the conversation.
- **Scientific talks:** one slide of interval-plus-threshold is more useful than
  three of results; see [24-04-01 Conference Talks](01-conference-talks.md).

## Related lessons

- [24-04-05 Public Engagement, Media and Policy Communication](05-public-and-media.md) —
  the compression that follows this material.
- [24-02-04 Writing Results and Discussion Without Overclaiming](../02-scientific-writing/04-writing-results-discussion.md) —
  the same discipline for specialist readers.
- [24-03-03 Designing Observational, Experimental and Modelling Studies](../03-research-methods-and-rigour/03-study-design.md) —
  where the precision of the interval is decided.
- [21-09-02 Reporting Uncertainty: Statistical Ethics](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/02-reporting-uncertainty-ethics.md) —
  the ethical frame for the same choices.

## Self-assessment checklist

- [ ] I can convert an interval into three sentences that name the threshold.
- [ ] I can compute intervals at other levels and state the change in the claim.
- [ ] I can quantify the ambiguity of a likelihood phrase.
- [ ] I can compute $p^{*}$ from a loss pair and read the decision table.
- [ ] I can explain why the same estimate gives different recommendations.
- [ ] I can test a sentence's framing on a non-specialist.
