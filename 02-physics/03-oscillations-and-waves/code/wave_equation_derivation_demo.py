"""Deriving the wave equation from continuum physics, and solving it.

Run:  python3 wave_equation_derivation_demo.py
Requires: Python standard library only.

Companion to lesson 02-03-05. The chain of reasoning tested numerically is:

* a lattice of masses joined by springs obeys an exact dispersion relation,
  omega = c (2/a) sin(k a/2), with c = sqrt(T/mu) the continuum speed;
* in the long-wavelength limit k a -> 0 that relation becomes omega = c k, i.e.
  mu u_tt = T u_xx, and the lattice stops being dispersive;
* the continuum wave equation, solved by the standard explicit finite-difference
  scheme, reproduces d'Alembert's solution with second-order convergence;
* the scheme is stable only for Courant number r = c dt/dx <= 1.

Every number printed below was produced by this script.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# Part 1: the lattice and its continuum limit
# ----------------------------------------------------------------------
def part1_lattice_dispersion():
    section("1. Lattice dispersion relation versus its continuum limit")
    a, c = 1.0, 1.0                     # spacing 1 m, continuum speed 1 m/s
    print(f"lattice spacing a = {a} m, continuum speed c = {c} m/s")
    print(f"{'k a':>7} {'v_ph/c':>10} {'v_g/c':>10} {'omega/(c k) - 1':>18}")
    for ka in (0.01, 0.05, 0.1, 0.3, 0.5, 1.0, 1.5, 2.0, math.pi):
        k = ka / a
        v_ph = c * math.sin(0.5 * ka) / (0.5 * ka)
        v_g = c * math.cos(0.5 * ka)
        omega = c * (2.0 / a) * math.sin(0.5 * ka)
        print(f"{ka:7.3f} {v_ph / c:10.6f} {v_g / c:10.6f} "
              f"{omega / (c * k) - 1.0:18.3e}")
    print()
    print("  At k a -> 0 both speeds tend to c: the lattice becomes a string.")
    print("  At k a = pi (wavelength two spacings) the group velocity vanishes:")
    print("  neighbouring masses move in antiphase and no energy propagates.")


def lattice_step(y, y_old, r2):
    """One leapfrog step of y_j'' = (c/a)^2 (y_{j+1} - 2 y_j + y_{j-1})."""
    n = len(y)
    new = [0.0] * n
    for j in range(1, n - 1):
        new[j] = 2.0 * y[j] - y_old[j] + r2 * (y[j + 1] - 2.0 * y[j] + y[j - 1])
    return new


def part2_packet_speed():
    section("2. Packet speed on the lattice: measured against d(omega)/dk")
    a, c = 1.0, 1.0
    n, start = 3000, 1500.0
    r = 0.5                             # c dt / a
    dt = r * a / c
    print(f"lattice of {n} masses, spacing a = {a} m, c = {c} m/s, r = {r}, "
          f"dt = {dt} s, flight = {600.0 * a / c:.0f} s")
    print(f"{'k0 a':>7} {'v_g formula':>12} {'v_g measured':>13} "
          f"{'rel. error':>11} {'envelope width (a)':>20}")
    for ka0 in (0.1, 0.5, 1.0):
        k0 = ka0 / a
        omega = c * (2.0 / a) * math.sin(0.5 * ka0)
        width = 5.0 * 2.0 * math.pi / k0        # envelope five carrier wavelengths wide

        def field(t):
            return [math.exp(-((j - start) / width) ** 2)
                    * math.cos(k0 * j * a - omega * t) for j in range(n)]

        def envelope(y):
            """Amplitude of the carrier, from y and its slope."""
            return [math.hypot(y[j], (y[j + 1] - y[j - 1]) / (2.0 * a * k0))
                    for j in range(1, n - 1)]

        def peak_position(yy):
            env = envelope(yy)
            i = max(range(len(env)), key=lambda j: env[j])
            y1, y2, y3 = env[i - 1], env[i], env[i + 1]
            shift = 0.5 * (y1 - y3) / (y1 - 2.0 * y2 + y3)
            return (i + 1 + shift) * a

        def width_now(yy):
            env = envelope(yy)
            s = sum(v * v for v in env)
            mean = sum(i * v * v for i, v in enumerate(env)) / s
            var = sum(v * v * (i - mean) ** 2 for i, v in enumerate(env)) / s
            return 2.0 * math.sqrt(var)

        y_old, y = field(0.0), field(dt)
        p1, w1 = peak_position(y), width_now(y)
        steps = int(round(600.0 / dt))
        for _ in range(steps):
            y_old, y = y, lattice_step(y, y_old, r * r)
        p2, w2 = peak_position(y), width_now(y)
        v_measured = (p2 - p1) / (steps * dt)
        v_theory = c * math.cos(0.5 * ka0)
        print(f"{ka0:7.3f} {v_theory:12.6f} {v_measured:13.6f} "
              f"{(v_measured - v_theory) / v_theory:11.3e} "
              f"{w1:8.2f} -> {w2:7.2f}")
    print()
    print("  The packet moves at the group velocity d(omega)/dk and spreads as it")
    print("  goes. The agreement is 0.1 per cent at k a = 0.1, 0.2 per cent at")
    print("  k a = 0.5, and 3 per cent at k a = 1.0, where the packet has spread by")
    print("  half its width and 'the speed of the packet' is itself an approximate")
    print("  notion. Dispersion is a property of the medium, not of waves in")
    print("  general, and measuring it means measuring over a band of frequencies.")


# ----------------------------------------------------------------------
# Part 3: the continuum equation, its exact solution and convergence
# ----------------------------------------------------------------------
def initial_pulse(x, centre=5.0, width=0.5):
    return math.exp(-((x - centre) / width) ** 2)


def exact_dalembert(x, t, c):
    return 0.5 * (initial_pulse(x - c * t) + initial_pulse(x + c * t))


def solve_wave(dx, r, t_end, c=1.0, x_min=0.0, x_max=10.0):
    """Explicit scheme for u_tt = c^2 u_xx, zero initial velocity."""
    nx = int(round((x_max - x_min) / dx)) + 1
    dt = r * dx / c
    steps = int(round(t_end / dt))
    x = [x_min + i * dx for i in range(nx)]
    u_old = [initial_pulse(xi) for xi in x]
    u = [0.0] * nx
    for i in range(1, nx - 1):
        u[i] = u_old[i] + 0.5 * r * r * (u_old[i + 1] - 2.0 * u_old[i] + u_old[i - 1])
    for _ in range(steps - 1):
        u_new = [0.0] * nx
        for i in range(1, nx - 1):
            u_new[i] = (2.0 * u[i] - u_old[i]
                        + r * r * (u[i + 1] - 2.0 * u[i] + u[i - 1]))
        u_old, u = u, u_new
    return x, u, steps * dt


def part3_convergence():
    section("3. Convergence to d'Alembert's solution: measured order")
    c, t_end, r = 1.0, 1.5, 0.5
    print(f"c = {c} m/s, Courant number r = {r}, t_end = {t_end} s, "
          f"initial u(x,0) = exp(-((x-5)/0.5)^2), u_t(x,0) = 0")
    print(f"{'dx (m)':>9} {'dt (s)':>10} {'steps':>7} {'max|error|':>12} "
          f"{'order':>7}")
    prev_err = prev_dx = None
    for dx in (0.05, 0.025, 0.0125, 0.00625, 0.003125):
        x, u, t_actual = solve_wave(dx, r, t_end, c)
        err = max(abs(u[i] - exact_dalembert(x[i], t_actual, c))
                  for i in range(len(x)))
        if prev_err is None:
            order = float("nan")
        else:
            order = math.log(prev_err / err) / math.log(prev_dx / dx)
        print(f"{dx:9.5f} {r * dx / c:10.6f} {int(round(t_end / (r * dx / c))):7d} "
              f"{err:12.3e} {order:7.3f}")
        prev_err, prev_dx = err, dx
    print()
    print("  Halving dx quarters the error: the scheme is second order in space and")
    print("  time, so a tenfold finer grid buys a hundredfold accuracy - and costs")
    print("  ten times more work in one dimension, a hundred in two, a thousand in")
    print("  three. This is why 3-D elastic modelling is a supercomputer problem.")


def part4_cfl():
    section("4. Stability: the Courant condition r = c dt/dx <= 1")
    c = 1.0
    dx = 0.02
    steps = 200
    print("Narrow initial pulse (width = one grid interval), so the initial data")
    print("contains the highest wavenumbers the grid can carry - and those are the")
    print("wavenumbers that decide stability.")
    print(f"{'r':>6} {'dt (s)':>9} {'max|u| at t=0':>14} "
          f"{'max|u| after 200 steps':>23} {'growth/step':>12} "
          f"{'theory':>12}")
    for r in (0.5, 0.9, 1.0, 1.05, 1.2):
        dt = r * dx / c
        x = [i * dx for i in range(501)]
        u_old = [math.exp(-((xi - 5.0) / dx) ** 2) for xi in x]
        u = [0.0] * len(x)
        for i in range(1, len(x) - 1):
            u[i] = u_old[i] + 0.5 * r * r * (u_old[i + 1] - 2.0 * u_old[i]
                                             + u_old[i - 1])
        peak0 = max(abs(v) for v in u)
        for _ in range(steps):
            u_new = [0.0] * len(x)
            for i in range(1, len(x) - 1):
                u_new[i] = (2.0 * u[i] - u_old[i]
                            + r * r * (u[i + 1] - 2.0 * u[i] + u[i - 1]))
            u_old, u = u, u_new
        peak = max(abs(v) for v in u)
        growth = (peak / peak0) ** (1.0 / steps)
        if r > 1.0:
            a_nyq = 2.0 * r * r - 1.0        # -a at theta = pi
            theory = a_nyq + math.sqrt(a_nyq * a_nyq - 1.0)
        else:
            theory = 1.0
        print(f"{r:6.2f} {dt:9.5f} {peak0:14.6f} {peak:23.6e} "
              f"{growth:12.6f} {theory:12.6f}")
    print()
    print("  At r = 1 the scheme is exact for this initial data: the numerical")
    print("  characteristics coincide with the grid characteristics, and the pulse")
    print("  is transported without error. Above r = 1 the amplification factor of")
    print("  the Nyquist wavenumber becomes |2r^2 - 1| + sqrt((2r^2 - 1)^2 - 1) per")
    print("  step, as the last column confirms to about 2 per cent: the small deficit")
    print("  is because the fastest-growing mode needs a few steps to dominate the")
    print("  initial data. The solution grows without bound: the numerical scheme,")
    print("  not the physics, has become unstable.")
    print("  In two and three dimensions the limit tightens to r <= 1/sqrt(2) and")
    print("  r <= 1/sqrt(3) for this five-point stencil.")


def part5_measured_speed():
    section("5. Speed measured from the numerical solution")
    c, t_end, r = 1.0, 1.0, 0.5
    dx = 0.01
    x, u, t_actual = solve_wave(dx, r, t_end, c)
    # Peak of the right-going pulse, by parabolic interpolation on the grid.
    best_i = max(range(len(x) // 2, len(x)), key=lambda i: u[i])
    x1, x2, x3 = x[best_i - 1], x[best_i], x[best_i + 1]
    y1, y2, y3 = u[best_i - 1], u[best_i], u[best_i + 1]
    denom = (y1 - 2.0 * y2 + y3)
    shift = 0.5 * (y1 - y3) / denom
    x_peak = x2 + shift * dx
    v_measured = (x_peak - 5.0) / t_actual
    print(f"right-going pulse peak at x = {x_peak:.6f} m after t = "
          f"{t_actual:.6f} s")
    print(f"speed = (x_peak - 5)/t = {v_measured:.9f} m/s "
          f"(input c = {c:.9f} m/s, error {abs(v_measured - c) / c:.2e})")
    print()
    print("  Plane waves verify the equation itself: substituting")
    print("  u = A cos(kx - omega t) into u_tt = c^2 u_xx gives")
    for k in (1.0, 10.0, 100.0):
        omega = c * k
        u_tt = -omega ** 2
        c2_u_xx = -c ** 2 * k ** 2
        print(f"    k = {k:6.1f} 1/m: u_tt = {u_tt:14.6f}, "
              f"c^2 u_xx = {c2_u_xx:14.6f}, ratio = {u_tt / c2_u_xx:.12f}")
    print("  The ratio is 1 for every k: the equation is non-dispersive by")
    print("  construction, so it is the right model for a homogeneous elastic")
    print("  solid at wavelengths long compared with the microstructure (02-04).")


if __name__ == "__main__":
    part1_lattice_dispersion()
    part2_packet_speed()
    part3_convergence()
    part4_cfl()
    part5_measured_speed()
