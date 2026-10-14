#!/usr/bin/env python3
"""Emulators and surrogate models: fitting a Gaussian-process surrogate to a
nonlinear synthetic climate response, measuring interpolation and extrapolation
error, and showing that a surrogate's own uncertainty is not model error.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python emulation_and_surrogates_demo.py

All models and data in this file are SYNTHETIC.  The "climate model" is a
chosen nonlinear algebraic response, not a climate model; it is used because its
answer is computable exactly, which lets the surrogate error be measured rather
than estimated.

Contents
--------
1. The synthetic response: equilibrium warming of a nonlinear energy-balance
   model as a function of a step forcing, obtained by root finding.
2. A Gaussian-process emulator: hyperparameters by marginal likelihood, error
   inside and outside the training range.
3. Error versus training-set size.
4. A smooth surrogate over a kinked response: the surrogate is confidently
   wrong exactly where the physics changes.
"""

import numpy as np
from scipy.optimize import brentq

RNG = np.random.default_rng(20261014)

LAMBDA_BASE_W_M2_K = 0.8      # SYNTHETIC feedback parameter at small warming
LAMBDA_EXTRA_W_M2_K = 0.6     # SYNTHETIC additional feedback at large warming
TRANSITION_K = 1.0            # SYNTHETIC warming scale of the feedback change
NOISE_K = 0.02                # SYNTHETIC surrogate-target noise


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def feedback_parameter(delta_t):
    """Feedback parameter that increases with warming (a stabilising feedback)."""
    return LAMBDA_BASE_W_M2_K + LAMBDA_EXTRA_W_M2_K * np.tanh(
        (delta_t - TRANSITION_K) / 1.5)


def equilibrium_warming(forcing):
    """Solve forcing = lambda(dT) * dT for dT, in kelvin."""
    def residual(delta_t):
        return feedback_parameter(delta_t) * delta_t - forcing
    return brentq(residual, 0.0, 50.0, xtol=1e-12)


def rbf_kernel(x1, x2, length_scale, signal_sd):
    d = x1[:, None] - x2[None, :]
    return signal_sd ** 2 * np.exp(-0.5 * (d / length_scale) ** 2)


def gp_log_marginal(x, y, length_scale, signal_sd, noise_sd):
    k = rbf_kernel(x, x, length_scale, signal_sd)
    k = k + noise_sd ** 2 * np.eye(len(x))
    with np.errstate(all="ignore"):
        sign, log_det = np.linalg.slogdet(k)
        if sign <= 0 or not np.isfinite(log_det):
            return -np.inf
        centred = y - y.mean()
        try:
            alpha = np.linalg.solve(k, centred)
        except np.linalg.LinAlgError:
            return -np.inf
        value = -0.5 * float(centred @ alpha) - 0.5 * len(x) * np.log(2 * np.pi) \
            - 0.5 * float(log_det)
    return value if np.isfinite(value) else -np.inf


def gp_predict(x_train, y_train, x_test, length_scale, signal_sd, noise_sd):
    mean_train = float(y_train.mean())
    k = rbf_kernel(x_train, x_train, length_scale, signal_sd) \
        + noise_sd ** 2 * np.eye(len(x_train))
    k_star = rbf_kernel(x_train, x_test, length_scale, signal_sd)
    chol = np.linalg.cholesky(k)
    alpha = np.linalg.solve(chol.T, np.linalg.solve(chol, y_train - mean_train))
    mean = mean_train + k_star.T @ alpha
    v = np.linalg.solve(chol, k_star)
    variance = signal_sd ** 2 - np.sum(v ** 2, axis=0)
    return mean, np.sqrt(np.clip(variance, 0.0, None))


def fit_gp(x_train, y_train):
    best = None
    for length_scale in (0.3, 0.5, 1.0, 2.0):
        for signal_sd in (0.5, 1.0, 2.0):
            for noise_sd in (0.01, 0.05, 0.1):
                value = gp_log_marginal(x_train, y_train, length_scale,
                                        signal_sd, noise_sd)
                if best is None or value > best[0]:
                    best = (value, length_scale, signal_sd, noise_sd)
    return best[1], best[2], best[3]


def main():
    section("1. The synthetic response")
    forcing_grid = np.linspace(0.0, 12.0, 241)
    warming = np.array([equilibrium_warming(f) for f in forcing_grid])
    linear_warming = forcing_grid / LAMBDA_BASE_W_M2_K
    print(f"  feedback parameter lambda(dT) = {LAMBDA_BASE_W_M2_K:.2f} + "
          f"{LAMBDA_EXTRA_W_M2_K:.2f}*tanh((dT - {TRANSITION_K:.1f})/1.5)"
          f" W m^-2 K^-1")
    print(f"  response found by root finding, xtol 1e-12")
    print(f"  {'F (W/m^2)':>10s} {'dT nonlinear (K)':>18s} "
          f"{'F/lambda_base (K)':>18s} {'difference (K)':>15s}")
    for f in (1.0, 2.0, 4.0, 6.0, 8.0, 12.0):
        dt = equilibrium_warming(f)
        print(f"  {f:10.1f} {dt:18.4f} {f / LAMBDA_BASE_W_M2_K:18.4f} "
              f"{dt - f / LAMBDA_BASE_W_M2_K:15.4f}")
    print("  The response is sublinear: as warming grows, lambda grows, so more")
    print("  forcing is needed per additional kelvin.")

    section("2. Gaussian-process emulator: interpolation and extrapolation")
    n_train = 12
    x_train = np.sort(RNG.uniform(0.0, 6.0, n_train))
    y_train = np.array([equilibrium_warming(f) for f in x_train]) \
        + NOISE_K * RNG.standard_normal(n_train)
    length_scale, signal_sd, noise_sd = fit_gp(x_train, y_train)
    print(f"  training points: {n_train}, drawn uniformly on F in [0, 6] W/m^2")
    print(f"  selected hyperparameters (by marginal likelihood over a grid):")
    print(f"    length scale = {length_scale:.2f} W/m^2, "
          f"signal sd = {signal_sd:.2f} K, noise sd = {noise_sd:.2f} K")
    inside = np.linspace(0.0, 6.0, 121)
    outside = np.linspace(6.0, 12.0, 61)
    mean_in, sd_in = gp_predict(x_train, y_train, inside, length_scale,
                                signal_sd, noise_sd)
    mean_out, sd_out = gp_predict(x_train, y_train, outside, length_scale,
                                  signal_sd, noise_sd)
    true_in = np.array([equilibrium_warming(f) for f in inside])
    true_out = np.array([equilibrium_warming(f) for f in outside])
    print(f"  RMSE inside the training range  = "
          f"{np.sqrt(np.mean((mean_in - true_in) ** 2)):.4f} K")
    print(f"  RMSE outside the training range = "
          f"{np.sqrt(np.mean((mean_out - true_out) ** 2)):.4f} K")
    linear_in = inside / LAMBDA_BASE_W_M2_K
    linear_out = outside / LAMBDA_BASE_W_M2_K
    print(f"  for comparison, a linear surrogate dT = F/{LAMBDA_BASE_W_M2_K:.1f}:")
    print(f"    RMSE inside  = "
          f"{np.sqrt(np.mean((linear_in - true_in) ** 2)):.4f} K")
    print(f"    RMSE outside = "
          f"{np.sqrt(np.mean((linear_out - true_out) ** 2)):.4f} K")
    print(f"  mean predictive sd inside  = {sd_in.mean():.4f} K")
    print(f"  mean predictive sd outside = {sd_out.mean():.4f} K")
    max_out_err = int(np.argmax(np.abs(mean_out - true_out)))
    print(f"  worst extrapolation error at F = {outside[max_out_err]:.2f} W/m^2: "
          f"{abs(mean_out[max_out_err] - true_out[max_out_err]):.4f} K, "
          f"while the surrogate's stated sd there is "
          f"{sd_out[max_out_err]:.4f} K")
    print("  A Gaussian process returns to its prior mean outside the data, and its")
    print("  predictive sd grows, so it is at least visibly unsure. A surrogate")
    print("  that is a fitted polynomial has no such signal and will extrapolate")
    print("  with the same (falsely small) confidence everywhere.")

    section("3. Error versus training-set size")
    print(f"  {'N':>4s} {'RMSE inside (K)':>16s} {'RMSE outside (K)':>17s}")
    for n in (6, 12, 24, 48):
        xs = np.sort(RNG.uniform(0.0, 6.0, n))
        ys = np.array([equilibrium_warming(f) for f in xs]) \
            + NOISE_K * RNG.standard_normal(n)
        ls, ss, ns = fit_gp(xs, ys)
        mi, _ = gp_predict(xs, ys, inside, ls, ss, ns)
        mo, _ = gp_predict(xs, ys, outside, ls, ss, ns)
        print(f"  {n:4d} {np.sqrt(np.mean((mi - true_in) ** 2)):16.4f} "
              f"{np.sqrt(np.mean((mo - true_out) ** 2)):17.4f}")
    print("  More training points reduce the interpolation error. The extrapolation")
    print("  error falls only if the added points extend the range; emulators are")
    print("  no better than their training design.")

    section("4. A smooth surrogate over a discontinuous response")
    def stepped(forcing):
        """Response with a threshold: a feedback switches on abruptly at F = 4."""
        return np.where(forcing < 4.0, 0.35 * forcing, 0.35 * forcing + 1.8)

    # Training points deliberately avoid a window around the transition.
    candidates = RNG.uniform(0.0, 8.0, 60)
    x_k = np.sort(candidates[(candidates < 3.4) | (candidates > 4.6)][:28])
    y_k = stepped(x_k) + NOISE_K * RNG.standard_normal(len(x_k))
    ls, ss, ns = fit_gp(x_k, y_k)
    dense = np.linspace(0.0, 8.0, 321)
    mean_k, sd_k = gp_predict(x_k, y_k, dense, ls, ss, ns)
    truth_k = stepped(dense)
    gap = np.abs(dense - 4.0) < 0.4
    error = np.abs(mean_k - truth_k)
    print(f"  true response has a step of +1.80 K at F = 4.0 W/m^2")
    print(f"  training points: {len(x_k)}, none within 0.6 W/m^2 of the step")
    print(f"  emulator RMSE over the whole range    = "
          f"{np.sqrt(np.mean((mean_k - truth_k) ** 2)):.4f} K")
    print(f"  emulator mean |error| in |F - 4| < 0.4 = {error[gap].mean():.4f} K")
    print(f"  mean stated sd in that window          = {sd_k[gap].mean():.4f} K")
    print(f"  ratio |error| / stated sd              = "
          f"{error[gap].mean() / sd_k[gap].mean():.3f}")
    print("  The emulator bridges the two branches smoothly, so inside the gap it is")
    print("  wrong by far more than its own stated sd: it is confidently wrong. Its")
    print("  predictive variance measures distance from training points, not")
    print("  disagreement with the physics. A surrogate fit over a transition it has")
    print("  never sampled reports interpolation-grade confidence on the wrong side")
    print("  of a tipping point, which is exactly where the answer matters.")


if __name__ == "__main__":
    main()
