"""Phase equilibria: Clapeyron slopes, mantle discontinuities, the inner core.

Run:  python3 phase_equilibria_demo.py
Requires: Python standard library only.

Companion to lesson 02-05-07.

Every pressure, temperature and Clapeyron slope used here is NOMINAL and, at
core and transition-zone conditions, carries a factor-of-two uncertainty. The
pressures at the CMB, ICB and centre are adopted model values from the
Preliminary Reference Earth Model; they are not derived in this script and
should not be quoted as measurements.

What the script does compute, from thermodynamics alone, is:

1. The Clausius-Clapeyron relation dP/dT = L/(T dV), checked against the
   measured pressure-melting behaviour of ice.
2. The depth shift of the 410 km and 660 km discontinuities for a +/-100 K
   perturbation of the geotherm, from dz = gamma dT/(rho g).
3. The adiabatic gradient inside the outer core, dT/dP = alpha T/(rho c_p).
4. The melting-curve slope that the solid inner core requires, and the
   demonstration that the inner core is solid while being ~1000 K hotter than
   the outermost outer core.
5. The latent heat and entropy released by growth of the inner core.
"""

import math

STANDARD_G = 9.80665

# Adopted model pressures (PREM; model values, not measurements).
P_CMB, P_ICB, P_CENTRE = 135.0e9, 329.0e9, 364.0e9


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def part1_clausius_clapeyron():
    section("1. The Clausius-Clapeyron relation, checked on ice")
    print("  dP/dT = dS/dV = L / (T dV),  with dV = V_liquid - V_solid")
    L, T0, rho_s, rho_l = 3.34e5, 273.15, 917.0, 1000.0
    dV = 1.0 / rho_l - 1.0 / rho_s
    dS = L / T0
    dPdT = dS / dV
    print(f"  ice: L = {L:.3e} J/kg, T = {T0:.2f} K, "
          f"rho_ice = {rho_s:.0f}, rho_water = {rho_l:.0f} kg/m3")
    print(f"  dV = 1/1000 - 1/917 = {dV:.6e} m3/kg  (NEGATIVE: water is denser)")
    print(f"  dS = L/T = {dS:.4f} J kg^-1 K^-1")
    print(f"  dP/dT = {dPdT:.6e} Pa/K = {dPdT / 1e6:.4f} MPa/K")
    print(f"  dT/dP = {1.0 / dPdT * 1e6:.6f} K/MPa")
    print()
    print("  The sign is the physics. dV < 0 makes dT/dP < 0: pressure LOWERS")
    print("  the melting point of ice by about 0.074 K per MPa. That is why a")
    print("  glacier can slide on a water film and why the effect is far too")
    print("  small to explain skating. Squeeze an ice cube and it melts; the")
    print("  same equation with dV > 0, as for almost every silicate, gives the")
    print("  opposite sign and pressure RAISES the melting point.")


def part2_discontinuities():
    section("2. Pressure and depth of the mantle discontinuities")
    print("  Estimate P = rho g z (uniform density; a first approximation):")
    for name, rho, z_km, actual in (("410 km", 3400.0, 410.0, 13.5),
                                    ("660 km", 3900.0, 660.0, 23.5)):
        P = rho * STANDARD_G * z_km * 1e3
        print(f"  {name:<8} rho = {rho:.0f} kg/m3 -> P = {P / 1e9:.2f} GPa "
              f"(commonly quoted near {actual:.1f} GPa)")
    print("  The uniform-density estimate overshoots at greater depth because")
    print("  the real density is not constant and g falls; these are rough")
    print("  figures, not PREM values.")
    print()
    print("  Depth shift of a phase boundary for a geotherm perturbation dT:")
    print("       dz = gamma dT / (rho g),   gamma = dP/dT")
    print(f"{'boundary':<12}{'gamma (MPa/K)':>15}{'rho (kg/m3)':>13}"
          f"{'dT (K)':>9}{'dz (km)':>10}")
    for name, gamma, rho, dT in (("410", 2.5e6, 3400.0, +100.0),
                                 ("410", 2.5e6, 3400.0, -100.0),
                                 ("660", -2.5e6, 4000.0, +100.0),
                                 ("660", -2.5e6, 4000.0, -100.0)):
        dz = gamma * dT / (rho * STANDARD_G)
        print(f"{name:<12}{gamma / 1e6:>15.1f}{rho:>13.0f}{dT:>9.0f}"
              f"{dz / 1e3:>10.2f}")
    print()
    print("  The signs differ because the 410 (olivine -> wadsleyite) slope is")
    print("  positive and the 660 (ringwoodite -> bridgmanite + periclase) slope")
    print("  is negative. A hot mantle and a cold slab therefore displace the two")
    print("  boundaries in OPPOSITE directions, which thickens or thins the")
    print("  transition zone. That is the seismological observable: seismic")
    print("  receivers detect a deepened 660 km boundary above subducting")
    print("  slabs, and it is explained by a negative Clapeyron slope, not")
    print("  fitted by it.")
    print()
    print("  A 100 K perturbation moves a boundary by only 6-8 km. Resolving")
    print("  that requires receiver functions with km-scale depth control, which")
    print("  is why this is a hard measurement rather than a routine one.")


def part3_core_adiabat():
    section("3. The adiabatic gradient in the outer core")
    alpha, T, rho, cp = 1.0e-5, 4500.0, 11500.0, 700.0
    s_ad = alpha * T / (rho * cp)
    print("  dT/dP|_ad = alpha T / (rho c_p)  -- exactly the isentropic")
    print("  gradient for a homogeneous medium (lesson 02-05-02).")
    print(f"  alpha = {alpha:.1e} /K, T = {T:.0f} K, rho = {rho:.0f} kg/m3, "
          f"c_p = {cp:.0f} J kg^-1 K^-1")
    print(f"  dT/dP = {s_ad:.4e} K/Pa = {s_ad * 1e9:.3f} K/GPa")
    dP = P_ICB - P_CMB
    dT = s_ad * dP
    print(f"  dP across the outer core = {dP / 1e9:.0f} GPa")
    print(f"  adiabatic temperature rise CMB -> ICB = {dT:.1f} K")
    T_CMB = 4000.0
    T_ICB_ad = T_CMB + dT
    print(f"  with an adopted T_CMB = {T_CMB:.0f} K, the adiabat reaches")
    print(f"  {T_ICB_ad:.1f} K at the inner-core boundary")
    return s_ad, T_CMB, T_ICB_ad, dP


def part4_inner_core_solid():
    section("4. Why the inner core is solid and hotter than the outer core")
    s_ad, T_CMB, T_ICB_ad, dP = part3_core()
    print("  The outer core is liquid at its top, so there the adiabat lies")
    print("  ABOVE the melting curve: T_ad(P_CMB) > T_m(P_CMB).")
    print("  The inner core is solid, so at the ICB the melting curve has")
    print("  caught up: T_m(P_ICB) = T_ad(P_ICB).")
    T_m_CMB = 3600.0
    s_m = (T_ICB_ad - T_m_CMB) / dP
    print()
    print(f"  Adopt T_m(P_CMB) = {T_m_CMB:.0f} K (below the adiabat, hence")
    print("  liquid at the top of the outer core). Requiring the two curves to")
    print("  meet at the ICB gives an average melting slope")
    print(f"    s_m = ({T_ICB_ad:.1f} - {T_m_CMB:.0f}) / {dP / 1e9:.0f} GPa"
          f" = {s_m * 1e9:.3f} K/GPa")
    print(f"  against the computed adiabatic slope {s_ad * 1e9:.3f} K/GPa.")
    print(f"  The melting curve is steeper by a factor "
          f"{s_m / s_ad:.3f}.")
    print()
    print("  Now extend both to the centre:")
    print(f"{'location':<14}{'P (GPa)':>10}{'T_ad (K)':>11}{'T_m (K)':>11}"
          f"{'T_m - T_ad':>12}{'state':>9}")
    for name, P in (("CMB", P_CMB), ("mid outer core", 0.5 * (P_CMB + P_ICB)),
                    ("ICB", P_ICB), ("centre", P_CENTRE)):
        Tad = T_CMB + s_ad * (P - P_CMB)
        Tm = T_m_CMB + s_m * (P - P_CMB)
        if abs(Tm - Tad) < 1.0:
            state = "BOUNDARY"
        else:
            state = "solid" if Tm > Tad else "liquid"
        print(f"{name:<14}{P / 1e9:>10.1f}{Tad:>11.1f}{Tm:>11.1f}"
              f"{Tm - Tad:>12.1f}{state:>9}")
    T_centre = T_CMB + s_ad * (P_CENTRE - P_CMB)
    print()
    print("  Read the centre row against the CMB row. The centre of the inner")
    print(f"  core is at {T_centre:.0f} K and is SOLID; the outermost outer core")
    print(f"  is at {T_CMB:.0f} K and is LIQUID — hotter by {T_centre - T_CMB:.0f} K")
    print("  and solid all the same. Pressure, not temperature, decides the")
    print("  phase: the melting curve rises faster with pressure than the adiabat")
    print("  does, so descending material is dragged from the liquid side of the")
    print("  melting curve to the solid side.")
    print()
    print("  The margin at the centre is only "
          f"{(T_m_CMB + s_m * (P_CENTRE - P_CMB)) - (T_CMB + s_ad * (P_CENTRE - P_CMB)):.0f} K")
    print("  in this model, which is far smaller than the uncertainty on any")
    print("  input. The conclusion that the inner core is solid is robust; the")
    print("  numbers are not. Every slope and temperature above is nominal.")


def part5_latent_heat():
    section("5. Latent heat and entropy of inner-core growth")
    r_icb = 1221.0e3
    rho_ic, L_iron = 12800.0, 2.5e5
    V = (4.0 / 3.0) * math.pi * r_icb ** 3
    M = rho_ic * V
    Q = L_iron * M
    T_ic = 5200.0
    print(f"  Inner-core radius {r_icb / 1e3:.0f} km, "
          f"rho = {rho_ic:.0f} kg/m3, L = {L_iron:.1e} J/kg (nominal)")
    print(f"  Volume = {V:.4e} m3,  Mass = {M:.4e} kg")
    print(f"  Total latent heat released to date = L M = {Q:.4e} J")
    print(f"  Entropy = Q/T with T ~ {T_ic:.0f} K -> {Q / T_ic:.4e} J/K")
    print()
    annual_loss = 4.4e13 * 3.15576e7
    print(f"  One year of the Earth's total surface heat loss (at 44 TW) is")
    print(f"  {annual_loss:.4e} J, so the cumulative latent heat of the inner")
    print(f"  core equals {Q / annual_loss:.3e} years of that loss — but it was")
    print("  released over billions of years, so the cumulative figure says")
    print("  nothing about the present-day power.")
    v_growth = 1.0e-3 / 3.15576e7                # 1 mm/yr, ADOPTED growth rate
    dMdt = 4.0 * math.pi * r_icb ** 2 * rho_ic * v_growth
    P = L_iron * dMdt
    print()
    print("  For the present-day power, adopt a growth rate of 1 mm/yr:")
    print(f"    v = 1 mm/yr = {v_growth:.4e} m/s (nominal, poorly constrained)")
    print(f"    dM/dt = 4 pi r^2 rho v = {dMdt:.4e} kg/s")
    print(f"    P = L dM/dt = {P:.4e} W = {P / 1e12:.2f} TW")
    print()
    print("  A couple of terawatts is a real contribution to the energy budget")
    print("  of the core, and it is the reason the inner core keeps growing")
    print("  while the geodynamo is driven partly by the buoyancy of the light")
    print("  elements rejected at the freezing front. The growth rate is not")
    print("  measured directly; it is inferred from the thermal history, and")
    print("  that inference is model-dependent.")


def part3_core():
    alpha, T, rho, cp = 1.0e-5, 4500.0, 11500.0, 700.0
    s_ad = alpha * T / (rho * cp)
    return s_ad, 4000.0, 4000.0 + s_ad * (P_ICB - P_CMB), P_ICB - P_CMB


if __name__ == "__main__":
    part1_clausius_clapeyron()
    part2_discontinuities()
    part3_core_adiabat()
    part4_inner_core_solid()
    part5_latent_heat()
