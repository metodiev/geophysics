"""The z-transform and discrete linear systems, measured.

Run:  python3 ztransform_demo.py
Requires: Python standard library only (``cmath``, ``math``).

Companion to lesson 01-11-05 (The z-Transform and Discrete Linear Systems).

Sections
--------
1. X(z) = sum x[n] z^-n as a convergent series, against the closed form.
2. The unit circle is the DFT: X(e^{i omega}) equals the discrete transform of
   the same finite record.
3. Difference equation -> transfer function -> impulse response, verified by
   running the recursion and by convolving.
4. Poles in the z plane: radius sets the decay rate, argument sets the
   frequency; stability is |pole| < 1, measured both ways.
5. A two-pole resonator and the exact location of its amplitude peak, which is
   *not* at the pole angle.
6. The convolution theorem for discrete linear systems, plus the factor-of-N
   and circular-versus-linear traps.
7. The s-plane to z-plane map, z = e^{sT}, and the frequency warping of the
   bilinear transform.
"""

import cmath
import math


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def dft(values):
    """Direct O(N^2) discrete transform: X[k] = sum_n x[n] exp(-2 pi i k n / N)."""
    n = len(values)
    out = []
    for k in range(n):
        acc = 0j
        for j, x in enumerate(values):
            acc += x * cmath.exp(-2j * math.pi * k * j / n)
        out.append(acc)
    return out


def idft(values):
    """Inverse of ``dft`` for any length, by conjugation."""
    n = len(values)
    conj = [v.conjugate() for v in values]
    return [v.conjugate() / n for v in dft(conj)]


def fft(a):
    """Iterative radix-2 Cooley-Tukey FFT (N a power of two)."""
    n = len(a)
    a = [complex(v) for v in a]
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


def z_sum(x, z, n_max=None):
    """sum_{n=0}^{n_max} x[n] z^-n, the z-transform of a finite section."""
    total = 0j
    limit = len(x) if n_max is None else min(n_max, len(x))
    zinv = 1.0 / z
    power = 1.0
    for n in range(limit):
        total += x[n] * power
        power *= zinv
    return total


def apply_filter(b, a, x):
    """Run y[n] = sum b[k] x[n-k] - sum_{k>=1} a[k] y[n-k]."""
    y = [0j] * len(x)
    for n in range(len(x)):
        acc = 0j
        for k, bk in enumerate(b):
            if n - k >= 0:
                acc += bk * x[n - k]
        for k in range(1, len(a)):
            if n - k >= 0:
                acc -= a[k] * y[n - k]
        y[n] = acc
    return y


def main():
    section("1. The z-transform as a sum, against the closed form")
    a = 0.85
    n_max = 200
    geom = [a ** n for n in range(n_max)]
    print(f"  x[n] = a^n with a = {a};  X(z) = 1/(1 - a z^-1) for |z| > |a|")
    print(f"  {'z':>16} {'|z|':>8} {'sum to n=199':>34} {'closed form':>34}"
          f" {'error':>9}")
    for z in (2 + 0j, 1.3 + 0.7j, -1.5 + 1.5j, 1.2 - 0.9j):
        num = z_sum(geom, z)
        closed = 1.0 / (1.0 - a / z)
        print(f"  {z.real:>8.3f}{z.imag:>+7.3f}i {abs(z):>8.4f}"
              f" {num.real:>17.12f}{num.imag:>+16.12f}i"
              f" {closed.real:>17.12f}{closed.imag:>+16.12f}i"
              f" {abs(num - closed):>9.2e}")
    print("  Truncating at n = 199 leaves a residual of order |a/z|^200 = 1e-48")
    print("  at the z used above, so the measured error is pure round-off.")
    print("  Inside the radius of convergence the series diverges.  At z = 0.5,")
    bad = z_sum([a ** n for n in range(60)], 0.5)
    print(f"    a/0.5 = {a / 0.5:.2f} > 1, so each term grows by that factor and")
    print(f"    the partial sum to n = 59 is already {bad.real:.4e}.")
    print("    The closed form is not a valid representation of the series")
    print("    there: the region of convergence is part of the transform, not a")
    print("    technicality.")

    section("2. The unit circle is the DFT")
    b, aa = [0.5, 0.5], [1.0, -0.9]
    print("  H(z) = (0.5 + 0.5 z^-1)/(1 - 0.9 z^-1)")
    for n in (64, 1024):
        x = [1.0] + [0.0] * (n - 1)
        h = apply_filter(b, aa, x)
        spec = fft(h)
        worst = 0.0
        for k in range(n):
            z = cmath.exp(1j * 2 * math.pi * k / n)
            worst = max(worst, abs(spec[k] - (0.5 + 0.5 / z) / (1 - 0.9 / z)))
        print(f"  n = {n:>4}: worst |DFT[k] - H(e^(i omega_k))| = {worst:.3e}"
              f"   (tail of h at n = {n - 1}: {abs(h[-1]):.3e})")
    n = 64
    h = apply_filter(b, aa, [1.0] + [0.0] * (n - 1))
    spec = fft(h)
    print(f"  {'k':>4} {'omega (rad)':>12} {'DFT of h':>34}"
          f" {'H(e^{i omega})':>34}")
    for k in (0, 4, 8, 16, 24, 32):
        omega = 2 * math.pi * k / n
        z = cmath.exp(1j * omega)
        closed = (0.5 + 0.5 / z) / (1 - 0.9 / z)
        print(f"  {k:>4} {omega:>12.6f} {spec[k].real:>17.9f}{spec[k].imag:>+16.9f}i"
              f" {closed.real:>17.9f}{closed.imag:>+16.9f}i")
    print("  The DFT of a finite record *is* the z-transform evaluated at the")
    print("  N-th roots of unity; there is no new transform, only N samples of")
    print("  the old one.  The 64-sample column is off by about 1e-2 because the")
    print("  impulse response of an IIR filter has not died away by n = 63:")
    print("  that is truncation, not a defect of the identity.")

    section("3. Difference equation, transfer function, impulse response")
    n = 64
    h = apply_filter([0.5, 0.5], [1.0, -0.9], [1.0] + [0.0] * (n - 1))
    closed = [0.5 if k == 0 else 0.95 * 0.9 ** (k - 1) for k in range(n)]
    print("  y[n] = 0.5 x[n] + 0.5 x[n-1] + 0.9 y[n-1], so")
    print("  H(z) = (0.5 + 0.5 z^-1)/(1 - 0.9 z^-1) and, for n >= 1,")
    print("  h[n] = 0.95 * 0.9^(n-1).")
    print(f"  {'n':>4} {'h[n] from recursion':>22} {'closed form':>18}"
          f" {'error':>10}")
    for k in (0, 1, 2, 5, 10, 30, 63):
        print(f"  {k:>4} {h[k].real:>22.12f} {closed[k]:>18.12f}"
              f" {abs(h[k] - closed[k]):>10.2e}")
    print("  The recursion and the closed form agree to round-off, which is the")
    print("  practical meaning of 'the difference equation is the transform'.")

    section("4. Poles: radius sets decay, argument sets frequency, |z| = 1 decides stability")
    print(f"  {'zeros':>18} {'poles':>18} {'radius':>9} {'ln|h| slope':>14}"
          f" {'ln(radius)':>13} {'verdict':>12}")
    for label, poles in [("single, r = 0.5", [0.5]),
                         ("single, r = 0.9", [0.9]),
                         ("single, r = -0.9", [-0.9]),
                         ("single, r = 1.0", [1.0]),
                         ("single, r = 1.02", [1.02])]:
        b = [1.0]
        a = [1.0] + [0.0] * len(poles)
        for p in poles:
            poly = [1.0, -p]
            new = [0.0] * (len(a) + 1)
            for i, ai in enumerate(a):
                for j, pj in enumerate(poly):
                    new[i + j] += ai * pj
            a = new
        n = 80
        h = apply_filter(b, a, [1.0] + [0.0] * (n - 1))
        if abs(poles[0]) == 1.0:
            slope = float("nan")
        else:
            vals = [math.log(abs(h[k])) for k in range(10, 40)]
            slope = (vals[-1] - vals[0]) / (len(vals) - 1)
        radius = max(abs(p) for p in poles)
        verdict = "stable" if radius < 1 else ("marginal" if radius == 1 else "unstable")
        print(f"  {'-':>18} {label:>18} {radius:>9.4f} {slope:>14.6f}"
              f" {math.log(radius) if radius else float('nan'):>13.6f}"
              f" {verdict:>12}")
    print("  The measured logarithmic slope of |h[n]| equals ln r to three")
    print("  decimals: the pole radius *is* the per-sample decay factor.  At")
    print("  r = 1 the response neither decays nor grows; above 1 it grows and")
    print("  the system is unusable.")

    section("5. A two-pole resonator: the peak is not at the pole angle")
    fs, f0, r = 100.0, 10.0, 0.95
    w0 = 2 * math.pi * f0 / fs
    cos_w0, r2 = math.cos(w0), r * r


    def mag(w):
        z = cmath.exp(1j * w)
        return abs(1.0 / (1.0 - 2 * r * cos_w0 / z + r2 / z ** 2))

    target = (1 + r2) / (2 * r) * cos_w0
    w_peak_closed = math.acos(target)
    steps = 400000
    best_w, best_m = 0.0, -1.0
    grid = [(math.pi * j / steps, mag(math.pi * j / steps))
            for j in range(steps + 1)]
    for w, mval in grid:
        if mval > best_m:
            best_m, best_w = mval, w
    half = best_m / math.sqrt(2.0)
    crossings = [grid[j][0] for j in range(1, len(grid))
                 if (grid[j][1] - half) * (grid[j - 1][1] - half) <= 0]
    print(f"  poles at r e^(+-i w0): r = {r}, f0 = {f0} Hz, fs = {fs} Hz,"
          f" w0 = {w0:.9f} rad")
    print(f"  brute-force scan over {steps + 1} points of |H| on [0, pi]:")
    print(f"    peak at omega = {best_w:.9f} rad ="
          f" {best_w * fs / (2 * math.pi):.9f} Hz")
    print(f"    closed form arccos((1+r^2)/(2r) cos w0) = {w_peak_closed:.9f} rad"
          f" = {w_peak_closed * fs / (2 * math.pi):.9f} Hz")
    print(f"    difference = {abs(best_w - w_peak_closed):.3e} rad ="
          f" {abs(best_w - w_peak_closed) / w0 * 100:.5f} per cent of w0")
    print(f"    the pole angle w0 = {w0:.9f} rad = {f0:.6f} Hz is *not* the peak:")
    print(f"    quoting it would misplace the resonance by"
          f" {abs(w0 - w_peak_closed) / w0 * 100:.4f} per cent.")
    print(f"  |H| at the pole angle: {mag(w0):.6f}; at the true peak:"
          f" {best_m:.6f}")
    print(f"  Approximation 1/((1-r) 2 sin w0) ="
          f" {1 / ((1 - r) * 2 * math.sin(w0)):.4f}, i.e. low by"
          f" {(1 - 1 / ((1 - r) * 2 * math.sin(w0)) / best_m) * 100:.2f} per cent"
          f" at this pole radius.")
    if len(crossings) >= 2:
        low, high = crossings[0], crossings[-1]
        bw = (high - low) * fs / (2 * math.pi)
        print(f"  measured -3 dB points at {low:.6f} and {high:.6f} rad,"
              f" bandwidth {bw:.6f} Hz = {(high - low):.6f} rad")
        print(f"  measured Q = f0 / bandwidth = {f0 / bw:.4f};"
              f" the pole radius predicts Q ~ w0/(2(1-r)) ="
              f" {w0 / (2 * (1 - r)):.4f}")

    section("6. The convolution theorem, and the two traps")
    # (a) an FIR filter and a short input: the worst case for wraparound.
    nx, nh = 12, 8
    x = [0.0] * nx
    for j in range(nx):
        u = (j - 5) / 1.5
        x[j] = (1.0 - 2.0 * u * u) * math.exp(-u * u)
    h_fir = [1.0, -0.5, 0.25, -0.125, 0.0625, -0.03125, 0.015625, -0.0078125]
    linear = [0.0] * (nx + nh - 1)
    for i, xi in enumerate(x):
        for j, hj in enumerate(h_fir):
            linear[i + j] += xi * hj

    def circ_conv(a, b, length):
        pa = a + [0.0] * (length - len(a))
        pb = b + [0.0] * (length - len(b))
        fa, fb = dft(pa), dft(pb)
        prod = [fa[k] * fb[k] for k in range(length)]
        return idft(prod)

    unpadded = circ_conv(x, h_fir, nx)
    padded = circ_conv(x, h_fir, 32)
    print(f"  input: {nx} samples (a Ricker-like wavelet), FIR filter with"
          f" {nh} coefficients")
    print("  y = ifft(fft(x) .* fft(h)) reproduces the convolution only if the")
    print("  transform length is at least n_x + n_h - 1 ="
          f" {nx + nh - 1} samples.")
    print(f"  {'n':>4} {'linear convolution':>22} {'length 12':>16}"
          f" {'length 32':>16} {'wrap error':>14}")
    for k in (0, 1, 2, 3, 10, 12, 15, 18):
        want = linear[k] if k < len(linear) else 0.0
        print(f"  {k:>4} {want:>22.9f} {unpadded[k % nx].real:>16.9f}"
              f" {padded[k].real:>16.9f}"
              f" {abs(unpadded[k % nx].real - want):>14.2e}")
    print(f"  worst wrap error at length {nx}:"
          f" {max(abs(unpadded[k].real - linear[k]) for k in range(nx)):.3e}")
    print(f"  worst error at length 32:"
          f" {max(abs(padded[k].real - linear[k]) for k in range(len(linear))):.3e}")
    print("  Circular convolution folds the tail of the response back onto its")
    print("  start.  Pad to n_x + n_h - 1, never to the length of the input.")
    # (b) an IIR system, where the impulse response must itself be truncated.
    n = 256
    h_iir = apply_filter([0.5, 0.5], [1.0, -0.9], [1.0] + [0.0] * (n - 1))
    x_iir = [math.exp(-((j - 20) / 6.0) ** 2) for j in range(n)]
    y_rec = apply_filter([0.5, 0.5], [1.0, -0.9], x_iir)
    y_fft = circ_conv(x_iir, h_iir, 512)
    print(f"\n  IIR case, n = {n}, transform length 512: worst difference"
          f" between the recursion and the transform product on the first"
          f" {n} samples")
    print(f"    = {max(abs(y_rec[k] - y_fft[k].real) for k in range(n)):.3e}"
          f"  (the residual is the truncated tail |h[{n - 1}]| ="
          f" {abs(h_iir[-1]):.3e} times the sum of x)")

    section("7. The s plane to the z plane: z = exp(sT), and bilinear warping")
    T = 0.01
    print(f"  Sampling interval T = {T} s.  z = exp(sT) maps the left half of the")
    print("  s plane onto the inside of the unit circle:")
    print(f"  {'s':>20} {'Re s':>10} {'z = exp(sT)':>34} {'|z|':>12}")
    for s in (-5 + 0j, -2 + 30j, -1 + 100j, 1 + 2j):
        z = cmath.exp(s * T)
        print(f"  {s.real:>9.3f}{s.imag:>+9.3f}i {s.real:>10.3f}"
              f" {z.real:>17.12f}{z.imag:>+16.12f}i {abs(z):>12.9f}")
    print("  A negative real part always gives |z| < 1; the imaginary axis is")
    print("  the unit circle, and the strip |Im s| < pi/T maps onto it without")
    print("  overlap.  That overlap limit is aliasing, seen from the z plane.")
    print(f"\n  Bilinear transform z = (1 + sT/2)/(1 - sT/2), s = i Omega:")
    print(f"  {'Omega T':>10} {'|z|':>14} {'phase omega (rad)':>20}"
          f" {'2 atan(Omega T/2)':>20} {'error':>10}")
    for x_val in (0.5, 1.0, 2.0, 4.0, 8.0):
        s = 1j * x_val / T
        z = (1 + s * T / 2) / (1 - s * T / 2)
        print(f"  {x_val:>10.3f} {abs(z):>14.10f} {cmath.phase(z):>20.10f}"
              f" {2 * math.atan(x_val / 2):>20.10f}"
              f" {abs(cmath.phase(z) - 2 * math.atan(x_val / 2)):>10.2e}")
    print("  The bilinear transform keeps every pole inside the circle, at the")
    print("  price of warping frequency: the analogue Omega is compressed into")
    print("  omega = 2 arctan(Omega T/2) in (-pi, pi).  Pre-warp the design")
    print("  frequency, or the corner of your filter lands in the wrong place.")


if __name__ == "__main__":
    main()
