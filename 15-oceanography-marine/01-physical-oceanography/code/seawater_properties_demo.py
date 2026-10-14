#!/usr/bin/env python3
"""Seawater properties: a synthetic equation of state, sigma-t, cabbeling and
the buoyancy frequency.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seawater_properties_demo.py

Everything here is SYNTHETIC.  The equation of state below is a *teaching*
equation of state: its coefficients are chosen numbers, not measured
coefficients of real seawater.  No published data set, station or salinity
standard is reproduced.

Contents
--------
1. A linear (reference) equation of state and the sigma-t surface.
2. Compressibility: pressure vs depth, in-situ vs potential density.
3. Cabbeling: the density anomaly produced by mixing two water masses.
4. Buoyancy frequency N^2 from a synthetic temperature-salinity profile.
5. Sound speed from a chosen teaching formula.
6. Verification: linear versus nonlinear equation of state over a T-S box.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC equation-of-state constants (chosen, not measured) ------------
RHO0 = 1027.0        # kg/m^3, reference density at T0, S0, p = 0
T0, S0 = 10.0, 35.0  # degC, g/kg  (reference state)
ALPHA0 = 1.70e-4     # 1/degC, thermal expansion at T0
DALPHA = 1.50e-5     # 1/degC^2, curvature: alpha grows with T
BETA = 7.60e-4       # 1/(g/kg), haline contraction
KAPPA = 4.40e-6      # 1/dbar, compressibility

G = 9.81             # m/s^2, standard gravity
RHO_FRESH = 1000.0   # kg/m^3, reference density of fresh water (definition of sigma)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def alpha_of_T(T):
    """Thermal expansion coefficient, linear in T.  Units 1/degC."""
    return ALPHA0 + DALPHA * (T - T0)


def rho_linear(T, S, p_dbar=0.0):
    """Reference (linear) equation of state.  T in degC, S in g/kg, p in dbar."""
    return RHO0 * (1.0 - ALPHA0 * (T - T0) + BETA * (S - S0) + KAPPA * p_dbar)


def rho_nonlinear(T, S, p_dbar=0.0):
    """Nonlinear teaching EOS: same terms, but alpha depends on T.

    The integral of alpha(T) dT gives a quadratic term, which is what makes the
    rho(T,S) surface curved and produces cabbeling in section 3.
    """
    dT = T - T0
    # integral of -(ALPHA0 + DALPHA*(T-T0)) dT  from T0 to T
    therm = -(ALPHA0 * dT + 0.5 * DALPHA * dT ** 2)
    return RHO0 * (1.0 + therm + BETA * (S - S0) + KAPPA * p_dbar)


def sigma_t(T, S):
    """sigma-t = rho(S,T,0) - 1000, in kg/m^3."""
    return rho_linear(T, S, 0.0) - RHO_FRESH


def depth_to_pressure(z_m):
    """Teaching approximation p ~ rho0 g z, converted to dbar (1 dbar = 1e4 Pa)."""
    return RHO0 * G * z_m / 1.0e4


def sound_speed(T, S, z_m):
    """Chosen teaching formula for sound speed, m/s.  Not a published relation."""
    return (1449.0 + 4.6 * T - 0.055 * T ** 2
            + 1.34 * (S - 35.0) + 0.016 * z_m)


def main():
    section("1. Reference equation of state and the sigma-t surface")
    print(f"SYNTHETIC EOS: rho = rho0 [1 - alpha(T-T0) + beta(S-S0) + kappa p]")
    print(f"  rho0 = {RHO0:.1f} kg/m^3, T0 = {T0:.1f} degC, S0 = {S0:.1f} g/kg")
    print(f"  alpha = {ALPHA0:.2e} 1/degC, beta = {BETA:.2e} 1/(g/kg), "
          f"kappa = {KAPPA:.2e} 1/dbar")
    print("\n  sigma_t (kg/m^3) on a synthetic T-S grid:")
    Ts = (2.0, 10.0, 20.0, 28.0)
    Ss = (33.0, 34.0, 35.0, 36.0, 37.0)
    print("      S \\ T  " + "".join(f"{t:9.1f}" for t in Ts))
    for S in Ss:
        row = "".join(f"{sigma_t(T, S):9.2f}" for T in Ts)
        print(f"      {S:5.1f}  " + row)
    print("\n  d(sigma_t)/dS = "
          f"{(sigma_t(10.0, 35.05) - sigma_t(10.0, 34.95)) / 0.1:.3f} per (g/kg)  "
          "(haline)")
    print("  d(sigma_t)/dT = "
          f"{(sigma_t(10.05, 35.0) - sigma_t(9.95, 35.0)) / 0.1:.3f} per degC  "
          "(thermal)")
    print("  So a salinity change of 1 g/kg outweighs a temperature change of "
          f"{BETA / ALPHA0:.1f} degC.")

    section("2. Compressibility: in-situ versus potential density")
    print("  One water mass, T = 4.0 degC and S = 34.9 g/kg, at increasing depth.")
    print("\n  z (m)   p (dbar)   rho_insitu   rho_potential   compression term")
    for z in (0.0, 500.0, 1000.0, 2000.0, 4000.0, 6000.0):
        p = depth_to_pressure(z)
        T, S = 4.0, 34.9
        rho_i = rho_linear(T, S, p)
        rho_pot = rho_linear(T, S, 0.0)
        print(f"  {z:5.0f}   {p:8.0f}   {rho_i:10.3f}   {rho_pot:13.3f}   "
              f"{rho_i - rho_pot:14.3f}")
    p_at = depth_to_pressure(4000.0)
    d_rho = rho_linear(4.0, 34.9, p_at) - rho_linear(4.0, 34.9, 0.0)
    print(f"\n  at 4000 m (p = {p_at:.0f} dbar) compression adds "
          f"{d_rho:.3f} kg/m^3 = {100 * d_rho / RHO0:.2f}% of density.")
    print("  That is comparable to a cooling of "
          f"{d_rho / RHO0 / ALPHA0:.1f} degC: compression, not temperature,")
    print("  is the largest single control on in-situ density at depth.")
    print("  Stability must therefore be judged with POTENTIAL density "
          "(pressure removed).")

    section("3. Cabbeling: mixing two water masses of equal density")
    T1, S1 = 14.0, 35.50
    T2 = 2.0
    r1 = rho_nonlinear(T1, S1)
    # Solve for S2 so that the two water masses have exactly equal density.
    lo, hi = 33.0, 37.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if rho_nonlinear(T2, mid) > r1:
            hi = mid
        else:
            lo = mid
    S2 = 0.5 * (lo + hi)
    r2 = rho_nonlinear(T2, S2)
    Tm, Sm = 0.5 * (T1 + T2), 0.5 * (S1 + S2)
    r_mean = 0.5 * (r1 + r2)
    r_mix = rho_nonlinear(Tm, Sm)
    print(f"  water A: T = {T1:.2f} degC, S = {S1:.3f} g/kg  -> "
          f"rho = {r1:.4f} kg/m^3")
    print(f"  water B: T = {T2:.2f} degC, S = {S2:.3f} g/kg  -> "
          f"rho = {r2:.4f} kg/m^3")
    print(f"  equal density to {abs(r1 - r2) * 1e6:.1f} micro-kg/m^3")
    print(f"  50/50 mixture: T = {Tm:.2f} degC, S = {Sm:.3f} g/kg")
    print(f"  mean of the two densities   = {r_mean:.5f} kg/m^3")
    print(f"  density of the mixture      = {r_mix:.5f} kg/m^3")
    print(f"  cabbeling anomaly           = {1e3 * (r_mix - r_mean):.4f} "
          "g/m^3 (mixture is DENSER)")
    r_lin_mean = 0.5 * (rho_linear(T1, S1) + rho_linear(T2, S2))
    r_lin_mix = rho_linear(Tm, Sm)
    print(f"  the same experiment with the LINEAR EOS gives "
          f"{1e3 * (r_lin_mix - r_lin_mean):.4f} g/m^3,")
    print("  i.e. exactly zero: cabbeling is a consequence of the CURVATURE of "
          "the EOS.")

    section("4. Buoyancy frequency N^2 from a synthetic profile")
    z = np.linspace(0.0, 1500.0, 3001)
    T = 4.0 + 22.0 * np.exp(-z / 120.0)      # seasonal thermocline
    S = 34.80 + 0.50 * (1.0 - np.exp(-z / 300.0))
    rho_pot = rho_linear(T, S, 0.0)          # potential density (p = 0)
    drho_dz = np.gradient(rho_pot, z)
    # z is DEPTH, positive downwards, so N^2 = +(g/rho) d(rho_pot)/dz.
    N2 = G / RHO0 * drho_dz
    print("  synthetic profile:  T = 4 + 22 exp(-z/120) degC, "
          "S = 34.8 + 0.5 (1 - exp(-z/300)) g/kg")
    print("\n     z (m)    T (degC)   S (g/kg)   sigma_t    N^2 (1/s^2)   "
          "N (rad/s)   period (s)")
    for zz in (0.0, 50.0, 100.0, 200.0, 500.0, 1000.0, 1500.0):
        i = int(np.argmin(np.abs(z - zz)))
        n2 = max(N2[i], 0.0)
        n = np.sqrt(n2) if n2 > 0 else 0.0
        per = 2 * np.pi / n if n > 0 else float("inf")
        print(f"  {zz:7.0f}   {T[i]:8.2f}   {S[i]:9.3f}   {sigma_t(T[i], S[i]):8.3f}   "
              f"{n2:10.3e}   {n:9.5f}   {per:9.1f}")
    i0 = int(np.argmax(N2))
    print(f"\n  maximum N^2 = {N2[i0]:.3e} 1/s^2 at z = {z[i0]:.0f} m "
          f"(N = {np.sqrt(N2[i0]):.5f} rad/s, period "
          f"{2 * np.pi / np.sqrt(N2[i0]):.0f} s).")
    print(f"  minimum N^2 below the thermocline = "
          f"{N2[z > 500].min():.3e} 1/s^2, a factor of "
          f"{N2[i0] / N2[z > 500].min():.0f} smaller.")
    print("  N is real only if potential density increases with depth; the "
          "profile must be checked, not assumed.")

    section("5. Sound speed from a chosen teaching formula")
    print("  c = 1449 + 4.6 T - 0.055 T^2 + 1.34 (S - 35) + 0.016 z   [m/s]")
    print("\n     T (degC)   z (m)    c (m/s)")
    for Tt, zz in ((0.0, 0.0), (10.0, 0.0), (25.0, 0.0),
                   (10.0, 1000.0), (4.0, 4000.0), (4.0, 6000.0)):
        print(f"  {Tt:9.1f} {zz:8.0f}   {sound_speed(Tt, 35.0, zz):8.1f}")
    c_ref = 1500.0
    print(f"\n  the reference value c = {c_ref:.0f} m/s in seawater is used "
          "throughout this folder.")
    print(f"  this formula spans "
          f"{sound_speed(25.0, 37.0, 0.0):.1f} to {sound_speed(0.0, 33.0, 0.0):.1f} "
          f"m/s, i.e. a range of "
          f"{100 * (sound_speed(25.0, 37.0, 0.0) / sound_speed(0.0, 33.0, 0.0) - 1):.1f}%.")
    print("  A 1% sound-speed error therefore maps into a 1% depth error in any "
          "travel-time sounding.")

    section("6. Verification: linear versus nonlinear EOS over a T-S box")
    Tg = np.linspace(0.0, 30.0, 61)
    Sg = np.linspace(33.0, 37.0, 41)
    TT, SS = np.meshgrid(Tg, Sg)
    diff = rho_nonlinear(TT, SS) - rho_linear(TT, SS)
    print(f"  T in [0, 30] degC, S in [33, 37] g/kg  ({TT.size} points)")
    print(f"  max |rho_nonlinear - rho_linear| = "
          f"{np.abs(diff).max():.4f} kg/m^3")
    print(f"  as a fraction of rho0          = "
          f"{100 * np.abs(diff).max() / RHO0:.4f} %")
    print(f"  equivalent temperature error   = "
          f"{np.abs(diff).max() / RHO0 / ALPHA0:.2f} degC")
    print("\n  The linear EOS is therefore adequate for a stability argument at the")
    print("  few-per-cent level, and it is exactly the wrong tool for cabbeling:")
    print("  the effect we set out to measure in section 3 lives entirely in the")
    print("  term the linear EOS discards.")


if __name__ == "__main__":
    main()
