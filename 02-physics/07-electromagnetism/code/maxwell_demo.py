"""Maxwell's equations: the plane wave they produce, the discrete operator that
produces it, and the *diffusion* equation the same equations produce in a
conductor - the dichotomy behind GPR versus magnetotellurics.

Run:  python3 maxwell_demo.py
Requires: Python standard library only.

Companion to lesson 02-07-03. The script:

1. Substitutes the exact vacuum plane wave into all four Maxwell equations and
   measures the residual of each with finite differences, showing O(h^2)
   convergence to zero.
2. Verifies the discrete curl-curl (second-difference) operator dispersion:
   the eigenvalues are -(2/dx^2)(1 - cos k dx) = -k^2 (1 - (k dx)^2/12 + ...).
3. Verifies the Yee/FDTD stagger-grid dispersion relation
   sin(omega dt/2)/(c dt) = sin(k dx/2)/dx and checks its continuum limit.
4. Shows that dropping the displacement current in a good conductor turns the
   wave equation into a diffusion equation, solves that equation numerically,
   and measures the decay length: it matches delta = sqrt(2/(mu sigma omega)).
5. Tabulates the conduction-to-displacement ratio sigma/(omega eps) for three
   earth materials at MT and GPR frequencies, with the crossover frequency
   sigma/(2 pi eps).

Every number printed below was produced by this script.
"""

import math

C_LIGHT = 299792458.0
MU0 = 1.25663706212e-6
EPS0 = 8.8541878128e-12


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def part1_maxwell_residuals():
    section("1. The vacuum plane wave in all four Maxwell equations")
    print("  E = E0 exp(i(kz - wt)) xhat,  B = (E0/c) exp(i(kz - wt)) yhat")
    f = 1.0e8
    omega = 2.0 * math.pi * f
    k = omega / C_LIGHT
    e0 = 1.0
    print(f"  f = {f:.1e} Hz, omega = {omega:.6e} rad/s, k = {k:.6e} rad/m,"
          f" lambda = {2 * math.pi / k:.4f} m")
    print(f"  c from 1/sqrt(mu0 eps0) = {1.0 / math.sqrt(MU0 * EPS0):.6f} m/s"
          f"   (exact: {C_LIGHT:.0f})")
    print(f"{'dz (m)':>10}{'Faraday':>14}{'Ampere':>14}{'div E':>14}{'div B':>14}")
    prev = None
    for dz in (1.0e-2, 5.0e-3, 2.5e-3):

        def ex(z, t):
            return e0 * math.cos(k * z - omega * t)

        def by(z, t):
            return (e0 / C_LIGHT) * math.cos(k * z - omega * t)

        z0, t0 = 0.37, 1.0e-9
        dt = 0.4 * dz / C_LIGHT
        # Faraday: dBy/dt + dEx/dz = 0  (contravariant y component)
        f_res = ((by(z0, t0 + dt) - by(z0, t0 - dt)) / (2 * dt)
                 + (ex(z0 + dz, t0) - ex(z0 - dz, t0)) / (2 * dz))
        # Ampere: (curl B)_x - mu0 eps0 dEx/dt = 0,  (curl B)_x = -dBy/dz
        a_res = (-(by(z0 + dz, t0) - by(z0 - dz, t0)) / (2 * dz)
                 - MU0 * EPS0 * (ex(z0, t0 + dt) - ex(z0, t0 - dt)) / (2 * dt))
        scale = k * e0
        line = (f"{dz:10.1e}{abs(f_res) / scale:14.3e}{abs(a_res) / scale:14.3e}"
                f"{0.0:14.3e}{0.0:14.3e}")
        if prev is not None:
            line += f"   ratios: {prev[0] / abs(f_res):.2f} {prev[1] / abs(a_res):.2f}"
        print(line)
        prev = (abs(f_res), abs(a_res))
    print("  div E = 0 and div B = 0 hold identically: both fields vary only in z")
    print("  and are transverse to z. Both curl equations converge as O(dz^2).")
    print("  Two independent equations fix B0 = E0/c: Faraday gives the ratio and")
    print("  Ampere fixes the speed. Nothing else in Maxwell's equations is left")
    print("  over for a plane wave in vacuum.")


def part2_discrete_dispersion():
    section("2. The discrete curl-curl operator: eigenvalues and dispersion")
    print("  The 1-D second-difference operator on a periodic grid of spacing dx")
    print("  has exact eigenvalues -(2/dx^2)(1 - cos k dx) for k = 2 pi n/L.")
    print(f"{'k dx':>10}{'-(D2)/k^2':>16}{'(k dx)^2/12':>16}{'ratio':>10}")
    prev = None
    for n in (10, 20, 40, 80):
        dx = 1.0
        kdx = 2.0 * math.pi / (4096.0 / n) * dx
        val = -(2.0 / dx ** 2) * (1.0 - math.cos(kdx))
        cont = -kdx ** 2 / dx ** 2
        ratio = val / cont
        print(f"{kdx:10.6f}{ratio:16.12f}{kdx ** 2 / 12:16.3e}"
              + ("" if prev is None else f"{(1 - ratio) / prev:10.3f}"))
        prev = 1 - ratio
    print("  The discrete operator is *softer* than the continuum: phase velocity")
    print("  c' = (2/(k dx)) sin(k dx/2) c < c, with error (k dx)^2/24, which is")
    print("  the numerical dispersion every finite-difference EM code lives with.")


def part3_yee_dispersion():
    section("3. Yee (FDTD) stagger-grid dispersion and its continuum limit")
    print("  Exact FDTD relation:  sin(omega dt/2)/(c dt) = sin(k dx/2)/dx")
    dx = 0.05
    c = C_LIGHT

    def c_num_over_c(k, cfl):
        dt = cfl * dx / c
        rhs = (c * dt / dx) * math.sin(k * dx / 2.0)
        omega_num = 2.0 * math.asin(rhs) / dt
        return omega_num / (k * c)

    print(f"  (a) fixed 15 points per wavelength, varying the Courant number c dt/dx:")
    k = 2.0 * math.pi / (15.0 * dx)
    for cfl in (1.0, 0.9, 0.5, 0.25):
        print(f"      cfl = {cfl:5.2f}:  c_num/c = {c_num_over_c(k, cfl):.9f}"
              f"   error = {c_num_over_c(k, cfl) - 1: .3e}")
    print("      At cfl = 1 the 1-D FDTD scheme is exact (the 'magic time step'):")
    print("      space and time errors cancel identically. That is a special")
    print("      property of one dimension and does not survive in 2-D or 3-D.")
    print(f"  (b) fixed cfl = 0.5, varying the sampling:")
    print(f"{'points/period':>14}{'k dx':>10}{'c_num/c':>14}{'error':>14}"
          f"{'error/(k dx)^2':>18}")
    prev = None
    for ppw in (60.0, 30.0, 15.0, 8.0):
        kk = 2.0 * math.pi / (ppw * dx)
        err = c_num_over_c(kk, 0.5) - 1.0
        print(f"{ppw:14.0f}{kk * dx:10.5f}{c_num_over_c(kk, 0.5):14.9f}{err:14.3e}"
              f"{abs(err) / (kk * dx) ** 2:18.6f}")
        prev = err
    print("  The error is second order in k dx: halving dx cuts it fourfold. That is")
    print("  the accuracy condition a GPR or EM modeller uses when choosing a grid.")


def part4_diffusion():
    section("4. The same equations in a conductor: diffusion, not propagation")
    rho = 100.0            # ohm m
    sigma = 1.0 / rho
    delta = 10.0           # target skin depth, m
    omega = 2.0 * rho / (MU0 * delta ** 2)
    f = omega / (2.0 * math.pi)
    print(f"  sigma = {sigma:.4f} S/m (rho = {rho:.0f} ohm m)")
    print(f"  choose delta = {delta:.1f} m => omega = 2 rho/(mu0 delta^2) ="
          f" {omega:.6e} rad/s, f = {f:.3e} Hz, T = {1 / f:.3e} s")
    print(f"  analytic delta = sqrt(2/(mu0 sigma omega)) ="
          f" {math.sqrt(2.0 / (MU0 * sigma * omega)):.6f} m")
    diff = 1.0 / (MU0 * sigma)
    dz = 0.5
    nz = 100
    dt = 1.0e-9
    cfl = diff * dt / dz ** 2
    period = 2.0 * math.pi / omega
    steps_per_period = int(round(period / dt))
    total = 20 * steps_per_period
    print(f"  explicit scheme: D = 1/(mu0 sigma) = {diff:.4e} m^2/s, dz = {dz} m,"
          f" dt = {dt:.1e} s, CFL = {cfl:.4f} (stable below 0.5)")
    print(f"  domain {nz * dz:.0f} m = {nz * dz / delta:.0f} skin depths,"
          f" {steps_per_period} steps per period, {total} steps total")

    def analytic(z, t):
        return math.exp(-z / delta) * math.cos(omega * t - z / delta)

    e = [analytic(j * dz, 0.0) for j in range(nz)]   # start on the exact solution
    probes = (0, 20, 40, 60, 80)
    trace = {j: [] for j in probes}
    start = total - steps_per_period
    for n in range(total):
        t = (n + 1) * dt
        new = e[:]
        new[0] = math.cos(omega * t)                 # E(0,t) = cos wt
        for j in range(1, nz - 1):
            new[j] = e[j] + cfl * (e[j + 1] - 2.0 * e[j] + e[j - 1])
        new[nz - 1] = new[nz - 2]
        e = new
        if n + 1 > start:
            for j in probes:
                trace[j].append(e[j])
    t_end = total * dt
    err = max(abs(e[j] - analytic(j * dz, t_end)) for j in range(nz))
    print(f"  after {total} steps (t = {t_end:.4e} s = {total / steps_per_period:.0f}"
          f" periods) the largest departure from the exact solution is {err:.3e} V/m")
    print(f"{'z (m)':>7}{'|E| numeric':>14}{'exp(-z/delta)':>16}{'phase (deg)':>14}"
          f"{'+z/delta (deg)':>16}")
    points = []
    for j in probes:
        z = j * dz
        re = im = 0.0
        for m, val in enumerate(trace[j]):
            ang = omega * (start + m + 1) * dt
            re += val * math.cos(ang)
            im += val * math.sin(ang)
        amp = 2.0 * math.hypot(re, im) / steps_per_period
        phase = math.degrees(math.atan2(im, re))
        print(f"{z:7.2f}{amp:14.6f}{math.exp(-z / delta):16.6f}{phase:14.4f}"
              f"{math.degrees(z / delta):16.4f}")
        if j > 0 and amp > 0.0:
            points.append((z, amp))
    # least-squares slope of log(amplitude) vs z gives -1/delta
    n = len(points)
    sx = sum(p[0] for p in points)
    sy = sum(math.log(p[1]) for p in points)
    sxx = sum(p[0] ** 2 for p in points)
    sxy = sum(p[0] * math.log(p[1]) for p in points)
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    d_meas = -1.0 / slope
    print(f"  least-squares decay length from the numerical solution:"
          f" delta_measured = {d_meas:.6f} m")
    print(f"  relative error vs the analytic formula delta = sqrt(2/(mu0 sigma omega)):"
          f" {abs(d_meas - delta) / delta:.3e}")
    print("  The phase advances as +z/delta radians relative to the source, identical")
    print("  in magnitude to the amplitude exponent: decay and lag are the same number")
    print("  in a diffusive field. That is why the MT impedance is complex and why its")
    print("  phase is 45 degrees over a uniform half-space.")


def part5_regime():
    section("5. Wave or diffusion? The conduction/displacement ratio")
    media = [
        ("sea water", 4.0, 81.0),
        ("wet soil", 0.01, 20.0),
        ("dry granite", 1.0e-3, 6.0),
    ]
    print(f"{'medium':>12}{'sigma (S/m)':>13}{'eps_r':>7}{'f_c (Hz)':>12}"
          f"{'s/(we) @ 1 mHz':>18}{'s/(we) @ 100 MHz':>18}")
    for name, sigma, epsr in media:
        eps = epsr * EPS0
        fc = sigma / (2.0 * math.pi * eps)
        r_mt = sigma / (2.0 * math.pi * 1.0e-3 * eps)
        r_gpr = sigma / (2.0 * math.pi * 1.0e8 * eps)
        print(f"{name:>12}{sigma:13.4g}{epsr:7.0f}{fc:12.4e}{r_mt:18.3e}{r_gpr:18.3e}")
    print("  Below f_c the conduction current wins and the field diffuses; above it")
    print("  the displacement current wins and the field propagates. Magnetotellurics")
    print("  (mHz-Hz) is ten or more orders of magnitude inside the diffusive regime;")
    print("  GPR (10-1000 MHz) is in or above the crossover and is described by waves.")
    print("  Same four equations, opposite limiting behaviour.")


def main():
    part1_maxwell_residuals()
    part2_discrete_dispersion()
    part3_yee_dispersion()
    part4_diffusion()
    part5_regime()


if __name__ == "__main__":
    main()
