#!/usr/bin/env python3
"""Beginner project 3: gravity through a spherically layered Earth.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python layered_earth_gravity_demo.py

Everything here is SYNTHETIC.  The layering and densities are chosen teaching
values, not a published Earth model; the shell-theorem arithmetic is exact for
the model as specified.

Sections
--------
1. The layered model: radius, density and enclosed mass for each layer.
2. g(r) from the shell theorem, layer by layer, with the maximum located.
3. Comparison with a uniform sphere of the same mass and radius.
4. Surface gravity, total mass and the sensitivity to a crustal density change.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

GRAV_CONST = 6.67430e-11     # m^3 kg^-1 s^-2

# --- SYNTHETIC layered model: (name, inner radius, outer radius, density) ----
# Radii in m, densities in kg/m^3.  Chosen values, not a published model.
LAYERS = (
    ("inner core",   0.0,       1.2215e6, 13090.0),
    ("outer core",   1.2215e6,  3.4800e6, 11000.0),
    ("lower mantle", 3.4800e6,  5.7010e6,  4900.0),
    ("upper mantle", 5.7010e6,  6.3466e6,  3500.0),
    ("crust",        6.3466e6,  6.3710e6,  2800.0),
)
R_SURFACE = LAYERS[-1][2]


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def shell_mass(r_in, r_out, rho):
    """Mass of a uniform spherical shell, kg."""
    return 4.0 / 3.0 * np.pi * rho * (r_out ** 3 - r_in ** 3)


def mass_enclosed(r, layers):
    """Mass inside radius r for the layered model, kg."""
    total = 0.0
    for _, r_in, r_out, rho in layers:
        if r <= r_in:
            continue
        top = min(r, r_out)
        total += shell_mass(r_in, top, rho)
    return total


def g_at(r, layers):
    """Gravitational acceleration at radius r, m/s^2 (shell theorem)."""
    if r == 0.0:
        return 0.0
    return GRAV_CONST * mass_enclosed(r, layers) / r ** 2


def main():
    section("1. The layered model")
    print("SYNTHETIC layered Earth - chosen teaching values")
    print(f"{'layer':<14}{'r_in (km)':>12}{'r_out (km)':>12}"
          f"{'rho (kg/m^3)':>15}{'mass (kg)':>14}")
    masses = []
    for name, r_in, r_out, rho in LAYERS:
        m = shell_mass(r_in, r_out, rho)
        masses.append(m)
        print(f"{name:<14}{r_in / 1e3:>12.1f}{r_out / 1e3:>12.1f}"
              f"{rho:>15.0f}{m:>14.4e}")
    total_mass = sum(masses)
    print(f"{'total':<14}{'':>12}{R_SURFACE / 1e3:>12.1f}{'':>15}{total_mass:>14.4e}")
    for (name, _, _, _), m in zip(LAYERS, masses):
        print(f"  {name:<14} contributes {m / total_mass * 100:5.1f}% of the mass")

    section("2. g(r) from the shell theorem")
    print(f"{'location':<22}{'r (km)':>10}{'M enclosed (kg)':>17}{'g (m/s^2)':>12}")
    radii = [0.0] + [r_in for _, r_in, _, _ in LAYERS if r_in > 0] + [R_SURFACE]
    names = ["centre"]
    for name, r_in, r_out, _ in LAYERS:
        names.append(f"top of {name}")
    for name, r in zip(names, radii):
        print(f"{name:<22}{r / 1e3:>10.1f}{mass_enclosed(r, LAYERS):>17.4e}"
              f"{g_at(r, LAYERS):>12.4f}")
    r_grid = np.linspace(0.0, R_SURFACE, 400)
    g_grid = np.array([g_at(r, LAYERS) for r in r_grid])
    i_max = int(np.argmax(g_grid))
    print(f"  maximum g = {g_grid[i_max]:.4f} m/s^2 at r = "
          f"{r_grid[i_max] / 1e3:.1f} km (the core-mantle boundary region)")
    print(f"  g at the surface = {g_at(R_SURFACE, LAYERS):.4f} m/s^2")
    print(f"  g increases outward through the core because rho*r grows faster")
    print(f"  than r^2: at r = 1000 km, g = {g_at(1.0e6, LAYERS):.4f} m/s^2")

    section("3. Comparison with a uniform sphere")
    rho_mean = total_mass / (4.0 / 3.0 * np.pi * R_SURFACE ** 3)
    g_uniform_surface = GRAV_CONST * total_mass / R_SURFACE ** 2
    g_uniform_interior = np.array([GRAV_CONST * (4.0 / 3.0) * np.pi * rho_mean * r
                                   for r in r_grid])
    print(f"  mean density 3M/(4 pi R^3) = {rho_mean:.1f} kg/m^3")
    print(f"  uniform-sphere surface g (same M, R) = {g_uniform_surface:.4f} m/s^2")
    print(f"  layered model surface g            = {g_at(R_SURFACE, LAYERS):.4f} m/s^2")
    print(f"  surface difference = "
          f"{(g_at(R_SURFACE, LAYERS) - g_uniform_surface) / g_uniform_surface * 100:+.2f}%")
    i_cmb = int(np.argmin(np.abs(r_grid - 3.48e6)))
    print(f"  at the core-mantle boundary (r = 3480 km): layered g = "
          f"{g_grid[i_cmb]:.4f}, uniform g = {g_uniform_interior[i_cmb]:.4f} m/s^2")
    print("  -> the uniform model gets the surface value roughly right and the")
    print("     interior badly wrong; g(r) is a probe of the density profile.")

    section("4. Total mass and sensitivity to a crustal density change")
    print(f"  total mass = {total_mass:.4e} kg")
    print(f"  surface g  = {g_at(R_SURFACE, LAYERS):.4f} m/s^2 "
          f"(reference value about 9.82 m/s^2)")
    for rho_c in (2800.0, 3000.0):
        layers = LAYERS[:-1] + (("crust", LAYERS[-1][1], LAYERS[-1][2], rho_c),)
        g_new = g_at(R_SURFACE, layers)
        print(f"  crust density {rho_c:.0f} kg/m^3 -> surface g = {g_new:.6f} m/s^2 "
              f"({(g_new - g_at(R_SURFACE, LAYERS)) / g_at(R_SURFACE, LAYERS) * 1e6:+.2f} ppm)")
    print("  -> a 200 kg/m^3 change in the WHOLE crust moves surface gravity by")
    print("     about 408 mGal, because it changes the enclosed mass; a local")
    print("     density change moves far less. Compare with the free-air")
    print("     gradient of 0.3083 mGal/m from project 1.")
    rho_draw = 2800.0 + 100.0 * RNG.standard_normal(400)   # SYNTHETIC prior, kg/m^3
    g_draw = np.array([
        g_at(R_SURFACE, LAYERS[:-1] + (("crust", LAYERS[-1][1], LAYERS[-1][2], rc),))
        for rc in rho_draw
    ])
    print(f"  Monte Carlo over crust density 2800 +/- 100 kg/m^3 (400 draws):")
    print(f"    surface g = {g_draw.mean():.6f} +/- {g_draw.std(ddof=1):.6f} m/s^2 "
          f"(1 s.d.)")
    print(f"    scatter in mGal = {g_draw.std(ddof=1) / 1e-5:.2f} mGal")


if __name__ == "__main__":
    main()
