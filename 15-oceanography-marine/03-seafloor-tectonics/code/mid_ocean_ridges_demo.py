#!/usr/bin/env python3
"""Mid-ocean ridges: thermal subsidence, surface heat flow, the onset of
hydrothermal convection in the crust, and the axial thermal structure.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mid_ocean_ridges_demo.py

Everything here is SYNTHETIC.  The thermal model is the classical half-space
cooling model with the standard material constants listed below; the
hydrothermal model is a teaching model, not a fit to any survey, and no number
is quoted from a published measurement.  No real ridge, vent field or cruise is
referenced.

Contents
--------
1. Subsidence coefficient a in  depth = d_ridge + a sqrt(age), DERIVED from
   thermal contraction, and RE-MEASURED from synthetic noisy bathymetry.
2. Half-space surface heat flow versus age, and the ridge-flank slope.
3. Onset of porous convection: Rayleigh number, critical permeability,
   predicted fluid flux.
4. Removing the young-crust heat-flow deficit with a 350 K fluid: volume flux.
5. Axial thermal structure: depth to the 600 C isotherm versus spreading rate.
6. Worked examples used in the lesson.
"""

import numpy as np
from scipy.special import erf, erfinv

RNG = np.random.default_rng(20261014)

# --- standard material constants (SI unless noted) ---------------------------
RHO_M = 3300.0        # kg/m^3   mantle density at ridge-axis temperature
RHO_W = 1030.0        # kg/m^3   seawater density (model value for this lesson)
T_M = 1350.0          # K        mantle temperature above the seafloor
ALPHA_V = 3.0e-5      # 1/K      volumetric thermal expansion, mantle rock
KAPPA = 1.0e-6        # m^2/s    thermal diffusivity, rock
K_COND = 3.2          # W/m/K    thermal conductivity, rock
D_RIDGE = 2500.0      # m        ridge-axis depth, model value
RA_C = 4.0 * np.pi ** 2   # critical Rayleigh number for porous convection
G = 9.81              # m/s^2
SEC_PER_MYR = 3.15576e13
SEC_PER_YR = 3.15576e7


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def subsidence_rate() -> float:
    """Depth increase per sqrt(second), m/s^0.5, from isostatic thermal contraction."""
    return (RHO_M / (RHO_M - RHO_W)) * ALPHA_V * T_M * 2.0 * np.sqrt(KAPPA / np.pi)


def subsidence_rate_per_myr() -> float:
    """Same coefficient in m per (Myr)^0.5, the unit bathymetric fits use."""
    return subsidence_rate() * np.sqrt(SEC_PER_MYR)


def depth_m(age_myr):
    """Seafloor depth in metres for an age in Myr (half-space cooling)."""
    return D_RIDGE + subsidence_rate_per_myr() * np.sqrt(age_myr)


def heat_flow(age_myr):
    """Conductive surface heat flow in W/m^2 for half-space cooling, Myr in."""
    t = np.asarray(age_myr, dtype=float) * SEC_PER_MYR
    return K_COND * T_M / np.sqrt(np.pi * KAPPA * t)


def raid(perm, H, dT, mu, alpha_w):
    """Rayleigh number for convection of water in a permeable layer of thickness H."""
    return RHO_W * G * alpha_w * dT * perm * H / (mu * KAPPA)


def main():
    section("1. Subsidence coefficient from thermal contraction")
    a_myr = subsidence_rate_per_myr()
    print("model:  depth = d_ridge + a * sqrt(age),  a = rho_m/(rho_m-rho_w)")
    print("        x alpha_v T_m 2 sqrt(kappa/pi)")
    print(f"  rho_m/(rho_m-rho_w) = {RHO_M:.0f}/({RHO_M - RHO_W:.0f}) = "
          f"{RHO_M / (RHO_M - RHO_W):.5f}")
    print(f"  alpha_v T_m         = {ALPHA_V:.1e} 1/K x {T_M:.0f} K = "
          f"{ALPHA_V * T_M:.4e}")
    print(f"  2 sqrt(kappa/pi)    = {2 * np.sqrt(KAPPA / np.pi):.5e} m/s^0.5")
    print(f"  a = {subsidence_rate():.5e} m/s^0.5 = {a_myr:.1f} m per (Myr)^0.5")
    print(f"  d_ridge = {D_RIDGE:.0f} m (model value)")
    print("\n  age (Myr)   depth (m)   depth - d_ridge (m)")
    for age in (1.0, 4.0, 10.0, 25.0, 50.0, 100.0):
        d = depth_m(age)
        print(f"  {age:9.1f}   {d:9.0f}   {d - D_RIDGE:17.0f}")

    section("1b. Re-measuring the coefficient from SYNTHETIC noisy bathymetry")
    age = np.linspace(1.0, 60.0, 60)
    sigma = 60.0  # m, synthetic depth scatter
    depth_obs = depth_m(age) + RNG.normal(0.0, sigma, age.size)
    # fit a straight line in sqrt(age)
    A = np.vstack([np.ones_like(age), np.sqrt(age)]).T
    coef, *_ = np.linalg.lstsq(A, depth_obs, rcond=None)
    resid = depth_obs - A @ coef
    dof = age.size - 2
    s2 = resid @ resid / dof
    cov = s2 * np.linalg.inv(A.T @ A)
    a_fit = coef[1]
    a_err = np.sqrt(cov[1, 1])
    print(f"  {age.size} synthetic depths on 1-60 Myr crust, scatter sigma = {sigma:.0f} m")
    print(f"  fit: d_ridge = {coef[0]:.0f} +/- {np.sqrt(cov[0, 0]):.0f} m")
    print(f"       a       = {a_fit:.1f} +/- {a_err:.1f} m per (Myr)^0.5")
    print(f"  true a = {a_myr:.1f}; residual rms = "
          f"{np.sqrt(resid @ resid / dof):.1f} m")
    t_slope = (a_fit - a_myr) / a_err
    print(f"  (measured - true)/error = {t_slope:+.2f} sigma")

    section("2. Surface heat flow versus age (half-space cooling)")
    print("  model:  q = k T_m / sqrt(pi kappa t)")
    print(f"  k T_m = {K_COND * T_M:.0f} W/m/K x K  ;  pi kappa = {np.pi * KAPPA:.4e} m^2/s")
    print("\n   age (Myr)   q (mW/m^2)   subsidence rate (mm/yr)")
    for age in (0.1, 1.0, 5.0, 10.0, 25.0, 50.0, 100.0):
        q = heat_flow(age) * 1e3
        dzdt = subsidence_rate() / (2 * np.sqrt(age * SEC_PER_MYR)) * 1e3 * SEC_PER_YR
        print(f"   {age:9.1f}   {q:10.1f}   {dzdt:21.4f}")
    print(f"\n  ratio q(1 Myr)/q(10 Myr) = {heat_flow(1.0) / heat_flow(10.0):.3f} "
          f"(half-space theory: 10^{0.5} = {np.sqrt(10):.3f})")
    u_half = 0.05 / SEC_PER_YR   # 5 cm/yr in m/s
    slope = subsidence_rate() / (2.0 * np.sqrt(10.0 * SEC_PER_MYR)) / u_half
    print(f"  ridge-flank slope at 10 Myr, half-rate 5 cm/yr: {slope * 1e3:.2f} mm/m "
          f"= {slope * 1e3:.2f} m/km")

    section("3. Onset of hydrothermal convection in the crust")
    alpha_w, dT, mu, H_perm = 5.0e-4, 200.0, 2.0e-4, 1000.0
    print("teaching model:  Ra = rho_w g alpha_w dT k H / (mu kappa)")
    print(f"  alpha_w = {alpha_w:.1e} 1/K, dT = {dT:.0f} K, mu = {mu:.1e} Pa s,")
    print(f"  H (permeable layer) = {H_perm:.0f} m, kappa = {KAPPA:.1e} m^2/s")
    print(f"  critical Rayleigh number Ra_c = 4 pi^2 = {RA_C:.2f}")
    print("\n  permeability (m^2)   Ra      Ra/Ra_c   regime")
    for perm in (1e-15, 5e-15, 1e-14, 1e-13):
        ra = raid(perm, H_perm, dT, mu, alpha_w)
        print(f"  {perm:18.1e}   {ra:7.1f}   {ra / RA_C:8.2f}   "
              f"{'convecting' if ra > RA_C else 'conductive'}")
    k_min = RA_C * mu * KAPPA / (RHO_W * G * alpha_w * dT * H_perm)
    print(f"\n  permeability needed for onset: k_min = {k_min:.2e} m^2 "
          f"= {k_min / 9.869e-16:.1f} mD (1 mD = 9.869e-16 m^2)")
    for perm in (1e-14, 1e-13):
        ra = raid(perm, H_perm, dT, mu, alpha_w)
        nu = max(1.0, ra / RA_C)
        q_cond = K_COND * dT / H_perm
        print(f"  k = {perm:.0e} m^2: Nu = {nu:.1f} (linear closure), "
              f"conductive q = {q_cond:.3f} W/m^2, convective q = {nu * q_cond:.3f} W/m^2")

    section("4. Fluid flux that removes the young-crust heat-flow deficit")
    t1_myr, f_removed, area = 10.0, 0.3, 1.0e10   # 100 km x 100 km patch
    t1 = t1_myr * SEC_PER_MYR
    #  integral_0^t1 k T_m / sqrt(pi kappa t) dt = 2 k T_m sqrt(t1/(pi kappa))
    q_int = 2.0 * K_COND * T_M * np.sqrt(t1 / (np.pi * KAPPA))
    c_p, dT_f = 5000.0, 350.0
    rho_c_dT = RHO_W * c_p * dT_f
    vol = f_removed * q_int * area / rho_c_dT
    print(f"  crust younger than {t1_myr:.0f} Myr, patch {np.sqrt(area) / 1e3:.0f} km x "
          f"{np.sqrt(area) / 1e3:.0f} km")
    print(f"  integrated half-space heat over 0-{t1_myr:.0f} Myr: "
          f"{q_int:.3e} J/m^2")
    print(f"  fraction removed by advection (model): {f_removed:.2f}")
    print(f"  fluid: rho c_p dT = {RHO_W:.0f} x {c_p:.0f} x {dT_f:.0f} = "
          f"{rho_c_dT:.3e} J/m^3")
    print(f"  water volume passed through the patch: {vol:.3e} m^3")
    print(f"  = {vol / area:.3e} m^3 per m^2 of seafloor, i.e. a uniform column of "
          f"{vol / area:.0f} m")
    print(f"  equivalent flux = {vol / area / t1:.3e} m/s = "
          f"{vol / area / t1 * 1e3 * 3.15576e7:.2f} mm/yr")
    print(f"  per metre of ridge line: {vol / 1.0e5:.3e} m^3 in {t1_myr:.0f} Myr")

    section("5. Axial thermal structure: depth to the 600 C isotherm")
    u_frac = 600.0 / T_M
    u_arg = erfinv(u_frac)
    print(f"  T(z,t) = T_m erf(z / (2 sqrt(kappa t)));  solve erf(u) = "
          f"600/{T_M:.0f} = {u_frac:.4f}")
    print(f"  u = {u_arg:.5f}, so z = {2 * u_arg:.5f} sqrt(kappa t), t = x / u_half")
    print("\n  half-rate (cm/yr)   x (km)   age (Myr)   z600 (m)")
    for u_cm in (1.0, 5.0, 10.0):
        u = u_cm / 100.0 / SEC_PER_YR
        for x_km in (2.0, 5.0, 10.0):
            t = x_km * 1e3 / u
            print(f"  {u_cm:17.1f}   {x_km:7.1f}   {t / SEC_PER_MYR:9.3f}   "
                  f"{2 * u_arg * np.sqrt(KAPPA * t):9.0f}")
    print("  the 600 C depth grows as sqrt(x / u_half): slower spreading buries the")
    print("  brittle-ductile transition deeper, which is why slow ridge axes sit in")
    print("  rifted valleys and fast axes sit on an axial high.")

    section("6. Worked examples used in the lesson")
    age_ex = 4.0
    print(f"(a) depth of {age_ex:.0f} Myr crust: d = {D_RIDGE:.0f} + "
          f"{a_myr:.1f} sqrt({age_ex:.0f}) = {depth_m(age_ex):.0f} m")
    print(f"    subsidence from the axis = {depth_m(age_ex) - D_RIDGE:.0f} m")
    print(f"(b) heat flow at {age_ex:.0f} Myr = {heat_flow(age_ex) * 1e3:.1f} mW/m^2")
    print(f"    conductive-equivalent heat flow at 25 Myr = "
          f"{heat_flow(25.0) * 1e3:.1f} mW/m^2")
    print(f"(c) Ra at k = 1e-14 m^2, H = {H_perm:.0f} m, dT = {dT:.0f} K: "
          f"{raid(1e-14, H_perm, dT, mu, alpha_w):.1f} vs Ra_c = {RA_C:.2f}")
    print(f"    onset permeability = {k_min:.3e} m^2")
    print(f"(d) water column equivalent over 0-{t1_myr:.0f} Myr = {vol / area:.0f} m "
          f"at f = {f_removed:.2f}")
    print(f"(e) z600 at x = 5 km, half-rate 5 cm/yr = "
          f"{2 * u_arg * np.sqrt(KAPPA * 5e3 / (0.05 / SEC_PER_YR)):.0f} m")
    print(f"    z600 at x = 5 km, half-rate 1 cm/yr = "
          f"{2 * u_arg * np.sqrt(KAPPA * 5e3 / (0.01 / SEC_PER_YR)):.0f} m")
    print("\nAll values are SYNTHETIC model output; the material constants are the")
    print("standard thermal constants stated in the header of this file.")


if __name__ == "__main__":
    main()
