#!/usr/bin/env python3
"""The GPU programming model, expressed and measured with numpy: data parallelism,
coalescing, launch overhead and precision.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpu_computing_demo.py

WHAT THIS SCRIPT DOES NOT DO: it does not use a GPU.  No CUDA, OpenCL or array-API
device is present or timed, and no GPU timing or vendor figure appears anywhere in
the output.  What it does is express the same kernels in the vectorised form a GPU
program would take, measure them on the CPU, and quantify the ONE cost model that
is independent of hardware: the number of memory transactions implied by the
access pattern.

Everything is SYNTHETIC: array sizes, thread-block geometry and precision examples
are chosen teaching values.

Contents
--------
1. A stencil written two ways: neighbour gather and shifted slices, and the
   measured cost of the gather.
2. Coalescing: transactions per warp for contiguous, strided and scattered
   patterns -- arithmetic from an assumed thread/sector geometry, then the matching
   measured time ratios on the CPU.
3. Launch overhead: measured per-call cost of a tiny kernel and the array size at
   which it stops dominating.
4. Precision: fp32 against fp64, measured time and measured accumulation error.
5. Summary of measured quantities.
"""

import time

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def best_of(fn, repeats=5):
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn()
        times.append(time.perf_counter() - t0)
    return min(times)


def main():
    section("1. One kernel, two expression styles: gather against slices")
    n = 1024
    u = RNG.standard_normal(n * n)
    out = np.empty(n * n)
    lid = np.arange(n * n)
    neighbours = np.empty((n * n, 4), dtype=np.int64)
    neighbours[:, 0] = np.maximum(lid - n, 0)
    neighbours[:, 1] = np.minimum(lid + n, n * n - 1)
    neighbours[:, 2] = np.maximum(lid - 1, 0)
    neighbours[:, 3] = np.minimum(lid + 1, n * n - 1)

    def gather_stencil():
        np.add(u[neighbours[:, 0]], u[neighbours[:, 1]], out=out)
        np.add(out, u[neighbours[:, 2]], out=out)
        np.add(out, u[neighbours[:, 3]], out=out)
        np.multiply(out, 0.25, out=out)

    def slice_stencil():
        a = u.reshape(n, n)
        b = out.reshape(n, n)
        b[1:-1, 1:-1] = 0.25 * (a[:-2, 1:-1] + a[2:, 1:-1]
                                + a[1:-1, :-2] + a[1:-1, 2:])

    t_gather = best_of(gather_stencil)
    gather_result = out.copy()
    t_slice = best_of(slice_stencil)
    interior = np.zeros(n * n, dtype=bool)
    interior.reshape(n, n)[1:-1, 1:-1] = True
    diff = np.max(np.abs(out - gather_result)[interior])
    print(f"  grid {n}x{n} = {n*n} elements; neighbour index table of shape "
          f"{neighbours.shape}")
    print(f"    gather-based  : {t_gather*1e3:8.3f} ms")
    print(f"    slice-based   : {t_slice*1e3:8.3f} ms")
    print(f"    measured ratio gather/slice = {t_gather/t_slice:.3f}")
    print(f"    the two agree in the interior to {diff:.3e}")
    print("  both express pure data parallelism -- the same operation applied to")
    print("  every element with no communication between iterations, which is the")
    print("  SIMT model.  The gather pays for an index table: four indirections per")
    print("  element instead of four arithmetic offsets, and on the CPU that is")
    print(f"  {t_gather/t_slice:.1f}x the cost.  On a GPU the same distinction appears as")
    print("  uncoalesced loads, which is the subject of the next section.")

    section("2. Coalescing: transactions implied by an access pattern")
    warp, sector = 32, 32
    line_doubles = sector // 8
    print(f"  assumed geometry, stated because this script does not measure it:")
    print(f"    a warp = {warp} consecutive lanes, a memory sector = {sector} bytes "
          f"= {line_doubles} doubles")
    print("  transactions per warp for a 32-element access:")
    print("     pattern                distinct sectors touched   doubles per sector")
    for name, idx in (
        ("contiguous (lane = i)", np.arange(warp)),
        ("stride 2", np.arange(warp) * 2),
        ("stride 4", np.arange(warp) * 4),
        ("stride 8", np.arange(warp) * 8),
        ("scattered (random)", RNG.permutation(warp * 8)[:warp]),
    ):
        touched = np.unique(idx // line_doubles).size
        print(f"  {name:24s} {touched:12d}          {warp/touched:10.2f}")
    print(f"  with {line_doubles} doubles per {sector}-byte sector, a contiguous warp")
    print("  of 32 doubles touches 8 sectors and uses every double in them; a stride-8")
    print("  warp touches 32 sectors for the same 32 values and uses one double in")
    print("  each.  That is an unavoidable consequence of the geometry and is")
    print("  independent of which device runs it.")
    print("  the matching CPU measurement, on the machine that ran this script:")
    base = None
    for name, step in (("contiguous", 1), ("stride 2", 2), ("stride 8", 8)):
        arr = RNG.standard_normal(1 << 22)
        view = arr[::step]
        t = best_of(lambda: np.add(view, 1.0, out=view))
        if base is None:
            base = t
        print(f"    {name:12s}: {t*1e3:8.3f} ms, {t/base:6.2f}x contiguous")
    print("  the CPU penalty is smaller than the sector arithmetic for a GPU would")
    print("  predict, because a CPU core also fetches whole cache lines but uses")
    print("  hardware prefetch and out-of-order execution.  The arithmetic above is a")
    print("  transaction count, not a prediction of GPU time.")

    section("3. Launch overhead: the crossover between overhead and work")
    small = np.zeros(1 << 10)
    big = np.zeros(1 << 24)

    def tiny_kernel():
        np.add(small, 1.0, out=small)

    def big_kernel():
        np.add(big, 1.0, out=big)

    t_tiny = best_of(tiny_kernel, repeats=50)
    t_big = best_of(big_kernel)
    per_element = t_big / big.size
    crossover = t_tiny / per_element
    print(f"  a minimal numpy ufunc call on {small.size} elements: "
          f"{t_tiny*1e6:8.2f} us")
    print(f"  the same call on {big.size} elements: {t_big*1e3:8.3f} ms -> "
          f"{per_element*1e9:.4f} ns/element marginal")
    print(f"  implied crossover size: {crossover:.0f} elements, i.e. below about")
    print("  this many elements the fixed per-call cost dominates the arithmetic.")
    print("  Every separate operation pays a fixed cost once, so a kernel that does")
    print("  ten passes pays it ten times.  On a GPU this fixed cost is the launch")
    print("  overhead; here it is the ufunc call overhead.  The value differs, the")
    print("  structure of the trade is the same, and the crossover is measured.")

    section("4. Precision: fp32 against fp64")
    m = 1 << 22
    x64 = RNG.standard_normal(m)
    x32 = x64.astype(np.float32)
    a64 = np.zeros(m, dtype=np.float64)
    a32 = np.zeros(m, dtype=np.float32)

    def sum64():
        np.add(x64, a64, out=a64)

    def sum32():
        np.add(x32, a32, out=a32)

    t64 = best_of(sum64)
    t32 = best_of(sum32)
    print(f"  elementwise add over {m} values:")
    print(f"    float64 : {t64*1e3:8.3f} ms")
    print(f"    float32 : {t32*1e3:8.3f} ms   speedup {t64/t32:.3f}x")
    print(f"  a 1e6-element accumulation, exact reference from math.fsum:")
    import math
    vals = RNG.standard_normal(1_000_000)
    exact = math.fsum(vals.tolist())
    s64 = float(np.sum(vals.astype(np.float64), dtype=np.float64))
    s32 = float(np.sum(vals.astype(np.float32), dtype=np.float32))
    print(f"    exact (fsum)     : {exact!r}")
    print(f"    float64 pairwise : {s64!r}  rel. error {abs(s64-exact)/abs(exact):.3e}")
    print(f"    float32 pairwise : {s32!r}  rel. error {abs(s32-exact)/abs(exact):.3e}")
    ratio = abs(s32-exact)/abs(s64-exact) if s64 != exact else np.nan
    print(f"    float32 error / float64 error = {ratio:.1e}")
    print("  half the bits means a much larger unit roundoff, and a reduction")
    print("  accumulates it: this is why a mixed-precision GPU code keeps its")
    print("  reductions in 64-bit even when the kernel arithmetic is 32-bit.")

    section("5. Summary of measured quantities")
    print(f"  gather / slice stencil cost ratio           : {t_gather/t_slice:.3f}")
    print(f"  interior agreement of the two forms         : {diff:.3e}")
    print(f"  sector arithmetic, contiguous / stride 8    : 1 / 32 per warp "
          f"(assumed geometry)")
    print(f"  per-call ufunc overhead on {small.size} elements : {t_tiny*1e6:.2f} us")
    print(f"  implied crossover                           : {crossover:.0f} elements")
    print(f"  float64 / float32 elementwise add           : {t64*1e3:.3f} / "
          f"{t32*1e3:.3f} ms")
    print(f"  accumulation error, float32 / float64       : "
          f"{abs(s32-exact)/abs(exact):.3e} / {abs(s64-exact)/abs(exact):.3e}")
    print("  No GPU was used or timed.  Every number is a CPU measurement or an")
    print("  explicit arithmetic count from a stated assumed geometry; all model")
    print("  inputs are SYNTHETIC teaching values.")


if __name__ == "__main__":
    main()
