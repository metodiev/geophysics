#!/usr/bin/env python3
"""Vertical datums, part 2: geopotential numbers, orthometric and normal heights,
the datum offset, and what GNSS plus a geoid model changes.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python vertical_datum_modernisation_demo.py

Everything here is SYNTHETIC: the levelling line, the heights, the gravity
profile, the geoid and the error levels are teaching values.  No real network,
benchmark or datum is used.

Contents
--------
1. A synthetic levelling line and its geopotential numbers.
2. Dynamic, orthometric and normal heights from the same geopotential numbers.
3. The orthometric correction: what the naive sum of levelled differences costs.
4. The datum offset: mean sea level versus the geoid.
5. Modernisation: GNSS + geoid, with an error budget, and what cancels in
   differences.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
GAMMA_45 = 9.806199                # m s^-2, normal gravity at 45 deg (rounded)
FREE_AIR = 0.3086e-5               # m s^-2 per m, free-air gradient (rounded)
MEAN_GRAV_GRAD = 0.0424e-5         # m s^-2 per m, Poincare-Prey gradient
M_GAL = 1.0e-5

# --- SYNTHETIC parameters ----------------------------------------------------
N_STATION = 21
LAT0 = 45.0
DLAT = 0.15                        # deg per station (~16.7 km)
H_START, H_END = 0.0, 800.0        # m, orthometric height along the line
SST = 0.30                         # m, synthetic sea-surface topography
GEOID_SLOPE = 0.8                  # m per 1000 km of the synthetic geoid
LEV_ERROR = 1.0e-3                 # m per sqrt(km), synthetic levelling noise
GNSS_SIGMA = 0.015                 # m
GEOID_SIGMA = 0.020                # m (absolute; correlated over ~100 km)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def gamma_normal(lat_deg):
    """A rounded standard normal-gravity formula (International Gravity Formula)."""
    p = np.deg2rad(lat_deg)
    return 9.780327 * (1.0 + 0.0053024 * np.sin(p) ** 2
                       - 0.0000058 * np.sin(2 * p) ** 2)


def main():
    lats = LAT0 + DLAT * np.arange(N_STATION)
    dist_km = DLAT * 111.32 * np.cos(np.deg2rad(lats)) * np.arange(N_STATION)
    H_true = np.linspace(H_START, H_END, N_STATION)      # orthometric heights

    section("1. A synthetic levelling line")
    g_surf = gamma_normal(lats) - FREE_AIR * H_true
    g_mean = g_surf + MEAN_GRAV_GRAD * H_true / 2.0      # Poincare-Prey mean
    C = g_mean * H_true                                  # geopotential number
    print(f"  {N_STATION} stations, latitude {lats[0]:.2f} to {lats[-1]:.2f} deg")
    print(f"  line length {dist_km[-1]:.1f} km; heights {H_true[0]:.0f} to "
          f"{H_true[-1]:.0f} m")
    print(f"  normal gravity gamma(45 deg) = {gamma_normal(45.0):.6f} m/s^2, "
          f"gamma({lats[-1]:.2f} deg) = {gamma_normal(lats[-1]):.6f} m/s^2")
    print(f"  surface gravity at the first and last station: "
          f"{g_surf[0]:.6f}, {g_surf[-1]:.6f} m/s^2")
    print(f"  geopotential number C = 0 to {C[-1]:.1f} m^2/s^2")
    print("  (C is the physical quantity levelling measures: sum of g dn)")

    section("2. Dynamic, orthometric and normal heights")
    H_dyn = C / GAMMA_45
    H_ortho = C / g_mean
    gamma_bar = gamma_normal(lats) + FREE_AIR * H_true / 2.0
    H_norm = C / gamma_bar
    print("   station   C (m^2/s^2)   H_dyn (m)   H_ortho (m)   H_norm (m)")
    for i in (0, 5, 10, 15, 20):
        print(f"   {i:7d} {C[i]:13.1f} {H_dyn[i]:11.3f} {H_ortho[i]:12.3f} "
              f"{H_norm[i]:12.3f}")
    print(f"  maximum |H_ortho - H_norm| over the line = "
          f"{np.max(np.abs(H_ortho-H_norm)):.4f} m")
    print(f"  maximum |H_dyn - H_ortho| over the line = "
          f"{np.max(np.abs(H_dyn-H_ortho)):.4f} m")
    print("  Three heights, one geopotential number: the differences are")
    print("  systematic functions of latitude and height, and any two national")
    print("  height systems differ by exactly this kind of term.")

    section("3. The orthometric correction")
    dn = np.diff(C) / g_mean[1:]                 # levelled height differences
    H_lev = np.concatenate([[0.0], np.cumsum(dn)])
    ortho_corr = H_ortho - H_lev
    print("  Summing the levelled differences gives a 'height' that is not the")
    print("  orthometric height:")
    print("   station   levelled sum (m)   H_ortho (m)   difference (mm)")
    for i in (0, 5, 10, 15, 20):
        print(f"   {i:7d} {H_lev[i]:16.4f} {H_ortho[i]:13.4f} "
              f"{(H_ortho[i]-H_lev[i])*1e3:16.2f}")
    print(f"  maximum orthometric correction over the line = "
          f"{np.max(np.abs(ortho_corr))*1e3:.2f} mm")
    print("  It is small on a short line and grows with the height range and the")
    print("  latitude range; on this 223 km, 800 m line it is already comparable")
    print("  with the GNSS + geoid error computed in Section 5, and it is a")
    print("  SYSTEMATIC term that no amount of repeating the levelling removes.")

    section("4. The datum offset")
    N_geoid = GEOID_SLOPE * dist_km / 1000.0      # synthetic geoid along the line
    msl = N_geoid + SST                           # mean sea level above the
    #                                                ellipsoid at the coast
    datum_offset = SST
    print(f"  SYNTHETIC sea-surface topography = {SST:.2f} m")
    print(f"  the national datum is defined by mean sea level at the coast, which")
    print(f"  sits {datum_offset:.2f} m above the geoid in this model.")
    print(f"  geoid height along the line: {N_geoid[0]:.2f} to {N_geoid[-1]:.2f} m")
    print("  Consequences:")
    print(f"    - published heights differ from geoid-referenced orthometric")
    print(f"      heights by a constant {datum_offset*100:.1f} cm")
    print(f"    - HEIGHT DIFFERENCES between benchmarks are unaffected by it:")
    print(f"      max |difference change| = 0.0 mm")
    print("  A datum offset is a choice of origin.  It matters for absolute")
    print("  heights (flood risk, sea-level comparison) and not for differences")
    print("  (engineering, deformation).  Saying which one a number refers to is")
    print("  the whole of 'datum modernisation'.")

    section("5. Modernisation: GNSS + geoid, and what the errors do")
    h_ell = H_ortho + N_geoid                    # ellipsoidal height
    print(f"  error model: GNSS sigma = {GNSS_SIGMA*100:.1f} cm (white),")
    print(f"               geoid sigma = {GEOID_SIGMA*100:.1f} cm, correlated")
    print("               over ~100 km")
    print("  Three ways to obtain heights, and their errors over the line:")
    print("   method                        sigma at a point   "
          "difference over 3 km")
    lev_point = LEV_ERROR * np.sqrt(dist_km[-1])
    lev_diff = LEV_ERROR * np.sqrt(3.0)
    print(f"   spirit levelling from the datum {lev_point*100:9.2f} cm "
          f"{lev_diff*100:16.2f} cm")
    gnss_point = np.sqrt(GNSS_SIGMA ** 2 + GEOID_SIGMA ** 2)
    gnss_diff = np.sqrt(2 * GNSS_SIGMA ** 2 + 2 * (GEOID_SIGMA * 0.05) ** 2)
    print(f"   GNSS + geoid                   {gnss_point*100:9.2f} cm "
          f"{gnss_diff*100:16.2f} cm")
    print(f"   (for the 3 km difference the geoid error is taken as 5% of its")
    print(f"    absolute value, i.e. correlated, so it largely cancels; the GNSS")
    print(f"    error is treated as white and does not)")
    cross = (gnss_point / LEV_ERROR) ** 2
    cross_diff = (gnss_diff / LEV_ERROR) ** 2
    print("  The numbers do NOT support the folklore that the new method is")
    print(f"  always better.  At {dist_km[-1]:.0f} km, levelling from the datum")
    print(f"  ({lev_point*100:.2f} cm) beats GNSS+geoid ({gnss_point*100:.2f} cm),")
    print("  because levelling error accumulates only as sqrt(L) while the")
    print("  GNSS+geoid error is dominated by two independent white terms.")
    print(f"  The crossover in this error model is L = {cross:.0f} km for absolute")
    print(f"  heights and L = {cross_diff:.0f} km for differences: below those")
    print(f"  lengths levelling wins (at 3 km: {lev_diff*100:.2f} cm against "
          f"{gnss_diff*100:.2f} cm), and above them GNSS+geoid wins, because a")
    print("  correlated geoid error cancels in differences while a white one does")
    print("  not.  Real networks change these numbers: levelling standards vary,")
    print("  the height-system corrections of Section 3 are systematic, and GNSS")
    print("  errors are correlated over baselines of tens of kilometres.")
    print("  A modernisation plan must therefore state WHICH heights it is")
    print("  improving -- absolute, long-line or short-baseline -- and quote the")
    print("  crossover length, not an average improvement.")


if __name__ == "__main__":
    main()
