# Exercises — 03-06-03 Making Notebooks Reproducible

> Solutions, with the measured values, are in
> [`03-reproducible-notebooks-solutions.md`](./03-reproducible-notebooks-solutions.md).

---

## ★ Foundational

**★1.** For each item, say whether it makes a notebook irreproducible and why:
(a) `np.random.random()`, (b) `np.random.default_rng(7).random()`, (c) iterating a
`set` of strings, (d) `time.time()`, (e) reading a CSV that changed on disk.

**★2.** Why does the output digest exclude `execution_count`?

**★3.** A notebook's outputs match after a restart-and-run-all. Name two things
that does *not* prove.

**★4.** Compute by hand `np.sum([1e16, 1.0, -1e16])` and
`math.fsum([1e16, 1.0, -1e16])`, and explain the difference in one sentence.

**★5.** State the difference between `allow_errors=True` and `allow_errors=False`
in one sentence each, and say which one is a test.

---

## ★★ Applied

**★★6.** Take a notebook of your own with more than five cells. Restart and run
all, then compute the output digest for the stored version and the fresh version.
Report both digests and whether they agree. If they disagree, identify the first
cell whose output changed.

**★★7.** Reproduce the order-dependence measurement: build the three-cell notebook
of the lesson's §4 and execute it in both orders with `nbclient`. Report the two
values and the ratio, then modify the notebook so the two orders agree and state
what you changed.

**★★8.** Quantify the unseeded distance. Run an unseeded five-value notebook 200
times, record each run's values, and report the standard deviation of the first
value across runs and the maximum absolute difference between any two runs.
Compare with the 0.05 standard deviation of the underlying distribution and
explain the relationship.

**★★9.** Write a pre-commit hook that fails if any `.ipynb` under a directory
contains a call to `numpy.random` without `default_rng` on the same line or
earlier in the file. Report how many of your own notebooks it flags.

**★★10.** The demonstration reports that the same notebook saved twice had
different file digests while the output digests matched. Explain why, with
reference to what `nbclient` records, and state which digest you would quote in a
paper.

---

## ★★★ Research-oriented

**★★★11.** Measure the summation error's scaling. For $n$ in a geometric sequence
from $10^3$ to $10^7$, sum $n$ standard normal deviates (one seeded draw) by naive
accumulation in a Python loop, by `np.sum`, and by `math.fsum`, and compare each
against the `fsum` value. Report the growth of the absolute error with $n$ and the
empirical exponent, and state whether you would expect the naive loop's exponent
to differ from `np.sum`'s.

**★★★12.** Assess hash randomisation's reach. Run the same 20-line analysis
script in 50 subprocesses with `PYTHONHASHSEED=random`, and count how many produce
byte-identical stdout. Then modify the script to sort every set iteration and
repeat. Report both counts and the number of lines you changed.

**★★★13.** Design a reproducibility report for a published figure: list every
number a reader would need in order to regenerate it, including the environment.
State which items you could obtain from the notebook, which from the environment,
and which you would have to record by hand.
