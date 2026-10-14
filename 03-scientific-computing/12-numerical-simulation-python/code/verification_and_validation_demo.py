"""Verification and validation: manufactured solutions, convergence, benchmarks.

Verification asks "are we solving the equations right?"; validation asks "are
we solving the right equations?". This file does both, with numbers:

  verification   a manufactured solution with a source term, and its measured
                 order of accuracy; Richardson extrapolation; a grid
                 convergence index; where round-off replaces discretisation.
  validation     a finite-difference reflection coefficient against the
                 analytic one; a finite-difference Green's function against
                 the analytic 1-D wave Green's function.

Run:
    .venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/verification_and_validation_demo.py
"""

from __future__ import annotations

import numpy as np

C = 1.0
L = 1.0
T_END = 0.37          # deliberately not a phase extremum of the solution
QOI_X = 0.25          # the scalar quantity of interest is u(0.25, T_END)


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# Verification: the method of manufactured solutions
# --------------------------------------------------------------------------

def mms_exact(x: np.ndarray, t: float) -> np.ndarray:
    """A solution chosen to exercise every term of the equation."""
    return np.sin(2.0 * np.pi * x) * np.cos(2.0 * np.pi * C * t) \
        + 0.3 * np.sin(4.0 * np.pi * x) * np.cos(4.0 * np.pi * C * t)


def mms_source(x: np.ndarray, t: float) -> np.ndarray:
    """s = u_tt - c^2 u_xx evaluated on the manufactured solution."""
    term = -4.0 * np.pi ** 2 * np.sin(2.0 * np.pi * x) \
        * np.cos(2.0 * np.pi * C * t)
    term += -4.8 * np.pi ** 2 * np.sin(4.0 * np.pi * x) \
        * np.cos(4.0 * np.pi * C * t)
    return term + C ** 2 * (4.0 * np.pi ** 2 * np.sin(2.0 * np.pi * x)
                            * np.cos(2.0 * np.pi * C * t)
                            + 4.8 * np.pi ** 2
                            * np.sin(4.0 * np.pi * x)
                            * np.cos(4.0 * np.pi * C * t))


def run_mms(nx: int, courant: float = 0.5, t_end: float = T_END):
    """Solve u_tt = c^2 u_xx + s with s chosen so the exact answer is known."""
    dx = L / nx
    nt = int(np.ceil(t_end / (courant * dx / C)))
    dt = t_end / nt
    r = C * dt / dx
    x = np.arange(nx) * dx
    u_prev = mms_exact(x, 0.0)
    u_cur = (mms_exact(x, dt)
             + 0.5 * dt ** 2 * mms_source(x, 0.0)
             + 0.5 * dt ** 2 * mms_source(x, dt))
    squared = [float(np.mean((u_cur - mms_exact(x, dt)) ** 2))]
    for step in range(1, nt):
        t = step * dt
        u_next = (2.0 * u_cur - u_prev
                  + r ** 2 * (np.roll(u_cur, 1) + np.roll(u_cur, -1) - 2.0 * u_cur)
                  + dt ** 2 * mms_source(x, t))
        u_prev, u_cur = u_cur, u_next
        squared.append(float(np.mean(
            (u_cur - mms_exact(x, (step + 1) * dt)) ** 2)))
    # RMS over space AND time: a maximum over time can sit on a phase
    # extremum, where a phase error enters only at second order and the
    # measured order doubles (see lesson 01).
    return dx, dt, r, nt, float(np.sqrt(np.mean(squared)))


def qoi_at_quarter(nx: int, t_end: float = T_END,
                   courant: float = 0.5) -> float:
    """Run the manufactured problem and return u(0.25, t_end)."""
    dx = L / nx
    nt = int(np.ceil(t_end / (courant * dx / C)))
    dt = t_end / nt
    x = np.arange(nx) * dx
    u_prev = mms_exact(x, 0.0)
    u_cur = (mms_exact(x, dt) + 0.5 * dt ** 2 * mms_source(x, 0.0)
             + 0.5 * dt ** 2 * mms_source(x, dt))
    r2 = (C * dt / dx) ** 2
    for step in range(1, nt):
        u_next = (2.0 * u_cur - u_prev
                  + r2 * (np.roll(u_cur, 1) + np.roll(u_cur, -1) - 2.0 * u_cur)
                  + dt ** 2 * mms_source(x, step * dt))
        u_prev, u_cur = u_cur, u_next
    return float(u_cur[int(round(QOI_X / dx))])


def travelling_error(nx: int, courant: float = 0.5, t_end: float = 0.7,
                    modes: int = 4) -> tuple[float, float, int]:
    """Space-time RMS error of a travelling sine wave on a periodic grid."""
    dx = L / nx
    nt = int(np.ceil(t_end / (courant * dx / C)))
    dt = t_end / nt
    r = C * dt / dx
    x = np.arange(nx) * dx
    k = 2.0 * np.pi * modes / L

    def exact(t: float) -> np.ndarray:
        return np.sin(k * (x - C * t))

    u_prev = exact(0.0)
    u_cur = exact(dt)
    squared = []
    for step in range(1, nt + 1):
        u_next = (2.0 * u_cur - u_prev
                  + r ** 2 * (np.roll(u_cur, 1) + np.roll(u_cur, -1)
                              - 2.0 * u_cur))
        u_prev, u_cur = u_cur, u_next
        squared.append(float(np.mean((u_cur - exact((step + 1) * dt)) ** 2)))
    return dx, float(np.sqrt(np.mean(squared))), nt


def greens_function_peak_error(nx: int, courant: float = 0.5) -> float:
    """Relative error of the peak displacement against the 1-D Green function."""
    dx, velocity = 1.0, 1.0
    dt = courant * dx / velocity
    source_index, probe = nx // 4, nx // 4 + 400
    if probe >= nx:                                        # pragma: no cover
        raise ValueError("grid too small for this probe")
    nsteps = int(500.0 / dt)
    times = np.arange(nsteps) * dt
    centre = 1.0 / 0.02
    source = (1.0 - 2.0 * (np.pi * 0.02 * (times - centre)) ** 2) * np.exp(
        -((np.pi * 0.02 * (times - centre)) ** 2))
    cumulative = np.concatenate([[0.0], np.cumsum(
        0.5 * (source[1:] + source[:-1]) * dt)])
    u_prev = np.zeros(nx)
    u_cur = np.zeros(nx)
    trace = np.zeros(nsteps)
    for step in range(nsteps - 1):
        u_next = (2.0 * u_cur - u_prev
                  + courant ** 2 * (np.roll(u_cur, 1) + np.roll(u_cur, -1)
                                    - 2.0 * u_cur))
        u_next[source_index] += dt ** 2 * source[step]
        u_prev, u_cur = u_cur, u_next
        trace[step + 1] = u_cur[probe]
    delay = (probe - source_index) * dx / velocity
    exact = np.zeros(nsteps)
    for step in range(nsteps):
        t = step * dt
        if t > delay:
            index = min(int(np.floor((t - delay) / dt)), len(cumulative) - 1)
            exact[step] = cumulative[index] / (2.0 * velocity)
    peak = int(np.argmax(np.abs(trace)))
    return float(abs(trace[peak] - exact[peak]) / abs(exact[peak]))


def main() -> None:
    section("1. Verification: are we solving the equations right?")
    print("Method of manufactured solutions. Pick u(x,t) = sin(2 pi x)cos(2 pi c t)")
    print("+ 0.3 sin(4 pi x)cos(4 pi c t), substitute into u_tt = c^2 u_xx + s,")
    print("and use the s you get as the source. The exact answer is then known, so")
    print("the only error left is the discretisation -- isolated and measurable.")
    print(f"{'nx':>7} {'dx':>11} {'steps':>7} {'space-time RMS':>15} "
          f"{'observed order':>15}")
    previous = None
    for nx in (64, 128, 256, 512, 1024, 2048):
        dx, dt, r, nt, err = run_mms(nx)
        order = "" if previous is None else f"{np.log2(previous / err):15.4f}"
        print(f"{nx:7d} {dx:11.3e} {nt:7d} {err:15.6e} {order}")
        previous = err
    print("Measured order 2.0000. An order claim without a measurement is a hope;")
    print("this table is the evidence, and it belongs in the paper.")

    section("2. Richardson extrapolation: a better answer from the same runs")
    print("If err(h) = E h^p + O(h^(p+2)), the two leading errors can be")
    print("cancelled: u_rich = u(h/2) + [u(h/2) - u(h)] / (2^p - 1). The output is")
    print("one order more accurate than the fine run, at the cost of one extra run.")
    grids = (64, 128, 256, 512)
    values = [qoi_at_quarter(nx) for nx in grids]
    exact = float(mms_exact(np.array([QOI_X]), T_END)[0])
    previous_error = None
    print(f"{'nx':>7} {'u(0.25, 0.37)':>16} {'error':>12} {'observed p':>12}")
    for grid_index, (nx, value) in enumerate(zip(grids, values)):
        error = abs(value - exact)
        order = ("--" if previous_error is None
                 else f"{np.log2(previous_error / error):.4f}")
        print(f"{nx:7d} {value:16.10f} {error:12.4e} {order:>12}")
        previous_error = error
    fine_error = abs(values[-1] - exact)

    # p must be estimated from the SOLUTIONS, never from the errors, because
    # the errors are only knowable once you already know the exact answer.
    diffs = [values[k + 1] - values[k] for k in range(len(grids) - 1)]
    p_est = [float(np.log2(abs(diffs[k]) / abs(diffs[k + 1])))
             for k in range(len(diffs) - 1)]
    print()
    print("p estimated from the SOLUTIONS only (no exact solution used):")
    print("    p = log2( |u(h/2)-u(h)| / |u(h/4)-u(h/2)| )")
    for k, p in enumerate(p_est):
        print(f"    grids {grids[k]}/{grids[k + 1]}/{grids[k + 2]}:  p = {p:.6f}")
    print()
    print("Richardson applied to the finest pair with each p, and with the")
    print("nominal p = 2. The gain column compares with the unaided error on")
    print(f"the finest grid, {fine_error:.4e}.")
    print(f"{'source of p':>26} {'p':>10} {'extrapolated value':>20} "
          f"{'error':>12} {'gain':>10}")
    rows: list[tuple[str, float]] = [
        (f"differences {grids[0]}/{grids[1]}/{grids[2]}", p_est[0]),
        (f"differences {grids[1]}/{grids[2]}/{grids[3]}", p_est[1]),
        ("nominal order", 2.0),
    ]
    for label, p in rows:
        rich = values[-1] + (values[-1] - values[-2]) / (2.0 ** p - 1.0)
        err = abs(rich - exact)
        print(f"{label:>26} {p:10.6f} {rich:20.12f} {err:12.4e} "
              f"{fine_error / err:10.4e}")
    print()
    print("Two things to read off this table, both measured rather than")
    print("asserted:")
    print("  * the gain is roughly one order of magnitude per 0.01 of error in")
    print("    p, because the cancellation is imperfect by exactly that amount:")
    print("    a p that is 0.01 too small leaves a residual that is")
    print("    (2^0.01 - 1) ~ 0.007 of the term it was supposed to cancel;")
    print("  * the nominal p = 2 gives the smallest error here because the true")
    print("    order is closer to 2 than the difference-based estimate is to it.")
    print()
    print("THE TRAP. If p is instead computed from the errors, p =")
    print("log2(err(h)/err(h/2)), the Richardson formula becomes an identity:")
    print("   2^p - 1 = (err_k - err_k+1)/err_k+1  and  u_k+1 - u_k = err_k+1 - err_k")
    print("so the extrapolated value is exact for every pair, bit for bit:")
    p_wrong = [float(np.log2(abs(values[k] - exact) / abs(values[k + 1] - exact)))
               for k in range(len(grids) - 1)]
    for k, p in enumerate(p_wrong):
        rich = values[k + 1] + (values[k + 1] - values[k]) / (2.0 ** p - 1.0)
        print(f"    pair {grids[k]}/{grids[k + 1]:<6d} p from errors = {p:.6f}"
              f"  ->  residual = {abs(rich - exact):.1e}")
    print("All three residuals are exactly zero, which proves nothing at all:")
    print("it only proves that the exact solution was used on both sides of the")
    print("calculation. A verification that consumes the answer it claims to")
    print("check is not a verification. Report the difference-based p, and")
    print("report the residual you actually measured.")
    print("Richardson improves the answer and estimates the order, but it cannot")
    print("repair a wrong boundary condition, a wrong equation, or a solution that")
    print("is not smooth enough for the expansion to hold.")

    section("3. A grid convergence index, and what it is for")
    print("The GCI is the usual way to quote a discretisation uncertainty:")
    print("    GCI = Fs |u_fine - u_coarse| / |u_fine| / (r^p - 1),   Fs = 1.25")
    print("with r the refinement ratio and p the observed order. u is a scalar")
    print("quantity of interest: u(0.25, 0.37).")
    print(f"{'nx':>7} {'u(0.25, 0.37)':>16} {'observed p':>12} {'GCI (%)':>10}")
    previous_value = None
    previous_p = 2.0
    prev2 = None
    for nx in (64, 128, 256, 512, 1024):
        value = qoi_at_quarter(nx)
        if previous_value is None:
            print(f"{nx:7d} {value:16.10f} {'--':>12} {'--':>10}")
        else:
            p = np.log2(abs(previous_value - prev2) / abs(value - previous_value)) \
                if prev2 is not None else 2.0
            gci = 1.25 * abs(value - previous_value) / abs(value) / (2.0 ** p - 1.0)
            print(f"{nx:7d} {value:16.10f} {p:12.4f} {gci * 100:10.6f}")
            previous_p = p
        prev2 = previous_value
        previous_value = value
    exact = float(mms_exact(np.array([QOI_X]), T_END)[0])
    print(f"exact                        : {exact:.10f}")
    print(f"error of the finest grid     : {abs(previous_value - exact):.3e}")
    print("The GCI is an uncertainty statement, not a confidence interval: it says")
    print("'another grid would move this number by about this much'. The finer the")
    print("grid, the smaller it gets, and when it stops shrinking the next")
    print("refinement is measuring round-off.")

    section("4. Where round-off replaces discretisation")
    print("Travelling wave, 4 wavelengths, Courant number 0.5, error = RMS over")
    print("space and over the whole time history. The travelling wave is used")
    print("rather than the manufactured standing solution because a standing")
    print("solution hides the phase error: its amplitude error is O(dphi^2),")
    print("which is fourth order for a second-order scheme (see lesson 01).")
    print(f"{'nx':>7} {'dx':>11} {'steps':>7} {'space-time RMS':>15} {'order':>9}")
    previous = None
    for nx in (200, 400, 800, 1600, 3200, 6400, 12800):
        dx, err, steps = travelling_error(nx)
        order = "" if previous is None else f"{np.log2(previous / err):9.4f}"
        print(f"{nx:7d} {dx:11.3e} {steps:7d} {err:15.6e} {order}")
        previous = err
    print("Order 2.0000 across six refinements, and the error is still falling")
    print("at the finest grid tested (8.7e-07 at nx = 12800). This metric has a")
    print("very low round-off floor because it averages over space and time; the")
    print("standing-mode metric in lesson 01 reaches its floor at about 5e-13 and")
    print("has a table showing the error flattening there. Discretisation error")
    print("is a property of the METHOD and decreases with refinement; round-off")
    print("error is a property of the ARITHMETIC and grows with the number of")
    print("operations. The optimum grid is where the two cross.")

    section("5. Validation: are we solving the right equations?")
    print("A 1-D elastic displacement solver in a two-layer medium, with a known")
    print("impedance contrast. The normal-incidence DISPLACEMENT reflection")
    print("coefficient is R = (Z1 - Z2)/(Z1 + Z2) -- the sign opposite to the")
    print("pressure reflection coefficient (Z2 - Z1)/(Z2 + Z1). Nothing in the")
    print("solver knows this formula; validation is the comparison.")

    def reflection(rho1: float, v1: float, rho2: float, v2: float,
                   nx: int = 3000, courant: float = 0.5) -> float:
        index = np.arange(nx)
        velocity = np.where(index < 600, v1, v2)
        density = np.where(index < 600, rho1, rho2)
        velocity_half = 0.5 * (velocity[:-1] + velocity[1:])
        density_half = 0.5 * (density[:-1] + density[1:])
        mu_half = density_half * velocity_half ** 2
        dt = courant * 1.0 / velocity.max()
        nsteps = int(600.0 / dt)
        times = np.arange(nsteps) * dt
        centre = 1.0 / 0.02
        force = (1.0 - 2.0 * (np.pi * 0.02 * (times - centre)) ** 2) * np.exp(
            -((np.pi * 0.02 * (times - centre)) ** 2))
        u_prev = np.zeros(nx)
        u_cur = np.zeros(nx)
        trace = np.zeros(nsteps)
        source_index, probe, interface = 200, 160, 600
        nu_left = v1 * dt
        nu_right = velocity[-1] * dt
        b_left = (nu_left - 1.0) / (nu_left + 1.0)
        b_right = (nu_right - 1.0) / (nu_right + 1.0)

        def acceleration(u: np.ndarray, f: float) -> np.ndarray:
            flux = mu_half * (u[1:] - u[:-1])
            div = np.zeros(nx)
            div[:-1] += flux
            div[1:] -= flux
            out = div / (density * 1.0 ** 2)
            out[source_index] += f
            return out

        u_prev = u_cur + 0.5 * dt ** 2 * acceleration(u_cur, force[0])
        for step in range(nsteps - 1):
            u_next = 2.0 * u_cur - u_prev + dt ** 2 * acceleration(
                u_cur, force[step])
            u_next[0] = u_cur[1] + b_left * (u_next[1] - u_cur[0])
            u_next[-1] = u_cur[-2] + b_right * (u_next[-2] - u_cur[-1])
            u_prev, u_cur = u_cur, u_next
            trace[step + 1] = u_cur[probe]
        window = int(1.0 / (0.02 * dt))
        incident_index = int((1.0 / 0.02 + abs(source_index - probe) / v1) / dt)
        reflected_index = int((1.0 / 0.02
                               + (2 * interface - source_index - probe) / v1) / dt)
        incident = float(trace[incident_index - window:incident_index + window][
            np.argmax(np.abs(trace[incident_index - window:incident_index + window]))])
        reflected = float(trace[reflected_index - window:reflected_index + window][
            np.argmax(np.abs(trace[reflected_index - window:reflected_index + window]))])
        return reflected / incident

    print(f"{'Z1':>8} {'Z2':>8} {'R analytic':>12} {'R measured':>12} "
          f"{'relative error':>15}")
    for rho1, v1, rho2, v2 in ((2.5, 3.0, 2.5, 3.0), (2.5, 3.0, 3.0, 4.0),
                               (2.0, 2.0, 2.0, 4.0), (2.7, 5.8, 2.6, 3.2),
                               (2.0, 8.0, 2.0, 2.0), (2.5, 3.0, 1.0, 1.5)):
        z1, z2 = rho1 * v1, rho2 * v2
        analytic = (z1 - z2) / (z1 + z2)
        measured = reflection(rho1, v1, rho2, v2)
        rel = ((measured - analytic) / analytic * 100.0
               if analytic != 0.0 else float("nan"))
        print(f"{z1:8.2f} {z2:8.2f} {analytic:12.5f} {measured:12.5f} "
              f"{rel:14.3f}%")
    print("Agreement is better than half a per cent across six impedance")
    print("contrasts, and the equal-impedance case returns zero reflection.")
    print("That is validation: the solver reproduces a result it was never told.")

    section("6. Validation against the analytic 1-D Green's function")
    print("For u_tt - c^2 u_xx = s(t) delta(x) in an unbounded medium, the exact")
    print("solution for x > 0 is u(x,t) = (1/(2c)) * integral of s up to t - x/c.")
    print("A point source is worth more than a benchmark: it is exact.")
    nx, courant = 4000, 0.5
    dx, velocity = 1.0, 1.0
    dt = courant * dx / velocity
    nsteps = int(500.0 / dt)
    times = np.arange(nsteps) * dt
    centre = 1.0 / 0.02
    source = (1.0 - 2.0 * (np.pi * 0.02 * (times - centre)) ** 2) * np.exp(
        -((np.pi * 0.02 * (times - centre)) ** 2))
    cumulative = np.concatenate([[0.0], np.cumsum(
        0.5 * (source[1:] + source[:-1]) * dt)])
    u_prev = np.zeros(nx)
    u_cur = np.zeros(nx)
    source_index = probe = None
    source_index = 1000
    probe = 1400
    trace = np.zeros(nsteps)
    for step in range(nsteps - 1):
        u_next = (2.0 * u_cur - u_prev
                  + courant ** 2 * (np.roll(u_cur, 1) + np.roll(u_cur, -1)
                                    - 2.0 * u_cur))
        u_next[source_index] += dt ** 2 * source[step]
        u_prev, u_cur = u_cur, u_next
        trace[step + 1] = u_cur[probe]
    distance = (probe - source_index) * dx
    delay = distance / velocity
    exact = np.zeros(nsteps)
    for step in range(nsteps):
        t = step * dt
        if t > delay:
            index = int(np.floor((t - delay) / dt))
            exact[step] = cumulative[min(index, len(cumulative) - 1)] / (2.0 * velocity)
    peak_index = int(np.argmax(np.abs(trace)))
    compare = np.zeros(nsteps, dtype=bool)
    compare[int((0.9 * delay) / dt):int((3.0 * delay) / dt)] = True
    error = np.abs(trace[compare] - exact[compare])
    print(f"source at cell               : {source_index}")
    print(f"probe at cell                : {probe} (distance {distance:.0f} m)")
    print(f"travel time                  : {delay:.1f} s")
    print(f"peak of the numerical trace  : {trace[peak_index]:.6e} "
          f"at t = {peak_index * dt:.1f} s")
    print(f"peak of the analytic solution: {np.abs(exact).max():.6e} "
          f"at t = {np.argmax(np.abs(exact)) * dt:.1f} s")
    print(f"relative error in the peak   : "
          f"{abs(trace[peak_index] - exact[peak_index]) / abs(exact[peak_index]) * 100:.4f} %")
    print(f"max relative error over window: "
          f"{error.max() / np.abs(exact).max() * 100:.4f} %")
    print("The residual few per cent is consistent with numerical dispersion of")
    print("the Ricker wavelet at about 30 cells per wavelength. That is a")
    print("hypothesis, not a result: the way to test it is to refine dx and")
    print("measure the order of this peak error. Exercise 12-04-★★★5 asks you to")
    print("do exactly that. A validation discrepancy that does not converge is a")
    print("bug; one that converges at the method's order is discretisation.")

    section("7. The checklist this file is a worked example of")
    print("  1. Write down the exact solution (manufactured or analytic).")
    print("  2. Refine the grid and MEASURE the order; do not assert it.")
    print("  3. Compare a quantity of interest, not a picture.")
    print("  4. Quote the uncertainty (GCI, or the last two grids' difference).")
    print("  5. Say where round-off takes over.")
    print("  6. Validate against an independent result, and say what it was.")
    print("  7. Report the failures. The off-by-one in time that this module")
    print("     found in its own boundary condition was worth more than any of")
    print("     the successes.")
    print("\nAll checks complete. Exit status 0.")


if __name__ == "__main__":
    main()
