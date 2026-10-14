---
id: 24-05-04
title: "Academic CVs, Research Statements and Career Paths"
level: advanced
prereqs: ["24-05-01", "24-04-01"]
estimated_minutes: 50
tags: [career, cv, h-index, bibliometrics, research-statement, hiring]
---

# Academic CVs, Research Statements and Career Paths

A CV is a compressed argument about what you will do next, and the numbers on it —
publications, citations, an h-index — are summaries of a highly unequal distribution.
This lesson computes what those summaries do and do not capture, then treats the
hiring rubric the way the proposal lesson treats a funding scheme: as a weighting
that determines what a week of preparation is worth.

The organising principle is **report a distribution, not a number**. A citation record
in the demonstration has a mean of $2.18$ times its median and a Gini coefficient of
$0.562$; on such a distribution an h-index of $24$ is unchanged by adding $100$
citations to the most-cited paper and unchanged by adding sixty lightly cited papers.
A CV that reports only $h$ tells the reader almost nothing about which of those records
it is.

> **Data provenance.** All numbers are **SYNTHETIC**. Citation counts are generated
> from a chosen distribution; no bibliometric database was queried, and no real
> person's record is used. The rubric weights are chosen teaching values; hiring
> practices vary widely.

## Learning objectives

By the end of this lesson you will be able to:

1. **Summarise** a publication record with a distribution, not a single index: mean,
   median, top-decile share and Gini.
2. **Demonstrate** the h-index's insensitivity to a highly cited paper and to volume.
3. **Compute** how a bibliometric index grows with career length and **explain** why
   comparisons must be within cohorts.
4. **Rank** candidates under two rubrics and **compute** how many change position.
5. **Write** a research statement as a proposal with a short horizon, aligned to a
   department's stated priorities.
6. **State** what a CV cannot establish about a candidate and what a hiring process
   uses instead.

## Prerequisites

- [24-05-01 Writing a Compelling Research Proposal](01-research-proposal.md) — the
  rubric arithmetic reused here.
- [24-04-01 Conference Talks: Structure, Pacing, Visuals](../04-presentation-and-communication/01-conference-talks.md) —
  the job talk that accompanies the documents.

## 1. The citation distribution

The demonstration's synthetic record of $60$ papers:

| Quantity | Value |
|---|---|
| Total citations | $2030$ |
| Mean per paper | $33.8$ |
| Median per paper | $16$ |
| Ratio mean/median | $2.18$ |
| Top $10\%$ of papers ($6$) share | $35.3\%$ |
| Gini coefficient | $0.562$ |

The mean is more than twice the median, and a sixth of the papers hold a third of the
citations. The practical presentation follows: **list the papers, not the summary.**
A reader who sees the five most-cited works and their venues learns what the record
contains; a reader who sees "mean citations per paper: 34" learns a statistic that
could describe many records, including one with no heavily cited work at all.

## 2. What the h-index is insensitive to

Starting from $h = 24$:

| Perturbation | New $h$ |
|---|---|
| $+100$ citations to the most-cited paper | $24$ (unchanged) |
| $+60$ papers with $5$ citations each | $24$ (unchanged) |
| Every paper duplicated | $38$ |

The h-index is the largest $h$ such that $h$ papers have at least $h$ citations. It is
therefore a **floor in the middle of the distribution**: it ignores the peak entirely
and it ignores low-citation volume. The duplication row shows the arithmetic of a
different problem — counting the same work twice raises $h$ from $24$ to $38$ without
any new contribution — which is why any evaluation of a record should be based on a
deduplicated list of distinct works.

The honest use of $h$ is as one descriptive number among several, reported alongside
the median and the top-decile share, and never as a comparison across career stages.

## 3. Career length

| Years | Papers | $h$ | $h/\sqrt{\text{papers}}$ | Total citations |
|---|---|---|---|---|
| $5$ | $15$ | $9$ | $2.32$ | $268$ |
| $10$ | $30$ | $13$ | $2.37$ | $913$ |
| $15$ | $45$ | $17$ | $2.53$ | $1091$ |
| $20$ | $60$ | $26$ | $3.36$ | $2519$ |
| $25$ | $75$ | $30$ | $3.46$ | $3657$ |

At a constant publication rate of $3$ papers per year, $h$ grows roughly as the square
root of the number of papers, so it grows sublinearly in time. The consequence is
direct: **comparing an h-index across career stages compares exposure time.** Either
divide by years, or compare within a cohort, or — better — describe the trajectory:
"$h = 13$ at ten years, with four papers above $100$ citations" is a stronger
description than a bare number.

## 4. The hiring rubric is also a weighting

The demonstration applies two rubrics to the same $12$ synthetic candidates:

| Criterion | Default | Teaching-weighted |
|---|---|---|
| Publications | $0.30$ | $0.20$ |
| Funding | $0.20$ | $0.15$ |
| Teaching | $0.20$ | $0.35$ |
| Service | $0.10$ | $0.10$ |
| Fit | $0.20$ | $0.20$ |

Under the two rubrics, $7$ of $12$ candidates change rank, and one candidate's position
among the top five changes. As with proposals, the ranking correlation is high and the
disagreement is concentrated near the decision boundary — here, the top five.

**What to do with this.** A candidate cannot change a department's rubric, but can:

1. **Read it.** Hiring advertisements and departmental review criteria usually state
   the weights; a research statement should name them.
2. **Prepare evidence per criterion.** A teaching portfolio, a funding record, a
   service list: each is a criterion with a weight, and unspecified evidence scores as
   absent.
3. **Emphasise trajectory, not totals.** A five-year plan with two concrete deliverables
   reads as fit; a list of past achievements reads as history.

## 5. The research statement

A research statement is a proposal with a two-to-five-year horizon. Five moves:

1. **What I have done**, in two sentences, with the one result that identifies you.
2. **The question I will answer next**, with the gap and the design.
3. **What I will need**, named concretely: equipment, data, collaborators, students.
4. **What the department gains**, mapped to its stated priorities and its existing
   strengths — the "fit" criterion, which is usually weighted.
5. **The five-year trajectory**, with two verifiable deliverables.

The common failure is proportionality: three pages of past work and one paragraph of
future plans, when the committee is hiring the future. A useful test is to count the
words: the future should have at least as many as the past.

## 6. What a CV cannot establish

A CV is a record of outputs, not of capacity. It cannot establish:

- **judgement** — which problems are worth attacking;
- **collaboration** — whether people work with you again;
- **teaching ability** — a list of courses is not a classroom;
- **fit** — whether you will thrive in this department.

Hiring processes therefore rely on other evidence: the job talk and its questions (see
[24-04-03 Seminars, Qualifying Exams and Thesis Defence](../04-presentation-and-communication/03-seminar-and-defence.md)),
references with specific rather than general statements, teaching demonstrations, and
the informal conversations that a visit makes possible. For a candidate, the implication
is that the documents get you considered and the interactions get you hired: prepare
both.

## Assumptions and regime of validity

1. **The citation distribution is chosen.** Its parameters produce the inequality
   described; real distributions vary by field, and some fields cite far more heavily
   than others, so cross-field comparison of any citation metric is invalid.
2. **The h-index arithmetic is exact for the given counts.** The insensitivity
   demonstrated is a property of the definition, not of the parameters.
3. **The rubrics are invented.** Real hiring criteria are negotiated, weighted
   differently by institution type, and often include criteria not listed here.
4. **Synthetic candidates are exchangeable.** Real candidates differ in ways the
   model does not represent, and committees see documents, not scores.
5. **Bibliometrics describe attention, not quality.** A citation is a social act with
   many motivations; the underlying literature on this is extensive and should be
   consulted before any metric is used evaluatively.

## The honest summary

Citations are unequal: the mean is $2.18$ times the median and the Gini is $0.562$. The
h-index ignores the peak and low-citation volume, and grows sublinearly with career
length, so it must not be compared across stages. A hiring rubric is a weighting that
moves $7$ of $12$ candidates when it changes. Report distributions, prepare evidence
per criterion, and spend your preparation where the weight is.

## Python demonstration

[`code/cv_and_career_demo.py`](./code/cv_and_career_demo.py) prints four labelled
sections: the citation distribution and its inequality; the h-index insensitivity
demonstrations; the growth of metrics with career length; and the sensitivity of a
hiring ranking to rubric weights.

```bash
cd /Users/miroslav/Documents/workspace/geophysics/24-research-papers-writing/05-thesis-and-proposals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cv_and_career_demo.py
```

## Exercises

Problems are in
[`exercises/04-cv-and-career-exercises.md`](./exercises/04-cv-and-career-exercises.md),
worked answers in
[`exercises/04-cv-and-career-solutions.md`](./exercises/04-cv-and-career-solutions.md).

## Mastery checkpoint

1. List your five most-cited works and compute the share of your total citations they
   hold.
2. Compute your median and mean citations per paper; state the ratio.
3. Compute your $h$-index by hand and check it against the definition.
4. Find the weights of a department you would like to join and map your evidence to
   each.
5. Rewrite your research statement so that the future has at least as many words as
   the past.

## Common pitfalls

1. **Leading with an index.** It ignores exactly the work that identifies you.
2. **Comparing across fields or stages.** Citation practices differ by an order of
   magnitude between subfields.
3. **Counting the same work twice.** Duplication raises $h$ and is a problem, both
   bibliometrically and ethically; see
   [24-03-06 Research Ethics, Plagiarism, Authorship and Integrity](../03-research-methods-and-rigour/06-research-ethics.md).
4. **Ignoring the rubric.** Evidence that is not presented per criterion scores as
   absent.
5. **A research statement that is mostly retrospective.** The committee is hiring the
   future.
6. **Treating the documents as the whole application.** The talk, the references and
   the visit carry the judgement and fit criteria.

## Where this is used

- **Job and fellowship applications:** the CV, the research statement and the rubric
  arithmetic.
- **Annual reviews and promotion:** the same criteria are weighted, usually explicitly,
  in institutional processes.
- **Mentoring:** the distributional view of a record prevents both over- and
  under-confidence; see
  [24-05-03 Understanding Grant Funding and Review Criteria](03-grant-funding.md).
- **Departmental policy:** reading a rubric's effect on rankings is the first step in
  arguing about it.

## Related lessons

- [24-05-03 Understanding Grant Funding and Review Criteria](03-grant-funding.md) —
  the funding component of the record.
- [24-05-02 Thesis Structure, Chapters and the Contribution Statement](02-thesis-structure.md) —
  the contribution statement a CV summarises.
- [24-04-03 Seminars, Qualifying Exams and Thesis Defence](../04-presentation-and-communication/03-seminar-and-defence.md) —
  the talk and questioning that accompany the documents.
- [26-04-04 Bibliography: Potential Fields and EM](../../26-reference-library/04-textbook-bibliography/04-bibliography-potential-em.md) —
  the literature whose citation practices shape these metrics.

## Self-assessment checklist

- [ ] I can summarise a record with a distribution, not an index.
- [ ] I can demonstrate what the h-index ignores.
- [ ] I can explain why h must not be compared across career stages.
- [ ] I can compute how many candidates a rubric change moves.
- [ ] I can write a research statement with a proportionate future.
- [ ] I can name what a CV cannot establish and what fills the gap.
