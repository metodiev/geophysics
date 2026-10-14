#!/usr/bin/env python3
"""Bayes' theorem as an inverse-problem formulation: prior x likelihood -> posterior.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python bayes_inverse_formulation_demo.py

All models and data in this demo are SYNTHETIC.  The forward operator, the
parameter values and the noise level are chosen teaching values, not measurements.

Contents
--------
1. A SYNTHETIC linear-Gaussian inverse problem and its exact posterior.
2. The posterior as a normalised map over model space (grid check of the analytics).
3. MAP = posterior mean for a Gaussian posterior; residual norms at both.
4. Equivalence of the Bayesian MAP to Tikhonov regularisation, with lambda shown.
5. Degenerate (nearly singular) design: the prior is what makes the problem solvable.
"""

import numpy as np
import scipy.linalg as sla
from scipy.optimize import minimize
from scipy.stats import multivariate_normal

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC problem: d = G m + e, two parameters, three data ---------------
G = np.array([[1.0, 0.0],
              [0.0, 1.0],
              [1.0, 1.0]])          # data = [m1, m2, m1 + m2], dimensionless units
SIGMA_D = 0.5                    # data standard deviation, same units as d
M_TRUE = np.array([2.0, -1.0])   # synthetic true model
M0 = np.array([0.0, 0.0])        # prior mean
S0 = 2.0                         # prior standard deviation (isotropic), same units
CI = np.diag([S0 ** 2, S0 ** 2])  # prior covariance


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def gaussian_posterior(G, d, Cd, m0, Ci):
    """Exact posterior of a linear-Gaussian inverse problem.

    Prior  m ~ N(m0, Ci);  likelihood  d | m ~ N(G m, Cd).  Returns (mean, cov).
    """
    Ci_inv = sla.inv(Ci)
    Cd_inv = sla.inv(Cd)
    Cpost = sla.inv(G.T @ Cd_inv @ G + Ci_inv)
    mpost = Cpost @ (G.T @ Cd_inv @ d + Ci_inv @ m0)
    return mpost, Cpost


def main():
    d = G @ M_TRUE + SIGMA_D * RNG.standard_normal(G.shape[0])
    Cd = SIGMA_D ** 2 * np.eye(G.shape[0])

    section("1. SYNTHETIC problem and its exact posterior")
    print(f"forward operator G (rows = model, columns = data):")
    for row in G:
        print("   ", row)
    print(f"true model (synthetic) m_true = {M_TRUE}  (dimensionless)")
    print(f"data standard deviation sigma_d = {SIGMA_D:.3f} (same units as d)")
    print(f"data d = {np.array2string(d, precision=4)}")

    mpost, Cpost = gaussian_posterior(G, d, Cd, M0, CI)
    sd = np.sqrt(np.diag(Cpost))
    corr = Cpost[0, 1] / (sd[0] * sd[1])
    print(f"\nprior          : mean {M0}, std {S0:.2f} (isotropic)")
    print(f"posterior mean : {np.array2string(mpost, precision=4)}")
    print(f"posterior std  : {np.array2string(sd, precision=4)}")
    print(f"posterior corr : {corr:+.4f}")
    print(f"truth errors   : {np.array2string(mpost - M_TRUE, precision=4)}  "
          f"(in units of posterior std: "
          f"{np.array2string((mpost - M_TRUE) / sd, precision=2)})")

    section("2. The posterior as a normalised map: grid check of the analytic result")
    # Vectorised evaluation of
    #   p(m|d) propto exp[-1/2 ||d-Gm||^2/sigma_d^2 - 1/2 (m-m0)' Ci^-1 (m-m0)]
    lo, hi, n = -4.0, 7.0, 401
    ax = np.linspace(lo, hi, n)
    M1, M2 = np.meshgrid(ax, ax, indexing="ij")
    dm = ax[1] - ax[0]
    resid = (d[0] - M1) ** 2 + (d[1] - M2) ** 2 + (d[2] - M1 - M2) ** 2
    logp = -0.5 * resid / SIGMA_D ** 2 - 0.5 * (M1 ** 2 + M2 ** 2) / S0 ** 2
    logp -= logp.max()
    p = np.exp(logp)
    p /= (p.sum() * dm * dm)
    grid_mean = np.array([(M1 * p).sum() * dm * dm, (M2 * p).sum() * dm * dm])
    var1 = ((M1 - grid_mean[0]) ** 2 * p).sum() * dm * dm
    var2 = ((M2 - grid_mean[1]) ** 2 * p).sum() * dm * dm
    cov12 = ((M1 - grid_mean[0]) * (M2 - grid_mean[1]) * p).sum() * dm * dm
    imax = np.unravel_index(np.argmax(p), p.shape)
    print(f"grid {n}x{n} over [{lo:g},{hi:g}]^2, spacing {dm:.4f}")
    print(f"grid  mean      : {np.array2string(grid_mean, precision=4)}")
    print(f"analytic mean   : {np.array2string(mpost, precision=4)}")
    print(f"grid  std       : [{np.sqrt(var1):.4f}, {np.sqrt(var2):.4f}]")
    print(f"analytic std    : [{sd[0]:.4f}, {sd[1]:.4f}]")
    print(f"grid  correlation: {cov12 / np.sqrt(var1 * var2):+.4f}")
    print(f"grid  argmax (MAP): ({ax[imax[0]]:.4f}, {ax[imax[1]]:.4f})")
    print("The mode of a multivariate Gaussian is its mean: the row above should")
    print("coincide with the posterior mean to within the grid spacing.")

    section("3. Is the posterior mean the best data fit? (no: it is a compromise)")
    J = lambda m: 0.5 * np.sum((d - G @ m) ** 2) / SIGMA_D ** 2 \
        + 0.5 * (m - M0) @ sla.inv(CI) @ (m - M0)
    res_mean = np.linalg.norm(d - G @ mpost)
    res_mle = np.linalg.norm(d - G @ np.linalg.lstsq(G, d, rcond=None)[0])
    print(f"data misfit ||d - G m|| at the posterior mean : {res_mean:.4f}")
    print(f"data misfit ||d - G m|| at the least-squares fit: {res_mle:.4f}")
    print(f"objective J(m) at the posterior mean          : {J(mpost):.6f}")
    opt = minimize(J, x0=[0.0, 0.0], method="Nelder-Mead",
                   options={"xatol": 1e-10, "fatol": 1e-12})
    print(f"objective J(m) at the numeric minimiser       : {opt.fun:.6f}")
    print(f"numeric minimiser                             : "
          f"{np.array2string(opt.x, precision=4)}")
    print("Maximising the posterior (minimising J) and averaging under the")
    print("posterior are the same point here only because the posterior is Gaussian.")

    section("4. Bayes' rule is Tikhonov regularisation with a named lambda")
    lam2 = SIGMA_D ** 2 / S0 ** 2
    print(f"with Ci = S0^2 I and Cd = sigma_d^2 I, the exponent of the posterior is")
    print(f"    -(1/2 sigma_d^2) [ ||d - G m||^2 + lambda^2 ||m - m0||^2 ]")
    print(f"    lambda^2 = sigma_d^2 / S0^2 = {SIGMA_D ** 2:.4f} / {S0 ** 2:.4f} "
          f"= {lam2:.6f}")
    print(f"    lambda   = sigma_d / S0      = {SIGMA_D / S0:.6f}")
    for lam in (0.05, 0.25, 1.0, 4.0):
        dmp = sla.inv(G.T @ G + lam ** 2 * np.eye(2)) @ (G.T @ d
                                                        + lam ** 2 * M0)
        print(f"    lambda = {lam:5.2f} -> damped solution "
              f"{np.array2string(dmp, precision=4)}")
    print("A small lambda (weak prior) walks toward the least-squares solution and")
    print("inflates the variance; a large lambda (strong prior) shrinks toward m0.")

    section("5. A rank-deficient design: the prior is what makes the problem solvable")
    G_bad = np.array([[1.0, 1.0],
                      [2.0, 2.0],
                      [3.0, 3.0]])   # columns are parallel: rank 1, null space exists
    d_bad = G_bad @ M_TRUE + SIGMA_D * RNG.standard_normal(3)
    sv = np.linalg.svd(G_bad, compute_uv=False)
    print(f"singular values of the rank-deficient G: {np.array2string(sv, precision=4)}")
    print(f"null-space direction (G v = 0): v = {np.array2string(
        np.array([1.0, -1.0]) / np.sqrt(2.0), precision=4)}")
    mpost_bad, Cpost_bad = gaussian_posterior(G_bad, d_bad, Cd, M0, CI)
    print(f"posterior mean (rank-deficient G): "
          f"{np.array2string(mpost_bad, precision=4)}")
    print(f"posterior std  (rank-deficient G): "
          f"{np.array2string(np.sqrt(np.diag(Cpost_bad)), precision=4)}")
    v = np.array([1.0, -1.0]) / np.sqrt(2.0)
    print(f"posterior std along the null-space direction: "
          f"{np.sqrt(v @ Cpost_bad @ v):.4f}")
    print(f"prior std along the same direction          : {S0:.4f}")
    print("The likelihood says nothing along v, so the posterior there IS the prior:")
    print("the data set that direction to be undetermined, not to be zero.")


if __name__ == "__main__":
    main()
