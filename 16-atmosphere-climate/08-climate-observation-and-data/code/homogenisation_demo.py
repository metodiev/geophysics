#!/usr/bin/env python3
"""Homogenisation and bias adjustment: detecting a step change in a station
record by a neighbour-difference t-statistic scan, measuring how much the
adjustment repairs the trend, how large a step is detectable, and how two
superficially similar quantile-mapping procedures give different trends.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python homogenisation_demo.py

Everything is SYNTHETIC.  The stations, the step change, the reference series and
the model/observation pairs are chosen teaching constructions.  No real station,
network, dataset or published adjustment is used, and no published number is
quoted.

Contents
--------
1. A synthetic truth, a reference station and a candidate station with a step.
2. Breakpoint detection by a neighbour-difference t-statistic scan.
3. Detection performance versus step size, and the false-positive rate.
4. What the adjustment does to the trend (Monte Carlo over realisations).
5. Bias adjustment and trends: a fixed quantile mapping preserves the trend, a
   misapplied one destroys it.
6. What a homogenisation report must state.
"""

import numpy as np
from scipy import stats

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC setting (chosen, not measured) -------------------------------
N_YEARS = 80
TRUE_TREND = 0.020            # K/yr in the synthetic regional truth
STEP_YEAR = 40                # the instrument change at the candidate station
STEP_SIZE = 0.50              # K, the inhomogeneity to be detected
STATION_NOISE = 0.20          # K, independent annual noise at each station
TRUTH_NOISE = 0.50            # K, regional anomaly noise (AR(1), phi below)
PHI = 0.40                    # lag-1 autocorrelation of the regional anomaly
DETECT_T = 3.0                # |t| threshold used as the detection criterion
N_MC = 300                    # Monte Carlo realisations


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def ols_trend(x):
    """OLS slope and its standard error for a unit-spaced series."""
    n = x.size
    t = np.arange(n, dtype=float)
    tb = t.mean()
    sxx = np.sum((t - tb) ** 2)
    slope = np.sum((t - tb) * x) / sxx
    resid = x - (x.mean() + slope * (t - tb))
    s2 = np.sum(resid ** 2) / (n - 2)
    return slope, np.sqrt(s2 / sxx)


def regional_truth():
    """AR(1) regional anomaly around a linear trend (SYNTHETIC)."""
    e = np.zeros(N_YEARS)
    for t in range(1, N_YEARS):
        e[t] = PHI * e[t - 1] + np.sqrt(1 - PHI ** 2) * TRUTH_NOISE * \
            RNG.standard_normal()
    return TRUE_TREND * np.arange(N_YEARS) + e


def make_pair(step_size=STEP_SIZE, step_year=STEP_YEAR):
    """Return (truth, reference station, candidate station with a step)."""
    truth = regional_truth()
    ref = truth + STATION_NOISE * RNG.standard_normal(N_YEARS)
    cand = truth + STATION_NOISE * RNG.standard_normal(N_YEARS)
    if step_size:
        cand = cand + step_size * (np.arange(N_YEARS) >= step_year)
    return truth, ref, cand


def scan_breakpoint(diff):
    """Return the year maximising |t| of a mean difference across the split."""
    best_t, best_year = 0.0, None
    for t0 in range(5, diff.size - 5):
        a, b = diff[:t0], diff[t0:]
        se = np.sqrt(a.var(ddof=1) / a.size + b.var(ddof=1) / b.size)
        if se == 0:
            continue
        stat = abs(a.mean() - b.mean()) / se
        if stat > best_t:
            best_t, best_year = stat, t0
    return best_year, best_t


def main():
    section("1. A synthetic truth and two neighbouring stations")
    truth, ref, cand = make_pair()
    print(f"  {N_YEARS} years, regional truth: trend {TRUE_TREND:.3f} K/yr and")
    print(f"  AR(1) anomaly noise sd {TRUTH_NOISE:.2f} K, phi = {PHI:.2f}")
    print(f"  reference station: truth + independent noise sd "
          f"{STATION_NOISE:.2f} K")
    print(f"  candidate station: truth + noise + a step of {STEP_SIZE:.2f} K "
          f"from year {STEP_YEAR}")
    print(f"  fitted trend, truth     : {ols_trend(truth)[0]:+.4f} K/yr")
    print(f"  fitted trend, candidate : {ols_trend(cand)[0]:+.4f} K/yr")
    print(f"  trend error before any adjustment: "
          f"{ols_trend(cand)[0] - ols_trend(truth)[0]:+.4f} K/yr")

    section("2. Breakpoint detection by a neighbour-difference scan")
    diff = cand - ref
    year, stat = scan_breakpoint(diff)
    print("  the reference is unbiased, so the step survives in the neighbour")
    print("  difference (candidate - reference) while the common regional signal")
    print("  cancels:")
    print(f"  detected break year = {year} (true {STEP_YEAR}), |t| = {stat:.2f}")
    print(f"  detection error = {year - STEP_YEAR:+d} years")
    offset = diff[year:].mean() - diff[:year].mean()
    adj = cand - offset * (np.arange(N_YEARS) >= year)
    print(f"  estimated adjustment = {offset:+.3f} K applied from year {year}")
    print(f"  trend before adjustment                : "
          f"{ols_trend(cand)[0]:+.4f} K/yr")
    print(f"  trend after adjustment (detected year) : {ols_trend(adj)[0]:+.4f} K/yr")
    adj_true = cand - STEP_SIZE * (np.arange(N_YEARS) >= STEP_YEAR)
    print(f"  trend after adjustment (known truth)   : "
          f"{ols_trend(adj_true)[0]:+.4f} K/yr")
    print(f"  error after adjustment (detected year) : "
          f"{ols_trend(adj)[0] - ols_trend(truth)[0]:+.4f} K/yr")

    section("3. Detection performance versus step size and the false alarms")
    print("  step (K)   detection rate (|t|>3, |year error|<=3)   mean |t|")
    for size in (0.10, 0.20, 0.30, 0.50, 0.80, 1.20):
        hits, stats_ = 0, []
        for _ in range(N_MC):
            _, r, c = make_pair(size)
            yr, st = scan_breakpoint(c - r)
            stats_.append(st)
            if st > DETECT_T and abs(yr - STEP_YEAR) <= 3:
                hits += 1
        print(f"  {size:8.2f}   {hits / N_MC:33.3f}   {np.mean(stats_):8.2f}")
    fp = 0
    for _ in range(N_MC):
        _, r, c = make_pair(0.0)
        _, st = scan_breakpoint(c - r)
        if st > DETECT_T:
            fp += 1
    print(f"  false-positive rate with NO step: {fp / N_MC:.3f} "
          f"(at |t| > {DETECT_T:.1f})")
    print(f"  A step below the noise level is not detectable, and the scan tests")
    print(f"  about {N_YEARS - 10} candidate break years, so the nominal |t| > "
          f"{DETECT_T:.1f}")
    print(f"  threshold fires on {fp / N_MC:.3f} of realisations that contain no")
    print("  break at all.  A calibrated rule must control that multiplicity.")

    section("4. What the adjustment does to the trend")
    err_before, err_after = [], []
    for _ in range(N_MC):
        tr, r, c = make_pair()
        err_before.append(ols_trend(c)[0] - ols_trend(tr)[0])
        d = c - r
        yr, st = scan_breakpoint(d)
        off = d[yr:].mean() - d[:yr].mean()
        a = c - off * (np.arange(N_YEARS) >= yr)
        err_after.append(ols_trend(a)[0] - ols_trend(tr)[0])
    err_before = np.array(err_before)
    err_after = np.array(err_after)
    print(f"  step {STEP_SIZE:.2f} K at year {STEP_YEAR}, {N_MC} realisations")
    print(f"  trend error, unadjusted: mean {err_before.mean():+.4f}, "
          f"sd {err_before.std():.4f} K/yr")
    print(f"  trend error, adjusted  : mean {err_after.mean():+.4f}, "
          f"sd {err_after.std():.4f} K/yr")
    print(f"  The adjustment removes the systematic part (mean error "
          f"{err_before.mean():+.4f}")
    print(f"  -> {err_after.mean():+.4f} K/yr) and leaves a residual of standard")
    print(f"  deviation {err_after.std():.4f} K/yr, because the break year and the")
    print(f"  step size are estimated, not known.  That residual, not the")
    print(f"  unadjusted bias, is the homogenisation uncertainty to report.")

    section("5. Bias adjustment and trends: two similar procedures")
    # A model's historical and future distributions and an observed historical one
    m_hist = RNG.normal(10.0, 2.0, 2000)
    m_fut = RNG.normal(12.0, 2.0, 2000)
    o_hist = RNG.normal(11.0, 2.0, 2000)
    print(f"  synthetic model historical mean {m_hist.mean():.2f} K, future mean "
          f"{m_fut.mean():.2f} K -> model change {m_fut.mean() - m_hist.mean():+.2f} K")
    print(f"  synthetic observed historical mean {o_hist.mean():.2f} K")

    def qm(x, src, dst):
        """Quantile mapping: map x from the src empirical CDF to the dst CDF."""
        ranks = np.searchsorted(np.sort(src), x, side="left") / (src.size + 1.0)
        ranks = np.clip(ranks, 1.0 / (src.size + 1.0), 1.0 - 1.0 / (src.size + 1.0))
        return np.quantile(dst, ranks)

    # Method A: transfer function built on the historical pair, applied to future
    fut_qm = qm(m_fut, m_hist, o_hist)
    print("  Method A -- transfer built on the historical model/observation pair,")
    print("    then applied to the future model:")
    print(f"    corrected future mean {fut_qm.mean():.2f} K -> change "
          f"{fut_qm.mean() - o_hist.mean():+.2f} K")
    # Method B: map the future model onto the historical observed distribution
    fut_qm_wrong = qm(m_fut, m_fut, o_hist)
    print("  Method B -- the future model mapped directly onto the historical")
    print("    observed distribution (a common misapplication):")
    print(f"    corrected future mean {fut_qm_wrong.mean():.2f} K -> change "
          f"{fut_qm_wrong.mean() - o_hist.mean():+.2f} K")
    print("  Both are called 'quantile mapping'.  Method A preserves the model's")
    print("  climate change signal; Method B removes it by construction, because")
    print("  it maps the future distribution onto the historical one.  Bias")
    print("  adjustment is a transfer function, and which function is applied")
    print("  decides whether a trend survives.")

    section("6. What a homogenisation report must state")
    print("  1. the detection method and the threshold (here: |t| > 3 on the")
    print("     neighbour difference);")
    print("  2. the detected break dates and their uncertainty (here the break")
    print("     year has a residual trend error, reported above);")
    print("  3. the reference series and its own homogeneity;")
    print("  4. the adjustment size and sign;")
    print("  5. the residual trend error contributed by the adjustment;")
    print("  6. the false-positive rate of the detection rule on this network.")
    print("  All numbers above are SYNTHETIC.")


if __name__ == "__main__":
    main()
