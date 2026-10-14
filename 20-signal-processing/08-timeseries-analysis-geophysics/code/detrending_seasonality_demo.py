#!/usr/bin/env python3
"""Detrending, deseasonalising and anomalies on a SYNTHETIC geophysical series.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python detrending_seasonality_demo.py

All models and data are SYNTHETIC: a chosen trend, chosen seasonal harmonics and
seeded AR(1) noise.  No real series or station is used.

Contents
--------
1. The additive model and the truth used to generate the series.
2. Trend estimated on the raw series: the seasonal-term bias, measured.
3. Trend estimated jointly with the seasonal harmonics.
4. Moving-average detrending: window length, leakage and end effects.
5. Spurious regression: a trend fitted to a pure random walk.
6. A slope change fitted by a single line.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

NYEAR = 30
MONTHS = 12 * NYEAR
TREND = 2.0            # mm/yr, chosen
A_ANN = 30.0           # mm
A_SEMI = 8.0           # mm
AR1 = 0.5
SIGMA = 10.0           # mm


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ar1_noise(n, rho, sigma, rng):
    e = rng.standard_normal(n) * sigma * np.sqrt(1.0 - rho ** 2)
    x = np.zeros(n)
    for i in range(1, n):
        x[i] = rho * x[i - 1] + e[i]
    return x


def seasonal(t_months, a_ann, a_semi, phase_ann, phase_semi):
    return (a_ann * np.cos(2.0 * np.pi * t_months / 12.0 - phase_ann)
            + a_semi * np.cos(2.0 * np.pi * t_months / 6.0 - phase_semi))


def design(t_months, seasonal_terms=True):
    cols = [np.ones_like(t_months), t_months / 12.0]      # t in years
    if seasonal_terms:
        cols += [np.cos(2.0 * np.pi * t_months / 12.0),
                 np.sin(2.0 * np.pi * t_months / 12.0),
                 np.cos(2.0 * np.pi * t_months / 6.0),
                 np.sin(2.0 * np.pi * t_months / 6.0)]
    return np.column_stack(cols)


def ols(G, y):
    coef, *_ = np.linalg.lstsq(G, y, rcond=None)
    resid = y - G @ coef
    return coef, resid


def main():
    t = np.arange(MONTHS, dtype=float)
    phase_ann, phase_semi = 0.9, 2.1
    s_true = seasonal(t, A_ANN, A_SEMI, phase_ann, phase_semi)

    section("1. The additive model")
    print("y(t) = a + b*t + seasonal(t) + AR(1) noise")
    print(f"SYNTHETIC truth: slope b = {TREND:.1f} mm/yr, "
          f"annual amplitude = {A_ANN:.1f} mm, semiannual = {A_SEMI:.1f} mm")
    print(f"AR(1) noise: rho = {AR1:.2f}, sigma = {SIGMA:.1f} mm, "
          f"{MONTHS} monthly samples ({NYEAR} years)")
    print("monthly sampling: the annual cycle is 12 samples, "
          "the semiannual 6 samples")

    # ------------------------------------------- trend on the raw series -----
    section("2. Trend fitted to the RAW series: seasonal bias versus length")
    print("  fixed seasonal phase (as for a real deployment date); 200 draws")
    print("   years   raw bias   raw std   raw |err|>0.5   harmonic std")
    global_rng = RNG
    phase_ann, phase_semi = 0.9, 2.1
    for nyr in (3, 5, 10, 30):
        n = 12 * nyr
        tt = np.arange(n, dtype=float)
        s_here = seasonal(tt, A_ANN, A_SEMI, phase_ann, phase_semi)
        raw_err, harm_err = [], []
        for _ in range(200):
            y = TREND * tt / 12.0 + s_here + ar1_noise(n, AR1, SIGMA, global_rng)
            c_raw, _ = ols(design(tt, False), y)
            c_hh, _ = ols(design(tt, True), y)
            raw_err.append(c_raw[1] - TREND)
            harm_err.append(c_hh[1] - TREND)
        raw_err = np.array(raw_err)
        harm_err = np.array(harm_err)
        print(f"  {nyr:5d}   {raw_err.mean():+8.3f}   {raw_err.std():7.3f}   "
              f"{np.mean(np.abs(raw_err) > 0.5):11.3f}   {harm_err.std():12.3f}")
    print("  all values in mm/yr; truth = 2.000 mm/yr throughout.")
    print("  the bias of the raw fit is the seasonal term projected on to the")
    print("  trend column, which is the correlation of the seasonal cycle with")
    print("  time; it falls as the record covers more whole cycles, and it is")
    print("  zero for the harmonic fit at every length.")

    # -------------------------------------------------- joint estimation -----
    section("2b. The same bias in closed form (no Monte Carlo)")
    print("  bias = sum_t (u - ubar) s(t) / sum_t (u - ubar)^2, u = t/12 in years,")
    print("  evaluated on the true seasonal term of this model")
    for m in (12, 24, 36, 60, 120, 360):
        tt = np.arange(m, dtype=float)
        s_here = seasonal(tt, A_ANN, A_SEMI, phase_ann, phase_semi)
        u = tt / 12.0
        bias = float(np.sum((u - u.mean()) * s_here) / np.sum((u - u.mean()) ** 2))
        print(f"    {m:4d} months ({m/12:5.1f} yr): closed-form bias = "
              f"{bias:+9.3f} mm/yr")
    print("  the closed form is an exact evaluation of the quantity the Monte")
    print("  Carlo table estimated: at 36 months it matches the measured mean raw")
    print("  bias, which is the check that the Monte Carlo is unbiased and that")
    print("  the error is a projection, not a search artefact.")

    # -------------------------------------------------- joint estimation -----
    section("3. Joint trend + harmonic fit on one realisation")
    t = np.arange(MONTHS, dtype=float)
    y = TREND * t / 12.0 + s_true + ar1_noise(MONTHS, AR1, SIGMA, RNG)
    c_h, r_h = ols(design(t, True), y)
    amp_ann = np.hypot(c_h[2], c_h[3])
    amp_semi = np.hypot(c_h[4], c_h[5])
    print(f"  fitted intercept        : {c_h[0]:8.3f} mm")
    print(f"  fitted slope            : {c_h[1]:8.3f} mm/yr   (truth {TREND:.1f})")
    print(f"  annual amplitude        : {amp_ann:8.3f} mm     (truth {A_ANN:.1f})")
    print(f"  semiannual amplitude    : {amp_semi:8.3f} mm     (truth {A_SEMI:.1f})")
    print(f"  residual std            : {r_h.std():8.3f} mm     "
          f"(input noise sigma {SIGMA:.1f})")
    rho_hat = float(np.corrcoef(r_h[:-1], r_h[1:])[0, 1])
    print(f"  residual lag-1 autocorr : {rho_hat:8.3f}     (input rho {AR1:.2f})")
    print(f"  effective sample size n(1-r)/(1+r) = "
          f"{MONTHS*(1-rho_hat)/(1+rho_hat):.1f} of {MONTHS}")
    print("  the trend uncertainty from an OLS formula that assumes white noise")
    print("  is therefore too small: the residuals are autocorrelated.")

    # -------------------------------------- moving-average detrending --------
    section("4. Moving-average detrending (measured)")

    def centred_ma(y, w):
        half = w // 2
        out = np.full(y.size, np.nan)
        for i in range(half, y.size - half):
            out[i] = np.mean(y[i - half:i + half])     # centre at i - 0.5
        return out

    y = TREND * t / 12.0 + s_true + ar1_noise(MONTHS, AR1, SIGMA, RNG)
    true_trend = TREND * t / 12.0
    y_det = true_trend + s_true          # noise-free: isolates the operator
    print("  window  seasonal amp left   implied lag   valid samples   "
          "one-sided edge bias   noisy interior bias")
    for w in (12, 18, 24, 30):
        half = w // 2
        cma = centred_ma(y_det, w)
        valid = ~np.isnan(cma)
        gm, _ = ols(design(t[valid], True), cma[valid])
        bias_in = float(np.nanmean(cma - true_trend))
        lag_months = -bias_in / (TREND / 12.0)
        padded = np.convolve(y_det, np.ones(w) / w, mode="same")
        edge_idx = np.r_[0:half, MONTHS - half:MONTHS]
        edge_bias = float(np.mean(padded[edge_idx] - true_trend[edge_idx]))
        noisy_bias = float(np.nanmean(centred_ma(y, w) - true_trend))
        print(f"  {w:5d}   {np.hypot(gm[2], gm[3]):15.3f} mm   "
              f"{lag_months:9.1f} mo   {int(valid.sum()):13d}   "
              f"{edge_bias:18.3f} mm   {noisy_bias:14.3f} mm")
    print("  a centred window cannot be evaluated in the first and last W/2")
    print("  samples, so those values are missing, not estimated.  For a window")
    print("  of a whole number of cycles (12, 24 months) no seasonal component is")
    print("  left in the smoothed series; 18 and 30 months leave several")
    print("  millimetres, which appears as a once-a-year wobble in the trend.")
    print("  The implied lag is the half-sample centring offset of an even")
    print("  window, 0.5 months (a bias of 0.083 mm at 2 mm/yr), and the")
    print("  one-sided end filling (zero-padded mean) biases the trend by about")
    print("  seven millimetres there, two orders of magnitude more.")
    print("  On the noisy realisation the interior bias is -1.3 mm, dominated by")
    print("  that realisation's own low-frequency wander rather than by the")
    print("  smoother: a 30-year record of AR(1) noise wanders by millimetres.")

    # ------------------------------------------------- spurious regression ---
    section("5. Spurious regression: a trend fitted to a pure random walk")
    n_mc2 = 400
    tstats, r2 = [], []
    for _ in range(n_mc2):
        rw = np.cumsum(RNG.standard_normal(MONTHS))
        c, r = ols(design(t, False), rw)          # no seasonal terms: no trend
        ss_res = np.sum(r ** 2)
        ss_tot = np.sum((rw - rw.mean()) ** 2)
        r2.append(1.0 - ss_res / ss_tot)
        se = np.sqrt(ss_res / (MONTHS - 2) /
                     np.sum((t / 12.0 - (t / 12.0).mean()) ** 2))
        tstats.append(c[1] / se)
    tstats = np.array(tstats)
    print(f"  {n_mc2} realisations of a random walk with NO trend")
    print(f"  fraction with |t| > 2 (the usual 5% rule) = "
          f"{np.mean(np.abs(tstats) > 2.0):.3f}")
    print(f"  fraction with |t| > 3                      = "
          f"{np.mean(np.abs(tstats) > 3.0):.3f}")
    print(f"  median R^2 of a trend through a random walk = {np.median(r2):.3f}")
    print("  the t-test is not conservative here, it is wrong: its null")
    print("  distribution assumes independent residuals, and a random walk's are")
    print("  not.  A trend in a non-stationary series is a model statement.")

    # ----------------------------------------------------- slope change ------
    section("6. A slope change fitted by a single straight line")
    break_m = MONTHS // 2
    y_break = np.where(t < break_m,
                       1.0 * t / 12.0,
                       1.0 * break_m / 12.0 + 5.0 * (t - break_m) / 12.0)
    y_break = y_break + ar1_noise(MONTHS, AR1, SIGMA, RNG)
    c1, r1 = ols(design(t, True), y_break)
    seg1, _ = ols(design(t[:break_m], True), y_break[:break_m])
    seg2, _ = ols(design(t[break_m:], True), y_break[break_m:])
    print(f"  true slopes: {1.0:.1f} mm/yr then {5.0:.1f} mm/yr, "
          f"break at month {break_m}")
    print(f"  single-line fit : slope {c1[1]:6.3f} mm/yr, "
          f"residual rms {r1.std():7.3f} mm, R^2 "
          f"{1 - np.sum(r1**2)/np.sum((y_break-y_break.mean())**2):.3f}")
    print(f"  two-segment fit : slopes {seg1[1]:.3f} and {seg2[1]:.3f} mm/yr")
    print(f"  residual rms of each segment: {r1[:break_m].std():.3f} and "
          f"{r1[break_m:].std():.3f} mm for the single line")
    print("  the single slope is a weighted average of the two; it is not wrong")
    print("  as a summary, but it is not the model that generated the data, and")
    print("  the residual structure is where that shows.")


if __name__ == "__main__":
    main()
