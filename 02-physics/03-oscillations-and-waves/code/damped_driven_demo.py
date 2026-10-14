"""Damped and driven oscillators: resonance and the quality factor, measured.

Run:  python3 damped_driven_demo.py
Requires: Python standard library only.

Companion to lesson 02-03-02. The script:

1. Integrates the free damped oscillator and recovers the damping coefficient
   from the logarithmic decrement of successive peaks.
2. Integrates the driven oscillator at a sweep of frequencies and compares the
   measured steady-state amplitude with

       A(omega) = (F0/m) / sqrt((omega0^2 - omega^2)^2 + (2 beta omega)^2),

   locating the resonance peak at omega_r = sqrt(omega0^2 - 2 beta^2).
3. Measures the half-power bandwidth and compares Q = omega0/(2 beta) with
   Q = omega0/Delta omega and with Q = pi/delta.
4. Computes the phase lag, and shows it passes through 90 degrees at omega0 for
   every damping level - the operational definition of resonance.

Every number printed below was produced by this script.
"""

import math

F0, M, K = 1.0, 1.0, 100.0        # N, kg, N/m
OMEGA0 = math.sqrt(K / M)         # 10 rad/s


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def rk4(f, y, t, dt):
    k1 = f(t, y)
    k2 = f(t + 0.5 * dt, [yi + 0.5 * dt * ki for yi, ki in zip(y, k1)])
    k3 = f(t + 0.5 * dt, [yi + 0.5 * dt * ki for yi, ki in zip(y, k2)])
    k4 = f(t + dt, [yi + dt * ki for yi, ki in zip(y, k3)])
    return [yi + dt * (a + 2.0 * b + 2.0 * c + d) / 6.0
            for yi, a, b, c, d in zip(y, k1, k2, k3, k4)]


def integrate(f, y0, t_end, dt):
    n = int(round(t_end / dt))
    t, y = 0.0, list(y0)
    times, states = [t], [list(y)]
    for _ in range(n):
        y = rk4(f, y, t, dt)
        t += dt
        times.append(t)
        states.append(list(y))
    return times, states


def free_oscillator(beta):
    """x'' + 2 beta x' + omega0^2 x = 0, released from x0 with zero velocity."""
    return lambda t, y: [y[1], -2.0 * beta * y[1] - OMEGA0 ** 2 * y[0]]


def peaks(times, values):
    out = []
    for i in range(1, len(values) - 1):
        if values[i] > values[i - 1] and values[i] >= values[i + 1] and values[i] > 0.0:
            out.append((times[i], values[i]))
    return out


def part1_log_decrement():
    section("1. Free decay: logarithmic decrement and Q")
    print(f"omega0 = sqrt(k/m) = sqrt({K}/{M}) = {OMEGA0:.6f} rad/s")
    print(f"{'beta':>6} {'regime':>16} {'omega_d':>10} {'x0/x1 meas':>11} "
          f"{'delta meas':>11} {'Q=pi/delta':>11} {'Q=w0/2b':>10}")
    for beta, label in ((0.5, "light"), (2.0, "moderate"), (10.0, "critical"),
                        (20.0, "overdamped")):
        if beta < OMEGA0:
            omega_d = math.sqrt(OMEGA0 ** 2 - beta ** 2)
            times, states = integrate(free_oscillator(beta), [0.01, 0.0], 20.0, 1.0e-4)
            xs = [s[0] for s in states]
            pk = peaks(times, xs)
            if len(pk) >= 3:
                ratios = [pk[i][1] / pk[i + 1][1] for i in range(len(pk) - 1)]
                mean_ratio = math.exp(sum(math.log(r) for r in ratios) / len(ratios))
                delta = math.log(mean_ratio)
            else:
                mean_ratio = delta = float("nan")
            print(f"{beta:6.2f} {label:>16} {omega_d:10.5f} {mean_ratio:11.6f} "
                  f"{delta:11.6f} {math.pi / delta:11.4f} {OMEGA0 / (2 * beta):10.4f}")
        else:
            times, states = integrate(free_oscillator(beta), [0.01, 0.0], 5.0, 1.0e-4)
            pk = peaks(times, [s[0] for s in states])
            print(f"{beta:6.2f} {label:>16} {'--':>10} {'--':>11} {'--':>11} "
                  f"{'--':>11} {OMEGA0 / (2 * beta):10.4f}")
    print()
    print("  For light damping, delta = 2 pi beta / omega_d exactly, so")
    print("  Q = pi/delta = omega_d/(2 beta), while Q = omega0/(2 beta) is larger")
    print("  by the factor omega0/omega_d = (1 - 1/(4Q^2))^-1/2. At Q = 10 the")
    print("  two differ by 0.13 per cent; the difference is a genuine, measurable")
    print("  distinction, not rounding.")


def analytic_amplitude(omega, beta):
    return (F0 / M) / math.sqrt((OMEGA0 ** 2 - omega ** 2) ** 2
                                + (2.0 * beta * omega) ** 2)


def driven_amplitude_numeric(omega, beta, dt=2.0e-3):
    """Steady-state amplitude measured after the transient has decayed."""
    f = lambda t, y: [y[1],
                      (F0 / M) * math.cos(omega * t) - 2.0 * beta * y[1]
                      - OMEGA0 ** 2 * y[0]]
    t_end = min(max(20.0 / beta, 40.0), 400.0)
    times, states = integrate(f, [0.0, 0.0], t_end, dt)
    tail = states[len(states) // 2:]
    return max(abs(s[0]) for s in tail)


def part2_resonance_curve():
    section("2. Driven oscillator: measured resonance curve")
    beta = 0.5
    print(f"beta = {beta} rad/s -> Q = omega0/(2 beta) = {OMEGA0 / (2 * beta):.4f}, "
          f"static deflection A(0) = {analytic_amplitude(0.0, beta):.6f} m")
    print(f"{'omega':>9} {'A numeric':>12} {'A analytic':>12} {'rel. diff':>11}")
    for omega in (5.0, 8.0, 9.0, 9.5, 9.8, 10.0, 10.2, 10.5, 11.0, 12.0, 15.0):
        an = driven_amplitude_numeric(omega, beta)
        th = analytic_amplitude(omega, beta)
        print(f"{omega:9.2f} {an:12.6f} {th:12.6f} {(an - th) / th:+11.2e}")

    best, best_omega = -1.0, float("nan")
    omega = 9.0
    while omega <= 10.5:
        a = analytic_amplitude(omega, beta)
        if a > best:
            best, best_omega = a, omega
        omega += 0.0005
    peak_theory = math.sqrt(OMEGA0 ** 2 - 2.0 * beta ** 2)
    print()
    print(f"  analytic peak at omega_r = sqrt(omega0^2 - 2 beta^2) = "
          f"{peak_theory:.5f} rad/s (fine sweep found {best_omega:.5f})")
    print(f"  A_max = {best:.6f} m; A_max/A(0) = "
          f"{best / analytic_amplitude(0.0, beta):.4f} (compare Q = {OMEGA0 / (2 * beta):.4f})")


def part3_bandwidth():
    section("3. Half-power bandwidth: how Q is measured from a spectrum")
    print(f"{'beta':>6} {'Q=w0/2b':>9} {'A_res':>10} {'w_lo':>10} {'w_hi':>10} "
          f"{'Dw':>10} {'w0/Dw':>9} {'Dw/2b':>8}")
    for beta in (0.2, 0.5, 1.0, 2.0):
        w_r = math.sqrt(OMEGA0 ** 2 - 2.0 * beta ** 2)
        target = analytic_amplitude(w_r, beta) / math.sqrt(2.0)

        def solve_rising(lo, hi):
            """A(omega) increases with omega below omega_r."""
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                if analytic_amplitude(mid, beta) < target:
                    lo = mid
                else:
                    hi = mid
            return 0.5 * (lo + hi)

        def solve_falling(lo, hi):
            """A(omega) decreases with omega above omega_r."""
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                if analytic_amplitude(mid, beta) > target:
                    lo = mid
                else:
                    hi = mid
            return 0.5 * (lo + hi)

        w_lo = solve_rising(1.0e-6, w_r)
        w_hi = solve_falling(w_r + 1.0e-9, 100.0)
        dw = w_hi - w_lo
        # Closed form of the half-power frequencies:
        root = math.sqrt(OMEGA0 ** 2 - beta ** 2)
        w_lo_exact = math.sqrt(OMEGA0 ** 2 - 2.0 * beta ** 2 - 2.0 * beta * root)
        w_hi_exact = math.sqrt(OMEGA0 ** 2 - 2.0 * beta ** 2 + 2.0 * beta * root)
        print(f"{beta:6.2f} {OMEGA0 / (2 * beta):9.3f} "
              f"{analytic_amplitude(w_r, beta):10.5f} {w_lo:10.5f} {w_hi:10.5f} "
              f"{dw:10.5f} {OMEGA0 / dw:9.4f} {dw / (2 * beta):8.4f}")
        assert abs(w_lo - w_lo_exact) < 1e-6 and abs(w_hi - w_hi_exact) < 1e-6
    print()
    print("  The bracketed values agree with the closed form")
    print("  omega_{lo,hi} = sqrt(omega0^2 - 2 beta^2 -/+ 2 beta sqrt(omega0^2 - beta^2)).")
    print("  Delta omega = 2 beta + O(beta^2/omega0^2), so Q = omega0/Delta omega")
    print("  recovers Q = omega0/(2 beta) in the high-Q limit and errs by 4.7 per")
    print("  cent at Q = 2.5, where 'high-Q' has already failed.")


def part4_phase_and_power():
    section("4. Phase lag and power absorption (beta = 0.5)")
    beta = 0.5
    print(f"{'omega':>8} {'lag(deg)':>11} {'A (m)':>11} {'mean power (W)':>15}")
    for omega in (0.0, 5.0, 9.0, 10.0, 11.0, 20.0):
        lag = math.degrees(math.atan2(2.0 * beta * omega, OMEGA0 ** 2 - omega ** 2))
        a = analytic_amplitude(omega, beta)
        power = 0.5 * F0 * omega * a * math.sin(math.radians(lag))
        print(f"{omega:8.2f} {lag:11.4f} {a:11.6f} {power:15.6f}")
    print()
    print("  The lag is exactly 90 degrees at omega = omega0 for any beta, and the")
    print("  absorbed power peaks there: at resonance the force is always doing")
    print("  work on the velocity, which is what 'resonance' means operationally.")


if __name__ == "__main__":
    part1_log_decrement()
    part2_resonance_curve()
    part3_bandwidth()
    part4_phase_and_power()
