#!/usr/bin/env python3
"""Gravity fieldwork arithmetic: instrument drift, base ties, loop closure and the
residual left by a drift correction, on SYNTHETIC data.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_fieldwork_demo.py

Everything here is SYNTHETIC.  The drift rate, tidal amplitudes, loop times,
reading uncertainty and station spacing are chosen teaching values.  No measured
instrument drift, no tidal model and no field reading is used or reproduced.

Sections
--------
1. A synthetic gravity drift: a linear instrument term plus a nonlinear tidal term.
2. What a two-tie and a three-tie drift correction leaves behind.
3. Loop closure error as a QC statistic, and how it scales with loop duration.
4. Reading repeatability and the survey accuracy it implies.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

DRIFT_RATE = 0.008       # mGal per hour, linear instrument drift (chosen)
TIDE_SEMI = 0.10         # mGal, semi-diurnal tidal amplitude (chosen)
TIDE_DIURNAL = 0.04      # mGal, diurnal tidal amplitude (chosen)
READ_NOISE = 0.005       # mGal, one-reading standard deviation (chosen)
LOOP_HOURS = 6.0         # duration of one loop (chosen)
N_STATION = 12


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def drift(t):
    """SYNTHETIC drift: linear instrument term plus two tidal harmonics."""
    return (DRIFT_RATE * t
            + TIDE_SEMI * np.sin(2.0 * np.pi * t / 12.4)
            + TIDE_DIURNAL * np.sin(2.0 * np.pi * t / 24.0))


def correction_from_ties(t, tie_times):
    """Piecewise-linear correction that passes through the ties assuming a
    true reading of 0 at every tie (the synthetic convention)."""
    tie_values = drift(np.asarray(tie_times))
    return np.interp(t, tie_times, tie_values)


def main():
    section("1. A synthetic gravity drift")
    times = np.linspace(0.0, LOOP_HOURS, 601)
    print(f"  linear instrument drift = {DRIFT_RATE:.4f} mGal/h")
    print(f"  tidal terms: {TIDE_SEMI:.2f} mGal at a 12.4 h period and "
          f"{TIDE_DIURNAL:.2f} mGal at 24 h (SYNTHETIC amplitudes)")
    print(f"  {'t (h)':>7s} {'drift (mGal)':>14s}")
    for t in (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0):
        print(f"  {t:7.1f} {drift(t):14.4f}")
    print(f"  total change over a {LOOP_HOURS:.0f} h loop = "
          f"{drift(LOOP_HOURS) - drift(0.0):.4f} mGal")
    print(f"  the tidal part alone would not be removed by a drift RATE, because")
    print(f"  it is not linear in time.")

    section("2. What the drift correction leaves behind")
    t_stat = np.linspace(0.25, LOOP_HOURS - 0.25, N_STATION)
    signal = drift(t_stat)          # the reading = drift; the true anomaly is 0
    for label, tries in (("no correction", None),
                         ("two base ties (0 and 6 h)", [0.0, LOOP_HOURS]),
                         ("three ties (0, 3, 6 h)",
                          [0.0, LOOP_HOURS / 2.0, LOOP_HOURS]),
                         ("four ties (0, 2, 4, 6 h)",
                          [0.0, 2.0, 4.0, LOOP_HOURS])):
        if tries is None:
            residual = signal
        else:
            residual = signal - correction_from_ties(t_stat, tries)
        print(f"  {label:<30s} RMS residual = "
              f"{np.sqrt((residual ** 2).mean()):.4f} mGal, "
              f"max = {np.abs(residual).max():.4f} mGal")
    print("  -> the residual falls fast as ties are added: 0.0732 -> 0.0160 mGal")
    print("     when a midpoint tie is added, and a further 2.2x with a fourth.")
    print("     The cost is field time, not money.")

    section("3. Loop closure error as a QC statistic")
    print("  the closure error is the difference between the first and last base")
    print("  readings before correction; it depends on the loop DURATION and on")
    print("  the phase of the tide at which the loop runs")
    print(f"  {'loop (h)':>9s} {'closure over 4 start times (mGal)':>36s}"
          f" {'worst (mGal)':>14s}")
    starts = (0.0, 3.0, 6.0, 9.0)
    for hours in (2.0, 4.0, 6.0, 8.0):
        values = [abs(drift(t0 + hours) - drift(t0)) for t0 in starts]
        text = " ".join(f"{v:7.3f}" for v in values)
        print(f"  {hours:9.1f} {text:>36s} {max(values):14.4f}")
    noise = READ_NOISE * np.sqrt(2.0)
    print(f"  reading noise on a closure difference = {noise:.4f} mGal, which is")
    print(f"  negligible compared with the tidal term at these loop lengths")
    print("  -> the closure tolerance has to be stated with the loop duration AND")
    print("     with the time of day; a single number for all loops is not a")
    print("     criterion, it is a hope.")

    section("4. Reading repeatability and survey accuracy")
    n_repeat = 10
    readings = drift(2.0) + READ_NOISE * RNG.standard_normal(n_repeat)
    sd = readings.std(ddof=1)
    print(f"  {n_repeat} repeats of one station, SYNTHETIC reading noise "
          f"{READ_NOISE:.3f} mGal")
    print(f"  measured standard deviation = {sd:.4f} mGal")
    print(f"  95 % repeatability (2.23 x sd for n = {n_repeat}) = "
          f"{2.23 * sd:.4f} mGal")
    print(f"  with 3 repeats per station the standard error of the station mean")
    print(f"  would be {sd / np.sqrt(3.0):.4f} mGal")
    print(f"  free-air equivalent of a 0.01 mGal error at "
          f"0.3086 mGal/m = {0.01 / 0.3086:.4f} m")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file.  They constrain a survey model, not any real instrument.")


if __name__ == "__main__":
    main()
