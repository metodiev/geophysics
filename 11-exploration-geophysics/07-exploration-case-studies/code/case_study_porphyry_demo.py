#!/usr/bin/env python3
"""Case study archetype: a porphyry-copper district.

This demonstration carries the quantitative content of the lesson.  It is
entirely SYNTHETIC: no real deposit, district, company, hole or grade is used or
implied.  The lesson names settings only as argument archetypes and quotes no
site-specific number.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_porphyry_demo.py

Print-only; no network access.
"""

import numpy as np
from scipy.stats import norm

RNG = np.random.default_rng(20261014)

MU0_OVER_4PI = 1.0e-7


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def posterior(prior, tpr, fpr):
    """P(target | positive indicator) for a single binary indicator."""
    return prior * tpr / (prior * tpr + (1.0 - prior) * fpr)


def likelihood_ratio(tpr, fpr):
    return tpr / fpr


def main():
    section("1. Prospectivity: the prior does the work")
    print("  ARGUMENT ARCHETYPE, no site-specific data.  The base rate p is the")
    print("  fraction of drilled targets of this type that prove economic.")
    tpr, fpr = 0.70, 0.15       # SYNTHETIC indicator: an IP chargeability high
    print(f"  indicator: IP chargeability high; TPR = {tpr:.2f}, FPR = {fpr:.2f}")
    print(f"  likelihood ratio = TPR/FPR = {likelihood_ratio(tpr, fpr):.2f}")
    print("\n   prior p    posterior    targets per discovery   discovery per target")
    for p in (0.002, 0.01, 0.05, 0.20):
        post = posterior(p, tpr, fpr)
        print(f"   {p:7.3f}    {post:8.4f}    {1.0/post:20.1f}    {post:20.3f}")
    print("\n  The same survey, with the same detection performance, is a discovery")
    print("  machine in a fertile belt and a hole-making machine in a poor one.")

    section("2. Combining indicators: independence is an assumption")
    print("  three indicators, each with TPR/FPR = 0.70/0.15")
    prior = 0.02
    lr = likelihood_ratio(0.70, 0.15)
    print(f"  prior = {prior:.3f}")
    for n in (1, 2, 3):
        odds = (prior / (1 - prior)) * lr ** n
        post_ind = odds / (1 + odds)
        # correlated: the n-th indicator adds only a fraction rho of the
        # independent information, expressed as lr^(rho^n)
        for rho, tag in ((1.0, "independent"), (0.5, "half-independent"),
                         (0.25, "strongly correlated")):
            eff = lr ** (sum(rho ** k for k in range(1, n + 1)))
            odds_c = (prior / (1 - prior)) * eff
            post_c = odds_c / (1 + odds_c)
            print(f"    n = {n}, {tag:19s}: posterior = {post_c:.4f}")
        print(f"    (fully independent reference: {post_ind:.4f})")
    print("\n  Correlated indicators — a magnetic high that is also the radiometric")
    print("  high because both come from the same intrusive body — overstate the")
    print("  posterior if they are treated as independent.  The bias grows with n.")

    section("3. Deposit-scale magnetics: depth from a profile, and its ambiguity")
    x = np.linspace(-400.0, 400.0, 81)
    print("  two SYNTHETIC sources of the same peak amplitude (teaching shapes):")
    print("  a vertical dipole (compact body, ~ z^-3) and a horizontal cylinder (~ z^-2)")
    amp, z_true = 500.0, 150.0       # nT and m
    prof_p = amp * z_true ** 3 / (x ** 2 + z_true ** 2) ** 1.5
    prof_c = amp * z_true ** 2 / (x ** 2 + z_true ** 2)
    # fit each model to the other profile by least squares on depth
    zs = np.linspace(20.0, 600.0, 400)
    chi_p = np.array([np.sum((amp * z ** 3 / (x ** 2 + z ** 2) ** 1.5
                              - prof_c) ** 2) for z in zs])
    chi_c = np.array([np.sum((amp * z ** 2 / (x ** 2 + z ** 2)
                              - prof_p) ** 2) for z in zs])
    z_fit_p = zs[chi_p.argmin()]
    z_fit_c = zs[chi_c.argmin()]
    print(f"\n  true depth {z_true:.0f} m")
    print(f"  fitting a COMPACT (z^-3) model to a CYLINDER (z^-2) profile gives "
          f"z = {z_fit_p:.1f} m")
    print(f"  fitting a CYLINDER model to a COMPACT profile gives z = {z_fit_c:.1f} m")
    print("  The depth error from the wrong shape is tens of per cent, larger than")
    print("  the picking error: the geological model, not the instrument, sets it.")

    section("4. The drilling decision")
    post = posterior(0.02, 0.70, 0.15)
    cost_hole = 1.0            # arbitrary synthetic cost units
    value_hit = 40.0           # arbitrary synthetic value units (net present)
    print(f"  posterior probability of an economic discovery at the target = "
          f"{post:.4f}")
    print(f"  hole cost = {cost_hole:.1f} units, net value of a discovery = "
          f"{value_hit:.1f} units")
    print(f"  expected value of drilling = {post*value_hit - cost_hole:+.2f} units")
    break_even = cost_hole / value_hit
    print(f"  break-even posterior = cost/value = {break_even:.4f}")
    print(f"  the survey must lift the prior above {break_even:.4f} to justify a hole:")
    for p in (0.002, 0.01, 0.02, 0.05):
        po = posterior(p, 0.70, 0.15)
        print(f"    prior {p:.3f} -> posterior {po:.4f} -> EV "
              f"{po*value_hit - cost_hole:+.2f} units "
              f"({'drill' if po > break_even else 'do not drill'})")
    print("\n  A district programme can still be worth running on a low prior if the")
    print("  programme's cost per hole falls and the discovery value rises, or if a")
    print("  cheaper early indicator lifts the prior before the expensive test.")
    print("\n  All models and data in this module are SYNTHETIC.")


if __name__ == "__main__":
    main()
