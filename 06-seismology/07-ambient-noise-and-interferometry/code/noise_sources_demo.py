#!/usr/bin/env python3
"""Sources of ambient seismic noise: microseism bands, heavy-tailed statistics,
and the two-station coherence of a diffuse (isotropic) noise field.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python noise_sources_demo.py

Everything is SYNTHETIC.  The ocean-wave periods, the source ring radius, the
station separation and the noise realisations are chosen teaching values, not
measurements.  No real station, event or waveform is used.

Contents
--------
1. Microseism period bands from a synthetic ocean-wave model.
2. A synthetic ambient-noise spectrum with two microseism peaks; the measured
   peak periods recovered from a Welch periodogram.
3. Kurtosis and skewness: continuous vs impulsive source statistics.
4. Two-station coherence of an isotropic source ring; measured against J0(kd).
5. Directional (sector) illumination: the measured phase and amplitude bias.
"""

import numpy as np
from scipy import ndimage, signal, special, stats

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
SWELL_PERIODS_S = np.array([8.0, 10.0, 12.0, 14.0, 16.0])  # ocean swell
F_PRIMARY_HZ = 1.0 / 16.0     # primary microseism band centre (~16 s)
F_SECONDARY_HZ = 1.0 / 7.0    # secondary microseism band centre (~7 s)
C_SURFACE_KM_S = 3.20         # Rayleigh-wave speed of the teaching model
RING_RADIUS_KM = 500.0        # radius of the source ring
D_STATION_KM = 60.0           # inter-station distance
FS_HZ = 5.0                   # sampling rate of the synthetic records
T_REC_S = 20_000.0            # ~5.6 h of synthetic noise at FS_HZ


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def synthetic_spectrum(freq):
    """Synthetic ambient-noise amplitude spectrum (arbitrary units, teaching)."""
    f = np.maximum(freq, 1e-4)
    base = (f / 0.2) ** -1.0                                   # 1/f background
    prim = 6.0 * np.exp(-0.5 * ((f - F_PRIMARY_HZ) / 0.012) ** 2)
    sec = 10.0 * np.exp(-0.5 * ((f - F_SECONDARY_HZ) / 0.035) ** 2)
    return base + prim + sec


def main():
    section("1. Microseism period bands from a synthetic ocean-wave model")
    print("Teaching relation: primary microseism period = swell period;")
    print("secondary (double-frequency) microseism period = swell period / 2.")
    print("\n  swell period (s)   primary (s)   secondary (s)")
    for tp in SWELL_PERIODS_S:
        print(f"  {tp:15.1f}   {tp:11.1f}   {tp / 2.0:13.1f}")

    section("2. Synthetic ambient-noise spectrum: measured peak periods")
    n = int(T_REC_S * FS_HZ)
    freq = np.fft.rfftfreq(n, d=1.0 / FS_HZ)
    amp = synthetic_spectrum(freq)
    phase = RNG.uniform(0.0, 2.0 * np.pi, freq.size)
    spec = amp * np.exp(1j * phase)
    ts = np.fft.irfft(spec, n=n)
    ts /= ts.std()
    f_w, psd = signal.welch(ts, fs=FS_HZ, nperseg=32768, noverlap=16384)
    smooth = ndimage.uniform_filter1d(psd, size=101, mode="nearest")
    print(f"  record: {n} samples, {T_REC_S:.0f} s at {FS_HZ:.1f} Hz "
          f"(SYNTHETIC white-phase realisation)")
    print(f"  frequency resolution of the periodogram: df = {f_w[1] - f_w[0]:.2e} Hz")
    print("\n  search band (s)   input centre (s)   measured peak (s)   error (s)")
    for name, T_lo, T_hi, centre in (("primary", 12.0, 20.0, 1.0 / F_PRIMARY_HZ),
                                     ("secondary", 5.0, 9.0, 1.0 / F_SECONDARY_HZ)):
        win = (f_w >= 1.0 / T_hi) & (f_w <= 1.0 / T_lo)
        f_peak = f_w[win][np.argmax(smooth[win])]
        print(f"  {name:10s} {T_lo:4.0f}-{T_hi:<4.0f}   {centre:12.1f}   "
              f"{1.0 / f_peak:17.2f}   {1.0 / f_peak - centre:+8.2f}")

    section("3. Source statistics: continuous vs impulsive noise")
    gauss = RNG.standard_normal(400_000)
    n_imp = 400
    impuls = RNG.standard_normal(400_000)
    hits = RNG.integers(0, impuls.size, n_imp)
    impuls[hits] += RNG.uniform(8.0, 20.0, n_imp) * RNG.choice([-1.0, 1.0], n_imp)
    for name, x in (("continuous (Gaussian)", gauss), ("impulsive (transients)", impuls)):
        print(f"  {name:24s} skewness = {stats.skew(x):+7.3f}   "
              f"excess kurtosis = {stats.kurtosis(x):+7.3f}   "
              f"rms = {x.std():6.3f} (unitless, normalised)")

    section("4. Isotropic source ring: measured coherence vs J0(kd)")
    theta = np.linspace(0.0, 2.0 * np.pi, 720, endpoint=False)
    print(f"  source ring radius {RING_RADIUS_KM:.0f} km, station separation "
          f"{D_STATION_KM:.0f} km, c = {C_SURFACE_KM_S:.2f} km/s")
    print("\n  period (s)   f (Hz)   k*d (rad)   measured C = Re    J0(kd)      error")
    for T in (20.0, 14.0, 10.0, 7.0, 5.0, 3.5):
        f = 1.0 / T
        k = 2.0 * np.pi * f / C_SURFACE_KM_S
        kd = k * D_STATION_KM
        # cross-spectrum of a diffuse field of uncorrelated sources
        C = np.mean(np.exp(1j * kd * np.cos(theta)))
        exact = special.j0(kd)
        print(f"  {T:10.1f}   {f:6.3f}   {kd:10.3f}   {C.real:15.5f}   "
              f"{exact:9.5f}   {abs(C - exact):7.1e}")
    print("  The synthetic diffuse field reproduces the exact result C = J0(kd):")
    print("  coherence magnitude falls to zero at kd = 2.405 (the first J0 zero)")
    print("  and again at every subsequent zero of J0.")

    section("5. Directional illumination: what a sector of sources does")
    print("  Sources confined to an azimuth sector d(theta) centred on the")
    print("  station-pair axis; the isotropic case is d(theta) = 360 deg.")
    print("\n  sector (deg)   Re(C)     Im(C)    |C|      phase (deg)   |C|-|J0|")
    T = 7.0
    f = 1.0 / T
    kd = 2.0 * np.pi * f / C_SURFACE_KM_S * D_STATION_KM
    j0 = special.j0(kd)
    for width in (360.0, 180.0, 90.0, 45.0, 20.0):
        half = np.deg2rad(width / 2.0)
        th = np.linspace(-half, half, 20001)
        C = np.mean(np.exp(1j * kd * np.cos(th)))
        print(f"  {width:12.0f}   {C.real:+7.4f}   {C.imag:+7.4f}   "
              f"{abs(C):6.4f}   {np.rad2deg(np.angle(C)):11.2f}   "
              f"{abs(C) - abs(j0):+7.4f}")
    print(f"\n  at T = {T:.1f} s (kd = {kd:.3f}) the diffuse-field value is "
          f"J0 = {j0:+.4f}, with no imaginary part.")
    print("  A one-sided source sector makes the cross-spectrum complex: its phase")
    print("  measures the mean source azimuth, so a one-sided source field is")
    print("  indistinguishable from a laterally varying structure in a single")
    print("  measurement.  This is the central bias of noise interferometry.")


if __name__ == "__main__":
    main()
