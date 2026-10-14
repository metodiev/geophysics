---
id: 24-03-01
title: "Formulating Answerable Research Questions"
level: advanced
prereqs: ["24-01-02", "24-01-03"]
estimated_minutes: 50
tags: [research, questions, design, specificity, proposals]
---

# Formulating Answerable Research Questions

A research question is answerable when a reader can tell what would count as an
answer, over what region and time span, and compared with what. Everything else
is a research area. This lesson treats specificity as a measurable property: it
counts the elements a question states, estimates how many distinct studies a
vague question is consistent with, and puts a cost on the ambiguity.

The organising idea is **the mapping from a sentence to a study**. A specific
question maps to few studies; a vague question maps to many, and each unmade
decision becomes a choice someone will make later, often after data have been
collected. Writing the question is therefore the cheapest moment to make those
choices, and the measure of a good question is how much of the design it already
fixes.

> **Data provenance.** All numbers are **SYNTHETIC**. Questions are represented as
> four binary content elements with chosen probabilities, and the candidate-design
> model is a chosen teaching rule ($2^{k}$ designs for $k$ missing elements). No
> real research question or proposal was analysed.

## Learning objectives

By the end of this lesson you will be able to:

1. **Name** the four elements of an answerable question and **identify** which are
   missing from a given sentence.
2. **Compute** the number of candidate studies a question is consistent with under
   a stated model of missing elements.
3. **Measure** two-rater agreement on a "falsifiable" judgement using Cohen's
   $\kappa$, and **state** what a given $\kappa$ licenses.
4. **Place** a cost on ambiguity by converting unresolved elements into effort, and
   **justify** the cost model you used.
5. **Rewrite** a topic into a question with quantity, comparison and scope, and
   **state** the design it implies.
6. **Explain** why a mechanism element is not required for answerability.

## Prerequisites

- [24-01-02 Reading Strategies: Skim, Map, Deep-Read, Critique](../01-reading-research-literature/02-reading-strategies.md) —
  how a reader discovers what a paper actually asked.
- [24-01-03 Critiquing Methods, Data and Inference](../01-reading-research-literature/03-critiquing-methods.md) —
  the axes a question must eventually satisfy.

## 1. The four elements

| Element | Question it answers | Example clause |
|---|---|---|
| Measurable quantity | What will be measured? | "the shear-wave velocity profile" |
| Comparison or reference | Compared with what? | "against the borehole log" |
| Stated scope | Where and when? | "0–30 m depth, across the 2020 array" |
| Mechanism or reason | Why would it be so? | "because of weathering" |

The first three are **required for answerability**. The fourth is a hypothesis:
useful for framing and useless as a precondition, because a result that shows an
unexpected pattern is still a result. A question that states only its mechanism
("why is the basin so deep?") is a topic with an adverb.

## 2. Measured specificity of a synthetic corpus

The demonstration models $400$ question phrasings with chosen element rates:

| Element | Chosen | Measured |
|---|---|---|
| measurable quantity | $82.0\%$ | $83.8\%$ |
| comparison or reference | $61.0\%$ | $61.3\%$ |
| stated scope | $55.0\%$ | $53.0\%$ |
| mechanism or reason | $44.0\%$ | $44.5\%$ |

The mean number of elements present is $2.42 \pm 0.94$ of $4$, and only $107$ of
$400$ ($26.8\%$) state quantity, comparison and scope together. So roughly three
questions in four are missing at least one required element.

## 3. What a missing element costs

Under the chosen model — each missing element can be resolved in two directions
that change the design — a question missing $k$ elements is consistent with
$2^{k}$ candidate studies:

| Missing elements | Questions | Mean candidate designs |
|---|---|---|
| $0$ | $54$ | $1.0$ |
| $1$ | $128$ | $2.0$ |
| $2$ | $159$ | $4.0$ |
| $3$ | $52$ | $8.0$ |
| $4$ | $7$ | $16.0$ |

The corpus mean is $3.7$ candidate designs, with a median of $4$ and a maximum of
$16$. The model is a teaching device, not a law: its point is that vagueness
multiplies interpretations rather than merely being imprecise.

**Placing a cost on it.** At a modelled cost of $14$ days to resolve one candidate
design, the expected false-start effort per question is

$$(3.7 - 1) \times 14 = 37.6\ \text{days}.$$

The number is illustrative; the structure is the argument. Each extra clause in the
question removes a factor of two from the interpretations, and every unremoved
interpretation becomes someone's work later.

## 4. Judging answerability: agreement between readers

Two readers rating the same questions as "falsifiable" or "not" agree more than
chance but not perfectly. The demonstration's raters, with sensitivities of
$0.88$ and $0.85$ and specificities of $0.85$ and $0.88$ against the truth:

$$\mathbb{P}_o = 0.7600, \qquad \mathbb{P}_e = 0.5648, \qquad
\kappa = \frac{\mathbb{P}_o - \mathbb{P}_e}{1 - \mathbb{P}_e} = 0.4485 .$$

For comparison, each rater against the truth scores $\kappa = 0.6854$: the raters
are closer to the truth than to each other, which is what happens when both are
mostly right but disagree on the same ambiguous cases.

**Why this matters for a proposal.** A reviewer rating the same question uses
their own thresholds, so a question whose answerability is arguable will be judged
partly at random. A coding protocol with worked examples — five questions labelled
answerable and five not, with the reason — is what raises $\kappa$, and it is the
cheapest fix available.

## 5. Rewriting a topic into a question

Take a topic: *crustal structure in the basin*. Rewrite in four steps:

1. **Quantity.** "…the shear-wave velocity profile…"
2. **Comparison.** "…compared with the borehole measurements at four sites…"
3. **Scope.** "…in the upper $30\ \mathrm{m}$, for the 2019–2021 array…"
4. **Falsification.** "…and would be refuted by a systematic $20\%$ offset that
   persists across all four sites."

The result is one sentence that names its own refutation. Note that the mechanism
does not appear, and its absence does not weaken the question: the mechanism is a
hypothesis the study may or may not support.

**A checklist before the question leaves your desk:**

- Does it name a quantity with a unit?
- Does it name the comparison or the reference standard?
- Does it state the spatial and temporal scope?
- Does it state what observation would refute the answer?
- Can a reader name the design from the sentence alone?

## Assumptions and regime of validity

1. **The corpus is synthetic.** Element probabilities are chosen teaching values,
   not measurements of real proposals.
2. **The $2^{k}$ model is a teaching rule.** Real ambiguity is not binary per
   element, and some missing elements do not change the design.
3. **The cost per unresolved design ($14$ days) is illustrative.** The transferable
   point is that ambiguity has a cost proportional to the number of live
   interpretations.
4. **$\kappa$ depends on prevalence.** With a very high or very low base rate of
   answerable questions, $\kappa$ falls even at constant accuracy; report prevalence
   alongside it.
5. **A specific question can still be unanswerable.** Specificity is necessary and
   not sufficient: the data must also be able to bear on it.

## The honest summary

Three questions in four in the synthetic corpus omit at least one required element,
and the mean number of studies a question could be describing is $3.7$. Specificity
is cheap to add and it is the only ambiguity in a project that can be removed for
free, at the writing stage, before any data exist. Two readers agreeing at
$\kappa = 0.45$ is the quantitative warning that the judgement is not self-evident
and needs a protocol.

## Python demonstration

[`code/research_questions_demo.py`](./code/research_questions_demo.py) prints four
labelled sections: the element rates; the candidate-design distribution; the
two-rater agreement with $\kappa$; and the false-start cost arising from ambiguity.

```bash
cd 24-research-papers-writing/03-research-methods-and-rigour/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python research_questions_demo.py
```

## Exercises

Problems are in
[`exercises/01-research-questions-exercises.md`](./exercises/01-research-questions-exercises.md),
worked answers in
[`exercises/01-research-questions-solutions.md`](./exercises/01-research-questions-solutions.md).

## Mastery checkpoint

1. Write your current research question in one sentence.
2. Mark the four elements and compute the number of candidate designs under the
   model of §3.
3. Add the missing required clauses.
4. State the design the sentence now implies, and the observation that would refute
   the answer.
5. Give the question to a colleague and record their verdict and yours; after five
   questions, compute the raw agreement.

## Common pitfalls

1. **A topic masquerading as a question.** "Subsidence in the delta" names an area,
   not a question.
2. **Mechanism instead of quantity.** "Why is the basin deep?" cannot be answered
   without first measuring something.
3. **Scope creep in the middle of the project.** An unstated scope is decided later,
   usually by what the data permit.
4. **No comparison.** Without a reference, a measurement has no interpretation.
5. **No falsification clause.** If nothing could refute the answer, the question is
   not empirical.
6. **Over-specifying.** A question with six clauses and a named method is a
   protocol; the question should leave the method free.

## Where this is used

- **Proposals and thesis plans:** the question is the first thing a panel reads and
  the first thing it can object to; see
  [24-05-01 Writing a Compelling Research Proposal](../05-thesis-and-proposals/01-research-proposal.md).
- **Study design:** the design follows from the question's elements; see
  [03 Designing Observational, Experimental and Modelling Studies](03-study-design.md).
- **Pre-registration:** the falsification clause becomes the analysis plan.
- **Reviewing:** "what would count as an answer?" is the fastest useful question a
  reviewer can ask; see [05 Peer Review Practice](05-peer-review-practice.md).

## Related lessons

- [24-03-02 Hypotheses, Falsifiability and Testing in Earth Science](02-hypothesis-and-falsifiability.md) —
  the next step: turning the question into testable hypotheses.
- [24-03-03 Designing Observational, Experimental and Modelling Studies](03-study-design.md) —
  the design the question implies.
- [24-05-01 Writing a Compelling Research Proposal](../05-thesis-and-proposals/01-research-proposal.md) —
  where questions are graded.
- [21-08-01 Experimental Design](../../21-statistics-bayesian-ml/08-causal-inference-and-design/01-experimental-design.md) —
  the statistical view of what a design must fix in advance.

## Self-assessment checklist

- [ ] I can name the four elements and mark them in a sentence.
- [ ] I can compute candidate designs for a question.
- [ ] I can compute and interpret $\kappa$ for two raters.
- [ ] I can convert ambiguity into an effort estimate and defend the model.
- [ ] I can rewrite a topic into a question with a falsification clause.
- [ ] I can say why mechanism is not required.
