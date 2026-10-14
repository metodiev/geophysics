# Exercises — 03-01-09 Iterators, Generators and Lazy Evaluation for Large Data

Attempt these **closed-book** before opening the
[solutions](./09-iterators-generators-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/iterators_generators_demo.py`](../code/iterators_generators_demo.py)
require you to run it and report its **actual** output.

---

## ★ Foundational

**★1.** Describe the iterator protocol in three lines: what `iter(obj)` returns,
what `next(it)` does, and what a `for` loop does with those two operations.

---

**★2.** For each snippet, state whether any file is opened and any line is read at
the moment the marked statement executes.

```python
def gen(path):
    print("opening")
    with path.open() as handle:
        for line in handle:
            yield line

g = gen(p)        # (a)
first = next(g)   # (b)
rest = list(g)    # (c)
print(sum(1 for _ in g))   # (d)
```

---

**★3.** Rewrite each eager construct lazily, and say what changes in memory.

(a) `rows = [line.split(",") for line in handle]`
(b) `total = sum([float(x) for x in values])`
(c) `ok = [r for r in records if r.magnitude >= 2.0]`

---

## ★★ Applied

**★★4.** Run `python3 iterators_generators_demo.py` and report:

(a) the catalogue's size in MB and its row count;
(b) the number of events selected above $M_c = 2.0$, the elapsed time and the mean
depth;
(c) the two peak-memory figures and the ratio;
(d) the absolute and relative difference between the two means, and whether they
agree to a relative tolerance of $10^{-12}$;
(e) the single-use demonstration's four numbers.

---

**★★5.** Using `itertools.islice`:

(a) write an infinite generator `walks(step=1.0)` yielding a random-walk position,
seeded for reproducibility;
(b) take the first 20 steps and print them;
(c) compute the maximum absolute position over the first $10^{5}$ steps *without*
materialising the walk;
(d) explain why `list(walks())` is a hang, and what the `islice` changes.

---

**★★6.** A file has 10⁸ rows at 38.5 bytes per row.

(a) Compute the file size in GB.
(b) Estimate the peak memory of `list(iter_records(iter_lines(path)))` if each
parsed record is a 5-tuple of a string and four floats, using the demo's measured
48.87 MB for $2\times10^{5}$ rows as the calibration.
(c) Estimate the peak memory of the generator pipeline.
(d) State the smallest machine that can run each, and the one code change that
converts the first into the second.

---

## ★★★ Research-oriented

**★★★7.** Convert a two-pass script to one pass.

A script (i) reads a CSV of station readings to compute the mean and standard
deviation of the anomaly, then (ii) re-reads the same file to select the readings
more than two standard deviations from the mean.

(a) Explain why the second pass is required by the current code.
(b) Rewrite it as a single pass by accumulating the sums needed for mean and
variance, then explaining what is *missing* from a single pass (the selection
itself).
(c) Give two designs that resolve the tension: one that buffers only what it needs,
one that re-opens the file. State the memory cost of each.
(d) State which you would choose for a 10 GB file and why.

---

**★★★8.** Prove a lazy rewrite equivalent to an eager one.

For the demo's mean depth:

(a) compute the eager and lazy means with exact rational arithmetic on the first
1 000 rows, so the exact answer is known;
(b) compute both with `float` and compare each with the exact value;
(c) report the two rounded differences in units of the last place of the float
result;
(d) explain why the demo's two floating-point sums differ by $3.45\times10^{-13}$ km
even though both are "the same" reduction;
(e) state the general rule this implies for comparing a refactored pipeline against
its original.

---

**★★★9.** Project the memory scaling.

Using the demo's measurements ($2\times10^{5}$ rows → 48.87 MB eager, 0.15 MB
lazy):

(a) fit a linear model for the eager peak as a function of $n$;
(b) predict the peak at $n = 10^{6}, 10^{7}, 10^{8}$;
(c) explain why the lazy peak does not scale with $n$, and name the two quantities
that do grow with the data *if you keep them* (a list of distinct place names, for
instance);
(d) state the design rule that follows: which reductions *require* materialising and
which do not.
