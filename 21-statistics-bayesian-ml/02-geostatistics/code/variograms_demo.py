#!/usr/bin/env python3
"""Variograms on SYNTHETIC data: the experimental semivariogram, weighted
least-squares fitting of the spherical, exponential and Gaussian models, and
the effect of outliers on the classical and robust estimators.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python variograms_demo.py

Everything is SYNTHETIC: the field is generated from a stated exponential
covariance plus a stated nugget. No measured value is used.

Sections
--------
1. The experimental semivariogram.
2. Fitting three models by weighted least squares.
3. Classical versus robust semivariance when outliers are present.
"""

import numpy as np
from scipy.optimize import least_squares

RNG = np.random.default_rng(20261014)

N = 600            # samples along a line
DX = 1.0           # spacing, m
SILL = 1.0         # structured variance
NUGGET = 0.2       # nugget variance
ARANGE = 15.0      # exponential effective range (gamma = C0 + C(1-exp(-3h/a)))
MAXLAG = 60
N_OUT = 8          # outliers added in section 3
OUTLIER = 6.0
PHI = float(np.exp(-3.0 * DX / ARANGE))


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def exp_ar1(n, phi, rng):
    w = np.sqrt(1.0 - phi ** 2) * rng.standard_normal(n)
    x = np.empty(n)
    x[0] = rng.standard_normal()
    for i in range(1, n):
        x[i] = phi * x[i - 1] + w[i]
    return x


def experimental_variogram(z, maxlag, robust=False):
    lags, gam, cnt = [], [], []
    for h in range(1, maxlag + 1):
        d = z[:-h] - z[h:]
        if robust:
            m = np.mean(np.abs(d) ** 0.5)
            g = 0.5 * m ** 4 / (0.457 + 0.494 / d.size)
        else:
            g = 0.5 * np.mean(d ** 2)
        lags.append(h * DX)
        gam.append(g)
        cnt.append(d.size)
    return np.array(lags), np.array(gam), np.array(cnt)


def spherical(h, p):
    c0, c, a = p
    r = np.minimum(h / a, 1.0)
    return c0 + c * (1.5 * r - 0.5 * r ** 3)


def exponential(h, p):
    c0, c, a = p
    return c0 + c * (1.0 - np.exp(-3.0 * h / a))


def gaussian(h, p):
    c0, c, a = p
    return c0 + c * (1.0 - np.exp(-3.0 * (h / a) ** 2))


MODELS = (("spherical", spherical), ("exponential", exponential),
          ("gaussian", gaussian))


def fit_model(model, h, g, n):
    weights = n / g ** 2

    def resid(p):
        return np.sqrt(weights) * (model(h, p) - g)

    res = least_squares(resid, x0=[0.1, 1.0, 10.0],
                        bounds=([0.0, 0.0, 0.1], [np.inf, np.inf, 500.0]))
    sse = float(np.sum(weights * (model(h, res.x) - g) ** 2))
    return res.x, sse


def main():
    print(f"SYNTHETIC field: exponential covariance with sill {SILL:.1f}, "
          f"nugget {NUGGET:.1f}, range {ARANGE:.0f} m; {N} samples every "
          f"{DX:.0f} m.")

    sig = np.sqrt(SILL) * exp_ar1(N, PHI, RNG)
    z = sig + np.sqrt(NUGGET) * RNG.standard_normal(N)

    section("1. The experimental semivariogram")
    lags, gamma, counts = experimental_variogram(z, MAXLAG)
    print("  lag (m)   gamma_hat   pairs   model truth")
    for h in (1, 2, 5, 10, 15, 20, 30, 45, 60):
        i = int(h / DX) - 1
        truth = NUGGET + SILL * (1.0 - PHI ** h)
        print(f"  {lags[i]:7.1f}   {gamma[i]:9.4f}   {counts[i]:5d}   "
              f"{truth:11.4f}")
    print(f"  the observed sill (mean gamma at the largest lags) = "
          f"{gamma[-10:].mean():.4f} against the model sill + nugget = "
          f"{SILL + NUGGET:.4f}")
    print("  the gap is finite-sample scatter: with a correlation length of one")
    print(f"  fifth of the record the effective sample size is about {N / 20:.0f},")
    print("  and the sample variance of such a series has a large spread.")

    section("2. Fitting three models by weighted least squares")
    print("  model        nugget C0   sill C   range a (m)   weighted SSE")
    best = None
    for name, model in MODELS:
        p, sse = fit_model(model, lags, gamma, counts)
        print(f"  {name:11s}  {p[0]:9.4f}  {p[1]:8.4f}  {p[2]:12.2f}   "
              f"{sse:12.4f}")
        if best is None or sse < best[1]:
            best = (name, sse)
    print(f"  best model by weighted SSE: {best[0]} (SSE {best[1]:.4f})")
    print(f"  the true parameters are nugget {NUGGET:.2f}, sill {SILL:.2f}, "
          f"range {ARANGE:.0f} m (approached differently by each model form).")

    section("3. Classical versus robust semivariance with outliers")
    z_out = z.copy()
    idx_out = np.arange(0, N, N // N_OUT)[:N_OUT]
    z_out[idx_out] += OUTLIER
    lags_c, gam_c, cnt_c = experimental_variogram(z_out, MAXLAG, robust=False)
    _, gam_r, _ = experimental_variogram(z_out, MAXLAG, robust=True)
    _, gam_clean, _ = experimental_variogram(z, MAXLAG, robust=False)
    p_clean, _ = fit_model(exponential, lags_c, gam_clean, cnt_c)
    p_c, _ = fit_model(exponential, lags_c, gam_c, cnt_c)
    p_r, _ = fit_model(exponential, lags_c, gam_r, cnt_c)
    print("  fit (exponential)   nugget C0   sill C   range a (m)")
    print(f"  clean data          {p_clean[0]:9.4f}  {p_clean[1]:8.4f}  "
          f"{p_clean[2]:12.2f}")
    print(f"  classical, outliers {p_c[0]:9.4f}  {p_c[1]:8.4f}  "
          f"{p_c[2]:12.2f}")
    print(f"  Cressie-Hawkins     {p_r[0]:9.4f}  {p_r[1]:8.4f}  "
          f"{p_r[2]:12.2f}")
    print(f"  sill change under outliers: classical {(p_c[1] / p_clean[1] - 1) * 100:+.1f} %, "
          f"robust {(p_r[1] / p_clean[1] - 1) * 100:+.1f} %")
    print(f"  nugget change: classical {(p_c[0] / p_clean[0] - 1) * 100:+.1f} %, "
          f"robust {(p_r[0] / p_clean[0] - 1) * 100:+.1f} %")
    print("  the eight large values inflate the classical semivariance at every")
    print("  lag; the Cressie-Hawkins estimator discounts them.")


if __name__ == "__main__":
    main()
