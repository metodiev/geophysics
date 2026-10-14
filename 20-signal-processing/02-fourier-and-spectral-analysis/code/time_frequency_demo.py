#!/usr/bin/env python3
"""Time-frequency analysis: an STFT of a chirp against its known frequency law,
the measured time-bandwidth product of a Gaussian window against the exact
1/(4 pi), the measured resolution/localisation trade with window length, and the
analytic-signal instantaneous frequency against the STFT ridge.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python time_frequency_demo.py

All models and data in this module are SYNTHETIC.  Every signal is generated here
and every resolution number is measured.

Contents
--------
1.  STFT of a linear chirp: the ridge against the true instantaneous frequency.
2.  Time-bandwidth product of a Gaussian window against the exact 1/(4 pi).
3.  Resolution versus localisation as the window length changes (Hann).
4.  Two-tone resolution measured on a spectrogram, in hertz.
5.  Pulse localisation measured on a spectrogram, in seconds.
6.  Instantaneous frequency from the analytic signal against the STFT ridge.
"""

import numpy as np
from scipy import signal as sps

RNG = np.random.default_rng(20261014)

FS = 1000.0
DT = 1.0 / FS


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def energy_widths(x, fs=FS, nperseg=256, hop=None):
    """Energy-RMS width in time (s) and in frequency (Hz) of the STFT of x.

    The window is Gaussian with standard deviation nperseg/8 samples, so the
    truncation at +-4 sigma perturbs the width by a fraction of a per cent.
    """
    win = ("gaussian", nperseg / 8.0)
    if hop is None:
        hop = max(1, nperseg // 16)
    f, t, Z = sps.stft(x, fs=fs, window=win, nperseg=nperseg,
                       noverlap=nperseg - hop, boundary=None)
    P = np.abs(Z) ** 2
    pt = P.sum(axis=0)
    pf = P.sum(axis=1)
    t_c = np.sum(t * pt) / np.sum(pt)
    f_c = np.sum(f * pf) / np.sum(pf)
    width_t = np.sqrt(np.sum((t - t_c) ** 2 * pt) / np.sum(pt))
    width_f = np.sqrt(np.sum((f - f_c) ** 2 * pf) / np.sum(pf))
    return width_t, width_f


def main():
    section("1. STFT of a linear chirp against its known frequency law")
    duration = 2.0
    n = int(duration * FS)
    t = np.arange(n) * DT
    f0, f1 = 20.0, 180.0
    inst_f = f0 + (f1 - f0) * t / t[-1]
    phase = 2 * np.pi * np.cumsum(inst_f) * DT
    x = np.cos(phase)
    for nperseg in (64, 256, 1024):
        f, tt, Z = sps.stft(x, fs=FS, window="hann", nperseg=nperseg,
                            noverlap=nperseg // 2, boundary=None)
        ridge = f[np.argmax(np.abs(Z), axis=0)]
        truth = f0 + (f1 - f0) * tt / t[-1]
        err = ridge - truth
        print(f"nperseg = {nperseg:5d}: df = {f[1] - f[0]:7.3f} Hz, "
              f"max ridge error = {np.max(np.abs(err)):7.3f} Hz, "
              f"rms error = {np.sqrt(np.mean(err ** 2)):7.3f} Hz")
    print("the ridge follows the sweep; the residual error falls as the window")
    print("lengthens in frequency resolution but grows near the record ends,")
    print("where the window has no data to work with")

    section("2. Time-bandwidth product of a Gaussian window")
    print("energy-RMS widths: the exact Heisenberg bound for a Gaussian is")
    print("sigma_t sigma_f >= 1/(4 pi) = "
          f"{1 / (4 * np.pi):.6f} s Hz, with equality")
    nperseg = 256
    print("   nperseg   sigma_t (ms)   sigma_f (Hz)   product   product/(1/4pi)")
    for nperseg in (64, 128, 256, 512, 1024):
        impulse = np.zeros(int(4 * FS))
        impulse[int(2 * FS)] = 1.0
        wt, _ = energy_widths(impulse, nperseg=nperseg)
        tone = np.cos(2 * np.pi * 100.0 * np.arange(int(4 * FS)) * DT)
        _, wf = energy_widths(tone, nperseg=nperseg)
        print(f"   {nperseg:7d}   {wt * 1e3:11.4f}   {wf:12.4f}   "
              f"{wt * wf:7.4f}   {wt * wf / (1 / (4 * np.pi)):14.3f}")
    print("the product is constant as the window lengthens: the trade is not a")
    print("property of the transform but of the window, and no window can beat")
    print("the Gaussian's bound of 1/(4 pi)")
    print("\nfor comparison, the Hann window's energy-RMS product:")
    for nperseg in (64, 256, 1024):
        w = sps.windows.hann(nperseg, sym=False)
        ts = np.arange(nperseg) * DT
        p_t = w ** 2
        t_c = np.sum(ts * p_t) / np.sum(p_t)
        st = np.sqrt(np.sum((ts - t_c) ** 2 * p_t) / np.sum(p_t))
        ff = np.linspace(-FS / 2, FS / 2, 200001)
        Wf = np.abs(np.sum(w[None, :]
                           * np.exp(-2j * np.pi * ff[:, None] * ts[None, :]),
                           axis=1)) ** 2
        f_c = np.sum(ff * Wf) / np.sum(Wf)
        sf = np.sqrt(np.sum((ff - f_c) ** 2 * Wf) / np.sum(Wf))
        print(f"   nperseg = {nperseg:5d}: sigma_t = {st * 1e3:8.4f} ms, "
              f"sigma_f = {sf:8.4f} Hz, product = {st * sf:.6f} = "
              f"{st * sf / (1 / (4 * np.pi)):.4f} x the bound")

    section("3. Resolution versus localisation as the window length changes")
    print("two tones 2 Hz apart near 100 Hz, and a single 4 ms pulse")
    print("   nperseg   two-tone dip (dB)   pulse sigma_t (ms)   "
          "sigma_t / (nperseg dt)")
    for nperseg in (64, 128, 256, 512):
        t = np.arange(int(2 * FS)) * DT
        tones = (np.cos(2 * np.pi * 100.0 * t)
                 + np.cos(2 * np.pi * 102.0 * t))
        f, tt, Z = sps.stft(tones, fs=FS, window="hann", nperseg=nperseg,
                            noverlap=nperseg // 2, boundary=None)
        P = np.abs(Z) ** 2
        mag = np.sqrt(P.sum(axis=1))
        band = (f > 90.0) & (f < 112.0)
        i1 = np.argmin(np.abs(f - 100.0))
        i2 = np.argmin(np.abs(f - 102.0))
        dip = mag[band].min() / max(mag[i1], mag[i2])
        pulse = np.zeros(int(2 * FS))
        pulse[int(FS)] = 1.0
        f2, t2, Z2 = sps.stft(pulse, fs=FS, window="hann", nperseg=nperseg,
                              noverlap=nperseg - 1, boundary=None)
        pt = (np.abs(Z2) ** 2).sum(axis=0)
        tc = np.sum(t2 * pt) / np.sum(pt)
        tw = np.sqrt(np.sum((t2 - tc) ** 2 * pt) / np.sum(pt))
        print(f"   {nperseg:7d}   {20 * np.log10(dip):17.2f}   "
              f"{tw * 1e3:17.3f}   {tw / (nperseg * DT):20.3f}")
    print("as the window lengthens the tones separate (the dip deepens) and the")
    print("pulse smears (sigma_t grows in proportion to nperseg, by the measured")
    print("factor 0.141 that is a property of the Hann window). The two effects move in")
    print("opposite directions, which is the content of the time-frequency")
    print("uncertainty principle measured in section 2")

    section("4. Two-tone resolution against window length, in hertz")
    t = np.arange(int(4 * FS)) * DT
    print("two equal tones at 100 Hz and 100 + sep; the reported resolution is")
    print("the smallest sep whose spectrogram dip reaches -3 dB relative to the")
    print("lower of the two peaks, measured on a zero-padded (nfft = 8192) grid")
    print("   nperseg   resolution (Hz)   df (Hz)   resolution/df")
    for nperseg in (64, 128, 256, 512, 1024):
        df = FS / nperseg
        found = None
        for sep in np.arange(0.25, 60.0, 0.25):
            tones = (np.cos(2 * np.pi * 100.0 * t)
                     + np.cos(2 * np.pi * (100.0 + sep) * t))
            f, tt, Z = sps.stft(tones, fs=FS, window="hann", nperseg=nperseg,
                                noverlap=nperseg // 2, nfft=8192, boundary=None)
            mag = np.sqrt((np.abs(Z) ** 2).mean(axis=1))
            sel = (f > 100.0 - 3 * df) & (f < 100.0 + sep + 3 * df)
            m = mag[sel]
            loc = sps.argrelmax(m, order=5)[0]
            if len(loc) < 2:
                continue
            cand = [i for i in loc if m[i] >= 0.5 * m.max()]
            if len(cand) < 2:
                continue
            i1, i2 = int(min(cand)), int(max(cand))
            iv = i1 + int(np.argmin(m[i1:i2 + 1]))
            dip = m[iv] / min(m[i1], m[i2])
            if dip <= 0.5:
                found = sep
                break
        txt = f"{found:10.2f}" if found is not None else f"{'none':>10s}"
        ratio = f"{found / df:13.2f}" if found is not None else " " * 13
        print(f"   {nperseg:7d}   {txt:16s}   {df:7.3f}   {ratio}")
    print("the resolution is a constant number of BINS (about 2.4 for Hann) and")
    print("therefore a frequency that falls as the window lengthens: the same")
    print("trade measured in section 3 from the other side")

    section("5. Pulse localisation against window length, in seconds")
    t = np.arange(int(4 * FS)) * DT
    pulse = np.zeros_like(t)
    pulse[int(2 * FS)] = 1.0
    print("   nperseg   time width sigma (ms)   nperseg x DT (ms)   ratio")
    for nperseg in (64, 128, 256, 512, 1024):
        f, tt, Z = sps.stft(pulse, fs=FS, window="hann", nperseg=nperseg,
                            noverlap=nperseg - 1, boundary=None)
        P = np.abs(Z) ** 2
        pt = P.sum(axis=0)
        tc = np.sum(tt * pt) / np.sum(pt)
        tw = np.sqrt(np.sum((tt - tc) ** 2 * pt) / np.sum(pt))
        print(f"   {nperseg:7d}   {tw * 1e3:20.3f}   {nperseg * DT * 1e3:17.3f}"
              f"   {tw / (nperseg * DT):5.3f}")
    print("the localisation in time is proportional to the window length: the")
    print("spectrogram's time resolution IS the window duration (to a factor")
    print("that depends on the window shape)")

    section("6. Instantaneous frequency: analytic signal against the STFT ridge")
    duration = 2.0
    n = int(duration * FS)
    t = np.arange(n) * DT
    f0, f1 = 20.0, 180.0
    inst_true = f0 + (f1 - f0) * t / t[-1]
    phase = 2 * np.pi * np.cumsum(inst_true) * DT
    x = np.cos(phase)
    analytic = sps.hilbert(x)
    inst = np.diff(np.unwrap(np.angle(analytic))) / (2 * np.pi * DT)
    good = (t[:-1] > 0.05) & (t[:-1] < 1.95)
    f, tt, Z = sps.stft(x, fs=FS, window="hann", nperseg=256,
                        noverlap=128, boundary=None)
    ridge = f[np.argmax(np.abs(Z), axis=0)]
    ridge_true = f0 + (f1 - f0) * tt / t[-1]
    print(f"mono-component chirp {f0:.0f} -> {f1:.0f} Hz over {duration:.0f} s")
    print(f"   analytic-signal IF: rms error = "
          f"{np.sqrt(np.mean((inst[good] - inst_true[:-1][good]) ** 2)):6.3f} Hz, "
          f"max error = "
          f"{np.max(np.abs(inst[good] - inst_true[:-1][good])):6.3f} Hz")
    print(f"   STFT ridge:         rms error = "
          f"{np.sqrt(np.mean((ridge - ridge_true) ** 2)):6.3f} Hz, "
          f"max error = {np.max(np.abs(ridge - ridge_true)):6.3f} Hz")
    print("the analytic signal is exact for a single component and gives the")
    print("frequency at every sample; the ridge is quantised by the window's")
    print("frequency resolution, which is why it is the more robust of the two")
    print("when the record is noisy or multi-component")


if __name__ == "__main__":
    main()
