#!/usr/bin/env python3
"""Components of the climate system and their timescales: heat capacities per
unit area, radiative relaxation times, a two-layer ocean model with its two
timescales, ice-sheet timescales, and a timescale summary.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_system_components_demo.py

Everything is SYNTHETIC. Depths, layer thicknesses and temperatures are chosen
teaching values, printed by this script. They are not measurements of any
particular ocean, ice sheet or atmosphere. Physical constants (the specific heat
of water and of air, the latent heat of fusion, surface pressure, gravity) are
standard constants, and the Stefan-Boltzmann constant is exact in SI.

Contents
--------
1. Heat capacity per unit area of each component, and their ratios.
2. Radiative relaxation time from the Planck response.
3. A two-layer ocean model: its two eigenvalues, the response to a step forcing,
   and a check that the long-time limit equals F/lambda.
4. Ice-sheet timescales: the mass-balance timescale and the thermal diffusion
   timescale, which differ by two orders of magnitude.
5. A timescale table for the whole system.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

SIGMA = 5.670374419e-8       # W/(m^2 K^4), exact in SI
G = 9.81
P_SURF = 1.013e5             # Pa, standard atmosphere
C_P_AIR = 1004.0             # J/(kg K)
C_P_WATER = 3985.0           # J/(kg K)
RHO_WATER = 1025.0           # kg/m^3
RHO_ICE, C_ICE = 917.0, 2100.0
K_ICE = 2.2                  # W/(m K)
L_FUSION = 3.34e5            # J/kg
T_REF = 288.0                # K, a chosen reference surface temperature
YEAR = 365.0 * 86400.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# ---------------------------------------------------------------------------
# 1. Heat capacities
# ---------------------------------------------------------------------------

def ocean_capacity(depth_m):
    return RHO_WATER * C_P_WATER * depth_m


def ice_capacity(thickness_m):
    return RHO_ICE * C_ICE * thickness_m


def part1_capacities():
    section("1. Heat capacity per unit area of each component")
    c_atm = C_P_AIR * P_SURF / G
    print("Atmosphere: C = c_p p_s/g = "
          f"{C_P_AIR:.0f} x {P_SURF:.3e}/{G:.2f} = {c_atm:.4e} J/(m^2 K)")
    print(f"  (equivalent to a water layer of {c_atm / (RHO_WATER * C_P_WATER):.2f} m)")
    print(f"\n{'component':>28} {'depth/thickness':>17} {'C (J/m^2/K)':>15} "
          f"{'C/C_atm':>10}")
    rows = [("atmosphere (whole column)", "1 atm", c_atm)]
    for d in (50.0, 100.0, 200.0):
        rows.append(("ocean mixed layer", f"{d:.0f} m", ocean_capacity(d)))
    for d in (1000.0, 3800.0):
        rows.append(("ocean (to depth)", f"{d:.0f} m", ocean_capacity(d)))
    for h in (1000.0, 3000.0):
        rows.append(("ice sheet", f"{h:.0f} m", ice_capacity(h)))
    rows.append(("land, 10 m skin", "10 m",
                 10.0 * 2.0e6))
    for name, thick, c in rows:
        print(f"{name:>28} {thick:>17} {c:15.4e} {c / c_atm:10.2f}")
    print("\n  a 50 m mixed layer already outranks the whole atmosphere by a")
    print("  factor of twenty, and the full ocean by three orders of magnitude.")
    print("  Every statement about 'the climate response time' is therefore a")
    print("  statement about WHICH reservoir is being considered, and the same")
    print("  forcing produces responses differing by four orders of magnitude in")
    print("  time depending on the answer.")


# ---------------------------------------------------------------------------
# 2. Radiative relaxation time
# ---------------------------------------------------------------------------

def part2_relaxation():
    section("2. Radiative relaxation time from the Planck response")
    lam0 = 4.0 * SIGMA * T_REF ** 3
    c_atm = C_P_AIR * P_SURF / G
    print("A blackbody of temperature T radiates sigma T^4, so a temperature")
    print("perturbation changes the outgoing flux by d(sigma T^4)/dT = 4 sigma T^3:")
    print(f"  lambda_0 = 4 sigma T^3 = 4 x {SIGMA:.4e} x {T_REF:.0f}^3 "
          f"= {lam0:.3f} W/(m^2 K)")
    print(f"\n{'component':>28} {'C (J/m^2/K)':>15} {'tau = C/lambda_0':>17} "
          f"{'in':>12}")
    for name, c in (("atmosphere", c_atm),
                    ("ocean, 50 m", ocean_capacity(50.0)),
                    ("ocean, 100 m", ocean_capacity(100.0)),
                    ("ocean, 3800 m", ocean_capacity(3800.0)),
                    ("ice sheet, 3000 m", ice_capacity(3000.0))):
        tau = c / lam0
        unit = f"{tau / YEAR:.2f} yr" if tau > 0.5 * YEAR else \
            f"{tau / 86400.0:.1f} d"
        print(f"{name:>28} {c:15.4e} {tau:17.4e} {unit:>12}")
    print("\n  this is a LOWER BOUND on the response time for each reservoir:")
    print("  it is the time for that reservoir alone to radiate away a")
    print("  temperature anomaly at the Planck rate, with no transport and no")
    print("  feedbacks. Real feedbacks change the effective lambda, and a")
    print("  positive feedback lengthens every entry in the table.")


# ---------------------------------------------------------------------------
# 3. Two-layer ocean model
# ---------------------------------------------------------------------------

def two_layer(c_mixed, c_deep, lam, gamma):
    """Return (M, f) for  dX/dt = M X + f  with X = (T_m, T_d)."""
    m = np.array([[-(lam + gamma) / c_mixed, gamma / c_mixed],
                  [gamma / c_deep, -gamma / c_deep]])
    f = np.array([1.0 / c_mixed, 0.0])
    return m, f


def part3_two_layer():
    section("3. A two-layer ocean: two timescales from one forcing")
    from scipy.linalg import expm
    c_mixed = ocean_capacity(50.0)
    c_deep = ocean_capacity(3350.0)
    lam, gamma = 4.0 * SIGMA * T_REF ** 3, 0.7
    forcing = 3.7
    m, f = two_layer(c_mixed, c_deep, lam, gamma)
    print("SYNTHETIC two-box model with a step forcing F = "
          f"{forcing:.1f} W/m^2:")
    print("  C_m dT_m/dt = F - lambda T_m - gamma (T_m - T_d)")
    print("  C_d dT_d/dt =              + gamma (T_m - T_d)")
    print(f"  C_m = {c_mixed:.4e}, C_d = {c_deep:.4e} J/(m^2 K), "
          f"lambda = {lam:.3f} W/(m^2 K), gamma = {gamma:.2f} W/(m^2 K)")
    f_vec = forcing * f
    ev, vec = np.linalg.eig(m)
    tau = np.sort(-1.0 / ev.real)
    x_eq = -np.linalg.solve(m, f_vec)
    print(f"\n  timescales from the eigenvalues: {tau[0] / YEAR:.3f} yr "
          f"(mixed layer) and {tau[1] / YEAR:.1f} yr (deep ocean)")
    print(f"  exact equilibrium from -M^-1 f: T_m = {x_eq[0]:.4f} K, "
          f"T_d = {x_eq[1]:.4f} K")
    print(f"  analytic F/lambda = {forcing / lam:.4f} K: the two boxes must come")
    print("  to the SAME temperature at equilibrium, and they do, which is a")
    print("  check on the algebra rather than on the ocean.")
    print(f"\n{'time (yr)':>10} {'T_mixed (K)':>13} {'T_deep (K)':>12} "
          f"{'T_m/T_eq':>10} {'T_d/T_eq':>10}")
    for target in (1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0,
                   1000.0, 2000.0, 5000.0):
        t = target * YEAR
        x = x_eq + expm(m * t) @ (np.zeros(2) - x_eq)
        print(f"{target:10.0f} {x[0]:13.4f} {x[1]:12.4f} "
              f"{x[0] / x_eq[0]:10.4f} {x[1] / x_eq[1]:10.4f}")
    print("\n  read the last two columns together: at 100 years the surface has")
    print("  done most of its work while the deep ocean has barely started, and")
    print("  the remaining surface warming is the part that is already committed")
    print("  but not yet realised. The ratio of the two columns at any time is a")
    print("  quantitative 'commitment', and it is a property of gamma, not of the")
    print("  forcing: increasing gamma moves heat down faster, which lowers the")
    print("  surface temperature at every time while leaving the equilibrium")
    print("  untouched.")
    print("  The exact exponential solution is used rather than a time-stepped")
    print("  one because the fast and slow timescales differ by a factor of 660:")
    print("  a single explicit step size cannot resolve both.")


# ---------------------------------------------------------------------------
# 4. Ice-sheet timescales
# ---------------------------------------------------------------------------

def part4_ice():
    section("4. Ice-sheet timescales: mass balance versus thermal diffusion")
    print("Two different timescales are both called 'the ice-sheet response':")
    print("  (i)  mass balance:  tau_mass = H/b_dot  (thickness over accumulation)")
    print("  (ii) thermal:       tau_therm = H^2/kappa, kappa = k/(rho c)")
    kappa = K_ICE / (RHO_ICE * C_ICE)
    print(f"  ice: k = {K_ICE:.1f} W/(m K), rho = {RHO_ICE:.0f} kg/m^3, "
          f"c = {C_ICE:.0f} J/(kg K) -> kappa = {kappa:.4e} m^2/s")
    print(f"\n{'thickness (m)':>14} {'b_dot (m/yr)':>13} {'tau_mass':>12} "
          f"{'tau_therm':>12}")
    for h in (1000.0, 3000.0):
        for bdot in (0.1, 0.3, 1.0):
            tau_m = h / bdot
            tau_t = h ** 2 / kappa / YEAR
            print(f"{h:14.0f} {bdot:13.1f} {tau_m:9.0f} yr {tau_t:9.1e} yr")
    print("\n  the mass-balance timescale is 10^3-10^4 yr for a large ice sheet;")
    print("  the thermal timescale through 3 km of ice is a quarter of a million")
    print("  years. Both are 'the' ice-sheet timescale depending on the question,")
    print("  and quoting one without saying which is a category error.")
    lat = 3.34e5 * RHO_ICE * 1000.0
    heat_1km = ocean_capacity(1000.0)
    print(f"  for scale, melting 1000 m of ice per unit area takes "
          f"{lat:.3e} J/m^2,")
    print(f"  which is {lat / heat_1km:.0f} K worth of a 1 km ocean column's heat")
    print("  capacity. Heat budgets, not temperatures, decide melt: the same")
    print("  ocean delivers those joules by cooling, and the cooling required is")
    print("  far larger than any observed temperature change.")
    print(f"  (Latent heat of fusion used: {L_FUSION:.3e} J/kg.)")


# ---------------------------------------------------------------------------
# 5. Summary
# ---------------------------------------------------------------------------

def part5_summary():
    section("5. Timescale table for the climate system")
    print(f"{'component':>32} {'timescale':>18} {'what sets it':>30}")
    rows = [
        ("atmosphere (radiative)", "~3 weeks", "C/(4 sigma T^3)"),
        ("land surface skin", "hours to days", "diurnal energy balance"),
        ("ocean mixed layer", "months to 1 yr", "C_m/lambda"),
        ("upper ocean / thermocline", "1-10 yr", "wind and buoyancy coupling"),
        ("deep ocean", "10^2-10^3 yr", "C_d/gamma"),
        ("sea ice", "months to years", "growth and melt balance"),
        ("ice sheets (mass balance)", "10^3-10^4 yr", "H/b_dot"),
        ("ice sheets (thermal)", "10^5 yr", "H^2/kappa"),
        ("carbon cycle (atmosphere)", "10^1-10^2 yr", "ocean and land uptake"),
        ("carbon cycle (carbonate)", "10^3-10^4 yr", "ocean chemistry"),
        ("carbon cycle (silicate)", "10^5 yr", "weathering"),
    ]
    for name, tau, why in rows:
        print(f"{name:>32} {tau:>18} {why:>30}")
    print("\n  every entry is a model or a scaling, not a measurement, and each")
    print("  is conditional on the mechanism named in the last column. The point")
    print("  of the table is the SPREAD: seven orders of magnitude. A statement")
    print("  of the form 'the climate will respond in X years' is incomplete")
    print("  unless X's mechanism is named.")


def main():
    part1_capacities()
    part2_relaxation()
    part3_two_layer()
    part4_ice()
    part5_summary()
    print("\nAll models and data in this module are SYNTHETIC teaching models.")


if __name__ == "__main__":
    main()
