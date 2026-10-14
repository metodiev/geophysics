#!/usr/bin/env python3
"""Downscaling: a measured comparison of raw coarse output, elevation-based
(lapse-rate) downscaling, statistical downscaling, and a hybrid, together with
the failure of a statistical relationship when the relationship itself changes.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python downscaling_demo.py

All models and data in this file are SYNTHETIC.  The orography is a generated
profile and the temperatures are generated from a chosen lapse rate.  No real
model output or station record is used.

Contents
--------
1. A synthetic fine-grid orography and a fine-grid temperature, plus its
   coarse-grid (grid-box mean) counterpart.
2. Four downscaling methods evaluated by RMSE and bias against the fine truth.
3. The same methods under a changed regime (a different true lapse rate).
4. How much of the fine-scale variance each predictor carries.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N_FINE = 80                 # fine-grid points
BLOCK = 4                   # fine points per coarse grid box
N_COARSE = N_FINE // BLOCK
SURFACE_PRESSURE_T_K = 288.15   # a chosen surface reference, K
LAPSE_K_KM = 6.5               # SYNTHETIC environmental lapse rate, K/km
LAPSE_CHANGED_K_KM = 8.5       # SYNTHETIC changed regime in the test period
NOISE_K = 0.30


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def orography():
    """Synthetic fine-grid orography, km, non-negative."""
    x = np.linspace(0.0, 1.0, N_FINE, endpoint=False)
    h = (0.40 + 0.50 * np.sin(2 * np.pi * 3 * x)
         + 0.30 * np.sin(2 * np.pi * 7 * x + 1.0)
         + 0.15 * np.sin(2 * np.pi * 13 * x + 2.0))
    return np.clip(h, 0.0, None)


def block_mean(fine):
    return fine.reshape(N_COARSE, BLOCK).mean(axis=1)


def block_repeat(coarse):
    return np.repeat(coarse, BLOCK)


def temperature_field(h_fine, lapse):
    """Fine-grid temperature from elevation and a lapse rate, plus noise."""
    return (SURFACE_PRESSURE_T_K - lapse * h_fine
            + NOISE_K * RNG.standard_normal(N_FINE))


def fit_linear(predictors, target, mask):
    """Least-squares fit on the masked samples; return coefficients and a
    full-length prediction from the fitted coefficients."""
    design_full = np.column_stack([np.ones_like(target)] + list(predictors))
    coef, *_ = np.linalg.lstsq(design_full[mask], target[mask], rcond=None)
    return coef, design_full @ coef


def report(name, prediction, truth, mask, out):
    rmse = float(np.sqrt(np.mean((prediction[mask] - truth[mask]) ** 2)))
    bias = float(np.mean(prediction[mask] - truth[mask]))
    out.append((name, rmse, bias))


def main():
    h_fine = orography()
    h_coarse = block_mean(h_fine)
    print(f"  fine grid: {N_FINE} points; coarse grid: {N_COARSE} boxes of "
          f"{BLOCK} fine points")
    print(f"  fine orography range {h_fine.min():.3f} to {h_fine.max():.3f} km; "
          f"coarse range {h_coarse.min():.3f} to {h_coarse.max():.3f} km")
    print(f"  within-box orography range that the coarse grid cannot represent:")
    within = h_fine.reshape(N_COARSE, BLOCK)
    print(f"    mean within-box standard deviation = "
          f"{within.std(axis=1).mean():.3f} km")

    section("1. Stationary regime: true lapse rate "
            f"{LAPSE_K_KM:.1f} K/km")
    t_fine = temperature_field(h_fine, LAPSE_K_KM)
    t_coarse = block_mean(t_fine)
    train = np.zeros(N_FINE, dtype=bool)
    train[:N_FINE // 2] = True
    test = ~train
    print(f"  fine temperature mean {t_fine.mean():.3f} K, "
          f"std {t_fine.std():.3f} K")

    raw = block_repeat(t_coarse)
    lapse_pred = block_repeat(t_coarse) + LAPSE_K_KM * (
        block_repeat(h_coarse) - h_fine)

    coef_stat, stat_pred = fit_linear([block_repeat(t_coarse)], t_fine, train)

    coef_hyb, hybrid_fitted = fit_linear(
        [block_repeat(t_coarse), h_fine], t_fine, train)

    out = []
    report("raw coarse", raw, t_fine, test, out)
    report("lapse-rate", lapse_pred, t_fine, test, out)
    report("statistical (T only)", stat_pred, t_fine, test, out)
    report("statistical (T + orog)", hybrid_fitted, t_fine, test, out)
    print(f"  {'method':<24s} {'RMSE (K)':>9s} {'bias (K)':>9s}")
    for name, rmse, bias in out:
        print(f"  {name:<24s} {rmse:9.3f} {bias:9.3f}")
    print("  statistical (T only) cannot resolve structure inside a coarse box,")
    print("  because its only predictor is constant there: it can correct a mean")
    print("  bias but not add within-box detail.  Deterministic orography, which")
    print("  is known at fine scale, can.")
    print(f"  fitted statistical coefficients (T only): intercept "
          f"{coef_stat[0]:.3f} K, slope {coef_stat[1]:.4f}")
    print(f"  fitted hybrid coefficients: intercept {coef_hyb[0]:.3f} K, "
          f"slope(T) {coef_hyb[1]:.4f}, slope(orography) {coef_hyb[2]:.3f} K/km")
    print(f"  (the true lapse rate is {-LAPSE_K_KM:.3f} K/km; the fitted "
          f"orography coefficient recovers it to "
          f"{abs(coef_hyb[2] + LAPSE_K_KM):.3f} K/km)")

    section("2. Changed regime: true lapse rate becomes "
            f"{LAPSE_CHANGED_K_KM:.1f} K/km in the test period")
    t_fine_new = temperature_field(h_fine, LAPSE_CHANGED_K_KM)
    # The coarse model sees the new regime; the statistical fit is frozen.
    t_coarse_new = block_mean(t_fine_new)
    raw_new = block_repeat(t_coarse_new)
    lapse_new = block_repeat(t_coarse_new) + LAPSE_K_KM * (
        block_repeat(h_coarse) - h_fine)
    stat_new = coef_stat[0] + coef_stat[1] * block_repeat(t_coarse_new)
    hybrid_new = coef_hyb[0] + coef_hyb[1] * block_repeat(t_coarse_new) + coef_hyb[2] * h_fine
    out_new = []
    report("raw coarse", raw_new, t_fine_new, test, out_new)
    report("lapse-rate (old gamma)", lapse_new, t_fine_new, test, out_new)
    report("statistical (T only)", stat_new, t_fine_new, test, out_new)
    report("statistical (T + orog)", hybrid_new, t_fine_new, test, out_new)
    print(f"  {'method':<24s} {'RMSE (K)':>9s} {'bias (K)':>9s}")
    for name, rmse, bias in out_new:
        print(f"  {name:<24s} {rmse:9.3f} {bias:9.3f}")
    print("  The statistical model is frozen at the old relationship and now has a")
    print("  systematic error; the lapse method is frozen at the old lapse rate and")
    print("  also degrades. A statistically downscaled product implicitly assumes the")
    print("  training relationship holds in the target period. When it does not, the")
    print("  error is a bias, which is the dangerous kind because it does not look")
    print("  like noise.")

    section("3. How much fine-scale variance each predictor carries")
    var_total = float(np.var(t_fine, ddof=1))
    residual_raw = t_fine - raw
    residual_lapse = t_fine - lapse_pred
    print(f"  total fine-scale variance              : {var_total:8.4f} K^2")
    print(f"  variance left by raw coarse output     : "
          f"{np.var(residual_raw, ddof=1):8.4f} K^2")
    print(f"  variance left after lapse correction   : "
          f"{np.var(residual_lapse, ddof=1):8.4f} K^2")
    print(f"  fraction of variance removed by lapse  : "
          f"{1.0 - np.var(residual_lapse, ddof=1) / np.var(residual_raw, ddof=1):8.4f}")
    print("  Lapse correction removes the part of the fine-scale variance correlated")
    print("  with fine orography. What remains is noise: statistically downscaling")
    print("  cannot create information that no predictor contains.")


if __name__ == "__main__":
    main()
