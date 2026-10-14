#!/usr/bin/env python3
"""Licence compatibility, version constraints and software citation accounting.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python licensing_and_citation_demo.py

Everything here is SYNTHETIC.  The licence table is a small teaching model of
well-known licence families, the release lists are generated, and the citation
curve is a deterministic growth model with chosen parameters.  No legal advice is
given and no citation database is queried.

Sections
--------
1. Combining two pieces of code: which combined licence is forced.
2. Version-constraint arithmetic on a generated release list.
3. Citation accounting for a software paper and a software DOI.
4. Time for a software citation count to reach a threshold.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC / illustrative licence model (see the lesson's caveat) -------
LICENCES = {
    "MIT":          {"copyleft": "none",     "network": False},
    "BSD-3-Clause": {"copyleft": "none",     "network": False},
    "Apache-2.0":   {"copyleft": "none",     "network": False},
    "MPL-2.0":      {"copyleft": "file",     "network": False},
    "LGPL-3.0":     {"copyleft": "library",  "network": False},
    "GPL-3.0":      {"copyleft": "strong",   "network": False},
    "AGPL-3.0":     {"copyleft": "strong",   "network": True},
}
STRENGTH = {"none": 0, "file": 1, "library": 2, "strong": 3}


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def combined(a, b):
    """Combined-work licence forced by mixing code under licences a and b."""
    if a == "GPL-2.0" or b == "GPL-2.0":
        return "GPL-2.0 (Apache-2.0 is incompatible; see SPDX notes)"
    net = LICENCES[a]["network"] or LICENCES[b]["network"]
    level = max(STRENGTH[LICENCES[a]["copyleft"]], STRENGTH[LICENCES[b]["copyleft"]])
    if level == 3:
        return "AGPL-3.0" if net else "GPL-3.0"
    if level == 2:
        return "LGPL-3.0"
    if level == 1:
        return "MPL-2.0"
    return "any permissive licence (e.g. MIT)"


def parse_version(v):
    return tuple(int(part) for part in v.split("."))


def satisfies(version, constraint):
    parts = parse_version(version)
    if constraint.startswith("^"):
        lo = parse_version(constraint[1:])
        return parts >= lo and parts[0] == lo[0]
    if constraint.startswith("~"):
        lo = parse_version(constraint[1:])
        return parts >= lo and parts[:2] == lo[:2]
    if constraint.startswith(">="):
        lo, hi = constraint[2:].split(",<")
        return parse_version(lo) <= parts < parse_version(hi)
    raise ValueError(f"unsupported constraint: {constraint}")


def main():
    section("1. Combining two pieces of code: the forced combined licence")
    names = list(LICENCES)
    print("SYNTHETIC licence model (teaching values; check the actual licence "
          "text and SPDX compatibility notes before relying on this)")
    print("  code A      | code B      | combined-work licence")
    for a in ("MIT", "Apache-2.0", "MPL-2.0", "LGPL-3.0", "GPL-3.0", "AGPL-3.0"):
        for b in ("MIT", "Apache-2.0", "GPL-3.0", "AGPL-3.0"):
            print(f"  {a:<11} | {b:<11} | {combined(a, b)}")
    permissive = sum(1 for a in names for b in names
                     if STRENGTH[LICENCES[a]["copyleft"]] == 0
                     and STRENGTH[LICENCES[b]["copyleft"]] == 0)
    pairs = len(names) ** 2
    print(f"  fully permissive pairs = {permissive}/{pairs} "
          f"({100.0 * permissive / pairs:.0f} %) of the modelled table")

    section("2. Version-constraint arithmetic on a generated release list")
    releases = [f"{major}.{minor}.{patch}"
                for major in (1, 2) for minor in range(4) for patch in (0, 3)]
    print(f"  release list = {releases}")
    for constraint in ("^1.2", "~1.2", ">=2.0,<3"):
        ok = [v for v in releases if satisfies(v, constraint)]
        print(f"  constraint {constraint:<10} -> {len(ok)} of {len(releases)} "
              f"releases: {ok}")
    unconstrained = [v for v in releases if satisfies(v, "^1.2")]
    print("  -> an unpinned environment resolves to the highest release that "
          "satisfies the constraint; the number of admissible releases is the "
          "size of the search the solver performs")

    section("3. Citation accounting for software")
    years = 6
    c0 = 8.0             # citations in the first year (chosen)
    growth = 0.35        # exponential growth per year (chosen)
    software_share = 0.40  # fraction of credit to the software DOI (chosen)
    per_year = c0 * np.exp(growth * np.arange(years))
    cumulative = np.cumsum(per_year)
    print(f"  model: {c0:.0f} citations in year 1, {growth:.2f}/yr growth, "
          f"{software_share:.0%} to the software DOI (chosen)")
    print("  year | citations/yr | cumulative | software-DOI credit")
    for i, c in enumerate(per_year, start=1):
        print(f"  {i:>4d} | {c:>12.1f} | {cumulative[i - 1]:>10.1f} | "
              f"{cumulative[i - 1] * software_share:>18.1f}")
    print(f"  cumulative citations after {years} years = {cumulative[-1]:.1f} "
          f"(model output)")

    section("4. Time to reach a citation threshold")
    ratio = np.exp(growth) - 1.0
    print(f"  model: citations in year t = {c0:.0f} exp({growth:.2f} (t-1)), "
          "cumulative = geometric sum (chosen parameters)")
    for target in (25.0, 50.0, 100.0):
        years = np.log(1.0 + target * ratio / c0) / growth
        print(f"  target {target:>5.0f} cumulative citations -> year "
              f"{years:>4.1f}")
    print("  -> a citation threshold and the year it is reached are both "
          "functions of the growth assumption; reporting either without the "
          "other is not informative")


if __name__ == "__main__":
    main()
