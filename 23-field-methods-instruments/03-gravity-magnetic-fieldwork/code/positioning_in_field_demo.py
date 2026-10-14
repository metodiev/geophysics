#!/usr/bin/env python3
"""Positioning and elevation arithmetic for potential-field surveys, on SYNTHETIC
parameters.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python positioning_in_field_demo.py

Everything here is SYNTHETIC or derived from stated standard formulas.  The
densities, position accuracies, geoid undulation and averaging counts are chosen
teaching values.  No field survey position, no real geoid model and no measured
accuracy figure is used or reproduced.

Sections
--------
1. The elevation sensitivity of a gravity survey, free-air plus Bouguer.
2. The latitude sensitivity, and the position error it allows.
3. The vertical gradient of the total magnetic field, computed from a dipole model.
4. GNSS methods, their accuracy, and what averaging buys.
5. Ellipsoidal versus orthometric height, and the error of confusing them.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

FREE_AIR = 0.3086          # mGal/m, standard free-air gradient
BOUGUER = 0.0419           # mGal/m per g/cm^3
RHO = 2.67                 # g/cm^3, a chosen reduction density
EARTH_RADIUS = 6.371e6     # m


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def dipole_field(r, latitude_deg, moment):
    """Magnitude of a centred-dipole field, T, at radius r and latitude lambda."""
    lam = np.radians(latitude_deg)
    # components in a local frame: Br = 2 Mm sin(lam)/r^3, Btheta = Mm cos(lam)/r^3
    br = 2.0 * moment * np.sin(lam) / r ** 3
    bt = moment * np.cos(lam) / r ** 3
    return np.sqrt(br ** 2 + bt ** 2)


def main():
    section("1. Elevation sensitivity of a gravity survey")
    bouguer = BOUGUER * RHO
    total = FREE_AIR - bouguer
    print(f"  free-air gradient        = {FREE_AIR:.4f} mGal/m")
    print(f"  Bouguer gradient         = {BOUGUER:.4f} x {RHO:.2f} = "
          f"{bouguer:.4f} mGal/m")
    print(f"  combined (Bouguer anomaly) = {FREE_AIR:.4f} - {bouguer:.4f} = "
          f"{total:.4f} mGal/m")
    print(f"  {'elevation error (m)':>20s} {'free-air (mGal)':>16s}"
          f" {'Bouguer anomaly (mGal)':>24s}")
    for dh in (0.02, 0.05, 0.10, 0.20, 0.50, 1.00):
        print(f"  {dh:20.2f} {FREE_AIR * dh:16.4f} {total * dh:24.4f}")
    print("  -> a microgravity target of 0.01 mGal is met by levelling to about")
    print("     5 cm; a 0.5 m error is 10 % of a 1 mGal regional anomaly.")

    section("2. Latitude sensitivity and the position error it allows")
    print("  normal-gravity latitude gradient is about 0.811 sin(2 phi) mGal/km")
    print(f"  {'latitude':>9s} {'gradient (mGal/km)':>19s} "
          f"{'error from 20 m N-S (mGal)':>28s} {'from 100 m N-S (mGal)':>23s}")
    for phi in (0.0, 30.0, 45.0, 60.0, 90.0):
        grad = 0.811 * np.sin(np.radians(2.0 * phi))
        print(f"  {phi:9.1f} {grad:19.4f} {grad * 0.020:28.4f} "
              f"{grad * 0.100:23.4f}")
    print("  -> a 20 m north-south position error is negligible; a 100 m error is")
    print("     not, at mid-latitudes where the gradient is largest.")

    section("3. Vertical gradient of the total magnetic field")
    moment = 7.8e15           # A m^2, a chosen dipole moment giving ~3e-5 T
    print(f"  centred-dipole model, moment {moment:.1e} A m^2 (chosen so that the")
    print(f"  equatorial surface field is about "
          f"{1.0e9 * dipole_field(EARTH_RADIUS, 0.0, moment):.2f} nT)")
    print(f"  {'latitude':>9s} {'|B| (nT)':>12s} {'d|B|/dz (nT/m)':>17s}")
    dz = 1.0
    for phi in (0.0, 30.0, 45.0, 60.0, 90.0):
        b0 = 1.0e9 * dipole_field(EARTH_RADIUS, phi, moment)
        b1 = 1.0e9 * dipole_field(EARTH_RADIUS + dz, phi, moment)
        print(f"  {phi:9.1f} {b0:12.2f} {(b1 - b0) / dz:17.4f}")
    print("  -> the field decreases upward by a few hundredths of a nT per metre,")
    print("     so a 1 m height error is a fraction of a nanotesla: magnetics is")
    print("     far less sensitive to height than gravity is.")

    section("4. GNSS methods and what averaging buys")
    methods = [("autonomous, single receiver", 5.0, 3.0),
               ("differential (DGPS)", 0.5, 1.0),
               ("RTK, short baseline", 0.02, 0.005)]
    print(f"  accuracy stated as sigma (m), SYNTHETIC values")
    print(f"  {'method':<30s} {'sigma (m)':>10s} {'1 epoch':>10s}"
          f" {'10 epochs':>11s} {'100 epochs':>12s}")
    for label, sigma, _ in methods:
        row = f"  {label:<30s} {sigma:10.3f}"
        for n in (1, 10, 100):
            row += f"{sigma / np.sqrt(n):{10 if n == 1 else 11 if n == 10 else 12}.3f}"
        print(row)
    base_km = 20.0
    ppm = 1.0
    print(f"\n  baseline-dependent term: {ppm:.0f} ppm over {base_km:.0f} km = "
          f"{ppm * 1.0e-6 * base_km * 1000.0:.4f} m")
    print("  -> averaging reduces the random part and not the systematic part:")
    print("     100 epochs cannot remove a baseline-dependent bias.")

    section("5. Ellipsoidal versus orthometric height")
    print(f"  a GNSS receiver returns an ellipsoidal height; the anomaly calculus")
    print(f"  needs an orthometric height, and the difference is the geoid")
    print(f"  undulation, which reaches tens of metres")
    print(f"  {'undulation error (m)':>22s} {'Bouguer anomaly error (mGal)':>30s}")
    for dn in (1.0, 5.0, 10.0, 30.0, 50.0):
        print(f"  {dn:22.0f} {total * dn:30.3f}")
    print("  -> a 30 m geoid error is 5.9 mGal: larger than almost any target")
    print("     anomaly in a microgravity survey.  Use a geoid model, or occupy")
    print("     the stations with optical levelling from a known benchmark.")

    print("\nSYNTHETIC: the parameters above are chosen teaching values; the")
    print("gradients come from the standard formulas quoted in each section.")


if __name__ == "__main__":
    main()
