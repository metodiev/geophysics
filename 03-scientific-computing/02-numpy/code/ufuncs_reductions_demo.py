"""Universal functions, reductions and axis semantics.

Run:  .venv/bin/python ufuncs_reductions_demo.py
Requires: numpy only.

Companion to lesson 03-02-04. The cube is SYNTHETIC and deterministic: a
(depth, north, east) gravity/model cube built from arithmetic on the indices.

The script:

1. Reduces a 3-D cube over each axis in turn and prints the resulting shapes,
   which is the axis-arithmetic reference table.
2. Reproduces the classic axis mix-up on a (row, column) grid and shows the
   wrong-axis answer is dimensionally plausible -- the reason the bug survives.
3. Uses keepdims to make an axis reduction broadcast back onto the original.
4. Handles NaNs, which propagate silently through sum and mean.
5. Uses cumulative and locating reductions, plus ufunc methods
   (reduce, accumulate, outer).
6. Compares a ufunc reduction with an explicit Python loop over slices and
   reports the operation counts.
"""

import time

import numpy as np


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


NZ, NY, NX = 8, 10, 12


def make_cube():
    """SYNTHETIC (depth, north, east) cube with a linear trend and a body."""
    k = np.arange(NZ, dtype=np.float64)[:, None, None]
    j = np.arange(NY, dtype=np.float64)[None, :, None]
    i = np.arange(NX, dtype=np.float64)[None, None, :]
    cube = 100.0 + 5.0 * k + 0.5 * j + 0.25 * i
    cube[2:5, 3:7, 4:9] += 40.0
    return cube


def part1_axis_shapes():
    section("1. Reducing a 3-D cube: the shape table")

    cube = make_cube()
    print(f"cube.shape = {cube.shape}  (depth, north, east)")
    for axis in (0, 1, 2, (0, 1), (0, 2), (1, 2), (0, 1, 2)):
        print(f"  cube.sum(axis={str(axis):<9}) -> shape "
              f"{str(cube.sum(axis=axis).shape):<12} "
              f"sum = {cube.sum(axis=axis).sum():.4f}")
    print("\n  `axis=k` removes axis k. Everything else survives, in order.")
    print("  `axis=(0, 1)` removes two axes at once. The grand total is")
    print("  independent of the order the axes are removed in, but each")
    print("  intermediate result is not.")


def part2_the_mixup():
    section("2. The classic axis mix-up, and why it survives")

    cube = make_cube()
    gravity = cube.sum(axis=0)            # depth-collapsed map, shape (north, east)
    print(f"cube.shape     = {cube.shape}")
    print(f"gravity.shape  = {gravity.shape}  (north, east)")

    correct = gravity.mean(axis=0)        # mean over stations north -> (east,)
    wrong = gravity.mean(axis=1)          # mean over stations east -> (north,)
    print(f"\nmean over north stations (axis=0) -> shape {correct.shape}: "
          f"{np.round(correct, 4)}")
    print(f"mean over east stations  (axis=1) -> shape {wrong.shape}: "
          f"{np.round(wrong, 4)}")
    print(f"the two answers have different shapes: {correct.shape} vs "
          f"{wrong.shape}")
    try:
        np.allclose(correct, wrong)
    except ValueError as exc:
        print(f"comparing them raises ValueError: {exc}")
    print(f"first {wrong.size} entries of `correct` vs `wrong` are different: "
          f"{not np.allclose(correct[:wrong.size], wrong)}")
    print("\n  Both are 10 +- a few mGal. Neither reduction raises an error. The bug is")
    print("  invisible unless you check the shape against the coordinate array")
    print("  it is supposed to match. Assert shapes; do not eyeball plots.")

    # The disciplined form.
    north = np.linspace(0.0, 9000.0, NY)
    profile = gravity.mean(axis=1)
    assert profile.shape == north.shape, (profile.shape, north.shape)
    print(f"  assert profile.shape == north.shape -> "
          f"{profile.shape} == {north.shape}: passed")


def part3_keepdims():
    section("3. keepdims: reductions that broadcast back")

    cube = make_cube()
    plain = cube.mean(axis=0)
    kept = cube.mean(axis=0, keepdims=True)
    print(f"cube.mean(axis=0).shape              = {plain.shape}")
    print(f"cube.mean(axis=0, keepdims=True).shape = {kept.shape}")
    anomaly = cube - kept                 # (8, 10, 12) - (1, 10, 12)
    print(f"cube - kept.shape                    = {anomaly.shape}")
    print(f"anomaly.mean(axis=0).max()           = "
          f"{np.abs(anomaly.mean(axis=0)).max():.3e}")
    print("  keepdims is the difference between a broadcast that works and a")
    print("  ValueError; it also documents which axis you collapsed.")


def part4_nan():
    section("4. NaN propagation and the nan-aware reductions")

    a = np.array([[1.0, 2.0, np.nan],
                  [4.0, np.nan, 6.0]])
    print("a =\n", a)
    print(f"np.sum(a)            = {np.sum(a)}")
    print(f"np.mean(a)           = {np.mean(a)}")
    print(f"np.nansum(a)         = {np.nansum(a)}")
    print(f"np.nanmean(a)        = {np.nanmean(a)}")
    print(f"np.nanmax(a)         = {np.nanmax(a)}")
    print(f"np.all(np.isnan(a).sum(axis=1) > 0) = "
          f"{np.all(np.isnan(a).sum(axis=1) > 0)}")
    print(f"np.isnan(a).any()    = {np.isnan(a).any()}")
    print("\n  A single NaN silently contaminates sum/mean/min/max but NOT")
    print("  argmax or comparisons. nansum/nanmean exist precisely because this")
    print("  is the most common silent failure with real field data.")


def part5_cumulative_locating():
    section("5. Cumulative and locating reductions")

    cube = make_cube()
    depth_profile = cube.mean(axis=(1, 2))
    print(f"depth profile (mean over the map) = {np.round(depth_profile, 3)}")
    cum = np.cumsum(depth_profile)
    print(f"cumulative sum                    = {np.round(cum, 3)}")
    print(f"np.trapezoid-free total (cum[-1]) = {cum[-1]:.6f}   "
          f"equals profile.sum(): {cum[-1] == depth_profile.sum()}")

    flat = cube.ravel()
    print(f"\ncube.ravel().shape = {flat.shape}")
    print(f"argmax (flat index) = {flat.argmax()}, value = {flat.max():.4f}")
    k, j, i = np.unravel_index(flat.argmax(), cube.shape)
    print(f"unravel_index -> (depth, north, east) = ({k}, {j}, {i})")
    print(f"cube[{k}, {j}, {i}] = {cube[k, j, i]}   (same value)")

    print(f"\nnp.argmax(cube, axis=0).shape = {np.argmax(cube, axis=0).shape}"
          "  -> the depth of the maximum at every map cell")
    print(f"np.percentile(depth_profile, [0, 50, 100]) = "
          f"{np.percentile(depth_profile, [0, 50, 100])}")
    print("  arg-reductions return integer indices; converting them to physical")
    print("  coordinates requires the same origin and spacing as the array.")


def part6_ufunc_methods():
    section("6. ufunc methods: reduce, accumulate, outer")

    a = np.array([1.0, 2.0, 3.0, 4.0])
    b = np.array([10.0, 20.0, 30.0])
    print(f"np.add.reduce(a)      = {np.add.reduce(a)}")
    print(f"np.add.accumulate(a)  = {np.add.accumulate(a)}")
    print(f"np.add.outer(a, b) =\n{np.add.outer(a, b)}")
    print(f"np.maximum.reduce([a, np.array([2.5, 1.0, 5.0, 3.0])]) = "
          f"{np.maximum.reduce([a, np.array([2.5, 1.0, 5.0, 3.0])])}")
    print(f"np.multiply.reduce(a) = {np.multiply.reduce(a)} (factorial 4!)")
    print("\n  `np.add.reduce` IS `np.sum`. Recognising the ufunc behind the")
    print("  reduction explains why np.maximum.reduce works for elementwise")
    print("  maxima and np.sum does not.")


def part7_speed():
    section("7. A reduction versus an explicit loop (operation counts)")

    n = 4_000_000
    x = np.arange(n, dtype=np.float64)

    t0 = time.perf_counter()
    s_np = np.sum(x)
    t_np = time.perf_counter() - t0

    t0 = time.perf_counter()
    s_loop = 0.0
    for value in x:
        s_loop += float(value)
    t_loop = time.perf_counter() - t0

    print(f"n = {n} elements")
    print(f"np.sum          : {s_np!r} in {t_np * 1e3:8.3f} ms")
    print(f"Python for-loop : {s_loop!r} in {t_loop * 1e3:8.3f} ms")
    print(f"ratio (loop/numpy) = {t_loop / t_np:.1f}x   (machine dependent)")
    print(f"both results agree exactly: {s_np == s_loop}")
    print("\n  The reproducible claim is the operation count: the loop performs")
    print(f"  {n} interpreted iterations plus {n} Python-level additions; np.sum")
    print("  performs the same additions in compiled, pairwise-ordered code.")
    print("  Wall-clock ratios vary with CPU, cache and library build; the")
    print("  count of interpreted operations does not.")


def main():
    print("NumPy ufuncs and reductions -- companion to lesson 03-02-04")
    print(f"numpy version: {np.__version__}")
    part1_axis_shapes()
    part2_the_mixup()
    part3_keepdims()
    part4_nan()
    part5_cumulative_locating()
    part6_ufunc_methods()
    part7_speed()


if __name__ == "__main__":
    main()
