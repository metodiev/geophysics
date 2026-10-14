# Solutions — 03-01-10 Context Managers, Decorators and Functional Idioms

> **Read this after attempting the exercises, not before.** Numbers attributed to
> a demo are its actual printed output.

---

## ★1 — Context managers for resources

| Resource | Form | `__exit__` must |
|---|---|---|
| (a) an open file | `with path.open("w", encoding="utf-8", newline="") as handle` | close it, and in a `finally`-style path so a raised exception still closes |
| (b) a lock | `with lock:` | release it, exactly once, whether or not the block raised |
| (c) a temporary directory | `@contextmanager` around `tempfile.TemporaryDirectory()` (or `contextlib.ExitStack`) | remove the tree even on failure |
| (d) an atomic result file | a custom `atomic_write_text` manager | close, `fsync`, then `os.replace` on success; delete the temporary file and re-raise on failure |
| (e) a thread-count setting | a class-based manager | restore the previous value whether or not the block raised, and not swallow the exception |

Every row has the same shape: **acquire, run the block, release unconditionally.**
That is why one language feature covers all five.

---

## ★2 — Two-sentence explanations

**(a)** `flush` pushes Python's user-space buffer into the operating system, and
`os.fsync` pushes the operating system's buffer to the storage device; only the
second survives a power failure. It matters because a rename can be durable while
the *contents* it points at are still in a cache, which is how a "zero-length file
after a crash" happens.

**(b)** `os.replace` is a single atomic filesystem operation, so a reader sees
either the old file or the new one and never a partial one; writing in place
truncates the target first, so a crash leaves a file that exists and is wrong. It
matters most for long jobs, where "exists and is wrong" is more dangerous than
"does not exist".

**(c)** `functools.wraps` copies `__name__`, `__qualname__`, `__doc__`,
`__module__` and `__dict__` from the wrapped function onto the wrapper and sets
`__wrapped__`; without it every traceback, docstring, help page and test report
names the wrapper instead of the function. It matters because a test runner that
discovers tests by name would otherwise find one function called `wrapper`
repeatedly.

**(d)** `lru_cache` on a function that reads a file memoises the *first* file
contents for the life of the process, so a later edit to the file has no effect and
the function silently returns stale data. The fix is either not to cache it, or to
key the cache on a value that changes when the file changes (its mtime or hash).

---

## ★3 — What `True` from `__exit__` means

Returning a truthy value from `__exit__` **suppresses the exception**: execution
resumes after the `with` block as if nothing had happened.

**Legitimate use:** a manager for an *optional* resource whose absence is expected
and handled — for example, a "best-effort" cache directory that may not be
writable, where the block's purpose is an optimisation and its failure is
acceptable while being logged.

**Illegitimate use:** suppressing an error to "keep the pipeline running" when the
data are the product. A suppressed parse failure, a suppressed non-convergence or a
suppressed write error converts a loud failure into a quiet wrong answer — the exact
failure mode lesson 07 is about. If you suppress, you must log, and you must be able
to say why the result remains valid.

---

## ★★4 — The demo's outputs

**(a)**

```text
  [timed] sum of 10^6 squares (function form): 23.272 ms
  result = 333332833333500000
  [Timed] sum of 10^6 squares (class form): 23.820 ms
  result = 333332833333500000
```

The two timings agree to within 2.4 per cent, which is the expected agreement
between two ways of writing the same manager; note that both are single runs and
the difference is within run-to-run noise.

**(b)**

```text
  clean exit  -> result.csv exists: True, temporary file left behind: False
  failed run  -> raised RuntimeError('simulated failure mid-write')
  published file still says: STA01,0.268390
  temporary file left behind: False
```

**(c)**

```text
  __name__ preserved     : b_value_maxlik
  __doc__ preserved      : Aki-Utsu maximum-likelihood b-value (continuous form, uncorrected).
  __wrapped__ available  : True
```

**(d)** `calls made : 1000`, `hits : 996, misses: 4`,
`total time : 0.21 ms for 1000 calls`, `t0(1000 m) : 666.666667 ms`.

**After the failure:** `result.csv` contains the *previous* good content, namely

```text
station,anomaly_mgal
STA01,0.268390
```

and the partially written data were in the sibling file `result.csv.tmp`, which
the `except` branch deleted. Nothing partial was published, and the directory
contains one file rather than two.

---

## ★★5 — The cache

**(a)** $t_0 = 2z/v = 2 \times 1000/3000 = 0.6666667$ s. The printed number is in
**milliseconds**: $0.6666667\ \text{s} = 666.6667$ ms. The trailing
`666.666667` is the infinite decimal $2/3$ truncated to nine places, so quoting more
digits of it would be false precision.

**(b)** The call sequence is `[500, 1000, 1500, 2000] * 250`, so exactly four
distinct argument pairs appear. The first occurrence of each is a miss and the
remaining 996 calls are hits, giving 996 + 4 = 1 000 calls.

**(c)** Two ways it becomes a bug:

| Failure | Fix |
|---|---|
| The function is not pure — it reads a file, a clock or a remote service — so a changed input is not seen | Remove the cache, or key it on the input's identity (path plus mtime, or a hash) |
| The argument is a mutable object (a list of magnitudes) that the caller later mutates, so the cache key is unchanged but the meaning has changed | Make the cached function's arguments immutable (a `tuple`), and document that the caller must not mutate them |

A third, subtler one: an unbounded cache (`maxsize=None`) in a long-running process
keyed on a continuous parameter (a float depth) grows without limit and is a memory
leak.

**(d)** Each miss performs a 2 000-step Python loop. At roughly 30–40 ns per
iteration plus loop overhead, one miss costs of the order of 0.1–0.2 ms; four misses
are therefore about 0.4–0.8 ms against a measured total of 0.21 ms — the measured
figure is at the fast end of that band, which is the correct way to report it: an
estimate with a stated spread, checked against a measurement, not a fabricated
constant. Had the cache not existed, 1 000 misses would have cost roughly
$1\,000 \times 0.15\ \text{ms} = 150$ ms, so the cache saved about two orders of
magnitude.

---

## ★★6 — Retry

**(a)**

```python
def retry(attempts=3, delay_s=0.0, catch=(ValueError, OSError)):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except catch as exc:
                    last = exc
                    if delay_s:
                        time.sleep(delay_s)
            raise last
        return wrapper
    return decorate
```

Catching `Exception` instead would also catch programming errors — a `TypeError`
from a wrong argument, an `AttributeError` from a typo, a `KeyError` from a missing
configuration entry — and retrying those three times just delays the same failure
and triples the log noise, while *hiding* the fact that the first failure was a bug
rather than a transient condition. A retry is only meaningful for a failure that
might not recur: a timeout, a locked file, a not-yet-converged iteration.

**(b)**

```python
def wrapper(*args, **kwargs):
    last = None
    wrapper.attempts = 0
    try:
        for attempt in range(1, attempts + 1):
            wrapper.attempts = attempt
            try:
                return func(*args, **kwargs)
            except catch as exc:
                last = exc
                if delay_s:
                    time.sleep(delay_s)
        raise last
    finally:
        logger.info("%s: %d attempt(s)", func.__name__, wrapper.attempts)
```

The `finally` guarantees the count is recorded on the success path, the
re-raise path and even if a *different* exception type escapes mid-loop.

**(c)** When all attempts fail the decorator must **re-raise** the last exception.
Returning the last value would be catastrophic: the caller receives a number (or a
partially updated object) that looks like a result, with no indication that the
operation did not succeed. This is lesson 07's silent-wrongness pattern with a
retry wrapper around it, and it is the reason a retry decorator must never have
a "default" return value.

---

## ★★★7 — A logging decorator

```python
import functools
import logging
import time

def logged(logger):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            logger.info("%s called args=%r kwargs=%r", func.__name__, args, kwargs)
            try:
                result = func(*args, **kwargs)
            except Exception:
                logger.exception("%s raised after %.3f ms",
                                 func.__name__, (time.perf_counter() - start) * 1e3)
                raise
            logger.info("%s returned %r after %.3f ms",
                        func.__name__, result, (time.perf_counter() - start) * 1e3)
            return result
        return wrapper
    return decorate
```

**(b)** Two log records:

```text
INFO  b_value_maxlik called args=([1.0, 2.0, 3.0], 1.0) kwargs={}
INFO  b_value_maxlik returned 0.7213475204444817 after 0.004 ms
```

```text
INFO  parse_magnitude called args=('oops',) kwargs={}
ERROR parse_magnitude raised after 0.002 ms
Traceback (most recent call last):
  ...                     # (intermediate frames omitted)
ValueError: could not convert string to float: 'oops'
```

Note `logger.exception` inside the `except` block, which records the traceback —
logging the message alone would lose the call path that lesson 07 shows is the part
worth reading.

**(c)** `functools.wraps` copies `__module__`, `__name__`, `__qualname__`,
`__doc__`, `__dict__` (updated, not replaced) and sets `__wrapped__`; it does *not*
copy the function's **signature** by itself, although `inspect.signature` follows
`__wrapped__` to recover it, so most introspection works. For a test runner that
discovers tests by name and calls them, `__name__` and `__qualname__` are the ones
that matter — without them a decorated test is reported as `wrapper`, and two
decorated tests collide under the same name. A logging decorator preserves the
signature because `wraps` sets `__wrapped__`.

**(d)** A logging decorator must not *alter* the return value — it may not drop it,
convert it, or return a log record instead. The bug when `return result` is omitted
is that every call returns `None`, and the failure appears not at the decorator but
wherever the caller first does arithmetic with the result, as
`TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'`. That is the
single most common decorator bug, and it is why the `return result` line belongs in
every decorator template you write.

---

## ★★★8 — A re-runnable pipeline stage

```python
import hashlib, json, os
from pathlib import Path

VERSION = "1.0.0"

def sha256_of(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

@report_step
def process(input_path, output_path, params):
    output_path = Path(output_path)
    sidecar = output_path.with_suffix(output_path.suffix + ".done.json")
    signature = {"input_sha256": sha256_of(input_path),
                 "params": params, "version": VERSION}
    if sidecar.exists() and json.loads(sidecar.read_text()) == signature:
        return "skipped"
    with atomic_write_text(output_path) as handle:
        handle.write(run_algorithm(input_path, params))
    with atomic_write_text(sidecar) as handle:
        json.dump(signature, handle, sort_keys=True)
    return "computed"
```

**(b)** First run prints `computed`; second run — with the same input, the same
params and the same `VERSION` — prints `skipped` without writing either file. Prove
it by touching the output's mtime (it does not change on the second run) and by
timing the two runs: the skip returns in microseconds, not in the algorithm's
seconds.

**(c)** Three ways the skip test can be wrong:

| Wrong skip | Why | Safe version |
|---|---|---|
| The input changed but has the same *name* | Content is not compared | Hash the content, as above |
| The *code* changed but the hash and params did not | A bug fix leaves the signature identical | Include a version string that the developer bumps; a hash of the source file is stronger but can be brittle |
| The output was truncated or corrupted but the sidecar survived | The sidecar is evidence of intent, not of the output | Record the output's own size and hash in the sidecar and verify it before skipping |

The third is the subtle one: **a sidecar is a claim, and a claim must be checked.**

**(d)** The sidecar must be written *after* the output, because it is the marker
that says "the output is complete". If it were written first, a crash between the
two writes would leave a signature claiming a result that does not exist, and the
next run would skip the computation and report success while the output file was
absent or stale. Writing the evidence last is the same ordering rule as the atomic
write itself: publish the claim only after the fact it describes is durable.

---

## ★★★9 — Cache invalidation

**(a)** `lru_cache` keys on the *arguments*: `(station, network, time)`. The
function's result, however, depends on remote state — the station's metadata — that
is not among the arguments. Until that metadata changes, the mapping from arguments
to result is stable and the cache is correct; the moment the service corrects the
metadata, the same key should map to a different value, and the cache returns the
old one. **The function is impure with respect to state that is invisible in its
signature**, which is exactly the condition §4 of the lesson warns about.

**(b)** Two designs:

| Design | Mechanism | Trade-off |
|---|---|---|
| Version key | Add a `metadata_version` argument obtained cheaply from the service (a shortened digest endpoint), and include it in the cache key; the decorator is applied to an inner function | Requires the service to expose a version; when the version changes, the whole cache for that station is invalidated, and every *other* station's entries survive unnecessarily |
| Validity interval | Do not use `lru_cache`; write a small cache keyed by the arguments with an expiry timestamp, and re-fetch when expired | Bounds staleness by the interval rather than by correctness; costs one clock comparison per call and a policy decision about the interval |

A third, often best: cache within a single *run* (a fresh cache per process or per
analysis), which bounds staleness to the duration of the computation and needs no
version machinery at all.

**(c)** The version design trades a dependency on the service's ability to report a
version, and it invalidates in bursts. The interval design trades correctness for a
bound: a response can be up to one interval stale, which is acceptable for a
slowly-changing metadata catalogue and unacceptable for, say, a real-time alerting
service.

**(d)** `b_value_maxlik(magnitudes, mc)` is a **pure function of its arguments**: it
reads no files, consults no clock, and depends on no module state that changes. So
caching it is safe with respect to *correctness* — but the key is `magnitudes`, a
list, which is unhashable, so `lru_cache` will raise
`TypeError: unhashable type: 'list'` unless the caller passes a tuple. And the key
is the *whole list*, so the cache only helps if the identical list is passed
repeatedly — for example in a Monte-Carlo loop that reuses a fixed synthetic
catalogue. Where it genuinely helps is on a wrapper that takes
`(sorted_magnitudes_tuple, mc)` and is called thousands of times with a handful of
distinct `mc` values; that is precisely the pattern in
[`../code/catalog_report.py`](../code/catalog_report.py), where `magnitude_frequency`
calls the estimator once per threshold on the same array.

---

## ★★★10 — Assembling the module

Running `python3 catalog_report.py` produces the report quoted in lesson 10 §7. Each
line's mechanism, by lesson:

| Report line | Lesson |
|---|---|
| `generator seed`, `events generated`, `magnitude law` | 08 (a record of parameters), 02 (reproducible floats) |
| `magnitude range`, `mean depth` | 03 (loops and accumulators), 05 (the reductions) |
| `mean epicentral distance`, `within 100 km` | 01 (the geometry), 04 (`haversine_km` from the module) |
| `Depth distribution` histogram | 05 (`list` of bins), 03 (binning with `//`) |
| `Magnitude-frequency statistics` | 04 (`b_value_maxlik`), 07 (the "too few events" guard) |
| `Monte-Carlo calibration` | 03 (bounded loop), 02 (float summation) |
| `b/sqrt(N_above)` note | 07 (stating the limit) and the physics of the estimator |
| `Timing` block | 10 (the `report_step` decorator) |
| `report written atomically` | 10 (the atomic-write context manager), 06 (encoding and newline) |

**(a)** A peak-memory decorator:

```python
def traced_memory(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        try:
            return func(*args, **kwargs)
        finally:
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print(f"  [memory] {func.__name__}: peak {peak / 1e6:.3f} MB")
    return wrapper
```

**(b)** A refusing context manager:

```python
@contextlib.contextmanager
def require_calibration(mean, target, sem, sigmas=3.0):
    if abs(mean - target) > sigmas * sem:
        raise RuntimeError(
            f"estimator calibration failed: |{mean:.4f} - {target}| > "
            f"{sigmas} x {sem:.4f}")
    yield
```

used as `with require_calibration(mc_mean, B_INPUT, sem):` around the atomic write,
so a mis-calibrated estimator cannot publish a report.

**(c)** The memory decorator is **instrumentation**: it observes the function from
outside and changes nothing about the result. It belongs in the reporting code as a
decorator, and it could be removed without changing any number in the report. The
calibration check is **logic**: it decides whether a result may be published, it can
abort the run, and removing it changes the deliverable. Therefore it belongs
*inside* `main()`, near the point where the decision is made, where a reader can see
that the run either produces a verified report or no report at all. Putting a
control decision inside a decorator hides it behind a name that reads like
bookkeeping, which is the failure mode §6 of the lesson describes from the other
direction: **decorators add bookkeeping; decisions live in the main flow.**
