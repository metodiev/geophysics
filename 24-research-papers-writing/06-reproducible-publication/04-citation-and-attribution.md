---
id: 24-06-04
title: "Citation Practice and Attribution of Data and Software"
level: advanced
prereqs: ["24-06-02", "22-01-05"]
estimated_minutes: 45
tags: [citation, attribution, credit, data, software, bibliometrics]
---

# Citation Practice and Attribution of Data and Software

Citation is the mechanism by which scientific work becomes visible, and it has a
measurable gap: the infrastructure a result depends on — datasets, code, instruments,
archives — is used almost universally and cited much less often. This lesson measures
the gap and the distribution it operates in, then states the practices that close it.

The organising idea is that **citation is a pointer with legal and social force**. A
citation records a dependency, assigns credit, and — through the identifier system —
makes the dependency retrievable. An uncited dependency is invisible to every index
built from the literature, which is why the omission matters even when the authors'
intentions are good.

> **Data provenance.** All numbers are **SYNTHETIC**. Citation counts are drawn from
> a chosen heavy-tailed distribution, and the citation rates for data and software are
> chosen teaching values; no bibliometric database was queried and no real paper,
> dataset or package is described.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** a citation distribution by its centre, spread and inequality, and
   **explain** why the mean describes no paper.
2. **Estimate** a power-law exponent from a complementary cumulative distribution and
   **state** the limits of the estimate.
3. **Compute** the attribution gap for data and software from stated citation rates.
4. **Quantify** the credit a dependency loses when it is used but not cited.
5. **Apply** a citation checklist to a manuscript so that every dependency is a
   pointer.
6. **State** what citation counts measure and what they cannot be used to decide.

## Prerequisites

- [24-06-02 DOIs, ORCID, Persistent Identifiers and Data Repositories](02-persistent-identifiers.md) —
  the identifiers that make a citation resolvable.
- [22-01-05 Licensing and Citation](../../22-data-engineering-reproducibility/01-research-software-engineering/05-licensing-and-citation.md) —
  the licence side, which is the legal counterpart of attribution.

## 1. The distribution citations live in

The demonstration's $800$ synthetic papers, drawn from a lognormal with median $12$
and log-scale standard deviation $1.30$:

| Quantity | Value |
|---|---|
| Mean citations | $25.8$ |
| Median citations | $12$ |
| Ratio mean/median | $2.25$ |
| Top $10\%$ share of citations | $49.1\%$ |
| Papers with no citations | $0.2\%$ |
| Gini coefficient | $0.632$ |

The mean is more than twice the median and a tenth of the papers hold $49.1\%$ of the
citations. Two consequences for practice. First, a citation *is* the mechanism by
which a work enters this distribution at all — the difference between zero and one is
qualitative, not marginal. Second, any summary of credit should report the
distribution: the top-decile share and the median together say more than a total.

## 2. A slope, estimated rather than assumed

Fitting a straight line to the log of the complementary cumulative distribution over
the $798$ papers with at least one citation gives

$$\text{slope} = -0.713, \qquad \alpha = -\text{slope} + 1 = 1.713,$$

fitted over the range $1$ to $661$ citations. The estimate is reported with three
caveats, all of which belong in any real use:

- **A lognormal is not exactly a power law.** The generator is lognormal by
  construction, so the fitted exponent describes the tail's local behaviour over the
  fitted range and nothing more.
- **The fit depends on the range.** Including or excluding the smallest counts changes
  the slope, which is why the range must be stated.
- **An exponent is not a mechanism.** Preferential attachment, heterogeneity in
  quality and field size all produce heavy tails; the slope does not distinguish them.

The honest use of such a number is descriptive and comparative — "this corpus's tail
is heavier than that one's over the same range" — never as a constant quoted without
its range and model.

## 3. The attribution gap

The demonstration models $800$ papers: $85\%$ use a dataset, $95\%$ use software, and
formal citations are given with probabilities $0.42$ (data) and $0.35$ (software):

| | Uses | Cites | Gap |
|---|---|---|---|
| Data | $671$ | $298$ ($44.4\%$ of uses) | $373$ uses without a traceable citation |
| Software | $762$ | $266$ ($34.9\%$ of uses) | $496$ uses without a traceable citation |

Roughly two-thirds of software uses and more than half of data uses leave no citation.
The modelled additional factor — a software paper accruing about $0.25$ of the
citations of a method paper — compounds the effect, because infrastructure is both
cited less and credited less when it is cited.

## 4. What an uncited dependency loses

With a mean of $25.8$ citations per paper and $800$ papers, the corpus total is about
$20\,669$ citations. Under the demonstration's rates:

| Dependency | Credited citations | Share of corpus | Uncredited |
|---|---|---|---|
| Software | $1809$ | $8.75\%$ | $3359$ |
| Data | $8681$ | $42.0\%$ | $11\,988$ |

The second column is the number the index sees; the fourth is the number that used the
thing without recording it. The absolute figures follow from the chosen rates, but the
mechanism is real and it is why infrastructure funding and maintenance are chronically
under-justified: the evidence of use exists in the papers' methods, not in their
reference lists.

## 5. A citation checklist

Before submission, check that each of the following is cited by identifier, not
described:

1. **Datasets** — with the version DOI and the accession, in the Data Availability
   statement and in the text where first used.
2. **Software** — with the release and the version, and with the repository where the
   authors ask for citations to be recorded.
3. **Instruments and archives** — with the community's convention, stated once.
4. **Methods taken from prior work** — including your own prior work, whether or not
   the text is reused; see
   [24-03-06 Research Ethics, Plagiarism, Authorship and Integrity](../03-research-methods-and-rigour/06-research-ethics.md).
5. **Standards and conventions** — the version of the standard, not the manual you
   happen to use.
6. **Derived products** — the intermediate dataset, if a reader needs it to reproduce
   your result.

The checklist is short and it is the entire practice: a dependency that is not cited
cannot be counted, and one that is cited with a version can be reused.

## Assumptions and regime of validity

1. **The distribution and rates are synthetic.** Real citation practices vary by field
   by an order of magnitude, and citation counts differ correspondingly.
2. **Citation counts measure attention, not quality.** A citation may be critical,
   perfunctory or self-serving; the bibliometric literature is extensive and should be
   consulted before any evaluation.
3. **The software penalty is a single modelled factor.** Real software citation
   practice is changing rapidly and varies by community.
4. **The exponent is a local fit.** It describes one generated sample over one range.
5. **Attribution is a norm, not an enforcement mechanism.** Nothing in a reference
   list compels correct citation; the practices here are professional obligations, and
   licences and requirements are the binding instruments.

## The honest summary

Citations are heavy-tailed (mean $2.25$ times the median, Gini $0.632$, top decile
holding $49.1\%$), and the fitted exponent over the stated range is $1.713$ — a local
description, not a constant. Two-thirds of software uses and more than half of data
uses are uncited in the demonstration, which costs infrastructure the visibility of
about $3359$ and $11\,988$ citations respectively. Cite the version, cite the release,
and cite by identifier.

## Python demonstration

[`code/citation_and_attribution_demo.py`](./code/citation_and_attribution_demo.py)
prints four labelled sections: the citation distribution with its inequality; the
power-law fit from the complementary cumulative distribution; the attribution gap for
data and software; and the credit lost by uncited dependencies.

```bash
cd 24-research-papers-writing/06-reproducible-publication/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python citation_and_attribution_demo.py
```

## Exercises

Problems are in
[`exercises/04-citation-and-attribution-exercises.md`](./exercises/04-citation-and-attribution-exercises.md),
worked answers in
[`exercises/04-citation-and-attribution-solutions.md`](./exercises/04-citation-and-attribution-solutions.md).

## Mastery checkpoint

1. Take a paper you have published: list every dataset, package and archive you used,
   and mark which you cited.
2. Compute your own gap: uses recorded, citations given.
3. Write the citations you would add, with identifiers and versions.
4. Check that each identifier resolves.
5. Record the distribution of your own citation counts (median, top-decile share) so
   that you never quote a mean in isolation.

## Common pitfalls

1. **Acknowledging instead of citing.** "We thank the X project" is not a citation and
   does not enter any index.
2. **Citing the project, not the release.** The reader cannot tell which version
   produced your numbers.
3. **Citing software only in the text.** The reference list is where indexes look.
4. **Omitting your own prior work.** It is the work you are most likely to describe
   without citing, and it is a conduct issue as well; see
   [24-03-06 Research Ethics, Plagiarism, Authorship and Integrity](../03-research-methods-and-rigour/06-research-ethics.md).
5. **Treating citation counts as quality.** They measure attention; see
   [24-05-04 Academic CVs, Research Statements and Career Paths](../05-thesis-and-proposals/04-cv-and-career.md).
6. **Quoting an exponent without its range.** The fit changes with the range, and the
   number without it is not reproducible.

## Where this is used

- **Every manuscript:** the checklist is a pre-submission step.
- **Data and software maintenance:** citation is the visibility that justifies
  continued funding of infrastructure.
- **Metrics discussions:** the distributional facts are the basis for any argument
  about indices; see
  [24-05-04 Academic CVs, Research Statements and Career Paths](../05-thesis-and-proposals/04-cv-and-career.md).
- **Repository and journal policy:** citation requirements are set at the venue level,
  and a venue that requires software citation for its own archive is demonstrating the
  norm.

## Related lessons

- [24-06-01 Publishing Data and Code Alongside Papers](01-data-publication.md) —
  what there is to cite.
- [24-06-02 DOIs, ORCID, Persistent Identifiers and Data Repositories](02-persistent-identifiers.md) —
  the identifiers that make a citation resolvable.
- [24-01-04 Systematic Literature Search and Reference Management](../01-reading-research-literature/04-literature-search.md) —
  the library side of the same records.
- [22-01-05 Licensing and Citation](../../22-data-engineering-reproducibility/01-research-software-engineering/05-licensing-and-citation.md) —
  the licence requirements that accompany attribution.

## Self-assessment checklist

- [ ] I can describe a citation record by centre, spread and inequality.
- [ ] I can fit a slope and state its range, model and limits.
- [ ] I can compute an attribution gap from stated rates.
- [ ] I can quantify the credit an uncited dependency loses.
- [ ] I can apply the citation checklist to a manuscript.
- [ ] I can state what citation counts cannot be used to decide.
