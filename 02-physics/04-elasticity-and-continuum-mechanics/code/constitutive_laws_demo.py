"""Constitutive laws: the generalised Hooke law, checked from the inside.

Run:  python3 constitutive_laws_demo.py
Requires: Python standard library only.

Companion to lesson 02-04-03. The script:

1. Builds the fourth-rank stiffness tensor of an isotropic solid,
   C_ijkl = lambda delta_ij delta_kl + mu (delta_ik delta_jl + delta_il delta_jk),
   and verifies the minor and major symmetries that reduce 81 components to 21
   independent ones.
2. Contracts it with a strain tensor and verifies sigma = lambda tr(eps) I +
   2 mu eps component by component.
3. Flattens C into the 6x6 Voigt matrix, verifies that the strain-energy density
   is positive for every strain tested, and recovers the strain from the stress
   with the inverse matrix.
4. Shows that an isotropic tensor is fully determined by two constants, by
   rebuilding C from those two numbers and comparing every element.

Every number printed below was produced by this script.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


LAMBDA, MU = 25.0e9, 30.0e9           # Pa


def delta(i, j):
    return 1.0 if i == j else 0.0


def C(i, j, k, l):
    return LAMBDA * delta(i, j) * delta(k, l) + MU * (delta(i, k) * delta(j, l)
                                                      + delta(i, l) * delta(j, k))


def part1_symmetry():
    section("1. Symmetries of the stiffness tensor")
    minor = 0.0
    major = 0.0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    minor = max(minor, abs(C(i, j, k, l) - C(j, i, k, l)),
                                abs(C(i, j, k, l) - C(i, j, l, k)))
                    major = max(major, abs(C(i, j, k, l) - C(k, l, i, j)))
    print(f"max |C_ijkl - C_jikl| or |C_ijkl - C_ijlk| (minor symmetry) = "
          f"{minor:.3e} Pa")
    print(f"max |C_ijkl - C_klij| (major symmetry)                        = "
          f"{major:.3e} Pa")
    print()
    print("  Minor symmetry says the stress and strain tensors are symmetric, so a")
    print("  symmetric part of C can never be observed; that takes 81 components to")
    print("  36. Major symmetry follows from the existence of a strain-energy")
    print("  function and takes 36 to 21, which is the maximum number of independent")
    print("  elastic constants any linear elastic material can have.")


def part2_contraction():
    section("2. Stress from strain, component by component")
    eps = [[1.0e-3, -4.0e-4, 2.0e-4],
           [-4.0e-4, 3.0e-3, 1.0e-4],
           [2.0e-4, 1.0e-4, -2.0e-3]]
    trace = sum(eps[i][i] for i in range(3))
    print("strain tensor (dimensionless):")
    for row in eps:
        print("   [" + ", ".join(f"{v:12.6e}" for v in row) + "]")
    print(f"trace = {trace:.6e}")
    print(f"{'i j':>5} {'sigma from C_ijkl':>20} "
          f"{'lambda tr(e) delta_ij + 2 mu e_ij':>34} {'difference':>12}")
    worst = 0.0
    for i in range(3):
        for j in range(3):
            sigma_full = sum(C(i, j, k, l) * eps[k][l]
                             for k in range(3) for l in range(3))
            sigma_closed = LAMBDA * trace * delta(i, j) + 2.0 * MU * eps[i][j]
            worst = max(worst, abs(sigma_full - sigma_closed))
            print(f"{i}{j:>4} {sigma_full:20.6e} {sigma_closed:28.6e} "
                  f"{abs(sigma_full - sigma_closed):12.3e}")
    print(f"max difference = {worst:.3e} Pa")
    print()
    print("  The general constitutive law collapses to two terms for an isotropic")
    print("  material: one proportional to the mean strain (volume change) and one")
    print("  proportional to the deviatoric strain (shape change). Every isotropic")
    print("  elastic constant you have met is a combination of lambda and mu.")


def voigt_matrix():
    """6x6 matrix with Voigt index pairs (11, 22, 33, 23, 13, 12)."""
    pairs = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
    return [[C(p[0], p[1], q[0], q[1]) for q in pairs] for p in pairs]


def part3_voigt_and_energy():
    section("3. Voigt matrix, strain energy and inversion")
    cm = voigt_matrix()
    print("Voigt stiffness matrix (GPa), index order 11, 22, 33, 23, 13, 12:")
    for row in cm:
        print("   [" + ", ".join(f"{v / 1e9:8.3f}" for v in row) + "]")
    eps = [[1.0e-3, -4.0e-4, 2.0e-4],
           [-4.0e-4, 3.0e-3, 1.0e-4],
           [2.0e-4, 1.0e-4, -2.0e-3]]
    sigma = [[sum(C(i, j, k, l) * eps[k][l] for k in range(3) for l in range(3))
              for j in range(3)] for i in range(3)]
    energy_tensor = 0.5 * sum(sigma[i][j] * eps[i][j] for i in range(3)
                              for j in range(3))
    tr_e = sum(eps[i][i] for i in range(3))
    energy_closed = (0.5 * LAMBDA * tr_e ** 2
                     + MU * sum(eps[i][j] ** 2 for i in range(3) for j in range(3)))
    print(f"strain energy density from 1/2 sigma:eps      = {energy_tensor:.6e} J/m^3")
    print(f"from 1/2 lambda (tr e)^2 + mu e:e             = {energy_closed:.6e} J/m^3")
    print(f"difference = {abs(energy_tensor - energy_closed):.3e} J/m^3")

    # inversion through the Voigt matrix
    n = 6
    # build the full 6x6 inverse by Gauss-Jordan
    aug = [[cm[i][j] for j in range(n)] + [1.0 if i == j else 0.0 for j in range(n)]
           for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        pv = aug[col][col]
        aug[col] = [v / pv for v in aug[col]]
        for r in range(n):
            if r != col and aug[r][col] != 0.0:
                factor = aug[r][col]
                aug[r] = [a - factor * b for a, b in zip(aug[r], aug[col])]
    comp = [row[n:] for row in aug]
    print(f"compliance component S_1111 first entry = {comp[0][0]:.6e} 1/Pa")
    print(f"  compare with 1/E where E = mu (3 lambda + 2 mu)/(lambda + mu) = "
          f"{1.0 / (MU * (3 * LAMBDA + 2 * MU) / (LAMBDA + MU)):.6e} 1/Pa")
    # round trip
    pairs = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
    evec = [eps[p[0]][p[1]] for p in pairs]
    svec = [sum(cm[i][j] * evec[j] for j in range(n)) for i in range(n)]
    eback = [sum(comp[i][j] * svec[j] for j in range(n)) for i in range(n)]
    err = max(abs(eback[i] - evec[i]) for i in range(n))
    print(f"round trip strain -> stress -> strain: max error = {err:.3e}")

    worst = 0.0
    for scale in (1.0, 0.5, 2.0):
        for shear in (1.0, 3.0):
            test = [[scale * 1e-3 * delta(i, j) + shear * 1e-3 * delta(i, j + 1)
                     for j in range(3)] for i in range(3)]
            tr = sum(test[i][i] for i in range(3))
            e = (0.5 * LAMBDA * tr ** 2
                 + MU * sum(test[i][j] ** 2 for i in range(3) for j in range(3)))
            worst = max(worst, abs(e))
    print(f"strain energy rounded to zero anywhere? smallest tested value = "
          f"{worst:.3e} J/m^3 (all positive)")
    print()
    print("  Positive strain energy for every strain is the condition that makes a")
    print("  material stable: it forces mu > 0, K = lambda + 2 mu/3 > 0 and")
    print("  consequently -1 < nu < 1/2. The last of those is the assertion that a")
    print("  material cannot swell when squeezed, and it is what makes v_p > v_s.")
    print("  The compliance is the inverse of the stiffness; geophysicists invert")
    print("  it every time they convert measured moduli into wave speeds.")


def part4_two_constants():
    section("4. Isotropic elasticity has exactly two constants")
    cm = voigt_matrix()
    worst = 0.0
    for i in range(6):
        for j in range(6):
            c11 = LAMBDA + 2.0 * MU
            c12 = LAMBDA
            c44 = MU
            expected = {(0, 0): c11, (1, 1): c11, (2, 2): c11,
                        (0, 1): c12, (0, 2): c12, (1, 2): c12,
                        (1, 0): c12, (2, 0): c12, (2, 1): c12,
                        (3, 3): c44, (4, 4): c44, (5, 5): c44}.get((i, j), 0.0)
            worst = max(worst, abs(cm[i][j] - expected))
    print(f"lambda = {LAMBDA / 1e9:.3f} GPa, mu = {MU / 1e9:.3f} GPa")
    print(f"C11 = lambda + 2 mu = {(LAMBDA + 2 * MU) / 1e9:.3f} GPa, "
          f"C12 = lambda = {LAMBDA / 1e9:.3f} GPa, C44 = mu = {MU / 1e9:.3f} GPa")
    print(f"max |C_voigt - pattern| over all 36 entries = {worst:.3e} Pa")
    print(f"check: C11 - C12 = 2 C44? "
          f"{((LAMBDA + 2 * MU) - LAMBDA) / (2 * MU):.12f}")
    print()
    print("  The identity C11 - C12 = 2 C44 is the isotropy condition; it is the")
    print("  cheapest way to test whether a set of measured elastic constants is")
    print("  consistent with isotropy, and it fails by large margins for real rocks")
    print("  at the core scale (lesson 02-04-06).")


if __name__ == "__main__":
    part1_symmetry()
    part2_contraction()
    part3_voigt_and_energy()
    part4_two_constants()
