#!/usr/bin/env python3
"""Data versioning and provenance: storage, deduplication and ancestry.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_versioning_demo.py

Everything here is SYNTHETIC.  The versions of the gridded dataset are generated
by the code below with chosen edit rates; no archive, catalogue or repository is
queried.  Storage numbers are properties of this model.

Sections
--------
1. Versions of one gridded dataset: naive storage versus content-addressed chunks.
2. Deduplication: how much of each version is genuinely new.
3. Provenance: the ancestry of the version that produced a figure.
4. Ambiguity: what "the data used" means without a recorded version.
"""

import hashlib
import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC dataset model (chosen, not measured) -------------------------
SHAPE = (200, 200)        # grid cells
CHUNK = (25, 25)          # chunk shape for content addressing
N_VERSIONS = 50
BLOCK = 30                # side of the region edited by a small version
REPROCESS_EVERY = 10      # every tenth version reprocesses the whole grid


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def chunk_hashes(grid, chunk):
    """Content hashes of every chunk of a 2-D array."""
    hashes = []
    for i in range(0, grid.shape[0], chunk[0]):
        for j in range(0, grid.shape[1], chunk[1]):
            block = grid[i:i + chunk[0], j:j + chunk[1]]
            hashes.append(hashlib.sha256(block.tobytes()).hexdigest()[:16])
    return hashes


def main():
    section("1. Versions of one dataset: naive versus content-addressed storage")
    n_cells = SHAPE[0] * SHAPE[1]
    bytes_per_version = n_cells * 8     # float64
    print(f"SYNTHETIC dataset: {SHAPE[0]} x {SHAPE[1]} float64 grid = "
          f"{bytes_per_version / 1000:.1f} kB per version, {N_VERSIONS} versions")
    grid = RNG.normal(0.0, 1.0, SHAPE)
    unique_chunks = set()
    new_chunks_per_version = []
    for v in range(1, N_VERSIONS):
        if v % REPROCESS_EVERY == 0:
            grid = RNG.normal(0.0, 1.0, SHAPE)      # full reprocessing
        else:
            i0 = int(RNG.integers(0, SHAPE[0] - BLOCK + 1))
            j0 = int(RNG.integers(0, SHAPE[1] - BLOCK + 1))
            grid[i0:i0 + BLOCK, j0:j0 + BLOCK] += \
                RNG.normal(0.0, 0.1, (BLOCK, BLOCK))
        hashes = chunk_hashes(grid, CHUNK)
        before = len(unique_chunks)
        unique_chunks.update(hashes)
        new_chunks_per_version.append(len(unique_chunks) - before)
    n_chunks = len(chunk_hashes(grid, CHUNK))
    naive = N_VERSIONS * bytes_per_version
    stored_chunks = len(unique_chunks)
    chunk_bytes = CHUNK[0] * CHUNK[1] * 8
    stored = stored_chunks * chunk_bytes
    print(f"  chunks per version = {n_chunks} of "
          f"{CHUNK[0]} x {CHUNK[1]} cells ({chunk_bytes / 1000:.1f} kB each)")
    print(f"  naive storage (all versions whole)  = {naive / 1e6:.2f} MB")
    print(f"  content-addressed storage           = {stored / 1e6:.2f} MB "
          f"({stored_chunks} unique chunks)")
    print(f"  deduplication ratio                 = {naive / stored:.1f}x")

    section("2. How much of each version is genuinely new")
    print(f"  a small version edits a {BLOCK} x {BLOCK} block; every "
          f"{REPROCESS_EVERY}th reprocesses the grid")
    print("  version | new chunks | new bytes (kB) | share of the version")
    for v, new in enumerate(new_chunks_per_version, start=1):
        if v % 5 == 0 or v <= 3:
            print(f"  {v:>7d} | {new:>10d} | {new * chunk_bytes / 1000:>14.1f} | "
                  f"{100.0 * new / n_chunks:>23.0f} %")
    changes = np.array(new_chunks_per_version)
    print(f"  mean new chunks per version = {changes.mean():.1f} of {n_chunks} "
          f"({100.0 * changes.mean() / n_chunks:.0f} %)")
    print("  -> most versions add almost nothing: versioning cost is dominated by")
    print("     the rare full reprocessing, not by the steady stream of edits")

    section("3. Provenance: the ancestry of the figure version")
    print("  model: each version records its parent(s), and small edits and")
    print("  reprocessing versions both have a single parent, the previous version")
    n_ancestors = N_VERSIONS - 1
    print(f"  version {N_VERSIONS} has {n_ancestors} direct ancestors")
    print(f"  a reprocessing happened at versions "
          f"{list(range(REPROCESS_EVERY, N_VERSIONS, REPROCESS_EVERY))}")
    print("  -> the ancestry answers 'which data', and the recorded parent links")
    print("     answer 'which processing' only as far as the model records it")

    section("4. Ambiguity: what 'the data used' means without a version")
    print(f"  versions in the archive = {N_VERSIONS}")
    print(f"  probability of guessing the figure's version = "
          f"{1.0 / N_VERSIONS:.2f} ({100.0 / N_VERSIONS:.0f} %)")
    print(f"  storage cost of recording the version in the figure metadata = "
          f"{len(str(N_VERSIONS))} characters")
    print("  -> recording the version costs nothing and is the difference between")
    print("     a reproducible figure and a plausible one")


if __name__ == "__main__":
    main()
