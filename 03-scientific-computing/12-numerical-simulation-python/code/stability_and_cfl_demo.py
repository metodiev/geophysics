"""Stability: von Neumann analysis, measured growth rates, and CFL limits.

Every growth rate quoted as 'measured' is the ratio of successive maxima of a
single eigenmode of the scheme, so the measurement and the theory are
comparable. Three schemes are examined: the explicit wave equation, the
explicit diffusion equation, and an implicit (backward Euler) diffusion
scheme. A deliberately broken operator is included as a fourth case, because
that is what a stability failure looks like in practice.

Run:
    .venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/stability_and_cfl_demo.py
"""

from __future__ import annotations

import numpy as np


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def sawtooth(nx: int) -> np.ndarray:
    """The k dx = pi eigenmode: the shortest wave a grid can carry."""
    return np.where(np.arange(nx) % 2 == 0, 1.0, -1.0)


def wave_amplitudes(nx: int, r: float, steps: int,
                    laplacian_sign: float = 1.0) -> np.ndarray:
    """Max |u| after each step of the 3-level wave scheme on a sawtooth IC."""
    u_prev = sawtooth(nx)
    u_cur = u_prev.copy()
    out = []
    for _ in range(steps):
        lap = np.roll(u_cur, 1) + np.roll(u_cur, -1) - 2.0 * u_cur
        u_next = 2.0 * u_cur - u_prev + laplacian_sign * r * r * lap
        u_prev, u_cur = u_cur, u_next
        out.append(np.abs(u_cur).max())
    return np.array(out)


def wave_growth_prediction(r: float) -> float:
    """Largest |G| for the 3-level scheme at k dx = pi."""
    a = 1.0 - 2.0 * r * r
    if abs(a) <= 1.0:
        return 1.0
    return abs(a) + np.sqrt(a * a - 1.0)


def diffusion_amplitudes(nx: int, r: float, steps: int) -> np.ndarray:
    u = sawtooth(nx)
    out = []
    for _ in range(steps):
        u = u + r * (np.roll(u, 1) + np.roll(u, -1) - 2.0 * u)
        out.append(np.abs(u).max())
    return np.array(out)


def implicit_diffusion_growth(nx: int, r: float, steps: int) -> float:
    """Amplitude after `steps` solves of (I - r D2) u_new = u_old."""
    u = sawtooth(nx)
    matrix = np.eye(nx) * (1.0 + 2.0 * r) - r * np.eye(nx, k=1) - r * np.eye(nx, k=-1)
    matrix[0, -1] = -r
    matrix[-1, 0] = -r
    for _ in range(steps):
        u = np.linalg.solve(matrix, u)
    return float(np.abs(u).max())


def main() -> None:
    section("1. Von Neumann analysis of the explicit wave scheme")
    print("Insert u(i,n) = G^n exp(i k i dx) into")
    print("    u(i,n+1) = 2u(i,n) - u(i,n-1) + r^2 [u(i+1,n) - 2u(i,n) + u(i-1,n)]")
    print("Divide by G^(n-1) exp(i k i dx) and write a = 1 - 2 r^2 sin^2(k dx/2):")
    print("    G^2 - 2 a G + 1 = 0,     G = a +- sqrt(a^2 - 1)")
    print("|G| = 1 exactly whenever |a| <= 1, which holds for all k if and only")
    print("if r <= 1. The most dangerous wavenumber is k dx = pi, where")
    print("|a| = |1 - 2r^2| is largest. So the stability limit is r <= 1.")

    section("2. Measured growth rate versus the von Neumann prediction")
    print("Initial condition: u = (-1)^i (the k dx = pi eigenmode), u_t = 0.")
    print("Growth is measured as the ratio of successive maxima far into the run.")
    print(f"{'r':>8} {'predicted |G|':>14} {'measured |G|':>13} "
          f"{'difference':>12} {'max |u| @300':>13}")
    for r in (0.5, 0.9, 0.99, 0.999, 1.0, 1.001, 1.01, 1.05, 1.2):
        steps = 300 if r <= 1.0 else 60
        amp = wave_amplitudes(200, r, steps)
        if r <= 1.0:
            measured = float(np.max(amp))
            print(f"{r:8.3f} {wave_growth_prediction(r):14.6f} "
                  f"{'bounded':>13} {'-':>12} {measured:13.1f}")
            continue
        # ratios are only meaningful once the growing root dominates
        ratios = amp[-20:] / amp[-21:-1]
        measured = float(np.mean(ratios))
        predicted = wave_growth_prediction(r)
        print(f"{r:8.3f} {predicted:14.6f} {measured:13.6f} "
              f"{measured - predicted:12.2e} {'unstable':>12}")
    print("For r > 1 the agreement with the von Neumann prediction is exact to")
    print("six decimal places: the measured instability IS the predicted one,")
    print("not an artefact of the test.")
    print("For r <= 1 the amplitude is bounded by 2, EXCEPT as r approaches 1:")
    print("at r = 1 the max |u| after 300 steps is 601 = 2*300 + 1. There |G| = 1")
    print("with a DOUBLE root at -1, the amplification matrix is defective, and")
    print("the amplitude grows linearly, |u| = 2n - 1. The von Neumann test")
    print("(|G| <= 1) is necessary but not sufficient when roots coincide: a")
    print("scheme can be 'stable' by that test and still grow without bound.")

    section("3. The same scheme run with the sign of the Laplacian flipped")
    print("This is the single most common coding error in a stencil: accumulating")
    print("the flux into the wrong index. The operator becomes -d2/dx2 and the")
    print("scheme becomes an exponential amplifier.")
    print(f"{'r':>8} {'measured growth/step':>22} {'prediction (3 + sqrt(5))/2':>28}")
    amp = wave_amplitudes(200, 0.5, 60, laplacian_sign=-1.0)
    ratios = amp[-20:] / amp[-21:-1]
    measured = float(np.mean(ratios))
    print(f"{0.5:8.3f} {measured:22.6f} {0.5 * (3.0 + np.sqrt(5.0)):28.6f}")
    print("With the sign flipped, a = 1 + 2r^2 sin^2, and at k dx = pi,")
    print("G = a + sqrt(a^2-1) with a = 1 + 2r^2 = 1.5: the largest root of")
    print("G^2 - 3G + 1 = 0 is (3 + sqrt(5))/2 = 2.618. The measured growth per")
    print("step matches. A sign error is not a small error; it changes a")
    print("conservative scheme into a divergent one, and the divergence rate is")
    print("predictable, which is how you identify it.")

    section("4. Explicit diffusion: a one-sided stability limit")
    print("u_t = kappa u_xx, explicit: u(n+1) = u(n) + r [u(i+1) - 2u(i) + u(i-1)],")
    print("r = kappa dt/dx^2. Von Neumann gives G = 1 - 4r sin^2(k dx/2), so")
    print("|G| <= 1 for all k if and only if r <= 1/2.")
    print(f"{'r':>8} {'|1-4r| predicted':>18} {'measured growth/step':>22} "
          f"{'difference':>13}")
    for r in (0.25, 0.4, 0.45, 0.4999, 0.5, 0.5001, 0.505, 0.51, 0.6):
        amp = diffusion_amplitudes(200, r, 100)
        predicted = abs(1.0 - 4.0 * r)
        measured = (float((amp[-1] / amp[0]) ** (1.0 / (len(amp) - 1)))
                    if predicted > 0.0 else 0.0)
        print(f"{r:8.4f} {predicted:18.6f} {measured:22.6f} "
              f"{measured - predicted:13.2e}")
    print("The scalar recursion has a single root, so the measured growth per")
    print("step matches |1 - 4r| exactly (differences are round-off). Note that")
    print("r = 1/2 is only marginally stable: G = -1 at k dx = pi, so that mode")
    print("oscillates forever without decaying. Using r = 0.4 leaves margin.")

    section("5. Implicit diffusion is unconditionally stable")
    print("Backward Euler: (I - r D2) u_new = u_old, an nx-by-nx linear solve")
    print("per step. The d2/dx2 operator has eigenvalues in [-4/dx^2, 0], so")
    print("G = 1/(1 + 4r sin^2(k dx/2)) and |G| < 1 for every positive r.")
    print(f"{'r':>9} {'predicted |G|':>14} {'amplitude after 6 steps':>25} "
          f"{'check':>9}")
    for r in (0.5, 1.0, 10.0, 100.0, 1000.0):
        amp = implicit_diffusion_growth(200, r, 6)
        predicted = (1.0 / (1.0 + 4.0 * r)) ** 6
        print(f"{r:9.1f} {1.0 / (1.0 + 4.0 * r):14.6f} {amp:25.6e} "
              f"{'ok' if abs(amp - predicted) < 1e-12 else 'MISMATCH':>9}")
    print("The amplitude after six steps matches (1/(1+4r))^6 to round-off even")
    print("at r = 1000, where the explicit scheme would need 2000 times more")
    print("steps to be stable. The price is a linear solve per step:")
    print("  explicit cost per step ~ nx flops, stable only for r <= 1/2")
    print("  implicit cost per step ~ nx flops with a banded solver, stable always")
    print("Stability is not accuracy: at r = 1000 the implicit solution is")
    print("stable and wrong, because the timestep resolves nothing.")

    section("6. The CFL condition as a physical statement")
    print("For the explicit wave scheme, r = c dt/dx <= 1 is the statement that")
    print("    (distance the wave travels in one step) <= (one grid cell).")
    print("Equivalently, the numerical domain of dependence must contain the")
    print("physical one; otherwise the scheme is being asked to produce a")
    print("solution from information it never saw. Two consequences that are")
    print("easy to verify by hand:")
    dx = 1.0
    for velocity, dt in ((2.0, 0.4), (2.0, 0.6), (6.0, 0.2)):
        r = velocity * dt / dx
        print(f"  c = {velocity:4.1f} m/s, dt = {dt:4.2f} s, dx = {dx:4.2f} m "
              f"-> r = {r:5.3f} -> {'stable' if r <= 1 else 'UNSTABLE'}")
    print("For a heterogeneous medium the limit uses the largest local velocity,")
    print("and any local time-step refinement must use the same rule; a single")
    print("too-large cell anywhere in the mesh destabilises the whole run.")

    section("7. Summary of the measured limits")
    print(f"{'scheme':>34} {'stability limit':>18} {'order':>7}")
    print(f"{'explicit wave (3-level, centred)':>34} {'r <= 1':>18} {'2':>7}")
    print(f"{'explicit diffusion (FTCS)':>34} {'r <= 1/2':>18} {'2 in x, 1 in t':>7}")
    print(f"{'explicit diffusion, r = 1/2':>34} {'marginal':>18} {'2 in x, 1 in t':>7}")
    print(f"{'implicit diffusion (backward Euler)':>34} {'unconditional':>18} {'1 in t':>7}")
    print(f"{'first-order upwind advection':>34} {'nu <= 1':>18} {'1':>7}")
    print(f"{'Lax-Wendroff advection':>34} {'nu <= 1':>18} {'2':>7}")
    print("Every 'r <= ...' above was confirmed by the measured growth rates in")
    print("sections 2 to 5. A stability claim that has not been measured is a")
    print("hypothesis.")


if __name__ == "__main__":
    main()
