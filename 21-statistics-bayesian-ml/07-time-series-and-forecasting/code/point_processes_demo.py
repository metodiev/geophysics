#!/usr/bin/env python3
"""Point processes and seismicity rates: Poisson, clustering and Omori decay.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python point_processes_demo.py

Everything here is SYNTHETIC.  The catalogue is simulated from a background rate
plus an Omori aftershock sequence generated below; no real catalogue, no published
Omori parameter and no observed rate is used.

Sections
--------
1. The synthetic catalogue: background plus one mainshock.
2. Counting statistics: Poisson or overdispersed?
3. A 30-day forecast under two models.
4. Recovering the Omori decay exponent.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

T_DAYS = 3650.0     # catalogue length, days
LAMBDA0 = 0.02      # background rate, events per day
T_MAIN = 1000.0     # mainshock time, days
OMORI_K = 7.35      # Omori productivity, events per day^(1-p)
OMORI_C = 0.1       # Omori time offset, days
OMORI_P = 1.10      # Omori decay exponent, dimensionless
HORIZON = 30.0      # forecast horizon, days


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def omori_rate(t):
    """Background plus Omori rate, events per day, for an array of times."""
    tau = np.maximum(t - T_MAIN, 0.0)
    return LAMBDA0 + np.where(tau > 0.0, OMORI_K * (tau + OMORI_C) ** (-OMORI_P),
                              0.0)


def omori_only(t):
    """The Omori term alone, events per day, for tau > 0."""
    tau = np.maximum(t - T_MAIN, 0.0)
    return np.where(tau > 0.0, OMORI_K * (tau + OMORI_C) ** (-OMORI_P), 0.0)


def simulate():
    """Background Poisson process plus a thinned Omori sequence."""
    # background: exponential inter-arrival times over the whole catalogue
    gaps = RNG.exponential(1.0 / LAMBDA0, size=100000)
    background = np.cumsum(gaps)
    background = background[background <= T_DAYS]

    # aftershocks: thinning of the Omori term alone on [T_MAIN, T_DAYS]
    lam_max = OMORI_K * OMORI_C ** (-OMORI_P)
    waits = RNG.exponential(1.0 / lam_max, size=400000)
    candidate = T_MAIN + np.cumsum(waits)
    candidate = candidate[candidate <= T_DAYS]
    accept = RNG.random(candidate.size) < omori_only(candidate) / lam_max
    aftershocks = candidate[accept]
    times = np.sort(np.concatenate([background, aftershocks]))
    return times, background.size, aftershocks.size, lam_max


def main():
    section("1. The synthetic catalogue: background plus one mainshock")
    times, n_bg, n_aft, lam_max = simulate()
    print(f"SYNTHETIC catalogue: {T_DAYS:.0f} days, background rate "
          f"{LAMBDA0:.3f} events/day, one mainshock at t = {T_MAIN:.0f} days")
    print(f"  Omori rate above the mainshock: K/(tau+c)^p with K = "
          f"{OMORI_K:.2f}, c = {OMORI_C:.1f} day, p = {OMORI_P:.2f}")
    expected_aft = OMORI_K * ((T_DAYS - T_MAIN + OMORI_C) ** (1.0 - OMORI_P)
                              - OMORI_C ** (1.0 - OMORI_P)) / (1.0 - OMORI_P)
    print(f"  expected aftershocks by integration = {expected_aft:.1f}, "
          f"simulated count = {n_aft}")
    print(f"  background events = {n_bg}, aftershocks = {n_aft}, "
          f"total events = {times.size}")
    print(f"  peak Omori rate immediately after the mainshock = {lam_max:.1f} "
          f"events/day, which is {lam_max / LAMBDA0:.0f}x the background rate")
    print("  the peak is over three orders of magnitude above the background:")
    print("  any statistic averaged over the whole catalogue is dominated by the")
    print("  few days that follow the mainshock")

    section("2. Counting statistics: Poisson or overdispersed?")
    counts = np.histogram(times, bins=np.arange(0.0, T_DAYS + 1.0))[0]
    mean = counts.mean()
    index = counts.var(ddof=1) / mean
    nonzero = counts[counts > 0]
    print(f"  daily counts over {counts.size} days: mean = {mean:.4f} events/day, "
          f"variance = {counts.var(ddof=1):.4f}")
    print(f"  variance-to-mean ratio (index of dispersion) = {index:.3f} "
          f"(Poisson: 1.000)")
    print(f"  days with zero events = {np.mean(counts == 0):.3f}, "
          f"maximum daily count = {counts.max()}")
    print(f"  Poisson prediction for the zero fraction with the same mean = "
          f"{np.exp(-mean):.3f}")
    print("  the index of dispersion is above 1: the counts are clustered, so a")
    print("  Poisson model with the mean rate understates both quiet periods and")
    print("  aftershock bursts")
    print(f"  observed counts range from {counts.min()} to {counts.max()} in a")
    print(f"  catalogue whose mean is {mean:.3f}/day")

    section("3. A 30-day forecast under two models")
    lam_bar = times.size / T_DAYS
    grid = np.linspace(T_MAIN, T_MAIN + HORIZON, 20001)
    expected_recent = float(np.trapezoid(omori_rate(grid), grid))
    mean_poisson = HORIZON * lam_bar
    observed = int(np.sum((times > T_MAIN) & (times <= T_MAIN + HORIZON)))

    def poisson_tail(mean, k):
        """P(at least k events) for a Poisson mean."""
        prob = 0.0
        term = np.exp(-mean)
        for i in range(k):
            prob += term
            term *= mean / (i + 1)
        return 1.0 - prob

    print(f"  a Poisson model with the catalogue mean {lam_bar:.4f} events/day:")
    print(f"    expected events in the next {HORIZON:.0f} days = "
          f"{mean_poisson:.3f}")
    print(f"    P(at least 1) = {poisson_tail(mean_poisson, 1):.4f}, "
          f"P(at least 3) = {poisson_tail(mean_poisson, 3):.4f}")
    print(f"  a clustered model evaluated just after the mainshock:")
    print(f"    expected events = {expected_recent:.3f} "
          f"({expected_recent / mean_poisson:.0f}x the Poisson expectation)")
    print(f"    P(at least 1) = {poisson_tail(expected_recent, 1):.4f}, "
          f"P(at least 3) = {poisson_tail(expected_recent, 3):.4f}")
    print(f"  the simulation produced {observed} events in the 30 days after the")
    print(f"  mainshock, against a Poisson expectation of {mean_poisson:.1f}")
    print("  the same catalogue therefore supports two forecasts whose expected")
    print("  counts differ by a factor of "
          f"{expected_recent / mean_poisson:.0f}, and the difference is the")
    print("  conditioning: what is happening NOW is the input, not the long-run")
    print("  average")

    section("4. Recovering the Omori decay exponent")
    tau = np.sort(times[times > T_MAIN] - T_MAIN)
    edges = np.logspace(np.log10(0.2), np.log10(60.0), 9)
    counts_b, _ = np.histogram(tau[tau <= 60.0], bins=edges)
    centres = np.sqrt(edges[:-1] * edges[1:])
    widths = np.diff(edges)
    rate = counts_b / widths
    keep = counts_b > 0
    x_fit = np.log10(centres[keep] + OMORI_C)
    y_fit = np.log10(rate[keep])
    slope, intercept = np.polyfit(x_fit, y_fit, 1)
    residual = y_fit - (slope * x_fit + intercept)
    dof = max(keep.sum() - 2, 1)
    slope_se = np.sqrt(np.sum(residual ** 2) / dof
                       / np.sum((x_fit - x_fit.mean()) ** 2))
    print(f"  binned aftershock rate over 8 log-spaced bins from 0.2 to 60 days")
    print(f"  counts per bin: " + ", ".join(str(int(c)) for c in counts_b))
    print(f"  least-squares slope of log10(rate) against log10(tau + c) = "
          f"{slope:+.3f}")
    print(f"  recovered p = {-slope:.3f} against the generator's {OMORI_P:.2f} "
          f"(error {-slope - OMORI_P:+.3f})")
    print(f"  least-squares standard error of the slope = {slope_se:.3f}, so the")
    print(f"  error is {abs(-slope - OMORI_P) / slope_se:.2f} standard errors: the")
    print("  estimate is consistent with the truth but does not pin it")
    print(f"  recovered log10(K) = {intercept:+.3f} "
          f"(generator {np.log10(OMORI_K):+.3f})")
    print("  the honest report is the estimate WITH its standard error, the")
    print("  binning, and the count per bin: "
          f"{int(counts_b[keep].sum())} aftershocks across")
    print("  eight bins cannot resolve p more finely than a few tenths, and a")
    print("  real study needs many sequences, not a longer window")
    print("\nSYNTHETIC: this catalogue was generated here, so the truth is known.")
    print("A real rate model must state the magnitude of completeness, the")
    print("declustering rule and the catalogue's own reporting changes.")


if __name__ == "__main__":
    main()
