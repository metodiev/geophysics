#!/usr/bin/env python3
"""IIR filter design: Butterworth, Chebyshev I, Chebyshev II and elliptic -- the
order each needs for one specification, MEASURED attenuation, stability from the
pole locations, and the phase non-linearity that causal IIR filters impose.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python iir_filters_demo.py

Everything is SYNTHETIC.  The specification is a chosen teaching specification.

Contents
--------
1. Specification and the order each prototype needs (buttord/cheb1ord/...).
2. Measured passband ripple and stopband attenuation for the designed filters.
3. Stability: pole magnitudes against the unit circle.
4. Phase: the group delay is NOT constant; measure how non-linear it is.
5. IIR versus FIR: order for the same job, and what the order buys and costs.
"""

import numpy as np
from scipy import signal

RNG = np.random.default_rng(20261014)

FS = 250.0
FP = 40.0
FST = 60.0
RP = 1.0     # dB passband ripple allowed
RS = 60.0    # dB stopband attenuation required


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def measure(b, a):
    w, h = signal.freqz(b, a, worN=8192, fs=FS)
    db = 20.0 * np.log10(np.maximum(np.abs(h), 1e-300))
    pb = w <= FP
    sb = w >= FST
    return db[pb].max() - db[pb].min(), -db[sb].max()


def group_delay_variation(b, a):
    """Peak-to-peak group delay over the passband, in samples."""
    w, h = signal.freqz(b, a, worN=8192, fs=FS)
    omega = 2.0 * np.pi * w / FS
    phase = np.unwrap(np.angle(h))
    gd = -np.gradient(phase, omega)
    band = (w > 2.0) & (w < FP)
    return gd[band].max() - gd[band].min(), gd[band].mean()


def main():
    section("1. SYNTHETIC specification and the order each prototype needs")
    print(f"  fs = {FS:.1f} Hz, passband edge {FP:.1f} Hz, stopband edge {FST:.1f} Hz")
    print(f"  passband ripple <= {RP:.1f} dB, stopband attenuation >= {RS:.1f} dB")
    orders = {
        "butter": signal.buttord(FP, FST, RP, RS, fs=FS)[0],
        "cheby1": signal.cheb1ord(FP, FST, RP, RS, fs=FS)[0],
        "cheby2": signal.cheb2ord(FP, FST, RP, RS, fs=FS)[0],
        "ellip": signal.ellipord(FP, FST, RP, RS, fs=FS)[0],
    }
    print("   prototype     minimum order for the specification")
    for name, order in orders.items():
        print(f"   {name:<10}    {int(order):4d}")

    section("2. MEASURED ripple and attenuation of the designed filters")
    designs = {
        "butter": signal.butter(orders["butter"], FP, btype="low", fs=FS),
        "cheby1": signal.cheby1(orders["cheby1"], RP, FP, btype="low", fs=FS),
        "cheby2": signal.cheby2(orders["cheby2"], RS, FST, btype="low", fs=FS),
        "ellip": signal.ellip(orders["ellip"], RP, RS, FP, btype="low", fs=FS),
    }
    print("   prototype   ripple (dB)   attenuation (dB)")
    for name, (b, a) in designs.items():
        r, at = measure(b, a)
        print(f"   {name:<10}   {r:9.3f}   {at:14.2f}")
    print("  Butterworth is monotonic in both bands; Chebyshev I ripples the")
    print("  passband, Chebyshev II the stopband, elliptic ripples both -- and each")
    print("  trade buys order.")

    section("3. Stability: poles must lie strictly inside the unit circle")
    print("   prototype   max |pole|   stable?")
    for name, (b, a) in designs.items():
        poles = np.roots(a)
        mx = np.abs(poles).max()
        print(f"   {name:<10}   {mx:10.6f}   {'yes' if mx < 1.0 else 'NO'}")

    section("4. Phase: group delay is not constant for a causal IIR")
    print("   prototype   passband group delay (samples)   variation (samples)")
    for name, (b, a) in designs.items():
        var, mean = group_delay_variation(b, a)
        print(f"   {name:<10}   {mean:26.3f}   {var:21.3f}")
    print("  A causal IIR filter cannot have exactly linear phase: its poles are")
    print("  not symmetric about the unit circle.  The variation above is the")
    print("  dispersion the filter adds to the waveform.")

    section("5. IIR versus FIR for the same specification")
    gpass, gstop = RP, RS
    fir_taps, beta = signal.kaiserord(gstop, (FST - FP) / (FS / 2))
    b_fir = signal.firwin(fir_taps, (FP + FST) / 2, window=("kaiser", beta), fs=FS)
    r_fir, a_fir = measure(b_fir, 1.0)
    print(f"  FIR (Kaiser) : {fir_taps} taps, attenuation {a_fir:.2f} dB, "
          f"constant group delay {(fir_taps - 1) / 2:.1f} samples")
    ell_b, ell_a = designs["ellip"]
    print(f"  elliptic IIR : order {int(orders['ellip'])} -> "
          f"{max(len(ell_a), len(ell_b)) - 1} poles, "
          f"attenuation {measure(ell_b, ell_a)[1]:.2f} dB, non-constant delay")
    print(f"  the FIR needs ~{fir_taps / (max(len(ell_a), len(ell_b)) - 1):.1f}x more")
    print("  coefficients; the IIR buys efficiency but gives up linear phase.")


if __name__ == "__main__":
    main()
