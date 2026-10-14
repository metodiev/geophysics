"""Designing reusable model code: grids, operators, boundaries, models.

The lesson's claim is that four small interfaces -- Grid, Operator, Boundary,
Model -- carry almost every finite-difference code. This file builds them,
then uses them to demonstrate three things you cannot demonstrate with a
single-script solver:

  1. that an operator can be verified against a known analytic derivative;
  2. that the same sign error in a stencil changes a stable scheme into a
     divergent one, and that a one-line test catches it;
  3. that a boundary condition is an object with its own measurable property
     (here, the reflection coefficient of a first-order absorbing condition).

Run:
    .venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/modular_design_demo.py
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# The four interfaces
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Grid:
    """A uniform 1-D grid. Owns the mesh, not the physics."""

    nx: int
    dx: float

    def __post_init__(self) -> None:
        if self.nx < 4:
            raise ValueError(f"nx must be at least 4, got {self.nx}")
        if not self.dx > 0.0:
            raise ValueError(f"dx must be positive, got {self.dx}")

    @property
    def x(self) -> np.ndarray:
        return np.arange(self.nx) * self.dx

    @property
    def length(self) -> float:
        return self.nx * self.dx

    def wavenumber(self, modes: int) -> float:
        return 2.0 * np.pi * modes / self.length


class Operator:
    """A spatial discretisation. Must expose apply() and order()."""

    name = "operator"

    def apply(self, u: np.ndarray, dx: float) -> np.ndarray:  # pragma: no cover
        raise NotImplementedError

    def order(self) -> int:                                    # pragma: no cover
        raise NotImplementedError

    @staticmethod
    def analytic(k: float, x: np.ndarray, order_of_derivative: int) -> np.ndarray:
        """The exact (d/dx)^n sin(kx), for the verification test."""
        if order_of_derivative == 1:
            return k * np.cos(k * x)
        return -k ** 2 * np.sin(k * x)


class SecondDerivative(Operator):
    """Centred (1, -2, 1) / dx^2, second order."""

    name = "centred d2/dx2"

    def apply(self, u: np.ndarray, dx: float) -> np.ndarray:
        return (np.roll(u, 1) + np.roll(u, -1) - 2.0 * u) / dx ** 2

    def order(self) -> int:
        return 2


class SecondDerivativeFourthOrder(Operator):
    """(-1, 16, -30, 16, -1) / (12 dx^2), fourth order."""

    name = "five-point d2/dx2"

    def apply(self, u: np.ndarray, dx: float) -> np.ndarray:
        return (-np.roll(u, 2) + 16.0 * np.roll(u, 1) - 30.0 * u
                + 16.0 * np.roll(u, -1) - np.roll(u, -2)) / (12.0 * dx ** 2)

    def order(self) -> int:
        return 4


class FirstDerivative(Operator):
    """Centred (1, 0, -1) / (2 dx), second order."""

    name = "centred d/dx"

    def apply(self, u: np.ndarray, dx: float) -> np.ndarray:
        return (np.roll(u, -1) - np.roll(u, 1)) / (2.0 * dx)

    def order(self) -> int:
        return 2


class FirstDerivativeForward(Operator):
    """One-sided (1, -1) / dx, first order."""

    name = "forward d/dx"

    def apply(self, u: np.ndarray, dx: float) -> np.ndarray:
        return (np.roll(u, -1) - u) / dx

    def order(self) -> int:
        return 1


class BrokenSecondDerivative(SecondDerivative):
    """The same stencil written with the flux accumulated at the wrong index.

    This is the exact mistake it is named after: `div[1:] += flux;
    div[:-1] -= flux` computes the BACKWARD difference of the flux, which
    gives minus the Laplacian. The class exists so that the test suite has
    something to fail on.
    """

    name = "centred d2/dx2 with flipped sign"

    def apply(self, u: np.ndarray, dx: float) -> np.ndarray:
        flux = u[1:] - u[:-1]
        div = np.zeros_like(u)
        div[1:] += flux
        div[:-1] -= flux
        return div / dx ** 2


class Boundary:
    """A boundary condition. Owns only its own parameters."""

    name = "boundary"

    def apply(self, u_prev: np.ndarray, u_next: np.ndarray) -> None:
        raise NotImplementedError                              # pragma: no cover


class Periodic(Boundary):
    name = "periodic"

    def apply(self, u_prev: np.ndarray, u_next: np.ndarray) -> None:
        return None                     # np.roll already wraps


class Rigid(Boundary):
    """u = 0 at both ends: a total reflection with a polarity reversal."""

    name = "rigid (Dirichlet)"

    def apply(self, u_prev: np.ndarray, u_next: np.ndarray) -> None:
        del u_prev
        u_next[0] = 0.0
        u_next[-1] = 0.0


class ShiftOutgoing(Boundary):
    """The naive one-way condition u(0,n+1) = u(1,n): transparent only at
    Courant number 1, and strongly reflecting below it."""

    name = "naive one-way shift"

    def apply(self, u_prev: np.ndarray, u_next: np.ndarray) -> None:
        u_next[0] = u_prev[1]
        u_next[-1] = u_prev[-2]


class AbsorbingFirstOrder(Boundary):
    """Reynolds' first-order one-way condition, valid for normal incidence.

        u(0,n+1)     = u(1,n)     + b [u(1,n+1)     - u(0,n)]
        u(N-1,n+1)   = u(N-2,n)   + b [u(N-2,n+1)   - u(N-1,n)]
    with b = (nu - 1)/(nu + 1) and nu = c dt/dx the Courant number.
    """

    name = "first-order absorbing (Reynolds)"

    def __init__(self, courant: float = 0.5) -> None:
        self.courant = courant

    def set_courant(self, courant: float) -> None:
        """The condition depends on c dt/dx, which the interior scheme owns."""
        self.courant = courant

    @property
    def b(self) -> float:
        return (self.courant - 1.0) / (self.courant + 1.0)

    def apply(self, u_prev: np.ndarray, u_next: np.ndarray) -> None:
        b = self.b
        u_next[0] = u_prev[1] + b * (u_next[1] - u_prev[0])
        u_next[-1] = u_prev[-2] + b * (u_next[-2] - u_prev[-1])


# --------------------------------------------------------------------------
# A model that composes them
# --------------------------------------------------------------------------

class WaveModel1D:
    """u_tt = c^2 u_xx with a local wave speed array and a boundary object."""

    def __init__(self, grid: Grid, velocity_left: float, velocity_right: float,
                 interface_index: int | None = None,
                 boundary: Boundary | None = None,
                 operator: Operator | None = None,
                 courant: float = 0.5) -> None:
        self.grid = grid
        self.velocity = np.full(grid.nx, velocity_left)
        if interface_index is not None:
            self.velocity[interface_index:] = velocity_right
        self.boundary = boundary if boundary is not None else Periodic()
        self.operator = operator if operator is not None else SecondDerivative()
        self.courant = courant
        self.dt = self.courant * grid.dx / self.velocity.max()
        if isinstance(self.boundary, AbsorbingFirstOrder):
            self.boundary.set_courant(self.courant)

    def step(self, u_prev: np.ndarray, u_cur: np.ndarray) -> np.ndarray:
        u_next = (2.0 * u_cur - u_prev
                  + self.dt ** 2 * self.velocity ** 2
                  * self.operator.apply(u_cur, self.grid.dx))
        self.boundary.apply(u_cur, u_next)
        return u_next

    def run(self, u0: np.ndarray, steps: int, source_index: int = 0,
            source: np.ndarray | None = None) -> np.ndarray:
        u_prev = u0.copy()
        u_cur = u0 + 0.5 * self.dt ** 2 * self.velocity ** 2 * self.operator.apply(
            u0, self.grid.dx)
        history = np.zeros((steps, self.grid.nx))
        for step_index in range(steps):
            u_next = (2.0 * u_cur - u_prev
                      + self.dt ** 2 * self.velocity ** 2
                      * self.operator.apply(u_cur, self.grid.dx))
            if source is not None:
                u_next[source_index] += self.dt ** 2 * source[step_index]
            self.boundary.apply(u_cur, u_next)
            u_prev, u_cur = u_cur, u_next
            history[step_index] = u_cur
        return history


# --------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------

def probe_trace(treatment: str, courant: float, nx: int = 2000,
                steps: int = 1200) -> tuple[float, float]:
    """One interior scheme, one boundary treatment, one measurement.

    The treatments are the same three implemented as Boundary objects
    above; they are written out here because the reflection coefficient is
    a property of the ARITHMETIC, and writing it out removes every doubt
    about which object received which parameter.
    """
    dx, velocity = 1.0, 1.0
    dt = courant * dx / velocity
    coefficient = (velocity * dt / dx) ** 2
    b = (courant - 1.0) / (courant + 1.0)
    times = np.arange(steps) * dt
    centre = 1.0 / 0.02
    wavelet = (1.0 - 2.0 * (np.pi * 0.02 * (times - centre)) ** 2) * np.exp(
        -((np.pi * 0.02 * (times - centre)) ** 2))
    u_prev = np.zeros(nx)
    u_cur = np.zeros(nx)
    trace = np.zeros(steps)
    for step_index in range(steps):
        u_next = 2.0 * u_cur - u_prev + coefficient * (
            np.roll(u_cur, 1) + np.roll(u_cur, -1) - 2.0 * u_cur)
        u_next[200] += dt ** 2 * wavelet[step_index]
        if treatment == "rigid":
            u_next[0] = 0.0
            u_next[-1] = 0.0
        elif treatment == "shift":
            u_next[0] = u_cur[1]
            u_next[-1] = u_cur[-2]
        elif treatment == "reynolds":
            # u_cur is the level n, u_next is level n+1: the one-way condition
            # needs those two, NOT u_prev.
            u_next[0] = u_cur[1] + b * (u_next[1] - u_cur[0])
            u_next[-1] = u_cur[-2] + b * (u_next[-2] - u_cur[-1])
        else:                                               # pragma: no cover
            raise ValueError(treatment)
        u_prev, u_cur = u_cur, u_next
        trace[step_index] = u_cur[240]
    outgoing = float(np.abs(trace[int(60 / dt):int(140 / dt)]).max())
    returning = float(np.abs(trace[int(430 / dt):int(560 / dt)]).max())
    return outgoing, returning

def measured_order(operator: Operator, derivative: int, modes: int = 3,
                   refinements: int = 6) -> tuple[list[float], list[float]]:
    """Refine nx and measure the order from the error against the analytic result."""
    errors = []
    for nx in (128 * 2 ** k for k in range(refinements)):
        grid = Grid(nx=nx, dx=1.0 / nx)
        k = grid.wavenumber(modes)
        u = np.sin(k * grid.x)
        analytic = operator.analytic(k, grid.x, derivative)
        numeric = operator.apply(u, grid.dx)
        errors.append(float(np.sqrt(np.mean((numeric - analytic) ** 2))))
    orders = [float(np.log2(errors[i] / errors[i + 1]))
              for i in range(len(errors) - 1)]
    return errors, orders


def main() -> None:
    section("1. Operators are testable objects: measure their order")
    print("Continuous reference: d2/dx2 sin(kx) = -k^2 sin(kx),")
    print("d/dx sin(kx) = k cos(kx). Periodic grid, 3 wavelengths, nx doubled.")
    for operator, derivative in ((SecondDerivative(), 2),
                                 (SecondDerivativeFourthOrder(), 2),
                                 (FirstDerivative(), 1),
                                 (FirstDerivativeForward(), 1)):
        errors, orders = measured_order(operator, derivative)
        tail = ", ".join(f"{o:.4f}" for o in orders[-3:])
        print(f"  {operator.name:>24} : nominal {operator.order()}, "
              f"measured {tail} (last three doublings)")
        print(f"  {'':>24}   errors: " +
              ", ".join(f"{e:.3e}" for e in errors[:4]))
    print("The centred second derivative holds order 2.0000 over the whole range.")
    print("The five-point second derivative holds 4.00 until nx = 2048 and then")
    print("collapses: at that point the truncation error has fallen to the level")
    print("of round-off amplified by the dx^-2 scaling of the stencil, roughly")
    print("eps/dx^2 = 2.2e-16 * 4.2e6 = 9e-10. The measured error stops falling")
    print("there. Refining an operator past its round-off floor measures nothing.")
    print("The one-sided difference reaches order 1 and the centred first")
    print("derivative order 2, both with the correct analytic reference -- which")
    print("is the point: an operator test must know WHICH derivative it is")
    print("testing. Comparing a d/dx stencil against -k^2 sin(kx) reports order")
    print("zero and looks like a broken operator instead of a broken test.")

    section("2. The same class with one index swapped")
    good = SecondDerivative()
    broken = BrokenSecondDerivative()
    grid = Grid(nx=200, dx=1.0 / 200)
    k = grid.wavenumber(3)
    u = np.sin(k * grid.x)
    print(f"{'operator':>34} {'error vs analytic':>18}")
    for operator in (good, broken):
        numeric = operator.apply(u, grid.dx)
        analytic = -k ** 2 * np.sin(k * grid.x)
        print(f"{operator.name:>34} "
              f"{np.sqrt(np.mean((numeric - analytic) ** 2)):18.6e}")
    print("The broken operator is not slightly wrong, it is the negative of the")
    print("right answer, and its error is 100% of the signal. In a time-stepping")
    print("code this produces the exponential divergence measured in lesson 02;")
    print("here it fails a unit test in three lines.")

    section("3. Boundaries are objects with measurable properties")
    print("A wave is launched at cell 200 of a 2000-cell domain and recorded at")
    print("cell 240, so the LEFT boundary (200 cells away) sends its reflection")
    print("back at about t = 50 + 200 + 240 = 490 s. The right boundary is 1800")
    print("cells away and cannot return inside the 600 s run.")
    print()
    print("The right boundary uses the same treatment as the left, so what is")
    print("measured is the reflection of the boundary treatment itself.")
    print(f"{'boundary':>28} {'courant':>8} {'outgoing':>10} "
          f"{'returning':>11} {'reflection':>11}")

    for treatment, label, courant in (
            ("rigid", "rigid (u = 0)", 0.5),
            ("rigid", "rigid (u = 0)", 1.0),
            ("shift", "naive shift u(0)=u(1)", 0.5),
            ("shift", "naive shift u(0)=u(1)", 1.0),
            ("reynolds", "Reynolds first order", 0.4),
            ("reynolds", "Reynolds first order", 0.5),
            ("reynolds", "Reynolds first order", 0.7),
            ("reynolds", "Reynolds first order", 0.9),
            ("reynolds", "Reynolds first order", 1.0)):
        outgoing, returning = probe_trace(treatment, courant)
        print(f"{label:>28} {courant:8.2f} {outgoing:10.4e} "
              f"{returning:11.4e} {returning / outgoing:11.6f}")

    print("The reflection coefficient is a measurable property of the boundary")
    print("arithmetic. A rigid boundary reflects everything (1.02, the excess")
    print("being a second reflection arriving inside the run). The naive")
    print("one-sided condition u(0,n+1) = u(1,n) reflects 0.34 of the amplitude")
    print("at Courant number 0.5 and becomes transparent only at nu = 1, which is")
    print("useless because nu = 1 is the 1-D stability limit. The Reynolds")
    print("condition, whose coefficient b = (nu-1)/(nu+1) is the discrete")
    print("impedance match, reflects 0.12% at nu = 0.5 and 0.04% at nu = 1.")
    print()
    print("A note on how this number was obtained, because the first version was")
    print("wrong. The three-level scheme has u_prev = u(n-1) and u_cur = u(n),")
    print("and produces u_next = u(n+1). A one-way condition relates levels n and")
    print("n+1. Passing (u_prev, u_next) instead of (u_cur, u_next) is a silent")
    print("off-by-one in time, and it changed the measured reflection of the")
    print("Reynolds condition from 0.12% to 34% -- the sign of the conclusion,")
    print("not the third digit. The bug is invisible in the code and obvious in")
    print("the measurement, which is the argument for measuring.")

    section("4. Composition: the same model with a different operator")
    print("Single mode on nx = 256 cells, one second of propagation, both")
    print("operators, two wavenumbers. The temporal error is identical for both")
    print("operators, so any difference is spatial.")
    print(f"{'points/wavelength':>18} {'operator':>24} {'RMS error':>12} "
          f"{'operator error':>15}")
    for modes in (32, 64):
        for operator in (SecondDerivative(), SecondDerivativeFourthOrder()):
            grid = Grid(nx=256, dx=1.0)
            model = WaveModel1D(grid, 1.0, 1.0, boundary=Periodic(),
                                operator=operator)
            steps = int(1.0 / model.dt)
            x = grid.x
            k = grid.wavenumber(modes)
            u0 = np.sin(k * x)
            history = model.run(u0, steps)
            analytic = np.sin(k * (x - steps * model.dt))
            error = float(np.sqrt(np.mean((history[-1] - analytic) ** 2)))
            pure = float(np.sqrt(np.mean(
                (operator.apply(u0, grid.dx) + k ** 2 * u0) ** 2)))
            print(f"{256 / modes:18.1f} {operator.name:>24} {error:12.6e} "
                  f"{pure:15.3e}")
    print("At 8 points per wavelength the two runs agree to a few per cent: the")
    print("temporal discretisation error dominates, and the operator is almost")
    print("irrelevant. At 4 points per wavelength the difference is large. The")
    print("model does not know which operator it was given -- that is the point")
    print("of the interface, and also the danger: a verification test must travel")
    print("with the operator, not with the script that happened to build it.")

    section("5. Types and invariants catch errors the tests do not")
    try:
        Grid(nx=100, dx=0.0)
        print("  dx = 0 was accepted")
    except ValueError as exc:
        print(f"  Grid(nx=100, dx=0.0) -> ValueError: {exc}")
    try:
        Grid(nx=2, dx=1.0)
        print("  nx = 2 was accepted")
    except ValueError as exc:
        print(f"  Grid(nx=2, dx=1.0)   -> ValueError: {exc}")
    print("  Without that check, dx = 0 produces inf and nan from a RuntimeWarning")
    print("  rather than an error, and the nan propagates silently for the rest of")
    print("  the run.")
    try:
        model = WaveModel1D(Grid(nx=10, dx=1.0), 1.0, 1.0)
        model.step(np.zeros(11), np.zeros(11))
        print("  a mismatched array length was accepted")
    except ValueError as exc:
        print(f"  wrong array length -> ValueError: {exc}")
    print("  Grid is frozen, so a grid cannot be mutated half way through a run.")
    print("  WaveModel1D derives dt from the maximum velocity, so the CFL")
    print(f"  condition cannot be violated by forgetting to update dt: "
          f"courant = {WaveModel1D(Grid(nx=100, dx=1.0), 1.0, 3.0).courant} "
          f"and dt = {WaveModel1D(Grid(nx=100, dx=1.0), 1.0, 3.0).dt:.6f} s")

    section("6. Cost, measured in temporary arrays rather than seconds")
    grid = Grid(nx=1_000_000, dx=1.0)
    u = np.zeros(grid.nx)
    operator = SecondDerivative()
    print(f"grid                            : {grid.nx} points")
    for label, code in (
            ("np.roll twice (two temporaries)",
             lambda: operator.apply(u, grid.dx)),
            ("np.empty + in-place slicing",
             lambda: _lap_inplace(u, grid.dx))):
        result = code()
        print(f"  {label:<32} checksum {result.sum():.1f}, "
              f"max |value| {np.abs(result).max():.1f}")
    print("Both give the same answer on a constant array, which is the trap:")
    print("a constant array cannot distinguish a correct stencil from a wrong")
    print("one. Use a sine with a known wavenumber, as in section 1.")
    print("np.roll allocates two full-length")
    print("temporaries per call, which is 16 MB per call at 1e6 float64 points.")
    print("At 10 000 steps that is 160 GB of memory traffic, and it is the")
    print("single most common reason a Python solver is 100x slower than the")
    print("same loop in Fortran. Measure it with a profiler; do not guess.")
    print("(No timings are quoted in this file: they are machine-specific.)")


def _lap_inplace(u: np.ndarray, dx: float) -> np.ndarray:
    """The same (1, -2, 1)/dx^2 stencil, written to reuse one buffer."""
    out = np.empty_like(u)
    out[1:-1] = u[2:] - 2.0 * u[1:-1] + u[:-2]
    out[0] = 0.0
    out[-1] = 0.0
    out /= dx ** 2
    return out


if __name__ == "__main__":
    main()
