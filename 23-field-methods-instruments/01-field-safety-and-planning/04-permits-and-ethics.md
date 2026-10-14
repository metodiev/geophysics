---
id: 23-01-04
title: "Permits, Land Access, Cultural Heritage and Ethics"
level: intermediate
prereqs: ["23-01-02", "21-09-03"]
estimated_minutes: 75
tags: [fieldwork, permits, land-access, cultural-heritage, ethics, consent]
---

# Permits, Land Access, Cultural Heritage and Ethics

## Learning objectives

By the end of this lesson you will be able to:

1. **Identify** the parties with standing over a survey area and **classify** what
   each can grant, refuse or require.
2. **Compute** the probability that an $M$-parcel permission chain succeeds, the
   expected number of refusals, and the per-parcel probability needed for a
   stated overall success probability.
3. **Compute** the probability that a survey line of length $L$ clips a protected
   zone of areal coverage $a$, and **measure** it against a simulation.
4. **Compute** the increase in excluded area caused by a mandated buffer
   $\pm b$ around a zone of width $d$.
5. **Compare** an all-or-nothing consent protocol with a parcel-level protocol
   and **state** the factor by which the publishable fraction changes.
6. **Model** the resolution of access issues week by week and **derive** the lead
   time a mobilisation date implies.
7. **State** what free, prior and informed consent requires in practice and what
   an agreement does not settle.

All parcel counts, probabilities, zone coverages and buffer widths in this lesson
are **SYNTHETIC** teaching values printed by the demonstration. This lesson is
arithmetic and process design; it is **not legal advice**, and the applicable
rules depend on the jurisdiction, the land and the community. Every specific
requirement must be checked with the responsible authority and with the affected
community.

## Prerequisites

- [02 Planning a Field Campaign: Objectives, Permits, Logistics](02-field-planning.md) —
  where permissions enter the schedule as the critical path.
- [21-09-03 Data Ethics, Indigenous Data Sovereignty and Geoscience](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/03-data-ethics-geoscience.md) —
  the data-governance side of the same obligations.

## 1. Intuition: permission is a chain, not a checklist

A survey crosses land that belongs to other people. Getting onto it is not one
approval but a sequence of them, and a sequence of probabilities multiplies. With
25 parcels and an 80 % chance of agreement on each, the chance that *every*
parcel is agreed is 0.378 %. The survey is not 80 % likely to happen; it is
almost certainly incomplete before it starts.

This single piece of arithmetic reorganises the whole planning problem:

- **Access is a design constraint, not a formality.** If unanimity is required,
  the design must be robust to gaps, or the survey must be split into parcels
  that can be treated independently.
- **The marginal value of a refusal is not uniform.** Losing one parcel in the
  middle of a grid breaks the coverage; losing an isolated corner may not matter.
- **Lead time is set by other people.** Permission processes run on the
  timescales of landholders, councils and communities, not on the field season.

## 2. Who has standing

| Party | Can grant / refuse | Typically also requires |
|---|---|---|
| Landowner or title holder | Physical access to the parcel | Insurance, a written agreement, restoration |
| Tenant, leaseholder or land manager | Practical access, in many cases a veto | Notification, timing constraints around crops or stock |
| Indigenous peoples and local communities | Consent, especially where rights are recognised in law or asserted | Free, prior and informed consent, benefit sharing, data agreements |
| Heritage or antiquities authority | Permission to disturb ground; conditions on work near known sites | Assessment, reporting of finds, stop-work procedures |
| Environmental regulator | Permits for disturbance, protected species, watercourses | Season windows, mitigation measures |
| Local government | Road use, noise, working hours | Notifications |
| National or regional government | Research permits, export of samples | Reporting, sample deposition |
| Military or border authority | Access to restricted areas | Escort, timing |
| Utility and infrastructure operators | Crossing pipelines, cables, railways | Supervision, stand-off distances |

Two features of this table matter more than its length. First, these parties are
**not substitutable**: a permit from the environmental regulator does not
substitute for a landowner's agreement. Second, they are **not simultaneous** by
nature — several of them condition their approval on the others.

## 3. The permission chain

Let $M$ be the number of independent approvals required and $p$ the probability
that any one is granted within the planning horizon. Then

$$P(\text{all granted}) = p^{M}, \qquad
\mathbb{E}[\text{refusals}] = M(1-p), \qquad
p_{\text{required}} = (1-\beta)^{1/M}$$

for an overall success probability $1-\beta$. The demonstration reports

| $M$ | $p$ | $P(\text{all granted})$ | expected refusals | $p$ needed for 90 % overall |
|---|---|---|---|---|
| 25 | 0.80 | 0.003778 | 5.0 | 0.99579 |
| 60 | 0.80 | 0.000002 | 12.0 | 0.99825 |
| 25 | 0.95 | 0.277390 | 1.3 | 0.99579 |

Read the last column carefully: with 60 parcels, per-parcel agreement must exceed
99.8 % before the whole survey is 90 % likely to be fully permitted. That is not
an achievable target, and its unachievability is the useful conclusion — it says
the *design* must change, not the persuasion.

Three design responses follow directly:

1. **Make parcels independent.** If each parcel is surveyed, processed and
   reported as a unit, one refusal costs one unit instead of the campaign. The
   overall result then degrades gracefully, and the deliverable becomes "the
   areas we could access, with the gaps stated".
2. **Reduce $M$ by negotiating with representative bodies** where that is the
   legitimate route, rather than with $M$ individuals.
3. **Fund the permission work as a work package** with its own lead time, not as
   a prerequisite that someone does "when they get a chance".

## 4. Protected zones and the buffer arithmetic

A **protected zone** is an area where ground disturbance is restricted: an
archaeological site, a cemetery, a sacred place, a registered heritage area, a
protected habitat, or a utility easement. In practice the survey team works from
a mask — a polygon layer of zones supplied by the authority and, where
appropriate, by the community — plus a mandated **buffer** around each zone.

Two quantities determine the cost of compliance.

**(a) The chance that a line clips a zone.** Model a line of length $L$ as
$n = L/\ell$ independent segments of length $\ell$, each inside a zone with
probability equal to the areal coverage $a$. Then

$$P(\text{clipping}) = 1 - (1-a)^{n} .$$

With $a = 0.005$ (0.5 % coverage), $L = 2000\ \mathrm{m}$ and
$\ell = 10\ \mathrm{m}$ ($n = 200$), this gives 0.6330. The demonstration's
simulation measured **79 of 120 lines (65.8 %)** clipping a zone, against an
expectation of $120 \times 0.6330 = 76.0$; the difference is well within the
binomial scatter of $\sqrt{120 \times 0.633 \times 0.367} = 5.3$. It also
measured 114 clipped segments against an expected
$120 \times 200 \times 0.005 = 120$.

The lesson of this number is that a *small average* coverage does not mean a small
number of affected lines. At this line length and this coverage, roughly two
lines in three touch something, so compliance has to be checked line by line
against a mask — an average is not an operational answer.

**(b) What a buffer costs.** If a zone has width $d$ and the rule is a buffer of
$\pm b$, the excluded strip has width $d + 2b$, so the excluded area grows by the
factor

$$F = \frac{d + 2b}{d}.$$

For $d = 30\ \mathrm{m}$ and $b = 25\ \mathrm{m}$: $F = 80/30 = 2.667$, and the
excluded fraction rises from 0.50 % of the survey area to 1.33 %. The buffer, not
the archaeology, sets the loss — and unlike the archaeology it is negotiable, in
writing, with the authority, if the geophysical method is non-invasive and the
case is made explicitly.

## 5. Consent, and why unanimity is a trap

Consider a consent question put to each of $M$ parties, granted independently
with probability $p_c = 0.85$. Two protocol designs:

| Protocol | 25 parcels | 60 parcels |
|---|---|---|
| Publish only if every party consents | 0.017198 (1.7 %) | 0.000058 (0.006 %) |
| Publish at the level each party consented to | 0.85 (85 %) | 0.85 (85 %) |

The ratio between them is **49×** at 25 parcels and **14 598×** at 60. The same
underlying willingness produces either a near-total loss of the dataset or an
85 % release, depending entirely on whether agreement is sought as a single
collective decision or per parcel.

This is not an argument for avoiding collective decisions: where a community
speaks as a collective, its decision *is* the decision, and designing around it
would be a violation. It is an argument for **designing the data model to match
the consent model** — if consent is per parcel, the data structure, the archive
and the publication must all be capable of representing a parcel-level embargo.
Deciding that after the data are collected is not possible.

The general standard that governs this in research with Indigenous peoples is
**free, prior and informed consent**: free of coercion, sought before the
activity begins, and informed about the purpose, methods, risks and intended use
of the data. Its practical requirements — who is consulted, over what period, and
with what data-sharing and benefit-sharing agreements — are specific to the
community and must be established with them, not assumed by the researcher.

## 6. Lead time: access resolves slowly

Access issues resolve at a rate set by other people's calendars. With $K$
unresolved parcels and a per-week resolution probability $p_w$ (independent
across parcels and weeks),

$$\mathbb{E}[\text{unresolved after } n \text{ weeks}] = K(1-p_w)^{n}, \qquad
P(\text{all resolved}) = \left[1-(1-p_w)^{n}\right]^{K}.$$

The demonstration's table for $K = 8$ and $p_w = 0.40$:

| Weeks | Expected unresolved | $P(\text{all resolved})$ |
|---|---|---|
| 2 | 2.880 | 0.0281 |
| 4 | 1.037 | 0.3294 |
| 6 | 0.373 | 0.6823 |
| 10 | 0.048 | 0.9526 |

Note the shape: the *expected* number falls quickly — most parcels are resolved
early — but the *probability that everything is resolved* lags far behind,
because it is a statement about the worst parcel. Ten weeks is needed for a 95 %
chance that nothing is outstanding. Permission work must therefore start in the
season before the field season, and its progress has to be reported as a
probability, not as a count of parcels.

## 7. Assumptions and regime of validity

1. **Independence of approvals.** Real permission processes are correlated: one
   hostile council, one shared access road or one adverse local story moves many
   parties at once, which makes $p^{M}$ optimistic. The approximation is a sizing
   tool, not a forecast.
2. **Constant $p$.** Approval probability varies with the parcel, the approach,
   the season and the reputation of the team.
3. **Uniform areal coverage** in the clipping model. Real zones cluster, so
   $1-(1-a)^n$ understates the chance of clipping where zones are dense and
   overstates it where they are absent.
4. **A single buffer width.** Buffers are usually set case by case; the arithmetic
   is a planning estimate.
5. **Registers are incomplete.** A heritage register records what is known and
   reported. Absence from a register is not evidence of absence, which is why
   ground disturbance procedures must include a stop-work rule and a find
   protocol.
6. **Consent is not a transaction.** The probabilities above model a *process*,
   not a right; no arithmetic converts an obligation into an option.

## 8. The honest summary

- Permissions multiply: 25 parcels at 80 % give a 0.378 % chance of a complete
  survey.
- Design for graceful degradation, and report the gaps.
- A 0.5 % protected-zone coverage still clipped 79 of 120 lines; check line by
  line against a mask.
- A $\pm 25\ \mathrm{m}$ buffer around a 30 m zone multiplies the excluded area by
  2.667.
- All-or-nothing consent can cost a factor of 49 in publishable data; the data
  model must match the consent model.
- Access resolves on other people's timescales: expect ten weeks for a 95 %
  chance of clearing eight outstanding parcels.

## 9. Python demonstration

[`code/permits_and_ethics_demo.py`](./code/permits_and_ethics_demo.py) prints
every number quoted above. It:

1. tabulates the permission chain for three (parcel count, probability) pairs,
   including the per-parcel probability needed for a 90 % overall success;
2. simulates 120 lines against a 0.5 % protected-zone mask and reports the
   predicted and measured clipping;
3. computes the increase in excluded area produced by a mandated buffer;
4. contrasts all-or-nothing and parcel-level consent at 25 and 60 parcels;
5. tabulates the expected number of unresolved access issues and the probability
   that all are resolved, for four lead times.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/01-field-safety-and-planning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python permits_and_ethics_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/04-permits-and-ethics-exercises.md`](./exercises/04-permits-and-ethics-exercises.md)
and
[`exercises/04-permits-and-ethics-solutions.md`](./exercises/04-permits-and-ethics-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A survey needs 40 parcels, each agreed with probability 0.85. Compute the
   probability that all are agreed and the expected number of refusals. What
   per-parcel probability would give a 95 % chance of a complete survey?
2. A zone is 20 m wide and the rule mandates a $\pm 15\ \mathrm{m}$ buffer. By
   what factor does the excluded area grow? If the zone coverage is 0.8 % of the
   survey area, what is the excluded fraction after buffering?
3. A line is 1500 m long, sampled at 10 m, over an area with 0.8 % protected
   coverage. Compute the probability that the line clips a zone.
4. State two design responses to a permission chain with a low $p^{M}$, and one
   thing that no arithmetic justifies.

## 12. Common pitfalls

1. **Treating permission as a formality with a fixed lead time.** It is a
   probabilistic process with an unbounded tail.
2. **Assuming a small average coverage means few affected lines.** It meant 79 of
   120 here.
3. **Forgetting the buffer when estimating the loss.** It tripled the excluded
   area in the demonstration.
4. **Designing the data model after the consent negotiation.** An embargo that
   cannot be represented cannot be honoured.
5. **Reading absence from a register as absence of a site.** Registers are
   incomplete by construction.
6. **Treating consent as a signature.** It is an ongoing relationship with
   conditions attached to data use, not a one-off transaction.
7. **Ignoring the community's own research protocols.** They take precedence over
   the team's convenience and are usually knowable in advance.

## 13. Where this is used

- Every land-based survey: mineral exploration, groundwater, geotechnical
  investigation, archaeology, and academic field programmes.
- Seismic network deployment, where stations remain on private land for years and
  the access agreement must cover maintenance visits —
  [23-02-05 Deployment, Orientation, Timing and Metadata](../02-seismic-instruments-and-fieldwork/05-seismic-deployment.md).
- Marine campaigns, where permits cover territorial waters, exclusive economic
  zones, marine protected areas and, for some areas, cultural heritage on the
  seabed.
- Borehole and laboratory programmes, where sample export and deposition
  requirements apply.
- Any project publishing data that identifies communities or places of cultural
  significance.

## 14. Related lessons

- [02 Planning a Field Campaign: Objectives, Permits, Logistics](02-field-planning.md) —
  where this lead time enters the schedule and the cost.
- [03 Field Notebooks, Metadata and Data Provenance](03-field-notebooks.md) —
  where consent conditions and access restrictions are recorded.
- [21-09-03 Data Ethics, Indigenous Data Sovereignty and Geoscience](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/03-data-ethics-geoscience.md) —
  the governance framework this lesson applies in the field.
- [22-05-04 Research Data Management Plans and FAIR Principles](../../22-data-engineering-reproducibility/05-collaboration-and-project-management/04-research-data-management-plan.md) —
  where consent and embargo conditions are written into the data plan.
- [23-07-02 Case Study: An ERT Survey from Design to Report](../07-field-campaign-case-studies/02-case-study-ert-survey.md) —
  a campaign in which access and archaeology set the design.

## 15. Self-assessment checklist

- [ ] I can list the parties with standing and what each can grant or refuse.
- [ ] I can compute $p^{M}$ and the per-parcel probability a target requires.
- [ ] I can compute the clipping probability of a line over a zone mask.
- [ ] I can compute the excluded-area factor of a buffer.
- [ ] I can compare all-or-nothing and parcel-level consent.
- [ ] I can derive the lead time implied by a required probability of clearance.
