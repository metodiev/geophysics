"""Indexing, selection, loc/iloc and boolean masks.

Run:  .venv/bin/python 03-scientific-computing/04-pandas/code/indexing_selection_demo.py
Requires: pandas (installed in the project venv).

Companion to lesson 03-04-02.  The catalogue is SYNTHETIC (see
``synthetic_catalog.py``); it is not the USGS catalogue.

Demonstrates:

1. Boolean masks, and the one operator-precedence trap that bites everyone.
2. ``.loc`` (label) versus ``.iloc`` (position) on the same frame.
3. Single-step selection and assignment with ``.loc[mask, column]``.
4. The chained-assignment trap as it actually behaves under pandas 3
   Copy-on-Write: a ChainedAssignmentError warning, and *no* modification.
5. ``isin``, ``between`` and ``query`` for readable conditions.
"""

import warnings

import pandas as pd

import synthetic_catalog as sc


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def cleaned():
    """Deduplicated frame, so row selections are unambiguous."""
    return sc.raw_catalog().drop_duplicates("event_id", keep="first")


def part1_boolean_masks():
    section("1. Boolean masks: selection by condition")
    df = cleaned()
    shallow = df["depth_km"] < 30.0
    strong = df["mw"] >= 3.0
    print(f"  rows in frame                      : {len(df)}")
    print(f"  depth_km < 30                      : {int(shallow.sum())}")
    print(f"  mw >= 3.0                          : {int(strong.sum())}")
    both = shallow & strong
    print(f"  shallow AND strong (&)             : {int(both.sum())}")
    either = shallow | strong
    print(f"  shallow OR strong (|)              : {int(either.sum())}")
    print(f"  NOT shallow (~)                    : {int((~shallow).sum())}")
    print()
    print("  Prescription: put every comparison in parentheses. '&' binds")
    print("  tighter than 'and' does in Python's grammar, so without")
    print("  parentheses the expression is parsed as something else:")
    print("    correct : df[(df['mw'] > 2.0) & (df['depth_km'] < 30.0)]")
    try:
        df["mw"] > 2.0 & df["depth_km"] < 30.0        # missing parentheses
    except Exception as exc:                          # noqa: BLE001
        print(f"    wrong   : df[df['mw'] > 2.0 & df['depth_km'] < 30.0]")
        print(f"              -> {type(exc).__name__}: {exc}")
    print()
    result = df[(df["mw"] >= 4.0) & (df["depth_km"].between(0, 70))]
    print(f"  Events with mw >= 4.0 and 0 <= depth <= 70 km: {len(result)}")
    print(result[["event_id", "origin_time", "mw", "depth_km", "region"]]
          .to_string(index=False))


def part2_loc_versus_iloc():
    section("2. .loc is by label, .iloc is by position -- never mixed up")
    df = cleaned().set_index("event_id")
    print("  index is now event_id; the frame is sorted by origin_time:")
    print(df.head(4)[["origin_time", "mw", "depth_km"]].to_string())
    print()
    print("  .iloc[0:3]  -> first three ROWS by position (stop is exclusive):")
    print(f"    labels {list(df.iloc[0:3].index)}")
    print("  .loc['S0002':'S0005'] -> rows by LABEL (stop is INCLUSIVE):")
    print(f"    labels {list(df.loc['S0002':'S0005'].index)}")
    print()
    print("  The inclusivity asymmetry is deliberate (loc slices like a")
    print("  labelled range, iloc like a Python range) and it is the single")
    print("  most common off-by-one when the two are confused.")
    print()
    print("  Scalar, row and cell access:")
    print(f"    df.loc['S0003', 'mw']            = {df.loc['S0003', 'mw']}")
    print(f"    df.iloc[2]['depth_km']           = {df.iloc[2]['depth_km']}")
    print(f"    df.at['S0003', 'region']         = {df.at['S0003', 'region']}")
    print(f"    df.iat[2, 3] (row 2, col 3 pos)  = {df.iat[2, 3]}"
          "   <- column 3 is depth_km")
    print(f"    columns by position: {list(enumerate(df.columns))[:4]} ...")


def part3_loc_selection_and_set():
    section("3. Select and assign in one step with .loc[mask, column]")
    df = cleaned()
    deep = df["depth_km"] > 60.0
    print(f"  events deeper than 60 km: {int(deep.sum())}")
    print("  their current agency labels:")
    print(df.loc[deep, "agency"].value_counts().to_string())
    print()
    df.loc[deep, "agency"] = "SYN-REVIEW"
    print("  after df.loc[deep, 'agency'] = 'SYN-REVIEW':")
    print(df.loc[deep, "agency"].value_counts().to_string())
    print(f"  rows touched: {int(deep.sum())} -- one row per True mask entry,")
    print("  no loop, no index arithmetic, no possibility of a positional slip.")


def part4_chained_assignment():
    section("4. The chained-assignment trap (and how pandas 3 reports it)")
    df = cleaned()
    before = df.loc[df["depth_km"] > 60.0, "mag_type"].iloc[0]

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        df[df["depth_km"] > 60.0]["mag_type"] = "XX"      # chained: wrong
    print(f"  warnings raised: "
          f"{[w.category.__name__ for w in caught]}")
    if caught:
        first = str(caught[0].message).splitlines()[0]
        print(f"  message begins : {first}")
    after = df.loc[df["depth_km"] > 60.0, "mag_type"].iloc[0]
    print(f"  mag_type of that first deep event before : {before!r}")
    print(f"  mag_type of that first deep event after  : {after!r}")
    print(f"  -> modified? {before != after}")
    print()
    print("  The chained form makes an intermediate object and writes to it.")
    print("  Under Copy-on-Write (pandas 3, always on) that intermediate is a")
    print("  copy, so the write is discarded. pandas 3 raises")
    print("  ChainedAssignmentError, a Warning subclass that says so; the old")
    print("  SettingWithCopyWarning no longer exists in pandas 3.")
    print()
    print("  The one-step form writes to the frame itself, so it sticks:")
    with warnings.catch_warnings(record=True) as caught2:
        warnings.simplefilter("always")
        df.loc[df["depth_km"] > 60.0, "mag_type"] = "Mw-review"
    print(f"  warnings raised: "
          f"{[w.category.__name__ for w in caught2] or 'none'}")
    print("  first five mag_type values now:")
    print(df["mag_type"].value_counts().to_string())


def part5_readable_conditions():
    section("5. isin, between and query for readable conditions")
    df = cleaned()
    wanted = df["region"].isin(["Northvale", "Westhold"])
    print(f"  region in {{Northvale, Westhold}} (isin) : {int(wanted.sum())}")
    print(f"  depth between 10 and 25 km (between)   : "
          f"{int(df['depth_km'].between(10, 25).sum())}")
    print(f"  magnitude between 3.5 and 4.5          : "
          f"{int(df['mw'].between(3.5, 4.5).sum())}")
    print()
    q = df.query("mw >= 3.5 and depth_km < 20 and region in @wanted_regions",
                 local_dict={"wanted_regions": ["Northvale", "Southgate"]})
    print("  query('mw >= 3.5 and depth_km < 20 and region in @wanted_regions')")
    print(f"  result: {len(q)} events")
    print(q[["event_id", "mw", "depth_km", "region"]].to_string(index=False))
    print()
    print("  query() is the same mask machinery with the parentheses spelled")
    print("  for you; it is a readability tool, not a different execution path.")


if __name__ == "__main__":
    print("SYNTHETIC catalogue: generated in-code, not an observation of the"
          "\nEarth and not the USGS catalogue.  See synthetic_catalog.py.")
    part1_boolean_masks()
    part2_loc_versus_iloc()
    part3_loc_selection_and_set()
    part4_chained_assignment()
    part5_readable_conditions()
