---
id: 24-03-05
title: "Peer Review: How to Do It Well and Receive It Well"
level: research
prereqs: ["24-02-07", "24-03-01"]
estimated_minutes: 60
tags: [research, peer-review, referee-report, aggregation, agreement, icc]
---

# Peer Review: How to Do It Well and Receive It Well

Peer review is a measuring instrument with a known noise level, and both writing
reviews and receiving them are easier once that is understood. This lesson
quantifies the instrument: how much reviewers differ on the same proposal, how much
of a score's variance belongs to the proposal and how much to the reviewer, what
happens to a funding line when one reviewer is dropped, and what reviewer-
normalised scores do to a ranking.

The organising idea is **separating the object from the instrument**. A review
report should make claims about the manuscript that another reader could check, and
a review received should be read for the checkable claims and the requests. The
numbers below explain why a reviewer who disagrees with you may still be right, and
why a panel's decision is partly a property of its composition.

> **Data provenance.** All numbers are **SYNTHETIC**. Proposals, qualities,
> reviewer biases and noise are generated with chosen parameters; no real review,
> score sheet or panel decision is analysed anywhere in this repository.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a review report whose claims are checkable, with a stated recommendation
   and its reasons.
2. **Measure** within-proposal reviewer spread and **state** what it means for a
   single score.
3. **Compute** an intraclass correlation for a panel and **interpret** it as the
   proportion of score variance attributable to the proposal.
4. **Quantify** how aggregation, panel composition and normalisation change a
   ranking, and **state** what each cannot fix.
5. **Extract** the checkable content from a review you receive and **write** a
   response that addresses it.
6. **State** the limits of peer review as an instrument and **name** the practices
   that compensate.

## Prerequisites

- [24-02-07 Self-Editing, Revision and Response to Reviewers](../02-scientific-writing/07-editing-and-revision.md) —
  the response side of the exchange.
- [24-03-01 Formulating Answerable Research Questions](01-research-questions.md) —
  the question a reviewer must be able to identify.

## 1. The synthetic panel

The demonstration scores $40$ proposals with $4$ reviewers each on a $1$–$5$ scale
in half-point steps. True quality has a standard deviation of $0.86$ points;
reviewer biases are $(-0.45, +0.10, +0.35, -0.10)$ with a per-review noise standard
deviation of $0.55$. The measured reviewer means are $2.46$, $3.00$, $3.42$ and
$2.84$.

| Quantity | Value |
|---|---|
| Mean within-proposal standard deviation | $0.61$ points |
| Mean within-proposal range | $1.35$ points |
| Proposals where two reviewers differ by $\geq 2$ points | $17.5\%$ |

A range of $1.35$ points on a $5$-point scale is the instrument's resolution. It
means a single review is a sample of one, and that "reviewer 2 says 2.0" is not a
statement about the proposal alone.

## 2. Variance decomposition

With $n_p = 40$ proposals and $k = 4$ reviewers:

$$\text{MS}_{\text{between}} = 2.856, \qquad
\text{MS}_{\text{within}} = 0.420,$$
$$\text{ICC}(1) = \frac{\text{MS}_B - \text{MS}_W}{\text{MS}_B + (k-1)\text{MS}_W}
= \frac{2.856 - 0.420}{2.856 + 3 \times 0.420} = 0.592 .$$

So $59.2\%$ of the score variance is attributable to the proposal and $40.8\%$ to
reviewers and noise. Two consequences:

- The panel carries real signal: ICC well above zero means the scores are not
  merely opinion.
- Averaging more reviewers improves the *aggregate's* reliability by the
  Spearman-Brown relation,
  $\rho_k = k\rho_1/[1 + (k-1)\rho_1]$, but it does not change the ICC, which is a
  property of the instrument.

## 3. Aggregation and panel composition

Dropping the harshest reviewer in the demonstration (mean bias $-0.45$):

| Quantity | Value |
|---|---|
| Mean shift in the panel score | $+0.156$ points |
| Proposals funded in both rankings | $10$ of $10$ |
| Funded status flips | $0$ |
| Spearman rank correlation (4 vs 3 reviewers) | $0.9831$ |

The ranking is robust and the *level* is not. With a fixed funding fraction, the
same proposals survive here because the removed bias is common to all proposals and
the ranking is invariant to a level shift. Replace the bias with reviewer-specific
noise instead — a reviewer who is harsh on some proposals and generous on others —
and the funded set moves. This is the quantitative reason a resubmission to a
different panel is not a lottery but is not deterministic either.

## 4. Normalisation

Reviewer-normalised scores, $z = (s - \bar s_j)/\mathrm{sd}_j$ per reviewer, then
averaged:

| Quantity | Value |
|---|---|
| Spearman correlation with the raw mean ranking | $0.9976$ |
| Proposals changing decile | $6$ of $40$ ($15.0\%$) |
| Reviewer means after normalisation | exactly $0$ for each |

Normalisation removes stable level differences between reviewers. It cannot remove
differences in how two reviewers read the same proposal, which is the component
that produces the $17.5\%$ disagreement rate in §1. Six of forty proposals change
decile, which is a real effect on borderline decisions and none at all on the top
and bottom.

## 5. Writing a review

A report that an editor and an author can use has four parts:

1. **Summary.** The claim as you understood it, in two sentences. If you cannot
   write it, say so: that is a finding about the manuscript.
2. **Major points.** Each names the axis (reproducibility, data adequacy, inference,
   presentation), quotes or locates the evidence, states the consequence and says
   what would settle it.
3. **Minor points.** Numbered, specific, and separated from the major ones, so the
   author can triage.
4. **Recommendation with reasons.** Accept, minor revision, major revision, reject
   — with the reasons that would change your mind.

Two rules make a report checkable: **every criticism carries a location**, and
**every requested change states what it would establish**. "The Methods are unclear"
is not a point; "§3.2 does not state the taper length; without it the corner
frequency cannot be interpreted" is.

## 6. Receiving a review

Read a review in three passes, in this order:

1. **Extract the checkable claims.** Underline every statement that could be
   verified: a missing parameter, an inconsistent number, an unsupported sentence.
   These are the ones that are either right or wrong.
2. **Separate requests from opinions.** A request has an action; an opinion has an
   adjective. Act on requests, and answer opinions with evidence.
3. **Sort by cost.** Cheap changes that improve the paper come first, regardless of
   who is right, because they cost minutes and they remove a point from the next
   round (see
   [24-02-07 Self-Editing, Revision and Response to Reviewers](../02-scientific-writing/07-editing-and-revision.md)).

Two failure modes are worth naming. Taking a review personally wastes the pass that
identifies checkable claims; dismissing a review because one point is wrong
discards the rest. Both are common, and both are avoidable with the three-pass
order.

## Assumptions and regime of validity

1. **The panel is synthetic and small.** $40$ proposals and $4$ reviewers is a
   realistic teaching size, not a study of any journal or panel.
2. **Quality is a scalar.** Real proposals differ along several dimensions, and a
   single score compresses them; a multi-criteria rubric changes the ICC.
3. **Reviewer bias is additive.** Real biases interact with proposal content, which
   is the case normalisation cannot fix.
4. **The ICC is computed on a balanced design.** Missing reviews, which are common,
   require a mixed model or pairwise estimation.
5. **Peer review is not the only filter.** Post-publication review, replication and
   reader scrutiny carry part of the load; the numbers here describe one stage.

## The honest summary

A panel's scores carry real signal ($59.2\%$ of the variance is the proposal) and a
substantial noise component ($40.8\%$), with a within-proposal range of $1.35$
points and a $17.5\%$ rate of two-point disagreements. Normalisation fixes levels
and not readings. Write reviews that make checkable claims with locations, and read
reviews by extracting those claims first.

## Python demonstration

[`code/peer_review_practice_demo.py`](./code/peer_review_practice_demo.py) prints
four labelled sections: the panel scores and their spread; the variance
decomposition with the ICC; the effect of dropping the harshest reviewer; and the
ranking stability under reviewer normalisation.

```bash
cd 24-research-papers-writing/03-research-methods-and-rigour/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python peer_review_practice_demo.py
```

## Exercises

Problems are in
[`exercises/05-peer-review-practice-exercises.md`](./exercises/05-peer-review-practice-exercises.md),
worked answers in
[`exercises/05-peer-review-practice-solutions.md`](./exercises/05-peer-review-practice-solutions.md).

## Mastery checkpoint

1. Review a manuscript you have been sent, or a published paper, using the four-part
   structure of §5, with a location for every point.
2. Compute the within-proposal range of a set of scores you have access to (a panel,
   a group's rubric, a journal club).
3. Write the two sentences that summarise the paper's claim; if you cannot, state
   what stopped you.
4. For a review you have received, extract the checkable claims and separate them
   from opinions.
5. State which of your own standard criticisms are opinions dressed as requests, and
   reformulate them.

## Common pitfalls

1. **A review with no locations.** Uncheckable, and therefore unfixable.
2. **Confusing the paper you would have written with the paper submitted.** Relevance
   to your interests is not a criterion.
3. **Using the recommendation to signal effort.** A reject with two lines is worse
   for the author than a major revision with ten points.
4. **Treating a score difference as a disagreement about quality.** It is often a
   difference in weighting.
5. **Aggregating by mean only.** Level bias and rank are different; report both.
6. **Defending every point on receipt.** Cheap fixes cost minutes and remove a round.

## Where this is used

- **Journals and panels:** the ICC describes the instrument; the four-part report is
  the deliverable.
- **Group review:** the same structure works for internal review before submission.
- **Open review:** a published report is a document with your name on it; write
  accordingly; see
  [24-06-03 Interactive Publications and Notebooks as Articles](../06-reproducible-publication/03-notebooks-as-publications.md).
- **Supervision:** the three-pass reading order is teachable and immediately useful;
  see [24-04-03 Seminars, Qualifying Exams and Thesis Defence](../04-presentation-and-communication/03-seminar-and-defence.md).

## Related lessons

- [24-02-07 Self-Editing, Revision and Response to Reviewers](../02-scientific-writing/07-editing-and-revision.md) —
  the other half of the exchange.
- [24-01-03 Critiquing Methods, Data and Inference](../01-reading-research-literature/03-critiquing-methods.md) —
  the three axes a review names.
- [24-03-06 Research Ethics, Plagiarism, Authorship and Integrity](06-research-ethics.md) —
  the conduct rules that govern review, including confidentiality.
- [24-05-03 Understanding Grant Funding and Review Criteria](../05-thesis-and-proposals/03-grant-funding.md) —
  where panels and score sheets become funding decisions.

## Self-assessment checklist

- [ ] I can write a four-part review with a location for every point.
- [ ] I can compute within-proposal spread and interpret it.
- [ ] I can compute and interpret an ICC.
- [ ] I can state what normalisation fixes and what it cannot.
- [ ] I can extract checkable claims from a review I receive.
- [ ] I can name the limits of peer review and the practices that compensate.
