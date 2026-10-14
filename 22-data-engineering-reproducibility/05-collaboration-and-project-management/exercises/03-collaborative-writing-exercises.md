# Exercises — 22-05-03 Collaborative Writing with LaTeX and Markdown

Attempt these before reading the
[solutions](./03-collaborative-writing-solutions.md). The lesson is
[03 Collaborative Writing with LaTeX and Markdown](../03-collaborative-writing.md).
Numbers refer to the **SYNTHETIC** model of `code/collaborative_writing_demo.py`:
8 000 words, 12 words per wrapped line, 18 words per sentence, three-line merge context,
four editors.

## ★ Foundational

**★1.** Explain in two sentences why a line-based merge treats prose differently from
code, and name the LaTeX-specific complication.

**★2.** For the 8 000-word manuscript: (a) compute the line counts under both
conventions; (b) compute the ratio of the diff sizes; (c) state which convention gives
the smaller diff *per edit* and why.

**★3.** State the conflict probability at 5, 10 and 20 lines of separation for
hard-wrapped prose and for sentence-per-line writing, and name the quantity that
explains the difference.

## ★★ Applied

**★★4.** A manuscript of 12 000 words is written by five authors, each editing two
sections of roughly 1 200 words.

(a) Compute each author's number of hard-wrapped lines and of sentences. (b) State
which convention you would adopt and the reason in terms of edit regions. (c) State the
second convention (beyond line breaks) that would further reduce conflicts.

**★★5.** Four editors work on the same document, two sessions a week each, and the
pairwise conflict probability at their typical separation is 0.7.

(a) Compute the probability that a session conflicts with at least one other. (b) State
the change that reduces it most. (c) State the mechanism by which that change works.

**★★6.** A repository for a submitted paper contains: LaTeX sources, the compiled PDF,
eight PNG figures without code, a `.bib` file, `*.aux` and `*.log` files, and a
`figures/` directory with the manuscript's figures.

(a) State what should be tracked and what excluded, with a reason each. (b) State the
two items that make the figures unreproducible and the fix for each. (c) State what the
submission's tag should point at.

## ★★★ Research-oriented

**★★★7.** Design a manuscript repository and build for a 40-page report with 12 authors
across three institutions: state the file layout, the conventions, the build command and
its pinned environment, the CI checks, the figure regeneration, the review workflow, and
the artefact linking the text to code and data. State the one thing your design makes
hard.

**★★★8.** Design a measurement of a real manuscript's collaboration friction: state the
data (commit history with diffs, conflict records), the statistics (diff size per
semantic change, conflict rate per file and per week, time to merge), and the confounder
(author habits, deadlines). State what the measurement cannot tell you about the paper's
quality.

**★★★9.** A group wants to move from a word processor to text sources while four authors
are mid-paper. Propose the migration: state the conversion steps, the conventions to
adopt, the training the co-authors need, the risks (a lost week before a deadline), and
the criterion that would tell you to abandon the migration and go back.
