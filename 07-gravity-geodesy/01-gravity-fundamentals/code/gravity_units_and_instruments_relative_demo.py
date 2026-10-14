#!/usr/bin/env python3
"""Gravity units and the difference between absolute and relative measurement:
conversions among m/s^2, Gal, mGal and uGal, a synthetic least-squares calibration
of a relative meter against absolute stations, error propagation into a measured
difference, a precision-versus-accuracy experiment, and how uncertainty grows away
from a network's absolute base.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_units_and_instruments_relative_demo.py

Everything is SYNTHETIC: the meter, its calibration, the station values and the
noise are chosen teaching values.  The only exact quantities are G (6.67430e-11
m^3 kg^-1 s^-2), the GM of the model Earth (3.986004418e14 m^3 s^-2, WGS84) and
the unit definitions 1 Gal = 0.01 m/s^2, 1 mGal = 1e-5 m/s^2,
1 uGal = 1e-8 m/s^2.

Contents
--------
1. Units: the whole field and the smallest useful differences, in every unit.
2. How small is a mGal?  A geometric comparison and a mass comparison.
3. Absolute versus relative measurement, with SYNTHETIC uncertainties.
4. Least-squares calibration of a relative meter against absolute stations.
5. Error propagation into a measured gravity difference.
6. A precision-versus-accuracy experiment: two meters, two failure modes.
7. A network tied to one absolute base: how the uncertainty grows with distance.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 6.67430e-11
GM_EARTH = 3.986004418e14       # m^3 s^-2 (WGS84 defining constant)
G_EARTH_MODEL = 9.820250        # m/s^2, spherical model from lesson 01

COUNTS_PER_MGAL = 1000.0        # SYNTHETIC instrument sensitivity, counts/mGal
SIGMA_ABSOLUTE_MGAL = 5.0e-3    # 5 uGal absolute reference uncertainty
SIGMA_COUNT = 0.3               # counts, SYNTHETIC reading repeatability


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    section("1. Units")
    print("  exact definitions: 1 Gal = 0.01 m/s^2, 1 mGal = 1e-5 m/s^2,")
    print("                     1 uGal = 1e-8 m/s^2")
    print("   value                     m/s^2          Gal           mGal          uGal")
    for label, g in (("model surface g", G_EARTH_MODEL),
                     ("1 mGal", 1.0e-5),
                     ("1 uGal", 1.0e-8),
                     ("best absolute meter (5 uGal)", 5.0e-8),
                     ("typical relative survey (10 uGal)", 1.0e-7),
                     ("field difference between two stations", 1.0e-4)):
        print(f"   {label:30s} {g:12.5e} {g * 1e2:12.5e} {g * 1e5:12.5e} "
              f"{g * 1e8:12.5e}")
    print(f"  1 mGal is {1e-5 / G_EARTH_MODEL:.3e} of the field: about 1 part in 10^6")

    section("2. How small is a mGal?")
    mass = 1000.0                        # kg
    r_for_mgal = np.sqrt(G * mass / 1.0e-5)
    print(f"  a {mass:.0f} kg mass produces 1 mGal at r = {r_for_mgal:.4f} m")
    print(f"  1 uGal corresponds to the same mass at r = "
          f"{np.sqrt(G * mass / 1.0e-8):.4f} m")
    print(f"  ratio of those distances = sqrt(100) = {np.sqrt(100.0):.1f}, "
          f"as r ~ g^-1/2 requires")
    dz = 1.0
    print(f"  vertically, 1 mGal is equivalent to {1.0e-5 / (2 * G_EARTH_MODEL / 6371e3):.4f} m")
    print("  of elevation, using 2g/r = 3.083e-6 s^-2 from lesson 01: a microgal")
    print("  is a 3 mm change in the station's height.")
    print(f"  a change of 1 uGal is equivalent to a density change of "
          f"{1.0e-8 / (2 * np.pi * G * 1000.0):.4f} kg/m^3 acting through 1000 m")
    print(f"  of rock, or {1.0e-8 / (2 * np.pi * G * 100.0):.4f} kg/m^3 acting through "
          f"100 m: gravity responds to the product of density and thickness")

    section("3. Absolute versus relative measurement (SYNTHETIC)")
    g_abs = 979_500.0000        # mGal, SYNTHETIC absolute value at the base
    print(f"  ABSOLUTE measurement: g_base = {g_abs:.4f} mGal "
          f"+/- {SIGMA_ABSOLUTE_MGAL * 1e3:.1f} uGal")
    print("  a relative meter does not produce g.  It produces a reading whose")
    print("  differences are proportional to gravity differences:")
    print(f"   sensitivity assumed: {COUNTS_PER_MGAL:.0f} counts per mGal, i.e. "
          f"1 count = {1.0 / COUNTS_PER_MGAL:.6f} mGal")
    print("  The reading at the base and at a field station, SYNTHETIC:")
    reading_base = 12_345.0
    reading_field = reading_base + 6_250.0        # counts
    print(f"   base   reading = {reading_base:.1f} counts")
    print(f"   field  reading = {reading_field:.1f} counts, "
          f"difference {reading_field - reading_base:.1f} counts")
    diff_mgal = (reading_field - reading_base) / COUNTS_PER_MGAL
    print(f"   nominal difference = {diff_mgal:.4f} mGal, so the field station is")
    print(f"   g_field = {g_abs + diff_mgal:.4f} mGal on that calibration alone")
    print("  The absolute value enters as a datum; the meter supplies the shape.")

    section("4. Least-squares calibration against absolute stations")
    n_st = 12
    truth_g = g_abs + np.linspace(-6.0, 6.0, n_st)          # mGal, SYNTHETIC truth
    cal_true = 1.0 / COUNTS_PER_MGAL                        # mGal per count
    counts = reading_base + (truth_g - g_abs) / cal_true \
        + SIGMA_COUNT * RNG.standard_normal(n_st)
    measured_g = truth_g + SIGMA_ABSOLUTE_MGAL * RNG.standard_normal(n_st)
    A = np.column_stack([counts, np.ones(n_st)])            # slope, intercept
    coef, *_ = np.linalg.lstsq(A, measured_g, rcond=None)
    resid = measured_g - A @ coef
    dof = n_st - 2
    s2 = resid @ resid / dof
    cov = s2 * np.linalg.inv(A.T @ A)
    slope, intercept = coef
    sig_slope, sig_int = np.sqrt(np.diag(cov))
    corr = cov[0, 1] / (sig_slope * sig_int)
    print(f"  fit: g = slope * counts + intercept, using {n_st} stations")
    print(f"   slope     = {slope:.6e} mGal/count "
          f"(+/- {sig_slope:.2e}, i.e. {sig_slope / slope * 100:.4f}%)")
    print(f"   intercept = {intercept:.4f} mGal (+/- {sig_int:.4f})")
    print(f"   correlation between slope and intercept = {corr:+.4f}")
    print(f"   residuals: rms = {np.sqrt(np.mean(resid ** 2)):.5f} mGal, "
          f"max |r| = {np.max(np.abs(resid)):.5f} mGal, dof = {dof}")
    print(f"   nominal sensitivity is exactly 1/1000 = 0.001000 mGal/count:")
    print(f"   recovered slope implies {1.0 / slope:.3f} counts per mGal")
    print("  The strong negative correlation between slope and intercept is the")
    print("  reason a calibration must span a wide gravity range: with a narrow")
    print("  range, an error in the slope can be absorbed by the intercept.  The")
    print("  intercept refers to counts = 0, far outside the observed range, which")
    print(f"  is why its uncertainty ({sig_int * 1e3:.1f} uGal) is comparable with")
    print("  the input noise and its correlation is large;")
    print("  centring the counts on their mean would reduce both, without changing")
    print("  any difference computed from the fit.")

    section("5. Error propagation into a measured difference")
    diff_counts = reading_field - reading_base
    sig_from_cal = abs(diff_counts) * sig_slope
    sig_from_counts = np.sqrt(2.0) * SIGMA_COUNT * slope
    sig_total = np.sqrt(sig_from_cal ** 2 + sig_from_counts ** 2)
    print(f"  difference = {diff_counts:.0f} counts x {slope:.6e} mGal/count "
          f"= {diff_counts * slope:.4f} mGal")
    print(f"   uncertainty from the calibration slope: {sig_from_cal * 1e3:.4f} uGal")
    print(f"   uncertainty from the readings (2 stations): "
          f"{sig_from_counts * 1e3:.4f} uGal")
    print(f"   combined: {sig_total * 1e3:.4f} uGal "
          f"({sig_total / abs(diff_counts * slope) * 100:.4f}% of the difference)")
    print("  For this instrument the calibration slope dominates, which is typical")
    print("  of relative meters: their repeatability is better than their scale")
    print("  accuracy, so differences over SHORT spans are more reliable than")
    print("  differences over long spans.")

    section("6. Precision versus accuracy: two SYNTHETIC meters")
    span = 5.0            # mGal, the difference we care about
    for label, bias_frac, noise in (
            ("precise but mis-calibrated", 1.0e-3, 0.2e-3),
            ("imprecise but unbiased", 0.0, 5.0e-3)):
        bias = bias_frac * span
        total = np.sqrt(bias ** 2 + (np.sqrt(2.0) * noise) ** 2)
        print(f"  {label:28s}: bias {bias * 1e3:+.3f} uGal, "
              f"random {np.sqrt(2.0) * noise * 1e3:.3f} uGal, "
              f"total {total * 1e3:.3f} uGal")
        print(f"      {'->' if total > 3e-3 else '  '} on a {span:.0f} mGal span, "
              f"error = {total / span * 100:.4f}% of the signal")
    print("  Precision is repeatability; accuracy is closeness to the true value.")
    print("  Averaging repeats reduces the random part and does nothing to the bias,")
    print("  so a calibration error cannot be averaged away.  The only cure is an")
    print("  independent check: an absolute station, a tie, or a known reference.")

    section("7. Network uncertainty away from an absolute base")
    sigma_link = 8.0e-3          # mGal = 8 uGal per link, SYNTHETIC
    print(f"  SYNTHETIC per-link uncertainty: {sigma_link * 1e3:.1f} uGal "
          f"(repeatability of the meter)")
    print(f"  base uncertainty from the absolute measurement: "
          f"{SIGMA_ABSOLUTE_MGAL * 1e3:.1f} uGal")
    print("   links from base   sqrt(N)*link (uGal)   plus base (uGal)   propagated (uGal)")
    for links in (1, 2, 5, 10, 25, 100):
        rand = np.sqrt(links) * sigma_link * 1e3
        total = np.sqrt(rand ** 2 + (SIGMA_ABSOLUTE_MGAL * 1e3) ** 2)
        print(f"   {links:15d}   {rand:20.3f}   "
              f"{SIGMA_ABSOLUTE_MGAL * 1e3:14.1f}   {total:16.3f}")
    print("  Uncertainty grows as the square root of the number of links, so it is")
    print("  the NUMBER of links that matters, not the distance: a long single tie")
    print("  is better than a chain of short ones.  Re-occupying the base, or adding")
    print("  a second absolute station, resets the accumulation.")
    print("  Note also that at 100 links the random term "
          f"({np.sqrt(100) * sigma_link * 1e3:.1f} uGal) finally exceeds the")
    print(f"  absolute datum ({SIGMA_ABSOLUTE_MGAL * 1e3:.1f} uGal): before that, the")
    print("  network is limited by the datum, not by the survey.")


if __name__ == "__main__":
    main()
