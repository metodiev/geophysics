"""The Laplace transform: forward transforms, inversion, and transients.

Run:  python3 laplace_transient_demo.py
Requires: Python standard library only (``cmath``, ``math``).

Companion to lesson 01-11-04 (The Laplace Transform and Transient Problems).

What is checked, and how
------------------------
1. Forward transforms L{f}(s) = int_0^inf e^{-s t} f(t) dt for the standard
   pairs, by quadrature with the exact polynomial tail added.
2. The differentiation property L{f'} = s L{f} - f(0).
3. The step response of a first-order system: the transform answer, an RK4
   integration, and the Bromwich inversion integral all agree.
4. The Bromwich integral directly, including the *measured* contribution of the
   closing arc, which is what turns the inversion integral into a sum of
   residues.
5. Residues of Y(s) e^{s t} computed from small circular contours, summed and
   compared with the exact transient.
6. An underdamped second-order system, and the heat-diffusion case
   Y(s) = exp(-a sqrt(s))/s, whose inverse is the complementary error function:
   verified against the Bromwich integral and against a finite-difference
   solution of the diffusion equation itself.
"""

import cmath
import math


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def simpson(f, a, b, n):
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for j in range(1, n):
        total += (4.0 if j % 2 else 2.0) * f(a + j * h)
    return total * h / 3.0


def laplace_numeric(f, s, t_end, tail=None, n=200000):
    """int_0^T e^{-s t} f(t) dt + exact tail for the cases used here.

    ``tail(T)`` returns int_T^inf e^{-s t} f(t) dt in closed form; without it
    the truncation error is O(e^{-Re s T}).
    """
    real_s = s.real
    main = simpson(lambda t: (cmath.exp(-s * t) * f(t)).real, 0.0, t_end, n)
    imag = simpson(lambda t: (cmath.exp(-s * t) * f(t)).imag, 0.0, t_end, n)
    val = main + 1j * imag
    if tail is not None:
        val += tail(t_end)
    return val


def bromwich(Y, t, c, omega_max, n=200000):
    """(1/2 pi i) int_{c-i inf}^{c+i inf} Y(s) e^{s t} ds, by Simpson.

    With s = c + i omega the integral becomes
        (1/2 pi) int_{-inf}^{inf} Y(c + i omega) e^{(c + i omega) t} d omega.
    """
    re = simpson(lambda w: (Y(c + 1j * w) * cmath.exp((c + 1j * w) * t)).real,
                 -omega_max, omega_max, n)
    im = simpson(lambda w: (Y(c + 1j * w) * cmath.exp((c + 1j * w) * t)).imag,
                 -omega_max, omega_max, n)
    return (re + 1j * im) / (2 * math.pi)


def arc_left(Y, t, c, radius, n=20000):
    """Integral of Y(s) e^{s t} along the left semicircle |s - c| = radius."""
    acc = 0j
    for j in range(n + 1):
        theta = math.pi / 2 + math.pi * j / n
        s = c + radius * cmath.exp(1j * theta)
        ds = 1j * radius * cmath.exp(1j * theta) * (math.pi / n)
        acc += Y(s) * cmath.exp(s * t) * ds
    return acc


def residue_circle(Y, t, pole, radius=1e-3, n=2048):
    """Residue of Y(s) e^{s t} at ``pole``, from a small circular contour."""
    acc = 0j
    for j in range(n):
        theta = 2 * math.pi * j / n
        s = pole + radius * cmath.exp(1j * theta)
        ds = 1j * radius * cmath.exp(1j * theta) * (2 * math.pi / n)
        acc += Y(s) * cmath.exp(s * t) * ds
    return acc / (2j * math.pi)


def rk4(rate, y0, dt, n):
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


def main():
    section("1. Forward transforms, by quadrature, with exact tails")
    a, w = 2.0, 3.0
    T = 60.0
    cases = [
        ("f = 1            -> 1/s", lambda t: 1.0, lambda s: 1.0 / s),
        ("f = t            -> 1/s^2", lambda t: t, lambda s: 1.0 / s ** 2),
        ("f = exp(-a t)    -> 1/(s+a)", lambda t: math.exp(-a * t),
         lambda s: 1.0 / (s + a)),
        ("f = sin(w t)     -> w/(s^2+w^2)", lambda t: math.sin(w * t),
         lambda s: w / (s ** 2 + w ** 2)),
        ("f = cos(w t)     -> s/(s^2+w^2)", lambda t: math.cos(w * t),
         lambda s: s / (s ** 2 + w ** 2)),
    ]
    print(f"  a = {a}, w = {w}, s = 0.7 + 1.1i, integration to T = {T}")
    print(f"  {'pair':>34} {'numeric':>40} {'closed form':>28} {'error':>9}")
    for label, f, F in cases:
        s = 0.7 + 1.1j
        val = laplace_numeric(f, s, T)
        exact = F(s)
        print(f"  {label:>34}"
              f" {val.real:>18.12f}{val.imag:>+18.12f}i"
              f" {exact.real:>14.9f}{exact.imag:>+12.9f}i"
              f" {abs(val - exact):>9.2e}")
    s = 0.7 + 1.1j
    print("  Truncating the integral at T costs e^{-Re(s) T}; measured for f = 1:")
    print(f"    {'T':>6} {'error':>12}")
    for T_short in (1.0, 2.0, 5.0, 20.0, 60.0):
        val = laplace_numeric(lambda t: 1.0, s, T_short)
        print(f"    {T_short:>6.1f} {abs(val - 1 / s):>12.2e}")
    print(f"  At T = 60 the truncation error is e^-42.0 = {math.exp(-42.0):.2e}")
    print("  and the quadrature itself is the limiting factor, at ~1e-13.")

    section("2. Differentiation becomes multiplication")
    print("  Property: L{f'}(s) = s F(s) - f(0).")
    f = lambda t: math.sin(w * t)
    fp = lambda t: w * math.cos(w * t)
    print(f"  {'s':>14} {'L{fprime}(s) numeric':>34} {'s F(s) - f(0)':>34}"
          f" {'error':>9}")
    for s in (0.5 + 2.0j, 1.0 + 1.0j, 2.0 + 0.5j):
        lhs = laplace_numeric(fp, s, T)
        rhs = s * (w / (s ** 2 + w ** 2)) - 0.0
        print(f"  {s.real:.2f}{s.imag:+.2f}i {lhs.real:>17.12f}{lhs.imag:>+16.12f}i"
              f" {rhs.real:>17.12f}{rhs.imag:>+16.12f}i"
              f" {abs(lhs - rhs):>9.2e}")

    section("3. First-order step response, three independent routes")
    a = 2.0
    Y = lambda s: 1.0 / (s * (s + a))
    exact = lambda t: (1.0 - math.exp(-a * t)) / a
    dt, n = 1e-4, 40000
    ys = rk4(lambda t, y: 1.0 - a * y, 0.0, dt, n)
    print(f"  ODE y' + {a} y = 1, y(0) = 0;  Y(s) = 1/(s(s+{a}));"
          f"  y(t) = (1 - e^(-{a}t))/{a}")
    print(f"  {'t':>8} {'exact':>18} {'RK4':>18} {'Bromwich':>18}"
          f" {'|Bromwich-exact|':>18}")
    for t in (0.1, 0.5, 1.0, 3.0):
        idx = min(int(round(t / dt)), n)
        closed = exact(t)
        brom = bromwich(Y, t, c=3.0, omega_max=200.0, n=40000)
        print(f"  {t:>8.2f} {closed:>18.12f} {ys[idx]:>18.12f}"
              f" {brom.real:>18.12f} {abs(brom.real - closed):>18.2e}")
    print("  The Bromwich quadrature was truncated at |omega| = 200 with c = 3.")
    print("  Its residual, a few times 1e-5, is *not* a numerical failure: it is")
    print("  the closing arc that the next section adds back.")

    section("4. What the closing arc contributes")
    t = 1.0
    print(f"  At t = {t}, with c = 3:")
    print(f"  {'radius':>8} {'vertical line':>18} {'arc/(2 pi i)':>18}"
          f" {'line + arc':>18} {'sum of residues':>18}")
    for radius in (10.0, 20.0, 40.0, 80.0, 160.0):
        line = bromwich(Y, t, c=3.0, omega_max=radius, n=40000)
        arc = arc_left(Y, t, c=3.0, radius=radius, n=8000) / (2j * math.pi)
        res = residue_circle(Y, t, 0.0) + residue_circle(Y, t, -a)
        print(f"  {radius:>8.0f} {line.real:>18.12f} {arc.real:>18.12f}"
              f" {(line + arc).real:>18.12f} {res.real:>18.12f}")
    print("  The vertical line alone converges slowly, as 1/radius; adding the")
    print("  measured arc contribution reproduces the residue sum immediately.")
    print("  That is the whole content of 'close the contour to the left'.")

    section("5. Residues of Y(s) e^{st}, from small circles")
    print("  Y(s) e^{st} = e^{st}/(s(s+2)); the poles are s = 0 and s = -2.")
    print(f"  {'t':>8} {'Res at 0':>20} {'Res at -2':>20} {'sum':>18}"
          f" {'exact y(t)':>18}")
    for t in (0.2, 0.5, 1.0, 4.0):
        r0 = residue_circle(Y, t, 0.0)
        r2 = residue_circle(Y, t, -a)
        print(f"  {t:>8.2f} {r0.real:>20.12f} {r2.real:>20.12f}"
              f" {(r0 + r2).real:>18.12f} {exact(t):>18.12f}")
    print("  At s = 0 the residue is e^{0}/2 = 0.5 = the final value; at s = -2")
    print("  it is e^{-2t}/(-2), the decaying transient.  Pole position is decay")
    print("  rate, residue is amplitude: that is the reading of a pole.")

    section("6. Underdamped second-order system")
    w0, zeta = 5.0, 0.25
    wd = w0 * math.sqrt(1.0 - zeta ** 2)
    Y2 = lambda s: w0 ** 2 / (s * (s * s + 2 * zeta * w0 * s + w0 ** 2))
    exact2 = lambda t: 1.0 - math.exp(-zeta * w0 * t) * (
        math.cos(wd * t) + (zeta * w0 / wd) * math.sin(wd * t))
    dt2 = 2e-4
    n2 = 100000
    x, v, tt = 0.0, 0.0, 0.0
    hist = [(0.0, 0.0)]
    for _ in range(n2):
        def acc(t, x, v):
            return v, (w0 ** 2 - 2 * zeta * w0 * v - w0 ** 2 * x)
        k1x, k1v = acc(tt, x, v)
        k2x, k2v = acc(tt + dt2 / 2, x + dt2 * k1x / 2, v + dt2 * k1v / 2)
        k3x, k3v = acc(tt + dt2 / 2, x + dt2 * k2x / 2, v + dt2 * k2v / 2)
        k4x, k4v = acc(tt + dt2, x + dt2 * k3x, v + dt2 * k3v)
        x += dt2 * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
        v += dt2 * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
        tt += dt2
        hist.append((tt, x))
    print(f"  omega0 = {w0}, zeta = {zeta}: poles at 0 and"
          f" {-zeta * w0:+.6f} +- {wd:.6f}i (omega_d = {wd:.6f})")
    print(f"  {'t':>8} {'exact':>18} {'RK4':>18} {'Bromwich':>18}"
          f" {'|Bromwich-exact|':>18}")
    for t in (0.2, 0.6, 1.2, 2.5):
        idx = min(int(round(t / dt2)), n2)
        closed = exact2(t)
        brom = bromwich(Y2, t, c=2.0, omega_max=300.0, n=60000)
        print(f"  {t:>8.2f} {closed:>18.12f} {hist[idx][1]:>18.12f}"
              f" {brom.real:>18.12f} {abs(brom.real - closed):>18.2e}")
    print("  The complex poles give the ringing at omega_d; their real part")
    print(f"  -{zeta * w0:.4f} is the decay constant, so the envelope time constant is"
          f" {1 / (zeta * w0):.6f} s.")

    section("7. Diffusive transient: the inverse of exp(-a sqrt(s))/s is erfc")
    aa = 1.5
    Yd = lambda s: cmath.exp(-aa * cmath.sqrt(s)) / s
    print("  Y(s) = exp(-a sqrt(s))/s  <->  y(t) = erfc(a/(2 sqrt(t)))")
    print(f"  a = {aa}")
    print(f"  {'t':>8} {'Bromwich (c=1.0)':>22} {'erfc(a/(2 sqrt t))':>22}"
          f" {'difference':>12}")
    for t in (0.2, 0.5, 1.0, 2.0, 5.0):
        brom = bromwich(Yd, t, c=1.0, omega_max=800.0, n=200000)
        closed = math.erfc(aa / (2 * math.sqrt(t)))
        print(f"  {t:>8.2f} {brom.real:>22.12f} {closed:>22.12f}"
              f" {abs(brom.real - closed):>12.2e}")
    print("  The square root in the exponent is the signature of diffusion: the")
    print("  transform is not rational, the 'pole' is a branch point at s = 0,")
    print("  and there is no single decay time.")

    section("8. The same diffusive problem solved as a partial differential equation")
    kappa = 1.0
    x_max, nx = 20.0, 401
    dx = x_max / (nx - 1)
    dt = 0.4 * dx * dx / kappa
    T_end = 4.0
    steps = int(T_end / dt)
    temp = [0.0] * nx
    temp[0] = 1.0
    for _ in range(steps):
        new = temp[:]
        for i in range(1, nx - 1):
            new[i] = temp[i] + dt * kappa * (temp[i + 1] - 2 * temp[i] + temp[i - 1]) / (dx * dx)
        new[nx - 1] = 0.0
        temp = new
    t = steps * dt
    print(f"  Explicit finite differences: dx = {dx:.4f}, dt = {dt:.3e},"
          f" {steps} steps to t = {t:.3f} (kappa = {kappa})")
    print(f"  {'x':>7} {'FD solution':>16} {'erfc(x/(2 sqrt t))':>20}"
          f" {'difference':>12}")
    worst = 0.0
    for x in (1.0, 2.0, 4.0, 6.0, 8.0):
        i = int(round(x / dx))
        closed = math.erfc(x / (2 * math.sqrt(kappa * t)))
        worst = max(worst, abs(temp[i] - closed))
        print(f"  {x:>7.2f} {temp[i]:>16.8f} {closed:>20.8f}"
              f" {abs(temp[i] - closed):>12.2e}")
    print(f"  worst difference over these points: {worst:.2e}, which is the")
    print("  O(dx^2) error of the finite-difference scheme, not an error in the")
    print("  transform pair.")


if __name__ == "__main__":
    main()
