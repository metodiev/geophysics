#!/usr/bin/env python3
"""Underdetermined problems, minimum-norm solutions and other selection rules.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python underdetermined_demo.py

Everything here is SYNTHETIC: a toy transmission problem with chosen rays and a
chosen true slowness field, used only to demonstrate algebra.

Contents
--------
1. Fewer data than parameters: the linear system and its feasible set.
2. The minimum-norm solution from the SVD, and its defining properties.
3. What varies inside the feasible set when the norm cannot.
4. Three selection rules, three different models, one identical fit:
   minimum norm, minimum roughness, and sparsity (L1).
5. Report a range, not a point.
"""

import numpy as np
from scipy.optimize import linprog

RNG = np.random.default_rng(20261014)

NC = 8                                       # cells (model parameters)
RAYS = {
    "R1 cells 0-3": [0, 1, 2, 3],
    "R2 cells 2-5": [2, 3, 4, 5],
    "R3 cells 4-7": [4, 5, 6, 7],
}
M_TRUE = np.array([0.30, 0.36, 0.10, 0.14, 0.22, 0.30, 0.12, 0.16])   # s/km


def coverage_matrix():
    G = np.zeros((len(RAYS), NC))
    for i, cells in enumerate(RAYS.values()):
        G[i, cells] = 1.0
    return G


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    G = coverage_matrix()
    d = G @ M_TRUE
    N, M = G.shape

    section("1. The underdetermined problem")
    print(f"  model: {M} cell slownesses in s/km; data: {N} travel-time residuals in s")
    for name, cells in RAYS.items():
        print(f"    {name}  covers cells {cells}")
    print(f"  G is {N} x {M}: N < M, so the system is underdetermined")
    print(f"  data d (s, exact): {np.array2string(d, precision=4)}")
    U, s, Vt = np.linalg.svd(G)
    V = Vt[:s.size].T
    rank = int(np.sum(s > 1e-10 * s[0]))
    print(f"  singular values: {np.array2string(s, precision=4)}")
    print(f"  rank = {rank}, null-space dimension = {M - rank}")
    print("  All singular values are non-zero, so the matrix has full ROW rank and the")
    print("  data can always be fitted exactly: existence is not the problem here.")
    print("  Uniqueness is.")

    section("2. Minimum-norm solution and why it is minimal")
    Gp = (V / s) @ U.T
    m_min = Gp @ d
    print(f"  m_min = {np.array2string(m_min, precision=5)} s/km")
    print(f"  ||G m_min - d||_inf = {np.max(np.abs(G @ m_min - d)):.3e} s  (exact fit)")
    print(f"  ||m_min|| = {np.linalg.norm(m_min):.6f} s/km")
    proxy = G.T @ np.linalg.solve(G @ G.T, d)               # m = G^T (G G^T)^-1 d
    print(f"  G^T (G G^T)^-1 d = {np.array2string(proxy, precision=5)} s/km")
    print(f"  max difference from the SVD route = {np.max(np.abs(proxy - m_min)):.3e}")
    print(f"  ||m_min - projection onto row space|| = "
          f"{np.linalg.norm(m_min - V @ (V.T @ m_min)):.3e} s/km")
    print("  property 1: m_min lies in range(G^T), i.e. it has no null-space part.")
    Z = Vt[rank:].T
    print("  property 2: sweep the null-space amplitude ||w|| and record ||m||:")
    print("    ||w||     ||m_min + Z w||      sqrt(||m_min||^2 + ||w||^2)")
    for scale in (0.0, 0.01, 0.05, 0.2, 0.5):
        w = RNG.standard_normal(Z.shape[1])
        w *= scale / max(np.linalg.norm(w), 1e-300)
        m = m_min + Z @ w
        print(f"    {scale:5.2f}     {np.linalg.norm(m):16.6f}     "
              f"{np.sqrt(np.linalg.norm(m_min) ** 2 + scale ** 2):24.6f}")
    print("  The measured norms match sqrt(||m_min||^2 + ||w||^2) to six decimals, and")
    print("  the minimum is at ||w|| = 0: for any null-space vector,")
    print("  ||m_min + Z w||^2 - ||m_min||^2 = ||w||^2 >= 0.  No feasible model has a")
    print("  smaller norm, and m_min is the point of the feasible set closest to the")
    print("  origin.")

    section("3. What varies inside the feasible set when the norm cannot")
    samples = []
    for _ in range(2000):
        w = RNG.standard_normal(Z.shape[1])
        w *= 0.2 / np.linalg.norm(w)
        samples.append(m_min + Z @ w)
    samples = np.array(samples)
    print("  2000 feasible models with ||null-space part|| = 0.2 s/km:")
    print("   quantity                       min          max        spread")
    for label, vals in (("cell 0", samples[:, 0]), ("cell 1", samples[:, 1]),
                        ("cell 2", samples[:, 2]), ("cell 3", samples[:, 3]),
                        ("m0+m1+m2+m3 (ray 1)", samples[:, 0] + samples[:, 1] +
                         samples[:, 2] + samples[:, 3]),
                        ("||m||", np.linalg.norm(samples, axis=1))):
        print(f"   {label:28s} {vals.min():10.4f}   {vals.max():10.4f}   "
              f"{vals.max() - vals.min():8.4f}")
    print(f"  Every sample has data residual <= "
          f"{np.max(np.abs(samples @ G.T - d)):.2e} s.")
    print("  The measured combination is pinned to 0.9000 s; individual cells move by")
    print("  up to about 0.31 s/km.  Reporting a cell value is reporting the norm's")
    print("  preference, not the data's.")

    section("4. Three selection rules, one identical fit")
    D = np.diff(np.eye(NC), axis=0)                   # first-difference operator
    m_rough = np.linalg.solve(
        np.block([[G.T @ G + 1e-6 * D.T @ D, G.T], [G, np.zeros((N, N))]]),
        np.concatenate([np.zeros(NC), d]))[:NC]
    res = linprog(np.ones(NC), A_eq=G, b_eq=d, bounds=[(0, None)] * NC,
                  method="highs")
    m_sparse = res.x
    print("   rule               ||m||_2   ||Dm||_2   ||m||_1   non-zero cells")
    for name, m in (("minimum norm", m_min), ("minimum roughness", m_rough),
                    ("sparse (L1)", m_sparse)):
        nnz = int(np.sum(np.abs(m) > 1e-8))
        print(f"   {name:18s} {np.linalg.norm(m):7.4f}   {np.linalg.norm(D @ m):8.4f}   "
              f"{np.sum(np.abs(m)):7.4f}   {nnz:13d}")
    print("   rule               residual ||Gm - d||_inf (s)")
    for name, m in (("minimum norm", m_min), ("minimum roughness", m_rough),
                    ("sparse (L1)", m_sparse)):
        print(f"   {name:18s} {np.max(np.abs(G @ m - d)):.3e}")
    print("   m for each rule (s/km):")
    for name, m in (("minimum norm", m_min), ("minimum roughness", m_rough),
                    ("sparse (L1)", m_sparse)):
        print(f"     {name:18s} {np.array2string(m, precision=4, floatmode='fixed')}")
    print("  All three fit the data to machine precision and they are different")
    print("  pictures of the same measurement: a smooth field, a rough-but-minimal")
    print("  field, and a field confined to three cells.  The rule is an assumption.")

    section("5. Report a range, not a point")
    print("  feasible set: G m = d and 0 <= m_j <= 1 s/km; interval per cell")
    print("   cell   [min, max] (s/km)     width")
    bounds = [(0.0, 1.0)] * NC
    for j in range(NC):
        c = np.zeros(NC)
        c[j] = 1.0
        lo = linprog(c, A_eq=G, b_eq=d, bounds=bounds, method="highs")
        hi = linprog(-c, A_eq=G, b_eq=d, bounds=bounds, method="highs")
        print(f"   {j:4d}   [{lo.x[j]:.4f}, {hi.x[j]:.4f}]   {hi.x[j] - lo.x[j]:.4f}")
    c = np.array([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])
    lo = linprog(c, A_eq=G, b_eq=d, bounds=bounds, method="highs")
    hi = linprog(-c, A_eq=G, b_eq=d, bounds=bounds, method="highs")
    print(f"   ray-1 sum m0+m1+m2+m3: [{lo.fun:.4f}, {-hi.fun:.4f}]  "
          f"width {-hi.fun - lo.fun:.4f}")
    print("  Every individual cell has lower bound 0 and a width near the ray value,")
    print("  because each cell shares its rays with partners that can carry the whole")
    print("  load.  The ray sum, by contrast, is fixed exactly.  Report the resolved")
    print("  combination, or the interval, but never a bare cell value.")
    print("\n  All models and data in this demonstration are SYNTHETIC.")


if __name__ == "__main__":
    main()
