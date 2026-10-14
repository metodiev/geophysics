#!/usr/bin/env python3
"""Reference Earth models: what a 1-D radial model is, what it predicts, and
what it leaves undetermined.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python prem_and_reference_models_demo.py

Everything here is SYNTHETIC.  The radial model below is a chosen teaching
profile that mimics the SHAPE of a reference Earth model; it is not PREM, not
IASP91 and not any published model.  The only standard values used are named
conventions quoted for scale: the Earth radius (6371 km), conventional
PREM-like interface radii (24.4, 400, 670, 2891 and 5149.5 km depth), the Earth
mass (5.9722e24 kg) and g at the CMB (10.68 m/s^2).

Contents
--------
1. The radial model: layer table and interfaces.
2. Vertical travel time through the mantle (an integral, not a measurement).
3. Validation of the ray integrals against a homogeneous sphere, where Delta
   and T have closed forms.
4. The mantle P travel-time curve and the core-grazing limit; the slowness
   check dT/dDelta = p.
5. Core phases PKP and PKIKP: the caustic, the short-distance end of the
   inner-core branch, and the shadow zone where no ray turns at all.
6. Mass and moment of inertia from the same density profile, with the uniform
   sphere result C/MR^2 = 2/5 as an exact reference.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

R_EARTH_KM = 6371.0        # standard mean Earth radius
R_CMB_KM = 3480.0          # conventional PREM-like CMB radius
R_ICB_KM = 1221.5          # conventional PREM-like ICB radius
M_EARTH_KG = 5.9722e24     # standard Earth mass (named constant, for scale)
G_CMB = 10.68              # m/s^2, conventional g at the CMB (named convention)
DEG_PER_RAD = float(np.degrees(1.0))

# SYNTHETIC layered profile: (depth_top_km, depth_bot_km, vp_top, vp_bot,
#                             vs_top, vs_bot, rho_top, rho_bot)
SYNTHETIC_LAYERS = [
    (0.0,    24.4,  5.80,  6.50,  3.20,  3.70,  2.60,  2.90),   # crust
    (24.4,  180.0,  8.10,  8.10,  4.49,  4.45,  3.38,  3.36),   # lid
    (180.0, 400.0,  8.08,  8.55,  4.42,  4.66,  3.35,  3.54),   # low-velocity zone
    (400.0, 670.0,  8.90, 10.15,  4.80,  5.55,  3.65,  3.99),   # transition zone
    (670.0, 2891.0, 10.75, 13.72, 5.85,  7.26,  4.01,  5.57),   # lower mantle
    (2891.0, 5149.5, 8.06, 10.29,  0.00,  0.00,  9.90, 12.17),  # outer core
    (5149.5, 6371.0, 11.03, 11.26, 3.50,  3.67, 12.76, 13.09),  # inner core
]

DR_KM = 1.0


def build_profile(dr=DR_KM):
    """Sample the layered model onto a fine radial grid (radius increasing)."""
    r = np.arange(0.0, R_EARTH_KM + dr, dr)
    depth = R_EARTH_KM - r
    vp = np.zeros_like(r)
    vs = np.zeros_like(r)
    rho = np.zeros_like(r)
    for d0, d1, vp0, vp1, vs0, vs1, rh0, rh1 in SYNTHETIC_LAYERS:
        m = (depth >= d0) & (depth < d1)
        f = (depth[m] - d0) / (d1 - d0)
        vp[m] = vp0 + f * (vp1 - vp0)
        vs[m] = vs0 + f * (vs1 - vs0)
        rho[m] = rh0 + f * (rh1 - rh0)
    # the outermost sample belongs to the first layer
    vp[-1], vs[-1], rho[-1] = SYNTHETIC_LAYERS[0][2], SYNTHETIC_LAYERS[0][4], \
        SYNTHETIC_LAYERS[0][6]
    # the centre sample belongs to the innermost layer
    vp[0], vs[0], rho[0] = SYNTHETIC_LAYERS[-1][3], SYNTHETIC_LAYERS[-1][5], \
        SYNTHETIC_LAYERS[-1][7]
    return r, vp, vs, rho


R_GRID, VP_GRID, VS_GRID, RHO_GRID = build_profile()
R_JUST_ABOVE_CMB = R_CMB_KM + DR_KM
# U = r/v evaluated on either side of a first-order interface, using the layer
# velocities directly: interpolating across a jump would average the two.
U_OC_TOP = R_ICB_KM / SYNTHETIC_LAYERS[5][3]   # bottom of the outer core
U_IC_TOP = R_ICB_KM / SYNTHETIC_LAYERS[6][2]   # top of the inner core


def p_velocity(r_km):
    """P velocity in km/s at radius r_km (piecewise-linear interpolation)."""
    return float(np.interp(r_km, R_GRID, VP_GRID))


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def trapezoid(y, x):
    """Trapezoid rule (np.trapz was removed in NumPy 2)."""
    return float(np.sum(0.5 * (y[1:] + y[:-1]) * np.diff(x)))


# --------------------------------------------------------------------------
# Spherical ray integrals
# --------------------------------------------------------------------------

def shell_edges(r_tp, r_top=R_EARTH_KM):
    """Radii where the velocity field changes shell: turning point, ICB, CMB."""
    pts = {float(r_tp), float(r_top)}
    for rb in (R_ICB_KM, R_CMB_KM):
        if r_tp < rb < r_top:
            pts.add(rb)
    return sorted(pts)


def ray_parameter(r_tp_km, v_km_s=None):
    """U = r/v at the turning radius, in seconds per radian.

    In a spherical Earth the conserved quantity is U = r sin(i)/v, a time per
    radian, not a slowness in s/km.  Dividing by 57.2958 converts it to s/deg,
    the unit in which dT/dDelta is measured.
    """
    v = p_velocity(r_tp_km) if v_km_s is None else v_km_s
    return r_tp_km / v


def ray_exists(p, r_tp):
    """A ray of parameter p exists only if no shell above the turning point has
    U = r/v smaller than p.  U increases upward in every shell of this model, so
    testing the bottom of each traversed shell is sufficient."""
    for bottom in shell_edges(r_tp)[:-1]:
        if bottom > 0.0 and ray_parameter(bottom) < p * (1.0 - 1e-9):
            return False
    return True


def _kernel(ra, rb, p, v_km_s=None, n=4000):
    """Integrate the (Delta, T) kernels over [ra, rb], with ra the turning radius.

    The substitution r = ra + s^2 removes the inverse-square-root singularity at
    the turning point; a midpoint rule in s then converges quickly.  If v_km_s
    is given, a constant-velocity sphere is integrated instead of the profile.
    """
    if rb <= ra:
        return 0.0, 0.0
    s_max = np.sqrt(rb - ra)
    s = (np.arange(n) + 0.5) * (s_max / n)
    ds = s_max / n
    r = ra + s ** 2
    if v_km_s is None:
        rad = np.sqrt(np.maximum((r / np.interp(r, R_GRID, VP_GRID)) ** 2 - p ** 2,
                                 1e-24))
        d_delta = float(np.sum(2.0 * p * (2.0 * s * ds) / (r * rad)))
        d_time = float(np.sum(2.0 * (r / np.interp(r, R_GRID, VP_GRID) ** 2)
                              * (2.0 * s * ds) / rad))
    else:
        rad = np.sqrt(np.maximum((r / v_km_s) ** 2 - p ** 2, 1e-24))
        d_delta = float(np.sum(2.0 * p * (2.0 * s * ds) / (r * rad)))
        d_time = float(np.sum(2.0 * (r / v_km_s ** 2) * (2.0 * s * ds) / rad))
    return d_delta, d_time


def ray_integral(p, r_tp, max_step_km=200.0):
    """(Delta_deg, T_s) for a P ray of parameter p turning at radius r_tp.

    Mantle P velocities are used outside the CMB and core P velocities inside
    it.  Returns (None, None) when no such ray exists in this model.
    """
    if not ray_exists(p, r_tp):
        return None, None
    delta = time = 0.0
    edges = shell_edges(r_tp)
    for ra, rb in zip(edges[:-1], edges[1:]):
        n_seg = max(1, int(np.ceil((rb - ra) / max_step_km)))
        cuts = np.linspace(ra, rb, n_seg + 1)
        for a, b in zip(cuts[:-1], cuts[1:]):
            dd, dt = _kernel(a, b, p)
            delta += dd
            time += dt
    return float(np.degrees(delta)), float(time)


def main():
    r, vp, vs, rho = R_GRID, VP_GRID, VS_GRID, RHO_GRID
    u_cmb = ray_parameter(R_JUST_ABOVE_CMB)      # core-grazing ray parameter

    section("1. SYNTHETIC radial model: layer table")
    print("  depth range (km)      vp (km/s)      vs (km/s)     rho (g/cm^3)")
    for d0, d1, vp0, vp1, vs0, vs1, rh0, rh1 in SYNTHETIC_LAYERS:
        print(f"  {d0:7.1f} - {d1:7.1f}   {vp0:5.2f} - {vp1:5.2f}   "
              f"{vs0:5.2f} - {vs1:5.2f}   {rh0:5.2f} - {rh1:5.2f}")
    print(f"  Earth radius R = {R_EARTH_KM:.0f} km. Conventional interface names:")
    print(f"    Moho 24.4 km, transition zone 400-670 km, CMB depth "
          f"{R_EARTH_KM - R_CMB_KM:.0f} km,")
    print(f"    ICB depth {R_EARTH_KM - R_ICB_KM:.1f} km.")

    section("2. Vertical travel time (p = 0): an integral, not a measurement")
    t_icb = trapezoid(1.0 / vp[(r >= R_ICB_KM)], r[(r >= R_ICB_KM)])
    for name, r_lo in (("surface -> CMB", R_CMB_KM), ("surface -> ICB", R_ICB_KM),
                       ("surface -> centre", 0.0)):
        m = (r >= r_lo) & (r <= R_EARTH_KM)
        t = trapezoid(1.0 / vp[m], r[m])
        print(f"  {name:16s}  T_vertical = {t:8.3f} s   "
              f"(integral of dr/vp over {R_EARTH_KM - r_lo:.1f} km)")
        print(f"  {'':16s}  effective vertical velocity = "
              f"{(R_EARTH_KM - r_lo) / t:7.4f} km/s (a harmonic mean of vp)")
    print(f"  the inner-core leg alone (centre -> ICB, {R_ICB_KM:.1f} km) takes "
          f"{trapezoid(1.0 / vp[r <= R_ICB_KM], r[r <= R_ICB_KM]):.3f} s, i.e. a")
    print(f"  mean inner-core vp of "
          f"{R_ICB_KM / trapezoid(1.0 / vp[r <= R_ICB_KM], r[r <= R_ICB_KM]):.4f}"
          " km/s")

    section("3. Validation of the ray integrals on a homogeneous sphere")
    v_const, r_tp_c = 8.00, 3000.0
    p_const = r_tp_c / v_const
    delta_num, time_num = _kernel(r_tp_c, R_EARTH_KM, p_const, v_km_s=v_const,
                                  n=400000)
    delta_ana = 2.0 * np.arccos(r_tp_c / R_EARTH_KM)
    time_ana = 2.0 * np.sqrt(R_EARTH_KM ** 2 - r_tp_c ** 2) / v_const
    print(f"  constant v = {v_const:.2f} km/s, turning radius r_tp = "
          f"{r_tp_c:.0f} km (the ray is a straight chord)")
    print(f"  analytic  : Delta = {np.degrees(delta_ana):10.6f} deg   "
          f"T = {time_ana:10.6f} s")
    print(f"  numerical : Delta = {np.degrees(delta_num):10.6f} deg   "
          f"T = {time_num:10.6f} s")
    print(f"  relative error: {abs(delta_num - delta_ana) / delta_ana:.2e} (Delta), "
          f"{abs(time_num - time_ana) / time_ana:.2e} (T)")

    section("4. Mantle P travel-time curve and the core-grazing limit")
    print("  r_tp (km)  p (s/rad)  p (s/deg)   Delta (deg)   T (s)   dT/dDelta (s/deg)")
    mantle = []
    for rtp in (6350, 6300, 6100, 5800, 5500, 5100, 4600, 4200, 3900, 3700,
                3550, R_JUST_ABOVE_CMB):
        p = ray_parameter(rtp)
        d, t = ray_integral(p, rtp)
        mantle.append((rtp, p, d, t))
    for i, (rtp, p, d, t) in enumerate(mantle):
        slope = np.nan if i == 0 else (t - mantle[i - 1][3]) / (d - mantle[i - 1][2])
        print(f"  {rtp:8.1f}  {p:8.3f}  {p / DEG_PER_RAD:8.4f}   {d:9.3f}   "
              f"{t:7.2f}   {slope:9.4f}")
    print("  slowness check: the measured dT/dDelta must equal the mean of the two")
    print("  endpoint ray parameters (p is averaged over the finite interval):")
    for i in (5, 8, 10):
        _, p_i, d_i, t_i = mantle[i]
        _, p_j, d_j, t_j = mantle[i - 1]
        slope = (t_i - t_j) / (d_i - d_j)
        mean_p = 0.5 * (p_i + p_j) / DEG_PER_RAD
        print(f"    Delta = {d_j:6.2f} -> {d_i:6.2f} deg: measured {slope:7.4f} s/deg,"
              f" mean p = {mean_p:7.4f} s/deg, error {100 * (slope - mean_p) / mean_p:+.2f}%")
    print(f"  the branch ends at the core-grazing ray, U(CMB) = {u_cmb:.3f} s/rad "
          f"({u_cmb / DEG_PER_RAD:.4f} s/deg),")
    print(f"  at Delta = {mantle[-1][2]:.2f} deg; beyond that no mantle P ray turns.")

    section("5. Core phases: PKP and PKIKP, and the fold of the curve")
    print("  outer-core turning points (PKP):")
    print("  r_tp (km)  p (s/rad)   Delta (deg)   T (s)")
    oc = []
    for rtp in np.linspace(2100.0, R_ICB_KM + 0.5, 12):
        p = ray_parameter(rtp)
        d, t = ray_integral(p, rtp)
        oc.append((rtp, p, d, t))
        print(f"  {rtp:8.1f}  {p:8.3f}   {d:9.3f}   {t:8.2f}")
    print("  inner-core turning points (PKIKP):")
    print("  r_tp (km)  p (s/rad)   Delta (deg)   T (s)")
    ic = []
    for rtp in np.linspace(R_ICB_KM - 0.5, 80.0, 12):
        p = ray_parameter(rtp)
        if p >= U_IC_TOP:
            print(f"  {rtp:8.1f}  {p:8.3f}   no turning point in the inner core")
            continue
        d, t = ray_integral(p, rtp)
        ic.append((rtp, p, d, t))
        print(f"  {rtp:8.1f}  {p:8.3f}   {d:9.3f}   {t:8.2f}")
    d_caustic = min(row[2] for row in oc)
    r_caustic = [row[0] for row in oc if row[2] == d_caustic][0]
    d_ic_short = min(row[2] for row in ic)
    print(f"  outer-core branch caustic: Delta = {d_caustic:.2f} deg at r_tp = "
          f"{r_caustic:.0f} km (the branch folds there)")
    print(f"  inner-core branch reaches inward to Delta = {d_ic_short:.2f} deg "
          f"at r_tp = {[row[0] for row in ic if row[2] == d_ic_short][0]:.0f} km")
    print(f"  rays with p between U just above the ICB in the outer core "
          f"({U_OC_TOP:.2f} s/rad) and")
    print(f"  U at the bottom of the mantle ({u_cmb:.2f} s/rad) have no turning point")
    print(f"  anywhere: their epicentral distances fill the gap from "
          f"{mantle[-1][2]:.1f} to {d_ic_short:.1f} deg.")
    print("  This SYNTHETIC shadow gap is a property of the chosen core radius and")
    print("  gradients; the classic observed limits for the real Earth are ~103 and")
    print("  ~143 deg, and the model reproduces the mechanism, not the numbers.")
    d0, t0 = ray_integral(0.0, R_ICB_KM)
    print(f"  a vertical ray reflected at the ICB (down and up, p = 0) takes "
          f"{t0:.3f} s = 2 x {t_icb:.3f} s,")
    print(f"  and its horizontal offset is Delta = {d0:.1f} deg: a p = 0 ray is "
          "radial.")

    section("6. Mass and moment of inertia from the same density profile")
    r_m = r * 1e3
    rho_si = rho * 1e3
    dr_m = DR_KM * 1e3
    mass = float(np.sum(rho_si * 4.0 * np.pi * r_m ** 2 * dr_m))
    inert = float(np.sum(rho_si * (8.0 / 3.0) * np.pi * r_m ** 4 * dr_m))
    print(f"  model mass   M = {mass:.4e} kg   (standard Earth mass "
          f"{M_EARTH_KG:.4e} kg; ratio {mass / M_EARTH_KG:.4f})")
    print(f"  model moment C = {inert:.4e} kg m^2")
    print(f"  model C/MR^2   = {inert / (mass * (R_EARTH_KM * 1e3) ** 2):.4f}")
    print("  exact reference: a uniform sphere gives C/MR^2 = 2/5 = 0.4 exactly,")
    print("  so any radial density increase pushes a model below 0.4. The value")
    print("  conventionally adopted for the Earth is 0.3307, and this chosen profile")
    print("  lands close to it because it was built to mimic that shape.")
    print(f"  g at the CMB, quoted as a named convention: {G_CMB:.2f} m/s^2")

    print("\n  A two-layer model, solved in closed form (uniform core + uniform mantle):")
    rho_core, rho_mantle = 10.50, 4.90   # g/cm^3, chosen values
    q = R_CMB_KM / R_EARTH_KM
    b = lambda x: rho_core * x ** 5 + rho_mantle * (1 - x ** 5)
    a_ = lambda x: rho_core * x ** 3 + rho_mantle * (1 - x ** 3)
    ratio = lambda x: 0.4 * b(x) / a_(x)
    print(f"    core fraction q = a/R = 3480/6371 = {q:.4f}, "
          f"rho_core = {rho_core:.2f}, rho_mantle = {rho_mantle:.2f} g/cm^3")
    print(f"    C/MR^2 = (2/5) [rho_c q^5 + rho_m (1-q^5)] / [rho_c q^3 + rho_m (1-q^3)]")
    print(f"           = {ratio(q):.4f}   (a uniform sphere would give 0.4000)")
    qs = np.linspace(1e-6, 1.0 - 1e-6, 2000001)
    vals = ratio(qs)
    i_best = int(np.argmin(vals))
    print(f"    no value of q reproduces 0.3307 with these two densities: the smallest")
    print(f"    ratio any two-layer model can reach is {vals[i_best]:.4f} at "
          f"q = {qs[i_best]:.4f}")
    print(f"    (core radius {qs[i_best] * R_EARTH_KM:.0f} km). A density increase "
          f"within the")
    print(f"    core, or a denser deep mantle, is therefore required by C/MR^2 -- this")
    print(f"    is a genuine, if weak, constraint on the interior from geodesy.")

    section("7. What this model does NOT constrain")
    print("  * the ray integrals assume a spherically symmetric, isotropic, purely")
    print("    elastic Earth: no anisotropy, no attenuation and no 3-D structure;")
    print("  * velocities and densities are independent inputs here, so the mass and")
    print("    moment of inertia above are not predictions of the travel times;")
    print("  * the layer table is a set of chosen numbers, and any other profile that")
    print("    preserves the same slowness integrals would fit the same travel times.")


if __name__ == "__main__":
    main()
