"""Temperature, heat, internal energy and specific heat in Earth materials.

Run:  python3 temperature_heat_demo.py
Requires: Python standard library only.

Companion to lesson 02-05-01.

Every material property used here is a NOMINAL value: a representative number
for a class of materials, not a measurement of any particular sample. Rock
specific heat varies from about 700 to 1000 J kg^-1 K^-1 and thermal
conductivity from about 1.5 to 3.5 W m^-1 K^-1 depending on mineralogy,
porosity, fluid content and temperature, so every figure printed below should
be read as an order-of-magnitude estimate for the class of material, never as
a measured value.

The only exactly known numbers here are the defining constants: the Boltzmann
constant k_B and the molar gas constant R = N_A k_B.

The script:

1. Tabulates volumetric heat capacity rho*c_p for rock, water, air and iron.
2. Compares the sensible heat stored in a rock volume with the heat needed to
   melt the same volume, and separates sensible from latent heat.
3. Computes the heat content of a 1 km^3 magma body.
4. Computes the difference c_p - c_v for a solid and for water, to justify
   using c_p and c_v interchangeably for rock.
5. Computes the Dulong-Petit high-temperature limit of c_v for bridgmanite and
   compares it with the nominal mantle c_p.
"""

import math

# Exact defining constants (SI, 2019).
K_B = 1.380649e-23          # J/K        Boltzmann constant, exact
N_A = 6.02214076e23         # 1/mol      Avogadro constant, exact
R_GAS = N_A * K_B           # J/mol/K    molar gas constant, exact (derived)

# Nominal material properties. (k: W m^-1 K^-1, rho: kg m^-3,
# c: J kg^-1 K^-1, alpha: 1/K, K_T: Pa)
MATERIALS = {
    "granite":      {"k": 2.5, "rho": 2700.0, "c": 790.0, "alpha": 8.0e-6,
                     "K_T": 40.0e9},
    "basalt":       {"k": 1.8, "rho": 2900.0, "c": 840.0, "alpha": 2.0e-5,
                     "K_T": 45.0e9},
    "mantle rock":  {"k": 4.0, "rho": 3300.0, "c": 1250.0, "alpha": 3.0e-5,
                     "K_T": 130.0e9},
    "water":        {"k": 0.60, "rho": 1000.0, "c": 4186.0, "alpha": 2.0e-4,
                     "K_T": 2.2e9},
    "air":          {"k": 0.026, "rho": 1.225, "c": 1005.0, "alpha": 3.4e-3,
                     "K_T": 1.0e5},
    "iron":         {"k": 80.0, "rho": 7870.0, "c": 450.0, "alpha": 1.2e-5,
                     "K_T": 170.0e9},
}

LATENT_FUSION = {"basalt": 4.0e5, "ice": 3.34e5, "iron": 2.5e5}  # J/kg, nominal

YEAR_CONST = 3.15576e7      # s, Julian year (365.25 days)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def part1_volumetric_heat_capacity():
    section("1. Volumetric heat capacity rho*c_p  (nominal material values)")
    print(f"{'material':<14}{'rho (kg/m3)':>13}{'c_p (J/kg/K)':>14}"
          f"{'rho*c_p (J/m3/K)':>19}")
    for name, m in MATERIALS.items():
        print(f"{name:<14}{m['rho']:>13.1f}{m['c']:>14.1f}"
              f"{m['rho'] * m['c']:>19.4e}")
    granite_cv = MATERIALS["granite"]["rho"] * MATERIALS["granite"]["c"]
    water_cv = MATERIALS["water"]["rho"] * MATERIALS["water"]["c"]
    print()
    print("  A cubic metre of water stores "
          f"{water_cv / granite_cv:.4f} times as much heat per kelvin as a")
    print("  cubic metre of granite, because of its hydrogen-bond network, not")
    print("  because it is denser (it is not). Air stores "
          f"{MATERIALS['air']['rho'] * MATERIALS['air']['c'] / granite_cv:.3e} times")
    print("  as much per kelvin: the atmosphere is thermally thin.")
    print()
    print(f"  1 m^3 of granite warmed by 1 K takes "
          f"{granite_cv:.4e} J = {granite_cv / 3.6e6:.4f} kWh")
    print(f"  1 km^3 of granite (1e9 m^3) warmed by 1 K takes "
          f"{granite_cv * 1e9:.4e} J")
    return granite_cv


def part2_sensible_vs_latent():
    section("2. Sensible heat versus latent heat: melting 1 m^3 of basalt")
    m = MATERIALS["basalt"]
    rho, c = m["rho"], m["c"]
    T0, T_bypass, T_liq = 300.0, 1500.0, 1500.0
    dT = T_liq - T0
    sensible = rho * c * dT                      # J per m^3
    latent = rho * LATENT_FUSION["basalt"]       # J per m^3
    total = sensible + latent
    print(f"  rho = {rho:.0f} kg/m^3, c_p = {c:.0f} J kg^-1 K^-1, "
          f"T from {T0:.0f} to {T_liq:.0f} K, delta T = {dT:.0f} K")
    print(f"  sensible heat  rho c_p delta T = {sensible:.4e} J per m^3")
    print(f"  latent heat    rho L           = {latent:.4e} J per m^3 "
          f"(L = {LATENT_FUSION['basalt']:.3e} J/kg, nominal)")
    print(f"  total                          = {total:.4e} J per m^3")
    print(f"  latent fraction of the total   = {latent / total:.4f}")
    print()
    print("  Consequence: a crystallising magma body stalls near the solidus")
    print("  because ~28 per cent of its heat is released at a fixed")
    print("  temperature. This is the single most important latent-heat fact")
    print("  in igneous geophysics and it is why cooling curves are not")
    print("  linear in time.")
    return sensible, latent, total


def part3_magma_body_heat():
    section("3. Heat content of a 1 km^3 magma body")
    sensible, latent, total = part2_values()
    volume = 1.0e9                                # m^3
    energy = total * volume
    print(f"  volume = {volume:.3e} m^3 (a 1 km x 1 km x 1 km body)")
    print(f"  energy released cooling 1500 K -> 300 K = {energy:.4e} J")
    print(f"  of which latent heat                    = "
          f"{latent * volume:.4e} J")
    print()
    print(f"  Compare with 1 kW of continuous heat for one year (a kW-year)")
    kwh_year = 1000.0 * YEAR_CONST
    print(f"  1 kW-year = 1000 W x {YEAR_CONST:.5e} s = {kwh_year:.4e} J")
    print(f"  so the body's heat equals {energy / kwh_year:.4e} kW-years,")
    print(f"  i.e. {energy / kwh_year / 1e6:.2f} GW-years,")
    print("  an enormous resource and an enormous hazard at the same time.")
    print()
    print("  This is energy, not power. Converting it to a cooling time")
    print("  requires a heat-transfer path, which is lesson 02-05-04.")
    return energy


def part2_values():
    m = MATERIALS["basalt"]
    rho, c = m["rho"], m["c"]
    sensible = rho * c * (1500.0 - 300.0)
    latent = rho * LATENT_FUSION["basalt"]
    return sensible, latent, sensible + latent


def part4_cp_minus_cv():
    section("4. How different are c_p and c_v?")
    print("  For a solid:  c_p - c_v = alpha^2 T K_T / rho")
    print(f"{'material':<14}{'T (K)':>8}{'alpha^2 T K_T/rho':>20}{'c_p':>12}"
          f"{'(c_p-c_v)/c_p':>16}")
    for name in ("granite", "mantle rock", "iron", "water"):
        m = MATERIALS[name]
        T = 300.0 if name != "mantle rock" else 1600.0
        diff = m["alpha"] ** 2 * T * m["K_T"] / m["rho"]
        print(f"{name:<14}{T:>8.0f}{diff:>20.4f}{m['c']:>12.1f}"
              f"{diff / m['c']:>16.3e}")
    print()
    print("  For a crystalline solid at crustal temperatures the difference is")
    print("  well under 1 per cent, which is why rock physics uses c_p and c_v")
    print("  interchangeably. At mantle temperatures the product alpha T is")
    print("  larger and the difference reaches a few per cent - still small for")
    print("  most purposes, but no longer negligible when a temperature rise is")
    print("  computed adiabatically. For a gas the two differ by tens of per")
    print("  cent, which is why the atmosphere must keep the distinction")
    print("  (lesson 16-01).")


def part5_dulong_petit():
    section("5. Why rock specific heat is ~800-1250 J kg^-1 K^-1")
    print("  Dulong-Petit high-temperature limit: c_v = 3 n R per mole, with n")
    print("  the number of atoms per formula unit.")
    minerals = {
        "periclase MgO":      (2, 24.305 + 15.999),
        "bridgmanite MgSiO3": (5, 24.305 + 28.0855 + 3 * 15.999),
        "quartz SiO2":        (3, 28.0855 + 2 * 15.999),
    }
    print(f"  R = N_A k_B = {R_GAS:.10f} J mol^-1 K^-1 (exact)")
    print(f"{'mineral':<22}{'n':>3}{'M (g/mol)':>12}{'3nR (J/mol/K)':>16}"
          f"{'c_v (J/kg/K)':>15}")
    for name, (n, M_g) in minerals.items():
        M = M_g / 1000.0
        c_molar = 3.0 * n * R_GAS
        print(f"{name:<22}{n:>3}{M_g:>12.4f}{c_molar:>16.3f}"
              f"{c_molar / M:>15.1f}")
    print()
    print("  Every silicate lands on ~1240 J kg^-1 K^-1, whatever its formula,")
    print("  because the Dulong-Petit limit is 3R per ATOM and almost all")
    print("  rock-forming oxides have about 20 g of mass per atom. The nominal")
    print("  mantle value of ~1250 J kg^-1 K^-1 is therefore a genuine")
    print("  theoretical result, not a coincidence: at mantle temperature every")
    print("  lattice mode is excited.")
    print()
    print("  Room-temperature measurements are LOWER (granite ~790 J kg^-1 K^-1)")
    print("  because 300 K is not above the Debye temperature of every mode, so")
    print("  the classical limit is not yet reached. Dulong-Petit is a")
    print("  high-temperature limit; at low temperature the Debye spectrum is")
    print("  required, and c falls towards zero as T^3.")


if __name__ == "__main__":
    part1_volumetric_heat_capacity()
    part2_sensible_vs_latent()
    part3_magma_body_heat()
    part4_cp_minus_cv()
    part5_dulong_petit()
