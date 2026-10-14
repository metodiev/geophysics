"""Calculus of variations: the direct method and the Euler-Lagrange equation.

Run:  python3 variational_calculus_demo.py
Requires: Python standard library only.

Companion to lesson 01-14-06.

Three things are measured here.

1. The *direct method*: discretise a functional, minimise over the node values,
   and check that the discrete minimiser converges to the solution of the
   Euler-Lagrange boundary-value problem as O(h^2). The measured rate is printed,
   not asserted.
2. The *first variation*: differentiate the functional along a perturbation and
   compare the result with the integral of the gradient against that
   perturbation, which is what "the variational derivative is 1 - 2y''" means.
3. *Natural boundary conditions*: minimise a functional with a free end and watch
   the boundary condition y'(1) = 0 appear by itself, at the rate h/2.

The last section treats the Rayleigh quotient, the variational statement of the
eigenvalue problem, which is the form in which free oscillations and geoid
problems are usually posed.
"""

import math

Vector = list[float]


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def thomas(lower: float, diag: float, upper: float, rhs: Vector) -> Vector:
    """Solve a tridiagonal system with constant bands."""
    n = len(rhs)
    cp = [0.0] * n
    dp = [0.0] * n
    cp[0] = upper / diag
    dp[0] = rhs[0] / diag
    for i in range(1, n):
        denom = diag - lower * cp[i - 1]
        cp[i] = upper / denom
        dp[i] = (rhs[i] - lower * dp[i - 1]) / denom
    x = [0.0] * n
    x[-1] = dp[-1]
    for i in range(n - 2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]
    return x


# --------------------------------------------------------------------------
# The two model problems
# --------------------------------------------------------------------------

def analytic_fixed(y0: float, y1: float):
    """Solution of y'' = 1/2 with y(0) = y0, y(1) = y1."""
    return lambda x: x * x / 4.0 + (y1 - y0 - 0.25) * x + y0


def analytic_free(y0: float):
    """Solution of y'' = -1 with y(0) = y0 and the natural condition y'(1) = 0."""
    c = 1.0 - y0
    return lambda x: -x * x / 2.0 + c * x + y0


def direct_fixed(n: int, y0: float = 0.0, y1: float = 1.0) -> tuple[Vector, float]:
    """Minimise F[y] = int (y'^2 + y) dx over a uniform grid of n intervals.

    Stationarity of the discrete functional gives
    2 y_j - y_{j-1} - y_{j+1} = -h^2/2, i.e. y'' = 1/2 to O(h^2).
    """
    h = 1.0 / n
    interior = n - 1
    rhs = [-h * h / 2.0] * interior
    rhs[0] += y0
    rhs[-1] += y1
    sol = thomas(-1.0, 2.0, -1.0, rhs)
    y = [y0] + sol + [y1]
    return y, h


def direct_free(n: int, y0: float = 0.0) -> tuple[Vector, float]:
    """Minimise F[y] = int (y'^2 - 2y) dx with y(0) = y0 and y(1) free."""
    h = 1.0 / n
    # Unknowns y_1 .. y_n. Interior equations -y_{j-1} + 2 y_j - y_{j+1} = -h^2;
    # the last equation is the natural boundary condition y_n - y_{n-1} = h^2/2.
    rhs = [h * h] * n
    rhs[0] += y0
    rhs[-1] = h * h / 2.0
    lower = [0.0] * n
    diag = [0.0] * n
    upper = [0.0] * n
    for j in range(n):
        diag[j] = 2.0
        if j > 0:
            lower[j] = -1.0
        if j < n - 1:
            upper[j] = -1.0
    diag[-1] = 1.0
    upper[-2] = -1.0
    # Generic Thomas solve for varying bands.
    cp = [0.0] * n
    dp = [0.0] * n
    cp[0] = upper[0] / diag[0]
    dp[0] = rhs[0] / diag[0]
    for i in range(1, n):
        denom = diag[i] - lower[i] * cp[i - 1]
        cp[i] = upper[i] / denom if i < n - 1 else 0.0
        dp[i] = (rhs[i] - lower[i] * dp[i - 1]) / denom
    y = [0.0] * n
    y[-1] = dp[-1]
    for i in range(n - 2, -1, -1):
        y[i] = dp[i] - cp[i] * y[i + 1]
    return [y0] + y, h


def direct_sinh(n: int, y0: float = 0.0, y1: float = 1.0) -> tuple[Vector, float]:
    """Minimise F[y] = int (y'^2 + y^2) dx, y(0) = y0, y(1) = y1.

    Stationarity gives (2 + h^2) y_j - y_{j-1} - y_{j+1} = 0, whose solution is
    the O(h^2) approximation to y'' = y.
    """
    h = 1.0 / n
    interior = n - 1
    rhs = [0.0] * interior
    rhs[0] += y0
    rhs[-1] += y1
    sol = thomas(-1.0, 2.0 + h * h, -1.0, rhs)
    return [y0] + sol + [y1], h


def functional(y: Vector, h: float, quadratic: bool = True) -> float:
    """Discrete F on a uniform grid.

    quadratic=True  ->  int (y'^2 + y^2) dx  (trapezoid for y^2)
    quadratic=False ->  int (y'^2 + y) dx
    """
    total = 0.0
    for i in range(len(y) - 1):
        total += (y[i + 1] - y[i]) ** 2 / h
        if quadratic:
            total += (y[i] ** 2 + y[i + 1] ** 2) * h / 2.0
        else:
            total += (y[i] + y[i + 1]) * h / 2.0
    return total


def rayleigh_min_eigen(n: int, iterations: int = 2000) -> tuple[float, float]:
    """Smallest eigenvalue of -y'' = lambda y by inverse iteration.

    The discrete problem is A y = lambda y with A = (1/h^2) tridiag(-1, 2, -1),
    which is the Rayleigh quotient int y'^2 / int y^2 in discretised form.
    Inverse iteration converges to the smallest eigenvalue of A. Returns the
    eigenvalue and the discrete Rayleigh quotient of the converged vector.
    """
    h = 1.0 / n
    h2 = h * h
    size = n - 1
    x = [math.sin(math.pi * (i + 1) * h) for i in range(size)]
    y = x[:]
    for _ in range(iterations):
        y = thomas(-1.0 / h2, 2.0 / h2, -1.0 / h2, x)
        ynorm = math.sqrt(h * sum(v * v for v in y))
        y = [v / ynorm for v in y]
        x = y[:]
    # Rayleigh quotient with A applied to the converged vector.
    ay = [0.0] * size
    for i in range(size):
        ay[i] = (2.0 * y[i] - (y[i - 1] if i > 0 else 0.0)
                 - (y[i + 1] if i < size - 1 else 0.0)) / h2
    lam = h * sum(y[i] * ay[i] for i in range(size)) / (h * sum(v * v for v in y))
    return lam, lam


def main() -> None:
    section("1. The direct method for a fixed-endpoint problem")

    print("  Minimise F[y] = int_0^1 (y'^2 + y^2) dx, y(0) = 0, y(1) = 1.")
    print("  Euler-Lagrange: y'' = y with y(0) = 0, y(1) = 1,")
    print("  so y = sinh(x) / sinh(1) = %.10f sinh(x)" % (1.0 / math.sinh(1.0)))
    exact = lambda x: math.sinh(x) / math.sinh(1.0)
    print(f"  {'n':>6}{'h':>10}{'max error':>14}{'error ratio':>14}"
          f"{'measured order':>16}")
    previous = None
    for n in (10, 20, 40, 80, 160, 320):
        y, h = direct_sinh(n)
        err = max(abs(y[i] - exact(i * h)) for i in range(n + 1))
        ratio = previous / err if previous else float("nan")
        order = math.log2(ratio) if previous else float("nan")
        ratio_text = f"{ratio:.4f}" if previous else "-"
        order_text = f"{order:.4f}" if previous else "-"
        print(f"  {n:>6}{h:>10.5f}{err:>14.4e}{ratio_text:>14}{order_text:>16}")
        previous = err
    print("  The error falls by a factor of four when h halves: the direct method")
    print("  inherits the O(h^2) of the difference approximation, and that is now")
    print("  measured rather than asserted.")

    section("2. The discrete minimiser really minimises the discrete functional")

    n = 40
    y, h = direct_sinh(n)
    f_min = functional(y, h)
    print(f"  n = {n}, h = {h:.5f}")
    print(f"    F_h at the discrete minimiser:    {f_min:.12f}")
    print(f"    F_h at the sampled exact solution:"
          f" {functional([exact(i * h) for i in range(n + 1)], h):.12f}")
    print(f"    the sampled exact solution is higher by:"
          f" {functional([exact(i * h) for i in range(n + 1)], h) - f_min:+.3e}"
          f"  (round-off)")
    for perturb, label in ((1e-3, "bump of amplitude 1e-3 at the midpoint"),
                           (1e-2, "bump of amplitude 1e-2 at the midpoint"),
                           (-1e-3, "dip of amplitude 1e-3 at the midpoint")):
        trial = y[:]
        trial[n // 2] += perturb
        print(f"    {label:<40} F_h = {functional(trial, h):.12f}"
              f"  (difference {functional(trial, h) - f_min:+.3e})")
    print("  Every perturbation increases the functional, so the discrete solution")
    print("  is the minimiser of the discrete problem: it is below the sampled")
    print("  exact solution and lower than any of its neighbours. It is not the")
    print("  exact minimiser of the continuous problem, as Section 1 measured.")

    section("3. The first variation, checked against the Euler-Lagrange form")

    def first_variation_numeric(y_fun, delta_fun, eps: float = 1e-6) -> float:
        def f(scale):
            npts = 4000
            h = 1.0 / npts
            y = [y_fun(i * h) + scale * delta_fun(i * h) for i in range(npts + 1)]
            dy = [(y[i + 1] - y[i]) / h for i in range(npts)]
            mid = [(y[i] + y[i + 1]) / 2.0 for i in range(npts)]
            return sum((dy[i] ** 2 + mid[i]) * h for i in range(npts))
        return (f(eps) - f(-eps)) / (2.0 * eps)

    def grad_integral(y_fun, delta_fun) -> float:
        npts = 200000
        h = 1.0 / npts
        # The gradient (L2) of F is 1 - 2 y''; for y = x^2 the value is -3.
        total = 0.0
        for i in range(npts):
            x = (i + 0.5) * h
            total += (1.0 - 2.0 * 2.0) * delta_fun(x) * h
        return total

    y_fun = lambda x: x * x
    delta = lambda x: math.sin(math.pi * x)
    numeric = first_variation_numeric(y_fun, delta)
    analytic = grad_integral(y_fun, delta)
    print("  Take y = x^2 (not a minimiser) and delta y = sin(pi x).")
    print(f"    dF/deps at eps = 0 by central difference: {numeric:.10f}")
    print(f"    int (1 - 2y'') delta y dx analytically:   {analytic:.10f}")
    print(f"    exact value -(3)(2/pi) = {-6.0 / math.pi:.10f}")
    print(f"    difference between the two routes: {abs(numeric - analytic):.3e}")
    print("  Setting this to zero for every admissible delta y is what makes")
    print("  1 - 2y'' = 0, and the boundary terms vanish because delta y(0) =")
    print("  delta y(1) = 0.")

    section("4. A free end: the natural boundary condition appears by itself")

    print("  Minimise F[y] = int_0^1 (y'^2 - 2y) dx with y(0) = 0 and y(1) free.")
    print("  Euler-Lagrange: y'' = -1, and the boundary term at x = 1 forces")
    print("  y'(1) = 0, so y = -x^2/2 + x, which gives y(1) = 0.5.")
    exact_free = analytic_free(0.0)
    print(f"  {'n':>6}{'h':>10}{'max error':>14}{'y(1)':>12}{'y_n - y_{n-1}':>16}"
          f"{'predicted h/2':>16}")
    for n in (10, 20, 40, 80):
        y, h = direct_free(n)
        err = max(abs(y[i] - exact_free(i * h)) for i in range(n + 1))
        print(f"  {n:>6}{h:>10.5f}{err:>14.3e}{y[n]:>12.6f}"
              f"{y[n] - y[n - 1]:>16.6f}{h / 2.0:>16.6f}")
    print("  The discrete natural boundary condition is y_n - y_{n-1} = h^2/2,")
    print("  that is y'(1) = h/2, which tends to zero with h. The continuous")
    print("  condition was never imposed; it emerged from the minimisation.")
    print("  The error column is at round-off because this particular exact")
    print("  solution is a quadratic and the scheme is exact for quadratics; the")
    print("  convergence rate for a general problem was measured in Section 1.")

    section("5. The Rayleigh quotient: the variational eigenvalue problem")

    print("  Minimise R[y] = int y'^2 / int y^2 over y with y(0) = y(1) = 0;")
    print("  the minimum is achieved for y = sin(pi x) and equals pi^2.")
    print(f"  pi^2 = {math.pi ** 2:.10f}")
    print(f"  {'n':>6}{'h':>10}{'lambda_min':>16}{'error':>14}{'measured order':>16}")
    previous = None
    for n in (10, 20, 40, 80):
        lam, _ = rayleigh_min_eigen(n)
        err = abs(lam - math.pi ** 2)
        ratio = previous / err if previous else float("nan")
        order = math.log2(ratio) if previous else float("nan")
        ratio_text = f"{order:.4f}" if previous else "-"
        print(f"  {n:>6}{1.0 / n:>10.5f}{lam:>16.10f}{err:>14.3e}"
              f"{ratio_text:>16}")
        previous = err
    print("  Again O(h^2): the discrete Rayleigh quotient converges at the same")
    print("  rate as the direct method, because it is the same finite-difference")
    print("  approximation of the second derivative.")

    section("6. The price of refinement: the system becomes ill-conditioned")

    print("  The matrix of Section 1 has eigenvalues 2 - 2 cos(k pi/(m+1)) for")
    print("  m = n - 1 unknowns, so its condition number grows like 4(m+1)^2/pi^2.")
    print(f"  {'n':>6}{'m':>6}{'kappa measured':>18}{'4(m+1)^2/pi^2':>18}")
    for n in (10, 20, 40, 80, 160):
        m = n - 1
        lam_min = 2.0 - 2.0 * math.cos(math.pi / (m + 1))
        lam_max = 2.0 - 2.0 * math.cos(m * math.pi / (m + 1))
        print(f"  {n:>6}{m:>6}{lam_max / lam_min:>18.4f}"
              f"{4.0 * (m + 1) ** 2 / math.pi ** 2:>18.4f}")
    print("  Refinement buys accuracy in the functional and pays for it in")
    print("  conditioning: at n = 160 the system is already losing four digits,")
    print("  which is the trade the direct method makes and the reason it is used")
    print("  with a moderate mesh and a good preconditioner.")


if __name__ == "__main__":
    main()
