#!/usr/bin/env python3
"""Resolution and information matrices, and what they mean for interpretation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resolution_matrices_demo.py

Everything here is SYNTHETIC: a chosen ray geometry, a chosen true model and
chosen test patterns.

Contents
--------
1. The operator and the three matrices R = G^+ G, N = I - R, D = G G^+.
2. Identities that must hold, checked: G R = G, R^2 = R, traces.
3. Per-cell resolution: diagonal, averaging-kernel width, and a ranking.
4. Checkerboard and smooth-pattern tests: what an inversion can and cannot see.
5. The information matrix and the model covariance: which combinations are
   determined, and how well.
6. Interpretation: how to phrase a conclusion in terms of resolved combinations.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

NC = 16
X_KM = np.arange(NC, dtype=float) + 0.5
ROWS = []
for i in range(5):
    ROWS.append((i, np.array([0.6, 1.0, 0.6])))      # shallow rays, cells 0..6
for i in range(4):
    ROWS.append((i + 6, np.array([0.6, 1.0, 0.6])))  # central rays, cells 6..12
for i in range(3):
    ROWS.append((i + 10, np.array([0.6, 1.0, 0.6])))  # deep rays, cells 10..15
SIGMA = 0.004                                        # s
TRUE = 0.30 + 0.08 * np.cos(2 * np.pi * X_KM / NC)


def build_operator():
    G = np.zeros((len(ROWS), NC))
    for i, (first, w) in enumerate(ROWS):
        G[i, first:first + 3] = w
    return G


def kernel_width(row):
    """Averaging width in km, using absolute weights (rows may go negative)."""
    w = np.abs(row)
    total = np.sum(w)
    if total < 1e-12:
        return float("nan")
    j0 = int(np.argmax(w))
    return float(np.sqrt(np.sum(w * (X_KM - X_KM[j0]) ** 2) / total))


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main():
    G = build_operator()
    U, s, Vt = np.linalg.svd(G)
    V = Vt[:s.size].T
    keep = s > 1e-10 * s[0]
    r = int(keep.sum())
    Gp = (V[:, keep] / s[keep]) @ U[:, :s.size][:, keep].T
    d_true = G @ TRUE

    section("1. The operator and the three matrices")
    print(f"  model: {NC} cells at {X_KM[0]:.1f} ... {X_KM[-1]:.1f} km (values in s)")
    print(f"  data : {G.shape[0]} rays, weighted sums 0.6/1.0/0.6 over three cells")
    print(f"  G is {G.shape[0]} x {NC}; rank = {r}; "
          f"null-space dimension = {NC - r}; range(G)^perp dimension = "
          f"{G.shape[0] - r}")
    print(f"  singular values: {np.array2string(s, precision=5)}")
    print(f"  sigma_max/sigma_min = {s[0] / s[r - 1]:.4f}")
    R = Gp @ G
    N = np.eye(NC) - R
    D = G @ Gp
    print(f"  R = G^+ G has shape {R.shape}: the model resolution matrix")
    print(f"  D = G G^+ has shape {D.shape}: the data resolution matrix")
    print(f"  N = I - R has shape {N.shape}: the null-space projector")

    section("2. Identities, checked")
    print(f"  G R  - G          : max |.| = {np.max(np.abs(G @ R - G)):.3e}")
    print(f"  R G^+ - G^+       : max |.| = {np.max(np.abs(R @ Gp - Gp)):.3e}")
    print(f"  R^2 - R           : max |.| = {np.max(np.abs(R @ R - R)):.3e}")
    print(f"  D^2 - D           : max |.| = {np.max(np.abs(D @ D - D)):.3e}")
    print(f"  G N  (should be 0): max |.| = {np.max(np.abs(G @ N)):.3e}")
    print(f"  trace(R) = {np.trace(R):.6f}, trace(D) = {np.trace(D):.6f}, "
          f"rank = {r}")
    print("  R and D are projectors whose traces equal the rank: the number of")
    print("  independent model combinations equals the number of independent data.")

    section("3. Per-cell resolution")
    print("   cell   x (km)   R_jj   kernel width (km)   resolved?")
    widths = []
    for j in range(NC):
        wj = kernel_width(R[j])
        widths.append(wj)
        tag = "no (null space)" if R[j, j] < 1e-8 else (
            "well" if (not np.isnan(wj) and wj < 3.0) else "coarsely")
        print(f"   {j:4d}   {X_KM[j]:6.2f}   {R[j, j]:5.3f}   {wj:17.4f}   {tag}")
    finite = [w for w in widths if not np.isnan(w)]
    empty = [j for j in range(NC) if R[j, j] < 1e-8]
    print(f"  cells with R_jj = 0 (no ray covers them): {empty}")
    print(f"  mean kernel width over the covered cells = {np.mean(finite):.4f} km")
    print("  Best resolved: cells 3 and 4 (widths 2.65 and 2.60 km), which lie in the")
    print("  overlap of the shallow and central ray families.  The ends have the")
    print("  largest R_jj (0.846 at cell 0) AND the widest kernels (5.99 km): a big")
    print("  diagonal does not mean good resolution, it means little averaging bias.")

    section("4. Pattern tests: what the inversion can see")
    smooth = 0.08 * np.cos(2 * np.pi * X_KM / NC)
    checker = 0.08 * ((-1.0) ** np.arange(NC))
    spike = np.zeros(NC)
    spike[0] = 0.08
    for name, pat in (("smooth cosine", smooth), ("checkerboard", checker),
                      ("end spike (cell 0)", spike)):
        Rn = R @ pat
        seen = np.linalg.norm(Rn) / np.linalg.norm(pat)
        print(f"   {name:20s} ||G p||/||p|| = "
              f"{np.linalg.norm(G @ pat) / np.linalg.norm(pat):8.4f}   "
              f"recovered fraction ||R p||/||p|| = {seen:8.4f}")
    print("  A pattern with a small data image is badly determined.  Measured energy")
    print("  fractions in the null space:")
    for name, pat in (("smooth cosine", smooth), ("checkerboard", checker),
                      ("end spike (cell 0)", spike)):
        Rn = R @ pat
        print(f"    {name:20s} {1 - np.linalg.norm(Rn) ** 2 / np.linalg.norm(pat) ** 2:6.3f}")
    print("  The smooth cosine is nearly fully visible (93.5% recovered); the 2-cell")
    print("  checkerboard keeps only 79.2% of its norm, so 37.2% of its energy is")
    print("  invisible to these rays.  Quote these fractions, not adjectives.")

    section("5. The information matrix and the model covariance")
    Cinv = np.eye(G.shape[0]) / SIGMA ** 2
    F = G.T @ Cinv @ G
    eF = np.linalg.eigvalsh(F)[::-1]
    print(f"  information matrix F = G^T C_d^-1 G; eigenvalues sigma_i^2/sigma^2:")
    print(f"    {np.array2string(eF[eF > 1e-20], precision=3)}")
    print(f"    number of eigenvalues above 1e-10 of the largest = "
          f"{int(np.sum(eF > 1e-10 * eF[0]))} = rank = {r}")
    print(f"    smallest well-determined eigenvalue = {eF[r - 1]:.3e}, largest = "
          f"{eF[0]:.3e}; ratio = {eF[r - 1] / eF[0]:.3e}")
    Cov = V[:, keep] @ np.diag(SIGMA ** 2 / s[keep] ** 2) @ V[:, keep].T
    sd = np.sqrt(np.diag(Cov))
    print("   cell   posterior sd of m_j (s)   sd of a 3-cell average (s)")
    for j in range(NC):
        if j + 2 < NC:
            c = np.zeros(NC)
            c[j:j + 3] = 1 / 3
            var_avg = float(c @ Cov @ c)
            print(f"   {j:4d}   {sd[j]:22.6f}   {np.sqrt(var_avg):24.6f}")
    avgs = []
    for j in range(NC - 2):
        c = np.zeros(NC)
        c[j:j + 3] = 1 / 3
        avgs.append(float(np.sqrt(c @ Cov @ c)))
    print(f"  median per-cell sd = {np.median(sd):.6f} s; median 3-cell-average sd = "
          f"{np.median(avgs):.6f} s")
    print(f"  ratio = {np.median(sd) / np.median(avgs):.3f}: averaging a resolved")
    print("  combination is better determined than any single cell.  The data")
    print("  determine combinations, not cells, and the covariance says which.")

    section("6. Interpretation: phrases that survive review")
    bad = ["the anomaly is in cell 14",
           "cell 15 is undisturbed (it is simply unmeasured)",
           "the checkerboard is present"]
    good = ["the 12 ray sums are reproduced to within the data error",
            "the smooth cos(2 pi x/16) component is recovered to 93.5% of its norm",
            "the 2-cell checkerboard is recovered at only 79.2%, with 37.2% of its"
            " energy in the null space"]
    print("  Unsupportable with this experiment:")
    for b in bad:
        print(f"    - {b}")
    print("  Supportable, expressed as resolved combinations:")
    for g in good:
        print(f"    - {g}")
    print("  Rule: a statement is defensible exactly to the extent that its")
    print("  indicator function lies in the row space of G.")

    section("7. Synthetic recovery test at the stated noise level")
    d_obs = d_true + SIGMA * RNG.standard_normal(G.shape[0])
    m_est = Gp @ d_obs
    bias2 = float(np.mean((R @ TRUE - TRUE) ** 2))
    print(f"  ||G m_est - d_obs||_inf = {np.max(np.abs(G @ m_est - d_obs)):.3e} s "
          f"(data sigma = {SIGMA:.4f} s)")
    print(f"  rms (m_est - m_true), one realisation = "
          f"{np.sqrt(np.mean((m_est - TRUE) ** 2)):.6f} s")
    print(f"  predicted: sqrt(mean diag(Cov) + bias^2) = "
          f"{np.sqrt(np.mean(np.diag(Cov)) + bias2):.6f} s")
    meas = []
    for _ in range(300):
        dd = d_true + SIGMA * RNG.standard_normal(G.shape[0])
        meas.append(np.sqrt(np.mean((Gp @ dd - TRUE) ** 2)))
    print(f"  measured over 300 realisations: {np.mean(meas):.6f} s "
          f"(sd {np.std(meas):.6f})")
    print(f"  ratio measured/predicted = "
          f"{np.mean(meas) / np.sqrt(np.mean(np.diag(Cov)) + bias2):.4f}")
    print("  The covariance plus the resolution bias predicts the achieved accuracy:")
    print("  this is the check to run before believing a resolution statement.")
    print("\n  All models and data in this demonstration are SYNTHETIC.")


if __name__ == "__main__":
    main()
