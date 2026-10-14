"""StationXML, instrument response and deconvolution with a water level.

The instrument is synthetic but realistic: a 1 Hz geophone (two zeros at the
origin, a critically damped pole pair) followed by a digitizer. The ground
motion is a 5 Hz wave packet superposed on a 50 s long-period signal, and the
"counts" the digitizer would record are computed exactly with ObsPy's own
response evaluation, so the inverse problem has a known answer.

No data are downloaded.

Run:
    .venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/inventory_and_metadata_demo.py
"""

from __future__ import annotations

import numpy as np
from obspy import Inventory, Trace, UTCDateTime
from obspy.core.inventory import Channel, Network, Response, Station
from obspy.signal.util import _npts2nfft

FS = 100.0                 # Hz
NPTS = 6000                # samples -> 60 s
F0 = 1.0                   # geophone corner frequency, Hz
ZETA = 1.0 / np.sqrt(2.0)   # damping
SENSITIVITY = 5.1e8        # counts per (m/s): 1500 V/(m/s) x 3.4e5 counts/V
F_NORM = 1.0               # frequency at which the sensitivity is defined, Hz
F_LONG_PERIOD = 0.05       # Hz: the long-period signal we want to keep

START = UTCDateTime("2024-03-15T08:30:00.000000Z")


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def poles() -> list[complex]:
    w0 = 2.0 * np.pi * F0
    p = -ZETA * w0 + 1j * w0 * np.sqrt(1.0 - ZETA ** 2)
    return [p, np.conj(p)]


def normalization_factor() -> float:
    """A0 such that |H(f_norm)| == 1 for the analogue part of the response."""
    s = 1j * 2.0 * np.pi * F_NORM
    p = poles()
    return float(abs((s - p[0]) * (s - p[1]) / s ** 2))


def build_inventory(a0: float) -> Inventory:
    ch = Channel(code="BHZ", location_code="00", latitude=48.10,
                 longitude=11.20, elevation=520.0, depth=0.0, azimuth=0.0,
                 dip=-90.0, sample_rate=FS,
                 start_date=UTCDateTime("2020-01-01"),
                 end_date=UTCDateTime("2030-01-01"))
    ch.response = Response.from_paz(
        zeros=[0j, 0j], poles=poles(), stage_gain=SENSITIVITY,
        stage_gain_frequency=F_NORM, normalization_frequency=F_NORM,
        normalization_factor=a0, input_units="M/S", output_units="COUNTS")
    st = Station(code="ABCD", latitude=48.10, longitude=11.20, elevation=520.0,
                 start_date=UTCDateTime("2020-01-01"), channels=[ch])
    return Inventory(networks=[Network(code="XX", stations=[st])],
                     source="synthetic demo")


def ground_velocity(t: np.ndarray) -> np.ndarray:
    """100 um/s wave packet at 5 Hz plus 5 um/s at F_LONG_PERIOD Hz."""
    packet = 1.0e-4 * np.exp(-((t - 30.0) / 1.2) ** 2) * np.sin(2 * np.pi * 5.0 * t)
    long_period = 5.0e-6 * np.sin(2 * np.pi * F_LONG_PERIOD * t)
    return packet + long_period


def main() -> None:
    a0 = normalization_factor()
    inv = build_inventory(a0)
    resp = inv.get_response("XX.ABCD.00.BHZ", UTCDateTime("2024-06-01"))

    section("1. The response is a pole-zero ratio plus one scale factor")
    print(f"geophone corner frequency f0 : {F0:.4f} Hz")
    print(f"damping zeta                 : {ZETA:.6f}  (= 1/sqrt(2), critical)")
    print(f"poles (rad/s)                : "
          f"{poles()[0]:.4f}, {poles()[1]:.4f}")
    print(f"zeros                        : 0, 0  (two zeros at the origin)")
    print(f"normalisation factor A0      : {a0:.6f}")
    print(f"stage gain (sensitivity)     : {SENSITIVITY:.4e} counts per m/s")
    print(f"defined at                   : {F_NORM:.4f} Hz")
    print(str(resp).rstrip())

    section("2. |H(f)| in counts per (m/s): measured, not remembered")
    nfft = _npts2nfft(NPTS)
    h, freqs = resp.get_evalresp_response(1.0 / FS, nfft, output="VEL")
    h = np.abs(h)
    print(f"nfft used by remove_response  : {nfft} samples "
          f"(next smooth number >= npts)")
    print(f"frequency spacing             : {freqs[1] - freqs[0]:.6f} Hz")
    print(f"{'f (Hz)':>10} {'|H| (counts per m/s)':>22} {'phase (deg)':>12}")
    ph = np.angle(resp.get_evalresp_response_for_frequencies(
        np.array([0.01, 0.1, 1.0, 10.0, 45.0]), output="VEL"))
    for target in (0.01, 0.1, 0.5, 1.0, 2.0, 10.0, 20.0, 45.0):
        i = int(np.argmin(np.abs(freqs - target)))
        print(f"{freqs[i]:10.4f} {h[i]:22.6e} "
              f"{np.degrees(np.angle(resp.get_evalresp_response_for_frequencies(np.array([freqs[i]]), output='VEL')[0])):12.4f}")

    section("3. Two zeros at the origin give a 40 dB/decade low-frequency roll-off")
    lo = (freqs > 0.004) & (freqs < 0.02)
    slope = np.polyfit(np.log10(freqs[lo]), np.log10(h[lo]), 1)[0]
    print(f"log-log slope, 0.004-0.02 Hz : {slope:.4f} decades/decade")
    print(f"expected for two zeros       : 2.0000")
    hi = (freqs > 5.0) & (freqs < 45.0)
    slope_hi = np.polyfit(np.log10(freqs[hi]), np.log10(h[hi]), 1)[0]
    print(f"log-log slope, 5-45 Hz       : {slope_hi:+.6f} decades/decade "
          f"(flat passband)")
    flat = h[hi].mean()
    i_f0 = int(np.argmin(np.abs(freqs - F0)))
    print(f"flat level |H(inf)|          : {flat:.6e} counts per m/s")
    print(f"|H(f0)| = |H({F0:.2f} Hz)|     : {h[i_f0]:.6e} counts per m/s")
    print(f"ratio |H(f0)| / |H(inf)|     : {h[i_f0] / flat:.6f}   "
          f"(1/sqrt(2) = {1 / np.sqrt(2):.6f})")
    print("The corner of a critically damped geophone is the -3 dB point:")
    print("above it the response is flat to velocity, below it |H| falls")
    print(f"as f^2, i.e. {20 * np.log10(10.0) * 2:.1f} dB per decade.")

    section("4. Forward model: counts = |H(f)| * velocity")
    t = np.arange(NPTS) / FS
    v_true = ground_velocity(t)
    counts_true = np.fft.irfft(np.fft.rfft(v_true, n=nfft) * h, n=nfft)[:NPTS]
    rng = np.random.default_rng(20240315)
    counts = np.round(counts_true + rng.normal(0.0, 0.5, NPTS))
    print(f"true ground velocity peak    : {np.abs(v_true).max():.6e} m/s "
          f"= {np.abs(v_true).max() * 1e6:.4f} um/s")
    print(f"true ground velocity RMS     : {np.sqrt(np.mean(v_true ** 2)):.6e} m/s")
    print(f"synthetic counts peak         : {np.abs(counts_true).max():.1f} counts")
    print(f"added noise                  : 0.5 counts RMS, 1 count quantisation")
    print(f"signal-to-noise (peak/RMS)   : "
          f"{20 * np.log10(np.abs(counts_true).max() / 0.5):.2f} dB")

    tr = Trace(counts.astype(np.float64))
    tr.stats.network, tr.stats.station = "XX", "ABCD"
    tr.stats.location, tr.stats.channel = "00", "BHZ"
    tr.stats.sampling_rate, tr.stats.starttime = FS, START

    section("5. The water level: what it clamps, and what it costs")
    print("remove_response divides by H(f), replacing |H| with")
    print("max(|H|) * 10^(-water_level/20) wherever |H| is smaller.")
    hmax = h.max()
    hf = np.fft.rfftfreq(nfft, 1.0 / FS)
    band = (hf >= 2.0) & (hf <= 20.0)
    basis = np.vstack([np.cos(2 * np.pi * F_LONG_PERIOD * t),
                       np.sin(2 * np.pi * F_LONG_PERIOD * t)]).T

    def band_rms(x, mask=band):
        spec = np.fft.rfft(x, n=nfft) * mask
        return float(np.sqrt(np.mean(np.fft.irfft(spec, n=nfft)[:len(x)] ** 2)))

    print(f"true 2-20 Hz RMS             : {band_rms(v_true) * 1e6:.4f} um/s")
    print(f"true {F_LONG_PERIOD * 1e3:.0f} mHz amplitude      : "
          f"{5.0e-6 * 1e6:.4f} um/s")
    print(f"max |H| over all frequencies : {hmax:.6e} counts per m/s")
    print(f"{'wl (dB)':>8} {'clamp f (Hz)':>13} {'LF amp (um/s)':>14} "
          f"{'LF recovery':>12} {'2-20 Hz RMS':>12} {'total RMS err':>14}")
    for wl in (20, 40, 54, 60, 66, 80, 100, 200):
        out = tr.copy()
        out.remove_response(inventory=inv, output="VEL", water_level=wl,
                            zero_mean=False, taper=False, pre_filt=None)
        thr = hmax * 10 ** (-wl / 20.0)
        f_clamp = float(np.interp(thr, h, freqs))
        amp_lf = float(np.hypot(*np.linalg.lstsq(
            basis, out.data, rcond=None)[0]))
        print(f"{wl:8d} {f_clamp:13.5f} {amp_lf * 1e6:14.4f} "
              f"{(amp_lf / 5.0e-6 - 1) * 100:+11.2f}% "
              f"{band_rms(out.data) * 1e6:12.4f} "
              f"{np.sqrt(np.mean((out.data - v_true) ** 2)) * 1e6:14.4f}")
    print("Reading the table. The clamp frequency is where |H| falls to")
    print("max|H|*10^(-wl/20); below it the deconvolution is a constant")
    print("amplification instead of the true 1/|H|. At 40 dB the clamp sits at")
    print("0.100 Hz, above the 50 mHz signal, and three quarters of it is")
    print("lost. At 54 dB the clamp is 0.044 Hz and the 50 mHz amplitude is")
    print("recovered to within a few per cent. Beyond about")
    print("80 dB the amplified half-count noise below the corner overwhelms")
    print("the long period, and by 100 dB the estimate is 7.5 um/s for a true")
    print("5.0 um/s. The 2-20 Hz band is unaffected until the leakage from")
    print("those huge low-frequency excursions reaches it.")

    section("5b. A pre-filter is the better tool than a large water level")
    print("pre_filt applies a cosine taper in the frequency domain before the")
    print("deconvolution, so nothing outside the passband is amplified.")
    plain = tr.copy()
    plain.remove_response(inventory=inv, output="VEL", water_level=60,
                          zero_mean=False, taper=False)
    filtered = tr.copy()
    filtered.remove_response(inventory=inv, output="VEL", water_level=60,
                             zero_mean=False, taper=False,
                             pre_filt=(0.02, 0.04, 8.0, 10.0))
    low = (hf < 0.04)
    print(f"water_level=60, no pre_filt  : low-f (<0.04 Hz) RMS "
          f"{band_rms(plain.data, low) * 1e6:9.4f} um/s, "
          f"2-20 Hz RMS {band_rms(plain.data) * 1e6:8.4f} um/s")
    print(f"water_level=60, pre_filt     : low-f (<0.04 Hz) RMS "
          f"{band_rms(filtered.data, low) * 1e6:9.4f} um/s, "
          f"2-20 Hz RMS {band_rms(filtered.data) * 1e6:8.4f} um/s")
    print(f"true 2-20 Hz RMS             : "
          f"                                        "
          f"2-20 Hz RMS {band_rms(v_true) * 1e6:8.4f} um/s")
    print(f"CHECK pre_filt lowers low-f noise: "
          f"{band_rms(filtered.data, low) < band_rms(plain.data, low)}")
    print("For a 1 Hz geophone recording local events, pre_filt=(0.02, 0.04,")
    print("8, 10) Hz is a defensible starting point: it keeps the 1-8 Hz")
    print("signal band and removes everything the response cannot support.")

    section("6. A wrong A0 silently rescales the whole instrument")
    bad = build_inventory(1.0)          # normalisation forgotten
    print(str(bad.get_response("XX.ABCD.00.BHZ",
                               UTCDateTime("2024-06-01"))).splitlines()[2].strip())
    print(f"with A0 = {a0:.6f}: overall sensitivity = "
          f"{SENSITIVITY:.6e} counts per m/s")
    print(f"with A0 = 1.0     : obspy derives "
          f"|H(1 Hz)| * gain = {SENSITIVITY * abs(1j * 2 * np.pi * F_NORM) ** 2 / abs((1j * 2 * np.pi * F_NORM - poles()[0]) * (1j * 2 * np.pi * F_NORM - poles()[1])):.2f}"
          f" counts per m/s")
    print("The number in <InstrumentSensitivity> is a derived summary: if the")
    print("stage normalisation is wrong it disagrees with the stage gain, and")
    print("StationXML validators flag the mismatch.")

    section("7. Sensitivity-only removal is a common shortcut")
    plain = tr.copy()
    plain.remove_sensitivity(inventory=inv)
    print(f"remove_sensitivity peak       : {np.abs(plain.data).max():.6e} m/s")
    print(f"true peak                      : {np.abs(v_true).max():.6e} m/s")
    print(f"ratio                          : "
          f"{np.abs(plain.data).max() / np.abs(v_true).max():.4f}")
    print("remove_sensitivity divides by one scalar; remove_response divides by")
    print("the full frequency-dependent transfer function. They differ by the")
    print("shape of |H(f)|, which for this geophone is a factor "
          f"{hmax / SENSITIVITY:.4f} at high frequency.")


if __name__ == "__main__":
    main()
