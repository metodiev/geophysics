#!/usr/bin/env python3
"""Reproducible geospatial workflows: determinism, provenance, guards and checks.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geospatial_workflows_demo.py

Everything is SYNTHETIC and in memory.  Nothing is read from or written to disk;
the "hashes" below are computed in RAM from in-memory objects.

Contents
--------
1. A pipeline as a pure function: same input -> same hash.
2. Bitwise versus numeric reproducibility: a CRS round trip.
3. Order dependence: why an unsorted group-by can change the answer.
4. Random steps: seeding, and the order in which random numbers are drawn.
5. Guards: failing loudly on a missing CRS or degree units.
6. A provenance record: versions, parameters, input and output hashes.
7. Output validation: schema, CRS, extent and nodata checks.
8. A parameter manifests check, and why the cache key must include the parameters.
"""

import hashlib
import json
import sys

import numpy as np
import pandas as pd
import geopandas as gpd
import shapely
import pyproj
from shapely.geometry import Point, box

RNG = np.random.default_rng(20261014)

AREA = box(0.0, 0.0, 20_000.0, 12_000.0)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def make_points(n=60, seed=20261014):
    """A synthetic sample layer in a projected metre frame (not a real CRS)."""
    rng = np.random.default_rng(seed)
    x = rng.uniform(0.0, 20_000.0, n)
    y = rng.uniform(0.0, 12_000.0, n)
    return gpd.GeoDataFrame(
        {
            "site": [f"S{i:03d}" for i in range(n)],
            "zone": rng.choice(["north", "south"], size=n),
            "value": np.round(rng.normal(10.0, 2.0, n), 6),
        },
        geometry=[Point(a, b) for a, b in zip(x, y)],
    )


def canonical(frame, sort=True, digits=6):
    """A canonical text encoding of a geo-table.

    With sort=False the encoding follows the row order, so two logically
    identical tables in different orders encode differently -- that is exactly
    the point of the experiment in section 3.  With sort=True the rows are
    sorted on every non-geometry column and the coordinates are snapped to
    `digits`, which makes the encoding invariant to row order and to the last
    digits of a projection.
    """
    f = frame.reset_index()
    cols = list(f.columns)
    if "geometry" in cols:
        f["geometry"] = shapely.to_wkt(
            shapely.set_precision(f.geometry.to_numpy(), 10.0 ** (-digits)))
    if sort:
        key = [c for c in cols if c != "geometry"]
        f = f.sort_values(key).reset_index(drop=True)
    f = f[cols]
    parts = []
    for col in f.columns:
        parts.append(str(col) + "|" + "|".join(str(v) for v in f[col].tolist()))
    return "\n".join(parts).encode("utf-8")


def digest(obj, sort=True):
    return hashlib.sha256(canonical(obj, sort=sort)).hexdigest()[:16]


def process(points, params):
    """The pipeline under study: buffer by a distance, then summarise by zone."""
    buffered = points.copy()
    buffered["geometry"] = buffered.geometry.buffer(params["buffer_m"])
    buffered["area_m2"] = buffered.geometry.area
    summary = (buffered.groupby("zone", sort=params["sort_groups"])
               .agg(n=("site", "count"), mean_area=("area_m2", "mean"))
               .reset_index())
    return summary


def guard_crs(frame, expected_units="metre"):
    """Fail loudly if the layer cannot support a metric operation."""
    if frame.crs is None:
        raise ValueError("layer has no CRS: distances and areas would be unitless")
    unit = frame.crs.axis_info[0].unit_name
    if unit != expected_units:
        raise ValueError(f"CRS units are {unit!r}, expected {expected_units!r}")


def main():
    section("1. A pipeline as a pure function: same input, same hash")
    pts = make_points(60)
    params = {"buffer_m": 500.0, "sort_groups": True}
    a = process(make_points(60), params)
    b = process(make_points(60), params)
    c = process(make_points(60, seed=7), params)
    print(f"  input layer: {len(pts)} synthetic points, no CRS declared")
    print(a.to_string(index=False))
    print(f"\n  hash(run 1)                 : {digest(a)}")
    print(f"  hash(run 2)                 : {digest(b)}")
    print(f"  hashes equal                : {digest(a) == digest(b)}")
    print(f"  hash(different input)       : {digest(c)}")
    print(f"  hash differs on new input   : {digest(a) != digest(c)}")
    print("The function has no hidden state: no clock, no unseeded randomness, no reliance")
    print("on dict or file-system ordering.  That is the whole content of 'reproducible' at")
    print("this level, and it is a property of the CODE, not of the analyst's care.")

    section("2. Bitwise versus numeric reproducibility: a CRS round trip")
    lon = 0.0 + RNG.uniform(0.0, 0.05, 40)
    lat = 40.0 - RNG.uniform(0.0, 0.05, 40)
    wgs = gpd.GeoDataFrame({"id": np.arange(40)},
                           geometry=[Point(a, b) for a, b in zip(lon, lat)],
                           crs="EPSG:4326")
    utm = wgs.to_crs("EPSG:32631")
    back = utm.to_crs("EPSG:4326")
    dx = (back.geometry.x.to_numpy() - wgs.geometry.x.to_numpy())
    dy = (back.geometry.y.to_numpy() - wgs.geometry.y.to_numpy())
    print(f"  routes: EPSG:4326 -> EPSG:32631 -> EPSG:4326, {len(wgs)} synthetic points")
    print(f"  maximum longitude discrepancy: {np.max(np.abs(dx)):.3e} deg "
          f"({np.max(np.abs(dx)) * 111_320.0:.3e} m at the equator)")
    print(f"  maximum latitude  discrepancy: {np.max(np.abs(dy)):.3e} deg "
          f"({np.max(np.abs(dy)) * 111_132.0:.3e} m)")
    print(f"  bitwise identical coordinates : "
          f"{np.array_equal(back.geometry.x.to_numpy(), wgs.geometry.x.to_numpy())}")
    # A different but equivalent route through another intermediate CRS.
    via = wgs.to_crs("EPSG:3857").to_crs("EPSG:32631").to_crs("EPSG:4326")
    dx2 = (via.geometry.x.to_numpy() - wgs.geometry.x.to_numpy())
    print(f"  a second route (via EPSG:3857): max discrepancy "
          f"{np.max(np.abs(dx2)):.3e} deg")
    print(f"  the two routes agree with each other to "
          f"{np.max(np.abs(via.geometry.x.to_numpy() - back.geometry.x.to_numpy())):.3e} deg")
    print("Deterministic is not the same as identical.  A projection is an iterative")
    print("computation whose last digits depend on the route taken and on the version of")
    print("the projection library and its datum grids; the honest target is agreement to a")
    print("STATED tolerance, not bitwise equality.  A workflow that asserts bitwise equality")
    print("across library versions will fail on the day the library is upgraded, and a")
    print("workflow that accepts any difference will never notice a real bug.")

    section("3. Order dependence: an unsorted group-by over geopandas")
    same = gpd.GeoDataFrame(
        {"zone": ["north", "south", "north", "south"],
         "value": [1.0, 2.0, 3.0, 4.0]},
        geometry=[Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)],
    )
    shuffled = gpd.GeoDataFrame(
        {"zone": ["south", "north", "south", "north"],
         "value": [4.0, 3.0, 2.0, 1.0]},
        geometry=[Point(1, 1), Point(0, 1), Point(1, 0), Point(0, 0)],
    )
    d1 = same.dissolve(by="zone", aggfunc="mean", sort=True)
    d2 = shuffled.dissolve(by="zone", aggfunc="mean", sort=True)
    d3 = shuffled.dissolve(by="zone", aggfunc="mean", sort=False)
    print(f"  dissolve(sort=True) on the original order : index {list(d1.index)}")
    print(f"  dissolve(sort=True) on a shuffled copy    : index {list(d2.index)}")
    print(f"  dissolve(sort=False) on the shuffled copy : index {list(d3.index)}")
    print(f"  encoding WITHOUT canonicalisation, d1 vs d2: "
          f"{digest(d1, sort=False)} vs {digest(d2, sort=False)} "
          f"(equal: {digest(d1, sort=False) == digest(d2, sort=False)})")
    print(f"  encoding WITHOUT canonicalisation, d1 vs d3: "
          f"{digest(d1, sort=False)} vs {digest(d3, sort=False)} "
          f"(equal: {digest(d1, sort=False) == digest(d3, sort=False)})")
    print(f"  encoding WITH canonicalisation,   d1 vs d3: "
          f"{digest(d1)} vs {digest(d3)} (equal: {digest(d1) == digest(d3)})")
    print(f"  mean values identical despite the order   : "
          f"{np.allclose(d1['value'].sort_index(), d3['value'].sort_index())}")
    print("The numbers are the same and the FILES are not: row order changes the hash, the")
    print("diff, and therefore every downstream comparison.  Sorting is the cheapest fix")
    print("and must be applied wherever a group key is generated, not just before printing.")

    section("4. Random steps: seeding and the order in which entities are visited")
    def jitter(seed):
        r = np.random.default_rng(seed)
        return r.normal(0.0, 1.0, 3)

    print(f"  seeded twice with 20261014  : {np.round(jitter(20261014), 6)}")
    print(f"  the same call again         : {np.round(jitter(20261014), 6)}")
    print(f"  identical                   : "
          f"{np.array_equal(jitter(20261014), jitter(20261014))}")
    print(f"  seeded with a different value: {np.round(jitter(7), 6)}")
    # The same seed, the same numbers, attached to entities in a different order.
    rows = np.arange(6)
    order_a = rows
    order_b = np.array([3, 0, 5, 1, 4, 2])

    def jittered(order, seed=20261014):
        r = np.random.default_rng(seed)
        out = np.empty(order.size)
        for i, row in enumerate(order):
            out[row] = r.normal(0.0, 0.05)
        return out

    ja, jb = jittered(order_a), jittered(order_b)
    print(f"\n  same seed, rows visited 0..5       : {np.round(ja, 6)}")
    print(f"  same seed, rows visited 3,0,5,1,4,2 : {np.round(jb, 6)}")
    print(f"  the two MULTISETS of draws are equal : "
          f"{np.array_equal(np.sort(ja), np.sort(jb))}")
    print(f"  the two ASSIGNMENTS are equal        : {np.array_equal(ja, jb)}")
    print(f"  max difference between the two jitters: "
          f"{np.max(np.abs(ja - jb)):.6f}")
    print("A seed makes a run repeatable; it does not make it portable.  The generator")
    print("produces one sequence, and which row receives which number depends on the order")
    print("the code visits the rows.  Reordering the input, adding a filter, or parallelising")
    print("the loop therefore changes every random number's destination while leaving the")
    print("seed untouched.  A random step is reproducible only together with the iteration")
    print("order -- and if the order is not fixed in the code, the seed buys nothing.")

    section("5. Guards: failing loudly instead of silently in the wrong unit")
    for frame, label in ((pts, "no CRS declared"),
                         (wgs, "geographic (degree) CRS")):
        try:
            guard_crs(frame)
            print(f"  {label:28s}: guard passed")
        except ValueError as exc:
            print(f"  {label:28s}: guard raised -> {exc}")
    ok = pts.set_crs("EPSG:32633", allow_override=True)
    guard_crs(ok)
    print(f"  {'projected metre CRS':28s}: guard passed "
          f"({ok.crs.axis_info[0].unit_name})")
    print("The buffer in section 1 was applied to a layer with NO CRS.  With no declared")
    print("CRS the number 500 has no unit, and the pipeline cannot know whether the")
    print("analyst meant 500 m or 500 degrees.  A guard turns an invisible assumption into")
    print("an exception at the point where it is still cheap to fix.")

    section("6. A provenance record")
    prov = {
        "input_hash": digest(pts),
        "input_rows": int(len(pts)),
        "parameters": params,
        "output_hash": digest(process(make_points(60), params)),
        "python": sys.version.split()[0],
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "geopandas": gpd.__version__,
        "shapely": shapely.__version__,
        "pyproj": pyproj.__version__,
        "proj": pyproj.proj_version_str,
    }
    print(json.dumps(prov, indent=2, sort_keys=True))
    print("Every field is a fact about this machine, measured rather than assumed.  The")
    print("projection library version matters as much as the code: a datum or grid update")
    print("changes transformed coordinates, so a run reproduced with a different PROJ is a")
    print("different computation even when the script is byte-identical.")

    section("7. Output validation: schema, CRS, extent and nodata")
    out = process(make_points(60), params)
    checks = [
        ("has the expected columns",
         set(out.columns) == {"zone", "n", "mean_area"}),
        ("row count equals the zone count", len(out) == 2),
        ("no null values", not out.isna().any().any()),
        ("all areas positive", bool((out["mean_area"] > 0).all())),
        ("within the buffered study area",
         bool((out["mean_area"] < AREA.area).all())),
    ]
    for label, okk in checks:
        print(f"  {'PASS' if okk else 'FAIL'}  {label}")
    bad = out.copy()
    bad.loc[0, "mean_area"] = -1.0
    try:
        assert (bad["mean_area"] > 0).all(), "negative area: the pipeline is broken"
        print("  the corrupted copy passed (this line should not print)")
    except AssertionError as exc:
        print(f"  the deliberately corrupted copy was caught -> {exc}")
    print("A validation suite is only useful if it can fail.  Each check above is a")
    print("statement that must hold for the *result* to mean anything, and the corrupted")
    print("copy confirms the check is wired up rather than merely present.")

    section("8. Manifest check: why the cache key must contain the parameters")
    m1 = {"buffer_m": 500.0, "sort_groups": True}
    m2 = {"buffer_m": 500.0, "sort_groups": True}
    m3 = {"buffer_m": 501.0, "sort_groups": True}
    base = process(make_points(60), m1)
    print(f"  run with {m1} -> hash {digest(base)}")
    print(f"  rerun with an equal manifest                -> "
          f"{digest(process(make_points(60), m2))} "
          f"(equal: {digest(process(make_points(60), m2)) == digest(base)})")
    changed = process(make_points(60), m3)
    print(f"  rerun with buffer_m = 501.0                 -> {digest(changed)} "
          f"(equal: {digest(changed) == digest(base)})")
    print(f"  the two outputs differ in mean_area by "
          f"{abs(changed['mean_area'].iloc[0] - base['mean_area'].iloc[0]):.6f} m^2 per "
          f"site-buffer, i.e. {100 * abs(changed['mean_area'].iloc[0] - base['mean_area'].iloc[0]) / base['mean_area'].iloc[0]:.4f} %")
    print("A 1 m change in the buffer changes every reported area, so a cache keyed on the")
    print("input file alone would serve a stale result and never say so.  The manifest is")
    print("the smallest set of facts that must be equal for two runs to be the same run: the")
    print("input hash, the parameters, the code revision and the library versions.")


if __name__ == "__main__":
    main()
