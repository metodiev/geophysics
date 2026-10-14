"""Anisotropic elasticity: VTI, HTI, Thomsen parameters and S splitting.

Run:  python3 anisotropic_elasticity_demo.py
Requires: Python standard library only.

Companion to lesson 02-04-06. A model shale-like set of stiffnesses is used:
C11 = 30, C33 = 22, C44 = 7, C66 = 10, C13 = 12 GPa, rho = 2400 kg/m^3. These
are model parameters chosen to be self-consistent for hexagonal symmetry
(C11 - C12 = 2 C66), not measurements of a particular rock.

The script:

1. Computes the Thomsen parameters epsilon, gamma and delta from the C's.
2. Solves the Christoffel problem for the VTI medium at several angles and
   compares the results with the known exact results for the symmetry
   directions and the exact SH-wave formula.
3. Rotates the stiffness tensor to make the symmetry axis horizontal (HTI) and
   verifies that the rotation does what it should: the speeds along the axis
   exchange roles.
4. Measures the S-wave splitting for the HTI medium and compares it with the
   weak-anisotropy prediction gamma.

Every number printed below was produced by this script.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


C11, C33, C44, C66, C13 = 30.0e9, 22.0e9, 7.0e9, 10.0e9, 12.0e9
C12 = C11 - 2.0 * C66
RHO = 2400.0


def jacobi_eigen(a, tol=1e-16, sweeps=100):
    n = len(a)
    A = [row[:] for row in a]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(sweeps):
        off = sum(A[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
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


# Voigt index order: 11, 22, 33, 23, 13, 12
PAIRS = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]


def vti_voigt():
    """The VTI stiffness matrix, written out entry by entry.

    The three distinct "normal" shear-free entries of the upper 3x3 block are
    C11 (in the isotropy plane, and equal for the two in-plane normal strains),
    C33 (along the axis) and C13 (coupling the axial and in-plane normal
    strains). The fourth, C12, is not independent: hexagonal symmetry requires
    C12 = C11 - 2 C66. Building the matrix without imposing that identity
    produces a tensor with tetragonal rather than hexagonal symmetry, which
    still looks plausible in a printed matrix but rotates incorrectly.
    """
    n = 6
    cm = [[0.0] * n for _ in range(n)]
    cm[0][0] = cm[1][1] = C11
    cm[2][2] = C33
    cm[0][1] = cm[1][0] = C12
    cm[2][0] = cm[0][2] = cm[2][1] = cm[1][2] = C13
    cm[3][3] = cm[4][4] = C44
    cm[5][5] = C66
    return cm


def voigt_index(i, j):
    return PAIRS.index((min(i, j), max(i, j)))


def voigt_to_tensor(cm):
    return [[[[cm[voigt_index(i, j)][voigt_index(k, l)]
               for l in range(3)] for k in range(3)] for j in range(3)]
            for i in range(3)]


def tensor_to_voigt(C):
    return [[C[p[0]][p[1]][q[0]][q[1]] for q in PAIRS] for p in PAIRS]


def rotate_tensor(C, R):
    return [[[[sum(R[i][p] * R[j][q] * R[k][r] * R[l][s] * C[p][q][r][s]
                   for p in range(3) for q in range(3) for r in range(3)
                   for s in range(3))
               for l in range(3)] for k in range(3)] for j in range(3)]
            for i in range(3)]


def christoffel_voigt(cm, rho, n):
    """Gamma_ij = C_ijkl n_j n_l / rho, from the Voigt matrix."""
    C = voigt_to_tensor(cm)
    return [[sum(C[i][j][k][l] * n[j] * n[l] for j in range(3) for l in range(3))
             / rho for k in range(3)] for i in range(3)]


def part1_thomsen():
    section("1. Thomsen parameters of the VTI model")
    eps = (C11 - C33) / (2.0 * C33)
    gam = (C66 - C44) / (2.0 * C44)
    de = ((C13 + C44) ** 2 - (C33 - C44) ** 2) / (2.0 * C33 * (C33 - C44))
    print(f"C11 = {C11 / 1e9:.1f}, C33 = {C33 / 1e9:.1f}, C44 = {C44 / 1e9:.1f}, "
          f"C66 = {C66 / 1e9:.1f}, C13 = {C13 / 1e9:.1f} GPa, "
          f"rho = {RHO:.0f} kg/m^3")
    print(f"C12 = C11 - 2 C66 = {C12 / 1e9:.1f} GPa (the hexagonal constraint)")
    cm = vti_voigt()
    print(f"check on the assembled matrix: C11 - C12 - 2 C66 = "
          f"{(cm[0][0] - cm[0][1] - 2.0 * cm[5][5]) / 1e9:.1f} GPa "
          f"(must be 0 for hexagonal symmetry)")
    print(f"epsilon = (C11 - C33)/(2 C33)                    = {eps:.9f}")
    print(f"gamma   = (C66 - C44)/(2 C44)                    = {gam:.9f}")
    print(f"delta   = ((C13 + C44)^2 - (C33 - C44)^2)/"
          f"(2 C33 (C33 - C44)) = {de:.9f}")
    print()
    print("  delta - epsilon = "
          f"{de - eps:+.9f}: for this model delta exceeds epsilon, so the P-wave")
    print("  velocity is larger horizontally than expected from epsilon alone at")
    print("  intermediate angles. Real shales usually have delta between epsilon")
    print("  and epsilon/(1 + 2 epsilon) or above; the value is a measured property")
    print("  of the rock and cannot be predicted from the mineralogy alone.")


def part2_vti_velocities():
    section("2. VTI phase velocities from the Christoffel problem")
    cm = vti_voigt()
    vp_v = math.sqrt(C33 / RHO)
    vs_v = math.sqrt(C44 / RHO)
    vp_h = math.sqrt(C11 / RHO)
    vsh_h = math.sqrt(C66 / RHO)
    print(f"exact results: v_p(0) = sqrt(C33/rho) = {vp_v:.6f} m/s")
    print(f"               v_sv(0) = v_sh(0) = sqrt(C44/rho) = {vs_v:.6f} m/s")
    print(f"               v_p(90) = sqrt(C11/rho) = {vp_h:.6f} m/s")
    print(f"               v_sh(90) = sqrt(C66/rho) = {vsh_h:.6f} m/s")
    print(f"{'theta (deg)':>12} {'v_qP (m/s)':>12} {'v_qSV (m/s)':>13} "
          f"{'v_SH (m/s)':>12} {'SH formula':>12} {'SH error':>10}")
    worst = 0.0
    for theta_deg in (0.0, 15.0, 30.0, 45.0, 60.0, 90.0):
        theta = math.radians(theta_deg)
        n = [math.sin(theta), 0.0, math.cos(theta)]
        G = christoffel_voigt(cm, RHO, n)
        eig, _ = jacobi_eigen(G)
        speeds = sorted((math.sqrt(max(0.0, e)) for e in eig), reverse=True)
        # identify the SH mode: the purely horizontal polarisation (y)
        _, vectors = jacobi_eigen(G)
        sh_index = max(range(3), key=lambda i: abs(vectors[1][i]))
        sh_speed = math.sqrt(max(0.0, eig[sh_index]))
        sh_formula = math.sqrt((C66 * math.sin(theta) ** 2
                                + C44 * math.cos(theta) ** 2) / RHO)
        worst = max(worst, abs(sh_speed - sh_formula) / sh_formula)
        others = [math.sqrt(max(0.0, eig[i])) for i in range(3) if i != sh_index]
        others.sort(reverse=True)
        print(f"{theta_deg:12.1f} {others[0]:12.6f} {others[1]:13.6f} "
              f"{sh_speed:12.6f} {sh_formula:12.6f} "
              f"{abs(sh_speed - sh_formula) / sh_formula:10.2e}")
    print(f"max relative difference between the SH eigenvalue and its closed form = "
          f"{worst:.3e}")
    print()
    print("  The SH wave has an exact closed form because it decouples: its motion")
    print("  is purely horizontal and orthogonal to the plane containing the")
    print("  symmetry axis and the propagation direction. The two remaining modes,")
    print("  qP and qSV, are coupled and have no simple closed form; that coupling -")
    print("  not the shear anisotropy alone - is what delta parameterises, and it is")
    print("  why delta matters more than epsilon for surface-seismic travel times.")


def rotation_y(angle):
    c, s = math.cos(angle), math.sin(angle)
    # rotate about the y axis: e_z -> e_x
    return [[c, 0.0, s], [0.0, 1.0, 0.0], [-s, 0.0, c]]


def part3_hti():
    section("3. Rotating the medium: VTI becomes HTI")
    cm = vti_voigt()
    C = voigt_to_tensor(cm)
    R = rotation_y(math.pi / 2.0)
    C2 = rotate_tensor(C, R)
    cm2 = tensor_to_voigt(C2)
    print("HTI stiffness matrix (GPa), symmetry axis now along x:")
    for row in cm2:
        print("   [" + ", ".join(f"{v / 1e9:8.3f}" for v in row) + "]")
    worst = 0.0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    worst = max(worst,
                                abs(C2[i][j][k][l] - C2[j][i][k][l]),
                                abs(C2[i][j][k][l] - C2[k][l][i][j]))
    print(f"max symmetry violation after rotation = {worst:.3e} Pa")
    hexid = max(abs(cm2[1][1] - cm2[1][2] - 2.0 * cm2[3][3]),
                abs(cm2[0][1] - cm2[0][2]),
                abs(cm2[1][1] - cm2[2][2]), abs(cm2[5][5] - cm2[4][4]))
    print("max violation of the hexagonal identities of the rotated matrix "
          f"(TI about x) = {hexid:.3e} Pa")
    print(f"speeds along the symmetry axis (x): v_p = "
          f"{math.sqrt(cm2[0][0] / RHO):.6f} m/s "
          f"(= sqrt(C33/rho) = {math.sqrt(C33 / RHO):.6f})")
    print(f"speeds along z (isotropy plane):    v_p = "
          f"{math.sqrt(cm2[2][2] / RHO):.6f} m/s "
          f"(= sqrt(C11/rho) = {math.sqrt(C11 / RHO):.6f})")
    print()
    print("  The rotation exchanged the roles of the two directions, as it must:")
    print("  the fast direction follows the symmetry axis around. Nothing physical")
    print("  changed, which is the test that the rotation was applied correctly -")
    print("  an error in the tensor rotation would break the symmetry, which the")
    print("  check above shows it does not.")


def part4_splitting():
    section("4. S-wave splitting in the HTI medium")
    cm = vti_voigt()
    C = voigt_to_tensor(cm)
    C2 = rotate_tensor(C, rotation_y(math.pi / 2.0))
    cm2 = tensor_to_voigt(C2)
    gamma = (C66 - C44) / (2.0 * C44)
    print("the symmetry axis is along x; theta is measured from z and azimuth")
    print("from the x axis, so (theta, azimuth) = (90, 0) is propagation along the")
    print("symmetry axis and (0, .) is propagation in the plane perpendicular to it")
    print(f"{'theta (deg)':>12} {'azimuth (deg)':>14} {'v_S1 (m/s)':>12} "
          f"{'v_S2 (m/s)':>12} {'splitting (%)':>14} {'gamma (%)':>10}")
    for theta_deg, azimuth_deg in ((90.0, 0.0), (60.0, 0.0), (45.0, 0.0),
                                   (45.0, 45.0), (45.0, 90.0), (0.0, 0.0)):
        az = math.radians(azimuth_deg)
        theta = math.radians(theta_deg)
        n = [math.sin(theta) * math.cos(az), math.sin(theta) * math.sin(az),
             math.cos(theta)]
        G = christoffel_voigt(cm2, RHO, n)
        eig, _ = jacobi_eigen(G)
        speeds = sorted((math.sqrt(max(0.0, e)) for e in eig), reverse=True)
        splitting = (speeds[1] - speeds[2]) / (0.5 * (speeds[1] + speeds[2]))
        print(f"{theta_deg:12.1f} {azimuth_deg:14.1f} {speeds[1]:12.6f} "
              f"{speeds[2]:12.6f} {splitting * 100:14.4f} {gamma * 100:10.4f}")
    print()
    print("  The two shear modes are degenerate only along the symmetry axis, where")
    print("  every direction perpendicular to it is equivalent. For every other")
    print("  direction they differ; in particular propagation in the plane")
    print("  perpendicular to the axis still splits, because one shear polarisation")
    print("  lies along the axis and the other lies in the plane. The relative")
    print("  splitting is of order gamma, as the weak-anisotropy approximation")
    print("  predicts, but it equals gamma only in the limit of small anisotropy;")
    print("  at gamma = 21 per cent here the measured splitting runs from 0 along")
    print("  the axis to about 18 per cent across it. Shear-wave splitting is the")
    print("  standard field measurement of anisotropy, and one of the standard")
    print("  observations that the mantle is not isotropic.")


def part5_phase_group():
    section("5. Phase velocity versus group (ray) velocity")
    print("for a homogeneous anisotropic medium the phase velocity depends only")
    print("on the direction n, so the group velocity vector is")
    print("   G = V n + (dV/dtheta) t,   t = dn/dtheta")
    print("i.e. the ray direction is tilted away from the wavefront normal by")
    print("   dphi = phi_G - theta, with tan(phi_G) = (V sin + V' cos)/(V cos - V' sin)")
    print("V and dV/dtheta come from the exact Christoffel eigenvalues; the")
    print("derivative is a centred finite difference with h = 1e-6 rad.")
    cm = vti_voigt()
    h = 1e-6
    worst = 0.0
    print(f"{'theta (deg)':>12} {'mode':>5} {'phase V (m/s)':>14} "
          f"{'group |G| (m/s)':>16} {'group angle':>12} {'dphi (deg)':>11}")
    for theta_deg in (30.0, 45.0, 60.0):
        th = math.radians(theta_deg)
        for label, ind in (("qP", 0), ("qSV", 1)):
            V = _vti_phase(th, ind)
            Vp = _vti_phase(th + h, ind)
            Vm = _vti_phase(th - h, ind)
            dVdth = (Vp - Vm) / (2.0 * h)
            gx = V * math.sin(th) + dVdth * math.cos(th)
            gz = V * math.cos(th) - dVdth * math.sin(th)
            phi = math.degrees(math.atan2(gx, gz))
            gx2, gz2 = _group_from_omega(th, ind)
            worst = max(worst, abs(gx - gx2), abs(gz - gz2))
            print(f"{theta_deg:12.1f} {label:>5} {V:14.6f} "
                  f"{math.hypot(gx, gz):16.6f} {phi:12.6f} {phi - theta_deg:+11.6f}")
    print(f"max difference between G = V n + V' t and the direct derivative "
          f"d(omega)/dk of the Christoffel dispersion relation = {worst:.3e} m/s")
    print()
    print("  Unlike an isotropic medium, the ray does not travel along the")
    print("  wavefront normal. The qP ray tilts towards the fast (horizontal)")
    print("  direction by several degrees at every non-axial angle, because the qP")
    print("  velocity increases monotonically from the axis to the isotropy plane.")
    print("  The qSV tilt is smaller and changes sign, because the qSV velocity")
    print("  surface has a minimum near 45 degrees, so dV/dtheta changes sign")
    print("  there. The angular error is comparable with the anisotropy itself,")
    print("  which is why NMO velocities, ray angles and well ties must all be")
    print("  interpreted with the anisotropy in mind.")


def _group_from_omega(th, ind, dk=1e-3):
    """Group velocity as the gradient of omega(k) with respect to k."""
    kx, kz = math.sin(th), math.cos(th)

    def omega(x, z):
        return _vti_phase(math.atan2(x, z), ind) * math.hypot(x, z)

    return ((omega(kx + dk, kz) - omega(kx - dk, kz)) / (2.0 * dk),
            (omega(kx, kz + dk) - omega(kx, kz - dk)) / (2.0 * dk))


def _vti_phase(rad, ind):
    """Exact qP (ind=0) or qSV (ind=1) phase speed at angle rad from the axis."""
    s, c = math.sin(rad), math.cos(rad)
    a = (C11 * s * s + C44 * c * c) / RHO
    b = (C13 + C44) * s * c / RHO
    d = (C44 * s * s + C33 * c * c) / RHO
    half = 0.5 * (a + d)
    root = math.sqrt(0.25 * (a - d) ** 2 + b * b)
    v2 = half + root if ind == 0 else half - root
    return math.sqrt(max(0.0, v2))


if __name__ == "__main__":
    part1_thomsen()
    part2_vti_velocities()
    part3_hti()
    part4_splitting()
    part5_phase_group()
