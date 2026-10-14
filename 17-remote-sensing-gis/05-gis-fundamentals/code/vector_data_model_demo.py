#!/usr/bin/env python3
"""Vector data model: geometry types, attribute operations, joins and topology.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python vector_data_model_demo.py

All geometries and attribute values are SYNTHETIC teaching objects built in
memory.  Nothing is read from or written to disk.

Contents
--------
1. The six simple-feature geometry types and what a vertex costs.
2. Attribute operations: filter, assign, group-by, join, concat.
3. An attribute join is a relational join: row counts can multiply.
4. A spatial join: predicate choice changes the answer.
5. A spatial index: candidate pairs versus true intersections.
6. Validity: a self-intersecting ring, make_valid, and the area it changes.
7. Mixed geometry types and missing values: what breaks, and how it fails.
"""

import numpy as np
import pandas as pd
import shapely
import geopandas as gpd
from shapely.geometry import (
    Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon,
    box,
)
from shapely import make_valid, is_valid
from shapely.ops import unary_union

RNG = np.random.default_rng(20261014)

# Synthetic local frame in metres: 20 km x 12 km survey block.  Not a real CRS.
AREA = box(0.0, 0.0, 20_000.0, 12_000.0)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def make_sites(n=40):
    """Synthetic survey sites: a clustered pattern, reproducible from the seed."""
    centres = np.array([[4_000.0, 3_000.0], [15_000.0, 9_000.0]])
    which = RNG.integers(0, 2, size=n)
    xy = centres[which] + RNG.normal(0.0, 900.0, size=(n, 2))
    xy[:, 0] = np.clip(xy[:, 0], 0.0, 20_000.0)
    xy[:, 1] = np.clip(xy[:, 1], 0.0, 12_000.0)
    return gpd.GeoDataFrame(
        {
            "site_id": [f"S{i:03d}" for i in range(n)],
            "rock": RNG.choice(["granite", "schist", "cover"], size=n,
                               p=[0.35, 0.45, 0.20]),
            "conductivity_ms_m": np.round(RNG.lognormal(0.0, 0.7, size=n), 3),
        },
        geometry=[Point(x, y) for x, y in xy],
        crs=None,
    )


def main():
    section("1. Geometry types and the cost of a vertex")
    geoms = [
        ("Point", Point(1_000.0, 2_000.0)),
        ("MultiPoint", MultiPoint([(0.0, 0.0), (1.0, 1.0), (2.0, 0.0)])),
        ("LineString", LineString([(0.0, 0.0), (3.0, 4.0), (6.0, 0.0)])),
        ("MultiLineString", MultiLineString([[(0.0, 0.0), (1.0, 1.0)],
                                            [(1.0, 1.0), (2.0, 0.0)]])),
        ("Polygon", box(0.0, 0.0, 4.0, 3.0)),
        ("MultiPolygon", MultiPolygon([box(0.0, 0.0, 1.0, 1.0),
                                       box(2.0, 2.0, 3.0, 3.0)])),
    ]
    print("  type              dim  n_coords  length(m)  area(m^2)  bounds")
    for name, g in geoms:
        npts = shapely.get_coordinates(g).shape[0]
        length = getattr(g, "length", 0.0)
        area = getattr(g, "area", 0.0)
        print(f"  {name:16s} {shapely.get_dimensions(g):>4d}   {npts:8d}  {length:9.2f} "
              f"{area:10.2f}  {np.round(g.bounds, 1)}")
    print("A geometry is a coordinate sequence plus a type tag.  Everything else --")
    print("length, area, contains -- is *computed* from the coordinates, which is why")
    print("computing them repeatedly in a loop is the usual performance mistake.")
    print("32 bytes of float64 per ordinate (16 bytes per vertex in 2-D) is the")
    print("storage floor of the simple-features model; an indexed shapefile adds a")
    print("fixed 100-byte record header per geometry.")

    section("2. Attribute operations on a layer of points")
    sites = make_sites(40)
    print(f"layer: {len(sites)} rows x {sites.shape[1]} columns "
          f"(includes the geometry column)")
    print("\nfilter: rock == 'granite'")
    gran = sites[sites["rock"] == "granite"]
    print(f"  {len(gran)} of {len(sites)} rows; mean conductivity "
          f"{gran['conductivity_ms_m'].mean():.3f} mS/m")
    print("\nassign: a new attribute derived from existing ones")
    sites = sites.assign(cond_class=pd.cut(
        sites["conductivity_ms_m"], bins=[0.0, 0.5, 1.5, np.inf],
        labels=["low", "medium", "high"]))
    tab = sites.groupby("rock", observed=True).agg(
        n=("site_id", "count"),
        mean_cond=("conductivity_ms_m", "mean"),
        max_cond=("conductivity_ms_m", "max"),
    )
    print(tab.round(3).to_string())
    print("\ngroup-by result is a *new table* with one row per group; the geometry is")
    print("gone unless the aggregation redefines it (a centroid, a convex hull, or a")
    print("dissolve).  This is the commonest silent mistake in attribute GIS:")
    print("statistics are produced for a layer whose geometry no longer matches them.")

    section("3. An attribute join is a relational join: rows can multiply")
    base = pd.DataFrame({
        "site_id": [f"S{i:03d}" for i in range(40)],
        "operator": ["A" if i % 2 == 0 else "B" for i in range(40)],
    })
    # Deliberately non-unique key on the right, and deliberately incomplete.
    rows = []
    for i in range(40):
        n = 0 if i >= 35 else (3 if i < 10 else 2)
        for rep in range(n):
            rows.append((f"S{i:03d}", ["xrf", "assay", "icp"][rep]))
    lab = pd.DataFrame(rows, columns=["site_id", "analysis"])
    lab["value"] = np.round(RNG.normal(10.0, 2.0, size=len(lab)), 3)
    joined = base.merge(lab, on="site_id", how="left")
    matched = joined["value"].notna()
    row_mean = joined.loc[matched, "value"].mean()
    site_mean = joined.loc[matched].groupby("site_id")["value"].mean().mean()
    print(f"  left table rows                 : {len(base)}")
    print(f"  right table rows                : {len(lab)}")
    print(f"  joined rows (how='left')        : {len(joined)}")
    print(f"  sites with no lab result        : "
          f"{joined.loc[~matched, 'site_id'].nunique()} "
          f"(each contributes one NaN row)")
    print(f"  mean of 'value' over matched ROWS     : {row_mean:.4f}")
    print(f"  mean of per-SITE means                : {site_mean:.4f}")
    print(f"  difference caused purely by weighting : "
          f"{row_mean - site_mean:+.4f} ({100 * (row_mean - site_mean) / site_mean:+.3f} %)")
    print("A join duplicates the left row once per matching right row.  Ten sites happen")
    print("to carry three analyses instead of two, so a mean taken over ROWS over-weights")
    print("them by 50%; the difference above is produced entirely by the join, with no")
    print("change to the data.  Row counts before and after every join, plus a decision")
    print("about the unit of analysis (row or site), are the cheapest checks there are.")

    section("4. A spatial join: the predicate changes the answer")
    blocks = gpd.GeoDataFrame(
        {"block": ["west", "east"],
         "land_cover": ["vegetated", "bare"]},
        geometry=[box(0.0, 0.0, 10_000.0, 12_000.0),
                  box(10_000.0, 0.0, 20_000.0, 12_000.0)],
    )
    # Put five sites exactly on the shared boundary x = 10 km.
    on_cut = gpd.GeoDataFrame(
        {"site_id": [f"C{i}" for i in range(5)]},
        geometry=[Point(10_000.0, 1_000.0 + 2_000.0 * i) for i in range(5)],
    )
    all_sites = pd.concat([sites[["site_id", "geometry"]], on_cut],
                          ignore_index=True)
    all_sites = gpd.GeoDataFrame(all_sites, geometry="geometry")
    for pred in ("within", "intersects", "contains"):
        try:
            j = gpd.sjoin(all_sites, blocks, how="left", predicate=pred)
            n_matched = j["block"].notna().sum()
            n_rows = len(j)
        except Exception as exc:                      # predicate not applicable
            n_rows, n_matched = -1, f"error: {type(exc).__name__}"
        print(f"  predicate '{pred:10s}': result rows = {n_rows}, "
              f"matched to a block = {n_matched}")
    print("A site on the shared boundary is in NO block under 'within' (it is on both")
    print("boundaries) and in TWO blocks under 'intersects'.  The row count of a spatial")
    print("join is a *property of the predicate*, and both answers are correct.  The")
    print("analyst's job is to name the predicate and check the row count.")
    print("Note 'contains' is the converse of 'within' -- it asks whether the LEFT")
    print("geometry contains the right one -- so no point can ever contain a block; the")
    print("predicate is not symmetric and swapping the arguments changes the join.")

    section("5. A spatial index: candidate pairs versus true intersections")
    # 30 L-shaped synthetic polygons.  An L is not its own bounding box, so a
    # bounding-box test can admit pairs that do not actually intersect.
    xs = RNG.uniform(0.0, 17_000.0, size=30)
    ys = RNG.uniform(0.0, 9_000.0, size=30)
    ss = RNG.uniform(1_200.0, 2_800.0, size=30)
    lgeoms = []
    for x, y, s in zip(xs, ys, ss):
        h = s / 2.0
        lgeoms.append(Polygon([(x, y), (x + s, y), (x + s, y + h),
                               (x + h, y + h), (x + h, y + s), (x, y + s)]))
    polys = gpd.GeoDataFrame({"id": np.arange(30)}, geometry=lgeoms)
    m = len(polys)
    pairs_all = m * (m - 1) // 2
    sindex = polys.sindex
    cand = set()
    for i, geom in enumerate(polys.geometry):
        for j in sindex.query(geom, predicate="intersects"):
            if int(j) > i:
                cand.add((i, int(j)))
    true_pairs = {
        (i, j) for i in range(m) for j in range(i + 1, m)
        if polys.geometry[i].intersects(polys.geometry[j])
    }
    # Bounding-box-only candidates: how many would a bbox test admit?
    bbox_pairs = set()
    for i in range(m):
        for j in range(i + 1, m):
            if polys.geometry[i].envelope.intersects(polys.geometry[j].envelope):
                bbox_pairs.add((i, j))
    print(f"  geometries                              : {m}")
    print(f"  all unordered pairs (brute force)       : {pairs_all}")
    print(f"  pairs admitted by a bounding-box test   : {len(bbox_pairs)}")
    print(f"  pairs actually intersecting (post-filter): {len(true_pairs)}")
    print(f"  index query returned                    : {len(cand)} pairs")
    print(f"  index agrees with the exact test        : {cand == true_pairs}")
    print(f"  bbox false-positive pairs (bbox but no intersection): "
          f"{len(bbox_pairs) - len(true_pairs)}")
    print(f"  candidate reduction vs brute force      : "
          f"{pairs_all / max(len(cand), 1):.1f}x on {pairs_all} pairs")
    print("The index is exact here (R-tree first, then the exact predicate), not")
    print("approximate: it changes the *cost*, not the answer.  An R-tree never returns a")
    print("false negative for a 'bbox intersects' query, which is exactly why it can be")
    print("used as a filter before the expensive exact test; the false positives it does")
    print("admit are pruned by that second stage.  This is the single most important")
    print("scalability idea in vector GIS.")
    print("\nhow the saving grows with geometry count at CONSTANT density (2 km squares,")
    print("30 per 20 km x 12 km, area scaled with n so the density stays fixed):")
    print("   n_geom   all pairs   bbox candidates   reduction")
    for n in (30, 120, 480):
        scale = np.sqrt(n / 30.0)
        W, H = 20_000.0 * scale, 12_000.0 * scale
        bx = RNG.uniform(0.0, W - 2_000.0, size=n)
        by = RNG.uniform(0.0, H - 2_000.0, size=n)
        g = [box(float(x), float(y), float(x + 2_000.0), float(y + 2_000.0))
             for x, y in zip(bx, by)]
        sidx = gpd.GeoSeries(g).sindex
        c = set()
        for i, gg in enumerate(g):
            for j in sidx.query(gg, predicate="intersects"):
                if int(j) > i:
                    c.add((i, int(j)))
        allp = n * (n - 1) // 2
        print(f"   {n:6d}   {allp:9d}   {len(c):15d}   "
              f"{allp / max(len(c), 1):8.1f}x")
    print("At constant density the brute-force count grows as n^2/2 while the indexed")
    print("candidate set grows about linearly, so the reduction factor grows linearly in")
    print("n.  That is why an index turns an unusable operation into a routine one -- and")
    print("why the same code that is instant on 500 features stalls at 500,000 without one.")

    section("6. Validity: a self-intersecting ring and make_valid")
    bowtie = Polygon([(0.0, 0.0), (2_000.0, 2_000.0), (2_000.0, 0.0), (0.0, 2_000.0)])
    fixed = make_valid(bowtie)
    print(f"  bow-tie vertices              : 4 (no repeated vertex, so it looks fine)")
    print(f"  shapely reports valid         : {is_valid(bowtie)}")
    print(f"  reported .area                : {bowtie.area / 1e6:.6f} km^2")
    print(f"  area of make_valid() result   : {fixed.area / 1e6:.6f} km^2")
    print(f"  type after make_valid         : {fixed.geom_type}")
    print(f"  number of parts               : {len(fixed.geoms)}")
    print(f"  part areas (km^2)             : "
          f"{[round(g.area / 1e6, 6) for g in fixed.geoms]}")
    print("The two lobes are each 1 km^2, so the shape encloses 2 km^2, yet the shoelace")
    print("sum gives exactly 0: the lobes have opposite orientation and cancel.  A")
    print("self-intersecting ring therefore reports a *plausible-looking number* -- here")
    print("0 rather than 2 -- and no arithmetic on the coordinates can tell you that the")
    print("number is meaningless.  Validity is a separate, explicit check.")

    section("7. Mixed geometry types and missing values")
    mixed = gpd.GeoDataFrame(
        {"id": ["a", "b", "c"]},
        geometry=[Point(0.0, 0.0), box(1.0, 1.0, 2.0, 2.0),
                  LineString([(0.0, 0.0), (1.0, 1.0)])],
    )
    print(f"  geom_type of each row          : {list(mixed.geom_type)}")
    print(f"  .centroid is defined for all   : "
          f"{[f'({c.x:.1f}, {c.y:.1f})' for c in mixed.centroid]}")
    print(f"  .area on the mixed layer       : {list(np.round(mixed.area, 3))} "
          "(a point's area is 0, a line's area is 0)")
    print("  area of a layer that mixes points, lines and polygons is therefore")
    print("  numerically defined and semantically meaningless -- a trap that raises no")
    print("  error.  Filter by geometry type before any measurement.")
    with_na = sites.copy()
    with_na.loc[with_na.index[:5], "rock"] = None
    print(f"\n  5 rows of 'rock' set to None:")
    vc = with_na["rock"].value_counts(dropna=False)
    print(f"    value_counts(dropna=False) : "
          f"{{{', '.join(f'{k!r}: {int(v)}' for k, v in vc.items())}}}")
    print(f"    groupby mean excludes the NaN rows: "
          f"{len(with_na.groupby('rock', dropna=True).size())} groups, "
          f"{with_na.groupby('rock', dropna=True).size().sum()} of {len(with_na)} rows")
    print("Silent row loss on group-by is the counterpart of silent row gain on join.")
    print("Both are invisible in a figure and both change the reported number.")


if __name__ == "__main__":
    main()
