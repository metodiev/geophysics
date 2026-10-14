"""Sampling, aliasing, leakage and windowing -- measured, not asserted.

Run:  python3 aliasing_leakage_demo.py
Requires: Python standard library only.

Companion to lesson 01-10-05 (Sampling, Aliasing, Leakage and Windowing).

Convention: forward DFT with exp(-2*pi*i*k*n/N), no scaling; inverse with 1/N.
Bin spacing df = 1/(N dt) with dt the sample spacing; Nyquist f_N = 1/(2 dt).
"""

import cmath
import math


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def fft(a):
    """Iterative radix-2 FFT.  N must be a power of two."""
    n = len(a)
    a = list(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j |= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        half = length >> 1
        wl = cmath.exp(-2j * math.pi / length)
        for start in range(0, n, length):
            w = 1 + 0j
            for k in range(start, start + half):
                u = a[k]
                v = a[k + half] * w
                a[k] = u + v
                a[k + half] = u - v
                w *= wl
        length <<= 1
    return a


def magnitudes(values, pad):
    padded = [complex(v) for v in values] + [0j] * (pad - len(values))
    spec = fft(padded)
    return [abs(spec[k]) for k in range(pad // 2 + 1)]


def fold(f, fs):
    """Apparent frequency of a tone f sampled at rate fs (fold into [-fs/2, fs/2])."""
    g = (f + fs / 2.0) % fs - fs / 2.0
    return g


def windows():
    """The classic windows, plus their coherent gain (mean of the samples)."""
    return (
        ("rectangular", lambda i, n: 1.0),
        ("Hann", lambda i, n: 0.5 * (1.0 - math.cos(2 * math.pi * i / n))),
        ("Hamming", lambda i, n: 0.54 - 0.46 * math.cos(2 * math.pi * i / n)),
        ("Blackman", lambda i, n: 0.42 - 0.5 * math.cos(2 * math.pi * i / n)
         + 0.08 * math.cos(4 * math.pi * i / n)),
    )


def main():
    section("1. Aliasing: what the samples cannot tell you")
    fs = 10.0
    dt = 1.0 / fs
    n = 100
    print(f"  sampling rate fs = {fs} Hz, dt = {dt} s, Nyquist = {fs / 2} Hz")
    print(f"  {'true f':>9} {'folded f':>10} {'|samples(7Hz) - samples(f)|':>30}")
    ref = [math.cos(2 * math.pi * 7.0 * i * dt) for i in range(n)]
    for f in (7.0, -3.0, 13.0, -7.0, 3.0, 17.0, 23.0):
        cand = [math.cos(2 * math.pi * f * i * dt) for i in range(n)]
        diff = max(abs(a - b) for a, b in zip(ref, cand))
        print(f"  {f:>9.1f} {fold(f, fs):>10.2f} {diff:>30.2e}")
    print("  Every frequency in the list produces the SAME samples: 7 Hz, -3 Hz,")
    print("  13 Hz, ... are indistinguishable at this sampling rate.  The apparent")
    print("  frequency is the fold of the true frequency into [-fs/2, fs/2].")
    print("\n  Aliasing of a seismic band.  A 100 Hz event sampled at different")
    print("  rates:")
    print(f"  {'fs (Hz)':>9} {'Nyquist':>9} {'apparent f (Hz)':>17} {'aliased?':>95}")
    for rate in (1000.0, 400.0, 250.0, 200.0, 125.0, 100.0):
        d = 1.0 / rate
        sig = [math.sin(2 * math.pi * 100.0 * i * d) for i in range(int(2.0 * rate) + 1)]
        pad = 8192
        mags = magnitudes(sig, pad)
        dfp = 1.0 / (pad * d)
        kpk = max(range(1, len(mags)), key=lambda k: mags[k])
        fpk = kpk * dfp
        aliased = "no" if abs(fpk - 100.0) < 1.0 else "YES"
        print(f"  {rate:>9.1f} {rate / 2:>9.1f} {fpk:>17.2f} {aliased:>7}")

    section("2. Spatial aliasing: the same rule with dx instead of dt")
    dx = 25.0
    v = 1000.0                      # apparent velocity along the line
    f_alias = v / (2.0 * dx)
    print(f"  receiver spacing dx = {dx} m, event apparent velocity v ="
          f" {v} m/s")
    print(f"  the event is aliased above f = v/(2 dx) = {f_alias:.1f} Hz.")
    kn = math.pi / dx                          # Nyquist wavenumber
    print(f"  Nyquist wavenumber = pi/dx = {kn:.4f} rad/m.")
    print(f"  {'f (Hz)':>8} {'true k':>10} {'phase step':>11} {'folded step':>12}"
          f" {'apparent k':>11} {'apparent v (m/s)':>18}")
    for f in (10.0, 20.0, 30.0, 40.0):
        k = 2.0 * math.pi * f / v
        dphi = k * dx
        dphi_folded = fold(math.degrees(dphi), 360.0)
        k_app = math.radians(dphi_folded) / dx
        v_app = 2.0 * math.pi * f / k_app if k_app != 0.0 else float("inf")
        print(f"  {f:>8.1f} {k:>10.4f} {math.degrees(dphi):>10.1f}"
              f" {dphi_folded:>12.1f} {k_app:>11.4f} {v_app:>18.1f}")
    print("  Below v/(2 dx) the phase step between neighbouring traces is under 180")
    print("  degrees and both the dip and the velocity read correctly.  Above it the")
    print("  step folds back and the event is misread:")
    print("    20 Hz: the step is exactly 180 degrees, the limit of readability (and")
    print("           indistinguishable from -180, i.e. the opposite dip at the same")
    print("           steepness);")
    print("    30 Hz: the apparent wavenumber flips sign, so a 1000 m/s event reads")
    print("           as a 3000 m/s event dipping the other way;")
    print("    40 Hz: the step is 0, so the event reads as horizontal.")
    print("  Every one of these is a plausible-looking arrival on a section: aliasing")
    print("  does not announce itself.  Survey design chooses dx from the highest")
    print("  frequency and the slowest (steepest) event that must be recorded,")
    print("  dx <= v_min / (2 f_max).")

    section("3. Leakage: the price of a finite record")
    n = 256
    dt = 1.0 / n                     # so that T = 1 s and df = 1 Hz
    df = 1.0 / (n * dt)
    pad = 64 * n
    dfp = 1.0 / (pad * dt)
    print(f"  N = {n}, dt = {dt:.6f} s, so T = {n * dt:.3f} s and df = {df:.3f} Hz.")
    print("  A tone at the same frequency as a bin (an integer number of cycles in")
    print("  the record) needs one bin.  A tone between bins loses amplitude at the")
    print("  nearest bin and spreads across the band:")
    print(f"  {'offset (bins)':>14} {'nearest bin':>12} {'2|X|/N there':>13}"
          f" {'sinc(offset)':>13} {'error (dB)':>11} {'interpolated peak':>18}")
    for offset in (0.0, 0.25, 0.5, 0.75, 1.0):
        f0 = (40.0 + offset) * df
        sig = [math.cos(2 * math.pi * f0 * i * dt) for i in range(n)]
        mags = magnitudes(sig, pad)
        k_near = int(round(f0 / df))
        k_pad = int(round(f0 / dfp))
        k_near_pad = int(round(k_near * df / dfp))
        at_bin = 2.0 * mags[k_near_pad] / n
        delta = abs(f0 / df - k_near)
        analytic = abs(math.sin(math.pi * delta) / (math.pi * delta)) if delta else 1.0
        peak = 2.0 * mags[k_pad] / n
        print(f"  {offset:>14.2f} {k_near * df:>12.3f} {at_bin:>13.6f}"
              f" {analytic:>13.6f} {20.0 * math.log10(at_bin):>11.2f} {peak:>18.6f}")
    print("  Reading the nearest bin costs up to 3.92 dB (the 'scalloping loss' of a")
    print("  rectangular window, 2/pi = 0.6366).  The energy is not lost: it is")
    print("  spread over the neighbouring bins, and the interpolated peak recovers")
    print("  the amplitude to within 0.4% even at the worst offset.  Interpolation")
    print("  fixes the amplitude;")
    print("  it does not fix the resolution (lesson 01-10-04, Section 6).")
    print("\n  Leakage from a trend is the damaging case in geophysics, because a")
    print("  trend leaks as 1/f across the whole band.  The next experiment uses a")
    print(f"  record of 512 samples at dt = 1/128 s, so T = 4.0 s and a 3 Hz tone is")
    print("  exactly 12 cycles long -- periodic in the record, and therefore leaking")
    print("  nothing.  Anything the tone's own spectrum does not explain must come")
    print("  from the trend:")
    n, dt = 512, 1.0 / 128.0
    ramp = [1.0 + 2.0 * (i * dt) / (n * dt) for i in range(n)]
    tone = [math.sin(2 * math.pi * 3.0 * i * dt) for i in range(n)]
    trended = [a + b for a, b in zip(tone, ramp)]

    def detrend(values):
        m = len(values)
        mi = (m - 1) / 2.0
        slope = (sum((i - mi) * v for i, v in enumerate(values))
                 / sum((i - mi) ** 2 for i in range(m)))
        inter = sum(values) / m - slope * mi
        return [v - (inter + slope * i) for i, v in enumerate(values)]

    def power_law(mags, lo, hi):
        xs = [math.log(k) for k in range(lo, hi)]
        ys = [math.log(mags[k] + 1e-30) for k in range(lo, hi)]
        mx = sum(xs) / len(xs)
        my = sum(ys) / len(ys)
        return (sum((a - mx) * (b - my) for a, b in zip(xs, ys))
                / sum((a - mx) ** 2 for a in xs))

    for label, sig in (("ramp alone", ramp), ("ramp, detrended", detrend(ramp))):
        mags = magnitudes(sig, n)
        print(f"    {label:>16}: 1/f exponent over bins 4-40 ="
              f" {power_law(mags, 4, 40):+.3f}, mean |X| over bins 8-40 ="
              f" {sum(mags[8:40]) / 32.0:.3e}")
    print("  A ramp leaks with an exponent of -0.996, i.e. 1/f, and fills the whole")
    print("  band; removing the best-fit straight line reduces that level to")
    print("  round-off.  Detrending before a spectral estimate is not tidiness --")
    print("  it is the difference between measuring the signal and measuring the")
    print("  trend.")
    print("\n  Detrending is not free either.  A sampled sinusoid is not exactly")
    print("  orthogonal to a linear function over a finite record, so subtracting a")
    print("  fitted line takes a little of the signal with it:")
    sig_tone = [math.sin(2 * math.pi * 12.0 * i / n) for i in range(n)]
    for label, sig in (("tone alone", sig_tone),
                       ("tone + ramp", [a + b for a, b in zip(sig_tone, ramp)]),
                       ("tone + ramp, detrended",
                        detrend([a + b for a, b in zip(sig_tone, ramp)]))):
        mags = magnitudes(sig, n)
        amp = 2.0 * mags[12] / n
        print(f"    {label:>24}: amplitude recovered at the tone's bin"
              f" (k = 12) = {amp:.6f}")
    print("  The overlap falls as 1/N, so for long records the effect is small; for")
    print("  short ones it is a bias to be aware of.  Every processing step that")
    print("  removes something removes a little of everything.")

    section("4. Windows: main-lobe width against sidelobe level")
    n = 4096
    pad = 4 * n
    print(f"  measurements on an {n}-point window zero-padded to {pad}; the main")
    print("  lobe width is quoted in bins of the unpadded transform (1 bin = 1/T):")
    print(f"  {'window':>13} {'coherent gain':>14} {'main lobe (bins)':>17}"
          f" {'peak sidelobe (dB)':>19} {'8-30 bin max (dB)':>19}")
    results = {}
    for name, wfun in windows():
        w = [wfun(i, n) for i in range(n)]
        cg = sum(w) / n
        mags = magnitudes(w, pad)
        peak = mags[0]
        k = 1
        while k < len(mags) - 1 and mags[k + 1] < mags[k]:
            k += 1
        first_null = k
        mlw = 2.0 * first_null * (n / pad)     # in unpadded bins, null to null
        peaks = [j for j in range(first_null, len(mags) - 1)
                 if mags[j] > mags[j - 1] and mags[j] >= mags[j + 1]]
        side = [20.0 * math.log10(mags[j] / peak) for j in peaks]
        psl = max(side) if side else float("-inf")
        far_bins = [20.0 * math.log10(mags[j] / peak) for j in peaks
                    if 8 * n / pad < j * n / pad < 30]
        far = max(far_bins) if far_bins else float("-inf")
        results[name] = (cg, mlw, psl)
        print(f"  {name:>13} {cg:>14.6f} {mlw:>17.2f} {psl:>19.2f} {far:>18.2f}")
    print("  Coherent gain is what you must divide by to keep amplitudes correct:")
    print("  a Hann window halves every amplitude (0.5), Hamming 0.54, Blackman")
    print("  0.42.  Forgetting it is a silent 6 dB error.")
    print("  Narrow main lobe and low sidelobes cannot both be had: the rectangular")
    print("  window wins on width and loses badly on sidelobes, Blackman is the")
    print("  reverse.  The last column is the worst sidelobe between 8 and 30 bins")
    print("  away, which is where Hamming's slow far-field decay shows up: Hamming")
    print("  has a lower FIRST sidelobe than Hann but a higher far sidelobe.")

    section("5. What a window is worth: detecting a weak tone next to a strong one")
    n = 1024
    dt = 1.0
    strong_bin = 100.35               # deliberately between bins
    offs = 3.0
    weak_bin = strong_bin + offs
    print(f"  N = {n}, dt = 1 s.  A strong tone at bin {strong_bin} (amplitude 1),")
    print(f"  deliberately OFF the bin grid so that it leaks, and a weak tone")
    print(f"  {offs:.0f} bins away at bin {weak_bin}.  The leakage floor is the")
    print("  largest value of the strong tone's own spectrum within one bin of the")
    print("  weak tone's position -- a worst case, not a lucky null.")
    for offs, why in ((3.0, "inside the main lobe of the wider windows"),
                      (8.0, "clear of every main lobe here")):
        weak_bin = strong_bin + offs
        print(f"\n  separation {offs:.0f} bins -- {why}:")
        print(f"  {'window':>13} {'floor (rel. peak)':>17} {'floor (dB)':>11}"
              f" {'weakest a for +6 dB':>20}")
        for name, wfun in windows():
            w = [wfun(i, n) for i in range(n)]
            cg = sum(w) / n
            sig = [w[i] * math.cos(2 * math.pi * strong_bin * i / n) for i in range(n)]
            mags = magnitudes(sig, n)
            kc = int(round(weak_bin))
            peak = max(mags)
            floor = max(mags[kc - 1:kc + 2])
            rel = floor / peak
            need = None
            amp = 1e-6
            while amp < 2.0:
                sig2 = [w[i] * (math.cos(2 * math.pi * strong_bin * i / n)
                                + amp * math.cos(2 * math.pi * weak_bin * i / n))
                        for i in range(n)]
                mags2 = magnitudes(sig2, n)
                if max(mags2[kc - 1:kc + 2]) >= 2.0 * floor:
                    need = amp
                    break
                amp *= 1.1
            print(f"  {name:>13} {rel:>17.3e} {20.0 * math.log10(rel):>11.1f}"
                  f" {need:>20.3e}")
        if offs == 3.0:
            print("  At 3 bins the 'floor' for Hann and Blackman is largely the skirt")
            print("  of their own wider main lobes, and Blackman is the WORST of the")
            print("  four: a wide main lobe hides a weak nearby event just as surely as")
            print("  a high sidelobe does.")
        else:
            print("  At 8 bins the windows are ordered as their sidelobe tables")
            print("  predict, and the weak-tone threshold improves by two to three")
            print("  orders of magnitude over no window at all.")
    print("\n  'Floor' is the strong tone's own spectrum at the weak tone's position")
    print("  relative to the strong tone's peak.  'Weakest a' is the smallest weak")
    print("  amplitude that lifts the local peak to twice the floor -- a 6 dB")
    print("  criterion found by scanning the amplitude, not by asserting a rule.")
    print("  The lesson is that windowing helps when the interference is a sidelobe")
    print("  and hurts when it is the main lobe.  Choose from the physics.")

    section("6. Resolution: how deep a valley do you require?")
    n = 128
    dt = 1.0
    df = 1.0 / (n * dt)
    print(f"  N = {n}, dt = 1 s, T = {n * dt:.0f} s, df = {df:.5f} Hz.  Two equal")
    print("  tones at the centre of the band, separation given as a multiple of")
    print("  1/T.  The 'valley' is the minimum between the two peaks, relative to")
    print("  their height (0 dB = no split at all).")
    print("  Definition used: two equal tones are RESOLVED when the spectrum shows")
    print("  two local maxima, each within 1.5 bins of one of the tone frequencies,")
    print("  separated by a valley at least 3 dB below the lower of the two.  The")
    print("  separation is scanned in steps of 0.1/T to find the threshold.")
    print(f"  {'window':>13} {'threshold (x 1/T)':>18} {'depth there (dB)':>17}"
          f" {'main lobe (bins)':>17}")
    for name, wfun in windows():
        w = [wfun(i, n) for i in range(n)]
        cg = sum(w) / n
        threshold = None
        depth_at = None
        mult = 0.5
        while mult <= 4.05:
            sep = mult * df
            fa, fb = 40.0 * df, 40.0 * df + sep
            sig = [w[i] * (math.cos(2 * math.pi * fa * i * dt)
                           + math.cos(2 * math.pi * fb * i * dt)) for i in range(n)]
            pad = 16384
            mags = magnitudes(sig, pad)
            dfp = 1.0 / (pad * dt)
            ka, kb = int(round(fa / dfp)), int(round(fb / dfp))
            lo, hi = ka - 16, kb + 17
            block = mags[lo:hi]
            peaks = [j for j in range(1, len(block) - 1)
                     if block[j] > block[j - 1] and block[j] >= block[j + 1]]
            good = [j for j in peaks
                    if min(abs(lo + j - ka), abs(lo + j - kb)) <= 1.5 * df / dfp]
            ok = False
            if len(good) >= 2:
                j1, j2 = good[0], good[-1]
                valley = min(block[j1:j2 + 1])
                depth = 20.0 * math.log10(valley / min(block[j1], block[j2]))
                ok = depth < -3.0
                if ok and threshold is None:
                    threshold = mult
                    depth_at = depth
            mult = round(mult + 0.1, 10)
        # main-lobe width for this window, in unpadded bins
        wspec = magnitudes(w, 4 * n)
        k = 1
        while k < len(wspec) - 1 and wspec[k + 1] < wspec[k]:
            k += 1
        mlw = 2.0 * k * n / (4 * n)
        print(f"  {name:>13} {threshold:>18.1f} {depth_at:>17.1f} {mlw:>17.1f}")
    print("  The rectangular window resolves at about 1.2/T, close to the 1/T of")
    print("  the familiar 'Rayleigh criterion'.  A tapered window costs")
    print("  resolution: Hann and Blackman need materially more than 1/T, in")
    print("  proportion to their wider main lobes.  That is the price of the")
    print("  sidelobe suppression that made them worth using in the first place.")
    print("  The trade is unavoidable: you can suppress a strong nearby event or")
    print("  resolve a weak one, and the choice depends on which matters.")

    section("7. Summary of the numbers measured here")
    print("  Nyquist: fs > 2 f_max; apparent frequency = fold of the true frequency")
    print("    into [-fs/2, fs/2]; spatially, f_alias = v/(2 dx).")
    print("  Bin spacing: df = 1/(N dt) = 1/T.  Resolution: also 1/T, and cannot be")
    print("    improved by zero padding (lesson 01-10-04, Section 6).")
    print("  Scalloping loss, rectangular window, tone halfway between bins:"
          " -3.92 dB.")
    print("  Window trade-off, measured above: main-lobe width against sidelobe")
    print("    level, with a coherent gain that must be divided out.")
    print("  Leakage from a trend: 1/f, removed by detrending before the transform.")


if __name__ == "__main__":
    main()
