#!/usr/bin/env python3
"""Detection and attribution by optimal fingerprinting: a synthetic two-signal
generalised-least-squares regression, the cost of ignoring the noise covariance,
the separability of two fingerprints, and the bias from a misspecified pattern.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python detection_attribution_demo.py

Everything is SYNTHETIC.  There is no real observing system, no climate model and
no observed temperature series here: the "observations" are a chosen signal plus
a chosen correlated-noise model.  No published scaling factor or attribution
result is quoted.

Contents
--------
1. The synthetic setup: two spatial fingerprints, a separable AR(1) noise model,
   and a stated signal-to-noise ratio.
2. One realisation: OLS versus GLS estimates, and a detection test
   (beta = 0) followed by an attribution test (beta consistent with 1).
3. Monte Carlo coverage of the nominal 90% interval for OLS and for GLS.
4. Separating two fingerprints: the pattern correlation and the variance
   inflation when the signals resemble one another.
5. A misspecified fingerprint: how a stated pattern error biases the scaling
   factor.
6. What a scaling factor does and does not mean.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC setup (chosen, not measured) ---------------------------------
N_SPACE = 20          # synthetic "grid boxes"
N_YEARS = 40          # length of the synthetic observational record
BETA_TRUE = np.array([1.00, 1.00])   # model amplitudes are correct in truth
RHO = 0.5             # lag-1 autocorrelation of the noise in time
LENGTH_SCALE = 3.0    # spatial correlation length, in grid boxes
SIGMA_NOISE = 0.35    # noise standard deviation, in K
N_MC = 300            # Monte Carlo realisations for the coverage study


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def spatial_cov():
    """Exponential spatial correlation of unit variance (SYNTHETIC)."""
    d = np.abs(np.arange(N_SPACE)[:, None] - np.arange(N_SPACE)[None, :])
    return np.exp(-d / LENGTH_SCALE)


def temporal_cov():
    """AR(1) temporal covariance rho^|i-j| (SYNTHETIC)."""
    t = np.abs(np.arange(N_YEARS)[:, None] - np.arange(N_YEARS)[None, :])
    return RHO ** t


def noise_cov():
    """Full space-time noise covariance (separable, SYNTHETIC)."""
    return SIGMA_NOISE ** 2 * np.kron(temporal_cov(), spatial_cov())


def patterns(corr_target):
    """Two unit-norm spatial fingerprints with a chosen inner-product.

    Returns (x_ant, x_aer) as vectors of length N_SPACE.  x_ant is a fixed
    large-scale pattern; x_aer is adjusted so that cos(theta) between the two
    equals corr_target.
    """
    x_ant = np.cos(np.linspace(0.0, 2.5 * np.pi, N_SPACE))
    x_ant = x_ant - x_ant.mean()
    x_ant /= np.linalg.norm(x_ant)
    rng = np.random.default_rng(7)
    w = rng.standard_normal(N_SPACE)
    w = w - w.mean()
    w -= w @ x_ant * x_ant               # orthogonal component
    w /= np.linalg.norm(w)
    c = corr_target
    x_aer = c * x_ant + np.sqrt(max(0.0, 1.0 - c ** 2)) * w
    return x_ant, x_aer


def design(x_ant, x_aer):
    """Design matrix: each pattern constant in time (a stated simplification)."""
    return np.column_stack([np.kron(np.ones(N_YEARS), x_ant),
                            np.kron(np.ones(N_YEARS), x_aer)])


def ols(y, X):
    """Ordinary least squares with the naive (i.i.d.) covariance."""
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    resid = y - X @ beta
    dof = y.size - X.shape[1]
    s2 = resid @ resid / dof
    cov = s2 * np.linalg.inv(X.T @ X)
    return beta, cov


def gls(y, X, C):
    """Generalised least squares using the known noise covariance C."""
    Cinv = np.linalg.inv(C)
    XtCi = X.T @ Cinv
    cov = np.linalg.inv(XtCi @ X)
    beta = cov @ (XtCi @ y)
    return beta, cov


def ci90(beta, cov):
    """90% interval from a point estimate and its covariance matrix."""
    se = np.sqrt(np.diag(cov))
    return beta - 1.6449 * se, beta + 1.6449 * se


def se_of(cov, i):
    return float(np.sqrt(cov[i, i]))


def main():
    section("1. Synthetic setup: patterns, noise covariance, signal-to-noise")
    x_ant, x_aer = patterns(0.30)
    X = design(x_ant, x_aer)
    C = noise_cov()
    L = np.linalg.cholesky(C)
    signal = X @ BETA_TRUE
    snr = np.sqrt(signal @ signal / np.trace(C))
    print(f"  {N_SPACE} grid boxes x {N_YEARS} years; two signals, "
          f"beta_true = {BETA_TRUE}")
    print(f"  pattern correlation cos(theta) = {x_ant @ x_aer:+.3f}")
    print(f"  noise: sigma = {SIGMA_NOISE:.2f} K, lag-1 rho = {RHO:.2f}, "
          f"spatial length scale = {LENGTH_SCALE:.1f} boxes")
    print(f"  rms(signal)/rms(noise) over the whole space-time vector = "
          f"{snr:.3f}")
    print("  this is a *chosen* signal-to-noise ratio, not a measured one.")

    section("2. One realisation: estimation, detection, attribution")
    eps = L @ RNG.standard_normal(N_SPACE * N_YEARS)
    y = signal + eps
    b_ols, c_ols = ols(y, X)
    b_gls, c_gls = gls(y, X, C)
    print("  fingerprint scaling factors (unitless; 1 = model amplitude correct)")
    for i, name in enumerate(("anthropogenic", "aerosol")):
        so, sg = se_of(c_ols, i), se_of(c_gls, i)
        print(f"    {name:13s}: OLS {b_ols[i]:+.3f}  90% CI "
              f"[{b_ols[i] - 1.6449 * so:+.3f}, {b_ols[i] + 1.6449 * so:+.3f}]"
              f"   width {2 * 1.6449 * so:.3f}")
        print(f"    {'':13s}  GLS {b_gls[i]:+.3f}  90% CI "
              f"[{b_gls[i] - 1.6449 * sg:+.3f}, {b_gls[i] + 1.6449 * sg:+.3f}]"
              f"   width {2 * 1.6449 * sg:.3f}")
    lo, hi = ci90(b_gls, c_gls)
    print(f"  detection (GLS): is beta_ant different from 0?  "
          f"{'yes' if lo[0] > 0 else 'no'}  (CI [{lo[0]:+.3f}, {hi[0]:+.3f}])")
    print(f"  attribution (GLS): is beta_ant consistent with 1?  "
          f"{'yes' if lo[0] <= 1.0 <= hi[0] else 'no'}")
    print("  detection and attribution are different tests against different")
    print("  nulls; a signal can be detected and still have an amplitude that")
    print("  the model gets wrong.")

    section("3. Coverage of the nominal 90% interval, OLS versus GLS")
    act_ols = np.empty((N_MC, 2))
    act_gls = np.empty((N_MC, 2))
    w_ols = np.empty((N_MC, 2))
    w_gls = np.empty((N_MC, 2))
    for k in range(N_MC):
        e = L @ RNG.standard_normal(N_SPACE * N_YEARS)
        yy = signal + e
        bo, co = ols(yy, X)
        bg, cg = gls(yy, X, C)
        lo_o, hi_o = ci90(bo, co)
        lo_g, hi_g = ci90(bg, cg)
        act_ols[k] = (lo_o <= BETA_TRUE) & (BETA_TRUE <= hi_o)
        act_gls[k] = (lo_g <= BETA_TRUE) & (BETA_TRUE <= hi_g)
        w_ols[k] = hi_o - lo_o
        w_gls[k] = hi_g - lo_g
    print(f"  nominal coverage 0.90, {N_MC} realisations")
    for i, name in enumerate(("anthropogenic", "aerosol")):
        print(f"    {name:13s}: OLS coverage {act_ols[:, i].mean():.3f}, "
              f"mean width {w_ols[:, i].mean():.3f}")
        print(f"    {'':13s}  GLS coverage {act_gls[:, i].mean():.3f}, "
              f"mean width {w_gls[:, i].mean():.3f}")
    print("  OLS is unbiased but its stated uncertainty is not: it assumes")
    print("  independent samples, and the noise here is correlated.  GLS knows")
    print("  the covariance and its interval means what it says.  Reporting a")
    print("  significance level means reporting the covariance assumption.")

    section("4. Separating two fingerprints that resemble one another")
    print("  cos(theta)   SE(beta_ant)   variance inflation vs orthogonal")
    for corr in (0.0, 0.30, 0.60, 0.85, 0.95):
        xa, xb = patterns(corr)
        Xs = design(xa, xb)
        _, cg = gls(signal, Xs, C)
        se = np.sqrt(cg[0, 0])
        if corr == 0.0:
            se0 = se
        print(f"  {corr:10.2f}   {se:12.4f}   {(se / se0) ** 2:14.2f}x")
    print("  as the two patterns converge, the regression can no longer tell")
    print("  which one produced the signal and the variance explodes.  This is")
    print("  the honest reason a single-signal analysis is weaker than a")
    print("  two-signal one: it is not about the number of signals, it is about")
    print("  how distinguishable their patterns are.")

    section("5. A misspecified fingerprint")
    x_ant, x_aer = patterns(0.30)
    X_true = design(x_ant, x_aer)
    rng = np.random.default_rng(11)
    pert = rng.standard_normal(N_SPACE)
    pert -= pert.mean()
    pert -= (pert @ x_ant) * x_ant
    pert /= np.linalg.norm(pert)
    print("  the analysis uses x_ant_used = (1-f) x_ant_true + f x_noise, unit-norm")
    print("     f     cos(pattern, truth)   mean beta_hat_ant   bias")
    for f in (0.0, 0.10, 0.25, 0.40, 0.60):
        x_used = (1.0 - f) * x_ant + f * pert
        x_used /= np.linalg.norm(x_used)
        Xu = design(x_used, x_aer)
        vals = np.empty(N_MC)
        for k in range(N_MC):
            e = L @ RNG.standard_normal(N_SPACE * N_YEARS)
            yy = X_true @ BETA_TRUE + e
            vals[k] = gls(yy, Xu, C)[0][0]
        print(f"  {f:5.2f}   {x_used @ x_ant:17.3f}   {vals.mean():17.3f}   "
              f"{vals.mean() - BETA_TRUE[0]:+6.3f}")
    print("  a fingerprint error biases the scaling factor away from 1 even")
    print("  when the model amplitude is right; the regression cannot tell a")
    print("  wrong amplitude from a wrong pattern, because only their product")
    print("  enters the fit.")

    section("6. What a scaling factor does and does not mean")
    print("  beta is the factor by which the model's response pattern must be")
    print("  scaled to best match the observations.")
    print("  (a) beta = 1 => the observations are consistent with the model's")
    print("      amplitude for that forcing combination. It is NOT proof that")
    print("      the forcing caused the change.")
    print("  (b) beta = 0 => no detectable contribution from that pattern in this")
    print("      record and with this noise model. It is NOT proof of absence.")
    print("  (c) The uncertainty depends on the noise covariance, on the")
    print("      separability of the patterns, and on the length of both the")
    print("      observational and the control record.")
    print("  (d) An attribution statement is probabilistic and conditional on")
    print("      the counterfactual (here: the noise model and the pattern).")


if __name__ == "__main__":
    main()
