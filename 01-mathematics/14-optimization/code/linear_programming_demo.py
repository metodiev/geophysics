"""Linear programming: an exact simplex, L1 and Chebyshev fitting.

Run:  python3 linear_programming_demo.py
Requires: Python standard library only.

Companion to lesson 01-14-07.

All linear programs here are solved in exact rational arithmetic with a
two-phase simplex, so the answers are certificates rather than approximations:
the optimal objective values are exact rationals, the duality gap is exactly
zero, and the reduced costs are exact. That matters for the lesson because the
claims being made are about *optimality*, and an optimality claim from a
floating-point interior point solver with a 1e-8 tolerance is a weaker statement.

The geophysical content is the fitting of a straight trend to data containing a
blunder, in the L1, L2 and L-infinity norms, and a small blending (mixing)
problem whose dual variables are the marginal costs of the specifications.
"""

import math
import random
from fractions import Fraction

Vector = list[Fraction]


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def fmt(value: Fraction | float) -> str:
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return str(value.numerator)
        return f"{float(value):.8f}"
    return f"{value:.8f}"


# --------------------------------------------------------------------------
# Two-phase simplex in exact rational arithmetic
# --------------------------------------------------------------------------

def solve_lp(c, a, b):
    """Minimise c^T x subject to A x <= b and x >= 0, in exact rational arithmetic.

    A two-phase simplex with Bland's rule (guaranteed to terminate, at the cost
    of extra iterations). Returns (x, objective, iterations, status). Every
    number in the tableau is a Fraction, so "optimal" is a statement about the
    arithmetic rather than about a tolerance.
    """
    m, n = len(a), len(c)
    need = [i for i in range(m) if Fraction(b[i]) < 0]
    total = n + m + len(need)
    art_col = {i: n + m + k for k, i in enumerate(need)}
    rows, basis = [], []
    for i in range(m):
        row = [Fraction(0)] * (total + 1)
        rhs, sign = Fraction(b[i]), 1
        if rhs < 0:
            sign, rhs = -1, -rhs
        for j in range(n):
            row[j] = sign * Fraction(a[i][j])
        if sign == 1:
            row[n + i] = Fraction(1)
            basis.append(n + i)
        else:
            row[n + i] = Fraction(-1)
            row[art_col[i]] = Fraction(1)
            basis.append(art_col[i])
        row[total] = rhs
        rows.append(row)
    artificials = set(art_col.values())

    def reduced_costs(cost):
        r = [Fraction(v) for v in cost]
        for i, var in enumerate(basis):
            if r[var] != 0:
                factor = r[var]
                r = [r[j] - factor * rows[i][j] for j in range(len(r))]
        return r

    def pivot(row_index, col):
        pivot_value = rows[row_index][col]
        rows[row_index] = [v / pivot_value for v in rows[row_index]]
        for i in range(len(rows)):
            if i != row_index and rows[i][col] != 0:
                factor = rows[i][col]
                rows[i] = [rows[i][j] - factor * rows[row_index][j]
                           for j in range(len(rows[i]))]
        basis[row_index] = col

    def optimise(cost, allowed):
        iterations = 0
        while True:
            r = reduced_costs(cost)
            entering = next((j for j in allowed if r[j] < 0), None)
            if entering is None:
                z = sum(cost[basis[i]] * rows[i][-1] for i in range(len(basis)))
                return z, iterations
            leaving, best_ratio = None, None
            for i in range(len(basis)):
                if rows[i][entering] > 0:
                    ratio = rows[i][-1] / rows[i][entering]
                    if best_ratio is None or ratio < best_ratio:
                        leaving, best_ratio = i, ratio
            if leaving is None:
                return None, iterations
            pivot(leaving, entering)
            iterations += 1

    # Phase 1: minimise the sum of the artificial variables.
    cost1 = [Fraction(0)] * (total + 1)
    for col in artificials:
        cost1[col] = Fraction(1)
    _, iters1 = optimise(cost1, list(range(total)))
    phase1 = sum(rows[i][-1] for i in range(len(basis)) if basis[i] in artificials)
    if phase1 != 0:
        return None, None, iters1, "infeasible"

    # Drive any basic artificial out; drop the row if it is redundant.
    keep = []
    for i in range(len(basis)):
        if basis[i] in artificials:
            moved = False
            for j in range(total):
                if j not in artificials and rows[i][j] != 0:
                    pivot(i, j)
                    moved = True
                    break
            if not moved:
                continue
        keep.append(i)
    rows = [rows[i] for i in keep]
    basis = [basis[i] for i in keep]

    # Phase 2: minimise the real objective over the real columns.
    cost2 = [Fraction(v) for v in c] + [Fraction(0)] * (total + 1 - n)
    allowed2 = [j for j in range(total) if j not in artificials]
    z, iters2 = optimise(cost2, allowed2)
    if z is None:
        return None, None, iters1 + iters2, "unbounded"
    x = [Fraction(0)] * n
    for i, var in enumerate(basis):
        if var < n:
            x[var] = rows[i][-1]
    return x, z, iters1 + iters2, "optimal"


def dual_lp(c, a, b):
    """Solve the dual of  min c^T x, A x <= b, x >= 0  and return its optimum.

    The dual is  min b^T y  subject to  -A^T y <= c  and  y >= 0, and strong
    duality says its optimal value is minus the primal optimal value.
    """
    m = len(a)
    at = [[-Fraction(a[i][j]) for i in range(m)] for j in range(len(c))]
    return solve_lp([Fraction(b[i]) for i in range(m)], at,
                    [Fraction(v) for v in c])


# --------------------------------------------------------------------------
# Problem data
# --------------------------------------------------------------------------

X = [Fraction(i) for i in range(5)]
Y_CLEAN = [Fraction(1), Fraction(2), Fraction(2), Fraction(4), Fraction("4.6")]
Y_OUTLIER = [Fraction(1), Fraction(2), Fraction(2), Fraction(4), Fraction(9)]


def l1_design(y):
    """Build the L1 regression LP: variables a+, a-, b+, b-, r+_i, r-_i."""
    n = len(y)
    idx = {"ap": 0, "am": 1, "bp": 2, "bm": 3}
    for i in range(n):
        idx[f"rp{i}"] = 4 + i
        idx[f"rm{i}"] = 4 + n + i
    nvar = 4 + 2 * n
    c = [Fraction(0)] * nvar
    for i in range(n):
        c[idx[f"rp{i}"]] = Fraction(1)
        c[idx[f"rm{i}"]] = Fraction(1)
    a_ub, b_ub = [], []
    for i in range(n):
        row = [Fraction(0)] * nvar
        row[idx["ap"]] = Fraction(1)
        row[idx["am"]] = Fraction(-1)
        row[idx["bp"]] = X[i]
        row[idx["bm"]] = -X[i]
        row[idx[f"rp{i}"]] = Fraction(-1)
        row[idx[f"rm{i}"]] = Fraction(1)
        a_ub.append(row)
        b_ub.append(y[i])
        a_ub.append([-v for v in row])
        b_ub.append(-y[i])
    return c, a_ub, b_ub, idx, nvar


def l1_fit(y, extra_rows=None, extra_rhs=None):
    c, a_ub, b_ub, idx, nvar = l1_design(y)
    if extra_rows:
        a_ub = a_ub + extra_rows
        b_ub = b_ub + extra_rhs
    x, obj, iters, status = solve_lp(c, a_ub, b_ub)
    if status != "optimal":
        raise RuntimeError(status)
    a = x[idx["ap"]] - x[idx["am"]]
    b = x[idx["bp"]] - x[idx["bm"]]
    return a, b, obj, iters, x, idx


def l1_problem(y):
    c, a_ub, b_ub, idx, nvar = l1_design(y)
    return c, a_ub, b_ub


def chebyshev_fit(y):
    """Minimise max_i |a + b x_i - y_i| as a linear program."""
    n = len(y)
    idx = {"t": 0, "ap": 1, "am": 2, "bp": 3, "bm": 4}
    c = [Fraction(0)] * 5
    c[idx["t"]] = Fraction(1)
    a_ub, b_ub = [], []
    for i in range(n):
        for sign in (1, -1):
            row = [Fraction(0)] * 5
            row[idx["t"]] = Fraction(-1)
            row[idx["ap"]] = Fraction(sign)
            row[idx["am"]] = Fraction(-sign)
            row[idx["bp"]] = sign * X[i]
            row[idx["bm"]] = -sign * X[i]
            a_ub.append(row)
            b_ub.append(sign * y[i])
    x, obj, iters, status = solve_lp(c, a_ub, b_ub)
    if status != "optimal":
        raise RuntimeError(status)
    return (x[idx["ap"]] - x[idx["am"]], x[idx["bp"]] - x[idx["bm"]], obj, iters)


def l2_fit(y):
    n = len(y)
    sx = sum(X)
    sxx = sum(v * v for v in X)
    sy = sum(y)
    sxy = sum(X[i] * y[i] for i in range(n))
    det = n * sxx - sx * sx
    return float((sxx * sy - sx * sxy) / det), float((n * sxy - sx * sy) / det)


def residuals(a, b, y):
    return [a + b * X[i] - y[i] for i in range(len(y))]


def main() -> None:
    section("1. A blending problem, solved exactly")

    print("  Rock-physics mixing: choose fractions x1, x2, x3 >= 0 of three end")
    print("  members to hit a target density and velocity exactly, at least cost.")
    print("  x1 + x2 + x3 = 1, rho.x = 2.6725 g/cm3, v.x = 5.24 km/s,")
    print("  costs 1, 3, 2 per unit fraction.")
    rows = [
        [Fraction(1), Fraction(1), Fraction(1)],
        [Fraction(-1), Fraction(-1), Fraction(-1)],
        [Fraction("2.6"), Fraction("2.7"), Fraction("2.75")],
        [Fraction("-2.6"), Fraction("-2.7"), Fraction("-2.75")],
        [Fraction("5.8"), Fraction("5.2"), Fraction("4.4")],
        [Fraction("-5.8"), Fraction("-5.2"), Fraction("-4.4")],
    ]
    rhs = [Fraction(1), Fraction(-1), Fraction("2.6725"),
           Fraction("-2.6725"), Fraction("5.24"), Fraction("-5.24")]
    x, obj, iters, status = solve_lp([Fraction(1), Fraction(3), Fraction(2)],
                                     rows, rhs)
    print(f"    status {status}, iterations {iters}")
    print("    x (exact): (" + ", ".join(str(v) for v in x) + ")")
    print("    x (decimal): (" + ", ".join(f"{float(v):.10f}" for v in x) + ")")
    print(f"    objective, exact: {obj} = {float(obj):.10f}")
    rho = sum(rows[2][j] * x[j] for j in range(3))
    vel = sum(rows[4][j] * x[j] for j in range(3))
    print(f"    achieved rho = {rho} (target 2.6725),"
          f" v = {vel} (target 5.24)")
    print("    constraints satisfied exactly, in exact arithmetic.")

    blend_dual_y, z_dual, d_iters, d_status = dual_lp(
        [Fraction(1), Fraction(3), Fraction(2)], rows, rhs)
    print(f"    dual LP: status {d_status}, iterations {d_iters},"
          f" optimum {z_dual}")
    print(f"    primal + dual = {obj + z_dual}  (strong duality, exactly)")
    print("    dual variables (marginal cost of each specification):")
    print("      " + ", ".join(f"{float(v):+.6f}" for v in blend_dual_y))

    section("2. L1 regression: robust fitting as a linear program")

    a_l1, b_l1, obj_l1, iters, _, _ = l1_fit(Y_OUTLIER)
    a_l2, b_l2 = l2_fit(Y_OUTLIER)
    a_clean, b_clean = l2_fit(Y_CLEAN)
    a_l1c, b_l1c, obj_l1c, _, _, _ = l1_fit(Y_CLEAN)
    print("  Data y = (1, 2, 2, 4, 9) at x = 0, 1, 2, 3, 4 (last datum a blunder);")
    print("  the clean data have 4.6 in place of 9.")
    print(f"  {'fit':<28}{'intercept':>12}{'slope':>12}{'L1 cost':>12}"
          f"{'max |r|':>12}")
    for label, a_fit, b_fit in (("L1, blundered data", float(a_l1), float(b_l1)),
                                ("L2, blundered data", a_l2, b_l2),
                                ("L2, clean data", a_clean, b_clean),
                                ("L1, clean data", float(a_l1c), float(b_l1c))):
        r = [float(v) for v in residuals(a_fit, b_fit, Y_OUTLIER)]
        print(f"  {label:<28}{a_fit:>12.6f}{b_fit:>12.6f}"
              f"{sum(abs(v) for v in r):>12.6f}{max(abs(v) for v in r):>12.6f}")
    print(f"  simplex iterations: {iters}")
    print(f"  exact L1 objective: {obj_l1} = {float(obj_l1):.10f}")
    print("  residuals of the L1 fit, exact: "
          + ", ".join(str(v) for v in residuals(a_l1, b_l1, Y_OUTLIER)))
    print(f"  slope shifts caused by the blunder:"
          f"  L1 {float(b_l1 - b_l1c):+.6f}   L2 {b_l2 - b_clean:+.6f}")
    print(f"  ratio of the two shifts:"
          f" {abs((b_l2 - b_clean) / float(b_l1 - b_l1c)):.1f}")
    print(f"  residuals of the L1 fit that are exactly zero:"
          f" {sum(1 for v in residuals(a_l1, b_l1, Y_OUTLIER) if v == 0)} of 5")
    print("  The blunder moves the least-squares slope about nine times further")
    print("  than the least-absolute-deviations slope.")

    section("3. L-infinity (Chebyshev) fitting as a linear program")

    a_inf, b_inf, t_inf, iters_inf = chebyshev_fit(Y_OUTLIER)
    print("    intercept " + str(a_inf) + ", slope " + str(b_inf))
    print(f"    minimax value {t_inf} = {float(t_inf):.6f},"
          f" iterations {iters_inf}")
    r_inf = [float(v) for v in residuals(float(a_inf), float(b_inf), Y_OUTLIER)]
    print("    residuals: " + ", ".join(f"{v:+.6f}" for v in r_inf))
    at_max = sum(1 for v in r_inf if abs(abs(v) - float(t_inf)) < 1e-9)
    print(f"    residuals attaining the maximum: {at_max}")
    print("  The minimax fit is decided entirely by the extreme points, so one")
    print("  blunder determines the whole line. Robustness is a property of the")
    print("  norm, not of the algorithm used to minimise it.")

    section("4. Strong duality, and the multiplier as a shadow price")

    c_l1, a_l1_rows, b_l1_rows = l1_problem(Y_OUTLIER)
    x_p, z_p, it_p, status_p = solve_lp(c_l1, a_l1_rows, b_l1_rows)
    dual_y, z_d, it_d, status_d = dual_lp(c_l1, a_l1_rows, b_l1_rows)
    print("  the L1 fit as a linear program with 14 variables and 10 constraints:")
    print(f"    primal optimum (exact): {z_p}")
    print(f"    dual optimum (exact):   {z_d}")
    print(f"    primal + dual = {z_p + z_d}  (exactly zero)")
    print(f"    simplex iterations: primal {it_p}, dual {it_d}")
    print(f"    non-zero primal variables:"
          f" {sum(1 for v in x_p if v != 0)} of {len(x_p)}")
    print("  A zero duality gap in exact arithmetic is a certificate that the")
    print("  reported solution is optimal, not merely that no improvement was")
    print("  found. A float solver reports the same thing, but as an inequality.")
    print("  Shadow price check by direct differentiation of the blending LP:")
    eps = Fraction(1, 10000)
    z_plus = solve_lp([Fraction(1), Fraction(3), Fraction(2)],
                      rows, [rhs[0], rhs[1], rhs[2] + eps, rhs[3] - eps,
                             rhs[4], rhs[5]])[1]
    z_minus = solve_lp([Fraction(1), Fraction(3), Fraction(2)],
                       rows, [rhs[0], rhs[1], rhs[2] - eps, rhs[3] + eps,
                              rhs[4], rhs[5]])[1]
    derivative = (z_plus - z_minus) / (2 * eps)
    print(f"    d(objective)/d(density target), central difference: "
          f"{derivative} = {float(derivative):.6f}")
    print(f"    dual variables of the two density rows (from Section 1):"
          f" {float(blend_dual_y[2]):+.6f} and {float(blend_dual_y[3]):+.6f}")
    print("    the rule dz/db_i = -y_i reproduces the measured derivative:")
    print(f"      (-y_2)(+1) + (-y_3)(-1) ="
          f" {float(blend_dual_y[3] - blend_dual_y[2]):+.6f}")

    section("5. Constrained fitting: bounds, and what they cost")

    bound_row = [Fraction(0)] * 14
    bound_row[2] = Fraction(-1)
    bound_row[3] = Fraction(1)
    a_b, b_b, obj_b, iters_b, x_b, idx_b = l1_fit(Y_OUTLIER, [bound_row],
                                                 [Fraction(-1.5)])
    obj_unb = float(obj_l1)
    print("  the same fit, with the slope bounded below by 1.5 (an independent")
    print("  regional constraint):")
    print(f"    unbounded: a = {float(a_l1):.6f}, b = {float(b_l1):.6f},"
          f" cost = {obj_unb:.6f}")
    print(f"    bounded:   a = {float(a_b):.6f}, b = {float(b_b):.6f},"
          f" cost = {float(obj_b):.6f}")
    print(f"    the bound costs {float(obj_b) - obj_unb:.6f} in L1 misfit")
    c_b, a_b_rows, b_b_rows = l1_problem(Y_OUTLIER)
    a_b_rows = a_b_rows + [bound_row]
    b_b_rows = b_b_rows + [Fraction(-1.5)]
    dual_yb, z_db, it_db, st_db = dual_lp(c_b, a_b_rows, b_b_rows)
    print(f"    dual LP: status {st_db}, iterations {it_db}, optimum {z_db}")
    print(f"    primal + dual = {obj_b + z_db}  (exactly zero)")
    print(f"    dual variable of the bound constraint (row"
          f" {len(b_b_rows) - 1}): {float(dual_yb[-1]):+.6f}")
    print("    dual variables of the first five data rows:"
          " " + ", ".join(f"{float(v):+.4f}" for v in dual_yb[:5]))
    # Shadow price of the bound, by differentiating the constrained LP.
    eps = Fraction(1, 10000)
    z_plus = l1_fit(Y_OUTLIER, [bound_row], [Fraction(-1.5) + eps])[2]
    z_minus = l1_fit(Y_OUTLIER, [bound_row], [Fraction(-1.5) - eps])[2]
    print(f"    d(cost)/d(bound right-hand side) by central difference:"
          f" {float((z_plus - z_minus) / (2 * eps)):+.6f}")
    print(f"    the rule dz/db = -y gives:"
          f" {float(-dual_yb[-1]):+.6f}")

    section("6. Exact arithmetic versus floating point on the same LP")

    rng = random.Random(7)
    exact = float(obj_l1)
    worst = 0.0
    n = len(Y_OUTLIER)
    for _ in range(5):
        y_perturbed = [Y_OUTLIER[i] * (1.0 + rng.uniform(-1e-12, 1e-12))
                       for i in range(n)]
        a_g, b_g, _, _, _, _ = l1_fit([Fraction(v) for v in y_perturbed])
        cost_g = sum(abs(float(a_g + b_g * X[i] - Y_OUTLIER[i]))
                     for i in range(n))
        worst = max(worst, abs(cost_g - exact))
    print(f"  exact L1 optimum of the unperturbed data: {exact:.12f}")
    print(f"  worst change in the objective after perturbing every datum by 1e-12")
    print(f"  relative: {worst:.3e}")
    print("  Three of the five residuals are kinked at the optimum, so the")
    print("  objective is not smooth there, but the *value* is still stable: the")
    print("  extremal residual belongs to the blunder, whose exact value does not")
    print("  determine the fit. That insensitivity is why L1 is worth an LP.")


if __name__ == "__main__":
    main()
