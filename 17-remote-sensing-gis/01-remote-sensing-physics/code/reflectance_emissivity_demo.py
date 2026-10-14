#!/usr/bin/env python3
"""Reflectance, emissivity and spectral signatures of three notional surfaces.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reflectance_emissivity_demo.py

Everything is SYNTHETIC.  The three spectral reflectance curves are SUM OF
LOGISTIC AND GAUSSIAN terms whose centres, widths and depths are chosen in this
file; they are teaching shapes, not measured spectra of any real material, and
the notional bands are intervals in this file, not instrument bands.

Contents
--------
1. Energy conservation rho + tau + alpha = 1 on the synthetic surfaces.
2. The synthetic reflectance spectra and their notional band means.
3. Broadband albedo by weighting with a synthetic solar spectrum.
4. Lambertian radiance L = rho E / pi from a stated irradiance.
5. Kirchhoff: emissivity of the opaque surfaces, eps = 1 - rho.
6. Brightness temperature and the error an emissivity assumption causes.
7. Non-Lambertian geometry: what a nadir measurement misses.
8. Verification of the Planck inversion by forward modelling.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

H_PLANCK = 6.62607015e-34      # J s
C_LIGHT = 2.99792458e8         # m / s
K_BOLTZ = 1.380649e-23         # J / K
SIGMA_SB = 5.670374419e-8      # W m^-2 K^-4
SOLAR_CONSTANT = 1361.0        # W m^-2

SURFACES = ("soil-like", "vegetation-like", "water-like")

# Notional band intervals, micrometres.  CHOSEN for this exercise.
BANDS = [
    ("blue", 0.45, 0.52),
    ("green", 0.52, 0.60),
    ("red", 0.63, 0.69),
    ("near-infrared", 0.76, 0.90),
    ("shortwave-infrared-1", 1.55, 1.75),
    ("shortwave-infrared-2", 2.08, 2.35),
    ("thermal-infrared", 10.3, 11.3),
]


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def reflectance(kind, lam_um):
    """SYNTHETIC spectral reflectance of a notional surface (0-1)."""
    lam = np.asarray(lam_um, dtype=float)
    step = lambda x0, w: 1.0 / (1.0 + np.exp(-(lam - x0) / w))
    gauss = lambda c, w: np.exp(-((lam - c) / w) ** 2)
    if kind == "soil-like":
        r = (0.36 + 0.20 * step(1.30, 0.15)
             - 0.13 * gauss(2.20, 0.06)
             - 0.06 * gauss(1.40, 0.05)
             - 0.45 * step(6.50, 0.25))
    elif kind == "vegetation-like":
        r = (0.04 + 0.46 * step(0.70, 0.03)
             - 0.16 * step(1.30, 0.20)
             - 0.10 * gauss(1.45, 0.05)
             - 0.12 * gauss(1.95, 0.07)
             - 0.20 * step(6.50, 0.25))
    elif kind == "water-like":
        r = (0.05 + 0.02 * gauss(0.48, 0.06)
             - 0.045 * step(0.75, 0.05)
             - 0.025 * step(6.50, 0.25))
    else:
        raise ValueError(f"unknown surface {kind!r}")
    return np.clip(r, 0.005, 0.95)


def planck(lam_um, T_K):
    lam_m = lam_um * 1e-6
    x = H_PLANCK * C_LIGHT / (lam_m * K_BOLTZ * T_K)
    return 2.0 * H_PLANCK * C_LIGHT ** 2 / lam_m ** 5 / np.expm1(x)


def planck_inverse_um(L, lam_um):
    """Brightness temperature [K] from spectral radiance L at wavelength lam_um."""
    lam_m = lam_um * 1e-6
    x = 2.0 * H_PLANCK * C_LIGHT ** 2 / (lam_m ** 5 * L)
    return H_PLANCK * C_LIGHT / (lam_m * K_BOLTZ * np.log1p(x))


def band_mean(kind, lo, hi, n=400):
    lam = np.linspace(lo, hi, n)
    return float(np.trapezoid(reflectance(kind, lam), lam) / (hi - lo))


def main():
    section("1. Energy conservation and the three optical regimes")
    print("For every surface and wavelength an opaque medium has tau = 0 and")
    print("rho + alpha = 1.  Three SYNTHETIC illustrations at 0.65 um:")
    print("   surface              rho      tau    alpha   rho+tau+alpha")
    for kind, rho, tau in (("soil-like", 0.36, 0.0), ("vegetation-like", 0.045, 0.0),
                           ("clear water (teaching tau)", 0.055, 0.02)):
        alpha = 1.0 - rho - tau
        print(f"  {kind:26s} {rho:6.3f}  {tau:6.3f}  {alpha:6.3f}   "
              f"{rho + tau + alpha:8.3f}")
    print("  An opaque surface is described by rho alone; a translucent one needs")
    print("  tau, and then Kirchhoff must be applied to (1 - rho - tau).")

    section("2. SYNTHETIC reflectance spectra: notional band means")
    print("Absorption features are Gaussian dips with (centre um, width um, depth):")
    print("  soil-like        (2.20, 0.06, 0.13) and (1.40, 0.05, 0.06)")
    print("  vegetation-like  (1.45, 0.05, 0.10) and (1.95, 0.07, 0.12)")
    print("  water-like       no notional feature, a monotone near-IR fall")
    hdr = "   surface              " + "".join(f"{n[:9]:>11s}" for n, _, _ in BANDS)
    print(hdr)
    for kind in SURFACES:
        vals = "".join(f"{band_mean(kind, lo, hi):11.3f}" for _, lo, hi in BANDS)
        print(f"   {kind:20s} {vals}")
    print("  (columns: " + ", ".join(n for n, _, _ in BANDS) + ")")

    section("3. Broadband albedo from a SYNTHETIC solar spectrum")
    lam = np.linspace(0.20, 6.0, 6000)
    B_sun = planck(0.20, 5772.0) * 0.0 + planck(lam, 5772.0)
    # Scale the Planck curve so that its integral is the solar constant.
    E_sun = B_sun / np.trapezoid(B_sun, lam * 1e-6) * SOLAR_CONSTANT
    print(f"  synthetic TOA spectral irradiance integrated over 0.20-6.0 um: "
          f"{np.trapezoid(E_sun, lam * 1e-6):.1f} W/m^2")
    print(f"  (fixed by construction to the solar constant {SOLAR_CONSTANT:.0f} W/m^2)")
    print("   surface              broadband albedo")
    for kind in SURFACES:
        rho = reflectance(kind, lam)
        alb = float(np.trapezoid(rho * E_sun, lam * 1e-6) / np.trapezoid(E_sun, lam * 1e-6))
        print(f"  {kind:22s} {alb:16.3f}")
    E_red = planck(lam, 4500.0)
    E_red = E_red / np.trapezoid(E_red, lam * 1e-6) * SOLAR_CONSTANT
    print("  Same surfaces under a reddened SYNTHETIC illumination (4500 K):")
    print("   surface              broadband albedo")
    for kind in SURFACES:
        rho = reflectance(kind, lam)
        alb = float(np.trapezoid(rho * E_red, lam * 1e-6) / np.trapezoid(E_red, lam * 1e-6))
        print(f"  {kind:22s} {alb:16.3f}")
    print("  The broadband albedo is a WEIGHTED mean: the same reflectance curve")
    print("  gives a different albedo under a different illumination spectrum.")

    section("4. Lambertian radiance L = rho E / pi")
    E_irr = 800.0                       # SYNTHETIC surface irradiance, W/m^2
    print(f"  irradiance E = {E_irr:.0f} W/m^2 (SYNTHETIC); rho from the band means")
    print("   surface              rho(red)   L(red)          rho(NIR)   L(NIR)")
    print("                                 W m^-2 sr^-1               W m^-2 sr^-1")
    for kind in SURFACES:
        rr = band_mean(kind, 0.63, 0.69)
        rn = band_mean(kind, 0.76, 0.90)
        print(f"  {kind:22s} {rr:8.3f}  {rr * E_irr / np.pi:12.3f}   {rn:8.3f}  "
              f"{rn * E_irr / np.pi:12.3f}")
    print("  Lambertian assumes radiance is independent of viewing angle and that")
    print("  the surface reflects all intercepted energy back into the hemisphere:")
    print("  integrating L cos(theta) over the hemisphere returns rho E, exactly.")

    section("5. Kirchhoff: emissivity of the opaque synthetic surfaces")
    lam_tir = 10.8
    print(f"   surface              rho({lam_tir:.1f} um)   emissivity = 1 - rho")
    for kind in SURFACES:
        rho = float(reflectance(kind, lam_tir))
        print(f"  {kind:22s} {rho:10.3f}   {1.0 - rho:18.3f}")
    print("  Kirchhoff's law for an opaque body in local thermodynamic equilibrium:")
    print("  eps(lambda) = 1 - rho(lambda).  It is a statement of energy conservation,")
    print("  not an empirical correlation.")

    section("6. Brightness temperature and the emissivity error")
    T_TRUE = 300.0
    lam_use = 10.8
    print(f"  true surface temperature T = {T_TRUE:.1f} K at lambda = {lam_use:.1f} um")
    print("   surface              eps_true   L_obs          T_b(eps=1)  "
          "T(eps=0.95)   error")
    print("                                 W m^-2 sr^-1 m^-1      K            K      K")
    for kind in SURFACES:
        eps_true = 1.0 - float(reflectance(kind, lam_use))
        L_obs = eps_true * planck(lam_use, T_TRUE)
        T_b = planck_inverse_um(L_obs, lam_use)
        T_assumed = planck_inverse_um(L_obs / 0.95, lam_use)
        print(f"  {kind:22s} {eps_true:8.3f}  {L_obs:13.4e}   {T_b:10.3f}  "
              f"{T_assumed:11.3f}  {T_assumed - T_TRUE:+6.2f}")
    print("  Reading a radiance as a temperature with eps = 1 gives a brightness")
    print("  temperature BELOW the true surface temperature; dividing the radiance by")
    print("  a wrong eps bias the retrieved temperature in the opposite direction.")

    section("7. Non-Lambertian geometry: the nadir-measurement bias")
    print("SYNTHETIC bidirectional model: a surface with a forward-scattering lobe.")
    print("   view zenith   directional rho   model used      albedo error")
    rho_dh = 0.30
    print("   (deg)")
    for theta_deg in (0.0, 30.0, 45.0, 60.0):
        th = np.deg2rad(theta_deg)
        rho_dir = rho_dh * (1.0 + 0.35 * np.cos(th) ** 2)
        err = (rho_dir - rho_dh) / rho_dh
        print(f"   {theta_deg:10.0f}   {rho_dir:14.4f}   {rho_dh:10.3f}   {err:+11.2%}")
    print("  Using a single directional reflectance as if it were the hemispherical")
    print("  reflectance is a BRDF assumption, and for an anisotropic surface it is")
    print("  simply wrong by a factor that depends on the view geometry.")

    section("8. Verification of the Planck inversion")
    print("Forward-model the retrieved temperature back to radiance and compare.")
    for kind in SURFACES:
        eps_true = 1.0 - float(reflectance(kind, lam_use))
        L_obs = eps_true * planck(lam_use, T_TRUE)
        T_inv = planck_inverse_um(L_obs, lam_use)
        L_back = planck(lam_use, T_inv)
        rel = abs(L_back - L_obs) / L_obs
        print(f"  {kind:22s} relative radiance closure error = {rel:.2e}")
    print("  Closure to ~1e-16 is the expected double-precision round trip: it tests")
    print("  the algebra of the inversion, not the physics of the radiance.")


if __name__ == "__main__":
    main()
