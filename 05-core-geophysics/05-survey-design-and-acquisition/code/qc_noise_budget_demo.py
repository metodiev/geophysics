#!/usr/bin/env python3
"""Acquisition QC: noise budget, repeatability, drift and the cost of averaging.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python qc_noise_budget_demo.py

All instrument and environment numbers are SYNTHETIC; the point is to show HOW a
noise budget is assembled and checked, not to quote a particular instrument.

Contents
--------
1. A noise budget: independent contributions combined in quadrature, with the
   dominant term identified.
2. Repeatability measured from repeated occupations of one station, with a linear
   drift, before and after drift correction by base-station ties.
3. Drift estimation from loop closures: the measured residual after correction.
4. What averaging buys: measured standard error versus 1/sqrt(N).
"""

import numpy as np

RNG_SEED = 20261014


def main() -> None:
    rng = np.random.default_rng(RNG_SEED)

    # --- 1. Noise budget ----------------------------------------------------
    print("1. Noise budget (all values SYNTHETIC, in mGal)")
    budget = [
        ("instrument resolution / repeatability", 0.010),
        ("vertical positioning (DGPS, 0.5 m via free-air)", 0.154),
        ("terrain / near-surface correction residual", 0.050),
        ("tidal and earth-tide correction residual", 0.015),
        ("drift residual after ties", 0.020),
        ("reading noise and coupling scatter", 0.005),
    ]
    total = float(np.sqrt(sum(v ** 2 for _, v in budget)))
    for name, v in budget:
        print(f"   {name:<46}{v:>8.4f}  ({v**2/total**2*100:5.1f} % of variance)")
    print(f"   {'TOTAL (quadrature)':<46}{total:>8.4f}")
    dominant = max(budget, key=lambda kv: kv[1])
    print(f"   dominant term: {dominant[0]}  -> {dominant[1]:.3f} mGal")
    print("   -> improving anything else while leaving this term unchanged buys")
    print("      almost nothing; a budget exists to find the binding constraint.")

    # --- 2. Repeatability with drift ---------------------------------------
    print("\n2. Repeatability of a repeated station occupation")
    n_repeat = 12
    true_value = 979_812.40          # mGal, SYNTHETIC absolute reading
    drift_rate = 0.030               # mGal per minute, SYNTHETIC linear drift
    interval_min = 4.0               # min between repeats, SYNTHETIC
    t = np.arange(n_repeat) * interval_min
    drift = drift_rate * t
    scatter = rng.normal(0.0, 0.010, size=n_repeat)
    readings = true_value + drift + scatter
    print(f"   repeated occupations                  = {n_repeat}")
    print(f"   interval between repeats              = {interval_min:.1f} min")
    print(f"   synthetic linear drift rate           = {drift_rate:.4f} mGal/min")
    print(f"   std of raw repeated readings          = {readings.std(ddof=1):.5f} mGal")
    # Least-squares straight-line fit for the drift, then remove it.
    slope, intercept = np.polyfit(t, readings, 1)
    corrected = readings - (slope * t + intercept - slope * t.mean() - intercept)
    print(f"   estimated drift rate from the data    = {slope:.5f} mGal/min")
    print(f"   std after removing the fitted drift   = {corrected.std(ddof=1):.5f} mGal")
    print(f"   ratio raw/corrected                   = "
          f"{readings.std(ddof=1)/corrected.std(ddof=1):.2f}")
    span_min = t[-1] - t[0]
    print(f"   total elapsed span                     = {span_min:.1f} min")
    print("   -> uncorrected drift of "
          f"{drift_rate*span_min:.2f} mGal accumulates across the span, far above")
    print("      the 0.01 mGal reading noise: the drift term, not the instrument,")
    print("      sets the repeatability of an uncorrected occupation.")

    # --- 3. Loop closures ---------------------------------------------------
    print("\n3. Drift from loop closures (base-station ties)")
    n_loops = 8
    loop_minutes = 25.0
    closure = drift_rate * loop_minutes + rng.normal(0.0, 0.010, size=n_loops)
    rate_est = closure / loop_minutes
    print(f"   loops                                = {n_loops}")
    print(f"   loop duration                        = {loop_minutes:.1f} min")
    print(f"   mean closure misclosure              = {closure.mean():.5f} mGal")
    print(f"   std of closure misclosures           = {closure.std(ddof=1):.5f} mGal")
    print(f"   estimated drift rate (mean/loop)     = {rate_est.mean():.5f} mGal/min")
    print(f"   true drift rate                      = {drift_rate:.5f} mGal/min")
    print(f"   error in the estimated rate          = "
          f"{abs(rate_est.mean()-drift_rate):.5f} mGal/min")
    print(f"   residual over a {loop_minutes:.0f} min loop after correction = "
          f"{abs(rate_est.mean()-drift_rate)*loop_minutes:.5f} mGal")
    print("   -> the loop residual scales with LOOP LENGTH, so loop duration is a")
    print("      design decision with a directly computable error consequence.")

    # --- 4. Averaging -------------------------------------------------------
    print("\n4. Cost of averaging: standard error of the mean vs 1/sqrt(N)")
    one = 0.010
    print(f"   {'N':>5}{'measured SEM (mGal)':>22}{'1/sqrt(N) prediction':>23}")
    for n in (1, 4, 16, 64, 256):
        draws = rng.normal(0.0, one, size=(4000, n))
        sem = float(draws.mean(axis=1).std(ddof=1))
        print(f"   {n:>5}{sem:>22.6f}{one / np.sqrt(n):>23.6f}")
    print("   -> quartering the noise takes 16x the acquisition effort.")


if __name__ == "__main__":
    main()
