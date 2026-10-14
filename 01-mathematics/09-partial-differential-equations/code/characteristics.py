"""First-order PDEs: characteristics, kinematic waves, and shock formation.

Run:  python3 characteristics.py
Requires: Python standard library only.

Companion to lesson 01-09-06 (Method of Characteristics and First-Order PDEs).

Sections
    1. Linear advection u_t + c u_x = 0: characteristics are exact, and the
       upwind scheme replaces them with numerical diffusion
    2. A variable-coefficient example, u_t + x u_x = 0
    3. Kinematic waves: u_t + u u_x = 0, shock formation at t = 1
    4. Finite speed of information, and why weak solutions are needed

Everything is SYNTHETIC and one-dimensional. Every numerical result is
compared with the exact solution obtained from the characteristics.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# 1. Linear advection
# ----------------------------------------------------------------------

def report_advection() -> None:
    section("1. Linear advection: u_t + c u_x = 0 with u(x,0) = f(x)")
    print("Characteristics dx/dt = c give the exact solution u = f(x - c t):")
    print("the initial profile is simply translated, unchanged, at speed c.")
    c = 1.0
    print(f"\n  c = {c}. Verify by substitution that u = f(x - ct) is exact:")
    f = lambda x: math.exp(-x * x)
    u = lambda x, t: f(x - c * t)
    x0, t0 = 0.2, 0.3
    previous = None
    print(f"\n  {'hx':>10}{'ht':>10}{'|u_t + c u_x|':>18}{'order':>8}")
    for step in range(4):
        hx = 1.0e-2 / (2 ** step)
        ht = 0.7 * hx
        ut = (u(x0, t0 + ht) - u(x0, t0 - ht)) / (2 * ht)
        ux = (u(x0 + hx, t0) - u(x0 - hx, t0)) / (2 * hx)
        res = abs(ut + c * ux)
        order = "" if previous is None else f"{math.log2(previous / res):.2f}"
        print(f"  {hx:>10.2e}{ht:>10.2e}{res:>18.3e}{order:>8}")
        previous = res
    h = 1.0e-2
    ut = (u(x0, t0 + h) - u(x0, t0 - h)) / (2 * h)
    ux = (u(x0 + h, t0) - u(x0 - h, t0)) / (2 * h)
    print(f"\n  With ht = hx = {h:.0e} the residual is exactly {abs(ut + c*ux):.1e}: the two")
    print("  central differences then sample the same points along the characteristic.")
    print("\n  Residual -> 0 at second order: u = f(x - ct) solves the PDE exactly,")
    print("  and the first-order PDE needs only ONE boundary or initial condition,")
    print("  not a whole boundary curve. That is the structural difference from the")
    print("  elliptic and hyperbolic second-order problems of lessons 01 and 04.")

    print("\n  Now solve numerically with the upwind scheme")
    print("    u^{n+1}_i = u^n_i - nu (u^n_i - u^n_{i-1}),  nu = c dt/dx,")
    print("  and compare with the exact translated profile.")
    print(f"\n  {'N':>5}{'dx':>11}{'L-infinity error':>18}{'order':>8}")
    previous = None
    for n in (100, 200, 400, 800, 1600):
        err, nu = advection_upwind(n, c, 0.8, 0.5)
        order = "" if previous is None else f"{math.log2(previous / err):.2f}"
        print(f"  {n:>5}{2.0/n:>11.2e}{err:>18.3e}{order:>8}")
        previous = err
    print("\n  Order ~ 1, not 2: upwind is only first-order accurate. The leading")
    print("  truncation term is a diffusion, so the scheme does not translate the")
    print("  profile - it translates and smears it.")

    print("\n  The modified equation makes that precise. For constant nu,")
    print("    u_t + c u_x = (c dx / 2)(1 - nu) u_xx + higher order,")
    print("  so the numerical diffusion coefficient is D = (c dx / 2)(1 - nu) and a")
    print("  pulse's variance about its own centre must grow at rate 2D.")
    c, n, nu = 1.0, 200, 0.8
    dx = 2.0 / n
    steps = 240
    measured, predicted = advection_variance(c, n, nu, steps)
    print(f"\n    grid N = {n}, dx = {dx:.4f}, nu = {nu}")
    print(f"    measured d(variance)/dt          = {measured:.6e}")
    print(f"    predicted 2D = c dx (1 - nu)      = {predicted:.6e}")
    print(f"    relative difference               = "
          f"{abs(measured - predicted)/predicted*100:.2f} %")
    print("\n  The measured spreading is the modified-equation diffusion, not a")
    print("  physical effect. This is why second-order or spectral advection schemes")
    print("  are used whenever amplitude matters, and why an upwind scheme must never")
    print("  be used to argue that a real wave 'attenuated' with distance.")


def advection_upwind(n: int, c: float, nu: float, tend: float):
    """Upwind solution on [0,2] with periodic boundary; IC a Gaussian bump."""
    dx = 2.0 / n
    dt = nu * dx / c
    nt = int(round(tend / dt))
    f = lambda x: math.exp(-((x - 0.5) / 0.08) ** 2)
    u = [f(i * dx) for i in range(n)]
    for _ in range(nt):
        new = u[:]
        for i in range(n):
            new[i] = u[i] - nu * (u[i] - u[(i - 1) % n])
        u = new
    t = nt * dt
    exact = [f((i * dx - c * t) % 2.0) for i in range(n)]
    return max(abs(u[i] - exact[i]) for i in range(n)), nu


def advection_variance(c: float, n: int, nu: float, steps: int):
    """Measure the variance growth of a Gaussian under the upwind scheme."""
    dx = 2.0 / n
    dt = nu * dx / c
    sigma0 = 0.1
    u = [math.exp(-((i * dx - 0.5) / sigma0) ** 2) for i in range(n)]

    def variance(field):
        mass = sum(field)
        mean = sum(i * dx * field[i] for i in range(n)) / mass
        return sum((i * dx - mean) ** 2 * field[i] for i in range(n)) / mass

    v0 = variance(u)
    for _ in range(steps):
        new = u[:]
        for i in range(n):
            new[i] = u[i] - nu * (u[i] - u[(i - 1) % n])
        u = new
    t = steps * dt
    v1 = variance(u)
    return (v1 - v0) / t, c * dx * (1.0 - nu)


# ----------------------------------------------------------------------
# 2. Variable coefficient: u_t + x u_x = 0
# ----------------------------------------------------------------------

def report_variable_coefficient() -> None:
    section("2. Variable coefficient: u_t + x u_x = 0")
    print("Characteristics solve dx/dt = x, so x = x0 e^t and the solution is")
    print("    u(x,t) = f(x e^{-t}).")
    print("Characteristics fan out for x > 0 (a rarefaction) and into the origin")
    print("for x < 0; nothing crosses x = 0 because the coefficient vanishes there.")
    x0, t0 = 0.7, 0.25

    def f(x):
        return math.exp(-x * x)

    def u(x, t):
        return f(x * math.exp(-t))

    previous = None
    print(f"\n  f(s) = exp(-s^2), verified by substitution at x = {x0}, t = {t0}:")
    print(f"\n  {'h':>10}{'|u_t + x u_x|':>18}{'order':>8}")
    for step in range(4):
        h = 1.0e-3 / (2 ** step)
        ut = (u(x0, t0 + h) - u(x0, t0 - h)) / (2 * h)
        ux = (u(x0 + h, t0) - u(x0 - h, t0)) / (2 * h)
        res = abs(ut + x0 * ux)
        order = "" if previous is None else f"{math.log2(previous / res):.2f}"
        print(f"  {h:>10.2e}{res:>18.3e}{order:>8}")
        previous = res
    print("\n  Order ~ 2, so u = f(x e^{-t}) is an exact solution and the")
    print("  characteristics did all the work. Note what the formula says about")
    print("  observables: an initial feature at x0 appears later at x = x0 e^t, so")
    print("  the *shape* is preserved in the characteristic coordinate but stretched")
    print("  in the physical coordinate. Kinematic-wave problems in geophysics")
    print("  (flood waves, sediment pulses, glacier surges) are exactly this: the")
    print("  observable is a stretched version of the input.")


# ----------------------------------------------------------------------
# 3. Burgers: shock formation
# ----------------------------------------------------------------------

def report_shock() -> None:
    section("3. Kinematic wave: u_t + u u_x = 0, shock formation at t = 1")
    print("Characteristics satisfy dx/dt = u0(x0), so x = x0 + u0(x0) t and u is")
    print("constant along each. The map x0 -> x has derivative")
    print("    dx/dx0 = 1 + u0'(x0) t,")
    print("so it stops being invertible at the earliest t with 1 + u0'(x0) t = 0:")
    print("    t_s = -1 / min u0'.   Over that range the gradient is")
    print("    u_x = u0'(x0) / (1 + u0'(x0) t).")
    print("\n  Take u0(x) = sin(x) on [0, 2 pi): min u0' = -1 at x0 = pi, so")
    print("  t_s = 1 and the largest slope is attained on the characteristic that")
    print("  starts at x0 = pi, which stays at x = pi because u0(pi) = 0. There")
    print("    max |u_x| = 1 / (1 - t),   attained at x = pi.")
    print(f"\n  {'t':>7}{'exact 1/(1-t)':>16}{'scheme max|u_x|':>19}{'ratio':>10}")
    for t in (0.2, 0.4, 0.6, 0.8, 0.9, 0.95):
        exact = 1.0 / (1.0 - t)
        measured = burgers_max_gradient(t)
        print(f"  {t:>7.2f}{exact:>16.6f}{measured:>19.6f}"
              f"{measured/exact:>10.4f}")
    print("\n  The scheme reproduces the divergence to within a few per cent while")
    print("  the shock is still resolvable, and slightly under-predicts it as")
    print("  t -> 1 because numerical viscosity smooths the peak over a few cells.")
    print("  The exact solution itself has no smooth limit: at t = 1 the map is")
    print("  non-invertible at x0 = pi, and beyond t = 1 it is many-to-one, so u is")
    print("  multivalued and the PDE has no classical solution at all. A weak")
    print("  (shock) solution is required, and the conservation form decides which.")
    print("\n  This is the mechanism behind kinematic-wave applications: a smooth")
    print("  input steepens into a front at a predictable time, and the front then")
    print("  travels at a speed set by the Rankine-Hugoniot condition rather than by")
    print("  the local value of u. It is also why nonlinear first-order PDEs are the")
    print("  natural home of discontinuities, whereas the diffusion equation of")
    print("  lesson 02 smooths every initial profile.")


def burgers_max_gradient(tend: float, n: int = 1200, nu: float = 0.5):
    """Upwind (sign-dependent) solution of u_t + u u_x = 0, u0 = sin(x)."""
    dx = 2.0 * math.pi / n
    dt = nu * dx
    nt = int(round(tend / dt))
    dt = tend / nt
    u = [math.sin(i * dx) for i in range(n)]
    for _ in range(nt):
        new = u[:]
        for i in range(n):
            if u[i] >= 0.0:
                new[i] = u[i] - u[i] * dt / dx * (u[i] - u[(i - 1) % n])
            else:
                new[i] = u[i] - u[i] * dt / dx * (u[(i + 1) % n] - u[i])
        u = new
    return max(abs((u[(i + 1) % n] - u[(i - 1) % n]) / (2 * dx))
               for i in range(n))


# ----------------------------------------------------------------------
# 4. Finite speed and weak solutions
# ----------------------------------------------------------------------

def report_speed() -> None:
    section("4. Finite information speed, and why weak solutions are needed")
    print("For u_t + c u_x = 0 with compactly supported initial data, the exact")
    print("solution is zero outside [x0 - w + ct, x0 + w + ct]: the support moves")
    print("with the characteristics and never widens.")
    c = 1.0
    x0, w = 0.4, 0.05

    def f(x):
        s = abs(x - x0)
        return 0.0 if s > w else 0.5 * (1.0 + math.cos(math.pi * s / w))

    print(f"\n  {'t':>7}{'exact support':>32}{'exact max outside cone':>24}")
    for t in (0.1, 0.25, 0.4):
        left, right = x0 - w + c * t, x0 + w + c * t
        outside = max(abs(f(x - c * t)) for x in (0.0, 0.05, 0.95))
        print(f"  {t:>7.2f}{f'[{left:.4f}, {right:.4f}]':>32}{outside:>24.3e}")
    print("\n  Compare the heat equation, where the same compact pulse is nonzero")
    print("  everywhere for any t > 0 (lesson 02, section 4 of the diffusion demo).")
    print("  The classification of lesson 01 is thus also a statement about how far")
    print("  and how fast a measurement can constrain a source:")
    print("    hyperbolic -> a finite cone, so arrival times invert for structure")
    print("    parabolic  -> no cone, only a decaying amplitude exp(-L^2/(4 kappa t))")
    print("    elliptic   -> no time at all, boundary data fix the interior globally")
    print("\n  Finally, first-order nonlinear equations force the notion of a weak")
    print("  solution: once characteristics cross, the classical solution ceases to")
    print("  exist, yet the physics keeps going. The integral (conservation) form")
    print("  still makes sense and selects the physically correct solution. Lesson 08")
    print("  develops this into the variational and weak formulation used by finite")
    print("  element codes and by inverse theory.")


def main() -> None:
    report_advection()
    report_variable_coefficient()
    report_shock()
    report_speed()


if __name__ == "__main__":
    main()
