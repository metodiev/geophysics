"""Pressure, density and gravity inside the Earth.

Run:  python3 interior_pressure_demo.py
Requires: Python standard library only.

Companion to lesson 02-11-01.

We build a spherically symmetric, layered *reference model* whose densities are
the rounded characteristic values tabulated in
26-reference-library/02-symbols-and-units/03-constant-handbook.md section 3.3.
Within each layer the density varies linearly with depth; there are density
jumps only at the Moho (35 km) and at the core-mantle boundary (2891 km),
because the rounded handbook ranges are continuous across the 410 km and
660 km discontinuities.

Nothing here is a measurement.  The model is an assumption; the interest is in
what the hydrostatic equation then *forces* to be true, and in how close the
resulting mass, gravity and moment of inertia come to the known values.

The script computes:

1. The layer table and the density profile rho(r).
2. The enclosed mass M(r) and the gravity g(r) = G M(r) / r^2.
3. The pressure by integrating dP/dr = -rho(r) g(r) inward from P(R) = 0.
4. Checks: total mass against the nominal Earth mass, and the moment of
   inertia factor C / (M R^2) against the nominal value about 0.33.
5. The seismic parameter phi = v_p^2 - (4/3) v_s^2 = K / rho from the handbook
   velocity ranges, and the Adams-Williamson density gradient rho g / phi,
   compared with the model's own gradient.
"""

import math

G = 6.67430e-11          # m^3 kg^-1 s^-2, CODATA (measured)
R_EARTH = 6.371e6        # m, nominal mean radius
M_EARTH = 5.972e24       # kg, nominal (derived from GM/G)
DR = 500.0               # m, radial step

# --------------------------------------------------------------------------
# The layered reference model.
#   (name, top depth km, base depth km, rho at top, rho at base)
# Densities: rounded characteristic values from the constant handbook s3.3.
# --------------------------------------------------------------------------
LAYERS = (
    ("crust",           0.0,   35.0, 2600.0,  2900.0),
    ("upper mantle",   35.0,  410.0, 3300.0,  3600.0),
    ("transition zone", 410.0,  660.0, 3600.0,  4400.0),
    ("lower mantle",  660.0, 2891.0, 4400.0,  5570.0),
    ("outer core",   2891.0, 5153.0, 9900.0, 12200.0),
    ("inner core",   5153.0, 6371.0, 12800.0, 13100.0),
)

# v_p, v_s ranges from the handbook s3.3, km/s: (vp_top, vp_base, vs_top, vs_base)
VEL = {
    "crust": (5.8, 6.5, 3.2, 3.7),
    "upper mantle": (8.1, 8.1, 4.5, 4.5),
    "transition zone": (9.1, 10.3, 5.0, 5.6),
    "lower mantle": (10.3, 13.7, 5.6, 7.3),
    "outer core": (8.0, 10.3, 0.0, 0.0),
    "inner core": (11.0, 11.3, 3.5, 3.7),
}


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def rho_of_depth(depth_km):
    """Density in kg/m^3 from the piecewise-linear layered model."""
    for _name, top, base, rt, rb in LAYERS:
        if top <= depth_km < base:
            frac = (depth_km - top) / (base - top)
            return rt + frac * (rb - rt)
    return LAYERS[-1][4]


def layer_of_depth(depth_km):
    for name, top, base, _rt, _rb in LAYERS:
        if top <= depth_km < base:
            return name
    return LAYERS[-1][0]


def velocities(depth_km):
    """(v_p, v_s) in km/s, linearly interpolated within each layer."""
    name = layer_of_depth(depth_km)
    top, base = 0.0, 0.0
    for lname, ltop, lbase, _rt, _rb in LAYERS:
        if lname == name:
            top, base = ltop, lbase
    frac = (depth_km - top) / (base - top)
    vp_t, vp_b, vs_t, vs_b = VEL[name]
    return vp_t + frac * (vp_b - vp_t), vs_t + frac * (vs_b - vs_t)


def seismic_parameter(depth_km):
    """phi = v_p^2 - (4/3) v_s^2 in m^2 s^-2, from the handbook velocity ranges."""
    vp, vs = velocities(depth_km)
    return (vp * vp - (4.0 / 3.0) * vs * vs) * 1e6


def build_profile():
    """Return (radii m, depths km, rhos) from the surface downward."""
    n = int(R_EARTH / DR)
    radii = [R_EARTH - i * DR for i in range(n + 1)]
    depths = [d / 1e3 for d in (R_EARTH - r for r in radii)]
    rhos = [rho_of_depth(d) for d in depths]
    return radii, depths, rhos


def integrate(radii, rhos):
    """Enclosed mass, gravity and pressure at each radius.

    M(r) = integral 4 pi r'^2 rho dr' from 0 to r
    g(r) = G M(r) / r^2
    P(r) = integral rho g dr' from r to R      (P(R) = 0)
    """
    n = len(radii)
    mass = [0.0] * n
    grav = [0.0] * n
    pres = [0.0] * n

    m = 0.0
    for i in range(n - 1, -1, -1):
        r = radii[i]
        m += 4.0 * math.pi * r * r * rhos[i] * DR
        mass[i] = m
        grav[i] = 0.0 if r == 0 else G * m / (r * r)

    p = 0.0
    for i in range(0, n):
        p += rhos[i] * grav[i] * DR
        pres[i] = p
    return mass, grav, pres


def at_depth(depths, values, target_km):
    """Value at the grid point closest to a target depth."""
    best = min(range(len(depths)), key=lambda i: abs(depths[i] - target_km))
    return values[best], depths[best]


def part1_model():
    section("1. Layered reference model (rounded handbook characteristics)")
    print(f"{'layer':<18}{'depth range (km)':>20}{'rho (kg/m3)':>20}")
    for name, top, base, rt, rb in LAYERS:
        print(f"{name:<18}{f'{top:.0f}-{base:.0f}':>20}"
              f"{f'{rt:.0f}-{rb:.0f}':>20}")
    print()
    print("  Density jumps occur only at the Moho (2900 -> 3300 kg/m3) and at")
    print("  the core-mantle boundary (5570 -> 9900 kg/m3). The 410 km and")
    print("  660 km boundaries are continuous in this rounded model.")


def part2_profiles(depths, rhos, grav, pres):
    section("2. Density, gravity, pressure and the seismic parameter")
    print(f"{'depth (km)':>11}{'rho (kg/m3)':>13}{'g (m/s2)':>11}"
          f"{'P (GPa)':>10}{'phi (km2/s2)':>15}{'K=rho*phi (GPa)':>18}")
    marks = (0, 35, 100, 410, 660, 1000, 2000, 2891, 3000, 4000, 5153,
             5500, 6000, 6370)
    for d in marks:
        rho, dd = at_depth(depths, rhos, d)
        g, _ = at_depth(depths, grav, d)
        p, _ = at_depth(depths, pres, d)
        phi = seismic_parameter(dd)
        print(f"{dd:>11.0f}{rho:>13.0f}{g:>11.3f}{p / 1e9:>10.2f}"
              f"{phi / 1e6:>15.2f}{rho * phi / 1e9:>18.1f}")
    print()
    print("  phi = v_p^2 - (4/3) v_s^2 = K/rho. The velocities are interpolated")
    print("  within each layer across the handbook ranges, so K at the base of")
    print("  the lower mantle uses v_p = 13.7 km/s and at the centre uses")
    print("  v_p = 11.3 km/s. K is a nominal anchor implied by those ranges,")
    print("  not a measured modulus.")
    print()
    print("  Read the phi column across 2891 km: rho rises from 5570 to 9900")
    print("  kg/m3 while v_p DROPS from 13.7 to 8.0 km/s, so phi collapses from")
    print("  116.6 to 64.0 km^2 s^-2. A jump in density in the opposite")
    print("  direction to the velocity jump cannot be self-compression of the")
    print("  same material: it requires a change of composition.")


def part3_checks(radii, depths, rhos, mass, grav, pres):
    section("3. Checks against known Earth values")
    m_total = mass[0]
    print(f"  model mass          = {m_total:.4e} kg")
    print(f"  nominal Earth mass  = {M_EARTH:.4e} kg")
    print(f"  ratio               = {m_total / M_EARTH:.5f}")
    print()
    c = 0.0
    for i in range(len(radii)):
        r = radii[i]
        c += (2.0 / 3.0) * r * r * rhos[i] * 4.0 * math.pi * r * r * DR
    print(f"  model C/(M R^2)     = {c / (m_total * R_EARTH ** 2):.4f}"
          "   (nominal Earth value ~0.33)")
    print()
    p_c, _ = at_depth(depths, pres, 6371.0)
    print(f"  model centre pressure = {p_c / 1e9:.1f} GPa")
    print("  The reference model gives a centre pressure of order 360 GPa; the")
    print("  exact number is set by the density profile you assume.")
    print()
    p_cmb, d_cmb = at_depth(depths, pres, 2891.0)
    g_cmb, _ = at_depth(depths, grav, 2891.0)
    p_icb, d_icb = at_depth(depths, pres, 5153.0)
    g_icb, _ = at_depth(depths, grav, 5153.0)
    print(f"  core-mantle boundary  at {d_cmb:.0f} km: P = {p_cmb / 1e9:.1f} GPa,"
          f" g = {g_cmb:.2f} m/s2")
    print(f"  inner-core boundary   at {d_icb:.0f} km: P = {p_icb / 1e9:.1f} GPa,"
          f" g = {g_icb:.2f} m/s2")
    print(f"  surface gravity       g = {grav[0]:.4f} m/s2"
          "   (standard gravity 9.80665 m/s2)")
    print(f"  g at 3000 km depth    = "
          f"{at_depth(depths, grav, 3000)[0]:.3f} m/s2")
    print(f"  g at the centre       = {grav[-1]:.3e} m/s2")


def part4_adams_williamson(depths, rhos, grav):
    section("4. Adams-Williamson: the adiabatic density gradient")
    print("  d rho / dz = rho g / phi        (z increasing downward)")
    print()
    print(f"{'region':<16}{'z mid':>7}{'rho':>7}{'g':>7}{'phi':>7}"
          f"{'A-W':>8}{'model':>8}{'ratio':>7}")
    for name, top, base, _rt, _rb in LAYERS:
        if name == "crust":
            continue
        mid = 0.5 * (top + base)
        rho, _ = at_depth(depths, rhos, mid)
        g, _ = at_depth(depths, grav, mid)
        phi = seismic_parameter(mid)
        aw = rho * g / phi * 1e3                      # kg/m^3 per km
        model = (rho_of_depth(base - 1.0) - rho_of_depth(top)) / (base - top)
        print(f"{name:<16}{mid:>7.0f}{rho:>7.0f}{g:>7.2f}{phi / 1e6:>7.1f}"
              f"{aw:>8.3f}{model:>8.3f}{aw / model:>7.2f}")
    print()
    print("  Units: rho g / phi has units (kg m^-3)(m s^-2)/(m^2 s^-2) =")
    print("  kg m^-3 m^-1; multiplying by 1e3 gives kg m^-3 km^-1. The model")
    print("  gradient is (rho at layer base - rho at layer top) / thickness.")
    print()
    print("  Interpretation of the ratio, A-W / model:")
    print("    ratio ~ 1  the density gradient is what adiabatic self-")
    print("               compression of a homogeneous layer would give")
    print("    ratio << 1 the gradient is supplied by something else, here the")
    print("               mineral phase changes of the transition zone (0.22)")
    print("    ratio > 1  the model thins less than adiabatic compression")
    print("               requires, i.e. the layer is not self-compressed")


def part5_s_values():
    section("5. Why v_s = 0 means the outer core is liquid")
    print("  v_p = sqrt((K + 4 mu/3)/rho)      v_s = sqrt(mu/rho)")
    print("  A fluid at rest supports no shear stress: mu = 0 => v_s = 0.")
    print()
    print("  Check the last two columns of section 2 against these formulae:")
    print("  with K and rho from section 2 and mu = 0 in the outer core,")
    print("  v_s = 0 there while v_p = sqrt(K/rho) = sqrt(634e9/9900) = 8.00 km/s.")
    print()
    print(f"{'medium':<16}{'K (GPa)':>9}{'mu (GPa)':>10}{'rho':>7}"
          f"{'v_p km/s':>10}{'v_s km/s':>10}{'v_p/v_s':>9}")
    media = (
        ("crustal rock", 50.0, 26.0, 2700.0),
        ("upper mantle", 127.0, 66.0, 3300.0),
        ("lower mantle", 283.0, 134.0, 4400.0),
        ("outer core", 634.0, 0.0, 9900.0),
        ("inner core", 1340.0, 161.0, 12800.0),
    )
    for name, K, mu, rho in media:
        vp = math.sqrt((K * 1e9 + 4.0 * mu * 1e9 / 3.0) / rho)
        vs = math.sqrt(mu * 1e9 / rho)
        ratio = f"{vp / vs:.3f}" if vs > 0 else "inf"
        print(f"{name:<16}{K:>9.0f}{mu:>10.0f}{rho:>7.0f}{vp / 1e3:>10.3f}"
              f"{vs / 1e3:>10.3f}{ratio:>9}")
    print()
    print("  The K values are the section-2 values at the layer tops; mu is")
    print("  chosen so that the resulting v_p and v_s reproduce the handbook")
    print("  ranges, so this table is a consistency check, not a measurement.")
    print("  A Poisson solid (lambda = mu) gives v_p/v_s = sqrt(3) = 1.732; the")
    print("  mantle is nearer 1.8 and the inner core near 3, which is a")
    print("  statement about how mu compares with K.")


def part6_verification():
    section("6. Verification of the integrator against exact solutions")
    print("  A numerical integrator is worthless until it has reproduced a")
    print("  case that can be solved in closed form. Two such cases exist for")
    print("  hydrostatic balance in a sphere.")
    print()
    # (a) uniform sphere
    rho_uni = M_EARTH / ((4.0 / 3.0) * math.pi * R_EARTH ** 3)
    radii, depths, rhos = build_profile()
    rhos_uni = [rho_uni] * len(radii)
    mass_u, grav_u, pres_u = integrate(radii, rhos_uni)
    p_num_uni = pres_u[-1]
    p_exact_uni = 3.0 * G * M_EARTH ** 2 / (8.0 * math.pi * R_EARTH ** 4)
    print("  (a) Uniform sphere, exact P_c = 3 G M^2 / (8 pi R^4):")
    print(f"      rho = {rho_uni:.1f} kg/m3  (mean density)")
    print(f"      numerical P_c = {p_num_uni / 1e9:.4f} GPa")
    print(f"      exact     P_c = {p_exact_uni / 1e9:.4f} GPa")
    print(f"      relative difference = "
          f"{(p_num_uni - p_exact_uni) / p_exact_uni:.3e}")
    print(f"      numerical M   = {mass_u[0]:.6e} kg  "
          f"(constructed to equal {M_EARTH:.3e} kg)")
    print()
    # (b) two-layer planet with an analytically integrable profile
    r_c = 3.480e6
    rho_c, rho_m = 12576.0, 4138.0
    radii2 = [R_EARTH - i * DR for i in range(int(R_EARTH / DR) + 1)]
    rhos2 = [rho_c if r < r_c else rho_m for r in radii2]
    mass2, grav2, pres2 = integrate(radii2, rhos2)
    a = (4.0 / 3.0) * math.pi
    p_core = (2.0 / 3.0) * math.pi * G * rho_c ** 2 * r_c ** 2
    p_mant = rho_m * G * a * ((rho_c - rho_m) * r_c ** 2 * (1.0 - r_c / R_EARTH)
                              + rho_m * (R_EARTH ** 2 - r_c ** 2) / 2.0)
    p_exact2 = p_core + p_mant
    print("  (b) Two-layer planet, core radius 3480 km, rho_core 12576 kg/m3,")
    print("      rho_mantle 4138 kg/m3. Analytic P_c by integrating the two")
    print("      shells separately:")
    print(f"      numerical P_c = {pres2[-1] / 1e9:.4f} GPa")
    print(f"      exact     P_c = {p_exact2 / 1e9:.4f} GPa")
    print(f"      relative difference = "
          f"{(pres2[-1] - p_exact2) / p_exact2:.3e}")
    print()
    print("  Both checks close to the accuracy of the radial step. That is what")
    print("  licenses the numbers in sections 2 and 3: the same integration, on")
    print("  the layered model, is being done correctly.")
    print()
    print(f"  For reference, the mean density of the real Earth is "
          f"{M_EARTH / ((4.0 / 3.0) * math.pi * R_EARTH ** 3):.0f} kg/m3,")
    print("  and the uniform-sphere pressure above is a lower bound on the")
    print("  central pressure of any body of the same mass and radius.")


def main():
    radii, depths, rhos = build_profile()
    mass, grav, pres = integrate(radii, rhos)
    part1_model()
    part2_profiles(depths, rhos, grav, pres)
    part3_checks(radii, depths, rhos, mass, grav, pres)
    part4_adams_williamson(depths, rhos, grav)
    part5_s_values()
    part6_verification()


if __name__ == "__main__":
    main()
