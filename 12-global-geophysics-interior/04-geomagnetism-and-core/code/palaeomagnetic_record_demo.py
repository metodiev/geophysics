#!/usr/bin/env python3
"""The palaeomagnetic record: reversal rates, superchrons, and sampling bias.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python palaeomagnetic_record_demo.py

Everything here is a SYNTHETIC teaching model.  The polarity sequence is
generated from an invented rate function; it is not the geomagnetic polarity
timescale (GPTS) or any published chronology, and no measured reversal age,
palaeointensity or site appears anywhere.

Contents
--------
1. A synthetic reversal chronology and the statistics of its intervals.
2. Are the intervals Poisson?  Coefficient of variation, skewness and a
   Kolmogorov-Smirnov test against the fitted exponential.
3. Superchrons: the probability of a long gap under a constant rate, and the
   rate drop a superchron requires.
4. Sampling bias: how many reversals a magnetostratigraphy of a given
   resolution actually sees.
5. Rate variation with time, tested by a parametric bootstrap.
6. The time-averaged field and the bias a detection threshold produces.
7. Verification against direct simulation.
"""

import numpy as np
from scipy import stats

RNG = np.random.default_rng(20261014)

AGE_SPAN = 300.0        # Myr of synthetic record
RATE_YOUNG = 5.0        # reversals per Myr, adopted recent rate
RATE_OLD = 1.0          # reversals per Myr, adopted early rate
SUPERCHRON = (120.0, 160.0)   # Myr window with zero rate in the synthetic record
VADM_MEAN = 8.0e22      # A m^2, adopted mean virtual axial dipole moment


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def rate_function(t, with_superchron=True):
    """Adopted reversal rate in reversals per Myr at age t (Myr before present)."""
    base = RATE_OLD + (RATE_YOUNG - RATE_OLD) * (1.0 - t / AGE_SPAN)
    if with_superchron and SUPERCHRON[0] <= t <= SUPERCHRON[1]:
        return 0.0
    return base


def simulate_sequence(rng, with_superchron=True, t0=0.0, t1=AGE_SPAN):
    """Thinning method for an inhomogeneous Poisson process of reversals."""
    times = []
    t = t0
    t_max_rate = RATE_YOUNG * 1.05
    while t < t1:
        t += -np.log(rng.random()) / t_max_rate
        if t >= t1:
            break
        if rng.random() < rate_function(t, with_superchron) / t_max_rate:
            times.append(t)
    return np.array(times)


def simulate_stationary(rng, rate, t0=0.0, t1=AGE_SPAN):
    """A stationary Poisson reversal sequence at a fixed rate."""
    n = rng.poisson(rate * (t1 - t0))
    return np.sort(rng.random(n) * (t1 - t0) + t0)


def main():
    section("1. A synthetic reversal chronology")
    times = simulate_sequence(RNG)
    intervals = np.diff(times)
    print(f"adopted rate function: {RATE_OLD:.1f} to {RATE_YOUNG:.1f} reversals/Myr"
          f" over {AGE_SPAN:.0f} Myr, with a zero-rate window inside"
          f" {SUPERCHRON[0]:.0f}-{SUPERCHRON[1]:.0f} Ma")
    print(f"reversals generated: {times.size}")
    print(f"mean interval: {intervals.mean():.3f} Myr"
          f" (median {np.median(intervals):.3f} Myr)")
    print(f"shortest {intervals.min():.4f} Myr, longest {intervals.max():.3f} Myr")
    q = np.quantile(intervals, [0.1, 0.25, 0.5, 0.75, 0.9])
    print(f"quantiles 10/25/50/75/90 %: {q[0]:.3f} {q[1]:.3f} {q[2]:.3f}"
          f" {q[3]:.3f} {q[4]:.3f} Myr")
    in_sc = intervals[(times[:-1] >= SUPERCHRON[1]) & (times[1:] <= SUPERCHRON[0])]
    print(f"the longest interval, {intervals.max():.1f} Myr, is the synthetic"
          f" superchron itself")

    section("2. Are the intervals Poisson?")
    inside = intervals[intervals < intervals.max() - 0.5]
    cv = inside.std(ddof=1) / inside.mean()
    print(f"coefficient of variation of the non-superchron intervals: {cv:.3f}")
    print("a Poisson process gives CV = 1 exactly, so the observed excess is the")
    print("variance contributed by the changing rate")
    ks = stats.kstest(inside, "expon", args=(0.0, inside.mean()))
    print(f"KS statistic against the fitted exponential: {ks.statistic:.4f},"
          f" p = {ks.pvalue:.4f}")
    print(f"skewness of the intervals: {stats.skew(inside):.3f}"
          " (an exponential has skewness 2)")
    print("interpretation: the record is piecewise Poisson with a rate that varies,")
    print("so pooled intervals are not exponential even though each short segment")
    print("is.  The KS test does not reject a single exponential here because 750")
    print("intervals give it little power against a modest rate variation: a")
    print("non-rejection is not evidence of stationarity")

    section("3. Superchrons under a constant rate")
    for rate in (RATE_YOUNG, 2.0):
        for gap in (10.0, 20.0, 30.0, 40.0):
            log10_p = -rate * gap / np.log(10.0)
            print(f"  rate {rate:4.1f}/Myr: P(gap >= {gap:2.0f} Myr) = "
                  f"{np.exp(-rate * gap):.3e}   (log10 = {log10_p:.1f})")
    gap_obs = float(intervals.max())
    print(f"\nthe synthetic gap is {gap_obs:.1f} Myr.  A constant rate of"
          f" {RATE_YOUNG:.1f}/Myr assigns it a probability of"
          f" {np.exp(-RATE_YOUNG * gap_obs):.2e}")
    required = np.log(1.0 / 0.05) / gap_obs
    print(f"for that gap to be a 5% fluctuation the rate would have to be"
          f" {required:.4f}/Myr, a factor {RATE_YOUNG / required:.1f} below the"
          " recent value")
    print("so a superchron is not an unusual gap in a stationary process: it is")
    print("evidence that the process is not stationary")

    section("4. Sampling bias: what a magnetostratigraphy sees")
    print("  resolution (Myr)   reversals seen   fraction of the truth")
    for res in (0.05, 0.1, 0.25, 0.5, 1.0, 2.0):
        grid = np.arange(0.0, AGE_SPAN + res, res)
        polar = np.array([np.searchsorted(times, g) % 2 for g in grid])
        seen = int(np.sum(np.abs(np.diff(polar)) > 0))
        print(f"  {res:16.2f} {seen:16d} {seen / times.size:22.3f}")
    print("\nthe bias is one-sided: short polarity intervals are merged rather than")
    print("invented, so a coarse sampling always *under*-counts reversals and")
    print("thus under-estimates the rate")

    section("5. Rate variation with time")
    windows = np.arange(0.0, AGE_SPAN, 20.0)
    rates = []
    for w in windows:
        n = int(np.sum((times >= w) & (times < w + 20.0)))
        rates.append(n / 20.0)
    rates = np.array(rates)
    mid = windows + 10.0
    ok = (mid < SUPERCHRON[0]) | (mid > SUPERCHRON[1])
    slope = float(np.polyfit(mid[ok], rates[ok], 1)[0])
    print(f"rates in {windows.size} windows of 20 Myr (reversals/Myr):")
    print("  " + " ".join(f"{r:5.2f}" for r in rates))
    print(f"\nlinear trend over the non-superchron windows: {slope:+.5f} per Myr"
          " per Myr")
    n_boot = 200
    mean_rate = times.size / AGE_SPAN
    null = []
    for _ in range(n_boot):
        sim = simulate_stationary(RNG, mean_rate)
        r = np.array([np.sum((sim >= w) & (sim < w + 20.0)) / 20.0 for w in windows])
        null.append(float(np.polyfit(mid, r, 1)[0]))
    null = np.array(null)
    p_value = float(np.mean(np.abs(null) >= abs(slope)))
    print(f"bootstrap null: {n_boot} *stationary* sequences at the record mean rate"
          f" {mean_rate:.3f}/Myr")
    print(f"  null slope sd {null.std(ddof=1):.5f}, p = {p_value:.3f}")
    print(f"the synthetic trend is {abs(slope) / null.std(ddof=1):.2f} standard"
          " deviations: detectable with this many windows, and only because the")
    print("adopted rate change is large")

    section("6. The time-averaged field and a detection threshold")
    n_sites = 400
    true_vadm = RNG.lognormal(mean=np.log(VADM_MEAN), sigma=0.45, size=n_sites)
    threshold = 0.4 * VADM_MEAN
    kept = true_vadm[true_vadm >= threshold]
    print(f"adopted distribution: lognormal, median {VADM_MEAN:.2e} A m^2,"
          f" sigma of log = 0.45")
    print(f"mean of {n_sites} synthetic results          :"
          f" {true_vadm.mean():.3e} A m^2")
    print(f"detection threshold at {threshold:.2e} A m^2 keeps {kept.size} results")
    print(f"mean of the censored set                        :"
          f" {kept.mean():.3e} A m^2")
    print(f"bias from censoring: {(kept.mean() / true_vadm.mean() - 1) * 100:+.1f}%")
    print("\n  threshold (A m^2)   kept   mean of kept (1e22 A m^2)   bias")
    for frac in (0.2, 0.4, 0.6, 0.8):
        thr = frac * VADM_MEAN
        k = true_vadm[true_vadm >= thr]
        print(f"  {thr:17.2e} {k.size:6d} {k.mean() / 1e22:25.3f}"
              f" {(k.mean() / true_vadm.mean() - 1) * 100:+7.1f}%")
    print("the bias is one-sided, grows as the threshold rises, and is invisible")
    print("in a database that records only accepted results")

    section("7. Verification against direct simulation")
    print("  rate/Myr   simulated P(max gap>=20 Myr)   union bound")
    for rate in (0.1, 0.25, 0.5, 1.0):
        rng = np.random.default_rng(7)
        gaps = []
        for _ in range(400):
            t = simulate_stationary(rng, rate)
            gaps.append(np.max(np.diff(t)) if t.size > 1 else np.nan)
        gaps = np.array(gaps)
        sim_p = float(np.nanmean(gaps >= 20.0))
        union = 1.0 - np.exp(-AGE_SPAN * rate * np.exp(-20.0 * rate))
        print(f"  {rate:8.2f} {sim_p:32.4f} {union:13.6f}")
    print("the comparison is with the probability that *any* gap in the record")
    print("exceeds 20 Myr, which is about N*exp(-rate*20) for N events, not with the")
    print("probability for one interval")
    ks_all = stats.kstest(inside, "expon", args=(0.0, inside.mean()))
    print(f"\nKS p-value of the intervals against a single exponential:"
          f" {ks_all.pvalue:.4f}")
    print(f"mean interval {inside.mean():.4f} Myr against 1/mean-rate"
          f" {1.0 / inside.mean():.4f} reversals/Myr (the same number twice: that"
          " is the definition)")
    print("\nSYNTHETIC teaching model; no measured reversal age is used.")


if __name__ == "__main__":
    main()
