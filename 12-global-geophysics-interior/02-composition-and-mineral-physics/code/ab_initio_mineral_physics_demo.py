#!/usr/bin/env python3
"""Ab initio mineral physics: elastic tensors, wave speeds in a crystal, stability,
and how crystal anisotropy becomes seismic anisotropy.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ab_initio_mineral_physics_demo.py

Everything is SYNTHETIC.  The elastic-constant tensors, densities and texture
fractions are chosen teaching values, picked to be in the range of dense oxides and
iron at high pressure.  They are not computed results and not measurements, and no
published tensor is reproduced.

Contents
--------
1. The elastic tensor: cubic (3 constants) and hexagonal (5 constants).
2. Derived isotropic moduli: Voigt, Reuss, Hill and the anisotropy factors.
3. The Christoffel equation: three wave speeds per direction.
4. Directional wave speeds and the size of the anisotropy, in the two crystals.
5. Stability: Born criteria, and what happens when one is violated.
6. From crystal anisotropy to seismic anisotropy: aggregate texture.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# SYNTHETIC elastic tensors in GPa (chosen values, not measured or computed)
CUBIC = {"C11": 294.0, "C12": 93.0, "C44": 155.0, "rho": 3.58, "name": "cubic oxide"}
HEX = {"C11": 280.0, "C12": 160.0, "C13": 140.0, "C33": 300.0, "C44": 110.0,
       "rho": 9.00, "name": "hexagonal metal"}

VOIGT_PAIRS = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))


def section(title):
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def cubic_matrix(c11, c12, c44):
    c = np.zeros((6, 6))
    for i in range(3):
        for j in range(3):
            c[i, j] = c11 if i == j else c12
    for i in (3, 4, 5):
        c[i, i] = c44
    return c


def hex_matrix(c11, c12, c13, c33, c44):
    c = np.zeros((6, 6))
    c[0, 0] = c[1, 1] = c11
    c[0, 1] = c[1, 0] = c12
    c[0, 2] = c[2, 0] = c[1, 2] = c[2, 1] = c13
    c[2, 2] = c33
    c[3, 3] = c[4, 4] = c44
    c[5, 5] = 0.5 * (c11 - c12)
    return c


def to_tensor(cv):
    """Expand the 6x6 Voigt matrix into the full C_ijkl tensor."""
    c = np.zeros((3, 3, 3, 3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    c[i, j, k, l] = cv[vi(i, j), vi(k, l)]
    return c


def vi(i, j):
    """Voigt index for a pair of Cartesian indices."""
    if i == j:
        return i
    return 3 + (3 - i - j) if i + j != 3 else 3


def voigt_index_map():
    """Build the (i, j) -> I table explicitly so vi() cannot be wrong."""
    table = {}
    order = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
    for idx, pair in enumerate(order):
        table[pair] = idx
        table[(pair[1], pair[0])] = idx
    return table


_VI = voigt_index_map()


def vi(i, j):                                    # noqa: F811
    return _VI[(i, j)]


def christoffel(cv, n, rho):
    """Solve the Christoffel equation for direction n; return (v_p, v_s1, v_s2).

    M_ij = C_ijkl n_j n_l, eigenvalues are rho v^2.
    """
    c = to_tensor(cv)
    n = np.asarray(n, dtype=float)
    n = n / np.linalg.norm(n)
    m = np.einsum("ijkl,j,l->ik", c, n, n)
    vals, vecs = np.linalg.eigh(m)
    speeds = np.sqrt(np.maximum(vals, 0.0) / rho)
    return speeds[2], speeds[1], speeds[0], vals


def isotropic_moduli(cv):
    """Voigt and Reuss isotropic moduli of a single crystal."""
    k_v = (cv[0, 0] + cv[1, 1] + cv[2, 2] + 2 * (cv[0, 1] + cv[0, 2] + cv[1, 2])) / 9.0
    g_v = (cv[0, 0] + cv[1, 1] + cv[2, 2] - (cv[0, 1] + cv[0, 2] + cv[1, 2])
           + 3 * (cv[3, 3] + cv[4, 4] + cv[5, 5])) / 15.0
    s = np.linalg.inv(cv)
    k_r = 1.0 / (s[0, 0] + s[1, 1] + s[2, 2] + 2 * (s[0, 1] + s[0, 2] + s[1, 2]))
    g_r = 15.0 / (4 * (s[0, 0] + s[1, 1] + s[2, 2])
                  - 4 * (s[0, 1] + s[0, 2] + s[1, 2])
                  + 3 * (s[3, 3] + s[4, 4] + s[5, 5]))
    return k_v, k_r, g_v, g_r


def isotropic_matrix(k, g):
    """Build a Voigt matrix for an isotropic medium from K and G."""
    c = np.zeros((6, 6))
    lam = k - 2.0 * g / 3.0
    for i in range(3):
        for j in range(3):
            c[i, j] = lam if i != j else lam + 2.0 * g
    for i in (3, 4, 5):
        c[i, i] = g
    return c


def main():
    section("1. The elastic tensor")
    cv_cub = cubic_matrix(CUBIC["C11"], CUBIC["C12"], CUBIC["C44"])
    cv_hex = hex_matrix(HEX["C11"], HEX["C12"], HEX["C13"], HEX["C33"], HEX["C44"])
    print(f"  SYNTHETIC cubic tensor ({CUBIC['name']}): C11 = {CUBIC['C11']:.0f}, "
          f"C12 = {CUBIC['C12']:.0f}, C44 = {CUBIC['C44']:.0f} GPa, "
          f"rho = {CUBIC['rho']:.2f} g/cm^3")
    print("    Voigt matrix (GPa), upper-left 3x3 and the diagonal shear terms:")
    print(np.array2string(cv_cub, precision=0, suppress_small=True))
    print(f"  SYNTHETIC hexagonal tensor ({HEX['name']}): C11 = {HEX['C11']:.0f}, "
          f"C12 = {HEX['C12']:.0f}, C13 = {HEX['C13']:.0f}, "
          f"C33 = {HEX['C33']:.0f}, C44 = {HEX['C44']:.0f} GPa, "
          f"rho = {HEX['rho']:.2f} g/cm^3")
    print(np.array2string(cv_hex, precision=0, suppress_small=True))
    print("  symmetry reduces 81 tensor components to 3 (cubic) and 5 (hexagonal).")
    print("  An ab initio calculation returns these numbers; everything else in this")
    print("  lesson is a consequence of them.")

    section("2. Derived isotropic moduli and anisotropy factors")
    for name, cv, rho in ((CUBIC["name"], cv_cub, CUBIC["rho"]),
                          (HEX["name"], cv_hex, HEX["rho"])):
        k_v, k_r, g_v, g_r = isotropic_moduli(cv)
        print(f"  {name}:")
        print(f"    K: Voigt {k_v:7.1f}, Reuss {k_r:7.1f}, Hill "
              f"{0.5 * (k_v + k_r):7.1f} GPa")
        print(f"    G: Voigt {g_v:7.1f}, Reuss {g_r:7.1f}, Hill "
              f"{0.5 * (g_v + g_r):7.1f} GPa")
        k_h = 0.5 * (k_v + k_r)
        g_h = 0.5 * (g_v + g_r)
        vp = np.sqrt((k_h + 4.0 * g_h / 3.0) / rho)
        vs = np.sqrt(g_h / rho)
        print(f"    isotropic-equivalent velocities: vp = {vp:.3f}, "
              f"vs = {vs:.3f} km/s")
    print(f"  cubic anisotropy factor A = 2C44/(C11-C12) = "
          f"{2 * CUBIC['C44'] / (CUBIC['C11'] - CUBIC['C12']):.3f}"
          "  (A = 1 means elastically isotropic)")
    print(f"  hexagonal ratio C33/C11 = {HEX['C33'] / HEX['C11']:.3f}, "
          f"C44/C11 = {HEX['C44'] / HEX['C11']:.3f}")
    print("  the cubic A shows how far a single crystal is from isotropic; the")
    print("  hexagonal ratios do the same job for the two symmetry directions.")

    print("  K_V = K_R for the cubic tensor is an identity, but for the hexagonal")
    print("  tensor it is an accident of the chosen numbers:")
    print(f"    C11 + C12 = {HEX['C11'] + HEX['C12']:.1f}, "
          f"C33 + C13 = {HEX['C33'] + HEX['C13']:.1f}"
          "  -> equal, so K_V = K_R here")
    cv_hex2 = hex_matrix(290.0, 230.0, 110.0, 280.0, 95.0)
    k_v2, k_r2, _, _ = isotropic_moduli(cv_hex2)
    print("  a second SYNTHETIC hexagonal tensor with C11 = 290, C12 = 230, "
          "C13 = 110,")
    print("  C33 = 280, C44 = 95 GPa (C11 + C12 = 520, C33 + C13 = 390) gives")
    print(f"    K_V = {k_v2:.4f} GPa, K_R = {k_r2:.4f} GPa, "
          f"difference = {k_v2 - k_r2:.4f} GPa")
    pred_k = 2.0 * (520.0 - 280.0 - 110.0) ** 2 / (9.0 * (520.0 + 2 * 280.0 - 4 * 110.0))
    print(f"    K_V - K_R = 2(C11+C12-C33-C13)^2 / [9(C11+C12+2C33-4C13)] "
          f"= {pred_k:.4f} GPa")
    print("  so K_V = K_R holds for hexagonal symmetry only when "
          "C11 + C12 = C33 + C13;")
    print("  the shear modulus is bracketed in every symmetry, cubic included.")

    section("3. The Christoffel equation: three speeds per direction")
    directions = {
        "[100]": (1, 0, 0), "[110]": (1, 1, 0), "[111]": (1, 1, 1),
        "[001]": (0, 0, 1),
    }
    print("  M_ij = C_ijkl n_j n_l; the three eigenvalues are rho v^2.")
    print("  cubic crystal:")
    print("    direction   v_p (km/s)   v_s1 (km/s)   v_s2 (km/s)   v_s splitting")
    for name, n in directions.items():
        vp, vs1, vs2, vals = christoffel(cv_cub, n, CUBIC["rho"])
        print(f"    {name:9s}   {vp:10.3f}   {vs1:12.3f}   {vs2:12.3f}   "
              f"{abs(vs1 - vs2):12.3f}")
    print("  hexagonal crystal (c-axis along [001]):")
    print("    direction   v_p (km/s)   v_s1 (km/s)   v_s2 (km/s)   v_s splitting")
    for name, n in directions.items():
        vp, vs1, vs2, vals = christoffel(cv_hex, n, HEX["rho"])
        print(f"    {name:9s}   {vp:10.3f}   {vs1:12.3f}   {vs2:12.3f}   "
              f"{abs(vs1 - vs2):12.3f}")
    print("  in the cubic crystal the shear splitting vanishes along [100] and")
    print("  [111] by symmetry and is largest along [110]; in a hexagonal crystal")
    print("  it is largest in the basal plane and vanishes along the c-axis.")

    section("4. Directional wave speeds and the size of the anisotropy")
    print("  hexagonal crystal, angle measured from the c-axis:")
    print("    angle (deg)   v_p (km/s)   fast v_s   slow v_s   "
          "splitting (s per 100 km)")
    angles = np.arange(0.0, 91.0, 15.0)
    vp_list = []
    for ang in angles:
        t = np.radians(ang)
        n = (np.sin(t), 0.0, np.cos(t))
        vp, vs1, vs2, _ = christoffel(cv_hex, n, HEX["rho"])
        vp_list.append(vp)
        split = 100.0 * abs(vs1 - vs2) / (vs1 * vs2)
        print(f"  {ang:11.0f}   {vp:10.3f}   {vs1:9.3f}   {vs2:8.3f}   "
              f"{split:17.3f}")
    vp_arr = np.array(vp_list)
    av_p = 200.0 * (vp_arr.max() - vp_arr.min()) / (vp_arr.max() + vp_arr.min())
    print(f"  P anisotropy AV_P = 200 (vp_max - vp_min)/(vp_max + vp_min) = "
          f"{av_p:.2f} %")
    print("  orientation-dependence of this size is what makes a single crystal a")
    print("  candidate explanation for a seismic anisotropy measurement, and the")
    print("  shear splitting is what a polarised shear-wave experiment measures.")

    section("5. Stability: the Born criteria")
    print("  a crystal is elastically stable only if the strain-energy matrix is")
    print("  positive definite, which for a cubic crystal requires:")
    checks = (("C11 - C12 > 0", CUBIC["C11"] - CUBIC["C12"]),
              ("C11 + 2C12 > 0", CUBIC["C11"] + 2 * CUBIC["C12"]),
              ("C44 > 0", CUBIC["C44"]))
    for label, value in checks:
        print(f"    {label:16s} = {value:8.1f} GPa  ->  "
              f"{'stable' if value > 0 else 'VIOLATED'}")
    print("\n  now violate C44 by making it negative and look at the wave speeds:")
    print("    C44 (GPa)   rho v^2 along [100] (GPa)   shear speed (km/s)")
    for c44 in (155.0, 50.0, 1.0, -1.0, -20.0):
        cv_bad = cubic_matrix(CUBIC["C11"], CUBIC["C12"], c44)
        vp, vs1, vs2, vals = christoffel(cv_bad, (1, 0, 0), CUBIC["rho"])
        print(f"  {c44:10.1f}   {vals[1]:25.2f}   "
              f"{'imaginary: unstable' if vals[1] < 0 else f'{vs1:18.3f}'}")
    print("  a negative eigenvalue means the medium cannot transmit that wave at")
    print("  all: the stiffness matrix corresponds to a material that would gain")
    print("  energy by shearing, so the calculation is unphysical.  Born stability")
    print("  is therefore the first check on any computed elastic tensor, and it")
    print("  is cheap; a tensor that fails it will still fit a distorted structure")
    print("  and still return numbers.")

    section("6. From crystal anisotropy to seismic anisotropy")
    k_v, k_r, g_v, g_r = isotropic_moduli(cv_hex)
    cv_iso = isotropic_matrix(0.5 * (k_v + k_r), 0.5 * (g_v + g_r))
    print("  a textured aggregate is modelled as a Voigt-style mixture of an")
    print("  aligned single crystal and an isotropic aggregate of the same crystals:")
    print(f"    C_eff = f C_aligned + (1 - f) C_isotropic")
    print("    alignment f   vp along c   vp in basal plane   AV_P (%)")
    for f in (0.0, 0.1, 0.25, 0.5, 0.75, 1.0):
        cv_eff = f * cv_hex + (1.0 - f) * cv_iso
        vp_c, _, _, _ = christoffel(cv_eff, (0, 0, 1), HEX["rho"])
        vp_a, _, _, _ = christoffel(cv_eff, (1, 0, 0), HEX["rho"])
        av = 200.0 * abs(vp_c - vp_a) / (vp_c + vp_a)
        print(f"  {f:13.2f}   {vp_c:10.3f}   {vp_a:16.3f}   {av:8.2f}")
    print("  the aggregate anisotropy is the single-crystal anisotropy scaled by")
    print("  the degree of alignment, so a measured 1 % aggregate anisotropy can")
    print("  mean either a strongly anisotropic crystal weakly aligned or a weakly")
    print("  anisotropic crystal strongly aligned.  Seismology measures the")
    print("  product; mineral physics supplies one factor, and the texture supplies")
    print("  the other.")


if __name__ == "__main__":
    main()
