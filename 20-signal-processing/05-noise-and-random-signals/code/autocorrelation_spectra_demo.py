#!/usr/bin/env python3
"""Autocorrelation, power spectral density and the Wiener-Khinchin theorem,
measured on SYNTHETIC noise.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python autocorrelation_spectra_demo.py

Everything here is SYNTHETIC: the traces are generated below, no files are read,
and no number is quoted from a published measurement.

Sections
--------
1. Wiener-Khinchin: the periodogram is the transform of the sample
   autocovariance (verified field by field).
2. Parseval: integrating the one-sided PSD recovers the variance.
3. Periodogram inconsistency: its variance does not fall as the record grows.
4. Welch averaging: measured variance reduction versus the number of segments.
5. Bias-versus-variance: segmenting smooths two close spectral peaks together.
6. The autocorrelation of an AR(1) process against the exact rho(k) = phi^|k|.
"""

import numpy as np
from scipy import signal

RNG = np.random.default_rng(20261014)

FS = 100.0        # sampling rate, Hz
N = 8192          # samples per record
DT = 1.0 / FS     # sampling interval, s
R = 500           # realisations for the ensemble statistics
PHI = 0.90        # AR(1) coefficient
SIGMA_W = 1.0     # driving-noise standard deviation


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def white_record(rng):
    return rng.standard_normal(N)


def ar1_record(rng):
    w = SIGMA_W * rng.standard_normal(N)
    x = np.empty(N)
    x[0] = w[0] / np.sqrt(1.0 - PHI ** 2)
    for i in range(1, N):
        x[i] = PHI * x[i - 1] + w[i]
    return x


def psd_from_acf(x):
    """One-sided PSD as the Fourier transform of the circular autocovariance."""
    X = np.fft.fft(x)
    acf = np.fft.ifft(np.abs(X) ** 2).real / N
    s_full = DT * np.fft.fft(acf).real
    one_sided = np.empty(N // 2 + 1)
    one_sided[0] = s_full[0]
    one_sided[-1] = s_full[N // 2]
    one_sided[1:-1] = 2.0 * s_full[1:N // 2]
    return one_sided


def main():
    df = FS / N
    section("1. Wiener-Khinchin: periodogram versus transform of the autocovariance")
    x = white_record(RNG)
    f, p = signal.periodogram(x, fs=FS, window="boxcar", detrend=False,
                              scaling="density")
    s_acf = psd_from_acf(x)
    print(f"  record: {N} samples at {FS:.1f} Hz ({N * DT:.2f} s), df = {df:.5f} Hz")
    print(f"  max |periodogram - transform(autocovariance)| = "
          f"{np.max(np.abs(s_acf - p)):.2e}")
    print("  -> the two estimators are the same number to machine precision: the")
    print("     PSD and the autocovariance are a Fourier pair (Wiener-Khinchin).")

    section("2. Parseval: integrating the PSD recovers the variance")
    print(f"  white record variance           = {x.var():.4f}")
    print(f"  sum(PSD) * df over 0..fs/2      = {np.sum(p) * df:.4f}")
    xa = ar1_record(RNG)
    fa, pa = signal.periodogram(xa, fs=FS, window="boxcar", detrend=False,
                                scaling="density")
    var_theory = SIGMA_W ** 2 / (1.0 - PHI ** 2)
    print(f"  AR(1) record variance           = {xa.var():.4f} (one record)")
    print(f"  AR(1) sum(PSD) * df             = {np.sum(pa) * df:.4f}")
    print(f"  AR(1) exact variance            = {var_theory:.4f}")
    print("  -> the integral of the one-sided PSD is the variance, by Parseval.")

    section("3. Periodogram inconsistency: variance does not fall with record length")
    target = 10.0
    idx = int(round(target / df))
    nperseg = 256
    est_std, est_mean = {}, {}
    for length in (1024, 4096, 16384, 65536):
        vals = np.empty(R)
        for r in range(R):
            xx = RNG.standard_normal(length)
            vals[r] = signal.periodogram(xx, fs=FS, window="boxcar",
                                         detrend=False,
                                         scaling="density")[1][
                int(round(target / (FS / length)))]
        est_std[length] = vals.std() / vals.mean()
        est_mean[length] = vals.mean()
    true_white_psd = 2.0 * 1.0 / FS
    print(f"  white-noise one-sided PSD level 2 sigma^2/fs = {true_white_psd:.5f}")
    print(f"  frequency examined = {target:.1f} Hz; {R} realisations per row")
    print("     record length   mean estimate   std/mean")
    for length in est_std:
        print(f"     {length:13d}   {est_mean[length]:.5f}        "
              f"{est_std[length]:.3f}")
    print("  -> the mean is unbiased and unchanging, but std/mean stays near 1:")
    print("     a longer record does NOT make the periodogram at one frequency")
    print("     more reliable.  This is the statistical inconsistency of the")
    print("     periodogram.")

    section("4. Welch averaging: measured variance reduction versus segments")
    print("  K disjoint segments of 1024 samples, nperseg=256, 50% overlap")
    print("     segments   measured std/mean   1/sqrt(K_eff)")
    for k_target in (1, 2, 4, 8, 16):
        length = 256 * 2 * k_target
        vals = np.empty(200)
        for r in range(200):
            xx = RNG.standard_normal(length)
            fw, pw = signal.welch(xx, fs=FS, nperseg=256, noverlap=128,
                                  window="hann", detrend=False,
                                  scaling="density")
            vals[r] = pw[np.argmin(np.abs(fw - target))]
        k_eff = max(1, (length - 128) // 128)
        print(f"     {k_target:8d}   {vals.std() / vals.mean():14.3f}   "
              f"{1.0 / np.sqrt(k_eff):10.3f}")
    print("  -> averaging independent segments cuts the scatter as 1/sqrt(K),")
    print("     the price being the resolution computed in the next section.")

    section("5. Bias versus variance: segmentation merges two close peaks")
    n2 = 16384
    t = np.arange(n2) * DT
    two = np.cos(2 * np.pi * 9.5 * t) + np.cos(2 * np.pi * 10.5 * t)
    two += 0.1 * RNG.standard_normal(n2)
    print("  two equal tones at 9.5 and 10.5 Hz (1.0 Hz apart), Hann window")
    print("     segment   nominal resolution   valley/peak   verdict")
    for nperseg in (128, 256, 1024, 4096):
        fw, pw = signal.welch(two, fs=FS, nperseg=nperseg,
                              noverlap=nperseg // 2, window="hann",
                              detrend=False, scaling="density")
        pk1 = pw[np.argmin(np.abs(fw - 9.5))]
        pk2 = pw[np.argmin(np.abs(fw - 10.5))]
        valley = pw[np.argmin(np.abs(fw - 10.0))]
        ratio = valley / (0.5 * (pk1 + pk2))
        verdict = "merged" if ratio > 0.5 else "resolved"
        print(f"     {nperseg:7d}   {2 * FS / nperseg:18.3f} Hz   "
              f"{ratio:11.4f}   {verdict}")
    print("  -> the nominal Hann resolution is 2*fs/nperseg.  When it exceeds the")
    print("     1.0 Hz tone separation the two peaks merge into one: averaging")
    print("     bought variance reduction by throwing away resolution.")

    section("6. Autocorrelation of AR(1) against the exact phi^|k|")
    lags = np.arange(0, 40)
    acfs = np.empty((R, lags.size))
    for r in range(R):
        xr = ar1_record(RNG)
        xr = xr - xr.mean()
        acfs[r] = (np.correlate(xr, xr, "full")[N - 1:][:lags.size]
                   / (xr.var() * N))
    theory = PHI ** lags
    print("     lag k   measured rho(k)      exact phi^k")
    for k in (0, 5, 10, 20, 30):
        print(f"     {k:5d}   {acfs[:, k].mean():.4f} +/- "
              f"{acfs[:, k].std():.4f}      {theory[k]:.4f}")
    print(f"  max |measured mean - phi^k| over k<=39 = "
          f"{np.max(np.abs(acfs.mean(axis=0) - theory)):.4f}")
    print("  -> the measured autocorrelation reproduces the exact geometric decay,")
    print("     and the scatter is what a finite record can resolve.")


if __name__ == "__main__":
    main()
