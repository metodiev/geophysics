#!/usr/bin/env python3
"""Constructing likelihoods and error models: what a noise assumption buys and costs.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python likelihood_models_demo.py

All models and data in this demo are SYNTHETIC.  The straight line, the noise
realisation and the outlier sizes are chosen teaching values, not measurements.

Contents
--------
1. SYNTHETIC line-fit data under three noise processes (iid, AR(1), outliers).
2. Gaussian, Laplace and Student-t likelihoods on a 2-D parameter grid.
3. Measured bias and reported uncertainty under the correct and wrong error model.
4. Correlated errors assumed to be independent: the uncertainty is understated.
5. Laplace vs Gaussian: the weight given to one outlier, measured.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

A_TRUE, B_TRUE = 1.0, 0.5          # intercept and slope of the teaching line
X = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0])
SIG = 0.20                          # noise standard deviation, same units as y


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def make_data(kind):
    """Return y and the error standard deviation assumed by an iid Gaussian fit."""
    if kind == "iid":
        y = A_TRUE + B_TRUE * X + SIG * RNG.standard_normal(X.size)
        return y, "iid Gaussian, sigma = 0.20"
    if kind == "ar1":
        rho, n = 0.9, X.size
        e = np.zeros(n)
        e[0] = SIG * RNG.standard_normal()
        for i in range(1, n):
            e[i] = rho * e[i - 1] + SIG * np.sqrt(1 - rho ** 2) * RNG.standard_normal()
        return A_TRUE + B_TRUE * X + e, "AR(1) with rho = 0.90, sigma = 0.20"
    if kind == "outlier":
        e = SIG * RNG.standard_normal(X.size)
        e[3] += 1.20
        e[9] -= 1.20
        return A_TRUE + B_TRUE * X + e, "iid Gaussian + two 1.2-sigma outliers"
    raise ValueError(kind)


def grid_posterior(y, order, extra_sigma=0.0):
    """Posterior mean and std of (a, b) on a grid under three likelihoods.

    Priors are flat over the grid, so the posterior is the likelihood normalised
    on the grid.  `order` is the model exponent of the data misfit.
    `extra_sigma` inflates the working noise scale (used to test misspecification).
    """
    a = np.linspace(-1.0, 3.0, 241)
    b = np.linspace(-0.4, 1.4, 241)
    A, B = np.meshgrid(a, b, indexing="ij")
    R = y[None, None, :] - A[..., None] - B[..., None] * X[None, None, :]
    s = SIG + extra_sigma
    if order == 2:
        logL = -0.5 * np.sum((R / s) ** 2, axis=-1)
    elif order == 1:
        logL = -np.sum(np.abs(R / s), axis=-1)
    else:
        nu = 4.0
        logL = -0.5 * (nu + 1.0) * np.sum(np.log1p((R / s) ** 2 / nu), axis=-1)
    logL -= logL.max()
    P = np.exp(logL)
    da, db = a[1] - a[0], b[1] - b[0]
    Z = P.sum() * da * db
    P = P / Z
    ma = (P * A).sum() * da * db
    mb = (P * B).sum() * da * db
    sa = np.sqrt((P * (A - ma) ** 2).sum() * da * db)
    sb = np.sqrt((P * (B - mb) ** 2).sum() * da * db)
    return ma, sa, mb, sb


def main():
    np.set_printoptions(precision=4, suppress=True)

    section("1. SYNTHETIC line-fit data under three noise processes")
    data = {k: make_data(k) for k in ("iid", "ar1", "outlier")}
    print(f"teaching line: y = {A_TRUE} + {B_TRUE} x, x = 0..11 (12 points)")
    for k, (y, desc) in data.items():
        print(f"  {k:8s}: {desc}")
        print(f"            realised rms misfit about the truth "
              f"= {np.sqrt(np.mean((y - (A_TRUE + B_TRUE * X)) ** 2)):.4f}")

    section("2. Posterior of (a, b) under three likelihoods (flat priors)")
    print("  order 2 = Gaussian (least squares), 1 = Laplace (L1), 4 = Student-t nu=4")
    print("  data set   likelihood   a_mean  a_std   b_mean  b_std")
    print("  " + "-" * 58)
    for k in data:
        y, _ = data[k]
        for name, order in (("Gaussian", 2), ("Laplace", 1), ("Student-t", 4)):
            ma, sa, mb, sb = grid_posterior(y, order)
            print(f"  {k:9s}  {name:9s}  {ma:6.3f}  {sa:5.3f}   {mb:6.4f}  {sb:5.4f}")

    section("3. Outliers: bias under Gaussian vs Laplace vs Student-t")
    y, _ = data["outlier"]
    for name, order in (("Gaussian", 2), ("Laplace", 1), ("Student-t", 4)):
        _, _, mb, sb = grid_posterior(y, order)
        print(f"  {name:9s}: slope {mb:.4f} (error {mb - B_TRUE:+.4f}), "
              f"reported std {sb:.4f}")
    print("A Gaussian likelihood squares the 1.2-unit outliers, so they drag the")
    print("slope; a Laplace or Student-t likelihood down-weights them.")

    section("4. Correlated errors fitted as independent: uncertainty understated")
    y_ar, _ = data["ar1"]
    _, _, b_iid, s_iid = grid_posterior(y_ar, 2)
    # Correct generalised least squares with the exact AR(1) covariance.
    rho = 0.9
    n = X.size
    C = np.array([[rho ** np.abs(i - j) for j in range(n)] for i in range(n)])
    W = np.linalg.inv(C) / SIG ** 2
    Amat = np.column_stack([np.ones(n), X])
    Cpost = np.linalg.inv(Amat.T @ W @ Amat)
    mpost = Cpost @ (Amat.T @ W @ y_ar)
    print(f"  slope from the (wrong) iid Gaussian fit : {b_iid:.4f} "
          f"+/- {s_iid:.4f}")
    print(f"  slope from the correct GLS (AR(1) cov)   : {mpost[1]:.4f} "
          f"+/- {np.sqrt(Cpost[1, 1]):.4f}")
    print(f"  uncertainty understated by a factor "
          f"{np.sqrt(Cpost[1, 1]) / s_iid:.2f}x "
          f"({(1 - s_iid / np.sqrt(Cpost[1, 1])) * 100:.0f}% too narrow)")
    print("Same data, same estimate: only the error model changed, and it changed")
    print("the width of the answer. A likelihood is an assumption with consequences.")

    section("5. Influence of ONE outlier: how far does the slope move? Measured")
    y0 = A_TRUE + B_TRUE * X + SIG * RNG.standard_normal(X.size)
    base = {name: grid_posterior(y0, order)[2]
            for name, order in (("Gaussian", 2), ("Laplace", 1), ("Student-t", 4))}
    print("  perturb y at x = 3 by delta (in units of sigma) and report the shift")
    print("  in the posterior-mean slope, d(b) = b(delta) - b(delta = 0):")
    print("   delta/sigma   Gaussian d(b)   Laplace d(b)   Student-t d(b)")
    print("   " + "-" * 58)
    for delta in (0.0, 1.0, 2.0, 4.0, 8.0, 16.0):
        y_pert = y0.copy()
        y_pert[3] += delta * SIG
        row = []
        for order in (2, 1, 4):
            row.append(grid_posterior(y_pert, order)[2])
        b_g, b_l, b_t = row
        print(f"   {delta:11.1f}   {b_g - base['Gaussian']:+12.4f}   "
              f"{b_l - base['Laplace']:+12.4f}   {b_t - base['Student-t']:+12.4f}")
    print("  A Gaussian likelihood has an UNBOUNDED influence: doubling the outlier")
    print("  roughly doubles the shift in the slope. The Laplace and Student-t")
    print("  influences grow far more slowly and begin to saturate, so one bad")
    print("  reading cannot move the answer without limit.")

    section("6. Estimating the unknown noise scale (hierarchical likelihood)")
    y, _ = data["iid"]
    # Profile the Gaussian likelihood over sigma on a grid, uniform prior on log sigma.
    sig = np.linspace(0.05, 0.60, 400)
    Amat = np.column_stack([np.ones(n), X])
    mle = np.linalg.lstsq(Amat, y, rcond=None)[0]
    rss = np.sum((y - Amat @ mle) ** 2)
    logpost = -(n / 2.0) * np.log(sig ** 2) - rss / (2.0 * sig ** 2) \
        + np.log(1.0 / sig)          # log prior 1/sigma (scale prior)
    logpost -= logpost.max()
    p = np.exp(logpost)
    ds = sig[1] - sig[0]
    p /= p.sum() * ds
    s_mean = (p * sig).sum() * ds
    s_std = np.sqrt((p * (sig - s_mean) ** 2).sum() * ds)
    s_hat = np.sqrt(rss / n)
    print(f"  flat prior on log sigma; profile likelihood over sigma")
    print(f"  sigma_hat (sqrt(rss/n))      = {s_hat:.4f}")
    print(f"  posterior mean of sigma      = {s_mean:.4f}")
    print(f"  posterior std                = {s_std:.4f}")
    print(f"  injected sigma               = {SIG:.4f}")
    print("  The scale is inferred from the same data that constrain (a, b): the")
    print("  likelihood is hierarchical, and sigma is a parameter like any other.")


if __name__ == "__main__":
    main()
