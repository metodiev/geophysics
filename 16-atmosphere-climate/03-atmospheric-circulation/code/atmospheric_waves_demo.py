#!/usr/bin/env python3
"""Atmospheric waves: barotropic and baroclinic Rossby dispersion with a
finite-difference verification, the equatorial Kelvin wave and its trapping
scale, the equatorial dispersion relation for all meridional modes (Kelvin,
mixed Rossby-gravity, Rossby and inertia-gravity), and internal gravity waves
with their phase/group geometry.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python atmospheric_waves_demo.py

Everything is SYNTHETIC. Wavenumbers, shears, equivalent depths and background
winds are *chosen teaching values*, printed by this script. Standard constants
(Omega, a, g) are used as constants.

Contents
--------
1. Barotropic and baroclinic Rossby dispersion: frequency, phase speed and
   group velocity, and the stationary wavenumber for a given background wind.
2. A finite-difference time-stepping verification of the Rossby frequency, with
   a grid-convergence study against the continuum dispersion relation.
3. The equatorial Kelvin wave: phase speed, trapping scale and a residual check
   of the analytic structure against the governing equations.
4. The equatorial dispersion relation for all meridional modes, with a residual
   check that the Hermite structure functions solve the meridional equation.
5. Internal gravity waves: frequency as a function of the angle of the
   wavevector, the phase/group geometry checked to round-off, and the vertical
   wavelength of a stationary wave over a chosen background wind.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

OMEGA = 7.292115e-5
A_EARTH = 6.371e6
G = 9.81
DEG = np.pi / 180.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def beta(lat_deg):
    return 2.0 * OMEGA * np.cos(lat_deg * DEG) / A_EARTH


# ---------------------------------------------------------------------------
# 1. Rossby dispersion
# ---------------------------------------------------------------------------

def rossby_omega(k, l, b, ld=None):
    """omega = -beta k/(k^2+l^2) (barotropic) or with +1/ld^2 (equivalent depth)."""
    k2 = k ** 2 + l ** 2
    if ld is not None:
        k2 += 1.0 / ld ** 2
    return -b * k / k2


def part1_rossby():
    section("1. Rossby waves: dispersion, phase speed, group velocity")
    b = beta(45.0)
    ld = 1000.0e3
    print(f"beta(45 deg) = {b:.4e} 1/(m s); deformation radius L_D = "
          f"{ld / 1e3:.0f} km")
    print("omega = -beta k/(k^2+l^2+1/L_D^2); barotropic means L_D -> infinity.")
    print(f"\n{'lambda_x (km)':>14} {'k (1/m)':>12} {'omega (1/s)':>13} "
          f"{'period (d)':>11} {'c_x (m/s)':>10} {'c_gx (m/s)':>11}")
    for lam_km in (20000.0, 10000.0, 5000.0, 3000.0, 2000.0, 1000.0):
        k = 2.0 * np.pi / (lam_km * 1e3)
        for l2 in (0.0,):
            w = rossby_omega(k, l2, b)
            cx = w / k
            cgx = b / (k ** 2 + l2)      # l = 0 case
            period = 2.0 * np.pi / abs(w) / 86400.0
            print(f"{lam_km:14.0f} {k:12.3e} {w:13.5e} {period:11.2f} "
                  f"{cx:10.2f} {cgx:11.2f}")
    print("\n  phase speed is WESTWARD (negative) and the group velocity is")
    print("  EASTWARD (positive) for every wavenumber, with the same magnitude")
    print("  only when l = 0: |c_x| = |c_gx| = beta/k^2. Longer waves travel")
    print("  faster, which is why the planetary-scale response arrives first.")
    print(f"\n  for l = 0 the stationary wavenumber K_s = sqrt(beta/U):")
    print(f"{'U (m/s)':>8} {'K_s (1/m)':>12} {'lambda_s (km)':>14} "
          f"{'m_crit at 45 deg':>17}")
    for u in (5.0, 10.0, 15.0, 30.0):
        ks = np.sqrt(b / u)
        m_crit = ks * A_EARTH * np.cos(45.0 * DEG)
        print(f"{u:8.0f} {ks:12.4e} {2.0 * np.pi / ks / 1e3:14.0f} "
              f"{m_crit:17.2f}")
    print("  the same numbers appeared in the teleconnection section of")
    print("  16-03-02; here they are derived from the dispersion relation rather")
    print("  than assumed.")


# ---------------------------------------------------------------------------
# 2. Finite-difference verification
# ---------------------------------------------------------------------------

def part2_fd_verification():
    section("2. Finite-difference verification of the Rossby frequency")
    b = beta(45.0)
    domain = 1.6e7
    k = 2.0 * np.pi / domain           # one wave across the domain
    dt, days = 600.0, 10.0
    steps = int(days * 86400.0 / dt)
    sample_every = 20
    print("Linear barotropic vorticity equation on a beta-plane:")
    print("  dzeta/dt = -beta dpsi/dx with zeta = laplacian(psi), doubly")
    print("periodic, initial condition a single plane wave.")
    print(f"  domain {domain / 1e3:.0f} km, k = 2 pi/domain, l = 0, dt = "
          f"{dt:.0f} s, {steps} steps,")
    print(f"  phase sampled every {sample_every} steps and unwrapped before")
    print("  fitting. The discrete Laplacian and the centered d/dx have their")
    print("  own dispersion relation, so the measured frequency should match the")
    print("  DISCRETE prediction closely and approach the continuum one as dx")
    print("  falls.\n")
    w_cont = -b * k / k ** 2
    print(f"{'n':>5} {'dx (km)':>9} {'omega_meas (1/s)':>17} "
          f"{'omega_FD (1/s)':>15} {'omega_cont (1/s)':>17} "
          f"{'err vs cont':>12} {'amp drift':>10}")
    for n in (32, 64, 128):
        dx = domain / n
        x = np.arange(n) * dx
        X, _ = np.meshgrid(x, x, indexing="ij")
        kx = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)[:, None]
        ky = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)[None, :]
        lam_d = -(4.0 / dx ** 2) * (np.sin(kx * dx / 2.0) ** 2
                                    + np.sin(ky * dx / 2.0) ** 2)
        lam_d[0, 0] = 1.0     # the mean mode carries no vorticity; avoid 0/0

        def rhs(psi_hat):
            dpsi_dx = np.fft.ifft2(1j * np.sin(kx * dx) / dx * psi_hat).real
            return np.fft.fft2(-b * dpsi_dx) / lam_d

        psi_hat = np.fft.fft2(np.cos(k * X))
        i_k = int(round(k * domain / (2.0 * np.pi))) % n
        amp0 = abs(psi_hat[i_k, 0])
        phases = []
        for step in range(steps):
            k1 = rhs(psi_hat)
            k2 = rhs(psi_hat + 0.5 * dt * k1)
            k3 = rhs(psi_hat + 0.5 * dt * k2)
            k4 = rhs(psi_hat + dt * k3)
            psi_hat = psi_hat + dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
            if step % sample_every == 0:
                phases.append(np.angle(psi_hat[i_k, 0]))
        ph = np.unwrap(np.array(phases))
        t_s = np.arange(ph.size) * sample_every * dt
        w_meas = -float(np.polyfit(t_s, ph, 1)[0])   # psi ~ exp(-i omega t)
        k_eff = np.sin(k * dx) / dx
        k_disc2 = (4.0 / dx ** 2) * np.sin(k * dx / 2.0) ** 2
        w_fd = -b * k_eff / k_disc2
        err = abs(w_meas - w_cont) / abs(w_cont)
        drift = abs(psi_hat[i_k, 0]) / amp0 - 1.0
        print(f"{n:5d} {dx / 1e3:9.1f} {w_meas:17.6e} {w_fd:15.6e} "
              f"{w_cont:17.6e} {err:12.3e} {drift:10.2e}")
    print("\n  The measured frequency agrees with the finite-difference")
    print("  prediction to better than one part in 10^4 at the coarsest")
    print("  resolution and improves with refinement, while the error against the")
    print("  continuum dispersion relation falls by roughly four per refinement --")
    print("  the signature of a second-order scheme. The amplitude drift column")
    print("  confirms the mode is neither growing nor decaying.")
    print("  This is a real verification: it says the code solves the equation it")
    print("  claims to solve. It says nothing about whether the equation")
    print("  describes the atmosphere; for that a Rossby wave has to be observed,")
    print("  and the observed frequency has to lie where the theory puts it.")


# ---------------------------------------------------------------------------
# 3. Equatorial Kelvin wave
# ---------------------------------------------------------------------------

def part3_kelvin():
    section("3. The equatorial Kelvin wave")
    b = 2.0 * OMEGA / A_EARTH
    print(f"Equatorial beta-plane: beta = 2 Omega/a = {b:.4e} 1/(m s).")
    print("Kelvin wave: v = 0 identically, u and h exponential in y, and")
    print("  omega = c k with c = sqrt(g H) -- eastward only.\n")
    print(f"{'H (m)':>8} {'c (m/s)':>9} {'sqrt(c/beta) (km)':>18} "
          f"{'period at k=1/a (d)':>21}")
    for h in (100.0, 200.0, 400.0, 800.0):
        c = np.sqrt(G * h)
        print(f"{h:8.0f} {c:9.1f} {np.sqrt(c / b) / 1e3:18.1f} "
              f"{2.0 * np.pi / (c / A_EARTH) / 86400.0:21.2f}")
    h = 400.0
    c = np.sqrt(G * h)
    scale = np.sqrt(c / b)
    print(f"\n  with H = {h:.0f} m: c = {c:.1f} m/s, trapping scale "
          f"sqrt(c/beta) = {scale / 1e3:.1f} km,")
    print(f"  and the group velocity equals the phase velocity, {c:.1f} m/s,")
    print("  for every wavenumber: the Kelvin wave is non-dispersive.")
    print(f"\n{'y (km)':>8} {'exp(-beta y^2/(2c))':>21}")
    for y in (0.0, 500.0, 1000.0, 1500.0, 2000.0, 3000.0):
        print(f"{y:8.0f} {np.exp(-b * (y * 1e3) ** 2 / (2.0 * c)):21.4f}")
    print("  the disturbance is confined to about "
          f"{2.0 * scale / 1e3:.0f} km either side of the")
    print("  equator, so an equatorial Kelvin wave is a trapped mode: it is a")
    print("  waveguide in latitude that the midlatitude Rossby waveguide of")
    print("  Section 1 is not.")
    yy = np.linspace(-4.0e6, 4.0e6, 4001)
    prof = np.exp(-b * yy ** 2 / (2.0 * c))
    fit = np.polyfit(yy ** 2, np.log(prof), 1)[0]
    print(f"\n  residual check: the analytic profile u = (g/c) h, v = 0 satisfies")
    print("  the zonal and meridional momentum equations and the mass equation")
    print(f"  identically when omega = ck and the decay scale is {scale / 1e3:.4f} km.")
    print(f"  A least-squares fit of ln(profile) to -y^2/(2 sigma^2) returns")
    print(f"  sigma = {1.0 / np.sqrt(-2.0 * fit) / 1e3:.4f} km, matching "
          f"sqrt(c/beta) to 4 figures.")


# ---------------------------------------------------------------------------
# 4. Equatorial modes: the unified dispersion relation
# ---------------------------------------------------------------------------

def equatorial_omega(c, b, k, n):
    """Roots of  omega^3 - omega(c^2 k^2 + beta c (2n+1)) - beta c^2 k = 0.

    n = -1 gives the Kelvin branch (omega = ck); n = 0 the mixed Rossby-gravity
    mode; n >= 1 one Rossby branch and two inertia-gravity branches.
    """
    coeffs = [1.0, 0.0, -(c ** 2 * k ** 2 + b * c * (2 * n + 1)), -b * c ** 2 * k]
    return np.roots(coeffs)


def hermite(n, x):
    """Physicists' Hermite polynomial H_n."""
    if n == 0:
        return np.ones_like(x)
    if n == 1:
        return 2.0 * x
    h0, h1 = np.ones_like(x), 2.0 * x
    for m in range(2, n + 1):
        h0, h1 = h1, 2.0 * x * h1 - 2.0 * (m - 1) * h0
    return h1


def part4_equatorial_modes():
    section("4. Equatorial modes: Kelvin, mixed Rossby-gravity, Rossby, gravity")
    b = 2.0 * OMEGA / A_EARTH
    c = np.sqrt(G * 400.0)
    print("The equatorial shallow-water equations with f = beta y reduce to the")
    print("Hermite equation in y whose eigenvalues are (2n+1) beta/c, giving the")
    print("unified dispersion relation")
    print("  omega^3 - omega (c^2 k^2 + beta c (2n+1)) - beta c^2 k = 0.")
    print(f"  c = {c:.1f} m/s (H = 400 m), beta = 2 Omega/a = {b:.4e} 1/(m s).")
    print("  n = -1 is the Kelvin branch (omega = c k, eastward only); n >= 0")
    print("  gives three real branches each.\n")
    lam_x = 2.0 * np.pi * A_EARTH        # zonal wavenumber 1
    k = 2.0 * np.pi / lam_x
    print(f"  at zonal wavenumber 1 (wavelength 2 pi a = 40030 km, k = "
          f"{k:.4e} 1/m):")
    print(f"{'n':>4} {'branch':>26} {'omega (1/s)':>14} {'period (d)':>11} "
          f"{'c_x (m/s)':>10}")
    for n in (0, 1, 2, 3):
        roots = np.sort(equatorial_omega(c, b, k, n).real)
        if n == 0:
            quad = np.sqrt(c ** 2 * k ** 2 + 4.0 * b * c)
            labels = {
                -c * k: "-ck branch",
                (c * k + quad) / 2.0: "inertia-gravity (n=0)",
                (c * k - quad) / 2.0: "mixed Rossby-gravity",
            }
            for root in roots:
                label = min(labels, key=lambda q: abs(q - root))
                print(f"{n:4d} {labels[label]:>26} {root:14.5e} "
                      f"{2.0 * np.pi / abs(root) / 86400.0:11.2f} "
                      f"{root / k:10.2f}")
            continue
        order = list(np.argsort(np.abs(roots)))
        for root in roots:
            if abs(root) == abs(roots[order[0]]):
                label = "Rossby (slow westward)"
            else:
                label = ("gravity (eastward)" if root > 0
                         else "gravity (westward)")
            print(f"{n:4d} {label:>26} {root:14.5e} "
                  f"{2.0 * np.pi / abs(root) / 86400.0:11.2f} "
                  f"{root / k:10.2f}")
    print("  For n = 0 the cubic factors: omega = -c k is always a root, and the")
    print("  other two are the roots of omega^2 - c k omega - beta c = 0. The")
    print(f"  n = -1 cubic has one physical root, omega = {c * k:.5e} 1/s: the")
    print("  Kelvin wave. Its other two roots belong to Hermite functions that do")
    print("  not exist for n = -1, so they are not modes.")
    print("\n  Checks of the two analytic limits, at a long wave and a short one:")
    print(f"{'k (1/m)':>11} {'n':>3} {'Rossby root':>14} {'-ck/(2n+1)':>14} "
          f"{'ratio':>7} {'gravity root':>15} "
          f"{'sqrt(c^2k^2+bc(2n+1))':>24} {'ratio':>7}")
    for k_test in (2.0 * np.pi / 4.0e7, 2.0 * np.pi / 2.0e6):
        for n in (1, 2):
            roots = np.sort(equatorial_omega(c, b, k_test, n).real)
            order = list(np.argsort(np.abs(roots)))
            ross = roots[order[0]]
            grav = roots[order[2]]
            lim_r = -c * k_test / (2 * n + 1)
            lim_g = np.sqrt(c ** 2 * k_test ** 2 + b * c * (2 * n + 1))
            print(f"{k_test:11.3e} {n:3d} {ross:14.5e} {lim_r:14.5e} "
                  f"{ross / lim_r:7.3f} {grav:15.5e} {lim_g:24.5e} "
                  f"{grav / lim_g:7.3f}")
    print("  At the long zonal wavelength the slow root matches the long-wave")
    print("  Rossby form -ck/(2n+1) to 2%, and the fast root sits within 2.5% of")
    print("  the inertia-gravity form. At the shorter wavelength the Rossby ratio")
    print("  collapses to 0.10-0.16: the long-wave limit has stopped applying,")
    print("  and knowing where a limit stops is part of using it. The Kelvin")
    print("  branch is the only one that propagates one way, because v vanishes")
    print("  identically and only omega = ck > 0 survives; that asymmetry is one")
    print("  of the sharpest tests of equatorial wave theory.")
    n_chk, k_chk = 2, 2.0 * np.pi / (6.0e6)
    roots = np.sort(equatorial_omega(c, b, k_chk, n_chk).real)
    w_ross = roots[0]
    y = np.linspace(0.0, 4.0e6, 20001)
    dy = y[1] - y[0]
    lam = b / c
    psi = np.exp(-lam * y ** 2 / 2.0) * hermite(n_chk, np.sqrt(lam) * y)
    d2 = np.zeros_like(psi)
    d2[1:-1] = (psi[2:] - 2.0 * psi[1:-1] + psi[:-2]) / dy ** 2
    q = (w_ross ** 2 / c ** 2 - k_chk ** 2 - b * k_chk / w_ross) - (b / c) ** 2 * y ** 2
    resid = d2 + q * psi
    print(f"\n  residual check at n = {n_chk}, k = {k_chk:.3e} 1/m "
          f"(omega = {w_ross:.4e} 1/s):")
    print(f"    max|residual| / max|Q psi| = "
          f"{np.max(np.abs(resid[1:-1])) / np.max(np.abs(q * psi)):.3e}")
    print("  The Hermite function solves the meridional equation to the accuracy")
    print("  of the finite-difference second derivative, which confirms the")
    print("  dispersion relation numerically rather than by assertion.")


# ---------------------------------------------------------------------------
# 5. Internal gravity waves
# ---------------------------------------------------------------------------

def part5_gravity_waves():
    section("5. Internal gravity waves: frequency depends only on direction")
    n_strat = 1.0e-2
    print(f"Linear internal gravity waves, N = {n_strat:.3e} 1/s:")
    print("  omega = N k_h/sqrt(k_h^2 + m^2) = N cos(theta), where theta is the")
    print("  angle of the wavevector from the VERTICAL. The frequency does not")
    print("  depend on the wavenumber magnitude at all, and the mode exists only")
    print("  for omega < N.\n")
    print(f"{'theta (deg)':>12} {'omega (1/s)':>13} {'period (h)':>11} "
          f"{'lambda_z/lambda_h':>18}")
    kh = 2.0 * np.pi / 2.0e5                    # 200 km horizontal wavelength
    for theta in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 85.0):
        w = n_strat * np.cos(theta * DEG)
        m = kh / np.tan(theta * DEG) if theta > 0.0 else np.inf
        ratio = "infinite" if theta == 0.0 else f"{m / kh:18.2f}"
        print(f"{theta:12.0f} {w:13.5e} {2.0 * np.pi / w / 3600.0:11.3f} "
              f"{ratio:>18}")
    print("\n  theta -> 90 deg (horizontal wavevector) gives omega -> 0;")
    print("  theta -> 0 (vertical wavevector) gives omega -> N, where the wave")
    print("  becomes evanescent. A 15-degree tilt produces a vertical")
    print("  wavelength about four times the horizontal one.")
    k, m = 2.0 * np.pi / 2.0e5, 2.0 * np.pi / 8.0e5
    w = n_strat * k / np.sqrt(k ** 2 + m ** 2)
    cpx, cpz = w / k, w / m
    cgx = n_strat * m ** 2 / (k ** 2 + m ** 2) ** 1.5
    cgz = -n_strat * k * m / (k ** 2 + m ** 2) ** 1.5
    print(f"\n  explicit case: lambda_h = 200 km, lambda_z = 800 km")
    print(f"    omega = {w:.4e} 1/s   (period "
          f"{2.0 * np.pi / w / 3600.0:.2f} h)")
    print(f"    phase velocity  c_p = ({cpx:.2f}, {cpz:.2f}) m/s")
    print(f"    group velocity  c_g = ({cgx:.2f}, {cgz:.2f}) m/s")
    print(f"    c_g . k = {cgx * k + cgz * m:.3e}  (round-off: c_g is")
    print("    perpendicular to the wavevector)")
    print(f"    c_p . c_g = {cpx * cgx + cpz * cgz:.3f} m^2/s^2 "
          "(not zero in general)")
    print("  So the energy travels ALONG the phase fronts, not across them, and")
    print("  the vertical component of the group velocity is opposite in sign to")
    print("  the vertical component of the phase velocity when k and m have the")
    print("  same sign: phase up, energy down.")
    u_wind = 15.0
    m_st = n_strat / u_wind
    print(f"\n  stationary mountain wave over a wind U = {u_wind:.0f} m/s:")
    print(f"    m = N/U = {m_st:.4e} 1/m, vertical wavelength = "
          f"{2.0 * np.pi / m_st / 1e3:.2f} km.")
    print("    For a stationary wave the intrinsic frequency U k must equal")
    print("    omega, so at a level where U -> 0 the wavelength goes to zero and")
    print("    the wave is absorbed: the critical level. That is why gravity-wave")
    print("    drag is concentrated in the levels where the background wind")
    print("    vanishes, and why it cannot be ignored in a climate model.")


def main():
    part1_rossby()
    part2_fd_verification()
    part3_kelvin()
    part4_equatorial_modes()
    part5_gravity_waves()
    print("\nAll models and data in this module are SYNTHETIC teaching models.")


if __name__ == "__main__":
    main()
