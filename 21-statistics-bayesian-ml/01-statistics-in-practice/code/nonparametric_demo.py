#!/usr/bin/env python3
"""Nonparametric statistics on SYNTHETIC data: rank tests against a t test
under Gaussian and contaminated conditions, and kernel density estimation with
two bandwidth rules compared by integrated squared error.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nonparametric_demo.py

All data are SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. Two-sample tests: Welch t versus Mann-Whitney, clean and contaminated.
2. Paired tests: Wilcoxon signed-rank and the sign test.
3. Kernel density estimation and the bandwidth rule.
4. Bandwidth selection by integrated squared error against a known truth.
"""

import numpy as np
from scipy import stats

RNG = np.random.default_rng(20261014)

N_A = N_B = 40
SHIFT = 0.4          # true mean shift, standard-deviation units
N_OUT = 5            # contaminated observations in group B
OUTLIER = 8.0        # contamination value
N_KDE = 200          # sample size for the density estimate
GRID = np.linspace(-4.0, 4.0, 401)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def silverman(x):
    n = x.size
    return 1.06 * min(x.std(ddof=1), (np.percentile(x, 75) - np.percentile(x, 25))
                      / 1.349) * n ** (-1.0 / 5.0)


def scott(x):
    return x.std(ddof=1) * x.size ** (-1.0 / 5.0)


def kde(x, grid, h):
    u = (grid[:, None] - x[None, :]) / h
    return np.exp(-0.5 * u ** 2).sum(axis=1) / (x.size * h * np.sqrt(2 * np.pi))


def main():
    print("SYNTHETIC two-group comparison: 40 + 40 Gaussian draws, then the "
          "same data with 5 outliers in group B.")

    a = RNG.standard_normal(N_A)
    b = SHIFT + RNG.standard_normal(N_B)

    section("1. Two-sample tests, clean and contaminated")
    for label, bb in (("clean", b), ("contaminated", np.concatenate(
            [b[:N_B - N_OUT], np.full(N_OUT, OUTLIER)]))):
        t_stat, p_t = stats.ttest_ind(a, bb, equal_var=False)
        u_stat, p_u = stats.mannwhitneyu(a, bb, alternative="two-sided")
        print(f"  {label:13s} means = {a.mean():+.3f} vs {bb.mean():+.3f}   "
              f"medians = {np.median(a):+.3f} vs {np.median(bb):+.3f}")
        print(f"                Welch t = {t_stat:+.3f} (p = {p_t:.4f})   "
              f"Mann-Whitney U = {u_stat:.1f} (p = {p_u:.4f})")
    print("  the outliers move the means and the t statistic; the rank test")
    print("  changes only through the ranks of the contaminated values.")

    section("2. Paired tests")
    d = 0.3 + RNG.standard_normal(30)
    w_stat, p_w = stats.wilcoxon(d)
    n_pos = int(np.sum(d > 0))
    p_sign = float(stats.binomtest(n_pos, d.size, 0.5).pvalue)
    print(f"  30 paired differences: mean = {d.mean():+.3f}, "
          f"median = {np.median(d):+.3f}")
    print(f"  Wilcoxon signed-rank W = {w_stat:.1f}, p = {p_w:.4f}")
    print(f"  sign test: {n_pos} of {d.size} positive, p = {p_sign:.4f}")
    print("  the sign test throws away the magnitudes; the signed-rank test")
    print("  keeps them and is the more powerful of the two when they matter.")

    section("3. Kernel density estimation and the bandwidth")
    x = np.concatenate([RNG.standard_normal(N_KDE // 2),
                        RNG.standard_normal(N_KDE // 2) + 2.5])
    h_s = silverman(x)
    h_sc = scott(x)
    print(f"  n = {N_KDE}, sample sd = {x.std(ddof=1):.3f}")
    print(f"  subgroups: mean1 = {x[:N_KDE // 2].mean():+.3f}, "
          f"mean2 = {x[N_KDE // 2:].mean():+.3f}")
    print(f"  Silverman bandwidth h = {h_s:.4f}, Scott bandwidth h = "
          f"{h_sc:.4f}")
    print("  h      density(0)  density(1.25)  density(2.5)  modes")
    for h in (0.20, 0.40, h_s, 1.00):
        dens = kde(x, GRID, h)
        d0 = float(np.interp(0.0, GRID, dens))
        dmid = float(np.interp(1.25, GRID, dens))
        d25 = float(np.interp(2.5, GRID, dens))
        peaks = np.sum((dens[1:-1] > dens[:-2]) & (dens[1:-1] > dens[2:])
                       & (dens[1:-1] > 0.20 * dens.max()))
        print(f"  {h:5.2f}  {d0:10.3f}  {dmid:13.3f}  {d25:12.3f}  "
              f"{int(peaks):5d}")
    print("  the automatic rules assume one smooth mode; on this two-component")
    print("  sample they nearly flatten the trough, while a manual h = 0.20")
    print("  invents spurious spikes.  The bandwidth is a modelling decision.")

    section("4. Bandwidth by integrated squared error against the truth")
    truth = 0.5 * stats.norm.pdf(GRID, 0.0, 1.0) + \
        0.5 * stats.norm.pdf(GRID, 2.5, 1.0)
    best_h, best_ise = None, np.inf
    for h in np.linspace(0.10, 1.20, 45):
        ise = float(np.trapezoid((kde(x, GRID, h) - truth) ** 2, GRID))
        if ise < best_ise:
            best_h, best_ise = h, ise
    ise_s = float(np.trapezoid((kde(x, GRID, h_s) - truth) ** 2, GRID))
    ise_sc = float(np.trapezoid((kde(x, GRID, h_sc) - truth) ** 2, GRID))
    print(f"  ISE at the Silverman bandwidth = {ise_s:.5f}")
    print(f"  ISE at the Scott bandwidth     = {ise_sc:.5f}")
    print(f"  ISE at the oracle bandwidth    = {best_ise:.5f} "
          f"(h = {best_h:.3f}, on the search grid)")
    print(f"  Silverman exceeds the oracle by "
          f"{100 * (ise_s / best_ise - 1):.1f} %")


if __name__ == "__main__":
    main()
