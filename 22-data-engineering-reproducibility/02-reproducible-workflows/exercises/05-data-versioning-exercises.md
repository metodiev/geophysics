# Exercises — 22-02-05 Data Versioning and Provenance Tracking

Attempt these before reading the
[solutions](./05-data-versioning-solutions.md). The lesson is
[05 Data Versioning and Provenance Tracking](../05-data-versioning.md). Storage
numbers refer to the **SYNTHETIC** model of `code/data_versioning_demo.py`:
$200 \times 200$ float64 grid (320.0 kB per version), 50 versions, $25 \times 25$
chunks (5.0 kB each, 64 per version), block edits of $30 \times 30$, a full
reprocessing every tenth version.

## ★ Foundational

**★1.** Define a data version and state the two properties of that definition, with
one consequence of each.

**★2.** For the demonstration's model: (a) compute the naive storage of 50 versions;
(b) compute the deduplicated storage given 514 unique chunks of 5.0 kB; (c) compute
the ratio. State which quantity would change if the 50 versions contained 20
reprocessings instead of 4.

**★3.** List the five provenance fields a derivation step must record, and state for
each the question it answers that a content hash alone cannot.

## ★★ Applied

**★★4.** A version series has 50 versions of a 320 kB product. A block edit touches
5 of 64 chunks on average; a reprocessing touches all 64.

(a) Estimate the stored bytes if every version were a block edit and there were no
reprocessings. (b) Estimate the stored bytes with reprocessings at every tenth
version. (c) State the general rule the two estimates illustrate.

**★★5.** A figure's pipeline reads three inputs (a catalogue, a velocity model and a
configuration file), runs two rules, and writes one output. Write its provenance
record as five fields per rule, and state which field is missing if the pipeline is
run by hand from a notebook.

**★★6.** The group's convention is to name files `catalogue_2024-05.csv`. State three
distinct failures this convention permits, and for each the recorded field that
would prevent it.

## ★★★ Research-oriented

**★★★7.** Design a versioning and provenance scheme for a sensor network that
appends 1 GB per day for five years: state the storage layout, the identifier scheme,
the retention policy for derived products, the metadata recorded per artefact, and the
annual storage under your scheme. State what your scheme cannot guarantee.

**★★★8.** The lesson's deduplication ratio depends on the chunk size relative to the
edit size. For a series of regional updates touching a contiguous $30 \times 30$
block, compute the stored bytes for chunk sizes 25, 30 and 50 (in each case state
chunks per version and the chunks touched by an edit), and state the design rule the
comparison implies. State when smaller chunks would *increase* storage.

**★★★9.** A group must reproduce a five-year-old result whose catalogue no longer
exists in its original version, but whose checksum is recorded in an old manifest.
Specify what can and cannot be established from the checksum alone, and describe the
minimum evidence that would let a reader decide whether a substitute catalogue is
adequate.
