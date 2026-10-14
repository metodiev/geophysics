#!/usr/bin/env python3
"""Closed-form gravity anomalies for the sphere, the 2-D cylinder, the infinite
sheet, the semi-infinite sheet (fault step) and the 2-D rectangle (dyke), each
checked against an independent numerical integration.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simple_body_formulas_demo.py

All models and data in this module are SYNTHETIC.  The bodies are chosen
teaching shapes with chosen densities.

Contents
--------
1. The closed forms, evaluated on a profile and printed in mGal.
2. Independent check: the 2-D rectangle closed form versus a double numerical
   integral over the same cross-section.
3. Limits: rectangle -> infinite sheet; rectangle -> semi-infinite sheet;
   sphere -> point mass.
4. Half-width rules and derivative depth rules for each body.
5. Sensitivity of the anomaly to each parameter (measured partial derivatives).
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_SI = 6.67430e-11
MGAL_TO_SI = 1.0e-5


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def mgal(g_si):
    return g_si / MGAL_TO_SI


def sphere_g(x, z, drho, radius):
    """Homogeneous sphere of density contrast drho, radius R, centre at depth z."""
    mass = (4.0 / 3.0) * np.pi * radius ** 3 * drho
    return G_SI * mass * z / (x * x + z * z) ** 1.5


def cylinder_g(x, z, drho, radius):
    """Infinite horizontal cylinder (2-D), axis at depth z, radius R.

    Returns the anomaly per unit length along the strike.
    """
    lam = np.pi * radius ** 2 * drho
    return 2.0 * G_SI * lam * z / (x * x + z * z)


def slab_g(drho, thickness):
    """Infinite horizontal sheet (Bouguer slab): independent of depth."""
    return 2.0 * np.pi * G_SI * drho * thickness


def halfsheet_g(x, z1, z2, drho):
    """Semi-infinite sheet of finite thickness: top z1, bottom z2, filling x > 0.

    Integrating the thin-sheet kernel 2 G drho (pi/2 + arctan(x/z)) over
    z in [z1, z2] gives exactly

        gz = 2 G drho [ (pi/2)(z2-z1) + z2 arctan(x/z2) - z1 arctan(x/z1)
                        + (x/2) ln((x^2+z2^2)/(x^2+z1^2)) ],

    which goes to 0 as x -> -inf, to the full slab 2 pi G drho (z2-z1) as
    x -> +inf, and is exactly half the slab at x = 0 whatever the thickness.
    """
    th = z2 - z1
    return 2.0 * G_SI * drho * (
        0.5 * np.pi * th
        + z2 * np.arctan(x / z2) - z1 * np.arctan(x / z1)
        + 0.5 * x * np.log((x * x + z2 * z2) / (x * x + z1 * z1))
    )


def _P(u, a):
    """Antiderivative helper: d/du P(u,a) = ln(u^2 + a^2)."""
    return u * np.log(u * u + a * a) - 2.0 * u + 2.0 * a * np.arctan(u / a)


def rect2d_g(x, x1, x2, z1, z2, drho):
    """Vertical gravity of a 2-D rectangle, infinite along strike.

    Cross-section x in [x1, x2], depth in [z1, z2].  Derived from
    gz = 2 G drho * integral_x integral_z  z'/((x-x')^2+z'^2) dz' dx':

        gz = 2 G drho [ J(x-x1) - J(x-x2) ],  J(u) = (P(u,z2) - P(u,z1))/2.
    """
    j1 = 0.5 * (_P(x - x1, z2) - _P(x - x1, z1))
    j2 = 0.5 * (_P(x - x2, z2) - _P(x - x2, z1))
    return 2.0 * G_SI * drho * (j1 - j2)


def rect2d_numeric(x, x1, x2, z1, z2, drho, order=220):
    """Same quantity by Gauss-Legendre quadrature of the defining double integral."""
    tg, wg = np.polynomial.legendre.leggauss(order)
    xp = 0.5 * (x2 - x1) * tg + 0.5 * (x2 + x1)
    zp = 0.5 * (z2 - z1) * tg + 0.5 * (z2 + z1)
    wx = 0.5 * (x2 - x1) * wg
    wz = 0.5 * (z2 - z1) * wg
    xx = x[:, None, None] - xp[None, :, None]
    zz = zp[None, None, :]
    f = zz / (xx ** 2 + zz ** 2)          # shape (n_obs, n_x, n_z)
    return 2.0 * G_SI * drho * np.einsum("a,iab,b->i", wx, f, wz)


def half_width(x, g):
    """Half-width of a single-peaked profile by linear interpolation."""
    peak = g.max()
    i = int(np.argmax(g))
    j = i
    while j < len(g) - 1 and g[j] > 0.5 * peak:
        j += 1
    return x[j - 1] + (0.5 * peak - g[j - 1]) * (x[j] - x[j - 1]) / (g[j] - g[j - 1])


def main():
    x = np.linspace(-5000.0, 5000.0, 20001)
    drho = 300.0
    z1, z2 = 500.0, 700.0

    section("1. Closed forms on a profile (all SYNTHETIC)")
    print(f"density contrast drho = {drho:.0f} kg/m^3 throughout")
    gs = sphere_g(x, 1000.0, drho, 500.0)
    gc = cylinder_g(x, 500.0, drho, 200.0)
    gb = np.full_like(x, slab_g(drho, 200.0))
    gh = halfsheet_g(x, z1, z2, drho)
    gd = rect2d_g(x, -250.0, 250.0, 300.0, 2000.0, drho)
    print("     x (m)   sphere(z=1km)  cylinder(z=0.5km)   slab(t=200m)  "
          "half-sheet(t=200m)  dyke(500x1700m)")
    for xv in (-3000.0, -1000.0, -250.0, 0.0, 250.0, 1000.0, 3000.0):
        i = int(np.argmin(np.abs(x - xv)))
        print(f"  {xv:8.0f}   {mgal(gs[i]):13.4f}   {mgal(gc[i]):16.4f}   "
              f"{mgal(gb[i]):12.4f}   {mgal(gh[i]):17.4f}   {mgal(gd[i]):15.4f}")
    print(f"  slab closed form: 2 pi G drho t = {mgal(slab_g(drho, 200.0)):.4f} mGal, "
          "independent of depth")

    section("2. Independent check: rectangle closed form vs double integral")
    for (zz1, zz2, w) in ((200.0, 1000.0, 400.0), (300.0, 5000.0, 1000.0)):
        xs = np.array([0.0, 250.0, 1000.0, 3000.0])
        closed = rect2d_g(xs, -w / 2, w / 2, zz1, zz2, drho)
        numeric = rect2d_numeric(xs, -w / 2, w / 2, zz1, zz2, drho)
        print(f"  rectangle width {w:.0f} m, depth {zz1:.0f}-{zz2:.0f} m:")
        for xv, a, b in zip(xs, closed, numeric):
            print(f"    x = {xv:7.0f} m   closed {mgal(a):10.5f}   "
                  f"quadrature {mgal(b):10.5f}   diff {abs(a - b):.3e} m/s^2")

    section("3. Limits")
    wide = rect2d_g(np.array([0.0]), -1.0e6, 1.0e6, 500.0, 700.0, drho)[0]
    print("  rectangle 2 km wide x 200 m thick at depth 500-700 m, observed at x = 0:")
    print(f"    closed form    = {mgal(wide):.5f} mGal")
    print(f"    infinite slab  = {mgal(slab_g(drho, 200.0)):.5f} mGal")
    print(f"    ratio          = {wide / slab_g(drho, 200.0):.6f}")
    edge = rect2d_g(np.array([0.0, -3000.0, 3000.0]), 0.0, 1.0e7, z1, z2, drho)
    hs = halfsheet_g(np.array([0.0, -3000.0, 3000.0]), z1, z2, drho)
    print("  rectangle from x = 0 to x -> +infinity (edge over x = 0), "
          "thickness 200 m:")
    for label, a, b in (("edge  x=    0", edge[0], hs[0]),
                        ("left  x=-3000", edge[1], hs[1]),
                        ("right x=+3000", edge[2], hs[2])):
        print(f"    {label}: closed form {mgal(a):8.5f}   semi-infinite sheet "
              f"{mgal(b):8.5f}   diff {abs(a - b):.2e} m/s^2")
    far = sphere_g(np.array([0.0]), 100000.0, drho, 500.0)[0]
    mass = (4.0 / 3.0) * np.pi * 500.0 ** 3 * drho
    print(f"  sphere at 100 km vs point mass G M / z^2: {mgal(far):.6f} vs "
          f"{mgal(G_SI * mass / 100000.0 ** 2):.6f} mGal")

    section("4. Half-width rules and derivative depth rules")
    for name, g, z_true, factor in (
        ("sphere   (z = centre)", sphere_g(x, 1000.0, drho, 500.0), 1000.0, 0.766421),
        ("cylinder (z = axis)  ", cylinder_g(x, 500.0, drho, 200.0), 500.0, 1.0),
    ):
        xh = half_width(x, g)
        print(f"  {name}: x_1/2 = {xh:8.1f} m -> z = {xh / factor:8.1f} m "
              f"(true {z_true:.0f} m)")
    print("  semi-infinite sheet (top 500 m, bottom 700 m, edge at x = 0):")
    edge0 = halfsheet_g(np.array([0.0]), z1, z2, drho)[0]
    print(f"    gz at the edge x = 0 = {mgal(edge0):.5f} mGal vs half the full "
          f"slab {mgal(0.5 * slab_g(drho, z2 - z1)):.5f} mGal: identical, so the")
    print("    50 % point sits exactly over the edge whatever the thickness.")
    dstep = np.gradient(gh, x)
    xm = abs(x[np.argmax(np.abs(dstep))])
    dxmax = np.abs(dstep).max()
    t_th = z2 - z1
    print(f"    |dg/dx| peaks at x = {xm:.1f} m with value {mgal(dxmax):.4f} mGal/m.")
    print("    For this geometry (dg/dx)max = 2 G drho ln(z2/z1), so with the "
          "thickness known")
    lnratio = dxmax / (2.0 * G_SI * drho)
    z1_rec = t_th / (np.exp(lnratio) - 1.0)
    print(f"    ln(z2/z1) = {lnratio:.5f} -> z1 = t/(exp(ln z2/z1) - 1) "
          f"= {z1_rec:.1f} m (true {z1:.1f} m).")

    section("5. Sensitivity to each parameter")
    base = cylinder_g(np.array([0.0]), 500.0, drho, 200.0)[0]
    d_rho = cylinder_g(np.array([0.0]), 500.0, drho * 1.01, 200.0)[0]
    d_r = cylinder_g(np.array([0.0]), 500.0, drho, 200.0 * 1.01)[0]
    d_z = base - cylinder_g(np.array([0.0]), 500.0 * 1.01, drho, 200.0)[0]
    print(f"  cylinder on-axis anomaly = {mgal(base):.5f} mGal")
    print(f"  +1 % in drho -> {100.0 * (d_rho - base) / base:+.2f} % in gz (linear)")
    print(f"  +1 % in R    -> {100.0 * (d_r - base) / base:+.2f} % in gz (~2x)")
    print(f"  +1 % in z    -> {100.0 * d_z / base:+.2f} % in gz (gz ~ 1/z)")
    print("  Amplitude is twice as sensitive to radius as to density for a 2-D body;")
    print("  the profile WIDTH is the only part that speaks about depth.")


if __name__ == "__main__":
    main()
