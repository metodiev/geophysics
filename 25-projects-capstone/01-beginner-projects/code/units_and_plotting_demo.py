#!/usr/bin/env python3
"""Beginner project 1: unit conversion, dimensional checking and the numbers a
first scientific figure must carry.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python units_and_plotting_demo.py

Everything here is SYNTHETIC.  The "measurements" are teaching values typed into
the script; no instrument, archive or published table is read.

Sections
--------
1. A field-units table converted to SI, one row at a time.
2. Derived gradients: what the free-air and Bouguer corrections are worth.
3. A dimensional check of the anomaly ratio, and the Earth-surface gravity value.
4. The summary statistics a first figure must print next to its points.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Exact standard constants (SI), used for the checks ----------------------
GRAV_CONST = 6.67430e-11      # gravitational constant, m^3 kg^-1 s^-2
GM_EARTH = 3.986004418e14     # Earth's gravitational parameter, m^3 s^-2
R_EARTH = 6.371e6             # mean Earth radius, m
MGAL = 1.0e-5                 # 1 mGal expressed in m s^-2

# --- SYNTHETIC field measurements, in the units a field sheet would use ------
FIELD = (
    ("gravity anomaly", 32.5, "mGal"),
    ("target depth", 2.4, "km"),
    ("rock density", 2.67, "g/cm^3"),
    ("seismic velocity", 5.80, "km/s"),
    ("total magnetic field", 48000.0, "nT"),
    ("station spacing", 250.0, "m"),
)

# unit -> (SI factor, SI unit)
TO_SI = {
    "mGal": (1.0e-5, "m/s^2"),
    "km": (1.0e3, "m"),
    "g/cm^3": (1.0e3, "kg/m^3"),
    "km/s": (1.0e3, "m/s"),
    "nT": (1.0e-9, "T"),
    "m": (1.0, "m"),
}


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    section("1. Field units converted to SI")
    print("SYNTHETIC measurements - typed into the script, not measured")
    print(f"{'quantity':<22}{'value':>12} {'unit':>8} -> {'SI value':>14} {'SI unit':>10}")
    for name, value, unit in FIELD:
        factor, si_unit = TO_SI[unit]
        print(f"{name:<22}{value:>12.4g} {unit:>8} -> {value * factor:>14.6g} {si_unit:>10}")

    section("2. Gravity gradients: free-air and Bouguer")
    g_surface = GM_EARTH / R_EARTH ** 2
    free_air = 2.0 * g_surface / R_EARTH
    density = 2670.0
    bouguer = 2.0 * np.pi * GRAV_CONST * density
    print(f"  g from GM/R^2 = {g_surface:.4f} m/s^2  (reference value 9.82 m/s^2)")
    print(f"  free-air gradient 2g/R          = {free_air:.4e} m/s^2 per m")
    print(f"                                  = {free_air / MGAL:.4f} mGal/m")
    print(f"  Bouguer slab 2*pi*G*rho (rho=2670 kg/m^3) = {bouguer:.4e} m/s^2 per m")
    print(f"                                  = {bouguer / MGAL:.4f} mGal/m")
    print(f"  ratio free-air / Bouguer        = {free_air / bouguer:.4f} (dimensionless)")
    print("  -> both gradients have units of acceleration per length, so a")
    print("     correction in mGal follows from a height in m with no extra factor.")

    section("3. Dimensional check of the anomaly ratio")
    anomaly = 32.5 * MGAL                       # m/s^2
    ratio_ppm = anomaly / g_surface * 1.0e6     # dimensionless, parts per million
    print(f"  anomaly {anomaly:.3e} m/s^2 divided by g {g_surface:.4f} m/s^2")
    print(f"  = {ratio_ppm:.3f} parts per million (dimensionless)")
    print("  -> a dimensionless ratio is the only form that survives a change of")
    print("     unit system; a bare 32.5 is meaningless without 'mGal'.")
    print(f"  velocity/time check: 5.80 km/s through 2.4 km takes "
          f"{(2.4e3) / (5.8e3):.4f} s")

    section("4. What a first figure must print")
    n = 120
    spacing = 250.0                                     # m
    x = np.arange(n) * spacing
    depth_true = 2400.0
    depth = depth_true + 60.0 * RNG.standard_normal(n)  # SYNTHETIC scatter, m
    print(f"  profile of {n} stations, spacing {spacing:.0f} m "
          f"(total length {(n - 1) * spacing / 1e3:.2f} km)")
    print(f"  depth: mean {depth.mean():.1f} m, std {depth.std(ddof=1):.1f} m, "
          f"range {depth.min():.1f} to {depth.max():.1f} m")
    print(f"  standard error of the mean = {depth.std(ddof=1) / np.sqrt(n):.2f} m")
    print(f"  x limits that must be labelled: 0 to {(n - 1) * spacing / 1e3:.2f} km")
    print(f"  y limits that must be labelled: {depth.min():.1f} to {depth.max():.1f} m")
    print("  -> a figure is honest when both axes carry a unit, the uncertainty is")
    print("     drawn or stated, and the plotted range matches the caption.")


if __name__ == "__main__":
    main()
