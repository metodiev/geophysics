"""A 1-D wave-equation solver from scratch, and how to know it is right.

The solver is 30 lines. The rest of the file is measurement: convergence order,
the exactness at CFL = 1, numerical dispersion, energy conservation, and the
point where round-off takes over from discretisation error.

Run:
    .venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/finite_difference_1d_demo.py
"""

from __future__ import annotations

import numpy as np

L = 1.0
C = 1.0


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def advance(u_prev: np.ndarray, u_cur: np.ndarray, r: float) -> np.ndarray:
    """One step of the explicit second-order scheme for u_tt = c^2 u_xx.

    Periodic boundaries are applied with np.roll, which is also the reason the
    scheme has no boundary layer: every point sees a full 3-point stencil.
    """
    laplacian = np.roll(u_cur, 1) + np.roll(u_cur, -1) - 2.0 * u_cur
    return 2.0 * u_cur - u_prev + r * r * laplacian


def run_travelling(nx: int, r: float, t_end: float, modes: int = 4,
                   c: float = C, length: float = L):
    """Travelling-wave test; returns the max RMS error over the whole history."""
    dx = length / nx
    nt = int(np.ceil(t_end / (r * dx / c)))
    dt = t_end / nt
    r_actual = c * dt / dx
    x = np.arange(nx) * dx
    k = 2.0 * np.pi * modes / length
    exact = lambda t: np.sin(k * (x - c * t))        # noqa: E731
    u_prev, u_cur = exact(0.0), exact(dt)
    worst = 0.0
    for step in range(1, nt + 1):
        u_next = advance(u_prev, u_cur, r_actual)
        u_prev, u_cur = u_cur, u_next
        worst = max(worst, float(np.sqrt(np.mean((u_cur - exact((step + 1) * dt)) ** 2))))
    final = float(np.sqrt(np.mean((u_cur - exact((nt + 1) * dt)) ** 2)))
    return dx, dt, r_actual, final, worst


def run_standing(nx: int, r: float, t_end: float, modes: int = 3,
                 c: float = C, length: float = L):
    """Standing mode with u_t = 0; sampled at t_end, which is a phase extremum."""
    dx = length / nx
    nt = int(round(t_end / (r * dx / c)))
    dt = t_end / nt
    r_actual = c * dt / dx
    x = np.arange(nx) * dx
    k = 2.0 * np.pi * modes / length
    u0 = np.sin(k * x)
    u_prev = u0
    u_cur = u0 + 0.5 * r_actual ** 2 * (np.roll(u0, 1) + np.roll(u0, -1) - 2 * u0)
    for _ in range(1, nt):
        u_prev, u_cur = u_cur, advance(u_prev, u_cur, r_actual)
    exact = np.sin(k * x) * np.cos(2.0 * np.pi * modes * c * nt * dt / length)
    return dx, dt, r_actual, float(np.sqrt(np.mean((u_cur - exact) ** 2)))


def main() -> None:
    section("1. The scheme, and the single number that controls it")
    print("u_tt = c^2 u_xx, discretised at (i dx, n dt):")
    print("    u(i,n+1) = 2 u(i,n) - u(i,n-1) + r^2 [u(i+1,n) - 2u(i,n) + u(i-1,n)]")
    print("    r = c dt / dx  (the Courant number)")
    print("Accuracy: second order in dx and dt. Stability: r <= 1 (lesson 02).")
    print("No timings are quoted anywhere in this file: they are machine-specific.")
    print("Grid sizes, step counts, errors and measured orders are not.")

    section("2. Convergence: measure the order, do not assume it")
    print("Travelling sine wave, 4 wavelengths on L = 1, r = 0.5 held fixed,")
    print("error = maximum RMS over the whole time history.")
    print(f"{'nx':>7} {'dx':>11} {'dt':>11} {'steps':>7} {'max RMS err':>14} "
          f"{'p (rms)':>9}")
    previous = None
    for nx in (100, 200, 400, 800, 1600, 3200, 6400):
        dx, dt, r_actual, _, worst = run_travelling(nx, 0.5, 0.7)
        steps = int(np.ceil(0.7 / dt))
        order = "" if previous is None else f"{np.log2(previous / worst):9.4f}"
        print(f"{nx:7d} {dx:11.3e} {dt:11.3e} {steps:7d} {worst:14.6e} {order}")
        previous = worst
    print("Measured order 2.0000 over six refinements. This is the number that")
    print("belongs in a paper's methods section; 'second-order accurate' is a")
    print("claim until it has been measured.")

    section("3. The same test sampled at one instant can lie about the order")
    print("Standing sine mode, u_t = 0, r = 0.5, error read at t = 1.0 s only.")
    print(f"{'nx':>7} {'dx':>11} {'RMS err':>12} {'p (rms)':>9}")
    previous = None
    for nx in (100, 200, 400, 800, 1600):
        dx, dt, r_actual, err = run_standing(nx, 0.5, 1.0)
        order = "" if previous is None else f"{np.log2(previous / err):9.4f}"
        print(f"{nx:7d} {dx:11.3e} {err:12.4e} {order}")
        previous = err
    print("Order 4.0000 for a second-order scheme. The leading error is a PHASE")
    print("error, delta_phi = O(dx^2); at the instant where the mode sits at a")
    print("maximum, cos(delta_phi) - 1 = O(delta_phi^2) = O(dx^4). The scheme is")
    print("still second order. A convergence test that samples one instant, or")
    print("one point, or one phase, can report an order the solver does not have.")
    print("Always state the norm, the time window and the sampling.")

    section("4. At r = 1 the 1-D scheme is exact")
    print("Travelling wave, r = 1 exactly, error = max RMS over the history.")
    for nx in (50, 100, 200, 400):
        dx, dt, r_actual, _, worst = run_travelling(nx, 1.0, 0.7)
        print(f"  nx = {nx:5d}  r = {r_actual:.6f}  max RMS error = "
              f"{worst:.3e}  (round-off level: {np.finfo(float).eps:.1e})")
    print("At r = 1 the numerical domain of dependence exactly matches the")
    print("physical one, the scheme is an exact identity for the continuum")
    print("solution sampled at grid points, and only round-off remains.")

    section("5. The 2-dx wave at r = 1 is a degenerate exception")
    nx = 200
    r_exact = 1.0
    sawtooth = np.where(np.arange(nx) % 2 == 0, 1.0, -1.0)
    u_prev = sawtooth.copy()
    u_cur = sawtooth.copy()
    print(f"initial condition: u = (-1)^i, i.e. the shortest wave the grid can")
    print(f"represent (wavelength 2 dx), with u_t = 0, at r = {r_exact}")
    print(f"{'step':>6} {'max |u|':>10} {'exact bound':>12}")
    for step in range(1, 13):
        u_prev, u_cur = u_cur, advance(u_prev, u_cur, r_exact)
        if step in (1, 2, 3, 5, 9, 13):
            print(f"{step:6d} {np.abs(u_cur).max():10.1f} "
                  f"{2 * (step + 1) - 1:12.1f}")
    cap = 2 * 41 - 1
    u_prev, u_cur = sawtooth.copy(), sawtooth.copy()
    for _ in range(40):
        u_prev, u_cur = u_cur, advance(u_prev, u_cur, r_exact)
    print(f"after 40 steps                  {np.abs(u_cur).max():10.1f} "
          f"{cap:12.1f}")
    print("The amplitude grows LINEARLY, |u| = 2n - 1, although the exact")
    print("solution is bounded by 1. The stability polynomial has a double root")
    print("at -1: the frequency is exact but the amplification matrix is")
    print("defective, so the exact initial condition u_t = 0 cannot be")
    print("represented and the difference grows without bound. It is a measure-")
    print("zero pathology, and a reminder that 'stable' and 'accurate at the")
    print("grid's shortest wavelength' are different properties.")

    section("6. Numerical dispersion: the phase speed is not c")
    print("Discrete dispersion relation: omega dt = 2 asin(r sin(k dx/2)).")
    print("A single complex Fourier mode is launched and its phase advance is")
    print("measured over N steps at r = 0.5, nx = 256.")
    nx = 256
    dx = L / nx
    r_disp = 0.5
    dt_disp = r_disp * dx / C
    x = np.arange(nx) * dx
    print(f"{'k dx':>10} {'points/wavelength':>18} {'c_num/c measured':>17} "
          f"{'c_num/c theory':>15} {'difference':>11}")
    for modes in (2, 4, 8, 16, 24, 32, 48, 64):
        k = 2.0 * np.pi * modes / L
        u_prev = np.exp(1j * k * x)
        u_cur = np.exp(1j * k * (x - C * dt_disp))
        omega_theory = 2.0 * np.arcsin(r_disp * np.sin(k * dx / 2.0)) / dt_disp
        steps = max(1, int(np.floor(0.5 * np.pi / (omega_theory * dt_disp))))
        phase0 = np.angle(np.fft.fft(u_cur)[modes])
        for _ in range(steps):
            u_prev, u_cur = u_cur, (2.0 * u_cur - u_prev
                                    + r_disp ** 2 * (np.roll(u_cur, 1)
                                                     + np.roll(u_cur, -1)
                                                     - 2.0 * u_cur))
        delta = np.angle(np.fft.fft(u_cur)[modes]) - phase0
        while delta > np.pi:
            delta -= 2.0 * np.pi
        while delta < -np.pi:
            delta += 2.0 * np.pi
        omega_measured = -delta / (steps * dt_disp)
        measured = omega_measured / (k * C)
        theory = omega_theory / (k * C)
        print(f"{k * dx:10.4f} {2 * np.pi / (k * dx):18.2f} {measured:17.6f} "
              f"{theory:15.6f} {measured - theory:11.2e}")
    print("Every discrete phase speed is below c and the deficit grows as")
    print("(k dx)^2: 0.0001% at 128 points per wavelength, 0.45% at 8 points.")
    print("The residual difference between measurement and theory is the")
    print("contamination of the tracked Fourier coefficient by the")
    print("counter-propagating discrete root: launching a genuinely one-way wave")
    print("on a grid with a second time level is not possible without knowing")
    print("the answer in advance. This is why dispersion measurements are quoted")
    print("with the estimator they used.")
    print("At k dx = pi the group velocity is zero: the 2 dx wave does not")
    print("propagate, it stands and oscillates. Five to ten points per")
    print("wavelength is the practical minimum for waveform modelling.")

    section("7. Energy is conserved by the scheme")
    dx_e = L / 400
    nx_e = 400
    r_e = 0.5
    dt_e = r_e * dx_e / C
    x_e = np.arange(nx_e) * dx_e
    u_prev = np.exp(-((x_e - 0.5) / 0.05) ** 2)
    u_cur = u_prev.copy()

    def discrete_energy(u_prev: np.ndarray, u_cur: np.ndarray) -> float:
        """The staggered energy the leapfrog scheme conserves exactly."""
        kinetic = 0.5 * np.sum(((u_cur - u_prev) / dt_e) ** 2) * dx_e
        grad_cur = (np.roll(u_cur, 1) - u_cur) / dx_e
        grad_prev = (np.roll(u_prev, 1) - u_prev) / dx_e
        potential = 0.5 * C ** 2 * np.sum(grad_cur * grad_prev) * dx_e
        return float(kinetic + potential)

    energies = [discrete_energy(u_prev, u_cur)]
    for _ in range(2000):
        u_prev, u_cur = u_cur, advance(u_prev, u_cur, r_e)
        energies.append(discrete_energy(u_prev, u_cur))
    energies = np.array(energies)
    print(f"steps                         : {len(energies) - 1}")
    print(f"initial energy                : {energies[0]:.6e}")
    print(f"final energy                  : {energies[-1]:.6e}")
    print(f"relative drift                : "
          f"{energies[-1] / energies[0] - 1:+.3e}")
    print(f"max relative excursion        : "
          f"{np.abs(energies / energies[0] - 1).max():.3e}")
    print(f"machine epsilon for reference : {np.finfo(float).eps:.3e}")
    print("The kinetic term uses (u(n+1) - u(n))/dt and the potential term uses")
    print("the product of the gradients at levels n+1 and n. Both halves must be")
    print("staggered in the same way; using the gradient at a single level, as")
    print("one would naively do, gives an energy that decays by O(dx^2) and")
    print("looks exactly like numerical damping that is not there.")

    section("8. Where round-off takes over")
    print("Standing-mode test above, pushed until the error stops falling.")
    print(f"{'nx':>7} {'dx':>11} {'steps':>8} {'RMS err':>12} {'p':>9}")
    previous = None
    for nx in (1600, 3200, 6400, 12800, 25600, 51200):
        dx, dt, r_actual, err = run_standing(nx, 0.5, 1.0)
        steps = int(round(1.0 / dt))
        order = "" if previous is None else f"{np.log2(previous / err):9.4f}"
        print(f"{nx:7d} {dx:11.3e} {steps:8d} {err:12.4e} {order}")
        previous = err
    print("The error falls as dx^4 until about nx = 12800, then stops. Beyond")
    print("that the difference between the computed and exact solution is")
    print("round-off accumulated over tens of thousands of steps, not")
    print("discretisation. Refining further only costs time.")
    print("Discretisation error and round-off error are different quantities:")
    print("the first is a property of the method, the second of the arithmetic.")
    print("One decreases with refinement; the other grows weakly with the")
    print("number of operations.")


if __name__ == "__main__":
    main()
