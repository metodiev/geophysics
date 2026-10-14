#!/usr/bin/env python3
"""Temperature, pressure and frequency dependence of electrical conductivity.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python temperature_and_pressure_effects_demo.py

Everything is SYNTHETIC.  The activation energy, the freezing-point model, the
compaction law and the Debye parameters are chosen teaching values, not
measurements.  The Boltzmann constant and the permittivity of free space are
exact SI-defined constants.

Contents
--------
1. Arrhenius temperature dependence, and the linear coefficient it implies.
2. Where the linear approximation breaks down.
3. Freezing: a synthetic unfrozen-water model and the conductivity collapse.
4. Compaction: porosity, formation factor and conductivity versus depth.
5. Frequency: charge relaxation versus polarisation relaxation.
6. Consistency checks.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Exact SI-defined constants ---------------------------------------------
K_BOLTZMANN_EV = 8.617333262e-5      # eV/K
EPS0 = 8.8541878128e-12              # F/m, permittivity of free space

# --- SYNTHETIC teaching parameters ------------------------------------------
EA_EV = 0.20             # eV, activation energy of ionic conduction (teaching)
SIGMA_REF = 0.10         # S/m at T_REF (teaching value)
T_REF_C = 25.0
T_REF = T_REF_C + 273.15

PHI0 = 0.40              # surface porosity of the compaction model
Z_C = 1500.0             # m, compaction length scale
RHO_BULK = 2.30e3        # kg/m^3
RHO_WATER = 1.00e3       # kg/m^3
G = 9.81                 # m/s^2
SIGMA_W_PORE = 0.20      # S/m, synthetic pore-water conductivity
M_ARCHIE = 2.0

EPS_R = 10.0             # relative permittivity of the rock (teaching value)
SIGMA_DEBYE_0 = 0.050    # S/m
SIGMA_DEBYE_INF = 0.060  # S/m
F_C = 1.0                # Hz


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def sigma_arrhenius(T_c, ea=EA_EV, sigma_ref=SIGMA_REF):
    """sigma(T) = sigma_ref exp(-(Ea/k)(1/T - 1/T_ref)), T in Celsius."""
    T = np.asarray(T_c, dtype=float) + 273.15
    return sigma_ref * np.exp(-(ea / K_BOLTZMANN_EV) * (1.0 / T - 1.0 / T_REF))


def main():
    section("1. Arrhenius temperature dependence")
    alpha = EA_EV / (K_BOLTZMANN_EV * T_REF ** 2)
    print(f"  SYNTHETIC model: Ea = {EA_EV:.3f} eV, sigma(25 C) = "
          f"{SIGMA_REF:.3f} S/m")
    print(f"  sigma(T) = sigma_ref exp(-(Ea/k)(1/T - 1/T_ref)), "
          f"k = {K_BOLTZMANN_EV:.6e} eV/K")
    print(f"  the Arrhenius form implies a relative coefficient")
    print(f"    alpha = Ea/(k T^2) = {alpha:.6f} per K at T_ref = {T_REF:.2f} K")
    print("   T (C)   sigma (S/m)   linear sigma_ref(1+alpha dT)   rel. error")
    lo_err = hi_err = 0.0
    for T_c in (5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0):
        s = sigma_arrhenius(T_c)
        lin = SIGMA_REF * (1.0 + alpha * (T_c - T_REF_C))
        err = (lin - s) / s
        if T_c < T_REF_C:
            lo_err = max(lo_err, abs(err))
        else:
            hi_err = max(hi_err, abs(err))
        print(f"  {T_c:6.1f} {s:12.6f} {lin:27.6f} {err * 100:14.3f}%")
    print(f"  worst linearisation error below 25 C: {lo_err * 100:.2f}%")
    print(f"  worst linearisation error above 25 C: {hi_err * 100:.2f}%")

    section("2. Activation energy controls the temperature coefficient")
    print("  alpha = Ea/(k T^2) at 25 C, and the conductivity ratio 5 -> 60 C:")
    print("     Ea (eV)   alpha (1/K)   sigma(60 C)/sigma(5 C)")
    for ea in (0.10, 0.15, 0.20, 0.30, 0.50):
        a = ea / (K_BOLTZMANN_EV * T_REF ** 2)
        ratio = sigma_arrhenius(60.0, ea) / sigma_arrhenius(5.0, ea)
        print(f"  {ea:10.2f} {a:13.6f} {ratio:24.3f}")
    print("  an activation energy is not a fitted convenience: it sets both the")
    print("  coefficient and its change over the working range.")

    section("3. Freezing: a synthetic unfrozen-water model")
    print("  SYNTHETIC teaching model: unfrozen water fraction")
    print("    w(T) = 1/(1 + (T_f - T)/dT) for T < T_f, T_f = 0 C, dT = 1.0 C")
    print("    sigma(T) = sigma_w(T) * w(T) / F  (pore-scale mixing ignored)")
    print("   T (C)    w(T)      sigma (S/m)   rho (ohm m)")
    for T_c in (2.0, 0.5, 0.0, -0.5, -1.0, -2.0, -5.0, -10.0):
        if T_c >= 0.0:
            w = 1.0
        else:
            w = 1.0 / (1.0 + (0.0 - T_c) / 1.0)
        sigma = sigma_arrhenius(max(T_c, 0.0)) * w / (0.25 ** -M_ARCHIE)
        print(f"  {T_c:7.1f} {w:9.4f} {sigma:13.6f} {1.0 / sigma:13.2f}")
    print("  sigma at -10 C is 11x lower than at 0 C, over 10 K, while 25 K of")
    print("  warming gives only 3.3x: phase change, not mobility, dominates the")
    print("  cold end of the range.")

    section("4. Compaction: porosity, formation factor and conductivity")
    print(f"  SYNTHETIC compaction law: phi(z) = phi0 exp(-z/z_c), "
          f"phi0 = {PHI0:.2f}, z_c = {Z_C:.0f} m")
    print(f"  Archie with m = {M_ARCHIE:.1f}, sigma_w = {SIGMA_W_PORE:.2f} S/m")
    print("     z (m)    phi     F = phi^-m   sigma (S/m)   rho (ohm m)   "
          "P_eff (MPa)")
    for z in (0.0, 100.0, 250.0, 500.0, 1000.0, 2000.0, 3000.0):
        phi = PHI0 * np.exp(-z / Z_C)
        F = phi ** (-M_ARCHIE)
        sigma = SIGMA_W_PORE / F
        p_eff = (RHO_BULK - RHO_WATER) * G * z / 1e6
        print(f"  {z:8.0f} {phi:7.4f} {F:12.3f} {sigma:13.5f} {1 / sigma:13.3f} "
              f"{p_eff:14.3f}")
    z_half = Z_C * np.log(2.0)
    p_half = (RHO_BULK - RHO_WATER) * G * z_half / 1e6
    print(f"\n  porosity falls to half of phi0 at z = z_c ln 2 = {z_half:.1f} m")
    print(f"  which is an effective pressure of {p_half:.3f} MPa "
          f"(compressional: rho_b - rho_w = "
          f"{(RHO_BULK - RHO_WATER):.0f} kg/m^3)")
    print("  porosity loss raises F, so the formation gets MORE resistive with")
    print("  depth under this model; a salinity increase with depth opposes it.")

    section("5. Frequency: two very different limits")
    sigma_rock = 0.10
    eps = EPS_R * EPS0
    tau_charge = eps / sigma_rock
    f_charge = 1.0 / (2.0 * np.pi * tau_charge)
    print(f"  charge relaxation of a conductive rock (Maxwell time tau = eps/sigma):")
    print(f"    eps = eps_r eps_0 = {EPS_R:.1f} x {EPS0:.4e} = {eps:.4e} F/m")
    print(f"    sigma = {sigma_rock:.2f} S/m -> tau = {tau_charge:.4e} s")
    print(f"    f_charge = 1/(2 pi tau) = {f_charge:.4e} Hz "
          f"({f_charge / 1e6:.3f} MHz)")
    print("    below this frequency the fields are diffusive and DC theory")
    print("    applies; standard resistivity frequencies are many decades below.")
    tau_pol = 1.0 / (2.0 * np.pi * F_C)
    print(f"\n  polarisation relaxation (SYNTHETIC Debye, f_c = {F_C:.1f} Hz):")
    print(f"    tau = {tau_pol:.4e} s")
    print("      f (Hz)   |sigma| (S/m)   phase (mrad)")
    for f in (1e-3, 1e-1, F_C, 10.0, 1e3, 1e5):
        w = 2.0 * np.pi * f
        s_complex = SIGMA_DEBYE_INF - (SIGMA_DEBYE_INF - SIGMA_DEBYE_0) / (
            1.0 + 1j * w * tau_pol)
        print(f"  {f:10.4g} {abs(s_complex):14.6f} {np.angle(s_complex) * 1e3:15.4f}")
    print(f"  the two limits differ by a factor "
          f"{f_charge / F_C:.3e}: 'DC' for a resistivity survey is not 'DC'")
    print("  for a polarisation measurement, and the temperature dependence of")
    print("  tau is what makes IP a permafrost thermometer.")

    section("6. Consistency checks")
    s_ref = sigma_arrhenius(T_REF_C)
    print(f"  Arrhenius at T_ref returns {s_ref:.12f} S/m (model "
          f"{SIGMA_REF:.12f})")
    print(f"  linear form at T_ref returns "
          f"{SIGMA_REF * (1 + alpha * 0.0):.12f} S/m")
    z_fit = Z_C * np.log(2.0)
    phi_at = PHI0 * np.exp(-z_fit / Z_C)
    print(f"  phi(z_c ln 2) = {phi_at:.12f} (half of phi0 = {PHI0 / 2:.12f})")
    print(f"  tau_charge * sigma/eps = {tau_charge * sigma_rock / eps:.12f}")


if __name__ == "__main__":
    main()
