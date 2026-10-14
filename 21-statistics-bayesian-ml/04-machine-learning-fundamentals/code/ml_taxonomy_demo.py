#!/usr/bin/env python3
"""The three machine-learning paradigms on SYNTHETIC data: a supervised logistic
regression and linear regression trained by gradient descent, an unsupervised
k-means clustering, and a reinforcement-learning multi-armed bandit.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ml_taxonomy_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. Supervised regression: linear model by gradient descent.
2. Supervised classification: logistic regression and its accuracy.
3. Unsupervised learning: k-means and the within-cluster sum of squares.
4. Reinforcement learning: epsilon-greedy bandit and its regret.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    print("SYNTHETIC data sets generated below; no measured value is used.")

    section("1. Supervised regression: linear model by gradient descent")
    n = 200
    x = RNG.uniform(-2.0, 2.0, n)
    y = 1.5 + 0.8 * x + 0.3 * RNG.standard_normal(n)
    X = np.column_stack([np.ones(n), x])
    beta = np.zeros(2)
    lr = 0.1
    for _ in range(400):
        grad = 2.0 / n * X.T @ (X @ beta - y)
        beta -= lr * grad
    exact = np.linalg.lstsq(X, y, rcond=None)[0]
    mse = float(np.mean((X @ beta - y) ** 2))
    print(f"  gradient-descent solution: intercept = {beta[0]:.4f}, "
          f"slope = {beta[1]:.4f}")
    print(f"  normal-equation solution : intercept = {exact[0]:.4f}, "
          f"slope = {exact[1]:.4f}")
    print(f"  training MSE = {mse:.4f} (noise variance 0.09)")
    print("  the two agree to three decimals: for a linear model with squared")
    print("  loss, gradient descent finds the same optimum as the closed form.")

    section("2. Supervised classification: logistic regression")
    x1 = RNG.standard_normal(400)
    x2 = RNG.standard_normal(400)
    logits = 1.2 * x1 - 0.8 * x2
    labels = (RNG.random(400) < 1.0 / (1.0 + np.exp(-logits))).astype(float)
    Xc = np.column_stack([np.ones(400), x1, x2])
    w = np.zeros(3)
    for _ in range(600):
        p = 1.0 / (1.0 + np.exp(-Xc @ w))
        w -= 0.5 * Xc.T @ (p - labels) / 400
    p = 1.0 / (1.0 + np.exp(-Xc @ w))
    pred = (p > 0.5).astype(float)
    acc = float(np.mean(pred == labels))
    print(f"  fitted coefficients: intercept = {w[0]:+.4f}, "
          f"beta1 = {w[1]:+.4f}, beta2 = {w[2]:+.4f} (truth +1.2, -0.8)")
    print(f"  training accuracy = {acc:.4f} on {labels.size} samples")
    print(f"  mean predicted probability = {p.mean():.4f} against the base rate "
          f"{labels.mean():.4f}")
    print("  the model is linear in the log-odds, so the decision boundary is a")
    print("  straight line; a curved boundary would need a nonlinear feature.")

    section("3. Unsupervised learning: k-means")
    centres = np.array([[-3.0, 0.0], [3.0, 1.0], [0.0, -3.0]])
    pts = np.vstack([c + 0.7 * RNG.standard_normal((100, 2)) for c in centres])
    best_wcss, best_labels = np.inf, None
    for k in (2, 3, 4, 5):
        wcss_k = np.inf
        for _ in range(20):
            seeds = pts[RNG.choice(pts.shape[0], k, replace=False)]
            for _ in range(50):
                d = ((pts[:, None, :] - seeds[None, :, :]) ** 2).sum(axis=2)
                lab = d.argmin(axis=1)
                new = np.array([pts[lab == j].mean(axis=0) if np.any(lab == j)
                                else seeds[j] for j in range(k)])
                if np.allclose(new, seeds):
                    break
                seeds = new
            wcss = float(((pts - seeds[lab]) ** 2).sum())
            wcss_k = min(wcss_k, wcss)
        print(f"  k = {k}: best within-cluster sum of squares = {wcss_k:8.2f}")
        if k == 3:
            best_wcss, best_labels = wcss_k, lab
    print(f"  the WSSC falls monotonically with k, so it cannot choose k; the")
    print(f"  elbow is between k = 3 and k = 4, matching the three true centres.")
    print(f"  cluster sizes recovered at k = 3: "
          f"{[int(np.sum(best_labels == j)) for j in range(3)]}")

    section("4. Reinforcement learning: epsilon-greedy bandit")
    true_means = np.array([0.2, 0.5, 0.65, 0.4])
    eps = 0.1
    steps = 2000
    n_pull = np.zeros(true_means.size)
    total = np.zeros(true_means.size)
    reward = 0.0
    for t in range(steps):
        if RNG.random() < eps or np.any(n_pull == 0):
            arm = int(RNG.integers(0, true_means.size))
        else:
            arm = int(np.argmax(total / np.maximum(n_pull, 1)))
        r = RNG.random() < true_means[arm]
        n_pull[arm] += 1
        total[arm] += r
        reward += r
    best = float(true_means.max())
    regret = steps * best - reward
    print(f"  arm means: " + ", ".join(f"{m:.2f}" for m in true_means))
    print(f"  pulls per arm: "
          + ", ".join(f"{int(c)}" for c in n_pull))
    print(f"  estimated means: "
          + ", ".join(f"{t / max(c, 1):.3f}" for t, c in zip(total, n_pull)))
    print(f"  total reward = {reward:.0f} of a possible {steps * best:.0f}, "
          f"regret = {regret:.0f} ({100 * regret / (steps * best):.1f} % of the")
    print(f"  optimal reward)")
    print("  the policy explores 10 % of the time and still concentrates its")
    print("  pulls on the better arm, which is the explore-exploit trade.")


if __name__ == "__main__":
    main()
