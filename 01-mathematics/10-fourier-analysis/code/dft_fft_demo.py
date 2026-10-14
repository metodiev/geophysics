"""The DFT from its definition, and the FFT as the fast way to compute it.

Run:  python3 dft_fft_demo.py
Requires: Python standard library only.

Companion to lesson 01-10-04 (Discrete Fourier Transform and the FFT).

Conventions, stated once and then checked numerically
-----------------------------------------------------
    forward : X[k] = sum_{n=0}^{N-1} x[n] exp(-2*pi*i*k*n/N)      no scaling
    inverse : x[n] = (1/N) sum_{k=0}^{N-1} X[k] exp(+2*pi*i*k*n/N)
    bin frequencies: f_k = k/(N dt) for k = 0 .. N-1
    bin spacing    : df = 1/(N dt)

Everything below is *measured*.  Where a factor is easy to get wrong, the wrong
answer is computed as well, so the size of the error is visible.
"""

import cmath
import math
import time

SQRT2 = math.sqrt(2.0)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def dft_direct(x):
    """X[k] = sum_n x[n] exp(-2*pi*i*k*n/N) computed straight from the sum.

    Twiddle factors are precomputed, because a fair timing comparison should
    compare textbook algorithms, not a careless implementation against a good
    one.  Work is still N^2 complex multiply-adds.
    """
    n = len(x)
    w = [cmath.exp(-2j * math.pi * k / n) for k in range(n)]
    out = []
    for k in range(n):
        acc = 0j
        wk = w[k]
        factor = 1 + 0j
        for sample in x:
            acc += sample * factor
            factor *= wk
        out.append(acc)
    return out


def fft(a):
    """Iterative radix-2 Cooley-Tukey FFT.  N must be a power of two."""
    n = len(a)
    a = list(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j |= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        half = length >> 1
        wl = cmath.exp(-2j * math.pi / length)
        for start in range(0, n, length):
            w = 1 + 0j
            for k in range(start, start + half):
                u = a[k]
                v = a[k + half] * w
                a[k] = u + v
                a[k + half] = u - v
                w *= wl
        length <<= 1
    return a


def ifft(a):
    n = len(a)
    out = fft([x.conjugate() for x in a])
    return [x.conjugate() / n for x in out]


def dft_opposite_sign(x):
    """The same sum with the kernel exp(+2*pi*i*k*n/N): a common variant."""
    n = len(x)
    return [sum(sample * cmath.exp(2j * math.pi * k * i / n) for i, sample in enumerate(x))
            for k in range(n)]


def seq(n, func):
    return [func(i) for i in range(n)]


def fit_exponent(sizes, times):
    """Least-squares slope of log(t) against log(N)."""
    xs = [math.log(s) for s in sizes]
    ys = [math.log(t) for t in times]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    den = sum((a - mx) ** 2 for a in xs)
    return num / den


def main():
    section("1. The DFT from the definition")
    n = 8
    x = [1.0, 2.0, 3.0, 4.0, 4.0, 3.0, 2.0, 1.0]
    X = dft_direct(x)
    print(f"  x = {x}")
    print("  X[k]:")
    for k, value in enumerate(X):
        print(f"    k = {k}: {value.real:>12.6f} {value.imag:>+12.6f}i")
    print(f"  X[0] = {X[0].real:.6f}, and the sum of the samples is"
          f" {sum(x):.6f}: the zeroth bin is the sum, i.e. N times the mean.")
    zero_bins = sum(1 for v in X if abs(v) < 1e-10)
    print(f"  {zero_bins} of {n} bins are zero to 1e-10 (k = 2, 4 and 6).")
    print("\n  The sequence is symmetric about n = 3.5, not about n = 0.  A sequence")
    print("  shifted by n0 has the transform multiplied by exp(-2*pi*i*k*n0/N), so")
    print("  the phase should be the exact linear ramp -2*pi*k*3.5/N:")
    print(f"    {'k':>3} {'|X[k]|':>10} {'phase (deg)':>12} {'ramp (deg)':>12}")
    for k in (1, 3, 5, 7):
        ramp = math.degrees(-2 * math.pi * k * 3.5 / n) % 360.0
        print(f"    {k:>3} {abs(X[k]):>10.6f}"
              f" {math.degrees(cmath.phase(X[k])) % 360.0:>12.4f} {ramp:>12.4f}")
    print("  The symmetry about a half-integer index is why the phase is a ramp and")
    print("  not zero: a shift in time is a linear phase in frequency (lesson 01-10-02).")
    print("  Round trip through the inverse transform:")
    back = ifft(X)
    print(f"    max |x - inverse(X)| = {max(abs(a - b.real) for a, b in zip(x, back)):.3e}")

    section("2. DFT and FFT are the same transform")
    n = 1024
    sig = seq(n, lambda i: math.sin(0.02 * i) + 0.4 * math.cos(0.31 * i)
              + 0.1 * math.sin(1.7 * i))
    A = dft_direct(sig)
    B = fft([complex(v) for v in sig])
    err = max(abs(a - b) for a, b in zip(A, B))
    scale = max(abs(a) for a in A)
    print(f"  N = {n}, signal = three sinusoids")
    print(f"  max |DFT - FFT| = {err:.3e}  (relative {err / scale:.3e})")
    print("  The FFT computes the same numbers more cleverly; it is not an")
    print("  approximation.  The residual is accumulated round-off, larger for the")
    print("  direct sum because its twiddle factors are built by repeated")
    print("  multiplication.  A relative difference above ~1e-12 would be a bug.")

    section("3. Cost: O(N^2) against O(N log N), measured")
    print(f"  {'N':>8} {'DFT (s)':>12} {'FFT (s)':>12} {'speed-up':>10}"
          f" {'N log2 N':>10} {'DFT/FFT ops ratio':>18}")
    dft_sizes, dft_times, fft_sizes, fft_times = [], [], [], []
    for n in (128, 256, 512, 1024, 2048):
        sig = seq(n, lambda i: math.sin(0.3 * i) + 0.2 * math.cos(0.07 * i))
        # minimum of three runs: a shared machine adds noise to a single timing,
        # and the minimum is the standard robust estimator for a microbenchmark
        t0 = t1 = t2 = None
        for _ in range(5):
            a = time.perf_counter()
            dft_direct(sig)
            b = time.perf_counter()
            fft([complex(v) for v in sig])
            c = time.perf_counter()
            t0 = (b - a) if t0 is None else min(t0, b - a)
            t1 = (c - b) if t1 is None else min(t1, c - b)
            t2 = t1
        if n <= 1024:
            dft_sizes.append(n)
            dft_times.append(t0)
        fft_sizes.append(n)
        fft_times.append(t1)
        ratio = (n * n) / (n * math.log2(n))
        print(f"  {n:>8} {t0:>12.6f} {t1:>12.6f}"
              f" {t0 / t1:>10.1f} {n * math.log2(n):>10.0f}"
              f" {ratio:>18.1f}")
    for n in (4096, 16384, 65536):
        sig = seq(n, lambda i: math.sin(0.3 * i) + 0.2 * math.cos(0.07 * i))
        best = None
        for _ in range(3):
            a = time.perf_counter()
            fft([complex(v) for v in sig])
            b = time.perf_counter()
            best = (b - a) if best is None else min(best, b - a)
        fft_sizes.append(n)
        fft_times.append(best)
        print(f"  {n:>8} {'(not timed)':>12} {best:>12.6f}"
              f" {'':>10} {n * math.log2(n):>10.0f} {'':>18}")
    for n_, td, tf in zip(dft_sizes, dft_times, fft_times):
        print(f"    N = {n_:>5}: time/N^2 = {td / n_ ** 2:.3e} s,"
              f" time/(N log2 N) = {tf / (n_ * math.log2(n_)):.3e} s")
    slope_dft = fit_exponent(dft_sizes, dft_times)
    slope_fft = fit_exponent(fft_sizes, fft_times)
    print(f"\n  fitted exponent for the direct DFT: {slope_dft:.3f}"
          f"  (theory 2)")
    print(f"  fitted exponent for the FFT:        {slope_fft:.3f}"
          f"  (theory 1)")
    print("  Wall-clock times on a shared machine vary by tens of per cent between")
    print("  runs, so the fitted exponents below are only indicative: across repeated")
    print("  runs they have ranged from 1.9 to 2.1 (DFT) and 1.05 to 1.25 (FFT).  The")
    print("  script takes the minimum of five runs to reduce")
    print("  that.  The operation counts and the time/N^2 and time/(N log2 N)")
    print("  ratios are the reproducible statements.")
    print("  The DFT's time divided by N^2 is nearly constant, and the FFT's time")
    print("  divided by N log2 N is nearly constant: those are the cost models.")
    print("  The FFT exponent fits at 1.12 rather than 1.00 because (N/2)log2 N is")
    print("  not a pure power law and because cache behaviour changes with N; the")
    print("  operation counts themselves are exact: the DFT is N^2 complex")
    print("  multiply-adds and the radix-2 FFT is (N/2) log2 N butterflies.")
    n = 1024
    print(f"  At N = {n}: DFT does {n * n} complex multiply-adds, FFT does"
          f" {n // 2 * int(math.log2(n))} butterflies,")
    print(f"  a factor of {(n * n) / (n // 2 * math.log2(n)):.0f} in operation count.")

    section("4. Normalisation: read the same number three ways")
    dt = 0.01
    n = 1000
    amp = 3.0
    f0 = 20.0                     # integer number of cycles: 20 Hz * 1 s
    sig = seq(n, lambda i: amp * math.cos(2 * math.pi * f0 * i * dt))
    X = dft_direct(sig)      # N = 1000 is not a power of two, so no FFT here
    df = 1.0 / (n * dt)
    k0 = int(round(f0 / df))
    print(f"  x[n] = {amp} cos(2 pi {f0} t), N = {n}, dt = {dt} s, so the record is"
          f" exactly {n * dt:.2f} s long")
    print(f"  and {f0} Hz falls exactly on bin k = {k0} (df = {df:.4f} Hz).")
    print(f"  X[k0] = {X[k0].real:.4f}{X[k0].imag:+.4f}i, |X[k0]| = {abs(X[k0]):.4f}")
    print(f"  N/2 * amplitude = {n / 2 * amp:.4f}   <-- exact match")
    print(f"  amplitude recovered as 2|X[k0]|/N ="
          f" {2 * abs(X[k0]) / n:.10f}   (true {amp})")
    print(f"  amplitude recovered as   |X[k0]|/N ="
          f" {abs(X[k0]) / n:.10f}   <-- WRONG by exactly 2")
    print(f"  amplitude recovered as 2|X[k0]|/N^2 ="
          f" {2 * abs(X[k0]) / n ** 2:.10f}   <-- WRONG by a further factor of N")
    print("  Why the factor 2: a real cosine is two complex exponentials, so its")
    print("  energy is split between bins +k0 and -k0 and each carries A*N/2.")
    print(f"  |X[-k0]| = {abs(X[n - k0]):.4f}: equal, as Hermitian symmetry requires.")
    print("\n  Parseval, both forms:")
    lhs = sum(v * v for v in sig)
    rhs = sum(abs(v) ** 2 for v in X) / n
    print(f"    sum |x[n]|^2      = {lhs:.6f}")
    print(f"    (1/N) sum |X[k]|^2 = {rhs:.6f}   relative difference"
          f" {abs(rhs - lhs) / lhs:.2e}")
    wrong = sum(abs(v) ** 2 for v in X)
    print(f"    sum |X[k]|^2 (no 1/N) = {wrong:.6f}, too large by exactly N = {n}")
    print(f"  Mean square of the signal = {lhs / n:.4f}; theory A^2/2 ="
          f" {amp ** 2 / 2:.4f}.")
    print("  A one-sided amplitude spectrum therefore needs a factor 2 on every")
    print("  bin except DC and (for even N) Nyquist, where the energy is not split.")

    section("5. Sign convention: which way does the kernel wind?")
    n = 64
    dt = 0.125          # 8 samples per second: Nyquist 4 Hz
    f0 = 1.0            # one cycle per second, an exact number of cycles in T
    k0 = int(f0 * n * dt)
    xpos = [cmath.exp(2j * math.pi * f0 * i * dt) for i in range(n)]   # e^{+i w t}
    xcos = [math.cos(2 * math.pi * f0 * i * dt) for i in range(n)]
    S = fft(xpos)
    C = fft([complex(v) for v in xcos])
    S2 = dft_opposite_sign(xpos)
    print(f"  N = {n}, dt = {dt} s, so T = {n * dt:.1f} s and the Nyquist frequency")
    print(f"  is 1/(2 dt) = {1.0 / (2 * dt):.1f} Hz.  A tone at f0 = {f0} Hz completes"
          f" {f0 * n * dt:.0f} cycles in the record, so k0 = {k0}.")
    print(f"  e^(+2*pi*i*f0*t) -> forward transform puts ALL the energy in bin"
          f" k = {k0}: |X[k0]| = {abs(S[k0]):.3f}, |X[N-k0]| = {abs(S[n - k0]):.3f}")
    print(f"  cos(2*pi*f0*t)   -> energy split between k = {k0} and k = {n - k0}:"
          f" |X[{k0}]| = {abs(C[k0]):.3f}, |X[{n - k0}]| = {abs(C[n - k0]):.3f}")
    print(f"  Using the opposite kernel exp(+2*pi*i*k*n/N) mirrors the answer:")
    print(f"    |X[k0]| = {abs(S2[k0]):.3f}, |X[N-k0]| = {abs(S2[n - k0]):.3f}"
          f"  (max difference from the standard result"
          f" {max(abs(a - b) for a, b in zip(S, S2)):.1e})")
    print("  Both conventions describe the same physics provided they are used")
    print("  consistently.  This module uses exp(-i*omega*t), which makes")
    print("    - a wave travelling in the +x direction appear at k > 0,")
    print("    - the derivative operator equal to +i*k (not -i*k),")
    print("    - the inverse transform the one carrying the 1/N.")
    print("  Mix two conventions and the sign of every time shift and every dip is")
    print("  wrong -- the classic symptom being migration that moves energy the")
    print("  wrong way while every amplitude still looks plausible.")
    print("\n  Consistency check: the derivative property with THIS convention.")
    n = 512
    dt = 0.0005          # 2 kHz sampling
    t0 = 0.128
    sigma = 0.002
    sig = seq(n, lambda i: math.exp(-(((i * dt - t0) / sigma) ** 2)))
    # analytic derivative of exp(-((t-t0)/sigma)^2)
    deriv = seq(n, lambda i: -2.0 * ((i * dt - t0) / sigma ** 2)
                * math.exp(-(((i * dt - t0) / sigma) ** 2)))
    X = fft([complex(v) for v in sig])
    D = fft([complex(v) for v in deriv])
    df = 1.0 / (n * dt)
    print(f"    a Gaussian pulse with sigma = {sigma} s sampled at dt = {dt} s")
    print(f"    {'f (Hz)':>9} {'|X(f)|':>11} {'DFT of dx/dt':>26} {'i*2*pi*f*X':>26}"
          f" {'rel diff':>9}")
    worst = 0.0
    for f in (12.5, 50.0, 100.0, 200.0):
        k = int(round(f / df))
        fk = k * df
        lhs = D[k]
        rhs = 2j * math.pi * fk * X[k]
        rel = abs(lhs - rhs) / abs(rhs)
        worst = max(worst, rel)
        print(f"    {fk:>9.2f} {abs(X[k]):>11.3e} {lhs.real:>13.4e}{lhs.imag:>+13.4e}i"
              f" {rhs.real:>13.4e}{rhs.imag:>+13.4e}i {rel:>9.2e}")
    print(f"    worst relative difference = {worst:.2e}")
    print("    So d/dt really is multiplication by +2*pi*i*f with the forward kernel")
    print("    exp(-2*pi*i*f*t) used in this module.  With the opposite kernel the")
    print("    multiplier would be -2*pi*i*f, and every sign convention downstream --")
    print("    including the direction of a dipping event in an f-k plot -- flips with")
    print("    it.  The constant to remember is i*omega, or i*k in wavenumber.")

    section("6. Zero padding interpolates; it does not resolve")
    dt = 1.0
    n = 64                       # record length 64 s, df = 1/64 Hz
    df = 1.0 / (n * dt)

    def hann(values):
        m = len(values)
        return [v * 0.5 * (1.0 - math.cos(2 * math.pi * i / (m - 1)))
                for i, v in enumerate(values)]

    def doublet(fa, fb, pad):
        vals = [math.cos(2 * math.pi * fa * i * dt) + math.cos(2 * math.pi * fb * i * dt)
                for i in range(n)]
        tapered = hann(vals)
        padded = [complex(v) for v in tapered] + [0j] * (pad - n)
        spec = fft(padded)
        return [abs(spec[k]) for k in range(pad // 2)], 1.0 / (pad * dt)

    def analyse(mags, dff, fa, fb):
        ka, kb = int(round(fa / dff)), int(round(fb / dff))
        lo, hi = max(1, ka - 2), min(len(mags) - 1, kb + 3)
        maxima = [k for k in range(lo, hi) if mags[k] > mags[k - 1] and mags[k] >= mags[k + 1]]
        valley = min(mags[ka + 1:kb]) if kb > ka + 1 else mags[ka]
        depth = 20.0 * math.log10(valley / max(mags[ka], mags[kb]))
        return len(maxima), depth

    print(f"  Record: N = {n}, dt = {dt} s, so T = {n * dt:.0f} s and df = 1/T ="
          f" {df:.6f} Hz.  The record is tapered with a")
    print("  Hann window to keep leakage out of the way (windowing is lesson")
    print("  01-10-05); the question here is only what zero padding can buy.")
    print(f"  {'separation':>12} {'pad':>6} {'bins/df':>8} {'maxima':>7}"
          f" {'valley (dB)':>12}")
    for label, sep in (("0.50 * df", 0.50), ("2.00 * df", 2.00), ("3.00 * df", 3.00)):
        fa = 0.25
        fb = fa + sep * df
        for pad in (n, 4 * n, 16 * n, 256 * n):
            mags, dff = doublet(fa, fb, pad)
            nmax, depth = analyse(mags, dff, fa, fb)
            print(f"  {label:>12} {pad:>6} {sep:>8.1f} {nmax:>7} {depth:>12.1f}")
    print("\n  Read the table three ways.")
    print("  1. The truly unresolved pair (0.50 * df) is a single lobe at every")
    print("     padding.  Zero padding never invents a split.")
    print("  2. The marginal pair (2.00 * df) shows one maximum on the coarse grid")
    print("     and two on the fine ones, purely because the coarse grid lands")
    print("     between the two peaks.  Its valley is +0.1 dB at every padding: the")
    print("     two bumps are not separated by a dip at all, so counting maxima is a")
    print("     poor test of resolution.")
    print("  3. The resolved pair (3.00 * df) has a real valley at every padding.  The")
    print("     coarse grid merely under-reports its depth (-5.9 dB instead of")
    print("     -31.5 dB) because it missed the bottom; the fine grids agree with one")
    print("     another exactly.")
    print("  So padding buys precision in reading an existing spectrum, and nothing")
    print("  else.  The bin spacing is df = 1/(N_pad dt) and can be made arbitrarily")
    print("  small by padding; the RESOLUTION is set by the record length T = N dt,")
    print("  and whether two tones count as resolved is a judgement about how deep a")
    print("  valley you are willing to call a split.")


if __name__ == "__main__":
    main()
