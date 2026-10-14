#!/usr/bin/env python3
"""Documentation coverage and documentation rot on a SYNTHETIC API.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python documentation_demo.py

Everything here is SYNTHETIC.  The API surface, the change rate and the update
rate are chosen; no repository is parsed and no survey of documentation practice
is quoted.

Sections
--------
1. Coverage at the start: documented, undocumented and signature drift.
2. Rot over eight releases: coverage, staleness and accuracy.
3. What a documentation test suite buys.
4. The cost of a stale parameter list, in reader-minutes.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC documentation model (chosen, not measured) -------------------
N_FUNCS = 120
INITIAL_COVERAGE = 0.72
NEW_PER_RELEASE = 4
P_SIGNATURE_CHANGE = 0.15
P_UPDATE_WHEN_CHANGED = 0.55
RELEASES = 8
READER_MINUTES_PER_STALE = 12.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. Starting point of the synthetic API")
    documented = RNG.random(N_FUNCS) < INITIAL_COVERAGE
    stale = np.zeros(N_FUNCS, dtype=bool)
    print(f"SYNTHETIC API: {N_FUNCS} public functions, initial coverage target "
          f"{INITIAL_COVERAGE:.2f} (chosen)")
    print(f"  documented at release 0 = {int(documented.sum())} "
          f"({100.0 * documented.mean():.1f} %)")
    print(f"  undocumented            = {int((~documented).sum())} "
          f"({100.0 * (~documented).mean():.1f} %)")

    section("2. Rot over eight releases")
    print("  release | functions | documented % | stale % | accurate %")
    history = []
    for release in range(1, RELEASES + 1):
        n_now = documented.size
        changed = RNG.random(n_now) < P_SIGNATURE_CHANGE
        updated = RNG.random(n_now) < P_UPDATE_WHEN_CHANGED
        stale = np.where(documented & changed & ~updated, True, stale)
        stale = np.where(documented & changed & updated, False, stale)
        new_doc = RNG.random(NEW_PER_RELEASE) < 0.5
        documented = np.concatenate([documented, new_doc])
        stale = np.concatenate([stale, np.zeros(NEW_PER_RELEASE, dtype=bool)])
        n = documented.size
        coverage = 100.0 * documented.mean()
        stale_pct = 100.0 * stale.mean()
        accurate = coverage - stale_pct
        history.append((release, n, coverage, stale_pct, accurate))
        print(f"  {release:>7d} | {n:>9d} | {coverage:>12.1f} | "
              f"{stale_pct:>7.1f} | {accurate:>10.1f}")
    acc = np.array([h[4] for h in history])
    ratio = (1.0 - P_UPDATE_WHEN_CHANGED) / P_UPDATE_WHEN_CHANGED
    print(f"  accurate documentation decays from {acc[0]:.1f} % to "
          f"{acc[-1]:.1f} % with no maintenance effort beyond acceptance")
    print(f"  long-run model limit: stale/documented = (1-u)/u = "
          f"{1.0 - P_UPDATE_WHEN_CHANGED:.2f}/{P_UPDATE_WHEN_CHANGED:.2f} = "
          f"{ratio:.3f}, i.e. {100.0 * ratio:.1f} % of documented functions stale")
    print(f"  at the modelled coverage that is "
          f"{100.0 * ratio * history[-1][2] / 100.0:.1f} % of all functions; "
          f"eight releases are still in the transient")
    print("  -> coverage is a snapshot; accuracy is the quantity that decays")

    section("3. What a documentation test suite buys")
    print("  model: a doctest/example runner catches a stale signature with "
          "probability 0.70 per release (chosen)")
    caught = 0.70
    stale_after = np.array([h[3] for h in history])
    print(f"  stale fraction without tests at release {RELEASES} = "
          f"{stale_after[-1]:.1f} %")
    residual = stale_after[-1] * (1.0 - caught)
    print(f"  stale fraction with tests (residual)                = "
          f"{residual:.1f} %")
    print(f"  stale documentation avoided                        = "
          f"{stale_after[-1] - residual:.1f} percentage points")

    section("4. Reader cost of stale documentation")
    consulted = 0.10   # fraction of stale docstrings a reader actually relies on
    minutes = (stale_after[-1] / 100.0) * documented.size * \
        READER_MINUTES_PER_STALE * consulted
    print(f"  assumptions: {READER_MINUTES_PER_STALE:.0f} reader-minutes lost per "
          f"consulted stale function, and {consulted:.0%} of stale docstrings are "
          f"consulted before the error is noticed (chosen)")
    print(f"  functions documented and stale at release {RELEASES} = "
          f"{stale_after[-1] / 100.0 * documented.size:.1f}")
    print(f"  lost minutes for one team pass through the API = {minutes:.0f} min "
          f"= {minutes / 60.0:.1f} h")
    print("  -> the number is a model output; it says the cost is real and "
          "recurring, not that it equals this value")


if __name__ == "__main__":
    main()
