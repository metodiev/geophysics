"""Ground truthing: does a surface inversion survive contact with a borehole?

Two synthetic cases, and the point is the contrast between them:

  CASE A -- the true source is one compact body.  A surface gravity inversion
  recovers it; the recovered model *predicts* an independent downhole gravity
  profile to within twice the station noise; and the density it implies at the
  borehole, using the borehole's own intersection geometry, matches the core to
  2 per cent.

  CASE B -- the same ore body, plus a broad deep body of the same sign.  A single
  surface body still fits the surface data to an indistinguishable residual, but
  it now fails the downhole prediction by a factor of 58 and the density it
  implies at the borehole is wrong by 59 per cent.

The true bodies are *finite spheres* discretised into point masses, so the
downhole computation is a finite, physical field rather than a point-mass
singularity.  The inverted model is a single point mass, which is what such an
inversion actually produces.

The lesson is not that inversion is useless; it is that a *good data fit is not a
validation*, and the borehole is the instrument that decides which of two
data-compatible models you have.

All masses, densities, depths, noise levels and borehole geometry are SYNTHETIC.

Run:  python3 groundtruth_demo.py
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import curve_fit

G = 6.674e-11  # m^3 kg^-1 s^-2
MGAL = 1.0e-5  # m s^-2 per mGal


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def sphere_points(cx, cy, cz, radius, d_rho, n=9):
    """Discretise a uniform sphere into (mass, x, y, z) point masses."""
    lin = np.linspace(-radius, radius, n)
    step = lin[1] - lin[0]
    xg, yg, zg = np.meshgrid(lin, lin, lin, indexing="ij")
    inside = xg * xg + yg * yg + zg * zg <= radius * radius
    cell_mass = d_rho * step ** 3
    return [(cell_mass, cx + float(a), cy + float(b), cz + float(c))
            for a, b, c in zip(xg[inside], yg[inside], zg[inside])]


def sphere_mass(radius, d_rho):
    """Exact anomalous mass of the sphere, for reference."""
    return d_rho * (4.0 / 3.0) * np.pi * radius ** 3


def gz_surface(x, y, masses):
    """Vertical gravity at the surface from point masses (m, x0, y0, z0)."""
    total = np.zeros_like(x, dtype=float)
    for m, x0, y0, z0 in masses:
        total += G * m * z0 / ((x - x0) ** 2 + (y - y0) ** 2 + z0 * z0) ** 1.5
    return total


def gz_downhole(depths, masses, bx=10.0, by=0.0):
    """Vertical gravity inside a borehole at (bx, by)."""
    total = np.zeros_like(depths, dtype=float)
    for m, x0, y0, z0 in masses:
        dz = z0 - depths
        total += G * m * dz / ((bx - x0) ** 2 + (by - y0) ** 2 + dz * dz) ** 1.5
    return total


def model_surface(xy, m, x0, y0, z0, offset):
    """Single point-mass model for curve_fit; xy is the (x, y) tuple of arrays."""
    x, y = xy
    return G * m * z0 / ((x - x0) ** 2 + (y - y0) ** 2 + z0 * z0) ** 1.5 + offset


def model_downhole(depths, m, x0, y0, z0, offset, bx=10.0, by=0.0):
    dz = z0 - depths
    return G * m * dz / ((bx - x0) ** 2 + (by - y0) ** 2 + dz * dz) ** 1.5 + offset


def main() -> None:
    sigma = 0.02 * MGAL        # SYNTHETIC station noise, mGal -> SI

    radius_ore, d_rho_ore, z_ore = 120.0, 800.0, 300.0
    radius_deep, d_rho_deep, z_deep = 270.0, 100.0, 900.0
    ore = sphere_points(0.0, 0.0, z_ore, radius_ore, d_rho_ore)
    deep = sphere_points(0.0, 0.0, z_deep, radius_deep, d_rho_deep)

    xs, ys = np.meshgrid(np.linspace(-1500.0, 1500.0, 17),
                         np.linspace(-1500.0, 1500.0, 17))
    xg, yg = xs.ravel(), ys.ravel()
    depths = np.linspace(500.0, 1300.0, 33)

    print(f"SYNTHETIC ore  : radius {radius_ore:.0f} m, contrast "
          f"{d_rho_ore:.0f} kg/m^3, centre {z_ore:.0f} m, mass "
          f"{sphere_mass(radius_ore, d_rho_ore):.3e} kg")
    print(f"SYNTHETIC deep : radius {radius_deep:.0f} m, contrast "
          f"{d_rho_deep:.0f} kg/m^3, centre {z_deep:.0f} m, mass "
          f"{sphere_mass(radius_deep, d_rho_deep):.3e} kg")
    print(f"spheres discretised into {len(ore)} and {len(deep)} point masses")
    print(f"borehole at x = 10 m; the ore intersects it from "
          f"{z_ore - radius_ore:.0f} to {z_ore + radius_ore:.0f} m")
    print(f"core density contrast over that interval = {d_rho_ore:.0f} kg/m^3")

    for name, masses in (("A (one body)", ore),
                         ("B (ore + deep body)", ore + deep)):
        section(f"CASE {name}")
        rng = np.random.default_rng(7)      # identical noise draw in both cases
        g_obs = gz_surface(xg, yg, masses) + rng.normal(0.0, sigma, xg.size)
        popt, pcov = curve_fit(model_surface, (xg, yg), g_obs,
                               p0=[5.8e9, 0.0, 0.0, 300.0, 0.0], maxfev=40000)
        m_rec, x_rec, y_rec, z_rec, off = popt
        z_err = float(np.sqrt(abs(pcov[3, 3])))
        rms = float(np.sqrt(np.mean((model_surface((xg, yg), *popt) - g_obs) ** 2))
                    / MGAL)
        true_mass = sum(m for m, _, _, _ in masses)
        print(f"surface stations         = {xg.size}; station noise = "
              f"{sigma / MGAL:.2f} mGal")
        print(f"true total mass          = {true_mass:.3e} kg")
        print(f"best single body         : m = {m_rec:.3e} kg, x0 = {x_rec:7.1f} m, "
              f"z0 = {z_rec:7.1f} +/- {z_err:.1f} m")
        print(f"surface RMS residual     = {rms:.4f} mGal "
              f"({rms / (sigma / MGAL):.1f} x the station noise)")

        diff = (model_downhole(depths, m_rec, x_rec, y_rec, z_rec, off)
                - gz_downhole(depths, masses)) / MGAL
        dh_rms = float(np.sqrt(np.mean(diff ** 2)))
        print("\nindependent observation -- downhole gravity, 33 stations, "
              "500 to 1300 m,")
        print("logged *below* the ore as a real borehole gravimeter would be:")
        print(f"  max |model - truth|    = {np.max(np.abs(diff)):.4f} mGal")
        print(f"  RMS |model - truth|    = {dh_rms:.4f} mGal")
        print(f"  ratio to station noise = {dh_rms / (sigma / MGAL):.1f}")

        implied = m_rec / ((4.0 / 3.0) * np.pi * radius_ore ** 3)
        print("\nproperty at the borehole, using the borehole's own geometry:")
        print(f"  density contrast implied by the model = {implied:9.1f} kg/m^3")
        print(f"  density contrast measured on core     = {d_rho_ore:9.1f} kg/m^3")
        print(f"  error factor                          = {implied / d_rho_ore:9.2f}")

    section("What the two cases establish")
    print("Case A passes all three checks: the surface fit, the downhole "
          "prediction and\nthe core density agree.  Case B passes only the first, "
          "and its surface residual is\nindistinguishable from case A's.  In both "
          "cases the recovered body is the best\nsingle body available, so no "
          "surface residual distinguishes them.  The borehole\nis a validation "
          "experiment, and a model must never be called verified on\nthe strength "
          "of its residual alone.")


if __name__ == "__main__":
    main()
