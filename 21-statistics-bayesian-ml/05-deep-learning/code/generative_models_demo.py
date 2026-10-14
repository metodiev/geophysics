#!/usr/bin/env python3
"""Generative models on SYNTHETIC data: a one-dimensional variational
autoencoder trained by gradient ascent on the exact ELBO, a two-sample
divergence measure used by generative adversarial training, and the forward
noising schedule of a diffusion model.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python generative_models_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. A variational autoencoder with a closed-form ELBO.
2. The generator-discriminator objective measured by a two-sample statistic.
3. The forward diffusion schedule and the signal-to-noise ratio.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    print("SYNTHETIC data generated below; no measured value is used.")

    section("1. A variational autoencoder with a closed-form ELBO")
    mu_true, sd_true = 2.0, 1.5
    n = 4000
    x = mu_true + sd_true * RNG.standard_normal(n)
    xbar = float(x.mean())
    ss = float(np.sum((x - xbar) ** 2))
    prior_var = 1.0

    def elbo(m, s2):
        rec = -0.5 * (n * np.log(2 * np.pi * sd_true ** 2)
                      + (ss + n * (xbar - m) ** 2 + n * s2) / sd_true ** 2)
        log_prior = -0.5 * (np.log(2 * np.pi * prior_var)
                            + (m ** 2 + s2) / prior_var)
        entropy = 0.5 * np.log(2 * np.pi * np.e * s2)
        return rec + log_prior + entropy

    post_var = 1.0 / (1.0 / prior_var + n / sd_true ** 2)
    post_mean = post_var * (n * xbar / sd_true ** 2)
    print(f"  data: {n} draws from N({mu_true:.1f}, {sd_true:.1f}^2); prior N(0,1)")
    print(f"  exact posterior mean and variance = {post_mean:.7f}, "
          f"{post_var:.7f}")
    print(f"  ELBO at the prior (m = 0, s^2 = 1)  = {elbo(0.0, 1.0):.4f}")
    print(f"  ELBO at the sample mean instead     = {elbo(xbar, post_var):.4f}")
    print(f"  ELBO at the exact posterior         = "
          f"{elbo(post_mean, post_var):.4f}")
    print(f"  improvement over the prior          = "
          f"{elbo(post_mean, post_var) - elbo(0.0, 1.0):.4f} nats")
    print("  the family is Gaussian and the true posterior is a member of it, so")
    print("  the maximum ELBO equals the log evidence exactly: with a rich enough")
    print("  family the variational bound ceases to be a bound and becomes the")
    print("  answer. The objective is reconstruction minus KL, and the three")
    print("  numbers above are that objective at three parameter settings.")

    section("2. The adversarial objective as a two-sample problem")
    real = 1.0 + 0.8 * RNG.standard_normal(500)
    for name, fake in (("bad generator", -1.0 + 0.8 * RNG.standard_normal(500)),
                       ("good generator", 1.05 + 0.85 * RNG.standard_normal(500))):
        allv = np.concatenate([real, fake])
        order = np.argsort(allv)
        labels = np.concatenate([np.ones(500), np.zeros(500)])[order]
        ranks = np.arange(1, 1001)
        auc = (ranks[labels == 1].sum() - 500 * 501 / 2.0) / (500 * 500)
        print(f"  {name:15s}: discriminator AUC = {auc:.4f}")
    print("  a perfect discriminator gives AUC = 1 and a generator that matches")
    print("  the data gives AUC = 0.5; the training game is a search for the")
    print("  point where the discriminator can no longer separate the two.")

    section("3. The forward diffusion schedule")
    steps = 1000
    betas = np.linspace(1e-4, 0.02, steps)
    alphas = 1.0 - betas
    abar = np.cumprod(alphas)
    snr = abar / (1.0 - abar)
    print("  step    alpha_bar   signal-to-noise")
    for t in (1, 10, 100, 500, 900, 1000):
        print(f"  {t:5d}   {abar[t - 1]:9.6f}   {snr[t - 1]:14.4f}")
    half = int(np.argmin(np.abs(snr - 1.0))) + 1
    print(f"  the signal and the noise are equal (SNR = 1) at step {half} of "
          f"{steps}")
    print("  forward diffusion is fixed and needs no training: it destroys")
    print("  information at a known rate. The model learns only the reverse")
    print("  step, and the SNR schedule is what sets how hard that step is.")


if __name__ == "__main__":
    main()
