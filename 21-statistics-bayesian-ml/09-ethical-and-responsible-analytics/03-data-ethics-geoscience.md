---
id: 21-09-03
title: "Data Ethics, Indigenous Data Sovereignty and Geoscience"
level: research
prereqs: ["21-09-02", "21-09-01", "23-01-03"]
estimated_minutes: 60
tags: [data-ethics, data-sovereignty, privacy, governance, teaching]
---

# Data Ethics, Indigenous Data Sovereignty and Geoscience

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** disclosure risk and utility for an aggregated spatial release, and
   **compute** both as a function of cell size.
2. **Measure** the effect of a small-cell suppression rule (a $k$-anonymity
   threshold) on the released fraction and on the population retained.
3. **Explain** why $k$-anonymity protects against a release but not against an
   adversary who holds auxiliary information, and **state** what other controls
   exist.
4. **Distinguish** the questions a privacy metric can answer from the questions that
   only an agreement with the data holders can answer — consent, authority,
   benefit-sharing, and the sensitivity of the sites themselves.
5. **State** the principles commonly applied to geoscientific data (FAIR, the CARE
   principles, free prior and informed consent, data sovereignty) and **explain**
   what each changes about a data-sharing plan.
6. **Plan** a release: what is published, at what resolution, under what conditions,
   with what agreement, and what is retained under controlled access.
7. **Identify** the geoscientific data types for which location is itself the
   sensitive attribute, and **state** why aggregation does not protect them.

Everything numeric below is **SYNTHETIC**, produced by
[`code/data_ethics_geoscience_demo.py`](./code/data_ethics_geoscience_demo.py). No
real survey, community, site or legal framework is described, and the numbers are
properties of that generator only. The governance frameworks named in §5 are
described at the level of principle; their details vary and must be checked against
current published guidance and, above all, against the requirements of the specific
data holders and communities involved.

## Prerequisites

- [21-09-02 Honest Reporting of Uncertainty and Limitations](./02-reporting-uncertainty-ethics.md) —
  the reporting obligations that accompany any quantitative claim.
- [21-09-01 Statistical Reproducibility, p-Hacking and Multiple Comparisons](./01-reproducibility-statistical.md) —
  the analysis-level integrity that a data-sharing plan must not undermine.
- [23-01-03 Field Notebooks, Metadata and Data Provenance](../../23-field-methods-instruments/01-field-safety-and-planning/03-field-notebooks.md) —
  the practical metadata that makes a release auditable.
- [17-06-04 Spatial Statistics, Autocorrelation and Hotspot Analysis](../../17-remote-sensing-gis/06-geospatial-analysis-advanced/04-spatial-statistics.md) —
  the spatial aggregation the privacy analysis uses.

## 1. Intuition: data are about people as well as about the Earth

A geophysical data set is usually described by its instrument, its processing and
its uncertainty. That description is necessary and insufficient, because the data
also have:

- **provenance**: whose territory the measurements come from, who was consulted,
  who consented, and for what purpose;
- **a location** that may itself be sensitive — a cultural or sacred site, a
  burial ground, a community's water source — where the coordinates are the
  sensitive attribute, not any personal characteristic attached to them;
- **beneficiaries**: who can use the data, who can publish from it, and whether the
  people the data describe share in what is learned;
- **obligations that do not expire**: an agreement made with a community for one
  project, which does not automatically extend to the next analysis, the next
  student, or an open repository release.

The quantitative part of this lesson is narrow and exact: **how much disclosure
risk an aggregated spatial release carries, and what suppression costs**. The rest
of the lesson is about the decisions that number informs but does not make.

## 2. What a privacy metric can measure

The demonstration models an $800$-record survey in a $20 \times 20$ km region, with
records clustered around $30$ settlements. It measures the two quantities that any
spatial release trades:

| Cell size | Occupied cells | Mean count | Singleton cells | Records in them |
|---|---|---|---|---|
| $1$ km | $286$ | $2.80$ | $79$ | $79$ |
| $2$ km | $90$ | $8.89$ | $11$ | $11$ |
| $5$ km | $16$ | $50.00$ | $0$ | $0$ |
| $10$ km | $4$ | $200.00$ | $0$ | $0$ |

A **singleton cell** — a published cell containing exactly one record — is the
sharpest form of disclosure in a count release: anyone holding an auxiliary list of
locations can attach a name to the count of one. At $1$ km nearly a third of the
occupied cells are singletons ($79$ of $286$); at $5$ km there are none, because the
mean cell holds $50$ records.

The trade is not subtle: the same coarsening that removes the singletons also
destroys the local structure — a village, a field, a catchment — that gives the data
their scientific value.

## 3. Suppression, and what it costs

A **$k$-anonymity** rule suppresses or coarsens cells whose count is below $k$:

| Cell size | $k$ | Cells suppressed | Records suppressed | Records retained |
|---|---|---|---|---|
| $1$ km | $5$ | $243$ | $540$ | $260$ ($32.5\%$) |
| $1$ km | $10$ | $285$ | $790$ | $10$ ($1.2\%$) |
| $2$ km | $5$ | $23$ | $51$ | $749$ ($93.6\%$) |
| $2$ km | $10$ | $52$ | $259$ | $541$ ($67.6\%$) |
| $5$ km | $10$ | $1$ | $8$ | $792$ ($99.0\%$) |
| $10$ km | $5$, $10$ | $0$ | $0$ | $800$ ($100\%$) |

Three findings, each with a governance consequence:

1. **At $1$ km, suppression cannot be both protective and useful.** $k = 5$ keeps
   barely a third of the records; $k = 10$ keeps $1.2\%$, which is a useless
   release. The policy implication is that fine-resolution release is not a
   suppression problem at all — it is a question of *whether* to release, under what
   agreement, or under controlled access.
2. **Coarsening dominates suppression.** At $2$ km with $k = 10$ the release retains
   $67.6\%$; at $5$ km it retains $99.0\%$. If a coarse release suffices for the
   science, it is both safer and more useful than a heavily suppressed fine one.
   That is the single most useful quantitative result of the lesson.
3. **$k$-anonymity is a weaker guarantee than it sounds.** It protects against the
   release *in isolation*. An adversary with an auxiliary data set — a cadastral
   list, a previous survey, a known individual whose location they know — can
   subtract, intersect or difference two releases to recover the suppressed cells.
   Two aggregated releases of overlapping populations compose into a more detailed
   one, which is why suppression rules must be applied across *all* releases of the
   same region, not release by release.

Other controls, in rough order of protection: aggregation to a resolution at which
every cell is large; jittering or geographic masking, at the cost of positional
accuracy that may matter more than privacy for some science; **controlled access**
(no public release, analysis by arrangement); and a **collaborative agreement**
where the data holders decide the release themselves. The last is not a technical
control — it is the governance answer, and §4 argues it is usually the right one.

## 4. What the arithmetic does not decide

The demonstration prints a list of questions its own numbers cannot answer, and the
list is the point:

1. **Consent.** Was permission obtained for *this* use, or for the original survey
   only? A general research-consent statement is not consent for open publication,
   and it is rarely consent for reuse in a later project by different people.
2. **Authority and sovereignty.** Whose decision is the release? For many
   Indigenous peoples and for many communities, data about their territory are
   governed by their own laws and institutions, and the relevant permission comes
   from them rather than from a research ethics board alone. A release plan that
   assumes otherwise is a plan to take a decision that is not the researcher's to
   take.
3. **Sensitive locations.** Aggregation counts records; it does not protect a site
   whose *existence* is the sensitive fact. Cultural, sacred, archaeological and
   burial sites, endangered-species locations, and community water sources can be
   compromised by a coarse map, because the sensitivity is in the location itself.
4. **Benefit.** Who gains from the analysis? A study that publishes results about a
   region without any pathway for the people there to benefit — through
   co-authorship, capacity, employment, local data control, or use of the findings —
   is an extractive relationship regardless of its statistical quality.
5. **Onward use.** A public release cannot be recalled. Data published openly may
   later be used in ways the original participants would refuse, and no licence
   prevents that in practice.

## 5. Principles commonly applied

The frameworks below are widely referenced in geoscience and environmental data.
They are described here at the level of principle; the specifics of any framework,
and any legal obligations, vary by jurisdiction and must be checked against current
published guidance and against the data holders' own requirements.

| Framework | What it says, in outline | What it changes in a release plan |
|---|---|---|
| **FAIR** (Findable, Accessible, Interoperable, Reusable) | data should be discoverable and reusable through good metadata and clear licensing | metadata and licensing are part of the deliverable, not an afterthought |
| **CARE** principles (collective benefit, authority to control, responsibility, ethics) | data governance should serve the people the data describe, whose authority over the data is primary | the decision to release, and the conditions, rest with the data holders; benefits are negotiated, not assumed |
| **Free, prior and informed consent** | permission is sought before work begins, without coercion, with full information about consequences | consent is a process with a timetable, not a form signed once |
| **Data sovereignty** | data about a people are governed by that people's laws and institutions | repository choice, licensing and even metadata may be subject to another jurisdiction's rules |

The practical consequence of the CARE principles for a data plan is that the
technical controls of §3 become *options presented to the data holders* rather than
decisions taken for them. The usual shape of the resulting agreement is:

1. **a negotiated release**: which layers, at which resolution, under which licence,
   with a named contact for future requests;
2. **a controlled-access tier** for the sensitive or fine-resolution components,
   with a stated review process and a record of who has access;
3. **a co-analysis arrangement** where results are discussed with the data holders
   before publication, so that interpretation and framing are shared;
4. **a benefit pathway**, stated in advance: co-authorship, training, data
   infrastructure, or a commitment about how the findings will be used.

None of this is measured by the $k$-anonymity number of §3, and the number should
never be used to *justify* a release decision — only to inform one.

## 6. Assumptions and regime of validity

1. **The generator is a caricature.** A uniform clustering model with Gaussian
   spreads stands in for settlement geography; real populations are more structured
   and their auxiliary information is richer, so the measured risks are illustrative.
2. **The adversary model is one of many.** Singleton counts are the simplest
   disclosure channel. Differencing releases, inference from the published totals,
   and re-identification through a third-party data set are all outside the
   arithmetic here.
3. **$k$-anonymity is a static guarantee.** It says nothing about composition
   across releases over time, which is the common failure in practice.
4. **Location is not always the sensitive attribute.** For some geoscience data the
   sensitive fact is the measurement, the land owner's identity, or the existence of
   the site; a privacy metric built on counts cannot see any of those.
5. **Ethics review is necessary and not sufficient.** An institutional review
   addresses a subset of the questions in §4; it is not a substitute for an
   agreement with the data holders.

## The honest summary

On a synthetic $800$-record survey in a $20 \times 20$ km region, a $1$ km release
contains $79$ singleton cells out of $286$ occupied, while $5$ km and $10$ km
releases contain none. A $k = 5$ suppression at $1$ km removes $540$ of $800$
records and retains $260$ ($32.5\%$); at $k = 10$ it retains $10$ ($1.2\%$), while
at $2$ km with $k = 10$ it retains $541$ ($67.6\%$) and at $5$ km with $k = 10$ it
retains $792$ ($99.0\%$). The quantitative conclusions are that coarsening
dominates suppression, that $k$-anonymity protects a single release but not a series
of them, and that at fine resolution the honest options are controlled access or no
release. What the arithmetic cannot decide is who has the authority to release, what
consent covers, whether a location is itself the sensitive attribute, and who
benefits — questions answered by agreement with the data holders, informed by these
numbers rather than settled by them.

## Python demonstration

[`code/data_ethics_geoscience_demo.py`](./code/data_ethics_geoscience_demo.py)
prints every number quoted above. It:

1. generates the synthetic survey and prints the release question, with an explicit
   statement that the arithmetic measures one narrow quantity and cannot decide the
   governance question;
2. prints occupied cells, mean counts and singleton cells for four cell sizes;
3. prints the suppression table — cells suppressed, records suppressed and records
   retained with percentages — for four cell sizes and three values of $k$;
4. prints the list of questions the arithmetic does not decide, and a `SYNTHETIC`
   provenance line stating that no real community or site is described.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_ethics_geoscience_demo.py
```

It runs in under 0.1 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/03-data-ethics-geoscience-exercises.md`](./exercises/03-data-ethics-geoscience-exercises.md)
and [`exercises/03-data-ethics-geoscience-solutions.md`](./exercises/03-data-ethics-geoscience-solutions.md).

## Mastery checkpoint

Without notes:

1. Define disclosure risk and utility for a spatial count release, and state why
   they trade.
2. Compute the retained fraction for a release whose cells hold 1, 3, 7, 20 and 60
   records under $k = 5$ and $k = 10$ suppression, taking the mean cell occupancy as
   the population share.
3. Explain in two sentences why two overlapping releases of the same region can
   defeat a $k = 10$ suppression applied to each separately.
4. A colleague argues that because the $k$-anonymity metric is satisfied, the
   release is ethical. State the three categories of question that argument leaves
   unanswered.

## Common pitfalls

1. **Treating $k$-anonymity as consent.** It is a disclosure control for one
   release, not permission from anyone.
2. **Applying suppression release by release.** Composition across releases recovers
   the suppressed cells.
3. **Assuming aggregation protects a site.** For some sites the location is the
   sensitive attribute.
4. **Choosing the resolution to maximise retained records.** The science decides the
   resolution; the privacy analysis then says what it costs.
5. **Reporting the metric as a justification.** It informs a negotiation; it does not
   settle it.
6. **Omitting the benefit pathway.** A technically careful release with no pathway
   for the community to benefit is still extractive.

## Where this is used

- **Release of survey, archaeological and cultural-heritage location data**, where
  the location is the sensitive attribute.
- **Community-based monitoring programmes**, where the data are collected by and
  with the community that governs them.
- **Endangered-species and protected-site mapping**, where precise coordinates are
  withheld or generalised.
- **Open-data policies for public agencies**, where FAIR and CARE pull in different
  directions and the resolution is a governance choice.
- **Reproducibility requirements**, where the push for open data must be reconciled
  with consent, sovereignty and confidentiality
  ([22-01-05](../../22-data-engineering-reproducibility/01-research-software-engineering/05-licensing-and-citation.md)).

## Related lessons

- [21-09-02 Honest Reporting of Uncertainty and Limitations](./02-reporting-uncertainty-ethics.md) —
  the reporting obligations that a data plan must complement.
- [21-09-01 Statistical Reproducibility, p-Hacking and Multiple Comparisons](./01-reproducibility-statistical.md) —
  the analysis-level integrity that open data serves.
- [23-01-03 Field Notebooks, Metadata and Data Provenance](../../23-field-methods-instruments/01-field-safety-and-planning/03-field-notebooks.md) —
  the metadata practice that makes a controlled release workable.
- [22-01-05 Licensing, Citation and Software Credit (CITATION.cff)](../../22-data-engineering-reproducibility/01-research-software-engineering/05-licensing-and-citation.md) —
  licensing as the technical expression of a data agreement.
- [17-06-04 Spatial Statistics, Autocorrelation and Hotspot Analysis](../../17-remote-sensing-gis/06-geospatial-analysis-advanced/04-spatial-statistics.md) —
  the analysis that coarsening or suppression degrades.

## Self-assessment checklist

- [ ] I can compute disclosure risk and utility for a release.
- [ ] I can compute the effect of a $k$ threshold on both.
- [ ] I can explain why coarsening dominates suppression here.
- [ ] I can name the four questions the metric cannot answer.
- [ ] I can outline what FAIR and the CARE principles each change.
- [ ] I can draft the four elements of a negotiated release agreement.
