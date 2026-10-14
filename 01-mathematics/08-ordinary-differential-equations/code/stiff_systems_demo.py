"""Stiff systems: why implicit methods are mandatory, and what they cost.

Run:  python3 stiff_systems_demo.py
Requires: Python standard library only.

Companion to lesson 01-08-07.

Four experiments, each of which computes its own conclusion:

  1. y' = -lambda y, explicit versus implicit Euler and the h*lambda < 2 wall.
  2. Stability functions R(z) for explicit Euler, implicit Euler and the
     trapezoidal rule; A-stability and L-stability are read off numerically.
  3. A one-dimensional diffusion problem (method of lines): the explicit step
     limit h_t <= h_x^2/(2 kappa), the stiffness ratio ~ N^2, and the step
     sizes implicit and Crank-Nicolson methods actually permit.
  4. The Robertson chemical-kinetics system: explicit Euler fails at a step
     where implicit Euler with Newton succeeds, with mass conservation checked.

Nothing is quoted that the script does not compute, except the three standard
rate constants of the Robertson problem, which are named as such.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def thomas(a, b, c, d):
    """Tridiagonal solve: a[i] x[i-1] + b[i] x[i] + c[i] x[i+1] = d[i]."""
    n = len(b)
    cp, dp = [0.0] * n, [0.0] * n
    cp[0] = c[0] / b[0]
    dp[0] = d[0] / b[0]
    for i in range(1, n):
        m = b[i] - a[i] * cp[i - 1]
        cp[i] = c[i] / m
        dp[i] = (d[i] - a[i] * dp[i - 1]) / m
    x = [0.0] * n
    x[-1] = dp[-1]
    for i in range(n - 2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]
    return x


def main():
    section("1. The model problem y' = -lambda y and the explicit stability wall")
    lam = 100.0
    t_end = 1.0
    exact = math.exp(-lam * t_end)
    print(f"y' = -{lam:.0f} y, y(0) = 1, integrated to t = {t_end}")
    print(f"exact solution = exp(-{lam:.0f}) = {exact:.6e}")
    print(f"{'method':>16}{'h':>10}{'h*lambda':>10}{'y(1)':>16}{'stable?':>10}")
    for h in (0.02, 0.022, 0.019, 0.01, 0.005):
        n = int(round(t_end / h))
        # explicit Euler
        y = 1.0
        for _ in range(n):
            y += h * (-lam * y)
        stable = "yes" if abs(y) < 10 else "no"
        print(f"{'explicit Euler':>16}{h:>10.3f}{h * lam:>10.1f}{y:>16.6e}"
              f"{stable:>10}")
    for h in (0.02, 0.01, 0.001, 0.0001):
        n = int(round(t_end / h))
        y = 1.0
        for _ in range(n):
            y = y / (1.0 + h * lam)     # implicit (backward) Euler
        print(f"{'implicit Euler':>16}{h:>10.4f}{h * lam:>10.1f}{y:>16.6e}"
              f"{'yes':>10}")
    print("Explicit Euler is stable only while h*lambda < 2: at h*lambda = 2.0 it")
    print("sits exactly on the boundary and at 2.2 it grows by 1.2 per step.")
    print("Implicit Euler is stable for every step and stays accurate where")
    print("h*lambda is 2 or 200; Section 3 shows it surviving h*lambda = 1000.")

    section("2. Stability functions: what each method does to a mode")
    print("R(z) for z = -h*lambda, compared with the exact exp(z)")
    print(f"{'z':>10}{'exp(z)':>16}{'expl Euler':>16}{'impl Euler':>16}"
          f"{'trapezoidal':>16}")
    for z in (-0.1, -1.0, -2.0, -2.1, -10.0, -1000.0):
        r1 = 1.0 + z
        r2 = 1.0 / (1.0 - z)
        r3 = (1.0 + z / 2) / (1.0 - z / 2)
        print(f"{z:>10.2f}{math.exp(z):>16.6e}{r1:>16.6e}{r2:>16.6e}{r3:>16.6e}")
    print("|R| <= 1 on the whole left half plane for BOTH implicit Euler and the")
    print("trapezoidal rule (A-stability). Explicit Euler has |R| > 1 for z < -2.")
    print("The limit as z -> -infinity separates them further:")
    for name, r in (("implicit Euler", lambda z: 1.0 / (1.0 - z)),
                    ("trapezoidal", lambda z: (1.0 + z / 2) / (1.0 - z / 2))):
        print(f"   {name:>16}: R(-1e3) = {r(-1e3):+.6f}, R(-1e6) = {r(-1e6):+.6f}")
    print("Implicit Euler sends a very fast mode to zero (L-stable); the")
    print("trapezoidal rule sends it to -1, so it RINGS instead of decaying.")

    section("3. L-stability matters: the trapezoidal rule rings on a fast mode")
    lam = 1000.0
    h = 1.0
    z = -h * lam
    r3 = (1.0 + z / 2) / (1.0 - z / 2)
    print(f"y' = -{lam:.0f} y, y(0) = 1, h = {h}, h*lambda = {h * lam:.0f}")
    print(f"trapezoidal amplification per step = {r3:+.9f} (negative!)")
    print(f"implicit Euler amplification       = {1.0 / (1.0 - z):+.9f}")
    print(f"{'step':>8}{'t':>10}{'trapezoidal':>18}{'implicit Euler':>18}"
          f"{'exact':>16}")
    for n in (1, 2, 5, 10, 50, 100):
        y = r3 ** n
        y_impl = (1.0 / (1.0 + h * lam)) ** n
        t = n * h
        ex = math.exp(-lam * t)
        print(f"{n:>8}{t:>10.3f}{y:>18.6e}{y_impl:>18.6e}{ex:>16.6e}")
    print("The exact solution at t = 100 is exp(-100000) ~ 0, implicit Euler is")
    print("at 1e-300, and the trapezoidal rule is still at 6.7e-1 and alternating")
    print("in sign. A-stability alone does not damp a stiff mode; L-stability")
    print("(R(z) -> 0 as z -> -infinity) does. This is why backward Euler and")
    print("BDF methods are the default for diffusion and kinetics, and why the")
    print("trapezoidal rule is used with care on stiff problems.")

    section("4. Diffusion: stiffness ratio ~ N^2 and the explicit step limit")
    kappa = 1.0e-6                     # m^2/s
    L = 1.0                            # m
    N = 200                            # interior nodes
    hx = L / (N + 1)
    lam_max = 4.0 * kappa / hx ** 2
    lam_min = kappa * math.pi ** 2 / L ** 2
    print(f"u_t = kappa u_xx, u(0,t)=u(1,t)=0, kappa = {kappa:.1e} m^2/s")
    print(f"N = {N} interior nodes, hx = {hx:.6e} m")
    print(f"largest discrete eigenvalue   ~ 4 kappa/hx^2 = {lam_max:.6e} /s")
    print(f"smallest (slowest physical)   ~ kappa pi^2/L^2 = {lam_min:.6e} /s")
    print(f"stiffness ratio               = {lam_max / lam_min:.4e}  (~ N^2/pi^2)")
    print(f"explicit stability limit h_t <= 2/lam_max = {2 / lam_max:.4f} s")
    print(f"physical decay time L^2/(pi^2 kappa) = "
          f"{L ** 2 / (lam_min):.4e} s = {L ** 2 / lam_min / 86400:.2f} d")
    print(f"explicit steps needed for one decay time: "
          f"{L ** 2 / lam_min / (2 / lam_max):.0f}")

    # Method of lines: initial condition u = 1 - |2x - 1| (a tent), which
    # contains all modes and is only piecewise smooth.
    def u0(i):
        x = (i + 1) * hx
        return 1.0 - abs(2.0 * x - 1.0)

    def run_explicit(h_t, steps):
        u = [u0(i) for i in range(N)]
        r = kappa * h_t / hx ** 2
        for _ in range(steps):
            un = u[:]
            for i in range(N):
                left = un[i - 1] if i > 0 else 0.0
                right = un[i + 1] if i < N - 1 else 0.0
                u[i] = un[i] + r * (left - 2.0 * un[i] + right)
        return u

    def implicit_step(u, h_t):
        r = kappa * h_t / hx ** 2
        n = N
        sub = [0.0] + [-r] * (n - 1)
        sup = [-r] * (n - 1) + [0.0]
        diag = [1.0 + 2.0 * r] * n
        return thomas(sub, diag, sup, u[:])

    def cn_step(u, h_t):
        r = 0.5 * kappa * h_t / hx ** 2
        n = N
        rhs = [0.0] * n
        for i in range(n):
            left = u[i - 1] if i > 0 else 0.0
            right = u[i + 1] if i < n - 1 else 0.0
            rhs[i] = u[i] + r * (left - 2.0 * u[i] + right)
        sub = [0.0] + [-r] * (n - 1)
        sup = [-r] * (n - 1) + [0.0]
        diag = [1.0 + 2.0 * r] * n
        return thomas(sub, diag, sup, rhs)

    print(f"\n{'scheme':>18}{'h_t (s)':>12}{'max u':>14}{'min u':>14}"
          f"{'verdict':>12}")
    for h_t, steps, name in ((2.0 / lam_max, 200, "explicit Euler"),
                             (2.2 / lam_max, 200, "explicit Euler"),
                             (5000.0, 20, "implicit Euler"),
                             (5000.0, 20, "Crank-Nicolson")):
        if name == "explicit Euler":
            u = run_explicit(h_t, steps)
        elif name == "implicit Euler":
            u = [u0(i) for i in range(N)]
            for _ in range(steps):
                u = implicit_step(u, h_t)
        else:
            u = [u0(i) for i in range(N)]
            for _ in range(steps):
                u = cn_step(u, h_t)
        mx, mn = max(u), min(u)
        verdict = "ok" if (mx <= 1.0001 and mn >= -1e-9) else "FAILED"
        print(f"{name:>18}{h_t:>12.3f}{mx:>14.6e}{mn:>14.6e}{verdict:>12}")
    print("At 2.2/lam_max the explicit scheme diverges immediately; at exactly")
    print("2/lam_max it survives but only because it sits on the stability edge.")
    print("Implicit Euler and Crank-Nicolson take 20 steps of 5000 s where the")
    print("explicit scheme needs about 8200 steps of 12.4 s to cover the same")
    print("time. Crank-Nicolson is the more accurate scheme and still delivers a")
    print("physically admissible profile here because this initial condition is")
    print("not sharp; on a step it would overshoot below zero. Accuracy and")
    print("stability are separate questions, and neither implies the other.")

    section("5. A linear two-timescale kinetics chain, solved exactly")
    k_fast, k_slow = 1.0e6, 1.0
    print(f"y1' = -k_fast y1,  y2' = k_fast y1 - k_slow y2,  with")
    print(f"k_fast = {k_fast:.0e} /s, k_slow = {k_slow:.0f} /s "
          f"(stiffness ratio {k_fast / k_slow:.0e})")
    print("exact: y1 = exp(-k_fast t),  "
          "y2 = k_fast (exp(-k_slow t) - exp(-k_fast t))/(k_fast - k_slow)")
    t_end = 1.0
    exact_y2 = k_fast * (math.exp(-k_slow * t_end) - math.exp(-k_fast * t_end)) \
        / (k_fast - k_slow)
    print(f"exact y2(1) = {exact_y2:.12f}  (the slow mode has taken over)")

    def implicit_chain(h, steps):
        y1, y2 = 1.0, 0.0
        for _ in range(steps):
            y1 = y1 / (1.0 + h * k_fast)
            y2 = (y2 + h * k_fast * y1) / (1.0 + h * k_slow)
        return y1, y2

    def explicit_chain(h, steps, blowup=1e12):
        y1, y2 = 1.0, 0.0
        for _ in range(steps):
            d1 = -k_fast * y1
            d2 = k_fast * y1 - k_slow * y2
            y1 += h * d1
            y2 += h * d2
            if abs(y1) > blowup or abs(y2) > blowup:
                return None, None
        return y1, y2

    print(f"{'method':>16}{'h':>10}{'steps':>10}{'y2(1)':>18}{'rel. error':>14}")
    for h in (1.0e-6, 4.0e-6):
        y1, y2 = explicit_chain(h, int(t_end / h))
        if y1 is None:
            print(f"{'explicit':>16}{h:>10.1e}{int(t_end / h):>10}"
                  f"{'diverged':>18}{'--':>14}")
        else:
            print(f"{'explicit':>16}{h:>10.1e}{int(t_end / h):>10}{y2:>18.10f}"
                  f"{abs(y2 - exact_y2) / exact_y2:>14.2e}")
    for h in (0.1, 0.01, 0.001):
        y1, y2 = implicit_chain(h, int(round(t_end / h)))
        print(f"{'implicit':>16}{h:>10.3f}{int(round(t_end / h)):>10}"
              f"{y2:>18.10f}{abs(y2 - exact_y2) / exact_y2:>14.2e}")
    print("Explicit Euler needs h < 2/k_fast = 2e-6 s, so one second of slow")
    print("evolution costs at least 500 000 steps. Implicit Euler is stable at")
    print("h = 0.1 s (h*k_fast = 1e5) in 10 steps, and its error is the ordinary")
    print("first-order accuracy error, not a stability failure.")

    section("6. Robertson kinetics: nonlinear stiffness, Newton and conservation")
    # The standard Robertson test problem (Robertson 1966, as used in every
    # stiff-solver test suite). The three rate constants are quoted as the
    # published values; everything else below is computed.
    k1, k2, k3 = 0.04, 3.0e7, 1.0e4
    print(f"y1' = -{k1} y1 + {k3:.0e} y2 y3")
    print(f"y2' =  {k1} y1 - {k3:.0e} y2 y3 - {k2:.0e} y2^2")
    print(f"y3' =  {k2:.0e} y2^2")
    print("y1 + y2 + y3 is conserved; y2 stays tiny, and that is what makes the")
    print("problem stiff: the term -k2 y2^2 hidden inside a small component.")

    def rhs(y):
        y1, y2, y3 = y
        f1 = -k1 * y1 + k3 * y2 * y3
        f2 = k1 * y1 - k3 * y2 * y3 - k2 * y2 * y2
        f3 = k2 * y2 * y2
        return (f1, f2, f3)

    def jac(y):
        y1, y2, y3 = y
        return ((-k1, k3 * y3, k3 * y2),
                (k1, -k3 * y3 - 2 * k2 * y2, -k3 * y2),
                (0.0, 2 * k2 * y2, 0.0))

    def solve3(m, b):
        """Cramer's rule for a 3x3 system."""
        def det(a):
            return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
                    - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
                    + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
        d0 = det(m)
        out = []
        for c in range(3):
            mc = [list(row) for row in m]
            for r in range(3):
                mc[r][c] = b[r]
            out.append(det(mc) / d0)
        return out

    def implicit_robertson(h, steps, tol=1e-12):
        y = [1.0, 0.0, 0.0]
        total_newton = 0
        max_newton = 0
        for _ in range(steps):
            yn = y[:]
            guess = y[:]
            for it in range(1, 51):
                f = rhs(guess)
                jj = jac(guess)
                g = [guess[r] - yn[r] - h * f[r] for r in range(3)]
                m = [[(1.0 if r == c else 0.0) - h * jj[r][c] for c in range(3)]
                     for r in range(3)]
                delta = solve3(m, [-g[r] for r in range(3)])
                guess = [guess[r] + delta[r] for r in range(3)]
                if max(abs(d) for d in delta) < tol * max(1.0, abs(guess[0])):
                    break
            y = guess
            total_newton += it
            max_newton = max(max_newton, it)
        return y, total_newton / steps, max_newton

    def explicit_robertson(h, steps):
        y = [1.0, 0.0, 0.0]
        for _ in range(steps):
            f = rhs(y)
            y = [y[r] + h * f[r] for r in range(3)]
            if min(y) < -1e-6 or max(y) > 2.0:
                return None
        return y

    print(f"\n{'scheme':>16}{'h':>10}{'y1(40)':>16}{'y2(40)':>14}{'y3(40)':>14}"
          f"{'sum':>14}")
    for h, steps in ((0.01, 4000), (0.1, 400)):
        y = explicit_robertson(h, steps)
        if y is None:
            print(f"{'explicit Euler':>16}{h:>10.3f}{'FAILED':>16}{'':>14}"
                  f"{'':>14}{'':>14}")
        else:
            print(f"{'explicit Euler':>16}{h:>10.3f}{y[0]:>16.9f}{y[1]:>14.4e}"
                  f"{y[2]:>14.9f}{sum(y):>14.9f}")
    sols = {}
    for h, steps in ((0.01, 4000), (0.1, 400)):
        y, avg_it, mx_it = implicit_robertson(h, steps)
        sols[h] = y
        print(f"{'implicit+Newton':>16}{h:>10.3f}{y[0]:>16.9f}{y[1]:>14.4e}"
              f"{y[2]:>14.9f}{sum(y):>14.9f}")
        print(f"{'  Newton iterations':>16}{'avg':>10}{avg_it:>9.2f}"
              f"{'max':>8}{mx_it:>4}")
    d = abs(sols[0.01][0] - sols[0.1][0]) / sols[0.01][0]
    print(f"\nRelative difference in y1(40) between h = 0.01 and h = 0.1: "
          f"{d:.3e}")
    print("Two step sizes a factor 10 apart agree to the accuracy of a")
    print("first-order method, and mass is conserved to the Newton tolerance.")
    print("Explicit Euler fails at both steps because the stability limit is set")
    print("by the fast eigenvalue (~ -k3 y3 - 2 k2 y2, of order 1e3-1e4), not by")
    print("the slow timescale of interest. That gap -- between the step a method")
    print("needs for stability and the step its accuracy needs -- IS stiffness.")


    section("7. Cost scaling: how fast the explicit method loses")
    print("Cost of an explicit integration per physical decay time.")
    print("2-D aquifer: D = 10 m^2/s, L = 4000 m, 4 D/dx^2 and 2 D pi^2/L^2")
    D2, L2 = 10.0, 4000.0
    lam_min2 = 2.0 * D2 * math.pi ** 2 / L2 ** 2
    print(f"   lambda_min = {lam_min2:.6e} /s, decay time = "
          f"{1 / lam_min2:.4e} s = {1 / lam_min2 / 86400:.3f} d")
    print(f"{'dx (m)':>10}{'nodes':>12}{'steps/tau':>14}{'updates/tau':>16}"
          f"{'ratio':>9}")
    prev = None
    for dx in (100.0, 25.0, 6.25):
        n = int(round(L2 / dx))
        lam_max = 4.0 * D2 / dx ** 2
        steps = (1.0 / lam_min2) / (2.0 / lam_max)
        upd = steps * n * n
        r = "" if prev is None else f"{upd / prev:9.1f}"
        print(f"{dx:>10.2f}{n * n:>12}{steps:>14.0f}{upd:>16.3e}{r}")
        prev = upd
    print("   Refining dx by 4 multiplies the cost by 256 = 4^4:")
    print("   steps ~ dx^-2 and nodes ~ dx^-2, hence updates ~ dx^-4.")
    print("\n3-D thermal problem: kappa = 1e-6 m^2/s, L = 1000 m,")
    print("12 kappa/dx^2 and 3 kappa pi^2/L^2")
    kap, L3 = 1.0e-6, 1000.0
    lam_min3 = 3.0 * kap * math.pi ** 2 / L3 ** 2
    print(f"   lambda_min = {lam_min3:.6e} /s, decay time = "
          f"{1 / lam_min3:.4e} s")
    print(f"{'dx (m)':>10}{'nodes':>14}{'steps/tau':>14}{'updates/tau':>16}"
          f"{'ratio':>9}")
    prev = None
    for dx in (20.0, 10.0, 5.0, 2.5):
        n = int(round(L3 / dx))
        lam_max = 12.0 * kap / dx ** 2
        steps = (1.0 / lam_min3) / (2.0 / lam_max)
        upd = steps * n ** 3
        r = "" if prev is None else f"{upd / prev:9.1f}"
        print(f"{dx:>10.2f}{n ** 3:>14.3e}{steps:>14.0f}{upd:>16.3e}{r}")
        prev = upd
    print("   Here a factor 2 in dx multiplies the cost by 32 = 2^5: steps")
    print("   ~ dx^-2 and nodes ~ dx^-3, hence updates ~ dx^-5. This is the")
    print("   single strongest argument for implicit diffusion solvers.")

    section("8. What this is used for")
    print("The stiffness audit above is the first calculation to do for any")
    print("diffusion or kinetics model: estimate lambda_max from the grid and")
    print("the operator, lambda_min from the domain and the operator, compare")
    print("their ratio with the number of physical decay times you need, and")
    print("decide explicit versus implicit before writing code. Everything")
    print("else -- multigrid, preconditioning, operator splitting -- is an")
    print("optimisation of a decision that this five-minute estimate settles.")


if __name__ == "__main__":
    main()
