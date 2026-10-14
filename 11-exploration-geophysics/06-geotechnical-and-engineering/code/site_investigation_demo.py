#!/usr/bin/env python3
"""Site investigation: small-strain stiffness from Vs, vs30 and profile
truncation, elastic settlement of a footing, microgravity detection of a void,
and the value of information of a survey against a stated prior.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python site_investigation_demo.py

Everything is SYNTHETIC: velocities, moduli, footing loads and costs are chosen
teaching values, not measurements of any site.  Print-only; no network access.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 6.67430e-11          # m^3 kg^-1 s^-2 (standard constant)
GAL_TO_MGAL = 1.0e5      # 1 mGal = 1e-5 m/s^2


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def g_max(rho, vs):
    """Small-strain shear modulus G_max = rho Vs^2, in Pa."""
    return rho * vs ** 2


def e_from_g(g, nu):
    """Young's modulus from shear modulus and Poisson's ratio."""
    return 2.0 * g * (1.0 + nu)


def settlement_circular(q, radius, e_young, nu):
    """Elastic settlement at the centre of a uniformly loaded flexible circular
    area, from the Boussinesq solution: s = 2 q R (1 - nu^2) / E."""
    return 2.0 * q * radius * (1.0 - nu ** 2) / e_young


def vs30(layer_top, layer_bottom, vs, depth=30.0):
    """Travel-time weighted (harmonic) Vs30 for a layered profile, m/s."""
    total_t = 0.0
    for top, bottom, v in zip(layer_top, layer_bottom, vs):
        lo, hi = max(top, 0.0), min(bottom, depth)
        if hi > lo:
            total_t += (hi - lo) / v
    return depth / total_t


def void_anomaly(radius, depth, d_rho):
    """Peak gravity anomaly of a buried sphere, in m/s^2."""
    return (4.0 / 3.0) * np.pi * G * d_rho * radius ** 3 / depth ** 2


def main():
    section("1. What Vs measures: small-strain stiffness")
    print("  G_max = rho * Vs^2,  E = 2 G (1 + nu),  nu = 0.30 (stated)")
    print("\n   material          rho (kg/m3)   Vs (m/s)   G (MPa)   E (MPa)")
    for name, rho, vs in (("soft soil", 1800.0, 150.0),
                          ("stiff soil", 1900.0, 300.0),
                          ("dense sand / gravel", 2000.0, 500.0),
                          ("weathered rock", 2200.0, 900.0),
                          ("competent rock", 2500.0, 2000.0)):
        g = g_max(rho, vs)
        print(f"   {name:19s} {rho:11.0f}   {vs:8.0f}   {g/1e6:8.1f}   "
              f"{e_from_g(g, 0.30)/1e6:8.1f}")
    print("\n  A factor-3 change in Vs is an order-of-magnitude change in stiffness:")
    print("  stiffness, not velocity, is what enters a deformation calculation.")

    section("2. vs30 and the effect of profile truncation")
    top = np.array([0.0, 3.0, 8.0, 20.0, 40.0])
    bot = np.array([3.0, 8.0, 20.0, 40.0, 60.0])
    vs = np.array([160.0, 240.0, 380.0, 600.0, 900.0])
    print("  SYNTHETIC profile: " + ", ".join(
        f"{v:.0f} m/s to {b:.0f} m" for v, b in zip(vs, bot)))
    print(f"  Vs30 (full profile, 0-30 m)      = {vs30(top, bot, vs):6.1f} m/s")
    print(f"  Vs30 if data stop at 20 m (assume 20-30 m = the 380 m/s layer) = "
          f"{vs30(np.array([0, 3, 8, 20]), np.array([3, 8, 20, 30]), vs[:3]):6.1f} m/s")
    print(f"  Vs30 if a 5 m stiff fill at 400 m/s is added at the surface = "
          f"{vs30(np.array([0, 5, 8, 13, 25]), np.array([5, 8, 13, 25, 45]),
                  np.array([400, 160, 240, 380, 600])):6.1f} m/s")
    print("  Vs30 moves by tens of per cent for a survey that stops at 20 m or misses")
    print("  a surface fill: it is a statement about the PROFILE, not a site constant.")

    section("3. Elastic settlement and its sensitivity to Vs")
    q = 200.0e3          # Pa, 200 kPa footing pressure (teaching value)
    radius = 2.5         # m, circular footing radius
    nu = 0.30
    rho = 2000.0
    strain_factor = 0.30  # stated: operational E is a fraction of the small-strain E
    print(f"  circular flexible footing: q = {q/1e3:.0f} kPa, R = {radius:.1f} m")
    print(f"  small-strain E from Vs, then E_operational = {strain_factor:.2f} E_max")
    print("  (a real design modulus is measured at working strain, not at Vs strain)")
    print("\n   Vs (m/s)   E_max (MPa)   E_op (MPa)   settlement (mm)")
    for vs in (250.0, 400.0, 600.0):
        e = e_from_g(g_max(rho, vs), nu)
        s = settlement_circular(q, radius, strain_factor * e, nu)
        print(f"   {vs:8.0f}   {e/1e6:11.1f}   {strain_factor*e/1e6:10.1f}   "
              f"{s*1e3:13.1f}")
    e0 = e_from_g(g_max(rho, 400.0), nu)
    s0 = settlement_circular(q, radius, strain_factor * e0, nu)
    for err in (-0.20, +0.20):
        vs_err = 400.0 * (1.0 + err)
        s1 = settlement_circular(q, radius,
                                 strain_factor * e_from_g(g_max(rho, vs_err), nu), nu)
        print(f"  Vs error {err*100:+.0f}% -> settlement {s1*1e3:7.1f} mm "
              f"({(s1/s0-1)*100:+.1f}%)")
    print(f"\n  Vs enters the settlement as Vs^-2 (through E): a 20% Vs error is a")
    print(f"  56% settlement error, and the strain factor shifts everything by the")
    print( "  same factor.  Both uncertainties belong in the reported settlement.")

    section("4. Microgravity detection of a void")
    rho_rock = 2500.0            # kg/m^3
    d_rho = -rho_rock            # air-filled void
    print("  sphere anomaly (peak, directly above): dg = (4/3) pi G |drho| R^3 / z^2")
    print("  rock density 2500 kg/m^3 (teaching value); void = air-filled")
    print("\n   radius (m)   z = 5 m     z = 10 m    z = 15 m   z = 20 m")
    for radius in (1.0, 2.0, 3.0):
        row = "   ".join(f"{void_anomaly(radius, z, d_rho)*GAL_TO_MGAL*1000:8.2f}"
                         for z in (5.0, 10.0, 15.0, 20.0))
        print(f"   {radius:10.1f}   {row}   (in microGal)")
    for radius in (1.0, 2.0, 3.0):
        zmax = np.sqrt((4.0 / 3.0) * np.pi * G * rho_rock * radius ** 3 /
                       (5.0e-8))
        print(f"  radius {radius:.0f} m reaches the 5 microGal noise floor at "
              f"z = {zmax:5.1f} m")
    print("  The depth limit goes as R^{3/2} while the anomaly falls as z^-2: a void")
    print("  twice as wide is detected about 2.8 times as deep, and no deeper.")

    section("5. Value of information: survey, protect, or drill blind?")
    prior = 0.10                # P(void) before any survey
    tpr = 0.85                  # P(anomaly | void)
    fpr = 0.20                  # P(anomaly | no void)
    cost_survey = 15.0          # arbitrary synthetic cost units
    cost_protect = 100.0        # cost of the protective measure taken on an anomaly
    cost_hit = 400.0            # cost of an undetected void (synthetic units)
    p_anom = prior * tpr + (1.0 - prior) * fpr
    miss = prior * (1.0 - tpr)
    post = prior * tpr / p_anom
    print(f"  prior P(void) = {prior:.2f}, TPR = {tpr:.2f}, FPR = {fpr:.2f}")
    print(f"  P(anomaly) = {p_anom:.3f}; P(void and no anomaly) = {miss:.3f}; "
          f"posterior P(void | anomaly) = {post:.3f}")
    cost_no_survey = prior * cost_hit
    cost_with_survey = cost_survey + p_anom * cost_protect + miss * cost_hit
    print(f"\n  expected cost, drill blind with no protection = {cost_no_survey:7.1f}")
    print(f"  expected cost, survey then act on the result = {cost_with_survey:7.1f}")
    print(f"  value of information                         = "
          f"{cost_no_survey - cost_with_survey:7.1f}")
    for pri in (0.01, 0.10, 0.30, 0.60):
        pa = pri * tpr + (1 - pri) * fpr
        ms = pri * (1 - tpr)
        vo = pri * cost_hit - (cost_survey + pa * cost_protect + ms * cost_hit)
        print(f"    prior {pri:.2f} -> VOI = {vo:7.1f}")
    print("  The survey pays only when the prior is high enough (or the miss cost")
    print("  large enough) to justify it: below that it is a cost with no decision")
    print("  to inform.  Note also that the survey never removes the risk — the")
    print("  residual miss term stays in the survey branch.")
    print("\n  All models and data in this module are SYNTHETIC.")


if __name__ == "__main__":
    main()
