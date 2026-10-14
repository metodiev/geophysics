---
id: 22-05-03
title: "Collaborative Writing with LaTeX and Markdown"
level: advanced
prereqs: ["22-05-02", "22-01-02"]
estimated_minutes: 45
tags: [collaborative-writing, latex, markdown, version-control, collaboration]
---

# Collaborative Writing with LaTeX and Markdown

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a line-based merge treats prose and LaTeX differently from code,
   and **measure** the conflict probability of two edits.
2. **Choose** a formatting convention (hard-wrapped, sentence-per-line, semantic line
   breaks, one file per section) from the merge behaviour it produces.
3. **Compute** the diff size of the same manuscript under two conventions, and **state**
   what the size costs a reviewer.
4. **Design** a manuscript repository: what is tracked, what is excluded, how figures
   and references are handled, and how the compiled PDF is produced.
5. **Diagnose** the four writing-repository failures: a conflict over formatting, a
   binary in the history, a figure that cannot be regenerated, and a submission that
   cannot be rebuilt.
6. **State** the convention in the repository's contribution notes, in one page.

The manuscript sizes, edit regions and conflict probabilities in this lesson are
**SYNTHETIC** with chosen parameters; the conflict model is the line-overlap model of
[22-01-02](../01-research-software-engineering/02-version-control-git.md) applied to a
document. No real manuscript was parsed.

## Prerequisites

- [22-05-02 Issue Tracking, Milestones and Kanban for Research](./02-issue-tracking.md) —
  the review states this lesson's merges complete.
- [22-01-02 Version Control with Git](../01-research-software-engineering/02-version-control-git.md) —
  the merge machinery and its conflict geometry.

## 1. Intuition: a merge tool sees lines, not sentences

Version control merges text by **line**. Code is written one statement per line, so a
line is a coherent unit of change and a conflict is meaningful. Prose is written as
paragraphs, so a line may be a whole paragraph, and a merge tool then sees two edits
to "line 412" when two authors changed different sentences in it. LaTeX adds a second
complication: the source's line breaks are a formatting choice, and re-wrapping a
paragraph rewrites lines that contain no semantic change.

Two consequences follow. First, the conflict rate in collaborative writing is a
property of the **formatting convention**, not of the tool. Second, the reviewer's
cost is set by the **diff size**: a convention that produces large diffs for small
changes makes every review slower, and reviews are where the science is checked.

## 2. Two conventions for the same manuscript

The demonstration's **SYNTHETIC** manuscript is 8 000 words:

| Convention | Lines | Diff size relative to hard-wrapped |
|---|---|---|
| hard-wrapped paragraphs (≈12 words/line) | 667 | 1.00 |
| one sentence per line (≈18 words/sentence) | 444 | 0.67 |

The sentence-per-line convention is *not* smaller in total; it is smaller **per edit**,
which is what matters: changing one sentence rewrites one line instead of a paragraph's
worth of wrapped lines. The trade is that the source's appearance in a plain-text
editor is less paragraph-like, and a reader of the diff sees a sentence rather than a
paragraph — for review, that is usually an improvement.

## 3. Conflict probability, measured

Applying the line-overlap model with a three-line context and typical edit regions:

| Separation of the two edits (lines) | Hard-wrapped prose | Sentence per line |
|---|---|---|
| 0 | 1.000 | 1.000 |
| 5 | 1.000 | 1.000 |
| 10 | 0.846 | 0.066 |
| 20 | 0.004 | 0.000 |
| 40 | 0.000 | 0.000 |

The mechanism is the same as in code: a conflict occurs when two edit regions are closer
than the diff's context. Because a sentence-per-line edit region is roughly a quarter of
the size of a hard-wrapped paragraph's, its conflict distance is correspondingly shorter:
at 10 lines of separation the sentence convention conflicts 6.6 % of the time against
84.6 % for wrapped prose.

With several editors the probability that a session conflicts at all is

$$P(\text{any}) = 1 - (1 - p_{\text{pair}})^{n_{\text{sessions}} - 1},$$

which for four editors (eight sessions) is 1.000 at 5 lines of separation, 1.000 at 10,
0.026 at 20 and 0.000 at 50. The practical reading: **conflict is a function of
proximity**, and proximity is a function of the convention and of how the work is
divided. Assigning whole sections to authors, or using one file per section, moves the
edits far apart and makes the conflict rate negligible regardless of the tool.

## 4. What to track, and what to exclude

| Item | Track? | Why |
|---|---|---|
| LaTeX or Markdown sources | yes | the text is the artefact; diffs are meaningful |
| Figure source code and data identifiers | yes | the figure must be regenerable |
| Compiled PDF | no (usually) | a build product; commit it only as a release artefact |
| `*.aux`, `*.log`, `*.bbl`, `*.toc` | no | build intermediates; regenerate |
| Rendered figure images from code | as a release artefact | regenerable, but useful for review |
| Word-processor documents | no | not diffable or mergeable; convert to text sources |
| Reference library (`.bib`) | yes | it is a source; keep it under review |
| Obtained licences / permissions | yes | they are evidence |

The general rule is the one from
[22-02-04](../02-reproducible-workflows/04-notebooks-vs-pipelines.md) §5: track the
sources, exclude the products, and make the products reproducible from the sources. A
manuscript repository that tracks only the PDF can neither review nor reproduce.

## 5. Figures and references

Two recurring sources of unreproducible manuscripts:

1. **Figures pasted from a graphics program.** The figure exists; the code that made it
   does not. The fix is to generate every figure from tracked code and identified data,
   with the figure's caption naming both
   ([22-02-05](../02-reproducible-workflows/05-data-versioning.md) §5). The compiled
   document then depends on a workflow, not on an author's memory.
2. **References edited outside version control.** A shared bibliography that changes
   silently makes a submission non-reproducible; keep the `.bib` under review like the
   text, and record which version was used for a submission.

The build itself should be one command with a pinned environment
([22-02-02](../02-reproducible-workflows/02-environment-pinning.md)): the same sources
plus the same toolchain produce the submitted PDF, so "which version did we submit" is
answerable by a tag.

## 6. Practice: a one-page convention

1. **One sentence per line** (or semantic line breaks), so an edit's region is small.
2. **One section, one file** for long documents, so authors rarely touch the same file.
3. **Never reformat a whole file in the same commit as a content change.** A re-wrap or
   a whitespace change hides the science in the diff; do it as its own commit, or not at
   all.
4. **Review the diff, not the document.** Assign a reviewer per section, and read the
   diff with the compiled output beside it.
5. **Tag the submitted version** and archive it with the artefact, so the reportable
   version is identifiable
   ([22-01-05](../01-research-software-engineering/05-licensing-and-citation.md)).
6. **Automate the build and the figure regeneration** in CI so a broken cross-reference
   or a missing figure is caught before submission.
7. **State the convention** in the repository's contribution notes, with the reason (a
   smaller diff), because conventions survive on their rationale.

## 7. Worked example: a submission that cannot be rebuilt

A group submitted a paper and, two years later, must respond to a query about a figure.
The repository contains the LaTeX sources and the PDF, and the figures are PNGs
committed by an author.

1. **Can the paper be rebuilt?** Partially: the text compiles, the figures are whatever
   was committed, and no code regenerates them. The figure's provenance is the author's
   memory.
2. **Can the figure be re-derived?** Only if the analysis code and the data version are
   identifiable. If the code lives in another repository without a tag, and the data file
   is `final_data_v3.mat`, the answer is no.
3. **What would have prevented it?** Tracked figure code, a data identifier recorded in
   the caption, and a release tag linking the manuscript version to the code and data
   versions.
4. **What can be done now?** Reconstruct as much as possible, and state plainly in the
   response which parts were regenerated and which are the original committed images —
   the same honesty as
   [22-03-04](../03-data-formats-and-engineering/04-getting-earth-data.md) §7.

## Assumptions and regime of validity

1. **A line-based merge model.** The conflict probabilities come from the three-line
   context model; different merge tools and diff algorithms shift the numbers, and the
   ordering of the conventions is what transfers.
2. **Chosen manuscript parameters.** 8 000 words, 12 words per wrapped line and 18 per
   sentence are teaching values; a manuscript with equations has very different line
   statistics (a display equation is its own line and conflicts locally).
3. **Text-based sources.** Word-processor workflows are outside this model: they are not
   mergeable, and the lesson's advice is to convert or to accept a different process.
4. **Independent edits.** Correlated edits (co-authors revising the same argument) are the
   real case and are handled by section ownership, not by the model.
5. **No measurement of a real manuscript.** Nothing here describes a particular group's
   practice, and the numbers are properties of the model.

## The honest summary

Collaborative writing inherits the merge geometry of code with one twist: prose lines are
paragraph-sized, so an edit's region is large and conflicts are frequent. The measurements
are simple — 667 wrapped lines against 444 sentence-per-line lines for 8 000 words, a
sentence-per-line conflict probability of 0.066 against 0.846 at ten lines of separation —
and they point at conventions rather than tools: one sentence per line, one section per
file, never reformat and edit in the same commit. The repository should track sources and
exclude products, regenerate figures from tracked code and identified data, keep the
bibliography under review, tag the submitted version, and state the convention with its
reason in one page of contribution notes.

## Python demonstration

[`code/collaborative_writing_demo.py`](./code/collaborative_writing_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. the line counts under two conventions (667 and 444) and the 0.67× diff ratio;
2. the conflict-probability table from 0 to 40 lines of separation for both conventions;
3. the multi-editor probability, showing the dominance of proximity (1.000 at 10 lines,
   0.026 at 20);
4. the four formatting choices with their benefits and costs.

```bash
cd 22-data-engineering-reproducibility/05-collaboration-and-project-management/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python collaborative_writing_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/03-collaborative-writing-exercises.md`](./exercises/03-collaborative-writing-exercises.md)
and
[`exercises/03-collaborative-writing-solutions.md`](./exercises/03-collaborative-writing-solutions.md).

## Mastery checkpoint

Without notes: a manuscript of 12 000 words is written by five authors, each editing two
sections, with paragraphs of about 120 words.

1. Compute the number of hard-wrapped lines (12 words/line) and the number of sentences
   (18 words/sentence).
2. State which convention you would adopt and the reason in terms of edit regions.
3. State three items to track and three to exclude, with the reason for each.
4. State how you would make figure 2 reproducible, and what the caption must contain.

## Common pitfalls

1. **Reformatting in a content commit.** It hides the science in a whitespace diff.
2. **Tracking the compiled PDF as the artefact.** The sources are the artefact; the PDF
   is a build product.
3. **Figures without code.** The most common irreproducibility in manuscripts.
4. **A bibliography outside version control.** A silent reference change is
   unreproducible.
5. **Conventions in someone's memory.** Write them in the contribution notes with the
   rationale, or they decay with the author's departure.
6. **No tag for the submitted version.** "Which version did we submit" must have an
   answer.

## Where this is used

- **Paper and thesis writing** — the repository is the record, and the tag is the version
  of record: see
  [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md).
- **Proposals and reports** — the same conventions at a smaller scale, with deadlines that
  make conflicts expensive.
- **Teaching materials** — one file per lecture, with a build check that the examples
  still run.
- **Multi-institution collaborations** — section ownership and the convention are what make
  a shared repository workable.

## Related lessons

- [22-01-02 Version Control with Git](../01-research-software-engineering/02-version-control-git.md) —
  the merge geometry this lesson applies to prose.
- [22-05-02 Issue Tracking, Milestones and Kanban for Research](./02-issue-tracking.md) —
  the review stage a merge completes.
- [22-02-04 Notebooks vs Pipelines: Choosing the Right Tool](../02-reproducible-workflows/04-notebooks-vs-pipelines.md) —
  the same sources-versus-products rule for analysis.
- [22-05-04 Research Data Management Plans and FAIR Principles](./04-research-data-management-plan.md) —
  where the figure's data identifier is recorded.

## Self-assessment checklist

- [ ] I can explain why a merge tool treats prose differently from code.
- [ ] I can measure the conflict probability of an editing convention.
- [ ] I can choose a convention from the merge behaviour it produces.
- [ ] I can state what a manuscript repository should track and exclude.
- [ ] I can make a figure reproducible from tracked code and data.
- [ ] I can write the convention in one page of contribution notes.
