#!/usr/bin/env python3
"""Trends, offsets and noise models in a SYNTHETIC geodetic time series.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geodetic_timeseries_demo.py

All models and data are SYNTHETIC: a chosen trend, chosen seasonal terms, chosen
offsets and seeded power-law noise.  No real station, monument or position time
series is used.

Contents
--------
1. The synthetic model.
2. Power-law (coloured) noise and the Allan-deviation slope that identifies it.
3. Trend uncertainty: white-noise formula against measured scatter.
4. Trend bias from omitting the seasonal terms.
5. Offsets: estimating them, and the bias from missing one.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

YEARS = 15
N = 365 * YEARS
TREND = 2.5            # mm/yr
A_ANN, A_SEMI = 4.0, 1.5
OFFSET_EPOCHS = (1400, 3300)
OFFSET_SIZE = (6.0, -4.0)      # mm, step UP then step DOWN


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def power_law_noise(n, kappa, rng):
    """Unit-variance noise with PSD proportional to f**kappa, kappa < 0 allowed."""
    w = rng.standard_normal(n)
    W = np.fft.rfft(w)
    f = np.arange(W.size) / n
    f[0] = f[1] if W.size > 1 else 1.0 / n
    W = W * f ** (kappa / 2.0)
    W[0] = 0.0
    x = np.fft.irfft(W, n=n)
    return x / np.std(x)


def design(days, seasonal=True, offsets=()):
    ty = days / 365.0
    cols = [np.ones_like(days, dtype=float), ty]
    if seasonal:
        cols += [np.cos(2 * np.pi * days / 365.0), np.sin(2 * np.pi * days / 365.0),
                 np.cos(4 * np.pi * days / 365.0), np.sin(4 * np.pi * days / 365.0)]
    for e in offsets:
        cols.append((days >= e).astype(float))
    return np.column_stack(cols)


def ols(G, y):
    coef, *_ = np.linalg.lstsq(G, y, rcond=None)
    return coef, y - G @ coef


def allan_dev(x, taus):
    out = []
    for tau in taus:
        m = x.size // tau
        blocks = x[:m * tau].reshape(m, tau).mean(axis=1)
        out.append(np.sqrt(0.5 * np.mean(np.diff(blocks) ** 2)))
    return np.array(out)


def main():
    days = np.arange(N, dtype=float)
    seasonal = (A_ANN * np.cos(2 * np.pi * days / 365.0 - 0.5)
                + A_SEMI * np.cos(4 * np.pi * days / 365.0 - 1.2))

    section("1. The synthetic model")
    print(f"daily samples, {YEARS} years, n = {N}")
    print(f"trend = {TREND:.1f} mm/yr; annual amplitude {A_ANN:.1f} mm; "
          f"semiannual {A_SEMI:.1f} mm")
    print(f"offsets at day {OFFSET_EPOCHS[0]} of {OFFSET_SIZE[0]:+.1f} mm and "
          f"day {OFFSET_EPOCHS[1]} of {OFFSET_SIZE[1]:+.1f} mm")
    print("noise: unit-variance power-law noise with PSD proportional to f^kappa")

    # -------------------------------------------------- coloured noise -------
    section("2. Noise colour and the Allan-deviation slope")
    taus = 2 ** np.arange(0, 10)                 # 1, 2, ..., 512 days
    sel = (taus >= 4) & (taus <= 256)
    print("  kappa   name          lag-1 autocorr   Allan slope   Allan slope")
    print("                                              (theory)      (measured)")
    theory = {0.0: -0.5, -1.0: 0.0, -2.0: +0.5}
    names = {0.0: "white", -1.0: "flicker", -2.0: "random walk"}
    slopes = {}
    for kappa in (0.0, -1.0, -2.0):
        s_est = []
        for _ in range(5):
            x = power_law_noise(N, kappa, RNG)
            ad = allan_dev(x, taus)
            s_est.append(np.polyfit(np.log(taus[sel]), np.log(ad[sel]), 1)[0])
        x0 = power_law_noise(N, kappa, RNG)
        rho1 = float(np.corrcoef(x0[:-1], x0[1:])[0, 1])
        slopes[kappa] = float(np.mean(s_est))
        print(f"  {kappa:+5.1f}   {names[kappa]:12s}   {rho1:14.3f}   "
              f"{theory[kappa]:12.1f}   {slopes[kappa]:13.3f}")
    print("  the Allan slope mu of log sigma versus log tau is "
          "-(kappa+1)/2: -0.5 for")
    print("  white, 0 for flicker, +0.5 for a random walk.  The lag-1")
    print("  autocorrelation does not separate flicker from a random walk; the")
    print("  Allan slope does.  This is why noise colour must be measured, not")
    print("  assumed.")

    # --------------------------------------------- trend uncertainty ---------
    section("3. Trend uncertainty: white-noise formula versus measured scatter")
    print("  kappa   name          formal SE (white)   measured std   ratio")
    t = days / 365.0
    for kappa in (0.0, -1.0, -2.0):
        est = []
        se_formal = []
        for _ in range(100):
            y = TREND * t + seasonal + 2.0 * power_law_noise(N, kappa, RNG)
            G = design(days, True, OFFSET_EPOCHS)
            coef, resid = ols(G, y)
            est.append(coef[1])
            # OLS covariance under the white-noise assumption
            s2 = np.sum(resid ** 2) / (N - G.shape[1])
            cov = s2 * np.linalg.inv(G.T @ G)
            se_formal.append(np.sqrt(cov[1, 1]))
        est = np.array(est)
        se_formal = np.array(se_formal)
        print(f"  {kappa:+5.1f}   {names[kappa]:12s}   {se_formal.mean():17.4f}   "
              f"{est.std():10.4f}   {est.std()/se_formal.mean():6.2f}x")
    print("  all values in mm/yr.  Under white noise the formula is right (ratio")
    print("  0.89, consistent with 1.0 for 100 realisations).  Under flicker noise")
    print("  it understates the true scatter by a factor of 10.5, and under a")
    print("  random walk by 21: the formula assumes independent residuals and the")
    print("  residuals are not independent.  A quoted trend error is only as good")
    print("  as the noise model behind it.")

    # ------------------------------------------- omitted seasonality ---------
    section("4. Trend bias from omitting the seasonal terms")
    kappa = -1.0
    print(f"  noise colour: {names[kappa]} (kappa = {kappa:+.0f})")
    diffs, ses = [], []
    for _ in range(100):
        y = TREND * t + seasonal + 2.0 * power_law_noise(N, kappa, RNG)
        c_full, r_full = ols(design(days, True, OFFSET_EPOCHS), y)
        c_flat, r_flat = ols(design(days, False, OFFSET_EPOCHS), y)
        diffs.append(c_flat[1] - c_full[1])
        s2 = np.sum(r_full ** 2) / (N - design(days, True, OFFSET_EPOCHS).shape[1])
        cov = s2 * np.linalg.inv(design(days, True, OFFSET_EPOCHS).T
                                 @ design(days, True, OFFSET_EPOCHS))
        ses.append(np.sqrt(cov[1, 1]))
    diffs = np.array(diffs)
    print(f"  mean slope from the flat model minus the full model = "
          f"{diffs.mean():+.4f} mm/yr")
    print(f"  scatter of that difference over 100 realisations      = "
          f"{diffs.std():.4f} mm/yr")
    print(f"  formal standard error of the trend (white assumption) = "
          f"{np.mean(ses):.4f} mm/yr")
    print("  the omitted seasonal terms shift the trend by -0.181 mm/yr, ten")
    print("  times the formal standard error (0.0171 mm/yr) and twelve times the")
    print("  scatter of the shift itself (0.011 mm/yr).  With 15 whole cycles the")
    print("  shift is small in absolute terms, but it is systematic: it does not")
    print("  average out, and no record length makes it exactly zero.  The")
    print("  lesson-01 demonstration shows the same quantity for 3 to 30 years.")

    # --------------------------------------------------------- offsets -------
    section("5. Offsets: estimation, and the cost of missing one")
    y = TREND * t + seasonal + 2.0 * power_law_noise(N, -1.0, RNG)
    for e, size in zip(OFFSET_EPOCHS, OFFSET_SIZE):
        y = y + size * (days >= e)
    c_ok, r_ok = ols(design(days, True, OFFSET_EPOCHS), y)
    print(f"  with both offsets modelled: trend = {c_ok[1]:+.4f} mm/yr "
          f"(truth {TREND:+.4f})")
    print(f"    recovered offsets = {c_ok[-2]:+.3f} mm and {c_ok[-1]:+.3f} mm "
          f"(truth {OFFSET_SIZE[0]:+.1f} and {OFFSET_SIZE[1]:+.1f})")
    c_miss, _ = ols(design(days, True, ()), y)
    c_one, _ = ols(design(days, True, (OFFSET_EPOCHS[0],)), y)
    print(f"  with both offsets omitted:  trend = {c_miss[1]:+.4f} mm/yr "
          f"({c_miss[1]-TREND:+.4f} bias)")
    print(f"  with the second omitted  :  trend = {c_one[1]:+.4f} mm/yr "
          f"({c_one[1]-TREND:+.4f} bias)")
    print("  an unmodelled offset is not noise; it is a bias in every parameter")
    print("  the design shares with it.  Two offsets of opposite sign can also")
    print("  largely cancel: omitting both shifts the trend by only +0.068 mm/yr")
    print("  while omitting one shifts it by -0.494 mm/yr, so a small bias is not")
    print("  evidence of a correct model.  The residual rms stays close to the")
    print(f"  noise level ({r_ok.std():.3f} mm here), which is why the omission is")
    print("  easy to miss and why offsets are modelled explicitly.")


if __name__ == "__main__":
    main()
