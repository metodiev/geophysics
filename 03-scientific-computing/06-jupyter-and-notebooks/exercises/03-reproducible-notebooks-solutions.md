# Solutions — 03-06-03 Making Notebooks Reproducible

> **Read this after attempting the exercises.** All values are the demonstration's
> actual output, produced with nbformat 5.11.1, nbclient 0.11.0, NumPy 2.5.4 and
> Python 3.14.4.

---

## ★1 — What breaks reproducibility

| Item | Irreproducible? | Why |
|---|---|---|
| (a) `np.random.random()` | yes | draws from the global generator, seeded from the OS |
| (b) `np.random.default_rng(7).random()` | no | the stream is fixed by 7 |
| (c) iterating a `set` of strings | yes | Python randomises `str` hashes per process |
| (d) `time.time()` | yes | a value nothing can reproduce |
| (e) a CSV that changed on disk | yes | the input is not under the notebook's control |

Note (b): the *generator* must be created once and passed to consumers. Creating
`default_rng(7)` inside each cell restarts the stream and produces the same five
numbers everywhere, which is a different bug.

---

## ★2 — Why counts are excluded from the digest

Because they are bookkeeping, not results. The digest is intended to answer "did a
number change?", and a count changes whenever a cell is clicked again. Including
them would report every notebook as irreproducible. Measured:
`digests equal: True` for the seeded pair, where the counts in the two kernels
were identical anyway, and `digests equal: False` for the unseeded pair, where
the *values* differed — which is the discrimination the digest is for.

---

## ★3 — What a matching digest does not prove

Two of the following suffice:

1. That the model is right (it may be reproducibly wrong).
2. That the environment is the same (a different NumPy can change the digest, and
   the demonstration states that the file "does not carry the environment").
3. That the inputs were the ones claimed (the data could have changed).
4. That the units are what the prose says (units live in markdown).

---

## ★4 — Summation, by hand

`np.sum([1e16, 1.0, -1e16])` accumulates left to right: $10^{16} + 1$ rounds to
$10^{16}$ because the spacing of binary64 numbers at $10^{16}$ is 2, so the $+1$
is lost; subtracting $10^{16}$ then gives exactly 0. Measured:

```
  np.sum([1e16, 1.0, -1e16]) = +0
  math.fsum([1e16, 1.0, -1e16]) = +1
```

`math.fsum` carries the rounding error in a separate accumulator, so the answer is
the correctly rounded sum, 1.

---

## ★5 — The two client settings

- `allow_errors=True`: a failing cell stores its traceback as an output and the
  run continues. Measured: `error outputs stored: ['ValueError']` and
  `cells executed anyway: [1, 2, 3]`.
- `allow_errors=False`: a failing cell raises `CellExecutionError` and the run
  stops. Measured: `raised CellExecutionError`, and
  `cells with a stored output afterwards: 2 of 3 (cell 3 untested and unrecorded)`.

`allow_errors=False` is the test setting, because a run that continues past a
failure cannot tell you whether the rest of the notebook worked. It is also what
`jupyter nbconvert --execute` does by default.

---

## ★6 — Your own notebook

There is no universal answer; report what you measured. The two outcomes and their
meanings:

- **Digests agree:** the notebook is a record of a linear run, in this
  environment. Record the package versions beside the digest, because that is the
  half of the claim the notebook cannot carry.
- **Digests disagree:** the stored outputs came from a different kernel state.
  The first changed cell is the one to inspect; it is usually a cell that reads
  something set by a later cell, or a cell with an unseeded random draw.

---

## ★7 — Reproducing the order dependence

```python
cells = [code_cell("dt = 0.01  # s, sampling interval"),
         code_cell("v = 9.81 * dt\nprint(f'{v:.6f}')"),
         code_cell("dt = 0.001  # s, changed later in the session")]
run(order_nb, [[0, 1, 2]])      # -> 0.098100
run(other_nb,  [[0], [2], [1]]) # -> 0.009810
```

Measured ratio: `10.0`, with `source of cell 1 identical in both files: True`.

A modification that makes both orders agree: make cell 1 read the parameter from a
cell that cannot be re-run after it, or (better) pass `dt` as an argument —

```python
# cell 1
def velocity(dt):
    return 9.81 * dt
# cell 2
print(f"{velocity(0.01):.6f}")
```

Now no execution order changes the answer, because no cell reads state written by
another. That is the structural fix: **remove the shared mutable state rather than
manage its order.**

---

## ★8 — The unseeded distance

Measured over 200 runs of the five-value notebook, the reported summary is
`max |difference| between the two runs: 0.154678` for two runs, with
`runs disagree in all 5 of 5 values: True`. Over 200 runs the standard deviation of
the first value should be close to the underlying 0.05, and the maximum absolute
difference between any two of 200 five-value runs should approach
$0.05 \times 2 \times z$ for the largest pair — several tenths of a unit.

The relationship to state: the *spread over runs* estimates the underlying
standard deviation (0.05), while the *maximum pairwise difference* grows with the
number of runs sampled, because it is an extreme-value statistic. Two different
questions, two different numbers.

---

## ★9 — A hook that flags unseeded randomness

The check is a search of the notebook's code cells for `numpy.random.` or
`np.random.` not preceded in the same file by `default_rng`. Report what it finds;
what matters is the false-positive policy: `np.random.default_rng` itself contains
the substring `np.random`, so the pattern must exclude it explicitly.

---

## ★10 — Why the file digest differs and the output digest does not

`nbclient` records cell metadata when `record_timing` is true (the default),
including timestamps for the busy and idle states of each cell. The file's
SHA-256 therefore changes between runs even when nothing in the code or the
outputs changed. Measured in the demonstration: the saved notebook's digest was
`6dbefa8a8b6e1853` on one run and `f905b78c3ff54fb7` on the next, while the
source-and-output digest of the same notebook was stable.

In a paper, quote the **output** digest plus the package versions, and say
explicitly that the file bytes are not reproducible.

---

## ★11 — Summation error scaling

The expectation to check: `np.sum` uses pairwise summation, so its error grows
like $\log n$ for random signs, while a naive Python loop accumulates error like
$n$ (random walk $\sqrt n$ for zero-mean data). So yes, the exponents should
differ, and the measurement is the evidence. Report the fitted exponents and
state the sample size behind them: a single seeded draw per $n$ gives one point
per $n$, and a defensible study repeats with several seeds and reports the spread.

---

## ★12 — Hash randomisation's reach

Measured, on four subprocesses running the same `set`-iterating expression:

```
  process 1: epsilon,alpha,gamma,zeta,beta,delta
  process 2: epsilon,zeta,beta,alpha,delta,gamma
  process 3: alpha,epsilon,delta,zeta,gamma,beta
  process 4: delta,zeta,epsilon,gamma,beta,alpha
  distinct orders observed in 4 processes: 4
  with PYTHONHASHSEED=0, two processes agree: True
```

Four distinct orders in four processes. After sorting every set iteration, the
count should be 1 of 50, and the change is typically one `sorted(...)` call per
visible iteration — often a single line. That ratio (one line changed, all
variation removed) is the argument for doing it.

---

## ★13 — A reproducibility report for a figure

Items a reader needs:

1. **From the notebook:** cell sources, the seed values, the input file paths and
   their digests, the plotting parameters that are not in the data.
2. **From the environment:** Python version, every package version actually
   imported, the operating system, the font stack (for figures, because glyph
   fallback changes pixels).
3. **By hand:** the data itself (a DOI or an archive), the version of the data,
   the processing decisions made outside the notebook, and the output digest.

The notebook can carry (1) and, with a cell that prints them, (2). It cannot carry
(3), which is why a figure's provenance is never complete inside the notebook.
