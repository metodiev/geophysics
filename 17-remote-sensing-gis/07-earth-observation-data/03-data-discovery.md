---
id: 17-07-03
title: "Data Discovery, Access and Licensing"
level: intermediate
prereqs: ["17-07-01", "22-03-06"]
tags: [remote-sensing, earth-observation, metadata, catalogues, precision-recall, licensing]
---

# Data Discovery, Access and Licensing

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why data discovery is a search over *metadata* rather than over
   data, and why the metadata is itself a measurement with error.
2. **Write** the spatial and temporal predicates of a query as boolean
   functions of the record fields.
3. **Define** precision, recall and $F_1$ for a discovery query and **compute**
   them from a confusion table.
4. **Quantify** how increasing position error in a catalogue degrades both
   precision and recall simultaneously.
5. **Distinguish** "free to access", "free to redistribute" and "free to build
   on", and **state** which filtering a licence field permits.
6. **Recognise** the failure mode of a missing metadata field, which cannot be
   filtered by a query at all.
7. **Argue** why only an identifier plus a pinned version — not a description —
   makes a discovered result reproducible.

## Prerequisites

- [17-07-01 Landsat, Sentinel and MODIS Data Products](01-landsat-sentinel.md)
  — the products a catalogue indexes.
- [22-03-06 Metadata Standards](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md)
  — the vocabulary a record is written in.

> All models and data in this module are **SYNTHETIC**. The catalogue, its
> footprints, its metadata errors and its licence codes below are chosen
> teaching values. No real archive, portal or licence text is used, and no
> number is a measurement of any real catalogue.

## 1. Discovery is search over a description

You cannot look at every pixel in every archive. Discovery is therefore a search
over a **catalogue** — a database of *records*, each describing one asset by a
footprint, a time range, a resolution, a processing level, a licence and an
identifier. The crucial point is that a record is a *description*, and a
description is a measurement of the data, produced by a person or a pipeline,
with its own error.

This reframes the familiar frustration "the search found nothing, but the data
exist". The data always exist. What failed is that the *description* did not
overlap the query. A discovery query therefore has the same structure as any
detection problem: it can miss things that are there (false negatives) and
return things that are not (false positives), and both grow when the metadata is
sloppy.

## 2. Definitions

For a record with an axis-aligned bounding box
$\mathbf{b} = (x_0, y_0, x_1, y_1)$ in a projected plane and a time interval
$[t_s, t_e]$, and a region of interest (ROI) $\mathbf{w}$ over a window
$[t_0, t_1]$:

- **Spatial predicate.** Two boxes overlap (including touching) iff

$$
\text{overlap}(\mathbf{a}, \mathbf{b}) =
x_0^{a} \le x_1^{b} \;\wedge\; x_0^{b} \le x_1^{a} \;\wedge\;
y_0^{a} \le y_1^{b} \;\wedge\; y_0^{b} \le y_1^{a}.
$$

- **Temporal predicate.** The record's interval meets the window iff
  $t_s < t_1 \;\wedge\; t_0 < t_e$.
- **Query result.** The set of records satisfying *both*, using the **reported**
  footprint and time — because that is all the catalogue has.
- **Ground truth.** The set satisfying both using the **true** footprint and
  time. This is the set the user actually wanted.
- **Precision** $= \mathrm{TP}/(\mathrm{TP}+\mathrm{FP})$; **recall**
  $= \mathrm{TP}/(\mathrm{TP}+\mathrm{FN})$; $F_1 = 2PR/(P+R)$.

Precision answers "of what I was shown, how much was relevant?"; recall answers
"of what was relevant, how much was I shown?" They trade against each other, and
metadata error moves *both* the wrong way at once — which is why a discovery
problem is not solved by tuning a threshold.

## 3. Worked example 1 — measuring a query

Take the synthetic catalogue of
[`code/data_discovery_demo.py`](code/data_discovery_demo.py): $200$ records over
a $100\ \mathrm{km}\times100\ \mathrm{km}$ region and two years. The ROI is the
box $(40, 40, 60, 60)\ \mathrm{km}$ and the window is day $200$ to day $560$.
Metadata positions carry a Gaussian error with $\sigma = 4\ \mathrm{km}$.

- True matches (using true footprints): $16$.
- Returned (using reported footprints): $17$.
- $\mathrm{TP} = 13$, $\mathrm{FP} = 4$, $\mathrm{FN} = 3$.

Then

$$
P = \frac{13}{13+4} = 0.765, \qquad
R = \frac{13}{13+3} = 0.812, \qquad
F_1 = \frac{2 \times 0.765 \times 0.812}{0.765 + 0.812} = 0.788.
$$

Four of seventeen returned records do not actually overlap the ROI; three of
sixteen relevant records were never shown. **A correct query with correct logic
still has a $24\%$ false-discovery rate and a $19\%$ miss rate**, purely from
metadata error. This is the number a data user must carry, and it is almost
never reported.

## 4. Metadata error degrades both ways

The demonstration repeats the query while growing the position error
$\sigma$:

| $\sigma$ (km) | returned | TP | FP | FN | precision | recall |
|---|---|---|---|---|---|---|
| 0.0 | 20 | 20 | 0 | 0 | 1.000 | 1.000 |
| 2.0 | 22 | 22 | 0 | 1 | 1.000 | 0.957 |
| 4.0 | 27 | 23 | 4 | 3 | 0.852 | 0.885 |
| 8.0 | 18 | 11 | 7 | 6 | 0.611 | 0.647 |
| 16.0 | 21 | 6 | 15 | 12 | 0.286 | 0.333 |

The pattern is the honest core of this lesson. At $\sigma = 0$ the query is
perfect. As $\sigma$ grows, precision and recall **fall together**: the
catalogue is not answering the question you asked, it is answering a question
about a slightly shifted copy of your ROI. At $\sigma = 16\ \mathrm{km}$ —
comparable to the ROI's own half-width — precision is $0.286$ and recall
$0.333$: fewer than a third of the returned records matter, and two thirds of
the relevant ones are lost. No amount of query cleverness fixes this, because
the information is not in the metadata.

### 4.1 Why both metrics fall together

Consider a record whose true footprint just clips the edge of the ROI. Its
reported centre is displaced by a random vector of magnitude of order $\sigma$.
The record becomes a **false positive** if a true non-overlap is reported as an
overlap, and a **false negative** if a true overlap is reported as a
non-overlap; both require the displacement to carry the footprint *across* the
edge, and both become more likely as $\sigma$ grows. Because the displacement is
independent of relevance, the two error rates rise *together*, so precision and
recall fall together — unlike a stricter query threshold, which trades one
against the other.

Quantitatively, records within a boundary strip of width of order $2\sigma$ are
at risk; the expected fraction misclassified grows roughly linearly in $\sigma$
while the ROI is large compared with $\sigma$, then saturates when $\sigma$
approaches the ROI's own size. That is the shape of the table above: a slow fall
from $\sigma = 0$ to $4\ \mathrm{km}$, then a steep one at $8$ and
$16\ \mathrm{km}$. The decisive consequence is that **no threshold on the query
can undo this**, because the missing information — the true footprint — is not
in the metadata. Only a better catalogue, or a manual check, can.

## 5. Licensing: three permissions, not one

A record's licence is not a single "free / not free" flag. At minimum, three
permissions matter, and they are independent:

| Permission | Question it answers |
|---|---|
| Access | May I download it? |
| Redistribution | May I publish, mosaic or pass on the pixels? |
| Derivatives | May I publish a product built from it? |

The demonstration builds a result set of $17$ records with a synthetic
permission model. Of those, **14 are free to view but only 10 are free to
redistribute**; 4 permit neither redistribution nor derivatives (for example, a
registration-gated or restricted code). A project that plans to publish a
mosaic must filter on *redistribution*, not on *access*, and will lose four of
its fourteen viewable records. Discovering a record and being allowed to use it
are different questions, and only the second one matters at publication time.

### 5.1 The missing-field failure mode

Twelve of the two hundred records ($6\%$) carry **no licence field at all**. A
query that filters on licence cannot classify them: it must either drop them
(and lose potentially useful data) or include them (and risk a licence
violation). Neither is safe. The general lesson is that **an absent metadata
field is worse than an adverse one**, because an adverse value can be filtered
and an absent one cannot. Completeness of metadata is a correctness property of
the catalogue, not a nicety.

### 5.1 Quantifying the missing-field risk

Twelve of two hundred records ($6\%$) carry no licence field. For a query that
filters on licence, those twelve are unclassifiable, so the attainable recall is
capped at $94\%$ *before any spatial or temporal criterion is applied* — no
query design can recover a record whose permission is unknown. The practical
consequence is a forced choice: drop them (losing up to $6\%$ of relevant data,
and any of them that were usable) or include them (risking a licence violation).
The safe engineering response is to flag the missing field as a *record
defect*, quarantine those records for manual review, and report the quarantine
rate alongside the query's precision and recall — because a filter that silently
drops $6\%$ of the catalogue has changed the answer, not just cleaned it.

## 6. Identifiers and versions make discovery reproducible

Descriptive discovery — "snow scenes, winter, middle of the region" — ranks
candidates. Rerun it next month and the ranking changes, because records were
added and metadata edited. A result that cites only a description is therefore
not reproducible, even if every individual record is correct.

The fix is an **identifier** (a stable name for one asset) plus a **version** (a
stable name for one processing of it). Descriptive search finds the candidate;
the identifier freezes it. This is the same requirement as in
[17-07-02](02-cloud-platforms.md), applied to discovery: *search is fuzzy,
citation is exact.* A published result should cite identifiers and versions,
and a pipeline should store them, so that the same query reconstructs the same
set.

## 7. Assumptions and regime of validity

1. **Metadata error is random and unbiased.** The demonstration uses Gaussian
   position error; real catalogues often have *systematic* offsets (a datum
   mismatch, a swapped axis order), which are worse: they shift every record the
   same way, so the false positives and negatives are spatially structured.
2. **Footprints are axis-aligned boxes.** Real footprints may be polygons or
   multi-part; a box is an over-approximation that inflates false positives.
3. **"True" footprint is knowable.** In this synthetic setting it is; in
   practice it is the *best available* geometry, itself uncertain, so the
   measured precision and recall are estimates of an estimate.
4. **Licence codes map to permissions faithfully.** A synthetic matrix is
   unambiguous; real licence text is not, and legal review is outside the query.
5. **One record per asset.** Duplicated records inflate query results and are a
   common catalogue defect.

## 8. Worked example 2 — the cost of a stricter query

Suppose a query returns $100$ records of which $30$ are relevant. Adding a
stricter spatial filter (buffer the reported footprint inward by $5\ \mathrm{km}$)
removes $40$ records that were *relevant in their reported geometry* but drops
$6$ of the $30$ relevant ones. New counts: returned $60$, relevant $24$,
$\mathrm{FP} = 36$, $\mathrm{FN} = 6$.

$$
P_{\text{before}} = \frac{30}{100} = 0.300, \qquad
P_{\text{after}} = \frac{24}{60} = 0.400,
$$
$$
R_{\text{before}} = \frac{30}{30} = 1.000, \qquad
R_{\text{after}} = \frac{24}{30} = 0.800.
$$

Precision improved from $0.300$ to $0.400$; recall fell from $1.000$ to
$0.800$. The example makes the trade explicit: a stricter filter buys precision
with recall, and the right balance depends on whether a missed record is
expensive (as in a safety or monitoring study) or a spurious one is (as in a
download-limited study).

## Mastery checkpoint

Complete this without notes.

> A query returns $50$ records; the true relevant set has $40$; the overlap is
> $32$. **(a)** Compute precision, recall and $F_1$. **(b)** The catalogue's
> position error is then halved. State the expected direction of change in
> precision and in recall, and whether they must both improve. **(c)** Six of
> the returned records have no licence field. State the two unsafe options and
> the safe one. **(d)** State what must be recorded so that the query can be
> reproduced next year.

A worked version appears in the
[solutions](exercises/03-data-discovery-solutions.md).

## Common pitfalls

1. **Treating a catalogue as ground truth.** It is a description with error.
2. **Reporting a query result without a relevance measure.** Returning $17$
   records says nothing about how many mattered.
3. **Confusing access with redistribution.** Free to download is not free to
   publish.
4. **Ignoring missing fields.** They cannot be filtered and are a correctness
   risk.
5. **Citing a description instead of an identifier.** Descriptions are not
   stable.
6. **Assuming metadata error is random.** Systematic offsets are common and
   worse.
7. **Building geometry on unverified footprints.** A box is an approximation
   that alters the query.

## Related modules

- [17-07-02 Cloud Platforms: GEE, Copernicus, NASA Earthdata](02-cloud-platforms.md)
  — where a catalogue is queried and a reducer runs.
- [17-05-01 GIS Concepts: Layers, Attributes and Topology](../05-gis-fundamentals/01-gis-concepts.md)
  — footprints, attributes and the geometry a record carries.
- [22-03-06 Metadata Standards](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md)
  — the completeness requirement in formal terms.
- [21-01-01 Descriptive Statistics](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md)
  — precision and recall as estimated proportions.

## Materials

- Demonstration: [`code/data_discovery_demo.py`](code/data_discovery_demo.py)
  — catalogue, query measurement, metadata-error sweep and licence filtering.
- Exercises: [`exercises/03-data-discovery-exercises.md`](exercises/03-data-discovery-exercises.md)
  with [solutions](exercises/03-data-discovery-solutions.md).
