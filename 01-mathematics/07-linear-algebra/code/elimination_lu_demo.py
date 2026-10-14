"""Gaussian elimination, pivoting and LU factorisation, on a small tomography system.

Run:  python3 elimination_lu_demo.py
Requires: Python standard library only.

Companion to lesson 01-07-03.

The physical problem is a three-cell travel-time tomography: three rays traverse
a strip divided into three cells, the path length in each cell is known (the
matrix), and the travel-time residuals are measured (the right-hand side). What
we want is the slowness perturbation in each cell.
"""

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


def max_abs_diff(a: Matrix, b: Matrix) -> float:
    return max(abs(a[i][j] - b[i][j])
               for i in range(len(a)) for j in range(len(a[0])))


def show(title: str, a: Matrix, places: int = 4) -> None:
    print(f"  {title}")
    for row in a:
        print("     [" + "  ".join(f"{x:>{9 + places}.{places}f}" for x in row) + "]")


def gauss_solve(a: Matrix, b: Vector, trace: bool = True) -> Vector:
    """Gaussian elimination with partial pivoting, then back substitution."""
    n = len(a)
    m = [[a[i][j] for j in range(n)] + [b[i]] for i in range(n)]
    if trace:
        print("  augmented system [A | b]:")
        show("", m)
    for k in range(n - 1):
        pivot = max(range(k, n), key=lambda r: abs(m[r][k]))
        if abs(m[pivot][k]) < 1e-14:
            raise ArithmeticError(f"column {k} is empty below the diagonal: singular")
        if pivot != k:
            m[k], m[pivot] = m[pivot], m[k]
            if trace:
                print(f"  swap rows {k} and {pivot} (partial pivoting):")
                show("", m)
        for r in range(k + 1, n):
            factor = m[r][k] / m[k][k]
            for c in range(k, n + 1):
                m[r][c] -= factor * m[k][c]
            if trace:
                print(f"  eliminate row {r} using row {k} (multiplier {factor:+.4f}):")
                show("", m)
    if trace:
        print("  back substitution:")
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        known = sum(m[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (m[i][n] - known) / m[i][i]
        if trace:
            print(f"    x{i + 1} = ({m[i][n]:.6f} - {known:.6f}) "
                  f"/ {m[i][i]:.6f} = {x[i]:.6f}")
    return x


def gauss_without_pivoting(a: Matrix, b: Vector) -> Vector | None:
    """The textbook algorithm with no pivoting: returns None if a pivot is zero."""
    n = len(a)
    m = [[a[i][j] for j in range(n)] + [b[i]] for i in range(n)]
    for k in range(n - 1):
        if m[k][k] == 0.0:
            print(f"    step {k + 1}: pivot is exactly zero -> division by zero.")
            return None
        for r in range(k + 1, n):
            factor = m[r][k] / m[k][k]
            for c in range(k, n + 1):
                m[r][c] -= factor * m[k][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        acc = m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))
        x[i] = acc / m[i][i]
    return x


def lu_factor(a: Matrix) -> tuple[Matrix, Matrix, Matrix, list[int]]:
    """LU with partial pivoting. Returns (P, L, U, swaps)."""
    n = len(a)
    u = [row[:] for row in a]
    l = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    perm = list(range(n))
    for k in range(n):
        pivot = max(range(k, n), key=lambda r: abs(u[r][k]))
        if abs(u[pivot][k]) < 1e-14:
            raise ArithmeticError("matrix is singular")
        if pivot != k:
            u[k], u[pivot] = u[pivot], u[k]
            perm[k], perm[pivot] = perm[pivot], perm[k]
            for j in range(k):
                l[k][j], l[pivot][j] = l[pivot][j], l[k][j]
        for r in range(k + 1, n):
            factor = u[r][k] / u[k][k]
            l[r][k] = factor
            for c in range(k, n):
                u[r][c] -= factor * u[k][c]
    p = [[1.0 if perm[i] == j else 0.0 for j in range(n)] for i in range(n)]
    return p, l, u, perm


def substitution_counts(n: int) -> tuple[int, int]:
    """Multiply-add counts: (elimination, back substitution) for an n x n system.

    At step k there are n-k-1 rows left below the pivot and n-k entries per row
    to update, so the count is the exact sum, not an asymptotic estimate.
    """
    elim = sum((n - k - 1) * (n - k) for k in range(n - 1))
    back = n * (n + 1) // 2
    return elim, back


def main() -> None:
    section("1. The physical system: three rays, three cells")
    # Path lengths in km, one row per ray and one column per cell.
    g: Matrix = [[2.0, 1.0, 0.0],
                 [1.0, 2.0, 1.0],
                 [0.0, 1.0, 2.0]]
    # True slowness perturbations in s/km: +50, -20, +100 ms/km.
    m_true: Vector = [0.050, -0.020, 0.100]
    d = matvec(g, m_true)
    show("G (path length, km)", g)
    print(f"  m_true (s/km) = {m_true}")
    print(f"  d = G m_true   = {[round(x, 6) for x in d]}   (travel-time residual, s)")
    print("\nReading: row i says 'the travel-time residual for ray i is the sum")
    print("over the cells of (path length in cell) x (slowness change in cell)'.")
    print("Rows of G are rays; columns are model cells.")

    section("2. Forward elimination and back substitution")
    m_est = gauss_solve(g, d)
    print(f"\n  recovered slowness changes: {[round(x, 9) for x in m_est]}")
    print(f"  exact:                      {m_true}")
    print(f"  max error: {max(abs(a - b) for a, b in zip(m_est, m_true)):.3e} s/km")

    section("3. Determinant from the pivots")
    _, _, u, _ = lu_factor(g)
    det = 1.0
    for i in range(len(u)):
        det *= u[i][i]
    print(f"  diagonal of U: {[round(u[i][i], 6) for i in range(len(u))]}")
    print(f"  product of pivots (the determinant, sign aside) = {det:.6f}")
    print(f"  exact determinant by cofactor expansion = "
          f"{2.0 * (2.0 * 2.0 - 1.0 * 1.0) - 1.0 * (1.0 * 2.0 - 0.0):.6f}")
    print("\nReading: elimination does not change the determinant apart from row")
    print("swaps, so the product of the pivots is the determinant. A zero pivot")
    print("is therefore the same statement as a zero determinant.")

    section("4. LU factorisation and the check P A = L U")
    p, l, u, perm = lu_factor(g)
    show("P", p)
    show("L", l)
    show("U", u)
    lu = matmul(l, u)
    pa = matmul(p, g)
    print(f"  max|P A - L U| = {max_abs_diff(pa, lu):.3e}")
    # Solve via the factors.
    pb = [d[perm[i]] for i in range(len(d))]
    y = [0.0] * len(d)
    for i in range(len(d)):
        y[i] = (pb[i] - sum(l[i][j] * y[j] for j in range(i))) / l[i][i]
    x = [0.0] * len(d)
    for i in range(len(d) - 1, -1, -1):
        x[i] = (y[i] - sum(u[i][j] * x[j] for j in range(i + 1, len(d)))) / u[i][i]
    print(f"  solution via L and U: {[round(v, 9) for v in x]}")
    print(f"  max error: {max(abs(a - b) for a, b in zip(x, m_true)):.3e} s/km")
    print("\nReading: L records the multipliers, U records the elimination result,")
    print("P records the row swaps. Factor once, solve many times: a second data")
    print("vector costs two triangular solves, not a second elimination.")

    section("5. Why pivoting is not optional")
    a_bad: Matrix = [[0.0, 2.0], [1.0, 3.0]]
    b_bad: Vector = [4.0, 4.0]
    print(f"  system A x = b with A = {a_bad}, b = {b_bad}")
    print("  no-pivot elimination:")
    naive = gauss_without_pivoting(a_bad, b_bad)
    print(f"    result: {naive}")
    print("  partial-pivot elimination:")
    with_pivot = gauss_solve(a_bad, b_bad, trace=False)
    print(f"    result: {[round(v, 6) for v in with_pivot]}")
    print(f"  check A x: {[round(v, 6) for v in matvec(a_bad, with_pivot)]}")
    print("\nReading: for this A the exact solution is x = (-2, 2). Without row")
    print("swapping the algorithm divides by a zero pivot at the first step and")
    print("there is nothing to divide by. The physics was never singular; the")
    print("*ordering* was.")

    section("6. Cost of elimination, and its scaling")
    print(f"  {'n':>6}  {'multiply-adds':>16}  {'ratio to n/2':>14}")
    previous = None
    for n in (8, 16, 32, 64, 128):
        elim, back = substitution_counts(n)
        total = elim + back
        ratio = "-" if previous is None else f"{total / previous:.4f}"
        print(f"  {n:>6}  {total:>16}  {ratio:>14}")
        previous = total
    print("  Ratios approach 8 per doubling: cost grows as n^3 / 3 to leading")
    print("  order. That is why sparsity (lesson 01-07-09) is not a refinement")
    print("  but a requirement.")

    section("7. A residual can be small while the answer is wrong")
    # Two rays through two cells with nearly identical path lengths.
    print(f"  {'delta':>8}  {'||G m - d||':>14}  {'model error':>14}")
    for delta in (1e-1, 1e-2, 1e-3, 1e-4):
        g2: Matrix = [[1.0, 1.0], [1.0, 1.0 + delta]]
        truth2 = [0.05, -0.02]
        d2 = matvec(g2, truth2)
        # Corrupt the second datum by 1 % of its own value.
        d2[1] *= 1.01
        x2 = gauss_solve(g2, d2, trace=False)
        residual = max(abs(v) for v in
                       [matvec(g2, x2)[i] - d2[i] for i in range(2)])
        error = max(abs(a - b) for a, b in zip(x2, truth2))
        print(f"  {delta:>8.0e}  {residual:>14.3e}  {error:>14.6f}")
    print("\nReading: the residual is at round-off level in every row, yet the")
    print("model error grows by a factor of ten each time delta shrinks by ten.")
    print("A small residual certifies consistency, not correctness. Quantifying")
    print("this gap is the subject of lesson 01-07-05.")


if __name__ == "__main__":
    main()
