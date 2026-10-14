#!/usr/bin/env python3
"""Metadata standards: required fields, controlled vocabularies and units.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python metadata_standards_demo.py

Everything here is SYNTHETIC.  The station records are generated with chosen error
rates; no real catalogue is read, no standard's text is reproduced, and the unit
table is a teaching subset.

Sections
--------
1. Required-field completeness across a synthetic catalogue.
2. Controlled vocabularies: free text against a canonical list.
3. Units: declared units, conversions and the records that fail.
4. ISO 8601 durations, parsed and validated.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC catalogue model (chosen, not measured) -----------------------
N_RECORDS = 200
REQUIRED = ("network", "station", "channel", "latitude", "longitude",
            "elevation_m", "unit", "start_time")
P_MISSING = {"network": 0.02, "station": 0.01, "channel": 0.03,
             "latitude": 0.04, "longitude": 0.04, "elevation_m": 0.12,
             "unit": 0.05, "start_time": 0.02}
SENSOR_TERMS = ["STS-2", "Trillium 120", "trillium120", "Trillium-120",
                "STS2", "STS-2 broadband", "T120", "broadband",
                "unspecified sensor"]
CANONICAL = {"STS-2": ["STS-2", "STS2", "STS-2 broadband"],
             "Trillium 120": ["Trillium 120", "trillium120", "Trillium-120",
                              "T120"],
             "broadband (unspecified)": ["broadband"]}
UNIT_TABLE = {"m/s^2": 1.0, "m/s2": 1.0, "gal": 0.01, "cm/s^2": 0.01,
              "nm/s^2": 1e-9}
CANONICAL_UNIT = "m/s^2"


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. Required-field completeness")
    present = {f: RNG.random(N_RECORDS) >= P_MISSING[f] for f in REQUIRED}
    n_complete = int(np.all([present[f] for f in REQUIRED], axis=0).sum())
    print(f"SYNTHETIC catalogue: {N_RECORDS} records, {len(REQUIRED)} required "
          f"fields, per-field omission rates chosen")
    print("  field          | missing | missing (%)")
    for f in REQUIRED:
        n_missing = int((~present[f]).sum())
        print(f"  {f:<14} | {n_missing:>7d} | {100 * n_missing / N_RECORDS:>11.1f}")
    print(f"  records with every required field present = {n_complete} "
          f"({100 * n_complete / N_RECORDS:.1f} %)")
    print(f"  records missing at least one required field = "
          f"{N_RECORDS - n_complete} ({100 * (N_RECORDS - n_complete) / N_RECORDS:.1f} %)")
    print("  -> the completeness of the *record* is what matters: a per-field")
    print("     omission rate of a few per cent, repeated over eight fields,")
    print("     leaves a quarter of the catalogue unusable as it stands")

    section("2. Controlled vocabularies")
    terms = RNG.choice(SENSOR_TERMS, N_RECORDS)
    canonical_map = {t: c for c, variants in CANONICAL.items() for t in variants}
    mapped = np.array([canonical_map.get(t, "UNMAPPED") for t in terms])
    n_terms = len(set(terms))
    n_canonical = len(set(mapped) - {"UNMAPPED"})
    unmatched = int((mapped == "UNMAPPED").sum())
    print(f"  distinct free-text terms used        = {n_terms}")
    print(f"  canonical classes they map to        = {n_canonical}")
    print(f"  records with an unmapped term        = {unmatched} "
          f"({100 * unmatched / N_RECORDS:.1f} %)")
    print(f"  reduction in distinct labels = {n_terms} -> {n_canonical} "
          f"({n_terms / n_canonical:.1f}x)")
    print("  -> free text splits one instrument into many labels; a controlled")
    print("     vocabulary is what makes a group-by query meaningful")

    section("3. Units: declared, converted, failed")
    declared = RNG.choice(list(UNIT_TABLE), N_RECORDS)
    canonical_count = int((declared == CANONICAL_UNIT).sum())
    unmapped = int(sum(1 for u in declared if u not in UNIT_TABLE))
    print(f"  records declaring the canonical unit '{CANONICAL_UNIT}' = "
          f"{canonical_count} ({100 * canonical_count / N_RECORDS:.1f} %)")
    print(f"  records whose unit has no conversion entry = {unmapped}")
    print("  declared unit | records | factor to canonical")
    for unit in UNIT_TABLE:
        n = int((declared == unit).sum())
        print(f"  {unit:<13} | {n:>7d} | {UNIT_TABLE[unit]:>19.2e}")
    example = 9.81
    print(f"  example: {example} m/s^2 = {example / 0.01:.0f} gal = "
          f"{example / 1e-9:.2e} nm/s^2")
    print("  -> units in metadata are what let two data sets be compared; an")
    print("     unmapped unit is a silent factor-of-100 error waiting to happen")

    section("4. ISO 8601 durations, parsed and validated")
    durations = ["P1Y", "P2M", "P1Y2M3DT4H5M6S", "PT30M", "P1DT12H",
                 "P0.5D", "foo"]
    factors = {"Y": 365.25 * 86400, "M": 30.44 * 86400, "W": 7 * 86400,
               "D": 86400, "H": 3600, "S": 1}
    print("  value            | seconds       | parses?")
    ok = 0
    for text in durations:
        try:
            seconds = parse_duration(text, factors)
            print(f"  {text:<16} | {seconds:>13.1f} | yes")
            ok += 1
        except ValueError:
            print(f"  {text:<16} | {'-':>13} | no (rejected)")
    print(f"  parsed {ok} of {len(durations)}; a validator rejects malformed")
    print("  values before they reach an analysis")
    print("  -> note the ambiguity: 'M' is months in a date part and minutes in a")
    print("     time part, which is exactly why a parser must be used, not a")
    print("     hand-written string split")


def parse_duration(text, factors):
    """Minimal ISO 8601 duration parser: P[nY][nM][nW][nD][T[nH][nM][nS]].

    `factors` maps the date-part designators; the time part uses its own table,
    because 'M' means months in the date part and minutes in the time part.
    """
    time_factors = {"H": 3600.0, "M": 60.0, "S": 1.0}
    if not text.startswith("P"):
        raise ValueError("must start with P")
    body = text[1:]
    date_part, _, time_part = body.partition("T")
    seconds = _scan(date_part, "YMWD", factors)
    seconds += _scan(time_part, "HMS", time_factors)
    if seconds == 0.0 and "0" not in text:
        raise ValueError("empty duration")
    return seconds


def _scan(part, order, factors):
    total = 0.0
    i = 0
    seen = []
    while i < len(part):
        j = i
        while j < len(part) and (part[j].isdigit() or part[j] == "."):
            j += 1
        if j == i or j >= len(part) or part[j] not in order:
            raise ValueError(f"malformed component at {i}")
        if part[j] in seen:
            raise ValueError(f"repeated designator {part[j]}")
        seen.append(part[j])
        total += float(part[i:j]) * factors[part[j]]
        i = j + 1
    return total


if __name__ == "__main__":
    main()
