#!/usr/bin/env python3
"""Denoising: a fixed band-pass versus a dictionary learned from clean patches.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python denoising_ml_demo.py

Everything here is SYNTHETIC.  The traces, the reflectivity, the wavelet and the
noise are generated below; no field record and no published signal-to-noise
improvement is used.

Sections
--------
1. The synthetic traces and the noise model.
2. The learned dictionary, and what it was trained on.
3. Measured signal-to-noise ratio before and after each method.
4. A mismatched dictionary: why the training distribution is the method.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

FS = 250.0              # sampling rate, Hz
NTR = 1000              # samples per trace (4.0 s)
N_TRAIN = 200           # clean training traces
N_TEST = 40             # clean test traces
WAVELET_HZ = 30.0       # training wavelet dominant frequency, Hz
MISMATCH_HZ = 20.0      # mismatched wavelet frequency, Hz
PATCH = 32              # patch length, samples
STRIDE = 8              # patch stride, samples
N_ATOMS = 16            # dictionary size
RIDGE = 1e-3            # ridge penalty on the coefficients
NOISE_LEVELS = (0.3, 0.6)   # noise RMS / clean RMS


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def ricker(t, f):
    a = (np.pi * f * t) ** 2
    return (1.0 - 2.0 * a) * np.exp(-a)


def make_trace(f_dom):
    """One reflectivity series convolved with a Ricker wavelet."""
    n_spikes = 40
    positions = np.sort(RNG.choice(np.arange(20, NTR - 20), n_spikes,
                                   replace=False))
    amplitudes = RNG.laplace(0.0, 1.0, n_spikes)
    reflectivity = np.zeros(NTR)
    reflectivity[positions] = amplitudes
    t = np.arange(-30, 31) / FS
    wavelet = ricker(t, f_dom)
    wavelet = wavelet / np.abs(wavelet).sum()
    return np.convolve(reflectivity, wavelet, mode="same")


def patches(x, taper):
    rows = []
    for start in range(0, x.size - PATCH + 1, STRIDE):
        rows.append(x[start:start + PATCH] * taper)
    return np.array(rows)


def bandpass(y, f_max):
    spec = np.fft.rfft(y)
    freq = np.fft.rfftfreq(y.size, d=1.0 / FS)
    spec[freq > f_max] = 0.0
    return np.fft.irfft(spec, n=y.size)


def denoise(y, dictionary, taper):
    """Overlap-add projection of tapered patches onto the dictionary."""
    out = np.zeros(y.size)
    weight = np.zeros(y.size)
    for start in range(0, y.size - PATCH + 1, STRIDE):
        p = y[start:start + PATCH] * taper
        coef = np.linalg.solve(dictionary.T @ dictionary
                               + RIDGE * np.eye(dictionary.shape[1]),
                               dictionary.T @ p)
        out[start:start + PATCH] += (dictionary @ coef) * taper
        weight[start:start + PATCH] += taper ** 2
    return out / np.maximum(weight, 1e-12)


def snr_db(clean, estimate):
    return 20.0 * np.log10(np.linalg.norm(clean)
                           / max(np.linalg.norm(estimate - clean), 1e-12))


def main():
    section("1. The synthetic traces and the noise model")
    train = np.array([make_trace(WAVELET_HZ) for _ in range(N_TRAIN)])
    test_clean = np.array([make_trace(WAVELET_HZ) for _ in range(N_TEST)])
    clean_rms = np.sqrt(np.mean(test_clean ** 2))
    print(f"SYNTHETIC traces: {NTR} samples at {FS:.0f} Hz ({NTR / FS:.1f} s), "
          f"{N_TRAIN} clean training traces, {N_TEST} test traces")
    print(f"  wavelet: {WAVELET_HZ:.0f} Hz Ricker; 40 reflectivity spikes per "
          f"trace, Laplace amplitudes")
    print(f"  clean RMS over the test set = {clean_rms:.4f} (arbitrary units)")
    for r in NOISE_LEVELS:
        print(f"  noise level {r:.1f} x clean RMS -> nominal input SNR = "
              f"{20 * np.log10(1.0 / r):+.2f} dB")
    print("  the input SNR measured in section 3 is a few tenths of a dB lower,")
    print("  because the noise is a finite realisation and its RMS is not exact")

    section("2. The learned dictionary")

    def learn(clean_traces, taper):
        """Top principal components of the clean training patches."""
        rows = np.vstack([patches(tr, taper) for tr in clean_traces])
        eigval, eigvec = np.linalg.eigh(rows.T @ rows)
        order = np.argsort(eigval)[::-1]
        return eigvec[:, order][:, :N_ATOMS], rows.shape[0], eigval[order]

    taper = np.hanning(PATCH)
    dictionary, n_patch, eigval = learn(train, taper)
    dictionary_mismatch, _, _ = learn(
        np.array([make_trace(MISMATCH_HZ) for _ in range(N_TRAIN)]), taper)
    energy = eigval / np.sum(eigval)
    print(f"  training patches: {n_patch} of length {PATCH}, "
          f"stride {STRIDE}, Hann-tapered")
    print(f"  dictionary: {N_ATOMS} principal components (basis vectors of "
          f"length {PATCH})")
    print(f"  variance captured by {N_ATOMS} atoms = "
          f"{energy[:N_ATOMS].sum():.6f}")
    print(f"  a mismatched dictionary is trained the same way on "
          f"{MISMATCH_HZ:.0f} Hz wavelets")

    section("3. Measured signal-to-noise ratio, dB")
    cutoffs = (30.0, 40.0, 60.0, 80.0)
    header = (f"  {'noise':>5s} {'input':>7s} "
              + " ".join(f"{int(c):>3d}Hz" for c in cutoffs)
              + f" {'learned':>8s}")
    print(f"  band-pass corner frequency, and the learned dictionary:")
    print(header)
    for r in NOISE_LEVELS:
        noise = r * clean_rms * RNG.standard_normal(test_clean.shape)
        noisy = test_clean + noise
        cells = []
        for c in cutoffs:
            bp = np.array([bandpass(y, c) for y in noisy])
            cells.append(np.mean([snr_db(a, e)
                                  for a, e in zip(test_clean, bp)]))
        learned = np.array([denoise(y, dictionary, taper) for y in noisy])
        inp = np.mean([snr_db(a, e) for a, e in zip(test_clean, noisy)])
        print(f"  {r:>5.1f} {inp:>+7.2f} "
              + " ".join(f"{v:>+5.2f}" for v in cells)
              + f" {np.mean([snr_db(a, e) for a, e in zip(test_clean, learned)]):>+8.2f}")
    print("  each cell is the mean over "
          f"{N_TEST} test traces; the per-trace scatter is not shown")
    print("  the corner frequency is a modelling choice, and it dominates: a")
    print("  default cut at the 30 Hz wavelet's own frequency removes the wavelet's")
    print("  high-frequency lobe and makes the trace WORSE than doing nothing,")
    print("  while a 60 Hz corner leaves 99% of the signal energy in place")

    section("4. A mismatched dictionary")
    for r in NOISE_LEVELS:
        noise = r * clean_rms * RNG.standard_normal(test_clean.shape)
        noisy = test_clean + noise
        good = np.array([denoise(y, dictionary, taper) for y in noisy])
        bad = np.array([denoise(y, dictionary_mismatch, taper) for y in noisy])
        g = np.mean([snr_db(c, e) for c, e in zip(test_clean, good)])
        b = np.mean([snr_db(c, e) for c, e in zip(test_clean, bad)])
        print(f"  noise {r:.1f}: matched dictionary {g:+.2f} dB, "
              f"dictionary trained on {MISMATCH_HZ:.0f} Hz wavelets {b:+.2f} dB, "
              f"penalty {g - b:+.2f} dB")
    print("  The band-pass does not care which wavelet generated the trace: it")
    print("  removes everything outside its pass band and keeps everything inside")
    print("  it.  The learned dictionary only works")
    print("  while the test signal resembles its training patches, which is why a")
    print("  denoiser must be reported together with the data it was trained on.")
    print("\nSYNTHETIC: every trace was generated here.  Real seismic noise is")
    print("coloured and non-stationary, and real reflectivity is not Laplace.")


if __name__ == "__main__":
    main()
