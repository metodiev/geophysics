#!/usr/bin/env python3
"""Neural networks from scratch on SYNTHETIC data: a two-layer network trained
on XOR, a regression network, and a numerical gradient check that verifies the
backpropagation implementation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python neural_networks_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. XOR: why one layer cannot and two can.
2. Backpropagation verified by finite differences.
3. Hidden-activation comparison on a smooth regression target.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def forward(W1, b1, W2, b2, X, act):
    Z1 = X @ W1 + b1
    H = act(Z1)
    Z2 = H @ W2 + b2
    return Z1, H, Z2, sigmoid(Z2)


def backward(W1, b1, W2, b2, X, Y, act, dact):
    Z1, H, Z2, Yh = forward(W1, b1, W2, b2, X, act)
    n = X.shape[0]
    dZ2 = (Yh - Y) / n
    gW2 = H.T @ dZ2
    gb2 = dZ2.sum(axis=0)
    dH = dZ2 @ W2.T
    dZ1 = dH * dact(Z1)
    gW1 = X.T @ dZ1
    gb1 = dZ1.sum(axis=0)
    loss = -float(np.mean(Y * np.log(Yh + 1e-12)
                          + (1 - Y) * np.log(1 - Yh + 1e-12)))
    return gW1, gb1, gW2, gb2, loss


def main():
    print("SYNTHETIC data generated below; no measured value is used.")
    tanh, dtanh = np.tanh, lambda z: 1.0 - np.tanh(z) ** 2

    section("1. XOR: why one layer cannot and two can")
    X = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
    Y = np.array([[0.0], [1.0], [1.0], [0.0]])
    def train(hidden, iters=8000, lr=1.0):
        W1 = 0.8 * RNG.standard_normal((2, hidden))
        b1 = np.zeros(hidden)
        W2 = 0.8 * RNG.standard_normal((hidden, 1))
        b2 = np.zeros(1)
        for _ in range(iters):
            gW1, gb1, gW2, gb2, loss = backward(W1, b1, W2, b2, X, Y, tanh, dtanh)
            W1 -= lr * gW1; b1 -= lr * gb1; W2 -= lr * gW2; b2 -= lr * gb2
        return loss, forward(W1, b1, W2, b2, X, tanh)[3].ravel()
    for hidden in (0, 2, 4):
        if hidden == 0:
            # logistic regression: a linear model on the raw features
            w = np.zeros(2); b = 0.0
            for _ in range(8000):
                p = sigmoid(X @ w + b).ravel()
                grad = X.T @ (p - Y.ravel()) / 4.0
                w -= grad; b -= float(np.mean(p - Y.ravel()))
            p = sigmoid(X @ w + b)
            loss = -float(np.mean(Y.ravel() * np.log(p + 1e-12)
                                  + (1 - Y.ravel()) * np.log(1 - p + 1e-12)))
            print(f"  no hidden layer (logistic): loss = {loss:.4f}, "
                  f"predictions = "
                  f"{', '.join(f'{v:.3f}' for v in p)}")
        else:
            loss, pred = train(hidden)
            print(f"  {hidden} hidden units: loss = {loss:.4f}, predictions = "
                  f"{', '.join(f'{v:.3f}' for v in pred)}")
    print("  target is 0 1 1 0. A linear model cannot do better than 0.5 "
          "everywhere;")
    print("  two hidden units give it the two half-space features the XOR needs.")

    section("2. Backpropagation verified by finite differences")
    W1 = 0.5 * RNG.standard_normal((2, 3))
    b1 = 0.1 * RNG.standard_normal(3)
    W2 = 0.5 * RNG.standard_normal((3, 1))
    b2 = np.zeros(1)
    gW1, _, gW2, _, _ = backward(W1, b1, W2, b2, X, Y, tanh, dtanh)
    eps = 1e-6
    num = np.zeros_like(W1)
    for i in range(W1.shape[0]):
        for j in range(W1.shape[1]):
            Wp = W1.copy(); Wp[i, j] += eps
            Wm = W1.copy(); Wm[i, j] -= eps
            lp = backward(Wp, b1, W2, b2, X, Y, tanh, dtanh)[4]
            lm = backward(Wm, b1, W2, b2, X, Y, tanh, dtanh)[4]
            num[i, j] = (lp - lm) / (2 * eps)
    print(f"  analytic dW1[0,0]  = {gW1[0, 0]:+.8f}")
    print(f"  numerical dW1[0,0] = {num[0, 0]:+.8f}")
    print(f"  maximum absolute difference over all entries = "
          f"{np.max(np.abs(num - gW1)):.2e}")
    print("  a finite-difference check is the only cheap way to confirm that a")
    print("  backpropagation implementation is correct; agreement to 1e-7 or")
    print("  better is the expected result at this epsilon.")

    section("3. Hidden-activation comparison on a smooth target")
    xr = RNG.uniform(-3.0, 3.0, 300)
    yr = (np.sin(xr) + 0.3 * xr)[:, None]
    Xr = xr[:, None]
    activations = (("tanh", np.tanh, dtanh),
                   ("relu", lambda z: np.maximum(z, 0.0),
                    lambda z: (z > 0).astype(float)))
    for name, act, dact in activations:
        W1 = 0.5 * RNG.standard_normal((1, 20))
        b1 = np.zeros(20)
        W2 = 0.5 * RNG.standard_normal((20, 1))
        b2 = np.zeros(1)
        for _ in range(4000):
            Z1 = Xr @ W1 + b1
            H = act(Z1)
            Yh = H @ W2 + b2
            dZ2 = (Yh - yr) / Xr.shape[0]
            gW2 = H.T @ dZ2; gb2 = dZ2.sum(axis=0)
            dH = dZ2 @ W2.T
            dZ1 = dH * dact(Z1)
            W1 -= 0.1 * (Xr.T @ dZ1); b1 -= 0.1 * dZ1.sum(axis=0)
            W2 -= 0.1 * gW2; b2 -= 0.1 * gb2
        mse = float(np.mean((H @ W2 + b2 - yr) ** 2))
        print(f"  hidden activation {name:5s}: final training MSE = {mse:.5f}")
    print("  both reach the same order: with a smooth target and enough hidden")
    print("  units the activation choice is a detail. It matters for the")
    print("  gradient, not for the representable function class.")


if __name__ == "__main__":
    main()
