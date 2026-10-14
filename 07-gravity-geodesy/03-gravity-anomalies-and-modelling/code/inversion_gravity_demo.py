#!/usr/bin/env python3
"""Gravity inversion and its non-uniqueness, measured rather than asserted.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python inversion_gravity_demo.py

All models and data in this module are SYNTHETIC.  The target body, the station
spacing and the noise level are chosen teaching values.

Contents
--------
1. A synthetic data set over a buried 2-D block.
2. A cell parameterisation and inversion by non-negative least squares with a
   smoothness penalty: misfit versus regularisation strength.
3. The true model and the inverted model: both fit, and they differ.
4. The resolution matrix: what the data can and cannot see at depth.
5. An exact annihilator: a density distribution that produces almost no field.
6. Aperture and the admitted (mass, depth) set for a compact body.
"""

import numpy as np
from scipy.optimize import nnls

RNG = np.random.default_rng(20261014)

G_SI = 6.67430e-11
MGAL_TO_SI = 1.0e-5
NOISE_MGAL = 0.02


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def mgal(g_si):
    return g_si / MGAL_TO_SI


def _P(u, a):
    return u * np.log(u * u + a * a) - 2.0 * u + 2.0 * a * np.arctan(u / a)


def rect2d_g(x, x1, x2, z1, z2, drho):
    """Vertical gravity (m/s^2) of a 2-D rectangle, infinite along strike."""
    j1 = 0.5 * (_P(x - x1, z2) - _P(x - x1, z1))
    j2 = 0.5 * (_P(x - x2, z2) - _P(x - x2, z1))
    return 2.0 * G_SI * drho * (j1 - j2)


LAYERS = [(100.0, 200.0), (200.0, 400.0), (400.0, 800.0),
          (800.0, 1600.0), (1600.0, 3200.0), (3200.0, 6400.0)]
NX, DXW = 41, 200.0


def build_grid():
    """Cell geometry: 41 columns x 6 depth layers (SYNTHETIC)."""
    xc = (np.arange(NX) - (NX - 1) / 2.0) * DXW
    cells, zref = [], []
    for z1, z2 in LAYERS:
        for cx in xc:
            cells.append((cx - DXW / 2, cx + DXW / 2, z1, z2))
            zref.append(np.sqrt(z1 * z2))
    return np.array(cells), np.array(zref)


def smoothness():
    rows = []
    for k in range(len(LAYERS)):
        for i in range(NX - 1):
            r = np.zeros(NX * len(LAYERS))
            r[k * NX + i], r[k * NX + i + 1] = 1.0, -1.0
            rows.append(r)
    for k in range(len(LAYERS) - 1):
        for i in range(NX):
            r = np.zeros(NX * len(LAYERS))
            r[k * NX + i], r[(k + 1) * NX + i] = 1.0, -1.0
            rows.append(r)
    return np.array(rows)


def mass_per_length(m, cells):
    """Total anomalous mass per unit strike length, kg/m."""
    return float(np.sum(m * DXW * (cells[:, 3] - cells[:, 2])))


def mass_centre_depth(m, cells, zref):
    w = m * (cells[:, 3] - cells[:, 2])
    return float(np.sum(w * zref) / np.sum(w))


def main():
    section("1. A synthetic data set")
    x_obs = np.arange(-3000.0, 3000.0 + 1.0, 100.0)
    truth = (-800.0, 800.0, 200.0, 1200.0, 400.0)
    d_true = rect2d_g(x_obs, *truth)
    noise = NOISE_MGAL * MGAL_TO_SI
    d = d_true + noise * RNG.standard_normal(x_obs.size)
    print("SYNTHETIC truth: 2-D block x in [-800, 800] m, depth 200-1200 m, "
          "rho = 400 kg/m^3")
    print(f"stations: {x_obs.size} at 100 m spacing over 6 km; noise rms "
          f"{NOISE_MGAL:.4f} mGal")
    print(f"peak anomaly {mgal(d_true.max()):.4f} mGal; data rms "
          f"{mgal(np.sqrt(np.mean(d ** 2))):.4f} mGal")
    print(f"true mass per unit strike length = "
          f"{400.0 * 1600.0 * 1000.0:.3e} kg/m")

    section("2. Inversion: misfit versus regularisation strength")
    cells, zref = build_grid()
    G = np.column_stack([rect2d_g(x_obs, *c, 1.0) for c in cells])
    D = smoothness()
    print(f"parameters: {cells.shape[0]} cells ({len(LAYERS)} layers x {NX} "
          f"columns); data: {x_obs.size}; smoothness rows: {D.shape[0]}")
    print("     alpha   rms misfit (mGal)   mass per length (kg/m)   "
          "mass centre depth (m)")
    m_ref = {}
    for alpha in (1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1):
        A = np.vstack([mgal(G), alpha * D])
        b = np.concatenate([mgal(d), np.zeros(D.shape[0])])
        m, _ = nnls(A, b)
        m_ref[alpha] = m
        rms = np.sqrt(np.mean((mgal(G @ m) - mgal(d)) ** 2))
        print(f"  {alpha:8.0e}   {rms:17.4f}   {mass_per_length(m, cells):22.3e}   "
              f"{mass_centre_depth(m, cells, zref):20.1f}")
    print("  Strong regularisation smooths the model and misfits the data; weak")
    print("  regularisation fits tightly and scatters density.  The table is a")
    print("  statement about the penalty, not about the Earth.")

    section("3. The true model and the inverted model: both fit")
    m = m_ref[1e-5]
    rms_true = np.sqrt(np.mean((mgal(d_true) - mgal(d)) ** 2))
    rms_inv = np.sqrt(np.mean((mgal(G @ m) - mgal(d)) ** 2))
    print(f"  rms misfit of the TRUE model        = {rms_true:.4f} mGal "
          "(it equals the noise, by construction)")
    print(f"  rms misfit of the INVERTED model    = {rms_inv:.4f} mGal")
    print(f"  stated noise level                  = {NOISE_MGAL:.4f} mGal rms")
    print("  Both are consistent with the data, yet:")
    print(f"    true   mass centre depth = {(1200.0 ** 2 - 200.0 ** 2) / (2.0 * 1000.0):.1f} m, "
          f"mass per length {400.0 * 1600.0 * 1000.0:.3e} kg/m")
    print(f"    inverted mass centre depth = {mass_centre_depth(m, cells, zref):.1f} m, "
          f"mass per length {mass_per_length(m, cells):.3e} kg/m")
    print("  The inversion has placed comparable mass at a shallower depth, where")
    print("  the kernel is largest.  Nothing in the data rejects it; this is the")
    print("  non-uniqueness, measured.")

    section("4. Resolution matrix: what the data can see")
    A = mgal(G)
    L = 1e-5 * D
    Mtx = A.T @ A + L.T @ L
    R = np.linalg.solve(Mtx, A.T @ A)
    diagR = np.diag(R)
    print("  diag(R) averaged over the 41 columns of each layer:")
    print("     layer depth (m)    mean diag(R)    reading")
    for k, (z1, z2) in enumerate(LAYERS):
        block = diagR[k * NX: (k + 1) * NX].mean()
        verdict = ("well resolved" if block > 0.5 else
                   "weakly resolved" if block > 0.1 else "essentially invisible")
        print(f"  {z1:8.0f} - {z2:6.0f}   {block:14.4f}    {verdict}")
    print(f"  trace(R) = {diagR.sum():.1f} for {cells.shape[0]} parameters and "
          f"{x_obs.size} data:")
    print("  the number of resolvable parameters cannot exceed the number of")
    print("  independent data, however many cells are drawn on the map.")

    section("5. An exact annihilator: mass the data cannot see")
    k0 = 2.0 * np.pi / 1000.0
    wl = 2.0 * np.pi / k0
    dxg = wl / 40.0
    xg = np.arange(-50.0 * wl, 50.0 * wl, dxg)
    xpro = np.array([0.0, 200.0, 500.0])
    h1, h2 = 800.0, 1600.0
    s1 = 1.0
    s2 = -s1 * np.exp(k0 * (h2 - h1))

    def sheet(x, h, s0):
        return float(np.sum(2.0 * G_SI * s0 * np.cos(k0 * xg) * dxg * h
                            / ((x - xg) ** 2 + h ** 2)))

    g1 = np.array([sheet(xv, h1, s1) for xv in xpro])
    an1 = 2.0 * np.pi * G_SI * s1 * np.cos(k0 * xpro) * np.exp(-k0 * h1)
    print(f"harmonic: k0 = {k0:.6e} 1/m, wavelength {wl:.0f} m")
    print("  the discrete line-mass sum against the analytic kernel "
          "2 pi G s0 cos(kx) exp(-kh):")
    print("     x (m)   discrete sum (mGal)   analytic (mGal)   rel. diff")
    for xv, a, b in zip(xpro, g1, an1):
        print(f"  {xv:7.0f}   {mgal(a):18.6e}   {mgal(b):16.6e}   "
              f"{abs(a - b) / abs(b):.2e}")
    g2 = np.array([sheet(xv, h2, s2) for xv in xpro])
    print(f"  sheet 1: depth {h1:.0f} m, amplitude {s1:+.3f} kg/m^2")
    print(f"  sheet 2: depth {h2:.0f} m, amplitude {s2:+.3f} kg/m^2 "
          f"= -exp(k0 * (h2 - h1)) times sheet 1")
    print("     x (m)   sheet 1 (mGal)   sheet 2 (mGal)        sum (mGal)")
    for xv, a, b in zip(xpro, g1, g2):
        print(f"  {xv:7.0f}   {mgal(a):14.6e}   {mgal(b):14.6e}   "
              f"{mgal(a + b):14.6e}")
    rel = mgal(np.abs(g1 + g2).max()) / mgal(np.abs(g1).max())
    print(f"  the pair sums to {rel:.2e} of the individual signal in these "
          "discrete sums;")
    print("  in the continuum the cancellation is exact, and the residual here is")
    print("  quadrature error (each sum is itself accurate only to ~1e-4) amplified")
    print("  by the near-cancellation -- a numerical, not a physical, residual.")
    print(f"  The two sheets carry harmonic amplitudes in the ratio "
          f"{abs(s2) / abs(s1):.1f}:1, so the mass implied by the data")
    print("  is ambiguous by that factor at this wavelength.")

    section("6. Aperture and the admitted (mass, depth) set")
    m0, z0 = 2.0e11, 1000.0
    tol = NOISE_MGAL * MGAL_TO_SI
    print(f"SYNTHETIC point mass M = {m0:.1e} kg at depth {z0:.0f} m; the shape is")
    print(f"assumed, the mass is fitted, and a model is accepted when its rms "
          f"misfit <= {NOISE_MGAL:.2f} mGal")
    print("   aperture (m)   stations   admitted depth (m)   admitted mass (kg)"
          "        mass factor")
    zs = np.logspace(np.log10(200.0), np.log10(40000.0), 800)
    for xmax in (250.0, 500.0, 1000.0, 4000.0):
        xp = np.arange(-xmax, xmax + 1.0, 25.0)
        d_pm = G_SI * m0 * z0 / (xp ** 2 + z0 ** 2) ** 1.5
        adm = []
        for z in zs:
            k = G_SI * z / (xp ** 2 + z ** 2) ** 1.5
            mf = float(np.dot(k, d_pm) / np.dot(k, k))
            if np.sqrt(np.mean((mf * k - d_pm) ** 2)) <= tol:
                adm.append((z, mf))
        adm = np.array(adm)
        print(f"  {2 * xmax:10.0f}   {xp.size:8d}   {adm[0, 0]:9.0f} - "
              f"{adm[-1, 0]:8.0f}   {adm[0, 1]:.2e} - {adm[-1, 1]:.2e}   "
              f"{adm[-1, 1] / adm[0, 1]:10.2f}")
    print("  A survey whose aperture is small compared with the source depth")
    print("  admits a wide range of depths and a mass range of a factor of three;")
    print("  extending the aperture past the depth collapses the set.  Aperture,")
    print("  not the number of decimal places in the printout, sets the resolution.")


if __name__ == "__main__":
    main()
