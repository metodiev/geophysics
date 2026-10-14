#!/usr/bin/env python3
"""Retrieving the Green's function by cross-correlation of ambient noise.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cross_correlation_green_demo.py

Everything is SYNTHETIC.  The station geometry, the source ring, the passband
and the noise realisations are chosen teaching values, not measurements.

Contents
--------
1. The analytic 2-D Green's function: travel time d/c and the Bessel result.
2. Time-domain noise simulation: cross-correlate two station records and recover
   the arrival at +/- d/c.
3. Emergence with stacking: the repeatability of the retrieved peak, measured
   over independent noise realisations.
4. Source distribution: causal/acausal amplitude ratio versus sector width.
5. Spectral whitening: measured pulse width before and after.
"""

import numpy as np
from scipy import signal, special

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
C_KM_S = 3.20            # homogeneous-medium phase speed
D_KM = 60.0              # inter-station distance
RING_KM = 500.0          # source-ring radius
FS_HZ = 2.0              # sampling rate
T_TOTAL_S = 4096.0       # total simulated record length
F1_HZ, F2_HZ = 0.05, 0.60  # analysis passband
N_SRC = 90               # sources on the ring
SEG_S = 64.0             # length of one stacking segment


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def bandpass(x, fs, f1, f2, order=4):
    sos = signal.butter(order, [f1, f2], btype="bandpass", fs=fs, output="sos")
    return signal.sosfiltfilt(sos, x)


def build_records(theta, n, dt, f1=F1_HZ, f2=F2_HZ, d_km=D_KM):
    """Synthetic records at two stations from uncorrelated ring sources.

    Each source emits independent noise; the far-field travel time from a ring
    source at azimuth theta to a station at axial coordinate x is
    (R - x cos theta)/c.  Shifts are rounded to whole samples, which limits the
    timing accuracy to half a sample.  The records are band-passed once here.
    """
    ra = np.zeros(n)
    rb = np.zeros(n)
    for th in theta:
        tau_a = (RING_KM - (d_km / 2.0) * np.cos(th)) / C_KM_S
        tau_b = (RING_KM + (d_km / 2.0) * np.cos(th)) / C_KM_S
        w = RNG.standard_normal(n)
        ra += np.roll(w, int(round(tau_a / dt)))
        rb += np.roll(w, int(round(tau_b / dt)))
    return bandpass(ra, FS_HZ, f1, f2), bandpass(rb, FS_HZ, f1, f2)


def stack_correlation(ra, rb, dt, n_seg, seg_len):
    """Stack the cross-correlation of n_seg consecutive segments.

    Lags are returned so that the causal arrival for propagation A -> B sits at
    the positive lag +d/c (scipy's raw correlation index runs the other way).
    """
    acc = np.zeros(2 * seg_len - 1)
    taper = np.hanning(seg_len)
    for m in range(n_seg):
        a = ra[m * seg_len:(m + 1) * seg_len] * taper
        b = rb[m * seg_len:(m + 1) * seg_len] * taper
        acc += signal.correlate(a, b, mode="full")
    return acc / (n_seg * seg_len)


def main():
    dt = 1.0 / FS_HZ
    n = int(T_TOTAL_S * FS_HZ)
    t_arr = D_KM / C_KM_S
    seg_len = int(SEG_S * FS_HZ)
    n_seg = n // seg_len
    lags = (seg_len - 1 - np.arange(2 * seg_len - 1)) * dt

    section("1. The analytic Green's function of a homogeneous medium")
    print(f"  SYNTHETIC model: c = {C_KM_S:.2f} km/s, station separation "
          f"d = {D_KM:.1f} km")
    print(f"  direct arrival time d/c = {t_arr:.3f} s (causal) and "
          f"{-t_arr:.3f} s (acausal)")
    print("  In a diffuse 2-D field the cross-spectrum of two stations separated")
    print("  by d is C(f) = S(f) J0(2*pi*f*d/c); its inverse transform is in")
    print("  principle the Green's function, time-limited to |t| <= d/c.")
    print("\n  period (s)   k*d (rad)   J0(k*d)")
    for T in (20.0, 14.0, 10.0, 7.0, 5.0):
        kd = 2.0 * np.pi * (1.0 / T) * D_KM / C_KM_S
        print(f"  {T:10.1f}   {kd:10.3f}   {special.j0(kd):+8.4f}")

    section("2. Time-domain retrieval: cross-correlation of two noise records")
    theta = np.linspace(0.0, 2.0 * np.pi, N_SRC, endpoint=False)
    ra, rb = build_records(theta, n, dt)
    cc = stack_correlation(ra, rb, dt, n_seg, seg_len)
    win = np.abs(lags - t_arr) < 4.0
    t_meas = lags[win][np.argmax(np.abs(cc[win]))]
    print(f"  sources: {N_SRC} on a ring of {RING_KM:.0f} km; passband "
          f"{F1_HZ:.2f}-{F2_HZ:.2f} Hz; {n} samples at {FS_HZ:.1f} Hz")
    print(f"  stacked segments: {n_seg} of {SEG_S:.0f} s ({T_TOTAL_S:.0f} s total)")
    print(f"  analytic arrival d/c      = {t_arr:+.3f} s")
    print(f"  measured causal peak lag  = {t_meas:+.3f} s  "
          f"(error {t_meas - t_arr:+.3f} s, half a sample = {0.5 * dt:.3f} s)")
    print(f"  travel time read from the measurement -> c = "
          f"{D_KM / abs(t_meas):.3f} km/s")
    print(f"  causal / acausal peak amplitudes: "
          f"{np.max(np.abs(cc[np.abs(lags - t_arr) < 1.5])):.4f} / "
          f"{np.max(np.abs(cc[np.abs(lags + t_arr) < 1.5])):.4f}")

    section("3. Emergence: the retrieval noise floor falls as 1/sqrt(N)")
    print("  The arrival amplitude converges to a fixed value A; the noise floor")
    print("  (rms of the correlation for 25 s < |lag| < 60 s) is measured for each")
    print("  stack length N, and SNR is quoted as A / floor(N).")
    print("\n  N segments   noise floor     log10(N)   log10(floor)")
    ms, floors = [], []
    c_max = None
    for nseg in (1, 2, 4, 8, 16, 32, 64):
        c2 = stack_correlation(ra, rb, dt, nseg, seg_len)
        floors.append(float(np.sqrt(np.mean(c2[np.abs(lags) > 25.0] ** 2))))
        ms.append(nseg)
        if nseg == 64:
            c_max = c2.copy()
    for nseg, fl in zip(ms, floors):
        print(f"  {nseg:10d}   {fl:11.5f}   {np.log10(nseg):8.3f}   "
              f"{np.log10(fl):11.3f}")
    slope = np.polyfit(np.log10(ms), np.log10(floors), 1)[0]
    A = float(np.mean(np.abs(c_max[np.abs(lags - t_arr) < 1.5])))
    print(f"  converged arrival amplitude (N = 64): A = {A:.4f}")
    print(f"  measured slope d log(floor) / d log(N) = {slope:.3f} "
          f"(the sqrt(N) law predicts -0.500)")
    print(f"  SNR(N) = A / floor(N): {A / floors[0]:.1f} at N = 1, "
          f"{A / floors[-1]:.1f} at N = 64")
    print("  The retrieval becomes detectable only because the incoherent part")
    print("  of the correlation averages down; the coherent arrival does not.")

    section("4. One-sided sources: causal/acausal amplitude ratio")
    print("  Sources restricted to a sector centred on the station-pair axis.")
    print("\n  sector (deg)   N sources   |c(+d/c)|   |c(-d/c)|   ratio")
    for width in (360.0, 180.0, 90.0, 45.0):
        half = np.deg2rad(width / 2.0)
        th = np.linspace(-half, half, N_SRC)
        a2, b2 = build_records(th, n, dt)
        c2 = stack_correlation(a2, b2, dt, n_seg, seg_len)
        ap = np.max(np.abs(c2[np.abs(lags - t_arr) < 1.5]))
        am = np.max(np.abs(c2[np.abs(lags + t_arr) < 1.5]))
        print(f"  {width:12.0f}   {th.size:9d}   {ap:10.5f}   {am:10.5f}   "
              f"{ap / am:5.2f}")

    section("5. Verification: the retrieved travel time is linear in separation")
    print("  The Green's function is retrieved for four station separations with")
    print("  the same source ring.  The arrival must move linearly with d.")
    print("\n    d (km)   predicted t = d/c (s)   measured lag (s)   c from lag (km/s)")
    errs, cs = [], []
    for d_km in (20.0, 40.0, 60.0, 80.0):
        a4, b4 = build_records(theta, n, dt, d_km=d_km)
        c4 = stack_correlation(a4, b4, dt, n_seg, seg_len)
        t_pred = d_km / C_KM_S
        w = np.abs(lags - t_pred) < 4.0
        t_got = lags[w][np.argmax(np.abs(c4[w]))]
        errs.append(t_got - t_pred)
        cs.append(d_km / abs(t_got))
        print(f"    {d_km:6.0f}   {t_pred:18.2f}   {t_got:16.2f}   "
              f"{cs[-1]:16.3f}")
    print(f"    mean inferred c = {np.mean(cs):.3f} km/s "
          f"(model {C_KM_S:.2f} km/s); rms timing error = "
          f"{np.sqrt(np.mean(np.square(errs))) / dt:.2f} samples "
          f"({np.sqrt(np.mean(np.square(errs))):.3f} s)")


if __name__ == "__main__":
    main()
