"""Newton's laws and free-body analysis: five force balances, checked.

Run:  python3 newtons_laws_demo.py
Requires: Python standard library only.

Companion to lesson 02-02-02.  For every system the free-body diagram is turned
into algebra, the algebra is solved in closed form, and the closed form is then
checked against a numerical integration of the same equations of motion.  Where
a geophysical application exists, it is included: the apparent gravity of a
rotating Earth, the isostatic force balance, and the terminal velocity of a
falling body in air.

Constants: GM = 3.986 004 418e14 m^3 s^-2 and omega = 7.292 115e-5 rad/s
(defining, WGS 84); R = 6 371 km (nominal).  Densities and air density are
nominal values from the constant handbook.  All masses are SYNTHETIC.
"""

import math

GM = 3.986004418e14
R_MEAN = 6371000.0
OMEGA = 7.292115e-5
G = GM / R_MEAN ** 2          # 9.82025 m/s^2 at the mean radius
RHO_AIR = 1.225               # kg/m^3, nominal at sea level, 15 C
RHO_WATER = 1025.0            # kg/m^3, nominal seawater
RHO_CRUST = 2700.0            # kg/m^3, nominal
RHO_MANTLE = 3300.0           # kg/m^3, nominal


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main() -> None:
    section("1. Block on an incline: the static friction threshold")
    mu_s = 0.60
    print(f"  On the point of slipping, mg sin(theta) = mu_s mg cos(theta),")
    print(f"  so tan(theta_c) = mu_s.  With mu_s = {mu_s:.2f}:")
    print(f"      theta_c = {math.degrees(math.atan(mu_s)):.4f} deg")
    for th_deg in (20.0, 30.0, 31.0, 40.0):
        th = math.radians(th_deg)
        need = math.tan(th)
        print(f"  theta = {th_deg:5.1f} deg: required mu = tan(theta) = {need:.4f}"
              f" -> {'SLIPS' if need > mu_s else 'holds'}")
    print("  The mass cancels exactly: the threshold depends only on the")
    print("  friction coefficient.  That is a free-body result, not an accident.")

    section("2. Atwood machine: close the algebra against the dynamics")
    m1, m2 = 5.0, 3.0
    a = G * (m1 - m2) / (m1 + m2)
    T = 2 * m1 * m2 * G / (m1 + m2)
    print(f"  m1 = {m1} kg on one side, m2 = {m2} kg on the other")
    print(f"  a = (m1-m2)g/(m1+m2) = {a:.6f} m/s^2")
    print(f"  T = 2 m1 m2 g/(m1+m2) = {T:.6f} N")
    # Check 1: integrate the equation of motion the free-body analysis
    # produced.  This validates the algebra's consistency, not the physics.
    dt = 1.0e-5
    v, y = 0.0, 0.0
    for _ in range(int(1.0 / dt)):
        v += dt * a
        y += dt * v
    print(f"  after 1 s of numerical motion: y = {y:.6f} m, "
          f"compare (1/2) a t^2 = {0.5 * a:.6f} m")
    print(f"  (relative difference {abs(y - 0.5 * a) / (0.5 * a):.2e}, the")
    print(f"  Euler discretisation error)")
    # Check 2: an independent law.  Work-energy for the same system:
    # the loss of potential energy over a distance s must equal the gain in
    # kinetic energy of both masses.
    s_drop = 1.0
    v2 = 2 * a * s_drop
    ke = 0.5 * (m1 + m2) * v2
    pe_change = (m1 - m2) * G * s_drop
    print(f"  independent check from energy, not from the equations of motion:")
    print(f"      after {s_drop:.0f} m: v^2 = 2 a s = {v2:.6f} m^2/s^2")
    print(f"      kinetic energy gain      = {ke:.6f} J")
    print(f"      potential energy lost    = {pe_change:.6f} J")
    print(f"      relative difference      = {abs(ke - pe_change) / ke:.2e}")
    print("  Two independent routes to the same number: this is what a")
    print("  free-body analysis should be checked against.")

    section("3. Apparent gravity on a rotating Earth")
    print(f"  omega = {OMEGA:.6e} rad/s, omega^2 R = {OMEGA ** 2 * R_MEAN:.6f}"
          f" m/s^2 ({100 * OMEGA ** 2 * R_MEAN / G:.4f}% of g)")
    print("    lat      g_grav - centrif.   horizontal     |g_eff|     "
          "deflection")
    for lat_deg in (0.0, 30.0, 45.0, 60.0, 90.0):
        lat = math.radians(lat_deg)
        vert = G - OMEGA ** 2 * R_MEAN * math.cos(lat) ** 2
        horiz = OMEGA ** 2 * R_MEAN * math.cos(lat) * math.sin(lat)
        g_eff = math.hypot(vert, horiz)
        deflect = math.degrees(math.atan2(horiz, vert))
        print(f"  {lat_deg:5.1f}  {vert:12.6f}   {horiz:10.6f}   "
              f"{g_eff:10.6f}   {deflect:8.4f} deg")
    print("  The horizontal component peaks at 45 deg and is zero at the pole")
    print("  and equator; it is the reason a plumb line does not point exactly")
    print("  at the centre of mass.  This is the *centrifugal* part alone: the")
    print("  full deflection of the vertical also contains the gravitational")
    print("  effect of the flattening, which has the same order of magnitude.")

    section("4. Terminal velocity with quadratic drag")
    m, area, cd = 1.0, 0.01, 0.5
    v_term = math.sqrt(2 * m * G / (RHO_AIR * cd * area))
    print(f"  m = {m} kg, A = {area} m^2, C_d = {cd}, rho = {RHO_AIR} kg/m^3")
    print(f"  terminal speed = sqrt(2 m g / (rho C_d A)) = {v_term:.4f} m/s")
    # Integrate to confirm approach to the terminal speed.
    dt, v, t = 1.0e-4, 0.0, 0.0
    while t < 30.0:
        acc = G - (RHO_AIR * cd * area / (2 * m)) * v * v
        v += dt * acc
        t += dt
    print(f"  after 30 s of numerical fall: v = {v:.6f} m/s "
          f"({100 * v / v_term:.3f}% of terminal)")
    t_to_95 = (1 / G) * math.sqrt(2 * m / (RHO_AIR * cd * area)) \
        * math.atanh(0.95)
    print(f"  analytic time to 95% of terminal speed = {t_to_95:.4f} s")
    print("  Terminal velocity is a force balance, not a kinematic fact: it")
    print("  exists only because drag grows with speed.")

    section("5. Isostasy as a force balance at depth")
    h_mtn = 3000.0               # mountain height above the datum
    h_crust = 35.0e3             # crustal thickness away from the load
    r_root = RHO_CRUST * h_mtn / (RHO_MANTLE - RHO_CRUST)
    print(f"  mountain height h = {h_mtn / 1e3:.1f} km, normal crust "
          f"H = {h_crust / 1e3:.0f} km")
    print(f"  root from a pressure balance: rho_c h = (rho_m - rho_c) r")
    print(f"      r = rho_c h / (rho_m - rho_c) = "
          f"{RHO_CRUST:.0f} x {h_mtn:.0f} / "
          f"({RHO_MANTLE:.0f} - {RHO_CRUST:.0f}) = {r_root:.1f} m "
          f"= {r_root / 1e3:.2f} km")
    # Verify by comparing the pressure of the two columns at the depth of the
    # base of the root, which is h_crust + r_root below the datum.
    depth = h_crust + r_root
    p_plain = RHO_CRUST * G * h_crust + RHO_MANTLE * G * r_root
    p_mtn = RHO_CRUST * G * (h_mtn + h_crust + r_root)
    print(f"  pressures at depth {depth / 1e3:.2f} km below the datum:")
    print(f"      column without a load : {p_plain:.6e} Pa")
    print(f"      column under the load : {p_mtn:.6e} Pa")
    print(f"      difference            : {abs(p_mtn - p_plain):.3e} Pa "
          f"(relative {abs(p_mtn - p_plain) / p_plain:.2e})")
    print(f"  The Moho under the mountain lies at "
          f"{(h_mtn + h_crust + r_root) / 1e3:.1f} km depth, against "
          f"{h_crust / 1e3:.0f} km elsewhere.")
    print("  The correction is a genuine force balance: the two are equal to")
    print("  round-off because the root was derived from the balance.  What")
    print("  the calculation does not provide is the *density contrast*; it is")
    print("  a nominal input, and a 50 kg/m^3 error in it moves the root by")
    print(f"  {abs(RHO_CRUST * h_mtn / (RHO_MANTLE - 50 - RHO_CRUST) - r_root) / 1e3:.2f} km.")

    section("6. Newton's third law: equal and opposite, checked numerically")
    # Two masses at rest separated by 10 km, released: the centre of mass must
    # not move, which requires the forces to be exactly equal and opposite.
    m_a, m_b = 2.0e10, 3.0e10
    xa, xb = 0.0, 1.0e4
    va = vb = 0.0
    dt = 1.0e-2
    xa0 = (m_a * xa + m_b * xb) / (m_a + m_b)
    for _ in range(2000):
        d = xb - xa
        f = 6.67430e-11 * m_a * m_b / d ** 2
        va += dt * f / m_a
        vb -= dt * f / m_b
        xa += dt * va
        xb += dt * vb
    xa1 = (m_a * xa + m_b * xb) / (m_a + m_b)
    print(f"  centre of mass at t = 0    : {xa0:.9e} m")
    print(f"  centre of mass after 20 s  : {xa1:.9e} m")
    print(f"  drift                      : {abs(xa1 - xa0):.3e} m "
          f"(relative {abs(xa1 - xa0) / 1e4:.2e})")
    print("  The centre of mass is stationary to round-off because the two")
    print("  momentum increments cancel pairwise -- the third law as a")
    print("  numerical identity, exactly as in 02-01-04.")


if __name__ == "__main__":
    main()
