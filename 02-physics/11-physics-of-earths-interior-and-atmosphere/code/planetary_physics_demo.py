"""Comparative planetary physics and interiors.

Run:  python3 planetary_physics_demo.py
Requires: Python standard library only.

Companion to lesson 02-11-05.

The demonstrations are anchored on the Earth, because the Earth's mass, radius,
moment of inertia and core radius are the quantities we actually know, and then
generalised into the dimensionless diagnostics that are applied to other bodies.
No planetary data for other bodies is invented here: the same formulae are
evaluated over a range of parameter values so that the *shape* of the
dependence is visible, and the reader can substitute whichever body's measured
values they have.

The script:

1. The moment-of-inertia factor k = C/(M R^2) for a homogeneous sphere, for a
   two-layer planet, and inverts the Earth's nominal k to obtain the density
   ratio and core density implied by a two-layer model.
2. A table of k over a grid of (core radius fraction, core/mantle density
   ratio), which is the diagnostic used to infer that a planet has a core.
3. The magnetic Reynolds number and the magnetic diffusion time of a
   conducting core, and the thermal diffusion time across the same core.
4. The Jeans escape parameter and the scale height, which decide which
   atmospheric constituents a body can retain.
"""

import math

G = 6.67430e-11
R_EARTH = 6.371e6
M_EARTH = 5.972e24
F_CMB = 3480.0 / 6371.0        # core radius fraction, from the handbook depths
K_EARTH = 0.33                 # nominal, rounded C/(M R^2)
MU0 = 1.25663706212e-6         # N/A^2, CODATA (measured)
K_B = 1.380649e-23             # J/K, exact
U_ATOMIC = 1.66053906660e-27   # kg, exact-ish (derived from N_A)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def k_factor(f, alpha):
    """C/(M R^2) for a two-layer planet.

    Core of radius fraction f and density alpha times the mantle density:
    k = 0.4 (f^5 alpha + 1 - f^5) / (f^3 alpha + 1 - f^3).
    The 0.4 is the homogeneous-sphere value; the second factor is the
    central condensation.
    """
    f3, f5 = f ** 3, f ** 5
    return 0.4 * (f5 * alpha + 1.0 - f5) / (f3 * alpha + 1.0 - f3)


def part1_two_layer():
    section("1. The moment-of-inertia factor is a measure of central condensation")
    print("  For a spherically symmetric body, C = (8 pi/3) integral rho r^4 dr.")
    print("  Homogeneous sphere:  C/(M R^2) = 2/5 = 0.400")
    print("  Point mass at the centre:        C/(M R^2) -> 0")
    print(f"  Earth (nominal, rounded):        C/(M R^2) = {K_EARTH:.2f}")
    print()
    print("  Two-layer model: core radius fraction f, core density alpha times")
    print("  the mantle density. Then")
    print("    k = 0.4 (f^5 alpha + 1 - f^5) / (f^3 alpha + 1 - f^3).")
    print()
    print("  Solve for alpha at the Earth's k and the seismological f:")
    f = F_CMB
    f3, f5 = f ** 3, f ** 5
    # k = 0.4 (f5 a + 1 - f5)/(f3 a + 1 - f3)  =>  solve linearly in alpha
    alpha = (0.4 * (1.0 - f5) - K_EARTH * (1.0 - f3)) / \
            (K_EARTH * f3 - 0.4 * f5)
    print(f"    f = {3480.0 / 6371.0:.4f} "
          f"(core radius 3480 km / mean radius 6371 km)")
    print(f"    alpha = rho_core / rho_mantle = {alpha:.3f}")
    s = f3 * alpha + 1.0 - f3
    rho_m = M_EARTH / ((4.0 / 3.0) * math.pi * R_EARTH ** 3 * s)
    print(f"    mean mantle density implied = {rho_m:.0f} kg/m3")
    print(f"    mean core density implied   = {rho_m * alpha:.0f} kg/m3")
    print()
    print("  Read that against the handbook's own core densities: outer core")
    print("  9900-12200 kg/m3, inner core 12800-13100 kg/m3. A two-layer model")
    print("  forced only by the total mass, the radius, the moment of inertia")
    print("  and the core radius returns a mean core density in that range.")
    print("  This is the classical argument that the Earth has a dense central")
    print("  core, and it is why the moment of inertia is the primary")
    print("  diagnostic for the internal structure of any planet.")


def part2_grid():
    section("2. k over a grid of (core size, core density contrast)")
    print("  A single k value does not determine both f and alpha; it fixes a")
    print("  curve in the (f, alpha) plane. Read down a column to see how much")
    print("  k changes with core size at fixed density contrast.")
    print()
    alphas = (1.0, 1.5, 2.0, 3.0, 4.0)
    print(f"{'f':>6}" + "".join(f"{'alpha=' + str(a):>11}" for a in alphas))
    for f in (0.0, 0.2, 0.4, 0.5, 0.55, 0.6, 0.7, 0.8):
        print(f"{f:>6.2f}" + "".join(f"{k_factor(f, a):>11.4f}"
                                     for a in alphas))
    print()
    print("  alpha = 1 is a homogeneous body, and the row is 0.4000 everywhere.")
    print("  For f = 0 the row is also 0.4000: a core of zero radius changes")
    print("  nothing. Between those limits k falls as the core grows or as the")
    print("  density contrast grows, and because the two act in the same")
    print("  direction a measured k fixes a *curve* in the (f, alpha) plane and")
    print("  not a point on it. That degeneracy is why the moment of inertia")
    print("  alone cannot give a unique internal structure: additional")
    print("  information, such as the seismic core radius or a measured gravity")
    print("  quadrupole, is required to break it.")
    print()
    print("  Two consequences used constantly in comparative planetology:")
    print("   * k noticeably below 0.4 requires denser material toward the")
    print("     centre, so a low k is evidence for a core.")
    print("   * For a fixed composition and equation of state, a larger body")
    print("     compresses more and has a higher central density, so k falls")
    print("     with increasing mass even without a composition change.")


def part3_dynamo():
    section("3. The magnetic Reynolds number and diffusion times")
    print("  Rm = mu0 sigma U L      tau_eta = mu0 sigma L^2")
    print("  A magnetic field is frozen into a sufficiently conducting, fast")
    print("  flow when Rm >> 1; dynamo action is generally found for Rm above a")
    print("  few tens.")
    print()
    sigma = 1.0e6          # S/m, nominal for liquid iron alloy
    u = 3.0e-4             # m/s, nominal core flow speed (0.3 mm/s)
    length = 2.0e6         # m, nominal core scale (2000 km)
    rm = MU0 * sigma * u * length
    tau_eta = MU0 * sigma * length ** 2
    print(f"  sigma = {sigma:.1e} S/m (nominal), U = {u * 1e3:.2f} mm/s")
    print(f"  (nominal), L = {length / 1e3:.0f} km (nominal)")
    print()
    print(f"  Rm        = {rm:.1f}")
    print(f"  tau_eta   = {tau_eta:.3e} s = {tau_eta / 3.15576e7:.3e} yr")
    print()
    print("  Rm of several hundred is comfortably above the dynamo threshold, so")
    print("  the Earth's outer core can sustain a field. The diffusion time is")
    print("  the decay time of the field if the motion were switched off; it is")
    print("  only of order 1e5 yr, which is why palaeomagnetic evidence for a")
    print("  field over billions of years is direct evidence that the dynamo has")
    print("  operated for that long.")
    print()
    kappa_th = 1.0e-5      # m^2/s, nominal thermal diffusivity of liquid iron
    tau_th = length ** 2 / kappa_th
    print(f"  For comparison, the thermal diffusion time over the same length")
    print(f"  with a nominal thermal diffusivity of {kappa_th:.0e} m2/s is")
    print(f"    tau_th = {tau_th:.3e} s = {tau_th / 3.15576e7:.3e} yr,")
    print(f"  which is longer than the age of the Earth (about 4.5 Gyr). A core")
    print("  that could only conduct its heat away would still be nearly")
    print("  isothermal; convection is required, and convection is also what the")
    print("  dynamo needs. Two requirements, one mechanism.")
    print()
    print("  The three ingredients are therefore: a conducting fluid, an")
    print("  energy source to drive convection, and rotation to organise the")
    print("  flow. Remove any one and the global field disappears -- which is")
    print("  the framework for comparing planetary magnetic fields.")


def part4_escape():
    section("4. Which atmosphere a body can keep")
    print("  Scale height H = k T /(m g) = R_specific T / g")
    print("  Jeans parameter lambda = G M m /(k T r_exo) = v_esc^2 m /(2 k T)")
    print("  lambda is roughly the ratio of gravitational to thermal energy of a")
    print("  molecule at the exobase. Retention over billions of years needs")
    print("  lambda of a few tens; at lambda below about 10 escape is fast. The")
    print("  threshold is approximate and depends on the species and on the age.")
    print()
    t_exo = 1000.0         # K, nominal exospheric temperature
    print(f"  Using an exobase at 500 km and a nominal exospheric temperature of")
    print(f"  {t_exo:.0f} K (both nominal, they vary with solar activity):")
    print()
    r_exo = R_EARTH + 5.0e5
    print(f"{'species':<10}{'m (u)':>8}{'H (km)':>9}{'v_esc':>8}"
          f"{'lambda':>9}{'kept?':>8}")
    species = (("H2", 2.016), ("He", 4.003), ("N2", 28.014),
               ("O2", 31.998), ("CO2", 44.010))
    g_exo = G * M_EARTH / r_exo ** 2
    v_esc = math.sqrt(2.0 * G * M_EARTH / r_exo)
    for name, m_u in species:
        m = m_u * U_ATOMIC
        h = K_B * t_exo / (m * g_exo)
        lam = G * M_EARTH * m / (K_B * t_exo * r_exo)
        kept = "yes" if lam > 30 else ("slow" if lam > 10 else "no")
        print(f"{name:<10}{m_u:>8.3f}{h / 1e3:>9.2f}{v_esc / 1e3:>8.2f}"
              f"{lam:>9.1f}{kept:>8}")
    print()
    print("  The scale height falls with molecular mass, so heavy molecules")
    print("  occupy a thin layer and light ones extend far out. The Jeans")
    print("  parameter, being proportional to molecular mass, sorts the")
    print("  atmosphere by what can escape: hydrogen and helium leak, nitrogen")
    print("  and oxygen do not.")
    print()
    print("  The same formula is the whole comparative story for atmospheres.")
    print("  Escape is easier on a body with weaker gravity (small M/R), and")
    print("  easier when the exosphere is hot. That is why the large cold giant")
    print("  planets hold hydrogen and helium while a warm small body does not,")
    print("  and why the loss is selective rather than wholesale.")


def main():
    part1_two_layer()
    part2_grid()
    part3_dynamo()
    part4_escape()


if __name__ == "__main__":
    main()
