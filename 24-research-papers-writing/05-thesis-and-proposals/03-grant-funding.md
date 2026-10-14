---
id: 24-05-03
title: "Understanding Grant Funding and Review Criteria"
level: research
prereqs: ["24-05-01"]
estimated_minutes: 50
tags: [funding, grants, review, success-rate, panel, career]
---

# Understanding Grant Funding and Review Criteria

Funding decisions are made by comparing noisy scores against a budget line, and the
arithmetic of that process explains most of what researchers experience as arbitrary.
This lesson measures the noise: how wide the band of uncertain decisions is, how many
applications one award costs, and what a resubmission is worth. The point is not
resignation but planning — a scheme whose boundary is noisy can be navigated
rationally.

The organising idea is that **the boundary is set by the funding rate, not by the
proposals**. A panel with $20\%$ funding and $400$ applications funds $80$; which
$80$ depends on scores whose standard error is a property of the review process.
Understanding which decisions are stable and which are coin flips tells you where to
spend effort.

> **Data provenance.** All numbers are **SYNTHETIC**. Panel sizes, funding rates,
> reviewer noise, revision gains and preparation costs are chosen teaching values; no
> funding scheme, panel or application is analysed.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the success boundary from an application count and a funding rate.
2. **Compute** the standard error of a panel mean from the reviewer noise and the
   number of reviewers.
3. **Measure** the band of decisions that are uncertain and **state** what happens to
   its width when reviewers are added.
4. **Compute** the expected number of submissions to one award under a stated success
   rate, and the effect of revision.
5. **Compute** the cost per funded project and **justify** a triage policy from it.
6. **State** what a score sheet does and does not measure, and how to write for the
   form the panel uses.

## Prerequisites

- [24-05-01 Writing a Compelling Research Proposal](01-research-proposal.md) — the
  artefact being scored.

## 1. The scheme and the boundary

With $400$ applications, $12$ reviewers each, and a $20\%$ funding rate:

- true quality has a standard deviation of $0.74$ points on a $1$–$5$ scale;
- panel scores have a standard deviation of $0.75$;
- $80$ applications are funded, and the score at the boundary is $4.0272$.

The boundary's *position* is fixed by the funding rate; its *location on the score
scale* is fixed by the pool. A stronger pool moves the boundary up without changing
any applicant's work — which is why a rejection is not a statement about absolute
quality, and why resubmission to a different panel or year can succeed unchanged.

## 2. Review noise and the uncertain band

The standard error of a panel mean of $k$ reviews with per-reviewer noise
$\sigma = 0.55$ is

$$\text{SE} = \frac{\sigma}{\sqrt{k}} = \frac{0.55}{\sqrt{12}} = 0.1588 .$$

A $90\%$ band around the boundary is therefore

$$\pm 1.645 \times 0.1588 = \pm 0.2612\ \text{points}.$$

The demonstration finds $87$ applications ($21.8\%$ of all) inside that band, of which
$33$ are funded and $54$ are rejected. Inside the band, the decision is closer to a
coin toss than to a judgement; outside it, the panel is discriminating — the rank
correlation between true quality and panel score is $0.9766$.

**Adding reviewers.** Halving the band requires four times the reviewers:

$$\text{SE} \propto \frac{1}{\sqrt{k}} \;\Rightarrow\; k \to 4k .$$

From $12$ reviewers to $48$ halves the band from $0.261$ to $0.131$ points. This is the
arithmetic behind every proposal to improve peer review: the improvement is real,
priced at quadruple the reviewer effort, and concentrated exactly on the borderline
cases that discussion is designed to resolve.

## 3. Expected submissions and the value of revision

With a first-submission success probability of $p$, the number of submissions to one
award is geometric with mean $1/p$:

| Strategy | $p$ | Expected submissions |
|---|---|---|
| First-submission rate always | $0.12$ | $8.3$ |
| Revised resubmission rate always | $0.22$ | $4.5$ |
| Mixed (first, then revisions) | — | $5.9$ |

At the observed overall rate of $20\%$, the expected number of applications per award is

$$\frac{1}{0.20} = 5.0 .$$

Two planning consequences. First, **the number five is not a failure rate; it is the
scheme**. Second, the difference between $8.3$ and $4.5$ submissions is the value of
revision, and it is large: revising a proposal is worth more than writing a new one,
because the reviewed criticism is specific and the resubmission inherits the panel's
familiarity. The rational policy is to revise every promising proposal until it either
succeeds or the criticism stops being actionable.

## 4. Cost per funded project

The demonstration's effort model is $20$ days per application:

$$400 \times 20 = 8000\ \text{person-days},
\qquad \frac{8000}{80} = 100\ \text{person-days per funded project}
= 0.5\ \text{person-years}.$$

Of the $8000$ days, the successful applications consume $80 \times 20 = 1600$; the
remaining $6400$ days are the cost of the process. That ratio is the argument for
triage — not for writing worse proposals, but for spending the effort where the
expected return is highest:

- **Revise rather than rewrite.** The expected submissions per award falls from $8.3$
  to around $4.5$ when criticism is addressed.
- **Do not spend twenty days on a proposal that does not meet the scheme's threshold
  criteria.** Many calls have eligibility or scope filters that a careful read decides
  in an hour.
- **Reuse the writing.** A rejected proposal's background, method and data-management
  sections are reusable across calls; only the aims and the fit need rewriting.

## 5. What a score sheet measures

A score sheet measures a panel's judgement of a written document in a fixed time,
against named criteria. It does not measure the science's quality, the applicant's
ability, or the project's eventual value. Four consequences for writing:

1. **Comprehension is part of the score.** A reviewer with twenty proposals and a week
   reads quickly; headings that match the criteria are read, others are skimmed.
2. **Numbers are checkable and therefore persuasive.** Sample sizes, effect sizes and
   timelines give a reviewer something to verify, which converts an impression into an
   assessment.
3. **Fit is scored explicitly in some schemes.** Naming which part of the call you
   answer is a scored act, not a courtesy.
4. **Track record is evidence about feasibility.** It is the only part of the score
   you cannot fix in the current round, which makes it the reason to keep a funded
   project's outputs visible.

## Assumptions and regime of validity

1. **The scheme is synthetic and simple.** Real schemes include interviews, rebuttals,
   panel discussion and portfolio balancing, all of which add structure that a
   score-plus-noise model omits.
2. **Reviewer noise is homogeneous.** Real reviews differ in quality and scope, and a
   single careless review has more effect than an average one.
3. **Scores are comparable across panels.** In practice panel composition and
   calibration differ; this is part of why the boundary is noisy.
4. **The success probability is constant.** Real proposals differ in quality, and a
   strong proposal's $p$ is genuinely higher; the average is what the arithmetic uses.
5. **Effort is the only cost.** Opportunity cost, and the morale cost of repeated
   rejection, are real and are outside the model.

## The honest summary

The boundary is set by the funding rate; the band of uncertain decisions around it is
$\pm 0.26$ points at $12$ reviewers and halves only at $48$; the expected number of
applications per award is $5.0$, falling to about $4.5$ when criticism is addressed;
and one funded project costs about $100$ person-days of proposal writing. Revise,
reuse and triage — those are the three actions the arithmetic supports.

## Python demonstration

[`code/grant_funding_demo.py`](./code/grant_funding_demo.py) prints four labelled
sections: the scheme and the boundary; the noise band and its width against reviewer
count; the expected submissions under three strategies; and the cost per funded
project.

```bash
cd 24-research-papers-writing/05-thesis-and-proposals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python grant_funding_demo.py
```

## Exercises

Problems are in
[`exercises/03-grant-funding-exercises.md`](./exercises/03-grant-funding-exercises.md),
worked answers in
[`exercises/03-grant-funding-solutions.md`](./exercises/03-grant-funding-solutions.md).

## Mastery checkpoint

1. For a scheme you know, record the funding rate, the typical application count and
   the number of reviewers per application.
2. Compute the standard error of the panel mean and the $90\%$ band around the
   boundary.
3. State how many applications in a typical round fall inside the band.
4. Compute your expected number of submissions to one award at the scheme's rate, and
   the same with your revision policy.
5. Compute the cost of your proposal writing in person-days per award, using the
   scheme's rate.

## Common pitfalls

1. **Reading a rejection as a verdict.** Inside the band the decision is noise; the
   band is measurable.
2. **Writing a new proposal instead of revising.** The expected-submissions arithmetic
   is decisive.
3. **Ignoring eligibility and scope.** They are decided in an hour and lose a
   twenty-day effort.
4. **Underusing the criticism.** A review is the most specific feedback you will ever
   receive on a proposal; file it and answer it point by point.
5. **Believing the score is about the science.** It is about a document, read quickly,
   against named criteria.
6. **Not tracking the effort.** Without the person-days figure, triage decisions are
   made on feeling.

## Where this is used

- **Every funding round:** the arithmetic of the boundary, the band and the resubmission.
- **Group and departmental strategy:** the cost per funded project informs how many
  proposals a group should submit.
- **Mentoring:** the expected-submissions calculation is what makes a rejection
  survivable; see
  [24-05-04 Academic CVs, Research Statements and Career Paths](04-cv-and-career.md).
- **Panel service:** understanding the noise band is the reason panels discuss
  borderline cases instead of ranking them; see
  [24-03-05 Peer Review: How to Do It Well and Receive It Well](../03-research-methods-and-rigour/05-peer-review-practice.md).

## Related lessons

- [24-05-01 Writing a Compelling Research Proposal](01-research-proposal.md) — the
  document the panel scores.
- [24-03-05 Peer Review: How to Do It Well and Receive It Well](../03-research-methods-and-rigour/05-peer-review-practice.md) —
  the review process in general.
- [24-05-04 Academic CVs, Research Statements and Career Paths](04-cv-and-career.md) —
  how funding record enters a career narrative.
- [24-03-04 Reproducible Research Practice End to End](../03-research-methods-and-rigour/04-reproducible-research-practice.md) —
  what makes a funded project's outputs count later.

## Self-assessment checklist

- [ ] I can compute a funding boundary from a rate and a count.
- [ ] I can compute a panel-mean standard error and the uncertain band.
- [ ] I can state the cost of halving the band.
- [ ] I can compute expected submissions and the value of revision.
- [ ] I can compute cost per funded project.
- [ ] I can state what a score sheet does not measure.
