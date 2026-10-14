#!/usr/bin/env python3
"""Beginner project 2: mapping global seismicity and measuring the
Gutenberg-Richter b-value from a catalogue.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python earthquake_map_demo.py

Everything here is SYNTHETIC.  The catalogue is generated below from a chosen
b-value and a chosen tectonic geometry; no real catalogue is read and no real
earthquake is described.  Real catalogues are obtained from the USGS FDSN event
service (https://earthquake.usgs.gov/fdsnws/event/1/query).

Sections
--------
1. The synthetic catalogue: magnitude, completeness and depth distributions.
2. The Gutenberg-Richter b-value by maximum likelihood, with its uncertainty.
3. The sensitivity of b to the assumed magnitude of completeness.
4. Map statistics: epicentre density and recovery of the synthetic plate line.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC catalogue parameters (chosen, not measured) -------------------
B_TRUE = 1.00            # Gutenberg-Richter b-value, dimensionless
M_C_TRUE = 4.0           # true magnitude of completeness
DM = 0.1                 # magnitude bin width, magnitude units
N_EVENTS = 3000          # events in the catalogue
BOUNDARY_FRACTION = 0.85  # fraction of events placed on the plate line
LOY, HIY = -60.0, 60.0   # latitude box, degrees north
LOX, HIX = -90.0, 30.0   # longitude box, degrees east


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def plate_latitude(lon):
    """SYNTHETIC plate line: latitude of the boundary as a function of longitude."""
    return 35.0 + 12.0 * np.sin(np.radians(2.5 * (lon + 60.0)))


def make_catalogue(rng):
    """Magnitudes, epicentres and depths of N_EVENTS synthetic events."""
    beta = B_TRUE * np.log(10.0)                       # 1 / mean magnitude step
    excess = rng.exponential(1.0 / beta, N_EVENTS)     # magnitude above Mc
    mag = M_C_TRUE + np.floor(excess / DM) * DM        # binned to DM

    n_boundary = int(BOUNDARY_FRACTION * N_EVENTS)
    lon_b = rng.uniform(LOX, HIX, n_boundary)
    lat_b = plate_latitude(lon_b) + 1.2 * rng.standard_normal(n_boundary)
    lon_o = rng.uniform(LOX, HIX, N_EVENTS - n_boundary)
    lat_o = rng.uniform(LOY, HIY, N_EVENTS - n_boundary)

    lon = np.concatenate([lon_b, lon_o])
    lat = np.concatenate([lat_b, lat_o])

    # Wadati-Benioff style depth: deeper inland of the trench line.
    trench = plate_latitude(lon) - 3.0
    inland = np.clip(lat - trench, 0.0, None)
    depth = np.clip(25.0 + 55.0 * inland + 12.0 * rng.standard_normal(N_EVENTS),
                    5.0, 650.0)
    return mag, lat, lon, depth


def b_value_mle(mag, mc, dm):
    """Aki's maximum-likelihood b-value for a binned catalogue."""
    m_mean = mag.mean()
    return np.log10(np.e) / (m_mean - (mc - dm / 2.0))


def main():
    section("1. The synthetic catalogue")
    mag, lat, lon, depth = make_catalogue(RNG)
    print(f"SYNTHETIC catalogue: {N_EVENTS} events, true b = {B_TRUE:.2f}, "
          f"true Mc = {M_C_TRUE:.1f}, bin width {DM:.1f}")
    print(f"  magnitude range {mag.min():.1f} to {mag.max():.1f}, "
          f"mean {mag.mean():.4f}")
    print(f"  epicentre box: lat {lat.min():.1f} to {lat.max():.1f} deg, "
          f"lon {lon.min():.1f} to {lon.max():.1f} deg")
    counts = np.bincount(((mag - M_C_TRUE) / DM).astype(int))
    print(f"  mean magnitude step <dM> = {mag.mean() - M_C_TRUE + DM / 2:.4f} "
          f"(exact for an exponential: {1 / (B_TRUE * np.log(10.0)):.4f})")
    print(f"  depth: median {np.median(depth):.1f} km, "
          f"90th percentile {np.percentile(depth, 90):.1f} km, "
          f"max {depth.max():.1f} km")
    print(f"  events within 5 km of the surface: {np.sum(depth <= 5.001)}")

    section("2. b-value by maximum likelihood")
    b_est = b_value_mle(mag, M_C_TRUE, DM)
    sigma_b = b_est / np.sqrt(len(mag))
    print(f"  MLE b = log10(e) / (<M> - (Mc - dM/2))")
    print(f"        = {np.log10(np.e):.6f} / ({mag.mean():.4f} - "
          f"({M_C_TRUE:.1f} - {DM / 2:.2f})) = {b_est:.4f}")
    print(f"  Aki standard error b / sqrt(N) = {b_est:.4f} / "
          f"{np.sqrt(len(mag)):.1f} = {sigma_b:.4f}")
    print(f"  true b {B_TRUE:.2f} lies within "
          f"{abs(b_est - B_TRUE) / sigma_b:.2f} sigma of the estimate")

    section("3. Sensitivity to the assumed magnitude of completeness")
    hist, edges = np.histogram(mag, bins=np.arange(M_C_TRUE - 0.5, mag.max() + 0.2, DM))
    mc_curv = edges[np.argmax(hist)]
    print(f"  maximum-curvature Mc (mode of the histogram) = {mc_curv:.1f}")
    for mc_try in (mc_curv, M_C_TRUE, M_C_TRUE + 0.5):
        sel = mag >= mc_try
        b_try = b_value_mle(mag[sel], mc_try, DM)
        print(f"    Mc = {mc_try:.1f}: N = {sel.sum():5d}, b = {b_try:.4f}")
    print("  -> b drifts when Mc is raised: only the Mc used for the fit")
    print("     belongs in the headline number.")

    section("4. Map statistics and recovery of the synthetic plate line")
    line = plate_latitude(lon)
    dist_deg = np.abs(lat - line)
    near = dist_deg <= 2.0
    print(f"  events within 2 deg of the synthetic plate line: "
          f"{near.sum()} of {len(lon)} = {near.mean() * 100:.1f}%")
    for q in (25, 50, 75):
        print(f"  depth {q}th percentile within the 2 deg band = "
              f"{np.percentile(depth[near], q):.1f} km")
    east = near & (lon > 0)
    west = near & (lon <= 0)
    print(f"  median depth east of lon 0: {np.median(depth[east]):.1f} km, "
          f"west: {np.median(depth[west]):.1f} km")
    print(f"  epicentre density in a 10 deg x 10 deg box on the line: "
          f"{near.sum() / ((HIX - LOX) * (HIY - LOY) / 100.0):.1f} events per box")
    print("  -> a map recovers the plate line as a density contrast, not as a")
    print("     drawn boundary; the b-value is the quantitative product.")


if __name__ == "__main__":
    main()
