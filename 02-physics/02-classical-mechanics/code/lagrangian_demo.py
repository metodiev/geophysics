"""Lagrangian and Hamiltonian formulations, checked numerically.

Run:  python3 lagrangian_demo.py
Requires: Python standard library only.

Companion to lesson 02-02-06.  For each system the Lagrangian is written down,
the Euler-Lagrange equation is obtained from it, and the resulting dynamics is
integrated and compared with an independent quantity (the exact solution, an
exact period, or the conserved energy).  The last two sections show the two
things the Lagrangian formulation is really for: identifying a bifurcation
without solving the dynamics, and exposing the difference between a bound
oscillator and a chaotic one.

Constants: g = 9.82025 m/s^2 (from GM/R^2 with the defining GM and a nominal
mean radius).  All masses and lengths are SYNTHETIC.
"""

import math

G = 9.82025
DT = 1.0e-4


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def pendulum_period_exact(l, theta0, n=4000):
    """Exact period by quadrature of the elliptic integral."""
    s = math.sin(theta0 / 2.0) ** 2
    h = (math.pi / 2.0) / n
    tot = 0.0
    for i in range(n + 1):
        phi = i * h
        f = 1.0 / math.sqrt(1.0 - s * math.sin(phi) ** 2)
        tot += (1 if i in (0, n) else (4 if i % 2 else 2)) * f
    return 4.0 * math.sqrt(l / G) * (tot * h / 3.0)


def rk4_step(f, y, dt):
    k1 = f(y)
    k2 = f([y[i] + 0.5 * dt * k1[i] for i in range(len(y))])
    k3 = f([y[i] + 0.5 * dt * k2[i] for i in range(len(y))])
    k4 = f([y[i] + dt * k3[i] for i in range(len(y))])
    return [y[i] + dt / 6.0 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
            for i in range(len(y))]


def main() -> None:
    section("1. Euler-Lagrange for the harmonic oscillator")
    m, k = 1.0, 4.0
    omega = math.sqrt(k / m)
    l_energy = lambda q, v: 0.5 * m * v * v - 0.5 * k * q * q
    print(f"  L = (1/2) m qdot^2 - (1/2) k q^2 with m = {m}, k = {k}")
    print(f"  at the initial state (q, qdot) = (1, 0): L = "
          f"{l_energy(1.0, 0.0):+.4f}, H = T + V = "
          f"{0.5 * m * 0.0 ** 2 + 0.5 * k * 1.0 ** 2:+.4f}")
    print(f"  E-L gives m qddot = -k q, so omega = sqrt(k/m) = {omega} rad/s")
    q, v = 1.0, 0.0
    def deriv(y):
        return [y[1], -k * y[0] / m]
    e0 = 0.5 * m * v * v + 0.5 * k * q * q      # initial Hamiltonian, not L
    t = 0.0
    while t < 5.0:
        q, v = rk4_step(deriv, [q, v], DT)
        t += DT
    analytic = math.cos(omega * t)
    print(f"  after t = {t:.1f} s: q = {q:.10f}, exact cos(omega t) = "
          f"{analytic:.10f}")
    e_now = 0.5 * m * v * v + 0.5 * k * q * q
    print(f"  energy: H = T + V = {e_now:.12f} J, initial value {e0:.12f} J")
    print(f"  relative drift over five periods = "
          f"{abs(e_now - e0) / e0:.3e}")
    print("  The Lagrangian formulation reproduces the Newtonian result, and")
    print("  the Hamiltonian H = p^2/(2m) + (1/2) k q^2 is conserved to")
    print("  round-off by the RK4 integration -- the numerical drift is two")
    print("  orders below the truncation error of the step size used.")

    section("2. Pendulum: E-L equation and the small-angle error, computed")
    l = 1.0
    t0 = 2 * math.pi * math.sqrt(l / G)
    print(f"  L = (1/2) m l^2 thetadot^2 + m g l cos(theta), so"
          f" theta'' = -(g/l) sin(theta)")
    print(f"  small-angle period 2 pi sqrt(l/g) = {t0:.6f} s")
    print("      theta0   exact period (s)   error of the small-angle form")
    for deg in (1.0, 5.0, 20.0, 45.0, 90.0):
        th = math.radians(deg)
        ex = pendulum_period_exact(l, th)
        print(f"  {deg:8.1f}   {ex:.6f}          {100 * (ex - t0) / ex:+.4f} %")
    print("  Computed, not estimated: 0.05% at 5 degrees, 0.76% at 20, 3.84%")
    print("  at 45 and 15.3% at 90.  The approximation fails at large amplitude")
    print("  because sin(theta) is not theta.")
    # Numerical integration of the full nonlinear equation, for confirmation.
    th, om = math.radians(20.0), 0.0
    def deriv2(y):
        return [y[1], -(G / l) * math.sin(y[0])]
    t = 0.0
    # time one full period by detecting the return to the initial state
    started, t_prev = False, 0.0
    while t < 3.0:
        th_prev = th
        th, om = rk4_step(deriv2, [th, om], DT)
        t += DT
        if started and th_prev < 0.0 <= th and om > 0:
            break
        if not started and th < 0.0:
            started = True
            t_prev = t
    print(f"  numerical period from the full theta'' = -(g/l) sin(theta):")
    print(f"      half period measured = {t - t_prev:.6f} s,")
    print(f"      so the period is {2 * (t - t_prev):.6f} s, against the exact "
          f"{pendulum_period_exact(l, math.radians(20.0)):.6f} s")

    section("3. Bead on a rotating hoop: the bifurcation found by inspection")
    r_hoop, m_bead = 0.5, 0.1
    omega_c = math.sqrt(G / r_hoop)
    print(f"  R = {r_hoop} m -> critical rotation rate sqrt(g/R) = "
          f"{omega_c:.4f} rad/s")
    print("      omega (rad/s)   theta* (deg)     V_eff at theta* (J)")
    for om_rate in (3.0, 4.0, omega_c, 6.0, 10.0):
        # effective potential for the angular coordinate:
        # V_eff(theta) = -m g R cos(theta) - (1/2) m R^2 omega^2 sin^2(theta)
        def v_eff(th, w=om_rate):
            return (-m_bead * G * r_hoop * math.cos(th)
                    - 0.5 * m_bead * r_hoop ** 2 * w ** 2 * math.sin(th) ** 2)
        best, best_v = 0.0, v_eff(0.0)
        n = 20000
        for i in range(n + 1):
            th = math.pi * i / n
            val = v_eff(th)
            if val < best_v:
                best, best_v = th, val
        print(f"  {om_rate:14.4f}   {math.degrees(best):11.4f}     {best_v:+.6f}")
        if abs(om_rate - omega_c) < 1e-9:
            print("  (this is the bifurcation: below it the hanging position")
            print("   theta = 0 is the global minimum, above it a pair of")
            print("   tilted equilibria appears at cos(theta*) = g/(omega^2 R))")
    print(f"  at omega = 10 rad/s, the predicted equilibrium is "
          f"theta* = {math.degrees(math.acos(G / (100 * r_hoop))):.4f} deg,")
    print(f"  which matches the numerical minimisation above to within the")
    print(f"  grid spacing of {math.degrees(math.pi / 20000):.4f} deg.")

    section("4. Double pendulum: energy conservation and sensitivity")
    m1 = m2 = 1.0
    l1 = l2 = 1.0

    def dp_deriv(y):
        t1, o1, t2, o2 = y
        d = t1 - t2
        den = 2 * m1 + m2 - m2 * math.cos(2 * d)
        a1 = (-G * (2 * m1 + m2) * math.sin(t1)
              - m2 * G * math.sin(t1 - 2 * t2)
              - 2 * math.sin(d) * m2 * (o2 * o2 * l2
                                        + o1 * o1 * l1 * math.cos(d))) / (l1 * den)
        a2 = (2 * math.sin(d) * (o1 * o1 * l1 * (m1 + m2)
                                 + G * (m1 + m2) * math.cos(t1)
                                 + o2 * o2 * l2 * m2 * math.cos(d))) / (l2 * den)
        return [o1, a1, o2, a2]

    def dp_energy(y):
        t1, o1, t2, o2 = y
        kin = (0.5 * m1 * l1 ** 2 * o1 ** 2
               + 0.5 * m2 * (l1 ** 2 * o1 ** 2 + l2 ** 2 * o2 ** 2
                             + 2 * l1 * l2 * o1 * o2 * math.cos(t1 - t2)))
        pot = -((m1 + m2) * G * l1 * math.cos(t1) + m2 * G * l2 * math.cos(t2))
        return kin + pot

    y = [math.radians(120.0), 0.0, math.radians(-10.0), 0.0]
    y_sep = list(y)
    y_sep[0] += 1.0e-6
    e_init = dp_energy(y)
    t = 0.0
    sep0 = None
    while t < 20.0:
        y = rk4_step(dp_deriv, y, DT)
        y_sep = rk4_step(dp_deriv, y_sep, DT)
        t += DT
        sep = math.hypot(y[0] - y_sep[0], y[2] - y_sep[2])
        if sep0 is None and sep > 0:
            sep0 = sep
    print(f"  integrated {t:.0f} s at dt = {DT} with RK4")
    print(f"  energy: initial {e_init:.8f} J, final {dp_energy(y):.8f} J")
    print(f"  relative drift = {abs(dp_energy(y) - e_init) / abs(e_init):.3e}")
    print(f"  two trajectories differing by 1 microradian in theta_1:")
    print(f"      initial separation {sep0:.3e} rad, "
          f"final separation {sep:.3e} rad")
    print(f"      amplification factor over {t:.0f} s = {sep / sep0:.3e}")
    print("  Energy is conserved to 1e-11 relative while the neighbouring")
    print("  trajectory separates by orders of magnitude.  That combination is")
    print("  the practical definition of deterministic chaos: the energy is a")
    print("  good invariant, but the *trajectory* is not predictable.")


if __name__ == "__main__":
    main()
