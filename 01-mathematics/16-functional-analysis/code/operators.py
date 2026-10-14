"""Linear operators: boundedness, adjoints, compactness and adjoint gradients.

Run:  python3 operators.py
Requires: Python standard library only.

Companion to lesson 01-16-03 (Linear Operators, Adjoints and Compactness).

Sections
    1. A bounded operator and an unbounded one
    2. The adjoint identity, for a matrix and for a convolution
    3. The adjoint of convolution is correlation: the geophysical reading
    4. Compactness: singular values of a smoothing kernel, and of a projection
    5. The adjoint is what makes a gradient cheap
"""

import math
import random


def section(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


# ------------------------- small dense linear algebra -----------------

def mat_vec(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def transpose(A):
    return [list(col) for col in zip(*A)]


def mat_mul(A, B):
    Bt = transpose(B)
    return [[sum(a * b for a, b in zip(row, col)) for col in Bt] for row in A]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def norm2(x):
    return math.sqrt(dot(x, x))


def jacobi_eig(A, tol=1e-14, max_sweeps=200):
    """Cyclic Jacobi eigendecomposition of a real symmetric matrix.

    Returns (eigenvalues, V) with A = V diag(eigenvalues) V^T and V orthogonal.
    """
    n = len(A)
    a = [row[:] for row in A]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_sweeps):
        off = math.sqrt(sum(a[p][q] ** 2 for p in range(n) for q in range(p + 1, n)))
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                apq = a[p][q]
                if abs(apq) < 1e-300:
                    continue
                theta = (a[q][q] - a[p][p]) / (2.0 * apq)
                t = (1.0 if theta >= 0 else -1.0) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
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
    return [a[i][i] for i in range(n)], v


# ----------------------------------------------------------------------
# 1. Bounded and unbounded operators
# ----------------------------------------------------------------------

def bounded_and_unbounded():
    section("1. Differentiation: bounded as H1 -> L2, unbounded as L2 -> L2")

    n = 200001
    h = 1.0 / (n - 1)
    xs = [i * h for i in range(n)]
    w = [h] * n
    w[0] = w[-1] = 0.5 * h

    def l2(f):
        return math.sqrt(sum(wi * f(x) ** 2 for x, wi in zip(xs, w)))

    def h1(f, df):
        return math.sqrt(sum(wi * (f(x) ** 2 + df(x) ** 2)
                             for x, wi in zip(xs, w)))

    print("    f_N(x) = sin(N pi x) on (0,1); D f_N = N pi cos(N pi x)")
    print(f"    {'N':>5}{'||f_N||_L2':>13}{'||D f_N||_L2':>15}"
          f"{'ratio (L2->L2)':>18}{'ratio (H1->L2)':>17}")
    for N in (1, 2, 4, 8, 16, 32):
        f = lambda x, N=N: math.sin(N * math.pi * x)
        df = lambda x, N=N: N * math.pi * math.cos(N * math.pi * x)
        nf, ndf = l2(f), l2(df)
        print(f"    {N:>5}{nf:>13.6f}{ndf:>15.6f}{ndf / nf:>18.6f}"
              f"{ndf / h1(f, df):>17.6f}")
    print("    the L2->L2 ratio grows without bound (it is N pi / sqrt(2), since")
    print("    ||f_N|| = 1/sqrt(2) for every N), so D has no norm as an operator")
    print("    on L2. The H1->L2 ratio is bounded by 1 for every N: measuring the")
    print("    input in the norm that charges for its roughness makes the same")
    print("    operator bounded. Boundedness is a property of the pair of norms.")
    print(f"    N pi / sqrt(2) at N = 32: {32 * math.pi / math.sqrt(2.0):.6f}")


# ----------------------------------------------------------------------
# 2. The adjoint identity
# ----------------------------------------------------------------------

def adjoint_identity():
    section("2. <A x, y> = <x, A^T y>, checked for a matrix and a convolution")

    random.seed(11)
    n = 12
    A = [[random.uniform(-1, 1) for _ in range(n)] for _ in range(n)]
    x = [random.uniform(-1, 1) for _ in range(n)]
    y = [random.uniform(-1, 1) for _ in range(n)]

    lhs = dot(mat_vec(A, x), y)
    rhs = dot(x, mat_vec(transpose(A), y))
    print(f"    random 12x12 A: <Ax,y> = {lhs:+.12f}, <x,A^T y> = {rhs:+.12f}")
    print(f"    absolute difference {abs(lhs - rhs):.3e}")

    print("\n    convolution: (g * m)_i = sum_j g_{i-j} m_j, so")
    print("    G_{ij} = g_{i-j} and (G^T)_{ij} = g_{j-i}.")
    g = [math.exp(-0.5 * k * k) for k in range(5)]   # causal kernel, support 0..4
    m = 9
    G = [[0.0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            k = i - j
            if 0 <= k < len(g):
                G[i][j] = g[k]
    x = [random.uniform(-1, 1) for _ in range(m)]
    y = [random.uniform(-1, 1) for _ in range(m)]
    l = dot(mat_vec(G, x), y)
    r = dot(x, mat_vec(transpose(G), y))
    print(f"    G is {m}x{m} banded lower-triangular (Toeplitz)")
    print(f"    <Gx,y> = {l:+.12f}, <x,G^T y> = {r:+.12f}, diff = {abs(l - r):.3e}")

    print("\n    the adjoint applied to y is the correlation with the same kernel:")
    GTy = mat_vec(transpose(G), y)
    direct = []
    for i in range(m):
        s = 0.0
        for j in range(m):
            k = j - i
            if 0 <= k < len(g):
                s += g[k] * y[j]
        direct.append(s)
    print("    (G^T)_{ij} = G_{ji} = g_{j-i}, so (G^T y)_i = sum_j g_{j-i} y_j,")
    print("    which is cross-correlation of y with g at lag 0, not convolution")
    print(f"    max |G^T y - correlation with the same kernel| = "
          f"{max(abs(a - b) for a, b in zip(GTy, direct)):.3e}")
    print("    Reversing the kernel would give convolution again, which is why")
    print("    the adjoint source in a correlation-based inverse problem is")
    print("    built by cross-correlating the residual with the forward field.")

    print("\n    a symmetric kernel gives a self-adjoint operator:")
    gs = [math.exp(-0.5 * k * k) for k in range(3)] + [math.exp(-0.5 * k * k) for k in (2, 1)]
    S = [[0.0] * 7 for _ in range(7)]
    for i in range(7):
        for j in range(7):
            k = abs(i - j)
            if k < len(gs):
                S[i][j] = gs[k]
    print(f"    max |S - S^T| = {max(abs(S[i][j] - S[j][i]) for i in range(7) for j in range(7)):.3e}")
    print("    A symmetric Toeplitz matrix is self-adjoint, which is why the")
    print("    gravity and waveform adjoints can share the forward boundary")
    print("    conditions: the adjoint operator is the same operator.")


# ----------------------------------------------------------------------
# 3. Compactness
# ----------------------------------------------------------------------

def compactness():
    section("3. Compactness: which operators have singular values that decay?")

    n = 64
    h = 1.0 / (n - 1)
    xs = [i * h for i in range(n)]

    def kernel(sigma):
        return [[math.exp(-((xs[i] - xs[j]) ** 2) / (2.0 * sigma * sigma))
                 for j in range(n)] for i in range(n)]

    def singular_values_of_symmetric(K):
        ev, V = jacobi_eig(K)
        return sorted((abs(e) for e in ev), reverse=True)

    print("    (a) Gaussian smoothing kernel K(x,y) = exp(-(x-y)^2/(2 sigma^2))")
    print("    normalised singular values sigma_k / sigma_1")
    ks = (1, 2, 4, 8, 12, 16, 20, 24, 32)
    print(f"    {'sigma':>7}" + "".join(f"{'k=%d' % k:>12}" for k in ks))
    tables = {}
    for sigma in (0.30, 0.20, 0.10):
        sv = singular_values_of_symmetric(kernel(sigma))
        tables[sigma] = sv
        print(f"    {sigma:>7.2f}" + "".join(
            f"{sv[k - 1] / sv[0]:>12.3e}" for k in ks))

    print("\n    successive ratios sigma_k / sigma_{k-1} for sigma = 0.10")
    sv = tables[0.10]
    print(f"    {'k':>5}{'sigma_k/sigma_{k-1}':>22}")
    for k in (2, 4, 6, 8, 10, 12, 16, 20):
        print(f"    {k:>5}{sv[k - 1] / sv[k - 2]:>22.4f}")
    print("    the ratio itself keeps falling, so the decay is faster than any")
    print("    fixed geometric rate. The double-precision floor for the ratios")
    print(f"    above is about 2.2e-16, which the sigma = 0.10 column reaches")
    print(f"    near k = {next(k for k in range(1, 65) if sv[k - 1] / sv[0] < 1e-15)}.")
    print("    A smooth kernel is the prototype of a compact operator: it maps")
    print("    the unit ball into a set with compact closure, and 'sigma_k -> 0'")
    print("    is the same statement in the discrete picture.")

    print("\n    (b) a projection has no decay at all, so it is not compact")
    print("    P = identity on the retained subspace; its nonzero singular")
    print("    values are all 1 at every size, so sigma_k does not tend to 0")
    print(f"    {'n':>6}{'num sigma > 0.99':>20}{'value of sigma_{n/2}':>24}")
    for m in (16, 32, 64):
        P = [[1.0 if i == j else 0.0 for j in range(m)] for i in range(m)]
        svp = singular_values_of_symmetric(P)
        print(f"    {m:>6}{sum(1 for s in svp if s > 0.99):>20}{svp[m // 2]:>24.6f}")
    print("    the count grows linearly with n, so for the infinite-dimensional")
    print("    projection sigma_k = 1 for every k. This is the difference between")
    print("    a compact operator (Fourier coefficients of a smooth field) and a")
    print("    non-compact one (a filter that merely selects a band).")

    print("\n    (c) effective numerical rank of the 64 x 64 discrete kernel")
    print(f"    {'sigma':>7}{'rank, thr 1e-6':>18}{'rank, thr 1e-12':>18}"
          f"{'resolvable rank':>18}")
    for sigma in (0.30, 0.20, 0.10):
        sv = tables[sigma]
        r6 = sum(1 for s in sv if s / sv[0] >= 1e-6)
        r12 = sum(1 for s in sv if s / sv[0] >= 1e-12)
        rres = sum(1 for s in sv if s / sv[0] >= 1e-15)
        print(f"    {sigma:>7.2f}{r6:>18}{r12:>18}{rres:>18}")
    print("    the discrete matrix has full algebraic rank 64 for every sigma,")
    print("    but almost all of those directions carry no information that")
    print("    double precision can hold: beyond the 'resolvable rank' the")
    print("    computed singular values are round-off, not spectrum. Quoting a")
    print("    single condition number for this matrix is meaningless, and the")
    print("    meaningful rank is what the regularisation of lesson 01-16-06")
    print("    acts on.")


# ----------------------------------------------------------------------
# 4. The adjoint gradient
# ----------------------------------------------------------------------

def adjoint_gradient():
    section("4. The adjoint computes the gradient of a misfit in one extra solve")

    n = 40
    h = 1.0 / (n - 1)
    xs = [i * h for i in range(n)]
    sigma = 0.10
    K = [[h * math.exp(-((xs[i] - xs[j]) ** 2) / (2.0 * sigma * sigma))
          for j in range(n)] for i in range(n)]

    m_true = [math.exp(-((x - 0.3) ** 2) / (2 * 0.05 ** 2))
              + 0.7 * math.exp(-((x - 0.7) ** 2) / (2 * 0.08 ** 2)) for x in xs]
    d = mat_vec(K, m_true)

    def misfit(m):
        r = [a - b for a, b in zip(mat_vec(K, m), d)]
        return dot(r, r), r

    random.seed(3)
    m0 = [random.gauss(0.0, 0.5) for _ in range(n)]
    J0, r = misfit(m0)
    grad_adjoint = [2.0 * v for v in mat_vec(transpose(K), r)]

    eps = 1e-6
    grad_fd = []
    for i in range(n):
        mp = m0[:]
        mm = m0[:]
        mp[i] += eps
        mm[i] -= eps
        grad_fd.append((misfit(mp)[0] - misfit(mm)[0]) / (2.0 * eps))

    rel = max(abs(a - b) for a, b in zip(grad_adjoint, grad_fd)) / max(abs(v) for v in grad_fd)
    print(f"    model dimension n = {n}, misfit J(m_0) = {J0:.6f}")
    print(f"    ||adjoint gradient|| = {norm2(grad_adjoint):.6f}")
    print(f"    max relative difference from a central finite difference of J:")
    print(f"        {rel:.3e}")
    print("    the adjoint gives grad J = 2 K^T (K m - d) exactly, at the cost of")
    print("    one application of K^T to the residual. In a PDE setting that is")
    print("    one adjoint simulation, whatever the number of model parameters.")

    print("\n    gradient descent with the adjoint gradient, smoothing kernel:")
    A = mat_mul(transpose(K), K)   # K^T K, symmetric
    ev, _ = jacobi_eig(A)
    L = max(ev)
    tau = 0.5 / L
    m = m0[:]

    def wn(v):                     # weighted (grid) norm, matching the h weights
        return math.sqrt(h * dot(v, v))

    print(f"    L = ||K^T K|| = {L:.6f} (Jacobi); step tau = 0.5/L = {tau:.6f}")
    print("    the factor for mode k is 1 - 2 tau lambda_k = 1 - lambda_k/L:")
    print(f"    {'k':>5}{'lambda_k / L':>18}{'factor 1 - lambda_k/L':>24}"
          f"{'steps to 1e-3, log(1e-3)/log(f)':>34}")
    ev_desc = sorted(ev, reverse=True)
    for k in (1, 2, 4, 8, 16, 24, 32):
        ratio = ev_desc[k - 1] / L
        f = 1.0 - ratio
        if 1e-12 < f < 1.0:
            steps = math.log(1e-3) / math.log(f)
            steps_txt = f"{steps:.3g}"
        else:
            steps_txt = "never" if f >= 1.0 else "1"
        print(f"    {k:>5}{ratio:>18.3e}{f:>24.10f}{steps_txt:>34}")
    print("    the well-resolved modes need a few steps; the ill-resolved ones")
    print("    would need astronomically many, so the iteration stops helping")
    print("    long before it is finished. Measured, with the weighted model norm:")
    print(f"    {'iteration':>10}{'J(m)':>16}{'||m - m_true|| (weighted)':>30}")
    for it in range(0, 301, 100):
        J, r = misfit(m)
        print(f"    {it:>10}{J:>16.6e}"
              f"{wn([a - b for a, b in zip(m, m_true)]):>30.8f}")
        for _ in range(100 if it < 300 else 0):
            J, r = misfit(m)
            g = [2.0 * v for v in mat_vec(transpose(K), r)]
            m = [a - tau * b for a, b in zip(m, g)]
    print("    J falls by five orders of magnitude in the first 100 steps and then")
    print("    moves by less than a factor of two over the next 200, while the")
    print("    model error falls from 0.695 only to 0.386 and then crawls: the")
    print("    data determine the smooth part of the model and say almost nothing")
    print("    about the rest. Steepest descent on a compact normal operator is")
    print("    slow exactly where the spectrum is small. This is the discrete face")
    print("    of ill-posedness, and lesson 01-16-07 shows how stopping it early")
    print("    becomes a regularisation (semiconvergence).")

    print("\n    (c) a rank-3 separable kernel: descent converges, and the")
    print("    unrecovered part is exactly the null-space component")
    nn = 40
    hh = 1.0 / (nn - 1)
    xg = [i * hh for i in range(nn)]
    amps = (1.0, 0.5, 0.2)

    def phi(k, x):
        return math.sqrt(2.0) * math.sin(k * math.pi * x)

    def wnorm(v):
        return math.sqrt(hh * dot(v, v))

    Kr = [[hh * sum(amps[k - 1] * phi(k, xg[i]) * phi(k, xg[j])
                    for k in (1, 2, 3)) for j in range(nn)] for i in range(nn)]
    mt = [math.exp(-((x - 0.3) ** 2) / (2 * 0.06 ** 2))
          + 0.8 * math.exp(-((x - 0.65) ** 2) / (2 * 0.05 ** 2)) for x in xg]
    dr = mat_vec(Kr, mt)

    def misfit_r(m):
        r = [a - b for a, b in zip(mat_vec(Kr, m), dr)]
        return dot(r, r), r

    def coeff(v, k):
        return sum(hh * v[i] * phi(k, xg[i]) for i in range(nn))

    total2 = sum(hh * v * v for v in mt)
    null_norm = math.sqrt(max(0.0, total2 - sum(coeff(mt, k) ** 2 for k in (1, 2, 3))))
    print(f"    ||m_true||^2 (weighted) = {total2:.8f}")
    print(f"    retained subspace is span{{phi_1, phi_2, phi_3}}; the part of")
    print(f"    m_true outside it has norm {null_norm:.8f}")

    Ar = mat_mul(transpose(Kr), Kr)
    evr, _ = jacobi_eig(Ar)
    Lr = max(evr)
    taur = 0.5 / Lr
    ret = sorted((e for e in evr if e > 1e-12 * Lr), reverse=True)
    print(f"    nonzero eigenvalues of K^T K: "
          + ", ".join(f"{e:.6f}" for e in ret))
    print(f"    expected amplitudes are a_k^2 = "
          + ", ".join(f"{a * a:.6f}" for a in amps))
    print(f"    lambda_max = {Lr:.6f}, tau = 0.5/lambda_max = {taur:.6f},")
    print(f"    slowest retained-mode factor 1 - lambda_min/L = "
          f"{1.0 - ret[-1] / Lr:.6f}")
    m = [0.0] * nn
    print(f"    {'iteration':>10}{'J(m)':>18}{'||m - m_true|| (weighted)':>28}")
    for it in list(range(0, 601, 100)) + [3000]:
        if it == 3000:
            for _ in range(3000 - 600):
                J, r = misfit_r(m)
                g = [2.0 * v for v in mat_vec(transpose(Kr), r)]
                m = [a - taur * b for a, b in zip(m, g)]
        J, r = misfit_r(m)
        print(f"    {it:>10}{J:>18.6e}"
              f"{wnorm([a - b for a, b in zip(m, mt)]):>28.8f}")
        if it < 600:
            for _ in range(100):
                J, r = misfit_r(m)
                g = [2.0 * v for v in mat_vec(transpose(Kr), r)]
                m = [a - taur * b for a, b in zip(m, g)]
    J, r = misfit_r(m)
    final_err = wnorm([a - b for a, b in zip(m, mt)])
    print(f"    the iteration drives the data misfit to {J:.2e} and the weighted")
    print(f"    model error to {final_err:.8f}, against the null-space norm")
    print(f"    {null_norm:.8f}: the adjoint recovers everything the data can see")
    print("    and nothing the data cannot. No iteration can do better, because")
    print("    the missing component contributes zero to d. This is the")
    print("    non-uniqueness of lesson 01-16-05 appearing as a number.")
    print("    The residual drives the update: the adjoint is not an optional")
    print("    optimisation, it is the only way the gradient is ever formed in")
    print("    adjoint tomography and full-waveform inversion.")


if __name__ == "__main__":
    bounded_and_unbounded()
    adjoint_identity()
    compactness()
    adjoint_gradient()
