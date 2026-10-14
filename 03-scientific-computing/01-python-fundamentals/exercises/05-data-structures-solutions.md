# Solutions — 03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity

> **Read this after attempting the exercises, not before.** Numbers attributed to
> the demo are its actual printed output.

---

## ★1 — Container choice

| Task | Container | Operation and cost |
|---|---|---|
| (a) elevation by station code, 10⁶ times | `dict` | O(1) average lookup |
| (b) stations in acquisition order | `list` | O(1) append, O(n) iteration |
| (c) test whether a code exists | `set` | O(1) average membership |
| (d) count per 0.1-magnitude bin | `dict` (from `Counter`) | O(1) average increment per event |
| (e) a composite key | `tuple` inside a `dict` | `tuple` is hashable; a `list` is not |

---

## ★2 — Complexities

**(a)** $O(n)$ per iteration of an outer loop, so $O(nm)$ for $m$ iterations —
quadratic if $m$ scales with $n$. Fix first: build `station_set` once, then the
test is $O(1)$ and the whole thing is $O(n + m)$.

**(b)** $O(n^2)$; the inner loop performs $n(n-1)/2$ comparisons. Fix first: a
single pass with a `set` or a `Counter`, which is $O(n)$.

**(c)** $O(n)$ and already optimal. Nothing to fix.

For a 10⁵-element input the difference between (b) and its linear replacement is
$5\times10^{9}$ comparisons versus $10^{5}$ hash probes — five orders of magnitude.
That is why (b) is the one to fix first: it is not a constant-factor problem.

---

## ★3 — One-sentence reasons

**(a)** A dictionary key must be hashable, and hashability requires that the key's
value cannot change — a `tuple` is immutable so its hash is stable, while a `list`
can be mutated after insertion, which would strand it in the wrong hash bucket.

**(b)** `sorted()` is $O(n \log n)$, which for $n = 10^{6}$ is about $2\times10^{7}$
comparisons — noticeable but linear-ish; called once per iteration of an $m$-step
loop it becomes $O(n m \log n)$, which for $m = n$ is worse than quadratic and is
the version that never finishes.

**(c)** A `set` is implemented as a hash table keyed by the elements themselves
with no associated values, so it has the dictionary's $O(1)$ membership and its
$O(n)$ memory, and the demo measures the two as indistinguishable (1.96 µs for both
over 200 membership tests).

---

## ★4 — The demo's measurements

**(a)**

```text
  list scan (O(n))   : 0.2470 s  =    12.35 us per lookup
  dict lookup (O(1)) : 0.0005 s  =     0.02 us per lookup
  speed-up           : 512x
```

**(b)**

```text
  list :   2248.58 us total  (True)
  set  :      1.96 us total  (True)
  dict :      1.96 us total  (True)
  list/set ratio: 1148x
```

**(c)**

```text
  comparisons (n*(n-1)/2): 4,498,500
  nested loops (O(n^2)):    65.005 ms   duplicate pairs: 2,944
  set + Counter (O(n)) :     0.321 ms   duplicate pairs: 2,944
  speed-up             : 202x
```

**(d)** `list 8.0 B/element`, `tuple 8.0 B/element`, `dict 52.4 B/element`,
`set 41.9 B/element`.

**Least representative measurement:** the per-lookup times themselves, because they
are absolute costs on one machine and one interpreter, and both spread by tens of
per cent between runs. The *ratios* and the *per-comparison* cost are the
transferable quantities, because the ratio of an $O(n)$ scan to an $O(1)$ lookup
grows linearly in $n$ while the measurement at fixed $n$ does not.

---

## ★5 — Excluding bad stations

**(a)**

```python
bad_list = [...]                      # 500 codes
kept = [row for row in rows if row.code not in bad_list]
```

Cost: one scan of up to 500 elements per record, $O(500 \times 300\,000) =
1.5\times10^{8}$ comparisons in the worst case (each record scans until it finds a
match or exhausts the list; for a record that is *not* bad, the full 500).

**(b)**

```python
bad_set = set(bad_list)               # once: 500 hashes
kept = [row for row in rows if row.code not in bad_set]
```

Cost: $O(500 + 300\,000)$ hash probes.

**(c)** Comparisons avoided: up to $1.5\times10^{8}$. At the demo's measured cost of
about 12 ns per comparison, that is a saving of roughly

$$1.5\times10^{8} \times 12\times10^{-9}\ \text{s} = 1.8\ \text{s},$$

whereas the set version's 300 000 probes at roughly 30 ns cost about 9 ms.
(If only 10 per cent of records are bad, the average scan is still long, because a
*non*-matching scan must examine the whole list — so the saving is close to the
upper bound.)

**(d)** With 20 records, the set version is *slower*: building the set costs 500
hashes, which the list version would never pay. The rule is stated in ★9: build the
index when you will use it more than a handful of times.

---

## ★6 — Scenario by scenario

| Scenario | Container | Reason |
|---|---|---|
| (a) presence check over 10⁵ codes | `set` | only membership is needed, and unordered is fine |
| (b) a 4-field record iterated 10⁷ times | `tuple` | smallest per-instance cost, immutable, unpackable |
| (c) a record needing validation on construction | `@dataclass` with `__post_init__` | validation must run at construction |
| (d) a 60-bin magnitude histogram | `list` of 60 ints, or `Counter` | a fixed small index is a list; a sparse/unknown key set is a `Counter` |
| (e) LIFO stack | `list` (or `collections.deque`) | `append`/`pop` from the end are O(1) |

---

## ★7 — Scaling the lookup

**(a)** An average successful lookup scans about $n/2 = 1\,000$ entries for
$n = 2\,000$. At 12.35 µs per lookup,

$$\text{per comparison} = \frac{12.35\ \mu\text{s}}{1\,000} = 12.35\ \text{ns}.$$

The assumption is that the target's position is uniform, so the expected
comparisons are $(n+1)/2 \approx n/2$; a *unsuccessful* lookup always scans all
$n$, which is twice as expensive.

**(b)** For $n = 10^{5}$ and $10^{5}$ lookups: $10^{5} \times 5\times10^{4}
= 5\times10^{9}$ comparisons at 12.35 ns each

$$= 5\times10^{9} \times 1.235\times10^{-8}\ \text{s} = 61.75\ \text{s},$$

about **62 seconds**. The dictionary version performs $10^{5}$ lookups at
$\approx 0.02$–0.03 µs plus a one-off build of $10^{5}$ entries at 31 ns:
$3.1\times10^{-3}$ s + $3\times10^{-3}$ s $\approx 6$ ms.

**(c)** Ratio at $n = 10^{5}$: $61.75/0.006 \approx 1\times10^{4}$ — about
**ten thousand times**. At $n = 2\,000$ the demo measured 512×. The ratio grew by a
factor of about 20 while $n$ grew by a factor of 50, which is consistent with the
scan cost being linear in $n$ and the dictionary cost being independent of it.

**(d)** Running at $n = 20\,000$ with 20 000 lookups gives a list time of roughly
$20\,000 \times 10\,000 \times 12$ ns $\approx 2.4$ s against a dictionary time of
about 5 ms — a ratio of about 500. Whether it grew exactly as predicted depends on
whether the per-comparison cost changed, and there are two reasons it might not
have:

1. **Memory locality.** A 20 000-element Python list spans more memory than a
   2 000-element one, so more of the scan misses cache; the per-comparison cost
   could therefore *rise*, inflating the ratio above the prediction.
2. **String interning and comparison cost.** Comparing station codes compares
   object identity first and then characters; if the codes share a long prefix, the
   per-comparison cost rises with the code length, not with $n$. Both effects are
   real and both mean the measurement should be reported as measured rather than
   as a constant.

---

## ★8 — Quadratic versus linear, extrapolated

**(a)** $4\,498\,500$ comparisons in 65.005 ms gives

$$\frac{4\,498\,500}{0.065005\ \text{s}} = 6.92\times10^{7}\ \text{comparisons
per second},$$

i.e. about 14.5 ns per comparison.

**(b)** Comparisons scale as $n^2/2$:

| $n$ | Comparisons | Predicted time |
|---|---|---|
| $10^{5}$ | $5.0\times10^{9}$ | $\approx 72$ s |
| $10^{6}$ | $5.0\times10^{11}$ | $\approx 7\,200$ s $\approx 2$ hours |

(The demo itself prints the $10^{5}$ figure as "roughly 72 s", from
$65.005\ \text{ms} \times 1111$.)

**(c)** The `Counter` version is $O(n)$ in the number of events plus $O(d\log d)$ to
sort $d$ distinct keys, and the demo's $n = 3\,000$ run costs 0.321 ms. Scaling
linearly: $n = 10^{5}$ gives about $0.321 \times 33.3 = 10.7$ ms, and $n = 10^{6}$
about 107 ms. **Assumption:** the per-event cost is constant, which holds while the
table fits in cache; beyond that the constant rises modestly, and even a factor of
three leaves both well under a second.

**(d)** The nested loop exceeds one hour (3 600 s) when
$n^2/2 \times 14.5\times10^{-9} > 3600$, i.e.
$n > \sqrt{2 \times 3600/14.5\times10^{-9}} = \sqrt{4.97\times10^{11}}
= 7.0\times10^{5}$.

For one day (86 400 s) the factor of 24 multiplies $n$ by $\sqrt{24} = 4.9$:
$n \approx 3.4\times10^{6}$.

So a quadratic duplicate check is unusable above roughly $10^{6}$ events — the size
of a modest regional catalogue over a few decades.

**(e)** The comment:

```python
# One pass with Counter is O(n); the nested-loop version is O(n^2) and does not
# finish on a national catalogue.  See lesson 03-01-05.
```

---

## ★9 — The crossover

**(a)** Let $c_s = 12.35$ ns per comparison, $c_d = 31$ ns per dictionary entry
built, and $c_h \approx 30$ ns per dictionary lookup. Then for $k$ successful
lookups into an $n$-element collection:

$$t_{\text{list}}(n, k) = k \cdot \frac{n}{2} c_s, \qquad
t_{\text{dict}}(n, k) = n\,c_d + k\,c_h.$$

**(b)** Setting them equal:

$$k\frac{n}{2}c_s = n\,c_d + k\,c_h
\;\Longrightarrow\;
k\left(\frac{n}{2}c_s - c_h\right) = n\,c_d
\;\Longrightarrow\;
k = \frac{n\,c_d}{\frac{n}{2}c_s - c_h}.$$

For $n = 2\,000$: numerator $= 2\,000 \times 31 = 6.2\times10^{4}$; denominator
$= 1\,000 \times 12.35 - 30 = 1.232\times10^{4}$. So
$k = 6.2\times10^{4}/1.232\times10^{4} = 5.0$: about **5 lookups**.

**(c)** Measured on the same machine, with the dictionary rebuilt inside the timed
region and 200 repetitions per point:

| $k$ | list scan (µs) | dict build + lookups (µs) | faster |
|---|---|---|---|
| 1 | 9.4 | 45.5 | list |
| 2 | 50.1 | 44.3 | dict |
| 5 | 215.5 | 44.5 | dict |
| 10 | 328.6 | 46.5 | dict |
| 20 | 865.9 | 52.3 | dict |

The measured crossover lies between $k = 1$ and $k = 2$ — earlier than the model's
$k = 5$, because the model's $\frac{n}{2}$ average is pessimistic for the particular
keys used (the first probe happened to land near the front of the list) and because
the per-comparison cost in this measurement is lower than the demo's. Report your
own measured crossover; the *order of magnitude* — a handful of lookups — is the
transferable result.

**(d)** The answer is almost independent of $n$ because both sides scale linearly
in $n$ once $k \gtrsim 2$: the list's cost is $k\frac{n}{2}c_s$ and the dictionary's
build cost is $n c_d$, so $n$ cancels out of the comparison and only the *number of
lookups* decides. That is the practical rule: **if you will look anything up more
than once, build the index first.** The exception is a single lookup, where the
list is cheaper because the build cost is paid in full and never amortised.
