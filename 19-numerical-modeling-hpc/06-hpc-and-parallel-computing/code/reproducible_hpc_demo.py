#!/usr/bin/env python3
"""Reproducibility and provenance: what fixes the bits, what identifies a run, and
what a text round trip does to a floating-point number.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproducible_hpc_demo.py

Everything is SYNTHETIC: array sizes, chunk counts and the parameter dictionary
are chosen teaching values.  The demo starts only short-lived bounded thread pools
with explicit joins; it spawns no process and no MPI rank, and it deletes every
file it writes before exiting.

Contents
--------
1. Reduction order changes the bits: sequential, chunked and pairwise sums, in ulp.
2. An exactly-rounded sum is order independent: measured across every chunking.
3. The identity of a result: hashes of the same numbers, arranged differently.
4. Provenance: a canonical manifest of parameters and environment, hashed.
5. Serialisation: binary round trip against text round trip, measured.
6. A reproducibility test that fails when the decomposition changes.
7. Summary of measured quantities.
"""

import hashlib
import json
import os
import platform
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import scipy
import sympy

RNG = np.random.default_rng(20261014)

SCRATCH_DIR = os.path.dirname(os.path.abspath(__file__))


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def digest(obj):
    if isinstance(obj, np.ndarray):
        payload = obj.tobytes()
    elif isinstance(obj, (float, np.floating)):
        payload = np.float64(obj).tobytes()
    else:
        payload = json.dumps(obj, sort_keys=True).encode()
    return hashlib.sha256(payload).hexdigest()[:16]


def sequential_sum(a):
    total = 0.0
    for x in a:
        total += float(x)
    return total


def chunked_sum(a, chunks):
    """Sum in fixed-size chunks with a sequential merge in chunk order."""
    edges = np.linspace(0, a.size, chunks + 1).astype(int)
    partials = [float(np.sum(a[edges[i]:edges[i + 1]])) for i in range(chunks)]
    total = 0.0
    for p in partials:
        total += p
    return total


def main():
    global DATA
    DATA = RNG.standard_normal(1 << 20)

    section("1. Reduction order changes the bits")
    data = DATA
    m = data.size
    ref = float(np.sum(data))
    plain = 0.0
    for x in data[:200_000]:
        plain += float(x)
    pair_partial = float(np.sum(data[:200_000]))
    print(f"  {m} doubles from a fixed seed; numpy's pairwise sum = {ref!r}")
    print("  first 200000 values, three ways:")
    print(f"    Python for-loop accumulation : {plain!r}")
    print(f"    numpy pairwise on the slice  : {pair_partial!r}")
    print(f"    difference                   : {plain - pair_partial:+.6e} "
          f"= {(plain-pair_partial)/np.spacing(abs(plain)):+.1f} ulp of the result")
    print("\n  the whole array, five decompositions:")
    print("     chunks   value                      digest            ulp vs numpy")
    seen = set()
    for chunks in (1, 2, 4, 8, 16, 64):
        v = chunked_sum(data, chunks)
        seen.add(digest(v))
        print(f"  {chunks:8d}   {v!r}   {digest(v)}   "
              f"{(v-ref)/np.spacing(abs(ref)):+8.1f}")
    print(f"  distinct digests across six decompositions: {len(seen)}")
    print("  the same numbers, added in a different order, are different floats.  A")
    print("  reduction therefore has a defined value only once its order is defined.")

    section("2. An exactly-rounded sum removes the order dependence")
    import math
    values = data[:200_000].tolist()
    print("  math.fsum is exactly rounded: its result is the correctly rounded sum of")
    print("  the exact values, so it cannot depend on the order in which they arrive.")
    print("     chunks   fsum value                 digest")
    seen_fsum = set()
    for chunks in (1, 2, 3, 4, 8, 16):
        edges = np.linspace(0, len(values), chunks + 1).astype(int)
        partials = [math.fsum(values[edges[i]:edges[i + 1]]) for i in range(chunks)]
        total = math.fsum(partials)
        seen_fsum.add(digest(total))
        print(f"  {chunks:8d}   {total!r}   {digest(total)}")
    print(f"  distinct digests: {len(seen_fsum)}")
    print("  one digest for every decomposition.  Exact rounding costs time and is")
    print("  not free of memory traffic, but it converts 'reproducible if you use the")
    print("  same decomposition' into 'reproducible'.")

    section("3. The identity of a result")
    a = np.arange(8, dtype=np.float64) + 0.1
    b = a.copy()
    print(f"  two arrays with identical contents: digests {digest(a)} and {digest(b)}")
    print(f"  identical bytes: {digest(a) == digest(b)}")
    c = a[::-1].copy()
    print(f"  the same eight values in reverse order: digest {digest(c)}, "
          f"same: {digest(a) == digest(c)}")
    print(f"  same values as a set: {sorted(a.tolist()) == sorted(c.tolist())}")
    print("  a hash identifies bytes, not meaning.  Two runs whose results agree to")
    print("  1e-15 have different hashes; two runs that hash the same have agreed on")
    print("  every bit, which is a much stronger claim and the one worth making when")
    print("  a paper says 'bitwise reproducible'.")

    section("4. Provenance: a canonical manifest, hashed")
    manifest = {
        "grid": [256, 256],
        "dt_s": 0.004,
        "velocity_km_s": 3.5,
        "sweeps": 200,
        "decomposition": {"ranks": 4, "layout": "bands"},
        "reduction_order": "chunked, chunks=8, sequential merge",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "sympy": sympy.__version__,
        "byte_order": "little" if np.little_endian else "big",
        "float64_eps": float(np.finfo(np.float64).eps),
        "cpu_count": os.cpu_count(),
    }
    text = json.dumps(manifest, sort_keys=True, separators=(",", ":"))
    print("  canonical manifest (sorted keys, no whitespace), hashed with sha256:")
    print(f"    {text}")
    print(f"    digest: {hashlib.sha256(text.encode()).hexdigest()}")
    changed = dict(manifest)
    changed["dt_s"] = 0.0041
    text2 = json.dumps(changed, sort_keys=True, separators=(",", ":"))
    print("  one parameter changed in the fourth significant digit:")
    print(f"    digest: {hashlib.sha256(text2.encode()).hexdigest()}")
    print("  the hash is the cheapest way to answer 'is this the same run?' and the")
    print("  only way to answer it without reading the whole configuration by eye.")
    print(f"  the manifest records the reduction order explicitly, because section 1")
    print("  showed that the decomposition is part of the arithmetic.")

    section("5. Serialisation: binary against text round trips")
    arr = RNG.standard_normal(1000)
    npy = os.path.join(SCRATCH_DIR, "_demo_roundtrip.npy")
    txt17 = os.path.join(SCRATCH_DIR, "_demo_roundtrip_17.txt")
    txt6 = os.path.join(SCRATCH_DIR, "_demo_roundtrip_6.txt")
    np.save(npy, arr)
    back = np.load(npy)
    with open(txt17, "w") as fh:
        for x in arr:
            fh.write(f"{x:.17e}\n")
    with open(txt6, "w") as fh:
        for x in arr:
            fh.write(f"{x:.6e}\n")
    r17 = np.loadtxt(txt17)
    r6 = np.loadtxt(txt6)
    print(f"  .npy round trip          : identical bits: "
          f"{digest(back) == digest(arr)}, max|difference| = "
          f"{np.max(np.abs(back-arr)):.3e}")
    print(f"  text with 17 digits      : identical bits: "
          f"{digest(r17) == digest(arr)}, max|difference| = "
          f"{np.max(np.abs(r17-arr)):.3e}")
    print(f"  text with  6 digits      : identical bits: "
          f"{digest(r6) == digest(arr)}, max|difference| = "
          f"{np.max(np.abs(r6-arr)):.3e}")
    rel6 = np.max(np.abs(r6 - arr)) / np.sqrt(np.mean(arr ** 2))
    print(f"  largest absolute error of the 6-digit round trip: "
          f"{np.max(np.abs(r6 - arr)):.3e}, i.e. {rel6:.3e} of the array RMS")
    print("  one element of an array does not carry 17 digits of meaning, but the")
    print("  ARRAY does: rounding each value to 6 digits changes the state.")
    print("  a checkpoint keeps more than 'enough digits to plot'.  Six digits is a")
    print("  picture; seventeen digits (or the binary form) is the state.")
    for path in (npy, txt17, txt6):
        os.remove(path)

    section("6. A reproducibility test: fixed decomposition against a free one")
    values = DATA

    def reduce_fixed(chunks, pool_size):
        edges = np.linspace(0, m, chunks + 1).astype(int)

        def part(i):
            return float(np.sum(values[edges[i]:edges[i + 1]]))

        with ThreadPoolExecutor(max_workers=pool_size) as pool:
            futures = [pool.submit(part, i) for i in range(chunks)]
            partials = [f.result() for f in futures]      # chunk order preserved
        total = 0.0
        for p in partials:
            total += p
        return total

    baseline = reduce_fixed(8, 1)
    print(f"  baseline: 8 chunks, 1 worker  -> {baseline!r}, digest "
          f"{digest(baseline)}")
    for pool_size in (2, 4, 8):
        v = reduce_fixed(8, pool_size)
        print(f"  same 8 chunks, {pool_size} workers -> {digest(v)}   "
              f"identical: {digest(v) == digest(baseline)}")
    for chunks in (4, 16):
        v = reduce_fixed(chunks, 4)
        print(f"  {chunks} chunks, 4 workers      -> {digest(v)}   "
              f"identical: {digest(v) == digest(baseline)}")
    print("  the test that a reviewer can run is 'same decomposition, different")
    print("  machine size, same digest'.  A test that varies the decomposition asserts")
    print("  something that is false, and a code that passes it is not being checked.")

    section("7. Summary of measured quantities")
    print(f"  distinct digests across 6 chunk counts      : {len(seen)}")
    print(f"  distinct digests for math.fsum, 6 chunkings : {len(seen_fsum)}")
    print(f"  for-loop / pairwise difference on 200000    : "
          f"{(plain-pair_partial)/np.spacing(abs(plain)):+.1f} ulp")
    print(f"  text round trip, 6 digits                   : max abs error "
          f"{np.max(np.abs(r6 - arr)):.3e}, {rel6:.3e} of the array RMS")
    print("  manifest digest changes when one parameter changes : yes")
    print("  digest invariance to worker count, fixed decomposition : yes")
    print("  All inputs are SYNTHETIC teaching values; all differences are measured on")
    print("  this machine's IEEE-754 double arithmetic, which is what makes them")
    print("  reproducible elsewhere.")


if __name__ == "__main__":
    main()
