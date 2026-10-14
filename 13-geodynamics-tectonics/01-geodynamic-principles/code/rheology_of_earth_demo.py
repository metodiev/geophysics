#!/usr/bin/env python3
"""Rheology of the solid Earth: Maxwell relaxation, power-law creep, brittle
strength and the brittle-ductile transition.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rheology_of_earth_demo.py

Everything here is SYNTHETIC.  The two flow laws ("quartz-like" and
"olivine-like") use chosen teaching constants, not laboratory-derived values, and
no measured viscosity is quoted.  Print-only; no figures.

Contents
--------
1. Maxwell relaxation time and the Deborah number.
2. Steady-state creep: stress dependence and the measured stress exponent.
3. Temperature dependence of viscosity: the Arrhenius factor.
4. Diffusion versus dislocation creep: the crossover stress.
5. Brittle (frictional) strength and the brittle-ductile transition depth.
6. Postseismic relaxation of a stress step.
7. Laboratory-style inversion: recovering the stress exponent from noisy data.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
MU_SHEAR = 70.0e9      # Pa    shear modulus
G = 9.81               # m/s^2 gravitational acceleration (standard)
R_GAS = 8.314          # J/(mol K) gas constant (standard)
EPS_REF = 1.0e-15      # 1/s   reference strain rate for the strength envelope
MU_FRIC = 0.75         # -     SYNTHETIC friction coefficient
LAMBDA_P = 0.37        # -     SYNTHETIC pore-pressure (Hubbert-Rubey) factor
RHO_CRUST = 2800.0     # kg/m^3
RHO_MANTLE = 3300.0    # kg/m^3

# "quartz-like" crustal flow law (SYNTHETIC): edot = A sigma^n exp(-E/RT)
A_Q, N_Q, E_Q = 1.0e-19, 3.0, 200.0e3      # Pa^-n s^-1, -, J/mol
# "olivine-like" mantle flow law (SYNTHETIC)
A_O, N_O, E_O = 2.0e-28, 3.5, 350.0e3     # Pa^-n s^-1, -, J/mol
# diffusion creep (SYNTHETIC, Newtonian)
A_D, N_D, E_D = 1.0e-13, 1.0, 250.0e3     # Pa^-1 s^-1, -, J/mol

SEC_PER_YR = 3.1557e7


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def strain_rate(sigma, T, A, n, E):
    """Steady-state creep rate edot = A sigma^n exp(-E/(R T)), 1/s."""
    return A * sigma ** n * np.exp(-E / (R_GAS * T))


def effective_viscosity(sigma, T, A, n, E):
    """eta = sigma / (2 edot) for simple shear, Pa s."""
    return sigma / (2.0 * strain_rate(sigma, T, A, n, E))


def brittle_strength(z, rho):
    """Coulomb strength with pore pressure: mu_f (1 - lambda_p) rho g z, Pa."""
    return MU_FRIC * (1.0 - LAMBDA_P) * rho * G * z


def geotherm(z, gamma_c=20.0, gamma_m=12.0, h_crust=35.0e3, T_s=273.15):
    """Synthetic piecewise-linear geotherm in K (gamma in K/km, z in m)."""
    return np.where(
        z <= h_crust,
        T_s + gamma_c * z / 1e3,
        T_s + gamma_c * h_crust / 1e3 + gamma_m * (z - h_crust) / 1e3,
    )


def bdt_depth(gamma_c, gamma_m, h_crust, which):
    """Brittle-ductile transition depth by bisection (m)."""
    lo, hi = 1.0e3, 120.0e3

    def f(z):
        T = float(geotherm(np.array([z]), gamma_c, gamma_m, h_crust)[0])
        rho = RHO_CRUST if z <= h_crust else RHO_MANTLE
        br = brittle_strength(z, rho)
        if which == "crust":
            du = (EPS_REF / (A_Q * np.exp(-E_Q / (R_GAS * T)))) ** (1.0 / N_Q)
        else:
            du = (EPS_REF / (A_O * np.exp(-E_O / (R_GAS * T)))) ** (1.0 / N_O)
        return np.log10(max(br, 1e-30)) - np.log10(max(du, 1e-30))

    if f(lo) * f(hi) > 0:
        return np.nan
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def main():
    section("1. Maxwell relaxation time and the Deborah number")
    print("  t_M = eta / mu,  mu = %.1f GPa (SYNTHETIC constant)" % (MU_SHEAR / 1e9))
    print("   eta (Pa s)    t_M (s)       t_M (yr)")
    for eta in (1e18, 1e19, 1e20, 1e21, 1e22):
        tM = eta / MU_SHEAR
        print(f"   {eta:.0e}     {tM:.3e}      {tM / SEC_PER_YR:.3e}")
    print("\n  Deborah number De = t_M / t_observation:")
    print("   eta (Pa s)   t_obs = 1 s     1 yr        10 kyr")
    for eta in (1e19, 1e21):
        tM = eta / MU_SHEAR
        print(f"   {eta:.0e}      {tM / 1.0:.2e}     {tM / SEC_PER_YR:.2e}    "
              f"{tM / (SEC_PER_YR * 1e4):.2e}")
    print("  De << 1 -> elastic response; De >> 1 -> the material has forgotten")
    print("  its elastic strain and behaves as a viscous fluid.")

    section("2. Steady-state creep: stress dependence (T = 1600 K)")
    T = 1600.0
    print("  SYNTHETIC olivine-like law: n = %.1f, E = %.0f kJ/mol"
          % (N_O, E_O / 1e3))
    print("   sigma (MPa)   edot (1/s)     eta = sigma/(2 edot) (Pa s)")
    sig = np.array([1e6, 1e7, 1e8])
    eta_eff = np.array([effective_viscosity(s, T, A_O, N_O, E_O) for s in sig])
    for s, e, eta in zip(sig, [strain_rate(s, T, A_O, N_O, E_O) for s in sig],
                         eta_eff):
        print(f"   {s / 1e6:9.1f}   {e:.4e}      {eta:.4e}")
    slope = np.polyfit(np.log10(sig), np.log10(eta_eff), 1)[0]
    print(f"  measured slope d log(eta) / d log(sigma) = {slope:.4f}")
    print(f"  theory: 1 - n = {1.0 - N_O:.1f}.  A stress exponent n > 1 means the")
    print("  rock gets WEAKER the faster it is sheared (shear-thinning).")

    section("3. Temperature dependence of viscosity (sigma = 10 MPa)")
    sigma = 1.0e7
    etas = []
    for Tk in (1500.0, 1600.0, 1700.0):
        eta = effective_viscosity(sigma, Tk, A_O, N_O, E_O)
        etas.append(eta)
        print(f"  T = {Tk:.0f} K   eta = {eta:.4e} Pa s")
    print(f"  ratio eta(1500 K)/eta(1600 K) = {etas[0] / etas[1]:.3e}")
    print(f"  ratio eta(1600 K)/eta(1700 K) = {etas[1] / etas[2]:.3e}")
    ratio_1200_1600 = (effective_viscosity(sigma, 1200.0, A_O, N_O, E_O)
                       / effective_viscosity(sigma, 1600.0, A_O, N_O, E_O))
    print(f"  ratio eta(1200 K)/eta(1600 K) = {ratio_1200_1600:.3e}")
    print("  a few hundred kelvin changes viscosity by orders of magnitude, which")
    print("  is why the lithosphere/asthenosphere contrast is thermal.")

    section("4. Diffusion versus dislocation creep: the crossover stress")
    T = 1600.0
    lo, hi = np.log(1e3), np.log(1e10)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        s = np.exp(mid)
        d_dis = strain_rate(s, T, A_O, N_O, E_O)
        d_dif = strain_rate(s, T, A_D, N_D, E_D)
        if d_dis < d_dif:
            lo = mid
        else:
            hi = mid
    s_cross = np.exp(0.5 * (lo + hi))
    eta_dif = effective_viscosity(s_cross, T, A_D, N_D, E_D)
    print(f"  SYNTHETIC diffusion law: n = 1, E = {E_D / 1e3:.0f} kJ/mol")
    print(f"  crossover stress = {s_cross:.4e} Pa = {s_cross / 1e6:.2f} MPa")
    print(f"  eta at the crossover = {eta_dif:.4e} Pa s")
    print("  below the crossover (low stress, fine grains) diffusion creep wins and")
    print("  n = 1; above it dislocation creep wins and viscosity falls with stress.")

    section("5. Brittle strength and the brittle-ductile transition")
    print(f"  SYNTHETIC friction mu_f = {MU_FRIC:.2f}, pore factor lambda_p = "
          f"{LAMBDA_P:.2f}")
    print("  sigma_b = mu_f (1 - lambda_p) rho g z")
    print("    depth (km)   sigma_b (MPa)   [crust rho = 2800]")
    for zkm in (2.0, 5.0, 10.0, 20.0):
        print(f"      {zkm:6.1f}      {brittle_strength(zkm * 1e3, RHO_CRUST) / 1e6:9.1f}")
    for zkm in (35.0, 60.0, 90.0):
        print(f"      {zkm:6.1f}      {brittle_strength(zkm * 1e3, RHO_MANTLE) / 1e6:9.1f}"
              "   [mantle rho = 3300]")
    zc = bdt_depth(20.0, 12.0, 35.0e3, "crust")
    zm = bdt_depth(20.0, 12.0, 35.0e3, "mantle")
    print(f"\n  SYNTHETIC geotherm: 20 K/km in the crust, 12 K/km below 35 km")
    print(f"  crustal brittle-ductile transition at z = {zc / 1e3:.2f} km")
    print(f"  mantle  brittle-ductile transition at z = {zm / 1e3:.2f} km")
    for gam in (10.0, 20.0, 30.0):
        zc2 = bdt_depth(gam, gam, 35.0e3, "crust")
        zm2 = bdt_depth(gam, gam, 35.0e3, "mantle")
        print(f"  geotherm {gam:4.1f} K/km -> crust BDT {zc2 / 1e3:6.2f} km, "
              f"mantle BDT {zm2 / 1e3:6.2f} km")

    section("6. Postseismic relaxation of a stress step")
    print("  sigma(t) = sigma_0 exp(-t / t_M); fraction relaxed = 1 - exp(-t/t_M)")
    for eta in (1e18, 1e19, 1e20):
        tM = eta / MU_SHEAR
        for t in (1.0, 10.0):
            frac = 1.0 - np.exp(-t * SEC_PER_YR / tM)
            print(f"  eta = {eta:.0e} Pa s, t = {t:4.1f} yr -> "
                  f"relaxed {frac * 100:6.2f}%   (t_M = {tM / SEC_PER_YR:.3f} yr)")
    print("  a low-viscosity channel relaxes a coseismic stress within years; a")
    print("  10^20 Pa s region needs millennia.")

    section("7. Laboratory-style inversion: recovering the stress exponent")
    n_true = N_O
    T = 1600.0
    sig_lab = 10.0 ** np.linspace(6.0, 8.0, 12)
    edot_true = strain_rate(sig_lab, T, A_O, N_O, E_O)
    noise = 0.05 * RNG.standard_normal(sig_lab.size)
    edot_meas = edot_true * 10.0 ** noise
    fit = np.polyfit(np.log10(sig_lab), np.log10(edot_meas), 1)
    n_fit = fit[0]
    resid = np.log10(edot_meas) - np.polyval(fit, np.log10(sig_lab))
    print(f"  true n = {n_true:.2f}; 12 SYNTHETIC data points with 5% log-normal")
    print(f"  noise give fitted n = {n_fit:.3f}")
    print(f"  rms misfit in log10(edot) = {np.std(resid):.4f}")
    print("  the inversion is the log-log slope of a creep law: n is well resolved,")
    print("  the prefactor A is not (it trades off against E and T).")

    print("\n" + "=" * 72)
    print("All models are SYNTHETIC. Only g = 9.81 m/s^2 and R = 8.314 J/(mol K)")
    print("are standard constants.")
    print("=" * 72)


if __name__ == "__main__":
    main()
