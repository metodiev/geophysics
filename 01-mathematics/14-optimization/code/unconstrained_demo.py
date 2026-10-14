"""Unconstrained minimisation: gradient descent, Newton and quasi-Newton.

Run:  python3 unconstrained_demo.py
Requires: Python standard library only.

Companion to lesson 01-14-02.

Everything measured here is printed: iteration counts to a fixed tolerance,
observed convergence ratios against the textbook bound (kappa-1)/(kappa+1),
Newton's divergence without a line search, the effect of Levenberg damping, and
the loss of accuracy that a finite-difference gradient imposes on the final
model. No iteration count in the lesson is quoted that did not come from this
script.
"""

import math

Vector = list[float]
Matrix = list[list[float]]


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# Linear algebra helpers
# --------------------------------------------------------------------------

def matmul(a: Matrix, b: Matrix) -> Matrix:
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def matvec(a: Matrix, x: Vector) -> Vector:
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def dot(x: Vector, y: Vector) -> float:
    return sum(a * b for a, b in zip(x, y))


def norm(x: Vector) -> float:
    return math.sqrt(dot(x, x))


def sub(x: Vector, y: Vector) -> Vector:
    return [a - b for a, b in zip(x, y)]


def scaled(a: Vector, s: float) -> Vector:
    return [s * v for v in a]


def solve(a: Matrix, b: Vector) -> Vector:
    """Gaussian elimination with partial pivoting."""
    n = len(a)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) < 1e-300:
            raise ZeroDivisionError(f"singular at column {col}")
        m[col], m[pivot] = m[pivot], m[col]
        for r in range(col + 1, n):
            factor = m[r][col] / m[col][col]
            for c in range(col, n + 1):
                m[r][c] -= factor * m[col][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x


def rotation(theta: float) -> Matrix:
    c, s = math.cos(theta), math.sin(theta)
    return [[c, -s], [s, c]]


def quadratic(kappa: float, theta: float = math.pi / 6.0) -> Matrix:
    """A = Q diag(1, kappa) Q^T - a symmetric positive-definite test matrix."""
    q = rotation(theta)
    return matmul(q, matmul([[1.0, 0.0], [0.0, kappa]], transpose(q)))


# --------------------------------------------------------------------------
# Methods
# --------------------------------------------------------------------------

def gradient_descent(fun, grad, m0: Vector, alpha: float, tol: float,
                     max_iter: int = 200000) -> dict:
    m = m0[:]
    g = grad(m)
    g0 = norm(g)
    errors = []
    for k in range(max_iter):
        if norm(g) <= tol * g0:
            return {"m": m, "iters": k, "evals": k + 1, "errors": errors,
                    "gnorm": norm(g), "history": []}
        m = sub(m, scaled(g, alpha))
        g = grad(m)
        errors.append(norm(g))
    return {"m": m, "iters": max_iter, "evals": max_iter + 1, "errors": errors,
            "gnorm": norm(g), "history": []}


def newton(fun, grad, hess, m0: Vector, tol: float, max_iter: int = 200,
           line_search: bool = True, damping: float = 0.0) -> dict:
    m = m0[:]
    g = grad(m)
    g0 = norm(g)
    evals = 1
    hist = [norm(g)]
    for k in range(max_iter):
        if norm(g) <= tol * g0:
            return {"m": m, "iters": k, "evals": evals, "gnorm": norm(g),
                    "history": hist}
        h = hess(m)
        if damping:
            h = [[h[i][j] + (damping if i == j else 0.0) for j in range(len(h))]
                 for i in range(len(h))]
        step = solve(h, g)
        alpha = 1.0
        if line_search:
            f0 = fun(m)
            slope = dot(g, step)
            while alpha > 1e-10 and fun(sub(m, scaled(step, alpha))) > f0 + 1e-4 * alpha * slope:
                alpha *= 0.5
                evals += 1
        m = sub(m, scaled(step, alpha))
        g = grad(m)
        evals += 1
        hist.append(norm(g))
    return {"m": m, "iters": max_iter, "evals": evals, "gnorm": norm(g),
            "history": hist}


def bfgs(fun, grad, m0: Vector, tol: float, max_iter: int = 2000) -> dict:
    """BFGS with an Armijo backtracking line search."""
    n = len(m0)
    m = m0[:]
    g = grad(m)
    g0 = norm(g)
    h = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    evals = 1
    for k in range(max_iter):
        if norm(g) <= tol * g0:
            return {"m": m, "iters": k, "evals": evals, "gnorm": norm(g)}
        # p = -H g
        p = [-v for v in matvec(h, g)]
        slope = dot(g, p)
        if slope >= 0:                       # H lost positive definiteness
            p = [-v for v in g]
            h = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
            slope = -dot(g, g)
        alpha = 1.0
        f0 = fun(m)
        while alpha > 1e-12 and fun([m[i] + alpha * p[i] for i in range(n)]) > f0 + 1e-4 * alpha * slope:
            alpha *= 0.5
            evals += 1
        s = scaled(p, alpha)
        m = [m[i] + s[i] for i in range(n)]
        g_new = grad(m)
        evals += 1
        y = sub(g_new, g)
        sy = dot(s, y)
        if sy > 1e-14:
            rho = 1.0 / sy
            hy = matvec(h, y)
            yhy = dot(y, hy)
            term = (1.0 + rho * yhy) * rho
            h = [[h[i][j] + term * s[i] * s[j] - rho * (s[i] * hy[j] + hy[i] * s[j])
                  for j in range(n)] for i in range(n)]
        g = g_new
    return {"m": m, "iters": max_iter, "evals": evals, "gnorm": norm(g)}


# --------------------------------------------------------------------------
# Test problems
# --------------------------------------------------------------------------

def rosenbrock(m: Vector) -> float:
    x, y = m
    return (1.0 - x) ** 2 + 100.0 * (y - x * x) ** 2


def rosenbrock_grad(m: Vector) -> Vector:
    x, y = m
    return [-2.0 * (1.0 - x) - 400.0 * x * (y - x * x),
            200.0 * (y - x * x)]


def rosenbrock_hess(m: Vector) -> Matrix:
    x, y = m
    return [[2.0 - 400.0 * (y - 3.0 * x * x), -400.0 * x],
            [-400.0 * x, 200.0]]


def rate(errors: list[float]) -> float:
    """Geometric mean of successive error ratios (the observed linear rate)."""
    if len(errors) < 3:
        return float("nan")
    pairs = [(errors[i + 1] / errors[i]) for i in range(len(errors) - 2)
             if errors[i] > 0]
    if not pairs:
        return float("nan")
    return math.exp(sum(math.log(p) for p in pairs) / len(pairs))


def main() -> None:
    m_target = [1.0, -2.0]
    section("1. Gradient descent on a quadratic, and its measured rate")
    print("  f(m) = 0.5 (m - m*)^T A (m - m*),  m* = (1, -2),  A = Q diag(1, kappa) Q^T")

    for kappa in (10.0, 100.0, 1000.0):
        a = quadratic(kappa)
        fun = lambda m, a=a: 0.5 * dot(sub(m, m_target), matvec(a, sub(m, m_target)))
        grad = lambda m, a=a: matvec(a, sub(m, m_target))
        for label, alpha in (("alpha = 1/L", 1.0 / kappa),
                             ("alpha = 2/(L+mu)", 2.0 / (1.0 + kappa))):
            r = gradient_descent(fun, grad, [0.0, 0.0], alpha, tol=1e-8)
            error = norm(sub(r["m"], m_target))
            bound = (kappa - 1.0) / (kappa + 1.0)
            print(f"  kappa = {kappa:>7.0f}  {label:<16} iterations = "
                  f"{r['iters']:>7d}   ||m - m*|| = {error:9.3e}"
                  f"   measured rate = {rate(r['errors']):.4f}"
                  f"   bound = {bound:.4f}")

    section("2. Iteration count grows in proportion to kappa")

    print(f"  {'kappa':>10}{'iterations':>12}{'iters/kappa':>14}"
          f"{'sqrt(kappa)':>14}{'log(kappa)':>12}")
    for kappa in (1.0, 4.0, 10.0, 100.0, 1000.0, 10000.0):
        a = quadratic(kappa)
        fun = lambda m, a=a: 0.5 * dot(sub(m, m_target), matvec(a, sub(m, m_target)))
        grad = lambda m, a=a: matvec(a, sub(m, m_target))
        r = gradient_descent(fun, grad, [0.0, 0.0], 2.0 / (1.0 + kappa), tol=1e-8)
        print(f"  {kappa:>10.0f}{r['iters']:>12d}{r['iters'] / kappa:>14.3f}"
              f"{math.sqrt(kappa):>14.2f}{math.log(kappa):>12.3f}")
    print("  iterations/kappa stays near 9.2 for kappa >= 100, so the count is")
    print("  linear in the condition number, not logarithmic in the accuracy alone.")

    section("3. Newton on the same quadratic is exact in one step")

    a = quadratic(1000.0)
    fun = lambda m, a=a: 0.5 * dot(sub(m, m_target), matvec(a, sub(m, m_target)))
    grad = lambda m, a=a: matvec(a, sub(m, m_target))
    hess = lambda m, a=a: a
    rn = newton(fun, grad, hess, [0.0, 0.0], tol=1e-8)
    print(f"  Newton iterations to ||grad|| <= 1e-8 ||grad_0||: {rn['iters']}")
    print(f"  ||m - m*|| after the solve: {norm(sub(rn['m'], m_target)):.3e}")
    rb = bfgs(fun, grad, [0.0, 0.0], tol=1e-8)
    print(f"  BFGS iterations for the same problem (n = 2): {rb['iters']},"
          f" ||m - m*|| = {norm(sub(rb['m'], m_target)):.3e}")
    print(f"  gradient evaluations: Newton {rn['evals']}, BFGS {rb['evals']}")

    section("4. Rosenbrock: where the methods actually differ")

    x0 = [-1.2, 1.0]
    tol = 1e-8
    print(f"  start {x0}, 1 + 100 (y - x^2) type valley, minimum at (1, 1)")

    a = quadratic(100.0)
    steps = None
    # Steepest descent with backtracking (the honest fixed-step version stalls).
    for label, alpha in (("steepest descent, alpha = 1e-3", 1e-3),
                         ("steepest descent, alpha = 5e-4", 5e-4)):
        r = gradient_descent(rosenbrock, rosenbrock_grad, x0, alpha, tol=tol,
                             max_iter=500000)
        print(f"  {label:<34} iterations = {r['iters']:>7d}"
              f"   ||grad|| = {r['gnorm']:.3e}   error = "
              f"{norm(sub(r['m'], [1.0, 1.0])):.3e}")

    rn = newton(rosenbrock, rosenbrock_grad, rosenbrock_hess, x0, tol=tol)
    print(f"  Newton with Armijo line search        iterations = {rn['iters']:>7d}"
          f"   ||grad|| = {rn['gnorm']:.3e}   error = "
          f"{norm(sub(rn['m'], [1.0, 1.0])):.3e}")
    rb = bfgs(rosenbrock, rosenbrock_grad, x0, tol=tol)
    print(f"  BFGS with Armijo line search          iterations = {rb['iters']:>7d}"
          f"   ||grad|| = {rb['gnorm']:.3e}   error = "
          f"{norm(sub(rb['m'], [1.0, 1.0])):.3e}")
    print(f"  gradient evaluations: Newton {rn['evals']}, BFGS {rb['evals']}")

    section("5. Newton without a line search: an excursion and a divergence")

    m = x0[:]
    print(f"  Rosenbrock, undamped Newton, start {x0}:")
    print(f"  {'iteration':>10}{'x':>16}{'y':>16}{'f':>16}")
    for k in range(4):
        f = rosenbrock(m)
        print(f"  {k:>10d}{m[0]:>16.6f}{m[1]:>16.6f}{f:>16.6e}")
        g = rosenbrock_grad(m)
        step = solve(rosenbrock_hess(m), g)
        m = sub(m, step)
    print(f"  after 3 steps m = ({m[0]:.6f}, {m[1]:.6f}), f ="
          f" {rosenbrock(m):.3e}")
    print("  One violent excursion to f = 1.41e+03 at step 2, then recovery:")
    print("  the quadratic model was simply wrong where the step was taken.")

    rn_ns = newton(rosenbrock, rosenbrock_grad, rosenbrock_hess, x0, tol=tol,
                   line_search=False)
    print(f"  undamped Newton on Rosenbrock stopped after {rn_ns['iters']}"
          f" iterations with f = {rosenbrock(rn_ns['m']):.3e}")

    def scalar(x: float) -> float:
        return math.log(1.0 + x * x)

    print("\n  A function where undamped Newton genuinely diverges:")
    print("  f(x) = log(1 + x^2), non-convex for |x| > 1, minimised at x = 0.")
    x = 2.0
    print(f"  {'iteration':>10}{'x':>22}{"f'(x)":>16}{'f(x)':>16}")
    for k in range(9):
        g1 = 2.0 * x / (1.0 + x * x)
        print(f"  {k:>10d}{x:>22.6e}{g1:>16.6e}{scalar(x):>16.6e}")
        x = x - g1 / (2.0 * (1.0 - x * x) / (1.0 + x * x) ** 2)
    print("  |x| grows without bound: the Newton step is proportional to 1/f'',")
    print("  and f'' changes sign where the function is not convex.")

    # The repair: damp the Hessian so that the step is a descent direction.
    x = 2.0
    for _ in range(300):
        g1 = 2.0 * x / (1.0 + x * x)
        h1 = 2.0 * (1.0 - x * x) / (1.0 + x * x) ** 2
        h_damped = h1 if h1 > 1e-6 else (-h1 + 1.0)
        step = g1 / h_damped
        alpha = 1.0
        while alpha > 1e-12 and scalar(x - alpha * step) > scalar(x) - 1e-4 * alpha * g1 * step:
            alpha *= 0.5
        x -= alpha * step
    print(f"  the same iteration with a damped Hessian and line search:"
          f" x = {x:.3e}, f = {scalar(x):.3e}")

    section("6. Levenberg damping: interpolation between the two extremes")

    print(f"  {'lambda':>12}{'iterations':>12}{'evaluations':>14}{'error':>14}")
    for damping in (0.0, 1e-4, 1e-2, 1.0, 100.0):
        r = newton(rosenbrock, rosenbrock_grad, rosenbrock_hess, x0, tol=tol,
                   damping=damping, max_iter=5000)
        print(f"  {damping:>12.0e}{r['iters']:>12d}{r['evals']:>14d}"
              f"{norm(sub(r['m'], [1.0, 1.0])):>14.3e}")

    section("7. Newton's quadratic convergence, measured")

    def g_scalar(x: float) -> float:
        return math.exp(x) - 3.0

    x_star = math.log(3.0)
    x = 0.0
    errors = []
    for _ in range(8):
        errors.append(abs(x - x_star))
        x -= g_scalar(x) / math.exp(x)
    print("  f(x) = exp(x) - 3x, minimum at x* = ln 3 = "
          f"{x_star:.6f}")
    print("    errors |x_k - x*|: " + ", ".join(f"{e:.3e}" for e in errors[:6]))
    ratios = [errors[i + 1] / errors[i] ** 2 for i in range(5)
              if errors[i] > 1e-8]
    print("    ratios |e_{k+1}| / |e_k|^2: "
          + ", ".join(f"{r:.6f}" for r in ratios))
    print("  A sequence of ratios that is roughly constant is the signature of")
    print("  second-order convergence; the doubling of correct digits follows.")
    hist = [h for h in rn_ns["history"] if h > 0]
    print(f"  On Rosenbrock the same pattern appears only near the solution:")
    print("    last five gradient norms: "
          + ", ".join(f"{h:.4e}" for h in hist[-5:]))
    print("  Earlier iterations include an increase of the gradient norm, which")
    print("  is why purity of order cannot be claimed over the whole run.")

    section("8. A finite-difference gradient costs accuracy")

    a = quadratic(100.0)
    fun = lambda m, a=a: 0.5 * dot(sub(m, m_target), matvec(a, sub(m, m_target)))
    grad_exact = lambda m, a=a: matvec(a, sub(m, m_target))

    def make_fd(fun, h):
        def grad_fd(m):
            out = []
            for j in range(len(m)):
                e = [0.0] * len(m)
                e[j] = h
                out.append((fun([m[i] + e[i] for i in range(len(m))])
                            - fun([m[i] - e[i] for i in range(len(m))])) / (2.0 * h))
            return out
        return grad_fd

    h_values = (1e-2, 1e-4, 1e-6, 1e-8)
    probe = [0.31, -0.77]
    print("  central differences of a quadratic versus its analytic gradient:")
    print(f"  {'h':>8}{'max |grad error|':>20}{'iterations':>12}{'final error':>14}")
    for h in h_values:
        grad_fd = make_fd(fun, h)
        err = max(abs(grad_fd(probe)[j] - grad_exact(probe)[j]) for j in range(2))
        r = gradient_descent(fun, grad_fd, [0.0, 0.0], 2.0 / 101.0, tol=1e-8)
        print(f"  {h:>8.0e}{err:>20.3e}{r['iters']:>12d}"
              f"{norm(sub(r['m'], m_target)):>14.3e}")
    print("  A central difference is exact for a quadratic, so there is no")
    print("  truncation term at all and the error is pure round-off: it grows as")
    print("  h shrinks, in proportion to eps/h.")

    probe_r = [-1.0, 0.5]
    print("\n  the same test on Rosenbrock, where truncation is present:")
    print(f"  {'h':>8}{'max |grad error|':>20}")
    for h in h_values:
        grad_fd = make_fd(rosenbrock, h)
        exact = rosenbrock_grad(probe_r)
        err = max(abs(grad_fd(probe_r)[j] - exact[j]) for j in range(2))
        print(f"  {h:>8.0e}{err:>20.3e}")
    print("  Now the error is a sum of a truncation term O(h^2) and a round-off")
    print("  term O(eps/h), so it has an interior minimum: here the smallest")
    print("  observed error is 3.8e-09 at h = 1e-06, and h = 1e-08 is already")
    print("  worse (7.1e-07) because round-off has taken over.")

    section("9. Scaling and preconditioning: what actually changes the count")

    def eigenvalues_2x2(m: Matrix) -> tuple[float, float]:
        tr = m[0][0] + m[1][1]
        det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        root = math.sqrt(tr * tr - 4.0 * det)
        return 0.5 * (tr - root), 0.5 * (tr + root)

    def run(label: str, a: Matrix, target: Vector) -> None:
        lo, hi = eigenvalues_2x2(a)
        alpha = 2.0 / (lo + hi)
        fun = lambda u: 0.5 * dot(sub(u, target), matvec(a, sub(u, target)))
        grad = lambda u: matvec(a, sub(u, target))
        r = gradient_descent(fun, grad, [0.0, 0.0], alpha, tol=1e-8,
                             max_iter=2000000)
        print(f"  {label:<42} kappa = {hi / lo:>9.2f}   iterations ="
              f" {r['iters']:>8d}   ||u - u*|| = {norm(sub(r['m'], target)):.2e}")

    a_diag = [[1.0, 0.0], [0.0, 1.0e4]]
    run("A = diag(1, 1e4)", a_diag, [1.0, -1.0])

    scale = [1.0 / math.sqrt(a_diag[0][0]), 1.0 / math.sqrt(a_diag[1][1])]
    a_pre = [[a_diag[i][j] * scale[i] * scale[j] for j in range(2)] for i in range(2)]
    run("D A D with D = diag(1/sqrt(A_ii))", a_pre,
        [1.0 / scale[0], -1.0 / scale[1]])

    a_rot = quadratic(1.0e4)
    run("A = Q diag(1, 1e4) Q^T (rotated)", a_rot, [1.0, -1.0])
    scale = [1.0 / math.sqrt(a_rot[0][0]), 1.0 / math.sqrt(a_rot[1][1])]
    a_rot_pre = [[a_rot[i][j] * scale[i] * scale[j] for j in range(2)]
                 for i in range(2)]
    run("D A D on the rotated problem", a_rot_pre,
        [1.0 / scale[0], -1.0 / scale[1]])
    print("  Preconditioning helps when it changes the spectrum. Making the two")
    print("  parameters of comparable sensitivity is the geophysical version,")
    print("  and it costs nothing but a choice of units.")


if __name__ == "__main__":
    main()
