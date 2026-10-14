"""Classification of second-order PDEs and the three canonical behaviours.

Run:  python3 pde_classification.py
Requires: Python standard library only.

Companion to lesson 01-09-01 (Classification of PDEs).

A linear second-order PDE in two independent variables,

    A u_xx + 2 B u_xy + C u_yy + (lower order) = 0,

is classified by the discriminant ``D = B^2 - A*C`` of its principal part:

    D < 0   elliptic    boundary-value problem     Laplace / Poisson
    D = 0   parabolic    initial-boundary problem  diffusion / heat
    D > 0   hyperbolic   initial-value problem     wave / advection

This script (i) classifies the three canonical equations and a few
degenerate cases, then (ii) solves one member of each class numerically and
measures the error against an analytic solution, so the classification is
shown to be a statement about behaviour and not about bookkeeping.

All problems are SYNTHETIC and one-dimensional with known exact solutions.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# 1. Classification by the discriminant
# ----------------------------------------------------------------------

def classify(a: float, b: float, c: float) -> tuple[str, float]:
    """Return (class, discriminant) for A u_xx + 2B u_xy + C u_yy = 0."""
    disc = b * b - a * c
    if disc < 0.0:
        return "elliptic", disc
    if disc > 0.0:
        return "hyperbolic", disc
    return "parabolic", disc


CANONICAL = [
    # (label, A, B, C, physical realisation)
    ("Laplace    u_xx + u_yy = 0", 1.0, 0.0, 1.0,
     "potential fields, steady flow"),
    ("Heat       u_t = k u_xx", 1.0, 0.0, 0.0,
     "heat flow, pore pressure, EM induction"),
    ("Wave       u_tt = c^2 u_xx", -1.0, 0.0, 1.0,
     "seismology, GPR, acoustics"),
    ("Degenerate u_xx + 2u_xy + u_yy = 0", 1.0, 1.0, 1.0,
     "parabolic: (d_x + d_y)^2 u = 0"),
    ("Tricomi     u_xx - x u_yy = 0 (x>0)", 1.0, 0.0, -1.0,
     "mixed: hyperbolic for x>0, elliptic for x<0"),
]


def report_classification() -> None:
    section("1. Classification of the principal part: D = B^2 - A C")
    print(f"{'equation':<34}{'A':>5}{'B':>5}{'C':>5}{'D':>7}  class")
    print("-" * 70)
    for label, a, b, c, _realisation in CANONICAL:
        kind, disc = classify(a, b, c)
        print(f"{label:<34}{a:>5.1f}{b:>5.1f}{c:>5.1f}{disc:>7.1f}  {kind}")
    print("\nNotes. The heat equation is parabolic because it is only first order")
    print("in t; the discriminant test sees one variable at a time. First-order")
    print("PDEs such as u_t + c u_x = 0 have no principal part and are not")
    print("classified by D at all: they are handled by characteristics (lesson 06).")


# ----------------------------------------------------------------------
# 2. Parabolic: explicit heat equation versus the analytic solution
# ----------------------------------------------------------------------

def heat_solve(n: int, tend: float, kappa: float) -> tuple[float, float]:
    """FTCS solution of u_t = kappa u_xx, u(0)=u(1)=0, u(x,0)=sin(pi x).

    Returns (max error against exp(-kappa pi^2 tend) sin(pi x), r = kappa dt/dx^2).
    """
    dx = 1.0 / (n + 1)
    dt_max = 0.4 * dx * dx / kappa          # stability limit is 0.5
    nt = int(math.ceil(tend / dt_max))
    dt = tend / nt
    r = kappa * dt / (dx * dx)
    u = [math.sin(math.pi * (i + 1) * dx) for i in range(n)]
    for _ in range(nt):
        u_new = u[:]
        for i in range(n):
            left = u[i - 1] if i > 0 else 0.0
            right = u[i + 1] if i < n - 1 else 0.0
            u_new[i] = u[i] + r * (left - 2.0 * u[i] + right)
        u = u_new
    decay = math.exp(-kappa * math.pi * math.pi * tend)
    err = max(abs(u[i] - decay * math.sin(math.pi * (i + 1) * dx))
              for i in range(n))
    return err, r


def report_parabolic() -> None:
    section("2. Parabolic: heat equation, error vs grid refinement")
    kappa, tend = 1.0, 0.05
    print(f"u_t = {kappa} u_xx on (0,1), u(0,t)=u(1,t)=0,")
    print(f"u(x,0)=sin(pi x), evaluated at t = {tend}")
    print(f"exact: u = exp(-kappa pi^2 t) sin(pi x) = {math.exp(-kappa*math.pi**2*tend):.6f} sin(pi x)")
    print(f"\n{'N':>5}{'r = k dt/dx^2':>15}{'max error':>14}{'order':>8}")
    previous = None
    for n in (10, 20, 40, 80, 160):
        err, r = heat_solve(n, tend, kappa)
        order = "" if previous is None else f"{math.log2(previous / err):.2f}"
        print(f"{n:>5}{r:>15.4f}{err:>14.3e}{order:>8}")
        previous = err
    print("\nOrder ~ 2: FTCS is second order in space and first order in time,")
    print("but here dt ~ dx^2 is refined with dx, so the spatial term dominates.")


# ----------------------------------------------------------------------
# 3. Hyperbolic: wave equation versus d'Alembert
# ----------------------------------------------------------------------

def wave_solve(n: int, tend: float, cfl: float) -> tuple[float, float]:
    """Second-order leapfrog solution of u_tt = c^2 u_xx.

    u(0)=u(1)=0, u(x,0)=sin(pi x), u_t(x,0)=0, so the exact solution is the
    standing wave u = sin(pi x) cos(pi c t).  Returns (max error, cfl used).
    """
    dx = 1.0 / (n + 1)
    dt = cfl * dx / 1.0                      # c = 1
    nt = int(round(tend / dt))
    dt = tend / nt
    cfl_used = dt / dx
    c2 = cfl_used * cfl_used
    u = [math.sin(math.pi * (i + 1) * dx) for i in range(n)]
    # Second-order start for u_t(x,0) = 0:  u^{-1} = u^0 + (1/2) c^2 dt^2 u_xx^0.
    u_prev = [0.0] * n
    for i in range(n):
        left = u[i - 1] if i > 0 else 0.0
        right = u[i + 1] if i < n - 1 else 0.0
        u_prev[i] = u[i] + 0.5 * cfl_used * cfl_used * (left - 2.0 * u[i] + right)
    for _ in range(nt):
        u_next = [0.0] * n
        for i in range(n):
            left = u[i - 1] if i > 0 else 0.0
            right = u[i + 1] if i < n - 1 else 0.0
            u_next[i] = 2.0 * u[i] - u_prev[i] + c2 * (left - 2.0 * u[i] + right)
        u_prev, u = u, u_next
    exact = math.cos(math.pi * tend)
    err = max(abs(u[i] - exact * math.sin(math.pi * (i + 1) * dx))
              for i in range(n))
    return err, cfl_used


def report_hyperbolic() -> None:
    section("3. Hyperbolic: wave equation, error vs grid refinement (CFL = 0.5)")
    tend = 0.25
    print("u_tt = u_xx on (0,1), u(0,t)=u(1,t)=0,")
    print("u(x,0)=sin(pi x), u_t(x,0)=0, exact u = sin(pi x) cos(pi t)")
    print(f"evaluated at t = {tend}; cos(pi t) = {math.cos(math.pi*tend):.6f}")
    print(f"\n{'N':>5}{'CFL':>8}{'max error':>14}{'order':>8}")
    previous = None
    for n in (10, 20, 40, 80, 160):
        err, cfl = wave_solve(n, tend, 0.5)
        order = "" if previous is None else f"{math.log2(previous / err):.2f}"
        print(f"{n:>5}{cfl:>8.3f}{err:>14.3e}{order:>8}")
        previous = err
    print("\nOrder ~ 2: the leapfrog stencil is second order in space and time.")


def report_propagation_speed() -> None:
    section("4. Finite propagation speed: the domain of dependence is a cone")
    print("Exact right-moving solution u = f(x - ct) with a compactly supported")
    print("smooth bump f (zero outside |x-x0| <= w). At Courant number 1 the")
    print("leapfrog stencil lies exactly on the characteristics, so the scheme")
    print("reproduces the translation u = f(x - ct) to round-off.")
    n = 600
    dx = 1.0 / n
    cfl = 1.0
    dt = cfl * dx
    steps = 120
    x0, w = 0.30, 0.04

    def f(x: float) -> float:
        if abs(x - x0) > w:
            return 0.0
        return 0.5 * (1.0 + math.cos(math.pi * (x - x0) / w))

    u = [f(i * dx) for i in range(n + 1)]
    u_prev = [f(i * dx + dt) for i in range(n + 1)]   # exact value at t = -dt
    for _ in range(steps):
        u_next = [0.0] * (n + 1)
        for i in range(1, n):                          # Dirichlet from exact
            u_next[i] = u[i + 1] + u[i - 1] - u_prev[i]
        u_next[0] = f(-(steps + 1) * dt)
        u_next[n] = f(1.0 - (steps + 1) * dt)
        u_prev, u = u, u_next
    t = steps * dt
    exact = [f(i * dx - t) for i in range(n + 1)]
    err = max(abs(u[i] - exact[i]) for i in range(n + 1))
    predicted_left, predicted_right = x0 - w + t, x0 + w + t
    numerical_left = min(i * dx for i, v in enumerate(u) if abs(v) > 1e-12)
    numerical_right = max(i * dx for i, v in enumerate(u) if abs(v) > 1e-12)
    outside = max(abs(v) for i, v in enumerate(u) if i * dx > predicted_right)
    print(f"  steps                = {steps},  t = {t:.6f},  c t = {t:.6f}")
    print(f"  cell dx              = {dx:.6f}   (= c dt, Courant number 1)")
    print(f"  predicted support    = [{predicted_left:.6f}, {predicted_right:.6f}]")
    print(f"  numerical support    = [{numerical_left:.6f}, {numerical_right:.6f}]")
    print(f"  max error vs exact   = {err:.3e}   (round-off level)")
    print(f"  max |u| beyond cone  = {outside:.3e}   (exactly zero)")
    print("\nInformation travels at finite speed c: the solution is identically")
    print("zero outside the cone x0 +/- w + ct. The heat equation fails this")
    print("test — diffusion has infinite propagation speed (next demo).")


# ----------------------------------------------------------------------
# 5. Elliptic: Poisson by relaxation, and the cost of being global
# ----------------------------------------------------------------------

def poisson_jacobi(n: int, tol: float) -> tuple[int, float]:
    """Solve u'' = -pi^2 sin(pi x), u(0)=u(1)=0, exact u = sin(pi x)."""
    dx = 1.0 / (n + 1)
    u = [0.0] * n
    exact = [math.sin(math.pi * (i + 1) * dx) for i in range(n)]
    iterations = 0
    while True:
        iterations += 1
        residual = 0.0
        u_new = u[:]
        for i in range(n):
            left = u[i - 1] if i > 0 else 0.0
            right = u[i + 1] if i < n - 1 else 0.0
            rhs = math.sin(math.pi * (i + 1) * dx) * math.pi * math.pi * dx * dx
            u_new[i] = 0.5 * (left + right + rhs)
            residual = max(residual, abs(u_new[i] - u[i]))
        u = u_new
        if residual < tol:
            break
        if iterations > 4_000_000:
            break
    err = max(abs(u[i] - exact[i]) for i in range(n))
    return iterations, err


def report_elliptic() -> None:
    section("5. Elliptic: Poisson by Jacobi relaxation")
    print("u'' = -pi^2 sin(pi x) on (0,1), u(0)=u(1)=0, exact u = sin(pi x).")
    print("Iterate until the max update falls below 1e-8.")
    print(f"\n{'N':>5}{'dx':>10}{'iterations':>12}{'max error':>13}{'iters*N^2':>12}")
    for n in (10, 20, 40):
        iterations, err = poisson_jacobi(n, 1e-8)
        dx = 1.0 / (n + 1)
        print(f"{n:>5}{dx:>10.4f}{iterations:>12}{err:>13.3e}"
              f"{iterations / (n * n):>12.3f}")
    print("\nThe solution is smooth and the error is small, but the iteration")
    print("count grows like N^2 ~ 1/dx^2: an elliptic solve is global. Every")
    print("point depends on every boundary value at once, which is why the")
    print("steady-state problem is a linear system and not a time march.")


def main() -> None:
    report_classification()
    report_parabolic()
    report_hyperbolic()
    report_propagation_speed()
    report_elliptic()
    section("Summary")
    print("elliptic   : smooth, global, boundary data fix everything")
    print("parabolic  : smooths, one-sided in time, infinite propagation speed")
    print("hyperbolic : propagates, two-sided in time, finite propagation speed")


if __name__ == "__main__":
    main()
