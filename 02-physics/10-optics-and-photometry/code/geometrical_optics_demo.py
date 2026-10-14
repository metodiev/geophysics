"""Geometrical optics, refraction and lenses for geophysical sensing.

Run:  python3 geometrical_optics_demo.py
Requires: Python standard library only.

Companion to lesson 02-10-01.

The script:

1. Tabulates Snell's law and the Fresnel reflectance at an air-water
   interface, i.e. the two numbers that decide how much light enters a
   water body and at what angle it travels.
2. Computes critical angles for total internal reflection (TIR) at three
   interfaces, including the silica core-cladding interface of an optical
   fibre, which is the physical basis of every fibre-optic sensor.
3. Computes the numerical aperture, acceptance angle, V number, mode count
   and single-mode cutoff wavelength of a step-index fibre.
4. Solves the thin-lens equation for two imaging systems and reports the
   magnification and the image size.
5. Computes apparent depth and the lateral displacement of a ray through a
   plane-parallel slab.
6. Computes the angle over which geometrical optics stops being valid,
   i.e. the diffraction angle lambda/a, and compares it with the ray angles
   used above.

Indices are nominal values for the stated materials at the stated
wavelength; a refractive index is a function of wavelength, temperature and
composition and must be taken from a datasheet for quantitative work.
"""

import math


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def deg(rad):
    return math.degrees(rad)


def snell(n1, n2, theta1):
    """Refraction angle from medium 1 into medium 2, in radians.

    Returns None when the angle is beyond the critical angle.
    """
    s = n1 * math.sin(theta1) / n2
    if s > 1.0:
        return None
    return math.asin(s)


def fresnel_normal(n1, n2):
    """Intensity reflectance at normal incidence."""
    return ((n1 - n2) / (n1 + n2)) ** 2


def fresnel_rs_rp(n1, n2, theta1):
    """Intensity reflectance for s and p polarisation.

    Returns (R_s, R_p) or (1.0, 1.0) beyond the critical angle.
    """
    theta2 = snell(n1, n2, theta1)
    if theta2 is None:
        return 1.0, 1.0
    c1, c2 = math.cos(theta1), math.cos(theta2)
    rs = ((n1 * c1 - n2 * c2) / (n1 * c1 + n2 * c2)) ** 2
    rp = ((n1 * c2 - n2 * c1) / (n1 * c2 + n2 * c1)) ** 2
    return rs, rp


def critical_angle(n1, n2):
    """Critical angle for n1 -> n2, in radians. None if n1 <= n2."""
    if n1 <= n2:
        return None
    return math.asin(n2 / n1)


# ---------------------------------------------------------------- materials
# Nominal refractive indices. Fused silica and silica fibre values are for
# ~1550 nm; water for the visible. Always use a datasheet value in practice.
N_AIR = 1.000293          # dry air at 15 C, 101.325 kPa, visible
N_WATER = 1.333           # water, ~589 nm, 20 C
N_GLASS = 1.520           # soda-lime crown glass, ~589 nm
N_SILICA = 1.4447         # pure silica cladding, 1550 nm
N_CORE = 1.4504           # GeO2-doped silica core, 1550 nm
CORE_RADIUS = 4.1e-6      # m, nominal for a single-mode telecom fibre
LAMBDA_FIBRE = 1550e-9    # m
V_SINGLE_MODE = 2.4048    # first zero of J_0, the LP11 cutoff


def part1_snell():
    section("1. Snell's law and Fresnel reflectance: air -> water")
    print(f"n_air = {N_AIR}, n_water = {N_WATER}")
    print()
    print(f"{'theta_1 (deg)':>14}{'theta_2 (deg)':>14}{'R_s':>10}{'R_p':>10}"
          f"{'R_unpol':>10}{'transmitted':>13}")
    R0 = fresnel_normal(N_AIR, N_WATER)
    for t1_deg in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 85.0, 89.0):
        t1 = math.radians(t1_deg)
        t2 = snell(N_AIR, N_WATER, t1)
        rs, rp = fresnel_rs_rp(N_AIR, N_WATER, t1)
        ru = 0.5 * (rs + rp)
        print(f"{t1_deg:>14.2f}{deg(t2):>14.6f}{rs:>10.5f}{rp:>10.5f}"
              f"{ru:>10.5f}{1.0 - ru:>13.5f}")
    print()
    print(f"  Reflectance at normal incidence, R = ((n1-n2)/(n1+n2))^2 = {R0:.5f}")
    print("  About 2 per cent of light is reflected at a calm water surface at")
    print("  normal incidence. The water-air interface is not 'transparent':")
    print("  this is the surface glint every water-leaving-radiance measurement")
    print("  must correct for.")
    tb = math.atan(N_WATER / N_AIR)
    rs_b, rp_b = fresnel_rs_rp(N_AIR, N_WATER, tb)
    print()
    print(f"  Brewster angle for air -> water = atan(n2/n1) = {deg(tb):.3f} deg, where")
    print(f"  R_p = 0 (numerically {abs(rp_b):.1e}) but R_s = {rs_b:.4f}.  The reflected")
    print("  light is fully s-polarised there, which is why a polarising filter")
    print("  removes water glint: the glint has a polarisation the signal does not.")
    print()
    print("  The refracted ray is bent toward the normal (n_water > n_air), and")
    print("  the compression is not linear: 60 deg of incidence becomes")
    print(f"  {deg(snell(N_AIR, N_WATER, math.radians(60.0))):.2f} deg in the water.  The whole incident")
    print("  hemisphere (0-90 deg) is squeezed into a cone of half-angle")
    print(f"  {deg(snell(N_AIR, N_WATER, math.radians(90.0))):.4f} deg inside the water, so a diver")
    print("  looking up sees the entire sky in a cone of")
    print(f"  {2 * deg(snell(N_AIR, N_WATER, math.radians(90.0))):.2f} deg: the 'Snell window'.")


def part2_tir():
    section("2. Total internal reflection and the critical angle")
    print(f"{'interface':<28}{'n1':>8}{'n2':>8}{'theta_c (deg)':>16}")
    for name, n1, n2 in (("water -> air", N_WATER, N_AIR),
                         ("glass -> air", N_GLASS, N_AIR),
                         ("silica fibre core -> clad", N_CORE, N_SILICA)):
        tc = critical_angle(n1, n2)
        print(f"{name:<28}{n1:>8.4f}{n2:>8.4f}{deg(tc):>16.5f}")
    print()
    print("  Inside a step-index fibre the ray meets the core-cladding interface")
    print(f"  at an angle of {deg(critical_angle(N_CORE, N_SILICA)):.4f} deg from the normal to that")
    print("  interface, which corresponds to a ray at")
    tc_axis = math.asin(math.sqrt(N_CORE ** 2 - N_SILICA ** 2) / N_CORE)
    print(f"  {deg(tc_axis):.4f} deg to the fibre axis.  Any ray steeper than that")
    print("  leaks out.  The 0.4 per cent index step between core and cladding is")
    print("  the entire mechanism of light guidance: the fibre is a waveguide")
    print("  with no mirror inside it.")


def part3_fibre():
    section("3. Step-index fibre: numerical aperture, V number and mode count")
    NA = math.sqrt(N_CORE ** 2 - N_SILICA ** 2)
    theta_air = math.asin(NA)
    theta_core = math.asin(NA / N_CORE)
    V = 2.0 * math.pi * CORE_RADIUS / LAMBDA_FIBRE * NA
    lambda_c = 2.0 * math.pi * CORE_RADIUS * NA / V_SINGLE_MODE
    M = V ** 2 / 2.0
    print(f"  core index n1        = {N_CORE}")
    print(f"  cladding index n2    = {N_SILICA}")
    print(f"  core radius a        = {CORE_RADIUS * 1e6:.2f} um")
    print(f"  wavelength lambda    = {LAMBDA_FIBRE * 1e9:.0f} nm")
    print()
    print(f"  numerical aperture NA = sqrt(n1^2 - n2^2) = {NA:.6f}")
    print(f"  acceptance half-angle in air = asin(NA)   = {deg(theta_air):.4f} deg")
    print(f"  maximum ray angle to the axis in the core = {deg(theta_core):.4f} deg")
    print()
    print(f"  V = 2*pi*a*NA/lambda                      = {V:.4f}")
    print(f"  number of guided modes M ~ V^2/2          = {M:.3f}")
    print(f"  single-mode cutoff lambda_c = 2*pi*a*NA/2.4048 = {lambda_c * 1e9:.1f} nm")
    print()
    print(f"  V = {V:.3f} is below the single-mode limit 2.4048, so this fibre")
    print("  guides one spatial mode (two orthogonal polarisations).  Increase the")
    print("  core radius, raise the index step, or shorten the wavelength and V")
    print("  rises: at V = 10 the same formula gives M ~ 50 guided modes.")
    print()
    print("  Why this matters for sensing: a single-mode fibre carries one spatial")
    print("  mode, so the measured optical phase is a single well-defined number.")
    print("  A multimode fibre averages over many paths and has no single phase.")


def part4_lens():
    section("4. Thin-lens imaging: the instrument equation")
    print("  1/f = 1/s + 1/s' ,  magnification m = -s'/s")
    print()
    print(f"{'system':<26}{'f (mm)':>9}{'s (m)':>12}{'image s (mm)':>15}{'m':>12}")
    results = {}
    for name, f, s in (("camera, focused at 3 m", 0.050, 3.0),
                       ("camera, focused at 30 m", 0.050, 30.0),
                       ("camera, focused at inf", 0.050, 1.0e9),
                       ("telescope objective", 1.200, 1.0e9)):
        sp = 1.0 / (1.0 / f - 1.0 / s)
        m = -sp / s
        results[name] = (f, s, sp, m)
        print(f"{name:<26}{f * 1e3:>9.1f}{s:>12.4g}{sp * 1e3:>15.4f}{m:>12.4e}")
    print()
    f, s, sp, m = results["camera, focused at 3 m"]
    print(f"  With f = 50 mm and the subject at 3 m the sensor sits")
    print(f"  {sp * 1e3:.3f} mm behind the lens, and a 1 m object images to")
    print(f"  {abs(m) * 1e3:.3f} mm on the sensor.")
    print()
    for name in ("camera, focused at inf", "camera, focused at 3 m"):
        print(f"  {name:<26} image distance = {results[name][2] * 1e3:.4f} mm")
    travel = (results["camera, focused at 3 m"][2]
              - results["camera, focused at inf"][2])
    print()
    print(f"  Focus travel from infinity to 3 m = {travel * 1e3:.3f} mm.  That")
    print("  sub-millimetre number is what a camera's focus mechanism has to")
    print("  deliver, and it is why macro photography needs a different lens")
    print("  rather than a longer thread.")
    print()
    print("  Aperture sets resolution; focal length sets scale.  Those are two")
    print("  different jobs and confusing them is the commonest error in")
    print("  instrument design (lesson 02-10-02 gives the resolution limit).")


def part5_misc():
    section("5. Apparent depth, slab displacement and the ray-optics limit")
    apparent = 1.0 / N_WATER
    print(f"  apparent depth of water = real depth / n = {apparent:.4f} x real depth")
    print("  A 2 m deep pool looks 1.5 m deep.  Snell's law with n = 4/3 is why")
    print("  spear fishing is done with the correction applied.")
    print()
    print("  Lateral displacement of a ray through a plane-parallel slab of")
    print("  thickness t (glass, n = 1.52, in air):")
    t = 0.010
    print(f"  t = {t * 1e3:.1f} mm")
    print(f"{'theta_1 (deg)':>14}{'theta_2 (deg)':>14}{'displacement (mm)':>20}")
    for t1_deg in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0):
        t1 = math.radians(t1_deg)
        t2 = snell(N_AIR, N_GLASS, t1)
        d = t * math.sin(t1 - t2) / math.cos(t2)
        print(f"{t1_deg:>14.2f}{deg(t2):>14.4f}{d * 1e3:>20.6f}")
    print()
    print("  A window in front of a sensor does not merely attenuate: it shifts")
    print("  the apparent position of everything behind it, by an amount that")
    print("  grows with incidence angle.  A 10 mm window shifts an off-axis ray by")
    print(f"  {t * math.sin(math.radians(45) - snell(N_AIR, N_GLASS, math.radians(45))) / math.cos(snell(N_AIR, N_GLASS, math.radians(45))) * 1e3:.4f} mm at 45 deg.")


def part6_limit():
    section("6. Where geometrical optics stops being valid")
    print("  Ray optics assumes a -> 0 relative to lambda.  The diffraction")
    print("  half-angle of an aperture of characteristic size a is of order")
    print("  lambda/a, so the ray picture holds when lambda/a is far below the")
    print("  angles the system actually uses:")
    print()
    print(f"{'a':>12}{'lambda':>10}{'lambda/a (deg)':>18}   {'comment':<26}")
    rows = ((2.0e-3, 550e-9, "eye pupil: ray optics ok"),
            (0.15, 550e-9, "camera lens: ray optics ok"),
            (8.2e-6, 1550e-9, "fibre core: not ray optics"),
            (1.0e-6, 633e-9, "grating period: diffraction"),
            (1.0e-8, 500e-9, "protein: no ray picture"))
    for a, lam, comment in rows:
        print(f"{a:>12.3e}{lam * 1e9:>9.0f}nm{deg(lam / a):>18.4f}   {comment:<26}")
    print()
    print(f"  At a = {CORE_RADIUS * 2e6:.1f} um and lambda = 1550 nm, lambda/a =")
    print(f"  {1550e-9 / (CORE_RADIUS * 2):.4f} rad = {deg(1550e-9 / (CORE_RADIUS * 2)):.2f} deg, comparable with the")
    print(f"  guiding angle of {deg(math.asin(math.sqrt(N_CORE ** 2 - N_SILICA ** 2) / N_CORE)):.2f} deg.  The ray picture therefore gives the")
    print("  right acceptance cone — NA is defined by the indices, and the cone")
    print("  is a property of the boundary condition — but it cannot say how")
    print("  many modes the core supports or how the field is distributed")
    print("  across it.  That requires the waveguide eigenvalue problem of")
    print("  lesson 02-10-05, which is where V, the mode count and the")
    print("  single-mode cutoff of section 3 actually come from.")


def main():
    print("Geometrical optics, refraction and lenses")
    print("Nominal indices: air 1.000293, water 1.333, glass 1.520, silica 1.4447,")
    print("doped-silica core 1.4504.")
    part1_snell()
    part2_tir()
    part3_fibre()
    part4_lens()
    part5_misc()
    part6_limit()


if __name__ == "__main__":
    main()
