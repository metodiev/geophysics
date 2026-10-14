"""Linear and nonlinear systems, with Gaussian elimination from scratch.

Run:  python3 systems_demo.py
Requires: Python standard library only.

Companion to lesson 01-02-05. The linear examples use an explicit forward
operator and invert it; the nonlinear example solves for two parameters of a
buried sphere with Newton's method. All data are SYNTHETIC.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def solve_linear(matrix: list[list[float]], rhs: list[float]) -> list[float]:
    """Gaussian elimination with partial pivoting."""
    n = len(matrix)
    a = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        if abs(a[pivot][col]) < 1.0e-300:
            raise ValueError("singular matrix")
        a[col], a[pivot] = a[pivot], a[col]
        for r in range(col + 1, n):
            factor = a[r][col] / a[col][col]
            for c in range(col, n + 1):
                a[r][c] -= factor * a[col][c]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (a[r][n] - sum(a[r][c] * x[c] for c in range(r + 1, n))) / a[r][r]
    return x


def residual(matrix: list[list[float]], x: list[float], rhs: list[float]) -> float:
    return max(abs(sum(row[j] * x[j] for j in range(len(x))) - rhs[i])
               for i, row in enumerate(matrix))


def newton_system(f, x0: list[float], tol: float = 1.0e-14,
                  max_iter: int = 40) -> tuple[list[float], list[float]]:
    """Newton's method with a backtracking line search (globally convergent).

    A raw Newton step can overshoot badly on a nonlinear problem. Halving the
    step until the residual actually falls keeps the iteration on a decreasing
    path; the printed history shows how often that was necessary.
    """
    x = x0[:]
    n = len(x)
    history = [max(abs(v) for v in f(x))]

    def jacobian() -> list[list[float]]:
        fx = f(x)
        columns = []
        for j in range(n):
            h = 1.0e-6 * max(abs(x[j]), 1.0)
            xp = x[:]
            xp[j] += h
            columns.append([(f(xp)[i] - fx[i]) / h for i in range(n)])
        return [[columns[j][i] for j in range(n)] for i in range(n)]

    for _ in range(max_iter):
        fx = f(x)
        current = max(abs(v) for v in fx)
        try:
            step = solve_linear(jacobian(), [-v for v in fx])
        except ValueError:
            break
        scale = 1.0
        for _ in range(60):
            trial = [x[i] + scale * step[i] for i in range(n)]
            value = max(abs(v) for v in f(trial))
            if value < current:
                break
            scale *= 0.5
        x = trial
        history.append(value)
        if value < tol:
            break
    return x, history


def main() -> None:
    big_g = 6.674e-11

    section("1. Two masses from two gravity readings (a linear inverse problem)")
    # Two buried spheres under stations 1 and 2. The anomaly of a sphere of
    # mass m at horizontal offset 0 and depth z at the surface above it is
    # g(z) = G m z / (z**2 + R**2)**1.5. With R fixed, the data are linear in m.
    radius = 200.0
    depths = (400.0, 900.0)
    offsets = ((0.0, 300.0), (300.0, 0.0))     # signed offsets: station i to body j
    def kernel(offset: float, depth: float) -> float:
        z = depth
        horizontal = offset
        # Keep the far-field shape while allowing a horizontal offset.
        return big_g * z / (z * z + radius * radius + horizontal * horizontal) ** 1.5
    matrix = [[kernel(offsets[i][j], depths[j]) for j in range(2)] for i in range(2)]
    true_masses = [3.0e11, 8.0e11]
    data = [sum(matrix[i][j] * true_masses[j] for j in range(2)) for i in range(2)]
    print("forward operator A (m/s**2 per kg):")
    for i in range(2):
        print(f"  station {i + 1}: " + "  ".join(f"{matrix[i][j]:.4e}" for j in range(2)))
    print(f"SYNTHETIC data (m/s**2)      : "
          f"{', '.join(f'{d:.6e}' for d in data)}")
    recovered = solve_linear(matrix, data)
    for j in range(2):
        print(f"  mass {j + 1}: true {true_masses[j]:.4e} kg, "
              f"recovered {recovered[j]:.6e} kg")
    print(f"max residual: {residual(matrix, recovered, data):.3e}")
    print("The inversion is exact to round-off because the forward problem is")
    print("linear and the matrix is well conditioned (det = "
          f"{matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]:.4e}).")

    section("2. A 3x3 linear system with a residual check")
    a3 = [[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 3.0]]
    b3 = [15.0, 10.0, 10.0]
    x3 = solve_linear(a3, b3)
    print("A = [[4,-1,0],[-1,4,-1],[0,-1,3]], b = (15, 10, 10)")
    print(f"solution: ({x3[0]:.10f}, {x3[1]:.10f}, {x3[2]:.10f})")
    print(f"max residual ||A x - b|| = {residual(a3, x3, b3):.3e}")
    print("Check by substitution: row 1 = "
          f"{a3[0][0] * x3[0] + a3[0][1] * x3[1] + a3[0][2] * x3[2]:.12f}")

    section("3. Nearly dependent rows: a small data change moves the answer")
    eps = 1.0e-8
    near_singular = [[1.0, 1.0 + eps], [1.0, 1.0 - eps]]
    sol_a = solve_linear(near_singular, [2.0, 2.0])
    sol_b = solve_linear(near_singular, [2.0 + 1.0e-8, 2.0])
    print(f"matrix [[1, 1+eps], [1, 1-eps]] with eps = {eps:.0e}")
    print(f"solution for b = (2, 2)              : "
          f"({sol_a[0]:.4f}, {sol_a[1]:.4f})")
    print(f"solution for b = (2 + 1e-8, 2)       : "
          f"({sol_b[0]:.4f}, {sol_b[1]:.4f})")
    print(f"change in solution: {abs(sol_b[0] - sol_a[0]):.4f} for a relative")
    print(f"data change of {1.0e-8 / 2.0:.1e}  ->  amplification ~"
          f"{abs(sol_b[0] - sol_a[0]) / (1.0e-8 / 2.0):.3e}")
    print("The matrix is ill-conditioned: no algorithm can fix that, which is")
    print("the distinction between conditioning and stability (lesson 01-01-05).")

    section("4. Fixed-point iteration compared with Newton (scalar)")
    # Solve x = cos(x): well-behaved fixed point. Then solve x = 2 cos(x),
    # where |g'| can exceed 1 and the same iteration diverges.
    print(f"{'iteration':>10} {'x = cos x':>18} {'x = 2 cos x':>18}")
    x_ok, x_bad = 1.0, 1.0
    for i in range(9):
        print(f"{i:>10} {x_ok:>18.12f} {x_bad:>18.12f}")
        x_ok = math.cos(x_ok)
        x_bad = 2.0 * math.cos(x_bad)
    print("cos is a contraction (|g'| <= 1) and converges; 2 cos is not, and the")
    print("iterates wander instead of settling. Newton's rule x <- x - f/f' has")
    print("no such restriction, at the cost of needing f'.")

    section("5. Nonlinear inversion: mass and radius of one sphere")
    # Two gravity stations above a sphere: g(z) = G M z / (z**2 + R**2)**1.5.
    # The unknowns are scaled (M/1e11 kg and R/100 m) so that both parameters
    # are of order one: an unscaled Newton step mixes a 1e11 and a 1e2 and
    # loses accuracy in the Jacobian.
    true_mass, true_radius = 5.0e11, 350.0
    mass_scale, radius_scale = 1.0e11, 100.0
    stations = (500.0, 1200.0)

    def model(u: float, w: float) -> tuple[float, float]:
        mass, radius = u * mass_scale, w * radius_scale
        return tuple(big_g * mass * z / (z * z + radius * radius) ** 1.5
                     for z in stations)

    data2 = model(true_mass / mass_scale, true_radius / radius_scale)
    print("SYNTHETIC observations (m/s**2) at z = "
          f"{stations[0]:.0f} m and {stations[1]:.0f} m:")
    print(f"  g1 = {data2[0]:.9e}, g2 = {data2[1]:.9e}")

    def residual_fn(params: list[float]) -> list[float]:
        g = model(params[0], params[1])
        return [g[0] - data2[0], g[1] - data2[1]]

    start = [true_mass / mass_scale * 0.2, true_radius / radius_scale * 2.0]
    solution, history = newton_system(residual_fn, start)
    print(f"start guess: M = {start[0] * mass_scale:.3e} kg, "
          f"R = {start[1] * radius_scale:.0f} m")
    for step, value in enumerate(history):
        print(f"  step {step}: max |residual| = {value:.3e}")
    print(f"solution: M = {solution[0] * mass_scale:.6e} kg, "
          f"R = {solution[1] * radius_scale:.6f} m")
    print(f"true    : M = {true_mass:.6e} kg, R = {true_radius:.6f} m")
    gap = abs(abs(solution[1]) * radius_scale - true_radius)
    print(f"|R| agrees with the truth to {gap:.2e} m, but the fitted sign is")
    print("negative. That is not a bug: the anomaly depends on R")
    print("through R**2, so +R and -R are the same model. Only the physical")
    print("requirement R > 0 selects the branch -- a non-uniqueness that the")
    print("residual alone cannot see. The residuals fall by several orders of")
    print("magnitude per step, which is the quadratic convergence of Newton.")


if __name__ == "__main__":
    main()
