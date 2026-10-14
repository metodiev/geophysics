"""The Hilbert transform, the analytic signal and instantaneous attributes.

Run:  python3 hilbert_demo.py
Requires: Python standard library only.

Companion to lesson 01-10-06 (Hilbert Transform, Analytic Signal and
Instantaneous Phase).

Convention: forward DFT with exp(-2*pi*i*k*n/N), no scaling; inverse with 1/N.
Hilbert transform: multiply the spectrum by -i*sgn(f) -- i.e. rotate positive
frequencies by -90 degrees and negative frequencies by +90 degrees.  The
analytic signal is  z = x + i*H{x}; for a real x its spectrum is one-sided.
"""

import cmath
import math


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def fft(a):
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
    return [x.conjugate() / n for x in fft([v.conjugate() for v in a])]


def analytic_signal(x):
    """Return z = x + i H{x}, with the one-sided spectrum convention.

    The DFT's bins k = 1..N/2-1 are the positive frequencies, k > N/2 are the
    negative ones, and k = N/2 (when N is even) is the Nyquist bin, which is
    its own negative.  Doubling the positive bins and zeroing the negative ones
    gives the analytic signal; the Nyquist bin is left alone, because a real
    sampled signal cannot distinguish +f_N from -f_N.
    """
    n = len(x)
    spec = fft([complex(v) for v in x])
    out = [0j] * n
    out[0] = spec[0]
    for k in range(1, n // 2):
        out[k] = 2.0 * spec[k]
    if n % 2 == 0:
        out[n // 2] = spec[n // 2]
    return ifft(out)


def attributes(z):
    """Envelope, instantaneous phase and instantaneous frequency of z."""
    env = [abs(v) for v in z]
    phase = []
    unwrapped = 0.0
    previous = None
    for v in z:
        p = cmath.phase(v)
        if previous is not None:
            while p - previous > math.pi:
                p -= 2 * math.pi
            while p - previous < -math.pi:
                p += 2 * math.pi
        phase.append(p)
        previous = p
        unwrapped = p
    return env, phase


def inst_frequency(phase, dt):
    """d(phase)/dt / (2 pi), central differences."""
    n = len(phase)
    out = []
    for i in range(n):
        lo = max(0, i - 1)
        hi = min(n - 1, i + 1)
        out.append((phase[hi] - phase[lo]) / (2.0 * math.pi * (hi - lo) * dt))
    return out


def rms(v):
    return math.sqrt(sum(a * a for a in v) / len(v))


def main():
    section("1. The Hilbert transform on a pure cosine")
    n = 1024
    dt = 1.0 / 512.0            # T = 2 s, so 40 Hz is exactly 80 cycles
    f0 = 40.0
    amp1 = 2.5
    phi1 = 0.7
    x = [amp1 * math.cos(2 * math.pi * f0 * i * dt - phi1) for i in range(n)]
    z = analytic_signal(x)
    env, phase = attributes(z)
    f_inst = inst_frequency(phase, dt)
    interior = slice(64, n - 64)
    print(f"  x(t) = {amp1} cos(2 pi {f0} t - {phi1}); N = {n}, dt = {dt} s")
    print(f"  envelope:         mean {sum(env[interior]) / len(env[interior]):.8f},"
          f" max deviation from {amp1} ="
          f" {max(abs(v - amp1) for v in env[interior]):.2e}")
    print(f"  quadrature:       max |imag(z) - {amp1} sin(2 pi f0 t - phi)| ="
          f" {max(abs(z[i].imag - amp1 * math.sin(2 * math.pi * f0 * i * dt - phi1)) for i in range(64, n - 64)):.2e}")
    print(f"  instantaneous f:  mean {sum(f_inst[interior]) / len(f_inst[interior]):.8f}"
          f" Hz (true {f0}), max deviation"
          f" {max(abs(v - f0) for v in f_inst[interior]):.2e} Hz")
    predicted = [2 * math.pi * f0 * i * dt - phi1 for i in range(n)]

    def unwrap(p):
        out = [p[0]]
        for value in p[1:]:
            d = value - out[-1]
            while d > math.pi:
                value -= 2 * math.pi
                d = value - out[-1]
            while d < -math.pi:
                value += 2 * math.pi
                d = value - out[-1]
            out.append(value)
        return out

    upred = unwrap(predicted)
    uactual = unwrap(phase)
    shift = uactual[0] - math.degrees(0) * 0
    print(f"  phase:            the unwrapped phase is a straight line; after")
    print(f"                    removing the one constant offset it matches")
    print(f"                    -2*pi*f0*t + phi with max error"
          f" {max(abs(a - b - (uactual[0] - upred[0])) for a, b in zip(uactual, upred)):.2e} rad")
    print("  For a single sinusoid the analytic signal is exactly a rotating phasor:")
    print("  constant modulus, linear phase.  Every deviation from that is signal.")

    section("2. Hilbert transform properties, checked numerically")
    # integer-cycle components only: the record is exactly periodic, so there
    # are no edge effects to confuse the test
    rng = [math.sin(2 * math.pi * 37 * i / n)
           + 0.5 * math.cos(2 * math.pi * 101 * i / n)
           + 0.2 * math.sin(2 * math.pi * 200 * i / n) for i in range(n)]
    H1 = [v.imag for v in analytic_signal(rng)]
    H2 = [v.imag for v in analytic_signal(H1)]
    print("  H{H{x}} = -x :  max |H(H(x)) + x| ="
          f" {max(abs(a + b) for a, b in zip(H2, rng)):.2e}")
    Hs = [v.imag for v in analytic_signal([v + 1.5 for v in rng])]
    print(f"  linearity:        max |H(x + 1.5) - H(x) - H(1.5)| ="
          f" {max(abs(a - b - c) for a, b, c in zip(Hs, H1, [0.0] * n)):.2e}")
    corr = sum(a * b for a, b in zip(rng, H1))
    print(f"  orthogonality:    sum x*H(x) = {corr:.3e}"
          " (x and H{x} are uncorrelated)")
    print(f"  energy:           RMS(x) = {rms(rng[:n - 1]):.6f},"
          f" RMS(H(x)) = {rms(H1[:n - 1]):.6f}")
    print("  H{H{x}} = -x says the transform is a 90 degree phase shift applied")
    print("  twice.  It is why z = x + i*H{x} has a one-sided spectrum: the two")
    print("  terms reinforce on one side and cancel on the other.")
    spec_x = fft([complex(v) for v in rng])
    spec_z = fft(analytic_signal(rng))
    neg_energy = sum(abs(spec_z[k]) ** 2 for k in range(n // 2 + 1, n))
    pos_energy = sum(abs(spec_z[k]) ** 2 for k in range(1, n // 2))
    print(f"  energy of z in negative frequencies: {neg_energy:.3e}; in positive"
          f" frequencies: {pos_energy:.6e}")
    print("  The negative half of the spectrum is empty to round-off, which is the")
    print("  whole point: the analytic signal carries only the positive half.")

    section("3. Amplitude modulation: the envelope recovers the message")
    carrier = 60.0
    mod_f = 3.0
    n2 = 4096
    dt2 = 1.0 / 1024.0          # T = 4 s: 60 Hz is 240 cycles, 3 Hz is 12
    x = [(1.0 + 0.6 * math.cos(2 * math.pi * mod_f * i * dt2))
         * math.cos(2 * math.pi * carrier * i * dt2) for i in range(n2)]
    z = analytic_signal(x)
    env, _phase = attributes(z)
    truth = [1.0 + 0.6 * math.cos(2 * math.pi * mod_f * i * dt2) for i in range(n2)]
    interior = slice(256, n2 - 256)
    err = max(abs(env[i] - truth[i]) for i in range(256, n2 - 256))
    print(f"  x(t) = (1 + 0.6 cos(2 pi {mod_f} t)) cos(2 pi {carrier} t)")
    print(f"  envelope error against the true modulation: max {err:.3e},"
          f" RMS {math.sqrt(sum((env[i] - truth[i]) ** 2 for i in range(256, n2 - 256)) / len(env[interior])):.3e}")
    print("  An amplitude-modulated carrier has zero mean, so no amount of")
    print("  smoothing of x recovers the modulation; the envelope does, to the")
    print("  accuracy shown (the modulation is far below the carrier, which is the")
    print("  Bedrosian condition for the envelope to be exact).")
    print("  This is the operation used to compute amplitude attributes on seismic")
    print("  data and to demodulate any narrow-band signal.")

    section("4. A chirp: instantaneous frequency tracks the sweep")
    n3 = 4096
    dt3 = 0.002
    f_start, f_end = 5.0, 40.0
    t_total = n3 * dt3
    chirp = []
    for i in range(n3):
        t = i * dt3
        chirp.append(math.cos(2 * math.pi * (f_start * t
                                             + (f_end - f_start) * t * t / (2.0 * t_total))))
    z = analytic_signal(chirp)
    env, phase = attributes(z)
    f_inst = inst_frequency(phase, dt3)
    print(f"  a linear sweep from {f_start} to {f_end} Hz over {t_total:.3f} s")
    print(f"  {'t (s)':>8} {'true f (Hz)':>12} {'instantaneous f':>16}"
          f" {'envelope':>10}")
    for t in (0.25, 1.0, 2.0, 4.0, 8.0):
        i = int(round(t / dt3))
        if i >= n3:
            continue
        true_f = f_start + (f_end - f_start) * t / t_total
        print(f"  {t:>8.2f} {true_f:>12.3f} {f_inst[i]:>16.3f} {env[i]:>10.4f}")
    lo_i, hi_i = n3 // 8, 7 * n3 // 8
    err = max(abs(f_inst[i] - (f_start + (f_end - f_start) * i * dt3 / t_total))
              for i in range(lo_i, hi_i))
    err_all = max(abs(f_inst[i] - (f_start + (f_end - f_start) * i * dt3 / t_total))
                  for i in range(16, n3 - 16))
    print(f"  max error over the middle half of the sweep: {err:.3f} Hz,"
          f" over the whole record {err_all:.3f} Hz")
    print(f"  envelope in the middle half: {min(env[lo_i:hi_i]):.6f} to"
          f" {max(env[lo_i:hi_i]):.6f}; near the ends it departs from 1 because the")
    print("  transform needs samples on both sides of every point.")
    print("  A single number, f(t), describes a signal whose spectrum is spread")
    print("  over the whole band: instantaneous attributes are a different")
    print("  description from the spectrum, not a cheaper version of it.")

    section("5. A synthetic seismic trace: where are the reflections?")
    n4 = 2048
    dt4 = 0.002
    arrivals = ((0.30, 1.0), (0.52, 0.7), (0.62, -0.5), (0.95, 0.45), (1.40, 0.3))
    f_dom = 25.0

    def ricker(tau, f):
        a = math.pi * f * tau
        return (1.0 - 2.0 * a * a) * math.exp(-a * a)

    trace = [0.0] * n4
    for time, refl in arrivals:
        i0 = int(round(time / dt4))
        for j in range(-80, 81):
            i = i0 + j
            if 0 <= i < n4:
                trace[i] += refl * ricker(j * dt4, f_dom)
    z = analytic_signal(trace)
    env, _phase = attributes(z)
    print("  A synthetic trace built from Ricker wavelets with known arrival times")
    print("  and reflection coefficients (SYNTHETIC, chosen for readability):")
    print(f"  {'true t (s)':>11} {'true refl':>10} {'envelope peak (s)':>18}"
          f" {'envelope there':>15} {'error (ms)':>11}")
    for time, refl in arrivals:
        i0 = int(round(time / dt4))
        lo, hi = max(0, i0 - 40), min(n4, i0 + 41)
        k = max(range(lo, hi), key=lambda i: env[i])
        print(f"  {time:>11.3f} {refl:>10.2f} {k * dt4:>18.3f} {env[k]:>15.4f}"
              f" {(k * dt4 - time) * 1000.0:>11.1f}")
    print("  The envelope peaks land on the arrivals within a sample for the")
    print("  isolated events, and the peak height tracks the reflection coefficient")
    print("  (with the sign lost, since an envelope cannot be negative).")
    thin_gap = 1.0 / (2.0 * f_dom)
    thin = [0.0] * n4
    for tau_off, refl in ((0.0, 1.0), (thin_gap, -1.0)):
        i0 = int(round((0.8 + tau_off) / dt4))
        for j in range(-80, 81):
            i = i0 + j
            if 0 <= i < n4:
                thin[i] += refl * ricker(j * dt4, f_dom)
    zt = analytic_signal(thin)
    envt, _pt = attributes(zt)
    lo, hi = int(0.7 / dt4), int(0.95 / dt4)
    peaks = [i for i in range(lo + 1, hi - 1)
             if envt[i] > envt[i - 1] and envt[i] >= envt[i + 1]]
    print(f"\n  Two Ricker wavelets of opposite sign separated by {thin_gap * 1000:.1f} ms")
    print(f"  (half the {1.0 / f_dom * 1000:.1f} ms dominant period):")
    print(f"    number of envelope maxima in the window: {len(peaks)}")
    single = [0.0] * n4
    i0 = int(round(0.8 / dt4))
    for j in range(-80, 81):
        i = i0 + j
        if 0 <= i < n4:
            single[i] += ricker(j * dt4, f_dom)
    env_single = attributes(analytic_signal(single))[0]
    print(f"    peak envelope of the pair: {max(envt[lo:hi]):.4f}")
    print(f"    peak envelope of a single unit wavelet:"
          f" {max(env_single[lo:hi]):.4f}")
    print(f"    reflection coefficients are +1 and -1, whose envelope would be 0")
    print("  One maximum, not two, and an amplitude that is close to a single")
    print("  wavelet and unrelated to the sum of the two coefficients.  The envelope")
    print("  picks isolated events; it neither resolves a thin bed nor measures the")
    print("  reflection coefficient of an interfering pair.")

    section("6. What the instantaneous attributes cannot do")
    n5 = 4096
    dt5 = 0.0005
    two = [math.cos(2 * math.pi * 30.0 * i * dt5)
           + 0.9 * math.cos(2 * math.pi * 46.0 * i * dt5) for i in range(n5)]
    z = analytic_signal(two)
    env, phase = attributes(z)
    f_inst = inst_frequency(phase, dt5)
    print("  Two equal-ish tones at 30 Hz and 46 Hz.")
    print(f"  {'t (s)':>8} {'envelope':>10} {'instantaneous f':>17}")
    for t in (0.2, 0.4, 0.6, 0.8, 1.0):
        i = int(round(t / dt5))
        print(f"  {t:>8.2f} {env[i]:>10.4f} {f_inst[i]:>17.3f}")
    print(f"  envelope range {min(env[64:n5 - 64]):.4f} to {max(env[64:n5 - 64]):.4f};"
          f" instantaneous frequency {min(f_inst[64:n5 - 64]):.2f} to"
          f" {max(f_inst[64:n5 - 64]):.2f} Hz")
    print("  The instantaneous frequency sweeps between the two tones and beyond.")
    print("  It is a perfectly well-defined quantity and a completely misleading")
    print("  description of a two-tone signal: instantaneous attributes are only")
    print("  meaningful for a signal that is narrow-band at each instant.  Quote")
    print("  them next to the bandwidth, or not at all.")
    print("\n  Practical notes for implementation:")
    print("    - the transform needs the whole trace, so attributes near the ends")
    print("      are contaminated; taper or discard the first and last 1-2 wavelet")
    print("      lengths (the first and last 64 samples above).")
    print("    - for even N the Nyquist bin is shared between +f and -f, so it")
    print("      cannot be assigned to either; leaving it un-doubled (as here) is")
    print("      the standard choice.")
    print("    - the instantaneous frequency is a derivative of a wrapped phase, so")
    print("      it is noisy: a 2*pi wrap error becomes a spike of 1/dt.  Unwrap")
    print("      before differentiating, as the code here does.")


if __name__ == "__main__":
    main()
