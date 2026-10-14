"""Context managers, decorators and a few functional idioms.

Run:  python3 context_decorators_demo.py
Requires: Python standard library only.

Companion to lesson 03-01-10.  Two mechanisms, one theme: wrap a piece of work
so that the *bookkeeping* (close the file, time the call, restore the state) is
written once and cannot be forgotten.

Demonstrates:

1. A @contextmanager that times a block, and the same thing as a class.
2. An atomic-write context manager: a real scientific safety pattern.
3. A @timing decorator, and why functools.wraps matters.
4. @lru_cache memoisation on an expensive geophysical function.
5. A @retry decorator and a @count_calls decorator.
6. Composition: two decorators stacked, and the order they run in.
"""

import contextlib
import functools
import math
import os
import random
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# 1. Timing, two ways
# --------------------------------------------------------------------------

@contextlib.contextmanager
def timed(label):
    """Time the block and print the elapsed wall-clock seconds."""
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"  [timed] {label}: {elapsed * 1e3:.3f} ms")


class Timed:
    """The same job as a class: __enter__ returns, __exit__ cleans up."""

    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start
        print(f"  [Timed] {self.label}: {elapsed * 1e3:.3f} ms")
        return False        # False: do not swallow an exception


def part1_timing():
    section("1. Timing a block: generator-based and class-based")
    with timed("sum of 10^6 squares (function form)"):
        total = sum(i * i for i in range(1_000_000))
    print(f"  result = {total}")

    with Timed("sum of 10^6 squares (class form)"):
        total = sum(i * i for i in range(1_000_000))
    print(f"  result = {total}")
    print()
    print("  @contextmanager turns a generator with one yield into a context")
    print("  manager; the code before yield is __enter__, the code after is")
    print("  __exit__.  The class form is more verbose and is what you need if")
    print("  __exit__ must decide whether to suppress an exception.")


# --------------------------------------------------------------------------
# 2. Atomic write: a real scientific safety pattern
# --------------------------------------------------------------------------

@contextlib.contextmanager
def atomic_write_text(path):
    """Yield a writable handle; publish the file only on clean exit.

    The data goes to a sibling '.tmp' file and is moved into place with
    os.replace, which is atomic on POSIX and on Windows.  A crash halfway
    through therefore leaves the previous good file untouched - the difference
    between losing one run and losing a week of them.
    """
    path = Path(path)
    tmp = path.with_suffix(path.suffix + ".tmp")
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


def part2_atomic():
    section("2. Atomic write: publish a result only if the whole run succeeded")
    target = HERE / "_scratch_atomic" / "result.csv"
    target.parent.mkdir(parents=True, exist_ok=True)

    with atomic_write_text(target) as handle:
        handle.write("station,anomaly_mgal\n")
        handle.write("STA01,0.268390\n")
    print(f"  clean exit  -> {target.name} exists: {target.exists()},"
          f" temporary file left behind:"
          f" {target.with_suffix(target.suffix + '.tmp').exists()}")

    try:
        with atomic_write_text(target) as handle:
            handle.write("station,anomaly_mgal\n")
            raise RuntimeError("simulated failure mid-write")
    except RuntimeError as exc:
        print(f"  failed run  -> raised {exc!r}")
    print(f"  published file still says: {target.read_text().strip().splitlines()[-1]}")
    print(f"  temporary file left behind:"
          f" {target.with_suffix(target.suffix + '.tmp').exists()}")
    print()
    print("  The failed run could not corrupt the good result.  This is the")
    print("  single most valuable context manager in a long simulation job.")


# --------------------------------------------------------------------------
# 3, 4, 5. Decorators
# --------------------------------------------------------------------------

def timing(func):
    """Decorator: print how long the wrapped call took."""

    @functools.wraps(func)      # copies __name__, __doc__, __wrapped__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [timing] {func.__name__}: {elapsed * 1e3:.4f} ms")
        return result

    return wrapper


def count_calls(func):
    """Decorator: record how many times the function has been called."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def retry(attempts=3, delay_s=0.0):
    """Decorator factory: retry a flaky call, then re-raise."""
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except ValueError as exc:
                    last = exc
                    print(f"  [retry] attempt {attempt}/{attempts} failed: {exc}")
                    if delay_s:
                        time.sleep(delay_s)
            raise last
        return wrapper
    return decorate


def part3_decorator_basics():
    section("3. A decorator is a function that returns a wrapper")

    @timing
    def b_value_maxlik(magnitudes, mc):
        """Aki-Utsu maximum-likelihood b-value (continuous form, uncorrected)."""
        selected = [m for m in magnitudes if m >= mc]
        return math.log10(math.e) / (sum(selected) / len(selected) - mc)

    # SYNTHETIC magnitudes drawn from a Gutenberg-Richter distribution with a
    # known input b = 1.0, so the estimator can be checked against truth.
    b_input = 1.0
    rng = random.Random(20261014)
    magnitudes = [-1.0 - math.log10(rng.random()) / b_input for _ in range(2000)]
    mc = 0.0
    value = b_value_maxlik(magnitudes, mc)
    n_above = sum(1 for m in magnitudes if m >= mc)
    print(f"  synthetic sample : {len(magnitudes)} magnitudes, input b = {b_input}, Mc = {mc}")
    print(f"  events >= Mc     : {n_above}"
          f"   (asymptotic standard error of b: {b_input / math.sqrt(n_above):.3f})")
    print(f"  b-value estimate = {value:.6f}"
          f"  (difference from input: {abs(value - b_input):.4f})")
    print(f"  __name__ preserved     : {b_value_maxlik.__name__}")
    print(f"  __doc__ preserved      : {b_value_maxlik.__doc__}")
    print(f"  __wrapped__ available  : {hasattr(b_value_maxlik, '__wrapped__')}")
    print()
    print("  Without functools.wraps the wrapped function is called 'wrapper',")
    print("  its docstring is gone, and every traceback and help() call lies")
    print("  about what it is.  Always use wraps.")


def part4_cache():
    section("4. @lru_cache: memoising an expensive pure function")

    @functools.lru_cache(maxsize=None)
    def travel_time(depth_m, velocity):
        """Two-way travel time by an explicit (pretend-expensive) loop."""
        # A deterministic, deliberately wasteful integration so that caching
        # has something to save.  2000 steps stand in for a ray-tracing loop.
        steps = 2000
        dz = depth_m / steps
        total = 0.0
        for _ in range(steps):
            total += dz / velocity
        return 2.0 * total

    depths = [500.0, 1000.0, 1500.0, 2000.0] * 250
    start = time.perf_counter()
    for depth in depths:
        travel_time(depth, 3000.0)
    elapsed = time.perf_counter() - start
    info = travel_time.cache_info()
    print(f"  calls made : {len(depths)}")
    print(f"  hits       : {info.hits}, misses: {info.misses}")
    print(f"  total time : {elapsed * 1e3:.2f} ms for {len(depths)} calls")
    print(f"  t0(1000 m) : {travel_time(1000.0, 3000.0) * 1e3:.6f} ms")
    print()
    print("  Memoisation is only valid for a PURE function: the same arguments")
    print("  must always give the same answer.  Cache a function that reads a")
    print("  file or uses the clock and you have built a bug generator.")


def part5_retry_count():
    section("5. @retry and @count_calls")

    attempts = {"n": 0}

    @retry(attempts=3)
    def flaky_convergence(tolerance):
        attempts["n"] += 1
        error = 0.5 / attempts["n"]          # shrinks with every attempt
        if error > tolerance:
            raise ValueError(f"error {error:.3f} exceeds tolerance {tolerance:.3f}")
        return error

    result = flaky_convergence(0.3)
    print(f"  converged with error {result:.3f} after {attempts['n']} attempts")

    @count_calls
    def impedance(rho, vp):
        return rho * vp

    for _ in range(4):
        impedance(2670.0, 3000.0)
    print(f"  impedance called {impedance.calls} times")
    print(f"  impedance still named {impedance.__name__}")
    print()
    print("  A decorator can attach state to the wrapper (here, .calls).  That")
    print("  is legitimate for instrumentation and is why the state lives on the")
    print("  wrapper rather than in a module global.")


def part6_composition():
    section("6. Stacking decorators: order is not decoration")

    @timing
    @functools.lru_cache(maxsize=None)
    def slow_square(x):
        return x * x

    print("  calling slow_square(3) three times, decorated as:")
    print("    @timing")
    print("    @lru_cache(maxsize=None)")
    for _ in range(3):
        slow_square(3)
    print()
    print("  @timing is outermost, so it times every call - including the cache")
    print("  hits, which cost microseconds.  Swap the order and only the misses")
    print("  are timed, because lru_cache would short-circuit before timing.")
    print("  The two orders answer two different questions about performance,")
    print("  and neither is wrong; being unable to say which you wrote is.")


def cleanup():
    import shutil
    shutil.rmtree(HERE / "_scratch_atomic", ignore_errors=True)


if __name__ == "__main__":
    part1_timing()
    part2_atomic()
    part3_decorator_basics()
    part4_cache()
    part5_retry_count()
    part6_composition()
    cleanup()
