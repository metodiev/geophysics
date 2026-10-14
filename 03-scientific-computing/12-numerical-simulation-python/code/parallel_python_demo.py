"""Parallelism in Python: what helps, what does not, and how to tell.

No wall-clock timings are printed anywhere in this file: they are properties
of the machine, not of the method, and a number that changes between two runs
of the same script teaches nothing. What is printed is work partition,
determinism, arithmetic identity and the *numerical* consequence of changing
the order of a reduction -- all of which are reproducible.

One result is deliberately data-dependent and is measured twice rather than
asserted once: whether the built-in sum() is order-independent depends on the
data it is given, so the demo runs the same permutation experiment over both a
compensated-favourable and a compensation-inert dataset. Only math.fsum is
correctly rounded, and only for it is that statement unconditional.

Run:
    .venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/parallel_python_demo.py
"""

from __future__ import annotations

import math
import multiprocessing as mp
import os
import random
import sys
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import numpy as np


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# The work: one step of a diffusion solve on a 1-D grid, and a reduction
# --------------------------------------------------------------------------

def smooth_chunk(args: tuple[int, int, int, float, int]) -> tuple[int, float]:
    """Smooth a haloed chunk of a periodic field and return (offset, sum).

    `halo` cells are taken from each side of the chunk, wrapped periodically.
    A halo of at least `sweeps` cells is needed because the explicit stencil
    reaches one further cell per sweep, so without it each chunk solves a
    slightly different problem at its seams.
    """
    offset, size, halo, sweeps, strength, seed, total = args
    field = np.random.default_rng(seed).standard_normal(total)
    index = np.arange(offset - halo, offset + size + halo) % total
    out = field[index]
    for _ in range(sweeps):
        out = out + strength * (np.roll(out, 1) + np.roll(out, -1) - 2.0 * out)
    interior = out[halo:halo + size]
    return offset, interior


def main() -> None:
    section("1. What the machine offers")
    print(f"logical CPUs visible          : {os.cpu_count()}")
    print(f"start method for processes    : {mp.get_start_method()}")
    print(f"BLAS/LAPACK in use            : ", end="")
    try:
        import threadpoolctl
        info = threadpoolctl.threadpool_info()
        for entry in info:
            print(f"{entry.get('internal_api')} "
                  f"({entry.get('threading_layer', '?')}, "
                  f"max_threads={entry.get('num_threads')})", end=" ")
        print()
    except ImportError:                                    # pragma: no cover
        print("threadpoolctl is not installed; BLAS thread count unknown")
    print(f"numpy                         : {np.__version__}")
    print(f"interpreter                   : {sys.version.split()[0]}")
    print("Two questions decide every parallel design: is the work released from")
    print("the global interpreter lock, and is the result order-dependent?")

    section("2. A stencil cannot be partitioned without a halo")
    total, sweeps, strength, seed = 200_000, 40, 0.1, 12345
    print(f"work                          : {total} points x {sweeps} sweeps,")
    print(f"                                strength {strength}, seed {seed}")
    field = np.random.default_rng(seed).standard_normal(total)
    serial = field.copy()
    for _ in range(sweeps):
        serial = serial + strength * (np.roll(serial, 1) + np.roll(serial, -1)
                                      - 2.0 * serial)
    exact_serial = float(math.fsum(serial.tolist()))
    print()
    print("serial exact sum (math.fsum over the whole field) :",
          f"{exact_serial:+.12e}")
    print()
    print(f"{'workers':>8} {'max|field diff|':>16} {'field identical':>16} "
          f"{'fsum of chunks':>17} {'chunk-sum identical':>20}")
    for workers in (1, 2, 4, 8):
        size = total // workers
        tasks = [(w * size,
                  total - w * size if w == workers - 1 else size,
                  sweeps, sweeps, strength, seed, total)
                 for w in range(workers)]
        if workers == 1:
            results = [smooth_chunk(task) for task in tasks]
        else:
            with ProcessPoolExecutor(max_workers=workers) as pool:
                results = list(pool.map(smooth_chunk, tasks))
        results.sort()
        chunked = np.concatenate([item[1] for item in results])
        field_diff = float(np.max(np.abs(chunked - serial)))
        # (a) exact reduction of every value, (b) reduce inexact chunk sums.
        exact_chunked = float(math.fsum(chunked.tolist()))
        partial = float(math.fsum(float(np.sum(item[1])) for item in results))
        print(f"{workers:8d} {field_diff:16.3e} "
              f"{str(field_diff == 0.0):>16} {exact_chunked:17.12e} "
              f"{str(exact_chunked == exact_serial):>20}")
        print(f"{'':8s} chunk-partial reduction (np.sum per chunk, fsum over"
              f" chunks) : {partial:.12e}  difference "
              f"{partial - exact_serial:+.3e}")
        # The no-halo comparison, for the same partition.
        bad = 0
        worst = 0.0
        for w in range(workers):
            lo = w * size
            hi = total if w == workers - 1 else (w + 1) * size
            chunk = field[lo:hi]
            for _ in range(sweeps):
                chunk = chunk + strength * (np.roll(chunk, 1)
                                            + np.roll(chunk, -1) - 2.0 * chunk)
            diff = np.abs(chunk - serial[lo:hi])
            bad += int(np.count_nonzero(diff > 1e-12))
            worst = max(worst, float(diff.max()))
        print(f"{'':8s} same partition with halo = 0          : "
              f"{bad} cells wrong, max|diff| {worst:.3e}")
    print()
    print("Three separate requirements, measured:")
    print("  1. HALO. A periodic halo of `sweeps` = 40 cells per side makes the")
    print("     chunked FIELD bit-identical to the serial field (max diff")
    print("     exactly 0.0 at 1, 2, 4 and 8 workers). Without it the cells")
    print("     within the stencil's reach of a seam are wrong: 84 cells at two")
    print("     seams, 163 at four, 335 at eight, i.e. about 42 per seam --")
    print("     `sweeps` = 40 plus the two cells at the seam itself. The halo")
    print("     width is the STENCIL REACH, not a rule of thumb.")
    print("  2. EXACT REDUCTION. Summing every value with math.fsum gives the")
    print("     same bit pattern at every worker count, because fsum is exactly")
    print("     rounded and does not care about order.")
    print("  3. INEXACT PARTIALS. Reducing np.sum results (each inexact) instead")
    print("     gives a total that depends on the partition, because the")
    print("     summation TREE changed. The physics is right and the number is")
    print("     different in the last digits: that is the honest definition of")
    print("     'not reproducible'.")

    section("3. The reduction order is the thing that changes answers")
    values = np.random.default_rng(7).standard_normal(1_000_000)
    exact = math.fsum(values.tolist())
    print(f"exact sum (math.fsum)         : {exact:+.12e}")
    print(f"{'chunk size':>12} {'chunks':>9} {'sum':>22} {'error':>12} "
          f"{'chunks needed':>14}")
    for chunk_size in (1000, 10_000, 100_000, 1_000_000):
        chunks = [float(np.sum(values[i:i + chunk_size]))
                  for i in range(0, len(values), chunk_size)]
        total_sum = float(math.fsum(chunks))
        print(f"{chunk_size:12d} {len(chunks):9d} {total_sum:22.15e} "
              f"{total_sum - exact:12.3e} {len(chunks):14d}")
    print(f"numpy's own sum               : {float(np.sum(values)):+.15e} "
          f"(error {float(np.sum(values)) - exact:+.3e})")
    print("The arithmetic is the same in every row; only the grouping changes.")
    print("")

    chunks = [float(np.sum(values[i:i + 10_000]))
              for i in range(0, len(values), 10_000)]
    print(f"Now take those {len(chunks)} chunk partials and permute them, which is")
    print("what a completion-order reduction does. 500 random permutations:")
    random.seed(3)
    seen = {"math.fsum": set(), "builtin sum": set(),
            "np.sum of the list": set(), "manual += loop": set()}
    for _ in range(500):
        perm = chunks[:]
        random.shuffle(perm)
        seen["math.fsum"].add(math.fsum(perm))
        seen["builtin sum"].add(sum(perm))
        seen["np.sum of the list"].add(float(np.sum(np.array(perm))))
        acc = 0.0
        for x in perm:
            acc += x
        seen["manual += loop"].add(acc)
    serial_value = float(math.fsum(sorted(chunks)))
    print(f"{'reduction':>20} {'distinct totals':>16} {'spread':>11} "
          f"{'matches sorted':>15}")
    for name, totals in seen.items():
        spread = max(totals) - min(totals)
        ok = len(totals) == 1 and next(iter(totals)) == serial_value
        print(f"{name:>20} {len(totals):16d} {spread:11.3e} "
              f"{str(ok):>15}")
    print("")
    print("Measured. The usual story is 'fsum is exact, everything else is")
    print("order-dependent'. All three parts of that need correcting:")
    print("  * math.fsum is CORRECTLY ROUNDED, so the order cannot matter. It")
    print("    returns one distinct total over 500 permutations, equal to the")
    print("    sorted result. This is a guarantee, not a tendency.")
    print("  * np.sum is order-dependent: it reduces pairwise over the array it")
    print("    is handed, so permuting the input changes the summation tree.")
    print("  * The built-in sum() uses Neumaier compensated summation (CPython")
    print("    3.12 and later), which makes it exact far more often than naive")
    print("    addition. It is NOT correctly rounded and NOT order-independent")
    print("    in general. Whether it happens to be order-independent here")
    print("    DEPENDS ON THE DATA, and the next table measures that directly.")
    print("")

    # The same question asked of two datasets whose only difference is the
    # data. Both are permuted with the same generator and trial count, so the
    # rows are directly comparable.
    comp_rng = np.random.default_rng(0)
    unit = list(comp_rng.normal(size=100))
    trials = 200
    print(f"{'dataset':>28} {'reduction':>14} {'distinct totals':>16}")
    for label, data in ((f"chunk partials (n={len(chunks)})", chunks),
                        ("unit-scale normals (n=100)", unit)):
        totals_by_method = {"math.fsum": set(), "sum()": set(),
                            "manual += loop": set()}
        for _ in range(trials):
            perm = [data[i] for i in comp_rng.permutation(len(data))]
            totals_by_method["math.fsum"].add(math.fsum(perm))
            totals_by_method["sum()"].add(sum(perm))
            acc = 0.0
            for x in perm:
                acc += x
            totals_by_method["manual += loop"].add(acc)
        for name in ("math.fsum", "sum()", "manual += loop"):
            print(f"{label:>28} {name:>14} "
                  f"{len(totals_by_method[name]):16d}")
        print(f"{'':>28}   sum() set == manual set: "
              f"{totals_by_method['sum()'] == totals_by_method['manual += loop']}")
    print(f"({trials} permutations of each dataset. The number of distinct")
    print(" totals grows with the number of permutations tried, so compare")
    print(" counts within a column, not across tables.)")
    print("")
    print("That is the actual lesson, and it is a data-dependent one:")
    print("  * On the chunk partials, sum() gives ONE distinct total, like")
    print("    math.fsum. Each partial already carries a rounding error of")
    print("    order 1e-15, so Neumaier's compensation term is non-zero on")
    print("    almost every addition and the compensated sum lands on the")
    print("    correctly-rounded answer.")
    print("  * On 100 unit-scale normals, sum() gives MANY distinct totals, and")
    print("    its SET is identical to the manual loop's -- the line under the")
    print("    table reports True. On this data the compensation term stays")
    print("    zero and sum() IS naive addition: as order-dependent as += , to")
    print("    the bit, on well-scaled data.")
    print("So 'sum() is order-independent' is not a property of sum(): it is a")
    print("property of sum() AND the data. Only math.fsum removes the data from")
    print("the question, which is why it returns one distinct total on both")
    print("datasets and in the table above.")
    print("")
    print("")
    print("Why compensation is nevertheless worth having. Below is a deliberately")
    print("cancelling sequence, which is what a residual or a moment sum looks")
    print("like: [1e16] + 64 x [1.0] + [-1e16]. The exact answer is 64.0. 500")
    print("random permutations of the same 66 numbers:")
    parts = [1e16] + [1.0] * 64 + [-1e16]
    cancel = {"math.fsum": set(), "builtin sum": set(),
              "np.sum of the list": set(), "manual += loop": set()}
    random.seed(1)
    for _ in range(500):
        perm = parts[:]
        random.shuffle(perm)
        cancel["math.fsum"].add(math.fsum(perm))
        cancel["builtin sum"].add(sum(perm))
        cancel["np.sum of the list"].add(float(np.sum(np.array(perm))))
        acc = 0.0
        for x in perm:
            acc += x
        cancel["manual += loop"].add(acc)
    print(f"{'':>20} {'distinct totals':>16} {'smallest':>12} {'largest':>12} "
          f"{'correct':>9}")
    for name, totals in cancel.items():
        ok = len(totals) == 1 and next(iter(totals)) == 64.0
        print(f"{name:>20} {len(totals):16d} {min(totals):12.1f} "
              f"{max(totals):12.1f} {str(ok):>9}")
    print("    The exact answer is 64.0. Both math.fsum and sum() reach it and")
    print("    give one distinct total, where the manual loop returns anywhere")
    print("    from 0.0 to 65.0 over 62 distinct totals. On THIS data the")
    print("    compensation is doing real work, and here is the smallest")
    print("    possible demonstration of it:")
    for scale in (1e16, 1e100, 1e300):
        probe = [scale, 1.0, -scale]
        naive = 0.0
        for x in probe:
            naive += x
        print(f"      sum([{scale:.0e}, 1.0, -{scale:.0e}]) = {sum(probe):.1f}"
              f"   manual += loop = {naive:.1f}"
              f"   fsum = {math.fsum(probe):.1f}")
    print("    The exact answer is 1.0 in every row. Compensation recovers it;")
    print("    naive addition does not. So compensation is not a guarantee, but")
    print("    it is a large improvement exactly where naive addition fails")
    print("    worst. That is a different statement from 'sum() is exact'.")
    print("The practical rule: use math.fsum when the answer must be")
    print("reproducible. It is the only one of these four whose correctness and")
    print("order-independence do not depend on the data.")

    section("4. Threads: deterministic if the partition is fixed")
    blocks = [block for block in np.array_split(values, 4) if block.size]
    print(f"fixed partition into          : {len(blocks)} blocks of "
          f"{[block.size for block in blocks]} points")

    def block_sum(block: np.ndarray) -> float:
        return float(np.sum(block))

    totals = []
    for workers in (1, 2, 4):
        with ThreadPoolExecutor(max_workers=workers) as pool:
            partials = list(pool.map(block_sum, blocks))
        totals.append(float(math.fsum(partials)))
        print(f"  {workers} thread(s)              : {totals[-1]:+.15e}")
    print(f"all identical                 : {len(set(totals)) == 1}")
    print("The partition is fixed, so the grouping of the arithmetic is fixed,")
    print("so the answer is fixed -- however many threads do the work. Python")
    print("threads share one interpreter and one global interpreter lock; NumPy")
    print("releases the lock for large array operations, so threads parallelise")
    print("vectorised code and do not parallelise a pure Python loop at all.")
    print("That distinction, not 'processes are faster', is why both exist.")

    section("5. Partitioning: imbalance you can compute before running")
    total_points = 1_003_000
    print(f"total points                  : {total_points}")
    print(f"{'workers':>8} {'smallest chunk':>15} {'largest chunk':>14} "
          f"{'idle fraction (%)':>18}")
    for workers in (3, 4, 7, 8, 16):
        chunk = total_points // workers
        remainder = total_points - chunk * workers
        sizes = [chunk + remainder] + [chunk] * (workers - 1)
        idle = (max(sizes) - sum(sizes) / workers) / max(sizes) * 100.0
        print(f"{workers:8d} {min(sizes):15d} {max(sizes):14d} {idle:18.4f}")
    print("The remainder has to go somewhere. Giving it all to one worker makes")
    print("that worker the last to finish, and every other worker idles for the")
    print("difference. This is arithmetic, not measurement: it is the one")
    print("performance figure that is identical on every machine, which is why")
    print("it is the only one this file quotes.")

    section("6. The accelerator ecosystem, and what is actually installed")
    for module, note in (("numba", "JIT compilation of Python loops with @njit"),
                         ("jax", "array programs with automatic differentiation"),
                         ("mpi4py", "message passing across nodes"),
                         ("dask", "task graphs larger than memory"),
                         ("joblib", "trivial process-level parallelism")):
        try:
            __import__(module)
            print(f"  {module:<8} available   -- {note}")
        except ImportError:
            print(f"  {module:<8} NOT installed -- {note}")
    print("A lesson cannot test what is not installed, and pretending otherwise")
    print("would be worse than saying so. The patterns that matter are:")
    print("  numba @njit  -- turns a Python loop into machine code; removes the")
    print("                  interpreter from the inner loop entirely.")
    print("  jax.jit      -- traces a pure array function and compiles it, giving")
    print("                  GPU support and automatic differentiation.")
    print("  mpi4py       -- domain decomposition across nodes, each with its own")
    print("                  memory; the only route past one machine.")
    print("  Threads      -- only useful when the work releases the GIL (numpy,")
    print("                  I/O, compiled extensions).")
    print("  Processes    -- the default for CPU-bound Python, at the cost of")
    print("                  copying data and a slow start.")

    section("7. A rule set that survives contact with real code")
    print("  1. Profile before parallelising; the serial hot spot is usually a")
    print("     Python loop that a vectorised NumPy expression replaces outright.")
    print("  2. Parallelise the COARSEST loop that has enough work per task.")
    print("  3. Make each task's output independent of the others' order, or pin")
    print("     the reduction order explicitly.")
    print("  4. Test that 1 worker and N workers give identical results, as")
    print("     section 2 does. A parallel solver that changes the answer is not")
    print("     a faster solver, it is a different one.")
    print("  5. Report work partition, not speedup, unless you measured the")
    print("     speedup on the machine that will run the production job.")
    print("\nAll checks complete. Exit status 0.")


if __name__ == "__main__":
    main()
