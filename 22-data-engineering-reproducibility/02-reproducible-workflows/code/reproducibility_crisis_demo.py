#!/usr/bin/env python3
"""Power, replication and multiplicity in computational science: SYNTHETIC numbers.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproducibility_crisis_demo.py

Everything here is SYNTHETIC.  Studies are simulated by the code below from a
chosen effect size, sample size and noise level.  No published replication rate,
no meta-analysis and no measured effect is quoted.

Sections
--------
1. Power of a two-sided test versus sample size and effect size.
2. Conditional replication rate measured by Monte Carlo.
3. Winner's curse: the effect size reported by the significant studies.
4. Multiplicity: false discovery proportion when many hypotheses are tested.
"""

import numpy as np
from statistics import NormalDist

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC study model (chosen, not measured) ---------------------------
ALPHA = 0.05          # two-sided test level
SIGMA = 1.0           # noise standard deviation, arbitrary data unit
Z = NormalDist().inv_cdf(1.0 - ALPHA / 2.0)
N_STUDIES = 20000     # simulated studies per row


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def power(effect, n, sigma=SIGMA):
    """Analytic power of a two-sided z-test."""
    return NormalDist().cdf(effect * np.sqrt(n) / sigma - Z)


def n_for_power(effect, target, sigma=SIGMA):
    """Sample size giving the target power for a given effect size."""
    z_beta = NormalDist().inv_cdf(target)
    return ((Z + z_beta) * sigma / effect) ** 2


def main():
    section("1. Power versus sample size and effect size")
    print(f"SYNTHETIC two-sided test: alpha = {ALPHA}, noise sigma = {SIGMA:.1f} "
          f"(data units)")
    print("  effect (sigma) | n = 10 | n = 30 | n = 100 | n = 300")
    for effect in (0.2, 0.5, 0.8, 1.0):
        row = " | ".join(f"{power(effect, n):7.3f}" for n in (10, 30, 100, 300))
        print(f"  {effect:>14.1f} | {row}")
    for effect in (0.5, 0.2):
        n80 = n_for_power(effect, 0.80)
        print(f"  n for 80 % power at effect {effect:.1f} sigma = {n80:.1f} "
              f"(rounded up: {int(np.ceil(n80))})")

    section("2. Conditional replication rate (Monte Carlo)")
    print(f"  {N_STUDIES} simulated studies per row; only the significant ones are")
    print("  replicated, at the same n and at double n, with the true effect")
    print("  n | effect | power | significant | rep. rate n | rep. rate 2n")
    for n, effect in ((30, 0.3), (30, 0.5), (30, 0.8), (10, 1.0)):
        p = power(effect, n)
        obs = effect + RNG.normal(0, SIGMA / np.sqrt(n), N_STUDIES)
        sig = np.abs(obs) > Z * SIGMA / np.sqrt(n)
        n_sig = int(sig.sum())
        rep1 = np.abs(RNG.normal(effect, SIGMA / np.sqrt(n), n_sig)) > \
            Z * SIGMA / np.sqrt(n)
        rep2 = np.abs(RNG.normal(effect, SIGMA / np.sqrt(2 * n), n_sig)) > \
            Z * SIGMA / np.sqrt(2 * n)
        print(f"  {n:>2d} | {effect:>6.1f} | {p:5.3f} | {n_sig:>11d} | "
              f"{rep1.mean():>11.3f} | {rep2.mean():>11.3f}")
    print("  -> the replication rate of a *significant* result equals the power,")
    print("     not 1.0, when the effect is exactly the same; doubling n raises it")
    print("     towards 1 but never guarantees it")
    spread = 0.5
    n, effect = 30, 0.5
    n_sig = int((np.abs(effect + RNG.normal(0, SIGMA / np.sqrt(n), N_STUDIES))
                 > Z * SIGMA / np.sqrt(n)).sum())
    true_rep = effect + RNG.normal(0, spread * effect, n_sig)
    rep_het = np.abs(RNG.normal(true_rep, SIGMA / np.sqrt(n), n_sig)) > \
        Z * SIGMA / np.sqrt(n)
    print(f"  heterogeneous effects (sd {spread:.1f} x effect) at the same power:")
    print(f"    replication rate = {rep_het.mean():.3f}, below the "
          f"{power(effect, n):.3f} of the identical-effect case")

    section("3. Winner's curse: reported effect of the significant studies")
    print("  effect | n  | mean |effect| of significant | reported/true")
    for effect, n in ((0.2, 100), (0.5, 30), (0.8, 30)):
        obs = effect + RNG.normal(0, SIGMA / np.sqrt(n), N_STUDIES)
        sig = np.abs(obs) > Z * SIGMA / np.sqrt(n)
        reported = float(np.abs(obs[sig]).mean())
        print(f"  {effect:>6.1f} | {n:>2d} | {reported:>26.3f} | "
              f"{reported / effect:>13.3f}")
    print("  -> selecting on significance inflates the reported effect; the")
    print("     inflation is worst exactly where the power is lowest")

    section("4. Multiplicity: false discovery proportion")
    n_tests = 20
    prior_true = 0.10
    for effect in (0.0, 0.5):
        n_sim = 4000
        true_flags = RNG.random((n_sim, n_tests)) < prior_true
        eff = np.where(true_flags, effect, 0.0)
        draws = eff + RNG.normal(0, 1.0, (n_sim, n_tests))
        sig = np.abs(draws) > Z
        n_sig = sig.sum(axis=1)
        n_false = (sig & ~true_flags).sum(axis=1)
        risky = n_sig > 0
        fdp = float((n_false[risky] / n_sig[risky]).mean())
        fwer = float((n_false > 0).mean())
        print(f"  true-effect size {effect:.1f}: {n_tests} tests, "
              f"{prior_true:.0%} hypotheses truly non-zero")
        print(f"    mean number of significant tests = {n_sig.mean():.2f}, "
              f"mean false discovery proportion = {fdp:.3f}")
        print(f"    probability of at least one false positive = {fwer:.3f}")
    print("  -> with no correction, a 20-test paper reports a mean FDP of this")
    print("     size whenever the tested effects are small relative to the noise")


if __name__ == "__main__":
    main()
