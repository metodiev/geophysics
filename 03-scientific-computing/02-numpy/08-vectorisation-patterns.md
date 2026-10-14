---
id: 03-02-08
title: "Replacing Loops: Vectorisation Patterns and Traps"
level: advanced
prereqs: ["03-02-03", "03-02-04"]
estimated_minutes: 75
tags: [numpy, vectorisation, performance, memory, einsum]
---

# Replacing Loops: Vectorisation Patterns and Traps

"Vectorise your loops" is the most repeated and least examined advice in
scientific computing. It is usually right, sometimes spectacularly right, and
occasionally wrong in a way that makes code both slower and harder to read. This
lesson separates the three cases by measurement.

The four patterns that actually constitute vectorisation are worth naming before
the measurements:

1. **Replacement of a scalar loop by a ufunc expression**, so that the loop runs
   in compiled code (lesson [04](./04-ufuncs-reductions.md)).
2. **Replacement of a nested loop by broadcasting**, so that the outer loop
   disappears into a shape (lesson [03](./03-broadcasting.md)).
3. **Preallocation instead of growth**, because appending to an array in a loop
   is quadratic in the number of copies.
4. **Blocking**, because a fully vectorised expression can allocate an
   intermediate larger than any cache — and then the vectorised form is the
   slower and less memory-safe one.

Only the fourth is genuinely subtle, and it is the one this lesson measures most
carefully, because it is where the advice inverts.

## Learning objectives

By the end of this lesson you will be able to:

1. **Replace** a triple loop over (observation, source) pairs with broadcasting
   and **measure** the speed-up, including the check that the results agree.
2. **Explain** the memory-bound trap in `(x * x).sum()` and **choose** a fused
   alternative, reporting the peak allocation rather than only the time.
3. **Explain** why `np.vectorize` is not vectorisation and **measure** its cost
   against the array expression it replaces.
4. **Replace** array growth in a loop with preallocation, and **state** the
   quadratic copy count that the growth incurs.
5. **Identify** the case where a full broadcast is dominated by a row-wise loop,
   and **say** what makes the difference (the size of the intermediate relative
   to cache).
6. **Report** every performance claim with an operation count, an element count,
   or a peak allocation, and never as a bare wall-clock ratio.
7. **Recognise** the patterns that have dedicated kernels — `bincount`,
   `einsum`, `reduceat`, `out=` — and reach for them before writing the
   generic form.

## Prerequisites

- [03 Broadcasting Rules and Vectorised Thinking](./03-broadcasting.md) — the shape
  rules that make nested loops disappear.
- [04 Universal Functions, Reductions and Axis Semantics](./04-ufuncs-reductions.md)
  — ufuncs and their reduction methods.
- [07 Memory Layout, Strides and Cache-Aware Performance](./07-memory-performance.md)
  — why the intermediate's size is the real constraint.

## 1. The forward model: triple loop against broadcasting

The demo computes the vertical gravity of 400 point masses at 400 stations — a
$400 \times 400$ interaction — twice: once with nested Python loops and once with
broadcasting. The physics is the standard point-mass kernel
$g_z = G m \Delta z / r^3$ with $\Delta z$ the depth difference; the sources and
their masses are SYNTHETIC and drawn from the seeded generator.

```
nobs = 400, nsrc = 400, pairs = 160000
triple loop (1 run)   :     87.75 ms
broadcast  (best of 3):      0.42 ms
speedup               :     216.0x   (machine dependent)
max |loop - vector|   : 3.253e-19 m/s^2 (3.253e-14 mGal)
largest signal        : -6.7971 mGal
agreement (rel 1e-10) : True
```

Four things must be true for this to be a legitimate optimisation, and all four
are checked:

- **The results agree.** The maximum difference is $3.25 \times 10^{-19}$ m s⁻¹,
  which is $3.25 \times 10^{-14}$ mGal against a largest signal of about 6.8 mGal
  — a relative difference of $5 \times 10^{-15}$, i.e. a few units in the last
  place. The two formulations perform the same arithmetic in a different order,
  so exact equality is not expected; agreement to machine precision is.
- **The work is the same.** Both forms perform $n_{\text{obs}} \times n_{\text{src}}
  = 160\,000$ distance evaluations and the same number of floating-point
  operations. The 216× ratio is entirely interpreter overhead removed, not work
  removed.
- **The memory cost is stated.** The broadcast form allocates four `(400, 400)`
  temporaries of 1.28 MB each — 5.12 MB — against a few scalars for the loop. The
  demo says so, because a 216× speed-up that silently costs 5 MB per call is a
  different engineering decision at `nobs = 20 000`.
- **The signal scale is printed.** `largest signal = -6.7971 mGal` is the reference
  against which the agreement tolerance is judged; an absolute tolerance without a
  scale is meaningless.

The vectorised form is the pattern to use, with one structural improvement that
the demo does not make and that a production code should: **loop over blocks of
observations and vectorise the source axis inside**, so that the temporaries are
$O(\text{block} \times n_{\text{src}})$ rather than $O(n_{\text{obs}} \times
n_{\text{src}})$. Lesson [07](./07-memory-performance.md) calls this blocking.

## 2. The memory-bound trap

The demo computes the sum of squares of a 20-million-element vector two ways:

```
n = 20000000, x.nbytes = 160.0 MB

(x * x).sum()  :     5.56 ms, peak traced memory    160.0 MB
np.dot(x, x)   :     1.87 ms, peak traced memory      0.0 MB

ratio ((x*x).sum() / dot) = 2.97x   (machine dependent)
values agree within 1e-10: True
np.float64(19999831.31196038)
np.float64(19999831.311960384)
```

**Here the vectorised expression is the slower one.** `(x * x).sum()` is a
composition of two vectorised operations: the multiply allocates a full 160 MB
temporary, writes it to memory, and then the reduction reads it back. The
operation touches 320 MB of traffic to produce one number. `np.dot(x, x)`
dispatches to BLAS, which accumulates on the fly with no intermediate at all —
peak traced allocation is reported as 0.0 MB.

Three lessons:

- **Peak allocation is part of the performance claim.** A 2.97× speed difference
  is modest; a 160 MB transient in a function called in a loop is fatal. Both
  numbers belong in the report.
- **"Vectorised" is not the same as "fused".** The multiply and the sum are two
  kernels with a materialised boundary between them.
- **The values differ in the last two digits**
  ($19999831.31196038$ against $19999831.311960384$), because BLAS sums in a
  different order than NumPy's pairwise reduction. This is expected and is why the
  demo checks agreement to a *relative tolerance* of $10^{-10}$ rather than exact
  equality. It is also the reason a summing order that matters must be pinned by
  the algorithm, not left to the library.

The general rule: whenever a vectorised expression contains a chain of
elementwise operations that is immediately reduced, look for a fused kernel —
`np.dot`, `np.einsum`, `np.add.reduce` with `out=`, or a single ufunc with the
`where=`/`out=` arguments.

## 3. `np.vectorize` is a loop in disguise

```
n = 1000000 elements
Python list comprehension :    102.63 ms
array expression a*a-2*a+1:      0.59 ms
np.vectorize(lambda ...)  :     63.63 ms
np.vectorize / array expr =    107.8x   (machine dependent)
list comp    / array expr =    173.9x   (machine dependent)
all three results equal   : True
```

`np.vectorize` exists for one purpose: to give a Python function the *broadcasting
interface* of a ufunc. It does not compile anything and does not run in parallel;
it calls the Python function once per element. Consequently:

- It cannot beat a list comprehension performed after, it is about 1.6× faster
  here only because the comprehension's list construction is itself expensive.
- It is **more than two orders of magnitude slower** than the ufunc expression
  that replaces it (107.8× in this run, 89× in the previous one — the ratio moves
  between runs, the order of magnitude does not).
- It is not a ufunc, so it has no `reduce`/`accumulate`/`outer` methods and the
  `out=` argument behaves differently.

The reproducible claim is the **call count**: $10^6$ Python calls for
`np.vectorize`, three compiled array passes for the ufunc expression. The
milliseconds are machine-dependent; the calls are not. Use `np.vectorize` only
when a function genuinely cannot be expressed with array operations — a
discontinuous or table-driven function, for instance — and never inside a hot
loop.

## 4. Growing an array in a loop

```
m = 20000 values
np.append in a loop :     46.21 ms
preallocated fill   :      0.68 ms
ratio = 68x   (machine dependent)
results identical: True

  np.append copies the whole array every call, so the loop does
  1 + 2 + ... + 20000 = 200010000 element copies, about
  200.0100e6, instead of 20000.
```

The count is the point. Growing an array of length $m$ one element at a time
performs $\sum_{k=1}^{m} k = m(m+1)/2$ element copies — $2 \times 10^8$ here for
$m = 20\,000$ — because each `np.append` allocates a new buffer of length $k+1$
and copies. The growth is quadratic and independent of the machine.

Two correct patterns:

```python
# preallocate when the final size is known
out = np.empty(m)
for i in range(m):
    out[i] = compute(i)

# collect then convert when the size is not known in advance
chunks = [compute(i) for i in range(m)]      # a list of arrays
out = np.concatenate(chunks)                 # one allocation
```

The second is the right default for streaming or variable-length input: a Python
list of arrays grows amortised-constant, and the single `np.concatenate` at the
end costs one copy. The pathological form is `np.append` *inside* the loop,
which is quadratic and allocates a fresh array every iteration.

## 5. When the broadcast loses

The most important measurement in the lesson. A $4000 \times 4000$ matrix of
pairwise distances is computed two ways: with a full broadcast producing the
whole matrix, and with a row-wise loop that allocates only one row at a time.

```
nobs = 4000, pairs = 16000000
full 4000x4000 broadcast : run 1  0.041 s, run 2  0.033 s, peak traced   384.0 MB
row-wise loop            : run 1  0.045 s, run 2  0.045 s, peak traced     0.2 MB
time ratios full/row     : 0.90x then 0.70x   (machine dependent, unstable)
means agree to 1e-12: True
the full matrix alone is 128.0 MB of intermediate
peak memory ratio = 2392x   (this is the robust result)
```

Read this honestly, because it is a good example of how a performance claim
should be stated.

**The time result is unstable.** The full broadcast was 0.90× and 0.70× the loop's
time in two consecutive runs — it was *faster* both times, by a margin that
changes by 25 per cent between runs. On a different machine or with a different
BLAS, either order can win. The honest claim is: "at this size the two forms are
within a factor of about 1.5 of each other in time, and the ordering is not
stable across runs."

**The memory result is robust.** 384.0 MB against 0.2 MB is a factor of 2392, and
it is a consequence of the algorithm, not of the machine: the broadcast must
materialise $n^2$ values, the loop need not. At $n = 40\,000$ the broadcast needs
12.8 GB and the loop still needs 0.2 MB; the broadcast fails on an ordinary
laptop while the loop completes in minutes.

**So the choice is made on memory, not on time.** The vectorised form is selected
when the intermediate fits comfortably; the loop — or, better, a blocked loop —
is selected when it does not. And at a large enough $n$ the right tool is neither
a full broadcast nor a plain loop but a spatial index (a KD-tree), which avoids
computing most of the pairs at all.

The two runs are reported in the demo precisely so that the reader can see the
instability. A single timing would have supported a false claim.

## 6. Patterns with dedicated kernels

Three patterns recur often enough that NumPy provides a kernel, and using the
generic form is both slower and less clear:

**Counting and weighted accumulation.** `np.bincount(x, weights=w, minlength=n)`
sums `w` into bins indexed by `x`. It is the correct tool for gridding scattered
data, for histograms and for binned statistics. The generic alternatives are
`np.add.at` (unbuffered scatter-accumulate, correct with duplicate indices) and
`np.zeros(n)[idx] += w`, which is **silently wrong** with duplicate indices
because the augmented assignment gathers into a temporary (lesson
[02](./02-indexing-slicing.md) §4). On this machine the two correct forms were
within a factor of about 2 of each other on a one-million-sample problem, so
prefer `bincount` for its clarity and its purpose-built kernel rather than for a
speed claim.

**Segment reductions.** `np.add.reduceat(a, indices)` reduces contiguous segments
delimited by `indices`. It is the fast path for "sum each trace", "mean each
window", "stack each gather", and it avoids both a Python loop and the
`np.add.at`-style scatter.

**Einstein summation.** `np.einsum("ij,jk->ik", A, B)` expresses contractions
whose shapes do not fit `@` or broadcasting: a weighted sum over a source axis,
a trace, a tensor contraction. It reads as the mathematics and compiles to a
blocked loop; use `optimize=True` for multi-operand contractions.

**In-place and masked ufuncs.** `np.multiply(a, b, out=c)` and
`np.add(a, b, out=c, where=mask)` fuse the operation into a preallocated
destination and avoid a temporary. This is the tool for the §2 problem in the
cases where no fused kernel exists.

## 7. Physical interpretation

Every geophysical forward operator is a sum over physical causes. A gravity
anomaly is a sum over buried masses; a travel time is a sum along a ray; a
seismic trace is a convolution over reflectivity; a magnetic field is a sum over
dipoles. In each case the *efficient* implementation follows the structure of the
sum:

- If the sum has a **separable kernel** — a function of a difference, as in
  convolution — use the fast transform for that structure (FFT), not a generic
  matrix product.
- If the sum is **over pairs with no structure**, the kernels are a dense matrix
  or a broadcast; the memory of that matrix is the physical cost, and blocking is
  the physical remedy.
- If only a **subset of pairs** matters — near-field interactions, neighbouring
  cells — use a tree, a neighbour list or a sparse operator, and the cost falls
  from $O(n^2)$ to $O(n \log n)$ or $O(n)$.

Vectorisation is a tool for implementing the second case efficiently. It is not a
substitute for recognising the first and third.

## 8. Assumptions and regime of validity

- **A speed-up assumes the operation count is unchanged.** Remove work before
  removing loops; a matrix multiply that fuses three passes is a different
  algorithm, and its speed-up is not a vectorisation result.
- **Timings are not reproducible across machines or runs.** Report element counts,
  operation counts and peak allocations; quote times with the machine and the
  NumPy version, and with the number of repetitions.
- **Peak allocation must be measured, not estimated.** `tracemalloc` (used in the
  demo) tracks Python-level and NumPy buffer allocations; `resource.getrusage`
  gives the process high-water mark; `/usr/bin/time -l` on macOS gives the maximum
  resident set. Each measures a different thing.
- **Broadcasting trades memory for time and can lose both.** §5 is the
  measurement. The decision boundary is the size of the intermediate relative to
  cache and RAM, not a general rule.
- **`np.vectorize` is not a performance tool** and never was; its `otypes`
  argument and its inability to reduce are the giveaway.
- **`out=` changes aliasing semantics.** `np.multiply(a, b, out=a)` overwrites
  `a`; if `a` is a view of something you need later, you have corrupted it. This
  is lesson [02](./02-indexing-slicing.md)'s warning in a new guise.
- **`np.einsum` without `optimize=True` may allocate large intermediates.** The
  path is chosen by the library; ask for the optimised one when the contraction
  has more than two operands.
- **Multithreading is not the same as vectorisation.** BLAS calls (including
  `np.dot` and `@`) may use several threads; elementwise NumPy operations are
  single-threaded. A "vectorisation" speed-up attributed to NumPy may in fact be
  multi-threading inside BLAS, which changes the scaling story on a cluster.
- **Loop removal can hurt readability.** A three-line loop with a physical comment
  is often better science than a 200-character broadcast chain that nobody can
  check. Vectorise the inner loop, keep the outer structure recognisable, and
  document the physical index meaning of each axis.

## 9. Python demonstration

The script is
[`code/vectorisation_demo.py`](./code/vectorisation_demo.py):

```
.venv/bin/python 03-scientific-computing/02-numpy/code/vectorisation_demo.py
```

All quantities are SYNTHETIC (seeded source positions, depths and masses; seeded
random vectors); no dataset is read. The script prints its seed and states that
timings are machine-dependent. The machine used for the numbers below is an Apple
M5 (arm64), 16 GB RAM, NumPy 2.5.4, CPython 3.14.

Key output:

```
nobs = 400, nsrc = 400, pairs = 160000
triple loop (1 run)   :     87.75 ms
broadcast  (best of 3):      0.41 ms
speedup               :     216.0x   (machine dependent)
max |loop - vector|   : 3.253e-19 m/s^2 (3.253e-14 mGal)
agreement (rel 1e-10) : True
```

```
(x * x).sum()  :     5.56 ms, peak traced memory    160.0 MB
np.dot(x, x)   :     1.87 ms, peak traced memory      0.0 MB
ratio ((x*x).sum() / dot) = 2.97x   (machine dependent)
```

```
np.vectorize(lambda ...)  :     63.63 ms
np.vectorize / array expr =     107.8x   (machine dependent)
```

```
np.append in a loop :     46.21 ms
preallocated fill   :      0.68 ms
ratio = 68x   (machine dependent)
```

```
full 4000x4000 broadcast : run 1  0.041 s, run 2  0.033 s, peak traced   384.0 MB
row-wise loop            : run 1  0.045 s, run 2  0.045 s, peak traced     0.2 MB
time ratios full/row     : 0.90x then 0.70x   (machine dependent, unstable)
peak memory ratio = 2392x   (this is the robust result)
```

### What to observe

1. The 216× speed-up comes with an agreement check at the $10^{-14}$ mGal level and
   a stated memory cost. All three belong together.
2. In §2 the "vectorised" form is the slower one (2.97×) and uses 160 MB. This is
   the trap the lesson exists for.
3. The `np.vectorize` ratio (107.8×) is a *call-count* result wearing a timing
   costume: $10^6$ Python calls against three compiled passes.
4. The `np.append` ratio (68×) is a *copy-count* result: $2.0 \times 10^8$ element
   copies against $2 \times 10^4$.
5. The two-run timing bracket in §5 is there so that the reader sees the
   instability that a single measurement would have hidden. When a timing is not
   stable, the memory claim is the one to keep.

## 10. Common mistakes

1. **Vectorising before removing work.** A fused multiply-add beats a broadcast,
   and an $O(n \log n)$ algorithm beats both.
2. **Chaining elementwise operations that are immediately reduced**, as in
   `(x * x).sum()`.
3. **Believing `np.vectorize`.** It is an interface adapter, not a compiler.
4. **Growing arrays with `np.append` in a loop.** Quadratic copies.
5. **Broadcasting to an intermediate that does not fit in cache** and then
   claiming the loop was the problem.
6. **Timing once and reporting the ratio.** Use best-of-several and report the
   bracket.
7. **Forgetting the correctness check** that must accompany the speed claim.
8. **Using `out=` on a view** and overwriting data needed later.
9. **Assuming NumPy is multithreaded.** Only the BLAS-backed operations are.
10. **Sacrificing readability for marginal speed.** Keep the physical meaning of
    the axes visible in the code.

## 11. Real-world applications

- **Potential-field forward modelling.** The (observation, source) kernel is
  either a dense matrix or a broadcast; the production pattern is a loop over
  observation blocks with the source axis vectorised, which is §1's structure with
  §5's memory discipline.
- **Seismic convolution.** Convolution is a separable sum, so the FFT is the
  correct vectorisation — a factor of $10^3$ over the direct loop for a
  1-second wavelet at 1 ms sampling.
- **Travel-time tomography.** The design matrix is sparse; the ray-tracing inner
  loop is vectorised over receivers while the ray path remains a sequential loop,
  which is the standard hybrid.
- **Gridding and binning.** Scattered gravity or magnetic measurements are binned
  onto a grid with `np.bincount`/`np.add.at`; the pattern is §6's, and the
  duplicate-index rule is the correctness crux.
- **Monte Carlo inversion.** $10^4$ model realisations are evaluated by
  broadcasting over the realisation axis, which is the case where a full
  intermediate is acceptable precisely because the per-realisation problem is
  small.
- **Machine learning geoprocessing.** Minibatch normalisation, loss reduction and
  augmentation are all §2-shaped: a chain of elementwise operations that should be
  fused, with the fused version being both faster and smaller.

## 12. Further reading

- **NumPy documentation, "Beyond the basics" and `numpy.vectorize`.**
  [https://numpy.org](https://numpy.org) — including the explicit warning that
  `np.vectorize` is provided for convenience, not performance. Level: beginner.
- **NumPy documentation, `numpy.einsum`, `numpy.bincount`, `numpy.add.at`,
  `numpy.ufunc.reduceat`.** [https://numpy.org](https://numpy.org) — the
  dedicated kernels of §6, with their exact semantics. Level: intermediate.
- **Harris, C. R., et al. "Array programming with NumPy." *Nature* 585, 357–362
  (2020).** DOI 10.1038/s41586-020-2649-2. Level: intermediate.
- **van der Walt, S., Colbert, S. C., & Varoquaux, G. "The NumPy array: a
  structure for efficient numerical computation." *Computing in Science &
  Engineering* 13(2), 22–30 (2011).** DOI 10.1109/MCSE.2011.37. Level:
  intermediate.
- **Klockner, A., et al. "PyCUDA and PyOpenCL: A scripting-based approach to GPU
  run-time code generation." *Parallel Computing* 38(3), 157–174 (2012).** The
  next step after vectorisation when the bandwidth-bound argument is taken to its
  conclusion. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [03 Broadcasting Rules and Vectorised Thinking](./03-broadcasting.md) — the shape
  rules behind §1 and §5.
- [04 Universal Functions, Reductions and Axis Semantics](./04-ufuncs-reductions.md)
  — the ufunc model behind §2 and §3.
- [07 Memory Layout, Strides and Cache-Aware Performance](./07-memory-performance.md)
  — why the intermediate's size decides §5.
- [02 Indexing, Slicing, Views vs Copies and Fancy Indexing](./02-indexing-slicing.md)
  — the duplicate-index rule behind §6.
- [19-numerical-modeling-hpc/…](../../19-numerical-modeling-hpc/README.md) —
  parallel and distributed versions of these patterns.
- [25-projects-capstone/…](../../25-projects-capstone/README.md) — where these
  patterns are applied end to end.

Exercises:
[`exercises/08-vectorisation-patterns-exercises.md`](./exercises/08-vectorisation-patterns-exercises.md)
and
[`exercises/08-vectorisation-patterns-solutions.md`](./exercises/08-vectorisation-patterns-solutions.md).

## Self-assessment checklist

- [ ] I can replace a nested loop over pairs with broadcasting and check that the
      results agree. (§1)
- [ ] I can name the intermediate that a vectorised expression allocates and
      measure its peak size. (§2)
- [ ] I can explain why `np.vectorize` cannot be fast, in terms of call counts.
      (§3)
- [ ] I can compute the number of element copies that growing an array incurs.
      (§4)
- [ ] I can design a measurement that separates the time effect from the memory
      effect, and say which one is robust. (§5)
- [ ] I can name one pattern with a dedicated kernel and say how to find the
      others. (§6)
- [ ] I can report a speed-up with an operation count, an element count and a
      peak allocation. (§8, §9)
- [ ] I can give an example of a geophysical operator whose structure suggests an
      FFT or a tree rather than a vectorised loop. (§7)
