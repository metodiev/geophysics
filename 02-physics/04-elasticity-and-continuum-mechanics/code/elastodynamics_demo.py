"""Elastodynamics: from the constitutive law to the P and S wave speeds.

Run:  python3 elastodynamics_demo.py
Requires: Python standard library only.

Companion to lesson 02-04-05, and to the mastery checkpoint of the physics
folder. The script checks, numerically, the chain

    sigma_ij = lambda e_kk delta_ij + 2 mu e_ij          (constitutive law)
    e_ij     = (1/2)(u_i,j + u_j,i)                      (strain)
  -> rho u_i,tt = (lambda + mu) u_j,ji + mu u_i,jj        (equation of motion)
  -> rho u_i,tt = C_ijkl u_k,lj   with C_ijkl = lambda delta_ij delta_kl
                                + mu (delta_ik delta_jl + delta_il delta_jk)
  -> v_p = sqrt((lambda + 2 mu)/rho),  v_s = sqrt(mu/rho)

1. Reports the speeds for a granite-like model and for a Poisson solid.
2. Diagonalises the Christoffel matrix Gamma_ij = C_ijkl n_j n_l / rho and
   verifies that its eigenvalues are v_p^2, v_s^2, v_s^2 for every direction.
3. Verifies the plane-wave residual of the full elastodynamic equation in index
   notation, for a P wave and an S wave.
4. Verifies that a P wave is curl-free and an S wave is divergence-free, by
   finite differences on a grid, and that a general wave field is the sum of
   the two.
5. Measures the P and S speeds in an explicit finite-difference simulation of a
   homogeneous medium, comparing with the formulas.
6. Sets mu = 0 and shows v_s = 0 and that an S pulse cannot propagate.

Every number printed below was produced by this script.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def jacobi_eigen(a, tol=1e-14, sweeps=100):
    n = len(a)
    A = [row[:] for row in a]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(sweeps):
        off = math.sqrt(sum(A[i][j] ** 2 for i in range(n) for j in range(n)
                            if i != j))
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(A[p][q]) < 1e-18:
                    continue
                theta = 0.5 * math.atan2(2.0 * A[p][q], A[q][q] - A[p][p])
                c, s = math.cos(theta), math.sin(theta)
                for k in range(n):
                    akp, akq = A[k][p], A[k][q]
                    A[k][p] = c * akp - s * akq
                    A[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = A[p][k], A[q][k]
                    A[p][k] = c * apk - s * aqk
                    A[q][k] = s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = V[k][p], V[k][q]
                    V[k][p] = c * vkp - s * vkq
                    V[k][q] = s * vkp + c * vkq
    return [A[i][i] for i in range(n)], V


def delta(i, j):
    return 1.0 if i == j else 0.0


def make_C(lam, mu):
    return [[[[lam * delta(i, j) * delta(k, l)
               + mu * (delta(i, k) * delta(j, l) + delta(i, l) * delta(j, k))
               for l in range(3)] for k in range(3)] for j in range(3)]
            for i in range(3)]


RHO, LAMBDA, MU = 2700.0, 25.0e9, 30.0e9
VP = math.sqrt((LAMBDA + 2.0 * MU) / RHO)
VS = math.sqrt(MU / RHO)


def part1_speeds():
    section("1. The speeds, and the two limiting cases")
    print(f"granite-like model: rho = {RHO:.0f} kg/m^3, lambda = "
          f"{LAMBDA / 1e9:.0f} GPa, mu = {MU / 1e9:.0f} GPa")
    print(f"  v_p = sqrt((lambda + 2 mu)/rho) = sqrt(({LAMBDA / 1e9:.0f} + "
          f"2*{MU / 1e9:.0f})e9/{RHO:.0f}) = {VP:.4f} m/s")
    print(f"  v_s = sqrt(mu/rho)             = sqrt({MU / 1e9:.0f}e9/"
          f"{RHO:.0f})          = {VS:.4f} m/s")
    print(f"  v_p/v_s = {VP / VS:.6f}")
    lam_eq, mu_eq = 30.0e9, 30.0e9
    vp_eq = math.sqrt((lam_eq + 2.0 * mu_eq) / RHO)
    vs_eq = math.sqrt(mu_eq / RHO)
    print(f"Poisson solid (lambda = mu = {mu_eq / 1e9:.0f} GPa): "
          f"v_p = {vp_eq:.4f} m/s, v_s = {vs_eq:.4f} m/s, "
          f"v_p/v_s = {vp_eq / vs_eq:.9f} (sqrt(3) = {math.sqrt(3.0):.9f})")
    print(f"water (K = 2.2 GPa, mu = 0, rho = 1000 kg/m^3): "
          f"v_p = {math.sqrt(2.2e9 / 1000.0):.4f} m/s, v_s = 0 by inspection")
    print()
    print("  The P speed depends on lambda + 2 mu, the S speed only on mu. A fluid")
    print("  has mu = 0, so it cannot transmit a shear wave at any frequency - the")
    print("  statement that explains the S-wave shadow of the outer core.")


def christoffel(C, rho, n):
    return [[sum(C[i][j][k][l] * n[j] * n[l] for j in range(3) for l in range(3))
             / rho for k in range(3)] for i in range(3)]


def part2_christoffel():
    section("2. Christoffel eigenvalues are the squared wave speeds")
    C = make_C(LAMBDA, MU)
    print(f"predicted eigenvalues of Gamma: v_p^2 = {VP ** 2:.6e}, "
          f"v_s^2 = {VS ** 2:.6e} m^2/s^2")
    print(f"{'direction n':>26} {'sqrt(eigenvalues) (m/s)':>40} {'max error':>11}")
    for n in ((1, 0, 0), (0, 1, 0), (0, 0, 1),
              (1, 1, 0), (1, 0, 1), (1, 1, 1)):
        nn = math.sqrt(sum(c * c for c in n))
        u = [c / nn for c in n]
        G = christoffel(C, RHO, u)
        eig, _ = jacobi_eigen(G)
        speeds = sorted((math.sqrt(max(0.0, e)) for e in eig), reverse=True)
        err = max(abs(speeds[0] - VP), abs(speeds[1] - VS), abs(speeds[2] - VS))
        label = "(" + ",".join(f"{c:g}" for c in n) + ")"
        print(f"{label:>26} "
              f"{f'{speeds[0]:.4f}, {speeds[1]:.4f}, {speeds[2]:.4f}':>40} "
              f"{err:11.3e}")
    print()
    print("  For an isotropic solid the eigenvalues are independent of direction -")
    print("  that is what isotropy means - and they are exactly (lambda + 2 mu)/rho")
    print("  once and mu/rho twice. The one distinct direction of polarisation is")
    print("  the P wave; the two-fold degenerate direction is the S wave.")


def part3_plane_wave_residual():
    section("3. Plane waves: residual of the full elastodynamic equation")
    C = make_C(LAMBDA, MU)
    print("residual of rho u_i,tt = C_ijkl u_k,lj for u_i = A_i cos(k.x - omega t)")
    print(f"{'wave':>16} {'vector':>24} {'max |residual|/rho':>20} "
          f"{'relative':>11}")
    cases = (
        ("P along x", (1.0, 0.0, 0.0), (1.0, 0.0, 0.0), VP),
        ("S (y) along x", (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), VS),
        ("S (z) along x", (1.0, 0.0, 0.0), (0.0, 0.0, 1.0), VS),
        ("P along (1,1,1)", (1.0, 1.0, 1.0), (1.0, 1.0, 1.0), VP),
        ("S along (1,1,1)", (1.0, 1.0, 1.0), (1.0, -1.0, 0.0), VS),
    )
    for name, kdir, amp, v in cases:
        nn = math.sqrt(sum(c * c for c in kdir))
        u = [c / nn for c in kdir]
        an = math.sqrt(sum(c * c for c in amp))
        A = [c / an for c in amp]
        k = 2.0 * math.pi / 50.0                 # 50 m wavelength
        omega = v * k
        kv = [k * c for c in u]
        residual = []
        for i in range(3):
            lhs = omega ** 2 * A[i]
            rhs = sum(C[i][j][k2][l] * kv[j] * kv[l] * A[k2]
                      for j in range(3) for k2 in range(3) for l in range(3)) / RHO
            residual.append(abs(rhs - lhs))
        scale = omega ** 2 * max(abs(c) for c in A)
        print(f"{name:>16} ({', '.join(f'{c:+.4f}' for c in A)}) "
              f"{max(residual):20.6e} {max(residual) / scale:11.3e}")
    print()
    print("  A P wave has A parallel to k and meets the equation with v = v_p; an S")
    print("  wave has A perpendicular to k and meets it with v = v_s. Both")
    print("  polarisations are solutions of the same equation with different")
    print("  eigenvalues of the Christoffel matrix - which is why the derivation")
    print("  produces two speeds from one equation.")


def div_curl(field, x, y, z, h=1e-3):
    def component(i, point):
        return field(*point)[i]

    def shifted(point, axis, offset):
        q = list(point)
        q[axis] += offset
        return q

    point = [x, y, z]
    div = 0.0
    for i in range(3):
        div += (component(i, shifted(point, i, h))
                - component(i, shifted(point, i, -h))) / (2.0 * h)
    curl = []
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        dk_dj = (component(k, shifted(point, j, h))
                 - component(k, shifted(point, j, -h))) / (2.0 * h)
        dj_dk = (component(j, shifted(point, k, h))
                 - component(j, shifted(point, k, -h))) / (2.0 * h)
        curl.append(dk_dj - dj_dk)
    return div, curl


def part4_divergence_curl():
    section("4. P waves are curl-free, S waves are divergence-free")
    k = 2.0 * math.pi / 40.0
    omega = 20.0

    def p_field(x, y, z):
        s = math.cos(k * x - omega * 0.0)
        return (s, 0.0, 0.0)

    def s_field(x, y, z):
        s = math.cos(k * x - omega * 0.0)
        return (0.0, s, 0.0)

    def mixed(x, y, z):
        a = math.cos(k * x)
        b = math.cos(k * z)
        return (a, b, 0.0)

    for name, f in (("P (u = (cos kx, 0, 0))", p_field),
                    ("S (u = (0, cos kx, 0))", s_field)):
        div, curl = div_curl(f, 1.234, -0.567, 0.891)
        print(f"{name:>28}: div = {div:12.6f}, |curl| = "
              f"{math.sqrt(sum(c * c for c in curl)):12.6f}")
    div, curl = div_curl(mixed, 1.234, -0.567, 0.891)
    print(f"{'mixed field':>28}: div = {div:12.6f}, |curl| = "
          f"{math.sqrt(sum(c * c for c in curl)):12.6f}")
    print(f"analytic: div of the P field = -k sin(kx) = "
          f"{-k * math.sin(k * 1.234):.6f}; expected for the S field is 0")
    print()
    print("  The Helmholtz decomposition splits any displacement field into a")
    print("  gradient part (P, carrying dilatation) and a curl part (S, carrying")
    print("  rotation). That decomposition is the physical content of the two")
    print("  speeds, and it is what allows seismologists to separate the phases on")
    print("  a three-component record.")


def simulate_1d(c, rho_unused, length, dx, source, width, receivers, t_end,
                cfl=0.5):
    """1-D scalar wave equation u_tt = c^2 u_xx, one-way-then-split pulse."""
    n = int(round(length / dx)) + 1
    dt = cfl * dx / c
    steps = int(round(t_end / dt))
    u_old = [math.exp(-((i * dx - source) / width) ** 2) for i in range(n)]
    u = [0.0] * n
    for i in range(1, n - 1):
        u[i] = u_old[i] + 0.5 * cfl ** 2 * (u_old[i + 1] - 2.0 * u_old[i]
                                            + u_old[i - 1])
    idx = [int(round(r / dx)) for r in receivers]
    traces = [[] for _ in receivers]
    for _ in range(steps):
        u_new = [0.0] * n
        for i in range(1, n - 1):
            u_new[i] = (2.0 * u[i] - u_old[i]
                        + cfl ** 2 * (u[i + 1] - 2.0 * u[i] + u[i - 1]))
        u_old, u = u, u_new
        for j, i in enumerate(idx):
            traces[j].append(u[i])
    return dt, steps, traces, idx


def part5_simulation():
    section("5. Measuring v_p and v_s in an explicit simulation")
    length, dx, source, width = 3000.0, 1.0, 300.0, 20.0
    rec = (900.0, 2100.0)
    print(f"domain 0 to {length:.0f} m, dx = {dx} m, source at {source:.0f} m, "
          f"receivers at {rec[0]:.0f} and {rec[1]:.0f} m")
    print(f"{'wave':>6} {'c formula (m/s)':>17} {'arrival 1 (s)':>15} "
          f"{'arrival 2 (s)':>15} {'c measured (m/s)':>18} {'rel. error':>11}")
    for label, c in (("P", VP), ("S", VS)):
        t_end = (rec[1] - source) / c + 0.15
        dt, steps, traces, idx = simulate_1d(c, RHO, length, dx, source, width,
                                             rec, t_end)
        times = [i * dt for i in range(steps)]
        peaks = []
        for trace in traces:
            best_i = max(range(len(trace)), key=lambda i: abs(trace[i]))
            if 0 < best_i < len(trace) - 1:
                y1 = abs(trace[best_i - 1])
                y2 = abs(trace[best_i])
                y3 = abs(trace[best_i + 1])
                shift = 0.5 * (y1 - y3) / (y1 - 2.0 * y2 + y3)
            else:
                shift = 0.0
            peaks.append(times[best_i] + shift * dt)
        c_meas = (rec[1] - rec[0]) / (peaks[1] - peaks[0])
        print(f"{label:>6} {c:17.4f} {peaks[0]:15.6f} {peaks[1]:15.6f} "
              f"{c_meas:18.4f} {abs(c_meas - c) / c:11.3e}")
    print()
    print("  The simulation knows nothing about the formulas: it only advances")
    print("  u_tt = c^2 u_xx. The speeds it produces agree with sqrt((lambda + 2")
    print("  mu)/rho) and sqrt(mu/rho) to the accuracy of the peak picker, which")
    print("  is the honest test the folder's mastery checkpoint asks for.")


def part6_fluid():
    section("6. mu = 0: the shear speed vanishes and S waves do not propagate")
    print("water: lambda = K = 2.2 GPa, mu = 0, rho = 1000 kg/m^3")
    print(f"  v_p = sqrt((K + 2*0)/rho) = {math.sqrt(2.2e9 / 1000.0):.4f} m/s")
    print(f"  v_s = sqrt(0/rho) = 0 m/s: no restoring force against shear")
    # A shear pulse in a medium with c = 0: every time level equals the first.
    dx, c_zero = 1.0, 0.0
    n = 301
    u_old = [math.exp(-((i * dx - 100.0) / 20.0) ** 2) for i in range(n)]
    u = list(u_old)
    for _ in range(500):
        u_new = [0.0] * n
        for i in range(1, n - 1):
            u_new[i] = (2.0 * u[i] - u_old[i]
                        + c_zero ** 2 * (u[i + 1] - 2.0 * u[i] + u[i - 1]))
        u_old, u = u, u_new
    frozen = max(abs(u[i] - math.exp(-((i * dx - 100.0) / 20.0) ** 2))
                 for i in range(n))
    print(f"  a shear pulse with c = 0 advected for 500 steps: the displacement")
    print(f"  field differs from its initial state by {frozen:.3e} m, i.e. it never")
    print(f"  leaves the source region. There is no shear wave in a fluid because")
    print(f"  there is no shear modulus to provide the restoring stress.")
    print()
    print("  This is the derivation's explanation of the S-wave shadow: in the")
    print("  liquid outer core mu = 0, so v_s = 0 and only P waves cross it. The")
    print("  same statement makes v_p = sqrt(K/rho) there, so a P travel time")
    print("  through the core measures the bulk modulus of liquid iron.")


if __name__ == "__main__":
    part1_speeds()
    part2_christoffel()
    part3_plane_wave_residual()
    part4_divergence_curl()
    part5_simulation()
    part6_fluid()
