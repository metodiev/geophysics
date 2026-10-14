#!/usr/bin/env python3
"""Causal inference: what adjustment removes, and what it cannot.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python causal_inference_methods_demo.py

Everything here is SYNTHETIC.  The treatment, the confounder, the outcome and the
unmeasured term are generated below with a known true effect; no observational
data set, trial or published effect estimate is used.

Sections
--------
1. A synthetic observational study with a known average treatment effect.
2. Four estimators: unadjusted, regression, inverse-probability weighting,
   stratification.
3. An unmeasured confounder: the bias that no adjustment removes.
4. What the design would have to change to remove it.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression

RNG = np.random.default_rng(20261014)

N = 2000            # units
TRUE_ATE = 2.0      # the generator's causal effect, in outcome units
BETA_Z = 1.0        # confounder's effect on the outcome
GAMMA_U = 0.8       # unmeasured confounder's effect on the outcome
N_STRATA = 5
N_BOOT = 400


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def dgp(include_u_in_outcome):
    """One realisation: treatment, confounders and outcome."""
    z = RNG.standard_normal(N)              # measured confounder
    u = RNG.standard_normal(N)              # unmeasured confounder
    d = (z + u > 0.0).astype(int)           # treatment assignment
    noise = RNG.standard_normal(N)
    y = TRUE_ATE * d + BETA_Z * z + noise
    if include_u_in_outcome:
        y = y + GAMMA_U * u
    return z, u, d, y


def ols(y, columns):
    design = np.column_stack([np.ones(y.size)] + list(columns))
    coef, *_ = np.linalg.lstsq(design, y, rcond=None)
    resid = y - design @ coef
    dof = y.size - design.shape[1]
    cov = np.linalg.inv(design.T @ design) * np.sum(resid ** 2) / dof
    return coef, np.sqrt(np.diag(cov))


def main():
    section("1. A synthetic observational study with a known effect")
    z, u, d, y = dgp(False)
    print(f"SYNTHETIC study: n = {N} units")
    print(f"  treatment: D = 1 if Z + U > 0, where Z (measured) and U "
          f"(unmeasured) are standard normal")
    print(f"  outcome:   Y = {TRUE_ATE:.1f} D + {BETA_Z:.1f} Z + noise, noise "
          f"standard normal")
    print(f"  TRUE average treatment effect = {TRUE_ATE:.3f} outcome units")
    print(f"  treated units = {int(d.sum())} ({100 * d.mean():.1f}%)")
    print(f"  E[Z | D = 1] - E[Z | D = 0] = "
          f"{z[d == 1].mean() - z[d == 0].mean():.3f}: the confounder is "
          f"unbalanced")

    section("2. Four estimators of the same quantity")
    naive = y[d == 1].mean() - y[d == 0].mean()
    se_naive = np.sqrt(y[d == 1].var(ddof=1) / d.sum()
                       + y[d == 0].var(ddof=1) / (N - d.sum()))
    print(f"  unadjusted difference in means = {naive:+.3f} "
          f"+/- {1.96 * se_naive:.3f} (95%), bias "
          f"{naive - TRUE_ATE:+.3f}")

    coef, se = ols(y, [d, z])
    print(f"  regression on D and Z: effect = {coef[1]:+.3f} "
          f"+/- {1.96 * se[1]:.3f}, bias {coef[1] - TRUE_ATE:+.3f}")

    ps_model = LogisticRegression(max_iter=1000)
    ps_model.fit(z.reshape(-1, 1), d)
    ps = ps_model.predict_proba(z.reshape(-1, 1))[:, 1]
    ps = np.clip(ps, 0.02, 0.98)
    ipw = (np.sum(d * y / ps) / np.sum(d / ps)
           - np.sum((1 - d) * y / (1 - ps)) / np.sum((1 - d) / (1 - ps)))
    boot = []
    for _ in range(N_BOOT):
        idx = RNG.integers(0, N, N)
        ps_b = np.clip(ps[idx], 0.02, 0.98)
        d_b, y_b = d[idx], y[idx]
        boot.append(np.sum(d_b * y_b / ps_b) / np.sum(d_b / ps_b)
                    - np.sum((1 - d_b) * y_b / (1 - ps_b))
                    / np.sum((1 - d_b) / (1 - ps_b)))
    print(f"  inverse-probability weighting = {ipw:+.3f} "
          f"+/- {1.96 * np.std(boot, ddof=1):.3f} (bootstrap), bias "
          f"{ipw - TRUE_ATE:+.3f}")

    edges = np.quantile(ps, np.linspace(0.0, 1.0, N_STRATA + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    stratum = np.digitize(ps, edges[1:-1])
    effect, weight = 0.0, 0.0
    for k in range(N_STRATA):
        in_s = stratum == k
        n_t = int(np.sum(in_s & (d == 1)))
        n_c = int(np.sum(in_s & (d == 0)))
        if n_t == 0 or n_c == 0:
            continue
        diff = y[in_s & (d == 1)].mean() - y[in_s & (d == 0)].mean()
        w = in_s.sum() / N
        effect += w * diff
        weight += w
    effect /= weight
    print(f"  stratification on propensity quintiles = {effect:+.3f}, bias "
          f"{effect - TRUE_ATE:+.3f}")
    print(f"  propensity scores range {ps.min():.3f} to {ps.max():.3f}")
    print("  three adjusted estimators and one unadjusted: the three agree "
          "because")
    print("  they all condition on the SAME information, not because adjustment")
    print("  is a truth machine")

    section("3. An unmeasured confounder")
    z2, u2, d2, y2 = dgp(True)
    coef2, se2 = ols(y2, [d2, z2])
    naive2 = y2[d2 == 1].mean() - y2[d2 == 0].mean()
    ps2 = np.clip(LogisticRegression(max_iter=1000).fit(
        z2.reshape(-1, 1), d2).predict_proba(z2.reshape(-1, 1))[:, 1], 0.02, 0.98)
    ipw2 = (np.sum(d2 * y2 / ps2) / np.sum(d2 / ps2)
            - np.sum((1 - d2) * y2 / (1 - ps2)) / np.sum((1 - d2) / (1 - ps2)))
    marginal_imbalance = u2[d2 == 1].mean() - u2[d2 == 0].mean()
    coef_u, _ = ols(u2, [d2, z2])
    conditional_imbalance = float(coef_u[1])
    expected_bias = GAMMA_U * conditional_imbalance
    print(f"  the same study, with the outcome now also depending on the")
    print(f"  unmeasured U: Y = {TRUE_ATE:.1f} D + {BETA_Z:.1f} Z + "
          f"{GAMMA_U:.1f} U + noise")
    print(f"  the marginal imbalance in the unmeasured term "
          f"E[U|D=1] - E[U|D=0] = {marginal_imbalance:+.3f}")
    print(f"  unadjusted difference = {naive2:+.3f}, bias "
          f"{naive2 - TRUE_ATE:+.3f}")
    print(f"  regression on D and Z = {coef2[1]:+.3f} +/- "
          f"{1.96 * se2[1]:.3f}, bias {coef2[1] - TRUE_ATE:+.3f}")
    print(f"  the omitted-variable formula predicts that bias exactly: the "
          f"coefficient")
    print(f"  of D in the regression of U on (D, Z) is "
          f"{conditional_imbalance:+.3f}, so the bias should be")
    print(f"  {GAMMA_U:.1f} x {conditional_imbalance:+.3f} = "
          f"{expected_bias:+.3f}, against the measured "
          f"{coef2[1] - TRUE_ATE:+.3f}")
    print(f"  inverse-probability weighting = {ipw2:+.3f}, bias "
          f"{ipw2 - TRUE_ATE:+.3f}")
    print("  all three are biased in the same direction and by a similar "
          "amount:")
    print("  adjusting for Z cannot remove the part of the assignment that "
          "depends")
    print("  on U, and the confidence intervals are now centred on the wrong "
          "value")

    section("4. What the design would have to change")
    print(f"  an unmeasured confounder with coefficient {GAMMA_U:.1f} on the "
          f"outcome")
    print(f"  produces a bias of about {expected_bias:+.3f} outcome units -- "
          f"{100 * abs(expected_bias) / TRUE_ATE:.0f}% of the")
    print("  effect being estimated, against a standard error of "
          f"{1.96 * se2[1]:.3f}.")
    print("  no estimator repairs this: the remedy is a design change, in order "
          "of")
    print("  strength: (i) randomise the treatment, which severs D from both Z "
          "and U;")
    print("  (ii) find a source of exogenous variation in D -- an instrument, a")
    print("  policy threshold, a natural experiment -- and use instrumental")
    print("  variables or a regression discontinuity; (iii) measure U; "
          "(iv) bound the")
    print("  bias with a sensitivity analysis that states how strong an "
          "unmeasured")
    print("  confounder would have to be to explain the estimate away")
    print("\nSYNTHETIC: the causal structure is constructed here, so the true "
          "effect is")
    print("known and the biases are measured. On real data the same estimators "
          "are")
    print("used without that luxury, and the identification argument -- not the")
    print("estimator -- is what carries the claim.")


if __name__ == "__main__":
    main()
