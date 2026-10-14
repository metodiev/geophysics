#!/usr/bin/env python3
"""Explicit and implicit time stepping: measured stability limits, measured
orders of accuracy in time, and what an implicit scheme does and does not fix.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_time_stepping_demo.py

All models and data in this module are SYNTHETIC.  The teaching problem below is
a chosen model problem with a closed-form solution.

Contents
--------
1. Explicit diffusion: the stability limit r = 1/2, measured and predicted.
2. Orders of accuracy in time against the exact semi-discrete solution.
3. Cost: steps and storage for explicit versus implicit time stepping.
4. The CFL limit of the explicit wave scheme and its growth rate beyond it.
5. The trapezoidal (average-acceleration) scheme: stable at any C, accurate at
   no C.
"""

import numpy as np

RNG = np.random.default_rng(20261014)
ALPHA = 1.0          # thermal diffusivity, m^2/s
C_WAVE = 1.0         # wave speed, m/s
L = 1.0              # domain length, m


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def laplacian_matrix(n, h):
    """A = second difference / h^2 with Dirichlet zeros at both ends."""
    A = (np.diag(-2.0 * np.ones(n)) + np.diag(np.ones(n - 1), 1)
         + np.diag(np.ones(n - 1), -1)) / h ** 2
    return A


def diffusion_stability():
    print("u_t = alpha u_xx, periodic grid of 64 cells, FTCS: r = alpha dt/h^2")
    print("the checkerboard is an exact eigenmode with G = 1 - 4r, so the")
    print("measured growth per step must reproduce |1-4r| digit for digit")
    print(f"{'r':>8} {'|1-4r| predicted':>18} {'measured growth/step':>22} "
          f"{'amplitude after 200':>20}")
    n = 64
    for r in (0.25, 0.49, 0.5, 0.501, 0.55, 0.75):
        u = np.array([1.0 if j % 2 == 0 else -1.0 for j in range(n)])
        amp0 = np.max(np.abs(u))
        for _ in range(200):
            u = u + r * (np.roll(u, -1) - 2.0 * u + np.roll(u, 1))
        final = np.max(np.abs(u)) / amp0
        growth = final ** (1.0 / 200.0)
        print(f"{r:>8.3f} {abs(1.0 - 4.0 * r):>18.8f} {growth:>22.8f} "
              f"{final:>20.6e}")
    print("r = 1/2 is exactly neutral for the highest mode: the mode neither")
    print("grows nor decays, which is the boundary of stability, not a good scheme.")
    print("\nthe limit scales with the dimension: dt <= h^2/(2 alpha d), so for")
    print("h = 1/100 m and alpha = 1 m^2/s the step count to reach t = 1 s is")
    for d in (1, 2, 3):
        print(f"  {d}-D: dt <= {1.0 / (2.0 * d * 100 ** 2):.3e} s, "
              f"steps >= {2 * d * 100 ** 2:>7d}")


def semidiscrete_exact(n, h, u0, t):
    """Exact solution of the space-discretised heat equation at time t."""
    A = laplacian_matrix(n, h)
    lam, V = np.linalg.eigh(A)
    c = V.T @ u0
    return V @ (c * np.exp(lam * t))


def time_orders():
    print("time-integration error measured against the EXACT solution of the")
    print("space-discretised system, so the order in time is isolated from h")
    n = 64
    h = L / (n + 1)
    x = np.arange(1, n + 1) * h
    u0 = np.sin(np.pi * x)
    T = 0.1
    A = laplacian_matrix(n, h)
    print(f"n = {n} interior nodes, h = {h:.6f} m, T = {T} s; the explicit")
    print(f"stability limit at this h is dt <= 0.5 h^2/alpha = "
          f"{0.5 * h ** 2 / ALPHA:.3e} s")
    print(f"{'scheme':>16} {'dt':>12} {'steps':>7} {'L2 error':>16} "
          f"{'observed order':>16}")

    def run(kind, dt):
        steps = int(round(T / dt))
        u = u0.copy()
        for _ in range(steps):
            if kind == "explicit":
                u = u + dt * (A @ u)
            elif kind == "be":
                u = np.linalg.solve(np.eye(n) - dt * A, u)
            else:
                u = np.linalg.solve(np.eye(n) - 0.5 * dt * A,
                                    (np.eye(n) + 0.5 * dt * A) @ u)
        # the exact semi-discrete solution is evaluated at the time actually
        # reached, steps*dt, so that no time-mismatch error enters the comparison
        t_reached = steps * dt
        err = np.linalg.norm(u - semidiscrete_exact(n, h, u0, t_reached)) * np.sqrt(h)
        return err, steps

    for name, kind, dts in (
        ("FTCS explicit", "explicit",
         (1.2e-4, 6.0e-5, 3.0e-5, 1.5e-5, 7.5e-6)),
        ("backward Euler", "be", (1.0e-2, 5.0e-3, 2.5e-3, 1.25e-3, 6.25e-4)),
        ("Crank-Nicolson", "cn", (1.0e-2, 5.0e-3, 2.5e-3, 1.25e-3, 6.25e-4)),
    ):
        prev = None
        for dt in dts:
            err, steps = run(kind, dt)
            order = "n/a" if prev is None else f"{np.log(prev / err) / np.log(2.0):.4f}"
            print(f"{name:>16} {dt:>12.7f} {steps:>7} {err:>16.6e} {order:>16}")
            prev = err
    print("all three are second-order in space, and their time orders are 1, 1")
    print("and 2 respectively; the order is a property of the time")
    print("discretisation alone, which is why it is measured this way.")


def cost():
    print("cost to integrate the same problem to T = 0.1 s:")
    print(f"{'scheme':>16} {'dt (s)':>10} {'steps':>8} {'work per step':>16}")
    n = 64
    h = L / (n + 1)
    r_max = 0.5
    dt_explicit = r_max * h ** 2 / ALPHA
    print(f"{'FTCS explicit':>16} {dt_explicit:>10.6f} "
          f"{int(round(0.1 / dt_explicit)):>8} {'one mat-vec':>16}")
    for dt in (1e-2, 1e-3):
        print(f"{'backward Euler':>16} {dt:>10.6f} {int(round(0.1 / dt)):>8} "
              f"{'tridiagonal solve':>16}")
    print(f"the explicit step is limited by the grid, the implicit step is limited")
    print(f"only by accuracy: at h = {h:.5f} m the explicit step is "
          f"{dt_explicit:.2e} s,")
    print("so the implicit scheme needs thousands of times fewer steps at the")
    print("price of a linear solve in each one.  In three dimensions the ratio")
    print("grows again by a factor of three, because dt <= h^2/(2 alpha d).")


def wave_cfl():
    print("u_tt = c^2 u_xx, leapfrog, periodic 64 cells, started in the pure")
    print("eigenmode of the highest grid mode: the state admits only one root")
    print("G^2 - 2(1-2C^2)G + 1 = 0, so the measured growth per step must equal")
    print("|G|: 1 for C <= 1 and |1-2C^2| + sqrt((1-2C^2)^2 - 1) for C > 1")
    print(f"{'C':>7} {'predicted |G|':>15} {'measured growth/step':>22}")
    n = 64
    theta = np.pi
    for C in (0.9, 0.95, 1.0, 1.02, 1.05, 1.1):
        b = 1.0 - 2.0 * C ** 2 * np.sin(theta / 2.0) ** 2
        if abs(b) <= 1.0:
            g = complex(b, np.sqrt(max(0.0, 1.0 - b ** 2)))
            pred = 1.0
        else:
            g = b + np.sign(b) * np.sqrt(b ** 2 - 1.0)
            pred = abs(g)
        j = np.arange(n)
        u0 = np.exp(1j * theta * j)
        u_prev = u0 / g
        u = u0.copy()
        amp0 = np.max(np.abs(u0))
        steps = 200
        for _ in range(steps):
            u_next = 2.0 * u - u_prev + C ** 2 * (np.roll(u, -1) - 2.0 * u
                                                  + np.roll(u, 1))
            u_prev, u = u, u_next
        growth = (np.max(np.abs(u)) / amp0) ** (1.0 / steps)
        print(f"{C:>7.2f} {pred:>15.8f} {growth:>22.8f}")
    print("C = 1 is the exact stability boundary: below it the highest mode is")
    print("neutral, above it the scheme grows at a rate the quadratic gives in")
    print("closed form, which is what makes an unstable run diagnosable.")


def trapezoidal_wave():
    print("average-acceleration (trapezoidal) scheme in time:")
    print("  u^{n+1} - 2u^n + u^{n-1} = (C^2/4) D^2(u^{n+1} + 2u^n + u^{n-1})")
    print("its amplification has |G| = 1 for every C, so it is unconditionally")
    print("stable and non-dissipative; the question is only accuracy.")
    n = 200
    h = L / n
    x = np.arange(n) * h
    print(f"{'C':>7} {'amplitude ratio after 1000 steps':>34} "
          f"{'L2 error against exact':>24}")
    for C in (0.5, 1.0, 2.0, 5.0, 10.0):
        dt = C * h / C_WAVE
        T = 0.5
        steps = int(round(T / dt))
        A = (np.diag(-2.0 * np.ones(n)) + np.diag(np.ones(n - 1), 1)
             + np.diag(np.ones(n - 1), -1))
        A[0, -1] = 1.0
        A[-1, 0] = 1.0
        u_prev = np.sin(2.0 * np.pi * x / L)
        u = np.sin(2.0 * np.pi * (x - C_WAVE * dt) / L)
        amp0 = np.max(np.abs(u))
        M = (np.eye(n) - 0.25 * C ** 2 * A)
        rhs_operator = 2.0 * np.eye(n) + 0.5 * C ** 2 * A
        for _ in range(steps):
            rhs = rhs_operator @ u + (0.25 * C ** 2 * A - np.eye(n)) @ u_prev
            u_next = np.linalg.solve(M, rhs)
            u_prev, u = u, u_next
        amp = np.max(np.abs(u)) / amp0
        t_final = steps * dt
        exact = np.sin(2.0 * np.pi * (x - C_WAVE * t_final) / L)
        err = np.linalg.norm(u - exact) / np.sqrt(n)
        print(f"{C:>7.2f} {amp:>34.10f} {err:>24.6e}")
    print("the amplitude is bounded at every C -- that is unconditional stability")
    print("-- but the error at C = 5 and 10 is of the order of the solution")
    print("itself.  Stability buys the absence of blow-up, never accuracy.")


def main():
    section("1. Explicit diffusion: measuring the stability limit")
    diffusion_stability()

    section("2. Order of accuracy in time, isolated from the spatial error")
    time_orders()

    section("3. The cost of the stability limit")
    cost()

    section("4. The CFL limit of the explicit wave scheme")
    wave_cfl()

    section("5. Unconditional stability without accuracy")
    trapezoidal_wave()


if __name__ == "__main__":
    main()
