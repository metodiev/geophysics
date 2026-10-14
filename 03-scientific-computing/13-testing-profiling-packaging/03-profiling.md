---
id: 03-13-03
title: "Profiling CPU and Memory: cProfile, line_profiler, memory_profiler"
level: advanced
prereqs: ["03-13-02", "03-02-07", "03-02-08"]
estimated_minutes: 110
tags: [profiling, cprofile, timeit, tracemalloc, benchmarking, performance]
---

# Profiling CPU and Memory: cProfile, line_profiler, memory_profiler

Optimisation without measurement is guessing, and guessing about performance is
worse than guessing about almost anything else, because performance folklore is
abundant, plausible, and frequently false. This lesson is about measurement
protocol — what to count, what to time, when a timing is a result and when it is
noise — and about the discipline of falsifying your own assumptions before you
act on them.

The tools are the standard library's `cProfile` and `pstats`,
[`timeit`](https://docs.python.org/3/library/timeit.html),
[`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html), and, for
line-level resolution, `line_profiler` and `memory_profiler`. Neither of those
two is installed in this repository's environment — a fact stated plainly
because the demos here reconstruct their measurements with `sys.settrace` and
`tracemalloc` instead of pretending.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the one rule that makes a benchmark reproducible: count events,
   never seconds, and never report a single timing.
2. **Read** a `cProfile`/`pstats` table and say which columns are properties of
   the code and which of the machine.
3. **Explain** why NumPy ufunc calls are invisible to `cProfile`, and measure
   per-line hit counts when they are not enough.
4. **Measure** the profiler's own overhead and predict its size from the Python
   call count.
5. **Design** a paired A/B micro-benchmark, and report a median plus a
   fraction-of-rounds-lost statistic.
6. **Falsify** three widely repeated NumPy performance claims, and say which one
   survived.
7. **Find** a memory bottleneck with `tracemalloc` and connect it to the timing.

## Prerequisites

- [03-13-02 Testing Numerical Code Against Analytic Solutions](./02-testing-scientific-code.md)
  — why a count is a reproducible measurement and a residual is a reproducible
  value.
- [03-02-07 Memory Layout, Views and Performance](../02-numpy/07-memory-performance.md)
  — strides, contiguity and temporaries.
- [03-02-08 Vectorisation Patterns](../02-numpy/08-vectorisation-patterns.md)
  — the idioms whose performance this lesson measures.

## 1. The protocol, before any tool

A timing is a measurement of the machine, the load and the caches at one instant.
A count is a measurement of the program. Everything in this lesson follows from
that asymmetry.

The demonstration measures the same call, `np.sum` on a million doubles, twelve
times in a row:

```
run  1: 143.46 us    run  7: 134.38 us
run  2: 139.75 us    run  8: 137.58 us
...
min 134.38 us   median 140.04 us   max 152.08 us
```

The spread is **13% of the minimum** — and in a second run of the same twelve
measurements it was 38%. This is a quiet laptop. On a shared CI runner the
spread is larger. A benchmark that runs an operation once and prints the elapsed
time has a measurement uncertainty of tens of per cent and no way to know it.

Four rules follow.

1. **Warm up.** The first call pays for lazy imports, page faults and frequency
   scaling. Discard it.
2. **Repeat and take an order statistic.** The minimum is the least contaminated
   by other processes; the median is more representative of the typical cost.
   Report both, or report the median and the spread.
3. **Interleave A and B.** Measuring all of A, then all of B, attributes any
   drift in CPU frequency between the two blocks to the difference between the
   implementations. Alternating inside the same loop cancels the drift.
4. **Prefer counts.** Function calls, iterations, array sizes and allocated
   bytes are integers that reproduce exactly. Use them as the primary evidence
   and treat seconds as supporting detail.

## 2. `cProfile`: what it counts, and what it cannot see

`cProfile` is a deterministic profiler: it instruments calls and accumulates
them exactly, with no sampling. It therefore reports *exact* counts, and its
timings are the sum of observed durations.

The measured table for a 200-repetition workload that corrects a 400-trace
gather with a Python loop of scalar ufunc calls:

```
         1024 function calls in 0.021 seconds
   Ordered by: internal time
   ncalls  tottime  cumtime  filename:lineno(function)
      200    0.021    0.021  profiling_demo.py:47(nmo_gather)
      200    0.000    0.000  {method 'reduce' of 'numpy.ufunc' objects}
        1    0.000    0.021  profiling_demo.py:71(numpy_workload)
```

Read the counts first: 200 calls to `numpy_workload` and 200 to `nmo_gather`,
exactly one per repetition. Those integers are properties of the code and are
identical on any machine. The `tottime` column is not.

Now the limitation. The loop body contains 400 calls to `np.sqrt` per
repetition — 80,000 over the run — and **not one of them appears**. A NumPy
ufunc is an object whose callable slot is implemented in C. Calling it creates
no Python frame, and `lsprof` instruments Python frames. So:

> `cProfile` tells you *that* `nmo_gather` is hot, in its `tottime` column, and
> cannot tell you *which line inside it* is hot.

The same limitation applies to `math.sin`, list indexing, arithmetic between
Python floats, and C-level method calls on most extension types. It does *not*
apply to `math.fsum`, which registers as a builtin call — the boundary is
"does the callee create a frame", not "is the callee written in C".

### 2.1 The columns

| Column | Meaning | Property of |
|---|---|---|
| `ncalls` | times the callable was invoked | the code |
| `tottime` | time in the function, excluding callees | the machine |
| `percall` (first) | `tottime / ncalls` | mixed |
| `cumtime` | time including callees | the machine |
| `percall` (second) | `cumtime / primitive calls` | mixed |

`ncalls` written as `14/6` means 14 total calls of which 6 were primitive
(non-recursive). Recursion shows up here and nowhere else.

## 3. The profiler's own overhead, measured

`cProfile` adds cost per instrumented Python call. Measured on a function that
does nothing but increment a counter:

| calls | bare (ms) | under `cProfile` (ms) | ns per call | factor |
|---|---|---|---|---|
| 50 000 | 1.11 | 4.70 | 72 | 4.24× |
| 200 000 | 4.71 | 20.80 | 80 | 4.41× |

About **76 ns per Python call**, a constant independent of what the call does.
The slow-down factor is therefore that constant times the call count, divided by
the runtime — and it explains the two very different factors observed for two
realistic workloads:

| workload | bare (ms) | profiled (ms) | factor |
|---|---|---|---|
| NumPy-heavy loop (no Python frames in the body) | 4.43 | 4.75 | 1.07× |
| Python-heavy loop (one call per sample) | 0.22 | 0.50 | 2.30× |

The same profiler is nearly transparent on one program and materially distorting
on another. That is not a defect; it is the predictable consequence of a
per-frame cost. The practical rule: **quote the call count, and treat any
`percall` time as an estimate with an uncertainty of order 76 ns.**

## 4. Line-level measurement without `line_profiler`

`line_profiler` reports the same information per source line, with a time
column. Its count column is the part that survives a change of machine, and it
can be obtained from the standard library with `sys.settrace`. The measured
table for one call of the slow gather:

| line | hits | source |
|---|---|---|
| 53 | 1 | `out = np.empty_like(offsets_m, dtype=float)` |
| 54 | 401 | `for i in range(offsets_m.size):` |
| 55 | 400 | `out[i] = np.sqrt(t0_s**2 + (offsets_m[i] / v_rms[i]) ** 2)` |
| 56 | 1 | `return out` |

Three things are visible that `cProfile` could not show:

1. The hot line is the loop **body**, executed 400 times for 400 offsets — the
   line-ranked answer to the question `cProfile` left open.
2. The loop **header** is executed 401 times, once more than the body. An
   off-by-one in the loop condition is invisible to a stopwatch and immediate in
   a hit count.
3. The counts are exact integers. `assert counts[body] == n_traces` is a test
   that either passes everywhere or fails everywhere.

The same table makes the fix testable. A vectorised rewrite makes the loop-body
count **zero**, so the assertion that documents the intent is
`assert hits.get(body_line, 0) == 0` — a claim about the implementation's
asymptotic cost rather than about a duration.

## 5. `tracemalloc`: finding the allocation, not the arithmetic

`cProfile` says *where*. `tracemalloc` says *what was allocated*, and for NumPy
code that is often the more informative question. Measured peaks for four ways of
writing one inner product of a 4 000 000-element array (32 MB):

| expression | peak traced memory |
|---|---|
| `np.sum(a*a)` | 32.00 MB |
| `(a**2).sum()` | 32.00 MB |
| `a @ a` | 0.00 MB |
| `np.einsum('i,i->', a, a)` | 0.00 MB |

The arithmetic is identical in all four. The allocation is not: the first two
must materialise the whole product array before reducing it, one full-size
temporary per call. `a @ a` lets BLAS accumulate as it computes, and `einsum`
walks the arrays in place.

All four agree numerically — relative differences from `a @ a` were
$3.493\times10^{-16}$, $3.493\times10^{-16}$ and $5.822\times10^{-16}$, i.e. one
to three ulp. So the choice is purely about memory traffic and speed, and
`tracemalloc` is what falsifies the hypothesis "the arithmetic is the cost".

## 6. Micro-benchmarking, and five claims tested

### 6.1 The method

```python
def paired_ratio(f_a, f_b, calls_a=200, calls_b=200, rounds=40):
    for _ in range(5):
        f_a(); f_b()                      # warm up both sides
    times_a, times_b = [], []
    for _ in range(rounds):
        t0 = time.perf_counter()
        for _ in range(calls_a): f_a()
        times_a.append((time.perf_counter() - t0) / calls_a)
        t0 = time.perf_counter()
        for _ in range(calls_b): f_b()
        times_b.append((time.perf_counter() - t0) / calls_b)
    med_a, med_b = statistics.median(times_a), statistics.median(times_b)
    loses = sum(1 for x, y in zip(times_a, times_b) if x > y) / rounds
    return med_a, med_b, med_a / med_b, loses
```

The paired structure cancels frequency drift. The median resists outliers. The
`loses` fraction is the statistic that decides whether a difference exists at
all: **if the ratio crosses 1.0 between independent repetitions, the two
implementations are not distinguishable by this method**, however many decimals
the median has. Reporting three repetitions of the whole experiment, and the
range of the ratio, is the cheapest honesty available.

### 6.2 The claims

| # | Claim | Measured | Verdict |
|---|---|---|---|
| C1 | "`x * x` is faster than `x ** 2`" | ratios 1.083, 1.104, 1.099 (all > 1) | **contradicted** — `a*a` is ~9% slower |
| C2 | "`np.sqrt(x)` is faster than `x ** 0.5`" | ratios 1.017, 0.999, 1.008 | **not supported** — the ratio crosses 1.0 |
| C3 | "summing along axis 0 is cache-hostile" | median ratio 1.07 (range 1.03–1.14) | **small but real** — not the 2–8× that cache reasoning predicts |
| C4 | "`np.vectorize` speeds up a Python function" | 60.0 ms vs 0.17 ms, ratio **353×** | **confirmed, in the opposite direction** |
| C5 | "`np.sum(a*a)` is the obvious sum of squares" | `a@a` 7× faster, and 0 MB vs 32 MB peak | the obvious version is not the fastest |

Notes that matter more than the table.

- **C1.** NumPy 2.x fast-paths an integer power of two to `np.square`, so `a**2`
  is not a general power at all. The folklore is a CPython-level fact — floats
  get no `square` special case there — misapplied to a library that does
  specialise. Reported ratio: `a*a` consistently *above* 1.0 across three
  independent repetitions, i.e. reproducibly slower, by about 9%.
- **C2.** With ratios of 1.017, 0.999 and 1.008, the sign of the difference
  flips between repetitions. `**0.5` is fast-pathed to `np.sqrt`, so both reach
  the same kernel. The claim cannot be tested into existence at this size.
- **C3.** The effect is reproducible (the ratio exceeded 1.0 in all three
  repetitions) but it is ~7%, not a factor. NumPy sums with pairwise
  accumulation and cache blocking, so the stride penalty is largely hidden.
  Textbook cache reasoning predicts a factor of two to eight here; **the model is
  wrong at this size, and only the measurement shows it.**
- **C4.** `np.vectorize` is a Python loop that builds an output array element by
  element. Its own documentation says so. The 353× factor is what "not
  vectorised" costs at a million elements. Use it for a scalar function on
  Python objects, never for arithmetic.
- **C5.** Ranked by measurement: `a @ a` (57 µs) < `np.sum(a*a)` (375 µs) <
  `np.einsum('i,i->',a,a)` (435 µs) at $10^6$ elements. The naive story "the
  winner avoids the temporary" explains only part of it: `einsum` also allocates
  nothing and is still slowest, because its generic kernel does not use the BLAS
  SIMD dot. Two distinct causes, separated only by measuring both time and
  memory.

### 6.3 The counter-intuitive result worth keeping

`a @ a` beats `np.sum(a * a)` by a factor 7 for a sum of squares. This is the
case where the "obvious optimisation" — writing the reduction you want — is not
the fastest, and where the correct instinct is to ask *what does the library
already have?* before writing anything. The dot product is the single most
optimised kernel in the numerical stack; a hand-written reduction will not beat
it, and a temporary will certainly not.

### 6.4 Small-array crossover, measured

A related claim that *is* true: "NumPy is always faster". It is false below a few
hundred elements, because `np.sum` has a fixed call overhead of about **0.68 µs**.

| $n$ | `sum(list)` ns | `np.sum(arr)` ns | winner |
|---|---|---|---|
| 8 | 57.6 | 641.6 | python |
| 64 | 162.3 | 673.2 | python |
| 256 | 507.2 | 722.3 | python |
| 384 | 783.5 | 716.3 | numpy |
| 1024 | 1905.8 | 761.9 | numpy |
| 65536 | 124 271 | 9481.8 | numpy |

The crossover sits near $n \approx 350$ for data that is *already* a Python list.
If you must convert with `.tolist()` first, the conversion cost dominates and
NumPy wins everywhere. Every serious numerical code base therefore carries a
size threshold somewhere near 100, and the threshold is only trustworthy because
someone measured it.

## 7. Python demonstration

Two files, both runnable offline under the project virtual environment:

```bash
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/profiling_demo.py
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/benchmark_folklore_demo.py
```

- `profiling_demo.py` — `cProfile` on both workloads, the overhead measurement,
  the `sys.settrace` line-hit table and the `tracemalloc` peaks. Runs in under a
  second.
- `benchmark_folklore_demo.py` — the paired A/B protocol and the five claims.
  Takes about 20 s because it repeats each experiment three times; the repetition
  is the point.

Expected output includes `stats.total_calls = 1024` for the NumPy-heavy workload
and `8001` for the Python-heavy one, `~76 ns per Python call`, and the peaks
`32.00 / 32.00 / 0.00 / 0.00 MB`.

### 7.1 What `line_profiler` and `memory_profiler` would add

Stated from their documentation; neither is installed here and nothing below was
executed.

- `line_profiler` gives a per-line time column via
  `kernprof -l -v script.py`, and requires the `@profile` decorator (it injects
  that name). Its time column has the same machine-dependence as any timing; its
  `Hits` column is the deterministic part.
- `memory_profiler` gives per-line *resident* memory via `@profile` and
  `python -m memory_profiler script.py`, and `mprof run`/`mprof plot` for a
  time series. It samples `/proc`-style process memory, so it measures what the
  allocator holds, including freed-but-retained blocks; `tracemalloc` measures
  what Python's allocator handed out. For NumPy arrays — which are single large
  allocations — both are adequate, and they occasionally disagree on small ones.

## 8. Assumptions and limits

- **Wall-clock numbers are not results.** Every ratio in Section 6 is a property
  of this machine and this load. The counts are not.
- **A micro-benchmark is not the program.** Optimising a 50 ns difference in an
  inner idiom does nothing if the program spends 90% of its time elsewhere; that
  is what step one of any optimisation must establish, with a profile.
- **`cProfile` cannot see C frames**, so a NumPy-only hot loop appears as one
  flat `tottime`. Interpret it as "this function", not "this line".
- **`tracemalloc` sees Python allocations.** Memory mapped by an extension
  outside Python's allocator may be invisible.
- **Peak memory and runtime are different objectives.** C5's winner is the same
  under both; that is luck, not law.
- **Virtualised and containerised environments change all of these numbers**,
  usually by making them worse and noisier.

## 9. Common mistakes

1. Timing an operation once, or without a warm-up, and reporting four
   significant figures.
2. Comparing A and B sequentially rather than interleaved, so CPU frequency
   drift is attributed to the change.
3. Optimising the code you *guessed* was slow without profiling it.
4. Believing that `cProfile`'s `tottime` for a NumPy-heavy function identifies
   the hot line.
5. Assuming NumPy is faster for small arrays.
6. Assuming `x*x` beats `x**2`, or `np.sqrt` beats `**0.5`, without measuring
   the NumPy version — both are fast-pathed, and the measured differences are
   within noise or in the opposite direction.
7. Testing performance with an assertion on elapsed seconds. Assertions on
   *counts* (`Hits`, `ncalls`, array sizes, allocations) are stable; assertions
   on durations fail on a busy runner.
8. Replacing a readable reduction with an expression whose speed says nothing
   about the program's actual bottleneck.

## 10. Real-world applications

- **Seismic processing pipelines.** A profile of a processing sequence usually
  shows the cost concentrated in one or two kernels (I/O, a filter, an
  interpolation), not spread evenly. Without the profile, the optimisation
  effort is distribution across the code proportional to readability rather than
  to cost.
- **Inversion loops.** A forward solver called $10^4$ times per iteration makes
  a 10% kernel improvement a 10% runtime improvement on a cluster job whose
  budget is measured in node-hours. That is a measurable financial decision, and
  it deserves a measurement.
- **Memory-bound field operations.** Processing a 3-D survey does not fit in
  RAM. Which step materialises a temporary array decides whether the job runs on
  a laptop or needs a cluster — a question `tracemalloc` answers in seconds.
- **Benchmarking for publication.** Any performance claim in a paper needs the
  method (repeat count, order statistic, machine) stated with the number, or it
  is not reproducible. The paired protocol of Section 6.1 is short enough to
  describe in a footnote.

## 11. Further reading

- **Python standard library.**
  [`profile` and `cProfile`](https://docs.python.org/3/library/profile.html),
  [`timeit`](https://docs.python.org/3/library/timeit.html),
  [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html),
  [`statistics`](https://docs.python.org/3/library/statistics.html),
  [`subprocess`](https://docs.python.org/3/library/subprocess.html) for the
  thread-count probes of the environments lesson. Level: reference.
- **NumPy.** [`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html)
  (pairwise summation) and
  [`numpy.einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html).
  Level: reference. The documentation states that `einsum` is generic; the
  measured consequence is in Section 6.2.
- **Gregg, B. (2020). *Systems Performance: Enterprise and the Cloud* (2nd ed.).
  Addison-Wesley.** Level: advanced. The methodology chapter — especially the
  "streetlight anti-method" and the value of counting — is the source of the
  protocol in Section 1.
- **Beyer, D., Löwe, S. & Wendler, P. (2019). Reliable benchmarking: requirements
  and state of the art. *Software Quality Journal*, 27, 1–29.** Level: advanced.
  The academic case for paired, repeated, order-statistic benchmarking.
- **Georges, A., Buytaert, D. & Eeckhout, L. (2007). Statistically rigorous Java
  performance evaluation. *OOPSLA*.** Level: advanced. The origin of the
  "repeat the whole experiment and report the range" practice.

> Note on citations: bibliographic details are given so you can locate the
> works. This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [03-13-02 Testing Numerical Code Against Analytic Solutions](./02-testing-scientific-code.md)
  — measurement protocol for accuracy, the analogue of this lesson's protocol
  for speed.
- [03-13-04 Code Quality](./04-code-quality.md) — static analysis, which finds
  different defects than either tests or profiles.
- [03-13-08 Reproducible Environments](./08-reproducible-environment.md) — why
  a benchmark result depends on the BLAS, the thread count and the machine.
- [03-02-07 Memory Layout, Views and Performance](../02-numpy/07-memory-performance.md)
  — strides and contiguity, the mechanism behind the C3 measurement.
- [03-02-08 Vectorisation Patterns](../02-numpy/08-vectorisation-patterns.md)
  — the idioms whose cost Section 6 measures.

## 13. Self-assessment checklist

- [ ] I can name the four rules of the measurement protocol without looking. (§1)
- [ ] I can read a `pstats` table and say which columns would change on another
      machine. (§2.1)
- [ ] I can explain why `np.sqrt` calls do not appear in a `cProfile` table. (§2)
- [ ] I can estimate the profiler's slow-down factor from a call count. (§3)
- [ ] I can obtain per-line execution counts with the standard library alone. (§4)
- [ ] I can measure a peak allocation and use it to falsify a hypothesis about
      where the time goes. (§5)
- [ ] I can report a benchmark as a median ratio plus a fraction-of-rounds-lost
      statistic, and say what would make me retract the conclusion. (§6.1)
- [ ] I can state at least one NumPy performance claim I used to repeat that
      measurement contradicted. (§6.2)
- [ ] I know the size threshold below which NumPy loses to a Python list, and
      why it exists. (§6.4)
