#!/usr/bin/env python3
"""Conjugate priors on SYNTHETIC data: Beta-Binomial, Normal-Normal and
Gamma-Poisson posteriors in closed form, checked against numerical posteriors,
and the precision-weighted shrinkage each implies.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python conjugate_priors_demo.py

All data are SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. Beta-Binomial: the posterior as an exponential-family update.
2. Normal-Normal with known variance: precision and shrinkage.
3. Gamma-Poisson: rate estimation.
"""

import numpy as np
from scipy import stats

RNG = np.random.default_rng(20261014)

N_TRIALS, P_TRUE = 30, 0.45
N_NORMAL, MU_TRUE, SIGMA = 10, 0.8, 1.0     # data sd is KNOWN
N_POISSON, LAMBDA_TRUE = 10, 1.5


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    print("SYNTHETIC data for three conjugate families; every posterior below")
    print("has a closed form and is checked against a numerical integration.")

    section("1. Beta-Binomial")
    k = int((RNG.random(N_TRIALS) < P_TRUE).sum())
    a0, b0 = 2.0, 2.0
    a1, b1 = a0 + k, b0 + N_TRIALS - k
    print(f"  data: {k} successes in {N_TRIALS} trials; prior Beta({a0:.0f},{b0:.0f})")
    print(f"  posterior Beta({a1:.0f},{b1:.0f})")
    print(f"  posterior mean  = a/(a+b)     = {a1 / (a1 + b1):.6f}")
    print(f"  posterior mode  = (a-1)/(a+b-2) = {(a1 - 1) / (a1 + b1 - 2):.6f}")
    print(f"  posterior var   = ab/((a+b)^2(a+b+1)) = "
          f"{a1 * b1 / ((a1 + b1) ** 2 * (a1 + b1 + 1)):.6f}")
    lo, hi = stats.beta.ppf([0.025, 0.975], a1, b1)
    print(f"  95% credible interval = [{lo:.4f}, {hi:.4f}]")
    grid = np.linspace(1e-6, 1 - 1e-6, 2001)
    lp = stats.beta.logpdf(grid, a1, b1)
    print(f"  check: numerical mode on the grid = "
          f"{grid[int(np.argmax(lp))]:.6f}")

    section("2. Normal-Normal with known variance")
    x = MU_TRUE + SIGMA * RNG.standard_normal(N_NORMAL)
    xbar = float(x.mean())
    mu0, tau = 0.0, 1.0
    post_var = 1.0 / (1.0 / tau ** 2 + N_NORMAL / SIGMA ** 2)
    weight = (N_NORMAL / SIGMA ** 2) / (1.0 / tau ** 2 + N_NORMAL / SIGMA ** 2)
    post_mean = weight * xbar + (1 - weight) * mu0
    print(f"  data: n = {N_NORMAL}, sample mean = {xbar:.5f}, known sd = "
          f"{SIGMA:.2f}")
    print(f"  prior N({mu0:.1f}, {tau ** 2:.1f}); posterior N({post_mean:.5f}, "
          f"{post_var:.6f})")
    print(f"  data weight = (n/sigma^2)/(1/tau^2 + n/sigma^2) = {weight:.6f}")
    print(f"  posterior sd = {np.sqrt(post_var):.6f} against the prior sd "
          f"{tau:.2f} and the data se {SIGMA / np.sqrt(N_NORMAL):.4f}")
    print(f"  shrinkage of the sample mean towards the prior: "
          f"{post_mean - xbar:+.5f}")

    section("3. Gamma-Poisson")
    counts = RNG.poisson(LAMBDA_TRUE, N_POISSON)
    total = int(counts.sum())
    alpha0, beta0 = 2.0, 1.0
    alpha1, beta1 = alpha0 + total, beta0 + N_POISSON
    print(f"  data: {total} events in {N_POISSON} intervals; prior "
          f"Gamma({alpha0:.0f}, rate {beta0:.0f})")
    print(f"  posterior Gamma({alpha1:.0f}, rate {beta1:.0f})")
    print(f"  posterior mean = {alpha1 / beta1:.6f} (MLE {total / N_POISSON:.4f})")
    print(f"  posterior sd   = sqrt(a)/b = {np.sqrt(alpha1) / beta1:.6f}")
    lo, hi = stats.gamma.ppf([0.025, 0.975], alpha1, scale=1.0 / beta1)
    print(f"  95% credible interval = [{lo:.4f}, {hi:.4f}]")
    print("  the prior adds 2 events' worth of rate information; with 20 events")
    print("  the posterior is dominated by the data but not identical to the MLE.")


if __name__ == "__main__":
    main()
