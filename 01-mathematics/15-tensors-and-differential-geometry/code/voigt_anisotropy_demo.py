"""How 81 components become 21, and how symmetry classes reduce them further.

Run:  python3 voigt_anisotropy_demo.py
Requires: Python standard library only.

Companion to lesson 01-15-05.

This demo counts, rather than asserts. Everything below is built from explicit
index loops over the 3^4 = 81 entries of a rank-4 tensor:

  1. the minor symmetries C_ijkl = C_jikl = C_ijlk cut 81 down to 36;
  2. the major symmetry C_ijkl = C_klij cuts 36 down to 21;
  3. Voigt notation is a relabelling of index PAIRS, with a factor of 2 hiding
     in the shear-strain convention -- shown both ways;
  4. imposing a point group by averaging rotations over the group gives the
     standard count for each crystal class, including 5 for transverse
     isotropy and 3 for cubic, and 2 for isotropic;
  5. a matrix with the VTI *pattern* but the wrong C12 is NOT hexagonal, and
     the demo exhibits the failure;
  6. Voigt is what feeds the Christoffel equation, hence the Thomsen
     parameters and the measured wave speeds.

Stress-strain convention: sigma_ij = C_ijkl e_kl with e_kl the SCIENTIFIC
strain, 1/2 (u_k,l + u_l,k). Voigt ordering is (11, 22, 33, 23, 13, 12).
"""

import math
import random

random.seed(31337)
TOL = 1.0e-9


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def idx(i, j, k, l):
    return ((i * 3 + j) * 3 + k) * 3 + l


def delta(i, j):
    return 1.0 if i == j else 0.0


VOIGT = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))
PAIR = {(0, 0): 0, (1, 1): 1, (2, 2): 2, (1, 2): 3, (2, 1): 3,
        (0, 2): 4, (2, 0): 4, (0, 1): 5, (1, 0): 5}


# --------------------------------------------------------------------------
# Rank-4 tensors as flat 81-vectors, and a rank routine
# --------------------------------------------------------------------------

def zeros():
    return [0.0] * 81


def rank(vectors, tol=TOL):
    """Dimension of the span of the given 81-vectors (modified Gram-Schmidt)."""
    basis = []
    for v in vectors:
        w = list(v)
        for _ in range(2):                     # reorthogonalise once
            for b in basis:
                dot = sum(x * y for x, y in zip(w, b))
                w = [x - dot * y for x, y in zip(w, b)]
        n = math.sqrt(sum(x * x for x in w))
        if n > tol * max(1.0, math.sqrt(sum(x * x for x in v))):
            basis.append([x / n for x in w])
    return len(basis)


def minor_basis():
    """The 36 tensors symmetric under i<->j and k<->l, built explicitly."""
    out = []
    for i in range(3):
        for j in range(i, 3):
            for k in range(3):
                for l in range(k, 3):
                    v = zeros()
                    for (a, b) in ((i, j), (j, i)):
                        for (c, d) in ((k, l), (l, k)):
                            v[idx(a, b, c, d)] += 0.25
                    out.append(v)
    return out


def major_basis():
    """The 21 tensors with both minor and major symmetry, built explicitly."""
    out = []
    for a in range(6):
        for b in range(a, 6):
            pa, pb = VOIGT[a], VOIGT[b]
            v = zeros()
            for (c, d) in ((pa[0], pa[1]), (pa[1], pa[0])):
                for (e, f) in ((pb[0], pb[1]), (pb[1], pb[0])):
                    v[idx(c, d, e, f)] += 0.125
            for (c, d) in ((pb[0], pb[1]), (pb[1], pb[0])):
                for (e, f) in ((pa[0], pa[1]), (pa[1], pa[0])):
                    v[idx(c, d, e, f)] += 0.125
            out.append(v)
    return out


# --------------------------------------------------------------------------
# Rotation of a rank-4 tensor, four single-index contractions
# --------------------------------------------------------------------------

STRIDE = (27, 9, 3, 1)


def contract(C, Q, d):
    """Contract index d of C with Q: D_i... = Q_i p C_p..."""
    st = STRIDE[d]
    out = [0.0] * 81
    for base in range(81):
        if (base // st) % 3 != 0:
            continue
        for new in range(3):
            total = 0.0
            for old in range(3):
                total += Q[new][old] * C[base + old * st]
            out[base + new * st] = total
    return out


def rotate(C, Q):
    out = C
    for d in range(4):
        out = contract(out, Q, d)
    return out


def maxdiff81(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def scale81(a):
    return max(abs(x) for x in a)


def rot(axis, deg):
    ang = math.radians(deg)
    n = math.sqrt(sum(c * c for c in axis))
    k = [c / n for c in axis]
    c, s = math.cos(ang), math.sin(ang)
    m = [[c * delta(i, j) + (1 - c) * k[i] * k[j] for j in range(3)] for i in range(3)]
    kx = [[0.0, -k[2], k[1]], [k[2], 0.0, -k[0]], [-k[1], k[0], 0.0]]
    for i in range(3):
        for j in range(3):
            m[i][j] += s * kx[i][j]
    return m


def matmul(a, b):
    return [[sum(a[i][t] * b[t][j] for t in range(3)) for j in range(3)]
            for i in range(3)]


def key(m):
    return tuple(round(x, 9) for row in m for x in row)


def closure(generators):
    """The group generated by a list of 3x3 rotations, as a list of matrices."""
    ident = [[delta(i, j) for j in range(3)] for i in range(3)]
    group = {key(ident): ident}
    frontier = [ident]
    while frontier:
        new = []
        for g in frontier:
            for h in generators:
                p = matmul(g, h)
                k = key(p)
                if k not in group:
                    group[k] = p
                    new.append(p)
        frontier = new
    return list(group.values())


# --------------------------------------------------------------------------
# 1 and 2. Counting the components by explicit construction
# --------------------------------------------------------------------------

section("1. 81 -> 36 -> 21, counted by construction (no table quoted)")

mb = minor_basis()
print(f"  basis tensors symmetric under i<->j and k<->l, written down: {len(mb)}")
print(f"  dimension of their span (Gram-Schmidt): {rank(mb)}")

JB = major_basis()
print(f"  basis tensors with both minor and major symmetry: {len(JB)}")
print(f"  dimension of their span: {rank(JB)}")

# The same two dimensions by orthogonal projection instead of basis building.
def sym_minor(C):
    out = zeros()
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    out[idx(i, j, k, l)] = 0.25 * (
                        C[idx(i, j, k, l)] + C[idx(j, i, k, l)]
                        + C[idx(i, j, l, k)] + C[idx(j, i, l, k)])
    return out


def sym_major(C):
    out = zeros()
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    out[idx(i, j, k, l)] = 0.5 * (C[idx(i, j, k, l)]
                                                  + C[idx(k, l, i, j)])
    return out


E = [zeros() for _ in range(81)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                E[idx(i, j, k, l)][idx(i, j, k, l)] = 1.0
print(f"  rank of P_minor acting on the 81 unit tensors: "
      f"{rank([sym_minor(v) for v in E])}")
print(f"  rank of P_major P_minor acting on the same:    "
      f"{rank([sym_major(sym_minor(v)) for v in E])}")
print("  Reading: 81 raw components, 36 after the two minor symmetries that")
print("  follow from sigma and e being symmetric, and 21 after the major")
print("  symmetry that follows from the existence of a strain-energy density.")
print("  21 = 6*7/2, which is what a symmetric 6x6 matrix has.")


# --------------------------------------------------------------------------
# 3. Voigt notation, and the factor of 2
# --------------------------------------------------------------------------

section("2. Voigt notation: relabelling pairs, and the factor of 2")


def voigt_matrix(C):
    return [[C[idx(*VOIGT[a], *VOIGT[b])] for b in range(6)] for a in range(6)]


def from_voigt(M):
    """C_ijkl = M[alpha][beta] with alpha = pair(i,j), beta = pair(k,l).

    Building it this way makes the minor symmetries automatic, which is the
    point: Voigt notation never uses the reversed index orders.
    """
    C = zeros()
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    C[idx(i, j, k, l)] = M[PAIR[(i, j)]][PAIR[(k, l)]]
    return C


random.seed(4242)
# A random tensor with both symmetries, built as a random symmetric 6x6 matrix.
M = [[0.0] * 6 for _ in range(6)]
for a in range(6):
    for b in range(a, 6):
        M[a][b] = M[b][a] = random.gauss(0.0, 1.0)
C = from_voigt(M)
print(f"  max |C_ijkl - C_jikl| = "
      f"{max(abs(C[idx(i, j, k, l)] - C[idx(j, i, k, l)]) for i in range(3) for j in range(3) for k in range(3) for l in range(3)):.1e}")
print(f"  max |C_ijkl - C_klij| = "
      f"{max(abs(C[idx(i, j, k, l)] - C[idx(k, l, i, j)]) for i in range(3) for j in range(3) for k in range(3) for l in range(3)):.1e}")
print(f"  round trip Voigt -> tensor -> Voigt: max |dM| = "
      f"{max(abs(voigt_matrix(from_voigt(M))[a][b] - M[a][b]) for a in range(6) for b in range(6)):.1e}")

e = [[0.01, -0.004, 0.002], [-0.004, 0.006, 0.003], [0.002, 0.003, -0.002]]
sigma_tensor = [[sum(C[idx(i, j, k, l)] * e[k][l]
                     for k in range(3) for l in range(3)) for j in range(3)]
                for i in range(3)]


def voigt_vector(e_):
    """Voigt strain: the three engineering shears carry a factor 2."""
    return [e_[0][0], e_[1][1], e_[2][2],
            2.0 * e_[1][2], 2.0 * e_[0][2], 2.0 * e_[0][1]]


ev = voigt_vector(e)
sigma_voigt = [sum(M[a][b] * ev[b] for b in range(6)) for a in range(6)]
sigma_from_voigt = [[sigma_voigt[PAIR[(i, j)]] for j in range(3)] for i in range(3)]
print(f"\n  sigma_ij = C_ijkl e_kl  versus  sigma_alpha = C_ab eps_b")
print(f"  largest difference = "
      f"{max(abs(sigma_tensor[i][j] - sigma_from_voigt[i][j]) for i in range(3) for j in range(3)):.1e}")
print(f"  Voigt strain vector = {[f'{x:.4f}' for x in ev]}")
print("  The factor 2 on the shear entries is what makes this an identity.")
print("  Using eps_4 = e_23 instead would halve every shear stress for which")
print("  C_a4 is the only contributor.")

bad = [e[0][0], e[1][1], e[2][2], e[1][2], e[0][2], e[0][1]]
sigma_bad = [sum(M[a][b] * bad[b] for b in range(6)) for a in range(6)]
print(f"  with eps_4 = e_23 (wrong for this matrix): sigma_xy would be "
      f"{sigma_bad[5]:+.6f} instead of {sigma_voigt[5]:+.6f},"
      f" i.e. wrong by {100 * abs(sigma_bad[5] / sigma_voigt[5] - 1):.1f} per cent")

# The factor of 2 in isolation: one shear modulus, one shear strain.
M_shear = [[0.0] * 6 for _ in range(6)]
M_shear[5][5] = 20.0e9
e_pure = [[0.0, 0.01, 0.0], [0.01, 0.0, 0.0], [0.0, 0.0, 0.0]]
sig_pure = [[sum(from_voigt(M_shear)[idx(i, j, k, l)] * e_pure[k][l]
                 for k in range(3) for l in range(3)) for j in range(3)]
            for i in range(3)]
print(f"\n  C_1212 = 20 GPa alone, pure shear e_12 = e_21 = 0.01:")
print(f"    tensor form: sigma_12 = C_1212 e_12 + C_1221 e_21 = "
      f"{sig_pure[0][1] / 1e6:.4f} MPa")
print(f"    Voigt with eps_6 = 2 e_12: sigma_6 = C_66 eps_6 = "
      f"{M_shear[5][5] * (2 * 0.01) / 1e6:.4f} MPa")
print(f"    Voigt with eps_6 = e_12:   sigma_6 = C_66 eps_6 = "
      f"{M_shear[5][5] * 0.01 / 1e6:.4f} MPa   <- a factor of 2 too small")
print("  Both conventions exist in the literature. The matrix C_ab is the same")
print("  object only if you also fix which strain vector multiplies it.")


# --------------------------------------------------------------------------
# 4. Symmetry classes by explicit group averaging
# --------------------------------------------------------------------------

section("3. Symmetry classes: counting by averaging over the point group")

IDENT = [[delta(i, j) for j in range(3)] for i in range(3)]
C2X = [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]
C2Y = [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]
C2Z = [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]
C3DIAG = [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]
GENERATORS = {
    "triclinic (1, -1)": [],
    "monoclinic (2, m, 2/m)": [C2Z],
    "orthorhombic (222, mm2, mmm)": [C2X, C2Y, C2Z],
    "tetragonal (422, 4mm, -42m, 4/mmm)": [rot([0, 0, 1], 90.0), C2X],
    "trigonal (32, 3m, -3m)": [rot([0, 0, 1], 120.0), C2Y],
    "hexagonal (622, 6mm, -6m2, 6/mmm)": [rot([0, 0, 1], 60.0), C2X],
    "cubic (23, m-3, 432, -43m, m-3m)": [rot([0, 0, 1], 90.0), C3DIAG],
}
TABLE = {
    "triclinic (1, -1)": 21,
    "monoclinic (2, m, 2/m)": 13,
    "orthorhombic (222, mm2, mmm)": 9,
    "tetragonal (422, 4mm, -42m, 4/mmm)": 6,
    "trigonal (32, 3m, -3m)": 6,
    "hexagonal (622, 6mm, -6m2, 6/mmm)": 5,
    "cubic (23, m-3, 432, -43m, m-3m)": 3,
}

print(f"  {'crystal class':38s} {'|G|':>5s} {'computed':>9s} {'standard':>9s}  ok")
for name, gens in GENERATORS.items():
    group = closure(gens)
    projected = []
    for v in major_basis():
        acc = zeros()
        for g in group:
            t = rotate(v, g)
            acc = [x + y for x, y in zip(acc, t)]
        projected.append([x / len(group) for x in acc])
    n = rank(projected)
    flag = "yes" if n == TABLE[name] else "NO"
    print(f"  {name:38s} {len(group):5d} {n:9d} {TABLE[name]:9d}  {flag}")

# The isotropic case: the group is continuous, so bracket the count instead of
# sampling it. A LOWER bound comes from writing down two independent isotropic
# tensors and checking that they really are invariant; an UPPER bound comes from
# averaging over a large sample of rotations and measuring the rank.
I_ten = zeros()
J_ten = zeros()
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                I_ten[idx(i, j, k, l)] = delta(i, j) * delta(k, l)
                J_ten[idx(i, j, k, l)] = 0.5 * (delta(i, k) * delta(j, l)
                                                + delta(i, l) * delta(j, k))
print(f"\n  LOWER BOUND, by explicit construction: the two tensors delta_ij delta_kl and")
print(f"  1/2 (delta_ik delta_jl + delta_il delta_jk) are independent")
print(f"  (rank of the pair = {rank([I_ten, J_ten])}) and invariant:")
worst = 0.0
n_rot = 2000
rots = []
for _ in range(n_rot):
    axis = [random.gauss(0, 1) for _ in range(3)]
    if sum(c * c for c in axis) < 1e-12:
        axis = [0.0, 0.0, 1.0]
    rots.append(rot(axis, random.uniform(0.0, 360.0)))
for vec in (I_ten, J_ten):
    for g in rots:
        worst = max(worst, maxdiff81(rotate(vec, g), vec) / scale81(vec))
print(f"    largest relative change over {n_rot} random rotations = {worst:.1e}")
print("  (A sampled check like this can only support a claim, never establish it,")
print("   which is why the count itself is decided by exact groups below.)")

print("  UPPER BOUND: no finite group equals the full rotation group, but a small")
print("  generating set already pins the invariant space down, and the fixed space")
print("  of a group generated by g1 and g2 is exactly the intersection of the fixed")
print("  spaces of g1 and g2. So it is enough to stack the residuals (I - R)v over")
print("  the 21 basis tensors and measure the rank of that stack.")

mb21 = major_basis()


def fixed_dim(gens):
    """dim of the space of tensors unchanged by every element of <gens>."""
    rows = []
    for g in gens:
        for v in mb21:
            rows.append([a - b for a, b in zip(rotate(v, g), v)])
    return len(mb21) - rank(rows)


for label, gens, expected in (
        ("30 deg about z alone", [rot([0, 0, 1], 30.0)], 5),
        ("30 deg about z and 90 deg about y",
         [rot([0, 0, 1], 30.0), rot([0, 1, 0], 90.0)], 2),
        ("cubic generators, for cross-check",
         [rot([0, 0, 1], 90.0), C3DIAG], 3)):
    print(f"    {label}: independent constants = {fixed_dim(gens)}"
          f"   (expected {expected})")
print("  The first is the five-constant transversely isotropic space: a rotation")
print("  by 30 deg about z leaves only the components of weight zero, which are")
print("  C11 = C22, C13 = C23, C33, C44 = C55 and C66 with C12 = C11 - 2 C66.")
print("  Adding the 90 deg rotation about y exchanges the z axis with the x axis")
print("  and leaves only lambda and mu. Lower bound 2 (explicit pair of isotropic")
print("  tensors), upper bound 2 (fixed space of two generators): the count is 2.")
print("  No component above was counted by reading a table.")

print("\n  Note that inversion has no effect: C has four indices, and")
print("  (-1)^4 = +1, so every centrosymmetric pair of point groups shares a")
print("  count. That is why 622 and 6/mmm both give 5 here.")


# --------------------------------------------------------------------------
# 5. The fake VTI trap
# --------------------------------------------------------------------------

section("4. A VTI-looking matrix that is not hexagonal")

C11, C33, C44, C66, C13 = 30.0, 22.0, 7.0, 10.0, 12.0
C12 = C11 - 2.0 * C66
RHO = 2400.0


def vti(c11, c33, c44, c66, c13, c12):
    m = [[0.0] * 6 for _ in range(6)]
    m[0][0] = m[1][1] = c11
    m[2][2] = c33
    m[0][1] = m[1][0] = c12
    m[0][2] = m[2][0] = m[1][2] = m[2][1] = c13
    m[3][3] = m[4][4] = c44
    m[5][5] = c66
    return m


M_real = vti(C11, C33, C44, C66, C13, C12)          # GPa
M_fake = vti(C11, C33, C44, C66, C13, 20.0)
M_hti_src = vti(C11, C33, C44, C66, C13, C12)
C_real = from_voigt([[v * 1.0e9 for v in row] for row in M_real])   # Pa
C_fake = from_voigt([[v * 1.0e9 for v in row] for row in M_fake])

C6 = rot([0, 0, 1], 60.0)
for label, Mc, Cc in (("C12 = C11 - 2 C66 = 10 (hexagonal)", M_real, C_real),
                      ("C12 = 20 (same pattern, wrong value)", M_fake, C_fake)):
    dev = maxdiff81(rotate(Cc, C6), Cc)
    print(f"  {label:36s} max change under 60 deg about z = {dev:9.3e}"
          f"   (relative {dev / scale81(Cc):.1e})")
print("  Both matrices have the transverse-isotropic PATTERN: zeros in the same")
print("  places. Only one is invariant under the six-fold rotation, and only")
print("  that one may be called hexagonal. The pattern is necessary, not")
print("  sufficient; the constraint C12 = C11 - 2 C66 is part of the definition.")
print(f"  axial speeds are unaffected by the difference: C33 and C44 are the")
print("  same in both matrices, so v_p along the axis is the same. A wrong")
print("  rotation behaviour is invisible in that measurement.")

print("\n  The same test for the other classes, using the invariant tensors the")
print("  group average produces:")
for label, (c11, c12, c44) in (("cubic", (30.0, 10.0, 15.0)),):
    Mc = [[0.0] * 6 for _ in range(6)]
    for a in range(3):
        for b in range(3):
            Mc[a][b] = c12
        Mc[a][a] = c11
    for a in range(3, 6):
        Mc[a][a] = c44
    Cc = from_voigt(Mc)
    dev_hex = maxdiff81(rotate(Cc, C6), Cc) / scale81(Cc)
    dev_cub = maxdiff81(rotate(Cc, C3DIAG), Cc) / scale81(Cc)
    print(f"    {label}: relative change under 60 deg about z = {dev_hex:.3e}"
          f" (not hexagonal); under 120 deg about (1,1,1) = {dev_cub:.3e} (cubic)")


# --------------------------------------------------------------------------
# 6. Towards the wave speeds: Christoffel and Thomsen
# --------------------------------------------------------------------------

section("5. What the representation is for: Christoffel, Thomsen, speeds")

eps_t = (C11 - C33) / (2.0 * C33)
gam_t = (C66 - C44) / (2.0 * C44)
dlt_t = ((C13 + C44) ** 2 - (C33 - C44) ** 2) / (2.0 * C33 * (C33 - C44))
print(f"  Thomsen parameters of the VTI model (constants in GPa):")
print(f"    epsilon = {eps_t:.9f}")
print(f"    gamma   = {gam_t:.9f}")
print(f"    delta   = {dlt_t:.9f}")


def christoffel(Cc, n):
    """Gamma_ik = C_ijkl n_j n_l / rho."""
    return [[sum(Cc[idx(i, j, k, l)] * n[j] * n[l]
                 for j in range(3) for l in range(3)) / RHO
             for k in range(3)] for i in range(3)]


def eig_values(a):
    """Eigenvalues of a symmetric 3x3 matrix by Jacobi rotations."""
    m = [row[:] for row in a]
    for _ in range(100):
        off = max(abs(m[i][j]) for i in range(3) for j in range(3) if i != j)
        if off < 1.0e-12 * max(1.0, max(abs(m[i][i]) for i in range(3))):
            break
        for p in range(3):
            for q in range(p + 1, 3):
                if abs(m[p][q]) < 1e-300:
                    continue
                th = 0.5 * math.atan2(2.0 * m[p][q], m[q][q] - m[p][p])
                cc, ss = math.cos(th), math.sin(th)
                for k in range(3):
                    apk, aqk = m[p][k], m[q][k]
                    m[p][k] = cc * apk - ss * aqk
                    m[q][k] = ss * apk + cc * aqk
                for k in range(3):
                    akp, akq = m[k][p], m[k][q]
                    m[k][p] = cc * akp - ss * akq
                    m[k][q] = ss * akp + cc * akq
    return sorted(m[i][i] for i in range(3))


for label, n in (("n = z (vertical)", [0.0, 0.0, 1.0]),
                 ("n = x (horizontal)", [1.0, 0.0, 0.0])):
    vals = eig_values(christoffel(C_real, n))
    speeds = [math.sqrt(max(0.0, v)) for v in vals]
    print(f"  {label:20s} velocities = "
          f"{[f'{v:10.4f}' for v in speeds]} m/s")
v_axis_p = math.sqrt(C33 * 1e9 / RHO)
v_axis_s = math.sqrt(C44 * 1e9 / RHO)
v_horiz_p = math.sqrt(C11 * 1e9 / RHO)
v_horiz_sh = math.sqrt(C66 * 1e9 / RHO)
print(f"  closed form: v_p(0) = sqrt(C33/rho) = {v_axis_p:.4f}")
print(f"               v_sv(0) = sqrt(C44/rho) = {v_axis_s:.4f}")
print(f"               v_p(90) = sqrt(C11/rho) = {v_horiz_p:.4f}")
print(f"               v_sh(90) = sqrt(C66/rho) = {v_horiz_sh:.4f}")

C_hti = rotate(C_real, rot([0, 1, 0], 90.0))
print(f"\n  rotating the tensor by 90 deg about y (VTI -> HTI):")
print(f"    relative change under 60 deg about x (the new axis) = "
      f"{maxdiff81(rotate(C_hti, rot([1, 0, 0], 60.0)), C_hti) / scale81(C_hti):.3e}")
print(f"    relative change under 60 deg about z (now the hard direction) = "
      f"{maxdiff81(rotate(C_hti, C6), C_hti) / scale81(C_hti):.3e}")
print("  The symmetry axis moved with the tensor, as it must: the constants")
print("  are unchanged as an ordered list, only their labels moved.")
speeds_hti = [math.sqrt(max(0.0, v)) for v in eig_values(christoffel(C_hti, [1.0, 0.0, 0.0]))]
print(f"    propagation along the new axis: {[f'{v:.4f}' for v in speeds_hti]} m/s,"
      f" against {[f'{v:.4f}' for v in [v_axis_s, v_axis_s, v_axis_p]]} m/s from the"
      " VTI axial values")
print("  The eigenvalue SET is invariant even though every component changed.")


# --------------------------------------------------------------------------
# 6. Compliance, positivity, and what the representation preserves
# --------------------------------------------------------------------------

section("6. Compliance, positive definiteness, and invariances")


def inverse(m):
    """Gauss-Jordan inverse of a small square matrix."""
    n = len(m)
    a = [list(row) + [1.0 if i == j else 0.0 for j in range(n)]
         for i, row in enumerate(m)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(a[r][c]))
        if abs(a[piv][c]) < 1e-300:
            raise ValueError("singular")
        a[c], a[piv] = a[piv], a[c]
        d = a[c][c]
        a[c] = [x / d for x in a[c]]
        for r in range(n):
            if r != c and a[r][c] != 0.0:
                f = a[r][c]
                a[r] = [x - f * y for x, y in zip(a[r], a[c])]
    return [row[n:] for row in a]


S_voigt = inverse(M_real)
print("  compliance S = C^-1 in Voigt notation (1/GPa, rounded):")
for a in range(6):
    print("     [" + "  ".join(f"{S_voigt[a][b]:9.5f}" for b in range(6)) + "]")
eps_test = [0.001, -0.0004, 0.0007, 0.0012, -0.0009, 0.0005]
sig_test = [sum(M_real[a][b] * eps_test[b] for b in range(6)) for a in range(6)]
eps_back = [sum(S_voigt[a][b] * sig_test[b] for b in range(6)) for a in range(6)]
print(f"  max |eps_alpha - S_ab sigma_b| = "
      f"{max(abs(eps_test[a] - eps_back[a]) for a in range(6)):.1e}")
print(f"  S_44 = {S_voigt[3][3]:.8f} vs 1/C_44 = {1.0 / M_real[3][3]:.8f}")
print(f"  S_66 = {S_voigt[5][5]:.8f} vs 1/C_66 = {1.0 / M_real[5][5]:.8f}")
print("  The factor-2 convention is what makes S the ordinary matrix inverse: no")
print("  further factors appear, and that is a strong reason to keep the")
print("  engineering strain on the vector side.")

def sym_eig(a, tol=1e-13, sweeps=200):
    """Eigenvalues of a real symmetric matrix of any size, by Jacobi rotations."""
    m = [row[:] for row in a]
    n = len(m)
    for _ in range(sweeps):
        off = max(abs(m[i][j]) for i in range(n) for j in range(n) if i != j)
        if off < tol:
            break
        for p in range(n):
            for q in range(p + 1, n):
                if abs(m[p][q]) < 1e-300:
                    continue
                th = 0.5 * math.atan2(2.0 * m[p][q], m[q][q] - m[p][p])
                cc, ss = math.cos(th), math.sin(th)
                for k in range(n):
                    apk, aqk = m[p][k], m[q][k]
                    m[p][k] = cc * apk - ss * aqk
                    m[q][k] = ss * apk + cc * aqk
                for k in range(n):
                    akp, akq = m[k][p], m[k][q]
                    m[k][p] = cc * akp - ss * akq
                    m[k][q] = ss * akp + cc * akq
    return sorted(m[i][i] for i in range(n))


evals = sym_eig(M_real)
print(f"\n  eigenvalues of the 6x6 stiffness matrix (GPa): "
      f"{[f'{v:.6f}' for v in evals]}")
print(f"  all six positive: {all(v > 0.0 for v in evals)}, so the strain energy")
print("  is positive definite for this model, as a stable material requires.")
print(f"  the classical necessary conditions also hold: C_44 = {M_real[3][3]:.0f} > 0,")
print(f"  C_11 = {C11:.0f} > |C_12| = {abs(C12):.0f}, and "
      f"C_33(C_11 + C_12) = {C33 * (C11 + C12):.0f} > 2 C_13^2 = {2 * C13 ** 2:.0f}.")

print("\n  what the representation preserves, and what it does not:")
C_rot = rotate(C_real, C6)
C_voigt_rot = voigt_matrix(C_rot)
print(f"    the 81-component tensor rotated by 60 deg about z changes by "
      f"{maxdiff81(C_rot, C_real):.3e} (relative "
      f"{maxdiff81(C_rot, C_real) / scale81(C_real):.1e}): it is the same tensor")
M_ref = voigt_matrix(C_real)
print(f"    its Voigt matrix therefore changes by "
      f"{max(abs(M_ref[a][b] - C_voigt_rot[a][b]) for a in range(6) for b in range(6)) / 1e9:.3e} GPa"
      " (all quantities in GPa)")

# The classic trap: treat the 6x6 array as if it were a tensor and rotate it
# with the block-diagonal 6x6 matrix built from the rotation.
R6 = [[0.0] * 6 for _ in range(6)]
for i in range(3):
    for j in range(3):
        R6[i][j] = C6[i][j]
        R6[i + 3][j + 3] = C6[i][j]
M_naive = [[sum(R6[a][c] * R6[b][d] * M_real[c][d] for c in range(6) for d in range(6))
            for b in range(6)] for a in range(6)]
worst = max(abs(M_naive[a][b] - C_voigt_rot[a][b] / 1e9)
            for a in range(6) for b in range(6))
print(f"    rotating the 6x6 array with the block-diagonal 6x6 rotation gives a")
print(f"    matrix differing from the true one by up to {worst:.4f} GPa;")
print(f"    for instance the (1,2) entry would become "
      f"{M_naive[0][1]:.4f} GPa instead of {C_voigt_rot[0][1] / 1e9:.4f} GPa.")
print("    The Voigt array is a storage convention, not a tensor: only the")
print("    81-component object obeys the transformation law of lesson 01-15-02.")
print("    A correct 6x6 rotation exists (the Bond transformation), and it is")
print("    derived from the tensor, with factors of 2 in the shear rows and")
print("    columns -- exactly the factors this lesson has been tracking.")


def main() -> None:
    print("Anisotropy representation: counting, Voigt notation, symmetry classes")


if __name__ == "__main__":
    main()
