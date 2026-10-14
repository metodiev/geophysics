#!/usr/bin/env python3
"""Case study archetype: arid-region groundwater exploration.

Entirely SYNTHETIC.  No real basin, aquifer, borehole, yield or recharge rate is
used or implied; the lesson names settings only as argument archetypes.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_groundwater_demo.py

Print-only; no network access.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def bayes(prior, tpr, fpr):
    return prior * tpr / (prior * tpr + (1.0 - prior) * fpr)


def main():
    section("1. The base rate: how many holes are dry?")
    p = 0.15                      # SYNTHETIC prior: fraction of sites that are productive
    tpr, fpr = 0.60, 0.25         # SYNTHETIC AEM indicator performance
    print("  ARGUMENT ARCHETYPE, no site-specific numbers.")
    print(f"  prior P(productive site) = {p:.2f}")
    print(f"  AEM indicator: TPR = {tpr:.2f}, FPR = {fpr:.2f}")
    post = bayes(p, tpr, fpr)
    print(f"  posterior P(productive | AEM anomaly) = {post:.3f}")
    print(f"  so {post:.0%} of anomalies are worth drilling and {1-post:.0%} are not:")
    print(f"  the survey has improved the odds from {p:.0%} to {post:.0%}, and about")
    print("  two thirds of the holes it recommends are still dry.")
    for pp in (0.05, 0.15, 0.40):
        print(f"    prior {pp:.2f} -> posterior {bayes(pp, tpr, fpr):.3f}")

    section("2. Staged surveys: cost per productive well, not wells found")
    n_sites = 100
    cost_aem, cost_tdem, cost_well = 0.05, 0.5, 10.0     # arbitrary synthetic units
    value_well = 60.0
    tpr2, fpr2 = 0.85, 0.15      # SYNTHETIC follow-up TDEM on AEM anomalies
    print(f"  {n_sites} candidate sites; prior {p:.2f}; well cost {cost_well:.1f}, "
          f"value {value_well:.1f}")
    print(f"  AEM: TPR {tpr:.2f}/FPR {fpr:.2f}, cost {cost_aem:.2f} per site")
    print(f"  TDEM: TPR {tpr2:.2f}/FPR {fpr2:.2f}, cost {cost_tdem:.2f} per site")
    # conditional independence of the two indicators given the true state
    flag_aem = n_sites * (p * tpr + (1 - p) * fpr)
    both = n_sites * (p * tpr * tpr2 + (1 - p) * fpr * fpr2)
    found_blind = n_sites * p
    found_aem = n_sites * p * tpr
    found_both = n_sites * p * tpr * tpr2
    rows = [
        ("blind drilling", 0.0, found_blind, n_sites * cost_well),
        ("AEM then drill anomalies",
         n_sites * cost_aem, found_aem, n_sites * cost_aem + flag_aem * cost_well),
        ("AEM + TDEM then drill",
         n_sites * cost_aem + flag_aem * cost_tdem,
         found_both,
         n_sites * cost_aem + flag_aem * cost_tdem + both * cost_well),
    ]
    print("\n   strategy                       found   cost    cost/found   net value")
    for name, pre, found, cost in rows:
        net = found * value_well - cost
        print(f"   {name:29s} {found:6.2f} {cost:8.1f} {cost/found:12.2f} "
              f"{net:11.1f}")
    print(f"\n  AEM alone finds the most productive wells; AEM + TDEM gives the lowest")
    print(f"  cost per productive well and the highest net value, because the")
    print(f"  expensive drilling is spent on the smallest, best-selected set.")
    print("  Maximising the number of wells found is NOT the objective.")

    section("3. Sustainability: what the geophysics cannot measure")
    rainfall = 0.20              # m/yr (synthetic arid-region teaching value)
    recharge_coeff = 0.05        # fraction of rainfall that becomes recharge
    area = 500e6                 # m^2 (500 km^2)
    recharge = rainfall * recharge_coeff * area
    abstraction_well = 0.5e6     # m^3/yr per well (synthetic)
    print(f"  rainfall {rainfall*1000:.0f} mm/yr, recharge coefficient "
          f"{recharge_coeff:.2f} -> recharge {recharge/1e6:.2f} Mm^3/yr over "
          f"{area/1e6:.0f} km^2")
    print(f"  abstraction per well {abstraction_well/1e6:.1f} Mm^3/yr")
    print(f"  wells supportable at steady state = {recharge/abstraction_well:.1f}")
    storage = 100e6              # m^3 (synthetic)
    for n_wells in (5.0, 10.0, 20.0):
        pump = n_wells * abstraction_well
        if pump <= recharge:
            print(f"    {n_wells:5.0f} wells: pump {pump/1e6:.1f} Mm^3/yr <= recharge; "
                  f"no net loss from storage at this estimated recharge")
        else:
            years = storage / (pump - recharge)
            print(f"    {n_wells:5.0f} wells: pump {pump/1e6:.1f} Mm^3/yr; storage "
                  f"({storage/1e6:.0f} Mm^3) drawn down in {years:5.1f} years")
    print("\n  Recharge is estimated from rainfall and a coefficient, not measured by")
    print("  a geophysical survey: the survey finds water, the water balance decides")
    print("  how long it lasts.  Both must be reported, and they are different")
    print("  uncertainties.")

    section("4. Value of information per well")
    print("  the survey's value is the reduction in expected cost, not the anomalies")
    p_low = 0.15
    post_hi = bayes(p_low, tpr, fpr)
    cost_dry = cost_well
    cost_value = value_well
    ev_blind = p_low * cost_value - cost_dry
    # survey all sites, then drill only the anomalies
    p_flag = p_low * tpr + (1 - p_low) * fpr
    ev_survey = -cost_aem + p_flag * (post_hi * cost_value - cost_dry)
    print(f"  drill every site: EV = {ev_blind:+.2f} units per site")
    print(f"  survey then drill anomalies: EV = {ev_survey:+.2f} units per site")
    print(f"  VOI = {ev_survey - ev_blind:+.2f} units per site "
          f"({(ev_survey-ev_blind)/cost_aem:+.1f} x the survey cost)")
    print("  Note the accounting includes the productive wells that are MISSED: a")
    print("  screening survey's benefit is not 'holes saved' but the change in the")
    print("  expected value of the whole programme.")
    print("\n  All models and data in this module are SYNTHETIC.")


if __name__ == "__main__":
    main()
