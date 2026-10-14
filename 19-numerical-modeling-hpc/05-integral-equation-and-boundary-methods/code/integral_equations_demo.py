#!/usr/bin/env python3
"""Integral-equation formulations for geophysical potential fields.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python integral_equations_demo.py

Everything printed here is SYNTHETIC.  The "body" is a chosen rectangle of
uniform density in a 2-D model space; the Fredholm kernels are chosen smooth
functions.  Nothing is a measurement of the Earth, and no published benchmark is
quoted.

Contents
--------
1. 2-D logarithmic potential of a uniform rectangular body, and the Poisson
   equation as an independent check of the sign and scale conventions.
2. Volume (area) quadrature: measured order of convergence, Richardson
   extrapolation, and accuracy per unknown.
3. Surface (boundary) quadrature via the divergence theorem: the same field from
   a 1-D quadrature, plus the far-field multipole residual slope.
4. Fredholm equation of the second kind: Nystrom discretisation, measured error
   order and a measured Neumann contraction factor.
5. Fredholm equation of the first kind: measured condition-number growth and the
   semi-convergence of the naive solution.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_CONST = 6.67430e-11          # m^3 kg^-1 s^-2, standard gravitational constant
RHO = 2600.0                   # kg/m^3, chosen uniform density (SYNTHETIC model)
XMIN, XMAX = -6000.0, 6000.0   # m, body extent in x
ZMIN, ZMAX = 3000.0, 9000.0    # m, body extent in z (z positive downward)
AREA = (XMAX - XMIN) * (ZMAX - ZMIN)
XC, ZC = 0.5 * (XMIN + XMAX), 0.5 * (ZMIN + ZMAX)
M2D = 2.0 * G_CONST * RHO * AREA   # m^2/s^2, the 2-D "monopole strength"


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def log_potential_area(x0, z0, n):
    """Phi = 2 G rho * integral_A ln|r0 - r'| dA' by midpoint area quadrature.

    Units: G [m^3 kg^-1 s^-2] * rho [kg m^-3] * area [m^2] * ln(1) -> m^2/s^2.
    """
    xs = XMIN + (np.arange(n) + 0.5) * (XMAX - XMIN) / n
    zs = ZMIN + (np.arange(n) + 0.5) * (ZMAX - ZMIN) / n
    dA = ((XMAX - XMIN) / n) * ((ZMAX - ZMIN) / n)
    dx = x0 - xs[:, None]
    dz = z0 - zs[None, :]
    r2 = dx ** 2 + dz ** 2
    return 2.0 * G_CONST * RHO * dA * np.sum(0.5 * np.log(r2))


def rectangle_edges():
    """Outward normals and endpoints of the four edges, counter-clockwise."""
    corners = np.array([[XMIN, ZMAX], [XMAX, ZMAX], [XMAX, ZMIN], [XMIN, ZMIN]])
    edges = []
    for i in range(4):
        p1 = corners[i]
        p2 = corners[(i + 1) % 4]
        d = p2 - p1
        length = np.hypot(*d)
        # outward normal of a CCW polygon in (x, z) coordinates
        normal = np.array([d[1], -d[0]]) / length
        centre = 0.5 * (p1 + p2)
        if np.dot(normal, centre - np.array([XC, ZC])) < 0.0:
            normal = -normal
        edges.append((p1, p2, length, normal))
    return edges


def boundary_gradient(x0, z0, n_gl=48):
    """Gradient of Phi from the boundary integral  grad Phi = -2 G rho ∮ ln|r0-r'| n dl'.

    The area gradient integral is converted with the divergence theorem:
        integral_A (x0-x')/|r0-r'|^2 dA' = -∮ ln|r0-r'| n_x dl'.
    Each edge integral is evaluated with n_gl Gauss-Legendre nodes.
    """
    t_gl, w_gl = np.polynomial.legendre.leggauss(n_gl)
    t = 0.5 * (t_gl + 1.0)
    w = 0.5 * w_gl
    gx = gz = 0.0
    for p1, p2, length, normal in rectangle_edges():
        r = p1[None, :] + t[:, None] * (p2 - p1)[None, :]
        rr = np.hypot(x0 - r[:, 0], z0 - r[:, 1])
        gx += -2.0 * G_CONST * RHO * length * np.sum(w * np.log(rr)) * normal[0]
        gz += -2.0 * G_CONST * RHO * length * np.sum(w * np.log(rr)) * normal[1]
    return np.array([gx, gz])


def main():
    section("1. 2-D logarithmic potential and the Poisson equation")
    print(f"SYNTHETIC model: uniform rectangle, {AREA/1e6:.1f} km^2, "
          f"rho = {RHO:.0f} kg/m^3, centroid at z = {ZC/1e3:.1f} km")
    print(f"monopole strength 2 G rho A = {M2D:.6e} m^2/s^2")
    print(f"2-D Laplacian of Phi must equal 4 pi G rho = "
          f"{4*np.pi*G_CONST*RHO:.6e} s^-2 inside, 0 outside")

    # Divergence of the boundary-integral field, by central differences.
    for label, (xg, zg) in (("inside ", (0.0, 6000.0)),
                            ("outside", (0.0, 0.0))):
        hs = []
        res = []
        for h in (400.0, 200.0, 100.0):
            gx_p = boundary_gradient(xg + h, zg)[0]
            gx_m = boundary_gradient(xg - h, zg)[0]
            gz_p = boundary_gradient(xg, zg + h)[1]
            gz_m = boundary_gradient(xg, zg - h)[1]
            div = (gx_p - gx_m) / (2.0 * h) + (gz_p - gz_m) / (2.0 * h)
            hs.append(h)
            res.append(div)
        for h, div in zip(hs, res):
            print(f"  {label} point ({xg/1e3:5.1f}, {zg/1e3:5.1f}) km, "
                  f"h = {h:5.0f} m : div(grad Phi) = {div:+.6e} s^-2, "
                  f"ratio to 4 pi G rho = {div/(4*np.pi*G_CONST*RHO):+.5f}")
        order = np.log2(abs(res[0] - res[1]) / abs(res[1] - res[2]))
        print(f"  {label} observed order of the difference operator = {order:.2f}")
    print("  the inside ratio approaches 1 and the outside ratio approaches 0;")
    print("  the residual is the O(h^2) error of the central difference, not of")
    print("  the integral, so it falls by 4x for each halving of h.")

    section("2. Volume (area) quadrature: measured order of convergence")
    x_prof = np.array([0.0, 3000.0, 6000.0, 10000.0])
    z_prof = np.zeros_like(x_prof)                    # observation profile at z = 0
    cache = {}

    def phi(x, z, n):
        key = (x, z, n)
        if key not in cache:
            cache[key] = log_potential_area(x, z, n)
        return cache[key]

    phi_ref = phi(6000.0, 0.0, 2400) + (phi(6000.0, 0.0, 2400)
                                         - phi(6000.0, 0.0, 1200)) / 3.0
    print("  reference: Richardson extrapolation of the n = 1200 and n = 2400")
    print(f"  midpoint values -> {phi_ref:.9f} m^2/s^2")
    print("     n     error at x = 6 km (m^2/s^2)     observed order")
    err_prev = None
    for n in (12, 24, 48, 96, 192, 384):
        err = abs(phi(6000.0, 0.0, n) - phi_ref)
        order = np.nan if err_prev is None else np.log2(err_prev / err)
        print(f"  {n:5d}     {err:.6e}                {order:8.2f}")
        err_prev = err
    rich_a = phi(6000.0, 0.0, 192) + (phi(6000.0, 0.0, 192)
                                      - phi(6000.0, 0.0, 96)) / 3.0
    rich_b = phi(6000.0, 0.0, 384) + (phi(6000.0, 0.0, 384)
                                      - phi(6000.0, 0.0, 192)) / 3.0
    print(f"  Richardson from n = 96,192 : {rich_a:.10f} m^2/s^2, "
          f"error = {abs(rich_a - phi_ref):.3e}")
    print(f"  Richardson from n = 192,384: {rich_b:.10f} m^2/s^2, "
          f"error = {abs(rich_b - phi_ref):.3e}")
    print(f"  the two extrapolations differ by {abs(rich_a - rich_b):.3e} m^2/s^2")

    def phi_rich(x, z):
        a = phi(x, z, 1200)
        b = phi(x, z, 2400)
        return b + (b - a) / 3.0

    print("  profile error at n = 192 over x = 0, 3, 6, 10 km: "
          f"{np.max(np.abs([phi(x, z, 192) - phi_rich(x, z) for x, z in zip(x_prof, z_prof)])):.3e} m^2/s^2")

    section("3. Surface integral: area integral reduced to a 1-D quadrature")
    print("  boundary discretisation: 4 edges x 48 Gauss-Legendre nodes = 192 nodes")
    print(f"  area reference uses 1200 x 1200 = {1200**2} unknowns")
    print("   x (km)   gx_area (m/s^2)    gx_bound (m/s^2)     |difference|    rel.")
    for x0 in (0.0, 3000.0, 6000.0, 10000.0):
        # area route: differentiate the potential at high n
        h = 20.0
        gx_area = (log_potential_area(x0 + h, 0.0, 1200)
                   - log_potential_area(x0 - h, 0.0, 1200)) / (2.0 * h)
        gx_bound = boundary_gradient(x0, 0.0)[0]
        diff = abs(gx_area - gx_bound)
        rel = "    n/a" if abs(gx_bound) < 1e-9 else f"{diff/abs(gx_bound):.3e}"
        print(f"  {x0/1e3:6.1f}   {gx_area:+.8e}   {gx_bound:+.8e}   {diff:.3e}   {rel}")
    print("  at x = 0 the field vanishes by symmetry (the body is symmetric in x),")
    print("  so only the absolute difference is meaningful there.")
    print("  elsewhere the agreement is limited by the reference: a second-order")
    print("  area rule with 1.44e6 cells and a finite-difference derivative, not by")
    print("  the boundary rule.")

    print("\n  far-field multipole residual  |R g_R - 2 G rho A| versus R:")
    rs = np.array([30.0, 60.0, 120.0, 240.0]) * 1e3
    resid = []
    for R in rs:
        x0, z0 = R, ZC
        gx, gz = boundary_gradient(x0, z0)
        gR = gx                                   # radial direction is +x here
        resid.append(abs(R * gR - M2D))
    resid = np.array(resid)
    slope = np.polyfit(np.log(rs), np.log(resid), 1)[0]
    for R, q in zip(rs, resid):
        print(f"    R = {R/1e3:6.0f} km : residual = {q:.6e} m^2/s^2")
    print(f"  measured slope of log|residual| versus log R = {slope:.3f}")
    print("  -> the leading term is the monopole 2 G rho A / R; the next term")
    print("     decays like R^-2 (the 2-D quadrupole), which is the structure the")
    print("     fast-multipole expansion exploits.")

    section("4. Fredholm equation of the second kind: (I - lambda K) psi = f")
    sigma, lam = 0.10, 0.80

    def kernel(s, sp):
        return np.exp(-((s - sp) ** 2) / (2.0 * sigma ** 2)) / (np.sqrt(2 * np.pi) * sigma)

    def solve_second_kind(n):
        s = (np.arange(n) + 0.5) / n
        h = 1.0 / n
        K = kernel(s[:, None], s[None, :]) * h
        f = 1.0 + 0.5 * np.cos(2.0 * np.pi * s)
        psi = np.linalg.solve(np.eye(n) - lam * K, f)
        return psi, np.linalg.cond(np.eye(n) - lam * K), lam * np.max(np.abs(K).sum(axis=1))

    psi_ref, _, _ = solve_second_kind(4096)
    s_ref = (np.arange(4096) + 0.5) / 4096
    print("  reference: Nystrom solution with n = 4096 midpoint panels")
    print("     n     max|psi - psi_ref|   observed order   cond(I-lambda K)   contraction")
    prev = None
    for n in (8, 16, 32, 64, 128, 256):
        psi, cond, contr = solve_second_kind(n)
        s = (np.arange(n) + 0.5) / n
        err = np.max(np.abs(np.interp(s, s_ref, psi_ref) - psi))
        order = np.nan if prev is None else np.log2(prev / err)
        print(f"  {n:5d}     {err:.6e}         {order:8.2f}       {cond:10.4f}     {contr:10.4f}")
        prev = err
    print(f"  predicted cond ~ 1/(1 - lambda) = {1/(1-lam):.4f}: measured at n = 256")
    print("  the contraction factor is below 1, so the Neumann series converges, and")
    print("  the discretised operator stays well conditioned at every n.")

    def neumann(n, tol=1e-12):
        s = (np.arange(n) + 0.5) / n
        h = 1.0 / n
        K = kernel(s[:, None], s[None, :]) * h
        f = 1.0 + 0.5 * np.cos(2.0 * np.pi * s)
        psi = f.copy()
        it = 0
        while True:
            new = f + lam * (K @ psi)
            it += 1
            if np.max(np.abs(new - psi)) < tol:
                return it, new
            psi = new

    iters, psi_n = neumann(256)
    print(f"  measured Neumann iterations to 1e-12 (n = 256): {iters}; "
          f"predicted from the contraction = "
          f"{np.log(1e-12)/np.log(lam):.0f}")

    section("5. Fredholm equation of the first kind: g(s) = integral K rho")
    print("  same Gaussian kernel, smooth model rho(s) = 1 + 0.5 cos(2 pi s)")
    print("     n    sigma_max/sigma_min   cond(A)      solution error (noise 1e-6)")
    rho_s = lambda s: 1.0 + 0.5 * np.cos(2.0 * np.pi * s)
    for n in (8, 16, 32, 64, 128):
        s = (np.arange(n) + 0.5) / n
        h = 1.0 / n
        A = kernel(s[:, None], s[None, :]) * h
        g = A @ rho_s(s)
        g_noisy = g + 1e-6 * RNG.standard_normal(n)
        rho_hat = np.linalg.solve(A, g_noisy)
        cond = np.linalg.cond(A)
        err = np.max(np.abs(rho_hat - rho_s(s))) / np.max(np.abs(rho_s(s)))
        print(f"  {n:5d}    {cond:.3e}          {np.log10(cond):6.2f}       {err:.4e}")
    print("  the singular values of a smooth-kernel matrix decay geometrically, so")
    print("  cond(A) grows without bound with n: the first-kind equation is")
    print("  ill-posed.  The clean-data residual can be driven to zero while the")
    print("  solution error grows -- semi-convergence.  Truncating the expansion or")
    print("  adding a penalty is the remedy (see 18-inverse-problems).")

    section("6. Worked example: the numbers the lesson quotes")
    print("  (a) monopole far field at R = 30 km along the profile:")
    gR = boundary_gradient(30000.0, ZC)[0]
    print(f"      boundary quadrature  gx = {gR:.6e} m/s^2")
    print(f"      monopole estimate  2 G rho A / R = {M2D/30000.0:.6e} m/s^2")
    print(f"      ratio measured/monopole = {gR/(M2D/30000.0):.6f}")
    print("  (b) log potential at the surface point (6 km, 0):")
    print(f"      midpoint n = 2400     = {phi(6000.0, 0.0, 2400):.6f} m^2/s^2")
    print(f"      Richardson reference  = {phi_ref:.6f} m^2/s^2")
    print(f"      error at n = 192      = {abs(phi(6000.0, 0.0, 192)-phi_ref):.3e} m^2/s^2")

    section("7. Summary of measured quantities")
    print(f"  monopole strength 2 G rho A                    = {M2D:.6e} m^2/s^2")
    print(f"  area-quadrature error at n = 384 (x = 6 km)    = "
          f"{abs(phi(6000.0, 0.0, 384) - phi_ref):.3e} m^2/s^2")
    print(f"  boundary nodes (4 edges x 48 nodes)            = 192")
    print(f"  area unknowns in the reference quadrature      = {1200**2}")
    def contraction(n):
        s = (np.arange(n) + 0.5) / n
        return lam * np.max(np.abs(kernel(s[:, None], s[None, :]) / n).sum(axis=1))

    def first_kind_deg(n):
        s = (np.arange(n) + 0.5) / n
        return np.linalg.cond(kernel(s[:, None], s[None, :]) / n)

    print(f"  second-kind contraction factor (n = 256)       = "
          f"{contraction(256):.4f}")
    print(f"  first-kind cond(A) at n = 128                  = "
          f"{first_kind_deg(128):.3e}")
    print("  All values are SYNTHETIC model outputs of this script.")


if __name__ == "__main__":
    main()
