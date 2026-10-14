#!/usr/bin/env python3
"""Reservoir characterisation: rock physics, the attribute trade-off, and the
Bayesian probability that a sand is a pay sand.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reservoir_characterisation_demo.py

Contents
--------
1. Gassmann fluid substitution on a critical-porosity sand: acoustic impedance
   and Vp/Vs for brine, oil and gas.
2. Attribute trade-off: (porosity, saturation) pairs with identical impedance.
3. Bayesian facies probability from two attributes, and the base-rate effect.
4. Net-to-gross averaging: the same impedance from different mixtures.
5. Scale: what one seismic resolution cell averages.

All models and numbers are SYNTHETIC teaching values: a chosen sand model with
chosen spreads.  The mineral and fluid constants quoted are standard textbook
values with units; no measured dataset is used.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard mineral and fluid constants (with units) -----------------------
K_QUARTZ = 36.6e9      # Pa, quartz bulk modulus
MU_QUARTZ = 45.0e9     # Pa, quartz shear modulus
RHO_QUARTZ = 2650.0    # kg/m^3
K_BRINE = 2.2e9        # Pa, brine bulk modulus
RHO_BRINE = 1000.0     # kg/m^3
K_OIL = 1.0e9          # Pa, oil bulk modulus
RHO_OIL = 800.0        # kg/m^3
K_GAS = 0.02e9         # Pa, gas bulk modulus at reservoir conditions
RHO_GAS = 200.0        # kg/m^3

# --- Chosen model parameters (SYNTHETIC) -------------------------------------
PHI_CRIT = 0.40        # critical porosity of the sand model
VP_SHALE, RHO_SHALE = 2800.0, 2450.0   # m/s, kg/m^3, chosen shale end member


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def fluid_properties(sw, shc, kind):
    """Wood's equation for the fluid bulk modulus and arithmetic density.

    Saturations are fractions of pore volume and are normalised internally.
    """
    k_hc, rho_hc = (K_GAS, RHO_GAS) if kind == "gas" else (K_OIL, RHO_OIL)
    tot = sw + shc
    sw, shc = sw / tot, shc / tot
    k_fl = 1.0 / (sw / K_BRINE + shc / k_hc)
    rho_fl = sw * RHO_BRINE + shc * rho_hc
    return k_fl, rho_fl


def saturated_velocities(phi, sw, shc, kind):
    """Critical-porosity dry moduli + Gassmann + density -> vp, vs, rho."""
    k_dry = K_QUARTZ * (1.0 - phi / PHI_CRIT)
    mu_dry = MU_QUARTZ * (1.0 - phi / PHI_CRIT)
    k_fl, rho_fl = fluid_properties(sw, shc, kind)
    num = (1.0 - k_dry / K_QUARTZ) ** 2
    den = phi / k_fl + (1.0 - phi) / K_QUARTZ - k_dry / K_QUARTZ ** 2
    k_sat = k_dry + num / den
    rho = (1.0 - phi) * RHO_QUARTZ + phi * rho_fl
    vp = np.sqrt((k_sat + 4.0 * mu_dry / 3.0) / rho)
    vs = np.sqrt(mu_dry / rho)
    return vp, vs, rho


def ai_vpvs(phi, sw, shc, kind):
    vp, vs, rho = saturated_velocities(phi, sw, shc, kind)
    return rho * vp, vp / vs


def main():
    section("1. Gassmann fluid substitution: impedance and Vp/Vs")
    print(f"quartz: K = {K_QUARTZ / 1e9:.1f} GPa, mu = {MU_QUARTZ / 1e9:.1f} GPa, "
          f"rho = {RHO_QUARTZ:.0f} kg/m^3")
    print(f"fluids: brine K = {K_BRINE / 1e9:.1f} GPa rho = {RHO_BRINE:.0f}; "
          f"oil K = {K_OIL / 1e9:.1f} GPa rho = {RHO_OIL:.0f}; "
          f"gas K = {K_GAS / 1e9:.2f} GPa rho = {RHO_GAS:.0f}")
    print("(K in GPa, rho in kg/m^3; the critical-porosity sand has "
          f"phi_c = {PHI_CRIT:.2f})")
    print("\n  fluid      phi    vp (km/s)   vs (km/s)   rho (g/cm^3)   "
          "AI (MRayl)   Vp/Vs")
    for kind, sw, shc in (("brine", 1.00, 0.00), ("oil", 0.25, 0.75),
                          ("gas", 0.25, 0.75)):
        for phi in (0.15, 0.20, 0.25):
            vp, vs, rho = saturated_velocities(phi, sw, shc, kind)
            ai, ratio = ai_vpvs(phi, sw, shc, kind)
            print(f"  {kind:6s}  {phi:5.2f}   {vp / 1000:8.2f}   {vs / 1000:8.2f}   "
                  f"{rho / 1000:11.3f}   {ai / 1e6:11.2f}   {ratio:6.3f}")
    vp_b, vs_b, rho_b = saturated_velocities(0.20, 1.0, 0.0, "gas")
    ai_b, r_b = ai_vpvs(0.20, 1.0, 0.0, "gas")
    ai_g, r_g = ai_vpvs(0.20, 0.25, 0.75, "gas")
    ai_o, r_o = ai_vpvs(0.20, 0.25, 0.75, "oil")
    print(f"\nat phi = 0.20: gas changes AI by {(ai_g - ai_b) / ai_b * 100:+.1f}% "
          f"and Vp/Vs by {(r_g - r_b) / r_b * 100:+.1f}%")
    print(f"              oil changes AI by {(ai_o - ai_b) / ai_b * 100:+.1f}% "
          f"and Vp/Vs by {(r_o - r_b) / r_b * 100:+.1f}%")

    section("2. Attribute trade-off: identical impedance, different rock")
    phis = np.linspace(0.05, 0.35, 121)
    sgs = np.linspace(0.0, 0.90, 91)
    AI = np.zeros((phis.size, sgs.size))
    RATIO = np.zeros_like(AI)
    for i, phi in enumerate(phis):
        for j, sg in enumerate(sgs):
            AI[i, j], RATIO[i, j] = ai_vpvs(phi, 1.0 - sg, sg, "gas")
    target = ai_g
    print(f"target: the pay sand of section 1, AI = {target / 1e6:.2f} MRayl "
          f"(phi = 0.20, Sg = 0.75)")
    print("how much does saturation alone move the impedance?")
    print(f"  AI(dry, phi = 0.20)   = {ai_b / 1e6:.2f} MRayl")
    print(f"  AI(gas, phi = 0.20)   = {ai_g / 1e6:.2f} MRayl  "
          f"({(ai_g - ai_b) / ai_b * 100:+.1f}%)")
    print("\n(porosity, saturation) pairs that match that impedance to 1%:")
    print("\n   phi     Sg      AI (MRayl)   Vp/Vs")
    idx = np.argwhere(np.abs(AI - target) / target < 0.01)
    step = max(1, len(idx) // 8)
    for i, j in idx[::step][:9]:
        print(f"  {phis[i]:5.2f}   {sgs[j]:4.2f}   {AI[i, j] / 1e6:10.2f}   "
              f"{RATIO[i, j]:6.3f}")
    spread = RATIO[idx[:, 0], idx[:, 1]]
    sg_span = (sgs[idx[:, 1]].min(), sgs[idx[:, 1]].max())
    print(f"\n{len(idx)} combinations match this impedance to 1%: porosity is")
    print(f"pinned to {phis[idx[:, 0]].min():.2f}-{phis[idx[:, 0]].max():.2f}, while "
          f"saturation is free over Sg = {sg_span[0]:.2f}-{sg_span[1]:.2f}.")
    print(f"Vp/Vs over that set spans {spread.min():.3f} to {spread.max():.3f}, a")
    print(f"spread of {(spread.max() - spread.min()) / spread.min() * 100:.1f}%.  That is")
    print("the fluid signal, and it is barely twice the 3% attribute noise assumed")
    print("in section 3: Vp/Vs constrains saturation, but weakly.  Impedance")
    print("answers porosity; Vp/Vs adds a little about fluid; neither is a")
    print("hydrocarbon detector.")

    section("3. Bayesian facies probability from two attributes")
    # SYNTHETIC facies model: pay sand (gas) and wet sand (brine), same porosity
    ai_pay, r_pay = ai_vpvs(0.22, 0.25, 0.75, "gas")
    ai_wet, r_wet = ai_vpvs(0.22, 1.0, 0.0, "gas")
    sd_ai = 0.05 * 0.5 * (ai_pay + ai_wet)
    sd_r = 0.03 * 0.5 * (r_pay + r_wet)
    print(f"pay sand: AI = {ai_pay / 1e6:.2f} MRayl, Vp/Vs = {r_pay:.3f}")
    print(f"wet sand: AI = {ai_wet / 1e6:.2f} MRayl, Vp/Vs = {r_wet:.3f}")
    print(f"attribute spreads: sigma_AI = {sd_ai / 1e6:.2f} MRayl, "
          f"sigma_VpVs = {sd_r:.3f} (chosen)")
    d1 = abs(ai_pay - ai_wet) / sd_ai
    d2 = np.hypot((ai_pay - ai_wet) / sd_ai, (r_pay - r_wet) / sd_r)
    print(f"\nseparation in standard deviations: AI alone {d1:.2f}, "
          f"AI + Vp/Vs jointly {d2:.2f}")

    def posterior(x_ai, x_r, prior_pay):
        def loglik(mu_ai, mu_r):
            return -0.5 * (((x_ai - mu_ai) / sd_ai) ** 2
                           + ((x_r - mu_r) / sd_r) ** 2)
        lp = np.log(prior_pay) + loglik(ai_pay, r_pay)
        lw = np.log(1.0 - prior_pay) + loglik(ai_wet, r_wet)
        m = np.maximum(lp, lw)
        return np.exp(lp - m) / (np.exp(lp - m) + np.exp(lw - m))

    print("\nposterior probability of pay for a given likelihood ratio:")
    print("   likelihood ratio   prior 0.50   prior 0.20   prior 0.05   prior 0.01")
    for lr in (1.0, 4.0, 10.0, 50.0, 200.0):
        row = [1.0 / (1.0 + (1.0 - p) / (lr * p)) for p in (0.50, 0.20, 0.05, 0.01)]
        print(f"  {lr:16.1f}   {row[0]:11.3f}   {row[1]:11.3f}   {row[2]:11.3f}   "
              f"{row[3]:11.3f}")
    print("The likelihood ratio is the data's contribution; the base rate is not")
    print("optional.  A 10:1 likelihood ratio sounds decisive and leaves a 0.05")
    print("base rate at 0.345 -- a two-to-one bet against paying off.")

    print("\nconfusion matrix from a synthetic population of 200000 prospects")
    print("(call 'pay' when the posterior exceeds the stated threshold):")
    print("   prior   threshold   called pay   true pos   false pos   precision   "
          "recall")
    for prior in (0.50, 0.20, 0.05):
        n = 200000
        is_pay = RNG.random(n) < prior
        ai_draw = np.where(is_pay,
                           ai_pay + sd_ai * RNG.standard_normal(n),
                           ai_wet + sd_ai * RNG.standard_normal(n))
        r_draw = np.where(is_pay,
                          r_pay + sd_r * RNG.standard_normal(n),
                          r_wet + sd_r * RNG.standard_normal(n))
        post = posterior(ai_draw, r_draw, prior)
        for thr in (0.50, 0.20):
            call = post > thr
            tp = np.sum(call & is_pay)
            fp = np.sum(call & ~is_pay)
            prec = tp / max(tp + fp, 1)
            rec = tp / max(np.sum(is_pay), 1)
            print(f"  {prior:6.2f}   {thr:9.2f}   {np.sum(call):10.0f}   "
                  f"{tp:9.0f}   {fp:10.0f}   {prec:9.3f}   {rec:6.3f}")
    print("Lowering the threshold raises recall and destroys precision: the")
    print("threshold is a cost decision, not a physical one (see 11-01-03).")

    section("4. Net-to-gross averaging: the same impedance, different mixtures")
    print(f"shale end member (chosen): vp = {VP_SHALE / 1000:.2f} km/s, "
          f"rho = {RHO_SHALE:.0f} kg/m^3")
    print("cell averages: rho = NTG*rho_sand + (1-NTG)*rho_shale (mass per volume),")
    print("and 1/vp = NTG/vp_sand + (1-NTG)/vp_shale, which is exact for the")
    print("transit time through the cell.")
    print("\n   NTG   clean-sand phi   AI (MRayl)")
    for ntg in (0.30, 0.50, 0.70):
        for phi in (0.15, 0.20, 0.25, 0.30):
            vp_s, vs_s, rho_s = saturated_velocities(phi, 1.0, 0.0, "gas")
            rho_e = ntg * rho_s + (1 - ntg) * RHO_SHALE
            vp_e = 1.0 / (ntg / vp_s + (1 - ntg) / VP_SHALE)
            print(f"  {ntg:5.2f}   {phi:14.2f}   {rho_e * vp_e / 1e6:11.2f}")
    vp_ref, _, rho_ref = saturated_velocities(0.25, 1.0, 0.0, "gas")
    target2 = (0.5 * rho_ref + 0.5 * RHO_SHALE) * \
        1.0 / (0.5 / vp_ref + 0.5 / VP_SHALE)
    print(f"\ntarget: the 50% NTG cell with clean-sand phi = 0.25, "
          f"AI = {target2 / 1e6:.2f} MRayl")
    print("other (NTG, phi) mixtures within 1% of that impedance:")
    print("\n   NTG   clean-sand phi   AI (MRayl)")
    found = 0
    for ntg in np.arange(0.15, 0.95, 0.01):
        for phi in np.arange(0.10, 0.34, 0.005):
            vp_s, vs_s, rho_s = saturated_velocities(phi, 1.0, 0.0, "gas")
            rho_e = ntg * rho_s + (1 - ntg) * RHO_SHALE
            vp_e = 1.0 / (ntg / vp_s + (1 - ntg) / VP_SHALE)
            if abs(rho_e * vp_e - target2) / target2 < 0.01:
                found += 1
                if found % 12 == 1:
                    print(f"  {ntg:5.2f}   {phi:14.2f}   "
                          f"{rho_e * vp_e / 1e6:11.2f}")
    print(f"{found} mixtures in the scanned range give this impedance to 1%.")
    print("Net-to-gross and clean-sand porosity are not separately determined by")
    print("one band-limited impedance: the measurement is a bulk average over the")
    print("cell, and its low-frequency content comes from the interpreter's model.")

    section("5. Scale: one seismic resolution cell versus a core plug")
    cell = 25.0 * 25.0 * 10.0          # m^3, a lambda/4-thick cell
    plug = np.pi * (0.025 / 2) ** 2 * 0.05   # m^3, 25 mm x 50 mm plug
    lam = 3000.0 / 30.0                # m, 30 Hz in a 3 km/s rock
    print(f"resolution cell {cell:.0f} m^3, core plug {plug * 1e6:.1f} cm^3")
    print(f"volume ratio cell/plug = {cell / plug:.3e}")
    print(f"wavelength at 30 Hz in 3.0 km/s rock = {lam:.0f} m, grain size ~1e-4 m")
    print(f"wavelength / grain size = {lam / 1e-4:.1e}")
    print("Every seismic property is an average over ~10^8 core-plug volumes and")
    print("of order 10^15 grain volumes; permeability, which lives at the pore")
    print("scale, is never directly measured by it.")


if __name__ == "__main__":
    main()
