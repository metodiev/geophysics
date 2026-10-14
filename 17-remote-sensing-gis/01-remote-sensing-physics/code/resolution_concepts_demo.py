#!/usr/bin/env python3
"""The four resolutions: spatial, spectral, temporal and radiometric.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resolution_concepts_demo.py

Everything is SYNTHETIC.  The instrument is a teaching geometry defined entirely
by the parameters below (altitude, aperture, detector pitch, slit width, swath,
orbit rate, bit depth).  No real instrument, mission or orbit is represented.

Contents
--------
1. Ground sample distance from altitude and instantaneous field of view.
2. The diffraction limit and the ratio GSD / diffraction spot.
3. Sampling and Nyquist: when the detector pitch undersamples the optics.
4. Modulation transfer function of the optics and the detector.
5. Spectral resolution from a grating dispersion and a slit width.
6. Spectral sampling ratio: band width against band spacing.
7. Temporal resolution: the equatorial revisit of a single swath.
8. Radiometric resolution: quantisation, SNR and NE-delta-T.
9. The spatial-spectral-radiometric trade, quantified.
10. Mixed pixels: the detectable fractional cover of a thermal anomaly.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

H_PLANCK = 6.62607015e-34
C_LIGHT = 2.99792458e8
K_BOLTZ = 1.380649e-23
R_EARTH = 6371.0e3            # m, mean Earth radius (standard)

# --- SYNTHETIC instrument definition (all chosen teaching values) ------------
ALTITUDE_M = 700.0e3          # orbit altitude
APERTURE_M = 0.30             # primary aperture diameter
IFOV_RAD = 10.0e-6            # detector instantaneous field of view
PITCH_RAD = 12.0e-6           # detector pitch (centre-to-centre spacing)
FOCAL_M = 2.0                 # effective focal length
SWATH_M = 100.0e3             # swath width for the revisit example
REVISIT_SWATH_M = 2900.0e3    # wide-swath alternative
ORBITS_PER_DAY = 14.3         # SYNTHETIC orbit rate, chosen
BIT_DEPTH = 12                # radiometric quantisation bits
L_MAX = 5.0e7                 # W m^-2 sr^-1 m^-1, full-scale radiance
NE_DL = 2.0e4                 # W m^-2 sr^-1 m^-1, noise-equivalent radiance


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def planck(lam_um, T_K):
    lam_m = lam_um * 1e-6
    x = H_PLANCK * C_LIGHT / (lam_m * K_BOLTZ * T_K)
    return 2.0 * H_PLANCK * C_LIGHT ** 2 / lam_m ** 5 / np.expm1(x)


def planck_inverse_um(L, lam_um):
    """Brightness temperature [K] from a spectral radiance L at lam_um."""
    lam_m = lam_um * 1e-6
    x = 2.0 * H_PLANCK * C_LIGHT ** 2 / (lam_m ** 5 * L)
    return H_PLANCK * C_LIGHT / (lam_m * K_BOLTZ * np.log1p(x))


def main():
    section("1. Ground sample distance from altitude and IFOV")
    print(f"  altitude H = {ALTITUDE_M / 1e3:.0f} km, IFOV = {IFOV_RAD * 1e6:.1f} urad")
    gsd = ALTITUDE_M * IFOV_RAD
    print(f"  GSD = H x IFOV = {gsd:.3f} m")
    print(f"  detector pitch {PITCH_RAD * 1e6:.1f} urad -> pitch on the ground "
          f"= {ALTITUDE_M * PITCH_RAD:.3f} m")
    print(f"  Nyquist frequency from the pitch = 1/(2 x {ALTITUDE_M * PITCH_RAD:.3f} m)"
          f" = {1.0 / (2 * ALTITUDE_M * PITCH_RAD):.5f} cycles/m")
    print("  GSD is a GEOMETRIC quantity: it says nothing about whether the")
    print("  optical system can actually resolve a feature that size.")

    section("2. The diffraction limit and GSD / diffraction spot")
    print("   lambda (um)   Airy spot on ground (m)   GSD / spot")
    for lam_um in (0.45, 0.55, 0.66, 0.86, 1.65, 10.8):
        spot = 1.22 * lam_um * 1e-6 * ALTITUDE_M / APERTURE_M
        print(f"  {lam_um:11.2f}   {spot:25.3f}   {gsd / spot:11.3f}")
    print(f"  Airy first-zero diameter = 1.22 lambda H / D with D = {APERTURE_M:.2f} m.")
    print("  The incoherent diffraction cut-off frequency is f_c = D / (lambda H);")
    print("  the Airy spot is 1.22 / f_c wide.  Where GSD/spot is near or below 1 the")
    print("  geometric GSD is a fiction: the aperture, not the detector, sets the")
    print("  smallest resolvable feature.")

    section("3. Sampling and Nyquist")
    f_nyq = 1.0 / (2.0 * ALTITUDE_M * PITCH_RAD)
    print(f"  detector pitch on the ground = {ALTITUDE_M * PITCH_RAD:.3f} m")
    print(f"  Nyquist frequency            = 1/(2 x pitch) = {f_nyq:.5f} cycles/m")
    print("   lambda (um)   f_c = D/(lambda H)   f_c / f_Nyquist   sampling")
    for lam_um in (0.45, 0.55, 0.86, 1.65, 10.8):
        f_cut = APERTURE_M / (lam_um * 1e-6 * ALTITUDE_M)
        ratio = f_cut / f_nyq
        verdict = "OK" if ratio <= 1.0 else "ALIASED"
        print(f"  {lam_um:11.2f}   {f_cut:18.5f}   {ratio:16.2f}   {verdict}")
    print("  Nyquist: content above 1/(2 pitch) cannot be represented and folds back")
    print("  as a false low-frequency pattern.  The design rule is to place the")
    print("  optical cut-off at or below the sampling Nyquist frequency, which here")
    print("  holds only in the thermal band.  In the visible this design is")
    print("  undersampled and must rely on the optical MTF to suppress aliasing.")

    section("4. Contrast at the design's own Nyquist frequency")
    lam_um = 0.66
    f_c = APERTURE_M / (lam_um * 1e-6 * ALTITUDE_M)
    print(f"  lambda = {lam_um} um, optical cut-off f_c = {f_c:.5f} cycles/m")
    print("  MTF_optics(f) = 1 - f/f_c (cut-off-limited approximation);")
    print("  MTF_detector(f) = sinc(f w) for a rectangular pixel of width w = pitch.")
    print("  At every design's own Nyquist frequency f = 1/(2w), f w = 1/2, so the")
    print("  detector MTF is always sinc(0.5) = 0.6366.  What changes is the optics:")
    print("   pitch w (m)   Nyquist (cyc/m)   MTF_optics   net contrast")
    for w_m in (16.0, 8.4, 4.0, 2.0, 1.879, 1.0):
        f_n = 1.0 / (2.0 * w_m)
        m_opt = max(0.0, 1.0 - f_n / f_c)
        print(f"  {w_m:11.3f}   {f_n:15.5f}   {m_opt:11.4f}   "
              f"{m_opt * float(np.sinc(0.5)):11.4f}")
    print("  Coarser pixels keep more contrast AT their Nyquist frequency, but that")
    print("  frequency is lower, so the finest recoverable wavelength, 2w, is worse.")
    print("  Resolution and contrast are two different numbers, and the system MTF is")
    print("  the product of its parts: improving one part alone does not help once")
    print("  another dominates.")

    section("5. Spectral resolution from a grating")
    groove_m = 1.0 / 100.0e3          # 100 lines/mm -> groove spacing
    order = 1
    slen = 0.20                       # m, illuminated grating width -> N = slen/g
    n_grooves = slen / groove_m
    lam0 = 0.55
    m_spectral = order * n_grooves
    print(f"  grating groove spacing d = {groove_m * 1e6:.2f} um ({1 / groove_m / 1e3:.0f} lines/mm)")
    print(f"  illuminated width s = {slen:.2f} m -> N = {n_grooves:.0f} grooves")
    print(f"  resolving power at order m = {order}: R = m N = {m_spectral:.0f}")
    print(f"  at lambda = {lam0:.2f} um: Delta lambda = lambda / R = "
          f"{lam0 / m_spectral * 1e3:.6f} nm")
    print("  This is the DIFFRACTION-limited spectral resolution; a finite slit or")
    print("  detector element usually makes the achieved value coarser.")

    section("6. Spectral sampling ratio")
    print("   band FWHM (nm)   band spacing (nm)   FWHM/spacing   sampling")
    for fwhm, spacing in ((10.0, 10.0), (20.0, 10.0), (5.0, 10.0), (10.0, 30.0)):
        r = fwhm / spacing
        verdict = "contiguous" if abs(r - 1.0) < 1e-9 else (
            "oversampled" if r < 1.0 else "undersampled")
        print(f"  {fwhm:15.1f}   {spacing:17.1f}   {r:12.2f}   {verdict}")
    print("  A band response narrower than the spacing leaves gaps (undersampling);")
    print("  wider than the spacing overlaps the neighbours.  Both change what a")
    print("  band ratio means, and neither is a defect in itself.")

    section("7. Temporal resolution: equatorial revisit")
    print("  Single satellite, single swath, no pointing: the equator is covered in")
    print("  T_revisit = 2 pi R_E / (N_orbits_per_day x W) days.")
    print(f"  N = {ORBITS_PER_DAY:.1f} orbits/day, R_E = {R_EARTH / 1e3:.0f} km")
    print("   swath (km)   revisit (days)   revisit with 3 satellites (days)")
    for W_km in (50.0, 100.0, 290.0, 1000.0, REVISIT_SWATH_M / 1e3):
        days = 2.0 * np.pi * R_EARTH / (ORBITS_PER_DAY * W_km * 1e3)
        print(f"  {W_km:11.0f}   {days:14.2f}   {days / 3.0:31.2f}")
    print("  This is an idealised geometric bound: it ignores swath overlap at")
    print("  high latitude, Earth rotation, off-nadir pointing, daylight-only")
    print("  operation and clouds, each of which makes the achieved revisit WORSE.")

    section("8. Radiometric resolution")
    levels = 2 ** BIT_DEPTH
    step = L_MAX / levels
    print(f"  full scale L_max = {L_MAX:.2e} W m^-2 sr^-1 m^-1, {BIT_DEPTH} bits")
    print(f"  quantisation levels = {levels}; step = L_max/2^b = {step:.3e} "
          "W m^-2 sr^-1 m^-1")
    print(f"  noise-equivalent radiance NE_dL = {NE_DL:.2e} W m^-2 sr^-1 m^-1")
    print(f"  quantisation step / NE_dL = {step / NE_DL:.4f}  "
          "-> quantisation is NOT the limit" if step < NE_DL else
          "  -> quantisation IS the limit")
    print(f"  SNR at full scale = L_max / NE_dL = {L_MAX / NE_DL:.1f}")
    lam_t, T = 10.8, 300.0
    L = planck(lam_t, T)
    dlnL_dT = H_PLANCK * C_LIGHT / (lam_t * 1e-6 * K_BOLTZ * T ** 2)
    dL_dT = L * dlnL_dT
    ne_dt = NE_DL / dL_dT
    print(f"  at lambda = {lam_t} um, T = {T:.0f} K: L = {L:.4e}, "
          f"dL/dT = {dL_dT:.4e} W m^-2 sr^-1 m^-1 K^-1")
    print(f"  NE_delta_T = NE_dL / (dL/dT) = {ne_dt:.4f} K")
    print("  NE-delta-T is the temperature change that produces one noise sigma;")
    print("  it is the radiometric resolution expressed in the units of the answer.")

    section("9. The spatial-spectral-radiometric trade")
    print("  Signal per pixel scales with GSD^2 x band width (fixed aperture and")
    print("  integration time, unresolved scene).  Relative SNR for synthetic")
    print("  designs, all normalised to the first row:")
    print("   GSD (m)   band width (nm)   relative SNR")
    base_gsd, base_bw = 10.0, 20.0
    for gsd_m, bw_nm in ((10.0, 20.0), (5.0, 20.0), (10.0, 10.0), (5.0, 10.0),
                         (20.0, 40.0)):
        rel = (gsd_m / base_gsd) ** 2 * (bw_nm / base_bw)
        print(f"  {gsd_m:8.1f}   {bw_nm:16.1f}   {rel:12.3f}")
    print("  Halving GSD quarters the signal per pixel; halving the band width")
    print("  halves it.  Sharper or finer always costs radiometric precision, and")
    print("  that is a designed trade, not an engineering failure.")

    section("10. Mixed pixels and the detectable fractional cover")
    T_hot, T_bg = 360.0, 300.0
    L_hot = planck(lam_t, T_hot)
    L_bg = planck(lam_t, T_bg)
    print(f"  a pixel mixes a hot target at {T_hot:.0f} K with background at "
          f"{T_bg:.0f} K at {lam_t} um")
    print(f"  L_hot = {L_hot:.4e}, L_bg = {L_bg:.4e} W m^-2 sr^-1 m^-1")
    print("   cover f    pixel radiance   excess over background   excess / NE_dL")
    for f in (0.01, 0.02, 0.05, 0.10, 0.25, 0.50):
        Lpix = f * L_hot + (1 - f) * L_bg
        exc = Lpix - L_bg
        print(f"  {f:7.2f}   {Lpix:13.4e}   {exc:21.4e}   {exc / NE_DL:14.2f}")
    f_detect = NE_DL / (L_hot - L_bg)
    print(f"  the noise-equivalent fractional cover is NE_dL/(L_hot - L_bg) = "
          f"{f_detect:.5f}")
    print("  A sub-pixel fraction below that value cannot be seen at one sigma, no")
    print("  matter how large the target is in temperature: at fixed GSD, small and")
    print("  hot is indistinguishable from large and warm in a single band.")

    section("11. The mixed-pixel null space: one band, many (f, T) pairs")
    L_pix_ref = 0.05 * L_hot + 0.95 * L_bg
    print(f"  fix the pixel radiance at the f = 0.05, T_hot = {T_hot:.0f} K value:")
    print(f"  L_pix = {L_pix_ref:.4e} W m^-2 sr^-1 m^-1")
    print("   assumed cover f   implied target temperature (K)")
    for f in (0.01, 0.02, 0.05, 0.10, 0.25, 0.50):
        L_target = (L_pix_ref - (1.0 - f) * L_bg) / f
        T_implied = planck_inverse_um(L_target, lam_t)
        print(f"  {f:17.2f}   {T_implied:31.3f}")
    print("  Every one of those pairs produces the SAME measured radiance in this")
    print("  single band: the inverse problem has a one-parameter null space.  Only a")
    print("  second band, an independent size estimate, or a prior on the target")
    print("  temperature resolves it -- and a prior is an assumption, not a")
    print("  measurement.")


if __name__ == "__main__":
    main()
