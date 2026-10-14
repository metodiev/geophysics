"""The layered Earth: mass, gravity, pressure and the seismic shadow zones.

Run:  .venv/bin/python layered_earth_demo.py
Requires: numpy (and the standard library).

Companion to lesson 04-01-01, "Crust, Mantle, Core: Seismological and
Geochemical Evidence".

This script does not look up the Earth's mass, its moment of inertia, the
pressures at the internal discontinuities, or the position of the seismic
shadow zones. It *computes* all of them from a layered density and velocity
model, and compares the results with the tabulated observations. That is the
whole point of the lesson: the interior is not observed directly, it is
inferred from a model, and the model is testable because it has to reproduce
several independent observables at once.

The model is a seven-layer, explicitly nominal discretisation built from the
rounded characteristic values of the Preliminary Reference Earth Model (PREM)
collected in 26-02-03 Physical Constants and Earth Parameters with Sources,
section 3.3. It is NOT PREM. PREM has hundreds of layers, tabulated values at
each depth and a full equation-of-state treatment; this model has seven layers
and piecewise-linear interpolation. Every number derived from it is therefore a
check on the order of magnitude and on the qualitative behaviour, not a
reference value. That is why the script prints the tabulated comparison values
separately and labels them TABULATED.

The script computes:

1. The mass, the surface gravity, the gravity at the core-mantle boundary and
   the moment-of-inertia factor I/(M R^2), by direct numerical integration.
2. The hydrostatic pressure profile and the pressures at the core-mantle
   boundary and the inner-core boundary.
3. The epicentral distance of the S-wave shadow boundary, from ray theory in
   the spherical model: the ray that grazes the core-mantle boundary. It then
   runs the counterfactual in which the outer core is given a finite shear
   velocity, and shows that the shadow would be filled. That counterfactual is
   the actual seismological evidence for a liquid outer core.
4. The angular extent of the P-wave shadow zone from the same ray theory: one
   ray parameter sets both edges, and the gap between them opens only because
   the velocity drops at the core-mantle boundary.
"""

from __future__ import annotations

import math

import numpy as np

G_CONST = 6.67430e-11          # m^3 kg^-1 s^-2, CODATA 2018 (tabulated)
R_EARTH_KM = 6371.0            # km, mean radius (nominal)
R_CMB_KM = 3480.0              # km, core-mantle boundary
R_ICB_KM = 1218.0              # km, inner-core boundary
R_MOHO_KM = 6347.0             # km, base of the model crust (top of the mantle)

# --------------------------------------------------------------------------
# The layered model: (name, r_top, r_bot, rho_top, rho_bot, vp_top, vp_bot,
# vs_top, vs_bot).  Radii in km, densities in kg/m^3, velocities in km/s.
# The values at each end are the rounded characteristic PREM values of
# 26-02-03 section 3.3; the interpolation between them is linear in radius.
# This is a caricature of PREM, not PREM.
# --------------------------------------------------------------------------
LAYERS = [
    ("water (global mean)",  6371.0, 6368.0,  1020.0,  1020.0,  1.50,  1.50, 0.00, 0.00),
    ("crust",                6368.0, 6347.0,  2850.0,  2850.0,  6.40,  6.40, 3.60, 3.60),
    ("lithospheric mantle",  6347.0, 5961.0,  3300.0,  3600.0,  8.10,  9.10, 4.50, 5.00),
    ("transition zone",      5961.0, 5711.0,  3600.0,  4400.0,  9.10, 10.30, 5.00, 5.60),
    ("lower mantle",         5711.0, 3480.0,  4400.0,  5570.0, 10.30, 13.70, 5.60, 7.30),
    ("outer core",           3480.0, 1218.0,  9900.0, 12200.0,  8.00, 10.30, 0.00, 0.00),
    ("inner core",           1218.0,    0.0, 12800.0, 13100.0, 11.00, 11.30, 3.50, 3.70),
]

TABULATED = {
    "mass_kg": 5.9722e24,          # nominal Earth mass
    "g_surface": 9.80665,          # m/s^2, standard gravity (a defined value)
    "I_over_MR2": 0.3307,          # observed/geodetic value
    "p_cmb_gpa": 136.0,            # rounded characteristic PREM value
    "p_icb_gpa": 329.0,            # rounded characteristic PREM value
    "s_shadow_deg": 103.0,         # classic textbook shadow-zone entry
    "p_shadow_outer_deg": 143.0,   # classic textbook shadow-zone exit
}

# Indices into a LAYERS row.
RHO_T, RHO_B, VP_T, VP_B, VS_T, VS_B = 3, 4, 5, 6, 7, 8


def _sample(top_val, bot_val, r, r_top, r_bot):
    """Linear interpolation of one property inside one layer."""
    if r_top == r_bot:
        return top_val
    f = (r - r_bot) / (r_top - r_bot)
    return bot_val + f * (top_val - bot_val)


def property_at(r_km, top_idx, bot_idx, above_wins=True):
    """Value of a property at a radius, from the layer that contains it.

    At a radius shared by two layers the convention is set by ``above_wins``:
    True returns the value from the layer above the boundary (the shallow
    medium), False returns the value from below it (the medium a down-going
    ray enters).
    """
    ordered = LAYERS if above_wins else list(reversed(LAYERS))
    for name, r_top, r_bot, *vals in ordered:
        if r_bot - 1e-12 <= r_km <= r_top + 1e-12:
            return _sample(vals[top_idx - 3], vals[bot_idx - 3], r_km, r_top, r_bot)
    return LAYERS[0][top_idx] if r_km > LAYERS[0][1] else LAYERS[-1][bot_idx]


def profile_grid(n=400_001):
    """Fine radial grid with density and velocities (deeper layer wins)."""
    r = np.linspace(0.0, R_EARTH_KM, n)
    rho = np.zeros_like(r)
    vp = np.zeros_like(r)
    vs = np.zeros_like(r)
    for name, r_top, r_bot, *vals in LAYERS:
        m = (r >= r_bot) & (r <= r_top)
        rr = r[m]
        rho[m] = _sample(vals[0], vals[1], rr, r_top, r_bot)
        vp[m] = _sample(vals[2], vals[3], rr, r_top, r_bot)
        vs[m] = _sample(vals[4], vals[5], rr, r_top, r_bot)
    return r, rho, vp, vs


_IDX = {"vp": (VP_T, VP_B), "vs": (VS_T, VS_B)}


def mantle_only(r_km, prop):
    """Velocity restricted to the mantle side of the CMB.

    Below the CMB the value is held at the bottom-of-mantle value, so that a
    finite-difference slope taken at the boundary stays on the mantle side.
    """
    top_idx, bot_idx = _IDX[prop]
    r_clamped = min(max(r_km, R_CMB_KM), R_MOHO_KM - 1e-3)
    return property_at(r_clamped, top_idx, bot_idx, above_wins=True)


def full_model(r_km, prop):
    """Velocity with the deeper layer winning at every boundary.

    Outside the mantle the radius is clamped to the model shell, so that the
    ray integral runs from the top of the mantle to the surface of the model
    rather than through the water and crust layers.
    """
    top_idx, bot_idx = _IDX[prop]
    r_clamped = min(max(r_km, R_ICB_KM), R_MOHO_KM)
    return property_at(r_clamped, top_idx, bot_idx, above_wins=False)


def slope(fun, r_km, h=0.25):
    """Central-difference slope, in the units of fun per km."""
    return (fun(r_km + h) - fun(r_km - h)) / (2.0 * h)


def section(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


# --------------------------------------------------------------------------
# Spherical ray theory.  For a spherically symmetric profile v(r), Snell's law
# along a ray gives the ray parameter p = r sin(theta) / v(r), constant along
# the ray, with theta the angle between the ray and the radial direction. Then
#     Delta = 2 int p / ( r sqrt(r^2/v^2 - p^2) ) dr     [radians]
#         T = 2 int r / ( v^2 sqrt(r^2/v^2 - p^2) ) dr   [seconds]
# integrated from the turning point r_min (where r/v = p) to the surface.
# --------------------------------------------------------------------------

def delta_and_time(p, vfun, r_min_km, r_surface_km=R_EARTH_KM, n=400_001):
    """Epicentral distance in degrees and travel time in seconds.

    ``p`` is in seconds, ``vfun(r_km)`` returns km/s.  The substitution
    r = r_min + (R - r_min) s^2 removes the integrable square-root singularity
    at the turning point; the first integrand value is replaced by its
    analytic limit.
    """
    km = 1e3
    span = r_surface_km - r_min_km
    s = np.linspace(0.0, 1.0, n)
    r = r_min_km + span * s**2
    v = np.array([vfun(float(rr)) for rr in r])
    r_ms = r * km
    v_ms = v * km
    eta2 = np.maximum((r_ms / v_ms) ** 2 - p**2, 0.0)
    eta2[0] = 0.0

    dr_ds = 2.0 * span * s * km
    with np.errstate(divide="ignore", invalid="ignore"):
        g_delta = p / (r_ms * np.sqrt(np.maximum(eta2, 1e-300))) * dr_ds
        g_time = r_ms / (v_ms**2 * np.sqrt(np.maximum(eta2, 1e-300))) * dr_ds

    # Analytic limit of each integrand times dr/ds at s = 0, where
    # r^2/v^2 - p^2 ~ k (r - r_min) with k = 2r/v^2 - 2 r^2 v'/v^3.
    v0 = vfun(r_min_km) * km
    dv = slope(lambda x: vfun(x) * km, r_min_km) / km      # (m/s) per m
    k_slope = 2.0 * r_ms[0] / v0**2 - 2.0 * r_ms[0] ** 2 * dv / v0**3
    if k_slope > 0.0 and span > 0.0:
        root_span = math.sqrt(span * km)
        g_delta[0] = 2.0 * p * root_span / (r_ms[0] * math.sqrt(k_slope))
        g_time[0] = 2.0 * r_ms[0] * root_span / (v0**2 * math.sqrt(k_slope))
    else:
        g_delta[0] = 0.0
        g_time[0] = 0.0

    delta = 2.0 * np.trapezoid(g_delta, s)
    time = 2.0 * np.trapezoid(g_time, s)
    return math.degrees(delta), time


def find_turning(p, vfun, r_top_km, r_bot_km):
    """Radius where r/v(r) = p, by bisection inside one radial interval."""
    f_top = r_top_km / vfun(r_top_km)
    f_bot = r_bot_km / vfun(r_bot_km)
    if p > f_top:
        return None
    if p < f_bot:
        return r_bot_km
    lo, hi = r_bot_km, r_top_km        # lo: r/v < p,  hi: r/v > p
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if mid / vfun(mid) > p:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def part1_mass_gravity_moi():
    section("1. Mass, gravity and the moment of inertia")
    r, rho, _, _ = profile_grid()
    r_m = r * 1e3

    dm = 4.0 * math.pi * rho * r_m**2 * np.gradient(r_m)
    m_enclosed = np.cumsum(dm)
    mass = float(m_enclosed[-1])

    with np.errstate(divide="ignore", invalid="ignore"):
        g = np.where(r_m > 0, G_CONST * m_enclosed / np.maximum(r_m, 1.0) ** 2, 0.0)

    i_moment = (8.0 * math.pi / 3.0) * float(np.trapezoid(rho * r_m**4, r_m))
    moif = i_moment / (mass * r_m[-1] ** 2)

    print(f"  model mass                        = {mass:.4e} kg")
    print(f"  TABULATED Earth mass              = {TABULATED['mass_kg']:.4e} kg")
    print(f"  relative difference               = "
          f"{100 * (mass - TABULATED['mass_kg']) / TABULATED['mass_kg']:+.1f} %")
    print()
    print(f"  model surface gravity g(R)        = {g[-1]:.4f} m/s^2")
    print(f"  TABULATED standard gravity        = {TABULATED['g_surface']:.5f} m/s^2")
    print(f"  relative difference               = "
          f"{100 * (g[-1] - TABULATED['g_surface']) / TABULATED['g_surface']:+.1f} %")
    print()
    print(f"  model moment-of-inertia factor    = {moif:.4f}")
    print(f"  TABULATED I/(M R^2)               = {TABULATED['I_over_MR2']:.4f}")
    print()
    print("  Why the moment-of-inertia factor is the sharp test. A model can be")
    print("  tuned to match the mass and the surface gravity while putting the")
    print("  density in the wrong place. I/(M R^2) is the mass-weighted mean of")
    print("  (r/R)^2, so it measures *where* the mass sits. A uniform sphere")
    print("  gives 2/5 = 0.4000; the model and the observation agree near")
    print(f"  {moif:.3f}, well below 0.4, which is the quantitative statement")
    print("  that the Earth is strongly concentrated toward its centre. Mass and")
    print("  g are each one number; I/(M R^2) is a third, independent number, and")
    print("  it is the agreement of all three that makes the layered model")
    print("  credible rather than merely fitted.")
    print()
    j = int(np.argmin(np.abs(r - R_CMB_KM)))
    print(f"  gravity at the core-mantle boundary (r = 3480 km) = {g[j]:.3f} m/s^2")
    print("  It is larger than the surface value. g peaks at the CMB because")
    print("  the dense core below pulls outwards, while the light mantle above")
    print("  contributes little inward attraction at that radius. A homogeneous")
    print("  body would instead show g falling linearly from the surface to 0.")
    print()
    print("  Where the model is deliberately coarse: it uses one 24 km 'average'")
    print("  crust for the whole planet. The real crust is about 7 km of basalt")
    print("  beneath the oceans and 35-40 km of granitic rock beneath the")
    print("  continents, so the model's crustal mass is wrong in detail and its")
    print("  surface gravity carries that error. Closing the gap is an exercise.")
    print()


def part2_pressure():
    section("2. Hydrostatic pressure to the centre")
    r, rho, _, _ = profile_grid()
    r_m = r * 1e3
    dr = np.gradient(r_m)

    m_enclosed = np.cumsum(4.0 * math.pi * rho * r_m**2 * dr)
    with np.errstate(divide="ignore", invalid="ignore"):
        g = np.where(r_m > 0, G_CONST * m_enclosed / np.maximum(r_m, 1.0) ** 2, 0.0)
    pressure = np.cumsum(-rho * g * dr)
    pressure -= pressure[-1]                      # reference the surface to zero

    def p_at(radius_km):
        return float(np.interp(radius_km, r, pressure))

    for radius, name, tab in ((R_CMB_KM, "core-mantle boundary", TABULATED["p_cmb_gpa"]),
                              (R_ICB_KM, "inner-core boundary", TABULATED["p_icb_gpa"])):
        p_gpa = p_at(radius) / 1e9
        print(f"  {name:<22} model {p_gpa:7.1f} GPa   "
              f"TABULATED {tab:6.1f} GPa   "
              f"({100 * (p_gpa - tab) / tab:+.1f} %)")
    print(f"  {'centre':<22} model {p_at(0.0) / 1e9:7.1f} GPa")
    print()
    print("  The pressure gradient is roughly 0.3 GPa per 10 km in the crust and")
    print("  about 4.5 GPa per 10 km at the base of the mantle, because the")
    print("  overburden is both thicker and denser with depth. That steep")
    print("  gradient is why an equation of state is needed to say which")
    print("  minerals are stable at a given depth, and why the same rock is a")
    print("  different rock at 30 km and at 3000 km.")
    print()
    print("  Pressure carries the *entire* weight of the column above it, so it")
    print("  is sensitive to the same crustal simplification as the mass: the")
    print("  model is off at every depth by the error accumulated above. That is")
    print("  why the comparison with PREM is a check on the whole column, not on")
    print("  one layer.")
    print()


def mantle_family(prop, alpha):
    """A one-parameter family of mantle velocity profiles.

    v(r) = v_bot + (v_top - v_bot) * ((r - r_bot)/(r_top - r_bot))^alpha,
    with v_top and v_bot the model values at the top of the mantle and at the
    core-mantle boundary.  alpha = 1 is a linear profile.  Large alpha keeps
    the velocity near its CMB value through the deep mantle and puts the
    gradient high up; small alpha does the opposite.  The family is a device
    for testing how sensitive the shadow boundary is to the shape of the
    gradient, which is the only thing about it the boundary can measure.
    """
    top_idx, bot_idx = _IDX[prop]
    v_bot = property_at(R_CMB_KM, top_idx, bot_idx, above_wins=True)
    v_top = property_at(R_MOHO_KM - 1e-3, top_idx, bot_idx, above_wins=True)

    def vfun(r_km):
        rc = min(max(r_km, R_CMB_KM), R_MOHO_KM)
        u = (rc - R_CMB_KM) / (R_MOHO_KM - R_CMB_KM)
        return v_bot + (v_top - v_bot) * u**alpha

    return vfun


def grazing_distance(prop, vfun):
    """Epicentral distance (deg) of the ray that grazes the CMB, with a time."""
    v_bot = vfun(R_CMB_KM)
    p = R_CMB_KM / v_bot
    return p, v_bot, delta_and_time(p, vfun, R_CMB_KM, r_surface_km=R_MOHO_KM)


def part3_shadow_zones():
    section("3. The shadow zones, computed from ray theory")

    vp_bot = mantle_only(R_CMB_KM, "vp")
    vs_bot = mantle_only(R_CMB_KM, "vs")

    print("  MODEL velocities at the base of the mantle:")
    print(f"    v_P = {vp_bot:.2f} km/s      v_S = {vs_bot:.2f} km/s")
    print("    (the outer core is assigned v_S = 0 exactly)")
    print()

    # ---- S waves: the deepest possible mantle ray grazes the CMB.
    v_s_mantle = lambda x: mantle_only(x, "vs")
    p_s, v_s_bot, (delta_s, time_s) = grazing_distance("vs", v_s_mantle)
    print("  S waves.  The mantle ray that just grazes the core-mantle boundary:")
    print(f"    ray parameter   p = r_CMB / v_S = 3480 / {v_s_bot:.2f} "
          f"= {p_s:.2f} s")
    print(f"    turning radius  3480.0 km  (the CMB itself)")
    print(f"    distance        Delta = {delta_s:.1f} deg")
    print(f"    travel time     T     = {time_s / 60.0:.2f} min")
    print(f"    TABULATED S-shadow entry = ~{TABULATED['s_shadow_deg']:.0f} deg")
    print("  Beyond that distance no direct S arrives: there is no S velocity")
    print("  below the boundary for the ray to turn in. The shadow is not a")
    print("  statement that the core is slow -- it is a statement that the core")
    print("  cannot carry a shear wave at all.")
    print()

    # The P grazing ray is needed for the table below and reused later.
    v_p_mantle = lambda x: mantle_only(x, "vp")
    p_p, v_p_bot, (delta_p_near, time_p_near) = grazing_distance("vp", v_p_mantle)

    # ---- Sensitivity: how much does the boundary depend on the gradient?
    print("  The computed boundary is not a property of the ray parameter alone;")
    print("  it depends on the *shape* of the velocity gradient, because that is")
    print("  what bends the ray back to the surface.  Sweep the one-parameter")
    print("  family of the model (see mantle_family) for the S grazing ray:")
    print()
    print(f"    {'alpha':>8}{'v_top (km/s)':>15}{'Delta_S (deg)':>16}"
          f"{'Delta_P (deg)':>16}")
    print(f"    {'LAYERS':>8}{v_s_mantle(R_MOHO_KM - 1e-3):>15.2f}"
          f"{delta_s:>16.1f}{delta_p_near:>16.1f}   <- nominal model")
    best = None
    for alpha in (0.5, 1.0, 2.0, 4.0, 8.0):
        _, _, (d_s, _) = grazing_distance("vs", mantle_family("vs", alpha))
        _, _, (d_p, _) = grazing_distance("vp", mantle_family("vp", alpha))
        v_top = mantle_family("vs", alpha)(R_MOHO_KM - 1e-3)
        print(f"    {alpha:>8.2f}{v_top:>15.2f}{d_s:>16.1f}{d_p:>16.1f}")
        if best is None or abs(d_s - TABULATED["s_shadow_deg"]) < best[1]:
            best = (alpha, abs(d_s - TABULATED["s_shadow_deg"]), d_s)
    print()
    print(f"  The observation, ~{TABULATED['s_shadow_deg']:.0f} deg, lies inside")
    print("  this family: the row nearest to it is alpha = "
          f"{best[0]:.2f}, giving {best[2]:.1f} deg.")
    print("  Read the table in the other direction and it says something")
    print("  stronger.  Because Delta_S varies strongly and monotonically with")
    print("  the gradient, the *measured* shadow boundary is itself a")
    print("  measurement of the mantle velocity gradient -- one of the")
    print("  constraints that the reference models are built to satisfy.")
    print()

    # ---- The counterfactual: give the outer core a finite shear velocity.
    core_vs = 4.0
    sin_core = p_s * core_vs / R_CMB_KM
    print("  Counterfactual test.  Give the outer core v_S = "
          f"{core_vs:.1f} km/s and re-ask.")
    print(f"    At the CMB, sin(theta_core) = p v_S(core) / r_CMB = "
          f"{sin_core:.3f} < 1,")
    print("    so the grazing ray would refract into the core and turn there,")
    print(f"    at r = p v_S = {p_s * core_vs:.0f} km.  S arrivals would then")
    print("    appear inside the 'shadow'.  They are not observed.  That")
    print("    absence is the seismological evidence for a liquid outer core:")
    print("    v_S = 0 -- a zero shear modulus, not merely a small one.")
    print()

    # ---- P waves: the shadow gap opens on a velocity *decrease*.
    v_p_full = lambda x: full_model(x, "vp")
    r_turn_p = find_turning(p_p, v_p_full, R_CMB_KM, R_ICB_KM)
    delta_p_far, time_p_far = delta_and_time(p_p, v_p_full, r_turn_p,
                                             r_surface_km=R_MOHO_KM)

    print("  P waves.  The same ray parameter, p = r_CMB / v_P(bottom of mantle)")
    print(f"    = {p_p:.2f} s, gives two distances for the nominal model:")
    print(f"      mantle ray grazing the CMB   Delta = {delta_p_near:6.1f} deg,"
          f"  T = {time_p_near / 60.0:.2f} min")
    print(f"      same ray transmitted into the core, turning at r = "
          f"{r_turn_p:.0f} km")
    print(f"                                   Delta = {delta_p_far:6.1f} deg,"
          f"  T = {time_p_far / 60.0:.2f} min")
    print(f"    TABULATED P-shadow zone = ~{103.0:.0f} to "
          f"~{TABULATED['p_shadow_outer_deg']:.0f} deg")
    print()
    print("  Between those two distances there is no direct P arrival at all.")
    print("  The gap opens because the P velocity *drops* at the CMB, from")
    print(f"  {v_p_bot:.1f} to {full_model(R_CMB_KM, 'vp'):.1f} km/s: a ray that can just reach the")
    print("  boundary is bent steeply downward into the core and must travel")
    print("  much further before it turns.  Had the velocity increased instead,")
    print("  the ray would be reflected at the boundary rather than transmitted")
    print("  and there would be no gap at all -- see the counterfactual below.")
    print("  The shadow zone is therefore a measurement of the *sign* of the")
    print("  velocity jump at the boundary, and its two edges constrain the")
    print("  velocities on either side.")
    print()
    # Flip the sign of the jump and watch the gap close.
    v_core_high = 16.0
    sin_high = p_p * v_core_high / R_CMB_KM
    print("  Counterfactual test.  Now suppose the velocity *increased* at the")
    print(f"  CMB, to {v_core_high:.1f} km/s.  Then for the same ray")
    print(f"    sin(theta_core) = p v_core / r_CMB = {sin_high:.3f} > 1,")
    print("  which has no solution: the ray cannot enter the core at all and is")
    print("  reflected back into the mantle.  There is then no core branch and")
    print("  no gap, so direct P would be observed continuously across the")
    print("  whole distance range.  It is not.  The existence of the shadow is")
    print("  a measurement of the *sign* of the jump, and it is a decrease.")
    print()
    print("  Model versus observation.  The nominal seven-layer model gets the")
    print("  *mechanism* exactly right and the numbers to within the width of")
    print("  the alpha sweep: the coarse model's lower-mantle gradient is")
    print("  linear, whereas the real Earth's is weak through the mid-mantle")
    print("  and steep in the lowermost 200 km.  Both computed boundaries move")
    print("  by more than ten degrees across the sweep, which is the honest")
    print("  statement: a shadow boundary constrains structure, but only as")
    print("  tightly as the rest of the model is known.  Refining the profile")
    print("  until Delta_S lands on the observed value is an exercise.")
    print()


def main():
    print("The layered Earth: mass, gravity, pressure and the seismic shadow zones.")
    part1_mass_gravity_moi()
    part2_pressure()
    part3_shadow_zones()
    print("=" * 74)
    print("Every quantity above is computed from LAYERS except the rows labelled")
    print("TABULATED, which are the independent observations the model is tested")
    print("against. The model is a rounded, seven-layer caricature of PREM, not")
    print("PREM, and the residuals are reported rather than hidden.")
    print("=" * 74)


if __name__ == "__main__":
    main()
