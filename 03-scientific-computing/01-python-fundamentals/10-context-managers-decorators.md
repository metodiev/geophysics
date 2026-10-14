---
id: 03-01-10
title: "Context Managers, Decorators and Functional Idioms"
level: advanced
prereqs: ["03-01-04", "03-01-07"]
estimated_minutes: 75
tags: [context-managers, decorators, functools, atomic-write, reproducibility]
---

# Context Managers, Decorators and Functional Idioms

Long simulation jobs fail in a specific and expensive way: they fail *after* they
have written half of their output. A seven-hour inversion that dies at hour six
and leaves a truncated result file, a partially updated catalogue, or an open
database transaction is worse than one that died at minute two, because the
partial output looks like output. Both mechanisms in this lesson exist to prevent
that.

A **context manager** wraps a block so that cleanup is written once, next to the
acquisition, and cannot be skipped. A **decorator** wraps a function so that
cross-cutting bookkeeping — timing, caching, retrying, counting — is written once
and applied by name. Neither is a trick: they are the two ways Python lets you say
"run this extra code around this work, always".

This is the module's final lesson, and it is where the module's complete program
is assembled.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a context manager with `@contextlib.contextmanager`, and explain
   which part becomes `__enter__` and which becomes `__exit__`.
2. **Write** a class-based context manager, and say when it is preferable — in
   particular what `__exit__`'s return value controls.
3. **Implement** an atomic-write context manager that publishes a result only on
   clean exit, and explain why that prevents a truncated result.
4. **Write** a decorator with `functools.wraps`, and demonstrate why `wraps`
   matters.
5. **Apply** `functools.lru_cache` to a pure function, and state the one condition
   that makes memoisation safe.
6. **Explain** the order in which stacked decorators run, and what each order is
   measuring.
7. **Assemble** the module's complete program and run it end to end.

## Prerequisites

- [03-01-04 Functions, Scope, Modules and Packages](./04-functions-modules.md) —
  decorators are functions that take functions.
- [03-01-07 Exceptions, Assertions and Systematic Debugging](./07-errors-and-debugging.md)
  — `finally`, exception suppression and validation.

## 1. Context managers: cleanup that cannot be forgotten

Every resource has an acquire/release pair: open/close, lock/unlock, begin/commit.
Written by hand, the release is on a path that an early `return` or an exception
can skip:

```python
handle = path.open("w")
handle.write(header)
result = compute()      # if this raises, the file is never closed
handle.write(result)
handle.close()
```

The `with` statement makes the release unconditional. Two ways to build one.

**Generator form**, which is the shorter and covers most cases:

```python
@contextlib.contextmanager
def timed(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"  [timed] {label}: {(time.perf_counter() - start) * 1e3:.3f} ms")
```

Everything before `yield` is `__enter__`; everything after is `__exit__`. The
`try/finally` is what makes the timing happen even when the block raises — which
is exactly what you want when the point is to find out how long the failure took.

**Class form**, which is longer and more capable:

```python
class Timed:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"  [Timed] {self.label}: ...")
        return False
```

```text
  [timed] sum of 10^6 squares (function form): 23.272 ms
  result = 333332833333500000
  [Timed] sum of 10^6 squares (class form): 23.820 ms
  result = 333332833333500000
```

The class form exists for two reasons. `__enter__` can return a *different* object
than the manager — a handle, a client, a prepared buffer — which is how `with
path.open() as handle:` gives you the handle and not the path. And `__exit__`
receives the exception information and can return `True` to **suppress** the
exception. `False` (the demo's choice, stated in a comment) lets it propagate.
Suppression is occasionally correct — a "retry once on this specific error"
manager, a "optional resource that may not exist" manager — and dangerous
everywhere else, because a suppressed exception is a failure that was not
reported.

## 2. Worked walkthrough: atomic writes

This is the context manager that matters most in a long job. The requirement is
simple to state: **either the whole result file exists and is complete, or the
previous version is untouched.**

```python
@contextlib.contextmanager
def atomic_write_text(path):
    tmp = Path(path).with_suffix(Path(path).suffix + ".tmp")
    handle = tmp.open("w", encoding="utf-8", newline="")
    try:
        yield handle
        handle.flush()
        os.fsync(handle.fileno())
    except Exception:
        handle.close()
        tmp.unlink(missing_ok=True)
        raise
    else:
        handle.close()
        os.replace(tmp, path)
```

Three mechanisms make it work.

**Write to a sibling temporary file.** Nothing is written to the real path until
the block completes, so the real path always holds a complete, self-consistent
result — either the previous one or the new one.

**`flush` then `os.fsync`.** `flush` pushes Python's buffer to the operating
system; `fsync` pushes the operating system's buffer to the disk. Without the
second, a power failure can leave the rename durable and the contents not — the
classic "zero-length file after a crash" bug.

**`os.replace` is atomic.** On POSIX and on Windows, replacing an existing path is
a single filesystem operation, so there is no instant at which the file is
half-updated.

The demo shows both outcomes:

```text
  clean exit  -> result.csv exists: True, temporary file left behind: False
  failed run  -> raised RuntimeError('simulated failure mid-write')
  published file still says: STA01,0.268390
  temporary file left behind: False
```

After the simulated mid-write failure, the published file still contains the
*previous* good content, and the temporary file has been cleaned up. Nothing about
the failure is silent: the `raise` re-raises the original exception, so the job
still fails loudly — it just fails without destroying anything.

This pattern is used by the module's complete program, and it is the single
highest-value context manager in scientific computing. A simulation that runs for
hours and writes partial output is a simulation you cannot trust.

## 3. Worked walkthrough: decorators and `functools.wraps`

A decorator is a function that takes a function and returns a replacement:

```python
def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"  [timing] {func.__name__}: {(time.perf_counter() - start) * 1e3:.4f} ms")
        return result
    return wrapper
```

Applied to the module's $b$-value estimator:

```text
  [timing] b_value_maxlik: 0.0163 ms
  synthetic sample : 2000 magnitudes, input b = 1.0, Mc = 0.0
  events >= Mc     : 214   (asymptotic standard error of b: 0.068)
  b-value estimate = 0.961524  (difference from input: 0.0385)
  __name__ preserved     : b_value_maxlik
  __doc__ preserved      : Aki-Utsu maximum-likelihood b-value (continuous form, uncorrected).
  __wrapped__ available  : True
```

**`@functools.wraps(func)` is not decoration.** Without it, the wrapped function
is called `wrapper`, has no docstring, and appears under the wrong name in every
traceback, every `help()` call, every log line and every test report. The demo
prints all three preserved attributes to make the point checkable. `__wrapped__` is
what makes a decorator transparent to introspection: tools can look through the
wrapper to the original.

**The wrapper takes `*args, **kwargs`.** A decorator must accept whatever the
decorated function accepts, which it cannot know in advance. This is the one place
where an unspecified signature is correct.

**Return the result.** A decorator that forgets `return result` returns `None`
from every call, and the resulting `TypeError: unsupported operand type(s) for *:
'NoneType'` will appear somewhere else entirely.

The $b$-value numbers in that output are a self-consistency check worth reading:
214 events above $M_c = 0$, a b-value estimate of 0.961524 against an input of
1.0, and an asymptotic standard error of $1/\sqrt{214} = 0.068$. The estimate is
0.57 standard errors from the input, which is a pass. **A method demonstration
that does not check its output against a known input is a method demonstration
that proves nothing** — this is the same discipline as the module's other
self-tests.

## 4. `functools.lru_cache`: memoisation and its one condition

```text
  calls made : 1000
  hits       : 996, misses: 4
  total time : 0.21 ms for 1000 calls
  t0(1000 m) : 666.666667 ms
```

A thousand calls to an expensive travel-time function with only four distinct
argument pairs: 996 cache hits, four misses, and a total cost of four expensive
evaluations rather than a thousand. The travel time itself —
$t_0 = 2z/v = 2\times1000/3000 = 0.6667$ s = 666.67 ms — is printed as a
correctness check, not as a performance claim.

**`lru_cache` is safe only for pure functions.** The same arguments must always
produce the same result. Cache a function that reads a file, consults the clock,
or depends on module state and you have built a bug generator: the second call
returns a stale answer, silently and permanently for the life of the process.

`maxsize=None` gives an unbounded cache; a finite `maxsize` bounds memory with an
LRU eviction policy. In a long-running process, unbounded is a leak. In a
within-run calculation over a small parameter set, unbounded is fine and much
faster. Choose deliberately.

The pattern is worth keeping in mind wherever a geophysical computation is
expensive and its parameters repeat: a travel-time table, a spherical-harmonic
basis evaluation, a gravity kernel between a source and receiver pair, an
instrument response at a set of frequencies. Memoisation turns "recompute for
every event" into "compute once per distinct key".

## 5. Worked walkthrough: retry and instrumentation

```text
  [retry] attempt 1/3 failed: error 0.500 exceeds tolerance 0.300
  converged with error 0.250 after 2 attempts
  impedance called 4 times
  impedance still named impedance
```

**A decorator factory** is a decorator that takes arguments, so it is written as a
function returning a decorator: `@retry(attempts=3)`. The extra nesting is
unavoidable and is the reason decorator factories read oddly the first time.

The retry decorator catches one specific exception type (`ValueError` here),
retries a bounded number of times, and then re-raises the last exception. Three
properties make it safe rather than merely convenient: it is bounded, it re-raises
rather than returning a default (a returned default after a failure is lesson
[07](./07-errors-and-debugging.md)'s silent wrongness), and it logs each attempt so
that a job that succeeds on attempt three is visibly different from one that
succeeds immediately. Numerical iterations that can stall — a solver, a network
fetch, a file lock — are the legitimate use.

**Instrumentation decorators attach state to the wrapper.** `wrapper.calls = 0`
and `wrapper.calls += 1` count invocations; because the state is on the wrapper
and not on the module, two functions decorated with `count_calls` keep separate
counts. This is the sanctioned alternative to a module global (lesson
[04](./04-functions-modules.md) §3).

## 6. Worked walkthrough: composition order

```text
  calling slow_square(3) three times, decorated as:
    @timing
    @lru_cache(maxsize=None)
  [timing] slow_square: 0.0004 ms
  [timing] slow_square: 0.0000 ms
  [timing] slow_square: 0.0001 ms
```

Stacked decorators apply bottom-up at definition time, so `slow_square` is first
wrapped in `lru_cache`, then the result is wrapped in `timing`. At call time the
*outermost* wrapper runs first, which means `timing` measures every call —
including the cache hits at microseconds — while `lru_cache` short-circuits the
body.

Swap the two lines and the meaning changes: with `@lru_cache` outermost, the
cache would be consulted before `timing` ran, and only the four misses would be
timed. **Both orders are legitimate; they answer different questions.** The first
answer is "what does a caller experience?"; the second is "what does the
computation cost?". Being unable to say which one you wrote is the actual defect,
and it is why the demo prints the decorator order as part of its output.

## 7. Assembling the complete program

Everything in this module is now in place, and
[`code/catalog_report.py`](./code/catalog_report.py) is where it comes together:

| Lesson | Contribution to the complete program |
|---|---|
| 02 | `float64` arithmetic, and a `b`-value estimator whose precision is stated |
| 03 | The Monte-Carlo loop, with a bounded iteration count |
| 04 | `geophys_core`, imported: `sphere_mass`, `haversine_km`, `b_value_maxlik`, `mean` |
| 05 | `stder`-style reductions over lists, and the `depth_bins` histogram |
| 06 | `csv.DictReader`, an explicit encoding, `newline=""`, and a skipped comment line |
| 07 | `ValueError` on an empty catalogue, and a self-check with `assert` |
| 08 | No class where none is needed: tuples and dicts, with one `atomic_write_text` class |
| 09 | `iter_catalogue`, the streaming reader that makes the pass memory-bounded |
| 10 | The `report_step` timing decorator and the atomic write context manager |

Run it and the report is the module's deliverable:

```text
SYNTHETIC earthquake-catalogue report
========================================================================
generator seed       : 20261014
events generated     : 5,000
magnitude law        : Gutenberg-Richter, input b = 1.0
minimum magnitude    : -1.0
reference site       : Zurich (nominal) (47.3769 N, 8.5417 E)
data status          : SYNTHETIC - no real catalogue is used

events read          : 5,000
magnitude range      : -1.000 to 4.220
mean depth           : 30.19 km
mean epicentral distance from Zurich (nominal): 241.5 km
farthest event       : 449.8 km
events within 100 km : 378 (7.6 %)

Magnitude-frequency statistics (Aki-Utsu maximum likelihood)
     Mc   N >= Mc    b estimate   b/sqrt(N)
    0.0       450        0.9968      0.0470
    1.0        47        0.8828      0.1288
    2.0         6        too few events
    3.0         1        too few events

Monte-Carlo calibration of the estimator at Mc = 0
  replicas            : 100, each of 2,000 events
  mean estimate       : 1.0101  (input b = 1.0)
  scatter of estimates: 0.0683  vs  b/sqrt(2000) = 0.0224
  events above Mc=0   : about 200  ->  b/sqrt(N_above) = 0.0707
  The relevant sample size is the number of events ABOVE Mc, not the
  total: only about one event in ten clears Mc = 0 here, which is why
  the measured scatter matches the second line, not the first.
  standard error of the mean: 0.0068
  mean within 2 standard errors of the input: True
```

Then the last lines of the run:

```text
report written atomically to catalog_report.txt: 2,814 characters, verified by re-reading
scratch directory removed: True
```

(The character count moves by a few characters between runs, because the timing
block is part of the report; the verification is a character-for-character
comparison within a single run, which is the property that matters.)

Four things about that output are the module's actual conclusions.

**The program checks itself.** The report is read back and compared with what was
written, character for character, before the run is declared successful. A file
that exists is not the same as a file that is correct.

**The $b$-value is checked against truth.** The input $b$ is 1.0 by construction;
the maximum-likelihood estimate at $M_c = 0$ is 0.9968 with an asymptotic standard
error of 0.047 for 450 events, and the Monte-Carlo mean over 100 replicas is
1.0101. The estimator works, and the report says how precisely.

**The Monte-Carlo block corrects a plausible misreading, in the report itself.**
The scatter of the estimates is 0.0683, which looks far too large against
$b/\sqrt{2000} = 0.0224$. The explanation is on the next line: only about one
event in ten clears $M_c = 0$, and $b/\sqrt{200} = 0.0707$ matches the measured
scatter. **The relevant sample size is the number of events above the threshold,
not the number of events.**

**The limits are stated in the output, not hidden in a footnote.** The synthetic
data status, the spherical-Earth distance approximation, the $dM/2$ correction
that a discrete catalogue would require, and the fact that the depth distribution
is a property of the generator rather than of the Earth, are all printed with the
numbers they qualify.

## 8. Assumptions and limits

1. **`os.replace` is atomic, but only within one filesystem.** Writing a temporary
   file on a different mount and replacing across the boundary fails; keep the
   temporary file as a sibling of the target, as the demo does.
2. **`fsync` is not free.** On a spinning disk it costs milliseconds. For a
   per-station output stream it is prohibitive; for a result file written once per
   run it is exactly the right level of care.
3. **The timing numbers are anecdotal.** A single run of a 20 ms block on a shared
   machine is an illustration. The demo's timing decorator prints one number per
   call, and one number is not a benchmark.
4. **`lru_cache` requires purity and hashable arguments.** A list argument is
   unhashable; a mutated argument is a stale cache entry. Both are silent.
5. **Decorators obscure signatures unless you keep `functools.wraps`.** Even with
   it, a stack of decorators changes the callable's type in ways that some
   introspection tools cannot see through.
6. **Suppressing an exception in `__exit__` is a decision about the physics as
   well as the code.** A suppressed error is a result computed on incomplete data;
   if you suppress, log it.
7. **The complete program's data are synthetic** (seeded, labelled in the file
   header and in the report), and its "Zurich" coordinates are nominal, used to
   make distances meaningful rather than to make a geographic claim.

## 9. Python demonstration

```bash
cd 03-scientific-computing/01-python-fundamentals/code
python3 context_decorators_demo.py      # sections 1-6 of this lesson
python3 catalog_report.py               # the complete program
```

The first script writes a temporary directory, provokes a mid-write failure on
purpose, and removes the directory on exit. The second writes its report
atomically, reads it back, verifies it and removes its scratch directory. Neither
leaves anything behind, which is itself the lesson.

## 10. Common mistakes

1. **Forgetting `return result` in a decorator.** Returns `None` and fails
   elsewhere.
2. **Forgetting `functools.wraps`.** Every traceback and docstring lies.
3. **Memoising an impure function.** Silent, permanent staleness.
4. **Writing a result file in place.** A crash leaves a truncated result that looks
   like a result.
5. **`flush` without `os.fsync`.** The rename is durable and the contents are not.
6. **`__exit__` returning `True` by accident.** An exception disappears.
7. **A context manager that swallows its own cleanup error.** The `finally` path
   must not raise over the original exception.
8. **Decorators for control flow.** A decorator that changes *what* a function
   computes is hard to see at the call site; decorators should add bookkeeping,
   not behaviour.
9. **Stacking decorators without knowing the order.** §6.
10. **Timing with one measurement.** Report the spread or repeat the run.

## 11. Real-world applications

- **Reproducible simulation jobs.** Atomic writes plus a timing decorator plus a
  verified read-back is the minimum viable result-management pattern for a
  multi-hour run, and it is what module
  [19 Numerical Modelling and HPC](../../19-numerical-modeling-hpc/README.md)
  assumes.
- **Data processing pipelines.** Every stage writes to a temporary location and
  publishes atomically; the alternative is a pipeline that cannot be restarted
  after a failure without manual cleanup.
- **Caching expensive kernels.** Travel-time tables, spherical-harmonic
  evaluations, gravity or magnetic kernel matrices and instrument responses are
  all recomputed far too often without memoisation.
- **Instrumentation in shared code.** Timers, counters and loggers applied as
  decorators keep the measurement out of the algorithm, so the algorithm remains
  testable in isolation — the discipline of module
  [03-13](../13-testing-profiling-packaging/README.md).
- **Journal-facing reproducibility.** A script that runs from raw input to a
  verified output file, with pinned dependencies and no manual steps, is what the
  [22 Data Engineering and Reproducibility](../../22-data-engineering-reproducibility/README.md)
  folder formalises.

## 12. Further reading

- NumPy — [numpy.org](https://numpy.org): the `with np.errstate(...)` context
  manager, which controls floating-point error handling around a block — the same
  pattern applied to numerical warnings.
- SciPy — [scipy.org](https://scipy.org): decorators and context managers used to
  control stochastic and performance behaviour in a large scientific library.
- ObsPy — [docs.obspy.org](https://docs.obspy.org): `read()` used as a context
  manager, and the resource discipline that makes waveform handling safe.
- NOAA National Centers for Environmental Information — [www.ncei.noaa.gov](https://www.ncei.noaa.gov):
  long-archived data whose reproducibility depends on the kind of verified,
  atomic output practice described here.

## 13. Related lessons

- [03-01-04 Functions, Scope, Modules and Packages](./04-functions-modules.md) —
  functions as first-class objects, which is what a decorator requires.
- [03-01-07 Exceptions, Assertions and Systematic Debugging](./07-errors-and-debugging.md)
  — `finally`, re-raising, and why suppression is dangerous.
- [03-01-09 Iterators, Generators and Lazy Evaluation for Large Data](./09-iterators-generators.md)
  — `@contextmanager` is built from a generator, and generators need resource
  discipline.
- [03-01-06 Files, Text I/O and Data Encodings](./06-files-and-io.md) — the file
  whose write must be made atomic.
- [03-13 Testing, Profiling and Packaging](../13-testing-profiling-packaging/README.md)
  — the natural home for decorators and context managers at scale.

## 14. Exercises

[`exercises/10-context-managers-decorators-exercises.md`](./exercises/10-context-managers-decorators-exercises.md) —
eight problems, ★ to ★★★. Problem ★★4 requires the atomic-write behaviour;
problem ★★★7 asks you to write a decorator that logs the arguments and result of
any function while preserving its signature, and to say what it must do when the
function raises.

## 15. Self-assessment checklist

- [ ] I can write a context manager with `@contextmanager` and say which part is
      which dunder method.
- [ ] I can explain what a class-based `__exit__` returning `True` does.
- [ ] I can write an atomic-write context manager and explain the roles of the
      temporary file, `fsync` and `os.replace`.
- [ ] I can write a decorator with `functools.wraps` and say why `wraps` matters.
- [ ] I can state the one condition under which `lru_cache` is safe.
- [ ] I can predict the behaviour of two stacked decorators in either order.
- [ ] I have run `catalog_report.py` and can name which lesson contributed each
      part of it.
- [ ] I can explain why the report's Monte-Carlo scatter matches
      $b/\sqrt{N_\text{above}}$ rather than $b/\sqrt{N_\text{total}}$.
