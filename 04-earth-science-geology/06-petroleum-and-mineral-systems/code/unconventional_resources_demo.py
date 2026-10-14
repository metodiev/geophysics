"""Unconventional resources: shale gas, tight gas and gas hydrate.

Run:  .venv/bin/python unconventional_resources_demo.py
Requires: Python standard library only.

Companion to lesson 04-06-05.

The demo computes the *physics* of each play type and stops there. It does not
compute, state or imply any recovery factor, estimated ultimate recovery,
resource volume or reserve: those are engineering, economic and regulatory
quantities, they change with price and technology, and they are not geophysical.
Where a recovery factor would be needed it is left symbolic and its effect is
shown only as a sensitivity.

Parts:

1. Gassmann fluid substitution on a sandstone: bulk modulus, P- and S-wave
   velocity against water saturation, and the "fizz gas" effect.
2. Poisson's ratio and the Vp/Vs discriminator, computed from the same
   velocities.
3. A brittleness index from the elastic moduli, with its arbitrary bounds
   stated.
4. Gas-hydrate stability: the hydrostatic pressure profile, a *stated local
   linearisation* of the laboratory phase boundary, the intersection with a
   geotherm, and the sensitivity of the base of the stability zone to bottom-
   water temperature and to the geothermal gradient.
5. The bottom-simulating reflector as an acoustic-impedance contrast.
6. Tight gas: the Klinkenberg correction to a measured permeability, and the
   uniaxial-strain closure stress.
"""

import math

G = 9.81

K_MINERAL = 36.0e9      # [Pa] quartz bulk modulus (nominal)
MU_MINERAL = 44.0e9     # [Pa] quartz shear modulus (nominal)
K_WATER = 2.8e9         # [Pa] brine (nominal)
K_GAS = 0.05e9          # [Pa] methane at reservoir conditions (nominal)
RHO_MINERAL = 2650.0    # [kg/m^3]
RHO_WATER = 1050.0      # [kg/m^3]
RHO_GAS = 200.0         # [kg/m^3]

POROSITY = 0.30         # [-]
K_DRY = 8.0e9           # [Pa] MODELLED dry-frame bulk modulus
MU_DRY = 6.0e9          # [Pa] MODELLED dry-frame shear modulus (fluid
                        # independent in Gassmann's theory)

BI_E_BOUNDS = (10.0e9, 60.0e9)   # MODELLED convention for the index
BI_NU_BOUNDS = (0.40, 0.20)      # MODELLED convention for the index


def woods_fluid_modulus(sw: float) -> float:
    """Wood's harmonic average of water and gas bulk moduli."""
    if sw <= 0.0:
        return K_GAS
    return 1.0 / (sw / K_WATER + (1.0 - sw) / K_GAS)


def gassmann(phi: float, k_dry: float, k_fl: float) -> float:
    """Gassmann's saturated bulk modulus."""
    num = (1.0 - k_dry / K_MINERAL) ** 2
    den = phi / k_fl + (1.0 - phi) / K_MINERAL - k_dry / (K_MINERAL ** 2)
    return k_dry + num / den


def velocities(phi: float, k_sat: float, mu: float, rho: float
               ) -> tuple[float, float]:
    vp = math.sqrt((k_sat + 4.0 * mu / 3.0) / rho)
    vs = math.sqrt(mu / rho)
    return vp, vs


def poisson(vp: float, vs: float) -> float:
    return (vp * vp - 2.0 * vs * vs) / (2.0 * (vp * vp - vs * vs))


def young(vp: float, vs: float, rho: float) -> float:
    return rho * vs * vs * (3.0 * vp * vp - 4.0 * vs * vs) / (vp * vp - vs * vs)


def part_gassmann() -> None:
    print("=" * 72)
    print("1. GASSMANN FLUID SUBSTITUTION AND THE FIZZ-GAS EFFECT")
    print("=" * 72)
    print("  MODELLED inputs:")
    print(f"    K_mineral = {K_MINERAL / 1e9:.0f} GPa, K_water = "
          f"{K_WATER / 1e9:.2f} GPa, K_gas = {K_GAS / 1e9:.3f} GPa")
    print(f"    K_dry = {K_DRY / 1e9:.0f} GPa, mu_dry = {MU_DRY / 1e9:.0f} GPa, "
          f"porosity = {POROSITY}")
    print("  COMPUTED Gassmann's equation relates the saturated modulus to the")
    print("  dry frame, the mineral and the fluid; mu is taken as fluid")
    print("  independent, which is the central assumption of the theory.")
    print()
    print("   S_w    K_fl (GPa)  K_sat (GPa)  rho    vp      vs     Vp/Vs   nu")
    for sw in (1.0, 0.95, 0.90, 0.80, 0.60, 0.40, 0.20, 0.0):
        k_fl = woods_fluid_modulus(sw)
        k_sat = gassmann(POROSITY, K_DRY, k_fl)
        rho = (POROSITY * (sw * RHO_WATER + (1.0 - sw) * RHO_GAS)
               + (1.0 - POROSITY) * RHO_MINERAL)
        vp, vs = velocities(POROSITY, k_sat, MU_DRY, rho)
        print(f"   {sw:4.2f}  {k_fl / 1e9:10.4f}  {k_sat / 1e9:11.4f}  "
              f"{rho:6.0f}  {vp:6.0f}  {vs:5.0f}  {vp / vs:6.3f}  "
              f"{poisson(vp, vs):5.3f}")
    print()
    k_fl_90 = woods_fluid_modulus(0.90)
    k_90 = gassmann(POROSITY, K_DRY, k_fl_90)
    rho_90 = (POROSITY * (0.90 * RHO_WATER + 0.10 * RHO_GAS)
              + (1.0 - POROSITY) * RHO_MINERAL)
    vp_90, vs_90 = velocities(POROSITY, k_90, MU_DRY, rho_90)
    k_1 = gassmann(POROSITY, K_DRY, K_WATER)
    rho_1 = POROSITY * RHO_WATER + (1.0 - POROSITY) * RHO_MINERAL
    vp_1, vs_1 = velocities(POROSITY, k_1, MU_DRY, rho_1)
    k_0 = gassmann(POROSITY, K_DRY, K_GAS)
    rho_0 = POROSITY * RHO_GAS + (1.0 - POROSITY) * RHO_MINERAL
    vp_0, vs_0 = velocities(POROSITY, k_0, MU_DRY, rho_0)
    print("  COMPUTED the three cases that define the problem:")
    print(f"    fully brine-saturated: vp = {vp_1:.0f} m/s, vs = {vs_1:.0f} m/s")
    print(f"    90 per cent brine, 10 per cent free gas: vp = {vp_90:.0f} m/s "
          f"({100 * (vp_90 - vp_1) / vp_1:+.1f} per cent), vs = {vs_90:.0f} m/s "
          f"({100 * (vs_90 - vs_1) / vs_1:+.1f} per cent)")
    print(f"    fully gas-saturated: vp = {vp_0:.0f} m/s "
          f"({100 * (vp_0 - vp_1) / vp_1:+.1f} per cent), vs = {vs_0:.0f} m/s "
          f"({100 * (vs_0 - vs_1) / vs_1:+.1f} per cent)")
    print("  The P-wave velocity at 10 per cent gas saturation is *lower* than")
    print("  at 100 per cent, because the fluid modulus collapses as soon as any")
    print("  free gas appears while the density is still nearly that of brine.")
    print("  That is the fizz-gas effect, and it is the reason a seismic")
    print("  amplitude anomaly cannot be converted into a saturation without")
    print("  additional information: a small amount of gas and a large amount")
    print("  look similar in P-wave data, and the S-wave velocity is the")
    print("  discriminator because it is almost fluid independent.")


def part_elastic() -> None:
    print()
    print("=" * 72)
    print("2. ELASTIC MODULI, POISSON'S RATIO AND BRITTLENESS")
    print("=" * 72)
    print("  COMPUTED E = rho vs^2 (3 vp^2 - 4 vs^2)/(vp^2 - vs^2),")
    print("           nu = (vp^2 - 2 vs^2)/(2 (vp^2 - vs^2))")
    print("  MODELLED two shale compositions as input velocities:")
    cases = {
        "quartz-rich (brittle)": (2650.0, 3600.0, 2100.0),
        "clay-rich (ductile)": (2500.0, 3100.0, 1600.0),
    }
    for name, (rho, vp, vs) in cases.items():
        e = young(vp, vs, rho)
        nu = poisson(vp, vs)
        print(f"    {name:24s} rho = {rho:.0f}, vp = {vp:.0f}, vs = {vs:.0f}: "
              f"E = {e / 1e9:5.1f} GPa, nu = {nu:.3f}")
    print()
    print("  COMPUTED brittleness index as the mean of two normalised moduli,")
    print("  with the bounds below declared as a CONVENTION rather than derived:")
    print(f"    BI = [ (E - {BI_E_BOUNDS[0] / 1e9:.0f} GPa)/(50 GPa) + "
          f"(0.40 - nu)/(0.20) ] / 2")
    print("  The bounds are arbitrary: another paper would choose different ones")
    print("  and get a different index from the same rock. The index is included")
    print("  because it is used commercially, and labelled because it is not a")
    print("  physical property.")
    for name, (rho, vp, vs) in cases.items():
        e = young(vp, vs, rho)
        nu = poisson(vp, vs)
        bi_e = (e - BI_E_BOUNDS[0]) / (BI_E_BOUNDS[1] - BI_E_BOUNDS[0])
        bi_n = (BI_NU_BOUNDS[0] - nu) / (BI_NU_BOUNDS[0] - BI_NU_BOUNDS[1])
        bi_e = min(max(bi_e, 0.0), 1.0)
        bi_n = min(max(bi_n, 0.0), 1.0)
        print(f"    {name:24s}: BI_E = {bi_e:.3f}, BI_nu = {bi_n:.3f}, "
              f"BI = {(bi_e + bi_n) / 2.0:.3f}")
    print("  What is *physical* here is the pair (E, nu) and the velocities they")
    print("  come from. The index is a rescaling of that pair onto an arbitrary")
    print("  0-1 scale, and it inherits the arbitrariness.")


def part_hydrate() -> None:
    print()
    print("=" * 72)
    print("3. GAS-HYDRATE STABILITY FIELD")
    print("=" * 72)
    rho_sw, g = 1030.0, 9.81
    water_depth = 1500.0
    t_bottom = 2.0
    grad = 0.030             # [K/m] 30 K/km in the sediment
    p_floor = rho_sw * g * water_depth / 1e6
    print(f"  MODELLED water depth {water_depth:.0f} m, bottom-water temperature "
          f"{t_bottom:.1f} degC,")
    print(f"           geothermal gradient {grad * 1000:.1f} K/km, "
          f"sea-water density {rho_sw:.0f} kg/m^3")
    print(f"  COMPUTED hydrostatic pressure at the seafloor "
          f"P = rho g z = {p_floor:.3f} MPa")
    dp_dz = rho_sw * g / 1e6
    print(f"  COMPUTED pressure gradient in the sediment = {dp_dz:.6f} MPa/m")

    # A LOCAL LINEARISATION of the laboratory phase boundary, stated as such.
    t_ref, p_ref, beta = 12.0, p_floor, 0.90     # [degC], [MPa], [degC/MPa]
    print()
    print("  MODELLED phase boundary, used only as a LOCAL LINEARISATION to")
    print("  demonstrate the geometry:")
    print(f"    T_stable(P) = {t_ref:.1f} degC + {beta:.2f} (P - "
          f"{p_ref:.3f} MPa)")
    print("  A real assessment takes this boundary from a current laboratory")
    print("  compilation of methane-hydrate dissociation data; the two constants")
    print("  above are not a measurement and are not offered as one.")
    print()
    slope_boundary = beta * dp_dz          # [K/m]
    slope_geo = grad
    print(f"  COMPUTED the boundary rises at {slope_boundary * 1000:.2f} K/km in")
    print(f"  the T-z plane, while the geotherm rises at {slope_geo * 1000:.1f}"
          f" K/km.")
    print(f"  The stability zone exists only because the geotherm is steeper:")
    print(f"  the difference, {(slope_geo - slope_boundary) * 1000:.2f} K/km, "
          f"sets the depth.")

    def base_depth(t_bw: float, g_geo: float) -> float:
        rhs = (t_ref - t_bw) + beta * 0.0
        denom = g_geo - beta * dp_dz
        return rhs / denom

    h = base_depth(t_bottom, grad)
    print(f"  COMPUTED base of the stability zone at {h:.1f} m below the "
          f"seafloor")
    print(f"    = {water_depth + h:.0f} m below sea level, "
          f"T = {t_bottom + grad * h:.2f} degC, "
          f"P = {p_floor + dp_dz * h:.3f} MPa")
    assert 400.0 < h < 600.0
    print()
    print("  COMPUTED sensitivity, which is the whole of the resource question:")
    print("   bottom water (degC)   gradient (K/km)   base depth (m)")
    for t_bw, g_km in ((2.0, 25.0), (2.0, 30.0), (2.0, 40.0),
                       (4.0, 30.0), (6.0, 30.0)):
        hh = base_depth(t_bw, g_km / 1000.0)
        print(f"   {t_bw:19.1f}   {g_km:15.0f}   {hh:14.1f}")
    print("  A 2 K warming of the bottom water thins the stability zone sharply,")
    print("  and a warmer geotherm does the same. Both are quantities that a")
    print("  geophysical survey constrains only indirectly: the *depth* of the")
    print("  bottom-simulating reflector is the observable, and the temperature")
    print("  is the inference.")


def part_bsr() -> None:
    print()
    print("=" * 72)
    print("4. THE BOTTOM-SIMULATING REFLECTOR")
    print("=" * 72)
    print("  MODELLED nominal properties across the base of the stability zone:")
    above = (1950.0, 1900.0)     # hydrate-bearing sediment
    below = (1900.0, 1500.0)     # gas-bearing sediment (vp suppressed)
    print(f"    hydrate-bearing above: rho = {above[0]:.0f}, "
          f"vp = {above[1]:.0f}")
    print(f"    gas-bearing below:     rho = {below[0]:.0f}, "
          f"vp = {below[1]:.0f}")
    z1 = above[0] * above[1]
    z2 = below[0] * below[1]
    r = (z2 - z1) / (z2 + z1)
    print(f"  COMPUTED Z above = {z1 / 1e6:.3f} MRayl, below = "
          f"{z2 / 1e6:.3f} MRayl")
    print(f"  COMPUTED R = {r:+.4f}, a *negative* coefficient.")
    print("  The free gas below the stability zone lowers the velocity sharply,")
    print("  so the reflector is polarity-reversed relative to the seafloor and")
    print("  is a strong, continuous, bottom-simulating event. That is the")
    print("  geophysical signature: not a measurement of hydrate, but a")
    print("  measurement of the *base of the stability field*, which is a")
    print("  temperature-and-pressure surface and therefore a palaeoclimate and")
    print("  heat-flow proxy as much as a resource indicator.")
    print("  Note also what the section cannot show: hydrate itself has almost")
    print("  the same elastic properties as the sediment frame it fills, so the")
    print("  *top* of the stability zone is usually invisible and the internal")
    print("  hydrate concentration is not recoverable from the reflection alone.")


def part_tight_gas() -> None:
    print()
    print("=" * 72)
    print("5. TIGHT GAS: KLINKENBERG CORRECTION AND CLOSURE STRESS")
    print("=" * 72)
    print("  COMPUTED Klinkenberg: k_gas = k_liquid (1 + b/p), so a gas")
    print("  permeability measured at low pressure overestimates the liquid")
    print("  permeability. b is a MODELLED slip coefficient.")
    k_liquid = 1.0e-16       # [m^2] ~0.1 mD
    b_slip = 2.0e6           # [Pa] MODELLED Klinkenberg slip factor
    print(f"    MODELLED k_liquid = {k_liquid:.1e} m^2 "
          f"({k_liquid / 9.869233e-16:.2f} mD), b = {b_slip:.1e} Pa")
    print("     mean pressure (MPa)   k_gas (m^2)      k_gas/k_liquid")
    for p_mpa in (1.0, 2.0, 5.0, 10.0, 20.0):
        k_g = k_liquid * (1.0 + b_slip / (p_mpa * 1e6))
        print(f"     {p_mpa:19.1f}   {k_g:.4e}   {k_g / k_liquid:14.3f}")
    print("  The correction vanishes at high pressure, which is why the")
    print("  measurement protocol states the pressure: for these parameters the")
    print("  same rock reports about 2.7 times more permeability at 1 MPa than at")
    print("  20 MPa, and the difference is slip flow in the pore throats, not a")
    print("  change in the rock. The size of the effect is set by b, which is")
    print("  itself a MODELLED input and is rock specific.")
    print()
    print("  COMPUTED uniaxial-strain closure stress:")
    print("    sigma_h = [nu/(1 - nu)] (sigma_v - alpha p) + alpha p")
    sigma_v = 40.0e6          # [Pa] at ~1.6 km, nominal
    alpha = 0.8               # Biot coefficient (nominal)
    p_pore = 16.0e6           # [Pa] pore pressure (nominal)
    print(f"    MODELLED sigma_v = {sigma_v / 1e6:.0f} MPa, "
          f"alpha = {alpha}, p = {p_pore / 1e6:.0f} MPa")
    print("     nu     sigma_h (MPa)   horizontal stress ratio")
    for nu in (0.15, 0.20, 0.25, 0.30, 0.35):
        sh = nu / (1.0 - nu) * (sigma_v - alpha * p_pore) + alpha * p_pore
        print(f"     {nu:4.2f}   {sh / 1e6:13.2f}   {sh / sigma_v:19.3f}")
    print("  The closure stress is what keeps a hydraulic fracture open, so it")
    print("  is the single most important elastic quantity in a stimulation")
    print("  design; and it is computed here from a *model of the stress state*,")
    print("  not measured. Only a leak-off test or a fracture calibration")
    print("  measures it.")
    print()
    print("  FINALLY, the boundary of what this demo computes. The permeability,")
    print("  the moduli, the stress state and the hydrate stability field are")
    print("  physical. How much gas a well delivers, how much of it a field")
    print("  recovers, and whether the project is viable are engineering and")
    print("  economic questions. No recovery factor, resource volume or reserve")
    print("  is stated anywhere in this script, and none should be inferred from")
    print("  it.")


def main() -> None:
    k1 = gassmann(POROSITY, K_DRY, K_WATER)
    k0 = gassmann(POROSITY, K_DRY, K_GAS)
    assert k1 > k0
    rho1 = POROSITY * RHO_WATER + (1 - POROSITY) * RHO_MINERAL
    rho0 = POROSITY * RHO_GAS + (1 - POROSITY) * RHO_MINERAL
    vp1, vs1 = velocities(POROSITY, k1, MU_DRY, rho1)
    vp0, vs0 = velocities(POROSITY, k0, MU_DRY, rho0)
    assert vp1 > vp0
    assert abs(vs1 - vs0) / vs1 < 0.10, "vs changes only through density"
    part_gassmann()
    part_elastic()
    part_hydrate()
    part_bsr()
    part_tight_gas()
    print()
    print("All assertions passed.")


if __name__ == "__main__":
    main()
