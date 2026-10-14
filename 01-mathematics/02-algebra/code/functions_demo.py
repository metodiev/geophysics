"""Functions, graphs and transformations — tables instead of a plotting library.

Run:  python3 functions_demo.py
Requires: Python standard library only.

Companion to lesson 01-02-02. No third-party packages are needed: the "plot"
below is an ASCII grid, which is enough to see shape, intercepts, monotonicity
and asymptotic behaviour at reading distance.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 66}\n{title}\n{'=' * 66}")


def ascii_plot(f, x_min: float, x_max: float, width: int = 61,
               height: int = 15, label: str = "f") -> None:
    """Plot y = f(x) on a text grid; invert the y axis so up is +y."""
    xs = [x_min + (x_max - x_min) * i / (width - 1) for i in range(width)]
    ys = [f(x) for x in xs]
    y_min, y_max = min(ys), max(ys)
    if y_max == y_min:
        y_max = y_min + 1.0
    grid = [[" "] * width for _ in range(height)]
    for col, y in enumerate(ys):
        row = height - 1 - int((y - y_min) / (y_max - y_min) * (height - 1))
        grid[row][col] = "*"
    print(f"{label}  on x in [{x_min}, {x_max}], y in "
          f"[{y_min:.3f}, {y_max:.3f}]")
    for row_index, row in enumerate(grid):
        y_here = y_max - (y_max - y_min) * row_index / (height - 1)
        print(f"{y_here:>9.3f} |" + "".join(row))
    print(" " * 10 + "+" + "-" * width)
    print(" " * 10 + f"{x_min:<{width // 2}.3f}{x_max:>{width - width // 2}.3f}")


def main() -> None:
    section("1. A geophysical function and its inverse: velocity, time, depth")
    v = 6000.0  # m/s, a typical lower-crustal P-wave speed
    travel_time = lambda depth: depth / v          # f: depth -> time
    depth = lambda t: v * t                        # f^-1: time -> depth
    print(f"v = {v:.0f} m/s")
    for d in (1000.0, 5000.0, 30000.0):
        print(f"  depth {d:>8.0f} m -> t = {travel_time(d):.6f} s -> "
              f"recovered depth = {depth(travel_time(d)):.6f} m")
    print("f(f^-1(t)) = t only because f is strictly monotonic on this domain.")

    section("2. Transformations change the graph, not the physics")
    base = lambda x: 1.0 / (1.0 + x * x)          # a smooth bump, peak at x = 0
    grid = [(-5.0 + 0.01 * i) for i in range(1001)]
    for name, fn in (("f(x)", base),
                     ("f(x) + 0.5  (shift up)", lambda x: base(x) + 0.5),
                     ("f(x - 1)    (shift right)", lambda x: base(x - 1.0)),
                     ("2 f(x)      (stretch up)", lambda x: 2.0 * base(x)),
                     ("f(2x)       (compress x)", lambda x: base(2.0 * x)),
                     ("-f(x)       (reflect in x)", lambda x: -base(x))):
        x_peak = max(grid, key=fn)
        print(f"  {name:<26} f(0) = {fn(0.0):+.4f}   max over [-5,5] = "
              f"{fn(x_peak):+.4f} at x = {x_peak:+.2f}")
    print("The peak height and the peak position translate and scale exactly as")
    print("the transformation says, which is how an anomaly map is matched to the")
    print("body that caused it.")

    section("3. Same values, different shapes: linear, quadratic, exponential")
    print(f"{'x':>5} {'2x':>10} {'x**2':>10} {'2**x':>12}")
    for x in range(0, 11):
        print(f"{x:>5} {2 * x:>10} {x ** 2:>10} {2 ** x:>12}")
    print("At x = 10 the linear function has grown 20-fold, the quadratic")
    print("100-fold and the exponential 1024-fold. Exponential domination is")
    print("the reason decay and growth laws are written with e, not with x.")

    section("4. Rate of change of a depth-dependent property")
    # Temperature with depth in a conductive crust: T(z) = T0 + g*z.
    T0, gradient = 10.0, 25.0  # degC, degC/km
    T = lambda z: T0 + gradient * z
    print(f"T(z) = {T0} + {gradient} z  (z in km)")
    for z in (0.0, 1.0, 2.5, 5.0):
        avg_rate = (T(z + 0.5) - T(z)) / 0.5
        print(f"  z = {z:>4.1f} km: T = {T(z):>6.1f} degC, "
              f"average slope over 0.5 km = {avg_rate:.6f} degC/km")
    print("A linear function has the same slope everywhere; the average slope")
    print("over any interval equals the derivative. That is not true below.")

    section("5. Even, odd and superposed parts")
    # A function that is neither even nor odd can be split uniquely.
    f = lambda x: 1.0 + x + x ** 3
    even = lambda x: (f(x) + f(-x)) / 2.0
    odd = lambda x: (f(x) - f(-x)) / 2.0
    for x in (-2.0, -1.0, 1.0, 2.0):
        print(f"  x = {x:+.0f}: f = {f(x):+.3f}, even part = {even(x):+.3f}, "
              f"odd part = {odd(x):+.3f}, sum = {even(x) + odd(x):+.3f}")
    print("The even part is the constant 1, the odd part is x + x**3.")

    section("6. Asymptotics visible in a table")
    print(f"{'z (km)':>8} {'z/(1+z)':>12} {'1 - 1/(1+z**2)':>18} "
          f"{'(1+1/z)**z':>14}")
    for z in (1.0, 10.0, 100.0, 1000.0, 100000.0):
        print(f"{z:>8.0f} {z / (1 + z):>12.6f} {1 - 1 / (1 + z * z):>18.9f} "
              f"{(1 + 1 / z) ** z:>14.6f}")
    print(f"e = {math.e:.9f}: the last column approaches e, slowly, from below.")

    section("7. ASCII graph of a decaying oscillation")
    # A damped oscillation, the shape of a seismogram envelope.
    wave = lambda t: math.exp(-0.3 * t) * math.sin(2.0 * math.pi * t)
    ascii_plot(wave, 0.0, 10.0, width=61, height=13, label="exp(-0.3 t) sin(2 pi t)")
    print("Amplitude decays while the period stays fixed: the envelope is the")
    print("exponential and the zeros remain equally spaced.")


if __name__ == "__main__":
    main()
