# Solutions — 22-02-05 Data Versioning and Provenance Tracking

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [05 Data Versioning and Provenance Tracking](../05-data-versioning.md).

---

## ★1 — Definition and its two properties

A **data version** is an immutable snapshot of a dataset with an identifier derived
from or attached to that snapshot.

- **Immutability.** Consequence: the identifier never lies — a change to the content
  creates a new version, so a figure that names a version names exactly one set of
  bytes.
- **Identification.** Consequence: a script, a paper and a future analysis can all
  refer to the same content without depending on a path, a filename or a date in
  someone's memory.

## ★2 — Storage of the demonstration's series

(a) Naive: $50 \times 320.0\ \text{kB} = 16\,000\ \text{kB} = 16.00$ MB.

(b) Deduplicated: $514 \times 5.0\ \text{kB} = 2570\ \text{kB} = 2.57$ MB.

(c) Ratio: $16.00/2.57 = 6.2\times$ — matching the printed value.

With **20** reprocessings instead of 4, each reprocessing contributes 64 new chunks,
so the unique-chunk count would rise to approximately

$$64 + 30 \times 4.8 + 20 \times 64 \approx 64 + 144 + 1280 = 1488\ \text{chunks},$$

i.e. $1488 \times 5.0\ \text{kB} = 7.44$ MB against the same 16.00 MB naive, a ratio
of only $2.2\times$. Reprocessings, not versions, set the storage.

## ★3 — The five provenance fields

| Field | Question it answers that a hash cannot |
|---|---|
| Inputs, by version identifier | *which* content the step consumed (the hash says the output's bytes, not its ancestry) |
| Code, by commit or tag | which implementation produced it |
| Parameters, including seeds | under which configuration, and whether randomness was controlled |
| Environment, by lock hash or image digest | which implementations of the operations ran |
| Output, by its own content hash | that the artefact you hold is the one recorded |

A hash alone answers "is this the artefact?"; only the first four fields answer "how
was it made?".

## ★★4 — Storage as a function of the edit pattern

(a) If every version were a block edit touching 5 of 64 chunks, with all 64 shared
after the first: unique chunks $= 64 + 49 \times 5 = 309$, i.e.
$309 \times 5.0\ \text{kB} = 1.55$ MB against 16.00 MB naive, a ratio of $10.3\times$.

(b) With a reprocessing every tenth version (4 reprocessings among versions 10, 20,
30, 40), each contributing 64 new chunks and each block edit about 4.8:

$$64 + 45 \times 4.8 + 4 \times 64 = 64 + 216 + 256 = 536\ \text{chunks} \approx
2.68\ \text{MB},$$

close to the demonstration's 2.57 MB (the small difference is the model's exact
per-edit chunk counts, which vary between 4 and 6).

(c) **The rule**: deduplicated storage grows with the number of *chunks that change*,
not the number of versions. A reprocessing changes every chunk and therefore costs
as much as a whole new copy, so the storage forecast should be written as
"versions plus reprocessings", and the way to reduce it is to reduce the
reprocessing rate.

## ★★5 — Provenance record for the two-rule pipeline

```yaml
rule prepare:
  inputs:
    catalogue: "doi:10.0000/catalogue.2024-05"     # identifier, not a path
    velocity:  "sha256:3f2a...c91"                 # content hash
    config:    "config/filter.yml@8c1d4e2"         # hash of the exact file
  code: "commit 8c1d4e2 of analysis-repo"
  parameters: {corner_hz: 2.0, taper: "hann", seed: 20261014}
  environment: "lock 9a11c0f (python 3.11.7)"
  output: "sha256:77bd...10e"

rule invert:
  inputs:
    prepared: "sha256:77bd...10e"
  code: "commit 8c1d4e2 of analysis-repo"
  parameters: {damping: 0.05}
  environment: "lock 9a11c0f (python 3.11.7)"
  output: "sha256:aa32...9f4"
```

The field missing when the pipeline is run by hand from a notebook is the **code**
field: a notebook's execution does not pin a commit, and the parameters field is
usually incomplete because values live in the session rather than in a recorded
configuration. The environment field is also typically absent, since the session's
interpreter is not a recorded artefact.

## ★★6 — Failures permitted by a date-named file

1. **Silent content change at the same name.** If the file `catalogue_2024-05.csv` is
   corrected and overwritten, the name still resolves and the analysis silently uses
   different bytes. *Prevented by*: a content hash recorded with the artefact.
2. **Two different files sharing a name across locations.** A copy in a personal
   directory and the copy in the shared store can differ while the name matches.
   *Prevented by*: a unique identifier (hash or DOI) plus a manifest of the
   authoritative location.
3. **Ambiguity about the processing state.** The date in the name records when the
   file was created, not which processing level it holds (raw, corrected, filtered).
   A later reader cannot tell whether the version is the one the analysis used.
   *Prevented by*: the derivation record naming the parent version and the rule that
   produced the file.

## ★★★7 — A sensor network with 1 GB per day for five years

**Storage layout.** Raw data are append-only and immutable, written as one file per
station-day (or per station-hour for dense networks) in a self-describing format,
with each file content-addressed by its hash. Derived products (quality-controlled
series, aggregates, model inputs) live in a separate namespace and are stored
content-addressed with chunking chosen at the timescale of the common queries
(for example one chunk per station-month).

**Identifier scheme.** Every raw file has a hash; every derived product has a hash
plus a derivation record naming its input hashes, the code commit and the parameters;
every *published* dataset (a quarterly release, say) gets a persistent identifier
(DOI) pointing at a manifest listing the hashes.

**Retention for derived products.** Derived products are regenerable from raw plus
the provenance record, so they are kept for a bounded window (say the last two
releases) and regenerated on demand; raw data are kept indefinitely. This is the
distinction between irreplaceable observed data and replaceable derived data. The
manifest for a published release is kept indefinitely, because without it the DOI
resolves to nothing checkable.

**Metadata per artefact.** Station identifier, instrument, sampling rate, time span,
units, calibration state, the hash, the parent hashes for derived products, and the
code commit — plus the quality flags of
[22-03-05](../../03-data-formats-and-engineering/05-data-quality-control.md).

**Annual storage.** Raw: $1\ \text{GB/day} \times 365 = 365\ \text{GB/year}$, so
$1.83$ TB over five years with no deduplication (raw data are appended, so
deduplication gains nothing). Retaining two derived releases at, say, 0.2 GB/day
each costs $2 \times 0.2 \times 365 = 146\ \text{GB/year}$. Total on the order of
**0.5 TB/year**, dominated by raw data — which is why the retention decision should
be made explicitly and in a data management plan.

**What the scheme cannot guarantee.** That the raw files are *correct* (a failed
sensor writes perfect bytes), and that a future reader can interpret them without
the metadata that was never recorded at the time — a calibration applied before
archiving is invisible to the hash.

## ★★★8 — Chunk size versus edit size

Edit: a contiguous $30 \times 30$ block. Grid $200 \times 200$.

| Chunk | Chunks per version | Chunks touched by the edit | Bytes per touched chunk | Bytes per edit |
|---|---|---|---|---|
| $25 \times 25$ | $8 \times 8 = 64$ | $4$–$6$, mean $\approx 4.8$ | $25^2 \times 8 = 5.0$ kB | $\approx 24$ kB |
| $30 \times 30$ | $7 \times 7 = 49$ | $1$–$4$, mean $\approx 3.2$ | $30^2 \times 8 = 7.2$ kB | $\approx 23$ kB |
| $50 \times 50$ | $4 \times 4 = 16$ | $1$–$4$, mean $\approx 2.6$ | $50^2 \times 8 = 20$ kB | $\approx 52$ kB |

(The per-dimension counts: a 30-wide interval touches 2 chunks of size 25 usually
and 3 when it straddles a boundary; 1 or 2 chunks of size 30; 1 or 2 chunks of size
50. The expected counts above are the products of the per-dimension expectations and
are approximate.)

**Design rule.** Storage per edit is minimised when the chunk size is close to the
edit size, and the $25$ and $30$ columns are within 5 % of each other — the
improvement from matching chunk to edit size is modest, while the *fragmentation*
cost of too-small chunks and the *over-copying* cost of too-large chunks are both
clear. A chunk of $50$ costs twice the bytes per edit of a chunk of $25$–$30$
because each touched chunk is four times larger and the touched count only halves.

**When smaller chunks increase storage.** When the edit is large or scattered:
a whole-grid reprocessing touches every chunk, so storing 256 small chunks per
version costs the same bytes but adds per-chunk metadata and index entries; and a
scattered edit approaches a full reprocessing at any chunk size. Below some size,
the hash and index overhead per chunk exceeds the saving — a design factor this
model does not include and a real system measures.

## ★★★9 — Reproducing from a checksum alone

**What the checksum establishes.** That the bytes the group holds *now* can be
tested against the recorded checksum: if they match, the content is exactly the
original; if they do not, the content is known not to be the original. That is all:
the checksum carries no information about the data's content, so it cannot
reconstruct a lost file, and it cannot tell you *how* a substitute differs.

**What it cannot establish.** Whether a substitute is adequate — a different
catalogue could be larger, smaller, or shifted in space or time, and all three would
change results in ways the checksum cannot detect.

**Minimum evidence for adequacy.** Compare the substitute with the original on the
*features the analysis depends on*, not on the file as a whole:

1. **Catalogue-level summaries** recorded with the original if available: number of
   events, magnitude-of-completeness curve, spatial and temporal coverage bounds,
   per-station counts. If the original's summaries were not recorded, this is the
   evidence that is missing.
2. **The analysis's sensitivity.** Rerun the analysis on the substitute and on any
   surviving subset of the original (even a partial copy), and report the difference
   in the published quantity against its uncertainty. A substitute is adequate if the
   published result is unchanged within the stated uncertainty and the comparison
   covers the data range the figure uses.
3. **Documentation of the difference.** The catalogue provider's version history,
   stating what changed between the original and the substitute version.

The report should say plainly what was established (a rerun on a documented
substitute, with a stated difference) and what was not (a rerun on the original
bytes, which is no longer possible).
