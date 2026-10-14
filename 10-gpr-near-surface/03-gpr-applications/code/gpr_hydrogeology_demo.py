#!/usr/bin/env python3
"""GPR hydrogeology: dielectric mixing, soil moisture, the water table and
depth conversion.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_hydrogeology_demo.py

All models and data in this module are SYNTHETIC.  The porosities, water
contents, conductivities, depths and targets below are chosen teaching values,
not measured site properties.  The only numbers that are not chosen are the
physical constants, which are labelled as such.

Contents
--------
1. Volumetric dielectric mixing (CRIM) and the resulting GPR speed.
2. Inverting the mixing model for moisture: the porosity problem and the model
   error against an independent published calibration form.
3. A layered moisture profile: two-way times and the depth-conversion error of
   a single average velocity.
4. Water-table reflectivity: a sharp contact against a graded capillary fringe,
   with the graded case verified against the analytic sinc result.
5. Attenuation and penetration depth: the low-loss formula against the exact
   complex-wavenumber result, with the loss tangent printed as a regime check.
6. A Monte Carlo depth budget for a picked water-table time.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_M_NS = 0.299792458        # speed of light in vacuum, m/ns (exact, by definition)
Z0_OHM = 376.730313668      # impedance of free space, ohm (exact, by definition)
EPS0_F_M = 8.8541878128e-12  # vacuum permittivity, F/m (standard value)
EPS_WATER = 80.1            # static relative permittivity of pure water, 20 C
EPS_AIR = 1.0               # air, dimensionless
EPS_GRAIN = 5.0             # soil mineral grains, SYNTHETIC teaching value
PHI = 0.35                  # porosity of the teaching soil, SYNTHETIC


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def crim(phi, theta, eps_grain=EPS_GRAIN, eps_water=EPS_WATER, eps_air=EPS_AIR):
    """CRIM relative permittivity of a three-component soil.

    The complex refractive index model (CRIM) is a volumetric average of
    refractive indices, n = sqrt(eps_r):

        sqrt(eps) = (1-phi) sqrt(eps_g) + theta sqrt(eps_w) + (phi-theta) sqrt(eps_a)

    with phi the porosity and theta the volumetric water content (theta <= phi).
    Returns eps, dimensionless.
    """
    s = (1.0 - phi) * np.sqrt(eps_grain) + theta * np.sqrt(eps_water) \
        + (phi - theta) * np.sqrt(eps_air)
    return s ** 2


def v_of_eps(eps):
    """Low-loss non-magnetic phase speed in m/ns."""
    return C_M_NS / np.sqrt(eps)


def crim_theta(eps_meas, phi, eps_grain=EPS_GRAIN, eps_water=EPS_WATER,
               eps_air=EPS_AIR):
    """Invert CRIM for the water content theta given a measured permittivity."""
    s = np.sqrt(eps_meas) - (1.0 - phi) * np.sqrt(eps_grain) - phi * np.sqrt(eps_air)
    return s / (np.sqrt(eps_water) - np.sqrt(eps_air))


def topp(eps_meas):
    """Topp-type empirical soil-moisture calibration, theta(eps).

    Quoted for comparison with CRIM only; the coefficients are the published
    form and are used here as a fixed reference curve, not as site data.
    """
    return (-5.3e-2 + 2.92e-2 * eps_meas - 5.5e-4 * eps_meas ** 2
            + 4.3e-6 * eps_meas ** 3)


def reflection_coeff(eps1, eps2):
    """Normal-incidence reflection coefficient, eta = Z0/sqrt(eps_r)."""
    return (np.sqrt(eps1) - np.sqrt(eps2)) / (np.sqrt(eps1) + np.sqrt(eps2))


def alpha_low_loss(sigma, eps):
    """Low-loss attenuation constant, Np/m.  sigma in S/m, eps dimensionless."""
    return 0.5 * sigma * Z0_OHM / np.sqrt(eps)


def alpha_exact(sigma, eps, f_hz):
    """Exact attenuation constant of a lossy dielectric, Np/m.

    tan(delta) = sigma/(omega eps0 eps_r);  alpha = omega sqrt(mu eps')
    * sqrt((sqrt(1+tan^2 delta) - 1)/2).
    """
    omega = 2.0 * np.pi * f_hz
    eps_p = EPS0_F_M * eps
    mu = 4.0e-7 * np.pi
    tan_d = sigma / (omega * eps_p)
    b = np.sqrt((np.sqrt(1.0 + tan_d ** 2) - 1.0) / 2.0)
    return omega * np.sqrt(mu * eps_p) * b, tan_d


def main():
    section("1. CRIM mixing: volumetric water content to permittivity and speed")
    print(f"SYNTHETIC soil: porosity phi = {PHI:.2f}, grain eps_r = {EPS_GRAIN:.1f};")
    print(f"water eps_r = {EPS_WATER:.1f} (standard value, 20 C), air {EPS_AIR:.1f}")
    print("  theta   S=theta/phi   eps_r    v (m/ns)   lambda at 250 MHz (m)")
    for theta in np.arange(0.0, PHI + 1e-9, 0.05):
        e = crim(PHI, theta)
        v = v_of_eps(e)
        print(f"  {theta:5.2f}   {theta / PHI:11.3f}   {e:6.2f}   {v:8.4f}   "
              f"{v / 0.250:16.3f}")
    e_min = crim(PHI, 0.0)
    e_max = crim(PHI, PHI)
    print(f"\n  the same soil spans eps_r {e_min:.2f} to {e_max:.2f}, i.e. v "
          f"{v_of_eps(e_max):.4f} to {v_of_eps(e_min):.4f} m/ns")
    print(f"  the speed ratio between dry and saturated is "
          f"{v_of_eps(e_min) / v_of_eps(e_max):.2f}, so a fixed-velocity depth")
    print("  conversion is wrong by up to the same factor over one profile.")

    section("2. Inverting for moisture: the porosity problem and model error")
    eps_meas = 9.0
    print(f"measured eps_r = {eps_meas:.2f} at one point (SYNTHETIC pick);")
    print(f"the same Topp-type empirical calibration gives theta = "
          f"{topp(eps_meas):.4f}")
    print("  assumed phi   theta from CRIM   difference from the phi=0.35 value")
    theta_ref = crim_theta(eps_meas, PHI)
    for phi in (0.25, 0.30, 0.35, 0.40, 0.45, 0.50):
        th = crim_theta(eps_meas, phi)
        flag = "  (S > 1: impossible)" if th > phi else ""
        print(f"  {phi:11.2f}   {th:15.4f}   {th - theta_ref:+25.4f}{flag}")
    print(f"\n  reference: phi = {PHI:.2f} gives theta = {theta_ref:.4f} "
          f"(S = {theta_ref / PHI:.3f})")
    th_topp = topp(eps_meas)
    print(f"  the empirical calibration gives {th_topp:.4f}, i.e. "
          f"{(th_topp - theta_ref) * 100:+.2f} percentage points of volumetric")
    print(f"  water content against CRIM, at the SAME measured permittivity.")
    print("  That difference is model error, not measurement error: it is the")
    print("  petrophysical non-uniqueness of the moisture measurement.")

    section("3. A layered moisture profile: times and the conversion error")
    # SYNTHETIC teaching profile: dry topsoil, a transition, a saturated zone
    layers = (("dry topsoil", 0.00, 0.50, 0.08),
              ("transition", 0.50, 1.20, 0.22),
              ("saturated zone", 1.20, 4.00, PHI))
    print("  layer            top(m)  base(m)  theta  eps_r   v(m/ns)  "
          "1-way t(ns)  cum TWT(ns)")
    cum = 0.0
    times = []
    for name, z1, z2, theta in layers:
        e = crim(PHI, theta)
        v = v_of_eps(e)
        one = (z2 - z1) / v
        cum += 2.0 * one
        times.append(cum)
        print(f"  {name:14s} {z1:7.2f} {z2:7.2f}  {theta:5.2f}  {e:5.2f}  "
              f"{v:7.4f}  {one:11.2f}  {cum:11.2f}")
    t_twt = times[2]
    z_true = layers[2][2]
    v_shallow = v_of_eps(crim(PHI, 0.08))
    z_conv = v_shallow * t_twt / 2.0
    v_avg = layers[2][2] / (t_twt / 2.0)
    z_avg = v_avg * t_twt / 2.0
    print(f"\n  two-way time to the 4.00 m base: {t_twt:.2f} ns")
    print(f"  converted with the DRY topsoil velocity {v_shallow:.4f} m/ns: "
          f"depth = {z_conv:.2f} m (true {z_true:.2f} m, "
          f"{(z_conv - z_true) / z_true * 100:+.1f}%)")
    print(f"  converted with the travel-time average velocity {v_avg:.4f} m/ns: "
          f"depth = {z_avg:.2f} m ({(z_avg - z_true) / z_true * 100:+.1f}%)")
    print("  The average velocity is a weighted mean with the TIME as weight,")
    print("  not a depth average; both conversions are only as good as the")
    print("  velocity model, and the shallow-velocity choice is the worst case.")
    t_wt = times[1]
    z_wt_shallow = v_shallow * t_wt / 2.0
    print(f"\n  water table: true depth {layers[2][1]:.2f} m, two-way time "
          f"{t_wt:.2f} ns")
    print(f"  converted with the dry velocity it appears at "
          f"{z_wt_shallow:.2f} m ({(z_wt_shallow - layers[2][1]) / layers[2][1] * 100:+.1f}%)")

    section("4. Water-table reflectivity: sharp contact versus capillary fringe")
    e_dry = crim(PHI, 0.08)
    e_sat = crim(PHI, PHI)
    r_sharp = reflection_coeff(e_dry, e_sat)
    print(f"  eps_r above {e_dry:.2f}, below {e_sat:.2f}")
    print(f"  R = (sqrt(e1)-sqrt(e2))/(sqrt(e1)+sqrt(e2)) = {r_sharp:+.4f} "
          f"-> power {20 * np.log10(abs(r_sharp)):.1f} dB")
    # graded fringe: N thin slabs spanning the transition, Born summation.
    # Times are computed in ns and converted to seconds only inside the phase.
    f_hz = 250e6
    for fringe_m in (0.05, 0.10, 0.15, 0.30):
        n = 400
        z = np.linspace(0.0, fringe_m, n + 1)
        eps_ramp = e_dry + (e_sat - e_dry) * z / fringe_m
        r_i = np.array([reflection_coeff(eps_ramp[i], eps_ramp[i + 1])
                        for i in range(n)])
        t_ns = np.cumsum(2.0 * (z[1] - z[0]) / v_of_eps(eps_ramp[:-1]))
        spectrum = np.sum(r_i * np.exp(-1j * 2.0 * np.pi * f_hz * t_ns * 1e-9))
        tau_s = 2.0 * fringe_m / v_of_eps(0.5 * (e_dry + e_sat)) * 1e-9
        print(f"  fringe {fringe_m:.2f} m: two-way time across it {tau_s * 1e9:5.2f} ns, "
              f"f*tau = {f_hz * tau_s:.3f}")
        print(f"      summed amplitude {abs(spectrum):.4f}, ratio to sharp "
              f"{abs(spectrum) / abs(r_sharp):.3f}")
    print("  A fringe comparable with a wavelength costs most of the amplitude:")
    print("  the SAME weak echo can be a thin strong contact deep down or a thick")
    print("  weak one near the surface, and a two-way time alone cannot separate")
    print("  contrast from transition thickness.")
    # Verification of the summation itself: for a WEAK single-step contrast the
    # Bragg/Born sum over a linear ramp must equal the analytic sinc result.
    e1, e2 = 5.95, 6.55
    f_weak, fringe_weak = 250e6, 0.15
    r0 = reflection_coeff(e1, e2)
    n = 2000
    z = np.linspace(0.0, fringe_weak, n + 1)
    eps_ramp = e1 + (e2 - e1) * z / fringe_weak
    r_i = np.array([reflection_coeff(eps_ramp[i], eps_ramp[i + 1])
                    for i in range(n)])
    t_ns = np.cumsum(2.0 * (z[1] - z[0]) / v_of_eps(eps_ramp[:-1]))
    summed = np.sum(r_i * np.exp(-1j * 2.0 * np.pi * f_weak * t_ns * 1e-9))
    tau_s = 2.0 * fringe_weak / v_of_eps(0.5 * (e1 + e2)) * 1e-9
    analytic = r0 * np.sinc(f_weak * tau_s) * np.exp(-1j * np.pi * f_weak * tau_s)
    print(f"\n  verification on a weak ramp ({e1:.2f} -> {e2:.2f} over "
          f"{fringe_weak:.2f} m):")
    print(f"    R0 = {r0:+.5f}, f*tau = {f_weak * tau_s:.3f}")
    print(f"    summed {abs(summed):.6f}, analytic |R0 sinc(f tau)| "
          f"= {abs(analytic):.6f}, relative deviation "
          f"{abs(abs(summed) - abs(analytic)) / abs(analytic) * 100:.2f}%")
    print("    The analytic form is a weak-contrast (single-scattering) result;")
    print("    the direct sum is what the demonstration uses for the strong")
    print("    water-table contrast, where the two differ by several tens of")
    print("    percent because the denominator sqrt(eps) is not linear.")

    section("5. Attenuation and penetration: low-loss versus exact")
    f_list = (100e6, 250e6)
    media = (("dry sand", 4.0, 1.0e-3),
             ("moist soil", 9.0, 1.0e-2),
             ("saturated clay-rich soil", 25.0, 5.0e-2),
             ("saline wet soil", 25.0, 2.0e-1))
    print("  medium                    f(MHz)  tan(d)  alpha(low-loss)  "
          "alpha(exact)  dB/m   two-way 60 dB depth")
    for name, eps, sigma in media:
        for f in f_list:
            a_ll = alpha_low_loss(sigma, eps)
            a_ex, tan_d = alpha_exact(sigma, eps, f)
            a_db = 8.685889638 * a_ex
            print(f"  {name:24s} {f / 1e6:7.0f}  {tan_d:6.3f}  "
                  f"{a_ll:14.4f}  {a_ex:11.4f}  {a_db:5.2f}  "
                  f"{60.0 / (2.0 * a_db):18.2f} m")
    print("\n  tan(d) = sigma/(omega eps): the low-loss formula is only the")
    print("  leading term, and it fails as tan(d) approaches 1 (clay at 100 MHz).")
    print("  60 dB two-way is a conventional dynamic range, not a physical limit;")
    print("  it is quoted so the trade-off between resolution and depth is explicit.")

    section("6. Monte Carlo depth budget for a picked water-table time")
    z_true = 1.20
    v_meas = v_of_eps(e_dry)                 # m/ns, from a CMP/diffraction fit
    t_meas_ns = 2.0 * z_true / v_meas        # ns, both-way time
    n = 20000
    sigma_t_ns = 0.5                         # ns, pick error (SYNTHETIC)
    sigma_v = 0.04 * v_meas                  # m/ns, velocity error (SYNTHETIC)
    t_s_ns = t_meas_ns + RNG.normal(0.0, sigma_t_ns, n)
    v_s = v_meas + RNG.normal(0.0, sigma_v, n)
    z_s = v_s * t_s_ns / 2.0                 # m
    print(f"  true depth {z_true:.2f} m; velocity {v_meas:.4f} m/ns "
          f"(4% standard deviation); two-way time {t_meas_ns:.2f} ns "
          f"(0.5 ns standard deviation)")
    print(f"  depth estimate: mean {z_s.mean():.4f} m, standard deviation "
          f"{z_s.std():.4f} m")
    print(f"  one-at-a-time contributions:")
    print(f"    velocity only : {np.std(v_s * t_meas_ns / 2.0):.4f} m")
    print(f"    time only     : {np.std(v_meas * t_s_ns / 2.0):.4f} m")
    print(f"  the velocity term dominates by a factor of about "
          f"{np.std(v_s * t_meas_ns / 2.0) / max(np.std(v_meas * t_s_ns / 2.0), 1e-12):.1f}")
    print("  A two-way time is only ever a depth through a velocity, and the")
    print("  velocity is the larger of the two errors in a soil profile.")


if __name__ == "__main__":
    main()
