---
id: 25-06-05
title: "Capstone: Presentation, Defence and Peer Critique"
level: research
prereqs: ["25-06-04", "22-01-02", "21-09-01", "25-05-05"]
estimated_minutes: 240
tags: [capstone, defence, presentation, peer-review, research]
---

# Capstone: Presentation, Defence and Peer Critique

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** a presentation whose every slide carries one quantitative claim restating
   a Results item, and whose timing is rehearsed to the minute.
2. **Predict** the questions a panel will ask by mapping each one to a re-computation of
   the analysis, and **rank** them by how far they move the answer.
3. **Prepare** answers for the questions whose swing exceeds the quoted uncertainty, and
   **state** plainly which questions require new data rather than a new calculation.
4. **Answer** a question you cannot answer, without either bluffing or conceding the
   result.
5. **Critique** a peer's capstone using the same rubric and the same question-impact
   method, separating what the analysis establishes from what it assumes.
6. **Write** a defence report recording what was asked, what was answered and what
   changed as a result.
7. **Recognise** the difference between a defence and a performance: the panel tests the
   analysis, not the candidate's composure.

## Prerequisites

- [25-06-04 Capstone: Manuscript-Style Write-Up and Code Release](./04-capstone-writeup.md) —
  the audited manuscript and release being defended.
- [22-01-02 Version Control with Git](../../22-data-engineering-reproducibility/01-research-software-engineering/02-version-control-git.md) —
  the commit history a panel may ask to see.
- [21-09-01 Reproducibility and Statistical Integrity](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/01-reproducibility-statistical.md) —
  the obligations that come with a claim.
- [25-05-05 Project: Reproducing a Published Result](../05-doctoral-projects/05-reproduce-published-result.md) —
  the same method-dependence reasoning, applied to your own result in a critique.

## 1. The question

*Which question would break your result, and what is your answer to it?*

The demonstration replaces rehearsal with arithmetic. Eight plausible viva questions are
each mapped to a re-computation of the analysis, and the swing of the answer is compared
with the quoted uncertainty of $2.00$ km:

| question | resulting claim | swing | in sd | verdict |
|---|---|---|---|---|
| $V_p/V_s$ is 1.70, not 1.75 | $37.45 \pm 2.22$ km | 2.46 | $1.23$ | prepare |
| $V_p/V_s$ is 1.80, not 1.75 | $32.85 \pm 1.82$ km | 2.16 | $1.08$ | prepare |
| $V_p$ is 5% lower | $33.47 \pm 1.94$ km | 1.53 | $0.77$ | on the fly |
| the picking error is 0.30 s | $35.00 \pm 2.90$ km | 0.90 | $0.45$ | on the fly |
| only 10 independent clusters | $35.00 \pm 3.02$ km | 1.02 | $0.51$ | on the fly |
| the ray parameter is off by 0.010 s/km | $34.42 \pm 1.97$ km | 0.58 | $0.29$ | on the fly |
| the systematic budget is doubled | $35.00 \pm 3.47$ km | 1.47 | $0.74$ | on the fly |
| the filter width changes $t$ by 0.05 s | $35.40 \pm 2.03$ km | 0.40 | $0.20$ | on the fly |

**Two of eight questions move the answer by more than one standard deviation, and every
one of them is answerable in milliseconds from the registry** — which is the whole
argument for the provenance discipline of
[25-06-03](./03-capstone-execution.md) and [25-06-04](./04-capstone-writeup.md). The
dangerous questions are not the technical ones; they are the ones about the assumptions,
and they are dangerous in a precisely measurable way.

## 2. What each question type tests

| question form | what it tests | how to answer |
|---|---|---|
| "What exactly did you measure?" | the claim | restate the headline with its budget and the assumption it depends on |
| "Why that value of $X$?" | the design decisions | the tested range and the swing it produces (the table above) |
| "How do you know the code is right?" | verification | the analytic check, the synthetic recovery, the coverage result |
| "What if the assumption is wrong?" | robustness | the recomputation, then the honest boundary: new data needed |
| "Why not method $Y$?" | awareness | the reason, and the paper that used $Y$ on this problem |
| "What is the uncertainty?" | discipline | the budget with its split, never a single number |
| "What did you *not* establish?" | scientific judgement | a specific list, not a disclaimer |
| "What next?" | the contribution | the measurement that would remove the dominant term |

A defence is a test of whether the candidate can distinguish these, and the commonest
failure is answering a question of the fourth kind with an answer of the first kind: the
panel asks what happens if $V_p/V_s$ is wrong, and hears the headline number repeated
with more confidence.

## 3. The presentation

A $20$-minute capstone talk has about $14$ content slides at $80$ seconds each. The
allocation that works:

| slides | content | the quantitative object |
|---|---|---|
| 1–2 | question and why it matters | the effect size and the decision rule of [25-06-01](./01-capstone-design.md) |
| 3–4 | data | the count, the noise estimate and the map |
| 5–8 | method | the forward model, the estimator, the verification result |
| 9–11 | results | the headline number, the budget, the sensitivity table |
| 12 | comparison with the literature | the published value in its own uncertainty units |
| 13 | limitations | the dominant assumption and what it would take to remove it |
| 14 | conclusion and next step | what is established and what is not |

Three rules:

1. **One claim per slide, in the title.** "Moho depth is $35.0 \pm 2.0$ km, dominated by
   the assumed $V_p/V_s$" is a title; "Results" is not.
2. **The verification slide is not optional.** It is the slide that distinguishes the
   talk from a plausibility argument, and it is the one the panel looks for.
3. **Rehearse to the minute** with a visible timer, three times, including the
   questions you plan to be asked. A capstone talk that overruns is judged on the
   overrun, whatever the content.

## 4. Answering what you cannot answer

Three categories, and the correct response to each:

1. **Answerable from the analysis (the table above).** Answer with the number:
   *"If $V_p/V_s$ were 1.70, the depth would be 37.5 km — the same depth formula,
   recomputed"*. Instant, specific, and it demonstrates the registry.
2. **Answerable only with new data.** Say so, and state the measurement and its cost:
   *"I cannot answer that from this dataset; a $V_p/V_s$ measured to $\pm 0.01$ at these
   stations would reduce the budget from 2.0 to about 1.5 km, and that is the next
   study."* This answer is stronger than a guess, because it shows the candidate knows
   where their result ends.
3. **Answerable only by conceding.** If the question identifies a genuine error — a wrong
   unit, a mis-cited value, a check that was not run — say so, state the effect, and
   state when it will be fixed. A panel that finds an error and receives an admission
   plus a plan for correction is testing rigour; a panel that finds an error and receives
   a defence of the indefensible is testing composure, and loses interest in the science.

**The one sentence never to say:** "that result is within the error bars". If the
question was about a systematic assumption, the error bars were computed *under* that
assumption, so the sentence is circular — and a numerically literate panel will say so.
The correct form is: *"that assumption contributes $X$ km to the budget; the quoted
interval is conditional on it."*

## 5. Peer critique

Critiquing a peer's capstone uses the same tools as defending your own:

1. **Restate their claim in one sentence** with its uncertainty, and check with them that
   the restatement is correct. Half of all critique disagreement ends here.
2. **Identify the dominant assumption** from their uncertainty budget, and ask what
   happens if it is wrong. Compare the swing with their quoted uncertainty, as in §1.
3. **Ask for the verification.** If there is none, the critique's main point is the
   missing verification, not the result.
4. **Separate the three judgements**: (i) is the analysis internally correct? (ii) is it
   adequate for the claim made? (iii) is the claim interesting? Confusing (i) with (iii)
   is the commonest failure in student peer review, in both directions.
5. **Write the critique as actions**: "report the budget with its split", "state the
   tested range of the filter width", "cite the comparison value's uncertainty type".
   An actionable critique is one whose recipient can answer it with a change.

The same discipline applies to the **defence report** the candidate writes afterwards:
what was asked, what was answered, what was conceded, what changed. It belongs in the
repository next to the audit, and it is the document that shows the work was defended
rather than merely submitted.

## 6. Failure modes

1. **Rehearsing the talk but not the questions.** The talk is 20 minutes; the questions
   are where the result is tested, and they can be prepared by computation.
2. **Repeating the headline instead of answering the question.** The panel hears
   confidence where it asked for a recomputation.
3. **"Within the error bars"** as an answer about a systematic assumption — circular,
   and detectable.
4. **A presentation with no verification slide**, so the result reads as a plausibility
   argument.
5. **Claiming a result the analysis cannot support** under questioning, which converts a
   limitation into a credibility problem.
6. **A critique that lists preferences rather than actions**, giving the recipient
   nothing to change.
7. **No defence report**, so the corrections requested by the panel are lost.

## 7. Rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Presentation | 20% | one claim per slide title, verification slide present, on time |
| Claim and uncertainty stated correctly | 15% | budget with its split, dominant assumption named |
| Question preparation | 25% | the impact table computed, the dangerous questions identified and answered with numbers |
| Honesty about limits | 20% | new-data questions stated as such, errors conceded with an effect and a plan |
| Peer critique | 20% | claim restated, dominant assumption tested, three judgements separated, actions listed |

## 8. The honest summary

The product of the defence is a candidate who can state the result with its budget, name
the assumption that dominates it ($47\%$ of the variance), compute the answer to eight
plausible challenges in milliseconds, and say plainly which questions require new data
rather than a new calculation. Of the eight questions analysed here, two move the answer
by more than one standard deviation — both of them about $V_p/V_s$ — and the largest
swing is $1.2$ sd, i.e. $+7\%$ in the depth. The transferable results are that a defence
is prepared by recomputation rather than by rehearsal, that the answer to a question
about a systematic assumption is a number and a boundary rather than a confidence
statement, and that the same method makes a peer critique specific enough to act on.

## Python demonstration

[`code/capstone_defence_demo.py`](./code/capstone_defence_demo.py) prints every number
above: the claim on the table, the question-by-question recomputation with swings and
verdicts, the three questions to prepare first, what the analysis cannot answer, and the
three numbers to know without notes.

```bash
cd 25-projects-capstone/06-capstone-research/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python capstone_defence_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, no network, no files, no
plots, exits 0, runs in about $0.1$ s.

## Exercises

Graded problems and worked solutions are in
[`exercises/05-capstone-defence-exercises.md`](./exercises/05-capstone-defence-exercises.md)
and
[`exercises/05-capstone-defence-solutions.md`](./exercises/05-capstone-defence-solutions.md).
The ★★★ item asks you to build the question-impact table for your own capstone and
write the two answers you would give to the most dangerous question.

## Mastery checkpoint

Without notes:

1. State the eight question forms and what each tests.
2. Given a swing of 2.46 km and a quoted uncertainty of 2.00 km, compute the swing in
   standard deviations and state the verdict rule.
3. Explain why "within the error bars" is a circular answer about a systematic
   assumption.
4. State the three categories of unanswerable question and the correct response to each.
5. List the five steps of a peer critique.

## Common pitfalls

1. Preparing the talk and not the questions.
2. Answering a robustness question with a restatement of the result.
3. Presenting a result without the verification slide.
4. Guessing at an answer that new data would be needed for.
5. A critique that separates preference from analysis nowhere and actions never.

## Where this is used

The defence closes the capstone module, and the *method* is the one used for every
subsequent peer review: in a journal referee report, a conference question session, or a
project review. The question-impact analysis is reusable — a version of it belongs in
the repository alongside the audit — and the defence report is the first entry in the
record of what the candidate's work has survived.

## Related lessons

- [25-06-04 Capstone: Manuscript-Style Write-Up and Code Release](./04-capstone-writeup.md) —
  the audited material being defended.
- [25-06-03 Capstone: Data, Modelling and Uncertainty Analysis](./03-capstone-execution.md) —
  the budget whose dominant term decides which questions are dangerous.
- [25-05-05 Project: Reproducing a Published Result](../05-doctoral-projects/05-reproduce-published-result.md) —
  the identical reasoning applied to someone else's result.
- [21-09-01 Reproducibility and Statistical Integrity](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/01-reproducibility-statistical.md) —
  the obligations a defended claim carries.

## Self-assessment checklist

- [ ] I can state my claim with its budget and its dominant assumption.
- [ ] I can compute the impact of any plausible question on my result.
- [ ] I can name the questions that move my answer by more than one standard deviation.
- [ ] I can say which questions require new data.
- [ ] I can answer without bluffing and without conceding the result.
- [ ] I can critique a peer's work in actions rather than preferences.
