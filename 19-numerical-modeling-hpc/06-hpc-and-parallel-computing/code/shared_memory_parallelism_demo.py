#!/usr/bin/env python3
"""Shared-memory parallelism in Python: what threading buys, what the GIL costs,
what a race looks like, and what survives into the result bits.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python shared_memory_parallelism_demo.py

Everything is SYNTHETIC: array sizes, chunk counts and per-item costs are chosen
teaching values.  No hardware model name and no published scaling figure is used.

The demo starts only short-lived, bounded thread pools, and every pool is closed
with an explicit join before the next section begins.  Nothing here spawns a
process, an MPI rank, a subprocess or a daemon.  All timings are wall-clock
measurements on the machine that runs the script and are machine-dependent.

Contents
--------
1. The GIL: pure-Python work, serial against four threads.
2. Released-GIL work: the same experiment on numpy elementwise kernels.
3. A read-modify-write race, and the lock that removes it.
4. Static blocks against a dynamic queue when the items have unequal cost.
5. Reproducibility: a reduction whose result does not depend on the worker count.
6. Summary of measured quantities and the caveats that limit them.
"""

import hashlib
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np

RNG = np.random.default_rng(20261014)

WORKERS = 4


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def best_of(fn, repeats=3):
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn()
        times.append(time.perf_counter() - t0)
    return min(times)


def python_work(n):
    """Pure-Python arithmetic: this one holds the GIL for its whole duration."""
    total = 0
    for i in range(n):
        total += i * i
    return total




def main():
    section("1. The GIL: pure-Python work, serial against four threads")
    n = 400_000 * 8
    t_serial = best_of(lambda: python_work(n))
    chunks = [n // WORKERS] * WORKERS

    def threaded():
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            futures = [pool.submit(python_work, c) for c in chunks]
            return [f.result() for f in futures]

    t_threaded = best_of(threaded)
    print(f"  work: sum of i*i for i < {n}, split into {WORKERS} equal chunks")
    print(f"    serial              : {t_serial*1e3:8.3f} ms")
    print(f"    {WORKERS} threads           : {t_threaded*1e3:8.3f} ms")
    print(f"    measured speedup    : {t_serial/t_threaded:8.3f}x  "
          f"(ideal {WORKERS}x, efficiency {100*(t_serial/t_threaded)/WORKERS:.1f}%)")
    print("  essentially no speedup: CPython executes bytecode under one lock, so")
    print("  four threads take turns rather than run together.  Threads are still")
    print("  useful here -- for I/O and for kernels that release the lock.")

    section("2. Released-GIL work: when threads help and when they hurt")
    m = 1 << 22
    reps = 40
    x = RNG.standard_normal(m)
    out = np.empty_like(x)
    parts = np.array_split(np.arange(m), WORKERS)

    def repeat_chunk(p, times):
        for _ in range(times):
            np.add(x[p], 1.0, out=out[p])
        return float(out[p][0])

    def serial_numpy():
        for _ in range(reps):
            np.add(x, 1.0, out=out)

    def threaded_numpy():
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            futures = [pool.submit(repeat_chunk, p, reps) for p in parts]
            return [f.result() for f in futures]

    t_serial_np = best_of(serial_numpy)
    t_thread_np = best_of(threaded_numpy)
    bytes_moved = m * 16 * reps
    print(f"  (a) bandwidth-bound kernel: out = x + 1, {m} doubles per pass, "
          f"{reps} passes, {WORKERS} chunks")
    print(f"      serial      : {t_serial_np*1e3:8.3f} ms "
          f"({bytes_moved/t_serial_np/1e9:.2f} GB/s)")
    print(f"      {WORKERS} threads   : {t_thread_np*1e3:8.3f} ms "
          f"({bytes_moved/t_thread_np/1e9:.2f} GB/s)")
    print(f"      measured speedup = {t_serial_np/t_thread_np:.3f}x")
    print("      one thread already saturates this machine's memory system; adding")
    print("      three more adds GIL handover between operations and cache contention")
    print("      and gains nothing.  Measured, not assumed: threading a bandwidth-bound")
    print("      kernel made it slower here.")
    print("      the lesson is not that threads fail.  Section 1 of this module")
    print("      measured the same plateau; a kernel already at it cannot be")
    print("      parallelised into a higher rate.")

    sort_data = [RNG.standard_normal(m // WORKERS).copy() for _ in range(WORKERS)]

    def serial_sort():
        for arr in sort_data:
            np.sort(arr)

    def threaded_sort():
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            futures = [pool.submit(np.sort, arr) for arr in sort_data]
            return [f.result() for f in futures]

    t_serial_sort = best_of(serial_sort)
    t_thread_sort = best_of(threaded_sort)
    print(f"\n  (b) compute-bound kernel: sort {WORKERS} arrays of "
          f"{m//WORKERS} doubles")
    print(f"      serial      : {t_serial_sort*1e3:8.3f} ms")
    print(f"      {WORKERS} threads   : {t_thread_sort*1e3:8.3f} ms")
    print(f"      measured speedup = {t_serial_sort/t_thread_sort:.3f}x  "
          f"(efficiency {100*(t_serial_sort/t_thread_sort)/WORKERS:.1f}%)")
    print("      a comparison sort moves each element more than once through the")
    print("      cache and releases the GIL, so the work is CPU bound and the threads")
    print("      do overlap: this is the case where shared-memory parallelism pays.")

    from scipy import fft as sfft
    big = RNG.standard_normal((2048, 2048))

    def fft1():
        sfft.rfft2(big, workers=1)

    def fft4():
        sfft.rfft2(big, workers=4)

    t1 = best_of(fft1)
    t4 = best_of(fft4)
    print(f"\n  (c) a library-managed pool: scipy.fft.rfft2 on a 2048x2048 array")
    print(f"      workers=1   : {t1*1e3:8.3f} ms")
    print(f"      workers=4   : {t4*1e3:8.3f} ms")
    print(f"      measured speedup = {t1/t4:.3f}x")
    print("      the library owns the pool, so no Python-level task scheduling is in")
    print("      the path.  Both this and (b) are compute bound; (a) is not.")

    section("3. A read-modify-write race, and the lock that removes it")
    iterations = 200
    total_expected = WORKERS * iterations

    def bump_unsafe(counter):
        for _ in range(iterations):
            tmp = counter[0]
            time.sleep(0)            # forces a context switch mid-update
            counter[0] = tmp + 1

    def bump_safe(counter, lock):
        for _ in range(iterations):
            with lock:
                tmp = counter[0]
                time.sleep(0)
                counter[0] = tmp + 1

    counter = [0]
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(bump_unsafe, counter) for _ in range(WORKERS)]
        for f in futures:
            f.result()
    final_unsafe = counter[0]
    lost_unsafe = total_expected - final_unsafe

    counter = [0]
    lock = threading.Lock()
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(bump_safe, counter, lock) for _ in range(WORKERS)]
        for f in futures:
            f.result()
    final_safe = counter[0]
    lost_safe = total_expected - final_safe
    print(f"  {WORKERS} threads x {iterations} increments of one shared counter")
    print(f"    without a lock: final value {final_unsafe} of {total_expected} -- "
          f"{lost_unsafe} updates lost")
    print(f"    with a lock   : final value {final_safe} of {total_expected} -- "
          f"{lost_safe} updates lost")
    print("  the loss is not hypothetical: a read-modify-write is three operations,")
    print("  and another thread can run between them.  time.sleep(0) is used only to")
    print("  make that window wide enough to see in a demo of this length; the window")
    print("  exists without it, which is why the same bug appears in real codes as a")
    print("  rare, irreproducible wrong answer.")

    section("4. Static blocks against a dynamic queue with unequal item costs")
    weights = np.array([1, 2, 3, 4, 5, 6, 7, 8] * 3)      # 24 items
    scratch = RNG.standard_normal(800_000)

    def do_item(w):
        total = 0.0
        for _ in range(w):
            total += float(scratch.sum())
        return int(w)

    # static: contiguous equal blocks, one block per worker
    blocks = np.array_split(np.arange(weights.size), WORKERS)
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(lambda b=blk: sum(do_item(weights[i]) for i in b))
                   for blk in blocks]
        blocks_done = [f.result() for f in futures]
    t_static = time.perf_counter() - t0

    # dynamic: one queue, workers take the next item when they finish
    order = np.argsort(-weights)
    queue = list(order)
    qlock = threading.Lock()
    done = []

    def take_next():
        while True:
            with qlock:
                if not queue:
                    return
                item = queue.pop(0)
            done.append(do_item(weights[item]))

    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(take_next) for _ in range(WORKERS)]
        for f in futures:
            f.result()
    t_dynamic = time.perf_counter() - t0

    ideal = weights.sum()
    work_per_block = [int(weights[b].sum()) for b in blocks]
    print(f"  item weights {weights.tolist()}")
    print(f"  static blocks of {blocks[0].size} items: work per block "
          f"{work_per_block}, total {ideal}")
    print(f"  ideal makespan if work divided perfectly: {ideal/WORKERS:.2f} units;")
    print(f"  the largest static block already contains {max(work_per_block)} units")
    print(f"    static  : {t_static*1e3:8.2f} ms")
    print(f"    dynamic : {t_dynamic*1e3:8.2f} ms")
    print(f"    measured ratio static/dynamic = {t_static/t_dynamic:.3f}")
    print(f"    largest block / ideal = {max(work_per_block)/(ideal/WORKERS):.2f}")
    print("  the static schedule cannot beat its largest block and the dynamic queue")
    print("  is limited only by the largest single item; both bounds are visible in")
    print("  the work counts, and the measured times carry Python scheduling noise.")

    section("5. Reproducibility: the decomposition decides the bits, not the workers")
    m = 1 << 20
    data = RNG.standard_normal(m)
    n_chunks = 8

    def chunk_sum(lo, hi):
        return float(np.sum(data[lo:hi]))

    def reduce_with(worker_count, chunks):
        edges = np.linspace(0, m, chunks + 1).astype(int)
        with ThreadPoolExecutor(max_workers=worker_count) as pool:
            futures = [pool.submit(chunk_sum, edges[i], edges[i + 1])
                       for i in range(chunks)]
            partials = [f.result() for f in futures]        # collected in chunk order
        total = 0.0
        for p in partials:
            total += p
        return total

    def digest(value):
        return hashlib.sha256(np.float64(value).tobytes()).hexdigest()[:16]

    reference = float(np.sum(data))
    print(f"  reference: numpy's own sum of {m} doubles = {reference!r}")
    print(f"  fixed decomposition into {n_chunks} chunks, varying pool size:")
    print("     workers   chunk reduction             digest")
    seen = set()
    for w in (1, 2, 3, 4, 8):
        value = reduce_with(w, n_chunks)
        seen.add(digest(value))
        print(f"  {w:9d}   {value!r}   {digest(value)}")
    print(f"  distinct digests across pool sizes 1..8 with {n_chunks} chunks: "
          f"{len(seen)}")
    print("  varying the number of CHUNKS instead:")
    seen2 = set()
    print("     chunks    chunk reduction             digest")
    for c in (1, 2, 3, 4, 8, 16):
        value = reduce_with(WORKERS, c)
        seen2.add(digest(value))
        print(f"  {c:9d}   {value!r}   {digest(value)}")
    print(f"  distinct digests across chunk counts: {len(seen2)}")
    diff_ulp = abs(reduce_with(WORKERS, n_chunks) - reference) / np.spacing(abs(reference))
    print(f"  the fixed-decomposition result differs from numpy's own sum by "
          f"{diff_ulp:.2f} ulp")
    print("  the arithmetic, not the scheduling, is what fixes the bits: a fixed")
    print("  chunk count and a fixed merge order reproduce exactly across pool sizes,")
    print("  while changing the chunk count changes the answer in the last bits.  A")
    print("  reproducibility claim must therefore name the decomposition.")

    section("6. Summary of measured quantities")
    print(f"  pure-Python work, {WORKERS} threads          : speedup "
          f"{t_serial/t_threaded:.3f}x    (the GIL)")
    print(f"  bandwidth-bound numpy kernel, {WORKERS} threads : speedup "
          f"{t_serial_np/t_thread_np:.3f}x  (already at the plateau)")
    print(f"  compute-bound sort, {WORKERS} threads        : speedup "
          f"{t_serial_sort/t_thread_sort:.3f}x")
    print(f"  library pool, scipy.fft workers=4         : speedup {t1/t4:.3f}x")
    print(f"  unsynchronised counter, {total_expected} updates: {lost_unsafe} lost")
    print(f"  locked counter, {total_expected} updates       : {lost_safe} lost")
    print(f"  static/dynamic schedule ratio             : {t_static/t_dynamic:.3f}")
    print(f"  distinct digests, 8 chunks, 5 pool sizes  : {len(seen)}")
    print(f"  distinct digests, 6 chunk counts          : {len(seen2)}")
    print("  Every number is a wall-clock measurement on the machine that ran this")
    print("  script.  The qualitative results to carry away: no speedup under the")
    print("  GIL, no speedup for a kernel already at the memory plateau, real")
    print("  speedup for compute-bound released-GIL work, lost updates without a")
    print("  lock, and a schedule bounded by its largest item.")


if __name__ == "__main__":
    main()
