"""Coupled oscillators, normal modes and beats, measured.

Run:  python3 coupled_oscillators_demo.py
Requires: Python standard library only.

Companion to lesson 02-03-03. The script:

1. Builds the coupling matrix of a chain of N masses joined by identical
   springs between fixed walls, diagonalises it with the Jacobi method, and
   compares the eigenvalues with the closed form
   omega_n = 2 sqrt(k/m) sin(n pi / (2(N+1))).
2. Checks hermiticity consequences numerically: orthonormality of the mode
   vectors and the residual ||A v - omega^2 v||.
3. Integrates a two-mass chain, shows the energy sloshing from one mass to the
   other, and measures the beat (energy-exchange) period against
   2 pi / (omega2 - omega1).
4. Shows that an initial condition proportional to an eigenvector excites a
   single mode, which therefore never changes shape.

Every number printed below was produced by this script.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# Jacobi eigenvalue algorithm for a real symmetric matrix.
# ----------------------------------------------------------------------
def jacobi_eigen(a, tol=1e-15, max_sweeps=100):
    n = len(a)
    A = [row[:] for row in a]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_sweeps):
        off = math.sqrt(sum(A[i][j] ** 2 for i in range(n) for j in range(n)
                            if i != j))
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(A[p][q]) < 1e-18:
                    continue
                theta = 0.5 * math.atan2(2.0 * A[p][q], A[q][q] - A[p][p])
                c, s = math.cos(theta), math.sin(theta)
                for k in range(n):
                    akp, akq = A[k][p], A[k][q]
                    A[k][p] = c * akp - s * akq
                    A[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = A[p][k], A[q][k]
                    A[p][k] = c * apk - s * aqk
                    A[q][k] = s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = V[k][p], V[k][q]
                    V[k][p] = c * vkp - s * vkq
                    V[k][q] = s * vkp + c * vkq
    return [A[i][i] for i in range(n)], V


def chain_matrix(n, k, m):
    """Chain of n masses, fixed walls at both ends: diag 2k/m, off-diag -k/m."""
    A = [[0.0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = 2.0 * k / m
        if i + 1 < n:
            A[i][i + 1] = A[i + 1][i] = -k / m
    return A


def part1_normal_modes():
    section("1. Normal-mode frequencies of a fixed-end chain")
    k, m = 30.0, 0.5                        # N/m, kg
    for n in (3, 5, 8):
        A = chain_matrix(n, k, m)
        eig, V = jacobi_eigen(A)
        order = sorted(range(n), key=lambda i: eig[i])
        print(f"\nN = {n} masses, k = {k} N/m, m = {m} kg:")
        print(f"  {'n':>3} {'omega_numeric':>15} {'omega_formula':>15} {'rel.diff':>10}")
        for idx, i in enumerate(order, start=1):
            formula = 2.0 * math.sqrt(k / m) * math.sin(idx * math.pi / (2.0 * (n + 1)))
            print(f"  {idx:3d} {math.sqrt(eig[i]):15.9f} {formula:15.9f} "
                  f"{abs(math.sqrt(eig[i]) - formula) / formula:10.2e}")
        # orthonormality and eigen-residual
        worst = 0.0
        for a in range(n):
            for b in range(n):
                dot = sum(V[t][a] * V[t][b] for t in range(n))
                worst = max(worst, abs(dot - (1.0 if a == b else 0.0)))
        print(f"  max |v_i . v_j - delta_ij| over all pairs = {worst:.3e}")
        worst_res = 0.0
        for i in range(n):
            v = [V[t][i] for t in range(n)]
            Av = [sum(A[r][c] * v[c] for c in range(n)) for r in range(n)]
            res = math.sqrt(sum((Av[r] - eig[i] * v[r]) ** 2 for r in range(n)))
            worst_res = max(worst_res, res)
        print(f"  max ||A v - omega^2 v||                       = {worst_res:.3e}")
    print()
    print("  The eigenvalues match the closed form to ~1e-14: the mode shapes of a")
    print("  discrete chain are sine waves, and the frequencies are packed between")
    print("  omega_1 (the fundamental) and 2 sqrt(k/m) (the highest mode, at which")
    print("  neighbouring masses move exactly out of phase).")


def integrate_chain(A, y0, v0, t_end, dt):
    """Second-order explicit integration of y'' = -A y (A symmetric, negative)."""
    n = len(y0)
    steps = int(round(t_end / dt))
    y = list(y0)
    v = list(v0)
    a = [-sum(A[i][j] * y[j] for j in range(n)) for i in range(n)]
    times, ys = [0.0], [list(y)]
    for _ in range(steps):
        for i in range(n):
            y[i] += dt * v[i] + 0.5 * dt * dt * a[i]
        new_a = [-sum(A[i][j] * y[j] for j in range(n)) for i in range(n)]
        for i in range(n):
            v[i] += 0.5 * dt * (a[i] + new_a[i])
        a = new_a
        times.append(times[-1] + dt)
        ys.append(list(y))
    return times, ys


def energy(n, k, m, y, v):
    ke = 0.5 * m * sum(vi * vi for vi in v)
    # spring energy: walls at the ends plus couplings
    pe = 0.5 * k * (y[0] ** 2 + y[-1] ** 2 + sum((y[i + 1] - y[i]) ** 2
                                                 for i in range(n - 1)))
    return ke + pe


def part2_energy_exchange():
    section("2. Two coupled masses: energy exchange and the beat period")
    n, k, m = 2, 30.0, 0.5
    A = chain_matrix(n, k, m)
    eig, V = jacobi_eigen(A)
    order = sorted(range(n), key=lambda i: eig[i])
    w1, w2 = math.sqrt(eig[order[0]]), math.sqrt(eig[order[1]])
    print(f"N = {n}: omega1 = {w1:.9f} rad/s, omega2 = {w2:.9f} rad/s")
    print(f"  check: 2 sqrt(k/m) sin(pi/6) = {2 * math.sqrt(k / m) * math.sin(math.pi / 6):.9f} rad/s")
    print(f"  check: 2 sqrt(k/m) sin(pi/3) = {2 * math.sqrt(k / m) * math.sin(math.pi / 3):.9f} rad/s")
    print(f"  beat frequency |omega2 - omega1| = {w2 - w1:.9f} rad/s, "
          f"beat period = {2 * math.pi / (w2 - w1):.9f} s")

    dt = 1.0e-4
    times, ys = integrate_chain(A, [0.01, 0.0], [0.0, 0.0], 8.0, dt)
    vs = [[(ys[i + 1][j] - ys[i - 1][j]) / (2.0 * dt) for j in range(n)]
          for i in range(1, len(ys) - 1)]
    energies = [energy(n, k, m, ys[i], vs[i - 1]) for i in range(1, len(ys) - 1)]
    e_tot = sum(energies) / len(energies)
    spread = (max(energies) - min(energies)) / e_tot
    print(f"  relative energy drift over 8 s: {spread:.3e}")

    # Time at which mass 2 first reaches its maximum displacement = half a beat
    amp2 = [abs(row[1]) for row in ys]
    # The envelope of |x2| is |sin((omega2-omega1) t/2)|, so it peaks at odd
    # multiples of pi/|omega2-omega1| and returns every beat period. It is only
    # sampled once per fast oscillation, so measure it window by window.
    t_fast = 2.0 * math.pi / (0.5 * (w1 + w2))
    win = int(round(t_fast / dt))
    env_t, env_a = [], []
    for k in range(0, len(amp2) - win, win):
        seg = amp2[k:k + win]
        j = seg.index(max(seg))
        env_t.append(times[k + j])
        env_a.append(max(seg))
    env_peaks = [(env_t[i], env_a[i]) for i in range(1, len(env_a) - 1)
                 if env_a[i] > env_a[i - 1] and env_a[i] >= env_a[i + 1]]
    gaps = [env_peaks[i + 1][0] - env_peaks[i][0] for i in range(len(env_peaks) - 1)]
    print(f"  measured envelope maxima at t = "
          f"{', '.join(f'{t:.3f}' for t, _ in env_peaks[:4])} s ...")
    print(f"  mean spacing of envelope maxima = {sum(gaps) / len(gaps):.4f} s "
          f"(beat period 2 pi/|omega2-omega1| = {2 * math.pi / (w2 - w1):.4f} s)")
    print(f"  predicted envelope maxima at odd multiples of the half beat:")
    print("    " + ", ".join(f"{(2 * m + 1) * math.pi / (w2 - w1):.3f}"
                             for m in range(5)) + " s")
    print(f"  the detector misses the very first one (the envelope rises")
    print(f"  monotonically to it) and resolves the rest to +-{0.5 * t_fast:.3f} s,")
    print(f"  the fast period over which it takes the maximum.")
    print(f"  largest |x2| measured = {max(amp2):.6f} m (theory 0.010000 m)")
    print("  At the envelope maximum the two normal modes are in antiphase and all")
    print("  the energy that started on mass 1 resides on mass 2.")


def part3_single_mode():
    section("3. Exciting one normal mode leaves it invariant")
    n, k, m = 4, 30.0, 0.5
    A = chain_matrix(n, k, m)
    eig, V = jacobi_eigen(A)
    order = sorted(range(n), key=lambda i: eig[i])
    dt = 1.0e-4
    for rank in (0, 1, 2, 3):
        idx = order[rank]
        mode = [V[t][idx] for t in range(n)]
        y0 = [0.01 * c for c in mode]
        times, ys = integrate_chain(A, y0, [0.0] * n, 3.0, dt)
        omega = math.sqrt(eig[idx])
        worst = 0.0
        for ti, row in enumerate(ys):
            t = times[ti]
            predicted = [0.01 * math.cos(omega * t) * c for c in mode]
            worst = max(worst, max(abs(row[j] - predicted[j]) for j in range(n)))
        print(f"  mode {rank + 1}: omega = {omega:.6f} rad/s, "
              f"max deviation from cos(omega t) * mode over 3 s = {worst:.3e}")
    print()
    print("  Each mode oscillates at its own single frequency forever: the")
    print("  normal modes are the coordinates in which the coupled problem is")
    print("  four independent simple harmonic oscillators (lesson 02-03-01).")


if __name__ == "__main__":
    part1_normal_modes()
    part2_energy_exchange()
    part3_single_mode()
