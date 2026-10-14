#!/usr/bin/env python3
"""FIR filter design by the window method, by least squares, and by
Parks-McClellan (equiripple) -- with every specification MEASURED from the
designed filter rather than assumed.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fir_filters_demo.py

Everything is SYNTHETIC.  The "specification" below is a chosen teaching
specification, not a measurement from any instrument or survey.

Contents
--------
1. The specification and how a window design uses it.
2. Window family: measured stopband attenuation and transition width.
3. Order versus attenuation: does the window rule of thumb hold?
4. Parks-McClellan equiripple versus the window method.
5. Least-squares (firls) design: passband error in an L2 sense.
6. Linear phase: the measured group delay is exactly (N-1)/2 samples.
"""

import numpy as np
from scipy import signal

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching specification ---------------------------------------
FS = 250.0            # Hz sample rate
FP = 40.0             # Hz, passband edge
FST = 60.0            # Hz, stopband edge


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def response(b, a=1.0, n=8192):
    """Frequency response on n points from 0 to Nyquist, in Hz."""
    w, h = signal.freqz(b, a, worN=n, fs=FS)
    return w, h


def measure(b, a=1.0, floor_db=60.0):
    """Return (passband ripple dB, stopband attenuation dB, transition edge Hz).

    The transition edge is the first frequency above the passband at which the
    response has fallen by floor_db, i.e. the width of the roll-off.
    """
    w, h = response(b, a)
    db = 20.0 * np.log10(np.maximum(np.abs(h), 1e-300))
    pb = w <= FP
    sb = w >= FST
    ripple = db[pb].max() - db[pb].min()
    atten = -db[sb].max()
    ref = db[pb].max()
    below = np.where((db <= ref - floor_db) & (w > FP))[0]
    f3 = w[below[0]] if below.size else np.nan
    return ripple, atten, f3


def main():
    section("1. SYNTHETIC specification")
    print(f"  sample rate fs      = {FS:.1f} Hz  (Nyquist {FS / 2:.1f} Hz)")
    print(f"  passband            = 0 to {FP:.1f} Hz (ripple target < 1 dB)")
    print(f"  stopband            = {FST:.1f} to {FS / 2:.1f} Hz (attenuation target > 60 dB)")
    print(f"  transition width    = {FST - FP:.1f} Hz")
    print("  The window method chooses ONE cutoff near the band centre and a")
    print("  window whose sidelobe level sets the achievable attenuation.")

    section("2. Window family: MEASURED attenuation and transition edge")
    print(f"  numtaps = 121 (odd -> symmetric, linear phase)")
    print("   window          ripple (dB)   atten (dB)   transition edge (~60 dB, Hz)")
    for name in ("boxcar", "hann", "hamming", "blackman", "blackmanharris"):
        b = signal.firwin(121, (FP + FST) / 2, window=name, fs=FS)
        ripple, atten, f3 = measure(b)
        edge = f"{f3:.2f}" if np.isfinite(f3) else "above -60 dB"
        print(f"   {name:<12}   {ripple:11.3f}   {atten:9.2f}   {edge:>26}")

    section("3. Order sets the transition width; the window sets the stopband floor")
    print("  Fixed Kaiser beta = 6.0, increasing order:")
    print("   numtaps   atten (dB)   transition edge (~60 dB, Hz)   roll-off width (Hz)")
    for nt in (31, 61, 121, 241):
        b = signal.firwin(nt, (FP + FST) / 2, window=("kaiser", 6.0), fs=FS)
        ripple, atten, f3 = measure(b)
        print(f"   {nt:7d}   {atten:9.2f}   {f3:26.2f}   {f3 - FP:17.2f}")
    print("  Fixed order 121 taps, increasing Kaiser beta (the floor moves):")
    print("   beta   atten (dB)   transition edge (~60 dB, Hz)")
    for beta in (0.0, 3.0, 5.0, 7.0, 9.0):
        b = signal.firwin(121, (FP + FST) / 2, window=("kaiser", beta), fs=FS)
        ripple, atten, f3 = measure(b)
        edge = f"{f3:.2f}" if np.isfinite(f3) else "never reaches -60 dB"
        print(f"   {beta:4.1f}   {atten:9.2f}   {edge:>26}")
    print("  Order buys a faster roll-off; beta (equivalently the window sidelobe")
    print("  level) buys a deeper stopband floor.  They are separate knobs.")

    section("4. Parks-McClellan (equiripple) versus window method")
    # equiripple design, weight the stopband to push attenuation up
    gpass, gstop = 1.0, 60.0
    numtaps, beta = signal.kaiserord(gstop, (FST - FP) / (FS / 2))
    b_kaiser = signal.firwin(numtaps, (FP + FST) / 2, window=("kaiser", beta), fs=FS)
    r_k, a_k, f_k = measure(b_kaiser)
    print(f"  kaiserord -> numtaps = {numtaps}, beta = {beta:.4f}")
    print(f"  window (Kaiser) : atten = {a_k:6.2f} dB, ripple = {r_k:6.3f} dB, edge {f_k:.2f} Hz")
    # remez with the same order for a like-for-like comparison
    taps = numtaps if numtaps % 2 else numtaps + 1
    bands = [0.0, FP, FST, FS / 2]
    desired = [1.0, 0.0]
    b_remez = signal.remez(taps, bands, desired, fs=FS, weight=[1.0, 20.0])
    r_p, a_p, f_p = measure(b_remez)
    print(f"  Parks-McClellan : atten = {a_p:6.2f} dB, ripple = {r_p:6.3f} dB, edge {f_p:.2f} Hz")
    print(f"  same order ({taps} taps): equiripple gains {a_p - a_k:+.2f} dB of stopband")
    print("  attenuation by spreading the error uniformly instead of concentrating it.")

    section("5. Least-squares design (firls): L2 error is not uniform")
    b_ls = signal.firls(taps, bands, [1.0, 1.0, 0.0, 0.0], fs=FS, weight=[1.0, 20.0])
    r_ls, a_ls, f_ls = measure(b_ls)
    print(f"  firls (same order): atten = {a_ls:6.2f} dB, ripple = {r_ls:6.3f} dB")
    print("  Least squares minimises the total squared error, so it can allow a")
    print("  larger local ripple than equiripple near the band edge.")

    section("6. Linear phase: measured group delay of a symmetric FIR")
    for nt in (61, 121):
        b = signal.firwin(nt, (FP + FST) / 2, window="hamming", fs=FS)
        w, h = response(b)
        phase = np.unwrap(np.angle(h))
        # group delay = -d(phase)/d(omega); work in samples via omega
        omega = 2.0 * np.pi * w / FS
        gd = -np.gradient(phase, omega)
        band = (w > 2.0) & (w < FP)
        print(f"  numtaps = {nt:3d}: theoretical (N-1)/2 = {(nt - 1) / 2:6.2f} samples")
        print(f"                 measured group delay in passband = "
              f"{gd[band].mean():6.4f} +/- {gd[band].std():.2e} samples")
    print("  Constant group delay across frequency = linear phase = no dispersion.")


if __name__ == "__main__":
    main()
