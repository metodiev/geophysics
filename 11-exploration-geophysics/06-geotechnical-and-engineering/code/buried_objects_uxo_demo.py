#!/usr/bin/env python3
"""Buried objects, UXO detection and clearance: the magnetic dipole anomaly and
its mass-depth scaling, the probability of detection against a stated noise
level, the velocity-depth trade of a GPR hyperbola, and the statistics of a
clearance claim.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python buried_objects_uxo_demo.py

Everything is SYNTHETIC: object magnetisations, sizes, depths, GPR velocities and
clutter rates are chosen teaching values.  No real site, survey or clearance
report is used.  Print-only; no network access.
"""

import numpy as np
from scipy.stats import norm

RNG = np.random.default_rng(20261014)

MU0_OVER_4PI = 1.0e-7      # T m / A (standard constant)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def dipole_anomaly(moment, depth):
    """Vertical magnetic field on the axis of a vertically magnetised dipole.

    B_z = 2 (mu0/4pi) m / z^3, in T for m in A m^2 and z in m.
    """
    return 2.0 * MU0_OVER_4PI * moment / depth ** 3


def sphere_moment(radius, magnetisation):
    """Magnetic moment of a uniformly magnetised sphere, in A m^2."""
    return magnetisation * (4.0 / 3.0) * np.pi * radius ** 3


def hyperbola_time(x, depth, velocity):
    """Two-way GPR travel time to a point target, in ns (m, m/ns)."""
    return 2.0 * np.sqrt(x ** 2 + depth ** 2) / velocity


def main():
    section("1. Magnetic dipole anomaly: mass matters as the cube root")
    magnetisation = 1000.0      # A/m, SYNTHETIC induced magnetisation teaching value
    print(f"  B_z = 2 (mu0/4pi) m / z^3,  m = M * V,  M = {magnetisation:.0f} A/m")
    print("\n   radius (m)   m (A m^2)   B at 0.5 m   at 1 m    at 2 m    at 3 m (nT)")
    for radius in (0.05, 0.10, 0.20, 0.40):
        m = sphere_moment(radius, magnetisation)
        row = "   ".join(f"{dipole_anomaly(m, z)*1e9:9.1f}"
                         for z in (0.5, 1.0, 2.0, 3.0))
        print(f"   {radius:10.2f}   {m:10.3f}   {row}")
    print("\n  A factor-8 mass increase (double radius) buys a factor 8 in moment, and")
    print("  the anomaly falls as z^-3, so the detectable depth grows only as m^{1/3}.")

    section("2. Probability of detection against a stated noise level")
    noise_nt, threshold_nt = 1.0, 2.0      # nT
    noise, threshold = noise_nt * 1e-9, threshold_nt * 1e-9   # T
    print(f"  noise sigma = {noise_nt:.1f} nT, detection threshold = "
          f"{threshold_nt:.1f} nT")
    print("  POD = P(A + noise > threshold) = Phi((A - threshold)/sigma)")
    print("\n   object          POD=0.5 depth   POD=0.9 depth   POD=0.99 depth")
    for label, radius in (("small (0.05 m)", 0.05), ("medium (0.10 m)", 0.10),
                          ("large (0.20 m)", 0.20), ("very large (0.40 m)", 0.40)):
        m = sphere_moment(radius, magnetisation)
        z50 = (2.0 * MU0_OVER_4PI * m / threshold) ** (1.0 / 3.0)
        a90 = threshold + 1.2816 * noise
        z90 = (2.0 * MU0_OVER_4PI * m / a90) ** (1.0 / 3.0)
        a99 = threshold + 2.3263 * noise
        z99 = (2.0 * MU0_OVER_4PI * m / a99) ** (1.0 / 3.0)
        print(f"   {label:16s} {z50:12.2f} m   {z90:12.2f} m   {z99:12.2f} m")
    print("\n  A detection is a PROBABILITY, not a yes/no: the same object is ~90%")
    print("  detectable at one depth and ~50% at a depth only 15% greater.")

    section("3. GPR hyperbola: velocity and depth trade against aperture")
    true_v, true_z = 0.10, 0.50           # m/ns and m (teaching values)
    print(f"  SYNTHETIC target: depth {true_z:.2f} m, velocity {true_v:.3f} m/ns")
    print("  t(x) = 2 sqrt(x^2 + z^2) / v, apex time = "
          f"{2*true_z/true_v:.2f} ns")
    for aperture in (0.5, 1.0, 2.0):
        x = np.linspace(-aperture, aperture, 21)
        t = hyperbola_time(x, true_z, true_v) + 0.02 * RNG.standard_normal(x.size)
        v_grid = np.linspace(0.06, 0.18, 90)
        z_grid = np.linspace(0.3, 1.0, 90)
        chi2 = np.zeros((v_grid.size, z_grid.size))
        for i, v in enumerate(v_grid):
            for j, z in enumerate(z_grid):
                chi2[i, j] = np.sum((hyperbola_time(x, z, v) - t) ** 2)
        best = np.unravel_index(chi2.argmin(), chi2.shape)
        ok = chi2 <= chi2.min() + 4.0
        v_acc = v_grid[ok.any(axis=1)]
        z_acc = z_grid[ok.any(axis=0)]
        print(f"  aperture +/-{aperture:.1f} m: best fit v = {v_grid[best[0]]:.3f} "
              f"m/ns, z = {z_grid[best[1]]:.2f} m; admitted v {v_acc.min():.3f}-"
              f"{v_acc.max():.3f}, z {z_acc.min():.2f}-{z_acc.max():.2f}")
    print("\n  A deeper target with a smaller aperture relative to its depth is worse:")
    true_v2, true_z2 = 0.12, 1.00
    for aperture in (0.4, 0.6, 1.5):
        x = np.linspace(-aperture, aperture, 21)
        t = hyperbola_time(x, true_z2, true_v2) + 0.02 * RNG.standard_normal(x.size)
        v_grid2 = np.linspace(0.05, 0.25, 120)
        z_grid2 = np.linspace(0.5, 1.8, 120)
        chi2 = np.zeros((v_grid2.size, z_grid2.size))
        for i, v in enumerate(v_grid2):
            for j, z in enumerate(z_grid2):
                chi2[i, j] = np.sum((hyperbola_time(x, z, v) - t) ** 2)
        ok = chi2 <= chi2.min() + 4.0
        v_acc = v_grid2[ok.any(axis=1)]
        z_acc = z_grid2[ok.any(axis=0)]
        print(f"  z = {true_z2:.2f} m, aperture +/-{aperture:.1f} m "
              f"(= {aperture/true_z2:.1f} x depth): admitted v {v_acc.min():.3f}-"
              f"{v_acc.max():.3f} m/ns, z {z_acc.min():.2f}-{z_acc.max():.2f} m")
    print("\n  Wide aperture gives the velocity from the hyperbola's curvature and the")
    print("  depth follows.  A narrow aperture sees only the apex, so the depth is a")
    print("  product of the (unknown) velocity: depth and velocity trade exactly.")

    section("4. Clearance statistics: no survey finds everything")
    print("  P(all n objects found) = POD^n")
    print("\n   POD     n = 10      n = 50      n = 100     n = 500")
    for pod in (0.99, 0.95, 0.90, 0.80):
        row = "   ".join(f"{pod**n:10.3f}" for n in (10, 50, 100, 500))
        print(f"   {pod:.2f}   {row}")
    print("\n  A 95% single-object detection rate over 50 objects gives a 7.7% chance")
    print("  that the site is fully cleared.  '100% clearance' is a statement about a")
    print("  detection model and an object population, not a property of an instrument.")
    far = 0.002                  # false alarms per m^2 (teaching value)
    area = 10000.0               # m^2, one hectare
    print(f"\n  with {far*1000:.1f} false alarms per 1000 m^2 over one hectare:")
    print(f"    expected false alarms = {far*area:.0f}, each requiring a dig")
    print("  The cost of the false alarms (and of the ones that are real) is the")
    print("  quantity an operator optimises; a detector with a higher POD and a much")
    print("  higher false-alarm rate can be the more expensive choice.")
    print("\n  All models and data in this module are SYNTHETIC.")


if __name__ == "__main__":
    main()
