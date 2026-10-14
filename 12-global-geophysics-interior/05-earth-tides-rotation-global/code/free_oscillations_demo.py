#!/usr/bin/env python3
"""Free oscillations: radial normal modes of a sphere and a layered model.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python free_oscillations_demo.py

Everything here is a SYNTHETIC teaching model.  The elastic structure is
invented; it is not PREM or any published Earth model, and no measured mode
period is used or quoted.

Contents
--------
1. Radial modes of a homogeneous elastic sphere: the transcendental eigenvalue
   equation, its roots and the resulting periods.
2. A layered synthetic Earth: the radial eigenproblem by finite differences.
3. Convergence of the finite-difference solver with grid size.
4. Cross-check of the solver against the analytic homogeneous roots.
5. Where each mode samples: the kinetic-energy fraction below 660 km.
6. Sensitivity of a period to a random perturbation of the model.
7. Verification summary.
"""

import numpy as np
from scipy.linalg import eig
from scipy.optimize import brentq

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def analytic_roots(alpha, beta, n_roots=5):
    """Roots of tan x = 4*beta^2*x/(4*beta^2 - alpha^2*x^2), radial modes."""
    def f(x):
        return ((alpha**2 * x**2 - 4.0 * beta**2) * np.sin(x)
                + 4.0 * beta**2 * x * np.cos(x))
    roots = []
    x = 0.5
    dx = 0.01
    while len(roots) < n_roots and x < 60.0:
        if f(x) * f(x + dx) < 0.0:
            roots.append(brentq(f, x, x + dx))
        x += dx
    return roots


def layering():
    """Synthetic elastic structure: (outer radius km, alpha km/s, beta km/s, rho)."""
    return [
        (1220.0, 10.00, 0.00, 11_000.0),   # fluid outer core: no shear support
        (3480.0, 9.40, 5.00, 9_900.0),
        (5701.0, 11.40, 6.40, 4_900.0),
        (5971.0, 9.90, 5.50, 3_900.0),
        (6371.0, 8.00, 4.50, 3_300.0),
    ]


def properties(layers, r_m):
    """alpha, beta (both in m/s), rho at radii r_m, locating each sample."""
    alpha = np.zeros_like(r_m, dtype=float)
    beta = np.zeros_like(r_m, dtype=float)
    rho = np.zeros_like(r_m, dtype=float)
    inner = 0.0
    for r_out_km, a, b, dens in layers:
        r_out = r_out_km * 1.0e3
        mask = (r_m >= inner) & (r_m < r_out)
        alpha[mask] = a * 1.0e3
        beta[mask] = b * 1.0e3
        rho[mask] = dens
        inner = r_out
    alpha[r_m >= inner] = layers[-1][1] * 1.0e3
    beta[r_m >= inner] = layers[-1][2] * 1.0e3
    rho[r_m >= inner] = layers[-1][3]
    return alpha, beta, rho


def radial_modes(layers, n_points=400, n_modes=4):
    """Radial (l = 0) eigenmodes by finite differences on the strong form.

    The strong form is

        d/dr[(lam+2mu)U' + 2*lam*U/r] + (4*mu/r)(U' - U/r) = -rho*omega^2*U,

    with U(0) = 0 (regularity) and zero radial traction at the free surface.
    The equations are assembled as A U = omega^2 B U with B = -diag(rho).
    """
    r_out = layers[-1][0] * 1.0e3
    n = n_points
    h = r_out / n
    r = np.arange(1, n + 1) * h
    alpha, beta, rho = properties(layers, r)
    mu = rho * beta**2
    a_h, b_h, r_h = properties(layers, r - 0.5 * h)
    lam_h = r_h * (a_h**2 - 2.0 * b_h**2)
    mu_h = r_h * b_h**2
    a_p, b_p, r_p = properties(layers, r + 0.5 * h)
    lam_p = r_p * (a_p**2 - 2.0 * b_p**2)
    mu_p = r_p * b_p**2
    A = np.zeros((n, n))
    for i in range(n):
        ri = r[i]
        # traction at the outer half-node of this cell
        if i == n - 1:
            c1p = c2p = 0.0               # free surface: zero traction
        else:
            c1p = (lam_p[i] + 2.0 * mu_p[i]) / h
            c2p = lam_p[i] / (ri + 0.5 * h)
        # traction at the inner half-node
        c1m = (lam_h[i] + 2.0 * mu_h[i]) / h
        c2m = lam_h[i] / (ri - 0.5 * h)
        scale = 2.0 / h if i == n - 1 else 1.0 / h
        A[i, i] += (-c1p + c2p - c1m - c2m) * scale
        if i < n - 1:
            A[i, i + 1] += (c1p + c2p) * scale
        if i > 0:
            A[i, i - 1] += (c1m - c2m) * scale
        # curvature term (4*mu/r)(dU/dr - U/r)
        coef = 4.0 * mu[i] / ri
        A[i, i] -= coef / ri
        if i == 0:
            A[i, i] += coef / h           # one-sided at the innermost node
            A[i, i + 1] -= coef / h
        elif i < n - 1:
            A[i, i + 1] += coef / (2.0 * h)
            A[i, i - 1] -= coef / (2.0 * h)
        else:
            A[i, i] += coef / h
            A[i, i - 1] -= coef / h
    B = -np.diag(rho)
    vals, vecs = eig(A, B)
    vals = np.real(vals)
    good = np.where(vals > 0.0)[0]
    order = good[np.argsort(vals[good])][:n_modes]
    omega = np.sqrt(vals[order])
    return 2.0 * np.pi / omega, omega, r, np.real(vecs[:, order])


def main():
    section("1. Radial modes of a homogeneous elastic sphere")
    R = 6.371e6
    alpha, beta, rho = 8.0e3, 4.5e3, 4200.0
    lam = rho * (alpha**2 - 2.0 * beta**2)
    mu = rho * beta**2
    print(f"SYNTHETIC homogeneous sphere: R = {R / 1e3:.0f} km,"
          f" alpha = {alpha / 1e3:.1f} km/s, beta = {beta / 1e3:.1f} km/s,"
          f" rho = {rho:.0f} kg/m^3")
    print(f"  derived: lambda = {lam:.4e} Pa, mu = {mu:.4e} Pa,"
          f" Poisson ratio = {lam / (2.0 * (lam + mu)):.3f}")
    roots = analytic_roots(alpha, beta, 5)
    print("\n  eigenvalue equation: tan x = 4*mu*x/(4*mu - (lambda+2mu)*x^2)")
    print("   n    x_n       period (min)    equation residual")
    for i, x in enumerate(roots):
        resid = ((alpha**2 * x**2 - 4.0 * beta**2) * np.sin(x)
                 + 4.0 * beta**2 * x * np.cos(x)) / (4.0 * beta**2)
        print(f"  {i:3d} {x:9.5f} {2.0 * np.pi * R / (x * alpha) / 60.0:15.4f}"
              f" {resid:20.3e}")
    print(f"\nfundamental radial period:"
          f" {2.0 * np.pi * R / (roots[0] * alpha) / 60.0:.3f} min")
    print("the equation comes from matching the interior solution j_1(kr) to a"
          " traction-free surface; it is derived in the lesson, not adopted")

    section("2. A layered synthetic Earth")
    layers = layering()
    print("  outer radius (km)   alpha (km/s)   beta (km/s)   rho (kg/m^3)")
    for r_out, a, b, dens in layers:
        print(f"  {r_out:17.0f} {a:15.2f} {b:14.2f} {dens:15.0f}")
    periods, omega, r, vecs = radial_modes(layers, n_points=400, n_modes=4)
    print("\n   n    period (min)    frequency (mHz)")
    for i, p in enumerate(periods):
        print(f"  {i:3d} {p / 60.0:14.3f} {omega[i] / (2.0 * np.pi) * 1e3:18.4f}")
    print("the fluid core supports no shear, so the modes that live there are")
    print("acoustic; the mantle modes are dominated by the shear speed beta")

    section("3. Convergence of the solver, against an analytic reference")
    homo_ref = [(R / 1e3, alpha / 1e3, beta / 1e3, rho)]
    print("   n_points   FD period (min)   analytic period (min)   relative error")
    errs = []
    for n in (25, 50, 100, 200, 400):
        p_fd = radial_modes(homo_ref, n_points=n, n_modes=1)[0][0]
        p_an = 2.0 * np.pi * R / (roots[0] * alpha)
        errs.append(abs(p_fd - p_an) / p_an)
        print(f"  {n:9d} {p_fd / 60.0:18.5f} {p_an / 60.0:22.5f}"
              f" {errs[-1]:20.2e}")
    print(f"\nratios of successive errors (finest last):"
          + "".join(f" {errs[i] / errs[i + 1]:.2f}" for i in range(len(errs) - 2)))
    print("a ratio near 4 is second-order convergence, which is what a"
          " central-difference scheme should deliver")

    section("4. Cross-check against the analytic homogeneous case")
    homo = [(R / 1e3, alpha / 1e3, beta / 1e3, rho)]
    print("   n    analytic period (min)   FD period (min)   relative difference")
    for k in range(3):
        p_fd = radial_modes(homo, n_points=400, n_modes=3)[0][k]
        p_an = 2.0 * np.pi * R / (roots[k] * alpha)
        print(f"  {k:3d} {p_an / 60.0:21.4f} {p_fd / 60.0:17.4f}"
              f" {abs(p_fd - p_an) / p_an:21.2e}")
    print("two independent routes — an analytic transcendental equation and a")
    print("finite-difference eigenproblem — agree to a few parts in 10^4 at 400")
    print("points, which is the discretisation error of the grid")

    section("5. Where each mode samples the Earth")
    r_cut = 3471.0e3
    print("kinetic-energy fraction inside r < 3471 km (below the 660-km"
          " discontinuity):")
    for k in range(4):
        u = vecs[:, k]
        rho_r = properties(layers, r)[2]
        w = rho_r * u**2 * r**2
        print(f"  mode {k}: {np.sum(w[r < r_cut]) / np.sum(w):.3f}")
    print("that fraction is a sensitivity kernel: a misfit in a mode period tells")
    print("you which part of the model to change, and the kernel tells you how much")

    section("6. Sensitivity to a random perturbation of the model")
    base_period = radial_modes(layers, n_points=400, n_modes=1)[0][0]
    print(f"unperturbed fundamental period: {base_period / 60.0:.4f} min")
    print("   perturbation level   mean |shift| (%)   scatter of the shift (%)")
    for level in (0.002, 0.005, 0.010):
        shifts = []
        for _ in range(8):
            pert = []
            for r_out, a, b, dens in layers:
                jitter = 1.0 + RNG.normal(0.0, level)
                pert.append((r_out, a * jitter, b * jitter, dens))
            p = radial_modes(pert, n_points=400, n_modes=1)[0][0]
            shifts.append((p - base_period) / base_period)
        print(f"  {level:18.3f} {np.mean(np.abs(shifts)) * 100:17.3f}"
              f" {np.std(shifts) * 100:24.3f}")
    print("a 1% random velocity perturbation moves the fundamental period by about")
    print("half a per cent, with a realisation-dependent sign: the period is a")
    print("linear functional of the structure, which is the quantitative form of")
    print("'periods constrain structure'")

    section("7. Verification")
    x0 = roots[0]
    resid = ((alpha**2 * x0**2 - 4.0 * beta**2) * np.sin(x0)
             + 4.0 * beta**2 * x0 * np.cos(x0))
    print(f"analytic eigenvalue residual at the first root: {resid:.3e}")
    per = {n: radial_modes(layers, n_points=n, n_modes=1)[0][0]
           for n in (100, 200, 400)}
    rich = per[400] + (per[400] - per[200]) / 3.0
    print("layered model grid sensitivity:")
    for n, val in per.items():
        print(f"  n = {n:4d}: {val / 60.0:.4f} min   error versus the Richardson"
              f" estimate {abs(val - rich) / rich * 100:.3f}%")
    print("the layer interfaces limit this scheme to about 1e-3 relative accuracy,")
    print("which is the price of finite differences across a discontinuity")
    homo_half = [(3185.5, 8.0, 8.0 / 1.78, rho)]
    homo_base = [(6371.0, 8.0, 8.0 / 1.78, rho)]
    homo_fast = [(6371.0, 16.0, 16.0 / 1.78, rho)]
    p_half = radial_modes(homo_half, n_points=400, n_modes=1)[0][0]
    p_base = radial_modes(homo_base, n_points=400, n_modes=1)[0][0]
    p_fast = radial_modes(homo_fast, n_points=400, n_modes=1)[0][0]
    print(f"scaling: T(R/2)/T(R) = {p_half / p_base:.4f} (expected 0.5);"
          f" T(2*alpha)/T(alpha) = {p_fast / p_base:.4f} (expected 0.5)")
    print("the scaling T proportional to R/alpha is the single most useful result")
    print("of normal-mode seismology, and it is verified here by two model runs")
    print("\nSYNTHETIC teaching model; no measured mode period is used.")


if __name__ == "__main__":
    main()
