#!/usr/bin/env python3
"""Robust versus classical descriptive statistics on a SYNTHETIC porosity
sample that has been contaminated by instrument spikes.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python descriptive_statistics_demo.py

Everything here is SYNTHETIC: the "clean" values are drawn from a stated normal
distribution and the spikes are placed by hand.  No number is a measured
porosity and no data file is read.

Sections
--------
1. Location estimators under contamination.
2. Scale estimators, and the MAD-to-sigma consistency factor.
3. Outlier detection: classical z versus modified z.
4. Breakdown point of the mean and the median.
5. Efficiency of the mean and the median on clean Gaussian data.
6. Shape: skewness and kurtosis.
"""

import numpy as np
from scipy import stats

RNG = np.random.default_rng(20261014)

MU = 50.0        # true mean porosity, %
SIGMA = 10.0     # true standard deviation, %
N = 200          # number of samples
N_OUT = 10       # number of spikes
OUTLIER = 200.0  # spike value, %
M = 3000         # Monte-Carlo ensembles for the efficiency test


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    print("SYNTHETIC porosity sample: 200 draws from N(50, 10^2) % plus 10 "
          "spikes placed at 200 %.")
    clean = MU + SIGMA * RNG.standard_normal(N)
    dirty = clean.copy()
    dirty[:N_OUT] = OUTLIER

    section("1. Location estimators (porosity, %)")
    for label, s in (("clean", clean), ("contaminated", dirty)):
        print(f"  {label:12s}  mean = {s.mean():9.3f}   "
              f"median = {np.median(s):9.3f}   "
              f"10% trimmed mean = {stats.trim_mean(s, 0.1):9.3f}")
    shift_mean = dirty.mean() - clean.mean()
    shift_med = np.median(dirty) - np.median(clean)
    predicted = (N_OUT * OUTLIER - clean[:N_OUT].sum()) / N
    print(f"  replacing {N_OUT} clean values with {OUTLIER:.0f} % moves the mean")
    print(f"  by {predicted:+.3f} % (observed {shift_mean:+.3f} %), but moves "
          f"the median by only {shift_med:+.3f} %")

    section("2. Scale estimators (porosity, %)")
    for label, s in (("clean", clean), ("contaminated", dirty)):
        iqr = stats.iqr(s)
        mad = stats.median_abs_deviation(s)          # median |x - median|
        print(f"  {label:12s}  std = {s.std(ddof=1):8.3f}   "
              f"IQR = {iqr:7.3f}   MAD = {mad:7.3f}   "
              f"MAD/0.6745 = {mad / 0.67449:7.3f}")
    print("  MAD/0.6745 is the Gaussian-consistent robust scale; compare it with")
    print("  the std column: the robust value barely moves under contamination.")

    section("3. Masking: a gross spike hides moderate ones from the classical z")
    masked = clean.copy()
    masked[0] = 2000.0      # one gross spike
    masked[1:5] = 120.0     # four moderate spikes
    truth = np.zeros(N, dtype=bool)
    truth[:5] = True
    z = (masked - masked.mean()) / masked.std(ddof=1)
    mod_z = (0.67449 * (masked - np.median(masked))
             / stats.median_abs_deviation(masked))
    flag_z = np.abs(z) > 3.5
    flag_mz = np.abs(mod_z) > 3.5
    print(f"  one spike at 2000 % inflates the std from "
          f"{clean.std(ddof=1):.2f} % to {masked.std(ddof=1):.2f} %")
    print(f"  classical z (threshold 3.5)   : finds {np.sum(flag_z & truth)} of "
          f"5 spikes, {np.sum(flag_z & ~truth)} false positives")
    print(f"  modified z (MAD-based)        : finds {np.sum(flag_mz & truth)} of "
          f"5 spikes, {np.sum(flag_mz & ~truth)} false positives")
    print("  the gross spike hides the four moderate ones from any scale that is")
    print("  itself computed from the contaminated sample.")

    section("4. Breakdown point of the mean and the median")
    print("  fraction  n_spikes   median (%)   mean (%)")
    for frac in (0.0, 0.05, 0.10, 0.20, 0.40, 0.45, 0.50, 0.55):
        k = int(round(frac * N))
        s = clean.copy()
        s[:k] = OUTLIER
        print(f"  {frac:8.2f}  {k:8d}   {np.median(s):10.3f}   {s.mean():9.3f}")
    first_mean = first_med = None
    for frac in np.arange(0.0, 0.61, 0.01):
        k = int(round(frac * N))
        s = clean.copy()
        s[:k] = OUTLIER
        if first_mean is None and s.mean() > 60.0:
            first_mean = frac
        if first_med is None and np.median(s) > 90.0:
            first_med = frac
    print(f"  the mean passes 60 % at contamination {first_mean:.2f}")
    print(f"  the median leaves the clean data range (> 90 %) at "
          f"contamination {first_med:.2f} (theory: 0.50)")

    section("5. Efficiency on clean Gaussian data (M = 3000 ensembles)")
    means = np.empty(M)
    medians = np.empty(M)
    for i in range(M):
        s = MU + SIGMA * RNG.standard_normal(N)
        means[i] = s.mean()
        medians[i] = np.median(s)
    sd_mean = means.std(ddof=1)
    sd_med = medians.std(ddof=1)
    print(f"  sd of the sample mean   = {sd_mean:.4f} %")
    print(f"  sd of the sample median = {sd_med:.4f} %")
    print(f"  relative efficiency of the median = "
          f"{(sd_mean / sd_med) ** 2:.4f}  (Gaussian theory: 2/pi = "
          f"{2 / np.pi:.4f})")
    print("  the median pays ~36 % extra variance for its robustness.")

    section("6. Shape: skewness and kurtosis (Fisher)")
    for label, s in (("clean", clean), ("contaminated", dirty)):
        print(f"  {label:12s}  skewness = {stats.skew(s, bias=False):+7.3f}   "
              f"excess kurtosis = {stats.kurtosis(s, bias=False):+9.3f}")
    print("  a symmetric Gaussian has skew 0 and excess kurtosis 0; the spikes")
    print("  produce a coefficient of excess kurtosis near +10.")


if __name__ == "__main__":
    main()
