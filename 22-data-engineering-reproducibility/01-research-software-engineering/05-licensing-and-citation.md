---
id: 22-01-05
title: "Licensing, Citation and Software Credit (CITATION.cff)"
level: graduate
prereqs: ["22-01-04", "22-01-02"]
estimated_minutes: 45
tags: [licensing, citation, credit, open-source, research-software]
---

# Licensing, Citation and Software Credit (CITATION.cff)

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why code with no licence is not free to reuse, and **state** what a
   licence decision actually decides.
2. **Classify** licences as permissive, weak-copyleft or strong-copyleft, and
   **predict** the licence forced on a combined work.
3. **Audit** a dependency tree for licence constraints, and **state** which
   obligations attach to distribution rather than to internal use.
4. **Write** a `CITATION.cff` file and a software-availability statement that give
   a reader a resolvable identifier and an accurate author list.
5. **Compute** a version constraint's admissible release set, and **explain** why a
   paper must record the exact version it used.
6. **Account** for software credit explicitly, and **state** what a citation count
   does and does not measure.

This lesson is **not legal advice**. The licence table below is a small
**ILLUSTRATIVE** teaching model of well-documented licence families; the
citation curve is a **SYNTHETIC** model with chosen parameters. Before relying on
a licence conclusion, read the licence text, the SPDX licence list and the
compatibility notes, and ask whoever is responsible for your institution's
compliance.

## Prerequisites

- [22-01-04 Documentation, Docstrings and READMEs That Work](./04-documentation.md) —
  the artefact that carries the licence, citation and data provenance sections.
- [22-01-02 Version Control with Git](./02-version-control-git.md) — tags are the
  versions that licences and citations refer to.

## 1. Intuition: two independent questions

Reusing research software raises two questions that are often conflated:

- **May I use this legally?** That is the licence question, and it is about
  copyright, distribution and derivative works.
- **How do I give credit?** That is the citation question, and it is about
  identifiers, authorship and the scholarly record.

They are independent: a permissively licensed package can be uncitable (no
identifier, no authors stated), and a well-cited paper's code may carry no licence
at all, which makes it unusable by anyone else however famous it is. A complete
software release answers both, and answering neither has become one of the
recognised failure modes of computational science.

## 2. No licence is not "free to use"

Under the copyright conventions that most countries follow, a work is protected
from the moment it is fixed, without any registration. The default is therefore
**all rights reserved**: without a licence, nobody else may copy, modify or
redistribute the code, regardless of where it is hosted. A public repository with
no `LICENSE` file grants readers the right to *read* it and nothing more; internal
use inside the author's own institution may be fine by policy, but reuse elsewhere
is not. "Public" and "open source" are different claims, and the licence is the
grant: the minimum action is one file, `LICENSE` at the repository root, named in
the README.

## 3. Three families, and the compatibility question

| Family | Examples | Obligation when you distribute a derivative |
|---|---|---|
| Permissive | MIT, BSD-3-Clause, Apache-2.0 | Keep the copyright notice and licence text; no source obligation |
| Weak copyleft | MPL-2.0 (per file), LGPL-3.0 (per library) | The covered files/library stay under the same licence; your surrounding code need not |
| Strong copyleft | GPL-3.0 | The whole distributed work must be under GPL-3.0 with source available |
| Network copyleft | AGPL-3.0 | As GPL-3.0, and the obligation is triggered by giving users access over a network |

Combining code from two sources forces a choice: the **combined work** must be
licensable under a single set of terms. The demonstration's **ILLUSTRATIVE**
model prints the forced licence for the pairs it tests; the representative cases:

- MIT + Apache-2.0 → permissive; you must preserve both notices.
- MIT + GPL-3.0 → **GPL-3.0**: the combined work is copyleft.
- LGPL-3.0 + GPL-3.0 → GPL-3.0 (the strong term dominates).
- GPL-3.0 + AGPL-3.0 → AGPL-3.0 (the network clause dominates).
- Of the 49 pairs in the model's 7 × 7 table, only **9 (18 %)** are
  permissive-to-permissive, which is the quantitative version of the practical
  warning: most pairs of licences constrain each other.

One specific incompatibility is well documented and worth knowing by name:
**Apache-2.0 code is generally considered incompatible with GPL-2.0-only**, which
is why projects that need both use GPL-3.0 as the common ground. Verify this
against the current SPDX compatibility notes rather than from memory; the
authoritative sources are the licence texts and the licence-compatibility
documentation of the Free Software Foundation and of the SPDX project.

The distinction that matters most in practice is **internal use versus
distribution**. Copyleft obligations attach to distributing the work to others;
running GPL code on your own cluster to produce a paper's figures is not
distribution of the software. A group that never distributes has far fewer
obligations than a group that publishes a container image — and publishing a
container image *is* distribution, which is why
[22-02-06 Containers for Computational Reproducibility](../02-reproducible-workflows/06-containers-reproducibility.md)
has a licensing section.

## 4. Auditing a dependency tree

A licence audit answers three questions for each dependency:

1. **What licence is it actually under?** Not the README's badge: the metadata of
   the version you installed (`importlib.metadata` in Python, the package
   manifest, or the vendored `LICENSE` file).
2. **Do we distribute it?** A dependency used only to produce figures internally
   is not distributed with the paper's code, unless that code imports it.
3. **Is the combination permissible?** For every distributed dependency, apply
   the §3 rule and record the forced combined licence in the release notes.

A small script that prints the name, version and licence of every installed
dependency is enough to start; the hard part is the third question, which needs a
decision that should be recorded rather than inferred.

## 5. Citing software, and being citable

A citation needs a resolvable identifier and an accurate author list. The minimum
package of artefacts is:

- a **`CITATION.cff`** file at the repository root, in the Citation File Format,
  with `title`, `authors`, `version`, `doi` (once assigned), `license`, and
  `preferred-citation` when a paper describes the software;
- a **persistent identifier** for the release: a DOI minted by a data/software
  archive for a tagged snapshot, cited together with the tag;
- a **software-availability statement** in the paper, naming the version, the
  identifier, the licence and the environment.

A minimal `CITATION.cff` for the kind of package this curriculum's demonstrations
resemble:

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
title: "Tidal strain-rate toolkit"
version: 1.1.3
license: MIT
authors:
  - family-names: Rossi
    given-names: Anna
    orcid: "0000-0000-0000-0000"     # placeholder in the ORCID iD format
doi: 10.0000/example.doi
```

The `orcid` value above is a **placeholder in the ORCID iD format**
(`0000-0000-0000-0000`, an identifier string, not a link): illustrative, not resolvable.
A real ORCID iD belongs to the author and must never be invented — omit the field instead.

The `authors` list must be a decision, not a reflex: contributors who wrote code,
designed the method and maintained the release are usually all authors of the software,
and the geosciences norm is to cite the software release as well as the method paper.
State the convention in the `CITATION.cff` so a reader does not have to guess.

## 6. Versions: what a citation actually pins

A citation names a version, and a version constraint admits a set of releases.
The demonstration's semver arithmetic on 16 generated releases illustrates the
size of that set:

| Constraint | Meaning | Admissible releases |
|---|---|---|
| `^1.2` | $\ge 1.2.0$, $< 2.0.0$ | 4 of 16 |
| `~1.2` | $\ge 1.2.0$, $< 1.3.0$ | 2 of 16 |
| `>=2.0,<3` | the whole 2.x line | 8 of 16 |

A paper that cites "the toolkit, version 1.x" has therefore pinned nothing: four
admissible releases exist in this small list, and the analysis may have run under
any of them. The reproducibility requirement is the **exact** version plus a hash
or DOI that identifies the snapshot — the principle of
[22-02-02 Pinning Environments and Managing Dependencies](../02-reproducible-workflows/02-environment-pinning.md)
applied to credit rather than to execution.

## 7. Accounting for credit

Citations to software accrue like citations to papers but split between artefacts.
The demonstration's **SYNTHETIC** model — 8 citations in the first year, 35 %
annual growth, and 40 % of the credit attributed to the software DOI — gives

| Year | Citations that year | Cumulative | Software-DOI credit |
|---|---|---|---|
| 1 | 8.0 | 8.0 | 3.2 |
| 2 | 11.4 | 19.4 | 7.7 |
| 3 | 16.1 | 35.5 | 14.2 |
| 4 | 22.9 | 58.3 | 23.3 |
| 5 | 32.4 | 90.8 | 36.3 |
| 6 | 46.0 | 136.8 | 54.7 |

and the year in which the cumulative count crosses a threshold follows from the
geometric sum, $\text{cum}(m) = c_0\,(e^{rm} - 1)/(e^{r} - 1)$:

| Target cumulative citations | Year reached |
|---|---|
| 25 | 2.4 |
| 50 | 3.7 |
| 100 | 5.2 |

Two honest qualifications. First, the growth rate is chosen, so a threshold quoted
without it is not informative. Second, a citation count measures **attention, not
quality**: a widely used wrong implementation accumulates citations, and a correct
niche tool may accumulate none.

## 8. Worked example: preparing a release for citation

A package is ready to accompany a paper. The checks, in order:

1. **Licence.** A `LICENSE` file exists and is named in the README; the
   dependency audit shows only permissive dependencies, so the release can be
   distributed under MIT. Record the audit in the release notes.
2. **Citation metadata.** `CITATION.cff` lists the four authors with ORCIDs, the
   version `1.1.3`, the licence and (after minting) the DOI. Verify the file
   parses with a CFF validator; a malformed file is worse than none.
3. **Version pin.** The paper's figure scripts are re-run from a clean environment
   created by the pinned environment file, and the resulting figure hashes are
   recorded: this is what establishes that the cited version produced the figure.
4. **Availability statement.** "The analysis code is archived at DOI …, version
   1.1.3, under the MIT licence; the environment is defined by
   `environment.yml` in that archive." One sentence, resolvable.
5. **Credit.** The software DOI is cited in the paper's references, and the
   `CITATION.cff` says which of the two references readers should use.

Steps 3 and 4 are the ones that make the difference between a citation and an
assertion: without the version and the environment, the reader has a name, not a
reproduction.

## Assumptions and regime of validity

1. **The licence table is illustrative.** It models families, not every licence
   and not every combination; the GPL-2.0/Apache-2.0 case is documented, while
   many edge cases need the actual texts.
2. **Jurisdiction matters.** Copyright scope, the legal status of a network
   clause and the treatment of databases differ by country; this lesson states
   the widely used conventions, not a legal analysis.
3. **The citation curve is a chosen model.** Exponential growth was assumed; real
   citation profiles are flat, delayed or bursty, and the year of a threshold
   crossing is a property of the assumption.
4. **Author lists are decisions.** The lesson gives the principle (credit the
   contributors who made the artefact) and does not settle any particular
   authorship dispute.
5. **Identifiers persist only if an archive commits to them.** A DOI from a
   repository that later deletes content resolves to nothing, which is why the
   archive's preservation policy is part of the citation.

## The honest summary

Licensing and citation are the two artefacts that make software reusable and
creditworthy, and both are cheap to add and expensive to retrofit. Code with no
licence is not reusable at all; a licence decides what a derivative work may be
licensed as, and with the model's table only 18 % of licence pairs are
permissive-to-permissive, so the audit is worth doing before, not after, a
release. Permanent identifiers and a `CITATION.cff` are what let a reader resolve
the exact version that produced a paper's figure; a constraint like `^1.2` admits
four releases in the demonstration's 16-release list and pins nothing. Credit
accrues in a way that is measurable once an identifier exists — 136.8 cumulative
citations after six years under the model's chosen 35 % annual growth, with 54.7
attributed to the software DOI — but a count measures attention, not correctness,
and it is reported usefully only with the artefacts that made it possible.

## Python demonstration

[`code/licensing_and_citation_demo.py`](./code/licensing_and_citation_demo.py)
prints, with `np.random.default_rng(20261014)` set even though the calculation is
deterministic:

1. the combined-work licence for 24 licence pairs, with the permissive-to-
   permissive count (9 of 49 pairs, 18 %);
2. version-constraint arithmetic on 16 generated releases (`^1.2` → 4, `~1.2` →
   2, `>=2.0,<3` → 8);
3. the citation table for six years and the cumulative software-DOI credit;
4. the year in which cumulative citations cross 25, 50 and 100 — 2.4, 3.7 and
   5.2 years under the stated growth assumption.

```bash
cd 22-data-engineering-reproducibility/01-research-software-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python licensing_and_citation_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/05-licensing-and-citation-exercises.md`](./exercises/05-licensing-and-citation-exercises.md)
and
[`exercises/05-licensing-and-citation-solutions.md`](./exercises/05-licensing-and-citation-solutions.md).

## Mastery checkpoint

Without notes: a paper's code depends on a permissively licensed library, a
GPL-3.0 package and an LGPL-3.0 library, and the authors intend to publish a
container image with the analysis.

1. State the licence the distributed combined work must carry, and the one
   dependency whose obligations are limited to its own files.
2. State what changes if the container image is never published and only a paper
   is produced from internal runs.
3. Write the software-availability sentence, including the version and the
   environment.
4. A colleague says "our software is cited 137 times, so it is correct". State
   the two things the number does not establish.

## Common pitfalls

1. **Assuming a public repository is reusable.** No licence means all rights
   reserved; the grant must be explicit.
2. **Reading the licence from a badge or the README prose.** Check the version's
   metadata and the vendored licence text.
3. **Ignoring the licence of a *dependency you distribute*.** Publishing a
   container image distributes every library inside it.
4. **Citing the paper and not the software version.** The paper describes the
   method; the release is what produced the number.
5. **Using a caret constraint as a citation.** `^1.2` admits 4 of the
   demonstration's 16 releases and pins no analysis.
6. **Treating a citation count as a quality measure.** It measures attention and
   depends on the field, the venue and the year.

## Where this is used

- **Paper submission** — the software-availability statement and the archived
  version are required by a growing number of journals: see
  [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md).
- **Institutional or commercial reuse** — the licence decides whether a company
  can build on a group's code at all.
- **Container and environment publication** — distribution triggers the
  obligations of §3: see
  [22-02-06 Containers for Computational Reproducibility](../02-reproducible-workflows/06-containers-reproducibility.md).

## Related lessons

- [22-01-04 Documentation, Docstrings and READMEs That Work](./04-documentation.md) —
  where the licence and citation sections live.
- [22-01-02 Version Control with Git](./02-version-control-git.md) — the tags that
  a citation and an archive identify.
- [22-02-02 Pinning Environments and Managing Dependencies](../02-reproducible-workflows/02-environment-pinning.md) —
  the same version arithmetic applied to execution.
- [22-05-05 Open Science Practice in the Geosciences](../05-collaboration-and-project-management/05-open-science-practice.md) —
  the wider policy context of licensing and credit.

## Self-assessment checklist

- [ ] I can explain why code without a licence is not reusable.
- [ ] I can classify a licence family and predict the forced combined licence.
- [ ] I can audit a dependency tree for distribution obligations.
- [ ] I can write a valid `CITATION.cff` and an availability statement.
- [ ] I can compute the admissible release set of a version constraint.
- [ ] I can state what a citation count does not measure.
