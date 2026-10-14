#!/usr/bin/env python3
"""Campaign scheduling arithmetic: weather downtime, schedule risk and the cost of
ignoring weather persistence, on SYNTHETIC weather.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_planning_demo.py

Everything here is SYNTHETIC.  The working-day probabilities, the day-to-day
persistence, the crew day rate and the mobilisation cost are chosen teaching
values.  No weather record and no commercial rate is used or reproduced.

Sections
--------
1. The naive schedule: onsite days divided by the working fraction.
2. Simulation with independent days.
3. Simulation with persistent (Markov) weather at the same long-run working rate.
4. Cost of the schedule, and the price of assuming independence.
5. Sensitivity of the schedule to the assumed working fraction.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

ONSITE_DAYS = 20.0      # productive days the survey needs
P_WET_GIVEN_WET = 0.65  # day-to-day persistence of bad weather (chosen)
P_WET_GIVEN_DRY = 0.30
WET_STATIONARY = P_WET_GIVEN_DRY / (P_WET_GIVEN_DRY + 1.0 - P_WET_GIVEN_WET)
WORK_STATIONARY = 1.0 - WET_STATIONARY
M = 20000               # simulated campaigns
LMAX = 120              # maximum calendar days simulated
RATE = 2400.0           # crew cost per calendar day (chosen units/day)
MOB = 25000.0           # mobilisation and demobilisation (chosen units)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def finish_days(cumulative_work):
    """First day index (1-based) on which the onsite requirement is met."""
    ok = cumulative_work >= ONSITE_DAYS
    days = np.argmax(ok, axis=1) + 1
    censored = ~ok[:, -1]
    days[censored] = LMAX + 1
    return days, int(censored.sum())


def simulate_independent(working_rate):
    work = RNG.random((M, LMAX)) < working_rate
    return finish_days(np.cumsum(work, axis=1))


def simulate_persistent():
    wet = np.empty((M, LMAX), dtype=bool)
    wet[:, 0] = RNG.random(M) < WET_STATIONARY
    u = RNG.random((M, LMAX - 1))
    prev = wet[:, :-1]
    wet[:, 1:] = np.where(prev, u < P_WET_GIVEN_WET, u < P_WET_GIVEN_DRY)
    return finish_days(np.cumsum(~wet, axis=1))


def main():
    section("1. The naive schedule")
    print(f"  onsite requirement = {ONSITE_DAYS:.0f} productive days")
    print(f"  assumed independent daily working probability = "
          f"{WORK_STATIONARY:.4f}")
    print(f"  naive expected calendar days = {ONSITE_DAYS:.0f}/"
          f"{WORK_STATIONARY:.4f} = {ONSITE_DAYS / WORK_STATIONARY:.2f} d")

    section("2. Simulation with independent days")
    ind, ind_censored = simulate_independent(WORK_STATIONARY)
    print(f"  {M} simulated campaigns, censoring at {LMAX} days "
          f"({ind_censored} censored)")
    print(f"  mean = {ind.mean():.2f} d, median = {np.median(ind):.1f} d, "
          f"sd = {ind.std():.2f} d")
    print(f"  P90 = {np.percentile(ind, 90):.1f} d, "
          f"P95 = {np.percentile(ind, 95):.1f} d, "
          f"max = {ind.max()} d")
    print(f"  P(overrun beyond 40 days) = {100.0 * (ind > 40).mean():.2f} %")

    section("3. Simulation with persistent weather at the same working rate")
    print(f"  Markov wet persistence: P(wet|wet) = {P_WET_GIVEN_WET:.2f}, "
          f"P(wet|dry) = {P_WET_GIVEN_DRY:.2f}")
    print(f"  stationary wet fraction = {WET_STATIONARY:.4f}, so the long-run")
    print(f"  working fraction is {WORK_STATIONARY:.4f} - the same as section 2")
    per, per_censored = simulate_persistent()
    print(f"  mean = {per.mean():.2f} d, median = {np.median(per):.1f} d, "
          f"sd = {per.std():.2f} d")
    print(f"  P90 = {np.percentile(per, 90):.1f} d, "
          f"P95 = {np.percentile(per, 95):.1f} d, "
          f"max = {per.max()} d")
    print(f"  P(overrun beyond 40 days) = {100.0 * (per > 40).mean():.2f} %")
    print(f"  sd ratio persistent/independent = {per.std() / ind.std():.3f}")

    section("4. Cost of the schedule")
    print(f"  crew rate = {RATE:.0f} units/day, mobilisation = {MOB:.0f} units")
    for label, days in (("independent", ind), ("persistent", per)):
        exp_cost = MOB + RATE * days.mean()
        p90_cost = MOB + RATE * np.percentile(days, 90)
        print(f"  {label:<12s} expected cost = {exp_cost:,.0f} units, "
              f"P90 cost = {p90_cost:,.0f} units")
    print(f"  price of the persistence assumption = "
          f"{(MOB + RATE * np.percentile(per, 90)) - (MOB + RATE * np.percentile(ind, 90)):,.0f} "
          f"units at the 90th percentile")
    print(f"  fixed-price 40-day contract = {MOB + RATE * 40.0:,.0f} units")

    section("5. Sensitivity of the expected schedule to the working fraction")
    print(f"  {'working fraction':>17s} {'expected days':>14s} "
          f"{'days per 0.01':>14s}")
    for w in (0.40, 0.45, 0.50, 0.55, 0.60, 0.70):
        expected = ONSITE_DAYS / w
        slope = ONSITE_DAYS / w ** 2 * 0.01
        print(f"  {w:17.2f} {expected:14.2f} {slope:14.3f}")
    print("  -> near a working fraction of 0.50 the schedule costs one extra")
    print("     day for every percentage point of assumed productivity.")

    print("\nSYNTHETIC: all numbers above come from the chosen parameters in this")
    print("file.  They constrain a scheduling model, not any real weather record")
    print("or rate card.")


if __name__ == "__main__":
    main()
