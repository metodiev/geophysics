"""Constrained optimisation, Lagrange multipliers and KKT conditions.

Run:  python3 constrained_demo.py
Requires: Python standard library only.

Companion to lesson 01-14-03.

The Lagrange multiplier is treated here as a measurable sensitivity, not as a
symbol: the script differentiates the optimal value with respect to the
constraint and compares the result with the multiplier computed from the KKT
system. Box constraints are solved twice, once by projected gradient descent and
once by exhaustive active-set enumeration, and the two answers are compared. The
penalty method's constraint violation is measured as a function of the penalty
weight, so the text can quote a measured rate rather than an asserted one.
"""

import itertools
import math

Vector = list[float]
Matrix = list[list[float]]


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


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


# --------------------------------------------------------------------------
# A two-cell travel-time problem used throughout
# --------------------------------------------------------------------------

KERNEL = [[1.0, 0.4], [0.6, 1.0]]          # km, SYNTHETIC ray geometry
A = matmul(transpose(KERNEL), KERNEL)       # G^T G
B = matvec(transpose(KERNEL), [0.052, 0.061])   # G^T d, d in s


def misfit(m: Vector) -> float:
    """One half the squared residual of the two-cell problem."""
    r = sub(matvec(KERNEL, m), [0.052, 0.061])
    return 0.5 * dot(r, r)


def gradient(m: Vector) -> Vector:
    return sub(matvec(A, m), B)


# --------------------------------------------------------------------------
# A three-cell problem with a bound on every cell
# --------------------------------------------------------------------------

KERNEL3 = [[1.00, 1.00, 0.00],
           [0.50, 0.70, 1.00],
           [0.30, 0.00, 1.00]]
A3 = matmul(transpose(KERNEL3), KERNEL3)


def synthetic_data(model: Vector) -> Vector:
    """Exact data for a chosen model: no noise, so the truth is recoverable."""
    return matvec(KERNEL3, model)


def misfit3(m: Vector, d: Vector) -> float:
    r = sub(matvec(KERNEL3, m), d)
    return 0.5 * dot(r, r)


def gradient3(m: Vector, d: Vector) -> Vector:
    return matvec(transpose(KERNEL3), sub(matvec(KERNEL3, m), d))


def active_set_scan(b: Vector, d: Vector, lo: Vector, hi: Vector) -> tuple:
    """Exhaustive search over bound patterns for a three-parameter box problem.

    Returns the best KKT point, its pattern, and how many patterns yielded a
    KKT point, so that uniqueness is reported rather than assumed.
    """
    points = []
    for status in itertools.product("lfu", repeat=3):
        fixed = {i: (lo[i] if status[i] == "l" else hi[i])
                 for i in range(3) if status[i] != "f"}
        free = [i for i in range(3) if status[i] == "f"]
        if not free:
            m = [fixed[i] for i in range(3)]
        else:
            sub_a = [[A3[i][j] for j in free] for i in free]
            rhs = [b[i] - sum(A3[i][j] * fixed[j] for j in fixed) for i in free]
            sub_m = solve(sub_a, rhs)
            m = [fixed[i] if i in fixed else sub_m[free.index(i)]
                 for i in range(3)]
        g = gradient3(m, d)
        feasible = all(lo[i] - 1e-12 <= m[i] <= hi[i] + 1e-12 for i in range(3))
        kkt_ok = all((status[i] == "l" and g[i] >= -1e-9)
                     or (status[i] == "u" and g[i] <= 1e-9)
                     or (status[i] == "f" and abs(g[i]) < 1e-9)
                     for i in range(3))
        if feasible and kkt_ok:
            points.append((m, status))
    best = min(points, key=lambda p: misfit3(p[0], d))
    return best, len(points)


def kkt_solve(constraint: Matrix, rhs: Vector) -> tuple[Vector, Vector]:
    """Solve the equality-constrained quadratic problem via its KKT system."""
    k = len(constraint)
    n = len(A)
    system = [[0.0] * (n + k) for _ in range(n + k)]
    for i in range(n):
        for j in range(n):
            system[i][j] = A[i][j]
    for r in range(k):
        for i in range(n):
            system[i][n + r] = constraint[r][i]
            system[n + r][i] = constraint[r][i]
    sol = solve(system, list(B) + list(rhs))
    return sol[:n], sol[n:]


def main() -> None:
    section("1. The unconstrained problem and its constrained relative")

    m_unc = solve(A, B)
    print("  two-cell travel-time problem, G = [[1, 0.4], [0.6, 1]] km (SYNTHETIC)")
    print(f"    unconstrained minimiser  m = ({m_unc[0]:+.8f}, {m_unc[1]:+.8f}) s/km")
    print(f"    gradient there           {gradient(m_unc)}")
    print(f"    misfit                   {misfit(m_unc):.10f}")
    print("  Suppose the two cells must have equal slowness perturbation, because")
    print("  a well log ties the two depths together. Constraint: m1 - m2 = 0.")

    c = [[1.0, -1.0]]
    d = [0.0]
    m_con, lam = kkt_solve(c, d)
    print(f"    constrained minimiser    m = ({m_con[0]:+.8f}, {m_con[1]:+.8f})")
    print(f"    C m - d                  {dot(c[0], m_con) - d[0]:+.3e}  (feasible)")
    g_con = gradient(m_con)
    print(f"    gradient + C^T lambda    "
          f"({g_con[0] + c[0][0] * lam[0]:+.3e},"
          f" {g_con[1] + c[0][1] * lam[0]:+.3e})")
    print(f"    lambda                   {lam[0]:+.8f}")
    print(f"    misfit                   {misfit(m_con):.10f}"
          f"   (higher than unconstrained: {misfit(m_unc):.10f})")
    print(f"    difference               {misfit(m_con) - misfit(m_unc):.10f}")

    section("2. The multiplier is the derivative of the optimal value")

    print("  phi*(d) = min over Cm = d. Theory: dphi*/dd = -lambda.")
    print(f"  {'eps':>10}{'central difference':>22}{'-lambda':>16}")
    for eps in (1e-2, 1e-3, 1e-4):
        plus, _ = kkt_solve(c, [d[0] + eps])
        minus, _ = kkt_solve(c, [d[0] - eps])
        fd = (misfit(plus) - misfit(minus)) / (2.0 * eps)
        print(f"  {eps:>10.0e}{fd:>22.10f}{-lam[0]:>16.10f}")
    print("  The multiplier therefore has units of misfit per unit of constraint:")
    print("  it prices the constraint in the currency of the objective.")

    section("3. Inequality constraints and complementarity")

    cases = [("target (2, -1): constraint inactive", 2.0),
             ("target (-3, -1): constraint active", -3.0)]
    print("  minimise 0.5(m1 - t1)^2 + 0.5(m2 + 1)^2 subject to m1 >= 0")
    print(f"  {'case':<38}{'m1':>12}{'m2':>10}{'lambda':>12}"
          f"{'lambda*(-m1)':>14}")
    for label, t1 in cases:
        if t1 >= 0.0:                     # unconstrained point is feasible
            m1, lam_val = t1, 0.0
        else:                             # constraint is active
            m1, lam_val = 0.0, -t1
        print(f"  {label:<38}{m1:>12.6f}{-1.0:>10.6f}{lam_val:>12.6f}"
              f"{lam_val * (-m1):>14.3e}")
    print("  In the first case the constraint is inactive and lambda = 0; in the")
    print("  second it is active, lambda = 3 > 0, and the complementarity product")
    print("  lambda * g(m*) is zero in both. Those three facts plus stationarity")
    print("  are the KKT conditions.")

    section("4. Box constraints: projected gradient versus active-set search")

    lo3 = [0.0, 0.0, 0.0]
    hi3 = [0.03, 0.03, 0.03]
    m_true = [0.050, 0.005, 0.022]
    d3 = synthetic_data(m_true)
    b3 = matvec(transpose(KERNEL3), d3)
    m_unc3 = solve(A3, b3)
    print("  three-cell cross-hole problem, SYNTHETIC data built from a known")
    print("  model so the unconstrained answer is exact and interpretable:")
    print("    true model (s/km):          "
          + ", ".join(f"{v:+.6f}" for v in m_true))
    print("    unconstrained model (s/km): "
          + ", ".join(f"{v:+.6f}" for v in m_unc3))
    print(f"    misfit at the unconstrained model: {misfit3(m_unc3, d3):.3e}")
    print("    bounds 0.00 <= m_i <= 0.03 s/km put cell 1 outside the box")

    m = [0.0, 0.0, 0.0]
    alpha = 1.0 / max(sum(abs(v) for v in row) for row in A3)
    for _ in range(20000):
        m = [min(hi3[i], max(lo3[i], m[i] - alpha * gradient3(m, d3)[i]))
             for i in range(3)]
    step_norm = norm([min(hi3[i], max(lo3[i], m[i] - alpha * gradient3(m, d3)[i])) - m[i]
                      for i in range(3)])
    print(f"    projected gradient: alpha = 1/L = {alpha:.6f}, 20000 iterations,")
    print(f"      last step norm = {step_norm:.3e} (converged)")
    print("      model (s/km):             "
          + ", ".join(f"{v:+.8f}" for v in m))
    print("      status: " + ", ".join(
        (f"m{i + 1} at lower bound" if abs(m[i] - lo3[i]) < 1e-10 else
         f"m{i + 1} at upper bound" if abs(m[i] - hi3[i]) < 1e-10 else
         f"m{i + 1} free")
        for i in range(3)))
    print(f"      misfit = {misfit3(m, d3):.10e}")

    best, n_kkt = active_set_scan(b3, d3, lo3, hi3)
    print(f"    exhaustive active-set scan over all 27 bound patterns:")
    print(f"      patterns that satisfy feasibility and the KKT sign"
          f" conditions: {n_kkt}")
    print("      best KKT point (s/km):    "
          + ", ".join(f"{v:+.8f}" for v in best[0]))
    print(f"      pattern {best[1]} (l = at lower bound, f = free, u = at upper"
          f" bound), misfit = {misfit3(best[0], d3):.10e}")
    print(f"      max difference from projected gradient:"
          f" {max(abs(best[0][i] - m[i]) for i in range(3)):.3e}")

    section("5. Physically inadmissible models and what the bound buys")

    m_phys = [0.040, -0.010, 0.020]
    d4 = synthetic_data(m_phys)
    m_unc4 = solve(A3, matvec(transpose(KERNEL3), d4))
    print("  data built from a model whose second cell has a negative slowness")
    print("  perturbation (SYNTHETIC: nothing physical, only the arithmetic):")
    print("    data d (s):                 "
          + ", ".join(f"{v:.4f}" for v in d4))
    print("    unconstrained model (s/km): "
          + ", ".join(f"{v:+.6f}" for v in m_unc4))
    print("    cells that are physically inadmissible (m_i < 0): "
          + str([i + 1 for i, v in enumerate(m_unc4) if v < 0]))

    lo4, hi4 = [0.0, 0.0, 0.0], [0.05, 0.05, 0.05]
    best4, n_kkt4 = active_set_scan(matvec(transpose(KERNEL3), d4), d4, lo4, hi4)
    print("    bounded model (s/km):       "
          + ", ".join(f"{v:+.6f}" for v in best4[0]))
    print(f"    misfit: unconstrained {misfit3(m_unc4, d4):.3e},"
          f" bounded {misfit3(best4[0], d4):.3e},"
          f" increase {misfit3(best4[0], d4) - misfit3(m_unc4, d4):.3e}")
    print("    The bound is not free: forcing cell 2 to zero costs misfit. What it")
    print("    buys is a model that does not claim an impossible velocity.")

    section("6. The penalty method: measured violation versus weight")

    c_eq = [1.0, 1.0, 0.0]
    d_eq = 0.02
    print("  minimise 0.5||Gm - d||^2 + (mu/2)(m1 + m2 - 0.02)^2")
    print(f"  {'mu':>10}{'m1':>12}{'m2':>12}{'m3':>12}{'violation':>14}"
          f"{'misfit':>16}")
    prev = None
    for mu in (1.0, 10.0, 100.0, 1000.0, 10000.0, 100000.0):
        system = [[A3[i][j] + mu * c_eq[i] * c_eq[j] for j in range(3)]
                  for i in range(3)]
        rhs = [b3[i] + mu * c_eq[i] * d_eq for i in range(3)]
        m = solve(system, rhs)
        violation = abs(dot(c_eq, m) - d_eq)
        print(f"  {mu:>10.0f}{m[0]:>12.6f}{m[1]:>12.6f}{m[2]:>12.6f}"
              f"{violation:>14.3e}{misfit3(m, d3):>16.10f}")
        if prev is not None:
            print(f"            violation ratio when mu is multiplied by ten:"
                  f" {prev / violation:.3f}")
        prev = violation
    print("  Each factor of ten in mu divides the violation by roughly ten: the")
    print("  penalty method converges, but only as 1/mu, so the constraint is")
    print("  satisfied exactly only in the limit of an infinite weight.")

    section("7. Duality: the multiplier solves a problem too")

    def dual_value(lam_trial: float) -> float:
        """q(lambda) = min_m [ phi(m) + lambda (C m - d) ]."""
        m = solve(A, [B[0] - lam_trial * c[0][0], B[1] - lam_trial * c[0][1]])
        return misfit(m) + lam_trial * (dot(c[0], m) - d[0])

    lo_l, hi_l = -0.005, 0.005
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    a_l, b_l = lo_l, hi_l
    c_l, d_l = b_l - gr * (b_l - a_l), a_l + gr * (b_l - a_l)
    f_c, f_d = dual_value(c_l), dual_value(d_l)
    for _ in range(120):
        if f_c > f_d:
            b_l, d_l, f_d = d_l, c_l, f_c
            c_l = b_l - gr * (b_l - a_l)
            f_c = dual_value(c_l)
        else:
            a_l, c_l, f_c = c_l, d_l, f_d
            d_l = a_l + gr * (b_l - a_l)
            f_d = dual_value(d_l)
    lam_dual = 0.5 * (a_l + b_l)
    print("  equality-constrained quadratic problem, dual function")
    print("  q(lambda) = min_m [ phi(m) + lambda (C m - d) ] on C = [1, -1]")
    print(f"    golden-section maximum of q: lambda = {lam_dual:+.10f},"
          f" q = {dual_value(lam_dual):.10f}")
    print(f"    KKT solution:                lambda = {lam[0]:+.10f},"
          f" phi* = {misfit(m_con):.10f}")
    print(f"    agreement in lambda: {abs(lam_dual - lam[0]):.3e}")
    print("  The multiplier is the argmax of a dual problem, and any admissible")
    print("  lambda gives a lower bound on the constrained optimum.")


if __name__ == "__main__":
    main()
