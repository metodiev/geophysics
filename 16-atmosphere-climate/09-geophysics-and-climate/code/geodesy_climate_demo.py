#!/usr/bin/env python3
"""Geodesy for climate: closing a sea-level budget from synthetic components,
the bias a tide gauge acquires from uncorrected vertical land motion, the
uncertainty a GIA correction contributes, and how long a record needs to be
before a trend is detectable.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geodesy_climate_demo.py

Everything is SYNTHETIC.  The component trends, the vertical land motion and the
noise are chosen teaching values expressed in mm/yr.  No real tide gauge,
satellite mission, gravity solution, GIA model or published rate is used.

Contents
--------
1. A synthetic sea-level budget: total, mass and steric components, and closure.
2. The tide gauge and vertical land motion: why relative sea level is not
   sea level.
3. A GIA correction: its size, and the uncertainty it injects into the budget.
4. Trend detection time as a function of the noise and the trend.
5. What is measured, what is corrected, what is assumed.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC budget (chosen, not measured) --------------------------------
N_YEARS = 30
TOTAL_TREND = 3.30       # mm/yr, synthetic "total" sea-level change
MASS_TREND = 1.90        # mm/yr, synthetic mass component (ice + land water)
STERIC_TREND = 1.30      # mm/yr, synthetic steric component
NOISE_SD = 25.0          # mm, synthetic annual noise on each component
PHI = 0.7                # lag-1 autocorrelation of the component noise
VLM_TRUE = -1.50         # mm/yr, synthetic vertical land motion (subsidence)
VLM_ASSUMED = 0.00       # mm/yr, what the analyst initially assumes
GIA_CORRECTION = 0.60    # mm/yr, synthetic GIA correction applied to mass
GIA_UNCERTAINTY = 0.25   # mm/yr, its assumed uncertainty


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def ar1_noise(n, sd=NOISE_SD, phi=PHI):
    e = np.zeros(n)
    for t in range(1, n):
        e[t] = phi * e[t - 1] + np.sqrt(1 - phi ** 2) * sd * \
            RNG.standard_normal()
    return e


def ols_trend(x):
    n = x.size
    t = np.arange(n, dtype=float)
    tb = t.mean()
    sxx = np.sum((t - tb) ** 2)
    slope = np.sum((t - tb) * x) / sxx
    resid = x - (x.mean() + slope * (t - tb))
    s2 = np.sum(resid ** 2) / (n - 2)
    return slope, np.sqrt(s2 / sxx)


def main():
    section("1. A synthetic sea-level budget")
    years = np.arange(N_YEARS)
    total = TOTAL_TREND * years + ar1_noise(N_YEARS)
    mass = MASS_TREND * years + ar1_noise(N_YEARS)
    steric = STERIC_TREND * years + ar1_noise(N_YEARS)
    t_tot, se_tot = ols_trend(total)
    t_mass, se_mass = ols_trend(mass)
    t_ster, se_ster = ols_trend(steric)
    print(f"  SYNTHETIC truth: total {TOTAL_TREND:.2f}, mass {MASS_TREND:.2f},")
    print(f"  steric {STERIC_TREND:.2f} mm/yr over {N_YEARS} years")
    print(f"  annual noise sd {NOISE_SD:.1f} mm, AR(1) phi {PHI:.2f}")
    print("  component        fitted trend (mm/yr)   standard error")
    for name, est, se in (("total", t_tot, se_tot), ("mass", t_mass, se_mass),
                          ("steric", t_ster, se_ster)):
        print(f"  {name:15s}   {est:19.3f}   {se:14.3f}")
    residual = t_tot - t_mass - t_ster
    res_sd = np.sqrt(se_tot ** 2 + se_mass ** 2 + se_ster ** 2)
    print(f"  closure residual (total - mass - steric) = {residual:+.3f} mm/yr")
    print(f"  its 1-sigma from the three standard errors = {res_sd:.3f} mm/yr")
    print(f"  residual / sigma = {residual / res_sd:+.2f}")
    print("  A budget closes when the residual is small relative to its stated")
    print("  uncertainty -- not when it is exactly zero.  The residual here is")
    print("  consistent with a closed budget and is also consistent with a")
    print("  systematic term of a few tenths of a mm/yr.")

    section("2. Tide gauges measure relative sea level")
    tide_true = TOTAL_TREND * years + ar1_noise(N_YEARS)
    # relative sea level = absolute sea level - vertical land motion effect
    tide_measured = tide_true - VLM_TRUE * years  # VLM negative -> land sinks
    t_abs, se_abs = ols_trend(tide_true)
    t_rel, se_rel = ols_trend(tide_measured)
    print(f"  SYNTHETIC vertical land motion at the site: {VLM_TRUE:+.2f} mm/yr")
    print(f"  (negative = the land is sinking, so the gauge sees more rise)")
    print(f"  absolute (satellite-like) trend : {t_abs:+.3f} +/- {se_abs:.3f} mm/yr")
    print(f"  relative (tide-gauge) trend     : {t_rel:+.3f} +/- {se_rel:.3f} mm/yr")
    print(f"  difference                      : "
          f"{t_rel - t_abs:+.3f} mm/yr")
    print(f"  error if the land motion is assumed to be {VLM_ASSUMED:+.2f} mm/yr:")
    print(f"    the gauge trend is wrong by {-VLM_TRUE:+.2f} mm/yr, which is")
    print(f"    {100 * abs(VLM_TRUE) / t_abs:.0f}% of the absolute trend")
    print("  A few mm/yr of land motion is larger than the sea-level signal;")
    print("  the vertical velocity must be measured, not assumed.")

    section("3. A GIA correction and its uncertainty")
    print(f"  SYNTHETIC live GIA correction applied to the mass component: "
          f"{GIA_CORRECTION:+.2f} mm/yr")
    print(f"  assumed uncertainty: {GIA_UNCERTAINTY:.2f} mm/yr")
    mass_corr = MASS_TREND + GIA_CORRECTION
    t_corr, se_corr = ols_trend(mass_corr * years + ar1_noise(N_YEARS))
    print(f"  mass trend before correction : {t_mass:+.3f} "
          f"+/- {se_mass:.3f} mm/yr")
    print(f"  mass trend after correction  : {t_corr:+.3f} "
          f"+/- {se_corr:.3f} mm/yr")
    budget_sd = np.sqrt(se_tot ** 2 + se_corr ** 2 + GIA_UNCERTAINTY ** 2
                        + se_ster ** 2)
    print(f"  budget residual uncertainty including the GIA term: "
          f"{budget_sd:.3f} mm/yr")
    print(f"  the GIA uncertainty alone is {GIA_UNCERTAINTY:.2f} mm/yr "
          f"({100 * GIA_UNCERTAINTY ** 2 / budget_sd ** 2:.0f}% of the variance)")
    print("  A correction is not a measurement: it moves the answer by its size")
    print("  and widens the uncertainty by at least its assumed error.")

    section("4. How long until a trend is detectable?")
    print("  detection criterion: |trend| > 2 x its standard error")
    print("   n (yr)   mean se(trend) mm/yr   truth/se   detectable at 2 sigma?")
    for n in (10, 15, 20, 25, 30, 40, 50, 60):
        ses = []
        for _ in range(200):
            x = TOTAL_TREND * np.arange(n) + ar1_noise(n)
            ses.append(ols_trend(x)[1])
        se = float(np.mean(ses))
        print(f"  {n:7d}   {se:20.3f}   {TOTAL_TREND / se:9.2f}   "
              f"{'yes' if TOTAL_TREND / se > 2 else 'no':>10s}")
    print(f"  SYNTHETIC trend {TOTAL_TREND:.2f} mm/yr with an annual noise sd of")
    print(f"  {NOISE_SD:.1f} mm and AR(1) phi {PHI:.2f} (persistent, as sea-level")
    print("  variability is).  A ten-year record gives a trend only 1.9 times its")
    print("  own standard error and does not establish anything; by 15 years the")
    print("  ratio exceeds 3.  The standard error itself falls roughly as")
    print("  n^(-3/2) for a trend, much faster than the 1/sqrt(n) of a mean,")
    print("  which is why lengthening a record buys trend precision so quickly")
    print("  -- and why a decade is not a climate record for this variable when")
    print("  the interannual variability is tens of millimetres.")

    section("5. Measured, corrected, assumed")
    print("  measured : water level at a gauge; sea-surface height from")
    print("             altimetry; gravity change from repeat or satellite")
    print("             gravimetry; position from GNSS; ocean temperature and")
    print("             salinity for the steric term.")
    print("  corrected: GIA for the mass term; land motion for the gauge;")
    print("             reference-frame and geocentre conventions for altimetry.")
    print("  assumed  : the error budget of every correction, and the")
    print("             separability of the mass and steric terms.")
    print("  A budget that reports only the measured terms has not reported the")
    print("  uncertainties that dominate it.  All numbers above are SYNTHETIC.")


if __name__ == "__main__":
    main()
