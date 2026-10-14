#!/usr/bin/env python3
"""Cloud-native geoscience access: range requests over chunked objects.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cloud_native_geoscience_demo.py

Everything here is SYNTHETIC.  The object layout, request costs and window queries
are chosen teaching values; no object store was queried and no real cloud service is
described.

Sections
--------
1. A chunked object: bytes fetched versus bytes needed for a window.
2. Request count and the cost of many small reads.
3. Overviews for a viewer: reading a coarse level instead of subsampling the fine.
4. Concurrency: wall time as a function of the request count and latency.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC object model (chosen, not measured) --------------------------
GRID = 16_384               # pixels per side (a large raster)
DTYPE_BYTES = 2             # uint16 reflectance
CHUNKS = (512, 1024, 2048)
REQUEST_MS = 30.0           # per-request latency on an object store
BANDWIDTH_MB_S = 100.0      # per-connection bandwidth
CONCURRENCY = 16


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. A chunked object: bytes fetched versus bytes needed")
    total_bytes = GRID * GRID * DTYPE_BYTES
    print(f"SYNTHETIC raster: {GRID} x {GRID} uint16 = "
          f"{total_bytes / 1e9:.2f} GB (chosen)")
    for side in (256, 1024):
        need = side * side * DTYPE_BYTES
        print(f"  window {side} x {side} needs {need / 1e3:.0f} kB")
        for c in CHUNKS:
            n = (side / c + 1) ** 2 if c < side else 4.0
            read = n * c * c * DTYPE_BYTES
            print(f"    chunk {c:>4}: {n:>5.1f} chunks, {read / 1e6:>7.2f} MB "
                  f"fetched, amplification {read / need:>5.2f}x")
    print("  -> the request count and the amplification are both set by the chunk")
    print("     size relative to the window; neither is visible from the file name")

    section("2. Request count and its cost")
    for c in CHUNKS:
        n_requests = int(np.ceil(1024 / c + 1)) ** 2
        latency = n_requests * REQUEST_MS / 1000
        transfer = n_requests * c * c * DTYPE_BYTES / 1e6 / BANDWIDTH_MB_S
        print(f"  chunk {c:>4}: {n_requests:>5.0f} requests, latency "
              f"{latency:>6.2f} s, transfer {transfer:>5.3f} s, "
              f"total {latency + transfer:>6.2f} s")
    print("  -> at 30 ms per request the request term dominates for small chunks;")
    print("     a viewer that reads a window per pan spends its time in latency")

    section("3. Overviews for a viewer")
    print("  level | resolution | bytes for the full extent | use")
    base = GRID
    for level in range(0, 6):
        side = base // (2 ** level)
        bytes_full = side * side * DTYPE_BYTES
        print(f"  {level:>5d} | {side:>10d} px | {bytes_full / 1e6:>24.2f} MB | "
              f"{'thumbnail' if level >= 4 else ('preview' if level >= 2 else 'analysis')}")
    print("  -> a zoomed-out view should read a coarse overview, not subsample the")
    print("     fine level: the byte saving is a factor of 4 per level")

    section("4. Concurrency and wall time")
    print("  requests | serial (s) | with 16 connections (s) | speedup")
    for n in (16, 64, 256, 1024):
        serial = n * REQUEST_MS / 1000
        parallel = max(serial / CONCURRENCY, REQUEST_MS / 1000)
        print(f"  {n:>8d} | {serial:>10.2f} | {parallel:>23.2f} | "
              f"{serial / parallel:>7.1f}x")
    print("  -> concurrency converts latency into throughput, and the ceiling is")
    print("     the per-connection bandwidth times the connection count")


if __name__ == "__main__":
    main()
