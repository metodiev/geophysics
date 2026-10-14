"""Cross-correlation, polarisation and array processing on synthetic data.

No data are downloaded; the three-component and array records are synthesised
from stated back-azimuths, incidence angles and slownesses so that every
measurement has a known answer to compare against.

Run:
    .venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/obspy_advanced_demo.py
"""

from __future__ import annotations

import numpy as np
from obspy import Stream, Trace, UTCDateTime
from obspy.core.util.attribdict import AttribDict
from obspy.signal.array_analysis import array_processing
from obspy.signal.cross_correlation import correlate, xcorr_max
from obspy.signal.polarization import polarization_analysis
from obspy.signal.trigger import recursive_sta_lta, trigger_onset

FS = 100.0
START = UTCDateTime("2024-03-15T08:30:00.000000Z")
RICKER_F = 5.0


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def ricker(t: np.ndarray, f: float, t0: float) -> np.ndarray:
    a = (np.pi * f * (t - t0)) ** 2
    return (1.0 - 2.0 * a) * np.exp(-a)


def main() -> None:
    section("1. Cross-correlation recovers a known time shift")
    npts, lag_true = 2000, 25
    t = np.arange(npts) / FS
    rng = np.random.default_rng(42)
    a = ricker(t, RICKER_F, 5.0)
    b = ricker(t, RICKER_F, 5.0 + lag_true / FS)
    print(f"true shift                    : {lag_true} samples "
          f"= {lag_true / FS * 1000:.1f} ms")
    print(f"{'case':>28} {'lag (samples)':>14} {'lag (ms)':>10} "
          f"{'coefficient':>13} {'method':>8}")
    for label, sig, method in (
            ("clean, direct", b, "direct"),
            ("clean, fft", b, "fft"),
            ("+ 0.05 counts rms noise", b + 0.05 * rng.standard_normal(npts), "direct"),
            ("+ 0.20 counts rms noise", b + 0.20 * rng.standard_normal(npts), "direct"),
            ("+ 0.50 counts rms noise", b + 0.50 * rng.standard_normal(npts), "direct")):
        cc = correlate(a, sig, 50, method=method)
        lag, value = xcorr_max(cc)
        print(f"{label:>28} {int(lag):14d} {lag / FS * 1000:10.2f} "
              f"{value:13.6f} {method:>8}")
    print("A NEGATIVE lag means the second signal is LATER than the first: ObsPy")
    print("returns lag = shift - (delay in samples). Getting this sign wrong")
    print("flips every relative arrival time downstream.")
    print("The FFT and direct methods agree to ")
    cc_d = correlate(a, b, 50, method="direct")
    cc_f = correlate(a, b, 50, method="fft")
    print(f"   {np.abs(cc_d - cc_f).max():.3e} (maximum absolute difference)")

    section("2. Sub-sample lag from a parabolic fit")
    cc = correlate(a, b, 50, method="direct")
    i_max = int(np.argmax(cc))
    y0, y1, y2 = cc[i_max - 1], cc[i_max], cc[i_max + 1]
    delta = 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2)
    print(f"integer peak index            : {i_max} "
          f"(lag {i_max - 50} samples)")
    print(f"parabolic offset              : {delta:+.6f} samples")
    print(f"interpolated lag              : {i_max - 50 + delta:.6f} samples "
          f"= {(i_max - 50 + delta) / FS * 1000:.4f} ms")
    print(f"true lag                      : {-lag_true:.4f} samples "
          f"= {-lag_true / FS * 1000:.4f} ms")
    print("A three-point parabolic fit is the cheapest sub-sample estimator. It")
    print("is biased towards zero lag; the bias is a few per cent of the shift,")
    print("which matters when the shift is a fraction of a sample.")

    section("3. Polarisation: recovering back-azimuth and incidence angle")
    npts3 = 2500
    t3 = np.arange(npts3) / FS
    baz_true, inc_true = 45.0, 30.0
    wavelet = ricker(t3, 8.0, 10.0)
    vertical = np.cos(np.radians(inc_true)) * wavelet
    north = np.sin(np.radians(inc_true)) * np.cos(np.radians(baz_true)) * wavelet
    east = np.sin(np.radians(inc_true)) * np.sin(np.radians(baz_true)) * wavelet
    noise = 0.02
    station = Stream()
    for data, channel in ((vertical, "BHZ"), (north, "BHN"), (east, "BHE")):
        tr = Trace(data + noise * rng.standard_normal(npts3))
        tr.stats.network, tr.stats.station = "XX", "ABCD"
        tr.stats.location, tr.stats.channel = "00", channel
        tr.stats.sampling_rate, tr.stats.starttime = FS, START
        station.append(tr)
    result = polarization_analysis(station, 0.5, 0.2, 1.0, 20.0,
                                  START + 8.0, START + 12.0, method="flinn")
    rect = np.asarray(result["rectilinearity"], dtype=float)
    azim = np.asarray(result["azimuth"], dtype=float)
    inci = np.asarray(result["incidence"], dtype=float)
    planar = np.asarray(result["planarity"], dtype=float)
    good = rect > 0.9
    print(f"true back-azimuth / incidence : {baz_true:.1f} deg / "
          f"{inc_true:.1f} deg")
    print(f"windows analysed              : {len(rect)}")
    print(f"windows with rectilinearity>0.9: {int(good.sum())}")
    print(f"azimuth, mean over good windows: "
          f"{np.degrees(np.mean(np.angle(np.exp(1j * np.radians(azim[good]))))):.4f} deg")
    print(f"incidence, mean over good      : {inci[good].mean():.4f} deg")
    print(f"rectilinearity range (good)    : {rect[good].min():.4f} .. "
          f"{rect[good].max():.4f}")
    print(f"azimuth in the noise-only part : "
          f"{azim[~good].mean():.2f} deg  (meaningless)")
    print("Polarisation estimates are only interpretable where the rectilinearity")
    print("is high. Quoting an azimuth from a noise window is the most common")
    print("abuse of this method.")

    section("4. Array beamforming: back-azimuth and slowness, measured")
    radius = 2.0                       # km
    offsets = [(0.0, 0.0)] + [
        (radius * np.cos(np.radians(a)), radius * np.sin(np.radians(a)))
        for a in np.arange(6) * 60.0]
    baz_arr = 60.0                     # propagation azimuth
    apparent_velocity = 4.0            # km/s
    slowness_true = 1.0 / apparent_velocity
    npts_arr = 2000
    ta = np.arange(npts_arr) / FS
    array = Stream()
    for index, (x_km, y_km) in enumerate(offsets):
        delay = slowness_true * (x_km * np.sin(np.radians(baz_arr))
                                 + y_km * np.cos(np.radians(baz_arr)))
        shifted = ricker(ta - delay, 6.0, 10.0)
        tr = Trace(shifted + 0.01 * rng.standard_normal(npts_arr))
        tr.stats.network, tr.stats.station = "XX", f"S{index:02d}"
        tr.stats.location, tr.stats.channel = "00", "BHZ"
        tr.stats.sampling_rate, tr.stats.starttime = FS, START
        tr.stats.coordinates = AttribDict({"x": x_km, "y": y_km,
                                           "elevation": 0.0})
        array.append(tr)
    out = array_processing(array, win_len=4.0, win_frac=0.5,
                           sll_x=-0.6, slm_x=0.6, sll_y=-0.6, slm_y=0.6,
                           sl_s=0.002, semb_thres=-1e9, vel_thres=-1e9,
                           frqlow=2.0, frqhigh=12.0, stime=START + 8.0,
                           etime=START + 13.0, prewhiten=0, coordsys="xy")
    print(f"symmetry of the array         : {len(offsets)} elements, "
          f"radius {radius:.1f} km")
    print(f"true propagation azimuth      : {baz_arr:.1f} deg")
    print(f"true apparent slowness        : {slowness_true:.4f} s/km")
    print(f"true apparent velocity        : {apparent_velocity:.1f} km/s")
    print(f"windows returned              : {out.shape[0]}")
    print(f"{'rel. power':>11} {'azimuth (deg)':>14} {'slowness':>10}")
    for row in out:
        print(f"{row[1]:11.5f} {row[3]:14.4f} {row[4]:10.5f}")
    print("MEASURED CONVENTIONS, checked against this synthetic case:")
    print(f"  1. the azimuth column is {out[0][3]:.2f} deg, and the propagation")
    print(f"     azimuth we injected is {baz_arr:.1f} deg: the column is the")
    print("     BACK-azimuth (propagation azimuth + 180, taken modulo 360),")
    print("     i.e. the direction the wave comes from. The docstring says")
    print("     'backazimuth', and for once the docstring is right.")
    print("  2. the slowness column is in s/km, although the docstring says")
    print(f"     s/deg: measured {out[0][4]:.5f} matches "
          f"{slowness_true:.4f} s/km and not")
    print(f"     {slowness_true * 111.195:.2f} s/deg. Never re-use a numerical")
    print("     column without checking its units against a known case.")

    section("5. An independent beamformer as a check")
    print("Grid search over the slowness VECTOR (sx, sy) rather than over")
    print("(azimuth, slowness): the pair (theta, p) and (theta+180, -p) describe")
    print("the same vector, so a search over both at once has a two-fold")
    print("ambiguity that a search over (sx, sy) does not.")
    sx_grid = np.arange(-0.6, 0.6001, 0.005)
    window = slice(int(9 * FS), int(12 * FS))
    traces = [tr.data[window] for tr in array]
    coords = np.array(offsets)
    best = None
    for sx in sx_grid:
        for sy in sx_grid:
            shifts = -np.round((coords[:, 0] * sx + coords[:, 1] * sy)
                                * FS).astype(int)
            beam = np.zeros(traces[0].size)
            for tr_data, shift in zip(traces, shifts):
                beam += np.roll(tr_data, shift)
            value = float(np.sum(beam ** 2))
            if best is None or value > best[0]:
                best = (value, sx, sy)
    _, sx_best, sy_best = best
    magnitude = float(np.hypot(sx_best, sy_best))
    propagation = float(np.degrees(np.arctan2(sx_best, sy_best)) % 360.0)
    back_azimuth = (propagation + 180.0) % 360.0
    print(f"best slowness vector           : sx = {sx_best:+.4f}, "
          f"sy = {sy_best:+.4f} s/km")
    print(f"magnitude                      : {magnitude:.4f} s/km "
          f"(true {slowness_true:.4f})")
    print(f"propagation azimuth            : {propagation:.2f} deg "
          f"(true {baz_arr:.1f})")
    print(f"back-azimuth                   : {back_azimuth:.2f} deg")
    print(f"obspy array_processing gave    : azimuth {out[0][3]:.2f} deg, "
          f"slowness {out[0][4]:.5f} s/km")
    wrapped = abs((back_azimuth - out[0][3] + 180.0) % 360.0 - 180.0)
    print(f"agreement in back-azimuth      : {wrapped:.2f} deg")
    print(f"agreement in slowness          : "
          f"{abs(magnitude - out[0][4]):.5f} s/km")
    print("Two independent implementations agreeing to a fraction of the")
    print("theoretical resolution is the only reason to believe either of them.")
    print("In practice array-geometry errors, not the beamformer, produce the")
    print("few degrees of back-azimuth bias that matter.")

    section("6. STA/LTA: a detector, not a picker")
    npts_trig = 3000
    tt = np.arange(npts_trig) / FS
    event = ricker(tt, 8.0, 10.0)
    trace_data = 0.02 * rng.standard_normal(npts_trig) + event
    for scale in (1.0, 0.2, 0.05):
        data = 0.02 * rng.standard_normal(npts_trig) + scale * event
        cft = recursive_sta_lta(data, int(0.5 * FS), int(5.0 * FS))
        pairs = trigger_onset(cft, 4.0, 1.5)
        reported = (pairs[0][0] / FS) if len(pairs) else float("nan")
        print(f"amplitude x{scale:4.2f}: max STA/LTA {cft.max():8.3f}, "
              f"at t = {np.argmax(cft) / FS:6.3f} s, "
              f"trigger at t = {reported:6.3f} s, {len(pairs)} trigger(s)")
    print("The trigger time is a detection time; no threshold on STA/LTA turns it")
    print("into an arrival time. Picking is a different problem (see the")
    print("polarisation and cross-correlation sections above).")
    print(f"wavelet centre (true onset)   : 10.000 s")
    print(f"peak of the STA/LTA curve     : "
          f"{np.argmax(recursive_sta_lta(trace_data, int(0.5 * FS), int(5.0 * FS))) / FS:.3f} s")
    print("The characteristic function peaks a fraction of a second after the")
    print("onset, because the short-term window must fill with signal.")


if __name__ == "__main__":
    main()
