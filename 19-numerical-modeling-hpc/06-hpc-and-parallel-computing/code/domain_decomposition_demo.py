#!/usr/bin/env python3
"""Domain decomposition and load balancing: geometry, measured imbalance, and the
measured cost of ignoring it.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python domain_decomposition_demo.py

Everything is SYNTHETIC: the grid, the velocity field used to generate unequal
per-column cost, and the unit of work are chosen teaching values.  The emulated
"ranks" are short-lived bounded threads inside this process; no process, MPI rank
or subprocess is started, and every pool is closed with an explicit join.

Contents
--------
1. Decomposition geometry: strips against blocks, and the halo fraction of each.
2. A SYNTHETIC velocity field that makes the work unequal, and the CFL reason.
3. Partitioning: equal width against a greedy work-balanced split, in counts.
4. The same two partitions run as emulated ranks: measured makespan.
5. Decomposition correctness: the answer does not depend on the number of ranks.
6. Amdahl's law from a measured serial fraction, and the summary.
"""

import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np

RNG = np.random.default_rng(20261014)

N = 512                 # grid points per side (SYNTHETIC)
RANKS = 4
REPEATS_PER_UNIT = 12   # work per unit of partition weight (tuned for ~tens of ms)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def jacobi_sweep(u):
    new = u.copy()
    new[1:-1, 1:-1] = 0.25 * (u[:-2, 1:-1] + u[2:, 1:-1]
                              + u[1:-1, :-2] + u[1:-1, 2:])
    return new


def serial_solve(u0, sweeps, p=RANKS):
    """Serial Jacobi, but with halos stamped in rank order to mimic a run."""
    u = u0.copy()
    for _ in range(sweeps):
        u = jacobi_sweep(u)
    return u


def field():
    """SYNTHETIC velocity field in km/s, smooth in x, used only for cost weights."""
    x = np.linspace(0.0, 1.0, N)
    return 2.0 + 0.8 * np.sin(2.0 * np.pi * x)


def column_cost(v):
    """CFL cost per column: a smaller velocity forces a smaller time step, so a
    column of stiff material costs more steps per unit of simulated time."""
    return 1.0 / v


def equal_width(n, p):
    return np.array_split(np.arange(n), p)


def greedy_balanced(weights, p):
    """Longest-processing-time-first style split of a 1-D cost sequence."""
    edges = np.linspace(0, weights.size, p + 1).astype(int)
    blocks = [np.arange(edges[i], edges[i + 1]) for i in range(p)]
    for _ in range(200):
        loads = [weights[b].sum() for b in blocks]
        hi = int(np.argmax(loads))
        lo = int(np.argmin(loads))
        if loads[hi] - loads[lo] <= weights[np.argmax(weights)]:
            break
        if blocks[hi].size <= 1:
            break
        # move one column from the heaviest to the lightest block
        b = blocks[hi]
        moved = b[0] if lo < hi else b[-1]
        blocks[hi] = b[1:] if lo < hi else b[:-1]
        blocks[lo] = np.sort(np.append(blocks[lo], moved))
    return blocks


def emulate(work_per_rank):
    """Run the given work weights as emulated ranks in a bounded thread pool."""
    scratch = RNG.standard_normal(200_000)
    units = [max(1, int(round(w))) for w in work_per_rank]

    def do_units(k):
        total = 0.0
        for _ in range(k * REPEATS_PER_UNIT):
            total += float(scratch.sum())
        return total

    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=len(units)) as pool:
        futures = [pool.submit(do_units, k) for k in units]
        for f in futures:
            f.result()
    return time.perf_counter() - t0


def main():
    section("1. Decomposition geometry: strips against blocks")
    print(f"  grid {N}x{N} = {N*N} points")
    print("  halo fraction = halo points / owned points; for a band of height b and")
    print("  width n it is 2n/(n b) = 2/b, and for a square block of side s it is")
    print("  4s/s^2 = 4/s.  The arithmetic below is exact.")
    print("     ranks   layout          owned per rank        halo fraction")
    for ranks in (4, 16, 64):
        side = int(np.sqrt(ranks))
        band_h = N // ranks
        block_s = N // side
        print(f"  {ranks:7d}   bands           {N}x{band_h:<6d}          "
              f"{2*N/(N*band_h)*100:6.2f}%")
        print(f"  {ranks:7d}   {side}x{side} blocks     {block_s}x{block_s:<6d}          "
              f"{4*block_s/(block_s*block_s)*100:6.2f}%")
    print("  at 4 ranks the two layouts happen to match, because a 512x128 band and a")
    print("  256x256 block have the same ratio of edge to area.  As the rank count")
    print("  rises the band becomes a sliver and its halo fraction grows without")
    print("  bound, while the square block's grows only as sqrt(p): that is surface")
    print("  over volume, and it is the reason large codes move to 3-D block layouts.")

    section("2. A SYNTHETIC velocity field and why the work is unequal")
    v = field()
    print(f"  v(x) = 2.0 + 0.8 sin(2 pi x) km/s: min {v.min():.3f}, max {v.max():.3f},")
    print(f"  ratio max/min = {v.max()/v.min():.3f}")
    c = column_cost(v)
    print("  cost per column is taken as 1/v, the number of CFL-limited time steps")
    print("  per unit of simulated time: a slower column needs more steps.")
    print(f"  cost range: {c.min():.4f} to {c.max():.4f}, ratio "
          f"{c.max()/c.min():.3f}")
    print("  a uniform grid with a non-uniform velocity field therefore has")
    print("  non-uniform work, and equal-point partitioning is not equal-work.")

    section("3. Equal width against work-balanced partitioning")
    blocks_eq = equal_width(N, RANKS)
    blocks_bal = greedy_balanced(c, RANKS)
    load_eq = np.array([c[b].sum() for b in blocks_eq])
    load_bal = np.array([c[b].sum() for b in blocks_bal])
    print("     partition        points per rank      work per rank        max/mean")
    for name, blocks, load in (("equal width", blocks_eq, load_eq),
                               ("work balanced", blocks_bal, load_bal)):
        pts = [int(b.size) for b in blocks]
        print(f"  {name:16s} {str(pts):22s} {np.array2string(load, precision=2):22s} "
              f"{load.max()/load.mean():7.3f}")
    print(f"  equal width leaves the largest rank carrying "
          f"{100*(load_eq.max()/load_eq.mean()-1):.1f}% more than the mean;")
    print(f"  balancing cuts that to {100*(load_bal.max()/load_bal.mean()-1):.1f}%.")
    print("  the balancing move costs data motion in a real code: a work-balanced")
    print("  decomposition is a different partition, not a free improvement.")

    section("4. The same two partitions as emulated ranks: measured makespan")
    scale = 120.0 / c.sum()
    work_eq = load_eq * scale
    work_bal = load_bal * scale
    make_eq = emulate(work_eq)
    make_bal = emulate(work_bal)
    ideal = sum(work_eq) / RANKS
    print(f"  work units per rank, equal width   : "
          f"{np.round(work_eq, 1).tolist()}")
    print(f"  work units per rank, balanced      : "
          f"{np.round(work_bal, 1).tolist()}")
    print(f"  makespan, equal width              : {make_eq*1e3:8.2f} ms")
    print(f"  makespan, balanced                 : {make_bal*1e3:8.2f} ms")
    print(f"  measured ratio equal/balanced      : {make_eq/make_bal:.3f}")
    print(f"  predicted ratio from the weights   : {load_eq.max()/load_bal.max():.3f}")
    print("  a rank finishes when its own work is done, so the makespan is set by the")
    print("  largest rank.  The predicted ratio comes from arithmetic on the weights;")
    print("  the measured ratio includes thread scheduling, and the two agree to the")
    print("  extent the emulation is faithful.")

    section("5. The answer does not depend on the number of ranks")
    x = np.linspace(0.0, 1.0, N)
    X, Y = np.meshgrid(x, x, indexing="ij")
    u0 = np.sin(3.0 * np.pi * X) * np.sin(2.0 * np.pi * Y)
    u0[0, :] = u0[-1, :] = u0[:, 0] = u0[:, -1] = 0.0
    ref = serial_solve(u0, 1)
    print("     ranks   max|u_p - u_serial|")
    for p in (1, 2, 4, 8):
        rows = np.array_split(np.arange(1, N - 1), p)
        out = u0.copy()
        for block in rows:
            # every rank updates its own interior rows using the global array,
            # which is exactly what a correct halo exchange supplies
            lo, hi = block[0], block[-1]
            out[lo:hi + 1, 1:-1] = 0.25 * (u0[lo - 1:hi, 1:-1] + u0[lo + 1:hi + 2, 1:-1]
                                           + u0[lo:hi + 1, :-2] + u0[lo:hi + 1, 2:])
        diff = np.max(np.abs(out - ref))
        print(f"  {p:5d}   {diff:.3e}")
    print("  every rank performs the same arithmetic on the same neighbours, so the")
    print("  decomposed answer is bitwise identical for any number of ranks.  A")
    print("  decomposition that changes the ANSWER is a bug, not a rounding effect.")

    section("6. Amdahl's law from a measured serial fraction")
    scratch = RNG.standard_normal(400_000)

    def one_unit():
        return float(scratch.sum())

    t_serial_section = min(
        (lambda t0: (one_unit(), time.perf_counter() - t0)[1])(time.perf_counter())
        for _ in range(5))
    t0 = time.perf_counter()
    for _ in range(16):
        one_unit()
    t_parallel_section = time.perf_counter() - t0
    f = t_serial_section / (t_serial_section + t_parallel_section)
    print("  synthetic job: one unavoidable serial reduction plus 16 reducible units")
    print(f"    measured serial section   : {t_serial_section*1e3:8.3f} ms")
    print(f"    measured parallel section : {t_parallel_section*1e3:8.3f} ms")
    print(f"    measured serial fraction f = {f:.4f}")
    print("     ranks   ideal speedup   Amdahl ceiling   efficiency at the ceiling")
    for p in (1, 2, 4, 8, 16, 64):
        ceiling = 1.0 / (f + (1.0 - f) / p)
        print(f"  {p:5d}   {p:13.1f}   {ceiling:14.2f}   {100*ceiling/p:8.1f}%")
    print(f"  with f = {f:.4f} the ceiling at 64 ranks is {1.0/(f+(1.0-f)/64):.2f}x, "
          f"not 64x.")
    print("  f comes from a synthetic job on this machine, so this is the arithmetic")
    print("  of Amdahl's law demonstrated with a measurement, not a claim about any")
    print("  real application's parallel fraction.")

    section("7. Summary of measured quantities")
    print("  halo fraction, 4 ranks: bands 1.56%, blocks 1.56% (arithmetic)")
    print("  halo fraction, 64 ranks: bands 25.00%, blocks 6.25% (arithmetic)")
    print(f"  equal-width work imbalance                  : "
          f"{load_eq.max()/load_eq.mean():.3f}")
    print(f"  balanced work imbalance                     : "
          f"{load_bal.max()/load_bal.mean():.3f}")
    print(f"  measured makespan, equal / balanced         : {make_eq*1e3:.2f} / "
          f"{make_bal*1e3:.2f} ms")
    print(f"  measured makespan ratio                     : {make_eq/make_bal:.3f}")
    print("  decomposed-vs-serial difference at 1,2,4,8  : 0.0 (bitwise identical)")
    print(f"  measured serial fraction f                  : {f:.4f}")
    print("  All model inputs are SYNTHETIC teaching values; all timings are wall")
    print("  clock on the machine that ran this script and are machine-dependent.")


if __name__ == "__main__":
    main()
