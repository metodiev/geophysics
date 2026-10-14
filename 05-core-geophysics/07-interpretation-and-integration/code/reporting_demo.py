"""Reporting results: an uncertainty budget, propagated and separated by source.

Three quantities a report must carry are computed here, with the *source* of each
uncertainty isolated rather than lumped:

  1. DEPTH WITH UNCERTAINTY.  A Monte Carlo over a half-width measurement, with
     the shape assumption treated as a discrete random variable.  The result is
     bimodal, and the two modes are further apart than the measurement
     uncertainty: the model choice dominates, and the report must say so.
  2. DETECTABILITY.  The smallest mass detectable at a stated depth, and the
     greatest depth detectable for a stated mass, at a stated noise level with a
     stated number of stations.  Stated as a threshold, with the threshold named.
  3. THE MEASUREMENT FLOOR REQUIRED.  What noise level would be needed to place a
     bound on the depth that is tighter than the shape ambiguity.  This is the
     number that decides whether to buy better instruments or better geology.

No number here is an instrument specification; every parameter is a SYNTHETIC
input chosen for the calculation.

Run:  python3 reporting_demo.py
"""

from __future__ import annotations

import numpy as np

G = 6.674e-11  # m^3 kg^-1 s^-2
MGAL = 1.0e-5  # m s^-2 per mGal


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main() -> None:
    rng = np.random.default_rng(20261014)

    section("1. Depth with a stated uncertainty, and its dominant source")
    n = 400_000
    x_half_true = 383.23          # SYNTHETIC measured half-width, m
    sigma_x = 0.02 * x_half_true  # SYNTHETIC 2 per cent reading uncertainty
    x_half = rng.normal(x_half_true, sigma_x, n)

    is_point = rng.random(n) < 0.5          # prior: equal weight to both shapes
    depth = np.where(is_point, 1.30477 * x_half, 1.0 * x_half)

    q = np.percentile(depth, [5, 16, 50, 84, 95])
    print(f"half-width                        = {x_half_true:.2f} +/- "
          f"{sigma_x:.2f} m ({100 * sigma_x / x_half_true:.1f} per cent)")
    print(f"depth percentiles 5/16/50/84/95   = "
          + " / ".join(f"{v:.1f}" for v in q) + " m")
    print(f"depth from the measurement alone  = {1.30477 * sigma_x:.2f} m "
          "(1 sigma, shape fixed)")
    print(f"spread from the shape assumption  = "
          f"{abs(1.30477 * x_half_true - x_half_true):.2f} m")
    ratio = abs(1.30477 * x_half_true - x_half_true) / (1.30477 * sigma_x)
    print(f"shape spread / measurement spread = {ratio:.1f}")
    print("The reportable sentence is not 'depth = 500 m'; it is 'depth between "
          "383 and\n500 m, the two ends corresponding to a cylinder and a sphere, "
          "and the data\ndo not distinguish them'.  Quoting only the measurement "
          "error would understate\nthe true uncertainty by a factor of "
          f"{ratio:.0f}.")

    section("2. Detectability: what noise level and station count buy")
    z_target = 300.0
    mass = 5.79e9                 # SYNTHETIC body, kg
    sigma = 0.02 * MGAL           # SYNTHETIC noise per station
    peak = G * mass / z_target ** 2
    print(f"body mass {mass:.3e} kg at {z_target:.0f} m -> peak anomaly "
          f"{peak / MGAL:.3f} mGal")
    print(f"station noise {sigma / MGAL:.2f} mGal -> peak/noise = "
          f"{peak / sigma:.1f}")
    print(f"detected at 3 sigma?  {peak / sigma > 3.0}")
    z_max = np.sqrt(G * mass / (3.0 * sigma))
    mass_min = 3.0 * sigma * z_target ** 2 / G
    print(f"greatest depth for this mass at 3 sigma  = {z_max:7.1f} m")
    print(f"smallest mass at {z_target:.0f} m for 3 sigma      = "
          f"{mass_min:.3e} kg")
    print(f"a factor of 2 less noise pushes the depth limit to "
          f"{np.sqrt(2.0) * z_max:7.1f} m")
    print("Depth of investigation scales as the square root of the noise and as "
          "the square\nroot of the mass: this is the entire content of a "
          "detectability study, and it\nshould be done before the survey, not "
          "after.")

    section("3. The measurement floor that would beat the shape ambiguity")
    print("To place a depth bound tighter than the shape ambiguity (117 m at "
          "500 m), the\n1-sigma depth error from the measurement must be below "
          "about 117 m, i.e.")
    needed_sigma_x = 117.0 / 1.30477
    print(f"  half-width read to better than {needed_sigma_x:.1f} m "
          f"({100 * needed_sigma_x / x_half_true:.0f} per cent)")
    print(f"  measured half-width is read to {sigma_x:.2f} m "
          f"({100 * sigma_x / x_half_true:.0f} per cent), which already meets it")
    print("So better instruments do not help.  What helps is an independent "
          "constraint on\nthe SHAPE -- a second dataset with transverse "
          "sensitivity, or a borehole.  This\nis the calculation that tells you "
          "which to buy.")


if __name__ == "__main__":
    main()
