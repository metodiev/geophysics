"""Rank, null space and solvability: when a survey cannot see everything.

Run:  python3 rank_and_nullspace_demo.py
Requires: Python standard library only.

Companion to lesson 01-07-04.

The kernel below is a three-ray, three-cell tomography geometry in which the
third ray happens to traverse exactly the same total path length combination as
the first two. That single coincidence is a null space of dimension one, and it
means the experiment cannot distinguish a whole one-parameter family of models.
Non-uniqueness is not a numerical artefact here; it is a property of the
geometry.
"""

import math

Matrix = list[list[float]]
Vector = list[float]


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def matvec(a: Matrix, x: Vector) -> Vector:
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def dot(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(a: Vector) -> float:
    return math.sqrt(dot(a, a))


def sub(a: Vector, b: Vector) -> Vector:
    return [x - y for x, y in zip(a, b)]


def scale(a: Vector, s: float) -> Vector:
    return [s * x for x in a]


def add(a: Vector, b: Vector) -> Vector:
    return [x + y for x, y in zip(a, b)]


def show(title: str, a: Matrix, places: int = 2) -> None:
    print(f"  {title}")
    for row in a:
        print("     [" + "  ".join(f"{x:>{8 + places}.{places}f}" for x in row) + "]")


def rref(a: Matrix, tol: float = 1e-10) -> tuple[int, Matrix, list[int]]:
    """Reduced row echelon form. Returns (rank, rref, pivot columns)."""
    m = [row[:] for row in a]
    rows, cols = len(m), len(m[0])
    pivots: list[int] = []
    pivot_row = 0
    for col in range(cols):
        best = max(range(pivot_row, rows), key=lambda r: abs(m[r][col]))
        if abs(m[best][col]) <= tol:
            continue
        m[pivot_row], m[best] = m[best], m[pivot_row]
        pivot = m[pivot_row][col]
        m[pivot_row] = [x / pivot for x in m[pivot_row]]
        for r in range(rows):
            if r != pivot_row and m[r][col] != 0.0:
                factor = m[r][col]
                m[r] = [x - factor * y for x, y in zip(m[r], m[pivot_row])]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == rows:
            break
    for row in m:
        for j in range(len(row)):
            if abs(row[j]) < tol:
                row[j] = 0.0
    return pivot_row, m, pivots


def null_space_basis(a: Matrix, tol: float = 1e-10) -> list[Vector]:
    """An orthonormal-free basis of the null space, from the RREF."""
    rank, m, pivots = rref(a, tol)
    cols = len(m[0])
    free = [c for c in range(cols) if c not in pivots]
    basis: list[Vector] = []
    for f in free:
        v = [0.0] * cols
        v[f] = 1.0
        for r, p in enumerate(pivots):
            v[p] = -m[r][f]
        basis.append(v)
    return basis


def gram_schmidt(vectors: list[Vector]) -> list[Vector]:
    basis: list[Vector] = []
    for v in vectors:
        w = list(v)
        for e in basis:
            w = sub(w, scale(e, dot(w, e)))
        if norm(w) > 1e-12:
            basis.append(scale(w, 1.0 / norm(w)))
    return basis


def projector(vectors: list[Vector]) -> Matrix:
    """Orthogonal projection matrix onto the span of the given vectors."""
    basis = gram_schmidt(vectors)
    n = len(basis[0])
    return [[sum(e[i] * e[j] for e in basis) for j in range(n)] for i in range(n)]


def main() -> None:
    section("1. A geometry with a redundant ray")
    g: Matrix = [[1.0, 1.0, 0.0],
                 [0.0, 1.0, 1.0],
                 [1.0, 2.0, 1.0]]
    show("G (path lengths, km): three rays, three cells", g)
    print("  row 3 = row 1 + row 2")
    rank, m, pivots = rref(g)
    print(f"  rank(G) = {rank}, pivot columns {[p + 1 for p in pivots]}")
    print(f"  n - rank = {3 - rank} null direction(s)")
    basis = null_space_basis(g)
    for nvec in basis:
        n_hat = scale(nvec, 1.0 / norm(nvec))
        print(f"  null-space basis vector   : {[round(v, 6) for v in nvec]}")
        print(f"  normalised                : {[round(v, 6) for v in n_hat]}")
        print(f"  G times it                : {[round(v, 12) for v in matvec(g, nvec)]}")
    print("\nReading: the null-space direction is proportional to (1, -1, 1):")
    print("raise cell 1 and cell 3, lower cell 2, by the same amount, and every")
    print("one of the three rays sees exactly the same delay. The data are")
    print("completely blind to that perturbation.")

    section("2. A one-parameter family of models fits one dataset exactly")
    d: Vector = [1.0, 0.0, 1.0]
    m_p: Vector = [1.0, 0.0, 0.0]
    print(f"  data d = {d}   (consistent: d3 = d1 + d2)")
    print(f"  a particular model that reproduces it: m = {m_p}")
    n_unit = scale(null_space_basis(g)[0], 1.0 / norm(null_space_basis(g)[0]))
    print(f"  {'alpha':>10}  {'m1':>10}  {'m2':>10}  {'m3':>10}  "
          f"{'||G m - d||':>14}  {'||m||':>10}")
    for alpha in (-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0):
        mv = add(m_p, scale(n_unit, alpha))
        residual = max(abs(v) for v in sub(matvec(g, mv), d))
        print(f"  {alpha:>10.4f}  {mv[0]:>10.6f}  {mv[1]:>10.6f}  {mv[2]:>10.6f}"
              f"  {residual:>14.3e}  {norm(mv):>10.6f}")
    alpha_min = -dot(m_p, n_unit)
    m_min = add(m_p, scale(n_unit, alpha_min))
    print(f"\n  smallest model in the family: alpha = {alpha_min:.6f} -> "
          f"m = {[round(v, 6) for v in m_min]}, ||m|| = {norm(m_min):.6f}")
    print("  Every row above fits the data to round-off. The data cannot choose")
    print("  between them; only a prior (a norm, a smoothness assumption, a")
    print("  regularisation weight) can.")

    section("3. Inconsistent data: the other failure mode")
    for d_bad in ([1.0, 0.0, 0.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0]):
        aug = [g[i][:] + [d_bad[i]] for i in range(3)]
        rank_a, _, _ = rref(aug)
        rank_c, _, _ = rref(g)
        print(f"  d = {d_bad}:  rank([G|d]) = {rank_a}, rank(G) = {rank_c}, "
              f"consistent = {rank_a == rank_c}")
    print("\nReading: rank([G|d]) > rank(G) means the equations contradict each")
    print("other. For this G the only inconsistent data are those with")
    print("d3 - d1 - d2 != 0. Existence and uniqueness are two separate tests,")
    print("and G can fail either one independently -- lesson 01-07-08 shows how")
    print("the SVD diagnoses both at once.")

    section("4. The four fundamental subspaces, by dimension")
    rank_g, _, _ = rref(g)
    left_null = null_space_basis([list(row) for row in zip(*g)])
    print(f"  column space of G : dimension {rank_g}   (reachable data)")
    print(f"  null space of G   : dimension {3 - rank_g}   (invisible models)")
    print(f"  row space of G    : dimension {rank_g}   (resolvable model combos)")
    print(f"  left null space   : dimension {3 - rank_g}   (data that cannot occur)")
    for v in left_null:
        print(f"    left null vector  = {[round(x, 6) for x in v]}, "
              f"G^T times it = {[round(x, 12) for x in matvec([list(r) for r in zip(*g)], v)]}")
    print("\nReading: a left null vector is a combination of the data that is")
    print("identically zero for every model. Here it is (1, 1, -1): the third")
    print("ray carries exactly the sum of the first two, so its datum is")
    print("redundant. A real survey with a left null vector is a survey with a")
    print("wasted ray -- or, in a noisy survey, a check on the noise level.")
    print("Rank plus nullity equals 3 in both cases (2+1 for the model space of")
    print("columns, 2+1 for the data space of rows): the rank-nullity theorem.")

    section("5. The resolution matrix: what the data can and cannot fix")
    r = projector([row for row in g])
    show("R = projection onto the row space of G", r)
    r2 = [[sum(r[i][k] * r[k][j] for k in range(3)) for j in range(3)]
          for i in range(3)]
    print(f"  idempotent, max|R^2 - R| = "
          f"{max(abs(r2[i][j] - r[i][j]) for i in range(3) for j in range(3)):.3e}")
    print(f"  symmetric,  max|R^T - R| = "
          f"{max(abs(r[j][i] - r[i][j]) for i in range(3) for j in range(3)):.3e}")
    print(f"  trace(R) = {sum(r[i][i] for i in range(3)):.6f} = rank(G)")
    print(f"  R applied to the null vector: "
          f"{[round(v, 12) for v in matvec(r, null_space_basis(g)[0])]}")
    for mv in ([1.0, 2.0, 3.0], [1.0, 0.0, 0.0], m_min):
        rm = matvec(r, mv)
        print(f"  m = {[round(v, 4) for v in mv]}")
        print(f"    R m = {[round(v, 6) for v in rm]}   "
              f"||m - R m|| = {norm(sub(mv, rm)):.6f}")
    print("\nReading: R is the identity only when the data resolve every model")
    print("direction. Here it removes the (1, -1, 1) component from any model")
    print("you feed it. The diagonal of R is the classic 'resolution' diagnostic:")
    print(f"  diag(R) = {[round(r[i][i], 6) for i in range(3)]} --")
    print("  none of the three cells is perfectly resolved on its own.")

    section("6. The same phenomenon in the simplest operator there is")
    print("  The first-difference matrix of lesson 01-07-02:")
    n = 5
    dd: Matrix = [[0.0] * n for _ in range(n)]
    dd[0][0], dd[0][1] = -1.0, 1.0
    for i in range(1, n - 1):
        dd[i][i - 1], dd[i][i + 1] = -0.5, 0.5
    dd[n - 1][n - 2], dd[n - 1][n - 1] = -1.0, 1.0
    show("D", dd, places=1)
    print(f"  rank(D) = {rref(dd)[0]} of {n}; "
          f"null space = span of {null_space_basis(dd)[0]}")
    print("  Two velocity profiles that differ by a constant give identical")
    print("  gradients. Any method that inverts a gradient field -- a strain rate")
    print("  from GPS, a velocity from a travel-time gradient -- has this null")
    print("  space exactly, and must supply the constant by other means.")


if __name__ == "__main__":
    main()
