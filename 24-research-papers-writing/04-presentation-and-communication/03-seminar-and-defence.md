---
id: 24-04-03
title: "Seminars, Qualifying Exams and Thesis Defence"
level: doctoral
prereqs: ["24-04-01", "24-03-01"]
estimated_minutes: 50
tags: [presentation, defence, examination, questioning, preparation]
---

# Seminars, Qualifying Exams and Thesis Defence

An examination is a talk followed by questions you cannot choose. The talk part is
covered by [24-04-01 Conference Talks](01-conference-talks.md); what distinguishes an
examination is that the **question space is bounded and knowable**, and that
preparation is therefore a coverage problem with a measurable curve. This lesson
treats it that way: which areas questions come from, how coverage grows with
preparation, how many questions fit in the time, and what risk remains.

The organising idea is that **preparation should be proportional to question weight,
not to comfort**. The areas you can already discuss fluently are, by construction,
the ones you have practised; the areas that carry the most questions are often the
ones where your reasoning is weakest, precisely because you have not had to defend
it.

> **Data provenance.** All numbers are **SYNTHETIC**. The question areas, their
> weights, the coverage curve, the timings and the simulated panel are chosen
> teaching values; no examination was observed or recorded.

## Learning objectives

By the end of this lesson you will be able to:

1. **Enumerate** the probable question areas for your work and **weight** them by
   how often each is likely to be asked.
2. **Compute** coverage as a function of the number of prepared answers, and
   **identify** the point of diminishing returns.
3. **Compute** how many questions fit in a defence and **state** the effect of
   answer length.
4. **Estimate** the residual risk from low-weight areas and **state** the minimum
   preparation that removes most of it.
5. **Structure** an answer as a three-part reply: direct answer, reason, limit.
6. **Handle** the three difficult question types — a wrong premise, a question
   outside your expertise, and a challenge to your method's validity.

## Prerequisites

- [24-04-01 Conference Talks: Structure, Pacing, Visuals](01-conference-talks.md) —
  the talk the examination follows.
- [24-03-01 Formulating Answerable Research Questions](../03-research-methods-and-rigour/01-research-questions.md) —
  the question the examination tests.

## 1. The question space

The demonstration models $60$ plausible questions across eight areas with chosen
weights:

| Area | Weight |
|---|---|
| Motivation and context | $10\%$ |
| Method choice | $18\%$ |
| Data and sampling | $15\%$ |
| Uncertainty and error | $14\%$ |
| Assumptions and limitations | $16\%$ |
| Alternatives and competitors | $11\%$ |
| Reproducibility and code | $8\%$ |
| Significance and implications | $8\%$ |

Method choice, assumptions and data sampling carry $49\%$ of the weight between
them. These are the areas where an examiner can ask *why* rather than *what*, and
they are also the areas where an unprepared candidate is most exposed, because a
"why" question cannot be answered from memory of the results.

The three highest-weight areas are worth writing explicit answers for. An explicit
answer is not a script: it is two sentences stating the choice, one sentence stating
the alternative, and one stating the consequence if the choice were wrong.

## 2. Coverage and its diminishing returns

Modelling coverage as $1 - e^{-n/12}$ for $n$ prepared answers:

| Prepared | Coverage |
|---|---|
| $4$ | $28.3\%$ |
| $8$ | $48.7\%$ |
| $12$ | $63.2\%$ |
| $16$ | $73.6\%$ |
| $20$ | $81.1\%$ |
| $24$ | $86.5\%$ |
| $32$ | $93.1\%$ |
| $48$ | $98.2\%$ |

Twenty-four prepared answers reach $86.5\%$ coverage; doubling the preparation to
$48$ adds $11.7$ percentage points. The shape is the argument: prepare the *first*
two answers in each area, because the tenth question about the same assumption
teaches almost nothing new. Breadth beats depth in preparation, even though depth
wins in the answers you give.

## 3. Timing

A $45$-minute defence with a $15$-minute talk leaves $30$ minutes of questions.
Answer length determines how many questions you can address:

| Answer length | Questions answered | Words spoken |
|---|---|---|
| $1.5\ \mathrm{min}$ | $20.0$ | $3900$ |
| $3.5\ \mathrm{min}$ | $8.6$ | $3900$ |
| $5.0\ \mathrm{min}$ | $6.0$ | $3900$ |

The word total is the same in every row — the thirty minutes are the thirty
minutes. What changes is the *number of questions*, i.e. how much of the examiners'
agenda is reached. Long answers are therefore not thoroughness; they are a way of
leaving questions unasked, which is not the same as answering them.

**The three-part answer** fits in about $90$ seconds:

1. **Direct answer**, first and in one sentence. "Yes, because the dispersion
   estimate uses the same stations for both arrays."
2. **Reason**, in two sentences, with the specific evidence.
3. **Limit**, in one sentence: what would change the answer. "If the station sets
   did not overlap, the comparison would not be paired and the uncertainty would
   roughly double."

The structure is visible to the panel, which is what makes an answer judgeable.

## 4. Residual risk

A simulated panel of eight questions drawn from the area weights illustrates the
tail:

- the lowest-weight areas (reproducibility and code, significance and
  implications, $8\%$ each) still receive questions in most defences;
- the probability that at least one of these two areas appears in an eight-question
  panel is $75.2\%$.

So a candidate who prepares only the high-weight areas faces roughly a three-in-four
chance of an unprepared question. The remedy is cheap: two prepared sentences per
low-weight area — "the code is archived at this location and reproduces the main
table to four digits"; "the implication for hazard assessment is bounded by the
catalogue completeness" — removes most of the exposure.

## 5. Three difficult question types

**1. A wrong premise.** "Given that your model assumes a flat Earth…" when it does
not. Do not answer the question as posed; correct the premise first, politely and
briefly: "The model is spherical; if it assumed flatness the phase shift would be
$3\%$ at this distance. With the spherical model the shift is $0.2\%$." Then answer
the question they probably meant.

**2. A question outside your expertise.** Separate what you know from what you do
not: "I have not computed that; the relevant paper is X, and my expectation is Y
because Z, but I would want to check before relying on it." Examiners can tell the
difference between a candidate who knows the limits of their work and one who
improvises confidently; the first is the stronger position.

**3. A challenge to validity.** Distinguish a challenge to *correctness* from a
challenge to *interpretation*. Answer correctness with a check: "I tested that by
re-running with a synthetic model where the answer is known, and the recovery was
within $2\%$." Answer interpretation with the scope: "The claim is about this depth
range only; outside it, I have no evidence."

## 6. Preparing the room

- **The five slides you will return to.** Under questioning, a prepared slide
  returns the discussion to evidence; have a map of where each figure is.
- **The one-page summary.** A handout with the claim, the design, the primary
  number and the limitations; useful when the panel asks you to state your
  contribution.
- **The list of what you did not do.** Being the first to name the limitations
  converts a probable question into evidence of judgement.
- **A rehearsal with an unfriendly audience.** Colleagues instructed to interrupt
  and to ask "why" three times train the skill that the examination actually tests.

## Assumptions and regime of validity

1. **The weights are chosen.** They describe a plausible geophysics examination, not
   any particular committee; a candidate should revise the weights from their own
   committee's publications and known interests.
2. **Coverage is modelled, not measured.** The exponential form captures
   diminishing returns; the rate constant is arbitrary.
3. **Answer length is not purely under your control.** Some questions genuinely
   require four minutes; the point is the average, and the panel's agenda.
4. **Examiners are not adversaries.** Most questions are attempts to understand the
   work; treating the panel as hostile wastes the exchange.
5. **A defence is not a viva for the field.** The examination tests the thesis and
   the candidate's reasoning about it, not the whole of geophysics.

## The honest summary

The question space is bounded and weighted, and preparation has a measurable
coverage curve: $24$ answers reach $86.5\%$, and doubling them adds $11.7$ points.
Thirty minutes of questioning yields $20$ short answers or $6$ long ones, and the
low-weight areas still appear in three defences out of four. Prepare by area, answer
in three parts, and name the limitations before the panel does.

## Python demonstration

[`code/seminar_and_defence_demo.py`](./code/seminar_and_defence_demo.py) prints four
labelled sections: the weighted question areas; the coverage curve; the timing of
questions by answer length; and a simulated panel with the residual risk from
low-weight areas.

```bash
cd 24-research-papers-writing/04-presentation-and-communication/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seminar_and_defence_demo.py
```

## Exercises

Problems are in
[`exercises/03-seminar-and-defence-exercises.md`](./exercises/03-seminar-and-defence-exercises.md),
worked answers in
[`exercises/03-seminar-and-defence-solutions.md`](./exercises/03-seminar-and-defence-solutions.md).

## Mastery checkpoint

1. Write your eight question areas with weights derived from your committee.
2. Write two prepared answers per area and count them.
3. Time yourself answering three questions; compute your question count.
4. Write the three-part answer for your method choice.
5. Ask a colleague to challenge your primary result for ten minutes and write down
   every question you could not answer; prepare an answer for each.

## Common pitfalls

1. **Preparing only what you can already discuss.** The weights, not the comfort,
   decide.
2. **Answering a question you wish had been asked.** The panel notices.
3. **Four-minute answers.** They leave questions unasked rather than answered.
4. **Improvising outside your expertise.** Naming the limit is the stronger answer.
5. **Not naming your own limitations.** The panel will, and it will count against a
   candidate who did not.
6. **Rehearsing only with friendly colleagues.** The skill being tested is answering
   an interruption.

## Where this is used

- **Qualifying and comprehensive exams:** the coverage curve is the syllabus
  priority list.
- **Thesis defence:** the areas correspond to the chapters and the discussion.
- **Job talks and interviews:** the same question areas with more emphasis on
  future plans and fundability; see
  [24-05-04 Academic CVs, Research Statements and Career Paths](../05-thesis-and-proposals/04-cv-and-career.md).
- **Group seminars:** an interruption-rich question session is training for all of
  the above.

## Related lessons

- [24-04-01 Conference Talks: Structure, Pacing, Visuals](01-conference-talks.md) —
  the talk that opens the examination.
- [24-03-05 Peer Review: How to Do It Well and Receive It Well](../03-research-methods-and-rigour/05-peer-review-practice.md) —
  the same skills in the reviewer's role.
- [24-05-02 Thesis Structure, Chapters and the Contribution Statement](../05-thesis-and-proposals/02-thesis-structure.md) —
  the document being examined.
- [24-05-04 Academic CVs, Research Statements and Career Paths](../05-thesis-and-proposals/04-cv-and-career.md) —
  where the examination leads.

## Self-assessment checklist

- [ ] I can list and weight my probable question areas.
- [ ] I can compute coverage for a preparation set and find its knee.
- [ ] I can compute my question count from my answer length.
- [ ] I can give a three-part answer in ninety seconds.
- [ ] I can handle a wrong premise, an unknown area and a validity challenge.
- [ ] I have named my own limitations before the panel does.
