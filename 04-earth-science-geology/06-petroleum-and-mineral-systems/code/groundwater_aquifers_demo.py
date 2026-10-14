"""Aquifer types and groundwater occurrence.

Run:  .venv/bin/python groundwater_aquifers_demo.py
Requires: Python standard library only.

Companion to lesson 04-06-04.

Output labels every number COMPUTED, MODELLED or DERIVED.

Note on the quantities that are *not* here. A hydraulic conductivity, a
storativity and a specific yield are properties of a *particular* aquifer, and
the values used below are MODELLED illustrations inside reported ranges. A
recharge rate, a safe yield or an abstraction licence is a water-resource and
regulatory quantity: no such number is computed or suggested here.

Parts:

1. Darcy's law, transmissivity and the specific capacity of a well.
2. Storage: specific storage for a confined aquifer against specific yield for
   an unconfined one, and what the difference means for a water balance.
3. Theis drawdown, with the exponential integral evaluated from its series and
   its integral representation, and the radius of influence.
4. Recharge from the water-table fluctuation method.
5. Archie's law: the formation factor and the resistivity signature of
   saturation.
6. The dielectric signature: CRIM mixing, GPR velocity and the reflection
   coefficient at the water table.
7. Aquifer type against the physical property contrast and the method.
"""

import math

G = 9.81
C_LIGHT = 2.99792458e8      # [m/s]

EULER_GAMMA = 0.5772156649015329


def exp1(x: float) -> float:
    """Exponential integral E1(x) = integral_x^inf exp(-t)/t dt for x > 0."""
    if x <= 0.0:
        raise ValueError("E1 is defined here for x > 0")
    if x < 1.0:
        total = -EULER_GAMMA - math.log(x)
        term = 1.0
        for n in range(1, 80):
            term *= -x / n
            add = -term / n
            total += add
            if abs(add) < 1e-17 * max(1.0, abs(total)):
                break
        return total
    # For x >= 1 the integrand exp(-s)/(x+s) is bounded by 1, so Simpson on a
    # truncated interval is accurate and simple.  E1(x) = exp(-x) times that
    # integral, because the substitution t = x + s brings out the factor.
    n = 200000
    s_max = 45.0
    h = s_max / n
    s = 0.0
    total = 0.0
    for i in range(n + 1):
        w = 1.0 if i in (0, n) else (4.0 if i % 2 else 2.0)
        total += w * math.exp(-s) / (x + s)
        s += h
    return math.exp(-x) * total * h / 3.0


def part_darcy() -> None:
    print("=" * 72)
    print("1. DARCY'S LAW, TRANSMISSIVITY AND SPECIFIC CAPACITY")
    print("=" * 72)
    print("  COMPUTED Q = K i A (Darcy), T = K b (transmissivity)")
    print(f"  MODELLED hydraulic gradient i = 0.002, cross-section A = 1000 m^2")
    print("   K (m/s)    K (m/day)   Q (m^3/day)   b (m)   T (m^2/day)")
    for k, b in ((1.0e-5, 10.0), (1.0e-4, 20.0), (1.0e-3, 5.0), (1.0e-2, 30.0)):
        q = k * 0.002 * 1000.0
        print(f"   {k:9.1e}  {k * 86400:10.2f}  {q * 86400:12.2f}   "
              f"{b:5.0f}   {k * b * 86400:12.1f}")
    print("  Gravel to silt spans five orders of magnitude in K, and the same")
    print("  factor appears in the yield. This is why the *method* for mapping an")
    print("  aquifer and the *method* for estimating its yield are different")
    print("  questions: geophysics maps the geometry and, indirectly, the grain")
    print("  size; the yield needs a pumping test.")
    print()
    print("  COMPUTED specific capacity Q/s at a well of radius 0.15 m after one")
    print("  day of pumping, from the Theis solution. It is a property of the")
    print("  well, the aquifer and the pumping duration together, not of the")
    print("  aquifer alone -- which is why two reports of 'specific capacity' for")
    print("  the same aquifer need not agree.")
    q_pump = 0.05
    t_one_day = 86400.0
    for t_trans, stor in ((0.005, 1.0e-4), (0.01, 1.0e-4), (0.05, 1.0e-4),
                          (0.01, 1.0e-3)):
        s_draw, u = theis_drawdown(q_pump, t_trans, stor, 0.15, t_one_day)
        print(f"    T = {t_trans:5.3f} m^2/s, S = {stor:.0e}: s = {s_draw:7.3f} m, "
              f"Q/s = {q_pump / s_draw * 86400:9.1f} m^3/day per metre "
              f"(u at the well = {u:.2e})")


def part_storage() -> None:
    print()
    print("=" * 72)
    print("2. STORAGE: CONFINED AGAINST UNCONFINED")
    print("=" * 72)
    print("  COMPUTED confined: S = S_s b, with S_s = rho_w g (alpha + phi beta)")
    print(f"  MODELLED rho_w = 1000 kg/m^3, alpha (matrix) = 1.0e-10 1/Pa,")
    print(f"           beta (water) = 4.4e-10 1/Pa, phi = 0.20")
    alpha_m, beta_w, phi = 1.0e-10, 4.4e-10, 0.20
    s_s = 1000.0 * G * (alpha_m + phi * beta_w)
    print(f"  COMPUTED S_s = {s_s:.4e} 1/m")
    for b in (10.0, 50.0, 200.0):
        print(f"    b = {b:5.0f} m: S = S_s b = {s_s * b:.4e} "
              f"(dimensionless)")
    print("  COMPUTED unconfined: the water released is by drainage, so the")
    print("  storage coefficient is the specific yield S_y, a MODELLED")
    print("  sediment property:")
    for name, sy in (("gravel", 0.20), ("sand", 0.15), ("silt", 0.05),
                     ("clay", 0.02)):
        print(f"    {name:8s}: S_y = {sy:.2f}")
    print(f"  COMPUTED ratio S_y / S for b = 50 m: "
          f"{0.15 / (s_s * 50.0):.0f} times more water released per metre of")
    print("  head change in the unconfined case. The two aquifers can therefore")
    print("  have the same transmissivity and completely different responses to")
    print("  a drought, which is why storage and transmissivity are separate")
    print("  targets -- and why a gravity measurement (which sees the mass) and a")
    print("  head measurement (which sees the potential) carry different")
    print("  information.")


def theis_drawdown(q: float, t_trans: float, stor: float, r: float,
                   t_seconds: float) -> tuple[float, float]:
    u = r * r * stor / (4.0 * t_trans * t_seconds)
    return q / (4.0 * math.pi * t_trans) * exp1(u), u


def part_theis() -> None:
    print()
    print("=" * 72)
    print("3. THEIS DRAWDOWN")
    print("=" * 72)
    print("  COMPUTED s(r,t) = Q/(4 pi T) W(u), u = r^2 S/(4 T t),")
    print("  W(u) = E1(u) evaluated from its series for u < 1 and from its")
    print("  integral for u >= 1.")
    print(f"  CHECK E1(1) = {exp1(1.0):.10f} (reference 0.2193839344)")
    assert abs(exp1(1.0) - 0.2193839344) < 1e-9
    q, t_trans, stor = 0.05, 0.01, 1.0e-4
    print(f"  MODELLED Q = {q} m^3/s ({q * 86400:.0f} m^3/day), "
          f"T = {t_trans} m^2/s, S = {stor:.0e} (confined)")
    print()
    print("   time (d)     s at 50 m   s at 100 m   s at 500 m   u at 500 m")
    for days in (0.1, 1.0, 10.0, 100.0, 1000.0):
        t = days * 86400.0
        s50, _ = theis_drawdown(q, t_trans, stor, 50.0, t)
        s100, _ = theis_drawdown(q, t_trans, stor, 100.0, t)
        s500, u500 = theis_drawdown(q, t_trans, stor, 500.0, t)
        print(f"   {days:8.1f}   {s50:9.3f}   {s100:10.3f}   {s500:10.3f}   "
              f"{u500:10.3e}")
    print()
    print("  COMPUTED radius of influence, taken as u = 1 (the convention where")
    print("  the well function is of order 0.22):")
    for days in (1.0, 100.0):
        t = days * 86400.0
        r = math.sqrt(4.0 * t_trans * t / stor)
        print(f"    t = {days:7.1f} d: r(u=1) = {r:9.1f} m")
    print("  The radius grows as the square root of time, and it is *not* a")
    print("  property of the aquifer alone -- it depends on the stated convention")
    print("  for where the influence ends. Reporting it without the convention is")
    print("  the standard error.")


def part_recharge() -> None:
    print()
    print("=" * 72)
    print("4. RECHARGE FROM THE WATER-TABLE FLUCTUATION METHOD")
    print("=" * 72)
    print("  COMPUTED R = S_y dh/dt for a rising water table with no pumping")
    print("  MODELLED S_y = 0.10, seasonal rise dh = 0.80 m over 1 yr")
    sy, dh, dt = 0.10, 0.80, 1.0
    print(f"    R = {sy} x {dh} / {dt} = {sy * dh * 1000:.1f} mm/yr")
    print("  COMPUTED the sensitivity, which is the whole point of the method:")
    for sy_val in (0.05, 0.10, 0.20):
        print(f"    S_y = {sy_val:.2f}: R = {sy_val * dh * 1000:.1f} mm/yr")
    print("  The answer is linear in S_y, and S_y is estimated from grain size or")
    print("  from a pumping test. A factor of two in S_y is a factor of two in the")
    print("  recharge, so the method is a *consistency* check on a water balance")
    print("  rather than an independent measurement -- and it fails entirely where")
    print("  the water table is pumped, drained or connected to a river.")


def part_archie() -> None:
    print()
    print("=" * 72)
    print("5. ARCHIE'S LAW AND THE RESISTIVITY SIGNATURE")
    print("=" * 72)
    print("  COMPUTED F = a / phi^m with a = 1, m = 2, and rho0 = F rho_w")
    print(f"  MODELLED rho_w = 10 ohm m (a nominal fresh-to-brackish water)")
    print("   phi     F        rho0 (ohm m) at Sw = 1")
    for phi in (0.40, 0.30, 0.20, 0.10, 0.05):
        f = 1.0 / phi ** 2
        print(f"   {phi:5.2f}  {f:7.2f}   {f * 10.0:10.3f}")
    print()
    print("  COMPUTED partial saturation: rho_t = rho0 / Sw^n with n = 2")
    for sw in (1.0, 0.8, 0.5, 0.3):
        f = 1.0 / 0.30 ** 2
        print(f"    phi = 0.30, Sw = {sw:.1f}: rho_t = "
              f"{f * 10.0 / sw ** 2:9.2f} ohm m")
    print("  Two cautions, both stated rather than hidden. Archie's law is an")
    print("  EMPIRICAL relation with two fitted exponents (a and m) and a fitted")
    print("  saturation exponent n, all of which are lithology dependent; and")
    print("  converting a water resistivity to a salinity or a total dissolved")
    print("  solids is a further temperature-dependent empirical step, so no")
    print("  salinity number is offered here.")


def crim_permittivity(phi: float, theta: float, eps_w: float, eps_s: float,
                      eps_a: float) -> float:
    """Complex Refractive Index Model effective permittivity."""
    root = theta * math.sqrt(eps_w) + (1.0 - phi) * math.sqrt(eps_s) \
        + (phi - theta) * math.sqrt(eps_a)
    return root * root


def part_dielectric() -> None:
    print()
    print("=" * 72)
    print("6. THE DIELECTRIC SIGNATURE AND THE WATER TABLE IN GPR")
    print("=" * 72)
    phi = 0.30
    eps_w, eps_s, eps_a = 81.0, 5.0, 1.0
    print(f"  MODELLED eps_water = {eps_w}, eps_solid = {eps_s}, eps_air = {eps_a},")
    print(f"           porosity = {phi}")
    print("  COMPUTED CRIM: sqrt(eps) = theta sqrt(eps_w) + (1-phi) sqrt(eps_s)")
    print("                              + (phi - theta) sqrt(eps_air)")
    print("   S_w    theta    eps_eff    v (m/ns)    rho (ohm m, Archie n=2)")
    for sw in (1.0, 0.8, 0.5, 0.2, 0.0):
        theta = sw * phi
        eps = crim_permittivity(phi, theta, eps_w, eps_s, eps_a)
        v = C_LIGHT / math.sqrt(eps)
        if sw > 0.0:
            rho_txt = f"{(1.0 / phi ** 2) * 10.0 / sw ** 2:12.1f}"
        else:
            rho_txt = "         n/a"
        print(f"   {sw:4.1f}   {theta:5.2f}   {eps:7.2f}   {v / 1e9:9.4f}   "
              f"{rho_txt}")
    print()
    print("  COMPUTED GPR reflection coefficient between the unsaturated and")
    print("  saturated states, R = (sqrt(eps1) - sqrt(eps2))/(sqrt(eps1) + sqrt(eps2)):")
    eps_dry = crim_permittivity(phi, 0.2 * phi, eps_w, eps_s, eps_a)
    eps_sat = crim_permittivity(phi, phi, eps_w, eps_s, eps_a)
    r1, r2 = math.sqrt(eps_dry), math.sqrt(eps_sat)
    print(f"    dry (Sw = 0.2) sqrt(eps) = {r1:.4f}, saturated sqrt(eps) = "
          f"{r2:.4f}")
    print(f"    R = {(r1 - r2) / (r1 + r2):+.4f} "
          f"({100 * abs((r1 - r2) / (r1 + r2)):.1f} per cent of amplitude)")
    print("  COMPUTED the electrical reflection at the same boundary, if the")
    print("  unsaturated zone is 300 ohm m and the saturated zone 100 ohm m:")
    print(f"    the resistivity *ratio* is 3, which is a large ERT anomaly too.")
    print("  Both methods see the water table, and they see it through different")
    print("  properties: radar through the permittivity (water has eps = 81 and")
    print("  air has 1), and electrical methods through the conductivity of the")
    print("  pore fluid. Neither measures the water table directly -- both measure")
    print("  a contrast, and the interpretation step is the same as anywhere else")
    print("  in geophysics.")


def part_methods() -> None:
    print()
    print("=" * 72)
    print("7. AQUIFER TYPE AGAINST CONTRAST AND METHOD")
    print("=" * 72)
    rows = [
        ("alluvial sand and gravel",
         "resistivity and permittivity against clay",
         "ERI, electromagnetic induction, GPR"),
        ("glacial outwash (buried valley)",
         "resistivity, seismic velocity, density",
         "seismic refraction, EM, gravity"),
        ("fractured crystalline bedrock",
         "fracture porosity: resistivity, seismic anisotropy",
         "ERT, azimuthal seismic, borehole logging"),
        ("karst / carbonate",
         "voids and clay infill: resistivity, velocity, density",
         "ERT, microgravity, GPR, seismic"),
        ("volcanic and basalt aquifer",
         "permeability from fracturing and weathering",
         "EM, ERT, magnetics for flow boundaries"),
        ("coastal / saline intrusion",
         "pore-fluid conductivity, a large resistivity contrast",
         "EM and ERT, which are the standard methods"),
    ]
    for name, contrast, methods in rows:
        print(f"  {name}")
        print(f"      sees: {contrast}")
        print(f"      method: {methods}")
    print()
    print("  Every row is a property contrast. A saline wedge is the easiest")
    print("  target in the list because the contrast is in the pore fluid itself;")
    print("  a fractured granite is the hardest because the target is a 1 per cent")
    print("  void fraction whose connectivity, not whose volume, controls the")
    print("  yield.")


def main() -> None:
    assert abs(exp1(1.0) - 0.2193839344) < 1e-9
    assert crim_permittivity(0.3, 0.3, 81.0, 5.0, 1.0) > \
        crim_permittivity(0.3, 0.0, 81.0, 5.0, 1.0)
    part_darcy()
    part_storage()
    part_theis()
    part_recharge()
    part_archie()
    part_dielectric()
    part_methods()
    print()
    print("All assertions passed.")


if __name__ == "__main__":
    main()
