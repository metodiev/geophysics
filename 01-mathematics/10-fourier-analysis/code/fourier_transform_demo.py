"""The Fourier transform and its properties, checked numerically.

Run:  python3 fourier_transform_demo.py
Requires: Python standard library only.

Companion to lesson 01-10-02 (The Fourier Transform and Its Properties).

Convention (used throughout this module)
----------------------------------------
    X(f) = integral of x(t) * exp(-2*pi*i*f*t) dt          (forward)
    x(t) = integral of X(f) * exp(+2*pi*i*f*t) df          (inverse)
so the forward kernel is exp(-i*omega*t) and

    d/dt  ->  multiply by  +2*pi*i*f = +i*omega
    d/dx  ->  multiply by  +i*k                (k = 2*pi*f)

Every property is *verified numerically* against a signal whose transform is
known in closed form.  Nothing is asserted without being computed here.
"""

import cmath
import math

DT = 0.02                 # sample spacing in the synthetic (t, f) units
N = 4096                  # samples; a power of two so the FFT applies
T0 = -(N // 2) * DT       # time origin of sample 0


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def fft(a):
    """Iterative radix-2 Cooley-Tukey FFT: X[k] = sum_n a[n] exp(-2*pi*i*k*n/N).

    O(N log N).  Derived properly in lesson 01-10-04; included here so that a
    full-resolution spectrum is cheap enough to integrate.  N must be a power
    of two.
    """
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
    """Inverse DFT with the 1/N normalisation."""
    n = len(a)
    conj = [x.conjugate() for x in a]
    out = fft(conj)
    return [(x.conjugate() / n) for x in out]


def samples(func):
    """Sample a function on the symmetric grid used throughout this demo."""
    return [func(T0 + i * DT) for i in range(N)]


def numeric_ft(values, freqs, dt=DT, t0=T0):
    """X(f) ~ dt * sum_n x[n] exp(-2*pi*i*f*t_n): the integral as a Riemann sum.

    This is the *definition* evaluated on a grid, valid at any frequency, not
    only at the DFT bins.
    """
    out = []
    for f in freqs:
        acc = 0j
        phase = cmath.exp(-2j * math.pi * f * t0)
        step = cmath.exp(-2j * math.pi * f * dt)
        w = 1 + 0j
        for value in values:
            acc += value * w
            w *= step
        out.append(acc * phase * dt)
    return out


def gauss(t):
    """x(t) = exp(-pi t^2), whose transform is exp(-pi f^2) (self-reciprocal)."""
    return math.exp(-math.pi * t * t)


def boxcar_of(width):
    half = width / 2.0
    return lambda t: 1.0 if -half <= t <= half else 0.0


def rms_widths(values, dt=DT):
    """RMS width in time and in frequency, from the energy densities."""
    energy = sum(v * v for v in values) * dt
    mean_t = sum(t * v * v for t, v in zip((T0 + i * DT for i in range(N)), values)) * dt / energy
    var_t = sum((t - mean_t) ** 2 * v * v
                for t, v in zip((T0 + i * DT for i in range(N)), values)) * dt / energy
    spec = fft(values)
    df = 1.0 / (N * DT)
    power = [abs(x) ** 2 * df * DT ** 2 for x in spec]
    total = sum(power)
    freqs = [(k if k < N // 2 else k - N) * df for k in range(N)]
    mean_f = sum(f * p for f, p in zip(freqs, power)) / total
    var_f = sum((f - mean_f) ** 2 * p for f, p in zip(freqs, power)) / total
    return math.sqrt(var_t), math.sqrt(var_f), energy


def main():
    print(f"grid: N = {N} samples, dt = {DT} s, span = {N * DT:.2f} s, "
          f"t0 = {T0:.3f} s, df = {1.0 / (N * DT):.6f} Hz")

    section("1. The Gaussian is its own transform")
    x = samples(gauss)
    freqs = [0.0, 0.25, 0.5, 1.0, 1.5, 2.0]
    got = numeric_ft(x, freqs)
    print(f"  {'f':>6} {'X numeric':>26} {'exp(-pi f^2)':>14} {'abs err':>10}")
    for f, value in zip(freqs, got):
        exact = math.exp(-math.pi * f * f)
        print(f"  {f:>6.2f} {value.real:>13.10f}+{value.imag:>11.1e}i"
              f" {exact:>14.10f} {abs(value.real - exact):>10.2e}")
    print("  Real, even signal -> real, even spectrum; the imaginary part is at")
    print("  the 1e-16 level, i.e. round-off.")
    print("  Widely-quoted 'transform pairs' table value: exp(-a t^2) <-> sqrt(pi/a)")
    print("  * exp(-pi^2 f^2/a); with a = pi that is exp(-pi f^2).")

    section("2. A boxcar becomes a sinc, with zeros at multiples of 1/T")
    width = 4.0
    # Sample the boxcar at cell *midpoints* (t = t0 + (i + 1/2) dt).  Then the
    # sampled boxcar contains exactly M = width/dt = 200 samples, symmetric
    # about zero, so M*dt = width exactly and the discrete sum of the sampled
    # pulse vanishes exactly at f = n/width -- matching the zeros of the sinc.
    t_mid0 = T0 + DT / 2.0
    b = [1.0 if abs(t_mid0 + i * DT) < width / 2.0 else 0.0 for i in range(N)]
    nonzero = sum(1 for v in b if v)
    print(f"  boxcar width T = {width} s sampled at dt = {DT} s: {nonzero} nonzero"
          f" samples, so M*dt = {nonzero * DT:.2f} s = T.")

    def sinc(x):
        return 1.0 if x == 0.0 else math.sin(math.pi * x) / (math.pi * x)

    test_f = [0.0, 0.1, 0.25, 0.3, 0.5, 0.75]
    got = numeric_ft(b, test_f, t0=t_mid0)
    print(f"  {'f (Hz)':>9} {'f/(1/T)':>8} {'Re X numeric':>15} {'T*sinc(fT)':>15}"
          f" {'mag err':>10}")
    for f, value in zip(test_f, got):
        exact = width * sinc(f * width)
        err = abs(abs(value) - abs(exact))
        err_text = f"{err:>10.2e}" if abs(exact) > 1e-6 else "  at a zero"
        print(f"  {f:>9.4f} {f * width:>8.2f} {value.real:>15.6e} {exact:>15.6e}"
              f" {err_text}")
    print("  At f = n/T the sampled sum cancels to round-off, exactly where the")
    print("  continuous transform has its zeros.  Elsewhere the sampled sum equals")
    print("  the sinc times the Dirichlet correction (pi f dt)/sin(pi f dt), here")
    for f in (0.3, 0.75):
        corr = (math.pi * f * DT) / math.sin(math.pi * f * DT)
        print(f"    f = {f:.2f} Hz: correction = {corr:.6f}, so |X| / |T sinc|"
              f" = {corr:.6f}")

    scan = [1.0 / width + k * 0.0005 for k in range(0, 1400)]
    vals = numeric_ft(b, scan, t0=t_mid0)
    mags = [abs(v) for v in vals]
    smags = [abs(width * sinc(f * width)) for f in scan]
    imax = max(range(len(mags)), key=lambda i: mags[i])
    ismax = max(range(len(smags)), key=lambda i: smags[i])
    print(f"  First sidelobe, numeric sum  : f = {scan[imax]:.4f} Hz"
          f" = {scan[imax] * width:.4f}/T, level"
          f" {20.0 * math.log10(mags[imax] / width):+.2f} dB")
    print(f"  First sidelobe, T*sinc(fT)   : f = {scan[ismax]:.4f} Hz"
          f" = {scan[ismax] * width:.4f}/T, level"
          f" {20.0 * math.log10(smags[ismax] / width):+.2f} dB")
    print("  A hard edge in time costs about 13 dB of sidelobe suppression in")
    print("  frequency.  Tapering the edge is what a window does (lesson 01-10-05).")

    section("3. The property table, verified one line at a time")
    xg = samples(gauss)
    f0 = 1.0
    print("  (a) Linearity: F{2g + g'} = 2G + G'")
    gp = samples(lambda t: 2.0 * gauss(t) + math.exp(-t * t))
    lhs = numeric_ft(gp, [0.0, 0.5, 1.0])
    rhs = [2.0 * v for v in numeric_ft(xg, [0.0, 0.5, 1.0])]
    rhs = [a + b for a, b in zip(rhs, numeric_ft(samples(lambda t: math.exp(-t * t)),
                                                [0.0, 0.5, 1.0]))]
    print(f"      max |lhs - rhs| = {max(abs(a - b) for a, b in zip(lhs, rhs)):.3e}")

    print("  (b) Shift: F{g(t - t0)} = G(f) exp(-2*pi*i*f*t0), t0 = 5")
    shift = 5.0
    shifted = samples(lambda t: gauss(t - shift))
    g0 = numeric_ft(xg, [0.0, 0.5, 1.0, 1.5])
    gs = numeric_ft(shifted, [0.0, 0.5, 1.0, 1.5])
    for f, a, b2 in zip([0.0, 0.5, 1.0, 1.5], g0, gs):
        predicted = a * cmath.exp(-2j * math.pi * f * shift)
        print(f"      f = {f:4.2f}: |shifted| = {abs(b2):.6e} (unshifted"
              f" {abs(a):.6e}), phase error = {abs(b2 - predicted):.2e}")
    print("      A time shift touches only the phase: |X| is unchanged.")

    print("  (c) Scaling: F{g(2t)} = (1/2) G(f/2)")
    scaled = samples(lambda t: gauss(2.0 * t))
    for f in (0.0, 0.5, 1.0):
        lhs2 = numeric_ft(scaled, [f])[0]
        rhs2 = 0.5 * numeric_ft(xg, [f / 2.0])[0]
        print(f"      f = {f:4.2f}: lhs = {lhs2.real:.10f}, rhs = {rhs2.real:.10f},"
              f" diff = {abs(lhs2 - rhs2):.2e}")
    print("      Compressing in time expands in frequency, and vice versa.")

    print("  (d) Modulation: F{g(t) cos(2 pi f0 t)} = [G(f-f0) + G(f+f0)]/2")
    f0 = 2.0
    mod = samples(lambda t: gauss(t) * math.cos(2 * math.pi * f0 * t))
    for f in (0.0, 2.0, 4.0):
        lhs3 = numeric_ft(mod, [f])[0]
        rhs3 = 0.5 * (numeric_ft(xg, [f - f0])[0] + numeric_ft(xg, [f + f0])[0])
        print(f"      f = {f:4.2f}: lhs = {lhs3.real:.3e}+{lhs3.imag:.1e}i,"
              f" rhs = {rhs3.real:.3e}, diff = {abs(lhs3 - rhs3):.2e}")

    print("  (e) Differentiation: F{dx/dt} = 2*pi*i*f * X(f)")
    deriv = samples(lambda t: -2.0 * math.pi * t * gauss(t))
    dfreq = [0.0, 0.5, 1.0, 1.5]
    dl = numeric_ft(deriv, dfreq)
    dr = [2j * math.pi * f * v for f, v in zip(dfreq, numeric_ft(xg, dfreq))]
    for f, a, b2 in zip(dfreq, dl, dr):
        print(f"      f = {f:4.2f}: numeric {a.real:+.6e}{a.imag:+.6e}i"
              f"   i*2*pi*f*X {b2.real:+.6e}{b2.imag:+.6e}i"
              f"   diff {abs(a - b2):.2e}")
    print("      This is the single most useful line in the table: differentiating")
    print("      in space or time is multiplying by i*k or i*omega in wavenumber or")
    print("      frequency.  It converts differential equations into algebra.")

    print("  (f) Real signal: X(-f) = conj(X(f)) (Hermitian symmetry)")
    for f in (0.0, 0.5, 1.0):
        pos = numeric_ft(xg, [f])[0]
        neg = numeric_ft(xg, [-f])[0]
        print(f"      f = {f:4.2f}: |X(-f) - conj(X(f))| = {abs(neg - pos.conjugate()):.3e}")
    print("      For a real signal the negative frequencies carry no independent")
    print("      information -- which is why the one-sided spectrum works and why")
    print("      the analytic signal of lesson 01-10-06 can discard them.")

    section("4. The finite-difference operator is a filter, not a derivative")
    print("  Ideal spectral derivative multiplies by 2*pi*i*f.  A finite difference")
    print("  multiplies by its own transfer function:")
    print("    central: 2*pi*i*f ->  i*sin(2*pi*f*h)/h")
    print("    forward: 2*pi*i*f ->  (exp(2*pi*i*f*h) - 1)/h")
    print(f"  {'f (Hz)':>8} {'h':>7} {'|H_central|/|i2pif|':>21}"
          f" {'phase err (deg)':>17} {'|H_fwd|/|i2pif|':>17}")
    for h in (0.02, 0.1, 0.5):
        for f in (0.1, 1.0, 5.0, 10.0):
            w = 2 * math.pi * f
            hc = 1j * cmath.sin(w * h) / h
            hf = (cmath.exp(1j * w * h) - 1.0) / h
            ideal = 1j * w
            phase_err = math.degrees(cmath.phase(hc / ideal))
            print(f"  {f:>8.2f} {h:>7.2f} {abs(hc) / abs(ideal):>21.6f}"
                  f" {phase_err:>17.3f} {abs(hf) / abs(ideal):>17.6f}")
    print("  The central difference has exactly the same 90 degree phase as the")
    print("  ideal operator, so its only error is the real amplitude factor")
    print("  sin(2*pi*f*h)/(2*pi*f*h): a low-pass roll-off that attenuates precisely")
    print("  the high wavenumbers where a rough surface or a thin bed puts its")
    print("  signal.  At f = 1/(2h) the response is exactly zero -- the stencil is")
    print("  blind there, and flips sign just above it (the 180 degree entry).")
    print("  A one-sided (forward) difference has no such blind frequency but a much")
    print("  larger amplitude error plus a first-order phase error, which is why it")
    print("  smears dipping events in migration.  Spectral differentiation with i*k")
    print("  has no roll-off at all -- but it is global, it assumes periodicity, and")
    print("  it amplifies whatever noise sits at the top of the band.")

    section("5. Parseval: the same energy in either domain")
    x = samples(gauss)
    spec = fft(x)
    df = 1.0 / (N * DT)
    energy_time = sum(v * v for v in x) * DT
    # Integral of |X|^2 df, with X ~ dt * X_DFT:
    energy_freq = sum(abs(s) ** 2 for s in spec) * df * DT ** 2
    print(f"  integral |x(t)|^2 dt = {energy_time:.12f}")
    print(f"  integral |X(f)|^2 df = {energy_freq:.12f}")
    print(f"  relative difference  = {abs(energy_freq - energy_time) / energy_time:.3e}")
    dc = spec[0]
    print(f"  The DC bin read three ways, all of them the same number:")
    print(f"    sum of samples  X_DFT[0]     = {dc.real:.10f}")
    print(f"    average         X_DFT[0]/N   = {dc.real / N:.10f}  (= df * X(0),"
          f" df = {df:.6f})")
    print(f"    integral        dt * X_DFT[0] = {dc.real * DT:.10f}  (= X(0) = 1)")
    print("  'The FFT is wrong by a factor of N' almost always means one of these")
    print("  three was confused with another.  The forward DFT sums; it does not")
    print("  average and it does not integrate.")
    wrong1 = sum(abs(v) ** 2 for v in spec) * df
    wrong2 = sum(abs(v) ** 2 for v in spec) * (1.0 / N) * DT ** 2
    print(f"  Forgetting the dt scaling of X_DFT gives {wrong1:.6e},"
          f" too large by {wrong1 / energy_time:.1f}x = 1/dt^2.")
    print(f"  Using df = 1/N instead of 1/(N dt) gives {wrong2:.6e},"
          f" too small by {energy_time / wrong2:.1f}x = 1/dt.")
    print("  Both classic normalisation errors are demonstrated, not asserted.")

    section("6. Bridge: DFT values are the continuous transform sampled")
    print("  For a signal that is negligible outside the window,")
    print("      X_DFT[k] ~ (1/dt) * X(f_k) * exp(+2*pi*i*f_k*t0)")
    print("  where the phase factor is the shift property applied to the grid")
    print("  origin t0.  Check with the Gaussian:")
    freqs_check = [0, 8, 16, 24, 40, 80]
    print(f"  {'k':>4} {'f_k (Hz)':>10} {'dt*X_DFT':>14} {'X(f_k)':>14}"
          f" {'|mag err|':>11} {'phase resid':>12}")
    for k in freqs_check:
        fk = k * df
        lhs = spec[k] * DT
        rhs = math.exp(-math.pi * fk * fk)
        detrended = lhs * cmath.exp(-2j * math.pi * fk * T0)
        print(f"  {k:>4} {fk:>10.5f} {abs(lhs):>14.10f} {rhs:>14.10f}"
              f" {abs(abs(lhs) - rhs):>11.2e} {abs(detrended - rhs):>12.2e}")
    print("  So the DFT is not a different transform: it is the continuous")
    print("  transform, sampled at the bins, multiplied by dt, and carrying a")
    print("  phase factor for wherever the time origin sits.  Every normalisation")
    print("  dispute in Fourier practice is this one sentence.")

    section("7. The uncertainty relation, measured rather than quoted")
    for scale in (0.5, 1.0, 2.0, 4.0):
        vals = samples(lambda t: gauss(scale * t))
        st, sf, _ = rms_widths(vals)
        print(f"  x(t) = exp(-pi ({scale} t)^2): sigma_t = {st:.6f},"
              f" sigma_f = {sf:.6f}, product = {st * sf:.8f}")
    print(f"  1/(4*pi) = {1.0 / (4.0 * math.pi):.8f}; the product is invariant under")
    print("  scaling, which is the content of the uncertainty relation")
    print("  sigma_t * sigma_f >= 1/(4*pi), with equality for a Gaussian.")


if __name__ == "__main__":
    main()
