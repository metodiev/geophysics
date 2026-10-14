# 24 — Research Papers, Scientific Writing and Communication

**Stages:** intermediate → research

This folder covers the part of research that is not the physics: reading the
literature, writing a paper people can use, designing a study that can answer a
question, presenting the result to four different audiences, asking for money, and
publishing the artefacts a result depends on. Its organising principle is that
these activities are **measurable**, and that measuring them is more useful than
admonishing about them. A triage rule has a precision and a recall. A query has a
recall and an hour cost. A discussion section has a $p$-value and an effect size,
and they move apart as sample size grows. A proposal has a weighted score, a
margin at the funding line and a sensitivity to the weighting scheme. A poster has
a minimum text height for its viewing distance. A deposit has a completeness score,
and a citation has a version.

The central honest difficulty in this folder is that **every one of these
quantities is a property of a process, not of a person**. The funding line is set
by the funding rate; the review panel's spread is a property of the instrument;
two readers of the same proposal disagree at $\kappa = 0.45$; a $160$-cell notebook
has a $77\%$ chance of containing hidden state regardless of who wrote it. The
lessons report those numbers because they convert anxiety into arithmetic — you
cannot fix a funding rate, but you can revise rather than rewrite a proposal once
you know that the expected submissions per award fall from $8.3$ to about $4.5$;
you cannot remove reviewer noise, but you can stop reading a rejection as a verdict
once you know the uncertain band around the boundary is $\pm 0.26$ points wide and
holds a fifth of the applications.

A second theme is that **containers constrain claims**. A paper's four sections
carry different licences; a $12$-minute talk holds $1560$ spoken words, $8$ slides
and about four retained ideas; a poster read at $1.5\ \mathrm{m}$ needs $12.8\
\mathrm{mm}$ text and holds about $100$ words; a headline is a $500\!:\!1$
compression of a paper in which $1.07$ of $6$ qualifiers survive four retellings; a
thesis claims contributions it must be able to support with words somewhere. Every
lesson measures what the container can carry and what it costs to exceed it,
because the failure mode is always the same: putting the argument in the channel
that is about to be compressed, capped, skipped or retold.

A third theme is **consistency between the claim and the evidence, at every
length**. The same claim is rendered as a title, an abstract, a talk, a poster, a
proposal and a public message, and each rendering has its own way of drifting.
This folder's habit is to check the renderings against each other: the number in
the abstract must appear in the Results, the qualifier must be in the same clause
as the number, the contribution statement must be traceable to chapters, the
availability statement must resolve.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Read** a paper as a structured argument, **measure** its proportions, and
   **triage** a literature at a stated precision, recall and hour cost.
2. **Audit** a paper's reporting, **compute** joint compliance and **explain** why
   it is governed by the weakest required item.
3. **Write** at four lengths — title, abstract, paper, release — so that the claim
   and its uncertainty survive each compression.
4. **Rank** the parameters of a method by influence, **state** the reproduction
   tolerance you claim, and **measure** what a $1\%$ change does to the reported
   digits.
5. **Separate** significance, effect size and precision, and **compute** the
   inflation that selection and flexibility induce.
6. **Formulate** an answerable question, **write** a falsifiable hypothesis, and
   **fix** a design in three numbers before the data arrive.
7. **Quantify** a review panel's reliability, a funding line's noise band and a
   rubric's sensitivity to weights.
8. **Design** a talk, poster, examination preparation or public message from its
   budget rather than from taste, and **state** what each format cannot carry.
9. **Publish** data, code and a reproducibility claim so that a stranger can check
   them, with identifiers, versions, licences and a manifest.
10. **State** what each metric in this folder does not measure, and refuse to use
    it for a decision it cannot support.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Topic | Lessons |
|---|---|---|---|
| 01 | [Reading the Research Literature](./01-reading-research-literature/README.md) | Anatomy of a paper; the four reading passes; critiquing methods, data and inference; systematic search and reference management; keeping up with the stream | 5 |
| 02 | [Scientific Writing](./02-scientific-writing/README.md) | Clear prose as measurement; IMRaD and its variants; reproducible Methods; Results and Discussion without overclaiming; abstracts and titles; figures and captions; revision and response to reviewers | 7 |
| 03 | [Research Methods and Scientific Rigour](./03-research-methods-and-rigour/README.md) | Answerable questions; hypotheses and falsifiability; study design; reproducibility end to end; peer review; ethics, plagiarism and authorship | 6 |
| 04 | [Presentation and Science Communication](./04-presentation-and-communication/README.md) | Conference talks; posters; seminars, qualifying exams and defence; communicating uncertainty; public engagement, media and policy | 5 |
| 05 | [Theses, Proposals and Career Documents](./05-thesis-and-proposals/README.md) | Research proposals; thesis structure and the contribution statement; grant funding and review criteria; CVs, research statements and career paths | 4 |
| 06 | [Reproducible Publication and Open Data](./06-reproducible-publication/README.md) | Publishing data and code; persistent identifiers and repositories; notebooks as articles; citation practice and attribution | 4 |

**31 lessons**, each with a graded exercise set, a worked solution set, and a
print-only demonstration.

## Suggested paths

**If you are starting a research project:** 24-01-01 → 24-01-02 → 24-03-01 →
24-03-03. Read a paper properly, triage the literature, write the question, then fix
the design in three numbers. Everything later in the folder depends on those four
lessons.

**If you are writing your first paper:** 24-02-01 → 24-02-02 → 24-02-03 → 24-02-05.
Structure, then Methods, then the abstract and title; the figures lesson
(24-02-06) is worth an hour because two thirds of readers see only those.

**If you are revising under review:** 24-02-07 → 24-02-04 → 24-03-05. The response
letter, the overclaiming checks, and the reviewer's perspective in that order.

**If you are presenting:** 24-04-01 for the talk, 24-04-02 for the poster, 24-04-04
for anything a decision-maker will read, and 24-04-05 if a journalist or a policy
audience is involved.

**If you are applying for funding or a job:** 24-05-01 → 24-05-03 → 24-05-04. Read
the scheme, compute the arithmetic of expected submissions, then write the documents
against the rubric.

**If you are depositing data or code:** 24-06-01 → 24-06-02 → 24-06-04, with
24-06-03 if the container is a notebook.

**If you are supervising:** 24-01-02 (triage), 24-03-02 §6 (pre-analysis plans),
24-05-02 §3 (contribution support) and 24-06-03 §5 (the notebook checklist) are the
four artefacts worth requiring, because each is a record rather than a promise.

## Mastery checkpoint for the folder

1. Triage a $20$-paper queue with a stated sensitivity and specificity, and report
   the precision you achieved.
2. Audit a published paper against a ten-item checklist and compute joint compliance
   for the four reproducibility-critical items.
3. Write a $250$-word abstract and a four-element title, then verify that every number
   appears in the Results with the same uncertainty.
4. Rank the parameters of a method you use by elasticity and state the tolerance at
   which you claim reproduction.
5. Write one Results sentence as estimate plus interval plus sample size, and one
   Discussion sentence with a falsification condition.
6. Plan a $12$-minute talk in words, slides and ideas, marking three optional slides.
7. Write a Data and Code Availability statement, with versions, that resolves.
8. For any metric you use in this folder, write the sentence "this does not measure
   …" and complete it.

## Conventions used throughout

- **Every lesson is self-contained but assumes its prerequisites**, which are linked.
- **Units and uncertainty accompany every number** produced, quoted or modelled, and
  every dataset is labelled **SYNTHETIC**, **OBSERVED** or **ILLUSTRATIVE**.
- **Every demonstration is print-only**: no figures, no display, no file I/O, no
  network, fixed seed, under ten seconds, exit 0. The numbers quoted in a lesson are
  the numbers its demonstration prints.
- **Bibliographic facts are limited to stable, well-established entries** — author,
  title, venue — and no DOI, URL or quotation is invented anywhere in this folder.

## A caution about numbers in this folder

Word budgets, reading rates, caption rates, elasticities, effect sizes, funding
rates, reviewer noise, similarity thresholds, metadata completeness and citation
statistics in this folder **vary** — with the field, the venue, the corpus, the
panel and the year. Where the folder gives a number it gives a *teaching value*
with its units and its provenance: a synthetic corpus generated by a demonstration
with chosen parameters, an exact mathematical result such as $\kappa$ or the
Spearman-Brown relation, or a stated published convention such as the ISO/IEC 7064
MOD 11-2 check-character scheme or the likelihood phrases used in IPCC assessment
reports. No number in this folder is presented with the authority of a measurement
of real papers, a real panel, a real audience, a real repository or a real
bibliometric database — because none was measured. Each demonstration says so in
its own header, and each lesson carries a provenance banner.

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 24-research-papers-writing/02-scientific-writing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python paper_structure_demo.py
```

The demonstrations are meant to be read as well as run: each is a short program
whose structure mirrors the lesson's argument, and each prints labelled sections
with units so that a reader can check any quoted number.

## Where this folder sits

Before it: [22 Data Engineering and Reproducibility](../22-data-engineering-reproducibility/README.md)
supplies the software practice that lesson 24-03-04 and module 24-06 package for
publication, and [23 Field Methods and Instruments](../23-field-methods-instruments/README.md)
supplies the data whose metadata module 24-06 makes usable.

Alongside it: [21 Statistics, Bayesian Methods and Machine Learning](../21-statistics-bayesian-ml/README.md)
supplies the inference that module 24-03 designs studies around, and
[26 Reference Library](../26-reference-library/README.md) catalogues the literature
that module 24-01 teaches you to read.

After it: [25 Projects and Capstone](../25-projects-capstone/README.md), where the
skills of this folder are exercised end to end on a real project — a proposal, a
study, a paper, a talk and a deposit.
