"""Glacial and periglacial landforms and sediments.

Run:  .venv/bin/python glacial_landforms_demo.py
Requires: Python standard library only.

Companion to lesson 04-05-02.

The three number categories are separated in the output:

* COMPUTED  -- from a formula stated in the lesson: driving stress, internal
               deformation velocity, the perfect-plasticity thickness, Airy
               isostatic depression, the relaxation time of a viscous half
               space, reflection coefficients, GPR travel time and the Stefan
               active-layer depth.
* MODELLED  -- a rheological parameter of a *particular* ice mass or substrate:
               the flow-law coefficient A, the flow-law exponent n, the
               activation energy Q, the mantle viscosity, the ice and sediment
               properties. These are parameterisations; the values quoted are
               nominal and a real study calibrates them.
* DERIVED   -- a combination of the two.

Parts:

1. Driving stress and internal deformation velocity from Glen's flow law.
   Temperature sensitivity of A, and the weak dependence of velocity on
   temperature through the exponent n.
2. Geometry from perfect plasticity: the ice thickness a stated yield stress
   permits on a given surface slope.
3. Basal sliding as an explicitly flagged sensitivity on the deformation rate.
4. Isostatic response: Airy depression under an ice load, and the relaxation
   time of a viscous half space for a given wavelength.
5. The geophysical signature of glacial sediment: acoustic-impedance reflection
   coefficients for till over bedrock and for a water-saturated versus dry
   layer.
6. GPR in ice: velocity, two-way travel time and vertical resolution.
7. Periglacial: the Stefan active-layer depth and the frost-heave magnitude of
   the water-ice volume change.
"""

import math

# --------------------------------------------------------------------------
# MODELLED parameters
# --------------------------------------------------------------------------

RHO_ICE = 917.0          # [kg/m^3] density of ice (near 0 degC, low pressure)
G = 9.81                 # [m/s^2]
N_GLEN = 3.0             # Glen's flow-law exponent (dimensionless)
A_GLEN_0C = 2.4e-24      # [Pa^-3 s^-1] flow-law coefficient at 0 degC (nominal)
Q_CREEP = 60.0e3         # [J/mol] activation energy for creep (nominal)
R_GAS = 8.314462618      # [J/(mol K)]
YEAR = 3.15576e7         # [s]

TAU_YIELD = 1.0e5        # [Pa] plastic yield stress, the perfect-plasticity model
RHO_MANTLE = 3300.0      # [kg/m^3] effective density of the displaced mantle
ETA_MANTLE = 1.0e21      # [Pa s] upper-mantle viscosity (nominal, range 1e20-1e21)
EPS_ICE = 3.17           # relative permittivity of cold ice (nominal 3.1-3.2)
C_LIGHT = 2.99792458e8   # [m/s]

LATENT_FUSION = 334.0e3  # [J/kg] latent heat of fusion of water
RHO_WATER = 1000.0       # [kg/m^3]
K_FROZEN = 1.5           # [W/(m K)] thermal conductivity of frozen ground (nominal)
FREEZE_MONTHS = 6.0      # [months]


def glen_a(temperature_c: float) -> float:
    """Arrhenius temperature dependence of the flow-law coefficient."""
    t1 = 273.15
    t2 = temperature_c + 273.15
    return A_GLEN_0C * math.exp(Q_CREEP / R_GAS * (1.0 / t1 - 1.0 / t2))


def ice_flow() -> None:
    print("=" * 72)
    print("1. ICE FLOW -- driving stress and deformation velocity")
    print("=" * 72)
    h = 1000.0                     # [m] ice thickness
    alpha = 1.0                    # [deg] surface slope
    sin_a = math.sin(math.radians(alpha))
    tau_b = RHO_ICE * G * h * sin_a
    u_d = 2.0 * A_GLEN_0C / (N_GLEN + 1.0) * tau_b ** N_GLEN * h
    print(f"  MODELLED H = {h:.0f} m, surface slope = {alpha:.1f} deg, "
          f"A(0 degC) = {A_GLEN_0C:.1e} Pa^-3 s^-1, n = {N_GLEN:.0f}")
    print(f"  COMPUTED driving stress tau_b = rho g H sin(alpha) = {tau_b:.4e} Pa")
    print(f"  COMPUTED depth-averaged deformation velocity")
    print(f"    u_d = 2A/(n+1) tau_b^n H = {u_d:.4e} m/s = "
          f"{u_d * YEAR:.2f} m/yr")
    print(f"  COMPUTED basal shear strain rate A tau_b^n = "
          f"{A_GLEN_0C * tau_b ** N_GLEN:.4e} s^-1")

    print()
    print("  COMPUTED temperature sensitivity, A(T) = A0 exp(Q/R (1/T0 - 1/T))")
    for temp in (0.0, -10.0, -20.0, -30.0):
        a = glen_a(temp)
        u = 2.0 * a / (N_GLEN + 1.0) * tau_b ** N_GLEN * h
        print(f"    T = {temp:6.1f} degC: A = {a:.3e} Pa^-3 s^-1 "
              f"({100 * a / A_GLEN_0C:5.1f} per cent of A(0)), "
              f"u_d = {u * YEAR:8.3f} m/yr")
    print("  Velocity is linear in A, so a 10 K cooling cuts this glacier's")
    print("  deformation rate to about a third. That is why a polythermal or")
    print("  cold-based margin moves metres per year while a temperate tongue")
    print("  moves hundreds.")

    print()
    print("  COMPUTED strain-rate sensitivity: u varies as tau_b^n with n = 3,")
    print("  so a 10 per cent error in thickness is a 33 per cent velocity error.")
    for factor in (0.9, 1.1):
        hh = h * factor
        t = RHO_ICE * G * hh * sin_a
        u = 2.0 * A_GLEN_0C / (N_GLEN + 1.0) * t ** N_GLEN * hh
        print(f"    H x {factor}: u_d = {u * YEAR:8.2f} m/yr "
              f"(ratio to reference {u / u_d:.3f})")


def perfect_plasticity() -> None:
    print()
    print("=" * 72)
    print("2. PERFECT-PLASTICITY GEOMETRY")
    print("=" * 72)
    print(f"  MODELLED yield stress tau_y = {TAU_YIELD:.1e} Pa")
    print("  COMPUTED H(slope) = tau_y / (rho g sin alpha)")
    for alpha in (0.25, 0.5, 1.0, 2.0, 5.0):
        s = math.sin(math.radians(alpha))
        h = TAU_YIELD / (RHO_ICE * G * s)
        print(f"    slope {alpha:5.2f} deg: H = {h:8.1f} m, "
              f"tau_b = {RHO_ICE * G * h * s:.1e} Pa")
    print("  The thickness is inversely proportional to the sine of the surface")
    print("  slope, which is why an ice sheet is kilometres thick on a plain and")
    print("  tens of metres thick on a steep valley wall.")


def sliding_sensitivity() -> None:
    print()
    print("=" * 72)
    print("3. BASAL SLIDING -- an explicitly flagged sensitivity")
    print("=" * 72)
    h, alpha = 1000.0, 1.0
    sin_a = math.sin(math.radians(alpha))
    tau_b = RHO_ICE * G * h * sin_a
    u_d = 2.0 * A_GLEN_0C / (N_GLEN + 1.0) * tau_b ** N_GLEN * h
    print("  MODELLED sliding multiplier f, so that u = u_d (1 + f). The sliding")
    print("  law and its coefficient are not derived here; f is a declared")
    print("  parameter, reported so that its effect on the geomorphology is")
    print("  visible. A real value comes from a sliding law plus an effective")
    print("  pressure, both of which are model choices.")
    for f in (0.0, 1.0, 5.0, 20.0):
        u = u_d * (1.0 + f)
        print(f"    f = {f:5.1f}: u = {u * YEAR:9.2f} m/yr, "
              f"transit time over 100 km = {1.0e5 / (u * YEAR) / 1e3:6.2f} kyr")
    print("  Geomorphic consequence: sliding fraction, not thickness, sets the")
    print("  flux (ice flux q = u H), and it is the flux that carves the trough.")


def isostasy() -> None:
    print()
    print("=" * 72)
    print("4. ISOSTATIC RESPONSE TO AN ICE LOAD")
    print("=" * 72)
    print(f"  MODELLED rho_ice = {RHO_ICE} kg/m^3, "
          f"rho_mantle(displaced) = {RHO_MANTLE} kg/m^3")
    for h in (1000.0, 2000.0, 3000.0):
        dep = RHO_ICE / RHO_MANTLE * h
        print(f"    ice thickness {h:6.0f} m: Airy depression = "
              f"{dep:7.2f} m ({100 * dep / h:.2f} per cent of the load)")
    print("  COMPUTED The ratio is density-only; it is exact for local, thin,")
    print("  uncompensated crust, and it ignores flexural rigidity.")

    print()
    print("  COMPUTED relaxation time of a viscous half space under a load of")
    print("  wavelength lambda: tau = 2 eta k / (rho g) with k = 2 pi / lambda")
    for lam_km in (100.0, 1000.0, 3000.0):
        k = 2.0 * math.pi / (lam_km * 1e3)
        tau = 2.0 * ETA_MANTLE * k / (RHO_MANTLE * G)
        print(f"    lambda = {lam_km:6.0f} km: tau = {tau:.4e} s = "
              f"{tau / YEAR:9.0f} yr = {tau / YEAR / 1e3:6.2f} kyr")
    print(f"  MODELLED eta = {ETA_MANTLE:.0e} Pa s; tau is linear in eta, so an")
    print("  order of magnitude in viscosity is an order of magnitude in tau.")
    print("  This is why the Fennoscandian and Laurentide loads are still")
    print("  relaxing: the load was removed in thousands of years and the")
    print("  response takes tens of thousands.")


def sediment_signature() -> None:
    print()
    print("=" * 72)
    print("5. GEOPHYSICAL SIGNATURE OF GLACIAL SEDIMENT")
    print("=" * 72)
    print("  MODELLED nominal properties (ranges, not measurements of a site):")
    mats = {
        # name: (density kg/m^3, P-wave velocity m/s)
        "till (saturated, soft)": (2000.0, 1600.0),
        "till (compacted, dry)": (1900.0, 900.0),
        "glaciofluvial sand/gravel": (2050.0, 1700.0),
        "shale bedrock": (2400.0, 2900.0),
        "limestone bedrock": (2600.0, 4500.0),
        "granite bedrock": (2650.0, 5200.0),
        "ice": (917.0, 3800.0),
    }
    for name, (rho, vp) in mats.items():
        print(f"    {name:26s} rho = {rho:6.0f} kg/m^3, vp = {vp:5.0f} m/s, "
              f"Z = {rho * vp / 1e6:8.3f} MRayl")
    print()
    print("  COMPUTED normal-incidence reflection coefficient R = (Z2 - Z1)/(Z2 + Z1)")
    z_till = 2000.0 * 1600.0
    for name in ("shale bedrock", "limestone bedrock", "granite bedrock", "ice"):
        rho, vp = mats[name]
        z2 = rho * vp
        r = (z2 - z_till) / (z2 + z_till)
        print(f"    till over {name:20s}: R = {r:+.4f}  "
              f"({100 * abs(r):5.2f} per cent of the amplitude)")
    print("  Sediment over bedrock is not a subtle contact: R is 0.37 to 0.62")
    print("  here, because both the density and the velocity step up. That is")
    print("  why the sediment-bedrock interface is the easiest horizon in a")
    print("  shallow survey, and why a refraction or surface-wave survey can")
    print("  map its depth with a travel-time curve alone.")
    print()
    rho_d, vp_d = mats["till (compacted, dry)"]
    rho_w, vp_w = mats["till (saturated, soft)"]
    r = (rho_w * vp_w - rho_d * vp_d) / (rho_w * vp_w + rho_d * vp_d)
    print(f"  COMPUTED the same till dry vs saturated, a pure fluid effect:")
    print(f"    R = {r:+.4f} for the water table inside the till.")
    print("  R near 0.3 from saturation alone is why the water table is the")
    print("  strongest shallow seismic and GPR reflector in an aquifer.")


def gpr_in_ice() -> None:
    print()
    print("=" * 72)
    print("6. GPR IN ICE")
    print("=" * 72)
    v = C_LIGHT / math.sqrt(EPS_ICE)
    print(f"  MODELLED relative permittivity of cold ice = {EPS_ICE}")
    print(f"  COMPUTED v = c / sqrt(eps) = {v:.4e} m/s "
          f"= {v / 1e8:.4f} x 10^8 m/s")
    for depth in (100.0, 500.0, 2000.0):
        t2 = 2.0 * depth / v
        print(f"    depth {depth:7.0f} m: two-way travel time = {t2 * 1e6:8.3f} us")
    lam = v / 100e6
    print(f"  COMPUTED at 100 MHz the wavelength is {lam:.3f} m, so the")
    print(f"  quarter-wavelength vertical resolution is about {lam / 4:.3f} m.")
    print("  A 2000 m ice sheet from the surface is therefore not a problem for")
    print("  travel time or attenuation, but a 3000 m one strains the record")
    print("  length and the gain range instead.")


def periglacial() -> None:
    print()
    print("=" * 72)
    print("7. PERIGLACIAL -- active layer and frost heave")
    print("=" * 72)
    dt_k = 15.0
    t = FREEZE_MONTHS * YEAR / 12.0
    x = math.sqrt(2.0 * K_FROZEN * dt_k * t / (LATENT_FUSION * RHO_WATER))
    print(f"  MODELLED k = {K_FROZEN} W/(m K), surface offset dT = {dt_k} K,")
    print(f"           latent heat L = {LATENT_FUSION:.0e} J/kg, "
          f"freezing season = {FREEZE_MONTHS} months")
    print(f"  COMPUTED Stefan depth X = sqrt(2 k dT t / (L rho_w)) = {x:.4f} m")
    print("  The Stefan solution assumes latent heat dominates, a mean constant")
    print("  thermal conductivity and a step surface temperature; it over-")
    print("  predicts where the soil is dry or the winter oscillates.")
    print()
    print("  COMPUTED sensitivity to the season length and the surface offset:")
    for months in (4.0, 6.0, 8.0):
        xx = math.sqrt(2.0 * K_FROZEN * dt_k * months * YEAR / 12.0
                       / (LATENT_FUSION * RHO_WATER))
        print(f"    {months:4.1f} months: X = {xx:.4f} m")
    for dtemp in (10.0, 15.0, 25.0):
        xx = math.sqrt(2.0 * K_FROZEN * dtemp * t / (LATENT_FUSION * RHO_WATER))
        print(f"    dT = {dtemp:5.1f} K: X = {xx:.4f} m")
    print()
    print("  COMPUTED frost heave from the 9 per cent volume change of water:")
    for thickness in (0.30, 0.60, 1.20):
        print(f"    a {thickness:.2f} m water-saturated layer freezing in place "
              f"would rise {0.09 * thickness * 1000:.1f} mm")
    print("  The observed heave of a real soil is usually smaller than this")
    print("  because water drains and refreezes rather than freezing in place;")
    print("  the calculation is an upper bound and is labelled as one.")


def main() -> None:
    assert abs(glen_a(0.0) - A_GLEN_0C) < 1e-30
    assert glen_a(-10.0) < glen_a(0.0)
    ice_flow()
    perfect_plasticity()
    sliding_sensitivity()
    isostasy()
    sediment_signature()
    gpr_in_ice()
    periglacial()
    print()
    print("All assertions passed.")


if __name__ == "__main__":
    main()
