#!/usr/bin/env python3
"""Research data management plans: storage forecast, FAIR score and risk.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python research_data_management_plan_demo.py

Everything here is SYNTHETIC.  The project volumes, growth rates and checklist
weights are chosen teaching values; no funder policy is quoted and no real plan is
evaluated.

Sections
--------
1. A storage forecast over a project lifetime, with and without an archive tier.
2. FAIR readiness: what a plan scores on, and what each item buys.
3. Risk: the probability of losing an irreplaceable artefact.
4. Cost of the plan, and what the plan cannot decide.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC project model (chosen, not measured) -------------------------
YEARS = 5
RAW_TB_PER_YEAR = 8.0          # instrument output
DERIVED_TB_PER_YEAR = 3.0      # processed products
REPROCESS_FACTOR = 1.5         # extra passes stored per year
ARCHIVE_YEARS = 10             # retention after the project


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. A storage forecast")
    print(f"SYNTHETIC project: {RAW_TB_PER_YEAR:.0f} TB/year raw, "
          f"{DERIVED_TB_PER_YEAR:.0f} TB/year derived, {YEARS}-year project, "
          f"{ARCHIVE_YEARS}-year retention (chosen)")
    print("  year | raw (TB) | derived (TB) | total (TB) | cumulative (TB)")
    raw = derived = 0.0
    for year in range(1, YEARS + 1):
        raw += RAW_TB_PER_YEAR
        derived += DERIVED_TB_PER_YEAR * REPROCESS_FACTOR
        total = raw + derived
        print(f"  {year:>4d} | {raw:>8.1f} | {derived:>12.1f} | {total:>10.1f} | "
              f"{total:>14.1f}")
    project_total = raw + derived
    archived = project_total * (1 + ARCHIVE_YEARS / YEARS)
    print(f"  project total            = {project_total:.1f} TB")
    print(f"  with a {ARCHIVE_YEARS}-year archive tier = {archived:.1f} TB")
    print("  -> the archive decision multiplies the bill by "
          f"{archived / project_total:.1f}x, and it is made once, at the start")

    section("2. FAIR readiness")
    items = {
        "persistent identifier per dataset": 0.9,
        "machine-readable metadata": 0.7,
        "documented licence": 0.6,
        "versioned releases with checksums": 0.8,
        "a published data dictionary": 0.4,
        "a documented retention policy": 0.3,
    }
    print("  item                                   | readiness")
    for k, v in items.items():
        print(f"  {k:<38} | {100 * v:>7.0f} %")
    score = float(np.mean(list(items.values())))
    weakest = sorted(items.items(), key=lambda kv: kv[1])[:2]
    print(f"  mean readiness = {score:.3f}")
    print(f"  weakest two: {weakest[0][0]} ({100 * weakest[0][1]:.0f} %), "
          f"{weakest[1][0]} ({100 * weakest[1][1]:.0f} %)")
    print("  -> the score is only worth computing if each item maps to an artefact")
    print("     a reviewer can open; otherwise it measures intentions")

    section("3. Risk of losing an irreplaceable artefact")
    print("  backups | P(loss in a year) | expected artefacts lost of 20")
    for n_backups in (0, 1, 2, 3):
        p_fail = 0.02                     # per copy, per year, chosen
        p_lose = p_fail ** (n_backups + 1)
        print(f"  {n_backups:>7d} | {p_lose:>17.5f} | {20 * p_lose:>25.4f}")
    print("  -> the model's point is the exponent: one independent copy changes")
    print("     the risk by orders of magnitude, and a second adds little")
    print("  -> a copy in the same building, on the same account, or in the same")
    print("     backup rotation is not an independent copy")

    section("4. Cost of the plan and what it cannot decide")
    tb_year_cost = 25.0           # arbitrary units per TB-year, chosen
    print(f"  storage cost at {tb_year_cost:.0f} units/TB-year:")
    print(f"    project phase  = {project_total * YEARS * tb_year_cost / 2:.0f} "
          f"units (average half-full)")
    print(f"    archive phase  = {project_total * ARCHIVE_YEARS * tb_year_cost:.0f} "
          f"units")
    print(f"  efforts a plan must schedule: backups tested, metadata written,")
    print(f"  identifiers minted, retention policy reviewed")
    print("  -> a plan cannot decide the science: which derived products may be")
    print("     deleted, and which raw data must be kept forever, are research")
    print("     decisions that the plan only records")


if __name__ == "__main__":
    main()
