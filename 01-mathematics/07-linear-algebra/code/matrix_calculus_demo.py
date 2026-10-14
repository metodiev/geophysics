"""Matrix calculus: gradients, Jacobians, sensitivities and Gauss-Newton.

Run:  python3 matrix_calculus_demo.py
Requires: Python standard library only.

Companion to lesson 01-07-10.

Every derivative identity in the lesson is checked here against a central
finite difference, because the point of matrix calculus is to be able to *write*
down the derivative without making a mistake in the index bookkeeping. Section 6
then uses one of those derivatives -- the travel-time sensitivity -- to invert a
two-parameter problem in five Gauss-Newton steps.
"""

import math

Matrix = list[list[float]]
Vector = list[float]


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def matvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(a[i]))) for i in range(len(a))]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(x):
    return math.sqrt(sum(v * v for v in x))


def grad_fd(f, x, h=1e-6):
    """Central-difference gradient of a scalar function of a vector."""
    g = []
    for i in range(len(x)):
        xp = list(x)
        xm = list(x)
        xp[i] += h
        xm[i] -= h
        g.append((f(xp) - f(xm)) / (2.0 * h))
    return g


def jacobian_fd(f, x, h=1e-6):
    """Central-difference Jacobian of a vector function of a vector."""
    base = f(x)
    rows = len(base)
    cols = len(x)
    jac = [[0.0] * cols for _ in range(rows)]
    for j in range(cols):
        xp = list(x)
        xm = list(x)
        xp[j] += h
        xm[j] -= h
        fp = f(xp)
        fm = f(xm)
        for i in range(rows):
            jac[i][j] = (fp[i] - fm[i]) / (2.0 * h)
    return jac


def max_abs_diff(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def transpose(a):
    return [list(row) for row in zip(*a)]


def jacobi_eigen(a, tol=1e-15, sweeps=100):
    n = len(a)
    work = [[float(x) for x in row] for row in a]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(sweeps):
        off = math.sqrt(sum(work[i][j] ** 2 for i in range(n)
                            for j in range(n) if i != j))
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(work[p][q]) < 1e-300:
                    continue
                theta = (work[q][q] - work[p][p]) / (2.0 * work[p][q])
                t = 1.0 if theta == 0.0 else \
                    math.copysign(1.0, theta) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k in range(n):
                    akp, akq = work[k][p], work[k][q]
                    work[k][p] = c * akp - s * akq
                    work[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = work[p][k], work[q][k]
                    work[p][k] = c * apk - s * aqk
                    work[q][k] = s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = v[k][p], v[k][q]
                    v[k][p] = c * vkp - s * vkq
                    v[k][q] = s * vkp + c * vkq
    return [work[i][i] for i in range(n)], v


def main() -> None:
    section("1. Scalar-valued derivatives, verified against finite differences")
    a = [1.5, -2.0, 0.5]
    x0 = [0.3, -0.7, 1.1]
    f_linear = lambda x: dot(a, x)
    g_analytic = a
    g_numeric = grad_fd(f_linear, x0)
    print(f"  f(x) = a^T x with a = {a}")
    print(f"    analytic d f / d x = {g_analytic}")
    print(f"    numerical          = {[round(v, 9) for v in g_numeric]}")
    print(f"    max error = {max(abs(g_analytic[i] - g_numeric[i]) for i in range(3)):.3e}")

    amat = [[2.0, 1.0, 0.0], [-1.0, 3.0, 0.5], [0.0, 0.5, 1.0]]
    f_quad = lambda x: dot(x, matvec(amat, x))
    g_quad_analytic = [matvec(amat, x0)[i] + sum(amat[j][i] * x0[j] for j in range(3))
                       for i in range(3)]
    g_quad_numeric = grad_fd(f_quad, x0)
    print(f"\n  f(x) = x^T A x with A = {amat}")
    print(f"    analytic d f / d x = (A + A^T) x = {[round(v, 9) for v in g_quad_analytic]}")
    print(f"    numerical                        = {[round(v, 9) for v in g_quad_numeric]}")
    print(f"    max error = {max(abs(g_quad_analytic[i] - g_quad_numeric[i]) for i in range(3)):.3e}")
    print("  For a symmetric A this simplifies to 2 A x, which is why the")
    print("  gradient of an energy functional is twice the matrix times the vector.")

    g_design = [[1.0, 0.0], [1.0, 1.0], [1.0, 2.0], [1.0, 3.0]]
    d_obs = [0.5, -2.5, -5.5, -8.5]

    def misfit(m):
        return 0.5 * sum((matvec(g_design, m)[i] - d_obs[i]) ** 2 for i in range(4))

    m0 = [1.0, -2.0]
    residual0 = [matvec(g_design, m0)[i] - d_obs[i] for i in range(4)]
    g_analytic2 = matvec(transpose(g_design), residual0)
    g_numeric2 = grad_fd(misfit, m0)
    print(f"\n  phi(m) = 0.5 ||G m - d||^2 with G the 4x2 design matrix")
    print(f"    residual G m - d = {residual0}")
    print(f"    analytic grad phi = G^T (G m - d) = {[round(v, 9) for v in g_analytic2]}")
    print(f"    numerical                         = {[round(v, 9) for v in g_numeric2]}")
    print(f"    max error = "
          f"{max(abs(g_analytic2[i] - g_numeric2[i]) for i in range(2)):.3e}")
    print("  Setting this gradient to zero gives the normal equations of")
    print("  lesson 01-07-07, G^T G m = G^T d. The normal equations are not a")
    print("  separate fact to memorise; they are the stationarity condition of")
    print("  this quadratic.")

    section("2. Jacobians: the derivative of a vector function")
    jac_analytic = g_design
    jac_numeric = jacobian_fd(lambda m: matvec(g_design, m), m0)
    print(f"    d(G m)/d m = G, and the numerical Jacobian agrees to")
    print(f"    {max_abs_diff(jac_analytic, jac_numeric):.3e}")

    # A nonlinear model: the two-way travel time to a horizontal reflector.
    def travel_times(params):
        h, v = params
        return [math.sqrt(x * x + 4.0 * h * h) / v for x in (0.0, 1.0, 2.0, 3.0)]

    params0 = [1.2, 3.7]
    jac_num = jacobian_fd(travel_times, params0)
    jac_an = []
    for x in (0.0, 1.0, 2.0, 3.0):
        h, v = params0
        root = math.sqrt(x * x + 4.0 * h * h)
        jac_an.append([4.0 * h / (v * root), -root / v ** 2])
    print(f"\n  T(x; h, v) = sqrt(x^2 + 4h^2) / v, parameterised by (h, v)")
    print(f"  at (h, v) = {params0}, offsets x = 0, 1, 2, 3 km:")
    print(f"    {'x (km)':>8}  {'dT/dh':>14}  {'dT/dv':>14}")
    for i, x in enumerate((0.0, 1.0, 2.0, 3.0)):
        print(f"    {x:>8.1f}  {jac_an[i][0]:>14.9f}  {jac_an[i][1]:>14.9f}")
    print(f"    analytic rows of the Jacobian = "
          f"{[[round(v, 9) for v in row] for row in jac_an]}")
    print(f"    numerical rows                = "
          f"{[[round(v, 9) for v in row] for row in jac_num]}")
    print(f"    max error = {max_abs_diff(jac_an, jac_num):.3e}")
    print("\n  At zero offset T = 2h/v, so dT/dh = 2/v = 0.5405 s/km and")
    print("  dT/dv = -2h/v^2 = -0.1753 s per (km/s). Moving to larger offset")
    print("  lengthens the ray, so the travel time becomes more sensitive to")
    print("  velocity and less to depth: by x = 3 km the depth sensitivity has")
    print("  fallen by about 38 % and the velocity sensitivity has risen by")
    print("  about 60 %. That asymmetry is the kernel structure behind the")
    print("  depth-velocity trade-off, and the offsets you record decide which of")
    print("  the two the experiment can resolve -- the singular vectors of lesson")
    print("  01-07-08 applied to two competing parameters.")

    section("3. The derivative of an eigenvalue")
    def sym_matrix(p):
        return [[2.0 + p, 1.0, 0.0],
                [1.0, 3.0 - p, 0.0],
                [0.0, 0.0, 1.0 + 0.5 * p]]

    def largest_eigenvalue(p):
        vals, _ = jacobi_eigen(sym_matrix(p))
        return max(vals)

    p0 = 0.4
    vals, vecs = jacobi_eigen(sym_matrix(p0))
    index = max(range(3), key=lambda i: vals[i])
    v_vec = [vecs[r][index] for r in range(3)]
    dA = [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 0.5]]
    analytic = dot(v_vec, matvec(dA, v_vec))
    numeric = (largest_eigenvalue(p0 + 1e-6) - largest_eigenvalue(p0 - 1e-6)) / 2e-6
    print(f"  A(p) = [[2+p, 1, 0], [1, 3-p, 0], [0, 0, 1+p/2]], evaluated at p = {p0}")
    print(f"  eigenvalues = {[round(v, 9) for v in sorted(vals, reverse=True)]}")
    print(f"  largest eigenvalue = {vals[index]:.9f}, eigenvector = "
          f"{[round(v, 9) for v in v_vec]}")
    print(f"  analytic  d lambda / d p = v^T (dA/dp) v = {analytic:.10f}")
    print(f"  numerical d lambda / d p                = {numeric:.10f}")
    print(f"  difference = {abs(analytic - numeric):.3e}")
    print("\n  This is the perturbation formula used everywhere in normal-mode")
    print("  seismology and in stability analysis: the sensitivity of a natural")
    print("  frequency to a parameter is the mode's energy in the part of the")
    print("  operator that the parameter changes. No eigenvector derivative is")
    print("  needed, which is why the formula is usable on large problems.")

    section("4. Gauss-Newton: one Jacobian per iteration, quadratic convergence")
    x_offsets = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0]
    h_true, v_true = 1.0, 4.0
    d_true = [math.sqrt(x * x + 4.0 * h_true ** 2) / v_true for x in x_offsets]
    print(f"  true model (h, v) = ({h_true}, {v_true}) km, km/s")
    print(f"  observed travel times (s) = {[round(v, 8) for v in d_true]}")
    params = [1.5, 3.0]
    print(f"\n  {'iteration':>10}  {'h':>14}  {'v':>14}  {'||residual||':>14}  "
          f"{'||error||':>12}  {'error/prev^2':>14}")
    previous_error = None
    for it in range(1, 8):
        h, v = params
        jac = []
        predicted = []
        for x in x_offsets:
            root = math.sqrt(x * x + 4.0 * h * h)
            predicted.append(root / v)
            jac.append([4.0 * h / (v * root), -root / v ** 2])
        residual = [d_true[i] - predicted[i] for i in range(len(x_offsets))]
        # normal equations for the 2x2 Gauss-Newton step
        jtj = [[sum(jac[k][i] * jac[k][j] for k in range(len(x_offsets))) for j in range(2)]
               for i in range(2)]
        jtr = [sum(jac[k][i] * residual[k] for k in range(len(x_offsets))) for i in range(2)]
        det = jtj[0][0] * jtj[1][1] - jtj[0][1] * jtj[1][0]
        step = [(jtj[1][1] * jtr[0] - jtj[0][1] * jtr[1]) / det,
                (-jtj[1][0] * jtr[0] + jtj[0][0] * jtr[1]) / det]
        params = [params[0] + step[0], params[1] + step[1]]
        error = math.hypot(params[0] - h_true, params[1] - v_true)
        ratio = "-" if previous_error is None else f"{error / previous_error ** 2:.6f}"
        print(f"  {it:>10}  {params[0]:>14.10f}  {params[1]:>14.10f}  "
              f"{norm(residual):>14.3e}  {error:>12.3e}  {ratio:>14}")
        previous_error = error
        if error < 1e-12:
            break
    print("\n  The last column is error_k+1 / error_k^2, and it converges to a")
    print("  constant near 0.26. That constant is the signature of quadratic")
    print("  convergence: the number of correct digits doubles each iteration, and")
    print("  the second-order term of the residual expansion, not the computer,")
    print("  is what sets the constant. Iteration stops automatically once the")
    print("  error reaches round-off; further steps would only amplify nothing.")
    print("  The mechanism is the one that gave Newton's method in lesson")
    print("  01-05-07, and it is the reason Gauss-Newton is the default engine of")
    print("  geophysical inversion -- see ../../18-inverse-problems/README.md.")

    section("5. Why the adjoint matters: counting linear solves")
    for nd, nm in ((10 ** 3, 10 ** 4), (10 ** 4, 10 ** 5), (10 ** 5, 10 ** 6)):
        explicit = nd
        adjoint = 2
        print(f"  {nd:.0e} data and {nm:.0e} model parameters:")
        print(f"    explicit Jacobian: {explicit:.0e} linear solves of size {nm:.0e}"
              f"  -> about {explicit * nm:.1e} operations")
        print(f"    adjoint gradient : {adjoint} linear solves of size {nm:.0e}"
              f"  -> about {adjoint * nm:.1e} operations")
        print(f"    saving factor    : {explicit / adjoint:.1e}")
    print("\n  The adjoint identity is d/dp [ <something, F(m)> ] = <F^T(something), dm/dp>,")
    print("  read right to left: instead of differentiating the model-to-data map")
    print("  once per datum, differentiate the *scalar objective* once. It is the")
    print("  same fact as (Ax)^T y = x^T (A^T y) -- the defining property of the")
    print("  transpose, which is why a library only needs a matrix-vector product")
    print("  and a transposed matrix-vector product to run a full gradient-based")
    print("  inversion.")
    print("  These are operation counts, not measured timings; the point is the")
    print("  ratio, and it is why no production code forms an explicit Jacobian.")


if __name__ == "__main__":
    main()
