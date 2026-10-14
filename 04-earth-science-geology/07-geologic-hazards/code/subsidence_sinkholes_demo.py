"""Subsidence, sinkholes and karst: the mechanics and the measurements.

Run:  .venv/bin/python subsidence_sinkholes_demo.py
Requires: numpy (used only for a gradient).

Companion to lesson 04-07-04.

1. Effective stress from a water-level decline, and the compaction of a clay
   layer, in the two forms that are actually used (a constrained modulus, and
   a compression index).
2. The free-air gradient, derived from g = GM/r^2, and its relation to the
   Bouguer correction.  This pair is the whole basis of 4-D microgravity.
3. Karst denudation from a dissolved-load mass balance, with the time to
   dissolve a cave passage.
4. A crude cavity-roof stability model, presented as crude, to show why
   sinkhole prediction is not a solved problem.
5. InSAR sensitivity: the phase change produced by a centimetre of motion, and
   the loss of sensitivity when the displacement is horizontal.
6. The residual gravity change from a water-table decline, which is the
   quantity a repeat gravity survey is trying to isolate.

All parameters are NOMINAL and labelled.  No measured subsidence rate, no
sinkhole and no karst region is quoted.
"""

import math

import numpy as np

G = 6.67430e-11
G_W = 9.80665
RHO_W = 1000.0
R_EARTH = 6.371e6      # m, mean radius (a defined/measured mean value)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# --------------------------------------------------------------------------
# 1. Effective stress and compaction
# --------------------------------------------------------------------------

def part1():
    section("1. Effective stress and the compaction of a clay layer")
    dh = 5.0          # m, water-level decline
    h_clay = 30.0     # m, clay thickness
    print(f"  water-level decline dh = {dh:.1f} m over a clay layer "
          f"{h_clay:.1f} m thick")
    dsig = RHO_W * G_W * dh
    print(f"  Terzaghi: dsig' = rho_w g dh = {RHO_W*G_W:.0f} * {dh:.1f} = "
          f"{dsig:.1f} Pa = {dsig/1000:.2f} kPa")
    print()
    print("  Form 1 (a constrained modulus): dH = m_v dsig' H.")
    print("  m_v = 1/E_oed is a MEASURED oedometer property; typical soft clay")
    print("  values span about 0.1 to 1.5 m^2/MN, so the answer is a range.")
    print()
    print("     m_v (m^2/MN)   dH (m)   dH (mm)")
    for mv in (0.1, 0.3, 0.5, 1.0, 1.5):
        dH = mv * (dsig / 1e6) * h_clay
        print(f"  {mv:13.2f}   {dH:7.4f}   {dH*1000:8.1f}")
    print()
    print("  Form 2 (a compression index, for a normally consolidated clay):")
    print("    dH = C_c/(1+e_0) H log10((sig'_0 + dsig')/sig'_0),")
    print("  with C_c and e_0 both MEASURED.  It is logarithmic, so the")
    print("  subsidence from the first metre of drawdown is much larger than")
    print("  from the tenth: the response is not proportional to the cause.")
    cc, e0, sig0 = 0.3, 1.0, 100e3
    print()
    print("     sig'_0 (kPa)   dH (m)")
    for s0 in (50e3, 100e3, 200e3):
        dH = cc / (1.0 + e0) * h_clay * math.log10((s0 + dsig) / s0)
        print(f"  {s0/1000:12.1f}   {dH:7.4f}")
    print()
    print("  Same 5 m of drawdown, three different answers depending on the")
    print("  pre-consolidation stress.  This is why a subsidence forecast requires")
    print("  a laboratory compressibility test and an in-situ stress history,")
    print("  neither of which any geophysical method supplies directly.")


# --------------------------------------------------------------------------
# 2. Free-air and Bouguer gradients
# --------------------------------------------------------------------------

def part2():
    section("2. The free-air gradient, derived")
    print("  g(z) = GM/(R+z)^2, so dg/dz = -2GM/R^3 = -2g/R.")
    grad = -2.0 * G_W / R_EARTH
    print(f"  -2g/R = {grad:.6e} (m/s^2) per m")
    print(f"  = {abs(grad)/1e-5:.5f} mGal per metre"
          f" = {abs(grad)*1e-2/1e-8:.4f} microgal per cm")
    print("  The conventional free-air coefficient is 0.3086 mGal/m.  The")
    print("  difference from the 0.30785 computed here is 0.25 per cent, and it")
    print("  is not an error: the conventional value is the gradient of the")
    print("  NORMAL gravity field on the ellipsoid (the Somigliana formula),")
    print("  which contains the flattening and a latitude dependence that 2g/R")
    print("  does not.  Use the conventional value to reduce a survey; use 2g/R")
    print("  to know why the number is what it is.")
    print()
    print("  Bouguer slab of density rho, thickness 1 m: dg = 2 pi G rho h.")
    print()
    print("     rho (kg/m^3)   2 pi G rho (mGal/m)")
    for rho in (1000.0, 2000.0, 2670.0, 3000.0):
        print(f"  {rho:12.0f}   {2*math.pi*G*rho/1e-5:18.5f}")
    print()
    print("  For rho = 2670 the Bouguer term is 0.1119 mGal/m, so the combined")
    print(f"  free-air minus Bouguer gradient is "
          f"{(abs(grad)/1e-5 - 2*math.pi*G*2670.0/1e-5):.5f} mGal/m.")
    print("  That residual is the gradient a borehole gravimeter measures in")
    print("  uniform rock, and the amount by which it deviates is the density.")
    print("  This is densimetry, not subsidence yet.")


# --------------------------------------------------------------------------
# 3. Karst denudation
# --------------------------------------------------------------------------

def part3():
    section("3. Karst denudation from a dissolved-load mass balance")
    print("  Mass balance over a catchment of area A with recharge P and a")
    print("  dissolved load concentration c (kg/m^3):")
    print("     rho_rock * D * A = c * P * A   ->   D = c P / rho_rock")
    print("  so the denudation rate D needs only a concentration, a recharge")
    print("  and a rock density — all three measured, none of them inferred")
    print("  from a model.")
    print()
    rho_rock = 2700.0
    P = 0.5           # m/yr, NOMINAL temperate recharge
    print(f"  recharge P = {P:.1f} m/yr (NOMINAL), rock density "
          f"{rho_rock:.0f} kg/m^3 (NOMINAL limestone)")
    print()
    print("     c (mg/L)   D (mm/ka)   D (m/Ma)   time to dissolve 10 m (ka)")
    for c_mgl in (30.0, 60.0, 100.0, 150.0, 200.0):
        c = c_mgl * 1e-3
        D = c * P / rho_rock
        print(f"  {c_mgl:10.0f}   {D*1e6:10.2f}   {D*1e6:10.2f}   "
              f"{10.0/D/1e3:25.0f}")
    print()
    c = 100.0e-3
    D = c * P / rho_rock
    print(f"  At c = 100 mg/L the denudation rate is {D:.3e} m/yr = "
          f"{D*1e6:.1f} mm/ka and a 10 m")
    print(f"  void takes {10.0/D/1e3:.0f} ka to remove.  That is the scale of the")
    print("  process: karst is a landscape formed over hundreds of thousands of")
    print("  years, which is why a sinkhole that forms in an afternoon is the")
    print("  final collapse of a void that was already there.")
    print()
    print("  The number that matters for hazard is therefore not the dissolution")
    print("  rate but the location and size of the existing voids, which is a")
    print("  geophysical question (microgravity, GPR, ERT, seismic).")


# --------------------------------------------------------------------------
# 4. Cavity roof stability, crudely
# --------------------------------------------------------------------------

def part4():
    section("4. A crude cavity-roof model, to show that it is crude")
    print("  Model: the roof is a simply supported beam of thickness t and unit")
    print("  width spanning a cavity of span D under its own weight w = rho g t.")
    print("     M = w D^2 / 8,  sigma = 6M/t^2 = 3 rho g D^2 / (4 t)")
    print("  Setting sigma equal to the tensile strength sigma_t gives")
    print("     D_c = sqrt(4 sigma_t t / (3 rho g)).")
    print()
    rho = 1800.0
    print(f"  rho = {rho:.0f} kg/m^3 (NOMINAL soil)")
    print()
    print("     t (m)   sigma_t = 10 kPa   sigma_t = 20 kPa   sigma_t = 50 kPa")
    for t in (1.0, 2.0, 3.0, 5.0, 10.0):
        row = []
        for st in (10e3, 20e3, 50e3):
            row.append(math.sqrt(4.0 * st * t / (3.0 * rho * G_W)))
        print(f"  {t:7.1f}   {row[0]:16.3f}   {row[1]:16.3f}   {row[2]:16.3f}")
    print()
    print("  Every assumption in that model is wrong: a soil roof carries load")
    print("  by arching, not bending; tensile strength is not a soil property in")
    print("  the way it is for steel; and the water table, which is the actual")
    print("  control, does not appear at all.  The model is included to make")
    print("  the point that a critical span can be computed and still be")
    print("  useless.  The physical statement that survives is the scaling:")
    print("  D_c grows as the square root of roof thickness and of tensile")
    print("  strength, so a doubling of thickness buys only a 41 per cent")
    print(f"  increase in the span that survives ({math.sqrt(2.0):.4f} x).")


# --------------------------------------------------------------------------
# 5. InSAR phase sensitivity
# --------------------------------------------------------------------------

def part5():
    section("5. InSAR: one centimetre of motion, and the horizontal blind spot")
    lam = 0.0556      # m, C-band (Sentinel-1 carrier), a NOMINAL instrument value
    print(f"  wavelength lambda = {lam*100:.2f} cm (C-band carrier, nominal)")
    print("  One-way path change dr gives dphi = 4 pi dr / lambda (two-way path).")
    print()
    print("     dr (cm)   dphi (rad)   dphi (cycles)")
    for dr_cm in (0.1, 0.5, 1.0, 2.8, 5.0):
        dr = dr_cm / 100.0
        phi = 4.0 * math.pi * dr / lam
        print(f"  {dr_cm:9.1f}   {phi:11.4f}   {phi/(2*math.pi):13.4f}")
    print()
    print(f"  One fringe (2 pi) is {lam/2*100:.3f} cm of line-of-sight motion,")
    print("  so the method resolves a fraction of a centimetre on a stable")
    print("  scatterer and is ambiguous beyond that fraction (phase wrapping).")
    print()
    print("  Geometry.  If the surface moves purely vertically by u_z and the")
    print("  satellite looks at incidence angle theta, the line-of-sight")
    print("  component is u_LOS = u_z cos(theta).")
    print()
    print("     theta (deg)   u_LOS/u_z   fraction of vertical recovered")
    for theta in (0.0, 23.0, 33.0, 39.0, 45.0):
        print(f"  {theta:11.1f}   {math.cos(math.radians(theta)):9.4f}"
              f"   {math.cos(math.radians(theta))*100:26.1f} per cent")
    print()
    print("  For a Sentinel-1-class geometry near 39 deg, a 1 cm vertical")
    print(f"  motion appears as {math.cos(math.radians(39.0)):.4f} cm of path change.")
    print("  A displacement that is purely HORIZONTAL and perpendicular to the")
    print("  look direction produces NO phase change at all: a single track")
    print("  cannot separate vertical from horizontal motion, which is why")
    print("  ascending and descending geometries are used together, and why")
    print("  GNSS is still needed to fix the sense of the motion.")


# --------------------------------------------------------------------------
# 6. Residual gravity from a water-table decline
# --------------------------------------------------------------------------

def part6():
    section("6. Residual gravity from a water-table decline")
    por = 0.30
    dh = 5.0
    drho = -por * RHO_W
    slab = 2.0 * math.pi * G * drho * dh
    print(f"  porosity phi = {por:.2f}, decline dh = {dh:.1f} m,")
    print(f"  so the density change in the drained zone is -phi rho_w = "
          f"{drho:.0f} kg/m^3")
    print()
    print(f"  mass term  2 pi G drho dh = {slab:.6e} m/s^2 = "
          f"{slab/1e-8:.3f} microgal")
    fa = abs(-2.0 * G_W / R_EARTH) * dh
    print(f"  free-air term from the surface declining by the same {dh:.1f} m = "
          f"{fa/1e-8:.3f} microgal")
    print()
    print("  Sign convention matters and is the commonest error in 4-D")
    print("  microgravity.  The ground surface drops by dh, and a benchmark set")
    print("  in the ground drops with it, moving toward the centre where g is")
    print(f"  larger: the free-air term is a POSITIVE change in g of "
          f"{fa/1e-8:.1f} microgal.")
    print(f"  The water loss is a negative change of {abs(slab)/1e-8:.1f} microgal.")
    print(f"  The measured change is the sum, {fa/1e-8 - abs(slab)/1e-8:.1f} microgal,")
    print("  and it is the residual after removing the free-air term that reports")
    print("  the mass loss.")
    print()
    print("  A repeat survey repeatable to 5 microgal therefore sees this")
    print("  signal with a signal-to-noise of about "
          f"{abs(slab)/1e-8/5.0:.1f}, provided the elevation change is measured")
    print("  as accurately as the gravity — typically by levelling or GNSS.")


def main():
    print("Subsidence and karst -- computed quantities")
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()
    print()
    print("=" * 72)
    print("No subsidence rate, sinkhole event, karst region or survey dataset")
    print("is quoted in this script.  All parameters are NOMINAL.")
    print("=" * 72)


if __name__ == "__main__":
    main()
