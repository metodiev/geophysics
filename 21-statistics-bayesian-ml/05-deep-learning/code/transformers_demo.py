#!/usr/bin/env python3
"""Attention and transformers on SYNTHETIC data: scaled dot-product attention
computed directly, the causal mask, positional encoding, attention entropy, and
the parameter and compute scaling against a recurrent layer.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python transformers_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. Scaled dot-product attention, with and without a causal mask.
2. Positional encoding and attention entropy.
3. Parameter and compute scaling against a recurrent layer.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def softmax(x, axis=-1):
    x = x - x.max(axis=axis, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis=axis, keepdims=True)


def attention(Q, K, V, mask=None):
    scores = Q @ K.T / np.sqrt(Q.shape[1])
    if mask is not None:
        scores = np.where(mask, scores, -1e9)
    A = softmax(scores, axis=-1)
    return A, A @ V


def main():
    print("SYNTHETIC tensors generated below; no measured value is used.")

    section("1. Scaled dot-product attention")
    T, d = 6, 4
    Q = RNG.standard_normal((T, d))
    K = RNG.standard_normal((T, d))
    V = RNG.standard_normal((T, d))
    A, out = attention(Q, K, V)
    print(f"  sequence length {T}, key/query dimension {d}")
    print("  attention weight matrix (rows sum to 1):")
    for row in A:
        print("   " + " ".join(f"{v:.3f}" for v in row) + f"   sum = {row.sum():.6f}")
    print(f"  output shape {out.shape}; every output is a convex combination of")
    print("  the values, so it lies inside their convex hull.")
    causal = np.tril(np.ones((T, T), dtype=bool))
    Ac, outc = attention(Q, K, V, mask=causal)
    print("  with a causal mask the upper triangle is zero:")
    for row in Ac:
        print("   " + " ".join(f"{v:.3f}" for v in row) + f"   sum = {row.sum():.6f}")
    print("  masking makes the layer autoregressive: token t can attend only to")
    print("  tokens up to t, which is what a forecasting model requires.")

    section("2. Positional encoding and attention entropy")
    positions = np.arange(T)[:, None]
    dims = np.arange(0, d, 2)[None, :]
    pe = np.zeros((T, d))
    pe[:, 0::2] = np.sin(positions / 10000 ** (dims / d))
    pe[:, 1::2] = np.cos(positions / 10000 ** (dims / d))
    print("  sinusoidal positional encoding, first four rows:")
    for row in pe[:4]:
        print("   " + " ".join(f"{v:+.3f}" for v in row))
    print(f"  the encoding is deterministic and unbounded in position, so the")
    print(f"  model can address a position it has never seen.")
    ent = -np.sum(A * np.log(A + 1e-12), axis=1)
    print(f"  attention entropy per row: "
          + ", ".join(f"{v:.3f}" for v in ent))
    print(f"  maximum possible entropy with {T} keys = {np.log(T):.3f} nats")
    print("  entropy near the maximum means the row is nearly uniform, i.e. the")
    print("  layer is averaging rather than selecting; a low entropy means it")
    print("  has concentrated on one or two keys.")

    section("3. Parameter and compute scaling")
    d_model = 64
    for T in (8, 32, 128, 512):
        attn_params = 4 * d_model * d_model
        rnn_params = 2 * d_model * d_model
        attn_ops = T * T * d_model
        rnn_ops = T * d_model * d_model
        print(f"  T = {T:4d}: attention parameters = {attn_params}, "
              f"RNN parameters = {rnn_params}, "
              f"attention score ops = {attn_ops:,}, RNN ops = {rnn_ops:,}")
    print("  attention has more parameters than a simple recurrent layer but its")
    print("  cost is quadratic in the sequence length while the recurrence is")
    print("  linear; the crossover is what limits attention on long records.")


if __name__ == "__main__":
    main()
