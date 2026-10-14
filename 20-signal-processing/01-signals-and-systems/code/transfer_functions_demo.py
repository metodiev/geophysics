#!/usr/bin/env python3
"""Transfer functions, poles and zeros: from a difference equation to H(z), the
meaning of pole radii, resonance in a second-order system, the Butterworth pole
pattern, discretisation by two mappings, and minimum-phase versus all-pass.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python transfer_functions_demo.py

All models and data in this module are SYNTHETIC.  The systems below are chosen
teaching transfer functions with closed-form answers, so every measured number
can be checked against algebra rather than against a recording.

Contents
--------
1.  Zeros and poles of a second-order IIR filter, and the stability test.
2.  Frequency response three ways: freqz, direct evaluation of H(z), recursion.
3.  Measured decay of the impulse response against the pole radius.
4.  Resonance of a second-order continuous system against 1/(2 zeta) and the
    exact peak 1/(2 zeta sqrt(1-zeta^2)).
5.  Butterworth N = 4: pole pattern, pole radius, and the -3 dB frequency.
6.  Discretisation: bilinear transform versus impulse invariance.
7.  Minimum-phase and all-pass factors: identical magnitude, different phase,
    different energy concentration.
8.  Group delay of the resonator.
"""

import numpy as np
from scipy import signal as sps

RNG = np.random.default_rng(20261014)

FS = 100.0          # sample rate of the discrete systems, Hz


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def iir_recursion(x, b, a):
    """Direct-form I evaluation of sum b[k]x[n-k] - sum a[k]y[n-k], a[0] = 1."""
    y = np.zeros(len(x))
    for n in range(len(x)):
        acc = 0.0
        for k in range(len(b)):
            if n - k >= 0:
                acc += b[k] * x[n - k]
        for k in range(1, len(a)):
            if n - k >= 0:
                acc -= a[k] * y[n - k]
        y[n] = acc
    return y


def main():
    section("1. A second-order IIR system: zeros, poles, stability")
    b = np.array([1.0, -0.9])                 # numerator:  1 - 0.9 z^-1
    a = np.array([1.0, -1.2, 0.5])            # denominator: 1 - 1.2 z^-1 + 0.5 z^-2
    zeros = np.roots(b)
    poles = np.roots(a)
    print("difference equation: y[n] = 1.2 y[n-1] - 0.5 y[n-2] + x[n] - 0.9 x[n-1]")
    print(f"zeros: {np.array2string(zeros, precision=6)}  |zero| = "
          f"{np.abs(zeros)}")
    print(f"poles: {np.array2string(poles, precision=6)}")
    for p in poles:
        print(f"   pole {p.real:+.6f} {p.imag:+.6f}j: |p| = {abs(p):.6f}, "
              f"angle = {np.degrees(np.angle(p)):+.3f} deg")
    print(f"causal system is stable iff every |pole| < 1: "
          f"{'STABLE' if np.all(np.abs(poles) < 1) else 'UNSTABLE'}")
    print("the pole pair has the same radius and conjugate angles, so the")
    print("impulse response is a damped oscillation at that angle")

    section("2. Frequency response three ways")
    n = 200
    impulse = np.zeros(n)
    impulse[0] = 1.0
    h = iir_recursion(impulse, b, a)
    h_expected = sps.lfilter(b, a, impulse)
    print(f"max|direct recursion - scipy.signal.lfilter| = "
          f"{np.max(np.abs(h - h_expected)):.3e}")
    for w in (0.0, np.pi / 4, np.pi / 2, np.pi):
        z = np.exp(1j * w)
        H_z = np.sum(b * z ** -np.arange(len(b))) / np.sum(a * z ** -np.arange(len(a)))
        _, H_f = sps.freqz(b, a, worN=[w])
        print(f"  w = {w:.4f} rad: H(z) = {H_z.real:+.6f}{H_z.imag:+.6f}j, "
              f"freqz = {H_f[0].real:+.6f}{H_f[0].imag:+.6f}j, "
              f"|H| = {abs(H_z):.6f}")
    print(f"  also recoverable from the impulse response: H(e^(i pi/2)) from "
          f"sum h[n]z^-n = "
          f"{np.sum(h * np.exp(-1j * np.pi / 2 * np.arange(n))).real:+.6f}"
          f"{np.sum(h * np.exp(-1j * np.pi / 2 * np.arange(n))).imag:+.6f}j")

    section("3. Impulse response decay versus the pole radius")
    p = np.max(np.abs(poles))
    mag = np.abs(h)
    tail = np.where(mag > 1e-12)[0]
    tail = tail[tail > 5]
    slope = np.polyfit(tail, np.log(mag[tail]), 1)[0]
    print(f"largest pole radius |p| = {p:.6f}")
    print(f"measured decay of ln|h[n]| with n = {slope:.6f} per sample")
    print(f"ln|p| = {np.log(p):.6f} per sample")
    print(f"a pole of radius |p| gives decay |p|^n: to fall by 60 dB takes "
          f"n = {np.log(1e-3) / np.log(p):.1f} samples = "
          f"{np.log(1e-3) / np.log(p) / FS * 1e3:.2f} ms at {FS:.0f} Hz")

    section("4. Resonance of a second-order continuous system")
    print("H(s) = w0^2 / (s^2 + 2 zeta w0 s + w0^2), w0 = 1 rad/s (SYNTHETIC)")
    w0 = 1.0
    print("   zeta    measured peak   exact w_r      1/(2 zeta)   "
          "1/(2 zeta sqrt(1-zeta^2))")
    for zeta in (0.05, 0.1, 0.25, 0.5):
        w = np.linspace(0.01, 3.0, 40000)
        _, H = sps.freqs([w0 ** 2], [1.0, 2 * zeta * w0, w0 ** 2], worN=w)
        mag = np.abs(H)
        i = int(np.argmax(mag))
        if zeta < 1 / np.sqrt(2):
            wr = w0 * np.sqrt(1 - 2 * zeta ** 2)
            peak_exact = 1.0 / (2 * zeta * np.sqrt(1 - zeta ** 2))
        else:
            wr = 0.0
            peak_exact = 1.0
        print(f"  {zeta:5.2f}   {mag[i]:12.4f}   {wr:10.4f}   "
              f"{1 / (2 * zeta):10.4f}   {peak_exact:14.4f}")
    print("the 1/(2 zeta) rule is the small-zeta limit; the exact peak sits at")
    print("w_r = w0 sqrt(1 - 2 zeta^2) and equals 1/(2 zeta sqrt(1 - zeta^2)),")
    print("and there is no peak at all for zeta >= 1/sqrt(2) = "
          f"{1 / np.sqrt(2):.6f}")

    section("5. Butterworth order 4: pole pattern and the -3 dB point")
    N = 4
    wc = 2.0                                  # rad/s
    k = np.arange(N)
    poles_s = wc * np.exp(1j * np.pi * (2 * k + N + 1) / (2 * N))
    b_but, a_but = sps.butter(N, wc, analog=True)
    poles_scipy = np.roots(a_but)
    print(f"analytic poles (radius should be wc = {wc:.1f}):")
    for p in poles_s:
        print(f"   {p.real:+.6f} {p.imag:+.6f}j   |p| = {abs(p):.6f}  "
              f"angle = {np.degrees(np.angle(p)):+.3f} deg")
    print(f"max|analytic - scipy.butter pole| = "
          f"{np.max(np.abs(np.sort_complex(poles_s) - np.sort_complex(poles_scipy))):.3e}")
    for probe in (0.1, 1.0, 2.0, 4.0):
        _, H = sps.freqs(b_but, a_but, worN=[probe])
        print(f"   |H(i{probe:5.1f})| = {np.abs(H[0]):.6f} "
              f"= {20 * np.log10(np.abs(H[0])):+8.3f} dB")
    print(f"the -3 dB point is at w = wc = {wc:.1f} rad/s: "
          f"|H| = {1 / np.sqrt(2):.6f} = {-3.0103:.4f} dB, and the roll-off is "
          f"-{20 * N:.0f} dB per decade (N = {N})")

    section("6. Discretising H(s) = 1/(s+1) at fs = 100 Hz")
    b_analog, a_analog = [1.0], [1.0, 1.0]
    b_bil, a_bil = sps.bilinear(b_analog, a_analog, fs=FS)
    b_imp, a_imp, _ = sps.cont2discrete((b_analog, a_analog), 1.0 / FS,
                                        method="impulse")
    b_imp, a_imp = np.trim_zeros(np.squeeze(b_imp), "b"), np.squeeze(a_imp)
    print(f"bilinear:            b = {np.array2string(b_bil, precision=6)}, "
          f"a = {np.array2string(a_bil, precision=6)}")
    print(f"impulse invariance:  b = {np.array2string(b_imp, precision=6)}, "
          f"a = {np.array2string(a_imp, precision=6)}")
    print("   f (Hz)   |H_analog|   |H_bilinear|   |H_impulse invariance|")
    for f in (0.5, 2.0, 10.0, 30.0, 45.0):
        _, Ha = sps.freqs(b_analog, a_analog, worN=[2 * np.pi * f])
        _, Hb = sps.freqz(b_bil, a_bil, worN=[2 * np.pi * f / FS])
        _, Hi = sps.freqz(b_imp, a_imp, worN=[2 * np.pi * f / FS])
        print(f"   {f:6.1f}   {np.abs(Ha[0]):10.6f}   {np.abs(Hb[0]):12.6f}   "
              f"{np.abs(Hi[0]):21.6f}")
    print("the bilinear transform matches the analog magnitude closely up to")
    print("about fs/10 and then compresses (warping); impulse invariance departs")
    print("because the analog response above Nyquist folds back (aliasing)")
    print("   f (Hz)   warped analog w (rad/s)   1/sqrt(1+w^2)   |H_bilinear|")
    for f in (2.0, 10.0, 30.0, 45.0):
        wd = 2 * np.pi * f / FS
        wa = 2 * FS * np.tan(wd / 2.0)
        _, Hb = sps.freqz(b_bil, a_bil, worN=[wd])
        print(f"   {f:6.1f}   {wa:20.4f}   {1 / np.sqrt(1 + wa ** 2):13.6f}   "
              f"{np.abs(Hb[0]):12.6f}")
    print("the warp w_analog = 2 fs tan(w_digital/2) is exact: pre-warping a")
    print("designed corner frequency with its inverse makes the digital filter")
    print("hit the analog specification exactly at that one frequency")

    section("7. Minimum-phase and all-pass factors")
    h_min = np.convolve([1.0, -0.5], [1.0, -0.3])     # zeros at 0.5 and 0.3
    h_max = np.convolve([-0.5, 1.0], [-0.3, 1.0])     # zeros at 2 and 10/3
    print(f"minimum-phase h = {h_min}  (zeros inside the unit circle)")
    print(f"maximum-phase h = {h_max}  (zeros outside, the same magnitudes)")
    w, H_min = sps.freqz(h_min, worN=2 ** 12)
    _, H_max = sps.freqz(h_max, worN=2 ** 12)
    print(f"max difference of the two magnitude spectra = "
          f"{np.max(np.abs(np.abs(H_min) - np.abs(H_max))):.3e}")
    for wi in (0.0, 0.5, 1.0):
        p_min = np.angle(np.sum(h_min * np.exp(-1j * wi * np.arange(len(h_min)))))
        p_max = np.angle(np.sum(h_max * np.exp(-1j * wi * np.arange(len(h_max)))))
        print(f"   phase at w = {wi:.1f} rad: minimum-phase {p_min:+.6f} rad, "
              f"maximum-phase {p_max:+.6f} rad")
    print("   partial energy in the first L samples:")
    for L in (1, 2, 3):
        e_min = np.sum(h_min[:L] ** 2)
        e_max = np.sum(h_max[:L] ** 2)
        print(f"     L = {L}: minimum-phase {e_min:8.6f}, maximum-phase "
              f"{e_max:8.6f}, ratio {e_min / e_max:6.3f}")
    print("both factors have the same magnitude spectrum; only the phase (and")
    print("therefore the energy concentration in time) differs")

    section("8. Group delay of the resonator")
    w, H = sps.freqz(b, a, worN=2 ** 14)
    phase = np.unwrap(np.angle(H))
    gd = -np.gradient(phase, w)
    i = int(np.argmax(gd))
    print(f"group delay at its maximum (w = {w[i]:.4f} rad): {gd[i]:.3f} samples "
          f"= {gd[i] / FS * 1e3:.3f} ms at {FS:.0f} Hz")
    _, Hn = sps.freqz(b, [1.0], worN=[1e-6])
    _, Hd = sps.freqz([1.0], a, worN=[1e-6])
    gd_num = -np.angle(Hn[0]) / 1e-6
    gd_den = -np.angle(Hd[0]) / 1e-6
    print(f"at w -> 0 the total group delay is {gd[0]:.6f} samples, made of "
          f"numerator {gd_num:+.4f} and denominator {gd_den:+.4f}")
    print("the numerator's zero at z = 0.9 sits close to z = 1 and contributes")
    print("a large NEGATIVE delay near DC; this is not acausality but the")
    print("reshaping of a pulse by the numerator. The peak delay of")
    print(f"{gd[i]:.3f} samples at the resonance is the part that delays the")
    print("resonant band, i.e. dispersion produced by the filter, not by the Earth")


if __name__ == "__main__":
    main()
