#!/usr/bin/env python3
"""Self-supervised learning on SYNTHETIC data: masked reconstruction as a
pretext task, a contrastive InfoNCE loss on positive and negative pairs, and a
linear probe that measures the quality of the learned representation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python self_supervised_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. Masked reconstruction: predicting held-out entries from the rest.
2. Contrastive learning with the InfoNCE loss.
3. A linear probe on frozen features.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    print("SYNTHETIC data generated below; no measured value is used.")

    section("1. Masked reconstruction")
    n_feat, n_samp, mask_frac = 20, 400, 0.2
    W = RNG.standard_normal((6, n_feat))          # a low-rank generator
    Z = RNG.standard_normal((n_samp, 6))
    X = Z @ W + 0.3 * RNG.standard_normal((n_samp, n_feat))
    n_train = n_samp // 2
    train, test = X[:n_train], X[n_train:]
    mu = train.mean(axis=0)
    # pretext step: for each feature, a ridge predictor from the other features
    coefs = []
    lam = 1e-2
    for j in range(n_feat):
        obs = [k for k in range(n_feat) if k != j]
        A = train[:, obs]
        y = train[:, j] - mu[j]
        beta = np.linalg.solve(A.T @ A + lam * np.eye(len(obs)), A.T @ y)
        coefs.append((obs, beta))
    err_model, err_base = [], []
    for _ in range(30):
        for i in range(test.shape[0]):
            idx = RNG.choice(n_feat, int(mask_frac * n_feat), replace=False)
            masked = set(idx.tolist())
            base = 0.0
            model = 0.0
            for j in idx:
                base += (test[i, j] - mu[j]) ** 2
                obs, beta = coefs[j]
                xv = np.array([test[i, k] if k not in masked else mu[k]
                               for k in obs])
                model += (test[i, j] - (mu[j] + float(xv @ beta))) ** 2
            err_base.append(base / idx.size)
            err_model.append(model / idx.size)
    base = float(np.mean(err_base))
    model = float(np.mean(err_model))
    print(f"  data: {n_samp} samples, {n_feat} features, rank 6 plus noise")
    print(f"  masked fraction = {mask_frac:.0%}; {n_train} samples used for the")
    print("  pretext predictors, the rest for evaluation")
    print(f"  predicting a masked entry by the feature mean: MSE = {base:.5f}")
    print(f"  predicting it from the observed entries (ridge): MSE = {model:.5f}")
    print(f"  reduction = {100 * (1 - model / base):.1f} %")
    print("  masked modelling is self-supervised: the target for the masked")
    print("  entries is supplied by the data itself, so no labels are needed.")

    section("2. Contrastive learning with InfoNCE")
    d = 8
    anchor = RNG.standard_normal((200, d))
    positive = anchor + 0.3 * RNG.standard_normal((200, d))
    def cos(a, b):
        return (a * b).sum(axis=1) / (np.linalg.norm(a, axis=1)
                                      * np.linalg.norm(b, axis=1))
    sim_p = cos(anchor, positive)
    print("  negative difficulty: how far the negatives are from the anchor")
    print("  negative scale   InfoNCE loss   positive ranked first")
    for scale in (2.0, 1.0, 0.5, 0.3, 0.25):
        negative = anchor + scale * RNG.standard_normal((200, d))
        logits = np.concatenate([sim_p[:, None], cos(anchor, negative)[:, None]],
                                axis=1)
        ex = np.exp(logits - logits.max(axis=1, keepdims=True))
        p = ex / ex.sum(axis=1, keepdims=True)
        loss = float(-np.mean(np.log(p[:, 0] + 1e-12)))
        acc = float(np.mean(p[:, 0] > 0.5))
        print(f"  {scale:12.2f}   {loss:12.5f}   {acc:20.3f}")
    print(f"  the loss equals ln 2 = {np.log(2):.5f} when the positive and the")
    print("  negative are indistinguishable, and it exceeds ln 2 whenever the")
    print("  positive is ranked below the negative.  As the negatives approach")
    print("  the anchor the loss rises towards that value, which is what makes")
    print("  hard negatives valuable in training a representation.")

    section("3. A linear probe on frozen features")
    n = 600
    latent = RNG.standard_normal((n, 2))
    labels = (latent[:, 0] + 0.5 * latent[:, 1] > 0).astype(float)
    raw = latent @ np.array([[1.0, 0.9, 0.0, 0.0], [0.0, 0.0, 1.0, 0.9]])
    raw = raw + 0.2 * RNG.standard_normal((n, 4))
    P = RNG.standard_normal((4, 6))
    frozen = np.tanh(raw @ P)                  # a fixed, "pretrained" encoder

    def sigm(z):
        z = np.clip(z, -30.0, 30.0)
        return 1.0 / (1.0 + np.exp(-z))

    def probe(F, idx, te):
        Xd = np.column_stack([np.ones(idx.size), F[idx]])
        w = np.zeros(Xd.shape[1])
        for _ in range(600):
            p = sigm(Xd @ w)
            w -= 0.1 * (Xd.T @ (p - labels[idx]) / idx.size
                        + 1e-2 * np.r_[0.0, w[1:]])
        Xt = np.column_stack([np.ones(te.size), F[te]])
        p = sigm(Xt @ w)
        return float(np.mean((p > 0.5) == labels[te]))

    te = RNG.choice(n, 150, replace=False)
    pool = np.setdiff1d(np.arange(n), te)
    for n_lab in (450, 40, 12):
        idx = RNG.choice(pool, n_lab, replace=False)
        print(f"  {n_lab:4d} labelled samples: raw features "
              f"{probe(raw, idx, te):.4f}, frozen features "
              f"{probe(frozen, idx, te):.4f}")
    print("  the probe is trained with the labels but the features are fixed, so")
    print("  it measures how much of the label the representation already")
    print("  carries. The two columns are close when labels are plentiful; the")
    print("  interesting regime is the few-label regime, where a good")
    print("  representation is worth most.")


if __name__ == "__main__":
    main()
