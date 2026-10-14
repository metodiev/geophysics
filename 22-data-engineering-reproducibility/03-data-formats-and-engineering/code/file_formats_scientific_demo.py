#!/usr/bin/env python3
"""Scientific file formats: size, precision and parse cost, on SYNTHETIC data.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python file_formats_scientific_demo.py

Everything here is SYNTHETIC.  The arrays are generated below and the size and
time models use chosen constants; no real file is written, read or compressed.

Sections
--------
1. Same numbers, different representations: bytes per value.
2. Text precision: how many digits it takes to round-trip a float64.
3. Parse cost: time as a function of representation and record count.
4. What each format makes easy and hard.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC data and cost model (chosen, not measured) -------------------
N_VALUES = 250_000
PARSE_RATE_MB_S = 60.0       # text parsing throughput, MB/s (chosen)
READ_RATE_MB_S = 2000.0      # binary unpacking throughput, MB/s (chosen)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. Same numbers, different representations")
    x = RNG.normal(0.0, 1.0, N_VALUES)
    ascii_default = ",".join(f"{v:.6f}" for v in x).encode()
    ascii_short = ",".join(f"{v:.3f}" for v in x).encode()
    binary64 = x.astype(np.float64).tobytes()
    binary32 = x.astype(np.float32).tobytes()
    print(f"SYNTHETIC array: {N_VALUES} float64 values, sigma = 1.0 "
          f"(data units, chosen)")
    print("  representation        | bytes | bytes/value | overhead vs float64")
    for name, blob in (("text, 6 decimals", ascii_default),
                       ("text, 3 decimals", ascii_short),
                       ("binary float64", binary64),
                       ("binary float32", binary32)):
        print(f"  {name:<21} | {len(blob):>5d} | {len(blob) / N_VALUES:>11.2f} | "
              f"{len(blob) / len(binary64):>18.2f}x")
    print("  -> text is not 'smaller because it is human readable'; it is usually")
    print("     2-3x larger than binary and loses precision in the process")

    section("2. Text precision and round-trip error")
    print("  digits | max |round-trip error| | values that change bits")
    for digits in (3, 6, 9, 12):
        back = np.array([float(f"{v:.{digits}f}") for v in x[:20000]])
        err = np.abs(back - x[:20000]).max()
        changed = int((back != x[:20000]).sum())
        print(f"  {digits:>6d} | {err:>21.6e} | {changed:>24d}")
    print(f"  float32 rounding floor for comparison = "
          f"{np.abs(x.astype(np.float32).astype(np.float64) - x).max():.3e}")
    print("  -> 12 decimals still changes bits for most values: text is a lossy")
    print("     representation unless the digits are chosen from the data's scale")

    section("3. Parse cost as a function of representation")
    print("  model: text parsed at "
          f"{PARSE_RATE_MB_S:.0f} MB/s, binary unpacked at "
          f"{READ_RATE_MB_S:.0f} MB/s (chosen; fixed open/close overhead excluded)")
    print("  representation        | size (MB) | parse time (s) | ratio to binary64")
    times = {}
    for name, blob, rate in (("text, 6 decimals", ascii_default, PARSE_RATE_MB_S),
                             ("text, 3 decimals", ascii_short, PARSE_RATE_MB_S),
                             ("binary float64", binary64, READ_RATE_MB_S),
                             ("binary float32", binary32, READ_RATE_MB_S)):
        times[name] = (len(blob) / 1e6, len(blob) / 1e6 / rate)
    base = times["binary float64"][1]
    for name, (mb, seconds) in times.items():
        print(f"  {name:<21} | {mb:>9.2f} | {seconds:>14.4f} | "
              f"{seconds / base:>16.1f}x")
    print("  -> the same numbers cost tens of times more time in text; the cost is")
    print("     in parsing characters, not in reading bytes from disk")

    section("4. What each representation makes easy")
    rows = [
        ("CSV", "human inspection, diff, one number per line",
         "no types, no units, larger, slow parse"),
        ("Parquet", "column selection, compression, typed schema",
         "write-once columnar layout, needs a library"),
        ("HDF5", "hierarchical groups, partial reads, rich metadata",
         "complexity, format versions, one-file contention"),
        ("netCDF", "self-describing arrays with CF conventions",
         "conventions to learn, tooling heterogeneity"),
        ("Zarr", "chunked arrays on object stores, parallel writes",
         "many small objects, needs an object store"),
    ]
    print("  format   | makes easy                                     | costs")
    for name, easy, cost in rows:
        print(f"  {name:<8} | {easy:<46} | {cost}")
    print("  -> choose the representation that matches the access pattern, then")
    print("     record the choice: a format is part of the data's documentation")


if __name__ == "__main__":
    main()
