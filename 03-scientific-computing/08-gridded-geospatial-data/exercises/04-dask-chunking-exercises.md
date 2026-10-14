# Exercises — 03-08-04 Chunking with Dask for Out-of-Core Analysis

Attempt these **closed-book** before opening the
[solutions](./04-dask-chunking-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/dask_chunking_demo.py`](../code/dask_chunking_demo.py); report its
**actual** output. Nothing is timed: the measurements are task counts and byte
footprints. All fields are **SYNTHETIC**.

---

## ★ Foundational

**★1.** Define `npartitions`, `chunks` and `chunksize` for a dask array, and give
the relation between `chunk footprint` and `dtype.itemsize`.

**★2.** A float64 array is 4000 × 4000.
(a) What is `nbytes`?
(b) How many chunks at `(1000, 1000)`?
(c) What is the chunk footprint in bytes and in MiB?

**★3.** Explain in one sentence why a reduction over $n$ chunks costs $O(n)$ tasks
rather than $O(1)$.

**★4.** State two operations that force each chunk to see its neighbours, and the
concept that describes the additional data they must obtain.

---

## ★★ Applied

**★★5.** Run the demo, Sections 1 and 2.
(a) Report `nbytes`, `npartitions` and the task count for the sum of the 2000 ×
2000 float64 array at 500 × 500 chunks.
(b) Report the task counts for chunk sizes 2000, 1000, 500, 250 and 100.
(c) Plot (or tabulate) task count against chunk count and describe the growth.

**★★6.** Run the demo, Section 3.
(a) Report the three rechunked means of the deterministic field and the largest
difference from the reference.
(b) State what that difference means in ulp terms for a value near 0.5.
(c) Would a bit-for-bit reproducibility policy survive? Justify.

**★★7.** Run the demo, Section 4.
(a) Report the three means of the dask-generated random array and the maximum
absolute difference between two chunkings.
(b) State the rule that follows.

**★★8.** Run the demo, Section 8.
(a) Report the `npartitions`, maximum chunk size and `polyfit` task count for the
three chunk layouts.
(b) Explain the factor-of-15 difference in task count in terms of which chunks must
be gathered.

---

## ★★★ Research-oriented

**★★★9.** The halo arithmetic in the lesson states
$((c + 2r)/c)^{2}$ for a stencil of radius $r$ on $c \times c$ chunks. Verify it
empirically for `r = 1, 2, 5` and $c = 50, 100, 250$: for each combination, build
a chunked array, compute a `map_overlap`-based operation, and record the graph
node count. Report a table, and state where the formula holds and where the
constant overhead of the graph dominates.

**★★★10.** Design a chunk layout for a 0.25° global temperature cube
(720 × 721 × 1440 float32) analysed three ways: (a) a 40-year time series at a
single grid point; (b) a daily global map; (c) a per-pixel linear trend over the
full record. For each, give the layout, the chunk footprint in MiB, and the number
of chunks; then choose a compromise layout and quantify the cost to each query in
chunks read. State which of the three you would sacrifice and why.

**★★★11.** Write a 250–400 word note titled "Reproducibility rules for chunked
pipelines". It must cover: the chunk-invariance of deterministic reductions
(measured), the chunk-dependence of dask's random generator (measured), what an
archive must record to be reproducible, and one concrete failure you would expect
if a collaborator changes a chunk size without telling you.
