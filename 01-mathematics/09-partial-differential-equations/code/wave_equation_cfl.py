"""The wave equation: continuum limit, d'Alembert solutions and the CFL limit.

Run:  python3 wave_equation_cfl.py
Requires: Python standard library only.

Companion to lesson 01-09-03 (The Wave Equation and Its Physical Content).

Sections
    1. Continuum limit of a mass-spring chain -> c = a sqrt(k/m)
    2. d'Alembert solutions verified by substitution
    3. Leapfrog solution of u_tt = c^2 u_xx vs the exact standing wave
    4. The Courant-Friedrichs-Lewy limit: stable, exact, and unstable
    5. Information travels along characteristics at speed c

Everything is SYNTHETIC and one-dimensional; every error is measured against
an exact solution or a verified algebraic identity.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# 1. Continuum limit of a discrete chain
# ----------------------------------------------------------------------

def report_continuum_limit() -> None:
    section("1. Continuum limit: chain of masses and springs -> wave equation")
    print("Discrete:  m d2y_i/dt2 = k (y_{i+1} - 2 y_i + y_{i-1}),  spacing a.")
    print("Trial mode y_i(t) = sin(q i a) cos(omega t) satisfies it exactly with")
    print("    omega(q) = 2 sqrt(k/m) |sin(q a / 2)|.")
    print("The PDE u_tt = c^2 u_xx follows for q a << 1 with c = a sqrt(k/m).")
    m, k, a = 1.0, 1.0, 1.0
    c_theory = a * math.sqrt(k / m)
    print(f"\n  assumed m = {m} kg, k = {k} N/m, a = {a} m  ->  "
          f"c = a sqrt(k/m) = {c_theory:.6f} m/s")
    print(f"\n  {'q a (rad)':>11}{'omega (exact)':>16}{'omega/q (speed)':>18}"
          f"{'speed / c':>12}{'relative residual':>20}")
    for m_mode in (1, 2, 4, 8, 16, 32):
        qa = m_mode * math.pi / 64.0
        om = 2.0 * math.sqrt(k / m) * abs(math.sin(qa / 2.0))
        speed = om / (qa / a)
        # Substitute the trial mode into the discrete equation at an interior
        # point, using the exact derivatives of cos(omega t).  The algebra is
        # the identity sin(qa(i+1)) - 2 sin(qa i) + sin(qa(i-1))
        #                          = -4 sin^2(qa/2) sin(qa i).
        i, t = 7, 0.37
        lhs = -m * om * om * math.sin(qa * i) * math.cos(om * t)
        rhs = k * (math.sin(qa * (i + 1)) - 2 * math.sin(qa * i)
                   + math.sin(qa * (i - 1))) * math.cos(om * t)
        scale = 4.0 * k * math.sin(qa / 2.0) ** 2 * abs(math.cos(om * t))
        residual = abs(lhs - rhs) / scale
        print(f"  {qa:>11.5f}{om:>16.8f}{speed:>18.8f}{speed/c_theory:>12.6f}"
              f"{residual:>20.2e}")
    print("\n  The residual is at round-off: the trial mode solves the discrete")
    print("  equations exactly, not approximately. The speed omega/q -> c as")
    print("  q a -> 0, and deviation grows as the wavelength approaches the")
    print("  spacing. That deviation is numerical (lattice) dispersion, and it is")
    print("  the reason a finite-difference grid distorts short wavelengths.")


# ----------------------------------------------------------------------
# 2. d'Alembert solutions verified by substitution
# ----------------------------------------------------------------------

def report_dalembert() -> None:
    section("2. d'Alembert solutions u = F(x-ct) + G(x+ct) verified by substitution")
    print("u_tt - c^2 u_xx = 0 is satisfied identically by any F and G.")
    print("Numerically: central differences of an exact travelling pulse, refined")
    print("in h, must converge to zero at second order.")
    c = 1.5

    def f(x):                                  # smooth travelling waveform
        return math.exp(-x * x) * math.cos(3.0 * x)

    def u(x, t):
        return f(x - c * t) + 0.5 * f(x + c * t)

    x0, t0 = 0.3, 0.4
    print(f"\n  c = {c}, F(x) = exp(-x^2) cos(3x), G(x) = 0.5 F(x)")
    print(f"  differentiated at x = {x0}, t = {t0}")
    print(f"\n  {'h':>10}{'|u_tt - c^2 u_xx|':>22}{'order':>8}")
    previous = None
    for step in range(6):
        h = 0.1 / (2 ** step)
        utt = (u(x0, t0 + h) - 2 * u(x0, t0) + u(x0, t0 - h)) / (h * h)
        uxx = (u(x0 + h, t0) - 2 * u(x0, t0) + u(x0 - h, t0)) / (h * h)
        residual = abs(utt - c * c * uxx)
        order = "" if previous is None else f"{math.log2(previous / residual):.2f}"
        print(f"  {h:>10.2e}{residual:>22.3e}{order:>8}")
        previous = residual
    print("\n  Order ~ 2: the residual that remains is pure finite-difference")
    print("  truncation error, so u = F(x-ct) + G(x+ct) is confirmed as an exact")
    print("  solution. Right- and left-going waves superpose independently.")
    print("  Two special superpositions that geophysics uses constantly:")
    print("    F = G = f/2     -> standing wave, u = f(x-ct)/2 + f(x+ct)/2")
    print("    G = 0          -> one-way wave, the basis of migration and of the")
    print("                       one-way (parabolic) wave equation.")


# ----------------------------------------------------------------------
# 3. Leapfrog solution vs the exact standing wave
# ----------------------------------------------------------------------

def wave_error_naive(n: int, cfl: float, tend: float, sigma: float) -> float:
    """Same problem with the naive first-order start u^{-1} = u^0."""
    dx = 1.0 / (n + 1)
    nt = max(1, int(round(tend / (cfl * dx))))
    dt = tend / nt
    c2 = sigma * sigma
    u = [math.sin(math.pi * (i + 1) * dx) for i in range(n)]
    u_prev = u[:]
    for _ in range(nt):
        u_next = [0.0] * n
        for i in range(n):
            left = u[i - 1] if i > 0 else 0.0
            right = u[i + 1] if i < n - 1 else 0.0
            u_next[i] = 2.0 * u[i] - u_prev[i] + c2 * (left - 2.0 * u[i] + right)
        u_prev, u = u, u_next
    exact = math.cos(math.pi * tend)
    return max(abs(u[i] - exact * math.sin(math.pi * (i + 1) * dx))
               for i in range(n))


def wave_error(n: int, cfl: float, tend: float) -> tuple[float, float]:
    """Leapfrog solution of u_tt = c^2 u_xx, u(0)=u(1)=0, u(x,0)=sin(pi x).

    Returns (max error against the exact standing wave, achieved Courant number).
    """
    dx = 1.0 / (n + 1)
    nt = max(1, int(round(tend / (cfl * dx))))
    dt = tend / nt
    sigma = dt / dx
    c2 = sigma * sigma
    u = [math.sin(math.pi * (i + 1) * dx) for i in range(n)]
    u_prev = [0.0] * n
    for i in range(n):
        left = u[i - 1] if i > 0 else 0.0
        right = u[i + 1] if i < n - 1 else 0.0
        u_prev[i] = u[i] + 0.5 * c2 * (left - 2.0 * u[i] + right)
    for _ in range(nt):
        u_next = [0.0] * n
        for i in range(n):
            left = u[i - 1] if i > 0 else 0.0
            right = u[i + 1] if i < n - 1 else 0.0
            u_next[i] = 2.0 * u[i] - u_prev[i] + c2 * (left - 2.0 * u[i] + right)
        u_prev, u = u, u_next
    exact = math.cos(math.pi * tend)
    return (max(abs(u[i] - exact * math.sin(math.pi * (i + 1) * dx))
                for i in range(n)), sigma)


def report_leapfrog() -> None:
    section("3. Leapfrog solution vs the exact standing wave (Courant number 0.5)")
    tend = 0.3
    print("u_tt = u_xx on (0,1), u(0,t)=u(1,t)=0, u(x,0)=sin(pi x), u_t(x,0)=0.")
    print("Exact: u = sin(pi x) cos(pi t); at t = 0.3, cos(pi t) = "
          f"{math.cos(math.pi*tend):.6f}.")
    print(f"\n  {'N':>5}{'Courant':>10}{'max error':>13}{'order':>8}"
          f"{'naive start':>14}{'ratio':>8}")
    previous = None
    for n in (20, 40, 80, 160, 320):
        err, sigma = wave_error(n, 0.5, tend)
        naive = wave_error_naive(n, 0.5, tend, sigma)
        order = "" if previous is None else f"{math.log2(previous / err):.2f}"
        print(f"  {n:>5}{sigma:>10.2f}{err:>13.3e}{order:>8}"
              f"{naive:>14.3e}{naive/err:>8.0f}")
        previous = err
    print("\n  Order ~ 2. The scheme is second order in dx and dt; because the")
    print("  Courant number is held fixed, dt also halves when dx halves.")
    print("\n  The last two columns repeat the run with the NAIVE initialisation")
    print("  u^{-1}_j = u^0_j (implying u_t = 0 to first order only, instead of the")
    print("  second-order start used above). That error falls by only a factor of two")
    print("  when the grid is halved: first order. The ratio grows without bound, which")
    print("  is the diagnostic. Initial data must be imposed to the order of the scheme.")


# ----------------------------------------------------------------------
# 4. The CFL limit
# ----------------------------------------------------------------------

def growth_experiment(cfl: float, steps: int) -> tuple[float, float, float]:
    """Run the leapfrog scheme on the most oscillatory grid mode u_i = (-1)^i.

    Returns (final max|u|, observed growth per step, theoretical factor).
    """
    n = 200
    u = [(-1.0) ** i for i in range(n)]
    u_prev = [0.0] * n
    c2 = cfl * cfl
    for _ in range(steps):
        u_next = [0.0] * n
        for i in range(n):
            left = u[i - 1] if i > 0 else 0.0
            right = u[i + 1] if i < n - 1 else 0.0
            u_next[i] = 2.0 * u[i] - u_prev[i] + c2 * (left - 2.0 * u[i] + right)
        u_prev, u = u, u_next
    final_peak = max(abs(v) for v in u)
    observed = final_peak ** (1.0 / steps)
    # |g| = root of g^2 - (2 - 4 cfl^2) g + 1 = 0 with modulus > 1.
    b = 2.0 - 4.0 * cfl * cfl
    disc = b * b - 4.0
    theoretical = (abs(b) + math.sqrt(disc)) / 2.0 if disc > 0 else 1.0
    return final_peak, observed, theoretical


def report_cfl() -> None:
    section("4. The CFL limit: c dt <= dx")
    print("Scheme:  u^{n+1}_i = 2u^n_i - u^{n-1}_i + sigma^2 (u^n_{i+1} - 2u^n_i + u^n_{i-1})")
    print("sigma = c dt / dx. von Neumann analysis: stable for sigma <= 1. For")
    print("sigma > 1 the alternating grid mode grows by |g| per step with")
    print("    g^2 - (2 - 4 sigma^2) g + 1 = 0.")
    print("\n(a) The alternating grid mode u_i = (-1)^i, initial velocity zero.")
    print(f"\n  {'sigma':>8}{'steps':>7}{'final max|u|':>15}"
          f"{'observed growth/step':>22}{'theory':>10}{'verdict':>12}")
    for cfl, steps in ((0.5, 2000), (0.9, 2000), (1.01, 200), (1.05, 100)):
        final_peak, observed, theory = growth_experiment(cfl, steps)
        verdict = "stable" if cfl < 1.0 else "UNSTABLE"
        print(f"  {cfl:>8.2f}{steps:>7}{final_peak:>15.4g}"
              f"{observed:>22.6f}{theory:>10.6f}{verdict:>12}")
    print("\n  Below sigma = 1 the mode stays bounded: the amplification factor has")
    print("  modulus exactly 1, so a wave code at sigma = 0.5 does not amplify")
    print("  round-off. Above sigma = 1 the observed growth matches the predicted")
    print("  worst-mode factor, so the instability is exponential in the step count")
    print("  and no amount of arithmetic precision removes it.")
    exact_err, sigma_used = wave_error(99, 1.0, 0.3)
    print(f"\n(b) At sigma = 1.0 exactly (N = 99, dx = dt = 0.01) the standing-wave")
    print(f"    error is {exact_err:.3e} (achieved sigma = {sigma_used:.6f}): the stencil")
    print("    lands on the characteristics and the scheme is exact for")
    print("    one-dimensional constant-velocity propagation.")
    print("\n  Why the limit exists: the numerical domain of dependence widens by one")
    print("  cell per time step, so it contains the physical cone x' = x +- c dt only")
    print("  if c dt <= dx. Violate that and the scheme is asked to use information")
    print("  from a region it never saw. This is the Courant-Friedrichs-Lewy")
    print("  condition, and every explicit wave solver respects it.")


# ----------------------------------------------------------------------
# 5. Characteristics and Riemann invariants
# ----------------------------------------------------------------------

def report_characteristics() -> None:
    section("5. Information travels along characteristics at speed c")
    print("For u_tt = c^2 u_xx, the combinations")
    print("    u_t - c u_x  is constant along  dx/dt = +c")
    print("    u_t + c u_x  is constant along  dx/dt = -c")
    c = 2.0

    def f(x):
        return math.exp(-x * x)

    def u(x, t):
        return f(x - c * t) + 0.3 * f(x + c * t)

    def ut(x, t):
        h = 1e-6
        return (u(x, t + h) - u(x, t - h)) / (2 * h)

    def ux(x, t):
        h = 1e-6
        return (u(x + h, t) - u(x - h, t)) / (2 * h)

    print(f"\n  c = {c}, u = F(x - ct) + 0.3 F(x + ct), F(x) = exp(-x^2)")
    print(f"\n  {'t':>8}{'x = x0 + ct':>14}{'u_t - c u_x':>16}{'x = x0 - ct':>14}"
          f"{'u_t + c u_x':>16}")
    x0 = 0.0
    for t in (0.0, 0.1, 0.2, 0.3):
        xr = x0 + c * t
        xl = x0 - c * t
        print(f"  {t:>8.1f}{xr:>14.4f}{ut(xr, t) - c * ux(xr, t):>16.10f}"
              f"{xl:>14.4f}{ut(xl, t) + c * ux(xl, t):>16.10f}")
    print("\n  Along x = x0 + ct the right-going invariant is constant because the")
    print("  disturbance f(x - ct) is unchanged there; along x = x0 - ct the")
    print("  left-going invariant is constant because g(x + ct) is unchanged")
    print("  there. Each family carries its own signal. Setting G = 0 makes the")
    print("  right-going invariant exactly zero — the one-way wave equation")
    print("  u_t + c u_x = 0 used in lesson 06 on characteristics.")
    print("  Physical reading: a disturbance at (x0, 0) can only influence points")
    print("  inside the cone |x - x0| <= c t. This is why first-arrival times")
    print("  invert for structure, and why the numerical stencil must respect it.")



# ----------------------------------------------------------------------
# 6. Variable velocity: what survives of the sigma = 1 exactness
# ----------------------------------------------------------------------

def variable_velocity_solve(n: int, tend: float, cfl: float, cfun):
    """Leapfrog solution of u_tt = c(x)^2 u_xx with fixed ends."""
    dx = 1.0 / (n + 1)
    cmax = max(cfun(i * dx) for i in range(n + 2))
    dt = cfl * dx / cmax
    nt = int(round(tend / dt))
    dt = tend / nt
    u = [math.sin(math.pi * (i + 1) * dx) for i in range(n)]
    u_prev = [0.0] * n
    for i in range(n):
        x = (i + 1) * dx
        c2 = (cfun(x) * dt / dx) ** 2
        left = u[i - 1] if i > 0 else 0.0
        right = u[i + 1] if i < n - 1 else 0.0
        u_prev[i] = u[i] + 0.5 * c2 * (left - 2.0 * u[i] + right)
    for _ in range(nt):
        new = [0.0] * n
        for i in range(n):
            x = (i + 1) * dx
            c2 = (cfun(x) * dt / dx) ** 2
            left = u[i - 1] if i > 0 else 0.0
            right = u[i + 1] if i < n - 1 else 0.0
            new[i] = 2.0 * u[i] - u_prev[i] + c2 * (left - 2.0 * u[i] + right)
        u_prev, u = u, new
    return u, dx


def report_variable_velocity() -> None:
    section("6. Variable velocity: order 2 survives, exactness does not")
    print("u_tt = c(x)^2 u_xx on (0,1), fixed ends, u(x,0) = sin(pi x), u_t = 0,")
    print("c(x) = 1 + 0.5 sin(2 pi x); Courant number 0.5 based on c_max = 1.5.")
    print("Reference: the same scheme on N = 3200, interpolated to the coarse grid.")
    cfun = lambda x: 1.0 + 0.5 * math.sin(2.0 * math.pi * x)
    nref, tend = 3200, 0.3
    ref, dxr = variable_velocity_solve(nref, tend, 0.5, cfun)

    def reference_at(x):
        t = x / dxr
        j = max(0, min(nref - 2, int(math.floor(t)) - 1))
        f = t - (j + 1)
        return (1.0 - f) * ref[j] + f * ref[j + 1]

    print(f"\n  {'N':>6}{'dx':>11}{'max error':>14}{'order':>8}")
    previous = None
    for n in (50, 100, 200, 400, 800):
        u, dx = variable_velocity_solve(n, tend, 0.5, cfun)
        err = max(abs(u[i] - reference_at((i + 1) * dx)) for i in range(n))
        order = "" if previous is None else f"{math.log2(previous / err):.2f}"
        print(f"  {n:>6}{dx:>11.2e}{err:>14.3e}{order:>8}")
        previous = err
    print("\n  The order is still 2, even though the velocity varies and the time")
    print("  step is set by the largest velocity: the stencil is second-order")
    print("  accurate and the coefficient is smooth, so sampling it at the nodes")
    print("  costs nothing at this order. What is lost is the EXACTNESS at")
    print("  Courant number 1, because no single dt/dx can place the stencil on the")
    print("  characteristics at every node once c varies.")
    print("  A discontinuous c(x) misaligned with the grid is the harder case: the")
    print("  equation must then be written in conservation form and the coefficient")
    print("  averaged over the cell, or the order degrades.")


def main() -> None:
    report_continuum_limit()
    report_dalembert()
    report_leapfrog()
    report_cfl()
    report_characteristics()
    report_variable_velocity()


if __name__ == "__main__":
    main()
