#!/usr/bin/env python3
"""Consistency, stability and the Lax equivalence theorem, measured.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python consistency_stability_demo.py

All models and data in this module are SYNTHETIC.  The advection problem below
is a chosen teaching model, not a measurement of any physical system.

Contents
--------
1. Consistency: the residual of the scheme applied to the exact solution,
   compared with its exact Taylor value.
2. Stability: the amplification factor of the upwind scheme, obtained from the
   exact eigenmode, against the analytic |G|.
3. The Lax equivalence theorem in action: a stable consistent scheme converges
   at a measurable rate; an unstable one diverges at a measurable rate.
4. A consistent scheme that is unconditionally unstable (central difference in
   space, forward Euler in time).
5. Exactness at CFL = 1: a corner case where the stable scheme has zero error.
"""

import numpy as np

RNG = np.random.default_rng(20261014)
A_VEL = 1.0          # advection speed of the SYNTHETIC model, in m/s


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def exact(x, t, a=A_VEL):
    """Exact solution of u_t + a u_x = 0 on [0, 1] with u(x, 0) = sin(2 pi x)."""
    return np.sin(2.0 * np.pi * (x - a * t))


def upwind_step(u, C):
    """One step of the upwind scheme on a periodic grid, C = a dt/h."""
    return u - C * (u - np.roll(u, 1))


def consistency():
    """Residual of the upwind operator applied to the exact solution."""
    print("u_t + a u_x = 0 on [0, 1] with u(x,0) = sin(2 pi x), a = 1 m/s,")
    print("exact u = sin(2 pi (x - t)); C = a dt/h = 0.5 fixed")
    x0, t0, C = 0.15, 0.30, 0.5
    pred = 2.0 * np.pi ** 2 * A_VEL * (1.0 - C) * np.sin(2.0 * np.pi * (x0 - A_VEL * t0))
    print(f"{'h (m)':>10} {'dt (s)':>10} {'R (1/s)':>16} {'R/h (1/m/s)':>16} "
          f"{'exact limit':>16}")
    for h in (0.05, 0.025, 0.0125, 0.00625, 0.003125):
        dt = C * h / A_VEL
        R = ((exact(x0, t0 + dt) - exact(x0, t0)) / dt
             + A_VEL * (exact(x0, t0) - exact(x0 - h, t0)) / h)
        print(f"{h:>10.5f} {dt:>10.5f} {R:>16.8e} {R / h:>16.8f} "
              f"{pred:>16.8f}   (R/h - limit)/h = {(R / h - pred) / h:+.4f}")
    print("the residual vanishes as h -> 0 while R/h approaches the Taylor value")
    print("(a/2)(1-C) * 4 pi^2 sin(2 pi (x-t)); the difference falls like h, which")
    print("is consistency of a first-order scheme")


def amplification(C, theta):
    """Exact amplification factor of upwind for a mode exp(i theta j)."""
    g = 1.0 - C * (1.0 - np.exp(-1j * theta))
    return g


def stability():
    """Growth per step of the exact eigenmode against |G|."""
    print("periodic advection, initial state a pure eigenmode of amplitude 1e-6,")
    print("64 cells; 20 steps while |G| < 1 so the amplitude stays above round-off,")
    print("200 steps where it grows")
    print(f"{'C':>7} {'theta/pi':>9} {'predicted |G|':>14} {'steps':>6} "
          f"{'measured growth/step':>21} {'amplitude ratio':>17}")
    for C, frac in ((0.5, 0.5), (0.5, 1.0), (0.9, 1.0), (1.0, 0.5),
                    (1.0, 1.0), (1.2, 1.0), (1.5, 1.0)):
        theta = frac * np.pi
        g = abs(amplification(C, theta))
        n = 1 if g == 0.0 else (200 if g > 1.0 else 20)
        j = np.arange(64)
        u = 1e-6 * np.exp(1j * theta * j)
        for _ in range(n):
            u = upwind_step(u, C)
        final = np.max(np.abs(u))
        if final == 0.0:
            growth = "removed in one step"
        else:
            growth = f"{(final / 1e-6) ** (1.0 / n):.8f}"
        print(f"{C:>7.3f} {frac:>9.2f} {g:>14.8f} {n:>6} "
              f"{growth:>21} {final / 1e-6:>17.6e}")
    print("C = 0.5 annihilates the theta = pi mode in a single step: G = 0 exactly")
    print("for that mode, because 1 - C(1 - e^-i pi) = 1 - 0.5(2) = 0.  The measured")
    print("relative amplitude after one step is round-off, not a slow decay.")
    print("For C > 1 the theta = pi mode grows by |G| = sqrt(1 + 4C(C-1)) per step:")
    for C in (1.2, 1.5):
        pred = np.sqrt(1.0 + 4.0 * C * (C - 1.0))
        meas = abs(amplification(C, np.pi))
        print(f"  C = {C:.2f}: |G| = sqrt(1 + 4C(C-1)) = {pred:.10f}, "
              f"|1 - C(1-e^-i pi)| = {meas:.10f}")


def lax_equivalence():
    """Stable-consistent converges; unstable diverges; both at a known rate."""
    print("refinement with C = 0.5 fixed, integrated to t = 2 s (two periods)")
    print(f"{'h (m)':>10} {'steps':>8} {'Linf error':>16} {'observed order':>16}")
    t_end, C = 2.0, 0.5
    prev = None
    for h in (0.05, 0.025, 0.0125, 0.00625, 0.003125):
        n = int(round(1.0 / h))
        x = np.arange(n) * h
        u = exact(x, 0.0)
        dt = C * h / A_VEL
        steps = int(round(t_end / dt))
        for _ in range(steps):
            u = upwind_step(u, C)
        err = np.max(np.abs(u - exact(x, steps * dt)))
        order = np.nan if prev is None else np.log(prev / err) / np.log(2.0)
        print(f"{h:>10.5f} {steps:>8} {err:>16.6e} {order:>16.6f}")
        prev = err
    print("consistent, stable, and converging at the first-order rate that the")
    print("truncation error of section 1 predicts.")

    print("\nthe same scheme at C = 1.2 (unstable), 200 steps, h = 0.05 m")
    g = abs(amplification(1.2, np.pi))
    j = np.arange(64)
    u = 1e-6 * np.exp(1j * np.pi * j)
    for _ in range(200):
        u = upwind_step(u, 1.2)
    print(f"  predicted growth |G|^200 = {g ** 200:.3e} with |G| = {g:.8f}")
    print(f"  measured growth = {np.max(np.abs(u)) / 1e-6:.3e}")

    print("\nexactness at C = 1: upwind reduces to a shift by exactly one cell")
    h = 0.01
    x = np.arange(int(round(1.0 / h))) * h
    u = exact(x, 0.0)
    for _ in range(100):
        u = upwind_step(u, 1.0)
    print(f"  after 100 steps at C = 1: Linf error = "
          f"{np.max(np.abs(u - exact(x, 100 * h))):.3e}")
    print("  a stable scheme need not be accurate, but this one is exact in the")
    print("  special case where the Courant number is exactly one.")


def consistent_but_unstable():
    """Central difference in space with forward Euler in time."""
    print("u^{n+1} = u^n - (C/2)(u_{j+1} - u_{j-1}) : consistent to order 2 in h,")
    print("but |G|^2 = 1 + C^2 sin^2(theta) > 1 for every mode with sin(theta) != 0")
    theta = np.pi / 2.0
    print(f"{'C':>7} {'predicted |G|':>14} {'measured growth/step':>21} "
          f"{'steps to grow 1e6x':>20}")
    for C in (0.25, 0.5, 1.0):
        n = 200
        j = np.arange(64)
        u = 1e-6 * np.exp(1j * theta * j)
        for _ in range(n):
            u = u - 0.5 * C * (np.roll(u, -1) - np.roll(u, 1))
        growth = (np.max(np.abs(u)) / 1e-6) ** (1.0 / n)
        g = np.sqrt(1.0 + C ** 2 * np.sin(theta) ** 2)
        print(f"{C:>7.3f} {g:>14.8f} {growth:>21.8f} "
              f"{np.log(1e6) / np.log(g):>20.1f}")
    print("this scheme is consistent (the truncation error vanishes with h and dt)")
    print("and unconditionally unstable: Lax equivalence therefore forbids")
    print("convergence, and the growth rate is predicted by |G|, not fitted.")


def main():
    section("1. Consistency: residual of the scheme on the exact solution")
    consistency()

    section("2. Stability: exact eigenmode growth per step")
    stability()

    section("3. Lax equivalence: convergence versus divergence at a known rate")
    lax_equivalence()

    section("4. Consistent does not imply stable")
    consistent_but_unstable()


if __name__ == "__main__":
    main()
