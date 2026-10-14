#!/usr/bin/env python3
"""Climate observation records: how instrument changes, network composition and
diurnal drift manufacture trends that are not in the true signal, and what a
processing chain has to do about them.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python observation_records_demo.py

Everything is SYNTHETIC.  The "stations" and the "satellite" series are chosen
teaching constructions around a known synthetic truth.  No real station,
radiosonde, satellite, mission, instrument or published temperature record is
used, and no published warming rate is quoted.

Contents
--------
1. A known truth, and three synthetic "measurement systems" observing it.
2. Naive averaging of raw records: the trend error produced by uncorrected
   instrument changes.
3. Network-composition bias: a changing set of stations manufactures a trend.
4. Satellite-style diurnal-drift bias as a spurious trend.
5. What a defensible processing chain reports, and with what uncertainty.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC truth and observing systems (chosen, not measured) -----------
N_YEARS = 120
TRUE_TREND_K_PER_YR = 0.015      # K/yr, the synthetic true trend
NOISE_K = 0.18                   # K, station-level interannual noise
STEP_YEAR = 40                   # year of an instrument change at station A
STEP_BIAS_K = 0.40               # K, the bias it introduces
DRIFT_BIAS_K_PER_YR = 0.002      # K/yr, slow siting-related drift at station B
NETWORK_CHANGE_YEAR = 60         # composition of the "network" changes here


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def trend(x, years):
    """Ordinary least-squares linear trend with its standard error."""
    A = np.column_stack([np.ones_like(years, dtype=float), years.astype(float)])
    beta, *_ = np.linalg.lstsq(A, x, rcond=None)
    resid = x - A @ beta
    dof = x.size - 2
    s2 = resid @ resid / dof
    cov = s2 * np.linalg.inv(A.T @ A)
    return beta[1], np.sqrt(cov[1, 1])


def main():
    years = np.arange(N_YEARS)
    truth = 0.0 + TRUE_TREND_K_PER_YR * years + NOISE_K * RNG.standard_normal(
        N_YEARS)
    print(f"SYNTHETIC truth: {N_YEARS} years, trend {TRUE_TREND_K_PER_YR:.3f} "
          f"K/yr,")
    print(f"  interannual noise {NOISE_K:.2f} K (same at every station here)")
    t_hat, se = trend(truth, years)
    print(f"  the truth itself fits to {t_hat:.4f} +/- {se:.4f} K/yr")

    section("1. Three synthetic observing systems")
    # Station A: instrument change at STEP_YEAR, plus its own local noise
    a = (truth - truth.mean()
         + STEP_BIAS_K * (years >= STEP_YEAR)
         + 0.05 * RNG.standard_normal(N_YEARS))
    # Station B: gradual siting-related drift
    b = (truth - truth.mean()
         + DRIFT_BIAS_K_PER_YR * years
         + 0.05 * RNG.standard_normal(N_YEARS))
    # Station C: clean, but only available in the first half of the record
    c = truth - truth.mean() + 0.05 * RNG.standard_normal(N_YEARS)
    print("  A: step bias of +0.40 K from year 40 (instrument change)")
    print("  B: linear bias drift of +0.002 K/yr (siting/microclimate)")
    print("  C: unbiased, but only present before year 60")
    for name, series in (("A", a), ("B", b), ("C", c)):
        tt, ss = trend(series, years)
        print(f"  station {name}: fitted trend {tt:+.4f} +/- {ss:.4f} K/yr "
              f"(true {TRUE_TREND_K_PER_YR:+.3f})")

    section("2. Naive averaging of raw records")
    raw_mean = np.nanmean(np.vstack([a, b, c]), axis=0)
    tt, ss = trend(raw_mean, years)
    print(f"  mean of the three raw records : {tt:+.4f} +/- {ss:.4f} K/yr")
    print(f"  true trend                    : {TRUE_TREND_K_PER_YR:+.4f} K/yr")
    print(f"  trend error from bias          : {tt - TRUE_TREND_K_PER_YR:+.4f} K/yr "
          f"({100 * (tt - TRUE_TREND_K_PER_YR) / TRUE_TREND_K_PER_YR:+.0f}%)")
    # correct station A by a step adjustment detected at the known break
    a_corr = a - STEP_BIAS_K * (years >= STEP_YEAR)
    b_corr = b - DRIFT_BIAS_K_PER_YR * years
    clean_mean = np.nanmean(np.vstack([a_corr, b_corr, c]), axis=0)
    tc, sc = trend(clean_mean, years)
    print(f"  after adjusting A and B       : {tc:+.4f} +/- {sc:.4f} K/yr")
    print(f"  residual error                 : {tc - TRUE_TREND_K_PER_YR:+.4f} K/yr")
    print("  The raw average is not wrong because the stations are noisy --")
    print("  noise averages out.  It is wrong because the biases are systematic")
    print("  and change in time, which is exactly what an inhomogeneity is.")

    section("3. Network-composition bias across a coverage change")
    # A "network mean" whose composition changes: the reliable stations stop
    # in year 60 and are replaced by stations in a warmer (biased) region.
    warm_bias = 0.8      # K, offset of the replacement sites
    def composed(year_start, year_end, replacement=False):
        idx = np.arange(year_start, year_end)
        if replacement:
            return truth[idx] + warm_bias + 0.05 * RNG.standard_normal(idx.size)
        return truth[idx] + 0.05 * RNG.standard_normal(idx.size)
    early = composed(0, NETWORK_CHANGE_YEAR, replacement=False)
    late = composed(NETWORK_CHANGE_YEAR, N_YEARS, replacement=True)
    composite = np.concatenate([early, late])
    tt, ss = trend(composite, years)
    print(f"  reliable sites only before year {NETWORK_CHANGE_YEAR}; replacement")
    print(f"  sites have a +{warm_bias:.1f} K mean offset (a chosen value)")
    print(f"  composite trend               : {tt:+.4f} +/- {ss:.4f} K/yr")
    print(f"  true trend                    : {TRUE_TREND_K_PER_YR:+.4f} K/yr")
    print(f"  apparent trend inflation      : {tt - TRUE_TREND_K_PER_YR:+.4f} K/yr")
    print(f"  the discontinuity at year {NETWORK_CHANGE_YEAR} is "
          f"{warm_bias:.2f} K, which is")
    print("  larger than the entire true change over the record -- network")
    print("  composition is a first-order term, not a detail.")

    section("4. Satellite-style diurnal drift as a spurious trend")
    # A satellite-like series observes at a local time that drifts slowly; the
    # diurnal cycle then leaks into the record as a trend.  The drift here is
    # deliberately exaggerated so that the effect is visible.
    amp = 1.5                       # K, amplitude of the synthetic diurnal cycle
    total_drift_h = 6.0             # hours of local-time drift over the record
    local_hour = 13.0 + (total_drift_h / N_YEARS) * years
    phase = 2.0 * np.pi * (local_hour - 14.0) / 24.0    # 14 h reference
    diurnal = amp * (np.cos(phase) - np.cos(phase[0]))
    sat = truth + diurnal + 0.05 * RNG.standard_normal(N_YEARS)
    tt, ss = trend(sat, years)
    t_corr, s_corr = trend(sat - diurnal, years)
    print(f"  synthetic diurnal cycle amplitude {amp:.1f} K; local observation")
    print(f"  time drifts {total_drift_h:.1f} h over the {N_YEARS}-year record")
    print(f"  (exaggerated relative to a real drift so the effect is visible)")
    print(f"  uncorrected trend              : {tt:+.4f} +/- {ss:.4f} K/yr")
    print(f"  after removing the diurnal term: {t_corr:+.4f} +/- {s_corr:.4f} K/yr")
    print(f"  true trend                     : {TRUE_TREND_K_PER_YR:+.4f} K/yr")
    print(f"  spurious trend from the drift  : {tt - TRUE_TREND_K_PER_YR:+.4f} K/yr "
          f"({100 * (tt - TRUE_TREND_K_PER_YR) / TRUE_TREND_K_PER_YR:+.0f}%)")
    print(f"  the diurnal term changes by {diurnal[-1] - diurnal[0]:+.2f} K across")
    print("  the record, which is why an uncorrected drift of a few hours can")
    print("  produce or remove a trend of the same size as the signal.")

    section("5. What a defensible processing chain reports")
    print("  Every one of the records above is a PRODUCT, not a direct")
    print("  measurement: it is a series with a processing chain attached.")
    print("  A defensible product states, at minimum:")
    print("    1. which observations were used, and which were left out;")
    print("    2. how instrument and siting changes were detected and adjusted;")
    print("    3. how the network composition changed over time, and how the")
    print("       index is made insensitive to it (e.g. anomalies, not absolutes);")
    print("    4. how satellite drift and inter-satellite offsets were removed;")
    print("    5. an uncertainty that includes structural, not only random,")
    print("       error.");
    print("  The numbers above are SYNTHETIC and the biases are chosen, but the")
    print("  failure modes are the real ones.")


if __name__ == "__main__":
    main()
