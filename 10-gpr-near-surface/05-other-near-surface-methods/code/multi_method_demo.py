#!/usr/bin/env python3
"""Integrating near-surface methods: joint inversion of water content from an
electrical and a thermal measurement, the narrowing it buys, the Monte Carlo
uncertainty of the result, and the material degeneracy that survives.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multi_method_demo.py

Everything here is SYNTHETIC.  The petrophysical relations, their exponents, the
material properties, the water contents and the measurement uncertainties are
chosen teaching values, not calibrations and not site parameters.

Contents
--------
1. Rock-physics transforms and the synthetic "observed" data.
2. Inversion from the electrical measurement alone: what it admits.
3. Joint inversion with the thermal measurement: the admissible set and its size.
4. Monte Carlo error propagation and the theta-sigma_w correlation.
5. The degeneracy that survives: fresh water in a porous soil versus saline water
   in a tight one.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

PHI = 0.45          # porosity, teaching value
M_EXP = 1.5         # Archie-type exponent, teaching value
KS = 3.0            # mineral thermal conductivity, W/m/K, teaching value
KW = 0.60           # water thermal conductivity, W/m/K
KA = 0.025          # air thermal conductivity, W/m/K
THETA_TRUE = 0.20   # volumetric water content
SIGMA_W_TRUE = 0.25  # pore-water conductivity, S/m
SIGMA_REL_ERR = 0.05   # 5% one-sigma error on the conductivity reading
K_REL_ERR = 0.03       # 3% one-sigma error on the thermal reading


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def sigma_of(theta, sigma_w, m=M_EXP):
    """Archie-type teaching relation: bulk conductivity from water content.

    Not a published calibration: sigma = sigma_w * theta^m with m a teaching
    exponent, linear in the pore-water conductivity by construction.
    """
    return sigma_w * theta ** m


def k_of(theta, phi=PHI, ks=KS):
    """Geometric-mean mixing model for thermal conductivity."""
    return ks ** (1.0 - phi) * KW ** theta * KA ** (phi - theta)


def main():
    section("1. Rock-physics transforms and the synthetic data")
    sigma_true = sigma_of(THETA_TRUE, SIGMA_W_TRUE)
    k_true = k_of(THETA_TRUE)
    print(f"  teaching model: phi = {PHI:.2f}, m = {M_EXP:.2f}, ks = {KS:.2f} W/m/K,")
    print(f"  kw = {KW:.2f} W/m/K, ka = {KA:.3f} W/m/K")
    print(f"  truth: theta = {THETA_TRUE:.3f}, sigma_w = {SIGMA_W_TRUE:.3f} S/m")
    print(f"  forward: sigma = {sigma_true:.5f} S/m ({sigma_true * 1e3:.2f} mS/m), "
          f"k = {k_true:.4f} W/m/K")
    sigma_obs = sigma_true * (1.0 + SIGMA_REL_ERR * RNG.standard_normal())
    k_obs = k_true * (1.0 + K_REL_ERR * RNG.standard_normal())
    print(f"  synthetic observation: sigma = {sigma_obs:.5f} S/m, k = {k_obs:.4f} W/m/K")
    print(f"  stated one-sigma errors: {SIGMA_REL_ERR * 100:.1f}% and "
          f"{K_REL_ERR * 100:.1f}%")
    print(f"  sensitivity dk/dtheta at the truth = "
          f"{k_true * np.log(KW / KA):.4f} W/m/K per unit theta")

    section("2. Inversion from the electrical measurement alone")
    sigma_prior = (0.05, 1.00)      # S/m, teaching prior on pore-water conductivity
    print(f"  with sigma known and sigma_w unknown, the reading constrains only the")
    print(f"  product sigma_w * theta^m.  Over the prior sigma_w in "
          f"[{sigma_prior[0]:.2f}, {sigma_prior[1]:.2f}] S/m:")
    print("     sigma_w (S/m)   theta from sigma alone")
    thetas = []
    for sw in (0.05, 0.10, 0.25, 0.50, 1.00):
        th = (sigma_obs / sw) ** (1.0 / M_EXP)
        print(f"     {sw:14.2f}   {th:23.4f}")
        thetas.append(th)
    th_lo, th_hi = min(thetas), max(thetas)
    th_hi = min(th_hi, PHI)
    print(f"  admissible theta range: {th_lo:.3f} to {th_hi:.3f} "
          f"(width {th_hi - th_lo:.3f}, factor {(th_hi) / th_lo:.1f})")
    print("  The electrical reading alone does not measure water content; it measures")
    print("  the product of water content and pore-water conductivity.")

    section("3. Joint inversion with the thermal measurement")
    theta_grid = np.linspace(0.01, 0.45, 2000)
    n_chi = 0
    chi_sigma = ((sigma_of(theta_grid, SIGMA_W_TRUE) - sigma_obs)
                 / (SIGMA_REL_ERR * sigma_obs)) ** 2
    chi_k = ((k_of(theta_grid) - k_obs) / (K_REL_ERR * k_obs)) ** 2
    # single-method: theta is unknown, so chi_sigma is evaluated along the
    # best-fitting sigma_w for each theta
    sw_best = sigma_obs / theta_grid ** M_EXP
    ok = (sw_best >= sigma_prior[0]) & (sw_best <= sigma_prior[1])
    chi1 = np.where(ok, 0.0, np.inf)
    admissible = theta_grid[chi1 < 1.0]
    print("  The thermal reading constrains theta on its own: inverting k for theta")
    print(f"  gives a best value and a range.  With a {K_REL_ERR * 100:.0f}% error on k:")
    from scipy.optimize import brentq
    th_fit = brentq(lambda t: k_of(t) - k_obs, 0.001, 0.449)
    th_lo_k = brentq(lambda t: k_of(t) - (k_obs - K_REL_ERR * k_obs), 0.001, th_fit)
    th_hi_k = brentq(lambda t: k_of(t) - (k_obs + K_REL_ERR * k_obs), th_fit, 0.449)
    print(f"    theta = {th_fit:.4f}  ({th_fit - THETA_TRUE:+.4f} against the truth)")
    sig_th = 0.5 * (th_hi_k - th_lo_k)
    print(f"    one-sigma range from k alone: {th_fit:.4f} +/- {sig_th:.4f} "
          f"(the endpoints of the w+/-1 sigma k interval span {th_hi_k - th_lo_k:.4f})")
    print(f"    whole range from sigma alone: {admissible.min():.4f} to "
          f"{admissible.max():.4f} (width {admissible.max() - admissible.min():.4f})")
    print(f"  the thermal measurement narrows the admissible water content by a factor "
          f"{(admissible.max() - admissible.min()) / (2.0 * sig_th):.1f}")
    sw_fit = sigma_obs / th_fit ** M_EXP
    sw_err = sw_fit * np.sqrt((SIGMA_REL_ERR) ** 2
                              + (M_EXP * sig_th / th_fit) ** 2)
    print(f"  the pore-water conductivity then follows from the electrical reading:")
    print(f"    sigma_w = {sw_fit:.4f} +/- {sw_err:.4f} S/m against the truth "
          f"{SIGMA_W_TRUE:.3f} S/m")
    print(f"  (that error is dominated by the {M_EXP:.1f}-fold amplification of the "
          f"theta error through sigma_w = sigma/theta^m)")

    section("4. Monte Carlo error propagation")
    n_mc = 20000
    sig_mc = sigma_obs * (1.0 + SIGMA_REL_ERR * RNG.standard_normal(n_mc))
    k_mc = k_obs * (1.0 + K_REL_ERR * RNG.standard_normal(n_mc))
    theta_mc = np.array([brentq(lambda t: k_of(t) - kk, 0.001, 0.449) for kk in k_mc[:2000]])
    sw_mc = sig_mc[:2000] / theta_mc ** M_EXP
    print(f"  {n_mc} trials (first 2000 shown in the statistics below):")
    print(f"    theta   = {theta_mc.mean():.4f} +/- {theta_mc.std(ddof=1):.4f} "
          f"({theta_mc.std(ddof=1) / theta_mc.mean() * 100:.2f}%)")
    print(f"    sigma_w = {sw_mc.mean():.4f} +/- {sw_mc.std(ddof=1):.4f} "
          f"({sw_mc.std(ddof=1) / sw_mc.mean() * 100:.2f}%)")
    corr = np.corrcoef(theta_mc, sw_mc)[0, 1]
    print(f"    correlation of the two estimates = {corr:+.3f}")
    print("  The correlation is strongly negative: a lower water content needs a more")
    print("  conductive pore water to explain the same reading.  The joint inversion")
    print("  returns a line of acceptable pairs, not an isolated point.")

    section("5. The degeneracy that survives: material versus water content")
    print("  the same two readings are fitted by different (phi, ks, theta, sigma_w):")
    print("    phi    ks (W/m/K)   theta    sigma_w (S/m)   k model   sigma model")
    rows = [(0.45, 3.00, 0.200, 0.2500), (0.35, 3.00, 0.049, 2.0610)]
    # second row recomputed for consistency below
    k_alt = k_of(0.0494, phi=0.35, ks=3.0)
    rows[1] = (0.35, 3.00, 0.0494, sigma_obs / 0.0494 ** M_EXP)
    for phi, ks, th, sw in rows:
        print(f"    {phi:5.2f}   {ks:11.2f}   {th:6.3f}   {sw:14.4f}   "
              f"{k_of(th, phi, ks):8.4f}   {sigma_of(th, sw):11.5f}")
    print("  Both rows reproduce the measurements within their uncertainties.  One is")
    print("  fresh water in a porous soil, the other saline water in a tight one.  The")
    print("  geophysics cannot separate them; the porosity or a water sample can.")
    theta_for_alt = 0.0494
    print(f"  the water content differs by a factor {THETA_TRUE / theta_for_alt:.1f} "
          f"between the two solutions, and the pore-water conductivity by "
          f"{rows[1][3] / SIGMA_W_TRUE:.1f}")

    section("6. What was measured, inferred and assumed")
    print("  measured : an apparent conductivity and a thermal conductivity, with")
    print("             their stated uncertainties.")
    print("  inferred : water content and pore-water conductivity, as a set rather")
    print("             than a point, plus the negative correlation between them.")
    print("  assumed  : the porosity, the mineral thermal conductivity, the Archie")
    print("             exponent m, and the mixing model.  Each one is a number that")
    print("             the geophysics did not measure, and the last section shows what")
    print("             happens when one of them is wrong.")


if __name__ == "__main__":
    main()
