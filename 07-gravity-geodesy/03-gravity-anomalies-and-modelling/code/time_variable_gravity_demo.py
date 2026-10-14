#!/usr/bin/env python3
"""Time-variable gravity: water storage to gravity, gravity to mass, attenuation
with altitude, leakage from filtering, and separating a trend from a season.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python time_variable_gravity_demo.py

All models and data in this module are SYNTHETIC.  The layer thicknesses, the
region size, the observation altitude and the noise levels are chosen teaching
values, not measurements from any real mission or station.

Contents
--------
1. A local water layer (flat-Earth slab) and a global water layer (spherical
   shell): two different constants, 2 pi G and 4 pi G.
2. A seasonal storage cycle, and the density-thickness ambiguity.
3. Attenuation of a compact mass with observation altitude (measured).
4. Leakage from a smoothing filter: amplitude bias and mass outside the source.
5. Gravity change to mass change for a region, with an error budget.
6. Separating a secular trend from a seasonal cycle when both are present.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_SI = 6.67430e-11
UGAL_TO_SI = 1.0e-8
RHO_WATER = 1000.0          # kg/m^3
R_EARTH = 6371000.0         # m, a representative mean radius (SYNTHETIC use)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ugal(g_si):
    return g_si / UGAL_TO_SI


def main():
    section("1. A local water layer and a global water layer")
    print("   layer (m)   flat-Earth slab 2 pi G rho h   global shell 4 pi G rho h"
          "   ratio")
    print("               (uGal)                          (uGal)")
    for h in (0.01, 0.1, 1.0, 10.0):
        slab = 2.0 * np.pi * G_SI * RHO_WATER * h
        shell = 4.0 * np.pi * G_SI * RHO_WATER * h
        print(f"  {h:9.2f}   {ugal(slab):24.3f}   {ugal(shell):31.3f}   "
              f"{shell / slab:6.2f}")
    print("  1 m of water = 41.9 uGal over an infinite slab, 83.9 uGal spread over")
    print("  the whole sphere.  The factor of two is geometry, not sloppiness, and")
    print("  quoting one number without saying which model it belongs to is an error.")

    section("2. A seasonal storage cycle, and the density-thickness ambiguity")
    t = np.arange(0.0, 730.0, 10.0)                 # two years, 10-day steps
    amp_h = 0.5                                     # m of water
    h_seasonal = amp_h * np.cos(2.0 * np.pi * t / 365.25)
    dg = 2.0 * np.pi * G_SI * RHO_WATER * h_seasonal
    print(f"SYNTHETIC seasonal cycle: +/-{amp_h:.2f} m equivalent water, period "
          "365.25 d")
    print(f"  gravity amplitude = {ugal(np.abs(dg).max()):.2f} uGal pk-pk "
          f"{ugal(dg.max() - dg.min()):.2f} uGal")
    print("  time (d)   EWH (m)   dg (uGal)")
    for tt, hh, gg in list(zip(t, h_seasonal, dg))[::9]:
        print(f"  {tt:8.0f}   {hh:8.3f}   {ugal(gg):9.3f}")
    dg_rock = 2.0 * np.pi * G_SI * 2500.0 * (amp_h * 1000.0 / 2500.0)
    print(f"  {amp_h:.2f} m of water gives the same signal as "
          f"{amp_h * RHO_WATER / 2500.0:.3f} m of rock at 2500 kg/m^3:")
    print(f"    water: {ugal(2 * np.pi * G_SI * RHO_WATER * amp_h):.3f} uGal; "
          f"rock: {ugal(dg_rock):.3f} uGal (identical)")
    print("  Gravity fixes the product of density and thickness, never either alone.")

    section("3. Attenuation of a compact mass with observation altitude")
    n, extent = 256, 4.0e6                          # 4 Mm box, ~15.6 km pixels
    k1 = 2.0 * np.pi / extent
    f = np.fft.fftfreq(n, d=extent / n) * 2.0 * np.pi
    KX, KY = np.meshgrid(f, f, indexing="ij")
    K = np.hypot(KX, KY)
    x = np.arange(n) * (extent / n) - extent / 2.0
    X, Y = np.meshgrid(x, x, indexing="ij")

    def gaussian_layer(sigma_m):
        return RHO_WATER * 1.0 * np.exp(-(X ** 2 + Y ** 2) / (2.0 * sigma_m ** 2))

    print("SYNTHETIC surface mass (1 m equivalent water) with a Gaussian footprint")
    print(f"  grid {n} x {n} over {extent / 1000:.0f} km; wavenumber "
          f"k1 = {k1:.3e} 1/m")
    print("   sigma (km)   peak dg on the ground   peak dg at 400 km   factor")
    print("                (uGal)                   (uGal)")
    for sig in (20.0e3, 40.0e3, 80.0e3, 160.0e3):
        sigma = gaussian_layer(sig)
        Sk = np.fft.fft2(sigma)
        ground = np.real(np.fft.ifft2(2.0 * np.pi * G_SI * Sk))
        alt = np.real(np.fft.ifft2(2.0 * np.pi * G_SI * np.exp(-K * 4.0e5) * Sk))
        i = n // 2
        print(f"  {sig / 1000:11.0f}   {ugal(ground[i, i]):22.4f}   "
              f"{ugal(alt[i, i]):18.4f}   {alt[i, i] / ground[i, i]:6.3f}")
    print("  The kernel 2 pi G sigma is exact for the ground field; at altitude the")
    print("  short wavelengths are lost by exp(-k H), so a compact mass is seen")
    print("  weaker than it is: a 20 km footprint keeps 0.3 % of its amplitude, a")
    print("  160 km footprint 11.6 %.  Compact storage is nearly invisible from")
    print("  orbit, which is why satellite gravimetry is a large-scale technique.")

    section("4. Leakage from a smoothing filter")
    sig = 40.0e3
    sigma = gaussian_layer(sig)
    truth = sigma / RHO_WATER                         # equivalent water height, m
    Sc = np.fft.fft2(truth)
    ground = np.real(np.fft.ifft2(Sc))
    print(f"SYNTHETIC footprint sigma = {sig / 1000:.0f} km, 1 m equivalent water")
    print("   filter radius (km)   recovered peak (m EWH)   peak bias (%)   "
          "mass outside 3 sigma (%)")
    inside = (X ** 2 + Y ** 2) <= (3.0 * sig) ** 2
    dxcell = (extent / n) ** 2
    for rf in (20.0e3, 40.0e3, 80.0e3, 160.0e3):
        filt = np.exp(-(K * rf) ** 2 / 2.0)
        rec = np.real(np.fft.ifft2(filt * Sc))
        i = n // 2
        outside_frac = np.sum(rec[~inside]) * dxcell / np.sum(rec * dxcell) * 100.0
        print(f"  {rf / 1000:18.0f}   {rec[i, i]:20.3f}   "
              f"{100.0 * (rec[i, i] - 1.0):14.2f}   {outside_frac:24.2f}")
    print("  Smoothing lowers the peak and spreads mass outward: the recovered")
    print("  amplitude is a lower bound on the true storage, and the leaked signal")
    print("  is easily mistaken for mass where there is none.")

    section("5. Gravity change to mass change for a region")
    area = (200.0e3) ** 2
    for dg_ugal in (1.0, 2.0, 10.0):
        dg = dg_ugal * UGAL_TO_SI
        mass = dg * area / (2.0 * np.pi * G_SI)
        ewh = mass / (RHO_WATER * area)
        print(f"  dg = {dg_ugal:5.2f} uGal over {(200):.0f} x {(200):.0f} km: "
              f"mass = {mass:.3e} kg, equivalent water height = {ewh:.3f} m")
    print("  The conversion divides by 2 pi G and multiplies by the area, so an")
    print("  area error enters linearly and a density error enters linearly too.")
    print("  With a 0.2 uGal uncertainty on a 2 uGal signal the mass carries a 10 %")
    print("  random error before any systematic leakage bias.")

    section("6. Separating a trend from a season")
    t2 = np.arange(0.0, 3650.0, 30.0)                # ten years
    trend_rate = -0.05                               # m/yr of equivalent water
    truth_ewh = trend_rate * t2 / 365.25 + 0.3 * np.cos(2.0 * np.pi * t2 / 365.25)
    dg_series = 2.0 * np.pi * G_SI * RHO_WATER * truth_ewh
    print(f"SYNTHETIC ten-year record: trend {trend_rate:+.2f} m/yr in equivalent")
    print("  water height, plus a 0.30 m annual cycle; no noise")
    A = np.column_stack([np.ones_like(t2), t2 / 365.25,
                         np.cos(2.0 * np.pi * t2 / 365.25),
                         np.sin(2.0 * np.pi * t2 / 365.25)])
    coef, *_ = np.linalg.lstsq(A, dg_series, rcond=None)
    rate_fit = coef[1] / (2.0 * np.pi * G_SI * RHO_WATER)
    amp_fit = np.hypot(coef[2], coef[3]) / (2.0 * np.pi * G_SI * RHO_WATER)
    print(f"  fitted trend = {rate_fit:+.5f} m/yr (true {trend_rate:+.2f})")
    print(f"  fitted annual amplitude = {amp_fit:.5f} m (true 0.300)")
    print("  Now add white noise and repeat:")
    print("   noise (uGal)   mean fitted trend   scatter of the trend   "
          "scatter of the annual amplitude")
    print("                  (m/yr)              (m/yr)                 (m)")
    for nl in (0.0, 0.5, 1.0, 2.0):
        fits_r, fits_a = [], []
        for _ in range(200):
            y = dg_series + nl * UGAL_TO_SI * RNG.standard_normal(t2.size)
            c, *_ = np.linalg.lstsq(A, y, rcond=None)
            fits_r.append(c[1] / (2.0 * np.pi * G_SI * RHO_WATER))
            fits_a.append(np.hypot(c[2], c[3]) / (2.0 * np.pi * G_SI * RHO_WATER))
        print(f"  {nl:11.1f}   {np.mean(fits_r):+19.5f}   {np.std(fits_r):22.5f}   "
              f"{np.std(fits_a):29.5f}")
    print("  A ten-year record with 1 uGal noise pins the trend to about 1e-4 m/yr,")
    print("  because ten years of a 0.05 m/yr trend integrate to a 0.5 m signal.")
    print("  Shorten the record or reduce the trend and the noise dominates -- which")
    print("  is why time-variable gravity is a long-baseline method.")


if __name__ == "__main__":
    main()
