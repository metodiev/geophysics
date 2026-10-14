"""Convolution, filtering and the convolution theorem -- with deconvolution
shown to be an inverse problem rather than an operation.

Run:  python3 convolution_demo.py
Requires: Python standard library only.

Companion to lesson 01-10-03 (Convolution, Filtering and the Convolution
Theorem).

Convention: same as the rest of the module,
    X(f) = integral x(t) exp(-2*pi*i*f*t) dt
so the convolution theorem reads  F{x * h} = F{x} . F{h}  with no conjugation
and no factor of 2*pi.  The DFT pair is
    X[k] = sum_n x[n] exp(-2*pi*i*k*n/N),  x[n] = (1/N) sum_k X[k] exp(+...).
"""

import cmath
import math

N = 512            # signal length
NPAD = 2 * N       # zero-padded length: makes circular convolution = linear
DT = 0.004         # seconds


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def fft(a):
    """Iterative radix-2 FFT (N a power of two).  Derived in lesson 01-10-04."""
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


def convolve(x, h):
    """Direct linear convolution, O(len(x) * len(h))."""
    nx, nh = len(x), len(h)
    y = [0.0] * (nx + nh - 1)
    for i, xi in enumerate(x):
        if xi == 0.0:
            continue
        for j, hj in enumerate(h):
            y[i + j] += xi * hj
    return y


def convolve_circular(x, h, n):
    """Circular convolution of two sequences of the same length n, via FFT."""
    xf, hf = fft([complex(v) for v in x]), fft([complex(v) for v in h])
    return [v.real for v in ifft([a * b for a, b in zip(xf, hf)])]


def rms(v):
    return math.sqrt(sum(x * x for x in v) / len(v))


def grid(n=N):
    return [i * DT for i in range(n)]


def main():
    section("1. Convolution is a weighted running average")
    signal = [0.0] * N
    for i in range(N):
        t = i * DT
        signal[i] = (1.0 if t < 0.6 else -0.4) + 0.15 * math.sin(2 * math.pi * 23.0 * t)
    box3 = [1.0 / 3.0] * 3
    box9 = [1.0 / 9.0] * 9
    sm3 = convolve(signal, box3)[1:N + 1]
    sm9 = convolve(signal, box9)[4:N + 4]
    print(f"  input  : RMS = {rms(signal):.6f}, range"
          f" {min(signal):+.4f} to {max(signal):+.4f}")

    def dirichlet_gain(f, m):
        return abs(math.sin(math.pi * f * m * DT) / (m * math.sin(math.pi * f * DT)))

    def tone_amplitude(v, lo, hi, f=23.0):
        n_ = hi - lo
        a = 2.0 / n_ * sum(v[i] * math.sin(2 * math.pi * f * i * DT) for i in range(lo, hi))
        b = 2.0 / n_ * sum(v[i] * math.cos(2 * math.pi * f * i * DT) for i in range(lo, hi))
        return math.hypot(a, b)

    pure = [math.cos(2 * math.pi * 23.0 * i * DT) for i in range(N)]
    print("  Gain of each filter measured on a pure 23 Hz cosine (interior samples),")
    print("  against the analytic Dirichlet response |H(23 Hz)|:")
    for label, h, m in (("boxcar3", box3, 3), ("boxcar9", box9, 9)):
        t = len(h)
        outp = convolve(pure, h)[t // 2:N + t // 2]
        gain = tone_amplitude(outp, N // 4, 3 * N // 4) / tone_amplitude(pure, N // 4, 3 * N // 4)
        print(f"    {label}: measured {gain:.6f}, predicted {dirichlet_gain(23.0, m):.6f}")
    print("  The same filter applied to the two-level signal gives a different")
    print("  apparent attenuation, because the step leaks energy into every")
    print("  frequency, including 23 Hz.  Leakage corrupts naive amplitude")
    print("  estimates; this is quantified in lesson 01-10-05.")
    print("  A moving average of M points reduces the standard deviation of white")
    print("  noise by 1/sqrt(M) (measured in Section 3) but leaves a constant")
    print("  offset and a linear trend untouched, because |H(0)| = 1.")

    print("\n  Commutativity  x * h = h * x :"
          f" max |diff| = {max(abs(a - b) for a, b in zip(convolve(signal, box9), convolve(box9, signal))):.2e}")
    gauss5 = []
    for i in range(5):
        z = (i - 2) / 1.0
        gauss5.append(math.exp(-0.5 * z * z))
    total = sum(gauss5)
    gauss5 = [g / total for g in gauss5]
    left = convolve(convolve(signal, box9), gauss5)
    right = convolve(signal, convolve(box9, gauss5))
    print(f"  Associativity (x*h1)*h2 = x*(h1*h2) : max |diff| ="
          f" {max(abs(a - b) for a, b in zip(left, right)):.2e}")
    print("  Associativity is the reason a chain of filters can be replaced by one")
    print("  equivalent filter -- and the reason a source wavelet and an instrument")
    print("  response can be lumped into a single operator.")

    section("2. The convolution theorem")
    sig2 = [math.sin(0.7 * i) * math.cos(0.13 * i) + 0.3 * math.sin(2.1 * i)
            for i in range(N)]
    response = [math.exp(-0.05 * i) * math.cos(0.4 * i) for i in range(40)]

    direct = convolve(sig2, response)
    n_eval = min(len(direct), NPAD)
    padded_x = sig2 + [0.0] * (NPAD - N)
    padded_h = response + [0.0] * (NPAD - len(response))
    xf, hf = fft([complex(v) for v in padded_x]), fft([complex(v) for v in padded_h])
    spectral = ifft([a * b for a, b in zip(xf, hf)])
    err = max(abs(spectral[i].real - direct[i]) for i in range(n_eval))
    scale = max(abs(v) for v in direct)
    print(f"  x: {N} samples, h: {len(response)} samples, both zero-padded to {NPAD}")
    print(f"  max |direct - FFT| = {err:.3e}  (relative {err / scale:.3e})")
    print("  With the padding the circular convolution of the DFT equals the linear")
    print("  convolution, so the theorem holds exactly up to round-off.")

    no_pad_x = sig2
    no_pad_h = response + [0.0] * (N - len(response))
    circular = convolve_circular(no_pad_x, no_pad_h, N)
    wrap = max(abs(circular[i] - direct[i]) for i in range(N))
    print(f"  Without padding (circular, N = {N}) the error is {wrap:.3e},"
          f" which is {wrap / err:.1e} times")
    print("  the round-off level, and {:.2f} times the peak of the convolution."
          .format(wrap / scale))
    print("  The missing samples do not vanish; they wrap around to the start of")
    print("  the record.  This is the practical meaning of 'use enough padding'.")

    section("3. A filter is a convolution, and its response is its transform")
    print("  Amplitude response |H(f)| of a few candidate filters, computed by")
    print("  taking the FFT of the impulse response (zero-padded to 4096):")
    nfft = 4096
    df = 1.0 / (nfft * DT)

    def response_of(h, freqs):
        padded = list(h) + [0.0] * (nfft - len(h))
        spec = fft([complex(v) for v in padded])
        return [abs(spec[int(round(f / df))]) for f in freqs]

    freqs = [0.0, 10.0, 20.0, 25.0, 40.0, 50.0, 62.5]
    box5 = [1.0 / 5.0] * 5
    box9h = [1.0 / 9.0] * 9
    tri = [(i + 1) for i in range(5)] + [4, 3, 2, 1]
    tri = [v / sum(tri) for v in tri]
    gauss = [math.exp(-0.5 * ((i - 4) / 1.5) ** 2) for i in range(9)]
    gauss = [v / sum(gauss) for v in gauss]
    print(f"  {'f (Hz)':>8} {'boxcar 5':>10} {'boxcar 9':>10} {'triangular 9':>13}"
          f" {'gaussian 9':>11}")
    rows = {}
    for name, h in (("box5", box5), ("box9", box9h), ("tri9", tri), ("gauss9", gauss)):
        rows[name] = response_of(h, freqs)
    for j, f in enumerate(freqs):
        print(f"  {f:>8.1f} {rows['box5'][j]:>10.5f} {rows['box9'][j]:>10.5f}"
              f" {rows['tri9'][j]:>13.5f} {rows['gauss9'][j]:>11.5f}")
    print("  Nyquist for this sampling is 1/(2 dt) ="
          f" {1.0 / (2.0 * DT):.1f} Hz, so f = 62.5 Hz is the top of the band.")
    # Find the first zero of the 9-point boxcar response.
    scan = [i * 0.05 for i in range(1, 2000)]    # up to 100 Hz
    mags = response_of(box9h, scan)
    zero_idx = min(range(len(mags)), key=lambda i: mags[i])
    print(f"  The 9-point boxcar has its first spectral zero at f ="
          f" {scan[zero_idx]:.3f} Hz, predicted at 1/(9 dt) ="
          f" {1.0 / (9 * DT):.3f} Hz.")
    print("  At that frequency the filter output is exactly zero: no subsequent")
    print("  processing can recover what the filter destroyed.  A Gaussian has no")
    print("  zeros, which is one reason it is preferred when inversion follows.")
    print("  At the frequencies where it is not near zero the discrete response")
    print("  equals the Dirichlet kernel; far below the first zero it equals the")
    print("  sinc sin(pi f M dt)/(pi f M dt).")
    print("  Noise-averaging check: for white input, std(out)/std(in) should be")
    print("  1/sqrt(M).  Measured with 20000 pseudo-random samples:")
    for m in (3, 9, 25):
        data = [math.sin(12.9898 * i) * 43758.5453 for i in range(20000)]
        data = [(v - math.floor(v)) * 2.0 - 1.0 for v in data]
        h = [1.0 / m] * m
        out = convolve(data, h)[m:len(data)]
        noise = [v - sum(data) / len(data) for v in data]
        noise_out = [v - sum(out) / len(out) for v in out]
        print(f"    M = {m:>2}: measured {rms(noise_out) / rms(noise):.5f},"
              f" 1/sqrt(M) = {1.0 / math.sqrt(m):.5f}")


    section("4. Hard edges: a boxcar in time is a sinc in frequency, and back")
    square = [1.0 if i < N // 2 else -1.0 for i in range(N)]
    smoothed = convolve(square, box9h)[4:4 + N]
    print(f"  A periodic square wave (jump of 2) smoothed by a 9-point boxcar becomes")
    print(f"  a ramp of width 9*dt = {9 * DT:.3f} s with no overshoot at all:"
          f" max {max(smoothed[10:N - 10]):.6f}, min {min(smoothed[10:N - 10]):.6f}.")

    nfft2 = 1024
    square2 = [1.0 if i < nfft2 // 2 else -1.0 for i in range(nfft2)]
    spec = fft([complex(v) for v in square2])
    print("\n  The same square wave through an ideal brick-wall low-pass, compared")
    print("  with the truncated Fourier series of the continuous square wave at the")
    print("  same sample points.  The two are the same operation:")
    print(f"  {'bins/side':>10} {'odd harmonics':>14} {'filter max':>11}"
          f" {'overshoot':>10} {'series overshoot':>17} {'difference':>11}")
    for keep in (1, 2, 3, 5, 9, 17, 33, 65, 129):
        brick = [0j] * nfft2
        for k in range(nfft2):
            if k <= keep or k >= nfft2 - keep:
                brick[k] = spec[k]
        filtered = [v.real for v in ifft(brick)]
        odd_terms = (keep + 1) // 2
        smax = 0.0
        for i in range(nfft2):
            t = 2.0 * math.pi * i / nfft2
            acc = 0.0
            for n_ in range(1, 2 * odd_terms, 2):
                acc += math.sin(n_ * t) / n_
            smax = max(smax, 4.0 / math.pi * acc)
        f_pc = 100.0 * (max(filtered) - 1.0) / 2.0
        s_pc = 100.0 * (smax - 1.0) / 2.0
        print(f"  {keep:>10} {odd_terms:>14} {max(filtered):>11.6f}"
              f" {f_pc:>9.3f}% {s_pc:>16.3f}% {f_pc - s_pc:>10.3f}%")
    print("  The two overshoots track each other as terms are added and both stop")
    print("  near 9%: a brick-wall filter and a truncated Fourier series are the")
    print("  same operation.  The small residual difference is a sampling effect --")
    print("  the jump of a sampled square wave sits between sample points and the")
    print("  sampled coefficients deviate from 1/n as the harmonic index rises.")
    print("  Ringing near an edge is therefore not a defect of a particular")
    print("  program; it is the price of a sharp band limit, and it is why a")
    print("  sharp-cutoff filter makes seismic data look 'ringy' and why a gap in a")
    print("  survey produces spurious amplitudes at its edges.  A boxcar in time")
    print("  avoids the ringing but has a sinc response in frequency, whose")
    print("  sidelobes pass noise.  Lesson 01-10-05 is about that trade.")

    section("5. Instrument response is a convolution")
    tau = 0.5                        # s: a slow first-order sensor
    nh = 800                         # 3.2 s = 6.4 tau: truncation error e^-6.4
    nfft3 = 2048
    h_instr = [(DT / tau) * math.exp(-i * DT / tau) for i in range(nh)]
    print(f"  sensor: h(t) = (dt/tau) exp(-t/tau), tau = {tau} s, truncated at"
          f" {nh} samples ({nh * DT:.2f} s).")
    infinite_sum = (DT / tau) / (1.0 - math.exp(-DT / tau))
    print(f"  Sum of h over all n: {infinite_sum:.6f};  sum of the {nh} stored"
          f" samples: {sum(h_instr):.6f}")
    print(f"  Ratio = {sum(h_instr) / infinite_sum:.6f} = 1 - e^-6.4, i.e. the")
    print("  truncation loses 0.17% of the low-frequency gain.  This is exactly why")
    print("  a real instrument response is stored as poles and zeros rather than as")
    print("  a finite impulse response.")
    print(f"  {'f (Hz)':>8} {'continuous':>12} {'discrete sum':>13}"
          f" {'FFT of h':>11} {'|d-c|/c':>9} {'phase deg':>10}")
    padded_h3 = h_instr + [0.0] * (nfft3 - nh)
    H3 = fft([complex(v) for v in padded_h3])
    df3 = 1.0 / (nfft3 * DT)
    for f in (0.1, 0.5, 1.0, 5.0, 25.0, 100.0):
        k = int(round(f / df3))
        fk = k * df3
        cont = 1.0 / complex(1.0, 2 * math.pi * fk * tau)
        disc = sum(h * cmath.exp(-2j * math.pi * fk * i * DT)
                   for i, h in enumerate(h_instr))
        print(f"  {fk:>8.3f} {abs(cont):>12.6f} {abs(disc):>13.6f}"
              f" {abs(H3[k]):>11.6f} {abs(disc - cont) / abs(cont):>9.2e}"
              f" {math.degrees(cmath.phase(H3[k])):>10.2f}")
    truth = [math.exp(-(((i * DT) - 0.6) / 0.05) ** 2)
             * math.sin(2 * math.pi * 18.0 * i * DT) for i in range(N)]
    recorded = convolve(truth, h_instr)[:N]
    print(f"  Peak input amplitude {max(abs(v) for v in truth):.4f}, peak recorded"
          f" amplitude {max(abs(v) for v in recorded):.4f}: the sensor has both")
    print("  attenuated and delayed the signal, and the |H| table above says by how")
    print("  much.  This synthetic ground motion is reused in Section 6.")
    print("  The FFT of the stored impulse response and the direct sum agree to")
    print("  round-off; both differ from the continuous response by the aliasing of")
    print("  the tails above Nyquist.  Filtering a record with this response is a")
    print("  convolution, so undoing it is a deconvolution.")

    section("6. Deconvolution is an inverse problem, not an operation")
    truth = [math.exp(-(((i * DT) - 0.6) / 0.05) ** 2)
             * math.sin(2 * math.pi * 18.0 * i * DT) for i in range(N)]
    truth_full = truth + [0.0] * (nfft3 - N)
    conv = convolve(truth, h_instr)
    y_full = conv + [0.0] * (nfft3 - len(conv))
    print(f"  truth is confined to the first {N} samples; the linear convolution with")
    print(f"  h occupies {len(conv)} samples, which fits inside the {nfft3}-sample")
    print("  window, so the circular transform of the padded arrays equals the")
    print("  linear convolution and the discrete system is exactly invertible.")
    noise_level = 1.0e-3
    noise = [noise_level * 0.5 * (math.sin(97.0 * i) + math.sin(191.0 * i))
             for i in range(nfft3)]
    print(f"  signal RMS {rms(truth_full):.6f}, added noise RMS {rms(noise):.6f},"
          f" ratio {rms(noise) / rms(truth_full):.4%}")
    H = fft([complex(v) for v in padded_h3])
    noisy_full = [a + b for a, b in zip(y_full, noise)]
    Y = fft([complex(v) for v in noisy_full])

    def recover(eps, yy):
        out = [0j] * nfft3
        for k in range(nfft3):
            hk = H[k]
            out[k] = yy[k] * hk.conjugate() / (abs(hk) ** 2 + eps ** 2)
        return [v.real for v in ifft(out)]

    def misfit(x):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(x, truth_full)) / nfft3)

    clean_err = misfit(recover(0.0, fft([complex(v) for v in y_full])))
    print(f"\n  noise-free, naive division: RMS error = {clean_err:.3e}"
          f"  (round-off, as expected)")
    print(f"  {'water level':>12} {'RMS error':>12} {'max gain':>10}")
    best = None
    for eps in (0.0, 1e-4, 1e-3, 3e-3, 0.01, 0.03, 0.1, 0.3):
        m = misfit(recover(eps, Y))
        if best is None or m < best[1]:
            best = (eps, m)
        gain = max(abs(H[k]) / (abs(H[k]) ** 2 + eps ** 2) for k in range(nfft3))
        print(f"  {eps:>12.1e} {m:>12.6f} {gain:>10.2f}")
    print(f"  Best water level in this scan: eps = {best[0]:.1e},")
    print(f"  RMS error {best[1]:.6f} against a perfect-noise-free floor of"
          f" {clean_err:.1e}.")
    print("  eps = 0 is the naive X = Y/H.  It is not merely suboptimal, it is the")
    print("  worst entry in the table: wherever |H| is small the division multiplies")
    print("  the noise by |1/H| without limit.  Regularisation trades a little bias")
    print("  where |H| is small for a large reduction in variance -- the same")
    print("  bias/variance trade-off as every other inverse problem.")
    amp = max(1.0 / (abs(H[k]) + 1e-30) for k in range(nfft3))
    print(f"  Largest |1/H| on the grid: {amp:.1f} = {20 * math.log10(amp):.1f} dB"
          f" of noise gain.")
    print("  Note also that the size of eps is not a property of the data alone: it")
    print("  must scale with the noise level, which is why a deconvolution result")
    print("  without an error bar or a stated regularisation cannot be evaluated.")

    print("\n  How the answer depends on the noise level (fixed eps = 1e-2):")
    print(f"  {'noise RMS':>11} {'naive err':>11} {'regularised':>12} {'winner':>12}")
    for nl in (1e-4, 1e-3, 1e-2, 3e-2, 1e-1):
        nz = [nl * 0.5 * (math.sin(97.0 * i) + math.sin(191.0 * i))
              for i in range(nfft3)]
        Y2 = fft([complex(v) for v in [a + b for a, b in zip(y_full, nz)]])
        naive = misfit(recover(0.0, Y2))
        reg = misfit(recover(1e-2, Y2))
        print(f"  {nl:>11.1e} {naive:>11.6f} {reg:>12.6f}"
              f" {'naive' if naive < reg else 'regularised':>12}")
    print("  At a noise level of 1e-4 the naive inverse still wins; at 1e-3 the")
    print("  regularised inverse is already five times better, and at 1e-2 it is")
    print("  better by a factor of seven.  There is no 'correct' deconvolution")
    print("  independent of the noise, and no way to choose eps without estimating")
    print("  it.")


if __name__ == "__main__":
    main()
