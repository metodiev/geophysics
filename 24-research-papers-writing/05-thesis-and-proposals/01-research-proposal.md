---
id: 24-05-01
title: "Writing a Compelling Research Proposal"
level: doctoral
prereqs: ["24-03-01", "24-03-03"]
estimated_minutes: 60
tags: [research, proposals, writing, scoring, funding, planning]
---

# Writing a Compelling Research Proposal

A proposal is a promise evaluated by a scoring scheme you can usually find in
advance. That makes it a different genre from a paper: the deliverable is a plan,
the evidence is a design and a track record, and the decision is made by comparing
weighted scores measured against a budget line. This lesson works the arithmetic of
that comparison — the weights, the margin at the cutoff, and the sensitivity of the
decision to the scheme.

The organising idea is that **the weighting is part of the specification**. Two
panels reading the same proposals with different weights fund different sets, and
the difference is concentrated exactly at the boundary: in the demonstration the
ranking correlation between the two schemes is $0.9957$, yet $20\%$ of the funded set
changes. A proposal is therefore not optimised in the abstract; it is optimised for a
stated rubric.

> **Data provenance.** All numbers are **SYNTHETIC**. Proposals, criterion scores and
> the two weighting schemes are generated with chosen parameters; no real proposal,
> panel or funding scheme is analysed. The criterion names are generic.

## Learning objectives

By the end of this lesson you will be able to:

1. **Identify** the scoring scheme of a target call and **state** the weights it
   applies to each criterion.
2. **Compute** a weighted score and **rank** proposals under two schemes, reporting
   the proposals whose status flips.
3. **Measure** the margin at the funding line and **compare** it with the typical
   shift produced by a change of scheme.
4. **Compute** the marginal value of one point on each criterion and **allocate**
   effort accordingly.
5. **Structure** a proposal as claim, gap, plan, feasibility, and evaluation, with
   each move aimed at a named criterion.
6. **State** what a proposal cannot do: it cannot make an unanswerable question
   fundable, nor substitute for a track record.

## Prerequisites

- [24-03-01 Formulating Answerable Research Questions](../03-research-methods-and-rigour/01-research-questions.md) —
  the question the proposal promises to answer.
- [24-03-03 Designing Observational, Experimental and Modelling Studies](../03-research-methods-and-rigour/03-study-design.md) —
  the design that makes the promise credible.

## 1. The scoring scheme is a specification

A typical scheme gives weighted criteria. The demonstration uses two plausible
schemes on the same five criteria:

| Criterion | Science-led | Impact-led |
|---|---|---|
| Novelty | $0.25$ | $0.15$ |
| Feasibility | $0.25$ | $0.20$ |
| Methods | $0.20$ | $0.20$ |
| Impact | $0.20$ | $0.35$ |
| Team | $0.10$ | $0.10$ |

The weighted score is

$$S = \sum_{k} w_k s_k, \qquad \sum_k w_k = 1,$$

with criterion scores $s_k$ on a stated scale (here $1$–$5$). The first task when
approaching a call is therefore not writing but reading: find the weights, the
scale, the review form and any published scoring guidance.

## 2. Ranking under two schemes

With $40$ synthetic proposals scored on five criteria, the top $25\%$ (a funding
line at $10$ proposals) gives:

| Quantity | Value |
|---|---|
| Proposals funded under both schemes | $9$ of $10$ |
| Proposals whose funded status flips | $2$ |
| Spearman rank correlation between schemes | $0.9957$ |

Two proposals change side. That is the characteristic pattern: near-perfect rank
agreement overall, with the disagreement concentrated at the boundary where it
matters. The practical consequence is that the most valuable thing a proposal can do
is clear the boundary by more than the scheme's uncertainty — not top the ranking.

## 3. The margin at the line

The demonstration's scores around the cutoff:

| Rank | Score |
|---|---|
| $9$ | $3.8590$ |
| $10$ | $3.8088$ (last funded) |
| $11$ | $3.7941$ |
| $12$ | $3.7832$ |

$$\text{margin} = 3.8088 - 3.7941 = 0.0147\ \text{points on a 5-point scale}
= 0.29\%\ \text{of the range}.$$

The typical score shift between the two weighting schemes is $0.0765$ points, so

$$\frac{\text{shift}}{\text{margin}} = \frac{0.0765}{0.0147} = 5.19 .$$

**When the shift exceeds the margin, the decision is set by the scheme rather than
by the proposals.** That single inequality explains a familiar experience: a proposal
rejected by one panel can be funded by another without a word changed. It is not
irrational; it is what a $5\!:\!1$ ratio between scheme-shift and margin predicts.

The corollary is the drafting target: aim to be more than one scheme-shift above the
anticipated line. In this corpus that means being a clear rank above the boundary
rather than a coin-flip among the near-ties.

## 4. Marginal value of a point

One point of improvement on a single criterion is worth its weight:

| Criterion | Weight | Score gain per $+1$ point |
|---|---|---|
| Novelty | $0.25$ | $0.25$ |
| Feasibility | $0.25$ | $0.25$ |
| Methods | $0.20$ | $0.20$ |
| Impact | $0.20$ | $0.20$ |
| Team | $0.10$ | $0.10$ |

The ratio between the most and least valuable criterion is $2.5$. A week spent
strengthening the feasibility argument (weight $0.25$ under the science-led scheme)
buys $2.5$ times what the same week spent improving team presentation buys. Under the
impact-led scheme the ordering changes: impact at $0.35$ becomes the most valuable
criterion by a wide margin. **Read the weights before allocating the weeks.**

## 5. Five moves, aimed at named criteria

1. **Claim** — the result you will deliver, with its scope and its uncertainty
   target. Aimed at novelty.
2. **Gap** — what is not known, evidenced by citations rather than assertion. Aimed
   at novelty and impact.
3. **Plan** — work packages with deliverables, dependencies and a timeline. Aimed at
   methods and feasibility.
4. **Feasibility** — method precedent, team roles, data access, contingency for the
   two most likely failures. Aimed at feasibility and team.
5. **Evaluation** — what would count as failure, and how you would know. Aimed at
   methods and impact.

A proposal that does not name the failure modes reads as optimism; one that names
them and states the contingency reads as planning. The distinction is measurable in
the feasibility score, which is why it is worth a paragraph.

## 6. Writing to the review form

The review form is the finished artefact's reader. Practices that follow from it:

- **Use the criteria as headings** where the form allows, so a reviewer scoring
  "methods" finds the material without searching.
- **State the numbers**: the number of sites, the effect size to be detected, the
  sample size and the power. A reviewer scoring feasibility can then check the
  arithmetic.
- **Quantify the deliverables**: datasets, papers, code, trained people, with a
  stated completion criterion.
- **Answer the likely objection in the text**, in the section where it arises.

## Assumptions and regime of validity

1. **The corpus and weights are synthetic.** Real schemes differ in criteria, scales,
   thresholds and interview stages; the transferable content is the arithmetic of
   weights, margins and shifts.
2. **Scores are independent across criteria.** In practice a strong proposal scores
   well on several, and reviewers anchor; the independence assumption makes the
   marginal-value table clean, not realistic.
3. **The funding line is a ranking cutoff.** Real panels use bands, discuss near-ties
   and consider portfolio balance, so the boundary is softer than a cutoff — which
   usually *increases* the influence of the scheme.
4. **Writing quality is not scored.** It influences every score through comprehension;
   that path is not modelled.
5. **A good score is not a good project.** The scheme measures what the funder wants
   to know, not what the science will deliver.

## The honest summary

The weights are the specification, the margin at the line is $0.29\%$ of the scale in
the demonstration, and a change of scheme shifts scores by five times that margin.
Under science-led weights a point on feasibility is worth $2.5$ points on team; under
impact-led weights a point on impact is worth more than either. Write to the rubric,
clear the line by more than a scheme shift, and name your failure modes.

## Python demonstration

[`code/research_proposal_demo.py`](./code/research_proposal_demo.py) prints four
labelled sections: the criterion scores; the ranking under two weighting schemes with
the flips; the margin at the funding line against the scheme shift; and the marginal
value of a point on each criterion.

```bash
cd 24-research-papers-writing/05-thesis-and-proposals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python research_proposal_demo.py
```

## Exercises

Problems are in
[`exercises/01-research-proposal-exercises.md`](./exercises/01-research-proposal-exercises.md),
worked answers in
[`exercises/01-research-proposal-solutions.md`](./exercises/01-research-proposal-solutions.md).

## Mastery checkpoint

1. Find the scoring scheme for a call you intend to answer and tabulate its weights.
2. Compute the weighted score of your current draft under that scheme, and under a
   plausible alternative.
3. Estimate the margin at the anticipated funding line from the call's own data.
4. Allocate your remaining preparation time by marginal value.
5. Write the paragraph that names your two most likely failure modes and the
   contingency for each.

## Common pitfalls

1. **Writing before reading the scheme.** The weights decide what a week is worth.
2. **Optimising the total instead of clearing the line.** A clear rank above the
   boundary is worth more than a marginal top score.
3. **Claiming feasibility without precedent.** Method precedent and data access are
   what a reviewer checks.
4. **No failure modes.** Their absence reads as naivety, not confidence.
5. **Ignoring the panel's portfolio.** Panels fund coherent portfolios, so a proposal
   that duplicates the department's existing strengths may lose on fit.
6. **Assuming the scheme is stable.** It changes between calls; reuse last year's
   weighting at your own risk.

## Where this is used

- **Grant and fellowship applications:** the same arithmetic applies with different
  scales; see [03 Understanding Grant Funding and Review Criteria](03-grant-funding.md).
- **Thesis proposals and qualifying exams:** the criteria are the committee's
  questions; see
  [24-04-03 Seminars, Qualifying Exams and Thesis Defence](../04-presentation-and-communication/03-seminar-and-defence.md).
- **Internal project approvals:** a small scheme with named weights is the fastest
  route to a decision.
- **Job applications:** the research statement is a proposal with a shorter horizon;
  see [04 Academic CVs, Research Statements and Career Paths](04-cv-and-career.md).

## Related lessons

- [24-05-02 Thesis Structure, Chapters and the Contribution Statement](02-thesis-structure.md) —
  the document the proposal becomes.
- [24-03-03 Designing Observational, Experimental and Modelling Studies](../03-research-methods-and-rigour/03-study-design.md) —
  the design the feasibility section reports.
- [24-03-01 Formulating Answerable Research Questions](../03-research-methods-and-rigour/01-research-questions.md) —
  the claim the proposal promises.
- [24-02-02 Paper Structure: IMRaD and Its Variants](../02-scientific-writing/02-paper-structure.md) —
  the argument structure borrowed here.

## Self-assessment checklist

- [ ] I can tabulate the weights of a target scheme.
- [ ] I can compute weighted scores and identify the flips between schemes.
- [ ] I can measure the margin at the funding line.
- [ ] I can compute the marginal value of a point on each criterion.
- [ ] I can write the five moves aimed at named criteria.
- [ ] I can state the two most likely failure modes and my contingencies.
