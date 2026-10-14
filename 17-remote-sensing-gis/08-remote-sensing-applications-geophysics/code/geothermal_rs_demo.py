#!/usr/bin/env python3
"""Thermal remote sensing for geothermal systems: Planck radiance, brightness
temperature, the emissivity error, a conductive surface anomaly, and the
detection limit.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geothermal_rs_demo.py

Physical constants used (CODATA 2018, exact by definition of the SI):
h = 6.62607015e-34 J s, c = 2.99792458e8 m/s, k = 1.380649e-23 J/K.
Everything else is SYNTHETIC: the band, the noise, the conductivities and the
heat fluxes are chosen teaching values, not measurements of a real field.  No
file is read or written and no network access is used.

Contents
--------
1. Planck radiance at a thermal band and the exact inverse for temperature.
2. Emissivity: the largest single error in a land-surface temperature.
3. A subsurface heat flux and the surface temperature anomaly it sustains.
4. The detection limit, and what it demands of the emissivity.
5. Diurnal amplitude and thermal inertia.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

H_PLANCK = 6.62607015e-34   # J s
C_LIGHT = 2.99792458e8      # m/s
K_BOLTZ = 1.380649e-23      # J/K
LAMBDA = 11.0e-6            # band centre, m (SYNTHETIC)
NE_DT = 0.20                # noise-equivalent temperature difference, K


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def planck(T, lam=LAMBDA):
    """Spectral radiance of a blackbody, W m^-2 sr^-1 m^-1."""
    a = 2.0 * H_PLANCK * C_LIGHT ** 2 / lam ** 5
    b = H_PLANCK * C_LIGHT / (lam * K_BOLTZ * np.asarray(T, dtype=float))
    return a / np.expm1(b)


def invert_planck(L, lam=LAMBDA):
    """Brightness temperature (K) from spectral radiance; exact inverse."""
    a = 2.0 * H_PLANCK * C_LIGHT ** 2 / lam ** 5
    return H_PLANCK * C_LIGHT / (lam * K_BOLTZ * np.log(a / np.asarray(L, float) + 1.0))


def main():
    section("1. Planck radiance and its inverse (SYNTHETIC band)")
    print(f"band centre = {LAMBDA * 1e6:.1f} um")
    for T in (280.0, 300.0, 320.0):
        L = planck(T)
        print(f"  T = {T:.0f} K -> L = {L:.4f} W m^-2 sr^-1 m^-1 "
              f"-> inverse gives {invert_planck(L):.3f} K")
    print(f"dL/dT near 300 K = {(planck(300.5) - planck(299.5)):.4f} "
          f"W m^-2 sr^-1 m^-1 per K")
    print("Radiance is what the sensor measures; temperature is the inverse.")
    print("The inverse is exact, but only for a blackbody.")

    section("2. Emissivity is the dominant error (SYNTHETIC)")
    T_true = 300.0
    print(f"ground temperature (truth) = {T_true:.1f} K")
    print("  emissivity   apparent T (K)   error (K)")
    for eps in (1.00, 0.98, 0.95, 0.90, 0.85):
        L_obs = eps * planck(T_true)
        T_app = float(invert_planck(L_obs))
        print(f"  {eps:11.2f}   {T_app:14.2f}   {T_app - T_true:+8.2f}")
    print("Assuming a blackbody (emissivity 1) when the surface emits at 0.95")
    print("understates the temperature by several kelvin -- far more than the")
    print("instrument noise. Emissivity must be modelled, not assumed.")

    section("3. A subsurface heat flux and the surface anomaly (SYNTHETIC)")
    k_rock = 2.0        # thermal conductivity, W m^-1 K^-1 (SYNTHETIC)
    z_cond = 20.0       # depth over which the anomaly conducts, m
    print(f"thermal conductivity = {k_rock:.1f} W m^-1 K^-1, conduction depth "
          f"= {z_cond:.0f} m")
    print("  heat flux (W/m^2)   gradient (mK/m)   surface anomaly (K)")
    for q in (0.05, 0.10, 0.20, 0.40):
        grad = q / k_rock * 1000.0
        dT = q * z_cond / k_rock
        print(f"  {q:17.2f}   {grad:14.1f}   {dT:18.2f}")
    print("A modest geothermal flux produces a surface warming of a few tenths")
    print("to a couple of kelvin -- the same order as the emissivity error.")

    section("4. The detection limit and what it demands of the emissivity")
    q_detect = NE_DT * k_rock / z_cond
    print(f"instrument NE(dT) = {NE_DT:.2f} K")
    print(f"surface anomaly per 0.10 W m^-2 = {0.10 * z_cond / k_rock:.2f} K")
    print(f"smallest flux detectable on noise alone = {q_detect:.3f} W m^-2")
    eps_err = 0.02
    dT_eps = float(invert_planck((1.0 - eps_err) * planck(T_true))) - T_true
    print(f"a {eps_err:.2f} emissivity error alone moves T by {dT_eps:+.2f} K")
    print(f"it would take a flux of {abs(dT_eps) * k_rock / z_cond:.3f} W m^-2 to")
    print("produce that shift. The detection limit is set by the radiative")
    print("model, not by the detector.")

    section("5. Diurnal amplitude and thermal inertia (SYNTHETIC)")
    A0 = 12.0           # diurnal amplitude at unit thermal inertia, K (SYNTHETIC)
    B0 = 4.0            # seasonal amplitude at unit thermal inertia, K
    print("  thermal inertia   diurnal amplitude (K)   seasonal amplitude (K)")
    for inertia in (500.0, 1000.0, 2000.0, 4000.0):
        diurnal = A0 / np.sqrt(inertia / 1000.0)
        seasonal = B0 / np.sqrt(inertia / 1000.0)
        print(f"  {inertia:15.0f}   {diurnal:21.2f}   {seasonal:22.2f}")
    print("Both amplitudes fall as the inverse square root of thermal inertia, so")
    print("low inertia (dry, rocky) swings hard and high inertia (wet, vegetated)")
    print("is damped. A geothermal anomaly is easiest to see in the diurnal")
    print("difference, where the static ground temperature cancels.")


if __name__ == "__main__":
    main()
