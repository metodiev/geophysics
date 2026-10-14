#!/usr/bin/env python3
"""Feature engineering on SYNTHETIC data: the effect of feature scaling on a
distance-based learner, the effect of constructing an interaction feature on a
linear one, and a target-leakage feature that survives a random split.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python feature_engineering_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. Scaling: a k-nearest-neighbour classifier with and without standardisation.
2. Feature construction: making an XOR problem linearly separable.
3. Leakage: a feature derived from the target.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def knn_predict(Xtr, ytr, Xte, k):
    d = ((Xte[:, None, :] - Xtr[None, :, :]) ** 2).sum(axis=2)
    idx = np.argsort(d, axis=1)[:, :k]
    return (ytr[idx].mean(axis=1) > 0.5).astype(float)


def main():
    print("SYNTHETIC data generated below; no measured value is used.")

    section("1. Scaling and a distance-based learner")
    n = 300
    informative = RNG.standard_normal(n)          # scale 1
    nuisance = RNG.standard_normal(n) * 500.0     # scale 500
    label = (informative + 0.5 * RNG.standard_normal(n) > 0).astype(float)
    X = np.column_stack([informative, nuisance])
    Xtr, ytr, Xte, yte = X[:150], label[:150], X[150:], label[150:]
    for name, A, B in (("raw", Xtr, Xte),
                       ("standardised",
                        (Xtr - Xtr.mean(0)) / Xtr.std(0),
                        (Xte - Xtr.mean(0)) / Xtr.std(0))):
        acc = float(np.mean(knn_predict(A, ytr, B, 5) == yte))
        print(f"  {name:13s} 5-NN accuracy = {acc:.4f}")
    print("  the nuisance feature has 500 times the scale of the informative")
    print("  one, so in the raw space the Euclidean distance is dominated by")
    print("  noise; standardising to unit variance restores the signal.")

    section("2. Feature construction and linear separability")
    x1 = RNG.uniform(-2.0, 2.0, n)
    x2 = RNG.uniform(-2.0, 2.0, n)
    yxor = ((x1 > 0) ^ (x2 > 0)).astype(float)
    def logit_fit_acc(Xf, yf, Xv, yv):
        Xd = np.column_stack([np.ones(len(Xf)), Xf])
        w = np.zeros(Xd.shape[1])
        for _ in range(3000):
            p = 1.0 / (1.0 + np.exp(-Xd @ w))
            w -= 0.5 * Xd.T @ (p - yf) / len(yf)
        Xv2 = np.column_stack([np.ones(len(Xv)), Xv])
        pv = 1.0 / (1.0 + np.exp(-Xv2 @ w))
        return float(np.mean((pv > 0.5) == yv))
    base = logit_fit_acc(np.column_stack([x1[:150], x2[:150]]), yxor[:150],
                         np.column_stack([x1[150:], x2[150:]]), yxor[150:])
    prod = logit_fit_acc(np.column_stack([x1[:150], x2[:150],
                                          x1[:150] * x2[:150]]), yxor[:150],
                         np.column_stack([x1[150:], x2[150:],
                                          x1[150:] * x2[150:]]), yxor[150:])
    print(f"  logistic regression on (x1, x2)          accuracy = {base:.4f}")
    print(f"  logistic regression on (x1, x2, x1*x2)   accuracy = {prod:.4f}")
    print("  the XOR target is not linearly separable in the original features;")
    print("  the product feature makes it separable, and the model is unchanged.")

    section("3. Leakage: a feature derived from the target")
    m = 200
    Xs = RNG.standard_normal((m, 2))
    ys = (Xs[:, 0] + 0.8 * RNG.standard_normal(m) > 0).astype(float)
    leaked_feature = ys + 0.05 * RNG.standard_normal(m)     # a leak
    Xleak = np.column_stack([Xs, leaked_feature])
    perm = RNG.permutation(m)
    tr, te = perm[:140], perm[140:]

    def acc_with(feats):
        Xd = np.column_stack([np.ones(len(tr)), feats[tr]])
        w = np.zeros(Xd.shape[1])
        for _ in range(2000):
            p = 1.0 / (1.0 + np.exp(-Xd @ w))
            w -= 0.5 * Xd.T @ (p - ys[tr]) / len(tr)
        Xv = np.column_stack([np.ones(len(te)), feats[te]])
        pv = 1.0 / (1.0 + np.exp(-Xv @ w))
        return float(np.mean((pv > 0.5) == ys[te]))

    honest = acc_with(Xs)
    leaked = acc_with(Xleak)
    print(f"  honest features (2)      hold-out accuracy = {honest:.4f}")
    print(f"  with the leaked feature  hold-out accuracy = {leaked:.4f}")
    print(f"  the correlation of the leaked feature with the target is "
          f"{np.corrcoef(leaked_feature, ys)[0, 1]:.4f}")
    print("  the leak survives a random split because the feature carries the")
    print("  target for the test points too; holding out is not enough, the")
    print("  feature must not exist. In a real pipeline a leak of this kind")
    print("  arises whenever a variable measured after the outcome is included.")


if __name__ == "__main__":
    main()
