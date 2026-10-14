#!/usr/bin/env python3
"""Visualising and communicating uncertainty: bands, coverage and overlap.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python uncertainty_visualisation_demo.py

All models in this demo are SYNTHETIC.  The velocity profile is drawn from a
chosen covariance, not from an inversion of real data, and no measured value
appears anywhere.

Contents
--------
1. An ensemble of SYNTHETIC velocity profiles and its pointwise credible bands.
2. Pointwise coverage measured on new ensemble members.
3. Simultaneous coverage: why a pointwise band is not a band for the curve.
4. A skewed quantity of interest: equal-tailed versus HPD interval.
5. Overlap of credible bands is not evidence that two models agree.
6. A reporting checklist for uncertainty figures.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

Z = np.linspace(0.5, 40.0, 120)          # depth grid, km
V0 = 5.8                                  # mean velocity at the top, km/s
GRAD = 0.02                               # mean gradient, (km/s) per km
SIG = 0.35                                # profile standard deviation, km/s
LEN = 8.0                                 # correlation length, km


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def make_ensemble(n, seed):
    """Gaussian-process ensemble with a squared-exponential covariance."""
    rng = np.random.default_rng(seed)
    D = Z[:, None] - Z[None, :]
    C = SIG ** 2 * np.exp(-0.5 * (D / LEN) ** 2)
    C += 1e-8 * np.eye(Z.size)
    L = np.linalg.cholesky(C)
    mean = V0 + GRAD * Z
    return mean[None, :] + rng.standard_normal((n, Z.size)) @ L.T


def hpd_interval(x, level=0.95):
    """Shortest interval containing `level` of a sample: sort, then scan."""
    xs = np.sort(x)
    n = xs.size
    m = int(np.floor(level * n))
    widths = xs[m:] - xs[:n - m]
    i = int(np.argmin(widths))
    return float(xs[i]), float(xs[i + m]), float(widths[i])


def main():
    mean_curve = V0 + GRAD * Z
    ens = make_ensemble(5000, 1)
    lo68, hi68 = np.percentile(ens, [16.0, 84.0], axis=0)
    lo95, hi95 = np.percentile(ens, [2.5, 97.5], axis=0)

    section("1. A SYNTHETIC velocity ensemble and its credible bands")
    print(f"grid: {Z.size} depths from {Z[0]:.1f} to {Z[-1]:.1f} km")
    print(f"prior mean profile: v(z) = {V0:.1f} + {GRAD:.2f} z  (km/s)")
    print(f"covariance: squared exponential, sd = {SIG:.2f} km/s, "
          f"correlation length = {LEN:.1f} km")
    print(f"ensemble size: {ens.shape[0]} profiles")
    i = int(np.argmin(np.abs(Z - 20.0)))
    print(f"\n  at z = {Z[i]:.1f} km: mean = {ens[:, i].mean():.3f} km/s, "
          f"ensemble sd = {ens[:, i].std(ddof=1):.3f} km/s")
    print(f"  68% band = [{lo68[i]:.3f}, {hi68[i]:.3f}] km/s, "
          f"width {hi68[i] - lo68[i]:.3f} km/s")
    print(f"  95% band = [{lo95[i]:.3f}, {hi95[i]:.3f}] km/s, "
          f"width {hi95[i] - lo95[i]:.3f} km/s")
    print(f"  the ensemble sd is {ens[:, 1].std(ddof=1):.4f} km/s at the top and "
          f"{ens[:, -1].std(ddof=1):.4f} km/s at the bottom,")
    print("  constant here because the covariance is stationary; in a real")
    print("  inversion the width would grow with depth where the data are silent.")

    section("2. Pointwise coverage, measured on new members")
    fresh = make_ensemble(20000, 99)
    inside95 = (fresh >= lo95[None, :]) & (fresh <= hi95[None, :])
    inside68 = (fresh >= lo68[None, :]) & (fresh <= hi68[None, :])
    print("  fraction of NEW ensemble members inside the band at each depth:")
    print(f"    mean pointwise coverage of the 68% band = "
          f"{inside68.mean() * 100:.2f}%")
    print(f"    mean pointwise coverage of the 95% band = "
          f"{inside95.mean() * 100:.2f}%")
    print(f"    worst depth for the 95% band = {inside95.mean(axis=0).min() * 100:.2f}%")
    print("The bands are calibrated pointwise, which is what they claim: at each")
    print("single depth the stated fraction of members lies inside.")

    section("3. Simultaneous coverage: the band is not a band for the curve")
    whole95 = inside95.all(axis=1).mean()
    whole68 = inside68.all(axis=1).mean()
    print(f"  fraction of NEW members lying inside the 95% band at ALL depths")
    print(f"    = {whole95 * 100:.2f}%  (nominal 95%)")
    print(f"  fraction lying inside the 68% band at ALL depths = {whole68 * 100:.2f}%")
    print("Read a figure with a 95% band as 'each depth is covered 95% of the")
    print("time': the chance that the whole curve is inside the band is far")
    print("smaller. To make a simultaneous 95% band, widen it:")
    sd_curve = ens.std(axis=0, ddof=1)
    dev = np.abs(fresh - mean_curve[None, :]) / sd_curve[None, :]
    kmax = np.quantile(dev.max(axis=1), 0.95)
    k_point = 1.959963984540054
    print(f"    scale factor for a pointwise 95% band : k = {k_point:.4f}")
    print(f"    scale factor for a simultaneous 95% band: k = {kmax:.3f} "
          f"({kmax / k_point:.2f}x wider)")
    print(f"    at z = 20 km that is a band of width "
          f"{2 * kmax * sd_curve[i]:.3f} km/s against "
          f"{2 * k_point * sd_curve[i]:.3f} km/s pointwise")
    print("Reporting a pointwise band and describing it as a simultaneous one is")
    print("the commonest over-claim in an uncertainty figure. Say which it is.")

    section("4. A skewed quantity of interest: equal-tailed versus HPD")
    # (a) a mildly skewed case from the ensemble itself.
    j = slice(int(np.argmin(np.abs(Z - 19.0))), int(np.argmin(np.abs(Z - 21.0))))
    v_layer = ens[:, j].mean(axis=1)
    h = 2.0                                     # layer thickness, km
    twt = 2.0 * h / v_layer                     # two-way travel time, s
    lo_eq, hi_eq = np.quantile(twt, [0.025, 0.975])
    h0, h1, w_hpd = hpd_interval(twt)
    print("  (a) layer travel time from the ensemble, h = 2.0 km:")
    print(f"      mean interval velocity {v_layer.mean():.4f} km/s; "
          f"t = 2h/v")
    print(f"      mean {twt.mean():.5f} s, median {np.median(twt):.5f} s, "
          f"mean - median = {twt.mean() - np.median(twt):+.5f} s")
    print(f"      95% equal-tailed = [{lo_eq:.5f}, {hi_eq:.5f}] s, "
          f"width {hi_eq - lo_eq:.5f} s")
    print(f"      95% HPD          = [{h0:.5f}, {h1:.5f}] s, width {w_hpd:.5f} s")
    print(f"      HPD is {(hi_eq - lo_eq) / w_hpd:.4f}x narrower")
    print("      The skew here is mild, so the two intervals nearly coincide. That")
    print("      is a measurement, not a licence to use either one silently.")
    # (b) a strongly skewed case, stated explicitly.
    a_log = 0.6                                  # lognormal log-standard-deviation
    v_ln = 6.2 * np.exp(a_log * RNG.standard_normal(2_000_000) - 0.5 * a_log ** 2)
    t_ln = 2.0 * h / v_ln
    lo_eq2, hi_eq2 = np.quantile(t_ln, [0.025, 0.975])
    g0, g1, w_hpd2 = hpd_interval(t_ln)
    skew = float(((t_ln - t_ln.mean()) ** 3).mean() / t_ln.std() ** 3)
    print("\n  (b) a strongly skewed SYNTHETIC case: v lognormal with")
    print(f"      log-standard-deviation {a_log} (coefficient of variation "
          f"{np.sqrt(np.exp(a_log ** 2) - 1):.2f})")
    print(f"      mean {t_ln.mean():.4f} s, median {np.median(t_ln):.4f} s, "
          f"skewness {skew:.2f}")
    print(f"      sd = {t_ln.std(ddof=1):.4f} s, so mean + 2 sd = "
          f"{t_ln.mean() + 2 * t_ln.std(ddof=1):.4f} s and mean - 2 sd = "
          f"{t_ln.mean() - 2 * t_ln.std(ddof=1):+.4f} s")
    print(f"      95% equal-tailed = [{lo_eq2:.4f}, {hi_eq2:.4f}] s, "
          f"width {hi_eq2 - lo_eq2:.4f} s")
    print(f"      95% HPD          = [{g0:.4f}, {g1:.4f}] s, width {w_hpd2:.4f} s")
    print(f"      HPD is {(hi_eq2 - lo_eq2) / w_hpd2:.3f}x narrower")
    print("      A symmetric mean +/- 2 sd bar would extend below zero, which is")
    print("      impossible for a travel time. Whenever the posterior is skewed,")
    print("      a symmetric bar is not merely conservative or narrow: it is the")
    print("      wrong shape, and it can report an unphysical value.")

    section("5. Overlapping bands are not evidence that the models agree")
    # Two SYNTHETIC models for the same profile: constant velocity, and a
    # constant-gradient model. Their bands overlap everywhere.
    # constant-velocity model: one uncertain speed, the same at every depth
    ens_const = ens.mean() + 0.15 * RNG.standard_normal((5000, 1))
    ens_grad = ens
    ov = np.mean((np.percentile(ens_const, 2.5, axis=0)
                  <= np.percentile(ens_grad, 97.5, axis=0)) &
                 (np.percentile(ens_grad, 2.5, axis=0)
                  <= np.percentile(ens_const, 97.5, axis=0)))
    print(f"  a constant-velocity model and a gradient model: their 95% bands")
    print(f"  overlap at {ov * 100:.1f}% of depths")
    # Evidence: a SYNTHETIC data set of 12 picks with tiny noise.
    xd = np.linspace(2.0, 38.0, 12)
    yd = V0 + GRAD * xd + 0.15 * RNG.standard_normal(xd.size)
    s2 = 0.15 ** 2
    logev_grad = -0.5 * np.sum((yd - (V0 + GRAD * xd)) ** 2) / s2
    logev_const = -0.5 * np.sum((yd - yd.mean()) ** 2) / s2
    bf = np.exp(np.clip(logev_grad - logev_const, -700, 700))
    print(f"  a SYNTHETIC data set of {xd.size} picks with sigma = {np.sqrt(s2):.2f} km/s")
    print(f"  gives log10 Bayes factor (gradient vs constant) = "
          f"{(logev_grad - logev_const) / np.log(10):.2f}")
    print(f"  while the bands still overlap at {ov * 100:.1f}% of depths")
    print("Overlap is a statement about marginal widths at each depth. It cannot")
    print("express the fact that the two models are separated by a consistent,")
    print("small offset across many depths, and it cannot be read as evidence for")
    print("or against either model. Evidence comes from the likelihood, not from")
    print("the picture.")

    section("6. Reporting checklist")
    print("  1. Say which interval: pointwise or simultaneous, and the width.")
    print("  2. State the prior and likelihood the ensemble came from.")
    print("  3. Say whether the ensemble is posterior samples or prior samples.")
    print("  4. Never plot a band without the ensemble size and the number of")
    print("     effective samples behind it.")
    print("  5. Distinguish epistemic spread from aleatory spread on the figure.")
    print("  6. Report the quantity of interest and its transform: a band on v is")
    print("     not a band on 1/v, and the mean does not transform.")


if __name__ == "__main__":
    main()
