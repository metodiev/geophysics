#!/usr/bin/env python3
"""Recurrent networks on SYNTHETIC data: a hand-written RNN trained by
backpropagation through time, the vanishing-gradient measurement as a function of
sequence length, and a comparison with a gated recurrence.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rnns_time_series_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. An RNN trained by backpropagation through time.
2. Vanishing gradients: the gradient of a long-range dependence.
3. A gated recurrence and why it helps.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    print("SYNTHETIC sequences generated below; no measured value is used.")

    section("1. An RNN trained by backpropagation through time")
    T, n_seq = 20, 200
    X = RNG.standard_normal((n_seq, T, 1))
    # target: the running mean of the sequence up to each step
    Y = np.cumsum(X[:, :, 0], axis=1) / np.arange(1, T + 1)
    h_dim = 8
    Wx = 0.3 * RNG.standard_normal((1, h_dim))
    Wh = 0.3 * RNG.standard_normal((h_dim, h_dim))
    Wy = 0.3 * RNG.standard_normal(h_dim)
    lr = 0.01
    losses = []
    for epoch in range(120):
        gWx = np.zeros_like(Wx); gWh = np.zeros_like(Wh); gWy = np.zeros_like(Wy)
        tot = 0.0
        for s in range(n_seq):
            h = np.zeros(h_dim)
            hs = [h]
            ys = []
            for t in range(T):
                h = np.tanh(X[s, t] @ Wx + h @ Wh)
                hs.append(h)
                ys.append(float(h @ Wy))
            ys = np.array(ys)
            err = ys - Y[s]
            tot += float(np.mean(err ** 2))
            dh_next = np.zeros(h_dim)
            for t in range(T - 1, -1, -1):
                dy = 2 * err[t] / T
                gWy += hs[t + 1] * dy
                dh = dy * Wy + dh_next
                dpre = dh * (1 - hs[t + 1] ** 2)
                gWx += X[s, t][:, None] * dpre
                gWh += hs[t][:, None] * dpre
                dh_next = dpre @ Wh.T
        Wx -= lr * gWx / n_seq
        Wh -= lr * gWh / n_seq
        Wy -= lr * gWy / n_seq
        losses.append(tot / n_seq)
    print(f"  task: predict the running mean of a random sequence, T = {T}, "
          f"{n_seq} sequences")
    print(f"  hidden dimension = {h_dim}, {len(losses)} epochs of full-batch BPTT")
    print(f"  MSE after 1 epoch   = {losses[0]:.5f}")
    print(f"  MSE after 20 epochs = {losses[19]:.5f}")
    print(f"  MSE after 120 epochs= {losses[-1]:.5f}")
    print(f"  variance of the target = {float(Y.var()):.5f}")
    print("  BPTT is ordinary backpropagation unrolled over time; the gradient at")
    print("  an early step is a product of one Jacobian per intervening step.")

    section("2. Vanishing gradients")
    print("  gradient norm at step 1 of a dependence at step T, for a linear")
    print("  recurrence with spectral radius rho:")
    for rho in (0.5, 0.9, 1.0, 1.1):
        print(f"    rho = {rho:4.2f}:  " + "  ".join(
            f"T={T}: {rho ** T:.2e}" for T in (5, 10, 20, 40)))
    print(f"  with rho = 0.9 the gradient after only 20 steps is "
          f"{0.9 ** 20:.2e} of its initial value, and after 40 it is "
          f"{0.9 ** 40:.2e}: the dependence is present in the data and")
    print("  invisible to the optimiser.")
    print(f"  with rho = 1.1 it explodes to {1.1 ** 40:.2e} at T = 40 instead.")
    print("  a plain RNN therefore has a narrow window: neither growth nor decay")
    print("  is acceptable, and no fixed choice of weights gives both.")

    section("3. A gated recurrence")
    rng = np.random.default_rng(7)
    Whh = 0.9 * np.eye(4) + 0.02 * rng.standard_normal((4, 4))
    Wf = np.array([4.0, -3.0, 2.0, -1.0])
    bias = -2.0
    def forget_gate(x):
        return 1.0 / (1.0 + np.exp(-(x @ Wf + bias)))
    x_low = np.array([0.5, -0.2, 0.1, 0.3])
    x_high = np.array([1.5, 0.5, 1.5, 0.0])
    print(f"  plain recurrence: coefficient after 40 steps = {0.9 ** 40:.3e}")
    for name, x_in in (("forget gate closed", x_low),
                       ("forget gate open", x_high)):
        f = float(forget_gate(x_in))
        print(f"  {name:20s}: gate g = {f:.4f}, coefficient after 40 steps = "
              f"{f ** 40:.3e}")
    print("  the gate can be driven to 1 by the input, so the same layer can")
    print("  either discard a dependence or carry it for forty steps: the decay")
    print("  is a learned, input-dependent quantity rather than a fixed product")
    print("  of weights. That is the whole idea of an LSTM or GRU.")


if __name__ == "__main__":
    main()
