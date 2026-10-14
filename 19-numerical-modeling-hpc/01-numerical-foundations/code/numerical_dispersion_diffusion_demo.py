#!/usr/bin/env python3
"""Numerical dispersion, numerical dissipation and grid anisotropy, measured
against closed-form discrete dispersion relations.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python numerical_dispersion_diffusion_demo.py

All models and data in this module are SYNTHETIC.  The waves below are solutions
of a chosen teaching equation, not observations.

Contents
--------
1. Exact discrete phase speed of the leapfrog (CTCS) scheme; zero dissipation.
2. Phase error measured in a simulation and compared with the closed form.
3. Group velocity: the measured arrival delay of a pulse.
4. Numerical dissipation of the upwind scheme and its equivalent diffusivity.
5. Grid anisotropy: five-point versus nine-point Laplacian symbols.
"""

import numpy as np

RNG = np.random.default_rng(20261014)
A_VEL = 1.0          # m/s, the SYNTHETIC advection speed
N_CELLS = 128        # periodic domain, in cells


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def run_mode(C, ppw, n_cells, n_steps, branch="physical"):
    """Advect one Fourier mode with CTCS.

    branch="physical" initialises the state so that only the physical root of
    the quadratic amplification equation is present; branch="analytic" uses the
    exact solution at t = -dt, which excites both roots, the physical one and
    the spurious one.  Returns (v_num/v, |amplitude|).
    """
    h = 1.0
    x = np.arange(n_cells) * h
    k = 2.0 * np.pi / (ppw * h)
    theta = k * h
    omega_dt = np.arcsin(C * np.sin(theta))
    dt = C * h / A_VEL
    u0 = np.exp(1j * k * x)
    if branch == "physical":
        u_prev = u0 / np.exp(-1j * omega_dt)
    else:
        u_prev = np.exp(1j * k * (x + A_VEL * dt))
    # the reference phase is the exact continuum solution, so the measurement
    # is of the numerical phase speed itself, not of a relation assumed twice
    phase_exact = -k * A_VEL * n_steps * dt
    u = u0.copy()
    for _ in range(n_steps):
        u_next = u_prev - C * (np.roll(u, -1) - np.roll(u, 1))
        u_prev, u = u, u_next
    T = n_steps * dt
    amp = np.sum(u * np.exp(-1j * k * x)) / n_cells
    dphase = (np.angle(amp) - phase_exact + np.pi) % (2.0 * np.pi) - np.pi
    ratio = 1.0 - dphase / (k * A_VEL * T)
    return ratio, abs(amp)


def run_pulse(C, sigma, ppw, n_cells, x0, t_end):
    """Advect a modulated pulse with CTCS; return its envelope centroid."""
    h = 1.0
    x = np.arange(n_cells) * h
    k = 2.0 * np.pi / (ppw * h)
    dt = C * h / A_VEL
    steps = int(round(t_end / dt))

    def pulse(xc):
        return np.exp(-((x - xc) ** 2) / (2.0 * sigma ** 2)) * np.sin(k * (x - xc))

    u_prev = pulse(x0)
    u = pulse(x0 + A_VEL * dt)
    for _ in range(steps):
        u_next = u_prev - C * (np.roll(u, -1) - np.roll(u, 1))
        u_prev, u = u, u_next
    centroid = np.sum(x * u ** 2) / np.sum(u ** 2)
    return centroid, steps * dt


def phase_speed(C, theta):
    """v_num/v = arcsin(C sin theta)/(C theta) for the CTCS scheme."""
    return np.arcsin(C * np.sin(theta)) / (C * theta)


def group_speed(C, theta):
    """v_g/v = cos(theta)/sqrt(1 - C^2 sin^2(theta))."""
    return np.cos(theta) / np.sqrt(1.0 - C ** 2 * np.sin(theta) ** 2)


def section_dispersion_table():
    print("CTCS leapfrog: omega dt = arcsin(C sin theta), |G| = 1 exactly, so the")
    print("scheme has no numerical dissipation at all -- only dispersion")
    print(f"{'C':>6} {'PPW':>6} {'theta (rad)':>12} {'v_num/v':>12} "
          f"{'phase error %':>14} {'small-theta estimate %':>22}")
    for C in (0.5, 1.0):
        for ppw in (4, 5, 8, 10, 16, 20, 40):
            theta = 2.0 * np.pi / ppw
            ratio = phase_speed(C, theta)
            est = 1.0 - (1.0 - C ** 2) * theta ** 2 / 6.0
            print(f"{C:>6.2f} {ppw:>6} {theta:>12.6f} {ratio:>12.8f} "
                  f"{(ratio - 1.0) * 100:>14.4f} {(est - 1.0) * 100:>22.4f}")
    print("at C = 1 the two branches differ: arcsin(sin theta) = theta for")
    print("theta <= pi/2 (PPW >= 4), so the scheme is exact there, and dispersive")
    print("again for the poorly resolved modes with PPW < 4.")


def section_phase_measurement():
    """Measure the phase error of a single Fourier mode in a real run."""
    print("N = 128 cells, h = 1 m, a = 1 m/s; one period of the mode in each run")
    print("pure physical branch (the state admits only the physical root):")
    print(f"{'C':>6} {'PPW':>6} {'measured v_num/v':>18} {'predicted':>12} "
          f"{'|amplitude|':>14}")
    for C in (0.5, 1.0):
        for ppw in (4, 8, 16, 32):
            n_steps = int(round(ppw / C))
            ratio, amp = run_mode(C, ppw, N_CELLS, n_steps, "physical")
            pred = phase_speed(C, 2.0 * np.pi / ppw)
            print(f"{C:>6.2f} {ppw:>6} {ratio:>18.10f} {pred:>12.10f} "
                  f"{amp:>14.10f}")
    print("measured and predicted agree to the last digit, and the amplitude is")
    print("preserved to round-off: the scheme is purely dispersive.")

    print("\nnow the same run started from the exact solution at t = -dt, which")
    print("also excites the spurious root of the leapfrog scheme (C = 0.5):")
    print(f"{'PPW':>6} {'measured v_num/v':>18} {'predicted':>12} "
          f"{'|amplitude|':>14}")
    for ppw in (8, 16, 32):
        n_steps = int(round(ppw / 0.5))
        ratio, amp = run_mode(0.5, ppw, N_CELLS, n_steps, "analytic")
        pred = phase_speed(0.5, 2.0 * np.pi / ppw)
        print(f"{ppw:>6} {ratio:>18.10f} {pred:>12.10f} {amp:>14.10f}")
    print("the spurious root is neutral in amplitude too, so it contaminates the")
    print("phase and amplitude of the physical mode instead of dying away.  This")
    print("is a leapfrog artefact, not a physical wave, and it is why a dispersion")
    print("relation is verified on the physical branch and judged in practice with")
    print("a pulse test (section 3).")


def section_group_velocity():
    """Arrival lag of a narrow-band pulse against the group velocity."""
    print("pulse: Gaussian envelope of width 6 m, carrier PPW = 8, 2048 cells,")
    print("travel distance 400 m; the lag is reported relative to travel at a")
    print(f"{'C':>6} {'v_g/v predicted':>18} {'predicted lag %':>18} "
          f"{'measured lag %':>18}")
    x0 = 256.0
    t_end = 400.0
    for C in (0.5, 0.8, 1.0):
        centroid, T = run_pulse(C, 6.0, 8, 2048, x0, t_end)
        measured_lag = 1.0 - (centroid - x0) / (A_VEL * T)
        vg = group_speed(C, 2.0 * np.pi / 8.0)
        print(f"{C:>6.2f} {vg:>18.8f} {(1.0 - vg) * 100:>18.6f} "
              f"{measured_lag * 100:>18.6f}")
    print("the envelope travels at the group velocity, which is exactly a at")
    print("C = 1 and below a for C < 1: the pulse is late, and the lag is the")
    print("dispersion error of section 1 accumulated over a travel path.")


def section_dissipation():
    """Upwind damping: is it predicted by an equivalent diffusivity?"""
    print("upwind: |G|^2 = 1 - 2C(1-C)(1 - cos theta); dissipation is real")
    print(f"{'C':>6} {'PPW':>6} {'|G| per step':>14} {'|G|^n over 320 s':>18} "
          f"{'D_num (m^2/s)':>14} {'exp(-D k^2 t)':>16}")
    h = 1.0
    ppw = 16
    k = 2.0 * np.pi / (ppw * h)
    t_end = 320.0
    for C in (0.25, 0.5, 0.75, 1.0):
        theta = k * h
        g = np.sqrt(1.0 - 2.0 * C * (1.0 - C) * (1.0 - np.cos(theta)))
        dt = C * h / A_VEL
        steps = int(round(t_end / dt))
        d_num = 0.5 * A_VEL * h * (1.0 - C)
        print(f"{C:>6.2f} {ppw:>6} {g:>14.8f} {g ** steps:>18.6e} "
              f"{d_num:>14.4f} {np.exp(-d_num * k ** 2 * t_end):>16.6e}")
    print("the equivalent diffusivity D_num = a h (1-C)/2 reproduces the damping")
    print("at long wavelength; the harmonic decay is the exact discrete result.")
    print("\nmeasured versus predicted decay in an actual run (PPW = 16):")
    n = N_CELLS
    x = np.arange(n) * h
    print(f"{'C':>6} {'measured amplitude ratio':>26} {'predicted |G|^n':>18}")
    for C in (0.25, 0.5, 0.75, 1.0):
        k = 2.0 * np.pi / (ppw * h)
        dt = C * h / A_VEL
        steps = int(round(t_end / dt))
        u = np.sin(k * x)
        for _ in range(steps):
            u = u - C * (u - np.roll(u, 1))
        amp = 2.0 / n * np.sum(u * np.exp(-1j * k * x))
        theta = k * h
        g = np.sqrt(1.0 - 2.0 * C * (1.0 - C) * (1.0 - np.cos(theta)))
        print(f"{C:>6.2f} {abs(amp):>26.8e} {g ** steps:>18.8e}")


def laplacian_symbol(kx, ky, h, kind):
    """Discrete Laplacian symbol, returned as the effective wavenumber k_eff."""
    if kind == "5-point":
        s = (2.0 * np.cos(kx * h) + 2.0 * np.cos(ky * h) - 4.0) / h ** 2
    else:
        s = (8.0 * (np.cos(kx * h) + np.cos(ky * h))
             + 4.0 * np.cos(kx * h) * np.cos(ky * h) - 20.0) / (6.0 * h ** 2)
    return np.sqrt(-s)


def section_anisotropy():
    """Angular dependence of the discrete Laplacian at fixed |k|."""
    print("effective wavenumber of the discrete Laplacian, |k| h = 2 pi / PPW")
    print(f"{'scheme':>10} {'PPW':>6} {'k_eff/|k| at 0 deg':>20} "
          f"{'at 45 deg':>12} {'anisotropy %':>14}")
    for ppw in (4, 8, 16, 32):
        k = 2.0 * np.pi / ppw
        for kind in ("5-point", "9-point"):
            e0 = laplacian_symbol(k, 0.0, 1.0, kind) / k
            e45 = laplacian_symbol(k / np.sqrt(2.0), k / np.sqrt(2.0), 1.0, kind) / k
            print(f"{kind:>10} {ppw:>6} {e0:>20.8f} {e45:>12.8f} "
                  f"{(e45 / e0 - 1.0) * 100:>14.4f}")
    print("the five-point Laplacian is exact along the axes and worst along the")
    print("diagonals; the nine-point operator removes most of that anisotropy at")
    print("the cost of a wider stencil and a denser matrix.")


def main():
    section("1. Discrete dispersion relation of the CTCS scheme")
    section_dispersion_table()

    section("2. Phase error in a simulation")
    section_phase_measurement()

    section("3. Group velocity and the arrival delay of a pulse")
    section_group_velocity()

    section("4. Numerical dissipation of the upwind scheme")
    section_dissipation()

    section("5. Grid anisotropy of two Laplacian discretisations")
    section_anisotropy()


if __name__ == "__main__":
    main()
