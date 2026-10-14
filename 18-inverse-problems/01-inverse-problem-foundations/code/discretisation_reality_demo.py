#!/usr/bin/env python3
"""Discretisation, parameterisation and model choice.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python discretisation_reality_demo.py

Everything here is SYNTHETIC.  The density profile, the sensor depths and the
noise are chosen teaching values, not measurements.

Physics used (exact, stated): the vertical gravity of an infinite horizontal slab
of density rho and thickness h, measured at a point outside it, is +-2 pi G rho h,
positive when the slab lies BELOW the sensor.  Summing slabs is the Bouguer-slab
forward model for a horizontally layered Earth.

Contents
--------
1. The truth: a smooth density profile and the data it produces.
2. Discretisation error of the parameterisation, with the measured order.
3. The same data, five parameterisations: the answer moves with the grid.
4. Over-parameterisation: 100 blocks, effective rank 6, and what min-norm gives.
5. The equivalence class at fixed parameterisation: same fit, different answer.
6. Regularisation as a model choice.
7. A basis is a physical assumption: linear truth, blocks versus linear elements.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_CONST = 6.67430e-11                    # m^3 kg^-1 s^-2
SLAB = 2.0 * np.pi * G_CONST * 1e5       # mGal per (kg/m^3) per metre of slab

Z_TOP_KM, Z_BOT_KM = 0.0, 10.0
SENSOR_DEPTHS_KM = np.array([0.0, 1.0, 2.0, 4.0, 6.0, 8.0, 10.0])
N_FINE = 2000
TOL = 1e-10


def rho_true(z_km):
    """The SYNTHETIC true density profile, kg/m^3."""
    return 2700.0 + 30.0 * z_km + 120.0 * np.exp(-((z_km - 6.0) / 1.2) ** 2)


def slab_kernel(edges_km, sensor_depths_km):
    """G[j, k] in mGal per kg/m^3 for layers with the given edges."""
    G = np.zeros((sensor_depths_km.size, len(edges_km) - 1))
    for k in range(len(edges_km) - 1):
        z0, z1 = edges_km[k], edges_km[k + 1]
        for j, d in enumerate(sensor_depths_km):
            below = max(0.0, z1 - max(d, z0))
            above = max(0.0, min(d, z1) - z0)
            G[j, k] = SLAB * (below - above) * 1e3
    return G


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main():
    edges_f = np.linspace(Z_TOP_KM, Z_BOT_KM, N_FINE + 1)
    centres_f = 0.5 * (edges_f[:-1] + edges_f[1:])
    G_fine = slab_kernel(edges_f, SENSOR_DEPTHS_KM)
    m_fine = rho_true(centres_f)
    d_exact = G_fine @ m_fine

    section("1. The truth: a smooth density profile and its data")
    print("  SYNTHETIC profile rho(z) = 2700 + 30 z + 120 exp(-((z-6)/1.2)^2) kg/m^3")
    print(f"  z from {Z_TOP_KM:.1f} to {Z_BOT_KM:.1f} km; forward model = sum of slabs")
    print(f"  slab constant = 2*pi*G = {SLAB:.8f} mGal per (kg/m^3) per metre")
    print(f"  reference quadrature: {N_FINE} sublayers of "
          f"{(edges_f[1] - edges_f[0]) * 1e3:.1f} m")
    print(f"  sensors at depths {SENSOR_DEPTHS_KM} km ({SENSOR_DEPTHS_KM.size} readings)")
    print(f"  exact data (mGal): {np.array2string(d_exact, precision=5, sign='+')}")
    print(f"  numerical rank of the 7 x {N_FINE} kernel: "
          f"{np.linalg.matrix_rank(G_fine, tol=TOL)}")
    print("  The sensor at 10 km sees the entire stack from BELOW, so its reading is")
    print("  the exact negative of the surface reading: 7 numbers, 6 independent ones.")

    section("2. Discretisation error of the parameterisation")
    print("  Replace the smooth profile by M equal blocks, each holding its own")
    print("  average of the true profile.  Measure the data error this causes.")
    print("\n   M blocks   block (km)   ||d_M - d_exact|| / ||d_exact||")
    errs, thick = [], []
    for M in (2, 4, 8, 16, 32, 64):
        edges = np.linspace(Z_TOP_KM, Z_BOT_KM, M + 1)
        Gm = slab_kernel(edges, SENSOR_DEPTHS_KM)
        h = (Z_BOT_KM - Z_TOP_KM) / M
        avg = np.array([np.mean(rho_true(np.linspace(edges[k], edges[k + 1], 41)))
                        for k in range(M)])
        err = np.linalg.norm(Gm @ avg - d_exact) / np.linalg.norm(d_exact)
        errs.append(err)
        thick.append(h)
        print(f"   {M:8d}   {h:9.4f}   {err:28.3e}")
    slope = np.polyfit(np.log(thick[1:]), np.log(errs[1:]), 1)[0]
    print(f"\n  measured order over the last five refinements: slope = {slope:.3f}")
    print("  A block-averaged representation of a smooth profile converges as h^2.")
    print("  The block size therefore sets an accuracy floor that no inversion can")
    print("  remove: it is a statement about the model, not about the algorithm.")

    section("3. The same data, five parameterisations")
    noise = 2e-3 * np.abs(d_exact).max() * RNG.standard_normal(d_exact.size)
    d_obs = d_exact + noise
    print(f"  data noise rms = {noise.std():.4e} mGal "
          f"({noise.std() / np.abs(d_exact).max() * 100:.3f}% of peak)")
    print(f"  truth at z = 5 km: {np.interp(5.0, centres_f, m_fine):.1f} kg/m^3")
    print("\n   M blocks   data misfit   model error   rho at z = 5 km   min-norm ||m||")
    for M in (3, 4, 5, 7, 20):
        edges = np.linspace(Z_TOP_KM, Z_BOT_KM, M + 1)
        Gm = slab_kernel(edges, SENSOR_DEPTHS_KM)
        m_est, *_ = np.linalg.lstsq(Gm, d_obs, rcond=None)
        misfit = np.linalg.norm(Gm @ m_est - d_obs) / np.linalg.norm(d_obs)
        centres = 0.5 * (edges[:-1] + edges[1:])
        m_on_fine = np.interp(centres_f, centres, m_est)
        err = np.linalg.norm(m_on_fine - m_fine) / np.linalg.norm(m_fine)
        print(f"   {M:8d}   {misfit * 100:10.4f}%   {err * 100:10.4f}%   "
              f"{np.interp(5.0, centres, m_est):16.1f}   {np.linalg.norm(m_est):13.1f}")
    print(f"  Misfit is not monotone either (0.32% at M = 4, 0.17% at M = 5), but it")
    print("  is pinned at the noise level once M reaches the number of INDEPENDENT")
    print("  data (6).  Model error is worse: the 7-block model fits the data better")
    print("  than the 4-block model and sits further from the truth, because the")
    print("  underdetermined part is filled in by the norm-minimising rule, not by")
    print("  the physics.")

    section("4. Over-parameterisation: 100 blocks, effective rank 6")
    M = 100
    edges = np.linspace(Z_TOP_KM, Z_BOT_KM, M + 1)
    centres = 0.5 * (edges[:-1] + edges[1:])
    Gm = slab_kernel(edges, SENSOR_DEPTHS_KM)
    U, s, Vt = np.linalg.svd(Gm)
    keep = s > TOL * s[0]
    rank = int(keep.sum())
    V = Vt[:s.size].T
    print(f"  G is {Gm.shape[0]} x {M}; singular values above the noise-free")
    print(f"  tolerance {TOL:.0e}: {rank} of {s.size}; effective null space = {M - rank}")
    print(f"  ({M - s.size} exactly null directions plus the numerically empty 7th)")
    print(f"  sigma_1 = {s[0]:.6e}, sigma_7 = {s[6]:.6e}, ratio = {s[6] / s[0]:.3e}")
    print("  sigma_7/sigma_1 is at machine precision: the matrix is 'full rank' on")
    print("  paper and rank 6 in fact.")
    m_naive = V @ ((1.0 / s) * (U.T @ d_obs))
    print(f"  dividing by ALL seven singular values: ||m|| = {np.linalg.norm(m_naive):.3e} kg/m^3,")
    print(f"  rho(5 km) = {np.interp(5.0, centres, m_naive):.3e} kg/m^3  <- meaningless")
    m_pinv = np.linalg.pinv(Gm) @ d_obs
    print(f"  np.linalg.pinv truncates automatically (rcond = max(M,N)*eps = "
          f"{max(Gm.shape) * np.finfo(float).eps:.1e})")
    print(f"  and returns ||m|| = {np.linalg.norm(m_pinv):.1f} kg/m^3, rho(5 km) = "
          f"{np.interp(5.0, centres, m_pinv):.1f} kg/m^3.")
    print("  The usable answer must be truncated at a tolerance you declare.")

    section("5. The equivalence class: same fit, different answer")
    filt = np.where(keep, 1.0 / s, 0.0)
    m0 = V @ (filt * (U.T @ d_obs))
    Z = Vt[s.size:].T
    print(f"  truncated min-norm model: fit = "
          f"{np.linalg.norm(Gm @ m0 - d_obs) / np.linalg.norm(d_obs) * 100:.4f}% of ||d||, "
          f"||m|| = {np.linalg.norm(m0):.1f}, rho(5 km) = "
          f"{np.interp(5.0, centres, m0):.1f} kg/m^3")
    print(f"  null space of the truncated operator: {Z.shape[1]} directions; sampling")
    print("  300 models m0 + Z w with ||w|| = 5% of ||m0||:")
    fits, vals, norms = [], [], []
    for _ in range(300):
        w = RNG.standard_normal(Z.shape[1])
        w *= 0.05 * np.linalg.norm(m0) / np.linalg.norm(w)
        m = m0 + Z @ w
        fits.append(np.linalg.norm(Gm @ m - d_obs) / np.linalg.norm(d_obs))
        vals.append(np.interp(5.0, centres, m))
        norms.append(np.linalg.norm(m))
    print(f"    worst fit over the sample: {max(fits) * 100:.4f}% of ||d|| "
          f"(min-norm fit was {np.linalg.norm(Gm @ m0 - d_obs) / np.linalg.norm(d_obs) * 100:.4f}%)")
    print(f"    rho(5 km) ranges over [{min(vals):.1f}, {max(vals):.1f}] kg/m^3, "
          f"a spread of {max(vals) - min(vals):.1f} kg/m^3")
    print(f"    ||m|| = {norms[0]:.1f} kg/m^3 for every member of the sample, by")
    print("    construction: the perturbations are orthogonal to m0.")
    print("  All 300 models fit the data exactly as well as the min-norm model, have")
    print("  the same model norm, and disagree about the density at 5 km by 20% of the")
    print("  truth (2909.9 kg/m^3).  The data do not choose among them.")

    section("6. Regularisation as a model choice")
    print("   damping alpha   data misfit   model error   rho at z = 5 km   roughness")
    for alpha in (0.0, 1e-4, 1e-3, 1e-2, 3e-2, 1e-1):
        f = np.where(keep, s / (s ** 2 + alpha ** 2), 0.0)
        m = V @ (f * (U.T @ d_obs))
        m_on_fine = np.interp(centres_f, centres, m)
        print(f"   {alpha:13.0e}   "
              f"{np.linalg.norm(Gm @ m - d_obs) / np.linalg.norm(d_obs) * 100:10.4f}%   "
              f"{np.linalg.norm(m_on_fine - m_fine) / np.linalg.norm(m_fine) * 100:10.4f}%   "
              f"{np.interp(5.0, centres, m):16.1f}   "
              f"{np.sqrt(np.mean(np.diff(m, 2) ** 2)):9.2f}")
    print("  alpha = 0 is the truncated minimum-norm solution.  As alpha grows the")
    print("  misfit rises, the sharpest variation is damped away, and the number that")
    print("  gets reported moves: rho(5 km) goes from 2960.4 to 2785.9 kg/m^3 between")
    print("  alpha = 0 and alpha = 3e-2, a change of 175 kg/m^3, and by alpha = 0.1")
    print("  the model is over-smoothed (rho(5 km) = 1334.7 kg/m^3, misfit 60.6%).")
    print("  Alpha is a choice you make, so report it with the misfit it produced.")

    section("7. A basis is a physical assumption")
    rho_lin = lambda z: 2700.0 + 30.0 * z
    m_lin_fine = rho_lin(centres_f)
    d_lin = G_fine @ m_lin_fine
    K_fine = slab_kernel(edges_f, SENSOR_DEPTHS_KM)
    print("  Truth is now exactly linear in z: rho = 2700 + 30 z (kg/m^3).")
    print("\n   M blocks   block-basis data error   linear-basis data error")
    for M in (4, 8, 16, 32):
        e2 = np.linspace(Z_TOP_KM, Z_BOT_KM, M + 1)
        G2 = slab_kernel(e2, SENSOR_DEPTHS_KM)
        blk = np.array([np.mean(rho_lin(np.linspace(e2[k], e2[k + 1], 41)))
                        for k in range(M)])
        err_blk = np.linalg.norm(G2 @ blk - d_lin) / np.linalg.norm(d_lin)
        width = (Z_BOT_KM - Z_TOP_KM) / M
        GL = np.zeros((SENSOR_DEPTHS_KM.size, e2.size))
        for k in range(e2.size):
            GL[:, k] = K_fine @ np.clip(1.0 - np.abs(centres_f - e2[k]) / width, 0.0, None)
        coef, *_ = np.linalg.lstsq(GL, d_lin, rcond=None)
        err_lin = np.linalg.norm(GL @ coef - d_lin) / np.linalg.norm(d_lin)
        print(f"   {M:8d}   {err_blk:20.3e}   {err_lin:21.3e}")
    print("  The block basis has an O(h^2) representation error even though the truth")
    print("  is a straight line; the linear basis represents it exactly (machine")
    print("  precision).  Parameterising in blocks asserts that the Earth is")
    print("  piecewise uniform.  That assertion, not the algorithm, sets the error.")
    print("\n  All models and data in this demonstration are SYNTHETIC.")


if __name__ == "__main__":
    main()
