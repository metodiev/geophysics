#!/usr/bin/env python3
"""Palaeoclimate proxies: water-isotope fractionation during Rayleigh
distillation, the temperature sensitivity of the proxy, and the degeneracy
between temperature and source composition.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python paleoclimate_proxies_demo.py

All models and data in this file are SYNTHETIC.  The fractionation factor is a
chosen function of temperature, not a measured calibration, and no ice-core
record or published slope is quoted.  The physical constants in the
Clausius-Clapeyron expression are standard and are stated in the code.

Contents
--------
1. Rayleigh distillation: the isotope ratio of the remaining vapour and of the
   instantaneous condensate as a function of the remaining vapour fraction.
2. A cooling parcel: linking the remaining fraction to temperature through a
   Clausius-Clapeyron saturation curve, and measuring d(delta)/dT.
3. Structural uncertainty: the same delta values under two different
   fractionation parameterisations imply different temperatures.
4. Degeneracy: one measured delta is consistent with a family of
   (source composition, condensation temperature) pairs.
"""

import numpy as np
from scipy.optimize import brentq

RNG = np.random.default_rng(20261014)

# --- standard physical constants --------------------------------------------
LATENT_HEAT_VAPORISATION_J_KG = 2.501e6    # J kg^-1 at 0 degC (standard value)
RV_WATER_J_KG_K = 461.5                    # J kg^-1 K^-1 (standard value)
REFERENCE_TEMPERATURE_K = 288.15           # K, chosen reference state

# --- SYNTHETIC teaching parameters ------------------------------------------
FRACTIONATION_SCALE_A = 9.0e-3    # alpha = 1 + a*(T_ref/T)^2
FRACTIONATION_SCALE_B = 13.0e-3   # alternative parameterisation (structural test)
SOURCE_DELTA_PER_MIL = -12.0      # delta of the initial vapour, per mil (chosen)
T_START_K = 292.0                 # starting temperature of the parcel, K
T_END_K = 250.0                   # final temperature, K


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def fractionation_alpha(temperature_k, scale):
    """Synthetic equilibrium fractionation factor alpha = R_condensate/R_vapour."""
    return 1.0 + scale * (REFERENCE_TEMPERATURE_K / temperature_k) ** 2


def saturation_mixing_ratio(temperature_k):
    """Clausius-Clapeyron saturation mixing ratio shape, arbitrary units.

    q_s(T) is proportional to exp(-L/Rv (1/T - 1/T_ref)).  The constant of
    proportionality cancels in the ratio used below, so it is set to 1.
    """
    exponent = -(LATENT_HEAT_VAPORISATION_J_KG / RV_WATER_J_KG_K) * (
        1.0 / temperature_k - 1.0 / REFERENCE_TEMPERATURE_K)
    return np.exp(exponent)


def rayleigh_vapour(delta_0, f, alpha):
    """delta of the remaining vapour after a fraction 1-f has condensed."""
    return (delta_0 + 1000.0) * f ** (alpha - 1.0) - 1000.0


def rayleigh_condensate(delta_0, f, alpha):
    """delta of the instantaneous condensate (equilibrium with the vapour)."""
    return alpha * (delta_0 + 1000.0) * f ** (alpha - 1.0) - 1000.0


def main():
    section("1. Rayleigh distillation at fixed temperature")
    alpha_fixed = fractionation_alpha(280.0, FRACTIONATION_SCALE_A)
    print(f"  initial vapour delta_0 = {SOURCE_DELTA_PER_MIL:+.1f} per mil")
    print(f"  alpha(T = 280 K) = {alpha_fixed:.5f} "
          f"(synthetic: alpha = 1 + {FRACTIONATION_SCALE_A:.4f}*(T_ref/T)^2)")
    print(f"  {'f remaining':>12s} {'delta vapour':>14s} {'delta condensate':>18s}")
    for f in (1.0, 0.8, 0.6, 0.4, 0.2, 0.1):
        dv = rayleigh_vapour(SOURCE_DELTA_PER_MIL, f, alpha_fixed)
        dc = rayleigh_condensate(SOURCE_DELTA_PER_MIL, f, alpha_fixed)
        print(f"  {f:12.2f} {dv:14.3f} {dc:18.3f}")
    print("  Units: delta is a relative isotope ratio in parts per thousand (per")
    print("  mil). Both reservoirs become more negative as the heavy isotope is")
    print("  preferentially removed into the condensate. This is the physical")
    print("  reason a cold site records a more negative isotope value.")

    section("2. A cooling parcel: linking f to temperature")
    temperatures = np.linspace(T_START_K, T_END_K, 200)
    remaining = saturation_mixing_ratio(temperatures) / saturation_mixing_ratio(T_START_K)
    deltas = np.array([
        rayleigh_condensate(SOURCE_DELTA_PER_MIL, f,
                            fractionation_alpha(t, FRACTIONATION_SCALE_A))
        for t, f in zip(temperatures, remaining)])
    slope, intercept = np.polyfit(temperatures, deltas, 1)
    print(f"  parcel cools from {T_START_K:.1f} K to {T_END_K:.1f} K")
    print(f"  remaining vapour fraction falls from {remaining[0]:.3f} to "
          f"{remaining[-1]:.3f}")
    print(f"  {'T (K)':>7s} {'T (degC)':>9s} {'f':>7s} {'delta condensate':>18s}")
    for index in (0, 40, 80, 120, 160, 199):
        print(f"  {temperatures[index]:7.1f} {temperatures[index] - 273.15:9.2f} "
              f"{remaining[index]:7.3f} {deltas[index]:18.3f}")
    print(f"  least-squares slope d(delta)/dT = {slope:.4f} per mil per K")
    print(f"  over this range, i.e. about {-slope:.3f} per mil per K of cooling.")
    print("  The slope is not a constant of nature: it depends on alpha(T), on the")
    print("  condensation path and on the initial vapour. It is a property of the")
    print("  model, which is why proxy calibrations are site-specific.")

    section("3. Structural uncertainty of the calibration")
    deltas_b = np.array([
        rayleigh_condensate(SOURCE_DELTA_PER_MIL, f,
                            fractionation_alpha(t, FRACTIONATION_SCALE_B))
        for t, f in zip(temperatures, remaining)])
    slope_alt, intercept_alt = np.polyfit(temperatures, deltas_b, 1)
    print(f"  alpha parameterisation A (scale {FRACTIONATION_SCALE_A:.4f}): "
          f"slope = {slope:.4f} per mil per K")
    print(f"  alpha parameterisation B (scale {FRACTIONATION_SCALE_B:.4f}): "
          f"slope = {slope_alt:.4f} per mil per K")
    print(f"  ratio B/A = {slope_alt / slope:.4f}")
    measured_delta = -25.0
    t_a_kelvin = (measured_delta - intercept) / slope
    t_b_kelvin = (measured_delta - intercept_alt) / slope_alt
    print(f"  a measured delta of {measured_delta:.1f} per mil implies:")
    print(f"    T = {t_a_kelvin - 273.15:.2f} degC under parameterisation A")
    print(f"    T = {t_b_kelvin - 273.15:.2f} degC under parameterisation B")
    print(f"    disagreement = {abs(t_a_kelvin - t_b_kelvin):.2f} K")
    print("  Both calibrations are internally consistent. The disagreement is")
    print("  structural uncertainty in the fractionation physics, which no amount")
    print("  of extra sampling of the same proxy removes.")

    section("4. Degeneracy between source composition and temperature")
    alpha_280 = fractionation_alpha(280.0, FRACTIONATION_SCALE_A)
    target = -30.0
    print(f"  fix the observed condensate at delta = {target:+.1f} per mil and")
    print("  solve for the pairs (delta_0, T) that reproduce it, using the")
    print("  fixed-alpha distillation at the parcel's final fraction.")
    print(f"  {'delta_0 (per mil)':>18s} {'required alpha':>15s} "
          f"{'implied T (K)':>14s} {'implied T (degC)':>17s}")
    f_end = float(remaining[-1])
    solutions = []
    for delta_0 in (-8.0, -10.0, -12.0, -14.0, -16.0):
        def residual(a, delta_0=delta_0):
            return rayleigh_condensate(delta_0, f_end, a) - target
        alpha_solution = brentq(residual, 1.0, 1.05)
        # invert alpha(T): alpha = 1 + s*(Tref/T)^2  ->  T = Tref*sqrt(s/(alpha-1))
        t_implied = REFERENCE_TEMPERATURE_K * np.sqrt(
            FRACTIONATION_SCALE_A / (alpha_solution - 1.0))
        solutions.append((delta_0, alpha_solution, t_implied))
        print(f"  {delta_0:18.1f} {alpha_solution:15.5f} "
              f"{t_implied:14.2f} {t_implied - 273.15:17.2f}")
    spread = max(s[2] for s in solutions) - min(s[2] for s in solutions)
    per_mil = spread / 8.0
    print(f"  spread of implied temperature across the assumed source values = "
          f"{spread:.2f} K")
    print(f"  sensitivity: about {per_mil:.2f} K of implied temperature per 1 per")
    print("  mil of uncertainty in the source composition (in this synthetic model).")
    print("  A single isotope value therefore constrains a curve in")
    print("  (delta_0, T) space, not a temperature. Independent information about")
    print("  the source, or an independent temperature proxy, is required to pick a")
    print("  point. This is the same non-uniqueness structure as any underdetermined")
    print("  inverse problem.")


if __name__ == "__main__":
    main()
