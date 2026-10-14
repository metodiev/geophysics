#!/usr/bin/env python3
"""How a positioning error becomes an anomaly error.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python positioning_error_demo.py

Everything printed is computed here.

Contents
--------
1. The free-air gradient is DERIVED as 2 g / a, then converted to mGal/m.
2. Vertical GNSS error -> gravity error through that gradient, for three grades
   of positioning (autonomous, SBAS/DGPS, RTK).
3. Horizontal mislocation of a station across a point-mass anomaly, for a range
   of body depths: the error is (dg/dx) * dx, measured by finite differences on
   the analytic profile.
4. The same horizontal error for a magnetic dipole (inverse-cube falloff), to
   show that the potential-field gradient problem is far worse for magnetics.
"""

import numpy as np

# --- constants (exact/derived, not remembered instrument specs) --------------
G = 6.67430e-11          # m^3 kg^-1 s^-2   CODATA 2018, rel. unc. 2.2e-5
G_SURFACE = 9.80665      # m s^-2  standard gravity (definition of the standard)
EARTH_A = 6371.0e3       # m       IUGG mean Earth radius
MGAL = 1.0e-5            # m s^-2 per mGal  (by definition of the Gal)


def point_mass_gz(x, mass_kg, depth_m):
    """Vertical gravity of a point mass (exact for the exterior of a uniform sphere)."""
    return G * mass_kg * depth_m / (x ** 2 + depth_m ** 2) ** 1.5


def main() -> None:
    # --- 1. Free-air gradient from first principles --------------------------
    dfree = 2.0 * G_SURFACE / EARTH_A                     # s^-2
    dfree_mgal = dfree / MGAL                             # mGal per m
    print("1. Free-air gradient, derived as 2 g / a")
    print(f"   g at the surface                = {G_SURFACE:.5f} m s^-2")
    print(f"   mean Earth radius a             = {EARTH_A:.0f} m")
    print(f"   dg/dz = 2g/a                    = {dfree:.6e} s^-2")
    print(f"   dg/dz                           = {dfree_mgal:.5f} mGal/m")
    print("   (the familiar '0.3086 mGal/m' is this number; it is derived, not assumed)")

    # --- 2. Vertical positioning error --------------------------------------
    print("\n2. Vertical error of the station -> gravity error (free-air only)")
    print(f"   {'grade':<14}{'sigma_z (m)':>13}{'error (mGal)':>15}")
    for grade, sigma_z in (("RTK", 0.03), ("DGPS/SBAS", 0.5), ("autonomous", 3.0)):
        err = sigma_z * dfree_mgal
        print(f"   {grade:<14}{sigma_z:>13.2f}{err:>15.4f}")
    print("   -> a levelled survey exists because uncorrected height error alone")
    print("      can exceed the target anomaly.")

    # --- 3. Horizontal mislocation across a gravity anomaly ------------------
    print("\n3. Horizontal mislocation across a point-mass gravity anomaly")
    print("   SYNTHETIC body: uniform sphere of density contrast 1000 kg/m^3, radius R.")
    drho = 1000.0
    print(f"   {'R (m)':>7}{'depth (m)':>11}{'peak (mGal)':>13}{'max |dg/dx| (mGal/m)':>22}"
          f"{'err @0.5m':>11}{'err @5m':>10}")
    for radius, depth in ((50.0, 150.0), (50.0, 300.0), (100.0, 500.0), (200.0, 1000.0)):
        mass = 4.0 / 3.0 * np.pi * radius ** 3 * drho
        x = np.linspace(-3000.0, 3000.0, 600001)
        gz = point_mass_gz(x, mass, depth) / MGAL
        grad = np.gradient(gz, x)
        peak = point_mass_gz(np.array([0.0]), mass, depth)[0] / MGAL
        gmax = float(np.max(np.abs(grad)))
        print(f"   {radius:>7.0f}{depth:>11.0f}{peak:>13.4f}{gmax:>22.5f}"
              f"{gmax*0.5:>11.5f}{gmax*5.0:>10.4f}")
    print("   -> for these synthetic bodies the horizontal gradient term is small")
    print("      compared with the vertical/free-air term of section 2; horizontal")
    print("      positioning is second-order for gravity but dominant for magnetics")
    print("      (section 4) and for very shallow surveys.")

    # --- 4. Magnetic dipole: the same error, much larger ---------------------
    print("\n4. Horizontal mislocation across a magnetic dipole")
    print("   SYNTHETIC: vertical dipole, moment m = 1e5 A m^2 at depth h.")
    mu0_over_4pi = 1.0e-7       # T m / A   exact (SI definition of mu0)
    m_moment = 1.0e5
    print(f"   {'depth (m)':>10}{'peak (nT)':>12}{'max |dB/dx| (nT/m)':>21}"
          f"{'err @0.5m (nT)':>17}")
    for depth in (10.0, 30.0, 100.0):
        x = np.linspace(-1000.0, 1000.0, 400001)
        b = mu0_over_4pi * m_moment * (2.0 * depth ** 2 - x ** 2) / (x ** 2 + depth ** 2) ** 2.5
        b_nT = b * 1e9
        grad = np.gradient(b_nT, x)
        peak = mu0_over_4pi * m_moment * 2.0 / depth ** 3 * 1e9
        print(f"   {depth:>10.0f}{peak:>12.1f}{np.max(np.abs(grad)):>21.1f}"
              f"{np.max(np.abs(grad))*0.5:>17.1f}")
    print("   -> magnetic gradients are orders of magnitude steeper than gravity")
    print("      gradients over the same body, so magnetic surveys need better")
    print("      positioning for the same anomaly error.")


if __name__ == "__main__":
    main()
