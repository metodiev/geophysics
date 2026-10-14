#!/usr/bin/env python3
"""Estuarine and delta geophysics: seawater sound speed and its refraction, the
estuarine mixing classification, salinity intrusion, and the competition between
sediment supply and accommodation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python estuarine_geophysics_demo.py

Everything here is SYNTHETIC.  The sound-speed model, the estuaries and the
sediment budget are teaching models with the stated model constants.  No real
estuary, delta, river or survey is referenced, and no number is quoted from a
published measurement.

Contents
--------
1. A teaching sound-speed model c = sqrt(K/rho) with a linear seawater state
   equation; the vertical profile in a stratified estuary and the sounding error
   from assuming a constant sound speed.
2. Estuarine classification by the densimetric Froude number and the tidal-to-
   river velocity ratio, for three model estuaries.
3. Salinity intrusion length from a steady advection-diffusion balance.
4. Accommodation versus sediment supply: basin fill time with and without
   sea-level rise, and the progradation rate.
5. Worked examples used in the lesson.
"""

import numpy as np
from scipy.optimize import brentq

RNG = np.random.default_rng(20261014)

K_BULK = 2.34e9           # Pa, bulk modulus of seawater (model constant)
RHO_REF, T_REF, S_REF = 1028.0, 10.0, 35.0
ALPHA_T = 2.0e-4          # 1/K, thermal expansion (model value)
BETA_S = 7.8e-4           # 1/(g/kg), haline contraction (model value)
G = 9.80665
SEC_PER_YR = 3.15576e7


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def rho_sw(T_C, S_gkg):
    """Linear seawater state equation about the reference state."""
    return RHO_REF * (1.0 - ALPHA_T * (T_C - T_REF) + BETA_S * (S_gkg - S_REF))


def c_sw(T_C, S_gkg):
    """Sound speed from c = sqrt(K/rho), K constant."""
    return np.sqrt(K_BULK / rho_sw(T_C, S_gkg))


def main():
    section("1. Sound speed and its vertical structure")
    print(f"  model: c = sqrt(K/rho), K = {K_BULK / 1e9:.2f} GPa (constant)")
    print(f"         rho(T,S) = {RHO_REF:.0f}[1 - {ALPHA_T:.1e}(T-{T_REF:.0f}) + "
          f"{BETA_S:.1e}(S-{S_REF:.0f})]")
    print("\n   T (C)   S (g/kg)   rho (kg/m^3)   c (m/s)")
    for T, S in ((0.0, 0.0), (10.0, 35.0), (20.0, 30.0), (8.0, 2.0),
                 (25.0, 36.0)):
        print(f"  {T:6.1f}   {S:9.1f}   {rho_sw(T, S):12.1f}   {c_sw(T, S):7.2f}")
    print("  fresh cold water is FASTER than warm salty water in this model,")
    print("  because the density term dominates the temperature term: the thermal")
    print("  expansion coefficient is smaller than the haline one by a factor of")
    print(f"  {BETA_S / ALPHA_T:.1f}.")

    T_top, S_top, T_bot, S_bot, depth = 20.0, 30.0, 8.0, 2.0, 20.0
    c_top, c_bot = c_sw(T_top, S_top), c_sw(T_bot, S_bot)
    grad = (c_bot - c_top) / depth
    a_rel = grad / c_top
    print(f"\n  stratified estuary: surface T = {T_top:.0f} C, S = {S_top:.0f}; "
          f"bottom T = {T_bot:.0f} C, S = {S_bot:.0f}")
    print(f"    c(surface) = {c_top:.2f} m/s, c(bottom) = {c_bot:.2f} m/s over "
          f"{depth:.0f} m")
    print(f"    gradient {grad:.3f} m/s per m = {a_rel:.2e} relative per m")
    print("\n  sounding error if a constant c0 = 1500 m/s is assumed for a nadir")
    print("  beam (exact linear gradient: the estimate is low by a z^2/2):")
    print("   depth (m)   true velocity range (m/s)   depth error (m)   error (%)")
    for z in (10.0, 25.0, 50.0, 100.0):
        err = -a_rel * z ** 2 / 2.0
        print(f"   {z:9.1f}   {c_top:9.2f} to {c_bot:9.2f}   {err:14.3f}   "
              f"{err / z * 100:9.2f}")
    print("  the error grows with the square of the depth: the model's 2.5% extreme")
    print(f"  gives {a_rel * 100 ** 2 / 2:.2f} m at 100 m, which is larger than the")
    print("  morphological change a monitoring programme tries to resolve, so the")
    print("  sound-speed profile is not an optional correction.")
    theta1 = np.radians(45.0)
    theta2 = np.arcsin(np.sin(theta1) * c_bot / c_top)
    print(f"\n  ray bending: a 45 deg beam in the surface layer reaches "
          f"{np.degrees(theta2):.2f} deg after crossing to the bottom layer")
    print(f"  (Snell: sin(theta)/c is conserved; rays bend toward the slower")
    print(f"   medium).  Over {depth:.0f} m of the same gradient the beam angle")
    print(f"  changes by {np.degrees(theta2) - np.degrees(theta1):+.2f} deg, which")
    print("  changes the footprint spacing and therefore the apparent rugosity.")

    section("2. Estuarine classification")
    estuaries = [
        dict(name="model A", Q=50.0, b=500.0, h=8.0, dT=15.0, u_t=0.10),
        dict(name="model B", Q=200.0, b=800.0, h=6.0, dT=5.0, u_t=0.50),
        dict(name="model C", Q=500.0, b=1200.0, h=4.0, dT=1.0, u_t=1.00),
    ]
    print("  densimetric Froude number Fr_d = u_r / sqrt(g' h), with")
    print("  u_r = Q/(b h), g' = g drho/rho, and the mixing parameter u_t/u_r.")
    print("\n   estuary   Q (m^3/s)   u_r (m/s)   drho (kg/m^3)   Fr_d    u_t/u_r   class")
    for e in estuaries:
        rho1 = rho_sw(10.0, 35.0)
        rho2 = rho_sw(10.0, 35.0) - e["dT"]
        gp = G * e["dT"] / rho1
        u_r = e["Q"] / (e["b"] * e["h"])
        Fr_d = u_r / np.sqrt(gp * e["h"])
        ratio = e["u_t"] / u_r
        if Fr_d < 0.02:
            cls = "salt wedge"
        elif Fr_d < 0.2:
            cls = "partially mixed"
        else:
            cls = "well mixed"
        print(f"   {e['name']:8s} {e['Q']:11.0f}   {u_r:11.4f}   {e['dT']:15.1f}   "
              f"{Fr_d:6.4f}   {ratio:8.1f}   {cls}")
    print("  both parameters matter: Fr_d measures whether the river flow can")
    print("  overcome the buoyancy of the density difference, and u_t/u_r measures")
    print("  how much tidal energy is available to mix.  The thresholds used here")
    print("  are model choices, stated in the code.")

    section("3. Salinity intrusion")
    print("  steady balance: u S = K_x dS/dx  ->  S(x) = S0 exp(-x/L_d),")
    print("  with L_d = K_x / u the e-folding intrusion length.")
    K_x, S0_ocean, S_1ppt = 200.0, 30.0, 1.0
    print(f"  model values: K_x = {K_x:.0f} m^2/s (constant), oceanic salinity "
          f"{S0_ocean:.0f} g/kg")
    print("\n   Q (m^3/s)   b (m)   h (m)   u_r (m/s)   L_d (km)   distance to 1 g/kg (km)")
    for Q, b, h in ((50.0, 500.0, 8.0), (100.0, 600.0, 7.0), (200.0, 800.0, 6.0),
                    (400.0, 1000.0, 5.0)):
        u_r = Q / (b * h)
        L_d = K_x / u_r
        x_1ppt = L_d * np.log(S0_ocean / S_1ppt)
        print(f"   {Q:9.0f}   {b:7.0f}   {h:7.0f}   {u_r:11.4f}   "
              f"{L_d / 1e3:9.2f}   {x_1ppt / 1e3:27.2f}")
    print(f"  the 1 g/kg isohaline sits ln({S0_ocean:.0f}/{S_1ppt:.0f}) = "
          f"{np.log(S0_ocean / S_1ppt):.2f} e-folding lengths from the mouth in")
    print("  this model.")
    print("  with K_x held constant the intrusion length scales as 1/Q, so")
    print("  doubling the river flow halves the intrusion.  That is the model's")
    print("  weakest assumption: in reality K_x grows with the tidal energy and")
    print("  with the flow, and the observed dependence is much weaker.")
    u1, u2 = 200.0 / (800.0 * 6.0), 400.0 / (1000.0 * 5.0)
    print(f"  check: u_r rises from {u1:.4f} to {u2:.4f} m/s "
          f"({u2 / u1:.2f}x) while L_d falls from {K_x / u1 / 1e3:.2f} to "
          f"{K_x / u2 / 1e3:.2f} km ({u1 / u2:.2f}x)")

    section("4. Accommodation versus sediment supply")
    area, depth_m, slr = 100e6, 5.0, 0.004
    Q_river, ssc, rho_bulk = 200.0, 0.20, 1660.0
    load_kg = Q_river * ssc * SEC_PER_YR
    supply = load_kg / rho_bulk
    accommodation = area * slr
    print(f"  basin area {area / 1e6:.0f} km^2, mean depth {depth_m:.0f} m, "
          f"sea-level rise {slr * 1e3:.0f} mm/yr")
    print(f"  river discharge {Q_river:.0f} m^3/s with suspended load "
          f"{ssc * 1e3:.0f} mg/L")
    print(f"    sediment mass flux = {load_kg:.3e} kg/yr = {load_kg / 1e9:.2f} Mt/yr")
    print(f"    bulk volume (deposited at bulk density {rho_bulk:.0f} kg/m^3) = "
          f"{supply:.3e} m^3/yr")
    print(f"  accommodation created by the rise = area x SLR = "
          f"{accommodation:.3e} m^3/yr")
    print(f"  net infilling rate = supply - accommodation = "
          f"{supply - accommodation:.3e} m^3/yr")
    area_rate = (supply - accommodation) / depth_m
    print(f"  area lost per year = net / mean depth = {area_rate:.3e} m^2/yr "
          f"= {area_rate / 1e6:.4f} km^2/yr")
    print(f"  naive fill time at that rate = {area / area_rate:.0f} yr")

    T_eq = supply / slr
    if area < T_eq:
        t_with = (depth_m / slr) * np.log(T_eq / (T_eq - area))
    else:
        t_with = np.inf
    t_without = area * depth_m / supply
    print(f"\n  the net rate is not constant: as the basin fills, the accommodation")
    print(f"  shrinks.  Solving dA/dt = -(supply - A SLR)/d analytically:")
    print("    A(t) = supply/SLR + (A0 - supply/SLR) exp(+SLR t/d), so the")
    print("    accommodation shrinks as the basin fills and the net rate rises")
    print(f"    equilibrium area supply/SLR = {T_eq / 1e6:.1f} km^2 "
          f"(larger than the present {area / 1e6:.0f} km^2,")
    print("     so the basin fills completely rather than reaching equilibrium)")
    print(f"    fill time WITH the rise = (d/SLR) ln[(supply/SLR)/(supply/SLR-A0)]"
          f" = {t_with:.0f} yr")
    print(f"    fill time WITHOUT the rise = A0 d / supply = {t_without:.0f} yr")
    print(f"  the rise lengthens the fill by {(t_with / t_without - 1) * 100:.0f}%,")
    print(f"  the constant-net-rate estimate above ({area / area_rate:.0f} yr)")
    print("  overstates it, because it holds the accommodation at its initial")
    print("  (largest) value instead of letting it shrink.")

    section("5. Worked examples used in the lesson")
    print(f"(a) c(10 C, 35) = {c_sw(10.0, 35.0):.2f} m/s; "
          f"c(0 C, 0) = {c_sw(0.0, 0.0):.2f} m/s")
    print(f"(b) gradient in the model estuary = {grad:.3f} m/s per m; a 50 m")
    print(f"    sounding is low by {a_rel * 50 ** 2 / 2:.3f} m "
          f"({a_rel * 50 ** 2 / 2 / 50 * 100:.2f}%) if c = 1500 m/s is assumed")
    print(f"(c) model B: u_r = {200.0 / (800 * 6):.4f} m/s, "
          f"Fr_d = {200.0 / (800 * 6) / np.sqrt(9.80665 * 5.0 / rho_sw(10.0, 35.0) * 6.0):.4f}")
    print(f"(d) L_d for model B = {K_x / (200.0 / (800 * 6)) / 1e3:.2f} km; "
          f"distance to 1 g/kg = "
          f"{K_x / (200.0 / (800 * 6)) / 1e3 * np.log(30.0):.2f} km")
    print(f"(e) supply = {supply:.3e} m^3/yr, accommodation = "
          f"{accommodation:.3e} m^3/yr; fill times {t_with:.0f} yr (with SLR) and")
    print(f"    {t_without:.0f} yr (without)")
    print("\nAll numbers are SYNTHETIC model output.")


if __name__ == "__main__":
    main()
