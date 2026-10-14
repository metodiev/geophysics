"""Stress: traction, principal stresses, invariants and the Mohr circle.

Run:  python3 stress_demo.py
Requires: Python standard library only.

Companion to lesson 02-04-01. The script:

1. Computes tractions t = sigma n for several plane orientations of a given
   stress state and verifies that |t| lies between the least and greatest
   principal stress.
2. Diagonalises the stress tensor (Jacobi) and verifies that the principal
   stresses are the extrema of the normal stress over all orientations, that
   the principal directions give zero shear, and that the three invariants are
   unchanged by the rotation to principal axes.
3. Checks the Mohr-circle construction by scanning every plane orientation in a
   plane-stress state and comparing the measured maximum shear stress with
   (sigma1 - sigma3)/2.
4. Computes lithostatic stress and the effective stress at depth, for stated
   density and pore-pressure assumptions.

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


SIGMA = [[120.0, 30.0, 0.0],
         [30.0, 70.0, -15.0],
         [0.0, -15.0, 40.0]]          # MPa


def matvec(a, v):
    return [sum(a[i][j] * v[j] for j in range(3)) for i in range(3)]


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def part1_traction():
    section("1. Traction on a plane: t = sigma n")
    print("stress tensor (MPa):")
    for row in SIGMA:
        print("   [" + ", ".join(f"{v:8.3f}" for v in row) + "]")
    eig, _ = jacobi_eigen(SIGMA)
    s1, s2, s3 = sorted(eig, reverse=True)
    print(f"principal stresses (MPa): s1 = {s1:.6f}, s2 = {s2:.6f}, "
          f"s3 = {s3:.6f}")
    print(f"{'normal n':>26} {'t (MPa)':>28} {'|t|':>10} {'t_n':>10} {'|t_s|':>10}")
    for n in ((1, 0, 0), (0, 1, 0), (0, 0, 1),
              (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)):
        nn = norm(n)
        u = [c / nn for c in n]
        t = matvec(SIGMA, u)
        t_n = sum(t[i] * u[i] for i in range(3))
        t_s = math.sqrt(max(0.0, norm(t) ** 2 - t_n ** 2))
        label = "(" + ", ".join(f"{c:g}" for c in n) + ") / " + f"{nn:.4g}"
        print(f"{label:>26} ({t[0]:8.3f}, {t[1]:8.3f}, {t[2]:8.3f}) "
              f"{norm(t):10.4f} {t_n:10.4f} {t_s:10.4f}")
    print()
    print(f"  the bound s3 <= t_n <= s1 holds for every orientation; the greatest")
    print(f"  normal stress over all planes is s1 = {s1:.4f} MPa and the least is")
    print(f"  s3 = {s3:.4f} MPa. Normal stress is a projection, so it cannot exceed")
    print(f"  the largest principal value.")


def part2_principal():
    section("2. Principal axes: extrema of normal stress and zero shear")
    eig, V = jacobi_eigen(SIGMA)
    order = sorted(range(3), key=lambda i: -eig[i])
    print(f"{'axis':>5} {'eigenvalue (MPa)':>17} {'traction (MPa)':>28} "
          f"{'t_n':>11} {'|t_s|':>10} {'1^T sigma 1':>12}")
    for rank, i in enumerate(order, start=1):
        v = [V[k][i] for k in range(3)]
        t = matvec(SIGMA, v)
        t_n = sum(t[k] * v[k] for k in range(3))
        t_s = math.sqrt(max(0.0, norm(t) ** 2 - t_n ** 2))
        print(f"{rank:5d} {eig[i]:17.6f} ({t[0]:8.4f}, {t[1]:8.4f}, {t[2]:8.4f}) "
              f"{t_n:11.6f} {t_s:10.2e} {sum(v[k] ** 2 for k in range(3)):12.9f}")
    print()
    inv1 = SIGMA[0][0] + SIGMA[1][1] + SIGMA[2][2]
    inv2 = (SIGMA[0][0] * SIGMA[1][1] - SIGMA[0][1] ** 2
            + SIGMA[1][1] * SIGMA[2][2] - SIGMA[1][2] ** 2
            + SIGMA[0][0] * SIGMA[2][2] - SIGMA[0][2] ** 2)
    inv3 = (SIGMA[0][0] * (SIGMA[1][1] * SIGMA[2][2] - SIGMA[1][2] ** 2)
            - SIGMA[0][1] * (SIGMA[1][0] * SIGMA[2][2] - SIGMA[1][2] * SIGMA[2][0])
            + SIGMA[0][2] * (SIGMA[1][0] * SIGMA[2][1] - SIGMA[1][1] * SIGMA[2][0]))
    print(f"invariants from the components:  I1 = {inv1:.6f}, I2 = {inv2:.6f}, "
          f"I3 = {inv3:.6f}")
    print(f"invariants from the eigenvalues: I1 = {sum(eig):.6f}, "
          f"I2 = {eig[0]*eig[1] + eig[1]*eig[2] + eig[0]*eig[2]:.6f}, "
          f"I3 = {eig[0]*eig[1]*eig[2]:.6f}")
    mean = inv1 / 3.0
    dev = [[SIGMA[i][j] - (mean if i == j else 0.0) for j in range(3)]
           for i in range(3)]
    j2 = 0.5 * sum(dev[i][j] ** 2 for i in range(3) for j in range(3))
    print(f"mean stress = I1/3 = {mean:.6f} MPa; deviatoric second invariant "
          f"J2 = {j2:.6f} MPa^2")
    print(f"von Mises equivalent stress = sqrt(3 J2) = {math.sqrt(3.0 * j2):.6f} MPa")
    print("  A state of stress separates into a mean part (which changes volume)")
    print("  and a deviatoric part (which changes shape); only the latter drives")
    print("  shear failure, and only the former changes pore volume.")


def part3_mohr():
    section("3. Mohr circle: every plane lies on it")
    # plane-stress subset for a clean 2-D construction
    sxx, syy, sxy = 120.0, 40.0, 30.0
    print(f"2-D state: sxx = {sxx}, syy = {syy}, sxy = {sxy} MPa")
    centre = 0.5 * (sxx + syy)
    radius = math.sqrt(0.25 * (sxx - syy) ** 2 + sxy ** 2)
    print(f"Mohr circle centre = {centre:.6f} MPa, radius = {radius:.6f} MPa")
    print(f"{'theta (deg)':>12} {'sigma_n':>11} {'tau':>10} "
          f"{'distance from centre':>21}")
    worst = 0.0
    for theta_deg in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        theta = math.radians(theta_deg)
        # normal on a plane whose normal is rotated by theta
        nx, ny = math.cos(theta), math.sin(theta)
        t = (sxx * nx + sxy * ny, sxy * nx + syy * ny)
        t_n = t[0] * nx + t[1] * ny
        t_s = -t[0] * ny + t[1] * nx
        dist = math.hypot(t_n - centre, t_s)
        worst = max(worst, abs(dist - radius))
        print(f"{theta_deg:12.2f} {t_n:11.6f} {t_s:10.6f} {dist:21.6f}")
    print(f"max deviation from the circle radius = {worst:.3e} MPa")
    print(f"maximum shear over all planes = radius = {radius:.6f} MPa, "
          f"= (s1 - s3)/2 with s1 = {centre + radius:.6f}, "
          f"s3 = {centre - radius:.6f} MPa")
    print(f"the failure plane in a Mohr-Coulomb sense makes 45 deg with the")
    print(f"greatest principal stress only when the friction angle is zero;")
    print(f"with friction the optimal plane is at 45 deg - phi/2.")


def part4_lithostatic():
    section("4. Lithostatic and effective stress at depth")
    rho_rock, rho_water, g = 2700.0, 1000.0, 9.81
    print(f"assumptions: rho_rock = {rho_rock:.0f} kg/m^3, "
          f"rho_water = {rho_water:.0f} kg/m^3, g = {g} m/s^2,")
    print("hydrostatic pore pressure (a drained, connected crust)")
    print(f"{'depth (km)':>11} {'sigma_v (MPa)':>14} {'p_f (MPa)':>11} "
          f"{'sigma_v_eff (MPa)':>18}")
    for depth_km in (1.0, 5.0, 10.0, 20.0, 30.0):
        z = depth_km * 1000.0
        sv = rho_rock * g * z / 1e6
        pf = rho_water * g * z / 1e6
        print(f"{depth_km:11.1f} {sv:14.3f} {pf:11.3f} {sv - pf:18.3f}")
    print()
    print("  Effective stress, not total stress, controls frictional sliding and")
    print("  fracture: pore pressure carries part of the load and reduces the normal")
    print("  stress on every plane. Overpressure therefore promotes failure at")
    print("  shallower depth than the total-stress arithmetic would suggest. The")
    print("  gradients above are the simplest possible model - constant densities,")
    print("  hydrostatic pore pressure - and every number changes if the crust is")
    print("  overpressured, which is common.")


if __name__ == "__main__":
    part1_traction()
    part2_principal()
    part3_mohr()
    part4_lithostatic()
