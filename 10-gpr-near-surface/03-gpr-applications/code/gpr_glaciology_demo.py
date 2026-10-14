#!/usr/bin/env python3
"""GPR glaciology: ice and firn permittivity, bed and internal reflections,
resolution, attenuation and the depth conversion of two-way times.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_glaciology_demo.py

All models and data in this module are SYNTHETIC.  The ice thickness, firn
density profile, attenuation coefficients, ages and interface properties are
chosen teaching values, not measurements of any glacier.  Physical constants
and standard material permittivities are labelled as such.

Contents
--------
1. Firn density to permittivity and speed (CRIM on an ice/air mixture); the
   depth error introduced by treating firn as ice.
2. Two-way time to the bed and the depth conversion against assumed eps_r.
3. Bed reflection coefficients, with the air/ice surface echo as a calibrated
   in-situ amplitude reference.
4. Vertical resolution lam/4 at three sounding frequencies.
5. Attenuation in cold ice and its temperature dependence: the 60 dB depth.
6. A bed point diffractor: hyperbola geometry, the single-velocity fit bias
   introduced by the firn layer, and the migration-collapse depth.
7. Internal horizons as isochrones: layer thickness, accumulation rate, and the
   velocity sensitivity of both.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_M_NS = 0.299792458        # speed of light in vacuum, m/ns (exact)
EPS_ICE = 3.17              # relative permittivity of cold ice (standard value)
EPS_AIR = 1.0               # air
RHO_ICE = 917.0             # density of ice, kg/m^3 (standard value)
R_GAS = 8.314462618         # J/(mol K) (exact)
T0_K = 273.15               # 0 C in kelvin (exact conversion)
H_BED_M = 800.0             # SYNTHETIC ice thickness of the teaching model
H_FIRN_M = 20.0             # SYNTHETIC firn layer thickness
RHO_FIRN = 500.0            # SYNTHETIC firn density, kg/m^3


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def crim_ice_air(rho_kg_m3):
    """Permittivity of a firn/ice mixture: CRIM with an air pore fraction."""
    phi = 1.0 - rho_kg_m3 / RHO_ICE
    n = (1.0 - phi) * np.sqrt(EPS_ICE) + phi * np.sqrt(EPS_AIR)
    return n ** 2


def v_of_eps(eps):
    """Low-loss phase speed in m/ns."""
    return C_M_NS / np.sqrt(eps)


def reflection_coeff(eps1, eps2):
    """Normal-incidence reflection coefficient with eta = Z0/sqrt(eps_r)."""
    return (np.sqrt(eps1) - np.sqrt(eps2)) / (np.sqrt(eps1) + np.sqrt(eps2))


def two_way_ns(depth_m, v_m_ns):
    return 2.0 * depth_m / v_m_ns


def vertical_two_way(z_m, v_firn, v_ice, h_firn=H_FIRN_M):
    """Zero-offset two-way time through a firn layer over ice, in ns."""
    if z_m <= h_firn:
        return 2.0 * z_m / v_firn
    return 2.0 * h_firn / v_firn + 2.0 * (z_m - h_firn) / v_ice


def two_layer_time(x_m, z_m, v_firn, v_ice, h_firn=H_FIRN_M):
    """Two-way time at offset x to a diffractor at depth z below the surface.

    The ray is refracted at the firn/ice contact; the take-off parameter is
    found by scanning the horizontal slowness, so the check is independent of
    any ray-tracing library.  Valid for z > h_firn.
    """
    p = np.linspace(1e-9, 0.999999 / max(v_firn, v_ice), 400000)
    one_way = (h_firn / (v_firn * np.sqrt(1.0 - (p * v_firn) ** 2))
               + (z_m - h_firn) / (v_ice * np.sqrt(1.0 - (p * v_ice) ** 2)))
    t = 2.0 * one_way
    x = (h_firn * p * v_firn / np.sqrt(1.0 - (p * v_firn) ** 2)
         + (z_m - h_firn) * p * v_ice / np.sqrt(1.0 - (p * v_ice) ** 2))
    return float(np.interp(abs(x_m), x, t))


def alpha_db_m(temp_c, alpha0_db_m=0.02, e_act=6.0e4):
    """SYNTHETIC teaching model of englacial absorption.

    alpha0_db_m is the chosen one-way attenuation at -20 C and e_act the chosen
    activation energy (J/mol) of an Arrhenius temperature dependence.  Neither
    is a measured value; the FORM is the standard one used for ice.
    """
    t_k = temp_c + T0_K
    ref = -20.0 + T0_K
    return alpha0_db_m * np.exp(-e_act / R_GAS * (1.0 / t_k - 1.0 / ref))


def invert_vertical(t_ns, v_firn, v_ice, z_max=2000.0):
    """Depth whose vertical two-way time equals t_ns (firn + ice model)."""
    z = np.linspace(1.0, z_max, 4000)
    tt = np.array([vertical_two_way(zi, v_firn, v_ice) for zi in z])
    return float(np.interp(t_ns, tt, z))


def main():
    section("1. Firn density to permittivity and speed (CRIM, ice + air)")
    print(f"ice eps_r = {EPS_ICE:.2f} (standard value), ice density "
          f"{RHO_ICE:.0f} kg/m^3 (standard value)")
    print("  rho(kg/m3)  pore fraction  eps_r    v (m/ns)")
    for rho in (400.0, 500.0, 600.0, 700.0, 800.0, 900.0, RHO_ICE):
        e = crim_ice_air(rho)
        print(f"  {rho:10.0f}  {1.0 - rho / RHO_ICE:13.3f}  {e:6.3f}   "
              f"{v_of_eps(e):8.4f}")
    v_firn = v_of_eps(crim_ice_air(RHO_FIRN))
    v_ice = v_of_eps(EPS_ICE)
    print(f"\n  a {RHO_FIRN:.0f} kg/m^3 firn has v = {v_firn:.4f} m/ns against "
          f"ice at {v_ice:.4f} m/ns: {v_firn / v_ice:.3f} times faster.")
    t_layered = two_way_ns(H_FIRN_M, v_firn) + two_way_ns(100.0 - H_FIRN_M, v_ice)
    t_uniform = two_way_ns(100.0, v_ice)
    print(f"  100 m column ({H_FIRN_M:.0f} m firn over {100 - H_FIRN_M:.0f} m ice): "
          f"two-way {t_layered:.1f} ns against {t_uniform:.1f} ns for pure ice")
    print(f"  converting {t_layered:.1f} ns as if all ice gives "
          f"{t_layered * v_ice / 2.0:.2f} m where the truth is 100.00 m "
          f"({t_layered * v_ice / 2.0 - 100.0:+.2f} m)")

    section("2. Two-way time to the bed and the depth conversion")
    t_bed = two_way_ns(H_BED_M, v_ice)
    print(f"SYNTHETIC ice thickness {H_BED_M:.0f} m, v_ice = {v_ice:.4f} m/ns")
    print(f"  two-way time to the bed: {t_bed:.2f} ns = {t_bed / 1000:.3f} us")
    print("  assumed eps_r   v (m/ns)   depth from that time (m)   error (m)")
    for eps in (3.00, 3.10, EPS_ICE, 3.30, 3.40):
        v = v_of_eps(eps)
        d = t_bed * v / 2.0
        print(f"  {eps:13.2f}   {v:8.4f}   {d:23.2f}   {d - H_BED_M:+9.2f}")
    print("\n  dH/H = -delta eps/(2 eps) exactly, so a +1% error in eps_r gives")
    print(f"  {(1.0 / np.sqrt(1.01) - 1.0) * 100:+.2f}% in depth, i.e. "
          f"{abs((1.0 / np.sqrt(1.01) - 1.0) * H_BED_M):.2f} m here.")
    # depth budget: uncertain eps_ice and an uncertain pick
    n = 20000
    eps_draw = EPS_ICE * (1.0 + 0.02 * RNG.standard_normal(n))
    t_draw = t_bed + RNG.normal(0.0, 1.0, n)          # ns pick error (SYNTHETIC)
    z_draw = v_of_eps(np.clip(eps_draw, 1.01, None)) * t_draw / 2.0
    print(f"  depth budget (2% eps_r, 1.0 ns pick): mean {z_draw.mean():.2f} m, "
          f"standard deviation {z_draw.std():.2f} m")
    print(f"    eps_r alone: {np.std(v_of_eps(eps_draw) * t_bed / 2.0):.2f} m; "
          f"pick alone: {np.std(v_ice * t_draw / 2.0):.2f} m")

    section("3. Bed reflections, referenced to the surface echo")
    r_surf = reflection_coeff(EPS_AIR, EPS_ICE)
    print(f"  air/ice surface echo: R = {r_surf:+.4f} "
          f"({20 * np.log10(abs(r_surf)):.1f} dB).  Because eps_ice is lower")
    print("  than that of almost every bed material (only air and very dry snow")
    print("  are lower), every bed coefficient below shares its SIGN; the")
    print("  discriminator is the calibrated AMPLITUDE, not the polarity.")
    print("  bed material            eps_r    R        |R|/|R_surf|   dB vs surface")
    for name, eps in (("subglacial water", 80.1), ("water-saturated till", 25.0),
                      ("frozen sediment", 6.0), ("crystalline rock", 5.0),
                      ("very dry sediment", 2.5)):
        r = reflection_coeff(EPS_ICE, eps)
        print(f"  {name:22s} {eps:6.1f}  {r:+7.4f}  {abs(r) / abs(r_surf):13.2f}  "
              f"{20 * np.log10(abs(r) / abs(r_surf)):+14.1f}")
    print("\n  The surface echo is a usable amplitude reference because its")
    print("  coefficient is fixed by eps_ice, which is known to a few percent.")
    print("  That is what converts 'bright' from an adjective into a number.")

    section("4. Vertical resolution: the lam/4 criterion")
    print("  resolution in a medium improves as 1/sqrt(eps_r), because the speed")
    print("  and the wavelength shrink together.")
    print("  f (MHz)   lambda in ice (m)   lam/4 (m)   two-way time (ns)")
    for f_mhz in (5.0, 20.0, 100.0):
        lam = v_ice / (f_mhz * 1e-3)          # v in m/ns, f in MHz -> m
        print(f"  {f_mhz:7.0f}   {lam:16.2f}   {lam / 4:8.2f}   "
              f"{two_way_ns(lam / 4, v_ice):16.1f}")
    print("  A quarter wavelength is the conventional limit; a layer thinner")
    print("  than that is detected as an amplitude change, not as two echoes.")

    section("5. Attenuation in cold ice: the SYNTHETIC teaching model")
    print("  alpha(T) = alpha0 exp(-Ea/R (1/T - 1/T_ref)), with SYNTHETIC")
    print("  alpha0 = 0.020 dB/m at -20 C and SYNTHETIC Ea = 6.0e4 J/mol.")
    print("  T (C)   alpha (dB/m)   60 dB two-way depth (m)")
    for tc in (-40.0, -30.0, -20.0, -10.0, -5.0):
        a = alpha_db_m(tc)
        print(f"  {tc:5.1f}   {a:11.4f}   {60.0 / (2.0 * a):21.0f}")
    print(f"  The spread between -40 C and -5 C is a factor of "
          f"{alpha_db_m(-5.0) / alpha_db_m(-40.0):.1f} in absorption, which is")
    print("  why cold ice is transparent for kilometres while temperate ice is")
    print("  not.  The coefficient itself is a chosen teaching value.")

    section("6. A point diffractor: geometry and the firn bias")
    x = np.linspace(-500.0, 500.0, 9)
    t_hyper = 2.0 * np.sqrt(x ** 2 + H_BED_M ** 2) / v_ice
    print("  uniform-ice hyperbola over a deep diffractor at 800 m:")
    print("  offset x (m)   two-way time (ns)   lag behind the apex (ns)")
    for xi, ti in zip(x[::2], t_hyper[::2]):
        print(f"  {xi:12.0f}   {ti:17.2f}   {ti - t_hyper[4]:21.2f}")
    print("\n  Now the same fit for two diffractor depths, with a 20 m firn layer")
    print("  present.  The best single-velocity hyperbola is fitted to the exact")
    print("  two-layer times; v_fit is the velocity a field analyst would report.")
    print("  depth (m)   v_fit (m/ns)   bias vs ice   max residual (ns)   "
          "depth from fit (m)")
    for z in (100.0, 400.0, H_BED_M):
        t_exact = np.array([two_layer_time(xi, z, v_firn, v_ice) for xi in x])
        a = 2.0 * np.sqrt(x ** 2 + z ** 2)
        v_fit = float(np.sum(a ** 2) / np.sum(a * t_exact))
        resid = t_exact - a / v_fit
        print(f"  {z:9.0f}   {v_fit:12.4f}   {(v_fit / v_ice - 1.0) * 100:+10.2f}%   "
              f"{np.max(np.abs(resid)):16.2f}   {t_exact[4] * v_fit / 2.0:18.1f}")
    print("\n  At 800 m the firn is a few per cent of the path and buys a small")
    print("  velocity bias; at 100 m it is a fifth of the path and moves the")
    print("  reported depth by several metres.  This is why firn correction is")
    print("  a shallow-section problem, and why a single velocity cannot be")
    print("  quoted for a whole profile.")

    section("7. Internal horizons as isochrones")
    t1_ns, t2_ns = 3000.0, 6000.0          # SYNTHETIC picked two-way times
    age_gap_a = 500.0                      # SYNTHETIC age difference, years
    z1_ice, z2_ice = t1_ns * v_ice / 2.0, t2_ns * v_ice / 2.0
    z1_two = invert_vertical(t1_ns, v_firn, v_ice)
    z2_two = invert_vertical(t2_ns, v_firn, v_ice)
    print(f"  SYNTHETIC two-way times {t1_ns:.0f} and {t2_ns:.0f} ns, age gap "
          f"{age_gap_a:.0f} a")
    print("  conversion            z1 (m)    z2 (m)   thickness (m)   "
          "accumulation (m/a)")
    for label, za, zb in (("uniform ice", z1_ice, z2_ice),
                          ("firn + ice", z1_two, z2_two)):
        print(f"  {label:20s} {za:8.1f}  {zb:8.1f}  {zb - za:14.1f}   "
              f"{(zb - za) / age_gap_a:18.4f}")
    dthick = (z2_two - z1_two) - (z2_ice - z1_ice)
    print(f"  the two conversions differ by {abs(dthick):.3f} m of thickness: the")
    print("  firn correction is a constant TIME offset shared by both horizons and")
    print("  it cancels in a difference.  Thicknesses between isochrones are")
    print("  therefore insensitive to the firn model, unlike absolute depths.")
    print("  What they are NOT insensitive to is the ice permittivity itself:")
    print("  eps_ice   thickness (m)   accumulation (m/a)")
    for eps in (EPS_ICE, EPS_ICE * 1.02, EPS_ICE * 0.98):
        v = v_of_eps(eps)
        th = (t2_ns - t1_ns) * v / 2.0
        print(f"  {eps:7.3f}   {th:13.1f}   {th / age_gap_a:18.4f}")
    print("  A 2% error in eps_ice is a 1% error in accumulation rate, which for")
    print("  a 500-year isochrone pair is five years of accumulation.")


if __name__ == "__main__":
    main()
