"""Diffusive timescales and the four geophysical diffusion problems.

Run:  python3 diffusion_timescales.py
Requires: Python standard library only.

Companion to lesson 01-09-02 (The Diffusion Equation and Diffusive
Timescales).

The dimensional analysis of u_t = kappa u_xx gives the single most useful
scaling law in geophysics:

    tau  ~  L^2 / kappa          (kappa = diffusivity, m^2 s^-1)

which is verified here numerically, and then evaluated for the four
subdisciplines that the diffusion equation governs:

    heat / palaeoclimate        kappa = thermal diffusivity
    pore pressure / seismicity  D     = hydraulic diffusivity
    hydrology / groundwater     D     = T / S (aquifer diffusivity)
    electromagnetics            the skin depth is the same length scale

Every parameter below is stated explicitly and is ILLUSTRATIVE; observed
crustal diffusivities span several orders of magnitude and should be checked
against the source you are citing.
"""

import math

MU0 = 4.0e-7 * math.pi          # vacuum permeability, T m A^-1 (exact by SI definition)
SECONDS_PER_YEAR = 365.25 * 24.0 * 3600.0


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def human_time(seconds: float) -> str:
    if seconds < 60.0:
        return f"{seconds:.3g} s"
    if seconds < 86400.0:
        return f"{seconds / 3600.0:.3g} h"
    if seconds < SECONDS_PER_YEAR:
        return f"{seconds / 86400.0:.3g} d"
    years = seconds / SECONDS_PER_YEAR
    if years < 1e6:
        return f"{years:.3g} yr"
    return f"{years / 1e6:.3g} Myr"


# ----------------------------------------------------------------------
# 1. The scaling law, applied to the four diffusion problems
# ----------------------------------------------------------------------

def report_timescales() -> None:
    section("1. tau ~ L^2 / kappa for the four geophysical diffusion problems")

    print("(a) Heat / palaeoclimate: thermal diffusivity")
    kappa_rock = 1.0e-6            # m^2 s^-1, typical crustal rock (range ~0.5-1.5e-6)
    print(f"    assumed kappa = {kappa_rock:.1e} m^2/s")
    for L_km in (1.0, 10.0, 100.0):
        tau = (L_km * 1e3) ** 2 / kappa_rock
        print(f"      L = {L_km:>6.1f} km  ->  tau = {tau:.3e} s = {human_time(tau)}")

    print("\n(b) Pore pressure / induced seismicity: hydraulic diffusivity")
    print("    D = k / (mu * S_s)   [k = permeability, mu = viscosity,")
    print("                          S_s = specific storage]")
    mu = 1.0e-3                    # Pa s (water)
    print(f"    assumed mu = {mu:.1e} Pa s")
    print(f"    {'k (m^2)':>10}{'S_s (1/m)':>12}{'D (m^2/s)':>12}"
          f"{'tau, L=5 km':>16}")
    for k in (1.0e-15, 1.0e-14, 1.0e-13):
        for S_s in (1.0e-6, 1.0e-7):
            D = k / (mu * S_s)
            tau = (5.0e3) ** 2 / D
            print(f"    {k:>10.1e}{S_s:>12.1e}{D:>12.3e}{human_time(tau):>16}")
    print("    A 1-year delay over 5 km needs D = 2.5e7 / 3.156e7 = "
          f"{(5.0e3)**2 / SECONDS_PER_YEAR:.3f} m^2/s.")
    print("    Reaching that with S_s = 1e-6 1/m requires k ~ "
          f"{(5.0e3)**2 / SECONDS_PER_YEAR * mu * 1e-6:.2e} m^2, which is high for")
    print("    intact rock. This is why triggering delays are debated.")

    print("\n(c) Hydrology: aquifer diffusivity D = T / S")
    T_trans, S_stor = 1.0e-2, 1.0e-3     # m^2/s, dimensionless (ILLUSTRATIVE)
    D_aq = T_trans / S_stor
    print(f"    assumed T = {T_trans:.1e} m^2/s, S = {S_stor:.1e}")
    print(f"    D = {D_aq:.3g} m^2/s")
    for L_km in (1.0, 10.0, 50.0):
        tau = (L_km * 1e3) ** 2 / D_aq
        print(f"      L = {L_km:>5.1f} km  ->  tau = {human_time(tau)}")

    print("\n(d) Electromagnetics: skin depth delta = sqrt(1 / (pi f mu0 sigma))")
    print(f"    mu0 = {MU0:.6e} T m / A")
    print(f"    {'sigma (S/m)':>13}{'f (Hz)':>10}{'delta (m)':>14}"
          f"{'tau = mu0 sigma delta^2':>26}")
    for sigma in (1.0e-4, 1.0e-2, 1.0):
        for f in (1.0e-3, 1.0, 1.0e3):
            delta = math.sqrt(1.0 / (math.pi * f * MU0 * sigma))
            tau = MU0 * sigma * delta * delta
            print(f"    {sigma:>13.1e}{f:>10.1e}{delta:>14.4g}{human_time(tau):>26}")
    print("    Note tau = mu0 sigma delta^2 = 1/(pi f): the diffusion time across")
    print("    one skin depth is exactly one radian of the driving period.")


# ----------------------------------------------------------------------
# 2. Numerical verification of u_t = kappa u_xx against an exact solution
# ----------------------------------------------------------------------

def diffusion_solve(n: int, kappa: float, sigma0: float, tend: float):
    """Solve u_t = kappa u_xx on [-1,1], u(+-1)=0, u(x,0)=exp(-x^2/sigma0^2).

    Returns (max error vs the exact Gaussian solution, dx, dt, r).
    Exact: u = (sigma0/s) exp(-x^2/s^2) with s = sqrt(sigma0^2 + 4 kappa t).
    """
    dx = 2.0 / (n + 1)
    r = 0.4                                  # stability limit: r <= 0.5
    dt_max = r * dx * dx / kappa
    nt = int(math.ceil(tend / dt_max))
    dt = tend / nt
    r = kappa * dt / (dx * dx)
    u = [math.exp(-((i + 0.5) * dx - 1.0) ** 2 / sigma0 ** 2) for i in range(n)]
    for _ in range(nt):
        u_new = u[:]
        for i in range(n):
            left = u[i - 1] if i > 0 else 0.0
            right = u[i + 1] if i < n - 1 else 0.0
            u_new[i] = u[i] + r * (left - 2.0 * u[i] + right)
        u = u_new
    s = math.sqrt(sigma0 ** 2 + 4.0 * kappa * tend)
    amp = sigma0 / s
    err = 0.0
    for i in range(n):
        x = (i + 0.5) * dx - 1.0
        exact = amp * math.exp(-x * x / (s * s))
        err = max(err, abs(u[i] - exact))
    return err, dx, dt, r


def report_verification() -> None:
    section("2. Explicit solve vs the exact Gaussian, error vs refinement")
    kappa, sigma0, tend = 1.0, 0.05, 0.02
    print("u_t = kappa u_xx on (-1,1), u(+-1)=0, u(x,0)=exp(-x^2/sigma0^2)")
    print(f"kappa = {kappa}, sigma0 = {sigma0}, t = {tend}; r = kappa dt/dx^2 = 0.4")
    s = math.sqrt(sigma0 ** 2 + 4 * kappa * tend)
    boundary = (sigma0 / s) * math.exp(-1.0 / (s * s))
    print(f"exact width s = sqrt(sigma0^2 + 4 kappa t) = {s:.6f}, "
          f"peak = sigma0/s = {sigma0/s:.6f}")
    print(f"exact value at the boundary x = +-1: {boundary:.3e} "
          f"(negligible, so the zero BC is consistent)")
    print(f"\n{'N':>6}{'dx':>11}{'max error':>13}{'order':>8}")
    previous = None
    for n in (50, 100, 200, 400, 800):
        err, dx, _dt, _r = diffusion_solve(n, kappa, sigma0, tend)
        order = "" if previous is None else f"{math.log2(previous / err):.2f}"
        print(f"{n:>6}{dx:>11.2e}{err:>13.3e}{order:>8}")
        previous = err
    print("\nObserved order ~ 2: second order in space, and dt ~ dx^2 keeps the")
    print("temporal error below the spatial error at every refinement.")
    print("sigma0 is deliberately narrow enough (0.05, 2 cells at N=50) that the")
    print("initial pulse is resolvable and the pulse never reaches the boundary.")


def report_variance_growth() -> None:
    section("3. Verifying the timescale: variance grows as d<x^2>/dt = 2 kappa")
    kappa, sigma0 = 1.0, 0.05
    n = 800
    dx = 4.0 / (n + 1)                       # domain (-2, 2): boundaries irrelevant
    r = 0.4
    dt = r * dx * dx / kappa
    u = [math.exp(-((i + 0.5) * dx - 2.0) ** 2 / sigma0 ** 2) for i in range(n)]

    def second_moment(field):
        mass = sum(field)
        return sum(((i + 0.5) * dx - 2.0) ** 2 * field[i] for i in range(n)) / mass

    m0 = second_moment(u)
    steps = 5000
    t = 0.0
    for _ in range(steps):
        u_new = u[:]
        for i in range(n):
            left = u[i - 1] if i > 0 else 0.0
            right = u[i + 1] if i < n - 1 else 0.0
            u_new[i] = u[i] + r * (left - 2.0 * u[i] + right)
        u = u_new
        t += dt
    m1 = second_moment(u)
    slope = (m1 - m0) / t
    print(f"  delta t                    = {t:.6f}")
    print(f"  <x^2> at t=0               = {m0:.8f}   (exact sigma0^2/2 = {sigma0**2/2:.8f})")
    print(f"  <x^2> at t=delta t         = {m1:.8f}")
    print(f"  measured d<x^2>/dt         = {slope:.6f}")
    print(f"  2 kappa                    = {2*kappa:.6f}")
    print(f"  relative difference        = {abs(slope - 2*kappa)/(2*kappa)*100:.3f} %")
    print("\nThe diffusion length grows like sqrt(2 kappa t), so the time to cross")
    print("a distance L scales as tau ~ L^2/kappa. This is the law used above.")


def report_infinite_speed() -> None:
    section("4. Infinite propagation speed: diffusion has no light cone")
    kappa, n, dx = 1.0, 400, 2.0 / 401
    x0, w = 0.0, 0.1
    r = 0.4
    dt = r * dx * dx / kappa

    def f(x: float) -> float:
        if abs(x - x0) > w:
            return 0.0
        return 0.5 * (1.0 + math.cos(math.pi * (x - x0) / w))

    u = [f((i + 0.5) * dx - 1.0) for i in range(n)]
    inside = {i for i in range(n) if abs(u[i]) > 1e-15}
    outside = [i for i in range(n) if i not in inside]
    print(f"  initial pulse support: |x| <= {w}  (zero outside)")
    done = 0
    for target in (1, 5, 50):
        for _ in range(target - done):
            u_new = u[:]
            for i in range(n):
                left = u[i - 1] if i > 0 else 0.0
                right = u[i + 1] if i < n - 1 else 0.0
                u_new[i] = u[i] + r * (left - 2.0 * u[i] + right)
            u = u_new
        done = target
        leaked = max(abs(u[i]) for i in outside)
        print(f"  after {target:>3} step(s): max |u| outside original support = "
              f"{leaked:.3e}")
    print(f"\n  Compare the wave demo, where the same test gives exactly 0.")
    print("  Diffusion is governed by a parabolic equation: a local disturbance is")
    print("  felt everywhere for any t > 0, though its amplitude decays like")
    print("  exp(-L^2/(4 kappa t)). Practically the signal is undetectable, but the")
    print("  mathematics has no finite speed. This is why 'how long does it take'")
    print("  is answered by tau ~ L^2/kappa and not by a velocity.")


def main() -> None:
    report_timescales()
    report_verification()
    report_variance_growth()
    report_infinite_speed()


if __name__ == "__main__":
    main()
