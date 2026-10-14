#!/usr/bin/env python3
"""Case study archetype: basin analysis and play assessment.

Entirely SYNTHETIC.  No real basin, play, field, well or resource number is used
or implied; the lesson names settings only as argument archetypes.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_basin_demo.py

Print-only; no network access.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def play_chance_independent(probs):
    p = 1.0
    for q in probs:
        p *= q
    return p


def play_chance_correlated(probs, rho, n=200000):
    """Monte-Carlo joint probability with a shared common risk factor.

    Element i is present when sqrt(rho)*Z + sqrt(1-rho)*e_i > z_i, where z_i is
    the standard-normal quantile of the marginal probability.  rho = 0 gives
    independence; rho = 1 makes every element move together.
    """
    from scipy.stats import norm
    z = norm.ppf(1.0 - probs)   # upper-tail quantile: P(Z > z) = p
    a = np.sqrt(rho)
    common = RNG.standard_normal(n)
    ok = np.ones(n, dtype=bool)
    for zi in z:
        ok &= (a * common + np.sqrt(1.0 - a ** 2) * RNG.standard_normal(n)) > zi
    return ok.mean()


def main():
    section("1. Play chance: five elements, one of them usually shared")
    probs = np.array([0.60, 0.70, 0.80, 0.75, 0.85])   # SYNTHETIC element chances
    names = ["source", "reservoir", "seal", "trap", "timing"]
    print("  ARGUMENT ARCHETYPE, no site-specific numbers.")
    for name, q in zip(names, probs):
        print(f"    P({name:9s}) = {q:.2f}")
    ind = play_chance_independent(probs)
    print(f"\n  independent product of the five = {ind:.4f}")
    for rho in (0.2, 0.4, 0.6):
        pc = play_chance_correlated(probs, rho)
        print(f"  shared-risk-factor rho = {rho:.1f} -> joint chance = {pc:.4f} "
              f"({pc/ind:.2f} x the independent value)")
    print("\n  Correlated elements (a single thermal or tectonic history that")
    print("  controls source, seal and timing together) raise the joint chance: the")
    print("  elements are more likely to be present or absent as a group.  The")
    print("  independent product is not a conservative default; it is a model.")

    section("2. A seismic amplitude anomaly is a test, not a result")
    prior = 0.25                    # SYNTHETIC prior chance of hydrocarbons
    tpr, fpr = 0.80, 0.35           # P(anomaly | HC) and P(anomaly | brine)
    ppv = prior * tpr / (prior * tpr + (1 - prior) * fpr)
    print(f"  prior P(hydrocarbons) = {prior:.2f}")
    print(f"  P(amplitude anomaly | hydrocarbons) = {tpr:.2f}")
    print(f"  P(amplitude anomaly | brine sand)   = {fpr:.2f}")
    print(f"  posterior P(hydrocarbons | anomaly) = {ppv:.3f}")
    print(f"  of 100 amplitude anomalies, {ppv*100:.0f} are hydrocarbons and "
          f"{(1-ppv)*100:.0f} are brine or lithology:")
    print("  the anomaly is a genuine test, and a third of the prospects it flags")
    print("  are still dry.")
    for p in (0.10, 0.25, 0.50):
        po = p * tpr / (p * tpr + (1 - p) * fpr)
        print(f"    prior {p:.2f} -> posterior {po:.3f}")

    section("3. Expected value of a wildcat, with an uncertain resource")
    p_success = ppv
    p50, p90 = 20.0, 5.0            # arbitrary synthetic resource units, P50/P90
    mu = np.log(p50)
    sigma = (np.log(p50) - np.log(p90)) / 1.2816
    draws = RNG.lognormal(mu, sigma, 400000)
    value_per_unit = 1.0
    cost = 12.0                     # arbitrary synthetic cost units
    net = value_per_unit * draws - cost
    gross_mean = (value_per_unit * draws).mean()
    emv = p_success * gross_mean - cost          # EMV = q E[Vgross] - C
    print(f"  P(commercial) = {p_success:.3f}")
    print(f"  resource distribution: P50 = {p50:.0f}, P90 = {p90:.0f} "
          f"(lognormal, sigma = {sigma:.3f} in log space)")
    print(f"  mean GROSS value of a success = {gross_mean:.2f} units, "
          f"well cost = {cost:.1f} units")
    print(f"  expected monetary value = q E[V] - C = {emv:.2f} units")
    break_even_p = cost / gross_mean
    print(f"  break-even P(commercial) = cost / mean value = {break_even_p:.3f}")
    print(f"  probability the well loses money even if it is a discovery: "
          f"{(net < 0).mean():.3f}")
    print("\n  The last line is the one usually omitted: a discovery that is too")
    print("  small to pay for its own development still loses money, so 'success'")
    print("  and 'profit' are different random variables.")

    section("4. Value of information of an additional survey")
    print("  decision tree: drill, do not drill, or survey first and decide")
    tpr_s, fpr_s = 0.75, 0.20       # SYNTHETIC additional (for example CSEM) survey
    cost_survey = 1.5               # arbitrary synthetic units
    gross = draws.mean()            # mean gross value of a success
    print(f"  survey: TPR = {tpr_s:.2f}, FPR = {fpr_s:.2f}, cost = "
          f"{cost_survey:.1f} units")
    print(f"  mean gross value of a success = {gross:.2f} units, well cost = "
          f"{cost:.1f} units")
    print("\n   prior    EV blind    P(pos)   EV survey    VOI    action")
    for p in (0.05, 0.15, 0.30, 0.50):
        ev_blind = max(0.0, p * gross - cost)
        p_pos = p * tpr_s + (1 - p) * fpr_s
        post_pos = p * tpr_s / p_pos
        post_neg = p * (1 - tpr_s) / (1 - p_pos)
        ev_pos = max(0.0, post_pos * gross - cost)
        ev_neg = max(0.0, post_neg * gross - cost)
        ev_survey = -cost_survey + p_pos * ev_pos + (1 - p_pos) * ev_neg
        action = "wasted" if (ev_pos > 0) == (ev_neg > 0) and (ev_blind > 0) == (ev_pos > 0) else "decision-flipping"
        print(f"   {p:5.2f}   {ev_blind:9.2f}   {p_pos:7.3f}   {ev_survey:9.2f}   "
              f"{ev_survey-ev_blind:6.2f}   {action}")
    print("\n  The survey pays only at an INTERMEDIATE prior, where it can flip the")
    print("  decision: at a very low prior no result justifies a well, and at a high")
    print("  prior a well is drilled whatever the survey says.  Value of information")
    print("  is a property of the DECISION, not of the instrument.")

    print("\n  All models and data in this module are SYNTHETIC.")


if __name__ == "__main__":
    main()
