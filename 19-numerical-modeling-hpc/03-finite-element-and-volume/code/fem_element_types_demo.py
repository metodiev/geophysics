#!/usr/bin/env python3
"""Element types, Lagrange shape functions and quadrature, measured.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fem_element_types_demo.py

SYNTHETIC throughout: the meshes, coefficients and manufactured solutions are
chosen teaching models.  No external FEM package is used.

Contents
--------
1. Lagrange shape functions: partition of unity, Kronecker property, derivative
   completeness, and interpolation error.
2. Gauss-Legendre exactness, including the degree at which it fails.
3. Element matrix properties: symmetry, definiteness, node-distribution
   conditioning.
4. h-refinement for polynomial order p = 1, 2, 3: measured L2 and H1 orders.
5. Consistent versus lumped (under-integrated) mass: eigenvalue error.
6. Quadrature order required by an element with a variable coefficient.
"""

import numpy as np
import scipy.linalg as sla
import scipy.special as ssp

RNG = np.random.default_rng(20261014)

U_EXACT = lambda x: np.sin(np.pi * x)
DU_EXACT = lambda x: np.pi * np.cos(np.pi * x)
F_SOURCE = lambda x: np.pi ** 2 * np.sin(np.pi * x)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def gl(n):
    """n-point Gauss-Legendre nodes and weights on [-1, 1]."""
    return np.polynomial.legendre.leggauss(n)


def gll_nodes(p):
    """p+1 Gauss-Lobatto-Legendre nodes on [-1, 1]."""
    if p == 1:
        return np.array([-1.0, 1.0])
    interior = ssp.roots_jacobi(p - 1, 1.0, 1.0)[0]
    return np.concatenate(([-1.0], np.sort(interior), [1.0]))


def lagrange_basis(xnodes, x):
    """Lagrange basis on nodes ``xnodes``, evaluated at ``x``; shape (p+1, |x|)."""
    n = xnodes.size
    out = np.ones((n, np.size(x)), dtype=float)
    for j in range(n):
        for m in range(n):
            if m != j:
                out[j] *= (x - xnodes[m]) / (xnodes[j] - xnodes[m])
    return out


def dlagrange_basis(xnodes, x):
    """Derivative with respect to the parent coordinate of the Lagrange basis."""
    n = xnodes.size
    out = np.zeros((n, np.size(x)), dtype=float)
    for j in range(n):
        for m in range(n):
            if m == j:
                continue
            term = np.ones(np.size(x), dtype=float) / (xnodes[j] - xnodes[m])
            for k in range(n):
                if k != j and k != m:
                    term = term * (x - xnodes[k]) / (xnodes[j] - xnodes[k])
            out[j] += term
    return out


def element_matrices(p, h, x_left, a_fun, n_q=None):
    """Stiffness and mass matrices of a Lagrange element of order p on one cell.

    Parent coordinate xi in [-1, 1]; the element is x = x_left + (h/2)(xi+1),
    so d/dx = (2/h) d/dxi and dx = (h/2) dxi.
    """
    n_q = n_q or (p + 3)
    xg, wg = gl(n_q)
    s = 0.5 * (xg + 1.0)                      # parent coordinate mapped to [0, 1]
    w = 0.5 * wg                              # weights summing to 1
    a = a_fun(x_left + h * s)
    xi = np.linspace(-1.0, 1.0, p + 1)        # equally spaced parent nodes
    phi = lagrange_basis(xi, xg)
    dphi = dlagrange_basis(xi, xg) * 2.0 / h
    ke = h * (dphi * a[None, :]) @ (dphi * w[None, :]).T
    me = h * (phi * a[None, :]) @ (phi * w[None, :]).T
    return ke, me


def assemble(p, n_elem, a_fun, f_fun, n_q=None):
    """Assembly and solution of -(a u')' = f with Dirichlet data at both ends."""
    h = 1.0 / n_elem
    ndof = p * n_elem + 1
    K = np.zeros((ndof, ndof))
    F = np.zeros(ndof)
    n_q = n_q or (p + 3)
    xg, wg = gl(n_q)
    s = 0.5 * (xg + 1.0)
    w = 0.5 * wg
    xi = np.linspace(-1.0, 1.0, p + 1)
    for e in range(n_elem):
        x_left = e * h
        ke, _ = element_matrices(p, h, x_left, a_fun, n_q)
        phi = lagrange_basis(xi, xg)
        fe = h * (phi * f_fun(x_left + h * s)[None, :]) @ w
        idx = e * p + np.arange(p + 1)
        K[np.ix_(idx, idx)] += ke
        F[idx] += fe
    u = np.zeros(ndof)
    u[1:-1] = np.linalg.solve(K[1:-1, 1:-1], F[1:-1])
    return u, K, F


def errors(p, n_elem, u):
    """L2 and H1-seminorm errors, integrated element by element."""
    h = 1.0 / n_elem
    n_q = 3 * p + 6
    xg, wg = gl(n_q)
    s = 0.5 * (xg + 1.0)
    w = 0.5 * wg
    xi = np.linspace(-1.0, 1.0, p + 1)
    phi = lagrange_basis(xi, xg)
    dphi = dlagrange_basis(xi, xg) * 2.0 / h
    e2 = eh1 = 0.0
    for e in range(n_elem):
        xq = e * h + h * s
        ue = u[e * p + np.arange(p + 1)] @ phi
        due = u[e * p + np.arange(p + 1)] @ dphi
        e2 += h * np.sum(w * (ue - U_EXACT(xq)) ** 2)
        eh1 += h * np.sum(w * (due - DU_EXACT(xq)) ** 2)
    return np.sqrt(e2), np.sqrt(eh1)


def fit_order(levels, errs):
    """Log-log least-squares slope, from the normal equations."""
    x = np.log(np.asarray(levels, float))
    y = np.log(np.asarray(errs, float))
    dx = x - x.mean()
    return float(np.sum(dx * (y - y.mean())) / np.sum(dx * dx))


def main():
    section("1. Lagrange shape functions on the parent interval [-1, 1]")
    for p in (1, 2, 3):
        xi = np.linspace(-1.0, 1.0, p + 1)
        phi = lagrange_basis(xi, xi)
        xg, wg = gl(12)
        s = 0.5 * (xg + 1.0)
        unity = lagrange_basis(xi, xg).sum(axis=0)
        dsum = dlagrange_basis(xi, np.array([0.0])).sum()
        h = 0.25
        nodal = U_EXACT(np.linspace(0.0, h, p + 1))
        uh = nodal @ lagrange_basis(xi, xg)
        err_int = np.max(np.abs(uh - U_EXACT(h * s)))
        print(f"  p = {p}: nodes xi = {np.round(xi, 3)}")
        print(f"          Kronecker residual max|phi_j(x_i) - delta_ij| = "
              f"{np.max(np.abs(phi - np.eye(p + 1))):.2f}")
        print(f"          partition of unity max|sum_j phi_j - 1| = "
              f"{np.max(np.abs(unity - 1.0)):.2e}; sum_j phi_j'(0) = {abs(dsum):.2e}")
        print(f"          interpolation error of sin(pi x) on one h = 0.25 m "
              f"element: {err_int:.3e}")

    section("2. Gauss-Legendre exactness: measured, and where it fails")
    print("  n-point Gauss-Legendre is exact for polynomials of degree <= 2n-1.")
    print("     n     error, degree 2n-1    error, degree 2n   measured order of")
    print("             (exact: 0)         (exact: 2/(2n+1))   the 2n-degree error")
    prev = None
    for n in (1, 2, 3, 4, 5, 8):
        xg, wg = gl(n)
        d_ok = 2 * n - 1
        e_ok = abs(np.sum(wg * xg ** d_ok))                      # exact value 0
        d_bad = 2 * n
        e_bad = abs(np.sum(wg * xg ** d_bad) - 2.0 / (d_bad + 1))
        ratio = "" if prev is None else f"{np.log2(prev / e_bad):14.2f}"
        print(f"  {n:4d}   {e_ok:22.3e}   {e_bad:19.3e}   {ratio}")
        prev = e_bad
    print("  The odd-degree column is round-off; the even-degree column is the first")
    print("  degree the rule cannot integrate exactly.  Its error falls by about 4x")
    print("  per doubling of the rule's internal order, i.e. the rule still converges")
    print("  on smooth integrands -- it is simply no longer exact.")

    section("3. Element matrices: symmetry, definiteness and conditioning")
    ke, me = element_matrices(1, 0.125, 0.0, lambda x: np.ones_like(x))
    print("  P1 element, a = 1, h = 0.125 m: Ke = (1/h)[[1,-1],[-1,1]], "
          "Me = (h/6)[[2,1],[1,2]]")
    print(f"  max|Ke - Ke^T| = {np.max(np.abs(ke - ke.T)):.2e}; "
          f"eigenvalues of Ke = {np.round(np.linalg.eigvalsh(ke), 4)}")
    print(f"  max|Me - Me^T| = {np.max(np.abs(me - me.T)):.2e}; "
          f"eigenvalues of Me = {np.round(np.linalg.eigvalsh(me), 6)}")
    print("  Ke is positive semidefinite with one zero eigenvalue (the constant")
    print("  mode carries no energy); Me is positive definite.")
    print("\n  Condition number of the element mass matrix versus node choice:")
    print("       p     equally spaced nodes       Gauss-Lobatto nodes")
    for p in (2, 4, 6, 8, 10):
        out = []
        xg, wg = gl(p + 4)
        for xi in (np.linspace(-1.0, 1.0, p + 1), gll_nodes(p)):
            phi = lagrange_basis(xi, xg)
            m = 2.0 * (phi * wg[None, :]) @ phi.T
            out.append(np.linalg.cond(m))
        print(f"  {p:5d}   {out[0]:22.3e}   {out[1]:22.3e}")
    print("  Equally spaced nodes lose conditioning quickly; Gauss-Lobatto nodes")
    print("  stay usable, which is why spectral elements use them (lesson 03).")

    section("4. h-refinement for polynomial order p = 1, 2, 3")
    print("  -u'' = pi^2 sin(pi x), u(0) = u(1) = 0, exact u = sin(pi x)")
    print("     p   n_elem    ndof      L2 error     order       H1 error    order")
    for p in (1, 2, 3):
        hs, l2s, h1s = [], [], []
        prev = None
        for n_elem in (2, 4, 8, 16, 32, 64):
            u, _, _ = assemble(p, n_elem, lambda x: np.ones_like(x), F_SOURCE)
            e2, eh1 = errors(p, n_elem, u)
            o2 = "" if prev is None else f"{np.log2(prev[0] / e2):8.3f}"
            oh = "" if prev is None else f"{np.log2(prev[1] / eh1):8.3f}"
            print(f"  {p:4d}   {n_elem:6d}   {p * n_elem + 1:5d}   {e2:11.3e}  "
                  f"{o2}   {eh1:11.3e}  {oh}")
            prev = (e2, eh1)
            hs.append(1.0 / n_elem)
            l2s.append(e2)
            h1s.append(eh1)
        print(f"       fitted: L2 order = {fit_order(hs, l2s):.3f}, "
              f"H1 order = {fit_order(hs, h1s):.3f}   (theory: p+1 and p)")
    print("\n  Smallest mesh that reaches an L2 tolerance of 1e-8:")
    for p in (1, 2, 3):
        n = 2
        while True:
            u, _, _ = assemble(p, n, lambda x: np.ones_like(x), F_SOURCE)
            e2, _ = errors(p, n, u)
            if e2 < 1e-8:
                break
            n *= 2
        print(f"  p = {p}: n_elem = {n:4d}, ndof = {p * n + 1:5d}, "
              f"L2 error = {e2:.2e}")

    section("5. Consistent versus lumped mass: eigenvalue error")
    print("  Generalised eigenproblem K v = lambda M v for -u'' on (0,1),")
    print("  u(0) = u(1) = 0; exact eigenvalues lambda_k = (k pi)^2, lambda_1 = 9.869604")
    print("   p   n_elem   consistent lambda_1    rel err      lumped lambda_1    rel err")
    for p, n_elem in ((1, 16), (1, 64), (2, 16), (3, 8)):
        h = 1.0 / n_elem
        ndof = p * n_elem + 1
        K = np.zeros((ndof, ndof))
        M = np.zeros((ndof, ndof))
        for e in range(n_elem):
            ke, me = element_matrices(p, h, e * h, lambda x: np.ones_like(x))
            idx = e * p + np.arange(p + 1)
            K[np.ix_(idx, idx)] += ke
            M[np.ix_(idx, idx)] += me
        K = K[1:-1, 1:-1]
        M = M[1:-1, 1:-1]
        lam_c = sla.eigh(K, M, eigvals_only=True)[0]
        lam_l = sla.eigh(K, np.diag(M.sum(axis=1)), eigvals_only=True)[0]
        print(f"  {p:2d}   {n_elem:6d}   {lam_c:18.6f}   {(lam_c / np.pi**2 - 1):+9.2e}   "
              f"{lam_l:18.6f}   {(lam_l / np.pi**2 - 1):+9.2e}")
    print("  Lumping is row-sum under-integration of the mass matrix.  It makes M")
    print("  diagonal (cheap explicit time stepping) but changes the eigenvalue")
    print("  error and its sign: both sequences converge, to different constants.")

    section("6. Quadrature order required by a variable coefficient")
    print("  P2 element, h = 0.25 m, a(x) = 1 + 0.5 x (degree 1).  The reference")
    print("  is a 12-point rule, exact for this integrand.")
    a_fun = lambda x: 1.0 + 0.5 * x
    ke_ref, me_ref = element_matrices(2, 0.25, 0.0, a_fun, n_q=12)
    print("   n_q   max|Ke - Ke_ref|   max|Me - Me_ref|")
    for n_q in (1, 2, 3, 4):
        ke, me = element_matrices(2, 0.25, 0.0, a_fun, n_q=n_q)
        print(f"  {n_q:4d}   {np.max(np.abs(ke - ke_ref)):.3e}   "
              f"{np.max(np.abs(me - me_ref)):.3e}")
    print("  With a degree-1 coefficient the stiffness integrand has degree 2p-1,")
    print("  so p+1 points suffice; the mass integrand has degree 2p, so p+2 do.")
    print("  Choosing the rule from the element order and the coefficient degree is")
    print("  the whole of quadrature policy.")
    print("\nAll numbers are printed by this script; the model is SYNTHETIC.")


if __name__ == "__main__":
    main()
