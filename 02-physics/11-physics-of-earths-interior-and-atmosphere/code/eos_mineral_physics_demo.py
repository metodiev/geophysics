"""Equations of state and high-pressure mineral physics.

Run:  python3 eos_mineral_physics_demo.py
Requires: Python standard library only.

Companion to lesson 02-11-02.

The equation of state used is the Birch-Murnaghan form, expanded to second and
to third order in the Eulerian finite strain.  The mineral parameters in the
first table are *nominal, illustrative* values from the high-pressure
literature, quoted to no more than two significant figures: the purpose is to
show the functional form and the magnitudes, not to fit any particular
experimental dataset.

The script:

1. Tabulates the Birch-Murnaghan pressure-volume curve, second and third order,
   and shows that the two coincide exactly (to round-off) when K0' = 4.
2. Inverts the EOS for V at a given P by bisection, and verifies the inversion
   by round-tripping P -> V -> P.
3. Compares an isothermal Birch-Murnaghan compression with the hydrostatic
   pressure of the layered reference model at the core-mantle boundary, and
   identifies what the discrepancy is made of.
4. Builds the seismic parameter phi = K/rho and the adiabatic temperature
   gradient (dT/dz)_ad = gamma g T / phi.
5. Estimates the thermal pressure contribution alpha K (T - T_ref) at core
   pressures, to show why an isothermal EOS is not enough in the deep Earth.
"""

import math

G0 = 9.80665                 # m/s^2

# Nominal, illustrative EOS parameters: K0 at zero pressure, K0' = dK/dP.
# Values are rounded literature anchors, not measured constants.
MINERALS = (
    ("forsterite Mg2SiO4", 128.0, 4.2, 3270.0),
    ("periclase MgO", 160.0, 4.0, 3580.0),
    ("bridgmanite MgSiO3", 260.0, 4.0, 4100.0),
    ("hcp iron Fe", 165.0, 5.0, 8300.0),
)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def bm_pressure(k0_gpa, k0p, compression, order=3):
    """Birch-Murnaghan pressure in GPa for compression V/V0.

    x = (V0/V)^(1/3); P2 = 3/2 K0 (x^7 - x^5);
    P3 = P2 (1 + 3/4 (K0' - 4) (x^2 - 1)).
    """
    x = (1.0 / compression) ** (1.0 / 3.0)
    p2 = 1.5 * k0_gpa * (x ** 7 - x ** 5)
    if order == 2:
        return p2
    return p2 * (1.0 + 0.75 * (k0p - 4.0) * (x * x - 1.0))


def invert_volume(k0_gpa, k0p, target_p_gpa, order=3):
    """Compression V/V0 at a target pressure, by bisection."""
    lo, hi = 0.3, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if bm_pressure(k0_gpa, k0p, mid, order) < target_p_gpa:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def part1_curve():
    section("1. Birch-Murnaghan pressure-volume curve")
    print("  P = 3/2 K0 (x^7 - x^5) [1 + 3/4 (K0'-4)(x^2 - 1)],  x = (V0/V)^(1/3)")
    print()
    print(f"{'V/V0':>7}{'rho/rho0':>10}"
          + "".join(f"{m[0].split()[0][:10]:>13}" for m in MINERALS))
    print(f"{'':>7}{'':>10}" + "".join(f"{'P (GPa)':>13}" for _ in MINERALS))
    for comp in (1.00, 0.98, 0.95, 0.90, 0.85, 0.80, 0.75, 0.70):
        row = f"{comp:>7.2f}{1.0 / comp:>10.3f}"
        for _name, k0, k0p, _rho in MINERALS:
            row += f"{bm_pressure(k0, k0p, comp):>13.1f}"
        print(row)
    print()
    print("  Pressure is not linear in volume. To reach a compression of 0.80")
    print("  requires far more than four times the pressure of 0.95, because K")
    print("  itself grows as the material is squeezed.")


def part2_order():
    section("2. Why K0' = 4 is special: second and third order coincide")
    print(f"{'K0 (GPa)':>10}{'K0_prime':>10}{'V/V0':>7}{'P2':>10}{'P3':>10}"
          f"{'P3-P2':>12}")
    for k0, k0p in ((160.0, 4.0), (160.0, 4.5), (160.0, 5.0), (260.0, 4.0)):
        for comp in (0.95, 0.85):
            p2 = bm_pressure(k0, k0p, comp, 2)
            p3 = bm_pressure(k0, k0p, comp, 3)
            print(f"{k0:>10.1f}{k0p:>10.1f}{comp:>7.2f}{p2:>10.2f}"
                  f"{p3:>10.2f}{p3 - p2:>12.3e}")
    print()
    print("  The third-order term is proportional to (K0' - 4), so it vanishes")
    print("  identically when K0' = 4. This is not a numerical accident: the")
    print("  third-order term is the next term in the Eulerian strain expansion,")
    print("  and its coefficient is fixed by requiring that K0' come out right.")
    print("  For most mantle minerals K0' is close to 4, which is why the")
    print("  second-order form is often good enough -- and why quoting K0'")
    print("  matters when it is not.")


def part3_inversion():
    section("3. Inverting the EOS: volume at a given pressure")
    print(f"{'mineral':<24}{'P target':>10}{'V/V0':>9}{'rho/rho0':>10}"
          f"{'P back':>10}{'residual':>11}")
    for name, k0, k0p, _rho in MINERALS:
        for target in (10.0, 50.0, 135.0, 330.0):
            comp = invert_volume(k0, k0p, target)
            back = bm_pressure(k0, k0p, comp)
            print(f"{name:<24}{target:>10.0f}{comp:>9.4f}{1.0 / comp:>10.4f}"
                  f"{back:>10.3f}{back - target:>11.2e}")
    print()
    print("  The inversion is exact to the tolerance of the bisection. That")
    print("  round trip is the standard test of an EOS implementation: an EOS")
    print("  that cannot be inverted reproducibly cannot be used to interpret a")
    print("  measured density or a measured unit-cell volume.")


def part4_isothermal_vs_model():
    section("4. Isothermal EOS versus the reference model at the CMB")
    k0 = 283.0          # GPa, K at the top of the lower mantle (see lesson 01)
    k0p = 4.0
    rho_top, rho_cmb = 4400.0, 5570.0
    comp = rho_top / rho_cmb                      # V/V0
    p_eos = bm_pressure(k0, k0p, comp)
    p_model = 134.6                               # GPa, from the hydrostatic model
    print(f"  Take the top of the lower mantle as the reference state:")
    print(f"    rho0 = {rho_top:.0f} kg/m3, K0 = {k0:.0f} GPa, K0' = {k0p:.1f}")
    print(f"  Compress that material isothermally to the CMB density")
    print(f"    rho = {rho_cmb:.0f} kg/m3  =>  V/V0 = {comp:.4f}")
    print(f"    Birch-Murnaghan pressure at that compression = {p_eos:.1f} GPa")
    print(f"    hydrostatic pressure at the CMB             = {p_model:.1f} GPa")
    print(f"    ratio EOS / hydrostatic                     = "
          f"{p_eos / p_model:.3f}")
    print()
    print("  The isothermal, single-phase EOS under-predicts the pressure by")
    print(f"  about {100 * (1 - p_eos / p_model):.0f}%. The missing physics is temperature and phase change: the")
    print("  real lower mantle is hotter at depth, and a hot material is less")
    print("  dense at a given pressure, so extra pressure is needed to reach the")
    print("  same density. Bridgmanite is also denser than the ringwoodite it")
    print("  replaces at 660 km, which adds density without pressure.")
    print("  Conclusion: an EOS calibrated at laboratory conditions cannot be")
    print("  extrapolated to the deep Earth without a thermal term and without")
    print("  the correct mineral assemblage.")


def part5_seismic_parameter():
    section("5. phi = K/rho and the adiabatic temperature gradient")
    print("  Adams-Williamson:   d rho/dz = rho g / phi")
    print("  Adiabatic gradient: (dT/dz)_ad = gamma g T / phi")
    print("  These are the same relation, because phi = K/rho and")
    print("  (dT/dP)_s = gamma T / K.")
    print()
    gamma = 1.5                                    # nominal Gruneisen parameter
    print(f"  Using gamma = {gamma:.1f} (nominal; it is of order 1-2 in the")
    print("  mantle and near 1.5 in the core), and the reference-model rho, g")
    print("  and phi of lesson 01:")
    print()
    # (depth km, region, rho, g, phi m^2/s^2)
    node = (
        (660.0, "lower mantle top", 4400.0, 9.947, 64.28e6),
        (1000.0, "lower mantle", 4578.0, 9.883, 71.26e6),
        (2000.0, "lower mantle", 5103.0, 9.882, 93.88e6),
        (2891.0, "just above CMB", 5570.0, 10.510, 116.64e6),
        (2891.0, "just below CMB", 9900.0, 10.510, 64.00e6),
        (4000.0, "outer core", 11028.0, 7.745, 83.31e6),
        (5153.0, "inner-core boundary", 12166.0, 4.387, 104.67e6),
    )
    t = 1900.0                                     # anchor at 660 km
    print(f"{'depth km':>9}{'region':>20}{'rho':>7}{'g':>7}"
          f"{'phi (m2/s2)':>13}{'T (K)':>8}{'dT/dz (K/km)':>14}")
    for i, (z, region, rho, g, phi) in enumerate(node):
        if i > 0:
            dz = z - node[i - 1][0]
            if dz > 0:
                grad_prev = gamma * node[i - 1][3] * t / node[i - 1][4] * 1e3
                t += grad_prev * dz
        grad = gamma * g * t / phi * 1e3
        print(f"{z:>9.0f}{region:>20}{rho:>7.0f}{g:>7.3f}{phi:>13.3e}"
              f"{t:>8.0f}{grad:>14.3f}")
    print()
    print("  The temperatures are integrated on the adiabat, not assumed: start")
    print("  at 1900 K at 660 km and add grad x dz at every step, recomputing")
    print("  grad from the current temperature. The absolute temperature is set")
    print("  by that one anchor; the gradients are what the physics fixes.")
    print()
    print("  Note the factor-of-two jump in dT/dz at the CMB, from 0.38 to")
    print("  0.70 K/km, and its cause: phi collapses across the boundary")
    print("  because v_p drops, so the same g T is divided by a much smaller")
    print("  phi. A mantle adiabat of a few tenths of a kelvin per kilometre")
    print("  and a core adiabat near one kelvin per kilometre are the correct")
    print("  orders of magnitude.")


def part6_thermal_pressure():
    section("6. Thermal pressure: why an isothermal EOS is not enough")
    print("  P(V,T) ~ P(V,T_ref) + alpha K (T - T_ref)")
    print()
    print(f"{'region':<20}{'alpha (1/K)':>13}{'K (GPa)':>9}{'dT (K)':>8}"
          f"{'dP_th (GPa)':>13}")
    t_ref = 300.0
    cases = (
        ("lower mantle 2000 km", 3.0e-5, 300.0, 2476.0),
        ("core-mantle boundary", 2.5e-5, 650.0, 2825.0),
        ("outer core 4000 km", 1.0e-5, 700.0, 3596.0),
        ("inner-core boundary", 1.0e-5, 1400.0, 4175.0),
    )
    for name, alpha, k, t in cases:
        dp = alpha * k * (t - t_ref)
        print(f"{name:<20}{alpha:>13.1e}{k:>9.0f}{t - t_ref:>8.0f}"
              f"{dp:>13.1f}")
    print()
    print("  The temperatures are the adiabat of section 5; the thermal")
    print("  pressures are tens of gigapascals, a substantial fraction of the")
    print("  135 GPa at the CMB itself. The thermal expansion coefficient alpha")
    print("  is nominal here, and it falls with pressure and rises with")
    print("  temperature, so this is an anchor and not a calculation. The lesson")
    print("  is that in the deep Earth P, V and T cannot be separated: a")
    print("  pressure scale calibrated at room temperature must be corrected")
    print("  before it is used at mantle temperature.")


def main():
    part1_curve()
    part2_order()
    part3_inversion()
    part4_isothermal_vs_model()
    part5_seismic_parameter()
    part6_thermal_pressure()


if __name__ == "__main__":
    main()
