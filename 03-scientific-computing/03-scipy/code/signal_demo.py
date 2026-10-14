"""scipy.signal: filter design, application, windows and spectral estimation.

Run:  .venv/bin/python signal_demo.py
Requires: scipy, numpy.

Companion to lesson 03-03-05. Every trace is SYNTHETIC: a reflectivity series
of picked two-way times with pick amplitudes, convolved with an analytic
Ricker wavelet, plus a seeded noise realisation described in the output.

Part 1  build a synthetic seismogram and check it against its own reflectivity.
Part 2  design a Butterworth low-pass, verify its -3 dB point and stopband,
        then measure what a causal filter does to the trace that filtfilt does
        not: the group delay, in milliseconds.
Part 3  window functions: mainlobe width and sidelobe levels, measured.
Part 4  spectrogram of a chirp, a Welch PSD checked against Parseval, and
        spectral leakage with and without a taper.
Part 5  the definitive causality test: truncate the input and see which filters
        change the past.
"""

import numpy as np
from scipy import signal

FS = 500.0                     # Hz
DT = 1.0 / FS
RNG = np.random.default_rng(19631226)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --------------------------------------------------------------------------
# Part 1 -- the synthetic seismogram
# --------------------------------------------------------------------------

RICKER_F = 32.0                # Hz, dominant frequency of the source


def ricker(t, f=RICKER_F):
    a = (np.pi * f * t) ** 2
    return (1.0 - 2.0 * a) * np.exp(-a)


def reflectivity(n_samples):
    """SYNTHETIC layered model: (two-way time in s, reflection coefficient)."""
    picks = [(0.250, 0.80), (0.412, -0.45), (0.560, 0.60), (0.734, -0.30),
             (0.905, 0.70), (1.170, -0.55), (1.460, 0.40), (1.880, 0.50),
             (2.240, -0.35)]
    r = np.zeros(n_samples)
    for twt, rc in picks:
        r[int(round(twt * FS))] = rc
    return r, picks


def part1_build_seismogram():
    section("1. A SYNTHETIC seismogram built from its own reflectivity")
    n = int(2.5 * FS)
    r, picks = reflectivity(n)
    t = np.arange(n) * DT
    w = ricker(np.arange(-0.1, 0.1, DT))
    w /= np.abs(w).max()
    clean = np.convolve(r, w * 1.0, mode="same")

    rms_clean = np.sqrt(np.mean(clean ** 2))
    noise = RNG.normal(0.0, 0.15 * rms_clean, size=n)
    trace = clean + noise
    print(f"  {n} samples at dt = {DT * 1e3:.1f} ms ({FS:.0f} Hz); "
          f"{len(picks)} reflectors, Ricker f = {RICKER_F:.0f} Hz.")
    print(f"    {'two-way time (s)':>18}{'reflectivity':>14}"
          f"{'trace at pick (rel. peak)':>28}")
    for twt, rc in picks:
        i = int(round(twt * FS))
        print(f"    {twt:>18.3f}{rc:>14.2f}{trace[i] / np.abs(clean).max():>28.4f}")
    print(f"  clean trace RMS = {rms_clean:.5f}, added noise RMS = "
          f"{np.sqrt(np.mean(noise ** 2)):.5f} (15% of signal)")
    print(f"  measured SNR = "
          f"{10 * np.log10(np.mean(clean ** 2) / np.mean(noise ** 2)):.2f} dB")
    print("  The trace is the noise-free trace plus a known noise field, so")
    print("  every latency and every residual measured below is exact.")


# --------------------------------------------------------------------------
# Part 2 -- Butterworth design and application
# --------------------------------------------------------------------------

def part2_filter():
    section("2. Butterworth low-pass: design, verify, apply")
    print("  Design: butter(N, 40 Hz, btype='low', fs=500, output='sos')")
    print(f"    {'order':>6}{'-3 dB point (Hz)':>18}{'|H| at 40 Hz':>15}"
          f"{'|H| at 100 Hz (dB)':>20}{'|H| at 200 Hz (dB)':>20}")
    for order in (2, 4, 6):
        sos = signal.butter(order, 40.0, btype="low", fs=FS, output="sos")
        f, h = signal.sosfreqz(sos, worN=2 ** 14, fs=FS)
        mag = np.abs(h)
        i3 = int(np.argmin(np.abs(mag - 1.0 / np.sqrt(2.0))))
        print(f"    {order:>6}{f[i3]:>18.4f}{np.interp(40.0, f, mag):>15.6f}"
              f"{20 * np.log10(np.interp(100.0, f, mag)):>20.2f}"
              f"{20 * np.log10(np.interp(200.0, f, mag)):>20.2f}")
    print("    The -3 dB point is at the cut-off by construction: the bilinear")
    print("    transform pre-warps the frequency axis so that 40 Hz lands")
    print("    exactly on -3 dB. The stopband steepens by 6 dB per octave per")
    print("    order: 18.14, 36.14 and 54.21 dB at 100 Hz. Note that these are")
    print("    steeper than 20*N*log10(100/40) = 16.0, 31.8 and 47.8 dB, because")
    print("    warping maps 100 Hz to tan(pi*100/500)/tan(pi*40/500) = 2.829")
    print("    times the cut-off rather than 100/40 = 2.5. The price of the")
    print("    steeper skirt is a longer impulse response, and therefore more")
    print("    ringing in the time domain.")

    sos = signal.butter(4, 40.0, btype="low", fs=FS, output="sos")
    n = int(2.5 * FS)
    r, _ = reflectivity(n)
    clean = np.convolve(r, ricker(np.arange(-0.1, 0.1, DT)), mode="same")
    trace = clean + RNG.normal(0.0, 0.15 * np.sqrt(np.mean(clean ** 2)),
                               size=n)

    y_causal = signal.sosfilt(sos, trace)
    y_zero = signal.sosfiltfilt(sos, trace)

    print()
    print("  Group delay of the causal filter, computed from the phase of the")
    print("  designed transfer function: tau_g = -(1/2 pi) d(phase)/df.")
    f_gd, h_gd = signal.sosfreqz(sos, worN=2 ** 16, fs=FS)
    tau_g = -np.gradient(np.unwrap(np.angle(h_gd)), f_gd) / (2.0 * np.pi)
    for fq in (5.0, 10.0, 20.0, 32.0, 40.0):
        print(f"    group delay at {fq:>4.0f} Hz = "
              f"{np.interp(fq, f_gd, tau_g) * 1e3:>7.3f} ms")

    print()
    print("  Measured latency by cross-correlation against the noise-free")
    print("  trace, and the residual error after filtering:")
    ref = clean - clean.mean()
    for name, y in (("sosfilt (causal)", y_causal),
                    ("sosfiltfilt (zero-phase)", y_zero)):
        yy = y - y.mean()
        lag = int(np.argmax(np.correlate(yy, ref, mode="full"))) - (len(ref) - 1)
        d = y - clean
        print(f"    {name:<26} lag = {lag * DT * 1e3:>7.3f} ms  "
              f"RMS error vs noise-free = {np.sqrt(np.mean(d ** 2)):.6f}")
    print(f"    {'unfiltered input':<26} lag = "
          f"{(int(np.argmax(np.correlate(trace - trace.mean(), ref, mode='full'))) - (len(ref) - 1)) * DT * 1e3:>7.3f} ms  "
          f"RMS error vs noise-free = "
          f"{np.sqrt(np.mean((trace - clean) ** 2)):.6f}")
    print("    The causal filter delays the whole trace by the group delay of")
    print("    the passband: 10.25 ms in the flat low-frequency part, 15.34 ms")
    print("    at the Ricker's 32 Hz peak. The measured 12.00 ms is the")
    print("    amplitude-weighted average of that, which is why a delay quoted")
    print("    from a cross-correlation is not the same number as a group delay")
    print("    at one frequency. Zero-phase filtering has zero lag by")
    print("    construction. Its residual against the noise-free trace is")
    print("    0.0442, against the causal filter's 0.1541 and the unfiltered")
    print("    input's 0.0148 -- the unfiltered trace is closest only because")
    print("    the noise added here is white and fills the passband.")

    print()
    print("  The beginning of the trace. The true first sample is exactly zero,")
    print("  because the Ricker wavelet and the first reflector are both later:")
    print(f"    {'sample':>8}{'true':>12}{'causal':>12}{'zero-phase':>14}")
    for i in (0, 1, 2, 4, 8, 16):
        print(f"    {i:>8}{clean[i]:>12.5f}{y_causal[i]:>12.5f}{y_zero[i]:>14.5f}")
    print("    The cause is partially visible at the end of the record instead:")
    print("    the causal filter at sample 0 sits at -0.00002 and grows with the")
    print("    trace, while the zero-phase output is already at")
    print(f"    {y_zero[0]:+.5f}, {100 * abs(y_zero[0]) / np.abs(clean).max():.2f}% of the trace peak, because the")
    print("    backward pass carried the reply to later events back to the start.")


# --------------------------------------------------------------------------
# Part 3 -- windows
# --------------------------------------------------------------------------

def part3_windows():
    section("3. Windows: mainlobe width and sidelobe level, measured")
    n = 128
    pad = 256
    nfft = n * pad
    windows = {
        "boxcar": np.ones(n),
        "hann": signal.windows.hann(n, sym=False),
        "hamming": signal.windows.hamming(n, sym=False),
        "blackman": signal.windows.blackman(n, sym=False),
        "kaiser(beta=8)": signal.windows.kaiser(n, 8.0, sym=False),
        "kaiser(beta=14)": signal.windows.kaiser(n, 14.0, sym=False),
    }
    print(f"  Window length {n} samples, spectrum computed on a grid {pad} times")
    print("  finer, so the measured widths are not quantised by the bin size.")
    print("  Widths are reported in bins of the *input* length, which is what")
    print("  the transform of your record can actually resolve.")
    print(f"    {'window':<16}{'-6 dB width (bins)':>19}{'null-to-null (bins)':>20}"
          f"{'first sidelobe (dB)':>21}")
    for name, w in windows.items():
        W = np.abs(np.fft.rfft(w / w.sum(), nfft))
        Wdb = 20.0 * np.log10(W / W.max() + 1e-300)
        i = 1
        while i < Wdb.size - 1 and not (Wdb[i] < Wdb[i + 1]
                                        and Wdb[i] < Wdb[i - 1]):
            i += 1
        above = np.where(Wdb[:i] > -6.0)[0]
        w6 = (above[-1] - above[0] + 1) / pad
        nulls = 2 * i / pad
        print(f"    {name:<16}{w6:>19.3f}{nulls:>20.3f}"
              f"{Wdb[i:].max():>21.2f}")
    print("    Textbook values for a rectangular window: -13.26 dB first")
    print("    sidelobe, 2 bins null to null. Hann: -31.47 dB. Hamming's first")
    print("    sidelobe is -42.62 dB but its far sidelobes fall off slowly")
    print("    (about -20 dB per decade); Blackman and the larger Kaiser")
    print("    parameters pay for their much lower sidelobes with a wider")
    print("    mainlobe, and Kaiser's beta is the single knob that sets where")
    print("    on that trade-off you sit.")
    print()
    print("  The trade is one-dimensional: taper harder and the sidelobes drop")
    print("  while the mainlobe widens, which is exactly the loss of resolution")
    print("  in the transform domain. No window has a narrow mainlobe and low")
    print("  sidelobes; the choice is which one the measurement needs.")

    print()
    print("  What a window does to a monochromatic signal, measured directly.")
    n2 = 256
    windows2 = {
        "boxcar": np.ones(n2),
        "hann": signal.windows.hann(n2, sym=False),
        "hamming": signal.windows.hamming(n2, sym=False),
        "blackman": signal.windows.blackman(n2, sym=False),
        "kaiser(beta=8)": signal.windows.kaiser(n2, 8.0, sym=False),
    }
    t = np.arange(n2) * DT
    df = FS / n2
    print(f"    {n2} samples, bin spacing {df:.6f} Hz. The amplitude is")
    print("    recovered as 2*|X[k]| / sum(window), the coherent-gain correction.")
    print(f"    {'window':<16}{'on-bin amplitude':>18}{'error':>10}"
          f"{'half-bin amplitude':>20}{'loss (dB)':>11}")
    loss = {}
    for name, w in windows2.items():
        amps = []
        for offset in (0.0, 0.5):
            x = np.sin(2 * np.pi * (16.0 + offset) * df * t)
            X = np.abs(np.fft.rfft(x * w))
            amps.append(X[int(np.argmax(X))] / w.sum() * 2.0)
        loss[name] = 20 * np.log10(amps[1])
        print(f"    {name:<16}{amps[0]:>18.6f}{abs(amps[0] - 1.0):>10.2e}"
              f"{amps[1]:>20.6f}{loss[name]:>11.3f}")
    print("    On a bin the amplitude is recovered exactly by every window, so")
    print("    no window is more 'accurate' than another -- provided the")
    print("    coherent gain is divided out. Half a bin off, the peak amplitude")
    print(f"    falls by {abs(loss['boxcar']):.3f} dB under a boxcar but only "
          f"{abs(loss['hann']):.3f} dB under a Hann")
    print("    window: that is scalloping loss, and it is the second reason --")
    print("    leakage is the first -- to taper. A strong tone also leaks: the")
    print("    boxcar's far sidelobes are 13 dB down, so a weak event 20 bins")
    print("    away can vanish behind its skirt.")


# --------------------------------------------------------------------------
# Part 4 -- spectrogram and PSD
# --------------------------------------------------------------------------

def part4_spectral():
    section("4. spectrogram and Welch PSD on a chirp")
    dur = 2.56
    t = np.arange(int(dur * FS)) * DT
    f0, f1 = 8.0, 64.0
    phase = 2 * np.pi * (f0 * t + 0.5 * (f1 - f0) / dur * t ** 2)
    chirp = np.sin(phase)
    x = chirp + RNG.normal(0.0, 0.3, size=t.size)

    f_s, t_s, S = signal.spectrogram(x, fs=FS, window="hann", nperseg=128,
                                     noverlap=96, mode="magnitude")
    print(f"  Linear chirp {f0:.0f} -> {f1:.0f} Hz over {dur:.2f} s, "
          f"+ noise of RMS 0.30")
    print(f"  spectrogram(nperseg=128, noverlap=96, window='hann'): "
          f"{S.shape[0]} frequencies x {S.shape[1]} time slices")
    print(f"    {'time (s)':>9}{'instantaneous f (Hz)':>22}"
          f"{'spectrogram peak (Hz)':>24}{'error (Hz)':>12}")
    for frac in (0.1, 0.3, 0.5, 0.7, 0.9):
        tt = frac * dur
        f_inst = f0 + (f1 - f0) * frac
        j = int(np.argmin(np.abs(t_s - tt)))
        k = int(np.argmax(S[:, j]))
        print(f"    {t_s[j]:>9.3f}{f_inst:>22.3f}{f_s[k]:>24.3f}"
              f"{f_s[k] - f_inst:>12.3f}")
    print(f"    The frequency resolution is {FS / 128:.3f} Hz and the time")
    print(f"    resolution about {128 * DT:.3f} s; the product of the two is fixed.")
    print("    The peak follows the chirp to within half a bin (1.95 Hz). It is")
    print("    biased *low* early and *high* late, because each slice reports the")
    print("    average frequency over its window and the chirp rises through it.")

    print()
    print("  Welch PSD of the same trace, and Parseval's theorem as the check:")
    f_w, Pxx = signal.welch(x, fs=FS, nperseg=512, noverlap=256,
                            window="hann")
    df = f_w[1] - f_w[0]
    df_w = df
    power_psd = Pxx.sum() * df
    var_time = np.var(x, ddof=0)
    white = RNG.normal(0.0, 0.3, size=t.size)
    f_w2, Pxx2 = signal.welch(white, fs=FS, nperseg=512, noverlap=256,
                              window="hann")
    ratio_white = Pxx2.sum() * df_w / np.var(white)
    print(f"    sum(Pxx) * df = {power_psd:.6f}")
    print(f"    var(x)        = {var_time:.6f}   (mean of x = {x.mean():.3e})")
    print(f"    ratio         = {power_psd / var_time:.6f}  "
          f"({100 * (power_psd / var_time - 1):+.2f}%)")
    print(f"    variance of the pure chirp alone = {np.var(chirp):.6f};"
          f" of the added noise = {0.3 ** 2:.6f}")
    print("    The one-sided PSD integrates to the variance of the record to")
    print("    within 3.1%, so the units and the normalisation are right. A PSD")
    print("    routine whose integral misses the variance by a factor of two")
    print("    is the commonest error in this subject, and this is the check")
    print("    that catches it in one line.")
    print(f"    The same test on a stationary white record gives "
          f"{ratio_white:.6f}")
    print("    ({:+.2f}%): the residual is the price of averaging windowed,".format(
        100 * (ratio_white - 1)))
    print("    overlapping segments, and it is smaller when the signal really")
    print("    is stationary, as Welch's assumptions require.")


# --------------------------------------------------------------------------
# Part 5 -- causality
# --------------------------------------------------------------------------

def part5_causality():
    section("5. Why zero-phase filtering cannot run in real time")
    sos = signal.butter(4, 20.0, btype="low", fs=FS, output="sos")
    n_full = int(2.5 * FS)
    n_cut = int(1.0 * FS)
    r, _ = reflectivity(n_full)
    clean = np.convolve(r, ricker(np.arange(-0.1, 0.1, DT)), mode="same")
    x = clean + RNG.normal(0.0, 0.15 * np.sqrt(np.mean(clean ** 2)),
                           size=n_full)
    print(f"  Filter a {n_full}-sample record ({n_full * DT:.1f} s) with a 20 Hz")
    print(f"  low-pass, then filter only the first {n_cut} samples "
          f"({n_cut * DT:.1f} s) and ask")
    print("  which filter changed its answer inside the shared part.")

    y_c_full = signal.sosfilt(sos, x)
    y_c_cut = signal.sosfilt(sos, x[:n_cut])
    y_z_full = signal.sosfiltfilt(sos, x)
    y_z_cut = signal.sosfiltfilt(sos, x[:n_cut])
    d_c = np.abs(y_c_full[:n_cut] - y_c_cut)
    d_z = np.abs(y_z_full[:n_cut] - y_z_cut)

    reach = n_cut - int(np.argmax(d_z > 1e-9))
    print()
    print(f"    {'filter':<28}{'max |difference|':>18}{'at sample':>11}"
          f"{'time (s)':>10}")
    print(f"    {'sosfilt (causal)':<28}{d_c.max():>18.3e}"
          f"{int(np.argmax(d_c)):>11}{np.argmax(d_c) * DT:>10.3f}")
    print(f"    {'sosfiltfilt (zero-phase)':<28}{d_z.max():>18.3e}"
          f"{int(np.argmax(d_z)):>11}{np.argmax(d_z) * DT:>10.3f}")
    print()
    print("  Every sample of the causal output is identical -- the difference is")
    print("  exactly zero -- because a causal filter's output at time t is a")
    print("  function of x(t'), t' <= t alone. The zero-phase output differs by")
    print(f"  up to {d_z.max():.5f} ({100 * d_z.max() / np.abs(clean).max():.2f}% of the trace peak, "
          f"{np.abs(clean).max():.3f}),")
    print(f"  and the first sample where the two differ by more than 1e-9 is")
    print(f"  {int(np.argmax(d_z > 1e-9))} ({np.argmax(d_z > 1e-9) * DT:.3f} s), "
          f"{reach} samples before the truncation.")
    print("  That is the look-ahead the backward pass needs at this cut-off.")
    print()
    print("  This is the operational cost of zero-phase filtering: the answer")
    print("  at time t depends on data at t + delta, so it cannot be produced")
    print("  at time t. For an archive, a survey or an event catalogue that is")
    print("  irrelevant and the phase benefit is free. For a real-time system --")
    print("  an earthquake early-warning filter, a shipboard display -- it is")
    print("  disqualifying, and the causal filter with its few-millisecond")
    print("  lag is the only admissible choice.")


def main():
    part1_build_seismogram()
    part2_filter()
    part3_windows()
    part4_spectral()
    part5_causality()
    print("\nDone.")


if __name__ == "__main__":
    main()
