#!/usr/bin/env python3
"""Autocorrelation of ambient noise: zero-offset reflectivity from a single
station.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python autocorrelation_demo.py

Everything is SYNTHETIC.  The layered model, the passband and the noise
realisations are chosen teaching values, not measurements of the Earth.  No real
station or waveform is used.

Contents
--------
1. A layered model: normal-incidence impedances and reflection coefficients.
2. Two-way travel times of the reflectors.
3. Retrieval: the autocorrelation of the vertical noise shows peaks at the
   two-way times; measured times against the model.
4. Amplitude recovery: peak amplitudes against the reflection coefficients.
5. Resolution: two reflectors closer than the wavelet cannot be separated.
6. Convergence: the rms error of the estimate falls as 1/sqrt(N).
"""

import numpy as np
from scipy import signal

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching model (chosen, not measured) -------------------------
#        vp      vs      rho     thickness
LAYERS = [(5.80, 3.30, 2.60, 5.0),     # km/s, km/s, g/cm^3, km
          (6.30, 3.60, 2.75, 4.0),
          (7.10, 4.00, 2.95, 6.0),
          (8.00, 4.45, 3.20, np.inf)]  # half-space
FS_HZ = 40.0
F1_HZ, F2_HZ = 1.0, 5.0
WIN_S = 60.0                # window length for one autocorrelation estimate


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def bandpass(x, fs, f1, f2, order=4):
    sos = signal.butter(order, [f1, f2], btype="bandpass", fs=fs, output="sos")
    return signal.sosfiltfilt(sos, x)


def model():
    """Impedances (rayl), reflection coefficients and two-way times (s)."""
    vp = np.array([l[0] for l in LAYERS])
    rho = np.array([l[2] for l in LAYERS])
    h = np.array([l[3] for l in LAYERS[:-1]])
    z = rho * vp * 1e3 * 1e3                  # g/cm^3 km/s -> kg m^-2 s^-1
    r = (z[1:] - z[:-1]) / (z[1:] + z[:-1])
    t = 2.0 * np.cumsum(h / vp[:-1])
    return z, r, t, h, vp


def reflectivity(coeffs, times, n, dt):
    """Reflection response of the stack to a source at the surface.

    A unit amplitude at t = 0 is the direct (down-going then up-going) arrival
    that must be present for the autocorrelation to give ABSOLUTE two-way times:
    the autocorrelation measures differences of arrival times.
    """
    r = np.zeros(n)
    r[0] = 1.0
    for c, t in zip(coeffs, times):
        r[int(round(t / dt))] += c
    return r


def autocorr_stack(x, dt, L, n_win):
    """Average the autocorrelation of n_win consecutive windows."""
    acc = np.zeros(2 * L - 1)
    for m in range(n_win):
        seg = x[m * L:(m + 1) * L]
        seg = seg - seg.mean()
        acc += np.correlate(seg, seg, mode="full")
    return acc / (n_win * L)


def peak_time(c, dt, t0, half_s=0.3):
    """Refined peak time near t0 using a three-point parabolic fit (s)."""
    i0 = int(round(t0 / dt))
    lo, hi = i0 - int(half_s / dt), i0 + int(half_s / dt)
    k = lo + int(np.argmax(np.abs(c[lo:hi])))
    y = np.abs(c[k - 1:k + 2])
    denom = y[0] - 2.0 * y[1] + y[2]
    shift = -0.5 * (y[2] - y[0]) / denom * dt if denom != 0 else 0.0
    return k * dt + shift, float(np.abs(c[k]))


def main():
    dt = 1.0 / FS_HZ
    z, r, t2, h, vp = model()

    section("1. Layered model: impedance and reflection coefficient")
    print("  normal-incidence relations:")
    print("    Z = rho * vp,   R = (Z2 - Z1) / (Z2 + Z1),   T = 1 + R")
    print("\n  interface   Z_above (rayl)   Z_below (rayl)   R          T")
    for i, (c, za, zb) in enumerate(zip(r, z[:-1], z[1:]), start=1):
        print(f"  {i:9d}   {za:15.3e}   {zb:15.3e}   {c:+8.5f}   {1 + c:8.5f}")
    print("  R is dimensionless; a negative R means the impedance drops, which is")
    print("  the signature of a low-velocity or low-density layer.")

    section("2. Two-way travel times")
    print("  t_i = 2 * sum(h_k / vp_k) over the layers above interface i")
    print("\n  interface   depth (km)   two-way time (s)")
    print(f"  {'surface':9s}   {0.0:10.1f}   {0.0:15.4f}")
    depth = 0.0
    for i, (ti, hi) in enumerate(zip(t2, h), start=1):
        depth += hi
        print(f"  {i:9d}   {depth:10.1f}   {ti:15.4f}")

    section("3. Retrieval from the autocorrelation of the vertical noise")
    n_win = 64
    L = int(WIN_S / dt)
    n = L * n_win
    w = bandpass(RNG.standard_normal(n), FS_HZ, F1_HZ, F2_HZ)
    refl = reflectivity(r, t2, n, dt)
    record = signal.fftconvolve(w, refl)[:n]
    c = autocorr_stack(record, dt, L, n_win)
    cc = c[L - 1:]                     # non-negative lags
    print(f"  passband {F1_HZ:.2f}-{F2_HZ:.2f} Hz, {n_win} windows of "
          f"{WIN_S:.0f} s, sampling {FS_HZ:.0f} Hz")
    print("  the reflectivity used here has a unit arrival at t = 0 (the direct")
    print("  wave) so that the autocorrelation gives absolute two-way times.")
    print("\n  interface   t_model (s)   t_measured (s)   error (ms)")
    amps = []
    for i, ti in enumerate(t2, start=1):
        tm, a = peak_time(cc, dt, ti)
        amps.append(a)
        print(f"  {i:9d}   {ti:11.4f}   {tm:15.4f}   {(tm - ti) * 1e3:+9.2f}")
    print(f"  zero-lag amplitude A(0) = {cc[0]:.5f} (the direct wave)")

    section("4. Amplitude recovery")
    # calibration: a single reflector must give A_peak = R * A(0) exactly
    single = signal.fftconvolve(w, reflectivity(np.array([r[0]]),
                                                np.array([t2[0]]), n, dt))[:n]
    cs = autocorr_stack(single, dt, L, n_win)[L - 1:]
    ts, a_single = peak_time(cs, dt, t2[0])
    print(f"  calibration with a single reflector of R = {r[0]:+.5f}:")
    print(f"    t = {ts:.4f} s (model {t2[0]:.4f} s), "
          f"A_peak/A(0) = {a_single / cs[0]:.6f}, "
          f"R * A(0) / A(0) = {r[0]:.6f}")
    print("  so A_peak = R_i * A(0) when no other reflector interferes.")
    print("\n  three-reflector model:")
    print("  interface   R_model     A_peak       A_peak/A(0)   ratio A_i/A_1")
    ratios = [amps[j] / amps[0] for j in range(len(amps))]
    for i, (ti, a) in enumerate(zip(t2, amps), start=1):
        print(f"  {i:9d}   {r[i - 1]:+8.5f}   {a:11.5f}   {a / cc[0]:11.6f}   "
              f"{ratios[i - 1]:13.4f}")
    print(f"  model ratios R_2/R_1 = {r[1] / r[0]:.4f}, "
          f"R_3/R_1 = {r[2] / r[0]:.4f}")
    print(f"  measured ratios are {100 * (ratios[1] / (r[1] / r[0]) - 1):+.1f}% and "
          f"{100 * (ratios[2] / (r[2] / r[0]) - 1):+.1f}% away from the model:")
    print("  the autocorrelation also contains the DIFFERENCES of reflector times")
    print("  (t_2 - t_1 = 1.270 s, t_3 - t_2 = 1.690 s), which are the internal")
    print("  multiples of the stack and fall within a wavelet of the primaries.")

    section("5. Resolution: reflectors closer than the wavelet")
    print("  A pair of reflectors of opposite polarity at 2.5 s and 2.5 + dt_s.")
    print("  The question is whether the autocorrelation is two reflections or one")
    print("  tuned response.")
    k0 = int(round(0.1 / dt))
    while k0 * dt < 5.0 and np.abs(cc[k0]) > 0.5 * np.abs(cc[0]):
        k0 += 1
    print(f"\n  measured HWHM of the source autocorrelation: {k0 * dt:.3f} s")
    n_win_res = 128
    x_res = bandpass(RNG.standard_normal(L * n_win_res), FS_HZ, F1_HZ, F2_HZ)

    def response(coeffs, times):
        rec = signal.fftconvolve(x_res, reflectivity(coeffs, times, L * n_win_res,
                                                     dt))[:L * n_win_res]
        c_full = autocorr_stack(rec, dt, L, n_win_res)[L - 1:]
        return c_full[int(2.0 / dt):int(3.6 / dt)]

    base = response(np.array([0.05]), np.array([2.5]))
    a_single = np.abs(base).max()
    print(f"  reference: one reflector R = +0.05 at 2.5 s, peak amplitude "
          f"{a_single:.5f} (stack of {n_win_res} windows)")
    Rww = np.correlate(w[:L], w[:L], mode="full") / L      # source autocorrelation
    lags_win = np.arange(int(2.0 / dt), int(3.6 / dt))

    def analytic_response(coeffs, times):
        out = np.zeros(lags_win.size)
        for ci, ti in zip(coeffs, times):
            for cj, tj in zip(coeffs, times):
                k = lags_win - int(round((tj - ti) / dt))
                ok = (k >= 0) & (k < Rww.size)
                out[ok] += ci * cj * Rww[k[ok]]
        return out

    print("\n  separation (s)   A(sep)/A_single   lag of maximum (s)")
    for sep in (0.05, 0.15, 0.30, 0.60):
        w_res = response(np.array([0.05, -0.05]), np.array([2.5, 2.5 + sep]))
        win = np.abs(w_res)
        print(f"  {sep:14.2f}   {win.max() / a_single:16.3f}   "
              f"{(2.0 + np.argmax(win) * dt):18.3f}")
    print("\n  tuning curve from the analytic response (no noise):")
    seps = np.linspace(0.02, 0.60, 120)
    ratios = np.array([np.abs(analytic_response(np.array([0.05, -0.05]),
                                                np.array([2.5, 2.5 + sp]))).max()
                       / np.abs(analytic_response(np.array([0.05]),
                                                  np.array([2.5]))).max()
                       for sp in seps])
    print(f"    minimum ratio {ratios.min():.3f} at separation {seps[np.argmin(ratios)]:.3f} s")
    print(f"    maximum ratio {ratios.max():.3f} at separation {seps[np.argmax(ratios)]:.3f} s")
    print("  At separations far below the HWHM the pair is one tuned response: its")
    print("  amplitude is not the sum of the two reflection coefficients, and its")
    print("  lag is not the time of either reflector.  The tuning curve is the")
    print("  only observable there, and it is not invertible for the separation.")

    section("6. Convergence of the estimate with the number of windows")
    n_ref = 256
    x_ref = bandpass(RNG.standard_normal(L * n_ref), FS_HZ, F1_HZ, F2_HZ)
    rec_ref = signal.fftconvolve(x_ref, refl)[:L * n_ref]
    ref = autocorr_stack(rec_ref, dt, L, n_ref)
    lo, hi = L - 1 + int(5.0 / dt), L - 1 + int(20.0 / dt)
    print(f"  reference: {n_ref} windows ({n_ref * WIN_S / 3600.0:.1f} h of noise).")
    print("  rms error of an N-window estimate over the 5-20 s lag window.")
    print("\n  windows   rms error")
    ns, errs = [], []
    for k in (1, 2, 4, 8, 16, 32, 64):
        ck = autocorr_stack(record, dt, L, k)
        e = float(np.sqrt(np.mean((ck[lo:hi] - ref[lo:hi]) ** 2)))
        ns.append(k)
        errs.append(e)
        print(f"  {k:7d}   {e:.5e}")
    slope = np.polyfit(np.log10(ns), np.log10(errs), 1)[0]
    print(f"  measured slope d log(error) / d log(N) = {slope:.3f} "
          f"(1/sqrt(N) predicts -0.500)")
    print("  The estimate is a stack of incoherent contributions, so its random")
    print("  error falls as the square root of the number of windows, exactly as")
    print("  the cross-correlation of a station pair does.")


if __name__ == "__main__":
    main()