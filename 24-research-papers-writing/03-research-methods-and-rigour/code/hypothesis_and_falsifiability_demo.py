#!/usr/bin/env python3
"""Hypotheses, falsifiability and testing: what flexibility does to error rates.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hypothesis_and_falsifiability_demo.py

Everything here is SYNTHETIC.  Experiments are simulated from the normal model;
no data set is analysed and no published result is reproduced.

Sections
--------
1. Calibration: the null and the false-positive rate.
2. Power as a function of effect size at fixed n.
3. Flexibility: researcher degrees of freedom under the null.
4. Multiplicity across many tests, with and without a correction.
"""

from math import erfc, sqrt

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC experiment parameters (chosen teaching values) ---------------
N_REPS = 4000
ALPHA = 0.05
N_PER_GROUP = 32
EFFECT_SIZES = (0.0, 0.2, 0.5, 0.8, 1.2)
FLEXIBILITY = (1, 4, 16, 64)
N_TESTS = 20


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def pvalues(n, effect, reps, rng):
    x = rng.normal(0.0, 1.0, (reps, n))
    y = rng.normal(effect, 1.0, (reps, n))
    diff = y.mean(axis=1) - x.mean(axis=1)
    se = np.sqrt(2.0 / n)
    t = diff / se
    return np.array([erfc(abs(ti) / sqrt(2.0)) for ti in t])


def main():
    section("1. Calibration: the null and the false-positive rate")
    p_null = pvalues(N_PER_GROUP, 0.0, N_REPS, RNG)
    rate = float(np.mean(p_null < ALPHA))
    se = float(np.sqrt(ALPHA * (1 - ALPHA) / N_REPS))
    print(f"SYNTHETIC: {N_REPS} null experiments, n = {N_PER_GROUP} per group, "
          f"alpha = {ALPHA}")
    print(f"  false positives = {rate * 100:.2f} % +/- {se * 100:.2f} (1 s.e.)")
    print(f"  of {N_REPS} null p-values, "
          f"{int(np.sum(p_null < 0.01))} are below 0.01 "
          f"({np.mean(p_null < 0.01) * 100:.2f} %, nominal 1 %)")
    print(f"  median null p-value = {np.median(p_null):.3f} (nominal 0.5)")
    print("  -> a single test is calibrated; the interesting failures come from")
    print("     everything that happens around it.")

    section("2. Power as a function of effect size at fixed n")
    print(f"  n = {N_PER_GROUP} per group; a two-sided test at alpha = {ALPHA}")
    for effect in EFFECT_SIZES:
        p = pvalues(N_PER_GROUP, effect, N_REPS, RNG)
        print(f"  true effect d = {effect:4.2f}: power = {np.mean(p < ALPHA) * 100:5.1f} %, "
              f"median p = {np.median(p):.4f}, "
              f"fraction with p < 0.001 = {np.mean(p < 0.001) * 100:5.2f} %")
    print("  -> at this sample size a d = 0.2 effect is almost never detected, and a")
    print("     d = 0.8 effect almost always is: the sample size chooses the question.")

    section("3. Flexibility: researcher degrees of freedom under the null")
    print(f"  {N_REPS} null experiments, each analysed with k defensible choices,")
    print("  each choice giving an independent chance to cross the threshold")
    print("   k   measured P(at least one p < 0.05)   independence prediction")
    for k in FLEXIBILITY:
        p = RNG.random((N_REPS, k))
        any_sig = np.any(p < ALPHA, axis=1)
        prediction = 1.0 - (1.0 - ALPHA) ** k
        print(f"  {k:3d}   {any_sig.mean() * 100:25.1f} %   {prediction * 100:20.1f} %")
    print("  -> with 64 defensible choices, a genuinely null result is reported as")
    print("     significant in most experiments.  This is flexibility, not fraud:")
    print("     each choice is defensible when made alone.")
    print("  -> falsifiability is the constraint that removes the choices in advance.")

    section("4. Multiplicity across many tests, with and without a correction")
    null_p = RNG.random((N_REPS, N_TESTS))
    print(f"  {N_TESTS} independent null tests per experiment, {N_REPS} experiments")
    print(f"  family-wise error rate, uncorrected = "
          f"{np.mean(np.any(null_p < ALPHA, axis=1)) * 100:5.1f} %  "
          f"(exact {100 * (1 - (1 - ALPHA) ** N_TESTS):.1f} %)")
    print(f"  Bonferroni threshold = {ALPHA}/{N_TESTS} = {ALPHA / N_TESTS:.5f}")
    print(f"  family-wise error rate, Bonferroni  = "
          f"{np.mean(np.any(null_p < ALPHA / N_TESTS, axis=1)) * 100:5.1f} %  "
          f"(exact {100 * (1 - (1 - ALPHA / N_TESTS) ** N_TESTS):.1f} %)")
    print(f"  expected number of significant results before correction = "
          f"{N_TESTS * ALPHA:.2f} per experiment")
    print("  -> report the search, the threshold and the correction together; any one")
    print("     of them alone leaves the reader unable to judge the result.")


if __name__ == "__main__":
    main()
