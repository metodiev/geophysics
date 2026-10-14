#!/usr/bin/env python3
"""Deployment arithmetic: orientation error, timing discipline, ground coupling
and sensor tilt, on SYNTHETIC parameters.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_deployment_demo.py

Everything here is SYNTHETIC.  The orientation errors, clock accuracies, lock-loss
rates, coupling resonates and tilt angles are chosen teaching values.  No measured
installation response, no manufacturer clock specification and no field data are
used or reproduced.

Sections
--------
1. Orientation error and the signal it leaks between horizontal components.
2. Timing: lock-loss statistics and the drift accumulated without a lock.
3. Ground coupling: the deviation a soil resonance adds to the response.
4. Sensor tilt and its apparent horizontal acceleration.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def resonance_mag(f, f0, h):
    """|H| of a single-degree-of-freedom system, normalised to 1 at high f."""
    r = np.asarray(f, dtype=float) / f0
    return r ** 2 / np.sqrt((1.0 - r ** 2) ** 2 + (2.0 * h * r) ** 2)


def main():
    section("1. Orientation error: leakage between radial and transverse")
    print("  a wave arriving in the radial plane has no transverse energy; an")
    print("  orientation error of delta puts sin(delta) of the radial amplitude")
    print("  into the transverse component")
    print(f"  {'delta (deg)':>12s} {'sin(delta)':>11s} {'T/R (dB)':>10s}"
          f" {'fast-direction bias':>21s}")
    for delta in (0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 30.0):
        s = np.sin(np.radians(delta))
        print(f"  {delta:12.1f} {s:11.5f} {20.0 * np.log10(s):10.2f} "
              f"{delta:19.1f} deg")
    print("  -> a 5 deg error puts transverse energy at -21.2 dB, which is")
    print("     larger than most real anisotropy signals, and biases a")
    print("     single-station fast direction by up to the error itself.")
    print("     Orientation is a measurement, not a formality.")

    section("2. Timing: lock loss and accumulated drift")
    n_stat, days, p_loss = 30, 20, 0.03
    print(f"  {n_stat} stations, {days} days, probability of losing the GNSS")
    print(f"  lock on any station-day = {p_loss:.2f} (chosen)")
    no_loss = (1.0 - p_loss) ** days
    print(f"  expected station-days with a loss = {n_stat * days * p_loss:.1f}")
    print(f"  stations with at least one loss = "
          f"{n_stat * (1.0 - no_loss):.2f} of {n_stat} "
          f"({100.0 * (1.0 - no_loss):.1f} %)")
    print(f"  expected lost time = {n_stat * days * p_loss * 24.0:.0f} station-hours")
    print("\n  fractional clock error -> drift while unlocked:")
    print(f"  {'error':>10s} {'1 day (s)':>11s} {'1 day (samples @100 sps)':>25s}"
          f" {'20 days (s)':>12s}")
    for eps in (1.0e-6, 5.0e-6, 1.0e-5, 5.0e-5):
        one_day = eps * 86400.0
        print(f"  {eps:10.1e} {one_day:11.4f} {one_day * 100.0:25.1f} "
              f"{eps * 86400.0 * 20.0:12.3f}")
    print("  -> a free-running oscillator does not fail loudly; it produces a")
    print("     record that is internally consistent and externally wrong.")

    section("3. Ground coupling: a soil resonance in series")
    f_c, h_c = 20.0, 0.5
    print(f"  synthetic soil-sensor resonance f_c = {f_c:.0f} Hz, damping "
          f"{h_c:.2f}")
    print(f"  {'f (Hz)':>8s} {'|H_coupling|':>14s} {'deviation (dB)':>16s}")
    for f in (1.0, 2.0, 5.0, 10.0, 20.0, 40.0, 80.0):
        m = resonance_mag(f, f_c, h_c)
        print(f"  {f:8.1f} {m:14.4f} {20.0 * np.log10(m):16.2f}")
    print("  -> below the coupling resonance the response is close to 1 and the")
    print("     installation is harmless; from ~0.3 f_c upward it is not, and a")
    print("     'response correction' that ignores the installation is wrong.")

    section("4. Sensor tilt and apparent horizontal acceleration")
    g = 9.81
    print("  a sensor tilted by theta from vertical senses g sin(theta) as an")
    print("  apparent horizontal acceleration")
    print(f"  {'theta (deg)':>12s} {'theta (arcsec)':>15s}"
          f" {'apparent a (m/s^2)':>20s}")
    for theta_deg in (0.001, 0.005, 0.01, 0.05, 0.1, 1.0):
        a = g * np.sin(np.radians(theta_deg))
        print(f"  {theta_deg:12.3f} {theta_deg * 3600.0:15.1f} {a:20.3e}")
    print("\n  tilt that produces a stated apparent acceleration:")
    print(f"  {'target a (m/s^2)':>18s} {'theta (deg)':>13s} "
          f"{'theta (arcsec)':>15s}")
    for target in (1.0e-6, 1.0e-5, 1.0e-4):
        theta = np.degrees(np.arcsin(target / g))
        print(f"  {target:18.1e} {theta:13.4f} {theta * 3600.0:15.1f}")
    print("  -> even a fraction of an arcsecond of tilt imitates a horizontal")
    print("     acceleration of order 1e-6 m/s^2, which is a large long-period")
    print("     signal: tilt, not sensor noise, usually sets the horizontal")
    print("     long-period noise floor, and is why broadband installations are")
    print("     levelled carefully and, at the best sites, tilt-compensated.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file.  They constrain a deployment model, not any real installation.")


if __name__ == "__main__":
    main()
