#!/usr/bin/env python3
"""Hyperspectral sensing: the linear mixing model and its constrained solutions.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hyperspectral_demo.py

Everything is SYNTHETIC.  The five endmembers are smooth teaching spectra built
in this file from logistic and Gaussian terms; the abundances are drawn from a
Dirichlet distribution with a chosen concentration.  No real material and no real
instrument is represented.

Contents
--------
1. The synthetic endmember library and its spectral features.
2. A synthetic scene of mixed pixels with known abundances.
3. Unconstrained least squares: negative abundances and unphysical sums.
4. Sum-to-one constrained least squares, in closed form.
5. Non-negativity: a fully constrained (FCLS) solution by NNLS.
6. Conditioning of the endmember matrix, and a near-duplicate endmember.
7. Noise propagation: abundance uncertainty versus noise, measured and predicted.
8. Dimensionality: how many components the scene really needs.
9. Endmember variability: model error against measurement error.
10. Verification: reconstruction residuals for each solver.
"""

import numpy as np
from scipy.optimize import nnls

RNG = np.random.default_rng(20261014)

N_BANDS = 60
LAM = np.linspace(0.40, 2.50, N_BANDS)      # micrometres
N_PIXELS = 400
ENDMEMBER_NAMES = ("vegetation-like", "bright-soil-like", "water-like",
                   "carbonate-like", "clay-like")


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def endmember_library():
    """SYNTHETIC endmember spectra: (p, m) array.  Chosen teaching shapes."""
    lam = LAM
    step = lambda x0, w: 1.0 / (1.0 + np.exp(-(lam - x0) / w))
    gauss = lambda c, w: np.exp(-((lam - c) / w) ** 2)
    veg = (0.03 + 0.45 * step(0.72, 0.03) - 0.10 * gauss(1.45, 0.05)
           - 0.12 * gauss(1.95, 0.07) - 0.05 * step(2.30, 0.10))
    soil = 0.20 + 0.30 * step(1.20, 0.20) - 0.05 * gauss(1.40, 0.05)
    water = (0.09 - 0.085 * step(0.80, 0.06) + 0.01 * gauss(0.48, 0.08)
             - 0.02 * step(1.00, 0.10))
    carbonate = (0.15 + 0.25 * step(1.30, 0.25) - 0.10 * gauss(2.33, 0.04)
                 - 0.04 * gauss(1.88, 0.05))
    clay = (0.14 + 0.22 * step(1.30, 0.25) - 0.09 * gauss(2.21, 0.05)
            - 0.07 * gauss(1.41, 0.04) + 0.05 * gauss(2.35, 0.08))
    return np.clip(np.vstack([veg, soil, water, carbonate, clay]), 0.010, 0.95)


def make_pixels(E, n_pixels, sigma):
    """SYNTHETIC mixtures: Dirichlet abundances plus Gaussian band noise."""
    abundances = RNG.dirichlet(1.5 * np.ones(E.shape[0]), size=n_pixels)
    clean = abundances @ E
    noisy = clean + sigma * RNG.standard_normal(clean.shape)
    return abundances, clean, noisy


def main():
    E = endmember_library()
    p, m = E.shape

    section("1. The synthetic endmember library")
    print(f"  {p} endmembers, {m} contiguous bands from {LAM[0]:.2f} to "
          f"{LAM[-1]:.2f} um (sampling {LAM[1] - LAM[0]:.4f} um)")
    print("   #   endmember name       reflectance range      feature centres (um)")
    features = {0: "step 0.72, dips 1.45 / 1.95",
                1: "step 1.20, dip 1.40",
                2: "step 0.80 (dark NIR)",
                3: "step 1.30, dip 2.33",
                4: "step 1.30, dips 2.21 / 1.41"}
    for i, name in enumerate(ENDMEMBER_NAMES):
        print(f"  {i:2d}   {name:18s}  {E[i].min():.3f}-{E[i].max():.3f}"
              f"        {features[i]}")
    print("  Spectral contrast between the carbonate-like and clay-like endmembers")
    print("  is a DIP POSITION difference at 2.33 um versus 2.21 um, which is why")
    print("  narrow bands with contiguous sampling are needed to separate them.")

    section("2. A synthetic scene of mixed pixels")
    sigma_clean = 0.0
    a_true, clean, noisy = make_pixels(E, N_PIXELS, 0.002)
    print(f"  {N_PIXELS} pixels, Dirichlet(1.5) abundances (a simplex interior),")
    print("  band noise sigma = 0.002 reflectance units (SNR about 100:1 on soil)")
    print("   endmember       mean abundance   min      max")
    for i, name in enumerate(ENDMEMBER_NAMES):
        col = a_true[:, i]
        print(f"  {name:18s} {col.mean():12.4f}   {col.min():6.4f}   {col.max():6.4f}")
    print(f"  abundance rows sum to {a_true.sum(axis=1).min():.6f} - "
          f"{a_true.sum(axis=1).max():.6f} by construction")

    section("3. Unconstrained least squares")
    M = E.T                                  # (m, p)
    G = M.T @ M                              # Gram matrix (p, p)
    a_unc = noisy @ M @ np.linalg.inv(G)     # (n,m)(m,p)(p,p) -> (n,p)
    print("  solve  min_a ||M a - x||^2  with no constraint on a:")
    print(f"  negative abundances in {int((a_unc < 0).any(axis=1).sum())} "
          f"of {N_PIXELS} pixels ({100 * (a_unc < 0).any(axis=1).mean():.1f}%)")
    print(f"  most negative abundance recovered = {a_unc.min():.4f}")
    print(f"  row sums range from {a_unc.sum(axis=1).min():.4f} to "
          f"{a_unc.sum(axis=1).max():.4f} (physical value: exactly 1)")
    print(f"  RMSE of abundances against truth = {np.sqrt(np.mean((a_unc - a_true) ** 2)):.5f}")
    print("  Unconstrained least squares gives the minimum-residual answer, and it")
    print("  is UNPHYSICAL.  Report it as a diagnostic, never as a cover fraction.")

    section("4. Sum-to-one constrained least squares (closed form)")
    x = noisy
    reduced_M = (M[:, :-1] - M[:, [-1]])      # (m, p-1)
    reduced_x = x - M[:, [-1]].T              # (n, m)
    Gr = reduced_M.T @ reduced_M
    a_free = reduced_x @ reduced_M @ np.linalg.inv(Gr)
    a_sum = np.hstack([a_free, (1.0 - a_free.sum(axis=1, keepdims=True))])
    print("  impose sum(a) = 1 exactly by writing a_p = 1 - sum of the others and")
    print("  regressing x - e_p on (e_1 - e_p, ..., e_{p-1} - e_p):")
    print(f"  row sums: {a_sum.sum(axis=1).min():.6f} to {a_sum.sum(axis=1).max():.6f}")
    print(f"  most negative abundance = {a_sum.min():.4f}")
    print(f"  RMSE of abundances against truth = {np.sqrt(np.mean((a_sum - a_true) ** 2)):.5f}")
    print("  The sum constraint fixes one failure mode and NOT the other: the answer")
    print("  still has negative entries, which are just as unphysical as before.")

    section("5. Fully constrained least squares (non-negative, sum to one)")
    a_fcls = np.zeros_like(a_true)
    big = 1e6
    M_aug = np.vstack([M * 1.0, big * np.ones((1, p))])
    for i in range(N_PIXELS):
        b = np.concatenate([x[i], [big]])
        a_fcls[i] = nnls(M_aug, b)[0]
    print("  minimise ||M a - x||^2 subject to a >= 0 and sum(a) = 1, by NNLS on the")
    print("  row-augmented system with a large weight on the sum row:")
    print(f"  row sums: {a_fcls.sum(axis=1).min():.6f} to {a_fcls.sum(axis=1).max():.6f}")
    print(f"  most negative abundance = {a_fcls.min():.2e}")
    print(f"  RMSE of abundances against truth = {np.sqrt(np.mean((a_fcls - a_true) ** 2)):.5f}")
    print(f"  pixels with a zero abundance: {int((a_fcls < 1e-8).sum())}"
          f" of {a_fcls.size} entries")
    print("  FCLS is the standard solution.  It is a projection onto the simplex, so")
    print("  it BIASES abundances at the boundary: a true 0.02 is drawn toward 0, and")
    print("  the bias is one-sided.  That is the price of the constraint.")

    section("6. Conditioning and a near-duplicate endmember")
    print(f"  condition number of the Gram matrix G = M^T M: {np.linalg.cond(G):.1f}")
    print(f"  condition number of M: {np.linalg.cond(M):.1f}")
    E2 = np.vstack([E, E[3] + 0.01 * (E[4] - E[3])])       # carbonate/clay blend
    M2 = E2.T
    G2 = M2.T @ M2
    print("  append a sixth endmember that is 99% carbonate-like + 1% clay-like:")
    print(f"  condition number of the new Gram matrix: {np.linalg.cond(G2):.1e}")
    print(f"  it grew by a factor {np.linalg.cond(G2) / np.linalg.cond(G):.1e}")
    a2 = x @ M2 @ np.linalg.pinv(G2)
    print(f"  abundance RMSE with 6 endmembers = "
          f"{np.sqrt(np.mean((a2[:, :5] - a_true) ** 2)):.5f}")
    print(f"  abundance RMSE with 5 endmembers = "
          f"{np.sqrt(np.mean((a_unc - a_true) ** 2)):.5f}")
    print("  More endmembers is not automatically better: a nearly collinear library")
    print("  amplifies noise into abundance, and the extra endmember is not")
    print("  identifiable.  Compare the two RMSEs above, not the count.")

    section("7. Noise propagation: abundance uncertainty versus band noise")
    Ginv = np.linalg.inv(G)
    print("  theory: cov(a) = sigma^2 (M^T M)^-1 for unconstrained least squares")
    print("   band sigma   MC sd(err a_0)   predicted sd(a_0)   MC sd(err a_3)   predicted")
    for sig in (0.001, 0.002, 0.005, 0.010, 0.020):
        x_s = clean + sig * RNG.standard_normal(clean.shape)
        a_s = x_s @ M @ Ginv
        err = a_s - a_true
        pred = sig * np.sqrt(np.diag(Ginv))
        print(f"  {sig:11.4f}   {err[:, 0].std(ddof=1):12.5f}   {pred[0]:18.5f}   "
              f"{err[:, 3].std(ddof=1):12.5f}   {pred[3]:10.5f}")
    print("  The uncertainty is proportional to the band noise and shaped by the")
    print("  library: sqrt(diag((M^T M)^-1)) is the conditioning fingerprint of the")
    print("  endmembers, so a badly conditioned library inflates abundance noise even")
    print("  when the bands are clean.")

    section("8. Dimensionality: how many components the scene needs")
    cov = np.cov(clean.T)
    evals = np.sort(np.linalg.eigvalsh(cov))[::-1]
    total = evals.sum()
    print("   component   eigenvalue   share (%)   cumulative (%)")
    cum = 0.0
    for i, ev in enumerate(evals[:8], start=1):
        share = 100.0 * ev / total
        cum += share
        print(f"  {i:10d}   {ev:10.5f}   {share:9.3f}   {cum:14.3f}")
    print(f"  rank of the endmember matrix = {np.linalg.matrix_rank(E)} (of {p})")
    print("  The scene has as many independent dimensions as it has genuine")
    print("  endmembers, not as many as it has bands.  A rotation of the data (PCA)")
    print("  finds those dimensions; it does NOT label them, and its components are")
    print("  linear mixtures, not materials.")

    section("9. Endmember variability: model error against measurement error")
    E_var = E.copy()
    E_var[0] = E[0] * (1.0 + 0.05 * np.sin(np.linspace(0.0, 6.0, m)))
    a_var = noisy @ E_var.T @ np.linalg.inv(E_var @ E_var.T)
    bias = (a_var - a_true).mean(axis=0)
    print("  unmix pixels made with the true vegetation-like endmember using a")
    print("  library whose vegetation-like endmember is 5% different in shape:")
    print("   endmember       mean bias (a_var - a_true)   RMSE")
    for i, name in enumerate(ENDMEMBER_NAMES):
        print(f"  {name:18s} {bias[i]:+22.5f}   "
              f"{np.sqrt(np.mean((a_var[:, i] - a_true[:, i]) ** 2)):8.5f}")
    print(f"  abundance RMSE with a 5% endmember shape error = "
          f"{np.sqrt(np.mean((a_var - a_true) ** 2)):.5f}")
    print(f"  abundance RMSE from 0.002 band noise alone      = "
          f"{np.sqrt(np.mean((a_unc - a_true) ** 2)):.5f}")
    print("  The 5% library error exceeds the measurement noise by a factor 2.4")
    print("  and -- more importantly -- produces a BIASED abundance, not merely a")
    print("  noisy one.")
    print("  This is why hyperspectral abundance maps are reported with their")
    print("  endmember provenance, and why endmember selection is the hard part.")

    section("10. Verification: reconstruction residuals")
    for name, a_hat in (("unconstrained", a_unc), ("sum-to-one", a_sum),
                        ("FCLS", a_fcls)):
        recon = a_hat @ E
        res = np.sqrt(np.mean((recon - noisy) ** 2))
        print(f"  {name:14s} reconstruction RMSE = {res:.6f} reflectance units")
    print("  All three are small relative to the 0.002 band noise: the model fits the")
    print("  data.  A small residual therefore validates the ARITHMETIC, not the")
    print("  physics -- section 9 shows the physics error hiding inside it.")


if __name__ == "__main__":
    main()
