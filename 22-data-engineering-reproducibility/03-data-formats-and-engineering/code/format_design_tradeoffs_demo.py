#!/usr/bin/env python3
"""Format trade-offs: access patterns, chunking and compression, on a SYNTHETIC grid.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python format_design_tradeoffs_demo.py

Everything here is SYNTHETIC.  The grid shape, chunk shapes and query windows are
chosen teaching values; no file is written or read and no benchmark is quoted.

Sections
--------
1. One query, four layouts: bytes read for a window subset.
2. Chunk shape versus query shape: the overshoot factor.
3. Compression: what it buys for smooth and for noisy data.
4. Append cost: why a time series wants a different layout from a grid.
"""

import zlib

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC grid and query (chosen, not measured) ------------------------
NX, NY = 1024, 1024
WINDOW = 256                 # side of the square query window
DTYPE_BYTES = 4              # float32
CHUNKS = (256, 128, 64, 32)
READ_RATE_MB_S = 200.0       # storage bandwidth, MB/s (chosen)
OBJECT_REQUEST_MS = 20.0     # per-request latency of an object store (chosen)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def chunks_touched(window, chunk):
    """Expected number of chunks a 1-D window of `window` cells touches."""
    return window / chunk + 1.0


def main():
    section("1. One query, four layouts")
    full_bytes = NX * NY * DTYPE_BYTES
    window_bytes = WINDOW * WINDOW * DTYPE_BYTES
    print(f"SYNTHETIC grid: {NX} x {NY} float32 = {full_bytes / 1e6:.1f} MB; "
          f"query window {WINDOW} x {WINDOW} = {window_bytes / 1e3:.0f} kB "
          f"(chosen)")
    print("  layout            | bytes read (MB) | overshoot vs the window")
    row_major = WINDOW * NY * DTYPE_BYTES          # contiguous rows
    col_major = WINDOW * NX * DTYPE_BYTES          # contiguous columns
    print(f"  row-major scan    | {row_major / 1e6:>15.2f} | "
          f"{row_major / window_bytes:>25.1f}x")
    print(f"  column-major scan | {col_major / 1e6:>15.2f} | "
          f"{col_major / window_bytes:>25.1f}x")
    for chunk in CHUNKS:
        n_chunks = int(np.ceil(NX / chunk)) * int(np.ceil(NY / chunk))
        touched = chunks_touched(WINDOW, chunk) ** 2
        read = touched * chunk * chunk * DTYPE_BYTES
        print(f"  chunks {chunk:>3}x{chunk:<3}      | {read / 1e6:>15.2f} | "
              f"{read / window_bytes:>25.2f}x   ({n_chunks} chunks in the grid)")
    print("  -> a windowed read from an unchunked array touches whole rows;")
    print("     chunking is what makes the bytes read proportional to the query")

    section("2. Chunk shape versus query shape: waste against request count")
    print(f"  read model: {READ_RATE_MB_S:.0f} MB/s; request costs 0.1 ms on a "
          f"local disk, {OBJECT_REQUEST_MS:.0f} ms on an object store (chosen)")
    print("  chunk      | chunks read | bytes read | overshoot | time local | "
          "time object")
    for c in CHUNKS:
        touched = chunks_touched(WINDOW, c) ** 2
        read_mb = touched * c * c * DTYPE_BYTES / 1e6
        overshoot = read_mb * 1e6 / window_bytes
        local = read_mb / READ_RATE_MB_S * 1000 + touched * 0.1
        remote = read_mb / READ_RATE_MB_S * 1000 + touched * OBJECT_REQUEST_MS
        print(f"  {c:>3} x {c:<3}  | {touched:>11.1f} | {read_mb:>10.2f} | "
              f"{overshoot:>9.2f}x | {local:>9.1f} ms | {remote:>9.1f} ms")
    print("  -> small chunks waste the fewest bytes but cost a request each; the")
    print("     optimum moves towards larger chunks as the per-request cost rises")

    section("3. Compression: measured on smooth and on noisy data")
    smooth = np.add.outer(np.linspace(0, 1, 256), np.linspace(0, 1, 256))
    noisy = RNG.normal(0.0, 1.0, (256, 256))
    print("  model: zlib on the raw float32 bytes of the array (measured here)")
    for name, data in (("smooth ramp", smooth), ("white noise", noisy)):
        raw = data.astype(np.float32).tobytes()
        packed = zlib.compress(raw, 6)
        print(f"  {name:<12}: {len(raw) / 1e3:>7.1f} kB raw -> "
              f"{len(packed) / 1e3:>6.1f} kB compressed "
              f"({len(raw) / len(packed):>5.2f}x)")
    print("  -> compression return depends on the data, so it must be measured on")
    print("     the data you have, not assumed from the format")

    section("4. Append cost: time series versus grids")
    n_days = 3650
    value_bytes = 8
    daily_grid = (256 * 256 * value_bytes)      # a grid snapshot per day
    daily_series = 86_400 * value_bytes          # one day of one-second samples
    print(f"  a daily 256 x 256 grid snapshot = {daily_grid / 1e6:.1f} MB")
    print(f"  one day of 1 Hz samples         = {daily_series / 1e6:.1f} MB")
    print(f"  ten years of daily grid snapshots = "
          f"{n_days * daily_grid / 1e9:.1f} GB")
    print(f"  ten years of 1 Hz samples         = "
          f"{n_days * daily_series / 1e9:.1f} GB")
    print("  -> the layout must match the write pattern: snapshots want whole-file")
    print("     replacement and time series want append-only chunks")


if __name__ == "__main__":
    main()
