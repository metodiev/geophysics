#!/usr/bin/env python3
"""Cross-spectra, coherence and phase: the SciPy cross-spectrum convention
(stated and verified), transfer-function estimation in noise, coherence against
its exact SNR/(1+SNR) form, the bias of a K-average coherence estimate, the
significance threshold checked by its false-alarm rate, and delay estimation from
the cross-spectrum phase.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cross_spectra_coherence_demo.py

All models and data in this module are SYNTHETIC.  The input is generated white
noise, the system is a short FIR filter and the noise is added here, so every
comparison is against algebra.

Contents
--------
1.  The cross-spectrum convention of scipy.signal.csd, verified on a known delay.
2.  Transfer-function estimation: H_hat = S_yx / S_xx against freqz(h), with the
    measured error against the coherence-based prediction.
3.  Coherence against the exact SNR/(1+SNR) for a known noise level.
4.  Bias of a K-average coherence estimate against gamma^2 + (1-gamma^2)^2 / K.
5.  The significance threshold, checked bin by bin and for a searched maximum.
6.  Delay estimation from the cross-spectrum phase, with the measured scaling.
7.  Coherence is not correlation: a pure delay has zero zero-lag correlation.
"""

import numpy as np
from scipy import signal as sps

RNG = np.random.default_rng(20261014)

FS = 100.0
DT = 1.0 / FS
NPSEG = 512
H_FILTER = np.array([0.5, 1.0, 0.5])      # a symmetric 3-point kernel


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def cross_spectra(x, y, npseg=NPSEG):
    """Welch cross- and auto-spectra.

    Convention (verified in section 1): scipy.signal.csd(a, b) returns
    conj(A(f)) B(f), so csd(x, y) is the cross-spectrum with x as the input
    signal; for y = x delayed by tau its phase is -omega tau.
    """
    f, Sxx = sps.welch(x, fs=FS, nperseg=npseg, noverlap=npseg // 2,
                       detrend=False, scaling="density")
    _, Syy = sps.welch(y, fs=FS, nperseg=npseg, noverlap=npseg // 2,
                       detrend=False, scaling="density")
    _, Syx = sps.csd(x, y, fs=FS, nperseg=npseg, noverlap=npseg // 2,
                     detrend=False, scaling="density")
    gamma2 = np.abs(Syx) ** 2 / (Sxx * Syy)
    return f, Sxx, Syy, Syx, gamma2


def segments_in(n, npseg):
    return 1 + (n - npseg) // (npseg // 2)


def main():
    section("1. The cross-spectrum convention of scipy.signal.csd")
    n = 8192
    x = RNG.normal(0.0, 1.0, n)
    delay_true = 3
    y = np.roll(x, delay_true)
    f, _, _, Syx_xy, _ = cross_spectra(x, y)
    _, _, _, Syx_yx, _ = cross_spectra(y, x)
    omega = 2 * np.pi * f / FS
    slope_xy = np.polyfit(omega, np.unwrap(np.angle(Syx_xy)), 1)[0]
    slope_yx = np.polyfit(omega, np.unwrap(np.angle(Syx_yx)), 1)[0]
    print(f"x and y = x delayed by {delay_true} samples")
    print(f"   slope of the phase of csd(x, y) = {slope_xy:+.6f} rad per rad/"
          f"sample   (exact -tau = {-delay_true})")
    print(f"   slope of the phase of csd(y, x) = {slope_yx:+.6f}   (exact +tau)")
    print("so csd(a, b) returns conj(A) B: the phase decreases with frequency")
    print("when the first argument leads, and the delay is -d(phase)/domega of")
    print("csd(x, y) with x the input")
    print(f"   conjugate symmetry: max|csd(x,y) - conj(csd(y,x))| = "
          f"{np.max(np.abs(Syx_xy - np.conj(Syx_yx))):.3e}")

    section("2. Transfer function estimation in noise")
    n = 8192
    x = RNG.normal(0.0, 1.0, n)
    y_true = sps.lfilter(H_FILTER, [1.0], x)          # causal, delay 1 sample
    snr_db = 10.0
    y = y_true + RNG.normal(0.0, np.std(y_true) * 10 ** (-snr_db / 20.0), n)
    f, Sxx, Syy, Syx, gamma2 = cross_spectra(x, y)
    _, H_exact = sps.freqz(H_FILTER, worN=2 * np.pi * f / FS)
    H_hat = Syx / Sxx                                  # S_yx / S_xx
    k = segments_in(n, NPSEG)
    predicted = np.sqrt((1.0 - gamma2) / (gamma2 * k))
    mask = np.abs(H_exact) > 0.05          # exclude the filter's null
    rel = np.abs(H_hat - H_exact) / np.where(mask, np.abs(H_exact), 1.0)
    print(f"system h = {H_FILTER} applied causally, white input, output noise "
          f"{snr_db:.0f} dB below the signal")
    print(f"Welch with nperseg = {NPSEG}, 50 % overlap: K = {k} segments")
    print("   f (Hz)   |H_exact|   |H_hat|    rel. error   coherence   "
          "predicted std")
    for target in (0.0, 2.5, 5.0, 12.5, 25.0):
        i = int(np.argmin(np.abs(f - target)))
        print(f"   {f[i]:6.2f}   {abs(H_exact[i]):9.4f}   {abs(H_hat[i]):8.4f}   "
              f"{rel[i]:11.4f}   {gamma2[i]:9.4f}   {predicted[i]:13.4f}")
    good = gamma2 > 0.9
    print(f"median relative error where coherence > 0.9: measured "
          f"{float(np.median(rel[good])):.4f}, predicted "
          f"sqrt((1-g2)/(g2 K)): {float(np.median(predicted[good])):.4f}")
    print(f"median relative error where coherence < 0.5: "
          f"{float(np.median(rel[gamma2 < 0.5])):.4f}: the estimate is useless")
    print("the relative error of the transfer function is set by the coherence")
    print("and the number of averages, not by the record length alone")

    section("3. Coherence against the exact SNR/(1+SNR)")
    print("y = a x + b n with a^2 = gamma^2, b^2 = 1 - gamma^2, independent white")
    print("x and n: the true coherence is gamma^2 at every frequency")
    n = 16384
    k = segments_in(n, NPSEG)
    print(f"NPSEG = {NPSEG}, 50 % overlap, K = {k} segments, bias prediction "
          f"1/K = {1.0 / k:.4f}")
    print("   gamma^2   mean coherence over bins   scatter of the per-record mean"
          "   records")
    for g2 in (0.0, 0.25, 0.5, 0.9):
        means = []
        for _ in range(60):
            xx = RNG.normal(0.0, 1.0, n)
            nn = RNG.normal(0.0, 1.0, n)
            yy = np.sqrt(g2) * xx + np.sqrt(1.0 - g2) * nn
            _, _, _, _, g2h = cross_spectra(xx, yy)
            means.append(float(np.mean(g2h)))
        means = np.array(means)
        print(f"   {g2:6.2f}   {means.mean():25.4f}   {means.std(ddof=1):30.4f}"
              f"   {means.size:7d}")
    print("the measured mean is the true coherence plus the 1/K bias, so a")
    print("coherence read from a few averages always overstates the relationship")

    section("4. Bias of a K-average coherence estimate")
    print("theory for independent averages: "
          "E[gamma^2_hat] ~ gamma^2 + (1-gamma^2)^2 / K")
    n = 8192
    print("   K     gamma^2 = 0: measured   formula    gamma^2 = 0.5: measured"
          "   formula")
    for npseg in (2048, 512, 128):
        k = segments_in(n, npseg)
        res = {}
        for g2 in (0.0, 0.5):
            means = []
            for _ in range(200):
                xx = RNG.normal(0.0, 1.0, n)
                nn = RNG.normal(0.0, 1.0, n)
                yy = np.sqrt(g2) * xx + np.sqrt(1.0 - g2) * nn
                _, _, _, _, g2h = cross_spectra(xx, yy, npseg)
                means.append(float(np.mean(g2h)))
            res[g2] = float(np.mean(means))
        print(f"   {k:4d}   {res[0.0]:20.4f}   {1.0 / k:8.4f}   "
              f"{res[0.5]:21.4f}   {(0.5 + 0.25 / k):8.4f}")
    print("the formula is confirmed at both coherence levels; the consequence is")
    print("that a coherence of 0.1 from four averages is not evidence at all")

    section("5. The significance threshold, checked by its false-alarm rate")
    n = 8192
    alpha = 0.05
    print("for incoherent signals P[gamma^2_hat <= c] = (1-c)^(K-1), so the")
    print("threshold for a single pre-selected bin is c = 1 - alpha^(1/(K-1))")
    print("   K     threshold   fraction above: one bin   fraction above: the"
          " maximum of 31 bins")
    for npseg in (2048, 512, 128):
        k = segments_in(n, npseg)
        thr = 1.0 - alpha ** (1.0 / (k - 1))
        trials = 400
        above_bin = 0
        above_max = 0
        for _ in range(trials):
            xx = RNG.normal(0.0, 1.0, n)
            nn = RNG.normal(0.0, 1.0, n)
            _, _, _, _, g2h = cross_spectra(xx, nn, npseg)
            mid = g2h.size // 2
            if g2h[mid] > thr:
                above_bin += 1
            if g2h[1:mid + 1].max() > thr:
                above_max += 1
        print(f"   {k:4d}   {thr:9.4f}   {above_bin / trials:24.3f}   "
              f"{above_max / trials:36.3f}")
    print("the threshold delivers the claimed rate for one pre-selected bin and")
    print("fails badly for a maximum over a band: a search must use a threshold")
    print("corrected for the number of bins searched, not this one")

    section("6. Delay estimation from the cross-spectrum phase")
    delay_true = 3
    n = 16384
    band = (5.0, 15.0)
    sos = sps.butter(4, np.array(band) / (FS / 2), btype="band", output="sos")
    print(f"x = band-limited white noise {band[0]:.0f}-{band[1]:.0f} Hz, "
          f"y = x delayed by {delay_true} samples plus noise")
    print("   noise (dB)   mean delay   std of the mean   bias   "
          "sqrt(predicted variance)")
    f_dom = 0.5 * (band[0] + band[1])
    stds = []
    for snr_db in (20.0, 10.0, 3.0):
        est = []
        for _ in range(60):
            xx = sps.sosfilt(sos, RNG.normal(0.0, 1.0, n))
            yy = np.roll(xx, delay_true)
            yy = yy + RNG.normal(0.0, np.std(yy) * 10 ** (-snr_db / 20.0), n)
            f, _, _, Syx, g2 = cross_spectra(xx, yy, 512)
            sel = (f >= band[0]) & (f <= band[1])
            omega = 2 * np.pi * f[sel] / FS
            phase = np.unwrap(np.angle(Syx[sel]))
            slope = np.polyfit(omega, phase, 1, w=np.sqrt(g2[sel] ** 2))[0]
            est.append(-slope)                      # delay = -d phase / d omega
        est = np.array(est)
        stds.append(est.std(ddof=1))
        pred = 1.0 / (2 * np.pi * f_dom * np.sqrt(10 ** (snr_db / 10.0)))
        print(f"   {snr_db:9.0f}   {est.mean():10.4f}   {est.std(ddof=1):16.4f}   "
              f"{est.mean() - delay_true:+6.4f}   {pred:24.4f}")
    print(f"the estimate is unbiased at all three noise levels: the largest bias")
    print(f"is {abs(est.mean() - delay_true):.4f} samples against a scatter of "
          f"{est.std(ddof=1):.4f}")
    print(f"measured scatter ratios: {stds[1] / stds[0]:.2f} for a 10 dB step and "
          f"{stds[2] / stds[1]:.2f} for a 7 dB step, against "
          f"{10 ** (10 / 20):.2f} and {10 ** (7 / 20):.2f} predicted by the "
          f"1/sqrt(SNR) scaling")
    print("the simple prediction is a factor of a few optimistic in absolute")
    print("terms, so use it for scaling, not for a quoted uncertainty")

    section("7. Coherence is not correlation")
    n = 8192
    x = RNG.normal(0.0, 1.0, n)
    for g2_true in (0.9, 0.5, 0.1, 0.0):
        xx = RNG.normal(0.0, 1.0, n)
        yy = (np.sqrt(g2_true) * xx
              + np.sqrt(1.0 - g2_true) * RNG.normal(0.0, 1.0, n))
        r = np.corrcoef(xx, yy)[0, 1]
        _, _, _, _, g2 = cross_spectra(xx, yy)
        print(f"true coherence {g2_true:.1f}: zero-lag correlation = {r:+.4f}, "
              f"mean coherence = {g2.mean():.4f}")
    xx = sps.sosfilt(sos, RNG.normal(0.0, 1.0, n))
    y_delayed = np.roll(xx, 20)
    r = np.corrcoef(xx, y_delayed)[0, 1]
    f, _, _, _, g2 = cross_spectra(xx, y_delayed)
    inband = (f >= band[0]) & (f <= band[1])
    print(f"pure 20-sample delay, no noise: zero-lag correlation = {r:+.4f}, "
          f"mean coherence in band = {g2[inband].mean():.4f}")
    print("a zero-lag correlation near zero is compatible with a coherence near 1")
    print("in the signal band: correlation is one number at one lag, coherence is")
    print("per-frequency and invariant to a time shift")


if __name__ == "__main__":
    main()
