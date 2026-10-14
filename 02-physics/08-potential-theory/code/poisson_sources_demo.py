#!/usr/bin/env python3
"""Poisson's equation: sources, superposition and source equivalence.

Standard library only.  Every printed number is computed here.

Contents
--------
1. Superposition: an exact identity (a prism split in two) and a composite body
   checked with one brute-force integrator.
2. A right rectangular prism by closed form (Nagy's formula) against 3-D volume
   quadrature -- two independent routes to the same number.
3. The infinite-slab limit g_z = 2 pi G rho t, and how a finite prism approaches
   it.  The slab's insensitivity to depth is the first appearance of the slab
   ambiguity that lesson 06 turns into a statement about non-uniqueness.
4. Source equivalence in magnetics: a uniformly magnetised sphere, its surface
   charge layer and its dipole are three descriptions of one exterior field.
5. Source equivalence in gravity: a thin body of thickness t and density rho is
   equivalent to a surface layer of areal density rho*t, with an O(t) error
   shown to shrink as t shrinks.
"""

import math

G = 6.67430e-11  # CODATA 2018 measured value


def gauss_legendre(n):
    x = [math.cos(math.pi * (i + 0.75) / (n + 0.5)) for i in range(n)]
    w = [0.0] * n
    for i in range(n):
        dp = 1.0
        for _ in range(100):
            p0, p1 = 1.0, x[i]
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x[i] * p1 - (k - 1) * p0) / k
            dp = n * (x[i] * p1 - p0) / (x[i] * x[i] - 1.0)
            dx = -p1 / dp
            x[i] += dx
            if abs(dx) < 1e-16:
                break
        w[i] = 2.0 / ((1.0 - x[i] * x[i]) * dp * dp)
    return x, w


def prism_gz(rho, bx, by, bz, x0=0.0, y0=0.0, z0=0.0):
    """Vertical gravity of a right rectangular prism (Nagy's closed form).

    The prism occupies bx = (x1, x2), by = (y1, y2), bz = (z1, z2); the observer
    is at (x0, y0, z0).  z is positive DOWNWARD, so bz > 0 lies below the
    observer and the returned value is the downward component.
    """
    s = 0.0
    for i, xi in enumerate(bx):
        for j, yj in enumerate(by):
            for k, zk in enumerate(bz):
                X = xi - x0
                Y = yj - y0
                Z = zk - z0
                r = math.sqrt(X * X + Y * Y + Z * Z)
                term = (X * math.log(Y + r) + Y * math.log(X + r)
                        - Z * math.atan2(X * Y, Z * r))
                s += (-1) ** (i + j + k) * term
    return G * rho * s


def prism_gz_quad(rho, bx, by, bz, x0=0.0, y0=0.0, z0=0.0, n=40):
    """The same quantity by midpoint volume quadrature."""
    tot = 0.0
    dx = (bx[1] - bx[0]) / n
    dy = (by[1] - by[0]) / n
    dz = (bz[1] - bz[0]) / n
    for i in range(n):
        X = bx[0] + (i + 0.5) * dx - x0
        for j in range(n):
            Y = by[0] + (j + 0.5) * dy - y0
            for k in range(n):
                Z = bz[0] + (k + 0.5) * dz - z0
                r2 = X * X + Y * Y + Z * Z
                tot += Z / (r2 * math.sqrt(r2)) * dx * dy * dz
    return G * rho * tot


def rectangle_surface_gz(sigma, rect, h, x0, y0, n=400):
    """Vertical field of a horizontal surface layer of density sigma at depth h."""
    tot = 0.0
    dx = (rect[1] - rect[0]) / n
    dy = (rect[3] - rect[2]) / n
    for i in range(n):
        X = rect[0] + (i + 0.5) * dx - x0
        for j in range(n):
            Y = rect[2] + (j + 0.5) * dy - y0
            r2 = X * X + Y * Y + h * h
            tot += h / (r2 * math.sqrt(r2)) * dx * dy
    return G * sigma * tot


def magnetic_surface_integral(M, a, r, theta, ncos=200, nphi=400):
    """Integral of sigma_m / |r - r'| dA' over a uniformly magnetised sphere.

    sigma_m = M cos(theta') is the fictitious surface magnetic charge; (1/4 pi)
    of the returned integral is the exterior scalar potential.  Source points lie
    on the sphere of radius a.
    """
    xc, wc = gauss_legendre(ncos)
    dphi = 2 * math.pi / nphi
    px = r * math.sin(theta)
    pz = r * math.cos(theta)
    tot = 0.0
    for i in range(ncos):
        ct = xc[i]
        st = math.sqrt(max(0.0, 1.0 - ct * ct))
        w_th = a * a * wc[i] * dphi * M * ct
        for j in range(nphi):
            phi = j * dphi
            dx = px - a * st * math.cos(phi)
            dy = 0.0 - a * st * math.sin(phi)
            dz = pz - a * ct
            tot += w_th / math.sqrt(dx * dx + dy * dy + dz * dz)
    return tot


def rule(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def main():
    print("Poisson's equation: sources, superposition and source equivalence")
    print("G = %.5e m^3 kg^-1 s^-2 (CODATA 2018, measured)" % G)

    # ---------------------------------------------------------------- 1
    rule("1. Superposition")
    rho_p = 2700.0
    prism = ((-800.0, 800.0), (-600.0, 600.0), (600.0, 900.0))
    whole = prism_gz(rho_p, *prism)
    left = prism_gz(rho_p, (-800.0, 0.0), prism[1], prism[2])
    right = prism_gz(rho_p, (0.0, 800.0), prism[1], prism[2])
    print("  (a) Exact identity: one prism split into two halves.")
    print("      whole prism      g_z = %.12e" % whole)
    print("      left half        g_z = %.12e" % left)
    print("      right half       g_z = %.12e" % right)
    print("      left + right     g_z = %.12e" % (left + right))
    print("      rel.diff         = %.3e" % (abs(whole - (left + right)) / abs(whole)))
    print()
    print("  (b) Composite body: two prisms of different densities at different")
    print("      depths, integrated once on a grid whose cell size divides every")
    print("      body edge exactly, and compared with the sum of the parts.")
    b1 = ((-800.0, 800.0), (-600.0, 600.0), (600.0, 900.0))
    b2 = ((1200.0, 2400.0), (-400.0, 400.0), (1200.0, 1500.0))
    rho1, rho2 = 2700.0, 3100.0
    g1 = prism_gz(rho1, *b1)
    g2 = prism_gz(rho2, *b2)
    lo = (-1000.0, -800.0, 600.0)
    hi = (3000.0, 800.0, 1600.0)
    print("      prism 1 (closed form)      : %.10e" % g1)
    print("      prism 2 (closed form)      : %.10e" % g2)
    print("      sum of the parts (route A) : %.10e" % (g1 + g2))
    for n in (40, 80, 160):
        gB = 0.0
        dx = (hi[0] - lo[0]) / n
        dy = (hi[1] - lo[1]) / n
        dz = (hi[2] - lo[2]) / n
        for i in range(n):
            X = lo[0] + (i + 0.5) * dx
            for j in range(n):
                Y = lo[1] + (j + 0.5) * dy
                for k in range(n):
                    Z = lo[2] + (k + 0.5) * dz
                    dens = 0.0
                    if (b1[0][0] < X < b1[0][1] and b1[1][0] < Y < b1[1][1]
                            and b1[2][0] < Z < b1[2][1]):
                        dens = rho1
                    elif (b2[0][0] < X < b2[0][1] and b2[1][0] < Y < b2[1][1]
                          and b2[2][0] < Z < b2[2][1]):
                        dens = rho2
                    if dens == 0.0:
                        continue
                    r2 = X * X + Y * Y + Z * Z
                    gB += dens * Z / (r2 * math.sqrt(r2)) * dx * dy * dz
        gB *= G
        print("      route B, n = %3d            : %.10e   rel.diff A-B = %.3e"
              % (n, gB, abs(gB - (g1 + g2)) / abs(g1 + g2)))
    print("  Superposition is exact by linearity; what these numbers measure is")
    print("  the quadrature error of route B, which falls as the grid is refined.")

    # ---------------------------------------------------------------- 2
    rule("2. A prism: closed form (Nagy) against volume quadrature")
    print("  Prism 1600 x 1200 m, top 600 m depth, thickness 300 m, rho = 2700.")
    worst_prism = 0.0
    for xo in (0.0, 800.0, 1600.0, 3000.0):
        a = prism_gz(rho_p, *prism, x0=xo)
        b2 = prism_gz_quad(rho_p, *prism, x0=xo, n=80)
        worst_prism = max(worst_prism, abs(b2 - a) / abs(a))
        print("     x = %6.0f m: Nagy = %.10e   quad(n=80) = %.10e   rel.diff = %.2e"
              % (xo, a, b2, abs(b2 - a) / abs(a)))

    # ---------------------------------------------------------------- 3
    rule("3. The infinite-slab limit, and the approach to it")
    rho = 2650.0
    thick = 200.0
    slab = 2 * math.pi * G * rho * thick
    print("  Closed form: g_z = 2 pi G rho t for an infinite slab of thickness t.")
    print("     rho = %.0f kg/m^3, t = %.0f m -> g_z = %.10e m/s^2 = %.6f mGal"
          % (rho, thick, slab, slab * 1e5))
    print("  A finite prism (top 500 m deep) approaches it as its extent grows:")
    for half in (500.0, 2000.0, 10000.0, 100000.0, 1000000.0):
        g = prism_gz(rho, (-half, half), (-half, half), (500.0, 500.0 + thick))
        print("     half-width %9.0f m: g_z = %.10e   g_z / slab = %.8f"
              % (half, g, g / slab))
    print("  Depth dependence at a fixed half-width of 1e6 m:")
    for top in (100.0, 500.0, 2000.0, 5000.0):
        g = prism_gz(rho, (-1e6, 1e6), (-1e6, 1e6), (top, top + thick))
        print("     top depth %6.0f m: g_z = %.10e   g_z / slab = %.8f"
              % (top, g, g / slab))
    print("  The slab value itself is independent of depth; the finite prism only")
    print("  approaches it, and a deeper slab needs a larger extent to get as")
    print("  close.  That is the slab ambiguity: g_z constrains rho*t, not rho.")

    # ---------------------------------------------------------------- 4
    rule("4. Magnetic source equivalence: sphere = surface charge = dipole")
    print("  For a sphere of radius a uniformly magnetised with M along z, the")
    print("  fictitious surface charge is sigma_m = M cos(theta').  Its surface")
    print("  integral gives the exterior scalar potential")
    print("      V_m = (1/4 pi) * integral sigma_m / |r-r'| dA' ,")
    print("  which should equal the dipole potential m cos(theta)/(4 pi r^2) with")
    print("  m = (4 pi/3) a^3 M.")
    a = 1000.0
    Mage = 1.0
    worst_mag = 0.0
    for (r, theta_deg) in ((2000.0, 0.0), (2000.0, 45.0), (2000.0, 90.0),
                           (4000.0, 30.0), (2000.0, 120.0)):
        theta = math.radians(theta_deg)
        v_surface = magnetic_surface_integral(Mage, a, r, theta) / (4 * math.pi)
        m = 4.0 / 3.0 * math.pi * a ** 3 * Mage
        v_dipole = m * math.cos(theta) / (4 * math.pi * r * r)
        rel = abs(v_surface - v_dipole) / abs(v_dipole) if abs(v_dipole) > 1e-9 else 0.0
        worst_mag = max(worst_mag, rel)
        print("     r = %5.0f m, theta = %3.0f deg: V_m(surface) = %+.10e"
              % (r, theta_deg, v_surface))
        print("                                     V_m(dipole)  = %+.10e"
              % v_dipole)
        print("                                     rel.diff     = %.2e   abs.diff = %.2e"
              % (rel, abs(v_surface - v_dipole)))
    print("  Three descriptions -- uniform magnetisation, surface charge, dipole --")
    print("  give one exterior field.  This is the magnetics analogue of mass")
    print("  equivalence, and the reason reduction to pole is a legitimate")
    print("  operation on a measured field.")

    # ---------------------------------------------------------------- 5
    rule("5. Gravity source equivalence: a thin body equals a surface layer")
    rho_layer = 2700.0
    thick5 = 200.0
    rect = (-1000.0, 1000.0, -1000.0, 1000.0)
    x_obs = 900.0
    h_top = 400.0
    sigma_target = rho_layer * thick5
    print("  Hold the areal density rho*t = %.0f kg/m^2 fixed and let the thickness"
          % sigma_target)
    print("  go to zero; the body must approach a surface layer of that density.")
    g_surface = rectangle_surface_gz(sigma_target, rect, h_top, x_obs, 0.0, n=300)
    print("     surface layer, sigma = %.0f kg/m^2 : g_z = %.10e"
          % (sigma_target, g_surface))
    ratios = []
    for tt in (400.0, 200.0, 100.0, 50.0, 25.0):
        rho_t = sigma_target / tt
        g = prism_gz(rho_t, rect[0:2], rect[2:4], (h_top, h_top + tt), x0=x_obs)
        ratios.append(abs(g - g_surface) / g_surface)
        print("     t = %6.1f m, rho = %9.1f kg/m^3: g_z = %.10e   rel.diff = %.3e"
              % (tt, rho_t, g, abs(g - g_surface) / g_surface))
    print("  Successive ratios: %.3f, %.3f, %.3f, %.3f -- each halving of the"
          % tuple(ratios[i] / ratios[i + 1] for i in range(len(ratios) - 1)))
    print("  thickness halves the discrepancy, so the error is O(t) as predicted.")

    print()
    print("SUMMARY OF MEASURED AGREEMENTS (every value is program output)")
    print("  split-prism superposition, rel.diff   = %.2e"
          % (abs(whole - (left + right)) / abs(whole)))
    print("  prism closed form vs quadrature(n=80): worst rel.diff = %.2e"
          % worst_prism)
    print("  finite prism (half-width 1e6 m) / slab              = %.8f"
          % (prism_gz(rho, (-1e6, 1e6), (-1e6, 1e6), (500.0, 700.0)) / slab))
    print("  magnetised sphere: surface charge vs dipole, worst rel.diff = %.2e"
          % worst_mag)
    print("  thin body vs surface layer: O(t), ratio per halving ~ 2")


if __name__ == "__main__":
    main()
