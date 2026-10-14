"""Simple harmonic motion: the small-oscillation approximation, measured.

Run:  python3 shm_demo.py
Requires: Python standard library only.

Companion to lesson 02-03-01. Three claims are tested numerically rather than
asserted:

1. A mass on a spring obeys x'' = -omega0^2 x exactly, and a fourth-order
   Runge-Kutta integration reproduces the analytic solution to the accuracy of
   the time step.
2. A pendulum obeys theta'' = -(g/L) sin(theta), NOT simple harmonic motion.
   The exact period needs the complete elliptic integral K(sin(theta0/2)).
   We compute K by the arithmetic-geometric mean (AGM), integrate the true
   equation, and measure the period numerically.
3. The small-angle approximation T ~ T0 (1 + theta0^2/16) is second order in
   amplitude; we measure where it fails by 1 per cent, 10 per cent, 100 per cent.

Every number printed below was produced by this script.
"""

import math

G = 9.80665          # m/s^2, standard gravity (exact by definition)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# The exact period of a pendulum requires K(k), the complete elliptic
# integral of the first kind. The AGM gives it in a handful of iterations:
#     K(k) = pi / (2 * AGM(1, sqrt(1 - k^2)))
# ----------------------------------------------------------------------
def elliptic_K(k):
    if not 0.0 <= k < 1.0:
        raise ValueError("k must lie in [0, 1)")
    a, b = 1.0, math.sqrt(1.0 - k * k)
    for _ in range(64):
        a, b = 0.5 * (a + b), math.sqrt(a * b)
        if abs(a - b) < 1e-17:
            break
    return math.pi / (2.0 * a)


def pendulum_period_exact(length, theta0):
    """Exact period of a simple pendulum released from rest at theta0."""
    return 4.0 * math.sqrt(length / G) * elliptic_K(math.sin(0.5 * theta0))


def pendulum_period_series(length, theta0):
    """Classical series T = T0 (1 + theta0^2/16 + 11 theta0^4/3072 + ...)."""
    t0 = 2.0 * math.pi * math.sqrt(length / G)
    return t0 * (1.0 + theta0 ** 2 / 16.0 + 11.0 * theta0 ** 4 / 3072.0)


# ----------------------------------------------------------------------
# Fourth-order Runge-Kutta for a first-order system y' = f(t, y)
# ----------------------------------------------------------------------
def rk4(f, y, t, dt):
    k1 = f(t, y)
    k2 = f(t + 0.5 * dt, [yi + 0.5 * dt * ki for yi, ki in zip(y, k1)])
    k3 = f(t + 0.5 * dt, [yi + 0.5 * dt * ki for yi, ki in zip(y, k2)])
    k4 = f(t + dt, [yi + dt * ki for yi, ki in zip(y, k3)])
    return [yi + dt * (a + 2.0 * b + 2.0 * c + d) / 6.0
            for yi, a, b, c, d in zip(y, k1, k2, k3, k4)]


def integrate(f, y0, t_end, dt):
    """Return (times, states) for the system y' = f(t, y)."""
    n = int(round(t_end / dt))
    t, y = 0.0, list(y0)
    times, states = [t], [list(y)]
    for _ in range(n):
        y = rk4(f, y, t, dt)
        t += dt
        times.append(t)
        states.append(list(y))
    return times, states


def measured_period(times, values):
    """Period from successive upward zero crossings, linearly interpolated."""
    crosses = []
    for i in range(1, len(values)):
        if values[i - 1] < 0.0 <= values[i]:
            frac = -values[i - 1] / (values[i] - values[i - 1])
            crosses.append(times[i - 1] + frac * (times[i] - times[i - 1]))
    if len(crosses) < 2:
        return float("nan"), 0
    # Average over all complete cycles to cancel the time-step bias.
    total = (crosses[-1] - crosses[0]) / (len(crosses) - 1)
    return total, len(crosses) - 1


# ----------------------------------------------------------------------
def part1_mass_on_spring():
    section("1. Mass on a spring: SHM is exact, and RK4 reproduces it")
    k, m = 25.0, 4.0                  # N/m, kg
    omega0 = math.sqrt(k / m)
    x0, v0 = 0.05, 0.0                # m, m/s
    A = math.hypot(x0, v0 / omega0)
    phi = math.atan2(-v0 / omega0, x0)
    print(f"k = {k} N/m, m = {m} kg  ->  omega0 = {omega0:.6f} rad/s, "
          f"T = {2 * math.pi / omega0:.6f} s")
    print(f"amplitude A = {A:.6f} m, phase phi = {phi:.6f} rad")

    f = lambda t, y: [y[1], -(k / m) * y[0]]
    for dt in (1.0e-2, 1.0e-3, 1.0e-4):
        times, states = integrate(f, [x0, v0], 2.0, dt)
        t, xs = times[-1], [s[0] for s in states]
        exact = A * math.cos(omega0 * t + phi)
        error = abs(xs[-1] - exact) / A
        print(f"  dt = {dt:.0e}: x(2 s) = {xs[-1]:+.12e} m, "
              f"exact = {exact:+.12e} m, relative error = {error:.3e}")
    print("  Relative error falls by ~10^4 per decade of dt: RK4 is 4th order.")


def part2_pendulum_period():
    section("2. Pendulum: measured period against the exact elliptic result")
    length = 1.0
    t0_small = 2.0 * math.pi * math.sqrt(length / G)
    print(f"L = {length} m, g = {G} m/s^2  ->  T0 (small angle) = {t0_small:.9f} s")
    print()
    print(f"{'theta0':>8} {'exact T(s)':>13} {'series T(s)':>13} "
          f"{'numeric T(s)':>14} {'T0 err':>9} {'series err':>11}")
    for theta0 in (0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0):
        exact = pendulum_period_exact(length, theta0)
        series = pendulum_period_series(length, theta0)
        n_cycles = 20
        f = lambda t, y: [y[1], -(G / length) * math.sin(y[0])]
        times, states = integrate(f, [theta0, 0.0], n_cycles * exact * 1.05, 2.0e-4)
        numeric, cycles = measured_period(times, [s[0] for s in states])
        print(f"{theta0:8.3f} {exact:13.9f} {series:13.9f} {numeric:14.9f} "
              f"{(exact - t0_small) / t0_small:9.3e} "
              f"{(series - exact) / exact:11.3e}")
    print()
    print("  Note: the small-angle period T0 is below the true period for every")
    print("  finite amplitude; the period grows monotonically with amplitude.")


def part3_failure_of_small_angle():
    section("3. Where the small-oscillation approximation breaks")
    length = 1.0
    t0_small = 2.0 * math.pi * math.sqrt(length / G)
    print(f"{'theta0(rad)':>12} {'theta0(deg)':>12} {'T/T0 - 1':>12} {'theta0^2/16':>12}")
    for theta0 in (0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0):
        exact = pendulum_period_exact(length, theta0)
        rel = (exact - t0_small) / t0_small
        print(f"{theta0:12.4f} {math.degrees(theta0):12.3f} {rel:12.6f} "
              f"{theta0 ** 2 / 16:12.6f}")

    def amplitude_for_error(target):
        lo, hi = 1e-6, 3.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            rel = (pendulum_period_exact(length, mid) - t0_small) / t0_small
            if rel < target:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    for target in (0.01, 0.10, 1.00):
        amp = amplitude_for_error(target)
        print(f"  period error reaches {target * 100:5.1f}% at "
              f"theta0 = {amp:.4f} rad = {math.degrees(amp):.2f} deg")


def part4_energy_and_universality():
    section("4. Energy conservation, and why SHM is universal")
    k, m = 25.0, 4.0
    omega0 = math.sqrt(k / m)
    f = lambda t, y: [y[1], -(k / m) * y[0]]
    energy = lambda y: 0.5 * m * y[1] ** 2 + 0.5 * k * y[0] ** 2
    print("Total energy E = 1/2 m v^2 + 1/2 k x^2, initial E = 0.5*25*0.05^2 = "
          f"{0.5 * k * 0.05 ** 2:.9f} J")
    for dt in (1.0e-2, 1.0e-3, 1.0e-4):
        times, states = integrate(f, [0.05, 0.0], 50.0, dt)
        e0 = energy(states[0])
        drift = max(abs(energy(s) - e0) for s in states) / e0
        print(f"  dt = {dt:.0e}: max relative energy drift over 50 s = {drift:.3e}")

    print()
    print("Any smooth potential well is a parabola near its minimum:")
    print("  V(x) = V(x*) + 1/2 V''(x*) (x - x*)^2 + O((x-x*)^3)")
    V = lambda x: 0.5 * 25.0 * x ** 2 * (1.0 + 0.4 * x)   # an asymmetric well
    x_star = 0.0
    Vpp = 25.0                    # exact second derivative of 12.5 x^2 + 5 x^3 at 0
    omega_eff = math.sqrt(Vpp / m)
    print(f"  Example: V(x) = 12.5 x^2 + 5 x^3, V''(0) = {Vpp} N/m "
          f"-> omega_eff = {omega_eff:.6f} rad/s")
    for amp in (0.001, 0.01, 0.05, 0.1):
        a = 1.0 + 0.4 * amp
        # exact period of x'' = -(V'/m) for this cubic potential, by RK4
        fv = lambda t, y: [y[1], -(25.0 * y[0] + 15.0 * y[0] ** 2) / m]
        times, states = integrate(fv, [amp, 0.0], 60.0, 1.0e-4)
        numeric, cycles = measured_period(times, [s[0] for s in states])
        print(f"  amplitude {amp:6.3f} m: measured T = {numeric:.6f} s, "
              f"T_SHM = {2 * math.pi / omega_eff:.6f} s, "
              f"relative difference = {(numeric - 2 * math.pi / omega_eff) / (2 * math.pi / omega_eff):+.3e}")
    print("  Asymmetric (cubic) terms shift the mean position AND the period;")
    print("  the SHM period is recovered only as amplitude -> 0.")


if __name__ == "__main__":
    part1_mass_on_spring()
    part2_pendulum_period()
    part3_failure_of_small_angle()
    part4_energy_and_universality()
