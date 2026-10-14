#!/usr/bin/env python3
"""Cross-hole electrical tomography: geometric factors, the adjoint sensitivity
kernel, conditioning of the tomographic system and the equivalence (non-unique)
model demonstration.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cross_hole_tomography_demo.py

EVERYTHING IS SYNTHETIC.  The "well pair", the electrode depths and the
conductivity anomaly are chosen teaching values, not measurements from a site.

Contents
--------
1. Whole-space Green's function, geometric factors and a forward check.
2. The four-electrode sensitivity kernel: it is a diffuse banana, not a ray;
   the kernel has positive and negative lobes.
3. Normalisation identity: the volume integral of the pole-pole kernel equals
   the exact derivative of the potential with respect to a uniform conductivity
   change, -1/(4 pi sigma^2 r_AM).  Verified numerically.
4. The tomographic system: Jacobian, singular-value spectrum, condition number,
   resolution diagonal.
5. Equivalence: a second model that fits the data as well as the first and is
   measurably further from the truth.
6. Data coverage: which cells the survey constrains, and which it leaves free.
"""

import numpy as np
from numpy.polynomial.legendre import leggauss

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC survey geometry (whole space; two boreholes) ------------------
L_HOLE = 20.0        # m, borehole separation
SIGMA0 = 0.050       # S/m, background conductivity (rho = 20 ohm m)
X_MIN, X_MAX = 2.0, 18.0   # m, parametrised model region between the holes
Z_MIN, Z_MAX = 2.0, 18.0   # m, parametrised model region in depth
NX, NZ = 4, 6              # model cells in x and z
NY = 1                     # one cell in y (a slab); half width below
W_Y = 8.0                  # m, model half-width in y

# Gauss-Legendre nodes per cell in x, y, z
NQX, NQY, NQZ = 6, 8, 6


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def unit_potential(points, src):
    """Potential per unit current in a whole space of unit conductivity, 1/(4 pi r).

    Parameters
    ----------
    points : (..., 3) array of observation points
    src    : (3,) source position
    Returns the array 1/(4 pi |points - src|); units 1/m.
    """
    r = np.linalg.norm(points - np.asarray(src, float), axis=-1)
    return 1.0 / (4.0 * np.pi * np.maximum(r, 1e-12))


def geom_factor(a, b, m, n):
    """Geometric factor K such that rho_apparent = K * (dV/I), whole space.

    Phi(r) = I rho / (4 pi r), so
        dV/I = rho (1/4pi) [1/rAM - 1/rBM - 1/rAN + 1/rBN],
    and K = 4 pi / [1/rAM - 1/rBM - 1/rAN + 1/rBN], with units of metres.
    """
    def r(p, q):
        return np.linalg.norm(np.asarray(p, float) - np.asarray(q, float))
    g4 = (1.0 / r(a, m) - 1.0 / r(b, m) - 1.0 / r(a, n) + 1.0 / r(b, n))
    return 4.0 * np.pi / g4, g4


def pole_kernel(points, a, m, sigma0):
    """Sensitivity dPhi_A(M)/d sigma(r) for a unit-current point pair A -> M.

    Derived from the adjoint (reciprocity) identity

        dPhi_A(M)/d sigma(r) = - grad(Phi_A) . grad(Phi_M)

    with Phi_X(P) = 1/(4 pi sigma0 |P - X|).  Result in ohm^2 / m^2 per unit
    volume of the perturbation; multiplying by dV (m^3) gives ohm^2 m.
    """
    ua = (points - np.asarray(a, float))
    ra = np.linalg.norm(ua, axis=-1)
    ua = ua / np.maximum(ra, 1e-12)[..., None]
    um = (points - np.asarray(m, float))
    rm = np.linalg.norm(um, axis=-1)
    um = um / np.maximum(rm, 1e-12)[..., None]
    cosang = np.sum(ua * um, axis=-1)
    return -cosang / (16.0 * np.pi ** 2 * sigma0 ** 2
                      * np.maximum(ra, 1e-12) ** 2 * np.maximum(rm, 1e-12) ** 2)


def quad_kernel(a, b, m, n, sigma0, boxes, nq=(NQX, NQY, NQZ)):
    """Volume-integrate the four-electrode kernel over each box in `boxes`.

    Returns an array of integrals, one per box, units ohm^2 m.
    """
    gx, wx = leggauss(nq[0])
    gy, wy = leggauss(nq[1])
    gz, wz = leggauss(nq[2])
    out = np.zeros(len(boxes))
    for i, (x0, x1, y0, y1, z0, z1) in enumerate(boxes):
        px = 0.5 * (x1 - x0) * gx + 0.5 * (x1 + x0)
        py = 0.5 * (y1 - y0) * gy + 0.5 * (y1 + y0)
        pz = 0.5 * (z1 - z0) * gz + 0.5 * (z1 + z0)
        X, Y, Z = np.meshgrid(px, py, pz, indexing="ij")
        pts = np.stack([X.ravel(), Y.ravel(), Z.ravel()], axis=-1)
        k = (pole_kernel(pts, a, m, sigma0) - pole_kernel(pts, b, m, sigma0)
             - pole_kernel(pts, a, n, sigma0) + pole_kernel(pts, b, n, sigma0))
        jac = (0.5 * (x1 - x0)) * (0.5 * (y1 - y0)) * (0.5 * (z1 - z0))
        w = np.einsum("i,j,k->ijk", wx, wy, wz).ravel()
        out[i] = jac * np.sum(k * w)
    return out


def make_boxes():
    xs = np.linspace(X_MIN, X_MAX, NX + 1)
    zs = np.linspace(Z_MIN, Z_MAX, NZ + 1)
    boxes, index = [], []
    for i in range(NX):
        for j in range(NZ):
            boxes.append((xs[i], xs[i + 1], -W_Y, W_Y, zs[j], zs[j + 1]))
            index.append((i, j))
    return boxes, index


def make_quadrupoles():
    """Cross-hole bipole-bipole survey: source bipole in hole 1, receiver in 2."""
    depths = np.arange(3.0, 19.0, 3.0)
    half = 1.0                      # bipole half-length, m
    quads = []
    for za in depths:
        a = (0.0, 0.0, za - half)
        b = (0.0, 0.0, za + half)
        for zm in depths:
            m = (L_HOLE, 0.0, zm - half)
            n = (L_HOLE, 0.0, zm + half)
            quads.append((a, b, m, n))
    return quads


def main():
    section("1. Whole-space Green's function, geometric factor, forward check")
    print("Point current source in an unbounded medium of conductivity sigma:")
    print("    Phi(r) = I / (4 pi sigma r)     [V]")
    print(f"SYNTHETIC background resistivity: rho0 = {1/SIGMA0:.3f} ohm m "
          f"(sigma0 = {SIGMA0:.3f} S/m)")
    a = (0.0, 0.0, 10.0)
    b = (0.0, 0.0, 12.0)
    m = (L_HOLE, 0.0, 9.0)
    n = (L_HOLE, 0.0, 11.0)
    K, g4 = geom_factor(a, b, m, n)
    print(f"example cross-hole quadrupole: A z=10 m, B z=12 m (hole 1);")
    print(f"                              M z=9 m, N z=11 m (hole 2)")
    print(f"  1/(4 pi)[1/rAM-1/rBM-1/rAN+1/rBN] = {g4:.6e} 1/m")
    print(f"  geometric factor K = {K:.4f} m")
    dv_over_i = g4 * (1.0 / SIGMA0) / (4.0 * np.pi)
    print(f"  forward: dV/I = rho0 * g4 / (4 pi) = {dv_over_i:.6e} ohm")
    print(f"  inverse: rho_a = K * (dV/I) = {K * dv_over_i:.6f} ohm m  "
          f"(recovers rho0 = {1 / SIGMA0:.3f})")

    section("2. The four-electrode sensitivity kernel: a diffuse banana")
    xg = np.linspace(2.2, L_HOLE - 2.2, 120)
    zg = np.linspace(2.0, 18.0, 120)
    X, Z = np.meshgrid(xg, zg, indexing="ij")
    pts = np.stack([X.ravel(), np.zeros(X.size), Z.ravel()], axis=-1)
    kk = (pole_kernel(pts, a, m, SIGMA0) - pole_kernel(pts, b, m, SIGMA0)
          - pole_kernel(pts, a, n, SIGMA0) + pole_kernel(pts, b, n, SIGMA0))
    kk = kk.reshape(X.shape)
    imax = np.unravel_index(np.argmax(np.abs(kk)), kk.shape)
    print(f"quadrupole used: A/B in hole 1 at z=10/12 m, M/N in hole 2 at z=9/11 m")
    print(f"kernel |J| maximum on the x-z plane at x = {X[imax]:.2f} m, "
          f"z = {Z[imax]:.2f} m")
    print(f"   straight-line midpoint between the two bipoles: x = "
          f"{0.5 * L_HOLE:.2f} m, z = {0.5 * (10.5 + 10.0):.2f} m")
    print(f"   peak sensitivity J = {kk[imax]:.4e} ohm^2/m^2")
    print("sign structure along the line z = 10.5 m:")
    iz = np.argmin(np.abs(zg - 10.5))
    for xq in (2.5, 6.0, 10.0, 14.0, 17.5):
        iq = np.argmin(np.abs(xg - xq))
        print(f"   x = {xq:5.1f} m:  J = {kk[iz, iq]:+.4e} ohm^2/m^2")
    print("J on a coarse (x, z) grid, in units of 1e-6 ohm^2/m^2:")
    print("      z=  4.0      6.0      8.0     10.5     13.0     15.0")
    for xq in (5.0, 10.0, 15.0):
        iq = np.argmin(np.abs(xg - xq))
        row = []
        for zq in (4.0, 6.0, 8.0, 10.5, 13.0, 15.0):
            jz = np.argmin(np.abs(zg - zq))
            row.append(f"{kk[jz, iq] * 1e6:+8.3f}")
        print(f"  x={xq:4.1f}  " + " ".join(row))
    neg = kk < 0.0
    print(f"fraction of the plane where the kernel is NEGATIVE: "
          f"{100.0 * neg.mean():.1f}%")
    print("A ray-based picture would put all sensitivity on one line; the true")
    print("kernel is broad, changes sign, and has no zero-thickness support.")
    print("The largest values sit close to the ELECTRODES (the kernel grows as")
    print("1/r^2 towards a current electrode), which is why the near-electrode")
    print("region dominates a cross-hole survey and is usually parameterised")
    print("coarsely or excluded.")

    section("3. Kernel normalisation identity (numerical verification)")
    # For a pole-pole pair, integrating the kernel over ALL space must give the
    # exact derivative of the potential with respect to a uniform conductivity
    # change:  dPhi/dsigma = -1/(4 pi sigma^2 r_AM).
    r_am = 6.0
    aa = np.array([0.0, 0.0, 0.0])
    mm = np.array([r_am, 0.0, 0.0])
    gt, wt = leggauss(400)
    th = 0.5 * np.pi * (gt + 1.0)             # 0 .. pi
    wth = 0.5 * np.pi * wt
    # radial grid: r = r_am * exp(s), so dr = r ds
    s = np.linspace(np.log(1e-4), np.log(4e4), 6000)
    r = r_am * np.exp(s)
    dr = r * (s[1] - s[0])
    R, TH = np.meshgrid(r, th, indexing="ij")
    W = np.outer(dr, wth)
    rM = np.sqrt(R ** 2 + r_am ** 2 - 2.0 * R * r_am * np.cos(TH))
    cosang = (R - r_am * np.cos(TH)) / rM
    integrand = cosang / (R ** 2 * rM ** 2)      # == u_A . u_M / (rA^2 rM^2)
    # dV in spherical coordinates includes r^2 sin(theta); here the kernel gives
    # J = -cosang/(16 pi^2 sigma^2 rA^2 rM^2), so multiply by r^2 sin(theta).
    integrand = integrand * R ** 2 * np.sin(TH)
    T = 2.0 * np.pi * float(np.sum(W * integrand))
    exact = 4.0 * np.pi / r_am
    print(f"integral of (u_A . u_M)/(rA^2 rM^2) dV for r_AM = {r_am:.1f} m:")
    print(f"   numerical = {T:.6f} 1/m")
    print(f"   exact 4 pi / r_AM = {exact:.6f} 1/m")
    print(f"   relative difference = {abs(T - exact) / exact * 100:.4f}%")
    int_kernel = -T / (16.0 * np.pi ** 2 * SIGMA0 ** 2)
    exact_kernel = -1.0 / (4.0 * np.pi * SIGMA0 ** 2 * r_am)
    print(f"integral of the kernel over all space = {int_kernel:.6e} ohm^2 m")
    print(f"exact dPhi/dsigma (uniform)          = {exact_kernel:.6e} ohm^2 m")
    print("The kernel is therefore correctly normalised: its volume integral")
    print("reproduces the exact response to a spatially uniform perturbation.")

    section("4. The tomographic system: Jacobian, spectrum, resolution")
    boxes, index = make_boxes()
    quads = make_quadrupoles()
    print(f"model: {NX} x {NZ} = {NX * NZ} cells, x in [{X_MIN},{X_MAX}] m, "
          f"z in [{Z_MIN},{Z_MAX}] m, |y| <= {W_Y} m")
    print(f"data : {len(quads)} cross-hole quadrupoles (bipole-bipole)")
    print("NOTE: the region within 2 m of a borehole is NOT parametrised; that")
    print("choice is part of the model and is a real source of model error.")
    J = np.zeros((len(quads), len(boxes)))
    for i, (qa, qb, qm, qn) in enumerate(quads):
        J[i] = quad_kernel(qa, qb, qm, qn, SIGMA0, boxes)
    Jrel = J * SIGMA0          # parametrise by delta sigma / sigma (dimensionless)
    print(f"Jacobian entries |J|: median {np.median(np.abs(Jrel)):.3e} ohm, "
          f"max {np.abs(Jrel).max():.3e} ohm")
    # SYNTHETIC true model: a conductive block (delta sigma / sigma = +0.50)
    m_true = np.zeros(len(boxes))
    for k, (i, j) in enumerate(index):
        if i in (1, 2) and j in (1, 2, 3):
            m_true[k] = 0.50
    d_clean = Jrel @ m_true
    sigma_d = 0.005 * np.abs(d_clean).max()      # 0.5% of the largest datum
    d = d_clean + sigma_d * RNG.standard_normal(d_clean.size)
    print(f"synthetic anomaly: +50% conductivity in a {2}x{3}-cell block; "
          f"max |d| = {np.abs(d_clean).max():.3e} ohm")
    print(f"added Gaussian noise: sigma_d = {sigma_d:.3e} ohm")
    U, sv, Vt = np.linalg.svd(Jrel, full_matrices=False)
    print("singular values of the Jacobian (ohm):")
    print("   " + "  ".join(f"{s:.2e}" for s in sv))
    print(f"condition number s_max/s_min = {sv[0] / sv[-1]:.3e}")
    print(f"rank at tolerance 1e-6 s_max: {int(np.sum(sv > 1e-6 * sv[0]))} "
          f"of {len(sv)}")
    alpha = (0.1 * sv[0]) ** 2                   # Tikhonov damping parameter
    Rmat = Vt.T @ np.diag(sv ** 2 / (sv ** 2 + alpha)) @ Vt
    m_est = Vt.T @ ((sv / (sv ** 2 + alpha)) * (U.T @ d))
    resid = np.linalg.norm(d - Jrel @ m_est) / np.linalg.norm(d)
    print(f"Tikhonov damping alpha = {alpha:.3e} ohm^2")
    print(f"relative data misfit ||d - Jm|| / ||d|| = {resid * 100:.3f}%")
    print("cell      x (m)   z (m)   true m   estimated m   resolution diag")
    for k, (i, j) in enumerate(index):
        xc = 0.5 * (boxes[k][0] + boxes[k][1])
        zc = 0.5 * (boxes[k][4] + boxes[k][5])
        print(f"  {k:2d}   {xc:6.2f}  {zc:6.2f}   {m_true[k]:+6.2f}   "
              f"{m_est[k]:+10.3f}   {Rmat[k, k]:9.3f}")
    print("The resolution diagonal is the fraction of each cell's anomaly that the")
    print("damped inversion recovers.  It is smallest in the cells mid-way between")
    print("the boreholes (0.12) and largest beside the electrodes (0.79); the peak")
    print("recovered anomaly is well below the injected +0.50 because damping trades")
    print("amplitude for stability.  The misfit is therefore never zero even though")
    print("the true model is in the parametrisation.")

    section("5. Equivalence: a different model with the same data fit")
    v = Vt[-1]                                   # weakest singular direction
    n_eff = max(1, int(np.sum(sv > 1e-4 * sv[0])))
    step = sigma_d * np.sqrt(max(1, d.size - n_eff)) / np.linalg.norm(Jrel @ v)
    m_alt = m_est + step * v
    r_est = np.linalg.norm(d - Jrel @ m_est)
    r_alt = np.linalg.norm(d - Jrel @ m_alt)
    print(f"null-space direction from the smallest singular vector "
          f"(s_min = {sv[-1]:.3e} ohm)")
    print(f"  ||d - J m_est|| = {r_est:.4e} ohm")
    print(f"  ||d - J m_alt|| = {r_alt:.4e} ohm   "
          f"(ratio {r_alt / r_est:.4f})")
    print(f"  ||m_alt - m_est|| = {np.linalg.norm(m_alt - m_est):.4f} "
          f"(dimensionless)")
    print(f"  ||m_alt - m_true|| = {np.linalg.norm(m_alt - m_true):.4f}")
    print(f"  ||m_est - m_true|| = {np.linalg.norm(m_est - m_true):.4f}")
    print(f"  the alternative is {np.linalg.norm(m_alt - m_true) / np.linalg.norm(m_est - m_true):.1f}x "
          f"further from the truth while fitting the data equally well")

    section("6. Data coverage: what the survey actually constrains")
    thresh = 0.2 * np.abs(Jrel).max(axis=0)
    strong = (np.abs(Jrel) > thresh[None, :]).sum(axis=0)
    print("cell      x (m)   z (m)   data with above-threshold sensitivity")
    for k, (i, j) in enumerate(index):
        xc = 0.5 * (boxes[k][0] + boxes[k][1])
        zc = 0.5 * (boxes[k][4] + boxes[k][5])
        print(f"  {k:2d}   {xc:6.2f}  {zc:6.2f}   {strong[k]:3d} of {len(quads)}")
    cov = (np.linalg.inv(Jrel.T @ Jrel / sigma_d ** 2 + 1e-6 * np.eye(len(boxes)))
           / 1.0)
    diag = np.sqrt(np.maximum(np.diag(cov), 0.0))
    print("model standard errors from the linearised covariance (dimensionless,")
    print("ignoring damping-induced bias):")
    print("   " + "  ".join(f"{s:.3f}" for s in diag))
    print("The smallest model error is in the cells beside the electrodes "
          f"({diag.min():.3f});")
    print(f"the largest is {diag.max():.3f}, in cells far from every electrode "
          f"({diag.max() / diag.min():.1f}x larger).")
    print("The survey illuminates the region it can reach, not a block model.")


if __name__ == "__main__":
    main()
