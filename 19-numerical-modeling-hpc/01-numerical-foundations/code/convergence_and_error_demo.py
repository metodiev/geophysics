#!/usr/bin/env python3
"""Order of accuracy: exact truncation constants, observed order from a
three-grid refinement study, Richardson extrapolation, a grid-convergence
index, and the round-off floor that terminates refinement.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python convergence_and_error_demo.py

All models and data in this module are SYNTHETIC.  The manufactured problem and
its exact solution are chosen teaching values, not measurements.

Contents
--------
1. Truncation constants of three difference operators, measured against exact.
2. Manufactured 1-D Poisson problem with the exact solution u = sin(pi x).
3. Observed order of accuracy from three grids; Richardson extrapolation.
4. Grid-convergence index and its safety factor, compared with the true error.
5. Round-off: the optimal step and the accuracy ceiling of refinement.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def d_forward(f, x, h):
    return (f(x + h) - f(x)) / h


def d_central(f, x, h):
    return (f(x + h) - f(x - h)) / (2.0 * h)


def d_central4(f, x, h):
    return (-f(x + 2 * h) + 8.0 * f(x + h) - 8.0 * f(x - h) + f(x - 2 * h)) / (12.0 * h)


def d_second(f, x, h):
    return (f(x + h) - 2.0 * f(x) + f(x - h)) / h ** 2


def truncation_constants():
    """Measured leading truncation error / h^p against the exact Taylor value."""
    f = np.sin
    x0 = 0.5
    print("f(x) = sin(x), x0 = 0.5 rad; exact first derivative = "
          f"{np.cos(x0):.8f}, exact second derivative = {-np.sin(x0):.8f}")
    cases = (
        ("forward  f1   p=1", d_forward, 1, np.cos(x0), -np.sin(x0) / 2.0),
        ("central  f1   p=2", d_central, 2, np.cos(x0), -np.cos(x0) / 6.0),
        ("central4 f1   p=4", d_central4, 4, np.cos(x0), -np.cos(x0) / 30.0),
        ("central  f2   p=2", d_second, 2, -np.sin(x0), np.sin(x0) / 12.0),
    )
    for name, op, p, exact_value, exact_c in cases:
        h = 0.01
        err = op(f, x0, h) - exact_value
        print(f"  {name}: h = {h:.4f}, error = {err:+.10e}, "
              f"error/h^{p} = {err / h ** p:+.7f}, exact Taylor value = {exact_c:+.7f}")
    print("  error/h^p matches the Taylor coefficient, so the order is not fitted")
    print("  but predicted: p is the exponent of the first non-cancelling term.")


def poisson_1d(n):
    """Solve -u'' = pi^2 sin(pi x) on (0,1), u(0) = u(1) = 0, exactly u = sin(pi x).

    The grid is x_i = i/n, so refining n -> 2n nests the grids and successive
    solutions can be compared node for node.  The Dirichlet values are imposed
    exactly, so the observed order is the interior order of the operator.
    """
    h = 1.0 / n
    x = np.arange(n + 1) * h
    m = n - 1
    rhs = np.pi ** 2 * np.sin(np.pi * x[1:-1])
    A = (np.diag(2.0 * np.ones(m)) + np.diag(-np.ones(m - 1), 1)
         + np.diag(-np.ones(m - 1), -1)) / h ** 2
    u = np.linalg.solve(A, rhs)
    u_full = np.concatenate(([0.0], u, [0.0]))
    exact = np.sin(np.pi * x)
    return np.max(np.abs(u_full - exact)), u_full, exact


def convergence_study():
    print("manufactured problem: -u'' = pi^2 sin(pi x) on (0,1), exact u = sin(pi x)")
    print("smooth-error prediction: e -> -(h^2 pi^2/12) u, so Linf error/h^2 -> "
          f"{np.pi ** 2 / 12:.6f}")
    ns = (10, 20, 40, 80, 160)
    errs, sols, exacts = [], [], []
    for n in ns:
        e, u, ex = poisson_1d(n)
        errs.append(e)
        sols.append(u)
        exacts.append(ex)
    print(f"{'n cells':>8} {'h':>10} {'Linf error':>16} {'error/h^2':>12} "
          f"{'p from pairs':>14} {'p from |du| ratio':>18}")
    for k, n in enumerate(ns):
        h = 1.0 / n
        p_pair = np.nan
        if k >= 1:
            p_pair = np.log(errs[k - 1] / errs[k]) / np.log(2.0)
        p_diff = np.nan
        if k >= 2:
            d_prev = sols[k - 1][::2] - sols[k - 2]      # on the coarser nodes
            d_here = sols[k][::2] - sols[k - 1]
            p_diff = np.log(np.max(np.abs(d_prev)) / np.max(np.abs(d_here))) / np.log(2.0)
        print(f"{n:>8} {h:>10.6f} {errs[k]:>16.6e} {errs[k] / h ** 2:>12.6f} "
              f"{p_pair:>14.6f} {p_diff:>18.6f}")
    print("p from the solution-difference ratio is the estimate a real study can")
    print("form: it assumes only that the grids nest and the error is smooth.")

    # Richardson extrapolation on the two finest grids, on the shared nodes.
    n_coarse, n_fine = ns[-2], ns[-1]
    u_coarse = sols[-2]
    u_fine_on_coarse = sols[-1][::2]
    exact_coarse = exacts[-2]
    p = np.log(np.max(np.abs(sols[-2][::2] - sols[-3])) /
               np.max(np.abs(u_fine_on_coarse - u_coarse))) / np.log(2.0)
    u_ext = u_fine_on_coarse + (u_fine_on_coarse - u_coarse) / (2.0 ** p - 1.0)
    err_fine = np.max(np.abs(u_fine_on_coarse - exact_coarse))
    err_ext = np.max(np.abs(u_ext - exact_coarse))
    print(f"\nRichardson extrapolation on the n = {n_coarse} and {n_fine} grids "
          f"with r = 2, p = {p:.6f}:")
    print(f"  Linf error of the fine solution      = {err_fine:.6e}")
    print(f"  Linf error of the extrapolated value = {err_ext:.6e}")
    print(f"  improvement factor                   = {err_fine / err_ext:.2f}")

    # Grid-convergence index (Roache's estimator, safety factor 1.25 by convention),
    # referred to the peak amplitude to avoid dividing by a zero of the solution.
    amp = np.max(np.abs(u_fine_on_coarse))
    gci = 1.25 * np.max(np.abs(u_fine_on_coarse - u_coarse)) / amp / (2.0 ** p - 1.0)
    true_rel = err_fine / amp
    print(f"\ngrid-convergence index (Fs = 1.25, p = {p:.6f}), referred to the peak")
    print(f"  GCI                          = {gci * 100:.6f} %")
    print(f"  true relative error of u_fine = {true_rel * 100:.6f} %")
    print(f"  ratio GCI / true error        = {gci / true_rel:.4f}")
    return errs


def roundoff_floor():
    """Accuracy ceiling of the second-derivative operator on a smooth function."""
    f = np.sin
    x0 = 0.5
    u = np.finfo(float).eps
    print("central difference of the second derivative at x0 = 0.5 with f = sin")
    print(f"  machine epsilon u = {u:.3e}")
    print(f"{'h':>10} {'measured error':>18} {'h^2/12 + 4u/h^2':>20}")
    hs = np.logspace(-1, -8, 60)
    errs = np.array([d_second(f, x0, h) + np.sin(x0) for h in hs])
    i = int(np.argmin(np.abs(errs)))
    for h in (1e-1, 1e-3, 1e-4, hs[i], 1e-5, 1e-6, 1e-8):
        e = d_second(f, x0, h) + np.sin(x0)
        print(f"{h:>10.3e} {e:>18.8e} {h ** 2 / 12 + 4 * u / h ** 2:>20.3e}")
    print(f"the smallest absolute error occurs at h = {hs[i]:.3e}, "
          f"|error| = {abs(errs[i]):.3e}")
    # Fit the round-off term where it dominates: |error| ~ c u / h^2.
    small = hs < 1e-6
    c = np.median(np.abs(errs[small]) * hs[small] ** 2 / u)
    print(f"measured round-off coefficient: |error| h^2 / u = {c:.4f}")
    print("  the classical worst-case bound uses 4 u / h^2, i.e. a coefficient of 4,")
    print(f"  so at these steps it overestimates the round-off by {4 / c:.0f}x")
    print(f"  predicted optimum from the measured coefficient: "
          f"(12 c u)^(1/4) = {(12 * c * u) ** 0.25:.3e} "
          f"(measured {hs[i]:.3e})")
    print("truncation error falls as h^2 while round-off grows as u/h^2, so there")
    print("is an accuracy ceiling: refining past it makes the answer worse.")


def main():
    section("1. Truncation constants versus the exact Taylor prediction")
    truncation_constants()

    section("2. Observed order of accuracy from a refinement study")
    convergence_study()

    section("3. Round-off floor: refinement has a ceiling")
    roundoff_floor()


if __name__ == "__main__":
    main()
