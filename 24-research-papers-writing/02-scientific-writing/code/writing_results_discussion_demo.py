#!/usr/bin/env python3
"""Results and Discussion: significance, effect size and overclaiming.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python writing_results_discussion_demo.py

Everything here is SYNTHETIC.  The experiments are simulated from the normal
model with chosen effect sizes and sample sizes; no data set is analysed.

Sections
--------
1. Calibration: what a truly null effect produces.
2. Power and observed effect size at three sample sizes.
3. The significance filter: inflated effects among declared winners.
4. Multiplicity: twenty tests, and what a correction costs.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC experiment parameters (chosen teaching values) ---------------
TRUE_EFFECT = 0.20         # effect size in units of the within-group sd
N_REPS = 1000
SAMPLE_SIZES = (20, 200, 2000)
ALPHA = 0.05
N_TESTS = 20


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def two_sample_ttest(n, effect, reps, rng):
    """Return (p-values, Cohen's d) for reps simulated two-group comparisons."""
    x = rng.normal(0.0, 1.0, (reps, n))
    y = rng.normal(effect, 1.0, (reps, n))
    diff = y.mean(axis=1) - x.mean(axis=1)
    sp = np.sqrt(0.5 * (x.var(axis=1, ddof=1) + y.var(axis=1, ddof=1)))
    d = diff / sp
    se = sp * np.sqrt(2.0 / n)
    t = diff / se
    # two-sided p from the normal approximation (n is large in every case shown)
    from math import erfc, sqrt
    p = np.array([erfc(abs(ti) / sqrt(2.0)) for ti in t])
    return p, d


def main():
    section("1. Calibration: what a truly null effect produces")
    print("SYNTHETIC experiments: two-group comparisons simulated from the normal")
    print("model with chosen effect sizes and sample sizes; no data set is analysed.")
    for n in SAMPLE_SIZES:
        p, d = two_sample_ttest(n, 0.0, N_REPS, RNG)
        rate = float(np.mean(p < ALPHA))
        se = float(np.sqrt(ALPHA * (1 - ALPHA) / N_REPS))
        print(f"  n = {n:5d} per group, true effect 0: false positives "
              f"{rate * 100:5.1f} % +/- {se * 100:.1f} (1 s.e.), "
              f"mean observed d = {d.mean():+.4f}")
    print(f"  nominal rate = {ALPHA * 100:.0f} %; a calibrated test recovers it")
    print("  -> significance is a statement about noise, not about importance.")

    section("2. Power and observed effect size at three sample sizes")
    print(f"  true effect = {TRUE_EFFECT:.2f} within-group standard deviations")
    for n in SAMPLE_SIZES:
        p, d = two_sample_ttest(n, TRUE_EFFECT, N_REPS, RNG)
        print(f"  n = {n:5d} per group: power (p < {ALPHA}) = "
              f"{np.mean(p < ALPHA) * 100:5.1f} %, "
              f"median p = {np.median(p):.2e}, "
              f"p < 0.001 in {np.mean(p < 0.001) * 100:5.1f} %, "
              f"mean d = {d.mean():+.3f} +/- {d.std(ddof=1):.3f}")
    print("  -> the effect size stays at 0.20 while the p-value falls by orders of")
    print("     magnitude; a tiny p-value is not a large effect.")

    section("3. The significance filter: inflated effects among declared winners")
    for n in SAMPLE_SIZES:
        p, d = two_sample_ttest(n, TRUE_EFFECT, N_REPS, RNG)
        winners = p < ALPHA
        reported = d[winners].mean()
        print(f"  n = {n:5d}: {int(winners.sum())} of {N_REPS} studies declared "
              f"significant; their mean d = {reported:+.3f} "
              f"(inflation {reported / TRUE_EFFECT:.2f}x the true "
              f"{TRUE_EFFECT:.2f})")
        print(f"           an independent replication at the same n is expected to "
              f"find d = {TRUE_EFFECT:.2f}, "
              f"{(reported - TRUE_EFFECT) / reported * 100:4.1f} % below the "
              f"reported value")
    print("  -> smaller studies must clear a higher hurdle of luck, so their published")
    print("     effects are the most inflated: the 'winner's curse'.")

    section("4. Multiplicity: twenty tests, and what a correction costs")
    null_p = RNG.random((N_REPS, N_TESTS))
    any_sig = np.any(null_p < ALPHA, axis=1)
    bonferroni = ALPHA / N_TESTS
    any_bonf = np.any(null_p < bonferroni, axis=1)
    print(f"  {N_TESTS} independent null tests per experiment, {N_REPS} experiments")
    print(f"  family-wise error rate, uncorrected  = {any_sig.mean() * 100:5.1f} %")
    print(f"  Bonferroni threshold = {ALPHA}/{N_TESTS} = {bonferroni:.5f}")
    print(f"  family-wise error rate, Bonferroni   = {any_bonf.mean() * 100:5.1f} %")
    print(f"  expected number of 'significant' results per experiment before checking: "
          f"{N_TESTS * ALPHA:.2f}")
    print("  -> with twenty tests, a single 'significant' result is the expected")
    print("     outcome under the null; report the search, not just the winner.")


if __name__ == "__main__":
    main()
