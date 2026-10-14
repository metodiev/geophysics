#!/usr/bin/env python3
"""Data ethics: disclosure risk and utility of an aggregated release.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_ethics_geoscience_demo.py

Everything here is SYNTHETIC.  The sites, their locations and the aggregation grid
are generated below; no real survey, community or cultural site is represented.

Sections
--------
1. The synthetic survey and the release problem.
2. Disclosure risk and utility at four cell sizes.
3. Small-cell suppression: what k does to both columns.
4. What this arithmetic does not decide.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N_RECORDS = 800         # surveyed sites or households
REGION_KM = 20.0        # square region, km
N_VILLAGES = 30         # settlements the records cluster around
CELL_SIZES = (1.0, 2.0, 5.0, 10.0)
K_VALUES = (1, 5, 10)
VILLAGE_SD_KM = 2.0


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    section("1. The synthetic survey and the release problem")
    centres = RNG.uniform(2.0, REGION_KM - 2.0, size=(N_VILLAGES, 2))
    which = RNG.integers(0, N_VILLAGES, N_RECORDS)
    xy = centres[which] + VILLAGE_SD_KM * RNG.standard_normal((N_RECORDS, 2))
    xy = np.clip(xy, 0.0, REGION_KM - 1e-9)
    print(f"SYNTHETIC survey: {N_RECORDS} records in a "
          f"{REGION_KM:.0f} x {REGION_KM:.0f} km region")
    print(f"  records cluster around {N_VILLAGES} settlements with a spread of "
          f"{VILLAGE_SD_KM:.1f} km")
    print("  the release question: at what spatial resolution can the data be")
    print("  published without identifying individuals, and what does the")
    print("  aggregation cost in utility?")
    print("  the arithmetic below measures ONE narrow quantity -- the")
    print("  k-anonymity of a spatial count release -- and it cannot decide the")
    print("  governance question of whether the data should be released at all")

    section("2. Disclosure risk and utility at four cell sizes")
    print(f"  {'cell size':>10s} {'occupied':>9s} {'mean count':>11s} "
          f"{'singletons':>11s} {'records in singletons':>22s}")
    for size in CELL_SIZES:
        n_cells = int(REGION_KM / size)
        ix = np.minimum((xy[:, 0] / size).astype(int), n_cells - 1)
        iy = np.minimum((xy[:, 1] / size).astype(int), n_cells - 1)
        flat = ix * n_cells + iy
        counts = np.bincount(flat, minlength=n_cells * n_cells)
        occupied = counts[counts > 0]
        singletons = int(np.sum(occupied == 1))
        records_in_singletons = int(occupied[occupied == 1].sum())
        print(f"  {size:>7.1f} km {occupied.size:>9d} {occupied.mean():>11.2f} "
              f"{singletons:>11d} {records_in_singletons:>22d}")
    print("  the finer the grid, the more cells hold a single record: at 1 km,")
    print("  79 of 286 occupied cells hold exactly one record, and a count of 1")
    print("  is a direct pointer to one household once an auxiliary address list")
    print("  is available.  At 2 km there are still 11 such cells; by 5 km there")
    print("  are none, because the mean cell holds 50 records")
    print("  coarsening the grid is therefore the single most effective control,")
    print("  and it costs exactly the local structure an analysis of a")
    print("  neighbourhood or a village would need -- the trade the next section")
    print("  quantifies")

    section("3. Small-cell suppression: what k does to both columns")
    print(f"  {'cell':>6s} {'k':>3s} {'cells suppressed':>17s} "
          f"{'records suppressed':>19s} {'records retained':>17s}")
    for size in CELL_SIZES:
        n_cells = int(REGION_KM / size)
        ix = np.minimum((xy[:, 0] / size).astype(int), n_cells - 1)
        iy = np.minimum((xy[:, 1] / size).astype(int), n_cells - 1)
        flat = ix * n_cells + iy
        counts = np.bincount(flat, minlength=n_cells * n_cells)
        occupied = counts[counts > 0]
        for k in K_VALUES:
            small = (counts > 0) & (counts < k)
            suppressed_cells = int(small.sum())
            suppressed_records = int(counts[small].sum())
            retained = N_RECORDS - suppressed_records
            print(f"  {size:>4.0f} km {k:>3d} {suppressed_cells:>17d} "
                  f"{suppressed_records:>19d} {retained:>17d} "
                  f"({100 * retained / N_RECORDS:>5.1f}%)")
    print("  with k = 5, suppression removes 540 of the 800 records at 1 km but")
    print("  none at all at 5 km or 10 km; with k = 10 it leaves 10 records (1.2%)")
    print("  at 1 km, which is a useless release")
    print("  so at fine resolution suppression cannot be both protective and")
    print("  useful: the choice is between a coarse release, a restricted release")
    print("  (controlled access), and no release.  That is the finding, and it is")
    print("  a finding about the data, not about the intent")
    print("  the k-anonymity guarantee is also weaker than it sounds: it")
    print("  protects against the release alone, not against an adversary who")
    print("  holds an auxiliary list of locations, and it says nothing about")
    print("  inference from the totals that remain")

    section("4. What this arithmetic does not decide")
    print("  - whose consent governs the release, and whether consent was")
    print("    obtained for this use rather than for the original survey")
    print("  - whether the community or nation whose territory the region is")
    print("    holds data sovereignty, and what conditions it attaches")
    print("  - whether the site locations are themselves sensitive (cultural,")
    print("    sacred or archaeological sites are not protected by counting)")
    print("  - who benefits from the analysis, and whether the benefit reaches")
    print("    the people the data describe")
    print("  these are governance questions, answered by agreement with the")
    print("  data holders and communities, not by a privacy metric.  The demo")
    print("  measures what a release costs in disclosure and utility so that the")
    print("  agreement can be made with the numbers on the table -- and it")
    print("  stops there")
    print("\nSYNTHETIC: these records, locations and settlements are generated by")
    print("this script.  No real community, site or survey is described, and the")
    print("numbers are properties of this generator only.")


if __name__ == "__main__":
    main()
