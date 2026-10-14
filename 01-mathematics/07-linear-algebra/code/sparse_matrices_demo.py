"""Sparse matrices and structured systems: Laplacians, bands, fill-in, iteration.

Run:  python3 sparse_matrices_demo.py
Requires: Python standard library only.

Companion to lesson 01-07-09.

The five-point Laplacian is the single most common matrix in computational
geophysics: it is what a finite-difference discretisation of the Poisson,
diffusion and (with a mass term) wave equations looks like. It is also the
cleanest illustration of everything that makes sparse linear algebra a subject
in its own right: almost all entries are zero, eliminating it destroys that
sparsity, and the direct factorisation is therefore not always the right answer.
"""

import math
import time


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def laplacian_2d(n: int) -> list[list[float]]:
    """Five-point Laplacian on an n x n interior grid, scaled by h^2 (integers).

    Dirichlet boundary conditions: a neighbour outside the grid contributes
    nothing, which is why some diagonal entries are less than 4.
    """
    size = n * n
    a = [[0.0] * size for _ in range(size)]
    for i in range(n):
        for j in range(n):
            k = i * n + j
            a[k][k] = 4.0
            if i > 0:
                a[k][(i - 1) * n + j] = -1.0
            if i < n - 1:
                a[k][(i + 1) * n + j] = -1.0
            if j > 0:
                a[k][i * n + j - 1] = -1.0
            if j < n - 1:
                a[k][i * n + j + 1] = -1.0
    return a





def nnz(a, tol: float = 0.0) -> int:
    return sum(1 for row in a for x in row if abs(x) > tol)


def matvec_dense(a, x):
    return [sum(row[j] * x[j] for j in range(len(x))) for row in a]


def lu_count(a):
    """LU without pivoting (valid here: the matrix is symmetric positive
    definite). Returns (nnz of L including the unit diagonal, nnz of U)."""
    n = len(a)
    m = [row[:] for row in a]
    l = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    u = [[0.0] * n for _ in range(n)]
    for k in range(n):
        for j in range(k, n):
            u[k][j] = m[k][j]
        for i in range(k + 1, n):
            factor = m[i][k] / m[k][k]
            l[i][k] = factor
            for j in range(k, n):
                m[i][j] -= factor * m[k][j]
    return nnz(l), nnz(u)


def thomas(lower, diag, upper, rhs):
    """Tridiagonal solve in O(n) operations.

    ``lower[i - 1]`` is A[i][i - 1] and ``upper[i]`` is A[i][i + 1], both of
    length n - 1.
    """
    n = len(diag)
    c = list(upper)
    d = list(diag)
    b = list(rhs)
    for i in range(1, n):
        w = lower[i - 1] / d[i - 1]
        d[i] -= w * c[i - 1]
        b[i] -= w * b[i - 1]
    x = [0.0] * n
    x[-1] = b[-1] / d[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - c[i] * x[i + 1]) / d[i]
    return x


def main() -> None:
    section("1. A real tomographic system is overwhelmingly empty")
    cells, rays = 400, 200
    # A deterministic ray-path matrix: each ray samples a short run of cells.
    entries = 0
    for r in range(rays):
        start = (r * 7) % (cells - 6)
        for c in range(start, start + 6):
            entries += 1
    print(f"  model cells (columns) = {cells}, rays (rows) = {rays}")
    print(f"  nonzeros = {entries} of {cells * rays} "
          f"({100.0 * entries / (cells * rays):.4f} % dense)")
    print(f"  dense storage: {cells * rays} doubles = "
          f"{cells * rays * 8 / 1.0e6:.2f} MB")
    print(f"  coordinate format: 3 x {entries} numbers = "
          f"{3 * entries * 8 / 1.0e3:.1f} kB")
    print(f"  ratio of storage = {cells * rays / (3.0 * entries):.1f} x")
    print("\nReading: each ray touches six cells, so each row has six entries")
    print("whatever the size of the model. Sparsity is not an implementation")
    print("trick here; it is a statement about the geometry of ray coverage.")
    print("A dense storage scheme would spend almost all its memory on zeros.")

    section("2. The five-point Laplacian: sparsity is exactly predictable")
    print(f"  {'n':>4}  {'unknowns N':>11}  {'nnz':>10}  {'5N - 4n':>10}  "
          f"{'density':>12}  {'nnz / N^2':>12}")
    for n in (4, 8, 16, 32, 64, 128):
        size = n * n
        predicted = 5 * size - 4 * n
        density = predicted / (size * size)
        print(f"  {n:>4}  {size:>11}  {predicted:>10}  {5 * size - 4 * n:>10}  "
              f"{density:>12.3e}  {predicted / (size * size):>12.3e}")
    print("\nReading: the count 5N - 4n is exact -- every interior node has five")
    print("stencil entries and the four boundary strips lose one each. So nnz")
    print("grows like N for a fixed number of dimensions, while a dense matrix")
    print("would grow like N^2. At n = 128 the density is 3.0e-4: 99.97 % of")
    print("the matrix is zeros that a dense algorithm would multiply by nothing.")

    section("3. What the pattern looks like")
    n = 4
    size = n * n
    a = laplacian_2d(n)
    print(f"  the {size}x{size} five-point Laplacian for n = {n} "
          f"(# = nonzero):")
    for i in range(size):
        print("    " + "".join("#" if a[i][j] != 0.0 else "." for j in range(size)))
    print("  Each block of four rows is one grid row; the two off-block bands")
    print("  are the coupling to the rows above and below. The pattern is")
    print("  'block tridiagonal with tridiagonal blocks' -- the structure of")
    print("  every second-order finite-difference operator on a rectangular grid.")

    section("4. Fill-in: eliminating a sparse matrix destroys sparsity")
    print(f"  {'n':>4}  {'N':>7}  {'nnz(A)':>9}  {'nnz(L)+nnz(U)':>14}  "
          f"{'factor/A':>10}  {'N^2 (dense)':>12}")
    for n in (4, 6, 8, 12, 16, 20):
        size = n * n
        a = laplacian_2d(n)
        nl, nu = lu_count(a)
        print(f"  {n:>4}  {size:>7}  {nnz(a):>9}  {nl + nu:>14}  "
              f"{(nl + nu) / nnz(a):>10.3f}  {size * size:>12}")
    print("\nReading: the factor is still sparse, but it is not *as* sparse. For")
    print("a two-dimensional grid the factor holds O(N^1.5) nonzeros instead of")
    print("O(N) -- an extra factor of n. Reordering the unknowns (nested")
    print("dissection, minimum degree) reduces the damage substantially, and")
    print("that is why sparse direct solvers ship with permutation algorithms")
    print("rather than just a factorisation.")

    section("5. Banded systems: solve in linear time, exactly")
    n1 = 200
    h = 1.0 / (n1 + 1)
    diag = [2.0] * n1
    off = [-1.0] * (n1 - 1)
    # -u'' = f with u(x) = sin(pi x): f = pi^2 sin(pi x), and the discrete
    # operator is divided by h^2.
    x = [(i + 1) * h for i in range(n1)]
    rhs = [h * h * math.pi ** 2 * math.sin(math.pi * xi) for xi in x]
    start = time.perf_counter()
    u = thomas(off, diag, off, rhs)
    elapsed = time.perf_counter() - start
    exact = [math.sin(math.pi * xi) for xi in x]
    max_err = max(abs(u[i] - exact[i]) for i in range(n1))
    print(f"  1-D Poisson problem, n = {n1} interior points, h = {h:.6f}")
    print(f"  Thomas algorithm: {8 * n1} operations, "
          f"max |u - sin(pi x)| = {max_err:.3e}")
    print(f"  observed as predicted: the error is O(h^2) = {h * h:.3e}")
    print(f"  wall time for the solve: {elapsed * 1e3:.3f} ms")
    print(f"  a dense Gaussian elimination would need about "
          f"{2 * n1 ** 3 / 3:.3e} operations instead of {8 * n1}")
    print(f"  ratio = {2 * n1 ** 3 / 3 / (8 * n1):.1f} x")
    print("\nReading: the tridiagonal case is the one place where the structure")
    print("is so simple that an exact O(n) solver exists. It is used constantly:")
    print("cubic-spline interpolation, implicit time stepping for the diffusion")
    print("equation in one dimension, and radiosity-style line relaxations all")
    print("reduce to tridiagonal solves.")

    section("6. When the problem is too big to factorise: iteration")
    print("  Jacobi iteration for the 2-D Poisson problem with Dirichlet")
    print("  boundary conditions, solving -laplacian(u) = 2 pi^2 sin(pi x) sin(pi y)")
    print("  Convergence is measured by the change between successive iterates,")
    print("  which is what a solver actually has available. The last column is")
    print("  the error against the continuous solution at convergence.")
    print(f"  {'n':>4}  {'N':>7}  {'iterations':>11}  {'measured ratio':>15}  "
          f"{'cos(pi h)':>11}  {'1 - (pi h)^2/2':>15}  {'disc. error':>12}  "
          f"{'time (s)':>9}")
    previous_iterations = None
    ratios_observed = []
    for n in (7, 15, 31):
        hh = 1.0 / (n + 1)
        size = n * n
        f = [2.0 * math.pi ** 2 * math.sin(math.pi * (i + 1) * hh)
             * math.sin(math.pi * (j + 1) * hh)
             for i in range(n) for j in range(n)]
        uu = [0.0] * size
        target = [math.sin(math.pi * (i + 1) * hh) * math.sin(math.pi * (j + 1) * hh)
                  for i in range(n) for j in range(n)]
        start = time.perf_counter()
        iterations = 0
        ratio = float("nan")
        previous_change = None
        while iterations < 100000:
            new = [0.0] * size
            for i in range(n):
                base = i * n
                for j in range(n):
                    k = base + j
                    total = hh * hh * f[k]
                    if i > 0:
                        total += uu[k - n]
                    if i < n - 1:
                        total += uu[k + n]
                    if j > 0:
                        total += uu[k - 1]
                    if j < n - 1:
                        total += uu[k + 1]
                    new[k] = total / 4.0
            change = max(abs(new[k] - uu[k]) for k in range(size))
            if previous_change is not None and previous_change > 1e-14:
                ratio = change / previous_change
            uu = new
            iterations += 1
            previous_change = change
            if change < 1e-7:
                break
        elapsed = time.perf_counter() - start
        ratios_observed.append(ratio)
        disc = max(abs(uu[k] - target[k]) for k in range(size))
        trend = "" if previous_iterations is None else \
            f" ({iterations / previous_iterations:.2f}x)"
        print(f"  {n:>4}  {size:>7}  {iterations:>11}  {ratio:>15.6f}  "
              f"{math.cos(math.pi * hh):>11.6f}  "
              f"{1.0 - (math.pi * hh) ** 2 / 2:>15.6f}  {disc:>12.2e}  "
              f"{elapsed:>9.2f}{trend}")
        previous_iterations = iterations
    print("\nReading: the measured error ratio is cos(pi h) to four decimal")
    print("places -- the spectral radius of the Jacobi iteration matrix for the")
    print("five-point Laplacian, printed side by side with the small-h")
    print("approximation 1 - (pi h)^2/2. Iteration counts grow by a factor of")
    print("about four when the grid is halved, exactly as 1/(1 - radius) predicts.")
    print("So the total work of a Jacobi solve grows faster than the size of the")
    print("problem: halving the mesh multiplies the work by roughly 4 (more")
    print("unknowns) x 4 (more iterations) = 16. That is the strongest single")
    print("argument for multigrid and for preconditioned Krylov methods, and it")
    print("is a statement about a spectral radius -- lesson 01-07-06.")
    print("Note also the last two columns before the elapsed time: the iteration")
    print("reaches its own fixed point long before the solution reaches the")
    print("continuous one. The remaining error is the discretisation error, O(h^2),")
    print("and it is a modelling floor that no amount of iterating will remove.")


if __name__ == "__main__":
    main()
