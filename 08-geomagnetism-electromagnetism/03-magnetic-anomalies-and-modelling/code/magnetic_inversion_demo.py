#!/usr/bin/env python3
"""Magnetic inversion and its non-uniqueness: a linear 2-D susceptibility
inversion, its singular-value spectrum, an explicit near-annihilator, the
regularisation trade-off and the effect of a positivity constraint.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_inversion_demo.py

Everything here is SYNTHETIC.  The 'true' model, the noise level, the cell grid
and the regularisation weights are chosen teaching values, not a field survey.

Contents
--------
1. The forward operator G for a 2-D grid of magnetised cells.
2. Synthetic data, and the singular-value spectrum of G.
3. A near-annihilator: a model that changes a lot and the data not at all.
4. Tikhonov inversion, the misfit-versus-roughness trade-off, and the recovered
   magnetisation.
5. Depth weighting, and why an unweighted inversion piles magnetisation at the top.
6. A positivity constraint, and the range of models it still admits.
7. Summary for the lesson.
"""

import numpy as np
from scipy.optimize import nnls

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi
C = MU0 / (4.0 * np.pi)
KM = 1.0e3
NT = 1.0e-9

NX_CELLS = 21                  # cells 1 km wide, from -10 to +10 km
NZ_CELLS = 8                   # cells 1 km thick, from 1 to 9 km depth
CELL_KM = 1.0
N_DATA = 41
X_MAX_KM = 10.0
NOISE_NT = 0.5
H0_AM = 40.0                   # ambient field / mu0, A/m (SYNTHETIC)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def build_operator():
    """G[i, j] = dT at station i from unit magnetisation in cell j."""
    xc = (np.arange(NX_CELLS) - (NX_CELLS - 1) / 2) * CELL_KM * KM
    zc = (np.arange(NZ_CELLS) + 0.5) * CELL_KM * KM
    V = (CELL_KM * KM) ** 3
    XC, ZC = np.meshgrid(xc, zc, indexing="ij")
    cell_x = XC.ravel()
    cell_z = ZC.ravel()
    stations = np.linspace(-X_MAX_KM * KM, X_MAX_KM * KM, N_DATA)
    G = np.zeros((N_DATA, cell_x.size))
    for i, xs in enumerate(stations):
        dx = xs - cell_x
        r = np.sqrt(dx ** 2 + cell_z ** 2)
        rhat_z = -cell_z / r
        G[i] = C * V * (3 * rhat_z ** 2 - 1) / r ** 3
    return G / NT, cell_x, cell_z, stations    # G in nT per (A/m)


def tikhonov(G, d, W, lam):
    """Solve min ||Gm - d||^2 + lam ||Wm||^2 by stacking."""
    A = np.vstack([G, np.sqrt(lam) * W])
    b = np.concatenate([d, np.zeros(W.shape[0])])
    m, *_ = np.linalg.lstsq(A, b, rcond=None)
    return m


def main():
    G, cell_x, cell_z, stations = build_operator()
    n_model = cell_x.size

    section("1. The forward operator")
    print(f"data: {N_DATA} stations from -{X_MAX_KM:.0f} to +{X_MAX_KM:.0f} km, "
          f"total-field anomaly, pole configuration")
    print(f"model: {NX_CELLS} x {NZ_CELLS} = {n_model} cells of "
          f"{CELL_KM:.1f} x {CELL_KM:.1f} km in a vertical section, top 0.5 km")
    print(f"G is {G.shape[0]} x {G.shape[1]}; each column is the anomaly of 1 A/m")
    print(f"column norms: surface row {np.linalg.norm(G[:, 0]):.4e}, "
          f"deepest row {np.linalg.norm(G[:, n_model - 1]):.4e} "
          f"(ratio {np.linalg.norm(G[:, 0]) / np.linalg.norm(G[:, n_model - 1]):.1f})")

    section("2. Synthetic data and the singular-value spectrum")
    M_true = np.zeros(n_model)
    for j in range(n_model):
        z_km = cell_z[j] / KM
        x_km = cell_x[j] / KM
        if abs(x_km + 5) <= 1.5 and 1.5 <= z_km <= 3.5:
            M_true[j] = 4.0
        if abs(x_km - 5) <= 1.5 and 5.5 <= z_km <= 7.5:
            M_true[j] = 1.5
    d_clean = G @ M_true
    d = d_clean + NOISE_NT * RNG.standard_normal(N_DATA)   # nT
    print(f"true model: {np.count_nonzero(M_true)} non-zero cells, two bodies at "
          f"depth 1.5-3.5 km (x = -5 km) and 5.5-7.5 km (x = +5 km)")
    print(f"magnetisation 4.0 A/m and 1.5 A/m; total moment-sum M*V = "
          f"{M_true.sum() * (CELL_KM * KM) ** 3:.3e} A m^2")
    print(f"peak anomaly {d_clean.max():.2f} nT, noise "
          f"{NOISE_NT:.2f} nT rms ({NOISE_NT / d_clean.max() * 100:.2f}% of peak)")
    U, s, Vt = np.linalg.svd(G, full_matrices=True)
    rank = int(np.sum(s > s[0] * 1e-10))
    nullity = n_model - rank
    print(f"singular values: largest {s[0]:.3e}, smallest {s[-1]:.3e}, "
          f"ratio {s[0] / s[-1]:.2e}")
    print("   index   singular value   relative to largest")
    for i in (0, 9, 19, 29, 40):
        if i < len(s):
            print(f"   {i:5d}   {s[i]:14.4e}   {s[i] / s[0]:18.3e}")
    n_small = int(np.sum(s < s[0] * 1e-6))
    print(f"   {n_small} of the {len(s)} non-zero-pattern values are below 1e-6 of the")
    print(f"   largest.  The operator is {G.shape[0]} x {n_model}, so its rank is "
          f"{rank} and")
    print(f"   its exact null space has dimension "
          f"{G.shape[1] - rank} = {nullity}.")

    section("3. A near-annihilator")
    v_null = Vt[rank + 5] if rank + 5 < n_model else Vt[-1]
    data_from_null = G @ v_null
    print(f"the smallest right singular vector v has ||G v|| = "
          f"{np.linalg.norm(data_from_null):.3e} nT for ||v|| = 1")
    print(f"   that is {np.linalg.norm(data_from_null) / np.linalg.norm(d_clean):.3e} "
          f"of the data norm and "
          f"{np.linalg.norm(data_from_null) / NOISE_NT:.3e} of the noise level")
    # A physically interesting null-space member: project a deep-cell indicator
    # onto the null space, so the added magnetisation sits at depth.
    deep = (cell_z / KM >= 5.0).astype(float)
    proj = deep - Vt[:rank].T @ (Vt[:rank] @ deep)
    proj /= np.linalg.norm(proj)
    amp = 20.0
    M_alt = M_true + amp * proj
    dd = G @ M_alt - d_clean
    print(f"take the null-space part of a 'deep cells only' indicator, unit norm, and")
    print(f"add {amp:.0f} A/m of it to the true model:")
    deep_frac = np.sum(proj[cell_z / KM >= 5.0] ** 2) / np.sum(proj ** 2)
    print(f"   {deep_frac * 100:.1f}% of the perturbing model's energy lies below 5 km; "
          f"max |magnetisation| {M_true.max():.2f} -> {np.abs(M_alt).max():.2f} A/m")
    print(f"   ||M_alt - M_true|| / ||M_true|| = "
          f"{np.linalg.norm(M_alt - M_true) / np.linalg.norm(M_true):.3f}")
    print(f"   change in the predicted data = "
          f"{np.linalg.norm(dd) / np.linalg.norm(d_clean):.3e} of the data norm")
    print("   a null-space perturbation is by construction invisible in this")
    print("   parametrisation, however large it is.")

    section("4. Tikhonov inversion and the trade-off")
    zc = cell_z
    W = np.diag(1.0 / (np.sqrt(zc / KM) ** 1.0))     # gentle depth weighting
    print("   lambda   data misfit (nT rms)   model norm   recovered peak (A/m)")
    best = None
    for lam in (1e-6, 1e-3, 1e-1, 1.0, 10.0, 1e2, 1e3):
        m = tikhonov(G, d, W, lam)
        misfit = np.linalg.norm(G @ m - d) / np.sqrt(N_DATA)
        print(f"   {lam:8.0e}   {misfit:21.4f}   {np.linalg.norm(W @ m):11.3f}   "
              f"{m.max():21.3f}")
        if best is None or abs(misfit - NOISE_NT) < abs(best[1] - NOISE_NT):
            best = (lam, misfit, m)
    lam_best, misfit_best, m_best = best
    print(f"   the misfit level of the noise is {NOISE_NT:.2f} nT rms; the closest "
          f"lambda is {lam_best:g}")
    print(f"   at that lambda the misfit is {misfit_best:.3f} nT and the recovered "
          f"peak is {m_best.max():.2f} A/m against a true {M_true.max():.2f} A/m")

    section("5. Depth weighting")
    m_now = tikhonov(G, d, np.eye(n_model), lam_best)
    depth_mean_now = np.sum(np.abs(m_now) * zc) / np.sum(np.abs(m_now))
    depth_mean_w = np.sum(np.abs(m_best) * zc) / np.sum(np.abs(m_best))
    depth_mean_true = np.sum(M_true * zc) / np.sum(M_true)
    print(f"   centroid depth of the true model            {depth_mean_true / KM:.2f} km")
    print(f"   centroid depth without depth weighting      {depth_mean_now / KM:.2f} km")
    print(f"   centroid depth with sqrt-depth weighting    {depth_mean_w / KM:.2f} km")
    print("   without a depth weight the inversion satisfies the data with magnetic")
    print("   material as close to the surface as possible; the weight pushes it down")

    section("6. A positivity constraint")
    A = np.vstack([G, np.sqrt(lam_best) * W])
    b = np.concatenate([d, np.zeros(n_model)])
    m_nn, res = nnls(A, b)
    print(f"unconstrained peak {m_best.max():7.3f} A/m, "
          f"negative cells {int(np.sum(m_best < -0.01))} of {n_model}")
    print(f"non-negative   peak {m_nn.max():7.3f} A/m, misfit "
          f"{np.linalg.norm(G @ m_nn - d) / np.sqrt(N_DATA):.3f} nT rms")
    print(f"total moment-sum, unconstrained {np.sum(m_best) * (CELL_KM * KM) ** 3:.3e}, "
          f"true {np.sum(M_true) * (CELL_KM * KM) ** 3:.3e}, "
          f"non-negative {np.sum(m_nn) * (CELL_KM * KM) ** 3:.3e} A m^2")
    print(f"   the two inverted models differ by "
          f"{np.linalg.norm(m_best - m_nn) / np.linalg.norm(m_best) * 100:.1f}% and fit")
    print("   the same data: the data cannot choose between them.")

    section("7. Summary for the lesson")
    print(f"  singular value range: {s[0] / s[-1]:.2e}; {n_small} directions below 1e-6")
    print(f"  annihilator: 20 A/m perturbation -> data change "
          f"{np.linalg.norm(G @ M_alt - d_clean) / np.linalg.norm(d_clean):.2e} of the norm")
    print(f"  true peak {M_true.max():.2f} A/m -> recovered {m_best.max():.2f} A/m")
    print(f"  true centroid depth {depth_mean_true / KM:.2f} km -> recovered "
          f"{depth_mean_w / KM:.2f} km")
    print("  a magnetic inversion does not return an Earth: it returns one member of")
    print("  a family, and the family has to be described.")


if __name__ == "__main__":
    main()
