#!/usr/bin/env python3
"""Impacts, exposure and risk: expected annual damage from a damage function
integrated over a hazard distribution, a multiplicative decomposition of a
change in risk, the shift of a design-event return period, compound flooding
under independence and correlation, and uncertainty propagation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python impacts_and_risk_demo.py

Everything is SYNTHETIC.  The hazard distribution, the damage function, the
exposure growth and the monetary values below are chosen teaching values in
arbitrary monetary units (MU).  No real asset value, loss, insurance figure or
economic estimate is quoted, and no policy or cost figure is used.

Contents
--------
1. A hazard distribution and a damage function; expected fractional damage.
2. Expected annual damage (EAD) and a multiplicative decomposition into hazard,
   exposure and vulnerability factors.
3. The design event: how a hazard shift changes the return period of a fixed
   level.
4. Compound flooding: joint exceedance under independence and under correlation,
   and the effect of a sea-level shift of the surge marginal.
5. Uncertainty propagation by Monte Carlo, reported as quantiles.
"""

import numpy as np
from scipy import stats

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC risk model (chosen, not measured) ----------------------------
H_MEDIAN = 1.0        # m, median annual maximum water depth
H_SIGMA = 0.40        # dimensionless, lognormal shape of the hazard
H0 = 0.5              # m, damage threshold (no damage below)
H1 = 3.0              # m, depth of full damage
ALPHA = 1.5           # dimensionless, damage-function curvature
EXPOSURE_0 = 1000.0   # MU, value of the exposed assets at t = 0
GROWTH = 0.02         # per year, nominal exposure growth
HORIZON = 30          # years
HAZARD_SHIFT = 1.15   # dimensionless, multiplicative shift of the hazard median
H0_ADAPTED = 0.7      # m, damage threshold after adaptation

# Gauss-Hermite nodes for integration over the lognormal hazard
_ZNODES, _ZWEIGHTS = np.polynomial.hermite_e.hermegauss(160)
_ZWEIGHTS = _ZWEIGHTS / np.sqrt(2.0 * np.pi)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def damage_fraction(h, h0=H0, h1=H1, alpha=ALPHA):
    """Fractional damage in [0, 1] as a function of hazard depth h (m)."""
    x = np.clip((np.asarray(h, dtype=float) - h0) / (h1 - h0), 0.0, 1.0)
    return x ** alpha


def expected_damage_fraction(medians, sigma=H_SIGMA, h0=H0, h1=H1, alpha=ALPHA):
    """E[damage] over lognormal hazards with the stated medians (scalar or array)."""
    medians = np.atleast_1d(np.asarray(medians, dtype=float))
    h = medians[:, None] * np.exp(sigma * _ZNODES)[None, :]
    h0v = np.asarray(h0, dtype=float)
    if h0v.ndim == 1 and h0v.size > 1:
        h0v = h0v[:, None]
    vals = damage_fraction(h, h0=h0v, h1=h1, alpha=alpha)
    out = vals @ _ZWEIGHTS
    return float(out[0]) if out.size == 1 else out


def ead(median, exposure, **kw):
    """Expected annual damage in MU."""
    return exposure * expected_damage_fraction(median, **kw)


def main():
    section("1. Hazard, vulnerability and expected damage")
    print("SYNTHETIC hazard: annual maximum flood depth lognormal with median")
    print(f"  {H_MEDIAN:.2f} m and log-sigma {H_SIGMA:.2f}")
    print(f"SYNTHETIC damage function: d(h) = [clip((h-{H0:.1f})/({H1:.1f}-{H0:.1f}),"
          f"0,1)]^{ALPHA:.1f}")
    print("   h (m)   d(h)   exceedance prob.")
    for h in (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0):
        pr = stats.lognorm.sf(h, s=H_SIGMA, scale=H_MEDIAN)
        print(f"  {h:6.1f}   {damage_fraction(h):4.2f}   {pr:13.4f}")
    e0 = expected_damage_fraction(H_MEDIAN)
    print(f"  expected fractional damage E[d] = {e0:.4f} (dimensionless)")
    print(f"  with exposure {EXPOSURE_0:.0f} MU, EAD = {EXPOSURE_0 * e0:.1f} MU/yr")

    section("2. Decomposing a change in risk into three factors")
    growth_factor = (1.0 + GROWTH) ** HORIZON
    exposure_later = EXPOSURE_0 * growth_factor
    base = ead(H_MEDIAN, EXPOSURE_0)
    hazard_only = ead(H_MEDIAN * HAZARD_SHIFT, EXPOSURE_0)
    hazard_exposure = ead(H_MEDIAN * HAZARD_SHIFT, exposure_later)
    all_three = ead(H_MEDIAN * HAZARD_SHIFT, exposure_later, h0=H0_ADAPTED)
    print(f"  exposure growth: (1+{GROWTH:.2f})^{HORIZON} = {growth_factor:.3f}")
    print("  scenario                                   EAD (MU/yr)   factor vs base")
    for name, val in (
        ("S0 baseline", base),
        ("S1 hazard shift only", hazard_only),
        ("S2 + exposure growth", hazard_exposure),
        ("S3 + adaptation (h0 -> 0.7 m)", all_three),
    ):
        print(f"  {name:38s}  {val:10.1f}   {val / base:12.3f}x")
    print(f"  hazard factor alone    : {hazard_only / base:.3f}x")
    print(f"  exposure factor alone  : {growth_factor:.3f}x")
    print(f"  product (S1/S0 x growth): {hazard_only / base * growth_factor:.3f}x, "
          f"measured S2/S0 = {hazard_exposure / base:.3f}x")
    print(f"  adaptation factor      : {all_three / hazard_exposure:.3f}x")
    print("  The decomposition is multiplicative and exact here because each")
    print("  factor was applied in turn.  Make the hazard shift depend on the")
    print("  damage threshold and the product no longer separates the effects.")
    print("  The interaction term is real; a three-way decomposition is a")
    print("  modelling choice, not a property of the system.")

    section("3. The design event and its return period")
    t_design = stats.lognorm.ppf(0.98, s=H_SIGMA, scale=H_MEDIAN)
    p_after = stats.lognorm.sf(t_design, s=H_SIGMA, scale=H_MEDIAN * HAZARD_SHIFT)
    print(f"  baseline 1-in-50 depth            : {t_design:.3f} m")
    print(f"  after a x{HAZARD_SHIFT:.2f} shift of the hazard median:")
    print(f"    P(h >= design level)            : {p_after:.4f} per year")
    print(f"    its new return period           : {1.0 / p_after:.1f} years")
    print(f"    exceedance frequency ratio      : {p_after / 0.02:.2f}x "
          f"(= 50 / new return period)")
    print("  An asset designed to the old standard is no longer designed to the")
    print("  standard it was built for, even though nothing about the asset")
    print("  changed.  That is a statement about the hazard distribution, not")
    print("  about the asset.")

    section("4. Compound flooding: independence versus correlation")
    r_med, s_med = 1.0, 0.8          # m, medians of river and surge
    r_sig, s_sig = 0.35, 0.30        # log-sigmas
    r_thr, s_thr = 2.0, 1.5          # exceedance thresholds, m
    zr = (np.log(r_thr) - np.log(r_med)) / r_sig
    zs = (np.log(s_thr) - np.log(s_med)) / s_sig
    print(f"  river discharge : lognormal median {r_med:.2f} m, log-sigma {r_sig:.2f}")
    print(f"  storm surge     : lognormal median {s_med:.2f} m, log-sigma {s_sig:.2f}")
    print(f"  thresholds: river {r_thr:.1f} m, surge {s_thr:.1f} m")
    print(f"  marginal exceedance probabilities: river {stats.norm.sf(zr):.4f}, "
          f"surge {stats.norm.sf(zs):.4f}")
    print("  rho     P(both)   P(either)   P(both)/P(either)")
    for rho in (0.0, 0.3, 0.6, 0.9):
        cov = np.array([[1.0, rho], [rho, 1.0]])
        mvn = stats.multivariate_normal(mean=[0.0, 0.0], cov=cov)
        phi2 = float(mvn.cdf([zr, zs]))
        p_both = 1.0 - stats.norm.cdf(zr) - stats.norm.cdf(zs) + phi2
        p_either = 1.0 - phi2
        print(f"  {rho:4.1f}   {p_both:.4f}   {p_either:.4f}   "
              f"{p_both / p_either:15.4f}")
    print("  independence UNDERSTATES the joint probability when the drivers")
    print("  are positively correlated, and the conditional fraction rises with")
    print("  the correlation.  Compound risk is a statement about dependence.")
    slr = 0.30      # m
    s_thr_eff = s_thr - slr
    zs2 = (np.log(s_thr_eff) - np.log(s_med)) / s_sig
    cov = np.array([[1.0, 0.6], [0.6, 1.0]])
    mvn = stats.multivariate_normal(mean=[0.0, 0.0], cov=cov)
    p_before = (1.0 - stats.norm.cdf(zr) - stats.norm.cdf(zs)
                + float(mvn.cdf([zr, zs])))
    p_after = (1.0 - stats.norm.cdf(zr) - stats.norm.cdf(zs2)
               + float(mvn.cdf([zr, zs2])))
    print(f"  a sea-level rise of {slr:.2f} m lowers the effective surge")
    print(f"  threshold to {s_thr_eff:.2f} m (dependence held at rho = 0.6):")
    print(f"    P(both) before = {p_before:.4f}")
    print(f"    P(both) after  = {p_after:.4f}")
    print(f"    ratio          = {p_after / p_before:.2f}x")
    print("  The change comes from moving the hazard marginal, not from")
    print("  changing the dependence; both matter and they are different.")

    section("5. Uncertainty propagation in the risk estimate")
    n_mc = 20000
    shift = RNG.uniform(1.0, 1.30, n_mc)
    growth = RNG.uniform(0.0, 0.04, n_mc)
    h0s = RNG.uniform(H0, H0 + 0.3, n_mc)
    exposure = EXPOSURE_0 * (1.0 + growth) ** HORIZON
    vals = exposure * expected_damage_fraction(H_MEDIAN * shift, h0=h0s)
    q = np.percentile(vals, [5, 25, 50, 75, 95])
    print(f"  {n_mc} Monte Carlo draws of (hazard shift 1.00-1.30, exposure")
    print(f"  growth 0-4%/yr, damage threshold {H0:.2f}-{H0 + 0.3:.2f} m)")
    print(f"  EAD quantiles (MU/yr): 5% {q[0]:.0f}  25% {q[1]:.0f}  "
          f"median {q[2]:.0f}  75% {q[3]:.0f}  95% {q[4]:.0f}")
    print(f"  the 5-95 range spans a factor {q[4] / q[0]:.2f}")
    print("  A single EAD number is a choice of three input distributions, not a")
    print("  measurement.  Report the inputs and the range, not the point.")


if __name__ == "__main__":
    main()
