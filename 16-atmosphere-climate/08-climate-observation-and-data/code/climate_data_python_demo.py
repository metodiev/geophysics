#!/usr/bin/env python3
"""Analysing climate data in Python: building a gridded dataset with xarray,
computing area-weighted versus unweighted means, climatologies and anomalies,
handling resampling labels and missing data, and coarse-graining conservatively.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_data_python_demo.py

Everything is SYNTHETIC.  The gridded field below is generated from a chosen
formula.  No real dataset, reanalysis, station or published value is used.

Contents
--------
1. Build a synthetic gridded field with xarray (time, lat, lon).
2. Area weighting: cos(lat) weights versus a plain mean.
3. Monthly climatology, anomalies and the seasonal cycle.
4. Resampling and rolling means, and the label convention.
5. Missing data: what happens if the weights are not renormalised.
6. Conservative coarse-graining, and the cost of doing it the naive way.
7. The xarray/CDO operator correspondence you will meet in practice.
"""

import numpy as np
import xarray as xr

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC grid (chosen, not measured) ----------------------------------
LAT = np.arange(-85.0, 86.0, 10.0)          # 18 latitudes
LON = np.arange(0.0, 360.0, 10.0)           # 36 longitudes
N_YEARS = 24
TIME = xr.date_range("2000-01-01", periods=N_YEARS * 12, freq="MS")
BASELINE_K = 288.0                          # K, a chosen mean level
TREND_K_PER_YR = 0.030                      # K/yr, global mean warming
SEASONAL_AMPLITUDE_K = 6.0                  # K, chosen seasonal amplitude
NOISE_K = 0.8                               # K, grid-point monthly noise
COARSE_FACTOR = 3                           # 3 x 3 blocks for coarse-graining


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def build_dataset():
    """A synthetic gridded near-surface temperature field."""
    t_year = (np.arange(TIME.size) // 12).astype(float)
    lat3 = LAT[:, None, None]
    mon3 = (np.arange(TIME.size) % 12)[None, None, :]
    # polar amplification: the warming pattern grows with |latitude|
    pattern = 1.0 + 1.5 * (np.abs(lat3) / 90.0) ** 2
    trend = TREND_K_PER_YR * t_year[None, None, :] * pattern
    seasonal = SEASONAL_AMPLITUDE_K * np.cos(
        2.0 * np.pi * (mon3 - 6.0) / 12.0) * (np.abs(lat3) / 90.0)
    noise = NOISE_K * RNG.standard_normal((LAT.size, LON.size, TIME.size))
    field = BASELINE_K - 30.0 * (np.abs(lat3) / 90.0) ** 2 + trend + seasonal \
        + noise
    return xr.DataArray(
        field,
        dims=("lat", "lon", "time"),
        coords={"lat": LAT, "lon": LON, "time": TIME},
        name="tas",
        attrs={"units": "K", "source": "SYNTHETIC teaching field"},
    )


def area_weights(da):
    """cos(lat) weights that broadcast over (lat, lon)."""
    w = np.cos(np.deg2rad(da["lat"]))
    return w.broadcast_like(da.isel(time=0, drop=True))


def main():
    section("1. A synthetic gridded field with xarray")
    da = build_dataset()
    print(f"  dims {da.dims}, shape {da.shape}, units {da.attrs['units']}")
    print(f"  lat {float(LAT[0]):.0f} to {float(LAT[-1]):.0f} deg, "
          f"{LAT.size} points; lon {LON.size} points; {TIME.size} months")
    print(f"  time coordinate: {TIME[0].date()} to {TIME[-1].date()}")
    print(f"  the field is a chosen formula: baseline - 30 (|lat|/90)^2 + trend")
    print(f"  + seasonal + noise; latitude labels are POINT coordinates, not")
    print(f"  cell bounds, which matters for the weighting below.")

    section("2. Area weighting: cos(lat) matters")
    w = area_weights(da)
    ts_plain = da.mean(dim=("lat", "lon"))
    ts_weighted = da.weighted(w).mean(dim=("lat", "lon"))
    print("  global-mean temperature (first month):")
    print(f"    plain mean over grid points : {float(ts_plain[0]):.4f} K")
    print(f"    cos(lat)-weighted mean      : {float(ts_weighted[0]):.4f} K")
    print(f"    difference (plain - weighted): "
          f"{float(ts_plain[0] - ts_weighted[0]):+.4f} K")
    trend_plain = float(np.polyfit(np.arange(TIME.size) / 12.0, ts_plain, 1)[0])
    trend_w = float(np.polyfit(np.arange(TIME.size) / 12.0, ts_weighted, 1)[0])
    print(f"  linear trend, plain mean      : {trend_plain:+.4f} K/yr")
    print(f"  linear trend, weighted mean   : {trend_w:+.4f} K/yr")
    print(f"  trend difference              : "
          f"{trend_plain - trend_w:+.4f} K/yr "
          f"({100 * (trend_plain - trend_w) / trend_w:+.1f}%)")
    print("  The field cools toward the poles and warms faster there, so")
    print("  weighting every grid point equally gives each high-latitude point")
    print("  far too much influence.  Multiplying by cos(lat) corrects the")
    print("  meridian convergence that the regular grid hides.")

    section("3. Climatology, anomalies and the seasonal cycle")
    clim = da.groupby("time.month").mean("time")
    anom = da.groupby("time.month") - clim
    print(f"  climatology shape {clim.shape} (12 months), anomaly shape "
          f"{anom.shape}")
    print("  seasonal cycle, area-weighted global mean, by month (K):")
    for m in range(0, 12, 3):
        val = float(clim.isel(month=m).weighted(w).mean())
        print(f"    month {m + 1:2d}: {val:.3f} K")
    gmean = clim.weighted(w).mean("lat").mean("lon")
    amp = float(gmean.max() - gmean.min())
    print(f"  area-weighted range of the global mean: {amp:.3f} K")
    print(f"  (the local seasonal amplitude is {SEASONAL_AMPLITUDE_K:.1f} K at the")
    print(f"  poles and shrinks toward the equator, so the global-mean range is")
    print(f"  much smaller than any local amplitude)")
    print(f"  standard deviation of the anomaly field: {float(anom.std()):.3f} K")
    print("  An anomaly is defined relative to a stated climatology.  Change")
    print("  the reference period and every anomaly changes, although")
    print("  differences of anomalies do not.")

    section("4. Resampling and rolling means: the label convention")
    yearly_end = ts_weighted.resample(time="YE").mean()
    yearly_start = ts_weighted.resample(time="YS").mean()
    same = bool(np.allclose(yearly_end.values, yearly_start.values))
    label_days = int((yearly_end["time"].values[0]
                      - yearly_start["time"].values[0]) / np.timedelta64(1, "D"))
    print(f"  resample('YE'): {len(yearly_end)} annual means, first label "
          f"{str(yearly_end['time'].values[0])[:10]}")
    print(f"  resample('YS'): {len(yearly_start)} annual means, first label "
          f"{str(yearly_start['time'].values[0])[:10]}")
    print(f"  the VALUES are identical ({same}); the LABELS differ by "
          f"{label_days} days.")
    print("  because this record starts in January, both bin whole years.  If a")
    print("  series starts mid-year, 'YE' produces a partial first bin:")
    ts_july = ts_weighted.sel(time=slice("2000-07-01", None))
    counts = ts_july.resample(time="YE").count()
    print(f"    July-start series: first 'YE' bin contains "
          f"{int(counts.values[0])} months, not 12")
    rolled = ts_weighted.rolling(time=12, center=True).mean()
    print(f"  rolling 12-month mean: {int(rolled.notnull().sum())} of "
          f"{TIME.size} values are valid")
    valid = rolled.dropna("time")["time"].values
    print(f"  first and last valid labels: {str(valid[0])[:10]} .. "
          f"{str(valid[-1])[:10]}")
    print("  a centred rolling mean loses 6 values at each end.  Always state the")
    print("  label convention: a 12-month mean labelled at the year START")
    print("  describes the year that FOLLOWS the label.")

    section("5. Missing data and weight renormalisation")
    masked = da.where(~((da.lat > 60) & (da.time.dt.year.isin([2005, 2006]))))
    ref = 60                     # a time step inside the masked period
    n_missing = int(np.isnan(masked.isel(time=ref)).sum())
    plain_full = float(da.isel(time=ref).mean())
    wmean_full = float(da.isel(time=ref).weighted(w).mean())
    plain_gap = float(masked.isel(time=ref).mean(skipna=True))
    wmean_gap = float(masked.isel(time=ref).weighted(w).mean())
    print(f"  masked every point north of 60 N for two years "
          f"({n_missing} points missing at one time step)")
    print("  quantity                       complete field   with the gap")
    print(f"  plain mean over grid points    {plain_full:14.3f}   {plain_gap:12.3f}")
    print(f"  cos(lat)-weighted mean         {wmean_full:14.3f}   {wmean_gap:12.3f}")
    print(f"  error of the plain mean        {0.0:14.3f}   "
          f"{plain_gap - plain_full:+12.3f} K")
    print(f"  error of the weighted mean     {0.0:14.3f}   "
          f"{wmean_gap - wmean_full:+12.3f} K")
    print("  weighted() renormalises the weights over the valid points, so the")
    print("  weighted mean remains an area-weighted mean of the available area;")
    print("  the plain skipna mean instead re-weights the grid by how many points")
    print("  happen to be present.  If the gap is systematic -- a satellite whose")
    print("  coverage changes -- the second error changes with time and becomes a")
    print("  trend.  Report coverage with every mean.")

    section("6. Conservative coarse-graining")
    nlat = LAT.size // COARSE_FACTOR
    nlon = LON.size // COARSE_FACTOR
    field0 = da.isel(time=0)
    block = field0.coarsen(lat=COARSE_FACTOR, lon=COARSE_FACTOR,
                           boundary="trim").mean()
    wsum = w.coarsen(lat=COARSE_FACTOR, lon=COARSE_FACTOR,
                     boundary="trim").sum()
    num = (field0 * w).coarsen(lat=COARSE_FACTOR, lon=COARSE_FACTOR,
                               boundary="trim").sum()
    cons = num / wsum
    print(f"  coarse-grained from {LAT.size}x{LON.size} to {nlat}x{nlon} "
          f"({COARSE_FACTOR}x{COARSE_FACTOR} blocks)")
    print("  block means in one column (K):")
    print("    latitude       simple mean   cos(lat)-weighted   difference")
    for j in range(4):
        idx = nlat - 1 - j
        simple = float(block.isel(lat=idx, lon=0))
        consv = float(cons.isel(lat=idx, lon=0))
        lat_c = float(block["lat"][idx])
        print(f"    {lat_c:+7.0f} deg   {simple:11.3f}   {consv:17.3f}   "
              f"{simple - consv:+10.3f}")
    diff = float(abs(block - cons).mean())
    print(f"  mean absolute difference between the two coarse-grainings: "
          f"{diff:.3f} K")
    print("  A simple cell average is not conservative on a latitude-longitude")
    print("  grid: the cells cover different areas, so a plain block mean")
    print("  over-weights the small high-latitude cells.  A conservative")
    print("  regridder weights each contributing cell by its area.")

    section("7. The xarray / CDO operator correspondence")
    print("  The command-line and Python worlds use the same operations:")
    print("    cdo fldmean        <-> da.weighted(coslat).mean(['lat','lon'])")
    print("    cdo timmean        <-> da.mean('time')")
    print("    cdo monmean        <-> da.groupby('time.month').mean('time')")
    print("    cdo ymonmean       <-> climatology (12 months)")
    print("    cdo sub/timmean    <-> anomaly = da.groupby('time.month') - clim")
    print("    cdo remapcon       <-> conservative regridding (area-weighted)")
    print("    cdo setmissval     <-> da.where(mask) and explicit renormalisation")
    print("  Three habits prevent most mistakes: (i) check the coordinate")
    print("  names, units and calendar before anything else; (ii) weight by")
    print("  cos(lat) for any zonal or global mean; (iii) write the reference")
    print("  period and the label convention next to every anomaly or mean.")
    print("  All numbers above are SYNTHETIC.")


if __name__ == "__main__":
    main()
