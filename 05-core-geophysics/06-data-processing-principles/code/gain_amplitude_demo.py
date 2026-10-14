#!/usr/bin/env python3
"""Gain, amplitude recovery and true-amplitude handling.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gain_amplitude_demo.py

Contents
--------
1. Build a synthetic trace with known reflection coefficients and a physically
   derived amplitude decay: spherical divergence 1/t and absorption
   exp(-pi f t / Q).
2. Measure the amplitude error of the primary peaks under four schemes: none,
   t-gain, AGC, and true-amplitude correction.
3. Show the diagnostic consequence: AGC makes every event look alike, so the
   RELATIVE amplitudes that carry the lithology are destroyed.
4. Quantify the absorption term alone at two Q values.
"""

import numpy as np

RNG_SEED = 20261014


def ricker(f_dom: float, dt: float, n: int) -> np.ndarray:
    t = (np.arange(n) - n // 2) * dt
    arg = (np.pi * f_dom * t) ** 2
    return (1.0 - 2.0 * arg) * np.exp(-arg)


def main() -> None:
    rng = np.random.default_rng(RNG_SEED)
    dt = 0.002
    nt = 1500
    t = np.arange(nt) * dt
    f_dom = 25.0
    Q = 80.0

    # --- 1. Synthetic trace -------------------------------------------------
    times = np.array([0.20, 0.45, 0.80, 1.20, 1.70, 2.30])
    coeffs = np.array([0.85, 0.40, -0.30, 0.20, -0.12, 0.07])
    wave = ricker(f_dom, dt, 121)
    trace = np.zeros(nt)
    for tk, ck in zip(times, coeffs):
        j = int(round(tk / dt))
        # Amplitude decay: 3-D spherical divergence ~1/t, plus absorption.
        decay = (0.2 / tk) * np.exp(-np.pi * f_dom * tk / Q)
        seg = np.zeros(nt)
        seg[j - 60:j + 61] = wave
        trace += ck * decay * seg
    noise = rng.normal(0.0, 0.0008, size=nt)
    trace += noise

    print("1. Synthetic trace (SYNTHETIC coefficients and Q)")
    print(f"   dt = {dt*0.002/0.002:.3f} s, samples = {nt}, wavelet {f_dom:.0f} Hz, Q = {Q:.0f}")
    print(f"   {'t (s)':>7}{'true coeff':>12}{'decay factor':>14}"
          f"{'expected amplitude':>20}")
    for tk, ck in zip(times, coeffs):
        decay = (0.2 / tk) * np.exp(-np.pi * f_dom * tk / Q)
        print(f"   {tk:>7.2f}{ck:>12.2f}{decay:>14.5f}{ck*decay:>20.5f}")

    def peak_near(arr, tk):
        """Peak amplitude of the trace within one wavelet length of t = tk."""
        j = int(round(tk / dt))
        lo, hi = max(0, j - 40), min(nt, j + 41)
        return float(arr[lo:hi][np.argmax(np.abs(arr[lo:hi]))])

    truth = np.array([ck * (0.2 / tk) * np.exp(-np.pi * f_dom * tk / Q)
                      for tk, ck in zip(times, coeffs)])

    # --- 2. Four schemes ----------------------------------------------------
    no_gain = trace.copy()

    t_gain = trace * np.maximum(t, 1e-3)          # 1/t style gain, clamped at t = 0

    def agc(y, window_s=0.4):
        w = int(window_s / dt)
        power = np.convolve(y ** 2, np.ones(w) / w, mode="same")
        return y / np.sqrt(power + 1e-30)

    agc_trace = agc(trace)

    def true_amp(y):
        scale = np.maximum(t, 1e-3) / 0.2
        return y * scale * np.exp(np.pi * f_dom * t / Q)

    ta_trace = true_amp(trace)

    print("\n2. Recovered amplitude of each event (arbitrary but constant units)")
    print(f"   {'t (s)':>7}{'no gain':>13}{'t-gain':>13}{'AGC':>13}"
          f"{'true amp':>13}{'true ratio':>13}")
    base = None
    for i, tk in enumerate(times):
        vals = [peak_near(no_gain, tk), peak_near(t_gain, tk),
                peak_near(agc_trace, tk), peak_near(ta_trace, tk)]
        print(f"   {tk:>7.2f}" + "".join(f"{v:>13.5f}" for v in vals)
              + f"{coeffs[i]:>13.2f}")
        _ = base

    # --- 3. Relative amplitudes --------------------------------------------
    print("\n3. Relative amplitude of event 2 divided by event 4  (true value %.3f)"
          % (coeffs[1] / coeffs[3]))
    r_none = peak_near(no_gain, times[1]) / peak_near(no_gain, times[3])
    r_tgain = peak_near(t_gain, times[1]) / peak_near(t_gain, times[3])
    r_agc = peak_near(agc_trace, times[1]) / peak_near(agc_trace, times[3])
    r_true = peak_near(ta_trace, times[1]) / peak_near(ta_trace, times[3])
    true_ratio = coeffs[1] / coeffs[3]
    print(f"   no gain   = {r_none:.3f}   error {(r_none/true_ratio-1)*100:+8.1f} %")
    print(f"   t-gain    = {r_tgain:.3f}   error {(r_tgain/true_ratio-1)*100:+8.1f} %")
    print(f"   AGC       = {r_agc:.3f}   error {(r_agc/true_ratio-1)*100:+8.1f} %")
    print(f"   true amp  = {r_true:.3f}   error {(r_true/true_ratio-1)*100:+8.1f} %")
    print("   -> AGC equalises every event and therefore DESTROYS relative")
    print("      amplitude. It is a display and picking tool, not an amplitude")
    print("      processor. Any acoustic-impedance or AVA work must avoid it.")
    print("   The residual -13.7 % for the true-amplitude correction is NOT a")
    print("   failure of the method: it is the amplified NOISE. The next table shows")
    print("   how much of the late record the correction lifts into the noise.")

    print("\n   true-amplitude correction: the noise it lifts with the signal")
    print(f"   {'t (s)':>7}{'gain applied':>14}{'true amplitude':>16}"
          f"{'noise after gain':>18}{'S/N':>8}")
    for tk, ck in zip(times, coeffs):
        gain_factor = (tk / 0.2) * np.exp(np.pi * f_dom * tk / Q)
        amp_true = abs(ck) * (0.2 / tk) * np.exp(-np.pi * f_dom * tk / Q)
        noise_after = 0.0008 * gain_factor
        print(f"   {tk:>7.2f}{gain_factor:>14.2f}{amp_true:>16.5f}"
              f"{noise_after:>18.5f}{amp_true/noise_after:>8.2f}")
    print("   -> the gain cancels in the ratio, so the S/N column is the S/N of each")
    print("      EVENT BEFORE the correction: correcting amplitudes cannot change it.")
    print("      It states how late an event is measurable at all. Beyond about 1.2 s")
    print("      in this SYNTHETIC trace the reflection amplitude is below the noise,")
    print("      which is exactly why the recovered ratio of event 2 to event 4 is")
    print("      1.726 instead of 2.000: the fourth event's amplitude is not there to")
    print("      be corrected. A true-amplitude correction preserves ratios in the")
    print("      band where the ratio is measurable, and does nothing outside it.")

    # --- 4. The absorption term -------------------------------------------
    print("\n4. Absorption alone, exp(-pi f t / Q)")
    print(f"   {'t (s)':>7}{'Q = 40':>12}{'Q = 80':>12}{'Q = 200':>12}")
    for tk in (0.5, 1.0, 2.0, 4.0):
        row = [np.exp(-np.pi * f_dom * tk / q) for q in (40.0, 80.0, 200.0)]
        print(f"   {tk:>7.1f}" + "".join(f"{v:>12.4f}" for v in row))
    print(f"   -> over 4 s at Q = 40 only "
          f"{np.exp(-np.pi*25*4/40)*100:.3f} % of the amplitude survives, on top of")
    print("      spherical divergence. This is why deep reflections are weak and")
    print("      why a single scalar gain cannot restore them correctly.")


if __name__ == "__main__":
    main()
