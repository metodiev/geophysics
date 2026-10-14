#!/usr/bin/env python3
"""Climate-model hierarchy: a zero-dimensional energy-balance model, a
latitudinally resolved one-dimensional energy-balance model, and a measurement
of what each level of the hierarchy adds and what it still leaves out.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_model_hierarchy_demo.py

All models and data in this file are SYNTHETIC teaching models.  The parameters
are chosen to make the arithmetic transparent; they are not fitted to
observations.  The only measured constants used are the solar constant and the
Stefan-Boltzmann constant, both stated explicitly in the code.

Contents
--------
1. Zero-dimensional EBM: effective radiating temperature of a bare blackbody.
2. Zero-dimensional EBM with a linear outgoing-longwave-radiation (OLR) law:
   equilibrium warming and the e-folding (relaxation) time.
3. One-dimensional EBM on x = sin(latitude): steady state, gradient, and the
   conservation check that a globally uniform albedo reproduces the 0-D mean.
4. Ice-albedo feedback in the 1-D model, and a comparison of the hierarchy.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- measured / standard constants (stated, not fitted) ----------------------
SOLAR_CONSTANT_W_M2 = 1361.0         # total solar irradiance, W m^-2 (standard value)
STEFAN_BOLTZMANN = 5.670374419e-8    # W m^-2 K^-4 (exact SI definition)
SECONDS_PER_YEAR = 3.15576e7         # s, Julian year

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
PLANETARY_ALBEDO = 0.30              # globally uniform albedo, dimensionless
OLR_A_W_M2 = 210.0                   # OLR = A + B*T, W m^-2
OLR_B_W_M2_K = 2.0                   # OLR slope, W m^-2 K^-1
HEAT_CAPACITY_W_YR_M2_K = 5.0        # effective heat capacity, W yr m^-2 K^-1
STEP_FORCING_W_M2 = 3.7              # synthetic step forcing, W m^-2
DIFFUSIVITY_W_M2_K = 0.6             # 1-D EBM diffusivity, W m^-2 K^-1
ALBEDO_ICE = 0.62                    # albedo of an ice-covered point
ALBEDO_OPEN = 0.30                   # albedo of an ice-free point
ICE_THRESHOLD_K = 263.15             # ice appears below this T, K (chosen)
N_LAT = 73                           # latitude points from -90 to +90 degrees


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def olr(t_celsius):
    """Linear outgoing longwave radiation law, W m^-2, from a surface temperature."""
    return OLR_A_W_M2 + OLR_B_W_M2_K * t_celsius


def effective_radiating_temperature():
    """Bare-blackbody planetary temperature: sigma T^4 = S(1-alpha)/4."""
    absorbed = SOLAR_CONSTANT_W_M2 * (1.0 - PLANETARY_ALBEDO) / 4.0
    return (absorbed / STEFAN_BOLTZMANN) ** 0.25, absorbed


def build_latitude_operator():
    """Discretise L[T] = d/dx[(1-x^2) dT/dx] on x = sin(latitude), zero flux at poles."""
    x = np.linspace(-1.0, 1.0, N_LAT)
    dx = x[1] - x[0]
    L = np.zeros((N_LAT, N_LAT))
    for i in range(N_LAT):
        if i == 0:
            x_half = 0.5 * (x[0] + x[1])
            coef = (1.0 - x_half ** 2) / dx ** 2
            L[i, i] = -coef
            L[i, i + 1] = coef
        elif i == N_LAT - 1:
            x_half = 0.5 * (x[-2] + x[-1])
            coef = (1.0 - x_half ** 2) / dx ** 2
            L[i, i] = -coef
            L[i, i - 1] = coef
        else:
            x_hi = 0.5 * (x[i] + x[i + 1])
            x_lo = 0.5 * (x[i - 1] + x[i])
            c_hi = (1.0 - x_hi ** 2) / dx ** 2
            c_lo = (1.0 - x_lo ** 2) / dx ** 2
            L[i, i] = -(c_hi + c_lo)
            L[i, i + 1] = c_hi
            L[i, i - 1] = c_lo
    return x, dx, L


def insolation_shape(x):
    """Synthetic insolation shape, normalised to unit global mean.

    The raw shape is S = 1 + k(1 - 3x^2), analytically of unit mean over
    x in [-1, 1].  It is renormalised on the grid so that the discrete mean is
    exactly 1, which makes the global-mean conservation check in section 3
    meaningful to round-off rather than to a quadrature error.
    """
    raw = 1.0 + 0.30 * (1.0 - 3.0 * x ** 2)
    return raw / raw.mean()


def run_one_dimensional(ice_feedback):
    """Time-step the 1-D EBM to steady state; return x, T (deg C) and history."""
    x, dx, L = build_latitude_operator()
    q0 = SOLAR_CONSTANT_W_M2 / 4.0
    s_shape = insolation_shape(x)
    t_c = np.full(N_LAT, 15.0)
    dt_yr = 0.05
    n_steps = 8000
    steps_done = 0
    for _ in range(n_steps):
        if ice_feedback:
            albedo = np.where(t_c < ICE_THRESHOLD_K - 273.15, ALBEDO_ICE, ALBEDO_OPEN)
        else:
            albedo = np.full(N_LAT, ALBEDO_OPEN)
        absorbed = q0 * s_shape * (1.0 - albedo)
        # implicit (backward Euler) step: (C/dt)(T_new - T_old) = D L T_new + absorbed - A - B T_new
        a = HEAT_CAPACITY_W_YR_M2_K / dt_yr
        mat = (a + OLR_B_W_M2_K) * np.eye(N_LAT) - DIFFUSIVITY_W_M2_K * L
        rhs = a * t_c + absorbed - OLR_A_W_M2
        t_new = np.linalg.solve(mat, rhs)
        change = np.max(np.abs(t_new - t_c))
        t_c = t_new
        steps_done += 1
        if change < 1e-9:
            break
    return x, t_c, steps_done * dt_yr


def main():
    section("1. Zero-dimensional EBM: bare blackbody temperature")
    t_eff, absorbed = effective_radiating_temperature()
    print(f"  solar constant S          = {SOLAR_CONSTANT_W_M2:.1f} W/m^2")
    print(f"  planetary albedo alpha    = {PLANETARY_ALBEDO:.2f}")
    print(f"  absorbed flux S(1-a)/4    = {absorbed:.2f} W/m^2")
    print(f"  Stefan-Boltzmann sigma    = {STEFAN_BOLTZMANN:.9e} W m^-2 K^-4")
    print(f"  effective radiating T     = {t_eff:.2f} K = {t_eff - 273.15:.2f} degC")
    print("  interpretation: this is the temperature of a blackbody that would emit")
    print("  the absorbed flux. It is a diagnostic definition, not a surface temperature.")

    section("2. Zero-dimensional EBM with linear OLR: equilibrium and timescale")
    equil = (absorbed - OLR_A_W_M2) / OLR_B_W_M2_K
    tau_yr = HEAT_CAPACITY_W_YR_M2_K / OLR_B_W_M2_K
    print(f"  OLR law: F_out = A + B*T with A = {OLR_A_W_M2:.1f} W/m^2, "
          f"B = {OLR_B_W_M2_K:.1f} W m^-2 K^-1")
    print(f"  equilibrium T0 = (absorbed - A)/B = {equil:.2f} degC")
    print(f"  e-folding time tau = C/B = {tau_yr:.2f} yr "
          f"(C = {HEAT_CAPACITY_W_YR_M2_K:.1f} W yr m^-2 K^-1)")
    warming = STEP_FORCING_W_M2 / OLR_B_W_M2_K
    print(f"  step forcing F = {STEP_FORCING_W_M2:.1f} W/m^2 -> equilibrium warming "
          f"dT = F/B = {warming:.2f} K")
    print("  time to reach 63.2% of the equilibrium response = tau above.")

    section("3. One-dimensional EBM: latitudinal profile (no ice feedback)")
    x, t_nofeedback, years = run_one_dimensional(ice_feedback=False)
    lat_deg = np.degrees(np.arcsin(x))
    weights = np.full(N_LAT, 1.0 / N_LAT)  # uniform in x = uniform area
    i_eq = int(np.argmin(np.abs(lat_deg)))
    print(f"  integrated to steady state in {years:.1f} model years")
    for name, la in (("equator", 0.0), ("30 N", 30.0), ("60 N", 60.0),
                     ("pole", 90.0), ("30 S", -30.0)):
        idx = int(np.argmin(np.abs(lat_deg - la)))
        print(f"  {name:>7s} (lat {lat_deg[idx]:+6.1f}) : T = {t_nofeedback[idx]:7.3f} degC")
    mean_1d = float(np.dot(weights, t_nofeedback))
    print(f"  area-weighted global mean     : T = {mean_1d:.3f} degC")
    print(f"  0-D prediction for the same albedo: T = {equil:.3f} degC")
    print(f"  difference (transport redistributes, it does not create heat): "
          f"{mean_1d - equil:+.4f} K")
    diff = t_nofeedback[i_eq] - t_nofeedback[-1]
    print(f"  equator-minus-pole contrast                = {diff:.3f} K")

    section("4. Ice-albedo feedback in the 1-D model")
    x2, t_ice, years_ice = run_one_dimensional(ice_feedback=True)
    print(f"  ice where T < {ICE_THRESHOLD_K - 273.15:.2f} degC; "
          f"albedo {ALBEDO_OPEN:.2f} -> {ALBEDO_ICE:.2f}")
    print(f"  integrated to steady state in {years_ice:.1f} model years")
    ice_points = int(np.sum(t_ice < ICE_THRESHOLD_K - 273.15))
    print(f"  ice-covered latitude points : {ice_points} of {N_LAT} "
          f"({100.0 * ice_points / N_LAT:.1f}%)")
    print(f"  area-weighted global mean   : T = {float(np.dot(weights, t_ice)):.3f} degC "
          f"(vs {mean_1d:.3f} degC without the feedback)")
    print(f"  equator T                   : {t_ice[i_eq]:.3f} degC")
    print(f"  north pole T                : {t_ice[-1]:.3f} degC")
    warmest = int(np.argmax(t_ice))
    print(f"  warmest point               : lat {lat_deg[warmest]:+.1f}, "
          f"T = {t_ice[warmest]:.3f} degC")
    print("  The feedback cools the planet by raising the albedo where ice exists;")
    print("  its strength depends on the chosen threshold and albedos, which are")
    print("  SYNTHETIC choices, so this number is illustrative, not a prediction.")

    section("5. What each level of the hierarchy can say")
    rows = [
        ("0-D blackbody", "1 number (T_eff)", "no transport, no OLR law, no albedo feedback"),
        ("0-D linear OLR", "1 number + timescale", "global mean only; no gradient"),
        ("1-D EBM (this file)", "profile T(lat)", "diffusion is a closure; no dynamics, no clouds"),
        ("GCM / ESM", "T(lat,lon,z,t)", "resolved dynamics; sub-grid processes parameterised"),
    ]
    print(f"  {'level':<20s} {'state':<22s} {'what is assumed or missing'}")
    for name, state, note in rows:
        print(f"  {name:<20s} {state:<22s} {note}")
    print("  Adding resolution adds state variables. Every level still contains")
    print("  closures whose parameters are choices, not measurements.")


if __name__ == "__main__":
    main()
