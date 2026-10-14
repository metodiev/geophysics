#!/usr/bin/env python3
"""Spectral elements: Gauss-Lobatto-Legendre nodes, diagonal mass, convergence.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spectral_elements_demo.py

All models are SYNTHETIC.  Every reference value is exact mathematics (the
polynomial exactness of Gauss-Lobatto quadrature, the diagonal mass identity) or
a number this script measures.

Contents
--------
1. Gauss-Lobatto-Legendre quadrature: exactness limit, measured.
2. The SEM mass matrix is diagonal with the quadrature weights, measured; and
   how far its diagonal is from the exact one.
3. p-refinement at fixed element size: exponential convergence, measured.
4. h-refinement at fixed order: algebraic convergence, measured, for comparison.
5. The largest stiffness eigenvalue against p and against h, with fitted
   exponents and the explicit time-step limit they impose.
"""

import numpy as np
import scipy.special as ssp

RNG = np.random.default_rng(20261014)

U_EXACT = lambda x: np.sin(np.pi * x)
DU_EXACT = lambda x: np.pi * np.cos(np.pi * x)
F_SOURCE = lambda x: np.pi ** 2 * np.sin(np.pi * x)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def gll_nodes_weights(p):
    """p+1 Gauss-Lobatto-Legendre nodes on [-1,1] and their quadrature weights."""
    if p == 1:
        x = np.array([-1.0, 1.0])
    else:
        x = np.concatenate(([-1.0], np.sort(ssp.roots_jacobi(p - 1, 1.0, 1.0)[0]),
                            [1.0]))
    # weights: w_j = 2 / (p(p+1) [P_p(x_j)]^2), computed stably from the
    # Legendre polynomial evaluated by its three-term recurrence
    Pp = np.polynomial.legendre.Legendre.basis(p)(x)
    w = 2.0 / (p * (p + 1) * Pp ** 2)
    return x, w


def lagrange(xnodes, x):
    n = xnodes.size
    out = np.ones((n, np.size(x)))
    for j in range(n):
        for m in range(n):
            if m != j:
                out[j] *= (x - xnodes[m]) / (xnodes[j] - xnodes[m])
    return out


def dlagrange(xnodes, x):
    n = xnodes.size
    out = np.zeros((n, np.size(x)))
    for j in range(n):
        for m in range(n):
            if m == j:
                continue
            term = np.ones(np.size(x)) / (xnodes[j] - xnodes[m])
            for k in range(n):
                if k != j and k != m:
                    term = term * (x - xnodes[k]) / (xnodes[j] - xnodes[k])
            out[j] += term
    return out


def gauss_nodes_weights(n):
    return np.polynomial.legendre.leggauss(n)


def sem_solve(p, n_elem, f_fun=F_SOURCE):
    """SEM (GLL) solution of -u'' = f on (0,1) with u(0) = u(1) = 0."""
    h = 1.0 / n_elem
    xi, w = gll_nodes_weights(p)
    phi = lagrange(xi, xi)
    dphi = dlagrange(xi, xi)
    ndof = p * n_elem + 1
    K = np.zeros((ndof, ndof))
    M = np.zeros((ndof, ndof))
    F = np.zeros(ndof)
    for e in range(n_elem):
        xq = h * 0.5 * (xi + 1.0) + e * h
        fe = h * 0.5 * (phi * f_fun(xq)[None, :]) @ w
        ke = (2.0 / h) * (dphi * w[None, :]) @ dphi.T
        me = (h / 2.0) * (phi * w[None, :]) @ phi.T
        idx = e * p + np.arange(p + 1)
        K[np.ix_(idx, idx)] += ke
        M[np.ix_(idx, idx)] += me
        F[idx] += fe
    u = np.zeros(ndof)
    u[1:-1] = np.linalg.solve(K[1:-1, 1:-1], F[1:-1])
    return u, K, M


def l2_h1(p, n_elem, u):
    """L2 and H1 errors, integrated with a Gauss rule of order p+6.

    Measuring the error with the GLL rule of the element itself under-integrates
    the error integrand and inflates the apparent convergence order; the error
    norm is part of the experiment, so it is computed to accuracy well beyond
    the discretisation error it reports.
    """
    h = 1.0 / n_elem
    xi, _ = gll_nodes_weights(p)
    xg, wg = gauss_nodes_weights(p + 6)
    phi = lagrange(xi, xg)
    dphi = dlagrange(xi, xg)
    e2 = eh1 = 0.0
    for e in range(n_elem):
        xq = h * 0.5 * (xg + 1.0) + e * h
        ue = u[e * p + np.arange(p + 1)] @ phi
        due = u[e * p + np.arange(p + 1)] @ dphi * (2.0 / h)
        e2 += h * 0.5 * np.sum(wg * (ue - U_EXACT(xq)) ** 2)
        eh1 += h * 0.5 * np.sum(wg * (due - DU_EXACT(xq)) ** 2)
    return np.sqrt(e2), np.sqrt(eh1)


def fit_slope(levels, errs):
    x = np.log(np.asarray(levels, float))
    y = np.log(np.asarray(errs, float))
    dx = x - x.mean()
    return float(np.sum(dx * (y - y.mean())) / np.sum(dx * dx))


def main():
    section("1. Gauss-Lobatto-Legendre quadrature: exactness, measured")
    print("  p+1 GLL nodes integrate polynomials of degree <= 2p-1 exactly.  The")
    print("  quantity measured is |sum_j w_j x_j^d - exact| for the highest exact")
    print("  degree and for the next degree up.")
    print("     p    sum of weights - 2     error at degree 2p-1      error at degree 2p")
    for p in (2, 4, 6, 8, 12):
        x, w = gll_nodes_weights(p)
        d_ok = 2 * p - 1
        e_ok = abs(np.sum(w * x ** d_ok) - (2.0 / (d_ok + 1) if d_ok % 2 == 0 else 0.0))
        d_bad = 2 * p
        e_bad = abs(np.sum(w * x ** d_bad) - 2.0 / (d_bad + 1))
        print(f"  {p:5d}   {abs(np.sum(w) - 2.0):18.3e}   {e_ok:22.3e}   "
              f"{e_bad:20.3e}")
    print("  The weights sum to 2 exactly and the odd-degree column is round-off, as")
    print("  it must be.  The even-degree column is non-zero from the first degree the")
    print("  rule cannot integrate, exactly as Gauss-Legendre behaves earlier than GLL")
    print("  for the same number of nodes -- the price of including the endpoints.")

    section("2. The element mass matrix is diagonal, measured")
    print("  Evaluating int phi_i phi_j dx with the GLL rule gives sum_q w_q")
    print("  phi_i(x_q) phi_j(x_q) = delta_ij w_i: diagonal BY CONSTRUCTION, because the")
    print("  Lagrange basis vanishes at every node but its own.  The exact integral is")
    print("  not diagonal, so this is under-integration -- and it is the reason")
    print("  spectral-element codes have a diagonal mass matrix and cheap explicit")
    print("  time stepping.")
    print("     p    max off-diagonal (GLL)    max |diag(GLL) - diag(exact)|")
    for p in (2, 4, 6, 8):
        xi, w = gll_nodes_weights(p)
        phi = lagrange(xi, xi)
        m_gll = (phi * w[None, :]) @ phi.T
        xg, wg = gauss_nodes_weights(p + 6)
        phig = lagrange(xi, xg)
        m_exact = (phig * wg[None, :]) @ phig.T
        off = np.max(np.abs(m_gll - np.diag(np.diag(m_gll))))
        dd = np.max(np.abs(np.diag(m_gll) - np.diag(m_exact)))
        print(f"  {p:5d}   {off:24.3e}   {dd:31.3e}")
    print("  The off-diagonal is round-off at every order, which is exact, not")
    print("  approximate.  The diagonal differs from the exact integral, and that")
    print("  difference is a modelling choice with a price, not an error to be removed.")

    section("3. p-refinement at fixed element size")
    print("  Two elements of order p spanning (0,1); exact u = sin(pi x).")
    print("     p   ndof      L2 error      ratio to previous     H1 error")
    prev = None
    for p in (2, 3, 4, 6, 8, 10, 12):
        u, _, _ = sem_solve(p, 2)
        e2, eh1 = l2_h1(p, 2, u)
        ratio = "" if prev is None else f"{prev / e2:22.3e}"
        print(f"  {p:4d}   {2 * p + 1:4d}   {e2:.3e}   {ratio}   {eh1:.3e}")
        prev = e2
    print("  The error falls by orders of magnitude per element order -- exponential")
    print("  convergence -- until it reaches the round-off floor of the assembly, after")
    print("  which nothing improves.  That floor, not the method, is what stops it.")
    print("  Contrast with Section 4, where refinement in h is only algebraic: p is the")
    print("  right knob when the solution is smooth inside each element, and h is the")
    print("  right knob when it is not.")

    section("4. h-refinement at fixed order p = 4")
    print("     n_elem   ndof      L2 error      order       H1 error     order")
    prev = None
    hs, l2s, h1s = [], [], []
    for n_elem in (2, 4, 8, 16, 32):
        u, _, _ = sem_solve(4, n_elem)
        e2, eh1 = l2_h1(4, n_elem, u)
        o2 = "" if prev is None else f"{np.log2(prev[0] / e2):8.3f}"
        oh = "" if prev is None else f"{np.log2(prev[1] / eh1):8.3f}"
        print(f"  {n_elem:8d}   {4 * n_elem + 1:4d}   {e2:.3e}  {o2}   {eh1:.3e}  {oh}")
        prev = (e2, eh1)
        hs.append(1.0 / n_elem)
        l2s.append(e2)
        h1s.append(eh1)
    print(f"  fitted orders: L2 {fit_slope(1.0 / np.asarray(hs), l2s):.2f}, "
          f"H1 {fit_slope(1.0 / np.asarray(hs), h1s):.2f}   (theory: p+1 = 5 and p = 4)")
    print("  The sequential orders are 5 and 4 per halving of h, exactly the p+1 and p")
    print("  of any order-p Galerkin method: a spectral element refines like a")
    print("  finite element in h.  What it adds is Section 3's behaviour in p.")

    section("5. Largest eigenvalue, and the time-step limit it sets")
    print("  For the explicit wave equation the stable step is dt <= 2/sqrt(lambda_max)")
    print("  where lambda_max is the largest GENERALISED eigenvalue of K v = lambda M v.")
    print("  Both matrices are built with the element's own GLL rule, as a spectral")
    print("  element code does.")
    print("     p (h = 0.5)   lambda_max      dt limit (s)     p^4 model")
    lams, ps = [], []
    for p in (2, 4, 6, 8, 10):
        _, K, M = sem_solve(p, 2)
        Kr, Mr = K[1:-1, 1:-1], M[1:-1, 1:-1]
        lam = np.linalg.eigvalsh(np.linalg.solve(Mr, Kr)).max()
        lams.append(lam)
        ps.append(p)
        print(f"  {p:13d}   {lam:11.4f}   {2.0 / np.sqrt(lam):13.6f}   "
              f"{p ** 4 / 0.25:11.1f}")
    print(f"  fitted exponent in p = {fit_slope(ps, lams):.3f} over p = 2..10")
    print("     n_elem (p=4)  h         lambda_max     dt limit (s)    1/h^2 model")
    hs2, lams2 = [], []
    for n_elem in (2, 4, 8, 16, 32):
        _, K, M = sem_solve(4, n_elem)
        Kr, Mr = K[1:-1, 1:-1], M[1:-1, 1:-1]
        lam = np.linalg.eigvalsh(np.linalg.solve(Mr, Kr)).max()
        hh = 1.0 / n_elem
        hs2.append(hh)
        lams2.append(lam)
        print(f"  {n_elem:13d}   {hh:7.4f}   {lam:11.4f}   {2.0 / np.sqrt(lam):13.6f}   "
              f"{1.0 / hh ** 2:11.1f}")
    print(f"  fitted exponent in 1/h = {fit_slope(1.0 / np.asarray(hs2), lams2):.3f} "
          f"over n_elem = 2..32")
    print("  The mesh dependence is the familiar h^-2 to three digits.  The order")
    print("  dependence is far steeper than the p^2 of a fixed-order scheme: the")
    print(f"  measured exponent over p = 2..10 is {fit_slope(ps, lams):.3f}, between p^3")
    print("  and p^4, and the p^4 column overpredicts at low order -- which is the")
    print("  point of measuring rather than quoting a stability bound.  Raising the")
    print("  order to gain accuracy shrinks the explicit time step at the same time;")
    print("  that trade, not the accuracy alone, is what governs a spectral-element")
    print("  wave solver.")
    print("\nAll numbers are printed by this script; the model is SYNTHETIC.")


if __name__ == "__main__":
    main()
