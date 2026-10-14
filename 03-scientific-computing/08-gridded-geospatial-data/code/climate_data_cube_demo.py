"""Case study: a synthetic climate data cube analysed end to end.

The cube is SYNTHETIC: an imposed linear warming trend, a seasonal cycle, a
meridional profile and a propagating ENSO-like oscillation, all generated with
a fixed seed. Nothing is downloaded and no real dataset is used. The point of
the demo is that the imposed numbers are known, so every analysis step can be
checked against ground truth.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_data_cube_demo.py
Requires: numpy, xarray.
"""

from __future__ import annotations

import numpy as np
import xarray as xr

RNG = np.random.default_rng(20260806)

N_YEAR = 40
N_LAT, N_LON = 36, 72
TREND_K_PER_DECADE = 0.20          # imposed linear trend
SEASONAL_K = 3.0                   # imposed seasonal amplitude
ENSO_K = 1.4                       # imposed oscillation amplitude
BASE_URL = ("https://cds.climate.copernicus.eu  (Copernicus Climate Data Store, "
            "ERA5 monthly reanalysis)")


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def build_cube() -> tuple[xr.DataArray, np.ndarray]:
    """Synthetic monthly SST-like field, K, plus its ENSO index."""
    lat = np.linspace(-87.5, 87.5, N_LAT)
    lon = np.linspace(-177.5, 177.5, N_LON)
    time = xr.date_range("1985-01-01", periods=12 * N_YEAR, freq="MS")
    months = np.arange(12 * N_YEAR)
    seasonal = SEASONAL_K * np.cos(2 * np.pi * months / 12.0)
    warming = TREND_K_PER_DECADE * (months / 120.0)
    enso = np.sin(2 * np.pi * months / 48.0) * np.exp(-((months % 240 - 120) / 60.0) ** 2)
    lat_profile = 28.0 - 0.30 * np.abs(lat) - 0.004 * lat ** 2
    # Broadcasting aligns trailing axes, so each factor is given an explicit
    # (time, lat, lon) shape instead of relying on (480,) * (1, 36, 1).
    pattern = np.cos(np.deg2rad(lat) * 2.0)[None, :, None]      # (1, 36, 1)
    enso_term = ENSO_K * enso[:, None, None] * pattern          # (480, 36, 1)
    noise = RNG.normal(0.0, 0.35, (12 * N_YEAR, N_LAT, N_LON))
    field = (lat_profile[None, :, None] + seasonal[:, None, None]
             + warming[:, None, None] + enso_term + noise)
    da = xr.DataArray(field, dims=("time", "lat", "lon"),
                      coords={"time": time, "lat": lat, "lon": lon}, name="sst",
                      attrs={"units": "K", "long_name": "SYNTHETIC sea surface "
                             "temperature", "source": "seeded generator"})
    return da, enso


def area_weights(da: xr.DataArray) -> xr.DataArray:
    """cos(lat) weights normalised so that the global mean is a proper mean."""
    w = np.cos(np.deg2rad(da.lat))
    return w / w.mean()


def global_mean(x: xr.DataArray) -> xr.DataArray:
    """Area-weighted global mean over lat and lon."""
    return x.weighted(area_weights(x)).mean(dim=("lat", "lon"))


def main() -> None:
    sst, enso_index = build_cube()

    section("1. The cube, and the ground truth it encodes")
    print(f"  dims = {dict(sst.sizes)}, dtype = {sst.dtype}, "
          f"nbytes = {sst.nbytes:,}")
    print(f"  time: {sst.time.values[0]} .. {sst.time.values[-1]} "
          f"({sst.sizes['time']} monthly steps)")
    print(f"  lat: {float(sst.lat[0]):.1f} .. {float(sst.lat[-1]):.1f} deg, "
          f"spacing {float(sst.lat[1] - sst.lat[0]):.1f} deg")
    print(f"  lon: {float(sst.lon[0]):.1f} .. {float(sst.lon[-1]):.1f} deg, "
          f"spacing {float(sst.lon[1] - sst.lon[0]):.1f} deg")
    print(f"  values: {float(sst.min()):.2f} .. {float(sst.max()):.2f} K")
    print(f"  IMPOSED: trend {TREND_K_PER_DECADE:.2f} K/decade, seasonal "
          f"amplitude {SEASONAL_K:.2f} K, ENSO amplitude {ENSO_K:.2f} K")
    print(f"  grid cells = {N_LAT * N_LON:,}; grid spacing is UNIFORM in"
          f" longitude and latitude, so cells are NOT equal-area")

    section("2. Climatology and anomalies relative to a baseline period")
    base = sst.sel(time=slice("1985-01-01", "2014-12-31"))
    clim = base.groupby("time.month").mean()
    print(f"  baseline 1985-2014 has {base.sizes['time']} months; climatology "
          f"{dict(clim.sizes)}")
    print(f"  global mean over the baseline = "
          f"{float(global_mean(base).mean()):.4f} K")
    anom = sst.groupby("time.month") - clim
    print(f"  monthly anomalies: shape {anom.shape}, mean over the WHOLE record = "
          f"{float(anom.mean()):+.4f} K (positive because of the trend)")
    base_anom = anom.sel(time=slice("1985-01-01", "2014-12-31"))
    print(f"  baseline anomaly mean = {float(base_anom.mean()):+.6f} K; "
          f"std = {float(base_anom.std()):.4f} K")
    print(f"  the seasonal cycle is removed first, so the residual std is the")
    print(f"  combined noise plus the ENSO signal, not the seasonal swing")

    section("3. Global mean time series: weighting changes the trend")
    naive = anom.mean(dim=("lat", "lon")).resample(time="YE").mean()
    weighted = global_mean(anom).resample(time="YE").mean()
    print(f"  annual means: naive grid mean vs cos(lat)-weighted mean")
    print(f"    naive    first/last = {float(naive[0]):+.4f} / "
          f"{float(naive[-1]):+.4f} K")
    print(f"    weighted first/last = {float(weighted[0]):+.4f} / "
          f"{float(weighted[-1]):+.4f} K")

    def trend_per_decade(series: xr.DataArray):
        """Least-squares trend in K/decade from the real time coordinate."""
        x = ((series.time.values - series.time.values[0])
             / np.timedelta64(1, "D")).astype(float) / 365.2425
        slope, intercept = np.polyfit(x, series.values, 1)
        resid = series.values - (slope * x + intercept)
        return float(slope * 10.0), float(np.sqrt(np.mean(resid ** 2)))

    slope_n, rms_n = trend_per_decade(naive)
    slope_w, rms_w = trend_per_decade(weighted)
    print(f"    naive    trend = {slope_n:+.4f} K/decade (residual rms "
          f"{rms_n * 1000:.2f} mK)")
    print(f"    weighted trend = {slope_w:+.4f} K/decade (residual rms "
          f"{rms_w * 1000:.2f} mK)")
    print(f"  IMPOSED trend = {TREND_K_PER_DECADE:+.4f} K/decade")
    print(f"    naive error    = {slope_n - TREND_K_PER_DECADE:+.4f} K/decade "
          f"({(slope_n - TREND_K_PER_DECADE) / TREND_K_PER_DECADE * 100:+.2f} %)")
    print(f"    weighted error = {slope_w - TREND_K_PER_DECADE:+.4f} K/decade "
          f"({(slope_w - TREND_K_PER_DECADE) / TREND_K_PER_DECADE * 100:+.2f} %)")
    print("  Both recover the imposed rate, and the 40-year record is what buys")
    print("  that; the two weightings differ by "
          f"{abs(slope_n - slope_w) * 1000:.2f} mK/decade here.")
    print("  Their residual rms differs by two orders of magnitude because the")
    print("  imposed oscillation has a cos(2*lat) pattern, which cancels almost")
    print("  exactly in an unweighted sum over uniformly spaced latitude rows but")
    print("  not under cos(lat) weighting. The cancellation is a coincidence of")
    print("  this pattern, not a property of area means.")

    section("4. The same trend on a raw (undeseasonalised) series")
    raw = global_mean(sst).resample(time="YE").mean()
    slope_raw, rms_raw = trend_per_decade(raw)
    print(f"  annual means of the RAW field: first = {float(raw[0]):.3f} K, "
          f"last = {float(raw[-1]):.3f} K")
    print(f"  every annual mean averages 12 months exactly, so the seasonal")
    print(f"  cycle cancels: measured trend = {slope_raw:+.4f} K/decade "
          f"(difference from the anomaly trend "
          f"{abs(slope_raw - slope_w) * 1000:.2f} mK/decade)")
    partial = raw.isel(time=slice(0, 40))
    print(f"  but a series with unequal month coverage does NOT cancel it:")
    months = sst.mean(dim=("lat", "lon"))
    jan_jul = months.sel(time=months.time.dt.month.isin([1, 7]))
    slope_jj, _ = trend_per_decade(jan_jul)
    print(f"    January+July only ({jan_jul.size} samples): trend = "
          f"{slope_jj:+.4f} K/decade")

    section("5. Zonal profiles and latitude bands")
    zonal = anom.mean(dim="lon").mean(dim="time")
    print("  time-mean zonal anomaly by latitude (K):")
    for lat_label in (-77.5, -47.5, -17.5, 7.5, 32.5, 62.5, 82.5):
        value = float(zonal.sel(lat=lat_label, method="nearest"))
        print(f"    {lat_label:+6.1f} deg: {value:+.4f}")
    band = anom.sel(lat=slice(-5.0, 5.0))
    trop = global_mean(band).resample(time="YE").mean()
    slope_t, _ = trend_per_decade(trop)
    polar = global_mean(anom.sel(lat=slice(60.0, 90.0))).resample(time="YE").mean()
    slope_p, _ = trend_per_decade(polar)
    print(f"  the imposed trend is uniform in space, so both bands should recover")
    print(f"  {TREND_K_PER_DECADE:+.4f} K/decade:")
    print(f"    5 S-5 N  : {slope_t:+.4f} K/decade "
          f"(error {(slope_t - TREND_K_PER_DECADE) * 1000:+.2f} mK/decade)")
    print(f"    60-90 N  : {slope_p:+.4f} K/decade "
          f"(error {(slope_p - TREND_K_PER_DECADE) * 1000:+.2f} mK/decade)")

    section("6. A regression map: which pixels follow the oscillation?")
    idx = xr.DataArray(enso_index, dims=("time",), coords={"time": sst.time})
    idx = idx.groupby("time.month") - idx.groupby("time.month").mean()
    idx_std = (idx - idx.mean()) / idx.std()
    corr = xr.corr(anom, idx_std, dim="time")
    peak = corr.where(np.abs(corr.lat) < 10.0)
    flat = np.abs(peak.fillna(0.0).values).argmax()
    i_lat, i_lon = np.unravel_index(flat, peak.shape)
    print(f"  correlation of the monthly anomaly with the ENSO index:")
    print(f"    global maximum |r| = {float(np.abs(corr).max()):.4f} at "
          f"lat {float(corr.lat[i_lat]):.1f}, lon {float(corr.lon[i_lon]):.1f}")
    print(f"    equatorial band (|lat| < 10 deg): max |r| = "
          f"{float(np.abs(peak).max()):.4f}")
    mid_lat = corr.sel(lat=slice(40.0, 60.0))
    print(f"    mid-latitude band 40-60 N: max |r| = "
          f"{float(np.abs(mid_lat).max()):.4f}")
    print(f"    the imposed pattern is cos(2*lat), which is +1 at the equator and")
    print(f"    -1 at 90 deg, so the equatorial band must respond more strongly")
    idx_std_value = float(idx.std())
    signal = ENSO_K * abs(np.cos(2.0 * np.deg2rad(7.5))) * idx_std_value
    predicted = signal / np.sqrt(signal ** 2 + 0.35 ** 2)
    print(f"    prediction from the imposed amplitudes: deseasonalised index")
    print(f"    std = {idx_std_value:.4f} K, so the local signal std is "
          f"{signal:.4f} K against {0.35:.2f} K of noise -> r = {predicted:.4f}")

    section("7. Lag correlation: the signal propagates")
    for lag in (0, 2, 4, 6, 9, 12):
        shifted = idx_std.shift(time=lag)
        lagged = xr.corr(anom, shifted, dim="time")
        r = float(global_mean(lagged).mean())
        print(f"  lag +{lag:2d} months: area-weighted mean correlation = {r:+.4f}")
    print("  the index is an amplitude-modulated sinusoid (4-year carrier inside")
    print("  a 20-year Gaussian burst), so the lag correlation decays over ~6-9")
    print("  months instead of oscillating the way a pure carrier would.")

    section("8. What would change with real data")
    print(f"  * A real cube would be fetched from {BASE_URL};")
    print("    this demo never touches the network.")
    print("  * A land-sea mask, a sea-ice mask and a variable land fraction all")
    print("    have to be applied before a global mean is meaningful.")
    print("  * Satellite-era SSTs are stored as float32 NetCDF with")
    print("    scale_factor/add_offset, so the last digits above are not physics.")
    print("  * Cell areas vary by cos(lat); this demo uses the cos(lat) weight,")
    print("    which is exact for a sphere and within 0.1-0.8 % of the WGS 84")
    print("    ellipsoidal band areas (measured in the Dataset lesson).")
    print(f"  * The cube is {sst.nbytes / 2**20:.1f} MiB: small enough for a")
    print("    laptop. A 0.25 deg satellite product is ~10^4 times bigger, which")
    print("    is where the chunking lesson becomes necessary.")


if __name__ == "__main__":
    main()
