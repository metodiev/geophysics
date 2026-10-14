#!/usr/bin/env python3
"""Model-data comparison in palaeoclimate: a proxy system model, calibration
bias when the calibration is transported to a different mean state, and the
variance reduction of a simple optimal-interpolation update.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python paleoclimate_model_data_demo.py

All models and data in this file are SYNTHETIC.  The "climate field", the
"proxies" and the "model prior" are generated, not measured, and no published
reconstruction or calibration is quoted.

Contents
--------
1. A synthetic climate field, a synthetic proxy system model with an
   unmodelled local factor, and a calibration period.
2. Reconstruction error: noise, unmodelled factor, and calibration transported
   to a different mean state.
3. A scalar optimal-interpolation (Kalman-style) update and its variance
   reduction, as a function of the prior and observation errors.
4. Why a biased proxy biases the posterior and leaves the variance small.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N_SITE = 40                 # synthetic sites along a transect
N_TIME = 60                 # synthetic time steps
PROXY_NOISE = 0.5           # proxy noise, K-equivalent
CONFOUND_STRENGTH = 0.8     # unmodelled local factor, K-equivalent
MODERN_MEAN_OFFSET = 0.0    # calibration period mean state
PALEO_MEAN_OFFSET = -3.0    # target period mean state (a different climate)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. Synthetic field and proxy system model")
    x = np.linspace(0.0, 1.0, N_SITE)
    pattern = 1.0 - 0.6 * x                       # a synthetic spatial gradient
    time = np.arange(N_TIME)
    t_signal = np.sin(2.0 * np.pi * time / 20.0)  # a synthetic temporal signal
    confound = np.sin(2.0 * np.pi * x * 2.5)[None, :] * np.ones((N_TIME, 1))
    truth_modern = 5.0 * pattern[None, :] * (1.0 + 0.4 * t_signal[:, None])
    truth_paleo = truth_modern + PALEO_MEAN_OFFSET
    print(f"  {N_SITE} sites, {N_TIME} time steps")
    print(f"  synthetic truth: modern mean {truth_modern.mean():.3f} K, "
          f"palaeo mean {truth_paleo.mean():.3f} K "
          f"(offset {PALEO_MEAN_OFFSET:+.1f} K)")
    print(f"  proxy = 1.4*T + {CONFOUND_STRENGTH:.1f}*local_factor + noise"
          f"({PROXY_NOISE:.1f} K)")

    proxy_modern = (1.4 * truth_modern + CONFOUND_STRENGTH * confound
                    + PROXY_NOISE * RNG.standard_normal((N_TIME, N_SITE)))
    proxy_paleo = (1.4 * truth_paleo + CONFOUND_STRENGTH * confound
                   + PROXY_NOISE * RNG.standard_normal((N_TIME, N_SITE)))

    section("2. Calibration and reconstruction error")
    # Calibrate with the modern period only, using the true slope and intercept
    # that the analyst is assumed to have estimated (a synthetic calibration).
    slope, intercept = 1.4, 0.0
    recon_modern = (proxy_modern - intercept) / slope
    recon_paleo = (proxy_paleo - intercept) / slope

    def stats(name, recon, truth):
        rmse = float(np.sqrt(np.mean((recon - truth) ** 2)))
        bias = float(np.mean(recon - truth))
        print(f"  {name:<44s} RMSE {rmse:6.3f} K   bias {bias:+6.3f} K")
        return rmse, bias

    print("  calibration estimated on the modern period and applied to:")
    stats("the modern period (perfect slope, wrong local factor)",
          recon_modern, truth_modern)
    stats("the palaeo period (same relationship)",
          recon_paleo, truth_paleo)

    # Now the analyst ignores the unmodelled local factor and fits a single
    # site-mean slope, then transports it to the palaeo period.
    slope_bad, intercept_bad = 1.0, 0.0
    recon_bad = (proxy_paleo - intercept_bad) / slope_bad
    stats("palaeo period, calibration slope wrong by 40%",
          recon_bad, truth_paleo)

    # A calibration fitted to the *modern* relationship but applied where the
    # relationship differs: simulate a changed proxy sensitivity in the palaeo era.
    proxy_paleo_changed = (1.9 * truth_paleo + CONFOUND_STRENGTH * confound
                           + PROXY_NOISE * RNG.standard_normal((N_TIME, N_SITE)))
    recon_changed = (proxy_paleo_changed - intercept) / slope
    stats("palaeo period, proxy sensitivity changed to 1.9",
          recon_changed, truth_paleo)
    print("  The last two rows show the failure mode that matters: the error is a")
    print("  bias, not scatter. A biased reconstruction is not flagged by its")
    print("  uncertainty estimate, because the uncertainty measures the noise of")
    print("  the calibration, not the distance between two different worlds.")

    section("3. Optimal-interpolation update and variance reduction")
    prior_std = 2.0
    for obs_std, prior_std_local in ((1.0, 2.0), (2.0, 2.0), (4.0, 2.0)):
        gain = prior_std_local ** 2 / (prior_std_local ** 2 + obs_std ** 2)
        posterior_std = np.sqrt((1.0 - gain) * prior_std_local ** 2)
        print(f"  prior sd {prior_std_local:.1f} K, observation sd {obs_std:.1f} K"
              f" -> gain {gain:.4f}, posterior sd {posterior_std:.4f} K")
    print("  gain = prior_variance/(prior_variance + obs_variance); the posterior")
    print("  variance is (1 - gain) times the prior variance at an observation site")
    print("  and unchanged where there is no observation.")

    section("4. A biased proxy keeps a small variance")
    print(f"  prior (model) = truth_paleo - 0.5 K + "
          f"{prior_std:.1f} K noise")
    prior = truth_paleo - 0.5 + prior_std * RNG.standard_normal((N_TIME, N_SITE))
    prior_error = float(np.sqrt(np.mean((prior - truth_paleo) ** 2)))
    obs = proxy_paleo / 1.4                 # a deliberately biased "observation"
    obs_error = float(np.sqrt(np.mean((obs - truth_paleo) ** 2)))
    gain = prior_std ** 2 / (prior_std ** 2 + obs_error ** 2)
    posterior = prior + gain * (obs - prior)
    posterior_error = float(np.sqrt(np.mean((posterior - truth_paleo) ** 2)))
    print(f"  prior RMSE      = {prior_error:.4f} K")
    print(f"  observation RMSE = {obs_error:.4f} K")
    print(f"  gain             = {gain:.4f}")
    print(f"  posterior RMSE   = {posterior_error:.4f} K")
    print(f"  posterior variance = {(1 - gain) * prior_std ** 2:.4f} K^2, "
          f"sd {np.sqrt((1 - gain) * prior_std ** 2):.4f} K")
    print("  The posterior is closer to the truth than the prior because the update")
    print("  reduces random error. It is still biased by the proxy's own bias, which")
    print("  the update cannot see: the observation is treated as unbiased by")
    print("  construction. In a real comparison this is the step where a proxy")
    print("  systematic error, if unknown, becomes a confident wrong answer.")


if __name__ == "__main__":
    main()
