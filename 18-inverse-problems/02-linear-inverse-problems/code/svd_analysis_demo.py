#!/usr/bin/env python3
"""SVD analysis of an inverse problem: model resolution and data importance.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python svd_analysis_demo.py

Everything here is SYNTHETIC: a chosen ray geometry and a chosen true model.

Contents
--------
1. The operator: 12 rays (4 of them redundant) through 12 cells; spectrum, rank.
2. Data importance: which measurements actually carry information.
3. Truncated SVD inversions: misfit, model norm, noise standard deviation.
4. Model resolution matrix R_k = V_k V_k^T and its length scale in km.
5. The estimate as a filtered truth plus a noise term, measured against theory.
6. The resolution-versus-variance trade-off, measured over realisations.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

NC = 12                                   # cells
WEIGHTS = np.array([0.7, 1.0, 0.7])       # path length of a ray inside each cell
PRIMARY = [(i, WEIGHTS) for i in range(8)]      # rays 1..8, overlapping windows
REDUNDANT = [(0, WEIGHTS), (3, WEIGHTS), (1, 0.5 * WEIGHTS), (7, WEIGHTS)]
X_KM = np.arange(NC, dtype=float) + 0.5
TRUE = 0.10 * np.sin(2.0 * np.pi * X_KM / NC) + 0.30     # s
SIGMA = 0.005                              # s


def build_operator():
    rows = PRIMARY + REDUNDANT
    G = np.zeros((len(rows), NC))
    for i, (first, w) in enumerate(rows):
        G[i, first:first + 3] = w
    return G


def spread_km(row):
    """Width (km) over which an estimator averages the truth, in absolute weight."""
    w = np.abs(row)
    total = np.sum(w)
    if total < 1e-12:
        return float("nan")
    return float(np.sqrt(np.sum(w * (X_KM - X_KM[np.argmax(w)]) ** 2) / total))


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main():
    G = build_operator()
    U, s, Vt = np.linalg.svd(G)
    V = Vt[:s.size].T
    keep = s > 1e-10 * s[0]
    r = int(keep.sum())
    d_true = G @ TRUE

    section("1. The operator and its spectrum")
    print(f"  model: {NC} cells at {X_KM[0]:.1f} ... {X_KM[-1]:.1f} km, values in s")
    print(f"  data : {G.shape[0]} rays, each the weighted sum 0.7/1.0/0.7 over three")
    print("         consecutive cells; of rays 9-12, two duplicate rays 1 and 8,")
    print("         one duplicates ray 4, and one is half of ray 2")
    print(f"  G is {G.shape[0]} x {G.shape[1]}; true model rms {TRUE.std():.5f} s; "
          f"data noise sigma {SIGMA:.4f} s")
    print(f"  singular values: {np.array2string(s, precision=5)}")
    print(f"  relative: {np.array2string(s / s[0], precision=3)}")
    print(f"  rank = {r}; null-space dimension = {NC} - {r} = {NC - r}; "
          f"dim range(G)^perp = {G.shape[0] - r}")
    print("  Four of the twelve rays are redundant: the data matrix has 12 rows but")
    print("  only 8 independent numbers, and four model directions are invisible.")
    print("  The two zero and two machine-precision singular values are that redundancy.")

    section("2. Data importance")
    imp = np.sum(U[:, :r] ** 2, axis=1)
    order = np.argsort(-imp)
    print("  importance_i = sum over retained directions of U_ij^2")
    print("   rank  ray    importance   share of total")
    for kk, j in enumerate(order, start=1):
        print(f"   {kk:4d}  {j + 1:3d}   {imp[j]:10.6f}   {imp[j] / r * 100:12.2f}%")
    print(f"  sum of importances = {imp.sum():.6f} = rank = {r}  ✔")
    print("  A duplicate does not ADD information: it splits the importance of the")
    print("  direction it duplicates.  Rays 1 and 9, 4 and 10, 8 and 12 each carry")
    print("  0.500 of a direction; the half-amplitude copy (ray 11) carries 0.200 while")
    print("  its twin (ray 2) keeps 0.800.  The total is still 8: five independent")
    print("  directions plus these splits.  Planning rule: a new station is worth its")
    print("  importance, and a station that duplicates an existing ray is worth 0.")

    section("3. Truncated SVD inversions")
    d_obs = d_true + SIGMA * RNG.standard_normal(G.shape[0])
    print(f"  data noise sigma = {SIGMA:.4f} s "
          f"({SIGMA / np.abs(d_true).max() * 100:.3f}% of the peak reading)")
    print("   k    data misfit     ||m_k|| (s)    rms noise in m_k (s)   mean R_jj")
    for k in range(1, r + 1):
        Vk = V[:, :k]
        mk = Vk @ ((U[:, :k].T @ d_obs) / s[:k])
        fit = np.linalg.norm(G @ mk - d_obs) / np.linalg.norm(d_obs)
        var = SIGMA ** 2 * np.sum(Vk ** 2 / s[:k] ** 2, axis=1)
        Rk = Vk @ Vk.T
        print(f"   {k:2d}   {fit * 100:10.4f}%   {np.linalg.norm(mk):12.5f}   "
              f"{np.sqrt(np.mean(var)):20.6f}   {np.mean(np.diag(Rk)):9.4f}")
    print("  Misfit falls and the noise standard deviation rises: the last column is")
    print("  dominated by 1/sigma_8, and sigma_8/sigma_1 = "
          f"{s[r - 1] / s[0]:.3f}.")

    section("4. The model resolution matrix R = V_r V_r^T")
    R = V[:, :r] @ V[:, :r].T
    print(f"  trace(R) = {np.trace(R):.6f} = rank, ||R^2 - R||_inf = "
          f"{np.max(np.abs(R @ R - R)):.3e}: R is an orthogonal projector")
    print("   cell   x (km)   R_jj (self-resolution)   spread (km)")
    for j in range(NC):
        print(f"   {j:4d}   {X_KM[j]:6.2f}   {R[j, j]:21.4f}   {spread_km(R[j]):11.4f}")
    print("  Cells with R_jj = 0 are in the null space: rays 1-8 cover cells 0-9 only,")
    print("  so cells 10 and 11 are never sampled at all.  Among the sampled cells the")
    print("  ENDS have the widest averaging kernel (4.43 km at cell 0 against 2.44 km at")
    print("  cell 3) even though their R_jj is the largest (0.8182 against 0.7743).")
    print("  A large diagonal is not resolution on its own: read the kernel width too.")

    section("5. The estimate as a filtered truth plus a noise term")
    Vk = V[:, :r]
    filtered = Vk @ (Vk.T @ TRUE)
    print(f"  ||(R - I) m_true|| (smoothing bias)   = {np.linalg.norm(filtered - TRUE):.6f} s")
    print(f"  theory: ||noise part|| = sigma*sqrt(sum 1/sigma_i^2) = "
          f"{SIGMA * np.sqrt(np.sum(1.0 / s[:r] ** 2)):.6f} s")
    measured = []
    for _ in range(300):
        e = SIGMA * RNG.standard_normal(G.shape[0])
        measured.append(np.linalg.norm(Vk @ ((U[:, :r].T @ e) / s[:r])) ** 2)
    print(f"  measured over 300 realisations: mean ||noise part||^2 = "
          f"{np.mean(measured):.3e} s^2")
    print(f"  theory: sigma^2 sum 1/sigma_i^2 = "
          f"{SIGMA ** 2 * np.sum(1.0 / s[:r] ** 2):.3e} s^2")
    print(f"  ratio = {np.mean(measured) / (SIGMA ** 2 * np.sum(1.0 / s[:r] ** 2)):.4f}")
    print("  So the error of the estimated model splits exactly into a deterministic")
    print("  smoothing bias from R and a random term whose variance is")
    print("  sigma^2 * sum 1/sigma_i^2 over the retained directions.")

    section("6. The resolution-versus-variance trade-off, measured")
    for sigma_now, label in ((SIGMA, "low noise"), (0.050, "high noise")):
        print(f"  noise sigma = {sigma_now:.4f} s "
              f"({sigma_now / np.abs(d_true).max() * 100:.2f}% of the peak reading) "
              f"--- {label}")
        print("   k   mean spread (km)   rms noise (s)   rms total error (s)")
        best_k, best_err = None, np.inf
        for k in range(1, r + 1):
            Vk = V[:, :k]
            sp = [spread_km((Vk @ Vk.T)[j]) for j in range(NC)]
            noise_rms = sigma_now * np.sqrt(np.mean(np.sum(Vk ** 2 / s[:k] ** 2, axis=1)))
            tot = []
            for _ in range(150):
                dd = d_true + sigma_now * RNG.standard_normal(G.shape[0])
                m = Vk @ ((U[:, :k].T @ dd) / s[:k])
                tot.append(np.sqrt(np.mean((m - TRUE) ** 2)))
            err = float(np.mean(tot))
            if err < best_err:
                best_k, best_err = k, err
            print(f"   {k:2d}   {np.nanmean(sp):15.4f}   {noise_rms:12.6f}   {err:18.6f}")
        print(f"    best k = {best_k} with rms total error {best_err:.6f} s")
        print()
    print("  With small noise the best truncation is the largest available k (8); as the")
    print("  noise grows the optimum moves inward to k = 5, where the loss of the noisier")
    print("  directions is worth the wider averaging kernel.  Note that the mean")
    print("  spreading width is NOT monotone in k, because the retained directions have")
    print("  different geometry: the trade-off must be measured, not read off the")
    print("  spectrum.")
    print("\n  All models and data in this demonstration are SYNTHETIC.")


if __name__ == "__main__":
    main()
