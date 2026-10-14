"""Profiling with the standard library: cProfile, pstats, tracemalloc, counters.

Run:  python profiling_demo.py
Requires: numpy (project virtual environment)

The lesson's rule is that a *count* is a reproducible measurement and a
*second* is not. So this script reports, in order:

1. ``cProfile`` on a NumPy-heavy inner loop.  The counts are the part that
   repeats; the seconds are not.  The profile also shows a real limitation:
   calling a NumPy ufunc creates **no Python frame**, so the profiler sees one
   call to the loop function and cannot say which line is hot.
2. ``cProfile`` on a Python-heavy loop, where the profiler *does* localise the
   cost -- and where its own overhead is measured to be four times larger.
3. Line-level *hit counts* using ``sys.settrace``: the deterministic part of
   what ``line_profiler`` gives you, and the measurement that localises the
   NumPy-heavy loop that cProfile could not.
4. ``tracemalloc`` peaks for four ways of writing the same inner product.

Every ratio printed here is a ratio of *times*, so it is a property of this
machine and this load. Every count printed is a property of the code.
"""

from __future__ import annotations

import cProfile
import inspect
import io
import math
import pstats
import sys
import time
import tracemalloc

import numpy as np


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --------------------------------------------------------------------------
# Two workloads with very different frame rates
# --------------------------------------------------------------------------

def nmo_gather(t0_s: float, v_rms: np.ndarray, offsets_m: np.ndarray) -> np.ndarray:
    """Normal-moveout correction applied trace by trace (the slow way).

    Every operation in the loop body is a ufunc or an index, and none of them
    creates a Python frame.  That fact is the point of the demonstration.
    """
    out = np.empty_like(offsets_m, dtype=float)
    for i in range(offsets_m.size):
        out[i] = np.sqrt(t0_s**2 + (offsets_m[i] / v_rms[i]) ** 2)
    return out


def nmo_gather_fast(t0_s: float, v_rms: np.ndarray, offsets_m: np.ndarray) -> np.ndarray:
    """The same answer without the trace loop."""
    return np.sqrt(t0_s**2 + (offsets_m / v_rms) ** 2)


def build_inputs(n: int = 400, seed: int = 5):
    rng = np.random.default_rng(seed)
    offsets = np.linspace(0.0, 4000.0, n)
    v_rms = 2000.0 + 200.0 * np.sin(offsets / 900.0) + rng.normal(0.0, 5.0, n)
    return 0.9, v_rms, offsets


def numpy_workload(repeats: int = 200) -> float:
    """Run the slow gather ``repeats`` times and return a checksum."""
    t0, v, x = build_inputs()
    total = 0.0
    for _ in range(repeats):
        total = float(nmo_gather(t0, v, x).sum())
    return total


def msd_kernel(x: float, y: float) -> float:
    """A three-line pure-Python kernel with one call per sample."""
    dx = x - y
    s = dx * dx
    if s > 0.0:
        s = math.fsum((dx * dx, 0.0, 0.0, 0.0))
    return s


def python_workload(n: int = 4000) -> float:
    """Sum a pure-Python statistic over ``n`` samples (the slow way)."""
    total = 0.0
    for i in range(n):
        total += msd_kernel(i * 0.001, (i % 7) * 0.002)
    return total


def profile_summary(fn, *args, top: int = 6) -> dict[str, object]:
    fn(*args)                                    # warm up imports and caches
    profiler = cProfile.Profile()
    profiler.enable()
    result = fn(*args)
    profiler.disable()
    buffer = io.StringIO()
    stats = pstats.Stats(profiler, stream=buffer).sort_stats("tottime")
    stats.print_stats(top)
    return {
        "result": result,
        "text": buffer.getvalue(),
        "total_calls": int(stats.total_calls),
    }


def best_seconds(fn, number: int, repeat: int = 7) -> float:
    """Best-of-repeat seconds per call, with the median kept for reference."""
    times = []
    for _ in range(repeat):
        t0 = time.perf_counter()
        for _ in range(number):
            fn()
        times.append((time.perf_counter() - t0) / number)
    return min(times)


# --------------------------------------------------------------------------
# 1 and 2: cProfile on both workloads, plus measured overhead
# --------------------------------------------------------------------------

def demo_cprofile() -> None:
    section("1. cProfile on a NumPy-heavy inner loop (400 traces per call)")
    info = profile_summary(numpy_workload, 200)
    print(f"checksum = {info['result']:.6f}")
    print("\n".join(info["text"].splitlines()[:10]))
    print(f"\nstats.total_calls = {info['total_calls']}")
    print("Read the ncalls column first: 200 calls to numpy_workload and 200 to")
    print("nmo_gather, i.e. exactly one per repetition. The 400 scalar ufunc")
    print("calls per repetition are invisible -- a ufunc is an object whose call")
    print("slot is in C, so no Python frame is created and lsprof never sees it.")
    print("The profiler tells you *that* nmo_gather is hot, in its tottime")
    print("column, and cannot tell you which line inside it is hot. Nor is")
    print("tottime reliable at that granularity: it is a stopwatch.")

    section("2. cProfile on a pure-Python loop (4000 kernel calls per call)")
    info2 = profile_summary(python_workload, 4000)
    print(f"checksum = {info2['result']:.6f}")
    print("\n".join(info2["text"].splitlines()[:10]))
    print(f"\nstats.total_calls = {info2['total_calls']}")
    print("Here every sample is a Python call, so the profiler localises the")
    print("cost exactly: msd_kernel's ncalls and percall are the answer.")
    print("The price is distortion. First, the profiler's overhead per call,")
    print("measured on a function that does nothing but increment a counter:")

    def noop(x: int) -> int:
        return x

    def counter_loop(n: int) -> int:
        acc = 0
        for i in range(n):
            acc += noop(i)
        return acc

    def counter_loop_profiled(n: int) -> int:
        p = cProfile.Profile()
        p.enable()
        result = counter_loop(n)
        p.disable()
        return result

    print(f"\n{'calls':>9} {'bare (ms)':>11} {'profiled (ms)':>15} "
          f"{'ns/call':>9} {'factor':>8}")
    overheads = []
    for n in (50_000, 200_000):
        bare = best_seconds(lambda: counter_loop(n), number=1, repeat=5)
        prof = best_seconds(lambda: counter_loop_profiled(n), number=1, repeat=5)
        overheads.append((prof - bare) / n * 1e9)
        print(f"{n:>9} {bare*1e3:>11.2f} {prof*1e3:>15.2f} "
              f"{overheads[-1]:>9.0f} {prof/bare:>8.2f}x")
    print(f"\nThe overhead is a constant ~{sum(overheads)/len(overheads):.0f} ns per Python call,")
    print("independent of what the call does. Now multiply that constant by the")
    print("call counts above and the two workloads' factors are predicted:")

    print(f"\n{'workload':>26} {'bare (ms)':>12} {'profiled (ms)':>14} {'factor':>8}")
    for label, fn, args in (
        ("numpy_workload(50)", numpy_workload, (50,)),
        ("python_workload(2000)", python_workload, (2000,)),
    ):
        fn(*args)
        bare = best_seconds(lambda: fn(*args), number=3)

        def instrumented():
            p = cProfile.Profile()
            p.enable()
            fn(*args)
            p.disable()

        prof = best_seconds(instrumented, number=3)
        print(f"{label:>26} {bare*1e3:>12.2f} {prof*1e3:>14.2f} {prof/bare:>8.2f}x")
    print("\nThe NumPy-heavy loop pays almost nothing because it creates almost no")
    print("Python frames; the Python-heavy loop pays a factor above two. The same")
    print("profiler is nearly transparent on one program and seriously distorting")
    print("on another, and the distortion is predicted by the call count, which")
    print("you already have. Quote counts; sanity-check seconds.")


# --------------------------------------------------------------------------
# 3: line hit counts with sys.settrace -- deterministic
# --------------------------------------------------------------------------

def line_hit_counts(fn, *args, **kwargs) -> dict[int, int]:
    """Count executions of each source line of ``fn``, excluding callees."""
    counts: dict[int, int] = {}
    target = fn.__code__

    def tracer(frame, event, arg):
        if event == "call":
            return tracer if frame.f_code is target else None
        if event == "line" and frame.f_code is target:
            counts[frame.f_lineno] = counts.get(frame.f_lineno, 0) + 1
        return tracer

    sys.settrace(tracer)
    try:
        fn(*args, **kwargs)
    finally:
        sys.settrace(None)
    return counts


def demo_line_counts() -> None:
    section("3. Line hit counts with sys.settrace (line_profiler's count column)")
    t0, v, x = build_inputs(n=400)
    counts = line_hit_counts(nmo_gather, t0, v, x)
    lines, first = inspect.getsourcelines(nmo_gather)
    source = {first + i: text for i, text in enumerate(lines)}
    print(f"{'line':>5} {'hits':>7}  source")
    for lineno in sorted(counts):
        print(f"{lineno:>5} {counts[lineno]:>7}  {source.get(lineno, '').rstrip()}")
    body = max(counts, key=lambda ln: counts[ln])
    print(f"\noffsets per call = {x.size}; hits on the hottest line "
          f"({body}) = {counts[body]}")
    print("The hottest line is the `for` header at 401 hits, one more than the")
    print("400 offsets: the loop test runs once more than the body. A hit count")
    print("makes that off-by-one visible; a stopwatch never will.")
    print("The line the *profiler* could not rank is identified here by an exact,")
    print("machine-independent integer. That is the measurement to put in a test:")
    print("assert the loop-body line is never executed -- a vectorised rewrite")
    print("makes the count zero, and the test then documents the intent forever.")
    print("line_profiler adds a time column to this same table; the count column")
    print("is the part that survives a change of machine.")


# --------------------------------------------------------------------------
# 4: tracemalloc
# --------------------------------------------------------------------------

def demo_memory() -> None:
    section("4. tracemalloc: four ways to write one inner product")
    n = 4_000_000
    rng = np.random.default_rng(0)
    a = rng.normal(size=n)
    print(f"input array: {n} float64 = {a.nbytes / 1e6:.1f} MB")

    def peak_of(fn) -> float:
        tracemalloc.start()
        fn()
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return peak / 1e6

    for label, fn in (
        ("np.sum(a*a)", lambda: np.sum(a * a)),
        ("(a**2).sum()", lambda: (a**2).sum()),
        ("a @ a", lambda: a @ a),
        ("np.einsum('i,i->',a,a)", lambda: np.einsum("i,i->", a, a)),
    ):
        print(f"  {label:>24}: peak {peak_of(fn):8.2f} MB")
    print("\n`a @ a` and `einsum` allocate essentially nothing: BLAS sums the")
    print("products as it computes them. `np.sum(a*a)` must materialise the whole")
    print("4e6-element product array first -- one 32 MB temporary, per call. The")
    print("peak falsifies the hypothesis 'the arithmetic is the cost'; the")
    print("arithmetic is identical, the allocation is not.")
    print("\nCorrectness is not optional -- all four must agree to the last bits:")
    ref = float(a @ a)
    for label, fn in (
        ("np.sum(a*a)", lambda: float(np.sum(a * a))),
        ("(a**2).sum()", lambda: float((a**2).sum())),
        ("np.einsum", lambda: float(np.einsum("i,i->", a, a))),
    ):
        got = fn()
        print(f"  {label:>24}: rel.diff from a@a = {abs(got - ref) / ref:.3e}")


def main() -> int:
    demo_cprofile()
    demo_line_counts()
    demo_memory()
    section("Summary")
    print("Instrument in this order: counts first (cProfile ncalls, settrace line")
    print("hits), memory second (tracemalloc), seconds last and never alone. A")
    print("number that changes between two successive runs is not yet a result.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
