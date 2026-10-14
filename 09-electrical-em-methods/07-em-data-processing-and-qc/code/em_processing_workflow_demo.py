#!/usr/bin/env python3
"""EM processing workflow and data editing: what each step removes, what each
step costs, and how to tell a bias from noise.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_processing_workflow_demo.py

EVERYTHING IS SYNTHETIC.  The transient decay is a chosen teaching shape,
V(t) = A (t + t0)^-p with p = 2.5, and the noise, drift and spike amplitudes are
chosen values.  No published decay, instrument or field data is used.

Contents
--------
1. The synthetic record: signal, offset drift, spikes, noise.
2. Despiking by a running median: detection, false positives, and early-gate bias.
3. Drift removal fitted in a late-time window: what "quiet window" assumes.
4. Low-pass filtering: noise reduction versus distortion at the earliest gate.
5. Stacking, standard error, and sigma-clipping.
6. A model-independent diagnostic: the fitted late-time power-law exponent.
7. Verification: running each step on the IDEAL record isolates its own bias,
   and the bias is monotone in the step's own control parameter.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC decay (chosen teaching shape) --------------------------------
AMP = 1.0            # arbitrary voltage units
T0 = 1.0e-4          # s
P_EXP = 2.5          # chosen decay exponent
T_GATES = np.array([3.0e-4, 6.0e-4, 1.2e-3, 2.4e-3, 4.0e-3, 6.0e-3])  # s
N_SAMPLES = 2048
T_MAX = 40.0e-3      # s, long enough to contain a genuinely quiet window
REL_NOISE = 0.02     # 2% of the local signal
DRIFT_FRAC = 2.0e-4  # offset at the end, as a fraction of the first sample
SPIKE_FACTOR = 25.0  # spike = 25 x the local noise amplitude


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def decay(t):
    """Synthetic transient: AMP (t + T0)^-P_EXP."""
    return AMP * (t + T0) ** (-P_EXP)


def gate_indices(t):
    return [int(np.argmin(np.abs(t - tg))) for tg in T_GATES]


def running_median(x, k):
    """Running median with window k (odd).  Edges use the available window."""
    if k < 3:
        return x.copy()
    half = k // 2
    out = np.empty_like(x)
    for i in range(len(x)):
        lo, hi = max(0, i - half), min(len(x), i + half + 1)
        out[i] = np.median(x[lo:hi])
    return out


def moving_average(x, m):
    """Centred moving average of length m."""
    if m < 2:
        return x.copy()
    out = np.empty_like(x)
    for i in range(len(x)):
        lo, hi = max(0, i - m // 2), min(len(x), i + m // 2 + 1)
        out[i] = x[lo:hi].mean()
    return out


def gated_errors(x, sig, idx):
    """Signed relative error of x against sig at the gate samples, in percent."""
    return 100.0 * (x[idx] - sig[idx]) / sig[idx]


def mean_abs_gate_error(x, sig, idx):
    """Mean absolute relative error over the gates, in percent."""
    return float(np.mean(np.abs(gated_errors(x, sig, idx))))


def fit_exponent(t, v, t_lo, t_hi):
    """Least-squares power-law exponent of v = A t^-p on [t_lo, t_hi]."""
    sel = (t >= t_lo) & (t <= t_hi) & (v > 0)
    if int(sel.sum()) < 3:
        return float("nan")
    slope, _ = np.polyfit(np.log(t[sel]), np.log(v[sel]), 1)
    return -slope


def main():
    section("1. The synthetic record")
    t = np.linspace(0.0, T_MAX, N_SAMPLES)
    sig = decay(t)
    idx = gate_indices(t)
    print(f"SYNTHETIC decay: A = {AMP:.2f}, t0 = {T0:.2e} s, p = {P_EXP:.1f}; "
          f"{N_SAMPLES} samples over {T_MAX * 1e3:.0f} ms")
    print("gate  time (us)      clean signal")
    for j, tg in enumerate(T_GATES):
        print(f"  {j + 1}   {tg * 1e6:9.1f}   {sig[idx[j]]:.6e}")
    print(f"the record spans a factor "
          f"{sig[0] / sig[-1]:.3e} from its first to its last sample: this is")
    print("why an offset that is negligible early can dominate late.")
    noise = REL_NOISE * sig * RNG.standard_normal(t.size)
    drift = DRIFT_FRAC * sig[0] * (t / t[-1])
    spikes = np.zeros_like(t)
    spike_at = RNG.choice(np.arange(5, t.size), size=6, replace=False)
    spikes[spike_at] = SPIKE_FACTOR * REL_NOISE * sig[spike_at] \
        * np.sign(RNG.standard_normal(spike_at.size))
    clean_meas = sig + drift          # what the despiker should preserve
    raw = sig + drift + noise + spikes
    print(f"\nnoise  : {REL_NOISE * 100:.1f}% of the local signal")
    print(f"drift  : linear, reaching {DRIFT_FRAC * sig[0]:.3e} at the last "
          f"sample = {DRIFT_FRAC * sig[0] / sig[-1]:.1f} x the signal there,")
    print(f"         {drift[idx[0]] / sig[idx[0]]:.2e} of the signal at gate 1 and "
          f"{drift[idx[-1]] / sig[idx[-1]]:.2f} at gate {len(T_GATES)}")
    print(f"spikes : 6 samples, amplitude {SPIKE_FACTOR * REL_NOISE:.2f} x the "
          f"local signal (samples {spike_at.min()}..{spike_at.max()})")
    print(f"late-time signal at the end of the record: {sig[-1]:.4e}; the drift")
    print(f"there is {drift[-1] / sig[-1]:.1f} x larger, so the last third of the")
    print("record is a genuinely quiet window.")
    print(f"\nfitted exponent of the RAW record       : "
          f"{fit_exponent(t[5:], raw[5:], 1.2e-3, 6.0e-3):.4f}  "
          f"(true {P_EXP:.1f})")
    print(f"fitted exponent of the IDEAL record     : "
          f"{fit_exponent(t[5:], sig[5:], 1.2e-3, 6.0e-3):.4f}")

    section("2. Despiking by a running median")
    print("Detection rule: the relative residual (x - running median)/median must")
    print("exceed a threshold of 6 sigma, where sigma is estimated from the")
    print("residual MAD.  Two ways of estimating that sigma are compared: a single")
    print("global MAD, and a LOCAL MAD in a sliding window of +-200 samples.")
    print("Errors below are against the clean measurement (signal + drift), so")
    print("they measure the despiker, not the un-removed offset.")
    print("\n  k   detector   flagged   true hits   false pos.   mean |gate err| %   "
          "exponent")

    def local_scale(res, half=200):
        n = res.size
        sc = np.empty(n)
        for i in range(n):
            lo, hi = max(0, i - half), min(n, i + half + 1)
            w = res[lo:hi]
            sc[i] = 1.4826 * np.median(np.abs(w - np.median(w)))
        return sc

    for k in (3, 5, 9):
        med = running_median(raw, k)
        resid = (raw - med) / med
        for det in ("global", "local"):
            scale = (1.4826 * np.median(np.abs(resid - np.median(resid)))
                     if det == "global" else local_scale(resid))
            flag = np.abs(resid) > 6.0 * scale
            clean = raw.copy()
            clean[flag] = med[flag]
            hits = int(np.isin(np.where(flag)[0], spike_at).sum())
            fp = int(flag.sum()) - hits
            e = mean_abs_gate_error(clean, clean_meas, idx)
            p = fit_exponent(t[5:], clean[5:], 1.2e-3, 6.0e-3)
            print(f"  {k:3d}  {det:9s}   {int(flag.sum()):7d}   {hits:9d}   "
                  f"{fp:10d}   {e:16.4f}   {p:8.4f}")
    print("The record's noise is multiplicative, so its relative noise level falls")
    print("by orders of magnitude across the record.  A single global MAD is then")
    print("dominated by the quiet late samples and sets a threshold that flags the")
    print("normal-accuracy early samples; estimating the scale locally fixes it.")
    med = running_median(raw, 5)
    resid = (raw - med) / med
    despiked = raw.copy()
    flag = np.abs(resid) > 6.0 * local_scale(resid)
    despiked[flag] = med[flag]
    print(f"with k = 5 and the local scale: {int(flag.sum())} samples flagged, of "
          f"which {int(np.isin(np.where(flag)[0], spike_at).sum())} are the six "
          f"spikes.")

    section("3. Drift removal in a late-time window")
    print("Model: x(t) = a + b t fitted in a window, then subtracted.")
    print("\n  window (ms)   fitted offset a      slope b (1/s)    mean |gate err| %   "
          "exponent")
    for w_lo, w_hi in ((30.0, 40.0), (20.0, 40.0), (10.0, 40.0), (4.0, 40.0),
                       (0.0, 40.0)):
        sel = (t >= w_lo * 1e-3) & (t <= w_hi * 1e-3)
        A = np.column_stack([np.ones(int(sel.sum())), t[sel]])
        coef, *_ = np.linalg.lstsq(A, despiked[sel], rcond=None)
        corr = despiked - (coef[0] + coef[1] * t)
        e = mean_abs_gate_error(corr, sig, idx)
        p = fit_exponent(t[5:], corr[5:], 1.2e-3, 6.0e-3)
        print(f"  {w_lo:4.1f}-{w_hi:4.1f}   {coef[0]:+.6e}   {coef[1]:+.4e}   "
              f"{e:18.4f}   {p:8.4f}" if np.isfinite(p) else
              f"  {w_lo:4.1f}-{w_hi:4.1f}   {coef[0]:+.6e}   {coef[1]:+.4e}   "
              f"{e:18.4f}   no positive signal left")
    print("A window that is genuinely quiet recovers the exponent; one that still")
    print("contains signal absorbs part of the decay, and the last row shows what")
    print("that costs.  'Quiet' is a model claim about the data, not a property of")
    print("the file, and its error is a fraction of the drift, not of the noise.")

    section("4. Low-pass filtering")
    print(f"Centred moving average; one sample = "
          f"{t[1] * 1e6:.3f} us.  The suppression is measured on a")
    print("noise-only record (signal + noise, no drift, no spikes).")
    noise_only = sig + REL_NOISE * sig * RNG.standard_normal(t.size)
    base = np.sqrt(np.mean((noise_only - sig) ** 2))
    print("\n     m   noise suppression   sqrt(m)   gate-1 bias %   gate-6 bias %")
    for m in (1, 3, 5, 9, 17):
        # the filter is linear, so the bias cancels in this difference
        resid_noise = moving_average(noise_only, m) - moving_average(sig, m)
        suppression = base / np.sqrt(np.mean(resid_noise ** 2))
        bias1 = 100.0 * (moving_average(sig, m)[idx[0]] - sig[idx[0]]) / sig[idx[0]]
        bias6 = 100.0 * (moving_average(sig, m)[idx[-1]] - sig[idx[-1]]) / sig[idx[-1]]
        print(f"  {m:5d}   {suppression:17.3f}   {np.sqrt(m):7.3f}   "
              f"{bias1:+13.4f}   {bias6:+13.4f}")
    print("The noise falls as sqrt(m) as expected, while the bias grows with m and")
    print("is concentrated at the earliest gate, where the decay changes fastest.")
    print("The filter length is a choice about which of the two you can afford.")

    section("5. Stacking, standard error and rejection")
    N = 40
    gate_signal = sig[idx]
    reps_clean = np.array([gate_signal * (1.0 + REL_NOISE * RNG.standard_normal(
        gate_signal.size)) for _ in range(N)])
    mean = reps_clean.mean(axis=0)
    sem = reps_clean.std(axis=0, ddof=1) / np.sqrt(N)
    print(f"N = {N} repeats.  First gate: mean = {mean[0]:.6e}, standard error = "
          f"{sem[0]:.6e}")
    print(f"   that is {100 * sem[0] / mean[0]:.4f}% of the mean, against the "
          f"{100 * REL_NOISE:.1f}% single-shot error")
    print("   the measured reduction factor is "
          f"{REL_NOISE * gate_signal[0] / sem[0]:.3f} for sqrt(N) = "
          f"{np.sqrt(N):.3f}")
    bad = [3, 11, 27]
    reps = reps_clean.copy()
    reps[bad, :] *= 1.25
    print(f"\nNow repeats {bad} are contaminated by a 25% gain error.")
    print("   gate   mean error %   sem error %   clipped mean error %   "
          "clipped sem %   rejected")
    for j in range(gate_signal.size):
        col = reps[:, j]
        med0 = np.median(col)
        scale = 1.4826 * np.median(np.abs(col - med0))
        keep = np.abs(col - med0) < 3.0 * scale
        e_mean = 100.0 * (col.mean() - gate_signal[j]) / gate_signal[j]
        e_sem = 100.0 * sem[j] / gate_signal[j]
        c_mean = 100.0 * (col[keep].mean() - gate_signal[j]) / gate_signal[j]
        c_sem = 100.0 * col[keep].std(ddof=1) / np.sqrt(int(keep.sum())) \
            / gate_signal[j]
        print(f"   {j + 1:4d}   {e_mean:+12.4f}   {e_sem:12.4f}   "
              f"{c_mean:+21.4f}   {c_sem:12.4f}   {N - int(keep.sum()):8d}")
    print("The standard error of the mean is the right error bar only if the")
    print("repeats are independent and the noise is stationary.  Both are claims,")
    print("and both are testable (see the exercises).")

    section("6. A model-independent diagnostic: the fitted exponent")
    def de_drift(x, w_lo, w_hi):
        sel = (t >= w_lo * 1e-3) & (t <= w_hi * 1e-3)
        return x - np.polyval(np.polyfit(t[sel], x[sel], 1), t)

    variants = [("ideal signal", sig),
                ("raw", raw),
                ("despiked (k = 5, local scale)", despiked),
                ("despiked + drift from 30-40 ms (quiet)",
                 de_drift(despiked, 30.0, 40.0)),
                ("despiked + drift from 6-40 ms (signal inside)",
                 de_drift(despiked, 6.0, 40.0)),
                ("quiet drift removal + m = 9 filter",
                 moving_average(de_drift(despiked, 30.0, 40.0), 9))]
    for name, v in variants:
        p = fit_exponent(t[5:], v[5:], 1.2e-3, 6.0e-3)
        print(f"   {name:34s}: p = {p:8.4f}  "
              f"({100 * (p - P_EXP) / P_EXP:+7.3f}%)")
    print("Every step is a biased estimator of the signal.  The honest workflow")
    print("reports the size of the bias in the units that matter, not only the")
    print("noise that was removed.")

    section("7. Verification: isolating each step's own bias")
    print("Each step is applied to the IDEAL record, where there is neither noise")
    print("nor drift nor any spike.  Whatever is left is that step's bias.")
    print("\n   step                     gate-1 error %   gate-6 error %   exponent")
    for m in (3, 5, 9, 17):
        f = moving_average(sig, m)
        e = gated_errors(f, sig, idx)
        p = fit_exponent(t[5:], f[5:], 1.2e-3, 6.0e-3)
        print(f"   moving average m = {m:3d}   {e[0]:+13.4f}   {e[-1]:+13.4f}   "
              f"{p:8.4f}")
    for k in (5, 9, 15):
        med = running_median(sig, k)
        e = gated_errors(med, sig, idx)
        p = fit_exponent(t[5:], med[5:], 1.2e-3, 6.0e-3)
        print(f"   running median  k = {k:3d}   {e[0]:+13.4f}   {e[-1]:+13.4f}   "
              f"{p:8.4f}")
    print("These numbers do not move when the noise is resampled: they are bias.")
    print("They do move monotonically with the step's own parameter, which is the")
    print("test that separates a bias from scatter.")


if __name__ == "__main__":
    main()
