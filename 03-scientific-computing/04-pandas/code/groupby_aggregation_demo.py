"""Group-by, aggregation and reshaping.

Run:  .venv/bin/python 03-scientific-computing/04-pandas/code/groupby_aggregation_demo.py
Requires: pandas (installed in the project venv).

Companion to lesson 03-04-04.  The catalogue is SYNTHETIC (see
``synthetic_catalog.py``); it is not the USGS catalogue.

Demonstrates:

1. ``groupby`` and the difference between ``size()`` and ``count()``.
2. Named aggregation, so the output columns are self-documenting.
3. A two-key group-by (region and year) and its long form.
4. Reshaping long to wide with ``unstack`` and ``pivot_table``, and back with
   ``melt``.
5. ``transform``: a group-wise value broadcast back to every row (an anomaly),
   which is a different operation from ``agg`` even though the grouping is the
   same.
6. Aggregating a *derived* column (radiated energy from magnitude).
"""

import numpy as np
import pandas as pd

import synthetic_catalog as sc


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def frame():
    df = sc.clean_catalog()
    df = df.assign(
        year=df["origin_time"].dt.year,
        energy_j=sc.mag_to_energy_j(df["mw"]),
    )
    return df


def part1_groupby_basics():
    section("1. groupby: split, apply, combine")
    df = frame()
    print("  one line splits the frame into four sub-frames, applies an")
    print("  operation and recombines the results:")
    print(df.groupby("region")["mw"].mean().round(4).to_string())
    print()
    print("  size() counts ROWS; count() counts NON-MISSING VALUES.")
    print("  On a column with no gaps they agree, so the bug hides until the")
    print("  day the data have a gap:")
    tab = pd.DataFrame(
        {
            "size (rows)": df.groupby("region").size(),
            "count of mw": df.groupby("region")["mw"].count(),
            "count of depth_km": df.groupby("region")["depth_km"].count(),
        }
    )
    print(tab.to_string())
    print()
    print("  A deliberate demonstration on a frame with a hole punched in it:")
    holed = df.copy()
    holed.loc[holed.index[:40], "mw"] = np.nan     # knock out 40 magnitudes
    print(pd.DataFrame(
        {
            "size()": holed.groupby("region").size(),
            "count() on mw": holed.groupby("region")["mw"].count(),
        }
    ).to_string())
    print("  'count' column = rows - missing.")


def part2_named_aggregation():
    section("2. Named aggregation: output columns that name themselves")
    df = frame()
    summary = df.groupby("region", observed=True).agg(
        n_events=("event_id", "count"),
        mean_mw=("mw", "mean"),
        max_mw=("mw", "max"),
        median_depth_km=("depth_km", "median"),
        total_energy_j=("energy_j", "sum"),
    )
    print(summary[["n_events", "mean_mw", "max_mw", "median_depth_km"]]
          .round(3).to_string())
    print()
    print("  Total radiated energy by region (J, from 10^(1.5 M + 4.8)):")
    for region, row in summary.iterrows():
        print(f"    {region:<11} {row['total_energy_j']:.3e}")
    print()
    print("  With a named aggregation the result of the group-by is already a")
    print("  tidy table with usable column names, instead of MultiIndex columns")
    print("  that have to be relabelled before plotting.")


def part3_two_keys_long():
    section("3. Two grouping keys, in long form")
    df = frame()
    counts = (df.groupby(["region", "year"], observed=True)["event_id"]
              .count()
              .rename("n_events"))
    print(f"  long form: {len(counts)} rows = regions x years observed")
    print(counts.head(12).to_string())
    print("  ...")
    print()
    print("  Long form is the form to aggregate, filter and plot in.")
    print("  It scales to a third key without changing shape.")


def part4_wide():
    section("4. Reshaping long to wide")
    df = frame()
    long = (df.groupby(["region", "year"], observed=True)["event_id"]
            .count().rename("n_events"))
    wide = long.unstack(fill_value=0)
    print("  long.unstack(fill_value=0) -- index = region, columns = year:")
    print(wide.to_string())
    print()
    print("  Also available in one step, and able to aggregate on the way:")
    pivot = df.pivot_table(index="region", columns="year", values="depth_km",
                           aggfunc="median")
    print("  df.pivot_table(values='depth_km', aggfunc='median'):")
    print(pivot.round(1).to_string())
    print()
    print("  Sign convention: 'long' one row per observation, 'wide' one row")
    print("  per region. pivot_table produces wide directly; unstack goes")
    print("  long -> wide after grouping. Both are the same reshape.")


def part5_melt_back():
    section("5. Reshaping wide back to long")
    df = frame()
    wide = (df.groupby(["region", "year"], observed=True)["event_id"]
            .count().rename("n_events").unstack(fill_value=0))
    back = (wide.reset_index()
            .melt(id_vars="region", var_name="year", value_name="n_events"))
    print(f"  wide shape {wide.shape} -> melted shape {back.shape}")
    print(back.head(8).to_string(index=False))
    print()
    print("  Round-trip check, sorted identically:")
    original = (df.groupby(["region", "year"], observed=True)["event_id"]
                .count().rename("n_events").reset_index())
    same = original.merge(back, on=["region", "year"],
                          suffixes=("_orig", "_melted"))
    equal = bool((same["n_events_orig"] == same["n_events_melted"]).all())
    print(f"    long -> wide -> long reproduces the original counts: {equal}")
    print(f"    rows compared: {len(same)}")


def part6_transform():
    section("6. transform: same grouping, different output shape")
    df = frame()
    df["region_median_mw"] = df.groupby("region", observed=True)["mw"].transform("median")
    df["mw_anomaly"] = df["mw"] - df["region_median_mw"]
    print("  agg reduces each group to one number; transform returns one number")
    print("  PER ROW, so it can be aligned straight back onto the frame:")
    print(df[["event_id", "region", "mw", "region_median_mw", "mw_anomaly"]]
          .head(6).to_string(index=False))
    print()
    print("  Cross-check against the explicit broadcast:")
    med = df.groupby("region", observed=True)["mw"].median()
    manual = df["mw"] - df["region"].map(med)
    diff = (manual - df["mw_anomaly"]).abs().max()
    print(f"    max |df minus hand-written map()| = {diff}")
    print()
    print("  The largest magnitude excess over its own region's median:")
    top = df.nlargest(3, "mw_anomaly")[
        ["event_id", "region", "mw", "region_median_mw", "mw_anomaly"]]
    print(top.to_string(index=False))


def part7_derived_column():
    section("7. Aggregating a derived (non-linear) column")
    df = frame()
    by_region = df.groupby("region", observed=True).agg(
        sum_energy_j=("energy_j", "sum"),
        max_energy_j=("energy_j", "max"),
    )
    by_region["share_of_total"] = (by_region["sum_energy_j"]
                                   / by_region["sum_energy_j"].sum())
    print("  Energy is 10^(1.5 M + 4.8) J, so the largest events dominate the")
    print("  sum. Aggregating energy is NOT the same as aggregating magnitude:")
    print(by_region.assign(
        sum_energy_j=by_region["sum_energy_j"].map("{:.3e}".format),
        max_energy_j=by_region["max_energy_j"].map("{:.3e}".format),
    ).to_string())
    print()
    counts = df.groupby("region", observed=True).size().rename("n_events")
    cmp = pd.concat([counts, by_region], axis=1)
    cmp["event_share"] = cmp["n_events"] / cmp["n_events"].sum()
    cmp["energy_share"] = cmp["sum_energy_j"] / cmp["sum_energy_j"].sum()
    print(cmp[["n_events", "event_share", "energy_share"]].round(4).to_string())
    print()
    print("  One region contributes a smaller share of the events than of the")
    print("  energy. Reporting only event counts would hide that; this is why")
    print("  the choice of aggregation statistic is a scientific choice.")


if __name__ == "__main__":
    print("SYNTHETIC catalogue: generated in-code, not an observation of the"
          "\nEarth and not the USGS catalogue.  See synthetic_catalog.py.")
    part1_groupby_basics()
    part2_named_aggregation()
    part3_two_keys_long()
    part4_wide()
    part5_melt_back()
    part6_transform()
    part7_derived_column()
