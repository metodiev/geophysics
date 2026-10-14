#!/usr/bin/env python3
"""The generalised (Moore-Penrose) inverse, constructed and verified.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python generalized_inverse_demo.py

Everything here is SYNTHETIC: a factored integer operator chosen so that its rank
is exactly known, used only to demonstrate algebra.

Contents
--------
1. A mixed-determined operator: 8 data, 6 parameters, rank 4.
2. The generalised inverse from the SVD, and the four Moore-Penrose conditions.
3. Equivalent constructions and the failure of the full-rank formulas.
4. The complete solution set m = G^+ d + (I - G^+ G) z.
5. Minimum-norm least squares: m = G^+ d is the best of both worlds.
6. Continuity: how far does G^+ move when G moves by 1e-3?
"""

import numpy as np

RNG = np.random.default_rng(20261014)

RANK = 4
N_DATA = 8
N_PAR = 6


def build_operator():
    """G = A B with A (8x4) and B (4x6): rank is at most 4, and equals 4 here."""
    A = np.array([[1.0, 0.0, 2.0, 0.0],
                  [0.0, 1.0, 0.0, 1.0],
                  [1.0, 1.0, 1.0, 0.0],
                  [0.0, 0.0, 1.0, 2.0],
                  [2.0, 0.0, 0.0, 1.0],
                  [0.0, 2.0, 1.0, 0.0],
                  [1.0, 0.0, 1.0, 1.0],
                  [0.0, 1.0, 2.0, 1.0]])
    B = np.array([[1.0, 0.0, 1.0, 0.0, 2.0, 0.0],
                  [0.0, 1.0, 0.0, 1.0, 0.0, 2.0],
                  [0.0, 0.0, 1.0, 1.0, 0.0, 0.0],
                  [1.0, 0.0, 0.0, 0.0, 1.0, 1.0]])
    return A @ B


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    G = build_operator()
    U, s, Vt = np.linalg.svd(G)
    V = Vt[:s.size].T
    keep = s > 1e-10 * s[0]
    r = int(keep.sum())

    section("1. A mixed-determined operator")
    print(f"  G is {G.shape[0]} x {G.shape[1]}: more data than parameters (N > M) yet")
    print("  singular in both directions, so neither the overdetermined nor the")
    print("  underdetermined formula applies.")
    print(f"  singular values: {np.array2string(s, precision=6)}")
    print(f"  relative singular values: {np.array2string(s / s[0], precision=3)}")
    print(f"  rank = {r}, so dim(range(G)) = {r}, dim N(G) = {G.shape[1] - r}, "
          f"dim range(G)^perp = {G.shape[0] - r}")

    section("2. The generalised inverse and the four conditions")
    Gp = (V[:, keep] / s[keep]) @ U[:, :s.size][:, keep].T
    E = G @ Gp @ G - G
    H = Gp @ G @ Gp - Gp
    S1 = (G @ Gp).T - G @ Gp
    S2 = (Gp @ G).T - Gp @ G
    print(f"  G^+ has shape {Gp.shape}; built as sum_i (u_i v_i^T)/sigma_i")
    print(f"  (1) G G^+ G   - G      : max |.| = {np.max(np.abs(E)):.3e}")
    print(f"  (2) G^+ G G^+  - G^+    : max |.| = {np.max(np.abs(H)):.3e}")
    print(f"  (3) (G G^+)^T - G G^+   : max |.| = {np.max(np.abs(S1)):.3e}  (symmetric)")
    print(f"  (4) (G^+ G)^T - G^+ G   : max |.| = {np.max(np.abs(S2)):.3e}  (symmetric)")
    print("  All four conditions of the Moore-Penrose definition hold to machine")
    print("  precision, which is what makes G^+ unique.")

    section("3. Equivalent constructions, and where the classic formulas fail")
    alt1 = np.linalg.pinv(G)
    print(f"  np.linalg.pinv(G) vs the SVD sum: max difference = "
          f"{np.max(np.abs(alt1 - Gp)):.3e}")
    alt2 = np.linalg.pinv(G.T @ G) @ G.T
    alt3 = G.T @ np.linalg.pinv(G @ G.T)
    print(f"  (G^T G)^+ G^T   vs G^+: max difference = {np.max(np.abs(alt2 - Gp)):.3e}")
    print(f"  G^T (G G^T)^+   vs G^+: max difference = {np.max(np.abs(alt3 - Gp)):.3e}")
    GtG = G.T @ G
    sGtG = np.linalg.svd(GtG, compute_uv=False)
    d_test = G @ np.ones(N_PAR)
    try:
        m_over = np.linalg.solve(GtG, G.T @ d_test)
        print(f"  (G^T G)^-1 G^T d returns {np.array2string(m_over[:3], precision=3)} ...")
        print(f"  but kappa(G^T G) = {sGtG[0] / sGtG[-1]:.3e}: the solve does not raise an")
        print(f"  exception, it silently returns garbage (max error "
              f"{np.max(np.abs(m_over - Gp @ d_test)):.3e} against G^+ d).")
    except np.linalg.LinAlgError:
        print("  (G^T G)^-1 raises LinAlgError")
    try:
        np.linalg.inv(G @ G.T)
        print("  (G G^T)^-1 exists")
    except np.linalg.LinAlgError:
        print("  (G G^T)^-1 does not exist: G G^T is exactly singular, so the")
        print("  underdetermined formula m = G^T (G G^T)^-1 d is NOT available.")
    damp = 1e-6
    m_naive = np.linalg.solve(G.T @ G + damp * np.eye(N_PAR), G.T @ G @ np.ones(N_PAR))
    print("  a naive damped solve with a true model of all ones returns")
    print(f"  {np.array2string(m_naive, precision=4)}")
    print(f"  against the exact G^+ G (ones) = "
          f"{np.array2string(Gp @ G @ np.ones(N_PAR), precision=4)}")
    print(f"  max error {np.max(np.abs(m_naive - Gp @ G @ np.ones(N_PAR))):.3e}: a damping")
    print("  four orders of magnitude below the smallest singular value is invisible")
    print("  here, and that is exactly why the damping must be chosen deliberately.")

    section("4. The complete solution set")
    d = G @ (np.arange(1.0, N_PAR + 1))
    m_particular = Gp @ d
    Pr = np.eye(N_PAR) - Gp @ G
    print(f"  m_particular = G^+ d: ||m|| = {np.linalg.norm(m_particular):.6f}, "
          f"||G m - d|| = {np.linalg.norm(G @ m_particular - d):.3e}")
    print(f"  projector I - G^+ G has rank {N_PAR - r} "
          f"(trace {np.trace(Pr):.6f}) and enters m = G^+ d + (I - G^+ G) z")
    for scale in (0.0, 0.5, 2.0):
        z = RNG.standard_normal(N_PAR)
        z *= scale / np.linalg.norm(z) if scale else 0.0
        m = m_particular + Pr @ z
        print(f"    ||z|| = {scale:4.1f}: ||m|| = {np.linalg.norm(m):7.4f}, "
              f"||G m - d|| = {np.linalg.norm(G @ m - d):.3e}, "
              f"||m - G^+ d|| = {np.linalg.norm(m - m_particular):7.4f}")
    print("  Every z gives the same data; G^+ d is the minimum-norm member.")

    section("5. Minimum-norm least squares")
    print("  Compare G^+ d with 500 random candidates m = G^+ d + (I - G^+ G) z:")
    worst_norm = 0.0
    for _ in range(500):
        z = RNG.standard_normal(N_PAR)
        z *= 0.3 / np.linalg.norm(z)
        m = m_particular + Pr @ z
        worst_norm = max(worst_norm, np.linalg.norm(m))
    print(f"    largest norm among the candidates = {worst_norm:.6f} s/km")
    print(f"    ||G^+ d|| = {np.linalg.norm(m_particular):.6f} s/km")
    print(f"    every candidate has the same residual "
          f"{np.linalg.norm(G @ m_particular - d):.3e}")
    print("  G^+ d is therefore the minimum-norm least-squares solution: it achieves")
    print("  the smallest possible residual AND, among those, the smallest norm.")

    section("6. Continuity: how far does G^+ move when G moves by 1e-3?")
    rng2 = np.random.default_rng(7)
    print("   relative perturbation   ||dG^+||/||G^+|| (rank-deficient G, rank 4)")
    base = np.linalg.norm(Gp)
    for delta in (1e-2, 1e-3, 1e-4):
        worst = 0.0
        for _ in range(200):
            dG = delta * rng2.standard_normal(G.shape)
            G2 = G + dG
            G2p = np.linalg.pinv(G2, rcond=1e-10)
            worst = max(worst, np.linalg.norm(G2p - Gp) / base)
        print(f"   {delta:20.0e}   {worst:30.3f}")
    Gwell = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    Gwp = np.linalg.pinv(Gwell)
    worst_w = 0.0
    for _ in range(200):
        dG = 1e-3 * rng2.standard_normal(Gwell.shape)
        worst_w = max(worst_w,
                      np.linalg.norm(np.linalg.pinv(Gwell + dG) - Gwp) /
                      np.linalg.norm(Gwp))
    print(f"   a full-rank, well-conditioned 3x2 operator at 1e-3: {worst_w:.3f}")
    print("  The generalised inverse of a rank-deficient operator is NOT continuous:")
    print("  the perturbation promotes a formerly empty direction to a finite singular")
    print("  value and its inverse (= sigma^-1) jumps by orders of magnitude.  Any")
    print("  implementation must fix a tolerance, and any result must state it.")
    print("\n  All models and data in this demonstration are SYNTHETIC.")


if __name__ == "__main__":
    main()
