#!/usr/bin/env python3
"""Overdetermined problems and least squares, measured.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python overdetermined_demo.py

Everything here is SYNTHETIC: a chosen regional trend, chosen station positions
and noise generated in this script.

Contents
--------
1. A two-parameter overdetermined problem: regional trend through gravity data.
2. The normal equations versus the QR/SVD route, with condition numbers.
3. Estimator uncertainty: predicted versus measured over 500 realisations.
4. The residual is orthogonal to the columns of G, and chi-squared behaves.
5. Heteroscedastic noise: what ignoring the weights costs.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC experiment ----------------------------------------------------
X_KM = np.linspace(-20.0, 20.0, 20)
M_TRUE = np.array([12.00, -0.850])          # mGal, and mGal/km
SIGMA_MGAL = 0.050                          # white noise level
N, M = X_KM.size, M_TRUE.size


def design(x_km):
    """G[i, :] = [1, x_i]: a straight line in x, units mGal per model unit."""
    return np.column_stack([np.ones_like(x_km), x_km])


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    G = design(X_KM)
    d_clean = G @ M_TRUE

    section("1. The overdetermined problem")
    print(f"  model:  d(x) = m1 + m2 x   (m1 in mGal, m2 in mGal/km)")
    print(f"  N = {N} stations over x in [{X_KM[0]:.0f}, {X_KM[-1]:.0f}] km, M = {M}")
    print(f"  G is {G.shape}, so N > M: the system is overdetermined")
    print(f"  true model: m1 = {M_TRUE[0]:.3f} mGal, m2 = {M_TRUE[1]:.3f} mGal/km")
    print(f"  white noise sigma = {SIGMA_MGAL:.3f} mGal")
    d_obs = d_clean + SIGMA_MGAL * RNG.standard_normal(N)
    print(f"  data range: {d_obs.min():.4f} to {d_obs.max():.4f} mGal")

    section("2. Two routes to the same estimator")
    GtG = G.T @ G
    Gtd = G.T @ d_obs
    m_normal = np.linalg.solve(GtG, Gtd)
    m_qr, *_ = np.linalg.lstsq(G, d_obs, rcond=None)
    print(f"  normal equations  m = {np.array2string(m_normal, precision=6)}")
    print(f"  lstsq (QR/SVD)    m = {np.array2string(m_qr, precision=6)}")
    print(f"  max difference = {np.max(np.abs(m_normal - m_qr)):.3e} mGal")
    print(f"  residual norm  = {np.linalg.norm(G @ m_qr - d_obs):.6e} mGal")
    s_G = np.linalg.svd(G, compute_uv=False)
    s_GtG = np.linalg.svd(GtG, compute_uv=False)
    print(f"  sigma(G)    = {np.array2string(s_G, precision=4)}")
    print(f"  sigma(G^T G)= {np.array2string(s_GtG, precision=4)}")
    print(f"  kappa(G) = {s_G[0] / s_G[-1]:.6f}, kappa(G^T G) = "
          f"{s_GtG[0] / s_GtG[-1]:.6f}, ratio = "
          f"{(s_GtG[0] / s_GtG[-1]) / (s_G[0] / s_G[-1]) ** 2:.6f}")
    print("  For a well-conditioned overdetermined system the normal equations are")
    print("  merely worse conditioned, not fatal.  Lesson 02-04 shows when it matters.")

    section("3. Estimator uncertainty: predicted versus measured")
    cov_pred = SIGMA_MGAL ** 2 * np.linalg.inv(GtG)
    sd_pred = np.sqrt(np.diag(cov_pred))
    est = np.array([np.linalg.lstsq(G, d_clean + SIGMA_MGAL * RNG.standard_normal(N),
                                    rcond=None)[0] for _ in range(500)])
    print(f"  predicted sd: m1 = {sd_pred[0]:.6f} mGal, m2 = {sd_pred[1]:.6f} mGal/km")
    print(f"  measured  sd: m1 = {est[:, 0].std():.6f} mGal, m2 = {est[:, 1].std():.6f} mGal/km")
    print(f"  measured bias: m1 = {est[:, 0].mean() - M_TRUE[0]:+.2e} mGal, "
          f"m2 = {est[:, 1].mean() - M_TRUE[1]:+.2e} mGal/km")
    print(f"  correlation predicted = {cov_pred[0, 1] / np.sqrt(cov_pred[0, 0] * cov_pred[1, 1]):+.6f}")
    print(f"  correlation measured  = {np.corrcoef(est[:, 0], est[:, 1])[0, 1]:+.6f}")
    print("  Least squares is unbiased here (mean error at the 1e-3 sigma level) and")
    print("  the analytic covariance predicts the measured scatter.")

    section("4. Residual orthogonality and chi-squared")
    r = d_obs - G @ m_qr
    print(f"  G^T r = {np.array2string(G.T @ r, precision=3)} mGal")
    print(f"  max |G^T r| = {np.max(np.abs(G.T @ r)):.3e} mGal "
          f"(orthogonality to the columns)")
    chi2 = np.sum(r ** 2) / SIGMA_MGAL ** 2
    dof = N - M
    print(f"  chi^2 = {chi2:.4f} with {dof} degrees of freedom")
    print(f"  reduced chi^2 = {chi2 / dof:.4f}  (expected 1.0 for the true sigma; this")
    print(f"  single realisation sits {(chi2 / dof - 1) / np.sqrt(2.0 / dof):.2f} "
          f"standard deviations above 1, which is ordinary for {dof} d.o.f.)")
    print(f"  rms residual = {r.std():.6f} mGal versus true sigma "
          f"{SIGMA_MGAL:.6f} mGal")
    red = []
    for _ in range(500):
        dd = d_clean + SIGMA_MGAL * RNG.standard_normal(N)
        mm, *_ = np.linalg.lstsq(G, dd, rcond=None)
        red.append(np.sum((dd - G @ mm) ** 2) / SIGMA_MGAL ** 2 / dof)
    print(f"  over 500 realisations: mean reduced chi^2 = {np.mean(red):.4f} "
          f"(expected 1), sd = {np.std(red):.4f}")
    print(f"  theoretical sd = sqrt(2/{dof}) = {np.sqrt(2.0 / dof):.4f}")
    print("  A reduced chi^2 far above 1 means the noise model is wrong, not that the")
    print("  fit is bad: the misfit floor is set by the data error you believe in.")

    section("5. Heteroscedastic noise: what ignoring weights costs")
    sig_i = 0.010 + 0.090 * (X_KM - X_KM[0]) / (X_KM[-1] - X_KM[0])  # 0.010 .. 0.100
    print(f"  true noise sd varies from {sig_i.min():.4f} to {sig_i.max():.4f} mGal (a factor 10)")
    W = np.diag(1.0 / sig_i ** 2)
    err_unw, err_w = [], []
    for _ in range(1000):
        dd = d_clean + sig_i * RNG.standard_normal(N)
        m_u, *_ = np.linalg.lstsq(G, dd, rcond=None)
        m_w = np.linalg.solve(G.T @ W @ G, G.T @ W @ dd)
        err_unw.append(m_u)
        err_w.append(m_w)
    err_unw, err_w = np.array(err_unw), np.array(err_w)
    print(f"  unweighted m2: sd = {err_unw[:, 1].std():.6f} mGal/km")
    print(f"  weighted   m2: sd = {err_w[:, 1].std():.6f} mGal/km")
    print(f"  variance ratio (unweighted/weighted) = "
          f"{(err_unw[:, 1].std() / err_w[:, 1].std()) ** 2:.4f}")
    cov_w = np.linalg.inv(G.T @ W @ G)
    print(f"  predicted weighted sd of m2 = {np.sqrt(cov_w[1, 1]):.6f} mGal/km "
          f"(measured {err_w[:, 1].std():.6f})")
    sig_assumed = float(np.sqrt(np.mean(sig_i ** 2)))
    print(f"  if you ASSUMED a constant sigma = {sig_assumed:.4f} mGal (the rms of the")
    print("  true values):")
    c_u = sig_assumed ** 2 * np.linalg.inv(G.T @ G)
    print(f"    predicted {np.sqrt(c_u[1, 1]):.6f} against measured "
          f"{err_unw[:, 1].std():.6f} mGal/km -> a factor "
          f"{err_unw[:, 1].std() / np.sqrt(c_u[1, 1]):.3f} understatement")
    print(f"  the unweighted estimate is a factor "
          f"{err_unw[:, 1].std() / err_w[:, 1].std():.3f} noisier than the weighted one")
    print("  (variance ratio 2.39).  Note what is NOT damaged: because the station")
    print("  design is symmetric, assuming a constant sigma still predicts a")
    print("  defensible-looking standard deviation (only 3.4% optimistic).  The loss")
    print("  shows up in the efficiency of the estimate, and with clustered stations")
    print("  and a strongly varying sigma it also corrupts the quoted uncertainty")
    print("  (lesson 18-02-06).  Ignoring a known variance structure is never neutral.")
    print("\n  All models and data in this demonstration are SYNTHETIC.")


if __name__ == "__main__":
    main()
