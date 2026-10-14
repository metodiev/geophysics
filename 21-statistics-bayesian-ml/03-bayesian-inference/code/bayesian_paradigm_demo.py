#!/usr/bin/env python3
"""The Bayesian paradigm on SYNTHETIC binomial data: prior, likelihood and
posterior on a grid, the effect of prior strength, sequential updating, and the
posterior predictive probability.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python bayesian_paradigm_demo.py

The data are SYNTHETIC: 14 successes in 30 trials drawn from a stated Bernoulli
process. No measured value is used.

Sections
--------
1. Three priors, one likelihood, three posteriors.
2. Sequential updating equals batch updating.
3. Prior strength and the prior-equivalent sample size.
"""

import numpy as np
from scipy import stats

RNG = np.random.default_rng(20261014)

N_TRIALS = 30
P_TRUE = 0.45
GRID = np.linspace(1e-6, 1.0 - 1e-6, 2001)
PRIORS = (
    ("uniform Beta(1,1)", 1.0, 1.0),
    ("weak Beta(2,2)", 2.0, 2.0),
    ("sceptical Beta(20,20)", 20.0, 20.0),
)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def posterior_grid(a, b, k, n):
    logp = stats.beta.logpdf(GRID, a, b) + k * np.log(GRID) + (n - k) * np.log1p(-GRID)
    p = np.exp(logp - logp.max())
    p /= np.trapezoid(p, GRID)
    return p


def summary(p):
    mean = float(np.trapezoid(GRID * p, GRID))
    cdf = np.cumsum(p) * (GRID[1] - GRID[0])
    lo = float(GRID[np.searchsorted(cdf, 0.025)])
    hi = float(GRID[np.searchsorted(cdf, 0.975)])
    mode = float(GRID[int(np.argmax(p))])
    return mean, lo, hi, mode


def main():
    draws = (RNG.random(N_TRIALS) < P_TRUE).astype(int)
    k = int(draws.sum())
    print(f"SYNTHETIC binomial data: {k} successes in {N_TRIALS} trials drawn "
          f"from a Bernoulli process with true probability {P_TRUE:.2f}.")
    print(f"  maximum-likelihood estimate k/n = {k / N_TRIALS:.4f}")

    section("1. Three priors, one likelihood, three posteriors")
    print("  prior                prior mean   post. mean   95% credible interval"
          "   MAP")
    for name, a, b in PRIORS:
        p = posterior_grid(a, b, k, N_TRIALS)
        mean, lo, hi, mode = summary(p)
        exact = (a + k) / (a + b + N_TRIALS)
        print(f"  {name:21s}  {a / (a + b):9.4f}   {mean:10.4f}   "
              f"[{lo:.4f}, {hi:.4f}]   {mode:.4f}")
        print(f"      exact conjugate posterior mean = {exact:.6f} "
              f"(grid agrees to {abs(mean - exact):.1e})")
    print("  the likelihood is identical in all three cases; only the prior")
    print("  changes, and the credible interval narrows as the prior strengthens.")

    section("2. Sequential updating equals batch updating")
    first, second = draws[:10], draws[10:]
    a, b = 2.0, 2.0
    a1, b1 = a + int(first.sum()), b + first.size - int(first.sum())
    a2, b2 = a1 + int(second.sum()), b1 + second.size - int(second.sum())
    print(f"  first batch:  {int(first.sum())} of {first.size}  -> "
          f"Beta({a1:.0f},{b1:.0f}), mean = {a1 / (a1 + b1):.6f}")
    print(f"  second batch: {int(second.sum())} of {second.size} -> "
          f"Beta({a2:.0f},{b2:.0f}), mean = {a2 / (a2 + b2):.6f}")
    print(f"  batch update: all {N_TRIALS} at once -> "
          f"Beta({a + k:.0f},{b + N_TRIALS - k:.0f}), mean = "
          f"{(a + k) / (a + b + N_TRIALS):.6f}")
    print("  the two paths agree exactly: the posterior is a sufficient summary,")
    print("  so the order in which evidence arrives does not matter.")

    section("3. Prior strength and the prior-equivalent sample size")
    print("  prior            prior-equivalent n   post. mean with k/n = "
          f"{k / N_TRIALS:.4f}")
    for name, a, b in PRIORS:
        equiv = a + b - 2.0
        print(f"  {name:21s}  {equiv:18.0f}   "
              f"{(a + k) / (a + b + N_TRIALS):12.4f}")
    predictive = (2.0 + k) / (2.0 + 2.0 + N_TRIALS)
    print(f"  posterior predictive P(next success | data) under Beta(2,2) = "
          f"{predictive:.6f}")
    print("  a Beta(a,b) prior acts like a-1 prior successes and b-1 prior")
    print("  failures, so its influence is fixed and the data eventually win.")


if __name__ == "__main__":
    main()
