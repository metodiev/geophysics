#!/usr/bin/env python3
"""Posterior summaries: marginals, credible intervals, correlations, propagation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python posterior_summary_demo.py

All models and data in this demo are SYNTHETIC.  The skewed posterior, the
prior used in the coverage study and the nonlinear function are chosen teaching
values, not measurements.

Contents
--------
1. A skewed 1-D posterior: mean, median, mode, equal-tailed vs HPD intervals.
2. Credible interval versus confidence interval: measured coverage.
3. Marginal versus conditional uncertainty in two dimensions.
4. Propagating the posterior through a nonlinear function (Jensen gap).
5. Correlation and the area of the credible region.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

SIGMA = 1.0        # known measurement standard deviation
MU_TRUE = 1.0      # synthetic true mean


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. A skewed 1-D posterior: summaries that disagree")
    # SYNTHETIC scale problem x_i ~ N(0, sigma^2), n = 4, with the Jeffreys
    # prior p(sigma) ~ 1/sigma.  The posterior is inverse-gamma and skewed.
    n = 4
    x = np.array([0.60, 1.10, 1.50, 0.80])
    ss = float(np.sum(x ** 2))
    alpha, beta = n / 2.0, ss / 2.0
    sig = np.linspace(1e-4, 4.0, 400001)
    dsig = sig[1] - sig[0]
    logp = -alpha * np.log(sig ** 2) - beta / sig ** 2 - np.log(sig)
    p = np.exp(logp - logp.max())
    p /= p.sum() * dsig
    cdf = np.cumsum(p) * dsig
    mean = float((p * sig).sum() * dsig)
    median = float(sig[np.searchsorted(cdf, 0.5)])
    mode = float(sig[np.argmax(p)])
    lo_eq = float(sig[np.searchsorted(cdf, 0.025)])
    hi_eq = float(sig[np.searchsorted(cdf, 0.975)])
    # HPD: the shortest interval holding 95% of the mass (two-pointer scan).
    target = 0.95
    j = 0
    best_w, i0, j0 = np.inf, 0, 0
    for i in range(sig.size):
        while j < sig.size - 1 and cdf[j] - cdf[i] < target:
            j += 1
        if cdf[j] - cdf[i] < target:
            break
        w = sig[j] - sig[i]
        if w < best_w:
            best_w, i0, j0 = w, i, j
    lo_hp, hi_hp = float(sig[i0]), float(sig[j0])
    print(f"SYNTHETIC n = {n} data, sum of squares = {ss:.4f}")
    print(f"inverse-gamma posterior: shape alpha = {alpha:.1f}, "
          f"rate beta = {beta:.4f}")
    print(f"  posterior mean   = {mean:.4f}")
    print(f"  posterior median = {median:.4f}")
    print(f"  posterior mode   = {mode:.4f}   (mean - mode = {mean - mode:+.4f})")
    print(f"  95% equal-tailed = [{lo_eq:.4f}, {hi_eq:.4f}]  "
          f"width {hi_eq - lo_eq:.4f}")
    print(f"  95% HPD          = [{lo_hp:.4f}, {hi_hp:.4f}]  "
          f"width {hi_hp - lo_hp:.4f}")
    def tails(lo, hi):
        clo = float(cdf[np.searchsorted(sig, lo)])
        chi = float(cdf[np.searchsorted(sig, hi)])
        return clo, 1.0 - chi

    eq_lo_m, eq_hi_m = tails(lo_eq, hi_eq)
    hp_lo_m, hp_hi_m = tails(lo_hp, hi_hp)
    print(f"  the HPD interval is {(hi_eq - lo_eq) / (hi_hp - lo_hp):.3f}x shorter")
    print(f"  tail masses, equal-tailed: left {eq_lo_m:.3f}, right {eq_hi_m:.3f}")
    print(f"  tail masses, HPD        : left {hp_lo_m:.3f}, right {hp_hi_m:.3f}")
    print("The equal-tailed interval holds 2.5% in each tail whatever the shape.")
    print("The HPD is the shortest interval carrying 95%, so it puts more mass in")
    print("the tail where the density is thinner (here the right tail). Both are")
    print("legitimate and they are different objects. When the posterior is skewed")
    print("the mean, median, mode and the two intervals all differ: a summary that")
    print("reports one of them under a symmetric +/- convention has hidden the")
    print("shape.")

    section("2. Credible interval is not a confidence interval: measured coverage")
    print("model: y_i = mu + e_i, six data, sigma = 1 known; 4000 synthetic trials")
    N = 6
    sd_bar = SIGMA / np.sqrt(N)
    trials = 4000
    z = 1.959963984540054   # exact standard-normal 97.5% quantile
    for label, m0, s0 in (("weak prior   (m0 = 1.0, s0 = 20)", 1.0, 20.0),
                          ("informative  (m0 = 1.0, s0 = 0.5)", 1.0, 0.5),
                          ("conflicting  (m0 = 3.0, s0 = 0.5)", 3.0, 0.5)):
        inside_bayes = 0
        inside_freq = 0
        for _ in range(trials):
            ybar = MU_TRUE + sd_bar * RNG.standard_normal()
            post_var = 1.0 / (1.0 / s0 ** 2 + 1.0 / sd_bar ** 2)
            post_mean = post_var * (m0 / s0 ** 2 + ybar / sd_bar ** 2)
            s = np.sqrt(post_var)
            inside_bayes += abs(MU_TRUE - post_mean) <= z * s
            inside_freq += abs(MU_TRUE - ybar) <= z * sd_bar
        print(f"  {label}: Bayesian coverage {inside_bayes / trials:.3f}, "
              f"frequentist coverage {inside_freq / trials:.3f}")
    print("With a weak prior the two coincide, and both are 0.95. With an")
    print("informative prior that disagrees with the truth, the Bayesian interval")
    print("under-covers: it does not have the repeated-sampling property, because")
    print("it was never designed to have it. '95% credible' and '95% confidence'")
    print("are different claims about different things.")

    section("3. Marginal versus conditional uncertainty")
    rho = 0.9
    C = np.array([[1.0, rho], [rho, 1.0]])
    marg = float(np.sqrt(C[0, 0]))
    cond = float(np.sqrt(C[0, 0] - C[0, 1] ** 2 / C[1, 1]))
    print(f"posterior correlation rho = {rho:.2f}")
    print(f"  marginal std of m1                = {marg:.4f}")
    print(f"  conditional std of m1 given m2     = {cond:.4f}")
    print(f"  ratio (marginal/conditional)       = {marg / cond:.4f}")
    print(f"  sqrt(1 - rho^2)                    = {np.sqrt(1 - rho ** 2):.4f}")
    print("Reporting the marginal alone overstates the uncertainty about m1 once m2")
    print("is known, and vice versa. Marginalising is the right default for")
    print("reporting, but a joint interpretation must use the conditional width.")

    section("4. Propagating the posterior through a nonlinear function")
    # SYNTHETIC: m ~ N(0, 1) posterior on a log-amplitude, g(m) = exp(m).
    m = RNG.standard_normal(400000)
    g = np.exp(m)
    gm = np.exp(0.0)
    print("posterior m ~ N(0,1); quantity of interest g(m) = exp(m) (a factor)")
    print(f"  E[g(m)]            = {g.mean():.4f}")
    print(f"  g(E[m])            = {gm:.4f}")
    print(f"  Jensen gap         = {g.mean() - gm:+.4f} "
          f"({100 * (g.mean() / gm - 1):+.2f}%)")
    lo, hi = np.quantile(g, [0.025, 0.975])
    print(f"  95% interval of g  = [{lo:.4f}, {hi:.4f}]")
    print(f"  g at the 95% interval endpoints of m = "
          f"[{np.exp(np.quantile(m, 0.025)):.4f}, "
          f"{np.exp(np.quantile(m, 0.975)):.4f}]")
    print(f"  median of g(m)     = {np.median(g):.4f}  (= g(median of m) = "
          f"{np.exp(np.median(m)):.4f})")
    print(f"  E[g] exceeds the median by {(g.mean() - np.median(g)):.4f}, and the")
    print(f"  posterior mean of m is {m.mean():+.4f}: the mean of g is NOT g of the")
    print("  mean, and it is not the centre of g's distribution.")
    print("The map is monotone, so transforming the endpoints of an interval is")
    print("exact and the median transforms exactly. The mean does not: a nonlinear")
    print("function of an uncertain input has a mean that is not the function of")
    print("the input mean. Quote intervals and medians, or propagate by sampling.")

    section("5. Correlation and the area of the credible region")
    chi2_95 = 5.991464547107979   # exact 95% chi-square quantile with 2 dof
    box = (2 * 1.959963984540054 * 1.0) ** 2   # product of marginal interval widths
    ref = chi2_95 * np.pi * 1.0                # area at rho = 0
    print("All region areas are for a Gaussian posterior with unit marginal stds.")
    print(f"product of the two marginal 95% interval widths (the box) = {box:.4f}")
    print("  rho   95% region area   relative to rho = 0   box/region")
    print("  " + "-" * 62)
    for r in (0.0, 0.5, 0.9, 0.99):
        env = np.array([[1.0, r], [r, 1.0]])
        lam = np.linalg.eigvalsh(env)
        area = chi2_95 * np.pi * np.sqrt(lam[0] * lam[1])
        print(f"  {r:5.2f}   {area:15.4f}   {area / ref:18.4f}   {box / area:10.4f}")
    print("The area of the joint credible region falls as the correlation rises,")
    print("because the parameters are confined to a ridge. The product of the two")
    print("marginal intervals is constant: it is the area of an axis-aligned box")
    print("that the posterior does not fill. At rho = 0 the box is a little SMALLER")
    print("than the 95% ellipse, because a 95% ellipse reaches 2.45 standard")
    print("deviations along its axes while an equal-tailed 1-D interval stops at")
    print("1.96; the ratio that carries the message is its growth to 5.79 at")
    print("rho = 0.99. Quoting a one-dimensional interval for each parameter")
    print("overstates the admitted volume of model space once the parameters are")
    print("correlated.")


if __name__ == "__main__":
    main()
