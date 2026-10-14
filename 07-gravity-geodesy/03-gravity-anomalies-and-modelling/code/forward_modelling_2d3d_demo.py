#!/usr/bin/env python3
"""Forward modelling in 2-D and 3-D: the closed-form rectangular prism, its
verification against a numerical triple integral, its limits (point mass, 2-D
body), and the discretisation error when a smooth body is voxelised.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python forward_modelling_2d3d_demo.py

All models and data in this module are SYNTHETIC.  The prisms, densities and
stations are chosen teaching quantities.

Contents
--------
1. The prism closed form versus a Gauss-Legendre triple integral.
2. Far field: prism -> point mass.
3. Long strike: 3-D prism -> 2-D formula (per unit length).
4. Voxelising a sphere: measured discretisation error versus voxel size.
5. Superposition of two prisms and the density-geometry trade-off.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_SI = 6.67430e-11
MGAL_TO_SI = 1.0e-5


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def mgal(g_si):
    return g_si / MGAL_TO_SI


def prism_gz(obs, prism, rho):
    """Vertical gravity of a homogeneous rectangular prism (Nagy's formula).

    obs   : (n, 3) observation points (x, y, 0); the surface is z = 0 with z
            positive downwards.
    prism : (x1, x2, y1, y2, z1, z2), z downward, z1 < z2, z1 > 0.
    rho   : density contrast in kg/m^3.

    Returns the anomaly in m/s^2 (positive downwards).
    """
    x1, x2, y1, y2, z1, z2 = prism
    obs = np.atleast_2d(obs)
    total = np.zeros(obs.shape[0])
    for i, xb in enumerate((x1, x2)):
        for j, yb in enumerate((y1, y2)):
            for k, zb in enumerate((z1, z2)):
                x = obs[:, 0] - xb
                y = obs[:, 1] - yb
                z = zb                        # depth of the face below obs
                r = np.sqrt(x * x + y * y + z * z)
                term = (x * np.log(y + r) + y * np.log(x + r)
                        - z * np.arctan2(x * y, z * r))
                total += ((-1.0) ** (i + j + k)) * term
    return G_SI * rho * total


def prism_gz_numeric(obs, prism, rho, order=40):
    """Same anomaly by Gauss-Legendre quadrature of  G rho * z' / |r'|^3 dV."""
    x1, x2, y1, y2, z1, z2 = prism
    tg, wg = np.polynomial.legendre.leggauss(order)

    def nodes(a, b):
        return 0.5 * (b - a) * tg + 0.5 * (b + a), 0.5 * (b - a) * wg

    px, wx = nodes(x1, x2)
    py, wy = nodes(y1, y2)
    pz, wz = nodes(z1, z2)
    obs = np.atleast_2d(obs)
    dx = obs[:, 0, None, None, None] - px[None, :, None, None]
    dy = obs[:, 1, None, None, None] - py[None, None, :, None]
    dz = pz[None, None, None, :]
    r3 = (dx ** 2 + dy ** 2 + dz ** 2) ** 1.5
    return G_SI * rho * np.einsum("a,b,c,iabc->i", wx, wy, wz, dz / r3)


def _P(u, a):
    return u * np.log(u * u + a * a) - 2.0 * u + 2.0 * a * np.arctan(u / a)


def rect2d_g(x, x1, x2, z1, z2, drho):
    """Vertical gravity per unit strike length of a 2-D rectangle (m/s^2)."""
    j1 = 0.5 * (_P(x - x1, z2) - _P(x - x1, z1))
    j2 = 0.5 * (_P(x - x2, z2) - _P(x - x2, z1))
    return 2.0 * G_SI * drho * (j1 - j2)


def sphere_prisms(radius, depth, drho, voxel):
    """Voxelise a sphere (centre at x = y = 0, depth `depth`) with cubes."""
    n = int(np.ceil(2.0 * radius / voxel))
    centres = (np.arange(n) - (n - 1) / 2.0) * voxel
    out = []
    for cx in centres:
        for cy in centres:
            for cz in centres:
                if cx ** 2 + cy ** 2 + cz ** 2 <= radius ** 2:
                    out.append((cx - voxel / 2, cx + voxel / 2,
                                cy - voxel / 2, cy + voxel / 2,
                                depth + cz - voxel / 2, depth + cz + voxel / 2))
    return out


def main():
    section("1. Prism closed form vs a triple numerical integral")
    prism = (-600.0, -200.0, -400.0, 400.0, 150.0, 800.0)
    rho = 400.0
    obs = np.array([[0.0, 0.0, 0.0], [-800.0, 0.0, 0.0],
                    [-400.0, 0.0, 0.0], [0.0, 1200.0, 0.0]])
    closed = prism_gz(obs, prism, rho)
    numeric = prism_gz_numeric(obs, prism, rho, order=36)
    print(f"SYNTHETIC prism {prism} m, rho = {rho:.0f} kg/m^3")
    for o, a, b in zip(obs, closed, numeric):
        print(f"  obs ({o[0]:7.0f},{o[1]:6.0f})  closed {mgal(a):10.5f}  "
              f"quadrature {mgal(b):10.5f}  diff {abs(a - b):.2e} m/s^2")

    section("2. Far field: prism -> point mass")
    far = np.array([[2.0e5, 0.0, 0.0], [5.0e5, 0.0, 0.0]])
    vol = (prism[1] - prism[0]) * (prism[3] - prism[2]) * (prism[5] - prism[4])
    mass = rho * vol
    for o, a in zip(far, prism_gz(far, prism, rho)):
        xx, yy = o[0], o[1]
        zc = 0.5 * (prism[4] + prism[5])
        xc = 0.5 * (prism[0] + prism[1])
        yc = 0.5 * (prism[2] + prism[3])
        r = np.sqrt((xx - xc) ** 2 + (yy - yc) ** 2 + zc ** 2)
        pm = G_SI * mass * zc / r ** 3
        print(f"  obs ({xx:.0e},{yy:.0f}): prism {mgal(a):.6e}  point mass "
              f"{mgal(pm):.6e} mGal  ratio {a / pm:.6f}")

    section("3. Long strike: 3-D prism -> 2-D formula")
    x = np.array([-600.0, 0.0, 600.0])
    obs = np.column_stack([x, np.zeros_like(x), np.zeros_like(x)])
    g2 = rect2d_g(x, prism[0], prism[1], prism[4], prism[5], rho)
    for strike in (2.0e3, 2.0e4, 2.0e5, 2.0e6):
        p = (prism[0], prism[1], -strike / 2, strike / 2, prism[4], prism[5])
        g3 = prism_gz(obs, p, rho)
        print(f"  strike length {strike:.0e} m:")
        for xv, a, b in zip(x, g3, g2):
            print(f"    x = {xv:7.0f} m   g3D = {mgal(a):10.5f}   "
                  f"2-D = {mgal(b):10.5f} mGal   ratio {a / b:.5f}")

    section("4. Voxelising a sphere: discretisation error vs voxel size")
    radius, depth = 500.0, 1200.0
    xpro = np.linspace(-3000.0, 3000.0, 25)
    obs = np.column_stack([xpro, np.zeros_like(xpro), np.zeros_like(xpro)])
    mass = (4.0 / 3.0) * np.pi * radius ** 3 * rho
    vol_true = (4.0 / 3.0) * np.pi * radius ** 3
    peak_true = mgal(G_SI * mass / depth ** 2)
    g_true = G_SI * mass * depth / (xpro ** 2 + depth ** 2) ** 1.5
    print(f"  SYNTHETIC sphere R = {radius:.0f} m, centre depth {depth:.0f} m, "
          f"rho = {rho:.0f} kg/m^3, analytic peak {peak_true:.5f} mGal")
    print("   voxel(m)  cells  volume err(%)  rms err naive(mGal)  "
          "rms err mass-matched(mGal)  mass-matched / peak(%)")
    for voxel in (400.0, 250.0, 150.0, 100.0, 60.0):
        cells = sphere_prisms(radius, depth, rho, voxel)
        g = np.zeros_like(xpro)
        for c in cells:
            g += prism_gz(obs, c, rho)
        vol_model = len(cells) * voxel ** 3
        rho_match = rho * vol_true / vol_model
        gm = np.zeros_like(xpro)
        for c in cells:
            gm += prism_gz(obs, c, rho_match)
        rms = mgal(np.sqrt(np.mean((g - g_true) ** 2)))
        rmsm = mgal(np.sqrt(np.mean((gm - g_true) ** 2)))
        print(f"  {voxel:9.0f}  {len(cells):6d}  "
              f"{100.0 * (vol_model - vol_true) / vol_true:13.2f}  "
              f"{rms:19.5f}  {rmsm:25.5f}  {100.0 * rmsm / peak_true:20.3f}")
    print("  The analytic sphere is exact.  The voxel error is a discretisation")
    print("  artefact: with cube voxels it is dominated by the volume they")
    print("  over-count, which is why it collapses only once the discrete model is")
    print("  mass-matched -- from 0.83 % of the peak at 400 m voxels to below")
    print("  0.2 % at 100-250 m.  It is not monotone, because the cube grid shifts")
    print("  relative to the sphere as the voxel size changes.")

    section("5. Superposition and the density-geometry trade-off")
    p1 = (-600.0, -200.0, -400.0, 400.0, 150.0, 800.0)
    p2 = (300.0, 900.0, -400.0, 400.0, 400.0, 1500.0)
    xpro = np.linspace(-3000.0, 3000.0, 13)
    obs = np.column_stack([xpro, np.zeros_like(xpro), np.zeros_like(xpro)])
    g1 = prism_gz(obs, p1, 400.0)
    g2 = prism_gz(obs, p2, -300.0)
    gsum = g1 + g2
    print("     x (m)   prism 1 (mGal)  prism 2 (mGal)   sum (mGal)   "
          "p1@200 (mGal)")
    g1b = prism_gz(obs, p1, 200.0)
    for xv, a, b, s, d in zip(xpro, g1, g2, gsum, g1b):
        print(f"  {xv:8.0f}   {mgal(a):14.5f}   {mgal(b):14.5f}   "
              f"{mgal(s):11.5f}   {mgal(d):13.5f}")
    print("  Halving the density halves every ordinate exactly; nothing in the")
    print("  profile shape separates rho from the volume, so a 2x deeper body of")
    print("  twice the volume can mimic it at long distances.")


if __name__ == "__main__":
    main()
