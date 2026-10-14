#!/usr/bin/env python3
"""Geostatistics combined with a geophysical forward model, on SYNTHETIC data:
a linear Bayesian inversion whose prior covariance is a variogram model,
compared with white-noise and mis-specified priors.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geostatistics_inversion_demo.py

Everything is SYNTHETIC. The model is a stated random field, the forward
operator is a stated smoothing kernel, and the noise level is stated. No
measured value is used.

Sections
--------
1. The forward problem and the data.
2. Posterior models under three prior covariances.
3. Resolution, posterior variance and the bias-variance trade.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N = 60                 # model cells
DX = 1.0               # cell size, m
TRUE_RANGE = 10.0      # exponential range of the true field, m
SIGMA_D = 0.05         # data noise standard deviation
KERNEL_LENGTH = 5      # smoothing length of the forward operator, cells


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def exp_cov(n, range_m, var=1.0):
    idx = np.arange(n) * DX
    return var * np.exp(-3.0 * np.abs(idx[:, None] - idx[None, :]) / range_m)


def exp_ar1(n, range_m, rng):
    phi = float(np.exp(-3.0 * DX / range_m))
    w = np.sqrt(1.0 - phi ** 2) * rng.standard_normal(n)
    x = np.empty(n)
    x[0] = rng.standard_normal()
    for i in range(1, n):
        x[i] = phi * x[i - 1] + w[i]
    return x


def main():
    print(f"SYNTHETIC inversion: {N} model cells of {DX:.0f} m, true field with "
          f"exponential range {TRUE_RANGE:.0f} m, forward operator a "
          f"{KERNEL_LENGTH}-cell boxcar, data noise sd {SIGMA_D:.2f}.")

    # --- forward operator: normalised boxcar smoothing ---
    G = np.zeros((N, N))
    for i in range(N):
        lo = max(0, i - KERNEL_LENGTH // 2)
        hi = min(N, i + KERNEL_LENGTH // 2 + 1)
        G[i, lo:hi] = 1.0 / (hi - lo)
    Cd = SIGMA_D ** 2 * np.eye(N)

    truth = exp_ar1(N, TRUE_RANGE, RNG)
    data = G @ truth + SIGMA_D * RNG.standard_normal(N)

    section("1. The forward problem and the data")
    print(f"  model variance (truth)       = {truth.var():.4f}")
    print(f"  data range                   = [{data.min():+.3f}, "
          f"{data.max():+.3f}]")
    print(f"  forward operator smoothing: data variance = {data.var():.4f} "
          f"against model variance {truth.var():.4f}")
    print("  the operator low-pass filters the model, so the data cannot see")
    print("  the short-wavelength part of the model; the prior decides it.")

    section("2. Posterior models under three prior covariances")
    priors = (
        ("white (range -> 0)", 1.0 * np.eye(N)),
        ("true range 10 m", exp_cov(N, 10.0)),
        ("long range 30 m", exp_cov(N, 30.0)),
    )
    print("  prior                RMSE vs truth   mean post. var   E[resolution]")
    results = {}
    for name, Cm in priors:
        A = Cm @ G.T @ np.linalg.inv(G @ Cm @ G.T + Cd)
        m_post = A @ data
        Cpost = Cm - A @ G @ Cm
        rmse = float(np.sqrt(np.mean((m_post - truth) ** 2)))
        R = A @ G
        print(f"  {name:19s}  {rmse:11.4f}   {np.trace(Cpost) / N:13.4f}   "
              f"{np.trace(R) / N:12.4f}")
        results[name] = (m_post, Cpost, rmse, R)

    section("3. Bias, variance and what the prior decides")
    for name, (m_post, Cpost, rmse, _) in results.items():
        bias = float(np.mean(m_post - truth))
        print(f"  {name:19s}  RMSE {rmse:.4f}   bias {bias:+.4f}   "
              f"mean posterior sd {np.sqrt(np.trace(Cpost) / N):.4f}")
    print("  the long-range prior smooths most strongly: it has the smallest")
    print("  posterior variance and the largest bias where the truth has short-")
    print("  wavelength structure.  The prior covariance is the geostatistical")
    print("  assumption of this inversion, and it is visible in the answer.")
    m_ls = np.linalg.lstsq(G, data, rcond=None)[0]
    print(f"  unregularised least-squares solution: RMSE = "
          f"{float(np.sqrt(np.mean((m_ls - truth) ** 2))):.4f}")


if __name__ == "__main__":
    main()
