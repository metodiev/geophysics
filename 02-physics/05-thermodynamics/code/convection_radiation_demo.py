"""Convection, radiation and combined heat transfer.

Run:  python3 convection_radiation_demo.py
Requires: Python standard library only.

Companion to lesson 02-05-05. Material properties are nominal; the
Stefan-Boltzmann constant is exact by definition.

The script:

1. Computes the Rayleigh number for four geophysical systems and compares each
   with the critical value ~1000.
2. Uses Nu ~ 0.1 Ra^(1/3) to convert each Rayleigh number into a convective
   heat flux, and compares it with the purely conductive flux.
3. Computes blackbody radiative fluxes and the radiative heat-transfer
   coefficient 4 sigma T^3 over the range of temperatures that matter in
   geophysics.
4. Computes the Earth's effective radiating temperature from an adopted solar
   constant and albedo.
5. Compares conduction, convection and radiation at a lava surface.
"""

import math

SIGMA = 5.670374419e-8         # W m^-2 K^-4, exact


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def rayleigh(rho, alpha, dT, d, kappa, eta):
    """Ra = rho g alpha dT d^3 / (kappa eta). g = 9.80665 m/s^2 (exact)."""
    g = 9.80665
    return rho * g * alpha * dT * d ** 3 / (kappa * eta)


SYSTEMS = {
    "whole mantle":  {"rho": 3300.0, "alpha": 3.0e-5, "dT": 2500.0,
                      "d": 2.9e6, "kappa": 1.0e-6, "eta": 1.0e21, "k": 4.0},
    "upper mantle":  {"rho": 3300.0, "alpha": 3.0e-5, "dT": 1300.0,
                      "d": 6.6e5, "kappa": 1.0e-6, "eta": 1.0e20, "k": 4.0},
    "water 1 m":     {"rho": 1000.0, "alpha": 2.0e-4, "dT": 10.0,
                      "d": 1.0, "kappa": 1.433e-7, "eta": 1.0e-3, "k": 0.60},
    "lava lake 10 m": {"rho": 2600.0, "alpha": 5.0e-5, "dT": 300.0,
                       "d": 10.0, "kappa": 1.0e-6, "eta": 100.0, "k": 1.8},
}
RA_CRITICAL = 1000.0           # nominal, rigid-rigid Rayleigh-Benard onset


def part1_rayleigh():
    section("1. Rayleigh number for geophysical systems")
    print(f"{'system':<16}{'Ra':>12}{'Ra/Ra_c':>12}{'Nu = 0.1 Ra^1/3':>18}")
    for name, p in SYSTEMS.items():
        Ra = rayleigh(p["rho"], p["alpha"], p["dT"], p["d"], p["kappa"],
                      p["eta"])
        Nu = 0.1 * Ra ** (1.0 / 3.0)
        print(f"{name:<16}{Ra:>12.3e}{Ra / RA_CRITICAL:>12.3e}{Nu:>18.2f}")
    print()
    print("  Every system here exceeds the critical value by three to eight")
    print("  orders of magnitude. Convection is not marginal anywhere in")
    print("  geophysics: it is the default state of any fluid layer heated from")
    print("  below, from the outer core to the atmosphere.")
    print()
    print("  The contrast that matters is the viscosity: the mantle's is ~1e21")
    print("  Pa s, twenty-four orders of magnitude above water's. Convection is")
    print("  the same instability in both; only the speed differs, from metres")
    print("  per second (water) to centimetres per year (mantle).")


def part2_nusselt():
    section("2. Convective versus conductive heat transport")
    print("  q_cond = k dT/d,   q_conv = Nu q_cond,   Nu ~ 0.1 Ra^(1/3)")
    print(f"{'system':<16}{'q_cond (W/m2)':>16}{'Nu':>10}"
          f"{'q_conv (W/m2)':>16}{'q_conv (mW/m2)':>17}")
    for name, p in SYSTEMS.items():
        Ra = rayleigh(p["rho"], p["alpha"], p["dT"], p["d"], p["kappa"],
                      p["eta"])
        Nu = 0.1 * Ra ** (1.0 / 3.0)
        q_cond = p["k"] * p["dT"] / p["d"]
        q_conv = Nu * q_cond
        print(f"{name:<16}{q_cond:>16.4e}{Nu:>10.1f}{q_conv:>16.4e}"
              f"{q_conv * 1e3:>17.2f}")
    print()
    print("  The mantle figure is a model result: with the adopted parameters it")
    print("  gives a convective flux within a factor of ~2 of the observed")
    print("  mean surface heat flow, which is the sense in which the scaling is")
    print("  useful. It is a one-third-power law with an empirical prefactor,")
    print("  not a prediction to two digits.")
    print()
    print("  Regime of validity: Nu ~ 0.1 Ra^(1/3) is a high-Rayleigh-number")
    print("  boundary-layer scaling for a plane layer with negligible internal")
    print("  heating and no phase changes. It fails for the strongly")
    print("  temperature-dependent viscosity of the real mantle, which is why")
    print("  mantle-convection modelling uses a different viscosity law.")


def part3_radiation():
    section("3. Blackbody radiation: flux and radiative coefficient")
    print("  F = sigma T^4,   h_rad = dF/dT = 4 sigma T^3")
    print(f"{'T (K)':>10}{'F (W/m2)':>16}{'h_rad (W/m2/K)':>18}"
          f"   {'example':<34}")
    examples = {254.6: "Earth effective radiating temperature",
                288.0: "Earth mean surface",
                373.15: "boiling water",
                1000.0: "hot lava crust",
                1400.0: "erupting lava",
                5772.0: "photosphere"}
    for T, label in examples.items():
        F = SIGMA * T ** 4
        print(f"{T:>10.1f}{F:>16.4e}{4 * SIGMA * T ** 3:>18.4f}"
              f"   {label:<34}")
    print()
    T1, T2 = 288.0, 1400.0
    print(f"  Scaling: raising T from {T1:.0f} K to {T2:.0f} K multiplies the")
    print(f"  radiative flux by {(T2 / T1) ** 4:.3f}, i.e. T^4 is violent. A")
    print("  composition change cannot compete with a temperature change: this")
    print("  is why lava at 1400 K is visible from space while the same rock at")
    print("  300 K is not.")
    print()
    print("  The radiative coefficient h_rad is comparable to a natural-")
    print("  convection coefficient in air (5-25 W m^-2 K^-1) near 300 K, and")
    print("  larger than any convective coefficient near 1400 K. So radiation")
    print("  and convection compete at ambient temperature and radiation wins")
    print("  outright once a surface is hot. For a planetary surface there is no")
    print("  competition at all: radiation is the only channel to space.")
    print("  Regime of validity: the blackbody formula assumes an optically")
    print("  thick, non-scattering emitter. A real surface is described by an")
    print("  emissivity epsilon <= 1, and a transparent gas layer (the")
    print("  atmosphere) requires line-by-line radiative transfer instead.")


def part4_earth_energy_balance():
    section("4. The Earth's effective radiating temperature")
    S, albedo = 1361.0, 0.30      # solar constant and planetary albedo, adopted
    absorbed = S * (1.0 - albedo) / 4.0
    T_e = (absorbed / SIGMA) ** 0.25
    print(f"  adopted solar constant S = {S:.0f} W/m2 (nominal), "
          f"albedo a = {albedo:.2f} (nominal)")
    print(f"  absorbed flux per unit area, S(1-a)/4 = {absorbed:.4f} W/m2")
    print(f"  T_e = (S(1-a)/(4 sigma))^(1/4) = {T_e:.4f} K "
          f"= {T_e - 273.15:.2f} C")
    print()
    print("  Sensitivity: dT_e/dS = T_e/(4S) = "
          f"{T_e / (4 * S):.6f} K per W/m2, so a 1 per cent change in S")
    print(f"  moves T_e by {(T_e / (4 * S)) * 0.01 * S:.3f} K. The fourth power")
    print("  is what makes the surface temperature stable against modest")
    print("  changes in absorbed flux and catastrophic against large ones.")
    print()
    q_geothermal = 0.087
    print(f"  For comparison, the geothermal flux of ~{q_geothermal:.3f} W/m2 is")
    print(f"  {q_geothermal / absorbed:.3e} of the absorbed solar flux. The")
    print("  Earth's internal heat engine is irrelevant to surface climate and")
    print("  decisive for tectonics; conflating the two is a classic error.")


def part5_lava_surface():
    section("5. Combined transfer at a lava surface (1400 K)")
    T_lava, T_air, k_lava, d = 1400.0, 300.0, 1.8, 1.0
    q_rad = SIGMA * T_lava ** 4
    q_cond = k_lava * (T_lava - T_air) / d
    h_conv = 15.0                 # nominal natural-convection coefficient
    q_conv = h_conv * (T_lava - T_air)
    print(f"{'mechanism':<26}{'flux (W/m2)':>16}{'share':>12}")
    total = q_rad + q_cond + q_conv
    for name, q in (("radiation", q_rad),
                    (f"conduction through 1 m rock", q_cond),
                    ("natural convection in air", q_conv)):
        print(f"{name:<26}{q:>16.4e}{q / total:>12.6f}")
    print(f"{'total':<26}{total:>16.4e}{1.0:>12.6f}")
    print()
    print("  Radiation carries the overwhelming majority of the heat; convection")
    print("  to the air takes a few per cent and conduction into the rock less")
    print("  than one per cent. That is why a lava lake crusts over only when")
    print("  radiation is suppressed, and why the radiative cooling rate of")
    print("  magma bodies sets their solidification time at the surface but not")
    print("  at depth, where conduction in the host rock takes over.")


def part6_wien():
    section("6. Wien displacement: where the radiation peaks")
    h = 6.62607015e-34            # J s, exact
    c = 299792458.0               # m/s, exact
    kB = 1.380649e-23             # J/K, exact
    x_wien = 4.965114231744276    # root of x = 5(1 - e^-x)
    b = h * c / (x_wien * kB)
    print("  lambda_max T = h c / (x k_B), with x the root of x = 5(1-e^-x).")
    print(f"  x = {x_wien:.9f},  b = {b:.6e} m K  (= {b * 1e3:.5f} mm K)")
    print(f"{'T (K)':>10}{'lambda_max (um)':>18}{'band':>14}")
    for T, band in ((5772.0, "visible"), (1400.0, "near IR"),
                    (288.0, "thermal IR"), (254.5781, "thermal IR")):
        lam = b / T
        print(f"{T:>10.4f}{lam * 1e6:>18.4f}{band:>14}")
    print()
    print("  The Sun radiates in the visible and the Earth in the thermal")
    print("  infrared, and the two spectra barely overlap. That separation is")
    print("  why the atmosphere can be transparent to sunlight and opaque to")
    print("  infrared at the same time, which is the whole of the greenhouse")
    print("  effect, and why a radiative balance cannot be computed with a")
    print("  single grey emissivity.")


def part7_peclet():
    section("7. Advection versus conduction: the Peclet number")
    kap = 1.157e-6
    L = 1.0e3
    print("  Pe = v L / kappa. Pe > 1 means advection, not conduction,")
    print("  controls the temperature field. For groundwater at L = 1 km and")
    print(f"  kappa = {kap:.3e} m2/s:")
    print(f"{'v (m/yr)':>12}{'v (m/s)':>14}{'Pe':>12}{'regime':>22}")
    for v_yr in (0.01, 0.0365, 0.1, 1.0, 10.0, 100.0):
        v = v_yr / 3.15576e7
        Pe = v * L / kap
        regime = "conduction" if Pe < 1 else "advection"
        print(f"{v_yr:>12.4f}{v:>14.4e}{Pe:>12.4f}{regime:>22}")
    print()
    print(f"  The crossover is at v = kappa/L = {kap / L:.4e} m/s = "
          f"{kap / L * 3.15576e7 * 100:.3f} cm/yr.")
    print("  Groundwater moving faster than a few centimetres per year")
    print("  carries more heat than conduction does over a kilometre. This is")
    print("  why heat flow in sedimentary basins and geothermal fields is")
    print("  routinely dominated by fluid flow, and why a conductive geotherm")
    print("  fitted to a well in an aquifer province can be badly wrong.")
    print()
    print("  The Peclet number is the right tool when a flow field is imposed")
    print("  from outside (groundwater, a hydrothermal plume). When the flow")
    print("  is self-organised by buoyancy, the Rayleigh number is the right")
    print("  tool instead, because there is no externally set velocity.")


if __name__ == "__main__":
    part1_rayleigh()
    part2_nusselt()
    part3_radiation()
    part4_earth_energy_balance()
    part5_lava_surface()
    part6_wien()
    part7_peclet()
