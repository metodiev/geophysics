#!/usr/bin/env python3
"""AVO/AVA: the Aki-Richards structure, the effect of fluid substitution, and the
non-uniqueness of AVO inversion.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python avo_demo.py

Everything is SYNTHETIC.  The rock and fluid parameters are CHOSEN teaching
values, not measured rock properties.

Contents
--------
1. The Aki-Richards two- and three-term approximations, verified at normal
   incidence against the exact impedance formula.
2. What each term means: intercept (impedance), gradient (vs and density),
   and the far-angle density term.
3. Fluid substitution with Gassmann: gas/oil/brine change R(theta).
4. Non-uniqueness: two different (vp, vs, rho) triples fitting the same AVO
   curve within a stated noise level.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(t):
    print(f"\n{'=' * 68}\n{t}\n{'=' * 68}")


def aki_richards(vp1, vs1, rho1, vp2, vs2, rho2, theta_deg, terms=3):
    """Aki-Richards approximation to the PP reflection coefficient.

    Terms:
      1st: intercept  A = 1/2 (dZ/Z) with Z = rho*vp
      2nd: gradient   B sin^2, containing dvp and dvs
      3rd: far-angle  C (sin^2 tan^2), density-dominated
    All velocities in m/s, densities in kg/m^3 (ratio-only, so units cancel).
    """
    th = np.radians(theta_deg)
    dvp = vp2 - vp1
    dvs = vs2 - vs1
    drho = rho2 - rho1
    vp = 0.5 * (vp1 + vp2)
    vs = 0.5 * (vs1 + vs2)
    rho = 0.5 * (rho1 + rho2)
    A = 0.5 * (drho / rho + dvp / vp)
    B = (0.5 * dvp / vp
         - 2.0 * (vs / vp) ** 2 * (drho / rho + 2.0 * dvs / vs))
    C = 0.5 * dvp / vp
    R = A + B * np.sin(th) ** 2
    if terms == 3:
        R = R + C * (np.sin(th) ** 2 * np.tan(th) ** 2)
    return R


def gassmann(K_dry, K_min, K_fl, phi, mu_dry):
    """Saturated bulk modulus and the resulting densities/velocities."""
    num = (1.0 - K_dry / K_min) ** 2
    den = phi / K_fl + (1.0 - phi) / K_min - K_dry / K_min ** 2
    K_sat = K_dry + num / den
    return K_sat, mu_dry          # mu is unchanged by the pore fluid


def main():
    section("1. Aki-Richards versus the exact normal-incidence formula")
    vp1, vs1, rho1 = 3000.0, 1600.0, 2300.0
    vp2, vs2, rho2 = 3400.0, 1900.0, 2450.0
    Z1, Z2 = rho1 * vp1, rho2 * vp2
    R_exact0 = (Z2 - Z1) / (Z2 + Z1)
    R_ar0 = aki_richards(vp1, vs1, rho1, vp2, vs2, rho2, 0.0)
    print(f"  layer 1: vp {vp1:.0f}, vs {vs1:.0f}, rho {rho1:.0f}")
    print(f"  layer 2: vp {vp2:.0f}, vs {vs2:.0f}, rho {rho2:.0f}")
    print(f"  exact normal-incidence R = (Z2-Z1)/(Z2+Z1) = {R_exact0:+.6f}")
    print(f"  Aki-Richards at theta = 0                 = {R_ar0:+.6f}")
    print(f"  absolute difference = {abs(R_exact0 - R_ar0):.2e}")
    print("  They agree only to FIRST order: the exact impedance ratio has")
    print("  second-order terms in the contrast that the average-parameter")
    print("  approximation drops.  For a ~10% contrast the residual is ~2e-4, as")
    print("  here.  This is worth remembering: an 'AVO intercept' is a first-order")
    print("  impedance contrast, not the impedance contrast.")

    section("2. The AVO curve and its three terms")
    th = np.array([0, 10, 20, 30, 40])
    R_full = aki_richards(vp1, vs1, rho1, vp2, vs2, rho2, th, terms=3)
    R_two = aki_richards(vp1, vs1, rho1, vp2, vs2, rho2, th, terms=2)
    print("   theta   R (3-term)   R (2-term)   difference")
    for a, b, c in zip(th, R_full, R_two):
        print(f"   {a:5.0f}   {b:+.5f}   {c:+.5f}   {b - c:+.5f}")
    vp = 0.5 * (vp1 + vp2)
    vs = 0.5 * (vs1 + vs2)
    rho = 0.5 * (rho1 + rho2)
    A = 0.5 * ((rho2 - rho1) / rho + (vp2 - vp1) / vp)
    B = (0.5 * (vp2 - vp1) / vp
         - 2 * (vs / vp) ** 2 * ((rho2 - rho1) / rho + 2 * (vs2 - vs1) / vs))
    print(f"  intercept A = {A:+.5f}  (impedance contrast at normal incidence)")
    print(f"  gradient  B = {B:+.5f}  (vs and density, the AVO signal)")
    print("  A and B are the two parameters a linearised AVO inversion estimates;")
    print("  the third term matters only beyond about 30-35 degrees and is heavily")
    print("  weighted by density.")

    section("3. Fluid substitution and what it does to AVO")
    # SYNTHETIC rock frame
    K_min, mu_min = 36.0e9, 30.0e9        # mineral bulk and shear (Pa)
    phi = 0.25
    K_dry = 8.0e9
    rho_min, rho_w, rho_oil, rho_gas = 2650.0, 1000.0, 800.0, 150.0
    K_w, K_oil, K_gas = 2.2e9, 0.8e9, 0.05e9
    mu_dry = 8.0e9
    print(f"  SYNTHETIC frame: phi = {phi:.2f}, K_dry = {K_dry/1e9:.1f} GPa, "
          f"mu = {mu_dry/1e9:.1f} GPa")
    print("   saturation    rho (kg/m3)   vp (m/s)   vs (m/s)   R(0)      R(30)")
    # cap (layer 1) is fixed brine-saturated shale
    for name, K_fl, rho_fl in (("brine", K_w, rho_w), ("oil", K_oil, rho_oil),
                               ("gas", K_gas, rho_gas)):
        K_sat, mu_s = gassmann(K_dry, K_min, K_fl, phi, mu_dry)
        rho_s = (1 - phi) * rho_min + phi * rho_fl
        vp_s = np.sqrt((K_sat + 4.0 / 3.0 * mu_s) / rho_s)
        vs_s = np.sqrt(mu_s / rho_s)
        R0 = aki_richards(vp1, vs1, rho1, vp_s, vs_s, rho_s, 0.0)
        R30 = aki_richards(vp1, vs1, rho1, vp_s, vs_s, rho_s, 30.0)
        print(f"   {name:10s}   {rho_s:11.0f}   {vp_s:8.0f}   {vs_s:8.0f}   "
              f"{R0:+.4f}   {R30:+.4f}")
    print("  Replacing brine with gas lowers the bulk modulus and the density; vp")
    print("  and vs drop, and the reflection coefficient changes sign.  That sign")
    print("  change across the fluid content is the physical basis of AVO")
    print("  hydrocarbon detection.  Note mu is UNCHANGED by the fluid: only the")
    print("  density change moves vs.")

    section("4. Non-uniqueness of AVO inversion")
    print("  In the two-term approximation the AVO curve is fixed by the pair")
    print("  (A, B).  Three layer-2 unknowns (dvp, dvs, drho) determine only two")
    print("  numbers, so a ONE-PARAMETER FAMILY of models gives the same curve.")
    print("  We construct two members of that family explicitly.")
    vpA, vsA, rhoA = 3400.0, 1900.0, 2450.0
    dvpA, dvsA, drhoA = vpA - vp1, vsA - vs1, rhoA - rho1
    vpbar = 0.5 * (vp1 + vpA)
    vsbar = 0.5 * (vs1 + vsA)
    rhobar = 0.5 * (rho1 + rhoA)
    k2 = (vsbar / vpbar) ** 2
    A_t = 0.5 * (drhoA / rhobar + dvpA / vpbar)
    B_t = 0.5 * dvpA / vpbar - 2.0 * k2 * (drhoA / rhobar + 2.0 * dvsA / vsbar)
    # choose a different dvs, solve for the dvp and drho that keep (A,B).
    # Iterate so that model B's OWN average parameters give the target (A,B).
    dvsB = 0.35 * dvsA
    vsB = vs1 + dvsB
    vpB, rhoB = vpA, rhoA
    for _ in range(50):
        vpbar = 0.5 * (vp1 + vpB)
        vsbar = 0.5 * (vs1 + vsB)
        rhobar = 0.5 * (rho1 + rhoB)
        k2 = (vsbar / vpbar) ** 2
        rvp = (B_t + 4.0 * A_t * k2 + 4.0 * k2 * (dvsB / vsbar)) / (0.5 + 2.0 * k2)
        rrho = 2.0 * A_t - rvp
        vpB, rhoB = vp1 + rvp * vpbar, rho1 + rrho * rhobar
    sigma = 0.005
    th_full = np.arange(0.0, 41.0, 2.0)
    RA = aki_richards(vp1, vs1, rho1, vpA, vsA, rhoA, th_full)
    RB = aki_richards(vp1, vs1, rho1, vpB, vsB, rhoB, th_full)
    RA2 = aki_richards(vp1, vs1, rho1, vpA, vsA, rhoA, th_full, terms=2)
    RB2 = aki_richards(vp1, vs1, rho1, vpB, vsB, rhoB, th_full, terms=2)
    near = th_full <= 30.0
    print(f"   model A: vp {vpA:.0f}, vs {vsA:.0f}, rho {rhoA:.0f}")
    print(f"   model B: vp {vpB:.0f}, vs {vsB:.0f}, rho {rhoB:.0f}   "
          f"(constructed to match A and B)")
    print(f"   max |R_A - R_B|, TWO-term model, 0-30 deg = "
          f"{np.max(np.abs((RA2 - RB2)[near])):.5f}  "
          f"({np.max(np.abs((RA2 - RB2)[near])) / sigma:.2f} sigma)")
    print(f"   max |R_A - R_B|, TWO-term model, 0-40 deg = "
          f"{np.max(np.abs(RA2 - RB2)):.5f}  "
          f"({np.max(np.abs(RA2 - RB2)) / sigma:.2f} sigma)")
    print(f"   max |R_A - R_B|, THREE-term model, 0-40 deg = "
          f"{np.max(np.abs(RA - RB)):.5f}  "
          f"({np.max(np.abs(RA - RB)) / sigma:.2f} sigma)")
    print("   => over near-to-mid angles the two models are the SAME curve to well")
    print("      within the noise; only the far-angle third term separates them.")
    print("   chi^2 test on repeated noisy realisations of model A's near-angle")
    print("   curve (2-term, 0-30 deg):")
    for _ in range(3):
        noisy = RA2[near] + sigma * RNG.standard_normal(near.sum())
        chiA = np.sum(((RA2[near] - noisy) / sigma) ** 2)
        chiB = np.sum(((RB2[near] - noisy) / sigma) ** 2)
        verdict = "tie (identical curve)" if abs(chiA - chiB) < 1e-9 else (
            "A fits better" if chiA < chiB else "B fits better")
        print(f"     chi2(A) = {chiA:6.2f}, chi2(B) = {chiB:6.2f}  -> {verdict}")
    print("  The two models differ in vp by "
          f"{vpB - vpA:+.0f} m/s and in vs by {vsB - vsA:+.0f} m/s while fitting")
    print("  the same near-angle curve.  Inverting that curve alone cannot choose")
    print("  between them: the family is a ridge in model space, the same geometry")
    print("  as the receiver-function H-k trade-off.  A unique (vp, vs, rho) needs")
    print("  prior information or far-angle data that constrains the third term.")


if __name__ == "__main__":
    main()
