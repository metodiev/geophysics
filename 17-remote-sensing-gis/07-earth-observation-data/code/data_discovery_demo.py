#!/usr/bin/env python3
"""Data discovery: searching a SYNTHETIC metadata catalogue, and what metadata
error does to precision and recall.  Licensing is treated as a filter.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_discovery_demo.py

Everything here is SYNTHETIC.  The catalogue, its spatial footprints, its
metadata errors and its licence codes are chosen teaching values, not a real
archive, portal or licence text.  No file is read or written and no network
access is used.

Contents
--------
1. Build a synthetic catalogue and print a few records.
2. A spatial + temporal query measured against ground truth: precision, recall.
3. How metadata error degrades a query.
4. Licences in a result set: access is not redistribution.
5. Why exact discovery needs identifiers, not descriptions.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N_RECORDS = 200
REGION_KM = 100.0          # catalogue spans a 100 km x 100 km area
DAY_MAX = 730              # two years of day index


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def bbox_intersects(a, b):
    """True where axis-aligned boxes a and b overlap.  a, b: (n, 4) x0,y0,x1,y1."""
    return ~((a[:, 2] < b[0]) | (a[:, 0] > b[2])
             | (a[:, 3] < b[1]) | (a[:, 1] > b[3]))


def build_catalogue(sigma_km):
    """Synthetic records with a TRUE footprint and a REPORTED (noisy) footprint."""
    cx = RNG.uniform(0.0, REGION_KM, N_RECORDS)
    cy = RNG.uniform(0.0, REGION_KM, N_RECORDS)
    half = RNG.uniform(3.0, 12.0, N_RECORDS)
    true_box = np.column_stack([cx - half, cy - half, cx + half, cy + half])
    # metadata is a measurement too: the reported centre carries a position error
    rx = cx + RNG.normal(0.0, sigma_km, N_RECORDS)
    ry = cy + RNG.normal(0.0, sigma_km, N_RECORDS)
    rep_box = np.column_stack([rx - half, ry - half, rx + half, ry + half])
    start = RNG.uniform(0.0, DAY_MAX - 300.0, N_RECORDS)
    duration = RNG.uniform(30.0, 300.0, N_RECORDS)
    return true_box, rep_box, start, start + duration


def expected_close(box, window):
    """Records whose TRUE footprint overlaps the AOI window."""
    return bbox_intersects(box, window)


def query(rep_box, start, end, window, t0, t1):
    """The query a user actually issues: reported footprint and time overlap."""
    spatial = bbox_intersects(rep_box, window)
    temporal = (start < t1) & (t0 < end)
    return spatial & temporal


def main():
    window = (40.0, 40.0, 60.0, 60.0)     # AOI: x0,y0,x1,y1 (km)
    t0, t1 = 200.0, 560.0                 # AOI time window (day index)

    section("1. A synthetic catalogue (SYNTHETIC)")
    true_box, rep_box, start, end = build_catalogue(sigma_km=4.0)
    print(f"{N_RECORDS} records over a {REGION_KM:.0f} km x {REGION_KM:.0f} km region,")
    print(f"two years (day index 0-{DAY_MAX}).")
    print("  #   true x0    true y0   reported x0  reported y0   start   end")
    for i in (0, 1, 2):
        print(f"  {i:3d} {true_box[i, 0]:8.2f} {true_box[i, 1]:9.2f} "
              f"{rep_box[i, 0]:11.2f} {rep_box[i, 1]:12.2f} "
              f"{start[i]:7.1f} {end[i]:6.1f}")
    print("The reported footprint is a measurement with error; the true footprint")
    print("is what the query is really trying to find.")

    section("2. The query measured against ground truth (SYNTHETIC)")
    truth = expected_close(true_box, window) & (start < t1) & (t0 < end)
    got = query(rep_box, start, end, window, t0, t1)
    tp = int((truth & got).sum())
    fp = int((~truth & got).sum())
    fn = int((truth & ~got).sum())
    precision = tp / (tp + fp) if tp + fp else float("nan")
    recall = tp / (tp + fn) if tp + fn else float("nan")
    f1 = 2 * precision * recall / (precision + recall)
    print(f"AOI bbox = {window}, time window = day {t0:.0f} to {t1:.0f}")
    print(f"true matches = {int(truth.sum())}, returned = {int(got.sum())}")
    print(f"TP = {tp}, FP = {fp}, FN = {fn}")
    print(f"precision = {precision:.3f}, recall = {recall:.3f}, F1 = {f1:.3f}")
    print("Even a correct query misses records: a record whose true footprint")
    print("touches the AOI but whose reported footprint does not is invisible.")

    section("3. How metadata error degrades the query (SYNTHETIC)")
    print("  sigma (km)   returned   TP   FP   FN   precision   recall")
    for sigma in (0.0, 2.0, 4.0, 8.0, 16.0):
        tb, rb, s, e = build_catalogue(sigma)
        tr = expected_close(tb, window) & (s < t1) & (t0 < e)
        go = query(rb, s, e, window, t0, t1)
        t = int((tr & go).sum()); f = int((~tr & go).sum()); m = int((tr & ~go).sum())
        p = t / (t + f) if t + f else float("nan")
        r = t / (t + m) if t + m else float("nan")
        print(f"  {sigma:8.1f}   {int(go.sum()):8d} {t:4d} {f:4d} {m:4d}   "
              f"{p:9.3f}   {r:6.3f}")
    print("Position error grows false positives and false negatives together:")
    print("the catalogue answers a slightly different question than the user asked.")

    section("4. Licences in the result set (SYNTHETIC)")
    # access, redistribution, derivatives -- a synthetic permission model
    modes = {
        "open-attribution": (True, True, True),
        "open-noncommercial": (True, True, False),
        "registration": (True, False, False),
        "restricted": (False, False, False),
    }
    keys = list(modes)
    assign = RNG.choice(len(keys), size=N_RECORDS, p=[0.45, 0.20, 0.20, 0.15])
    n_missing = int((RNG.random(N_RECORDS) < 0.08).sum())   # 8% have no licence field
    result_idx = np.where(got)[0]
    print(f"licence field missing on {n_missing} of {N_RECORDS} records; those")
    print("cannot be filtered by licence at all.")
    print("  licence               count in result set   redistributable?")
    for j, k in enumerate(keys):
        c = int((assign[result_idx] == j).sum())
        print(f"  {k:20s} {c:19d}   {'yes' if modes[k][1] else 'no'}")
    free_to_view = sum(int((assign[result_idx] == j).sum())
                       for j, k in enumerate(keys) if modes[k][0])
    free_to_share = sum(int((assign[result_idx] == j).sum())
                        for j, k in enumerate(keys) if modes[k][1])
    print(f"free to view = {free_to_view}, free to redistribute = {free_to_share}")
    print("Everything here may be viewed without payment; that is not the same")
    print("as permission to publish, mosaic or redistribute the pixels.")

    section("5. Discovery equals (identifier + version), not description")
    print('A query "snow scene, winter, middle of the region" returns many')
    print('records; a query by stable identifier and version returns one.')
    print("Descriptive discovery ranks candidates; only an identifier (and a")
    print("pinned version) makes a result reproducible.")


if __name__ == "__main__":
    main()
