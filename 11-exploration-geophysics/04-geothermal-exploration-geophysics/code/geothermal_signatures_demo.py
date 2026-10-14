#!/usr/bin/env python3
"""Geophysical signatures of geothermal reservoirs: geotherms and heat flow,
heat in place, the convection criterion, the resistivity signature of a clay
cap, the gravity anomaly of a buried body, and the source-depth trade-off.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geothermal_signatures_demo.py

Contents
--------
1. Conductive geotherm with radiogenic heat production, and the surface heat
   flow it implies.
2. Sensitivity: what heat flow is needed for 150 C at a given depth.
3. Heat in place and the thermal power it could sustain.
4. The Rayleigh criterion for convection in a permeable layer: how much
   permeability is needed.
5. Resistivity of a clay cap and of hot formation water (Archie).
6. Gravity anomaly of a buried body and the half-width depth rule.
7. The source-strength/source-depth trade-off in a heat-flow anomaly.

All models and numbers are SYNTHETIC teaching values: chosen rock properties,
chosen reservoir geometry and chosen fluid properties.  The mineral, fluid and
physical constants quoted are standard values with units.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 6.67430e-11        # m^3 kg^-1 s^-2, gravitational constant (exact constant)
RHO_W, C_W = 1000.0, 4180.0      # kg/m^3, J kg^-1 K^-1, water (standard)
RHO_R, C_R = 2700.0, 900.0       # kg/m^3, J kg^-1 K^-1, rock matrix (standard)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def geotherm(z, t0, k_cond, q_mantle, heat_prod):
    """T(z) with uniform radiogenic heat production (W/m^3)."""
    return t0 + (q_mantle * z + 0.5 * heat_prod * z ** 2) / k_cond


def main():
    section("1. Conductive geotherm and surface heat flow")
    t0 = 10.0                     # degC, chosen mean surface temperature
    k_cond = 2.5                  # W m^-1 K^-1, chosen conductivity
    q_mantle = 0.060              # W/m^2 = 60 mW/m^2, reduced heat flow
    heat_prod = 1.5e-6            # W/m^3, radiogenic production
    h_crust = 10000.0             # m, thickness producing heat
    q_surface = q_mantle + heat_prod * h_crust
    print(f"chosen: T0 = {t0:.0f} C, k = {k_cond:.1f} W/(m K), "
          f"reduced heat flow = {q_mantle * 1000:.0f} mW/m^2,")
    print(f"        radiogenic production = {heat_prod * 1e6:.1f} microW/m^3 "
          f"over {h_crust / 1000:.0f} km")
    print(f"surface heat flow q = q_m + A h = {q_surface * 1000:.0f} mW/m^2 "
          f"= {q_surface:.4f} W/m^2")
    print("\n   depth (km)   T (C)   dT/dz (C/km)")
    for z_km in (1.0, 2.0, 3.0, 5.0, 8.0):
        z = z_km * 1000.0
        temp = geotherm(z, t0, k_cond, q_mantle, heat_prod)
        grad = (q_mantle + heat_prod * z) / k_cond * 1000.0
        print(f"  {z_km:10.1f}   {temp:5.0f}   {grad:12.1f}")
    print("The gradient is not constant: radiogenic production makes it steepen")
    print("with depth.  A single 'geothermal gradient' is already a model.")

    section("2. What heat flow is needed for a given temperature?")
    print("conductive, no production: q = k (T - T0)/z")
    print("\n   target T (C)   depth (km)   q needed (mW/m^2) for k = 2.0 / 2.5 / 3.0")
    for t_target in (100.0, 150.0, 200.0, 250.0):
        for z_km in (2.0, 3.0, 4.0):
            row = [k_i * (t_target - t0) / (z_km * 1000.0) * 1000.0
                   for k_i in (2.0, 2.5, 3.0)]
            print(f"  {t_target:12.0f}   {z_km:10.1f}   {row[0]:15.0f} "
                  f"{row[1]:5.0f} {row[2]:5.0f}")
    print("A 250 C resource at 3 km needs about 200 mW/m^2, three times the")
    print("global average: an anomalous heat flow is the first-order screening")
    print("criterion, and it is measured directly (05-09-01), not inferred from")
    print("a geophysical inversion.")

    section("3. Heat in place and the power it could sustain")
    lx, ly, thick = 2000.0, 2000.0, 300.0      # m
    phi = 0.08
    t_res, t_ref = 250.0, 60.0
    vol = lx * ly * thick
    rho_c = (1.0 - phi) * RHO_R * C_R + phi * RHO_W * C_W
    heat = rho_c * vol * (t_res - t_ref)
    print(f"reservoir {lx / 1000:.0f} x {ly / 1000:.0f} km, {thick:.0f} m thick, "
          f"porosity {phi:.2f}")
    print(f"T_reservoir = {t_res:.0f} C, T_reference = {t_ref:.0f} C")
    print(f"volumetric heat capacity = {rho_c / 1e6:.2f} MJ/(m^3 K)")
    print(f"volume = {vol:.3e} m^3")
    print(f"heat in place = {heat:.3e} J = {heat / 1e18:.2f} EJ")
    years = 30.0
    print(f"\nsustained thermal power if all of it were produced in "
          f"{years:.0f} years:")
    print(f"  {heat / (years * 3.15576e7) / 1e6:.0f} MW (thermal)")
    print("\nsensitivity to the fraction actually recovered (a scenario")
    print("multiplier, not a physical prediction):")
    for frac in (0.02, 0.05, 0.10, 0.25):
        p = heat * frac / (years * 3.15576e7) / 1e6
        print(f"  recovery fraction {frac:4.2f}: {p:6.0f} MW (thermal) for "
              f"{years:.0f} years")
    print("The heat-in-place number is arithmetic; the recovery fraction, the")
    print("flow rate and the conversion efficiency are engineering and")
    print("economics.  This module computes the first and leaves the rest")
    print("symbolic, exactly as 04-06 does for hydrocarbon volumes.")

    section("4. Rayleigh criterion for convection in a permeable layer")
    beta = 5.0e-4           # 1/K, thermal expansion of water (chosen)
    nu = 3.0e-7             # m^2/s, kinematic viscosity (chosen, hot water)
    k_therm = 2.0           # W/(m K), chosen saturated conductivity
    rho_c_w = RHO_W * C_W
    ra_crit = 4.0 * np.pi ** 2      # free-free boundaries, exact for this model
    print(f"chosen beta = {beta:.1e} /K, nu = {nu:.1e} m^2/s, "
          f"k_thermal = {k_therm:.1f} W/(m K)")
    print(f"Ra = rho c beta g dT H k / (nu k_thermal); critical Ra = 4 pi^2 = "
          f"{ra_crit:.1f}")
    print("\n   layer thickness H (m)   dT (K)   k needed for Ra = 4 pi^2 (m^2)"
          "   in darcy")
    for h_lyr in (100.0, 200.0, 500.0):
        for dtemp in (50.0, 100.0, 200.0):
            k_req = ra_crit * nu * k_therm / (rho_c_w * beta * 9.81 * dtemp * h_lyr)
            print(f"  {h_lyr:21.0f}   {dtemp:6.0f}   {k_req:33.2e}   "
                  f"{k_req / 9.869233e-13:6.2f}")
    print("Across this range convection needs 0.01 to 0.23 darcy, and the")
    print("requirement falls as 1/(H dT): a thick layer with a big temperature")
    print("difference convects at permeability so low that no surface method")
    print("could resolve it.  The criterion assumes homogeneity, isotropic")
    print("permeability and idealised boundaries, so it is an order-of-magnitude")
    print("screen for whether convection is possible at all, not a prediction of")
    print("what a particular field does.")

    section("5. Resistivity of the clay cap and of hot water")
    a_archie, m_archie = 1.0, 2.0
    phi_cap = 0.25
    rho_w25 = 1.0            # ohm m, chosen formation-water resistivity at 25 C
    print("Archie: rho = a rho_w / phi^m with a = 1.0, m = 2.0 (chosen)")
    print("temperature dependence of rho_w (standard relation):")
    print("  rho_w(T) = rho_w(25 C) * (25 + 21.5)/(T + 21.5)")
    print("\n   T (C)   rho_w (ohm m)   cap resistivity (ohm m)")
    for temp in (25.0, 100.0, 200.0, 250.0):
        rho_w = rho_w25 * (25.0 + 21.5) / (temp + 21.5)
        rho_cap = a_archie * rho_w / phi_cap ** m_archie
        print(f"  {temp:5.0f}   {rho_w:13.3f}   {rho_cap:21.2f}")
    print("Hot water alone lowers the resistivity by a factor")
    print(f"{1.0 / ((25.0 + 21.5) / (250.0 + 21.5)):.1f} between 25 and 250 C,")
    print("and clay alteration lowers it much further.  Both effects appear as")
    print("the same low-resistivity anomaly, which is why an MT anomaly maps")
    print("conductance (a product) and not temperature.")

    section("6. Gravity anomaly of a buried body and the half-width rule")
    print("sphere: g(x) = (4/3) pi G drho a^3 z / (z^2 + x^2)^(3/2)")
    print("at x = 0: g_max = (4/3) pi G drho a^3 / z^2")
    drho = -200.0            # kg/m^3, low-density altered caprock (chosen)
    radius = 500.0
    print(f"\nchosen drho = {drho:.0f} kg/m^3, radius = {radius:.0f} m")
    print("\n   depth z (m)   g_max (mGal)   half-width (m)")
    for z_c in (500.0, 1000.0, 1500.0, 2500.0):
        g_max = 4.0 / 3.0 * np.pi * G * abs(drho) * radius ** 3 / z_c ** 2
        print(f"  {z_c:11.0f}   {g_max * 1e5:12.2f}   {0.766 * z_c:14.0f}")
    print("\nhalf-width derivation: g = g_max (1 + x^2/z^2)^(-3/2) = g_max/2")
    print(f"gives x = z sqrt(2^(2/3) - 1) = {np.sqrt(2 ** (2 / 3) - 1):.3f} z")
    print("A 0.3 mGal anomaly from a 500 m body is measurable, but the half-width")
    print("gives the depth only through the assumed shape: depth, density")
    print("contrast and radius trade off, which is the subject of 07-03-02.")

    section("7. Source strength and source depth trade off")
    print("steady-state heat flow from a point source of power Q at depth z")
    print("through the surface directly above it: q = Q/(2 pi z^2)")
    print("\n   surface anomaly (mW/m^2)   Q (MW) for z = 1 km / 2 km / 3 km")
    for q_surf in (20.0, 50.0, 100.0):
        row = [q_surf * 1e-3 * 2.0 * np.pi * (z * 1000.0) ** 2 / 1e6
               for z in (1.0, 2.0, 3.0)]
        print(f"  {q_surf:24.0f}   {row[0]:14.1f} {row[1]:7.1f} {row[2]:7.1f}")
    print("A 50 mW/m^2 anomaly at the surface can be a 0.3 MW source at 1 km or")
    print("a 2.8 MW source at 3 km.  Heat-flow amplitude alone does not separate")
    print("source strength from source depth; the anomaly's WIDTH does, in the")
    print("same way the half-width does for gravity.")


if __name__ == "__main__":
    main()
