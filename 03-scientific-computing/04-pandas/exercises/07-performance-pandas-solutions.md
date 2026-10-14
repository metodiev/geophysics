# Solutions — 03-04-07 Performance, dtypes and When to Leave Pandas

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output from one run on one machine. The table is
> SYNTHETIC. Timings are machine-dependent; the ratios are the content.

---

## ★1 — Memory arithmetic

**(a)** `10⁷ rows × 4 columns × 57.5 bytes ≈ 2.3 × 10⁹ bytes = 2.3 GB`. (The
57.5 bytes per row per text column is the demo's measurement: 34.5 MB for 600,000
rows of `region`.)

**(b)** No. A 4 GB process holds the four text columns plus whatever else the
analysis needs — a copy during a merge, a temporary in an expression, the
interpreter — and pandas makes copies freely. A table that nominally occupies
2.3 GB will routinely exceed 4 GB in use.

**(c)** With one 8-bit code per row, four columns cost
`10⁷ × 4 × 1 byte = 40 MB`, plus the dictionaries (a few hundred bytes each).
That is roughly a factor of 57 smaller, and it is the single largest structural
saving available.

---

## ★2 — float32 precision

**(a)** About **7** significant decimal digits (the IEEE-754 binary32 mantissa is
24 bits, giving `log10(2²⁴) ≈ 7.2`).

**(b)** Relative precision ≈ `1.2 × 10⁻⁷`, so for a value near 3.0 the absolute
error is about `3.0 × 1.2 × 10⁻⁷ ≈ 3.6 × 10⁻⁷`. The demo's measured maximum for
the real column was `4.578 × 10⁻⁷` magnitudes, consistent with that estimate.

**(c)** Acceptable. The measurement resolution is 0.1 and the representation error
is six orders of magnitude smaller, so no recorded value can be altered by the
downcast in any way that matters — but the equality check in ★6(c) still has to be
done, because "no value is altered" is a claim about the *measurement*, not about
the *bits*.

---

## ★3 — Loop against mask

**(a)** `15.86 / 0.51 ≈ 31.1`. The demo prints `31.38x` for the run captured in
the lesson; either figure is "about thirty times".

**(b)** Both scale linearly in the row count, so multiply by `10⁷/6 × 10⁵ ≈ 16.7`:
the loop takes about **265 ms** and the mask about **8.5 ms**. Still a quarter of
a second for the loop, which is why a loop inside a loop — over groups, over
files, over parameters — is where the time actually goes.

**(c)**

```python
df.loc[df["depth_km"] > 30.0, "depth_km"].sum()
```

---

## ★4 — Dtype choices

**(a)** `category`. Four distinct values in 600,000 rows gives the ~98 per cent
saving the demo measures, and the label set is naturally fixed.

**(b)** `str` (in pandas 3) or `object`. An identifier is high-cardinality, so
`category` would store a 600,000-entry dictionary and save nothing — the demo
measures exactly 0.0 % for `event_id`.

**(c)** `float64`, unless memory forces otherwise and the equality check passes.
Magnitudes are small, the column is cheap (3.3 per cent of the frame), and
`float64` removes the rounding question entirely. `float32` is defensible here
because the measurement resolution is 0.1, but it must be documented.

**(d)** A nullable integer dtype (`Int64`) or `float64` with `NaN`. A plain
`int64` cannot represent "missing"; assigning `NaN` to it either raises or upcasts
the whole column to `float64`, and an upcast that happens silently in the middle
of a pipeline is the kind of change that alters a later `groupby` result.

---

## ★5 — Categorising

**(a)** `region` 34.5 → 0.6 MB; `agency` 34.2 → 0.6 MB; `mag_type` 30.6 → 0.6 MB;
`event_id` 33.6 → 33.6 MB (unchanged). Numeric columns are unchanged.

**(b)** 147.3 MB → 49.8 MB, a factor of **2.96**.

**(c)** **0.0 %**, because `event_id` has 600,000 distinct values in 600,000 rows.
A category stores one dictionary entry per distinct label plus one code per row,
so with one label per row you pay for the dictionary *and* the codes — strictly
worse than the plain column in the general case, and no better here.

**(d)** `<StringDtype(storage='python', na_value=nan)>`, printed as `str` in a
dtype listing. This is the pandas 3 change from `object`, and it matters to any
code that branches on `dtype == object`.

---

## ★6 — The cost of a downcast

**(a)** `4.578e-07` magnitudes.

**(b)** **575,550** of 600,000 rows changed.

**(c)** `exact equality preserved  : False`.

**(d)** Grouping by exact float equality (`df.groupby("mw")` or a `==` mask)
produces a **different partition** after the downcast: values that were distinct
in `float64` can collide, and values that were equal can separate, because the
rounding is to binary rather than to the recorded decimal. Magnitudes that were
recorded as, say, 2.4 and 2.5 may still differ, but two values equal to 14
significant figures can now compare unequal. Every count, mean and join key built
on exact float equality is therefore at risk — and the fix is to bin explicitly
(`pd.cut`, or a round to the recorded resolution and convert to an integer key)
rather than to rely on representation.

---

## ★7 — The moving average

**(a)** `Series.rolling(200).mean()` **2.76 ms**, O(n) running sum;
`numpy.convolve` **11.28 ms**, O(n × window); `numpy.cumsum` difference
**1.42 ms**, O(n) running sum.

**(b)** Fastest: the NumPy `cumsum` difference. Slowest: `numpy.convolve`.

**(c)** `1.732e-10` km (rolling against cumsum), and `1.066e-14` km (rolling
against convolve) — both at the level of floating-point accumulation, far below
any geophysical meaning.

**(d)** The algorithm dominates: `rolling` and the `cumsum` difference both use an
O(n) running sum and beat `convolve`'s O(n × window) dot products, so the choice
of library is second-order compared with the choice of recurrence.

---

## ★8 — The timing harness

**(a)** Because the measurements are one-sided: cache misses, a garbage
collection, a background process and scheduler pre-emption can only make a run
*slower*. The minimum is therefore the best available estimate of the intrinsic
cost, and the spread between the maximum and minimum estimates the noise.
A mean would be contaminated by the tail.

**(b)** That both arms computed the same thing. An optimisation that changed the
answer is not an optimisation, and the cheapest guard against that is to compare
the returned objects — with a tolerance, because floating-point summation order
differs (the demo measures a relative difference of `4.96e-16` between the loop
and the mask).

**(c)** Thermal throttling, frequency scaling and the state of the machine's cache
between arms are not removed by repeats, because the arm that runs second may
face a different clock. Reduce it by interleaving the arms (run A, B, A, B, …) and
comparing the minima, or by reporting the ratio from a single interleaved batch
rather than the absolute times.

---

## ★9 — A 200 GB table on a 16 GB machine

**(a)** pandas materialises a whole column at a time and makes copies during
filtering, grouping and concatenation, so loading the table requires roughly its
size in RAM and the operations require more on top. The failure looks like
`MemoryError` — or, worse, the machine swapping until the process is killed, with
a total runtime that is far longer than the work justified.

**(b)** Two approaches:

- **A database.** Load the data once into a columnar store (or query it in place),
  and run the filtered aggregate as SQL so the engine streams the rows and
  touches only the named columns. This is what the demo's SQLite comparison is
  pointing at, even though SQLite won on speed there.
- **Chunked processing.** Read the table in row-chunks (`read_csv(..., chunksize=
  n)`, Parquet row groups, or a columnar/array format), aggregate each chunk, and
  combine the partial aggregates.

I would choose chunked processing if the aggregation is combinable (see (c)) and
the data are already in files, because it needs no new infrastructure and keeps
the pandas API; a database if the table will be queried repeatedly and by others,
because the query becomes a reviewable artefact.

**(c)** The per-chunk aggregation must be **combinable**: applying it to the union
of the combined partial results must equal applying it to the whole table. Counts,
sums, minima and maxima are combinable. A **median**, a **quantile**, or a
**count of distinct values** is not — the median of chunk medians is not the
median, because the chunks have different sizes and different distributions, and
the distinct count double-counts values appearing in more than one chunk.

**(d)** Compare against a ground truth on a subset. Run the chunked pipeline on
the first, say, 2 GB of the data *as if it were the whole table*, and run the same
computation directly with pandas on that subset, then require agreement to
floating-point tolerance. The chunking is then tested on a case where the answer
is known, which is the only way to distinguish a correct streaming result from a
plausible one.

---

## ★10 — A claimed 100× speed-up

**(a)** It is not a contradiction, because the two measurements are of different
quantities. The demo times a 200-point window over 600,000 rows and finds
`convolve` **slower**; the colleague reports a 100× speed-up at 50,000 rows. The
outcome depends on the window length relative to the row count (`convolve` costs
`n × w`, `rolling` costs `n`), on what the two arms actually compute (edge
handling and NaN semantics differ), and on the machine. A claim about speed is a
claim about a *specific* computation on a *specific* machine, and neither
measurement transfers.

**(b)** Two questions: **what exactly did each arm compute** — do the outputs
agree, including the edges and any NaNs? And **what was measured** — a best-of-N
minimum, or a single `time.time()` around a call that included the pandas
construction of the array itself? Both are common sources of an apparent order-of-
magnitude win that disappears on inspection.

**(c)** At 50,000 rows the whole array and its temporaries fit comfortably in
cache, so constant-factor differences (interpreter overhead, object allocation)
dominate. At 5,000,000 rows the computation is memory-bandwidth bound and
`convolve`'s 200× larger arithmetic count becomes the bottleneck, so a win driven
by per-call overhead can invert.

**(d)** One instruction settles it: *measure both, on the same machine, in the
same process, interleaved, returning both the time and the maximum absolute
difference between the two outputs.* If the outputs agree and the ratio holds in
the interleaved run, the claim is supported; if the outputs differ, the comparison
was never between two implementations of the same thing.
