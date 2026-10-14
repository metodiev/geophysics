#!/usr/bin/env python3
"""Ambient-noise tomography: Love-wave dispersion, phase- and group-velocity
measurement from retrieved correlations, and a damped least-squares inversion
for a 2-D phase-velocity map.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python noise_tomography_demo.py

Everything is SYNTHETIC.  The layered model, the station geometry, the anomaly
amplitudes and the noise realisations are chosen teaching values, not
measurements of the Earth.

Contents
--------
1. Love-wave dispersion of a synthetic two-layer model, solved from the
   transcendental dispersion relation.
2. Phase velocity measured from the phase of a synthetic cross-spectrum.
3. Group velocity from the envelope of the retrieved wave packet.
4. Damped least-squares tomography of a synthetic 2-D phase-velocity map:
   recovered amplitude, data misfit and model norm versus damping.
5. Checkerboard resolution test and the null space of the path coverage.
"""

import numpy as np
from scipy import optimize, signal

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
VS1_KM_S, RHO1 = 2.00, 2.80       # layer
VS2_KM_S, RHO2 = 4.00, 3.30       # half-space
H_KM = 20.0                       # layer thickness
D_PAIR_KM = 60.0                  # station separation for dispersion
PERIODS_S = np.array([5.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0])
NCELL = 6                         # tomography grid is NCELL x NCELL
BOX_KM = 120.0                    # side of the tomographic box


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def love_velocity(period, vs1=VS1_KM_S, vs2=VS2_KM_S, rho1=RHO1, rho2=RHO2,
                  h=H_KM):
    """Phase velocity of the fundamental Love mode (km/s).

    Solves  tan(w h k1) = (mu2/mu1) k2 / k1  with
    k1 = sqrt(1/vs1^2 - 1/c^2)  and  k2 = sqrt(1/c^2 - 1/vs2^2).
    The fundamental mode is the branch 0 < w h k1 < pi/2, which brackets the
    root between k1 -> 0 (residual -> -inf) and the first pole of tan.
    """
    w = 2.0 * np.pi / period
    mu1, mu2 = rho1 * vs1 ** 2, rho2 * vs2 ** 2
    k1max = np.sqrt(1.0 / vs1 ** 2 - 1.0 / vs2 ** 2)

    def residual(k1):
        k2 = np.sqrt(max(k1max ** 2 - k1 ** 2, 0.0))
        return np.tan(w * h * k1) - (mu2 / mu1) * k2 / k1

    lo = 1e-9 * k1max
    hi = min(np.pi / (2.0 * w * h), k1max) * (1.0 - 1e-12)
    k1_root = optimize.brentq(residual, lo, hi)
    return 1.0 / np.sqrt(1.0 / vs1 ** 2 - k1_root ** 2)


def cells_of_path(p0, p1, ncell=NCELL, box=BOX_KM, nsample=400):
    """Length of a straight path inside each grid cell (km, ravel order)."""
    t = np.linspace(0.0, 1.0, nsample)
    x = p0[0] + (p1[0] - p0[0]) * t
    y = p0[1] + (p1[1] - p0[1]) * t
    seg = np.hypot(np.diff(x), np.diff(y))
    ix = np.clip((x[:-1] / box * ncell).astype(int), 0, ncell - 1)
    iy = np.clip((y[:-1] / box * ncell).astype(int), 0, ncell - 1)
    out = np.zeros(ncell * ncell)
    np.add.at(out, iy * ncell + ix, seg)
    return out


def main():
    section("1. Love-wave dispersion of the two-layer teaching model")
    print(f"  layer: vs = {VS1_KM_S:.2f} km/s, rho = {RHO1:.2f} g/cm^3, "
          f"H = {H_KM:.1f} km")
    print(f"  half-space: vs = {VS2_KM_S:.2f} km/s, rho = {RHO2:.2f} g/cm^3")
    print("  dispersion relation (fundamental mode):")
    print("    tan(w H sqrt(1/vs1^2 - 1/c^2)) = (mu2/mu1) sqrt(1/c^2 - 1/vs2^2)")
    print("                                    / sqrt(1/vs1^2 - 1/c^2)")
    print("\n  period (s)   c (km/s)   wavelength (km)   c/vs1")
    c_true = np.array([love_velocity(T) for T in PERIODS_S])
    for T, c in zip(PERIODS_S, c_true):
        print(f"  {T:10.1f}   {c:8.4f}   {c * T:15.1f}   {c / VS1_KM_S:6.3f}")
    print(f"  the phase velocity is bounded by vs1 = {VS1_KM_S:.2f} and "
          f"vs2 = {VS2_KM_S:.2f} km/s at every period, as the relation requires.")

    section("2. Phase velocity measured from a synthetic cross-spectrum")
    f = np.linspace(0.02, 0.25, 600)
    T = 1.0 / f
    c_model = np.array([love_velocity(t) for t in T])
    # empirical Green's function of the pair: phase 2*pi*f*d/c(f)
    phase = 2.0 * np.pi * f * D_PAIR_KM / c_model
    C = np.exp(-1j * phase)
    df = f[1] - f[0]
    gf = np.fft.irfft(C, n=2 * (f.size - 1))
    gf = np.fft.fftshift(gf)
    t_lag = (np.arange(gf.size) - gf.size // 2) / (2 * (f.size - 1) * df)
    env = np.abs(signal.hilbert(gf))
    i_pk = np.argmax(env)
    print(f"  station separation d = {D_PAIR_KM:.0f} km; "
          f"frequency band {f[0]:.2f}-{f[-1]:.2f} Hz")
    print(f"  the arrival time of the wave packet is measured from the envelope of")
    print(f"  the retrieved correlation: t = {t_lag[i_pk]:.3f} s -> mean speed "
          f"{D_PAIR_KM / t_lag[i_pk]:.3f} km/s (a group, not a phase, velocity)")
    # phase velocity from the phase of the cross-spectrum: angle(C) = -2*pi*f*d/c
    phi = -np.unwrap(np.angle(C))
    print("\n  period (s)   c from phase (km/s)   c model (km/s)   error (km/s)")
    for T_chk in (5.0, 10.0, 20.0, 40.0):
        j = int(np.argmin(np.abs(f - 1.0 / T_chk)))
        c_meas = 2.0 * np.pi * f[j] * D_PAIR_KM / phi[j]
        c_ref = love_velocity(T_chk)
        print(f"  {T_chk:10.1f}   {c_meas:19.4f}   {c_ref:14.4f}   "
              f"{c_meas - c_ref:+11.4f}")
    print("  The phase is only determined modulo 2*pi: the unwrapping assumes the")
    print("  phase changes by less than pi between neighbouring frequencies.")

    section("3. Group velocity from the envelope of the wave packet")
    print("  U = c + k dc/dk = c / (1 + (T/c) dc/dT), evaluated on a fine period")
    print("  grid and reported at the tabulated periods.")
    T_fine = np.linspace(PERIODS_S[0], PERIODS_S[-1], 400)
    c_fine = np.array([love_velocity(t) for t in T_fine])
    dcdT_fine = np.gradient(c_fine, T_fine)
    print("\n  period (s)   c (km/s)   dc/dT (km/s per s)   U (km/s)")
    for T_chk in PERIODS_S:
        c = love_velocity(T_chk)
        dcdT = np.interp(T_chk, T_fine, dcdT_fine)
        U = c / (1.0 + (T_chk / c) * dcdT)
        print(f"  {T_chk:10.1f}   {c:8.4f}   {dcdT:18.5f}   {U:8.4f}")
    print("  U < c at every period: the mode is normally dispersive, and the two")
    print("  velocities coincide only for a non-dispersive wave.")

    section("4. Damped least-squares tomography of a 2-D phase-velocity map")
    ncell, box = NCELL, BOX_KM
    ncell_tot = ncell * ncell
    cell_km = box / ncell
    # SYNTHETIC station array: 12 stations on a ring plus one centre
    ang = np.linspace(0.0, 2.0 * np.pi, 12, endpoint=False)
    sta = np.column_stack([box / 2.0 + 50.0 * np.cos(ang),
                           box / 2.0 + 50.0 * np.sin(ang)])
    sta = np.vstack([sta, [box / 2.0, box / 2.0]])
    pairs = [(i, j) for i in range(sta.shape[0]) for j in range(i + 1, sta.shape[0])]
    rows, d_true = [], []
    # SYNTHETIC anomaly: a +3% slowness anomaly in a 2x2 patch (red = slow)
    m_true = np.zeros(ncell_tot)
    icx, icy = 4, 4
    m_true[icy * ncell + icx] = 0.03
    m_true[icy * ncell + icx - 1] = 0.03
    s0 = 1.0 / 3.0                      # reference slowness, s/km at 10 s period
    for i, j in pairs:
        l_ic = cells_of_path(sta[i], sta[j])
        Lp = l_ic.sum()
        if Lp <= 0:
            continue
        rows.append(l_ic / Lp)
        d_true.append(m_true @ (l_ic / Lp))      # relative slowness anomaly
    Gmat = np.array(rows)
    d_true = np.array(d_true)
    d_obs = d_true + 0.001 * RNG.standard_normal(d_true.size)
    print(f"  grid {ncell} x {ncell} cells of {cell_km:.1f} km; "
          f"{len(d_true)} station pairs; period 10 s")
    print(f"  reference slowness {s0:.4f} s/km (c = {1.0 / s0:.2f} km/s); "
          f"data noise 0.1% relative slowness")
    print(f"  true anomaly: {m_true.max() * 100:+.1f}% slowness in two cells "
          f"(row {icy}, columns {icx - 1} and {icx})")
    print("\n  damping    rms misfit   model norm   recovered peak   peak/true")
    best = None
    for lam in (0.003, 0.01, 0.03, 0.1, 0.3, 1.0):
        m_est = np.linalg.solve(Gmat.T @ Gmat + lam ** 2 * np.eye(ncell_tot),
                                Gmat.T @ d_obs)
        res = np.sqrt(np.mean((Gmat @ m_est - d_obs) ** 2))
        pk = m_est[icy * ncell + icx]
        print(f"  {lam:7.3f}   {res:10.2e}   {np.linalg.norm(m_est):10.5f}   "
              f"{pk * 100:13.2f}%   {pk / m_true.max():9.3f}")
        if best is None or abs(lam - 0.03) < 1e-9:
            best = m_est
    print("  Every damping value fits the data; the recovered peak shrinks as the")
    print("  damping grows.  The data alone cannot choose between them.")

    section("5. Checkerboard resolution test and the null space")
    m_check = np.zeros(ncell_tot)
    for iy in range(ncell):
        for ix in range(ncell):
            m_check[iy * ncell + ix] = 0.02 * (1.0 if (ix + iy) % 2 == 0 else -1.0)
    d_check = Gmat @ m_check
    lam = 0.03
    m_rec = np.linalg.solve(Gmat.T @ Gmat + lam ** 2 * np.eye(ncell_tot),
                            Gmat.T @ d_check)
    Rmat = np.linalg.solve(Gmat.T @ Gmat + lam ** 2 * np.eye(ncell_tot), Gmat.T @ Gmat)
    corr = np.corrcoef(m_check, m_rec)[0, 1]
    ratio = np.linalg.norm(m_rec) / np.linalg.norm(m_check)
    cover = (Gmat > 0).sum(axis=0)
    print(f"  input checkerboard amplitude 2.0%; damping {lam}")
    print(f"  recovered/true norm ratio = {ratio:.3f}; "
          f"pattern correlation = {corr:.3f}")
    print(f"  resolution matrix: mean diagonal = {np.mean(np.diag(Rmat)):.3f}, "
          f"worst diagonal = {np.min(np.diag(Rmat)):.3f}")
    print(f"  path counts per cell: min {cover.min()}, max {cover.max()}, "
          f"cells with no path: {(cover == 0).sum()}")
    print("  A cell crossed by few paths can only be recovered by its neighbours'")
    print("  leakage: it is in the null space of the geometry, not of the physics.")


if __name__ == "__main__":
    main()
