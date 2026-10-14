"""xarray Dataset: variables on shared dims, alignment, weights, groupby.

All data are SYNTHETIC. The area-weighting section measures the difference
between a naive grid mean and a proper cell-area-weighted mean, and compares the
usual ``cos(lat)`` weight with true WGS 84 ellipsoidal cell areas computed by
pyproj.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python xarray_dataset_demo.py
Requires: numpy, xarray, pyproj, shapely (for geodesic areas).
"""

from __future__ import annotations

import atexit
import tempfile
from pathlib import Path

import numpy as np
import xarray as xr
from pyproj import Geod
from shapely.geometry import Polygon

RNG = np.random.default_rng(20260803)
HERE = Path(__file__).resolve().parent
_SCRATCH = tempfile.TemporaryDirectory(prefix="_demo_ds_", dir=HERE)
atexit.register(_SCRATCH.cleanup)
WORK = Path(_SCRATCH.name)
GEOD = Geod(ellps="WGS84")


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main() -> None:
    lon = np.arange(-180.0, 180.0, 3.0)        # 120 columns (global)
    lat = np.arange(-88.5, 88.6, 3.0)          # 60 rows
    lon2d, lat2d = np.meshgrid(lon, lat)

    gauss = 28.0 * np.exp(-(((lon2d + 110.0) / 1.4) ** 2 + ((lat2d - 37.5) / 0.9) ** 2))
    polar = 12.0 * (np.abs(lat2d) / 88.5) ** 2          # strong meridional gradient
    noise = RNG.normal(0.0, 0.05, lon2d.shape)
    anomaly = xr.DataArray(gauss + polar + noise, dims=("lat", "lon"),
                           coords={"lat": lat, "lon": lon}, name="anomaly",
                           attrs={"units": "mGal"})
    elevation = xr.DataArray(2000.0 * np.cos(np.deg2rad(lat2d)) + gauss * 30.0,
                             dims=("lat", "lon"), coords={"lat": lat, "lon": lon},
                             name="elevation", attrs={"units": "m"})
    time = xr.date_range("2015-01-01", periods=36, freq="MS")
    temp = (15.0 - 0.6 * np.abs(lat2d)
            + 4.0 * np.cos(2 * np.pi * np.arange(36) / 12.0)[:, None, None]
            + RNG.normal(0.0, 0.2, (36, lat.size, lon.size)))
    temperature = xr.DataArray(temp, dims=("time", "lat", "lon"),
                               coords={"time": time, "lat": lat, "lon": lon},
                               name="t2m", attrs={"units": "degC",
                                                  "long_name": "SYNTHETIC 2 m air temperature"})
    ds = xr.Dataset({"anomaly": anomaly, "elevation": elevation, "t2m": temperature},
                    attrs={"title": "SYNTHETIC dataset", "Conventions": "CF-1.11"})

    section("1. Dataset anatomy: data_vars, coords, dims")
    print(f"  data_vars = {list(ds.data_vars)}")
    print(f"  coords    = {list(ds.coords)}")
    print(f"  dims      = {dict(ds.sizes)}")
    print(f"  anomaly shape {ds.anomaly.shape}, t2m shape {ds.t2m.shape}")
    print(f"  every variable names the dims it uses; 'lat' and 'lon' are shared")
    print(f"  total size in memory = {ds.nbytes:,} bytes")

    section("2. Selecting from a Dataset keeps the other variables untouched")
    point = ds.sel(lon=-111.0, lat=37.5)
    print(f"  ds.sel(lon=-111, lat=37.5): anomaly = {float(point.anomaly):.4f} mGal, "
          f"elevation = {float(point.elevation):.1f} m, "
          f"t2m has {point.t2m.size} time steps")
    print(f"  note: lon=-110.0 raises KeyError -- the 3 deg grid has no such label")
    band = ds.sel(lat=slice(30.0, 45.0), lon=slice(-120.0, -100.0))
    print(f"  box 30-45 N, 120-100 W: anomaly subset shape = {band.anomaly.shape} "
          f"({band.anomaly.size:,} of {ds.anomaly.size:,} cells, "
          f"{100 * band.anomaly.size / ds.anomaly.size:.1f} %)")

    section("3. Merging aligns on coordinates; the default is the union")
    coarse = anomaly.coarsen(lat=2, lon=2, boundary="trim").mean()
    print(f"  coarse grid {coarse.shape} with lat spacing "
          f"{float(coarse.lat[1] - coarse.lat[0]):.1f} deg")
    merged = xr.merge([ds[["anomaly"]], coarse.rename("anomaly_coarse")])
    nan_cells = int(merged.anomaly_coarse.isnull().sum())
    print(f"  xr.merge default join='outer' -> {dict(merged.sizes)}, "
          f"NaN in the coarse variable = {nan_cells:,} "
          f"({100 * nan_cells / merged.anomaly.size:.1f} % of the union grid)")
    inner = xr.merge([ds[["anomaly"]], coarse.rename("anomaly_coarse")], join="inner")
    print(f"  join='inner' -> {dict(inner.sizes)}, "
          f"NaN = {int(inner.anomaly_coarse.isnull().sum())}")
    print("  The union is the safe default for MERGING (no data is dropped, missing")
    print("  cells become NaN); xarray's default for ARITHMETIC is the intersection.")

    section("4. Area weighting: the single most common gridded-data error")
    w = np.cos(np.deg2rad(ds.lat))
    w.name = "cell_weight"
    print(f"  lat runs {float(lat[0]):.1f} .. {float(lat[-1]):.1f} deg, "
          f"so cos(lat) ranges {float(w.min()):.4f} .. {float(w.max()):.4f}")
    for name in ("anomaly", "elevation"):
        naive = float(ds[name].mean())
        weighted = float(ds[name].weighted(w).mean())
        print(f"  {name:9s}: naive grid mean = {naive:9.4f}, "
              f"cos(lat)-weighted = {weighted:9.4f}, "
              f"difference = {abs(naive - weighted):8.4f} "
              f"({100 * abs(naive - weighted) / abs(weighted):5.2f} %)")
    regional = ds.sel(lat=slice(30.0, 45.0), lon=slice(-120.0, -100.0))
    wr = np.cos(np.deg2rad(regional.lat))
    naive_r = float(regional.anomaly.mean())
    weighted_r = float(regional.anomaly.weighted(wr).mean())
    print(f"  same comparison inside a 15 x 20 deg box at 30-45 N:")
    print(f"    naive = {naive_r:.4f}, weighted = {weighted_r:.4f}, "
          f"difference = {abs(naive_r - weighted_r):.4f} "
          f"({100 * abs(naive_r - weighted_r) / abs(weighted_r):.2f} %)")
    print("  Weighting matters where the field has a meridional gradient and the")
    print("  rows cover a large range of cos(lat); it is nearly irrelevant inside")
    print("  a small box.")

    section("5. cos(lat) is a sphere weight; the Earth is an ellipsoid")
    a_wgs = 6378137.0                      # WGS 84 semi-major axis, m
    f_wgs = 1.0 / 298.257223563
    e2 = f_wgs * (2.0 - f_wgs)
    e = np.sqrt(e2)

    def band_area(dlam_deg: float, p1: float, p2: float) -> float:
        """Exact ellipsoidal area of a latitude band, m^2."""
        def capital(p):
            s = np.sin(p)
            return s / (1.0 - e2 * s ** 2) + (1.0 / (2.0 * e)) * np.log(
                (1.0 + e * s) / (1.0 - e * s))
        return (0.5 * np.deg2rad(dlam_deg) * a_wgs ** 2 * (1.0 - e2)
                * (capital(np.deg2rad(p2)) - capital(np.deg2rad(p1))))

    closed = 2.0 * np.pi * a_wgs ** 2 * (1.0 + (1.0 - e2) / e * np.arctanh(e))
    summed = band_area(360.0, -90.0, 90.0)
    print(f"  validation: sum of bands = {summed:.6e} m^2, closed form = "
          f"{closed:.6e} m^2, relative difference = "
          f"{abs(summed - closed) / closed:.2e}")
    print(f"  WGS 84 total surface = {closed / 1e12:.3f} x 10^6 km^2; sphere of "
          f"R = 6371 km = {4 * np.pi * 6371e3 ** 2 / 1e12:.3f} x 10^6 km^2")
    sphere = 4.0 * np.pi * 6371e3 ** 2
    print(f"  sphere-vs-ellipsoid total-area difference = "
          f"{100 * (sphere - closed) / closed:+.4f} %")
    print("  band      cos(lat_mid) rule     ellipsoid exact   cos-rule error")
    for lat_lo in (0.0, 30.0, 60.0, 75.0):
        lat_hi = lat_lo + 5.0
        dphi = np.deg2rad(lat_hi - lat_lo)
        mid = np.deg2rad(0.5 * (lat_lo + lat_hi))
        approx = np.cos(mid) * 2.0 * np.pi * 6371e3 ** 2 * dphi
        truth = band_area(360.0, lat_lo, lat_hi)
        print(f"  {lat_lo:4.0f}-{lat_hi:4.0f} N  {approx / 1e6:18.1f} km^2 "
              f"{truth / 1e6:16.1f} km^2 {100 * (approx - truth) / truth:13.3f} %")
    box_10 = abs(GEOD.geometry_area_perimeter(
        Polygon([(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]))[0])
    print(f"  caution: the 10 x 10 deg box bounded by GEODESICS has area "
          f"{box_10 / 1e6:.1f} km^2, but bounded by PARALLELS it is "
          f"{band_area(10.0, 0.0, 10.0) / 1e6:.1f} km^2 "
          f"({100 * (box_10 - band_area(10.0, 0.0, 10.0)) / band_area(10.0, 0.0, 10.0):+.3f} %)")
    print("  A geodesic between two points at the same latitude bows poleward, so")
    print("  'the area of a lat-lon box' depends on which boundary you mean.")

    section("6. Groupby: climatology and latitude bins")
    clim = ds.t2m.groupby("time.month").mean()
    print(f"  groupby('time.month').mean() -> {dict(clim.sizes)}")
    print(f"  samples per month: "
          f"{[int(v) for v in ds.t2m.groupby('time.month').count().isel(lat=0, lon=0).values]}")
    zonal = clim.mean(dim="lon")
    jan = float(zonal.sel(month=1, lat=43.5))
    jul = float(zonal.sel(month=7, lat=43.5))
    print(f"  zonal-mean temperature at 43.5 N (a grid row; 45.0 is not): "
          f"January {jan:.3f} degC, July {jul:.3f} degC, "
          f"difference {jul - jan:+.3f} K")
    print(f"  the imposed seasonal term is 4.0*cos(2*pi*i/12) K, so the expected")
    print(f"  half-amplitude is 4.000 K; measured {0.5 * (jan - jul):.3f} K")
    bins = np.arange(-90.0, 91.0, 15.0)
    binned = ds.anomaly.groupby_bins("lat", bins).mean()
    counts = ds.anomaly.groupby_bins("lat", bins).count().sum(dim=("lon",))
    print(f"  groupby_bins('lat', 15 deg) -> {binned.sizes['lat_bins']} bins; "
          f"first bin {binned.lat_bins.values[0]}, last {binned.lat_bins.values[-1]}")
    print(f"  cells per bin (summed over longitude) = "
          f"{[int(v) for v in counts.values]}")
    print(f"  bin edges stop at 90 while the grid stops at 88.5, so the last bin")
    print(f"  holds {int(counts.values[-1])} cells, the same as every other bin")
    eq = band_area(360.0, 0.0, 15.0)
    po = band_area(360.0, 75.0, 90.0)
    print(f"  but the 0-15 N band covers {eq / 1e6:.1f} km^2 and the 75-90 N band")
    print(f"  only {po / 1e6:.1f} km^2: equal cell counts, {eq / po:.2f}x different areas")

    section("7. weighted() is just a normalised sum")
    numerator = float((ds.anomaly * w).sum(dim=("lat", "lon")))
    denominator = float(w.sum(dim="lat")) * ds.sizes["lon"]
    manual = numerator / denominator
    api = float(ds.anomaly.weighted(w).mean())
    print(f"  numerator   sum(w*x) = {numerator:.6f} (mGal x dimensionless)")
    print(f"  denominator sum(w)   = {denominator:.6f} (dimensionless: {ds.sizes['lat']} "
          f"rows x {ds.sizes['lon']} columns)")
    print(f"  manual sum(w*x)/sum(w) = {manual:.10f} mGal")
    print(f"  ds.weighted(w).mean()  = {api:.10f} mGal")
    print(f"  difference = {abs(manual - api):.3e} mGal -- the same computation")
    print("  Note the units: the weight is dimensionless, so the result is in mGal")
    print("  only because x is; weighting never changes the units of the mean.")

    section("8. Rolling and shifting create NaN where you least expect it")
    series = ds.t2m.mean(dim=("lat", "lon"))
    rolled = series.rolling(time=12, center=True).mean()
    print(f"  monthly series: {series.sizes['time']} steps; "
          f"rolling(12, center=True) -> {int(rolled.isnull().sum())} NaN ends")
    print(f"  mean of the rolled series = {float(rolled.mean()):.4f} degC vs "
          f"unrolled {float(series.mean()):.4f} degC "
          f"(difference {abs(float(rolled.mean()) - float(series.mean())):.4f} K)")
    shifted = series.shift(time=1)
    print(f"  shift(time=1) -> {int(shifted.isnull().sum())} NaN, and it moves the "
          f"series in the LABEL direction, so you must decide the sign yourself")
    print(f"  correlation at lag +1 month = "
          f"{float(xr.corr(series, shifted, dim='time')):.4f}")

    section("9. stack and unstack: reshaping labeled data")
    stacked = ds.anomaly.stack(cell=("lat", "lon"))
    print(f"  stack(('lat','lon') -> 'cell') -> {stacked.shape} with a "
          f"MultiIndex of {stacked.indexes['cell'].nlevels} levels")
    print(f"  first label {stacked.cell.values[0]}, last {stacked.cell.values[-1]}")
    back = stacked.unstack("cell")
    print(f"  unstack returns {back.shape} and identical values: "
          f"{bool(np.allclose(back.values, ds.anomaly.values))} "
          f"(row order restored because unstack sorts the index)")

    section("10. Round trip through a NetCDF file")
    path = WORK / "dataset.nc"
    ds.to_netcdf(path)
    small = WORK / "dataset_f32.nc"
    ds.to_netcdf(small, encoding={name: {"dtype": "float32"} for name in ds.data_vars})
    with xr.open_dataset(path) as reopened:
        print(f"  default write: {path.stat().st_size:,} bytes; "
              f"variables = {list(reopened.data_vars)}")
        print(f"  global attrs preserved: {reopened.attrs}")
        print(f"  t2m attrs preserved: {reopened.t2m.attrs}")
        print(f"  time decoded to {reopened.time.dtype} "
              f"(the file stores numbers plus a 'days since ...' unit)")
        print(f"  dtypes after the round trip: anomaly {reopened.anomaly.dtype}, "
              f"t2m {reopened.t2m.dtype}")
        same = float(np.abs(reopened.anomaly.values - ds.anomaly.values).max())
        print(f"  max difference after the round trip = {same:.3e} mGal")
    with xr.open_dataset(small) as r32:
        diff32 = float(np.abs(r32.anomaly.values - ds.anomaly.values).max())
        relative = diff32 / float(ds.anomaly.max())
        print(f"  with encoding dtype='float32': {small.stat().st_size:,} bytes "
              f"({path.stat().st_size / small.stat().st_size:.2f}x smaller)")
        print(f"    dtype {r32.anomaly.dtype}; max difference = {diff32:.3e} mGal = "
              f"{relative:.2e} relative")
        print(f"    float32 carries about {-np.log10(relative) / np.log10(2):.0f} bits "
              f"of relative precision, i.e. 7 significant decimal digits")
    print("  xarray writes the dtype you give it: float64 unless you ask for less.")
    print("  Asking for float32 halves the file and costs 7-digit precision.")


if __name__ == "__main__":
    main()
