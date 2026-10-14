#!/usr/bin/env python3
"""Publishing data and code: metadata completeness, reuse and format longevity.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_publication_demo.py

Everything here is SYNTHETIC.  The datasets, their metadata fields, their sizes and
the reuse model are generated with chosen probabilities; no repository was queried
and no real deposit is described.

Sections
--------
1. Metadata completeness across a synthetic corpus of deposits.
2. What completeness buys: the reuse model.
3. The weakest fields and the effect of fixing one.
4. Format longevity and where the bytes live.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
N_DATASETS = 120
FIELDS = (
    ("title", 0.99),
    ("creators and affiliations", 0.96),
    ("licence", 0.71),
    ("methods description", 0.65),
    ("instrument and settings", 0.58),
    ("spatial coverage", 0.74),
    ("temporal coverage", 0.62),
    ("processing level", 0.55),
    ("file format description", 0.48),
    ("units and conventions", 0.53),
    ("related identifiers", 0.37),
    ("version and provenance", 0.44),
)
REUSE_AT_FULL = 0.75        # P(reuse | the record is perfect)
REUSE_AT_ZERO = 0.05        # P(reuse | nothing documented but the bytes)
PRESERVATION_FRIENDLY = ("csv", "netcdf", "geotiff", "hdf5", "png", "json",
                         "xml", "parquet", "seg-y", "txt")
FORMATS = (("csv", 0.22, 40.0), ("netcdf", 0.18, 900.0), ("geotiff", 0.14, 300.0),
           ("hdf5", 0.10, 700.0), ("seg-y", 0.08, 2500.0), ("json", 0.07, 5.0),
           ("xlsx", 0.08, 12.0), ("docx", 0.06, 2.0), ("proprietary binary", 0.05, 1800.0),
           ("png", 0.02, 3.0))


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    present = np.array([RNG.random(N_DATASETS) < p for _, p in FIELDS]).T
    completeness = present.mean(axis=1)

    section("1. Metadata completeness across a synthetic corpus of deposits")
    print(f"SYNTHETIC corpus: {N_DATASETS} deposits, {len(FIELDS)} metadata fields")
    print("  field                          chosen   measured")
    for k, (name, p) in enumerate(FIELDS):
        print(f"  {name:<30s} {p * 100:5.1f} % {(present[:, k].mean()) * 100:8.1f} %")
    print(f"  mean completeness per deposit = {completeness.mean() * 100:.1f} % "
          f"+/- {completeness.std(ddof=1) * 100:.1f} %")
    print(f"  deposits with all {len(FIELDS)} fields = "
          f"{int(np.all(present, axis=1).sum())} "
          f"({np.all(present, axis=1).mean() * 100:.1f} %)")
    print(f"  deposits with fewer than half the fields = "
          f"{int(np.sum(completeness < 0.5))} "
          f"({np.mean(completeness < 0.5) * 100:.1f} %)")
    print("  -> completeness is not a property of a repository; it is a property of each")
    print("     deposit, and the spread is what makes a record unpredictable.")

    section("2. What completeness buys: the reuse model")
    reuse_p = REUSE_AT_ZERO + (REUSE_AT_FULL - REUSE_AT_ZERO) * completeness
    reused = RNG.random(N_DATASETS) < reuse_p
    print(f"  modelled reuse probability = {REUSE_AT_ZERO:.2f} + "
          f"{REUSE_AT_FULL - REUSE_AT_ZERO:.2f} x completeness")
    print(f"  expected reuses = {reuse_p.sum():.1f}; observed reuses = "
          f"{int(reused.sum())}")
    for lo, hi in ((0.0, 0.5), (0.5, 0.75), (0.75, 1.01)):
        mask = (completeness >= lo) & (completeness < hi)
        if mask.sum() == 0:
            continue
        print(f"  completeness {lo * 100:3.0f}-{hi * 100:3.0f} %: "
              f"{int(mask.sum()):3d} deposits, mean completeness "
              f"{completeness[mask].mean() * 100:5.1f} %, "
              f"expected reuses {reuse_p[mask].sum():5.1f}")
    print("  -> the model is linear by construction; the transferable claim is that")
    print("     reuse is a function of the record, not only of the data.")

    section("3. The weakest fields and the effect of fixing one")
    order = np.argsort([present[:, k].mean() for k in range(len(FIELDS))])
    for k in order[:3]:
        name = FIELDS[k][0]
        without = completeness.copy()
        fixed = present.copy()
        fixed[:, k] = True
        new_completeness = fixed.mean(axis=1)
        new_reuse = REUSE_AT_ZERO + (REUSE_AT_FULL - REUSE_AT_ZERO) * new_completeness
        print(f"  fixing '{name}' (currently {present[:, k].mean() * 100:.1f} %):")
        print(f"    mean completeness {completeness.mean() * 100:.1f} % -> "
              f"{new_completeness.mean() * 100:.1f} %, "
              f"expected reuses {reuse_p.sum():.1f} -> {new_reuse.sum():.1f} "
              f"({(new_reuse.sum() / reuse_p.sum() - 1) * 100:+.1f} %)")
    print(f"  the weakest field is present in {present[:, order[0]].mean() * 100:.1f} % "
          f"of deposits; fixing it raises each deposit's completeness by "
          f"{100 / len(FIELDS):.1f} percentage points and its expected reuse")
    print(f"  by {(REUSE_AT_FULL - REUSE_AT_ZERO) / len(FIELDS) * 100:.1f} % "
          f"(a percentage point of reuse, not of completeness)")
    print("  -> one field per deposit is cheap; the marginal gain is the same for every")
    print("     field, so fix the one that is cheapest for you to fill in consistently.")

    section("4. Format longevity and where the bytes live")
    print("  format                share of deposits   mean size (MB)   preservation-"
          "friendly")
    total_bytes = 0.0
    friendly_bytes = 0.0
    for name, share, size_mb in FORMATS:
        n = int(round(share * N_DATASETS))
        friendly = name in PRESERVATION_FRIENDLY
        print(f"  {name:<22s} {n:5d} ({share * 100:4.1f} %)   {size_mb:11.1f}   "
              f"{'yes' if friendly else 'no':>19s}")
        total_bytes += n * size_mb
        friendly_bytes += n * size_mb * (1.0 if friendly else 0.0)
    print(f"  bytes in preservation-friendly formats = "
          f"{friendly_bytes / total_bytes * 100:.1f} % of the corpus")
    friendly_share = sum(s for n, s, _ in FORMATS if n in PRESERVATION_FRIENDLY)
    print(f"  deposits in preservation-friendly formats = {friendly_share * 100:.1f} %")
    print(f"  -> the byte share and the deposit share differ because the large files are")
    print(f"     the ones most often in specialist formats; size, not count, is the risk.")


if __name__ == "__main__":
    main()
