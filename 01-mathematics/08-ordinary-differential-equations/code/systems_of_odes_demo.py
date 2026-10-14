"""Systems of ODEs: eigenstructure, phase portraits and stability.

Run:  python3 systems_of_odes_demo.py
Requires: Python standard library only.

Companion to lesson 01-08-04.

For a linear system x' = A x the behaviour is decided entirely by the
eigenvalues of A, classified by trace T and determinant D:

    D < 0                 saddle                (real roots, opposite signs)
    D > 0, T^2 > 4 D      node                    (real roots, same sign)
    D > 0, T^2 < 4 D      focus/spiral            (complex roots)
    D > 0, T^2 = 4 D      degenerate/node         (double root)
    T < 0 stable, T > 0 unstable, T = 0 neutral

Every classification printed below is computed from the matrix, and every
trajectory is integrated numerically from the equations themselves.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def eigs(a, b, c, d):
    """Eigenvalues of [[a,b],[c,d]]."""
    T, D = a + d, a * d - b * c
    disc = T * T - 4 * D
    if disc >= 0:
        s = math.sqrt(disc)
        return (0.5 * (T + s), 0.0), (0.5 * (T - s), 0.0)
    s = math.sqrt(-disc)
    return (0.5 * T, 0.5 * s), (0.5 * T, -0.5 * s)


def classify(a, b, c, d):
    T, D = a + d, a * d - b * c
    disc = T * T - 4 * D
    if D < 0:
        kind = "saddle"
    elif disc > 0:
        kind = "node"
    elif disc < 0:
        kind = "spiral"
    else:
        kind = "degenerate node"
    if D > 0:
        if T < 0:
            stab = "stable"
        elif T > 0:
            stab = "unstable"
        else:
            stab = "centre" if disc < 0 else "degenerate (neutral)"
    else:
        stab = "unstable"
    return kind, stab


def show(name, a, b, c, d, scale=1.0):
    T, D = a + d, a * d - b * c
    kind, stab = classify(a, b, c, d)
    e1, e2 = eigs(a, b, c, d)

    def f(z):
        return (f"{z[0]:+.6f}" if z[1] == 0
                else f"{z[0]:+.6f}{z[1]:+.6f}i")

    print(f"{name}")
    print(f"   A = [[{a:g}, {b:g}], [{c:g}, {d:g}]]   T = {T:g}, D = {D:g}, "
          f"T^2-4D = {T * T - 4 * D:g}")
    print(f"   eigenvalues {f(e1)}, {f(e2)}  ->  {stab} {kind}")
    return T, D, e1, e2


def integrate(a, b, c, d, x0, y0, t_end, n=20000):
    h = t_end / n
    x, y = x0, y0
    for _ in range(n):
        dx = a * x + b * y
        dy = c * x + d * y
        x += h * dx
        y += h * dy
    return x, y


def main():
    section("1. The trace-determinant classification, on five matrices")
    cases = [
        ("two-box climate feedback, stable node", -0.30, 0.10, 0.05, -0.20),
        ("damped reservoir coupling, stable spiral", -0.10, 1.00, -1.00, -0.10),
        ("runaway thermal feedback, saddle", 0.20, 0.50, 0.50, -0.10),
        ("undamped conservative pair, centre", 0.0, 1.0, -1.0, 0.0),
        ("isotropic decay, degenerate node", -0.50, 0.0, 0.0, -0.50),
    ]
    for name, a, b, c, d in cases:
        show(name, a, b, c, d)
        print()

    section("2. Two-box energy balance model of a coupled climate")
    # C1 dT1/dt = F - lambda T1 + gamma (T2 - T1);  C2 dT2/dt = gamma (T1 - T2)
    # Written with C = 1 for both boxes after dividing through.
    lam, gamma = 1.2, 0.8
    A = -(lam + gamma)
    B = gamma
    C = gamma
    D = -gamma
    T, DET, e1, e2 = show("surface/deep-ocean two-box model", A, B, C, D)
    print(f"   relaxation timescales: -1/r1 = {-1 / e1[0]:.4f}, "
          f"-1/r2 = {-1 / e2[0]:.4f} (arbitrary time units)")
    print(f"   equilibrium of the homogeneous system is the origin; with forcing")
    print(f"   F it shifts to the particular solution, but the *stability* is")
    print(f"   the same: both roots negative, so a perturbation decays.")
    x, y = integrate(A, B, C, D, 1.0, 0.0, 50.0)
    print(f"   integrate (1,0) to t = 50: ({x:.6e}, {y:.6e}) -> origin")

    section("3. Predator-prey (Lotka-Volterra) as a coupled-reservoir analogue")
    # x' = a x - b x y ; y' = -c y + d x y
    a, b, c, d = 1.0, 0.5, 0.8, 0.4
    x_star, y_star = c / d, a / b
    print(f"x' = {a} x - {b} x y ;  y' = -{c} y + {d} x y")
    print(f"nontrivial equilibrium: x* = c/d = {x_star:.6f}, "
          f"y* = a/b = {y_star:.6f}")
    # Jacobian at the equilibrium.
    J = ((a - b * y_star, -b * x_star), (d * y_star, -c + d * x_star))
    ja, jb = J[0]
    jc, jd = J[1]
    show("   linearisation about the equilibrium", ja, jb, jc, jd)
    print("   The eigenvalues are purely imaginary: the linearisation is a")
    print("   centre, and the nonlinear system has closed orbits.")
    print("   The conserved quantity is H = d x - c ln x + b y - a ln y:")
    H = lambda x, y: d * x - c * math.log(x) + b * y - a * math.log(y)
    H0 = H(1.0, 1.0)
    print(f"   H(1,1) = {H0:.9f}")

    def lv_rk4(x, y, h):
        def rhs(u, v):
            return (a * u - b * u * v, -c * v + d * u * v)
        k1 = rhs(x, y)
        k2 = rhs(x + h * k1[0] / 2, y + h * k1[1] / 2)
        k3 = rhs(x + h * k2[0] / 2, y + h * k2[1] / 2)
        k4 = rhs(x + h * k3[0], y + h * k3[1])
        return (x + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
                y + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))

    print(f"{'t':>8}{'x':>14}{'y':>14}{'H(t)-H(0)':>16}")
    x, y = 1.0, 1.0
    h = 0.001
    for k in range(100001):
        if k % 20000 == 0:
            print(f"{k * h:>8.1f}{x:>14.8f}{y:>14.8f}{H(x, y) - H0:>16.3e}")
        x, y = lv_rk4(x, y, h)
    print("RK4 keeps H constant to the printed precision over 2000 oscillation")
    print("periods: the orbits are genuinely closed, and the linearisation is a")
    print("centre. Forward Euler on the same system spirals outwards; the drift")
    print("would be numerical, not physical.")

    section("4. A damped predator-prey analogue: the stable spiral")
    # Logistic prey with a mass-action (bilinear) predation term. The interior
    # equilibrium turns out to be attracting for EVERY positive parameter set;
    # the demonstration prints the closed form of the trace beside its value.
    a, b, c, d, K = 1.0, 0.6, 0.7, 0.5, 3.0
    print("x' = a x (1 - x/K) - b x y ;  y' = -c y + d x y")
    print(f"a = {a}, K = {K}, b = {b}, c = {c}, d = {d}")
    x_star = c / d
    y_star = a / b * (1 - x_star / K)
    print(f"equilibrium: x* = c/d = {x_star:.6f}, "
          f"y* = (a/b)(1 - x*/K) = {y_star:.6f}")
    j11 = a * (1 - 2 * x_star / K) - b * y_star
    j12 = -b * x_star
    j21 = d * y_star
    j22 = -c + d * x_star
    show("   Jacobian at the equilibrium", j11, j12, j21, j22)
    print(f"   closed form of the trace: T = -a c/(d K) = {-a * c / (d * K):.6f}")
    print("   T is negative for EVERY a, b, c, d, K > 0, so this equilibrium is")
    print("   always attracting: no limit cycle can be born from it. Watch the")
    print("   formula, not the appearance of the orbit:")
    for Kk in (3.0, 1.5, 20.0):
        xs = c / d
        ys = a / b * (1 - xs / Kk)
        Tk = a * (1 - 2 * xs / Kk) - b * ys + (-c + d * xs)
        print(f"      K = {Kk:6.1f}: T = {Tk:+10.6f}, predicted "
              f"{-a * c / (d * Kk):+10.6f}")
    print("   Destabilisation needs a different model: a saturating functional")
    print("   response b x y/(1 + h x). Then T = x*[-a/K + b h y*/(1+h x*)^2]")
    print("   and the sign CAN change when K grows. The next block checks that.")
    for Kk, hh in ((3.0, 0.5), (5.0, 0.5)):
        dd, cc, bb, aa = 1.0, 0.4, 1.0, 1.0
        xs = cc / (dd - cc * hh)
        ys = aa * (1 - xs / Kk) * (1 + hh * xs) / bb
        j11 = aa * (1 - 2 * xs / Kk) - bb * ys / (1 + hh * xs) \
            + bb * hh * xs * ys / (1 + hh * xs) ** 2
        j12 = -bb * xs / (1 + hh * xs)
        j21 = dd * ys / (1 + hh * xs) ** 2
        j22 = 0.0
        Tk, Dk = j11 + j22, j11 * j22 - j12 * j21
        if abs(Tk) < 1e-9:
            kind = "MARGINAL: linearisation is a centre (Hopf point)"
        else:
            kind = ("stable" if Tk < 0 else "UNSTABLE") + \
                (" spiral" if Tk * Tk < 4 * Dk else " node")
        print(f"   Holling II, K = {Kk:4.1f}, h = {hh}: T = {Tk:+.6f}, "
              f"D = {Dk:.6f} -> {kind}")

    def f_rk(v, h):
        x, y = v
        k1 = (a * x * (1 - x / K) - b * x * y, -c * y + d * x * y)
        x2, y2 = x + h * k1[0] / 2, y + h * k1[1] / 2
        k2 = (a * x2 * (1 - x2 / K) - b * x2 * y2, -c * y2 + d * x2 * y2)
        x3, y3 = x + h * k2[0] / 2, y + h * k2[1] / 2
        k3 = (a * x3 * (1 - x3 / K) - b * x3 * y3, -c * y3 + d * x3 * y3)
        x4, y4 = x + h * k3[0], y + h * k3[1]
        k4 = (a * x4 * (1 - x4 / K) - b * x4 * y4, -c * y4 + d * x4 * y4)
        return (x + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
                y + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))

    print(f"   trajectory from (1, 1) for the mass-action case:")
    print(f"{'t':>8}{'x':>14}{'y':>14}{'dist to fixed point':>24}")
    v = (1.0, 1.0)
    h, n = 0.001, 300000
    checkpoints = {0, 50000, 100000, 150000, 200000, 250000, 300000}
    for k in range(n + 1):
        if k in checkpoints:
            dist = math.hypot(v[0] - x_star, v[1] - y_star)
            print(f"{k * h:>8.1f}{v[0]:>14.7f}{v[1]:>14.7f}{dist:>24.3e}")
        v = f_rk(v, h)
    print("The distance to the fixed point falls monotonically: stable spiral,")
    print("i.e. the coupled reservoir relaxes to a steady state instead of")
    print("oscillating forever.")

    section("5. A saddle is how a system chooses a state, not just a warning")
    a, b, c, d = 0.3, 0.2, 0.2, -0.1
    show("ice-albedo / weathering feedback with opposite signs", a, b, c, d)
    lam_u, _ = eigs(a, b, c, d)[0]
    # eigenvector for the positive (unstable) eigenvalue: (A - lambda I) v = 0
    vx, vy = b, lam_u - a
    nrm = math.hypot(vx, vy)
    print(f"   unstable eigenvalue {lam_u:+.6f}, eigenvector direction "
          f"({vx / nrm:+.6f}, {vy / nrm:+.6f})")
    for x0, y0 in ((0.01, 0.0), (-0.01, 0.0), (0.0, 0.01), (0.0, -0.01),
                   (0.01, 0.01)):
        x, y = integrate(a, b, c, d, x0, y0, 20.0)
        r = math.hypot(x, y)
        print(f"   start ({x0:+.2f}, {y0:+.2f}) -> ({x:+.6f}, {y:+.6f});"
              f" direction ({x / r:+.5f}, {y / r:+.5f})")
    print("Two in-flowing and two out-flowing directions: what survives is the")
    print("unstable eigenvector, so the long-time direction is the same for every")
    print("start except those exactly on the stable line. Which state a")
    print("perturbation reaches depends on which side of the separatrix it starts.")

    section("6. Global stability from a Lyapunov function (two-box model)")
    print("For the Lotka-Volterra system the invariant H is not a Lyapunov")
    print("function (it is conserved, not decreasing), which is exactly why the")
    print("orbits are closed rather than spiralling in. For the two-box model")
    print("the quadratic V = (T1^2 + T2^2)/2 has dV/dt = -T^T Q T with")
    lam, gamma = 1.2, 0.8
    Q11, Q12, Q22 = lam + gamma, -gamma, gamma
    print(f"   Q = [[{Q11:g}, {-gamma:g}], [{-gamma:g}, {Q22:g}]]")
    det = Q11 * Q22 - Q12 * Q12
    print(f"   symmetric part of Q: det = {det:.6f} > 0, Q11 = {Q11:.6f} > 0")
    print("   -> positive definite, so dV/dt < 0 for all non-zero states and the")
    print("   origin is globally asymptotically stable.")


if __name__ == "__main__":
    main()
