#!/usr/bin/env python3
"""Timing arithmetic for geophysical instruments: fractional clock error, holdover
after loss of lock, PPS jitter averaging, Allan-deviation scaling and a timing
budget, on SYNTHETIC values.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python timing_and_gnss_demo.py

Everything here is SYNTHETIC.  The fractional errors, holdover stabilities, jitter
figures and timing budgets are chosen teaching values, and the relations printed are
the standard ones quoted in the text.  No measured oscillator specification and no
manufacturer figure is used or reproduced.

Sections
--------
1. Fractional clock error and the time it accumulates.
2. Holdover after losing the GNSS lock, and the days a timing budget survives.
3. PPS jitter, averaging, and the counter resolution it needs.
4. Allan deviation: how random error accumulates with averaging time.
5. A system timing budget: the requirement, the re-visit interval and the apparent
   distance error it implies.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main():
    section("1. Fractional clock error and accumulated time")
    print("  error = epsilon x elapsed time")
    print(f"  {'epsilon':>10s} {'1 h (s)':>12s} {'1 day (s)':>12s}"
          f" {'30 days (s)':>13s} {'1 day (samples at 100 sps)':>28s}")
    for eps in (1.0e-6, 1.0e-7, 1.0e-8, 1.0e-9):
        one_hour = eps * 3600.0
        one_day = eps * 86400.0
        month = eps * 86400.0 * 30.0
        print(f"  {eps:10.0e} {one_hour:12.4e} {one_day:12.4e} {month:13.4e} "
              f"{one_day * 100.0:28.1f}")
    print("  -> one part per million is 86.4 ms per day, which is already")
    print("     kilometres of apparent range; one part per billion is 86.4")
    print("     microseconds per day and is the regime a GNSS lock provides.")

    section("2. Holdover after losing the lock")
    budget = 1.0e-3
    print(f"  timing budget = {budget * 1000:.1f} ms")
    print(f"  {'holdover':>14s} {'per day (us)':>14s} {'days to exhaust budget':>24s}")
    for hold in (1.0e-5, 1.0e-6, 1.0e-7, 1.0e-8, 1.0e-9):
        per_day = hold * 86400.0
        print(f"  {hold:14.0e} {per_day * 1e6:14.2f} {budget / per_day:24.1f}")
    print("  (the holdover figure is a fractional frequency error per day, and its")
    print("   value must come from the oscillator's own documentation)")
    print("  -> a free-running quartz oscillator exhausts a millisecond budget in")
    print("     hours; a disciplined oscillator holds it for weeks.")

    section("3. PPS jitter and averaging")
    jitter = 20.0e-9
    print(f"  pulse-per-second jitter = {jitter * 1e9:.0f} ns rms (chosen)")
    print(f"  {'N averaged':>12s} {'effective jitter (ns)':>23s}"
          f" {'time error per day (us)':>25s}")
    for n in (1, 10, 100, 1000, 10000):
        eff = jitter / np.sqrt(n)
        print(f"  {n:12d} {eff * 1e9:23.3f} {eff * 86400.0 * 1e6:25.4f}")
    print("  -> averaging N pulses reduces the *random* part of the jitter by")
    print("     sqrt(N) but does nothing to a constant offset: the offset must be")
    print("     calibrated against a reference, not averaged away.")

    section("4. Allan deviation and random error accumulation")
    sigma_y_1s = 1.0e-11
    print(f"  white frequency noise with sigma_y(1 s) = {sigma_y_1s:.0e}")
    print("  sigma_y(tau) = sigma_y(1 s)/sqrt(tau/1 s)")
    print(f"  {'tau (s)':>9s} {'sigma_y(tau)':>15s}")
    for tau in (1.0, 10.0, 100.0, 1000.0, 10000.0):
        print(f"  {tau:9.0f} {sigma_y_1s / np.sqrt(tau):15.4e}")
    T = 86400.0
    sigma_x = sigma_y_1s * np.sqrt(T * 1.0)
    system = sigma_y_1s * T
    print(f"\n  over T = {T:.0f} s:")
    print(f"  random accumulated error sigma_x = sigma_y(1s) sqrt(T) = "
          f"{sigma_x:.4e} s = {sigma_x * 1e9:.2f} ns")
    print(f"  systematic offset        = sigma_y(1s) x T          = "
          f"{system:.4e} s = {system * 1e6:.3f} us")
    print("  -> over a day the *random* part of a good oscillator's error is")
    print("     nanoseconds while the *systematic* part is microseconds: the")
    print("     offset, not the noise, is what a clock comparison must remove.")

    section("5. A system timing budget")
    velocity = 3.0
    print(f"  apparent distance error = V x dt with V = {velocity:.1f} km/s")
    print(f"  {'dt':>10s} {'apparent distance (m)':>22s} {'holdover days at 1e-9':>23s}")
    for dt in (1.0e-6, 1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1):
        metres = velocity * dt * 1000.0
        days = dt / (1.0e-9 * 86400.0)
        print(f"  {dt:10.0e} {metres:22.3f} {days:23.2f}")
    print("  -> a 1 ms relative timing error is 3 m of apparent distance at this")
    print("     velocity, and a 1e-9 holdover allows 11.6 days before the budget")
    print("     is exhausted.  That number is the maintenance re-visit interval.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file, combined with the standard relations quoted in the text.")


if __name__ == "__main__":
    main()
