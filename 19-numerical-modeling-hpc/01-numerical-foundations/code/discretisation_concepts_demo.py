#!/usr/bin/env python3
"""Discretisation concepts: grids, nodes, cells, degrees of freedom, and the
exactly predictable error of a discrete rule.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python discretisation_concepts_demo.py

All models and data in this module are SYNTHETIC.  The functions, grids and
material contrasts below are chosen teaching values, not measurements.

Contents
--------
1. Degrees of freedom for node-centred and cell-centred grids, 1-D to 3-D.
2. Node-centred versus cell-centred storage of a two-material column.
3. Exactly predictable quadrature error: midpoint h^2/12, trapezoid h^2/6.
4. Discrete L2 norm of a grid function versus the continuous L2 norm.
5. Conditioning of the 1-D Poisson operator against its exact formula.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def dof_counts(length_km, n_cells_truncated):
    """Degrees of freedom and float64 storage for 1-D/2-D/3-D regular grids.

    A cell-centred grid of N cells per direction stores N values per direction;
    a node-centred grid stores N+1.  This factor of (1+1/N) is the whole reason
    the two conventions can be mistaken for one another on a coarse grid.
    """
    print(f"domain length = {length_km:.3f} km, N = {n_cells_truncated} per direction")
    print(f"{'grid':>22} {'nodes/cells per dir':>22} {'dof':>16} {'float64 (MiB)':>14}")
    rows = []
    for dim, name in ((1, "1-D"), (2, "2-D"), (3, "3-D")):
        for kind, per_dir, count in (
            ("node-centred", 1, (n_cells_truncated + 1) ** dim),
            ("cell-centred", 0, n_cells_truncated ** dim),
        ):
            mib = count * 8 / 1024.0 ** 2
            rows.append((f"{name} {kind}", count))
            print(f"{name + ' ' + kind:>22} {n_cells_truncated + (1 if kind == 'node-centred' else 0):>22} "
                  f"{count:>16} {mib:>14.2f}")
    h = length_km / n_cells_truncated
    print(f"cell size h = {h:.6f} km = {h * 1000.0:.3f} m in all three cases")
    return rows


def two_material_column(n_cells=40, L_km=1.0, interface_km=0.4,
                        kappa1=1.0, kappa2=4.0):
    """Steady conduction through a two-material column.

    Exact series conductance: kappa_eff = L / sum(t_i / kappa_i).  Two storage
    conventions are compared: cell-centred conductivities with a harmonic-mean
    face conductance, and node-centred conductivities averaged arithmetically
    onto the faces.
    """
    h = L_km / n_cells
    xc = (np.arange(n_cells) + 0.5) * h            # cell centres
    kappa_cell = np.where(xc < interface_km, kappa1, kappa2)
    kappa_node = np.where(np.arange(n_cells + 1) * h < interface_km, kappa1, kappa2)
    dT = 100.0                                     # K, boundary jump
    t1 = interface_km
    t2 = L_km - interface_km
    kappa_exact = L_km / (t1 / kappa1 + t2 / kappa2)
    q_exact = dT / (t1 / kappa1 + t2 / kappa2)

    # cell-centred: face conductance from the harmonic mean of neighbouring cells
    kf = 2.0 * kappa_cell[:-1] * kappa_cell[1:] / (kappa_cell[:-1] + kappa_cell[1:])
    k_up = np.empty(n_cells)
    k_dn = np.empty(n_cells)
    k_up[0] = np.nan
    k_dn[-1] = np.nan
    k_up[1:] = kf
    k_dn[:-1] = kf
    A = np.zeros((n_cells, n_cells))
    b = np.zeros(n_cells)
    for i in range(n_cells):
        if i > 0:
            A[i, i - 1] = -k_up[i] / h ** 2
            A[i, i] += k_up[i] / h ** 2
        else:
            A[i, i] += kappa_cell[0] / (0.5 * h) / h   # half-cell to the wall
            b[i] += (kappa_cell[0] / (0.5 * h) / h) * dT
        if i < n_cells - 1:
            A[i, i + 1] = -k_dn[i] / h ** 2
            A[i, i] += k_dn[i] / h ** 2
        else:
            A[i, i] += kappa_cell[-1] / (0.5 * h) / h
    T_cc = np.linalg.solve(A, b)
    q_cc = kappa_cell[0] * (dT - T_cc[0]) / (0.5 * h)

    # node-centred: arithmetic average of node values onto faces
    k_node_face = 0.5 * (kappa_node[:-1] + kappa_node[1:])
    A2 = np.zeros((n_cells + 1, n_cells + 1))
    b2 = np.zeros(n_cells + 1)
    for i in range(1, n_cells):
        A2[i, i - 1] = -k_node_face[i - 1] / h ** 2
        A2[i, i] = (k_node_face[i - 1] + k_node_face[i]) / h ** 2
        A2[i, i + 1] = -k_node_face[i] / h ** 2
    A2[0, 0] = 1.0
    b2[0] = dT
    A2[-1, -1] = 1.0
    T_nc = np.linalg.solve(A2, b2)
    q_nc = k_node_face[0] * (T_nc[0] - T_nc[1]) / h

    print(f"kappa1 = {kappa1:.2f} W/(m K) for x < {interface_km:.2f} km, "
          f"kappa2 = {kappa2:.2f} W/(m K) above")
    print(f"exact effective conductivity (series) = {kappa_exact:.6f} W/(m K)")
    print(f"exact steady flux q = {q_exact:.6f} W/m^2")
    print(f"cell-centred harmonic-mean face: q = {q_cc:.6f} W/m^2  "
          f"({(q_cc - q_exact) / q_exact * 100:+.3e} %)")
    print(f"node-centred arithmetic-mean face: q = {q_nc:.6f} W/m^2  "
          f"({(q_nc - q_exact) / q_exact * 100:+.3f} %)")
    print(f"face values at the material jump: harmonic = "
          f"{2 * kappa1 * kappa2 / (kappa1 + kappa2):.4f}, arithmetic = "
          f"{0.5 * (kappa1 + kappa2):.4f} W/(m K)")
    return kappa_exact, q_exact, q_cc, q_nc


def quadrature_exactness():
    """Midpoint and trapezoid error for f(x) = x^2 on [0, 1].

    For this integrand the errors are exactly h^2/12 and h^2/6 for every N, so
    the measured value and the analytic prediction can be compared digit for
    digit rather than merely in order of magnitude.
    """
    print("f(x) = x^2 on [0, 1], exact integral = 1/3 = 0.3333333333333333")
    print(f"{'N':>6} {'h':>10} {'midpoint err':>16} {'h^2/12':>14} "
          f"{'trapezoid err':>16} {'h^2/6':>14}")
    prev = None
    for N in (10, 20, 40, 80, 160):
        h = 1.0 / N
        xm = (np.arange(N) + 0.5) * h
        xn = np.arange(N + 1) * h
        mid = h * np.sum(xm ** 2)
        trp = h * (0.5 * xn[0] ** 2 + np.sum(xn[1:-1] ** 2) + 0.5 * xn[-1] ** 2)
        err_m = mid - 1.0 / 3.0
        err_t = trp - 1.0 / 3.0
        print(f"{N:>6} {h:>10.6f} {err_m:>16.3e} {h**2 / 12:>14.3e} "
              f"{err_t:>16.3e} {h**2 / 6:>14.3e}")
        if prev is not None:
            print(f"       successive error ratio: midpoint "
                  f"{prev[0] / err_m:.6f}, trapezoid {prev[1] / err_t:.6f} "
                  f"(exact 4 for a second-order rule)")
        prev = (err_m, err_t)


def discrete_and_continuous_norm():
    """Cell-centred discrete L2 norm of f(x) = x^2 versus the continuous norm.

    sqrt(h * sum f(x_i)^2) = sqrt(1/3 + 1/(12 N^2)) exactly, so the relative
    error must approach (1/(24 sqrt(1/3))) h^2 = 0.0721688 h^2.
    """
    exact = np.sqrt(1.0 / 5.0)
    pred = 1.0 / (12.0 * exact)
    print(f"continuous L2 norm of x^2 on [0, 1] = sqrt(1/5) = {exact:.10f}")
    print("the squared norm h*sum(x_i^4) is the midpoint rule for the integral of")
    print("x^4, whose error is h^2/24 * (4*1^3 - 4*0^3) = h^2/6; the norm therefore")
    print(f"approaches L2 + h^2/(2*6*L2) = L2 + {pred:.7f} h^2")
    print(f"{'N':>6} {'discrete norm':>18} {'difference':>16} "
          f"{'difference / h^2':>18} {'predicted':>12}")
    for N in (10, 20, 40, 80, 320):
        h = 1.0 / N
        xm = (np.arange(N) + 0.5) * h
        disc = np.sqrt(h * np.sum(xm ** 4))
        diff = disc - exact
        print(f"{N:>6} {disc:>18.10f} {diff:>16.3e} {diff / h ** 2:>18.7f} "
              f"{pred:>12.7f}")


def poisson_conditioning():
    """Condition number of the 1-D Dirichlet Poisson matrix.

    T = tridiag(-1, 2, -1)/h^2 with h = 1/(N+1) has the exact condition number
    (1 + cos(pi h)) / (1 - cos(pi h)), asymptotic to 4/(pi^2 h^2).
    """
    print(f"{'N':>6} {'measured cond':>18} {'exact formula':>18} "
          f"{'4/(pi^2 h^2)':>18}")
    for N in (15, 63, 255, 1023):
        h = 1.0 / (N + 1)
        main = 2.0 / h ** 2 * np.ones(N)
        off = -1.0 / h ** 2 * np.ones(N - 1)
        T = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
        c = np.linalg.cond(T)
        exact = (1.0 + np.cos(np.pi * h)) / (1.0 - np.cos(np.pi * h))
        asym = 4.0 / (np.pi ** 2 * h ** 2)
        print(f"{N:>6} {c:>18.4f} {exact:>18.4f} {asym:>18.4f}")
    print("the conditioning grows like N^2 while the truncation error falls like")
    print("N^-2: refining the grid improves accuracy and worsens the linear algebra.")


def main():
    section("1. Degrees of freedom: node-centred versus cell-centred grids")
    dof_counts(1.0, 100)

    section("2. Storing a material contrast: cell-centred versus node-centred")
    two_material_column()

    section("3. Quadrature error is predictable, not mysterious")
    quadrature_exactness()

    section("4. Grid-function norm versus continuous norm")
    discrete_and_continuous_norm()

    section("5. Conditioning of the discrete Laplacian")
    poisson_conditioning()


if __name__ == "__main__":
    main()
