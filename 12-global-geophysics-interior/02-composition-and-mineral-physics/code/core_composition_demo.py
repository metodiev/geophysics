#!/usr/bin/env python3
"""Core composition, light elements and the geodynamo -- a SYNTHETIC model.

Run with:
    cd 12-global-geophysics-interior/02-composition-and-mineral-physics/code
    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python core_composition_demo.py

All numbers in this script are SYNTHETIC teaching values: the density profile of
the Earth, the pure-iron equation of state, the thermal parameters and the heat
flows are ASSUMED inputs chosen to lie in the range usually discussed for the
core.  Nothing here is a measurement and no published model is reproduced.  Only
the gravitational constant and the Earth's mass and radius are standard
constants.

Contents
--------
1. The assumed model: geometry, density profile and thermal parameters.
2. Mass, gravity and pressure from the assumed profile (with a mass check).
3. The pure-iron reference equation of state and the thermal correction.
4. The density deficit and the implied light-element mass fraction.
5. The adiabatic gradient and the adiabatic (conducted) heat flow.
6. Cooling, inner-core growth, and the age of the inner core.
7. The dynamo: magnetic Reynolds number, diffusion time, Elsasser number.
8. Summary of the model.

The script is print-only: it never opens a window and exits with status 0.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- standard constants and named conventions ---------------------------------
G = 6.674e-11                 # gravitational constant [m^3 kg^-1 s^-2]
R_EARTH = 6371.0e3            # mean Earth radius [m]
M_EARTH = 5.9722e24           # Earth mass [kg]
D_CMB = 2891.0e3              # CMB depth, PREM-like convention [m]
R_CORE = R_EARTH - D_CMB      # core radius [m]
R_ICB = 1221.5e3              # ICB (inner-core) radius [m]; ICB depth 5149.5 km

# --- ASSUMED synthetic structure ---------------------------------------------
MANTLE_SHELLS = (                       # (r_inner, r_outer, rho) [m, m, kg/m^3]
    (6336.0e3, R_EARTH, 2900.0),        # crust
    (5971.0e3, 6336.0e3, 3450.0),       # upper mantle
    (R_CORE, 5971.0e3, 4680.0),         # lower mantle
)
RHO_OC_TOP, RHO_OC_BOT = 9900.0, 12150.0    # outer core, CMB -> ICB [kg/m^3]
RHO_IC_TOP, RHO_IC_CTR = 12750.0, 13500.0   # inner core, ICB -> centre [kg/m^3]
OC_EXPONENT = 0.9                           # shape of the outer-core profile

# --- ASSUMED pure-iron reference EOS and thermal parameters -------------------
FE_RHO0, FE_K0, FE_K0P = 8000.0, 160.0e9, 5.0   # zero-pressure reference state
ALPHA = 1.0e-5                # thermal expansivity [1/K]
T_REF = 300.0                 # reference temperature of the EOS [K]
T_CMB = 4000.0                # temperature at the top of the outer core [K]
CP = 800.0                    # specific heat capacity [J kg^-1 K^-1]
SOLID_JUMP = 1.03             # rho_solid / rho_liquid at the melting point
DTM_DS = 0.15e-3              # melting-curve slope, K per m (= 0.15 K/km)

# --- ASSUMED light-element and heat-flow parameters ---------------------------
RHO_LIGHT_CMB, RHO_LIGHT_ICB = 5000.0, 6000.0   # light-element density [kg/m^3]
Q_CMB = 10.0e12               # total heat flow out of the core [W]
L_LATENT = 2.5e5              # latent heat of freezing [J/kg]
K_GRID = (30.0, 60.0, 90.0, 110.0, 120.0, 150.0)   # thermal conductivity [W/m/K]

# --- ASSUMED dynamo parameters ------------------------------------------------
SIGMA = 1.0e6                 # electrical conductivity [S/m]
U_FLOW = 5.0e-4               # typical core flow speed [m/s]
B_CORE = 1.0e-3               # field strength in the core [T]
OMEGA = 7.292e-5              # Earth rotation rate [rad/s]
MU0 = 4.0e-7 * np.pi          # permeability of free space


def section(title):
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def rho_outer_core(r):
    """Assumed outer-core density profile [kg/m^3]."""
    frac = (R_CORE - r) / (R_CORE - R_ICB)
    return RHO_OC_TOP + (RHO_OC_BOT - RHO_OC_TOP) * frac ** OC_EXPONENT


def rho_inner_core(r):
    """Assumed inner-core density profile [kg/m^3]."""
    return RHO_IC_TOP + (RHO_IC_CTR - RHO_IC_TOP) * (1.0 - (r / R_ICB) ** 2)


def bm3_pressure(rho, rho0, k0, k0p):
    """Third-order Birch-Murnaghan pressure [Pa] for a density [kg/m^3]."""
    x = (rho / rho0) ** (1.0 / 3.0)
    return 1.5 * k0 * (x ** 7 - x ** 5) * (1.0 + 0.75 * (k0p - 4.0) * (x ** 2 - 1.0))


def bm3_density(p, rho0, k0, k0p):
    """Invert the Birch-Murnaghan EOS for the density [kg/m^3] at pressure p [Pa]."""
    lo, hi = 0.6 * rho0, 3.0 * rho0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if bm3_pressure(mid, rho0, k0, k0p) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def fe_reference_density(p, t):
    """Assumed pure-liquid-iron density [kg/m^3] at pressure p [Pa], temperature t [K]."""
    rho_300 = bm3_density(p, FE_RHO0, FE_K0, FE_K0P)
    return rho_300 * (1.0 - ALPHA * (t - T_REF))


def light_fraction(rho_mix, rho_fe, rho_light):
    """Mass fraction of light element from ideal volume additivity.

    1/rho_mix = (1 - x)/rho_fe + x/rho_light
    """
    inv_mix, inv_fe, inv_l = 1.0 / rho_mix, 1.0 / rho_fe, 1.0 / rho_light
    return (inv_mix - inv_fe) / (inv_l - inv_fe)


def build_radial_model(n=20001):
    """Assemble the assumed density profile and its mass, gravity and pressure."""
    r = np.linspace(0.0, R_EARTH, n)
    rho = np.empty_like(r)
    for i, x in enumerate(r):
        if x < R_ICB:
            rho[i] = rho_inner_core(x)
        elif x < R_CORE:
            rho[i] = rho_outer_core(x)
        else:
            rho[i] = MANTLE_SHELLS[-1][2]
            for r_in, r_out, rho_shell in MANTLE_SHELLS:
                if r_in <= x < r_out:
                    rho[i] = rho_shell
    # mass interior to each radius (cumulative trapezoid)
    shell = 0.5 * (4.0 * np.pi * r[1:] ** 2 * rho[1:]
                   + 4.0 * np.pi * r[:-1] ** 2 * rho[:-1]) * np.diff(r)
    mass = np.concatenate([[0.0], np.cumsum(shell)])
    g = G * mass / np.maximum(r, 1.0) ** 2
    # hydrostatic pressure, integrated inward from the surface
    p = np.zeros_like(r)
    for i in range(len(r) - 1, 0, -1):
        p[i - 1] = p[i] + 0.5 * (rho[i] * g[i] + rho[i - 1] * g[i - 1]) * (r[i] - r[i - 1])
    return r, rho, mass, g, p


def adiabatic_temperature(r_core, t_cmb, alpha, cp, n=1201):
    """Integrate the adiabatic gradient dT/dr = -alpha g T / Cp inward.

    Uses a prescribed gravity profile across the outer core (passed as a
    callable through the closure below) so that the calculation stays
    independent of the radial-model grid.
    """
    r = np.linspace(R_CORE, R_ICB, n)
    t = np.empty_like(r)
    t[0] = t_cmb
    for i in range(1, n):
        g_here = r_core(r[i])
        g_prev = r_core(r[i - 1])
        dt = -0.5 * alpha / cp * (g_here * t[i - 1] + g_prev * t[i - 1]) * (r[i] - r[i - 1])
        t[i] = t[i - 1] + dt
    return r, t


def main():
    section("1. The assumed model: geometry, density and thermal parameters")
    print("  standard constants: G = 6.674e-11 m^3 kg^-1 s^-2, "
          f"Earth radius {R_EARTH / 1e3:.0f} km, Earth mass {M_EARTH:.4e} kg")
    print(f"  named conventions: CMB depth {D_CMB / 1e3:.0f} km "
          f"(core radius {R_CORE / 1e3:.0f} km), inner-core radius "
          f"{R_ICB / 1e3:.1f} km (ICB depth {(R_EARTH - R_ICB) / 1e3:.1f} km)")
    print("  ASSUMED synthetic mantle shells (radius range -> density):")
    for r_in, r_out, rho_shell in MANTLE_SHELLS:
        print(f"    {r_in / 1e3:7.0f} - {r_out / 1e3:7.0f} km -> "
              f"{rho_shell / 1e3:.2f} g/cm^3")
    print(f"  ASSUMED outer-core density: {RHO_OC_TOP / 1e3:.2f} g/cm^3 at the CMB "
          f"to {RHO_OC_BOT / 1e3:.2f} g/cm^3 at the ICB")
    print(f"  ASSUMED inner-core density: {RHO_IC_TOP / 1e3:.2f} g/cm^3 at the ICB "
          f"to {RHO_IC_CTR / 1e3:.2f} g/cm^3 at the centre")
    print(f"  ASSUMED pure-iron EOS: rho0 = {FE_RHO0 / 1e3:.2f} g/cm^3, "
          f"K0 = {FE_K0 / 1e9:.0f} GPa, K0' = {FE_K0P:.1f}, "
          f"alpha = {ALPHA:.1e} 1/K, Cp = {CP:.0f} J/kg/K, T_CMB = {T_CMB:.0f} K")

    r, rho, mass, g, p = build_radial_model()

    def at(x, arr):
        return float(np.interp(x, r, arr))

    section("2. Mass, gravity and pressure from the assumed profile")
    print(f"  total mass of the model            : {mass[-1]:.4e} kg")
    print(f"  standard Earth mass for comparison : {M_EARTH:.4e} kg "
          f"(model is {100 * (mass[-1] / M_EARTH - 1):+.1f} %)")
    print(f"  core mass {at(R_CORE, mass):.4e} kg, of which outer core "
          f"{at(R_CORE, mass) - at(R_ICB, mass):.4e} kg and inner core "
          f"{at(R_ICB, mass):.4e} kg")
    print(f"  gravity at the CMB  : {at(R_CORE, g):.3f} m/s^2")
    print(f"  gravity at the ICB  : {at(R_ICB, g):.3f} m/s^2")
    print(f"  pressure at the CMB : {at(R_CORE, p) / 1e9:.1f} GPa")
    print(f"  pressure at the ICB : {at(R_ICB, p) / 1e9:.1f} GPa")
    print(f"  pressure at the centre: {p[0] / 1e9:.1f} GPa")
    print("  the mass check is the first test of any assumed profile: a 3-layer")
    print("  mantle reproduces the real Earth's mass to about a per cent, and the")
    print("  pressure at the CMB follows from that mass and the gravity above it.")
    p_cmb, p_icb = at(R_CORE, p), at(R_ICB, p)

    section("3. The pure-iron reference equation of state")
    rho_fe_cmb_300 = bm3_density(p_cmb, FE_RHO0, FE_K0, FE_K0P)
    rho_fe_icb_300 = bm3_density(p_icb, FE_RHO0, FE_K0, FE_K0P)
    print(f"  Birch-Murnaghan EOS, reference state at {FE_K0 / 1e9:.0f} GPa "
          f"and {T_REF:.0f} K:")
    print(f"    at the CMB ({p_cmb / 1e9:.0f} GPa, {T_REF:.0f} K): "
          f"rho_Fe = {rho_fe_cmb_300 / 1e3:.3f} g/cm^3")
    print(f"    at the ICB ({p_icb / 1e9:.0f} GPa, {T_REF:.0f} K): "
          f"rho_Fe = {rho_fe_icb_300 / 1e3:.3f} g/cm^3")
    print(f"  thermal correction with alpha = {ALPHA:.1e} 1/K "
          f"(rho = rho_300 [1 - alpha (T - 300)]):")

    # adiabatic temperature through the outer core, using the model gravity
    def g_of_r(x):
        return float(np.interp(x, r, g))

    _, t_oc = adiabatic_temperature(g_of_r, T_CMB, ALPHA, CP)
    t_icb = t_oc[-1]
    rho_fe_cmb = rho_fe_cmb_300 * (1.0 - ALPHA * (T_CMB - T_REF))
    rho_fe_icb = rho_fe_icb_300 * (1.0 - ALPHA * (t_icb - T_REF))
    print(f"    temperature at the CMB {T_CMB:.0f} K -> "
          f"rho_Fe = {rho_fe_cmb / 1e3:.3f} g/cm^3")
    print(f"    temperature at the ICB {t_icb:.0f} K -> "
          f"rho_Fe = {rho_fe_icb / 1e3:.3f} g/cm^3")
    rho_solid_fe_icb = rho_fe_icb * SOLID_JUMP
    print(f"  assumed melting density jump of {100 * (SOLID_JUMP - 1):.0f} % gives a "
          f"solid-iron reference at the ICB of {rho_solid_fe_icb / 1e3:.3f} g/cm^3")
    print("  the equation of state is the single most influential assumption in")
    print("  this whole calculation: every deficit below scales with it.")

    section("4. Density deficit and the light-element content")
    rho_oc_cmb = rho_outer_core(R_CORE)
    rho_oc_icb = rho_outer_core(R_ICB)
    rho_ic_icb = rho_inner_core(R_ICB)
    deficit_cmb = 1.0 - rho_oc_cmb / rho_fe_cmb
    deficit_icb = 1.0 - rho_oc_icb / rho_fe_icb
    deficit_ic = 1.0 - rho_ic_icb / rho_solid_fe_icb
    print(f"  outer core at the CMB: {rho_oc_cmb / 1e3:.3f} g/cm^3 against pure "
          f"iron {rho_fe_cmb / 1e3:.3f} g/cm^3 -> deficit {100 * deficit_cmb:.1f} %")
    print(f"  outer core at the ICB: {rho_oc_icb / 1e3:.3f} g/cm^3 against pure "
          f"iron {rho_fe_icb / 1e3:.3f} g/cm^3 -> deficit {100 * deficit_icb:.1f} %")
    print(f"  inner core at the ICB: {rho_ic_icb / 1e3:.3f} g/cm^3 against solid "
          f"iron {rho_solid_fe_icb / 1e3:.3f} g/cm^3 -> deficit {100 * deficit_ic:.1f} %")
    print("  the deficit is the mass of light elements, folded into a density.")

    x_cmb = light_fraction(rho_oc_cmb, rho_fe_cmb, RHO_LIGHT_CMB)
    x_icb = light_fraction(rho_oc_icb, rho_fe_icb, RHO_LIGHT_ICB)
    x_ic = light_fraction(rho_ic_icb, rho_solid_fe_icb, RHO_LIGHT_ICB)
    print(f"\n  ideal volume additivity with assumed light-element densities "
          f"{RHO_LIGHT_CMB / 1e3:.1f} and {RHO_LIGHT_ICB / 1e3:.1f} g/cm^3:")
    print(f"    outer core at the CMB: x = {100 * x_cmb:.1f} mass %")
    print(f"    outer core at the ICB: x = {100 * x_icb:.1f} mass %")
    print(f"    inner core at the ICB: x = {100 * x_ic:.1f} mass %")
    print("  sensitivity to the assumed light-element density at the CMB:")
    for rho_l in (3500.0, 5000.0, 6500.0):
        x = light_fraction(rho_oc_cmb, rho_fe_cmb, rho_l)
        print(f"    rho_light = {rho_l / 1e3:.1f} g/cm^3 -> x = {100 * x:.1f} mass %")
    print("  the fraction is the *deficit* divided by a contrast in density, so")
    print("  halving the contrast doubles the inferred light-element content.")

    rho_uniform = 1.0 / ((1.0 - x_cmb) / rho_fe_icb + x_cmb / RHO_LIGHT_ICB)
    print(f"\n  consistency test: a uniform {100 * x_cmb:.1f} mass % light element "
          f"would give")
    print(f"    {rho_uniform / 1e3:.3f} g/cm^3 at the ICB, but the assumed profile "
          f"has {rho_oc_icb / 1e3:.3f} g/cm^3")
    print(f"    ({100 * (rho_oc_icb / rho_uniform - 1):+.1f} %), so either the "
          "light-element fraction grows")
    print("  upward (stratification) or the EOS and temperature are wrong by that")
    print("  much -- the deficit profile is itself a constraint, not just a number.")

    jump_total = rho_ic_icb - rho_oc_icb
    jump_melting = rho_solid_fe_icb - rho_fe_icb
    print(f"\n  the assumed ICB density jump is {jump_total / 1e3:.2f} g/cm^3;")
    print(f"  of that, {jump_melting / 1e3:.2f} g/cm^3 comes from melting pure iron "
          "at the same")
    print(f"  temperature and {jump_total / 1e3 - jump_melting / 1e3:+.2f} g/cm^3 is "
          "left for a change in")
    print("  composition across the boundary, which is why the inner core is")
    print("  usually described as more iron-rich than the outer core.")

    section("5. The adiabatic gradient and the conducted heat flow")
    dt_ds_cmb = ALPHA * g_of_r(R_CORE) * T_CMB / CP
    dt_ds_icb = ALPHA * g_of_r(R_ICB) * t_icb / CP
    print(f"  adiabatic gradient dT/dr = -alpha g T / Cp (alpha = {ALPHA:.1e} 1/K,")
    print(f"    Cp = {CP:.0f} J/kg/K): {dt_ds_cmb * 1e3:.3f} K/km at the CMB and "
          f"{dt_ds_icb * 1e3:.3f} K/km at the ICB")
    print(f"  temperature rises inward from {T_CMB:.0f} K to {t_icb:.0f} K across the "
          f"outer core")
    print(f"    (an adiabatic rise of {t_icb - T_CMB:.0f} K over "
          f"{(R_CORE - R_ICB) / 1e3:.0f} km)")
    print("  the gradient is proportional to g, so it is *smaller* at depth even")
    print("  though the temperature is higher.")
    area = 4.0 * np.pi * R_CORE ** 2
    print(f"\n  conducted (adiabatic) heat flow at the CMB, Q_ad = 4 pi Rc^2 k dT/dr,")
    print(f"  with the core-side area {area:.3e} m^2 and k the thermal conductivity:")
    for k in K_GRID:
        q_ad = area * k * dt_ds_cmb
        print(f"    k = {k:5.0f} W/m/K -> Q_ad = {q_ad / 1e12:5.2f} TW "
              f"({'exceeds' if q_ad > Q_CMB else 'below  '} the assumed "
              f"{Q_CMB / 1e12:.0f} TW CMB heat flow)")
    k_paradox = Q_CMB / (area * dt_ds_cmb)
    print(f"  Q_ad = Q_cmb at k = {k_paradox:.0f} W/m/K: above that conductivity the")
    print("  core conducts away more heat than the CMB supplies, there is nothing")
    print("  left to drive cooling, and the inner core cannot grow.  This tension")
    print("  between the heat conducted down the adiabat and the heat actually")
    print("  leaving the core is the 'new core paradox'.")

    section("6. Cooling, inner-core growth and the age of the inner core")
    mass_core = at(R_CORE, mass)
    c_core = mass_core * CP                      # heat capacity of the core [J/K]
    d_grad = dt_ds_icb - DTM_DS
    print(f"  assumed melting-curve slope {DTM_DS * 1e3:.2f} K/km against an "
          f"adiabatic gradient of")
    print(f"    {dt_ds_icb * 1e3:.3f} K/km at the ICB: the difference "
          f"{d_grad * 1e3:.3f} K/km is what lets")
    print("  the adiabat cross the melting curve at all.  If the melting curve is")
    print("  the steeper of the two, the outer core would freeze from the top down")
    print("  and there would be no liquid outer core.")
    print(f"  heat capacity of the core, M Cp = {c_core:.3e} J/K")
    print(f"\n  cooling rate and inner-core age, for the assumed "
          f"{Q_CMB / 1e12:.0f} TW CMB heat flow:")
    print("    k (W/m/K)   Q_ad (TW)   cooling (K/Myr)   age (Gyr)   "
          "age with latent heat (Gyr)")
    latent_term = L_LATENT * RHO_IC_TOP * 4.0 * np.pi * R_ICB ** 2 / d_grad
    for k in K_GRID:
        q_ad = area * k * dt_ds_cmb
        q_excess = Q_CMB - q_ad
        if q_excess <= 0.0:
            print(f"    {k:9.0f}   {q_ad / 1e12:8.2f}   {'no cooling':>14}   "
                  f"{'--':>9}   {'--':>25}")
            continue
        gamma = q_excess / c_core                       # K/s
        age = R_ICB * d_grad / gamma                    # s
        gamma_lat = q_excess / (c_core + latent_term)   # K/s
        age_lat = R_ICB * d_grad / gamma_lat
        print(f"    {k:9.0f}   {q_ad / 1e12:8.2f}   {gamma * 3.156e13:14.3f}   "
              f"{age / 3.156e16:9.2f}   {age_lat / 3.156e16:25.2f}")
    print(f"  the latent-heat term adds {latent_term / c_core * 100:.0f} % to the "
          "heat the core must")
    print("  remove per kelvin of cooling, so it lengthens the growth time by that")
    print("  factor; gravitational energy release would offset part of it.")
    print(f"\n  sensitivity to the assumed CMB heat flow, at k = {K_GRID[0]:.0f} W/m/K:")
    q_ad = area * K_GRID[0] * dt_ds_cmb
    for q_here in (8.0e12, 10.0e12, 12.0e12):
        q_excess = q_here - q_ad
        if q_excess <= 0.0:
            print(f"    Q_cmb = {q_here / 1e12:.0f} TW -> no cooling at all")
            continue
        gamma = q_excess / c_core
        age = R_ICB * d_grad / gamma / 3.156e16
        gamma_lat = q_excess / (c_core + latent_term)
        age_lat = R_ICB * d_grad / gamma_lat / 3.156e16
        print(f"    Q_cmb = {q_here / 1e12:.0f} TW -> age {age:.2f} Gyr "
              f"({age_lat:.2f} Gyr with latent heat)")

    section("7. The dynamo: why a liquid iron core makes a magnetic field")
    eta = 1.0 / (MU0 * SIGMA)
    length = R_CORE - R_ICB
    rm = U_FLOW * length / eta
    tau = length ** 2 / eta
    elsasser = SIGMA * B_CORE ** 2 / (RHO_OC_TOP * OMEGA)
    print(f"  assumed sigma = {SIGMA:.1e} S/m, U = {U_FLOW:.1e} m/s, "
          f"L = {length / 1e3:.0f} km")
    print(f"  magnetic diffusivity eta = 1/(mu0 sigma) = {eta:.3f} m^2/s")
    print(f"  magnetic Reynolds number Rm = U L / eta = {rm:.0f}")
    print("    (a dynamo needs Rm above roughly 10-100, so the core qualifies)")
    print(f"  magnetic diffusion time L^2 / eta = {tau:.3e} s = "
          f"{tau / 3.156e7:.3e} yr")
    print("    (field structures decay in ~1e5 yr without motion: the field we see")
    print("     is being regenerated now)")
    print(f"  Elsasser number with B = {B_CORE * 1e3:.1f} mT: "
          f"Lambda = sigma B^2/(rho Omega) = {elsasser:.2f}")
    print("    (of order one, as observed: the Lorentz force is comparable to the")
    print("     Coriolis force in the core)")

    q_excess = Q_CMB - area * K_GRID[0] * dt_ds_cmb
    gamma_lat = q_excess / (c_core + latent_term)
    drdt = gamma_lat / d_grad
    dmdt = RHO_IC_TOP * 4.0 * np.pi * R_ICB ** 2 * drdt
    print(f"\n  inner-core growth at k = {K_GRID[0]:.0f} W/m/K:")
    print(f"    dr/dt = (cooling rate)/(gradient difference) = "
          f"{drdt * 3.156e13 / 1e3:.2f} km/Myr")
    print(f"    mass growth rate = {dmdt:.3e} kg/s, of which the light-element")
    print(f"    fraction in the liquid ({100 * x_icb:.1f} mass %) leaves "
          f"{x_icb * dmdt:.3e} kg/s")
    print("  that rejected light element is buoyant: it is the compositional half")
    print("  of the power source that keeps the dynamo running once the thermal")
    print("  part is consumed by conduction down the adiabat.")

    section("8. Summary of the synthetic model")
    print(f"  core radius {R_CORE / 1e3:.0f} km, ICB radius {R_ICB / 1e3:.1f} km")
    print(f"  CMB: {at(R_CORE, p) / 1e9:.1f} GPa, {T_CMB:.0f} K, "
          f"g = {at(R_CORE, g):.2f} m/s^2")
    print(f"  ICB: {at(R_ICB, p) / 1e9:.1f} GPa, {t_icb:.0f} K, "
          f"g = {at(R_ICB, g):.2f} m/s^2")
    print(f"  outer-core density deficit vs pure iron: "
          f"{100 * deficit_cmb:.1f} % at the CMB, {100 * deficit_icb:.1f} % at the ICB")
    print(f"  light-element mass fraction: {100 * x_cmb:.1f} % at the CMB, "
          f"{100 * x_icb:.1f} % at the ICB, {100 * x_ic:.1f} % in the inner core")
    print(f"  inner-core age: the age climbs steeply as k approaches the value")
    print(f"  {k_paradox:.0f} W/m/K at which the conducted heat flow consumes the whole")
    print("  budget; ages from about 1 Gyr to more than 20 Gyr are all reachable")
    print("  inside the assumed range of k and Q_cmb.")
    print("\n  Every number above follows from ASSUMED inputs and the standard")
    print("  constants G, M_Earth and R_Earth.  None of them is a measurement.")


if __name__ == "__main__":
    main()
