#!/usr/bin/env python3
"""Land-access and ethics arithmetic on SYNTHETIC parcels, zones and consents.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python permits_and_ethics_demo.py

Everything here is SYNTHETIC.  The parcel counts, per-parcel agreement
probabilities, protected-zone coverage, buffer widths and consent probabilities
are chosen teaching values.  This file is arithmetic, not legal or ethical
advice; the applicable rules depend on the jurisdiction and the land, and must
be checked with the responsible authority and the affected community.

Sections
--------
1. The permission chain: why a many-parcel survey fails as a whole.
2. Survey lines against a protected-zone mask.
3. What a mandated buffer does to the accessible area.
4. All-or-nothing consent versus parcel-level consent.
5. Access issues resolved week by week before mobilisation.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. The permission chain")
    print(f"  {'parcels':>8s} {'P(agree)':>9s} {'P(all agree)':>13s} "
          f"{'expected refusals':>18s} {'P needed for 90 %':>18s}")
    for parcels, p in ((25, 0.80), (60, 0.80), (25, 0.95)):
        p_all = p ** parcels
        p_needed = 0.90 ** (1.0 / parcels)
        print(f"  {parcels:8d} {p:9.2f} {p_all:13.6f} "
              f"{parcels * (1.0 - p):18.1f} {p_needed:18.5f}")
    print("  -> with 60 parcels, per-parcel agreement must exceed 99.8 % before")
    print("     the whole survey is 90 % likely to be fully permitted.")

    section("2. Survey lines against a protected-zone mask")
    coverage = 0.005      # fraction of the area inside a protected zone
    segment_m = 10.0      # length of one simulated line segment
    line_m = 2000.0       # line length
    lines = 120
    n_segment = int(line_m / segment_m)
    p_line = 1.0 - (1.0 - coverage) ** n_segment
    inside = RNG.random((lines, n_segment)) < coverage
    clipped = inside.any(axis=1).sum()
    total_segments = int(inside.sum())
    print(f"  protected coverage = {coverage * 100:.2f} % of the survey area")
    print(f"  line length = {line_m:.0f} m sampled at {segment_m:.0f} m -> "
          f"{n_segment} segments per line")
    print(f"  predicted P(a line clips a zone) = {p_line:.4f}")
    print(f"  measured clipped lines = {clipped} of {lines} "
          f"({100.0 * clipped / lines:.1f} %)")
    print(f"  expected clipped segments = "
          f"{lines * n_segment * coverage:.1f}, measured = {total_segments}")
    print("  -> at this line length nearly every line touches something, so a")
    print("     mask must be applied line by line, not assessed as an average.")

    section("3. The buffer arithmetic")
    zone_width = 30.0     # m
    buffer_width = 25.0   # m each side (chosen, check the local rule)
    effective = zone_width + 2.0 * buffer_width
    factor = effective / zone_width
    print(f"  measured zone width = {zone_width:.0f} m")
    print(f"  mandated buffer = {buffer_width:.0f} m either side")
    print(f"  effective excluded width = {effective:.0f} m "
          f"= {factor:.3f} x the zone")
    print(f"  excluded area therefore rises from {coverage * 100:.2f} % to "
          f"{coverage * factor * 100:.2f} % of the survey area")
    print("  -> the buffer, not the archaeology, usually sets the excluded area;")
    print("     it belongs in the design, not in the post-survey excuse.")

    section("4. All-or-nothing consent versus parcel-level consent")
    p_consent = 0.85
    print(f"  per-parcel consent probability = {p_consent:.2f}")
    for parcels in (25, 60):
        p_all = p_consent ** parcels
        ratio = p_consent / p_all
        print(f"  {parcels:3d} parcels: P(every parcel consents) = {p_all:.6f}, "
              f"publishable stations = {100.0 * p_consent:.1f} % under "
              f"parcel-level consent, ratio = {ratio:,.0f}x")
    print("  -> a protocol that requires unanimity to publish anything converts")
    print("     an 85 % majority into a near-zero release.")

    section("5. Access issues resolved week by week")
    unresolved = 8
    p_week = 0.40
    print(f"  {unresolved} unresolved parcels, {p_week:.2f} probability of")
    print(f"  resolution in any one week (chosen)")
    print(f"  {'weeks':>6s} {'expected unresolved':>20s} "
          f"{'P(all resolved)':>17s}")
    for weeks in (2, 4, 6, 10):
        expected = unresolved * (1.0 - p_week) ** weeks
        p_all = (1.0 - (1.0 - p_week) ** weeks) ** unresolved
        print(f"  {weeks:6d} {expected:20.3f} {p_all:17.4f}")
    print("  -> permission work has to start months before the mobilisation date")
    print("     because its timescale is set by other people.")

    print("\nSYNTHETIC: all numbers above come from chosen values in this file.")
    print("They constrain planning arithmetic only and are not legal advice.")


if __name__ == "__main__":
    main()
