#!/usr/bin/env python3
"""Finite element and finite volume discretisation for geodynamics: convergence
orders, the inf-sup (LBB) condition for Stokes elements, and the measured
numerical diffusion of upwind fluxes.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python finite_element_geodynamics_demo.py

Everything is SYNTHETIC: the problems below are chosen teaching problems with
analytic solutions, not geological data.  No number is quoted from a published
model; every printed value is computed here.

Contents
--------
1. 1-D Poisson, P1 elements: measured L2/H1 convergence orders, and the
   nodal-exactness property of the 1-D Galerkin solution.
2. The inf-sup constant of Q1-Q1 and Q2-P1 Stokes elements on a structured
   mesh, measured as a function of mesh size; and the effect of pressure
   stabilisation.
3. Steady advection-diffusion by finite volume: central versus upwind flux,
   measured overshoot, and the exact upwind numerical-diffusion identity
   D_num = |u| h / 2.
4. Discrete conservation: flux form versus advective form in a periodic domain.
"""

import numpy as np
import scipy.linalg as sla

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ---------------------------------------------------------------------------
# 1. 1-D Poisson with P1 elements
# ---------------------------------------------------------------------------

def p1_poisson_1d(n_elem, lumped=False):
    """Solve -u'' = f on (0,1), u(0)=u(1)=0, P1 elements on a uniform mesh.

    Manufactured solution u = sin(pi x), so f = pi^2 sin(pi x).
    Returns the node coordinates and the discrete node values.
    """
    h = 1.0 / n_elem
    x = np.linspace(0.0, 1.0, n_elem + 1)
    ndof = n_elem - 1                      # interior nodes only
    A = np.zeros((ndof, ndof))
    b = np.zeros(ndof)
    f = lambda t: np.pi ** 2 * np.sin(np.pi * t)
    for e in range(n_elem):
        xl, xr = x[e], x[e + 1]
        # element stiffness (1/h) * [[1,-1],[-1,1]]
        ke = np.array([[1.0, -1.0], [-1.0, 1.0]]) / h
        if lumped:
            fe = np.array([f(xl), f(xr)]) * h / 2.0
        else:
            # exact integration of f against linear hat functions (Simpson rule)
            fe = np.array([(f(xl) + 2.0 * f((xl + xr) / 2.0)) * h / 6.0,
                           (2.0 * f((xl + xr) / 2.0) + f(xr)) * h / 6.0])
        gdof = [e - 1, e]                  # -1 marks an eliminated boundary dof
        for i in range(2):
            if gdof[i] < 0 or gdof[i] >= ndof:
                continue
            b[gdof[i]] += fe[i]
            for j in range(2):
                if gdof[j] < 0 or gdof[j] >= ndof:
                    continue
                A[gdof[i], gdof[j]] += ke[i, j]
    u = np.linalg.solve(A, b)
    return x, np.concatenate(([0.0], u, [0.0]))


def l2_h1_errors(x, u, exact, dexact):
    """Discrete L2 and H1 seminorm errors of a piecewise-linear function."""
    h = x[1] - x[0]
    xm = 0.5 * (x[:-1] + x[1:])
    um = 0.5 * (u[:-1] + u[1:])
    e2 = np.sum((um - exact(xm)) ** 2) * h
    g = np.diff(u) / h
    e1 = np.sum((g - dexact(xm)) ** 2) * h
    return np.sqrt(e2), np.sqrt(e1)


def demonstration_1():
    section("1. 1-D Poisson, P1 elements: manufactured solution u = sin(pi x)")
    exact = lambda t: np.sin(np.pi * t)
    dexact = lambda t: np.pi * np.cos(np.pi * t)
    ns = [8, 16, 32, 64, 128]
    print("  exact load integration (Simpson quadrature of the load vector)")
    print("    n_elem    h        L2 error    order     H1 error    order")
    prev = None
    for n in ns:
        x, u = p1_poisson_1d(n)
        e2, e1 = l2_h1_errors(x, u, exact, dexact)
        o2 = "" if prev is None else f"{np.log2(prev[0] / e2):8.3f}"
        o1 = "" if prev is None else f"{np.log2(prev[1] / e1):8.3f}"
        print(f"    {n:6d}  {1.0/n:8.5f}  {e2:10.3e}  {o2:>6s}  {e1:10.3e}  {o1:>6s}")
        prev = (e2, e1)
    x, u = p1_poisson_1d(64)
    print(f"  maximum error of the nodal values at n = 64: "
          f"{np.max(np.abs(u - exact(x))):.3e}")
    print("  (with the load integrated exactly, the 1-D P1 Galerkin solution is")
    print("   nodally exact, so the L2 error is pure interpolation error and the")
    print("   nodal residual above is the error of the load quadrature.)")
    print()
    print("  nodal (lumped) load quadrature for comparison")
    print("    n_elem    h        L2 error    order     max nodal error")
    prev = None
    for n in ns:
        x, u = p1_poisson_1d(n, lumped=True)
        e2, _ = l2_h1_errors(x, u, exact, dexact)
        o2 = "" if prev is None else f"{np.log2(prev / e2):8.3f}"
        print(f"    {n:6d}  {1.0/n:8.5f}  {e2:10.3e}  {o2:>6s}  "
              f"{np.max(np.abs(u - exact(x))):10.3e}")
        prev = e2


# ---------------------------------------------------------------------------
# 2. Inf-sup (LBB) constant for Stokes elements on quads
# ---------------------------------------------------------------------------

def lagrange_1d(p):
    """Nodes, basis values and basis derivatives for 1-D Lagrange on [-1,1]."""
    if p == 1:
        nodes = np.array([-1.0, 1.0])
    elif p == 2:
        nodes = np.array([-1.0, 0.0, 1.0])
    else:
        raise ValueError("p must be 1 or 2")
    def phi(a, xi):
        out = np.ones_like(np.asarray(xi, dtype=float))
        for b in range(p + 1):
            if b != a:
                out = out * (xi - nodes[b]) / (nodes[a] - nodes[b])
        return out
    def dphi(a, xi):
        out = np.zeros_like(np.asarray(xi, dtype=float))
        for c in range(p + 1):
            if c == a:
                continue
            term = np.ones_like(np.asarray(xi, dtype=float))
            for b in range(p + 1):
                if b != a and b != c:
                    term = term * (xi - nodes[b]) / (nodes[a] - nodes[b])
            out = out + term / (nodes[a] - nodes[c])
        return out
    return nodes, phi, dphi


def quad_grid(p):
    """Gauss-Legendre points and weights sufficient for degree 2p+1."""
    n = p + 2 if p == 1 else 3
    return np.polynomial.legendre.leggauss(n)


def mesh_nodes(p, n_elem):
    """Node coordinates of a structured quad mesh of n_elem x n_elem elements."""
    nn = p * n_elem + 1
    xs = np.linspace(0.0, 1.0, nn)
    return xs, nn


def node_index(p, n_elem, i, j):
    _, nn = mesh_nodes(p, n_elem)
    return j * nn + i


def assemble_stokes_matrices(p_v, p_p, n_elem):
    """Assemble the divergence matrix B and the velocity H1 / pressure L2 masses.

    Velocity is Q_{p_v} (two components per node), pressure is Q_{p_p}.  A full
    Dirichlet condition u = 0 is imposed on the whole boundary of the unit
    square, which removes the rigid-body and constant-velocity modes.
    """
    _, nnv = mesh_nodes(p_v, n_elem)
    _, nnp = mesh_nodes(p_p, n_elem)
    nuv_full, np_full = 2 * nnv ** 2, nnp ** 2
    h = 1.0 / n_elem
    nodes_v, phiv, dphiv = lagrange_1d(p_v)
    nodes_p, phip, _ = lagrange_1d(p_p)
    gx, gw = quad_grid(max(p_v, p_p))
    ng = len(gx)

    B = np.zeros((np_full, nuv_full))
    Mv = np.zeros((nuv_full, nuv_full))
    Mp = np.zeros((np_full, np_full))

    for ey in range(n_elem):
        for ex in range(n_elem):
            # velocity dofs: local (a_y, a_x) -> global node (i,j)
            vloc = []
            for ay in range(p_v + 1):
                for ax in range(p_v + 1):
                    i = p_v * ex + ax
                    j = p_v * ey + ay
                    base = 2 * node_index(p_v, n_elem, i, j)
                    vloc.append((base, base + 1))
            ploc = []
            for by in range(p_p + 1):
                for bx in range(p_p + 1):
                    i = p_p * ex + bx
                    j = p_p * ey + by
                    ploc.append(node_index(p_p, n_elem, i, j))

            jac = (h / 2.0) ** 2
            for qy in range(ng):
                for qx in range(ng):
                    xi, eta = gx[qx], gx[qy]
                    w = gw[qx] * gw[qy] * jac
                    # physical derivatives: d/dx = (2/h) d/dxi, d/dy = (2/h) d/deta
                    dvx = np.array([dphiv(ax, xi) * phiv(ay, eta) * (2.0 / h)
                                    for ay in range(p_v + 1) for ax in range(p_v + 1)])
                    dvy = np.array([phiv(ax, xi) * dphiv(ay, eta) * (2.0 / h)
                                    for ay in range(p_v + 1) for ax in range(p_v + 1)])
                    vv = np.array([phiv(ax, xi) * phiv(ay, eta)
                                   for ay in range(p_v + 1) for ax in range(p_v + 1)])
                    pp = np.array([phip(bx, xi) * phip(by, eta)
                                   for by in range(p_p + 1) for bx in range(p_p + 1)])
                    # B: integral of p * div(u)
                    div = np.empty(2 * len(vv))
                    div[0::2] = dvx
                    div[1::2] = dvy
                    B[np.ix_(ploc, [d for pair in vloc for d in pair])] += \
                        w * np.outer(pp, div)
                    # velocity H1 mass: gradient part + L2 part
                    g = np.zeros((len(vv), len(vv)))
                    for i in range(len(vv)):
                        g[i, :] = dvx[i] * dvx + dvy[i] * dvy
                    m = np.outer(vv, vv)
                    for i, (bi, _) in enumerate(vloc):
                        for j, (bj, _) in enumerate(vloc):
                            Mv[bi, bj] += w * (g[i, j] + m[i, j])
                            Mv[bi + 1, bj + 1] += w * (g[i, j] + m[i, j])
                    Mp[np.ix_(ploc, ploc)] += w * np.outer(pp, pp)

    # eliminate velocity dofs on the boundary of the unit square
    keep_v = []
    for j in range(nnv):
        for i in range(nnv):
            if 0 < i < nnv - 1 and 0 < j < nnv - 1:
                keep_v.extend([2 * node_index(p_v, n_elem, i, j),
                               2 * node_index(p_v, n_elem, i, j) + 1])
    B = B[:, keep_v]
    Mv = Mv[np.ix_(keep_v, keep_v)]
    return B, Mv, Mp


def infsup_constant(p_v, p_p, n_elem, eps=0.0):
    """Measured inf-sup constant and the number of pressure modes with lambda~0.

    beta_h^2 is the smallest generalised eigenvalue of
    (B Mv^-1 B^T) x = lambda Mp x.  The constant pressure mode always gives
    lambda = 0; any further near-zero mode is a spurious (checkerboard) mode.
    """
    B, Mv, Mp = assemble_stokes_matrices(p_v, p_p, n_elem)
    K = B @ sla.solve(Mv, B.T, assume_a="pos")
    if eps > 0.0:
        # pressure Laplacian (Brezzi-Pitkaranta style stabilisation)
        nps = Mp.shape[0]
        L = np.zeros_like(K)
        nodes_p, phip, dphip = lagrange_1d(p_p)
        gx, gw = quad_grid(p_p)
        h = 1.0 / n_elem
        _, nnp = mesh_nodes(p_p, n_elem)
        for ey in range(n_elem):
            for ex in range(n_elem):
                ploc = [node_index(p_p, n_elem, p_p * ex + bx, p_p * ey + by)
                        for by in range(p_p + 1) for bx in range(p_p + 1)]
                jac = (h / 2.0) ** 2
                for qy in range(len(gx)):
                    for qx in range(len(gx)):
                        xi, eta = gx[qx], gx[qy]
                        w = gw[qx] * gw[qy] * jac
                        dpx = np.array([dphip(bx, xi) * phip(by, eta) * (2.0 / h)
                                        for by in range(p_p + 1) for bx in range(p_p + 1)])
                        dpy = np.array([phip(bx, xi) * dphip(by, eta) * (2.0 / h)
                                        for by in range(p_p + 1) for bx in range(p_p + 1)])
                        G = np.outer(dpx, dpx) + np.outer(dpy, dpy)
                        L[np.ix_(ploc, ploc)] += w * G
        K = K + eps * h * h * L
    lam = sla.eigvalsh(K, Mp)
    lam = np.sort(lam)
    lam_ref = lam.max()
    n_zero = int(np.sum(lam < 1e-9 * lam_ref))
    lam_nz = lam[lam >= 1e-9 * lam_ref]
    beta = np.sqrt(lam_nz[0] / lam_ref) / np.sqrt(lam[-1] / lam_ref) * 1.0 \
        if lam_nz.size else np.nan
    return np.sqrt(lam_nz[0]), n_zero, lam_ref, beta


def demonstration_2():
    section("2. Inf-sup (LBB) constant of Stokes elements, measured on a square mesh")
    print("  beta_h = sqrt(smallest positive generalised eigenvalue of")
    print("           B Mv^-1 B^T x = lambda Mp x);  velocity u = 0 on the boundary")
    print("\n  Q1 velocity / Q1 pressure (equal order, not LBB stable)")
    print("    n_elem   ndof_u   ndof_p   beta_h        near-zero modes")
    q1 = {}
    for n in (4, 6, 8, 12):
        b, nz, lref, _ = infsup_constant(1, 1, n)
        ndof_v = 2 * (n - 1) ** 2
        ndof_p = (n + 1) ** 2
        q1[n] = b
        print(f"    {n:6d}   {ndof_v:6d}   {ndof_p:6d}   {b:12.5e}   {nz:4d}")
    rate = np.polyfit(np.log([1.0 / n for n in q1]), np.log(list(q1.values())), 1)[0]
    print(f"    observed decay of beta_h with h: beta_h ~ h^{rate:.3f}")
    print("\n  Q2 velocity / P1 pressure (Taylor-Hood, LBB stable for Stokes)")
    print("    n_elem   ndof_u   ndof_p   beta_h        near-zero modes")
    for n in (4, 6, 8, 12):
        b, nz, lref, _ = infsup_constant(2, 1, n)
        ndof_v = 2 * (2 * n - 1) ** 2
        print(f"    {n:6d}   {ndof_v:6d}   {ndof_p if False else (n+1)**2:6d}   "
              f"{b:12.5e}   {nz:4d}")
    print("\n  Q1/Q1 with a pressure-Laplacian stabilisation, eps = 1.0 (term")
    print("  eps*h^2 * integral(grad p . grad q) added to the pressure operator)")
    print("    n_elem   beta_h        near-zero modes (stabilised)")
    for n in (4, 8, 12):
        b, nz, lref, _ = infsup_constant(1, 1, n, eps=1.0)
        print(f"    {n:6d}   {b:12.5e}   {nz:4d}")

    # assembly verification with a random discrete pressure: the constant mode
    # must be annihilated and a random mode must not be.
    B, Mv, Mp = assemble_stokes_matrices(1, 1, 6)
    one = np.ones(Mp.shape[0])
    u = sla.solve(Mv, B.T @ one, assume_a="pos")
    print(f"\n  assembly check: ||Mv^-1 B^T 1||_inf for the constant pressure = "
          f"{np.max(np.abs(u)):.3e}")
    p_rand = RNG.standard_normal(Mp.shape[0])
    u2 = sla.solve(Mv, B.T @ p_rand, assume_a="pos")
    print(f"  assembly check: ||Mv^-1 B^T p_random||_inf = "
          f"{np.max(np.abs(u2)):.3e}  (must not vanish)")


# ---------------------------------------------------------------------------
# 3. Steady advection-diffusion by finite volume: central versus upwind
# ---------------------------------------------------------------------------

def fv_dirichlet(n_cell, Pe, scheme):
    """Steady u T' = D T'' on (0,1), T(0)=0, T(1)=1, cell-centred finite volume.

    Boundary faces carry the Dirichlet values with the physical D; interior
    faces use the arithmetic mean of the two cell values (central scheme) or the
    value on the upwind side, written as central advection plus the diffusion
    |u| h / 2 (upwind scheme).  Returns cell centres and the solution.
    """
    h = 1.0 / n_cell
    xc = (np.arange(n_cell) + 0.5) * h
    D = 1.0 / Pe
    Df = D + (0.5 * h if scheme == "upwind" else 0.0)
    A = np.zeros((n_cell, n_cell))
    c = np.zeros(n_cell)
    for i in range(n_cell):
        if i == 0:
            A[i, i] += 2.0 * D / h ** 2                    # -F_left / h
        else:
            A[i, i] += Df / h ** 2 - 0.5 / h
            A[i, i - 1] += -Df / h ** 2 - 0.5 / h
        if i == n_cell - 1:
            A[i, i] += 2.0 * D / h ** 2                    # +F_right / h
            c[i] += 1.0 / h - 2.0 * D / h ** 2             # outlet value T(1)=1
        else:
            A[i, i] += 0.5 / h + Df / h ** 2
            A[i, i + 1] += 0.5 / h - Df / h ** 2
    return xc, np.linalg.solve(A, -c)


def periodic_operator(n_cell, Pe, scheme):
    """Discrete operator of the periodic advection-diffusion problem (matrix only).

    Equation: u T' - D T'' = f on a unit periodic domain with u = 1.  The
    scheme changes only the face diffusion coefficient: D (central) or
    D + |u| h / 2 (upwind).  The returned matrix maps the cell values of T to
    the cell values of u T' - D T''.
    """
    h = 1.0 / n_cell
    D = 1.0 / Pe
    Df = D + (0.5 * h if scheme == "upwind" else 0.0)
    A = np.zeros((n_cell, n_cell))
    for i in range(n_cell):
        iL, iR = (i - 1) % n_cell, (i + 1) % n_cell
        A[i, i] += (-0.5 + Df / h) / h
        A[i, iL] += (-0.5 - Df / h) / h
        A[i, i] += (0.5 + Df / h) / h
        A[i, iR] += (0.5 - Df / h) / h
    return A


def fv_periodic(n_cell, Pe, scheme):
    """Solve the periodic problem with the manufactured solution T = sin(2 pi x)."""
    h = 1.0 / n_cell
    xc = (np.arange(n_cell) + 0.5) * h
    D = 1.0 / Pe
    k = 2.0 * np.pi
    A = periodic_operator(n_cell, Pe, scheme)
    f = k * np.cos(k * xc) + D * k ** 2 * np.sin(k * xc)
    T = np.linalg.lstsq(A, f, rcond=None)[0]      # zero-mean (minimum norm)
    return xc, T


def fd_dirichlet(n_node, Pe, scheme):
    """Vertex-centred finite differences: u T' = D T'' on (0,1), T(0)=0, T(1)=1.

    The boundary nodes carry the Dirichlet data exactly, so any overshoot appears
    in the interior.  ``scheme`` is "central" or "upwind".  Returns the interior
    node coordinates and the full solution including the boundary values.
    """
    h = 1.0 / n_node
    D = 1.0 / Pe
    N = n_node - 1
    A = np.zeros((N, N))
    b = np.zeros(N)
    for i in range(N):
        A[i, i] += 2.0 * D / h ** 2
        if i - 1 >= 0:
            A[i, i - 1] += -D / h ** 2
        if i + 1 < N:
            A[i, i + 1] += -D / h ** 2
        else:
            b[i] += D / h ** 2                       # outlet node T(1) = 1
        if scheme == "central":
            if i - 1 >= 0:
                A[i, i - 1] += -0.5 / h
            if i + 1 < N:
                A[i, i + 1] += 0.5 / h
            else:
                b[i] += 0.5 / h                      # outlet node T(1) = 1
        else:
            A[i, i] += 1.0 / h
            if i - 1 >= 0:
                A[i, i - 1] += -1.0 / h
    T = np.concatenate(([0.0], np.linalg.solve(A, b), [1.0]))
    x = np.linspace(0.0, 1.0, n_node + 1)
    return x, T


def demonstration_3():
    section("3. Advection-diffusion: upwinding and the cell-Peclet limit")
    exact = lambda t, P: (np.exp(P * t) - 1.0) / (np.exp(P) - 1.0)
    print("\n  Part A: vertex-centred differences on u T' = D T'' in (0,1),")
    print("  T(0) = 0, T(1) = 1, n_node = 40 intervals, Pe = u L / D;")
    print("  cell Peclet number = Pe h.  Exact solution (exp(Pe x)-1)/(exp(Pe)-1).\n")
    print("   Pe    Pe h   scheme    Linf error   non-monotone amplitude")
    print("                                       max(0, max(T)-1, -min(T))")
    for Pe in (1.0, 5.0, 20.0, 100.0):
        for scheme in ("central", "upwind"):
            x, T = fd_dirichlet(40, Pe, scheme)
            err = np.max(np.abs(T - exact(x, Pe)))
            over = max(0.0, T.max() - 1.0, -T.min())
            print(f"  {Pe:5.0f}  {Pe / 40:6.2f}  {scheme:8s}  {err:11.4e}   "
                  f"{over:10.4e}")
    print("\n  Part A2: the central scheme loses monotonicity when the cell Peclet")
    print("  number exceeds 2; the upwind scheme never overshoots.")
    print("   Pe    Pe h   central non-monotone amplitude   central Linf   upwind Linf")
    for Pe in (40.0, 60.0, 80.0, 100.0, 120.0, 200.0):
        x, Tc = fd_dirichlet(40, Pe, "central")
        _, Tu = fd_dirichlet(40, Pe, "upwind")
        over = max(0.0, Tc.max() - 1.0, -Tc.min())
        print(f"  {Pe:5.0f}  {Pe / 40:6.2f}  {over:29.4e}   "
              f"{np.max(np.abs(Tc - exact(x, Pe))):11.4e}   "
              f"{np.max(np.abs(Tu - exact(x, Pe))):11.4e}")
    lo, hi = 0.0, 400.0
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        _, Tm = fd_dirichlet(40, mid, "central")
        if max(0.0, Tm.max() - 1.0, -Tm.min()) < 1e-10:
            lo = mid
        else:
            hi = mid
    print(f"  measured threshold, by bisection on the non-monotone amplitude: "
          f"cell Peclet = {0.5 * (lo + hi) / 40:.3f}")
    print("  (the classical threshold for central differencing is exactly 2)")
    print("\n  Part A3: convergence at Pe = 20 (cell Peclet 0.5 at n = 40)")
    print("    n_node   central error  order     upwind error   order")
    prevc = prevu = None
    for n in (10, 20, 40, 80, 160):
        x, Tc = fd_dirichlet(n, 20.0, "central")
        _, Tu = fd_dirichlet(n, 20.0, "upwind")
        ec = np.max(np.abs(Tc - exact(x, 20.0)))
        eu = np.max(np.abs(Tu - exact(x, 20.0)))
        oc = "" if prevc is None else f"{np.log2(prevc / ec):7.3f}"
        ou = "" if prevu is None else f"{np.log2(prevu / eu):7.3f}"
        print(f"    {n:6d}   {ec:12.4e}  {oc:>7s}    {eu:12.4e}  {ou:>7s}")
        prevc, prevu = ec, eu

    print("\n  Part B: periodic problem (no boundary treatment), manufactured")
    print("  solution T = sin(2 pi x), u = 1, D = 1/Pe.  Here the discretisations")
    print("  can be compared as operators.")
    print("\n  exact discrete identity: the upwind operator with diffusion D is")
    print("  identical to the central operator with D_eff = D + |u| h / 2.")
    print("   n_cell   max|A_upwind(D) - A_central(D + u h/2)|")
    for n in (10, 20, 40, 80, 160):
        Pe = 20.0
        A_up = periodic_operator(n, Pe, "upwind")
        peff = Pe / (1.0 + Pe * (1.0 / n) / 2.0)
        A_cen = periodic_operator(n, peff, "central")
        print(f"   {n:6d}   {np.max(np.abs(A_up - A_cen)):11.3e}")
    print("\n  and the same two schemes on the same smooth solution show the")
    print("  standard orders of accuracy (upwind numerical diffusion is O(h))")
    print("    n_cell   central error  order     upwind error   order")
    prevc = prevu = None
    k = 2.0 * np.pi
    for n in (5, 10, 20, 40, 80):
        xc, Tc = fv_periodic(n, 20.0, "central")
        _, Tu = fv_periodic(n, 20.0, "upwind")
        ec = np.max(np.abs(Tc - np.sin(k * xc)))
        eu = np.max(np.abs(Tu - np.sin(k * xc)))
        oc = "" if prevc is None else f"{np.log2(prevc / ec):7.3f}"
        ou = "" if prevu is None else f"{np.log2(prevu / eu):7.3f}"
        print(f"    {n:6d}   {ec:12.4e}  {oc:>7s}    {eu:12.4e}  {ou:>7s}")
        prevc, prevu = ec, eu


# ---------------------------------------------------------------------------
# 4. Discrete conservation
# ---------------------------------------------------------------------------

def demonstration_4():
    section("4. Discrete conservation: flux form versus advective form")
    n = 200
    h = 1.0 / n
    xc = (np.arange(n) + 0.5) * h
    xf = np.arange(n) * h
    u_cell = 1.0 + 0.5 * np.sin(2.0 * np.pi * xc)
    u_face = 1.0 + 0.5 * np.sin(2.0 * np.pi * xf)
    T0 = np.exp(-((xc - 0.5) ** 2) / (2.0 * 0.05 ** 2))
    dt = 0.25 * h / np.max(np.abs(u_cell))
    n_step = 4000

    def run(mode):
        T = T0.copy()
        for _ in range(n_step):
            if mode == "flux":
                ul = np.roll(u_face, 1)                  # velocity on the left face
                Fl = np.where(ul > 0.0, ul * np.roll(T, 1), ul * T)
                Fr = np.where(u_face > 0.0, u_face * T, u_face * np.roll(T, -1))
                T = T - dt / h * (Fr - Fl)
            else:
                # upwind advective form (stable, but not conservative)
                T = T - dt * u_cell * (T - np.roll(T, 1)) / h
        return T

    for mode in ("flux", "advective"):
        T = run(mode)
        m0, m1 = np.sum(T0) * h, np.sum(T) * h
        print(f"  {mode:10s} form: total = {m1:.12f}, initial = {m0:.12f}, "
              f"relative drift = {abs(m1 - m0) / m0:.3e}")
    print(f"  {n_step} steps, dt = {dt:.3e} (time units), maximum Courant number "
          f"= {np.max(np.abs(u_cell)) * dt / h:.3f}")
    print("  The flux form sums to a telescoping series over periodic faces, so the")
    print("  total is conserved to rounding; the advective form has no such identity.")


def main():
    demonstration_1()
    demonstration_2()
    demonstration_3()
    demonstration_4()
    print("\nAll results above are SYNTHETIC teaching computations.")


if __name__ == "__main__":
    main()
