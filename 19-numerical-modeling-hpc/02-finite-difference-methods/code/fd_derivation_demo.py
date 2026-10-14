#!/usr/bin/env python3
"""Deriving finite-difference operators from Taylor expansion: weights, exact
orders, exact truncation constants, and the cost of one misplaced node.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_derivation_demo.py

All models and data in this module are SYNTHETIC.  The functions and grids below
are chosen teaching values, not measurements.

Contents
--------
1. Solving the moment equations for stencil weights (Vandermonde system).
2. Exact order and leading truncation coefficient of each stencil.
3. Polynomial exactness: degree <= p reproduced to round-off, degree p+1 not.
4. Measured convergence order on a smooth function, against the exact constant.
5. A non-uniform node used as if it were uniform: the order collapses.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def factorial(n):
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out


def solve_weights(offsets, d):
    n = len(offsets)
    V = np.array([[xi ** m for xi in offsets] for m in range(n)], dtype=float)
    rhs = np.zeros(n)
    rhs[d] = float(factorial(d))
    return np.linalg.solve(V, rhs)


def order_and_coefficient(offsets, weights, d):
    """First non-vanishing moment: returns (order, leading coefficient / p!).

    For a stencil exact for polynomials of degree < p the truncation error is
    C h^p f^(p)(x) with C = sum_i w_i xi_i^p / p!.
    """
    n = len(offsets)
    for m in range(d, d + n + 3):
        if m == d:
            continue
        moment = sum(w * xi ** m for w, xi in zip(weights, offsets))
        if abs(moment) > 1e-12 * max(1.0, np.max(np.abs(weights))):
            return m - d, moment / float(factorial(m))
    return np.nan, 0.0


def demo_stencils():
    cases = [
        ("forward  u'  (2 nodes)", [-0.0, 1.0], 1),
        ("backward u'  (2 nodes)", [-1.0, 0.0], 1),
        ("central  u'  (3 nodes)", [-1.0, 0.0, 1.0], 1),
        ("one-sided u' (3 nodes)", [0.0, 1.0, 2.0], 1),
        ("central  u'  (5 nodes)", [-2.0, -1.0, 0.0, 1.0, 2.0], 1),
        ("central  u'  (7 nodes)", [-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0], 1),
        ("central  u'' (3 nodes)", [-1.0, 0.0, 1.0], 2),
        ("central  u'' (5 nodes)", [-2.0, -1.0, 0.0, 1.0, 2.0], 2),
        ("non-uniform u' (3 nodes)", [-1.0, 0.3, 1.7], 1),
    ]
    print(f"{'stencil':>26} {'weights (x h^d)':>44} {'order':>7} "
          f"{'coeff of h^p f^(p)':>20}")
    for name, offsets, d in cases:
        w = solve_weights(offsets, d)
        p, c = order_and_coefficient(offsets, w, d)
        wtxt = ", ".join(f"{wi:+.6f}" for wi in w)
        print(f"{name:>26} {wtxt:>44} {p:>7} {c:>20.8f}")
    print("the weights come from the moment equations; the order is the index of")
    print("the first moment that does not vanish by construction.")


def polynomial_exactness():
    f_deriv = {0: lambda x: x ** 2, 1: lambda x: 1.0 * x}
    print("applying the central 3-node u' stencil to monomials at x = 0.7")
    offsets = [-1.0, 0.0, 1.0]
    w = solve_weights(offsets, 1)
    h = 0.1
    for m in (1, 2, 3, 4):
        approx = sum(wi * (0.7 + xi * h) ** m for wi, xi in zip(w, offsets)) / h
        exact = m * 0.7 ** (m - 1)
        print(f"  x^{m}: stencil = {approx:.12e}, exact derivative = "
              f"{exact:.12e}, difference = {approx - exact:+.3e}")
    print("degree <= 2 is reproduced exactly (the stencil is exact for quadratics);")
    print("the residual for x^3 scales with h and is the first non-vanishing")
    print("moment of the stencil.")
    print("\nthe residual of the same stencil on x^3, for three step sizes:")
    for h in (0.1, 0.01, 0.001):
        approx = sum(wi * (0.7 + xi * h) ** 3 for wi, xi in zip(w, offsets)) / h
        exact = 3 * 0.7 ** 2
        print(f"  h = {h:.3f}: residual = {approx - exact:+.10e}, "
              f"residual/h^2 = {(approx - exact) / h ** 2:+.8f} "
              f"(exact coefficient f'''/6 = {6.0 / 6.0:.8f})")


def convergence_orders():
    f = np.sin
    x0 = 0.3
    print("measured convergence of several stencils on f = sin at x0 = 0.3 rad")
    print(f"{'stencil':>22} {'h = 0.1':>13} {'h = 0.05':>13} {'h = 0.025':>13} "
          f"{'order':>8} {'exact coeff':>14} {'measured err/h^p':>18}")
    cases = [
        ("forward  u'", [-0.0, 1.0], 1, 1, -np.sin(x0) / 2.0),
        ("central  u'", [-1.0, 0.0, 1.0], 1, 2, -np.cos(x0) / 6.0),
        ("central  u' (5)", [-2.0, -1.0, 0.0, 1.0, 2.0], 1, 4, -np.cos(x0) / 30.0),
        ("central  u''", [-1.0, 0.0, 1.0], 2, 2, np.sin(x0) / 12.0),
        ("one-sided u'", [0.0, 1.0, 2.0], 1, 2, np.cos(x0) / 3.0),
    ]
    for name, offsets, d, p, expected in cases:
        w = solve_weights(offsets, d)
        errs = []
        for h in (0.1, 0.05, 0.025):
            approx = sum(wi * f(x0 + xi * h) for wi, xi in zip(w, offsets)) / h ** d
            exact = np.cos(x0) if d == 1 else -np.sin(x0)
            errs.append(abs(approx - exact))
        order = np.log(errs[0] / errs[1]) / np.log(2.0)
        print(f"{name:>22} {errs[0]:>13.6e} {errs[1]:>13.6e} {errs[2]:>13.6e} "
              f"{order:>8.4f} {expected:>14.8f} {errs[-1] / 0.025 ** p:>18.8f}")
    print("the measured error/h^p reproduces the Taylor coefficient derived from")
    print("the first non-vanishing moment of the stencil.")


def misplaced_node():
    """Two ways to get the node positions wrong, and what each one costs."""
    f = np.sin
    delta = 0.1
    x0 = 0.3
    w_uniform = solve_weights([-1.0, 0.0, 1.0], 1)
    w_true = solve_weights([-1.0, 0.0, 1.0 + delta], 1)
    print("the right-hand node of a three-node stencil actually sits at (1+delta)h")
    print(f"with delta = {delta}, evaluated at x0 = {x0} rad")
    print("(a) the weights derived for a uniform grid are used anyway:")
    print(f"{'h':>8} {'error':>16} {'error ratio (prev/now)':>24}")
    prev = None
    for h in (0.1, 0.05, 0.025, 0.0125):
        approx = (w_uniform[0] * f(x0 - h) + w_uniform[1] * f(x0)
                  + w_uniform[2] * f(x0 + (1.0 + delta) * h)) / h
        err = approx - np.cos(x0)
        ratio = "n/a" if prev is None else f"{prev / err:.6f}"
        print(f"{h:>8.4f} {err:>16.8e} {ratio:>24}")
        prev = err
    print(f"the error does not vanish: it tends to delta/2 * f' = "
          f"{delta / 2.0 * np.cos(x0):.8f}.  The weights no longer cancel the")
    print("first-derivative term, so the operator is inconsistent, not merely")
    print("lower-order: refining the grid cannot recover the derivative.")
    c2 = sum(w * xi ** 2 for w, xi in zip(w_uniform, [-1.0, 0.0, 1.0 + delta]))
    print("\n(b) the weights solved for the true node positions [-1, 0, 1.1]:")
    print(f"{'h':>8} {'error':>16} {'order':>8} {'error/h^2':>14}")
    prev = None
    for h in (0.1, 0.05, 0.025, 0.0125):
        approx = (w_true[0] * f(x0 - h) + w_true[1] * f(x0)
                  + w_true[2] * f(x0 + (1.0 + delta) * h)) / h
        err = approx - np.cos(x0)
        order = "n/a" if prev is None else f"{np.log(abs(prev / err)) / np.log(2.0):.4f}"
        print(f"{h:>8.4f} {err:>16.8e} {order:>8} {err / h ** 2:>14.8f}")
        prev = err
    c3 = sum(w * xi ** 3 for w, xi in zip(w_true, [-1.0, 0.0, 1.0 + delta]))
    print(f"the order is 2 and the measured error/h^2 approaches the predicted")
    print(f"c3 * f''' = {(c3 / 6.0) * (-np.cos(x0)):.8f} "
          f"(c3 = {c3:.4f}, from the first surviving moment)")
    print("solving the moment equations for the actual node positions keeps the")
    print("order; assuming a uniform grid when the grid is not uniform does not.")


def main():
    section("1. Weights from the moment equations")
    demo_stencils()

    section("2. Polynomial exactness and the first non-vanishing moment")
    polynomial_exactness()

    section("3. Measured convergence orders against exact Taylor constants")
    convergence_orders()

    section("4. A grid-position error destroys the order")
    misplaced_node()


if __name__ == "__main__":
    main()
