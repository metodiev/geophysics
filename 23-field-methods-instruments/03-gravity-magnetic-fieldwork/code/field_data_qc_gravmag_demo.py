#!/usr/bin/env python3
"""Quality-control statistics for potential-field surveys: loop closures, repeats,
mis-ties, cross-overs and an error budget, on SYNTHETIC data.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_data_qc_gravmag_demo.py

Everything here is SYNTHETIC.  The drift rate, tidal amplitudes, reading noises,
line offsets and tolerances are chosen teaching values.  No field survey, no
airborne dataset and no measured repeatability figure is used or reproduced.

Sections
--------
1. Loop closures over a campaign: distribution, tolerance and what rejection does.
2. Repeat stations: pooled repeatability and the station standard error.
3. Levelling: mis-tie RMS before and after a line-level adjustment.
4. Cross-over errors from an airborne survey: systematic and random parts.
5. An error budget in quadrature, and which term dominates.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

READ_NOISE_GAL = 0.005     # mGal, gravity reading noise (chosen)
READ_NOISE_NT = 1.5        # nT, magnetic reading noise (chosen)
DRIFT_RATE = 0.008         # mGal/h (chosen)
TIDE_SEMI = 0.10           # mGal, semi-diurnal tidal amplitude (chosen)
TOLERANCE = 0.15           # mGal, loop closure tolerance (chosen)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def tidal_drift(t):
    return (DRIFT_RATE * t
            + TIDE_SEMI * np.sin(2.0 * np.pi * t / 12.4)
            + 0.04 * np.sin(2.0 * np.pi * t / 24.0))


def main():
    section("1. Loop closures over a campaign")
    n_loops = 60
    start = RNG.uniform(0.0, 24.0, n_loops)
    duration = RNG.uniform(2.0, 4.0, n_loops)
    closure = np.abs(tidal_drift(start + duration) - tidal_drift(start))
    closure = closure + READ_NOISE_GAL * np.sqrt(2.0) * RNG.standard_normal(n_loops)
    keep = closure <= TOLERANCE
    print(f"  {n_loops} SYNTHETIC loops, durations 2-4 h at random start times")
    print(f"  closure: mean = {closure.mean():.4f} mGal, "
          f"sd = {closure.std():.4f} mGal, max = {closure.max():.4f} mGal")
    print(f"  tolerance = {TOLERANCE:.2f} mGal: "
          f"{int((~keep).sum())} loops above it "
          f"({100.0 * (~keep).mean():.1f} %)")
    print(f"  RMS over all loops      = "
          f"{np.sqrt((closure ** 2).mean()):.4f} mGal")
    print(f"  RMS over the accepted   = "
          f"{np.sqrt((closure[keep] ** 2).mean()):.4f} mGal")
    print("  -> rejecting a loop because its closure is large does not improve the")
    print("     data: it removes the loop that carried the information about the")
    print("     drift.  Reject only on an identified cause (a storm, a re-levelling,")
    print("     a reading taken before the instrument settled).")

    section("2. Repeat stations")
    n_station, n_repeat = 8, 5
    repeats = READ_NOISE_GAL * RNG.standard_normal((n_station, n_repeat))
    per_station = repeats.std(axis=1, ddof=1)
    pooled = np.sqrt((per_station ** 2).mean())
    print(f"  {n_station} stations, {n_repeat} repeats each, SYNTHETIC reading"
          f" noise {READ_NOISE_GAL:.3f} mGal")
    print(f"  per-station standard deviations: min = {per_station.min():.4f}, "
          f"max = {per_station.max():.4f} mGal")
    print(f"  pooled repeatability = {pooled:.4f} mGal "
          f"(exact expectation {READ_NOISE_GAL:.4f})")
    print(f"  95 % repeatability for n = {n_repeat} "
          f"(coverage 2.78) = {2.78 * pooled:.4f} mGal")
    print(f"  standard error of a 3-reading station value = "
          f"{pooled / np.sqrt(3.0):.4f} mGal")
    print("  -> report the pooled value AND its scatter: one station's repeat is")
    print("     not the survey's repeatability.")

    section("3. Levelling: mis-ties before and after adjustment")
    n_line, n_tie = 6, 4
    offsets = RNG.normal(0.0, 6.0, n_line)
    offsets -= offsets.mean()
    noise = READ_NOISE_NT * np.sqrt(2.0)
    mis = (offsets[:, None] + noise * RNG.standard_normal((n_line, n_tie)))
    before = np.sqrt((mis ** 2).mean())
    fitted = mis.mean(axis=1)
    residual = mis - fitted[:, None]
    after = np.sqrt((residual ** 2).mean())
    print(f"  {n_line} lines crossed by {n_tie} tie lines "
          f"({n_line * n_tie} mis-ties), SYNTHETIC line offsets sd "
          f"{offsets.std(ddof=1):.2f} nT")
    print(f"  mis-tie mean = {mis.mean():+.3f} nT, sd = {mis.std(ddof=1):.3f} nT")
    print(f"  RMS mis-tie before adjustment = {before:.3f} nT")
    print(f"  fitted line offsets: " + " ".join(f"{v:+.2f}" for v in fitted))
    print(f"  RMS mis-tie after adjustment  = {after:.3f} nT "
          f"(expectation sqrt(2) x noise = {noise:.3f} nT)")
    print(f"  reduction factor = {before / after:.2f}x")
    print("  -> after levelling, the mis-tie scatter should be consistent with")
    print("     the reading noise.  If it is not, the cause is not a line offset.")

    section("4. Cross-over errors from an airborne survey")
    n_cross = 240
    systematic = 8.0
    random_sd = 4.0
    errors = systematic + random_sd * RNG.standard_normal(n_cross)
    print(f"  {n_cross} SYNTHETIC cross-overs, systematic +{systematic:.1f} nT and")
    print(f"  random scatter {random_sd:.1f} nT")
    print(f"  signed mean = {errors.mean():+.3f} nT  (the correctable part)")
    print(f"  sd about the mean = {errors.std(ddof=1):.3f} nT "
          f"(the random part)")
    print(f"  RMS = {np.sqrt((errors ** 2).mean()):.3f} nT")
    print(f"  |error| > 15 nT = {int((np.abs(errors) > 15.0).sum())} of "
          f"{n_cross}")
    corrected = errors - errors.mean()
    print(f"  after removing the mean: RMS = "
          f"{np.sqrt((corrected ** 2).mean()):.3f} nT")
    print(f"  the mean is a *level* error and is removable; the scatter is the")
    print(f"  noise and is not.  Report them separately.")

    section("5. An error budget for a microgravity station value")
    terms = [("reading repeatability (3 readings)", 0.005),
             ("drift and tide residual", 0.016),
             ("elevation error (0.1 m at 0.1967 mGal/m)", 0.0197),
             ("position / latitude (20 m N-S)", 0.016),
             ("density assumption for the Bouguer term", 0.020)]
    total = np.sqrt(sum(v ** 2 for _, v in terms))
    print(f"  {'term':<44s} {'value (mGal)':>13s} {'share':>8s}")
    for label, value in terms:
        print(f"  {label:<44s} {value:13.4f} {100.0 * value ** 2 / total ** 2:7.1f} %")
    print(f"  {'total (quadrature)':<44s} {total:13.4f} {100.0:7.1f} %")
    print("  -> quote the budget and the dominant term; a single 'accuracy' number")
    print("     hides which measurement to improve.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file.  They constrain a QC model, not any real survey.")


if __name__ == "__main__":
    main()
