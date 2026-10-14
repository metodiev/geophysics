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
    # g(x) = G m h / ((x - p)**2 + h**2)**1.5 is the vertical attraction of a
    # point mass: m at horizontal position p, depth h, observed at offset x.
    # With the positions and depths fixed, the data are linear in the masses.
    positions = (0.0, 400.0)
    depths = (400.0, 900.0)
    stations = (0.0, 400.0)

    def kernel(station_x: float, body_x: float, body_h: float) -> float:
        dx = station_x - body_x
        return big_g * body_h / (dx * dx + body_h * body_h) ** 1.5

    matrix = [[kernel(stations[i], positions[j], depths[j]) for j in range(2)]
              for i in range(2)]
    true_masses = [3.0e11, 8.0e11]
    data = [sum(matrix[i][j] * true_masses[j] for j in range(2)) for i in range(2)]
    print("forward operator A (m/s**2 per kg):")
    for i in range(2):
        print(f"  station x = {stations[i]:>5.0f} m: "
              + "  ".join(f"{matrix[i][j]:.4e}" for j in range(2)))
    print(f"SYNTHETIC data (m/s**2)      : "
          f"{', '.join(f'{d:.6e}' for d in data)}")
    recovered = solve_linear(matrix, data)
    for j in range(2):
        print(f"  mass {j + 1}: true {true_masses[j]:.4e} kg, "
              f"recovered {recovered[j]:.6e} kg")
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    inverse_columns = [solve_linear(matrix, [1.0 if i == j else 0.0
                                             for i in range(2)])
                       for j in range(2)]
    norm_a = max(sum(abs(v) for v in row) for row in matrix)
    norm_inverse = max(sum(abs(inverse_columns[j][i]) for j in range(2))
                       for i in range(2))
    print(f"max residual: {residual(matrix, recovered, data):.3e}")
    print(f"det(A) = {det:.4e}, cond_inf(A) = {norm_a * norm_inverse:.3f}")
    print("The geometry keeps the two responses distinct, so the problem is")
    print("invertible and (as the condition number shows) only mildly sensitive")
    print("to errors in the data.")

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

    section("5. Nonlinear inversion: mass and depth of one buried point mass")
    # g(x) = G m h / ((x - p)**2 + h**2)**1.5, with the horizontal position p
    # fixed by the symmetry of the profile. Two stations then determine (m, h).
    # The unknowns are parameterised as log(m) and log(h) so that the iteration
    # cannot wander into negative mass or negative depth.
    true_mass, true_position, true_depth = 5.0e11, 0.0, 350.0
    mass_scale, depth_scale = 1.0e11, 100.0
    stations = (-300.0, 400.0)

    def profile(mass: float, position: float, depth: float, x: float) -> float:
        dx = x - position
        return big_g * mass * depth / (dx * dx + depth * depth) ** 1.5

    data2 = tuple(profile(true_mass, true_position, true_depth, x)
                  for x in stations)
    print("SYNTHETIC observations (m/s**2) at x = "
          f"{stations[0]:.0f} m and x = {stations[1]:.0f} m:")
    print(f"  g1 = {data2[0]:.9e}, g2 = {data2[1]:.9e}")

    def residual_fn(params: list[float]) -> list[float]:
        mass = mass_scale * math.exp(params[0])
        depth = depth_scale * math.exp(params[1])
        return [profile(mass, true_position, depth, x) - d
                for x, d in zip(stations, data2)]

    start = [math.log(0.5), math.log(1.5)]
    solution, history = newton_system(residual_fn, start)
    print(f"start guess: m = {mass_scale * math.exp(start[0]):.3e} kg, "
          f"h = {depth_scale * math.exp(start[1]):.1f} m  "
          f"(log-parameterised)")
    for step, value in enumerate(history):
        print(f"  step {step}: max |residual| = {value:.3e}")
    print(f"solution: m = {mass_scale * math.exp(solution[0]):.6e} kg, "
          f"h = {depth_scale * math.exp(solution[1]):.6f} m")
    print(f"true    : m = {true_mass:.6e} kg, h = {true_depth:.6f} m")
    print("The amplitude of the profile fixes the mass and its shape fixes the")
    print("depth, so two stations are enough once the position is known.")

    section("6. The same data, a different answer: an underdetermined problem")
    # Now let the horizontal position be an unknown as well: three unknowns,
    # two measurements. For each assumed position there is an exact (mass,
    # depth) pair, obtained in closed form from the ratio of the two readings.
    g1, g2 = data2
    ratio = (g1 / g2) ** (2.0 / 3.0)
    print("solving the ratio equation in closed form for each assumed position:")
    print(f"{'assumed position':>17} {'mass (kg)':>14} {'depth (m)':>12} "
          f"{'max |residual|':>16}")
    for assumed in (0.0, -60.0, -150.0, -250.0):
        left, right = stations[0] - assumed, stations[1] - assumed
        depth_squared = (right * right - ratio * left * left) / (ratio - 1.0)
        depth = math.sqrt(depth_squared)
        mass = g1 * (left * left + depth_squared) ** 1.5 / (big_g * depth)
        value = max(abs(profile(mass, assumed, depth, x) - d)
                    for x, d in zip(stations, data2))
        print(f"{assumed:>17.0f} {mass:>14.6e} {depth:>12.4f} {value:>16.3e}")
    print("Every row reproduces the two observations to round-off, yet the")
    print("models differ in position by 250 m and in mass by a factor of 4.6.")
    print("Three unknowns with two measurements is underdetermined: the residual")
    print("cannot choose between them. A third station, or a physical constraint")
    print("on the position, is required.")


if __name__ == "__main__":
    main()
