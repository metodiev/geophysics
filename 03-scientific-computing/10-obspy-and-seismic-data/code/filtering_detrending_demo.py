"""Preprocessing: detrend, taper, filter, decimate, integrate, differentiate.

Synthetic traces only. Every reported number is printed by this script.

Run:
    .venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/filtering_detrending_demo.py
"""

from __future__ import annotations

import numpy as np
from obspy import Trace, UTCDateTime

FS = 500.0                  # Hz
NPTS = 10_000               # samples -> 20 s
START = UTCDateTime("2024-03-15T08:30:00.000000Z")
SIGNAL_HZ = 4.0
NOISE_HZ = 90.0
LINEAR_TREND = 2000.0       # counts per second


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def base_trace() -> Trace:
    rng = np.random.default_rng(20240315)
    t = np.arange(NPTS) / FS
    data = (5000.0 * np.exp(-((t - 10.0) / 1.0) ** 2) * np.sin(2 * np.pi * SIGNAL_HZ * t)
            + 300.0 * np.sin(2 * np.pi * NOISE_HZ * t)
            + LINEAR_TREND * t
            + 100.0                          # constant offset
            + rng.normal(0.0, 20.0, NPTS))
    tr = Trace(data)
    tr.stats.network, tr.stats.station = "XX", "ABCD"
    tr.stats.location, tr.stats.channel = "00", "BHZ"
    tr.stats.sampling_rate, tr.stats.starttime = FS, START
    return tr


def band_power(data: np.ndarray, f_lo: float, f_hi: float,
               fs: float = FS) -> float:
    """RMS amplitude in a frequency band, via a rectangular FFT filter.

    ``fs`` must be the sampling rate of ``data``; passing the wrong one is the
    classic way to report a band that does not exist in the record.
    """
    nfft = 2 ** int(np.ceil(np.log2(len(data))))
    spec = np.fft.rfft(data, n=nfft)
    freqs = np.fft.rfftfreq(nfft, 1.0 / fs)
    spec = np.where((freqs >= f_lo) & (freqs <= f_hi), spec, 0.0)
    return float(np.sqrt(np.mean(np.fft.irfft(spec, n=nfft)[:len(data)] ** 2)))


def main() -> None:
    tr = base_trace()
    t = np.arange(NPTS) / FS

    section("1. The synthetic trace, and what is in it")
    print(f"sampling rate                : {tr.stats.sampling_rate:.1f} Hz")
    print(f"Nyquist frequency            : {tr.stats.sampling_rate / 2:.1f} Hz")
    print(f"samples / duration           : {tr.stats.npts} / "
          f"{tr.stats.npts * tr.stats.delta:.1f} s")
    print(f"mean (constant offset)       : {tr.data.mean():.4f} counts")
    print(f"peak-to-peak                 : {np.ptp(tr.data):.1f} counts")
    print(f"RMS in 3-5 Hz (the signal)   : "
          f"{band_power(tr.data, 3.0, 5.0):.4f} counts")
    print(f"RMS in 80-99 Hz (the noise)  : "
          f"{band_power(tr.data, 80.0, 99.0):.4f} counts")
    print("So the true signal-to-noise is about 17:1 in amplitude, but the raw")
    print("trace is dominated by the trend and the 90 Hz component.")

    section("2. Detrend: remove the mean and the linear trend")
    detrended = tr.copy().detrend("linear")
    fit = np.polyfit(t, tr.data, 1)
    print(f"fitted linear trend           : {fit[0]:.4f} counts/s * t "
          f"+ {fit[1]:.1f} counts")
    print(f"true trend was                : {LINEAR_TREND:.4f} counts/s "
          f"+ 100.0 counts")
    print(f"mean before                   : {tr.data.mean():.4f} counts")
    print(f"mean after                    : {detrended.data.mean():.6f} counts")
    print(f"max |after|                   : {np.abs(detrended.data).max():.1f} counts")
    print(f"shape preserved               : "
          f"{detrended.stats.npts == tr.stats.npts}")
    simple = tr.copy().detrend("simple")
    print(f"detrend('simple') residual mean: {simple.data.mean():.4f} counts "
          f"(it only subtracts a constant, so the slope survives)")

    section("3. Taper: the price of forcing the ends to zero")
    print(f"raw first/last sample         : {tr.data[0]:.2f} / "
          f"{tr.data[-1]:.2f} counts")
    print(f"raw step at the seam          : "
          f"{abs(tr.data[-1] - tr.data[0]):.2f} counts "
          f"(the record must wrap to plot or transform)")
    unt = tr.copy()
    tap = tr.copy().taper(max_percentage=0.05, type="cosine")
    print(f"tapered first/last sample     : {tap.data[0]:.2e} / "
          f"{tap.data[-1]:.2e} counts")
    print(f"{'':>30} {'3-5 Hz RMS':>12} {'0-1 Hz RMS':>12} {'0-0.2 Hz RMS':>14}")
    for label, data in (("no taper, trended", unt.data),
                        ("cosine taper 5%, trended", tap.data)):
        print(f"{label:>30} {band_power(data, 3.0, 5.0):12.4f} "
              f"{band_power(data, 0.0, 1.0):12.4f} "
              f"{band_power(data, 0.05, 0.2):14.4f}")
    print("The taper removes the boundary step, which is what starts the ringing")
    print("in an FFT or a filter. But on a record that still contains a trend")
    print("most of the 0-1 Hz power IS the trend, and tapering cannot remove a")
    print("trend -- it only reduces the discontinuity. After detrending the")
    print("effect is small because the step is already gone:")
    unt_d = tr.copy().detrend("linear")
    tap_d = tr.copy().detrend("linear").taper(max_percentage=0.05, type="cosine")
    print(f"{'no taper, detrended':>30} {band_power(unt_d.data, 3.0, 5.0):12.4f} "
          f"{band_power(unt_d.data, 0.0, 1.0):12.4f} "
          f"{band_power(unt_d.data, 0.05, 0.2):14.4f}")
    print(f"{'cosine taper 5%, detrended':>30} "
          f"{band_power(tap_d.data, 3.0, 5.0):12.4f} "
          f"{band_power(tap_d.data, 0.0, 1.0):12.4f} "
          f"{band_power(tap_d.data, 0.05, 0.2):14.4f}")
    print("The taper is not free: it attenuates the first and last 5% of the")
    print("record, which must be reported when those samples matter.")

    section("4. Filter: causal and zero phase are different products")
    causal = detrended.copy()
    causal.filter("bandpass", freqmin=2.0, freqmax=6.0, corners=4,
                  zerophase=False)
    zero = detrended.copy()
    zero.filter("bandpass", freqmin=2.0, freqmax=6.0, corners=4,
                zerophase=True)
    print(f"{'filter':>26} {'3-5 Hz RMS':>12} {'80-99 Hz RMS':>14} "
          f"{'peak sample index':>18}")
    for label, data in (("none (detrended)", detrended.data),
                        ("bandpass 2-6 Hz causal", causal.data),
                        ("bandpass 2-6 Hz zero-phase", zero.data)):
        print(f"{label:>26} {band_power(data, 3.0, 5.0):12.4f} "
              f"{band_power(data, 80.0, 99.0):14.4f} "
              f"{int(np.argmax(np.abs(data))):18d}")
    true_peak = int(np.argmax(np.abs(detrended.data)))
    print(f"true signal peak sample       : {true_peak}")
    print(f"causal peak shift             : "
          f"{int(np.argmax(np.abs(causal.data))) - true_peak} samples "
          f"= {(int(np.argmax(np.abs(causal.data))) - true_peak) / FS * 1000:.1f} ms")
    print(f"zero-phase peak shift         : "
          f"{int(np.argmax(np.abs(zero.data))) - true_peak} samples")
    print("A causal filter shifts the arrival in time (and its group delay is")
    print("frequency dependent, so it also distorts the wavelet). filtfilt-style")
    print("zero-phase filtering removes the shift but reads the future, so it")
    print("cannot be used in real time and it smears energy at the ends.")

    section("5. Decimate: the anti-alias filter is the whole point")
    factor = 16
    fs_new = FS / factor
    alias = abs(NOISE_HZ - round(NOISE_HZ / fs_new) * fs_new)
    print(f"decimation factor             : {factor}")
    print(f"sample rate                   : {FS:.1f} Hz -> {fs_new:.2f} Hz")
    print(f"new Nyquist                   : {fs_new / 2:.3f} Hz")
    print(f"npts                          : {NPTS} -> {NPTS // factor}")
    print(f"90 Hz input aliases to        : {alias:.3f} Hz "
          f"(inside the 3-5 Hz signal band!)")
    clean = detrended.copy().decimate(factor, no_filter=False)
    dirty = detrended.copy().decimate(factor, no_filter=True)
    print(f"{'decimation':>26} {'RMS 3-5 Hz':>12} {'RMS 2.5-3.5 Hz':>16} "
          f"{'RMS 6-15 Hz':>12}")
    for label, data in (("none (detrended)", detrended.data),
                        ("with anti-alias filter", clean.data),
                        ("no_filter=True", dirty.data)):
        rate = FS if label == "none (detrended)" else fs_new
        lo = max(0.001, alias - 0.5)
        print(f"{label:>26} {band_power(data, 3.0, 5.0, rate):12.4f} "
              f"{band_power(data, lo, alias + 0.5, rate):16.4f} "
              f"{band_power(data, 6.0, min(15.0, rate / 2 - 0.01), rate):12.4f}")
    print("no_filter=True folds the 90 Hz component down onto 3.75 Hz, where it")
    print("is indistinguishable from signal: the 'signal' band gains energy and")
    print("nothing in the decimated trace reveals that it is an artefact.")
    dt = dirty.stats.delta
    print(f"alias time shift across the record: "
          f"{1 / alias / 1000:.6f} s per cycle of the artefact "
          f"(dt = {dt:.4f} s, {1 / alias / dt:.2f} samples per cycle)")
    print("ObsPy refuses decimation factors above 16 with automatic filter")
    print("design; measured on this installation:")
    try:
        detrended.copy().decimate(20)
        print("   decimate(20) unexpectedly succeeded")
    except ArithmeticError as exc:
        print(f"   decimate(20) -> ArithmeticError: {exc}")
    print("Use resample(25.0) instead, which designs an adequate filter.")

    section("6. Resample is decimate with an explicit target rate")
    res = detrended.copy().resample(31.25)
    dec = detrended.copy().decimate(16)
    print(f"resample(31.25)               : {res.stats.npts} samples, "
          f"{res.stats.sampling_rate:.6f} Hz")
    print(f"decimate(16)                  : {dec.stats.npts} samples, "
          f"{dec.stats.sampling_rate:.6f} Hz")
    print(f"CHECK same rate               : "
          f"{res.stats.sampling_rate == dec.stats.sampling_rate}")
    b_res = band_power(res.data, 3.0, 5.0, res.stats.sampling_rate)
    b_dec = band_power(dec.data, 3.0, 5.0, dec.stats.sampling_rate)
    print(f"3-5 Hz RMS after resample()   : {b_res:.4f} counts")
    print(f"3-5 Hz RMS after decimate(16) : {b_dec:.4f} counts")
    print(f"ratio                         : {b_res / b_dec:.6f} "
          f"(the two paths design different anti-alias filters)")

    section("7. Differentiate and integrate are spectral operations")
    diff = detrended.copy().differentiate()
    integ = detrended.copy().integrate()
    f_signal = SIGNAL_HZ
    print(f"RPMS of the signal            : "
          f"{band_power(detrended.data, 3.0, 5.0):.4f} counts")
    print(f"RPMS after differentiate()    : "
          f"{band_power(diff.data, 3.0, 5.0):.4f} counts")
    ratio_d = band_power(diff.data, 3.0, 5.0) / band_power(detrended.data, 3.0, 5.0)
    print(f"2*pi*f = {2 * np.pi * f_signal:.4f} rad/s; measured ratio = "
          f"{ratio_d:.4f}  (relative error "
          f"{(ratio_d / (2 * np.pi * f_signal) - 1) * 100:+.3f} %)")
    print(f"RPMS after integrate()        : "
          f"{band_power(integ.data, 3.0, 5.0):.4f} counts")
    ratio_i = band_power(integ.data, 3.0, 5.0) / band_power(detrended.data, 3.0, 5.0)
    print(f"1/(2*pi*f) = {1 / (2 * np.pi * f_signal):.6f} s; measured ratio = "
          f"{ratio_i:.6f}  (relative error "
          f"{(ratio_i * 2 * np.pi * f_signal - 1) * 100:+.3f} %)")
    print("Differentiation multiplies the spectrum by i*omega; integration")
    print("divides by it. A constant of integration is undetermined, which is")
    print("why integrating an uncleaned record drifts without limit.")

    section("8. Order matters")
    order_a = tr.copy().detrend("linear").taper(0.05).filter(
        "bandpass", freqmin=2.0, freqmax=6.0, corners=4)
    order_b = tr.copy().filter("bandpass", freqmin=2.0, freqmax=6.0,
                               corners=4).detrend("linear")
    print(f"detrend->taper->filter RMS 3-5 Hz : "
          f"{band_power(order_a.data, 3.0, 5.0):.4f} counts")
    print(f"filter->detrend RMS 3-5 Hz       : "
          f"{band_power(order_b.data, 3.0, 5.0):.4f} counts")
    print(f"difference                       : "
          f"{abs(band_power(order_a.data, 3.0, 5.0) - band_power(order_b.data, 3.0, 5.0)):.4f} counts")
    print("Removing the trend before filtering keeps the filter from ringing on")
    print("a step; applying the taper after detrending avoids tapering a ramp.")


if __name__ == "__main__":
    main()
