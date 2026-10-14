#!/usr/bin/env python3
"""Statistical spectral analysis: what a periodogram peak is worth.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spectral_analysis_statistical_demo.py

Everything here is SYNTHETIC.  The records are red-noise realisations generated
below, and the normalising spectrum is the generator's own theoretical spectrum;
no record, no published spectrum and no quoted detection threshold is used.

Sections
--------
1. The synthetic ensemble and the normalised periodogram statistic.
2. The per-frequency false-alarm rate.
3. The maximum over frequencies, and the family-wise level.
4. Segment averaging: what it buys and what it does not.
"""

import numpy as np
from scipy.stats import chi2

RNG = np.random.default_rng(20261014)

N = 512             # samples per record
M = 400             # realizations
PHI = 0.80          # AR(1) coefficient of the red-noise process
SEGMENTS = 4        # segments used by the averaging experiment
ALPHA = 0.05        # nominal significance level


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def ar1(n, phi, rng):
    w = rng.standard_normal(n)
    x = np.empty(n)
    x[0] = w[0] / np.sqrt(1.0 - phi ** 2)
    for i in range(1, n):
        x[i] = phi * x[i - 1] + w[i]
    return x


def theory_spectrum(n, phi):
    """AR(1) spectrum on the interior frequencies of an rfft grid."""
    freq = np.fft.rfftfreq(n, d=1.0)[1:-1]
    return 1.0 / (1.0 - 2.0 * phi * np.cos(2.0 * np.pi * freq) + phi ** 2)


def normalised_periodogram(x, spectrum):
    """One-sided periodogram divided by its expectation, then mean-scaled."""
    spec = np.abs(np.fft.rfft(x - x.mean())) ** 2
    ratio = spec[1:-1] / spectrum
    return ratio / ratio.mean()


def main():
    section("1. The synthetic ensemble and the periodogram statistic")
    s_full = theory_spectrum(N, PHI)
    n_freq = s_full.size
    print(f"SYNTHETIC ensemble: {M} realizations of an AR(1) process with "
          f"phi = {PHI:.2f}, n = {N} samples, unit sampling interval")
    print(f"  {n_freq} interior frequencies; the periodogram spans "
          f"{s_full.max() / s_full.min():.1f}x between its largest and "
          f"smallest expectation")
    print("  the statistic is P(f)/S(f), normalised by its own mean over "
          "frequencies")
    print("  under the null each frequency is exponentially distributed with 2")
    print("  degrees of freedom, so P(statistic > -ln(alpha)) = alpha")
    print("  the demonstration normalises by the GENERATOR's spectrum; in")
    print("  practice S(f) is replaced by a fitted AR spectrum or a smoothed")
    print("  periodogram, and the choice changes the calibration")

    freq_level = -np.log(ALPHA)
    print(f"  per-frequency 95% level = -ln(0.05) = {freq_level:.4f}")

    fixed_hits = 0
    maxima = np.empty(M)
    for m in range(M):
        r = normalised_periodogram(ar1(N, PHI, RNG), s_full)
        if r[64] > freq_level:               # a frequency fixed in advance
            fixed_hits += 1
        maxima[m] = r.max()
    mc_error = np.sqrt(ALPHA * (1.0 - ALPHA) / M)

    section("2. The per-frequency false-alarm rate")
    print(f"  measured rate at ONE PRE-SPECIFIED frequency = "
          f"{fixed_hits / M:.3f} (nominal {ALPHA:.2f}, Monte Carlo error "
          f"{mc_error:.3f})")
    print(f"  measured rate for the MAXIMUM over all {n_freq} frequencies at "
          f"that same level = {np.mean(maxima > freq_level):.3f}")
    print("  one level, two meanings: it is a 5% test of a pre-specified")
    print("  frequency and a near-certain 'detection' when applied to the")
    print("  largest peak of the same record, because there are 255 chances")

    section("3. The maximum over frequencies, and the family-wise level")
    level_fw = -np.log(1.0 - (1.0 - ALPHA) ** (1.0 / n_freq))
    print(f"  empirical 95th percentile of the maximum = "
          f"{np.percentile(maxima, 95):.3f}")
    print(f"  family-wise level -ln(1 - 0.95^(1/n)) = {level_fw:.3f}")
    print(f"  measured rate of the maximum at that level = "
          f"{np.mean(maxima > level_fw):.3f} (nominal {ALPHA:.2f})")
    print("  the empirical percentile and the analytic level agree, which is")
    print("  the check that the null distribution is what the theory says")

    section("4. Segment averaging: what it buys and what it does not")
    seg_n = N // SEGMENTS
    s_seg = theory_spectrum(seg_n, PHI)
    dof = 2 * SEGMENTS
    seg_level = chi2.ppf(1.0 - ALPHA, dof) / dof
    seg_level_fw = chi2.ppf(1.0 - ALPHA / s_seg.size, dof) / dof
    seg_fixed = 0
    seg_maxima = np.empty(M)
    spread_raw, spread_seg = [], []
    for m in range(M):
        x = ar1(N, PHI, RNG)
        segments = [normalised_periodogram(x[i * seg_n:(i + 1) * seg_n], s_seg)
                    for i in range(SEGMENTS)]
        averaged = np.mean(segments, axis=0)
        seg_maxima[m] = averaged.max()
        if averaged[16] > seg_level:
            seg_fixed += 1
        spread_raw.append(normalised_periodogram(x, s_full).std())
        spread_seg.append(averaged.std())
    print(f"  {SEGMENTS} segments of {seg_n} samples give {dof} degrees of "
          f"freedom per frequency")
    print(f"  per-frequency 95% level becomes chi2_8(0.95)/8 = "
          f"{seg_level:.4f} (was {freq_level:.4f})")
    print(f"  measured rate at one pre-specified frequency = "
          f"{seg_fixed / M:.3f} (nominal {ALPHA:.2f})")
    print(f"  measured rate for the maximum of the averaged estimate at the "
          f"per-frequency level = {np.mean(seg_maxima > seg_level):.3f}")
    print(f"  family-wise level for the averaged estimate = "
          f"{seg_level_fw:.4f}; measured rate there = "
          f"{np.mean(seg_maxima > seg_level_fw):.3f}")
    print(f"  scatter of the ordinates: raw {np.mean(spread_raw):.3f}, "
          f"averaged {np.mean(spread_seg):.3f} (ratio "
          f"{np.mean(spread_seg) / np.mean(spread_raw):.3f})")
    print("  averaging reduces the scatter of each ordinate -- here by a factor")
    print("  of about two in the standard deviation, as four independent")
    print("  segments predict -- but it does NOT touch the")
    print("  multiplicity problem: the maximum over frequencies still needs a")
    print("  family-wise level, and the averaged estimate has fewer frequencies")
    print("  and a correspondingly smaller correction")
    print("\nSYNTHETIC: these are red-noise realisations generated by this script.")
    print("The thresholds are properties of the statistic under the null, not")
    print("evidence of a periodic signal in any real record.")


if __name__ == "__main__":
    main()
