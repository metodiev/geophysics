#!/usr/bin/env python3
"""Earth-observation data products: digital numbers, calibration to
top-of-atmosphere reflectance, band indices, and grid resampling.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python landsat_sentinel_demo.py

Everything here is SYNTHETIC.  The scenes, calibration gains and offsets, band
solar irradiances, sun geometry and pixel sizes are chosen teaching values, not
the specifications of any real mission or scene.  No file is read or written and
no network access is used.

Contents
--------
1. DN -> radiance -> TOA reflectance: the two calibration coefficients and the
   solar-geometry correction, laid out with units.
2. Why the coefficients matter: one wrong gain biases every reflectance and
   shifts a band index.
3. NDVI and its saturation with leaf area.
4. Resampling is not linear: mean-of-NDVI differs from NDVI-of-mean.
5. A product is a level plus provenance: enumerating a processing chain.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC calibration and scene parameters (chosen, not measured) -------
GAIN = 0.020           # radiance per DN, W m^-2 sr^-1 um^-1 per DN
OFFSET = -1.0          # radiance offset, W m^-2 sr^-1 um^-1
ESUN_RED = 1950.0      # band solar irradiance, W m^-2 um^-1
ESUN_NIR = 1720.0      # band solar irradiance, W m^-2 um^-1
SUN_ZENITH_DEG = 35.0  # solar zenith angle, degrees
PIXEL_M = 30.0         # nadir pixel size, m (SYNTHETIC)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def dn_to_radiance(dn, gain=GAIN, offset=OFFSET):
    """Spectral radiance (W m^-2 sr^-1 um^-1) from a digital number.

    DN is dimensionless; gain carries the radiance unit per DN, so the product
    has the radiance unit and the offset is added in the same unit.
    """
    return gain * np.asarray(dn, dtype=float) + offset


def radiance_to_reflectance(radiance, esun, sun_zenith_deg, dist_au=1.0):
    """Top-of-atmosphere reflectance (dimensionless) from band radiance.

    rho = pi L d^2 / (E_sun cos(theta)).  L is W m^-2 sr^-1 um^-1 and E_sun is
    W m^-2 um^-1, so L/E_sun is sr^-1; the factor of pi (sr) makes rho
    dimensionless.
    """
    theta = np.deg2rad(sun_zenith_deg)
    return np.pi * radiance * dist_au ** 2 / (esun * np.cos(theta))


def ndvi(red, nir):
    """Normalised difference vegetation index (dimensionless)."""
    red = np.asarray(red, dtype=float)
    nir = np.asarray(nir, dtype=float)
    return (nir - red) / (nir + red)


def main():
    section("1. DN -> radiance -> TOA reflectance (SYNTHETIC coefficients)")
    dn = 4000.0
    L = dn_to_radiance(dn)
    rho = radiance_to_reflectance(L, ESUN_RED, SUN_ZENITH_DEG)
    print(f"calibration gain   = {GAIN:.4f} W m^-2 sr^-1 um^-1 per DN")
    print(f"calibration offset = {OFFSET:+.2f} W m^-2 sr^-1 um^-1")
    print(f"band solar irradiance = {ESUN_RED:.0f} W m^-2 um^-1")
    print(f"solar zenith angle = {SUN_ZENITH_DEG:.0f} deg")
    print(f"  DN = {dn:.0f}")
    print(f"  radiance        L   = {L:.4f} W m^-2 sr^-1 um^-1")
    print(f"  TOA reflectance rho = {rho:.4f} (dimensionless)")
    print("The same DN in a band with a different irradiance gives a different")
    print("reflectance: the coefficients carry the physics, the DN does not.")

    section("2. The coefficients move the answer (SYNTHETIC)")
    dn_red, dn_nir = 3000.0, 6000.0
    r_ok = radiance_to_reflectance(dn_to_radiance(dn_red), ESUN_RED, SUN_ZENITH_DEG)
    n_ok = radiance_to_reflectance(dn_to_radiance(dn_nir), ESUN_NIR, SUN_ZENITH_DEG)
    gain_wrong = GAIN * 0.90        # a 10% gain error, e.g. a mislabelled product
    r_wr = radiance_to_reflectance(dn_to_radiance(dn_red, gain=gain_wrong),
                                   ESUN_RED, SUN_ZENITH_DEG)
    n_wr = radiance_to_reflectance(dn_to_radiance(dn_nir, gain=gain_wrong),
                                   ESUN_NIR, SUN_ZENITH_DEG)
    print(f"correct  : red rho = {r_ok:.4f}, nir rho = {n_ok:.4f}, "
          f"NDVI = {ndvi(r_ok, n_ok):.4f}")
    print(f"10% low gain: red rho = {r_wr:.4f}, nir rho = {n_wr:.4f}, "
          f"NDVI = {ndvi(r_wr, n_wr):.4f}")
    print(f"reflectance bias on red = {(r_wr - r_ok) * 100:+.2f} percentage points")
    print(f"NDVI bias             = {(ndvi(r_wr, n_wr) - ndvi(r_ok, n_ok)):+.4f}")
    print("A multiplicative gain error is multiplicative in radiance, so it")
    print("partly cancels in a ratio index -- but not exactly, and not at all")
    print("in a single-band product.")

    section("3. NDVI saturation with leaf area (SYNTHETIC)")
    red = 0.05
    lai = np.array([0.5, 1.0, 2.0, 3.0, 4.0, 6.0])
    nir = 0.05 + 0.50 * lai / (lai + 1.0)   # chosen reflectance model
    v = ndvi(red, nir)
    print("  LAI    nir(rho)   NDVI")
    for l, n, x in zip(lai, nir, v):
        print(f"  {l:4.1f}   {n:8.4f}   {x:.4f}")
    print(f"gain in NDVI from LAI 0.5 to 2.0 = {v[2] - v[0]:.4f}")
    print(f"gain in NDVI from LAI 4.0 to 6.0 = {v[5] - v[4]:.4f}")
    print("The index saturates: doubling leaf area at high LAI adds far less")
    print("NDVI than at low LAI, so NDVI is not a linear measure of biomass.")

    section("4. Resampling is not linear: mean-of-NDVI vs NDVI-of-mean")
    red_px = np.array([0.04, 0.30, 0.06, 0.22])       # four 30 m pixels
    nir_px = np.array([0.40, 0.50, 0.44, 0.48])
    v_px = ndvi(red_px, nir_px)
    v_mean = v_px.mean()
    v_agg = ndvi(red_px.mean(), nir_px.mean())
    print(f"per-pixel NDVI         = {np.round(v_px, 4)}")
    print(f"mean of NDVI           = {v_mean:.4f}")
    print(f"NDVI of the mean bands = {v_agg:.4f}")
    print(f"difference (mean - agg) = {v_mean - v_agg:+.4f}")
    print("Aggregating to a coarser grid by averaging bands first is NOT the")
    print("same as averaging the index. The difference is the Jensen gap: a")
    print("ratio of averages is not the average of ratios.")

    section("5. A product is a level plus provenance (SYNTHETIC)")
    levels = [
        ("L0", "raw DN and ephemeris", "no calibration applied"),
        ("L1", "radiance and TOA reflectance", "calibration coefficients attached"),
        ("L2", "surface reflectance", "needs an atmospheric model"),
        ("L3", "composited, gap-filled grid", "needs a temporal model"),
    ]
    for lvl, what, needs in levels:
        print(f"  {lvl}: {what:<34} -- {needs}")
    print("Every step below L0 is an inference. Two archives holding 'the same'")
    print("scene can differ because they stopped at different levels.")

    section("6. Pixel size and a nominal footprint")
    print(f"nadir pixel size = {PIXEL_M:.0f} m (SYNTHETIC)")
    print(f"area per pixel   = {PIXEL_M ** 2 / 1e4:.2f} ha")
    print(f"a 1000 x 1000 pixel tile covers {1000 * PIXEL_M / 1000:.0f} km on a side")


if __name__ == "__main__":
    main()
