#!/usr/bin/env python3
"""Engineering seismics: refraction survey design, depth error, downhole Vs,
elastic moduli, site/building periods and the strain question.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python engineering_seismics_demo.py

Everything is SYNTHETIC.  The site profile, the borehole geometry, the picking
errors, the structural mass and stiffness and the modulus-reduction curve are
chosen teaching values, not measurements.  No real site, borehole, structure or
code value is used.

Contents
--------
1. Refraction spread design: crossover distance against velocity contrast, and
   the deepest target a given spread can reach.
2. Depth uncertainty of a two-layer interpretation from the picking error,
   checked by Monte Carlo against the least-squares covariance.
3. Downhole interval velocities, their errors, and Vs30 from the same profile.
4. Elastic moduli from Vp, Vs and density, and the sensitivity of Poisson's
   ratio to an error in Vs.
5. Site period against the period of a synthetic single-degree-of-freedom
   structure.
6. Strain level: why the small-strain velocity may not be the operative
   modulus, and how much the answer moves when it is not.
7. Uncertainty budget of Vs30: velocity error against thickness error.
8. The quarter-wavelength limit on what a survey can resolve.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC site: (thickness m, Vp m/s, Vs m/s, density kg/m^3) -----------
# Four layers, the last of which is the bedrock half-space for the Vs column.
SITE = (
    (4.0, 400.0, 150.0, 1800.0),     # fill / weathered rock
    (6.0, 1500.0, 250.0, 1900.0),    # soft clay
    (8.0, 1900.0, 450.0, 2000.0),    # dense sand and gravel
    (12.0, 3500.0, 1800.0, 2500.0),  # bedrock
)
DEPTH_REF_M = 30.0
SIGMA_TWO_WAY = 1.0e-3       # s, one-way picking error used in the design study
SPREAD_MULTIPLE = 3.0        # spread = 3 x crossover: a design convention
N_PICKS = 40                 # far-branch picks used by the depth fit


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def travel_time_average(layers, index):
    """Depth / travel time for one velocity column of the profile, in m/s."""
    thickness = sum(layer[0] for layer in layers)
    total = sum(layer[0] / layer[index] for layer in layers)
    return thickness, total, thickness / total


def crossover_two_layer(h_m, v1, v2):
    """Crossover distance of a two-layer model: 2h sqrt((v2+v1)/(v2-v1)), m."""
    return 2.0 * h_m * np.sqrt((v2 + v1) / (v2 - v1))


def intercept_two_layer(h_m, v1, v2):
    """Intercept time 2h sqrt(v2^2-v1^2)/(v1 v2), s."""
    return 2.0 * h_m * np.sqrt(v2 ** 2 - v1 ** 2) / (v1 * v2)


def depth_from_intercept(t_i, v1, v2):
    """h = t_i v1 v2 / (2 sqrt(v2^2 - v1^2)), m."""
    return t_i * v1 * v2 / (2.0 * np.sqrt(v2 ** 2 - v1 ** 2))


def main():
    print("06-10-06 engineering seismics -- SYNTHETIC site, no field data")

    h_soil = sum(layer[0] for layer in SITE[:3])
    v1_p_eff = travel_time_average(SITE[:3], 1)[2]
    v2_p = SITE[3][1]
    h_vs_eff = travel_time_average(SITE, 2)[2]
    h30, t30, vs30 = travel_time_average(SITE, 2)

    section("1. Refraction spread design against the velocity contrast")
    print(f"  SYNTHETIC site: {h_soil:.0f} m of overburden over bedrock")
    print(f"  travel-time-average P velocity of the overburden = {v1_p_eff:.1f} m/s")
    print(f"  P velocity of the bedrock                        = {v2_p:.1f} m/s")
    print(f"  contrast ratio v2/v1 = {v2_p / v1_p_eff:.3f}")
    print(f"  depth-to-target design example, h = {h_soil:.0f} m:")
    print("    contrast v2/v1   x_crossover (m)   spread = 3 x_c (m)")
    x_c_site = None
    for ratio in (1.2, 1.5, 2.0, v2_p / v1_p_eff, 5.0):
        v2 = v1_p_eff * ratio
        x_c = crossover_two_layer(h_soil, v1_p_eff, v2)
        if abs(ratio - v2_p / v1_p_eff) < 1e-9:
            x_c_site = x_c
        print(f"    {ratio:11.3f}   {x_c:15.2f}   {SPREAD_MULTIPLE * x_c:15.2f}")
    print(f"  the site's own crossover is {x_c_site:.2f} m; "
          f"{SPREAD_MULTIPLE * x_c_site:.1f} m of spread")
    print("  the same target at the same depth needs a spread 2.5 times longer")
    print("  when the contrast is 1.2 instead of 3.5: a weak contrast, not a")
    print("  thick layer, is what makes a refraction survey expensive.")
    print("  deepest target reachable when the crossover sits at L/3:")
    print("    spread L (m)   h_max for this site (m)")
    ratio_site = v2_p / v1_p_eff
    for spread in (50.0, 100.0, 200.0, 400.0):
        h_max = (spread / SPREAD_MULTIPLE) / (
            2.0 * np.sqrt((ratio_site + 1.0) / (ratio_site - 1.0)))
        print(f"    {spread:12.0f}   {h_max:23.2f}")

    section("2. What a 1 ms picking error does to the depth")
    v1, v2 = v1_p_eff, v2_p
    t_i = intercept_two_layer(h_soil, v1, v2)
    h_hat = depth_from_intercept(t_i, v1, v2)
    dh_dti = v1 * v2 / (2.0 * np.sqrt(v2 ** 2 - v1 ** 2))
    print(f"  two-layer fit of the site's bedrock refractor: h = {h_soil:.1f} m")
    print(f"  intercept time t_i = {t_i * 1e3:.3f} ms, "
          f"h from the closed form = {h_hat:.6f} m (round trip)")
    print(f"  sensitivity dh/dt_i = v1 v2 / (2 sqrt(v2^2 - v1^2)) = "
          f"{dh_dti:.3f} m/s")
    x = np.linspace(x_c_site, SPREAD_MULTIPLE * x_c_site, N_PICKS)
    x_bar = x.mean()
    s_xx = np.sum((x - x_bar) ** 2)
    sigma_ti = SIGMA_TWO_WAY * np.sqrt(1.0 / N_PICKS + x_bar ** 2 / s_xx)
    print(f"  {N_PICKS} picks over {x[0]:.1f}-{x[-1]:.1f} m, "
          f"sigma_t = {SIGMA_TWO_WAY * 1e3:.1f} ms")
    print(f"  least-squares sigma of the intercept = {sigma_ti * 1e3:.4f} ms")
    print(f"  predicted sigma_h = {sigma_ti * dh_dti:.4f} m "
          f"({sigma_ti * dh_dti / h_soil:.3%} of the depth)")
    n_mc = 4000
    h_draws = np.empty(n_mc)
    for k in range(n_mc):
        t = t_i + x / v2 + SIGMA_TWO_WAY * RNG.standard_normal(N_PICKS)
        A = np.vstack([np.ones_like(x), x]).T
        sol, *_ = np.linalg.lstsq(A, t, rcond=None)
        h_draws[k] = depth_from_intercept(sol[0], v1, v2)
    print(f"  Monte Carlo over {n_mc} surveys: sigma_h = {h_draws.std(ddof=1):.4f} m,"
          f" mean h = {h_draws.mean():.4f} m")
    print("  -> the analytic covariance and the simulation agree, so the depth")
    print("     error of a design can be predicted before the survey is shot.")
    print("  the same 1 ms error, for the depth from the intercept:")
    print("    contrast v2/v1   x_c (m)   sigma_ti (ms)   sigma_h (m)")
    for ratio in (1.2, 1.5, 2.0, 3.0, 5.0):
        v2b = v1 * ratio
        x_cb = crossover_two_layer(h_soil, v1, v2b)
        xb = np.linspace(x_cb, SPREAD_MULTIPLE * x_cb, N_PICKS)
        s_xxb = np.sum((xb - xb.mean()) ** 2)
        sti = SIGMA_TWO_WAY * np.sqrt(1.0 / N_PICKS + xb.mean() ** 2 / s_xxb)
        dhb = v1 * v2b / (2.0 * np.sqrt(v2b ** 2 - v1 ** 2))
        print(f"    {ratio:11.3f}   {x_cb:8.2f}   {sti * 1e3:13.4f}   "
              f"{sti * dhb:12.4f}")
    print("  -> the table keeps the geometry self-similar, so only dh/dt_i")
    print("     changes: the depth error rises from 0.281 m at a contrast of 5")
    print("     to 0.498 m at a contrast of 1.2, a factor of 1.8.")

    section("3. Downhole interval velocities and Vs30")
    print("  SYNTHETIC borehole: source at the surface, geophones at the layer")
    print("  boundaries; one-way arrival time of each geophone, sigma = 0.2 ms")
    depths = np.cumsum([layer[0] for layer in SITE])
    picks = np.concatenate([[0.0], depths])
    vs_true = np.array([layer[2] for layer in SITE])
    th_true = np.array([layer[0] for layer in SITE])
    t_true = np.cumsum(th_true / vs_true)
    print("    interval (m)   Vs true (m/s)   dt (ms)   Vs picked (m/s)   sigma_Vs")
    sigma_vs = np.empty(vs_true.size)
    vs_picked = np.empty(vs_true.size)
    for i in range(vs_true.size):
        sigma_dt = 0.2e-3 * np.sqrt(2.0)
        dt = t_true[i] - (t_true[i - 1] if i else 0.0)
        vs_picked[i] = th_true[i] / dt
        sigma_vs[i] = vs_picked[i] * sigma_dt / dt
        print(f"    {th_true[i]:5.1f}        {vs_true[i]:9.1f}   {dt * 1e3:7.3f}"
              f"   {vs_picked[i]:13.1f}   {sigma_vs[i]:8.2f}")
    print(f"  Vs30 from the noise-free intervals = {vs30:.2f} m/s "
          f"(30 m / {t30:.6f} s)")
    print(f"  site class from the standard boundaries 1500/760/360/180 m/s: "
          f"{'C' if vs30 > 360 else 'D'}")

    section("4. Elastic moduli from Vp, Vs and density")
    print("  isotropic relations: mu = rho Vs^2, nu = (Vp^2-2Vs^2)/(2(Vp^2-Vs^2)),")
    print("  E = 2 mu (1 + nu), M = rho Vp^2")
    print("    layer      Vp (m/s)   Vs (m/s)   mu (GPa)   nu       E (GPa)   M (GPa)")
    for h, vp, vs, rho in SITE:
        mu = rho * vs ** 2
        nu = (vp ** 2 - 2.0 * vs ** 2) / (2.0 * (vp ** 2 - vs ** 2))
        E = 2.0 * mu * (1.0 + nu)
        M = rho * vp ** 2
        print(f"    {h:4.0f} m   {vp:9.0f}   {vs:9.0f}   {mu / 1e9:8.3f}   "
              f"{nu:6.3f}   {E / 1e9:8.3f}   {M / 1e9:8.3f}")
    print("  Poisson's ratio is what Vp/Vs measures and it is the fragile one:")
    print("    layer   Vs error   nu error   nu range")
    for idx, (h, vp, vs, rho) in enumerate(SITE):
        nu = (vp ** 2 - 2.0 * vs ** 2) / (2.0 * (vp ** 2 - vs ** 2))
        for frac in (0.05,):
            nu_lo = (vp ** 2 - 2.0 * (vs * (1 + frac)) ** 2) / (
                2.0 * (vp ** 2 - (vs * (1 + frac)) ** 2))
            nu_hi = (vp ** 2 - 2.0 * (vs * (1 - frac)) ** 2) / (
                2.0 * (vp ** 2 - (vs * (1 - frac)) ** 2))
            print(f"    {h:4.0f} m   {frac:.0%}      {nu_lo - nu:+.4f}   "
                  f"{nu_lo:.4f} to {nu_hi:.4f}")
    print("  -> nu is most fragile where nu is near 1/4 and Vp/Vs near sqrt(3):")
    print("     a 5 % Vs error moves it by 0.026 in the bedrock. Where Vp/Vs is")
    print("     6, nu is already pinned at 1/2 and the same error moves it by")
    print("     0.0015.  A reliable nu therefore needs a reliable Vs, not a")
    print("     precise Vp.")

    section("5. Site period against the period of a structure")
    H = h_soil
    vs_eff = travel_time_average(SITE[:3], 2)[2]
    T_site = 4.0 * H / vs_eff
    print(f"  soil column: H = {H:.0f} m to bedrock, travel-time-average Vs = "
          f"{vs_eff:.1f} m/s")
    print(f"  uniform-column estimate T0 = 4H/Vs = {T_site:.4f} s "
          f"(f0 = {1.0 / T_site:.3f} Hz)")
    m_sdof = 5.0e5     # kg, SYNTHETIC mass
    k_sdof = 8.0e6     # N/m, SYNTHETIC stiffness
    T_b = 2.0 * np.pi * np.sqrt(m_sdof / k_sdof)
    print(f"  SYNTHETIC structure: m = {m_sdof:.1e} kg, k = {k_sdof:.1e} N/m "
          f"-> T = {T_b:.4f} s")
    print(f"  T_structure / T_site = {T_b / T_site:.3f}")
    k_res = m_sdof * (2.0 * np.pi / T_site) ** 2
    print(f"  stiffness for resonance with the site: k = {k_res:.3e} N/m, i.e.")
    print(f"  {k_res / k_sdof:.1f} times the design value: the design structure is far")
    print("  from resonance with this site, which is a statement about the pair,")
    print("  not about either one.")
    print("  -> the design question is a period comparison; the velocity enters")
    print("     only through the site period it implies.")

    section("6. Small strain, the operative modulus, and where it is applied")
    pgv = 0.10                      # m/s, SYNTHETIC design surface velocity
    vs_top = SITE[0][2]
    strain = pgv / vs_top
    print(f"  SYNTHETIC design PGV = {pgv:.2f} m/s in the top layer "
          f"(Vs = {vs_top:.0f} m/s)")
    print(f"  strain estimate gamma ~ PGV/Vs = {strain:.3e}")
    gamma_ref = 1.0e-3              # SYNTHETIC reference strain of the teaching curve
    g_ratio = 1.0 / (1.0 + strain / gamma_ref)
    print(f"  SYNTHETIC reduction curve G/Gmax = 1/(1 + gamma/{gamma_ref:.0e}) "
          f"-> G/Gmax = {g_ratio:.4f}")
    print(f"  Vs scales as sqrt(G/rho), so Vs -> {vs_top * np.sqrt(g_ratio):.1f} m/s"
          f" in that layer ({np.sqrt(g_ratio) - 1.0:+.1%})")
    soil = [(h, vp, vs, rho) for h, vp, vs, rho in SITE[:3]]
    uniform = [(h, vp, vs * np.sqrt(g_ratio), rho) for h, vp, vs, rho in soil]
    top_only = [(soil[0][0], soil[0][1], soil[0][2] * np.sqrt(g_ratio),
                 soil[0][3])] + soil[1:]
    print("    case                                  Vs_eff (m/s)   T_site (s)")
    for label, model in (("small strain (as measured)", soil),
                         ("reduction applied to every layer", uniform),
                         ("reduction applied only to the top layer", top_only)):
        vs_e = travel_time_average(model, 2)[2]
        print(f"    {label:36s}   {vs_e:10.1f}   {4.0 * H / vs_e:10.4f}")
    print("  -> the sign is certain and the size is not: applying the same")
    print("     reduction to every layer moves the period by "
          f"{(4.0 * H / travel_time_average(uniform, 2)[2]) / T_site - 1.0:+.1%},")
    print("     applying it only where the strain is large moves it by "
          f"{(4.0 * H / travel_time_average(top_only, 2)[2]) / T_site - 1.0:+.1%}.")
    print("     Which is right is a site-specific question that no velocity")
    print("     measurement answers, because strain depends on the shaking.")

    section("7. Uncertainty budget of Vs30")
    n_mc = 20000
    sigma_frac = sigma_vs / vs_true
    sigma_h_layer = 0.1             # m, SYNTHETIC survey tolerance
    print(f"  Vs errors from section 3 (fraction): "
          + ", ".join(f"{s:.4f}" for s in sigma_frac))
    print(f"  thickness errors: sigma = {sigma_h_layer:.2f} m on the three soil"
          " boundaries")
    base = vs30

    def column_vs30(thick_top3, vs):
        """Vs30 for a 30 m column whose top three boundaries are perturbed.

        The fourth layer absorbs the change so that the column stays 30 m deep,
        which is what a survey tolerance on the boundary depths means.
        """
        thick = np.empty(4)
        thick[:3] = np.asarray(thick_top3, dtype=float)
        thick[3] = DEPTH_REF_M - thick[:3].sum()
        return DEPTH_REF_M / np.sum(thick / vs)

    draw_v = vs_true[None, :] * (1.0 + sigma_frac[None, :]
                                 * RNG.standard_normal((n_mc, vs_true.size)))
    draw_h = th_true[:3][None, :] + sigma_h_layer * RNG.standard_normal((n_mc, 3))
    both = np.array([column_vs30(draw_h[i], draw_v[i]) for i in range(n_mc)])
    only_v = np.array([column_vs30(th_true[:3], draw_v[i]) for i in range(n_mc)])
    only_h = np.array([column_vs30(draw_h[i], vs_true) for i in range(n_mc)])
    print(f"    source               sigma_Vs30 (m/s)   variance share")
    var_tot = both.var(ddof=1)
    for label, arr in (("Vs only", only_v), ("thickness only", only_h),
                       ("both", both)):
        print(f"    {label:20s}   {arr.std(ddof=1):16.3f}   "
              f"{arr.var(ddof=1) / var_tot:13.1%}")
    print(f"  the two sources are independent, so their variances add and the")
    print(f"  two single-source variances account for "
          f"{(only_v.var(ddof=1) + only_h.var(ddof=1)) / var_tot:.1%} of the total")
    print(f"  Vs30 = {base:.2f} +/- {both.std(ddof=1):.2f} m/s, i.e. "
          f"{both.std(ddof=1) / base:.2%}")

    section("8. Quarter-wavelength limit on what the survey resolves")
    f_dom = 50.0                    # Hz, SYNTHETIC dominant frequency
    print(f"  SYNTHETIC dominant frequency f = {f_dom:.0f} Hz; a layer thinner")
    print("  than about a quarter wavelength is not resolved as a separate")
    print("  arrival (a rule of thumb, not a physical constant).")
    print("    layer   V (m/s)   lambda (m)   lambda/4 (m)   layer thickness (m)")
    for h, vp, vs, rho in SITE:
        for label, v in (("Vp", vp), ("Vs", vs)):
            lam = v / f_dom
            print(f"    {h:4.0f} m {label:>3s} {v:8.0f}   {lam:9.2f}   "
                  f"{lam / 4:12.2f}   {h:18.1f}")
    print("  -> at 50 Hz the P quarter-wavelength exceeds the thickness of every")
    print("     layer but the shallowest, while every layer is thicker than its S")
    print("     quarter-wavelength. The same profile is opaque to a P refraction")
    print("     survey and transparent to an S-wave or surface-wave survey, which")
    print("     is why shallow engineering work uses S-wave sources and MASW.")

    print("\ndone")


if __name__ == "__main__":
    main()
