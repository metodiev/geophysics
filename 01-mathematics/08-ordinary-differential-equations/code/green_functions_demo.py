"""Green's functions and impulse response.

Run:  python3 green_functions_demo.py
Requires: Python standard library only.

Companion to lesson 01-08-06.

A Green's function is the response to a unit impulse. The four objects
constructed and verified here are

  1. first-order operator   L = d/dt + a        G(t) = exp(-a t),  t >= 0
  2. undamped oscillator    L = d^2/dt^2 + w0^2 G(t) = sin(w0 t)/w0
  3. damped oscillator      L = d^2/dt^2 + 2 z w0 d/dt + w0^2
                                                 G(t) = exp(-z w0 t) sin(wd t)/wd
  4. spatial operator       L = -d^2/dx^2 on (0,1), u(0)=u(1)=0
                                                 G(x,xi) = x(1-xi), x <= xi

Each is verified three ways where possible: against a direct integration of
the ODE with a narrow pulse (the impulse limit), against convolution of the
Green's function with a smooth forcing (the superposition property), and, for
the oscillator, against the inverse Fourier transform of the frequency-domain
response (which also demonstrates causality).
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def rk4_first_order(f, t0, y0, h, n):
    """Integrate y' = f(t, y) with n RK4 steps of size h."""
    t, y = t0, y0
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h * k1 / 2)
        k3 = f(t + h / 2, y + h * k2 / 2)
        k4 = f(t + h, y + h * k3)
        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h
    return y


def rk4_scalar_forced(f, t0, y0, v0, h, n):
    """Integrate x'' = f(t, x, v) from (y0, v0) with n RK4 steps of size h."""
    t, y, v = t0, y0, v0
    for _ in range(n):
        a1 = f(t, y, v)
        k1y, k1v = v, a1
        a2 = f(t + h / 2, y + h * k1y / 2, v + h * k1v / 2)
        k2y, k2v = v + h * k1v / 2, a2
        a3 = f(t + h / 2, y + h * k2y / 2, v + h * k2v / 2)
        k3y, k3v = v + h * k2v / 2, a3
        a4 = f(t + h, y + h * k3y, v + h * k3v)
        k4y, k4v = v + h * k3v, a4
        y += h / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)
        v += h / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        t += h
    return y, v


def convolve(G, f, t, n=4000):
    """Integral_0^t G(t - s) f(s) ds by composite Simpson, cutoff at t."""
    if t <= 0.0:
        return 0.0
    if n % 2:
        n += 1
    h = t / n
    s = G(t - 0.0) * f(0.0) + G(0.0) * f(t)
    for i in range(1, n):
        si = i * h
        s += (4 if i % 2 else 2) * G(t - si) * f(si)
    return s * h / 3.0


def thomas(a, b, c, d):
    """Solve a tridiagonal system with sub-diagonal a, diagonal b, super c, rhs d."""
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
    section("1. First-order operator: G(t) = exp(-a t) for t >= 0")
    a = 2.0
    G1 = lambda t: math.exp(-a * t) if t >= 0 else 0.0
    f1 = lambda s: math.sin(3.0 * s)
    print(f"y' + {a} y = f(t), y(0) = 0, so y(t) = integral_0^t "
          f"exp(-{a}(t-s)) f(s) ds")
    print(f"{'t':>7}{'convolution':>16}{'RK4':>16}{'difference':>14}")
    for t in (0.5, 1.0, 2.0, 4.0):
        cv = convolve(G1, f1, t, 20000)
        rk = rk4_first_order(lambda tt, y: f1(tt) - a * y, 0.0, 0.0,
                             t / 20000.0, 20000)
        print(f"{t:>7.1f}{cv:>16.9f}{rk:>16.9f}{abs(cv - rk):>14.2e}")
    print("Impulse response and convolution reproduce the ODE solution: that is")
    print("the whole content of 'the Green's function solves the problem'.")

    section("2. Impulse limit: a narrow pulse tends to the delta function")
    zeta, omega0 = 0.08, 2.0
    wd = omega0 * math.sqrt(1 - zeta ** 2)
    G3 = lambda t: (math.exp(-zeta * omega0 * t) * math.sin(wd * t) / wd
                    if t >= 0 else 0.0)
    t_obs = 1.0
    print(f"oscillator: omega0 = {omega0}, zeta = {zeta}, wd = {wd:.9f}")
    print(f"forcing: rectangular pulse of width eps and unit area, "
          f"evaluated at t = {t_obs}")
    print(f"{'eps':>9}{'pulse response':>18}{'G(t)':>14}{'|error|':>12}"
          f"{'ratio':>9}")
    prev = None
    for eps in (0.4, 0.2, 0.1, 0.05, 0.025):
        f = lambda s, eps=eps: (1.0 / eps) if s < eps else 0.0
        val = convolve(G3, f, t_obs, 20000)
        err = abs(val - G3(t_obs))
        r = "" if prev is None else f"{prev / err:9.2f}"
        print(f"{eps:>9.3f}{val:>18.9f}{G3(t_obs):>14.9f}{err:>12.3e}{r}")
        prev = err
    print("The error falls in proportion to the pulse width: the pulse response")
    print("approaches G(t) at first order, which is exactly what delta(x - xi)")
    print("means as a weak limit. It never equals G(t) at finite eps, and the")
    print("difference is physical, not numerical.")

    section("3. Damped oscillator: convolution with a Green's function")
    print("forcing: a symmetric wavelet f(s) = (1 - 2 s^2) exp(-s^2), s = (t-tc)/w")
    tc, w = 2.0, 0.4
    f3 = lambda s: (1.0 - 2.0 * ((s - tc) / w) ** 2) * math.exp(-((s - tc) / w) ** 2)
    print(f"{'t':>7}{'convolution':>16}{'RK4':>16}{'difference':>14}")
    for t in (1.0, 2.0, 3.0, 4.0, 6.0):
        cv = convolve(G3, f3, t, 40000)
        rk, _ = rk4_scalar_forced(
            lambda tt, y, v: f3(tt) - 2 * zeta * omega0 * v - omega0 ** 2 * y,
            0.0, 0.0, 0.0, t / 40000.0, 40000)
        print(f"{t:>7.1f}{cv:>16.9f}{rk:>16.9f}{abs(cv - rk):>14.2e}")
    print("For a smooth forcing the agreement is at the quadrature floor: the")
    print("response to any source is the convolution of that source with the")
    print("impulse response. This is the statement behind instrument response")
    print("correction and source-time-function deconvolution.")

    section("4. Undamped oscillator at resonance: linear growth")
    w0 = 1.0
    G2 = lambda t: math.sin(w0 * t) / w0 if t >= 0 else 0.0
    f2 = lambda s: math.sin(w0 * s)
    print("x'' + x = sin(t), x(0) = x'(0) = 0")
    print("exact solution: x = (sin t - t cos t)/2, whose envelope grows as t/2")
    print(f"{'t':>8}{'convolution':>16}{'exact':>16}{'difference':>14}")
    for t in (5.0, 10.0, 20.0, 40.0):
        cv = convolve(G2, f2, t, 40000)
        exact = (math.sin(t) - t * math.cos(t)) / 2
        print(f"{t:>8.1f}{cv:>16.9f}{exact:>16.9f}{abs(cv - exact):>14.2e}")
    print("Driving an undamped oscillator at its natural frequency gives an")
    print("amplitude growing linearly as t/2, not a bounded resonance. Damping")
    print("is what converts this unbounded growth into a finite amplitude Q; the")
    print("build-up time 2Q/omega0 of lesson 03 is the damped version of this.")

    section("5. Spatial Green's function: -u'' = f, u(0) = u(1) = 0")
    print("G(x,xi) = x(1-xi) for x <= xi, and xi(1-x) for x >= xi")
    print("The 3-point stencil with the source placed exactly on a node is")
    print("EXACT here, because the exact G is piecewise linear and its second")
    print("difference vanishes at every node except the source node:")
    print(f"{'n interior nodes':>18}{'max |u_h - G| over nodes':>26}")
    for n in (20, 40, 80, 160):
        h = 1.0 / (n + 1)
        j = n // 2
        rhs = [0.0] * n
        rhs[j] = 1.0 / h
        diag = [2.0 / h ** 2] * n
        sub = [0.0] + [-1.0 / h ** 2] * (n - 1)
        sup = [-1.0 / h ** 2] * (n - 1) + [0.0]
        u = thomas(sub, diag, sup, rhs)
        err = 0.0
        for i in range(n):
            x = (i + 1) * h
            xi_i = (j + 1) * h
            exact = x * (1 - xi_i) if x <= xi_i else xi_i * (1 - x)
            err = max(err, abs(u[i] - exact))
        print(f"{n:>18}{err:>26.3e}")
    print("Now place the source off-centre. First naively: put all of its weight")
    print("on the nearest node, which is what a careless code does.")
    print(f"{'n interior nodes':>18}{'max |u_h - G|':>16}{'ratio':>9}")
    prev = None
    for n in (20, 40, 80, 160):
        h = 1.0 / (n + 1)
        k = n // 3
        xi = (k + 1.5) * h                  # true source location, mid-cell
        rhs = [0.0] * n
        rhs[k] = 1.0 / h                    # all weight at the nearest node
        diag = [2.0 / h ** 2] * n
        sub = [0.0] + [-1.0 / h ** 2] * (n - 1)
        sup = [-1.0 / h ** 2] * (n - 1) + [0.0]
        u = thomas(sub, diag, sup, rhs)
        err = 0.0
        for i in range(n):
            x = (i + 1) * h
            exact = x * (1 - xi) if x <= xi else xi * (1 - x)
            err = max(err, abs(u[i] - exact))
        r = "" if prev is None else f"{prev / err:9.2f}"
        print(f"{n:>18}{err:>16.3e}{r:>9}")
        prev = err
    print("Halving h only halves the error: misplacing the source costs one")
    print("order. Now distribute the source with the hat function of the grid,")
    print("which is the distribution consistent with the 3-point stencil:")
    print(f"{'n interior nodes':>18}{'max |u_h - G|':>16}")
    for n in (20, 40, 80, 160):
        h = 1.0 / (n + 1)
        k = n // 3
        alpha = 0.5
        xi = (k + 1 + alpha) * h
        rhs = [0.0] * n
        rhs[k] += (1.0 - alpha) / h
        rhs[k + 1] += alpha / h
        diag = [2.0 / h ** 2] * n
        sub = [0.0] + [-1.0 / h ** 2] * (n - 1)
        sup = [-1.0 / h ** 2] * (n - 1) + [0.0]
        u = thomas(sub, diag, sup, rhs)
        err = 0.0
        for i in range(n):
            x = (i + 1) * h
            exact = x * (1 - xi) if x <= xi else xi * (1 - x)
            err = max(err, abs(u[i] - exact))
        print(f"{n:>18}{err:>16.3e}")
    print("Back to machine precision. The lesson is not that this stencil is")
    print("magic: it is that the accuracy of a Green's function calculation")
    print("depends on how the source is represented, and that representation")
    print("must match the scheme's own interpolation. A source term is a")
    print("functional, not a function, and discretising it carelessly can cost")
    print("more accuracy than the scheme's formal order.")

    section("6. Reciprocity: G(x,xi) = G(xi,x), and superposition")
    n = 60
    h = 1.0 / (n + 1)
    sub = [0.0] + [-1.0 / h ** 2] * (n - 1)
    sup = [-1.0 / h ** 2] * (n - 1) + [0.0]
    diag = [2.0 / h ** 2] * n

    def column(j):
        rhs = [0.0] * n
        rhs[j] = 1.0 / h
        return thomas(sub, diag, sup, rhs)

    i, j = 10, 45
    col_j = column(j)
    col_i = column(i)
    print(f"n = {n}: source at node {j}, response at node {i}: {col_j[i]:.9f}")
    print(f"        source at node {i}, response at node {j}: {col_i[j]:.9f}")
    print(f"        relative asymmetry: "
          f"{abs(col_j[i] - col_i[j]) / abs(col_j[i]):.3e}")
    # Superposition: response to two sources equals the sum of responses.
    rhs_sum = [0.0] * n
    rhs_sum[i] = 1.0 / h
    rhs_sum[j] = 1.0 / h
    both = thomas(sub, diag, sup, rhs_sum)
    k = 25
    print(f"superposition at node {k}: u[i+j sources] = {both[k]:.9f}, "
          f"u[i] + u[j] = {col_i[k] + col_j[k]:.9f}")
    print("Reciprocity is the symmetry of the Green's function; superposition")
    print("is the linearity that lets a general source be written as a sum of")
    print("impulses. Both are exact for this operator and hold in the discrete")
    print("system as well as the continuous one.")

    section("7. Frequency domain and causality: one integral, two answers")
    zeta, omega0 = 0.1, 1.0
    wd = omega0 * math.sqrt(1 - zeta ** 2)

    def G_time(t):
        if t < 0:
            return 0.0
        return math.exp(-zeta * omega0 * t) * math.sin(wd * t) / wd

    # Ghat(omega) = 1 / (omega0^2 - omega^2 + 2 i zeta omega0 omega)
    # G(t) = (1/pi) Re integral_0^inf Ghat(omega) exp(i omega t) d omega
    big = 1200.0
    npts = 120000                      # even -> Simpson, d omega = 0.01
    dw = big / npts
    print(f"omega0 = {omega0}, zeta = {zeta}; band |omega| <= {big:.0f}, "
          f"{npts} points (d omega = {dw:.5f})")
    print(f"{'t':>8}{'inverse transform':>20}{'G(t) from formula':>20}"
          f"{'difference':>14}")
    for t in (-6.0, -3.0, -1.0, 0.5, 1.0, 2.0, 4.0, 8.0):
        total = 0.0
        for i in range(0, npts + 1):
            om = i * dw
            # Re[Ghat e^{i om t}] with a complex reciprocal
            den = complex(omega0 ** 2 - om * om, 2 * zeta * omega0 * om)
            val = (1.0 / den) * complex(math.cos(om * t), math.sin(om * t))
            wgt = 1 if i in (0, npts) else (4 if i % 2 else 2)
            total += wgt * val.real
        total *= dw / 3.0 / math.pi
        print(f"{t:>8.1f}{total:>20.9f}{G_time(t):>20.9f}"
              f"{abs(total - G_time(t)):>14.2e}")
    print("For t < 0 the integral is zero to about 2e-8, set by the width of the")
    print("integration band and not by the physics; for t > 0 it reproduces the")
    print("time-domain formula. That asymmetry IS causality: the same function")
    print("Ghat(omega) describes a system that cannot respond before it is")
    print("driven. An acausal Ghat (for example one with a pole in the lower")
    print("half plane) would give a non-zero result for t < 0.")

    section("8. What this is used for")
    print("Convolution with a Green's function is the forward model in most of")
    print("observational geophysics:")
    print("   - instrument response correction: divide out a known Ghat(omega)")
    print("   - source-time-function deconvolution in seismology")
    print("   - the representation theorem, in which the displacement field is a")
    print("     convolution of a moment-tensor source with the medium's Green's")
    print("     function, summed over source and receiver components")
    print("Everything above is the one-dimensional, scalar case of that idea;")
    print("the spatial problem of Section 5 is the same statement in x.")


if __name__ == "__main__":
    main()
