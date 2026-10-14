#!/usr/bin/env python3
"""Open science practice: adoption, reuse and credit, SYNTHETIC.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python open_science_practice_demo.py

Everything here is SYNTHETIC.  The adoption curve, reuse rates and citation multiplier
are chosen teaching values; no bibliometric database was queried and no measured effect
of open practice on citations is claimed.

Sections
--------
1. Adoption of an open-release policy across a community (logistic curve).
2. Reuse: how many downstream works use a released dataset.
3. Credit: citation accrual with and without an open release.
4. The cost side: preparing a release, and what it buys.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC community and credit model (chosen, not measured) ------------
N_GROUPS = 200
ADOPTION_RATE = 0.35        # logistic steepness per year
T0 = 5.0                    # midpoint year of adoption
REUSE_PER_YEAR = 0.08       # downstream works per group per year, if open
MULTIPLIER = 1.25           # citation multiplier for open releases (chosen)
BASE_CITES = 12.0           # citations per year for the method paper
GROWTH = 0.15


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def logistic(t, n, rate, t0):
    return n / (1.0 + np.exp(-rate * (t - t0)))


def main():
    section("1. Adoption of an open-release policy")
    years = np.arange(0, 16)
    adopted = logistic(years, N_GROUPS, ADOPTION_RATE, T0)
    print(f"SYNTHETIC community: {N_GROUPS} groups, logistic adoption with "
          f"rate {ADOPTION_RATE:.2f}/yr, midpoint year {T0:.0f} (chosen)")
    print("  year | groups releasing openly | share")
    for y, a in zip(years, adopted):
        if y % 3 == 0:
            print(f"  {y:>4d} | {a:>24.1f} | {100 * a / N_GROUPS:>5.1f} %")
    print("  -> adoption is slow then fast then saturating; a policy's effect on")
    print("     the community is dominated by the midpoint, not the steepness")

    section("2. Reuse of a released dataset")
    print("  year | releasing groups | downstream works that year")
    total_reuse = 0.0
    for y, a in zip(years, adopted):
        reuse = a * REUSE_PER_YEAR
        total_reuse += reuse
        if y % 3 == 0:
            print(f"  {y:>4d} | {a:>16.1f} | {reuse:>27.1f}")
    print(f"  cumulative downstream works over 15 years = {total_reuse:.0f}")
    print("  -> reuse is a property of the community's adoption, so one group's")
    print("     release matters less than a shared practice; the number to report")
    print("     is the community total with its assumption stated")

    section("3. Credit: citation accrual with and without an open release")
    print(f"  model: {BASE_CITES:.0f} citations/year growing at {GROWTH:.2f}/yr,")
    print(f"  with a {MULTIPLIER:.2f}x multiplier for an open release (chosen)")
    print("  year | closed | open | difference")
    closed = open_ = 0.0
    for year in range(0, 11):
        c = BASE_CITES * np.exp(GROWTH * year)
        closed += c
        open_ += c * MULTIPLIER
        if year % 2 == 0:
            print(f"  {year:>4d} | {closed:>6.1f} | {open_:>5.1f} | "
                  f"{open_ - closed:>10.1f}")
        if year == 3:
            early_closed = closed
    print(f"  after 10 years: closed {closed:.0f}, open {open_:.0f} "
          f"({100 * (open_ / closed - 1):.0f} % more)")
    print(f"  the multiplier's effect is cumulative, not multiplicative on the")
    print("  final year: it compounds with the growth curve")

    section("4. The cost side")
    costs = {"preparing a release (formatting, metadata, docs)": 60.0,
             "archiving with an identifier": 4.0,
             "answering user questions in year 1": 20.0,
             "maintaining the release for ten years": 25.0}
    print("  effort item                                  | hours (chosen)")
    for k, v in costs.items():
        print(f"  {k:<44} | {v:>13.0f}")
    total = sum(costs.values())
    print(f"  total = {total:.0f} hours, about {total / 8:.0f} working days")
    print("  -> the release is an artefact with a cost and a benefit; a plan that")
    print("     states both is defensible, one that claims only the benefit is not")


if __name__ == "__main__":
    main()
