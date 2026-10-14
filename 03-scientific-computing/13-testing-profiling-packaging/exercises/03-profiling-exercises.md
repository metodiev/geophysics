# Exercises — 03-13-03 Profiling CPU and Memory: cProfile, line_profiler, memory_profiler

Attempt these **closed-book** before opening the
[solutions](./03-profiling-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems marked **[demo]** refer to
[`../code/profiling_demo.py`](../code/profiling_demo.py) and
[`../code/benchmark_folklore_demo.py`](../code/benchmark_folklore_demo.py); run
them and report actual output:

```
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/profiling_demo.py
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/benchmark_folklore_demo.py
```

The lesson is [`../03-profiling.md`](../03-profiling.md).

---

## ★ Foundational

**★1. [demo]** The profiler's per-call overhead was measured as ~76 ns.

(a) One run of `python_workload(2000)` makes 1 call to `python_workload`, 2000
to `msd_kernel` and 1999 to `math.fsum`. How many instrumented Python calls is
that, what absolute overhead does 76 ns per call predict, and what slow-down does
that give against a measured bare time of 0.22 ms? Compare with the measured
profiled time of 0.50 ms.
(b) The NumPy-heavy workload's body performs 400 scalar ufunc calls per
repetition, 50 repetitions per timed run. How many *instrumented* calls does that
make, and why is the answer not 20 000?
(c) State the one rule that lets you quote a performance number without quoting
the machine.

**★2. [demo]** The crossover table for summing an existing Python list versus
`np.sum` on the array:

| $n$ | `sum(list)` ns | `np.sum(arr)` ns |
|---|---|---|
| 64 | 162.3 | 673.2 |
| 256 | 507.2 | 722.3 |
| 384 | 783.5 | 716.3 |
| 1024 | 1905.8 | 761.9 |

(a) From the two rows at $n = 64$ and $n = 1024$, estimate the marginal cost per
element of each method.
(b) Estimate `np.sum`'s fixed call overhead from the four rows.
(c) Predict the crossover $n$ and compare with the observed 256–384 bracket.

**★3.** State whether each statement is a property of the code or of the machine,
and say how you would test it: (a) `ncalls` for a function; (b) `tottime`;
(c) the number of elements in a temporary array; (d) the peak traced memory;
(e) the slow-down factor under `cProfile`.

---

## ★★ Applied

**★★4. [demo]** The folklore demo reports, over three independent repetitions of
the whole paired experiment:

```
C1 'x*x is faster than x**2':      ratios 1.083, 1.104, 1.099
C2 'np.sqrt faster than x**0.5':   ratios 1.017, 0.999, 1.008
C3 'axis=0 sum is cache-hostile':  median ratio 1.07 (range 1.03-1.14)
```

(a) For C1, state the claim's prediction about the ratio and whether the
measurement supports it.
(b) For C2, explain why the statistic that matters is not the median but the fact
that the ratio crosses 1.0.
(c) For C3, a textbook cache argument predicts a factor of two to eight. State
the measured factor and give the mechanism that hides the penalty in NumPy.

**★★5. [demo]** The memory measurements are

```
a @ a                 peak  0.00 MB
np.sum(a*a)           peak 32.00 MB
np.einsum('i,i->')    peak  0.00 MB
```

(a) Explain why `np.sum(a*a)` peaks at exactly one array.
(b) Explain why `einsum` allocates nothing and yet is the *slowest* of the three
(measured 435 µs against 375 µs for `np.sum(a*a)` and 57 µs for `a @ a`).
(c) State what a hypothesis "the arithmetic is the cost" predicts here, and what
the measurement does to it.

**★★6.** A colleague offers this benchmark as evidence that a rewrite is 15%
faster: they run the old code for one iteration, print the elapsed time, run the
new code for one iteration and print its elapsed time, and repeat the pair once.

(a) List three distinct problems with the protocol.
(b) The lesson measured a 13% spread between the minimum and maximum of twelve
successive timings of a single call, and 38% in a second such run. Use that to
say whether a 15% difference so measured is a result.
(c) Rewrite the protocol so that it could support the claim.

---

## ★★★ Research-oriented

**★★★7. [demo]** `cProfile` on the NumPy-heavy workload reports
`stats.total_calls = 1024` and cannot identify the hot line, while
`sys.settrace` reports 400 hits on the loop body.

(a) Explain the mechanism that makes the ufunc calls invisible, and name one
other callable from this module's code that *is* visible for the same reason.
(b) `cProfile.Profile` can write its data to a file with `dump_stats()`, and
`pstats.Stats` can then load it and do what the one-off printed table cannot:
`strip_dirs()` to merge entries from the same file, `print_callers()` and
`print_callees()` to see the calling relationships, and `Stats.add()` to *combine*
two dumps — which is how you compare a profile before and after a change without
keeping two tables side by side. State what each of those three buys for the
question "which change actually helped".
(c) Propose a test that fails if someone reintroduces the Python loop, and state
why an assertion on the elapsed time would be the wrong mechanism.

**★★★8. [demo]** The C5 result is that `a @ a` beats `np.sum(a*a)` by about a
factor 7 for a sum of squares.

(a) State the two distinct causes and say which one is measured by
`tracemalloc`.
(b) Design an experiment that separates the two causes quantitatively — for
example by comparing a reduction of a preallocated product array against a fused
dot.
(c) The folklore demo caps each experiment at 40 paired rounds. State what
increasing the round count buys, and what it cannot buy.

**★★★9.** You must decide whether to spend a week rewriting an inner loop that
occupies 30% of a processing pipeline's runtime, or two days adding a cache in
front of an I/O step that occupies 55%.

(a) State the decision from the profile alone.
(b) State two facts the profile does not give you that could reverse the
decision.
(c) Write the two lines of test that would prevent the optimisation from being
silently un-done by a later refactor.
