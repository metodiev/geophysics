"""Eigenvalues, eigenvectors and diagonalisation, on physical matrices.

Run:  python3 eigenvalues_demo.py
Requires: Python standard library only.

Companion to lesson 01-07-06.

Sections 1 and 2 are stress tensors: principal stresses and principal axes are
eigenvalues and eigenvectors, and nothing else. Section 5 is the convergence of
an iterative solver, which is governed by the spectral radius of its iteration
matrix. The two subjects are the same subject.
"""

import math

Matrix = list[list[float]]
Vector = list[float]


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def matvec(a: Matrix, x: Vector) -> Vector:
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def eye(n: int) -> Matrix:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def show(title: str, a: Matrix, places: int = 4) -> None:
    print(f"  {title}")
    for row in a:
        print("     [" + "  ".join(f"{x:>{9 + places}.{places}f}" for x in row) + "]")


def norm(x: Vector) -> float:
    return math.sqrt(sum(v * v for v in x))


def det(a: Matrix) -> float:
    n = len(a)
    m = [row[:] for row in a]
    sign = 1.0
    for k in range(n - 1):
        pivot = max(range(k, n), key=lambda r: abs(m[r][k]))
        if abs(m[pivot][k]) < 1e-300:
            return 0.0
        if pivot != k:
            m[k], m[pivot] = m[pivot], m[k]
            sign = -sign
        for r in range(k + 1, n):
            factor = m[r][k] / m[k][k]
            for c in range(k, n):
                m[r][c] -= factor * m[k][c]
    product = sign
    for i in range(n):
        product *= m[i][i]
    return product


def jacobi_eigen(a: Matrix, tol: float = 1e-15, sweeps: int = 100) -> tuple[Vector, Matrix]:
    """Cyclic Jacobi eigenvalues/vectors of a symmetric matrix; vectors in columns."""
    n = len(a)
    work = [row[:] for row in a]
    v = eye(n)
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
                if theta == 0.0:
                    t = 1.0
                else:
                    t = math.copysign(1.0, theta) / (abs(theta) + math.sqrt(theta * theta + 1.0))
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


def gauss_solve(a: Matrix, b: Vector) -> Vector:
    n = len(a)
    m = [[a[i][j] for j in range(n)] + [b[i]] for i in range(n)]
    for k in range(n - 1):
        pivot = max(range(k, n), key=lambda r: abs(m[r][k]))
        if abs(m[pivot][k]) < 1e-300:
            raise ArithmeticError("singular")
        m[k], m[pivot] = m[pivot], m[k]
        for r in range(k + 1, n):
            factor = m[r][k] / m[k][k]
            for c in range(k, n + 1):
                m[r][c] -= factor * m[k][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x


def bearing_deg(east: float, north: float) -> float:
    """Compass bearing (clockwise from north) of a horizontal direction."""
    return math.degrees(math.atan2(east, north)) % 180.0


def main() -> None:
    section("1. A two-dimensional stress tensor")
    # Sigma in MPa, x = east, y = north. Sign convention: compression positive,
    # which is the usual convention in rock mechanics.
    sigma: Matrix = [[60.0, -25.0], [-25.0, 20.0]]
    show("sigma (MPa)", sigma)
    values, vectors = jacobi_eigen(sigma)
    order = sorted(range(2), key=lambda i: -values[i])
    print(f"  principal stresses (MPa): ", end="")
    print(", ".join(f"{values[i]:.6f}" for i in order))
    print(f"  trace          = {sigma[0][0] + sigma[1][1]:.6f} MPa "
          f"(= sum of principal stresses, an invariant)")
    print(f"  determinant    = {det(sigma):.6f} MPa^2 "
          f"(= product of principal stresses)")
    print(f"  max shear stress = {(values[order[0]] - values[order[1]]) / 2:.6f} MPa")
    print("  principal axes (unit eigenvectors) and their bearings:")
    for i in order:
        v = [vectors[r][i] for r in range(2)]
        if v[0] < 0:
            v = [-c for c in v]
        print(f"    sigma = {values[i]:10.6f} MPa  axis = "
              f"[{v[0]:9.6f}, {v[1]:9.6f}]  bearing = {bearing_deg(v[0], v[1]):8.4f} deg")
    dot = sum(vectors[r][order[0]] * vectors[r][order[1]] for r in range(2))
    print(f"  the two axes are orthogonal: v1 . v2 = {dot:.3e}")
    print("  residual check A v - lambda v for the major axis:")
    major = [vectors[r][order[0]] for r in range(2)]
    diff = [matvec(sigma, major)[r] - values[order[0]] * major[r] for r in range(2)]
    print(f"    max |A v - lambda v| = {max(abs(x) for x in diff):.3e} MPa")
    print("\nReading: the state of stress at a point is a symmetric tensor, and")
    print("its eigenvectors are the planes on which shear vanishes. The bearings")
    print("differ by 90 degrees, as they must; the principal values are what a")
    print("borehole break-out or a focal mechanism actually measures.")

    section("2. A three-dimensional stress tensor")
    sigma3: Matrix = [[50.0, -20.0, 0.0],
                      [-20.0, 30.0, 0.0],
                      [0.0, 0.0, 10.0]]
    show("sigma (MPa)", sigma3)
    vals3, vecs3 = jacobi_eigen(sigma3)
    order3 = sorted(range(3), key=lambda i: -vals3[i])
    print("  principal stresses and directions:")
    for i in order3:
        v = [vecs3[r][i] for r in range(3)]
        if v[0] < 0:
            v = [-c for c in v]
        print(f"    {vals3[i]:10.6f} MPa   [{v[0]:8.5f}, {v[1]:8.5f}, {v[2]:8.5f}]"
              f"   bearing = {bearing_deg(v[0], v[1]):8.4f} deg,"
              f" plunge = {math.degrees(math.asin(max(-1.0, min(1.0, v[2])))):8.4f} deg")
    print(f"  trace = {sum(sigma3[i][i] for i in range(3)):.6f} MPa")
    print(f"  sum of principal stresses = {sum(vals3):.6f} MPa")
    print(f"  det = {det(sigma3):.6f} MPa^3, product = "
          f"{vals3[0] * vals3[1] * vals3[2]:.6f}")
    minors = (sigma3[0][0] * sigma3[1][1] - sigma3[0][1] * sigma3[1][0]) \
        + (sigma3[0][0] * sigma3[2][2] - sigma3[0][2] * sigma3[2][0]) \
        + (sigma3[1][1] * sigma3[2][2] - sigma3[1][2] * sigma3[2][1])
    products = sum(vals3[i] * vals3[j] for i in range(3) for j in range(i + 1, 3))
    print(f"  sum of principal 2x2 minors = {minors:.6f}, "
          f"sum of pairwise products = {products:.6f}")
    print("\nReading: three invariants -- trace, sum of the 2x2 minors, and the")
    print("determinant -- are identical in any coordinate system. They are the")
    print("coefficients of the characteristic polynomial, so they are also what")
    print("a stress state reports when a coordinate frame is unavailable.")
    print("A vertical axis (0, 0, 1) with lambda = 10 is an eigenvector here")
    print("only because the tensor was written in the principal frame of that")
    print("plane; in general nothing is aligned with the geographic axes.")

    section("3. Diagonalisation, and when it fails")
    a: Matrix = [[2.0, 1.0], [0.0, 3.0]]
    show("A (non-symmetric)", a, places=1)
    print("  eigenvalues from the characteristic polynomial:")
    tr, dt = a[0][0] + a[1][1], det(a)
    disc = math.sqrt(tr * tr - 4 * dt)
    print(f"    lambda^2 - {tr:.1f} lambda + {dt:.1f} = 0  ->  "
          f"lambda = {(tr + disc) / 2:.6f}, {(tr - disc) / 2:.6f}")
    v1 = [1.0, 0.0]
    v2 = [1.0, 1.0]
    vmat: Matrix = [[v1[0], v2[0]], [v1[1], v2[1]]]
    vmat_inv: Matrix = [[1.0, -1.0], [0.0, 1.0]]
    lam: Matrix = [[2.0, 0.0], [0.0, 3.0]]
    rebuilt = matmul(matmul(vmat, lam), vmat_inv)
    show("V L V^-1", rebuilt, places=4)
    print(f"  max |A - V L V^-1| = "
          f"{max(abs(rebuilt[i][j] - a[i][j]) for i in range(2) for j in range(2)):.3e}")
    print("\n  a defective matrix (a repeated eigenvalue with one eigenvector):")
    d: Matrix = [[2.0, 1.0], [0.0, 2.0]]
    show("A", d, places=1)
    print(f"    eigenvalues: {d[0][0]:.6f}, {d[1][1]:.6f} (repeated)")
    print("    solutions of (A - 2I) v = 0: v = (1, 0) only -- one direction,")
    print("    so V is singular and no diagonalisation exists.")
    print("\nReading: symmetric matrices are always diagonalisable, with an")
    print("orthogonal V. General matrices are diagonalisable only if they have a")
    print("full set of independent eigenvectors. Almost every matrix in")
    print("geophysics -- stiffness, moment of inertia, G^T G, covariance -- is")
    print("symmetric, which is why the useful theory is the symmetric theory.")

    section("4. Power iteration, and why the eigenvalue gap is what matters")
    p: Matrix = [[4.0, 1.0], [1.0, 3.0]]
    vals, _ = jacobi_eigen(p)
    vals = sorted(vals, reverse=True)
    ratio_theory = abs(vals[1] / vals[0])
    print(f"  A = [[4, 1], [1, 3]]; eigenvalues {vals[0]:.6f}, {vals[1]:.6f}")
    print(f"  |lambda_2 / lambda_1| = {ratio_theory:.6f}")
    x = [1.0, 0.0]
    previous = None
    print(f"\n  {'iteration':>10}  {'Rayleigh quotient':>20}  {'error':>12}  "
          f"{'error ratio':>12}")
    for it in range(1, 21):
        y = matvec(p, x)
        x = [v / norm(y) for v in y]
        rq = sum(x[i] * matvec(p, x)[i] for i in range(2))
        error = abs(rq - vals[0])
        ratio = "-" if previous is None else f"{error / previous:.4f}"
        if it <= 5 or it % 5 == 0:
            print(f"  {it:>10}  {rq:>20.12f}  {error:>12.3e}  {ratio:>12}")
        previous = error
    print(f"\nReading: the error ratio converges to {ratio_theory ** 2:.4f}, which")
    print(f"is |lambda_2/lambda_1|^2 = {ratio_theory:.6f}^2. The *eigenvector*")
    print("coefficient decays by the factor |lambda_2/lambda_1| per iteration, and")
    print("the Rayleigh quotient -- an eigenvalue estimate built from two factors")
    print("of the eigenvector -- therefore converges with the square of that")
    print("ratio. A small gap means slow convergence, and that is the mechanism")
    print("behind slow convergence of every iterative linear solver and every")
    print("slowly decaying normal mode. The power method finds the *largest*")
    print("eigenvalue; finding the smallest is the same algorithm applied to the")
    print("inverse, which costs a factorisation (lesson 01-07-03).")

    section("5. An iterative solver is governed by a spectral radius")
    g: Matrix = [[2.0, 1.0, 0.0], [1.0, 2.0, 1.0], [0.0, 1.0, 2.0]]
    d3 = [0.08, 0.11, 0.18]
    exact = gauss_solve(g, d3)
    bmat: Matrix = [[0.0, -0.5, 0.0], [-0.5, 0.0, -0.5], [0.0, -0.5, 0.0]]
    bvals, _ = jacobi_eigen(bmat)
    rho = max(abs(v) for v in bvals)
    print(f"  Jacobi iteration matrix B = -D^-1 (L + U) = ")
    show("B", bmat, places=1)
    print(f"  eigenvalues of B = {[round(v, 6) for v in sorted(bvals)]}")
    print(f"  spectral radius = {rho:.9f}   (1/sqrt(2) = {1 / math.sqrt(2):.9f})")
    for name, sweeps in (("Jacobi", "jacobi"), ("Gauss-Seidel", "gs")):
        x = [0.0, 0.0, 0.0]
        previous = None
        ratios: list[float] = []
        hits = None
        for it in range(1, 81):
            if sweeps == "jacobi":
                new = [0.0] * 3
                for i in range(3):
                    new[i] = (d3[i] - sum(g[i][j] * x[j] for j in range(3) if j != i)) / g[i][i]
                x = new
            else:
                for i in range(3):
                    x[i] = (d3[i] - sum(g[i][j] * x[j] for j in range(3) if j != i)) / g[i][i]
            error = norm([x[i] - exact[i] for i in range(3)])
            # Only ratios measured while the error is well above round-off are
            # meaningful; below that the arithmetic reports noise.
            if previous is not None and previous > 1e-10 and error > 1e-12:
                ratios.append(error / previous)
            if hits is None and error < 1e-10:
                hits = it
            previous = error
        residual = max(abs(matvec(g, x)[i] - d3[i]) for i in range(3))
        print(f"  {name:>13}: last measured error ratio = {ratios[-1]:.6f} "
              f"(from {len(ratios)} usable ratios), iterations to 1e-10 = {hits}, "
              f"max data residual = {residual:.3e}")
    print("\nReading: the measured Jacobi error ratio is the spectral radius")
    print("0.7071. Gauss-Seidel halves it, as the theory of consistently ordered")
    print("matrices predicts (rho_GS = rho_J^2 = 0.5). This is lesson 01-07-07's")
    print("series convergence applied to a matrix, and it is the whole content of")
    print("lesson 01-07-09's iterative solvers.")

    section("6. Definiteness is a statement about eigenvalues")
    for name, m in (("elastic stiffness (positive definite)", [[4.0, 1.0], [1.0, 3.0]]),
                    ("indefinite / saddle", [[1.0, 2.0], [2.0, 1.0]]),
                    ("semidefinite (rank deficient)", [[1.0, 1.0], [1.0, 1.0]])):
        vals, ve = jacobi_eigen(m)
        print(f"  {name}: eigenvalues {[round(v, 6) for v in sorted(vals)]}")
        for probe in ([1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, -1.0]):
            q = sum(probe[i] * m[i][j] * probe[j] for i in range(2) for j in range(2))
            print(f"    x = {probe}: x^T A x = {q:10.4f}")
    print("\nReading: a positive-definite quadratic form is an energy. Minimising")
    print("it is a well-posed problem with a unique stationary point; that is why")
    print("misfit functionals are built as m^T m. An indefinite form has a saddle")
    print("-- a direction in which the value decreases without limit -- and no")
    print("inversion that ignores that structure can work.")


if __name__ == "__main__":
    main()
