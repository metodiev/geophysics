#!/usr/bin/env python3
"""Null space, non-uniqueness and equivalence classes, demonstrated exactly.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python null_space_demo.py

Everything here is SYNTHETIC.  The 4x4 slowness grid and the ray coverage below
are a chosen teaching experiment, not a real tomographic survey.

Contents
--------
1. Build G from a stated ray-coverage pattern; data are exact (noise-free).
2. Rank-nullity: rank, null-space dimension, and explicit null vectors.
3. Two models in the same equivalence class give bit-identical data.
4. What the data DO determine: exact feasible interval for every cell, solved
   as a linear program over the equivalence class.
5. What combinations are determined: interval for a cell-weighted target.
6. Normal-equation conditioning: kappa(G^T G) = kappa(G)^2, and the null space
   is unchanged.
"""

import numpy as np
from scipy.optimize import linprog

RNG = np.random.default_rng(20261014)

NROW = NCOL = 4
NC = NROW * NCOL
# Ranges are (row, col) index lists; all rays travel 4 cells.
RAYS = {
    "R1 row 0": [0, 1, 2, 3],
    "R2 row 1": [4, 5, 6, 7],
    "R3 row 3": [12, 13, 14, 15],
    "R4 column 1": [1, 5, 9, 13],
    "R5 diagonal": [0, 5, 10, 15],
}


def coverage_matrix():
    G = np.zeros((len(RAYS), NC))
    for i, cells in enumerate(RAYS.values()):
        G[i, cells] = 1.0
    return G


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def solve_interval(c, A_eq, b_eq, lo=0.0, hi=1.0):
    """Exact [min, max] of c.m over {m: A_eq m = b_eq, lo <= m <= hi}."""
    bounds = [(lo, hi)] * A_eq.shape[1]
    lo_res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")
    hi_res = linprog(-c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")
    if not lo_res.success or not hi_res.success:
        return None
    return lo_res.fun, -hi_res.fun


def main():
    Gmat = coverage_matrix()
    m_true = np.zeros(NC)
    m_true[[0, 5, 10, 15]] = 0.30          # a chosen, reproducible anomaly
    m_true[1] = 0.10
    d = Gmat @ m_true

    section("1. The experiment: 5 rays through 16 cells")
    print(f"  model space: {NROW} x {NCOL} = {NC} cells, one scalar per cell")
    print(f"  data space : {len(RAYS)} rays, each the SUM of cell values along it")
    for name, cells in RAYS.items():
        print(f"    {name:14s} covers cells {cells}")
    print(f"  G is {Gmat.shape[0]} x {Gmat.shape[1]}, entries 0 or 1 (path length)")
    print(f"  data d (noise-free, exact): {np.array2string(d, precision=4)}")

    section("2. Rank-nullity and explicit null vectors")
    U, s, Vt = np.linalg.svd(Gmat)
    rank = int(np.sum(s > 1e-10 * s[0]))
    nullity = NC - rank
    print(f"  singular values: {np.array2string(s, precision=4)}")
    print(f"  rank(G) = {rank},  M - rank = {nullity}")
    print(f"  rank-nullity identity: {rank} + {nullity} = {rank + nullity} = M  ✔")
    Z = Vt[rank:].T                                  # columns span N(G)
    print(f"  orthonormal basis of N(G): {Z.shape[1]} vectors, "
          f"max |G Z| = {np.max(np.abs(Gmat @ Z)):.3e}")
    print(f"  ||Z^T Z - I||_inf = {np.max(np.abs(Z.T @ Z - np.eye(nullity))):.3e}")
    missing = [j for j in range(NC) if np.all(Gmat[:, j] == 0)]
    print(f"  cells no ray visits: {missing} -> the unit vectors e_j for these")
    print("  cells are themselves null vectors: 'structural' null space.")
    exchange = np.zeros(NC)
    exchange[2], exchange[3] = 1.0, -1.0             # both in row 0, same ray
    print(f"  an 'exchange' null vector inside one ray: G n = "
          f"{np.max(np.abs(Gmat @ exchange)):.3e}")
    print("  Swapping material between two cells that share every ray changes")
    print("  nothing: that is the trade-off null space of any tomography problem.")

    section("3. Same data, different models, to machine precision")
    m_min = np.linalg.pinv(Gmat) @ d
    n1 = Z[:, 0]
    m_alt = m_min + 0.5 * n1
    print(f"  m_min = pinv(G) d            ||m_min||   = {np.linalg.norm(m_min):.4f}")
    print(f"  m_alt = m_min + 0.5 n1       ||m_alt||   = {np.linalg.norm(m_alt):.4f}")
    print(f"  ||G m_min - d||_inf = {np.max(np.abs(Gmat @ m_min - d)):.3e}")
    print(f"  ||G m_alt - d||_inf = {np.max(np.abs(Gmat @ m_alt - d)):.3e}")
    print(f"  ||m_alt - m_min|| / ||m_min|| = "
          f"{np.linalg.norm(m_alt - m_min) / np.linalg.norm(m_min):.4f}")
    print("  Both models fit the data to machine precision.  The data cannot")
    print("  choose between them; only a prior, a constraint or more data can.")

    section("4. What the data DO determine: exact feasible interval per cell")
    print("  Constraint set: G m = d with 0 <= m_j <= 1 (an assumed bound).")
    print("   cell   interval [min, max]      width     visited by any ray?")
    widths = []
    for j in range(NC):
        c = np.zeros(NC)
        c[j] = 1.0
        iv = solve_interval(c, Gmat, d)
        widths.append(iv[1] - iv[0])
        print(f"   {j:4d}   [{iv[0]:.4f}, {iv[1]:.4f}]   {iv[1] - iv[0]:7.4f}   "
              f"{'yes' if np.any(Gmat[:, j] > 0) else 'no'}")
    print(f"  {sum(w == 0.0 for w in widths)} cells are determined exactly, "
          f"{sum(w > 0.99 for w in widths)} cells span the whole bound, and the")
    print(f"  median interval width is {np.median(widths):.4f}.  Non-uniqueness is")
    print("  per-parameter and can be quantified, not merely asserted.")

    section("5. Determined versus undetermined COMBINATIONS")
    targets = {
        "sum of ray 1 cells (1,2,3,4)": [0, 1, 2, 3],
        "sum of column 3 cells (3,7,11,15)": [3, 7, 11, 15],
        "difference m_0 - m_3": None,
        "sum of all 16 cells": list(range(NC)),
    }
    for name, cells in targets.items():
        c = np.zeros(NC)
        if name == "difference m_0 - m_3":
            c[0], c[3] = 1.0, -1.0
        else:
            c[cells] = 1.0
        iv = solve_interval(c, Gmat, d)
        print(f"   {name:34s} interval [{iv[0]:.4f}, {iv[1]:.4f}]  "
              f"width {iv[1] - iv[0]:.4f}")
    print("  A combination that lies in the row space of G is pinned down; a")
    print("  combination with a null-space component is not.  Interpretation must")
    print("  be phrased in terms of what is determined, not of cells.")

    section("6. Normal equations square the condition number")
    s_tg = np.linalg.svd(Gmat.T @ Gmat, compute_uv=False)
    print(f"  sigma_max(G) = {s[0]:.4f}, sigma_min non-zero(G) = {s[rank - 1]:.4f}, "
          f"kappa(G) = {s[0] / s[rank - 1]:.4f}")
    print(f"  sigma_max(G^T G) = {s_tg[0]:.4f}, sigma_min non-zero = "
          f"{s_tg[rank - 1]:.4f}, kappa(G^T G) = {s_tg[0] / s_tg[rank - 1]:.4f}")
    print(f"  ratio kappa(G^T G) / kappa(G)^2 = "
          f"{(s_tg[0] / s_tg[rank - 1]) / (s[0] / s[rank - 1]) ** 2:.6f}")
    print(f"  numerical rank of G^T G = {int(np.sum(s_tg > 1e-10 * s_tg[0]))}, "
          f"identical null space dimension {NC - int(np.sum(s_tg > 1e-10 * s_tg[0]))}")
    print("  Forming the normal equations never removes the null space and it")
    print("  squares the conditioning: solve with the SVD or a QR factorisation.")
    print("\n  SYNTHETIC data; no real tomographic measurement is used here.")


if __name__ == "__main__":
    main()
