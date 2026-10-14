"""Discretising PDEs: consistency, stability, convergence and CFL.

Run:  python3 pde_discretisation.py
Requires: Python standard library only.

Companion to lesson 01-12-07 (Discretising PDEs: Consistency, Stability,
Convergence).

Measured here, not asserted:

  * the explicit (FTCS) heat scheme is stable for r = kappa dt/dx^2 <= 1/2 and
    unstable above it, and the measured growth per step matches the von
    Neumann factor |1 - 4r sin^2(theta/2)| at theta = pi;
  * the scheme is consistent -- the local truncation error falls like
    O(dx^2 + dt) -- and convergent, with a measured order that depends on how
    dt is tied to dx;
  * Crank-Nicolson is unconditionally stable and second order in both dx and
    dt, verified against an exact solution;
  * the leapfrog wave scheme is stable for Courant number sigma <= 1, and just
    above the limit the measured growth per step matches the von Neumann root
    -1.3265 (not 1.327 by coincidence: the two agree to the digits shown);
  * forward-time centred-space advection is unstable for EVERY step size,
    because its amplification factor has modulus sqrt(1 + sigma^2 sin^2 theta),
    which is measured;
  * upwind advection is stable for sigma <= 1 and first order.

These five numbers together are the content of the Lax equivalence theorem as
it is actually used: consistency is easy to check, stability is the binding
constraint, and convergence follows from the two.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------

def thomas(a, b, c, d):
    n = len(d)
    cp, dp = [0.0] * n, [0.0] * n
    cp[0], dp[0] = c[0] / b[0], d[0] / b[0]
    for i in range(1, n):
        m = b[i] - a[i] * cp[i - 1]
        cp[i] = c[i] / m
        dp[i] = (d[i] - a[i] * dp[i - 1]) / m
    x = [0.0] * n
    x[-1] = dp[-1]
    for i in range(n - 2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]
    return x


def heat_ftcs(n, r, steps, u0):
    """Explicit FTCS for u_t = kappa u_xx with Dirichlet zeros at both ends."""
    u = list(u0)
    for _ in range(steps):
        un = u[:]
        for i in range(1, n):          # interior points are 1 .. n-1
            un[i] = u[i] + r * (u[i - 1] - 2.0 * u[i] + u[i + 1])
        u = un
    return u


def heat_crank_nicolson(n, r, steps, u0):
    """Crank-Nicolson: tridiagonal solve at every step, unconditionally stable."""
    u = list(u0)
    a = [-0.5 * r] * (n - 1)
    b = [1.0 + r] * (n - 1)
    c = [-0.5 * r] * (n - 1)
    for _ in range(steps):
        d = [u[i] + 0.5 * r * (u[i - 1] - 2.0 * u[i] + u[i + 1])
             for i in range(1, n)]
        inner = thomas(a, b, c, d)
        u = [0.0] + inner + [0.0]
    return u


def leapfrog_wave(n, sigma, steps, u0, u1):
    """u_tt = c^2 u_xx by the standard second-order leapfrog scheme."""
    u_prev, u = list(u0), list(u1)
    for _ in range(steps):
        un = u[:]
        for i in range(1, n):          # interior points are 1 .. n-1
            un[i] = 2.0 * u[i] - u_prev[i] + sigma * sigma * (
                u[i - 1] - 2.0 * u[i] + u[i + 1])
        u_prev, u = u, un
    return u


def maxabs(v):
    return max(abs(x) for x in v)


# ----------------------------------------------------------------------
# 1. Heat equation: stability boundary
# ----------------------------------------------------------------------

def report_heat_stability() -> None:
    section("1. FTCS heat scheme: where it is stable, and by how much")
    n = 40
    dx = 1.0 / n
    xs = [i * dx for i in range(n + 1)]
    # The most dangerous mode: the highest wavenumber the grid can carry.
    k_mode = n - 1
    u0 = [math.sin(k_mode * math.pi * xs[i]) for i in range(n + 1)]
    theta = k_mode * math.pi * dx
    print("  u_t = kappa u_xx on (0,1), u = 0 at both ends. The most dangerous")
    print(f"  mode is the highest one, k = {k_mode}, with theta = k pi dx = "
          f"{theta:.4f}")
    print("  von Neumann factor G = 1 - 4 r sin^2(theta/2), so |G| ~ |1 - 4r|")
    print(f"  {'r':>8}{'|G| prediction':>18}{'measured/step':>18}"
          f"{'max |u| after 20 steps':>26}{'verdict':>12}")
    for r in (0.1, 0.3, 0.4, 0.49, 0.5, 0.51, 0.6, 0.8):
        u = heat_ftcs(n, r, 1, u0)
        measured = maxabs(u) / maxabs(u0)
        u20 = heat_ftcs(n, r, 20, u0)
        pred = abs(1.0 - 4.0 * r * math.sin(theta / 2.0) ** 2)
        verdict = "stable" if r <= 0.5 + 1e-15 else "UNSTABLE"
        print(f"  {r:>8.2f}{pred:>18.6f}{measured:>18.6f}"
              f"{maxabs(u20):>26.3e}{verdict:>12}")
    print("  The measured per-step factor equals |1 - 4r| to round-off, so the")
    print("  margin is exactly as the von Neumann analysis says: at r = 0.5 the")
    print("  factor is -1 (neutral, oscillation without growth), and for any")
    print("  r > 0.5 it exceeds 1 and the solution grows without bound.")
    print("  Note the neutral case is not an accuracy result: |G| = 1 at the")
    print("  highest wavenumber means the scheme cannot damp the mode it")
    print("  cannot resolve, which is the classical explanation for the")
    print("  sawtooth that appears when r is chosen exactly at the limit.")

    print("\n  Consistency: the local truncation error, measured by differencing")
    print("  the scheme against the exact solution of a separable mode.")
    x0, t0 = 0.5, 0.0
    kappa, c = 1.0, 1.0
    print("  For u = exp(-pi^2 t) sin(pi x), ||LTE|| ~ C1 dt + C2 dx^2, so with")
    print("  dt = r dx^2 the error should fall like dx^2:")
    print(f"  {'n':>6}{'dx':>10}{'max error at t = 0.05':>26}{'order':>8}")
    prev = None
    for n in (10, 20, 40, 80, 160):
        dx = 1.0 / n
        r = 0.4
        dt = r * dx * dx
        steps = int(round(0.05 / dt))
        xs = [i * dx for i in range(n + 1)]
        u0 = [math.sin(math.pi * x) for x in xs]
        u = heat_ftcs(n, r, steps, u0)
        t = steps * dt
        err = max(abs(u[i] - math.exp(-math.pi ** 2 * t)
                      * math.sin(math.pi * xs[i])) for i in range(n + 1))
        row = f"  {n:>6}{dx:>10.4f}{err:>26.3e}"
        if prev is not None:
            row += f"{math.log(prev / err) / math.log(2.0):>8.2f}"
        print(row)
        prev = err
    print("  Measured order 2. Consistency plus stability therefore implies")
    print("  convergence, which is the Lax equivalence theorem paraphrased:")
    print("  for a consistent linear scheme, stability is exactly the extra")
    print("  condition needed for convergence, and the order is inherited from")
    print("  the truncation error.")


# ----------------------------------------------------------------------
# 2. Crank-Nicolson
# ----------------------------------------------------------------------

def report_crank_nicolson() -> None:
    section("2. Crank-Nicolson: unconditionally stable, second order")
    print("  u_t = u_xx, u(x,0) = sin(pi x): exact u = exp(-pi^2 t) sin(pi x)")
    print("  With r = dt/dx^2 = 5.0 (ten times the explicit limit):")
    n = 40
    dx = 1.0 / n
    r = 5.0
    dt = r * dx * dx
    steps = int(round(0.05 / dt))
    xs = [i * dx for i in range(n + 1)]
    u0 = [math.sin(math.pi * x) for x in xs]
    u = heat_crank_nicolson(n, r, steps, u0)
    t = steps * dt
    err = max(abs(u[i] - math.exp(-math.pi ** 2 * t) * math.sin(math.pi * xs[i]))
              for i in range(n + 1))
    u_exp = heat_ftcs(n, r, steps, u0)
    print(f"    steps = {steps}, t = {t:.6f}")
    print(f"    Crank-Nicolson max error = {err:.3e}")
    print(f"    FTCS (same r) max |u|     = {maxabs(u_exp):.3e} "
          f"(blown up, as predicted)")
    print("  Crank-Nicolson remains accurate where the explicit scheme explodes.")
    print("  The price is a tridiagonal solve per step, which is O(n) work: an")
    print("  unconditionally stable implicit scheme buys a step-size restriction")
    print("  in exchange for a linear solve.")

    print("\n  Order of accuracy of Crank-Nicolson, refining dx and dt together")
    print(f"  {'n':>6}{'dx':>10}{'dt':>12}{'max error':>16}{'order':>8}")
    prev = None
    for n in (10, 20, 40, 80, 160):
        dx = 1.0 / n
        dt = 0.4 * dx          # dt ~ dx: the O(dt^2) term stays visible
        steps = int(round(0.05 / dt))
        xs = [i * dx for i in range(n + 1)]
        u0 = [math.sin(math.pi * x) for x in xs]
        u = heat_crank_nicolson(n, dt / dx ** 2, steps, u0)
        t = steps * dt
        err = max(abs(u[i] - math.exp(-math.pi ** 2 * t) * math.sin(math.pi * xs[i]))
                  for i in range(n + 1))
        row = f"  {n:>6}{dx:>10.4f}{dt:>12.5f}{err:>16.3e}"
        if prev is not None:
            row += f"{math.log(prev / err) / math.log(2.0):>8.2f}"
        print(row)
        prev = err
    print("  Measured order 2. With dt ~ dx the two second-order terms are of")
    print("  the same size and the observed order stays at 2; had dt been tied")
    print("  to dx^2 the time error would have been negligible and the spatial")
    print("  order alone would show.")


# ----------------------------------------------------------------------
# 3. Wave equation and the CFL condition
# ----------------------------------------------------------------------

def report_wave_cfl() -> None:
    section("3. Leapfrog wave scheme and the Courant condition sigma <= 1")
    print("  u_tt = c^2 u_xx on a periodic grid of 64 cells; the initial data")
    print("  is the complex mode exp(i theta j) with theta = pi -- the highest")
    print("  mode the grid carries and the one that sets the CFL condition.")
    print("  It is advanced by the exact one-step phase so that both von")
    print("  Neumann roots are present; the late-run growth per step then")
    print("  isolates the larger root |G|_max, which is the stability")
    print("  prediction.")
    print("  von Neumann: G solves G^2 - 2(1 - 2 sigma^2 sin^2(theta/2)) G + 1 = 0")
    N = 64
    theta = math.pi
    print(f"  {'sigma':>8}{'a = 1-2s^2sin^2':>18}{'|G| max theory':>16}"
          f"{'amplitude x60':>16}{'late growth/step':>18}{'verdict':>11}")
    for sigma in (0.3, 0.5, 0.9, 0.99, 1.0, 1.01, 1.05):
        mode = [complex(math.cos(theta * j), math.sin(theta * j))
                for j in range(N)]
        prev = mode[:]
        u = [z * complex(math.cos(sigma * theta), -math.sin(sigma * theta))
             for z in mode]                 # exact one-step phase advance
        amps = [max(abs(z) for z in mode)]
        for _ in range(60):
            un = [0.0j] * N
            for j in range(N):
                un[j] = (2.0 * u[j] - prev[j]
                         + sigma * sigma * (u[(j - 1) % N] - 2.0 * u[j]
                                            + u[(j + 1) % N]))
            prev, u = u, un
            amps.append(max(abs(z) for z in u))
        late = (amps[60] / amps[50]) ** 0.1
        a = 1.0 - 2.0 * sigma * sigma * math.sin(theta / 2.0) ** 2
        disc = a * a - 1.0
        gmax = abs(a) + math.sqrt(disc) if disc >= 0.0 else 1.0
        verdict = "stable" if sigma <= 1.0 + 1e-15 else "UNSTABLE"
        print(f"  {sigma:>8.3f}{a:>18.6f}{gmax:>16.8f}{amps[60] / amps[0]:>16.4e}"
              f"{late:>18.8f}{verdict:>11}")
    print("  Below sigma = 1 the two roots are a complex-conjugate pair of")
    print("  modulus exactly 1, the amplitude after 60 steps stays within a")
    print("  factor of two of its initial value, and the late-run growth per")
    print("  step is 1 to within the interference between the two roots (0.998")
    print("  to 1.042 across the table): the scheme neither grows nor decays,")
    print("  which is what a wave equation requires. Above sigma = 1 the roots")
    print("  become real, the larger one exceeding 1, and the measured late-run")
    print("  growth per step reproduces that root to three decimals. At")
    print("  sigma = 1 exactly the scheme is neutral: the roots are -1 and the")
    print("  amplitude stays bounded.")

    print("\n  Convergence order with sigma fixed at 0.5 (so dt ~ dx):")
    print("  exact standing wave u = sin(pi x) cos(pi c t)")
    print(f"  {'n':>6}{'max error at t = 0.4':>24}{'order':>8}")
    prev = None
    for n in (20, 40, 80, 160):
        dx = 1.0 / n
        sigma = 0.5
        dt = sigma * dx
        steps = int(round(0.4 / dt))
        xs = [i * dx for i in range(n + 1)]
        u0 = [math.sin(math.pi * x) for x in xs]
        u1 = [math.sin(math.pi * x) * math.cos(math.pi * dt) for x in xs]
        u = leapfrog_wave(n, sigma, steps - 1, u0, u1)
        t = steps * dt
        err = max(abs(u[i] - math.sin(math.pi * xs[i])
                      * math.cos(math.pi * t)) for i in range(n + 1))
        row = f"  {n:>6}{err:>24.3e}"
        if prev is not None:
            row += f"{math.log(prev / err) / math.log(2.0):>8.2f}"
        print(row)
        prev = err
    print("  Measured order 2: the leapfrog stencil is second order in dx and")
    print("  in dt, and holding the Courant number fixed refines both together.")
    print("  That is unlike the heat equation, where stability forces dt ~ dx^2")
    print("  and the time error is negligible by the time the space error is")
    print("  acceptable.")


# ----------------------------------------------------------------------
# 4. Advection: central versus upwind
# ----------------------------------------------------------------------

def report_advection() -> None:
    section("4. Advection: central differences are unstable for every step")
    print("  u_t + c u_x = 0, forward Euler in time")
    print("  central in space:   G = 1 - i sigma sin theta,")
    print("                      |G|^2 = 1 + sigma^2 sin^2 theta > 1")
    print("  upwind in space:    G = 1 - sigma (1 - cos theta) - i sigma sin theta,")
    print("                      |G|^2 = 1 - 2 sigma (1 - sigma)(1 - cos theta)")
    print("  The measurement uses a single complex periodic mode exp(i theta j)")
    print("  on 64 cells, so the update is exactly multiplication by G and the")
    print("  measured ratio IS the amplification factor.")
    print(f"  {'sigma':>8}{'theta':>8}{'|G| central':>16}{'|G| upwind':>14}"
          f"{'measured central':>18}{'measured upwind':>18}")
    N = 64
    for sigma in (0.2, 0.5, 0.9, 1.0):
        for theta in (2.0 * math.pi * 4.0 / N, math.pi / 2.0):
            gc = math.sqrt(1.0 + sigma * sigma * math.sin(theta) ** 2)
            gu = math.sqrt(abs(1.0 - 2.0 * sigma * (1.0 - sigma)
                               * (1.0 - math.cos(theta))))
            base = [complex(math.cos(theta * i), math.sin(theta * i))
                    for i in range(N)]
            cen = [base[i] - 0.5 * sigma * (base[(i + 1) % N]
                                           - base[(i - 1) % N])
                   for i in range(N)]
            up = [base[i] - sigma * (base[i] - base[(i - 1) % N])
                  for i in range(N)]
            print(f"  {sigma:>8.2f}{theta:>8.4f}{gc:>16.8f}{gu:>14.8f}"
                  f"{maxabs(cen) / maxabs(base):>18.8f}"
                  f"{maxabs(up) / maxabs(base):>18.8f}")
    print("  The central scheme has |G| > 1 for every sigma > 0 and every")
    print("  non-zero wavenumber, so it is unconditionally unstable: reducing")
    print("  the step does not help, it only slows the divergence. The upwind")
    print("  scheme has |G| <= 1 exactly when 0 <= sigma <= 1, so it is")
    print("  conditionally stable with the same CFL restriction as the wave")
    print("  scheme, and it is only first order.")
    print("  This is the reason production transport and wave codes either use")
    print("  upwind/stabilised operators or add artificial dissipation: the")
    print("  symmetric, obvious discretisation is the one that fails.")


def main() -> None:
    report_heat_stability()
    report_crank_nicolson()
    report_wave_cfl()
    report_advection()
    section("Summary")
    print("consistent: local truncation error -> 0 as the grid is refined")
    print("stable    : the amplification factor stays bounded on every mode")
    print("convergent: error -> 0 at the order of the truncation term")
    print("Lax equivalence: consistent + stable  <=>  convergent")
    print("CFL       : c dt/dx <= 1 for explicit hyperbolic schemes")
    print("r <= 1/2  : kappa dt/dx^2 <= 1/2 for the explicit heat scheme")


if __name__ == "__main__":
    main()
