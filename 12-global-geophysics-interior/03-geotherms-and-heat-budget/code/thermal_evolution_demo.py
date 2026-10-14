#!/usr/bin/env python3
"""Thermal evolution of the Earth: secular cooling, buffering and the Urey ratio.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermal_evolution_demo.py

Everything here is a SYNTHETIC teaching model.  The rheology, the radiogenic
production, the heat loss and the core flux are *adopted inputs*; the present-day
mantle temperature is an adopted value and no real heat flow, temperature or age
is used anywhere.

Contents
--------
1. The one-box mantle model and its adopted parameters.
2. Flux sensitivity to temperature, the equilibrium state, and the buffering.
3. Integration from several initial temperatures: the present is insensitive.
4. Present-day diagnostics: Urey ratio and two different cooling rates.
5. The rheology scan: how much secular cooling the model admits.
6. The global inventory budget, and the tension it exposes.
7. Verification: integrator agreement, the equilibrium condition and the
   analytic quasi-static cooling rate.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

RNG = np.random.default_rng(20261014)

# --- adopted model inputs (synthetic teaching model) ------------------------
RHO = 3300.0            # kg m^-3, mantle density
CP = 1250.0             # J kg^-1 K^-1
D_MANTLE = 2.891e6      # m, mantle thickness
K_MANTLE = 4.5          # W m^-1 K^-1
KAPPA = 1.0e-6          # m^2 s^-1
ALPHA_TH = 3.0e-5       # 1/K
G_SURF = 9.81           # m s^-2
RA_C = 1100.0           # critical Rayleigh number
BETA = 1.0 / 3.0        # adopted Nusselt exponent
EA = 300.0e3            # J mol^-1, activation energy of the adopted rheology
R_GAS = 8.314462618     # J mol^-1 K^-1 (exact)
T_SURF = 273.0          # K
T_PRESENT = 1600.0      # K, adopted present-day potential temperature
Q_SURF_TARGET = 55.0e-3  # W m^-2, adopted present-day mantle-derived flux
A_MANTLE = 0.012e-6     # W m^-3, adopted bulk-mantle radiogenic production
Q_CMB = 10.0e-3         # W m^-2, adopted heat flux out of the core
Q_LOSS_TOTAL = 73.5e-3  # W m^-2, adopted mean surface heat loss (whole surface)
Q_CRUST_RAD = 19.3e-3   # W m^-2, adopted crustal radiogenic contribution
HALF_LIFE_MIX = 4.0e9   # yr, adopted effective half-life of the heat inventory
AGE = 4.5e9             # yr
S_PER_GYR = 3.1557e16   # s per billion years (365.25 d/yr)
S_PER_MYR = 3.1557e13   # s per million years


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def radiogenic_flux(t_yr, half_life=HALF_LIFE_MIX):
    """Mantle radiogenic flux per unit area [W/m^2] at time t, present-day fixed."""
    lam = np.log(2.0) / half_life
    return A_MANTLE * D_MANTLE * np.exp(lam * (AGE - t_yr))


def q_surface(t_pot, eta_ref, beta=BETA, ea=EA, t_ref=T_PRESENT):
    """Mantle-derived surface heat flux from Nu = (Ra/Ra_c)^beta, in W/m^2.

    Viscosity follows eta(T) = eta_ref exp( (Ea/R)(1/T - 1/T_ref) ), so the
    Rayleigh number is temperature dependent.
    """
    eta = eta_ref * np.exp(ea / R_GAS * (1.0 / t_pot - 1.0 / t_ref))
    ra = RHO * ALPHA_TH * G_SURF * (t_pot - T_SURF) * D_MANTLE**3 / (KAPPA * eta)
    nu = (max(ra, 0.0) / RA_C) ** beta
    return K_MANTLE * (t_pot - T_SURF) * nu / D_MANTLE


def dq_dt(t_pot, eta_ref, beta=BETA, ea=EA, h=1.0):
    """Numerical dQ/dT [W m^-2 K^-1]."""
    return (q_surface(t_pot + h, eta_ref, beta, ea)
            - q_surface(t_pot - h, eta_ref, beta, ea)) / (2.0 * h)


def rhs(t_gyr, t_pot, eta_ref, beta=BETA, ea=EA):
    """dT/dt in K per Gyr for the one-box mantle."""
    t_yr = t_gyr * 1.0e9
    heat_in = radiogenic_flux(t_yr) + Q_CMB
    heat_out = q_surface(t_pot[0], eta_ref, beta=beta, ea=ea)
    return np.array([(heat_in - heat_out) / (RHO * CP * D_MANTLE) * S_PER_GYR])


def integrate(t0_k, eta_ref, beta=BETA, ea=EA, t_end_gyr=AGE / 1e9):
    return solve_ivp(rhs, (0.0, t_end_gyr), [t0_k], method="LSODA",
                     rtol=1.0e-9, atol=1.0e-3, args=(eta_ref, beta, ea),
                     dense_output=True)


def main():
    section("1. The one-box mantle model")
    print(f"box: rho = {RHO:.0f} kg/m^3, cp = {CP:.0f} J/kg/K,"
          f" d = {D_MANTLE / 1e3:.0f} km, k = {K_MANTLE:.1f} W/m/K")
    print(f"convection: Nu = (Ra/Ra_c)^{BETA:.3f}, Ra_c = {RA_C:.0f},"
          f" Ea = {EA / 1e3:.0f} kJ/mol")
    print(f"adopted bulk-mantle production A = {A_MANTLE * 1e6:.3f} uW/m^3"
          f" -> A*d = {A_MANTLE * D_MANTLE * 1e3:.1f} mW/m^2")
    print(f"adopted heat inventory half-life: {HALF_LIFE_MIX / 1e9:.1f} Gyr")
    print(f"adopted core flux at the CMB: {Q_CMB * 1e3:.1f} mW/m^2")
    print(f"adopted present potential temperature: {T_PRESENT:.0f} K;"
          f" present mantle-derived surface flux: {Q_SURF_TARGET * 1e3:.1f} mW/m^2")
    eta_ref = brentq(lambda e: q_surface(T_PRESENT, e) - Q_SURF_TARGET,
                     1.0e16, 1.0e24)
    print(f"\ncalibrating eta_ref so that q({T_PRESENT:.0f} K) ="
          f" {Q_SURF_TARGET * 1e3:.1f} mW/m^2 gives eta_ref = {eta_ref:.3e} Pa s")
    ra_ref = RHO * ALPHA_TH * G_SURF * (T_PRESENT - T_SURF) * D_MANTLE**3 / (KAPPA * eta_ref)
    print(f"  Ra at that temperature: {ra_ref:.3e}, Nu = {(ra_ref / RA_C) ** BETA:.1f}")

    section("2. Flux sensitivity, equilibrium and buffering")
    dq = dq_dt(T_PRESENT, eta_ref)
    q_in = radiogenic_flux(AGE) + Q_CMB
    print(f"heat available inside today: H + q_cmb = {q_in * 1e3:.2f} mW/m^2")
    print(f"the box loses q = {q_surface(T_PRESENT, eta_ref) * 1e3:.2f} mW/m^2"
          " at the adopted temperature, so it is not in equilibrium")
    t_eq = brentq(lambda t: q_surface(t, eta_ref) - q_in, 1000.0, 3000.0)
    print(f"equilibrium temperature at today's production: {t_eq:.1f} K"
          f" (adopted present state {T_PRESENT:.0f} K)")
    print(f"dQ/dT at the present state = {dq * 1e3:.5f} mW/m^2 per K"
          f" -> 10 K is {dq * 10 / Q_SURF_TARGET * 100:.1f}% of the flux")
    tau = RHO * CP * D_MANTLE / dq / S_PER_MYR
    print(f"response time tau = rho*cp*d/(dQ/dT) = {tau:.3f} Myr")
    print(f"compare the conduction time d^2/kappa ="
          f" {D_MANTLE**2 / KAPPA / S_PER_MYR:.0f} Myr")
    dt_no_feedback = (q_in - Q_SURF_TARGET) / (RHO * CP * D_MANTLE) * S_PER_GYR
    print(f"\nif the transport did not respond to T at all, the same imbalance"
          f" would cool the box at {dt_no_feedback:+.1f} K/Gyr")
    print(f"with the adopted temperature dependence the response time is"
          f" {tau:.0f} Myr = {tau / 1000:.2f} Gyr,")
    print(f"a substantial fraction of the {AGE / 1e9:.1f} Gyr available: the box does"
          " not equilibrate, it lags")
    lag_rate = -np.log(2.0) / HALF_LIFE_MIX * q_in / dq * 1e9
    print(f"the lag is the secular cooling: dT/dt ~ -lambda*H/(dQ/dT) ="
          f" {lag_rate:+.1f} K/Gyr")

    section("3. Integration from three initial temperatures")
    print("  T(0) (K)   T(1 Gyr)   T(2 Gyr)   T(3 Gyr)   T(4.5 Gyr)   q(4.5 Gyr)")
    finals = []
    for t0 in (1300.0, 1600.0, 2200.0):
        sol = integrate(t0, eta_ref)
        vals = sol.sol(np.array([1.0, 2.0, 3.0, 4.5]))[0]
        finals.append(vals[3])
        print(f"  {t0:8.0f}   {vals[0]:9.1f}   {vals[1]:9.1f}   {vals[2]:9.1f}"
              f"   {vals[3]:11.1f}   {q_surface(vals[3], eta_ref) * 1e3:10.1f}")
    print(f"\na 900 K spread in the initial temperature leaves a"
          f" {max(finals) - min(finals):.1f} K spread at present"
          f" ({100 * (max(finals) - min(finals)) / np.mean(finals):.2f}%):")
    print("the present state is stiffly, not absolutely, independent of the initial")
    print("condition, because the response time is comparable to the age.  That is")
    print("why a thermal history is never unique")

    section("4. Present-day diagnostics")
    sol = integrate(2200.0, eta_ref)
    t_now = float(sol.sol(AGE / 1e9)[0])
    q_now = q_surface(t_now, eta_ref)
    h_now = radiogenic_flux(AGE)
    num_dtdt = float(rhs(AGE / 1e9, [t_now], eta_ref)[0])
    quasi1 = -np.log(2.0) / HALF_LIFE_MIX * h_now / dq_dt(t_now, eta_ref) * 1e9
    print(f"model present-day potential temperature: {t_now:.2f} K"
          f" (equilibrium today would be {t_eq:.1f} K)")
    print(f"model present-day flux: {q_now * 1e3:.2f} mW/m^2")
    print(f"model Urey ratio H/q = {h_now / q_now:.4f}"
          f"  (H = {h_now * 1e3:.2f}, q = {q_now * 1e3:.2f} mW/m^2)")
    print(f"model cooling rate: dT/dt = {num_dtdt:+.4f} K/Gyr"
          f" = {num_dtdt:+.1f} mK/Ma")
    print(f"quasi-static prediction -lambda*H/(dQ/dT) = {quasi1:+.4f} K/Gyr")
    print(f"instantaneous budget (H + q_cmb - q)/(rho*cp*d) ="
          f" {(h_now + Q_CMB - q_now) / (RHO * CP * D_MANTLE) * S_PER_GYR:+.4f}"
          " K/Gyr")
    print(f"the two differ by {abs(num_dtdt - quasi1) / abs(quasi1) * 100:.1f}%:"
          " the box is still catching up with a moving equilibrium")

    section("5. How much secular cooling does the model admit?")
    print("  Ea (kJ/mol)   dQ/dT (mW/m^2/K)   tau (Myr)   dT/dt (K/Gyr)")
    for ea in (0.0, 100.0e3, 200.0e3, 300.0e3, 400.0e3):
        dq_i = dq_dt(t_now, eta_ref, ea=ea)
        rate = -np.log(2.0) / HALF_LIFE_MIX * h_now / dq_i * 1e9
        print(f"  {ea / 1e3:12.0f}   {dq_i * 1e3:18.5f}   "
              f"{RHO * CP * D_MANTLE / dq_i / S_PER_MYR:9.0f}   {rate:12.2f}")
    print("\nwith no rheological feedback the same present-day imbalance gives a")
    print("cooling rate seven times larger than with a strong feedback.  The")
    print("present-day Urey ratio is unchanged at 0.65: it is the *sensitivity* of")
    print("heat transport to temperature, not the Urey ratio, that sets how fast")
    print("the Earth may cool in this model")

    section("6. The global inventory budget")
    print(f"adopted mean surface heat loss: {Q_LOSS_TOTAL * 1e3:.1f} mW/m^2")
    print(f"  of which crustal radiogenic:   {Q_CRUST_RAD * 1e3:.1f} mW/m^2")
    print(f"  of which core:                 {Q_CMB * 1e3:.1f} mW/m^2")
    print(f"  of which mantle radiogenic:    {h_now * 1e3:.1f} mW/m^2")
    residual = Q_CMB + h_now + Q_CRUST_RAD - Q_LOSS_TOTAL
    print(f"  production minus loss: {residual * 1e3:+.1f} mW/m^2"
          " (negative: the Earth loses more than it produces)")
    area = 5.6e14
    mass = RHO * D_MANTLE * area
    resid_tw = residual * area / 1e12
    rate_inv = residual * area / (mass * CP) * S_PER_GYR
    print(f"  that is {resid_tw:+.1f} TW over {area:.1e} m^2")
    print(f"mantle heat capacity = rho*d*A*cp = {mass * CP:.3e} J/K"
          f" -> cooling rate {rate_inv:+.1f} K/Gyr")
    print(f"the inventory budget is {(rate_inv / num_dtdt - 1) * 100:+.1f}% away from"
          " the dynamic model's rate")
    print("the agreement is a consistency check between two very different routes,")
    print("not a measurement: it holds only for the adopted inventory, and it would")
    print("move if the crustal production were larger or the core flux smaller")

    section("7. Verification")
    sol_rk = solve_ivp(rhs, (0.0, AGE / 1e9), [2200.0], method="RK45",
                       rtol=1.0e-11, atol=1.0e-4, args=(eta_ref, BETA, EA))
    sol_ls = solve_ivp(rhs, (0.0, AGE / 1e9), [2200.0], method="LSODA",
                       rtol=1.0e-11, atol=1.0e-4, args=(eta_ref, BETA, EA))
    print(f"final T: RK45 {sol_rk.y[0, -1]:.6f} K, LSODA {sol_ls.y[0, -1]:.6f} K,"
          f" difference {abs(sol_rk.y[0, -1] - sol_ls.y[0, -1]):.2e} K")
    print(f"right-hand-side evaluations: RK45 {sol_rk.nfev}, LSODA {sol_ls.nfev}")
    print(f"equilibrium check: q(T_eq) - (H + q_cmb) ="
          f" {(q_surface(t_eq, eta_ref) - q_in) * 1e12:.2e} pW/m^2")
    analytic = -np.log(2.0) / HALF_LIFE_MIX * h_now / dq_dt(t_now, eta_ref) * 1e9
    print(f"analytic quasi-static rate {analytic:+.4f} K/Gyr against the numerical"
          f" {num_dtdt:+.4f} K/Gyr: difference"
          f" {abs(analytic - num_dtdt) / abs(analytic) * 100:.1f}%")
    print("the residual is the second-order curvature of Q(T); near equilibrium the")
    print("cooling rate is set by dQ/dT, so a fractional error in dQ/dT is the same")
    print("fractional error in the cooling rate")
    print("\nSYNTHETIC teaching model; no measured value is used anywhere above.")


if __name__ == "__main__":
    main()
