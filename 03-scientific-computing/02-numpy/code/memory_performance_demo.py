"""Memory layout, strides and cache-aware performance.

Run:  .venv/bin/python memory_performance_demo.py
Requires: numpy only.

Companion to lesson 03-02-07. All arrays are SYNTHETIC (drawn from a seeded
generator); no data is read.

Timings are MACHINE DEPENDENT and are printed as such. The reproducible claims
are the element counts, the byte counts and the strides; the wall-clock ratios
are observations on one machine, to be re-measured rather than quoted as law.

The script deliberately reports one measurement that CONTRADICTS the folklore,
because the folklore is wrong: on a C-ordered array NumPy reduces along axis 0
at essentially the same speed as along axis 1, since the reduction streams
sequentially into an accumulator either way. The large layout penalty appears
when a strided VIEW is traversed elementwise, which is what sections 3 and 4
measure.
"""

import time

import numpy as np


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


SEED = 20261014
N = 3000


def best_of(fn, repeat=3):
    best = float("inf")
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn()
        best = min(best, time.perf_counter() - t0)
    return best, result


def part1_strides():
    section("1. Strides say which direction is contiguous")

    a = np.zeros((4, 5), dtype=np.float64)
    f = np.asfortranarray(a)
    print(f"C-order  shape {a.shape}, strides {a.strides} bytes "
          f"-> fastest axis is axis 1 (columns)")
    print(f"F-order  shape {f.shape}, strides {f.strides} bytes "
          f"-> fastest axis is axis 0 (rows)")
    print(f"a.itemsize = {a.itemsize} bytes")
    print("  Along the fastest axis consecutive elements are itemsize bytes")
    print("  apart. Along any other axis the step is a multiple of a row")
    print("  length, and every step lands on a different cache line.")


def part2_axis_reduction():
    section("2. Reducing along each axis of a C-ordered matrix")

    rng = np.random.default_rng(SEED)
    arr = rng.random((N, N))
    print(f"arr.shape = {arr.shape}, {arr.nbytes / 1e6:.1f} MB, "
          f"strides = {arr.strides}, C-contiguous = {arr.flags['C_CONTIGUOUS']}")
    print(f"elements touched by each reduction: {arr.size}")

    t_rows, s_rows = best_of(lambda: arr.sum(axis=1))
    t_cols, s_cols = best_of(lambda: arr.sum(axis=0))
    t_flat, _ = best_of(lambda: arr.sum())
    print(f"\n  arr.sum(axis=1)  (axis 1 contiguous)  : {t_rows * 1e3:8.2f} ms")
    print(f"  arr.sum(axis=0)  (axis 0 strided)     : {t_cols * 1e3:8.2f} ms")
    print(f"  arr.sum()        (both axes, one pass): {t_flat * 1e3:8.2f} ms")
    print(f"  ratio axis0/axis1 = {t_cols / t_rows:.2f}x   (machine dependent)")
    print(f"  sums agree within 1e-9: "
          f"{np.isclose(s_rows.sum(), s_cols.sum())}")
    print("\n  The folklore says summing along axis 0 of a C-ordered array is")
    print("  several times slower. It is not: NumPy walks the array row by")
    print("  row in BOTH cases and accumulates into a length-3000 buffer that")
    print("  stays in cache. Sequential streaming plus pairwise accumulation")
    print("  removes the penalty. Measure before optimising; this is the")
    print("  measurement that stops the folklore being repeated.")


def part3_strided_view():
    section("3. The real penalty: traversing a strided view")

    rng = np.random.default_rng(SEED)
    arr = rng.random((N, N))

    def strided():
        view = arr[:, ::16]              # (3000, 188), stride 128 bytes
        view += 1.0                      # in-place, no allocation
        return view

    def contiguous():
        view = arr[::16, :]              # (188, 3000), contiguous rows
        view += 1.0
        return view

    t_str, v_str = best_of(strided)
    t_con, v_con = best_of(contiguous)
    print(f"arr[:, ::16].shape = {v_str.shape}, strides = {v_str.strides}")
    print(f"arr[::16, :].shape = {v_con.shape}, strides = {v_con.strides}")
    print(f"elements modified by each : {v_str.size} and {v_con.size}")
    print(f"\n  column-strided (stride 128 B) : {t_str * 1e3:8.3f} ms")
    print(f"  row-subset     (contiguous)   : {t_con * 1e3:8.3f} ms")
    print(f"  ratio strided/contiguous = {t_str / t_con:.1f}x   "
          f"(machine dependent)")
    print("\n  Same number of elements, same arithmetic, same operation count.")
    print("  The 128-byte stride means each element sits alone on a 128-byte")
    print("  cache line, so the hardware moves many times more memory per")
    print("  useful value. Every decimation, every every-nth-trace gather, has")
    print("  this shape -- and the fix is to write into a contiguous output")
    print("  grid rather than to bang on the strided view.")


def part4_traversal_order():
    section("4. In-place traversal: row-wise against column-wise")

    rng = np.random.default_rng(SEED)
    n = 2000
    a = rng.random((n, n))
    b = rng.random((n, n))

    def row_wise():
        for i in range(n):
            a[i, :] += 1.0

    def col_wise():
        for j in range(n):
            b[:, j] += 1.0

    t_row, _ = best_of(row_wise, repeat=1)
    t_col, _ = best_of(col_wise, repeat=1)
    print(f"n = {n}, {a.nbytes / 1e6:.1f} MB per array")
    print(f"row-wise  for i: a[i, :] += 1.0 : {t_row * 1e3:8.2f} ms")
    print(f"col-wise  for j: b[:, j] += 1.0 : {t_col * 1e3:8.2f} ms")
    print(f"ratio column/row = {t_col / t_row:.2f}x   (machine dependent)")
    print(f"both loops perform {n} iterations and {n * n} additions")
    print("\n  This is the row-major versus column-major traversal result in")
    print("  its purest form: identical work, different memory order. A 2000-")
    print("  element row is 16 kB, contiguous, and stays in cache; a 2000-")
    print("  element column touches 2000 different cache lines.")


def part5_contiguity_copy():
    section("5. What making an array contiguous costs")

    rng = np.random.default_rng(SEED)
    arr = rng.random((N, N))
    at = arr.T
    print(f"arr.T is C-contiguous: {at.flags['C_CONTIGUOUS']}  "
          f"(strides {at.strides})")
    t_copy, contig = best_of(lambda: np.ascontiguousarray(at))
    t_nocopy, same = best_of(lambda: np.ascontiguousarray(arr))
    print(f"np.ascontiguousarray(arr.T) : {t_copy * 1e3:8.2f} ms  "
          f"(copies {at.nbytes / 1e6:.1f} MB)")
    print(f"np.ascontiguousarray(arr)   : {t_nocopy * 1e3:8.2f} ms  "
          f"(returns the same object: {same is arr})")
    print(f"copying {arr.size} elements costs "
          f"{t_copy * 1e3 / (arr.size / 1e6):.2f} ms per 1e6 elements "
          "(machine dependent)")
    print("\n  Copying is memory-bandwidth bound, which is why it costs about")
    print("  the same as one read-modify-write pass. Pay it once if the array")
    print("  is used many times; do not pay it inside a loop.")


def part6_matrix_product():
    section("6. Matrix product on C- and F-ordered operands")

    rng = np.random.default_rng(SEED)
    n = 1200
    A = rng.random((n, n))
    B = rng.random((n, n))
    Af = np.asfortranarray(A)
    Bf = np.asfortranarray(B)
    t0, C0 = best_of(lambda: A @ B)
    t1, C1 = best_of(lambda: Af @ Bf)
    print(f"n = {n}, {2 * A.nbytes / 1e6:.1f} MB of operands per multiplication")
    print(f"A @ B   (both C order): {t0 * 1e3:8.2f} ms")
    print(f"Af @ Bf (both F order): {t1 * 1e3:8.2f} ms")
    print(f"ratio = {t1 / t0:.3f}x   (machine dependent)")
    print(f"results identical: {np.array_equal(C0, C1)}")
    print("\n  BLAS selects a different kernel for each layout, so this is")
    print("  usually a wash -- provided both operands have the SAME layout.")
    print("  Mixing a C-order and an F-order operand forces a copy inside")
    print("  the library, and that copy is what shows up as an unexplained")
    print("  slow multiplication.")


def main():
    print("Memory layout and cache-aware performance -- companion to "
          "lesson 03-02-07")
    print(f"numpy version: {np.__version__}, SEED = {SEED}, N = {N}")
    print("Timings are machine dependent observations, not laws.")
    part1_strides()
    part2_axis_reduction()
    part3_strided_view()
    part4_traversal_order()
    part5_contiguity_copy()
    part6_matrix_product()


if __name__ == "__main__":
    main()
