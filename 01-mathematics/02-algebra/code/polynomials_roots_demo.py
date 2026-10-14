"""Polynomials, roots and asymptotic behaviour.

Run:  python3 polynomials_roots_demo.py
Requires: Python standard library only.

Companion to lesson 01-02-04. Roots are located three ways -- closed form,
bisection and Newton -- so that the convergence behaviour of each can be seen
rather than asserted.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def horner(coeffs: list[float], x: float) -> float:
    """Evaluate a polynomial given highest-degree coefficient first."""
    result = 0.0
    for c in coeffs:
        result = result * x + c
    return result


def horner_derivative(coeffs: list[float], x: float) -> float:
    """Evaluate p'(x) by synthetic division; coeffs highest degree first."""
    n = len(coeffs) - 1
    result = coeffs[0] * n
    for i in range(1, n):
        result = result * x + coeffs[i] * (n - i)
    return result


def bisection(f, a: float, b: float, tol: float = 1.0e-14) -> tuple[float, int]:
    fa = f(a)
    steps = 0
    while (b - a) / 2.0 > tol and steps < 200:
        mid = (a + b) / 2.0
        fm = f(mid)
        if fa * fm <= 0.0:
            b = mid
        else:
            a, fa = mid, fm
        steps += 1
    return (a + b) / 2.0, steps


def newton(f, df, x0: float, tol: float = 1.0e-15, max_iter: int = 60):
    """Newton's method, returning the iterate history for error inspection."""
    history = [x0]
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if fx == 0.0:
            break
        x = x - fx / df(x)
        history.append(x)
        if abs(history[-1] - history[-2]) < tol:
            break
    return history


def main() -> None:
    section("1. Horner's rule: fewer operations and more accuracy")
    coeffs = [1.0, -6.0, 11.0, -6.0]        # (x-1)(x-2)(x-3)
    x = 2.0000000001
    naive = x ** 3 - 6.0 * x ** 2 + 11.0 * x - 6.0
    nested = horner(coeffs, x)
    print(f"p(x) = x**3 - 6x**2 + 11x - 6 = (x-1)(x-2)(x-3)")
    print(f"at x = {x}: naive sum = {naive:.12e}, Horner = {nested:.12e}")
    print(f"difference = {abs(naive - nested):.3e}  (Horner uses 3 multiplications")
    print("and 3 additions; the naive form evaluates two powers as well)")
    for probe in (-1.0, 0.0, 1.0, 2.0, 3.0, 4.0):
        print(f"  p({probe:>4.1f}) = {horner(coeffs, probe):>10.4f}")

    section("2. Closed-form quadratic roots and the stable form")
    a, b, c = 1.0, -3.0, 2.0               # roots 1 and 2
    disc = math.sqrt(b * b - 4 * a * c)
    r1, r2 = (-b + disc) / (2 * a), (-b - disc) / (2 * a)
    print(f"{a}x**2 + {b}x + {c} = 0 -> discriminant = {disc}, "
          f"roots = {r1}, {r2}")
    print("Both roots are integers here, so no cancellation is visible; the")
    print("cancellation appears when the two roots differ by many orders of")
    print("magnitude (lesson 01-01-04, section 5).")

    section("3. Root finding when no formula exists: x**3 - x - 2 = 0")
    f = lambda x: x ** 3 - x - 2.0
    df = lambda x: 3.0 * x ** 2 - 1.0
    root_bis, steps_bis = bisection(f, 1.0, 2.0)
    print(f"bisection on [1, 2]: root = {root_bis:.15f} after {steps_bis} steps")
    history = newton(f, df, 1.5)
    print(f"Newton from x0 = 1.5: root = {history[-1]:.15f} after "
          f"{len(history) - 1} steps")
    print(f"check: f(root) = {f(history[-1]):.3e}, f'(root) = {df(history[-1]):.6f}")
    print("analytic check: the root satisfies x**3 = x + 2, so")
    print(f"  root**3 - root = {history[-1] ** 3 - history[-1]:.15f} (= 2)")
    print(f"\nNewton error history (quadratic convergence at a simple root):")
    errors = [abs(h - history[-1]) for h in history[:-1]]
    print(f"{'step':>4} {'x_n':>22} {'|e_n|':>12} {'|e_n| / |e_(n-1)|**2':>22}")
    for i, (h, e) in enumerate(zip(history[:-1], errors)):
        ratio = "" if i == 0 else f"{e / errors[i - 1] ** 2:>22.4f}"
        print(f"{i:>4} {h:>22.15f} {e:>12.3e} {ratio}")
    print("The last column stabilises near a constant: each step roughly squares")
    print("the number of correct digits, which is what 'quadratic' means.")

    section("4. A repeated root destroys Newton's speed")
    g = lambda x: (x - 2.0) ** 2 * (x + 1.0)
    dg = lambda x: 3.0 * (x - 2.0) * x
    hist_double = newton(g, dg, 3.0)
    print(f"g(x) = (x-2)**2 (x+1): root 2 has multiplicity 2")
    print(f"{'step':>4} {'x_n':>20} {'|e_n|':>12} {'ratio |e_n|/|e_(n-1)|':>24}")
    errs = [abs(h - 2.0) for h in hist_double[:-1]]
    for i, (h, e) in enumerate(zip(hist_double[:11], errs[:11])):
        ratio = "" if i == 0 else f"{e / errs[i - 1]:>24.6f}"
        print(f"{i:>4} {h:>20.12f} {e:>12.3e} {ratio}")
    print(f"  (iteration stopped after {len(hist_double) - 1} steps)")
    print("Here the ratio settles at about 0.5, i.e. linear convergence: one")
    print("binary digit per step instead of a doubling of digits.")

    section("5. Root sensitivity: a tiny coefficient change moves a root")
    # Roots 1, 2, 3; perturb the x**2 coefficient by a small relative amount.
    eps = 1.0e-6
    base_coeffs = [1.0, -6.0, 11.0, -6.0]
    pert_coeffs = [1.0, -6.0 + eps, 11.0, -6.0]
    root_base = newton(lambda x: horner(base_coeffs, x),
                       lambda x: horner_derivative(base_coeffs, x), 1.9)[-1]
    root_pert = newton(lambda x: horner(pert_coeffs, x),
                       lambda x: horner_derivative(pert_coeffs, x), 1.9)[-1]
    print(f"coefficient of x**2 changed from -6 to {-6 + eps}")
    print(f"root near 2: {root_base:.15f} -> {root_pert:.15f}")
    print(f"shift = {root_pert - root_base:.6e} for a coefficient change of {eps:.1e}")
    print(f"amplification = {(root_pert - root_base) / eps:.4f}")
    print("Roots separated by O(1) are only mildly sensitive; the amplification")
    print("grows without bound as roots coalesce (lesson 01-01-05).")

    section("6. Asymptotic behaviour: a rational model of a buried sphere")
    # g(z) = G M z / (z**2 + R**2)**(3/2)
    big_g, mass, radius = 6.674e-11, 1.0e12, 500.0
    g_at = lambda z: big_g * mass * z / (z * z + radius * radius) ** 1.5
    print(f"G = {big_g:.3e}, M = {mass:.3e} kg, R = {radius:.0f} m")
    print(f"{'z (m)':>8} {'g (mGal)':>14} {'g z**2 / (G M)':>16} "
          f"{'point-mass error':>18}")
    point_mass_limit = big_g * mass
    for z in (500.0, 1000.0, 2000.0, 5000.0, 10000.0):
        g = g_at(z)
        ratio = g * z * z / point_mass_limit
        print(f"{z:>8.0f} {g / 1.0e-5:>14.6f} {ratio:>16.6f} "
              f"{abs(1.0 - ratio):>18.6f}")
    print("For z >> R the ratio tends to 1 as R**2/z**2: the far-field anomaly")
    print("is the point-mass law, and the leading correction is the same shape")
    print("as the next term of a binomial expansion.")

    section("7. A truncated series is a polynomial: exp(-x) by Taylor terms")
    print(f"{'x':>6} {'exp(-x)':>14} {'1 - x + x2/2':>14} {'error':>12} "
          f"{'rel error':>11}")
    for x in (0.1, 0.5, 1.0, 2.0, 5.0):
        exact = math.exp(-x)
        degree2 = 1.0 - x + x * x / 2.0
        err = abs(degree2 - exact)
        print(f"{x:>6.1f} {exact:>14.9f} {degree2:>14.9f} {err:>12.3e} "
              f"{err / exact:>11.3e}")
    print("The quadratic truncation is excellent for x < 1 and useless at x = 5:")
    print("a Taylor polynomial is a local model with a finite useful range.")

    section("8. Refraction crossover distance solved for layer thickness")
    # x_c = 2 H sqrt((v2 + v1) / (v2 - v1)) for a two-layer medium.
    v1, v2, x_c = 1200.0, 3000.0, 60.0
    h_direct = x_c / 2.0 * math.sqrt((v2 - v1) / (v2 + v1))
    # The same answer by bisection on the residual, to show the method.
    residual = lambda h: x_c - 2.0 * h * math.sqrt((v2 + v1) / (v2 - v1))
    h_bis, steps = bisection(residual, 0.0, 100.0)
    print(f"v1 = {v1:.0f} m/s, v2 = {v2:.0f} m/s, crossover at x = {x_c:.0f} m")
    print(f"layer thickness from the closed form: H = {h_direct:.6f} m")
    print(f"layer thickness from bisection:       H = {h_bis:.6f} m "
          f"({steps} steps)")
    print(f"critical angle: sin(theta_c) = v1/v2 -> theta_c = "
          f"{math.degrees(math.asin(v1 / v2)):.4f} deg")


if __name__ == "__main__":
    main()
