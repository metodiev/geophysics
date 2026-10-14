#!/usr/bin/env python3
"""The electromagnetic spectrum and the atmospheric sensing windows.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_spectrum_remote_sensing_demo.py

Everything here is SYNTHETIC or a standard physical constant.  The atmospheric
transmittance model is a *teaching* model built from Gaussian absorption
features whose centres, widths and depths are chosen in this file; it is not a
measured or published spectrum, and no real instrument or mission is named.

Contents
--------
1. Standard constants, with units.
2. Planck spectral radiance for a solar-temperature and an Earth-temperature
   blackbody.
3. Wien displacement: peak wavelength versus temperature.
4. The photon picture: wavelength -> frequency -> photon energy (eV).
5. Stefan-Boltzmann exitance for the same temperatures.
6. A SYNTHETIC atmospheric transmittance model and the windows it leaves open.
7. Rayleigh 1/lambda^4 scattering weight across the spectrum.
8. Solar-energy-weighted radiance available inside each window.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard physical constants (exact SI values where defined) --------------
H_PLANCK = 6.62607015e-34      # J s
C_LIGHT = 2.99792458e8         # m / s
K_BOLTZ = 1.380649e-23         # J / K
SIGMA_SB = 5.670374419e-8      # W m^-2 K^-4
WIEN_B = 2.897771955e-3        # m K
SOLAR_CONSTANT = 1361.0        # W m^-2, total solar irradiance at 1 au
EV_PER_JOULE = 1.0 / 1.602176634e-19

# --- SYNTHETIC atmospheric absorption features -------------------------------
# Each entry: (label, centre [um], width [um], optical depth at line centre).
# The values are CHOSEN teaching values, not measured absorptions.
ABSORBERS = [
    ("ozone-a", 0.25, 0.04, 3.0),
    ("ozone-b", 0.60, 0.05, 1.0),
    ("water-1", 0.94, 0.05, 1.2),
    ("water-2", 1.38, 0.09, 3.5),
    ("water-3", 1.87, 0.11, 3.8),
    ("water-4", 2.70, 0.20, 4.2),
    ("carbondioxide", 4.26, 0.20, 3.0),
    ("water-5", 6.30, 0.60, 4.5),
    ("ozone-c", 9.60, 0.70, 2.0),
    ("water-6", 12.0, 1.50, 1.0),
]

# Nominal windows to test, in micrometres.
WINDOWS = [
    ("visible", 0.40, 0.70),
    ("near-infrared", 0.75, 1.30),
    ("shortwave-infrared", 1.55, 1.75),
    ("midwave-infrared", 3.50, 4.10),
    ("thermal-infrared", 8.00, 13.0),
]


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def planck_spectral_radiance(lam_m, T_K):
    """Spectral radiance B_lambda(T) in W m^-2 sr^-1 m^-1."""
    x = H_PLANCK * C_LIGHT / (lam_m * K_BOLTZ * T_K)
    return 2.0 * H_PLANCK * C_LIGHT ** 2 / lam_m ** 5 / np.expm1(x)


def wien_peak_m(T_K):
    """Wien displacement law: wavelength of peak spectral radiance, in metres."""
    return WIEN_B / T_K


def optical_depth(lam_um):
    """SYNTHETIC vertical optical depth from the Gaussian feature table."""
    tau = np.zeros_like(lam_um, dtype=float)
    for _name, centre, width, depth in ABSORBERS:
        tau += depth * np.exp(-((lam_um - centre) / width) ** 2)
    tau += 0.02                                   # small synthetic continuum
    return tau


def transmittance(lam_um):
    """Beer-Lambert transmittance of the synthetic atmosphere."""
    return np.exp(-optical_depth(lam_um))


def main():
    section("1. Standard constants used throughout")
    print(f"Planck constant      h     = {H_PLANCK:.6e} J s")
    print(f"Speed of light       c     = {C_LIGHT:.6e} m/s")
    print(f"Boltzmann constant   k_B   = {K_BOLTZ:.6e} J/K")
    print(f"Stefan-Boltzmann     sigma = {SIGMA_SB:.6e} W/m^2/K^4")
    print(f"Wien displacement    b     = {WIEN_B:.9f} m K")
    print(f"Solar constant (1 au) S     = {SOLAR_CONSTANT:.0f} W/m^2")
    print(f"Derived: h c = {H_PLANCK * C_LIGHT:.7e} J m "
          f"= {H_PLANCK * C_LIGHT / 1.602176634e-19 * 1e6:.7f} eV um")
    print(f"Derived: x = 5(1-exp(-x)) root used by Wien: 4.965114")

    section("2. Planck spectral radiance B_lambda(T)")
    print("SYNTHETIC choice of temperatures is explicit; the constants are exact.")
    print("   T (K)    lambda (um)   B_lambda (W m^-2 sr^-1 m^-1)")
    for T_K, lam_um in ((5772.0, 0.50), (288.0, 10.0), (1200.0, 2.4), (220.0, 13.2)):
        B = planck_spectral_radiance(lam_um * 1e-6, T_K)
        print(f"  {T_K:7.0f}   {lam_um:10.2f}   {B:14.4e}")
    B_sun_peak = planck_spectral_radiance(wien_peak_m(5772.0), 5772.0)
    B_earth_peak = planck_spectral_radiance(wien_peak_m(288.0), 288.0)
    print("  note: at their respective Wien peaks the Sun's spectral radiance")
    print(f"  exceeds the Earth's by {B_sun_peak / B_earth_peak:.3e} "
          "(same units).")

    section("3. Wien displacement: peak wavelength versus temperature")
    print("   T (K)     lambda_peak (um)   band")
    for T_K, band in ((5772.0, "visible (solar)"), (1200.0, "shortwave IR (hot rock)"),
                      (400.0, "midwave IR"), (288.0, "thermal IR (Earth)"),
                      (220.0, "thermal IR (cold cloud)")):
        lam_um = wien_peak_m(T_K) * 1e6
        print(f"  {T_K:7.0f}   {lam_um:14.3f}   {band}")
    print(f"  Wien constant b = {WIEN_B:.9f} m K (exact); lambda_peak = b / T")

    section("4. Frequency and photon energy versus wavelength")
    print("   band                lambda (um)   nu (THz)   E (eV)")
    band_specs = [
        ("gamma-ray", 1.0e-6), ("X-ray", 1.0e-3), ("ultraviolet", 0.30),
        ("visible", 0.55), ("near-infrared", 1.00), ("shortwave-infrared", 1.65),
        ("midwave-infrared", 3.90), ("thermal-infrared", 10.0),
        ("microwave (radar)", 5.6e4), ("radio", 1.0e6),
    ]
    for name, lam_um in band_specs:
        lam_m = lam_um * 1e-6
        nu_hz = C_LIGHT / lam_m
        E_eV = H_PLANCK * nu_hz * EV_PER_JOULE
        print(f"  {name:18s}  {lam_um:10.3e}   {nu_hz / 1e12:8.3e}   {E_eV:9.4g}")
    print("  E = h nu = h c / lambda; 1 eV = 1.602176634e-19 J (exact).")

    section("5. Stefan-Boltzmann total exitance M = sigma T^4")
    print("   T (K)     M (W/m^2)     M / M_Earth")
    M_E = SIGMA_SB * 288.0 ** 4
    for T_K in (5772.0, 1200.0, 400.0, 288.0, 220.0):
        M = SIGMA_SB * T_K ** 4
        print(f"  {T_K:7.0f}   {M:11.1f}   {M / M_E:8.3e}")
    albedo = 0.30                       # SYNTHETIC planetary albedo
    absorbed = SOLAR_CONSTANT * (1.0 - albedo) / 4.0
    T_eff = (absorbed / SIGMA_SB) ** 0.25
    print(f"  Earth surface at 288 K emits M = {M_E:.1f} W/m^2.")
    print(f"  Absorbed solar flux per unit area, S(1-A)/4 with A = {albedo:.2f}, "
          f"= {absorbed:.1f} W/m^2.")
    print(f"  Radiating temperature that balances it, T_eff = (flux/sigma)^0.25 "
          f"= {T_eff:.1f} K.")
    print(f"  Surface minus radiating temperature = {288.0 - T_eff:.1f} K; that gap is")
    print("  the greenhouse effect, and it is why a single-band thermal image")
    print("  needs the atmosphere in its radiative-transfer model.")

    section("6. SYNTHETIC atmospheric transmittance and the sensing windows")
    print("Absorption features (teaching values, NOT measured):")
    print("   label            centre (um)   width (um)   depth (optical depth)")
    for name, centre, width, depth in ABSORBERS:
        print(f"  {name:14s}  {centre:11.2f}   {width:10.2f}   {depth:8.1f}")
    lam = np.linspace(0.30, 16.0, 6000)
    tau_v = optical_depth(lam)
    tr_v = transmittance(lam)
    print(f"\n  mean vertical transmittance over 0.30-16.0 um = {tr_v.mean():.3f}")
    print("   window               range (um)     mean transmittance   opaque fraction")
    for name, lo, hi in WINDOWS:
        m = (lam >= lo) & (lam <= hi)
        tm = tr_v[m].mean()
        frac_opaque = float(np.mean(tau_v[m] > 1.0))
        print(f"  {name:20s} {lo:6.2f}-{hi:5.2f}   {tm:14.3f}   {frac_opaque:13.3f}")
    print("  A window is a wavelength interval the atmosphere leaves substantially")
    print("  open; it is the reason any surface-sensing band exists at all.")

    section("7. Rayleigh 1/lambda^4 scattering weight")
    lam_ref = 0.55e-6
    print("   band                lambda (um)   relative Rayleigh weight")
    for name, lam_um in band_specs[2:8]:
        weight = (lam_um * 1e-6 / lam_ref) ** -4.0
        print(f"  {name:18s}  {lam_um:10.3e}   {weight:22.4e}")
    print("  Relative to 0.55 um.  The 1/lambda^4 law makes blue skylight ~"
          f"{(0.45/0.65) ** -4:.1f}x")
    print("  stronger than red, which is why a blue sky and a red sunset are the")
    print("  same physics.")

    section("8. Solar-energy-weighted radiance inside each window")
    print("   window               range (um)   solar radiance (W m^-2 sr^-1)   fraction of 0.3-4 um")
    m_solar = (lam >= 0.30) & (lam <= 4.0)
    B_sun = planck_spectral_radiance(lam * 1e-6, 5772.0)
    tot = np.trapezoid((B_sun * tr_v)[m_solar], lam[m_solar] * 1e-6)
    for name, lo, hi in WINDOWS:
        if hi > 4.0:
            continue
        m = (lam >= lo) & (lam <= hi)
        val = np.trapezoid((B_sun * tr_v)[m], lam[m] * 1e-6)
        print(f"  {name:20s} {lo:6.2f}-{hi:5.2f}   {val:28.4e}   {val / tot:18.4f}")
    print(f"  total in 0.30-4.0 um after atmospheric absorption = {tot:.4e} W m^-2 sr^-1")
    print("  (an integral of a SYNTHETIC transmittance times the Planck function of")
    print("  a 5772 K blackbody; it is a teaching number, not a measured irradiance).")

    section("9. Transmittance at candidate diagnostic wavelengths")
    print("   lambda (um)   synthetic transmittance   optical depth")
    for lam_um in (0.55, 0.66, 1.40, 1.65, 2.20, 2.70, 11.0):
        tau = float(optical_depth(np.array([lam_um]))[0])
        print(f"  {lam_um:11.2f}   {np.exp(-tau):23.3f}   {tau:13.3f}")
    print("  A wavelength is usable only if it is BOTH diagnostic and transmitted;")
    print("  the 1.40 um entry is an example of a diagnostic feature the synthetic")
    print("  atmosphere blocks almost completely.")


if __name__ == "__main__":
    main()
