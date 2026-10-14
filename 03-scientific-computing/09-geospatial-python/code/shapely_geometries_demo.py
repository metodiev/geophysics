"""Shapely geometries: what is metric, what is not, and where that bites.

All geometries are SYNTHETIC and are built in code; nothing is downloaded. The
demo measures the cost of the two classic mistakes: treating degrees as lengths,
and trusting an invalid polygon.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python shapely_geometries_demo.py
Requires: numpy, shapely, pyproj.
"""

from __future__ import annotations

import json

import numpy as np
import shapely
from pyproj import Geod, Transformer
from shapely import (
    MultiPolygon, Point, Polygon, box, buffer, centroid, convex_hull,
    distance as shp_distance, get_coordinates, is_valid, make_valid, segmentize,
)
from shapely.geometry import LineString, mapping

RNG = np.random.default_rng(20260901)
GEOD = Geod(ellps="WGS84")
TO_UTM = Transformer.from_crs("EPSG:4326", "EPSG:32612", always_xy=True)
DEG_LAT_M = 111_132.0          # nominal metres per degree of latitude
UTM12 = "EPSG:32612"


def _project(transformer):
    """shapely.transform adapter: (N, 2) lon/lat -> (N, 2) projected."""
    def apply(coords: np.ndarray) -> np.ndarray:
        x, y = transformer.transform(coords[:, 0], coords[:, 1])
        return np.column_stack([x, y])
    return apply


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main() -> None:
    section("1. The basic geometries, and the units of every number")
    pt = Point(-110.0, 40.0)
    line = LineString([(-111.0, 39.0), (-110.5, 39.6), (-110.0, 40.0)])
    poly = Polygon([(-111.0, 39.0), (-109.0, 39.0), (-109.0, 40.5), (-111.0, 40.5)])
    print(f"  Point      : {pt.wkt}")
    print(f"  LineString : {len(line.coords)} vertices, length = {line.length:.4f}"
          f"  <- DEGREES, not metres")
    print(f"  Polygon    : {len(poly.exterior.coords)} vertices, "
          f"area = {poly.area:.4f}  <- SQUARE DEGREES")
    print(f"  the numbers are in the coordinate system's own units; shapely itself")
    print(f"  has no idea what a degree is")

    section("2. Degrees as lengths: how wrong, measured in metres")
    d = 1.0                                    # one degree of separation
    for lat in (0.0, 40.0, 50.0, 60.0, 70.0):
        a = Point(-110.0, lat)
        b = Point(-110.0 + d, lat)
        degrees = a.distance(b)
        _, _, metres = GEOD.inv(a.x, a.y, b.x, b.y)
        print(f"  at {lat:5.1f} N: shapely distance = {degrees:.4f} deg, "
              f"geodesic distance = {metres / 1000:7.2f} km "
              f"({metres / 1000 / d:.2f} km per degree)")
    print(f"  so 'distance < 1' in degrees is not a fixed physical threshold: at")
    print(f"  70 N one degree of longitude is "
          f"{GEOD.inv(-110.0, 70.0, -109.0, 70.0)[2] / 1000:.2f} km against "
          f"{DEG_LAT_M / 1000:.2f} km of latitude.")
    lat_only = GEOD.inv(-110.0, 40.0, -110.0, 41.0)[2]
    print(f"  latitude is nearly constant: 1 deg N-S at 40 N = "
          f"{lat_only / 1000:.3f} km ({lat_only / DEG_LAT_M:.5f} of the nominal)")
    print(f"  a 1/111132 scaling factor is therefore not a fix: it is only right")
    print(f"  for the meridional direction, and merely approximate there.")

    section("3. Area in degrees is worse than length in degrees")
    box_deg = box(-111.0, 39.0, -109.0, 40.5)
    print(f"  2 x 1.5 deg box: shapely area = {box_deg.area:.4f} square degrees")
    lon_c, lat_c = [float(v) for v in TransformDegrees().transform(box_deg.bounds)]
    utm = TransformDegrees().to_utm(box_deg)
    geo_area = abs(GEOD.geometry_area_perimeter(box_deg)[0])
    print(f"  geodesic area = {geo_area / 1e6:.4f} km^2")
    print(f"  UTM area      = {utm.area / 1e6:.4f} km^2 "
          f"({100 * (utm.area - geo_area) / geo_area:+.4f} % from the truth)")
    print(f"  the UTM result is trustworthy because the CRS has metre units and a")
    print(f"  scale factor known to ~1 part in 10^4 over the zone.")
    aspect = TransformDegrees().aspect_ratio(box_deg)
    print(f"  the same box as a rectangle in UTM is "
          f"{aspect[0] / 1000:.1f} km x {aspect[1] / 1000:.1f} km; its degree")
    print(f"  width and degree height are NOT proportional to those numbers.")

    section("4. Buffering in degrees is not a metric buffer")
    city = Point(-110.0, 60.0)
    buf_deg = city.buffer(0.05)
    utm_city = TO_UTM.transform(city.x, city.y)
    buf_m = TransformDegrees().to_utm(city).buffer(5000.0)
    print(f"  buffer(0.05) on {city.wkt}:")
    print(f"    bounds in degrees = "
          f"{tuple(round(v, 4) for v in buf_deg.bounds)}")
    ns = GEOD.inv(city.x, city.y, city.x, city.y + 0.05)[2]
    ew = GEOD.inv(city.x, city.y, city.x + 0.05, city.y)[2]
    print(f"    0.05 deg north-south = {ns / 1000:.3f} km")
    print(f"    0.05 deg east-west   = {ew / 1000:.3f} km "
          f"({100 * abs(ew - ns) / ns:.1f} % shorter -- the buffer is an ellipse)")
    ellipse = np.pi * (ns / 1000) * (ew / 1000)
    degree_area = abs(GEOD.geometry_area_perimeter(buf_deg)[0]) / 1e6
    print(f"    area = {degree_area:.3f} km^2")
    print(f"    the true shape is an ellipse with semi-axes {ns / 1000:.3f} km and "
          f"{ew / 1000:.3f} km, area pi*a*b = {ellipse:.3f} km^2 "
          f"({100 * (degree_area - ellipse) / ellipse:+.2f} %)")
    print(f"    a circle of the same radius would be "
          f"{np.pi * (ns / 1000) ** 2:.3f} km^2, i.e. "
          f"{np.pi * (ns / 1000) ** 2 / degree_area:.1f}x too big")
    print(f"  buffer(5000.0) after projecting to {UTM12}:")
    print(f"    area = {buf_m.area / 1e6:.3f} km^2 vs pi*r^2 = "
          f"{np.pi * 25.0:.3f} km^2 "
          f"({100 * (buf_m.area / 1e6 - np.pi * 25.0) / (np.pi * 25.0):+.3f} %)")
    print(f"    the residual difference is the UTM scale factor at this location,")
    print(f"    which is not exactly 1")
    back = TransformDegrees.from_utm(buf_m)
    d_lon = back.bounds[2] - back.bounds[0]
    d_lat = back.bounds[3] - back.bounds[1]
    print(f"    converted back to lon/lat its extent is "
          f"{d_lon:.4f} deg of longitude by {d_lat:.4f} deg of latitude:")
    print(f"    a metric circle is NOT a constant-degree shape, and the ratio")
    print(f"    {d_lon / d_lat:.3f} is 1/cos(60 deg) = {1 / np.cos(np.deg2rad(60.0)):.3f}")

    section("5. Invalid geometry: the bow-tie")
    bow = Polygon([(0.0, 0.0), (1.0, 1.0), (1.0, 0.0), (0.0, 1.0)])
    print(f"  ring = (0,0) (1,1) (1,0) (0,1): is_valid = {is_valid(bow)}, "
          f"reason = {shapely.is_valid_reason(bow)}")
    print(f"  its reported area is {bow.area:.4f} -- not 0.5, not 1.0, but ZERO,")
    print(f"  because the two triangles cancel in the shoelace sum")
    repaired = make_valid(bow)
    print(f"  shapely.make_valid -> {repaired.geom_type} of "
          f"{len(repaired.geoms)} parts, area = {repaired.area:.4f} "
          f"(both lobes, the correct answer)")
    zero = bow.buffer(0)
    print(f"  the older 'buffer(0)' repair -> {zero.geom_type}, area = "
          f"{zero.area:.4f} (ONE lobe: the other is silently lost)")
    print(f"  an invalid polygon does not raise; it returns a plausible-looking")
    print(f"  wrong number, which is why is_valid() belongs at the start of any")
    print(f"  area computation")

    section("6. contains / covers: the boundary case that breaks joins")
    sq = box(0.0, 0.0, 1.0, 1.0)
    edge = Point(0.5, 0.0)
    inside = Point(0.5, 0.5)
    for label, p in (("interior", inside), ("on the boundary", edge)):
        print(f"  point {label:16s} -> contains = {sq.contains(p)}, "
              f"covers = {sq.covers(p)}, intersects = {sq.intersects(p)}")
    print(f"  a spatial join that uses 'contains' drops boundary points; "
          f"'intersects' keeps them")
    print(f"  and non-empty returns: "
          f"{[sq.intersection(p).geom_type for p in (inside, edge)]}")

    section("7. Vectorised shapely 2 operations on arrays")
    pts = shapely.points(RNG.uniform(-111.0, -109.0, 5000),
                         RNG.uniform(38.0, 41.0, 5000))
    region = box(-110.5, 39.0, -109.5, 40.0)
    inside_mask = shapely.within(pts, region)
    print(f"  {pts.size} points tested against one box in one call: "
          f"{int(inside_mask.sum()):,} inside ({100 * inside_mask.mean():.2f} %)")
    print(f"  shapely.area on a point array = {np.unique(shapely.area(pts))} "
          f"(points have no area)")
    buf = shapely.buffer(pts[:5], 0.01)
    print(f"  buffer of 5 points by 0.01 deg -> {[round(b.area, 6) for b in buf]}")
    print(f"  get_coordinates returns a flat float64 array: "
          f"{get_coordinates(region).shape} for the box")

    section("8. Centroid is area-weighted; the vertex mean is not")
    # A polygon with a long, nearly degenerate spur: vertices cluster on one side.
    coarse = Polygon([(0.0, 0.0), (10.0, 0.0), (10.0, 10.0)])
    spur = LineString([(10.0, 10.0), (10.0001, 10.0001), (10.0002, 9.9999),
                       (10.0003, 10.0002), (10.0004, 9.9998)])
    verts = list(coarse.exterior.coords) + list(spur.coords)[1:]
    with_spur = Polygon(verts + [(10.0, 10.0)])
    coords = np.array(with_spur.exterior.coords)
    vertex_mean = coords[:-1].mean(axis=0)
    c = with_spur.centroid
    print(f"  vertices = {len(coords) - 1}; area = {with_spur.area:.4f}")
    print(f"  vertex mean = ({vertex_mean[0]:.4f}, {vertex_mean[1]:.4f})")
    print(f"  centroid    = ({c.x:.4f}, {c.y:.4f})")
    print(f"  the two differ by {c.distance(Point(*vertex_mean)):.4f} units: the")
    print(f"  centroid integrates area, the vertex mean counts vertices, and the")
    print(f"  spur carries {len(spur.coords) - 1} of {len(coords) - 1} vertices")

    section("9. Serialisation: WKT, WKB and GeoJSON")
    region2 = Polygon([(-110.0, 39.0), (-109.0, 39.0), (-109.0, 39.5),
                       (-110.0, 39.5)])
    wkt = region2.wkt
    wkb = region2.wkb
    geo = json.dumps(mapping(region2))
    print(f"  WKT    : {len(wkt)} characters; area preserved exactly: "
          f"{shapely.from_wkt(wkt).area == region2.area}")
    print(f"  WKB    : {len(wkb)} bytes, {2 * len(wkb)} hex characters")
    print(f"  GeoJSON: {len(geo)} characters; coordinates are lon,lat by")
    print(f"           convention, and CRS is NOT stored in RFC 7946 GeoJSON")
    print(f"  round trip difference: "
          f"{abs(shapely.from_wkb(wkb).area - region2.area):.3e}")
    print(f"  WKB is the compact binary choice; GeoJSON is the interoperable")
    print(f"  text choice, but neither carries the CRS reliably.")

    section("10. Densifying before projecting")
    straight = LineString([(-110.0, 60.0), (-100.0, 60.0)])
    dense = segmentize(straight, 0.05)
    print(f"  a 10 deg segment at 60 N: {len(straight.coords)} vertices -> "
          f"{len(dense.coords)} after segmentize(max_segment_length=0.05)")
    geodesic = abs(GEOD.geometry_length(straight))
    lat_arc = 2.0 * np.pi * 3_197_377.0 * np.deg2rad(10.0) / (2.0 * np.pi)
    print(f"  three different 'lengths' of the same two points:")
    print(f"    geodesic between the endpoints        = "
          f"{geodesic / 1000:.3f} km (cuts poleward of the parallel)")
    print(f"    arc along the 60 N parallel           = "
          f"{lat_arc / 1000:.3f} km ({(lat_arc - geodesic) / 1000:.2f} km longer)")
    simple = TransformDegrees().to_utm(straight)
    fin = TransformDegrees().to_utm(dense)
    print(f"    straight 2-vertex chord projected      = "
          f"{simple.length / 1000:.3f} km")
    print(f"    {len(dense.coords)}-vertex curve projected           = "
          f"{fin.length / 1000:.3f} km")
    print(f"  densifying makes the projected line follow the curve you drew, not")
    print(f"  the geodesic. The three numbers differ by up to "
          f"{100 * (lat_arc - geodesic) / geodesic:.3f} %, so 'the distance")
    print(f"  between two points' is only defined once you say which curve")


class TransformDegrees:
    """Small helper: reproject shapely geometries between lon/lat and UTM 12N."""

    @staticmethod
    def to_utm(geom):
        return shapely.transform(geom, _project(TO_UTM))

    @staticmethod
    def from_utm(geom):
        return shapely.transform(
            geom, _project(Transformer.from_crs(UTM12, "EPSG:4326",
                                                always_xy=True)))

    @staticmethod
    def transform(bounds):
        return TO_UTM.transform(bounds[0], bounds[1])

    @staticmethod
    def aspect_ratio(geom):
        u = TransformDegrees.to_utm(geom)
        b = u.bounds
        return (b[2] - b[0], b[3] - b[1])


if __name__ == "__main__":
    main()
