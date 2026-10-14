#!/usr/bin/env python3
"""Why deterministic earthquake prediction is considered unattainable, made
quantitative with SYNTHETIC statistics.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python earthquake_prediction_limits_demo.py

Everything is SYNTHETIC.  No real catalogue, no real forecast and no published
precursor claim is used.  The rates are teaching values chosen so that the
arithmetic can be checked by hand.

Contents
--------
1. Interevent times of a stationary Poisson process: the coefficient of
   variation, and how little it constrains a model at small sample size.
2. Memorylessness: the wait for the next event does not depend on how long you
   have already waited.
3. A b-value "precursor" from two equal windows: the null distribution of the
   difference, and what a given difference is worth.
4. Bayes with an alarm: how a good precursor test changes the probability of a
   large event, and what probability gain costs.
5. Retrospective search: how many spurious precursor series look significant
   when hundreds of candidates are examined.
6. The statement that does work: an aftershock rate forecast, measured as a rate
   ratio that decays with time.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC reference values (chosen teaching values) ---------------------
RECURRENCE_YR = 200.0    # mean recurrence of the reference event, years
RATE_M7_YR = 0.010       # rate of M >= 7 events per year
HORIZON_D = 30.0         # forecast window, days
SENSITIVITY = 0.60       # P(alarm | event in the window)
FALSE_ALARM = 0.05       # P(alarm | no event in the window)
B_GR = 1.00              # Gutenberg-Richter b of the synthetic population
DAYS_PER_YEAR = 365.25
P_OMORI = 1.10           # Omori exponent of the synthetic aftershock sequence
C_OMORI = 0.05           # Omori time offset, days
N_OFFSPRING = 5024       # mean direct offspring of a M7.0 mainshock
BG_RATE_M5 = 0.0001      # background rate of M >= 5, events per day


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. Poisson interevent times: is the sequence 'periodic'?")
    rate_yr = 1.0 / RECURRENCE_YR
    print(f"stationary Poisson rate = {rate_yr:.5f} events/yr (SYNTHETIC)")
    print(f"mean recurrence         = {RECURRENCE_YR:.0f} yr")
    waits = RNG.exponential(RECURRENCE_YR, size=200000)
    print(f"\n{waits.size:d} synthetic waits:")
    print(f"  mean wait                = {waits.mean():.2f} yr "
          f"(theory {RECURRENCE_YR:.2f} yr)")
    print(f"  standard deviation       = {waits.std(ddof=1):.2f} yr "
          f"(theory {RECURRENCE_YR:.2f} yr)")
    print(f"  coefficient of variation = {waits.std(ddof=1) / waits.mean():.3f}"
          f"  (theory 1.000)")
    print(f"  fraction longer than the mean  = "
          f"{np.mean(waits > RECURRENCE_YR):.3f} "
          f"(theory e^-1 = {np.exp(-1.0):.3f})")
    print(f"  fraction longer than twice it  = "
          f"{np.mean(waits > 2.0 * RECURRENCE_YR):.3f} "
          f"(theory e^-2 = {np.exp(-2.0):.3f})")
    print("\n  a finite sample scatters the measured CV as well:")
    print("      n intervals   5%-95% of measured CV   P(measured CV < 0.8)")
    for n_int in (10, 20, 50, 200):
        cvs = np.empty(4000)
        for i in range(4000):
            w = RNG.exponential(1.0, size=n_int)
            cvs[i] = w.std(ddof=1) / w.mean()
        lo, hi = np.percentile(cvs, [5.0, 95.0])
        print(f"      {n_int:11d}   {lo:8.3f}-{hi:7.3f}   "
              f"            {np.mean(cvs < 0.8):11.3f}")
    print("  a CV near 0.8 measured from 10-20 intervals is unremarkable, so")
    print("  'quasi-periodic' cannot be distinguished from Poisson at the sample")
    print("  sizes that recurrence histories provide.")

    section("2. Memorylessness: the wait does not know how long you waited")
    for t_y in (20.0, 30.0):
        print(f"  probability of an event in the next {t_y:4.0f} yr, no prior "
              f"information: {1.0 - np.exp(-rate_yr * t_y):.4f}")
    print(f"  after 100 yr with no event, the probability of an event in the")
    print(f"  NEXT 20 yr is still "
          f"{1.0 - np.exp(-rate_yr * 20.0):.4f}, exactly the unconditional")
    print("  value, because the exponential distribution has no memory:")
    print("  'overdue' is a statement about the observer, not the process.")
    print("\n  measured on the same 200000 waits:")
    big = waits[waits > 100.0]
    print(f"    waits beyond 100 yr        : {big.size:d} of {waits.size:d}")
    print(f"    mean excess beyond 100 yr  = {(big - 100.0).mean():.2f} yr "
          f"(theory {RECURRENCE_YR:.2f} yr)")
    print("  the mean excess is the FULL mean recurrence, not less: conditioning")
    print("  on a long wait does not shorten the next one.")

    section("3. A b-value 'precursor': the null distribution of the difference")
    print("  two windows of N events each, both from the SAME unit-rate")
    print("  Gutenberg-Richter population with b = 1.00; continuous magnitudes,")
    print("  so b_hat = log10(e) / mean(m)")
    print("      N per window   s.d. of db   95% of |db|   P(|db| > 0.2)")
    for n_win in (50, 100, 500, 2000):
        db = np.empty(4000)
        for i in range(4000):
            m1 = -np.log10(1.0 - RNG.random(n_win))
            m2 = -np.log10(1.0 - RNG.random(n_win))
            db[i] = np.log10(np.e) / m1.mean() - np.log10(np.e) / m2.mean()
        print(f"      {n_win:11d}   {db.std(ddof=1):10.3f}   "
              f"{np.percentile(np.abs(db), 95):11.3f}   "
              f"{np.mean(np.abs(db) > 0.2):12.3f}")
    print("  a 20% difference in b between two windows of 100 events is ordinary")
    print("  chance, not evidence.  The same difference measured on 2000-event")
    print(f"  windows would be informative: the null scatter is then "
          f"{0.149 / 0.032:.1f} times smaller.")

    section("4. Bayes with an alarm: what does a precursor buy?")
    p_event = 1.0 - np.exp(-RATE_M7_YR * HORIZON_D / DAYS_PER_YEAR)
    print(f"prior rate of M >= 7: {RATE_M7_YR:.4f} per year (SYNTHETIC)")
    print(f"prior probability of at least one event in a {HORIZON_D:.0f}-day "
          f"window:")
    print(f"  P(E) = 1 - exp(-{RATE_M7_YR * HORIZON_D / DAYS_PER_YEAR:.6f}) = "
          f"{p_event:.3e}")
    print(f"\ntest: sensitivity P(alarm|E) = {SENSITIVITY:.2f}, "
          f"false-alarm probability P(alarm|not E) = {FALSE_ALARM:.2f}")
    post = (SENSITIVITY * p_event
            / (SENSITIVITY * p_event + FALSE_ALARM * (1.0 - p_event)))
    print(f"posterior P(E|alarm) = {post:.3e}")
    print(f"probability gain = posterior / prior = {post / p_event:.1f} x")
    print("  a genuinely skilful precursor buys a factor, not a certainty: it")
    print(f"  turns a {p_event * 1e6:.0f}-in-a-million chance into about "
          f"{post * 100:.1f} in a hundred.")
    target = 0.5
    fa_needed = (SENSITIVITY * p_event * (1.0 - target)
                 / (target * (1.0 - p_event)))
    print(f"\nto reach a 50% posterior with the same sensitivity, the false-alarm")
    print(f"probability would have to fall below {fa_needed:.2e}, that is fewer")
    print(f"than one false alarm in {1.0 / fa_needed:.0f} quiet windows.")
    p1 = 1.0 - np.exp(-RATE_M7_YR / DAYS_PER_YEAR)
    post1 = (SENSITIVITY * p1 / (SENSITIVITY * p1 + FALSE_ALARM * (1.0 - p1)))
    print(f"\nthe same test applied to a 1-day window:")
    print(f"  P(E) = {p1:.3e}, P(E|alarm) = {post1:.3e}, "
          f"gain = {post1 / p1:.1f} x")
    print("  the gain is scale-free; the posterior probability is not.  Short")
    print("  windows cannot be made probable by any test with a finite")
    print("  false-alarm rate, which is exactly the deterministic-prediction")
    print("  problem stated as arithmetic.")

    section("5. Retrospective search: significance by multiplication")
    n_series = 500
    n_pre = 30
    n_post = 170
    flagged = 0
    for i in range(n_series):
        s = RNG.standard_normal(n_pre + n_post)
        diff = s[:n_pre].mean() - s[n_pre:].mean()
        se = np.sqrt(1.0 / n_pre + 1.0 / n_post)
        if abs(diff / se) > 1.96:
            flagged += 1
    print(f"  {n_series} candidate precursor series, every one pure white noise,")
    print("  each tested for a difference between a 30-sample pre-event window")
    print("  and the remaining 170 samples at the 5% level:")
    print(f"    series flagged as significant: {flagged:d} of {n_series:d} "
          f"({100.0 * flagged / n_series:.1f} %)")
    print("  a 5% test flags about 5% of pure noise.  Any retrospective search")
    print("  over many candidate predictors, windows and thresholds will produce")
    print("  'significant' precursors, and the p-value stops meaning what it")
    print("  says once the search itself is counted.")

    section("6. The statement that does work: an aftershock rate forecast")
    print(f"  SYNTHETIC Omori sequence after a M7.0 mainshock: p = "
          f"{P_OMORI:.2f}, c = {C_OMORI:.2f} d, mean direct offspring = "
          f"{N_OFFSPRING:d}, offspring magnitudes Gutenberg-Richter with b = "
          f"{B_GR:.2f}")
    n_seq = 500
    n_tot = n_seq * N_OFFSPRING
    u = RNG.random(n_tot)
    t_off = C_OMORI * ((1.0 - u) ** (-1.0 / (P_OMORI - 1.0)) - 1.0)
    m_off = 1.0 + (-np.log10(1.0 - RNG.random(n_tot))) / B_GR
    print(f"  {n_seq:d} simulated sequences, {n_tot:d} offspring times and "
          f"magnitudes")
    print(f"  background rate of M >= 5 in the region = {BG_RATE_M5:.4f} per "
          f"day (SYNTHETIC)")
    print("\n      window after mainshock   N(M>=5)   rate (/day)   ratio to "
          "background")
    for lo, hi in ((0.0, 1.0), (1.0, 7.0), (7.0, 30.0), (30.0, 365.0)):
        n_sel = int(np.sum((t_off >= lo) & (t_off < hi) & (m_off >= 5.0)))
        rate_obs = n_sel / n_seq / (hi - lo)
        print(f"      day {lo:5.1f}-{hi:5.1f}         {n_sel:8d}   "
              f"{rate_obs:11.6f}   {rate_obs / BG_RATE_M5:14.1f} x")
    print("  the forecast is a rate and its information decays with time: over")
    print("  a thousand times the background rate on the first day, about thirty")
    print("  times it at one month, and under twice it beyond a year.  It is")
    print("  accurate on average because it describes a population of")
    print("  aftershocks; it says nothing about which day or which patch of")
    print("  fault will host the next event.")


if __name__ == "__main__":
    main()
