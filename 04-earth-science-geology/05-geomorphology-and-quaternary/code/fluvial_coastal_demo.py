"""Fluvial, coastal and aeolian systems.

Run:  .venv/bin/python fluvial_coastal_demo.py
Requires: Python standard library only.

Companion to lesson 04-05-03.

Output labels every number COMPUTED, MODELLED or DERIVED. The empirical
coefficients (drag correlation, Shields threshold, Manning roughness,
Bagnold's coefficient and the breaker index) are MODELLED inputs: they are
standard forms with accepted nominal values, and no number below is a site
measurement.

Parts:

1. Settling velocity from a nonlinear drag balance, iterated to convergence,
   compared with Stokes' law and checked against the Reynolds number.
2. Shields threshold for the onset of bed motion, and the bed shear stress from
   the depth-slope product, giving the mobility ratio for a range of flows.
3. Manning flow in a rectangular channel: velocity, discharge, Froude number,
   and the downstream hydraulic-geometry scaling.
4. Linear water waves: solving the dispersion relation, shoaling by energy flux
   and the breaking depth.
5. The Rouse number as the bedload-suspension discriminant.
6. Aeolian threshold friction velocity and the Bagnold potential flux.
7. The Bruun rule stated as a model and reported as one.
"""

import math

RHO_W = 1000.0        # [kg/m^3] water
RHO_A = 1.225         # [kg/m^3] air at sea level, 15 degC
RHO_QUARTZ = 2650.0   # [kg/m^3] quartz grain density
MU_W = 1.002e-3       # [Pa s] dynamic viscosity of water at 20 degC
G = 9.81              # [m/s^2]
YEAR = 3.15576e7      # [s]

SHIELDS_CRIT = 0.045  # MODELLED dimensionless critical shear stress (nominal)
MANNING_N = 0.030     # MODELLED roughness for a natural sand-bed channel
BAGNOLD_A = 0.10      # MODELLED threshold coefficient in u*t = A sqrt(...)
BAGNOLD_C = 1.75      # MODELLED saltation-flux coefficient
BREAKER_GAMMA = 0.78  # MODELLED breaker index H/h at breaking
KAPPA_VON_KARMAN = 0.40


def schiller_naumann_cd(re: float) -> float:
    """Drag coefficient of a sphere. MODELLED correlation (Schiller-Naumann)."""
    if re < 1e-6:
        return 1e6
    return 24.0 / re * (1.0 + 0.15 * re ** 0.687)


def settling_velocity(d: float, rho_s: float = RHO_QUARTZ,
                      rho_f: float = RHO_W, mu: float = MU_W) -> tuple[float, float]:
    """Solve the drag balance for terminal velocity; return (v, C_D)."""
    def residual(v: float) -> float:
        re = rho_f * v * d / mu
        cd = schiller_naumann_cd(re)
        lhs = 0.25 * math.pi * d * d * cd * 0.5 * rho_f * v * v
        rhs = (math.pi / 6.0) * d ** 3 * (rho_s - rho_f) * G
        return lhs - rhs

    lo, hi = 1e-6, 10.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if residual(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    v = 0.5 * (lo + hi)
    return v, schiller_naumann_cd(rho_f * v * d / mu)


def stokes_velocity(d: float, rho_s: float = RHO_QUARTZ,
                    rho_f: float = RHO_W, mu: float = MU_W) -> float:
    return (rho_s - rho_f) * G * d * d / (18.0 * mu)


def part_settling() -> None:
    print("=" * 72)
    print("1. SETTLING VELOCITY -- drag balance vs Stokes")
    print("=" * 72)
    print("  Balance: (pi/6) d^3 (rho_s - rho_f) g = (pi/8) C_D rho_f d^2 v^2")
    print("  C_D from the Schiller-Naumann correlation; solved by bisection.")
    print(f"  MODELLED rho_s = {RHO_QUARTZ} kg/m^3, rho_f = {RHO_W} kg/m^3, "
          f"mu = {MU_W} Pa s")
    print()
    print("   d (mm)     v_drag (m/s)   Re     C_D    v_Stokes (m/s)  Stokes error")
    for d_mm in (0.0625, 0.125, 0.25, 0.5, 1.0, 2.0, 5.0):
        d = d_mm * 1e-3
        v, cd = settling_velocity(d)
        re = RHO_W * v * d / MU_W
        vs = stokes_velocity(d)
        print(f"   {d_mm:6.4f}   {v:12.5f}  {re:6.2f}  {cd:6.3f}   {vs:12.5f}"
              f"   {100 * (vs - v) / v:+8.2f} per cent")
    print()
    d = 0.25e-3
    v, cd = settling_velocity(d)
    print(f"  COMPUTED for 0.25 mm quartz sand: v = {v:.5f} m/s "
          f"({v * 100:.3f} cm/s), Re = {RHO_W * v * d / MU_W:.2f}, C_D = {cd:.3f}")
    print(f"  COMPUTED Stokes would give {stokes_velocity(d):.5f} m/s, an error of "
          f"{100 * (stokes_velocity(d) - v) / v:+.1f} per cent, because Re is "
          f"far above the Stokes regime (Re < 1).")
    print("  Interpretation: 3.4 cm/s is the scale of the contrast between sand")
    print("  and silt in a settling tube, and it is why a graded bed records")
    print("  grain size as a settling-velocity proxy.")


def part_shields() -> None:
    print()
    print("=" * 72)
    print("2. SHIELDS THRESHOLD AND BED MOBILITY")
    print("=" * 72)
    print(f"  MODELLED Shields critical value tau*c = {SHIELDS_CRIT}")
    print("  COMPUTED tau_c = tau*c (rho_s - rho_w) g d")
    sizes = {"silt 0.03 mm": 0.03e-3, "fine sand 0.15 mm": 0.15e-3,
             "medium sand 0.35 mm": 0.35e-3, "coarse sand 1 mm": 1.0e-3,
             "gravel 10 mm": 10.0e-3, "cobble 100 mm": 100.0e-3}
    for name, d in sizes.items():
        tc = SHIELDS_CRIT * (RHO_QUARTZ - RHO_W) * G * d
        print(f"    {name:22s}: tau_c = {tc:8.4f} Pa")
    print()
    print("  COMPUTED bed shear stress from the depth-slope product tau = rho g h S")
    for depth, slope in ((0.5, 1e-3), (2.0, 3e-4), (5.0, 2e-4)):
        tau = RHO_W * G * depth * slope
        print(f"    h = {depth:4.1f} m, S = {slope:.1e}: tau = {tau:.4f} Pa")
        for name in ("fine sand 0.15 mm", "medium sand 0.35 mm", "coarse sand 1 mm",
                     "gravel 10 mm"):
            d = sizes[name]
            tc = SHIELDS_CRIT * (RHO_QUARTZ - RHO_W) * G * d
            status = "moves" if tau > tc else "static"
            print(f"        {name:22s}: tau/tau_c = {tau / tc:7.3f}  {status}")
    print("  The threshold is a ratio, not an absolute stress, so a finer bed")
    print("  moves first at the same shear stress. That is the whole of the")
    print("  grain-size sorting seen in a point bar.")


def manning_channel(width: float, depth: float, slope: float) -> tuple[float, float]:
    area = width * depth
    perimeter = width + 2.0 * depth
    r_h = area / perimeter
    v = (1.0 / MANNING_N) * r_h ** (2.0 / 3.0) * slope ** 0.5
    return v, v * area


def part_manning() -> None:
    print()
    print("=" * 72)
    print("3. MANNING FLOW AND HYDRAULIC GEOMETRY")
    print("=" * 72)
    print(f"  MODELLED n = {MANNING_N}, rectangular channel, wide and shallow")
    print("  COMPUTED V = (1/n) R^(2/3) S^(1/2), Q = V A")
    print("   width(m) depth(m)  slope     R_h(m)   V(m/s)   Q(m^3/s)   Fr")
    for width, depth, slope in ((10.0, 1.0, 1e-3), (20.0, 1.5, 1e-3),
                                (50.0, 2.0, 5e-4), (100.0, 3.0, 2e-4)):
        v, q = manning_channel(width, depth, slope)
        fr = v / math.sqrt(G * depth)
        print(f"   {width:8.0f} {depth:8.1f} {slope:7.1e}  "
              f"{width * depth / (width + 2 * depth):7.3f} {v:8.3f} "
              f"{q:11.2f}   {fr:5.3f}")
    print("  Fr < 1 everywhere, so these are subcritical (tranquil) flows;")
    print("  supercritical flow needs Fr > 1 and is a different bedform regime.")
    print()
    print("  COMPUTED downstream hydraulic geometry, declared exponents:")
    print("    W = a Q^b, D = c Q^f, V = k Q^m with b + f + m = 1")
    b, f, m_exp = 0.50, 0.40, 0.10
    print(f"    MODELLED b = {b}, f = {f}, m = {m_exp}, sum = {b + f + m_exp}")
    for q in (1.0, 10.0, 100.0):
        rel = q / 10.0
        print(f"    Q = {q:6.1f} m^3/s: W/W10 = {rel ** b:.3f}, "
              f"D/D10 = {rel ** f:.3f}, V/V10 = {rel ** m_exp:.3f}")
    print("  The sum rule is a statement of continuity: Q = W D V, so the three")
    print("  exponents must add to one. It is a useful check on any published")
    print("  hydraulic-geometry set.")


def wave_dispersion(period: float, depth: float) -> tuple[float, float]:
    """Solve omega^2 = g k tanh(k h) for k by bisection."""
    omega = 2.0 * math.pi / period

    def resid(k: float) -> float:
        return G * k * math.tanh(k * depth) - omega * omega

    lo, hi = 1e-8, 100.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if resid(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    k = 0.5 * (lo + hi)
    return k, omega / k


def part_waves() -> None:
    print()
    print("=" * 72)
    print("4. WATER WAVES -- dispersion, shoaling and breaking")
    print("=" * 72)
    print("  COMPUTED dispersion relation omega^2 = g k tanh(k h), solved by")
    print("  bisection. Deep water: c = gT/(2 pi); shallow: c = sqrt(g h).")
    print("   T(s)   h(m)    k(1/m)    L(m)     c(m/s)   c_deep(m/s)  k h")
    for t, h in ((8.0, 100.0), (8.0, 20.0), (8.0, 5.0), (12.0, 5.0), (5.0, 2.0)):
        k, c = wave_dispersion(t, h)
        c_deep = G * t / (2.0 * math.pi)
        print(f"   {t:5.1f} {h:6.1f} {k:9.5f} {2 * math.pi / k:8.2f} "
              f"{c:9.3f} {c_deep:11.3f}   {k * h:6.3f}")
    print("  k h < 0.3 is shallow water (c = sqrt(g h), no period dependence),")
    print("  k h > 3 is deep water (c = gT/2 pi). Between them is the")
    print("  intermediate regime where refraction of swell actually happens.")
    print()
    print(f"  MODELLED breaker index gamma = {BREAKER_GAMMA}")
    print("  COMPUTED breaking depth from energy-flux conservation and H_b = gamma h_b:")
    print("    h_b^(5/2) = H0^2 c_g0 / (gamma^2 sqrt(g)),  c_g0 = c0/2")
    for h0, t in ((1.0, 6.0), (2.0, 8.0), (3.0, 10.0), (4.0, 12.0)):
        c0 = G * t / (2.0 * math.pi)
        cg0 = c0 / 2.0
        hb = (h0 ** 2 * cg0 / (BREAKER_GAMMA ** 2 * math.sqrt(G))) ** 0.4
        print(f"    H0 = {h0:3.1f} m, T = {t:4.1f} s: h_b = {hb:5.2f} m, "
              f"H_b = {BREAKER_GAMMA * hb:5.2f} m, "
              f"H_b/h_b = {BREAKER_GAMMA:.2f}")
    print("  A 2 m, 8 s swell breaks in about 2.8 m of water. That single number")
    print("  sets the surf-zone width, the bar position and the depth of the")
    print("  littoral cell all at once.")


def part_rouse() -> None:
    print()
    print("=" * 72)
    print("5. ROUSE NUMBER -- bedload versus suspension")
    print("=" * 72)
    print(f"  COMPUTED P = w_s / (kappa u*), kappa = {KAPPA_VON_KARMAN}")
    u_star = 0.05
    print(f"  MODELLED u* = {u_star} m/s (a sand-bed river)")
    for name, d in (("fine sand 0.15 mm", 0.15e-3), ("medium sand 0.35 mm", 0.35e-3),
                    ("coarse sand 1 mm", 1.0e-3), ("gravel 10 mm", 10.0e-3)):
        v, _ = settling_velocity(d)
        p = v / (KAPPA_VON_KARMAN * u_star)
        if p > 2.5:
            regime = "bedload dominated"
        elif p > 1.2:
            regime = "mixed, about half suspended"
        elif p > 0.8:
            regime = "fully suspended"
        else:
            regime = "wash load (essentially all in suspension)"
        print(f"    {name:22s}: w_s = {v:8.5f} m/s, P = {p:7.3f}  {regime}")
    print("  Thresholds are the conventional ones (2.5, 1.2, 0.8) and are")
    print("  MODELLED conventions, not exact physical boundaries.")


def part_aeolian() -> None:
    print()
    print("=" * 72)
    print("6. AEOLIAN THRESHOLD AND POTENTIAL FLUX")
    print("=" * 72)
    print(f"  MODELLED A = {BAGNOLD_A}, C = {BAGNOLD_C}, rho_a = {RHO_A} kg/m^3")
    print("  COMPUTED u*t = A sqrt((rho_s - rho_a) g d / rho_a)")
    for d_mm in (0.0625, 0.125, 0.25, 0.5, 1.0):
        d = d_mm * 1e-3
        u_t = BAGNOLD_A * math.sqrt((RHO_QUARTZ - RHO_A) * G * d / RHO_A)
        print(f"    d = {d_mm:6.4f} mm: u*t = {u_t:.4f} m/s "
              f"({u_t * 100:.2f} cm/s)")
    print("  Note the limitation: Bagnold's form is monotonic in d, so it")
    print("  predicts that the threshold falls all the way to zero as grains get")
    print("  smaller. The measured threshold instead has a minimum near 0.08-0.1")
    print("  mm and rises again below it, because interparticle cohesion becomes")
    print("  the resisting force. Reproducing that minimum needs an added")
    print("  cohesive term, which is a model input and is not included here.")
    print()
    print("  COMPUTED Bagnold's saturated flux q = C (rho_a/g) u*^3")
    for u in (0.25, 0.35, 0.50):
        q = BAGNOLD_C * RHO_A / G * u ** 3
        q_vol = q / 1600.0 * YEAR
        print(f"    u* = {u:.2f} m/s: q = {q:.5f} kg/(m s) = "
              f"{q * YEAR / 1000:8.1f} t/(m yr) = {q_vol:9.1f} m^3/(m yr)"
              f"  (potential)")
    print("  This is the potential, or saturated, flux of dry loose sand. A real")
    print("  dune field transports less because of moisture, vegetation, armour")
    print("  and supply limitation, and it is the ratio to the threshold that")
    print("  controls the bedform: ripples near threshold, dunes at several")
    print("  times it, and a flat sheet at very high transport.")


def part_bruun() -> None:
    print()
    print("=" * 72)
    print("7. THE BRUUN RULE -- a model, reported as one")
    print("=" * 72)
    print("  Model: R = S * L* / (B + h*), with S the sea-level rise, L* the")
    print("  shoreface length to closure depth, B the berm height and h* the")
    print("  closure depth. It assumes the shoreface profile translates")
    print("  landward without changing shape and that sand is conserved on the")
    print("  profile. It ignores longshore transport, sediment supply, rock,")
    print("  and it is known to fail where any of those matter.")
    for s_mm, l_star, b, h_star in ((2.0, 5000.0, 1.0, 15.0),
                                    (2.0, 20000.0, 1.0, 15.0),
                                    (5.0, 10000.0, 2.0, 20.0)):
        r = (s_mm / 1000.0) * l_star / (b + h_star)
        print(f"    S = {s_mm:4.1f} mm/yr, L* = {l_star:6.0f} m, B = {b:.0f} m, "
              f"h* = {h_star:4.0f} m: R = {r:.4f} m/yr")
    print("  Note that R scales linearly with the assumed L*, which is the")
    print("  closure depth times an assumed profile slope: the model's answer is")
    print("  only as good as that assumption, and it is a model, not physics.")


def main() -> None:
    v, _ = settling_velocity(0.25e-3)
    assert 0.030 < v < 0.040
    assert stokes_velocity(0.01e-3) > 0.0
    k, c = wave_dispersion(8.0, 100.0)
    assert abs(c - G * 8.0 / (2 * math.pi)) / c < 0.02
    part_settling()
    part_shields()
    part_manning()
    part_waves()
    part_rouse()
    part_aeolian()
    part_bruun()
    print()
    print("All assertions passed.")


if __name__ == "__main__":
    main()
