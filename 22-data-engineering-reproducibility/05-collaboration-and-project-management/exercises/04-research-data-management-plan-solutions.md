# Solutions — 22-05-04 Research Data Management Plans and FAIR Principles

> Read after attempting. Numbers are computed here and match the demonstration's printed
> output. Lesson:
> [04 Research Data Management Plans and FAIR Principles](../04-research-data-management-plan.md).

---

## ★1 — Checkable versus prose

A checkable plan states, for each commitment, an **artefact and a number**: what is kept,
where, for how long, at what cost, and who is responsible. A prose plan states an
intention.

- Prose: "Data will be retained as required by the funder and made available on request."
- Checkable: "Raw waveforms (approximately 40 TB) are archived at <identifier> with
  checksums; retention is ten years from project end; the responsible person is the PI;
  the cost is budgeted at 25 units per TB-year; a restore test is run each March and its
  record kept in the repository."

The second can be verified at review and costed in advance; the first cannot.

## ★2 — The forecast

(a) After three years: raw $3 \times 8 = 24$ TB; derived $3 \times 3 \times 1.5 = 13.5$
TB; total **37.5 TB** (the printed cumulative).

(b) Project total (five years): raw 40 TB, derived 22.5 TB, total **62.5 TB**. Archived:
$62.5 \times (1 + 10/5) = 187.5$ TB — the printed value.

(c) Multiplier $= 187.5/62.5 = 3.0$ — the archive decision multiplies the volume (and the
cost) by three, and it is made once at the start.

## ★3 — FAIR as artefacts

| Facet | Artefact | Reviewer's check |
|---|---|---|
| Findable | a persistent identifier with a landing page | resolve the identifier; is the title/author/description there? |
| Accessible | a documented access route or a stated restriction with a contact | follow the route; does it reach the data or an explicit access procedure? |
| Interoperable | an open format plus a schema with declared units and vocabularies | open the file; are the variables, units and codes documented? |
| Reusable | a licence, provenance and a data dictionary | read the licence; can the data be reused legally and interpreted correctly? |

## ★★4 — A 20 TB/year project

(a) Project total: raw $3 \times 20 = 60$ TB; derived $3 \times 8 = 24$ TB; total
**84 TB**. Archived (five years): $84 \times (1 + 5/3) = 84 \times 2.667 = 224$ TB.

(b) Multiplier $2.667$. Cost: project phase $84 \times 5 \times 25/2 = 5\,250$ units
(averaged at half-full); archive phase $224 \times 25 = 5\,600$ units — so the archive
phase costs slightly more than the project phase it follows, which is the pattern the
demonstration shows more strongly (3 906 against 15 625 units) because of its longer
retention.

(c) Delete the **derived** tier first: it is regenerable from raw plus the code, so the
cost is compute and time rather than information — provided the raw tier and the
provenance record survive. Deleting raw instead costs permanently: the retained aggregates
cannot be un-averaged, a nonlinear calibration cannot be reapplied, and a new method at
higher resolution is impossible.

## ★★5 — Independent copies

(a) $0.03^{1} = 0.03000$; $0.03^{2} = 0.00090$; $0.03^{3} = 0.000027$. The exponent is the
whole content: the first copy changes the risk by a factor of 33, the second by another
33.

(b) Pairs that are **not** independent: (i) two copies on the same file server under
different directory names; (ii) a laptop copy and its synchronised cloud account, when the
cloud account is the same credential that an attacker or a mis-click would delete; (iii) a
nightly backup and the primary store, when both are administered by the same person with
the same script — a bug deletes both.

(c) The **restore test**: restoring an artefact from each copy into a clean environment and
verifying its checksum. Without it, a "copy" may be a partial, encrypted, corrupt or
inaccessible set of bytes — the common failure is a backup that has never been restored.

## ★★6 — A plan's FAIR score

(a) Mean of (0.9, 0.7, 0.6, 0.8, 0.4, 0.3) $= 3.7/6 = 0.617$ — the printed value.

(b) Fix first: the **retention policy** (0.3) — write it with horizons per tier, an owner
and the deletion rules; and the **data dictionary** (0.4) — publish the variable
definitions, units and code lists. Both are documents, so both are cheap and both are
required for the archive to remain interpretable.

(c) Both weakest items are **reusability** facets (a dictionary is what makes data
interpretable without its author; a retention policy is what makes it still exist when
someone wants to reuse it), so the coincidence is coherent: the two items that score
lowest are the two that serve *future* users rather than the current project. That is the
typical finding and the reason reusability is the facet that decays first.

## ★★★7 — A plan for a five-year, three-institution project

**Inventory.** Field data: 40 TB over five years, mostly continuous waveforms and
campaign records, with field notes, instrument calibrations and site metadata. Model
output: 15 TB/year, of which a small fraction is the analysed product and the rest is
restartable intermediate state.

**Standards.** Waveforms in a standard self-describing format with station/channel
metadata following a community convention; model output in a chunked array format with CF
conventions; units SI with the convention stated; vocabularies from the community lists
where they exist, and a project list where they do not; identifiers from the institutional
archive, plus checksums.

**Access and licence.** Field and model data openly licensed with a citation requirement
and `CITATION.cff` files; the restricted dataset (say, a licensed third-party product)
made accessible through a documented procedure with a named contact and a stated
restriction, and its identifier resolving to the procedure rather than to the data.

**Retention per tier.** Raw field data: ten years, at two sites plus an archive (three
failure domains). Intermediate model state: 90 days, deleted automatically. Analysed
products: ten years, regenerable. Metadata and provenance: ten years, and effectively
permanent because they are small.

**Failure domains and restore tests.** Three: two institutions' storage systems and one
independent archive service. Annual restore test of a random sample from each domain, with
the record kept in the project repository; the failures that count (a domain unreachable
for a week) are rehearsed once.

**Roles and cost.** A named data steward per institution, a PI accountable for the plan,
annual cost stated in TB-years plus effort (the steward's time is the item funders
underestimate). The cost forecast is written for both horizons — project and retention —
because the retention cost outlives the grant.

**The commitment I would negotiate.** The **ten-year retention of the full-resolution raw
data** for all 40 TB: the scientifically defensible alternative is full resolution for a
documented subset (the calibration and reference channels, the periods used in published
results) and decimated or aggregated products for the rest, with the criterion written into
the plan. That is a science decision, so it belongs in negotiation with the funder rather
than in a unilateral budget cut after the project ends.

## ★★★8 — Measuring whether an archive is FAIR

**Artefacts inspected.** For a sample of datasets: the landing page and the identifier
resolution; the metadata record against a stated schema; the licence file or field; the
data dictionary; the format's openness; the checksums and version history; and the access
route (an attempt to fetch a small part).

**Checks per facet.** *Findable*: does the identifier resolve, and does the landing page
carry title, authors, description and keywords? *Accessible*: does the documented route
work, and for restricted data does it reach a procedure with a contact? *Interoperable*:
does the file open with an independent reader, and are units and vocabularies declared
against a schema? *Reusable*: is there a licence (and is it applicable to *this* data?),
a data dictionary, provenance and contact for questions?

**Scoring rule.** Score each facet per dataset as pass/fail with the failing artefact
named, and aggregate by facet rather than by dataset: "80 % of datasets are findable,
40 % reusable" is actionable, an overall 0.6 is not.

**Two ways the measurement could overstate compliance.** (i) **Metadata that exists but is
wrong** — a landing page naming the wrong authors, a unit field filled with a plausible
but incorrect value; only an independent check against the data or the authors detects it.
(ii) **A licence that is stated but not applicable** — a licence text copied from another
dataset, or one that conflicts with the source's terms; detecting that requires reading
the source's terms, not the archive's field.

**What it cannot tell you.** Whether the data are *correct* or scientifically useful: FAIR
describes the packaging, and an archive can be perfectly findable, accessible,
interoperable and reusable while containing a mis-calibrated instrument's output.

## ★★★9 — A 200 TB archive with a 100 TB budget

**Three policies.**

1. **Keep a subset at full resolution.** Selection criterion: the channels and periods
   used by published results, plus the calibration and reference channels, plus a random
   sample of the rest for future methods. *Scientific consequence*: the archived subset
   supports reproduction and method development on those channels; studies needing other
   periods or channels must re-observe, which for a past earthquake sequence is
   impossible. State the criterion and the sample's size explicitly.
2. **Downsample the rest.** Keep decimated time series (which preserve low-frequency
   information and long-term trends) and drop the high-rate band beyond a stated
   frequency. *Scientific consequence*: high-frequency studies (small events, tremor,
   spectral content) are excluded from the archived spans — a real loss, and a quantifiable
   one: state the frequency band that is lost and the research questions that depend on it.
3. **Seek additional funding or a partner archive.** Cost the retention honestly (the
   demonstration's arithmetic gives the multiplier) and approach an institutional or
   national archive, or include retention in the next proposal. *Scientific consequence*:
   none if successful, and a deadline if not — so it needs a fallback.

**The measurement that defends the choice.** Report, per policy: the volume retained, the
number of published results whose reproduction remains possible, the frequency band and
periods lost, the cost per year, and the requests the archive has received by channel and
period (the demand evidence). The last item is the one funders find most persuasive: a
documented usage history justifies keeping what is used and retiring what is not.

**What the choice cannot be decided by.** Cost alone. The decision is about which science
remains possible, and it requires knowing the group's (and the community's) research
priorities — a scientific judgement that the storage bill cannot make, and that a
different group would make differently.
