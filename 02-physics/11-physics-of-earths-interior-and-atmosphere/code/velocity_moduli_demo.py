"""Seismic velocities, elastic moduli and mineralogy.

Run:  python3 velocity_moduli_demo.py
Requires: Python standard library only.

Companion to lesson 02-11-03.

Starting from the rounded velocity and density ranges of the constant handbook
(26-reference-library/02-symbols-and-units/03-constant-handbook.md, s3.3), this
script inverts the elastic-wave relations to recover K, mu, Poisson's ratio and
the seismic parameter, and then uses those quantities to explain what a
seismogram can and cannot tell us about composition.

The script:

1. Recovers K, mu, Poisson's ratio and phi from (v_p, v_s, rho).
2. Shows that (v_p, v_s) alone does not determine rho, by construction: the
   same velocities with two different densities give two different moduli.
3. Fits Birch's law v_p = a + b rho to the silicate layers, reports the
   residuals, and shows why the law cannot be extrapolated to the core.
4. Computes normal-incidence reflection coefficients from the acoustic
   impedance at the Moho, the 410 km discontinuity, the core-mantle boundary
   and the inner-core boundary, and shows that the CMB is a weak reflector
   for P waves while being a total reflector for S waves.
"""

import math


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# Nominal anchors: (label, rho kg/m3, v_p km/s, v_s km/s)
LAYERS = (
    ("crust", 2750.0, 6.15, 3.45),
    ("upper mantle", 3300.0, 8.10, 4.50),
    ("transition zone", 4000.0, 9.70, 5.30),
    ("lower mantle", 4985.0, 12.00, 6.45),
    ("outer core", 11050.0, 9.15, 0.00),
    ("inner core", 12950.0, 11.15, 3.60),
)


def moduli(rho, vp, vs):
    """Return (K, mu) in GPa from rho (kg/m3) and velocities (km/s)."""
    vp_m, vs_m = vp * 1e3, vs * 1e3
    mu = rho * vs_m * vs_m
    k = rho * (vp_m * vp_m - (4.0 / 3.0) * vs_m * vs_m)
    return k / 1e9, mu / 1e9


def poisson(vp, vs):
    if vs == 0.0:
        return 0.5
    r = (vp / vs) ** 2
    return (r - 2.0) / (2.0 * (r - 1.0))


def part1_inversion():
    section("1. From (v_p, v_s, rho) to K, mu, Poisson's ratio and phi")
    print("  v_p^2 = (K + 4 mu/3)/rho      v_s^2 = mu/rho")
    print("  phi = v_p^2 - (4/3) v_s^2 = K/rho")
    print("  nu = (v_p^2 - 2 v_s^2) / (2 (v_p^2 - v_s^2))")
    print()
    print(f"{'layer':<16}{'rho':>7}{'v_p':>7}{'v_s':>7}{'K (GPa)':>10}"
          f"{'mu (GPa)':>10}{'K/mu':>7}{'nu':>7}{'phi km2/s2':>12}")
    for name, rho, vp, vs in LAYERS:
        k, mu = moduli(rho, vp, vs)
        phi = vp * vp - (4.0 / 3.0) * vs * vs
        ratio = f"{k / mu:.2f}" if mu > 0 else "inf"
        print(f"{name:<16}{rho:>7.0f}{vp:>7.2f}{vs:>7.2f}{k:>10.1f}"
              f"{mu:>10.1f}{ratio:>7}{poisson(vp, vs):>7.3f}{phi:>12.2f}")
    print()
    print("  Three things to read off:")
    print("   (a) K rises from ~60 GPa in the crust to ~1.4 TPa in the inner")
    print("       core: pressure dominates the incompressibility.")
    print("   (b) mu is undefined in the outer core because v_s = 0, so K/mu is")
    print("       not a material property there at all.")
    print("   (c) nu is 0.25-0.30 for the silicates, and near 0.44 in the inner")
    print("       core: the inner core is nearly incompressible relative to its")
    print("       resistance to shear, which is why v_p/v_s there is near 3 and")
    print("       not near 1.7.")


def part2_nonuniqueness():
    section("2. (v_p, v_s) alone does not determine rho")
    print("  Take one velocity pair and two densities:")
    print()
    vp, vs = 9.15, 5.00
    print(f"{'rho':>8}{'K (GPa)':>10}{'mu (GPa)':>10}{'phi km2/s2':>13}")
    for rho in (4000.0, 6000.0, 9900.0):
        k, mu = moduli(rho, vp, vs)
        phi = vp * vp - (4.0 / 3.0) * vs * vs
        print(f"{rho:>8.0f}{k:>10.1f}{mu:>10.1f}{phi:>13.2f}")
    print()
    print("  The seismic parameter phi = K/rho is fixed by the velocities alone,")
    print("  but K and mu scale with the density, which the velocities do not")
    print("  supply: tripling rho triples both K and mu and leaves phi unchanged.")
    print("  Two different densities reproduce the same seismogram and imply two")
    print("  different bulk moduli. This is the density-velocity ambiguity, and")
    print("  it is why a seismic velocity model does not by itself give a")
    print("  composition.")
    print()
    print("  The resolution has two halves:")
    print("   * An independent density constraint (free oscillations, the")
    print("     moment of inertia, normal-mode splitting, or a mineral-physics")
    print("     EOS such as lesson 02's Birch-Murnaghan) supplies rho.")
    print("   * Mineral physics supplies K and mu for a candidate assemblage at")
    print("     the same P and T. If that K and mu reproduce the observed v_p and")
    print("     v_s, the assemblage is admissible.")


def part3_birch():
    section("3. Birch's law inside the mantle, and why it fails for the core")
    silicates = [row for row in LAYERS if row[0] != "outer core"
                 and row[0] != "inner core"]
    xs = [row[1] for row in silicates]
    ys = [row[2] for row in silicates]
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / \
        sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    print(f"  Least-squares fit v_p = a + b rho over the four silicate layers:")
    print(f"    v_p (km/s) = {a:.4f} + {b * 1e3:.4f} x rho (g/cm3)")
    print(f"    i.e. a slope of {b * 1e3:.2f} km/s per g/cm3")
    print()
    print(f"{'layer':<16}{'rho':>7}{'v_p obs':>9}{'v_p fit':>9}{'resid':>9}"
          f"{'resid %':>9}")
    ss_res = ss_tot = 0.0
    for name, rho, vp, vs in LAYERS:
        fit = a + b * rho
        res = vp - fit
        print(f"{name:<16}{rho:>7.0f}{vp:>9.2f}{fit:>9.2f}{res:>9.2f}"
              f"{100 * res / vp:>9.2f}")
        if name not in ("outer core", "inner core"):
            ss_res += res * res
            ss_tot += (vp - my) ** 2
    r2 = 1.0 - ss_res / ss_tot
    print()
    print(f"  r^2 over the silicates = {r2:.5f}, so a straight line in the")
    print("  (rho, v_p) plane describes the mantle well. Published Birch-law")
    print("  slopes are of the order of 3 km/s per g/cm3; the fitted value is of")
    print("  that order, which is all that is claimed here, since the fit is to")
    print("  four rounded anchors and not to data.")
    print()
    print("  The core points, printed with the same coefficients, are far off the")
    print("  line. That is not a failure of the fit: Birch's law is an empirical")
    print("  correlation at nearly constant mean atomic weight, and the core has a")
    print("  mean atomic weight near that of iron rather than that of a silicate.")
    print("  The line must therefore not be extrapolated across the CMB. The size")
    print("  of the misfit is itself the evidence that the core is a different")
    print("  material, not merely a compressed mantle.")


def part4_impedance():
    section("4. Normal-incidence reflection coefficients from impedance")
    print("  Z = rho v_p (impedance),  R = (Z2 - Z1)/(Z2 + Z1)")
    print()
    boundaries = (
        ("Moho", 2900.0, 6.50, 3300.0, 8.10),
        ("410 km", 3600.0, 8.10, 3600.0, 9.10),
        ("core-mantle boundary", 5570.0, 13.70, 9900.0, 8.00),
        ("inner-core boundary", 12200.0, 10.30, 12800.0, 11.00),
    )
    print(f"{'boundary':<24}{'Z1 (1e6)':>11}{'Z2 (1e6)':>11}"
          f"{'R':>9}{'R %':>8}")
    for name, r1, v1, r2, v2 in boundaries:
        z1 = r1 * v1
        z2 = r2 * v2
        r = (z2 - z1) / (z2 + z1)
        print(f"{name:<24}{z1 / 1e3:>11.3f}{z2 / 1e3:>11.3f}{r:>9.4f}"
              f"{100 * r:>8.2f}")
    print()
    print("  Units: rho in kg/m3 and v in km/s give Z in 1e3 kg m^-2 s^-1, the")
    print("  column heading. The density step used at 410 km is zero, because")
    print("  the rounded handbook ranges are continuous there; a real model has a")
    print("  density step as well and a slightly larger contrast.")
    print()
    print("  Read the CMB row against the 410 km row. The core-mantle boundary")
    print("  carries a 78 per cent density jump -- by far the largest of the four")
    print("  boundaries -- yet it reflects less than a third as much P-wave")
    print("  energy at normal incidence as the 410 km discontinuity, where the")
    print("  rounded model has no density step at all. The reason is that at the")
    print("  CMB the density jump is almost exactly cancelled by the velocity")
    print("  drop: Z = rho v_p, and rho and v_p move in opposite directions.")
    print()
    print("  The Moho, the weakest density contrast of the four, is the strongest")
    print("  reflector. That is why wide-angle crustal seismology can map the")
    print("  Moho with explosive sources, and why P-waves alone give a misleading")
    print("  picture of how important each boundary is.")


def part5_s_shadow():
    section("5. Why the outer core is a total reflector for S waves")
    print("  In a fluid at rest mu = 0, so v_s = sqrt(mu/rho) = 0.")
    print("  An S wave arriving at the CMB from the mantle therefore meets a")
    print("  medium that cannot carry shear: the transmitted S amplitude is")
    print("  zero and the boundary is a perfect reflector for shear, R = -1.")
    print()
    print("  A P wave, however, converts at the same boundary: an incident P")
    print("  produces a reflected P, a reflected S, and a transmitted P.")
    print("  The partition depends on the angle of incidence as well as on the")
    print("  impedances, which is why the P-wave reflection coefficient at the")
    print("  CMB is small at normal incidence but not at large angles.")
    print()
    print("  The numbers that follow are the ones that matter for the")
    print("  observational test:")
    print(f"    v_s in the mantle just above the CMB = 7.30 km/s")
    print(f"    v_s in the outer core                 = 0 km/s (by assumption)")
    print(f"    v_p in the mantle just above the CMB  = 13.70 km/s")
    print(f"    v_p in the outer core just below      = 8.00 km/s")
    print()
    print("  A shear wave with v_s = 7.3 km/s crossing a 2891 km thick fluid")
    print("  outer core would take 2891/7.3 = 396 s and would appear in the")
    print("  S-wave coda; the observed S-wave shadow beyond about 103 degrees")
    print("  angular distance is the direct evidence that no such wave exists.")
    print("  The shadow is not an absence of signal, it is a hard boundary in")
    print("  the arrival-time curve, and it was recognised as such before the")
    print("  liquid outer core was accepted.")


def main():
    part1_inversion()
    part2_nonuniqueness()
    part3_birch()
    part4_impedance()
    part5_s_shadow()


if __name__ == "__main__":
    main()
