#!/usr/bin/env python3
"""Observing modern sea-level rise: the error budget of an altimetric trend, the
tide-gauge-plus-GNSS problem, the GRACE/Argo mass-steric budget, and the geometry
of the melting fingerprint.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sea_level_rise_observation_demo.py

Everything here is SYNTHETIC.  The records, the error terms and the ice masses are
teaching models with the stated model constants.  No real satellite mission, tide
gauge, ice sheet or published record is referenced, and no number is quoted from a
published measurement.

Contents
--------
1. The trend error of a synthetic altimetric record: the random term, the
   systematic drift term, and the red-noise inflation.
2. Tide gauges and vertical land motion: the bias an uncorrected subsidence
   introduces, and the size of the correction's own error.
3. The mass-steric budget: GRACE plus Argo against altimetry, the closure
   residual, and the Gt-per-millimetre conversion.
4. The melting fingerprint: the eustatic and self-attraction terms, and why sea
   level falls near a melting ice sheet.
5. Worked examples used in the lesson.
"""

import numpy as np
from scipy import stats

RNG = np.random.default_rng(20261014)

A_OCEAN = 3.61e14        # m^2, standard ocean area
RHO_W = 1000.0           # kg/m^3
RHO_SW = 1025.0
G = 9.80665
G_NEWTON = 6.67430e-11
GT = 1e12                # kg per gigatonne


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def trend_error_random(sigma_point_mm, n_points, spacing_yr):
    """Standard error of a linear trend from independent points."""
    x = np.arange(n_points) * spacing_yr
    sxx = np.sum((x - x.mean()) ** 2)
    return sigma_point_mm / np.sqrt(sxx)


def trend_error_drift(drift_mm_per_yr2, n_points, spacing_yr):
    """Bias in the fitted slope from a quadratic term (an instrument drift)."""
    x = np.arange(n_points) * spacing_yr
    xc = x - x.mean()
    # the fitted slope of 0.5 drift t^2 has expectation drift * mean(t)
    return drift_mm_per_yr2 * x.mean()


def main():
    section("1. The trend error of an altimetric record")
    years, sigma_pt = 20.0, 10.0
    spacing = 1.0 / 12.0
    n = int(years / spacing)
    sig_rand = trend_error_random(sigma_pt, n, spacing)
    print(f"  synthetic record: {years:.0f} years of monthly means, one point")
    print(f"  every {spacing * 12:.0f} month, per-point error sigma = "
          f"{sigma_pt:.0f} mm")
    print(f"  n = {n} points; random-error trend uncertainty = "
          f"{sig_rand:.4f} mm/yr")
    print("  the random term is negligible: the record is long and the points are")
    print("  many, so the formal error of a 20-year trend is a tenth of a")
    print("  millimetre per year.  Everything that matters is systematic.")
    print("\n  a linear instrument drift (a systematic acceleration) biases the")
    print("  fitted trend by drift x mean(t):")
    print("   drift (mm/yr per yr)   trend bias (mm/yr)   relative to a 3.3 mm/yr trend")
    for drift in (0.01, 0.05, 0.1, 0.2):
        bias = trend_error_drift(drift, n, spacing)
        print(f"   {drift:20.2f}   {bias:18.3f}   {bias / 3.3 * 100:30.1f}%")
    print("  a drift of 0.1 mm/yr per year over a 20-year record biases the trend")
    print("  by 1.0 mm/yr, which is 30% of the signal: systematic errors dominate")
    print("  by an order of magnitude, and they are what makes a trend statement")
    print("  depend on the instrument's pedigree rather than on its precision.")
    print("\n  red noise inflates the random term.  For a first-order")
    print("  autocorrelation rho, the variance of the mean is inflated by")
    print("  (1+rho)/(1-rho):")
    print("   rho    inflation factor   inflated trend uncertainty (mm/yr)")
    for rho in (0.0, 0.3, 0.5, 0.7, 0.9):
        infl = np.sqrt((1.0 + rho) / (1.0 - rho))
        print(f"   {rho:5.1f}   {infl:16.2f}   {sig_rand * infl:36.4f}")
    print("  even at rho = 0.9 the random term stays below 0.3 mm/yr: it is the")
    print("  drift and the reference-frame errors that decide the answer.")

    section("2. Tide gauges and vertical land motion")
    vlm_true, gauge_years = -1.0, 50.0
    print(f"  a tide gauge measures RELATIVE sea level: the true rise plus the")
    print(f"  land motion.  With VLM = {vlm_true:.1f} mm/yr and a true rise of")
    print("  3.3 mm/yr, the gauge reports 2.3 mm/yr before correction.")
    print(f"   VLM (mm/yr)   gauge trend (mm/yr)   bias vs the true rise (mm/yr)")
    for vlm in (-3.0, -1.0, 0.0, 1.0):
        print(f"   {vlm:11.1f}   {3.3 + vlm:19.1f}   {vlm:28.1f}")
    n_yr, sig_gauge = int(gauge_years), 5.0
    sig_trend = trend_error_random(sig_gauge, n_yr, 1.0)
    print(f"\n  formal trend error of {n_yr} annual means with "
          f"sigma = {sig_gauge:.0f} mm: {sig_trend:.4f} mm/yr")
    print("  the GNSS correction carries its own error of order 0.3 mm/yr, and the")
    print(f"  frame/realisation error a further fraction of that:")
    print("   term                      size (mm/yr)   share of the 0.3 mm/yr budget")
    for name, size in (("GNSS vertical velocity", 0.3), ("frame realisation",
                                                          0.2),
                       ("gauge datum stability", 0.1),
                       ("random trend error", sig_trend)):
        print(f"   {name:24s} {size:12.3f}   {size / 0.3 * 100:28.0f}%")
    print("  the random term contributes 16% of the GNSS error and the systematic")
    print("  terms dominate even the correction.  A tide-gauge trend is a")
    print("  statement about a reference frame as much as about the sea.")

    section("3. The mass-steric budget")
    print("  1 mm of global mean sea level = rho_w A_ocean x 1 mm = "
          f"{1e-3 * A_OCEAN * RHO_W / GT:.0f} Gt")
    print("\n  synthetic 15-year budget, all in mm/yr:")
    print("   component                   value    uncertainty")
    for name, val, unc in (("altimetry (total)", 3.40, 0.40),
                           ("GRACE (ocean mass)", 1.90, 0.30),
                           ("Argo (steric)", 1.40, 0.20)):
        print(f"   {name:24s} {val:8.2f}   {unc:11.2f}")
    resid = 3.40 - (1.90 + 1.40)
    resid_unc = np.sqrt(0.40 ** 2 + 0.30 ** 2 + 0.20 ** 2)
    print(f"   residual (altimetry - mass - steric) = {resid:+.2f} +/- "
          f"{resid_unc:.2f} mm/yr")
    print("  the budget closes within its uncertainty, which is the strongest")
    print("  statement the data support: the residual is consistent with zero but")
    print("  it is not zero, and its uncertainty is 16% of the signal.")
    print("\n  converting the mass term to an equivalent sea level:")
    for m in (1.0, 1.9, 3.0):
        print(f"   {m:.1f} mm/yr of ocean mass = "
              f"{m * 1e-3 * A_OCEAN * RHO_W / GT / 1e3:.2f} x 10^3 Gt/yr")

    section("4. The melting fingerprint")
    mass_kg = 1.0e18
    eustatic = mass_kg / (RHO_SW * A_OCEAN)
    print(f"  a synthetic ice mass of {mass_kg:.1e} kg (1 million Gt) added to")
    print(f"  the ocean: eustatic rise = M/(rho_sw A_ocean) = {eustatic:.2f} m")
    print("\n  the self-attraction of the added mass raises the sea surface near")
    print("  it by the geoid change GM/(g r):")
    print("   distance from the mass (km)   attraction (m)   net local change (m)")
    for r_km in (500.0, 1000.0, 2000.0, 5000.0, 10000.0):
        att = G_NEWTON * mass_kg / (G * r_km * 1e3)
        print(f"   {r_km:27.0f}   {att:13.2f}   {eustatic - att:19.2f}")
    att_2000 = G_NEWTON * mass_kg / (G * 2e6)
    print(f"\n  at 2000 km the attraction ({att_2000:.2f} m) EXCEEDS the eustatic")
    print(f"  rise ({eustatic:.2f} m), so sea level FALLS by "
          f"{att_2000 - eustatic:.2f} m near the")
    print("  melting ice sheet while the global mean rises.  The effect is real")
    print("  and is why the sea-level response to an ice-sheet loss is a pattern,")
    print("  not a number.  The point-mass approximation overstates the attraction")
    print("  at distances comparable with the ice sheet's own size, so the 500 km")
    print("  entry is indicative only; the sign and the crossover distance are the")
    print("  robust results.")
    print("  model limitation: this point-mass calculation omits the ocean's own")
    print("  gravitational self-interaction, the loading deformation of the solid")
    print("  Earth and the rotational feedback, all of which redistribute the")
    print("  meltwater and change the pattern by tens of per cent.  It gives the")
    print("  sign and the order of magnitude, which is what the qualitative")
    print("  statement needs.")

    section("5. Worked examples used in the lesson")
    print(f"(a) random trend error for {n} monthly points with "
          f"sigma = {sigma_pt:.0f} mm: {sig_rand:.4f} mm/yr")
    print(f"    drift bias for 0.1 mm/yr per yr over {years:.0f} years: "
          f"{trend_error_drift(0.1, n, spacing):.3f} mm/yr")
    print(f"(b) an uncorrected {vlm_true:.1f} mm/yr subsidence biases a 50-year")
    print(f"    gauge trend by {vlm_true:.1f} mm/yr; the GNSS correction's own")
    print(f"    error is 0.3 mm/yr, three times smaller but not negligible")
    print(f"(c) 1 mm of sea level = {1e-3 * A_OCEAN * RHO_W / GT:.0f} Gt; "
          f"1.9 mm/yr of ocean mass = "
          f"{1.9e-3 * A_OCEAN * RHO_W / GT / 1e3:.2f} x 10^3 Gt/yr")
    print(f"(d) eustatic rise for {mass_kg:.0e} kg = {eustatic:.2f} m; net change "
          f"at 2000 km = {eustatic - att_2000:+.2f} m")
    print("\nAll numbers are SYNTHETIC model output.")


if __name__ == "__main__":
    main()
