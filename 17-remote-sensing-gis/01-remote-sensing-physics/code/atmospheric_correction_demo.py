#!/usr/bin/env python3
"""Atmospheric attenuation, scattering and correction: measured trade-offs.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python atmospheric_correction_demo.py

Everything is SYNTHETIC.  The atmosphere is a teaching model: a vertical optical
depth split into a Rayleigh-like and an aerosol-like component with an Angstrom
exponent chosen in this file, plus an isothermal emitting layer for the thermal
example.  No measured optical depth, aerosol product or instrument is used.

Contents
--------
1. Beer-Lambert transmittance and the plane-parallel air mass.
2. Two-way transmittance for reflected solar radiation.
3. The Angstrom exponent from a two-wavelength optical depth ratio.
4. Path radiance and surface-reflectance retrieval, with the errors.
5. Sensitivity of the retrieved reflectance to an optical-depth error.
6. A Monte Carlo propagation of optical-depth uncertainty.
7. Rayleigh versus aerosol scattering across the visible.
8. Thermal atmospheric correction: emission, reflection and the bias.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

H_PLANCK = 6.62607015e-34
C_LIGHT = 2.99792458e8
K_BOLTZ = 1.380649e-23
SOLAR_CONSTANT = 1361.0

# --- SYNTHETIC atmosphere (chosen teaching values) ---------------------------
TAU_RAYLEIGH_550 = 0.10      # vertical Rayleigh-like optical depth at 0.55 um
TAU_AEROSOL_550 = 0.15       # vertical aerosol-like optical depth at 0.55 um
ANGSTROM_AEROSOL = 1.30      # tau_aerosol ~ lambda^-alpha
LAM_REF = 0.55               # um
T_ATM_K = 280.0              # isothermal atmospheric layer temperature
EPS_SURFACE = 0.95           # SYNTHETIC thermal emissivity
TAU_THERMAL = 0.85           # vertical transmittance in the thermal band


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def tau_vertical(lam_um):
    """SYNTHETIC vertical optical depth, Rayleigh-like + aerosol-like."""
    lam = np.asarray(lam_um, dtype=float)
    return (TAU_RAYLEIGH_550 * (lam / LAM_REF) ** -4.0
            + TAU_AEROSOL_550 * (lam / LAM_REF) ** -ANGSTROM_AEROSOL)


def air_mass(theta_deg):
    """Plane-parallel air mass m = 1/cos(theta) for zenith angle theta."""
    return 1.0 / np.cos(np.deg2rad(theta_deg))


def planck(lam_um, T_K):
    lam_m = lam_um * 1e-6
    x = H_PLANCK * C_LIGHT / (lam_m * K_BOLTZ * T_K)
    return 2.0 * H_PLANCK * C_LIGHT ** 2 / lam_m ** 5 / np.expm1(x)


def planck_inverse_um(L, lam_um):
    lam_m = lam_um * 1e-6
    x = 2.0 * H_PLANCK * C_LIGHT ** 2 / (lam_m ** 5 * L)
    return H_PLANCK * C_LIGHT / (lam_m * K_BOLTZ * np.log1p(x))


def main():
    section("1. Beer-Lambert transmittance and the air mass")
    tau_v = float(tau_vertical(0.55))
    print(f"SYNTHETIC vertical optical depth at 0.55 um = {tau_v:.3f}"
          f" (Rayleigh-like {TAU_RAYLEIGH_550:.2f} + aerosol-like {TAU_AEROSOL_550:.2f})")
    print("   zenith (deg)   air mass   slant tau   transmittance")
    for th in (0.0, 30.0, 45.0, 60.0, 75.0, 85.0):
        m = air_mass(th)
        print(f"  {th:12.0f}   {m:8.3f}   {tau_v * m:9.3f}   {np.exp(-tau_v * m):13.4f}")
    print("  T = exp(-tau m); the plane-parallel air mass diverges at the horizon,")
    print("  which is where this approximation must be replaced by a curved-air")
    print("  model.")

    section("2. Two-way transmittance for reflected solar radiation")
    print("   sun (deg)   view (deg)   T_down    T_up     round trip")
    for th_sun, th_view in ((30.0, 0.0), (30.0, 40.0), (60.0, 0.0), (60.0, 60.0)):
        t_d = np.exp(-tau_v * air_mass(th_sun))
        t_u = np.exp(-tau_v * air_mass(th_view))
        print(f"  {th_sun:9.0f}   {th_view:10.0f}   {t_d:7.4f}   {t_u:7.4f}   "
              f"{t_d * t_u:10.4f}")
    print("  The round-trip factor is the product of two one-way transmittances,")
    print("  and it is the quantity that multiplies surface reflectance.")

    section("3. Angstrom exponent from two wavelengths")
    for l1, l2 in ((0.45, 0.55), (0.55, 0.65)):
        t1 = TAU_AEROSOL_550 * (l1 / LAM_REF) ** -ANGSTROM_AEROSOL
        t2 = TAU_AEROSOL_550 * (l2 / LAM_REF) ** -ANGSTROM_AEROSOL
        alpha = -np.log(t1 / t2) / np.log(l1 / l2)
        print(f"  aerosol tau({l1:.2f} um) = {t1:.4f}, tau({l2:.2f} um) = {t2:.4f}"
              f"  ->  alpha = {alpha:.4f}")
    print(f"  The synthetic aerosol has alpha = {ANGSTROM_AEROSOL:.2f} exactly; the")
    print("  two-wavelength estimate recovers it to 4 decimal places, which shows")
    print("  the estimator is exact for a pure power law and therefore that any")
    print("  disagreement in practice comes from departures from the power law.")

    section("4. Path radiance and surface-reflectance retrieval")
    lam = 0.55
    mu_sun = np.cos(np.deg2rad(30.0))
    tau_tot = float(tau_vertical(lam))
    E_sun_surface = 800.0                      # SYNTHETIC W m^-2 um^-1
    rho_true = 0.30
    T_down = np.exp(-tau_tot * 1.0 / mu_sun)
    T_up = np.exp(-tau_tot * 1.0)
    L_surface = rho_true * E_sun_surface * T_down / np.pi
    # Single-scattering-like path radiance: albedo of single scattering x tau.
    omega0 = 0.95                              # SYNTHETIC single-scattering albedo
    L_path = omega0 * tau_tot * E_sun_surface / (4.0 * np.pi * mu_sun)
    L_sensor = L_path + T_up * L_surface
    print(f"  wavelength {lam:.2f} um, sun zenith 30 deg, view nadir")
    print(f"  vertical tau = {tau_tot:.4f}; T_down = {T_down:.4f}; T_up = {T_up:.4f}")
    print(f"  true surface reflectance rho = {rho_true:.3f}")
    print(f"  surface radiance at TOA (after up-leg) = {T_up * L_surface:.4f} "
          "W m^-2 sr^-1 um^-1")
    print(f"  path radiance (synthetic)              = {L_path:.4f} "
          "W m^-2 sr^-1 um^-1")
    print(f"  sensor radiance                        = {L_sensor:.4f} "
          "W m^-2 sr^-1 um^-1")
    rho_correct = np.pi * (L_sensor - L_path) / (E_sun_surface * T_down * T_up)
    rho_naive = np.pi * L_sensor / (E_sun_surface * T_down * T_up)
    rho_dos = np.pi * (L_sensor - L_path_dark_estimate(lam)) / (
        E_sun_surface * T_down * T_up)
    print(f"  retrieved with full correction = {rho_correct:.4f} (true {rho_true:.3f})")
    print(f"  retrieved ignoring path radiance = {rho_naive:.4f} "
          f"({(rho_naive - rho_true) / rho_true:+.1%})")
    print(f"  retrieved by dark-object subtraction, L_path assumed 10% low = "
          f"{rho_dos:.4f} ({100 * (rho_dos - rho_true) / rho_true:+.1f}%)")
    print("  A 10% error in the estimated path radiance, which is a good day's")
    print("  aerosol characterisation, is a several-percent reflectance error.")

    section("5. Sensitivity to an optical-depth error")
    L_sensor_true = L_path + T_up * L_surface
    m_total = 1.0 / mu_sun + 1.0
    print("  The analyst knows the path radiance but errs in tau; the true sensor")
    print("  radiance used the true tau.")
    print("   tau error   assumed T_round   retrieved rho   error")
    for rel in (-0.20, -0.10, 0.0, 0.10, 0.20):
        t_d_a = np.exp(-tau_tot * (1 + rel) / mu_sun)
        t_u_a = np.exp(-tau_tot * (1 + rel))
        rho_r = np.pi * (L_sensor_true - L_path) / (E_sun_surface * t_d_a * t_u_a)
        print(f"  {rel:+10.0%}   {t_d_a * t_u_a:14.4f}   {rho_r:15.4f}   "
              f"{(rho_r - rho_true) / rho_true:+8.2%}")
    pred = np.exp(tau_tot * m_total * 0.10) - 1.0
    print(f"  predicted +10% tau error: exp(tau m_round x 0.10) - 1 = {pred:+.2%}")
    print("  The correction is multiplicative, so an optical-depth error along BOTH")
    print("  legs is amplified by the round-trip air mass"
          f" m_round = {m_total:.4f}.")

    section("6. Monte Carlo propagation of optical-depth uncertainty")
    n = 20000
    u = 0.10 * RNG.standard_normal(n)
    t_d_a = np.exp(-tau_tot * (1 + u) / mu_sun)
    t_u_a = np.exp(-tau_tot * (1 + u))
    rho_mc = np.pi * (L_sensor_true - L_path) / (E_sun_surface * t_d_a * t_u_a)
    print(f"  {n} draws, assumed tau = true tau x (1 + u), u ~ N(0, {0.10:.2f}^2)")
    print(f"  retrieved rho = {rho_mc.mean():.4f} "
          f"+/- {rho_mc.std(ddof=1):.4f} (1 sigma)")
    print(f"  bias = {rho_mc.mean() - rho_true:+.4f} "
          f"({100 * (rho_mc.mean() - rho_true) / rho_true:+.2f}%)")
    print(f"  standard error of that bias estimate = "
          f"{100 * rho_mc.std(ddof=1) / np.sqrt(n) / rho_true:.3f}%")
    print(f"  relative spread = {rho_mc.std(ddof=1) / rho_true:.2%}")
    sig = tau_tot * m_total * 0.10
    print(f"  theory: log-spread tau m_round sigma_u = {sig:.4f} -> "
          f"spread {np.sqrt(np.exp(sig**2) - 1):.2%}, "
          f"bias exp(sigma^2/2)-1 = {np.exp(sig**2 / 2) - 1:+.3%}")
    print("  A multiplicative error is convex, so its noise has a small POSITIVE")
    print("  bias on top of the spread: averaging many uncertain corrections does")
    print("  not converge to the truth unless the tau errors are centred correctly.")

    section("7. Rayleigh versus aerosol scattering across the visible")
    print("   lambda (um)   Rayleigh tau   aerosol tau   total tau   Rayleigh share")
    for lam_um in (0.40, 0.45, 0.55, 0.65, 0.75, 1.00):
        tr = TAU_RAYLEIGH_550 * (lam_um / LAM_REF) ** -4.0
        ta = TAU_AEROSOL_550 * (lam_um / LAM_REF) ** -ANGSTROM_AEROSOL
        print(f"  {lam_um:11.2f}   {tr:12.4f}   {ta:11.4f}   {tr + ta:9.4f}   "
              f"{tr / (tr + ta):14.3f}")
    print("  Rayleigh scattering falls as lambda^-4 and aerosol as lambda^-1.3, so")
    lam_x = LAM_REF * (TAU_AEROSOL_550 / TAU_RAYLEIGH_550) ** (
        1.0 / (ANGSTROM_AEROSOL - 4.0))
    print(f"  the molecular term dominates toward the blue.  The two terms are equal")
    print(f"  at lambda = {lam_x:.4f} um in this synthetic atmosphere; blueward of it")
    print("  the molecular term wins, redward the aerosol term does.")

    section("8. Thermal atmospheric correction: bias by neglected term")
    lam_t = 10.8
    T_surf = 300.0
    L_emit = EPS_SURFACE * planck(lam_t, T_surf)
    L_down = planck(lam_t, T_ATM_K)
    L_up = (1.0 - TAU_THERMAL) * planck(lam_t, T_ATM_K)
    L_sky = (1.0 - EPS_SURFACE) * L_down
    L_sensor = TAU_THERMAL * (L_emit + L_sky) + L_up
    print(f"  lambda = {lam_t:.1f} um, SYNTHETIC T_surface = {T_surf:.0f} K, "
          f"eps = {EPS_SURFACE:.2f}, tau_atm = {TAU_THERMAL:.2f}, "
          f"T_atm = {T_ATM_K:.0f} K")
    print(f"  surface emission term  eps B(Ts)          = {L_emit:.4e} "
          f"({L_emit / L_sensor:6.2%} of sensor radiance)")
    print(f"  reflected sky term     tau (1-eps) B(Ta)  = "
          f"{TAU_THERMAL * L_sky:.4e} ({TAU_THERMAL * L_sky / L_sensor:6.2%})")
    print(f"  atmospheric up term    (1-tau) B(Ta)      = {L_up:.4e} "
          f"({L_up / L_sensor:6.2%})")
    print(f"  reduction of the surface term by tau      = "
          f"{L_emit - TAU_THERMAL * L_emit:.4e} "
          f"({(L_emit - TAU_THERMAL * L_emit) / L_sensor:6.2%})")
    print(f"  sensor radiance                           = {L_sensor:.4e} "
          "W m^-2 sr^-1 m^-1")
    print("\n  Retrieved surface temperature under four assumed forward models:")
    rows = [
        ("A  blackbody surface, no atmosphere",
         planck_inverse_um(L_sensor, lam_t)),
        ("B  emissivity known, no atmosphere",
         planck_inverse_um(L_sensor / EPS_SURFACE, lam_t)),
        ("C  tau and up term, sky term ignored",
         planck_inverse_um((L_sensor - L_up) / (TAU_THERMAL * EPS_SURFACE), lam_t)),
        ("D  full radiative transfer",
         planck_inverse_um(((L_sensor - L_up) / TAU_THERMAL - L_sky)
                           / EPS_SURFACE, lam_t)),
    ]
    for name, T in rows:
        print(f"  {name:38s} T = {T:8.3f} K  ({T - T_surf:+6.2f} K)")
    print("  Rows A and B look accurate only because two large errors CANCEL: the")
    print("  atmospheric up term adds radiance while tau removes it, and at these")
    print("  parameter values the two effects are within a quarter of a kelvin of")
    print("  each other.  Row C shows that the reflected-sky term alone is worth")
    print("  +2.52 K when omitted.  A retrieval that is right for the wrong reason")
    print("  will fail as soon as the atmosphere, the surface temperature or the")
    print("  emissivity changes.  The two-band (split-window) approach of 17-02-03")
    print("  removes part of this because the two bands share the emissivity and")
    print("  differ mainly in tau.")


def L_path_dark_estimate(lam_um):
    """A dark-object estimate of path radiance: deliberately 10% too low."""
    mu_sun = np.cos(np.deg2rad(30.0))
    omega0 = 0.95
    return 0.90 * omega0 * float(tau_vertical(lam_um)) * 800.0 / (4.0 * np.pi * mu_sun)


if __name__ == "__main__":
    main()
