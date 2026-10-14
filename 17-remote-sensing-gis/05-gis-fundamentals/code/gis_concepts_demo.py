#!/usr/bin/env python3
"""GIS concepts: layers, attributes and topology measured on synthetic objects.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gis_concepts_demo.py

All geometries, attributes and coordinates in this demonstration are SYNTHETIC
teaching objects built in memory.  Nothing is read from disk and nothing is
written to disk.  No real place, dataset or coordinate is used.

Contents
--------
1. A layer is a table plus a geometry column: schema, CRS, dtypes.
2. A planar partition: area additivity as a topological invariant.
3. Adjacency by exact shared boundary, and the cost of a snapping tolerance.
4. A sliver gap: how a digitising tolerance becomes an area error.
5. Simple-feature predicates on synthetic points (within / touches / crosses).
6. Coordinate reference systems: the same shape measured in degrees and metres.
7. Ring orientation and the Euler characteristic of a polygon set.
"""

import numpy as np
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon, LineString
from shapely.ops import unary_union
from shapely import is_valid
from pyproj import Geod

RNG = np.random.default_rng(20261014)

GEOD = Geod(ellps="WGS84")
# A synthetic 100 km x 60 km study area expressed on a local projected grid.
# The local grid uses metres only -- it is NOT a real CRS and is not registered
# in any EPSG database.  It is a teaching frame with 1 m units.
X0, Y0, X1, Y1 = 0.0, 0.0, 100_000.0, 60_000.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def make_partition(n_blocks=4):
    """Slice the study area into n_blocks vertical strips; a planar partition.

    A planar partition (also called a coverage) is a set of polygons whose
    interiors are disjoint and whose union is the study area.  The vertical cuts
    are chosen to be *exactly* representable in binary floating point (multiples
    of 1/4 km) so that shared boundaries are bit-for-bit identical and the area
    test is exact rather than approximate.
    """
    cuts = np.linspace(X0, X1, n_blocks + 1)
    polys = []
    for i in range(n_blocks):
        polys.append(
            Polygon(
                [
                    (cuts[i], Y0),
                    (cuts[i + 1], Y0),
                    (cuts[i + 1], Y1),
                    (cuts[i], Y1),
                ]
            )
        )
    return polys


def main():
    section("1. A layer is a table plus a geometry column")
    polys = make_partition(4)
    names = ["alpha", "beta", "gamma", "delta"]
    gdf = gpd.GeoDataFrame(
        {
            "block": names,
            "land_cover": ["bare", "vegetated", "water", "bare"],
            "ndvi_mean": [0.18, 0.71, -0.05, 0.22],
            "n_samples": RNG.integers(40, 200, size=4),
        },
        geometry=polys,
        crs="EPSG:32633",  # a real projected CRS, used only as a label here
    )
    print("attribute table (this is the whole 'attribute' half of a GIS layer):")
    print(gdf.drop(columns="geometry").to_string(index=False))
    print("\ncolumn dtypes:")
    for col, dt in gdf.dtypes.items():
        print(f"  {col:12s} {str(dt)}")
    print(f"\ngeometry column: 1 column, {len(gdf)} rows, type "
          f"{gdf.geometry.geom_type.unique().tolist()}")
    print(f"declared CRS: {gdf.crs.to_string()} "
          f"(units = {gdf.crs.axis_info[0].unit_name})")
    print("a GIS layer is therefore (n rows) x (n attribute columns + 1 geometry);")
    print("the geometry is a *value* in a column, not a separate object type.")

    section("2. Area additivity: the topological invariant of a partition")
    areas = gdf.geometry.area.to_numpy()
    total = areas.sum()
    union_area = unary_union(gdf.geometry.values).area
    print("per-block area (coordinates are metres; printed in km^2, 1 km^2 = 1e6 m^2):")
    for nm, a in zip(names, areas / 1e6):
        print(f"  {nm:6s} {a:10.3f} km^2")
    print(f"sum of parts           = {total / 1e6:10.3f} km^2")
    print(f"area of the union      = {union_area / 1e6:10.3f} km^2")
    print(f"additivity residual    = {(total - union_area) / 1e6:10.3e} km^2 "
          f"({(total - union_area) / total * 100:.2e} % of the total)")
    print("exact agreement (residual at the 1e-10 level) is the signature of a valid")
    print("planar partition: no overlaps, no gaps.  Overlap would make the sum larger")
    print("than the union; a gap would make it smaller.")

    section("3. Adjacency, gaps and overlaps under a snapping tolerance")
    shared = 0
    for i in range(len(gdf)):
        for j in range(i + 1, len(gdf)):
            if gdf.geometry[i].touches(gdf.geometry[j]):
                shared += 1
    print(f"pairs of blocks that touch: {shared} (a 4-strip partition has 3 internal cuts)")
    n_overlap = sum(
        gdf.geometry[i].overlaps(gdf.geometry[j])
        for i in range(4) for j in range(i + 1, 4)
    )
    print(f"pairs whose interiors overlap: {n_overlap}")
    print(f"all shared cuts are bit-for-bit identical: a valid planar partition.")

    # Redraw the second strip with a digitising error of 1 m on each cut.
    tol = 1.0  # metres
    print(f"\nredraw block 'beta' (nominal x from 25.0 to 50.0 km) mis-closed by {tol:.1f} m:")
    for label, x_a, x_b in (
        ("shrunk (gap of 1 m each side)", 25_000.0 + tol, 50_000.0 - tol),
        ("grown  (overlap 1 m each side)", 25_000.0 - tol, 50_000.0 + tol),
    ):
        strip = Polygon([(x_a, Y0), (x_b, Y0), (x_b, Y1), (x_a, Y1)])
        nb_l, nb_r = gdf.geometry[0], gdf.geometry[2]
        print(f"  {label}:")
        print(f"    touches the neighbours (exact predicate) : "
              f"{strip.touches(nb_l)} / {strip.touches(nb_r)}")
        print(f"    boundary-to-boundary distance            : "
              f"{strip.boundary.distance(nb_l.boundary):.3f} m, "
              f"{strip.boundary.distance(nb_r.boundary):.3f} m")
        misc = abs(strip.area - 25_000.0 * Y1)
        print(f"    area error vs the nominal strip          : "
              f"{misc / 1e6:.6f} km^2 ({misc / (25_000.0 * Y1) * 100:.6f} %)")
    print("Both errors have the same magnitude (1 m x 60 km = 0.06 km^2 per cut, two")
    print("cuts = 0.12 km^2) but opposite sign, and the *predicate* answers differently:")
    print("the shrunk strip is a gap (distance 1 m, not touching), while the grown strip")
    print("has distance 0 m and still is not 'touches', because touching requires the")
    print("interiors to stay disjoint.  A distance of zero is therefore not adjacency.")
    print("So 'adjacent' is a *tolerance-dependent* statement.  Every GIS either snaps")
    print("vertices to a grid (and silently moves them) or keeps an untidy coverage and")
    print("reports slivers and double-counted overlaps; there is no third option.  A snap")
    print("tolerance is a digitising choice and must be quoted with the result.")

    section("4. A sliver/overlap field: from digitising tolerance to area error")
    print("synthetic coverage of 20 strips of the 100 km x 60 km area, each strip")
    print("digitised with an independent Gaussian vertex error of sigma = 3 m:")
    sigma = 3.0
    strip_w = (X1 - X0) / 20.0
    polys_bad = []
    for i in range(20):
        dx0 = RNG.normal(0.0, sigma)
        dx1 = RNG.normal(0.0, sigma)
        polys_bad.append(
            Polygon(
                [
                    (i * strip_w + dx0, Y0),
                    ((i + 1) * strip_w + dx1, Y0),
                    ((i + 1) * strip_w + dx1, Y1),
                    (i * strip_w + dx0, Y1),
                ]
            )
        )
    area_nominal = (X1 - X0) * (Y1 - Y0)
    area_sum = sum(p.area for p in polys_bad)
    area_union = unary_union(polys_bad).area
    print(f"  nominal study area        = {area_nominal / 1e6:12.3f} km^2")
    print(f"  sum of 20 strip areas     = {area_sum / 1e6:12.3f} km^2 "
          f"({(area_sum - area_nominal) / 1e6:+.3f} km^2, "
          f"{(area_sum - area_nominal) / area_nominal * 100:+.4f} %)")
    print(f"  union of the 20 strips    = {area_union / 1e6:12.3f} km^2 "
          f"({(area_union - area_nominal) / 1e6:+.3f} km^2, "
          f"{(area_union - area_nominal) / area_nominal * 100:+.4f} %)")
    print(f"  overlap (sum - union)     = {(area_sum - area_union) / 1e6:12.3f} km^2")
    print(f"  sliver/edge gap (nominal - union) = "
          f"{(area_nominal - area_union) / 1e6:12.3f} km^2")
    print("the sum exceeds the nominal area because perturbed neighbours OVERLAP, while")
    print("the union falls short because the same perturbation leaves GAPS elsewhere.")
    print("The two errors do not cancel.  A zonal total computed as a sum over strips")
    print(f"is biased high by {(area_sum - area_union) / area_union * 100:+.4f} % of the")
    print("union area, and the coverage as drawn does not tile the study area at all.")

    section("5. Simple-feature predicates: within / touches / crosses")
    pts = gpd.GeoDataFrame(
        {"site": [f"S{i:02d}" for i in range(6)]},
        geometry=[
            Point(10_000.0, 30_000.0),   # inside alpha
            Point(30_001.0, 30_000.0),   # inside beta
            Point(50_000.0, 30_000.0),   # exactly on the beta/gamma boundary
            Point(0.0, 30_000.0),        # exactly on the west outer boundary
            Point(110_000.0, 30_000.0),  # outside the study area
            Point(75_000.0, 45_000.0),   # inside delta
        ],
        crs="EPSG:32633",
    )
    joined = gpd.sjoin(pts, gdf[["block", "geometry"]], how="left",
                       predicate="within")
    boundary_pts = pts.geometry.apply(
        lambda p: any(pol.boundary.intersects(p) for pol in gdf.geometry)
    )
    print("  site   x (km)   y (km)   within block   on a polygon boundary")
    for (_, p), onb in zip(pts.iterrows(), boundary_pts):
        blk = joined.loc[joined.index == _, "block"]
        blk = blk.iloc[0] if len(blk) and pd.notna(blk.iloc[0]) else "-"
        print(f"  {p['site']}   {p.geometry.x/1e3:6.1f}   {p.geometry.y/1e3:6.1f}"
              f"   {blk:^12s}   {str(bool(onb)):>5s}")
    print("Note S02 (shared cut), S03 (outer boundary) and S05 (a second internal cut)")
    print("are NOT 'within' any block: 'within' requires the point's interior to lie in")
    print("the polygon's interior, and a point on a boundary has empty interior.  This is")
    print("a specification, not a bug, and it is why every join must name its predicate:")
    print("'within' and 'intersects' disagree on precisely the boundary set.")

    section("6. CRS: the same shape measured in degrees and metres")
    # Synthetic WGS84 polygon: a 0.10 deg x 0.10 deg box near the equator.
    box_wgs = Polygon([(0.0, 0.0), (0.10, 0.0), (0.10, 0.10), (0.0, 0.10)])
    g_wgs = gpd.GeoDataFrame({"name": ["box"]}, geometry=[box_wgs],
                             crs="EPSG:4326")
    g_m = g_wgs.to_crs("EPSG:32631")  # UTM 31N, a real projected CRS
    naive = box_wgs.area
    lons, lats = np.array([0.0, 0.10, 0.10, 0.0]), np.array([0.0, 0.0, 0.10, 0.10])
    geod_area, _ = GEOD.polygon_area_perimeter(lons, lats)
    print(f"  planar area in degrees^2            : {naive:.8f} deg^2")
    print(f"  area after projection to UTM 31N     : {g_m.geometry.area.iloc[0]/1e6:.4f} km^2")
    print(f"  geodesic area on the WGS84 ellipsoid : {abs(geod_area)/1e6:.4f} km^2")
    print(f"  difference (projection distortion)   : "
          f"{(g_m.geometry.area.iloc[0] - abs(geod_area))/1e6:+.4f} km^2 "
          f"({(g_m.geometry.area.iloc[0] - abs(geod_area))/abs(geod_area)*100:+.4f} %)")
    print(f"  1 deg of longitude at the equator    : {GEOD.inv(0, 0, 1, 0)[2]/1e3:.3f} km")
    print(f"  1 deg of longitude at 60 deg N       : {GEOD.inv(0, 60, 1, 60)[2]/1e3:.3f} km")
    print("A degree is not a length, so an area in deg^2 is not an area.  Any area or")
    print("distance computed in EPSG:4326 is meaningless as a physical quantity; the")
    print("geodesic area and the projected area differ because a projection is a choice.")

    section("7. Ring orientation and the Euler characteristic")
    ring = np.array([(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)])
    signed = np.sum(ring[:, 0] * np.roll(ring[:, 1], -1))
    signed -= np.sum(ring[:, 1] * np.roll(ring[:, 0], -1))
    signed *= 0.5
    print(f"  signed area of a counter-clockwise ring = {signed:+.1f} km^2")
    print(f"  printed shapely WKT starts with        : {Polygon(ring).wkt[:42]}...")
    rev = Polygon(ring[::-1])
    print(f"  reversed ring signed area              = {-signed:+.1f} km^2 "
          f"(equals(...) = {Polygon(ring).equals(rev)})")
    print("Shapely normalises orientation on construction, so equals() is True even")
    print("though the vertex order is reversed: equality of geometry is not equality of")
    print("representation.  A file format (or a QGIS layer) may preserve the raw order,")
    print("which is why two 'identical' layers can hash differently.")

    # Planar graph of the 4-strip partition: 2 rows x 5 columns of vertices.
    V = 10
    E_boundary = 10   # 4 bottom + 4 top + 2 side segments of the outer rectangle
    E_internal = 3    # the three internal cuts
    E = E_boundary + E_internal
    F_bounded = 4
    F_total = F_bounded + 1  # +1 for the outer (unbounded) face
    print(f"\n  planar graph of the 4-strip partition:")
    print(f"    vertices V                    = {V} (2 rows x 5 columns)")
    print(f"    edges E                       = {E} ({E_boundary} boundary + "
          f"{E_internal} internal)")
    print(f"    bounded faces (blocks)        = {F_bounded}")
    print(f"    V - E + F_bounded             = {V - E + F_bounded} "
          "(a planar graph drawn on a disk, outer face excluded)")
    print(f"    V - E + F_total (outer face +1)= {V - E + F_total} "
          "(the Euler formula for a connected planar graph)")
    print(f"    incidence identity 2E = 4F + E_boundary: {2 * E} = "
          f"{4 * F_bounded} + {E_boundary} = {4 * F_bounded + E_boundary}")
    print("These counts are how a topologist checks a coverage: an unexpected extra")
    print("bounded face means a sliver has closed into its own polygon, and F_bounded")
    print("rising above the number of map units is the classic signature of that error.")


if __name__ == "__main__":
    main()
