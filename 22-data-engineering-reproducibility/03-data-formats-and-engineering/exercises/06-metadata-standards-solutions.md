# Solutions — 22-03-06 Metadata Standards and Controlled Vocabularies

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [06 Metadata Standards and Controlled Vocabularies](../06-metadata-standards.md).

---

## ★1 — What numbers alone cannot carry

A reader with only the numbers cannot recover: their **units**, their **coordinates**
(in space and time), the **convention for missing values**, the **flag or quality
state** of each value, the **processing** that produced them, and the **identity** of
the data set and its version. The six metadata items that supply these are, from the
file-format lesson: shape and dtype, units, coordinates, missing-value convention,
provenance, and compression/chunking. Only the first and last are format-level; the
rest are the writer's responsibility, which is why "we publish a netCDF file" is not a
metadata strategy.

## ★2 — Record-level completeness

(a) 152 of 200 records are complete: **76.0 %**.

(b) Using the printed omission rates (network 1.5 %, station 0 %, channel 1.5 %,
latitude 6.0 %, longitude 0.5 %, elevation 9.5 %, unit 6.5 %, start_time 1.5 %), the
product of completeness probabilities is

$$0.985 \times 1.000 \times 0.985 \times 0.940 \times 0.995 \times 0.905 \times 0.935
\times 0.985 = 0.717.$$

(c) The measured 76.0 % is higher than the product's 71.7 % because the product assumes
independence and the simulated omissions are independent draws, so the two should agree
in expectation; the difference of about four percentage points is sampling noise on 200
records (the standard error of a proportion near 0.72 with $n = 200$ is
$\sqrt{0.72 \times 0.28/200} = 3.2$ percentage points, so the discrepancy is within
1.3 standard errors).

## ★3 — Unit conversions

$2.5\ \mathrm{gal} \times 0.01 = 0.025\ \mathrm{m/s^{2}}$.

$1500\ \mathrm{nm/s^{2}} \times 10^{-9} = 1.5 \times 10^{-6}\ \mathrm{m/s^{2}}$ — a
typical weak-motion amplitude, which is the sanity check that the conversion went the
right way: the same number in gal would be $1.5 \times 10^{-5}$ gal, i.e.
$1.5 \times 10^{-7}\ \mathrm{m/s^{2}}$, and one of the two is off by the factor the
unit table says.

## ★★4 — Completeness with correlated omissions

(a) Six fields at 4 % each, independent: $(0.96)^{6} = 0.7827$, so **21.7 %** of records
are incomplete.

(b) Twelve fields at 4 %: $(0.96)^{12} = 0.6127$, so **38.7 %** incomplete. This is the
compounding that per-field reporting hides: every field looks fine.

(c) Six fields where two are missing together in 8 % of records and the other four in
2 %: the probability of completeness is

$$(1 - 0.08) \times (1 - 0.02)^{4} = 0.92 \times 0.9224 = 0.8486,$$

so **15.1 %** of records are incomplete. Compare with the independent model where the
same two fields are each missing in 4 %: $(0.96)^{2}(0.98)^{4} = 0.9216 \times 0.9224 =
0.850$. The two are nearly identical here — correlation matters less than the *marginal
rate* when the marginal rate is high — which is itself the lesson: to reduce
incompleteness, reduce the worst field, not the correlation. Where correlation bites is
when a whole provider is late: then a block of records is missing several fields at
once, and the independence-based estimate is optimistic for exactly the records you
care about.

## ★★5 — A value of 981 with a declared unit of m/s²

(a) Two hypotheses: (i) the value is genuinely
$981\ \mathrm{m/s^{2}}$, which is about $100g$ — physically implausible for a
seismological record and far outside any instrument's range; (ii) the declared unit is
wrong and the value is $981\ \mathrm{gal} = 9.81\ \mathrm{m/s^{2}}$, a plausible
strong-motion amplitude.

(b) The check is a **magnitude plausibility test after conversion to canonical units**,
using bounds derived from the channel type and the instrument's documented range. For a
strong-motion accelerometer, samples run from roughly $10^{-6}$ to a few
$\mathrm{m/s^{2}}$, with clipping at the instrument's full scale (often 2–4 g, i.e.
20–40 m/s²). So $981\ \mathrm{m/s^{2}}$ exceeds a bound of, say,
$50\ \mathrm{m/s^{2}}$ and is rejected as a unit error; $9.81\ \mathrm{m/s^{2}}$ passes.

(c) A genuine $0.98\ \mathrm{m/s^{2}}$ reading passes (it is within the range), so the
check does not convert the *unit identity* into a per-value test — it catches values
that are implausible *for the declared unit*, which is exactly the failure mode of a
wrong declaration with a large factor. The check must therefore be paired with the
cross-source comparison of §4 of the lesson for the small-factor case (a `cm/s²`
declaration where `m/s²` was meant changes values by 100× and may stay within bounds at
the small end).

## ★★6 — A hand-written duration parser

(a) Splitting on `T` and applying $M = 2\,592\,000$ s (30 days):

- `P1Y2M3DT4H5M6S`: date part `1Y2M3D` gives $1 \times 31\,557\,600 +
  2 \times 2\,592\,000 + 3 \times 86\,400 = 36\,901\,200$ s; the time part `4H5M6S`
  uses the same table, so $M$ is again treated as 30 days:
  $4 \times 3600 + 5 \times 2\,592\,000 + 6 = 12\,974\,406$ s; total
  **$49\,875\,606$ s** — which is wrong by a factor.
- `PT30M`: $30 \times 2\,592\,000 = 77\,760\,000$ s ≈ 900 days, instead of 30 minutes.

(b) Correct values: `P1Y2M3DT4H5M6S` $= 31\,557\,600 + 2 \times 2\,600\,016 +
259\,200 + 14\,400 + 300 + 6 = 37\,091\,538$ s (matching the demonstration), and
`PT30M` $= 1800$ s.

(c) The rule: **the designator's meaning depends on its position**, so a parser must
know whether it is in the date part or the time part; a single factor table and a
string split cannot be correct. The generalisation is that every interchange format
with context-dependent tokens needs a real parser, which is why the demonstration's
parser rejects malformed input rather than guessing.

## ★★★7 — A national strong-motion catalogue

**Required fields.** Network and station code; channel code; location code; latitude,
longitude and their datum; sensor and datalogger identifiers with their response
versions; sampling rate; units; start and end time with a time zone; instrument
orientation; and the data-quality flags of the QC procedure.

**Vocabularies and governance.** Sensor model names (from a manufacturer-maintained
list, mapped to a canonical family), channel codes (band, instrument, orientation),
units (an exact-conversion table plus a separate table of datum-dependent fields), and
quality flags. Governance: a documented proposal-and-review process, a version number
per vocabulary, a mapping table stored beside the data, and a published history of
changes — so a query answered today can be re-answered tomorrow with the same
semantics.

**Units and canonical forms.** Canonical $\mathrm{m/s^{2}}$ for acceleration,
$\mathrm{m}$ for elevation (with the vertical datum named), degrees north and east in a
named geodetic datum for coordinates, and seconds for durations. All declared values
are converted at entry and the raw declaration is stored alongside.

**Time conventions.** UTC with an explicit designator for instants; ISO 8601 with a
zone for intervals; a stated epoch for any numeric time; and a documented treatment of
leap seconds (typically a library's, recorded).

**Checks.** Schema and type validity; vocabulary membership; unit membership and
convertibility; magnitude plausibility per channel type; coordinate ranges and datum
presence; time ordering and span plausibility; and cross-field consistency (a sensor
that cannot sample at the declared rate).

**Rejection policy.** A record failing a check is **rejected with a reason** and
quarantined, not coerced; the rejection is reported in the release notes with counts
per reason, so the residue is visible and can be reduced by fixing sources.

**Published dictionary.** Field definitions, permitted values, units, ranges, the
meaning of the flag bits, the vocabulary versions, and a worked example record per
instrument family.

**The field expected to cause the most disputes.** The **elevation and its datum** (or,
in a strong-motion catalogue, the coordinates and their datum/time-dependent
realisation). Different providers use different vertical datums and geodetic
realisations, the differences reach tens of centimetres to a metre, and site response
and instrument-correction schemes are sensitive to them. The disputes are structural:
the value is not wrong, its reference surface is unstated or has changed, and every
consumer has a different use for it.

## ★★★8 — Measuring the dependence between missing fields

**Statistic.** The observed **co-missing rate** for every pair of fields: the fraction
of records missing both, compared with the product of their marginal missing rates
(the independent prediction). Report the ratio (observed/expected) per pair, and a
summary measure such as Cramér's $V$ or the mean pairwise lift over the field set.

**Pattern that would show correlation.** Co-missing ratios substantially above 1 for
specific pairs — the signature of a provider or an ingest route that omits a block of
fields together — together with a bimodal structure when the records are clustered by
provider (some providers complete, others missing the same fields). A useful diagnostic
is to compute the pairwise lift *within* each provider: correlation that survives
within providers is a data-model problem; correlation that disappears within providers
is a supplier problem.

**Consequence for the completeness estimate.** A consumer who multiplies per-field
completeness rates gets the independent prediction, which is *optimistic* for correlated
omissions — as the lesson's example shows, a block-missing pattern can leave a
substantial fraction of records missing several fields at once while every marginal
rate looks acceptable. The correct report is the **observed record-level completeness**
(measured directly) plus the co-missing matrix, so the consumer sees both the level and
the structure.

**What the measurement cannot tell you.** Anything about the records you do **not**
have: a catalogue that never received records from a station, or a provider that stopped
reporting, is invisible in a completeness table computed over the records you hold.
Completeness of a catalogue relative to the network it claims to represent requires an
external expectation — the station list, the deployment log, the expected channel count
— which is exactly the reconciliation gate of
[22-03-03](../03-data-pipelines.md) §6 applied to
metadata.

## ★★★9 — Harmonising vocabularies across five providers

**Proposing terms.** Any provider may propose a term with: a definition, the physical
or instrumental property it names, examples of records using it, and the proposed
canonical class it maps to. Proposals are reviewed by a small standing group with a
documented decision process and a published rationale for acceptance and rejection;
accepted terms enter the vocabulary with a version increment.

**Mapping.** Each provider's terms are mapped to canonical classes in a **mapping
table** that is versioned and published: `(provider, raw_term) → (canonical_class,
vocabulary_version, mapping_date)`. The mapping is data, not code, so it can be
reviewed, diffed and re-applied.

**Ambiguous mappings.** A term that maps to more than one canonical class (or to none)
must **not** be resolved silently. Options, in order of preference: (i) ask the provider
for a disambiguation rule (a location or time range where the term means one thing);
(ii) split the term into two canonical classes with a documented proportion, which is
honest only if the split is knowable; (iii) carry the term as `unknown` with the raw
string preserved, and report the count. Option (iii) is the fallback and must be visible
in every aggregate, because an `unknown` bucket that is large enough to matter changes
the interpretation of any grouped result.

**Release process for a mapping change.** A mapping change is a **new vocabulary
version**, published with a diff (which terms changed class, how many records are
affected), and applied prospectively to new ingests. Applying it retroactively requires
a *re-ingest with the new version*, so that a query answered under version $n$ can be
reproduced; the version used for a published result is recorded with the result
(the provenance practice of
[22-02-05](../../02-reproducible-workflows/05-data-versioning.md)).

**The failure of a silent retroactive change.** If the mapping is changed and applied
silently, an old query re-run today returns a different answer with no visible cause:
counts per class shift, which is exactly what a user treats as a change in the data.
The affected results are papers, instrument-reports and monitoring thresholds that were
calibrated under the old classes — and the harm is not merely the changed number but
the loss of the ability to say *which* mapping produced the published figure. Versioning
the vocabulary and recording the version with every result converts an unexplainable
discrepancy into a documented one.
