#!/usr/bin/env python3
"""Big-data patterns: partitioning, chunking, out-of-core work on a SYNTHETIC grid.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python big_data_patterns_demo.py

Everything here is SYNTHETIC.  The grid shape, partitions and memory budgets are
chosen teaching values; no array is written to disk and no cluster was used.

Sections
--------
1. A field too large for memory: how many passes a chunked algorithm needs.
2. Partition skew: the cost of an unbalanced key, with the tail measured.
3. Partition size versus task overhead: the small-file problem quantified.
4. Out-of-core shuffles: what a group-by by station costs when it does not fit.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC data and model (chosen, not measured) ------------------------
NX, NY, NZ = 4096, 4096, 64        # grid cells
DTYPE_BYTES = 4                    # float32
MEMORY_GB = 16.0                   # available memory
TASK_OVERHEAD_S = 3.0              # per-partition task overhead
N_STATIONS = 1200
STATION_EVENTS = 250_000           # total rows to group by station


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. A field too large for memory")
    total_gb = NX * NY * NZ * DTYPE_BYTES / 1e9
    chunk_gb = 512 * 512 * NZ * DTYPE_BYTES / 1e9
    print(f"SYNTHETIC field: {NX} x {NY} x {NZ} float32 = {total_gb:.1f} GB "
          f"(chosen)")
    print(f"  memory budget = {MEMORY_GB:.0f} GB, chunk = 512 x 512 x {NZ} = "
          f"{chunk_gb * 1000:.1f} MB")
    passes = int(np.ceil(total_gb / (MEMORY_GB * 0.5)))
    print(f"  single-pass algorithms fit only if the field is under "
          f"~{MEMORY_GB / 2:.0f} GB")
    print(f"  in-place reductions need {passes} pass(es) over the chunks")
    print(f"  a global statistic (a mean) accumulates in one pass; a global")
    print(f"  *order* statistic (a median) cannot, and needs either two passes")
    print(f"  or a reservoir/binning approximation")
    print("  -> decide which statistics you need before choosing the chunk loop,")
    print("     because order statistics set the number of passes")

    section("2. Partition skew")
    print("  synthetic station event counts, modelled as lognormal (chosen)")
    counts = RNG.lognormal(mean=np.log(STATION_EVENTS / N_STATIONS), sigma=1.2,
                           size=N_STATIONS).astype(int)
    total = counts.sum()
    share = np.sort(counts)[::-1] / total
    for k in (1, 5, 10):
        print(f"  top {k:>2d} stations hold {100 * share[:k].sum():>5.1f} % of "
              f"the rows")
    mean = total / N_STATIONS
    print(f"  mean rows per station = {mean:.0f}, largest = {counts.max():.0f} "
          f"({counts.max() / mean:.1f}x the mean)")
    print(f"  partition-by-station: largest task is {counts.max() / mean:.1f}x the")
    print(f"  average, so wall time is set by one station unless the key is")
    print(f"  rebalanced (hash the station, or split the largest by time)")

    section("3. Partition size versus task overhead")
    print("  partitions | rows/partition | overhead (s) | data (GB) | total (s)")
    rows = 20_000_000
    for n_parts in (4, 64, 1024, 16384):
        per = rows / n_parts
        overhead = n_parts * TASK_OVERHEAD_S
        data_s = rows * 120 / 1e9 * 4        # ~4 s per GB
        print(f"  {n_parts:>10d} | {per:>14.0f} | {overhead:>12.1f} | "
              f"{rows * 120 / 1e9:>9.3f} | {overhead + data_s:>9.1f}")
    print("  -> overhead is linear in the partition count and data time is not;")
    print("     the partition count is chosen where the two cross, which is far")
    print("     below 'one partition per key' for a high-cardinality key")

    section("4. Out-of-core group-by")
    bytes_per_row = 120
    hash_bytes = STATION_EVENTS * 32
    print(f"  {STATION_EVENTS:,} rows of {bytes_per_row} B = "
          f"{STATION_EVENTS * bytes_per_row / 1e6:.1f} MB (fits in memory)")
    print(f"  hash table for {N_STATIONS} groups = "
          f"{N_STATIONS * 256 / 1e6:.2f} MB (negligible)")
    big_rows = 2_000_000_000
    print(f"  {big_rows:,} rows = {big_rows * bytes_per_row / 1e9:.0f} GB "
          f"(does not fit)")
    print(f"  plan: partition by hash of the key, aggregate per partition, then")
    print(f"  merge {N_STATIONS} partial states")
    print(f"  spill traffic ≈ 2x the data volume = "
          f"{2 * big_rows * bytes_per_row / 1e9:.0f} GB of I/O")
    print("  -> out-of-core is a scheduling problem: the shuffle's I/O is what")
    print("     the pipeline pays, and it is twice the data volume in the worst")
    print("     case (write the partition, read it back)")


if __name__ == "__main__":
    main()
