---
id: 26-06-04
title: "Data Licensing, Attribution and Reuse Policy"
level: graduate
prereqs: []
estimated_minutes: 25
tags: [reference, licensing, attribution, reproducibility]
---

# Data Licensing, Attribution and Reuse Policy

What you may do with someone else's data, how to say so correctly, and how to
choose a licence for your own outputs. This is the reference page the rest of the
curriculum points at whenever a dataset, figure or code sample is reused.

## How to use this page

Read the sections in the order you will need them: what copyright covers, which
licence family applies, how to write an attribution, and what to do about your
own outputs. Nothing here is legal advice, and no licence is quoted from memory
where the licence text itself is available — **the licence text governs, and the
access points below link to it** (all registered in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv)).

*Provenance of this page:* policy reference. No external text is reproduced.

## 1. What is actually protected

| Object | Typical status | Practical consequence |
|---|---|---|
| Individual facts (a station's latitude, an event's origin time) | Not protected by copyright in most jurisdictions | You may use the fact; you may not copy a substantial part of a database's *arrangement* |
| Databases and compilations | Protected by copyright and/or a *sui generis* database right in some jurisdictions (notably the EU) | A downloaded catalogue carries terms even when its individual numbers are facts |
| Maps, figures and photographs | Protected as creative works | Reproduce only under a licence or an exception, and always with attribution |
| Software source code | Protected as a literary work; licensed, not "given away" | Read the licence before copying code, including short snippets |
| Government-produced data (many national agencies) | Often public domain domestically, not necessarily abroad | Verify the provider's own statement; do not generalise across borders |
| Your own paper's text and figures | Yours, unless assigned to a publisher by a publishing agreement | Check the agreement before posting the accepted version |

Two rules follow. First, **the provider's stated terms override your assumption**
from the category above. Second, **attribution is not a substitute for
permission** when permission is required.

## 2. The licence families you will meet

| Licence | Access point | Key obligations | Notes |
|---|---|---|---|
| CC BY 4.0 | [creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/) | Attribution, indication of changes, no additional restrictions | The standard for open scientific content; commercial use permitted |
| CC0 1.0 | [creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/) | None legally; attribution is courtesy | Used for public-domain dedications, e.g. some base-map data |
| Open Data Commons ODbL 1.0 | [opendatacommons.org/licenses/odbl/](https://opendatacommons.org/licenses/odbl/) | Attribution and **share-alike for derived databases** | The share-alike clause propagates to derived databases — read it before publishing a merged product |
| UK Open Government Licence v3.0 | [nationalarchives.gov.uk OGL v3](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) | Attribution | Common for national geoscience and survey data |
| Apache License 2.0 | [apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0) | Attribution, licence and notice retention; explicit patent grant | Common for scientific software |
| MIT, BSD-2 and BSD-3 | [OSI licence list](https://opensource.org/licenses) | Attribution, licence retention | Permissive; BSD-2/3 differ mainly on endorsement clauses |
| GNU GPL v3 | [gnu.org GPL v3](https://www.gnu.org/licenses/gpl-3.0.html) (blocks automated checks; valid in a browser) | Copyleft: derived works distributed must be under the same licence | Matters if you ship a modified GPL tool as part of a product |
| LGPL v3 | see the OSI list above | Copyleft with a linking exception | Common for geophysical libraries (ObsPy, Cartopy, GMT) |

**Share-alike and copyleft are the families that cause surprises.** CC BY-SA,
ODbL and the GPL family can require you to license *your* derived work under the
same terms. Check before combining datasets or shipping software.

## 3. How to write an attribution

A complete data attribution answers five questions:

| Question | Example shape |
|---|---|
| What is it? | "GRACE/GRACE-FO time-variable gravity products" |
| Who produced it? | "produced by <agency or project>" |
| Which version and when was it accessed? | "release <version>, accessed 2026-10-14" |
| Under what licence? | "licensed under CC BY 4.0" (with a link to the licence) |
| What did you change? | "filtered and resampled to a 1° grid" — required by CC BY 4.0 |

Patterns to copy:

```
<Producer> (<Year>). <Dataset title>, version <version>.
<Access point, registered in tools/verified_links.tsv>, accessed <YYYY-MM-DD>.
Licensed under <licence name>, <licence URL>. Modifications: <description or "none">.
```

```
Software: <Project name>, version <x.y.z>. <Project access point>.
Licensed under <licence>. Accessed <YYYY-MM-DD>.
```

For a figure: credit the underlying data *and* the figure's creator separately;
they are usually different people with different licences.

## 4. Reusing the four kinds of external material in this curriculum

| Material | Rule applied here |
|---|---|
| Datasets and services | Cited with a registered access point, a provenance label (OBSERVED / ILLUSTRATIVE / SYNTHETIC) and an instruction to read the provider's terms |
| Figures and tables | Not reproduced. Where a figure would help, the lesson says where to find it instead |
| Code | Demonstrated code in this repository is written for the lesson; third-party libraries are cited, not vendored |
| Textbook content | Cited only, by author and title; no excerpts |

This is the conservative policy: it is always lawful to cite and to point, and it
avoids the failure mode of a teaching repository accumulating unlicensed figures.

## 5. Choosing a licence for your own output

| Output | Common choice | Reason |
|---|---|---|
| Code | MIT or BSD-3 | Maximum reuse with attribution; Apache-2.0 if a patent grant matters |
| A derived dataset | CC BY 4.0 | Attribution without preventing reuse; **check the upstream terms first**, because share-alike propagates |
| Figures and lesson text | CC BY 4.0 | Standard for teaching material |
| Anything built on ODbL or CC BY-SA data | The same licence | Share-alike requires it |
| Anything containing personal or location-sensitive data | Do not publish, or aggregate and document the protection | Licensing cannot fix an ethical problem |

## 6. Practical checklist before you publish

1. List every dataset, figure and code snippet you reused.
2. For each, find the licence **on the provider's own page**, and copy the exact
   terms you are relying on.
3. Check share-alike and copyleft propagation into your own output.
4. Write the attributions in full, including access dates and modification
   statements.
5. State the provenance label (OBSERVED / ILLUSTRATIVE / SYNTHETIC) for every
   dataset in the manuscript or repository.
6. Record the version of every dataset and tool, so the result is reproducible.
7. If any item's terms are unclear, either obtain permission in writing or
   remove the item.

## 7. What licensing does not cover

- **Accuracy and fitness.** A licence grants reuse rights; it says nothing about
  whether the data are correct or suitable for your purpose.
- **Privacy and ethics.** Indigenous data sovereignty, sensitive site locations
  and personal data are governed by expectations and agreements that outrank a
  licence.
- **Trademarks and logos.**
- **Third-party content inside a dataset.** A compilation may contain material
  the compiler could not license on your behalf.

## 8. Verification obligations of this repository

| Practice | Where it is enforced |
|---|---|
| Every cited external URL must be registered | [`tools/verified_links.tsv`](../../tools/verified_links.tsv), checked by `tools/verify_links.py` |
| Dead links are marked, not silently reused | Statuses 404 and 000 in the registry, flagged in [module 26-05](../05-open-datasets-catalogue/README.md) |
| No copyrighted text or figures are reproduced | This module's contributing policy |
| Datasets carry provenance labels | All lessons in [module 26-05](../05-open-datasets-catalogue/README.md) |

## Caveats

- **This page is not legal advice.** Licences interact with national law,
  database rights and the terms of the specific provider.
- **Terms change.** A provider may relicense; the version you accessed governs,
  which is another reason to record the access date.
- **"Open" has a formal definition** (the Open Definition and the OSI definition
  of open source), and many resources that are free to read do not meet it.
- **Attribution strings are often prescribed.** Where a provider specifies the
  exact wording, use it verbatim rather than paraphrasing.

## Related pages

- [OER: Mathematics, Physics and Computing](./01-oer-mathematics.md)
- [OER: Geophysics, Seismology and Earth Science Courses](./02-oer-geophysics.md)
- [Software Directory: Open-Source Geophysics Tools](./03-software-directory.md)
- [How to cite a dataset](../05-open-datasets-catalogue/README.md)
- [22-data-engineering-reproducibility folder overview](../../22-data-engineering-reproducibility/README.md)
- [24-research-papers-writing folder overview](../../24-research-papers-writing/README.md)
