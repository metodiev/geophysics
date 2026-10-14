---
id: 24-05-02
title: "Thesis Structure, Chapters and the Contribution Statement"
level: research
prereqs: ["24-05-01", "24-02-02"]
estimated_minutes: 60
tags: [thesis, structure, chapters, redundancy, contribution, writing]
---

# Thesis Structure, Chapters and the Contribution Statement

A thesis is a set of chapters that must work as one argument, and the failure mode is
not incompleteness but **redundancy and unsupported claims**. Two measurements
address it: how much of the thesis repeats material already stated, and how many
words actually support each claimed contribution. This lesson computes both, plus the
page budget and the writing time.

The organising idea is that **a contribution statement is a testable list**. Each
claimed contribution should map to words somewhere in the thesis, and a claim
supported by a single chapter is a chapter result rather than a thesis contribution.
Making the list before writing the synthesis chapter turns the last chapter from a
summary into an argument.

> **Data provenance.** All numbers are **SYNTHETIC**. Chapter lengths, overlap
> fractions, the published fraction and the writing rate are chosen teaching values;
> no thesis was measured. Page norms vary widely between institutions and
> disciplines.

## Learning objectives

By the end of this lesson you will be able to:

1. **Allocate** a chapter word budget against a page limit and **state** which
   chapters must lose words.
2. **Compute** the redundancy of a thesis from chapter-to-chapter overlap and
   **state** the correct remedy for it.
3. **Map** each claimed contribution to the chapters that support it and **compute**
   the supporting word count.
4. **Diagnose** a contribution that is really a chapter result.
5. **Structure** a thesis as introduction, setting, method, results, synthesis,
   conclusions and appendices, and **state** the job of each.
6. **Estimate** the writing time net of redundancy and **compare** it with the
   revision time.

## Prerequisites

- [24-05-01 Writing a Compelling Research Proposal](01-research-proposal.md) — the
  promise the thesis delivers.
- [24-02-02 Paper Structure: IMRaD and Its Variants](../02-scientific-writing/02-paper-structure.md) —
  the chapter-level structure.

## 1. Chapter budget against the page limit

The demonstration's thesis: $8$ chapters, $69\,000$ words, $400$ words per page, and a
limit of $160$ pages:

| Chapter | Words | Share | Pages | Cumulative pages |
|---|---|---|---|---|
| 1 Introduction | $7000$ | $10.1\%$ | $18$ | $18$ |
| 2 Setting and data | $9000$ | $13.0\%$ | $22$ | $40$ |
| 3 Method | $12\,000$ | $17.4\%$ | $30$ | $70$ |
| 4 Result one | $10\,000$ | $14.5\%$ | $25$ | $95$ |
| 5 Result two | $11\,000$ | $15.9\%$ | $28$ | $122$ |
| 6 Synthesis and discussion | $10\,000$ | $14.5\%$ | $25$ | $148$ |
| 7 Conclusions | $4000$ | $5.8\%$ | $10$ | $158$ |
| Appendices | $6000$ | $8.7\%$ | $15$ | $172$ |

Total $172$ pages against a limit of $160$: **over by $12$ pages**, or $5000$ words
to cut. Where the cut comes from is the decision the budget forces, and the right
answer is not "everywhere":

- **Cut redundancy first** (§2): repeated method descriptions are the cheapest words
  to remove, because the reader has already read them.
- **Move material to appendices**, which are usually excluded from length limits and
  which the examiner is not required to read.
- **Cut evenly last**: distributing a cut evenly costs every chapter its clearest
  prose and buys nothing.

## 2. Redundancy, measured

Redundancy arises when consecutive chapters restate the same material — usually the
method, the setting, and the figures. With chosen overlap fractions, the demonstration
totals

$$10\,090\ \text{repeated words} = 14.6\%\ \text{of the thesis}.$$

That is not necessarily a defect: theses are read chapter by chapter, and a chapter
that is also a paper must stand alone. The defect is **repetition instead of
reference**. The remedy costs nothing:

> "Sections 3.2–3.4 describe the processing chain; this chapter uses it unchanged."

One sentence replaces several pages. Applying that rule where the overlap is genuine
removes most of the $14.6\%$ without removing any result — which is exactly the $5000$
words the page limit requires in §1.

**The published-chapter complication.** If about $40\%$ of the chapters are already
published (a chosen value here), some of the overlap is unavoidable, because the
published versions must repeat the method to be readable. The honest presentation
identifies which overlap is by requirement and which is by habit, and reduces only the
second.

## 3. The contribution statement as a test

The demonstration's six claimed contributions, with the chapters that support them and
the supporting word count:

| Claimed contribution | Chapters | Words | Supported? |
|---|---|---|---|
| A new processing chain | 2, 3, 4 | $31\,000$ | yes |
| The first regional velocity model | 4, 5 | $21\,000$ | yes |
| A quantified uncertainty budget | 3, 5 | $23\,000$ | yes |
| An open dataset and code | 2 | $9000$ | thin |
| A revised tectonic interpretation | 5, 6 | $21\,000$ | yes |
| A methodological recommendation | 7 | $4000$ | thin |

At a support threshold of $15\,000$ words, four of six claims are supported and two
are thin — and both thin ones are supported by a **single chapter**. That is the
diagnostic: a claim supported by one chapter is a chapter result. Two remedies are
available, and both are legitimate:

1. **Widen the claim's support** by adding the second result that tests it, or by
   quantifying it in the synthesis chapter.
2. **Narrow the claim** until it matches what the chapter supports: "an open dataset
   and code" becomes "a reproducible processing chain with archived code", which is
   supported by chapter 2 and by the chain itself.

The wrong remedy is to keep the claim and pad the synthesis chapter. A reader who
tests the claim against the chapter will find it unsupported however long the
synthesis is.

## 4. Writing time

Net new words after removing the redundancy:

$$69\,000 - 10\,090 = 58\,910\ \text{words}.$$

At a chosen $450$ words per day that is

$$\frac{58\,910}{450} = 131\ \text{days} = 26.2\ \text{weeks of full-time writing}.$$

Two honest caveats. First, $26$ weeks of *full-time* writing is not what a thesis
schedule usually provides: the honest plan spreads the writing across the analysis, in
chapter-sized pieces, so that each chapter is drafted when its results are fresh.
Second, revision is not a rounding error: the module on editing measures three passes
removing $23\%$ of a draft, and the second and third passes of a thesis chapter are
where the argument becomes visible. Budget time for them explicitly; a chapter that is
drafted but not revised is a chapter that will come back.

## 5. Chapter jobs and their order

| Chapter | Job | Test |
|---|---|---|
| Introduction | State the problem, the gap, the question and the contributions | A reader can state your contribution after §1 |
| Setting and data | Establish what the region and the data can support | Every later claim is bounded by this chapter |
| Method | Make the result reproducible | A competent stranger could repeat it (see module 24-02) |
| Results (one or more) | Present evidence with uncertainty | Every number has a unit and an interval |
| Synthesis and discussion | Turn results into contributions; compare with the literature; state limits | Each claimed contribution is traceable here |
| Conclusions | State the contribution, the limits and what would falsify | Nothing appears that is not established earlier |
| Appendices | Hold detail and reproductions | The examiner need not read them to judge the thesis |

## Assumptions and regime of validity

1. **Chapter lengths and overlaps are chosen.** Real theses vary by field, and a
   theory thesis or a data-descriptor thesis has different proportions.
2. **Word counts are a proxy for content.** Moving material to an appendix changes the
   page count without changing the content, and that is a legitimate tactic as long as
   the main text remains readable.
3. **The support threshold ($15\,000$ words) is illustrative.** The transferable test
   is traceability, not a particular count.
4. **Page limits are institutional.** Some institutions exclude appendices, some do
   not; check before relying on the arithmetic.
5. **The contribution statement is read by examiners and by future employers.** It is
   the part of a thesis that is read most often after the viva.

## The honest summary

A thesis is over its page limit by $12$ pages in the demonstration, and it repeats
$14.6\%$ of its words; the redundancy is the cheapest $5000$ words available, removed
by reference rather than deletion. Two of six claimed contributions are supported by a
single chapter each, and a claim supported by one chapter is a chapter result. Support
the claim or narrow it — never pad the synthesis.

## Python demonstration

[`code/thesis_structure_demo.py`](./code/thesis_structure_demo.py) prints four
labelled sections: the chapter budget against the page limit; the redundancy
calculation; the contribution-support table; and the writing time net of redundancy.

```bash
cd 24-research-papers-writing/05-thesis-and-proposals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thesis_structure_demo.py
```

## Exercises

Problems are in
[`exercises/02-thesis-structure-exercises.md`](./exercises/02-thesis-structure-exercises.md),
worked answers in
[`exercises/02-thesis-structure-solutions.md`](./exercises/02-thesis-structure-solutions.md).

## Mastery checkpoint

1. Tabulate your chapters with word counts and compute your page total against the
   limit.
2. Estimate the redundancy: for each adjacent pair, write down the material that is
   restated rather than referenced.
3. List your claimed contributions and the chapters that support each.
4. Compute the supporting words for each claim and mark the thin ones.
5. For each thin claim, decide whether to widen the support or narrow the claim, and
   write the revised sentence.

## Common pitfalls

1. **Writing the introduction first and the contribution statement last.** The
   contribution list should exist before the synthesis chapter is written.
2. **Repeating the method in every chapter.** Refer to it once and cite the section.
3. **Padding the synthesis.** It does not create support for a claim.
4. **Cutting evenly to meet a page limit.** Cut the redundancy instead.
5. **Treating the appendix as a bin.** It is read; it should be ordered and titled as
   carefully as the main text.
6. **Leaving revision out of the schedule.** Three passes are part of the writing, not
   an extra.

## Where this is used

- **Thesis and dissertation writing:** the whole lesson.
- **Cumulative theses:** the introduction and synthesis chapters carry the argument the
  papers do not; see [24-05-04 Academic CVs, Research Statements and Career Paths](04-cv-and-career.md).
- **Viva preparation:** examiners test the contribution statement; see
  [24-04-03 Seminars, Qualifying Exams and Thesis Defence](../04-presentation-and-communication/03-seminar-and-defence.md).
- **Turning a thesis into papers:** the contribution list is the paper plan, and the
  redundancy audit shows which material is genuinely new.

## Related lessons

- [24-05-01 Writing a Compelling Research Proposal](01-research-proposal.md) — the
  promise this document delivers.
- [24-02-02 Paper Structure: IMRaD and Its Variants](../02-scientific-writing/02-paper-structure.md) —
  the chapter-level structure and its variants.
- [24-02-07 Self-Editing, Revision and Response to Reviewers](../02-scientific-writing/07-editing-and-revision.md) —
  the revision passes the schedule must include.
- [24-03-05 Peer Review: How to Do It Well and Receive It Well](../03-research-methods-and-rigour/05-peer-review-practice.md) —
  what an examiner's questions will resemble.

## Self-assessment checklist

- [ ] I can compute a chapter budget against a page limit.
- [ ] I can estimate redundancy and state the remedy.
- [ ] I can map contributions to supporting chapters and words.
- [ ] I can diagnose a chapter result masquerading as a contribution.
- [ ] I can state each chapter's job and its test.
- [ ] I can plan the writing time including revision.
