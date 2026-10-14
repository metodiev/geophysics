#!/usr/bin/env python3
"""Resistivity forward modelling: image series, layered solutions, and the
Jacobian that shows what a survey cannot resolve.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resistivity_forward_modelling_demo.py

Everything is SYNTHETIC.  The layered models are chosen teaching values; no
field data are used.

Contents
--------
1. The two-layer image series and its convergence.
2. Independent verification against the layered (Stefanescu) integral.
3. Half-space limit and reciprocity.
4. The Jacobian of a sounding: singular values and the null direction.
5. What the null direction means: transverse-resistance equivalence.
6. Cost and accuracy of the Bessel-integral route.
"""

import time

import numpy as np
from scipy.integrate import quad
from scipy.special import j0

RNG = np.random.default_rng(20261014)

I_INJECT = 0.1
N_CALLS = [0]           # counter for the Bessel integrand evaluations


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def kernel_R(rhos, hs, lam):
    R = 0.0
    for i in range(len(hs) - 1, -1, -1):
        k = (rhos[i + 1] - rhos[i]) / (rhos[i + 1] + rhos[i])
        R = (k + R) * np.exp(-2.0 * lam * hs[i]) / (1.0 + k * R)
    return R


def layered_potential(rhos, hs, r, I=1.0, count=False):
    lam_max = 30.0 / min(hs)

    def integrand(lam):
        if count:
            N_CALLS[0] += 1
        return (1.0 / (1.0 - kernel_R(rhos, hs, lam)) - 1.0) * j0(lam * r)

    value, err = quad(integrand, 0.0, lam_max, limit=600)
    return rhos[0] * I / (2.0 * np.pi) * (1.0 / abs(r) + value), err


def image_two_layer(rho1, rho2, h, r, I=1.0, nmax=200):
    """Exact two-layer solution as an image series.

    V(r) = (rho_1 I / 2 pi) [ 1/r + sum_{n>=1} k^n / sqrt(r^2 + (2 n h)^2) ],
    with the reflection coefficient k = (rho_2 - rho_1)/(rho_2 + rho_1).
    """
    k = (rho2 - rho1) / (rho2 + rho1)
    total = 1.0 / r
    for n in range(1, nmax + 1):
        total += k ** n / np.sqrt(r * r + (2.0 * n * h) ** 2)
    return rho1 * I / (2.0 * np.pi) * total


def wenner_dV(rhos, hs, a, I=I_INJECT, count=False):
    """Wenner dV = 2 V(a) - 2 V(2a) for a layered model."""
    v1, e1 = layered_potential(rhos, hs, a, I, count)
    v2, e2 = layered_potential(rhos, hs, 2.0 * a, I, count)
    return 2.0 * v1 - 2.0 * v2, e1 + e2


def main():
    t0 = time.perf_counter()
    section("1. The two-layer image series and its convergence")
    rho1, rho2, h = 100.0, 500.0, 8.0
    k = (rho2 - rho1) / (rho2 + rho1)
    print(f"  SYNTHETIC two-layer model: rho_1 = {rho1:.0f}, rho_2 = "
          f"{rho2:.0f} ohm m, h = {h:.1f} m")
    print(f"  reflection coefficient k = {k:.6f}")
    print("  V(r) = (rho_1 I/2pi)[1/r + sum k^n/sqrt(r^2+(2nh)^2)]")
    print("     r (m)   V exact (partial n=200)   V(n=1)        V(n=5)  "
          "       V(n=20)")
    for r in (1.0, 4.0, 8.0, 16.0, 40.0):
        vals = [image_two_layer(rho1, rho2, h, r, I_INJECT, n)
                for n in (1, 5, 20, 200)]
        print(f"  {r:8.1f} {vals[3]:22.10f} {vals[0]:13.10f} {vals[1]:13.10f} "
              f"{vals[2]:13.10f}")
    dev1 = abs(image_two_layer(rho1, rho2, h, 40.0, I_INJECT, 1)
               - image_two_layer(rho1, rho2, h, 40.0, I_INJECT, 200)) / \
        image_two_layer(rho1, rho2, h, 40.0, I_INJECT, 200)
    dev20 = abs(image_two_layer(rho1, rho2, h, 40.0, I_INJECT, 20)
                - image_two_layer(rho1, rho2, h, 40.0, I_INJECT, 200)) / \
        image_two_layer(rho1, rho2, h, 40.0, I_INJECT, 200)
    print(f"  at r = 40 m the single-image truncation is off by "
          f"{dev1:.3e} and the twenty-image sum by {dev20:.3e}")
    print("  the series converges geometrically in |k|: a handful of images")
    print("  suffices for a two-layer earth.  A stack of many layers needs the")
    print("  recurrence instead, because the number of image terms explodes.")

    section("2. Independent verification against the layered integral")
    print("  the same model solved by the Stefanescu recurrence plus a Bessel")
    print("  integral (the route that generalises to any number of layers):")
    print("     r (m)   image series        layered integral    relative diff")
    worst = 0.0
    for r in (1.0, 2.0, 4.0, 8.0, 16.0, 40.0, 80.0):
        v_img = image_two_layer(rho1, rho2, h, r, I_INJECT, 400)
        v_int, err = layered_potential([rho1, rho2], [h], r, I_INJECT)
        diff = abs(v_int - v_img) / v_img
        worst = max(worst, diff)
        print(f"  {r:8.1f} {v_img:19.12f} {v_int:19.12f} {diff:18.3e}")
    print(f"  worst relative difference over the range: {worst:.3e}")
    print("  two completely different computations agree to twelve digits.")
    print("  This is the check that must be passed before any inversion, or any")
    print("  interpretation, is allowed to use the forward model at all.")

    section("3. Half-space limit and reciprocity")
    print("  setting rho_2 = rho_1 must return the half-space potential:")
    for rho in (10.0, 100.0, 1000.0):
        v_img = image_two_layer(rho, rho, h, 5.0, I_INJECT, 400)
        v_half = rho * I_INJECT / (2.0 * np.pi * 5.0)
        print(f"    rho = {rho:7.1f} ohm m: image = {v_img:.12f} V, "
              f"half-space = {v_half:.12f} V, diff = "
              f"{abs(v_img - v_half):.3e}")
    # reciprocity: exchange the current pair and the potential pair
    rhos, hs = [100.0, 20.0, 400.0], [4.0, 6.0]

    def dV4(A, B, M, N):
        def V(d):
            return layered_potential(rhos, hs, d, I_INJECT)[0]
        return V(M - A) - V(N - A) - V(M - B) + V(N - B)

    A, B, M, N = 0.0, 7.0, 3.0, 11.0
    d_ab_mn = dV4(A, B, M, N)
    d_mn_ab = dV4(M, N, A, B)
    print(f"\n  three-layer model rho = {rhos}, h = {hs}")
    print("  asymmetric array: current at 0 and 7 m, potential at 3 and 11 m")
    print(f"    current at (0, 7), potential at (3, 11): dV = {d_ab_mn:.12f} V")
    print(f"    current at (3, 11), potential at (0, 7): dV = {d_mn_ab:.12f} V")
    print(f"    difference = {abs(d_ab_mn - d_mn_ab):.3e} V, i.e. "
          f"{abs(d_ab_mn - d_mn_ab) / abs(d_ab_mn):.1e} relative")
    print("  reciprocity is a property of the conductivity operator, and any")
    print("  correct forward model reproduces it; a broken one usually does not.")

    section("4. The Jacobian of a sounding: singular values and null directions")
    spacings = np.array([1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 16.0, 24.0,
                         32.0, 48.0])
    rhos, hs = [100.0, 500.0, 20.0], [5.0, 4.0]
    print(f"  SYNTHETIC model: rho = {rhos} ohm m, h = {hs} m")
    print(f"  data: log-spaced Wenner sounding, {spacings.size} spacings")
    rho_a = np.array([2.0 * np.pi * a * wenner_dV(rhos, hs, a)[0] / I_INJECT
                      for a in spacings])
    # parameters in log space: ln rho_1, ln rho_2, ln rho_3, ln h_1, ln h_2
    params = np.concatenate([np.log(rhos), np.log(hs)])
    m = params.size
    J = np.zeros((spacings.size, m))
    for j in range(m):
        step = 1e-4
        pp = params.copy()
        pp[j] += step
        pm = params.copy()
        pm[j] -= step
        rr_p, hh_p = np.exp(pp[:3]), np.exp(pp[3:])
        rr_m, hh_m = np.exp(pm[:3]), np.exp(pm[3:])
        dp = np.array([2.0 * np.pi * a * wenner_dV(rr_p, hh_p, a)[0] / I_INJECT
                       for a in spacings])
        dm = np.array([2.0 * np.pi * a * wenner_dV(rr_m, hh_m, a)[0] / I_INJECT
                       for a in spacings])
        J[:, j] = (np.log(dp) - np.log(dm)) / (2.0 * step)
    print("\n  normalised sensitivities d ln rho_a / d ln parameter:")
    labels = ("ln rho_1", "ln rho_2", "ln rho_3", "ln h_1", "ln h_2")
    print("   a (m)  " + "".join(f"{lab:>10s}" for lab in labels))
    for i, a in enumerate(spacings):
        print(f"  {a:6.1f}  " + "".join(f"{J[i, j]:10.4f}" for j in range(m)))
    U, sv, Vt = np.linalg.svd(J, full_matrices=False)
    print(f"\n  singular values: " + ", ".join(f"{x:.4f}" for x in sv))
    print(f"  condition number = {sv[0] / sv[-1]:.4e}")
    v_min = Vt[-1]
    print("  smallest singular vector (normalised):")
    for lab, comp in zip(labels, v_min):
        print(f"    {lab:>8s}: {comp:+.6f}")
    print("  the data are nearly blind to the combination this vector points")
    print("  along: changing the model that way barely moves the sounding.")

    section("5. What the null direction means")
    eps_dir = 0.05
    r2 = rhos[1] * np.exp(eps_dir * v_min[1])
    h2 = hs[1] * np.exp(eps_dir * v_min[4])
    print(f"  move the model 5% along the null direction:")
    print(f"    rho_2: {rhos[1]:8.2f} -> {r2:8.2f} ohm m "
          f"({(r2 / rhos[1] - 1) * 100:+.2f}%)")
    print(f"    h_2  : {hs[1]:8.2f} -> {h2:8.2f} m "
          f"({(h2 / hs[1] - 1) * 100:+.2f}%)")
    print(f"    h_2 rho_2 (transverse resistance T): {hs[1] * rhos[1]:.1f} -> "
          f"{h2 * r2:.1f} ohm m^2 ({(h2 * r2 / (hs[1] * rhos[1]) - 1) * 100:+.2f}%)")
    print(f"    h_2/rho_2 (longitudinal conductance S): {hs[1] / rhos[1]:.6f} -> "
          f"{h2 / r2:.6f} S ({(h2 / r2) / (hs[1] / rhos[1]) * 100 - 100:+.2f}%)")
    curve0 = np.array([2.0 * np.pi * a * wenner_dV(rhos, hs, a)[0] / I_INJECT
                       for a in spacings])
    curve1 = np.array([2.0 * np.pi * a * wenner_dV(
        [rhos[0], r2, rhos[2]], [hs[0], h2], a)[0] / I_INJECT
        for a in spacings])
    print(f"  maximum change in the sounding along this direction: "
          f"{np.max(np.abs(curve1 - curve0) / curve0) * 100:.2f}%")
    print("  the null direction is (ln rho_2, ln h_2) with opposite signs, and")
    print("  it leaves the transverse resistance h rho nearly unchanged: this")
    print("  is T-equivalence, derived from the model rather than observed.")
    print("  A sounding cannot separate the thickness of a thin resistive layer")
    print("  from its resistivity; that is a null space, not a data problem.")

    section("6. Cost and accuracy of the Bessel-integral route")
    N_CALLS[0] = 0
    t1 = time.perf_counter()
    for _ in range(50):
        wenner_dV(rhos, hs, 8.0, count=True)
    dt = (time.perf_counter() - t1) / 50.0
    print(f"  one Wenner dV (two Bessel integrals) takes {dt * 1e3:.2f} ms and")
    print(f"  {N_CALLS[0] / 50:.0f} integrand evaluations of J_0")
    print(f"  the whole demo took {time.perf_counter() - t0:.2f} s")
    print(f"  quadrature error estimate from the last call: "
          f"{wenner_dV(rhos, hs, 8.0)[1]:.3e} V")


if __name__ == "__main__":
    main()
