"""Complex arithmetic, phasors and impedance, checked numerically.

Run:  python3 complex_arithmetic_demo.py
Requires: Python standard library only (``cmath``).

Companion to lesson 01-11-01 (Complex Numbers, Polar Form and Argand
Diagrams).

The point of the demo is that every identity in the lesson is *measured*.
Phasor addition is checked against the time-domain sum; the impedance of a
series RC network is checked against a direct simulation of the circuit; the
steady state of a damped driven oscillator is checked against a numerical
integration of its equation of motion; and the roots of unity are verified to
sum to zero.

Convention: a physical sinusoid is written
    a cos(omega t + phi)  =  Re{ A exp(i omega t) },  A = a exp(i phi),
with ``A`` the phasor.  The physics ``exp(-i omega t)`` convention is treated
in lesson 01-11-06.
"""

import cmath
import math


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def polar(z):
    """(magnitude, phase in radians) of a complex number."""
    return abs(z), cmath.phase(z)


def sum_phasors(terms):
    """Sum a list of (amplitude, phase) sinusoids into one (amplitude, phase).

    Each term represents a * cos(omega t + phi).  The sum of two sinusoids of
    the same frequency is again a sinusoid of that frequency, and the phasor
    sum gives it exactly -- this is the whole content of Section 4 of the
    lesson.
    """
    z = 0j
    for amp, phi in terms:
        z += amp * cmath.exp(1j * phi)
    return abs(z), cmath.phase(z)


def time_series_sum(terms, omega, n=24):
    """Sample sum_k a_k cos(omega t + phi_k) on one period, by direct evaluation."""
    out = []
    for j in range(n):
        t = 2 * math.pi * j / (omega * n)
        out.append(sum(a * math.cos(omega * t + p) for a, p in terms))
    return out


def series_residual(terms, amp, phi, omega, n=24):
    """Worst |direct sum - single phasor| over one period, normalised."""
    worst = 0.0
    for j in range(n):
        t = 2 * math.pi * j / (omega * n)
        direct = sum(a * math.cos(omega * t + p) for a, p in terms)
        phasor = amp * math.cos(omega * t + phi)
        worst = max(worst, abs(direct - phasor))
    return worst


def rc_impedance(omega, r, c):
    """Series R-C impedance Z = R + 1/(i omega C)."""
    return r + 1.0 / (1j * omega * c)


def rk4_first_order(rate, y0, dt, n):
    """Integrate y' = rate(t, y) with classical RK4; returns the state history."""
    ys = [y0]
    y, t = y0, 0.0
    for _ in range(n):
        k1 = rate(t, y)
        k2 = rate(t + dt / 2, y + dt * k1 / 2)
        k3 = rate(t + dt / 2, y + dt * k2 / 2)
        k4 = rate(t + dt, y + dt * k3)
        y += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += dt
        ys.append(y)
    return ys


def demodulate(values, omega, dt, t0):
    """(amplitude, phase) of the sinusoid in a long record, by projection.

    The projections onto cos and sin are the exact least-squares fit of
    a*cos(omega t) + b*sin(omega t) to the samples, so the amplitude is not
    biased by where the peak happens to fall between samples.  ``values[k]``
    is assumed to sit at ``t = t0 + k*dt``.
    """
    sc = ss = scs = scc = sss = 0.0
    for k, y in enumerate(values):
        c = math.cos(omega * (t0 + k * dt))
        s = math.sin(omega * (t0 + k * dt))
        sc += y * c
        ss += y * s
        scc += c * c
        sss += s * s
        scs += c * s
    det = scc * sss - scs * scs
    a = (sc * sss - ss * scs) / det
    b = (ss * scc - sc * scs) / det
    return math.hypot(a, b), math.atan2(-b, a)


def rk4_oscillator(m, damping, k, force, x0, v0, dt, n):
    """Integrate m x'' + c x' + k x = force(t) with classical RK4.

    Returns lists of times and positions.  Used to check the phasor answer for
    the driven oscillator without reusing the phasor algebra.
    """
    def deriv(t, x, v):
        return v, (force(t) - damping * v - k * x) / m

    ts, xs = [0.0], [x0]
    x, v, t = x0, v0, 0.0
    for _ in range(n):
        k1x, k1v = deriv(t, x, v)
        k2x, k2v = deriv(t + dt / 2, x + dt * k1x / 2, v + dt * k1v / 2)
        k3x, k3v = deriv(t + dt / 2, x + dt * k2x / 2, v + dt * k2v / 2)
        k4x, k4v = deriv(t + dt, x + dt * k3x, v + dt * k3v)
        x += dt * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
        v += dt * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
        t += dt
        ts.append(t)
        xs.append(x)
    return ts, xs


def main():
    section("1. Rectangular and polar form: the same number, two readings")
    samples = [
        ("3 + 4i", 3 + 4j),
        ("-1 + 1i", -1 + 1j),
        ("-2 - 2i", -2 - 2j),
        ("0.5 - 0.866i", 0.5 - 0.8660254037844386j),
    ]
    print(f"  {'z':>14} {'Re':>8} {'Im':>8} {'|z|':>10} {'arg z (deg)':>12}"
          f" {'deg in -180..180':>18}")
    for label, z in samples:
        mag, phi = polar(z)
        ang = math.degrees(phi)
        principal = (ang + 180.0) % 360.0 - 180.0
        print(f"  {label:>14} {z.real:>8.3f} {z.imag:>8.3f} {mag:>10.6f}"
              f" {ang:>12.6f} {principal:>18.6f}")
    print("  Round trips exp(i arg z)*|z| reproduce Re and Im to ~1e-16:")
    for label, z in samples:
        mag, phi = polar(z)
        back = mag * cmath.exp(1j * phi)
        print(f"    {label:>14}: |z_back - z| = {abs(back - z):.3e}")

    section("2. Multiplication is rotation and scaling; conjugation is reflection")
    a, b = 2 * cmath.exp(1j * math.radians(30)), 3 * cmath.exp(1j * math.radians(45))
    print(f"  a = {a.real:+.6f}{a.imag:+.6f}i  |a| = {abs(a):.6f}"
          f"  arg a = {math.degrees(cmath.phase(a)):.6f} deg")
    print(f"  b = {b.real:+.6f}{b.imag:+.6f}i  |b| = {abs(b):.6f}"
          f"  arg b = {math.degrees(cmath.phase(b)):.6f} deg")
    print(f"  a*b : |ab| = {abs(a * b):.6f} (=|a||b| = {abs(a) * abs(b):.6f}),"
          f" arg(ab) = {math.degrees(cmath.phase(a * b)):.6f} deg (= 30+45)")
    print(f"  |a/b| = {abs(a / b):.6f}, arg(a/b) ="
          f" {math.degrees(cmath.phase(a / b)):.6f} deg")
    print("  Reflection: arg(conj a) = "
          f"{math.degrees(cmath.phase(a.conjugate())):.6f} deg = -arg a")

    section("3. De Moivre and the nth roots of unity")
    for n in (3, 5, 8):
        roots = [cmath.exp(2j * math.pi * j / n) for j in range(n)]
        total = sum(roots)
        print(f"  n = {n}: sum of roots = {total.real:+.3e}{total.imag:+.3e}i"
              f"   |sum| = {abs(total):.3e}   product of roots ="
              f" {abs(math.prod(roots)):.6f}")
    z = 1 + 1j
    n = 6
    w = abs(z) ** (1.0 / n) * cmath.exp(1j * (cmath.phase(z) + 2 * math.pi * 2) / n)
    print(f"  The {n} roots of {z.real:.0f}{z.imag:+.0f}i (using k = 2 of the"
          f" branch): w = {w.real:+.9f}{w.imag:+.9f}i")
    print(f"    w^{n} = {(w ** n).real:+.9f}{(w ** n).imag:+.9f}i"
          f"   |w^{n} - z| = {abs(w ** n - z):.3e}")

    section("4. Phasor addition: two sinusoids make one, exactly")
    omega = 2 * math.pi * 5.0
    cases = [
        ("equal amplitudes, 90 deg apart", [(3.0, 0.0), (3.0, math.pi / 2)]),
        ("equal amplitudes, 180 deg apart", [(4.0, 0.0), (4.0, math.pi)]),
        ("1 + 1 = 2 in phase", [(1.0, 0.0), (1.0, 0.0)]),
        ("beating in phase to 30 deg", [(1.5, 0.0), (2.0, math.radians(30.0))]),
    ]
    print(f"  {'case':>34} {'A (phasor)':>12} {'phi (deg)':>12}"
          f" {'worst |direct-phasor|':>24}")
    for label, terms in cases:
        amp, phi = sum_phasors(terms)
        res = series_residual(terms, amp, phi, omega)
        print(f"  {label:>34} {amp:>12.6f} {math.degrees(phi):>12.6f}"
              f" {res:>24.3e}")
    print("  The residual is the floating-point noise of two routes to the same")
    print("  trigonometric identity, i.e. of order 1e-16 * the largest term.")

    section("5. Impedance of a series RC network at f = 1 kHz")
    r, c, f = 1000.0, 100e-9, 1000.0
    w = 2 * math.pi * f
    z = rc_impedance(w, r, c)
    mag, phi = abs(z), cmath.phase(z)
    print(f"  R = {r:.0f} ohm, C = {c * 1e9:.0f} nF, f = {f:.0f} Hz")
    print(f"  omega = {w:.6f} rad/s;  1/(omega C) = {1 / (w * c):.6f} ohm")
    print(f"  Z = {z.real:.6f}{z.imag:+.6f}i")
    print(f"  |Z| = {mag:.6f} ohm = sqrt(R^2 + Xc^2) ="
          f" {math.hypot(r, 1 / (w * c)):.6f} ohm")
    print(f"  arg Z = {math.degrees(phi):.6f} deg = -atan(Xc/R) ="
          f" {math.degrees(-math.atan(1 / (w * c) / r)):.6f} deg")
    print(f"  Corner frequency 1/(2 pi R C) = {1 / (2 * math.pi * r * c):.3f} Hz;"
          f" at 1 kHz the current leads the voltage by {abs(math.degrees(phi)):.3f} deg")
    print("  Sweeping the frequency (last column is |I| R / |V|, normalised by")
    print("  the high-frequency asymptote |V|/R):")
    print(f"  {'f (Hz)':>12} {'|Z| (ohm)':>16} {'arg Z (deg)':>14}"
          f" {'|I|R/|V|':>12}")
    for fs in (10.0, 100.0, 1000.0, 1.0 / (2 * math.pi * r * c), 10000.0, 100000.0):
        ws = 2 * math.pi * fs
        zs = rc_impedance(ws, r, c)
        print(f"  {fs:>12.3f} {abs(zs):>16.6f} {math.degrees(cmath.phase(zs)):>14.6f}"
              f" {abs(1 / zs) / (1 / r):>12.6f}")
    ratio = ((abs(1 / rc_impedance(2 * math.pi * 100, r, c)) / (1 / r))
             / (abs(1 / rc_impedance(2 * math.pi * 10, r, c)) / (1 / r)))
    print(f"  ratio of the last column at 100 Hz to 10 Hz: {ratio:.6f}, not 10:")
    print("  the resistive term is already making itself felt.")
    # Check against a direct simulation of V = V0 cos(omega t) with V0 = 1 V.
    # Series R-C driven by a voltage source: R q' + q/C = V(t), first order.
    v0 = 1.0
    cycles, per_cycle = 60, 400
    dt = (2 * math.pi / w) * cycles / (cycles * per_cycle)
    n = cycles * per_cycle
    ys = rk4_first_order(lambda t, q: (v0 * math.cos(w * t) - q / c) / r,
                         y0=0.0, dt=dt, n=n)
    tail = ys[int(0.5 * n):]
    amp_meas, _ = demodulate(tail, w, dt, t0=int(0.5 * n) * dt)
    amp_pred = v0 / (w * mag)
    print("  Direct ODE integration of R q' + q/C = V0 cos(omega t) (charge q):")
    print(f"    measured steady-state charge amplitude = {amp_meas:.9e} C")
    print(f"    V0/(omega |Z|)                        = {amp_pred:.9e} C")
    print(f"    relative difference                   ="
          f" {abs(amp_meas - amp_pred) / amp_pred:.3e}")

    section("6. Damped driven oscillator: impedance algebra versus RK4")
    m, damp, k, f0 = 1.0, 0.6, 25.0, 2.0
    w0 = math.sqrt(k / m)
    for wd in (2.0, 5.0, 9.0):
        zw = m * (w0 ** 2 - wd ** 2) + 1j * damp * wd
        amp_pred = f0 / abs(zw)
        phase_pred = -cmath.phase(zw)
        cycles, per_cycle = 400, 300
        n = cycles * per_cycle
        dt = (2 * math.pi / wd) * cycles / n
        _, xs = rk4_oscillator(m, damp, k, lambda t: f0 * math.cos(wd * t),
                               0.0, 0.0, dt, n)
        start = int(0.6 * n)
        amp_meas, phase_meas = demodulate(xs[start:], wd, dt, t0=start * dt)
        print(f"  omega = {wd:.3f} rad/s ({wd / (2 * math.pi):.6f} Hz):"
              f" predicted amplitude {amp_pred:.9f} m,"
              f" phase {math.degrees(phase_pred):+9.3f} deg")
        print(f"      RK4 projection gives {amp_meas:.9f} m and"
              f" {math.degrees(phase_meas):+9.3f} deg;"
              f" relative amplitude difference"
              f" {abs(amp_meas - amp_pred) / amp_pred:.2e}")
    print(f"  Resonance of the undamped system at omega0 = sqrt(k/m) ="
          f" {w0:.6f} rad/s; with damping the amplitude peak sits at"
          f" sqrt(omega0^2 - c^2/(2 m^2)) ="
          f" {math.sqrt(w0 ** 2 - damp ** 2 / (2 * m ** 2)):.6f} rad/s")


if __name__ == "__main__":
    main()
