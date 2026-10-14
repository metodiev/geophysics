"""Separation of variables: series solutions with real boundary conditions.

Run:  python3 separation_of_variables.py
Requires: Python standard library only.

Companion to lesson 01-09-05 (Separation of Variables and Boundary
Conditions).

Sections
    1. Bounded-slab heat conduction: series vs finite differences, order 2
    2. Eigenfunction expansions converge spectrally; eigenvalues set the decay
    3. Steady conduction in a layered Earth (geothermal gradient), verified by
       substitution
    4. Vibration of a bounded string: modes, orthogonality, and the free
       parameters of the problem

All parameters are ILLUSTRATIVE and stated explicitly. Grids and bodies are
SYNTHETIC; every error is measured against an analytic series solution.
"""

import math

SECONDS_PER_YEAR = 365.25 * 24.0 * 3600.0


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# 1. Slab heat conduction: separation of variables vs finite differences
# ----------------------------------------------------------------------

def triangle(x: float) -> float:
    """Plucked-string / triangular initial condition on [0,1], peak 1 at 0.5."""
    return 2.0 * x if x <= 0.5 else 2.0 * (1.0 - x)


def smooth_ic(x: float) -> float:
    """Two-mode initial condition: sin(pi x) + 0.5 sin(3 pi x)."""
    return math.sin(math.pi * x) + 0.5 * math.sin(3.0 * math.pi * x)


_COEFF_CACHE: dict = {}


def sine_coefficients(func, nterms: int, samples: int = 4000, key: str = ""):
    """b_n = 2 integral_0^1 f(x) sin(n pi x) dx, by the midpoint rule."""
    cache_key = (key, nterms)
    if cache_key in _COEFF_CACHE:
        return _COEFF_CACHE[cache_key]
    h = 1.0 / samples
    coeffs = []
    for n in range(1, nterms + 1):
        total = 0.0
        for k in range(samples):
            x = (k + 0.5) * h
            total += func(x) * math.sin(n * math.pi * x)
        coeffs.append(2.0 * total * h)
    _COEFF_CACHE[cache_key] = coeffs
    return coeffs


def series_solution(coeffs, x: float, t: float, kappa: float = 1.0) -> float:
    """u(x,t) = sum b_n sin(n pi x) exp(-kappa n^2 pi^2 t) on (0,1)."""
    total = 0.0
    for n, b in enumerate(coeffs, start=1):
        total += b * math.sin(n * math.pi * x) \
            * math.exp(-kappa * n * n * math.pi ** 2 * t)
    return total


def fd_heat(ic, n: int, tend: float, kappa: float = 1.0, r: float = 0.4):
    """Explicit solution of u_t = kappa u_xx, u(0)=u(1)=0, u(x,0) = ic(x)."""
    dx = 1.0 / (n + 1)
    dt = r * dx * dx / kappa
    nt = int(math.ceil(tend / dt))
    dt = tend / nt
    r = kappa * dt / (dx * dx)
    u = [ic((i + 1) * dx) for i in range(n)]
    for _ in range(nt):
        new = u[:]
        for i in range(n):
            left = u[i - 1] if i > 0 else 0.0
            right = u[i + 1] if i < n - 1 else 0.0
            new[i] = u[i] + r * (left - 2.0 * u[i] + right)
        u = new
    return u, dx


def report_slab_heat() -> None:
    section("1. Bounded-slab heat conduction: series solution vs finite differences")
    print("u_t = u_xx on (0,1), u(0,t) = u(1,t) = 0 (fixed temperatures),")
    print("u(x,0) = sin(pi x) + 0.5 sin(3 pi x)  (a two-mode initial profile).")
    print("Separation gives u = sum_n b_n sin(n pi x) exp(-kappa n^2 pi^2 t),")
    print("with b_n = 2 integral f(x) sin(n pi x) dx.")
    tend = 0.05
    coeffs = sine_coefficients(smooth_ic, 12, key="smooth")
    print("\n  coefficients recovered by numerical projection:")
    print("    " + ", ".join(f"b_{n} = {coeffs[n-1]:+.6f}" for n in range(1, 8)))
    print("  The projection returns b_1 = 1 and b_3 = 0.5 and zero elsewhere, so the")
    print("  smooth initial condition is already written in the eigenbasis.")
    print(f"\n  At t = {tend} the exact solution of the PDE is")
    print("    u = sin(pi x) e^{-pi^2 t} + 0.5 sin(3 pi x) e^{-9 pi^2 t}")
    print("  Compare the explicit finite-difference field with it:")
    print(f"\n  {'N':>5}{'dx':>11}{'max |FD - exact|':>20}{'order':>8}")
    previous = None
    for n in (25, 50, 100, 200):
        u, dx = fd_heat(smooth_ic, n, tend)
        err = 0.0
        for i in range(n):
            x = (i + 1) * dx
            exact = (math.sin(math.pi * x) * math.exp(-math.pi ** 2 * tend)
                     + 0.5 * math.sin(3 * math.pi * x)
                     * math.exp(-9 * math.pi ** 2 * tend))
            err = max(err, abs(u[i] - exact))
        order = "" if previous is None else f"{math.log2(previous / err):.2f}"
        print(f"  {n:>5}{dx:>11.2e}{err:>20.3e}{order:>8}")
        previous = err
    print("\n  Order ~ 2. The series solution supplies the exact answer that the")
    print("  difference scheme is checked against; both obey the same boundary")
    print("  conditions, which is the point of choosing an eigenfunction basis.")


def report_eigen_decay() -> None:
    section("2. Eigenvalues set the decay rate; the expansion is spectrally accurate")
    coeffs = sine_coefficients(triangle, 400, key="triangle")
    tend = 0.05
    print("Now a different initial condition, the triangular pluck:")
    print("  f(x) = 2x for x <= 1/2, 2(1-x) for x > 1/2.")
    print("  Its coefficients decay like 1/n^2:")
    print("    " + ", ".join(f"b_{n} = {coeffs[n-1]:+.6f}" for n in range(1, 7)))
    print("  Only odd n survive, because the pluck is symmetric about x = 1/2.")
    print("\nTruncating the series at N terms and comparing with the 400-term")
    print("reference at t = 0.05:")
    print(f"\n  {'N':>5}{'max truncation error':>24}")
    for nterm in (1, 2, 3, 5, 10, 15, 20, 30, 50):
        err = max(abs(series_solution(coeffs[:nterm], i / 500.0, tend)
                      - series_solution(coeffs, i / 500.0, tend))
                  for i in range(1, 500))
        print(f"  {nterm:>5}{err:>24.3e}")
    print("\n  The error collapses far faster than the 1/n^2 coefficients suggest,")
    print("  because the factor exp(-n^2 pi^2 t) suppresses high modes: each extra")
    print("  term is smaller than the previous by exp(-(2n+1) pi^2 t). An")
    print("  eigenfunction expansion is spectrally accurate for smooth data.")
    print("\n  Decay of a single mode. Initialise u = sin(3 pi x) and measure the")
    print("  decay rate of the midpoint amplitude:")
    kappa, n, dx = 1.0, 400, 1.0 / 401
    r = 0.4
    dt = r * dx * dx / kappa
    steps = 400
    u = [math.sin(3 * math.pi * (i + 1) * dx) for i in range(n)]
    amplitude = [u[n // 2]]
    for _ in range(steps):
        new = [0.0] * n
        for i in range(n):
            left = u[i - 1] if i > 0 else 0.0
            right = u[i + 1] if i < n - 1 else 0.0
            new[i] = u[i] + r * (left - 2.0 * u[i] + right)
        u = new
        amplitude.append(u[n // 2])
    t = steps * dt
    measured = math.log(amplitude[0] / amplitude[-1]) / t
    pde_rate = kappa * 9.0 * math.pi ** 2
    discrete_rate = 4.0 * kappa * math.sin(3.0 * math.pi * dx / 2.0) ** 2 / (dx * dx)
    print(f"    measured decay rate of sin(3 pi x)      = {measured:.6f} per unit time")
    print(f"    eigenvalue of the PDE, kappa (3 pi)^2   = {pde_rate:.6f}")
    print(f"    discrete eigenvalue 4 kappa sin^2(3 pi dx/2)/dx^2 = {discrete_rate:.6f}")
    print(f"    relative difference from the discrete value = "
          f"{abs(measured - discrete_rate)/discrete_rate:.2e}")
    print("\n  The measurement reproduces the discrete eigenvalue, not the continuous")
    print("  one: the finite-difference operator has its own spectrum, and it differs")
    print("  from the PDE spectrum by O(dx^2). Higher modes decay faster, which is why")
    print("  a buried heat pulse is smoothed into its lowest harmonic first.")


# ----------------------------------------------------------------------
# 3. Steady conduction in a layered Earth
# ----------------------------------------------------------------------

def report_geothermal() -> None:
    section("3. Steady conduction in the crust: the geothermal gradient")
    print("Steady heat conduction with uniform radiogenic production A and z")
    print("positive downward:")
    print("    d/dz (k dT/dz) + A = 0")
    print("    T(z) = T_s + (q0/k) z - (A/(2k)) z^2")
    print("The quadratic term is negative: radiogenic heat makes the geotherm")
    print("concave, because the upward heat flow decreases with depth as")
    print("q(z) = q0 - A z: part of the surface flow was generated on the way up.")
    k = 2.5                 # W m^-1 K^-1, ILLUSTRATIVE crustal conductivity
    q0 = 0.065              # W m^-2, ILLUSTRATIVE continental heat flow
    A = 1.0e-6              # W m^-3 = 1 microW/m^3, ILLUSTRATIVE production
    T_s = 10.0              # deg C at the surface
    print(f"\n  assumed k = {k} W/(m K), q0 = {q0} W/m^2, "
          f"A = {A:.1e} W/m^3, T_s = {T_s} deg C")
    gradient = q0 / k
    print(f"\n  surface gradient q0/k = {gradient*1000:.3f} K/km "
          f"(= {gradient:.6f} K/m)")
    print(f"\n  {'depth (km)':>12}{'T, A = 0 (C)':>15}{'T with A (C)':>15}"
          f"{'curvature (C)':>16}")
    for z_km in (5, 10, 20, 30, 40):
        z = z_km * 1e3
        linear = T_s + gradient * z
        full = T_s + gradient * z - A * z * z / (2.0 * k)
        print(f"  {z_km:>12}{linear:>15.2f}{full:>15.2f}"
              f"{full - linear:>16.2f}")
    print(f"\n  Verification by substitution (residual of k T'' + A at z = 30 km):")
    z = 3.0e4
    h = 1.0

    def t2(zz):
        return T_s + gradient * zz - A * zz * zz / (2.0 * k)

    residual = k * (t2(z + h) - 2 * t2(z) + t2(z - h)) / (h * h) + A
    print(f"    |k T'' + A| = {abs(residual):.3e} (a central difference is exact")
    print("    for a quadratic, so what is left is round-off)")
    print("\n  The curvature term matters: at 30 km it removes")
    print(f"  {A*z*z/(2*k):.1f} K from the linear extrapolation, about a quarter of the")
    print("  total. A single 'gradient in K/km' quoted without a depth range and a")
    print("  production model is therefore under-specified, and real k and A vary")
    print("  with lithology and depth, which is why these numbers are illustrative.")
    kappa_th = 1.0e-6
    tau = (3.0e4) ** 2 / kappa_th
    print(f"\n  Is steady state even reachable? With kappa = {kappa_th:.1e} m^2/s,")
    print(f"  tau ~ L^2/kappa for L = 30 km is {tau:.3e} s = "
          f"{tau/SECONDS_PER_YEAR/1e6:.1f} Myr.")
    print("  Where the lithosphere is younger than that, a steady geotherm is an")
    print("  assumption to be checked, not a default — exactly the caution from")
    print("  lesson 02 on diffusive timescales.")


# ----------------------------------------------------------------------
# 4. Vibration of a bounded string
# ----------------------------------------------------------------------

def report_string_modes() -> None:
    section("4. Vibration of a bounded string: modes and orthogonality")
    c, L = 1.0, 1.0
    print("u_tt = c^2 u_xx on (0,L), u(0,t) = u(L,t) = 0.")
    print("Separation gives u_n(x,t) = sin(n pi x/L) cos(omega_n t) with")
    print(f"    omega_n = n pi c / L   (c = {c}, L = {L}).")
    print(f"\n  {'n':>4}{'omega_n':>12}{'frequency (Hz)':>17}"
          f"{'residual, h = 1e-3':>22}")
    h = 1.0e-3

    def mode(n, x, t):
        return math.sin(n * math.pi * x / L) * math.cos(n * math.pi * c * t / L)

    for n in (1, 2, 3, 4, 5):
        omega = n * math.pi * c / L
        x0, t0 = 0.31, 0.23
        utt = (mode(n, x0, t0 + h) - 2 * mode(n, x0, t0)
               + mode(n, x0, t0 - h)) / (h * h)
        uxx = (mode(n, x0 + h, t0) - 2 * mode(n, x0, t0)
               + mode(n, x0 - h, t0)) / (h * h)
        print(f"  {n:>4}{omega:>12.6f}{omega/(2*math.pi):>17.6f}"
              f"{abs(utt - c * c * uxx):>22.3e}")
    print("\n  Each mode is an exact solution, so what remains is pure")
    print("  finite-difference truncation error. Refining the steps for the n = 1")
    print("  mode (at x = 0.31, t = 0.23) makes it vanish at second order. The time")
    print("  step is taken as 0.7 times the space step: when the two steps are equal")
    print("  and omega = pi c/L, the two discrete operators annihilate this mode")
    print("  identically and the residual collapses to round-off instead.")
    previous = None
    print(f"\n  {'hx':>10}{'ht':>10}{'|u_tt - c^2 u_xx|':>20}{'order':>8}")
    for step in range(4):
        hx = 1.0e-2 / (2 ** step)
        ht = 0.7 * hx
        utt = (mode(1, 0.31, 0.23 + ht) - 2 * mode(1, 0.31, 0.23)
               + mode(1, 0.31, 0.23 - ht)) / (ht * ht)
        uxx = (mode(1, 0.31 + hx, 0.23) - 2 * mode(1, 0.31, 0.23)
               + mode(1, 0.31 - hx, 0.23)) / (hx * hx)
        res = abs(utt - c * c * uxx)
        order = "" if previous is None else f"{math.log2(previous / res):.2f}"
        print(f"  {hx:>10.2e}{ht:>10.2e}{res:>20.3e}{order:>8}")
        previous = res
    print("\n  Orthogonality, integral_0^L sin(n pi x/L) sin(m pi x/L) dx:")
    samples = 200_000
    h = L / samples
    print(f"\n  {'n':>4}{'m':>4}{'numerical':>15}{'exact (L/2) delta_nm':>24}")
    for (n, m) in ((1, 1), (1, 2), (2, 3), (3, 3), (4, 7)):
        total = sum(math.sin(n * math.pi * (i + 0.5) * h / L)
                    * math.sin(m * math.pi * (i + 0.5) * h / L)
                    for i in range(samples)) * h
        exact = L / 2.0 if n == m else 0.0
        print(f"  {n:>4}{m:>4}{total:>15.9f}{exact:>24.9f}")
    print("\n  Orthogonality is what makes the coefficients decouple: each mode is")
    print("  projected out independently, so the initial condition's shape is")
    print("  encoded in the b_n and its time evolution is then fully determined.")
    print("\n  Free versus forced parameters: the eigenvalues omega_n are properties")
    print("  of the equation, the geometry and the homogeneous boundary conditions.")
    print("  The amplitudes b_n are properties of the initial condition. This is the")
    print("  same split that distinguishes the Earth's normal modes (eigenvalues)")
    print("  from the excitation of a particular earthquake (amplitudes).")



def report_terms_needed() -> None:
    section("5. How many terms are enough? (accuracy vs time)")
    coeffs = sine_coefficients(triangle, 400, key="triangle")
    print("Using the triangular initial profile of Section 2 and the 400-term series")
    print("as reference, find the smallest N for which the maximum error over 399")
    print("interior points is below 1e-8.")
    print(f"\n  {'t':>8}{'terms for 1e-8':>16}{'error at N=5':>15}"
          f"{'predicted N = 1.366/sqrt(t)':>32}")
    grid = [i / 400.0 for i in range(1, 400)]
    for t in (0.5, 0.05, 0.005):
        reference = [series_solution(coeffs, x, t) for x in grid]
        needed = None
        for nterm in range(1, 201):
            err = max(abs(series_solution(coeffs[:nterm], x, t) - reference[k])
                      for k, x in enumerate(grid))
            if err < 1e-8:
                needed = nterm
                break
        err5 = max(abs(series_solution(coeffs[:5], x, t) - reference[k])
                   for k, x in enumerate(grid))
        predicted = 1.366 / math.sqrt(t)
        print(f"  {t:>8.3f}{str(needed):>16}{err5:>15.3e}{predicted:>32.1f}")
    print("\n  Fewer terms are needed the longer the time, because mode n carries the")
    print("  factor exp(-n^2 pi^2 t): the terms that must be retained are those with")
    print("  n^2 pi^2 t below ln(1/accuracy), giving N ~ sqrt(ln(1/eps)/t)/pi. The")
    print("  prediction is an upper bound and the measured counts are slightly lower,")
    print("  because the coefficients also decay like 1/n^2. The scaling N ~ t^-1/2")
    print("  is the practical rule, and it is why the series is the wrong tool for")
    print("  very short times.")


def main() -> None:
    report_slab_heat()
    report_eigen_decay()
    report_geothermal()
    report_string_modes()
    report_terms_needed()


if __name__ == "__main__":
    main()
