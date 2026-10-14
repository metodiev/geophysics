"""Boundary and initial-boundary value problems: BC types, well-posedness,
and absorbing boundaries.

Run:  python3 boundary_value_problems.py
Requires: Python standard library only.

Companion to lesson 01-09-07 (Boundary and Initial-Boundary Value Problems).

Sections
    1. Dirichlet and Neumann heat problems against exact solutions, order 2
    2. Robin (convective) boundary: convergence to the steady state
    3. Energy decay, and why the backward heat problem is ill posed
    4. Boundary conditions for the wave equation: reflecting vs absorbing

All problems are SYNTHETIC and one-dimensional. Illustrative values only.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# 1. Dirichlet and Neumann problems
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 1. Dirichlet and Neumann problems
# ----------------------------------------------------------------------

def neumann_dirichlet(n: int, tend: float, kappa: float = 1.0, r: float = 0.4):
    """u_t = kappa u_xx on (0,1), u_x(0,t) = 0, u(1,t) = 0, u(x,0)=cos(pi x/2).

    Exact: u = cos(pi x/2) exp(-kappa pi^2 t / 4).
    """
    dx = 1.0 / n
    dt = r * dx * dx / kappa
    nt = int(math.ceil(tend / dt))
    dt = tend / nt
    r = kappa * dt / (dx * dx)
    u = [math.cos(math.pi * (i * dx) / 2.0) for i in range(n + 1)]
    u[n] = 0.0
    for _ in range(nt):
        new = u[:]
        # Neumann at x = 0: mirror node, u_{-1} = u_1
        new[0] = u[0] + r * (2.0 * u[1] - 2.0 * u[0])
        for i in range(1, n):
            new[i] = u[i] + r * (u[i + 1] - 2.0 * u[i] + u[i - 1])
        new[n] = 0.0                              # Dirichlet at x = 1
        u = new
    decay = math.exp(-kappa * math.pi ** 2 * tend / 4.0)
    err = max(abs(u[i] - math.cos(math.pi * (i * dx) / 2.0) * decay)
              for i in range(n + 1))
    return err, dx, r


def report_dirichlet_neumann() -> None:
    section("1. Insulated-left, fixed-right heat problem")
    print("u_t = u_xx on (0,1), u_x(0,t) = 0 (insulated), u(1,t) = 0 (fixed),")
    print("u(x,0) = cos(pi x / 2).  Exact: u = cos(pi x / 2) exp(-pi^2 t / 4).")
    tend = 0.05
    print(f"\n  At t = {tend}, exp(-pi^2 t/4) = "
          f"{math.exp(-math.pi**2*tend/4):.6f}")
    print(f"\n  {'N':>5}{'dx':>11}{'r':>8}{'max error':>14}{'order':>8}")
    previous = None
    for n in (25, 50, 100, 200):
        err, dx, r = neumann_dirichlet(n, tend)
        order = "" if previous is None else f"{math.log2(previous / err):.2f}"
        print(f"  {n:>5}{dx:>11.4f}{r:>8.3f}{err:>14.3e}{order:>8}")
        previous = err
    print("\n  Order ~ 2. The Neumann condition is imposed by a mirror (ghost)")
    print("  node, which is second-order accurate; using a one-sided difference")
    print("  would drop the whole solution to first order. Boundary conditions")
    print("  are part of the discretisation, not an afterthought.")
    print("\n  Physical reading: with the left end insulated the slowest decaying")
    print("  mode has rate pi^2/4 ~ 2.47, four times slower than the rate pi^2 of")
    print("  the Dirichlet-on-both-ends problem. Changing one boundary condition")
    print("  changed the eigenvalue, which is the generic situation. 'What are the")
    print("  boundary conditions?' is the first question to ask of any PDE model.")


# ----------------------------------------------------------------------
# 2. Robin boundary and the steady state
# ----------------------------------------------------------------------

def heat_robin(n: int, tend: float, biot: float, u_amb: float = 1.0,
               kappa: float = 1.0, r: float = 0.4, report_times=()):
    """u_t = kappa u_xx, u_x(0,t)=0, -u_x(1,t) = Bi (u(1,t) - u_amb).

    The steady state is u = u_amb everywhere (insulated far end, convective
    surface).  Returns (field, dx, energy history).
    """
    dx = 1.0 / n
    dt = r * dx * dx / kappa
    nt = int(math.ceil(tend / dt))
    dt = tend / nt
    r = kappa * dt / (dx * dx)
    u = [math.cos(math.pi * (i * dx) / 2.0) for i in range(n + 1)]
    energy = [sum((v - u_amb) ** 2 for v in u) * dx]
    for step in range(1, nt + 1):
        new = u[:]
        new[0] = u[0] + r * (2.0 * u[1] - 2.0 * u[0])
        for i in range(1, n):
            new[i] = u[i] + r * (u[i + 1] - 2.0 * u[i] + u[i - 1])
        # Robin at x = 1 via a ghost node: u_{n+1} = u_{n-1} - 2 Bi dx (u_n - u_amb)
        ghost = u[n - 1] - 2.0 * biot * dx * (u[n] - u_amb)
        new[n] = u[n] + r * (ghost - 2.0 * u[n] + u[n - 1])
        u = new
        energy.append(sum((v - u_amb) ** 2 for v in u) * dx)
    return u, dx, energy


def report_robin() -> None:
    section("2. Robin (convective) boundary: the steady state is u = u_ambient")
    print("u_t = u_xx, u_x(0,t) = 0, and at x = 1 the conductive flux balances")
    print("the convective loss:   -u_x(1,t) = Bi (u(1,t) - u_amb).")
    print("With the far end insulated the only steady state is u = u_amb, and it")
    print("is what the solution must relax to.")
    biot = 10.0
    n = 50
    nt_steps = 8.0                     # dimensionless time to run
    u, dx, energy = heat_robin(n, nt_steps, biot, report_times=())
    err = max(abs(v - 1.0) for v in u)
    print(f"\n  Bi = {biot}, N = {n}, run to t = {nt_steps}")
    print(f"  max |u - u_amb| at the end          = {err:.3e}")
    print(f"  the Robin condition residual: -u_x(1) - Bi(u(1)-1) = "
          f"{-(u[n] - u[n-1]) / dx - biot * (u[n] - 1.0):.3e}")
    print("\n  The flux residual is at the truncation-error level, so the discrete")
    print("  boundary condition is satisfied by the discrete solution. This is the")
    print("  definition of a consistent boundary condition: it is a statement about")
    print("  the solution, not a separate calculation.")
    print("\n  Energy history, E(t) = integral (u - u_amb)^2 dx. With an")
    print("  inhomogeneous boundary condition it is the deviation from the")
    print("  equilibrium that must decay, not the total square:")
    print(f"  {'t':>8}{'E':>16}")
    for frac in (0.0, 0.1, 0.25, 0.5, 1.0):
        index = int(frac * (len(energy) - 1))
        print(f"  {frac*nt_steps:>8.2f}{energy[index]:>16.9f}")
    monotone = all(energy[i + 1] <= energy[i] + 1e-15
                   for i in range(len(energy) - 1))
    print(f"\n  Monotonically decreasing at every step: {monotone}")
    print("  Diffusion is dissipative. That monotonicity is the energy method's")
    print("  proof of uniqueness and stability, and it is what fails for the")
    print("  backward problem in the next section.")


# ----------------------------------------------------------------------
# 3. Well-posedness: the backward heat problem
# ----------------------------------------------------------------------

def report_wellposedness() -> None:
    section("3. Why the backward heat problem is ill posed")
    print("The forward problem smooths. Take u(x,0) = sin(pi x) + eps sin(N pi x)")
    print("with the Dirichlet problem u(0,t) = u(1,t) = 0. Each mode evolves as")
    print("    exp(-(n pi)^2 t),")
    print("so the noise mode is suppressed by exp(-(N pi)^2 t).")
    kappa, tend = 1.0, 0.05
    print(f"\n  kappa = {kappa}, t = {tend}")
    print(f"  {'N':>5}{'decay exp(-(N pi)^2 t)':>26}{'amplification to invert':>25}")
    for n_mode in (1, 2, 5, 10, 20):
        decay = math.exp(-(n_mode * math.pi) ** 2 * kappa * tend)
        print(f"  {n_mode:>5}{decay:>26.3e}{1.0/decay:>25.3e}")
    print("\n  Numerically: run the forward problem twice, once from the smooth")
    print("  initial condition and once with a 1e-6 noise mode added, and measure")
    print("  how much of the noise survives.")
    n, dx = 200, 1.0 / 200
    r = 0.4
    dt = r * dx * dx / kappa
    nt = int(math.ceil(tend / dt))
    dt = tend / nt
    r = kappa * dt / (dx * dx)

    def forward(scale: float):
        u = [math.sin(math.pi * i * dx)
             + scale * math.sin(20 * math.pi * i * dx) for i in range(n + 1)]
        for _ in range(nt):
            new = u[:]
            for i in range(1, n):
                new[i] = u[i] + r * (u[i + 1] - 2.0 * u[i] + u[i - 1])
            new[0] = new[n] = 0.0
            u = new
        return u

    clean = forward(0.0)
    noisy = forward(1e-6)
    survived = max(abs(clean[i] - noisy[i]) for i in range(n + 1))
    smooth = math.exp(-math.pi ** 2 * kappa * tend)
    truncation = max(abs(clean[i] - smooth * math.sin(math.pi * i * dx))
                     for i in range(n + 1))
    expected_noise = 1e-6 * math.exp(-(20 * math.pi) ** 2 * kappa * tend)
    print(f"    noise survived to t = {tend}          = {survived:.3e}")
    print(f"    predicted noise amplitude          = {expected_noise:.3e}")
    print(f"    finite-difference truncation error = {truncation:.3e}")
    print("    (the truncation error is what limits the forward solve; the noise is")
    print("     far below it, so it has been destroyed rather than merely reduced)")
    print("\n  The noise is gone: the forward map has destroyed that information in")
    print("  this data set, and no algorithm can bring it back. To recover the")
    print("  initial condition you would have to multiply by 1e85, so any data error")
    print("  of size 1e-6 becomes an error of 1e79 in the answer. Hadamard's")
    print("  requirement that the solution depend continuously on the data fails,")
    print("  and the problem is ill posed. Regularisation, not inversion, is the")
    print("  only option — the subject of the inverse-problems folder.")


# ----------------------------------------------------------------------
# 4. Boundary conditions for the wave equation
# ----------------------------------------------------------------------

def report_wave_bc() -> None:
    section("4. Wave boundaries: reflecting (Dirichlet) vs absorbing (one-way)")
    print("u_tt = c^2 u_xx on (0,1), c = 1, Courant number 0.5. A compact")
    print("right-going pulse starts at x = 0.3 and reaches x = 1 at t = 0.7.")
    print("Right boundary:  (a) u = 0  -> total reflection")
    print("                 (b) first-order one-way (Mur) condition,")
    print("                     u^{n+1}_N = u^n_{N-1} + ((nu-1)/(nu+1))")
    print("                                 (u^{n+1}_{N-1} - u^n_N),")
    print("                     which is exact for normal incidence.")
    print(f"\n  {'boundary':>22}{'t = 0.7':>13}{'t = 1.0':>13}{'t = 1.6':>13}")
    for label, mode in (("Dirichlet u = 0", "dirichlet"),
                        ("one-way absorbing", "mur")):
        vals = [wave_run(mode, t) for t in (0.7, 1.0, 1.6)]
        print(f"  {label:>22}" + "".join(f"{v:>13.4e}" for v in vals))
    print("\n  Read the columns as the pulse's fate. At t = 0.7 the pulse is still")
    print("  inside the domain (amplitude ~1 in both cases). By t = 1.0 the fixed")
    print("  boundary has returned it with amplitude ~1, while the absorbing")
    print("  condition has left 0.07 per cent behind: a reflection coefficient of")
    print("  about 1e-3, limited by the first-order accuracy of the condition.")
    print("\n  Modelling the real Earth means deciding, for every edge of the mesh,")
    print("  whether that edge reflects or radiates. In seismology the physical free")
    print("  surface is a genuine reflector (traction free), while the artificial")
    print("  edges of the computational box must be made absorbing as accurately as")
    print("  possible; the residual reflections are a standard artefact in the")
    print("  seismic literature, and their amplitude is a common quality metric for")
    print("  a modelling code.")


def wave_run(boundary_mode: str, tend: float):
    """Max |u| at the end of a run of the 1-D wave equation with one right BC."""
    n = 400
    dx = 1.0 / n
    cfl = 0.5
    dt = cfl * dx
    nt = int(round(tend / dt))
    dt = tend / nt
    sigma = dt / dx
    c2 = sigma * sigma
    mur = (sigma - 1.0) / (sigma + 1.0)
    x0, w = 0.3, 0.05

    def f(x):
        s = abs(x - x0)
        return 0.0 if s > w else 0.5 * (1.0 + math.cos(math.pi * s / w))

    u = [f(i * dx) for i in range(n + 1)]
    u_prev = [f(i * dx + dt) for i in range(n + 1)]     # exact value at t = -dt
    for _ in range(nt):
        new = [0.0] * (n + 1)
        for i in range(1, n):
            new[i] = 2.0 * u[i] - u_prev[i] + c2 * (u[i + 1] - 2.0 * u[i] + u[i - 1])
        if boundary_mode == "dirichlet":
            new[n] = 0.0
        else:
            new[n] = u[n - 1] + mur * (new[n - 1] - u[n])
        new[0] = u[1] + mur * (new[1] - u[0])           # one-way outflow, left
        u_prev, u = u, new
    return max(abs(v) for v in u)


def main() -> None:
    report_dirichlet_neumann()
    report_robin()
    report_wellposedness()
    report_wave_bc()


if __name__ == "__main__":
    main()
