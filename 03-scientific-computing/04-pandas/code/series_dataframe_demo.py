"""Series, DataFrame and the labeled-data model.

Run:  .venv/bin/python 03-scientific-computing/04-pandas/code/series_dataframe_demo.py
Requires: pandas (installed in the project venv).

Companion to lesson 03-04-01.  The catalogue is SYNTHETIC (see
``synthetic_catalog.py``); it is not the USGS catalogue.

Demonstrates:

1. What a pandas Series adds to a NumPy array: an index.
2. The bug class a labelled axis prevents -- arithmetic that pairs values by
   *position* when the analyst meant to pair them by *name*.
3. A DataFrame as a dict of aligned Series.
4. Inspection: dtypes, shape, info(), describe().
5. That pandas 3 uses a dedicated string dtype by default.
"""

import numpy as np
import pandas as pd

import synthetic_catalog as sc


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def part1_series_is_array_plus_index():
    section("1. A Series is an array plus a labelled axis")
    raw = sc.raw_catalog()
    depth = raw["depth_km"]
    print(f"  type            : {type(depth).__name__}")
    print(f"  values (ndarray): {type(depth.to_numpy()).__name__} "
          f"dtype={depth.to_numpy().dtype}")
    print(f"  index           : {type(depth.index).__name__}, "
          f"first three = {list(depth.index[:3])}")
    print(f"  name            : {depth.name!r}   (carried by the container)")
    print()
    print("  The index is not decoration: it is what lets a Series answer")
    print("  'which event was this?' without a parallel bookkeeping array.")
    print()
    print("  depth statistics (NaNs skipped, which is the default):")
    print(f"    count = {depth.count()}   mean = {depth.mean():.2f} km"
          f"   median = {depth.median():.2f} km")
    print(f"    min   = {depth.min():.1f} km   max = {depth.max():.1f} km"
          "   <-- note the 999 sentinel")


def part2_positional_versus_label_aligned():
    section("2. The bug a labelled axis prevents")
    # Duplicate reports are set aside here (lesson 03 handles them) so that
    # every label is unique and the alignment argument is unambiguous.
    cat = (sc.raw_catalog()
           .drop_duplicates("event_id", keep="first")
           .set_index("event_id"))
    first = cat[cat["mw"].notna()].head(6)
    a = first["mw"]                                   # ordered by event_id
    b = first.sort_values("mw")["mw"]                 # same events, re-sorted

    print("  The same six events' magnitudes, held in two different orders:")
    print(f"    a (as read)                index: {list(a.index)}")
    print(f"    b (sorted by magnitude)    index: {list(b.index)}")
    print(f"    a values: {a.to_numpy().tolist()}")
    print(f"    b values: {b.to_numpy().tolist()}")
    print()

    naive = a.to_numpy() - b.to_numpy()
    print("  A) array arithmetic, values paired BY POSITION:")
    print(f"     {np.round(naive, 2).tolist()}")
    print("     Every one of those differences is between two different")
    print("     earthquakes. It is a number, and it is meaningless.")
    print()

    aligned = a - b
    print("  B) Series arithmetic, values paired BY LABEL:")
    print(f"     {np.round(aligned.to_numpy(), 3).tolist()}")
    print()
    print("     Zero everywhere, because each pair is the same event. pandas")
    print("     reached that by aligning on the index -- the step a")
    print("     position-based loop silently omits.")


def part3_misalignment_produces_nan():
    section("3. When labels do not match, pandas refuses to invent a pairing")
    cat = (sc.raw_catalog()
           .drop_duplicates("event_id", keep="first")
           .set_index("event_id"))
    ids = list(cat[cat["depth_km"].notna()].index[:5])
    a = cat.loc[ids, "depth_km"].rename("depth_net1")
    outsider = list(cat[cat["depth_km"].notna()].index)[9]
    b = cat.loc[ids[1:] + [outsider], "depth_km"].rename("depth_net2")

    print("  Two networks report depths for overlapping but not identical sets")
    print("  of events:")
    print("    SYN-NET1 reports (depth_net1):")
    print(a.to_string())
    print("    SYN-NET2 reports (depth_net2): the same events except the first,")
    print(f"    plus one it alone recorded ({outsider}):")
    print(b.to_string())
    print()
    joined = pd.concat([a, b], axis=1)
    joined["mean_depth_km"] = joined.mean(axis=1)
    print("  Putting them side by side aligns on the label:")
    print(joined.to_string())
    print()
    print(f"  rows carried through        : {len(joined)} = the union of labels")
    first_id, last_id = a.index[0], b.index[-1]
    print(f"  {first_id} has no SYN-NET2 depth -> depth_net2 = NaN, not zero")
    print(f"  {last_id} has no SYN-NET1 depth -> depth_net1 = NaN, not zero")
    print("  The mean then skips the missing cell rather than reading it as 0.")
    print()
    print("  NaN here is the correct answer: 'no such measurement exists'.")
    print("  Filling it with 0 would assert a depth of 0 km.")


def part4_dataframe():
    section("4. A DataFrame is a dict of Series sharing one index")
    raw = sc.raw_catalog()
    print(f"  shape  : {raw.shape}   (rows, columns)")
    print(f"  index  : {type(raw.index).__name__}, range "
          f"{raw.index.min()}..{raw.index.max()}")
    print(f"  columns: {list(raw.columns)}")
    print()
    print("  dtypes (pandas 3 gives text its own 'str' dtype, not object):")
    print(raw.dtypes.to_string())
    print()
    print("  A Series is one column of that frame, sharing its index:")
    print(f"    raw['mw'].index.equals(raw.index) -> "
          f"{raw['mw'].index.equals(raw.index)}")
    print()
    print("  Selecting several columns keeps the DataFrame and the labels:")
    sub = raw.loc[:3, ["event_id", "origin_time", "mw", "region"]]
    print(sub.to_string(index=False))


def part5_inspection():
    section("5. Looking before you compute")
    raw = sc.raw_catalog()
    print("  head():")
    print(raw.head(3)[["event_id", "origin_time", "mw", "depth_km", "region"]]
          .to_string(index=False))
    print()
    print("  tail():")
    print(raw.tail(3)[["event_id", "origin_time", "mw", "depth_km", "region"]]
          .to_string(index=False))
    print()
    print("  describe() on the numeric columns:")
    print(raw[["depth_km", "mw", "n_stations"]].describe().round(3).to_string())
    print()
    print("  info() gives dtypes, non-null counts and memory in one view:")
    raw.info(memory_usage="deep")
    print()
    print("  A first look at the categorical columns:")
    print(raw["region"].value_counts().to_string())
    print(f"  unique regions: {raw['region'].nunique()}  "
          f"unique agencies: {raw['agency'].nunique()}")
    print(f"  duplicated event_id: {int(raw['event_id'].duplicated().sum())}"
          "   <-- lesson 03 deals with these")


if __name__ == "__main__":
    print("SYNTHETIC catalogue: generated in-code, not an observation of the"
          "\nEarth and not the USGS catalogue.  See synthetic_catalog.py.")
    part1_series_is_array_plus_index()
    part2_positional_versus_label_aligned()
    part3_misalignment_produces_nan()
    part4_dataframe()
    part5_inspection()
