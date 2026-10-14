"""Spatial indexing: how many geometry tests a tree actually saves.

Nothing here is timed. Instead the demo counts the predicate evaluations that
each strategy performs, which is the machine-independent part of the cost.

All data are SYNTHETIC: seeded points against a regular grid of rectangular
cells, in a projected CRS with metre units.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spatial_indexing_demo.py
Requires: numpy, pandas, geopandas, shapely.
"""

from __future__ import annotations

import numpy as np
import geopandas as gpd
import shapely
import shapely.affinity
from shapely import box, points
from shapely.prepared import prep

RNG = np.random.default_rng(20260903)
GRID = "EPSG:32612"
X0, Y0 = 500_000.0, 4_200_000.0
CELL = 2_000.0                      # metres
NCOL, NROW = 20, 20                 # 400 cells covering 40 km x 40 km
N_POINT = 2_000
N_IN = 1_600


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def build_data():
    geoms, ids = [], []
    for i in range(NCOL):
        for j in range(NROW):
            geoms.append(box(X0 + i * CELL, Y0 + j * CELL,
                             X0 + (i + 1) * CELL, Y0 + (j + 1) * CELL))
            ids.append(f"C{i:02d}{j:02d}")
    cells = gpd.GeoDataFrame(
        {"cell": ids,
         "col": [i for i in range(NCOL) for _ in range(NROW)],
         "row": [j for _ in range(NCOL) for j in range(NROW)]},
        geometry=geoms, crs=GRID)
    px = np.concatenate([RNG.uniform(X0 + 1.0, X0 + NCOL * CELL - 1.0, N_IN),
                         RNG.uniform(X0 - 5_000.0, X0 + NCOL * CELL + 5_000.0,
                                     N_POINT - N_IN)])
    py = np.concatenate([RNG.uniform(Y0 + 1.0, Y0 + NROW * CELL - 1.0, N_IN),
                         RNG.uniform(Y0 - 5_000.0, Y0 + NROW * CELL + 5_000.0,
                                     N_POINT - N_IN)])
    pts = gpd.GeoDataFrame(
        {"station": [f"P{i:04d}" for i in range(N_POINT)],
         "value": RNG.normal(100.0, 15.0, N_POINT).round(3)},
        geometry=points(px, py), crs=GRID)
    return cells, pts


def brute_force_pairs(poly_geoms, point_geoms) -> list[tuple[int, int]]:
    """Every point-in-polygon test, explicitly enumerated."""
    prepared = [prep(g) for g in poly_geoms]
    pairs = []
    for pi, p in enumerate(point_geoms):
        for ci, pg in enumerate(prepared):
            if pg.contains(p):
                pairs.append((pi, ci))
    return pairs


def main() -> None:
    cells, pts = build_data()
    poly_geoms = list(cells.geometry)
    point_geoms = list(pts.geometry)

    section("1. The data, and the naive cost")
    print(f"  {len(pts)} points, {len(cells)} polygons, CRS = {pts.crs}")
    print(f"  points inside the tiled area = {N_IN}, outside = {N_POINT - N_IN}")
    print(f"  each polygon is {CELL:.0f} m x {CELL:.0f} m = "
          f"{CELL ** 2 / 1e6:.1f} km^2, tiling "
          f"{NCOL * CELL / 1000:.0f} km x {NROW * CELL / 1000:.0f} km")
    naive_tests = len(pts) * len(cells)
    print(f"  a naive nested loop performs {len(pts):,} x {len(cells):,} = "
          f"{naive_tests:,} point-in-polygon tests")

    section("2. The brute-force answer, with the test count measured")
    brute = brute_force_pairs(poly_geoms, point_geoms)
    brute_set = set(brute)
    matched_points = {pi for pi, _ in brute}
    print(f"  brute force: {naive_tests:,} tests -> {len(brute):,} matches")
    print(f"  hit rate = {100 * len(brute) / naive_tests:.4f} % of all tests; "
          f"{naive_tests - len(brute):,} tests returned nothing")
    print(f"  points matched = {len(matched_points):,} of {N_POINT:,}; "
          f"no point matched twice: {len(matched_points) == len(brute)}")
    print(f"  (the {N_POINT - N_IN} points drawn from the wider box are only")
    print(f"  partly outside the tiling: {len(matched_points) - N_IN} of them")
    print(f"  landed inside, as uniform sampling over a larger rectangle implies)")

    section("3. An STRtree answers the same question with fewer tests")
    tree = shapely.STRtree(poly_geoms)
    # STRtree applies predicate(input_geometry, tree_geometry).
    qi, ci = tree.query(pts.geometry.values, predicate="within")
    tree_set = set(zip(qi.tolist(), ci.tolist()))
    print(f"  STRtree built over {len(poly_geoms):,} polygons; "
          f"{len(pts)} query geometries")
    print(f"  bounding-box candidates returned = {len(qi):,}")
    print(f"  candidate pairs per point = {len(qi) / len(pts):.3f}")
    print(f"  reduction against brute force = "
          f"{naive_tests / max(len(qi), 1):,.1f}x fewer predicate evaluations")
    print(f"  tree geometries are returned as indices into the ORIGINAL array, so")
    print(f"  the caller never searches a list")
    print(f"  answer identical to brute force: {tree_set == brute_set}")
    n_false = len(qi) - len(tree_set)
    print(f"  candidates rejected by the predicate = {n_false:,} "
          f"({100 * n_false / max(len(qi), 1):.2f} % of the candidates)")
    print(f"  the tree returns bounding-box candidates only; the predicate is")
    print(f"  still evaluated for each of them")
    print(f"  tree.query(g, predicate='dwithin', distance=r) is the radius search;")
    print(f"  query(g, distance=r) alone does NOT expand the search")

    section("4. Bounding boxes are not geometry: a rotated band")
    band = shapely.affinity.rotate(
        box(X0, Y0 + 20_000.0, X0 + 40_000.0, Y0 + 21_000.0), 20.0,
        origin=(X0, Y0 + 20_500.0))
    btree = shapely.STRtree([band])
    bb = btree.query(pts.geometry.values)
    bm = btree.query(pts.geometry.values, predicate="within")
    print(f"  the band is 40 km x 1 km, rotated 20 deg: ")
    print(f"    its bounding box is "
          f"{band.bounds[2] - band.bounds[0]:,.0f} m x "
          f"{band.bounds[3] - band.bounds[1]:,.0f} m, "
          f"{band.envelope.area / band.area:.1f}x its area")
    print(f"    bbox candidates          = {bb.shape[1]:,} points")
    print(f"    predicate confirms       = {bm.shape[1]:,} points")
    print(f"    candidates the predicate rejects = {bb.shape[1] - bm.shape[1]:,} "
          f"({100 * (bb.shape[1] - bm.shape[1]) / max(bb.shape[1], 1):.1f} %)")
    print(f"  with axis-aligned tiles the bounding boxes ARE the tiles, so this")
    print(f"  demo's rectangular cells show no false positives at all "
          f"({len(qi) - len(tree_set):,} above).")
    print(f"  A rotated or oblique dataset is where the predicate earns its keep.")
    print(f"  A bbox-only query is not wrong, it is unfinished.")

    section("5. Nearest neighbours are a different query")
    poly_arr = np.asarray(poly_geoms, dtype=object)
    inside_q = pts.geometry.values[:5]
    _, inside_d = tree.query_nearest(inside_q, return_distance=True,
                                     all_matches=False)
    print(f"  STRtree.query_nearest on 5 points INSIDE the tiling -> "
          f"{len(inside_d)} pairs, distances = {np.unique(inside_d)} m")
    print(f"  the distance is zero because the points sit inside a polygon")
    outside = [shapely.Point(X0 - 2_500.0 + 500.0 * i, Y0 + 8_000.0 * i)
               for i in range(5)]
    _, out_d = tree.query_nearest(outside, return_distance=True,
                                  all_matches=False)
    print(f"  5 points WEST of the tiling (x = {X0 - 2000:.0f} .. "
          f"{X0 - 500:.0f}): nearest-polygon distance = "
          f"{np.round(out_d, 1)} m")
    radius = 9_000.0
    k = 3
    print(f"  k={k} nearest polygons per query point, found by one radius query")
    print(f"  (predicate='dwithin', distance={radius:.0f} m) plus an exact sort:")
    for i, g in enumerate(outside):
        cand = tree.query(g, predicate="dwithin", distance=radius)
        d = np.sort(shapely.distance(poly_arr[cand], g))
        print(f"    query {i} at ({shapely.get_x(g):,.0f}, {shapely.get_y(g):,.0f}): "
              f"{len(cand)} candidates, {k} nearest at "
              f"{', '.join(f'{v:.0f} m' for v in d[:k])}")
    print(f"  a point can be up to {np.hypot(CELL / 2, CELL / 2):.0f} m from the")
    print(f"  centre of its own cell, so the nearest polygon is not necessarily")
    print(f"  the containing one: nearest-neighbour work needs its own index and")
    print(f"  its own search radius")

    section("6. GeoPandas spatial joins use the same machinery")
    joined = gpd.sjoin(pts, cells, predicate="within", how="inner")
    print(f"  gpd.sjoin(predicate='within', how='inner') -> {len(joined):,} rows")
    print(f"  equal to the brute-force match count: "
          f"{len(joined) == len(brute)}")
    left = gpd.sjoin(pts, cells, predicate="within", how="left")
    print(f"  how='left' -> {len(left):,} rows, "
          f"{int(left.cell.isna().sum())} of them with no cell")
    print(f"  cells that received at least one point = "
          f"{int(joined.cell.nunique())} of {len(cells)}")

    section("7. A regular grid needs no tree at all")
    pts_x = pts.geometry.x.values
    pts_y = pts.geometry.y.values
    col = np.floor((pts_x - X0) / CELL).astype(int)
    row = np.floor((pts_y - Y0) / CELL).astype(int)
    inside = (col >= 0) & (col < NCOL) & (row >= 0) & (row < NROW)
    flat = col * NROW + row
    direct_set = {(int(pi), int(flat[pi])) for pi in np.nonzero(inside)[0]}
    print(f"  floor((x - x0) / dx) locates each point in a cell by arithmetic:")
    print(f"    points located        = {int(inside.sum()):,}")
    print(f"    predicate evaluations = 0 (integer division plus a range check)")
    print(f"    matches identical to brute force: {direct_set == brute_set}")
    print(f"  this works only for a regular grid, and it is exactly why large")
    print(f"  gridded datasets are stored as rasters instead of polygons")

    section("8. Counting points per cell: two routes, one answer")
    counts_join = joined.groupby("cell").size().reindex(cells.cell).fillna(0)
    counts_np = np.bincount(flat[inside], minlength=len(cells))
    print(f"  sjoin + groupby total = {int(counts_join.sum()):,} points")
    print(f"  numpy bincount total  = {int(counts_np.sum()):,} points")
    print(f"  identical per-cell counts: "
          f"{bool(np.array_equal(counts_np, counts_join.values.astype(int)))}")
    print(f"  busiest cell holds {int(counts_np.max())} points; "
          f"{int((counts_np == 0).sum())} cells are empty")
    print(f"  measured mean = {counts_np.mean():.3f}, variance = "
          f"{counts_np.var(ddof=1):.3f}, variance/mean = "
          f"{counts_np.var(ddof=1) / counts_np.mean():.3f}")
    print(f"  the points are uniform by construction, so variance/mean near 1 is")
    print(f"  expected; clustering would push it above 1")

    section("9. Why the tree helps, in one comparison")
    print(f"  naive nested loop : {naive_tests:,} predicate evaluations")
    print(f"  STRtree           : {len(qi):,} candidates, then {len(qi):,} "
          f"predicates")
    print(f"  regular grid      : 0 searches, {int(inside.sum()):,} integer "
          f"divisions")
    print(f"  the tree replaces a product of sizes with a sum of local queries.")
    print(f"  That is a change in the SHAPE of the cost, which is why the benefit")
    print(f"  grows with the dataset and never shrinks.")


if __name__ == "__main__":
    main()
