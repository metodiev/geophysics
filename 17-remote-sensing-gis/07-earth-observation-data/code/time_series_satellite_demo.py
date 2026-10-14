#!/usr/bin/env python3
"""Satellite time series and trend analysis: fitting a trend to a synthetic
index, the cost of autocorrelation, aliasing under sparse sampling, and a step
change that a single trend cannot see.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python time_series_satellite_demo.py

Everything here is SYNTHETIC.  The series, its seasonality, noise, revisit
interval and break are chosen teaching values, not measurements.  No file is
read or written and no network access is used.

Contents
--------
1. A daily truth, and a satellite that samples it every 16 days.
2. A trend estimate with a seasonal model and its naive standard error.
3. Autocorrelated residuals: the effective sample size and a corrected error.
4. Aliasing: sparse, uneven sampling invents a trend that is not there.
5. A step change missed by a single-trend model.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def design(t_days):
    """Design matrix: [1, t_years, sin(2 pi t / T), cos(2 pi t / T)]."""
    t_years = t_days / 365.25
    w = 2.0 * np.pi * t_days / 365.25
    return np.column_stack([np.ones_like(t_days), t_years, np.sin(w), np.cos(w)])


def ols(X, y):
    """Least squares; returns coefficients, residual variance, covariance."""
    beta, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    dof = X.shape[0] - X.shape[1]
    s2 = float(resid @ resid) / dof
    cov = s2 * np.linalg.inv(X.T @ X)
    return beta, s2, cov, resid


def main():
    section("1. A daily truth and a 16-day satellite (SYNTHETIC)")
    t_daily = np.arange(0.0, 5.0 * 365.25, 1.0)
    trend_true = 0.020            # per year, dimensionless index
    amp = 0.080                   # seasonal amplitude
    truth = (0.30 + trend_true * (t_daily / 365.25)
             + amp * np.sin(2 * np.pi * t_daily / 365.25)).copy()
    revisit = 16.0
    t_obs = np.arange(0.0, t_daily[-1], revisit)
    # noise is not white: persistent atmospheric and surface conditions make
    # consecutive observations correlated (an AR(1) process, rho = 0.55)
    ar_rho, sigma = 0.55, 0.030
    eps = RNG.normal(0.0, sigma, t_obs.size)
    noise = np.empty_like(eps)
    noise[0] = eps[0]
    for i in range(1, eps.size):
        noise[i] = ar_rho * noise[i - 1] + np.sqrt(1.0 - ar_rho ** 2) * eps[i]
    obs = (0.30 + trend_true * (t_obs / 365.25)
           + amp * np.sin(2 * np.pi * t_obs / 365.25)
           + noise)
    print(f"true trend = {trend_true * 100:.1f} index units per decade "
          f"({trend_true:.3f} per year)")
    print(f"seasonal amplitude = {amp:.3f}, noise sd = {sigma:.3f}")
    print(f"noise is AR(1) with lag-1 correlation {ar_rho:.2f}")
    print(f"observations = {t_obs.size} over {t_daily[-1] / 365.25:.1f} years "
          f"(revisit {revisit:.0f} d)")

    section("2. Trend with a seasonal model, and its naive standard error")
    X = design(t_obs)
    beta, s2, cov, resid = ols(X, obs)
    slope = beta[1]                       # per year
    se_naive = np.sqrt(cov[1, 1])
    print(f"fitted slope = {slope:.4f} index units per year "
          f"({slope * 10:.4f} per decade)")
    print(f"residual sd  = {np.sqrt(s2):.4f}")
    print(f"naive standard error of the slope = {se_naive:.4f} per year")
    print(f"naive 95% interval = [{slope - 1.96 * se_naive:.4f}, "
          f"{slope + 1.96 * se_naive:.4f}] per year")
    print(f"true trend = {trend_true:.4f} per year; "
          f"the truth is inside the interval: "
          f"{slope - 1.96 * se_naive <= trend_true <= slope + 1.96 * se_naive}")

    section("3. Autocorrelated residuals inflate significance (SYNTHETIC)")
    r1 = float(np.corrcoef(resid[:-1], resid[1:])[0, 1])
    n = t_obs.size
    n_eff = n * (1.0 - r1) / (1.0 + r1)
    inflate = np.sqrt((1.0 + r1) / (1.0 - r1))
    se_corr = se_naive * inflate
    print(f"lag-1 autocorrelation of residuals, rho = {r1:.4f}")
    print(f"nominal n = {n}, effective n = n(1-rho)/(1+rho) = {n_eff:.1f}")
    print(f"standard-error inflation = sqrt((1+rho)/(1-rho)) = {inflate:.3f}")
    print(f"corrected 95% interval = [{slope - 1.96 * se_corr:.4f}, "
          f"{slope + 1.96 * se_corr:.4f}] per year")
    print("Treating autocorrelated residuals as independent overstates the")
    print("significance. The correct question is how many independent looks")
    print("the series really contains, not how many spectra were downloaded.")

    section("4. Aliasing: sparse, uneven sampling invents a trend (SYNTHETIC)")
    # A pure annual cycle, sampled once a year with a drifting offset
    t_sparse = np.array([0.0, 400.0, 800.0, 1200.0, 1600.0])   # not 365.25 apart
    y_sparse = 0.10 * np.sin(2 * np.pi * t_sparse / 365.25)
    Xs = np.column_stack([np.ones_like(t_sparse), t_sparse / 365.25])
    bs, _, _, _ = ols(Xs, y_sparse)
    print(f"true signal = a pure annual sinusoid, amplitude 0.100, no trend")
    print(f"sample day indices = {t_sparse.astype(int)}")
    print(f"fitted slope on these 5 samples = {bs[1]:+.4f} index units per year")
    print("The samples beat against the seasonal cycle and a spurious trend")
    print("appears. Revisit interval and sampling phase are part of the answer.")

    section("5. A step change that one trend cannot see (SYNTHETIC)")
    step = np.where(t_obs >= 3.0 * 365.25, 0.060, 0.0)
    y_step = obs + step
    b2, s2b, _, resid2 = ols(X, y_step)
    Xstep = np.column_stack([X, (t_obs >= 3.0 * 365.25).astype(float)])
    b3, s2c, cov3, _ = ols(Xstep, y_step)
    print(f"series has a step of +0.060 at year 3.0")
    print(f"single-trend model residual sd = {np.sqrt(s2b):.4f}")
    print(f"step model residual sd         = {np.sqrt(s2c):.4f}")
    print(f"step size recovered = {b3[-1]:+.4f} "
          f"(true 0.060), se = {np.sqrt(cov3[-1, -1]):.4f}")
    print("A smooth trend through a step is a model error, not noise. The")
    print("residual power at the break is the signal that a change happened.")


if __name__ == "__main__":
    main()
