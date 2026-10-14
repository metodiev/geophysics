"""Stress and strain as physical tensors: decomposition, invariants, eigen-axes.

Run:  python3 stress_strain_demo.py
Requires: Python standard library only.

Companion to lesson 01-15-03.

Sign convention, stated once and used everywhere below: TENSION POSITIVE, so
the traction on a plane with unit normal n is t_i = sigma_ij n_j and a positive
principal stress pulls the face outwards. Many rock-mechanics and seismology
texts use compression positive instead; section 7 shows exactly what changes
(all first-rank quantities flip sign, all quadratic invariants do not) so that
you can convert between the two without rewriting the physics.

Strain convention: e_ij = 1/2 (u_i,j + u_j,i) is used throughout, i.e. the
SCIENTIFIC shear strain. The engineering shear strain gamma_ij = 2 e_ij
(i != j) is used only where it is explicitly named.
"""

import math
import random

N = 3
random.seed(7)


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def delta(i, j):
    return 1.0 if i == j else 0.0


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


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm(v):
    return math.sqrt(dot(v, v))


def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def jacobi_eig(a, tol=1e-15, sweeps=100):
    """Cyclic Jacobi eigen-decomposition of a real symmetric matrix."""
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
        print("     [" + "  ".join(f"{x:>{9 + places}.{places}f}" for x in row) + "]")


# --------------------------------------------------------------------------
# 1. A stress state and its principal values
# --------------------------------------------------------------------------

section("1. Principal stresses, mean stress and the three invariants")

SIG = [[100.0, 25.0, -10.0], [25.0, 60.0, 5.0], [-10.0, 5.0, 40.0]]   # MPa
show("sigma (MPa, tension positive)", SIG)

pvals, pdirs = jacobi_eig(SIG)
print(f"  principal stresses (ascending) = "
      f"{[f'{x:.6f}' for x in pvals]} MPa")
print(f"  mean stress p = tr(sigma)/3    = {trace(SIG) / 3.0:.6f} MPa")
print(f"  I1 = tr sigma                  = {trace(SIG):.6f} MPa")
print(f"  I2 = 1/2[(tr sigma)^2 - tr sigma^2] = "
      f"{0.5 * (trace(SIG) ** 2 - sum(SIG[i][j] * SIG[j][i] for i in range(N) for j in range(N))):.6f} MPa^2")
print(f"  I3 = det sigma                  = {det3(SIG):.6f} MPa^3")
print(f"  check: sum of principal stresses = {sum(pvals):.6f} MPa = I1")
print(f"  check: product of principal stresses = {pvals[0] * pvals[1] * pvals[2]:.6f} MPa^3 = I3")
print("  The three invariants are the only stress information that a change of")
print("  coordinate frame cannot touch; everything else is orientation.")


# --------------------------------------------------------------------------
# 2. Traction, normal and shear stress, and the maximum shear
# --------------------------------------------------------------------------

section("2. Traction on a plane, and the planes that maximise shear")


def traction(sigma, n):
    return matvec(sigma, n)


n = [0.36, 0.48, 0.8]
t = traction(SIG, n)
sigma_n = dot(t, n)
tau_vec = [t[i] - sigma_n * n[i] for i in range(N)]
print(f"  n = {n}, |n| = {norm(n):.12f}")
print(f"  t = sigma n            = {[f'{x:.6f}' for x in t]} MPa")
print(f"  normal stress t.n      = {sigma_n:.6f} MPa")
print(f"  shear stress |t - (t.n)n| = {norm(tau_vec):.6f} MPa")
print(f"  identity check |t|^2 = sigma_n^2 + tau^2: "
      f"{dot(t, t):.10f} vs {sigma_n ** 2 + norm(tau_vec) ** 2:.10f}")

best = 0.0
best_n = None
for _ in range(400000):
    cand = [random.gauss(0, 1) for _ in range(N)]
    ln = norm(cand)
    cand = [c / ln for c in cand]
    tt = traction(SIG, cand)
    sn = dot(tt, cand)
    tau = math.sqrt(max(0.0, dot(tt, tt) - sn * sn))
    if tau > best:
        best, best_n = tau, cand
predicted = 0.5 * (pvals[2] - pvals[0])
print(f"\n  random search over 400000 normals: max shear = {best:.6f} MPa")
print(f"  exact result (sigma_1 - sigma_3)/2          = {predicted:.6f} MPa")
print(f"  at n = {[f'{x:.4f}' for x in best_n]}")
bisector = [pdirs[2][i] + pdirs[0][i] for i in range(N)]
bisector = [c / norm(bisector) for c in bisector]
print(f"  bisector of the sigma_1 and sigma_3 principal directions = "
      f"{[f'{x:.4f}' for x in bisector]}")
print("  The maximising normal is the bisector, as the eigenvalue solution")
print("  requires: shear cannot exceed half the principal stress difference.")


# --------------------------------------------------------------------------
# 3. Hydrostatic / deviatoric split
# --------------------------------------------------------------------------

section("3. sigma_ij = p delta_ij + s_ij: what the split buys")

ph = trace(SIG) / 3.0
dev = [[SIG[i][j] - ph * delta(i, j) for j in range(N)] for i in range(N)]
show("deviatoric stress s_ij (MPa)", dev, places=6)
print(f"  tr s            = {trace(dev):.2e}   (trace-free by construction)")
print(f"  J2 = 1/2 s_ij s_ij = "
      f"{0.5 * sum(dev[i][j] * dev[i][j] for i in range(N) for j in range(N)):.6f} MPa^2")
print(f"  equivalent shear stress sqrt(3 J2) = "
      f"{math.sqrt(3 * 0.5 * sum(dev[i][j] * dev[i][j] for i in range(N) for j in range(N))):.6f} MPa")
print(f"  second invariant of s, I2(s) = "
      f"{0.5 * (trace(dev) ** 2 - sum(dev[i][j] * dev[j][i] for i in range(N) for j in range(N))):.6f} MPa^2")
print("  For a trace-free tensor I2 = -J2 exactly, so von Mises stress and the")
print("  second invariant are the same measurement written two ways.")

pvals_dev = jacobi_eig(dev)[0]
print(f"\n  principal deviatoric stresses = {[f'{x:.6f}' for x in pvals_dev]}")
print(f"  pvals - mean (same numbers)   = {[f'{x - ph:.6f}' for x in pvals]}")

print("\n  Why the split matters: at 2600 kg/m^3 a 1 km column of rock weighs")
print("  about 25.5 MPa, so the pressure at 40 km depth is roughly 1 GPa, while")
print("  the deviatoric stress that drives brittle failure is of order 10-100")
print("  MPa. Yielding criteria are written in s_ij, not in sigma_ij, for that")
print("  reason.")


# --------------------------------------------------------------------------
# 4. Mohr's circle in two dimensions
# --------------------------------------------------------------------------

section("4. Mohr's circle, derived from the transformation law")

a, b, cxy = SIG[0][0], SIG[1][1], SIG[1][0]
centre = 0.5 * (a + b)
radius = math.sqrt((0.5 * (a - b)) ** 2 + cxy ** 2)
block2d = jacobi_eig([[a, cxy, 0.0], [cxy, b, 0.0], [0.0, 0.0, 0.0]])[0]
print(f"  2-D block (sigma_xx, sigma_yy, sigma_xy) = ({a}, {b}, {cxy}) MPa")
print(f"  centre  (sigma_xx + sigma_yy)/2          = {centre:.6f} MPa")
print(f"  radius  sqrt[((a-b)/2)^2 + tau_xy^2]     = {radius:.6f} MPa")
print(f"  principal stresses from the circle       = "
      f"{centre - radius:.6f}, {centre + radius:.6f} MPa")
print(f"  from the 3x3 eigenproblem restricted to xy = "
      f"{block2d[1]:.6f}, {block2d[2]:.6f} MPa  (the third is {block2d[0]:.6f})")

print("\n  The circle is the graph of the transformation law: for a plane whose")
print("  normal is at angle phi to the x axis,")
worst = 0.0
for deg in range(0, 181, 5):
    phi = math.radians(deg)
    nn = [math.cos(phi), math.sin(phi), 0.0]
    tt = matvec([[a, cxy, 0.0], [cxy, b, 0.0], [0.0, 0.0, 0.0]], nn)
    sn = dot(tt, nn)
    tau = math.sqrt(max(0.0, dot(tt, tt) - sn * sn))
    worst = max(worst, abs((sn - centre) ** 2 + tau ** 2 - radius ** 2))
print(f"     (sigma_n - centre)^2 + tau^2 = radius^2 for every phi;")
print(f"     largest departure over 37 angles = {worst:.3e} MPa^2")
print(f"     symmetry: the state at phi and at phi + 90 deg gives the same tau,")
print("     opposite normal-stress deviation from the centre.")


# --------------------------------------------------------------------------
# 5. Strain from a displacement field
# --------------------------------------------------------------------------

section("5. e_ij and omega_ij from a displacement gradient")

H = 1.0e-6


def displacement(p):
    x, y, z = p
    return (1e-3 * (x + 2 * y * z),
            1e-3 * (x * z + 3 * y),
            1e-3 * (2 * x * y + z))


def grad_u(p):
    out = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            plus, minus = list(p), list(p)
            plus[j] += H
            minus[j] -= H
            out[i][j] = (displacement(plus)[i] - displacement(minus)[i]) / (2 * H)
    return out


point = (2.0, -1.0, 3.0)
G = grad_u(point)
show("u_i,j at (2, -1, 3)", G, places=6)

E = [[0.5 * (G[i][j] + G[j][i]) for j in range(N)] for i in range(N)]
OM = [[0.5 * (G[i][j] - G[j][i]) for j in range(N)] for i in range(N)]
show("e_ij = 1/2 (u_i,j + u_j,i)", E, places=6)
show("omega_ij = 1/2 (u_i,j - u_j,i)", OM, places=6)
print(f"  max |G - (E + omega)| = "
      f"{max(abs(G[i][j] - E[i][j] - OM[i][j]) for i in range(N) for j in range(N)):.1e}")
print(f"  tr e = {trace(E):.6f}   (dilatation; volume change per unit volume)")
print(f"  engineering shear strains gamma_ij = 2 e_ij: "
      f"gamma_xy = {2 * E[0][1]:.6f}, gamma_xz = {2 * E[0][2]:.6f}, "
      f"gamma_yz = {2 * E[1][2]:.6f}")


# --------------------------------------------------------------------------
# 6. Rigid rotation produces no strain
# --------------------------------------------------------------------------

section("6. A rigid-body rotation strains nothing")

OMEGA = [0.0, 0.0, 1.2e-3]          # rad/s


def rigid(p):
    return [sum(( [[0.0, -OMEGA[2], 0.0], [OMEGA[2], 0.0, 0.0], [0.0, 0.0, 0.0]][i][j]
                  * p[j]) for j in range(N)) for i in range(N)]


G2 = [[0.0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        plus, minus = list(point), list(point)
        plus[j] += H
        minus[j] -= H
        G2[i][j] = (rigid(plus)[i] - rigid(minus)[i]) / (2 * H)
E2 = [[0.5 * (G2[i][j] + G2[j][i]) for j in range(N)] for i in range(N)]
print(f"  max |e_ij| for a rigid rotation = "
      f"{max(abs(E2[i][j]) for i in range(N) for j in range(N)):.1e}")
print(f"  the non-zero part is omega_xy = {G2[0][1]:.6e} rad/s "
      f"(=-Omega_z, as the axial-vector correspondence requires)")
print("  Strain measures shape change; rotation is split off automatically by")
print("  taking the symmetric part, which is why the split is not cosmetic.")


# --------------------------------------------------------------------------
# 7. The length-change identity and the sign convention
# --------------------------------------------------------------------------

section("7. dl'^2 - dl^2 = 2 e_ij dl_i dl_j, and the sign convention")

dx = [1.0, -2.0, 0.5]
for factor in (1.0, 0.1, 0.01):
    es = [[factor * E[i][j] for j in range(N)] for i in range(N)]
    d = list(dx)
    moved = [sum(es[i][j] * d[j] for j in range(N)) for i in range(N)]
    before = dot(d, d)
    after = dot([d[i] + moved[i] for i in range(N)], [d[i] + moved[i] for i in range(N)])
    rhs = 2.0 * sum(es[i][j] * d[i] * d[j] for i in range(N) for j in range(N))
    print(f"  strain scaled by {factor:5.2f}:  dl'^2 - dl^2 = {after - before:.12e},"
          f"  2 e_ij dl_i dl_j = {rhs:.12e},"
          f"  relative difference = {abs((after - before) - rhs) / abs(rhs):.1e}")
print("  The identity is exact only to first order in the strain, so the")
print("  relative remainder falls in proportion to the strain magnitude.")
print("  (It does NOT depend on |dl| at fixed e: both sides are quadratic.)")
print("  The strain is dimensionless: u is in metres and so is x, with the")
print(f"  largest component of u_i,j equal to "
      f"{max(abs(G[i][j]) for i in range(N) for j in range(N)):.1e}.")

flipped = [[-SIG[i][j] for j in range(N)] for i in range(N)]
pvals_flip = jacobi_eig(flipped)[0]
print(f"\n  Compression-positive convention: sigma -> -sigma")
print(f"    principal stresses {[f'{x:.4f}' for x in pvals]} -> "
      f"{[f'{x:.4f}' for x in pvals_flip]}")
print(f"    mean stress {trace(SIG) / 3.0:.4f} -> {trace(flipped) / 3.0:.4f} MPa")
print(f"    max shear magnitude unchanged: {0.5 * (pvals[2] - pvals[0]):.4f} -> "
      f"{0.5 * (pvals_flip[2] - pvals_flip[0]):.4f} MPa")
print(f"    I2 unchanged: "
      f"{0.5 * (trace(SIG) ** 2 - sum(SIG[i][j] * SIG[j][i] for i in range(N) for j in range(N))):.4f}"
      f" -> "
      f"{0.5 * (trace(flipped) ** 2 - sum(flipped[i][j] * flipped[j][i] for i in range(N) for j in range(N))):.4f}")
print("    (I2 is quadratic in the components, so flipping every component")
print("     leaves it alone; I1 and I3 flip sign.)")


# --------------------------------------------------------------------------
# 8. Compatibility
# --------------------------------------------------------------------------

section("8. Compatibility: not every symmetric array is a strain field")


def strain_field(p):
    return [[0.5 * (grad_u(p)[i][j] + grad_u(p)[j][i]) for j in range(N)]
            for i in range(N)]


def d2(field, i, j, k, l, p):
    """Second derivative (field_ij),kl by a four-point central stencil."""
    def f(q):
        return field(q)[i][j]
    pp = list(p); pp[k] += H; pp[l] += H
    pm = list(p); pm[k] += H; pm[l] -= H
    mp = list(p); mp[k] -= H; mp[l] += H
    mm = list(p); mm[k] -= H; mm[l] -= H
    return (f(pp) - f(pm) - f(mp) + f(mm)) / (4.0 * H * H)


worst = 0.0
scale = 0.0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                val = (d2(strain_field, i, j, k, l, point)
                       + d2(strain_field, k, l, i, j, point)
                       - d2(strain_field, i, k, j, l, point)
                       - d2(strain_field, j, l, i, k, point))
                worst = max(worst, abs(val))
                scale = max(scale, abs(d2(strain_field, i, j, k, l, point)))
print(f"  strain from a displacement field: max |compatibility residual| = {worst:.3e}")
print(f"  scale of the second derivatives involved                      = {scale:.3e}")
print("  Zero to every printed digit: with this symmetric stencil the mixed")
print("  differences cancel algebraically, so the check confirms the algebra")
print("  but would not catch a coding error. The next case is the honest test.")


def bad_field(p):
    x, y, _ = p
    return [[y * y, 0.0, 0.0], [0.0, x * x, 0.0], [0.0, 0.0, 0.0]]


worst = 0.0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                val = (d2(bad_field, i, j, k, l, point)
                       + d2(bad_field, k, l, i, j, point)
                       - d2(bad_field, i, k, j, l, point)
                       - d2(bad_field, j, l, i, k, point))
                worst = max(worst, abs(val))
print(f"\n  e_xx = y^2, e_yy = x^2, all other components zero:")
print(f"    max |compatibility residual| = {worst:.6f}")
print("    The incompatible combination (x,y,x,y) gives e_xx,yy + e_yy,xx =")
print("    2 + 2 = 4, with no compensating shear term, so no displacement")
print("    field can produce this array. It describes a state the continuum")
print("    cannot reach, and any finite-element solution imposing it must fail.")


# --------------------------------------------------------------------------
# 9. Hooke's law and the volumetric/deviatoric response
# --------------------------------------------------------------------------

section("9. sigma_ij = lambda e_kk delta_ij + 2 mu e_ij")

LAM, MU = 30.0e9, 20.0e9        # Pa
E_SMALL = [[2.0e-4, 2.0e-4, 0.0], [2.0e-4, -3.0e-4, 1.0e-4], [0.0, 1.0e-4, 2.0e-4]]


def hooke(e):
    tr = trace(e)
    return [[LAM * tr * delta(i, j) + 2.0 * MU * e[i][j] for j in range(N)]
            for i in range(N)]


SIGMA = hooke(E_SMALL)
show("e (dimensionless)", E_SMALL, places=6)
show("sigma = lambda tr(e) I + 2 mu e (MPa)", [[x / 1e6 for x in row] for row in SIGMA], places=6)
print(f"  tr sigma = (3 lambda + 2 mu) tr e = "
      f"{(3 * LAM + 2 * MU) * trace(E_SMALL) / 1e6:.6f} MPa")
print(f"  bulk modulus K = lambda + 2 mu/3 = {(LAM + 2 * MU / 3) / 1e9:.6f} GPa")
print(f"  pressure = -tr(sigma)/3 = {-trace(SIGMA) / 3e6:.6f} MPa")

shear_only = [[0.0, 2.0e-4, 0.0], [2.0e-4, 0.0, 0.0], [0.0, 0.0, 0.0]]
SIGMA_SHEAR = hooke(shear_only)
print(f"\n  pure shear strain, gamma_xy = {2 * shear_only[0][1]:.1e}:")
print(f"    tr sigma = {trace(SIGMA_SHEAR):.3e} Pa   (a pure shear changes no volume)")
print(f"    sigma_xy = 2 mu e_xy = mu gamma_xy = {SIGMA_SHEAR[0][1] / 1e6:.6f} MPa")
print("    (for isotropic media the engineering form tau = mu gamma is correct;")
print("     the factor of 2 is intrinsic to e_xy and is why Voigt notation needs")
print("     care when the medium is anisotropic -- lesson 01-15-05)")

deviatoric_e = [[E_SMALL[i][j] - (trace(E_SMALL) / 3.0) * delta(i, j)
                 for j in range(N)] for i in range(N)]
dev_sigma = hooke(deviatoric_e)
print(f"\n  deviatoric part of sigma from the deviatoric part of e:")
print(f"    max |s_ij - 2 mu e'_ij| = "
      f"{max(abs(dev_sigma[i][j] - 2 * MU * deviatoric_e[i][j]) for i in range(N) for j in range(N)):.1e} Pa")
print("    i.e. the deviatoric response only sees mu, and the volumetric")
print("    response only sees K. That separation is the reason the split exists.")


def main() -> None:
    print("Stress and strain tensors: invariants, principal axes, compatibility")


if __name__ == "__main__":
    main()
