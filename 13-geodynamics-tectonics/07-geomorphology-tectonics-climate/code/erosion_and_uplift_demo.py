#!/usr/bin/env python3
"""Erosion, uplift and thermochronology: the steady geotherm with exhumation,
closure depth and apparent age, the age-elevation slope as an exhumation-rate
measurement, the bias from a transient history, and the topographic perturbation
of the closure isotherm.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python erosion_and_uplift_demo.py

Everything is SYNTHETIC: the closure temperature, the thermal parameters and the
exhumation histories are chosen teaching values.  No measured age or real
thermochronology data set is used.

Contents
--------
1. Steady geotherm with exhumation, and the Peclet number that controls it.
2. Closure depth and apparent age.
3. The age-elevation slope recovers the exhumation rate, exactly in steady state.
4. The bias a transient exhumation history puts into that inference.
5. The topographic perturbation of the closure isotherm.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


KAPPA = 1.0e-6                 # m^2/s, chosen thermal diffusivity
KAPPA_YR = KAPPA * 3.1557e7    # m^2/yr
T_MANTLE = 1350.0              # deg C, chosen temperature at the base of the layer
T_SURFACE = 10.0               # deg C, chosen mean surface temperature
L_KM = 40.0                    # km, chosen thickness of the conducting layer
T_CLOSURE = 200.0              # deg C, chosen closure temperature of the system
YR = 3.1557e7                  # s, julian year


def geotherm(z_km, e_mm_yr):
    """Steady geotherm with vertical exhumation: T(z) = Ts + (Tm - Ts) *
    (1 - exp(-Pe z/L)) / (1 - exp(-Pe)), with Pe = E L / kappa."""
    z = np.asarray(z_km, dtype=float) * 1e3
    L = L_KM * 1e3
    pe = (e_mm_yr * 1e-3) * L / KAPPA_YR
    if abs(pe) < 1e-12:
        return T_SURFACE + (T_MANTLE - T_SURFACE) * z / L
    return T_SURFACE + (T_MANTLE - T_SURFACE) * \
        (1.0 - np.exp(-pe * z / L)) / (1.0 - np.exp(-pe))


def closure_depth_km(e_mm_yr, t_closure=T_CLOSURE):
    """Depth of the closure isotherm in the steady state, by bisection."""
    lo, hi = 0.0, L_KM
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if float(geotherm(mid, e_mm_yr)) < t_closure:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def demonstration_1():
    section("1. Steady geotherm with exhumation")
    print("  The conducting layer is exhumed upward at rate E relative to the")
    print("  fixed isotherms below, so heat is advected as well as conducted:")
    print("     d2T/dz2 = (E/kappa) dT/dz,  T(0) = Ts,  T(L) = Tm")
    print("  whose solution is")
    print("     T(z) = Ts + (Tm - Ts)(1 - exp(-Pe z/L))/(1 - exp(-Pe)),")
    print("     Pe = E L / kappa  (a Peclet number).\n")
    print(f"  kappa = {KAPPA:.1e} m^2/s = {KAPPA_YR:.1f} m^2/yr, "
          f"L = {L_KM:.0f} km")
    print(f"  Ts = {T_SURFACE:.0f} C, Tm = {T_MANTLE:.0f} C\n")
    print("   E (mm/yr)   Pe      T at 10 km   T at 20 km   T at 30 km   "
          "surface gradient (C/km)")
    for e in (0.0, 0.1, 0.5, 1.0, 2.0, 5.0):
        pe = (e * 1e-3) * (L_KM * 1e3) / KAPPA_YR
        grad = (float(geotherm(0.5, e)) - T_SURFACE) / 0.5
        print(f"   {e:9.1f}   {pe:6.3f}   {float(geotherm(10.0, e)):11.1f}   "
              f"{float(geotherm(20.0, e)):11.1f}   {float(geotherm(30.0, e)):11.1f}"
              f"   {grad:20.1f}")
    print("\n  the geothermal gradient steepens with exhumation: fast exhumation")
    print("  brings hot rock upward, so a given isotherm sits shallower than it")
    print("  would in a purely conductive column.")


def demonstration_2():
    section("2. Closure depth and apparent age")
    print(f"  A thermochronometer with closure temperature {T_CLOSURE:.0f} C records")
    print("  the time at which the rock passed through that isotherm.  In a steady")
    print("  exhumation state the apparent age is simply z_c/E.\n")
    print("   E (mm/yr)   z_c (km)   z_c/E (Ma)   mean cooling rate (C/Ma)")
    for e in (0.05, 0.1, 0.2, 0.5, 1.0, 2.0):
        zc = closure_depth_km(e)
        age = (zc * 1e3) / (e * 1e-3) / 1e6
        rate = (T_CLOSURE - T_SURFACE) / (age * 1e6) * 1e6
        print(f"   {e:9.2f}   {zc:9.2f}   {age:11.2f}   {rate:21.1f}")
    print(" \n  the apparent age is inversely proportional to the exhumation rate")
    print("  and proportional to the closure depth, and both the closure depth and")
    print("  the age depend on the exhumation rate itself: the pair (z_c, E) is")
    print("  what a single age measures, and a single age cannot separate them.")


def demonstration_3():
    section("3. Age against elevation: recovering the exhumation rate")
    print("  In steady state, distance below the closure isotherm maps linearly")
    print("  onto time, so the apparent age at an elevation is")
    print("     t(z) = z / E")
    print("  with z measured down from the closure isotherm; the slope of the")
    print("  age-elevation line is 1/E.\n")
    print("   E (mm/yr)   slope from a fit (Ma/km)   1/E (Ma/km)   ratio")
    for e in (0.1, 0.25, 0.5, 1.0):
        zs = np.linspace(0.0, 3.0, 7)                 # km below the closure
        ages = zs * 1e3 / (e * 1e-3) / 1e6            # Ma
        slope = np.polyfit(zs, ages, 1)[0]
        print(f"   {e:9.2f}   {slope:22.4f}   {1.0 / e:10.4f}   "
              f"{slope / (1.0 / e):7.4f}")
    print("\n  the ratio is exactly 1 in every row: with a steady state and a")
    print("  uniform exhumation rate the age-elevation slope is an exact")
    print("  measurement of 1/E, and the closure temperature cancels.  That")
    print("  cancellation is why age-elevation plots are used at all.")
    print("\n  sensitivity to the closure temperature, at fixed E = 0.5 mm/yr:")
    print("    Tc (C)   z_c (km)   apparent age of a sample that now sits")
    print("                      2 km above the closure depth (Ma)")
    for tc in (120.0, 200.0, 300.0):
        zc = closure_depth_km(0.5, tc)
        age = (zc - 2.0) * 1e3 / (0.5 * 1e-3) / 1e6
        print(f"    {tc:6.0f}   {zc:9.2f}   {age:44.2f}")
    print("  the absolute age moves a lot with Tc while the slope does not: the")
    print("  slope measures a rate, the intercept measures a depth, and only the")
    print("  rate is independent of the closure temperature.")


def demonstration_4():
    section("4. The bias from a transient exhumation history")
    print("  History: E = 0.2 mm/yr from 20 Ma to 5 Ma, then 1.0 mm/yr from 5 Ma")
    print("  to the present, with the closure isotherm at a fixed depth.  The age")
    print("  of a sample at depth z is obtained by integrating dz/dt = E(t).\n")
    e1, e2, t_switch = 0.2, 1.0, 5.0
    z_at_switch = e1 * 1e-3 * t_switch * 1e6       # m exhumed in phase 1
    print("   elevation above reference (km)   true age (Ma)   "
          "steady-state age for E = 1.0 (Ma)")
    zs = np.linspace(0.0, 4.0, 5)
    ages = []
    for z_km in zs:
        z_m = z_km * 1e3
        if z_m <= z_at_switch:
            age = z_m / (e2 * 1e-3) / 1e6
        else:
            age = t_switch + (z_m - z_at_switch) / (e1 * 1e-3) / 1e6
        ages.append(age)
        print(f"   {z_km:28.1f}   {age:14.2f}   {z_km / e2:27.2f}")
    ages = np.array(ages)
    slope_low = np.polyfit(zs[:2], ages[:2], 1)[0]
    slope_high = np.polyfit(zs[-2:], ages[-2:], 1)[0]
    print(f"\n  fitted slope over the lower 1 km: {slope_low:.3f} Ma/km "
          f"-> apparent E = {1.0 / slope_low:.3f} mm/yr")
    print(f"  fitted slope over the upper 1 km: {slope_high:.3f} Ma/km "
          f"-> apparent E = {1.0 / slope_high:.3f} mm/yr")
    print(f"  the true rates are {e1:.1f} and {e2:.1f} mm/yr.")
    print("  The samples closest to the surface (lowest elevation above the")
    print("  reference) record the present, faster rate; the older, higher")
    print("  samples record the earlier, slower one.  A single age-elevation")
    print("  slope is a measurement of the rate averaged over the time span of")
    print("  the ages, not of the present rate, and a change of rate appears as a")
    print("  break in slope that has to be resolved to be avoided.")


def demonstration_5():
    section("5. The topographic perturbation of the closure isotherm")
    print("  A sinusoidal surface topography of amplitude A and wavelength lambda")
    print("  imposes a sinusoidal temperature on the surface of a half-space, so")
    print("  the perturbation at depth z is")
    print("     dT(z) = A * (dT/dz)_lapse * exp(-k z) cos(k x),  k = 2 pi/lambda,")
    print("  if the surface temperature follows the topography with the lapse rate")
    print("  (dT/dz)_lapse.  The closure isotherm is displaced by")
    print("  dT/(geothermal gradient), which the rock then records as an age shift.\n")
    print("  lapse rate used: 6.0 C/km (a chosen value)")
    lapse = 6.0e-3                     # C per m
    e = 0.5                            # mm/yr
    zc = closure_depth_km(e)
    grad = (float(geotherm(zc + 0.5, e)) - float(geotherm(zc - 0.5, e))) / 1.0
    print(f"  E = {e:.2f} mm/yr, closure depth = {zc:.2f} km, local geothermal")
    print(f"  gradient at that depth = {grad:.2f} C/km\n")
    print("   wavelength (km)   amplitude (km)   closure-depth shift (m)   "
          "age shift (Ma)")
    for lam_km, amp_km in ((10.0, 1.0), (20.0, 1.0), (50.0, 1.0), (20.0, 2.0)):
        k = 2.0 * np.pi / (lam_km * 1e3)
        dT = amp_km * 1e3 * lapse * np.exp(-k * zc * 1e3)     # deg C
        dz = dT / (grad / 1e3)                                # m
        age_shift = dz / (e * 1e-3) / 1e6                     # Ma
        print(f"   {lam_km:15.0f}   {amp_km:14.1f}   {dz:23.1f}   "
              f"{age_shift:13.4f}")
    print("\n  the perturbation decays exponentially with the ratio of the closure")
    print("  depth to the topographic wavelength, so short-wavelength topography")
    print("  produces almost no bias while long-wavelength relief does.  A")
    print("  sample collected in a valley is then older or younger than one on a")
    print("  ridge by the age shift above, which is a bias in the age-elevation")
    print("  slope unless it is modelled.")


def main():
    demonstration_1()
    demonstration_2()
    demonstration_3()
    demonstration_4()
    demonstration_5()
    print("\nAll results above are SYNTHETIC teaching computations.")


if __name__ == "__main__":
    main()
