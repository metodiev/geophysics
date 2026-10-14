#!/usr/bin/env python3
"""Window functions and spectral leakage control: the metric table (measured from
the windows scipy builds, not copied from a table), the analytic ENBW of the
cosine-sum windows, leakage-limited detection beside a strong tone, two-tone
resolution, and a Kaiser beta sweep.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python windowing_advanced_demo.py

All models and data in this module are SYNTHETIC.  Every metric is computed from
the window itself by zero-padded DTFT, so a reader can reproduce each number.

Contents
--------
1.  Metric table: coherent gain, ENBW, highest sidelobe, sidelobe roll-off,
    scalloping loss, 3 dB and 6 dB bandwidth, worst-case process loss.
2.  Analytic ENBW for the cosine-sum windows against the measurement.
3.  Leakage floor beside a strong half-bin-off tone, and the weak-tone amplitude
    ratio needed for a 3 dB detection at a stated distance.
4.  Two-tone resolution: the separation at which the dip reaches 3 dB, measured
    on a zero-padded spectrum so the dip itself is resolved.
5.  Kaiser beta sweep: one knob, the sidelobe/ENBW trade.
6.  Flat-top versus resolution: the amplitude a naive peak-read returns.
"""

import numpy as np
from scipy import signal as sps

RNG = np.random.default_rng(20261014)

FS = 100.0
DT = 1.0 / FS
N_WIN = 1024
NPAD = 2 ** 18
PAD_FACTOR = NPAD / N_WIN


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def dense_spectrum(w, x=None, factor=64):
    """|DTFT| of the window (or of window times x) on a factor-times-fine grid.

    Returns the offset in bins of 1/N (N = len(w)) and the linear magnitude.
    """
    n = len(w)
    signal_ = w if x is None else w * x
    X = np.fft.rfft(signal_, n * factor)
    bins = np.arange(len(X)) / factor
    return bins, np.abs(X)


def metrics(w):
    n = len(w)
    coherent_gain = float(np.mean(w))
    enbw = n * np.sum(w ** 2) / np.sum(w) ** 2
    bins, mag = dense_spectrum(w)
    mag = mag / mag[0]
    # first null: cross -10 dB, then take the first local minimum
    below = np.where(mag < 0.3)[0]
    k = int(below[0]) if below.size else 1
    while k + 1 < len(mag) and mag[k + 1] < mag[k]:
        k += 1
    main_end = max(k, 1)
    highest_sidelobe = float(mag[main_end:].max())
    # sidelobe envelope level at 10 bins from the centre (dB), and the fitted
    # decay between 3 and 40 bins
    grid = np.logspace(np.log10(3.0), np.log10(40.0), 30)
    env = np.array([mag[(bins >= g / 1.15) & (bins <= g * 1.15)].max()
                    for g in grid])
    near10 = float(mag[(bins >= 9.0) & (bins <= 11.0)].max())
    try:
        rolloff = float(np.polyfit(np.log10(grid), 20 * np.log10(env), 1)[0]
                        / np.log10(2.0))
    except Exception:
        rolloff = float("nan")
    # bandwidths, in bins of 1/N
    bw3 = float(bins[np.argmin(np.abs(mag - 1 / np.sqrt(2)))])
    bw6 = float(bins[np.argmin(np.abs(mag - 0.5))])
    # scalloping loss: worst case over the fractional bin offset
    offs = np.linspace(0.0, 0.5, 101)
    scal = min(abs(np.sum(w * np.exp(-2j * np.pi * o * np.arange(n) / n)))
               / abs(np.sum(w)) for o in offs)
    return dict(cgain=coherent_gain, enbw=enbw, side=highest_sidelobe,
                near10=near10, rolloff=rolloff, bw3=bw3, bw6=bw6,
                scal=float(scal), process_loss=coherent_gain * float(scal))


def main():
    section("1. The metric table, measured from each window")
    windows = {
        "rectangular": sps.windows.boxcar(N_WIN),
        "Hann": sps.windows.hann(N_WIN, sym=False),
        "Hamming": sps.windows.hamming(N_WIN, sym=False),
        "Blackman": sps.windows.blackman(N_WIN, sym=False),
        "Kaiser b=8.6": sps.windows.kaiser(N_WIN, 8.6, sym=False),
        "flat-top": sps.windows.flattop(N_WIN, sym=False),
    }
    print(f"window of {N_WIN} samples; ENBW and bandwidths in bins of 1/N")
    print("'sidelobe at 10 bins' is the envelope level 10 bins from the centre, a")
    print("robust proxy for how fast the sidelobes decay")
    print("window         cgain     ENBW   high sidelobe   sidelobe   scallop"
          "   3 dB    6 dB")
    print("                                    (dB)          at 10 bins   (dB)"
          "     (bins)  (bins)")
    print("                                                      (dB)")
    for name, w in windows.items():
        m = metrics(w)
        print(f"{name:13s}  {m['cgain']:.6f}  {m['enbw']:6.4f}  "
              f"{20 * np.log10(m['side']):13.2f}   "
              f"{20 * np.log10(m['near10']):10.2f}   "
              f"{20 * np.log10(m['scal']):7.2f}   {m['bw3']:6.3f}  {m['bw6']:7.3f}")
    print("worst-case process loss = coherent gain x scalloping:")
    for name, w in windows.items():
        m = metrics(w)
        print(f"   {name:13s}: {m['process_loss']:.6f} = "
              f"{20 * np.log10(m['process_loss']):+7.2f} dB")

    section("2. Analytic ENBW of the cosine-sum windows")
    print("   window     measured ENBW    classical value")
    for name, w, classic in (("Hann", sps.windows.hann(N_WIN, sym=False), 1.5),
                             ("Hamming", sps.windows.hamming(N_WIN, sym=False),
                              1.3628),
                             ("Blackman",
                              sps.windows.blackman(N_WIN, sym=False), 1.7269)):
        print(f"   {name:10s}   {metrics(w)['enbw']:12.6f}   {classic:15.4f}")
    print("ENBW is a moment of the window, so it is nearly independent of the")
    print("length; the small differences are the finite-length corrections")

    section("3. Leakage beside a strong tone, and the weak-tone amplitude needed")
    n = 1024
    t = np.arange(n) * DT
    df = FS / n
    f_strong = 20.0 + 0.5 * df
    distance_bins = 20
    f_probe = f_strong + distance_bins * df
    x_strong = np.sin(2 * np.pi * f_strong * t)
    print(f"strong tone of amplitude 1 at {f_strong:.4f} Hz (half a bin off)")
    print(f"probe bin {distance_bins} bins away, at {f_probe:.4f} Hz")
    print("   window         leakage floor at the probe   amplitude ratio for")
    print("                  relative to the peak (dB)    a 3 dB detection")
    for name, w in windows.items():
        _, P = sps.periodogram(x_strong, fs=FS, window=w, detrend=False,
                               scaling="spectrum")
        freqs = np.fft.rfftfreq(n, d=DT)
        idx = int(np.argmin(np.abs(freqs - f_probe)))
        floor_db = 10 * np.log10(P[idx] / P.max())
        ratio_needed = np.sqrt(2.0 * 10 ** (floor_db / 10))
        print(f"   {name:13s}  {floor_db:29.1f}   {ratio_needed:18.3e}")
    print("the leakage floor is what limits how weak a nearby tone can be: the")
    print("needed amplitude ratio is sqrt(2 x the floor ratio), the 2 being a")
    print("3 dB detection margin")

    section("4. Two-tone resolution: the phase-averaged dip between two tones")
    print("two equal tones of the same amplitude and random relative phase;")
    print("averaging over the phase makes the spectrum |W(f-f1)|^2 + |W(f-f2)|^2,")
    print("which is computed here exactly by adding two copies of the kernel")
    seps_search = np.arange(0.5, 4.01, 0.05)
    print("   window         smallest separation with a -3 dB dip   dip at 2 bins")
    for name, w in windows.items():
        n = len(w)
        factor = 64
        X = np.fft.fftshift(np.fft.fft(w, n * factor))
        c = len(X) // 2
        kern = (np.abs(X) / np.abs(X[c])) ** 2
        found = None
        dip_at_two = float("nan")
        for sep in seps_search:
            shift = int(round(sep * factor))
            total = kern.copy()
            total[shift:] += kern[:len(kern) - shift]        # copy at +sep
            total[:len(kern) - shift] += kern[shift:]        # copy at -sep
            lo, hi = c, c + shift
            p1 = total[lo - 16:lo + 17].max()
            p2 = total[hi - 16:hi + 17].max()
            dip = total[lo + 1:hi].min()
            depth = (20 * np.log10(dip / max(p1, p2)) if dip > 0 else -np.inf)
            if abs(sep - 2.0) < 1e-9:
                dip_at_two = depth
            if depth <= -3.0 and found is None:
                found = sep
        txt = f"{found:.2f} bins" if found is not None else "not reached"
        print(f"   {name:13s}  {txt:>31s}   {dip_at_two:8.2f} dB")
    print("the usual criterion is a dip of -3 dB, and the resolution tracks the")
    print("width of the main lobe: the rectangular window resolves the earliest,")
    print("the flat-top the latest, and the ENBW table above says the same thing a")
    print("different way")

    section("5. Kaiser beta sweep: one knob, one trade")
    print("   beta    ENBW (bins)   highest sidelobe (dB)   scalloping (dB)"
          "   cgain")
    for beta in (0.0, 3.0, 6.0, 8.6, 12.0, 16.0):
        w = sps.windows.kaiser(N_WIN, beta, sym=False)
        m = metrics(w)
        print(f"   {beta:5.1f}   {m['enbw']:11.4f}   "
              f"{20 * np.log10(m['side']):22.2f}   "
              f"{20 * np.log10(m['scal']):15.2f}   {m['cgain']:.4f}")
    print("beta = 0 is the rectangular window; increasing beta buys sidelobe")
    print("suppression and pays in ENBW, monotonically. That measured trade is the")
    print("whole design rule for this family")

    section("6. Flat-top versus resolution: the amplitude a grid reading returns")
    n = 1024
    t = np.arange(n) * DT
    df = FS / n
    bin_base = 204                                # 204 x df = 19.921875 Hz
    print(f"a unit-amplitude tone read at the nearest DFT bin; bin {bin_base} = "
          f"{bin_base * df:.6f} Hz")
    print("   offset (bins)   amplitude read:")
    print("                   rectangular    Hann    flat-top")
    for offset in (0.0, 0.25, 0.5):
        f = (bin_base + offset) * df
        x = np.sin(2 * np.pi * f * t)
        k0 = bin_base
        row = []
        for name in ("rectangular", "Hann", "flat-top"):
            w = windows[name]
            X = np.fft.fft(w * x)
            peak = np.abs(X[k0:k0 + 2]).max()
            row.append(2.0 * peak / np.sum(w))
        print(f"   {offset:12.2f}   {row[0]:12.6f}   {row[1]:7.4f}   "
              f"{row[2]:9.6f}")
    print("the recovered amplitude is 2 max|DFT(w x)| over the two nearest bins")
    print("divided by sum(w), the textbook amplitude-spectrum normalisation. The")
    print("rectangular window loses the full 2/pi = 0.6366 factor at a half-bin")
    print("offset, Hann about 0.85, and the flat-top stays at 1.000 to three")
    print("decimal places; the flat-top's ENBW of 3.77 bins is what that costs")


if __name__ == "__main__":
    main()
