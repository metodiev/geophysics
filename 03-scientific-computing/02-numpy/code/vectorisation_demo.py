"""Replacing loops: vectorisation patterns and traps.

Run:  .venv/bin/python vectorisation_demo.py
Requires: numpy only.

Companion to lesson 03-02-08. All quantities are SYNTHETIC: the source depths,
densities, station positions and random vectors are generated in-code.

Timings are MACHINE DEPENDENT and are printed as such. The reproducible claims
are the operation counts, the element counts and the peak memory measured by
tracemalloc. Three of the four sections contain a case where the apparently
vectorised form is slower than the loop it replaces, because a vectorisation
rule applied without measuring is how numerical code becomes both slow and
wrong.

The script:

1. Forward-models the gravity of many point masses at many stations with a
   triple loop and with broadcasting; checks agreement and reports the ratio.
2. Shows the memory-bound trap: (x * x).sum() against np.dot(x, x), with peak
   allocation measured.
3. Shows np.vectorize for what it is -- a Python-level loop, about two orders
   of magnitude slower than the array expression that replaces it.
4. Shows growth by np.append in a loop against filling a preallocated array.
5. Shows a broadcast that allocates a 384 MB intermediate where a row-wise loop
   needs 0.2 MB, and reports the timing honestly, including its instability.
"""

import time
import tracemalloc

import numpy as np


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


SEED = 20261014
G = 6.67430e-11          # m^3 kg^-1 s^-2


def best_of(fn, repeat=3):
    best = float("inf")
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn()
        best = min(best, time.perf_counter() - t0)
    return best, result


def part1_forward_model():
    section("1. Forward-model gravity: triple loop against broadcasting")

    rng = np.random.default_rng(SEED)
    nsrc = 400
    nobs = 400
    src = rng.uniform(0.0, 5000.0, size=(nsrc, 3))       # x, y, depth (m)
    src[:, 2] = rng.uniform(200.0, 2000.0, size=nsrc)
    mass = rng.uniform(1e9, 1e11, size=nsrc)             # kg
    obs = rng.uniform(0.0, 5000.0, size=(nobs, 2))       # x, y (m)
    obs_z = 0.0

    def loop_version():
        gz = np.zeros(nobs)
        for i in range(nobs):
            for j in range(nsrc):
                dx = obs[i, 0] - src[j, 0]
                dy = obs[i, 1] - src[j, 1]
                dz = obs_z - src[j, 2]
                r2 = dx * dx + dy * dy + dz * dz
                gz[i] += G * mass[j] * dz / (r2 * np.sqrt(r2))
        return gz

    def vector_version():
        dx = obs[:, 0][:, None] - src[:, 0][None, :]
        dy = obs[:, 1][:, None] - src[:, 1][None, :]
        dz = obs_z - src[:, 2][None, :]
        r2 = dx * dx + dy * dy + dz * dz
        return np.sum(G * mass[None, :] * dz / (r2 * np.sqrt(r2)), axis=1)

    t_loop, g_loop = best_of(loop_version, repeat=1)
    t_vec, g_vec = best_of(vector_version, repeat=3)
    max_diff = np.abs(g_loop - g_vec).max()
    mGal = 1e5
    print(f"nobs = {nobs}, nsrc = {nsrc}, pairs = {nobs * nsrc}")
    print(f"triple loop (1 run)   : {t_loop * 1e3:9.2f} ms")
    print(f"broadcast  (best of 3): {t_vec * 1e3:9.2f} ms")
    print(f"speedup               : {t_loop / t_vec:9.1f}x   (machine dependent)")
    print(f"max |loop - vector|   : {max_diff:.3e} m/s^2 "
          f"({max_diff * mGal:.3e} mGal)")
    print(f"largest signal        : {g_loop.max() * mGal:.4f} mGal")
    print(f"agreement (rel 1e-10) : {np.allclose(g_loop, g_vec, rtol=1e-10)}")
    print(f"\n  Both forms perform nobs*nsrc = {nobs * nsrc} distance evaluations")
    print("  and the same number of floating-point operations. The loop pays")
    print("  interpreter overhead per pair; the broadcast form runs the")
    print("  arithmetic in compiled loops but allocates four (nobs, nsrc)")
    print(f"  temporaries of {nobs * nsrc * 8 / 1e6:.2f} MB each.")
    print("  The speedup is real; so is the memory, and the memory claim is")
    print("  the one you should check before scaling nobs or nsrc.")


def part2_memory_bound():
    section("2. The memory-bound trap: (x * x).sum() versus np.dot(x, x)")

    rng = np.random.default_rng(SEED)
    n = 20_000_000
    x = rng.standard_normal(n)
    print(f"n = {n}, x.nbytes = {x.nbytes / 1e6:.1f} MB")

    tracemalloc.start()
    t_tmp, s_tmp = best_of(lambda: (x * x).sum())
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"\n(x * x).sum()  : {t_tmp * 1e3:8.2f} ms, "
          f"peak traced memory {peak / 1e6:8.1f} MB")

    tracemalloc.start()
    t_dot, s_dot = best_of(lambda: np.dot(x, x))
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"np.dot(x, x)   : {t_dot * 1e3:8.2f} ms, "
          f"peak traced memory {peak / 1e6:8.1f} MB")

    print(f"\nratio ((x*x).sum() / dot) = {t_tmp / t_dot:.2f}x   "
          f"(machine dependent)")
    print(f"values agree within 1e-10: {np.isclose(s_tmp, s_dot, rtol=1e-10)}")
    print(f"{s_tmp!r}")
    print(f"{s_dot!r}")
    print("\n  The vectorised expression is the slower one. It allocates a")
    print(f"  temporary of {n * 8 / 1e6:.0f} MB and streams it back from memory,"
          " so the operation")
    print("  is limited by DRAM bandwidth, not by arithmetic. np.dot routes to")
    print("  BLAS, which accumulates on the fly and never materialises the")
    print("  squares. Same answer, one pass over memory instead of two.")


def part3_vectorize():
    section("3. np.vectorize is a loop in disguise")

    rng = np.random.default_rng(SEED)
    n = 1_000_000
    x = rng.random(n) * 10.0

    def list_comp(a):
        return np.array([v * v - 2.0 * v + 1.0 for v in a])

    def array_expr(a):
        return a * a - 2.0 * a + 1.0

    def fake_vectorised(a):
        return np.vectorize(lambda v: v * v - 2.0 * v + 1.0)(a)

    t_list, r1 = best_of(lambda: list_comp(x))
    t_vec, r2 = best_of(lambda: array_expr(x))
    t_npv, r3 = best_of(lambda: fake_vectorised(x))
    print(f"n = {n} elements")
    print(f"Python list comprehension : {t_list * 1e3:9.2f} ms")
    print(f"array expression a*a-2*a+1: {t_vec * 1e3:9.2f} ms")
    print(f"np.vectorize(lambda ...)  : {t_npv * 1e3:9.2f} ms")
    print(f"np.vectorize / array expr = {t_npv / t_vec:8.1f}x   "
          f"(machine dependent)")
    print(f"list comp    / array expr = {t_list / t_vec:8.1f}x   "
          f"(machine dependent)")
    agree = np.allclose(r1, r2) and np.allclose(r2, r3)
    print(f"all three results equal   : {agree}")
    print("\n  np.vectorize calls the Python function once per element --")
    print(f"  {n} Python calls -- and only hides that from the reader. It")
    print("  cannot be faster than the list comprehension and it is two")
    print("  orders of magnitude slower than the ufunc expression. The")
    print("  reproducible claim is the call count, not the millisecond ratio.")
    print("  Use it only for a function that genuinely cannot be expressed")
    print("  with ufuncs, and never inside a hot loop.")


def part4_growing_arrays():
    section("4. Growing an array in a loop versus preallocating")

    m = 20_000

    def appending():
        a = np.empty(0)
        for i in range(m):
            a = np.append(a, [float(i)])
        return a

    def preallocated():
        a = np.empty(m)
        for i in range(m):
            a[i] = float(i)
        return a

    t_app, a1 = best_of(appending, repeat=1)
    t_pre, a2 = best_of(preallocated, repeat=1)
    print(f"m = {m} values")
    print(f"np.append in a loop : {t_app * 1e3:9.2f} ms")
    print(f"preallocated fill   : {t_pre * 1e3:9.2f} ms")
    print(f"ratio = {t_app / t_pre:.0f}x   (machine dependent)")
    print(f"results identical: {np.array_equal(a1, a2)}")
    print(f"\n  np.append copies the whole array every call, so the loop does")
    print(f"  1 + 2 + ... + {m} = {m * (m + 1) // 2} element copies, about")
    print(f"  {m * (m + 1) // 2 / 1e6:.4f}e6, instead of {m}. The fix is to")
    print("  allocate once and fill by index, or to collect into a Python list")
    print("  and call np.array once at the end. The quadratic copy count is")
    print("  the reproducible quantity; it does not depend on the machine.")


def part5_broadcast_memory():
    section("5. A broadcast whose intermediate does not fit in cache")

    rng = np.random.default_rng(SEED)
    nobs = 4000
    xy = rng.uniform(0.0, 5000.0, size=(nobs, 2))

    def full_matrix():
        dx = xy[:, None, 0] - xy[None, :, 0]
        dy = xy[:, None, 1] - xy[None, :, 1]
        return np.hypot(dx, dy).mean()

    def row_loop():
        total = 0.0
        for i in range(nobs):
            dx = xy[:, 0] - xy[i, 0]
            dy = xy[:, 1] - xy[i, 1]
            total += np.sqrt(dx * dx + dy * dy).sum()
        return total / (nobs * nobs)

    tracemalloc.start()
    t_full1, m_full = best_of(full_matrix, repeat=1)
    _, peak_full = tracemalloc.get_traced_memory()
    t_full2, _ = best_of(full_matrix, repeat=1)
    tracemalloc.stop()

    tracemalloc.start()
    t_row1, m_row = best_of(row_loop, repeat=1)
    _, peak_row = tracemalloc.get_traced_memory()
    t_row2, _ = best_of(row_loop, repeat=1)
    tracemalloc.stop()

    print(f"nobs = {nobs}, pairs = {nobs * nobs}")
    print(f"full {nobs}x{nobs} broadcast : "
          f"run 1 {t_full1:6.3f} s, run 2 {t_full2:6.3f} s, "
          f"peak traced {peak_full / 1e6:7.1f} MB")
    print(f"row-wise loop            : "
          f"run 1 {t_row1:6.3f} s, run 2 {t_row2:6.3f} s, "
          f"peak traced {peak_row / 1e6:7.1f} MB")
    print(f"time ratios full/row     : {t_full1 / t_row1:.2f}x then "
          f"{t_full2 / t_row2:.2f}x   (machine dependent, unstable)")
    print(f"means agree to 1e-12: {np.isclose(m_full, m_row, rtol=1e-12)}")
    print(f"the full matrix alone is {nobs * nobs * 8 / 1e6:.1f} MB of "
          "intermediate")
    print(f"peak memory ratio = {peak_full / peak_row:.0f}x   (this is the"
          " robust result)")
    print("\n  The speed difference between the two forms is not stable: the")
    print("  two runs above bracket it, and on other machines either order")
    print("  can win. The memory difference is not in doubt -- 384 MB against")
    print("  0.2 MB. The broadcast form allocates an intermediate that does")
    print("  not fit in cache (or, at ten times this station count, in RAM),")
    print("  while the row-wise loop allocates one n-element temporary that")
    print("  does. This is the honest limit of 'replace the loop': vectorise")
    print("  the inner axis, block the outer one, and always know the size of")
    print("  the largest array the expression must create.")


def main():
    print("Vectorisation patterns and traps -- companion to lesson 03-02-08")
    print(f"numpy version: {np.__version__}, SEED = {SEED}")
    print("Timings are machine dependent observations, not laws.")
    part1_forward_model()
    part2_memory_bound()
    part3_vectorize()
    part4_growing_arrays()
    part5_broadcast_memory()


if __name__ == "__main__":
    main()
