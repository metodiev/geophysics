"""xarray DataArray: named dimensions, label-based indexing, alignment.

All data are SYNTHETIC (a Gaussian gravity anomaly plus a seeded perturbation on
a regular lon/lat grid). Nothing is downloaded.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python xarray_dataarray_demo.py
Requires: numpy, xarray.
"""

from __future__ import annotations

import numpy as np
import xarray as xr

RNG = np.random.default_rng(20260802)
AMP, LON0, LAT0, SX, SY = 28.0, -110.0, 37.5, 1.4, 0.9


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def analytic(lon, lat):
    """SYNTHETIC Gaussian anomaly, mGal, defined everywhere in the plane."""
    return AMP * np.exp(-(((lon - LON0) / SX) ** 2 + ((lat - LAT0) / SY) ** 2))


def make(lon, lat, seed_scale=1.0, dtype=np.float64):
    lon2d, lat2d = np.meshgrid(lon, lat)
    g = analytic(lon2d, lat2d) + seed_scale * RNG.normal(0.0, 0.2, lon2d.shape)
    return xr.DataArray(
        g.astype(np.float64),
        dims=("lat", "lon"),
        coords={"lat": np.asarray(lat, dtype=dtype), "lon": np.asarray(lon, dtype=dtype)},
        name="anomaly",
        attrs={"units": "mGal", "long_name": "SYNTHETIC gravity anomaly",
               "source": "synthetic_gaussian + seeded noise"},
    )


def main() -> None:
    lon = np.arange(-120.0, -99.999, 0.125)
    lat = np.arange(30.0, 45.001, 0.125)
    da = make(lon, lat)

    section("1. A DataArray is an ndarray plus named axes plus labels")
    print(f"  dims      = {da.dims}")
    print(f"  shape     = {da.shape}")
    print(f"  sizes     = {dict(da.sizes)}")
    print(f"  dtype     = {da.dtype}")
    print(f"  name      = {da.name!r}")
    print(f"  attrs     = {da.attrs}")
    print(f"  nbytes    = {da.nbytes:,} bytes")
    print(f"  lon[0], lon[-1], spacing = {float(da.lon[0]):.3f}, "
          f"{float(da.lon[-1]):.3f}, {float(da.lon[1] - da.lon[0]):.4f} deg")
    print(f"  lat[0], lat[-1], spacing = {float(da.lat[0]):.3f}, "
          f"{float(da.lat[-1]):.3f}, {float(da.lat[1] - da.lat[0]):.4f} deg")
    print(f"  min, max  = {float(da.min()):.4f}, {float(da.max()):.4f} mGal")

    section("2. Labels are an address: .sel versus .isel")
    print(f"  positional da.isel(lon=56)  lon label = {float(da.isel(lon=56).lon):.4f} deg")
    point = da.sel(lon=-113.0, lat=37.5)
    print(f"  label      da.sel(lon=-113.0, lat=37.5) value = {point.item():.4f} mGal")
    print(f"  the two address the SAME cell: "
          f"{float(da.isel(lon=56, lat=60)) == point.item()}")
    box = da.sel(lon=slice(-113.0, -108.0), lat=slice(35.0, 40.0))
    print(f"  slice -113..-108 lon, 35..40 lat -> shape {box.shape} "
          f"({box.size:,} of {da.size:,} values, "
          f"{100 * box.size / da.size:.1f} %)")
    print(f"  box mean = {float(box.mean()):.4f} mGal")

    section("3. Coordinates of different dtype do not line up")
    lon_f = np.arange(-120.0, -99.9999, 0.1)      # 0.1 deg: not binary-exact
    lon_g = lon_f.astype(np.float32)
    shared = int(np.intersect1d(lon_f, lon_g.astype(np.float64)).size)
    shift = float(np.abs(lon_g.astype(np.float64) - lon_f).max())
    print(f"  {lon_f.size} labels at 0.1 deg spacing, stored float64 vs float32")
    print(f"  labels that still match after float32 -> float64: {shared}")
    print(f"  largest label shift = {shift:.3e} deg = {shift * 111_320:.3f} m")
    a64 = make(lon_f, lat, seed_scale=0.0)
    a32 = make(lon_g, lat.astype(np.float32), seed_scale=1.0, dtype=np.float32)
    print(f"  a64 = {a64.shape}, a32 = {a32.shape}")
    summed = a64 + a32
    print(f"  a64 + a32  ->  shape {summed.shape} with no error and no NaN")
    print("  The default arithmetic join is the INTERSECTION of the labels, and")
    print("  practically none of them intersect. xr.align fixes the intent:")
    pair = xr.align(a64, a32, join="override")
    combined = pair[0] + pair[1]
    print(f"  xr.align(..., join='override') then add -> shape {combined.shape}: "
          f"the float32 labels are mapped onto the float64 labels")
    print(f"  the two fields differ by up to "
          f"{float(np.abs(a64.values - a32.values.astype(np.float64)).max()):.4f} "
          f"mGal (different seeded noise); before aligning, only 1 column matched")
    print(f"  in-file .sel still works because the key is cast to float32: "
          f"a32.sel(lon=-110.0, lat=37.5) = "
          f"{float(a32.sel(lon=-110.0, lat=37.5).item()):.4f} mGal")

    section("4. Arithmetic aligns by LABEL, and the default is the INTERSECTION")
    half = make(lon + 0.0625, lat, seed_scale=0.0)      # shifted half a cell
    print(f"  da    lon: {float(da.lon[0]):.4f} .. {float(da.lon[-1]):.4f} "
          f"({da.sizes['lon']} labels)")
    print(f"  half  lon: {float(half.lon[0]):.4f} .. {float(half.lon[-1]):.4f} "
          f"({half.sizes['lon']} labels)")
    empty = da + half
    print(f"  da + half (default join='inner') -> shape {empty.shape}, "
          f"size {empty.size}: an EMPTY result, silently")
    uni, _ = xr.align(da, half, join="outer")
    print(f"  xr.align(da, half, join='outer') -> shape {uni.shape} "
          f"(161 + 161 = {161 + 161} labels: no label is shared)")
    pair = xr.align(da, half, join="outer")
    summed_outer = pair[0] + pair[1]
    n_nan = int(summed_outer.isnull().sum())
    print(f"  outer sum NaN count = {n_nan:,} "
          f"({100 * n_nan / summed_outer.size:.1f} % of the result)")
    shifted = make(lon[10:], lat, seed_scale=0.0)      # integer 10-cell shift
    inner_pair = da + shifted
    outer_pair = xr.align(da, shifted, join="outer")
    outer_sum = outer_pair[0] + outer_pair[1]
    print(f"  integer 10-cell shift: inner -> {inner_pair.shape} "
          f"({int(inner_pair.isnull().sum())} NaN), outer -> {outer_sum.shape} "
          f"({int(outer_sum.isnull().sum()):,} NaN, "
          f"{100 * int(outer_sum.isnull().sum()) / outer_sum.size:.1f} % of the result)")
    print("  The union keeps every left label, so the extra 10 columns are all-NaN.")
    try:
        xr.align(da, shifted, join="exact")
    except ValueError as exc:
        print(f"  join='exact' raises {type(exc).__name__} instead of guessing")

    section("5. Broadcasting follows the dimension names, not the shapes")
    profile = xr.DataArray(np.linspace(1.0, 1.2, lat.size), dims=("lat",),
                           coords={"lat": da.lat})
    scaled = da * profile
    print(f"  (lat,lon) * (lat,) -> {scaled.shape}")
    print(f"  row factors: {float(profile[0]):.4f} (30 N) .. "
          f"{float(profile[-1]):.4f} (45 N)")
    ratio = float(scaled.sel(lat=45.0).mean() / da.sel(lat=45.0).mean())
    print(f"  measured scaling at 45 N = {ratio:.4f} (expected 1.2000)")
    grad = da.differentiate("lat") * profile
    print(f"  differentiate('lat') keeps the same coords: {grad.dims}, "
          f"attrs = {grad.attrs}")

    section("6. Masking with .where, and what drop=True does")
    mask = da > 5.0
    print(f"  cells above 5 mGal = {int(mask.sum()):,} "
          f"({100 * int(mask.sum()) / da.size:.1f} %)")
    kept = da.where(mask, drop=True)
    nan_version = da.where(mask)
    print(f"  da.where(mask)          : shape {nan_version.shape}, "
          f"stored values {nan_version.size:,}, NaN {int(nan_version.isnull().sum()):,}")
    print(f"  da.where(mask, drop=True): shape {kept.shape}, "
          f"stored values {kept.size:,}")
    print(f"  both give the same mean, {float(kept.mean()):.4f} mGal, because drop")
    print("  removes only rows and columns that became entirely NaN.")
    print(f"  memory kept for the mask: {nan_version.nbytes:,} bytes vs "
          f"{kept.nbytes:,} bytes ({nan_version.nbytes / kept.nbytes:.1f}x)")

    section("7. Interpolation: how much does regridding cost, measured?")
    lon_c = np.arange(-120.0, -99.999, 0.25)      # coarse: 0.25 deg
    lat_c = np.arange(30.0, 45.001, 0.25)
    coarse = make(lon_c, lat_c, seed_scale=0.0)   # no noise: compare to analytic
    truth = xr.DataArray(analytic(*np.meshgrid(lon, lat)), dims=("lat", "lon"),
                         coords={"lat": da.lat, "lon": da.lon})
    for method in ("linear", "cubic"):
        fine = coarse.interp(lat=lat, lon=lon, method=method)
        err = np.abs(fine - truth)
        print(f"  {method:7s} regrid 0.25 deg -> 0.125 deg: "
              f"max error = {float(err.max()):.4f} mGal, "
              f"rms error = {float(np.sqrt((err ** 2).mean())):.4f} mGal, "
              f"peak value = {float(truth.max()):.3f} mGal")
    print("  On a smooth field sampled at twice the output spacing, cubic beats")
    print("  linear by a wide margin. That is a property of SMOOTH data:")
    step_lon = np.arange(-103.0, -97.0, 0.25)
    step_lat = np.arange(35.0, 38.0, 0.25)
    scarp = xr.DataArray(np.where(np.meshgrid(step_lon, step_lat)[0] < -100.0, 0.0, 100.0),
                         dims=("lat", "lon"),
                         coords={"lat": step_lat, "lon": step_lon})
    fine_lon = np.arange(-103.0, -99.999, 0.05)
    fine_lat = np.arange(35.0, 37.999, 0.05)
    for method in ("linear", "nearest", "cubic"):
        fine = scarp.interp(lat=fine_lat, lon=fine_lon, method=method)
        print(f"  {method:7s} across a 100 m step: min = {float(fine.min()):.2f} m, "
              f"max = {float(fine.max()):.2f} m "
              f"(overshoot = {max(0.0, float(fine.max()) - 100.0) + max(0.0, -float(fine.min())):.2f} m)")

    section("8. Time labels: resample and groupby")
    nt = 60
    t = np.array([np.datetime64("2000-01-01") + np.timedelta64(30 * i, "D")
                  for i in range(nt)])
    imposed = 1.5 * np.cos(2 * np.pi * np.arange(nt) / 12.0 + 0.4)
    series = xr.DataArray(
        imposed + 0.02 * np.arange(nt),
        dims=("time",), coords={"time": t}, name="level_m", attrs={"units": "m"})
    print(f"  {nt} samples, {t[0]} .. {t[-1]}, dtype {series.time.dtype}")
    yearly = series.resample(time="YE").mean()
    print(f"  resample(time='YE').mean() -> {yearly.sizes['time']} annual means; "
          f"first = {float(yearly[0]):.3f} m, last = {float(yearly[-1]):.3f} m")
    counts = series.groupby("time.month").count()
    monthly = series.groupby("time.month").mean()
    print(f"  groupby('time.month') -> {monthly.sizes['month']} groups, "
          f"samples per group {[int(v) for v in counts.values]}")
    print(f"  the imposed trend is exactly +0.02000 m per sample; a straight")
    print(f"  least-squares fit returns {float(np.polyfit(np.arange(nt), series.values, 1)[0]):.5f} "
          f"m/sample because the seasonal cosine is not removed first")
    print(f"  monthly means (composited over 5 years) range "
          f"{float(monthly.min()):.3f} .. {float(monthly.max()):.3f} m")

    section("9. Attributes: preserved, but never checked")
    print(f"  xr.get_options()['keep_attrs'] = {xr.get_options()['keep_attrs']}")
    print(f"  da.attrs before arithmetic: {sorted(da.attrs)}")
    plain = da * 2.0
    print(f"  (da * 2.0).attrs: {sorted(plain.attrs)}  <- units kept, magnitudes "
          f"doubled")
    with xr.set_options(keep_attrs=False):
        dropped = da * 2.0
    print(f"  with keep_attrs=False: {sorted(dropped.attrs)}")
    print(f"  (da * 1e6).attrs still claims {plain.attrs['units']!r} while the "
          f"values are 1e6 times larger:")
    print(f"    max = {float((da * 1e6).max()):.3e} labelled "
          f"{plain.attrs['units']!r}")
    print("  Attributes are metadata the library copies; nothing checks them.")

    section("10. .values is the buffer, not a copy")
    buf = da.values
    before = float(buf[60, 60])
    buf[60, 60] = -777.0
    print(f"  changed buf[60,60]: {before:.4f} -> "
          f"{float(da.values[60, 60]):.4f} mGal (the DataArray changed too)")
    echo = da.copy(deep=True)
    echo.values[60, 60] = 123.0
    print(f"  after copy(deep=True) and an edit: original = "
          f"{float(da.values[60, 60]):.4f}, copy = {float(echo.values[60, 60]):.4f}")
    print(f"  memory: da.nbytes = {da.nbytes:,} bytes for {da.size:,} values "
          f"({da.dtype.itemsize} bytes each)")


if __name__ == "__main__":
    main()
