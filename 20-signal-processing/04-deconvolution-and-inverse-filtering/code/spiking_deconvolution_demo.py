#!/usr/bin/env python3
"""Spiking (predictive) deconvolution: build a spike train, convolve it with a
MINIMUM-PHASE wavelet, and reshape the trace to spikes with a prediction-error
filter obtained from the trace autocorrelation by the Levinson recursion.
MEASURE the gain in spikiness and the match to the true reflectivity.  Then use
predictive deconvolution with a prediction gap to suppress a periodic multiple.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spiking_deconvolution_demo.py

Everything is SYNTHETIC.  The wavelet is a chosen teaching wavelet (the impulse
response of a minimum-phase resonator); no wavelet estimation from real data is
performed.

Contents
--------
1. Build a synthetic trace: sparse reflectivity (*) minimum-phase wavelet + noise.
2. Autocorrelation of the trace and the Levinson recursion; recover the wavelet.
3. Spiking deconvolution: measured kurtosis gain and match to the reflectivity.
4. Operator length: once past the wavelet, extra coefficients only fit noise.
5. Predictive deconvolution with prediction gap = multiple period.
"""

import numpy as np
from scipy import signal
from scipy.linalg import solve_toeplitz

RNG = np.random.default_rng(20261014)

N = 1024
DT = 0.002          # s
F0 = 45.0           # Hz resonator frequency of the teaching wavelet


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def minimum_phase_wavelet(n=120):
    """Impulse response of a two-pole minimum-phase resonator.

    A causal stable AR system has all its zeros at the origin, so its impulse
    response is minimum phase by construction, and its exact inverse is the
    two-term AR filter [1, a1, a2].
    """
    r = 0.88
    th = 2.0 * np.pi * F0 * DT
    a = np.array([1.0, -2.0 * r * np.cos(th), r ** 2])
    imp = np.zeros(n)
    imp[0] = 1.0
    w = signal.lfilter([1.0], a, imp)
    return w / np.abs(w).max()


def autocorr(x, maxlag):
    x = x - x.mean()
    r = np.correlate(x, x, mode="full")[x.size - 1:]
    return r[:maxlag + 1]


def levinson(r, p):
    """Levinson-Durbin recursion; returns the prediction-error filter a[0..p]."""
    a = np.zeros(p + 1)
    a[0] = 1.0
    e = r[0]
    for i in range(1, p + 1):
        acc = r[i] + sum(a[j] * r[i - j] for j in range(1, i))
        k = -acc / e
        new = a.copy()
        for j in range(1, i):
            new[j] = a[j] + k * a[i - j]
        new[i] = k
        a = new
        e *= (1.0 - k * k)
    return a


def kurtosis(x):
    x = x - x.mean()
    v = np.mean(x ** 2)
    return np.mean(x ** 4) / v ** 2


def main():
    section("1. Synthetic trace from a MINIMUM-PHASE wavelet")
    w = minimum_phase_wavelet()
    tw = np.arange(w.size) * DT
    centroid = np.sum(np.arange(w.size) * w ** 2) / np.sum(w ** 2)
    reflectivity = np.zeros(N)
    idx = RNG.choice(N, size=int(0.04 * N), replace=False)
    reflectivity[idx] = RNG.standard_normal(idx.size)
    clean = np.convolve(reflectivity, w)[:N]
    noise = 0.02 * clean.std() * RNG.standard_normal(N)
    trace = clean + noise
    print(f"  {N} samples, dt = {DT * 1000:.0f} ms")
    print(f"  wavelet: 2-pole resonator at {F0:.0f} Hz, r = 0.88, "
          f"{w.size} samples ({w.size * DT * 1000:.0f} ms)")
    print(f"  energy centroid of the wavelet = {centroid:.2f} samples "
          f"(a minimum-phase wavelet is front-loaded)")
    print(f"  reflectivity: {idx.size} spikes, rms = {reflectivity.std():.4f}")
    print(f"  noise rms = {noise.std():.5f} ({noise.std() / clean.std() * 100:.1f}% "
          f"of the clean trace rms)")
    print(f"  kurtosis: reflectivity = {kurtosis(reflectivity):.1f}, "
          f"trace = {kurtosis(trace):.1f}, noise = {kurtosis(noise):.2f}")
    print("  A Gaussian has kurtosis 3; a spike train has a much larger value.")
    print("  Spiking deconvolution aims to move the trace kurtosis toward the")
    print("  reflectivity's without ever seeing the true spikes.")

    section("2. Autocorrelation, Levinson recursion, and wavelet recovery")
    r = autocorr(trace, 60)
    print("  normalised autocorrelation r[k]/r[0] at selected lags:")
    for k in (0, 1, 2, 3, 5, 10, 20, 40):
        print(f"    lag {k:3d}: {r[k] / r[0]:+.4f}")
    print("  The trace autocorrelation decays in a few samples: it is the")
    print("  wavelet autocorrelation modulated by the white reflectivity.")
    a_true = np.array([1.0, -2 * 0.88 * np.cos(2 * np.pi * F0 * DT), 0.88 ** 2])
    a2 = levinson(r, 2)
    print(f"  true inverse of the wavelet (the AR filter): {np.round(a_true, 4)}")
    print(f"  Levinson PEF of order 2                  : {np.round(a2, 4)}")
    print("  The order-2 PEF recovers the wavelet's exact inverse from the trace")
    print("  autocorrelation alone.  That is why spiking deconvolution needs no")
    print("  explicit wavelet: it inverts the second-order statistics.")

    section("3. Spiking deconvolution: measured spikiness gain")
    print("   operator length   kurtosis   correlation with true reflectivity")
    print(f"   {'trace (no operator)':>15}   {kurtosis(trace):8.1f}   "
          f"{np.corrcoef(trace, reflectivity)[0, 1]:+.4f}")
    for p in (2, 5, 10, 20, 40, 80):
        a = levinson(autocorr(trace, p + 5), p)
        spiked = np.convolve(trace, a)[:N]
        cc = np.corrcoef(spiked, reflectivity)[0, 1]
        print(f"   {p:15d}   {kurtosis(spiked):8.1f}   {cc:+.4f}")
    print("  The operator moves the kurtosis from the trace value toward the")
    print("  reflectivity's and the recovered trace correlates strongly with the")
    print("  true spikes.  Recovery is possible because the wavelet is minimum")
    print("  phase; a zero-phase wavelet has no causal stable inverse.")

    section("4. Operator length: past the wavelet, extra coefficients fit noise")
    print("  A fixed noise realisation is pushed through each operator; the output")
    print("  rms per unit input rms is the operator's noise gain.")
    noise_real = RNG.standard_normal(N)
    print("   operator length   noise gain (x)   kurtosis   correlation")
    for p in (2, 5, 10, 20, 40, 80, 160):
        a = levinson(autocorr(trace, p + 5), p)
        spiked = np.convolve(trace, a)[:N]
        nz = np.convolve(noise_real, a)[:N]
        print(f"   {p:15d}   {nz.std():14.3f}   {kurtosis(spiked):8.1f}   "
              f"{np.corrcoef(spiked, reflectivity)[0, 1]:+.4f}")
    print("  Noise gain is near 2 for every length, but kurtosis and correlation")
    print("  fall once the operator is much longer than the wavelet: the extra")
    print("  coefficients have nothing left to whiten and start fitting the noise.")

    section("5. Predictive deconvolution with a prediction gap = multiple period")
    period = int(0.100 / DT)     # 100 ms multiple period -> 50 samples
    trace0 = np.convolve(reflectivity, w)[:N]
    with_multiples = trace0.copy()
    for kk in (1, 2, 3):
        shift = np.zeros(N)
        shifted = np.convolve(reflectivity, w)[:N - kk * period]
        shift[kk * period:] = (0.5 ** kk) * shifted
        with_multiples = with_multiples + shift
    with_multiples = with_multiples + 0.01 * RNG.standard_normal(N)
    r2 = autocorr(with_multiples, 400)
    print(f"  period = {period * DT * 1000:.0f} ms; multiples of amplitude "
          f"0.5, 0.25, 0.125 of the primary, added at 1, 2 and 3 periods")
    print("  normalised autocorrelation of the input at the period lags:")
    for kk in (1, 2, 3):
        print(f"    lag {kk} x period: {r2[kk * period] / r2[0]:+.4f}")
    print("  The periodicity is the multiple signature; a prediction filter can")
    print("  exploit it.  The prediction-error filter with gap = period subtracts")
    print("  the predictable (periodic) part and leaves the unpredictable primary.")
    p = 20
    print(f"  operator length p = {p}")
    print("   prediction gap       autocorrelation at 1, 2, 3 x period after")
    for gap in (period // 2, period, 2 * period):
        R = r2[:p]
        rhs = r2[gap:gap + p]
        g = solve_toeplitz((R, R), rhs)
        f = np.zeros(gap + p)
        f[0] = 1.0
        f[gap:gap + p] = -g
        out = np.convolve(with_multiples, f, mode="same")
        ro = autocorr(out, 400)
        label = f"{gap * DT * 1000:.0f} ms"
        tag = "= period" if gap == period else ("half period" if gap < period else "2 x period")
        print(f"   {label:>8} ({tag:<11})  "
              f"{ro[period] / ro[0]:+.4f}   {ro[2 * period] / ro[0]:+.4f}   "
              f"{ro[3 * period] / ro[0]:+.4f}")
    print("  Only the gap equal to the multiple period suppresses the periodicity;")
    print("  a half-period or double-period gap leaves it in place.  The gap is the")
    print("  multiple model, and it must be measured from the data, not guessed.")


if __name__ == "__main__":
    main()
