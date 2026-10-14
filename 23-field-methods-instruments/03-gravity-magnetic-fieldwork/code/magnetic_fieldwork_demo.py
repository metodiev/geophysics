#!/usr/bin/env python3
"""Magnetic fieldwork arithmetic: diurnal variation, base-station looping,
line levelling and a field depth estimate, on SYNTHETIC data.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_fieldwork_demo.py

Everything here is SYNTHETIC.  The diurnal amplitudes, reading noise, line
mis-tie and the sphere model are chosen teaching values.  No measured diurnal
curve, no field reading and no published anomaly is used or reproduced.

Sections
--------
1. A synthetic diurnal variation and what a base-loop correction leaves behind.
2. Line levelling: mis-tie statistics and the correction they justify.
3. Reading repeatability in nanotesla and the resulting survey accuracy.
4. A field depth estimate from the half-width of an anomaly, checked against the
   model depth.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

DIURNAL_A = 22.0        # nT, amplitude of the long-period diurnal term (chosen)
DIURNAL_B = 7.0         # nT, amplitude of the shorter-period term (chosen)
READ_NOISE = 1.5        # nT, one-reading standard deviation (chosen)
LINE_N = 5
DAY_HOURS = 8.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def diurnal(t):
    """SYNTHETIC diurnal variation in nT: one 24 h and one 8 h harmonic."""
    return (DIURNAL_A * np.sin(2.0 * np.pi * t / 24.0)
            + DIURNAL_B * np.sin(2.0 * np.pi * t / 8.0))


def sphere_anomaly(x, depth, radius):
    """Vertical-field anomaly of an induced sphere, arbitrary units."""
    x = np.asarray(x, dtype=float)
    return (depth ** 2 - x ** 2) / (x ** 2 + depth ** 2) ** 2.5 * radius ** 3


def main():
    section("1. A synthetic diurnal variation and the base-loop correction")
    print(f"  SYNTHETIC diurnal terms: {DIURNAL_A:.0f} nT at 24 h and "
          f"{DIURNAL_B:.0f} nT at 8 h")
    print(f"  {'t (h)':>7s} {'variation (nT)':>16s}")
    for t in (0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0):
        print(f"  {t:7.1f} {diurnal(t):16.3f}")
    t_stat = np.linspace(0.5, DAY_HOURS - 0.5, 40)
    signal = diurnal(t_stat)
    print(f"\n  40 stations read over {DAY_HOURS:.0f} h; the station's true anomaly")
    print(f"  is taken as 0 in this SYNTHETIC test, so the residual is the")
    print(f"  uncorrected diurnal variation")
    for label, ties in (("no correction", None),
                        ("two base ties (0, 8 h)", [0.0, DAY_HOURS]),
                        ("nine ties (hourly)",
                         list(np.linspace(0.0, DAY_HOURS, 9)))):
        if ties is None:
            residual = signal
        else:
            residual = signal - np.interp(t_stat, ties, diurnal(np.asarray(ties)))
        print(f"  {label:<26s} RMS residual = "
              f"{np.sqrt((residual ** 2).mean()):7.3f} nT, "
              f"max = {np.abs(residual).max():7.3f} nT")
    print("  -> a two-tie linear correction is not enough when the diurnal curve")
    print("     has a harmonic faster than the loop; loop more often, not longer.")

    section("2. Line levelling and mis-tie statistics")
    tie_levels = RNG.normal(0.0, 6.0, 12)     # nT shift per tie point
    mis_ties = []
    for line in range(LINE_N):
        for tie in range(12):
            mis_ties.append(tie_levels[tie] + READ_NOISE * RNG.standard_normal())
    mis_ties = np.array(mis_ties)
    mean_tie = mis_ties.mean()
    sd_tie = mis_ties.std(ddof=1)
    print(f"  {LINE_N} lines x 12 tie points, SYNTHETIC line-to-line shifts of")
    print(f"  6.0 nT standard deviation plus {READ_NOISE:.1f} nT reading noise")
    print(f"  mis-tie: mean = {mean_tie:.3f} nT, sd = {sd_tie:.3f} nT, "
          f"max |mis-tie| = {np.abs(mis_ties).max():.3f} nT")
    print(f"  95 % of mis-ties within = {1.96 * sd_tie:.3f} nT")
    print(f"  mis-ties exceeding 15 nT = "
          f"{int((np.abs(mis_ties) > 15.0).sum())} of {mis_ties.size}")
    print(f"  an unlevelled line-to-line shift of {sd_tie:.1f} nT is "
          f"{100.0 * sd_tie / 100.0:.1f} % of a 100 nT target anomaly,")
    print(f"  and it appears as a STEP along the tie line, which no filter can")
    print(f"  distinguish from a geological boundary running along that line.")
    print("  -> levelling removes the LINE, not the geology: correct it before")
    print("     interpreting any anomaly that crosses a tie point.")

    section("3. Reading repeatability")
    n_repeat = 15
    readings = diurnal(3.0) + READ_NOISE * RNG.standard_normal(n_repeat)
    sd = readings.std(ddof=1)
    print(f"  {n_repeat} repeats at one station, SYNTHETIC noise "
          f"{READ_NOISE:.1f} nT")
    print(f"  measured standard deviation = {sd:.3f} nT")
    print(f"  standard error of the mean of 3 readings = "
          f"{sd / np.sqrt(3.0):.3f} nT")
    print(f"  a 100 nT total-field anomaly is therefore "
          f"{100.0 / (sd / np.sqrt(3.0)):.0f} times the standard error of a")
    print(f"  three-reading station value")

    section("4. A field depth estimate from the half-width")
    depth = 40.0
    radius = 25.0
    x = np.linspace(-300.0, 300.0, 60001)
    a = sphere_anomaly(x, depth, radius)
    peak = a.max()
    above = a >= peak / 2.0
    half_width = x[above].max()
    ratio = depth / half_width
    print(f"  SYNTHETIC induced sphere: depth {depth:.0f} m, radius "
          f"{radius:.0f} m")
    print(f"  peak anomaly (arbitrary units) = {peak:.4e}")
    print(f"  half-width (x at half the peak) = {half_width:.2f} m")
    print(f"  full width at half maximum = {2.0 * half_width:.2f} m")
    print(f"  measured depth / half-width = {ratio:.3f}")
    print(f"  depth from depth ~= 2.2 x half-width = {2.2 * half_width:.2f} m "
          f"({100.0 * (2.2 * half_width - depth) / depth:+.2f} %)")
    print("  -> the factor is a property of the MODEL, not a constant of")
    print("     nature: a horizontal cylinder or a thin sheet gives a")
    print("     different number.  Quote the model with the rule, and treat")
    print("     the result as a siting aid, not as an inversion.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file.  They constrain a survey model, not any real dataset.")


if __name__ == "__main__":
    main()
