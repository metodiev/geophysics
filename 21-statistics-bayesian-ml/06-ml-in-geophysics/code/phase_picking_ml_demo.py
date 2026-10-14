#!/usr/bin/env python3
"""Phase picking: a threshold crossing versus a learned window classifier.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python phase_picking_ml_demo.py

Everything here is SYNTHETIC.  Records are a Ricker wavelet with a known onset
plus Gaussian noise generated below; no waveform, catalogue or picker archive is
read, and no published pick-error distribution is quoted.

Sections
--------
1. The synthetic record and the two pickers.
2. Pick-error statistics at a comfortable signal-to-noise ratio.
3. The same measurement when the signal is four times weaker.
4. What the tolerance and the label definition do to the reported error.
"""

import numpy as np
from scipy.ndimage import uniform_filter1d
from sklearn.linear_model import LogisticRegression

RNG = np.random.default_rng(20261014)

FS = 100.0          # sampling rate, Hz
NTR = 300           # samples per record (3.0 s)
ONSET = 150         # true P onset, samples (1.50 s)
EVENT_F = 8.0       # wavelet dominant frequency, Hz
N_TRAIN = 60        # training records
N_TEST = 200        # test records
WIN = 20            # classifier window length, samples (0.20 s)
SNR_LEVELS = (10.0, 4.0)   # event peak / noise RMS, dB


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def ricker(t, f):
    a = (np.pi * f * t) ** 2
    return (1.0 - 2.0 * a) * np.exp(-a)


def synth(snr_db):
    """One record: noise plus a wavelet whose peak is snr_db above the RMS."""
    noise = RNG.standard_normal(NTR)
    t = np.arange(NTR) / FS
    wavelet = ricker(t - ONSET / FS, EVENT_F)
    wavelet = wavelet / np.abs(wavelet).max()
    amplitude = 10 ** (snr_db / 20.0) * np.sqrt(np.mean(noise ** 2))
    return amplitude * wavelet + noise


def stalta_ratio(x):
    ms = x ** 2
    sta = uniform_filter1d(ms, 20, mode="nearest")
    lta = uniform_filter1d(ms, 160, mode="nearest")
    return sta / np.maximum(lta, 1e-12)


def window_features(x, ratio):
    """Features of every WIN-sample window, one row per window start."""
    n = x.size - WIN + 1
    rows = np.empty((n, 4))
    freq = np.fft.rfftfreq(WIN, d=1.0 / FS)
    hi = (freq >= 4.0) & (freq <= 12.0)
    lo = (freq >= 0.5) & (freq <= 2.0)
    for i in range(n):
        w = x[i:i + WIN]
        ms = float(np.mean(w ** 2))
        spec = np.abs(np.fft.rfft(w)) ** 2
        rows[i, 0] = np.log10(ms + 1e-12)
        rows[i, 1] = np.log10(float(ratio[i:i + WIN].max()) + 1e-12)
        rows[i, 2] = np.log10(float(np.mean(w ** 4) / max(ms ** 2, 1e-12)) + 1e-12)
        rows[i, 3] = np.log10(float(spec[hi].sum() / max(spec[lo].sum(), 1e-12))
                              + 1e-12)
    return rows


def build_dataset(snr_db, n_records):
    features, labels = [], []
    for _ in range(n_records):
        x = synth(snr_db)
        rows = window_features(x, stalta_ratio(x))
        rows = rows[:NTR - WIN + 1]
        starts = np.arange(rows.shape[0])
        lab = ((starts >= ONSET) & (starts < ONSET + WIN)).astype(int)
        features.append(rows)
        labels.append(lab)
    return np.vstack(features), np.concatenate(labels)


def stalta_pick(x, threshold=3.0):
    ratio = stalta_ratio(x)
    hits = np.nonzero((ratio > threshold) & (np.arange(x.size) >= 50))[0]
    return int(hits[0]) if hits.size else int(np.argmax(ratio))


def learned_pick(x, clf, mean, sd):
    rows = window_features(x, stalta_ratio(x))
    prob = clf.predict_proba((rows - mean) / sd)[:, 1]
    hits = np.nonzero(prob >= 0.5)[0]
    return int(hits[0]) if hits.size else int(np.argmax(prob))


def report(tag, errors):
    errors = np.asarray(errors, dtype=float)
    print(f"  {tag}")
    print(f"    picks made on all {errors.size} records")
    print(f"    bias   = {errors.mean():+.3f} s (mean signed error, "
          f"latched = late)")
    print(f"    MAE    = {np.abs(errors).mean():.3f} s, "
          f"scatter (1 s.d.) = {errors.std(ddof=1):.3f} s")
    for tol in (0.02, 0.05, 0.10):
        print(f"    within +/-{tol:.2f} s: {np.mean(np.abs(errors) <= tol):.3f}")


def main():
    section("1. The synthetic record and the two pickers")
    print(f"SYNTHETIC records: {NTR} samples at {FS:.0f} Hz "
          f"({NTR / FS:.1f} s), true onset at sample {ONSET} "
          f"({ONSET / FS:.2f} s)")
    print(f"  wavelet: {EVENT_F:.0f} Hz Ricker, peak amplitude "
          f"{10 ** (SNR_LEVELS[0] / 20):.2f} x noise RMS at 10 dB")
    print(f"  classifier: {WIN}-sample windows, stride 1, label 1 when the "
          f"window contains the onset")
    print(f"  training records per SNR: {N_TRAIN}, test records: {N_TEST}")

    for snr in SNR_LEVELS:
        x_train, y_train = build_dataset(snr, N_TRAIN)
        mean, sd = x_train.mean(axis=0), x_train.std(axis=0)
        clf = LogisticRegression(max_iter=2000)
        clf.fit((x_train - mean) / sd, y_train)

        sta_err, ml_err = [], []
        for _ in range(N_TEST):
            x = synth(snr)
            sta_err.append(stalta_pick(x) / FS - ONSET / FS)
            ml_err.append(learned_pick(x, clf, mean, sd) / FS - ONSET / FS)

        title = ("2. Pick-error statistics at peak/RMS = "
                 f"{10 ** (snr / 20):.2f} ({snr:.0f} dB)")
        if snr == SNR_LEVELS[1]:
            title = ("3. The same measurement at peak/RMS = "
                     f"{10 ** (snr / 20):.2f} ({snr:.0f} dB)")
        section(title)
        print(f"  training positives: {int(y_train.sum())} of {y_train.size} "
              f"windows ({100 * y_train.mean():.1f}%)")
        report("STA/LTA first crossing above ratio 3.0:", sta_err)
        report("learned window classifier, first probability above 0.5:", ml_err)

    section("4. What the tolerance and the label do to the reported error")
    print("  The same picks are scored at three tolerances above; the 'accuracy'")
    print("  of a picker is therefore a statement about the tolerance as much as")
    print("  about the picker.")
    print("  The learned picker latches on the leading edge of the labelled")
    print("  window, so it carries a negative bias by construction: the label")
    print("  says 'the onset is somewhere in this 0.20 s window', not 'here'.")
    print("  The STA/LTA picker carries the opposite bias, because the ratio")
    print("  needs the short-term average to build up before it crosses.")
    print("\nSYNTHETIC: the picks were made on records generated by this script;")
    print("the error statistics describe this generator and this picker pair.")


if __name__ == "__main__":
    main()
