---
id: 22-05-05
title: "Open Science Practice in the Geosciences"
level: graduate
prereqs: ["22-05-04", "22-01-05"]
estimated_minutes: 45
tags: [open-science, community-practice, credit, data-sharing, policy]
---

# Open Science Practice in the Geosciences

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** the several things "open" can mean — data, code, methods, reviews,
   publications — and **state** the artefact each one releases.
2. **Model** the adoption of an open practice across a community, and **compute** when a
   policy's effect appears.
3. **Estimate** reuse from adoption, and **state** why one group's release matters less
   than a shared practice.
4. **Account** for the costs and benefits of a release, with both stated in the same
   units.
5. **Choose** an access level for a dataset — open, embargoed, restricted — and **state**
   the protection each level actually provides.
6. **Diagnose** the four failures of open practice in a group: a release that no one can
   find, a licence that forbids the intended reuse, a commitment with no maintenance, and
   an openness policy that exposes data it should protect.

Adoption curves, reuse rates and citation multipliers in this lesson are **SYNTHETIC**
with chosen parameters. No bibliometric database was queried, and no measured effect of
open practice on citation counts or on research outcomes is claimed; such numbers vary by
field and by study, and any figure used in a policy argument should be checked against
the current literature.

## Prerequisites

- [22-05-04 Research Data Management Plans and FAIR Principles](./04-research-data-management-plan.md) —
  the artefacts a release is built from.
- [22-01-05 Licensing, Citation and Software Credit](../01-research-software-engineering/05-licensing-and-citation.md) —
  the licence and citation mechanics.

## 1. Intuition: "open" names several different releases

The word covers a family of practices, each with its own artefact and its own community:

| Practice | Artefact released | What it enables |
|---|---|---|
| Open data | datasets with identifiers and licences | re-analysis, new methods, meta-studies |
| Open code | the software that produced the results | reproduction, reuse, extension |
| Open methods | protocols, processing chains, parameters | independent replication |
| Open access | the publication itself | reading without a subscription |
| Open review | referee reports and responses | assessment of how claims were tested |

A group can be open in one and closed in another, and the *combination* determines what a
reader can actually check: open data without the code cannot reproduce an analysis, and
open code without the data cannot reproduce a result. The practical question is therefore
not "are we open?" but "what can someone else check with what we released?".

## 2. Adoption: the effect of a practice, not of a paper

Community practices spread logistically. The demonstration's **SYNTHETIC** community of
200 groups adopts an open-release policy with a logistic curve:

| Year | Groups releasing openly | Share |
|---|---|---|
| 0 | 29.6 | 14.8 % |
| 3 | 66.4 | 33.2 % |
| 6 | 117.3 | 58.7 % |
| 9 | 160.4 | 80.2 % |
| 12 | 184.1 | 92.1 % |
| 15 | 194.1 | 97.1 % |

The curve's shape matters for expectations: a policy or a tool introduced at year 0 has
little visible effect for several years (14.8 % adoption), most of its effect in the
middle (33 % to 80 % between years 3 and 9), and then saturates. Groups that judge such
a policy after two years will usually conclude it failed, which is a property of the
adoption curve rather than of the policy.

## 3. Reuse, and why a shared practice beats a single release

If each adopting group produces downstream works at a rate of 0.08 per year, the
reuse rate follows the adoption curve and its cumulative total over 15 years is **163
works** in the model — a number set by the *community's* adoption, not by any single
group's release. Two consequences:

1. **Standards are the leverage.** A group that releases data in a private format, with
   its own vocabulary, contributes little to reuse; the same data in a community format
   with community vocabularies
   ([22-03-06](../03-data-formats-and-engineering/06-metadata-standards.md)) is usable by
   the workflows others already run.
2. **Landing pages and identifiers are the entry point.** Reuse begins with finding, and
   finding begins with a resolvable identifier — the FAIR facet that is cheapest and most
   often missing ([22-05-04](04-research-data-management-plan.md) §3).

The honest caveat: the model's 0.08 reuse rate per group-year is a chosen value. Real
reuse rates depend on the field, the data's uniqueness, and whether an existing archive
already holds equivalent data; a group should not promise a reuse number it cannot
measure.

## 4. Credit: the arithmetic, and its limits

The demonstration models a publication's citation accrual with and without an open
release, with a chosen multiplier of 1.25:

| Year | Closed (cumulative) | Open (cumulative) |
|---|---|---|
| 0 | 12.0 | 15.0 |
| 4 | 82.8 | 103.5 |
| 10 | 311.9 | 389.9 |

After ten years the open release is **25 % ahead** — the multiplier applies to each year's
accrual, so it compounds with the citation growth rather than multiplying the final year.
Two honest qualifications, both important:

1. **The multiplier is chosen, not measured.** Studies of the citation effect of data
   sharing find effects that vary widely by field, by discipline's norms and by the type
   of data; some find little or no effect. The lesson's number is a modelling device.
2. **Attention is not quality, and citations are not the only benefit.** The benefits that
   dominate in practice are re-use by others (which returns new collaborations and
   corrections), compliance with funder requirements, and the ability to answer a question
   about your own results years later — none of which appears in a citation count.

## 5. Costs, stated in the same units

The demonstration's effort model for one release:

| Effort item | Hours |
|---|---|
| preparing the release (formatting, metadata, docs) | 60 |
| archiving with an identifier | 4 |
| answering user questions in year 1 | 20 |
| maintaining the release for ten years | 25 |
| **total** | **109** (about 14 working days) |

The point of stating costs is not to argue against release but to make it a **planned**
activity: 14 days is a real fraction of a project's effort, it is usually unbudgeted, and
the maintenance item is the one that is forgotten — a release with no named maintainer
becomes a broken link and then a liability. A defensible plan states both sides: the
release's cost, and the benefit as far as it can be measured (reuse requests, reproduction
attempts by others, the group's own later use).

## 6. Access levels and what they protect

| Level | Mechanism | What it actually protects |
|---|---|---|
| Open | a public identifier and licence | nothing; suitable for data with no restriction |
| Embargoed | a date, then public release | the group's priority period, and nothing after it |
| Restricted | a documented request route with review | sensitive, proprietary or community-protected data |
| Closed | no distribution | everything, including the ability to check any claim |

Two cautions. First, an embargo with a stated date is administratively honest; an embargo
with no date is an indefinite closure with better wording. Second, **access control is not
a security measure for data that should never be shared** — a request route with review is
appropriate for sensitive data whose use can be governed (a policy decision), while data
whose release would cause harm need a governance framework beyond a web form, which is the
subject of the folder's data-ethics material
([21-09 Ethical and Responsible Analytics](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/README.md)).
Community norms also matter: some data are stewarded under agreements with the communities
they describe, and the decision to share is not the researcher's alone.

## 7. Practice for a group

1. **Decide the access level per dataset** before the project starts, and write the reasons
   down; the decision is cheapest at the beginning.
2. **Release in community formats** with community vocabularies, or the release will not be
   used.
3. **Publish the identifier and the landing page**, and cite them in the paper's data
   availability statement
   ([22-01-05](../01-research-software-engineering/05-licensing-and-citation.md) §5).
4. **Name a maintainer** for each release and a review date, so the commitment survives
   the project.
5. **Budget the effort** — the demonstration's 109 hours — in the proposal, not in someone's
   spare time.
6. **Measure what you can**: download counts, reuse requests, corrections received. Those
   are the numbers that make the next release easier to justify.

## Assumptions and regime of validity

1. **Chosen adoption parameters.** The logistic rate and midpoint are teaching values; real
   practice adoption depends on funder requirements, journal policies and disciplinary
   norms, and differs sharply between subfields.
2. **A chosen reuse rate and citation multiplier.** Neither is a measured effect, and the
   lesson says so twice: the citation effect of open practice varies by field and study,
   and reuse depends on whether equivalent data are already available elsewhere.
3. **No policy is described.** Funder, journal and institutional requirements differ and
   change; read the current policy rather than the lesson.
4. **Openness as a choice with costs.** The lesson treats release as a decision with a cost
   to plan, not as an obligation without one; the cost is real and should be budgeted.
5. **Ethical limits are acknowledged, not resolved.** Data about people, about protected
   sites, and data stewarded by communities may not be openly distributable; that
   determination belongs to a governance process, not to a licensing default.

## The honest summary

"Open science" names a family of releases — data, code, methods, publications, reviews —
and what a reader can check depends on the combination, not on any single one. Community
practices follow a logistic adoption curve in which the visible effect appears in the
middle years (from 14.8 % at year 0 to a modelled 80.2 % at year 9), reuse is driven by
the community's adoption rather than by one group's release (a modelled 163 downstream
works over 15 years), and the credit argument rests on a multiplier that must be checked
against the literature rather than assumed. The cost side is modest but real — about 109
hours, or 14 working days, for one release in the demonstration's model — and the item
most often forgotten is the maintenance commitment. The defensible group practice is to
choose the access level per dataset and write the reason down, release in community
formats, publish and cite the identifiers, name a maintainer, budget the effort, and
measure the reuse that actually occurs.

## Python demonstration

[`code/open_science_practice_demo.py`](./code/open_science_practice_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. the logistic adoption curve of 200 groups over 15 years (14.8 % to 97.1 %);
2. the reuse that follows from it (a cumulative 163 downstream works);
3. citation accrual with and without an open release (a modelled 25 % difference after ten
   years), with the multiplier labelled as chosen;
4. the effort table: 109 hours, about 14 working days, for one release.

```bash
cd 22-data-engineering-reproducibility/05-collaboration-and-project-management/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python open_science_practice_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/05-open-science-practice-exercises.md`](./exercises/05-open-science-practice-exercises.md)
and
[`exercises/05-open-science-practice-solutions.md`](./exercises/05-open-science-practice-solutions.md).

## Mastery checkpoint

Without notes: a group has three datasets — a regional catalogue (publishable), a licensed
third-party product (not redistributable), and waveforms recorded with a partner
institution (joint ownership).

1. State the access level you would choose for each, with the mechanism and the reason.
2. State what a reader can check with the group's code released and the catalogue open,
   but the waveforms closed.
3. Compute the effort the group should budget for one release using the demonstration's
   table, and name the item most often forgotten.
4. State the two caveats you would attach to a claim that open release increases
   citations.

## Common pitfalls

1. **Treating openness as one thing.** Releasing code without data, or data without
   metadata, leaves the claim unchecked.
2. **An embargo without a date.** It is a closure with better wording.
3. **Releases without a maintainer.** The link breaks and the storage bill continues.
4. **Quoting a citation multiplier as established.** The effect varies by field and study;
   check the literature and state the uncertainty.
5. **Releasing sensitive or community-stewarded data by default.** The determination belongs
   to a governance process.
6. **Ignoring the effort.** Fourteen working days of unbudgeted work per release is how
   open practice becomes a burden instead of a practice.

## Where this is used

- **Papers and their data statements** — the release is what makes the statement true:
  see [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md).
- **Funder and institutional policy** — compliance is a matter of artefacts, and the plan
  of [22-05-04](./04-research-data-management-plan.md) is where they are committed.
- **Community data standards** — the formats and vocabularies that make a release reusable:
  see [22-03-06 Metadata Standards and Controlled Vocabularies](../03-data-formats-and-engineering/06-metadata-standards.md).
- **Ethical and Indigenous data governance** — where the decision to share is not the
  researcher's:
  see [21-09 Ethical and Responsible Analytics](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/README.md).

## Related lessons

- [22-05-04 Research Data Management Plans and FAIR Principles](./04-research-data-management-plan.md) —
  the plan that commits to the releases.
- [22-01-05 Licensing, Citation and Software Credit](../01-research-software-engineering/05-licensing-and-citation.md) —
  the licence and citation mechanics of a release.
- [22-03-04 Programmatic Access to Earth Data](../03-data-formats-and-engineering/04-getting-earth-data.md) —
  the services that make open data usable.
- [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md) —
  where the release meets the paper.

## Self-assessment checklist

- [ ] I can distinguish the practices that "open" names.
- [ ] I can describe an adoption curve and when a policy's effect appears.
- [ ] I can state why community formats drive reuse.
- [ ] I can state the costs of a release and the item most often forgotten.
- [ ] I can choose and justify an access level per dataset.
- [ ] I can state the limits of the citation argument for open practice.
