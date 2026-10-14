#!/usr/bin/env python3
"""The bias-variance trade-off on SYNTHETIC data: polynomial fits of increasing
degree, the measured train and test error, and a Monte-Carlo decomposition of the
expected squared error into bias squared and variance.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python bias_variance_demo.py

Everything is SYNTHETIC: a stated polynomial truth plus Gaussian noise. No
measured value is used.

Sections
--------
1. Train and test error against model complexity.
2. A Monte-Carlo bias-variance decomposition at one complexity.
3. The decomposition across complexity.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N_TRAIN = 25
N_TEST = 400
SIGMA = 0.3
DEGREES = (1, 3, 5, 7, 9, 12)
N_MC = 400
GRID = np.linspace(-1.0, 1.0, 60)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def truth(x):
    return np.sin(2.5 * x) + 0.3 * x


def design(x, degree):
    # Legendre basis: well conditioned at high degree, unlike a raw Vandermonde
    return np.polynomial.legendre.legvander(x, degree)


def fit_predict(xtr, ytr, degree):
    return design(xtr, degree) @ np.linalg.lstsq(design(xtr, degree), ytr,
                                                 rcond=None)[0]


def main():
    print(f"SYNTHETIC regression: y = sin(2.5x) + 0.3x + N(0, {SIGMA:.2f}^2), "
          f"{N_TRAIN} training points, {N_TEST} test points, x in [-1, 1].")

    section("1. Train and test error against model complexity")
    xtr = RNG.uniform(-1.0, 1.0, N_TRAIN)
    ytr = truth(xtr) + SIGMA * RNG.standard_normal(N_TRAIN)
    xte = RNG.uniform(-1.0, 1.0, N_TEST)
    yte = truth(xte) + SIGMA * RNG.standard_normal(N_TEST)
    print("  degree   train MSE   test MSE   parameters")
    for d in DEGREES:
        beta = np.linalg.lstsq(design(xtr, d), ytr, rcond=None)[0]
        pred_tr = design(xtr, d) @ beta
        pred_te = design(xte, d) @ beta
        print(f"  {d:6d}   {np.mean((pred_tr - ytr) ** 2):9.4f}   "
              f"{np.mean((pred_te - yte) ** 2):8.4f}   {d + 1:10d}")
    print("  training error falls monotonically; test error is U-shaped, with a")
    print("  minimum at an intermediate degree. That minimum is the trade-off.")

    section("2. A Monte-Carlo bias-variance decomposition")
    degree = 9
    preds = np.empty((N_MC, GRID.size))
    for m in range(N_MC):
        xs = RNG.uniform(-1.0, 1.0, N_TRAIN)
        ys = truth(xs) + SIGMA * RNG.standard_normal(N_TRAIN)
        beta = np.linalg.lstsq(design(xs, degree), ys, rcond=None)[0]
        preds[m] = design(GRID, degree) @ beta
    mean_pred = preds.mean(axis=0)
    bias2 = float(np.mean((mean_pred - truth(GRID)) ** 2))
    var = float(np.mean(preds.var(axis=0, ddof=1)))
    noise = SIGMA ** 2
    total = bias2 + var + noise
    print(f"  degree {degree}, averaged over a grid and {N_MC} training sets:")
    print(f"    bias^2            = {bias2:.5f}")
    print(f"    variance          = {var:.5f}")
    print(f"    noise variance    = {noise:.5f}")
    print(f"    expected MSE      = {total:.5f}")
    print(f"    measured test MSE = "
          f"{np.mean((preds - truth(GRID)[None, :]) ** 2):.5f}")
    print("  the three terms sum to the expected error; only the noise term is")
    print("  irreducible, and only the bias term shrinks for free.")

    section("3. Bias, variance and error across complexity")
    print("  degree    bias^2    variance    total")
    for d in DEGREES:
        preds = np.empty((N_MC, GRID.size))
        for m in range(N_MC):
            xs = RNG.uniform(-1.0, 1.0, N_TRAIN)
            ys = truth(xs) + SIGMA * RNG.standard_normal(N_TRAIN)
            beta = np.linalg.lstsq(design(xs, d), ys, rcond=None)[0]
            preds[m] = design(GRID, d) @ beta
        b2 = float(np.mean((preds.mean(axis=0) - truth(GRID)) ** 2))
        v = float(np.mean(preds.var(axis=0, ddof=1)))
        print(f"  {d:6d}   {b2:8.5f}   {v:9.5f}   {b2 + v + SIGMA ** 2:8.5f}")
    print("  bias falls with degree and variance rises; their sum is minimised")
    print("  near the degree that matches the truth, not at the largest model.")


if __name__ == "__main__":
    main()
