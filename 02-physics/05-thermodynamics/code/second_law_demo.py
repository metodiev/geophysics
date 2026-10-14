"""The second law: entropy, irreversibility and the direction of heat flow.

Run:  python3 second_law_demo.py
Requires: Python standard library only.

Companion to lesson 02-05-03. Material properties are nominal; the
Stefan-Boltzmann constant and the Boltzmann constant are exact by definition.

The script:

1. Computes the entropy change of a body receiving heat at temperature T.
2. Shows that heat conduction down a temperature gradient produces positive
   entropy and that the reverse process would destroy entropy.
3. Integrates the local entropy production rate k (grad T)^2 / T^2 down a
   conductive geotherm, and converts it to a global rate.
4. Tabulates Carnot limits against real geothermal conversion efficiencies.
5. Computes the entropy of fusion of rock, of the Earth's secular cooling, and
   of the degradation of solar radiation to terrestrial infrared.
"""

import math

SIGMA = 5.670374419e-8        # W m^-2 K^-4  Stefan-Boltzmann, exact
EARTH_AREA = 5.10e14          # m^2          nominal, derived from mean radius
MANTLE_CP = 1250.0            # J kg^-1 K^-1 nominal
MANTLE_MASS = 4.0e24          # kg           nominal (Earth minus core and crust)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def part1_entropy_change():
    section("1. Entropy change of a body receiving heat")
    print("  dS = Q / T  (reversible, at constant temperature T)")
    print(f"{'Q (J)':>12}{'T (K)':>10}{'dS (J/K)':>16}")
    for Q, T in ((1.0e6, 300.0), (1.0e6, 1000.0), (1.0e6, 3000.0),
                 (4.08e18, 1500.0)):
        print(f"{Q:>12.3e}{T:>10.0f}{Q / T:>16.6e}")
    print()
    print("  The same heat delivered at a lower temperature changes the entropy")
    print("  far more. That single fact explains why low-temperature heat is")
    print("  cheap and high-temperature heat is scarce: the second law prices")
    print("  heat by its temperature, not its energy.")


def part2_conduction_entropy():
    section("2. Entropy production in steady conduction")
    q = 0.065              # W/m^2 conducted upward through the lithosphere
    print("  Heat q crosses from a hot boundary T_h to a cold boundary T_c.")
    print("  Entropy produced per unit area = q (1/T_c - 1/T_h).")
    print(f"{'T_h (K)':>10}{'T_c (K)':>10}{'q (W/m2)':>12}"
          f"{'sigma (W/m2/K)':>18}")
    for T_h, T_c in ((1600.0, 283.0), (800.0, 283.0), (373.0, 283.0),
                     (1600.0, 1600.0)):
        s = q * (1.0 / T_c - 1.0 / T_h)
        print(f"{T_h:>10.1f}{T_c:>10.1f}{q:>12.4f}{s:>18.6e}")
    print()
    print("  The last row has no temperature difference and produces no entropy:")
    print("  heat flow is possible without entropy production only in the")
    print("  reversible limit of a vanishing gradient, which carries a vanishing")
    print("  flux. Reversing the flow gives sigma < 0, which the second law")
    print("  forbids. This is the formal statement that heat flows down the")
    print("  geotherm and never up.")


def part3_geotherm_integral():
    section("3. Entropy production inside the lithosphere")
    print("  For T(z) = T0 + G z and constant k, sigma = k G (1/T0 - 1/T_H)")
    print("  per unit area (the integral of k (dT/dz)^2 / T^2 over the column).")
    T0, T_H, H, k = 283.0, 1600.0, 150.0e3, 3.0
    G = (T_H - T0) / H
    sigma = k * G * (1.0 / T0 - 1.0 / T_H)
    print(f"  T0 = {T0:.0f} K, T_H = {T_H:.0f} K, H = {H / 1e3:.0f} km, "
          f"k = {k:.1f} W m^-1 K^-1")
    print(f"  G = {G * 1e3:.4f} K/km")
    print(f"  sigma = k G (1/T0 - 1/T_H) = {sigma:.6e} W m^-2 K^-1")
    print(f"  globally: {sigma * EARTH_AREA:.4e} W/K")
    print()
    print("  Conductive entropy production in the whole lithosphere is a few")
    print("  times 1e10 W/K. Hold that number against Section 5.")


def part4_carnot():
    section("4. Carnot limit versus realised geothermal conversion")
    print("  eta_Carnot = 1 - T_c/T_h with both temperatures in kelvin.")
    print(f"{'T_h (C)':>10}{'T_c (C)':>10}{'T_h (K)':>10}{'T_c (K)':>10}"
          f"{'eta_Carnot':>13}{'eta_real (nominal)':>20}")
    for T_hc, T_cc, eta_real in ((200.0, 25.0, 0.12), (150.0, 25.0, 0.10),
                                 (300.0, 25.0, 0.20), (90.0, 25.0, 0.06)):
        T_h = T_hc + 273.15
        T_c = T_cc + 273.15
        print(f"{T_hc:>10.1f}{T_cc:>10.1f}{T_h:>10.2f}{T_c:>10.2f}"
              f"{1 - T_c / T_h:>13.4f}{eta_real:>20.2f}")
    print()
    print("  Real plants reach roughly 40-60 per cent of their Carnot bound, the")
    print("  loss being irreversibility in the turbine, the heat exchangers and")
    print("  the reservoir itself. The Carnot figure is a ceiling, never a")
    print("  prediction.")


def part5_entropy_of_earth():
    section("5. Entropy of fusion and the Earth's entropy budget")
    L, T_m = 4.0e5, 1500.0
    print(f"  Entropy of fusion of basalt: L/T_m = {L:.3e}/{T_m:.0f} = "
          f"{L / T_m:.2f} J kg^-1 K^-1")
    secular = 3.1e13          # W, nominal deficit of heat loss over radiogenic
    dTdt = secular / (MANTLE_MASS * MANTLE_CP)
    print(f"  Secular-cooling entropy production, Q(1/T_c - 1/T_s), with")
    print(f"  Q = {secular:.2e} W, is of order "
          f"{secular * (1 / 283.0 - 1 / 1600.0):.4e} W/K.")
    print(f"  Implied mantle cooling rate dT/dt = Q/(M c_p) = {dTdt:.4e} K/s "
          f"= {dTdt * 3.15576e7 * 1e9:.1f} K per 10^9 yr")
    print()
    print("  Solar radiation degradation (adopted S = 1361 W/m2, albedo 0.30):")
    S, albedo = 1361.0, 0.30
    absorbed = S * (1 - albedo) / 4.0
    T_e = (absorbed / SIGMA) ** 0.25
    sigma_rad = absorbed * (1.0 / T_e - 1.0 / 5772.0)
    print(f"    absorbed flux S(1-a)/4 = {absorbed:.4f} W/m2")
    print(f"    effective radiating temperature = {T_e:.4f} K "
          f"= {T_e - 273.15:.2f} C")
    print(f"    entropy produced per unit area = {sigma_rad:.6f} W m^-2 K^-1")
    print(f"    globally = {sigma_rad * EARTH_AREA:.4e} W/K")
    print()
    print("  The climate system produces roughly four orders of magnitude more")
    print("  entropy than the entire solid Earth's conduction. The Earth's heat")
    print("  engine is enormous in energy and small in entropy production; the")
    print("  radiation budget is the reverse. Both statements are second-law")
    print("  statements, and both are quantitative.")


if __name__ == "__main__":
    part1_entropy_change()
    part2_conduction_entropy()
    part3_geotherm_integral()
    part4_carnot()
    part5_entropy_of_earth()
