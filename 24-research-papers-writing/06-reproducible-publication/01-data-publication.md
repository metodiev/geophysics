---
id: 24-06-01
title: "Publishing Data and Code Alongside Papers"
level: research
prereqs: ["24-03-04", "22-02-05"]
estimated_minutes: 60
tags: [open-data, code, publication, metadata, reproducibility, formats]
---

# Publishing Data and Code Alongside Papers

Publishing data and code is a **packaging problem with a measurable payoff**: the
record you deposit determines who can reuse it, and reuse is a function of the
metadata as much as of the data. This lesson measures both — how complete typical
records are, what completeness buys in expected reuse, and where the bytes live when
formats age.

The organising idea is that **a deposit is a document, not a folder**. The data are
the payload; the metadata are the instructions for use; the identifiers are the
address. A deposit whose payload is excellent and whose instructions are missing is,
for practical purposes, unavailable — and the demonstration's arithmetic shows how
much each missing field costs.

> **Data provenance.** All numbers are **SYNTHETIC**. The deposits, their metadata
> fields, sizes and the reuse model are generated with chosen probabilities; no
> repository was queried and no real deposit is described. The format list is
> generic and the "preservation-friendly" classification is a chosen teaching
> convention, not a standard.

## Learning objectives

By the end of this lesson you will be able to:

1. **List** the metadata fields a reusable deposit needs and **state** what each one
   prevents.
2. **Compute** a completeness score for a set of deposits and **interpret** its
   spread.
3. **Model** reuse as a function of completeness and **quantify** the gain from
   fixing a single field.
4. **Classify** file formats by preservation risk and **compute** the share of bytes
   at risk, not just the share of files.
5. **Package** a deposit so that one command reproduces the paper's main result.
6. **State** what a deposit cannot provide: the context, the judgement and the
   negative results that never made it into a figure.

## Prerequisites

- [24-03-04 Reproducible Research Practice End to End](../03-research-methods-and-rigour/04-reproducible-research-practice.md) —
  the digest and provenance practice this lesson packages.
- [22-02-05 Data Versioning](../../22-data-engineering-reproducibility/02-reproducible-workflows/05-data-versioning.md) —
  how the inputs are pinned.

## 1. The metadata that makes a deposit usable

The demonstration uses twelve fields with chosen presence probabilities. Read the
list as answers to a user's questions:

| Field | The question it answers | Measured presence |
|---|---|---|
| Title | What is this? | $99.2\%$ |
| Creators and affiliations | Who made it, and whom do I cite? | $97.5\%$ |
| Licence | May I use it, and how? | $71.7\%$ |
| Methods description | How was it produced? | $69.2\%$ |
| Instrument and settings | With what, and at what settings? | $60.0\%$ |
| Spatial coverage | Where? | $76.7\%$ |
| Temporal coverage | When? | $57.5\%$ |
| Processing level | Raw, corrected, or derived? | $56.7\%$ |
| File format description | How do I read the bytes? | $48.3\%$ |
| Units and conventions | What do the numbers mean? | $50.0\%$ |
| Related identifiers | What else does this depend on? | $35.0\%$ |
| Version and provenance | Which version is this, and what changed? | $47.5\%$ |

Mean completeness per deposit is $64.1\% \pm 12.4\%$; one deposit in $120$ has all
twelve fields and $5.8\%$ have fewer than half. That spread is the finding: a reader
cannot predict from the repository which records will be usable, so each one must be
checked.

**The two fields that decide usability.** A licence (may I use it?) and a file-format
description (how do I read it?) are not optional extras. A deposit without a licence
is legally unusable by default in most jurisdictions, and a deposit whose binary
format is undocumented is technically unusable however open the licence.

## 2. What completeness buys

Modelling reuse as a linear function of completeness,

$$p_{\text{reuse}} = 0.05 + 0.70 \times \text{completeness},$$

the demonstration's $120$ deposits imply $59.8$ expected reuses, against $56$ observed
under the model's own coin flips. Grouping by completeness:

| Completeness | Deposits | Mean completeness | Expected reuses |
|---|---|---|---|
| $0$–$50\%$ | $7$ | $38.1\%$ | $2.2$ |
| $50$–$75\%$ | $76$ | $59.8\%$ | $35.6$ |
| $75$–$100\%$ | $37$ | $77.9\%$ | $22.0$ |

The function is linear by construction, and that is the honest status of the number:
it is a **model**, and the transferable claim is structural — reuse depends on the
record, so metadata work is not administrative overhead but the difference between a
deposit that is used and one that is not.

**Fixing one field.** Adding the weakest field (related identifiers, present in
$35.0\%$ of deposits) to every record raises each deposit's completeness by

$$\frac{100}{12} = 8.3\ \text{percentage points}$$

and, in the demonstration, expected reuses from $59.8$ to $64.4$ — a gain of $7.6\%$.
Every field contributes the same marginal amount, so the practical rule is to fix the
one that is cheapest for you: for a field dataset, the related identifiers and the
instrument settings are usually the fastest to fill from your own logs.

## 3. Formats and the bytes at risk

The demonstration's corpus uses ten formats with chosen shares and mean sizes:

| Format | Share | Mean size | Preservation-friendly |
|---|---|---|---|
| csv | $22.0\%$ | $40\ \mathrm{MB}$ | yes |
| netcdf | $18.0\%$ | $900\ \mathrm{MB}$ | yes |
| geotiff | $14.0\%$ | $300\ \mathrm{MB}$ | yes |
| hdf5 | $10.0\%$ | $700\ \mathrm{MB}$ | yes |
| seg-y | $8.0\%$ | $2500\ \mathrm{MB}$ | yes |
| json | $7.0\%$ | $5\ \mathrm{MB}$ | yes |
| xlsx | $8.0\%$ | $12\ \mathrm{MB}$ | no |
| docx | $6.0\%$ | $2\ \mathrm{MB}$ | no |
| proprietary binary | $5.0\%$ | $1800\ \mathrm{MB}$ | no |
| png | $2.0\%$ | $3\ \mathrm{MB}$ | yes |

The result that matters is the difference between counting files and counting bytes:

$$\text{friendly deposits} = 81.0\%, \qquad
\text{friendly bytes} = 84.5\%.$$

Here the two are close; in practice the specialist or proprietary formats hold the
*large* files, so the byte share understates the risk relative to the file share, and
it is the bytes that carry the seismic and potential-field data a reader most wants.

**The practical rule.** Deposit in a documented, open format, and provide the
conversion script and the description of anything lossy. A SEG-Y file with a written
header description and a reader script is more usable than a proprietary container
with a viewer, because the first survives the company.

## 4. The deposit as a reproducible artefact

A deposit that reproduces the paper's main result contains:

1. **Raw data**, immutable, with a checksum per file.
2. **Derived data**, regenerated by the code — never hand-edited.
3. **Code**, importable and tested, with the version recorded.
4. **Parameters**, in one file with units and comments.
5. **Environment**, pinned; see
   [22-02-02 Environment Pinning](../../22-data-engineering-reproducibility/02-reproducible-workflows/02-environment-pinning.md).
6. **One entry point** that regenerates every reported number, and a **README** that
   states the command and the tolerance.
7. **A licence**, chosen deliberately for the data and for the code separately, since
   the appropriate licences differ.
8. **A manifest**, listing files with sizes and checksums, so a partial download is
   detectable.

The manifest is the least common and the most useful: it converts "I downloaded it"
into "I downloaded the version you described", which is the whole point of a deposit.

## Assumptions and regime of validity

1. **The fields, rates and reuse model are synthetic.** Real repositories mandate
   different fields and real reuse depends on the community's habits.
2. **The format classification is a convention.** "Preservation-friendly" means open,
   self-describing and widely implemented; formats move between categories as tools
   change, and a legacy format with a documented specification can be safer than a
   new one without.
3. **Completeness is not correctness.** A field can be present and wrong, and the
   model does not distinguish them.
4. **Reuse is not the only value.** Some datasets are deposited for provenance rather
   than for reuse, and for those the metadata requirement is different and smaller.
5. **Deposits age.** A deposit that resolves today may not resolve in twenty years if
   it is behind a licence or a platform; that is the subject of
   [02 DOIs, ORCID and Persistent Identifiers](02-persistent-identifiers.md).

## The honest summary

Mean completeness in the demonstration is $64.1\%$ with a standard deviation of
$12.4$ points, one deposit in $120$ is complete, and fixing the weakest field raises
expected reuse by $7.6\%$. Eighty-one per cent of deposits and $84.5\%$ of bytes use
preservation-friendly formats here — and in real corpora the bytes are the worse
number, not the better one. The deposit is a document: write its instructions.

## Python demonstration

[`code/data_publication_demo.py`](./code/data_publication_demo.py) prints four
labelled sections: metadata completeness across the corpus; the reuse model with its
grouping; the effect of fixing the weakest field; and format longevity with the byte
share.

```bash
cd 24-research-papers-writing/06-reproducible-publication/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_publication_demo.py
```

## Exercises

Problems are in
[`exercises/01-data-publication-exercises.md`](./exercises/01-data-publication-exercises.md),
worked answers in
[`exercises/01-data-publication-solutions.md`](./exercises/01-data-publication-solutions.md).

## Mastery checkpoint

1. Score your last deposit against the twelve fields and list the missing ones.
2. Compute its completeness and the modelled reuse probability.
3. List the formats you deposit in and mark each as preservation-friendly or not,
   weighting by size.
4. Write the manifest with checksums for the main files.
5. Write the README's first three lines: what it is, the command, and the tolerance.

## Common pitfalls

1. **Depositing a folder and calling it a dataset.** Without a format description and
   a licence, the bytes are not usable.
2. **No licence.** Defaults are restrictive; state the terms or the data cannot be
   reused.
3. **Hand-edited derived files.** They break the regeneration claim silently.
4. **No manifest or checksums.** A partial or corrupted download is undetectable.
5. **Ignoring the byte-share risk.** The big files are usually in the fragile formats.
6. **No README command.** A deposit without an entry point makes the reader reconstruct
   the workflow.

## Where this is used

- **Every paper with data or code:** the deposit is the artefact that makes the paper
  checkable; see
  [24-03-04 Reproducible Research Practice End to End](../03-research-methods-and-rigour/04-reproducible-research-practice.md).
- **Data-management plans:** the fields and the licence are decided at the start, not
  at submission; see
  [22-05-04 Research Data Management Plans](../../22-data-engineering-reproducibility/05-collaboration-and-project-management/04-research-data-management-plan.md).
- **Reuse by others:** the metadata is what a stranger has; see
  [21-09-03 Data Ethics in the Geosciences](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/03-data-ethics-geoscience.md).
- **Repository and journal policy:** the fields here are the ones policies mandate,
  and the reasons are the questions in §1.

## Related lessons

- [24-06-02 DOIs, ORCID, Persistent Identifiers and Data Repositories](02-persistent-identifiers.md) —
  how a deposit is addressed and cited.
- [24-06-03 Interactive Publications and Notebooks as Articles](03-notebooks-as-publications.md) —
  the code-side container and its hazards.
- [24-06-04 Citation Practice and Attribution of Data and Software](04-citation-and-attribution.md) —
  what happens to a deposit's credit.
- [22-03-01 Scientific File Formats](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/01-file-formats-scientific.md) —
  the format landscape in detail.

## Self-assessment checklist

- [ ] I can list the twelve fields and the question each answers.
- [ ] I can compute a completeness score and interpret the spread.
- [ ] I can model reuse and quantify the gain from one field.
- [ ] I can classify formats and compute the byte share at risk.
- [ ] I can assemble a deposit with a manifest and one entry point.
- [ ] I can state what a deposit cannot provide.
