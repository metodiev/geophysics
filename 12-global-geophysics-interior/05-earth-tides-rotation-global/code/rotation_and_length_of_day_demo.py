#!/usr/bin/env python3
"""Rotation variations, length of day and core-mantle coupling.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rotation_and_length_of_day_demo.py

Everything here is a SYNTHETIC teaching model.  The moment of inertia, the
conductivity, the topography and the wind series are adopted inputs; no measured
length-of-day value, coupling torque or lower-mantle conductivity is quoted.

Contents
--------
1. The angular momentum budget and what a millisecond of length of day costs.
2. A synthetic zonal-wind series and the part of the signal it explains.
3. The residual, and the core angular momentum it requires.
4. Electromagnetic coupling: the time constant and the conductivity it implies.
5. Topographic coupling: the torque capacity, verified by direct integration.
6. The inner core: how much differential rotation the residual requires.
7. A two-layer integration as a check on the budget arithmetic.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

OMEGA = 7.292115e-5        # rad/s, WGS 84 defining value
LOD = 86400.0              # s, adopted mean solar day
C_EARTH = 8.04e37          # kg m^2, adopted polar moment of inertia
C_CORE = 9.44e36           # kg m^2, adopted core contribution
C_INNER = 5.85e34          # kg m^2, adopted inner-core contribution
R_CMB = 3.480e6            # m
MU0 = 4.0e-7 * np.pi
DRHO = 4400.0              # kg/m^3, adopted density jump at the CMB
G_CMB = 10.7               # m/s^2, adopted gravity at the CMB
AREA_CMB = 4.0 * np.pi * R_CMB**2


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. The angular momentum budget")
    h3 = C_EARTH * OMEGA
    print(f"adopted: Omega = {OMEGA:.6e} rad/s, LOD = {LOD:.0f} s,"
          f" C = {C_EARTH:.3e} kg m^2")
    print(f"axial angular momentum of the solid Earth: C*Omega = {h3:.4e} kg m^2/s")
    print("\n  Delta LOD (ms)   Delta L / H3   Delta L (kg m^2/s)")
    for dlod_ms in (0.1, 0.5, 1.0, 5.0):
        frac = dlod_ms * 1.0e-3 / LOD
        print(f"  {dlod_ms:15.1f} {frac:14.4e} {frac * h3:25.4e}")
    print(f"\nthe conversion is Delta LOD/LOD = Delta H3/(C*Omega): the fractional")
    print(f"change in the day length equals the fractional change in axial angular")
    print(f"momentum, which is why millisecond-level LOD changes require")
    print(f"angular-momentum changes of order {1.0e-3 / LOD * h3:.2e} kg m^2/s")

    section("2. A synthetic zonal-wind series")
    t_yr = np.linspace(0.0, 40.0, 1601)
    annual = 0.6e25 * np.sin(2.0 * np.pi * t_yr / 1.0)
    decadal = 1.1e25 * np.sin(2.0 * np.pi * t_yr / 11.0 + 0.7)
    trend = -0.06e25 * t_yr / 40.0
    h_wind = annual + decadal + trend
    dlod_wind = LOD * h_wind / h3 * 1.0e3
    print(f"adopted wind angular momentum: an annual term of amplitude"
          f" {np.ptp(annual) / 2 / 1e25:.2f}e25, a decadal term of amplitude")
    print(f"{np.ptp(decadal) / 2 / 1e25:.2f}e25 and a linear drift, in kg m^2/s")
    print(f"  full range of the synthetic wind series:"
          f" {np.ptp(h_wind) / 1e25:.3f}e25 kg m^2/s")
    print(f"  implied LOD range: {np.ptp(dlod_wind):.3f} ms")
    print(f"  rms of the implied LOD series: {np.std(dlod_wind):.3f} ms")

    section("3. The residual and the core angular momentum it requires")
    core_signal = 0.35e25 * np.sin(2.0 * np.pi * t_yr / 7.0 + 2.1)
    dlod_total = LOD * (h_wind + core_signal) / h3 * 1.0e3
    dlod_resid = dlod_total - dlod_wind
    print(f"adopted core contribution: amplitude {np.ptp(core_signal) / 2 / 1e25:.2f}e25"
          f" kg m^2/s, period 7 yr")
    print(f"  total synthetic LOD range     : {np.ptp(dlod_total):.3f} ms")
    print(f"  residual after removing winds : {np.ptp(dlod_resid):.3f} ms")
    print(f"  core angular momentum implied : {np.ptp(dlod_resid) * 1e-3 / LOD * h3 / 2 / 1e25:.3f}e25"
          " kg m^2/s")
    torque_needed = (np.ptp(dlod_resid) * 1e-3 / LOD * h3) / (
        7.0 * 3.1557e7)
    print(f"\nto produce that change in 7 yr requires a mean torque of"
          f" {torque_needed:.3e} N m")
    print("this is the number the coupling mechanisms must be able to supply;")
    print("everything below is an estimate of whether they can")

    section("4. Electromagnetic coupling")
    print("scaling estimate: tau_EM = mu0*sigma*d*D, with d the thickness of the")
    print("conducting layer and D the horizontal scale of the shear, adopted here")
    print(f"as 2*pi*R_cmb = {2 * np.pi * R_CMB:.3e} m")
    d_horiz = 2.0 * np.pi * R_CMB
    print("\n  d (km)   tau = 10 yr -> sigma (S/m)   tau = 1 yr -> sigma (S/m)"
          "   tau = 30 yr -> sigma (S/m)")
    for d_km in (50.0, 100.0, 200.0):
        d = d_km * 1.0e3
        row = []
        for tau_yr in (10.0, 1.0, 30.0):
            sigma = tau_yr * 3.1557e7 / (MU0 * d * d_horiz)
            row.append(sigma)
        print(f"  {d_km:8.0f} {row[0]:26.3e} {row[1]:26.3e} {row[2]:26.3e}")
    sigma_ref = 10.0 * 3.1557e7 / (MU0 * 100.0e3 * d_horiz)
    print(f"\nfor a 100-km layer and a decadal time constant: sigma ="
          f" {sigma_ref:.3f} S/m")
    print("that is a semiconductor, not a metal: the inference is that the")
    print("lowermost mantle must be far less conductive than the core for the")
    print("electromagnetic torque to act on a decadal timescale")

    section("5. Topographic coupling")
    print("axial torque of a sinusoidal CMB topography, pressure in quadrature:")
    print("  tau = integral p*(dh/dphi)*R^2*sin^2(theta) dtheta dphi")
    print("      = (pi^2/2)*drho*g*h0^2*m*R^2")
    print("\n  h0 (km)   m   tau_max (N m)   ratio to the required torque")
    for h0_km in (0.1, 0.5, 1.0, 2.0):
        for m_mode in (2.0,):
            tau_max = (np.pi**2 / 2.0) * DRHO * G_CMB * (h0_km * 1e3) ** 2 \
                * m_mode * R_CMB**2
            print(f"  {h0_km:7.1f} {m_mode:3.0f} {tau_max:15.3e}"
                  f" {tau_max / torque_needed:26.3e}")
    tau_ref = (np.pi**2 / 2.0) * DRHO * G_CMB * (0.5e3) ** 2 * 2.0 * R_CMB**2
    print(f"\na 0.5-km topography at m = 2 gives {tau_ref:.3e} N m against the"
          f" required {torque_needed:.3e} N m")
    print(f"i.e. a capacity {tau_ref / torque_needed:.1e} times the requirement:")
    print("topographic coupling is not marginal, it is enormous - provided the")
    print("long-wavelength topography exists and is not compensated")
    theta = np.linspace(0.0, np.pi, 400)
    phi = np.linspace(0.0, 2.0 * np.pi, 2000)
    th, ph = np.meshgrid(theta, phi, indexing="ij")
    m_num = 2.0
    h0 = 0.5e3
    h_top = h0 * np.cos(m_num * ph)
    p_press = DRHO * G_CMB * h0 * np.sin(m_num * ph)
    integrand = p_press * np.gradient(h_top, phi[1] - phi[0], axis=1) \
        * R_CMB**2 * np.sin(th) ** 2
    tau_num = np.trapezoid(np.trapezoid(integrand, phi, axis=1), theta)
    print(f"\nnumerical check by quadrature over the sphere: {tau_num:.4e} N m")
    print(f"analytic (pi^2/2)*drho*g*h0^2*m*R^2: {tau_ref:.4e} N m")
    print(f"difference: {abs(abs(tau_num) - tau_ref) / tau_ref * 100:.3f}%"
          " (the sign is set by the assumed phase lag)")

    section("6. The inner core and differential rotation")
    print(f"adopted moments of inertia: whole Earth {C_EARTH:.3e},"
          f" core {C_CORE:.3e}, inner core {C_INNER:.3e} kg m^2")
    dl_core = np.ptp(dlod_resid) * 1e-3 / LOD * h3 / 2.0
    domega_core = dl_core / C_CORE
    domega_inner = dl_core / C_INNER
    print(f"\nrequired angular momentum change: {dl_core:.3e} kg m^2/s")
    print(f"  if supplied by the whole core: dOmega = {domega_core:.3e} rad/s"
          f" = {domega_core / OMEGA:.3e} of Omega")
    print(f"  if supplied by the inner core alone: dOmega = {domega_inner:.3e}"
          f" rad/s = {domega_inner / OMEGA:.3e} of Omega")
    print(f"  in degrees per year: {np.degrees(domega_core) * 3.1557e7:.4e}"
          f" (whole core), {np.degrees(domega_inner) * 3.1557e7:.4e} (inner core)")
    print("the same angular momentum in a smaller body means a larger rotation")
    print("change, which is why the inner core is the most sensitive detector of")
    print("core-mantle angular momentum exchange")

    section("7. A two-layer integration as a check on the budget")
    c_m = C_EARTH - C_CORE
    s0 = 1.0e-10               # rad/s, initial core-mantle shear
    k_couple = 1.0e29          # N m per rad/s, linear coupling
    decay = k_couple * (1.0 / c_m + 1.0 / C_CORE)
    t_yr = np.linspace(0.0, 40.0, 40001)
    shear = s0 * np.exp(-decay * t_yr * 3.1557e7)
    domega_m = (C_CORE / (c_m + C_CORE)) * (s0 - shear)
    dlod = -domega_m / OMEGA * LOD * 1.0e3
    domega_c = -(c_m / C_CORE) * domega_m
    print(f"adopted linear coupling {k_couple:.1e} N m per rad/s,"
          f" initial shear {s0:.1e} rad/s")
    print(f"  coupling time constant 1/(k*(1/C_m + 1/C_c)) ="
          f" {1.0 / decay / 3.1557e7:.2f} yr")
    print("   t (yr)   shear (rad/s)   dOmega_m (rad/s)   dLOD (ms)")
    for t_target in (0.0, 10.0, 20.0, 40.0):
        i = int(np.argmin(np.abs(t_yr - t_target)))
        print(f"  {t_yr[i]:7.0f} {shear[i]:15.4e} {domega_m[i]:18.4e}"
              f" {dlod[i]:12.4f}")
    l_before = c_m * OMEGA + C_CORE * (OMEGA + s0)
    l_after = c_m * (OMEGA + domega_m[-1]) + C_CORE * (
        OMEGA + s0 + domega_c[-1])
    print(f"\n  total angular momentum before: {l_before:.12e} kg m^2/s")
    print(f"  total angular momentum after : {l_after:.12e} kg m^2/s")
    print(f"  conservation residual        :"
          f" {abs(l_after - l_before) / l_before:.3e}")
    print("the exchange conserves total angular momentum to machine precision;")
    print("only the partition between the layers changes, which is why an LOD")
    print("change is evidence of an internal torque and never of a change in the")
    print("total")
    print("\nSYNTHETIC teaching model; no measured length-of-day value is used.")


if __name__ == "__main__":
    main()
