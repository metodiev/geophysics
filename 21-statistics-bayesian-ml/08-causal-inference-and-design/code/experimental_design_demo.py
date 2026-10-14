#!/usr/bin/env python3
"""Experimental design: sampling geometry, precision and aliasing.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python experimental_design_demo.py

Everything here is SYNTHETIC.  The measurement model, the noise, the trend and the
seasonal cycle are chosen by the code below; no monument, network or published
rate is used.

Sections
--------
1. The measurement model and the estimator of a linear trend.
2. Four sampling designs: precision, efficiency and the sample size for power.
3. Sampling interval and aliasing of a seasonal cycle.
4. What the design changes and what the estimator does not.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

SIGMA_MM = 5.0        # measurement scatter, mm (1 s.d.)
TREND_MM_YR = 1.0     # true linear rate, mm/yr
SEASON_A_MM = 3.0     # seasonal amplitude, mm
SEASON_PERIOD_M = 12.0
YEARS = 5.0
MONTHS = int(YEARS * 12)
Z_ALPHA = 1.959964    # two-sided 5%
Z_POWER = 0.841621    # 80% power
N_POINTS = 24         # points per campaign design


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def slope_se(t_years, sigma=SIGMA_MM):
    """Standard error of a fitted slope for a given sampling geometry."""
    t = np.asarray(t_years, dtype=float)
    return sigma / np.sqrt(np.sum((t - t.mean()) ** 2))


def n_for_power(sd_t_years, sigma=SIGMA_MM, trend=TREND_MM_YR):
    """Points needed for 80% power at 5% two-sided to detect `trend`."""
    se_target = trend / (Z_ALPHA + Z_POWER)
    return (sigma / (se_target * sd_t_years)) ** 2


def main():
    section("1. The measurement model and the estimator of a linear trend")
    print(f"SYNTHETIC measurement model: y(t) = {TREND_MM_YR:.1f} t + "
          f"seasonal + noise, t in years")
    print(f"  measurement scatter {SIGMA_MM:.1f} mm (1 s.d.); seasonal "
          f"amplitude {SEASON_A_MM:.1f} mm, period {SEASON_PERIOD_M:.0f} months")
    print(f"  detection target: 80% power at the two-sided 5% level for a true "
          f"rate of {TREND_MM_YR:.1f} mm/yr")
    print(f"  the slope's standard error is sigma / sqrt(sum (t - t_bar)^2):")
    print("  the design enters only through the spread of the sampling times")

    section("2. Four sampling designs")
    designs = {}
    month_index = np.arange(MONTHS)
    designs["even, 24 monthly points"] = np.linspace(0, MONTHS - 1, N_POINTS) / 12.0
    designs["first year only, 24 points"] = np.linspace(0, 11, N_POINTS) / 12.0
    designs["two campaigns, 12 at each end"] = np.concatenate([
        np.linspace(0, 0.5, 12), np.linspace(YEARS - 0.5, YEARS, 12)])
    designs["three campaigns of 8 months"] = np.concatenate([
        np.linspace(0.0, 7.0 / 12, 8), np.linspace(2.0, 2.0 + 7.0 / 12, 8),
        np.linspace(4.0, 4.0 + 7.0 / 12, 8)])
    del month_index

    print(f"  {'design':<34s} {'sd(t) (yr)':>11s} {'SE(slope)':>11s} "
          f"{'n for power':>12s} {'eff.':>6s}")
    best = None
    rows = []
    for name, t in designs.items():
        se = slope_se(t)
        sd_t = float(np.std(t))
        n = n_for_power(sd_t)
        rows.append((name, sd_t, se, n))
        if best is None or se < best[1]:
            best = (name, se)
    for name, sd_t, se, n in rows:
        print(f"  {name:<34s} {sd_t:>11.3f} {se:>8.3f} mm/yr {n:>11.1f} "
              f"{best[1] / se:>6.2f}")
    print("  'eff.' is the precision relative to the best design; a value "
          "below 1")
    print("  means the design wastes observations, and the cost is quadratic in "
          "it")
    print("  the design that puts half its points at each end of the interval "
          "wins,")
    print("  because the slope's standard error depends on the spread of t and "
          "not")
    print("  on the number of distinct times")

    section("3. Sampling interval and aliasing of a seasonal cycle")
    months = np.arange(MONTHS)
    t_monthly = months / 12.0
    phase = 0.7
    season = SEASON_A_MM * np.sin(2.0 * np.pi * months / SEASON_PERIOD_M + phase)
    y_monthly = (TREND_MM_YR * t_monthly + season
                 + SIGMA_MM * RNG.standard_normal(MONTHS))          # mm
    design_matrix = np.column_stack([
        np.ones(MONTHS), t_monthly,
        np.sin(2.0 * np.pi * months / 12.0),
        np.cos(2.0 * np.pi * months / 12.0)])
    coef, *_ = np.linalg.lstsq(design_matrix, y_monthly, rcond=None)
    residual = y_monthly - design_matrix @ coef
    s_resid = float(np.sqrt(np.sum(residual ** 2) / (MONTHS - 4)))
    amplitude = float(np.hypot(coef[2], coef[3]))
    amplitude_se = s_resid * np.sqrt(2.0 / MONTHS)
    se_monthly = s_resid / np.sqrt(np.sum((t_monthly - t_monthly.mean()) ** 2))
    print("  monthly sampling, 60 epochs, seasonal term fitted explicitly:")
    print(f"    recovered seasonal amplitude = {amplitude:.3f} +/- "
          f"{amplitude_se:.3f} mm (generator {SEASON_A_MM:.1f} mm)")
    print(f"    recovered trend = {coef[1]:+.3f} +/- {se_monthly:.3f} mm/yr "
          f"(generator {TREND_MM_YR:.1f} mm/yr)")

    t_annual = np.arange(0.0, YEARS, 1.0)
    season_annual = SEASON_A_MM * np.sin(2.0 * np.pi * t_annual + phase)
    y_annual = (TREND_MM_YR * t_annual + season_annual
                + SIGMA_MM * RNG.standard_normal(t_annual.size))
    annual_matrix = np.column_stack([np.ones(t_annual.size), t_annual])
    coef_a, *_ = np.linalg.lstsq(annual_matrix, y_annual, rcond=None)
    se_annual = slope_se(t_annual)
    print("  annual sampling, 5 epochs, one point per seasonal cycle:")
    print(f"    the seasonal phase is identical at every epoch, so the seasonal "
          f"term is")
    print(f"    aliased: it appears as the constant "
          f"{SEASON_A_MM * np.sin(phase):+.3f} mm in the intercept "
          f"({coef_a[0]:+.3f} mm fitted)")
    print(f"    recovered trend = {coef_a[1]:+.3f} +/- {se_annual:.3f} mm/yr ")
    print(f"    a constant aliased term does NOT bias the slope: the fitted "
          f"value is")
    print(f"    within {abs(coef_a[1] - TREND_MM_YR) / se_annual:.2f} standard "
          f"errors of the truth")
    print("  what aliasing costs here is precision and interpretability: the "
          "slope's")
    print(f"  standard error rises from {se_monthly:.3f} to {se_annual:.3f} "
          f"mm/yr, a factor of")
    print(f"  {se_annual / se_monthly:.2f}, because the 3 mm of seasonal signal "
          f"that the monthly")
    print("  design removes has become part of the scatter; and no seasonal "
          "claim is")
    print("  possible at all. With a drifting seasonal phase the aliased term "
          "is no")
    print("  longer constant and the slope is biased directly")

    section("4. What the design changes and what the estimator does not")
    print(f"  design efficiency across the four geometries: "
          f"{best[1] / max(r[2] for r in rows):.2f} to 1.00 in SE(slope),")
    print(f"  i.e. a factor of "
          f"{(max(r[2] for r in rows) / best[1]) ** 2:.0f} in the number of")
    print("  observations needed at the same precision")
    print(f"  the required count for 80% power ranges from "
          f"{min(r[3] for r in rows):.0f} to {max(r[3] for r in rows):.0f} points")
    print("  for the same estimator and the same noise: the design is not a")
    print("  detail of the analysis, it is the dominant term")
    print("\nSYNTHETIC: the scatter, the trend and the seasonal amplitude are")
    print("chosen teaching values. A real campaign must also state the monument")
    print("stability, the multipath environment and the reference frame.")


if __name__ == "__main__":
    main()
