#!/usr/bin/env python3
"""Change detection and time-series analysis on synthetic image data.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python change_detection_demo.py

Everything is SYNTHETIC.  The scene classes, the illumination differences, the
change patch, the time-series trend, seasonality, breakpoint and noise are chosen
teaching values in this file.  No real scene, sensor, product or time series is
represented.

Contents
--------
1. A two-date synthetic scene and a real change patch.
2. Differencing against ratioing: what the illumination does to each.
3. Change vector analysis: magnitude, angle and a threshold trade-off.
4. The cost of misregistration: differencing is an edge detector.
5. A synthetic time series with trend, seasonality and a breakpoint.
6. Theil-Sen against least squares under a breakpoint.
7. Mann-Kendall trend testing and its false-positive rate, including autocorrelation.
8. A spurious trend manufactured by an uncorrected radiometric drift.
9. Verification: Theil-Sen on noise-free linear data.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N = 120                      # SYNTHETIC number of monthly observations
SEASONAL_AMP = 0.050         # index units
NOISE_SD = 0.020             # index units
TRUE_TREND_PER_MONTH = 5.0e-4
BREAK_AT = 60                # a step at the midpoint of the record
BREAK_SIZE = -0.080          # index units, an abrupt loss
SPIKE_AT = 40                # a short contamination episode
SPIKE_LEN = 6                # months
SPIKE_SIZE = 0.250           # index units


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def synthetic_scene(n=120):
    """Two-date SYNTHETIC land-cover reflectance in two notional bands."""
    classes = {"soil": np.array([0.30, 0.40]),
               "vegetation": np.array([0.06, 0.45]),
               "water": np.array([0.05, 0.03])}
    labels = np.zeros((n, n), dtype=int)
    labels[:, n // 3:2 * n // 3] = 1
    labels[:, 2 * n // 3:] = 2
    labels[n // 4:3 * n // 4, n // 3:n // 2] = 2      # a lake patch (truth)
    rho1 = np.array(list(classes.values()))[labels]
    rho2 = rho1.copy()
    # a real change: the lake patch gains vegetation-like reflectance in band 2
    rho2[n // 4:3 * n // 4, n // 3:n // 2] = classes["vegetation"]
    # a multiplicative illumination difference between the two dates
    gain = 1.10
    rho2 = rho2 * gain
    # independent noise in each acquisition
    rho1 = rho1 + 0.004 * RNG.standard_normal(rho1.shape)
    rho2 = rho2 + 0.004 * RNG.standard_normal(rho2.shape)
    return rho1, rho2, labels


def theil_sen(y):
    """Theil-Sen slope estimate: median of pairwise slopes."""
    n = len(y)
    i, j = np.triu_indices(n, k=1)
    return float(np.median((y[j] - y[i]) / (j - i)))


def mann_kendall(y):
    """Mann-Kendall S and its z statistic (no tie correction)."""
    n = len(y)
    s = 0
    for i in range(n - 1):
        s += int(np.sum(np.sign(y[i + 1:] - y[i])))
    var_s = n * (n - 1) * (2 * n + 5) / 18.0
    z = (s - np.sign(s)) / np.sqrt(var_s) if s != 0 else 0.0
    return s, float(z), var_s


def ar1(n, rho, rng):
    e = rng.standard_normal(n)
    x = np.zeros(n)
    for i in range(1, n):
        x[i] = rho * x[i - 1] + e[i]
    return x / x.std(ddof=1)


def deseasonalise(y, period=12):
    """Remove a mean seasonal cycle by subtracting the calendar-month climatology."""
    t = np.arange(len(y))
    phase = t % period
    out = y.copy()
    for m in range(period):
        sel = phase == m
        out[sel] = y[sel] - y[sel].mean()
    return out


def make_series(rng, with_break=True, rho_ar=0.0, spike=False, with_trend=True):
    t = np.arange(N)
    seasonal = SEASONAL_AMP * np.sin(2.0 * np.pi * t / 12.0)
    trend = TRUE_TREND_PER_MONTH * t if with_trend else 0.0 * t
    if rho_ar > 0.0:
        noise = NOISE_SD * ar1(N, rho_ar, rng)
    else:
        noise = NOISE_SD * rng.standard_normal(N)
    y = 0.50 + trend + seasonal + noise
    if with_break:
        y[BREAK_AT:] += BREAK_SIZE
    if spike:
        y[SPIKE_AT:SPIKE_AT + SPIKE_LEN] += SPIKE_SIZE
    return y


def main():
    section("1. A two-date synthetic scene and the change patch")
    rho1, rho2, labels = synthetic_scene()
    print(f"  scene {labels.shape}, classes soil/vegetation/water in vertical strips")
    print("  a rectangular LAKE patch (water) inside the vegetation strip is")
    print("  replaced by vegetation between the dates -- the real change")
    print("  a UNIFORM gain of 1.10 is applied to the second date (illumination)")
    print(f"  independent band noise sd = 0.004 reflectance units")
    patch = (slice(N // 4, 3 * N // 4), slice(N // 3, N // 2))
    band2_ratio = rho2[:, :, 1] / rho1[:, :, 1]
    print(f"  mean band-2 ratio inside the patch  = {band2_ratio[patch].mean():.4f}")
    outside = np.ones_like(band2_ratio, dtype=bool)
    outside[patch] = False
    print(f"  mean band-2 ratio outside the patch = {band2_ratio[outside].mean():.4f}")
    print("  Both differ from the applied gain of 1.10: inside, the real change")
    print("  dominates the illumination; outside, the ratio recovers the gain exactly.")

    section("2. Differencing against ratioing")
    band2_diff = rho2[:, :, 1] - rho1[:, :, 1]
    print("   region            mean difference   mean ratio   mean normalised difference")
    for name, mask in (("inside the patch", patch), ("all but the patch", outside)):
        d = band2_diff[mask].mean()
        r = band2_ratio[mask].mean()
        nd = ((rho2[:, :, 1] - rho2[:, :, 0]) / (rho2[:, :, 1] + rho2[:, :, 0]))[mask].mean()
        print(f"  {name:20s} {d:17.4f} {r:12.4f} {nd:25.4f}")
    print("  The DIFFERENCE inside the patch is large partly because the whole scene")
    print("  brightened by 10%; the RATIO inside the patch is a single value while")
    print("  outside it reproduces the gain everywhere.  A difference image detects")
    print("  illumination as change; a ratio (or a normalised difference) does not,")
    print("  but it also DISCARDS albedo change, which is sometimes the signal.")
    print(f"  noise on the difference: theoretical sigma = sqrt(2) x 0.004 = "
          f"{np.sqrt(2) * 0.004:.5f}")
    print(f"  measured difference sd in a uniform region = "
          f"{band2_diff[:, :20].std():.5f}")

    section("3. Change vector analysis: magnitude and angle")
    diff = rho2 - rho1
    mag = np.linalg.norm(diff, axis=2)
    angle = np.degrees(np.arctan2(diff[:, :, 1], diff[:, :, 0]))
    print(f"  change magnitude inside the patch = {mag[patch].mean():.4f}, "
          f"outside = {mag[outside].mean():.4f}")
    print(f"  change angle (deg) inside the patch = {angle[patch].mean():.2f}, "
          f"outside = {angle[outside].mean():.2f}")
    print("  Thresholding the magnitude at k times the no-change sd:")
    sd = mag[outside].std()
    print("   threshold   fraction flagged outside (false alarms)   fraction flagged inside")
    for k in (1.0, 1.5, 2.0, 3.0, 5.0):
        thr = k * sd
        print(f"  {k:9.1f}   {np.mean(mag[outside] > thr):31.4f}   "
              f"{np.mean(mag[patch] > thr):24.4f}")
    print("  A single threshold trades misses against false alarms, and the trade is")
    print("  the deliverable: report both fractions, never just 'significant change'.")

    section("4. The cost of misregistration")
    print("  shift the second date by an integer number of pixels before differencing:")
    print("   shift (px)   mean |difference| outside the patch   ratio to no-shift")
    base = np.abs(band2_diff[outside]).mean()
    for sh in (0, 1, 2, 3):
        shifted = np.roll(rho2[:, :, 1], sh, axis=1)
        d = np.abs((shifted - rho1[:, :, 1]))
        print(f"  {sh:11d}   {d[outside].mean():39.4f}   {d[outside].mean() / base:15.2f}")
    print("  A sub-pixel or one-pixel misregistration turns every class boundary into")
    print("  a large apparent change.  The differencing operator is a spatial")
    print("  high-pass filter, so it responds to edges first -- which is why")
    print("  registration to a fraction of a pixel and a radiometric normalisation are")
    print("  prerequisites, not refinements.")

    section("5. A synthetic time series with trend, seasonality and a breakpoint")
    y = make_series(RNG, with_break=True)
    t = np.arange(N)
    print(f"  SYNTHETIC truth: trend {TRUE_TREND_PER_MONTH:.1e} per month "
          f"({TRUE_TREND_PER_MONTH * 12:.4f} per year), seasonal amplitude "
          f"{SEASONAL_AMP:.3f},")
    print(f"  noise sd {NOISE_SD:.3f}, an abrupt step of {BREAK_SIZE:+.3f} at "
          f"month {BREAK_AT}")
    print(f"  the step is {abs(BREAK_SIZE) / NOISE_SD:.1f} noise sigma and "
          f"{abs(BREAK_SIZE) / (TRUE_TREND_PER_MONTH * 12):.1f} years of trend")
    print(f"  a SECOND series carries a {SPIKE_LEN}-month contamination episode of "
          f"{SPIKE_SIZE:+.3f}")
    print(f"  starting at month {SPIKE_AT} instead of a step: a short-lived artefact")
    print(f"  affecting {SPIKE_LEN}/{N} = {SPIKE_LEN / N:.1%} of the observations")

    section("6. Theil-Sen against least squares: a step and a spike")
    y_spike = make_series(np.random.default_rng(3), with_break=False, spike=True)
    print("   series          true slope   Theil-Sen   OLS        TS error    OLS error")
    for name, series in (("clean", make_series(np.random.default_rng(7),
                                               with_break=False)),
                         ("6-month spike", y_spike),
                         ("step at month 60", y)):
        ts = theil_sen(series)
        ols = float(np.polyfit(t, series, 1)[0])
        print(f"  {name:16s} {TRUE_TREND_PER_MONTH:+.6f}   {ts:+.6f}  {ols:+.6f}  "
              f"{ts - TRUE_TREND_PER_MONTH:+.6f}   {ols - TRUE_TREND_PER_MONTH:+.6f}")
    print("  A 6-month spike affects only the pairs that straddle it -- about")
    print(f"  {SPIKE_LEN * (N - SPIKE_LEN) / (N * (N - 1) / 2):.1%} of all pairs -- so the "
          "MEDIAN of pairwise slopes")
    print("  barely moves, while the least-squares fit is tilted by the whole episode.")
    print("  A step at the midpoint affects HALF the pairs, which is beyond the")
    print("  breakdown point of the median: Theil-Sen fails too.  The correct")
    print("  treatment of a level shift is a breakpoint model, not a robust estimator.")
    print("  Robustness has a quantified limit, and it is worth knowing where it is.")

    section("7. Mann-Kendall and its false-positive rate")
    s_mk, z_mk, var_mk = mann_kendall(y)
    print(f"  Mann-Kendall on the RAW series: S = {s_mk}, var(S) = {var_mk:.1f}, "
          f"z = {z_mk:+.3f}")
    s_ds, z_ds, var_ds = mann_kendall(deseasonalise(y))
    print(f"  after removing the 12-month climatology: S = {s_ds}, z = {z_ds:+.3f}")
    print("  (|z| > 1.96 would be significance at the 5% level, two-sided)")
    n_rep = 4000
    cases = {"white noise, no drift": [], "white noise + 0.02%/month drift": [],
             "white noise + AR(1) rho=0.6": [],
             "seasonal cycle left in the raw series": []}
    tt = np.arange(N)
    for i in range(n_rep):
        rw = np.random.default_rng(1000 + i)
        base = NOISE_SD * rw.standard_normal(N)
        cases["white noise, no drift"].append(mann_kendall(base)[1])
        cases["white noise + 0.02%/month drift"].append(
            mann_kendall(base + 2.0e-4 * tt)[1])
        cases["white noise + AR(1) rho=0.6"].append(
            mann_kendall(NOISE_SD * ar1(N, 0.6, np.random.default_rng(9000 + i)))[1])
        cases["seasonal cycle left in the raw series"].append(
            mann_kendall(base + SEASONAL_AMP * np.sin(2 * np.pi * tt / 12.0))[1])
    print(f"\n  {n_rep} TREND-FREE simulations (no trend in any case):")
    print("   case                                    fraction |z|>1.96   mean z")
    for name, arr in cases.items():
        a = np.array(arr)
        print(f"  {name:38s} {np.mean(np.abs(a) > 1.96):18.4f}   {a.mean():+7.3f}")
    rate_drift = float(np.mean(np.abs(np.array(cases["white noise + 0.02%/month drift"])) > 1.96))
    rate_ar = float(np.mean(np.abs(np.array(cases["white noise + AR(1) rho=0.6"])) > 1.96))
    rate_seas = float(np.mean(np.abs(np.array(cases["seasonal cycle left in the raw series"])) > 1.96))
    print("  FOUR DIFFERENT FAILURE MODES.  (i) On plain white noise the test is")
    print("  calibrated: about 5% rejection, which validates the implementation.")
    print(f"  (ii) An uncorrected gain drift is rejected with probability {rate_drift:.4f}: an")
    print("  instrument property becomes an environmental trend.")
    print(f"  (iii) Autocorrelated noise inflates the rate {rate_ar / 0.05:.1f}x, because the")
    print("  effective number of independent observations is smaller than N.")
    print(f"  (iv) A constant-amplitude seasonal cycle makes the test CONSERVATIVE")
    print(f"  ({rate_seas:.4f} rejection), because the cycle inflates the true variance of")
    print("  S while var(S) does not know about it.  Reporting an uncorrected")
    print("  p-value therefore errs in BOTH directions depending on which")
    print("  assumption is violated -- there is no safe default.")

    n_tests = 1000
    print(f"\n  with {n_tests} independent per-pixel tests at the 5% level the expected")
    print(f"  number of false positives is {n_tests * 0.05:.0f}, and at least one occurs with")
    print(f"  probability {1 - 0.95 ** n_tests:.6f}.  Multiple testing must be controlled")
    print("  (Bonferroni, false-discovery rate) or the change map is a map of noise.")

    section("8. A spurious trend from an uncorrected radiometric drift")
    drift = 2.0e-4          # relative gain change per month
    print(f"  suppose the sensor gain drifts by {drift:.1e} per month (0.2% per year)")
    print("  and the reflectances are used WITHOUT normalisation:")
    z_series = make_series(np.random.default_rng(11), with_break=False)
    induced = z_series * (1.0 + drift * t) - z_series
    slope_induced = float(np.polyfit(t, induced, 1)[0])
    print(f"  induced linear component slope = {slope_induced:+.6f} per month")
    print(f"  true trend = {TRUE_TREND_PER_MONTH:+.6f}; the artefact is "
          f"{abs(slope_induced) / TRUE_TREND_PER_MONTH:.2f}x the signal")
    print(f"  over {N} months the artefact is {slope_induced * N:+.4f} index units,")
    print(f"  against a true change of {TRUE_TREND_PER_MONTH * N:+.4f}.")
    print("  A gain drift is fully correctable from pseudo-invariant targets; leaving")
    print("  it uncorrected converts an instrument property into an environmental")
    print("  trend.  THIS is why change detection starts with normalisation.")

    section("9. Verification: Theil-Sen on noise-free linear data")
    t2 = np.arange(50)
    for slope in (0.0, 0.01, -0.02):
        y2 = 3.0 + slope * t2
        ts = theil_sen(y2)
        ols = float(np.polyfit(t2, y2, 1)[0])
        print(f"  true slope {slope:+.3f}: Theil-Sen {ts:+.6f}, OLS {ols:+.6f}, "
              f"|error| {abs(ts - slope):.2e}")
    print("  Both estimators are exact on noise-free linear data, which validates the")
    print("  implementations; it says nothing about robustness, which section 6 tests.")


if __name__ == "__main__":
    main()
