# Exercises — 03-04-07 Performance, dtypes and When to Leave Pandas

Attempt these **closed-book** before opening the
[solutions](./07-performance-pandas-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/performance_dtypes_demo.py`](../code/performance_dtypes_demo.py);
report its **actual** output. The table is **SYNTHETIC** — 600,000 rows generated
in-code, not the USGS catalogue and not an observation of the Earth.

**Timings from any run are machine-dependent.** Report the *ratios* you measure,
and say so; never quote a millisecond as a property of pandas.

---

## ★ Foundational

**★1.** A table has 10⁷ rows and four text columns, each holding one of a handful
of short labels.

(a) Using the demo's measured cost of 57.5 bytes per row per text column, estimate
the memory of the four columns.
(b) State whether that fits comfortably in a 4 GB process alongside anything else.
(c) What is the total if all four columns are converted to `category` with an
8-bit code per row?

---

**★2.** A magnitude column holds values around 3.0, stored as `float64`.

(a) How many significant decimal digits does `float32` carry?
(b) Estimate the absolute representation error for a value near 3.0.
(c) Is `float32` acceptable for a magnitude recorded to 0.1? Justify in one
sentence.

---

**★3.** The demo measures a Python loop summing depths above 30 km at 15.86 ms
against a boolean mask at 0.51 ms.

(a) Compute the speed-up ratio.
(b) Estimate the times both approaches would take on 10⁷ rows, assuming linear
scaling.
(c) State the one-line expression that replaces the loop.

---

**★4.** For each column, name the dtype you would choose and say why:

(a) `region`, 4 distinct values in 600,000 rows;
(b) `event_id`, 600,000 distinct values in 600,000 rows;
(c) `mw`, a measurement recorded to 0.1;
(d) `n_stations`, a count that can occasionally be missing.

---

## ★★ Applied

**★★5.** Run the demo, Section 2.

(a) Report the per-column memory before and after the categorical conversion.
(b) Report the total before and after, and the factor.
(c) Report the saving for `event_id`, and explain why it is different.
(d) Report the printed dtype of the text column before conversion.

---

**★★6.** Run the demo, Section 3.

(a) Report the largest absolute change introduced by the downcast.
(b) Report how many rows changed.
(c) Report the `exact equality preserved` line.
(d) Explain what a pipeline that groups by exact float equality would do
differently after this change.

---

**★★7.** Run the demo, Section 5.

(a) Report the three timings and their stated complexities.
(b) Which is fastest, and which is slowest?
(c) Report the largest absolute difference between the `rolling` and `cumsum`
results.
(d) State the lesson in one sentence, mentioning algorithm and library.

---

**★★8.** The `best_of` harness in the demo runs each function three times and
returns the minimum.

(a) Why the minimum rather than the mean?
(b) What does returning the result alongside the time let you check?
(c) Name one source of noise that three repeats does not remove, and one way to
reduce it.

---

## ★★★ Research-oriented

**★★★9.** A table of 200 GB must be processed on a machine with 16 GB of RAM.
The operations are: select rows by magnitude threshold, compute a per-region
count, and write the result.

(a) State why pandas cannot do this in one call, and what the failure looks like.
(b) Describe two approaches that keep the computation possible, and say which you
would choose and why.
(c) For the chunked approach, state the property the per-chunk aggregation must
have for chunk-then-combine to equal the whole-table answer, and give one common
aggregation that violates it.
(d) State one check you would run on the result to confirm the chunking was
correct.

---

**★★★10.** A colleague reports that replacing `Series.rolling(200).mean()` with
`numpy.convolve` made their moving average **100 times faster**, on a table of
50,000 rows.

(a) Explain why the demo's measurement (convolve 11.28 ms against rolling
2.76 ms) is not a contradiction.
(b) State two questions you would ask about the colleague's measurement.
(c) Give one reason a speed-up at 50,000 rows might not survive at 5,000,000 rows.
(d) Write the one-line instruction that would settle the disagreement.
