#!/usr/bin/env python3
"""Finite-difference acoustic wave propagation: measured travel times against the
exact arrival, measured grid anisotropy, the exact von Neumann limit of the
2-D fourth-order scheme, and a measured normal-incidence reflection coefficient.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_wave_propagation_demo.py

All models and data in this module are SYNTHETIC.  The velocities, densities and
source frequencies below are chosen teaching values, not measurements.

Contents
--------
1. Two-dimensional phase speed along an axis and along a diagonal, against the
   phase speed of the discrete dispersion relation.
2. The exact von Neumann limit of the 2-D fourth-order scheme, and the measured
   growth of the highest mode at and beyond it.
3. A normal-incidence reflection coefficient in 1-D against (Z2-Z1)/(Z2+Z1).
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def ricker(t, t0, f0):
    tau = t - t0
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * tau ** 2) * np.exp(-a * tau ** 2)


def lap4_2d(u):
    """Fourth-order Laplacian stencil, returned in units of h^2."""
    d = (-np.roll(u, 2, 0) + 16.0 * np.roll(u, 1, 0) - 30.0 * u
         + 16.0 * np.roll(u, -1, 0) - np.roll(u, -2, 0))
    d += (-np.roll(u, 2, 1) + 16.0 * np.roll(u, 1, 1) - 30.0 * u
          + 16.0 * np.roll(u, -1, 1) - np.roll(u, -2, 1))
    return d / 12.0


def forward_2d(n, h, c, C, f0, t_end, recs, x_src):
    """Fourth-order in space, second-order in time, narrowband Gaussian source."""
    dt = C * h / c
    steps = int(round(t_end / dt))
    xx = np.arange(n) * h
    X, Y = np.meshgrid(xx, xx, indexing="ij")
    lam = c / f0                        # carrier wavelength
    sigma = 0.5 * lam                   # spatially narrowband source
    src_map = np.exp(-((X - x_src) ** 2 + (Y - x_src) ** 2) / (2.0 * sigma ** 2))
    p_prev = np.zeros((n, n))
    p = np.zeros((n, n))
    traces = np.zeros((len(recs), steps))
    for k in range(steps):
        t = k * dt
        p_next = (2.0 * p - p_prev + C ** 2 * lap4_2d(p)
                  + 0.5 * C ** 2 * src_map * ricker(t, 1.5 / f0, f0))
        for r, (ix, iy) in enumerate(recs):
            traces[r, k] = p_next[ix, iy]
        p_prev, p = p, p_next
    return np.arange(steps) * dt, traces


def discrete_omega(kx, ky, h, c, C):
    """Frequency of the 2-D fourth-order scheme: cos(omega dt) = 1 - C^2 S / 2."""
    def sym(k):
        return (30.0 - 32.0 * np.cos(k * h) + 2.0 * np.cos(2.0 * k * h)) / 12.0
    S = sym(kx) + sym(ky)
    dt = C * h / c
    return np.arccos(np.clip(1.0 - 0.5 * C ** 2 * S, -1.0, 1.0)) / dt


def group_speed(k, phi, h, c, C):
    """Magnitude of the discrete group velocity along the direction phi."""
    dk = 1e-5 * k
    kx, ky = k * np.cos(phi), k * np.sin(phi)
    wx = (discrete_omega(kx + dk, ky, h, c, C)
          - discrete_omega(kx - dk, ky, h, c, C)) / (2.0 * dk)
    wy = (discrete_omega(kx, ky + dk, h, c, C)
          - discrete_omega(kx, ky - dk, h, c, C)) / (2.0 * dk)
    return np.hypot(wx, wy)


N_GRID = 401
H_GRID = 10.0
C_GRID = 0.4
C_ACOUSTIC = 1000.0
X_SRC = 200.0 * H_GRID
REC_FROM = 40             # first receiver along the ray, in cells from the source
REC_TO = 100


def sponge_2d(n, width=60):
    """Absorbing taper near the four edges of the square grid."""
    idx = np.arange(n)
    dist = np.minimum(idx, n - 1 - idx).astype(float)
    tap = np.ones(n)
    mask = dist < width
    tap[mask] = 1.0 - 0.05 * ((width - dist[mask]) / width) ** 2
    return tap[:, None] * tap[None, :]


def mono_run(f0, recs, t_periods=40.0):
    """Monochromatic 2-D acoustic run with absorbing edges."""
    n, h, c, C = N_GRID, H_GRID, C_ACOUSTIC, C_GRID
    dt = C * h / c
    steps = int(round(t_periods / f0 / dt))
    t = np.arange(steps) * dt
    xx = np.arange(n) * h
    X, Y = np.meshgrid(xx, xx, indexing="ij")
    lam = c / f0
    src_map = np.exp(-((X - X_SRC) ** 2 + (Y - X_SRC) ** 2)
                     / (2.0 * (0.5 * lam) ** 2))
    tap = sponge_2d(n)
    p_prev = np.zeros((n, n))
    p = np.zeros((n, n))
    traces = np.zeros((len(recs), steps))
    for k in range(steps):
        tk = k * dt
        ramp = min(1.0, f0 * tk / 5.0)
        p_next = (2.0 * p - p_prev + C ** 2 * lap4_2d(p)
                  + 0.5 * C ** 2 * src_map * ramp * np.cos(2.0 * np.pi * f0 * tk))
        p_next *= tap
        for r, (ix, iy) in enumerate(recs):
            traces[r, k] = p_next[ix, iy]
        p_prev, p = p, p_next
    return t, traces


def measured_phase_speed(f0, diagonal=False, t_periods=40.0):
    """Phase speed from the slope of the unwrapped spatial phase along a ray.

    Every cell between REC_FROM and REC_TO along the ray is a receiver, so the
    phase profile is unwrapped cell by cell and fitted, which removes the
    wrap ambiguity of a two-receiver measurement.
    """
    isrc = int(round(X_SRC / H_GRID))
    cells = np.arange(REC_FROM, REC_TO)   # offsets from the source, in cells
    recs = [((isrc + i, isrc + i) if diagonal else (isrc + i, isrc))
            for i in cells]
    t, tr = mono_run(f0, recs, t_periods=t_periods)
    sel = t > 0.5 * t[-1]
    window = np.exp(-1j * 2.0 * np.pi * f0 * t[sel]) * np.hanning(int(sel.sum()))
    amps = np.array([np.sum(tr[i][sel] * window) for i in range(len(recs))])
    r = (cells - isrc) * H_GRID * (np.sqrt(2.0) if diagonal else 1.0)
    phase = np.unwrap(np.angle(amps))
    k_num = abs(np.polyfit(r, phase, 1)[0])
    return 2.0 * np.pi * f0 / k_num


def travel_times():
    print("2-D acoustic model: c = 1000 m/s, h = 10 m, C = c dt/h = 0.4,")
    print("fourth-order in space, second-order in time, absorbing edges; a")
    print("monochromatic point source and a dense line of receivers along a ray,")
    print("so the spatial phase is unwrapped cell by cell and its slope fitted")
    print("the prediction is the phase speed of the discrete dispersion relation")
    print("cos(omega dt) = 1 - C^2 S/2, evaluated at the carrier wavenumber")
    print(f"{'PPW':>5} {'axis measured':>14} {'predicted':>11} "
          f"{'diag measured':>14} {'predicted':>11} {'diag-axis %':>12}")
    for ppw in (4.0, 8.0, 16.0):
        f0 = C_ACOUSTIC / (ppw * H_GRID)
        va = measured_phase_speed(f0, diagonal=False)
        vd = measured_phase_speed(f0, diagonal=True)
        k = 2.0 * np.pi / (ppw * H_GRID)
        pa = discrete_omega(k, 0.0, H_GRID, C_ACOUSTIC, C_GRID) / (k * C_ACOUSTIC)
        kd = k / np.sqrt(2.0)
        pd = discrete_omega(kd, kd, H_GRID, C_ACOUSTIC, C_GRID) / (k * C_ACOUSTIC)
        print(f"{ppw:>5.1f} {va / C_ACOUSTIC:>14.8f} {pa:>11.8f} "
              f"{vd / C_ACOUSTIC:>14.8f} {pd:>11.8f} "
              f"{(vd / va - 1.0) * 100:>12.5f}")
    print("the waves are slower than the continuum value 1 by a fraction that")
    print("falls with resolution, and the diagonal is consistently faster than")
    print("the axis: that difference is the numerical anisotropy of the stencil.")


def von_neumann_limit_2d():
    def sym(k):
        return (30.0 - 32.0 * np.cos(k) + 2.0 * np.cos(2.0 * k)) / 12.0
    s_max = 2.0 * sym(np.pi)
    c_limit = 2.0 / np.sqrt(s_max)
    print("exact von Neumann limit of the 2-D fourth-order scheme: the growth")
    print("factor has modulus one only while |1 - C^2 S/2| <= 1 for every mode,")
    print("and the symbol S is largest at the grid Nyquist corner")
    print(f"  S_max = {s_max:.6f} in units of h^2, so C_max = 2/sqrt(S_max) = "
          f"{c_limit:.6f}")
    print("  the five-point (second-order) scheme has S_max = 8, giving the")
    print(f"  familiar limit 1/sqrt(2) = {1.0 / np.sqrt(2.0):.6f}")
    print("\nmeasured growth per step of the pure Nyquist eigenmode, 200 steps:")
    print(f"{'C':>8} {'predicted |G|':>15} {'measured growth':>18} {'stable?':>9}")
    n = 64
    j = np.arange(n)
    u0 = np.exp(1j * np.pi * (j[:, None] + j[None, :]))
    for C in (0.55, 0.60, 0.6124, 0.65, 0.70):
        b = 1.0 - 0.5 * C ** 2 * s_max
        if abs(b) <= 1.0:
            g = complex(b, np.sqrt(max(0.0, 1.0 - b ** 2)))
        else:
            b = float(np.real(b))
            g = b + np.sign(b) * np.sqrt(b ** 2 - 1.0)
        u_prev = u0 / g
        u = u0.copy()
        amp0 = np.max(np.abs(u0))
        for _ in range(200):
            u_next = 2.0 * u - u_prev + C ** 2 * lap4_2d(u)
            u_prev, u = u, u_next
        growth = (np.max(np.abs(u)) / amp0) ** (1.0 / 200.0)
        print(f"{C:>8.4f} {abs(g):>15.8f} {growth:>18.8f} "
              f"{'yes' if growth <= 1.0 + 1e-10 else 'no':>9}")
    print("the measured growth equals the predicted |G| to the last digit on both")
    print("sides of the limit, which is what makes an unstable run diagnosable")


def reflection_1d():
    """Dimensionless staggered 1-D acoustic scheme; reflection coefficient.

    All lengths are in wavelengths of the upper medium, so refining the grid
    means increasing the number of cells per wavelength.
    """
    print("dimensionless staggered 1-D acoustic scheme, second order:")
    print("  v_t = -(1/rho) p_x,   p_t = -K v_x,   K = rho c^2 (bulk modulus)")
    c1, rho1, c2, rho2 = 1.0, 1.0, 1.5, 1.2
    z1, z2 = rho1 * c1, rho2 * c2
    R_exact = (z2 - z1) / (z2 + z1)
    T_exact = 2.0 * z2 / (z2 + z1)
    print(f"  upper medium: rho = {rho1:.2f}, c = {c1:.2f}, Z1 = {z1:.2f}")
    print(f"  lower medium: rho = {rho2:.2f}, c = {c2:.2f}, Z2 = {z2:.2f}")
    print(f"  exact normal-incidence R = {R_exact:.6f}, T = {T_exact:.6f}")
    print("  lengths are in wavelengths of the upper medium: source at 5, front")
    print("  receiver at 8, interface at 15, back receiver at 25, domain 40")
    x_src, x_int, x_front, x_back, length = 5.0, 15.0, 8.0, 25.0, 40.0
    f0, t0, t_end = 1.0, 1.5, 26.0
    print(f"  Ricker source, dominant frequency {f0:.1f}, peak at t = {t0:.1f}")
    print(f"{'cells/wavelength':>17} {'h':>9} {'steps':>7} {'measured R':>13} "
          f"{'R error %':>11} {'measured T':>13} {'T error %':>11}")
    for ppw in (8.0, 16.0, 32.0, 64.0):
        h = c1 / (f0 * ppw)
        n = int(round(length / h))
        xv = (np.arange(n) + 0.5) * h
        xp = np.arange(n) * h
        dt = 0.5 * h / c2
        steps = int(round(t_end / dt))
        t = np.arange(steps) * dt
        i_front = int(round(x_front / h))
        i_back = int(round(x_back / h))
        i_src = int(round(x_src / h))
        t_inc = t0 + (x_front - x_src) / c1
        t_ref = t0 + (x_int - x_src) / c1 + (x_int - x_front) / c1
        t_tr = t0 + (x_int - x_src) / c1 + (x_back - x_int) / c2
        win = 0.5 / f0

        def run(with_interface):
            rho = (np.where(xv < x_int, rho1, rho2) if with_interface
                   else np.full(n, rho1))
            cc = (np.where(xp < x_int, c1, c2) if with_interface
                  else np.full(n, c1))
            K = rho * cc ** 2
            p = np.zeros(n)
            v = np.zeros(n)
            rec_f = np.zeros(steps)
            rec_b = np.zeros(steps)
            for k in range(steps):
                v = v - (dt / (rho * h)) * (np.roll(p, -1) - p)
                p = p - (dt * K / h) * (v - np.roll(v, 1))
                p[i_src] += dt * ricker(t[k], t0, f0)
                rec_f[k] = p[i_front]
                rec_b[k] = p[i_back]
            return rec_f, rec_b

        f_int, b_int = run(True)
        f_uni, b_uni = run(False)
        a_inc = np.max(np.abs(f_uni[np.abs(t - t_inc) < win]))
        d_ref = (f_int - f_uni)[np.abs(t - t_ref) < win]
        R_meas = d_ref[int(np.argmax(np.abs(d_ref)))] / a_inc
        d_tr = (b_int - b_uni)[np.abs(t - t_tr) < win]
        T_meas = d_tr[int(np.argmax(np.abs(d_tr)))] / a_inc
        print(f"{ppw:>17.1f} {h:>9.5f} {steps:>7} {R_meas:>13.6f} "
              f"{(R_meas / R_exact - 1.0) * 100:>11.4f} {T_meas:>13.6f} "
              f"{(T_meas / T_exact - 1.0) * 100:>11.4f}")
    print("the reflected and transmitted amplitudes are read from the scattered")
    print("field: the difference between the layered and the uniform runs removes")
    print("both the direct arrival and the reflection from the left edge, and the")
    print("window is short enough that the far edge has not answered yet.")


def main():
    section("1. Two-dimensional phase speed against the discrete relation")
    travel_times()

    section("2. The von Neumann limit of the 2-D fourth-order scheme")
    von_neumann_limit_2d()

    section("3. Normal-incidence reflection and transmission coefficients")
    reflection_1d()


if __name__ == "__main__":
    main()
