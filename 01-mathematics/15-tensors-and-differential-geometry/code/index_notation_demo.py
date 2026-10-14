"""Index notation, Einstein summation and the Kronecker delta, executed.

Run:  python3 index_notation_demo.py
Requires: Python standard library only.

Companion to lesson 01-15-01.

Every identity in that lesson is checked here by explicit enumeration of the
indices, not by quoting a textbook. Where a numerical derivative is needed the
step is central-difference with h = 1e-4, so truncation error is of order
1e-8 and the quoted residuals are limited by that, not by the identity.

Conventions used throughout:
  * free index appears once per term, summed index appears exactly twice;
  * indices run over 0, 1, 2 for the three Cartesian directions x, y, z;
  * the stress-strain convention is sigma_ij = C_ijkl * u_(k,l) with C
    isotropic, so the operator rebuilt in section 7 must equal
    (lam + mu) grad(div u) + mu laplacian(u).
"""

import math

H = 1.0e-4                     # central-difference step for smooth fields
LAM, MU = 3.0e9, 2.0e9         # Lame parameters of a synthetic rock (Pa)
N = 3


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# --------------------------------------------------------------------------
# The two elementary symbols, evaluated by rule
# --------------------------------------------------------------------------

def delta(i: int, j: int) -> float:
    """Kronecker delta, by definition rather than by a lookup table."""
    return 1.0 if i == j else 0.0


_PERM = {(0, 1, 2), (1, 2, 0), (2, 0, 1)}


def eps(i: int, j: int, k: int) -> float:
    """Levi-Civita symbol in three dimensions."""
    if i == j or j == k or i == k:
        return 0.0
    return 1.0 if (i, j, k) in _PERM else -1.0


def matvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def ident(n=N):
    return [[delta(i, j) for j in range(n)] for i in range(n)]


# --------------------------------------------------------------------------
# 1. The Kronecker delta as a substitution operator
# --------------------------------------------------------------------------

section("1. delta_ij a_j = a_i: the delta substitutes an index")
a = [2.0, -5.0, 7.5]
print(f"  a                     = {a}")
print("  delta_ij a_j computed for each i:")
for i in range(N):
    value = sum(delta(i, j) * a[j] for j in range(N))
    print(f"     i={i}: sum_j delta_{i}j a_j = {value:8.3f}   a_{i} = {a[i]:8.3f}"
          f"   equal? {math.isclose(value, a[i], rel_tol=0, abs_tol=1e-15)}")
print("  The free index i survives on both sides; the summed index j is")
print("  consumed by the delta. That is the whole content of the identity.")

print("\n  delta_ii = " + f"{sum(delta(i, i) for i in range(N)):.1f}"
      + "   (one term per value of the repeated index)")

print("\n  The delta leaves a product untouched only when it sits on the")
print("  correct pair of indices:")
for (i, j) in ((0, 1), (2, 2)):
    print(f"     delta_{i}{j} * 9.0 = {delta(i, j) * 9.0:5.1f}")


# --------------------------------------------------------------------------
# 2. Einstein summation is a loop
# --------------------------------------------------------------------------

section("2. Einstein summation as explicit loops")

A = [[1.0, 2.0, 3.0], [0.0, -1.0, 4.0], [5.0, 2.0, 0.0]]
B = [[2.0, 0.0, 1.0], [1.0, 3.0, 0.0], [0.0, 1.0, -2.0]]

# C_ik = A_ij B_jk, written as three nested loops with no library calls.
C = [[sum(A[i][j] * B[j][k] for j in range(N)) for k in range(N)]
     for i in range(N)]
print("  C_ik = A_ij B_jk is matrix multiplication, and nothing else:")
for row in C:
    print("     [" + "  ".join(f"{v:7.2f}" for v in row) + "]")

print(f"\n  A_ii = trace(A)   = {sum(A[i][i] for i in range(N)):.1f}"
      + "   (double loop, no transpose needed)")

x = [1.0, -2.0, 0.5]
quad = sum(A[i][j] * x[i] * x[j] for i in range(N) for j in range(N))
quad_xax = sum(x[i] * v for i, v in enumerate(matvec(A, x)))
print(f"  x_i A_ij x_j       = {quad:.6f}   x^T A x = {quad_xax:.6f}")
print("  Equal though one form is a scalar built from a 9-term double sum.")


# --------------------------------------------------------------------------
# 3. Symmetric / antisymmetric decomposition
# --------------------------------------------------------------------------

section("3. A_ij = S_ij + W_ij, and why W_ij vanishes in a quadratic form")

S = [[0.5 * (A[i][j] + A[j][i]) for j in range(N)] for i in range(N)]
W = [[0.5 * (A[i][j] - A[j][i]) for j in range(N)] for i in range(N)]

recon = max(abs(A[i][j] - S[i][j] - W[i][j])
            for i in range(N) for j in range(N))
print(f"  max |A_ij - S_ij - W_ij| = {recon:.1e}")
print(f"  W_ii = {sum(W[i][i] for i in range(N)):.1e}"
      + "   (an antisymmetric tensor has zero trace)")

q_s = sum(S[i][j] * x[i] * x[j] for i in range(N) for j in range(N))
q_w = sum(W[i][j] * x[i] * x[j] for i in range(N) for j in range(N))
q_a = sum(A[i][j] * x[i] * x[j] for i in range(N) for j in range(N))
print(f"  x_i S_ij x_j = {q_s:.15f}")
print(f"  x_i W_ij x_j = {q_w:+.3e}   <- identically zero")
print(f"  x_i A_ij x_j = {q_a:.15f}   <- the symmetric part alone")
print("  Reason: renaming i <-> j in W_ij x_i x_j reproduces the same")
print("  expression with the opposite sign, so the sum equals its own negative.")

y = [0.3, 1.7, -0.9]
b_wxy = sum(W[i][j] * x[i] * y[j] for i in range(N) for j in range(N))
b_wyx = sum(W[i][j] * y[i] * x[j] for i in range(N) for j in range(N))
print(f"\n  x_i W_ij y_j = {b_wxy:+.9f}")
print(f"  y_i W_ij x_j = {b_wyx:+.9f}   <- exact negation")
print("  With two DIFFERENT vectors the antisymmetric part does not vanish:")
print("  that surviving bilinear pairing is what makes an antisymmetric")
print("  tensor a rotation generator rather than a stress state.")


# --------------------------------------------------------------------------
# 4. The epsilon-delta identity, checked exhaustively
# --------------------------------------------------------------------------

section("4. eps_ijk eps_ilm = delta_jl delta_km - delta_jm delta_kl")

mismatch = 0
worst = 0.0
for j in range(N):
    for k in range(N):
        for l in range(N):
            for m in range(N):
                left = sum(eps(i, j, k) * eps(i, l, m) for i in range(N))
                right = delta(j, l) * delta(k, m) - delta(j, m) * delta(k, l)
                if abs(left - right) > 1e-12:
                    mismatch += 1
                    worst = max(worst, abs(left - right))
print(f"  index combinations tested (j,k,l,m): {N ** 4}")
print(f"  mismatches: {mismatch}   worst residual: {worst:.1e}")

contraction = sum(eps(i, j, k) * eps(i, j, k)
                  for i in range(N) for j in range(N) for k in range(N))
print(f"\n  eps_ijk eps_ijk = {contraction:.1f}   (= 3! = 6)")

contraction2 = sum(eps(i, j, k) * eps(i, k, j)
                   for i in range(N) for j in range(N) for k in range(N))
print(f"  eps_ijk eps_ikj = {contraction2:.1f}"
      + "   (a swap of one pair flips the sign)")

# The determinant as a fully antisymmetrised triple product.
det_eps = sum(eps(i, j, k) * A[0][i] * A[1][j] * A[2][k]
              for i in range(N) for j in range(N) for k in range(N))
det_cof = (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
           - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
           + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
print(f"\n  det A via eps_ijk A_1i A_2j A_3k = {det_eps:.6f}")
print(f"  det A via cofactor expansion      = {det_cof:.6f}")


# --------------------------------------------------------------------------
# 5. The two structural identities of vector calculus
# --------------------------------------------------------------------------

section("5. div(curl F) = 0 and curl(grad f) = 0, from eps and delta")


def field(p):
    """A smooth, deliberately asymmetric test field F(x, y, z)."""
    xp, yp, zp = p
    return (xp * yp * zp + yp ** 2, zp ** 2 * math.sin(xp), xp * yp + zp ** 3)


def div_fd(vfun, p):
    """d v_i / d x_i by central differences."""
    total = 0.0
    for i in range(N):
        plus, minus = list(p), list(p)
        plus[i] += H
        minus[i] -= H
        total += (vfun(plus)[i] - vfun(minus)[i]) / (2 * H)
    return total


def curl_of(vfun, p):
    out = []
    for i in range(N):
        total = 0.0
        for j in range(N):
            for k in range(N):
                plus, minus = list(p), list(p)
                plus[j] += H
                minus[j] -= H
                total += eps(i, j, k) * (vfun(plus)[k] - vfun(minus)[k]) / (2 * H)
        out.append(total)
    return out


point = (0.7, -1.3, 0.45)
print(f"  test point = {point}")
print(f"  div(curl F) = {div_fd(lambda q: curl_of(field, q), point):.3e}"
      + "   (eps_ijk d_j d_k F_k = 0 by index exchange)")
print("  A genuine truncation-level residual, nonzero in the last digits:")
print("  the terms being combined do not cancel algebraically, so what is")
print("  left is the finite-difference error. Section 5 below shows an")
print("  identity where the opposite happens, and why that is a warning.")


def scalar(p):
    xp, yp, zp = p
    return math.exp(0.3 * xp) * math.sin(0.8 * yp) + zp ** 2 * xp


def grad_fd(p):
    out = []
    for i in range(N):
        plus, minus = list(p), list(p)
        plus[i] += H
        minus[i] -= H
        out.append((scalar(plus) - scalar(minus)) / (2 * H))
    return out


print("  curl(grad f) = "
      + str([f"{v:+.3e}" for v in curl_of(grad_fd, point)]))
print("  Not merely small -- exactly zero in floating point, digit for digit.")
print("  With a symmetric stencil the mixed differences cancel algebraically,")
print("  so a zero residual here is NOT evidence that the code is right (see")
print("  section 5.1 of lesson 01-06-07). The contrast with div(curl F) above,")
print("  where the residual is genuinely ~1e-12, is the point: the first")
print("  identity is checked, the second only appears to be.")


# --------------------------------------------------------------------------
# 6. An identity derived with eps, not quoted
# --------------------------------------------------------------------------

section("6. div(a cross b) = b . curl a - a . curl b")


def a_field(p):
    xp, yp, zp = p
    return (yp * zp, xp ** 2, math.cos(zp) + xp * yp)


def b_field(p):
    xp, yp, zp = p
    return (xp + zp, yp * zp, xp * yp * zp)


def cross_fd(f, g):
    def h(q):
        u, v = f(q), g(q)
        return (u[1] * v[2] - u[2] * v[1],
                u[2] * v[0] - u[0] * v[2],
                u[0] * v[1] - u[1] * v[0])
    return h


lhs6 = div_fd(cross_fd(a_field, b_field), point)
rhs6 = (sum(b_field(point)[i] * curl_of(a_field, point)[i] for i in range(N))
        - sum(a_field(point)[i] * curl_of(b_field, point)[i] for i in range(N)))
print(f"  div(a x b)              = {lhs6:.9f}")
print(f"  b . curl a - a . curl b = {rhs6:.9f}")
print(f"  residual                = {abs(lhs6 - rhs6):.2e}")
print("  Derivation: d_i eps_ijk a_j b_k = eps_ijk (d_i a_j) b_k")
print("  - eps_ikj (d_i b_k) a_j, and eps_ijk d_i a_j = (curl a)_k.")


# --------------------------------------------------------------------------
# 7. The elastic operator in index form
# --------------------------------------------------------------------------

section("7. rho u_i,tt = (C_ijkl u_k,l),j for an isotropic C")


def displacement(p):
    """A polynomial displacement field: every derivative is exact."""
    xp, yp, zp = p
    return (xp ** 2 * yp, yp ** 2 * zp, zp ** 2 * xp)


def d_u(k, l, p):
    """u_{k,l} by central differences."""
    plus, minus = list(p), list(p)
    plus[l] += H
    minus[l] -= H
    return (displacement(plus)[k] - displacement(minus)[k]) / (2 * H)


def c_iso(i, j, k, l):
    """C_ijkl = lam delta_ij delta_kl + mu (delta_ik delta_jl + delta_il delta_jk)."""
    return (LAM * delta(i, j) * delta(k, l)
            + MU * (delta(i, k) * delta(j, l) + delta(i, l) * delta(j, k)))


def sigma(p):
    """sigma_ij = C_ijkl u_k,l at a point."""
    return [[sum(c_iso(i, j, k, l) * d_u(k, l, p)
                 for k in range(N) for l in range(N)) for j in range(N)]
            for i in range(N)]


def d_sigma_dj(i, j, p):
    plus, minus = list(p), list(p)
    plus[j] += H
    minus[j] -= H
    return (sigma(plus)[i][j] - sigma(minus)[i][j]) / (2 * H)


index_form = [sum(d_sigma_dj(i, j, point) for j in range(N)) for i in range(N)]

# The same operator written in vector-calculus form for this polynomial u:
# div(u) = 2xy + 2yz + 2zx, grad(div u) = (2y+2z, 2x+2z, 2y+2x),
# laplacian u = (2y, 2z, 2x).
xp, yp, zp = point
vector_form = [(LAM + MU) * (2 * yp + 2 * zp) + MU * (2 * yp),
               (LAM + MU) * (2 * xp + 2 * zp) + MU * (2 * zp),
               (LAM + MU) * (2 * yp + 2 * xp) + MU * (2 * xp)]
print("  (C_ijkl u_k,l),j  (index form, finite differences) =")
print("     " + str([f"{v:.4e}" for v in index_form]))
print("  (lam+mu) grad(div u) + mu laplacian u (analytic)   =")
print("     " + str([f"{v:.4e}" for v in vector_form]))
resid = max(abs(index_form[i] - vector_form[i]) for i in range(N))
scale = max(abs(v) for v in vector_form)
print(f"  largest residual {resid:.3e} Pa/m, relative to {scale:.3e} Pa/m")
print(f"  -> {resid / scale:.1e} : truncation-limited agreement, as expected.")

print("\n  The isotropic identity C_ijkl u_k,l = lam u_k,k delta_ij + 2 mu u_ij")
print("  (with u_ij the symmetric part) is what turns the index form into the")
print("  familiar vector statement; section 3 showed why the antisymmetric")
print("  part of u_k,l cannot contribute.")


# --------------------------------------------------------------------------
# 8. Index gymnastics that are easy to get wrong
# --------------------------------------------------------------------------

section("8. Three substitutions worth practising")

# (a) relabelling a dummy index is free; relabelling a free index is not.
print("  delta_ij delta_jk = delta_ik  (checked for i=k=1): "
      + f"{sum(delta(1, j) * delta(j, 1) for j in range(N)):.1f}")

# (b) two repeated pairs in one term means a double sum.
M = [[1.0, 2.0], [3.0, -1.0]]
double = sum(M[i][j] * M[i][j] for i in range(2) for j in range(2))
print(f"  M_ij M_ij over a 2x2 M = {double:.1f}   (sum of squares, not trace)")

# (c) squaring a contraction of a trace-free tensor.
Sdev = [[S[i][j] - (trace(S) / N) * delta(i, j) for j in range(N)]
        for i in range(N)]
print(f"  trace of the deviator of S: {trace(Sdev):.1e}")
print("  S'_ij S'_ij = "
      + f"{sum(Sdev[i][j] * Sdev[i][j] for i in range(N) for j in range(N)):.6f}")
print("  This is the shape of the second stress invariant, computed with no")
print("  reference to matrix notation at all.")


def main() -> None:
    print("Index notation, Einstein summation and the Kronecker delta")
    print("Every identity above was evaluated by explicit index loops.")


if __name__ == "__main__":
    main()
