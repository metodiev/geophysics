#!/usr/bin/env python3
"""Thermal infrared remote sensing: land surface temperature and heat flow.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermal_infrared_demo.py

Everything is SYNTHETIC.  The bands, the atmospheric transmittances, the layer
temperature, the thermal conductivity and diffusivity and the flux anomalies are
all chosen teaching values in this file.  No real band, sensor, mission, borehole
or heat-flow measurement is represented.

Contents
--------
1. Band-averaged Planck radiance and its temperature sensitivity.
2. Brightness temperature and the temperature-emissivity degeneracy.
3. Single-band land surface temperature and the emissivity error.
4. A synthetic split-window retrieval, fitted by least squares.
5. Thermal skin depth, damping and phase lag of a periodic surface temperature.
6. Conductive heat flow, the geothermal gradient and surface temperature anomalies.
7. The flux anomaly a stated radiometric resolution can detect.
8. Verification of the band integration against the band-centre approximation.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

H_PLANCK = 6.62607015e-34
C_LIGHT = 2.99792458e8
K_BOLTZ = 1.380649e-23

# --- SYNTHETIC instrument and atmosphere -------------------------------------
BANDS_UM = ((8.5, 9.5), (10.3, 11.3), (11.5, 12.5))   # notional band intervals
TAU_BANDS = (0.62, 0.80, 0.68)                        # SYNTHETIC transmittances
T_ATM = 280.0                                         # isothermal layer, K
EPS_BANDS = (0.955, 0.950, 0.945)                     # SYNTHETIC emissivities
NE_DT = 0.14                                          # K, from module 17-01

# --- SYNTHETIC ground properties ---------------------------------------------
CONDUCTIVITY = 2.5            # W m^-1 K^-1
DIFFUSIVITY = 1.0e-6          # m^2 s^-1
ANOMALY_DEPTH = 25.0          # m, thickness over which a flux anomaly is carried


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def planck(lam_um, T_K):
    lam_m = np.asarray(lam_um, dtype=float) * 1e-6
    x = H_PLANCK * C_LIGHT / (lam_m * K_BOLTZ * T_K)
    return 2.0 * H_PLANCK * C_LIGHT ** 2 / lam_m ** 5 / np.expm1(x)


def planck_inverse_um(L, lam_um):
    lam_m = np.asarray(lam_um, dtype=float) * 1e-6
    x = 2.0 * H_PLANCK * C_LIGHT ** 2 / (lam_m ** 5 * L)
    return H_PLANCK * C_LIGHT / (lam_m * K_BOLTZ * np.log1p(x))


def band_radiance(lo_um, hi_um, T_K, n=400):
    """Band-averaged Planck radiance over [lo, hi] in W m^-2 sr^-1 m^-1."""
    lam = np.linspace(lo_um, hi_um, n)
    return float(np.trapezoid(planck(lam, T_K), lam) / (hi_um - lo_um))


def main():
    section("1. Band-averaged Planck radiance and dL/dT")
    print("   T (K)   L(8.5-9.5)   L(10.3-11.3)   L(11.5-12.5)   dL/dT (10.3-11.3)")
    print("                    W m^-2 sr^-1 m^-1                 W m^-2 sr^-1 m^-1 K^-1")
    for T in (260.0, 280.0, 300.0, 320.0):
        Ls = [band_radiance(lo, hi, T) for lo, hi in BANDS_UM]
        centre = 0.5 * (BANDS_UM[1][0] + BANDS_UM[1][1])
        dLdT = Ls[1] * H_PLANCK * C_LIGHT / (centre * 1e-6 * K_BOLTZ * T ** 2)
        print(f"  {T:6.0f}   {Ls[0]:.5e}   {Ls[1]:.5e}   {Ls[2]:.5e}   {dLdT:.5e}")
    print("  dL/dT is computed from the Wien-limit form dL/dT = L hc/(lambda k T^2)")
    print("  evaluated at the band centre.  It grows steeply with temperature, so the")
    print("  radiometric resolution of a thermal instrument improves over a hot scene.")

    section("2. Brightness temperature and the T-emissivity degeneracy")
    lam = 10.8
    T0, eps0 = 300.0, 0.950
    L_obs = eps0 * planck(lam, T0)
    print(f"  observed radiance {L_obs:.4e} W m^-2 sr^-1 m^-1 at {lam} um")
    print(f"  produced by SYNTHETIC T = {T0:.1f} K with emissivity {eps0:.3f}")
    print("   assumed eps   implied T (K)   (T - T0)   radiance check")
    for eps in (0.90, 0.93, 0.95, 0.97, 1.00):
        T_imp = planck_inverse_um(L_obs / eps, lam)
        print(f"  {eps:12.3f}   {T_imp:12.3f}   {T_imp - T0:+8.3f}   "
              f"{eps * planck(lam, T_imp):.4e}")
    sens = lam * 1e-6 * K_BOLTZ * T0 ** 2 / (H_PLANCK * C_LIGHT)
    print(f"  sensitivity dT/dln(eps) = lambda k T^2/(hc) = {sens:.2f} K")
    print("  EVERY row reproduces the same radiance: temperature and emissivity are")
    print("  degenerate in a single band, and only the product eps x B(T) is measured.")
    print(f"  A 1% emissivity error is worth {sens * 0.01:.2f} K, and a 5% error "
          f"{sens * 0.05:.2f} K -- on the order of the phenomena being studied.")

    section("3. Single-band retrieval with an assumed emissivity")
    T_true = 305.0
    eps_true = 0.945
    L = eps_true * planck(lam, T_true)
    print(f"  true T = {T_true:.1f} K, true eps = {eps_true:.3f} at {lam} um")
    print(f"  measured radiance L = {L:.4e} W m^-2 sr^-1 m^-1 (SYNTHETIC)")
    print("   assumed eps   retrieved T (K)   error (K)")
    for eps_a in (0.900, 0.920, 0.945, 0.970, 0.990):
        T_r = planck_inverse_um(L / eps_a, lam)
        print(f"  {eps_a:12.3f}   {T_r:15.3f}   {T_r - T_true:+8.3f}")
    print("  The retrieval is unbiased only when the assumed emissivity is exactly")
    print("  right.  Because real emissivity maps are uncertain at the 1-3% level,")
    print("  a single-band product carries a systematic error of 0.7-2 K that is not")
    print("  visible in any per-pixel uncertainty estimate.")

    section("4. A synthetic split-window retrieval")
    print("  two thermal bands, SYNTHETIC transmittances "
          f"{TAU_BANDS[1]:.2f} and {TAU_BANDS[2]:.2f}")
    print("  (a more and a less transparent band in the same atmospheric window)")
    Ts_grid = np.linspace(280.0, 320.0, 41)
    Tb1, Tb2 = [], []
    for Ts in Ts_grid:
        Tb = []
        for k in (1, 2):
            lo, hi = BANDS_UM[k]
            centre = 0.5 * (lo + hi)
            eps = EPS_BANDS[k]
            tau = TAU_BANDS[k]
            L_g = eps * planck(centre, Ts) + (1.0 - eps) * planck(centre, T_ATM)
            L_s = tau * L_g + (1.0 - tau) * planck(centre, T_ATM)
            Tb.append(planck_inverse_um(L_s, centre))
        Tb1.append(Tb[0])
        Tb2.append(Tb[1])
    Tb1 = np.array(Tb1)
    Tb2 = np.array(Tb2)
    diff = Tb1 - Tb2
    design = np.column_stack([diff, np.ones_like(diff)])
    coef, *_ = np.linalg.lstsq(design, Ts_grid - Tb1, rcond=None)
    Ts_hat = Tb1 + design @ coef
    resid = Ts_hat - Ts_grid
    print("  fit Ts = T_b1 + a (T_b1 - T_b2) + b over 280-320 K:")
    print(f"  a = {coef[0]:+.5f}, b = {coef[1]:+.5f}")
    print(f"  residual: max |error| = {np.abs(resid).max():.4f} K, "
          f"RMSE = {np.sqrt(np.mean(resid ** 2)):.4f} K")
    print("  (the coefficients are fitted to THIS synthetic atmosphere; a real")
    print("  retrieval derives them from a radiative-transfer training set and its")
    print("  residual is set by the atmosphere's departure from the fitted form)")
    single = Tb1 - Ts_grid
    print(f"  single-band brightness temperature bias over the same range: "
          f"{single.min():+.3f} to {single.max():+.3f} K")
    print("  The split window does not remove the emissivity problem; it converts a")
    print("  large, systematic, temperature-dependent bias into a small residual,")
    print("  because the two bands share the surface emissivity but differ in tau.")
    print(f"  Check the difference T_b1 - T_b2 across the range: "
          f"{np.mean(Tb1 - Tb2):.3f} K on average.")

    section("5. Thermal skin depth, damping and phase lag")
    print(f"  SYNTHETIC thermal diffusivity alpha = {DIFFUSIVITY:.1e} m^2/s")
    print("   period          angular freq (s^-1)   skin depth (m)   "
          "amplitude at 0.30 m")
    for name, period in (("diurnal", 86400.0), ("annual", 365.25 * 86400.0)):
        omega = 2.0 * np.pi / period
        delta = np.sqrt(2.0 * DIFFUSIVITY / omega)
        amp = np.exp(-0.30 / delta)
        print(f"  {name:12s}   {omega:20.4e}   {delta:14.4f}   {amp:17.4f}")
    omega_d = 2.0 * np.pi / 86400.0
    delta_d = np.sqrt(2.0 * DIFFUSIVITY / omega_d)
    print("  A 10 K diurnal surface amplitude becomes "
          f"{10 * np.exp(-0.30 / delta_d):.3f} K at 0.30 m depth.")
    lag_h = 0.30 * np.sqrt(omega_d / (2.0 * DIFFUSIVITY)) / omega_d / 3600.0
    print(f"  phase lag at 0.30 m: {lag_h:.3f} h "
          f"(the temperature peak arrives later than the surface peak)")
    print("  Skin depth scales as sqrt(period): the annual wave penetrates about")
    print(f"  sqrt(365.25) = {np.sqrt(365.25):.2f} times deeper than the diurnal one,")
    print("  which is why long-period surface temperature changes reach measurable")
    print("  depths and short ones do not.")

    section("6. Conductive heat flow and surface temperature anomalies")
    print(f"  Fourier's law q = -k dT/dz with SYNTHETIC k = {CONDUCTIVITY:.2f} W m^-1 K^-1")
    print("   gradient (K/km)   dT/dz (K/m)   heat flow q (W/m^2)")
    for g in (10.0, 20.0, 25.0, 40.0, 60.0):
        dz = g / 1000.0
        print(f"  {g:16.1f}   {dz:12.5f}   {CONDUCTIVITY * dz:16.5f}")
    print("  A commonly quoted continental reference value of 0.065 W/m^2 (used here")
    print(f"  for scale only, not measured in this module) gives {0.065 / CONDUCTIVITY * 1000:.1f} K/km.")
    print("  A heat-flow ANOMALY appears at the surface as a temperature anomaly only")
    print("  when it crosses a layer of non-zero thermal resistance:")
    print("   flux anomaly (W/m^2)   surface dT across 25 m (K)   equivalent NE-dT")
    for dq in (0.05, 0.10, 0.30, 1.00):
        dT = dq * ANOMALY_DEPTH / CONDUCTIVITY
        print(f"  {dq:20.2f}   {dT:28.2f}   {dT / NE_DT:16.1f} sigma")
    print("  This is the physical reason geothermal remote sensing is hard: even a")
    print("  large flux anomaly produces a modest surface temperature signature.")

    section("7. The flux anomaly a stated radiometric resolution can detect")
    print(f"  NE-delta-T = {NE_DT:.2f} K (from the synthetic instrument of module 17-01)")
    print("   needed surface dT (K)   minimum detectable flux anomaly (W/m^2)")
    for n_sigma in (1.0, 2.0, 3.0, 5.0):
        dT = n_sigma * NE_DT
        dq = dT * CONDUCTIVITY / ANOMALY_DEPTH
        print(f"  {dT:21.2f}   {dq:38.3f}")
    print("  Detection therefore requires either a large flux anomaly, a shallow")
    print("  anomaly (small ANOMALY_DEPTH), or averaging over many pixels.  Averaging")
    print("  reduces the noise but NOT the confounds: emissivity variation, vegetation,")
    print("  topography, soil moisture and cloud all change surface temperature by")
    print("  more than the geothermal signal, so detection is a joint inversion, not a")
    print("  threshold test.")

    section("8. Verification: band integration against the band centre")
    print("   T (K)   integrated L(10.3-11.3)   centre value   relative difference")
    for T in (280.0, 300.0, 320.0):
        lo, hi = BANDS_UM[1]
        integrated = band_radiance(lo, hi, T)
        centre = planck(0.5 * (lo + hi), T)
        print(f"  {T:6.0f}   {integrated:.5e}   {centre:.5e}   "
              f"{(integrated - centre) / integrated:+.4%}")
    print("  The band-centre value differs from the band average by a fraction of a")
    print("  per cent over a 1 um band: usable for teaching, NOT usable for a")
    print("  retrieval whose error budget is 0.1 K.  Operational retrievals convolve")
    print("  the Planck function with the measured spectral response.")


if __name__ == "__main__":
    main()
