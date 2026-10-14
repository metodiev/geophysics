#!/usr/bin/env python3
"""Composition and vertical structure of the atmosphere: mean molar mass,
gas constant, density, scale height, hydrostatic pressure profile and total
atmospheric mass.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python atmospheric_composition_demo.py

Everything here is a SYNTHETIC teaching model or a named standard constant.
The dry-air mole fractions, the sea-level state and the tropospheric lapse rate
are *chosen inputs* of the model, printed below, not measurements made by this
module.  The gas constant R* and the molar masses are standard constants; R_d
and cp are DERIVED from them rather than quoted.

Contents
--------
1. Dry-air composition -> mean molar mass, specific gas constant, density.
2. Thermal speeds and scale height.
3. Hydrostatic pressure profile: RK4 integration versus analytic solutions.
4. Total atmospheric mass and column mass per unit area.
5. Moist versus dry air: virtual temperature and the density effect.
6. Latent heat stored as column water vapour, expressed as an air temperature.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
R_UNIVERSAL = 8.314462618      # J mol^-1 K^-1, molar gas constant (exact SI value)
G_STANDARD = 9.80665           # m s^-2, standard gravity (definition of the standard atmosphere)
P_SEA = 101325.0               # Pa, standard sea-level pressure (definition)
T_SEA = 288.15                 # K, standard sea-level temperature (definition)
LAPSE = 6.5e-3                 # K m^-1, the conventional tropospheric lapse rate
R_EARTH = 6.371e6              # m, conventional mean Earth radius
T_TROPOPAUSE = 11.0e3          # m, top of the modelled troposphere (model choice)
T_STRAT_TOP = 20.0e3           # m, top of the modelled isothermal layer (model choice)

# --- SYNTHETIC dry-air composition (mole fractions, chosen teaching values) --
DRY_AIR = [
    # species, molar mass (g mol^-1), mole fraction (dimensionless)
    ("N2", 28.0134, 0.780840),
    ("O2", 31.9988, 0.209476),
    ("Ar", 39.9480, 0.009340),
    ("CO2", 44.0095, 0.000420),
    ("Ne", 20.1797, 0.00001818),
    ("He", 4.002602, 0.00000524),
    ("CH4", 16.0425, 0.00000190),
    ("Kr", 83.7980, 0.00000114),
    ("H2", 2.01588, 0.00000055),
    ("N2O", 44.0128, 0.00000033),
]

LATENT_HEAT_VAP = 2.501e6      # J kg^-1, latent heat of vaporisation at 0 degC (standard constant)
COLUMN_WATER = 25.0            # kg m^-2, ILLUSTRATIVE column water vapour of the model


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def mean_molar_mass_kg_per_mol(composition):
    """Mole-fraction weighted mean molar mass, in kg/mol."""
    total = sum(x for _, _, x in composition)
    m = sum(x * M for _, M, x in composition) / total
    return m * 1e-3


def temperature_profile(z):
    """Modelled temperature (K) at geometric height z (m): troposphere + isotherm."""
    if z <= T_TROPOPAUSE:
        return T_SEA - LAPSE * z
    return T_SEA - LAPSE * T_TROPOPAUSE


def main():
    section("1. Dry-air composition -> mean molar mass and gas constant")
    print("  species   M (g/mol)   mole fraction")
    for name, M, x in DRY_AIR:
        print(f"  {name:6s} {M:10.4f} {x:16.8f}")
    frac_sum = sum(x for _, _, x in DRY_AIR)
    print(f"  sum of mole fractions = {frac_sum:.8f}  (must be 1: a check on the table)")

    M_dry = mean_molar_mass_kg_per_mol(DRY_AIR)
    R_d = R_UNIVERSAL / M_dry
    print(f"\n  mean molar mass of dry air  M_d = {M_dry * 1e3:.4f} g/mol")
    print(f"  specific gas constant       R_d = R*/M_d = {R_d:.3f} J kg^-1 K^-1")
    kappa = 1.4  # ratio of specific heats for a diatomic gas (derived below, not fitted)
    cp = kappa * R_d / (kappa - 1.0)
    cv = cp / kappa
    print(f"  with gamma = cp/cv = {kappa:.1f} for a diatomic gas:")
    print(f"    cp = gamma R_d/(gamma-1) = {cp:.2f} J kg^-1 K^-1")
    print(f"    cv = R_d/(gamma-1)      = {cv:.2f} J kg^-1 K^-1")
    print(f"    cp - cv = {cp - cv:.3f} J kg^-1 K^-1  (= R_d: the Mayer relation)")

    rho_sea = P_SEA / (R_d * T_SEA)
    print(f"\n  sea-level density rho = p/(R_d T) = {rho_sea:.4f} kg m^-3")

    section("2. Thermal speed and scale height")
    kB = 1.380649e-23           # J K^-1, Boltzmann constant (exact SI value)
    m_N2 = 28.0134e-3 / 6.02214076e23
    v_rms = np.sqrt(3.0 * kB * T_SEA / m_N2)
    print(f"  most probable molecule is N2, mass = {m_N2:.4e} kg")
    print(f"  rms thermal speed sqrt(3 kT/m) = {v_rms:.1f} m s^-1")
    print("  (compare with the ~10 m/s winds of lesson 05: molecules are ~50x faster,")
    print("   which is why a parcel equilibrates locally long before it moves far)")

    H_scale = R_d * T_SEA / G_STANDARD
    print(f"\n  scale height H = R_d T/g = {H_scale / 1e3:.4f} km")
    print("  physical meaning: the e-folding height of pressure for an isothermal")
    print("  atmosphere at the sea-level temperature.")
    for z_km in (1.0, 5.0, 10.0):
        print(f"    isothermal e^(-z/H): p({z_km:.0f} km)/p0 = "
              f"{np.exp(-z_km * 1e3 / H_scale):.6f}")

    section("3. Hydrostatic pressure profile: numerical integration vs analytics")
    # dp/dz = -rho g = -p g/(R_d T(z))  integrated with RK4
    def dpdz(p, z):
        return -p * G_STANDARD / (R_d * temperature_profile(z))

    def rk4(z0, z1, p0, n):
        z = np.linspace(z0, z1, n + 1)
        h = (z1 - z0) / n
        p = np.empty_like(z)
        p[0] = p0
        for i in range(n):
            k1 = dpdz(p[i], z[i])
            k2 = dpdz(p[i] + 0.5 * h * k1, z[i] + 0.5 * h)
            k3 = dpdz(p[i] + 0.5 * h * k2, z[i] + 0.5 * h)
            k4 = dpdz(p[i] + h * k3, z[i] + h)
            p[i + 1] = p[i] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        return z, p

    z_km = np.arange(0.0, 20.001, 1.0)
    print("   z(km)    T(K)    RK4 p(hPa)   analytic p(hPa)   diff(Pa)")
    for z in z_km:
        if z <= 20.0:
            zz = z * 1e3
            zz_cap = min(zz, T_STRAT_TOP)
            _, p_num = rk4(0.0, zz_cap, P_SEA, 4000)
            p_rk = p_num[-1]
            if zz <= T_TROPOPAUSE:
                # polytropic (lapse-rate) solution
                p_an = P_SEA * (temperature_profile(zz) / T_SEA) ** (
                    G_STANDARD / (R_d * LAPSE))
            else:
                p_11 = P_SEA * (temperature_profile(T_TROPOPAUSE) / T_SEA) ** (
                    G_STANDARD / (R_d * LAPSE))
                T_iso = temperature_profile(T_TROPOPAUSE)
                p_an = p_11 * np.exp(-(zz - T_TROPOPAUSE) * G_STANDARD / (R_d * T_iso))
            if z in (0.0, 1.0, 5.0, 10.0, 11.0, 15.0, 20.0):
                print(f"  {z:6.0f}  {temperature_profile(zz):6.2f}  {p_rk / 100:12.4f}"
                      f"  {p_an / 100:15.4f}  {p_rk - p_an:9.3f}")

    p_11 = P_SEA * (temperature_profile(T_TROPOPAUSE) / T_SEA) ** (
        G_STANDARD / (R_d * LAPSE))
    print(f"\n  pressure at 11 km (tropopause) = {p_11 / 100:.2f} hPa "
          f"= {100 * p_11 / P_SEA:.2f}% of sea-level pressure")
    _, p_half = rk4(0.0, T_TROPOPAUSE, P_SEA, 20000)
    print(f"  fraction of atmospheric mass below the tropopause "
          f"= {1 - p_half[-1] / P_SEA:.4f}")

    section("4. Total atmospheric mass")
    area = 4.0 * np.pi * R_EARTH ** 2
    column_mass = P_SEA / G_STANDARD
    M_atm = column_mass * area
    print(f"  Earth surface area  A = 4 pi R^2   = {area:.4e} m^2")
    print(f"  column mass       m/A = p0/g       = {column_mass:.2f} kg m^-2")
    print(f"  total mass            M = (p0/g) A = {M_atm:.4e} kg")
    print("  for scale: this is about 1.0e-6 of the mass of the Earth (5.97e24 kg)")

    section("5. Moist versus dry air: virtual temperature")
    q = 0.010                     # kg/kg, illustrative surface specific humidity
    T_v = T_SEA * (1.0 + 0.608 * q)
    rho_moist = P_SEA / (R_d * T_v)
    print(f"  specific humidity q = {q:.3f} kg kg^-1 (illustrative)")
    print(f"  virtual temperature T_v = T(1 + 0.608 q) = {T_v:.2f} K "
          f"(+{T_v - T_SEA:.2f} K)")
    print(f"  density: dry {rho_sea:.4f} -> moist {rho_moist:.4f} kg m^-3 "
          f"({(rho_moist - rho_sea) / rho_sea * 100:+.3f}%)")
    print("  moist air is LIGHTER at the same pressure and temperature because a")
    print("  water molecule (18 g/mol) replaces one of N2/O2 (~29 g/mol).")

    section("6. Latent heat stored as column water vapour")
    L_col = COLUMN_WATER * LATENT_HEAT_VAP
    dT_if_released = L_col / (cp * column_mass)
    print(f"  column water vapour (illustrative) = {COLUMN_WATER:.1f} kg m^-2")
    print(f"  latent heat                       = {L_col:.3e} J m^-2")
    print(f"  if released into the whole air column, dT = L/(cp m/A) "
          f"= {dT_if_released:.2f} K")
    print("  This is why water vapour is the dominant greenhouse gas mass-wise and")
    print("  why latent heating drives deep convection; it is quantified further in")
    print("  lesson 04.")


if __name__ == "__main__":
    main()
