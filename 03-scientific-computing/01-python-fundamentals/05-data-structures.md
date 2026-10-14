---
id: 03-01-05
title: "Lists, Tuples, Dictionaries, Sets and Complexity"
level: beginner
prereqs: ["03-01-04"]
estimated_minutes: 75
tags: [data-structures, complexity, dictionaries, performance, survey]
---

# Lists, Tuples, Dictionaries, Sets and Complexity

There is a moment in every processing script when the data structure stops being
a detail and becomes the result. It is the moment a 2,000-station lookup is
written as a scan over a list instead of a dictionary, or a duplicate check is
written as a nested loop instead of a set. Both programs are *correct*. One of
them scales; the other does not, and no amount of careful coding rescues it.

This is the module's **mastery lesson**. It is short on syntax and long on
measurement, because the skill being taught is a diagnostic one: given a task,
name the container and its cost before writing the loop.

## Learning objectives

By the end of this lesson you will be able to:

1. **Choose** between a list, a tuple, a dictionary and a set for a task, on the
   grounds of the operations required and their asymptotic cost.
2. **Measure** the difference between an O(n) list scan and an O(1) dictionary
   lookup on a realistic survey bookkeeping problem, and quote the result.
3. **Recognise** an O(n²) algorithm, and state what happens to it when the data
   set grows by a factor of thirty.
4. **Use** `Counter`, `defaultdict` and `namedtuple` for counting, grouping and
   records, and say what each replaces.
5. **Explain** why a dictionary and a set trade memory for speed, using measured
   byte counts per element.
6. **Estimate** the running time of a script at a larger *n* from a measurement
   at a smaller one, and say which term will dominate.

## Prerequisites

- [03-01-04 Functions, Scope, Modules and Packages](./04-functions-modules.md) —
  the functions that operate on these containers.

## 1. The four containers, by operation

| Container | Ordered | Mutable | Duplicates | Lookup by key | Typical use |
|---|---|---|---|---|---|
| `list` | yes | yes | allowed | O(n) scan | A station profile in acquisition order |
| `tuple` | yes | no | allowed | O(n) scan | A fixed record; a dict key |
| `dict` | insertion order | yes | unique keys | O(1) average | Station name → elevation |
| `set` | no | yes | unique | O(1) average membership | Duplicate detection, membership tests |

The `dict` and `set` rows are the whole lesson. Both are hash tables, both give
amortised O(1) lookup, and both are the difference between a script that finishes
and one that does not. The `list` row is not a defect — a list is exactly right
for a profile you iterate in order, and its memory layout (eight bytes per element,
a pointer) is the compact one. The mistake is using a list for *lookup*.

Two properties of `dict` are worth stating because they are commonly misremembered:
since Python 3.7, insertion order is a language guarantee, not an implementation
detail, so a dict is a perfectly good ordered record; and dict keys must be
hashable, which is why a tuple can be a key and a list cannot.

## 2. Worked walkthrough: O(n) lookup versus O(1)

The demo builds a synthetic survey of 2,000 stations with seeded random
elevations, then performs 20,000 lookups two ways: by scanning the parallel lists,
and by looking up a dictionary built once from them.

```text
  stations           : 2,000
  lookups            : 20,000
  list scan (O(n))   : 0.2470 s  =    12.35 us per lookup
  dict lookup (O(1)) : 0.0005 s  =     0.02 us per lookup
  speed-up           : 512x
  identical totals   : True
```

Three readings of that table, in increasing order of importance.

**The factor is about 500, and it is not the point.** A factor of 500 is what
happens at *this* n. The list scan touches about n/2 = 1,000 entries per lookup
on average; the dictionary touches one hash bucket. The factor scales as n, so at
n = 10⁵ with 10⁵ lookups the comparison count is 5 × 10⁹ and the pure-Python list
version stops being a slow script and becomes a wall-clock problem measured in
hours, while the dictionary version is still milliseconds.

**The results are identical.** `identical totals: True` — the two implementations
agree exactly, not approximately. This is the general shape of a complexity bug:
correct output, wrong scale. There is no test that fails, so the bug is only
visible if you know what n will be.

**The measurement is machine- and run-dependent.** Repeated runs of the demo give
per-lookup times spread over tens of per cent; the *ratio* is stable because both
sides are measured on the same machine in the same process. When you benchmark,
report ratios of measurements taken together, not absolute times taken
separately.

The fix is one line and it is worth internalising as a pattern:

```python
lookup = dict(zip(names, elevations))     # build once: O(n)
total = 0.0
for name in wanted:
    total += lookup[name]                 # use many times: O(1) each
```

Build the index once, use it many times. That is the *entire* content of most
performance work in scientific scripting.

## 3. Worked walkthrough: membership tests

The same argument applies to `in`:

```text
  200 membership tests for the LAST station in the list
  list :   2248.58 us total  (True)
  set  :      1.96 us total  (True)
  dict :      1.96 us total  (True)
  list/set ratio: 1148x
```

The probe is the *last* station in the list, which is the list's worst case: 2,000
comparisons per test. The set and the dictionary both hit a hash bucket, and the
measured per-test cost is about 10 ns for both — indistinguishable, because a set
*is* a dictionary without values.

The pattern to watch for is any loop whose body contains `in` on a collection that
was not built as a set:

```python
# O(n * m), and m grows with the survey
for station in new_survey:
    if station in old_survey_list:      # scan!
        pass      # body omitted: the question is about the membership test
```

The fix is `old_survey_set = set(old_survey_list)` once, outside the loop, which
turns the whole thing into O(n + m).

## 4. Worked walkthrough: the quadratic algorithm

The sharpest illustration is duplicate detection, because there the quadratic
version is the one most people write first:

```text
  catalogue size: 3,000 station codes,
  drawn from only 1,500 distinct codes, ...
  comparisons (n*(n-1)/2): 4,498,500
  nested loops (O(n^2)):    65.005 ms   duplicate pairs: 2,944
  set + Counter (O(n)) :     0.321 ms   duplicate pairs: 2,944
  identical answers    : True
  speed-up             : 202x
```

Both versions do exactly the same job — count every pair of events that share a
station code — and both return 2,944. The difference is that one performs
4,498,500 comparisons and the other performs 3,000 hash probes followed by a sum
over the counts.

Now the crucial part, which is not the 202× at n = 3,000 but the projection:

```text
  Raising n to 10^5 multiplies the pair count by about 1111, so the
  measured 65 ms becomes roughly 72 s - and the set version
  still finishes in milliseconds.
```

The pair count grows as n²/2, so scaling n from 3,000 to 100,000 multiplies the
work by $(100000/3000)^2 = 1111$. A 65 ms operation becomes 72 s. This is the
arithmetic you should be able to do in your head before writing the loop, and it is
why **O(n²) is a scaling error and not a slowdown**. There is no tuning, no
`numba`, no compiled extension that makes a quadratic algorithm competitive with a
linear one at n = 10⁵; there is only replacing the algorithm.

One subtlety the demo adds deliberately: a *set alone* answers "is there a
repeat?" but not "how many pairs?". The linear version counts occurrences with
`Counter` in one pass and then combines the counts — a two-step pattern that is
worth recognising, because the naive reaction ("just use a set") would have
produced a different answer, not a faster one.

## 5. Physical interpretation: why the container is a scientific decision

It is tempting to file this lesson under "computer science" and move on. That
would be a mistake, because in geophysics the container choice interacts with the
*measurement design*.

**A survey is a set of stations with a natural key.** Station codes are unique by
construction, which makes the station table a dictionary keyed by code. The moment
the field sheet is digitised, the natural data structure exists, and scanning a
list to find a station is an import failure waiting to be discovered by the
person who has to re-run the survey in five years.

**A catalogue is a multiset of events.** Events repeat: aftershocks, duplicate
reports, re-analyses under a new ID. Counting is the first operation anybody
performs on a catalogue, and `Counter` is the tool. A quadratic duplicate check on
a 10⁵-event catalogue is not a slow script; it is a script that never finishes
before the reviewer's deadline.

**Order matters for profiles and does not for membership.** A gravity profile is
an ordered sequence of stations along a line; a list is right. A set of station
codes that must be *excluded* is unordered; a set is right. Choosing a set for the
profile destroys the ordering that the physics of the profile depends on, and
choosing a list for the exclusions makes the loop quadratic. The two containers in
the same function serve different physics.

**Memory is part of the budget.** A 10⁸-sample seismic record as a Python list of
floats carries 8 bytes per pointer plus a boxed float object each — the demo's
measured 8 B/element for the list is the *pointer*, and the objects are elsewhere.
A dictionary of 10⁵ entries costs about 52 bytes per entry in the same
measurement:

```text
  list   of float :      800,056 bytes  (8.0 B/element)
  tuple  of float :      800,048 bytes  (8.0 B/element)
  dict   int->float:   5,242,960 bytes  (52.4 B/element)
  set    of int   :    4,194,520 bytes  (41.9 B/element)
```

That is the trade, stated in bytes: about 6× the memory for O(1) lookup. Module
[03-02 NumPy](../02-numpy/README.md) then shows the third option — a contiguous
array of doubles at 8 bytes per element *including the data*, which is both
compact and fast, and which is why NumPy exists.

## 6. Records: tuple, namedtuple and the record class

```text
  plain tuples      : [('STA01', 112.4, 0.31), ('STA02', 118.9, 0.27), ('STA03', 121.7, 0.29)]
  namedtuple        : Station(code='STA01', elevation=112.4, anomaly=0.31)
  attribute access  : records[0].anomaly = 0.31
  sorted by anomaly : ['STA01', 'STA03', 'STA02']
```

A tuple is immutable and hashable, so it can be a dictionary key or a set member;
a list cannot. A `namedtuple` keeps those properties and adds field names at
essentially no cost. A dataclass (lesson [08](./08-classes-and-oop.md)) adds
defaults, validation and methods, and costs a little more.

The practical rule: **use a plain tuple inside a tight loop over numeric
columns; use a namedtuple when the fields have distinct meanings; use a dataclass
when they need validation.** The transition from `row[1]` to `row.elevation` is
not cosmetic — it is the difference between code that survives a column reorder
and code that silently swaps latitude for longitude.

Sorting by a key is worth one line of attention:

```python
ordered = sorted(records, key=lambda r: -r.anomaly)
```

`sorted` is stable and O(n log n). Sorting a 10⁶-event catalogue is about 20 ×
10⁶ comparisons — noticeable but never the bottleneck. Sorting *inside* a loop is
the bottleneck, and it is a common accident in group-by code.

## 7. Grouping with `defaultdict`

```text
  defaultdict(list): {'L1': [110.0, 240.0, 5.0], 'L2': [95.0, 260.0, 12.0]}
  running sums     : {'L1': 355.0, 'L2': 367.0}
  mean per line    : {'L1': 118.33, 'L2': 122.33}
```

`defaultdict(list)` replaces

```python
if line not in grouped:
    grouped[line] = []
grouped[line].append(h)
```

with one line, and removes a branch that is easy to get wrong (forgetting to
initialise one of the two accumulators). The complexity is unchanged — grouping is
O(n) either way — so this is a readability win, not a performance one, and saying
so is part of the lesson.

This is the manual form of a group-by. Module
[03-04 pandas](../04-pandas/README.md) does the same thing with
`df.groupby("line")["height"].mean()`, which is shorter and substantially faster
because the loop runs in compiled code. Understanding the manual version is what
makes the one-liner auditable: you know what it must be doing, and you can predict
its memory cost.

## 8. Assumptions and limits

1. **O(1) is amortised and average-case.** Hash tables degrade to O(n) per
   operation on adversarial key collisions, and a resize is O(n) occasionally.
   For the string and integer keys used here, average-case behaviour is what you
   will observe.
2. **The measured ratios are from one machine and one interpreter.** The 512× and
   202× figures will move. The *scaling* — the ratio grows linearly with n for the
   list scan, and as n for the quadratic pair count — is the durable content.
3. **`sys.getsizeof` is shallow.** It reports the container, not the objects
   inside it. The 8 B/element for a list of floats is the pointer array; the
   floats themselves live elsewhere. Read the table as a comparison, not as an
   accounting of a process's RSS.
4. **Small n is not worth optimising.** Below a few hundred elements, a list scan
   is faster than building a dictionary, because the dictionary costs a hash of
   every key up front. The crossover is the thing to reason about, not a rule.
5. **Sets are unordered.** Iterating a set gives an arbitrary order that can
   differ between runs and versions. Never rely on it, and never produce a
   reproducible result by iterating a set of floats.
6. **Hashability requires immutability.** The reason a list cannot be a key is
   that mutating it would break the hash. This is a design constraint, not a
   convention.

## 9. Python demonstration

```bash
cd 03-scientific-computing/01-python-fundamentals/code
python3 data_structures_demo.py
```

Run it twice and note the variation in the absolute times against the stability of
the ratios. Then change `N_DUPLICATES` from 3,000 to 6,000 and predict the runtime
of the nested loop before running it: the comparison count should quadruple, from
4.5 × 10⁶ to 18 × 10⁶. If the measured time quadruples, you have confirmed the
quadratic scaling experimentally — which is the point of the exercise.

## 10. Common mistakes

1. **A list where the task is lookup.** The 512× measurement above, and it gets
   worse as n grows.
2. **`if x in big_list` inside a loop.** O(n) inside O(m) is O(nm). Build a set.
3. **A nested loop over the same collection.** Quadratic by construction; ask
   whether a hash table, a sort, or a single pass can replace it.
4. **Using a set where order matters.** The set is correct for membership and
   wrong for a profile.
5. **Using a list as a dict key.** Not hashable; the error message is clear, which
   is a mercy.
6. **Relying on set iteration order.** It is arbitrary; a result that depends on
   it is not reproducible.
7. **Assuming `sys.getsizeof` measures memory.** It measures the object, not the
   graph.
8. **Optimising below the crossover.** Building a 20-entry dictionary to replace a
   20-element list is slower and less readable.
9. **Sorting inside a loop.** O(n² log n) hiding inside an innocent-looking line.
10. **Confusing a column layout with a record layout.** Parallel lists
    (names, elevations, anomalies) are efficient for arithmetic and dangerous for
    edits, because every operation must be applied to every list in the same
    order. NumPy has the same property and the same hazard.

## 11. Real-world applications

- **Survey databases.** Stations are keyed by code; the first operation on a
  legacy field sheet is to build that key and detect duplicates, which is exactly
  §4's problem.
- **Earthquake catalogues.** Counting events per hour, per region or per magnitude
  bin is `Counter` and `defaultdict` work; the alternative is a nested loop that
  does not finish.
- **Cross-matching catalogues.** Finding events present in two bulletins is a
  *join*, which is a set or dictionary operation. A nested-loop join on two
  10⁵-event catalogues is 10¹⁰ comparisons.
- **Waveform indexing.** A continuous archive is indexed by channel and time
  window; the index is a dictionary or a database, and linear scanning it is the
  reason a data centre's old tooling felt slow.
- **Gridded data.** A 3,600 × 1,800 global grid is a 2-D array, not a list of
  lists; module [03-08](../08-gridded-geospatial-data/README.md) develops that
  shape properly.

## 12. Further reading

- NumPy — [numpy.org](https://numpy.org): contiguous arrays and the memory model
  that replaces the containers measured here; module
  [03-02](../02-numpy/README.md).
- SciPy — [scipy.org](https://scipy.org): `scipy.sparse`, which exists for exactly
  the case where a matrix is too sparse to store as a dense array and too large
  for a dictionary of pairs.

## 13. Related lessons

- [03-01-04 Functions, Scope, Modules and Packages](./04-functions-modules.md) —
  the functions that take these containers as arguments.
- [03-01-06 Files, Text I/O and Data Encodings](./06-files-and-io.md) — where the
  rows that fill these containers come from.
- [03-01-09 Iterators, Generators and Lazy Evaluation for Large Data](./09-iterators-generators.md)
  — the container you *do not* build.
- [03-01-02 Types, Variables, Expressions and Operator Semantics](./02-types-and-variables.md)
  — the aliasing rules that make `namedtuple` and tuple keys safe.
- [03-02 NumPy](../02-numpy/README.md) — the array, which is both the compact
  layout and the fast lookup's replacement for elementwise work.

## 14. Exercises

[`exercises/05-data-structures-exercises.md`](./exercises/05-data-structures-exercises.md) —
nine problems, ★ to ★★★. Problem ★★4 requires the measured lookup numbers;
problem ★★★8 asks you to predict, from one measurement at n = 3,000, the wall
clock of a quadratic routine at n = 10⁵ and then verify the prediction; problem
★★★9 asks you to find the number of lookups below which building the dictionary is
the slower choice.

## 15. Self-assessment checklist

- [ ] I can name the four containers and the operation each is optimal for.
- [ ] I can explain why a dictionary lookup is O(1) and a list scan is O(n).
- [ ] I have reproduced a list-versus-dictionary speed-up of several hundred and a
      quadratic-versus-linear speed-up of about two hundred.
- [ ] I can compute the factor by which a quadratic routine's work grows when n
      grows by a stated factor.
- [ ] I can state the memory trade in bytes per element, measured.
- [ ] I can choose between tuple, namedtuple and dataclass for a record.
- [ ] I can replace a manual group-by loop with `defaultdict` and say what changed
      (readability, not complexity).
