---
id: 22-05-04
title: "Research Data Management Plans and FAIR Principles"
level: advanced
prereqs: ["22-05-03", "22-02-05"]
estimated_minutes: 45
tags: [data-management, fair, retention, preservation, open-science]
---

# Research Data Management Plans and FAIR Principles

## Learning objectives

By the end of this lesson you will be able to:

1. **Forecast** a project's storage over its lifetime and its retention period, and
   **state** which decision multiplies the cost.
2. **Distinguish** the four FAIR facets, and **map** each to an artefact a reviewer can
   open rather than to an intention.
3. **Compute** a data-loss risk from the number of independent copies, and **state** what
   makes a copy independent.
4. **Decide** what to keep, what to regenerate and what to delete, and **defend** the
   decision with the cost of each tier.
5. **Write** the sections of a data management plan that a reviewer can check, with the
   numbers that make each one falsifiable.
6. **Diagnose** the four plan failures: an unaffordable archive, unopenable metadata, a
   single point of failure, and a retention policy that deletes what an analysis needs.

Storage volumes, readiness percentages and risk probabilities in this lesson are
**SYNTHETIC** with chosen parameters. No funder policy is quoted, no institutional
requirement is described, and no real plan is evaluated; the arithmetic and the mapping
from principle to artefact are the transferable content.

## Prerequisites

- [22-05-03 Collaborative Writing with LaTeX and Markdown](./03-collaborative-writing.md) —
  the manuscript whose data the plan describes.
- [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md) —
  the identifiers, manifests and derivation records the plan commits to.

## 1. Intuition: a plan is a set of commitments with numbers

A data management plan is often written as prose that repeats the funder's headings. Its
useful form is different: each section is a **commitment with an artefact and a number** —
which data will be kept, for how long, in what format, with which identifier, at what
cost, and who is responsible. That form has three advantages: it can be costed, it can be
checked at the end of the project, and it forces the decisions (what to delete) into the
open while they are still cheap.

The FAIR principles (findable, accessible, interoperable, reusable) are the organising
framework, and the lesson's addition is to insist that each one maps to something a
reviewer can open. "Metadata will be provided" is not FAIR; "each dataset has a
`CITATION.cff` and a data dictionary in the archive, checked by a validator in CI" is.

## 2. The forecast, and the decision that multiplies it

The demonstration's **SYNTHETIC** project produces 8 TB of raw data and 3 TB of derived
products per year for five years, with a 1.5× reprocessing factor on the derived tier:

| Year | Raw (TB) | Derived (TB) | Total (TB) |
|---|---|---|---|
| 1 | 8.0 | 4.5 | 12.5 |
| 2 | 16.0 | 9.0 | 25.0 |
| 3 | 24.0 | 13.5 | 37.5 |
| 4 | 32.0 | 18.0 | 50.0 |
| 5 | 40.0 | 22.5 | 62.5 |

The project total is **62.5 TB**, and a ten-year retention period raises it to
**187.5 TB** — a factor of **3.0**. Notice what the growth is: the archive decision is
made once, at the start, and it dominates every later choice. The derived tier is 36 % of
the project total and is regenerable; the raw tier is the part that cannot be recreated.

The practice that follows is to **cost the plan at two horizons** (project and retention)
and to decide the retention horizon explicitly, with the fraction of the archive that
needs to be kept at full resolution versus aggregated
([22-04-03](../04-databases-and-large-data/03-timeseries-databases.md) §4).

## 3. FAIR as artefacts, not intentions

The demonstration scores six items with chosen readiness values:

| Item | Readiness |
|---|---|
| persistent identifier per dataset | 90 % |
| machine-readable metadata | 70 % |
| documented licence | 60 % |
| versioned releases with checksums | 80 % |
| a published data dictionary | 40 % |
| a documented retention policy | 30 % |

Mean readiness **0.617**, with the weakest two being the retention policy and the data
dictionary. The mapping that makes the score meaningful:

| Facet | Artefact a reviewer can open |
|---|---|
| Findable | an identifier that resolves, and a landing page with the title, authors and description |
| Accessible | a documented access route — a URL, an API, or a stated restriction with a contact |
| Interoperable | an open format, a documented schema, declared units and vocabularies |
| Reusable | a licence, provenance, a data dictionary, and the code that produced the products |

Each row is checkable: a reviewer resolves the identifier, opens the landing page, reads
the schema, and looks for the licence. A plan whose items cannot be checked this way is a
statement of intent, and the honest score for it is not computable.

## 4. Risk: independent copies and the exponent

Data loss is the failure a plan exists to prevent, and its arithmetic is an exponent. With
a per-copy, per-year failure probability of 0.02 in the demonstration's **SYNTHETIC** model:

| Independent copies | $P(\text{loss in a year})$ | Expected artefacts lost of 20 |
|---|---|---|
| 1 | 0.02000 | 0.4000 |
| 2 | 0.00040 | 0.0080 |
| 3 | 0.00001 | 0.0002 |

The exponent is the whole content: one additional independent copy changes the risk by a
factor of 50, and the third by another factor of 40. What makes copies **independent** is
the part that is usually wrong: a second copy in the same building, on the same account,
in the same backup rotation, or on the same storage system is not independent — a fire, a
deleted account or a broken backup job removes both. Independence means a different
failure domain: a different site, a different provider, a different administrative login.
The plan should name the failure domains, and a restore test is the only evidence that a
copy exists in a usable form.

## 5. Keep, regenerate, delete

Three categories, with different rules:

1. **Irreplaceable**: raw observations, field notes, instrument calibrations, licences and
   permissions. Keep indefinitely, in at least two independent copies, with checksums and
   a restore test. This is the tier the retention horizon is really about.
2. **Regenerable**: derived products, figures, aggregates. Keep while useful (they save
   compute), rebuild from raw when required, and record the derivation so a rebuild is
   possible ([22-02-05](../02-reproducible-workflows/05-data-versioning.md) §5). Deleting
   these is a cost decision, and it is safe only if the raw tier and the code survive.
3. **Disposable**: caches, intermediates, logs beyond the regulatory minimum. Delete
   aggressively; they are where the unmanaged growth happens.

The demonstration's cost arithmetic (25 cost units per TB-year) is: the project phase,
averaged at half-full, is **3 906 units**, and the ten-year archive phase is **15 625
units** — four times the project phase. The plan's job is to state which tier that
archive phase holds, and the answer should be category 1 plus whatever category 2 the
analyses still need.

## 6. Writing a plan a reviewer can check

1. **Data inventory**: what is produced, in what volume, in what format, by whom.
2. **Standards**: the formats, metadata schemas, vocabularies and units, with the
   identifier scheme.
3. **Access and licence**: the route, the restrictions, the licence, and the contact for
   restricted data.
4. **Retention**: the horizon per tier, the responsible person, and the deletion policy
   for the regenerable and disposable categories.
5. **Preservation and backup**: the failure domains of the copies, the restore test's
   frequency and its record.
6. **Roles and cost**: who does each action, and the storage and effort cost per year.

Each item is falsifiable at review: the inventory can be compared with what exists, the
standards can be checked against the archive, the retention horizon against the stored
data, the copies against a restore test, and the cost against a bill.

## Assumptions and regime of validity

1. **Chosen volumes and rates.** The 8 TB/year and 1.5× reprocessing figures are teaching
   values; the structure (raw grows linearly, derived grows with reprocessing, the archive
   multiplies the total) is what transfers.
2. **A simple risk model.** The loss probability per copy per year is constant and copies
   fail independently; real failures are correlated (a provider outage, a budget cut that
   ends several services at once), so the exponent is an idealisation.
3. **Cheap storage.** Cost units are arbitrary; in an environment where storage is free,
   the retention decision is still about findability and about the effort of keeping data
   interpretable, which does not go to zero.
4. **No funder requirements are described.** Plans exist within policies that differ and
   change; the lesson gives the checkable form, not the requirements.
5. **FAIR is not a binary.** The readiness values are a modelling device; in practice each
   facet is a spectrum, and the useful question is which artefact is missing.

## The honest summary

A data management plan is a set of commitments with numbers: 62.5 TB over a five-year
project becomes 187.5 TB with a ten-year retention, a factor of 3.0 that is decided once;
FAIR becomes checkable only when each facet maps to an artefact someone can open; and the
risk of losing irreplaceable data falls by orders of magnitude with each *independent*
copy — 0.02000 to 0.00040 to 0.00001 in the modelled case — where independence means a
different failure domain, not a second folder. The decisions that make the plan
affordable are the three categories: keep the irreplaceable indefinitely, regenerate the
derived, delete the disposable, and state which is which before the project needs the
space.

## Python demonstration

[`code/research_data_management_plan_demo.py`](./code/research_data_management_plan_demo.py)
prints, with `np.random.default_rng(20261014)`:

1. the five-year forecast (12.5 to 62.5 TB) and the 3.0× archive multiplier;
2. the six FAIR readiness items, the 0.617 mean and the two weakest;
3. the loss-risk table for one to four copies (0.02000 to 1.6 × 10⁻⁷);
4. the cost of the plan's two phases (3 906 and 15 625 units).

```bash
cd 22-data-engineering-reproducibility/05-collaboration-and-project-management/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python research_data_management_plan_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/04-research-data-management-plan-exercises.md`](./exercises/04-research-data-management-plan-exercises.md)
and
[`exercises/04-research-data-management-plan-solutions.md`](./exercises/04-research-data-management-plan-solutions.md).

## Mastery checkpoint

Without notes: a project produces 20 TB/year of raw data and 8 TB/year of derived
products for three years, with a five-year retention.

1. Compute the project total and the archived total, and the multiplier.
2. State which tier each figure belongs to, and which of them may be deleted safely.
3. Compute the loss probability for two and three independent copies given a per-copy
   annual failure probability of 0.03, and state what "independent" requires.
4. State the six sections of a checkable plan, and for each one number a reviewer could
   verify.

## Common pitfalls

1. **A single copy described as a backup.** The same site, account or rotation is one
   failure domain.
2. **FAIR as prose.** Without an artefact, the claim cannot be checked, and it will not be
   true.
3. **Deleting raw data to save space.** Aggregates cost a small fraction of raw; the loss
   is permanent ([22-04-03](../04-databases-and-large-data/03-timeseries-databases.md) §4).
4. **Costing only the project phase.** The archive phase is 3× the project in the
   demonstration's model, and it arrives after the funding ends.
5. **No restore test.** An untested backup is a hypothesis; the test is the evidence.
6. **A retention policy with no owner.** Someone must be responsible for the deletion and
   for the decision to keep, or the policy is a wish.

## Where this is used

- **Grant applications** — the plan is a scored section, and the numbers make it
  credible.
- **Institutional repositories and archives** — the identifier and metadata commitments.
- **Field campaigns** — the raw tier's preservation is the campaign's only durable output
  ([22-03-04](../03-data-formats-and-engineering/04-getting-earth-data.md)).
- **Teaching and long-lived datasets** — the regeneration story is what lets a course's
  data outlive the course.

## Related lessons

- [22-05-05 Open Science Practice in the Geosciences](./05-open-science-practice.md) —
  the community context of the plan's commitments.
- [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md) —
  the identifiers and derivation records a plan promises.
- [22-01-05 Licensing, Citation and Software Credit](../01-research-software-engineering/05-licensing-and-citation.md) —
  the licence and citation artefacts the FAIR facets require.
- [22-04-03 Time-Series Databases for Sensor Networks](../04-databases-and-large-data/03-timeseries-databases.md) —
  the retention arithmetic for the largest tier.

## Self-assessment checklist

- [ ] I can forecast storage at two horizons and name the multiplying decision.
- [ ] I can map each FAIR facet to a checkable artefact.
- [ ] I can compute a loss risk from the number of independent copies.
- [ ] I can classify data into keep, regenerate and delete.
- [ ] I can write a plan whose items a reviewer can verify.
- [ ] I can name the four plan failures and their detectors.
