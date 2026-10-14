"""The petroleum system: generation, containment and geophysical signature.

Run:  .venv/bin/python petroleum_system_demo.py
Requires: Python standard library only.

Companion to lesson 04-06-01.

Output labels every number:

* COMPUTED  -- from a formula stated in the lesson (geotherm depths, Arrhenius
               rates and conversions, Athy compaction, effective stress,
               capillary column height, acoustic impedances and reflection
               coefficients, organic-carbon mass).
* MODELLED  -- a parameterisation of a particular system: the geothermal
               gradient, the kinetic coefficients, the compaction parameters,
               the interfacial tension and pore-throat radius, and the rock
               properties. They are illustrative values inside reported ranges,
               and a real study calibrates them.
* DERIVED   -- a combination of the two.

No reserve, production or recovery figure is computed anywhere in this script.
Those are economic and engineering quantities, not geophysical ones, and they
change with price, technology and regulation.

Parts:

1. Geotherm, overburden and the depth interval of the "oil window" defined by a
   temperature range.
2. Arrhenius kinetics: isothermal conversion times, and the temperature at which
   a fixed conversion is reached for different heating rates.
3. Athy compaction, bulk density, and vertical effective stress with depth.
4. Seal capacity: the buoyant column height a capillary entry pressure supports,
   for gas and for oil.
5. The seismic signature: acoustic impedance and the reflection coefficient at
   the top of a brine sand and of a gas sand.
6. Source-rock organic-carbon mass in a rock volume, with the conversion to
   hydrocarbon left as a stated model input.
"""

import math

# --------------------------------------------------------------------------
# MODELLED inputs
# --------------------------------------------------------------------------

T_SURFACE = 10.0        # [degC]
GRADIENT = 25.0e-3      # [degC/m] = 25 K/km
WINDOW = (60.0, 120.0)  # [degC] conventional liquid-hydrocarbon window

EA = 200.0e3            # [J/mol] activation energy, single-reaction model
A_FACTOR = 1.0e13       # [1/s] pre-exponential factor, single-reaction model
R_GAS = 8.314462618     # [J/(mol K)]
YEAR = 3.15576e7        # [s]

PHI0 = 0.50             # [-]
ATHY_C = 2000.0         # [m]
RHO_GRAIN = 2650.0      # [kg/m^3]
RHO_WATER = 1030.0      # [kg/m^3]
G = 9.81                # [m/s^2]

IFT_GAS_WATER = 0.030   # [N/m] nominal gas-water interfacial tension
IFT_OIL_WATER = 0.025   # [N/m] nominal oil-water interfacial tension
THROAT_R = 0.20e-6      # [m] pore-throat radius of the seal
RHO_GAS = 200.0         # [kg/m^3] at reservoir conditions (nominal)
RHO_OIL = 800.0         # [kg/m^3] (nominal)

ROCKS = {               # name: (density kg/m^3, P-wave velocity m/s)
    "shale (seal)": (2400.0, 2900.0),
    "brine sandstone": (2250.0, 3000.0),
    "gas sandstone": (2050.0, 2600.0),
    "limestone": (2600.0, 4500.0),
}

TOC = 0.04              # [-] 4 per cent total organic carbon by mass


def geotherm(z: float) -> float:
    return T_SURFACE + GRADIENT * z


def depth_for_temperature(t: float) -> float:
    return (t - T_SURFACE) / GRADIENT


def part_geotherm() -> None:
    print("=" * 72)
    print("1. GEOTHERM AND THE OIL WINDOW AS A DEPTH INTERVAL")
    print("=" * 72)
    print(f"  MODELLED surface temperature {T_SURFACE} degC, "
          f"gradient {GRADIENT * 1000:.1f} K/km")
    print("  COMPUTED T(z) = T0 + G z")
    for z in (1000.0, 2000.0, 3000.0, 4000.0, 5000.0):
        print(f"    z = {z / 1000:4.1f} km: T = {geotherm(z):7.1f} degC")
    print()
    print(f"  COMPUTED the {WINDOW[0]:.0f}-{WINDOW[1]:.0f} degC window lies at")
    for t in WINDOW:
        print(f"    {t:6.1f} degC -> {depth_for_temperature(t) / 1000:6.3f} km")
    print("  The window is a temperature interval, so its depth moves with the")
    print("  gradient. Doubling the gradient halves the depth interval:")
    for grad in (20.0e-3, 25.0e-3, 40.0e-3):
        print(f"    G = {grad * 1000:5.1f} K/km: window spans "
              f"{(WINDOW[0] - T_SURFACE) / grad / 1000:5.3f} to "
              f"{(WINDOW[1] - T_SURFACE) / grad / 1000:5.3f} km")


def rate_constant(t_celsius: float) -> float:
    return A_FACTOR * math.exp(-EA / (R_GAS * (t_celsius + 273.15)))


def part_kinetics() -> None:
    print()
    print("=" * 72)
    print("2. ARRHENIUS KINETICS OF GENERATION")
    print("=" * 72)
    print(f"  MODELLED single-reaction model: Ea = {EA / 1000:.0f} kJ/mol, "
          f"A = {A_FACTOR:.0e} 1/s")
    print("  COMPUTED k = A exp(-Ea/RT); isothermal time to 10 per cent")
    print("  conversion of a first-order reaction is t = -ln(0.9)/k")
    print("   T (degC)      k (1/s)        t (yr)")
    for t in (60.0, 80.0, 100.0, 120.0, 150.0, 180.0):
        k = rate_constant(t)
        tt = -math.log(0.9) / k / YEAR
        print(f"   {t:8.0f}   {k:.3e}   {tt:.3e}")
    print()
    print("  The single-reaction model is a MODELLED simplification. Real")
    print("  kinetic schemes use a distribution of activation energies, because")
    print("  kerogen is a mixture; the qualitative result -- a strong")
    print("  temperature dependence and a shift of the window with heating rate")
    print("  -- survives, the absolute temperatures do not.")
    print()
    print("  COMPUTED heating-rate dependence. Integrate the conversion along a")
    print("  linear heating path T = T0 + beta t until it reaches 10 per cent:")
    print("    beta (K/Myr)   T at 10 per cent (degC)")
    for beta_k_per_myr in (1.0, 3.0, 10.0, 30.0):
        beta = beta_k_per_myr / 1.0e6 / YEAR    # [K/s]
        # Integrate dC/dt = k(T) (1 - C) with RK4 on C.
        t = 0.0
        c = 0.0
        dt = 1.0e10                            # [s] ~ 317 yr
        t_max = 200.0e6 * YEAR
        while t < t_max and c < 0.10:
            temp = T_SURFACE + beta * t
            k = A_FACTOR * math.exp(-EA / (R_GAS * (temp + 273.15)))
            c += k * (1.0 - c) * dt
            t += dt
        print(f"    {beta_k_per_myr:12.1f}   {T_SURFACE + beta * t:17.1f}")
    print("  A reaction with a large activation energy moves to higher")
    print("  temperature as the heating rate rises: the same source rock that")
    print("  generates on a slow subsidence path needs a deeper, hotter burial")
    print("  if it is heated quickly. That is why burial history, not present")
    print("  depth, is the quantity a basin model predicts.")


def part_compaction() -> None:
    print()
    print("=" * 72)
    print("3. COMPACTION, DENSITY AND EFFECTIVE STRESS")
    print("=" * 72)
    print(f"  MODELLED Athy law phi = phi0 exp(-z/c), phi0 = {PHI0}, "
          f"c = {ATHY_C:.0f} m")
    print(f"           grain density {RHO_GRAIN} kg/m^3, pore water "
          f"{RHO_WATER} kg/m^3")
    print("   z (m)    phi      rho_bulk (kg/m^3)   sigma_v (MPa)   sigma_v' (MPa)")
    sigma_v = 0.0
    sigma_vp = 0.0
    z_prev = 0.0
    for z in (0.0, 500.0, 1000.0, 2000.0, 3000.0, 4000.0):
        phi = PHI0 * math.exp(-z / ATHY_C)
        rho = phi * RHO_WATER + (1.0 - phi) * RHO_GRAIN
        if z > z_prev:
            dz = z - z_prev
            phi_mid = PHI0 * math.exp(-(z + z_prev) / 2.0 / ATHY_C)
            rho_mid = phi_mid * RHO_WATER + (1.0 - phi_mid) * RHO_GRAIN
            sigma_v += rho_mid * G * dz / 1e6
            sigma_vp += (rho_mid - RHO_WATER) * G * dz / 1e6
            z_prev = z
        print(f"   {z:6.0f}   {phi:.4f}      {rho:8.1f}        "
              f"{sigma_v:8.2f}      {sigma_vp:8.2f}")
    print("  COMPUTED sigma_v is the overburden (lithostatic) pressure and")
    print("  sigma_v' the vertical effective stress, sigma_v' = sigma_v - p_pore")
    print("  with a hydrostatic pore pressure. The effective stress is what")
    print("  compacts the rock and what a velocity-porosity relation responds to.")
    print()
    print("  COMPUTED one-way and two-way seismic time through the column using")
    print("  the MODELLED linear velocity trend v(z) = 1500 + 1.2 z (m/s):")
    print("    t(z) = integral dz/v = ln(1 + 1.2 z/1500)/1.2, TWT = 2 t")
    for z in (1000.0, 2000.0, 3000.0, 4000.0):
        t_one = math.log(1.0 + 1.2 * z / 1500.0) / 1.2
        print(f"    z = {z / 1000:4.1f} km: v = {1500 + 1.2 * z:6.0f} m/s, "
              f"one-way {t_one:6.3f} s, TWT {2.0 * t_one:6.3f} s")
    print("  Depth in metres and depth in seconds are different maps of the same")
    print("  rock, and a seismic section is indexed in the second one. Time-to-")
    print("  depth conversion needs this velocity model, and the model is a")
    print("  MODELLED trend, not a measurement, wherever no well is present.")


def seal_column(ift: float, d_rho: float, r_throat: float) -> tuple[float, float]:
    p_c = 2.0 * ift / r_throat
    h = p_c / (d_rho * G)
    return p_c, h


def part_seal() -> None:
    print()
    print("=" * 72)
    print("4. SEAL CAPACITY AND BUOYANT COLUMN HEIGHT")
    print("=" * 72)
    print(f"  MODELLED pore-throat radius r = {THROAT_R * 1e6:.2f} micron,")
    print(f"           gas-water IFT {IFT_GAS_WATER} N/m, "
          f"oil-water IFT {IFT_OIL_WATER} N/m")
    print("  COMPUTED capillary entry pressure P_c = 2 sigma cos(theta)/r with")
    print("  cos(theta) = 1, and the column it supports h = P_c/(d_rho g)")
    for label, ift, rho_hc in (("gas", IFT_GAS_WATER, RHO_GAS),
                               ("oil", IFT_OIL_WATER, RHO_OIL)):
        d_rho = RHO_WATER - rho_hc
        p_c, h = seal_column(ift, d_rho, THROAT_R)
        print(f"    {label}: d_rho = {d_rho:6.0f} kg/m^3, P_c = {p_c:.3e} Pa, "
              f"h_max = {h:8.2f} m")
    print()
    print("  COMPUTED sensitivity to the throat radius, which is the least")
    print("  well-known input:")
    for r in (0.05e-6, 0.10e-6, 0.20e-6, 1.00e-6):
        _, h = seal_column(IFT_GAS_WATER, RHO_WATER - RHO_GAS, r)
        print(f"    r = {r * 1e6:5.2f} micron: h_max(gas) = {h:9.2f} m")
    print("  The column height is inversely proportional to the throat radius,")
    print("  which is why a seal's quality is a pore-scale measurement and why")
    print("  it is usually reported as a distribution rather than a number.")


def part_seismic() -> None:
    print()
    print("=" * 72)
    print("5. SEISMIC SIGNATURE OF THE RESERVOIR")
    print("=" * 72)
    print("  MODELLED nominal properties (ranges, not measurements of a field):")
    for name, (rho, vp) in ROCKS.items():
        print(f"    {name:18s} rho = {rho:6.0f} kg/m^3, vp = {vp:5.0f} m/s, "
              f"Z = {rho * vp / 1e6:7.3f} MRayl")
    z_shale = ROCKS["shale (seal)"][0] * ROCKS["shale (seal)"][1]
    print()
    print("  COMPUTED R = (Z2 - Z1)/(Z2 + Z1) at the top of each unit, shale above")
    for name in ("brine sandstone", "gas sandstone", "limestone"):
        rho, vp = ROCKS[name]
        z = rho * vp
        r = (z - z_shale) / (z + z_shale)
        print(f"    shale over {name:16s}: R = {r:+.4f}")
    z_brine = ROCKS["brine sandstone"][0] * ROCKS["brine sandstone"][1]
    z_gas = ROCKS["gas sandstone"][0] * ROCKS["gas sandstone"][1]
    r_b = (z_brine - z_shale) / (z_brine + z_shale)
    r_g = (z_gas - z_shale) / (z_gas + z_shale)
    print(f"  COMPUTED amplitude ratio gas sand / brine sand = "
          f"{abs(r_g) / abs(r_b):.2f}")
    print("  Both are negative (a soft, low-impedance unit below a harder one),")
    print("  so both are troughs, and the gas case is an order of magnitude")
    print("  larger. That is the physical content of a 'bright spot': a")
    print("  fluid-substitution effect on density and P-wave velocity, with the")
    print("  S-wave velocity nearly unchanged, which is why an amplitude")
    print("  anomaly alone is not proof of gas.")


def part_source_rock() -> None:
    print()
    print("=" * 72)
    print("6. ORGANIC CARBON IN A SOURCE ROCK")
    print("=" * 72)
    print(f"  MODELLED total organic carbon TOC = {TOC * 100:.1f} per cent by mass")
    print("  COMPUTED organic carbon mass m_C = TOC x rho_bulk x V")
    for area_km2, thickness in ((100.0, 50.0), (1000.0, 100.0)):
        v = area_km2 * 1e6 * thickness
        phi = PHI0 * math.exp(-2500.0 / ATHY_C)
        rho = phi * RHO_WATER + (1.0 - phi) * RHO_GRAIN
        m_c = TOC * rho * v
        print(f"    {area_km2:7.0f} km^2 x {thickness:5.0f} m at phi = {phi:.3f}: "
              f"m_C = {m_c:.3e} kg = {m_c / 1e12:.3f} Gt")
    print("  The mass of organic carbon is a physical quantity computable from a")
    print("  measured TOC and a rock volume. What fraction of it is converted to")
    print("  hydrocarbon, what fraction is expelled, and what fraction is")
    print("  recoverable are three further questions, and only the first is even")
    print("  partly a geophysical one. The other two are kinetic, geological and")
    print("  engineering quantities, and no number is offered for them here.")


def main() -> None:
    assert abs(depth_for_temperature(60.0) - 2000.0) < 1e-6
    assert rate_constant(120.0) > rate_constant(80.0)
    part_geotherm()
    part_kinetics()
    part_compaction()
    part_seal()
    part_seismic()
    part_source_rock()
    print()
    print("All assertions passed.")


if __name__ == "__main__":
    main()
