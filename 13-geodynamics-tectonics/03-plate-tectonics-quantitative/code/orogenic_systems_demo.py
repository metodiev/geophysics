#!/usr/bin/env python3
"""Orogenic systems: crustal thickening, Airy isostasy, the buoyancy force per
unit length, and how strong a lithosphere must be to hold a plateau up.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python orogenic_systems_demo.py

Everything is SYNTHETIC.  The crust, the plateau and the viscosities are chosen
teaching values, not measurements of any real orogen.  No published elevation,
crustal thickness or viscosity estimate is used or quoted.

Contents
--------
1. Airy isostasy: elevation, root and the Moho depth of a thickened crust.
2. Shortening needed to produce a given thickening (volume conservation).
3. The buoyancy force per unit length, integrated exactly and compared with the
   commonly quoted scale g rho_c (t^2 - t0^2)/2.
4. Isostatic rebound amplification: erosion is not exhumation.
5. Stokes collapse time and the effective viscosity a 50 Myr plateau requires.
6. Non-uniqueness: the same elevation from crustal thickening or from removal
   of cold mantle lithosphere.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
RHO_C = 2800.0          # crust density, kg/m^3
RHO_M = 3330.0          # mantle density, kg/m^3
RHO_W = 1030.0          # water density, kg/m^3
TC0_KM = 35.0           # reference (sea level) crustal thickness
A_KM = 125.0            # lithosphere thickness
ALPHA = 3.0e-5          # thermal expansion coefficient, 1/K
TM_C = 1300.0           # mantle potential temperature, deg C
G = 9.81                # m/s^2, standard gravity (exact standard constant)
SECONDS_PER_MYR = 365.25 * 24.0 * 3600.0 * 1.0e6


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def airy_elevation_km(tc_km):
    """Air-loaded Airy elevation of a crust of thickness tc, reference tc0 at 0."""
    return (tc_km - TC0_KM) * (RHO_M - RHO_C) / RHO_M


def gpe_exact(tc_km):
    """Buoyancy force per unit length between the tc column and the reference
    column, N/m, for air-loaded Airy isostasy with a constant crustal density.

    Integrand of  (P(z) - P_ref(z)) dz  from the sea-level datum downward:
      0 <= z <= tc0        : rho_c g E                      (E = elevation)
      tc0 < z <= t - E     : g [ rho_c (z + E) - rho_m (z - tc0) ]
      below t - E          : 0, because the columns are compensated.
    """
    t_m = tc_km * 1.0e3
    t0_m = TC0_KM * 1.0e3
    e_m = airy_elevation_km(tc_km) * 1.0e3
    part1 = RHO_C * G * e_m * t0_m
    u_bar = t_m - e_m - t0_m
    part2 = G * ((RHO_C - RHO_M) * u_bar ** 2 / 2.0
                 + RHO_C * (t0_m + e_m) * u_bar)
    return part1 + part2


def gpe_simple(tc_km):
    """The commonly quoted scale g rho_c (t^2 - t0^2)/2, N/m."""
    return 0.5 * G * RHO_C * ((tc_km * 1.0e3) ** 2 - (TC0_KM * 1.0e3) ** 2)


def main():
    section("1. Airy isostasy: elevation, root and Moho depth")
    print(f"  SYNTHETIC constants: rho_c = {RHO_C:.0f}, rho_m = {RHO_M:.0f} kg/m^3,")
    print(f"  reference crust tc0 = {TC0_KM:.0f} km at sea level, g = {G:.2f} m/s^2")
    print("  Airy isostasy gives e = (tc - tc0)(rho_m - rho_c)/rho_m, and the Moho")
    print("  depth below sea level is e + tc.")
    print("\n    crust tc (km)   elevation e (km)   Moho depth (km)   e/(tc-tc0)")
    print("    " + "-" * 62)
    for tc in (35.0, 40.0, 50.0, 60.0, 70.0, 80.0):
        e = airy_elevation_km(tc)
        print(f"    {tc:13.1f}   {e:16.3f}   {e + tc:15.1f}   "
              f"{e / (tc - TC0_KM) if tc != TC0_KM else float('nan'):.4f}")
    ratio = (RHO_M - RHO_C) / RHO_M
    print(f"  The ratio is constant: 1 km of thickening buys {ratio:.4f} km of")
    print(f"  elevation, i.e. {1.0 / ratio:.2f} km of crust per km of topography.")
    print(f"  This is the exact standard constant (rho_m-rho_c)/rho_m for the")
    print(f"  chosen densities, and it is not a measured value.")

    section("2. Shortening needed (volume conservation, no erosion)")
    print("    tc (km)   tc/tc0 = beta   horizontal shortening (%)   "
          "line shortening (km per 100 km)")
    for tc in (40.0, 50.0, 60.0, 70.0):
        beta = tc / TC0_KM
        short = 100.0 * (1.0 - 1.0 / beta)
        print(f"    {tc:7.1f}   {beta:14.3f}   {short:24.1f}   {short:26.1f}")
    print("  Shortening is 1 - tc0/tc if no material leaves the section: doubling")
    print("  the crust requires 50% shortening, which is why large orogens need")
    print("  either very large convergence or a wide, distributed deformation zone.")

    section("3. Buoyancy force per unit length")
    print("    tc (km)   e (km)   exact (1e12 N/m)   scale (1e12 N/m)   exact/scale")
    print("    " + "-" * 72)
    for tc in (40.0, 50.0, 60.0, 70.0, 80.0):
        ex, sp = gpe_exact(tc), gpe_simple(tc)
        print(f"    {tc:7.1f}   {airy_elevation_km(tc):6.3f}   {ex / 1e12:16.4f}   "
              f"{sp / 1e12:16.4f}   {ex / sp:11.3f}")
    print("  The exact integral and the widely used scale g rho_c (t^2-t0^2)/2")
    print("  agree in sign and order of magnitude but differ by a large factor")
    print("  because the scale ignores the isostatic root: part of the thickened")
    print("  column replaces mantle rather than adding mass above the Moho.")

    section("4. Isostatic rebound: erosion is not elevation loss")
    amp = RHO_M / (RHO_M - RHO_C)
    frac = 1.0 - RHO_C / RHO_M
    print("  Eroding a rock column of thickness h thins the crust by h and lowers")
    print("  the surface by only h(1 - rho_c/rho_m), because the root rebounds:")
    print(f"     1 - rho_c/rho_m = {frac:.4f}    (so {100 * frac:.1f}% of the erosion")
    print("     becomes net elevation loss and the rest is isostatic rebound)")
    h0 = airy_elevation_km(70.0)
    print(f"\n  Starting from a plateau of crustal thickness 70 km (e = {h0:.3f} km):")
    print("    erosion (km)   surface lowering (km)   remaining elevation (km)")
    for h in (0.5, 1.0, 2.0, 5.0, 10.0, 20.0):
        print(f"    {h:11.1f}   {h * frac:21.3f}   {h0 - h * frac:24.3f}")
    print(f"  Levelling the plateau completely needs h = e/(1 - rho_c/rho_m) = "
          f"{h0 / frac:.1f} km of erosion,")
    print(f"  that is {amp:.2f} times the elevation: the amplification factor")
    print(f"  rho_m/(rho_m-rho_c) = {amp:.3f} is why erosion is a weak way to destroy")
    print("  topography, and why the Moho rises almost as fast as the surface falls.")

    section("5. Stokes collapse time and the required effective viscosity")
    print("  Order-of-magnitude balance for a plateau of crustal thickness H, thermal")
    print("  or crustal buoyancy stress rho_c g de, half-width L and viscosity eta:")
    print("      viscous stress  eta V/H  balances  rho_c g de  ->  V = rho_c g de H / eta")
    print("      collapse time   tau = L / V = eta L / (rho_c g de H)")
    print("    tc (km)   e=de (km)   tau at eta=1e20 (Myr)   tau at eta=1e21 (Myr)")
    print("    " + "-" * 70)
    H_m, L_m = 70.0e3, 250.0e3
    for tc in (50.0, 60.0, 70.0, 80.0):
        de_m = airy_elevation_km(tc) * 1.0e3
        tau1 = 1e20 * L_m / (RHO_C * G * de_m * H_m) / SECONDS_PER_MYR
        tau2 = 1e21 * L_m / (RHO_C * G * de_m * H_m) / SECONDS_PER_MYR
        print(f"    {tc:7.1f}   {de_m / 1e3:9.3f}   {tau1:21.2f}   {tau2:20.2f}")
    de_m = airy_elevation_km(70.0) * 1.0e3
    print("\n  viscosity needed for a chosen collapse time (tc = 70 km, L = 250 km):")
    print("    collapse time (Myr)   required eta (Pa s)")
    for tau_myr in (1.0, 10.0, 50.0, 100.0):
        eta = tau_myr * SECONDS_PER_MYR * (RHO_C * G * de_m * H_m) / L_m
        print(f"    {tau_myr:18.1f}   {eta:18.2e}")
    print("  A geologically slow collapse needs eta of order 1e22-1e23 Pa s, two to")
    print("  three orders of magnitude above crustal-channel estimates.  That gap is")
    print("  the honest statement of the problem: the strong upper crust and mantle")
    print("  lithosphere, not the crust alone, decide whether a plateau collapses.")

    section("6. Non-uniqueness: the same elevation two ways")
    a_norm = ALPHA
    print("  Elevation can be produced by thickening the crust OR by removing cold")
    print("  mantle lithosphere, which is buoyant when replaced by asthenosphere.")
    print("  Removing a cold lid of thickness L with mean deficit Tm/2 raises the")
    print("  surface by rho_m alpha (Tm/2) L / (rho_m - rho_w):")
    print("\n    lid removed (km)   uplift (km)   equivalent crustal thickening (km)")
    coef = RHO_M * a_norm * (TM_C / 2.0) / (RHO_M - RHO_W)
    for lid in (25.0, 50.0, 100.0, 150.0):
        uplift = coef * lid
        print(f"    {lid:16.1f}   {uplift:10.3f}   "
              f"{uplift / ((RHO_M - RHO_C) / RHO_M):27.2f}")
    print(f"  coefficient rho_m alpha Tm/(2(rho_m-rho_w)) = {coef:.4f} m per m of lid")
    print("  Removing 100 km of cold mantle lithosphere explains 2.8 km of elevation")
    print("  with NO thickening at all.  Elevation alone therefore cannot separate")
    print("  crustal thickening from lithospheric thinning; seismological crustal")
    print("  thickness, or gravity, is needed to break the tie.")


if __name__ == "__main__":
    main()
