#!/usr/bin/env python3
"""Taxonomy of uncertainty: aleatory, epistemic and structural, measured.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python uncertainty_taxonomy_demo.py

All models and data in this demo are SYNTHETIC.  The design, the noise level, the
true slope and the structural coefficient are chosen teaching values.

Contents
--------
1. A prediction-error budget: bias^2 + epistemic variance + aleatory variance.
2. How each component moves with the prediction location.
3. How each component responds to more data (epistemic falls, aleatory does not).
4. Poor experimental design inflates epistemic uncertainty: a near-degenerate
   two-parameter problem, before and after one informative datum.
5. Reporting: what a claim of "reduced uncertainty" must specify.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

M_TRUE = 2.0          # true slope, model units per unit x
BETA = 0.005          # structural coefficient of the unmodelled x^2 term
SIGMA = 0.2           # aleatory measurement noise, same units as the data
X = np.arange(1.0, 9.0)   # SYNTHETIC design: 8 stations at x = 1..8 (km)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def fit_slope(x, y):
    """Least-squares slope through the origin for y = m x, and its variance."""
    m = float(np.sum(x * y) / np.sum(x ** 2))
    var = SIGMA ** 2 / float(np.sum(x ** 2))
    return m, var


def main():
    # SYNTHETIC data: a linear term plus a small quadratic structural term.
    y = M_TRUE * X + BETA * X ** 2 + SIGMA * RNG.standard_normal(X.size)
    m_hat, var_m = fit_slope(X, y)
    sd_m = np.sqrt(var_m)

    section("1. A prediction-error budget at one location")
    print(f"SYNTHETIC truth: d(x) = {M_TRUE} x + {BETA} x^2 + N(0, {SIGMA}^2)")
    print(f"fitted model  : d(x) = m x,  with a flat prior on m")
    print(f"estimate      : m = {m_hat:.4f} +/- {sd_m:.4f} "
          f"(model units per unit x)")
    print(f"design        : {X.size} stations at x = {X[0]:.0f}..{X[-1]:.0f} km, "
          f"sum(x^2) = {np.sum(X ** 2):.0f} km^2")
    print(f"\n  x* (km)   bias (units)   epistemic sd   aleatory sd"
          f"   total RMSE   bias share")
    print("  " + "-" * 78)
    for xstar in (2.0, 4.0, 6.0, 8.0, 12.0):
        bias = BETA * xstar ** 2          # E[m_hat] = m, so bias is structural
        epi_var = xstar ** 2 * var_m
        ale_var = SIGMA ** 2
        total = np.sqrt(bias ** 2 + epi_var + ale_var)
        share = bias ** 2 / (bias ** 2 + epi_var + ale_var)
        print(f"  {xstar:6.1f}   {bias:11.4f}   {np.sqrt(epi_var):12.4f}   "
              f"{np.sqrt(ale_var):11.4f}   {total:10.4f}   {share * 100:8.1f}%")
    print("At x* = 2 km the budget is almost entirely aleatory noise. By x* = 12 km")
    print("the extrapolated structural term dominates. The three components are")
    print("separately named because they respond to different remedies.")

    section("2. What each component responds to")
    print("  component     reduced by more stations?   reduced by a better model?")
    print("  " + "-" * 72)
    print("  aleatory      no (it is the measurement)  no")
    print("  epistemic     yes, as 1/sum(x^2)          partly (a tighter prior)")
    print("  structural    no                          yes, only by changing physics")
    print("\nDoubling the number of stations inside the same range:")
    x2 = np.linspace(1.0, 8.0, 2 * X.size)
    _, var_m2 = fit_slope(x2, M_TRUE * x2)
    print(f"  sum(x^2): {np.sum(X ** 2):.0f} -> {np.sum(x2 ** 2):.0f} km^2, "
          f"so the epistemic variance at x* = 4 km falls by a factor "
          f"{var_m * 16 / (var_m2 * 16):.3f}")
    print("Extending the aperture instead (stations to 16 km):")
    x3 = np.arange(1.0, 17.0)
    _, var_m3 = fit_slope(x3, M_TRUE * x3)
    print(f"  sum(x^2): {np.sum(X ** 2):.0f} -> {np.sum(x3 ** 2):.0f} km^2, "
          f"so the epistemic variance at x* = 4 km falls by a factor "
          f"{var_m * 16 / (var_m3 * 16):.3f}")
    print("Same number of extra stations would have been used either way; the")
    print("design, not the count, controls the epistemic term.")

    section("3. Epistemic and aleatory are not interchangeable")
    print("The aleatory standard deviation is a property of the measurement and")
    print(f"does not fall with n: it is {SIGMA:.3f} data units at every station.")
    print("The epistemic standard deviation at x* = 4 km falls as 1/sqrt(sum x^2):")
    for label, xs in (("8 stations, 1-8 km", X), ("16 stations, 1-8 km", x2),
                      ("16 stations, 1-16 km", x3)):
        _, v = fit_slope(xs, M_TRUE * xs)
        print(f"  {label:22s}: epistemic sd at 4 km = {4 * np.sqrt(v):.5f} "
              f"(data units)")
    print("A report that says 'more data reduced the uncertainty' must say which")
    print("term fell. Here no amount of extra data inside 1-8 km reduces the")
    print("structural term, and no amount reduces the aleatory term at all.")

    section("4. Poor design inflates the epistemic term: a degenerate problem")
    # Two parameters with a nearly degenerate design: the two rows are almost
    # parallel, so m1 - m2 is only weakly constrained.  The design is
    # ill-conditioned rather than singular.
    G = np.array([[1.0, 1.0],
                  [1.01, 1.0]])
    sigma_obs = 0.05
    C = sigma_obs ** 2 * np.linalg.inv(G.T @ G)
    lam = np.linalg.eigvalsh(C)
    print(f"SYNTHETIC design G = {G.tolist()}, sigma = {sigma_obs}")
    print(f"  singular values of G          : "
          f"{np.array2string(np.linalg.svd(G, compute_uv=False), precision=4)}")
    print(f"  posterior sd of m1, m2        : "
          f"{np.array2string(np.sqrt(np.diag(C)), precision=4)}")
    print(f"  posterior correlation         : {C[0, 1] / np.sqrt(C[0, 0] * C[1, 1]):+.4f}")
    print(f"  eigenvalues of the posterior covariance: "
          f"{np.array2string(np.sort(lam), precision=4)}")
    print(f"  sd along the worst direction  : {np.sqrt(lam[-1]):.4f}")
    # Add one datum that separates the two parameters: d3 = m1 - m2.
    G3 = np.vstack([G, [1.0, -1.0]])
    C3 = sigma_obs ** 2 * np.linalg.inv(G3.T @ G3)
    lam3 = np.linalg.eigvalsh(C3)
    print(f"\nafter adding the datum d3 = m1 - m2 (sigma = {sigma_obs}):")
    print(f"  posterior sd of m1, m2        : "
          f"{np.array2string(np.sqrt(np.diag(C3)), precision=4)}")
    print(f"  sd along the worst direction  : {np.sqrt(lam3[-1]):.4f}")
    print(f"  reduction factor in the worst direction: "
          f"{np.sqrt(lam[-1] / lam3[-1]):.1f}x")
    print("One well-placed datum is worth more than many badly placed ones: the")
    print("epistemic term is a property of the design, and it can be designed away.")

    section("5. What a claim of reduced uncertainty must specify")
    print("A complete statement names the component and the location:")
    xstar = 4.0
    bias = BETA * xstar ** 2
    epi = xstar ** 2 * var_m3
    print(f"  at x* = {xstar:.0f} km, with the extended aperture to 16 km,")
    print(f"    aleatory sd    = {SIGMA:.3f} data units (unchanged by design)")
    print(f"    epistemic sd   = {np.sqrt(epi):.5f} data units")
    print(f"    structural bias= {bias:.4f} data units (unchanged by design)")
    print(f"    total RMSE     = {np.sqrt(bias ** 2 + epi + SIGMA ** 2):.4f}")
    print("  A smaller epistemic term did not remove the structural bias. That bias")
    print("  grows as x*^2 and becomes the largest single term only at extrapolated")
    print("  distances: the measured budget above gives it 66.1% of the mean square")
    print("  error at 8 km and 88.4% at 12 km.")


if __name__ == "__main__":
    main()
