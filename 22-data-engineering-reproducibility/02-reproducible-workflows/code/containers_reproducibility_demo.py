#!/usr/bin/env python3
"""Containers for reproducibility: layers, caches and bitwise agreement.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python containers_reproducibility_demo.py

Everything here is SYNTHETIC.  Layer sizes, build times and drift probabilities
are chosen teaching values; no image is built and no registry is queried.

Sections
--------
1. A layered image: what is in it and what it costs.
2. Rebuild with cache: which layers survive a change to code, to data and to
   the package list.
3. Bitwise agreement of two builds from the same recipe, pinned and unpinned.
4. What the container does and does not freeze.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC image model (chosen, not measured) ---------------------------
LAYERS = [
    # name, size MB, build minutes, depends on recipe lines
    ("base image (digest pinned)", 120.0, 0.5),
    ("apt packages", 340.0, 4.0),
    ("python packages", 410.0, 6.5),
    ("reference data", 900.0, 2.0),
    ("analysis code", 12.0, 0.5),
]
DRIFT = {"apt packages": 0.15, "python packages": 0.25, "reference data": 0.05}


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def rebuild(change_layer):
    """Layers that must be rebuilt when `change_layer` changes."""
    names = [l[0] for l in LAYERS]
    start = names.index(change_layer)
    return LAYERS[start:]


def main():
    section("1. A layered image: what is in it and what it costs")
    total_mb = sum(l[1] for l in LAYERS)
    total_min = sum(l[2] for l in LAYERS)
    print("SYNTHETIC image recipe (sizes and times chosen):")
    print("  layer                          | size (MB) | build (min)")
    for name, size, minutes in LAYERS:
        print(f"  {name:<30} | {size:>9.1f} | {minutes:>11.1f}")
    print(f"  total image size = {total_mb / 1000:.2f} GB, cold build = "
          f"{total_min:.1f} min")
    print(f"  the analysis code is {100.0 * 12.0 / total_mb:.1f} % of the image "
          f"and {100.0 * 0.5 / total_min:.1f} % of the build time")
    print("  -> a container freezes the environment; the environment is the bulk")
    print("     of the image, and the code is a rounding error inside it")

    section("2. Rebuild with cache")
    print("  changed layer                  | rebuilt layers | rebuild (min)")
    for changed in ("analysis code", "reference data", "python packages",
                    "apt packages"):
        rebuilt = rebuild(changed)
        minutes = sum(l[2] for l in rebuilt)
        print(f"  {changed:<30} | {len(rebuilt):>14d} | {minutes:>13.1f}")
    print("  -> order the recipe so that the things that change most often come")
    print("     last: the cache then preserves the expensive layers")

    section("3. Bitwise agreement of two builds from the same recipe")
    print("  floating parts: apt packages and python packages resolve at build time")
    for pinned in (False, True):
        agreement = 1.0
        for name, p in DRIFT.items():
            if not pinned:
                agreement *= (1.0 - p)
        n_floating = 0 if pinned else sum(l[1] for l in LAYERS
                                          if l[0] in DRIFT)
        print(f"  digests pinned = {str(pinned):<5}: "
              f"P(two builds are bitwise identical) = {agreement:.3f}; "
              f"floating payload = {n_floating:.0f} MB")
    print("  -> the same recipe produces different environments unless every")
    print("     floating artefact is pinned by digest; the code is the easy part")

    section("4. What the container does and does not freeze")
    print("  frozen:  OS packages, python packages, reference data, the code")
    print("  not frozen: the host CPU and its math libraries, the scheduler")
    print("              (thread count, BLAS threading), the wall clock, and the")
    print("              external services the code calls")
    print(f"  model: a build that pins everything still differs in the last bits")
    print("         of a float32 sum on a different CPU (illustrative, not measured)")
    rng = RNG
    x = rng.normal(0.0, 1.0, 1_000_000).astype(np.float32)
    s1 = float(np.sum(x, dtype=np.float32))
    s2 = float(np.sum(x.astype(np.float64), dtype=np.float64))
    print(f"         float32 vs float64 accumulation of 1e6 samples: "
          f"{s1:.4f} vs {s2:.4f} (relative difference "
          f"{abs(s1 - s2) / abs(s2):.2e})")
    print("  -> a container pins the software, not the arithmetic; numerical")
    print("     tolerances belong in the tests, not in the image")


if __name__ == "__main__":
    main()
