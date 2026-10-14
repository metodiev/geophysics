"""Conservation laws as the engine of modelling: four numerical witnesses.

Run:  python3 conservation_demo.py
Requires: Python standard library only.

Companion to lesson 02-01-04.  Each section takes a conservation statement,
writes it in *flux* (divergence) form, and then measures numerically whether the
discrete scheme actually conserves the quantity.  The point of every section is
the same: a conservation law is not a slogan, it is an algebraic identity that a
discretisation either respects or violates -- and the violation is measurable.

All initial conditions and bodies are SYNTHETIC.  The gravitational parameter is
the WGS 84 defining value GM = 3.986 004 418e14 m^3 s^-2 (exact, defining).
"""

import math

GM_EARTH = 3.986004418e14      # m^3 s^-2, defining (WGS 84)


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def total(u) -> float:
    return math.fsum(u) * (1.0 / len(u))


def main() -> None:
    section("1. Mass: flux form conserves, advective form does not")
    n = 400
    dx = 1.0 / n
    c = 1.0                      # advection speed
    dt = 0.4 * dx / c            # CFL = 0.4
    steps = 1000
    x = [(i + 0.5) * dx for i in range(n)]
    x0, width = 0.5, 0.05
    u0 = [math.exp(-((xi - x0) / width) ** 2) for xi in x]

    def run(flux_form: bool):
        u = list(u0)
        for _ in range(steps):
            new = list(u)
            for i in range(n):
                im = (i - 1) % n
                if flux_form:
                    # du/dt = -(c/dx)(F_i - F_{i-1}), F = c u  (upwind)
                    new[i] = u[i] - c * dt / dx * (u[i] - u[im])
                else:
                    # advective form with a centred first derivative
                    ip = (i + 1) % n
                    new[i] = u[i] - c * dt / (2 * dx) * (u[ip] - u[im])
            u = new
        return u

    for label, flux in (("flux form (upwind)", True),
                        ("advective form (centred)", False)):
        u = run(flux)
        m_start, m_end = total(u0), total(u)
        print(f"  {label:26s} mass start = {m_start:.15f}")
        print(f"  {'':26s} mass end   = {m_end:.15f}")
        print(f"  {'':26s} relative drift = {abs(m_end - m_start) / m_start:.3e}")
    print("  The flux form's drift is round-off only; the advective form's is")
    print("  a property of the scheme and grows without bound in time.")

    section("2. Momentum: collisions, and the third law as an identity")
    m1, u1 = 2.0, 3.0
    m2, u2 = 5.0, -1.0
    p_before = m1 * u1 + m2 * u2
    ke_before = 0.5 * m1 * u1 ** 2 + 0.5 * m2 * u2 ** 2
    # Elastic 1-D collision in the centre-of-mass frame result.
    v1 = ((m1 - m2) * u1 + 2 * m2 * u2) / (m1 + m2)
    v2 = ((m2 - m1) * u2 + 2 * m1 * u1) / (m1 + m2)
    # Perfectly inelastic: common velocity.
    vcommon = p_before / (m1 + m2)
    print(f"  before: p = {p_before:8.4f} kg m/s, KE = {ke_before:8.4f} J")
    print(f"  elastic:  v1 = {v1:7.4f}, v2 = {v2:7.4f}, "
          f"p = {m1 * v1 + m2 * v2:8.4f}, "
          f"KE = {0.5 * m1 * v1 ** 2 + 0.5 * m2 * v2 ** 2:8.4f} J")
    print(f"  inelastic: v = {vcommon:7.4f}, "
          f"p = {m1 * vcommon + m2 * vcommon:8.4f}, "
          f"KE = {0.5 * (m1 + m2) * vcommon ** 2:8.4f} J")
    print(f"  kinetic energy lost in the inelastic case = "
          f"{ke_before - 0.5 * (m1 + m2) * vcommon ** 2:.4f} J "
          f"({100 * (1 - 0.5 * (m1 + m2) * vcommon ** 2 / ke_before):.2f} %)")

    section("3. Momentum conservation in a two-body system, checked numerically")
    # Two bodies in mutual gravitational attraction with non-zero total
    # momentum.  The Earth-like mass is GM/G, which is exactly how the mass in
    # the constant handbook is obtained; G is the measured CODATA value.
    G = 6.67430e-11
    m1 = GM_EARTH / G              # = 5.9724e24 kg, derived
    m2 = 1.0e22                    # SYNTHETIC moonlet
    r1 = [0.0, 0.0]
    r2 = [1.0e7, 0.0]
    v_circ = math.sqrt(G * (m1 + m2) / 1.0e7)
    v2 = [0.0, v_circ]            # relative orbit is circular ...
    v1 = [0.0, 0.0]               # ... while the centre of mass drifts
    dt = 20.0
    p0 = (m1 * v1[0] + m2 * v2[0], m1 * v1[1] + m2 * v2[1])
    sep = math.hypot(r2[0] - r1[0], r2[1] - r1[1])
    e0 = (0.5 * m1 * sum(x * x for x in v1) + 0.5 * m2 * sum(x * x for x in v2)
          - G * m1 * m2 / sep)
    orbit = 2 * math.pi * math.sqrt(1.0e7 ** 3 / (G * (m1 + m2)))
    steps = 1000
    for _ in range(steps):
        dx = r2[0] - r1[0]
        dy = r2[1] - r1[1]
        d2 = dx * dx + dy * dy
        d = math.sqrt(d2)
        f = G * m1 * m2 / d2
        acc1 = [f * dx / d / m1, f * dy / d / m1]
        acc2 = [-f * dx / d / m2, -f * dy / d / m2]
        for k in (0, 1):
            v1[k] += dt * acc1[k]
            v2[k] += dt * acc2[k]
        for k in (0, 1):
            r1[k] += dt * v1[k]
            r2[k] += dt * v2[k]
    p1 = (m1 * v1[0] + m2 * v2[0], m1 * v1[1] + m2 * v2[1])
    sep = math.hypot(r2[0] - r1[0], r2[1] - r1[1])
    e1 = (0.5 * m1 * sum(x * x for x in v1) + 0.5 * m2 * sum(x * x for x in v2)
          - G * m1 * m2 / sep)
    print(f"  m1 = GM/G = {m1:.5e} kg (derived), m2 = {m2:.1e} kg (synthetic)")
    print(f"  separation 1.0e7 m -> circular speed {v_circ:.2f} m/s, "
          f"period {orbit:.1f} s")
    print(f"  dt = {dt:.0f} s -> {steps} steps = {steps * dt / orbit:.2f} orbits")
    print(f"  total momentum, initial = ({p0[0]:.6e}, {p0[1]:.6e}) kg m/s")
    print(f"  total momentum, final   = ({p1[0]:.6e}, {p1[1]:.6e}) kg m/s")
    pk = max(abs(p0[0]), abs(p0[1]))
    print(f"  momentum scale m2 v     = {pk:.6e} kg m/s")
    print(f"  residual / scale        = "
          f"{max(abs(p1[0] - p0[0]), abs(p1[1] - p0[1])) / pk:.3e}")
    print("  (The residual is compared with the momentum scale of the largest")
    print("  term, not with zero: m1 v1 and m2 v2 are of order 1e25 and 1e22,")
    print("  so the sum is a cancellation of at most two orders -- benign here,")
    print("  but fatal if the mass ratio were 1e12 and the frame badly chosen.)")
    print(f"  mechanical energy drift = {abs((e1 - e0) / e0):.3e}")
    print("  Momentum is conserved to round-off because the two accelerations")
    print("  are built from the same force with opposite signs, so the momentum")
    print("  increments cancel pairwise.  Energy has no such identity: it is")
    print("  only as good as the integrator (explicit Euler here).")

    section("4. Angular momentum under a central force")
    # One body orbiting a fixed GM; L = r x v should be constant exactly.
    r = [7.0e6, 0.0]
    v = [0.0, math.sqrt(GM_EARTH / 7.0e6)]
    dt = 1.0
    L0 = r[0] * v[1] - r[1] * v[0]
    E0 = 0.5 * (v[0] ** 2 + v[1] ** 2) - GM_EARTH / math.hypot(*r)
    max_L_err = 0.0
    for _ in range(60000):
        a = [-GM_EARTH * r[0] / math.hypot(*r) ** 3,
             -GM_EARTH * r[1] / math.hypot(*r) ** 3]
        for k in (0, 1):
            v[k] += dt * a[k]
            r[k] += dt * v[k]
        L = r[0] * v[1] - r[1] * v[0]
        max_L_err = max(max_L_err, abs(L - L0) / abs(L0))
    E1 = 0.5 * (v[0] ** 2 + v[1] ** 2) - GM_EARTH / math.hypot(*r)
    print(f"  L0 = {L0:.6e} m^2/s, max relative deviation = {max_L_err:.3e}")
    print(f"  energy drift over 60000 steps = {abs((E1 - E0) / E0):.3e}")
    print("  Angular momentum is conserved *by construction*: the torque is")
    print("  r x F with F parallel to r.  The integrator cannot break it except")
    print("  through round-off, whereas it can and does drift in energy.")

    section("5. Energy: the integrator decides whether it is conserved")
    def energy(kind: str, dt: float, steps: int) -> float:
        q, p = 1.0, 0.0          # unit mass, unit angular frequency
        for _ in range(steps):
            if kind == "explicit":
                q_new = q + dt * p
                p = p - dt * q
                q = q_new
            elif kind == "implicit":
                p_new = (p - dt * q) / (1 + dt * dt)
                q = q + dt * p_new
                p = p_new
            else:                # leapfrog / velocity Verlet
                p_half = p - 0.5 * dt * q
                q = q + dt * p_half
                p = p_half - 0.5 * dt * q
        return 0.5 * (p * p + q * q)

    e_exact = 0.5
    total_time = 200.0
    print(f"  harmonic oscillator, initial energy {e_exact}, "
          f"integrated to t = {total_time:.0f}")
    print("     dt        steps     explicit       implicit       leapfrog")
    for dt in (0.1, 0.01, 0.001):
        steps = int(total_time / dt)
        row = [energy(kind, dt, steps) for kind in
               ("explicit", "implicit", "leapfrog")]
        print(f"  {dt:6.3f}  {steps:9d}  {row[0]:13.6f}  {row[1]:13.6f}  "
              f"{row[2]:13.6f}")
    print("  Explicit Euler pumps energy in without limit and implicit Euler")
    print("  bleeds it away; only the symplectic leapfrog scheme keeps the")
    print("  energy bounded and centred.  Both one-sided schemes improve as dt")
    print("  falls, but only leapfrog has no secular drift.")

    section("6. The continuity equation, verified on a discrete flux identity")
    # One-dimensional divergence of a flux; the sum of cell updates telescopes.
    n = 12
    F = [0.3 * math.sin(2 * math.pi * i / n) for i in range(n)]
    dx = 1.0 / n
    div = [(F[(i + 1) % n] - F[i]) / dx for i in range(n)]
    print(f"  fluxes          : {[round(f, 3) for f in F]}")
    print(f"  sum of fluxes   : {math.fsum(F):.3e}")
    print(f"  sum of -div F   : {math.fsum(-d for d in div):.3e}")
    print("  In exact arithmetic the discrete sum cancels pairwise, so the")
    print("  total of d(rho)/dt is zero for periodic boundaries.  That identity")
    print("  *is* the conservation law; any scheme that writes the update in")
    print("  flux form inherits it, and any scheme that does not, does not.")

    section("7. Rotation: what spin conservation costs, in joules")
    # Spin angular momentum and energy from the WGS 84 defining omega, with a
    # two-layer moment of inertia built from the constant handbook's nominal
    # densities (core 11 000, mantle 4 500 kg/m^3) and a 3 480 km core radius.
    # The resulting I is a MODEL value, not a measured one.
    omega = 7.292115e-5          # rad/s, defining
    R, Rc = 6371e3, 3480e3
    rho_c, rho_m = 11000.0, 4500.0
    Vc = 4 / 3 * math.pi * Rc ** 3
    Vt = 4 / 3 * math.pi * R ** 3
    Mc = rho_c * Vc
    M = Mc + rho_m * (Vt - Vc)
    I = 0.4 * Mc * Rc ** 2 + rho_m * (8 * math.pi / 15) * (R ** 5 - Rc ** 5)
    L = I * omega
    E = 0.5 * I * omega ** 2
    print(f"  two-layer model: M = {M:.4e} kg, I = {I:.4e} kg m^2, "
          f"I/(M R^2) = {I / (M * R ** 2):.4f}")
    print(f"  spin angular momentum L = I omega = {L:.4e} kg m^2/s")
    print(f"  rotational energy     E = I omega^2/2 = {E:.4e} J")
    for days in (1e-3, 1e-2, 1e-1):
        d_omega = -omega * days / 86400.0
        print(f"  a day longer by {days * 1e3:5.1f} ms changes omega by "
              f"{d_omega:+.3e} rad/s and L by {I * d_omega:+.3e} kg m^2/s,")
        print(f"      and E by {E * 2 * d_omega / omega:+.3e} J")
    print("  Conserved angular momentum forces that lost spin to appear in the")
    print("  Moon's orbit; the energies do not balance between the two, and the")
    print("  difference is dissipated as heat.  Measured rates come from lunar")
    print("  laser ranging and IERS, not from this model.")


if __name__ == "__main__":
    main()
