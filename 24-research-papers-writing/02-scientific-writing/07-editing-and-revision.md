---
id: 24-02-07
title: "Self-Editing, Revision and Response to Reviewers"
level: doctoral
prereqs: ["24-02-02", "24-01-02"]
estimated_minutes: 50
tags: [writing, editing, revision, peer-review, response-letter]
---

# Self-Editing, Revision and Response to Reviewers

Revision is a process with a measurable shape: each pass removes less than the one
before, and the useful question is when to stop. The response to reviewers is a
second document with its own structure, and its success is measurable too — in
coverage of the points raised and in the number of rounds the manuscript needs.
This lesson quantifies both: the diminishing returns of successive passes, how
much of the text actually changes in a "full rewrite", and the cost of leaving a
reviewer's point unaddressed.

The organising idea is that **editing is aimed at a decision**. A pass exists to
change something specific: the claim, the structure, the prose or the response.
A pass without a target removes words without changing the paper, and the
demonstration shows exactly how quickly that yields nothing.

> **Data provenance.** All numbers are **SYNTHETIC**. The manuscript is a
> generated word sequence, the cut fractions and hours per pass are chosen values,
> and the reviewer-point model (points raised, words per response, re-raise
> probability) is chosen teaching data. The similarity measure is
> `difflib.SequenceMatcher`, a standard library implementation.

## Learning objectives

By the end of this lesson you will be able to:

1. **Plan** revision as a sequence of targeted passes and **state** each pass's
   objective and stopping rule.
2. **Compute** the words removed and the words-per-hour yield of successive
   passes, and **decide** when the marginal cut no longer changes the claim.
3. **Measure** how much of a text actually changes between draft and final using a
   sequence-similarity score.
4. **Write** a response letter that addresses every point, and **compute** its
   coverage and length.
5. **Estimate** the cost of an unaddressed point in additional review rounds.
6. **Separate** the four kinds of editing — content, structure, prose, format —
   and **state** why they must not be performed in the same pass.

## Prerequisites

- [24-02-02 Paper Structure: IMRaD and Its Variants](02-paper-structure.md) — the
  structure that structural editing works on.
- [24-01-02 Reading Strategies: Skim, Map, Deep-Read, Critique](../01-reading-research-literature/02-reading-strategies.md) —
  the critique that generates revision items.

## 1. Four passes with four objectives

| Pass | Objective | Product | Stop when |
|---|---|---|---|
| Content | Every claim is supported | A list of claims and evidence | No claim is unsupported |
| Structure | The argument has four transitions | An outline that matches the text | The outline reads as an argument |
| Prose | Sentences carry one claim each | Sentence-level edits | No sentence over $30$ words |
| Format | Journal rules, references, figures | Compliant manuscript | The checklist is complete |

Performing them separately matters because they interfere: editing prose while
deciding content produces sentences that are polished and wrong. The
demonstration's numbers describe the prose pass, which is the one that can be
scheduled and measured.

## 2. Diminishing returns of successive prose passes

Starting from a $6200$-word draft and cutting a fixed fraction of the *remaining*
words in each pass:

| Pass | Cut | Words removed | Remaining | Share of draft | Words removed per hour |
|---|---|---|---|---|---|
| 1 | $12\%$ | $744$ | $5456$ | $88.0\%$ | $248$ |
| 2 | $8\%$ | $436$ | $5020$ | $81.0\%$ | $145$ |
| 3 | $5\%$ | $251$ | $4769$ | $76.9\%$ | $84$ |

Total reduction is $1431$ words ($23.1\%$ of the draft) in $9\ \mathrm{h}$. The
third pass removes a third of what the first removed for the same effort. The
operational rule: set the pass's target as a change in the *claim*, not a
percentage of words, and stop when the next cut would only shorten a sentence
whose content is already right.

## 3. How much actually changes

The demonstration builds a synthetic draft of $3100$ words, applies a revision
that replaces $20\%$ of words, drops $10\%$ of sentences and transposes $5\%$ of
adjacent sentence pairs, and measures the sequence similarity between draft and
final:

$$\text{similarity} = 0.7767,\qquad \text{changed} = 22.3\%,
\qquad \text{length change} = -198\ \text{words}\ (-6.4\%).$$

A revision that a co-author would call a complete rewrite changes about a fifth of
the sequence. Two consequences:

- **Similarity is the honest measure of revision.** Line counts and page counts
  change for formatting reasons; the sequence-similarity score changes only when
  words change.
- **Complete rewrites are usually wasteful.** If $78\%$ of the sequence survives a
  hard rewrite, the rewriting effort is largely spent re-typing text that was
  already correct. Targeted editing is cheaper, and the similarity score tells you
  which parts you actually changed.

## 4. The response letter

The demonstration's model has two reviewers raising $4$ and $5$ points, $9$ in
total, at about $180$ words per point for a complete response:

| Points addressed | Coverage | Response length |
|---|---|---|
| $0$ | $0.0\%$ | $0$ words |
| $3$ | $33.3\%$ | $540$ words |
| $6$ | $66.7\%$ | $1080$ words |
| $9$ | $100.0\%$ | $1620$ words |

A complete response is about $1600$ words — six and a half pages at $250$
words/page, which is normal and should be planned for, not resented.

**The cost of an unaddressed point.** With a re-raise probability of $0.60$ per
unaddressed point:

| Points addressed | Unaddressed | Expected re-raised next round |
|---|---|---|
| $9$ of $9$ | $0$ | $0.0$ |
| $6$ of $9$ | $3$ | $1.8$ |
| $4$ of $9$ | $5$ | $3.0$ |
| $0$ of $9$ | $9$ | $5.4$ |

Each unaddressed point costs roughly another round of review, and a round is
months of wall-clock time. The asymmetry is decisive: a paragraph that addresses a
point costs minutes; a round costs weeks to months and one more chance for a
reviewer to find something new.

**A point-by-point letter has four parts per point:**

1. **The point**, quoted or paraphrased faithfully — so a reader can check that you
   understood it.
2. **What you did**, with the location: "Methods §3.2, lines 210–218".
3. **The change itself**, quoted, so the editor need not reopen the manuscript.
4. **Where you disagree, the reason** — with evidence, and without adjectives.
   Disagreement is legitimate; ignoring is not.

If a change cannot be made, say what was done instead and why. "We cannot obtain
the 1962 field notes; we have added the digitised subset and labelled the gap in
Data Availability" is a complete answer. Silence is not.

## 5. The revision loop

1. Collect all points from all reviewers into one list; number them.
2. Classify each as content, structure, prose or format.
3. Do all content and structure changes first, because they invalidate prose work.
4. Re-run the prose pass on the changed sections only.
5. Write the response letter, with one entry per numbered point.
6. Re-derive the abstract and title from the revised text (they drift during
   revision; see
   [24-02-05 Abstracts, Titles and the Art of the Concrete Claim](05-writing-abstracts-titles.md)).
7. Recompile, check the figures' captions against the changed text, and submit.

## Assumptions and regime of validity

1. **The cut fractions and hours are chosen.** Real editing speed varies by an
   order of magnitude with the writer's familiarity and the text's maturity.
2. **The manuscript is a synthetic word sequence.** The similarity score measures
   exactly what it says — token overlap after alignment — and not readability,
   correctness or improvement.
3. **The reviewer model is two reviewers and nine points.** Real reviews vary from
   two to five reviewers and from three to thirty points.
4. **The re-raise probability is a single number.** Re-raise behaviour depends on
   the reviewer, the editor and the point's severity.
5. **Coverage is not concession.** Addressing every point includes addressing some
   of them with a reasoned disagreement; coverage counts responses, not changes.

## The honest summary

Three passes remove $23.1\%$ of a draft with the last pass yielding a third of the
first, a hard rewrite changes only $22.3\%$ of the sequence, and a complete
response to nine reviewer points is about $1600$ words while each unaddressed
point costs about $0.6$ of a review round. The process is measurable, and knowing
the numbers makes the decisions — how many passes, how long a letter — deliberate
rather than anxious.

## Python demonstration

[`code/editing_and_revision_demo.py`](./code/editing_and_revision_demo.py) prints
four labelled sections: the three passes with their diminishing words-per-hour
yield; the sequence-similarity measure of draft versus final; the coverage and
length table for a response letter; and the expected re-raises as a function of
coverage.

```bash
cd 24-research-papers-writing/02-scientific-writing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python editing_and_revision_demo.py
```

## Exercises

Problems are in
[`exercises/07-editing-and-revision-exercises.md`](./exercises/07-editing-and-revision-exercises.md),
worked answers in
[`exercises/07-editing-and-revision-solutions.md`](./exercises/07-editing-and-revision-solutions.md).

## Mastery checkpoint

Take a manuscript you are revising:

1. Write the four pass objectives as a list and record the hour you spend on each.
2. Compute the words removed per hour for each pass and stop when it falls below
   your threshold.
3. Compute the draft-to-final similarity and state which sections changed.
4. List every reviewer point, numbered, and write one response entry per point.
5. Re-derive the abstract from the revised text and check it against the Results.

## Common pitfalls

1. **Editing everything at once.** Prose polish on a section whose structure will
   change is wasted work.
2. **Cutting to a target length rather than to a claim.** The third pass rarely
   changes the paper.
3. **A response letter that says "done" without a location.** The editor cannot
   verify it, and the reviewer re-reads the whole manuscript.
4. **Answering points in prose paragraphs.** A point-by-point format is
   checkable; a narrative is not.
5. **Rewriting the abstract last and forgetting.** Abstract drift during revision
   is the commonest source of disagreement between abstract and results.
6. **Treating a reviewer disagreement as an insult.** Disagreement with evidence
   is what peer review is for; answer it with evidence.

## Where this is used

- **Every submission and resubmission:** the response letter is a document that
  editors read closely.
- **Thesis and report revision:** the same pass structure applies to chapters,
  with examiners in place of reviewers; see
  [24-05-02 Thesis Structure](../05-thesis-and-proposals/02-thesis-structure.md).
- **Co-author drafts:** numbering the points and classifying them by type works
  for internal review as well.
- **Open review:** the response is published alongside the paper, so its quality is
  part of the record; see
  [24-03-05 Peer Review Practice](../03-research-methods-and-rigour/05-peer-review-practice.md).

## Related lessons

- [24-02-01 Principles of Clear Scientific Writing](01-writing-principles.md) —
  the rules the prose pass applies.
- [24-01-03 Critiquing Methods, Data and Inference](../01-reading-research-literature/03-critiquing-methods.md) —
  how the critique that generates revision items is built.
- [24-03-05 Peer Review Practice](../03-research-methods-and-rigour/05-peer-review-practice.md) —
  the other side of the exchange.
- [22-05-03 Collaborative Writing](../../22-data-engineering-reproducibility/05-collaboration-and-project-management/03-collaborative-writing.md) —
  the tooling for multi-author revision.

## Self-assessment checklist

- [ ] I can name the four passes and their stopping rules.
- [ ] I can compute words removed per hour and decide when to stop.
- [ ] I can measure how much of a text changed between two versions.
- [ ] I can write a four-part response entry for any reviewer point.
- [ ] I can estimate the cost of an unaddressed point.
- [ ] I can re-derive the abstract after revision and check it.
