#!/usr/bin/env python3
"""Relational databases: index cost models on a SYNTHETIC table.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python relational_databases_demo.py

Everything here is SYNTHETIC.  The table is described (not built), and the cost
model uses chosen page and row sizes; no database was queried.

Sections
--------
1. A table and its pages: rows, bytes, and how many pages a scan touches.
2. Selectivity versus access path: full scan, index lookup, and index scan.
3. B-tree depth and the cost of a point lookup.
4. Join strategies: nested loop against hash join, by table size.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC database model (chosen, not measured) ------------------------
N_ROWS = 5_000_000        # rows in the event table
ROW_BYTES = 120           # average row size
PAGE_BYTES = 8192         # page size
FANOUT = 200              # B-tree fan-out
SEQ_PAGE_MS = 0.02        # sequential page read, ms
RAND_PAGE_MS = 0.60       # random page read, ms (index scan / point lookup)
SCAN_RATE_MB_S = 400.0    # sequential scan throughput, MB/s
ID_WIDTH = 8              # index entry width in bytes (key + pointer)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. A table and its pages")
    rows_per_page = max(1, PAGE_BYTES // ROW_BYTES)
    pages = int(np.ceil(N_ROWS / rows_per_page))
    print(f"SYNTHETIC table: {N_ROWS:,} rows of {ROW_BYTES} B, "
          f"{PAGE_BYTES} B pages (chosen)")
    print(f"  rows per page = {rows_per_page}, table pages = {pages:,}")
    print(f"  table size = {N_ROWS * ROW_BYTES / 1e9:.2f} GB")
    print(f"  full scan cost = {pages * SEQ_PAGE_MS / 1000:.1f} s "
          f"(sequential reads)")
    print("  -> a scan is cheap per row only because it is sequential; it is the")
    print("     wrong tool when the query returns a small fraction of the table")

    section("2. Selectivity versus access path")
    print("  selectivity | rows returned | scan (s) | index lookup (s) | winner")
    for sel in (1e-5, 1e-4, 1e-3, 1e-2, 0.1):
        rows = max(1.0, sel * N_ROWS)
        scan_s = pages * SEQ_PAGE_MS / 1000
        leaf = int(np.ceil(rows / rows_per_page))
        index_s = (3 * RAND_PAGE_MS + leaf * RAND_PAGE_MS) / 1000
        winner = "index" if index_s < scan_s else "scan"
        print(f"  {sel:>11.0e} | {rows:>13.0f} | {scan_s:>8.1f} | "
              f"{index_s:>16.2f} | {winner}")
    print("  -> the access path is chosen by selectivity; a query planner is")
    print("     estimating this table, and a bad estimate chooses the wrong path")

    section("3. B-tree depth and point lookups")
    depth = int(np.ceil(np.log(N_ROWS) / np.log(FANOUT)))
    print(f"  B-tree fan-out {FANOUT}, {N_ROWS:,} rows -> depth {depth} levels")
    print(f"  pages touched per point lookup (root to leaf) = {depth + 1}")
    print(f"  index size = {N_ROWS * ID_WIDTH / 1e9:.2f} GB "
          f"({100 * N_ROWS * ID_WIDTH / (N_ROWS * ROW_BYTES):.0f} % of the table)")
    one = (depth + 1) * RAND_PAGE_MS / 1000
    print(f"  cost of one lookup = {one * 1000:.2f} ms against "
          f"{pages * SEQ_PAGE_MS / 1000:.1f} s for a scan")
    print("  -> the index is small and the depth is bounded, which is why a")
    print("     point lookup is thousands of times cheaper than a scan")

    section("4. Join strategies")
    right_rows = np.array([1e2, 1e3, 1e4, 1e5, 1e6, 1e7])
    print("  right rows | nested loop (s) | hash join (s) | winner")
    probe_s = N_ROWS * ROW_BYTES / 1e6 / SCAN_RATE_MB_S
    for r in right_rows:
        # nested loop: one index lookup on the left table per right-hand row
        nl = r * (depth + 1) * RAND_PAGE_MS / 1000
        # hash join: read the smaller side to build, then read the larger to probe
        build_s = r * ROW_BYTES / 1e6 / SCAN_RATE_MB_S
        hj = build_s + probe_s
        winner = "nested loop" if nl < hj else "hash join"
        print(f"  {r:>10.0f} | {nl:>15.2f} | {hj:>13.2f} | {winner}")
    print("  -> the smaller side is the one to build the hash on; the strategy")
    print("     choice is again a size estimate, not a preference")


if __name__ == "__main__":
    main()
