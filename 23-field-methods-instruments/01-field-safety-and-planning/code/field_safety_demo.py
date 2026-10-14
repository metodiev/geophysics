#!/usr/bin/env python3
"""Field-safety arithmetic on SYNTHETIC values.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_safety_demo.py

Everything here is SYNTHETIC.  The hazard list, the likelihood and severity
ratings, the control effectiveness, the missed-check-in probability, the
escalation grace period and the rescue window are chosen teaching values.  They
are not measured incident statistics, they are not a risk assessment, and
nothing printed here is safety advice for a real campaign.

Sections
--------
1. A risk register scored as likelihood x severity.
2. Residual risk after a stated control.
3. Check-in arithmetic: how many alarms a campaign generates.
4. The detection delay implied by a check-in interval.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. SYNTHETIC risk register: score = likelihood x severity")
    hazards = [
        "vehicle rollover",
        "rockfall / unstable slope",
        "heat stress",
        "hypothermia / wet cold",
        "river crossing",
        "aircraft sling load",
        "wildlife encounter",
        "hand-tool laceration",
    ]
    likelihood = np.array([2, 2, 3, 2, 2, 1, 2, 3], dtype=float)
    severity = np.array([5, 5, 4, 4, 5, 5, 3, 1], dtype=float)
    score = likelihood * severity
    for i in np.argsort(-score):
        print(f"  {hazards[i]:<24s} L={likelihood[i]:.0f}  S={severity[i]:.0f}"
              f"  score={score[i]:.0f}")
    print(f"  hazards = {score.size}, total score = {score.sum():.0f}, "
          f"mean = {score.mean():.2f}, max = {score.max():.0f}")
    print("  (L and S are dimensionless 1-5 ratings chosen for teaching, "
          "not frequencies.)")

    section("2. Residual risk after a stated control")
    l_res = np.maximum(1.0, np.ceil(0.5 * likelihood))
    score_res = l_res * severity
    reduction = 100.0 * (1.0 - score_res.sum() / score.sum())
    print("  control assumption: halve the likelihood rating, keep severity")
    print(f"  total score before controls = {score.sum():.0f}")
    print(f"  total score after  controls = {score_res.sum():.0f}")
    print(f"  reduction = {reduction:.1f} % "
          f"(ratio {score.sum() / score_res.sum():.2f}x)")
    print(f"  hazards still at or above a score of 5 = "
          f"{int((score_res >= 5).sum())} of {score_res.size}")
    print(f"  mean residual score = {score_res.mean():.3f}")
    print("  -> a control that halves likelihood cannot remove a high-severity")
    print("     hazard; only removing the exposure can.")

    section("3. Check-in arithmetic for a 14-day campaign")
    campaign_days = 14.0
    p_miss = 0.02  # SYNTHETIC probability of one omitted or missed check-in
    print(f"  campaign = {campaign_days:.0f} days; probability that a single")
    print(f"  check-in is missed = {p_miss:.2f} per check-in (chosen)")
    print(f"  {'interval (h)':>12s} {'check-ins':>10s} {'expected missed':>16s}"
          f" {'P(>=1 alarm)':>13s}")
    for tau in (4.0, 8.0, 12.0, 24.0):
        n = campaign_days * 24.0 / tau
        expected_missed = n * p_miss
        p_any = 1.0 - (1.0 - p_miss) ** n
        print(f"  {tau:12.0f} {n:10.0f} {expected_missed:16.2f} "
              f"{p_any:13.3f}")
    print("  -> shortening the interval raises the number of chances to raise a")
    print("     false alarm faster than it raises the chance of a real one.")

    section("4. Detection delay implied by the check-in interval")
    grace = 2.0    # hours of grace before escalation (chosen)
    window = 10.0  # hours of useful rescue window (chosen)
    print(f"  escalation grace = {grace:.0f} h, useful rescue window = "
          f"{window:.0f} h")
    print(f"  {'interval (h)':>12s} {'mean wait (h)':>13s} {'mean delay (h)':>15s}"
          f" {'P(inside window)':>17s}")
    for tau in (4.0, 8.0, 12.0, 24.0):
        wait = RNG.uniform(0.0, tau, 200000).mean()
        delay = wait + grace
        p_inside = min(1.0, max(0.0, (window - grace) / tau))
        print(f"  {tau:12.0f} {wait:13.2f} {delay:15.2f} {p_inside:17.3f}")
    print("  -> the mean delay is tau/2 + grace; halving tau is the only lever")
    print("     in this model that buys rescue time.")

    print("\nSYNTHETIC: all numbers above come from chosen values in this file.")
    print("They constrain the arithmetic of a check-in protocol and nothing")
    print("about the probability of any real incident.")


if __name__ == "__main__":
    main()
