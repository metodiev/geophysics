"""Geothermal systems, heat flow and resource assessment.

Run:  .venv/bin/python geothermal_systems_demo.py
Requires: Python standard library only.

Companion to lesson 04-06-03.

Output labels every number COMPUTED, MODELLED or DERIVED.

Two boundaries are observed throughout:

* The **heat in place** is a physical quantity and is computed. Converting it to
  a recoverable energy or a capacity is an *engineering* question, governed by a
  recovery factor, a flow rate, a well count and a lifetime. No recovery factor,
  capacity or reserve figure is stated here; the recovery factor is left
  symbolic and the demo prints how the answer depends on it.
* The **temperature at depth** is computed from a stated gradient and
  conductivity. A real temperature at a proposed well site is a measurement
  from a well, not a calculation.

Parts:

1. Conductive heat flow from a gradient and a conductivity, and the temperature
   profile with a radiogenic source term.
2. The Rayleigh number for convection in a saturated porous layer, compared with
   the Horton-Rogers-Lapwood critical value, and why the onset depends on the
   product of layer thickness and temperature contrast.
3. Heat in place in a rock volume, with the recovery factor left symbolic.
4. Magnetotelluric skin depth, and the clay-cap contrast that makes MT the
   standard geothermal exploration method.
5. The temperature excess of an anomalous heat flow, and how deep a borehole
   must be to resolve it.
"""

import cmath
import math

# --------------------------------------------------------------------------
# MODELLED inputs
# --------------------------------------------------------------------------

K_ROCK = 2.5            # [W/(m K)] thermal conductivity of the rock column
GRADIENT = 25.0e-3      # [K/m] = 25 K/km
T_SURFACE = 10.0        # [degC]
HEAT_PRODUCTIVITY = 2.0e-6   # [W/m^3] radiogenic heat production, 2 uW/m^3

PERM = 1.0e-14          # [m^2] permeability of the reservoir layer (~10 mD)
RHO_W = 1000.0          # [kg/m^3]
C_W = 4186.0            # [J/(kg K)]
ALPHA_THERM = 5.0e-4    # [1/K] thermal expansion of water
MU_W = 2.5e-4           # [Pa s] dynamic viscosity of water at ~130 degC
LAMBDA_SAT = 2.0        # [W/(m K)] saturated rock conductivity
RA_CRIT = 4.0 * math.pi ** 2   # Horton-Rogers-Lapwood critical Rayleigh number

RHO_BULK = 2700.0       # [kg/m^3]
C_BULK = 900.0          # [J/(kg K)]
MU0 = 4.0e-7 * math.pi  # [H/m]


def part_heat_flow() -> None:
    print("=" * 72)
    print("1. CONDUCTIVE HEAT FLOW AND THE GEOTHERM")
    print("=" * 72)
    print("  COMPUTED q = k dT/dz (Fourier's law, one dimensional, steady)")
    print(f"  MODELLED surface temperature {T_SURFACE} degC")
    print("   conductivity (W/m/K)   gradient (K/km)   q (mW/m^2)")
    for k in (1.5, 2.0, 2.5, 3.5):
        for grad_km in (20.0, 25.0, 40.0):
            q = k * grad_km * 1e-3
            print(f"   {k:19.1f}   {grad_km:15.1f}   {q * 1000:9.2f}")
    print("  A 2.5 W/(m K) column at 25 K/km gives 62.5 mW/m^2, the order of")
    print("  magnitude of continental heat flow. Note that neither k nor the")
    print("  gradient is a constant: k varies with lithology and porosity and")
    print("  the gradient varies with the local flux, so a heat-flow map is a")
    print("  product of two measured fields and inherits both of their errors.")
    print()
    print("  COMPUTED temperature profile with a radiogenic source term:")
    print("    T(z) = T0 + q0 z/k + A z^2/(2k)")
    q0 = K_ROCK * GRADIENT
    print(f"    MODELLED q0 = {q0 * 1000:.2f} mW/m^2 at the surface, "
          f"A = {HEAT_PRODUCTIVITY * 1e6:.1f} uW/m^3")
    print("     z (km)   T without A (degC)   T with A (degC)   difference")
    for z_km in (1.0, 2.0, 3.0, 5.0):
        z = z_km * 1000.0
        t_lin = T_SURFACE + q0 * z / K_ROCK
        t_src = T_SURFACE + q0 * z / K_ROCK + HEAT_PRODUCTIVITY * z * z / (2.0 * K_ROCK)
        print(f"     {z_km:5.1f}   {t_lin:17.1f}   {t_src:15.1f}   "
              f"{t_src - t_lin:8.2f}")
    print("  The source term is quadratic in depth, so it matters at depth and")
    print("  not near the surface: A = 2 uW/m^3 adds 10 K at 5 km, which is a")
    print("  large enough effect that lesson 04-05-04's borehole analysis has to")
    print("  separate it from a palaeoclimate transient.")


def rayleigh_number(h: float, d_temp: float) -> float:
    """Rayleigh number for convection in a saturated porous layer."""
    return (PERM * RHO_W ** 2 * C_W * 9.81 * ALPHA_THERM * d_temp * h
            / (MU_W * LAMBDA_SAT))


def part_convection() -> None:
    print()
    print("=" * 72)
    print("2. ONSET OF CONVECTION IN A SATURATED LAYER")
    print("=" * 72)
    print("  COMPUTED Rayleigh number for a porous layer:")
    print("    Ra = k_perm rho_w^2 c_p g alpha dT H / (mu lambda)")
    print(f"  MODELLED permeability {PERM:.1e} m^2, alpha = {ALPHA_THERM:.1e} 1/K,")
    print(f"           mu = {MU_W:.1e} Pa s, lambda = {LAMBDA_SAT} W/(m K)")
    print(f"  COMPUTED critical value Ra_c = 4 pi^2 = {RA_CRIT:.3f}")
    print("   H (m)    dT (K)     Ra        Ra/Ra_c   regime")
    for h, dt in ((500.0, 50.0), (1000.0, 100.0), (1000.0, 50.0),
                  (2000.0, 150.0), (3000.0, 200.0)):
        ra = rayleigh_number(h, dt)
        ratio = ra / RA_CRIT
        regime = "convecting" if ratio > 1.0 else "conductive"
        print(f"   {h:6.0f}   {dt:7.0f}   {ra:9.2f}   {ratio:8.3f}   {regime}")
    print("  Ra is proportional to the product H dT, so a thin layer with a")
    print("  large contrast and a thick layer with a small one are not")
    print("  equivalent: what matters is the product. The 1 km, 100 K case sits")
    print("  at 1.04 times critical -- marginally convecting, which is the honest")
    print("  answer for a plausible reservoir and is exactly why a real field is")
    print("  neither obviously conductive nor obviously convective.")
    print("  The other two MODEL inputs that would change the conclusion are the")
    print("  permeability and the fluid viscosity: both appear to the first power,")
    print("  and permeability varies by orders of magnitude in a real reservoir,")
    print("  so Ra is not a number to be trusted to two figures.")


def part_heat_in_place() -> None:
    print()
    print("=" * 72)
    print("3. HEAT IN PLACE, AND WHERE THE ENGINEERING BEGINS")
    print("=" * 72)
    print("  COMPUTED Q = rho c V dT for a volume of hot rock")
    print(f"  MODELLED rho = {RHO_BULK} kg/m^3, c = {C_BULK} J/(kg K)")
    for v_km3, dt in ((1.0, 100.0), (10.0, 150.0), (100.0, 200.0)):
        v = v_km3 * 1e9
        q = RHO_BULK * C_BULK * v * dt
        print(f"    V = {v_km3:6.1f} km^3, dT = {dt:5.0f} K: Q = {q:.3e} J "
              f"= {q / 1e15:.3f} PJ")
    print("  COMPUTED the recoverable energy is Q_rec = R x Q, with R an")
    print("  ENGINEERING recovery factor. The demo does not choose a value for")
    print("  R: it is a function of the reservoir's permeability, the well")
    print("  pattern, the flow rate, the reinjection temperature, the project")
    print("  lifetime and the economics. What the physics fixes is the")
    print("  sensitivity: dQ_rec/dR = Q, so a factor of two in R is a factor of")
    print("  two in the answer, and no amount of additional geophysics removes")
    print("  that dependence.")
    print()
    print("  COMPUTED the instantaneous thermal power for a stated mass flow:")
    print("    P = m_dot c dT. The mass flow rate is an ENGINEERING input (a")
    print("    well test or a simulation), so it is shown as a function of m_dot:")
    for m_dot in (10.0, 50.0, 200.0):
        for dt in (50.0, 100.0):
            p = m_dot * C_W * dt
            print(f"    m_dot = {m_dot:5.0f} kg/s, dT = {dt:5.0f} K: "
                  f"P = {p / 1e6:7.1f} MW_th")
    print("  Note the units: this is a *thermal* power, before any conversion")
    print("  efficiency, which is another engineering parameter and is not")
    print("  stated here.")


def skin_depth(rho: float, period: float) -> float:
    return math.sqrt(2.0 * rho / (2.0 * math.pi / period * MU0))


def mt_apparent_resistivity(layers: list[tuple[float, float]],
                            period: float) -> float:
    """Cagniard apparent resistivity of a 1-D layered earth.

    layers: [(resistivity (ohm m), thickness (m)), ...] with the last entry a
    half-space, whose thickness is ignored. The recursion starts from the
    half-space impedance Z = sqrt(i omega mu0 rho) and works upwards.
    """
    omega = 2.0 * math.pi / period
    rho_last = layers[-1][0]
    z = cmath.sqrt(1j * omega * MU0 * rho_last)
    for rho, thickness in reversed(layers[:-1]):
        k = cmath.sqrt(1j * omega * MU0 / rho)
        zeta = rho * k
        t = cmath.tanh(k * thickness)
        z = zeta * (z + zeta * t) / (zeta + z * t)
    return abs(z) ** 2 / (omega * MU0)


def part_mt() -> None:
    print()
    print("=" * 72)
    print("4. MAGNETOTELLURIC SKIN DEPTH AND THE CLAY-CAP RESPONSE")
    print("=" * 72)
    print("  COMPUTED skin depth delta = sqrt(2 rho / (omega mu0)) = 503 sqrt(rho T)")
    print("   resistivity (ohm m)   T = 1 s     T = 10 s    T = 100 s")
    for rho in (1.0, 5.0, 10.0, 100.0, 1000.0):
        row = f"   {rho:19.1f}"
        for t in (1.0, 10.0, 100.0):
            row += f"   {skin_depth(rho, t):10.1f}"
        print(row)
    print("  Units are metres. Sounding depth is set by the period, so an MT site")
    print("  is a depth profile, and the depth is a *resistivity-weighted* depth:")
    print("  a feature at 1 km inside a conductive clay cap is reached at a much")
    print("  shorter period than one at 1 km in resistive basement.")
    print()
    print("  COMPUTED Cagniard apparent resistivity from the layered-earth")
    print("  recursion, starting from the half-space impedance sqrt(i omega mu0")
    print("  rho) and building upwards. Three sections:")
    sections = {
        "half-space 100 ohm m": [(100.0, 0.0)],
        "500 m cap 5 ohm m over 500 ohm m": [(5.0, 500.0), (500.0, 0.0)],
        "500 m cap 5 ohm m over 50 ohm m": [(5.0, 500.0), (50.0, 0.0)],
    }
    periods = (0.01, 0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0)
    header = "   T (s)     " + "".join(f"{name[:26]:>28s}" for name in sections)
    print(header)
    for t in periods:
        row = f"   {t:8.2f}"
        for name in sections:
            ra = mt_apparent_resistivity(sections[name], t)
            row += f"{ra:28.2f}"
        print(row)
    print("  The half-space column returns its own resistivity at every period,")
    print("  which is the check that the recursion is correct. The cap sections")
    print("  start at the cap resistivity (5 ohm m at 0.01 s), rise through the")
    print("  transition and approach the basement value only at the longest")
    print("  periods: the 500 ohm m case is still climbing at 100 s and reaches")
    print("  about 458 ohm m at 10 000 s. Two consequences follow, and both are")
    print("  practical. First, the *period range* needed to see the reservoir")
    print("  depends on the cap thickness and on the contrast, so a survey design")
    print("  cannot be copied between fields. Second, an apparent resistivity is")
    print("  not a true resistivity: at 1 s the 500 ohm m section reads 11 ohm m,")
    print("  and reading that number as the resistivity of the reservoir would be")
    print("  wrong by a factor of 45.")
    print()
    print("  The clay cap is the exploration key: hydrothermal alteration turns")
    print("  rock into clay, which is conductive, while the hot reservoir below is")
    print("  at least partly sealed and resistive. The property contrast that MT")
    print("  measures is therefore *electrical conductivity*; the temperature is")
    print("  inferred from the geology and a measured gradient, not measured by")
    print("  the electromagnetic method.")


def part_detectability() -> None:
    print()
    print("=" * 72)
    print("5. HOW DEEP A HOLE, AND HOW LARGE AN ANOMALY")
    print("=" * 72)
    print("  COMPUTED temperature excess from an anomalous heat flow, relative to")
    print("  a normal gradient: dT(z) = (q_anom - q_norm) z / k")
    q_norm = K_ROCK * GRADIENT
    print(f"  MODELLED normal q = {q_norm * 1000:.1f} mW/m^2, k = {K_ROCK} W/(m K)")
    print("   z (km)     dT for +10 mW/m^2   dT for +30 mW/m^2   dT for +60")
    for z_km in (0.5, 1.0, 2.0, 3.0):
        z = z_km * 1000.0
        row = f"   {z_km:5.1f}"
        for dq in (0.010, 0.030, 0.060):
            row += f"   {dq * z / K_ROCK:19.2f}"
        print(row)
    print("  Units are kelvin. A 30 mW/m^2 anomaly at 1 km is 12 K, which is")
    print("  measurable with a temperature log to about a tenth of a degree; a")
    print("  10 mW/m^2 anomaly at 500 m is 2 K, which is measurable only if the")
    print("  conductive column and the surface history are both known.")
    print()
    print("  COMPUTED required log precision at 500 m to resolve a +10 mW/m^2")
    dq = 0.010
    z = 500.0
    print(f"    anomaly, if the target is a {dq * z / K_ROCK:.2f} K step.")
    print("  That is the honest basis for stating a detection limit: not an")
    print("  instrument number, but a comparison between the temperature step the")
    print("  target produces and the uncertainty of the temperature model used to")
    print("  interpret the log.")


def main() -> None:
    assert abs(skin_depth(100.0, 1.0) - 503.0 * math.sqrt(100.0)) / 5030.0 < 0.01
    assert rayleigh_number(1000.0, 100.0) > RA_CRIT
    assert rayleigh_number(500.0, 50.0) < RA_CRIT
    for t in (1.0, 100.0):
        assert abs(mt_apparent_resistivity([(100.0, 0.0)], t) - 100.0) < 1e-6
    part_heat_flow()
    part_convection()
    part_heat_in_place()
    part_mt()
    part_detectability()
    print()
    print("All assertions passed.")


if __name__ == "__main__":
    main()
