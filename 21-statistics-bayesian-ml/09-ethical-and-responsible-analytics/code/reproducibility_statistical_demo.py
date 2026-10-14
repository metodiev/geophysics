#!/usr/bin/env python3
"""Reproducibility: multiplicity, correction procedures and optional stopping.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproducibility_statistical_demo.py

Everything here is SYNTHETIC.  The test statistics are drawn from chosen
distributions; no study, data set or published p-value is used.

Sections
--------
1. Twenty tests per experiment, and the family-wise error rate.
2. Bonferroni and Benjamini-Hochberg corrections, with and without true effects.
3. Optional stopping: what "stop when significant" does to the error rate.
4. What the published effect looks like after the selection.
"""

import numpy as np
from scipy.stats import norm

RNG = np.random.default_rng(20261014)

M_TESTS = 20            # hypotheses tested per experiment
N_EXPERIMENTS = 4000    # Monte Carlo replications
ALPHA = 0.05            # nominal level
N_TRUE = 5              # true alternatives among the 20
TRUE_Z = 2.5            # mean z of a true alternative
MAX_N = 100             # maximum sample size in the sequential experiment
LOOKS = (20, 40, 60, 80, 100)
N_SEQ = 4000


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def p_values(n_null, n_true, true_z, rng):
    """Two-sided p-values for n_null nulls and n_true alternatives."""
    z = np.concatenate([rng.standard_normal(n_null),
                        true_z + rng.standard_normal(n_true)])
    return 2.0 * (1.0 - norm.cdf(np.abs(z))), np.concatenate(
        [np.zeros(n_null, dtype=bool), np.ones(n_true, dtype=bool)])


def bh_reject(p, q):
    """Benjamini-Hochberg rejection set."""
    order = np.argsort(p)
    m = p.size
    thresholds = q * (np.arange(1, m + 1)) / m
    ordered = p[order]
    below = ordered <= thresholds
    k = np.max(np.nonzero(below)[0]) + 1 if below.any() else 0
    rejected = np.zeros(m, dtype=bool)
    rejected[order[:k]] = True
    return rejected


def main():
    section("1. Twenty tests per experiment, and the family-wise error rate")
    fwer_raw = 0
    fwer_bonf = 0
    fwer_bh = 0
    for _ in range(N_EXPERIMENTS):
        p, _ = p_values(M_TESTS, 0, 0.0, RNG)
        if np.any(p <= ALPHA):
            fwer_raw += 1
        if np.any(p <= ALPHA / M_TESTS):
            fwer_bonf += 1
        if bh_reject(p, ALPHA).any():
            fwer_bh += 1
    analytic = 1.0 - (1.0 - ALPHA) ** M_TESTS
    print(f"SYNTHETIC: {M_TESTS} independent true null hypotheses per "
          f"experiment, {N_EXPERIMENTS} experiments, alpha = {ALPHA:.2f}")
    print(f"  analytic family-wise error rate for m = {M_TESTS}: "
          f"1 - (1 - alpha)^m = {analytic:.4f}")
    print(f"  measured rate, NO correction            = "
          f"{fwer_raw / N_EXPERIMENTS:.4f}")
    print(f"  measured rate, Bonferroni (alpha/m)     = "
          f"{fwer_bonf / N_EXPERIMENTS:.4f}")
    print(f"  measured rate, Benjamini-Hochberg (q)   = "
          f"{fwer_bh / N_EXPERIMENTS:.4f}")
    print(f"  the analytic and measured uncorrected rates agree: the arithmetic "
          f"of")
    print(f"  multiplicity is a property of the number of tests, not of the "
          f"science")
    print(f"  a rate of {fwer_raw / N_EXPERIMENTS:.2f} means that an analyst who "
          f"tests 20")
    print("  hypotheses and reports the one that reached 0.05 is wrong about "
          "two")
    print("  thirds of the time, and nothing in the reported result says so")

    section("2. Bonferroni and Benjamini-Hochberg, now with true effects")
    n_reps = 400
    results = {"bonferroni": [0, 0, 0], "bh": [0, 0, 0]}
    for _ in range(n_reps):
        p, is_true = p_values(M_TESTS - N_TRUE, N_TRUE, TRUE_Z, RNG)
        for name, rejected in (("bonferroni",
                                p <= ALPHA / M_TESTS),
                               ("bh", bh_reject(p, ALPHA))):
            false_pos = int(np.sum(rejected & ~is_true))
            true_pos = int(np.sum(rejected & is_true))
            results[name][0] += false_pos
            results[name][1] += true_pos
            results[name][2] += int(np.sum(rejected))
    print(f"  {N_TRUE} of {M_TESTS} hypotheses are true alternatives with "
          f"mean z = {TRUE_Z:.1f}")
    print(f"  {'procedure':<14s} {'power':>7s} {'false disc.':>12s} "
          f"{'FDR':>7s} {'mean rejects':>13s}")
    for name in ("bonferroni", "bh"):
        fp, tp, total = results[name]
        power = tp / (N_TRUE * n_reps)
        fdr = fp / max(total, 1)
        print(f"  {name:<14s} {power:>7.3f} {fp / n_reps:>12.2f} "
              f"{fdr:>7.3f} {total / n_reps:>13.2f}")
    print("  Bonferroni controls the family-wise rate but is conservative: its "
          "power")
    print("  is lower and it finds fewer effects.  Benjamini-Hochberg controls "
          "the")
    print("  false discovery RATE (the expected share of wrong findings among "
          "the")
    print("  findings), which is usually the quantity a field actually needs")
    print("  whichever is chosen, it must be stated before the tests are run")

    section("3. Optional stopping")
    stopped_significant = 0
    effects = []
    for _ in range(N_SEQ):
        x = RNG.standard_normal(MAX_N)
        for n in LOOKS:
            z = x[:n].mean() * np.sqrt(n)          # sigma = 1, one-sample
            if 2.0 * (1.0 - norm.cdf(abs(z))) < ALPHA:
                stopped_significant += 1
                effects.append(abs(x[:n].mean()))
                break
    print(f"SYNTHETIC: {N_SEQ} null experiments, up to {len(LOOKS)} interim "
          f"looks at n = {LOOKS}")
    print(f"  nominal level {ALPHA:.2f}, no correction")
    print(f"  measured rate of a significant result with optional stopping = "
          f"{stopped_significant / N_SEQ:.4f}")
    print(f"  the inflation factor over the nominal level = "
          f"{stopped_significant / N_SEQ / ALPHA:.2f}")
    print(f"  mean reported effect among the significant results = "
          f"{np.mean(effects):.4f} in sigma units")
    print(f"  the truth is exactly 0: every reported effect is a selection "
          f"artefact,")
    print("  and the ones that survive the early looks are the ones that "
          "happened")
    print("  to wander far -- which is also why they do not replicate")
    print("  a pre-registered sample size, or a sequential design with a stated")
    print("  spending function, is the only way to interpret an interim look")

    section("4. What the published effect looks like after the selection")
    print(f"  the same null experiment, three reporting rules:")
    print(f"    (a) test one pre-specified hypothesis            -> level "
          f"{ALPHA:.2f}")
    print(f"    (b) test {M_TESTS} and report the smallest p-value        -> level "
          f"{fwer_raw / N_EXPERIMENTS:.2f}")
    print(f"    (c) test {M_TESTS} and stop when one is significant   -> level "
          f"{stopped_significant / N_SEQ:.2f}")
    print("  none of the three is a better analysis than the others; they are")
    print("  three different experiments with three different error rates, and")
    print("  the reported p-value alone cannot distinguish them.  That is why")
    print("  the pre-specification, the number of tests and the stopping rule")
    print("  belong in the methods section next to the result")
    print("\nSYNTHETIC: the statistics are drawn from known distributions, so the")
    print("error rates are measured rather than asserted.  On real data the same")
    print("three rules produce the same three error rates, unobserved.")


if __name__ == "__main__":
    main()
