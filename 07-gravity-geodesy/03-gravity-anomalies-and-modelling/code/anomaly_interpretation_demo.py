#!/usr/bin/env python3
"""Anomaly-interpretation rules: half-width versus depth, amplitude scaling with
depth, and derivative-based depth rules for simple bodies.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python anomaly_interpretation_demo.py

All models and data in this module are SYNTHETIC.  The densities, radii and
depths below are chosen teaching values, not measurements of any real body.

Contents
--------
1. Sphere: vertical anomaly, peak value, half-width and the depth rule.
2. Horizontal cylinder: the same quantities and a different depth rule.
3. Amplitude scaling with depth, measured as log-log slopes.
4. Horizontal derivative: where its maximum sits, and the depth rule it gives.
5. Excess mass and the depth-amplitude trade-off (the first taste of
   non-uniqueness).
6. The cost of assuming the wrong body shape.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_SI = 6.67430e-11        # m^3 kg^-1 s^-2   (CODATA 2018 exact-by-definition value)
MGAL_TO_SI = 1.0e-5       # 1 mGal = 1e-5 m/s^2


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def mgal(g_si):
    """Convert an acceleration in m/s^2 to mGal."""
    return g_si / MGAL_TO_SI


def sphere_g(x, z, mass):
    """Vertical gravity of a point mass / homogeneous sphere, SI.

    x, z in metres (x horizontal offset, z depth of the centre), mass in kg.
    """
    return G_SI * mass * z / (x * x + z * z) ** 1.5


def cylinder_g(x, z, lam):
    """Vertical gravity of an infinite horizontal line mass / 2-D cylinder, SI.

    x, z in metres, lam = mass per unit length in kg/m (= pi R^2 drho).
    """
    return 2.0 * G_SI * lam * z / (x * x + z * z)


def half_width(x, g):
    """Half-width: the |x| at which g first falls to half of its peak."""
    peak = g.max()
    i = int(np.argmax(g))
    j = i
    while j < len(g) - 1 and g[j] > 0.5 * peak:
        j += 1
    x1, x2 = x[j - 1], x[j]
    y1, y2 = g[j - 1], g[j]
    return x1 + (0.5 * peak - y1) * (x2 - x1) / (y2 - y1)


def main():
    section("1. Sphere: peak, half-width, depth rule")
    drho_s = 300.0        # kg/m^3 density contrast (SYNTHETIC)
    radius_s = 500.0      # m
    depth_s = 1000.0      # m to the centre
    mass_s = (4.0 / 3.0) * np.pi * radius_s ** 3 * drho_s
    print(f"SYNTHETIC sphere: R = {radius_s:.0f} m, drho = {drho_s:.0f} kg/m^3, "
          f"z(centre) = {depth_s:.0f} m")
    print(f"  mass M = (4/3) pi R^3 drho = {mass_s:.4e} kg")
    x = np.linspace(-4000.0, 4000.0, 40001)
    gs = sphere_g(x, depth_s, mass_s)
    print(f"  peak gz at x = 0        = {mgal(gs.max()):.4f} mGal "
          f"({gs.max():.4e} m/s^2)")
    print(f"  gz at x = z             = {mgal(sphere_g(depth_s, depth_s, mass_s)):.4f} mGal")
    xh_s = half_width(x, gs)
    print(f"  half-width x_1/2        = {xh_s:.1f} m")
    print(f"  measured  x_1/2 / z     = {xh_s / depth_s:.6f}")
    print(f"  analytic  sqrt(2^(2/3)-1)= {np.sqrt(2.0 ** (2.0 / 3.0) - 1.0):.6f}")
    print(f"  -> depth rule z = x_1/2 / 0.766421 = {xh_s / 0.766421:.1f} m")

    section("2. Horizontal cylinder: peak, half-width, depth rule")
    drho_c = 300.0
    radius_c = 200.0
    depth_c = 500.0
    lam_c = np.pi * radius_c ** 2 * drho_c
    print(f"SYNTHETIC 2-D cylinder: R = {radius_c:.0f} m, drho = {drho_c:.0f} kg/m^3, "
          f"z(axis) = {depth_c:.0f} m")
    print(f"  line density lam = pi R^2 drho = {lam_c:.4e} kg/m")
    gc = cylinder_g(x, depth_c, lam_c)
    print(f"  peak gz at x = 0        = {mgal(gc.max()):.4f} mGal")
    xh_c = half_width(x, gc)
    print(f"  half-width x_1/2        = {xh_c:.1f} m")
    print(f"  measured  x_1/2 / z     = {xh_c / depth_c:.6f}   (analytic 1.000000)")
    print(f"  -> depth rule z = x_1/2    = {xh_c:.1f} m (no scaling factor)")

    section("3. Amplitude scaling with depth (measured log-log slopes)")
    depths = np.array([200.0, 400.0, 800.0, 1600.0, 3200.0])
    peaks_s = np.array([sphere_g(0.0, z, mass_s) for z in depths])
    peaks_c = np.array([cylinder_g(0.0, z, lam_c) for z in depths])
    print("     z (m)     sphere peak (mGal)   cylinder peak (mGal)")
    for z, ps, pc in zip(depths, peaks_s, peaks_c):
        print(f"  {z:8.0f}   {mgal(ps):18.5f}   {mgal(pc):20.5f}")
    slope_s = np.polyfit(np.log(depths), np.log(peaks_s), 1)[0]
    slope_c = np.polyfit(np.log(depths), np.log(peaks_c), 1)[0]
    print(f"  measured slope d ln(peak)/d ln(z): sphere {slope_s:+.4f}, "
          f"cylinder {slope_c:+.4f}")
    print("  -> sphere amplitude ~ z^-2 (excess mass fixed); "
          "cylinder amplitude ~ z^-1")

    section("4. Horizontal derivative: where the maximum sits")
    dx_s = np.gradient(gs, x)
    dx_c = np.gradient(gc, x)
    xm_s = abs(x[np.argmax(np.abs(dx_s))])
    xm_c = abs(x[np.argmax(np.abs(dx_c))])
    print(f"  sphere   : |dg/dx| max at |x| = {xm_s:.1f} m "
          f"-> |x|/z = {xm_s / depth_s:.4f} (analytic 0.5000)")
    print(f"  cylinder : |dg/dx| max at |x| = {xm_c:.1f} m "
          f"-> |x|/z = {xm_c / depth_c:.4f} (analytic 0.5774 = 1/sqrt(3))")
    print(f"  sphere   (dg/dx)_max = {mgal(np.abs(dx_s).max()):.5f} mGal/m")
    print(f"  cylinder (dg/dx)_max = {mgal(np.abs(dx_c).max()):.5f} mGal/m")

    section("5. Excess mass and the depth-amplitude trade-off")
    g0_si = 0.30 * MGAL_TO_SI       # a target peak of exactly 0.30 mGal
    print(f"Target peak gz(0) = 0.3000 mGal = {g0_si:.4e} m/s^2")
    print("Sphere family with drho = 300 kg/m^3 reproducing that ONE number:")
    print("     z (m)     M (kg)       R (m)     R/z     half-width (m)")
    for z in (500.0, 1000.0, 2000.0, 4000.0):
        m_req = g0_si * z * z / G_SI
        r_req = (3.0 * m_req / (4.0 * np.pi * drho_s)) ** (1.0 / 3.0)
        xh = z * 0.766421
        print(f"  {z:8.0f}   {m_req:.4e}   {r_req:8.1f}   {r_req / z:5.3f}   "
              f"{xh:12.1f}")
    print("  One number, four admissible bodies: the peak alone does not fix either")
    print("  depth or mass.  Only the SHAPE of the profile, or an independent")
    print("  constraint, breaks the ambiguity.")

    section("6. The cost of assuming the wrong body shape")
    z_wrong = xh_c / 0.766421
    print(f"A 2-D cylinder at z = {depth_c:.0f} m has x_1/2 = {xh_c:.1f} m.")
    print(f"Interpreted with the SPHERE rule it gives z = x_1/2/0.766421 "
          f"= {z_wrong:.1f} m,")
    print(f"a depth error of {100.0 * (z_wrong - depth_c) / depth_c:+.1f} % -- "
          f"before any noise or measurement error.")


if __name__ == "__main__":
    main()
