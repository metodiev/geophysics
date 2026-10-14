#!/usr/bin/env python3
"""Intermediate project 2: the gravity anomaly of simple bodies, the depth rules
that follow from their shapes, and the non-uniqueness that survives.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simple_gravity_model_demo.py

Everything here is SYNTHETIC.  The body geometries and density contrasts are
chosen teaching values; the forward formulas are exact for the idealised shapes.

Sections
--------
1. Three idealised bodies and their anomaly amplitudes.
2. Depth from half-width: the shape of the curve, not its size.
3. Why the Bouguer slab has no depth information.
4. Non-uniqueness: amplitude alone, and what breaks it.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

GRAV_CONST = 6.67430e-11      # m^3 kg^-1 s^-2
MGAL = 1.0e-5                 # m/s^2 per mGal

D_RHO = 500.0                 # density contrast, kg/m^3 (SYNTHETIC)
R_BODY = 2.0e3                # sphere or cylinder radius, m
Z_DEPTH = 5.0e3               # depth to centre or axis, m
SLAB_T = 500.0                # slab thickness, m


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def g_sphere(x, rho, radius, z):
    """Vertical gravity of a sphere of radius `radius` centred at depth z."""
    mass = 4.0 / 3.0 * np.pi * rho * radius ** 3
    return GRAV_CONST * mass * z / (x ** 2 + z ** 2) ** 1.5


def g_cylinder(x, rho, radius, z):
    """Vertical gravity of an infinite horizontal cylinder (2-D)."""
    return 2.0 * np.pi * GRAV_CONST * rho * radius ** 2 * z / (x ** 2 + z ** 2)


def g_slab(rho, thickness):
    """Bouguer slab: independent of depth.  Returns a scalar."""
    return 2.0 * np.pi * GRAV_CONST * rho * thickness


def half_width(x, g):
    """Distance at which the anomaly falls to half its maximum, by interpolation."""
    g_max = g.max()
    mask = x >= 0.0
    xr, gr = x[mask], g[mask]          # gr decreasing in xr
    x_edge = float(np.interp(0.5 * g_max, gr[::-1], xr[::-1]))
    return x_edge, g_max


def main():
    section("1. Three idealised bodies")
    x = np.arange(-20.0e3, 20.0e3 + 1.0, 100.0)
    gs = g_sphere(x, D_RHO, R_BODY, Z_DEPTH)
    gc = g_cylinder(x, D_RHO, R_BODY, Z_DEPTH)
    slab = g_slab(D_RHO, SLAB_T)
    print(f"SYNTHETIC bodies: density contrast {D_RHO:.0f} kg/m^3, "
          f"radius {R_BODY / 1e3:.1f} km, depth {Z_DEPTH / 1e3:.1f} km")
    print(f"  sphere   peak = {gs.max() / MGAL:.4f} mGal "
          f"(exact 4/3 pi G rho R^3 / z^2 = "
          f"{4 / 3 * np.pi * GRAV_CONST * D_RHO * R_BODY ** 3 / Z_DEPTH ** 2 / MGAL:.4f})")
    print(f"  cylinder peak = {gc.max() / MGAL:.4f} mGal "
          f"(exact 2 pi G rho R^2 / z = "
          f"{2 * np.pi * GRAV_CONST * D_RHO * R_BODY ** 2 / Z_DEPTH / MGAL:.4f})")
    print(f"  Bouguer slab  = {slab / MGAL:.4f} mGal "
          f"(2 pi G rho t, thickness {SLAB_T:.0f} m)")
    print(f"  for the same R, z and rho the cylinder is "
          f"{gc.max() / gs.max():.2f} times the sphere: a 2-D body looks bigger")

    section("2. Depth from half-width")
    x_s, g_max_s = half_width(x, gs)
    x_c, g_max_c = half_width(x, gc)
    print(f"{'body':<12}{'x_1/2 (km)':>12}{'z from x_1/2 (km)':>20}{'true z (km)':>13}")
    print(f"{'sphere':<12}{x_s / 1e3:>12.3f}{1.3048 * x_s / 1e3:>20.3f}"
          f"{Z_DEPTH / 1e3:>13.1f}")
    print(f"{'cylinder':<12}{x_c / 1e3:>12.3f}{x_c / 1e3:>20.3f}"
          f"{Z_DEPTH / 1e3:>13.1f}")
    print(f"  sphere rule   z = x_1/2 / sqrt(2^(2/3) - 1) = 1.3048 x_1/2")
    print(f"  exact sphere x_1/2 = z sqrt(2^(2/3)-1) = "
          f"{Z_DEPTH * np.sqrt(2 ** (2 / 3) - 1) / 1e3:.3f} km")
    print(f"  cylinder rule z = x_1/2 exactly (the 2-D anomaly has a Lorentzian "
          f"shape)")

    section("3. The Bouguer slab has no depth information")
    for z_slab in (500.0, 2000.0, 5000.0):
        print(f"  slab at {z_slab:>6.0f} m depth: g = {g_slab(D_RHO, SLAB_T) / MGAL:.4f} mGal")
    print("  -> identical for every depth: a sheet of infinite extent produces the")
    print("     same field anywhere above it.  Depth must come from the EDGES.")

    section("4. Non-uniqueness: amplitude alone, and what breaks it")
    target = gs.max()
    print(f"  holding the sphere's peak at {target / MGAL:.4f} mGal, "
          f"the pairs (z, R) that match:")
    print(f"{'z (km)':>8}{'R (km)':>10}{'x_1/2 (km)':>13}{'z from x_1/2 (km)':>20}")
    for z_try in (3.0e3, 4.0e3, 5.0e3, 6.0e3, 7.0e3):
        r_try = (target * z_try ** 2 / (GRAV_CONST * 4.0 / 3.0 * np.pi * D_RHO)) ** (1.0 / 3.0)
        g_try = g_sphere(x, D_RHO, r_try, z_try)
        x_h, _ = half_width(x, g_try)
        print(f"{z_try / 1e3:>8.1f}{r_try / 1e3:>10.3f}{x_h / 1e3:>13.3f}"
              f"{1.3048 * x_h / 1e3:>20.3f}")
    print("  -> the amplitude is degenerate in (z, R); the half-width is not.")
    print("     A second, independent constraint - the half-width, a borehole, or")
    print("     a second field - removes the degeneracy that the peak leaves.")


if __name__ == "__main__":
    main()
