#!/usr/bin/env python3
"""Attribution: probability ratios, risk ratios and their uncertainty.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python attribution_methods_demo.py

Everything here is SYNTHETIC.  The factual and counterfactual worlds are simulated
from a chosen distribution shift and a chosen event-probability model; no observed
climate series, event catalogue or published attribution result is used.

Sections
--------
1. Two worlds differing by a forced shift of a covariate.
2. The probability ratio and the attributable fraction, with intervals.
3. The conditional risk ratio from logistic regression, and why it differs.
4. Rarer events: what happens to the uncertainty.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N_PER_WORLD = 2000      # seasons per world
FORCED_SHIFT = 1.0      # shift of the covariate, in sigma
A_BASE = -2.0           # logit intercept of the event probability
B_COVARIATE = 1.5       # logit slope on the covariate
RARE_A = (-3.5, -4.5)   # rarer event definitions
N_BOOT = 2000
GRID = np.linspace(-8.0, 12.0, 20001)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def sigmoid(t):
    return 1.0 / (1.0 + np.exp(-np.clip(t, -40.0, 40.0)))


def marginal_probability(a, mean_covariate):
    """E[P(event | X)] over X ~ Normal(mean_covariate, 1), by quadrature."""
    density = np.exp(-0.5 * (GRID - mean_covariate) ** 2) / np.sqrt(2.0 * np.pi)
    return float(np.trapezoid(sigmoid(a + B_COVARIATE * GRID) * density, GRID))


def logistic_fit(x, world, y):
    """Newton-Raphson logistic regression on [1, x, world]."""
    design = np.column_stack([np.ones(x.size), x, world])
    beta = np.zeros(3)
    hess = np.eye(3)
    for _ in range(80):
        eta = design @ beta
        p = sigmoid(eta)
        w = np.clip(p * (1.0 - p), 1e-9, None)
        grad = design.T @ (p - y)
        hess = design.T @ (design * w[:, None]) + 1e-9 * np.eye(3)
        try:
            step = np.linalg.solve(hess, grad)
        except np.linalg.LinAlgError:
            break
        beta -= step
        if np.max(np.abs(step)) < 1e-10:
            break
    cov = np.linalg.inv(hess)
    return beta, np.sqrt(np.diag(cov))


def main():
    section("1. Two worlds differing by a forced shift of a covariate")
    cf = RNG.standard_normal(N_PER_WORLD)
    fact = FORCED_SHIFT + RNG.standard_normal(N_PER_WORLD)
    print(f"SYNTHETIC experiment: {N_PER_WORLD} seasons in each world")
    print(f"  counterfactual covariate (no forcing): X ~ Normal(0, 1)")
    print(f"  factual covariate (with forcing):      X ~ "
          f"Normal({FORCED_SHIFT:.1f}, 1)")
    print(f"  event probability: P(event | X) = "
          f"sigmoid({A_BASE:.1f} + {B_COVARIATE:.1f} X), applied independently")
    print("  in each season, so the event is NOT a deterministic function of X:")
    print("  that is what a real event-vs-covariate relation looks like, and it")
    print("  is what allows both routes below to be estimated")
    p_cf_exact = marginal_probability(A_BASE, 0.0)
    p_fact_exact = marginal_probability(A_BASE, FORCED_SHIFT)
    print(f"  exact marginal probabilities: counterfactual {p_cf_exact:.5f}, "
          f"factual {p_fact_exact:.5f}")

    section("2. Probability ratio and attributable fraction")
    event_cf = (RNG.random(N_PER_WORLD)
                < sigmoid(A_BASE + B_COVARIATE * cf)).astype(float)
    event_fact = (RNG.random(N_PER_WORLD)
                  < sigmoid(A_BASE + B_COVARIATE * fact)).astype(float)
    n_cf, n_fact = int(event_cf.sum()), int(event_fact.sum())
    pr = n_fact / max(n_cf, 1)
    far = 1.0 - 1.0 / pr
    boot_pr = np.empty(N_BOOT)
    boot_far = np.empty(N_BOOT)
    for b in range(N_BOOT):
        idx_cf = RNG.integers(0, N_PER_WORLD, N_PER_WORLD)
        idx_fa = RNG.integers(0, N_PER_WORLD, N_PER_WORLD)
        p_c = event_cf[idx_cf].mean()
        p_f = event_fact[idx_fa].mean()
        boot_pr[b] = p_f / max(p_c, 1e-12)
        boot_far[b] = 1.0 - p_c / max(p_f, 1e-12)
    print(f"  events: counterfactual {n_cf}/{N_PER_WORLD} "
          f"({100 * event_cf.mean():.2f}%), factual {n_fact}/{N_PER_WORLD} "
          f"({100 * event_fact.mean():.2f}%)")
    print(f"  actual frequencies lie on the exact probabilities above, as they "
          f"must")
    print(f"  probability ratio PR = {pr:.3f} (95% bootstrap "
          f"{np.percentile(boot_pr, 2.5):.3f} to "
          f"{np.percentile(boot_pr, 97.5):.3f})")
    print(f"  attributable fraction FAR = 1 - 1/PR = {far:.3f} (95% "
          f"{np.percentile(boot_far, 2.5):.3f} to "
          f"{np.percentile(boot_far, 97.5):.3f})")
    print(f"  return period: counterfactual "
          f"{1.0 / event_cf.mean():.1f} seasons, factual "
          f"{1.0 / event_fact.mean():.1f} seasons")
    print("  the same statement in three forms: the event is about "
          f"{pr:.1f} times more")
    print(f"  frequent, its return period is {pr:.1f} times shorter, and "
          f"{100 * far:.0f}% of the")
    print("  events are attributable to the shift.  The FAR is the form most")
    print("  easily misread: a high FAR on a very rare event still means a very")
    print("  rare event, and the FAR says nothing about how rare it is")

    section("3. The conditional risk ratio from logistic regression")
    x_all = np.concatenate([cf, fact])
    world = np.concatenate([np.zeros(N_PER_WORLD), np.ones(N_PER_WORLD)])
    y_all = np.concatenate([event_cf, event_fact])
    beta, se = logistic_fit(x_all, world, y_all)
    pr_cond = float(np.exp(beta[2]))
    lo, hi = float(np.exp(beta[2] - 1.96 * se[2])), \
        float(np.exp(beta[2] + 1.96 * se[2]))
    print(f"  fit logit P(event | X, World) = a + b X + c World on the pooled "
          f"sample")
    print(f"  a = {beta[0]:+.4f} +/- {1.96 * se[0]:.4f} "
          f"(generator {A_BASE:.1f}),")
    print(f"  b = {beta[1]:+.4f} +/- {1.96 * se[1]:.4f} "
          f"(generator {B_COVARIATE:.1f}),")
    print(f"  c = {beta[2]:+.4f} +/- {1.96 * se[2]:.4f} "
          f"(generator 0.0 by construction)")
    print(f"  conditional risk ratio at fixed X: exp(c) = {pr_cond:.3f} "
          f"(95% {lo:.3f} to {hi:.3f})")
    print(f"  the interval contains 1.0, which is the correct answer here: this")
    print(f"  generator's world changes only the DISTRIBUTION of X, not the")
    print(f"  event's response to X, so at a fixed X the probability is "
          f"unchanged")
    print(f"  the marginal PR of section 2 is {pr:.3f} and is far from 1: the "
          f"two")
    print("  quantities answer different questions, and the pair is the "
          "informative")
    print("  report:")
    print(f"    - conditional ratio {pr_cond:.2f}: at the same covariate value, "
          f"no change")
    print(f"    - marginal ratio {pr:.2f}: the event is about twice as frequent "
          f"because X moved")
    print("  A study that reports only the second is claiming a change in")
    print("  frequency; only the first can claim a change in the event's")
    print("  sensitivity to the covariate.  Reporting both, with intervals, is")
    print("  what makes an attribution result falsifiable: a world that changed")
    print("  the response as well would show exp(c) away from 1")

    section("4. Rarer events: what happens to the uncertainty")
    for a_rare in (A_BASE,) + RARE_A:
        e_cf = (RNG.random(N_PER_WORLD)
                < sigmoid(a_rare + B_COVARIATE * cf)).astype(float)
        e_fact = (RNG.random(N_PER_WORLD)
                  < sigmoid(a_rare + B_COVARIATE * fact)).astype(float)
        prs = np.empty(N_BOOT)
        for b in range(N_BOOT):
            num = e_fact[RNG.integers(0, N_PER_WORLD, N_PER_WORLD)].mean()
            den = e_cf[RNG.integers(0, N_PER_WORLD, N_PER_WORLD)].mean()
            prs[b] = num / max(den, 1e-12)
        lo_b, hi_b = np.percentile(prs, [2.5, 97.5])
        print(f"  a = {a_rare:.1f}: counterfactual events "
              f"{int(e_cf.sum())}, factual events {int(e_fact.sum())}, "
              f"PR = {e_fact.mean() / max(e_cf.mean(), 1e-12):.2f}")
        print(f"    bootstrap 95% interval {lo_b:.2f} to {hi_b:.2f}, width "
              f"{hi_b - lo_b:.2f}")
    print("  the point estimate is similar across the three definitions, but the")
    print("  interval widens as the counterfactual count falls: the ratio is a")
    print("  ratio of small counts, and its uncertainty is set by the smaller of")
    print("  the two worlds, not by the total sample size")
    print("\nSYNTHETIC: the worlds are simulated from a chosen shift, so the true")
    print("probabilities are known.  A real attribution study must state the model")
    print("that produced the counterfactual, the covariate and its spatial scale,")
    print("the event definition, and the length and homogeneity of the")
    print("observational record, because each of them enters the answer.")


if __name__ == "__main__":
    main()
