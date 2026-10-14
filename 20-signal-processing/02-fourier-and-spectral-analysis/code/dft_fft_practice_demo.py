#!/usr/bin/env python3
"""Practical DFT/FFT: the exact convention numpy uses, the normalisation ladder,
Parseval, the frequency-bin conventions, the exact DFT of a boxcar against the
Dirichlet kernel, and the analytic 2/pi scalloping loss of an off-bin tone.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python dft_fft_practice_demo.py

All models and data in this module are SYNTHETIC.  Every comparison below is
against an exact algebraic identity or against the DFT computed from its own
definition, so each printed difference is a rounding residual, not an estimate.

Contents
--------
1.  DFT from the definition versus numpy.fft.fft; the inverse and its 1/N.
2.  Exact DFT identities: ones, a pure on-bin exponential, alternating +-1.
3.  The DFT of a boxcar against the analytic Dirichlet kernel.
4.  Normalisation ladder: amplitude, power and PSD, and what each recovers.
5.  Parseval in three forms, checked to rounding.
6.  fftfreq, rfftfreq and fftshift: the exact bin ordering, and the rfft trap.
7.  Scalloping loss: an off-bin tone at half a bin, against the exact 2/pi.
8.  Why leakage is not a numerical error: an integer-period record against a
    non-integer one.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def dft_by_definition(x):
    """X[k] = sum_n x[n] exp(-2 pi i k n / N), the slow way."""
    n = len(x)
    k = np.arange(n)
    return np.exp(-2j * np.pi * np.outer(k, np.arange(n)) / n) @ x


def idft_by_definition(x):
    """x[n] = (1/N) sum_k X[k] exp(+2 pi i k n / N)."""
    n = len(x)
    return (np.exp(2j * np.pi * np.outer(np.arange(n), np.arange(n)) / n) @ x) / n


def dirichlet(w, length):
    """sin(L w / 2)/sin(w / 2) with the removable singularity handled."""
    w = np.asarray(w, dtype=float)
    out = np.empty_like(w)
    small = np.abs(w) < 1e-12
    out[small] = length
    out[~small] = np.sin(length * w[~small] / 2.0) / np.sin(w[~small] / 2.0)
    return out


def main():
    section("1. The DFT from its definition versus numpy.fft")
    n = 64
    x = RNG.normal(0.0, 1.0, n)
    X_slow = dft_by_definition(x)
    X_fast = np.fft.fft(x)
    print(f"N = {n}")
    print(f"max|dft_from_definition - numpy.fft.fft| = "
          f"{np.max(np.abs(X_slow - X_fast)):.3e}")
    print(f"max|ifft_from_definition - numpy.fft.ifft| = "
          f"{np.max(np.abs(idft_by_definition(X_slow) - np.fft.ifft(X_fast))):.3e}")
    print(f"round trip max|ifft(fft(x)) - x|          = "
          f"{np.max(np.abs(np.fft.ifft(np.fft.fft(x)) - x)):.3e}")
    print("convention verified: X[k] = sum_n x[n] exp(-2 pi i k n / N),")
    print("and the inverse carries the factor 1/N (numpy does not scale fft)")

    section("2. Exact DFT identities")
    ones = np.ones(16)
    X = np.fft.fft(ones)
    print(f"DFT of ones(16): X[0] = {X[0].real:.6f} + {X[0].imag:.1e}j, "
          f"max|X[1:]| = {np.max(np.abs(X[1:])):.3e} (exact: N and 0)")
    n = 64
    k0 = 9
    z = np.exp(2j * np.pi * k0 * np.arange(n) / n)
    X = np.fft.fft(z)
    print(f"DFT of exp(+2 pi i {k0} n / N): |X[{k0}]| = {abs(X[k0]):.6f} "
          f"(exact N = {n}), max|X| elsewhere = "
          f"{np.max(np.delete(np.abs(X), k0)):.3e}")
    alt = (-1.0) ** np.arange(n)
    X = np.fft.fft(alt)
    print(f"DFT of (-1)^n: |X[N/2]| = {abs(X[n // 2]):.6f} (exact N = {n}), "
          f"max|X| elsewhere = {np.max(np.delete(np.abs(X), n // 2)):.3e}")

    section("3. The DFT of a boxcar against the analytic Dirichlet kernel")
    n = 256
    length = 32
    x = np.zeros(n)
    x[:length] = 1.0
    X = np.fft.fft(x)
    w = 2 * np.pi * np.arange(n) / n
    analytic = dirichlet(w, length) * np.exp(-1j * w * (length - 1) / 2.0)
    print(f"boxcar of length L = {length} in a record of N = {n}")
    print(f"max|DFT - Dirichlet kernel| = {np.max(np.abs(X - analytic)):.3e}")
    print(f"X[0] = {X[0].real:.1f} (exact L = {length})")
    zero_bins = [k for k in range(1, n) if k % (n // length) == 0][:4]
    print(f"exact zeros at k = {zero_bins} (multiples of N/L = {n // length}): "
          f"values {np.array2string(np.abs(X[zero_bins]), precision=2)}")
    print("the transform of a finite boxcar is the Dirichlet kernel, whose first")
    print(f"sidelobe is {20 * np.log10(0.217234):.3f} dB down (the asymptotic")
    print("rectangular-window figure)")

    section("4. The normalisation ladder")
    fs = 100.0
    n = 1000
    dt = 1.0 / fs
    t = np.arange(n) * dt
    amp, f0 = 3.0, 10.0                    # exactly bin 100 of 1000
    x = amp * np.sin(2 * np.pi * f0 * t)
    X = np.fft.rfft(x)
    freqs = np.fft.rfftfreq(n, d=dt)
    kpk = int(np.argmax(np.abs(X)))
    df = fs / n
    print(f"sine of amplitude {amp} at {f0} Hz, fs = {fs} Hz, N = {n}, df = {df} Hz")
    print(f"   raw |X[peak]|                       = {np.abs(X[kpk]):.3f}")
    print(f"   exact A N / 2                       = {amp * n / 2:.3f}")
    print(f"   two-sided power |X|^2              = {np.abs(X[kpk]) ** 2:.1f}")
    print(f"   amplitude spectrum 2|X|/N (DC excluded) = "
          f"{2 * np.abs(X[kpk]) / n:.6f}  (exact A = {amp})")
    print(f"   single-sided power spectral density 2|X|^2/(N^2 df) = "
          f"{2 * np.abs(X[kpk]) ** 2 / (n ** 2 * df):.3f} "
          f"(exact A^2 / (2 df) = {amp ** 2 / (2 * df):.3f})")
    print("units: raw X is signal-units x samples; 2|X|/N is in signal units;")
    print("2|X|^2/(N^2 df) is in (signal units)^2 per Hz")

    section("5. Parseval in three forms")
    n = 512
    fs = 200.0
    dt = 1.0 / fs
    df = fs / n
    x = RNG.normal(0.0, 2.0, n)
    X = np.fft.fft(x)
    Xr = np.fft.rfft(x)
    lhs = np.sum(x ** 2)
    print(f"sum x^2                        = {lhs:.6f}")
    print(f"(1/N) sum |X|^2                = {np.sum(np.abs(X) ** 2) / n:.6f}"
          f"   (difference {abs(lhs - np.sum(np.abs(X) ** 2) / n):.3e})")
    r_energy = (np.abs(Xr[0]) ** 2 + np.abs(Xr[-1]) ** 2
                + 2 * np.sum(np.abs(Xr[1:-1]) ** 2))
    print(f"one-sided sum (DC and Nyquist once, others doubled) = "
          f"{r_energy / n:.6f}   (difference {abs(lhs - r_energy / n):.3e})")
    psd = np.abs(Xr) ** 2 / (n ** 2 * df)
    psd[1:-1] *= 2.0
    print(f"mean square from the data      = {np.mean(x ** 2):.6f}")
    print(f"sum of the one-sided PSD x df  = {np.sum(psd) * df:.6f}"
          f"   (difference {abs(np.mean(x ** 2) - np.sum(psd) * df):.3e})")
    print(f"power = (1/N^2) sum |X|^2 = mean square; the one-sided PSD")
    print(f"P[k] = 2|X[k]|^2/(N^2 df) with df = {df:.6f} Hz integrates to it")

    section("6. fftfreq, rfftfreq and fftshift")
    n = 8
    fs = 8.0
    print(f"N = {n}, fs = {fs} Hz")
    print(f"fftfreq        = {np.fft.fftfreq(n, d=1 / fs)}")
    print(f"fftshift(fftfreq) = {np.fft.fftshift(np.fft.fftfreq(n, d=1 / fs))}")
    print(f"rfftfreq       = {np.fft.rfftfreq(n, d=1 / fs)}  "
          f"(length N//2 + 1 = {n // 2 + 1})")
    print(f"for odd N = 9: rfftfreq = {np.fft.rfftfreq(9, d=1 / fs)}")
    print("so for even N the last rfft bin is the Nyquist bin and must NOT be")
    print("doubled; for odd N there is no Nyquist bin and every bin except DC is")
    print("doubled. Applying fftshift to rfft output is meaningless: it is only")
    print("half a spectrum, and shifting it moves DC into the middle of nothing")
    X = np.fft.fft(RNG.normal(0, 1, n))
    print(f"DC bin imaginary part for a real signal: {X[0].imag:.1e} "
          f"(exact 0 for a real input)")
    print(f"Nyquist bin imaginary part: {X[n // 2].imag:.1e} (exact 0)")
    print(f"conjugate symmetry: max|X[k] - conj(X[N-k])| for k = 1..N-1 = "
          f"{np.max(np.abs(X[1:] - np.conj(X[n - 1:0:-1]))):.3e}")

    section("7. Scalloping loss of an off-bin tone")
    n = 1000
    fs = 100.0
    dt = 1.0 / fs
    df = fs / n
    t = np.arange(n) * dt
    amp = 1.0
    f0 = 200.0 * df                     # exactly bin 200 with this record
    print(f"N = {n}, fs = {fs} Hz, df = {df} Hz, on-bin frequency {f0:.4f} Hz")
    print("   offset (bins)   recovered amplitude   exact factor   loss (dB)")
    for offset in (0.0, 0.25, 0.5, 0.75):
        f = f0 + offset * df
        x = amp * np.sin(2 * np.pi * f * t)
        X = np.fft.rfft(x)
        rec = 2 * np.abs(X).max() / n
        dist = min(offset % 1.0, 1.0 - offset % 1.0)   # to the nearest bin
        exact = (abs(np.sin(np.pi * dist) / (n * np.sin(np.pi * dist / n)))
                 if dist > 0 else 1.0)
        print(f"   {offset:12.2f}   {rec:18.6f}   {exact:12.6f}   "
              f"{20 * np.log10(max(rec, 1e-12)):9.4f}")
    print(f"at a half-bin offset the exact loss factor is 2/pi = {2 / np.pi:.6f},")
    print(f"i.e. {20 * np.log10(2 / np.pi):.4f} dB: the peak amplitude is")
    print("under-reported by 36 % unless the tone is exactly on a bin. The")
    print("residual 0.08 % between the columns at 0.25 and 0.75 bins is the")
    print("negative-frequency term of the real sine, which the Dirichlet formula")
    print("for a complex exponential does not include")

    section("8. Integer-period and non-integer-period records")
    n = 1000
    fs = 100.0
    dt = 1.0 / fs
    t = np.arange(n) * dt
    for f, name in ((10.0, "exactly 100 periods (on bin)"),
                    (10.05, "not a whole number of periods (off bin)")):
        x = np.sin(2 * np.pi * f * t)
        X = np.fft.rfft(x)
        mag = np.abs(X)
        peak = int(np.argmax(mag))
        total = np.sum(mag ** 2)
        near = np.sum(mag[max(0, peak - 3):peak + 4] ** 2)
        print(f"{name}: peak bin {peak}, "
              f"fraction of the energy within +-3 bins = {near / total:.6f}")
    print("a non-integer number of periods spreads energy across the whole")
    print("spectrum (spectral leakage); this is the truncation of the record, not")
    print("an error in the transform, and it is cured by windowing")
    print("(see lesson 20-02-03) or by choosing an integer number of periods")


if __name__ == "__main__":
    main()
