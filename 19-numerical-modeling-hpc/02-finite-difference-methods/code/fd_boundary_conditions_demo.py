#!/usr/bin/env python3
"""Boundary conditions for finite differences: the order a Neumann condition
buys, the exact reflection coefficients of Dirichlet and free surfaces, the
residual reflection of a one-way condition, and a graded sponge layer.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_boundary_conditions_demo.py

All models and data in this module are SYNTHETIC.  Every pulse and material
contrast below is a chosen teaching value, not a measurement.

Contents
--------
1. Neumann by a one-sided difference versus by a ghost node: measured order.
2. Dirichlet (pressure-release) and free-surface reflection coefficients.
3. A first-order one-way (Mur) condition: residual reflection versus h.
4. A graded sponge layer: reflection versus damping strength and thickness.
"""

import numpy as np

RNG = np.random.default_rng(20261014)
C_WAVE = 1.0


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def neumann_study():
    """-u'' = (pi^2/4) cos(pi x/2), u'(0) = 0, u(1) = 0, exact u = cos(pi x/2).

    Two discretisations of the Neumann condition are compared: a two-point
    one-sided difference (first-order accurate) and a ghost node (second-order).
    The source term is non-zero on the boundary, which is what makes the two
    treatments differ at all.
    """
    print("model: -u'' = (pi^2/4) cos(pi x/2) on (0,1), u'(0) = 0, u(1) = 0")
    print("exact solution u = cos(pi x/2); the error is the maximum over the grid")
    print(f"{'n':>6} {'h':>9} {'one-sided (2 pt) err':>21} {'order':>8} "
          f"{'ghost node err':>16} {'order':>8}")
    prev_a = prev_b = None
    for n in (20, 40, 80, 160, 320):
        h = 1.0 / n
        x = np.arange(n + 1) * h
        exact = np.cos(0.5 * np.pi * x)
        f = 0.25 * np.pi ** 2 * np.cos(0.5 * np.pi * x)
        # unknowns u_0 .. u_{n-1}; u_n = 0 is the Dirichlet value at x = 1
        A = np.zeros((n, n))
        b = f[:n].copy()
        for i in range(1, n):
            A[i, i] = 2.0 / h ** 2
            A[i, i - 1] = -1.0 / h ** 2
            if i < n - 1:
                A[i, i + 1] = -1.0 / h ** 2
        A[0, 0] = -1.0 / h
        A[0, 1] = 1.0 / h
        b[0] = 0.0
        u_a = np.linalg.solve(A, b)
        # ghost node: u_{-1} = u_1 (since u'(0) = 0) gives 2(u_0 - u_1)/h^2 = f_0
        A2 = A.copy()
        b2 = b.copy()
        A2[0, :] = 0.0
        A2[0, 0] = 2.0 / h ** 2
        A2[0, 1] = -2.0 / h ** 2
        b2[0] = f[0]
        u_b = np.linalg.solve(A2, b2)
        ea = np.max(np.abs(u_a - exact[:n]))
        eb = np.max(np.abs(u_b - exact[:n]))
        oa = "n/a" if prev_a is None else f"{np.log(prev_a / ea) / np.log(2.0):.4f}"
        ob = "n/a" if prev_b is None else f"{np.log(prev_b / eb) / np.log(2.0):.4f}"
        print(f"{n:>6} {h:>9.5f} {ea:>21.6e} {oa:>8} {eb:>16.6e} {ob:>8}")
        prev_a, prev_b = ea, eb
    print("the two-point one-sided condition is consistent but first-order, and")
    print("that single point sets the order of the whole solution; the ghost node")
    print("keeps the second-order accuracy of the interior.")


def ricker(t, t0, f0):
    tau = t - t0
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * tau ** 2) * np.exp(-a * tau ** 2)


def run_wave(n_cells, h, C, n_steps, left_bc, sponge_cells=0, sigma_max=0.0,
             x_source=1200.0, x_recv=700.0, sigma=30.0):
    """Leapfrog wave equation in 1-D, velocity-free form, right end absorbing.

    Returns (time axis, receiver time series, dt).
    """
    dt = C * h / C_WAVE
    x = np.arange(n_cells) * h
    src = np.exp(-((x - x_source) ** 2) / (2.0 * sigma ** 2))
    u_prev = src.copy()                                   # t = 0
    # left-going wave: u(x, dt) = f(x + c dt)
    u = np.exp(-((x - x_source + C_WAVE * dt) ** 2) / (2.0 * sigma ** 2))
    if sponge_cells:
        sigma_field = np.zeros(n_cells)
        idx = np.arange(sponge_cells)
        sigma_field[:sponge_cells] = sigma_max * ((sponge_cells - idx)
                                                  / sponge_cells) ** 2
    else:
        sigma_field = np.zeros(n_cells)
    i_recv = int(round(x_recv / h))
    series = np.zeros(n_steps)
    for n in range(n_steps):
        u_next = (2.0 * u - (1.0 - 0.5 * sigma_field * dt) * u_prev
                  + C ** 2 * (np.roll(u, -1) - 2.0 * u + np.roll(u, 1)))
        u_next = u_next / (1.0 + 0.5 * sigma_field * dt)
        # right end: first-order one-way condition
        u_next[-1] = u[-2] + (C - 1.0) / (C + 1.0) * (u_next[-2] - u[-1])
        # left end
        if left_bc == "dirichlet":
            u_next[0] = 0.0
        elif left_bc == "neumann":
            u_next[0] = 2.0 * u[0] - u_prev[0] + 2.0 * C ** 2 * (u[1] - u[0])
        elif left_bc == "oneway":
            u_next[0] = u[1] + (C - 1.0) / (C + 1.0) * (u_next[1] - u[0])
        elif left_bc == "none":
            pass
        else:
            raise ValueError(left_bc)
        series[n] = u_next[i_recv]
        u_prev, u = u, u_next
    return np.arange(n_steps) * dt, series, dt


def reflection(left_bc, h=1.0, C=0.99, sponge_cells=0, sigma_max=0.0):
    """Ratio of the reflected to the incident pulse amplitude at the receiver."""
    n_cells = int(round(2000.0 / h))
    t_end = 2400.0
    dt_est = C * h / C_WAVE
    n_steps = int(round(t_end / dt_est))
    t, series, dt = run_wave(n_cells, h, C, n_steps, left_bc,
                             sponge_cells=sponge_cells, sigma_max=sigma_max)
    win_inc = (t > 300.0) & (t < 700.0)
    win_ref = (t > 1750.0) & (t < 2150.0)
    a_inc = np.max(np.abs(series[win_inc]))
    a_ref = np.max(np.abs(series[win_ref]))
    sign = np.sign(series[win_ref][np.argmax(np.abs(series[win_ref]))])
    return sign * a_ref / a_inc


def reflection_study():
    print("pulse at x = 1200 m travelling left at c = 1 m/s, receiver at 700 m,")
    print("right end one-way; the reflected pulse is measured at 1750-2150 s")
    print(f"{'left boundary':>26} {'h (m)':>7} {'C':>6} {'reflection':>14} "
          f"{'20 log10|R|':>13}")
    for bc, name in (("dirichlet", "Dirichlet (pressure release)"),
                     ("neumann", "free surface (Neumann)"),
                     ("oneway", "first-order one-way")):
        for h in (2.0, 1.0, 0.5):
            R = reflection(bc, h=h)
            db = "n/a" if abs(R) < 1e-16 else f"{20 * np.log10(abs(R)):.2f}"
            print(f"{name:>26} {h:>7.2f} {0.99:>6.2f} {R:>14.8f} {db:>13}")
    print("the Dirichlet and free-surface reflections are the exact values -1")
    print("and +1 that the boundary condition imposes; the one-way condition")
    print("leaves a residual reflection that shrinks as the grid is refined.")
    print("\nresidual reflection of the one-way condition, C = 0.99:")
    print(f"{'h (m)':>7} {'R':>14} {'ratio to previous':>18}")
    prev = None
    for h in (2.0, 1.0, 0.5, 0.25):
        R = abs(reflection("oneway", h=h))
        ratio = "n/a" if prev is None else f"{prev / R:.4f}"
        print(f"{h:>7.2f} {R:>14.8e} {ratio:>18}")
        prev = R


def sponge_study():
    print("damped sponge next to a Dirichlet wall: u_tt = c^2 u_xx - sigma u_t")
    print("sigma(x) ramps quadratically from 0 to sigma_max across the layer")
    print("(time spent in a layer of L cells is L/c seconds, so sigma must be")
    print("compared with c/L, not with 1)")
    print(f"{'layer cells':>12} {'sigma_max (1/s)':>17} {'reflection':>14} "
          f"{'20 log10|R| (dB)':>18}")
    best = None
    for cells in (10, 20, 40, 80):
        for smax in (0.05, 0.2, 0.5, 1.0):
            R = abs(reflection("dirichlet", sponge_cells=cells, sigma_max=smax))
            db = 20.0 * np.log10(R)
            print(f"{cells:>12} {smax:>17.3f} {R:>14.6e} {db:>18.1f}")
            if best is None or R < best[0]:
                best = (R, cells, smax)
    print(f"the best configuration in this scan is {best[1]} cells with "
          f"sigma_max = {best[2]:.3f} 1/s, giving |R| = {best[0]:.3e} "
          f"({20 * np.log10(best[0]):.1f} dB)")
    print("damping removes energy but the entry ramp reflects; a longer layer")
    print("with the same sigma_max absorbs more, and a stronger damping is not")
    print("unconditionally better, so the usable setting has to be measured.")


def main():
    section("1. Neumann boundary condition: one-sided versus ghost node")
    neumann_study()

    section("2. Reflection coefficients of the three classical conditions")
    reflection_study()

    section("3. Sponge layer: reflection against damping and thickness")
    sponge_study()


if __name__ == "__main__":
    main()
