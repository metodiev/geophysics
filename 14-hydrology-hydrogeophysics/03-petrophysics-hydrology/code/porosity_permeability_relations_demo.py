#!/usr/bin/env python3
"""Porosity-permeability relations: the capillary-bundle derivation, the
Kozeny-Carman (KC) form it produces, and the measured limits of that form.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python porosity_permeability_relations_demo.py

Everything here is SYNTHETIC: the grain sizes, porosities, the "clayey sand"
dataset and the geophysical porosity estimate are chosen teaching values, not
measurements from any site.  The unit conventions are the standard ones
(1 darcy = 9.869233e-13 m^2 is an exact definition).

Contents
--------
1.  Unit ladder: m^2 <-> darcy <-> millidarcy.
2.  Specific surface of a sphere pack: S0 = 6/d, and the exact packing porosities.
3.  Capillary-bundle derivation of k, checked term by term against k = phi^3/(2 tau S0^2 (1-phi)^2).
4.  KC vs porosity at fixed grain size.
5.  KC vs grain size at fixed porosity.
6.  Non-uniqueness: the (phi, d) pairs that give one measured permeability.
7.  Sensitivity to the Kozeny constant cK = 2 tau.
8.  From intrinsic permeability k to hydraulic conductivity K = k rho g / mu.
9.  Where KC fails: a synthetic "clayey sand" dataset and the KC misfit factor.
10. Error amplification when k is predicted from a geophysical porosity.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- exact / standard unit definitions ---------------------------------------
DARCY_M2 = 9.869233e-13          # 1 darcy in m^2, exact by definition
MD_M2 = DARCY_M2 * 1.0e-3        # 1 millidarcy in m^2

# --- standard water properties at 20 C (used for K = k rho g / mu) -----------
RHO_W = 998.2                    # kg/m^3
MU_W = 1.002e-3                  # Pa s
G = 9.80665                      # m/s^2


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def sphere_specific_surface(d_m):
    """Surface area per unit grain volume for spheres of diameter d, in 1/m."""
    return 6.0 / d_m


def kozeny_carman(phi, d_m, tau=2.5):
    """KC permeability in m^2: k = phi^3 / (2 tau S0^2 (1-phi)^2), S0 = 6/d."""
    S0 = sphere_specific_surface(d_m)
    return phi ** 3 / (2.0 * tau * S0 ** 2 * (1.0 - phi) ** 2)


def bundle_permeability(phi, d_m, tau=2.5):
    """Same formula written through the hydraulic radius R_h = phi/(S0(1-phi))."""
    S0 = sphere_specific_surface(d_m)
    R_h = phi / (S0 * (1.0 - phi))
    return phi * R_h ** 2 / (2.0 * tau)


def hydraulic_conductivity(k_m2, rho=RHO_W, mu=MU_W, g=G):
    """K = k rho g / mu, in m/s."""
    return k_m2 * rho * g / mu


def main():
    section("1. Unit ladder for permeability")
    print(f"  1 darcy      = {DARCY_M2:.6e} m^2   (exact definition)")
    print(f"  1 millidarcy = {MD_M2:.6e} m^2")
    print(f"  1 m^2        = {1.0 / DARCY_M2:.4e} darcy")

    section("2. Specific surface and exact packing porosities")
    print("  grain diameter d (mm)   S0 = 6/d (1/m)")
    for d_mm in (0.05, 0.10, 0.20, 0.50, 1.00):
        print(f"  {d_mm:19.2f}   {sphere_specific_surface(d_mm * 1e-3):14.1f}")
    phi_cubic = 1.0 - np.pi / 6.0                      # simple cubic sphere packing
    phi_rhomb = 1.0 - np.pi / (3.0 * np.sqrt(2.0))     # face-centred/rhombohedral
    print(f"  simple-cubic sphere packing    phi = 1 - pi/6           = {phi_cubic:.5f}")
    print(f"  rhombohedral sphere packing    phi = 1 - pi/(3 sqrt 2)  = {phi_rhomb:.5f}")

    section("3. Capillary-bundle derivation checked against the KC form")
    phi, d = 0.25, 0.20e-3
    S0 = sphere_specific_surface(d)
    R_h = phi / (S0 * (1.0 - phi))
    k_bundle = bundle_permeability(phi, d)
    k_kc = kozeny_carman(phi, d)
    print(f"  SYNTHETIC input: phi = {phi:.3f}, d = {d * 1e3:.3f} mm, tau = 2.5")
    print(f"  pore volume / bulk volume        phi            = {phi:.4f}")
    print(f"  wetted surface / bulk volume     S0 (1-phi)     = {S0 * (1 - phi):.1f} 1/m")
    print(f"  hydraulic radius R_h = phi/(S0(1-phi))         = {R_h:.6e} m")
    print(f"  k = phi R_h^2/(2 tau)  (bundle)                = {k_bundle:.6e} m^2")
    print(f"  k = phi^3/(2 tau S0^2 (1-phi)^2)  (KC)         = {k_kc:.6e} m^2")
    print(f"  difference                                     = {abs(k_bundle - k_kc):.3e} m^2")
    print(f"  k in darcy                                     = {k_kc / DARCY_M2:.4f} D")
    print(f"  k in millidarcy                                = {k_kc / MD_M2:.1f} mD")
    print(f"  the same formula with cK = 2 tau = 5 and 180 = 36 cK:")
    k_180 = d ** 2 * phi ** 3 / (180.0 * (1.0 - phi) ** 2)
    print(f"  k = d^2 phi^3/(180 (1-phi)^2)                  = {k_180:.6e} m^2")

    section("4. k versus porosity at fixed grain size (d = 0.20 mm)")
    d = 0.20e-3
    print("      phi      k (m^2)         k (mD)      k ratio to phi=0.20")
    k_ref = kozeny_carman(0.20, d)
    for phi in (0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40):
        k = kozeny_carman(phi, d)
        print(f"  {phi:7.2f}   {k:.6e}   {k / MD_M2:11.3f}   {k / k_ref:16.3f}")
    phi1, phi2 = 0.20, 0.40
    print(f"  doubling porosity from {phi1:.2f} to {phi2:.2f} multiplies k by "
          f"{kozeny_carman(phi2, d) / kozeny_carman(phi1, d):.1f}")

    section("5. k versus grain size at fixed porosity (phi = 0.25)")
    phi = 0.25
    print("      d (mm)        k (m^2)         k (mD)")
    for d_mm in (0.05, 0.10, 0.20, 0.50, 1.00):
        k = kozeny_carman(phi, d_mm * 1e-3)
        print(f"  {d_mm:9.2f}   {k:.6e}   {k / MD_M2:11.4f}")
    print("  k scales exactly as d^2 at fixed phi: "
          f"d 0.10 -> 0.20 mm multiplies k by "
          f"{kozeny_carman(phi, 0.20e-3) / kozeny_carman(phi, 0.10e-3):.1f}")

    section("6. Non-uniqueness: (phi, d) pairs that give the same k")
    k_target = 1.0e-12
    print(f"  target k = {k_target:.3e} m^2 = {k_target / MD_M2:.1f} mD")
    print("      phi      required d (mm)   S0 (1/m)")
    for phi in (0.15, 0.20, 0.25, 0.30, 0.35):
        d_req = np.sqrt(k_target * 180.0 * (1.0 - phi) ** 2 / phi ** 3)
        print(f"  {phi:7.2f}   {d_req * 1e3:15.4f}   "
              f"{sphere_specific_surface(d_req):9.1f}")
    print("  porosity alone does not determine k: the grain size (or the specific")
    print("  surface, or the fracture aperture) must be supplied independently.")

    section("7. Sensitivity to the Kozeny constant cK = 2 tau")
    phi, d = 0.25, 0.20e-3
    print("      tau     cK = 2 tau    k (mD)     K (m/s)")
    for tau in (1.5, 2.0, 2.5, 3.0, 4.0):
        k = kozeny_carman(phi, d, tau=tau)
        print(f"  {tau:7.2f}   {2 * tau:10.1f}   {k / MD_M2:10.2f}   "
              f"{hydraulic_conductivity(k):.3e}")
    k25 = kozeny_carman(phi, d, tau=2.5)
    k40 = kozeny_carman(phi, d, tau=4.0)
    print(f"  a factor {4.0 / 1.5:.2f} span in tau spans k by "
          f"{k25 / kozeny_carman(phi, d, tau=1.5):.2f} to "
          f"{k25 / k40:.2f} around the tau = 2.5 value")

    section("8. Intrinsic permeability to hydraulic conductivity")
    print("  water at 20 C: rho = 998.2 kg/m^3, mu = 1.002e-3 Pa s, g = 9.80665 m/s^2")
    print("      k (m^2)        k (mD)      K (m/s)     K (m/day)")
    for k in (1.0e-14, 1.0e-13, 1.0e-12, 1.0e-11):
        K = hydraulic_conductivity(k)
        print(f"  {k:.3e}   {k / MD_M2:11.3f}   {K:.3e}   {K * 86400.0:.3e}")
    print(f"  the conversion factor at 20 C is K/k = {hydraulic_conductivity(1.0):.3e} "
          f"1/(m s)")

    section("9. Where KC fails: a synthetic clayey-sand dataset")
    # The synthetic 'dataset' is generated by a different closure: pore space split
    # between a clean-sand fraction and a microporous clay fraction that carries
    # almost no flow.  KC is then fitted as if the medium were a clean sand.
    print("  SYNTHETIC generator: effective flow porosity phi_f = phi - phi_clay,")
    print("  with phi_clay = min(0.06, 0.35 phi); k_true = KC(phi_f, d).")
    print("      phi     phi_f    k_true (mD)   k_KC (mD)   k_KC/k_true")
    ratios = []
    for phi in (0.15, 0.20, 0.25, 0.30, 0.35):
        d = 0.20e-3
        phi_clay = min(0.06, 0.35 * phi)
        phi_f = phi - phi_clay
        k_true = kozeny_carman(phi_f, d)
        k_kc = kozeny_carman(phi, d)
        ratios.append(k_kc / k_true)
        print(f"  {phi:7.2f}   {phi_f:7.3f}   {k_true / MD_M2:11.2f}   "
              f"{k_kc / MD_M2:10.2f}   {k_kc / k_true:10.2f}")
    print(f"  KC over-predicts by {min(ratios):.1f}x to {max(ratios):.1f}x for this "
          f"SYNTHETIC clayey sand.")
    print("  A clay content that changes the flow porosity by a few points changes k")
    print("  by a large factor, and KC cannot see the clay at all.")

    section("10. Error amplification: geophysical porosity -> permeability")
    phi = 0.25
    dlnk_dphi = 3.0 / phi + 2.0 / (1.0 - phi)
    print(f"  at phi = {phi:.2f}:  d(ln k)/d(phi) = 3/phi + 2/(1-phi) = {dlnk_dphi:.3f}")
    for dphi in (0.005, 0.010, 0.020):
        print(f"  an absolute porosity error of {dphi:.3f} gives a permeability "
              f"error of {100.0 * dlnk_dphi * dphi:.1f}%")
    print("  A +-0.01 porosity error is a +-15% permeability error, before any error")
    print("  in grain size, specific surface or the Kozeny constant is counted.")

    section("Summary of the teaching numbers")
    k = kozeny_carman(0.25, 0.20e-3)
    print(f"  KC reference model: phi = 0.250, d = 0.200 mm, tau = 2.5")
    print(f"    k = {k:.4e} m^2 = {k / MD_M2:.1f} mD = {k / DARCY_M2:.3f} D")
    print(f"    K = {hydraulic_conductivity(k):.4e} m/s = "
          f"{hydraulic_conductivity(k) * 86400.0:.4e} m/day")


if __name__ == "__main__":
    main()
