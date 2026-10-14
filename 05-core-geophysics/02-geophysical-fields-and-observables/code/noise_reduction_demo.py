"""From instrument reading to anomaly: noise, drift, tides, and reductions.

A gravimeter does not output gravity.  It outputs a difference from a datum,
contaminated by instrument drift, Earth tides, and random noise.  Turning that
into a Bouguer anomaly takes a sequence of corrections whose size is often
larger than the anomaly itself.

This script builds a SYNTHETIC relative-gravity survey with the terrain effect
*included in the readings*, then processes it step by step:

  1. derive the free-air gradient dg/dh = -2g/R and the Bouguer gradient
     2*pi*G*rho, and use them to build the synthetic readings;
  2. simulate linear drift, an M2-like Earth tide, and white readout noise;
  3. remove drift and tide, then apply the free-air and Bouguer corrections;
  4. compare the recovered anomaly with the anomaly built in.

The point of including the terrain effect in the readings is that the
corrections must then *remove* it.  Subtracting a correction for an effect that
was never present is a real and common error; Section 6 quantifies what a
wrong Bouguer density costs.

Every numeric input is SYNTHETIC and stated.  Constants are SI and cited.

Run:  python3 noise_reduction_demo.py
"""

from __future__ import annotations

import numpy as np

G = 6.67430e-11  # m^3 kg^-1 s^-2 (CODATA 2018, NIST)
MGAL = 1.0e-5    # m/s^2 per mGal


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main() -> None:
    rng = np.random.default_rng(31415)

    # ==================================================================
    section("1. Derive the two elevation gradients BEFORE using them")
    g_surface = 9.8              # m/s^2, stated local value (measurable)
    R_earth = 6378137.0          # m, WGS 84 semi-major axis (defining constant)
    rho_slab = 2400.0            # kg/m^3, SYNTHETIC Bouguer density
    free_air_grad = -2.0 * g_surface / R_earth       # (m/s^2) per m
    bouguer_grad = 2.0 * np.pi * G * rho_slab        # (m/s^2) per m
    print(f"  free air: dg/dh = -2g/R = -2*{g_surface:.1f}/{R_earth:.0f}"
          f" = {free_air_grad:.4e} (m/s^2)/m = "
          f"{free_air_grad/MGAL:.6f} mGal/m")
    print("    (g = GM/r^2 differentiated; M is never needed.  The classical")
    print("     0.3086 mGal/m is the ELLIPSOIDAL normal-gravity gradient,")
    print("     -2*gamma/a*(1 + f + m - 2f sin^2 phi).  For WGS 84 at 45 deg")
    print("     that factor is 1.00344979, giving -0.308555 mGal/m.  The")
    print("     difference is the ellipsoidal factor, NOT a second-order term")
    print("     in h: the latter is of relative order h/R ~ 1e-6 at survey")
    print("     elevations.  We use the spherical leading term and say so.)")
    print(f"  Bouguer : dg/dh = 2 pi G rho = 2 pi * {G:.4e} * {rho_slab:.0f}"
          f" = {bouguer_grad:.4e} (m/s^2)/m")
    print(f"          = {bouguer_grad/MGAL:.6f} mGal/m")
    print(f"  ratio (Bouguer/free-air magnitudes) = "
          f"{bouguer_grad/abs(free_air_grad):.6f}")
    print("  Both are slab physics at different densities: the free-air term")
    print("  is the vertical gradient of g, the Bouguer term the attraction")
    print("  of an infinite slab whose thickness is the elevation change.")

    # ==================================================================
    section("2. SYNTHETIC survey with the terrain effect included")
    n_stations = 20
    spacing = 100.0
    x = np.arange(n_stations) * spacing
    anomaly_true = 4.0 * np.exp(-0.5 * ((x - x[9]) / 200.0) ** 2)   # mGal
    elevations = 120.0 + 8.0 * np.sin(2.0 * np.pi * x / 1400.0)     # m a.s.l.
    relief = elevations - elevations[0]

    drift_rate, tide_amp, noise_sigma = 0.05, 0.15, 0.02  # mGal units
    t_hours = np.linspace(0.0, 4.0, n_stations)
    drift = drift_rate * t_hours
    tide = tide_amp * np.sin(2.0 * np.pi * t_hours / 12.42)
    noise = rng.normal(0.0, noise_sigma, n_stations)

    free_air_effect = free_air_grad * relief / MGAL      # mGal, negative
    bouguer_effect = bouguer_grad * relief / MGAL        # mGal, positive
    reading = (anomaly_true + free_air_effect + bouguer_effect
               + drift + tide + noise)
    print(f"  {n_stations} stations, {spacing:.0f} m spacing, "
          f"4 h occupation time")
    print(f"  target anomaly      : 4.0 mGal Gaussian, 200 m half-width")
    print(f"  relief              : {relief.min():+.1f} to {relief.max():+.1f} m"
          f" relative to the base station")
    print(f"  free-air effect     : {free_air_effect.min():+.3f} to "
          f"{free_air_effect.max():+.3f} mGal")
    print(f"  Bouguer slab effect : {bouguer_effect.min():+.3f} to "
          f"{bouguer_effect.max():+.3f} mGal")
    print(f"  drift over 4 h      : {drift.max():.3f} mGal")
    print(f"  tide amplitude      : {tide_amp:.3f} mGal (period 12.42 h)")
    print(f"  reading noise sigma : {noise_sigma:.3f} mGal")
    err = reading - anomaly_true
    print(f"  raw RMS departure from the target anomaly = "
          f"{np.sqrt(np.mean(err**2)):.4f} mGal")
    print("  The raw number is dominated by drift and tide, and the elevation")
    print("  effects are of the same order as the target.  Until the")
    print("  corrections are applied, the reading is not an anomaly.")

    # ==================================================================
    section("3. Remove drift and tide (base-station repeat and tide model)")
    corrected = reading - drift - tide
    err3 = corrected - anomaly_true
    print(f"  after drift+tide removal, RMS departure = "
          f"{np.sqrt(np.mean(err3**2)):.4f} mGal")
    print("  What remains is the elevation effect plus noise, not noise alone.")
    print("  In practice drift is ESTIMATED by re-occupying a base station, so")
    print("  it is never removed perfectly; residual drift of 0.01-0.05 mGal")
    print("  over a survey is routine.  Here we removed it exactly -- an")
    print("  optimistic assumption, stated as such.")

    # ==================================================================
    section("4. Apply the corrections: this is where the elevation effect goes")
    free_air_corr = -free_air_effect        # added to the reading
    bouguer_corr = bouguer_effect           # subtracted from the reading
    bouguer_anomaly = corrected + free_air_corr - bouguer_corr
    resid = bouguer_anomaly - anomaly_true
    print(f"  free-air correction applied: {free_air_corr.min():+.3f} to "
          f"{free_air_corr.max():+.3f} mGal")
    print(f"  Bouguer correction applied : {-bouguer_corr.min():+.3f} to "
          f"{-bouguer_corr.max():+.3f} mGal")

    # ==================================================================
    section("5. Recovered anomaly versus the anomaly we built in")
    print("   station   x(m)   true(mGal)  recovered(mGal)   residual")
    for i in (0, 5, 9, 14, 19):
        print(f"  {i:7d} {x[i]:6.0f}   {anomaly_true[i]:9.4f}   "
              f"{bouguer_anomaly[i]:14.4f}   {resid[i]:+8.4f}")
    print(f"  RMS residual after all corrections = "
          f"{np.sqrt(np.mean(resid**2)):.4f} mGal")
    print(f"  reading noise sigma                = {noise_sigma:.4f} mGal")
    print(f"  peak true anomaly = {anomaly_true.max():.4f} mGal ; "
          f"peak recovered = {bouguer_anomaly.max():.4f} mGal")
    print("  The residual is now the reading noise, as it must be: the")
    print("  corrections removed exactly what the synthetic model put in.")
    print("  Any residual LARGER than the noise would be either a real")
    print("  feature or a mis-specified correction -- and the data alone")
    print("  cannot tell you which.  That ambiguity is the whole game.")

    # ==================================================================
    section("6. Sensitivity: what a wrong Bouguer density costs")
    print("  assumed rho   peak anomaly (mGal)   shift vs rho=2400 (mGal)")
    ref = bouguer_anomaly.max()
    for rho_try in (2000.0, 2200.0, 2400.0, 2670.0, 3000.0):
        bg = 2.0 * np.pi * G * rho_try * relief / MGAL
        rec = corrected + free_air_corr - bg
        print(f"  {rho_try:11.0f}   {rec.max():20.4f}   "
              f"{rec.max()-ref:+22.4f}")
    print("  A 670 kg/m^3 density error moves the anomaly by ~0.2 mGal, which")
    print("  is the same order as the target for a subtle body.  The Bouguer")
    print("  density is a modeller's CHOICE, not a measurement, and it is a")
    print("  dominant uncertainty in shallow gravity interpretation.  This is")
    print("  why the density must be reported with the anomaly.")

    print("\nSUMMARY: a raw reading is a difference from a datum and an")
    print("anomaly is a difference between corrections.  Know which number")
    print("you are looking at, and how large every correction is relative to")
    print("the feature you claim to see.")


if __name__ == "__main__":
    main()
