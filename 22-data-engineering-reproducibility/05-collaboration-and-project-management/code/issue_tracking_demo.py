#!/usr/bin/env python3
"""Issue tracking for research: Little's law, cycle time and WIP limits.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python issue_tracking_demo.py

Everything here is SYNTHETIC.  Arrival rates, service times and the congestion model
are chosen teaching values; no issue tracker was read and no team was observed.

Sections
--------
1. Little's law: throughput, work in progress and lead time.
2. The work itself: a cycle-time distribution with a long tail.
3. Lead time as work plus queueing, for four work-in-progress levels.
4. When demand exceeds capacity: what a WIP limit can and cannot do.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC team model (chosen, not measured) ----------------------------
ARRIVALS_PER_WEEK = 6.0          # new issues per week
CAPACITY_PER_WEEK = 12.0         # issues the team could finish if unblocked
MEDIAN_WORK_DAYS = 9.0           # median time actually spent on an issue
SIGMA_LOG = 1.1                  # lognormal shape: a long tail
N_ISSUES = 5000


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. Little's law: throughput, WIP and lead time")
    throughput = ARRIVALS_PER_WEEK / 5.0        # issues per working day
    print(f"SYNTHETIC team: arrivals {ARRIVALS_PER_WEEK:.1f} issues/week, "
          f"capacity {CAPACITY_PER_WEEK:.0f}/week (chosen)")
    print(f"  throughput in a steady state = {throughput:.2f} issues/day")
    print("  Little's law:  WIP = throughput x lead time, so")
    print("  WIP (issues in progress) | implied lead time (days)")
    for wip in (2, 6, 12, 24):
        print(f"  {wip:>24d} | {wip / throughput:>25.1f}")
    print("  -> with a fixed arrival rate every extra item in progress lengthens")
    print("     the wait for all of them; the WIP is the control, not the goal")

    section("2. The work itself: a cycle-time distribution")
    work = RNG.lognormal(np.log(MEDIAN_WORK_DAYS), SIGMA_LOG, N_ISSUES)
    print(f"  {N_ISSUES} SYNTHETIC issues, lognormal work time with median "
          f"{MEDIAN_WORK_DAYS:.0f} days (chosen)")
    for p in (50, 75, 90, 99):
        print(f"  {p:>2d}th percentile of work time = "
              f"{np.percentile(work, p):>6.1f} days")
    print(f"  mean = {work.mean():.1f} days, maximum = {work.max():.1f} days")
    print("  -> the mean sits above the median and the maximum is far above both:")
    print("     planning with the median understates the tail that people notice")

    section("3. Lead time as work plus queueing")
    print("  WIP | wait = WIP/throughput | median lead | 90th pct lead")
    for wip in (2, 6, 12, 24):
        wait = wip / throughput
        lead = work + wait
        print(f"  {wip:>3d} | {wait:>21.1f} | {np.median(lead):>11.1f} | "
              f"{np.percentile(lead, 90):>14.1f}")
    low, high = 2, 24
    ratio = np.percentile(work + high / throughput, 90) / \
        np.percentile(work + low / throughput, 90)
    print(f"  the 90th percentile of lead time is {ratio:.1f}x larger at WIP "
          f"{high} than at WIP {low}")
    print("  -> queueing adds a constant to every item's lead time, so a limit")
    print("     moves the percentile people plan with, at no cost to throughput")

    section("4. When demand exceeds capacity")
    for arrivals in (6.0, 12.0, 18.0):
        net = arrivals - CAPACITY_PER_WEEK
        if net <= 0:
            print(f"  arrivals {arrivals:.0f}/week: backlog drains at "
                  f"{-net:.0f}/week; a WIP limit only shortens the queue")
        else:
            print(f"  arrivals {arrivals:.0f}/week: backlog grows by {net:.0f}/week "
                  f"({net * 52:.0f}/year) and lead time grows without bound")
    print("  -> a WIP limit cannot create capacity: below capacity it shortens")
    print("     lead time, above it makes the growing backlog visible instead of")
    print("     hiding it inside everyone's in-progress list")


if __name__ == "__main__":
    main()
