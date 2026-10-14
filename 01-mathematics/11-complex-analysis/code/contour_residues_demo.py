"""Contour integration and residues: every closed form checked numerically.

Run:  python3 contour_residues_demo.py
Requires: Python standard library only (``cmath``).

Companion to lesson 01-11-03 (Contour Integration, Residues and Real
Integrals).

For each integral the demo reports

* the value obtained by *real* numerical quadrature alone,
* the closed form obtained by residues,
* the residue computed numerically from a small circular contour, and
* for the semicircle cases, the contribution of the closing arc, so that the
  step "the arc vanishes" is measured rather than assumed.

Quadrature machinery
--------------------
``quad_sinh`` uses the substitution x = sinh t, which turns an integrand
decaying like x^-n into one decaying like exp(-(n-1)|t|); the truncated
trapezoid/Simpson rule is then accurate to near round-off.  ``quad_osc``
integrates oscillatory integrands over a long finite interval and adds the
first-order asymptotic tail obtained by integrating exp(i x) by parts once.
"""

import cmath
import math


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --------------------------------------------------------------------------
# Quadrature
# --------------------------------------------------------------------------

def simpson(f, a, b, n):
    """Composite Simpson rule; n must be even."""
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for j in range(1, n):
        total += (4.0 if j % 2 else 2.0) * f(a + j * h)
    return total * h / 3.0


def quad_sinh(f, t_max=40.0, n=20000):
    """Integral of f over (-inf, inf) via x = sinh t, midpoint-free Simpson.

    The nodes stop at |t| = t_max; for the integrands used here the discarded
    tail is smaller than 1e-15, which is checked by the convergence column
    printed in the demo.
    """
    g = lambda t: f(math.sinh(t)) * math.cosh(t)
    return simpson(g, -t_max, t_max, n)


def quad_cos(g, omega, L=200.0, per_period=400):
    """Integral of g(x) cos(omega x) over (0, inf) for algebraically decaying g.

    Integrates over [0, L] with a fixed number of nodes per oscillation, then
    adds the two-term asymptotic tail obtained by integrating
    exp(i omega x) by parts twice:

        int_L^inf g(x) e^{i omega x} dx
            = i e^{i omega L} g(L)/omega - e^{i omega L} g'(L)/omega^2
              + O(g''/omega^3),

    whose real part is the correction applied here.  The error is then
    O(g''(L)/omega^3) = O(L^-4), far below the truncation error of a bare
    integral over [0, L], which would be O(g(L)) = O(L^-2).
    """
    n = int(math.ceil(per_period * L * omega / (2 * math.pi)))
    if n % 2:
        n += 1
    main = simpson(lambda x: g(x) * math.cos(omega * x), 0.0, L, n)
    h = 1e-6
    gp = (g(L + h) - g(L - h)) / (2 * h)
    tail = -g(L) * math.sin(omega * L) / omega - gp * math.cos(omega * L) / (omega ** 2)
    return main + tail


def quad_sin_over_x(L=2000.0, n=400000):
    """Integral of sin(x)/x over (0, inf) with a two-term tail correction.

    int_L^inf sin x / x dx = cos L / L + sin L / L^2 + O(L^-3).
    """
    main = simpson(lambda x: math.sin(x) / x if x else 1.0, 0.0, L, n)
    return main + math.cos(L) / L + math.sin(L) / (L * L)


def contour_integral(f, centre, radius, n=4096):
    """Value of the closed contour integral of f around a circle, by trapezoid.

    The integrand is 2*pi*i-periodic and analytic, so the trapezoidal rule is
    spectrally accurate: doubling n changes nothing beyond round-off.
    """
    acc = 0j
    for j in range(n):
        t = 2 * math.pi * j / n
        z = centre + radius * cmath.exp(1j * t)
        dz = 1j * radius * cmath.exp(1j * t) * (2 * math.pi / n)
        acc += f(z) * dz
    return acc


def arc_integral(f, radius, n=200000):
    """Integral of f over the upper semicircle |z| = radius, Im z >= 0."""
    acc = 0j
    for j in range(n + 1):
        t = math.pi * j / n
        z = radius * cmath.exp(1j * t)
        dz = 1j * radius * cmath.exp(1j * t) * (math.pi / n)
        acc += f(z) * dz
    return acc


def main():
    section("1. The building block: integral of 1/(1+x^2) = pi")
    f = lambda x: 1.0 / (1.0 + x * x)
    print(f"  sinh-substitution quadrature: {quad_sinh(f):.15f}")
    print(f"  pi                          : {math.pi:.15f}")
    print(f"  difference                  : {abs(quad_sinh(f) - math.pi):.3e}")
    print("  Convergence with the truncation point and the node count:")
    print(f"    {'t_max':>8} {'n':>8} {'value':>20} {'error':>10}")
    for t_max, n in [(5.0, 2000), (10.0, 5000), (20.0, 10000), (40.0, 20000)]:
        val = quad_sinh(f, t_max, n)
        print(f"    {t_max:>8.0f} {n:>8} {val:>20.15f} {abs(val - math.pi):>10.2e}")

    section("2. Residue theorem and the vanishing arc")
    g = lambda z: 1.0 / (1.0 + z * z)
    for radius in (5.0, 20.0, 100.0, 500.0):
        arc = arc_integral(g, radius, n=20000)
        real_part = quad_sinh(lambda x: 1.0 / (1.0 + x * x), t_max=math.asinh(radius), n=40000)
        total = real_part + arc
        print(f"  R = {radius:>6.0f}: real line = {real_part:>12.9f},"
              f" arc = {abs(arc):>10.3e}, sum = {total.real:>12.9f}"
              f"{total.imag:+.2e}i, 2*pi*i*Res = {2j * math.pi * (-0.5j):.9f}")
    print("  The arc contribution falls off like 1/R while the residue term is")
    print("  constant, so the closure is legitimate: measured, not assumed.")
    print("  R * |arc| (measured) at R = 5, 20, 100, 500:")
    print("    " + ", ".join(
        f"{radius * abs(arc_integral(g, radius, n=20000)):.6f}"
        for radius in (5.0, 20.0, 100.0, 500.0)))
    print("  The product is constant, and equal to 2, not pi: the leading term of")
    print("  the arc expansion cancels over the semicircle because")
    print("  int_0^pi exp(-2i theta) dtheta = 0.  The 2/R is the next term, from")
    print("  1/(1+z^2) = z^-2 - z^-4 + ..., so do not trust a bound that only")
    print("  says 'the arc is O(1/R)' without checking whether it cancels.")
    print("  Condition for the closure: f(z) -> 0 uniformly as |z| -> infinity,")
    print("  which here means degree(denominator) >= degree(numerator) + 2.")

    section("3. Residues verified from a circular contour")
    test_functions = [
        ("1/(1+z^2), simple pole at i", lambda z: 1 / (1 + z * z),
         1j, 1 / (2j), "simple"),
        ("1/(1+z^2)^2, double pole at i", lambda z: 1 / (1 + z * z) ** 2,
         1j, 1 / (4j), "double"),
        ("1/(z^2+2z+5), simple pole at -1+2i",
         lambda z: 1 / (z * z + 2 * z + 5), -1 + 2j, 1 / (4j), "simple"),
    ]
    print(f"  {'pole':>34} {'analytic Res':>22} {'numeric Res':>22}"
          f" {'error':>9}")
    for label, func, z0, res_analytic, _kind in test_functions:
        for radius in (0.3, 0.05, 0.005):
            num = contour_integral(func, z0, radius) / (2j * math.pi)
        print(f"  {label:>34} {res_analytic.real:>10.6f}{res_analytic.imag:>+10.6f}i"
              f" {num.real:>10.6f}{num.imag:>+10.6f}i"
              f" {abs(num - res_analytic):>9.2e}")
    print("  Radius 0.005 is the last one used; the trapezoidal contour is exact")
    print("  for a single enclosed pole at any radius, because the integrand is")
    print("  analytic on the contour and the rule is spectrally accurate.")

    section("4. Real integrals by residues, verified by real quadrature")
    checks = []
    checks.append((
        "int 1/(1+x^2) dx",
        lambda x: 1.0 / (1.0 + x * x),
        math.pi, quad_sinh(lambda x: 1.0 / (1.0 + x * x)),
    ))
    checks.append((
        "int 1/(x^2+4) dx",
        lambda x: 1.0 / (x * x + 4.0),
        math.pi / 2.0, quad_sinh(lambda x: 1.0 / (x * x + 4.0)),
    ))
    checks.append((
        "int 1/(1+x^2)^2 dx",
        lambda x: 1.0 / (1.0 + x * x) ** 2,
        math.pi / 2.0, quad_sinh(lambda x: 1.0 / (1.0 + x * x) ** 2),
    ))
    checks.append((
        "int 1/(x^4+1) dx",
        lambda x: 1.0 / (x ** 4 + 1.0),
        math.pi / math.sqrt(2.0), quad_sinh(lambda x: 1.0 / (x ** 4 + 1.0)),
    ))
    checks.append((
        "int (x^2+1)/(x^4+1) dx",
        lambda x: (x * x + 1.0) / (x ** 4 + 1.0),
        math.pi * math.sqrt(2.0), quad_sinh(lambda x: (x * x + 1.0) / (x ** 4 + 1.0)),
    ))
    checks.append((
        "int_0^inf 1/(1+x^2)^2 dx",
        lambda x: 1.0 / (1.0 + x * x) ** 2,
        math.pi / 4.0, quad_sinh(lambda x: 1.0 / (1.0 + x * x) ** 2) / 2.0,
    ))
    print(f"  {'integral':>30} {'closed form':>16} {'quadrature':>18}"
          f" {'difference':>10}")
    for label, _f, closed, numeric in checks:
        print(f"  {label:>30} {closed:>16.10f} {numeric:>18.12f}"
              f" {abs(closed - numeric):>10.2e}")

    section("5. Oscillatory integrals: the Green function of the 2-D Laplace equation")
    a = 0.8
    print(f"  int cos(omega x)/(x^2+a^2) dx = (pi/a) exp(-a|omega|) for a = {a}")
    print(f"  {'omega':>7} {'quadrature':>18} {'closed form':>18} {'difference':>11}")
    for omega in (0.5, 1.5, 3.0):
        closed = (math.pi / a) * math.exp(-a * abs(omega))
        numeric = 2.0 * quad_cos(lambda x: 1.0 / (x * x + a * a), omega)
        print(f"  {omega:>7.1f} {numeric:>18.12f} {closed:>18.12f}"
              f" {abs(numeric - closed):>11.2e}")
    print("  Poles at z = +i a and z = -i a; only +i a lies in the upper half")
    print("  plane, and for omega > 0 the arc in the upper half plane is")
    print("  exponentially small because exp(i omega z) decays there.  That is")
    print("  the whole reason the sign of omega selects a contour.")

    section("6. Dirichlet integral and the Cauchy principal value")
    direct = quad_sin_over_x()
    print(f"  int_0^inf sin(x)/x dx = {direct:.12f}; pi/2 ="
          f" {math.pi / 2:.12f}; difference {abs(direct - math.pi / 2):.2e}")
    print("  A bare truncation at L leaves an oscillatory tail of order 1/L;")
    print("  the two-term correction used here reaches 1e-11, and the contour")
    print("  route gives the limit exactly.  That is the practical reason")
    print("  residues are worth the algebra.")
    print("  Cauchy principal value of int 1/(x(1+x^2)) dx over the whole line:")
    eps = 1e-6
    left = simpson(lambda x: 1.0 / (x * (1.0 + x * x)), -50.0, -eps, 200001)
    right = simpson(lambda x: 1.0 / (x * (1.0 + x * x)), eps, 50.0, 200001)
    print(f"    P.V. numeric, punctured at +-{eps:g}, truncated at +-50:"
          f" {left + right:+.12f}")
    print("    The integrand is odd, so the principal value is exactly zero:")
    print("    puncturing symmetrically is precisely what the P.V. means.")

    section("7. Cauchy integral formula, checked on a circle")
    for label, func, z0, radius, note in [
        ("f(z) = exp(z), z0 = 1", cmath.exp, 1 + 0j, 3.0,
         "int e^z/(z-1) dz = 2 pi i e"),
        ("f(z) = z^2, z0 = i", lambda z: z * z, 1j, 2.0,
         "int z^2/(z-i) dz = 2 pi i * (-1)"),
        ("f(z) = cos(z), z0 = pi/2", cmath.cos, math.pi / 2, 2.0,
         "int cos z/(z-pi/2) dz = 2 pi i * cos(pi/2) = 0"),
    ]:
        num = contour_integral(lambda z: func(z) / (z - z0), z0, radius)
        closed = 2j * math.pi * func(z0)
        print(f"  {label:>28}: {note}")
        print(f"      numeric {num.real:>14.9f}{num.imag:>+14.9f}i   closed"
              f" {closed.real:>14.9f}{closed.imag:>+14.9f}i   error"
              f" {abs(num - closed):.2e}")


if __name__ == "__main__":
    main()
