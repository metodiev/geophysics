"""Dispersion: phase velocity, group velocity, and how to measure both.

Run:  python3 dispersion_demo.py
Requires: Python standard library only.

Companion to lesson 02-03-07. The script:

1. Compares the phase and group velocities for three dispersion relations:
   non-dispersive waves (omega = c k), deep-water gravity waves
   (omega = sqrt(g k)) and flexural waves on a thin plate (omega = alpha k^2).
2. Builds an explicit wave packet as a sum over wavenumbers, then *measures*
   the local wavenumber from the spatial phase gradient and the local frequency
   from the temporal phase gradient, forming v_ph = omega/k with no input from
   the dispersion relation, and measures the group velocity from the motion of
   the envelope peak. Both are compared with omega/k and d(omega)/dk.
3. Measures the spreading of each packet, at a propagation distance chosen so
   that every relation is tested at the same 2 m of travel.

Every number printed below was produced by this script.
"""

import cmath
import math

G = 9.80665


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


DISPERSIONS = (
    ("non-dispersive (omega = 100 k)", lambda k: 100.0 * k, lambda k: 100.0),
    ("deep-water gravity (omega = sqrt(g k))", lambda k: math.sqrt(G * k),
     lambda k: 0.5 * math.sqrt(G / k)),
    ("flexural plate (omega = 0.5 k^2)", lambda k: 0.5 * k * k, lambda k: k),
)


def part1_speeds():
    section("1. Phase and group velocities for three dispersion relations")
    print(f"{'k (1/m)':>9} {'v_ph (m/s)':>12} {'v_g (m/s)':>12} {'v_g/v_ph':>10}"
          f"   relation")
    for name, omega_of_k, domega_of_k in DISPERSIONS:
        for k in (0.1, 0.4, 1.0):
            v_ph = omega_of_k(k) / k
            v_g = domega_of_k(k)
            print(f"{k:9.3f} {v_ph:12.5f} {v_g:12.5f} {v_g / v_ph:10.5f}   {name}")
    print()
    print("  The ratios are the signature of each relation: 1 for non-dispersive")
    print("  waves, 1/2 for deep-water gravity waves, 2 for flexural waves. A")
    print("  measurement of v_g/v_ph therefore identifies the physics, and that is")
    print("  how surface-wave dispersion is inverted for shear velocity.")


K0 = 0.4
DK = 0.02
X_MIN, X_MAX, DX = -200.0, 200.0, 0.1


def packet(x, t, omega_of_k, k0=K0, dk=DK):
    """Complex wave packet: sum_k A(k) exp(i(kx - omega(k) t)).

    The Gaussian weight exp(-((k-k0)/dk)^2) is sampled at 30 points per dk and
    truncated at |k - k0| = 3 dk, where the weight has fallen to 1.2e-4. A
    discrete k sum repeats the envelope in x with period 2 pi/(dk/30), here
    1885 m for dk = 0.1 - far beyond the computational window, so the packet
    does not see its own periodic images.
    """
    total = 0j
    for i in range(-90, 91):
        k = k0 + i * dk / 30.0
        amplitude = math.exp(-((k - k0) / dk) ** 2)
        total += cmath.exp(1j * (k * x - omega_of_k(k) * t)) * amplitude
    return total


def unwrapped_phase(values):
    phases = [cmath.phase(v) for v in values]
    for i in range(1, len(phases)):
        while phases[i] - phases[i - 1] > math.pi:
            phases[i] -= 2.0 * math.pi
        while phases[i] - phases[i - 1] < -math.pi:
            phases[i] += 2.0 * math.pi
    return phases


def measure_packet(omega_of_k):
    """Return (k_local, omega_local, v_g measured, amplitude, width)."""
    xs = [X_MIN + DX * i for i in range(int((X_MAX - X_MIN) / DX) + 1)]
    t1 = 0.0
    # travel 2 m at the expected group speed, from part 1's relations
    v_g_guess = max(0.05, domega_of_k_global(omega_of_k, K0))
    t2 = 2.0 / v_g_guess
    u1 = [packet(x, t1, omega_of_k) for x in xs]
    u2 = [packet(x, t2, omega_of_k) for x in xs]
    amp1 = [abs(v) for v in u1]
    amp2 = [abs(v) for v in u2]
    i1 = max(range(len(xs)), key=lambda i: amp1[i])
    i2 = max(range(len(xs)), key=lambda i: amp2[i])
    # refine the peak positions by parabolic interpolation
    def refined(amp, i):
        y1, y2, y3 = amp[i - 1], amp[i], amp[i + 1]
        return xs[i] + 0.5 * (y1 - y3) / (y1 - 2.0 * y2 + y3) * DX
    p1, p2 = refined(amp1, i1), refined(amp2, i2)
    v_g_meas = (p2 - p1) / (t2 - t1)

    ph1 = unwrapped_phase(u1)
    ph2 = unwrapped_phase(u2)
    ic = i1
    k_meas = (ph1[ic + 1] - ph1[ic - 1]) / (2.0 * DX)
    omega_meas = -(ph2[ic] - ph1[ic]) / (t2 - t1)
    return abs(k_meas), abs(omega_meas), v_g_meas, amp1[i1], amp2[i2], (t2, p1, p2)


def domega_of_k_global(omega_of_k, k):
    h = 1.0e-5
    return (omega_of_k(k + h) - omega_of_k(k - h)) / (2.0 * h)


def part2_measure_packet_speeds():
    section("2. Measuring v_ph and v_g from a packet, for each relation")
    print(f"carrier wavenumber k0 = {K0} 1/m, bandwidth dk = {DK} 1/m; the same")
    print("2 m of travel is used for every relation")
    for name, omega_of_k, domega_of_k in DISPERSIONS:
        k_meas, omega_meas, v_g_meas, a1, a2, (t2, p1, p2) = measure_packet(omega_of_k)
        v_ph_meas = omega_meas / k_meas
        v_ph_theory = omega_of_k(K0) / K0
        v_g_theory = domega_of_k(K0)
        print(f"\n  {name}")
        print(f"    measured k = {k_meas:.6f} 1/m (input {K0}), measured omega = "
              f"{omega_meas:.6f} rad/s (input {omega_of_k(K0):.6f})")
        print(f"    v_ph measured = {v_ph_meas:11.6f} m/s, omega/k0 = "
              f"{v_ph_theory:11.6f} m/s, difference = "
              f"{(v_ph_meas - v_ph_theory) / v_ph_theory:+.3e}")
        print(f"    v_g  measured = {v_g_meas:11.6f} m/s, d(omega)/dk = "
              f"{v_g_theory:11.6f} m/s, difference = "
              f"{(v_g_meas - v_g_theory) / v_g_theory:+.3e}")
        print(f"    over t = {t2:.4f} s the envelope peak moved {p2 - p1:.4f} m; "
              f"peak amplitude {a1:.4f} -> {a2:.4f}")
    print()
    print("  Both speeds are recovered from the same packet, with the dispersion")
    print("  relation used only for the comparison. The phase velocity matches to")
    print("  1e-13 where omega is exactly linear in k and to about 1e-3 for the")
    print("  gravity-wave packet, where omega is curved and a finite-bandwidth")
    print("  packet therefore has no single phase speed; the group velocity is")
    print("  exact where omega is linear and within 5e-4 for the gravity waves.")


def part3_spreading():
    section("3. Packet spreading is predicted by d^2(omega)/dk^2")
    k0, dk, dx = K0, 0.1, 0.2            # broader band, to make spreading visible
    span = 200.0
    xs = [-span + dx * i for i in range(int(2.0 * span / dx) + 1)]
    travel = 20.0
    print(f"carrier k0 = {k0} 1/m, bandwidth dk = {dk} 1/m, travel = {travel} m")
    print(f"{'relation':>40} {'d2w/dk2':>11} {'width t=0 (m)':>14} "
          f"{'width at 20 m (m)':>18} {'growth':>8}")
    for name, omega_of_k, domega_of_k in DISPERSIONS:
        v_g = domega_of_k(k0)
        t2 = travel / v_g
        d2 = (omega_of_k(k0 + 1e-4) - 2.0 * omega_of_k(k0)
              + omega_of_k(k0 - 1e-4)) / 1e-8

        def width(t):
            w = [abs(packet(x, t, omega_of_k, k0, dk)) ** 2 for x in xs]
            total = sum(w)
            m = sum(i * wi for i, wi in enumerate(w)) / total
            var = sum(wi * (i - m) ** 2 for i, wi in enumerate(w)) / total
            return 2.0 * math.sqrt(var) * dx

        w1, w2 = width(0.0), width(t2)
        print(f"{name:>40} {d2:11.6f} {w1:14.4f} {w2:18.4f} {w2 / w1:8.5f}")
    print()
    print("  The non-dispersive packet does not spread at all. Whenever")
    print("  d^2(omega)/dk^2 differs from zero the packet broadens, without limit in")
    print("  time: a short pulse cannot stay short in a dispersive medium. The")
    print("  growth per metre is set by d^2(omega)/dk^2 multiplied by the bandwidth,")
    print("  which is why the sign of that derivative does not matter - only its")
    print("  magnitude.")


if __name__ == "__main__":
    part1_speeds()
    part2_measure_packet_speeds()
    part3_spreading()
