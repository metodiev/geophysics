"""Stress, strain, and the brittle-ductile transition in the crust.

Run:  .venv/bin/python 01-stress_strain_demo.py
Requires: NumPy.

Companion to lesson 04-04-01. This demo builds the two halves of rock mechanics
and then puts them in competition, which is what the structure of the crust
actually reflects:

1. Stress tensors: the lithostatic state with an Anderson tectonic increment, the
   principal stresses from the eigenvalues, the invariants, and the effect of
   pore pressure on the effective stress.
2. Mohr circles, and the optimum fracture orientation verified numerically: the
   angle that maximises the Coulomb function is located by a search and compared
   with the analytic 45 deg + phi/2.
3. Frictional strength with Byerlee's empirical law, evaluated in all three
   Anderson regimes, giving the differential stress required to slip a
   critically oriented fault at each depth.
4. Power-law dislocation creep, with the strength falling exponentially with
   depth as temperature rises.
5. The brittle-ductile transition: the depth at which the two curves cross,
   located by bisection, and the sensitivity of that depth to the flow-law
   parameters, the thermal gradient and the strain rate.
6. Strain: the deformation gradient tensor, the finite strain ellipse, principal
   stretches, volumetric strain and the rotation of a passive marker through
   progressive simple shear.

Every material parameter below is labelled TABULATED or TYPICAL. Friction
coefficients, flow-law exponents and activation energies are compilation- and
rock-dependent, and a strength profile is only as good as the values chosen for
it. The numerics are verified internally (search against analytic angle, creep
curve inverted by bisection) so that the values can be replaced without breaking
the method.
"""

from __future__ import annotations

import numpy as np

# --------------------------------------------------------------------------
# TABULATED / TYPICAL values.
# --------------------------------------------------------------------------
RHO = 2700.0          # kg/m^3, typical upper-crustal density
G = 9.81              # m/s^2
MU_FRICTION = 0.85    # Byerlee's law, TYPICAL coefficient of friction
COHESION = 0.0        # Pa; intact-rock cohesion is ignored for reactivated faults
LAMBDA_P = 0.38       # TYPICAL pore-fluid factor (hydrostatic ~ 0.4)
T_SURFACE = 10.0      # degC
GEOTHERM = 25.0       # degC/km, TYPICAL continental geotherm
EPS_DOT = 1.0e-15     # s^-1, TYPICAL geological strain rate
# TYPICAL wet-quartz dislocation-creep flow-law parameters; values differ between
# studies and the profile below changes with them (see part 5 of the demo).
A_CREEP = 1.1e-4      # MPa^-n s^-1
N_CREEP = 3.0         # dimensionless stress exponent
Q_CREEP = 223.0e3     # J/mol
R_GAS = 8.314         # J/(mol K)


def depth_temperature(depth_km: float, geotherm: float = GEOTHERM) -> float:
    return T_SURFACE + geotherm * depth_km


def lithostatic_vertical(depth_km: float) -> float:
    """Vertical stress in MPa from the weight of the overburden."""
    return RHO * G * depth_km * 1.0e3 / 1.0e6


def pore_pressure(depth_km: float, lam: float = LAMBDA_P) -> float:
    return lam * lithostatic_vertical(depth_km)


def anderson_tensor(depth_km: float, regime: str, differential: float):
    """Principal stresses for one of the three Anderson regimes, in MPa."""
    sv = lithostatic_vertical(depth_km)
    if regime == "normal":
        s1, s2, s3 = sv, sv - 0.5 * differential, sv - differential
    elif regime == "strike-slip":
        s1, s2, s3 = sv + 0.5 * differential, sv, sv - 0.5 * differential
    elif regime == "reverse":
        s1, s2, s3 = sv + differential, sv + 0.5 * differential, sv
    else:
        raise ValueError("regime must be normal, strike-slip or reverse")
    return np.array([s1, s2, s3])


def part_one() -> None:
    print()
    print("1. Stress tensors and effective stress")
    print("-" * 74)
    depth = 10.0
    sv = lithostatic_vertical(depth)
    pp = pore_pressure(depth)
    print(f"  depth {depth:.0f} km, rho = {RHO:.0f} kg/m^3, "
          f"pore-fluid factor {LAMBDA_P:.2f}")
    print(f"  vertical (lithostatic) stress  Sv = rho g z = {sv:,.1f} MPa")
    print(f"  pore pressure                  Pf = {LAMBDA_P:.2f} Sv = "
          f"{pp:,.1f} MPa")
    print(f"  vertical effective stress     Sv' = {sv - pp:,.1f} MPa")
    print()
    print(f"{'regime':<14}{'S1 (MPa)':>11}{'S2 (MPa)':>11}{'S3 (MPa)':>11}"
          f"{'mean (MPa)':>13}{'von Mises (MPa)':>17}")
    for regime in ("normal", "strike-slip", "reverse"):
        principal = anderson_tensor(depth, regime, 60.0)
        mean = principal.mean()
        von_mises = np.sqrt(0.5 * ((principal[0] - principal[1]) ** 2
                                   + (principal[1] - principal[2]) ** 2
                                   + (principal[2] - principal[0]) ** 2))
        print(f"  {regime:<12}{principal[0]:>11,.1f}{principal[1]:>11,.1f}"
              f"{principal[2]:>11,.1f}{mean:>13,.1f}{von_mises:>17,.1f}")
    print("  Mean stress never changes with the tectonic regime in this "
          "construction;")
    print("  what changes is which axis the largest principal stress lies along, "
          "and that")
    print("  is what decides whether the crust faults normally, "
          "strike-slip, or in reverse.")

    # Eigenvalues of a general tensor: the principal stresses are the
    # eigenvalues of the stress matrix, whatever the coordinate frame.
    stress = np.array([[sv + 20.0, 15.0, 5.0],
                       [15.0, sv - 10.0, -8.0],
                       [5.0, -8.0, sv - 5.0]])
    vals, vecs = np.linalg.eigh(stress)
    print()
    print("  For a general stress matrix, the principal stresses are its "
          "eigenvalues:")
    print(f"    matrix eigenvalues  = {', '.join(f'{v:,.2f}' for v in vals)} MPa")
    print(f"    invariants I1, I2  = {np.trace(stress):,.2f}, "
          f"{0.5 * (np.trace(stress) ** 2 - np.trace(stress @ stress)):,.2f} MPa^2")
    # self-check: trace and determinant are invariant under the eigenbasis
    diag = np.diag(vals)
    print(f"    trace(eigenbasis)   = {np.trace(diag):,.2f} MPa "
          f"(same trace, as required)")
    print("  Resolving the same stress onto different planes gives different "
          "normal and")
    print("  shear tractions; the eigenvalues do not depend on the plane chosen. "
          "That is")
    print("  why a strength envelope needs only sigma_1 and sigma_3.")


def coulomb_function(theta: float, s1: float, s3: float, mu: float,
                     pf: float, cohesion: float = 0.0) -> float:
    """Coulomb failure function tau - mu sigma_n' - C on a plane at angle theta.

    theta is measured from the sigma_3 axis.  Returns the value in MPa; failure
    occurs where it reaches zero.
    """
    sigma_n = 0.5 * (s1 + s3) + 0.5 * (s1 - s3) * np.cos(2.0 * theta)
    tau = 0.5 * (s1 - s3) * np.sin(2.0 * theta)
    return tau - mu * (sigma_n - pf) - cohesion


def part_two() -> None:
    print()
    print("2. Mohr circle and the optimum fracture angle")
    print("-" * 74)
    s1, s3 = 120.0, 40.0
    pf = 20.0
    print(f"  sigma_1 = {s1:.0f} MPa, sigma_3 = {s3:.0f} MPa, "
          f"pore pressure {pf:.0f} MPa, mu = {MU_FRICTION:.2f}")
    print(f"  centre of the circle  = {(s1 + s3) / 2:,.1f} MPa")
    print(f"  radius of the circle  = {(s1 - s3) / 2:,.1f} MPa  "
          f"(this is the maximum shear stress)")
    print()
    print(f"{'theta (deg)':>12}{'2 theta (deg)':>15}{'sigma_n (MPa)':>15}"
          f"{'tau (MPa)':>12}{'f(MPa)':>10}")
    for theta_deg in (15.0, 30.0, 45.0, 54.0, 60.0, 75.0):
        th = np.radians(theta_deg)
        sigma_n = 0.5 * (s1 + s3) + 0.5 * (s1 - s3) * np.cos(2 * th)
        tau = 0.5 * (s1 - s3) * np.sin(2 * th)
        fval = coulomb_function(th, s1, s3, MU_FRICTION, pf)
        print(f"  {theta_deg:>12.1f}{2 * theta_deg:>15.1f}{sigma_n:>15,.1f}"
              f"{tau:>12,.1f}{fval:>10,.2f}")

    scan = np.radians(np.linspace(0.01, 89.99, 200000))
    fvals = coulomb_function(scan, s1, s3, MU_FRICTION, pf)
    theta_num = float(scan[int(np.argmax(fvals))])
    phi = np.arctan(MU_FRICTION)
    theta_ana = np.pi / 4.0 + phi / 2.0
    print()
    print(f"  located maximum of the Coulomb function: theta = "
          f"{np.degrees(theta_num):.4f} deg")
    print(f"  analytic 45 deg + phi/2 with phi = atan(mu) = "
          f"{np.degrees(phi):.3f} deg: theta = {np.degrees(theta_ana):.4f} deg")
    print(f"  difference: {abs(np.degrees(theta_num - theta_ana)):.6f} deg "
          f"(the grid spacing of the search, not a physical difference)")
    print("  Two conjugate sets at +/-theta are equally favoured, which is why "
          "conjugate")
    print("  fault sets form a 'X' with an acute bisector along sigma_1. That "
          "prediction")
    print("  is one of the few in structural geology that is directly visible in "
          "the field.")

    print()
    print("  Required differential stress for failure, by bisection on "
          "(sigma_1 - sigma_3):")
    print(f"{'mu':>6}{'theta (deg)':>14}{'differential (MPa)':>21}")

    def required_differential(mu: float) -> float:
        lo, hi = 1.0e-3, 5000.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if coulomb_function(np.pi / 4 + np.arctan(mu) / 2, s3 + mid, s3,
                                mu, pf) < 0.0:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    for mu in (0.6, 0.75, 0.85, 1.0):
        print(f"  {mu:>4.2f}{np.degrees(np.pi / 4 + np.arctan(mu) / 2):>14.2f}"
              f"{required_differential(mu):>21,.1f}")
    needed = required_differential(MU_FRICTION)
    print(f"  The state used in the Mohr circle above has sigma_1 - sigma_3 = "
          f"{s1 - s3:.0f} MPa")
    print(f"  against a required {needed:,.1f} MPa, so it is a failed state: the "
          f"Coulomb function")
    print(f"  is positive on the optimum plane. Failure is a comparison of two "
          f"numbers, not a")
    print("  property of the rock alone.")


def differential_at_failure(s3_eff: float, mu: float = MU_FRICTION,
                          cohesion: float = COHESION) -> float:
    """Differential stress needed to slide a critically oriented fault.

    On the optimum plane, tau = mu sigma_n' + C with
        tau   = (ds/2) sin 2theta,  sigma_n' = (s1'+s3')/2 + (ds/2) cos 2theta
    and theta = 45 deg + phi/2.  Solving for ds gives the closed form
        ds = 2 (mu s3' + C) / (sqrt(1 + mu^2) - mu),
    which is checked against a numerical search in part 3.
    """
    return 2.0 * (mu * s3_eff + cohesion) / (np.sqrt(1.0 + mu ** 2) - mu)


def frictional_strength_normal(depth_km: float) -> float:
    """Upper bound on the differential stress for normal faulting at a depth.

    Normal faulting has sigma_1 vertical, and the least principal effective
    stress is s3' = Sv' - ds.  Substituting into the failure condition and
    solving gives ds = 2 mu Sv' / (sqrt(1 + mu^2) + mu).
    """
    sv_eff = (lithostatic_vertical(depth_km) - pore_pressure(depth_km))
    return 2.0 * MU_FRICTION * sv_eff / (np.sqrt(1.0 + MU_FRICTION ** 2)
                                         + MU_FRICTION)


def frictional_strength_reverse(depth_km: float) -> float:
    """Differential stress for reverse faulting: sigma_3 is vertical."""
    sv_eff = lithostatic_vertical(depth_km) - pore_pressure(depth_km)
    return differential_at_failure(sv_eff)


def frictional_strength_regime(depth_km: float, regime: str) -> float:
    if regime == "normal":
        return frictional_strength_normal(depth_km)
    if regime == "reverse":
        return frictional_strength_reverse(depth_km)
    raise ValueError("strike-slip needs an assumed horizontal stress: see part 3")


def part_three() -> None:
    print()
    print("3. Frictional strength with Byerlee's law")
    print("-" * 74)
    print(f"  mu = {MU_FRICTION:.2f} (Byerlee's TYPICAL value), cohesion "
          f"neglected,")
    print(f"  pore-fluid factor {LAMBDA_P:.2f} so the effective vertical stress "
          f"is {(1 - LAMBDA_P):.2f} Sv")
    print()
    print("  Closed form  ds = 2 (mu s3' + C)/(sqrt(1+mu^2) - mu), checked "
          "against a")
    print("  numerical search for the failure stress:")
    print(f"{'s3 eff (MPa)':>15}{'closed form (MPa)':>20}"
          f"{'search (MPa)':>16}{'difference':>13}")
    for s3_eff in (0.0, 50.0, 100.0, 200.0, 400.0):
        closed = differential_at_failure(s3_eff)
        lo, hi = 1.0e-6, 1.0e4
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            f = coulomb_function(np.pi / 4 + np.arctan(MU_FRICTION) / 2,
                                 s3_eff + mid, s3_eff, MU_FRICTION, 0.0)
            if f < 0.0:
                lo = mid
            else:
                hi = mid
        search = 0.5 * (lo + hi)
        print(f"  {s3_eff:>15,.1f}{closed:>20,.3f}{search:>16,.3f}"
              f"{closed - search:>13.2e}")

    print()
    print(f"{'depth (km)':>12}{'Sv (MPa)':>11}{"Sv' (MPa)":>12}"
          f"{'normal (MPa)':>15}{'reverse (MPa)':>15}{'ratio':>9}")
    for depth in (1.0, 5.0, 10.0, 15.0, 20.0, 30.0):
        sv = lithostatic_vertical(depth)
        sv_eff = sv - pore_pressure(depth)
        normal = frictional_strength_normal(depth)
        reverse = frictional_strength_reverse(depth)
        print(f"  {depth:>10.0f}{sv:>11,.1f}{sv_eff:>12,.1f}"
              f"{normal:>15,.1f}{reverse:>15,.1f}{reverse / normal:>9.3f}")
    print("  Both are proportional to the effective vertical stress and so grow "
          "linearly")
    print("  with depth; the ratio is a constant, "
          f"{(np.sqrt(1 + MU_FRICTION ** 2) + MU_FRICTION) / (np.sqrt(1 + MU_FRICTION ** 2) - MU_FRICTION):.3f}.")
    print("  Byerlee's law therefore predicts that reverse faulting needs about "
          "four to")
    print("  five times the stress difference that normal faulting does, and "
          "strike-slip")
    print("  lies between the two but is NOT determined by depth alone: for "
          "strike-slip")
    print("  faulting the vertical axis is the INTERMEDIATE principal stress, so "
          "the least")
    print("  principal stress is horizontal and the depth says nothing about it. "
          "That is")
    print("  the general statement, and it is why a strength profile must state "
          "a regime.")
    print("  The same ratio, expressed as a bound on the stress ratio "
          "s1'/s3', is the")
    print("  classic limiting value for a crust in frictional equilibrium.")


def creep_strength(depth_km: float, eps_dot: float = EPS_DOT,
                   a: float = A_CREEP, n: float = N_CREEP,
                   q: float = Q_CREEP, geotherm: float = GEOTHERM) -> float:
    """Differential stress in MPa for dislocation creep at a given depth.

    eps_dot = A sigma^n exp(-Q/(R T))  =>  sigma = (eps_dot exp(Q/(R T))/A)^(1/n)
    """
    temperature = depth_temperature(depth_km, geotherm) + 273.15
    return (eps_dot * np.exp(q / (R_GAS * temperature)) / a) ** (1.0 / n)


def part_four() -> None:
    print()
    print("4. Dislocation creep: strength falls with depth")
    print("-" * 74)
    print(f"  flow law eps_dot = A sigma^n exp(-Q/RT) with A = {A_CREEP:.1e} "
          f"MPa^-n s^-1,")
    print(f"  n = {N_CREEP:.1f}, Q = {Q_CREEP / 1e3:.0f} kJ/mol, "
          f"strain rate {EPS_DOT:.0e} s^-1, geotherm {GEOTHERM:.0f} degC/km")
    print(f"{'depth (km)':>12}{'T (degC)':>11}{'creep strength (MPa)':>22}"
          f"{'friction, reverse (MPa)':>25}{'mode':>10}")
    for depth in (5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0):
        creep = creep_strength(depth)
        fric = frictional_strength_reverse(depth)
        mode = "brittle" if fric < creep else "ductile"
        print(f"  {depth:>10.0f}{depth_temperature(depth):>11,.0f}"
              f"{creep:>22,.1f}{fric:>25,.1f}{mode:>10}")
    print("  The creep strength is a strong function of temperature and falls by "
          "orders of")
    print("  magnitude over a few tens of kilometres, while the frictional "
          "strength rises")
    print("  linearly. A curve this steep is very sensitive to the activation "
          "energy, so a")
    print("  strength profile carries the flow-law reference with it.")
    print("  The very large creep strengths at 5 km are a warning, not a result: "
          "the flow")
    print("  law was calibrated on experiments near and above ~300 degC, and "
          "extrapolating it")
    print("  to 135 degC is far outside its regime of validity. The number is "
          "formally")
    print("  produced by the equation and physically meaningless, which is "
          "exactly why the")
    print("  regime of validity of a fitted law has to be stated.")

    sigma = np.linspace(10.0, 1000.0, 5000)
    eps = A_CREEP * sigma ** N_CREEP * np.exp(-Q_CREEP / (R_GAS * 700.0))
    log_slope = np.polyfit(np.log(sigma), np.log(eps), 1)[0]
    print()
    print(f"  stress exponent recovered by fitting log(eps_dot) against "
          f"log(sigma) at 700 K:")
    print(f"    fitted n = {log_slope:.8f}, input n = {N_CREEP:.8f}, "
          f"difference {log_slope - N_CREEP:.2e}")


def brittle_ductile_transition(eps_dot: float = EPS_DOT,
                               geotherm: float = GEOTHERM,
                               q: float = Q_CREEP) -> float:
    """Depth in km where the frictional and creep strengths are equal.

    The friction curve used is the reverse-faulting one, which is the upper
    bound on the differential stress for frictional sliding and therefore gives
    the deepest transition of the three regimes.
    """
    def difference(depth: float) -> float:
        return (frictional_strength_reverse(depth)
                - creep_strength(depth, eps_dot, q=q, geotherm=geotherm))

    # Shallow: friction < creep (brittle).  Deep: friction > creep (ductile).
    lo, hi = 0.5, 80.0
    if difference(lo) > 0.0 or difference(hi) < 0.0:
        return float("nan")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if difference(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def part_five() -> None:
    print()
    print("5. The brittle-ductile transition, and what it depends on")
    print("-" * 74)
    depth = brittle_ductile_transition()
    print(f"  reference case ({EPS_DOT:.0e} s^-1, {GEOTHERM:.0f} degC/km, "
          f"Q = {Q_CREEP / 1e3:.0f} kJ/mol, reverse-faulting friction curve):")
    print(f"    brittle-ductile transition at {depth:.2f} km")
    print(f"    friction strength there {frictional_strength_reverse(depth):,.1f} MPa")
    print(f"    creep strength there    {creep_strength(depth):,.1f} MPa")
    print(f"    residual {frictional_strength_reverse(depth) - creep_strength(depth):,.4f} MPa "
          f"(the bisection tolerance)")
    print()
    print(f"{'what is changed':<38}{'BDT depth (km)':>17}{'change (km)':>14}")
    variants = [
        ("reference", depth),
        ("geotherm 20 degC/km", brittle_ductile_transition(geotherm=20.0)),
        ("geotherm 30 degC/km", brittle_ductile_transition(geotherm=30.0)),
        ("strain rate 1e-16 s^-1", brittle_ductile_transition(eps_dot=1.0e-16)),
        ("strain rate 1e-14 s^-1", brittle_ductile_transition(eps_dot=1.0e-14)),
        ("Q = 200 kJ/mol", brittle_ductile_transition(q=200.0e3)),
        ("Q = 250 kJ/mol", brittle_ductile_transition(q=250.0e3)),
    ]
    for label, value in variants:
        print(f"  {label:<36}{value:>17.2f}{value - depth:>+14.2f}")
    print("  A hotter geotherm, a faster strain rate, or a lower activation "
          "energy all")
    print("  shallows the transition. The depth of this crossover is, to first "
          "order, the")
    print("  thickness of the seismogenic layer; the same calculation is why "
          "continental")
    print("  earthquakes concentrate in the upper crust instead of filling the "
          "whole")
    print("  lithosphere.")
    print("  Note what the table does NOT show: any dependence on rock type. "
          "That is a")
    print("  consequence of a model that carries only one creep law; a layered "
          "crust with")
    print("  quartz-bearing and feldspar-bearing layers has two crossovers and "
          "two")
    print("  seismogenic layers, and that is a real and observed structure.")


def part_six() -> None:
    print()
    print("6. Strain: the deformation gradient and the finite strain ellipse")
    print("-" * 74)
    print("  Simple shear with shear strain gamma: F = [[1, gamma], [0, 1]]")
    print(f"{'gamma':>8}{'stretch max':>14}{'stretch min':>14}"
          f"{'area':>9}{'marker rotation (deg)':>23}{'analytic':>11}")
    for gamma in (0.25, 0.5, 1.0, 2.0, 4.0):
        f_tensor = np.array([[1.0, gamma], [0.0, 1.0]])
        left = f_tensor @ f_tensor.T
        vals, vecs = np.linalg.eigh(left)
        stretch = np.sqrt(vals[::-1])
        area = np.linalg.det(f_tensor)
        # rotation of a passive marker line initially along y (the vertical)
        marker0 = np.array([0.0, 1.0])
        marker = f_tensor @ marker0
        rot = np.degrees(np.arctan2(marker[0], marker[1]))
        analytic = np.degrees(np.arctan(gamma))
        print(f"  {gamma:>6.2f}{stretch[0]:>14.6f}{stretch[1]:>14.6f}"
              f"{area:>9.3f}{rot:>23.4f}{analytic:>11.4f}")
    print("  Two checks are visible here. det F = 1 for simple shear, so the "
          "strain is")
    print("  volume-preserving, as plane strain must be. And the rotation of a "
          "marker line")
    print("  originally perpendicular to the shear plane is exactly "
          "atan(gamma): the")
    print("  classic result that coaxial strain would give zero rotation, so any "
          "rotation")
    print("  measured in the field is direct evidence of a non-coaxial path.")

    gamma = 1.0
    f_tensor = np.array([[1.0, gamma], [0.0, 1.0]])
    print()
    print(f"  finite strain ellipse for gamma = {gamma:.1f}:")
    vals, vecs = np.linalg.eigh(f_tensor @ f_tensor.T)
    order = np.argsort(vals)[::-1]
    print(f"    squared stretches = {vals[order][0]:.6f}, {vals[order][1]:.6f}")
    print(f"    stretches         = {np.sqrt(vals[order][0]):.6f}, "
          f"{np.sqrt(vals[order][1]):.6f}")
    print(f"    expected squared stretches (3 +/- sqrt5)/2 = "
          f"{(3 + np.sqrt(5)) / 2:.6f}, {(3 - np.sqrt(5)) / 2:.6f}")
    print(f"    long axis trend from the x-axis: "
          f"{np.degrees(np.arctan2(vecs[:, order[0]][1], vecs[:, order[0]][0])):.4f} deg")
    print("  The exact agreement with (3 +/- sqrt 5)/2 is the check that the "
          "eigen-decomposition")
    print("  is being read in the right order: the large stretch belongs to the "
          "large")
    print("  eigenvalue, and the axes of the finite strain ellipse bear no fixed "
          "relation")
    print("  to the axes of the infinitesimal strain.")


def main() -> None:
    print("=" * 74)
    print("Stress, strain and the brittle-ductile transition")
    print("=" * 74)
    part_one()
    part_two()
    part_three()
    part_four()
    part_five()
    part_six()
    print()
    print("=" * 74)
    print("All material parameters above are TABULATED/TYPICAL values, not")
    print("measurements of a named rock formation at a named place. The")
    print("verifications are internal: a searched angle against its analytic")
    print("value, a bisected crossover against both curves, and an eigenvalue")
    print("decomposition against a closed form.")
    print("=" * 74)


if __name__ == "__main__":
    main()
