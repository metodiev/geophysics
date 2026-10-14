#!/usr/bin/env python3
"""Metadata completeness, provenance chaining and timing-error arithmetic on
SYNTHETIC station records.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_notebooks_demo.py

Everything here is SYNTHETIC.  The field list, the per-field completion
probabilities, the number of records and the timing offsets are chosen teaching
values.  No station log, no network metadata and no clock measurement is used.

Sections
--------
1. A metadata completeness score over synthetic records.
2. Content hashing and a hash chain: what a one-character correction does.
3. Timing errors translated into distance and into samples.
4. The size of the metadata the completeness score is measuring.
"""

import hashlib

import numpy as np

RNG = np.random.default_rng(20261014)

N_RECORDS = 40

# Field name and the SYNTHETIC probability that it is filled in correctly.
FIELDS = [
    ("station_id", 0.99),
    ("latitude", 0.99),
    ("longitude", 0.99),
    ("elevation_m", 0.95),
    ("sensor_serial", 0.98),
    ("sensor_orientation_deg", 0.90),
    ("sample_rate_sps", 0.99),
    ("gain_counts_per_m_s", 0.85),
    ("start_time_utc", 0.97),
    ("clock_source", 0.80),
    ("operator_initials", 0.99),
    ("site_photo_id", 0.60),
    ("soil_description", 0.55),
    ("ground_coupling_notes", 0.45),
]


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def record_values(i):
    """Deterministic synthetic metadata values for record i."""
    return {
        "station_id": f"STA{i:02d}",
        "latitude": f"{40.0 + 0.0025 * i:.5f}",
        "longitude": f"{-105.0 + 0.0020 * i:.5f}",
        "elevation_m": f"{1650.0 + 3.0 * i:.1f}",
        "sensor_serial": f"SN{i:05d}",
        "sensor_orientation_deg": f"{(i * 7) % 360:.0f}",
        "sample_rate_sps": "500",
        "gain_counts_per_m_s": f"{2.0e6 + 1000.0 * i:.0f}",
        "start_time_utc": f"2026-08-{10 + (i % 20):02d}T{6 + (i % 12):02d}:00:00Z",
        "clock_source": "GNSS",
        "operator_initials": "MJ",
        "site_photo_id": f"IMG_{i:03d}",
        "soil_description": "silty sand",
        "ground_coupling_notes": "spiked, dry",
    }


def canonical(record, present_row, overrides=None):
    values = record_values(record)
    if overrides:
        values.update(overrides)
    parts = [f"{name}={values[name]}" for index, (name, _) in enumerate(FIELDS)
             if present_row[index]]
    return ";".join(parts)


def sha256_hex(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    section("1. Metadata completeness over %d SYNTHETIC records" % N_RECORDS)
    probabilities = np.array([p for _, p in FIELDS])
    present = RNG.random((N_RECORDS, len(FIELDS))) < probabilities
    score = present.mean(axis=1)
    print(f"  required fields = {len(FIELDS)}, field slots = "
          f"{N_RECORDS * len(FIELDS)}, filled = {int(present.sum())} "
          f"({100.0 * present.mean():.1f} %)")
    print(f"  per-record completeness: mean = {score.mean():.4f}, "
          f"min = {score.min():.4f}, sd = {score.std():.4f}")
    print(f"  records below a completeness threshold of 0.80 = "
          f"{int((score < 0.80).sum())} of {N_RECORDS}")
    order = np.argsort(probabilities)
    print("  weakest fields (SYNTHETIC completion probability):")
    for index in order[:5]:
        name, p = FIELDS[index]
        observed = present[:, index].mean()
        print(f"    {name:<24s} assumed {p:.2f}  observed {observed:.2f}")
    print("  -> the score is computed from the record, but the probability that")
    print("     a field is empty is a property of the workflow, not the site.")

    section("2. Content hashing and the hash chain")
    digests = [sha256_hex(canonical(i, present[i], ))
               for i in range(N_RECORDS)]
    chain = []
    previous = "0" * 16
    for digest in digests:
        previous = sha256_hex(previous + digest)
        chain.append(previous)
    print(f"  digest length = {len(digests[0])} hex characters "
          f"= {4 * len(digests[0])} bits")
    for i in (0, 1, 2):
        print(f"  record {i:02d} digest = {digests[i][:16]}...")
    corrected = [sha256_hex(canonical(i, present[i],
                                     {"elevation_m": "9999.9"} if i == 5 else None))
                 for i in range(N_RECORDS)]
    differing = sum(a != b for a, b in zip(digests[5], corrected[5]))
    print(f"  one metadata value corrected in record 05 changes {differing} of")
    print(f"  {len(digests[5])} hex characters of its digest "
          f"(expected {len(digests[5]) * 15 / 16:.1f})")
    chain_corrected = []
    previous = "0" * 16
    for digest in corrected:
        previous = sha256_hex(previous + digest)
        chain_corrected.append(previous)
    changed = sum(a != b for a, b in zip(chain, chain_corrected))
    print(f"  chain entries that change = {changed} of {N_RECORDS} "
          f"(every entry from record 05 onward)")
    print("  -> a chain localises a change and cannot be edited unnoticed, but")
    print("     it proves integrity, not correctness.")

    section("3. Timing errors in distance and in samples")
    velocity = 3.0        # km/s, a chosen homogeneous model velocity
    range_km = 30.0       # source-receiver distance (chosen)
    rate = 500.0          # samples per second (chosen)
    table = [
        ("one sample at 500 sps", 1.0 / rate),
        ("a 0.5 s pick error", 0.5),
        ("a 1 ppm clock over 30 days", 1.0e-6 * 30.0 * 86400.0),
        ("a one-hour time-zone slip", 3600.0),
    ]
    print(f"  model velocity = {velocity:.1f} km/s, range = {range_km:.1f} km, "
          f"sample rate = {rate:.0f} sps")
    print(f"  {'error source':<26s} {'seconds':>10s} {'km':>10s} "
          f"{'% of range':>11s}")
    for label, seconds in table:
        km = velocity * seconds
        print(f"  {label:<26s} {seconds:10.4f} {km:10.4f} "
              f"{100.0 * km / range_km:11.1f}")
    print("  -> the first three are a calibration and discipline problem; the")
    print("     last is a bookkeeping error that no filtering can repair.")

    section("4. How much metadata the score is measuring")
    fill = present.mean()
    print(f"  measured fill fraction = {fill:.4f}; a field slot is one required")
    print(f"  field on one record")
    for count in (14, 40, 400):
        slots = count * len(FIELDS)
        print(f"  {count:4d} records -> {slots:6d} field slots, "
              f"{slots * fill:9.1f} filled at the measured rate")
    print("  (the second row is the SYNTHETIC set of section 1)")

    print("\nSYNTHETIC: all numbers above come from chosen values in this file.")
    print("They constrain a metadata-scoring model, not any real station log.")


if __name__ == "__main__":
    main()
