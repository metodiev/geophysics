#!/usr/bin/env python3
"""Radiogenic heat production and mantle geotherms.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python radiogenic_heat_demo.py

Everything here is a SYNTHETIC teaching model.  The decay data, the rock
compositions and the transport parameters below are *adopted inputs* chosen to be
representative; none of them is presented as a measurement, and no real sample,
borehole or region is used.

Contents
--------
1. Heat production of four heat-producing isotopes from activity times energy.
2. Volumetric heat production of two synthetic rock compositions.
3. Steady conductive geotherms in three provinces, with the heat-flow partition.
4. The mantle adiabat: exact exponential solution versus the constant-gradient
   approximation, and the temperature at the core-mantle boundary.
5. Conductive versus convective heat transport: why a conductive mantle is
   impossible, and where a conductive geotherm crosses the solidus.
6. Inverting a synthetic discontinuity depth for a temperature anomaly
   (Clapeyron-slope thermometer).
7. Verification: the printed geotherm against an independent ODE integration.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

NA = 6.02214076e23        # Avogadro constant, 1/mol (exact)
MEV_TO_J = 1.602176634e-13  # J per MeV (exact, from the elementary charge)

# --- SYNTHETIC teaching inputs: adopt a four-isotope heat-producing inventory --
# half_life_gyr : adopted half-life of the parent isotope
# q_total_mev   : adopted total energy released per decay chain [MeV]
# f_neutrino    : adopted fraction of that energy carried away by neutrinos
# molar_mass    : g/mol of the parent isotope
# iso_fraction  : adopted isotopic fraction of the natural element
ISOTOPES = {
    "U-238": dict(half_life_gyr=4.468, q_total_mev=51.7, f_neutrino=0.053,
                  molar_mass=238.0289, iso_fraction=0.9927, element="U"),
    "U-235": dict(half_life_gyr=0.7038, q_total_mev=46.4, f_neutrino=0.041,
                  molar_mass=235.0439, iso_fraction=0.0072, element="U"),
    "Th-232": dict(half_life_gyr=14.05, q_total_mev=42.6, f_neutrino=0.065,
                   molar_mass=232.0381, iso_fraction=1.0000, element="Th"),
    "K-40": dict(half_life_gyr=1.248, q_total_mev=1.31, f_neutrino=0.30,
                 molar_mass=39.9639, iso_fraction=1.17e-4, element="K"),
}
SEC_PER_GYR = 3.1557e16   # s, from 365.25 d/yr

# Synthetic rock compositions: element concentration by mass
ROCKS = {
    "average continental crust": dict(rho=2700.0, U=2.0e-6, Th=8.0e-6, K=2.0e-2),
    "depleted mantle": dict(rho=3300.0, U=8.0e-9, Th=2.4e-8, K=5.0e-5),
}

# Synthetic transport parameters
K_COND = 2.5              # W m^-1 K^-1, crustal thermal conductivity
K_MANTLE = 4.5            # W m^-1 K^-1, mantle thermal conductivity
ALPHA_TH = 3.0e-5         # 1/K, thermal expansivity
CP = 1250.0               # J kg^-1 K^-1, specific heat capacity
G_SURF = 9.81             # m s^-2
D_MANTLE = 2891.0e3       # m, core-mantle-boundary depth
ETA = 1.0e21              # Pa s, mantle viscosity
KAPPA = 1.0e-6            # m^2 s^-1, thermal diffusivity
RA_C = 1100.0             # critical Rayleigh number, free-slip
SOLIDUS_SLOPE = 3.0       # K/km, adopted solidus slope near 100 km depth


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def isotope_heat_mw_per_kg(spec):
    """Specific heat production of a parent isotope, in microwatt per kg.

    Activity per kg of the isotope is  lambda * N_A / M  with lambda = ln2/T.
    Multiplying by the *deposited* energy per decay gives W per kg of isotope.
    """
    lam = np.log(2.0) / (spec["half_life_gyr"] * SEC_PER_GYR)      # 1/s
    atoms_per_kg = NA / (spec["molar_mass"] * 1.0e-3)              # 1/kg
    q_heat_mev = spec["q_total_mev"] * (1.0 - spec["f_neutrino"])  # MeV
    w_per_kg = lam * atoms_per_kg * q_heat_mev * MEV_TO_J          # W/kg
    return w_per_kg * 1.0e6


def rock_heat_production(rock_mw_per_kg=False):
    """Volumetric heat production A of each synthetic rock, in microwatt per m^3."""
    out = {}
    for name, rock in ROCKS.items():
        total = 0.0
        for iso, spec in ISOTOPES.items():
            iso_mass_fraction = rock[spec["element"]] * spec["iso_fraction"]
            total += iso_mass_fraction * isotope_heat_mw_per_kg(spec)
        out[name] = rock["rho"] * total       # uW/kg * kg/m^3 = uW/m^3
    return out


def geotherm(z_km, q0_mw, a0_uw, h_km, k, t0_c):
    """Steady conductive geotherm with A(z) = A0 exp(-z/h), all SI-consistent.

    T(z) = T0 + (q0 - A0 h) z / k + (A0 h^2 / k)(1 - exp(-z/h)),
    with q0 in W/m^2, A0 in W/m^3, z and h in m.
    """
    z = np.asarray(z_km) * 1.0e3
    h = h_km * 1.0e3
    a0 = a0_uw * 1.0e-6
    q0 = q0_mw * 1.0e-3
    return t0_c + (q0 - a0 * h) * z / k + (a0 * h**2 / k) * (1.0 - np.exp(-z / h))


def main():
    section("1. Heat production of the four adopted isotopes")
    print("adopted inventory (synthetic teaching inputs, not measurements):")
    print("  isotope   T1/2 (Gyr)  Q_total (MeV)  nu loss   H (uW/kg of isotope)")
    for iso, spec in ISOTOPES.items():
        print(f"  {iso:8s} {spec['half_life_gyr']:10.3f} {spec['q_total_mev']:15.2f}"
              f" {spec['f_neutrino']:9.2f} {isotope_heat_mw_per_kg(spec):23.2f}")
    h_u238 = isotope_heat_mw_per_kg(ISOTOPES["U-238"])
    h_k40 = isotope_heat_mw_per_kg(ISOTOPES["K-40"])
    print(f"\ncheck: U-238 deposits {ISOTOPES['U-238']['q_total_mev'] * (1 - ISOTOPES['U-238']['f_neutrino']):.1f} MeV"
          f" per decay, of which {100 * ISOTOPES['U-238']['f_neutrino']:.1f}% escapes as neutrinos")
    print(f"check: K-40 deposits only {ISOTOPES['K-40']['q_total_mev'] * (1 - ISOTOPES['K-40']['f_neutrino']):.2f} MeV"
          f" per decay; its specific production is {h_u238 / h_k40:.0f} times smaller than U-238's")

    section("2. Volumetric heat production of two synthetic rocks")
    a_rock = rock_heat_production()
    for name, rock in ROCKS.items():
        print(f"{name}: rho = {rock['rho']:.0f} kg/m^3, U = {rock['U'] * 1e6:.3g} ppm,"
              f" Th = {rock['Th'] * 1e6:.3g} ppm, K = {rock['K'] * 100:.3g} wt%")
        print(f"    A = {a_rock[name]:.3f} uW/m^3")
    print("\ncontribution of each isotope to the continental-crust value (uW/m^3):")
    for iso, spec in ISOTOPES.items():
        frac = ROCKS["average continental crust"][spec["element"]] * spec["iso_fraction"]
        print(f"  {iso:8s} {ROCKS['average continental crust']['rho'] * frac * isotope_heat_mw_per_kg(spec):.4f}")

    section("3. Steady conductive geotherms and the heat-flow partition")
    provinces = [
        ("cold craton", 45.0, 0.6, 10.0),
        ("average crust", 65.0, 1.0, 10.0),
        ("extended crust", 90.0, 1.8, 8.0),
    ]
    print("  province         q0 (mW/m^2)  A0 (uW/m^3)  h (km)  A0*h (mW/m^2)"
          "  q_mantle  T(40 km) (C)")
    z = np.linspace(0.0, 40.0, 401)
    for name, q0, a0, h in provinces:
        q_mantle = q0 - a0 * h
        t40 = float(np.interp(40.0, z, geotherm(z, q0, a0, h, K_COND, 10.0)))
        print(f"  {name:15s} {q0:12.1f} {a0:12.2f} {h:7.1f} {a0 * h:11.2f}"
              f" {q_mantle:9.2f} {t40:11.1f}")
    print(f"\ncrustal column integral: A0*h = 1.0 uW/m^3 * 10 km = {1.0 * 10.0:.1f} mW/m^2")
    for name, q0, a0, h in provinces:
        print(f"radiogenic fraction A0*h/q0, {name:15s} = {a0 * h / q0:.3f}")
    print("the fraction is a ratio of two separately measured quantities and is not"
          " monotonic in q0, because A0 varies between provinces")
    print("hold A0*h fixed at 10 mW/m^2 and vary only q0:")
    for q0 in (45.0, 65.0, 90.0):
        print(f"  q0 = {q0:.0f} mW/m^2 -> A0*h/q0 = {10.0 / q0:.3f}")
    print("then the fraction falls as q0 rises: old cold provinces keep a larger"
          " share of their surface flux")
    q_mantle_dmm = a_rock["depleted mantle"] * (D_MANTLE / 1.0e3)
    print(f"\nmantle column, depleted composition: A*average = "
          f"{a_rock['depleted mantle']:.3f} uW/m^3 * {D_MANTLE / 1.0e3:.0f} km = "
          f"{q_mantle_dmm:.1f} mW/m^2")
    print(f"that is {q_mantle_dmm / 65.0:.3f} of the adopted continental surface flux")

    section("4. The mantle adiabat")
    dtdz = ALPHA_TH * G_SURF * 1600.0 / CP * 1.0e3
    print(f"adiabatic gradient at T = 1600 K: alpha*g*T/cp = {dtdz:.3f} K/km")
    z_ad = np.linspace(0.0, D_MANTLE / 1.0e3, 1000)
    t_exact = 1600.0 * np.exp(ALPHA_TH * G_SURF * z_ad * 1.0e3 / CP)
    t_linear = 1600.0 + dtdz * z_ad
    dt = float(t_exact[-1] - t_linear[-1])
    print(f"exact exponential adiabat at {z_ad[-1]:.0f} km : {t_exact[-1]:.1f} K")
    print(f"constant-gradient approximation at {z_ad[-1]:.0f} km: {t_linear[-1]:.1f} K")
    print(f"difference: {dt:.1f} K = {100 * dt / t_exact[-1]:.1f}%"
          " (the approximation is not conservative)")
    print(f"exponent alpha*g*D/cp actually reached = "
          f"{ALPHA_TH * G_SURF * D_MANTLE / CP:.3f} (not small)")

    section("5. Conductive versus convective transport in the mantle")
    dtemp = 2500.0
    ra = (ALPHA_TH * 3300.0 * G_SURF * dtemp * D_MANTLE**3) / (KAPPA * ETA)
    nu = (ra / RA_C) ** (1.0 / 3.0)
    q_cond = K_MANTLE * dtemp / D_MANTLE * 1.0e3
    q_conv = q_cond * nu
    print(f"Rayleigh number Ra = rho*alpha*g*dT*d^3/(kappa*eta) = {ra:.3e}")
    print(f"Nusselt number Nu = (Ra/Ra_c)^(1/3) = {nu:.1f}")
    print(f"purely conductive flux  k*dT/d = {q_cond:.3f} mW/m^2")
    print(f"convective flux        Nu*k*dT/d = {q_conv:.1f} mW/m^2")
    print(f"adopted nominal targets: continental 65 mW/m^2, oceanic 100 mW/m^2")
    q_target = 80.0
    eta_needed = (ALPHA_TH * 3300.0 * G_SURF * dtemp * D_MANTLE**3) / \
        (KAPPA * RA_C * (q_target / q_cond) ** 3)
    print(f"viscosity that would give {q_target:.0f} mW/m^2: {eta_needed:.2e} Pa s"
          f" (adopted eta = {ETA:.1e} Pa s)")
    z_iso = K_MANTLE * (1600.0 - 10.0) / (0.080 * 1.0e3)
    t_sol = 1400.0 + SOLIDUS_SLOPE * np.linspace(0.0, 400.0, 4001)
    z_grid = np.linspace(0.0, 400.0, 4001)
    t_cond = 10.0 + 0.080 * 1.0e3 * z_grid / K_MANTLE
    cross = z_grid[np.argmin(np.abs(t_cond - t_sol))]
    print(f"\na purely conductive mantle carrying 80 mW/m^2 has dT/dz ="
          f" q/k = {0.080 * 1.0e3 / K_MANTLE:.2f} K/km")
    print(f"that geotherm reaches the adopted solidus 1400 + {SOLIDUS_SLOPE:.0f}*z"
          f" (K, z in km) at z = {cross:.1f} km")
    print(f"it reaches the 1600 K isotherm at z = k*dT/q = {z_iso:.1f} km")
    print("either criterion puts the mantle below ~100 km above the solidus:"
          " conduction cannot remove the heat, so it must convect")

    section("6. Clapeyron-slope thermometer (synthetic)")
    rho_tz = 3800.0        # kg/m^3, adopted
    dtemp_anom = -100.0    # K, an adopted cold anomaly
    print(f"adopted: rho = {rho_tz:.0f} kg/m^3, g = {G_SURF:.2f} m/s^2;"
          f" a temperature anomaly of {dtemp_anom:+.0f} K")
    print("  transition   dP/dT (MPa/K)   dz = (dP/dT)*dT/(rho*g) (km)"
          "   direction")
    for label, m_mpa in (("410-type", 2.5), ("660-type", -2.0)):
        dz_km = m_mpa * 1.0e6 * dtemp_anom / (rho_tz * G_SURF) / 1.0e3
        arrow = "shallower" if dz_km < 0.0 else "deeper"
        print(f"  {label:11s} {m_mpa:13.2f} {dz_km:32.1f}   {arrow}")
    print("so a cold anomaly lifts the 410-type transition and deepens the"
          " 660-type one,")
    print(f"thickening the transition zone by {abs(2.5e6 * dtemp_anom / (rho_tz * G_SURF)) / 1.0e3 + abs(-2.0e6 * dtemp_anom / (rho_tz * G_SURF)) / 1.0e3:.1f} km"
          " for this anomaly:")
    print("that thickness is the temperature proxy, and it is a *difference* of"
          " two model depths, not a measured temperature")

    section("7. Verification of the analytic geotherm")
    zz = np.linspace(1.0, 39.0, 200)
    h = 10.0e3
    a0 = 1.0e-6
    q0 = 0.065
    t_analytic = geotherm(zz, 65.0, 1.0, 10.0, K_COND, 10.0)
    t_num = []
    for zi in zz:
        zs = np.linspace(0.0, zi * 1.0e3, 20001)
        integrand = 1.0 - a0 * h * (1.0 - np.exp(-zs / h)) / q0
        t_num.append(10.0 + np.trapezoid(integrand, zs) * q0 / K_COND)
    residual = float(np.max(np.abs(np.array(t_num) - t_analytic)))
    print(f"max |analytic - quadrature| temperature difference over 1-39 km:"
          f" {residual:.3e} K")
    print("the closed form and the direct integration of dT/dz = q(z)/k agree,"
          " so the partition q_mantle = q0 - A0*h is not an independent"
          " assumption but the same statement")
    print("\nSYNTHETIC teaching model; no measured value is used anywhere above.")


if __name__ == "__main__":
    main()
