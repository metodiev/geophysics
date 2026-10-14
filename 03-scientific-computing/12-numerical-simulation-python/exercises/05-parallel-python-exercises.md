# Exercises — 03-12-05 Parallelism in Python: Multiprocessing, Threads, Numba, JAX

Attempt these **closed-book** before opening the
[solutions](./05-parallel-python-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Run the demonstration first. It prints no wall-clock timings by design:

```
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/parallel_python_demo.py
```

---

## ★ Foundational

**★1.** Name the four parallelism mechanisms in the lesson and state, for each,
whether it releases the global interpreter lock and whether it scales across
nodes.

**★2.** Explain in three sentences why threads do not speed up a pure-Python
loop but do speed up a large NumPy array operation.

**★3.** State the measured number of logical CPUs and the multiprocessing start
method on this machine, and say why the start method matters for a workflow that
defines functions at the top level.

**★4.** List which of `numba`, `jax`, `mpi4py`, `dask` and `joblib` are installed
on this installation, and state what you would use each for.

**★5.** State the three questions the lesson says to answer before parallelising
anything.

---

## ★★ Applied

**★★6.** Run the demonstration's process pool at 1, 2, 4 and 8 workers and
report (a) the maximum absolute difference between the chunked field and the
serial field, (b) the value of `math.fsum` over every computed value, and (c) the
difference produced by reducing the *inexact* per-chunk `np.sum` values instead.
State the separate requirements that each of those three measurements tests, and
say what changes if the halo is removed.

**★★7.** Measure the error of four different groupings of a million-element sum
against `math.fsum`. Report the magnitudes as absolute and relative errors, and
state why "the results agree to ten digits" is not a reproducibility test. Check
whether the error decreases monotonically as the number of chunks grows, and
interpret the answer.

**★★8.** Verify the measured idle fractions 0.0002 %, 0.0030 % and 0.0120 % for
$N = 1\,003\,000$ split into 3, 7 and 16 workers with the remainder given to one
worker.

**★★9.** Permute 100 chunk partials into 500 random orders and count the
distinct totals produced by `math.fsum`, the built-in `sum`, `np.sum` of the
permuted list, and a manual `+=` loop. Report the counts and the spreads.

Then repeat the measurement on a *different* dataset — 100 unit-scale standard
normals — and report whether `sum()`'s set of totals is identical to the manual
loop's. State what the comparison shows about generalising an order-independence
claim from one dataset to the algorithm, and which of the four reductions
supports the unconditional claim.

**★★10.** The demonstration's thread test gives identical totals for 1, 2 and 4
threads. State the necessary condition for that identity and what would break it.

---

## ★★★ Research-oriented

**★★★11.** Convert the inner loop to a vectorised NumPy expression (numba is
not installed on this machine). Report which change you could measure and state
what you could *not* measure, and why not.

**★★★12.** Design a parallelism experiment that is fully reproducible without
quoting any elapsed time: state the work-partition metric, the determinism check
and the numerical-identity check, and explain why those three characterise
correctness but not speed.

**★★★13.** A colleague reports a parallel run that is 3.5× faster than serial on
8 cores with slightly different results. Write a three-sentence review response:
what you would ask for, what would resolve it, and the condition under which the
difference would be acceptable in a publication.
