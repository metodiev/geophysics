"""Merging, joining and aligning irregular time series.

Run:  .venv/bin/python 03-scientific-computing/04-pandas/code/merging_time_series_demo.py
Requires: pandas (installed in the project venv).

Companion to lesson 03-04-05.  All tables are SYNTHETIC (see
``synthetic_catalog.py``); they are not the USGS catalogue and not real station
metadata.

Demonstrates:

1. A join on a UNIQUE key: events to a region-lookup table. Row count preserved.
2. A join on a NON-UNIQUE key: events to stations on ``region``. Row count
   multiplied -- and per-event totals silently inflated.
3. The fix: aggregate before the join, or join on a unique key.
4. Aligning two irregular time series with an explicit outer ``reindex``.
5. ``merge_asof`` for a nearest-preceding match, with a tolerance.
"""

import numpy as np
import pandas as pd

import synthetic_catalog as sc


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def events():
    df = sc.clean_catalog().copy()
    df["energy_j"] = sc.mag_to_energy_j(df["mw"])
    return df


def part1_unique_key_join():
    section("1. A join on a unique key preserves the row count")
    df = events()
    lookup = pd.DataFrame(
        {
            "region": list(sc.REGIONS),
            "region_code": ["R1", "R2", "R3", "R4"],
            "tectonic_class": ["transitional", "subduction", "strike-slip",
                               "extensional"],
        }
    )
    print(f"  events   : {len(df)} rows, key 'region' unique in the lookup? "
          f"{lookup['region'].is_unique}")
    print(f"  lookup   : {len(lookup)} rows, one per region")
    merged = df.merge(lookup, on="region", how="left", validate="many_to_one")
    print(f"  merged   : {len(merged)} rows (unchanged)")
    print()
    print("  validate='many_to_one' is an assertion, not decoration: it")
    print("  raises if 'region' is ever duplicated in the lookup, which turns")
    print("  an accidental row explosion into a loud error at the join.")
    print()
    print(merged.groupby("tectonic_class", observed=True)
          .agg(n_events=("event_id", "count"), max_mw=("mw", "max"))
          .to_string())


def part2_non_unique_key_join():
    section("2. A join on a non-unique key multiplies rows")
    df = events()
    stations = sc.station_table()
    print(f"  events  : {len(df)} rows")
    print(f"  stations: {len(stations)} rows")
    print("  key     : 'region' on both sides -- NON-unique on both sides")
    print()
    print("  stations per region:")
    print(stations["region"].value_counts().sort_index().to_string())
    print()
    naive = df.merge(stations, on="region", how="inner")
    print(f"  naive merge result: {len(naive)} rows "
          f"(= sum over regions of events x stations)")
    print()
    print("  Every event now appears once per station in its region:")
    per_event = naive.groupby("event_id", observed=True).size()
    print(f"    rows per event: min = {per_event.min()}, "
          f"max = {per_event.max()}")
    print()
    print("  The damage: a per-event total summed AFTER the merge is inflated")
    print("  by the number of stations in the region.")
    print(f"    total energy, events alone        : "
          f"{df['energy_j'].sum():.4e} J")
    print(f"    total energy, after the bad merge : "
          f"{naive['energy_j'].sum():.4e} J")
    print(f"    inflation factor                  : "
          f"{naive['energy_j'].sum() / df['energy_j'].sum():.4f}")
    print()
    print("  The number is plausible, the units are right, and it is wrong.")
    print("  Nothing warned; a row count would have.")
    print()
    print("  Two correct alternatives:")
    print("    (a) join on a unique key -- here, region_code:")
    code = stations[["station_id", "region"]].merge(
        pd.DataFrame({"region": list(sc.REGIONS),
                      "region_code": ["R1", "R2", "R3", "R4"]}),
        on="region", how="left")
    print(f"        station rows after the lookup: {len(code)} (unchanged)")
    print("    (b) aggregate first, then join the summary to the detail:")
    summary = (df.groupby("region", observed=True)
               .agg(n_events=("event_id", "count"),
                    mean_mw=("mw", "mean")))
    both = stations.merge(summary, on="region", how="left")
    print(f"        station table enriched with region aggregates: "
          f"{len(both)} rows (still one per station)")
    print(both[["station_id", "region", "n_events", "mean_mw"]]
          .head(4).round(3).to_string(index=False))


def part3_outer_join_unmatched_keys():
    section("3. Outer joins keep unmatched keys -- and say so with NaN")
    df = events()
    stations = sc.station_table()
    left = (df.groupby("region", observed=True)["event_id"].count()
            .rename("n_events"))
    right = (stations.groupby("region", observed=True)["station_id"].count()
             .rename("n_stations"))
    outer = pd.concat([left, right], axis=1)
    outer["events_per_station"] = outer["n_events"] / outer["n_stations"]
    print("  concat(axis=1) is an outer join on the index:")
    print(outer.to_string())
    print()
    print("  Outerisle has stations and no events, so n_events is NaN and the")
    print("  ratio is NaN. That is the correct report: dividing by zero events")
    print("  is undefined, not infinite, and NaN is how pandas says so.")
    print()
    inner = left.to_frame().join(right, how="inner")
    print(f"  how='inner' would keep {len(inner)} regions and drop Outerisle")
    print(f"  silently. An outer join keeps it and marks it.")


def part4_aligning_irregular_series():
    section("4. Aligning two irregular time series")
    counts = sc.daily_event_counts()
    heads = sc.groundwater_series()
    print(f"  daily event counts : {len(counts)} observations")
    print(f"    from {counts.index.min()} to {counts.index.max()}")
    print(f"  groundwater levels : {len(heads)} observations")
    print(f"    from {heads.index.min()} to {heads.index.max()}")
    print()
    overlap = counts.index.intersection(heads.index)
    union = counts.index.union(heads.index)
    print(f"  timestamps in both series       : {len(overlap)}")
    print(f"  timestamps in the union         : {len(union)}")
    print(f"  union timestamps missing from one series or the other: "
          f"{len(union) - len(overlap)}")
    print("  The two series were sampled on different days with different")
    print("  calendars, so they cannot simply be laid side by side: the")
    print("  alignment has to be an explicit decision, and the decision changes")
    print("  how many usable rows exist.")
    print()
    print("  Option A: reindex both onto the union of all timestamps:")
    combined = pd.DataFrame({
        "n_events": counts.reindex(union),
        "head_m": heads.reindex(union),
    })
    print(f"    union has {len(union)} timestamps; "
          f"missing = {int(combined['n_events'].isna().sum())} event days, "
          f"{int(combined['head_m'].isna().sum())} head days")
    print(combined.head(4).to_string())
    print()
    print("  Option B: resample onto a common regular calendar period:")
    monthly_events = counts.resample("ME").sum().rename("n_events")
    monthly_head = heads.resample("ME").mean().rename("head_m_mean")
    monthly = pd.concat([monthly_events, monthly_head], axis=1)
    print(f"    monthly frame: {len(monthly)} rows")
    print(monthly.head(5).round(3).to_string())
    print()
    print("  Which is correct depends on what the number means: a count")
    print("  resampled by .sum() is still a count, whereas a level resampled by")
    print("  .sum() would be a meaningless 'total metres'.")


def part5_merge_asof():
    section("5. merge_asof: pair each observation with the nearest PRECEDING one")
    counts = sc.daily_event_counts()
    heads = sc.groundwater_series()
    left = counts.rename("n_events").rename_axis("date").reset_index()
    right = heads.rename("head_m").rename_axis("date").reset_index()
    print("  merge_asof requires both frames sorted on the key column:")
    print(f"    left sorted  : {left['date'].is_monotonic_increasing}")
    print(f"    right sorted : {right['date'].is_monotonic_increasing}")
    print()
    joined = pd.merge_asof(left, right, on="date", direction="backward",
                           tolerance=pd.Timedelta("5D"))
    print(f"  joined rows: {len(joined)} (same as left, as a backward asof")
    print("  never creates a row)")
    print(f"  rows with a head_m value inside the 5-day tolerance: "
          f"{int(joined['head_m'].notna().sum())} of {len(joined)}")
    print()
    print(joined.head(6).round(3).to_string(index=False))
    print()
    print("  direction='backward' means 'the most recent measurement at or")
    print("  before this date'. 'nearest' picks either side and can therefore")
    print("  use a measurement that had not been taken yet -- a look-ahead bug")
    print("  in anything forecast-like. The tolerance prevents pairing a day")
    print("  with a measurement from months earlier, which would otherwise")
    print("  happen silently at the start of the record.")


if __name__ == "__main__":
    print("SYNTHETIC tables: generated in-code, not observations of the Earth,"
          "\nnot the USGS catalogue and not real station metadata.")
    part1_unique_key_join()
    part2_non_unique_key_join()
    part3_outer_join_unmatched_keys()
    part4_aligning_irregular_series()
    part5_merge_asof()
