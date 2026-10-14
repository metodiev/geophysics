---
id: 24-02-05
title: "Abstracts, Titles and the Art of the Concrete Claim"
level: advanced
prereqs: ["24-02-01", "24-02-02"]
estimated_minutes: 45
tags: [writing, abstract, title, compression, metadata]
---

# Abstracts, Titles and the Art of the Concrete Claim

A title and an abstract are the only parts of a paper most readers will ever see.
They are also written under the tightest budget in the manuscript: a title of ten
to fifteen words and an abstract of a fixed word limit. This lesson treats both
as **compression problems**: what content survives a budget, what structure does
to the survival rate, and where uncertainty language is dropped on the way from
the paper to its advertisement.

The organising idea is that an abstract must contain **one concrete claim**: an
object, a result with a number, and a scope. Anything else is either setup or
advertisement. The demonstration measures how often each element survives, how
structured abstracts differ from unstructured ones, and how uncertainty language
is distributed unequally between significant and non-significant results.

> **Data provenance.** All numbers are **SYNTHETIC**. Abstracts and titles are
> modelled as token counts and binary content flags with chosen probabilities; no
> abstract or title was read, and no bibliometric study is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a title that names the object, the method, the setting and the scope,
   and **state** what each element makes retrievable.
2. **Compute** the word budget of an abstract under a limit and **choose** what to
   cut by information content rather than by position.
3. **Compare** a structured abstract with an unstructured one and **quantify** the
   content difference.
4. **Detect** spin: the loss of uncertainty language when a result is
   non-significant.
5. **State** the one concrete claim of an abstract in a single sentence, and check
   that the paper's Results support it.
6. **Explain** what a title or abstract cannot do, in particular that it cannot
   substitute for the Results section as evidence.

## Prerequisites

- [24-02-01 Principles of Clear Scientific Writing](01-writing-principles.md) —
  sentence-level compression.
- [24-02-02 Paper Structure: IMRaD and Its Variants](02-paper-structure.md) —
  where the content being compressed lives.

## 1. The title is a retrieval key

A title is read by people and parsed by indexes. Four elements make a paper
findable:

| Element | Example | Makes retrievable by |
|---|---|---|
| Object | "shear-wave velocity structure" | what is measured |
| Method | "ambient-noise tomography" | how it is measured |
| Setting | "the northern Andes" | region or system |
| Scope | "10–40 s period band" | the range over which it holds |

The demonstration models $400$ titles with chosen element probabilities: the
object appears in $89.2\%$, the method in $74.2\%$, the setting in $67.2\%$, the
scope in $36.5\%$. The mean concreteness score is $0.668 \pm 0.217$; all four
elements appear together in $16.8\%$ of titles and none of them in $0.2\%$.
$23.2\%$ of titles name the object but not the method — the reader learns what was
studied and not how.

A title missing the method is not wrong; it is less useful. A title stating the
scope invites disagreement at the right level: a reader who works outside the
period band knows immediately that the paper is not about their problem.

## 2. The abstract's word limit is a budget

The demonstration's $400$ abstracts have a mean of $245 \pm 43$ tokens, a median
of $246$ and a 90th percentile of $297$. Under a $250$-word limit, $190$ of them
($47.5\%$) are over — with a mean excess of $31$ words each and $5963$ words to
cut in total. Naive truncation at the limit gives a mean of $230$ tokens.

The arithmetic of the cut is the lesson. Cutting $31$ words from an abstract means
deleting one whole sentence, not trimming adjectives: adjectives cost a word each,
and a sentence costs fifteen. The choice is *which* content to lose, and the
content flags below say what is usually lost.

## 3. Structure and content survival

Content flags, compared between structured and unstructured abstracts (chosen
probabilities, measured on the sample):

| Content flag | Structured | Unstructured | Difference |
|---|---|---|---|
| context | $92.4\%$ | $89.0\%$ | $+3.4$ pp |
| gap | $60.3\%$ | $40.5\%$ | $+19.8$ pp |
| method | $95.8\%$ | $71.2\%$ | $+24.6$ pp |
| quantitative result | $85.2\%$ | $69.9\%$ | $+15.3$ pp |
| uncertainty | $48.1\%$ | $35.0\%$ | $+13.1$ pp |
| implication | $92.0\%$ | $81.6\%$ | $+10.4$ pp |

The overall content score is $0.731 \pm 0.178$, with structured abstracts at
$0.790$ and unstructured at $0.645$ — a difference of $14.5$ percentage points.
Structure's largest effects are on the **method**, the **gap** and the
**quantitative result**: the three elements that make an abstract useful for
deciding whether to read the paper. What structure does not fix is the uncertainty
flag, still below half in both groups.

## 4. Spin: where uncertainty language goes

The demonstration reports a significant result in $74.0\%$ of abstracts and
uncertainty language in $42.8\%$. Applying a modelled spin rate — a
non-significant result omits uncertainty language with probability $0.35$ — the
overall rate falls to $38.8\%$, and $18.0\%$ of abstracts report a
non-significant result while omitting any uncertainty language at all. The ratio
of uncertainty language between significant and non-significant abstracts is
$1.35$.

The pattern is the one to guard against in your own writing: hedging appears
abundantly where the result is already strong and disappears precisely where the
reader most needs it. An abstract that says "no significant change" without a
number or an interval has removed the one thing that would let a reader judge the
null result.

## 5. Writing the two artefacts

**Title.** Draft it as four elements, then delete the one that is least
informative for your audience:

> *Object + method + setting + scope:* "Shear-wave velocity structure of the
> northern Andes from ambient-noise tomography, 10–40 s period band."

**Abstract.** Six sentences, in this order, each with a job:

1. Context: what is already known, one sentence.
2. Gap: what is not known, one sentence.
3. Method: what you did, with the key parameters, one to two sentences.
4. Result: the primary number with its uncertainty, one sentence.
5. Interpretation: what it implies, with the hedge placed at the inferential
   link, one sentence.
6. Implication or limitation: what would change the reading, one sentence.

Then check: is the number in sentence 4 present in the Results section, with the
same value and the same uncertainty? An abstract that reports a number the
Results do not contain is the most common form of unintended overclaim.

## 6. Consistency across the paper

The abstract, the title and the conclusion are three renderings of the same claim
at three lengths, and they must agree in four respects: the value, the
uncertainty, the scope and the hedge. The demonstration's numbers give the reason
to be systematic about it: with $47.5\%$ of abstracts over a typical limit, many
are cut late, after the numbers have stabilised, and the cuts fall
disproportionately on uncertainty language. Write the abstract from the finished
Results, never from the plan.

## Assumptions and regime of validity

1. **The corpus is synthetic.** The flag probabilities were chosen to describe
   plausible behaviour and are not estimates of any real corpus.
2. **Structured abstracts are a convention with variants.** The headings differ
   between journals and fields, and the measured advantage depends on the template
   used.
3. **Word limits are journal-specific and enforced mechanically.** A limit that
   counts characters behaves differently from one that counts words.
4. **The spin model is a single probability.** Real spin is heterogeneous and
   includes changes of emphasis, not only deletion of hedges.
5. **Titles are also judged by non-textual signals.** Journal, author and citations
   influence reading decisions and are outside this measurement.

## The honest summary

Titles and abstracts are retrieval devices with hard budgets. The measurements
here put numbers on three habits: only $16.8\%$ of titles name all four elements,
structure raises abstract content by $14.5$ percentage points, and uncertainty
language appears $1.35$ times more often on strong results than weak ones. The one
rule worth memorising is consistency: whatever number the abstract states must be
findable, with the same uncertainty, in the Results.

## Python demonstration

[`code/writing_abstracts_titles_demo.py`](./code/writing_abstracts_titles_demo.py)
prints four labelled sections: abstract length and the effect of a hard limit; the
content flags by structure; the hedging and spin calculation; and the title
concreteness scores.

```bash
cd 24-research-papers-writing/02-scientific-writing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python writing_abstracts_titles_demo.py
```

## Exercises

Problems are in
[`exercises/05-writing-abstracts-titles-exercises.md`](./exercises/05-writing-abstracts-titles-exercises.md),
worked answers in
[`exercises/05-writing-abstracts-titles-solutions.md`](./exercises/05-writing-abstracts-titles-solutions.md).

## Mastery checkpoint

1. Write four candidate titles for your paper, one with each element omitted, and
   state what each omission costs a searcher.
2. Write your abstract as the six sentences of §5, then count words and cut to
   your limit by deleting a sentence rather than trimming adjectives.
3. Mark the one quantitative claim and confirm it appears in Results with the same
   value and uncertainty.
4. Check every hedge: is it at the inferential link?
5. Re-read the title after the abstract and delete any element the abstract
   already makes redundant.

## Common pitfalls

1. **Trimming adjectives to fit a limit.** The words are in whole sentences; cut
   content, not modifiers.
2. **Announcing a result without a number.** "We find improved resolution" tells a
   reader nothing to evaluate.
3. **Dropping the uncertainty from a null result.** It is the case where the
   interval matters most.
4. **A title that only names the topic.** It competes with every paper on the same
   topic.
5. **Abstract numbers that the Results do not contain.** Usually a late edit; it is
   a correctness problem, not a style problem.
6. **Using the abstract as the source of a citation.** Cite the paper's result, not
   its advertisement; see
   [24-06-04 Citation Practice and Attribution](../06-reproducible-publication/04-citation-and-attribution.md).

## Where this is used

- **Submission:** titles and abstracts are the fields most often returned for
  correction, and the ones most often read.
- **Conference submissions:** the same six sentences, cut to $250$ words, are the
  abstract you submit months before the paper exists.
- **Search and indexing:** keyword-bearing titles and abstracts determine whether
  your work is found; see
  [24-01-04 Systematic Literature Search](../01-reading-research-literature/04-literature-search.md).
- **Talks and posters:** the same concrete-claim discipline governs a title slide;
  see
  [24-04-01 Conference Talks](../04-presentation-and-communication/01-conference-talks.md).

## Related lessons

- [24-02-06 Figures, Captions and Self-Contained Visual Arguments](06-figures-and-captions.md) —
  the other part of a paper read before the text.
- [24-02-04 Writing Results and Discussion Without Overclaiming](04-writing-results-discussion.md) —
  where the claim being compressed is produced.
- [24-04-04 Communicating Uncertainty to Non-Specialists](../04-presentation-and-communication/04-communicating-uncertainty.md) —
  compression with a non-expert reader.
- [24-05-01 Writing a Compelling Research Proposal](../05-thesis-and-proposals/01-research-proposal.md) —
  the same concreteness applied to a promise rather than a result.

## Self-assessment checklist

- [ ] I can write a title containing all four elements and justify each.
- [ ] I can cut an abstract to a limit by removing content, not modifiers.
- [ ] I can name the three elements structure most improves.
- [ ] I can spot spin in my own abstract.
- [ ] I can verify that every abstract number appears in the Results.
- [ ] I can say what a title and abstract cannot establish.
