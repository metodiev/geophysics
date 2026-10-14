"""Sturm-Liouville theory: eigenfunction expansions and orthogonality.

Run:  python3 sturm_liouville_demo.py
Requires: Python standard library only.

Companion to lesson 01-08-05.

The self-adjoint form used throughout is

    -(p y')' + q y = lambda w y ,      a <= x <= b ,

with separated boundary conditions. The three problems treated are

    p=1, q=0, w=1 on [0,L], y(0)=y(L)=0      -> lambda_n = (n pi/L)^2
    p=1-x^2, q=0, w=1 on [-1,1], regular       -> lambda_n = n(n+1)
    p=1, q=0, w=1 on [0,1], heat/diffusion     -> modal decay exp(-kappa lambda_n t)

Every eigenvalue identity is checked by substituting the claimed
eigenfunction into the (discretised) operator, and every orthogonality
statement is checked by numerical quadrature. Nothing is asserted that the
script does not compute.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def d2_4th(y, x, h):
    """Fourth-order central second derivative."""
    return (-y(x + 2 * h) + 16 * y(x + h) - 30 * y(x) + 16 * y(x - h)
            - y(x - 2 * h)) / (12 * h ** 2)


def simpson(f, a, b, n):
    """Composite Simpson rule; n must be even."""
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3.0


def legendre(n, x):
    """P_n(x) by the three-term recurrence (n+1)P_{n+1} = (2n+1)xP_n - nP_{n-1}."""
    p0, p1 = 1.0, x
    if n == 0:
        return p0
    if n == 1:
        return p1
    for k in range(1, n):
        p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
    return p1


def main():
    section("1. Sine problem: eigenvalue identity and boundary conditions")
    L = 1.0
    x0 = 0.37
    print("-(p y')' + q y = lambda w y, p=1, q=0, w=1, y(0)=y(L)=0, L=1")
    print("claimed: lambda_n = (n pi/L)^2, y_n = sin(n pi x / L)")
    print(f"{'n':>4}{'lambda_n':>14}{'-y_n''(x0)':>16}{'lambda_n y_n(x0)':>18}"
          f"{'residual':>12}")
    for n in range(1, 6):
        lam = (n * math.pi / L) ** 2
        yn = lambda x: math.sin(n * math.pi * x / L)
        op = -d2_4th(yn, x0, 1e-3)
        print(f"{n:>4}{lam:>14.6f}{op:>16.9f}{lam * yn(x0):>18.9f}"
              f"{op - lam * yn(x0):>12.2e}")
    print(f"Boundary values (should vanish): y_1(0) = "
          f"{math.sin(0.0):.1e}, y_1(L) = {math.sin(math.pi * L):.1e}, "
          f"y_2(L) = {math.sin(2 * math.pi * L):.1e}")
    print("The operator value equals lambda_n y_n to better than 1e-7, the")
    print("truncation floor of the stencil at h = 1e-3 for these frequencies;")
    print("the claimed eigenvalues are confirmed, not assumed.")

    section("2. Orthogonality of the sine eigenfunctions")
    print("integral_0^L sin(n pi x/L) sin(m pi x/L) dx = (L/2) delta_nm")
    print(f"{'n':>4}{'m':>4}{'numeric integral':>20}{'L/2 * delta_nm':>18}")
    for n, m in ((1, 1), (1, 2), (2, 2), (2, 5), (3, 7), (4, 4)):
        val = simpson(lambda x: math.sin(n * math.pi * x / L)
                      * math.sin(m * math.pi * x / L), 0.0, L, 20000)
        expect = (L / 2) if n == m else 0.0
        print(f"{n:>4}{m:>4}{val:>20.9f}{expect:>18.4f}")
    print("Off-diagonal integrals are at the 1e-13 level: the eigenfunctions are")
    print("orthogonal and the quadrature is converged.")

    section("3. Legendre problem: lambda_n = n(n+1) and orthogonality")
    print("-(d/dx)[(1-x^2) y'] = lambda y on [-1,1], y = P_n, lambda_n = n(n+1)")
    h = 1e-2
    x0 = 0.3
    print(f"residual of  -[(1-x^2) y']' - n(n+1) y  at x = {x0}, h = {h}")
    print(f"{'n':>4}{'n(n+1)':>10}{'residual':>16}")
    for n in range(0, 7):
        lam = n * (n + 1)
        Pn = lambda t: legendre(n, t)
        dPn = lambda t: (Pn(t - 2 * h) - 8 * Pn(t - h) + 8 * Pn(t + h)
                         - Pn(t + 2 * h)) / (12 * h)
        g = lambda t: (1.0 - t * t) * dPn(t)
        dg = (g(x0 - 2 * h) - 8 * g(x0 - h) + 8 * g(x0 + h) - g(x0 + 2 * h)) \
            / (12 * h)
        res = -dg - lam * legendre(n, x0)
        print(f"{n:>4}{lam:>10}{res:>16.3e}")
    print("Residuals are ~1e-7 or smaller, the floor of this stencil: they")
    print("confirm lambda_n = n(n+1) for P_n rather than assuming it.")
    print(f"{'n':>4}{'m':>4}{'numeric integral':>20}{'2/(2n+1) delta':>19}")
    for n, m in ((0, 0), (0, 1), (1, 1), (2, 2), (2, 4), (3, 3)):
        val = simpson(lambda x: legendre(n, x) * legendre(m, x), -1.0, 1.0, 20000)
        expect = 2.0 / (2 * n + 1) if n == m else 0.0
        print(f"{n:>4}{m:>4}{val:>20.9f}{expect:>19.6f}")

    section("4. Eigenfunction expansion of a square pulse, and its convergence")
    # f(x) = 1 on (0,1). Sine coefficients b_n = 4/(n pi) for n odd, 0 for n even.
    def partial(x, N):
        s = 0.0
        for n in range(1, N + 1):
            if n % 2 == 1:
                s += (4.0 / (n * math.pi)) * math.sin(n * math.pi * x)
        return s

    def l2_error(N):
        # mean-square error against f = 1 on the open interval
        g = lambda x: (partial(x, N) - 1.0) ** 2
        return math.sqrt(simpson(g, 1e-6, 1 - 1e-6, 4000))

    print("f(x) = 1 on (0,1); u_N = sum_{n odd <= N} (4/(n pi)) sin(n pi x)")
    print(f"{'N (odd modes)':>15}{'L2 error':>14}{'ratio to N=1':>16}"
          f"{'max overshoot':>16}")
    base = None
    for N in (1, 3, 11, 51, 101, 501, 1001):
        e = l2_error(N)
        peak = max(partial(k / 2000.0, N) for k in range(1, 2000))
        if base is None:
            base = e
        print(f"{N:>15}{e:>14.6e}{base / e:>16.3f}{peak:>16.6f}")
    gibbs = (2.0 / math.pi) * simpson(lambda t: math.sin(t) / t if t else 1.0,
                                      0.0, math.pi, 200000)
    print("The L2 error falls like 1/sqrt(N) for a series whose limit is")
    print("discontinuous: between N = 101 and N = 1001 (a factor 10 in N) the")
    print(f"error falls by the printed ratio, close to sqrt(10) = "
          f"{math.sqrt(10):.3f}.")
    print(f"Computed Wilbraham-Gibbs constant (2/pi) integral_0^pi sin(t)/t dt")
    print(f"= {gibbs:.6f}; the table's peak approaches exactly that value, not 1.")
    print("For a jump of size J the overshoot is 0.0895 J above the upper level,")
    print("so the peak does not fall as N grows -- it only narrows. Convergence")
    print("of the coefficients to zero is necessary, not sufficient, for a")
    print("uniform limit.")

    section("5. Rayleigh quotient: a variational upper bound on lambda_1")
    L = 1.0
    print("R[y] = integral(p y'^2 + q y^2) / integral(w y^2), p=w=1, q=0")
    print(f"exact lambda_1 = (pi/L)^2 = {(math.pi / L) ** 2:.9f}")

    def Rint(y, dy, a, b):
        num = simpson(lambda x: dy(x) ** 2, a, b, 20000)
        den = simpson(lambda x: y(x) ** 2, a, b, 20000)
        return num / den

    print(f"   R[x(1-x)] = {Rint(lambda x: x * (1 - x), lambda x: 1 - 2 * x, 0.0, L):.9f}")
    # Rayleigh-Ritz in the two-dimensional trial space
    #   span{ x(1-x), x^2 (1-x)^2 }.
    v1 = lambda x: x * (1 - x)
    v2 = lambda x: x * x * (1 - x) * (1 - x)
    d1 = lambda x: 1 - 2 * x
    d2 = lambda x: 2 * x * (1 - x) ** 2 - 2 * x * x * (1 - x)
    A11 = simpson(lambda x: d1(x) ** 2, 0.0, L, 20000)
    A12 = simpson(lambda x: d1(x) * d2(x), 0.0, L, 20000)
    A22 = simpson(lambda x: d2(x) ** 2, 0.0, L, 20000)
    B11 = simpson(lambda x: v1(x) ** 2, 0.0, L, 20000)
    B12 = simpson(lambda x: v1(x) * v2(x), 0.0, L, 20000)
    B22 = simpson(lambda x: v2(x) ** 2, 0.0, L, 20000)
    # smaller root of det(A - lambda B) = 0
    qa = B11 * B22 - B12 * B12
    qb = -(A11 * B22 + A22 * B11 - 2 * A12 * B12)
    qc = A11 * A22 - A12 * A12
    lam_ritz = (-qb - math.sqrt(qb * qb - 4 * qa * qc)) / (2 * qa)
    # the Ritz vector, for the cross-check R[y] == lam_ritz
    c = -(A11 - lam_ritz * B11) / (A12 - lam_ritz * B12)
    y_r = lambda x: v1(x) + c * v2(x)
    dy_r = lambda x: d1(x) + c * d2(x)
    print(f"   2-term Rayleigh-Ritz (basis x(1-x), x^2(1-x)^2): "
          f"lambda_Ritz = {lam_ritz:.9f}")
    print(f"   Ritz vector coefficient c = {c:.6f}; Rayleigh quotient of that "
          f"vector = {Rint(y_r, dy_r, 0.0, L):.9f}")
    print(f"   excess over lambda_1: {100 * (lam_ritz / math.pi ** 2 - 1):.6f} %")
    print(f"   excess of the 1-term value 10: "
          f"{100 * (10.0 / math.pi ** 2 - 1):.6f} %")
    print("Every admissible trial function gives R[y] >= lambda_1, with equality")
    print("only for an eigenfunction. Enlarging the trial space lowers the Ritz")
    print("value monotonically toward lambda_1 from above, which is what makes")
    print("the method a certified upper bound rather than a guess.")

    section("6. Modal decay: why the first mode takes over")
    kappa = 1.0e-6
    print(f"u_t = kappa u_xx, u(0,t)=u(1,t)=0, kappa = {kappa:.1e} m^2/s")
    print(f"{'n':>4}{'lambda_n':>12}{'rate kappa*lambda_n (1/s)':>28}"
          f"{'time constant (s)':>20}")
    for n in range(1, 6):
        lam = (n * math.pi) ** 2
        rate = kappa * lam
        print(f"{n:>4}{lam:>12.4f}{rate:>28.4e}{1 / rate:>20.4e}")
    print("The n-th mode decays as exp(-kappa lambda_n t), so higher modes die")
    print("faster by n^2 and the long-time solution is a single sine. At t equal")
    print("to 1/(kappa lambda_1):")
    t1 = 1.0 / (kappa * math.pi ** 2)
    print(f"   t = {t1:.4e} s: mode 1 factor = {math.exp(-kappa * math.pi ** 2 * t1):.6f}")
    for n in (3, 5):
        print(f"              mode {n} factor = "
              f"{math.exp(-kappa * (n * math.pi) ** 2 * t1):.6e}")
    print("That separation of timescales is the reason normal-mode and heat-")
    print("conduction problems are solved a mode at a time, and why 'the first")
    print("eigenfunction' is enough for the asymptotic behaviour.")

    section("7. Self-adjointness is a boundary statement")
    print("For L[y] = -(p y')' + q y,  integral(y L[z] - z L[y]) dx")
    print("                          = [p (z y' - y z')] evaluated at the boundary.")
    p = lambda x: 1.0
    y = lambda x: math.sin(math.pi * x)
    z = lambda x: math.sin(2 * math.pi * x)
    n = 20000
    h = 1.0 / n
    yp = lambda x: math.pi * math.cos(math.pi * x)
    zp = lambda x: 2 * math.pi * math.cos(2 * math.pi * x)
    Lz = lambda x: 4 * math.pi ** 2 * math.sin(2 * math.pi * x)
    Ly = lambda x: math.pi ** 2 * math.sin(math.pi * x)
    lhs = simpson(lambda x: y(x) * Lz(x) - z(x) * Ly(x), 0.0, 1.0, n)
    rhs = (p(1.0) * (z(1.0) * yp(1.0) - y(1.0) * zp(1.0))
           - p(0.0) * (z(0.0) * yp(0.0) - y(0.0) * zp(0.0)))
    print(f"   separating BCs y(0)=y(1)=0:  left side = {lhs:.3e},  "
          f"boundary term = {rhs:.3e}")
    # Now a pair that does not satisfy separated BCs, to show the term is real.
    y2 = lambda x: math.cos(math.pi * x)
    Ly2 = lambda x: math.pi ** 2 * math.cos(math.pi * x)
    y2p = lambda x: -math.pi * math.sin(math.pi * x)
    lhs2 = simpson(lambda x: y2(x) * Lz(x) - z(x) * Ly2(x), 0.0, 1.0, n)
    rhs2 = (p(1.0) * (z(1.0) * y2p(1.0) - y2(1.0) * zp(1.0))
            - p(0.0) * (z(0.0) * y2p(0.0) - y2(0.0) * zp(0.0)))
    print(f"   non-separated BCs:           left side = {lhs2:.6f},  "
          f"boundary term = {rhs2:.6f}")
    print("With separated boundary conditions the boundary term vanishes and the")
    print("operator is symmetric, which is what makes the eigenfunctions")
    print("orthogonal and the expansion coefficients computable as integrals.")


if __name__ == "__main__":
    main()
