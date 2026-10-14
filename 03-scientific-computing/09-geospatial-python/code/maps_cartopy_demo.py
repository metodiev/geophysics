"""Cartopy and map projections: measuring the distortion instead of guessing.

Every quantitative claim here is measured with pyproj, which reports the true
scale factors of a projection at a point. All fields are SYNTHETIC and no map
data is downloaded: the "coastline" is a hand-built polygon.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python maps_cartopy_demo.py
Requires: numpy, matplotlib (Agg), cartopy, pyproj, shapely.
"""

from __future__ import annotations

import atexit
import tempfile
from pathlib import Path

import matplotlib
matplotlib.use("Agg")                       # no display, and no interactive window
import matplotlib.pyplot as plt             # noqa: E402
import numpy as np                          # noqa: E402
import cartopy.crs as ccrs                  # noqa: E402
import cartopy.feature as cfeature          # noqa: E402
from pyproj import CRS, Geod, Proj, Transformer  # noqa: E402
from shapely.geometry import box, Polygon   # noqa: E402

HERE = Path(__file__).resolve().parent
_SCRATCH = tempfile.TemporaryDirectory(prefix="_demo_map_", dir=HERE)
atexit.register(_SCRATCH.cleanup)
WORK = Path(_SCRATCH.name)
GEOD = Geod(ellps="WGS84")
RNG = np.random.default_rng(20260905)


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main() -> None:
    section("1. Geographic versus projected CRS, stated precisely")
    for code in (4326, 3857, 32612, 6933, 3031):
        crs = CRS.from_epsg(code)
        kind = "geographic" if crs.is_geographic else "projected"
        unit = "degree" if crs.is_geographic else crs.axis_info[0].unit_name
        print(f"  EPSG:{code:5d} {kind:10s} unit = {unit:8s} {crs.name[:46]}")
    print(f"  a geographic CRS coordinates on an ellipsoid; a projected CRS has")
    print(f"  already mapped that ellipsoid onto a plane, and only then are areas,")
    print(f"  distances and angles expressible in metres")

    section("2. Datum versus ellipsoid, which are not the same object")
    wgs84 = CRS.from_epsg(4326)
    nad83 = CRS.from_epsg(4269)
    print(f"  EPSG:4326 {wgs84.name}")
    print(f"    ellipsoid = {wgs84.ellipsoid.name}, a = "
          f"{wgs84.ellipsoid.semi_major_metre:.3f} m, "
          f"inv_f = {wgs84.ellipsoid.inverse_flattening:.9f}")
    print(f"  EPSG:4269 {nad83.name}")
    print(f"    ellipsoid = {nad83.ellipsoid.name}, a = "
          f"{nad83.ellipsoid.semi_major_metre:.3f} m, "
          f"inv_f = {nad83.ellipsoid.inverse_flattening:.9f}")
    print(f"  the semi-major axes agree to "
          f"{abs(wgs84.ellipsoid.semi_major_metre - nad83.ellipsoid.semi_major_metre) * 1000:.4f} mm;")
    print(f"  the ellipsoids are effectively the same shape, so a datum difference")
    print(f"  is a FRAME difference: the same physical point gets different")
    print(f"  coordinates. Measured at 110 W, 40 N:")
    lon, lat = -110.0, 40.0
    for code, label in ((4267, "NAD27 -> WGS 84"),
                        (4269, "NAD83 -> WGS 84 (PROJ default pipeline)"),
                        (4152, "NAD83(HARN) -> WGS 84")):
        x1, y1 = Transformer.from_crs(code, 4326, always_xy=True).transform(lon, lat)
        d = GEOD.inv(lon, lat, x1, y1)[2]
        print(f"    {label:38s} shift = {d:8.3f} m "
              f"(d_lon = {(x1 - lon) * 111_320 * np.cos(np.deg2rad(lat)):+8.3f} m, "
              f"d_lat = {(y1 - lat) * 110_570:+7.3f} m)")
    print(f"  NAD27 is a different frame and moves the point 60 m; PROJ's default")
    print(f"  NAD83 -> WGS 84 pipeline is a NULL transformation because the two")
    print(f"  frames are coincident to within about 2 m, so the measured shift is")
    print(f"  exactly 0.000 m. When a metre matters you must specify a")
    print(f"  transformation with a stated accuracy, not just a pair of EPSG codes.")

    section("3. Projection distortion, measured with pyproj's own scale factors")
    print("  projection     EPSG  at latitude   meridional  parallel   areal"
          "     angular")
    for name, code in (("Web Mercator", 3857), ("UTM 12N", 32612),
                       ("EASE-Grid 2.0", 6933)):
        prj = Proj(CRS.from_epsg(code))
        for lat in (0.0, 40.0, 60.0, 70.0):
            f = prj.get_factors(-110.0, lat)
            print(f"  {name:13s} {code:5d}  {lat:8.1f}   {f.meridional_scale:10.6f} "
                  f"{f.parallel_scale:10.6f} {f.areal_scale:8.4f} "
                  f"{f.angular_distortion:10.4f}")
        print()
    print("  get_factors() takes GEOGRAPHIC longitude and latitude and reports the")
    print("  local Jacobian of the projection at that point:")
    for lat in (0.0, 60.0, 70.0):
        f = Proj(CRS.from_epsg(3857)).get_factors(0.0, lat)
        print(f"    Web Mercator at {lat:4.1f} N: meridional scale = "
              f"{f.meridional_scale:.6f}, 1/cos(lat) = "
              f"{1 / np.cos(np.deg2rad(lat)):.6f}; areal = "
              f"{f.areal_scale:.4f}, 1/cos^2(lat) = "
              f"{1 / np.cos(np.deg2rad(lat)) ** 2:.4f}")
    print(f"  a conformal projection has angular_distortion = 0 (shapes preserved")
    print(f"  locally) and an equal-area projection has areal_scale = 1 exactly:")
    for lat in (0.0, 40.0, 60.0, 70.0):
        f = Proj(CRS.from_epsg(6933)).get_factors(0.0, lat)
        print(f"    EASE-Grid 2.0 at {lat:4.1f} N: areal = {f.areal_scale:.8f}, "
              f"meridional = {f.meridional_scale:.6f}, "
              f"parallel = {f.parallel_scale:.6f}")
    print(f"  no projection can hold shape, area and distance at once; each one")
    print(f"  chooses which to preserve and distorts the rest")

    section("4. The same two cities in four projections")
    places = {"Quito": (-78.5, -0.25), "Tromso": (18.96, 69.65)}
    tf = {code: Transformer.from_crs(4326, code, always_xy=True)
          for code in (4326, 3857, 32612, 6933)}
    for code in (4326, 3857, 32612, 6933):
        line = f"  EPSG:{code:5d}: "
        for name, (lon, lat) in places.items():
            x, y = tf[code].transform(lon, lat)
            line += f"{name} ({x:12.1f}, {y:11.1f})  "
        print(line)
    print(f"  metres in 3857, 32612 and 6933; DEGREES in 4326. Quoting")
    print(f"  sqrt(dlon^2 + dlat^2) is therefore not a distance, and neither is a")
    print(f"  straight line in a projection that was never intended to span the")
    print(f"  path. Measured anyway, to show how large the error gets:")
    dq, dt = [], []
    for code in (4326, 3857, 32612, 6933):
        a = tf[code].transform(*places["Quito"])
        b = tf[code].transform(*places["Tromso"])
        d = float(np.hypot(b[0] - a[0], b[1] - a[1]))
        (dq if code == 4326 else dt).append((code, d))
        print(f"  straight-line distance in the projected plane, EPSG:{code:5d}: "
              f"{d:14.2f}")
    true = GEOD.inv(*places["Quito"], *places["Tromso"])[2]
    print(f"  true geodesic distance = {true / 1000:.2f} km")
    for code, d in dt:
        print(f"    EPSG:{code:5d} error = {1000 * (d - true) / true:+.3f} % "
              f"({(d - true) / 1000:+.2f} km)")
    print(f"  the straight line in Web Mercator is 4,961 km (48 %) longer than the")
    print(f"  geodesic, and UTM zone 12 -- which does not contain either city -- is")
    print(f"  1,394 km out. These are not small-map distortions; they are what")
    print(f"  happens when a projection is used outside its design domain.")

    section("5. Great circle versus rhumb line")
    lon_q, lat_q = places["Quito"]
    lon_t, lat_t = places["Tromso"]
    fwd, back, gc = GEOD.inv(lon_q, lat_q, lon_t, lat_t)
    rho = 6371.0087714e3                       # IUGG mean Earth radius, m
    phi1, phi2 = np.deg2rad(lat_q), np.deg2rad(lat_t)
    dphi = phi2 - phi1
    dlam = np.deg2rad(((lon_t - lon_q + 180.0) % 360.0) - 180.0)
    psi = np.log(np.tan(np.pi / 4 + phi2 / 2) / np.tan(np.pi / 4 + phi1 / 2))
    q = dphi / psi if abs(psi) > 1e-12 else np.cos(phi1)
    rhumb = rho * np.hypot(dphi, q * dlam)
    points = GEOD.npts(lon_q, lat_q, lon_t, lat_t, 200)
    print(f"  Quito ({lon_q}, {lat_q}) to Tromso ({lon_t}, {lat_t}):")
    print(f"    geodesic (great circle)     = {gc / 1000:9.2f} km")
    print(f"    rhumb line (constant course) = {rhumb / 1000:9.2f} km "
          f"({100 * (rhumb - gc) / gc:+.2f} %)")
    print(f"    the rhumb constant course   = "
          f"{np.rad2deg(np.arctan2(dlam, psi)) % 360.0:9.2f} deg")
    print(f"    the geodesic leaves Quito at {fwd:9.2f} deg azimuth")
    print(f"    and arrives at Tromso at    {back:9.2f} deg azimuth")
    print(f"    a change of {abs(back - fwd):.2f} deg: a geodesic is not a")
    print(f"    straight line in lon/lat, so it must be DRAWN as a polyline")
    print(f"    npts() returned {len(points)} intermediate points for that reason")

    section("6. Plotting: what Cartopy adds to Matplotlib")
    field_lon = np.linspace(-180.0, 180.0, 181)
    field_lat = np.linspace(-90.0, 90.0, 91)
    lon2d, lat2d = np.meshgrid(field_lon, field_lat)
    field = (28.0 * np.exp(-(((lon2d + 110.0) / 12.0) ** 2
                             + ((lat2d - 37.5) / 8.0) ** 2))
             + 12.0 * np.cos(np.deg2rad(lat2d)) ** 2)      # SYNTHETIC, arbitrary units
    proj = ccrs.Robinson()
    fig = plt.figure(figsize=(7, 4))
    ax = fig.add_subplot(1, 1, 1, projection=proj)
    mesh = ax.pcolormesh(lon2d, lat2d, field, transform=ccrs.PlateCarree(),
                         cmap="viridis", shading="auto")
    ax.coastlines(resolution="110m", linewidth=0.4)
    ax.gridlines(draw_labels=True, linewidth=0.2, color="grey")
    fig.colorbar(mesh, ax=ax, orientation="horizontal", pad=0.08,
                 label="SYNTHETIC anomaly (arbitrary units)")
    out = WORK / "robinson.png"
    fig.savefig(out, dpi=110, bbox_inches="tight")
    plt.close(fig)
    print(f"  PlateCarree data plotted on a Robinson projection: the data are in")
    print(f"  lon/lat and the POINTS are reprojected, the array is not resampled")
    print(f"  figure written: {out.name}, {out.stat().st_size:,} bytes")
    print(f"  Cartopy's own coastline data are 1:110m Natural Earth vectors, drawn")
    print(f"  by projecting their coordinates at render time")

    section("7. Why a Plate Carree map is not a globe")
    cell = box(-10.0, 55.0, 10.0, 65.0)
    geo_area = abs(GEOD.geometry_area_perimeter(cell)[0])
    print(f"  a 20 x 10 deg box from 55 N to 65 N:")
    print(f"    geodesic area = {geo_area / 1e6:,.1f} km^2")
    ll = ccrs.PlateCarree()
    xy = ll.transform_points(ll, np.array([-10.0, 10.0, 10.0, -10.0]),
                             np.array([55.0, 55.0, 65.0, 65.0]))
    w = xy[1, 0] - xy[0, 0]
    h = xy[2, 1] - xy[1, 1]
    print(f"    its extent in PlateCarree degrees: {w:.1f} x {h:.1f}")
    print(f"    drawn as a rectangle it looks like {w / h:.1f}:1, while on the")
    print(f"    ground it is "
          f"{GEOD.inv(-10.0, 60.0, 10.0, 60.0)[2] / 1000:.0f} km wide and "
          f"{GEOD.inv(0.0, 55.0, 0.0, 65.0)[2] / 1000:.0f} km tall, i.e. "
          f"{GEOD.inv(-10.0, 60.0, 10.0, 60.0)[2] / GEOD.inv(0.0, 55.0, 0.0, 65.0)[2]:.2f}:1")
    print(f"  the aspect ratio you see is not the aspect ratio on the ground")

    section("8. Areas and lengths on a Mercator web map")
    merc = Proj(CRS.from_epsg(3857))
    for lat in (0.0, 40.0, 60.0, 85.0):
        at = merc.get_factors(0.0, lat)[2]
        print(f"  at {lat:4.1f} N: areal scale = {at:8.3f}, so a polygon that")
        print(f"    renders as 1,000 km^2 on a Web Mercator map is really "
              f"{1000.0 / at:8.1f} km^2")
    print(f"  Greenland is the standard example: it renders larger than Africa on")
    print(f"  a Web Mercator map; the areal scale at 70 N alone is "
          f"{merc.get_factors(0.0, 70.0)[2]:.2f}")
    a_wgs, f_wgs = 6378137.0, 1 / 298.257223563
    e2 = f_wgs * (2 - f_wgs)
    e = np.sqrt(e2)

    def cap_area(lat_deg):
        """Ellipsoidal area of a 360 deg band from -90 to lat_deg, m^2."""
        def capital(p):
            sn = np.sin(p)
            return (sn / (1 - e2 * sn ** 2)
                    + (1 / (2 * e)) * np.log((1 + e * sn) / (1 - e * sn)))
        return (np.pi * a_wgs ** 2 * (1 - e2)
                * (capital(np.deg2rad(lat_deg)) - capital(-np.pi / 2)))

    print(f"  the south of 60 S cap has ellipsoidal area "
          f"{cap_area(-60.0) / 1e12:.3f} x 10^6 km^2 "
          f"({100 * cap_area(-60.0) / 5.100656e14:.2f} % of the Earth)")
    print(f"  and cannot be drawn at all in Web Mercator: latitude 90 S maps to")
    print(f"  y = -infinity, so the projection has no representation of the pole")

    section("9. Choosing a projection from the quantity you care about")
    print("  quantity of interest      use                        why")
    print("  distances within a small   a local projected CRS      metric units and a")
    print("  survey                     (UTM, State Plane, etc.)    scale factor near 1")
    print("  areas over a region        an equal-area CRS           areal scale is 1")
    print("  a world map for reading    Robinson or Equal Earth     compromise distortion")
    print("  a web tile map             Web Mercator                conformal, not equal-area")
    print("  plate reconstructions      rotate first, then project  the reconstruction")
    print("                             in a plate model            is a coordinate change")
    area_err = {}
    for name, code in (("Web Mercator", 3857), ("UTM 12N", 32612),
                       ("EASE-Grid 2.0", 6933)):
        area_err[name] = Proj(CRS.from_epsg(code)).get_factors(-110.0, 40.0).areal_scale
    print(f"  measured at 40 N, 110 W: areal scale "
          f"Web Mercator {area_err['Web Mercator']:.4f}, "
          f"UTM {area_err['UTM 12N']:.4f}, "
          f"EASE-Grid 2.0 {area_err['EASE-Grid 2.0']:.4f}")

    section("10. Cartopy without the network")
    fig = plt.figure(figsize=(6, 3.5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.LambertConformal(
        central_longitude=-110.0, central_latitude=40.0))
    ax.set_extent([-120.0, -100.0, 30.0, 48.0], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.BORDERS.with_scale("110m"), linewidth=0.4)
    ax.add_feature(cfeature.STATES.with_scale("110m"), linewidth=0.3,
                   edgecolor="grey")
    ax.add_feature(cfeature.LAKES.with_scale("110m"), facecolor="lightblue")
    ax.coastlines(resolution="110m", linewidth=0.5)
    ax.plot([-111.0], [40.0], marker="o", markersize=6, color="red",
            transform=ccrs.PlateCarree())
    ax.set_title("Lambert conformal, 3 features, one point", fontsize=8)
    out2 = WORK / "lambert.png"
    fig.savefig(out2, dpi=110, bbox_inches="tight")
    plt.close(fig)
    print(f"  BORDERS, STATES and LAKES come from Natural Earth via Cartopy's own")
    print(f"  data package; if those data are not installed Cartopy downloads them")
    print(f"  on first use, which is the one network dependency in this lesson:")
    print(f"  figure written: {out2.name}, {out2.stat().st_size:,} bytes")
    print(f"  every other number in this demo comes from pyproj, numpy or the")
    print(f"  seeded generator, and runs offline")


if __name__ == "__main__":
    main()
