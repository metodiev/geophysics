#!/usr/bin/env python3
"""Weak formulation and the Galerkin method: 1-D Poisson assembled by hand.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fem_weak_form_demo.py

Everything here is SYNTHETIC: the coefficients and right-hand sides are chosen
teaching models, not measurements.  No external FEM package is used; the
stiffness and mass matrices are integrated with Gauss-Legendre quadrature and
the resulting sparse system is solved with SciPy.

Contents
--------
1. Element stiffness/mass matrices against their closed forms.
2. Manufactured solution -u'' = f: measured L2, H1 and nodal convergence.
3. Natural (Neumann) boundary term imposed weakly.
4. Cea's lemma: Galerkin error <= interpolant error in the energy norm.
5. Variable coefficient -(a u')' = f: FEM versus naive finite differences.
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC model problem: -(a(x) u')' = f on (0,1), u(0) = 0 ------------
A0, A1 = 1.0, 1.5          # a(x) = A0 + A1 x, dimensionless
N_GAUSS = 10               # Gauss-Legendre order used for element integrals


def gauss_legendre(n):
    """Nodes and weights of n-point Gauss-Legendre quadrature on [-1, 1]."""
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w


XI, WI = gauss_legendre(N_GAUSS)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ---------------------------------------------------------------------------
# Reference-element quantities.  On [0,1] with linear (P1) shape functions
#     phi_0(s) = 1 - s,   phi_1(s) = s,   s in [0,1],
# the element matrices are  Ke_ij = a_mid * (1/h) * [[1,-1],[-1,1]]  for
# constant a, and  Me_ij = (h/6)*[[2,1],[1,2]].
# ---------------------------------------------------------------------------

def p1_element_matrices(h, a_fun, x_left, n_gauss=N_GAUSS):
    """P1 element stiffness and mass matrices for coefficient a(x) on [x_left, x_left+h].

    All integrals are evaluated on the parent interval s in [0,1] with
    ds = h dx_parent, so dx = h ds.
    """
    s = 0.5 * (XI + 1.0)                 # map [-1,1] -> [0,1]
    w = 0.5 * WI                         # matching weights
    x = x_left + h * s
    a = a_fun(x)
    dphi = np.array([-np.ones_like(s), np.ones_like(s)]) / h      # dphi/dx
    phi = np.array([1.0 - s, s])
    ke = np.empty((2, 2))
    me = np.empty((2, 2))
    for i in range(2):
        for j in range(2):
            ke[i, j] = h * np.sum(w * a * dphi[i] * dphi[j])
            me[i, j] = h * np.sum(w * a * phi[i] * phi[j])
    return ke, me


def p1_load(h, x_left, f_fun):
    """Right-hand side integral int f phi_i dx over one element."""
    s = 0.5 * (XI + 1.0)
    w = 0.5 * WI
    x = x_left + h * s
    fv = f_fun(x)
    return np.array([h * np.sum(w * fv * (1.0 - s)), h * np.sum(w * fv * s)])


def assemble_poisson(n_elem, a_fun, f_fun, u_left=0.0, u_right=None,
                     load_right=None):
    """Assemble and solve the P1 Galerkin system on a uniform mesh.

    Degrees of freedom are the nodal values at x = 0, h, ..., 1.  The Dirichlet
    value at x = 0 is always eliminated.  At x = 1 either

    * ``u_right`` is given and the node is eliminated as a Dirichlet value, or
    * ``u_right`` is None and the node is left free, which imposes the *natural*
      condition u'(1) = 0, plus an optional Neumann datum ``load_right`` = g so
      that the natural condition reads u'(1) = g.

    The distinction is not cosmetic: with u(0) = 0 and a natural condition at
    x = 1 the problem is a different problem, and Section 2c measures the
    difference.
    """
    h = 1.0 / n_elem
    ndof = n_elem + 1
    K = np.zeros((ndof, ndof))
    F = np.zeros(ndof)
    X = np.linspace(0.0, 1.0, ndof)
    for e in range(n_elem):
        ke, _ = p1_element_matrices(h, a_fun, X[e])
        fe = p1_load(h, X[e], f_fun)
        idx = np.array([e, e + 1])
        K[np.ix_(idx, idx)] += ke
        F[idx] += fe
    F = F - K[:, 0] * u_left
    if u_right is None:
        if load_right is not None:
            F[-1] += load_right
        Kr = K[1:, 1:]
        Fr = F[1:]
    else:
        F = F - K[:, -1] * u_right
        Kr = K[1:-1, 1:-1]
        Fr = F[1:-1]
    u = np.empty(ndof)
    u[0] = u_left
    if u_right is None:
        u[1:] = np.linalg.solve(Kr, Fr)
    else:
        u[-1] = u_right
        u[1:-1] = np.linalg.solve(Kr, Fr)
    return X, u, K, F


def l2_h1_errors(X, u, u_exact, du_exact):
    """L2 and H1-seminorm errors of a P1 field, integrated with 10-pt Gauss."""
    h = X[1] - X[0]
    s = 0.5 * (XI + 1.0)
    w = 0.5 * WI
    err2 = errh1 = 0.0
    for e in range(X.size - 1):
        x = X[e] + h * s
        ue = u[e] * (1 - s) + u[e + 1] * s
        due = (u[e + 1] - u[e]) / h
        err2 += h * np.sum(w * (ue - u_exact(x)) ** 2)
        errh1 += h * np.sum(w * (due - du_exact(x)) ** 2)
    return np.sqrt(err2), np.sqrt(errh1)


def conv_rates(levels, errors):
    """Least-squares order of accuracy from a log-log refinement study.

    Implemented from the normal equations rather than ``np.polyfit`` because
    the installed NumPy raises ``LinAlgError: SVD did not converge`` for this
    small closed-form fit.
    """
    x = np.asarray(levels, dtype=float)
    y = np.asarray(errors, dtype=float)
    dx = x - x.mean()
    return float(np.sum(dx * (y - y.mean())) / np.sum(dx * dx))


def main():
    section("1. Element matrices against closed forms (SYNTHETIC, dimensionless)")
    a_const = lambda x: np.ones_like(x)
    for n_elem in (4, 40):
        h = 1.0 / n_elem
        ke, me = p1_element_matrices(h, a_const, 0.0)
        ke_exact = np.array([[1.0, -1.0], [-1.0, 1.0]]) / h
        me_exact = (h / 6.0) * np.array([[2.0, 1.0], [1.0, 2.0]])
        print(f"  h = {h:.4f}:  max|Ke - 1/h[[1,-1],[-1,1]]| = "
              f"{np.max(np.abs(ke - ke_exact)):.3e}")
        print(f"             max|Me - h/6[[2,1],[1,2]]|   = "
              f"{np.max(np.abs(me - me_exact)):.3e}")

    section("2. Manufactured solution: -u'' = pi^2 sin(pi x), u(0) = u(1) = 0")
    u_exact = lambda x: np.sin(np.pi * x)
    du_exact = lambda x: np.pi * np.cos(np.pi * x)
    f_fun = lambda x: np.pi ** 2 * np.sin(np.pi * x)
    print("  exact u(x) = sin(pi x); x in metres, u in metres")
    print("  n_elem        h         L2 error      order     H1 error     order     nodal error")
    prev = None
    L2s, H1s, nodals, hs = [], [], [], []
    for n_elem in (8, 16, 32, 64, 128, 256):
        h = 1.0 / n_elem
        X, u, _, _ = assemble_poisson(n_elem, a_const, f_fun, u_left=0.0,
                                      u_right=0.0)
        e2, eh1 = l2_h1_errors(X, u, u_exact, du_exact)
        enod = np.max(np.abs(u - u_exact(X)))
        o2 = "" if prev is None else f"{np.log2(prev[0] / e2):8.3f}"
        oh = "" if prev is None else f"{np.log2(prev[1] / eh1):8.3f}"
        print(f"  {n_elem:6d}   {h:8.5f}   {e2:11.3e}  {o2}   {eh1:10.3e}  {oh}   {enod:11.3e}")
        prev = (e2, eh1)
        L2s.append(e2)
        H1s.append(eh1)
        nodals.append(enod)
        hs.append(h)
    hs = np.array(hs)
    nodals = np.array(nodals)
    print(f"  fitted L2 order  = {conv_rates(np.log(hs), np.log(L2s)):.3f}")
    print(f"  fitted H1 order  = {conv_rates(np.log(hs), np.log(H1s)):.3f}")
    print(f"  max nodal error over the whole study = {nodals.max():.3e}")
    print("  (nodal values are reproduced to round-off: in 1-D the P1 Galerkin")
    print("   solution with exactly integrated loads is nodally exact)")

    section("2b. The same equation WITHOUT the Dirichlet condition at x = 1")
    print("  Leaving x = 1 free imposes the natural condition u'(1) = 0, i.e. a")
    print("  different problem.  Its exact solution is u = sin(pi x) + pi x,")
    print("  because -u'' is unchanged and u(1) = pi rather than 0.")
    X, u_nat, _, _ = assemble_poisson(64, a_const, f_fun, u_left=0.0, u_right=None)
    u_alt = np.sin(np.pi * X) + np.pi * X
    print(f"  n_elem = 64: max|u_h - (sin(pi x) + pi x)| = "
          f"{np.max(np.abs(u_nat - u_alt)):.3e},  u_h(1) = {u_nat[-1]:.6f} (pi = {np.pi:.6f})")

    section("3. Natural (Neumann) boundary condition imposed weakly")
    print("  Problem: -u'' = -2, u(0) = 0, u'(1) = 2  ->  exact u(x) = x^2")
    f_neu = lambda x: -2.0 * np.ones_like(x)
    u_neu = lambda x: x ** 2
    for n_elem in (4, 16):
        X, u, _, _ = assemble_poisson(n_elem, a_const, f_neu, u_left=0.0,
                                      u_right=None, load_right=2.0)
        err = np.max(np.abs(u - u_neu(X)))
        print(f"  n_elem = {n_elem:3d}: max nodal error = {err:.3e}  "
              f"(no boundary node is prescribed at x = 1)")

    section("4. Weak form, Galerkin orthogonality and Cea's lemma, measured")
    print("  Check A: the manufactured solution satisfies the weak equation")
    print("  int u' phi_j' dx = int f phi_j dx for every hat function phi_j.")
    for n_elem in (8, 32):
        h = 1.0 / n_elem
        X = np.linspace(0.0, 1.0, n_elem + 1)
        worst = 0.0
        for j in range(1, n_elem):
            lhs = rhs = 0.0
            for e in (j - 1, j):
                s = 0.5 * (XI + 1.0)
                w = 0.5 * WI
                x = X[e] + h * s
                phi = np.where(e == j - 1, s, 1.0 - s)
                dphi = np.where(e == j - 1, 1.0, -1.0) / h
                lhs += h * np.sum(w * np.pi * np.cos(np.pi * x) * dphi)
                rhs += h * np.sum(w * f_fun(x) * phi)
            worst = max(worst, abs(lhs - rhs))
        print(f"  n_elem = {n_elem:3d}: max |int u'phi' - int f phi| over all j = {worst:.3e}")
    print("\n  Check B: in 1-D the P1 solution equals the interpolant, so the")
    print("  energy-norm error equals the interpolation error (Cea with equality).")
    for n_elem in (8, 32, 128):
        X, u, _, _ = assemble_poisson(n_elem, a_const, f_fun, u_left=0.0,
                                      u_right=0.0)
        _, err_h1 = l2_h1_errors(X, u, u_exact, du_exact)
        _, err_int_h1 = l2_h1_errors(X, u_exact(X), u_exact, du_exact)
        print(f"  n_elem = {n_elem:3d}: |u_h - I_h u|_inf = "
              f"{np.max(np.abs(u - u_exact(X))):.3e}, "
              f"|u-u_h|_H1/|u-I_h u|_H1 = {err_h1 / err_int_h1:.6f}")

    section("5. Variable coefficient -(a u')' = f, a(x) = 1 + 0.5 x")
    a_fun = lambda x: A0 + A1 * x
    f_var = lambda x: (A0 + A1 * x) * np.pi ** 2 * np.sin(np.pi * x) \
        - A1 * np.pi * np.cos(np.pi * x)
    print("  exact u = sin(pi x); f = -(a u')' = a pi^2 sin(pi x) - 0.5 pi cos(pi x)")
    print("  n_elem        h         L2 error      order     H1 error     order")
    prev = None
    hs_v, l2_v, h1_v = [], [], []
    for n_elem in (8, 16, 32, 64, 128, 256):
        X, u, _, _ = assemble_poisson(n_elem, a_fun, f_var, u_left=0.0,
                                      u_right=0.0)
        e2, eh1 = l2_h1_errors(X, u, u_exact, du_exact)
        o2 = "" if prev is None else f"{np.log2(prev[0] / e2):8.3f}"
        oh = "" if prev is None else f"{np.log2(prev[1] / eh1):8.3f}"
        print(f"  {n_elem:6d}   {1.0 / n_elem:8.5f}   {e2:11.3e}  {o2}   {eh1:10.3e}  {oh}")
        prev = (e2, eh1)
        hs_v.append(1.0 / n_elem)
        l2_v.append(e2)
        h1_v.append(eh1)
    hs_v = np.array(hs_v)
    print(f"  fitted FE L2 order = {conv_rates(np.log(hs_v), np.log(l2_v)):.3f}, "
          f"H1 order = {conv_rates(np.log(hs_v), np.log(h1_v)):.3f}")

    # the naive FD scheme on the same smooth problem, for comparison
    print("\n  The same smooth problem by 3-point finite differences with")
    print("  arithmetic averaging of a at the faces (the naive FD scheme):")
    print("  n_elem        h         L2 error      order")
    prev = None
    hs_fd, l2_fd = [], []
    for n_elem in (8, 16, 32, 64, 128, 256):
        h = 1.0 / n_elem
        X = np.linspace(0.0, 1.0, n_elem + 1)
        a_face = 0.5 * (a_fun(X[:-1]) + a_fun(X[1:]))
        main_d = (a_face[:-1] + a_face[1:]) / h ** 2
        off_d = -a_face[1:-1] / h ** 2
        rhs = f_var(X[1:-1])
        A = np.diag(main_d) + np.diag(off_d, 1) + np.diag(off_d, -1)
        u = np.zeros(n_elem + 1)
        u[1:-1] = np.linalg.solve(A, rhs)
        e2, _ = l2_h1_errors(X, u, u_exact, du_exact)
        o2 = "" if prev is None else f"{np.log2(prev / e2):8.3f}"
        print(f"  {n_elem:6d}   {h:8.5f}   {e2:11.3e}  {o2}")
        prev = e2
        hs_fd.append(h)
        l2_fd.append(e2)
    print(f"  fitted naive-FD L2 order = "
          f"{conv_rates(np.log(np.array(hs_fd)), np.log(l2_fd)):.3f} "
          f"(for a smooth coefficient the naive face average is second order)")
    print("  So on a smooth coefficient the two methods agree in order; the")
    print("  difference appears when a(x) is discontinuous, which Section 6")
    print("  measures.")

    section("6. Piecewise-constant a(x): flux coupling across an interface")
    print("  -(a u')' = 0 on (0,1), u(0) = 0, u(1) = 1, a = aL for x < 1/2 and")
    print("  a = aR for x > 1/2.  Exact: u = q x for x <= 1/2 and")
    print("  u = q/2 + q (x-1/2)/ratio for x > 1/2, with ratio = aR/aL and")
    print("  q = 1/(1/2 + 1/(2 ratio)) set by u(1) = 1.  The flux q is continuous.")
    print("\n  Cell-centred two-point flux scheme, interface exactly on a face.")
    print("  The series (harmonic) face coefficient is 2 aL aR/(aL + aR); the")
    print("  arithmetic average is (aL + aR)/2.  Their ratio is")
    print("  (aL+aR)^2/(4 aL aR), which is the exact error factor of the wrong")
    print("  choice.")
    for ratio in (10.0, 1.0e6):
        q_exact = 1.0 / (0.5 + 0.5 / ratio)
        factor = (1.0 + ratio) ** 2 / (4.0 * ratio)

        def u_exact_pc(x, q=q_exact, r=ratio):
            x = np.asarray(x, dtype=float)
            return np.where(x <= 0.5, q * x, q * 0.5 + q * (x - 0.5) / r)

        print(f"\n  ratio aR/aL = {ratio:.0f}:  exact flux q = {q_exact:.9f},")
        print(f"  face-coefficient ratio arithmetic/harmonic = {factor:.6g}")
        print("  n_cell        h      harmonic error    arithmetic error   arith err/h")
        for n_cell in (8, 32, 128, 512):
            h = 1.0 / n_cell
            xc = (np.arange(n_cell) + 0.5) * h
            a_cell = np.where(xc < 0.5, 1.0, ratio)
            a_face_h = 2.0 * a_cell[:-1] * a_cell[1:] / (a_cell[:-1] + a_cell[1:])
            a_face_a = 0.5 * (a_cell[:-1] + a_cell[1:])
            errs = []
            for a_face in (a_face_h, a_face_a):
                # interior faces plus the two boundary faces.  A boundary face is
                # half a cell from its cell centre, so its conductance carries 2.
                n = n_cell
                T = np.zeros(n + 1)
                T[1:n] = a_face
                T[0] = 2.0 * a_cell[0]
                T[n] = 2.0 * a_cell[-1]
                A = np.zeros((n, n))
                b = np.zeros(n)
                for i in range(n):
                    A[i, i] = +(T[i] + T[i + 1])
                    if i > 0:
                        A[i, i - 1] = -T[i]
                    if i < n - 1:
                        A[i, i + 1] = -T[i + 1]
                b[0] += T[0] * 0.0        # Dirichlet u(0) = 0
                b[n - 1] += T[n] * 1.0    # Dirichlet u(1) = 1
                u = np.linalg.solve(A, b)
                errs.append(np.max(np.abs(u - u_exact_pc(xc))))
            print(f"  {n_cell:6d}   {h:8.5f}   {errs[0]:16.3e}   {errs[1]:16.3e}   "
                  f"{errs[1] / h:10.4f}")
    print("\n  The harmonic mean reproduces the exact piecewise-linear solution to")
    print("  round-off at every mesh, because it encodes the correct series flux.")
    print("  The arithmetic mean is only first order: its error is a fixed fraction")
    print("  of the mesh spacing whose size grows with the contrast, so refining the")
    print("  mesh does not repair a mis-modelled interface.  That asymmetry is the")
    print("  practical reason conservative flux (finite-volume) discretisation exists.")

    section("7. Sparse structure and a direct solve")
    for n_elem in (256, 4096):
        h = 1.0 / n_elem
        K = sp.diags([-1.0 / h, 2.0 / h, -1.0 / h], [-1, 0, 1],
                     shape=(n_elem - 1, n_elem - 1), format="csc")
        print(f"  n_elem = {n_elem:5d}: ndof = {n_elem - 1:5d}, nnz = {K.nnz:6d}, "
              f"nnz/ndof = {K.nnz / (n_elem - 1):.2f}, bandwidth = 3")
    n_elem = 4096
    h = 1.0 / n_elem
    K = sp.diags([-1.0 / h, 2.0 / h, -1.0 / h], [-1, 0, 1],
                 shape=(n_elem - 1, n_elem - 1), format="csc")
    b = np.ones(K.shape[0])
    lu = spla.splu(K.tocsc())
    x = lu.solve(b)
    print(f"  sparse LU solve of a {K.shape[0]}-dof system: residual "
          f"{np.linalg.norm(K @ x - b) / np.linalg.norm(b):.2e} (relative, 2-norm)")
    print(f"  max |u| = {np.max(np.abs(x)):.6e} m^2 for a unit load of 1 N/m^3")

    section("8. Randomized consistency check of nodal exactness")
    print("  Draw random amplitudes a_k and set u = sum a_k sin(k pi x),")
    print("  f = sum a_k k^2 pi^2 sin(k pi x) (RNG seed 20261014).")
    for n_elem in (16, 64):
        n_modes = 5
        amps = RNG.standard_normal(n_modes)
        ks = np.arange(1, n_modes + 1)
        u_r = lambda x: np.sum(amps[:, None] * np.sin(np.outer(ks, np.pi * x)), 0)
        f_r = lambda x: np.sum(amps[:, None] * (ks ** 2 * np.pi ** 2)[:, None]
                               * np.sin(np.outer(ks, np.pi * x)), 0)
        X, u, _, _ = assemble_poisson(n_elem, a_const, f_r, u_left=0.0,
                                      u_right=0.0)
        print(f"  n_elem = {n_elem:3d}: max nodal |u_h - u| = "
              f"{np.max(np.abs(u - u_r(X))):.3e}")
    print("\nAll numbers are printed by this script; the model is SYNTHETIC.")


if __name__ == "__main__":
    main()
