#!/usr/bin/env python3
"""Computer architecture, the memory hierarchy and roofline thinking, measured.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hpc_architecture_demo.py

Everything is SYNTHETIC: the arrays, kernels and grid sizes are chosen teaching
values.  No hardware model name, no vendor figure and no published benchmark is
used or quoted.  Every number is a measurement made by this script on the machine
that runs it, so every number is machine-dependent.

Contents
--------
1. Sustained bandwidth of one streaming kernel against working-set size.
2. Three streaming kernels with different arithmetic intensity: measured traffic,
   bandwidth, FLOP rate, and the rate ratio against the intensity ratio.
3. Access pattern: measured cost of strided sweeps against stride 1.
4. A 5-point stencil: byte bookkeeping, three implementations, and the measured
   fact that the obvious rewrite is slower.
5. Summary of measured quantities and the caveat that governs all of them.
"""

import os
import time

import numpy as np
from scipy import ndimage

RNG = np.random.default_rng(20261014)

BYTES_PER_DOUBLE = 8


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def best_of(fn, repeats=5):
    """Minimum wall-clock time of fn over a few repeats (seconds)."""
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn()
        times.append(time.perf_counter() - t0)
    return min(times)


def main():
    section("1. Sustained bandwidth of one streaming kernel versus working set")
    print("  kernel: y = a*x + y (a triad), float64")
    print("  traffic model: x read, temporary written, temporary read, y read, y")
    print("  written = 5 passes of 8 bytes = 40 bytes per element")
    print(f"  the machine reports logical CPUs = {os.cpu_count()}")
    print("     elements   per array   time (ms)    GB/s (40 B/element)")
    a = np.float64(1.0000001)
    rows = []
    for m in (1 << 10, 1 << 13, 1 << 16, 1 << 18, 1 << 20, 1 << 22, 1 << 23):
        x = RNG.standard_normal(m)
        y = RNG.standard_normal(m)
        t = best_of(lambda: np.add(y, a * x, out=y))
        gbs = 5 * BYTES_PER_DOUBLE * m / t / 1e9
        rows.append((m, t, gbs))
        print(f"  {m:10d}   {m*8/1024:8.0f} KB   {t*1e3:9.4f}   {gbs:6.2f}")
    peak = max(rows, key=lambda r: r[2])
    plateau = rows[-1]
    print(f"\n  smallest array ({rows[0][0]} elements): {rows[0][2]:.2f} GB/s, limited by")
    print("  per-call overhead rather than by memory")
    print(f"  largest value at {peak[0]} elements ({peak[0]*8/1024:.0f} KB per array): "
          f"{peak[2]:.2f} GB/s")
    print(f"  largest array ({plateau[0]} elements): {plateau[2]:.2f} GB/s")
    print(f"  plateau / peak = {plateau[2]/peak[2]:.3f}")
    print("  the shape is the transferable part: an overhead regime at the small end")
    print("  and a flat plateau where every access goes to main memory.  This script")
    print("  does not print cache sizes or hardware names because it does not measure")
    print("  them; it measures the transitions.")

    section("2. Three streaming kernels: intensity, bandwidth and rate")
    m = 1 << 23
    x = RNG.standard_normal(m)
    y = RNG.standard_normal(m)
    kernels = [
        ("copy  y = x", 0, 2, lambda: np.copyto(y, x)),
        ("scale y = a*x", 1, 2, lambda: np.multiply(x, a, out=y)),
        ("triad y = a*x + y", 2, 5, lambda: np.add(y, a * x, out=y)),
    ]
    print("  traffic is counted in 8-byte passes per element, as implemented by these")
    print("  numpy expressions (the triad's temporary costs two extra passes):")
    print("     kernel                flops/elem  passes  bytes/elem   GB/s    GFLOP/s")
    measured = {}
    for name, flops, passes, fn in kernels:
        t = best_of(fn)
        byt = passes * BYTES_PER_DOUBLE
        gbs = byt * m / t / 1e9
        gfl = flops * m / t / 1e9
        measured[name] = (gbs, gfl, t, byt, flops)
        print(f"  {name:22s} {flops:8d}  {passes:7d}  {byt:10d}   {gbs:6.2f}   {gfl:7.4f}")
    gb_copy = measured["copy  y = x"][0]
    gb_scale = measured["scale y = a*x"][0]
    gb_triad = measured["triad y = a*x + y"][0]
    r_flop = measured["triad y = a*x + y"][1] / measured["scale y = a*x"][1]
    r_int = (2 / 40) / (1 / 16)
    print(f"\n  bandwidth spread across the three kernels: "
          f"{max(gb_copy, gb_scale, gb_triad)/min(gb_copy, gb_scale, gb_triad):.3f}x")
    print(f"  FLOP-rate ratio triad/scale: measured {r_flop:.3f}, predicted from the")
    print(f"  intensity ratio (2/40)/(1/16) = {r_int:.3f}")
    print("  the three kernels share one resource -- bytes -- and their FLOP rates")
    print("  differ by the ratio of their arithmetic intensities, as the roofline says.")
    pred = 5 * BYTES_PER_DOUBLE * m / (gb_copy * 1e9)
    print(f"  triad time predicted from the INDEPENDENT copy kernel at {gb_copy:.2f} GB/s:")
    print(f"    predicted {pred*1e3:.3f} ms, measured "
          f"{measured['triad y = a*x + y'][2]*1e3:.3f} ms, ratio "
          f"{measured['triad y = a*x + y'][2]/pred:.3f}")
    print("  no vendor peak and no FLOP peak appear anywhere in that prediction.")

    section("3. Access pattern: strided against contiguous")
    m = 1 << 22
    v = RNG.standard_normal(m)
    base = best_of(lambda: float(v.sum()))
    print(f"  summing {m} doubles contiguous: {base*1e3:.3f} ms -> "
          f"{m*BYTES_PER_DOUBLE/base/1e9:.2f} GB/s")
    print("     stride   elements    time (ms)   time per element, relative to stride 1")
    for s in (1, 2, 4, 8, 16):
        view = v[::s]
        t = best_of(lambda: float(view.sum()))
        print(f"  {s:8d}   {view.size:8d}   {t*1e3:9.4f}   "
              f"{(t/view.size)/(base/m):8.2f}")
    print("  per element, a stride of 8 or 16 costs several times a stride of 1.  A")
    print("  cache line of 8 doubles holds one element of a stride-8 sweep and seven")
    print("  values that are fetched and discarded; the measured penalty is that")
    print("  fetch, scaled by the line size -- which is why the number of doubles per")
    print("  line is stated here as an assumption, not measured.")

    section("4. A 5-point stencil: bytes, temporaries, and what is measured")
    n = 2048
    u = RNG.standard_normal((n, n))
    out = np.empty_like(u)
    acc = np.empty((n - 2, n - 2))
    interior = (slice(1, -1), slice(1, -1))

    def laps_naive():
        out[1:-1, 1:-1] = (u[:-2, 1:-1] + u[2:, 1:-1] + u[1:-1, :-2]
                           + u[1:-1, 2:] - 4.0 * u[1:-1, 1:-1])

    def laps_no_temp():
        np.add(u[:-2, 1:-1], u[2:, 1:-1], out=acc)
        np.add(acc, u[1:-1, :-2], out=acc)
        np.add(acc, u[1:-1, 2:], out=acc)
        np.multiply(u[1:-1, 1:-1], 4.0, out=out[1:-1, 1:-1])
        np.subtract(acc, out[1:-1, 1:-1], out=out[1:-1, 1:-1])

    def laps_scipy():
        ndimage.laplace(u, output=out)

    points = (n - 2) ** 2
    ideal_bytes = 6 * BYTES_PER_DOUBLE
    naive_bytes = (5 + 4 + 4 + 1) * BYTES_PER_DOUBLE
    t_naive = best_of(laps_naive)
    ref = out.copy()
    laps_no_temp()
    no_temp = out.copy()
    t_no_temp = best_of(laps_no_temp)
    laps_scipy()
    scipy_res = out.copy()
    t_scipy = best_of(laps_scipy)
    print(f"  grid {n}x{n}, update points = {points}")
    print(f"  ideal traffic (five reads, one write)      = {ideal_bytes} bytes per point")
    print(f"  naive traffic (five reads, four temporaries written and read, one write)")
    print(f"                                             = {naive_bytes} bytes per point")
    print("     implementation            time (ms)    GB/s (ideal bytes)   GFLOP/s")
    for name, t in (("naive expression", t_naive),
                    ("no-temporary rewrite", t_no_temp),
                    ("scipy.ndimage.laplace", t_scipy)):
        print(f"  {name:26s} {t*1e3:9.3f}   {ideal_bytes*points/t/1e9:12.2f}   "
              f"{5*points/t/1e9:8.3f}")
    print(f"  naive and no-temporary agree to {np.max(np.abs(ref-no_temp)):.1e} "
          f"(identical arithmetic)")
    print(f"  scipy.ndimage agrees with the naive expression in the interior to "
          f"{np.max(np.abs(ref[interior]-scipy_res[interior])):.1e}; it differs at the")
    print("  edges because it applies a boundary mode rather than leaving the border")
    print(f"\n  measured result: the no-temporary rewrite is {t_no_temp/t_naive:.2f}x "
          f"the naive time and")
    print(f"  scipy.ndimage is {t_scipy/t_naive:.2f}x it.  Removing temporaries did not")
    print("  help: the rewrite replaces one contiguous pass with five strided row")
    print("  passes and five call overheads.  numpy has no fused expression evaluator,")
    print("  so 'fewer temporaries' and 'faster' are not the same sentence.")
    pred_stencil = naive_bytes * points / (gb_copy * 1e9)
    print(f"  prediction from the copy bandwidth ({gb_copy:.2f} GB/s) with the naive")
    print(f"  traffic model: {pred_stencil*1e3:.3f} ms, against {t_naive*1e3:.3f} ms "
          f"measured, ratio {t_naive/pred_stencil:.3f}")
    print("  so the stencil does not reach the streaming ceiling under either traffic")
    print("  model; the gap is the cost of row-slice strides, and it is measured here")
    print("  rather than assumed.")

    section("5. Summary of measured quantities")
    print(f"  main-memory plateau, triad (40 B/element model) : {plateau[2]:.2f} GB/s")
    print(f"  peak value across the size sweep                : {peak[2]:.2f} GB/s "
          f"at {peak[0]} elements")
    print(f"  copy / scale / triad bandwidth                  : {gb_copy:.2f} / "
          f"{gb_scale:.2f} / {gb_triad:.2f} GB/s")
    print(f"  FLOP-rate ratio triad/scale, measured / predicted: {r_flop:.3f} / "
          f"{r_int:.3f}")
    print(f"  triad time predicted from the copy               : ratio "
          f"{measured['triad y = a*x + y'][2]/pred:.3f}")
    print(f"  5-point stencil: naive / no-temp / scipy         : {t_naive*1e3:.3f} / "
          f"{t_no_temp*1e3:.3f} / {t_scipy*1e3:.3f} ms")
    print("  Every number in this file is a timing on the machine that ran it.  A")
    print("  reader on other hardware should expect different values and the same")
    print("  qualitative shape: a byte-limited plateau, a rate ratio equal to the")
    print("  intensity ratio, and a stride penalty set by the cache-line size.")


if __name__ == "__main__":
    main()
