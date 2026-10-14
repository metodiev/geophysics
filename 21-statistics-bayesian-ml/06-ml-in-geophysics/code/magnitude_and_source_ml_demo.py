#!/usr/bin/env python3
"""Magnitude estimation: a standard attenuation formula versus a learned regressor.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnitude_and_source_ml_demo.py

Everything here is SYNTHETIC.  Amplitudes and periods are generated from a
chosen magnitude and hypocentral distance through an exact attenuation law plus
lognormal scatter; no catalogue, station correction or magnitude is read.

Sections
--------
1. The synthetic measurement set.
2. A hand-written estimator and its irreducible error.
3. A learned estimator on the same random split.
4. The same learned estimator asked to extrapolate beyond its training range.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N = 400             # events
M_MIN, M_MAX = 2.0, 5.0
R_LOG_MIN, R_LOG_MAX = 0.7, 2.0        # log10(R / 1 km)
SIGMA_LOG_A = 0.15  # lognormal amplitude scatter, log10 units
SIGMA_LOG_T = 0.05  # period scatter, log10 units
LOG_A_REF = -1.0    # log10(counts) at M = 0, R = 10 km
RIDGE = 0.1         # ridge penalty on standardised features


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def make_events(n):
    mag = RNG.uniform(M_MIN, M_MAX, n)
    log_r = RNG.uniform(R_LOG_MIN, R_LOG_MAX, n)
    log_a = (mag - (log_r - 1.0) + LOG_A_REF
             + SIGMA_LOG_A * RNG.standard_normal(n))
    log_t = np.log10(0.4 + 0.1 * mag) + SIGMA_LOG_T * RNG.standard_normal(n)
    return mag, 10.0 ** log_r, log_a, 10.0 ** log_t


def baseline(log_a, r_km):
    """M = log10(A) + log10(R/10 km) - LOG_A_REF, with LOG_A_REF = -1."""
    return log_a + np.log10(r_km / 10.0) - LOG_A_REF


def design(log_a, r_km, t_p):
    return np.column_stack([log_a, np.log10(r_km), np.log10(t_p)])


def fit_ridge(x, y, lam=RIDGE):
    mean, sd = x.mean(axis=0), x.std(axis=0)
    z = (x - mean) / sd
    zc = np.column_stack([np.ones(z.shape[0]), z])
    penalty = lam * np.eye(zc.shape[1])
    penalty[0, 0] = 0.0
    coef = np.linalg.solve(zc.T @ zc + penalty, zc.T @ y)
    return mean, sd, coef


def predict(x, pars):
    mean, sd, coef = pars
    zc = np.column_stack([np.ones(x.shape[0]), (x - mean) / sd])
    return zc @ coef


def scores(tag, truth, estimate):
    err = estimate - truth
    print(f"  {tag}")
    print(f"    RMSE = {np.sqrt(np.mean(err ** 2)):.3f} magnitude units, "
          f"bias = {err.mean():+.3f}, scatter = {err.std(ddof=1):.3f}")
    return err


def main():
    section("1. The synthetic measurement set")
    mag, r_km, log_a, t_p = make_events(N)
    print(f"SYNTHETIC events: n = {N}, magnitude drawn uniformly from "
          f"{M_MIN:.1f} to {M_MAX:.1f}")
    print(f"  hypocentral distance {r_km.min():.1f} to {r_km.max():.1f} km")
    print(f"  amplitude: log10 A = M - log10(R/10 km) {LOG_A_REF:+.1f} "
          f"+ N(0, {SIGMA_LOG_A:.2f}^2)  [A in counts]")
    print(f"  period: log10 T = log10(0.4 + 0.1 M) + N(0, {SIGMA_LOG_T:.2f}^2)"
          f"  [T in s]")
    print(f"  the scatter {SIGMA_LOG_A:.2f} is irreducible for ANY estimator "
          f"that never sees T")

    section("2. A hand-written estimator and its irreducible error")
    print("  M_hat = log10 A + log10(R/10 km) - LOG_A_REF, with LOG_A_REF =")
    print(f"  {LOG_A_REF:+.1f} for this generator, recovers M exactly in the")
    print(f"  noise-free limit, so its error is exactly the amplitude scatter")
    base_err = baseline(log_a, r_km) - mag
    print(f"  full-sample check: RMSE = "
          f"{np.sqrt(np.mean(base_err ** 2)):.3f} magnitude units "
          f"(the generator used {SIGMA_LOG_A:.2f})")

    section("3. A learned estimator on the same random split")
    idx = RNG.permutation(N)
    n_train = int(0.7 * N)
    tr, te = idx[:n_train], idx[n_train:]
    pars = fit_ridge(design(log_a, r_km, t_p)[tr], mag[tr])
    est = predict(design(log_a, r_km, t_p)[te], pars)
    print(f"  training events {tr.size}, held-out events {te.size}")
    print(f"  features: log10 A, log10 R, log10 T (standardised), ridge = "
          f"{RIDGE:.2f}")
    print(f"  coefficients (standardised): intercept = {pars[2][0]:.3f}, "
          f"log10 A = {pars[2][1]:+.3f}, log10 R = {pars[2][2]:+.3f}, "
          f"log10 T = {pars[2][3]:+.3f}")
    e_base = scores("hand-written estimator on the held-out events:",
                    mag[te], baseline(log_a[te], r_km[te]))
    scores("learned estimator on the held-out events:", mag[te], est)
    gain = np.sqrt(np.mean(e_base ** 2)) - np.sqrt(np.mean(
        (est - mag[te]) ** 2))
    print(f"  the learned model gains {gain:+.3f} magnitude units of RMSE.")
    print("  The coefficient on log10 T is small because T adds little once")
    print("  log10 A and log10 R are present: the model rediscovered the")
    print("  attenuation law, it did not improve on it.")

    section("4. The learned estimator asked to extrapolate")
    cut = 3.6
    tr = np.nonzero(mag <= cut)[0]
    te = np.nonzero(mag > cut)[0]
    pars = fit_ridge(design(log_a, r_km, t_p)[tr], mag[tr])
    est = predict(design(log_a, r_km, t_p)[te], pars)
    print(f"  training on M <= {cut:.1f} ({tr.size} events), testing on "
          f"M > {cut:.1f} ({te.size} events)")
    e_base = scores("hand-written estimator on the extrapolation test:",
                    mag[te], baseline(log_a[te], r_km[te]))
    e_ml = scores("learned estimator on the extrapolation test:",
                  mag[te], est)
    print(f"  RMSE ratio learned/hand-written = "
          f"{np.sqrt(np.mean(e_ml ** 2)) / np.sqrt(np.mean(e_base ** 2)):.3f}")
    print(f"  learned mean error in the top bin (M > {cut:.1f}) = "
          f"{e_ml.mean():+.3f} magnitude units")
    print("  The attenuation law is exact and the hand-written estimator keeps")
    print("  working outside the training range; the learned one does not, so a")
    print(f"  network trained on M <= {cut:.1f} must not be pointed at M = 6.")
    print("\nSYNTHETIC: the 'true' magnitude is the generator's own number. A real")
    print("catalogue magnitude is itself an estimate with its own bias, which this")
    print("demo cannot quantify.")


if __name__ == "__main__":
    main()
