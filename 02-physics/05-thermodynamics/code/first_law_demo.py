"""The first law in geothermal and magmatic systems.

Run:  python3 first_law_demo.py
Requires: Python standard library only.

Companion to lesson 02-05-02.

Sign convention used throughout (the geophysical one):

    dU = Q - W,   Q > 0 heat INTO the system, W > 0 work done BY the system.

Material properties are nominal. The adiabatic gradient uses
dT/dP = alpha T / (rho c_p), which is exact for a reversible adiabatic
(isentropic) process in a homogeneous medium.

The script:

1. States and exercises the sign convention on one controlled cycle.
2. Computes the adiabatic (isentropic) gradient for the mantle, the crust and
   the dry atmosphere, and converts it to K/km.
3. Computes advective heat transport and the first-law energy balance of a
   geothermal power plant.
4. Computes the latent-heat plateau of a crystallising magma and the fraction
   of a magma's heat that is latent.
5. Computes the temperature change of a slab descending 100 km adiabatically.
"""

import math

STANDARD_G = 9.80665          # m/s^2  exact (standard gravity definition)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def part1_sign_convention():
    section("1. The sign convention, exercised on one cycle")
    Q_in, W_out = 5.0e6, 2.0e6           # J
    dU = Q_in - W_out
    print("  dU = Q - W with Q > 0 into the system, W > 0 done by the system")
    print(f"  Step 1: Q = +{Q_in:.1e} J, W = +{W_out:.1e} J  ->  "
          f"dU = {dU:.1e} J (internal energy rises)")
    dU2 = -1.0e6 - 2.0e6               # Q = -1e6, W = +2e6 (work still done BY)
    print(f"  Step 2: Q = -1.0e6 J, W = +2.0e6 J  ->  dU = {dU2:.1e} J")
    print(f"  Cycle total dU = {dU + dU2:.1e} J  (must be 0 for a closed cycle)")
    print()
    print("  A first-law audit is a bookkeeping exercise. Every failure to close")
    print("  an energy budget in geophysics is a missing flux, not new physics.")


def adiabatic_gradient(alpha, T, rho, cp):
    """Return dT/dP in K/Pa for a reversible adiabatic process."""
    return alpha * T / (rho * cp)


def part2_adiabatic_gradient():
    section("2. Adiabatic (isentropic) temperature gradient")
    systems = {
        "mantle (alpha=3e-5/T)":   (3.0e-5, 1600.0, 3300.0, 1250.0),
        "crust (alpha=8e-6/T)":    (8.0e-6, 800.0, 2700.0, 800.0),
        "outer core (alpha=1.0e-5/T)": (1.0e-5, 4000.0, 11000.0, 700.0),
    }
    print(f"{'system':<28}{'dT/dP (K/GPa)':>15}{'rho*g (Pa/m)':>15}"
          f"{'dT/dz (K/km)':>15}")
    for name, (alpha, T, rho, cp) in systems.items():
        dTdP = adiabatic_gradient(alpha, T, rho, cp)
        dPdz = rho * STANDARD_G
        dTdz = dTdP * dPdz * 1000.0        # K/m -> K/km
        print(f"{name:<28}{dTdP * 1e9:>15.4f}{dPdz:>15.1f}{dTdz:>15.4f}")
    # dry atmosphere: alpha = 1/T so dT/dP = 1/(rho c_p) and dT/dz = g/c_p
    cp_air = 1005.0
    print(f"{'dry atmosphere (g/c_p)':<28}{'':>15}{'':>15}"
          f"{STANDARD_G / cp_air * 1000.0:>15.4f}")
    print()
    print("  The mantle adiabat is a few tenths of a kelvin per kilometre; the")
    print("  conductive crustal gradient is tens of kelvin per kilometre, and the")
    print("  dry atmospheric lapse rate is about 9.8 K/km. The three regimes")
    print("  differ by two orders of magnitude in the same units, which is why")
    print("  comparing a geotherm with an adiabat must be done on one figure.")


def part3_geothermal_balance():
    section("3. First-law balance of a geothermal (flash) plant")
    m_dot = 100.0            # kg/s
    cp_w = 4186.0            # J/kg/K  nominal
    T_in, T_out = 200.0, 50.0
    dT = T_in - T_out
    thermal = m_dot * cp_w * dT
    eta_gross = 0.12         # nominal thermal-to-electric conversion
    electric = thermal * eta_gross
    rejected = thermal - electric
    print(f"  mass flow = {m_dot:.0f} kg/s, c_p = {cp_w:.0f} J kg^-1 K^-1, "
          f"delta T = {dT:.0f} K")
    print(f"  advected enthalpy drop  m_dot c_p dT = {thermal:.4e} W "
          f"= {thermal / 1e6:.2f} MW thermal")
    print(f"  electric output at eta = {eta_gross:.2f}      = {electric:.4e} W "
          f"= {electric / 1e6:.2f} MWe")
    print(f"  heat rejected to cooling    = {rejected:.4e} W "
          f"= {rejected / 1e6:.2f} MW")
    print(f"  closure check: electric + rejected = "
          f"{(electric + rejected) / 1e6:.2f} MW  (equals thermal input)")
    print()
    print("  The first law is satisfied for ANY eta. Choosing eta is the job of")
    print("  the second law (lesson 02-05-03): the Carnot bound for these")
    print(f"  temperatures is 1 - {273.15 + T_out:.2f}/{273.15 + T_in:.2f} = "
          f"{(1 - (273.15 + T_out) / (273.15 + T_in)):.4f}.")
    return thermal, electric


def part4_magma_plateau():
    section("4. The latent-heat plateau of a crystallising magma")
    rho, cp, L = 2900.0, 840.0, 4.0e5
    T_start, T_end = 1500.0, 300.0
    sensible = rho * cp * (T_start - T_end)
    latent = rho * L
    print(f"  A magma cooling {T_start:.0f} K -> {T_end:.0f} K per m^3:")
    print(f"    sensible  rho c_p dT = {sensible:.4e} J")
    print(f"    latent    rho L      = {latent:.4e} J")
    print(f"    latent fraction      = {latent / (sensible + latent):.4f}")
    print()
    print("  In a magma chamber the crystallisation interval spans a few tens to")
    print("  a few hundreds of kelvin. If it is taken as 150 K, the latent heat")
    print("  released per kelvin of cooling in that interval is")
    print(f"    rho L / 150 K = {latent / 150.0:.4e} J m^-3 K^-1")
    print(f"  against the sensible rate of {rho * cp:.4e} J m^-3 K^-1 — a factor")
    print(f"    {latent / 150.0 / (rho * cp):.2f}")
    print("  greater heat release per kelvin of cooling inside the interval than")
    print("  outside it. That factor is why a cooling curve is flat there and why")
    print("  the solidification front advances against a temperature that barely")
    print("  moves.")


def part5_descending_slab():
    section("5. Adiabatic heating of a descending parcel (100 km)")
    alpha, T, rho, cp = 3.0e-5, 1600.0, 3300.0, 1250.0
    dP = rho * STANDARD_G * 100.0e3        # Pa over 100 km
    dT = adiabatic_gradient(alpha, T, rho, cp) * dP
    print(f"  dP over 100 km = rho g dz = {dP:.4e} Pa = {dP / 1e9:.4f} GPa")
    print(f"  dT = (alpha T / rho c_p) dP = {dT:.3f} K")
    print()
    print("  A parcel that sinks 100 km without exchanging heat warms by only")
    print(f"  {dT:.1f} K. This is why the mantle adiabat is nearly isothermal in")
    print("  temperature-per-kilometre terms, and why a mantle plume can rise")
    print("  hundreds of kilometres and still be 200-300 K hotter than its")
    print("  surroundings — the excess is carried, not generated.")


if __name__ == "__main__":
    part1_sign_convention()
    part2_adiabatic_gradient()
    part3_geothermal_balance()
    part4_magma_plateau()
    part5_descending_slab()
