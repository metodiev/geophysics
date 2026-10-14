"""Kinematics in one and two dimensions, checked against exact solutions.

Run:  python3 kinematics_demo.py
Requires: Python standard library only.

Companion to lesson 02-02-01.  Three questions are answered numerically:

1.  How accurately does a time-stepping integrator reproduce the exact parabolic
    trajectory, and how does the error fall with the step size?
2.  What does air resistance do to a launch?  (Linear drag has an exact
    solution; quadratic drag does not, so it is integrated.)
3.  Does a dropped body really hit the ground at the same time as a horizontally
    thrown one, and what does drag do to that statement?

Values used: GM = 3.986 004 418e14 m^3 s^-2 (defining, WGS 84) and
R = 6 371 km (nominal mean radius), so g = GM/R^2 is the surface value used
throughout.  All projectiles are SYNTHETIC.
"""

import math

GM = 3.986004418e14
R = 6371000.0
G_LOCAL = GM / R ** 2          # 9.8203 m/s^2 at the nominal mean radius


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def euler(vx0, vy0, dt, t_end, drag=None):
    """Explicit Euler over a whole number of steps that lands exactly on t_end.

    Landing exactly on t_end matters: if the loop simply stops when ``t >= t_end``
    it overshoots by up to one step, and that overshoot (not the integrator)
    dominates the comparison between schemes.
    """
    n = max(1, round(t_end / dt))
    h = t_end / n
    x, y, vx, vy = 0.0, 0.0, vx0, vy0
    for _ in range(n):
        ax, ay = 0.0, -G_LOCAL
        if drag is not None:
            dx, dy = drag((vx, vy))
            ax += dx
            ay += dy
        x += h * vx
        y += h * vy
        vx += h * ax
        vy += h * ay
    return x, y, vx, vy


def rk4(vx0, vy0, dt, t_end, drag=None):
    """Classical fourth-order Runge-Kutta on the same state, same landing."""
    n = max(1, round(t_end / dt))
    h = t_end / n
    state = [0.0, 0.0, vx0, vy0]                    # x, y, vx, vy

    def deriv(s):
        ax, ay = 0.0, -G_LOCAL
        if drag is not None:
            dx, dy = drag((s[2], s[3]))
            ax += dx
            ay += dy
        return [s[2], s[3], ax, ay]

    for _ in range(n):
        k1 = deriv(state)
        k2 = deriv([state[i] + 0.5 * h * k1[i] for i in range(4)])
        k3 = deriv([state[i] + 0.5 * h * k2[i] for i in range(4)])
        k4 = deriv([state[i] + h * k3[i] for i in range(4)])
        state = [state[i] + h / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
                 for i in range(4)]
    return tuple(state)


def range_until_landing(v0, angle, dt, method="rk4"):
    """Horizontal range of a vacuum projectile, integrating until y crosses 0.

    The landing time is found by the integrator, not imposed analytically, so
    the discretisation error shows up in the range instead of cancelling.
    """
    y, x = 0.0, 0.0
    vx, vy = v0 * math.cos(angle), v0 * math.sin(angle)
    def deriv(s):
        return [s[2], s[3], 0.0, -G_LOCAL]
    state = [x, y, vx, vy]
    prev = list(state)
    while state[1] >= 0.0:
        prev = list(state)
        if method == "euler":
            k1 = deriv(state)
            state = [state[i] + dt * k1[i] for i in range(4)]
        else:
            k1 = deriv(state)
            k2 = deriv([state[i] + 0.5 * dt * k1[i] for i in range(4)])
            k3 = deriv([state[i] + 0.5 * dt * k2[i] for i in range(4)])
            k4 = deriv([state[i] + dt * k3[i] for i in range(4)])
            state = [state[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i]
                                          + k4[i]) for i in range(4)]
    # linear interpolation of the crossing between prev and state
    f = prev[1] / (prev[1] - state[1])
    return prev[0] + f * (state[0] - prev[0])


def main() -> None:
    section("1. Free fall and a horizontal projection: the same fall time")
    h = 100.0
    t_fall = math.sqrt(2 * h / G_LOCAL)
    v_impact = G_LOCAL * t_fall
    print(f"  g at R = 6371 km              : {G_LOCAL:.6f} m/s^2")
    print(f"  fall from {h:.0f} m             : t = {t_fall:.6f} s, "
          f"impact speed = {v_impact:.4f} m/s")
    for label, v0 in (("dropped      ", 0.0), ("thrown at 5 m/s", 5.0),
                      ("thrown at 20 m/s", 20.0)):
        # integrate to the ground crossing using the exact analytic time
        x, y, _, vy = rk4(v0, 0.0, 1.0e-4, t_fall)
        print(f"  {label}: y = {y:+.6f} m, horizontal distance = {x:8.4f} m, "
              f"vy = {vy:.4f} m/s")
    print(f"  analytic horizontal distance for 20 m/s = "
          f"{20.0 * t_fall:.4f} m")

    section("2. Vacuum projectile: range, apex, and integrator order")
    v0, angle = 20.0, math.radians(35.0)
    vx0, vy0 = v0 * math.cos(angle), v0 * math.sin(angle)
    t_apex = vy0 / G_LOCAL
    rng = 2 * vx0 * vy0 / G_LOCAL
    print(f"  v0 = {v0:.1f} m/s at {math.degrees(angle):.1f} deg")
    print(f"  range (exact)  = {rng:.6f} m, apex time = {t_apex:.6f} s, "
          f"apex height = {vy0 ** 2 / (2 * G_LOCAL):.6f} m")
    print("  range integrated until the trajectory lands, relative error:")
    print("      dt      Euler     ratio       RK4       ratio")
    pe = pr = None
    for dt in (0.1, 0.01, 0.001):
        e = abs(range_until_landing(v0, angle, dt, "euler") - rng) / rng
        r = abs(range_until_landing(v0, angle, dt, "rk4") - rng) / rng
        re_ = f"{pe / e:8.2f}" if pe else "     ---"
        rr_ = f"{pr / r:8.2f}" if pr else "     ---"
        print(f"  {dt:6.3f}  {e:.3e} {re_}  {r:.3e} {rr_}")
        pe, pr = e, r
    print("  Euler falls by ~10 per decade -> first order, as expected.")
    print("  RK4 falls by ~100, i.e. second order, NOT fourth: the limiting")
    print("  error is the linear interpolation of the landing time, not the")
    print("  integrator.  Measure the integrator separately, at a fixed time:")
    t_fix = 1.0
    y_exact = vy0 * t_fix - 0.5 * G_LOCAL * t_fix ** 2
    print(f"      dt      Euler error   ratio     RK4 error      ratio"
          f"   (height at t = {t_fix} s, exact {y_exact:.9f} m)")
    pe = pr = None
    for dt in (0.1, 0.01, 0.001, 0.0001):
        ye = euler(vx0, vy0, dt, t_fix)[1]
        yr = rk4(vx0, vy0, dt, t_fix)[1]
        ee, er = abs(ye - y_exact), abs(yr - y_exact)
        re_ = f"{pe / ee:8.2f}" if pe else "     ---"
        rr_ = f"{pr / er:7.2f}" if pr else "    ---"
        print(f"  {dt:7.4f}  {ee:.3e} {re_}  {er:.3e} {rr_}")
        pe, pr = ee, er
    print("  Euler is cleanly first order.  RK4 sits at round-off (~1e-14) and")
    print("  gets *worse* as dt shrinks, because it is exact for polynomials of")
    print("  degree <= 4 and the whole trajectory here is quadratic: what is")
    print("  left is floating-point noise, which grows with the step count.")
    print("  To see RK4's fourth order, use a problem with no polynomial")
    print("  solution -- quadratic drag, compared against a fine reference:")
    def qdrag(v):
        c = 0.01
        sp = math.hypot(*v)
        return (-c * sp * v[0], -c * sp * v[1])
    t_end = 3.0
    ref = rk4(20.0 * math.cos(angle), 20.0 * math.sin(angle), 1.0e-5, t_end,
              drag=qdrag)
    print("      dt      Euler error   ratio     RK4 error      ratio")
    pe = pr = None
    for dt in (0.1, 0.01, 0.001):
        ye = euler(vx0, vy0, dt, t_end, drag=qdrag)
        yr = rk4(vx0, vy0, dt, t_end, drag=qdrag)
        ee = math.hypot(ye[2] - ref[2], ye[3] - ref[3])
        er = math.hypot(yr[2] - ref[2], yr[3] - ref[3])
        re_ = f"{pe / ee:8.2f}" if pe else "     ---"
        rr_ = f"{pr / er:7.2f}" if pr else "    ---"
        print(f"  {dt:7.4f}  {ee:.3e} {re_}  {er:.3e} {rr_}")
        pe, pr = ee, er
    print("  (Reference = RK4 at dt = 1e-5.)  Now the orders appear: ~10 per")
    print("  decade for Euler (first order) and ~10^4 for RK4 (fourth order),")
    print("  until the RK4 residual itself reaches its round-off floor near")
    print("  1e-12 for velocities of order 10 m/s and flattens.  A measured")
    print("  convergence order is a property of the whole pipeline: a")
    print("  low-order component (the landing interpolation) or an exactly")
    print("  integrable test problem can each hide the true order.")

    section("3. Linear drag: exact solution versus integration")
    k = 0.20          # 1/s, SYNTHETIC drag coefficient per unit speed
    m = 1.0
    v_term = G_LOCAL / k
    print(f"  linear drag a = -g - k v, k = {k} 1/s")
    print(f"  terminal velocity = g/k = {v_term:.4f} m/s")
    def linear_drag(v, k=k):
        return (-k * v[0], -k * v[1])
    v_num = rk4(0.0, 0.0, 1.0e-3, 20.0, drag=linear_drag)[3]
    v_exact = -v_term * (1 - math.exp(-k * 20.0))
    print(f"  after 20 s of fall: RK4 vy = {v_num:.6f} m/s, "
          f"exact = {v_exact:.6f} m/s")
    print(f"  (the body was launched from rest, so this is a vertical drop)")
    print(f"  fraction of terminal speed reached in 20 s = "
          f"{abs(v_num) / v_term:.6f}")

    section("4. Quadratic drag: range reduction, measured")
    v0, angle = 20.0, math.radians(45.0)
    rng_vac = v0 ** 2 * math.sin(2 * angle) / G_LOCAL
    print(f"  vacuum range at 45 deg = {rng_vac:.6f} m")
    for c in (0.0, 0.002, 0.005, 0.01):
        if c == 0.0:
            continue
        def drag(v, c=c):
            speed = math.hypot(*v)
            return (-c * speed * v[0], -c * speed * v[1])
        # integrate until y returns to zero
        dt = 1.0e-4
        x, y, vx, vy = 0.0, 0.0, v0 * math.cos(angle), v0 * math.sin(angle)
        while y >= 0.0:
            ax = -c * math.hypot(vx, vy) * vx
            ay = -G_LOCAL - c * math.hypot(vx, vy) * vy
            x, y = x + dt * vx, y + dt * vy
            vx, vy = vx + dt * ax, vy + dt * ay
        print(f"  c = {c:.4f} m^-1: range = {x:8.3f} m "
              f"({100 * x / rng_vac:.2f}% of the vacuum value)")

    section("5. A borehole drop: how long to fall 400 m?")
    depth = 400.0
    print(f"  vacuum free fall from rest: t = "
          f"{math.sqrt(2 * depth / G_LOCAL):.4f} s")
    def drag2(v):
        """Quadratic drag acceleration only; gravity is added by the caller."""
        c = 0.002
        sp = math.hypot(*v)
        return (-c * sp * v[0], -c * sp * v[1])
    dt = 1.0e-4
    y, vy, t = 0.0, 0.0, 0.0
    while y > -depth:
        _, drag_ay = drag2((0.0, vy))
        ay = -G_LOCAL + drag_ay
        y += dt * vy
        vy += dt * ay
        t += dt
    print(f"  with quadratic drag c = 0.002 m^-1: t = {t:.4f} s "
          f"(difference {t - math.sqrt(2 * depth / G_LOCAL):+.4f} s)")
    print("  The sign and size of the difference is what a calibration drop")
    print("  test measures; the vacuum time is an upper bound on the speed and")
    print("  a lower bound on the time.")


if __name__ == "__main__":
    main()
