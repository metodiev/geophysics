#!/usr/bin/env python3
"""Designing observational and experimental studies: power, confounding, attenuation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python study_design_demo.py

Everything here is SYNTHETIC.  Effects are simulated from the normal model with
chosen parameters; no data set is analysed.

Sections
--------
1. The power curve: what sample size buys.
2. Confounding: a spurious association and what adjustment does to it.
3. Measurement error: attenuation of a slope by unreliable measurements.
4. Design consequences: the three numbers a design must fix in advance.
"""

from math import erfc, sqrt

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC design parameters (chosen teaching values) -------------------
SAMPLE_SIZES = (8, 12, 16, 24, 32, 48, 64, 96, 128, 192)
TRUE_EFFECT = 0.50          # within-group sd units
N_REPS = 2000
ALPHA = 0.05
CONFOUNDER_LOAD = 0.60      # correlation of the confounder with x and with y
RELIABILITIES = (1.0, 0.8, 0.6, 0.4)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def two_sample_power(n, effect, reps, rng):
    x = rng.normal(0.0, 1.0, (reps, n))
    y = rng.normal(effect, 1.0, (reps, n))
    diff = y.mean(axis=1) - x.mean(axis=1)
    t = diff / np.sqrt(2.0 / n)
    p = np.array([erfc(abs(ti) / sqrt(2.0)) for ti in t])
    return float(np.mean(p < ALPHA))


def main():
    section("1. The power curve: what sample size buys")
    print(f"SYNTHETIC: two-group comparison, true effect d = {TRUE_EFFECT:.2f}, "
          f"{N_REPS} replications per point")
    print("  n per group   power      simulated cost index (n^2)")
    smallest = None
    for n in SAMPLE_SIZES:
        power = two_sample_power(n, TRUE_EFFECT, N_REPS, RNG)
        if smallest is None and power >= 0.80:
            smallest = n
        print(f"  {n:11d}   {power * 100:5.1f} %   {n * n:8d}")
    print(f"  smallest n in the grid reaching 80 % power = {smallest}")
    theoretical = 2.0 * (1.96 + 0.842) ** 2 / TRUE_EFFECT ** 2
    print(f"  analytic n for 80 % power = 2(z_a/2 + z_b)^2 / d^2 = "
          f"{theoretical:.1f} per group")
    print("  -> power is bought quadratically: halving the effect size needs four")
    print("     times the sample.")

    section("2. Confounding: a spurious association and what adjustment does to it")
    n = 200
    z = RNG.normal(0.0, 1.0, (N_REPS, n))                  # the confounder
    x = CONFOUNDER_LOAD * z + np.sqrt(1 - CONFOUNDER_LOAD ** 2) * RNG.normal(0, 1, (N_REPS, n))
    y = CONFOUNDER_LOAD * z + np.sqrt(1 - CONFOUNDER_LOAD ** 2) * RNG.normal(0, 1, (N_REPS, n))
    b_unadj = np.array([np.polyfit(xi, yi, 1)[0] for xi, yi in zip(x, y)])
    b_adj = []
    for xi, yi, zi in zip(x, y, z):
        X = np.column_stack([xi, zi])
        b_adj.append(np.linalg.lstsq(X, yi, rcond=None)[0][0])
    b_adj = np.array(b_adj)
    print(f"  true direct effect of x on y: 0.000; confounder loading: "
          f"{CONFOUNDER_LOAD:.2f} on both")
    print(f"  unadjusted slope = {b_unadj.mean():+.4f} "
          f"+/- {b_unadj.std(ddof=1):.4f} (1 s.d. across replications)")
    print(f"  adjusted  slope = {b_adj.mean():+.4f} +/- {b_adj.std(ddof=1):.4f}")
    print(f"  fraction of replications declaring the unadjusted slope significant = "
          f"{np.mean(np.abs(b_unadj) / (b_unadj.std(ddof=1)) > 1.96) * 100:.1f} %")
    print("  -> an unmeasured common cause produces a replicable, significant,")
    print("     entirely spurious association; adjustment removes it here only")
    print("     because the confounder was measured.")

    section("3. Measurement error: attenuation of a slope by unreliability")
    n = 120
    x_true = RNG.normal(0.0, 1.0, (N_REPS, n))
    y = 1.0 * x_true + RNG.normal(0.0, 0.6, (N_REPS, n))   # true slope = 1.00
    print("  true slope = 1.000; x observed with additive noise")
    print("  reliability   measured slope   attenuation ratio")
    for rel in RELIABILITIES:
        noise_sd = np.sqrt((1.0 - rel) / rel)
        x_obs = x_true + noise_sd * RNG.normal(0.0, 1.0, (N_REPS, n))
        slopes = np.array([np.polyfit(xo, yi, 1)[0] for xo, yi in zip(x_obs, y)])
        print(f"  {rel:9.1f}   {slopes.mean():12.4f}   {slopes.mean() / 1.0:16.3f}")
    print("  -> attenuation is multiplicative and predictable: at reliability 0.6 the")
    print("     slope is about 60 % of the true value, however large n becomes.")

    section("4. Design consequences: the three numbers a design must fix in advance")
    print(f"  effect size to be detected (d)      : {TRUE_EFFECT:.2f}")
    print(f"  significance level (alpha)          : {ALPHA}")
    print(f"  required power (1 - beta)           : 0.80")
    print(f"  implied n per group                 : "
          f"{2.0 * (1.96 + 0.842) ** 2 / TRUE_EFFECT ** 2:.0f}")
    print(f"  if d is really 0.25 instead of 0.50, the same n gives power "
          f"{two_sample_power(52, 0.25, N_REPS, RNG) * 100:.1f} %")
    print("  -> a design is a commitment to three numbers; if a reviewer cannot find")
    print("     them in the proposal, the study is not yet designed.")


if __name__ == "__main__":
    main()
