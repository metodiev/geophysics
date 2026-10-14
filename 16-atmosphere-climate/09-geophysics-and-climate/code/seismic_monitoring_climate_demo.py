#!/usr/bin/env python3
"""Seismic monitoring of the cryosphere: event detection with an STA/LTA
trigger and its detection/false-alarm trade-off, and a measurement of a tiny
relative velocity change by coda-wave interferometry with its noise floor.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_monitoring_climate_demo.py

Everything is SYNTHETIC.  The "noise", the "icequakes" and the "coda" are
generated from chosen formulas.  No real station, glacier, event catalogue or
published measurement is used.

Contents
--------
1. A synthetic continuous record: coloured ambient noise plus impulsive events.
2. STA/LTA detection, and the detection / false-alarm trade-off versus threshold.
3. Coda-wave interferometry: recovering a relative velocity change by a stretch
   search.
4. The noise floor of that measurement, as a standard deviation over realisations.
5. What is measured, what is inferred, and what the two cannot tell apart.
"""

import numpy as np
from scipy.signal import butter, filtfilt, sosfiltfilt

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC acquisition (chosen, not measured) ---------------------------
FS = 100.0                 # Hz, sampling rate
DURATION = 600.0           # s, record length (and the noise-only record length)
N_EVENTS = 40              # number of impulsive events
EVENT_AMPLITUDE_MIN = 3.0  # smallest event, in multiples of the noise sd
EVENT_AMPLITUDE_MAX = 20.0  # largest event, in multiples of the noise sd
STA_LEN = 0.5              # s, short-term average window
LTA_LEN = 20.0             # s, long-term average window
CODA_LENGTH = 30.0         # s, coda window used for the stretch measurement
STRETCH_1 = 5.0e-3         # relative stretch case 1 (0.50%)
STRETCH_2 = 5.0e-4         # relative stretch case 2 (0.05%)
NOISE_LEVELS = (0.01, 0.05, 0.20, 0.50)   # noise sd relative to the coda peak
N_REALISATIONS = 40


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def coloured_noise(n, fs=FS, corner=2.0):
    """Smooth (band-limited) Gaussian noise with unit standard deviation."""
    white = RNG.standard_normal(n)
    b, a = butter(2, corner / (fs / 2.0), btype="low")
    x = filtfilt(b, a, white)
    return x / x.std()


def bandpass(x, lo, hi, fs=FS):
    """Zero-phase Butterworth band-pass, used to build the detection band."""
    sos = butter(2, [lo / (fs / 2.0), hi / (fs / 2.0)], btype="band",
                 output="sos")
    return sosfiltfilt(sos, x)


def ratio_series(data, fs=FS, sta_s=STA_LEN, lta_s=LTA_LEN, band=(5.0, 15.0)):
    """STA/LTA of the envelope of the band-passed signal.

    The detection band is part of the detector's design: events and noise have
    different spectra, so the band decides how separable they are.
    """
    env = np.abs(bandpass(data, band[0], band[1], fs))
    n_sta = int(sta_s * fs)
    n_lta = int(lta_s * fs)
    sta = np.convolve(env, np.ones(n_sta) / n_sta, mode="same")
    lta = np.convolve(env, np.ones(n_lta) / n_lta, mode="same")
    return sta / np.maximum(lta, 1e-9)


def trigger_onsets(ratio, thr, fs=FS, quiet_s=2.0):
    """Onset sample indices of above-threshold excursions at least quiet_s apart."""
    above = ratio > thr
    starts = np.where(above & ~np.roll(above, 1))[0]
    if starts.size == 0:
        return starts
    keep = [starts[0]]
    for s in starts[1:]:
        if s - keep[-1] > quiet_s * fs:
            keep.append(s)
    return np.array(keep)


def main():
    section("1. A synthetic continuous record")
    n = int(FS * DURATION)
    noise = coloured_noise(n)
    event_times = np.sort(RNG.uniform(5.0, DURATION - 5.0, N_EVENTS))
    event_amps = RNG.uniform(EVENT_AMPLITUDE_MIN, EVENT_AMPLITUDE_MAX, N_EVENTS)
    signal = np.zeros(n)
    for te, amp in zip(event_times, event_amps):
        i0 = int(te * FS)
        w = int(0.5 * FS)
        idx = np.arange(max(0, i0 - w // 2), min(n, i0 + w // 2))
        tau = (idx - i0) / FS
        a = (np.pi * 10.0) ** 2
        signal[idx] += amp * (1 - 2 * a * tau ** 2) * np.exp(-a * tau ** 2)
    data = noise + signal
    print(f"  {DURATION:.0f} s at {FS:.0f} Hz = {n} samples (SYNTHETIC)")
    print("  ambient noise: smooth Gaussian, unit standard deviation")
    print(f"  {N_EVENTS} impulsive events with amplitudes drawn uniformly from")
    print(f"  {EVENT_AMPLITUDE_MIN:.1f} to {EVENT_AMPLITUDE_MAX:.1f} times the "
          f"noise sd, plus a separate noise-only record")
    print("  A detection catalogue is a statement about a threshold, not a")
    print("  property of the glacier; the next section measures it.")

    section("2. STA/LTA detection and the false-alarm trade-off")
    ratio = ratio_series(data)
    ratio0 = ratio_series(noise)
    print(f"  STA window {STA_LEN:.1f} s, LTA window {LTA_LEN:.1f} s")
    print("  threshold   triggers   events found   false alarms   missed")
    for thr in (2.0, 3.0, 4.0, 6.0, 8.0, 12.0):
        starts = trigger_onsets(ratio, thr)
        found = 0
        for te in event_times:
            if starts.size and np.any(np.abs(starts / FS - te) < 2.0):
                found += 1
        fa = trigger_onsets(ratio0, thr).size
        print(f"  {thr:9.1f}   {starts.size:8d}   {found:12d}/{N_EVENTS}   "
              f"{fa:12d}   {N_EVENTS - found:6d}")
    print("  Lowering the threshold finds more events and also fires on noise, on")
    print("  a record containing no events at all.  Neither column is 'the'")
    print("  catalogue: the pair (detected, false alarms) is what a trigger")
    print("  reports, and its operating point must be stated with the catalogue.")

    section("3. Coda-wave interferometry: a relative velocity change")
    n_coda = int(CODA_LENGTH * FS)
    tc = np.arange(n_coda) / FS
    freqs = RNG.uniform(2.0, 12.0, 60)
    phases = RNG.uniform(0.0, 2.0 * np.pi, 60)
    amps = RNG.uniform(0.5, 1.0, 60)
    ref = np.sum([a * np.sin(2 * np.pi * f * tc + p)
                  for a, f, p in zip(amps, freqs, phases)], axis=0)
    ref *= np.exp(-tc / 8.0)
    ref /= np.abs(ref).max()
    grid = np.arange(-1.5e-2, 1.5e-2 + 1e-9, 2.5e-5)

    def stretch(sig, eps):
        """Resample sig onto a stretched axis, sig((1+eps) t)."""
        return np.interp(tc, tc * (1.0 + eps), sig, left=0.0, right=0.0)

    # Precompute the stretched reference matrix once: one row per stretch factor.
    Rmat = np.vstack([stretch(ref, e) for e in grid])
    Rmat -= Rmat.mean(axis=1, keepdims=True)
    Rnorm = np.linalg.norm(Rmat, axis=1)

    def measure(sig):
        s = sig - sig.mean()
        corr = (Rmat @ s) / (Rnorm * np.linalg.norm(s))
        return float(grid[int(np.argmax(corr))])

    print(f"  coda window {CODA_LENGTH:.0f} s; stretch search on a "
          f"{grid.size}-point grid")
    print("  convention: a relative velocity change dv/v = -eps, because slower")
    print("  material lengthens the travel time and stretches the coda.")
    for eps_true, label in ((STRETCH_1, "+0.50%"), (STRETCH_2, "+0.05%")):
        est = measure(stretch(ref, eps_true))
        print(f"  clean case, true stretch {label:8s}: recovered {est:+.6f} "
              f"(error {est - eps_true:+.2e})")

    section("4. The noise floor of the measurement")
    print(f"  {N_REALISATIONS} noise realisations per row; noise sd is relative")
    print("  to the coda peak amplitude")
    print("  true stretch   noise sd   mean estimate   sd of estimate   "
          "sd/signal")
    for eps_true, label in ((STRETCH_1, "0.50%"), (STRETCH_2, "0.05%")):
        clean = stretch(ref, eps_true)
        for nl in NOISE_LEVELS:
            est = np.array([measure(clean + nl * RNG.standard_normal(n_coda))
                            for _ in range(N_REALISATIONS)])
            print(f"  {label:12s}   {nl:8.2f}   {est.mean():+13.6f}   "
                  f"{est.std():15.2e}   {est.std() / eps_true:8.2f}")
    print("  The standard deviation of the estimate is the resolution.  For a")
    print("  0.05% stretch it reaches the size of the signal itself at the")
    print("  largest noise level tested; for a 0.50% stretch the same noise")
    print("  leaves the estimate useful.  What limits the measurement is the")
    print("  coda signal-to-noise ratio and the window length, not some fixed")
    print("  instrumental sensitivity.")

    section("5. What is measured, what is inferred")
    print("  measured : ground motion (or its absence) at a sensor; a stretch")
    print("             factor from a waveform comparison.")
    print("  inferred : the existence of an event, its time and size; a change in")
    print("             seismic velocity in the sampled volume.")
    print("  NOT determined by seismic data alone: whether a velocity change comes")
    print("  from ice thinning, a temperature change, a water-content change or a")
    print("  change in the scattering medium.  Those require an independent")
    print("  measurement -- geodesy for mass, boreholes for temperature.")
    print("  All numbers above are SYNTHETIC.")


if __name__ == "__main__":
    main()
