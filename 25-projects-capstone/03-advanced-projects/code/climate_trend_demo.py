#!/usr/bin/env python3
"""Advanced project 4: trend estimation in a climate-style time series, and the
uncertainty inflation that autocorrelation forces on the error bar.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_trend_demo.py

Everything here is SYNTHETIC.  The series is generated from a chosen trend, a
chosen seasonal cycle and a chosen AR(1) noise process; no station record, no
reanalysis product and no published trend is used.

Sections
--------
1. The synthetic series and its components.
2. Trend and seasonality by least squares: the naive and the corrected error bar.
3. The false-positive rate of the naive test, measured on red-noise surrogates.
4. Annual means, and what averaging actually buys.
5. What the analysis does not establish.
"""

import numpy as np
from scipy.signal import lfilter

RNG = np.random.default_rng(20261014)

N_YEARS = 50
MONTHS_PER_YEAR = 12
DT = 1.0 / MONTHS_PER_YEAR          # sample interval, years
TREND_TRUE = 0.020                  # deg C per year
AR_PHI = 0.70                       # monthly lag-1 autocorrelation
AR_SIGMA = 0.50                     # AR(1) innovation standard deviation, deg C
SEASONAL = (8.0, -1.5)              # cosine and sine amplitudes, deg C
N_SURROGATE = 500                   # Monte Carlo realisations
T_CRIT = 1.96                       # two-sided 5% normal critical value


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def make_series(rng, trend, phi, sigma, seasonal):
    n = N_YEARS * MONTHS_PER_YEAR
    t = np.arange(n) * DT
    noise = lfilter([1.0], [1.0, -phi], sigma * rng.standard_normal(n))
    signal = (trend * t
              + seasonal[0] * np.cos(2 * np.pi * t)
              + seasonal[1] * np.sin(2 * np.pi * t))
    return t, signal + noise, noise


def design(t):
    """Intercept, trend, annual cosine and annual sine."""
    return np.column_stack([np.ones_like(t), t,
                            np.cos(2 * np.pi * t), np.sin(2 * np.pi * t)])


def fit_trend(t, y):
    """Least-squares trend with its naive standard error."""
    a = design(t)
    cov = np.linalg.inv(a.T @ a)
    coef = cov @ a.T @ y
    resid = y - a @ coef
    dof = t.size - a.shape[1]
    s2 = resid @ resid / dof
    return coef[1], np.sqrt(s2 * cov[1, 1]), resid


def fit_linear(t, y):
    """Least-squares trend on an annual series (no seasonal terms)."""
    a = np.column_stack([np.ones_like(t), t])
    cov = np.linalg.inv(a.T @ a)
    coef = cov @ a.T @ y
    resid = y - a @ coef
    s2 = resid @ resid / (t.size - 2)
    return coef[1], np.sqrt(s2 * cov[1, 1]), resid


def lag1_autocorr(resid):
    r = resid - resid.mean()
    return float((r[:-1] @ r[1:]) / (r @ r))


def main():
    t, y, noise = make_series(RNG, TREND_TRUE, AR_PHI, AR_SIGMA, SEASONAL)

    section("1. The synthetic series")
    print(f"SYNTHETIC monthly series: {y.size} months = {N_YEARS} years, "
          f"dt = {DT:.6f} yr")
    print(f"  imposed trend {TREND_TRUE:+.4f} deg C/yr "
          f"= {TREND_TRUE * 10:+.3f} deg C/decade")
    print(f"  seasonal cycle amplitudes {SEASONAL[0]:.1f} and "
          f"{SEASONAL[1]:.1f} deg C")
    print(f"  AR(1) noise: phi = {AR_PHI:.2f} per month, sigma = "
          f"{AR_SIGMA:.2f} deg C; stationary sd = "
          f"{AR_SIGMA / np.sqrt(1 - AR_PHI ** 2):.3f} deg C")
    print(f"  series range {y.min():.2f} to {y.max():.2f} deg C; "
          f"first-year mean {y[:12].mean():.2f}, "
          f"last-year mean {y[-12:].mean():.2f} deg C")

    section("2. Trend and seasonality by least squares")
    slope, se_naive, resid = fit_trend(t, y)
    rho = lag1_autocorr(resid)
    tau_int = DT * (1.0 + rho) / (1.0 - rho)
    inflation = np.sqrt(tau_int / DT)
    se_corrected = se_naive * inflation
    print(f"  fit y = a + b t + c cos + d sin: b = {slope:+.6f} deg C/yr "
          f"(true {TREND_TRUE:+.4f})")
    print(f"  residual lag-1 autocorrelation rho = {rho:.4f}")
    print(f"  integrated time tau_int = dt (1+rho)/(1-rho) = {tau_int:.4f} yr "
          f"({tau_int / DT:.2f} samples)")
    print(f"  naive standard error        = {se_naive:.6f} deg C/yr")
    print(f"  autocorrelation inflation   = {inflation:.3f} "
          f"(sqrt((1+rho)/(1-rho)))")
    print(f"  corrected standard error    = {se_corrected:.6f} deg C/yr")
    print(f"  trend = {slope:.5f} +/- {se_naive:.5f} (naive) or "
          f"+/- {se_corrected:.5f} (corrected) deg C/yr")
    print(f"  the naive test gives t = {slope / se_naive:.2f}; the corrected "
          f"test gives t = {slope / se_corrected:.2f}")

    section("3. The false-positive rate of the naive test, measured")
    fp_naive = fp_corrected = 0
    for _ in range(N_SURROGATE):
        t_s, y_s, _ = make_series(RNG, 0.0, AR_PHI, AR_SIGMA, SEASONAL)
        b_s, se_s, res_s = fit_trend(t_s, y_s)
        r_s = lag1_autocorr(res_s)
        infl = np.sqrt((1.0 + r_s) / (1.0 - r_s))
        fp_naive += abs(b_s / se_s) > T_CRIT
        fp_corrected += abs(b_s / (se_s * infl)) > T_CRIT
    print(f"  {N_SURROGATE} surrogates with NO trend, tested at |t| > "
          f"{T_CRIT:.2f} (nominal 5%):")
    print(f"    naive t-test false positives      = {fp_naive:4d} "
          f"({fp_naive / N_SURROGATE:.1%})")
    print(f"    corrected t-test false positives  = {fp_corrected:4d} "
          f"({fp_corrected / N_SURROGATE:.1%})")
    print(f"  the naive test is wrong by a factor of "
          f"{(fp_naive / max(fp_corrected, 1)):.1f} in error rate")

    section("4. Annual means, and what averaging buys")
    annual = y.reshape(N_YEARS, MONTHS_PER_YEAR).mean(axis=1)
    t_annual = np.arange(N_YEARS) + 0.5
    slope_a, se_a_naive, resid_a = fit_linear(t_annual, annual)
    rho_a = lag1_autocorr(resid_a)
    infl_a = np.sqrt((1.0 + rho_a) / (1.0 - rho_a))
    print(f"  trend from {N_YEARS} annual means = {slope_a:+.6f} deg C/yr "
          f"(true {TREND_TRUE:+.4f})")
    print(f"  residual lag-1 autocorrelation    = {rho_a:.4f} "
          f"(monthly value was {rho:.4f})")
    print(f"  naive standard error              = {se_a_naive:.6f} deg C/yr")
    print(f"  inflation needed                  = {infl_a:.3f}")
    print(f"  corrected standard error          = {se_a_naive * infl_a:.6f} "
          f"deg C/yr")
    print(f"  ratio of monthly to annual corrected errors = "
          f"{se_corrected / (se_a_naive * infl_a):.3f}")
    print("  -> annual averaging removes most but not all of the month-to-month")
    print("     correlation, and it does not remove the correlation that carries")
    print("     over between years (the memory of the process).")

    section("5. What the analysis does not establish")
    print("  1. the trend is LINEAR by assumption; a curvature or a step is")
    print("     fitted as trend plus noise;")
    print("  2. the noise is AR(1) and stationary; a change in variance or a")
    print("     long-memory process changes the inflation factor;")
    print("  3. the confidence interval is for THIS station, not for a region:")
    print("     spatial correlation between stations is a second, separate")
    print("     inflation that the time series cannot see;")
    print("  4. a significant trend is not an attribution: this synthetic series")
    print("     was generated WITH a trend, so the only question the analysis can")
    print("     answer is whether the trend is detectable.");
    print(f"  5. the seasonal cycle was fitted with two harmonics; the residual")
    print(f"     autocorrelation of {rho:.3f} shows what is left.")


if __name__ == "__main__":
    main()
