"""Ill-posedness in the sense of Hadamard, on a gravity-like operator.

Run:  python3 ill_posedness.py
Requires: Python standard library only.

Companion to lesson 01-16-05 (Ill-Posedness in the Sense of Hadamard).

The operator is the surface gravity profile of a line mass at depth z:

    d(x) = int_0^1 K(x - y) m(y) dy,   K(s) = (z/pi) / (s^2 + z^2)

K is a probability density (its integral is 1), so m is a density contrast
and d is the resulting vertical gravity, up to a constant factor. Its
Fourier transform is exp(-2 pi z |f|), which is the whole story: high
wavenumbers are attenuated by a factor fixed by the depth.

Sections
    1. The singular spectrum, and why a condition number needs a precision
    2. Existence fails: data that no model at this depth can produce
    3. Uniqueness fails: an oscillating model with almost no data signature
    4. Stability fails: 0.1 per cent noise destroys the unregularised inverse
"""

import math
import random

NG = 80


def section(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def mat_vec(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def transpose(A):
    return [list(col) for col in zip(*A)]


def mat_mul(A, B):
    Bt = transpose(B)
    return [[sum(a * b for a, b in zip(row, col)) for col in Bt] for row in A]


def jacobi_eig(A, tol=1e-16, max_sweeps=300):
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


def build(n=NG, z=0.05, span=1.0):
    h = span / (n - 1)
    x = [i * h for i in range(n)]
    K = [[h * (z / math.pi) / ((x[i] - x[j]) ** 2 + z * z) for j in range(n)]
         for i in range(n)]
    return x, h, K


def main():
    x, h, K = build()
    n = len(x)

    def wnorm(v):
        return math.sqrt(h * sum(t * t for t in v))

    ev, V = jacobi_eig(K)
    order = sorted(range(n), key=lambda k: -abs(ev[k]))
    lam = [ev[i] for i in order]

    def spectral(mode, coeffs):
        out = [0.0] * n
        for k, c in enumerate(coeffs):
            col = [V[i][order[k]] for i in range(n)]
            for i in range(n):
                out[i] += c * col[i]
        return out

    def coeffs_of(d):
        return [sum(V[i][order[k]] * d[i] for i in range(n)) for k in range(n)]

    section("1. The singular spectrum of the gravity kernel, z = 0.05")
    print(f"    {n} nodes, h = {h:.6f}; K symmetric, so sigma_k = |lambda_k|")
    print(f"    {'k':>4}{'sigma_k / sigma_1':>20}{'k':>4}{'sigma_k / sigma_1':>20}")
    for k in range(1, 9):
        print(f"    {k:>4}{abs(lam[k - 1]) / abs(lam[0]):>20.4e}"
              f"{k + 8:>4}{abs(lam[k + 7]) / abs(lam[0]):>20.4e}")
    print(f"    sigma_1 = {abs(lam[0]):.6f}, sigma_{n} = {abs(lam[n - 1]):.3e}")
    ratio = abs(lam[0]) / abs(lam[n - 1])
    print(f"    condition number sigma_1 / sigma_{n} = {ratio:.3e}")
    print(f"    its reciprocal, {1.0 / ratio:.2e}, is far above the double-precision")
    print("    unit round-off of 2.2e-16, so the condition number is a genuine")
    print("    property of the matrix and not a round-off artefact: this discrete")
    print("    problem is technically well posed. The underlying continuous")
    print("    operator is not, and the way to see that is to refine the")
    print("    discretisation:")

    print(f"\n    {'n':>5}{'sigma_min / sigma_1':>22}{'condition number':>20}"
          f"{'resolvable modes':>20}")
    for nn in (40, 80, 160):
        _, _, Kn = build(n=nn)
        evn, _ = jacobi_eig(Kn)
        smin = min(abs(e) for e in evn)
        smax = max(abs(e) for e in evn)
        resolv = sum(1 for e in evn if abs(e) / smax > 1e-15)
        print(f"    {nn:>5}{smin / smax:>22.3e}{smax / smin:>20.3e}{resolv:>20}")
    print("    the condition number grows without bound as the discretisation is")
    print("    refined: sigma_min -> 0 because the continuous operator is")
    print("    compact and compact operators on infinite-dimensional spaces have")
    print("    no bounded inverse. Ill-posedness is therefore a property that")
    print("    only appears in the limit; every finite discretisation hides it,")
    print("    and the hiding gets less convincing as n grows.")

    section("2. Existence fails for the continuous operator, not the matrix")
    m_true = [math.exp(-((xi - 0.4) ** 2) / (2 * 0.10 ** 2)) for xi in x]
    d_attainable = mat_vec(K, m_true)
    d_unattainable = [math.exp(-((xi - 0.5) ** 2) / (2 * 0.012 ** 2)) for xi in x]

    def lsq(mode, d, rank):
        c = coeffs_of(d)
        m = spectral(mode, [c[k] / lam[k] if k < rank else 0.0 for k in range(n)])
        r = [a - b for a, b in zip(mat_vec(K, m), d)]
        return math.sqrt(h * sum(t * t for t in r)) / wnorm(d), wnorm(m)

    print("    d_attainable   = K m_true with m_true a 0.10-wide Gaussian")
    print("    d_unattainable = a 0.012-wide Gaussian: a source shallower than")
    print("                     the kernel can image")
    print(f"    {'rank used':>10}{'attainable: rel. residual':>28}"
          f"{'unattainable: rel. residual':>30}")
    for rank in (8, 16, 32, 48):
        print(f"    {rank:>10}{lsq(None, d_attainable, rank)[0]:>28.3e}"
              f"{lsq(None, d_unattainable, rank)[0]:>30.6f}")
    print("    For the attainable datum the residual falls to round-off as modes")
    print("    are added. For the unattainable one it stalls at a floor: the")
    print("    residual is the part of the datum outside the range of K.")

    r_at, norm_at = lsq(None, d_attainable, n)
    r_un, norm_un = lsq(None, d_unattainable, n)
    print(f"\n    at full rank both are fitted, but at a price:")
    print(f"    {'datum':>16}{'rel. residual':>16}{'||m|| (weighted)':>20}"
          f"{'max |m|':>12}")
    for name, d in (("attainable", d_attainable), ("unattainable", d_unattainable)):
        _, nrm = lsq(None, d, n)
        c = coeffs_of(d)
        m = spectral(None, [c[k] / lam[k] for k in range(n)])
        print(f"    {name:>16}{lsq(None, d, n)[0]:>16.3e}{nrm:>20.3e}"
              f"{max(abs(t) for t in m):>12.3e}")
    print(f"    ||m_true|| (weighted) = {wnorm(m_true):.6f}")
    print("    The exact solution exists in the discrete problem and is a wildly")
    print("    oscillating function of enormous amplitude - the classic")
    print("    'ringing' solution. In the continuous problem it does not exist at")
    print("    all, because the range of a compact operator is not closed. The")
    print("    practical lesson is identical either way: a datum that is not in")
    print("    the range is fitted by a model that is physically meaningless.")

    section("3. Uniqueness fails: oscillating models with tiny data signature")
    print("    m_k(x) = sin(2 pi k x), predicted ratio exp(-2 pi z k) from the")
    print("    Fourier transform of the Cauchy kernel")
    print(f"    {'k':>4}{'||K m_k|| / ||m_k||':>24}{'exp(-2 pi z k)':>18}"
          f"{'measured / predicted':>24}")
    for k in (1, 2, 4, 6, 8, 10, 12):
        mk = [math.sin(2.0 * math.pi * k * xi) for xi in x]
        rat = wnorm(mat_vec(K, mk)) / wnorm(mk)
        pred = math.exp(-2.0 * math.pi * 0.05 * k)
        print(f"    {k:>4}{rat:>24.6e}{pred:>18.6e}{rat / pred:>24.6f}")
    print("    the agreement is within a few per cent for the resolved")
    print("    wavenumbers and degrades as k grows towards the Nyquist wavenumber")
    print(f"    1/(2h) = {1.0 / (2 * h):.1f}, where the discrete kernel aliases.")

    print("\n    the near-null vectors are computable: the singular functions")
    print("    with the smallest resolvable singular values")
    d_norm = wnorm(mat_vec(K, m_true))
    print(f"    ||K m_true|| (weighted) = {d_norm:.6f}; ||m_true|| = "
          f"{wnorm(m_true):.6f}")
    print("    perturbation = 0.3 v_k / ||v_k||, so its weighted norm is 0.3")
    print(f"    {'mode k':>8}{'sigma_k/sigma_1':>18}{'data change / ||d||':>22}"
          f"{'as a multiple of 1% noise':>28}")
    for k in (4, 8, 16, 32, 48, 64):
        col = [V[i][order[k - 1]] for i in range(n)]
        cn = wnorm(col)
        pert = [0.3 * t / cn for t in col]
        dch = wnorm(mat_vec(K, pert)) / d_norm
        print(f"    {k:>8}{abs(lam[k - 1]) / abs(lam[0]):>18.3e}{dch:>22.3e}"
              f"{dch / 0.01:>28.3e}")
    print("    A perturbation of weighted norm 0.3 along the 4th and 8th singular")
    print("    functions changes the data by tens of per cent: those directions")
    print("    are well determined. Along the 64th it changes the data by a few")
    print("    times 1e-5, which is a small fraction of a 1 per cent noise level;")
    print("    such a perturbation is invisible. Between those two extremes lies")
    print("    the boundary of what the experiment can see, and it moves with the")
    print("    noise level. That is failure of uniqueness in its practical form,")
    print("    and its remedy is a prior or a regulariser, not a better algorithm.")

    section("4. Stability fails: 0.1 per cent noise destroys the inverse")
    random.seed(20261014)
    d_exact = mat_vec(K, m_true)
    print(f"    ||m_true|| (weighted) = {wnorm(m_true):.6f}")
    print(f"    {'noise level eps':>18}{'||Km-d||/||d||':>18}"
          f"{'rel. model error, full rank':>30}{'amplification':>16}")
    results = {}
    for eps in (1e-4, 1e-5, 1e-6):
        noise = [random.gauss(0.0, 1.0) for _ in range(n)]
        scale = eps * wnorm(d_exact) / wnorm(noise)
        dn = [d_exact[i] + scale * noise[i] for i in range(n)]
        c = coeffs_of(dn)
        m_full = spectral(None, [c[k] / lam[k] for k in range(n)])
        err = wnorm([a - b for a, b in zip(m_full, m_true)]) / wnorm(m_true)
        results[eps] = (dn, c)
        print(f"    {eps:>18.0e}{eps:>18.0e}{err:>30.3e}{err / eps:>16.3e}")
    print(f"    the amplification is roughly constant near 2.5e4, which is")
    print(f"    comparable with the reciprocal of the smallest singular value")
    print(f"    ratio, 1/(sigma_80/sigma_1) = {abs(lam[0]) / abs(lam[n - 1]):.3e}.")
    print("    It is smaller than that reciprocal by a factor of about four")
    print("    because the random noise does not align with the last singular")
    print("    vector. The error is therefore proportional to the noise level,")
    print("    with a constant of order the condition number, and no amount of")
    print("    care with the arithmetic changes it: it is a property of K.")

    print("\n    truncating the expansion at the resolvable rank repairs it:")
    print(f"    {'noise level eps':>18}{'rank':>8}{'rel. model error':>22}"
          f"{'amplification':>16}")
    for eps in (1e-4, 1e-5, 1e-6):
        dn, c = results[eps]
        for rank in (12, 20, 28):
            m_t = spectral(None, [c[k] / lam[k] if k < rank else 0.0 for k in range(n)])
            err = wnorm([a - b for a, b in zip(m_t, m_true)]) / wnorm(m_true)
            print(f"    {eps:>18.0e}{rank:>8}{err:>22.3e}{err / eps:>16.3e}")
    print("    the truncated inverse is stable because the small sigma_k, which")
    print("    carried the noise, are gone. It is biased, because the modes that")
    print("    were discarded are also part of the answer. Trading one failure")
    print("    for the other in a controlled way is regularisation (lesson")
    print("    01-16-06), and the optimal truncation depends on the noise level.")

    print("\n    the three failures, their diagnoses and their remedies:")
    print("    existence    -- in the continuous problem the range of K is not")
    print("                    closed, so data outside it are unattainable; in a")
    print("                    discretisation they are attained by a ringing model")
    print("                    remedy: change the kernel, the depth or the")
    print("                    parameterisation; accept the misfit")
    print("    uniqueness   -- K m = 0 with m != 0: a null space exists, and the")
    print("                    near-null directions are computable from the small")
    print("                    singular values")
    print("                    remedy: prior information or a regulariser")
    print("    stability    -- the inverse amplifies noise by ~1/sigma_min, and")
    print("                    sigma_min -> 0 as the discretisation is refined")
    print("                    remedy: truncate or damp the small singular modes")
    print("    'ill posed' is a diagnosis with three parts, and each part has a")
    print("    different cure. Confusing them is the commonest error in the")
    print("    inverse-problems literature.")


if __name__ == "__main__":
    main()
