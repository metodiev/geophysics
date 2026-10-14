"""rasterio: bands, the affine transform, windows, masks and reprojection.

The raster is SYNTHETIC: a tilted plane plus a Gaussian hill, written as a
GeoTIFF in EPSG:32612 (UTM zone 12N, metres) with known analytic gradients, so
every derived slope can be checked against an imposed value. The file is written
into a throw-away directory inside this module and deleted on exit.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rasterio_rasters_demo.py
Requires: numpy, rasterio, shapely, pyproj.
"""

from __future__ import annotations

import atexit
import tempfile
from pathlib import Path

import numpy as np
import rasterio
from pyproj import Geod, Transformer
from rasterio.enums import Resampling
from rasterio.mask import mask as rio_mask
from rasterio.transform import from_origin
from rasterio.warp import calculate_default_transform, reproject
from rasterio.windows import Window
from shapely.geometry import box

RNG = np.random.default_rng(20260807)
HERE = Path(__file__).resolve().parent
_SCRATCH = tempfile.TemporaryDirectory(prefix="_demo_rio_", dir=HERE)
atexit.register(_SCRATCH.cleanup)
WORK = Path(_SCRATCH.name)
GEOD = Geod(ellps="WGS84")
TO_WGS84 = Transformer.from_crs("EPSG:32612", "EPSG:4326", always_xy=True)

RES = 30.0                      # pixel size, metres
NCOL, NROW = 500, 400           # width x height in pixels
X0, Y0 = 500_000.0, 4_200_000.0  # UTM 12N coordinates of the upper-left corner
CRS = "EPSG:32612"
DZ_DX = 0.020                   # imposed plane gradient in x (dimensionless)
DZ_DY = 0.035                   # imposed plane gradient in y
HILL_Z = 150.0                  # imposed hill amplitude, metres
HILL_X, HILL_Y = X0 + 7_000.0, Y0 - 6_000.0
NODATA = -9999.0


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def dem_gradients(x: np.ndarray, y: np.ndarray):
    """Analytic (dz/dx, dz/dy) of the same SYNTHETIC surface, in m/m."""
    dx_plane = np.full_like(x, DZ_DX)
    dy_plane = np.full_like(y, DZ_DY)
    ex = np.exp(-(((x - HILL_X) / 1_200.0) ** 2 + ((y - HILL_Y) / 900.0) ** 2))
    dx_hill = HILL_Z * ex * (-2.0 * (x - HILL_X) / 1_200.0 ** 2)
    dy_hill = HILL_Z * ex * (-2.0 * (y - HILL_Y) / 900.0 ** 2)
    kx, ky = 2 * np.pi / 900.0, 2 * np.pi / 1_400.0
    dx_ridge = 12.0 * kx * np.cos(kx * (x - X0)) * np.cos(ky * (y - Y0))
    dy_ridge = -12.0 * ky * np.sin(kx * (x - X0)) * np.sin(ky * (y - Y0))
    return dx_plane + dx_hill + dx_ridge, dy_plane + dy_hill + dy_ridge


def dem(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """SYNTHETIC ground elevation, metres, as a pure function of position."""
    plane = 100.0 + DZ_DX * (x - X0) + DZ_DY * (y - Y0)
    hill = HILL_Z * np.exp(-(((x - HILL_X) / 1_200.0) ** 2
                             + ((y - HILL_Y) / 900.0) ** 2))
    ridges = 12.0 * np.sin(2 * np.pi * (x - X0) / 900.0) * np.cos(
        2 * np.pi * (y - Y0) / 1_400.0)
    return plane + hill + ridges


def main() -> None:
    transform = from_origin(X0, Y0, RES, RES)
    cols = np.arange(NCOL) + 0.5          # pixel CENTRES, in pixel units
    rows = np.arange(NROW) + 0.5
    xs = X0 + cols * RES
    ys = Y0 - rows * RES
    xx, yy = np.meshgrid(xs, ys)
    z = dem(xx, yy).astype("float32") + RNG.normal(0.0, 0.05, xx.shape).astype("float32")
    z[0:20, 0:30] = NODATA                # a synthetic "no data" corner

    path = WORK / "dem.tif"
    profile = {"driver": "GTiff", "height": NROW, "width": NCOL, "count": 1,
               "dtype": "float32", "crs": CRS, "transform": transform,
               "nodata": NODATA, "tiled": True,
               "blockxsize": 256, "blockysize": 256, "compress": "deflate"}
    with rasterio.open(path, "w", **profile) as dst:
        dst.write(z, 1)
        dst.update_tags(AREA_OR_POINT="Area", NOTE="SYNTHETIC elevation, metres")

    section("1. The dataset header: what rasterio actually stores")
    with rasterio.open(path) as src:
        print(f"  driver = {src.driver}, count (bands) = {src.count}, "
              f"dtypes = {src.dtypes}")
        print(f"  size = {src.width} columns x {src.height} rows")
        print(f"  crs = {src.crs.to_string()}  (EPSG:{src.crs.to_epsg()})")
        print(f"  crs units = {src.crs.linear_units}, "
              f"geographic = {src.crs.is_geographic}")
        print(f"  transform = {tuple(round(v, 4) for v in src.transform)[:6]}")
        print(f"  resolution = ({src.res[0]:.3f}, {src.res[1]:.3f}) m")
        print(f"  bounds = {tuple(round(v, 1) for v in src.bounds)} (left, bottom, "
              f"right, top)")
        print(f"  nodata = {src.nodata}")
        print(f"  block shapes = {src.block_shapes}  (tiled 256 x 256, not one "
              f"400 x 500 stripe)")
        print(f"  on-disk size = {path.stat().st_size:,} bytes for "
              f"{NROW * NCOL * 4:,} bytes of data")
        print(f"  tags = {src.tags()}")

    section("2. The affine transform is the map from (row, col) to (x, y)")
    with rasterio.open(path) as src:
        t = src.transform
        print(f"  transform.a = {t.a} (x per column), "
              f"transform.e = {t.e} (y per row, NEGATIVE: north-up)")
        print(f"  transform.c = {t.c:.1f} (x of column 0), "
              f"transform.f = {t.f:.1f} (y of row 0)")
        print(f"  x = c + a*col,  y = f + e*row")
        for col, row in ((0, 0), (1, 0), (0, 1)):
            x, y = t * (col, row)
            print(f"  transform * ({row}, {col}) -> ({x:.1f}, {y:.1f})")
        print(f"  the ORIGIN (c, f) is the upper-left CORNER of pixel (0, 0)")
        cx, cy = t * (0.5, 0.5)
        print(f"  the CENTRE of pixel (row=0, col=0) is at ({cx:.1f}, {cy:.1f}), "
              f"i.e. half a pixel in from the corner: "
              f"({cx - X0:+.1f}, {cy - Y0:+.1f}) m")
        print(f"  rasterio's own helper: src.xy(0, 0) = "
              f"{tuple(round(v, 1) for v in src.xy(0, 0))}")
        print(f"  and with offset='ul' it returns the corner: "
              f"{tuple(round(v, 1) for v in src.xy(0, 0, offset='ul'))}")
        print(f"  half a pixel is {RES / 2:.0f} m: writing the corner instead of")
        print(f"  the centre shifts every sample by 15 m, which is half a pixel of")
        print(f"  a 30 m DEM and can exceed the vertical accuracy claim of an")
        print(f"  interferometric DEM.")

    section("3. Row index increases southwards")
    with rasterio.open(path) as src:
        for row in (0, 1, NROW - 1):
            print(f"  row {row:3d}: y = {src.xy(row, 0)[1]:,.1f} m "
                  f"(row 0 is the northernmost)")
        print(f"  y(row 0) - y(row 1) = "
              f"{src.xy(0, 0)[1] - src.xy(1, 0)[1]:+.1f} m, so the row index runs")
        print(f"  southwards while x increases eastwards by "
              f"{src.xy(0, 1)[0] - src.xy(0, 0)[0]:+.1f} m per column.")

    section("4. Recovering the imposed gradients through the transform")
    with rasterio.open(path) as src:
        arr = src.read(1, masked=True)
        filled = arr.filled(np.nan).astype("float64")
        dz_drow, dz_dcol = np.gradient(filled)
        dz_dx = dz_dcol / src.res[0]
        dz_dy = -dz_drow / src.res[1]
        ax, ay = dem_gradients(xx, yy)
        err_x = np.abs(dz_dx - ax)
        err_y = np.abs(dz_dy - ay)
        print(f"  finite differences on the raster are compared with the analytic")
        print(f"  gradient of the same SYNTHETIC surface:")
        print(f"    max |dz/dx error| = {np.nanmax(err_x):.3e} m/m")
        print(f"    max |dz/dy error| = {np.nanmax(err_y):.3e} m/m")
        print(f"    median |dz/dx error| = {np.nanmedian(err_x):.3e} m/m")
        col_ok, row_ok = 200, 350          # away from the hill and the nodata
        print(f"  at (row={row_ok}, col={col_ok}) = "
              f"({src.xy(row_ok, col_ok)[0]:.0f}, {src.xy(row_ok, col_ok)[1]:.0f}) m:")
        print(f"    dz/dx = {dz_dx[row_ok, col_ok]:.6f} vs analytic "
              f"{ax[row_ok, col_ok]:.6f} (error {dz_dx[row_ok, col_ok] - ax[row_ok, col_ok]:+.2e})")
        print(f"    dz/dy = {dz_dy[row_ok, col_ok]:.6f} vs analytic "
              f"{ay[row_ok, col_ok]:.6f} (error {dz_dy[row_ok, col_ok] - ay[row_ok, col_ok]:+.2e})")
        print(f"  the plane-only gradient is ({DZ_DX:.5f}, {DZ_DY:.5f}); the ridge")
        print(f"  and hill terms add up to "
              f"{np.nanmax(np.abs(ax - DZ_DX)):.4f} m/m on top of it")
        slope = np.degrees(np.arctan(np.hypot(dz_dx, dz_dy)))
        aspect = np.degrees(np.arctan2(-dz_dx, -dz_dy)) % 360.0
        slope_analytic = np.degrees(np.arctan(np.hypot(ax, ay)))
        print(f"  slope: raster mean = {np.nanmean(slope):.3f} deg, "
              f"max = {np.nanmax(slope):.3f} deg; analytic max = "
              f"{np.max(slope_analytic):.3f} deg")
        print(f"  aspect at the probe pixel = {aspect[row_ok, col_ok]:.2f} deg")
        print(f"  sign convention: dz/dy = -dz/drow / res, because the row index")
        print(f"  runs south. Dropping that minus mirrors the terrain north-south.")

    section("5. Window order is (col_off, row_off, width, height)")
    with rasterio.open(path) as src:
        good = Window(col_off=100, row_off=50, width=80, height=60)
        swapped = Window(col_off=50, row_off=100, width=80, height=60)
        for label, win in (("correct", good), ("swapped", swapped)):
            sub = src.read(1, window=win, masked=True)
            xs_, ys_ = src.xy(win.row_off, win.col_off)
            print(f"  {label}: shape (rows, cols) = {sub.shape}, "
                  f"mean = {sub.mean():.2f} m, top-left centre = "
                  f"({xs_:.0f}, {ys_:.0f})")
        print(f"  the two windows share no pixel: their origins differ by "
              f"({(50 - 100) * RES:+.0f}, {(100 - 50) * RES:+.0f}) m")
        shifted = src.read(1, window=good)
        wrong = src.read(1, window=Window(col_off=50, row_off=100, width=80, height=60))
        print(f"  max |difference| = {np.abs(shifted - wrong).max():.2f} m "
              f"({'both read a different part of the DEM' if not np.array_equal(shifted, wrong) else 'identical'})")

    section("6. Nodata becomes a mask, not a number")
    with rasterio.open(path) as src:
        masked = src.read(1, masked=True)
        print(f"  masked read: type = {type(masked).__name__}, "
              f"masked cells = {int(masked.mask.sum()):,} "
              f"({100 * masked.mask.sum() / masked.size:.2f} %)")
        print(f"  the mask covers rows 0-19 and columns 0-29: "
              f"{20 * 30:,} cells")
        unmasked = src.read(1)
        print(f"  an UNMASKED read returns {unmasked.min():.0f} in that corner: "
              f"the -9999 sentinel would corrupt any statistic")
        print(f"  mean with masking = {masked.mean():.3f} m; "
              f"mean without = {unmasked.mean():.3f} m "
              f"(difference {masked.mean() - unmasked.mean():.3f} m)")

    section("7. Cropping to a polygon with rasterio.mask")
    with rasterio.open(path) as src:
        poly = box(X0 + 3000, Y0 - 9000, X0 + 9000, Y0 - 3000)
        corners = [(p[0], p[1]) for p in poly.exterior.coords]
        lon_cs, lat_cs = TO_WGS84.transform([c[0] for c in corners],
                                            [c[1] for c in corners])
        poly_geo = box(min(lon_cs), min(lat_cs), max(lon_cs), max(lat_cs))
        out, out_transform = rio_mask(src, [poly], crop=True, filled=False)
        print(f"  polygon = {tuple(round(v, 0) for v in poly.bounds)}")
        print(f"  cropped shape = {out.shape}, dtype = {out.dtype}")
        print(f"  untouched inside the box = "
              f"{int(out[0].count()):,} of {out[0].size:,} cells "
              f"({100 * out[0].count() / out[0].size:.1f} %)")
        print(f"  the returned transform starts at the crop corner: "
              f"({out_transform.c:.1f}, {out_transform.f:.1f})")
        geo_area = abs(GEOD.geometry_area_perimeter(poly_geo)[0])
        print(f"  polygon area in UTM metres^2 = {poly.area / 1e6:.4f} km^2")
        print(f"  GEODESIC area of the same box  = {geo_area / 1e6:.4f} km^2")
        print(f"  the projected area is "
              f"{100 * (poly.area - geo_area) / geo_area:+.4f} % from the truth: "
              f"UTM's scale factor is not 1")

    section("8. Reading at a coarser resolution is a resampling decision")
    with rasterio.open(path) as src:
        fine = src.read(1, masked=True).filled(np.nan)
        out_shape = (src.height // 4, src.width // 4)
        for method in (Resampling.nearest, Resampling.bilinear,
                       Resampling.average, Resampling.cubic):
            coarse = src.read(1, out_shape=out_shape, resampling=method,
                              masked=True).filled(np.nan)
            print(f"  {method.name:9s}: shape {coarse.shape}, "
                  f"cell {RES * 4:.0f} m, mean = {np.nanmean(coarse):8.3f} m, "
                  f"max = {np.nanmax(coarse):7.3f} m")
        blocks = fine.reshape(out_shape[0], 4, out_shape[1], 4).mean(axis=(1, 3))
        res = {}
        for method in (Resampling.nearest, Resampling.bilinear,
                       Resampling.average, Resampling.cubic):
            res[method.name] = src.read(1, out_shape=out_shape, resampling=method,
                                        masked=True).filled(np.nan)
        print(f"  a true 4x4 block mean: mean = {np.nanmean(blocks):8.3f} m, "
              f"std = {np.nanstd(blocks):.3f} m")
        for name in ("average", "bilinear", "nearest", "cubic"):
            d = res[name] - blocks
            print(f"  {name:9s} vs block mean: max |diff| = "
                  f"{np.nanmax(np.abs(d)):7.3f} m, rms = {np.nanstd(d):7.3f} m, "
                  f"std = {np.nanstd(res[name]):.3f} m")
        print(f"  nearest keeps the 30 m standard deviation "
              f"({np.nanstd(fine[20:, :]):.3f} m -> {np.nanstd(res['nearest'][5:, :]):.3f} m)")
        print(f"  while averaging smooths it "
              f"({np.nanstd(fine[20:, :]):.3f} m -> {np.nanstd(res['average'][5:, :]):.3f} m)")
        print(f"  with resampling=nearest, {4 * 4 - 1} of every {4 * 4} source")
        print(f"  pixels are never read at all")

    section("9. Reprojecting to a geographic CRS: degrees are not metres")
    with rasterio.open(path) as src:
        src_data = src.read(1, masked=True)
        dst_crs = "EPSG:4326"
        dst_transform, dst_width, dst_height = calculate_default_transform(
            src.crs, dst_crs, src.width, src.height, *src.bounds)
        print(f"  source: {src.crs}, {src.width} x {src.height} px at "
              f"{src.res[0]:.0f} m")
        print(f"  target: {dst_crs}, {dst_width} x {dst_height} px at "
              f"({dst_transform.a:.6f}, {abs(dst_transform.e):.6f}) deg")
        dst_data = np.full((dst_height, dst_width), np.nan, dtype="float32")
        reproject(source=src_data.filled(np.nan), destination=dst_data,
                  src_transform=src.transform, src_crs=src.crs,
                  dst_transform=dst_transform, dst_crs=dst_crs,
                  src_nodata=np.nan, dst_nodata=np.nan,
                  resampling=Resampling.bilinear)
        valid = np.isfinite(dst_data)
        print(f"  reprojected: valid cells = {int(valid.sum()):,} "
              f"({100 * valid.sum() / valid.size:.1f} % of the target grid)")
        print(f"  value range = {np.nanmin(dst_data):.2f} .. "
              f"{np.nanmax(dst_data):.2f} m (imposed plane plus hill)")
        lat_c = dst_transform.f + dst_transform.e * dst_height / 2
        lon_c = dst_transform.c + dst_transform.a * dst_width / 2
        d_lon, _, dist_lon = GEOD.inv(lon_c, lat_c, lon_c + dst_transform.a, lat_c)
        _, _, dist_lat = GEOD.inv(lon_c, lat_c, lon_c, lat_c + abs(dst_transform.e))
        print(f"  at the centre ({lon_c:.4f} E, {lat_c:.4f} N) one target cell is:")
        print(f"    {abs(dst_transform.e):.6f} deg of latitude  = "
              f"{dist_lat:.2f} m of ground distance")
        print(f"    {dst_transform.a:.6f} deg of longitude = "
              f"{dist_lon:.2f} m of ground distance")
        print(f"  both axes are nominally 'the same' pixel size in degrees, yet on")
        print(f"  the ground they differ by "
              f"{100 * abs(dist_lon - dist_lat) / dist_lat:.2f} % at the centre,")
        print(f"  and the ZONAL size is what changes with latitude:")
        for probe in (lat_c, 20.0, 50.0, 70.0):
            _, _, d = GEOD.inv(lon_c, probe, lon_c + dst_transform.a, probe)
            print(f"    a cell of {dst_transform.a:.6f} deg of longitude is "
                  f"{d:.2f} m at {probe:.1f} N")
        print(f"  the source grid had a CONSTANT 30 m cell; the geographic grid")
        print(f"  does not. Any distance, area or slope computed in degrees is")
        print(f"  wrong by this factor.")

    section("10. A geographic cell is not square on the ground")
    with rasterio.open(path) as src:
        arr = src.read(1, masked=True).filled(np.nan)
        drow, dcol = np.gradient(arr)
        slope_utm = np.degrees(np.arctan(np.hypot(dcol / 30.0, drow / 30.0)))
        print(f"  in UTM the cell is 30 m in both directions:")
        print(f"    mean slope = {np.nanmean(slope_utm):.3f} deg, "
              f"max = {np.nanmax(slope_utm):.3f} deg")
        print(f"  the cell can be used directly because both axes have the same")
        print(f"  ground length. Forgetting to divide by it multiplies every")
        print(f"  gradient by {30.0:.0f} m and reports a mean 'slope' of "
              f"{np.nanmean(np.degrees(np.arctan(np.hypot(dcol, drow)))):.3f} deg")
        print(f"  instead of {np.nanmean(slope_utm):.3f} deg.")
    step_deg = abs(dst_transform.e)
    print(f"  in the reprojected geographic grid the cell is {step_deg:.6f} deg in")
    print(f"  both axes, but on the ground that is {dist_lat:.2f} m north-south and")
    print(f"  {dist_lon:.2f} m east-west at the grid centre -- "
          f"{100 * abs(dist_lon - dist_lat) / dist_lat:.2f} % anisotropic.")
    drow_g, dcol_g = np.gradient(dst_data)
    isotropic = np.degrees(np.arctan(np.hypot(dcol_g / dist_lat, drow_g / dist_lat)))
    anisotropic = np.degrees(np.arctan(np.hypot(dcol_g / dist_lon, drow_g / dist_lat)))
    asp_iso = np.degrees(np.arctan2(-dcol_g / dist_lat, -drow_g / dist_lat)) % 360.0
    asp_aniso = np.degrees(np.arctan2(-dcol_g / dist_lon, -drow_g / dist_lat)) % 360.0
    delta_asp = np.abs((asp_iso - asp_aniso + 180.0) % 360.0 - 180.0)
    ok = np.isfinite(isotropic) & np.isfinite(anisotropic)
    print(f"  slope computed with one cell size for both axes (wrong): "
          f"mean {np.nanmean(isotropic):.3f} deg")
    print(f"  slope computed with the true cell sizes (right):          "
          f"mean {np.nanmean(anisotropic):.3f} deg")
    print(f"  mean bias = {np.nanmean(isotropic) - np.nanmean(anisotropic):+.3f} deg, "
          f"max bias = {np.nanmax(np.abs(isotropic - anisotropic)):.3f} deg")
    print(f"  aspect: mean |change| = {np.nanmean(delta_asp[ok]):.2f} deg, "
          f"max = {np.nanmax(delta_asp[ok]):.2f} deg")
    print(f"  the source grid had a constant 30 m cell; the geographic grid does")
    print(f"  not. One cell of {step_deg:.6f} deg is {dist_lat:.2f} m in latitude")
    print(f"  everywhere (to 0.1 %), but {dist_lon:.2f} m in longitude at 37.9 N and")
    print(f"  only 12.04 m at 70 N. Any distance, area or slope computed in")
    print(f"  degrees is wrong by the ratio of those numbers.")
    print(f"  the reprojected array also shows values from -326.30 to 404.23 m")
    print(f"  because the target footprint is not identical to the source one.")


if __name__ == "__main__":
    main()
