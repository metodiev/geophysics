# Solutions — 03-13-03 Profiling CPU and Memory: cProfile, line_profiler, memory_profiler

> **Read this after attempting the exercises, not before.** Values attributed to
> the demos are their actual output; derived values are shown with the arithmetic
> that produced them.

---

## ★1 — Overhead arithmetic

**(a)** Instrumented calls per run: $1 + 2000 + 1999 = 4000$. At 76 ns each that
is $4000 \times 76\ \mathrm{ns} = 0.304$ ms of pure profiler cost. Predicted
total: $0.22 + 0.30 = 0.52$ ms, a factor **2.36**. *Measured*: 0.50 ms, a factor
**2.30**. The prediction is 4% high, which is the accuracy you get from a
constant measured on a different call pattern. The important part of the
check is that the *form* is right: linear in the call count, independent of what
the call does.

**(b)** Zero instrumented calls from the ufuncs. A NumPy ufunc is an object whose
call slot is implemented in C, so calling `np.sqrt` creates no Python frame and
`lsprof` — which instruments Python frames — never sees it. The measured profile
for that workload reports 1024 calls total, made up of 200 for the workload
function, 200 for the gather and the rest from `build_inputs` and the `reduce`
method; the 80 000 ufunc invocations over the run are simply absent.

**(c)** *Count events, not seconds.* Function calls, iterations, array sizes and
allocated bytes are properties of the program and reproduce exactly; durations
are properties of the machine, the load and the caches. Quote the count as the
primary evidence and treat any timing as supporting detail with a stated method.

---

## ★2 — Crossover arithmetic

**(a)** `sum(list)`: $(1905.8 - 162.3)/(1024 - 64) = 1743.5/960 = 1.82$ ns per
element. `np.sum`: $(761.9 - 673.2)/960 = 0.092$ ns per element.

**(b)** Fitting $t = a + bn$ to the four rows for `np.sum` gives
$b \approx 0.092$ ns and $a \approx 673.2 - 0.092\times64 = 667$ ns. The
lesson's figure is "about 0.68 µs", consistent with this fit; the spread between
the four rows (673, 722, 716, 762 ns) is itself of order 0.1 µs and is the noise
floor of this kind of micro-benchmark.

**(c)** Setting $162.3 + 1.82(n-64) = 667 + 0.092(n-64)$ gives
$1.73(n-64) = 505$, so $n - 64 = 292$ and $n \approx 356$. The observed bracket
is between 256 (Python wins) and 384 (NumPy wins), which contains 356. The
crossover is a *prediction of a two-parameter model fitted to four points*, not a
fundamental constant — and the lesson's advice to put the threshold near 100 in
real code is deliberately conservative, because the exact value depends on the
machine and on whether a `.tolist()` conversion is needed.

---

## ★3 — Code or machine

| quantity | property of | how to test |
|---|---|---|
| `ncalls` | the code | assert it; it is an integer that reproduces exactly |
| `tottime` | the machine | never assert; quote with the method and the machine |
| number of elements in a temporary | the code | assert the shape of what `tracemalloc`/allocation tracking reports |
| peak traced memory | the code (mostly) | assert with a generous bound; the allocator's overhead varies |
| slow-down factor under `cProfile` | both | predict from the call count, then verify once per machine |

The distinction that makes this table useful: the left column of behaviours can
appear in a test suite, the right column cannot. A suite that asserts on
`tottime` fails on a busy CI runner for reasons that have nothing to do with the
change under review.

---

## ★4 — The three folklore claims

**(a)** The claim "`x*x` is faster than `x**2`" predicts ratio
$t_{x\cdot x}/t_{x^{**}} < 1$. The measured ratios are 1.083, 1.104 and 1.099 —
all above 1, in three independent repetitions of the whole paired experiment. So
the claim is not merely unsupported, it is **reversed**: `a*a` is reproducibly
about 9% slower, because NumPy 2.x fast-paths an integer power of two to
`np.square`, and `np.square` is a single-pass ufunc with no staging.

**(b)** Because with ratios 1.017, 0.999 and 1.008 the sign of the difference
flips between repetitions. A median of 1.008 looks like a 0.8% effect and is
really noise: the *method's resolution* at this size is a few per cent, so a
sub-per-cent difference cannot be resolved by it at all. Reporting the three
ratios rather than their median is what makes that visible, and it is the reason
the demo repeats the experiment three times.

**(c)** The measured factor is **1.07** (range 1.03–1.14 across repetitions),
against a textbook prediction of two to eight. The mechanism that hides the
penalty is NumPy's pairwise summation: the reduction is written as a balanced
tree of partial sums with cache blocking, so the working set at any instant is a
few cache lines rather than a full column of a 512 MB array. The stride penalty
is real but mostly amortised. The lesson's point is not that cache reasoning is
wrong; it is that the model's *quantitative* prediction was wrong by an order of
magnitude here, and only the measurement showed it.

---

## ★5 — Memory and the "obvious" version

**(a)** Because `np.sum(a * a)` must evaluate `a * a` first: a 4 000 000-element
float64 array is $4\times10^6 \times 8 = 32$ MB, and the peak traced memory is
exactly one such array. The peak is exact rather than approximate because
`tracemalloc` counts Python allocator requests, and this is a single large
allocation.

**(b)** `einsum` walks the arrays and accumulates a scalar in registers, so it
allocates nothing — but its kernel is a generic strided loop, whereas `a @ a`
dispatches to the BLAS `dot`, which is hand-tuned with SIMD. Measured: 57 µs
(`a @ a`) < 375 µs (`np.sum(a*a)`) < 435 µs (`einsum`). **Two different
explanations are needed for one ranking**, and only measuring both time and
memory separates them: `tracemalloc` alone would have predicted `einsum` to be as
fast as the dot.

**(c)** The hypothesis "the arithmetic is the cost" predicts that all three take
the same time, because all three perform the same $n$ multiplications and the
same $n-1$ additions. The measurement falsifies it: the spread is 7.6×, and the
memory difference (32 MB versus 0 MB) plus the kernel difference (generic versus
BLAS SIMD) account for it. This is the general shape of a performance hypothesis
worth testing: state what the naive model predicts, then check whether the
number agrees with the model or with the memory traffic.

---

## ★6 — Critiquing a benchmark protocol

**(a)** Three problems, any three of:

1. **One iteration each.** A single measurement has an uncertainty of tens of per
   cent (measured: 13% and 38% spreads on twelve successive timings of the same
   call), and no way to estimate it from the data.
2. **No warm-up.** The first call pays for lazy imports, page faults, JIT-like
   vector-unit wake-up and frequency scaling; the old code paid it, the new code
   did not, so the comparison is biased *against* the old code by construction.
3. **Sequential, not interleaved.** Any thermal or load drift between the two
   blocks is attributed to the rewrite.
4. **No order randomisation or repetition of the whole experiment.** Repeating the
   pair once allows the reader to see one number and no uncertainty.

**(b)** No. The measured noise floor of a single timing on this machine is 13% to
38% of the value, which is the same size as, or larger than, the claimed 15%
effect. The measurement cannot distinguish the claim from the noise, and a
difference of 15% measured this way should be reported as "not resolved".

**(c)** Interleave: for each of many rounds, time A then time B inside the same
loop; take the **median** of each side's per-round times; report the median ratio
and the fraction of rounds in which A lost. Repeat the whole experiment three
times and report the range of the ratio. Assert a conclusion only if the ratio
stays on the same side of 1.0 in every repetition — that is the protocol in
`benchmark_folklore_demo.py::paired_ratio` and `repeated_ratio`.

---

## ★7 — Profiling a NumPy inner loop

**(a)** The mechanism is that `lsprof` instruments Python *frames*, and a ufunc
call creates none: `np.sqrt` is an object with a C-level call slot, invoked
without a new frame. A callable in this module that *is* visible for the
converse reason is `math.fsum` inside `msd_kernel` — it appears in the profile
with `ncalls = 3999`, because it is a builtin that does create a frame. The
boundary is therefore "does the callee create a frame", not "is the callee
written in C".

**(b)** `profile.dump_stats("before.pstats")` then
`pstats.Stats("before.pstats")`:

- `strip_dirs()` merges entries that come from the same file, which is what you
  want when comparing two versions of one module;
- `print_callers()` answers "who called this?", which the default table cannot —
  useful when the same helper is hot from two call sites and you need to know
  which one;
- `Stats.add()` combines two dumps, so a before/after comparison is one table of
  deltas rather than two tables you read by eye.

**(c)** The test asserts on the line-hit count, not on time:

```python
def test_vectorised_path_has_no_python_loop():
    counts = line_hit_counts(nmo_gather_fast, 0.9, v, x)
    body = line_of_interest(nmo_gather_fast)
    assert counts.get(body, 0) == 0
```

An assertion on elapsed time would be the wrong mechanism because it fails
whenever the machine is busy and passes whenever it is idle, so it would be
disabled within a week. The hit count is zero for a vectorised implementation and
$n$ for a loop, on every machine, forever — which is exactly the property a test
should capture.

---

## ★8 — Separating two causes

**(a)** The causes are (i) **allocation**: `np.sum(a*a)` materialises a 32 MB
temporary, while `a @ a` does not; and (ii) **kernel quality**: BLAS `dot` is a
SIMD-tuned kernel, while `einsum` uses a generic strided loop. `tracemalloc`
measures (i) directly and cannot see (ii) at all — which is why the ranking
`a @ a < np.sum(a*a) < einsum` needs both measurements to explain.

**(b)** Preallocate the product once and reduce it repeatedly:

```python
prod = a * a                      # allocate once, outside the loop
# then compare, at equal allocation:
np.sum(prod)                      # reduction only, no temporary
np.einsum('i,i->', a, a)          # fused, no temporary
a @ a                             # fused, BLAS kernel
```

If `np.sum(prod)` and `einsum` come out close while `np.sum(a*a)` is far behind
both, then the difference between the latter two isolates kernel quality from
allocation. The measured result in this module is the opposite: `einsum` is
slower than `np.sum(a*a)` *despite* allocating nothing, so the kernel term is the
larger of the two for this size — a conclusion that the preallocated experiment
makes quantitative rather than anecdotal.

**(c)** More rounds narrow the uncertainty of the median ratio: the standard error
of a median falls roughly as $1/\sqrt{k}$ in the number of independent rounds, so
40 rounds resolves differences of a few per cent and 400 would resolve
sub-per-cent differences. What it **cannot** buy is a correction for a systematic
error — a non-representative array, a cache warmed by A but not B, a size that is
not the size in production. Those are controlled by the *design*, not by the
count, and no number of repetitions detects them.

---

## ★9 — Where to spend the week

**(a)** The profile says the I/O step: 55% of runtime against 30%, for two days
against five. Even a perfect elimination of the loop's cost saves 30%; a cache
that removes half the I/O time saves 27.5% — comparable — for 40% of the effort,
and the I/O change also removes load from a shared archive, which has a cost that
does not appear in the profile at all.

**(b)** Two facts the profile does not give you:

1. **The variance, not just the mean.** If the I/O step's 55% is dominated by
   tail latency — occasional 30-second stalls from a remote archive — then a
   cache removes the tail and changes the *usability* of the pipeline far more
   than its mean runtime, and the mean understates the benefit.
2. **The growth rate.** If the inner loop's cost scales with the survey size and
   the I/O step does not (because it is per *request*, and requests are batched),
   then the loop dominates the next survey and the week is better spent there.

**(c)** Two assertions that survive a refactor:

```python
def test_cache_is_hit_not_bypassed():
    fetch("kat.2024.001"); fetch("kat.2024.001")
    assert session.bytes_downloaded == first_fetch_size      # one download, not two

def test_inner_loop_has_no_python_framing():
    assert line_hit_counts(kernel, x).get(loop_body_line, 0) == 0
```

Both assert counts, both are deterministic, and both fail loudly if a later
refactor restores the behaviour the optimisation removed. An assertion on
elapsed time would fail on the machine that matters first — the CI runner.
