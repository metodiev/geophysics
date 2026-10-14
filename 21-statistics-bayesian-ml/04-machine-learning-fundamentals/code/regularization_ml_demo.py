#!/usr/bin/env python3
"""Regularisation on SYNTHETIC data: ridge and lasso coefficient paths, the
cross-validated choice of the penalty, and early stopping as an implicit
regulariser.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python regularization_ml_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. Ridge coefficients against the penalty.
2. Lasso coefficients, sparsity and support recovery.
3. Cross-validation for the penalty.
4. Early stopping in gradient descent.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def ridge(X, y, lam):
    n, p = X.shape
    return np.linalg.solve(X.T @ X + lam * np.eye(p), X.T @ y)


def soft(u, t):
    return np.sign(u) * max(abs(u) - t, 0.0)


def lasso(X, y, lam, iters=300):
    n, p = X.shape
    beta = np.zeros(p)
    col = (X ** 2).sum(axis=0)
    for _ in range(iters):
        for j in range(p):
            r = y - X @ beta + X[:, j] * beta[j]
            beta[j] = soft(X[:, j] @ r, lam * n / 2.0) / col[j]
    return beta


def main():
    print("SYNTHETIC high-dimensional regression: 60 samples, 20 predictors, "
          "only 4 with a nonzero coefficient.")

    n, p = 60, 20
    X = RNG.standard_normal((n, p))
    beta_true = np.zeros(p)
    beta_true[[0, 3, 7, 12]] = [2.0, -1.5, 1.0, 0.8]
    y = X @ beta_true + 0.5 * RNG.standard_normal(n)

    section("1. Ridge coefficients against the penalty")
    print("  lambda    ||beta||^2   beta_0     beta_3     beta_7    beta_12")
    for lam in (0.01, 1.0, 10.0, 100.0, 1000.0):
        b = ridge(X, y, lam)
        print(f"  {lam:8.2f}  {np.sum(b ** 2):10.4f}  {b[0]:8.4f}  {b[3]:8.4f}"
              f"  {b[7]:8.4f}  {b[12]:8.4f}")
    print("  ridge shrinks every coefficient smoothly towards zero and never")
    print("  sets one exactly to zero, so it cannot select a subset.")

    section("2. Lasso coefficients and sparsity")
    print("  lambda   nonzero   beta_0     beta_3     beta_7    beta_12"
          "   support recovered")
    for lam in (0.01, 0.05, 0.1, 0.2, 0.5):
        b = lasso(X, y, lam)
        nz = np.sum(np.abs(b) > 1e-6)
        rec = len(set(np.nonzero(np.abs(b) > 1e-6)[0]) & {0, 3, 7, 12})
        print(f"  {lam:6.2f}  {int(nz):7d}   {b[0]:8.4f}  {b[3]:8.4f}"
              f"  {b[7]:8.4f}  {b[12]:8.4f}   {rec}/4")
    print("  the lasso sets coefficients exactly to zero: at a moderate penalty")
    print("  it recovers part of the true support and leaves noise predictors at 0.")

    section("3. Cross-validation for the penalty")
    perm = RNG.permutation(n)
    folds = np.array_split(perm, 5)
    lams = np.logspace(-3, 2, 25)
    cv_mse = []
    for lam in lams:
        errs = []
        for k in range(5):
            tr = np.concatenate([folds[j] for j in range(5) if j != k])
            va = folds[k]
            b = ridge(X[tr], y[tr], lam)
            errs.append(float(np.mean((X[va] @ b - y[va]) ** 2)))
        cv_mse.append(np.mean(errs))
    cv_mse = np.array(cv_mse)
    best_lam = float(lams[int(np.argmin(cv_mse))])
    print(f"  best lambda by 5-fold CV = {best_lam:.4f} "
          f"(CV MSE {cv_mse.min():.4f})")
    print(f"  CV MSE at lambda = 0.001 = {cv_mse[0]:.4f}, at lambda = 100 = "
          f"{cv_mse[-1]:.4f}")
    print(f"  the ridge solution at the CV penalty has ||beta||^2 = "
          f"{np.sum(ridge(X, y, best_lam) ** 2):.4f}")
    print("  the curve is flat near its minimum, so the exact penalty matters")
    print("  far less than getting the order of magnitude right.")

    section("4. Early stopping in gradient descent")
    b = np.zeros(p)
    lr = 0.05
    n_train = 25
    best = (0, np.inf)
    train_curve, val_curve = [], []
    for it in range(1, 3001):
        b -= lr * 2.0 / n_train * X[:n_train].T @ (X[:n_train] @ b - y[:n_train])
        tr = float(np.mean((X[:n_train] @ b - y[:n_train]) ** 2))
        va = float(np.mean((X[n_train:] @ b - y[n_train:]) ** 2))
        train_curve.append(tr)
        val_curve.append(va)
        if va < best[1]:
            best = (it, va)
    print(f"  training on {n_train} samples with all {p} predictors")
    print(f"  iteration 1     train MSE = {train_curve[0]:.4f}, "
          f"val MSE = {val_curve[0]:.4f}")
    print(f"  iteration 100   train MSE = {train_curve[99]:.4f}, "
          f"val MSE = {val_curve[99]:.4f}")
    print(f"  iteration 3000  train MSE = {train_curve[-1]:.4f}, "
          f"val MSE = {val_curve[-1]:.4f}")
    print(f"  best validation MSE {best[1]:.4f} at iteration {best[0]}")
    print("  training error keeps falling while validation error turns up: the")
    print("  stopping point is a regularisation choice made by the data.")


if __name__ == "__main__":
    main()
