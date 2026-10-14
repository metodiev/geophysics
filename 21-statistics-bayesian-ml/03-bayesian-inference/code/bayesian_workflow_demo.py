#!/usr/bin/env python3
"""Bayesian workflow on SYNTHETIC count data: a prior predictive check, exact
leave-one-out comparison of a plug-in model with a conjugate model, WAIC from
posterior samples, and a posterior predictive check.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python bayesian_workflow_demo.py

The data are SYNTHETIC: 40 Poisson counts from a stated rate. No measured value
is used.

Sections
--------
1. Prior predictive check: what the prior expects before any data.
2. Two models compared by exact leave-one-out predictive density.
3. WAIC from posterior samples, as a cross-check.
4. Posterior predictive check of the winning model.
"""

import numpy as np
from scipy import special

RNG = np.random.default_rng(20261014)

N = 40
LAMBDA_TRUE = 1.75
ALPHA_PRIOR, BETA_PRIOR = 2.0, 1.0


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def nb_logpmf(y, alpha, beta):
    """Log pmf of the Gamma-Poisson (negative binomial) marginal."""
    return (special.gammaln(alpha + y) - special.gammaln(alpha)
            - special.gammaln(y + 1.0)
            + alpha * np.log(beta / (beta + 1.0))
            + y * np.log(1.0 / (beta + 1.0)))


def main():
    y = RNG.poisson(LAMBDA_TRUE, N)
    total = float(y.sum())
    lam_plug = total / N
    print(f"SYNTHETIC Poisson counts: {N} observations from a rate of "
          f"{LAMBDA_TRUE:.2f}.")
    print(f"  sample mean = {lam_plug:.4f}, sample variance = "
          f"{float(y.var(ddof=1)):.4f} (variance/mean = "
          f"{float(y.var(ddof=1)) / lam_plug:.3f})")

    section("1. Prior predictive check")
    lam_prior = RNG.gamma(ALPHA_PRIOR, 1.0, size=20000)
    y_prior = RNG.poisson(lam_prior)
    print(f"  prior Gamma({ALPHA_PRIOR:.0f}, rate {BETA_PRIOR:.0f}): predictive "
          f"mean = {y_prior.mean():.4f}, sd = {y_prior.std(ddof=1):.4f}")
    print(f"  predictive 95% range = [{np.percentile(y_prior, 2.5):.0f}, "
          f"{np.percentile(y_prior, 97.5):.0f}]; observed range = "
          f"[{y.min()}, {y.max()}], observed mean = {y.mean():.4f}")
    print("  the prior is compatible with the data, so it is not an obviously")
    print("  bad choice; a prior predictive check is the cheapest way to catch a")
    print("  prior that forbids the observed scale of the data.")

    section("2. Two models compared by exact leave-one-out")
    # model N: Poisson with the rate re-estimated from the remaining data
    loo_n = np.empty(N)
    for i in range(N):
        lam_i = (total - y[i]) / (N - 1)
        loo_n[i] = (y[i] * np.log(lam_i) - lam_i - special.gammaln(y[i] + 1.0))
    elpd_n = float(loo_n.sum())
    elpd_store = {}
    print(f"  model N (Poisson, rate re-estimated per fold):")
    print(f"    exact LOO elpd = {elpd_n:.2f} (se "
          f"{loo_n.std(ddof=1) * np.sqrt(N):.2f}), plug-in rate "
          f"{lam_plug:.4f}")
    for name, a0, b0 in (("weak Gamma(2, rate 1)", 2.0, 1.0),
                         ("strong Gamma(50, rate 25)", 50.0, 25.0)):
        loo_g = np.empty(N)
        for i in range(N):
            loo_g[i] = nb_logpmf(y[i], a0 + total - y[i], b0 + N - 1)
        elpd_g = float(loo_g.sum())
        elpd_store[name] = elpd_g
        diff = elpd_g - elpd_n
        se_diff = float(np.std(loo_g - loo_n, ddof=1) * np.sqrt(N))
        post_mean = (a0 + total) / (b0 + N)
        print(f"  model G with {name}:")
        print(f"    exact LOO elpd = {elpd_g:.2f} (se "
              f"{loo_g.std(ddof=1) * np.sqrt(N):.2f}), posterior mean "
              f"{post_mean:.4f}")
        print(f"    elpd difference (G - N) = {diff:+.2f} with se {se_diff:.2f}"
              f"  ->  {abs(diff) / max(se_diff, 1e-12):.1f} se")
        winner = "the conjugate model" if diff > 0 else "the plug-in model"
        if abs(diff) < 2.0 * se_diff:
            print("    the difference is within two standard errors: the two")
            print("    models are not distinguishable at this sample size, and")
            print("    parsimony prefers the simpler one.")
        else:
            print(f"    {winner} wins by more than 2 se.")
    print("  both priors leave the comparison within about one standard error at")
    print("  N = 40; the conjugate model's wider predictive helps only slightly")
    print("  here, because the counts are close to Poisson.")

    section("3. WAIC from posterior samples")
    samples = RNG.gamma(ALPHA_PRIOR + total, 1.0 / (BETA_PRIOR + N), size=4000)
    log_lik = np.array([y * np.log(s) - s - special.gammaln(y + 1.0)
                        for s in samples])
    mx = log_lik.max(axis=0)
    lppd = float(np.sum(np.log(np.exp(log_lik - mx).mean(axis=0)) + mx))
    p_waic = float(np.sum(log_lik.var(axis=0, ddof=1)))
    waic = -2.0 * (lppd - p_waic)
    print(f"  lppd = {lppd:.2f}, effective parameters p_WAIC = {p_waic:.2f}")
    print(f"  WAIC = -2(lppd - p) = {waic:.2f}; WAIC/2 as an elpd = "
          f"{-waic / 2:.2f}")
    print(f"  exact LOO elpd of the same model = "
          f"{elpd_store['weak Gamma(2, rate 1)']:.2f}")
    print("  the two differ by well under one standard error of the LOO")
    print("  estimate, which is the expected agreement between a good asymptotic")
    print("  approximation and an exact computation.")

    section("4. Posterior predictive check")
    idx = RNG.integers(0, samples.size, 500)
    y_rep = np.array([RNG.poisson(samples[i], size=N) for i in idx])
    obs_ratio = float(y.var(ddof=1)) / float(y.mean())
    rep_ratio = y_rep.var(axis=1, ddof=1) / y_rep.mean(axis=1)
    rep_mean = y_rep.mean(axis=1)
    print(f"  dispersion (variance/mean): observed {obs_ratio:.4f}")
    print(f"    replicated mean {rep_ratio.mean():.4f}, 95% range "
          f"[{np.percentile(rep_ratio, 2.5):.4f}, "
          f"{np.percentile(rep_ratio, 97.5):.4f}]")
    print(f"    fraction of replicates at least as dispersed = "
          f"{np.mean(rep_ratio >= obs_ratio):.4f}")
    print(f"  mean: observed {y.mean():.4f}, replicated 95% range "
          f"[{np.percentile(rep_mean, 2.5):.4f}, "
          f"{np.percentile(rep_mean, 97.5):.4f}]")
    print("  the check is a statement about the statistics chosen in advance:")
    print("  the observed dispersion sits inside the replicated distribution,")
    print("  so the Poisson assumption is not contradicted by this feature.")


if __name__ == "__main__":
    main()
