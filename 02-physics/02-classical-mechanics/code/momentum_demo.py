"""Momentum, impulse and collisions, including the seismic-source force system.

Run:  python3 momentum_demo.py
Requires: Python standard library only.

Companion to lesson 02-02-04.  The sections compute impulse, momentum change,
restitution and the net force/torque of a source representation, and check each
against an independent numerical calculation.

Masses, forces and geometries here are SYNTHETIC.  Where a real source is
discussed, its parameters are stated as assumed inputs, and no measured rate is
quoted.
"""

import math

G = 9.82025                   # m/s^2 at the nominal mean radius


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main() -> None:
    section("1. Impulse of a half-sine force, checked against momentum")
    f0, tau, m = 5.0e5, 0.02, 1000.0      # N, s, kg (SYNTHETIC impact)
    impulse_exact = 2 * f0 * tau / math.pi
    n = 200000
    impulse_num = 0.0
    for i in range(n):
        t1 = tau * i / n
        t2 = tau * (i + 1) / n
        impulse_num += 0.5 * (f0 * math.sin(math.pi * t1 / tau)
                             + f0 * math.sin(math.pi * t2 / tau)) * (t2 - t1)
    dv = impulse_exact / m
    print(f"  half-sine force: F0 = {f0:.1e} N over tau = {tau * 1e3:.1f} ms")
    print(f"  impulse, closed form 2 F0 tau/pi = {impulse_exact:.6f} N s")
    print(f"  impulse, trapezoid               = {impulse_num:.6f} N s")
    print(f"  relative difference              = "
          f"{abs(impulse_num - impulse_exact) / impulse_exact:.3e}")
    print(f"  mass {m:.0f} kg -> delta v = J/m = {dv:.6f} m/s")
    print("  The impulse-momentum theorem is Newton's second law integrated")
    print("  over time; it is the form you use when the force is a transient")
    print("  you cannot measure directly but whose time integral is known.")

    section("2. Collisions and the coefficient of restitution")
    ma, va, mb, vb = 3.0, 4.0, 5.0, -2.0
    p0 = ma * va + mb * vb
    ke0 = 0.5 * ma * va ** 2 + 0.5 * mb * vb ** 2
    print(f"  before: p = {p0:.6f} kg m/s, KE = {ke0:.6f} J")
    v_cm = p0 / (ma + mb)
    for e in (1.0, 0.8, 0.5, 0.0):
        # 1-D solution with restitution e (relative approach speed reversed
        # and scaled): v1' - v2' = -e (v1 - v2)
        rel = va - vb
        v1 = v_cm + mb * (-e * rel) / (ma + mb)
        v2 = v_cm - ma * (-e * rel) / (ma + mb)
        p = ma * v1 + mb * v2
        ke = 0.5 * ma * v1 ** 2 + 0.5 * mb * v2 ** 2
        print(f"  e = {e:.1f}: v1 = {v1:8.4f}, v2 = {v2:8.4f}, p = {p:8.4f}, "
              f"KE = {ke:8.4f} J, KE lost = {ke0 - ke:8.4f} "
              f"({100 * (ke0 - ke) / ke0:5.1f}%)")
    print("  Momentum is conserved for every e; kinetic energy is conserved")
    print("  only for e = 1.  The coefficient of restitution is a material")
    print("  property, and it must be measured — it is not derivable from")
    print("  momentum conservation.")

    section("3. Weight-drop source: impulse delivered to the ground")
    drop_m, height, e_drop = 1000.0, 2.0, 0.2     # kg, m, ASSUMED restitution
    v_impact = math.sqrt(2 * G * height)
    impulse = drop_m * v_impact * (1 + e_drop)
    ke_impact = 0.5 * drop_m * v_impact ** 2
    ke_rebound = e_drop ** 2 * ke_impact
    print(f"  mass {drop_m:.0f} kg released from {height:.1f} m")
    print(f"  impact speed                  = {v_impact:.4f} m/s")
    print(f"  impact kinetic energy         = {ke_impact:.4e} J")
    print(f"  impulse on the ground J = m v (1+e) = {impulse:.4e} N s")
    print(f"  rebound energy with e = {e_drop}   = {ke_rebound:.4e} J")
    print(f"  energy retained in the ground = {ke_impact - ke_rebound:.4e} J "
          f"({100 * (1 - e_drop ** 2):.1f}%)")
    print("  Only a small part of that energy goes into seismic waves: the")
    print("  rest is compaction, friction and heat.  A weight-drop source is")
    print("  characterised by its *impulse*, which is what the momentum was")
    print("  used to compute, and the seismic efficiency must be measured.")

    section("4. The double couple has zero net force and zero net torque")
    f, a = 1.0e6, 1.0e3          # N, m (SYNTHETIC representation)
    # Standard representation of a double couple with M_xy = M_yx: two
    # couples of *opposite* sense, so their moments cancel.
    forces = [
        ((0.0, +a), (+f, 0.0)),
        ((0.0, -a), (-f, 0.0)),
        ((+a, 0.0), (0.0, +f)),
        ((-a, 0.0), (0.0, -f)),
    ]
    fx = sum(p[0] for _, p in forces)
    fy = sum(p[1] for _, p in forces)
    torque_z = sum(x * py - y * px for (x, y), (px, py) in forces)
    print(f"  four point forces of magnitude {f:.1e} N at +/-{a:.0e} m")
    print(f"  net force    = ({fx:+.3e}, {fy:+.3e}) N")
    print(f"  net torque z = {torque_z:+.3e} N m")
    single_f = [(0.0, 0.0, f, 0.0)]
    print(f"  for comparison, a single force {f:.1e} N in x:")
    print(f"      net force  = ({f:+.3e}, 0.000e+00) N  <- non-zero")
    print("  A fault earthquake is modelled by the double couple: it radiates")
    print("  but injects no net linear momentum and no net angular momentum.")
    print("  A landslide or impact is modelled by a single force, which does.")
    print("  This is why the two appear differently in a source inversion.")

    section("5. Rocket equation: momentum conservation with variable mass")
    ve, m0, m1 = 2500.0, 1000.0, 100.0            # m/s, kg (SYNTHETIC)
    dv = ve * math.log(m0 / m1)
    print(f"  exhaust speed {ve:.0f} m/s, mass ratio {m0 / m1:.1f}")
    print(f"  delta v = v_e ln(m0/m1) = {dv:.4f} m/s")
    # Numerical check: discrete ejection of dm with momentum conservation.
    print("  discrete ejection, convergence to the logarithm:")
    for n in (100, 1000, 100000):
        v, m = 0.0, m0
        dm = (m0 - m1) / n
        for _ in range(n):
            # the ejected parcel leaves at speed v_e relative to the rocket in
            # the rocket's instantaneous rest frame, so v += v_e dm / m
            m -= dm
            v += ve * dm / m
        print(f"      {n:7d} parcels: delta v = {v:.6f} m/s, "
              f"relative difference from the logarithm = "
              f"{abs(v - dv) / dv:.3e}")
    print("  The rocket equation is momentum conservation applied to a system")
    print("  whose mass changes.  The discrete sum converges to the logarithm")
    print("  from above (each parcel is evaluated at the mass *after* the")
    print("  ejection) and the difference falls with the parcel size, showing")
    print("  that the continuum result is a limit, not an assumption.")

    section("6. Momentum scale of a solid-Earth process")
    # Angular momentum of the Earth's rotation, for comparison with any
    # momentum statement about a source.
    I = 8.4699e37                 # two-layer model value, 02-01-04
    omega = 7.292115e-5           # defining
    L = I * omega
    print(f"  Earth spin angular momentum L = {L:.4e} kg m^2/s")
    print(f"  a seismic source with M0 = 1.5e18 N m changes the internal")
    print(f"  momentum distribution but not L: compare M0 = 1.5e18 with L = "
          f"{L:.1e},")
    print(f"  a ratio of {1.5e18 / L:.2e}.")
    print("  Any claim that an earthquake 'changes the Earth's rotation' must")
    print("  therefore involve a change in the moment of inertia, not a")
    print("  change in angular momentum.")


if __name__ == "__main__":
    main()
