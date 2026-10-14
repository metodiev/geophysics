#!/usr/bin/env python3
"""Model assessment on SYNTHETIC data: a single hold-out versus k-fold
cross-validation, classification metrics with an ROC curve, and a demonstration
of how feature selection on the full data leaks information and inflates an
apparent score.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python model_assessment_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. Hold-out versus k-fold cross-validation.
2. Classification metrics: accuracy, precision, recall, ROC AUC.
3. Leakage: selecting features on the full data inflates the score.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def ridge_fit(X, y, lam):
    n, p = X.shape
    A = X.T @ X + lam * np.eye(p)
    return np.linalg.solve(A, X.T @ y)


def main():
    print("SYNTHETIC data generated below; no measured value is used.")

    section("1. Hold-out versus k-fold cross-validation")
    n, p = 120, 8
    X = RNG.standard_normal((n, p))
    beta_true = np.array([1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0])
    y = X @ beta_true + 0.5 * RNG.standard_normal(n)
    lam = 1.0

    def mse_of(idx_fit, idx_val):
        b = ridge_fit(X[idx_fit], y[idx_fit], lam)
        return float(np.mean((X[idx_val] @ b - y[idx_val]) ** 2))

    perm = RNG.permutation(n)
    holdout = perm[:30]
    train = perm[30:]
    hold_mse = mse_of(train, holdout)
    folds = np.array_split(perm, 5)
    cv = [mse_of(np.concatenate([folds[j] for j in range(5) if j != k]), folds[k])
          for k in range(5)]
    print(f"  single hold-out (30 points): MSE = {hold_mse:.4f}")
    print(f"  5-fold cross-validation    : MSE = {np.mean(cv):.4f} "
          f"+/- {np.std(cv, ddof=1):.4f} (fold sd)")
    print(f"  fold MSEs: " + ", ".join(f"{v:.4f}" for v in cv))
    print("  the single hold-out depends on which 30 points were withheld; the")
    print("  k-fold estimate averages that choice and reports its spread.")

    section("2. Classification metrics")
    n = 500
    x1 = RNG.standard_normal(n)
    score = 1.6 * x1 + RNG.standard_normal(n)
    label = (score > 0.8).astype(int)
    pred = (score > 1.0).astype(int)
    tp = int(np.sum((pred == 1) & (label == 1)))
    fp = int(np.sum((pred == 1) & (label == 0)))
    fn = int(np.sum((pred == 0) & (label == 1)))
    tn = int(np.sum((pred == 0) & (label == 0)))
    acc = (tp + tn) / n
    prec = tp / max(tp + fp, 1)
    rec = tp / max(tp + fn, 1)
    order = np.argsort(score)
    ranks = np.empty(n)
    ranks[order] = np.arange(1, n + 1)
    pos = label == 1
    auc = (ranks[pos].sum() - pos.sum() * (pos.sum() + 1) / 2.0) / (
        pos.sum() * (~pos).sum())
    print(f"  confusion matrix: TP = {tp}, FP = {fp}, FN = {fn}, TN = {tn}")
    print(f"  accuracy  = {acc:.4f}   precision = {prec:.4f}   "
          f"recall = {rec:.4f}")
    print(f"  base rate (positive fraction) = {label.mean():.4f}")
    print(f"  ROC AUC = {auc:.4f}")
    print("  accuracy alone is misleading when the classes are imbalanced; the")
    print("  base rate and the AUC are needed to interpret it.")

    section("3. Leakage: selecting features on the full data")
    n, p = 80, 200
    Xn = RNG.standard_normal((n, p))          # pure noise, no signal at all
    yn = RNG.standard_normal(n)
    corr = np.array([abs(np.corrcoef(Xn[:, j], yn)[0, 1]) for j in range(p)])
    top = np.argsort(-corr)[:5]
    honest = 0.0
    for _ in range(200):
        perm = RNG.permutation(n)
        tr, va = perm[:60], perm[60:]
        # selection inside the training fold only
        c = np.array([abs(np.corrcoef(Xn[tr, j], yn[tr])[0, 1]) for j in range(p)])
        sel = np.argsort(-c)[:5]
        b = np.linalg.lstsq(Xn[tr][:, sel], yn[tr], rcond=None)[0]
        pred = Xn[va][:, sel] @ b
        honest += float(np.mean((pred - yn[va]) ** 2))
    honest /= 200
    leaked = 0.0
    for _ in range(200):
        perm = RNG.permutation(n)
        tr, va = perm[:60], perm[60:]
        b = np.linalg.lstsq(Xn[tr][:, top], yn[tr], rcond=None)[0]
        pred = Xn[va][:, top] @ b
        leaked += float(np.mean((pred - yn[va]) ** 2))
    leaked /= 200
    print(f"  data are pure noise (no signal): the honest MSE should be about 1.")
    print(f"  selection inside the fold only : MSE = {honest:.4f}")
    print(f"  selection on the full data     : MSE = {leaked:.4f}")
    print(f"  the leaked pipeline looks better by "
          f"{100 * (honest - leaked) / honest:.1f} % on data with no signal at all.")
    print("  the leak is that the feature ranking used the validation points; a")
    print("  pipeline must be contained entirely inside each fold.")


if __name__ == "__main__":
    main()
