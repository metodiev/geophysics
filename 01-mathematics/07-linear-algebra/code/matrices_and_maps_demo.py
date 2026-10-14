"""Matrices as linear maps: composition, derivative operators, design matrices.

Run:  python3 matrices_and_maps_demo.py
Requires: Python standard library only.

Companion to lesson 01-07-02.

Every matrix here *does* something to a physical object: it rotates a survey
vector, it differentiates a velocity profile, it predicts travel times. The point
of the lesson is the one that a table of numbers hides -- a matrix is a map, and
matrix multiplication is composition of maps.
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


def show(name: str, a: Matrix, places: int = 4) -> None:
    print(f"  {name} =")
    for row in a:
        print("     [" + "  ".join(f"{x:>{8 + places}.{places}f}" for x in row) + "]")


def norm(x: Vector) -> float:
    return math.sqrt(sum(v * v for v in x))


def max_abs_diff(a: Matrix, b: Matrix) -> float:
    return max(abs(a[i][j] - b[i][j])
               for i in range(len(a)) for j in range(len(a[0])))


def determinant2(a: Matrix) -> float:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def rank_rref(a: Matrix, tol: float = 1e-10) -> tuple[int, Matrix]:
    """Reduced row echelon form, returning (rank, rref)."""
    m = [row[:] for row in a]
    rows, cols = len(m), len(m[0])
    pivot_row = 0
    for col in range(cols):
        best = max(range(pivot_row, rows), key=lambda r: abs(m[r][col]))
        if abs(m[best][col]) <= tol:
            continue
        m[pivot_row], m[best] = m[best], m[pivot_row]
        pivot = m[pivot_row][col]
        m[pivot_row] = [x / pivot for x in m[pivot_row]]
        for r in range(rows):
            if r != pivot_row and abs(m[r][col]) > 0.0:
                factor = m[r][col]
                m[r] = [x - factor * y for x, y in zip(m[r], m[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row, m


def main() -> None:
    section("1. A matrix is a map: rotation preserves length, stretch does not")
    theta = math.radians(30.0)
    rotation: Matrix = [[math.cos(theta), -math.sin(theta)],
                        [math.sin(theta), math.cos(theta)]]
    stretch: Matrix = [[1.0, 0.0], [0.0, 2.0]]
    x: Vector = [3.0, 1.0]
    print(f"  x = {x}")
    print(f"  rotation(30 deg) x = {[round(v, 6) for v in matvec(rotation, x)]}")
    print(f"  ||x|| = {norm(x):.6f}   ||R x|| = {norm(matvec(rotation, x)):.6f}")
    print(f"  ||S x|| = {norm(matvec(stretch, x)):.6f}  (stretch rescales)")
    print("  action on the unit square, area scale factors:")
    for name, a in (("R", rotation), ("S", stretch)):
        corners = [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]]
        images = [matvec(a, c) for c in corners]
        area = 0.0
        for i in range(4):
            x1, y1 = images[i]
            x2, y2 = images[(i + 1) % 4]
            area += x1 * y2 - x2 * y1
        print(f"    {name}: image area = {abs(area) / 2:.6f}, "
              f"det = {determinant2(a):.6f}")
    print("\nReading: the determinant is the area (in 3-D, volume) scale factor of")
    print("the map. Rotation has det = 1: it moves nothing in or out of the plane.")

    section("2. Composition of maps is matrix multiplication, and order matters")
    rs = matmul(rotation, stretch)
    sr = matmul(stretch, rotation)
    show("R S", rs)
    show("S R", sr)
    print(f"  max|R S - S R| = {max_abs_diff(rs, sr):.6f}")
    print(f"  R S applied to x = {[round(v, 6) for v in matvec(rs, x)]}")
    print(f"  S R applied to x = {[round(v, 6) for v in matvec(sr, x)]}")
    print("\nReading: these are two different processing sequences. 'Rotate the")
    print("survey into the anisotropy frame, then stretch' is not 'stretch, then")
    print("rotate'. Matrix multiplication is not commutative because maps do not")
    print("commute.")

    section("3. A derivative operator is a matrix -- and it is singular")
    # v(z) cubic in z, sampled on 0..6 km. The operator takes first differences.
    n = 7
    h = 1.0

    def velocity(z: float) -> float:
        return 1600.0 + 0.6 * z + 0.02 * z * z + 0.001 * z ** 3

    def gradient(z: float) -> float:
        return 0.6 + 0.04 * z + 0.003 * z * z

    zs = [h * i for i in range(n)]
    v = [velocity(z) for z in zs]
    # One-sided at the two boundaries, central in the interior: the standard
    # finite-difference first-derivative matrix.
    d: Matrix = [[0.0] * n for _ in range(n)]
    d[0][0], d[0][1] = -1.0 / h, 1.0 / h
    for i in range(1, n - 1):
        d[i][i - 1], d[i][i + 1] = -0.5 / h, 0.5 / h
    d[n - 1][n - 2], d[n - 1][n - 1] = -1.0 / h, 1.0 / h
    dv = matvec(d, v)
    print(f"  z (km)          : {'  '.join(f'{z:8.1f}' for z in zs)}")
    print(f"  v (m/s)         : {'  '.join(f'{x:9.3f}' for x in v)}")
    print(f"  D v (s^-1)      : {'  '.join(f'{x:9.4f}' for x in dv)}")
    print(f"  exact dv/dz     : {'  '.join(f'{gradient(z):9.4f}' for z in zs)}")
    errs = [dv[i] - gradient(zs[i]) for i in range(n)]
    print(f"  error           : {'  '.join(f'{e:9.4f}' for e in errs)}")
    print("  Interior error is +0.0010 everywhere (the O(h^2) central-difference")
    print("  term h^2 v'''/6 = 0.001); the two boundary errors are O(h) because")
    print("  one-sided stencils are only first-order accurate. Boundary rows")
    print("  usually govern the global accuracy of a discretisation.")
    rank, _ = rank_rref(d)
    ones = [1.0] * n
    print(f"\n  rank(D) = {rank} of {n}  (so {n - rank} null direction(s))")
    print(f"  D applied to the constant vector: {[round(x, 12) for x in matvec(d, ones)]}")
    print("  A constant added to the whole velocity profile leaves D v exactly")
    print("  unchanged. Absolute level is invisible to a derivative: the null")
    print("  space of this operator is the set of constant profiles. This is the")
    print("  simplest possible non-uniqueness, and it is exactly the mechanism of")
    print("  lesson 01-07-04.")
    print("\n  central differences on a cubic, h = 1, 0.5, 0.25 km:")
    for hh in (1.0, 0.5, 0.25):
        z = 3.0
        approx = (velocity(z + hh) - velocity(z - hh)) / (2 * hh)
        exact = gradient(z)
        print(f"    h = {hh:5.2f} km   central = {approx:.8f}   exact = {exact:.8f}"
              f"   error = {approx - exact:.3e}")
    print("  Errors fall by 4 when h halves, so the truncation error is O(h^2).")

    section("4. A design matrix: predicting data from a model")
    # Model: gravity residual g(z) = m0 + m1 z, with z the station elevation.
    z_all = [0.0, 1.0, 2.0, 3.0]
    g_design: Matrix = [[1.0, z] for z in z_all]
    m_true: Vector = [0.5, -3.0]
    show("G (design)", g_design)
    print(f"  m = {m_true}   (intercept, gradient)")
    print(f"  d = G m = {[round(x, 6) for x in matvec(g_design, m_true)]}")
    print("\n  The first column of G is the 'mean level' pattern applied to all")
    print("  stations; the second is the 'elevation-dependent' pattern. Every")
    print("  achievable data vector is a combination of those two columns, so the")
    print("  only data vectors we can explain are those in the column space of G.")

    section("5. Convolution is matrix multiplication (a structured matrix)")
    trace = [1.0, 2.0, 4.0, 3.0, 1.5]
    kernel = [0.25, 0.5, 0.25]
    m = len(trace)
    conv_matrix: Matrix = [[0.0] * m for _ in range(m)]
    for i in range(m):
        for k, w in enumerate(kernel):
            j = i + k - 1
            if 0 <= j < m:
                conv_matrix[i][j] = w
    show("C (smoothing filter)", conv_matrix)
    direct = [0.0] * m
    for i in range(m):
        for k, w in enumerate(kernel):
            j = i + k - 1
            if 0 <= j < m:
                direct[i] += w * trace[j]
    print(f"  trace              = {trace}")
    print(f"  direct convolution = {[round(x, 8) for x in direct]}")
    print(f"  C trace            = {[round(x, 8) for x in matvec(conv_matrix, trace)]}")
    nz = sum(1 for row in conv_matrix for x in row if x != 0.0)
    print(f"  nonzeros of C      = {nz} of {m * m} ({100.0 * nz / (m * m):.1f} %)")
    print("\nReading: the same arithmetic, three views. A filter is a matrix; a")
    print("matrix with a repeated diagonal is a convolution. Recognising the")
    print("structure is what makes the operation fast (lesson 01-07-09).")

    section("6. Two nonzero maps can annihilate everything")
    a: Matrix = [[1.0, 0.0], [0.0, 0.0]]
    b: Matrix = [[0.0, 0.0], [0.0, 1.0]]
    show("A", a)
    show("B", b)
    show("A B", matmul(a, b))
    print(f"  A is nonzero, B is nonzero, A B is {'zero' if max_abs_diff(matmul(a, b), [[0, 0], [0, 0]]) == 0 else 'nonzero'}")
    print("\nReading: A and B destroy different halves of the plane, so their")
    print("composition destroys everything. Matrix algebra with multiplication")
    print("cannot be done term by term; only structure and factorisation let you")
    print("reason about it.")


if __name__ == "__main__":
    main()
