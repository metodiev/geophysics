"""Cleaning: missing values, duplicates and outliers.

Run:  .venv/bin/python 03-scientific-computing/04-pandas/code/cleaning_data_demo.py
Requires: pandas (installed in the project venv).

Companion to lesson 03-04-03.  The catalogue is SYNTHETIC (see
``synthetic_catalog.py``); it is not the USGS catalogue.

The script does not merely *perform* cleaning -- it states a policy before each
step and reports the number of rows affected, so that a reader can judge whether
the policy changed the answer.

Demonstrates:

1. Triage: counting what is missing, repeated and physically impossible.
2. A missing-value policy, and why imputing magnitude is not allowed here.
3. Duplicate reports, and what keeping one row per event actually costs.
4. Outlier detection with a robust (median/MAD) score, not a mean/std one.
5. Before/after comparison of the quantities the cleaning is supposed to
   protect: event counts and the magnitude-frequency statistics.
"""

import numpy as np
import pandas as pd

import synthetic_catalog as sc


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def triage():
    section("1. Triage before treatment")
    raw = sc.raw_catalog()
    print(f"  raw rows: {len(raw)}")
    print("  missing values per column:")
    print(raw.isna().sum().to_string())
    print()
    print(f"  duplicated event_id rows      : {int(raw['event_id'].duplicated().sum())}")
    print(f"  duplicate (time, lat, lon) rows: "
          f"{int(raw.duplicated(['origin_time', 'latitude', 'longitude']).sum())}")
    print()
    print("  physically impossible depths (outside 0..700 km):")
    bad = raw[~raw["depth_km"].isna() & ~raw["depth_km"].between(0, 700)]
    print(bad[["event_id", "region", "depth_km", "agency"]].to_string(index=False))
    print()
    print("  summary statistics of a column with a sentinel in it:")
    print(f"    depth_km  mean   = {raw['depth_km'].mean():8.2f} km   "
          f"median = {raw['depth_km'].median():7.2f} km")
    print(f"    depth_km  min    = {raw['depth_km'].min():8.2f} km   "
          f"max    = {raw['depth_km'].max():7.2f} km")
    inrange = raw.loc[raw["depth_km"].between(0, 700), "depth_km"]
    print(f"    depth_km  mean excluding the two impossible values = "
          f"{inrange.mean():.2f} km")
    print("  Two impossible rows move the mean by "
          f"{raw['depth_km'].mean() - inrange.mean():.2f} km and leave the")
    print("  median untouched. That difference is the reason the median is the")
    print("  default summary for a skewed column.")


def missing_values():
    section("2. Missing values: state the policy, then count the cost")
    raw = sc.raw_catalog()
    print(f"  mw is missing for {int(raw['mw'].isna().sum())} rows "
          f"({raw['mw'].isna().mean() * 100:.1f} %)")
    print(f"  depth_km is missing for {int(raw['depth_km'].isna().sum())} rows "
          f"({raw['depth_km'].isna().mean() * 100:.1f} %)")
    print()
    print("  Policy for magnitude: DROP the row.")
    print("    Reason: magnitude is the analysis variable of the",
          "magnitude-frequency")
    print("    relation. Imputing it would manufacture the distribution we are")
    print("    about to measure. A drop is honest; a fill is a fabricated data")
    print("    point.")
    print()
    print("  Policy for depth: IMPUTE with the median depth of the same region.")
    print("    Reason: depth is a supporting variable here. The regional median")
    print("    preserves the regional depth structure and is robust to the")
    print("    sentinel outliers; a global mean would import the sentinel.")
    print()
    print("  What fillna(0) would do to the depth column, for contrast:")
    print(f"    mean after fillna(0) : {raw['depth_km'].fillna(0).mean():.2f} km"
          "   (asserts 0 km depth)")
    print(f"    mean after dropping  : {raw['depth_km'].dropna().mean():.2f} km")
    print()


def duplicates():
    section("3. Duplicate reports and the cost of a non-unique key")
    raw = sc.raw_catalog()
    dup_ids = raw.loc[raw["event_id"].duplicated(), "event_id"].unique()
    print(f"  events reported twice: {len(dup_ids)} "
          f"({', '.join(sorted(dup_ids))})")
    print()
    print("  The two reports of the same event are not identical:")
    first = dup_ids[0]
    print(raw.loc[raw["event_id"] == first,
                  ["event_id", "depth_km", "mw", "agency"]].to_string(index=False))
    print()
    print("  Naive per-region counts double-count those events:")
    naive = raw["region"].value_counts().sort_index()
    dedup = (raw.sort_values("agency")
             .drop_duplicates("event_id", keep="first")
             ["region"].value_counts().sort_index())
    cmp = pd.DataFrame({"with_duplicates": naive, "one_row_per_event": dedup})
    cmp["over_count"] = cmp["with_duplicates"] - cmp["one_row_per_event"]
    print(cmp.to_string())
    print()
    print("  keep='first' is only safe if the order is meaningful. Ordering by")
    print(f"  agency ({sc.AGENCY_PRIORITY}) makes 'first' mean 'preferred network',")
    print("  which is a stated rule rather than an accident of row order.")


def outliers():
    section("4. Outliers: robust detection, then an explicit decision")
    raw = sc.raw_catalog()
    depth = raw["depth_km"].dropna()
    med = depth.median()
    mad = (depth - med).abs().median()
    print(f"  median depth      = {med:.2f} km")
    print(f"  median abs. dev.  = {mad:.2f} km")
    print("  robust z-score    = 0.6745 * (x - median) / MAD  (Iglewicz-Hoban)")
    print()
    flag = raw["depth_km"].notna() & (
        (0.6745 * (raw["depth_km"] - med) / mad).abs() > 3.5
    )
    print(f"  rows flagged at |z| > 3.5: {int(flag.sum())}")
    print(raw.loc[flag, ["event_id", "region", "depth_km", "mw"]]
          .to_string(index=False))
    print()
    print("  A mean/std z-score on the same column, for contrast:")
    zz = (raw["depth_km"] - raw["depth_km"].mean()) / raw["depth_km"].std()
    print(f"    rows flagged at |z| > 3.5 : {int((zz.abs() > 3.5).sum())}")
    print(f"    the 999 km sentinel scores: {zz.loc[0]:.2f}")
    print("    The 999 inflates the standard deviation it is measured against,")
    print("    so it partially hides itself. That is the classic masking failure")
    print("    of non-robust outlier scores.")
    print()
    print("  Decision (stated, not implied): drop depths outside [0, 700] km.")
    print("    0 km is not a physical depth solution; 700 km is below the")
    print("    deepest seismicity. Everything inside the range is kept even if")
    print("    it is a statistical outlier, because a genuinely deep event is")
    print("    a fact, not an error.")


def before_after():
    section("5. Before and after: what the policy changed")
    raw = sc.raw_catalog()
    clean = sc.clean_catalog()

    def stats(frame):
        return {
            "rows": len(frame),
            "missing mw": int(frame["mw"].isna().sum()),
            "missing depth_km": int(frame["depth_km"].isna().sum()),
            "duplicate event_id": int(frame["event_id"].duplicated().sum()),
            "depth outside 0..700": int(
                (~frame["depth_km"].isna()
                 & ~frame["depth_km"].between(0, 700)).sum()
            ),
            "mw < 2.0": int((frame["mw"] < 2.0).sum()),
        }

    raw_stats, clean_stats = stats(raw), stats(clean)
    parsed = pd.DataFrame({"raw": raw_stats, "cleaned": clean_stats})
    print(parsed.to_string())

    print()
    print(f"  rows removed in total: {len(raw) - len(clean)}")
    print("  The quantity the cleaning exists to protect -- the count of")
    print("  events above each magnitude -- before and after:")
    for label, frame in (("raw", raw), ("cleaned", clean)):
        usable = frame["mw"].dropna()
        usable = usable[usable >= sc.M_MIN]
        counts = [(m, int((usable >= m).sum())) for m in (2.0, 3.0, 4.0)]
        print(f"    {label:>8}: " + "   ".join(
            f"N(M>={m:.1f}) = {n}" for m, n in counts))
    print()
    print("  On SYNTHETIC data this difference is small by construction; the")
    print("  point is not the size of the shift but that the shift is")
    print("  *reported*. A cleaned catalogue should always be accompanied by")
    print("  the count of rows each policy step removed, so a reader can judge")
    print("  whether the cleaning changed the answer.")


if __name__ == "__main__":
    print("SYNTHETIC catalogue: generated in-code, not an observation of the"
          "\nEarth and not the USGS catalogue.  See synthetic_catalog.py.")
    triage()
    missing_values()
    duplicates()
    outliers()
    before_after()
