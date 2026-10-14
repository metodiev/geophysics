#!/usr/bin/env python3
"""Cryosphere remote sensing: snow albedo and grain size, snow depth from a
brightness-temperature difference, glacier velocity by image correlation, and a
thaw-subsidence series.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cryosphere_rs_demo.py

Everything here is SYNTHETIC.  The albedo model, the depth relation, the imagery
and the subsidence series are chosen teaching values, not measurements of a real
glacier, snowpack or permafrost site.  No file is read or written and no network
access is used.

Contents
--------
1. Snow albedo as a function of grain size and impurity.
2. Snow depth from a passive-microwave brightness-temperature difference.
3. Glacier surface velocity from cross-correlation of two synthetic images.
4. A thaw-subsidence series and the detection of a few centimetres.
"""

import numpy as np
from numpy.fft import fft2, ifft2

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def snow_albedo(grain_um, impurity=0.0):
    """Synthetic broadband albedo: falls with grain size and with impurity."""
    return 0.99 - 0.22 * (1.0 - np.exp(-grain_um / 250.0)) - 0.35 * impurity


def tb_difference(sd_cm, forest_frac=0.0):
    """Synthetic 19/37 GHz brightness-temperature difference (K) for snow depth."""
    signal = 6.0 * (1.0 - np.exp(-sd_cm / 45.0))      # saturates past ~0.5 m
    return signal * (1.0 - 0.6 * forest_frac)


def cross_corr_shift(a, b):
    """Integer pixel shift (dx, dy) that best aligns b onto a (circular)."""
    c = np.real(ifft2(fft2(b) * np.conj(fft2(a))))
    peak = np.unravel_index(np.argmax(c), c.shape)
    dy, dx = int(peak[0]), int(peak[1])
    if dy > a.shape[0] // 2:
        dy -= a.shape[0]
    if dx > a.shape[1] // 2:
        dx -= a.shape[1]
    return dx, dy


def main():
    section("1. Snow albedo versus grain size and impurity (SYNTHETIC)")
    print("  grain (um)   clean albedo   with 5% impurity")
    for g in (50.0, 100.0, 200.0, 500.0, 1000.0):
        print(f"  {g:10.0f}   {snow_albedo(g):12.3f}   {snow_albedo(g, 0.05):17.3f}")
    print(f"clean albedo for 50 um to 1000 um falls from {snow_albedo(50.0):.3f} "
          f"to {snow_albedo(1000.0):.3f}")
    print("Coarse, old or dirty snow is darker; a retreating snowline is read")
    print("from albedo, and darkness has two causes that a single channel cannot")
    print("separate.")

    section("2. Snow depth from a brightness-temperature difference (SYNTHETIC)")
    a_cm_per_K = 7.5       # SYNTHETIC empirical coefficient, cm per K
    print(f"retrieval SD = {a_cm_per_K:.1f} cm/K x (TB19 - TB37), SYNTHETIC")
    print("  true SD (cm)   dTB (K)   retrieved (cm)   bias (cm)")
    for sd in (5.0, 15.0, 40.0, 80.0, 150.0):
        dtb = tb_difference(sd)
        ret = a_cm_per_K * dtb
        print(f"  {sd:12.0f}   {dtb:8.3f}   {ret:15.1f}   {ret - sd:+9.1f}")
    print("The relation saturates: past roughly half a metre the signal barely")
    print("grows, so deep snow is systematically underestimated.")
    print("  forest fraction   dTB (K) for 40 cm   retrieved (cm)")
    for f in (0.0, 0.25, 0.5):
        dtb = tb_difference(40.0, forest_frac=f)
        print(f"  {f:15.2f}   {dtb:18.3f}   {a_cm_per_K * dtb:14.1f}")
    print("A forest absorbs and re-emits the microwave signal; without a")
    print("vegetation correction, forested snow reads as thin snow.")

    section("3. Glacier velocity by image cross-correlation (SYNTHETIC)")
    size = 128
    tex = np.zeros((size, size))
    for _ in range(4000):
        tex[RNG.integers(0, size), RNG.integers(0, size)] += 1.0
    # smooth the speckle into a correlatable texture (simple box filter)
    k = 3
    tex = np.apply_along_axis(lambda r: np.convolve(r, np.ones(k) / k, mode="same"),
                              1, tex)
    tex = np.apply_along_axis(lambda r: np.convolve(r, np.ones(k) / k, mode="same"),
                              0, tex)
    dx_true, dy_true = 2, 3
    img2 = np.roll(np.roll(tex, dy_true, axis=0), dx_true, axis=1)
    img2 += RNG.normal(0.0, 0.05, img2.shape)
    dx, dy = cross_corr_shift(tex, img2)
    pixel_m = 10.0
    dt_days = 30.0
    mag_px = np.hypot(dx, dy)
    vel_m_per_yr = mag_px * pixel_m / dt_days * 365.25
    print(f"image size = {size} x {size} px, pixel = {pixel_m:.0f} m, "
          f"interval = {dt_days:.0f} d")
    print(f"true shift = ({dx_true}, {dy_true}) px; recovered = ({dx}, {dy}) px")
    print(f"speed = {mag_px:.3f} px = {mag_px * pixel_m:.1f} m over {dt_days:.0f} d")
    print(f"speed = {vel_m_per_yr:.1f} m/yr")
    unc = 0.5 * pixel_m / dt_days * 365.25
    print(f"integer-pixel quantisation gives +/- 0.5 px, i.e. +/- {unc:.1f} m/yr")
    print("Feature tracking measures displacement between two images; its")
    print("accuracy floor is a fraction of a pixel unless it is interpolated.")

    section("4. Thaw subsidence: a few centimetres against noise (SYNTHETIC)")
    t_days = np.arange(0.0, 5.0 * 365.25, 12.0)     # 12-day revisit
    thaw = -0.05 * np.sin(2 * np.pi * (t_days / 365.25 - 0.25))   # seasonal +/-5 cm
    trend = -0.010 * (t_days / 365.25)              # 1 cm/yr of net settlement
    noise = RNG.normal(0.0, 0.008, t_days.size)     # 8 mm measurement noise
    disp = thaw + trend + noise
    amp = (disp.max() - disp.min()) / 2
    print(f"revisit = 12 d, {t_days.size} observations over 5 yr")
    print(f"seasonal amplitude (model) = 5.00 cm; noise sd = {noise.std() * 100:.2f} cm")
    print(f"secular trend (model) = 1.0 cm/yr; measured half-range = {amp * 100:.2f} cm")
    print(f"measured total range = {(disp.max() - disp.min()) * 100:.2f} cm")
    print("A centimetre-per-year settlement sits under a five-centimetre seasonal")
    print("amplitude, so the honest statement separates the periodic thaw signal")
    print("from the secular trend; a single displacement map cannot do that.")


if __name__ == "__main__":
    main()
