# Exercises — 03-01-10 Context Managers, Decorators and Functional Idioms

Attempt these **closed-book** before opening the
[solutions](./10-context-managers-decorators-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/context_decorators_demo.py`](../code/context_decorators_demo.py) or
[`../code/catalog_report.py`](../code/catalog_report.py) require you to run them
and report their **actual** output.

---

## ★ Foundational

**★1.** For each resource, name the context-manager form you would use and what
its `__exit__` must do.

(a) an open file being written;
(b) a lock around a shared cache;
(c) a temporary directory that must be removed;
(d) a result file that must not be published unless the computation succeeded;
(e) an OpenBLAS thread-count setting that must be restored afterwards.

---

**★2.** Explain, in two sentences, what each of these does and why it matters:

(a) `handle.flush()` followed by `os.fsync(handle.fileno())`;
(b) `os.replace(tmp, target)` instead of `target.write_text(...)`;
(c) `functools.wraps(func)` inside a decorator;
(d) `lru_cache` on a function that reads a file.

---

**★3.** State what `__exit__` returning `True` does, and give one legitimate and
one illegitimate use.

---

## ★★ Applied

**★★4.** Run `python3 context_decorators_demo.py` and report:

(a) the two timing lines for the same block;
(b) the four lines of the atomic-write section;
(c) the three `functools.wraps` preservation results;
(d) the `lru_cache` hit/miss counts, the total time, and the printed travel time.

Then answer: after the simulated mid-write failure, what does
`result.csv` contain, and where is the partially written data?

---

**★★5.** The demo's cache section reports

```text
  calls made : 1000
  hits       : 996, misses: 4
  total time : 0.21 ms for 1000 calls
  t0(1000 m) : 666.666667 ms
```

(a) Compute the travel time by hand for $z = 1000$ m and $v = 3000$ m s⁻¹, and
state the unit of the printed `666.666667`.
(b) Explain why there are exactly four misses for 1 000 calls.
(c) State two ways this cache becomes a bug, and the change to each that fixes it.
(d) Estimate the time saved, given that each miss performs a 2 000-step loop.

---

**★★6.** The demo's retry section prints

```text
  [retry] attempt 1/3 failed: error 0.500 exceeds tolerance 0.300
  converged with error 0.250 after 2 attempts
```

(a) Modify the retry decorator to also catch a second exception type, and explain
why catching `Exception` instead would be wrong here.
(b) Add a `finally`-style guarantee that the number of attempts is recorded even
when the retry ultimately fails.
(c) State what the decorator must do when all attempts fail — and why returning
the last value would be worse than raising.

---

## ★★★ Research-oriented

**★★★7.** Write a logging decorator.

Write `@logged(logger)` that, for any function, logs the call's function name,
its arguments, its result, and either the elapsed time or the raised exception —
while preserving the wrapped function's `__name__`, `__doc__` and signature.

(a) Implement it with `functools.wraps` and `functools.partial`.
(b) Demonstrate it on a function that returns and on one that raises, showing the
two log records.
(c) Explain what `functools.wraps` copies and what it does *not* copy, and which of
those matters for a test runner that discovers tests by name.
(d) State one thing a logging decorator must not do to the return value, and the
bug that follows if it does.

---

**★★★8.** A re-runnable pipeline stage.

Design a function `process(input_path, output_path, params)` that:

1. writes `output_path` atomically;
2. writes a small sidecar `<output>.done.json` recording the input's SHA-256, the
   parameters, and the tool version;
3. skips the computation entirely if the sidecar matches, and re-runs it otherwise.

(a) Implement it, using a context manager for the atomic write and a decorator for
the timing.
(b) Show the first and second runs' output, and prove the second skipped the work.
(c) State three ways the "skip" test can be wrong, and how to make each safe.
(d) Explain why the sidecar must be written *after* the output, not before.

---

**★★★9.** Cache invalidation for an impure function.

A function `instrument_response(station, network, time)` fetches a response from a
remote service. It is decorated with `lru_cache(maxsize=128)`. The service's
responses change when a station's metadata is corrected.

(a) Explain why the cache is correct until the metadata changes and wrong
afterwards.
(b) Propose two designs that keep the speed-up while regaining correctness: one
keyed on a version, one keyed on a validity interval.
(c) State what each design trades away.
(d) Apply the same reasoning to `b_value_maxlik(magnitudes, mc)` from
`geophys_core`: is caching it safe, and if not, why not?

---

**★★★10.** Assemble the module.

Run `python3 catalog_report.py` and, for each line of its report, name the lesson
that contributed the mechanism that produced it. Then:

(a) add a decorator that prints the peak `tracemalloc` allocation of each step;
(b) add a context manager that refuses to publish the report if the
Monte-Carlo mean is further than three standard errors from the input $b$;
(c) state which of the two additions is *instrumentation* and which is *logic*, and
why the distinction decides where each belongs.
