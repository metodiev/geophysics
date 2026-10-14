"""Mantle convection: Rayleigh number and Rayleigh-Benard stability.

Run:  python3 mantle_convection_demo.py
Requires: Python standard library only.

Companion to lesson 02-06-06. The script:

1. Computes the mantle Rayleigh number Ra = rho g alpha dT d^3 / (kappa eta)
   from stated nominal inputs, prints every factor so the result can be
   checked by hand, and shows how Ra moves when the inputs move.
2. Computes the critical Rayleigh number for Rayleigh-Benard convection with
   stress-free boundaries by an independent numerical route: the linear
   stability operator (D^2 - a^2)^3 is discretised with finite differences,
   its eigenvalues are found with a Jacobi solver, and the minimum over the
   horizontal wavenumber a is found. The result is compared with the exact
   value 27 pi^4 / 4.
3. Computes the critical Rayleigh number for rigid (no-slip) boundaries from
   the biharmonic operator D^4 - 2 a^2 D^2 + a^4 with clamped boundary
   conditions, by the same eigen-solver and the same scan over a, and reports
   the grid convergence.
4. Converts the supercriticality to a boundary-layer thickness, a convective
   velocity and a Nusselt-number estimate, using scalings stated in the
   lesson, and computes the corresponding thermal-boundary-layer Rayleigh
   number.

Every number printed below was produced by this script. The viscosity,
thermal expansivity and temperature drop are nominal inputs, not measurements
of the present-day mantle, and the Ra which follows is therefore nominal too.
"""

import math

# Nominal inputs (handbook Sec. 3.4 and Sec. 3.3 unless noted).
RHO_MANTLE = 3300.0      # kg/m^3, uppermost mantle, nominal
G = 9.81                 # m/s^2, nominal surface gravity
ALPHA = 3.0e-5           # 1/K, thermal expansivity of mantle rock, nominal
DT = 2500.0              # K, temperature drop across the mantle, nominal
D_MANTLE = 2.891e6       # m, mantle thickness (base of the mantle, handbook)
KAPPA = 1.0e-6           # m^2/s, thermal diffusivity, nominal
ETA = 1.0e21             # Pa s, dynamic viscosity, nominal


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# ----------------------------------------------------------------------
# Linear algebra helpers (standard library only)
# ----------------------------------------------------------------------

def matmul(A, B):
    n = len(A)
    m = len(B[0])
    k = len(B)
    out = [[0.0] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Oi = out[i]
        for t in range(k):
            a = Ai[t]
            if a == 0.0:
                continue
            Bt = B[t]
            for j in range(m):
                Oi[j] += a * Bt[j]
    return out


def jacobi_eig(A, tol=1e-13, max_sweeps=60, want_vectors=False):
    """Eigen-decomposition of a real symmetric matrix by cyclic Jacobi.

    Returns the sorted eigenvalues, or (values, vectors) when want_vectors is
    True. Eigenvectors are the columns of the returned matrix.
    """
    n = len(A)
    a = [row[:] for row in A]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_sweeps):
        off = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                off += a[i][j] * a[i][j]
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                apq = a[p][q]
                if abs(apq) < 1e-300:
                    continue
                theta = 0.5 * math.atan2(2.0 * apq, a[q][q] - a[p][p])
                c = math.cos(theta)
                s = math.sin(theta)
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p] = c * akp - s * akq
                    a[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k] = c * apk - s * aqk
                    a[q][k] = s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = v[k][p], v[k][q]
                    v[k][p] = c * vkp - s * vkq
                    v[k][q] = s * vkp + c * vkq
    vals = [a[i][i] for i in range(n)]
    order = sorted(range(n), key=lambda i: vals[i])
    if not want_vectors:
        return [vals[i] for i in order]
    vecs = [[v[i][j] for j in order] for i in range(n)]
    return [vals[i] for i in order], vecs


def sqrt_psd(A):
    """Matrix square root of a symmetric positive-definite matrix."""
    n = len(A)
    vals, vecs = jacobi_eig(A, want_vectors=True)
    # vecs columns are eigenvectors; A = V diag(vals) V^T
    roots = [math.sqrt(max(val, 0.0)) for val in vals]
    out = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            acc = 0.0
            for k in range(n):
                acc += vecs[i][k] * roots[k] * vecs[j][k]
            out[i][j] = acc
    return out


def d2_dirichlet(n, h):
    """Second-derivative matrix on interior points with psi = 0 at both ends."""
    A = [[0.0] * n for _ in range(n)]
    inv = 1.0 / (h * h)
    for i in range(n):
        A[i][i] = -2.0 * inv
        if i > 0:
            A[i][i - 1] = inv
        if i < n - 1:
            A[i][i + 1] = inv
    return A


def d4_clamped(n, h):
    """Fourth-derivative matrix on interior points with psi = D psi = 0."""
    A = [[0.0] * n for _ in range(n)]
    inv = 1.0 / (h ** 4)
    for i in range(n):
        if i == 0:
            A[i][i] = 7.0 * inv
            A[i][i + 1] = -4.0 * inv
            if n > 2:
                A[i][i + 2] = 1.0 * inv
        elif i == 1:
            A[i][i - 1] = -4.0 * inv
            A[i][i] = 6.0 * inv
            A[i][i + 1] = -4.0 * inv
            A[i][i + 2] = 1.0 * inv
        elif i == n - 2:
            A[i][i - 2] = 1.0 * inv
            A[i][i - 1] = -4.0 * inv
            A[i][i] = 6.0 * inv
            A[i][i + 1] = -4.0 * inv
        elif i == n - 1:
            A[i][i] = 7.0 * inv
            A[i][i - 1] = -4.0 * inv
            if n > 2:
                A[i][i - 2] = 1.0 * inv
        else:
            A[i][i - 2] = 1.0 * inv
            A[i][i - 1] = -4.0 * inv
            A[i][i] = 6.0 * inv
            A[i][i + 1] = -4.0 * inv
            A[i][i + 2] = 1.0 * inv
    return A


def shifted(A, s):
    n = len(A)
    return [[A[i][j] + (s if i == j else 0.0) for j in range(n)]
            for i in range(n)]


def ra_profile_free_slip(n, h, a_grid):
    """Ra(a) for stress-free boundaries: (D^2 - a^2)^3 psi = -Ra a^2 psi."""
    D2 = d2_dirichlet(n, h)
    out = []
    for a in a_grid:
        M = matmul(matmul(shifted(D2, -a * a), shifted(D2, -a * a)),
                   shifted(D2, -a * a))
        eigs = jacobi_eig(M)                      # all negative
        Ra = -max(eigs) / (a * a)                 # least-negative eigenvalue
        out.append((a, Ra))
    return out


def ra_profile_rigid(n, h, a_grid):
    """Ra(a) for no-slip boundaries.

    The linearised equations (D^2-a^2)^2 W = Ra a^2 Theta and
    (D^2-a^2) Theta = -W, with W = DW = 0 and Theta = 0, give
    Theta = -(D^2-a^2)^(-1) W and hence (-(D^2-a^2)) B W = Ra a^2 W, where
    B = (D^2-a^2)^2 with clamped boundary conditions. The product is
    symmetrised as P^(1/2) B P^(1/2) with P = a^2 - D^2 (positive definite),
    and Ra is the smallest positive eigenvalue divided by a^2.
    """
    D2 = d2_dirichlet(n, h)
    D4 = d4_clamped(n, h)
    out = []
    for a in a_grid:
        a2 = a * a
        P = shifted([[-D2[i][j] for j in range(n)] for i in range(n)], a2)
        Ps = sqrt_psd(P)
        B = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                B[i][j] = D4[i][j] - 2.0 * a2 * D2[i][j] + (a2 * a2 if i == j else 0.0)
        S = matmul(matmul(Ps, B), Ps)
        vals = jacobi_eig(S)
        lam = min((x for x in vals if x > 1e-6), default=None)
        if lam is not None:
            out.append((a, lam / a2))
    return out


def parabolic_minimum(points):
    """Vertex of the parabola through three (x, y) points, y concave up."""
    (x1, y1), (x2, y2), (x3, y3) = points
    num = (x2 - x1) ** 2 * (y2 - y3) - (x2 - x3) ** 2 * (y2 - y1)
    den = (x2 - x1) * (y2 - y3) - (x2 - x3) * (y2 - y1)
    if den == 0.0:
        return x2, y2
    xv = x2 - 0.5 * num / den
    yv = (y1 * (xv - x2) * (xv - x3) / ((x1 - x2) * (x1 - x3))
          + y2 * (xv - x1) * (xv - x3) / ((x2 - x1) * (x2 - x3))
          + y3 * (xv - x1) * (xv - x2) / ((x3 - x1) * (x3 - x2)))
    return xv, yv


# ----------------------------------------------------------------------
# 1. The mantle Rayleigh number
# ----------------------------------------------------------------------

def part1_ra():
    section("1. Rayleigh number of the mantle")

    print("Ra = rho g alpha dT d^3 / (kappa eta)\n")
    factors = [
        ("rho (kg/m^3)", RHO_MANTLE),
        ("g (m/s^2)", G),
        ("alpha (1/K)", ALPHA),
        ("dT (K)", DT),
        ("d (m)", D_MANTLE),
        ("d^3 (m^3)", D_MANTLE ** 3),
        ("kappa (m^2/s)", KAPPA),
        ("eta (Pa s)", ETA),
    ]
    for name, value in factors:
        print(f"  {name:>16} = {value:.6g}")
    num = RHO_MANTLE * G * ALPHA * DT * D_MANTLE ** 3
    den = KAPPA * ETA
    Ra = num / den
    print(f"\n  numerator   = {num:.6e}")
    print(f"  denominator = {den:.6e}")
    print(f"  Ra          = {Ra:.6e}")
    print(f"  log10 Ra    = {math.log10(Ra):.4f}")

    print("\nsensitivity to the least well known input, eta (all others fixed):")
    print(f"{'eta (Pa s)':>13} {'Ra':>13} {'log10 Ra':>10}")
    for eta in (1.0e19, 1.0e20, 1.0e21, 1.0e22):
        Ra_ = RHO_MANTLE * G * ALPHA * DT * D_MANTLE ** 3 / (KAPPA * eta)
        print(f"{eta:13.0e} {Ra_:13.4e} {math.log10(Ra_):10.4f}")
    print("  two orders of magnitude in eta move Ra by two orders of magnitude;")
    print("  the mantle viscosity is the dominant uncertainty. The value ~1e21")
    print("  is a nominal reference viscosity, not a measurement of one rock.")


# ----------------------------------------------------------------------
# 2. Critical Rayleigh number, free-slip
# ----------------------------------------------------------------------

def part2_ra_critical_free():
    section("2. Critical Rayleigh number, stress-free boundaries")

    print("exact: (n^2 pi^2 + a^2)^3 = Ra a^2  ->  Ra(a) = (pi^2+a^2)^3/a^2 "
          "(n = 1)")
    # minimise the analytic curve by ternary search on a
    lo, hi = 1.0, 4.0
    for _ in range(200):
            m1 = lo + (hi - lo) / 3.0
            m2 = hi - (hi - lo) / 3.0
            f1 = (math.pi ** 2 + m1 * m1) ** 3 / (m1 * m1)
            f2 = (math.pi ** 2 + m2 * m2) ** 3 / (m2 * m2)
            if f1 < f2:
                hi = m2
            else:
                lo = m1
    a_min = 0.5 * (lo + hi)
    ra_min = (math.pi ** 2 + a_min ** 2) ** 3 / (a_min ** 2)
    print(f"  ternary-search minimum: a_c = {a_min:.6f}, "
              f"Ra_c = {ra_min:.6f}")
    print(f"  analytic predictions:    a_c = pi/sqrt(2) = "
              f"{math.pi / math.sqrt(2):.6f}, Ra_c = 27 pi^4 / 4 = "
              f"{27 * math.pi ** 4 / 4:.6f}")

    print("\nindependent finite-difference eigen-solution of "
              "(D^2-a^2)^3 psi = -Ra a^2 psi, minimum located by a parabola "
              "through three points")
    ac = math.pi / math.sqrt(2)
    a_grid = [ac - 0.2, ac - 0.1, ac, ac + 0.1, ac + 0.2]
    for N in (20, 40, 80):
            h = 1.0 / N
            prof = ra_profile_free_slip(N - 1, h, a_grid)
            xv, yv = parabolic_minimum(prof[1:4])
            print(f"  N = {N:3d} (interior {N - 1:3d}): a_c ~ {xv:.4f}, "
                  f"Ra_c ~ {yv:.3f}   (error {yv - 27 * math.pi ** 4 / 4:+.3f})")
    print("  the finite-difference values rise toward the exact value "
              "27 pi^4 / 4 = 657.511")
    print("  as the grid is refined, and a_c is recovered near pi/sqrt(2) = "
              "2.2214. The")
    print("  remaining error is the discretisation of a sixth-order operator, "
              "which is why")
    print("  it falls only as h^2 and why the coarse N = 20 value is 0.4 per "
              "cent low.")


def part3_ra_critical_rigid():
    section("3. Critical Rayleigh number, rigid (no-slip) boundaries")

    print("finite-difference eigen-solution of the coupled linearised system")
    print("  (D^2-a^2)^2 W = Ra a^2 Theta,  (D^2-a^2) Theta = -W,")
    print("  W = DW = 0 and Theta = 0 at z = 0, 1")
    ac = 3.1                              # expected location of the minimum
    a_grid = [ac - 0.2, ac - 0.1, ac, ac + 0.1, ac + 0.2]
    for N in (40, 60):
            h = 1.0 / N
            prof = ra_profile_rigid(N - 1, h, a_grid)
            xv, yv = parabolic_minimum(prof[1:4])
            print(f"  N = {N:3d} (interior {N - 1:3d}): a_c ~ {xv:.4f}, "
                  f"Ra_c ~ {yv:.3f}")
    print("\n  the values rise toward about 1707.8 as the grid is refined, "
              "and a_c is")
    print("  recovered near 3.12. Rigid boundaries are more restrictive than")
    print("  stress-free ones, so Ra_c is larger: about 1708 against 657.5. "
              "The classical")
    print("  small-amplitude stability analysis gives 1707.76 and a_c = 3.117 "
              "for rigid")
    print("  boundaries (Chandrasekhar 1961); the numbers above are an "
              "independent")
    print("  numerical reproduction of that result to better than 0.5 per cent "
              "at N = 60.")
    print("  both critical values are far below the mantle Ra of section 1, "
              "which is why")
    print("  the mantle convects, and why it does so in a time-dependent, "
              "three-dimensional")
    print("  manner rather than as a single steady roll.")


# ----------------------------------------------------------------------
# 4. Consequences of the supercriticality
# ----------------------------------------------------------------------

def part4_consequences():
    section("4. What the supercriticality implies")

    Ra = RHO_MANTLE * G * ALPHA * DT * D_MANTLE ** 3 / (KAPPA * ETA)
    Ra_c = 27 * math.pi ** 4 / 4
    ratio = Ra / Ra_c
    print(f"  Ra / Ra_c = {Ra:.3e} / {Ra_c:.3f} = {ratio:.3e}")

    # Thermal boundary-layer thickness. The definition delta ~ d Ra^(-1/3)
    # makes the local Rayleigh number identically 1, which is a consistency
    # check and nothing more.
    delta = D_MANTLE * Ra ** (-1.0 / 3.0)
    Ra_delta = RHO_MANTLE * G * ALPHA * DT * delta ** 3 / (KAPPA * ETA)
    print(f"  delta ~ d Ra^(-1/3) = {delta / 1e3:.1f} km; the local Rayleigh "
          f"number of that")
    print(f"  layer is Ra_delta = {Ra_delta:.6f}, i.e. exactly 1 by "
          "construction. That is an")
    print("  identity, not a result: this scaling cannot be used as a test of "
          "itself.")

    # Marginal-stability version: choose the layer that is itself marginally
    # unstable, Ra_delta = Ra_c.
    delta_c = D_MANTLE * (Ra_c / Ra) ** (1.0 / 3.0)
    Ra_delta_c = RHO_MANTLE * G * ALPHA * DT * delta_c ** 3 / (KAPPA * ETA)
    print(f"\n  imposing local marginal stability, Ra_delta = Ra_c, gives")
    print(f"  delta_c = d (Ra_c/Ra)^(1/3) = {delta_c / 1e3:.1f} km with "
          f"Ra_delta_c = {Ra_delta_c:.3f}")
    print("  the two definitions differ by the factor Ra_c^(1/3) = "
          f"{Ra_c ** (1.0 / 3.0):.2f}. A 'boundary-layer thickness' is only")
    print("  meaningful once the definition is stated.")

    # Velocity scale from the boundary-layer balance.
    u = KAPPA / D_MANTLE * Ra ** (2.0 / 3.0)
    print(f"\n  velocity scale u ~ (kappa/d) Ra^(2/3) = {u:.3e} m/s "
          f"= {u * 3.1557e7 * 100:.2f} cm/yr")
    print("  observed plate speeds are of order 1-10 cm/yr (a nominal range, "
          "not a single")
    print("  number), so this scaling overpredicts by roughly a factor of 30. "
          "That is the")
    print("  expected failure: the scaling assumes a constant viscosity and "
          "ignores the")
    print("  lithosphere, the temperature dependence of eta and the "
          "internal-heating profile.")
    print("  the value of the exercise is that Ra^(2/3) lands within a factor "
          "of a few tens,")
    print("  which is what a scaling argument can promise; it is not a "
          "prediction of any plate.")

    # Nusselt number scaling.
    Nu = 0.1 * Ra ** (1.0 / 3.0)
    print(f"\n  Nusselt estimate Nu ~ 0.1 Ra^(1/3) = {Nu:.1f}")
    print(f"  surface heat flow from this Nu, q = Nu k dT/d (k = 2.5 W/m/K "
          "nominal):")
    k_rock = 2.5
    q = Nu * k_rock * DT / D_MANTLE
    print(f"    q = {q * 1e3:.1f} mW/m^2")
    print("  the handbook gives continental surface heat flow ~65 mW/m^2 and "
          "oceanic")
    print("  ~100 mW/m^2 (nominal, Sec. 3.4), so the scaling is in the right "
          "range.")
    print("  the coefficient 0.1 in the Nu scaling is an empirical fit and "
          "must not be quoted")
    print("  as if it were a law; the exponent 1/3 is the boundary-layer "
          "scaling.")


def main():
    part1_ra()
    part2_ra_critical_free()
    part3_ra_critical_rigid()
    part4_consequences()


if __name__ == "__main__":
    main()
