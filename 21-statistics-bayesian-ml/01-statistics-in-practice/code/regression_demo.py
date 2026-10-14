#!/usr/bin/env python3
"""Linear, multiple and robust regression on SYNTHETIC data: an outlier that
carries leverage, the Huber M-estimator against ordinary least squares, and the
variance inflation produced by collinear predictors.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python regression_demo.py

All data are SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. Simple OLS with and without one high-leverage observation.
2. Robust regression: Huber M-estimator versus OLS.
3. Multiple regression and the variance-inflation factor.
4. Influence diagnostics: leverage and Cook's distance.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N = 100                    # calibration points
INTERCEPT, SLOPE = 2.0, 0.5   # truth: y = 2.0 + 0.5 x, y in mGal, x in km
SIGMA = 1.0                # noise standard deviation, mGal
X_LEV, Y_LEV = 120.0, 20.0  # the leverage observation (km, mGal)
N2 = 200                   # samples for the multiple-regression section


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def ols(X, y):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    n, p = X.shape
    s2 = float(resid @ resid) / (n - p)
    cov = s2 * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    tss = float(((y - y.mean()) ** 2).sum())
    r2 = 1.0 - float(resid @ resid) / tss
    return beta, se, r2, resid, s2


def huber_irls(X, y, c=1.345, iters=200):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    for _ in range(iters):
        resid = y - X @ beta
        scale = 1.4826 * np.median(np.abs(resid - np.median(resid)))
        u = np.abs(resid) / max(scale, 1e-12)
        weights = np.where(u <= c, 1.0, c / np.maximum(u, 1e-12))
        Xw = X * weights[:, None]
        beta = np.linalg.solve(X.T @ Xw, Xw.T @ y)
    return beta, weights


def main():
    print("SYNTHETIC gravity profile: y (mGal) = 2.0 + 0.5 x (km) + N(0, 1^2) "
          "mGal.")

    x = np.arange(N, dtype=float)
    y = INTERCEPT + SLOPE * x + SIGMA * RNG.standard_normal(N)

    section("1. Simple OLS with and without a high-leverage point")
    X = np.column_stack([np.ones(N), x])
    beta, se, r2, _, s2 = ols(X, y)
    print(f"  clean        intercept = {beta[0]:.3f} +/- {se[0]:.3f} mGal, "
          f"slope = {beta[1]:.4f} +/- {se[1]:.4f} mGal/km, R^2 = {r2:.4f}")
    print(f"               residual variance s^2 = {s2:.3f} mGal^2")
    xl = np.append(x, X_LEV)
    yl = np.append(y, Y_LEV)
    Xl = np.column_stack([np.ones(N + 1), xl])
    beta_l, se_l, r2_l, res_l, s2_l = ols(Xl, yl)
    print(f"  + one point  intercept = {beta_l[0]:.3f} +/- {se_l[0]:.3f} mGal, "
          f"slope = {beta_l[1]:.4f} +/- {se_l[1]:.4f} mGal/km, R^2 = {r2_l:.4f}")
    print(f"               slope error = "
          f"{100 * abs(beta_l[1] - SLOPE) / SLOPE:.1f} % of the true slope "
          f"(clean bias {100 * abs(beta[1] - SLOPE) / SLOPE:.2f} %)")

    section("2. Robust regression: Huber M-estimator")
    beta_h, weights = huber_irls(Xl, yl)
    print(f"  OLS (contaminated)   intercept = {beta_l[0]:.3f}, "
          f"slope = {beta_l[1]:.4f} mGal/km")
    print(f"  Huber (contaminated) intercept = {beta_h[0]:.3f}, "
          f"slope = {beta_h[1]:.4f} mGal/km")
    print(f"  clean OLS (reference) intercept = {beta[0]:.3f}, "
          f"slope = {beta[1]:.4f} mGal/km")
    print(f"  Huber slope error = {100 * abs(beta_h[1] - SLOPE) / SLOPE:.1f} % "
          f"of truth, versus {100 * abs(beta_l[1] - SLOPE) / SLOPE:.1f} % for OLS")
    print(f"  Huber down-weights {int(np.sum(weights < 0.5))} of {N + 1} points "
          f"; the minimum weight is {weights.min():.4f}")

    section("3. Multiple regression and collinearity")
    x1 = RNG.standard_normal(N2)
    x2_high = x1 + 0.05 * RNG.standard_normal(N2)      # nearly collinear
    x2_low = RNG.standard_normal(N2)                   # independent
    for label, x2 in (("collinear", x2_high), ("independent", x2_low)):
        y2 = 1.0 + 2.0 * x1 + 3.0 * x2 + 0.5 * RNG.standard_normal(N2)
        Xm = np.column_stack([np.ones(N2), x1, x2])
        bm, sem, r2m, _, _ = ols(Xm, y2)
        r_12 = np.corrcoef(x1, x2)[0, 1]
        vif = 1.0 / (1.0 - r_12 ** 2)
        print(f"  {label:12s} corr(x1,x2) = {r_12:+.4f}  VIF = {vif:8.1f}")
        print(f"               beta1 = {bm[1]:.3f} +/- {sem[1]:.3f},  "
              f"beta2 = {bm[2]:.3f} +/- {sem[2]:.3f},  R^2 = {r2m:.4f}")
    print("  the coefficient standard errors, not the point estimates, are what")
    print("  collinearity inflates; the SE scales as sqrt(VIF).")

    section("4. Influence: leverage and Cook's distance")
    XtX_inv = np.linalg.inv(Xl.T @ Xl)
    h = np.einsum("ij,jk,ik->i", Xl, XtX_inv, Xl)
    p = 2
    cook = (res_l ** 2 / (p * s2_l)) * (h / (1.0 - h) ** 2)
    i_lev = int(np.argmax(h))
    print(f"  mean leverage h_bar = {h.mean():.5f} (= p/n = {p}/{N + 1})")
    print(f"  the leveraged point: h_ii = {h[i_lev]:.4f}, "
          f"Cook's D = {cook[i_lev]:.3f}")
    print(f"  largest Cook's D among the other points = "
          f"{np.sort(cook)[-2]:.4f}")
    threshold = 4.0 / (N + 1)
    print(f"  conventional Cook's-D threshold 4/n = {threshold:.4f}; "
          f"{int(np.sum(cook > threshold))} point(s) exceed it")


if __name__ == "__main__":
    main()
