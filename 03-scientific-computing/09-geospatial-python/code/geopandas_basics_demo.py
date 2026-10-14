"""GeoDataFrames: CRS handling, the area/distance trap, and spatial joins.

All data are SYNTHETIC (seeded points and rectangular regions built in code).
No shapefile is downloaded and no real boundary is used.

The demo's central measurement is the cost of computing areas and distances in a
geographic CRS, and the difference between a projected area and the true
geodesic area.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geopandas_basics_demo.py
Requires: numpy, pandas, geopandas, shapely, pyproj.
"""

from __future__ import annotations

import numpy as np
import geopandas as gpd
import pandas as pd
import shapely
from pyproj import Geod, Transformer
from shapely import box, points

RNG = np.random.default_rng(20260902)
GEOD = Geod(ellps="WGS84")
WGS84 = "EPSG:4326"


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main() -> None:
    # 600 synthetic stations inside a 4 deg x 3 deg box in the western USA,
    # plus 6 rectangular "regions" tiling the same box.
    lon = RNG.uniform(-112.2, -107.8, 600)      # wider than the region tiling
    lat = RNG.uniform(36.8, 40.2, 600)
    stations = gpd.GeoDataFrame(
        {"station": [f"SYN{i:03d}" for i in range(600)],
         "elev_m": RNG.normal(1500.0, 400.0, 600).round(1),
         "v_p_kms": RNG.normal(6.0, 0.15, 600).round(3)},
        geometry=points(lon, lat), crs=WGS84)

    cells = []
    ids = []
    for i in range(3):                    # 3 columns of 2 rows, 4/3 x 1.5 deg
        for j in range(2):
            cells.append(box(-112.0 + i * (4.0 / 3), 37.0 + j * 1.5,
                             -112.0 + (i + 1) * (4.0 / 3), 37.0 + (j + 1) * 1.5))
            ids.append(f"R{i}{j}")
    regions = gpd.GeoDataFrame({"region": ids, "rock": list("ABCDEF")},
                               geometry=cells, crs=WGS84)

    section("1. A GeoDataFrame is a DataFrame with one geometry column and a CRS")
    print(f"  rows = {len(stations)}, columns = {list(stations.columns)}")
    print(f"  geometry column = {stations.geometry.name}, "
          f"dtype = {stations.geometry.dtype}")
    print(f"  crs = {stations.crs}, epsg = {stations.crs.to_epsg()}")
    print(f"  a plain DataFrame view still works for attributes:")
    print(f"    mean elevation = {stations.elev_m.mean():.1f} m, "
          f"mean v_p = {stations.v_p_kms.mean():.3f} km/s")
    print(f"  bounds = {tuple(round(v, 3) for v in stations.total_bounds)} "
          f"(minx, miny, maxx, maxy)")
    print(f"  lon/lat order: the x column is longitude even though EPSG:4326 is")
    print(f"  defined as lat,lon in the EPSG registry; GeoPandas and PROJ use the")
    print(f"  GIS convention x = lon, y = lat by default")

    section("2. Planar area in degrees: the wrong answer, quantified")
    deg_area = float(regions.geometry.area.sum())
    print(f"  sum of region areas as stored = {deg_area:.6f} square degrees")
    meters = regions.to_crs("EPSG:32612")          # UTM 12N, metres
    utm_area = float(meters.geometry.area.sum())
    utm_area_across_zones = float(
        regions.to_crs("EPSG:26912").geometry.area.sum())
    print(f"  after .to_crs('EPSG:32612') = {utm_area / 1e6:.4f} km^2")
    print(f"  after .to_crs('EPSG:26912') = {utm_area_across_zones / 1e6:.4f} km^2 "
          f"(UTM zone 12N on the NAD83 datum)")
    print(f"    difference from WGS 84 UTM = "
          f"{abs(utm_area - utm_area_across_zones) / 1e3:.3f} m^2 over "
          f"{utm_area / 1e6:.0f} km^2: NAD83 and WGS 84 differ by about a metre")
    print(f"    here, so the datum changes the answer by 1 part in 10^11 -- real,")
    print(f"    and irrelevant until you need millimetre precision")
    zone11 = float(regions.to_crs("EPSG:32611").geometry.area.sum())
    geo_total = sum(abs(GEOD.geometry_area_perimeter(g)[0])
                    for g in regions.geometry)
    print(f"  true geodesic area (pyproj Geod)  = {geo_total / 1e6:.4f} km^2")
    print(f"  error of the UTM area    = "
          f"{100 * (utm_area - geo_total) / geo_total:+.4f} %")
    print(f"  after .to_crs('EPSG:32611') = {zone11 / 1e6:.4f} km^2 "
          f"({100 * (zone11 - geo_total) / geo_total:+.4f} % true error)")
    print(f"    zone 11 has central meridian 117 W while the data sit at 110 W, so")
    print(f"    the SAME DATA IN THE WRONG UTM ZONE is out by "
          f"{100 * (zone11 - geo_total) / geo_total:+.3f} %,")
    print(f"    twenty times the error of the correct zone.")
    print(f"  error of the degree area = not even comparable: square degrees are")
    print(f"  not an area unit. The 12 deg^2 nominal box is "
          f"{deg_area:.1f} 'square degrees', and one square degree here is worth "
          f"{geo_total / 1e6 / deg_area:.1f} km^2")
    lat_span = stations.total_bounds[3] - stations.total_bounds[1]
    lon_span = stations.total_bounds[2] - stations.total_bounds[0]
    print(f"  the box is {lon_span:.1f} deg of longitude and {lat_span:.1f} deg of")
    print(f"  latitude, but {meters.total_bounds[2] - meters.total_bounds[0]:.0f} m")
    print(f"  wide and {meters.total_bounds[3] - meters.total_bounds[1]:.0f} m tall:")
    print(f"  the degree ratio is {lon_span / lat_span:.3f} and the metre ratio is "
          f"{(meters.total_bounds[2] - meters.total_bounds[0]) / (meters.total_bounds[3] - meters.total_bounds[1]):.3f}")

    section("3. Distances: three answers for the same pair of stations")
    a = stations.geometry.iloc[0]
    b = stations.geometry.iloc[1]
    deg = a.distance(b)
    utm_dist = stations.to_crs("EPSG:32612").geometry.iloc[0].distance(
        stations.to_crs("EPSG:32612").geometry.iloc[1])
    _, _, geo_dist = GEOD.inv(a.x, a.y, b.x, b.y)
    lat_mid = 0.5 * (a.y + b.y)
    approx = np.hypot((a.x - b.x) * 111_320 * np.cos(np.deg2rad(lat_mid)),
                      (a.y - b.y) * 110_570)
    print(f"  stations {stations.station.iloc[0]} and {stations.station.iloc[1]}:")
    print(f"    planar distance in degrees = {deg:.6f} deg")
    print(f"    projected distance in UTM   = {utm_dist / 1000:.4f} km "
          f"({100 * (utm_dist - geo_dist) / geo_dist:+.4f} % from geodesic)")
    print(f"    geodesic distance (pyproj)  = {geo_dist / 1000:.4f} km")
    print(f"    cos(lat) approximation      = {approx / 1000:.4f} km "
          f"({100 * (approx - geo_dist) / geo_dist:+.4f} %)")
    print(f"  a tolerance written as 'distance < 0.05' in degrees means "
          f"{0.05 * 111.32 * np.cos(np.deg2rad(lat_mid)):.3f} km east-west at")
    print(f"  this latitude and {0.05 * 110.57:.3f} km north-south: the threshold")
    print(f"  is not a distance, it is an ellipse in disguise")
    all_dist = stations.to_crs("EPSG:32612").geometry.distance(
        stations.to_crs("EPSG:32612").geometry.iloc[0]) / 1000.0
    print(f"  distances of all {len(all_dist)} stations from "
          f"{stations.station.iloc[0]}: min = {all_dist.min():.3f} km, "
          f"max = {all_dist.max():.3f} km")

    section("4. Spatial join: a point-in-polygon assignment")
    joined = gpd.sjoin(stations, regions, predicate="within", how="left")
    print(f"  sjoin(predicate='within', how='left'): {len(joined)} rows from "
          f"{len(stations)} stations")
    unmatched = int(joined.region.isna().sum())
    print(f"  stations with no region = {unmatched} "
          f"({100 * unmatched / len(stations):.2f} %)")
    counts = joined.groupby("region").size()
    print(f"  stations per region: {dict(counts)}")
    print(f"  the cells are equal in degrees but not in area: expected counts")
    exp = np.array([regions.to_crs("EPSG:32612").geometry.area.iloc[i]
                    for i in range(len(regions))])
    exp = exp / exp.sum() * (len(stations) - unmatched)
    print(f"    area-proportional expectation = "
          f"{[int(round(v)) for v in exp]}")
    print(f"    measured                     = "
          f"{[int(counts.get(f'R{i}{j}', 0)) for i in range(3) for j in range(2)]}")
    inner = gpd.sjoin(stations, regions, predicate="within", how="inner")
    print(f"  how='inner' silently drops the {unmatched} unmatched stations: "
          f"{len(inner)} rows")
    for predicate in ("intersects", "contains", "within", "touches"):
        try:
            n = len(gpd.sjoin(stations, regions, predicate=predicate))
            print(f"  predicate='{predicate:10s}' -> {n} rows")
        except Exception as exc:                      # noqa: BLE001
            print(f"  predicate='{predicate:10s}' -> {type(exc).__name__}")
    print(f"  'intersects' == 'within' here; the boundary case is the exception.")
    bnd_lon = -112.0 + 4.0 / 3          # the shared edge of R00/R01 and R10/R11
    on_edge = gpd.GeoDataFrame({"station": ["BND0", "BND1"]},
                               geometry=points([bnd_lon, bnd_lon], [38.0, 39.0]),
                               crs=WGS84)
    print(f"  two stations placed exactly on the shared edge lon = {bnd_lon:.6f}:")
    for predicate in ("within", "intersects", "covers", "touches"):
        hit = gpd.sjoin(on_edge, regions, predicate=predicate, how="left")
        matched = int(hit.region.notna().sum())
        print(f"    predicate='{predicate:10s}' -> {matched} matched point(s), "
              f"{len(hit)} output rows")
    print(f"  'within' drops them, 'intersects' assigns each to both cells and")
    print(f"  creates a duplicate station. Decide which you want, and assert the")
    print(f"  row count afterwards.")

    section("5. Aggregating inside each region")
    agg = joined.groupby("region").agg(n=("station", "size"),
                                       v_p=("v_p_kms", "mean"),
                                       elev=("elev_m", "mean"))
    areas = regions.to_crs("EPSG:32612").geometry.area / 1e6
    agg["area_km2"] = areas.values
    agg["density_per_1000km2"] = agg.n / agg.area_km2 * 1000
    print(agg.round(4).to_string())
    naive = joined.v_p_kms.mean()
    weighted = (agg.v_p * agg.area_km2).sum() / agg.area_km2.sum()
    print(f"  mean v_p over stations = {naive:.4f} km/s")
    print(f"  area-weighted by region = {weighted:.4f} km/s "
          f"(difference {abs(naive - weighted) * 1000:.2f} m/s)")
    print(f"  the difference is {abs(naive - weighted) * 1000:.2f} m/s here because the")
    print(f"  regions differ in area by only "
          f"{100 * (agg.area_km2.max() / agg.area_km2.min() - 1):.2f} % and the mean")
    print(f"  v_p barely varies between them. Weighting is not decoration: it is")
    print(f"  what stops a coastline-heavy grid from deciding a global average.")

    section("6. Doing geometry with the wrong CRS: the buffer-in-degrees error")
    poc = stations.iloc[[0]].copy()
    buf_deg = poc.copy()
    buf_deg["geometry"] = poc.geometry.buffer(0.1)
    deg_km2 = float(buf_deg.to_crs("EPSG:32612").geometry.area.sum()) / 1e6
    buf_m = poc.to_crs("EPSG:32612")
    buf_m["geometry"] = buf_m.geometry.buffer(11_000.0)
    m_km2 = float(buf_m.geometry.area.sum()) / 1e6
    print(f"  buffer(0.1) in degrees then measured in UTM = {deg_km2:.3f} km^2")
    print(f"  buffer(11000 m) in UTM                      = {m_km2:.3f} km^2")
    ew_km = GEOD.inv(poc.geometry.iloc[0].x, poc.geometry.iloc[0].y,
                     poc.geometry.iloc[0].x + 0.1, poc.geometry.iloc[0].y)[2] / 1000
    ns_km = GEOD.inv(poc.geometry.iloc[0].x, poc.geometry.iloc[0].y,
                     poc.geometry.iloc[0].x, poc.geometry.iloc[0].y + 0.1)[2] / 1000
    print(f"  ratio = {deg_km2 / m_km2:.4f}; 0.1 deg of longitude is {ew_km:.2f} km")
    print(f"  and 0.1 deg of latitude is {ns_km:.2f} km, so the degree buffer is an")
    print(f"  ellipse of area pi*a*b = {np.pi * ew_km * ns_km:.1f} km^2 against a")
    print(f"  11 km circle of area {np.pi * 121.0:.1f} km^2, ratio "
          f"{np.pi * ew_km * ns_km / (np.pi * 121.0):.4f} -- the measured value")

    section("7. Choosing a projection: estimate_utm_crs")
    guessed = stations.estimate_utm_crs()
    print(f"  GeoPandas suggests {guessed} for these stations "
          f"(epsg {guessed.to_epsg()})")
    print(f"  the data span {lon_span:.1f} deg of longitude; UTM zones are 6 deg")
    print(f"  wide, so a single zone already carries a scale-factor error at the")
    print(f"  edges. Measured: the same geometry in the neighbouring zone")
    print(f"    EPSG:32612 -> {utm_area / 1e6:.4f} km^2")
    print(f"    EPSG:32611 -> "
          f"{float(regions.to_crs('EPSG:32611').geometry.area.sum()) / 1e6:.4f} km^2")
    print(f"    EPSG:4326  -> meaningless square degrees")
    equal_area = float(regions.to_crs("EPSG:6933").geometry.area.sum())
    print(f"  an equal-area CRS (EPSG:6933, EASE-Grid 2.0) gives "
          f"{equal_area / 1e6:.4f} km^2")
    print(f"    error = {100 * (equal_area - geo_total) / geo_total:+.4f} % -- "
          f"the right choice whenever area is the quantity of interest")

    section("8. Conversion costs nothing except attention")
    back = regions.to_crs("EPSG:32612").to_crs(WGS84)
    diff = shapely.distance(back.geometry, regions.geometry).max()
    print(f"  lon/lat -> UTM -> lon/lat round trip: max coordinate shift = "
          f"{diff:.3e} deg ({diff * 111_320:.3e} m)")
    print(f"  the round trip is reversible to float precision, so a projection is")
    print(f"  a change of coordinates, not a loss of information -- but every")
    print(f"  interpolation, buffer or area computed in the wrong CRS is not")
    print(f"  recoverable")
    print(f"  CRS survives I/O: hex WKB of the first region "
          f"{len(regions.geometry.iloc[0].wkb)} bytes has no CRS; a GeoPackage "
          f"or GeoJSON file stores or assumes one")


if __name__ == "__main__":
    main()
