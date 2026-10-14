"""A tensor is defined by how it transforms; invariants are what survive.

Run:  python3 tensor_transformation_demo.py
Requires: Python standard library only.

Companion to lesson 01-15-02.

The lesson claims three things that are checked here one by one:
  1. the transformation law for a rank-2 tensor is T'_ij = Q_ip Q_jq T_pq,
     and for a rank-1 object v'_i = Q_ip v_p;
  2. combinations that are invariant under rotation (trace, second invariant,
     determinant, the eigenvalues) are the same in every frame;
  3. some arrays that look like tensors are not -- the Levi-Civita symbol
     under a reflection, and engineering shear strain under any rotation.

Conventions: indices 0,1,2 mean x,y,z; Q is the ACTIVE rotation matrix that
carries the object, applied to the components by v'_i = Q_ij v_j.
"""

import math
import random

N = 3
random.seed(20260101)


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def delta(i, j):
    return 1.0 if i == j else 0.0


# --------------------------------------------------------------------------
# Small dense linear algebra, by hand
# --------------------------------------------------------------------------

def matmul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matvec(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def maxdiff(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a)))


def rotation(axis, angle):
    """Rodrigues formula: R = I cos(a) + sin(a) [k]_x + (1-cos a) k k^T."""
    n = norm(axis)
    k = [c / n for c in axis]
    c, s = math.cos(angle), math.sin(angle)
    r = [[c * delta(i, j) + (1 - c) * k[i] * k[j] for j in range(N)] for i in range(N)]
    kx = [[0.0, -k[2], k[1]], [k[2], 0.0, -k[0]], [-k[1], k[0], 0.0]]
    for i in range(N):
        for j in range(N):
            r[i][j] += s * kx[i][j]
    return r


def jacobi_eig(a, tol=1e-15, sweeps=100):
    """Cyclic Jacobi for a real symmetric matrix: returns (values, columns)."""
    m = [row[:] for row in a]
    n = len(m)
    v = [[delta(i, j) for j in range(n)] for i in range(n)]
    for _ in range(sweeps):
        off = max(abs(m[i][j]) for i in range(n) for j in range(n) if i != j)
        if off < tol:
            break
        for p in range(n):
            for q in range(p + 1, n):
                if abs(m[p][q]) < 1e-300:
                    continue
                theta = 0.5 * math.atan2(2.0 * m[p][q], m[q][q] - m[p][p])
                cc, ss = math.cos(theta), math.sin(theta)
                for k in range(n):
                    apk, aqk = m[p][k], m[q][k]
                    m[p][k] = cc * apk - ss * aqk
                    m[q][k] = ss * apk + cc * aqk
                for k in range(n):
                    akp, akq = m[k][p], m[k][q]
                    m[k][p] = cc * akp - ss * akq
                    m[k][q] = ss * akp + cc * akq
                for k in range(n):
                    vkp, vkq = v[k][p], v[k][q]
                    v[k][p] = cc * vkp - ss * vkq
                    v[k][q] = ss * vkp + cc * vkq
    values = [m[i][i] for i in range(n)]
    cols = [[v[i][j] for i in range(n)] for j in range(n)]
    order = sorted(range(n), key=lambda j: values[j])
    return [values[j] for j in order], [cols[j] for j in order]


def show(name, a, places=4):
    print(f"  {name}")
    for row in a:
        print("     [" + "  ".join(f"{x:>{8 + places}.{places}f}" for x in row) + "]")


# --------------------------------------------------------------------------
# 1. Rotations
# --------------------------------------------------------------------------

section("1. The rotation matrix, and three properties that must hold")

Q = rotation([0.0, 0.0, 1.0], math.radians(30.0))
show("Q = rotation of +30 deg about z", Q)
print(f"  max |Q Q^T - I| = {maxdiff(matmul(Q, transpose(Q)),
                                   [[delta(i, j) for j in range(N)] for i in range(N)]):.1e}")
print(f"  det Q           = {det3(Q):.12f}   (a proper rotation, not a reflection)")
print(f"  max |Q(30 deg) Q(10 deg) - Q(40 deg)| about z = "
      f"{maxdiff(matmul(rotation([0.0, 0.0, 1.0], math.radians(30.0)), rotation([0.0, 0.0, 1.0], math.radians(10.0))), rotation([0.0, 0.0, 1.0], math.radians(40.0))):.1e}")
print("  Rotations compose, and Q^T = Q^-1 follows from Q Q^T = I. The law")
print("  v'_i = Q_ij v_j is therefore a representation of the rotation group,")
print("  not a rule invented for the occasion.")


# --------------------------------------------------------------------------
# 2. How vectors and rank-2 tensors transform
# --------------------------------------------------------------------------

section("2. v'_i = Q_ij v_j and T'_ij = Q_ip Q_jq T_pq")

v = [3.0, -1.0, 2.5]
vp = matvec(Q, v)
print(f"  v   = {v}")
print(f"  v'  = {[round(x, 6) for x in vp]}")
print(f"  |v| = {norm(v):.12f}   |v'| = {norm(vp):.12f}   (a rotation preserves length)")

T = [[8.0, -3.0, 1.0], [-3.0, 5.0, 2.0], [1.0, 2.0, -4.0]]
Tp = matmul(matmul(Q, T), transpose(Q))
show("T (a symmetric rank-2 tensor, arbitrary units)", T)
show("T' = Q T Q^T", Tp)

# The same numbers built the slow way, index by index, as the lesson writes it.
Tp_slow = [[sum(Q[i][p] * Q[j][q] * T[p][q] for p in range(N) for q in range(N))
            for j in range(N)] for i in range(N)]
print(f"  max |T'_ij (matrix form) - T'_ij (index form)| = {maxdiff(Tp, Tp_slow):.1e}")
print("  The two expressions are the same statement; the index form shows why")
print("  a rank-2 tensor carries one Q for each index it possesses.")


# --------------------------------------------------------------------------
# 3. The physical check: the traction must transform with the tensor
# --------------------------------------------------------------------------

section("3. What the transformation law means physically")

n = [0.6, 0.0, 0.8]
t = matvec(T, n)                       # traction on the plane with normal n
np_ = matvec(Q, n)
tp_expected = matvec(Q, t)             # the same physical vector, rotated
tp_from_tensor = matvec(Tp, np_)       # traction from the rotated tensor
print(f"  n  = {n}   ->  n'  = {[round(x, 6) for x in np_]}")
print(f"  t  = {[round(x, 6) for x in t]}")
print(f"  Q t                      = {[round(x, 6) for x in tp_expected]}")
print(f"  T' n'                    = {[round(x, 6) for x in tp_from_tensor]}")
print(f"  difference               = {max(abs(a - b) for a, b in zip(tp_expected, tp_from_tensor)):.1e}")
print("  If T' = Q T Q^T were wrong, the traction on the rotated plane would")
print("  disagree with the rotated traction. That is the operational test of a")
print("  tensor: predict a measurement in the new frame and compare.")


# --------------------------------------------------------------------------
# 4. Invariants
# --------------------------------------------------------------------------

section("4. Invariants: the numbers that do not move")

I1 = trace(T)
I2 = 0.5 * (trace(T) ** 2 - sum(T[i][j] * T[j][i] for i in range(N) for j in range(N)))
I3 = det3(T)
print(f"  I1 = tr T                  = {I1:.12f}")
print(f"  I2 = 1/2[(tr T)^2 - tr T^2] = {I2:.12f}")
print(f"  I3 = det T                 = {I3:.12f}")
print(f"  same three in the rotated frame: "
      f"{trace(Tp):.12f}, "
      f"{0.5 * (trace(Tp) ** 2 - sum(Tp[i][j] * Tp[j][i] for i in range(N) for j in range(N))):.12f}, "
      f"{det3(Tp):.12f}")

print("\n  Random rotations, 200 trials:")
worst = [0.0, 0.0, 0.0]
comp_range = [0.0, 0.0, 0.0]
for _ in range(200):
    q = rotation([random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1)],
                 random.uniform(0.0, 2.0 * math.pi))
    tp = matmul(matmul(q, T), transpose(q))
    i1 = trace(tp)
    i2 = 0.5 * (trace(tp) ** 2 - sum(tp[i][j] * tp[j][i]
                                     for i in range(N) for j in range(N)))
    i3 = det3(tp)
    worst[0] = max(worst[0], abs(i1 - I1))
    worst[1] = max(worst[1], abs(i2 - I2))
    worst[2] = max(worst[2], abs(i3 - I3))
    for i in range(N):
        comp_range[i] = max(comp_range[i], abs(tp[i][i] - T[i][i]))
print(f"    largest change in I1, I2, I3 over all 200 rotations: "
      f"{worst[0]:.1e}, {worst[1]:.1e}, {worst[2]:.1e}")
print(f"    largest change in a single component (T'_ii - T_ii): "
      f"{max(comp_range):.4f}")
print("  The invariants are constant to round-off; the components are not.")
print("  Anything you compute from components alone is frame-dependent unless")
print("  it can be rewritten in terms of these invariants.")


# --------------------------------------------------------------------------
# 5. Eigenvalues and principal directions
# --------------------------------------------------------------------------

section("5. Principal values and principal directions")

values, vectors = jacobi_eig(T)
print(f"  eigenvalues (ascending) = {[round(x, 10) for x in values]}")
print(f"  same eigenvalues from the rotated tensor: "
      + str([round(x, 10) for x in jacobi_eig(Tp)[0]]))

rebuilt = [[sum(values[a] * vectors[a][i] * vectors[a][j] for a in range(N))
            for j in range(N)] for i in range(N)]
print(f"  max |sum_a lam_a n_a n_a^T - T| = {maxdiff(rebuilt, T):.1e}")

lam, w = values[2], vectors[2]
res = max(abs(w[k] * lam - sum(T[k][j] * w[j] for j in range(N))) for k in range(N))
print(f"  residual |T n - lam n| for the largest principal value: {res:.1e}")

lam_p, w_p = jacobi_eig(Tp)
wy = matvec(Q, w)
print(f"  principal direction in the new frame, from the eigenproblem: "
      f"{[round(x, 6) for x in w_p[2]]}")
print(f"  the rotated principal direction Q w                          : "
      f"{[round(x, 6) for x in wy]}")
print(f"  difference (up to sign)                                      : "
      f"{min(max(abs(a - b) for a, b in zip(w_p[2], wy)), max(abs(a + b) for a, b in zip(w_p[2], wy))):.1e}")
print("  A principal direction is a vector, so it rotates as one. That is the")
print("  reason principal axes are physically meaningful and components are not.")

print("\n  Invariants as elementary symmetric functions of the eigenvalues:")
print(f"    sum lam_a            = {sum(values):.12f}   vs I1 = {I1:.12f}")
print(f"    sum lam_a lam_b      = "
      f"{values[0] * values[1] + values[1] * values[2] + values[0] * values[2]:.12f}"
      f"   vs I2 = {I2:.12f}")
print(f"    product lam_a        = {values[0] * values[1] * values[2]:.12f}"
      f"   vs I3 = {I3:.12f}")


# --------------------------------------------------------------------------
# 6. Arrays that are not tensors
# --------------------------------------------------------------------------

section("6a. The Levi-Civita symbol is a pseudo-tensor")

def eps(i, j, k):
    if i == j or j == k or i == k:
        return 0.0
    return 1.0 if (i, j, k) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1.0


mirror = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]     # det = -1
reflected = [[[0.0] * N for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            reflected[i][j][k] = sum(
                mirror[i][p] * mirror[j][q] * mirror[k][r] * eps(p, q, r)
                for p in range(N) for q in range(N) for r in range(N))
worst = max(abs(reflected[i][j][k] - eps(i, j, k))
            for i in range(N) for j in range(N) for k in range(N))
print(f"  det(mirror) = {det3(mirror):.1f}")
print(f"  max |eps'_ijk - eps_ijk| under the reflection = {worst:.1f}")
print("  A component such as eps_123 comes back as -1: the symbol is not")
print("  invariant under an improper transformation, only under proper ones.")
print("  Objects with this behaviour are called pseudo-tensors; angular")
print("  velocity, and the magnetic field treated as a vector, share it.")

section("6b. Engineering shear strain is not a tensor's component array")

# Scientific strain: a pure xy shear of 0.01.
strain = [[0.0, 0.01, 0.0], [0.01, 0.0, 0.0], [0.0, 0.0, 0.0]]
eng = [row[:] for row in strain]
eng[0][1] = eng[1][0] = 2.0 * strain[0][1]        # engineering convention
show("scientific strain e_ij", strain)
show("engineering array (gamma_xy = 2 e_xy)", eng)

rot45 = rotation([0.0, 0.0, 1.0], math.radians(-45.0))
correct = matmul(matmul(rot45, strain), transpose(rot45))
correct_eng = [row[:] for row in correct]
for i in range(N):
    for j in range(N):
        if i != j:
            correct_eng[i][j] = 2.0 * correct[i][j]
naive = matmul(matmul(rot45, eng), transpose(rot45))
show("rotated by -45 deg about z: CORRECT engineering array", correct_eng)
show("rotated by -45 deg about z: componentwise rotation of the array", naive)
print(f"  largest difference = "
      f"{max(abs(correct_eng[i][j] - naive[i][j]) for i in range(N) for j in range(N)):.4f}")
print("  The raw array cannot be rotated componentwise; only the symmetric")
print("  part with halves on the shear terms obeys the tensor law.")

def second_invariant(m):
    return 0.5 * (trace(m) ** 2 - sum(m[i][j] * m[j][i]
                                      for i in range(N) for j in range(N)))


print(f"\n  I1 of strain = {trace(strain):.6f}   I1 of engineering array = "
      f"{trace(eng):.6f}   (equal: the diagonal is untouched)")
print(f"  I2 of strain = {second_invariant(strain):.6f}   I2 of engineering "
      f"array = {second_invariant(eng):.6f}   (NOT equal: shear is doubled)")
print("  Convention trap: state whether your shear components are e_ij or")
print("  gamma_ij = 2 e_ij before you rotate, invert or build a stiffness.")


# --------------------------------------------------------------------------
# 7. Isotropic tensors
# --------------------------------------------------------------------------

section("7. The Kronecker delta and the isotropic rank-4 tensor")

worst = 0.0
for _ in range(200):
    q = rotation([random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1)],
                 random.uniform(0.0, 2.0 * math.pi))
    d = [[delta(i, j) for j in range(N)] for i in range(N)]
    worst = max(worst, maxdiff(matmul(matmul(q, d), transpose(q)), d))
print(f"  max |Q delta Q^T - delta| over 200 random rotations = {worst:.1e}")
print("  delta_ij has the same components in every frame: it is the one")
print("  rank-2 isotropic tensor (up to a scale factor).")

LAM, MU = 7.0, 3.0


def c_iso(i, j, k, l):
    return (LAM * delta(i, j) * delta(k, l)
            + MU * (delta(i, k) * delta(j, l) + delta(i, l) * delta(j, k)))


worst = 0.0
for _ in range(50):
    q = rotation([random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1)],
                 random.uniform(0.0, 2.0 * math.pi))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    val = sum(q[i][p] * q[j][r] * q[k][s] * q[l][t] * c_iso(p, r, s, t)
                              for p in range(N) for r in range(N)
                              for s in range(N) for t in range(N))
                    worst = max(worst, abs(val - c_iso(i, j, k, l)))
print(f"  max change of C_ijkl = lam dij dkl + mu (dik djl + dil djk) over 50")
print(f"  random rotations: {worst:.1e}")
print("  Two independent constants, and the form is frame-independent. That")
print("  is precisely what an isotropic elastic medium means.")


# --------------------------------------------------------------------------
# 8. Antisymmetric tensors and axial vectors
# --------------------------------------------------------------------------

section("8. W_ij = -eps_ijk w_k: an antisymmetric tensor is a vector in disguise")

W = [[0.0, -1.5, 2.0], [1.5, 0.0, -0.7], [-2.0, 0.7, 0.0]]


def axial(w_):
    return [[-sum(eps(i, j, k) * w_[k] for k in range(N)) for j in range(N)]
            for i in range(N)]


def axial_vector(w_tensor):
    return [-0.5 * sum(eps(i, j, k) * w_tensor[j][k]
                       for j in range(N) for k in range(N)) for i in range(N)]


w = axial_vector(W)
print(f"  W_ij given   = {W[0]}, {W[1]}, {W[2]}")
print(f"  w_i recovered = {[round(x, 8) for x in w]}")
print(f"  max |W_ij - axial(w)_ij| = {maxdiff(W, axial(w)):.1e}")

Wp = matmul(matmul(Q, W), transpose(Q))
wp_direct = matvec(Q, w)
wp_from_tensor = axial_vector(Wp)
print(f"  w from the rotated tensor    = {[round(x, 8) for x in wp_from_tensor]}")
print(f"  Q w                          = {[round(x, 8) for x in wp_direct]}")
print("  Under PROPER rotations the axial vector transforms as a vector.")
print("  Under the reflection of section 6a it does not: that difference is")
print("  exactly the pseudo-tensor property, and it is why angular velocity")
print("  and the magnetic field are handled with care in textbooks.")


def main() -> None:
    print("Tensor transformation laws and invariants, verified numerically")


if __name__ == "__main__":
    main()
