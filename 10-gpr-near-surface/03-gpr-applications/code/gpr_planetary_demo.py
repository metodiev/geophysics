#!/usr/bin/env python3
"""Planetary radar sounding: bandwidth and resolution, the Fresnel footprint,
surface clutter geometry, the permittivity ambiguity and ionospheric delay.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_planetary_demo.py

All models and data in this module are SYNTHETIC.  The orbital altitudes,
target depths, ionospheric densities and subsurface permittivities are chosen
teaching values, not measurements from any planetary mission.  Physical
constants, the permittivity of water and the plasma-frequency constant are
labelled as such.

Contents
--------
1. Range resolution against bandwidth, in vacuum and in a medium.
2. The Fresnel footprint of a nadir sounder at orbital altitude.
3. Surface clutter: the off-nadir surface distance that has the same delay as
   a subsurface echo.
4. The permittivity ambiguity: two models with the same echo time and the same
   echo amplitude, and their different depths.
5. Ionospheric group delay and dispersion, with two independent formulas
   compared.
6. The detection limit: attenuation against clutter.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_M_S = 2.99792458e8        # m/s (exact)
C_M_NS = 0.299792458        # m/ns (exact)
EPS_WATER = 80.1            # water, 20 C (standard value)
EPS_ICE = 3.17              # cold ice (standard value)
PLASMA_CONST = 8.98         # f_p[Hz] = 8.98 sqrt(n_e[m^-3])  (exact constant)
IONO_CONST = 40.3           # dispersion constant, m^3 s^-2 (standard constant)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def v_of_eps(eps):
    return C_M_NS / np.sqrt(eps)


def reflection_coeff(eps1, eps2):
    return (np.sqrt(eps1) - np.sqrt(eps2)) / (np.sqrt(eps1) + np.sqrt(eps2))


def main():
    section("1. Range resolution against bandwidth")
    print("  A pulse of bandwidth B separates two echoes a two-way time 1/B")
    print("  apart, so the range resolution is  dr = c / (2 B) in vacuum and")
    print("  dr / sqrt(eps_r) inside a medium (both the speed and the")
    print("  wavelength shrink).")
    print("  B (MHz)   dr vacuum (m)   dr in ice, eps 3.17 (m)   dr in water (m)")
    for b_mhz in (1.0, 10.0, 100.0):
        b = b_mhz * 1e6
        dr = C_M_S / (2.0 * b)
        print(f"  {b_mhz:7.0f}   {dr:13.1f}   {dr / np.sqrt(EPS_ICE):24.1f}   "
              f"{dr / np.sqrt(EPS_WATER):15.1f}")
    print("  Resolution and penetration pull in opposite directions: a deep")
    print("  sounding radar is a low-bandwidth, low-frequency instrument, and it")
    print("  buys depth by giving up the ability to see thin layers.")

    section("2. The Fresnel footprint at orbital altitude")
    print("  For a monostatic nadir sounder the first Fresnel zone radius is")
    print("  r_f = sqrt(lambda h / 2), with h the altitude.")
    h_km = 300.0
    h = h_km * 1e3
    print(f"  SYNTHETIC altitude h = {h_km:.0f} km")
    print("  f (MHz)   lambda (m)   r_f (m)   r_f (km)   two-way time to surface (us)")
    for f_mhz in (5.0, 20.0, 100.0):
        lam = C_M_S / (f_mhz * 1e6)
        rf = np.sqrt(lam * h / 2.0)
        print(f"  {f_mhz:7.0f}   {lam:10.2f}   {rf:8.0f}   {rf / 1e3:8.3f}   "
              f"{2 * h / C_M_S * 1e6:27.1f}")
    print("  The footprint is kilometres wide, so a nadir sounder averages the")
    print("  surface over that circle; the along-track resolution is recovered")
    print("  only by coherent (synthetic-aperture) processing of the Doppler")
    print("  history of each echo.")

    section("3. Surface clutter: the same delay, a different place")
    print("  On a flat surface, the off-nadir distance x whose surface echo has")
    print("  the same extra delay as a subsurface echo at depth d is")
    print("      x = sqrt(2 h d sqrt(eps_r))")
    print("  because the extra path to x is x^2/(2h) and the extra path down to d")
    print("  is 2 d sqrt(eps_r) (one way each, doubled for the round trip).")
    print("  d (m)   x for eps = 3.17 (km)   x for eps = 80.1 (km)")
    for d in (10.0, 100.0, 1000.0):
        for eps in (EPS_ICE, EPS_WATER):
            pass
        x_ice = np.sqrt(2.0 * h * d * np.sqrt(EPS_ICE))
        x_water = np.sqrt(2.0 * h * d * np.sqrt(EPS_WATER))
        print(f"  {d:5.0f}   {x_ice / 1e3:22.2f}   {x_water / 1e3:21.2f}")
    print("  A subsurface echo at 100 m therefore sits at the same delay as a")
    print("  surface echo from roughly 10 km off nadir.  Range alone cannot tell")
    print("  them apart; the Doppler history of the two differs, which is why")
    print("  these radars are coherent and why clutter modelling is a required")
    print("  part of any interpretation.")

    section("4. Two models, one observation")
    twt_us = 20.0
    print(f"  SYNTHETIC observation: a two-way time of {twt_us:.1f} us and an")
    print("  attenuation-corrected bed echo amplitude.  The time fixes the")
    print("  PRODUCT d sqrt(eps_r), not d.")
    alpha_a, eps_a = 0.010, 3.17
    eps_b = 4.00
    d_a = twt_us * 1e-6 * C_M_S / (2.0 * np.sqrt(eps_a))
    d_b = twt_us * 1e-6 * C_M_S / (2.0 * np.sqrt(eps_b))
    alpha_b = alpha_a * d_a / d_b
    print("  model   eps_r   d (m)   one-way alpha (dB/m)   two-way loss (dB)")
    for name, eps, d, a in (("A", eps_a, d_a, alpha_a), ("B", eps_b, d_b, alpha_b)):
        print(f"  {name:7s} {eps:6.2f}   {d:6.0f}   {a:21.4f}   {2 * a * d:18.2f}")
    print(f"  Both models reproduce the SAME time and the SAME echo amplitude, and")
    print(f"  their depths differ by {abs(d_a - d_b):.0f} m "
          f"({abs(d_a - d_b) / d_a * 100:.1f}%).  The depth is only as good as")
    print("  the permittivity, and the permittivity is only as good as the")
    print("  absolutely calibrated surface echo.")

    section("5. Ionospheric delay: two independent formulas")
    n_e = 1.0e11            # SYNTHETIC peak electron density, m^-3
    l_iono = 1.0e5          # SYNTHETIC ionospheric thickness, m
    f_hz = 20.0e6           # SYNTHETIC carrier, Hz
    b_hz = 10.0e6           # SYNTHETIC bandwidth, Hz
    fp = PLASMA_CONST * np.sqrt(n_e)
    tec = n_e * l_iono
    print(f"  SYNTHETIC ionosphere: n_e = {n_e:.2e} m^-3 over {l_iono / 1e3:.0f} km")
    print(f"  -> plasma frequency f_p = {fp / 1e6:.3f} MHz (f_p = 8.98 sqrt(n_e))")
    print(f"  -> total electron content TEC = {tec:.2e} m^-2")
    delay_slab = 0.5 * (fp / f_hz) ** 2 * l_iono
    delay_tec = IONO_CONST * tec / f_hz ** 2
    print(f"  excess path from the slab expansion  (1/2)(f_p/f)^2 L = "
          f"{delay_slab:8.1f} m")
    print(f"  excess path from the standard TEC form  40.3 TEC / f^2 = "
          f"{delay_tec:8.1f} m")
    print(f"  the two agree to {abs(delay_slab - delay_tec) / delay_tec * 100:.2f}%, "
          f"which is the check")
    print("  that the constants used here are consistent with each other.")
    d_group = 2.0 * delay_tec / C_M_S * 1e6
    print(f"  the round-trip group delay is {d_group:.1f} us, i.e. a range bias of")
    print(f"  {delay_tec:.0f} m.  The surface and the bed echoes share it, so a")
    print("  THICKNESS is unaffected while an absolute RANGE is not.")
    f1, f2 = f_hz - b_hz / 2.0, f_hz + b_hz / 2.0
    spread_m = IONO_CONST * tec * (1.0 / f1 ** 2 - 1.0 / f2 ** 2)
    print(f"  dispersion across the band {f1 / 1e6:.0f}-{f2 / 1e6:.0f} MHz: "
          f"{spread_m:.0f} m of differential")
    print(f"  delay, against a {C_M_S / (2.0 * b_hz):.1f} m range resolution.")
    print("  Uncorrected, the ionosphere smears one interface into a range of")
    print("  apparent depths; these radars therefore apply a phase correction")
    print("  derived from the same echoes.")

    section("6. What actually limits detection: attenuation or clutter?")
    alpha_db_m = 0.010      # SYNTHETIC one-way absorption in cold ice
    loss_limited = 60.0 / (2.0 * alpha_db_m)
    print(f"  SYNTHETIC one-way absorption {alpha_db_m:.3f} dB/m -> a 60 dB")
    print(f"  two-way budget is spent at {loss_limited:.0f} m.  In cold, dry")
    print("  material absorption is not the binding limit at depth; the")
    print("  surface-clutter window of Section 3 is.  The reverse is true in")
    print("  warm or wet material, where absorption removes the echo first.")
    print("  Neither limit is a property of the radar; both are properties of")
    print("  the target and of the surface above it.")


if __name__ == "__main__":
    main()
