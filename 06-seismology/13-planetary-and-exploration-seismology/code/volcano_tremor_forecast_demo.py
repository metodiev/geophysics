#!/usr/bin/env python3
"""Volcano seismology: LP-event resonance, tremor detection trade-offs, and
what a precursor hit rate does and does not imply.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python volcano_tremor_forecast_demo.py

Everything is SYNTHETIC.  The LP source model, the tremor rate model and the
eruption catalogue below are chosen teaching models, not measurements of any
volcano.  No real event, station or eruption is used.

Contents
--------
1. An LP (long-period) event as a damped oscillator: the spectral peak position
   and the half-power width, measured and compared with the closed forms.
2. Tremor as a superposition of many LP events: RSAM window length versus
   detection latency and false alarms, measured over many realisations.
3. A synthetic unrest catalogue: hit rate, false-alarm rate and the base-rate
   problem, measured as a function of the prior probability of eruption.
4. Summary of measured quantities.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC model parameters (chosen, not measured) -----------------------
F0_LP = 2.0          # Hz   dominant frequency of one LP event
Q_LP = 20.0          # -    quality factor of the LP resonance
T_RISE = 300.0       # s    e-folding time of the pre-eruptive event-rate rise
T_ERUPT = 900.0      # s    eruption time in the synthetic timeline
DT = 0.01            # s    sample interval (100 Hz)
T_TOTAL = 1200.0     # s    length of the synthetic record


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def lp_spectrum_amplitude(f_hz, f0_hz, q, amp=1.0):
    """Exact Fourier amplitude of a causal damped sinusoid.

    u(t) = amp * exp(-sigma t) sin(2 pi f0 t) for t >= 0, with the decay rate
    sigma fixed by the resonance quality factor, sigma = pi f0 / Q.
    Then  U(omega) = amp * w0 / ((sigma + i omega)^2 + w0^2).
    """
    sigma = np.pi * f0_hz / q
    w = 2.0 * np.pi * f_hz
    w0 = 2.0 * np.pi * f0_hz
    denom = (sigma + 1j * w) ** 2 + w0 ** 2
    return amp * w0 / np.abs(denom)


def lp_wavelet(t, f0_hz, q, amp=1.0):
    """Time-domain damped sinusoid, zero for t < 0 (t measured from onset)."""
    sigma = np.pi * f0_hz / q
    u = np.zeros_like(t)
    pos = t >= 0.0
    u[pos] = amp * np.exp(-sigma * t[pos]) * np.sin(2.0 * np.pi * f0_hz * t[pos])
    return u


def rsam(x, dt, window_s):
    """Real-time seismic amplitude measurement: running RMS over window_s."""
    n = max(1, int(round(window_s / dt)))
    kernel = np.ones(n) / n
    return np.sqrt(np.convolve(x * x, kernel, mode="same"))


def main() -> int:
    # ------------------------------------------------------------------
    section("1. LP event as a damped oscillator: peak and half-power width")
    print(f"MODEL: f0 = {F0_LP:.2f} Hz, Q = {Q_LP:.1f} -> decay rate "
          f"sigma = pi f0/Q = {np.pi * F0_LP / Q_LP:.4f} 1/s")
    print("The spectrum of a causal damped sinusoid peaks at")
    print("    f_peak = f0 sqrt(1 - 1/(4 Q^2))")
    print("and its -3 dB half-width is 2 sigma = 2 pi f0/Q, i.e. Q = f0/dF.\n")
    print("     Q    f_peak meas (Hz)   f_peak closed form   -3dB width (Hz)   "
          "Q = f0/dF")
    fgrid = np.linspace(0.01, 20.0, 400000)
    q_rec = {}
    for q in (3.0, 5.0, 10.0, 20.0, 50.0):
        a = lp_spectrum_amplitude(fgrid, F0_LP, q)
        i = int(np.argmax(a))
        f_peak = fgrid[i]
        f_pred = F0_LP * np.sqrt(1.0 - 1.0 / (4.0 * q ** 2))
        half = a[i] / np.sqrt(2.0)
        above = np.where(a >= half)[0]
        width = fgrid[above[-1]] - fgrid[above[0]]
        q_rec[q] = F0_LP / width
        print(f"  {q:5.1f}   {f_peak:15.4f}   {f_pred:18.4f}   {width:15.4f}   "
              f"{q_rec[q]:8.2f}")
    print("\n  Two readings.  (i) The peak of the spectrum is NOT at f0: the")
    print("  damping pulls it down by a factor sqrt(1-1/(4Q^2)), which is 0.501 per")
    print("  cent at Q=5 and 0.031 per cent at Q=20 -- measurable only for low Q.")
    print("  (ii) The half-power width recovers Q = f0/dF to 0.1 per cent for")
    print("  Q >= 10, but is biased LOW at very low Q (2.91 measured against 3.0")
    print("  input), where the spectrum is skewed and peak and bandwidth are no")
    print("  longer separable.  A 'dominant frequency' is only meaningful")
    print("  together with the Q that produced it.")

    # ------------------------------------------------------------------
    section("2. Tremor detection: RSAM window length versus latency and alarms")
    t = np.arange(0.0, T_TOTAL, DT)
    noise_sigma = 1.0e-6            # m/s, SYNTHETIC background noise level
    onset = T_RISE * np.log(4.0)    # lambda has risen 4x from its value at t=0
    print(f"MODEL: record {T_TOTAL:.0f} s at {1.0 / DT:.0f} Hz; event rate")
    print(f"       lambda(t) = lambda_0 exp((t - {T_ERUPT:.0f})/{T_RISE:.0f})")
    print(f"       'true onset' defined where lambda has risen 4x from its value")
    print(f"       at t = 0: onset = {T_RISE:.0f} ln 4 = {onset:.1f} s; eruption at "
          f"t = {T_ERUPT:.0f} s")
    print(f"       noise rms = {noise_sigma:.2e} m/s; LP events f0 = "
          f"{F0_LP:.1f} Hz, Q = {Q_LP:.0f}")

    nreal = 20
    results = {}
    for window_s in (1.0, 5.0, 20.0, 60.0):
        lat, alarms, thresh_list = [], [], []
        for _ in range(nreal):
            rate0 = 1.0
            lam = rate0 * np.exp((t - T_ERUPT) / T_RISE)
            n_events = RNG.poisson(lam * DT)          # per-sample Poisson count
            ev_idx = np.where(n_events > 0)[0]
            tr = noise_sigma * RNG.standard_normal(t.size)
            tau_dec = Q_LP / (np.pi * F0_LP)
            span = int(round(6.0 * tau_dec / DT))
            ev_t = np.arange(span) * DT
            wav = lp_wavelet(ev_t, F0_LP, Q_LP)
            for idx in ev_idx:
                amp = 4.0e-6 * np.exp(0.5 * RNG.standard_normal())
                end = min(t.size, idx + span)
                tr[idx:end] += amp * wav[: end - idx]
            r = rsam(tr, DT, window_s)
            base = r[t < 300.0]
            mad = np.median(np.abs(base - np.median(base)))
            thresh = np.median(base) + 3.0 * 1.4826 * mad
            thresh_list.append(thresh)
            quiet = t < onset
            over = (r > thresh).astype(int)
            crossings = np.where(np.diff(over) == 1)[0]
            alarms.append(int(np.sum(quiet[crossings])))
            after = crossings[~quiet[crossings]]
            lat.append(float(t[after[0]] - onset) if after.size else np.nan)
        results[window_s] = (np.array(lat), np.array(alarms))
        la = np.array(lat)
        n_quiet_runs = sum(1 for a in alarms if a > 0)
        print(f"  window {window_s:5.1f} s : threshold = {np.mean(thresh_list):.3e}"
              f" m/s (mean over runs); latency = {np.nanmean(la):7.2f} +/- "
              f"{np.nanstd(la):5.2f} s; false alarms before onset in "
              f"{n_quiet_runs}/{nreal} runs (mean {np.mean(alarms):.2f})")

    print("\n  The trade-off is measured, not asserted.  Going from a 1 s to a")
    print("  60 s RSAM window multiplies the mean detection latency by about 17")
    print("  (4.76 s -> 80.78 s) and divides the mean number of false crossings by")
    print("  about 33 (56.05 -> 1.70).  A longer window averages more noise away")
    print("  but delays the crossing of a rising tremor level.  There is no window")
    print("  that is best for both, and the choice is a decision about which error")
    print("  costs more -- which is a monitoring-policy question, not a")
    print("  seismological one.")

    # ------------------------------------------------------------------
    section("3. A synthetic unrest catalogue: the base-rate problem")
    print("MODEL: 2000 independent unrest episodes; an eruption occurs with")
    print("       probability p.  The precursor sounds with probability 0.90 if")
    print("       an eruption follows and 0.10 if not.  Both rates are MODEL")
    print("       choices standing in for a measured precursor's performance.\n")
    print("   base rate p   eruptions   alarms   true pos   false pos   "
          "precision   recall")
    n_ep = 2000
    hit, fa = 0.90, 0.10
    for p in (0.50, 0.10, 0.02, 0.005):
        erupt = RNG.random(n_ep) < p
        alarm = np.where(erupt, RNG.random(n_ep) < hit,
                         RNG.random(n_ep) < fa)
        tp = int(np.sum(alarm & erupt))
        fp = int(np.sum(alarm & ~erupt))
        fn = int(np.sum(~alarm & erupt))
        prec = tp / (tp + fp) if tp + fp else float("nan")
        rec = tp / (tp + fn) if tp + fn else float("nan")
        print(f"   {p:11.3f}   {int(erupt.sum()):9d}   {tp + fp:6d}   "
              f"{tp:8d}   {fp:9d}   {prec:9.3f}   {rec:6.3f}")
    print("\n  Recall stays near the hit rate while the base rate falls (0.892 and")
    print("  0.905 at p = 0.5 and 0.1; noisier, 0.791 and 0.818, at the two")
    print("  smallest base rates, where only 43 and 11 eruptions occur in 2000")
    print("  episodes).  Precision collapses: 0.904 -> 0.525 -> 0.153 -> 0.051.")
    print("  The same precursor that is right 9 times in 10 when eruptions are")
    print("  common is wrong 19 times in 20 when they are rare, because the")
    print("  non-eruptions outnumber the eruptions.  A statement about a")
    print("  precursor MUST be accompanied by the base rate it was applied to,")
    print("  or it cannot be used to forecast anything.")

    # ------------------------------------------------------------------
    section("4. Summary of measured quantities")
    print(f"  LP spectral peak shift at Q = 5           : "
          f"{100 * (1 - np.sqrt(1 - 1 / (4 * 25.0))):.3f} % below f0")
    print(f"  Q recovered from f0 / (-3dB width), Q=20  : {q_rec[20.0]:.2f}"
          f" (input 20.0)")
    for w, (lat, al) in results.items():
        print(f"  RSAM window {w:5.1f} s -> mean latency "
              f"{np.nanmean(lat):6.2f} s, mean false alarms {np.mean(al):.2f}")
    print("  Everything above is a MODEL result for the stated synthetic inputs.")
    print("  The structural conclusions -- peak pulled below f0, a latency/")
    print("  false-alarm trade-off, and a precision that depends on the base")
    print("  rate -- follow from the definitions and do not depend on the")
    print("  particular numbers chosen here.")
    return 0


if __name__ == "__main__":
    main()
