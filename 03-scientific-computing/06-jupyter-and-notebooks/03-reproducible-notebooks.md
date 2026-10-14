---
id: 03-06-03
title: "Making Notebooks Reproducible (Restart-and-Run-All)"
level: intermediate
prereqs: ["03-06-01", "03-02-06"]
estimated_minutes: 90
tags: [reproducibility, notebooks, seeds, determinism, testing]
---

# Making Notebooks Reproducible (Restart-and-Run-All)

A result is reproducible when someone else, starting from the same inputs, gets
the same numbers. In a notebook the phrase has a narrower and more checkable
meaning: **the outputs stored in the file are the outputs that a single
top-to-bottom run of that file produces, in an environment like mine.**

That is a small claim, and it is much harder to satisfy than it sounds. This
lesson measures the three ways it typically fails — hidden state, unseeded
randomness, and process-level nondeterminism — and gives the operations that
repair each one.

The mechanism is developed in [lesson 01](./01-notebook-workflow.md); here we
build the tests. Run the demonstration first:

```bash
.venv/bin/python 03-scientific-computing/06-jupyter-and-notebooks/code/reproducible_notebook_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** reproducibility for a notebook as a property of its stored outputs,
   and distinguish it from scientific correctness.
2. **Compute** a digest of a notebook's outputs that ignores bookkeeping, and use
   it to decide whether two runs agree.
3. **Measure** the distance between two unseeded runs and explain why
   "statistically identical" is not the same as "identical".
4. **Quantify** order dependence with a number, rather than describing it.
5. **Explain** why floating-point summation is order-dependent, with a measured
   example in which one ordering loses an additive term entirely.
6. **Identify** process-level nondeterminism — hash randomisation in particular —
   as a source of irreproducibility that no seed in the notebook can fix.

## Prerequisites

- [03-06-01 Notebook Workflow, Cells, Kernels and Execution Order](./01-notebook-workflow.md)
  — kernels, counts and hidden state.
- [03-02-06 Random Number Generation with NumPy](../02-numpy/06-random-module.md)
  — `default_rng` and seeds, which this lesson tests rather than introduces.

## 1. Intuition: a digest is to a notebook what a checksum is to a file

You cannot eyeball two notebooks and conclude that they agree: there are too many
numbers and they are too similar. So compute one number that stands for all of
them.

The digest in the demonstration serialises every cell's source and outputs —
**excluding `execution_count`** — and hashes it:

```python
def digest(nb) -> str:
    payload = []
    for cell in nb.cells:
        payload.append({
            "type": cell.cell_type,
            "source": cell.source,
            "outputs": [{k: v for k, v in out.items() if k != "execution_count"}
                        for out in cell.get("outputs", [])],
        })
    blob = json.dumps(payload, sort_keys=True, default=str).encode()
    return hashlib.sha256(blob).hexdigest()
```

The exclusion is the point. Counts are bookkeeping: they change when a cell is
clicked again and they say nothing about the numbers. A digest that included them
would report every notebook as irreproducible. A digest that excludes them
answers the only question that matters: **did a number change?**

## 2. Definitions

**Reproducible (notebook).** Running the file from a fresh kernel, top to bottom,
yields outputs whose digest equals the stored one.

**Deterministic (cell).** The same source, executed twice in the same
environment, produces the same output.

**Seed.** A value that initialises a pseudorandom sequence so that the sequence
is reproducible. `numpy.random.default_rng(20261014)` is the modern form.

**Hidden state.** State in the kernel that no cell re-creates on a top-to-bottom
run: the result of an out-of-order click, a modified global, a changed working
directory.

**Process-level nondeterminism.** Variation between separate interpreter
processes that is not caused by anything in the notebook's source. The measured
example below is hash randomisation of `str` keys.

## 3. Seeded against unseeded, measured

The demonstration executes the same two-cell notebook twice, in two separate
kernels. With a named seed:

```
  run 1 output: -0.023547 +0.023091 -0.040508 +0.093048 -0.073082
  run 2 output: -0.023547 +0.023091 -0.040508 +0.093048 -0.073082
  digests equal: True
```

Without one:

```
  run 1 output: +0.036995 +0.044866 -0.060362 +0.004039 +0.052473
  run 2 output: +0.016889 +0.014106 +0.094316 -0.041094 +0.124050
  digests equal: False
  max |difference| between the two runs: 0.154678 (dimensionless noise)
  runs disagree in all 5 of 5 values: True
```

The unseeded runs are *statistically identical* — both are five standard normal
deviates with mean 0 and standard deviation 0.05 — and *numerically different*.
That distinction is the whole reason this lesson exists. A figure regenerated
from the unseeded notebook is a different figure; a published panel cannot be
reproduced even by its own author, except in the weak sense that the statistics
match.

The rule follows directly: **every stochastic step in a notebook carries a named
seed, and the seed is visible in the cell.** A seed chosen once and stored in a
variable is better than a literal, because it is one edit to change every
realisation.

## 4. Order dependence, quantified

Lesson 01 counted the legal execution orders. Here we measure what an illegal one
costs:

```
  cells clicked 0, 1, 2 -> v = 0.098100 m/s
  cells clicked 0, 2, 1 -> v = 0.009810 m/s
  ratio between the two answers: 10.0
  source of cell 1 identical in both files: True
```

Cell 1 computed $v = g\,\Delta t$; cell 2 changed $\Delta t$ from 0.01 s to
0.001 s. Both notebooks are identical in every cell's source, and their answers
differ by a factor of ten. In dimensional terms both are correct:

$$[v] = \mathrm{m\,s^{-2}}\cdot\mathrm{s} = \mathrm{m\,s^{-1}},$$

so no unit check distinguishes them. **Restart-and-run-all is the operation that
makes the answer a property of the file**, and it is the only one.

### 4.1 Why restart-and-run-all is not a habit but a proof obligation

For a notebook with dependency relation $\prec$ (lesson 01, §6), a
restart-and-run-all executes the file order $\pi = (1, 2, \dots, n)$. That order
is legal **iff** no cell depends on a later one:

$$\forall\, i,j: \quad i \prec j \;\Longrightarrow\; i < j.$$

If the notebook was developed by clicking around — which is how notebooks are
developed — this condition is exactly what you do *not* know. Running it once, in
order, on a fresh kernel, is the test. It is cheap; the expensive failure is the
one that survives to a paper.

## 5. A derivation: summation is not associative, and the notebook is where you
notice

Floating-point addition is not associative. Write $\mathrm{fl}(x)$ for the
nearest representable double to $x$ and let $\epsilon = 2^{-52} \approx
2.22\times10^{-16}$ be the unit roundoff. Then for any $a$,

$$\mathrm{fl}(a + \delta) = a \quad\text{whenever}\quad |\delta| <
\epsilon\,|a|,$$

so an additive term smaller than $\epsilon$ times the running total is **lost**,
not rounded.

The demonstration makes the loss visible in two ways:

```
  np.sum of 200 000 standard normals (seeded):        -556.48923188998879
  same values summed in reverse order:                -556.48923188998913
  same values summed in sorted order:                 -556.48923188998015
  math.fsum, correctly rounded:                       -556.48923188998901
  distinct results among the four orders: 4
  np.sum([1e16, 1.0, -1e16]) = +0   (the 1.0 is absorbed, then added back as zero)
  math.fsum([1e16, 1.0, -1e16]) = +1
```

Four ways of adding the same 200 000 numbers, four different last bits — a spread
of about $3\times10^{-14}$ absolute, or ~130 ulp, on a value of magnitude 556.
And the second pair is categorical: adding $1$ to $10^{16}$ in binary64 gives
exactly $10^{16}$, so the $+1$ is absorbed and never comes back; `math.fsum`,
which accumulates the rounding error separately, returns the true answer 1.

Three consequences for reproducibility testing:

1. **A digest is a valid reproducibility check**, because NumPy's pairwise
   summation is deterministic for a given array length and order.
2. **It is only valid if the order does not change.** Reordering a column, or
   loading the same data with a different sort, changes the last bits and the
   digest legitimately changes.
3. **A changed last bit is not a bug**, so a digest is a *screening* tool: it
   tells you where to look, and the tolerance you then apply has to come from the
   physics, not from the float.

The general rule: compare with a tolerance derived from the quantity's
uncertainty, and use the digest to decide *which* numbers to compare.

## 6. Process-level nondeterminism

Two kernels running the same cell can differ even with no randomness in the cell,
because the *process* differs. The demonstration runs four subprocesses:

```
  process 1: epsilon,alpha,gamma,zeta,beta,delta
  process 2: epsilon,zeta,beta,alpha,delta,gamma
  process 3: alpha,epsilon,delta,zeta,gamma,beta
  process 4: delta,zeta,epsilon,gamma,beta,alpha
  distinct orders observed in 4 processes: 4
  with PYTHONHASHSEED=0, two processes agree: True
```

Python randomises the hash of `str` and `bytes` keys at interpreter start-up, so
a `set` of station names iterates in a different order in every process. A
notebook that plots a legend in `set` order, or writes a CSV whose row order
comes from a `set`, produces different output in every kernel — with no randomness
anywhere in the code.

The fixes are trivial and total:

- iterate `sorted(s)` whenever the order is visible;
- never rely on dict/set iteration order for anything a reader sees;
- if you must pin it, `PYTHONHASHSEED=0` in the environment makes the process
  reproducible — at the cost of disabling a denial-of-service mitigation, so
  prefer sorting.

## 7. Assumptions, units and limitations

- **Environment reproducibility is not addressed here.** A notebook run under a
  different NumPy can produce a different digest for the same source. This lesson
  measures *within* one environment; the version pinning that extends it is the
  subject of [03-13](../13-testing-profiling-packaging/README.md). The
  demonstration's own summary is blunt about it: the file "does not carry the
  environment".
- **The digest excludes counts, not timing metadata.** `nbclient` records
  execution timestamps in cell metadata when `record_timing` is true (the
  default), so the **file's** SHA-256 digest differed between two runs of the
  same script, while the digest of sources and outputs was identical. Do not
  quote a notebook file's hash as a reproducibility claim.
- **Units are not in the digest's reach either.** Two runs can agree bit for bit
  while the notebook's stored values are in mGal in one and SI in the other,
  because the convention lives in a markdown cell. Digest equality is necessary,
  not sufficient.
- **A seeded run is not a correct run.** Fixing the seed makes a wrong model
  wrong in a reproducible way. That is genuinely useful for debugging and
  genuinely irrelevant to whether the model is right.
- **No wall-clock times are quoted.** Kernel start-up and run time are
  machine-dependent; the measurements above are counts, digests and values.

## 8. Worked examples

### 8.1 Turning a flaky notebook into a testable one

Start from the failing state: outputs do not match a fresh run. The repair
sequence, in order:

1. **Restart and run all.** If the digest now matches, the problem was hidden
   state. If it does not, continue.
2. **Seed every random call.** Use `np.random.default_rng(seed)` in one cell and
   pass that generator to every consumer.
3. **Sort anything that iterates a set or dict.**
4. **Move stochastic or expensive stages into a script** that writes a file, and
   have the notebook read the file. The notebook then has no randomness at all.
5. **Record the versions** of the packages the notebook imports, next to the
   digest. The demonstration measures the digest as 16 hex characters; the
   versions are the other half of the claim.

### 8.2 A failure mode to check for explicitly

The demonstration ran a notebook with a failing cell under both client settings:

```
  allow_errors=True  -> error outputs stored: ['ValueError']
  cells executed anyway: [1, 2, 3]
  allow_errors=False -> raised CellExecutionError
  cells with a stored output afterwards: 2 of 3 (cell 3 untested and unrecorded)
  cell 3 stdout: ''
```

Read that carefully. With `allow_errors=True` the run *continued past the
failure*: all three cells have counts, and the notebook is saved looking
executed. With `allow_errors=False` the run stopped, two cells have outputs, and
cell 3 was never tested. The two settings answer different questions:

- `allow_errors=True` is for producing a readable notebook that shows where
  things went wrong.
- `allow_errors=False` — which is what `jupyter nbconvert --execute` does by
  default — is for *testing*, because a run that continues past a failure cannot
  tell you whether the rest of the notebook worked.

A reproducible notebook is executed with the second setting in CI, and with the
first when someone needs to read it.

### 8.3 What a digest does and does not prove

Suppose a colleague sends you a notebook and its digest. You re-run and get the
same digest. What do you know? That the outputs are identical to the ones they
saw, in the same environment, for the same cell sources. What do you *not* know?
That the inputs were the file they claim (the data could have changed and the
digest would change — unless they sent the data too), that the environment is the
same, or that the model is right. The digest is a fingerprint, not a proof.

## 9. Python demonstration

`code/reproducible_notebook_demo.py` runs in seven parts:

| Part | Measures | Key measured output |
|---|---|---|
| 1 | Seeded notebook, twice | `digests equal: True` |
| 2 | Unseeded notebook, twice | `max |difference| = 0.154678`, 5 of 5 values differ |
| 3 | Two execution orders | `0.098100` against `0.009810`, ratio `10.0` |
| 4 | Summation order | 4 distinct results among 4 orders; `0` against `1` |
| 5 | Failure handling | stored traceback vs raised `CellExecutionError` |
| 6 | Hash randomisation | 4 distinct orders in 4 processes |
| 7 | Artefacts | `reproducible_demo.ipynb`, 300 bytes, nbformat 4.5 |

Run it and change one thing at a time. In particular, try Part 3 with a
*seeded* random step in the middle: the answers will differ between orders even
though every individual cell is deterministic, which is the clearest possible
demonstration that seeds do not fix order dependence.

## 10. Exercises

Solutions are in
[`exercises/03-reproducible-notebooks-solutions.md`](./exercises/03-reproducible-notebooks-solutions.md).

### ★ Foundational

**★1.** For each item, say whether it makes a notebook irreproducible and why:
(a) `np.random.random()`, (b) `np.random.default_rng(7).random()`, (c) iterating
a `set` of strings, (d) `time.time()`, (e) reading a CSV that changed on disk.

**★2.** Why does the digest exclude `execution_count`?

**★3.** A notebook's outputs match after a restart-and-run-all. Name two things
that does *not* prove.

**★4.** Compute by hand: `np.sum([1e16, 1.0, -1e16])` and
`math.fsum([1e16, 1.0, -1e16])`. Explain the difference in one sentence.

### ★★ Applied

**★★5.** Take any notebook of your own with more than five cells. Restart and run
all, then compute the output digest of Section 1 for the stored version and the
fresh version. Report both digests and whether they agree. If they disagree,
identify the first cell whose output changed.

**★★6.** Reproduce the order-dependence measurement: build the three-cell
notebook from Section 4 and execute it in both orders with `nbclient`. Report the
two values and the ratio, then modify the notebook so that the two orders agree,
and state what you changed.

**★★7.** Quantify the unseeded distance. Run an unseeded five-value notebook 200
times, record each run's values, and report the standard deviation of the first
value across runs and the maximum absolute difference between any two runs.
Compare with the 0.05 standard deviation of the underlying distribution and
explain the relationship.

**★★8.** Write a pre-commit hook that fails if any `.ipynb` under a directory
contains a call to `numpy.random` without `default_rng` on the same line or
earlier in the file. Report how many of your own notebooks it flags.

### ★★★ Research-oriented

**★★★9.** Measure the summation error's *scaling*. For $n$ in a geometric
sequence from $10^3$ to $10^7$, sum $n$ standard normal deviates (one seeded
draw) by naive accumulation in a Python loop, by `np.sum`, and by `math.fsum`,
and compare each against the `fsum` value. Report the growth of the absolute
error with $n$ and the empirical exponent. State whether you would expect the
naive loop's exponent to differ from `np.sum`'s, and why.

**★★★10.** Assess hash randomisation's reach. Run the same 20-line analysis
script in 50 subprocesses with `PYTHONHASHSEED=random`, and count how many produce
byte-identical stdout. Then modify the script to sort every set iteration and
repeat the experiment. Report both counts and the number of lines you changed —
this is a measurement of how cheap the fix is.

## 11. Common mistakes

1. **Calling a notebook reproducible because the numbers look the same.** Compute
   the digest.
2. **Seeding the generator in one cell and creating a new one in another.** The
   second generator has a different seed; the stream is no longer reproducible.
3. **Believing a seed fixes order dependence.** It does not; it fixes the stream.
4. **Comparing floats for equality in a test.** Compare with a tolerance chosen
   from the measurement, and say what it is.
5. **Quoting a notebook file's SHA-256 as a reproducibility claim.** It changes
   with timing metadata.
6. **Running the notebook with `allow_errors=True` and calling it a test.**
   The run continued past the failure.
7. **Forgetting the environment.** A digest without the package versions is half
   a claim.
8. **Ignoring `set` order.** Deterministic code can still print in a different
   order in every process.

## 12. Real-world applications

- **A published figure.** The notebook that made it, a fixed seed, and a recorded
  digest make the panel reproducible by a reviewer who has the repository and no
  correspondence with you.
- **A processing pipeline for a survey.** The randomness is confined to a
  cross-validation split; its seed is fixed and reported, and the rest of the
  chain is deterministic, which makes the pipeline testable.
- **A teaching notebook with a demonstration of noise.** Students are asked to
  change one seed and observe that the *statistics* stay and the *numbers* move —
  which is the difference between a realisation and a distribution.
- **A regulatory submission.** Deterministic outputs, recorded versions, and a
  digest per run are what makes an analysis auditable rather than merely
  described.
- **Machine learning on geophysical data.** Splits, initialisations and dropout
  are all seeded; the environment is pinned; and the digest is compared before a
  model is retrained, so that a change in the metrics can be attributed to the
  model rather than to the sampler.

## 13. Further reading

- **Jupyter documentation** (jupyter.org). Level: beginner. The
  restart-and-run-all operation and its rationale.
- **NumPy random documentation** (numpy.org). Level: intermediate. The
  `Generator`/`default_rng` interface, and why it replaced the legacy global
  state.
- **Pimentel, J. F. et al. (2019). A large-scale study about quality and
  reproducibility of Jupyter notebooks. *MSR 2019*.** Level: advanced. Measured
  statistics on execution-order defects in public notebooks.
- **Granger, B. E. & Perez, F. (2021). Jupyter: Thinking and storytelling with
  code and data. *Computing in Science & Engineering*.** Level: intermediate.
  The design argument for literate documents, with an honest discussion of their
  reproducibility limits.
- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms* (2nd
  ed.). SIAM.** Chapter 4. Level: advanced. Summation error analysis, including
  the correctly rounded sums that `math.fsum` implements.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 14. Related lessons

- [01 Notebook Workflow, Cells, Kernels and Execution Order](./01-notebook-workflow.md)
  — the counts and hidden state this lesson tests.
- [02 Markdown and LaTeX in Notebooks](./02-markdown-and-latex.md) — the half of
  the file a digest cannot check.
- [04 Converting Notebooks to Scripts, Tests and Reports](./04-notebooks-to-scripts.md)
  — turning the reproducibility claim into an assertion.
- [03-13 Testing, Profiling and Packaging](../13-testing-profiling-packaging/README.md)
  — pytest, assertions and floating-point comparison.
- [01-01-04 Floating-Point Representation, Round-Off and Catastrophic
  Cancellation](../../01-mathematics/01-arithmetic/04-floating-point.md) — the
  arithmetic behind Section 5.

## 15. Self-assessment checklist

- [ ] I can define notebook reproducibility as a statement about stored outputs.
      (§2)
- [ ] I can compute an output digest that ignores counts. (§1)
- [ ] I can measure the distance between two unseeded runs. (§3)
- [ ] I can quantify an order dependence with a ratio. (§4)
- [ ] I can explain why `np.sum([1e16, 1.0, -1e16])` is 0. (§5)
- [ ] I can name one source of nondeterminism that no seed in the notebook fixes.
      (§6)
- [ ] I can say what a matching digest does and does not prove. (§8.3)
- [ ] I know to run a notebook with errors fatal when testing it. (§8.2)
