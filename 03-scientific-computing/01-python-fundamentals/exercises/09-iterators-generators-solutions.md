# Solutions — 03-01-09 Iterators, Generators and Lazy Evaluation for Large Data

> **Read this after attempting the exercises, not before.** Numbers attributed to
> the demo are its actual printed output.

---

## ★1 — The protocol

`iter(obj)` returns an *iterator*: an object with a `__next__` method that
represents a position in `obj`. `next(it)` returns the value at that position and
advances it, or raises `StopIteration` when the positions are exhausted. A `for`
loop calls `iter()` once, calls `next()` repeatedly, and swallows the final
`StopIteration` — everything else in this lesson is a way of writing `__next__`
with less code.

---

## ★2 — When work happens

| Statement | File opened? | Lines read? |
|---|---|---|
| (a) `g = gen(p)` | **No** | **No** — calling a generator function creates the generator object without running the body |
| (b) `first = next(g)` | Yes | One — the body runs up to the first `yield` |
| (c) `rest = list(g)` | Already open | **All the rest** — the handle stays open (and the generator holds it) while `list` consumes it |
| (d) `sum(1 for _ in g)` | No | **Zero** — `g` is exhausted, so the loop body never runs and the sum is 0 |

(d) is the silent-single-use trap: an exhausted generator yields nothing, so a
second pass returns a *plausible* answer (0, or an empty list) with no error.

---

## ★3 — Lazy rewrites

**(a)** `rows = (line.split(",") for line in handle)` — a generator expression
instead of a list comprehension. Memory changes from "one list plus one list of
fields per line, all live at once" to "one line and one field list live at a time".

**(b)** `total = sum(float(x) for x in values)` — the inner list comprehension
becomes a generator expression. Memory changes from an $n$-element list of floats
to a constant; the *result* is identical (and, for a long sequence,
`sum` over a generator is the same summation order, so the last bits agree too).

**(c)** `ok = (r for r in records if r.magnitude >= 2.0)` — but read the caveat:
if `ok` is later iterated twice, the second pass is empty. The lazy version is only
correct if the consumer iterates once; otherwise the eager list is what you want.
**Name which you chose, in a comment.**

---

## ★4 — The demo's measurements

**(a)** `catalogue: synthetic_big_catalogue.csv, 7.7 MB, 200,000 rows`.

**(b)** `selected   : 50,561 events in 0.07 s`, `mean depth : 30.523 km`. The
selection is 25.3 per cent of the rows, consistent with a uniform magnitude
distribution over $[-1, 3]$ and a cut at 2.0.

**(c)** `eager  : peak    48.87 MB` and `lazy   : peak     0.15 MB`, a ratio of
`325x less memory`.

**(d)** `absolute difference in the mean: 3.45e-13 km  (1.1e-14 relative)`, and
`agrees to 1e-12 relative: True`.

**(e)**

```text
  first record        : ('SYN000000', 31.851, -117.0562, 46.32, 2.23)
  remaining records   : 199,999
  sum(1 for _ in gen) again -> 0  (exhausted)
```

The first record plus 199 999 remaining is 200 000, and the second count is 0.

---

## ★5 — `islice` on an infinite generator

```python
import itertools
import random

def walks(step=1.0, seed=20261014):
    """Yield positions of a SYNTHETIC one-dimensional random walk."""
    rng = random.Random(seed)
    position = 0.0
    while True:
        yield position
        position += rng.choice((-step, step))
```

**(a)–(b)** `list(itertools.islice(walks(), 20))` prints 20 numbers starting at
0.0, each one a step of ±1.0 from the previous. `islice` is the correct way to take
a prefix because it stops *pulling* after 20 items; the generator is never asked
for the 21st.

**(c)**

```python
maximum = max(abs(x) for x in itertools.islice(walks(), 100_000))
```

Constant memory, one pass.

**(d)** `list(walks())` never returns: `list` requests items until `StopIteration`,
and an infinite generator never raises it, so the process allocates until it is
killed. `islice` changes exactly that — it introduces a *finite* consumption
boundary — and it is the idiom to reach for whenever a generator's length is
unknown or unbounded.

---

## ★6 — A 10⁸-row file

**(a)** $10^{8} \times 38.5$ bytes $= 3.85\times10^{9}$ bytes $= 3.85$ GB
(using 1 GB $= 10^{9}$ bytes).

**(b)** Scaling the demo's calibration linearly in $n$
($48.87\ \text{MB} / 2\times10^{5} = 2.44\times10^{-4}$ MB per row):

$$10^{8} \times 2.44\times10^{-4}\ \text{MB} = 2.44\times10^{4}\ \text{MB}
= 24.4\ \text{GB}.$$

Add the *list* of 10⁸ pointers itself (800 MB) and the interpreter, so a 32 GB
machine is the practical minimum, and it will swap.

**(c)** The generator pipeline stays at approximately 0.15 MB — the demo's lazy
figure — plus the running totals, independent of $n$.

**(d)** The eager version needs a 32 GB machine (and would still be fragile);
the lazy version runs on anything, including a laptop with 1 GB free. The one
change is to replace `list(...)` with a `for` loop over the generator, or to move
the reduction *into* the consumption expression: `sum(depth for depth in pipeline(...))`.

---

## ★★7 — One pass instead of two

**(a)** The second pass is required because the selection criterion — "more than
two standard deviations from the mean" — is not known until the whole first pass has
completed. The selection depends on a statistic of the data, so the data must be
seen once to *compute* the criterion and once to *apply* it.

**(b)** The sums needed are $n$, $\sum x$ and $\sum x^2$; the mean is
$\sum x/n$ and the sample variance is
$(\sum x^2 - (\sum x)^2/n)/(n-1)$. A single pass accumulates these three counters.
What is *missing* is the selection itself, because the threshold is only known at
the end — so the selection needs either a second pass or a buffer.

**(c)** Two designs:

| Design | Buffers | Memory cost | Wall clock |
|---|---|---|---|
| Buffer only the selected rows in a second list, then re-filter | the candidate rows (those outside a provisional band) | proportional to the *candidate* count, which is a small fraction of $n$ for a two-sigma band (typically a few per cent even with a provisional threshold) | one pass |
| Re-open the file and apply the now-known threshold | nothing | constant | two passes (roughly double the I/O) |

A third design — buffer a *sample* of the file, compute the threshold on the
sample, then filter in a single pass — is the standard streaming approximation and
is worth mentioning: it trades exactness for one pass, and its error is quantifiable
from the sample size.

**(d)** For a 10 GB file, the buffered-candidates design is the right default: the
file is read once (the expensive part), and the memory cost is proportional to the
number of rows that survive the provisional band, which for a two-sigma selection
on a smooth distribution is a few per cent of the rows — hundreds of MB at most, and
in the worst case (a heavy-tailed anomaly distribution) perhaps 10 per cent, which
is still 1 GB rather than 10 GB. If even that is too much, the two-pass version
costs only I/O and no memory, and on a machine with a fast disk it is often the
better engineering choice. **State the numbers for your file before choosing.**

---

## ★★8 — Proving a lazy rewrite equivalent

**(a) and (b)** For the first 1 000 parsed rows, compute:

```python
from fractions import Fraction
import itertools

first_1000 = list(itertools.islice(pipeline(path, 0.0), 1000))
exact = sum(Fraction(repr(depth)) for depth in first_1000) / 1000
eager = float(sum(first_1000)) / 1000
lazy = float(sum(d for d in itertools.islice(pipeline(path, 0.0), 1000))) / 1000
```

With `Fraction(repr(x))` the exact value is recoverable from the double *without*
introducing a new error, which is the point: `repr` round-trips, so the rational
arithmetic is exact on the same inputs the float code saw.

**(c)** Report the differences in units in the last place:

$$\frac{|\text{float} - \text{exact}|}{\mathrm{ulp}(\text{float})}.$$

A correct implementation gives a few ulps; anything more is a bug rather than
rounding, because the exact value is available for comparison. This is the standard
way to make "is my summation good?" a *decidable* question instead of a judgement.

**(d)** The demo's two sums differ by $3.45\times10^{-13}$ km, a relative difference
of $1.1\times10^{-14}$ — about one ulp of the total. The reason is that
floating-point addition is not associative: the eager version sums the depths in
file order after a separate selection pass, the lazy one sums them in the order the
pipeline emits them, and each ordering produces a different sequence of roundings,
each of which is individually correct to half an ulp.

**(e)** The rule: **compare a refactored pipeline against the original with a
*relative* tolerance chosen from the expected rounding, not with `==`.** About
$10^{-12}$–$10^{-11}$ relative is right for a few thousand additions of a sum of
magnitude near 30 (which is $10^{-14}$ relative plus margin). If you need bit-for-bit
reproducibility, you must fix the summation order, and that order becomes part of
the method description.

---

## ★★9 — Memory scaling

**(a)** Linear model from the demo:
$48.87\ \text{MB} / 2\times10^{5} = 2.44\times10^{-4}$ MB per row, so
$M_{\text{eager}}(n) \approx 2.44\times10^{-4}\,n$ MB (plus the 800 MB list of
pointers at $n = 10^{8}$).

**(b)**

| $n$ | Eager peak | Lazy peak |
|---|---|---|
| $10^{6}$ | ≈ 244 MB | ≈ 0.15 MB |
| $10^{7}$ | ≈ 2.4 GB | ≈ 0.15 MB |
| $10^{8}$ | ≈ 24 GB (+0.8 GB pointers) | ≈ 0.15 MB |

**(c)** The lazy peak does not scale because the pipeline holds only one record at
a time plus the running aggregates; the memory is proportional to the *number of
live accumulators*, not to the number of records. Two quantities that *do* grow even
in a streaming design are: (i) any collection of distinct keys the reduction must
remember — a set of distinct place names, a set of calendar days, a set of station
codes — which grows with the *cardinality* of the data rather than its length; and
(ii) any histogram or buffer whose size is fixed by the *output* resolution, which
is constant but can be large (a 10⁵-bin histogram is 0.8 MB, and that is fine).
The distinction to state: **memory proportional to cardinality is acceptable;
memory proportional to length is not.**

**(d)** The design rule:

| Reduction | Materialises? |
|---|---|
| count, sum, mean, variance, min, max, histogram, existence test | **no** |
| median, quantiles, "sorted by", "top-k" (for large k), join, dedupe by an arbitrary key | **yes**, in general |

Quantiles and medians are the interesting case: they require either the whole set
or a reservoir/histogram approximation, and the exact answer for a stream costs
memory proportional to $n$. Recognising that *before* writing the pipeline is the
practical skill: a "one pass" median is a claim that should always be examined.
