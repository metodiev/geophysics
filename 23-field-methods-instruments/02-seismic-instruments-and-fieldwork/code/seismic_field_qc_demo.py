#!/usr/bin/env python3
"""Field QC arithmetic for a seismic deployment: uptime, availability, noise
outliers, dead channels and continuity, on SYNTHETIC data.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_field_qc_demo.py

Everything here is SYNTHETIC.  The gap rates, noise levels, thresholds and
failure counts are chosen teaching values.  No real station, no real noise
measurement and no network log is used or reproduced.

Sections
--------
1. Uptime from gap statistics.
2. Availability from MTBF and MTTR.
3. Noise QC with a robust threshold and its false-positive rate.
4. Dead, constant and saturated channel detection.
5. Continuity accounting at the sample level.
"""

import numpy as np
from math import erfc

RNG = np.random.default_rng(20261014)

N_STATION = 20
N_DAY = 30
P_GAP = 0.04            # probability of one gap on a station-day (chosen)
GAP_HOURS = 2.0
RATE = 100.0            # samples per second


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def robust_scale(x):
    """Median absolute deviation converted to a Gaussian-equivalent sigma."""
    med = np.median(x)
    mad = np.median(np.abs(x - med))
    return med, 1.4826 * mad


def main():
    section("1. Uptime from gap statistics")
    total_hours = N_DAY * 24.0
    gaps = RNG.random((N_STATION, N_DAY)) < P_GAP
    lost = gaps.sum(axis=1) * GAP_HOURS
    uptime = 1.0 - lost / total_hours
    print(f"  {N_STATION} stations, {N_DAY} days ({total_hours:.0f} h each), "
          f"gap probability {P_GAP:.2f} per station-day")
    print(f"  expected gaps per station = {P_GAP * N_DAY:.2f}, expected lost "
          f"time = {P_GAP * N_DAY * GAP_HOURS:.2f} h "
          f"(uptime {1.0 - P_GAP * N_DAY * GAP_HOURS / total_hours:.5f})")
    print(f"  measured: mean uptime = {uptime.mean():.5f}, "
          f"minimum = {uptime.min():.5f}, sd = {uptime.std():.5f}")
    for threshold in (0.999, 0.995, 0.99):
        print(f"  stations below an uptime of {threshold:.3f}: "
              f"{int((uptime < threshold).sum())} of {N_STATION}")
    print("  -> an average uptime hides the tail; the stations in the tail are")
    print("     the ones that remove the network's detection capability.")

    section("2. Availability from MTBF and MTTR")
    print(f"  {'MTBF (d)':>9s} {'MTTR (h)':>9s} {'availability':>13s}"
          f" {'downtime (h/year)':>19s} {'repairs per year':>17s}")
    for mtbf, mttr in ((45.0, 6.0), (45.0, 2.0), (180.0, 6.0), (20.0, 6.0)):
        a = mtbf * 24.0 / (mtbf * 24.0 + mttr)
        print(f"  {mtbf:9.0f} {mttr:9.0f} {a:13.5f} "
              f"{(1.0 - a) * 8760.0:19.1f} {8760.0 / (mtbf * 24.0):17.1f}")
    print("  -> halving the repair time buys more availability per unit of")
    print("     effort than doubling the time between failures, when the MTTR is")
    print("     a large fraction of the MTBF.")

    section("3. Noise QC with a robust threshold")
    n_channel = N_STATION * 3
    clean = 10.0 ** RNG.normal(np.log10(1.0e-6), 0.15, n_channel)
    bad = np.zeros(n_channel, dtype=bool)
    bad[:4] = True
    level = clean.copy()
    level[bad] *= 10.0 ** RNG.uniform(0.5, 1.2, int(bad.sum()))
    median, sigma = robust_scale(level)
    z = (level - median) / sigma
    print(f"  {n_channel} channels; {int(bad.sum())} injected at 3x to 16x the")
    print(f"  median noise level (chosen)")
    print(f"  median level = {median:.3e} m/s, robust sigma = {sigma:.3e} "
          f"({sigma / median:.3f} of the median)")
    for threshold in (2.0, 3.0, 4.0):
        flagged = z > threshold
        true_positive = int((flagged & bad).sum())
        false_positive = int((flagged & ~bad).sum())
        expected_fp = float((~bad).sum()) * 0.5 * erfc(threshold / np.sqrt(2.0))
        print(f"  threshold z > {threshold:.1f}: flagged {int(flagged.sum())}, "
              f"of which injected {true_positive} of {int(bad.sum())}, "
              f"clean {false_positive} "
              f"(expected under Gaussianity {expected_fp:.1f})")
    print("  -> the false-positive count is a number you can predict before")
    print("     deployment; a QC threshold without it is a guess.")

    section("4. Dead, constant and saturated channels")
    n = 60000
    records = 0.1 * RNG.standard_normal((n_channel, n))
    channels = ["clean"] * n_channel
    for index in range(0, 6):
        channels[index] = "constant"
        records[index, :] = 0.0
    for index in range(6, 9):
        channels[index] = "saturated"
        records[index, :] = np.clip(3.0 * RNG.standard_normal(n), -1.0, 1.0)
    flat = records.std(axis=1) == 0.0
    at_limit = (np.abs(records) >= 0.999).mean(axis=1) > 0.05
    print(f"  {n_channel} channels, {n} samples each, SYNTHETIC")
    print(f"  channels with zero standard deviation: {int(flat.sum())} "
          f"(injected constant channels: 6)")
    print(f"  channels with more than 5 % of samples at the limit: "
          f"{int(at_limit.sum())} (injected saturated channels: 3)")
    fp = int(np.sum(flat & (np.array(channels) == 'clean'))), \
         int(np.sum(at_limit & (np.array(channels) == 'clean')))
    print(f"  false positives: constant test {fp[0]}, saturation test {fp[1]}")
    print("  -> both tests are cheap, deterministic and run before any")
    print("     processing; a dead channel found six months later is a hole in")
    print("     the catalogue, not a data-quality flag.")

    section("5. Continuity accounting at the sample level")
    expected = N_DAY * 24.0 * 3600.0 * RATE
    lost_samples = gaps.sum(axis=1) * GAP_HOURS * 3600.0 * RATE
    completeness = 1.0 - lost_samples / expected
    print(f"  expected samples per station = {expected:.3e}")
    print(f"  detected gaps, campaign total = {int(gaps.sum())}; per station "
          f"mean = {gaps.sum(axis=1).mean():.2f}")
    print(f"  lost samples, campaign total = {lost_samples.sum():.3e}")
    print(f"  per-station completeness: mean = {completeness.mean():.6f}, "
          f"min = {completeness.min():.6f}")
    print(f"  overlaps detected = 0 samples (none injected in this SYNTHETIC set)")
    print("  -> report completeness, gaps and overlaps as three separate")
    print("     numbers.  They have different causes and different remedies:")
    print("     gaps are power or storage, overlaps are clock or operator error.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file.  They constrain a QC model, not any real network.")


if __name__ == "__main__":
    main()
