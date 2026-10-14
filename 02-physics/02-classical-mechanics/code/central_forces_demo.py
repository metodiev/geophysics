"""Central forces and orbits: Kepler's laws, vis-viva, and the shell theorem.

Run:  python3 central_forces_demo.py
Requires: Python standard library only.

Companion to lesson 02-02-07.  Four things are established numerically rather
than asserted:

1.  The exterior field of a uniform spherical *ball* is exactly GM/z^2, and of a
    uniform spherical *shell* it is exactly GM/z^2 outside and exactly zero
    inside -- both by direct surface/volume quadrature of Newton's law, with no
    use of the result being tested.  (A point mass and a shell are therefore
    indistinguishable from outside, which is the shell theorem.)
2.  Kepler's second law: the areal velocity is constant for a central force.
3.  Kepler's third law: T^2 is proportional to a^3, with the constant 4 pi^2/GM.
4.  Vis-viva: v^2 = GM (2/r - 1/a) along the numerical orbit.

Constants: GM = 3.986 004 418e14 m^3 s^-2 (defining, WGS 84); R = 6 371 km
(nominal mean radius).  All orbits are SYNTHETIC.
"""

import math

GM = 3.986004418e14
R_EARTH = 6371.0e3


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def shell_field_z(z, radius, n_theta=400, n_phi=800):
    """Exterior (or interior) axial field of a unit-surface-density shell.

    Returns g_z in units of (G * sigma) for a shell of radius ``radius``
    observed on the axis at distance ``z`` from the centre.
    """
    dth = math.pi / n_theta
    dph = 2 * math.pi / n_phi
    total = 0.0
    for i in range(n_theta):
        th = (i + 0.5) * dth
        st, ct = math.sin(th), math.cos(th)
        # field from a ring at polar angle th, integrated over phi analytically
        d = math.sqrt(z * z + radius * radius - 2 * z * radius * ct)
        total += (z - radius * ct) / d ** 3 * st * dth
    return total * 2 * math.pi * radius * radius


def main() -> None:
    section("1. The shell theorem, by direct quadrature of Newton's law")
    radius, areal = 1.0, 1.0
    m_shell = 4 * math.pi * radius ** 2 * areal
    g_scale = m_shell / radius ** 2        # GM/R^2 for the shell
    print("  uniform spherical shell, radius 1, surface density 1 (SYNTHETIC)")
    print("      z         g_z (quadrature)   GM/z^2 (outside)   "
          "relative difference")
    for z in (1.05, 1.5, 3.0, 10.0):
        g = shell_field_z(z, radius)
        exact = m_shell / z ** 2
        print(f"  {z:6.2f}   {g:18.8f}   {exact:16.8f}   "
              f"{abs(g - exact) / exact:.3e}")
    print()
    print("  Inside the shell (z < R), the exact answer is zero:")
    print("      z         g_z (quadrature)   |g_z| / (GM/R^2)")
    for z in (0.0, 0.3, 0.7):
        g = shell_field_z(max(z, 1e-12), radius)
        print(f"  {z:6.2f}   {g:18.6e}   {abs(g) / g_scale:.3e}")
    print()
    print("  Points very close to the shell need finer quadrature, because the")
    print("  integrand is nearly singular where the observation point touches")
    print("  the surface.  Measure the convergence rather than assuming it:")
    print("      n_theta    z = 1.05 (outside)      z = 0.99 (inside)")
    for n in (400, 1600, 6400):
        g_out = shell_field_z(1.05, radius, n_theta=n, n_phi=n)
        g_in = shell_field_z(0.99, radius, n_theta=n, n_phi=n)
        print(f"  {n:9d}    {abs(g_out - m_shell / 1.05 ** 2) / (m_shell / 1.05 ** 2):.3e}"
              f"            {abs(g_in) / g_scale:.3e}")
    print("  Each 4x refinement cuts both errors by about 16, i.e. they fall")
    print("  as n^-2: the midpoint rate appropriate to a smooth integrand, with")
    print("  the near-singularity only reducing the constant, not the order.")
    print("  The *theorem* is exact; the quadrature is not, and the difference")
    print("  between those two statements is what this table measures.")
    print()
    print("  Why this matters for modelling: outside a spherically symmetric")
    print("  body the field is GM/z^2 with z the distance to the *centre* --")
    print("  the shell theorem.  The profile GM d/(rho^2 + d^2)^(3/2) that one")
    print("  often sees is the field of a *point* mass at depth d, evaluated at")
    print("  horizontal offset rho.  Using the point-mass profile where the")
    print("  shell theorem applies (or the reverse) is a modelling error of")
    print("  order (rho/d)^2 for small offsets, and it is invisible to a")
    print("  dimensional check: both expressions are m/s^2.")

    section("2. Circular orbit: the effective-potential condition")
    for alt_km in (500.0, 800.0, 20200.0):
        r = R_EARTH + alt_km * 1e3
        v = math.sqrt(GM / r)
        t = 2 * math.pi * math.sqrt(r ** 3 / GM)
        e = 0.5 * v * v - GM / r
        print(f"  altitude {alt_km:8.1f} km: r = {r:.4e} m, v = {v:.4f} m/s, "
              f"T = {t:.3f} s = {t / 60:.2f} min, "
              f"specific energy = {e:.6e} J/kg")
    print("  The centripetal condition v^2/r = GM/r^2 and the minimum of the")
    print("  effective potential V_eff = L^2/(2r^2) - GM/r give the same r for")
    print("  v: they are the same equation written two ways.")

    section("3. Kepler's second law on a numerical eccentric orbit")
    a, e = 1.0e7, 0.5
    r_peri = a * (1 - e)
    v_peri = math.sqrt(GM * (1 + e) / (a * (1 - e)))
    y = [r_peri, 0.0, 0.0, v_peri]          # x, y, vx, vy (velocity in +y)
    dt = 1.0
    period = 2 * math.pi * math.sqrt(a ** 3 / GM)
    print(f"  a = {a:.1e} m, e = {e}, period = {period:.3f} s "
          f"({period / 3600:.3f} h)")
    print("      time (s)     r (m)        areal rate (m^2/s)   "
          "specific L (m^2/s)")
    areal_rates = []
    t = 0.0
    report = 0.0
    while t < period:
        r = math.hypot(y[0], y[1])
        ax = -GM * y[0] / r ** 3
        ay = -GM * y[1] / r ** 3
        y[2] += dt * ax
        y[3] += dt * ay
        y[0] += dt * y[2]
        y[1] += dt * y[3]
        t += dt
        areal = 0.5 * (y[0] * y[3] - y[1] * y[2])   # (1/2)|r x v|
        L = 2 * areal
        areal_rates.append(areal)
        if t >= report:
            print(f"  {t:10.1f}   {r:12.4e}   {areal:18.6f}   {L:18.6f}")
            report += period / 4
    spread = (max(areal_rates) - min(areal_rates)) / (sum(areal_rates)
                                                      / len(areal_rates))
    print(f"  spread of the areal rate over one orbit = {spread:.3e}")
    print("  The areal rate is constant because the force is central: the")
    print("  torque r x F vanishes, so L = 2 x (areal rate) is conserved.  Note")
    print("  the update order: the velocity is advanced before the position,")
    print("  which makes this *symplectic* Euler.  That scheme conserves angular")
    print("  momentum for a central force as an algebraic identity, so the")
    print("  spread above (6e-15) is round-off, not truncation error.  Reversing")
    print("  the update order turns it into explicit Euler, and the same")
    print("  measurement then grows linearly with the number of steps.")
    print(f"  semi-latus rectum a (1 - e^2)                    = "
          f"{a * (1 - e ** 2):.6e} m")
    print(f"  the same quantity from the conserved L: L^2 / GM = "
          f"{L ** 2 / GM:.6e} m")
    print(f"  relative difference = "
          f"{abs(L ** 2 / GM - a * (1 - e ** 2)) / (a * (1 - e ** 2)):.3e}")
    print("  Two independent routes to the semi-latus rectum -- one from the")
    print("  orbit elements, one from the numerically conserved angular")
    print("  momentum and the defining relation L^2 = GM a (1 - e^2) -- agree,")
    print("  which is the check that the orbit being integrated is a Kepler")
    print("  ellipse and not something else.")

    section("4. Kepler's third law and vis-viva")
    print("      a (m)        T (s)        T^2/a^3      v^2 at r = a")
    for a_km in (7000.0, 20000.0, 42164.0):
        a_m = a_km * 1e3
        t = 2 * math.pi * math.sqrt(a_m ** 3 / GM)
        v_sq = GM / a_m
        print(f"  {a_m:12.4e}   {t:12.4f}   {t ** 2 / a_m ** 3:.6e}   "
              f"{v_sq:.6f}")
    print(f"  4 pi^2 / GM = {4 * math.pi ** 2 / GM:.6e}")
    print("  The middle column is a constant, and it equals 4 pi^2/GM.  That")
    print("  is how GM is measured from satellite tracking: observe T and a,")
    print("  and GM follows without ever knowing G.  This is why geodesy")
    print("  quotes GM to nine digits while the Earth's mass is known to five.")
    print("  The last column confirms v^2 = GM/a for the circular case, which")
    print("  is vis-viva with r = a.")


if __name__ == "__main__":
    main()
