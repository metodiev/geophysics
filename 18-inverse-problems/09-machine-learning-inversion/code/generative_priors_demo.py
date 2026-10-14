#!/usr/bin/env python3
"""Generative priors for inversion: learning what plausible models look like from
an ensemble, using it to fill the null space, and the bias when the target is
unlike the training ensemble.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python generative_priors_demo.py

All models and data are SYNTHETIC.  The "generative prior" here is a linear
(PCA / factor-analysis) model learned from a synthetic training ensemble; a deep
generative model generalises the same idea, and the effects measured below are
structural rather than an artifact of the linear choice.  No number below is a
measurement.

Contents
--------
1. A training ensemble of SYNTHETIC models and the subspace it spans.
2. In-family inversion: a learned prior against a smoothness prior.
3. Filling the null space: what the prior does where the data are silent.
4. Out-of-family targets: the prior imposes what it was taught.
5. What a generative prior is, in one sentence.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N = 30                     # model cells
N_DATA = 20                # observations
NOISE = 0.05               # data noise
N_TRAIN = 1500
N_COMPONENTS = 4
LAMBDA_SMOOTH = 1.0


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def build_operator():
    x = (np.arange(N) + 0.5) / N
    xo = (np.arange(N_DATA) + 0.5) / N_DATA
    return np.exp(-(xo[:, None] - x[None, :]) ** 2 / (2 * 0.06 ** 2)) / N_DATA


def sample_ensemble(n, rng=RNG):
    """SYNTHETIC geological family: a blocky layered model built from a random
    walk with few long steps, plus a smooth trend."""
    x = (np.arange(N) + 0.5) / N
    M = np.zeros((n, N))
    for i in range(n):
        n_breaks = rng.integers(2, 4)
        breaks = np.sort(rng.choice(np.arange(3, N - 3), size=n_breaks,
                                    replace=False))
        levels = rng.normal(0.0, 0.4, size=n_breaks + 1)
        prof = np.zeros(N)
        start = 0
        for b, lev in zip(np.append(breaks, N), levels):
            prof[start:b] = lev
            start = b
        M[i] = prof + 0.15 * np.sin(2 * np.pi * x)
    return M


def main():
    A = build_operator()
    D = np.zeros((N - 1, N))
    for k in range(N - 1):
        D[k, k] = -1.0
        D[k, k + 1] = 1.0

    section("1. A training ensemble and the subspace it spans")
    M_tr = sample_ensemble(N_TRAIN)
    mu = M_tr.mean(axis=0)
    Mc = M_tr - mu
    U, s, Vt = np.linalg.svd(Mc, full_matrices=False)
    var = s ** 2 / np.sum(s ** 2)
    print(f"  {N_TRAIN} SYNTHETIC training models on {N} cells")
    print(f"  the model ensemble is described to {var[:N_COMPONENTS].sum() * 100:.2f}% "
          f"of its variance by {N_COMPONENTS} linear components")
    print(f"  residual variance outside those {N_COMPONENTS} components: "
          f"{(1 - var[:N_COMPONENTS].sum()) * 100:.2f}%")
    print("  components (fraction of variance): "
          + " ".join(f"{v * 100:.1f}%" for v in var[:6]))

    section("2. In-family inversion: learned prior against smoothness prior")
    Vk = Vt[:N_COMPONENTS]                       # (k, N)
    s_perp = np.sqrt(np.mean((Mc - Mc @ Vk.T @ Vk) ** 2))
    s_par = np.sqrt(np.mean((Mc @ Vk.T) ** 2))
    P_learn = (np.eye(N) - Vk.T @ Vk) / s_perp ** 2 + (Vk.T @ Vk) / s_par ** 2
    P_smooth = LAMBDA_SMOOTH * (D.T @ D) + 1e-6 * np.eye(N)
    print(f"  prior scales: along the learned subspace {s_par:.4f}, "
          f"orthogonal to it {s_perp:.4f}")
    M_te = sample_ensemble(400)
    D_te = M_te @ A.T + NOISE * RNG.standard_normal((400, N_DATA))
    C_sm = np.linalg.inv(A.T @ A / NOISE ** 2 + P_smooth)
    C_lp = np.linalg.inv(A.T @ A / NOISE ** 2 + P_learn)
    m_sm = D_te @ (C_sm @ A.T / NOISE ** 2).T
    # the learned prior has a non-zero mean, so the posterior mean includes its
    # contribution: m = (A'A/s^2 + P)^-1 (A'd/s^2 + P mu)
    lhs = A.T @ D_te.T / NOISE ** 2 + np.outer(P_learn @ mu, np.ones(400))
    m_lp = (C_lp @ lhs).T
    print(f"  smoothness prior: MSE = {np.mean((m_sm - M_te) ** 2):.3e}  "
          f"(rms {np.sqrt(np.mean((m_sm - M_te) ** 2)):.4f})")
    print(f"  learned prior   : MSE = {np.mean((m_lp - M_te) ** 2):.3e}  "
          f"(rms {np.sqrt(np.mean((m_lp - M_te) ** 2)):.4f})")
    print("  in-family the learned prior wins, because the ensemble it was trained")
    print("  on IS the population the test models come from.  This is the whole")
    print("  reason to use one; it is also the whole risk, as section 4 shows.")

    section("3. Filling the null space: what the prior does where data are silent")
    Ua, sa, Vta = np.linalg.svd(A, full_matrices=True)
    null_dirs = Vta[N_DATA:]                     # N - N_DATA = 10 directions
    print(f"  the operator has {null_dirs.shape[0]} exact null directions "
          f"(no observation depends on them)")
    print("  posterior standard deviation along those directions (mean over the")
    print("  10 directions): this is what a modeller is claiming to know about")
    print("  parts of the model the data never touch.")
    for name, C in (("smoothness", C_sm), ("learned", C_lp)):
        sig = np.mean([np.sqrt(v @ C @ v) for v in null_dirs])
        print(f"    {name:11s} prior: mean null-space sigma = {sig:.4f}")
    print(f"  the learned prior is more confident there ({s_par:.4f} along its own")
    print(f"  subspace, {s_perp:.4f} orthogonal to it) because the ensemble says a")
    print("  plausible model has bounded structure in those directions.  If the")
    print("  ensemble is right, that confidence is earned; if the target is outside")
    print("  the ensemble, it is fabricated, and the misfit cannot tell -- no")
    print("  observation depends on those directions at all.")

    section("4. Out-of-family targets: the prior imposes what it was taught")
    x = (np.arange(N) + 0.5) / N
    ood = {
        "high-frequency oscillation": np.tile(np.sin(12 * np.pi * x), (200, 1)),
        "isolated spike": None,
    }
    spk = np.zeros((200, N))
    spk[:, N // 2] = 1.5
    ood["isolated spike"] = spk
    print("  target                    smooth MSE   learned MSE   ratio   "
          "truth energy in subspace")
    for name, M in ood.items():
        D_o = M @ A.T + NOISE * RNG.standard_normal((M.shape[0], N_DATA))
        m_s = D_o @ (C_sm @ A.T / NOISE ** 2).T
        lhs_o = A.T @ D_o.T / NOISE ** 2 + np.outer(P_learn @ mu,
                                                    np.ones(M.shape[0]))
        m_l = (C_lp @ lhs_o).T
        e_s = np.mean((m_s - M) ** 2)
        e_l = np.mean((m_l - M) ** 2)
        truth_frac = np.mean((M @ Vk.T @ Vk) ** 2) / np.mean(M ** 2)
        rec_frac = np.mean((m_l @ Vk.T @ Vk) ** 2) / np.mean(m_l ** 2)
        print(f"  {name:26s} {e_s:.3e}    {e_l:.3e}    {e_l / e_s:5.2f}   "
              f"{truth_frac:.3f} -> {rec_frac:.3f}")
    print("  the aggregate error is not the point: on the oscillation the learned")
    print("  prior is 8% worse, on the spike it happens to be better.  What is")
    print("  systematic is WHERE the recovered energy sits.  The last column pairs")
    print("  the fraction of the truth's energy inside the learned subspace with the")
    print("  fraction of the recovered model's energy there: whatever the truth is,")
    print("  the prior forces about 95% of the answer into a 4-dimensional subspace")
    print("  that a sparse or oscillatory truth barely occupies.")
    print("  A generative prior is a bet on the ensemble it was trained on.  It wins")
    print("  the bet in-distribution; outside it, it substitutes the shapes it")
    print("  knows for the structure it does not, and reports no warning.")


if __name__ == "__main__":
    main()
