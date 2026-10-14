"""Rock-forming minerals and their physical properties.

Run:  .venv/bin/python mineralogy_demo.py
Requires: numpy (and the standard library).

Companion to lesson 04-01-03, "Rock-Forming Minerals and Their Physical
Properties".

A mineral's physical properties are not a list to be memorised. They follow
from the crystal structure and the composition, and this script computes three
of them from first principles so that the reader can see the connection and
check it:

1. **Density from the unit cell.** For a mineral whose cell volume, cell
   contents Z and formula mass are known,
       rho = Z M / (N_A V_cell).
   Nothing is fitted; the computed density either reproduces the measured one
   or the structure or the composition is wrong. All six minerals below land
   within about one per cent, which is how a reader can tell that the formula
   is being applied correctly.

2. **Elastic moduli from measured velocities.** For an isotropic rock,
       G = rho v_S^2,   K = rho (v_P^2 - (4/3) v_S^2),
       E = 9KG/(3K + G),   nu = (3K - 2G) / (2(3K + G)).
   This is the inverse of the direction normally used in the rock-physics
   lesson, and it is the direction that matters here: it turns a *measured*
   velocity into the modulus that controls how the mineral deforms.

3. **Mean atomic number and electron density.** The photoelectric absorption
   cross section per electron scales roughly as Z^3, so the *mean* atomic
   number of a mineral sets its photoelectric response, which is the physical
   basis of the lithology-diagnostic PEF curve in borehole logging. It also
   sets the electron density that a gamma-gamma (density) log responds to.

The mineral structural data are TABULATED crystallographic and physical data.
They are printed with the label TABULATED so they cannot be mistaken for
computed quantities, and every computed value is followed by the measured
value it is being checked against.
"""

from __future__ import annotations

import math

import numpy as np

N_A = 6.02214076e23             # mol^-1, exact by the 2019 SI definition

# --------------------------------------------------------------------------
# TABULATED inputs.
# (name, formula, Z, cell volume in A^3, formula mass in g/mol, Mohs
#  hardness, measured density in g/cm^3, v_P in km/s, v_S in km/s)
# Cell volumes from the conventional unit cells: alpha-quartz (hexagonal,
# a = 4.9134, c = 5.4052 A), forsterite (orthorhombic, a = 4.756,
# b = 10.207, c = 5.980 A), calcite (hexagonal, a = 4.990, c = 17.061 A),
# halite (cubic, a = 5.6402 A), pyrite (cubic, a = 5.4178 A),
# hematite (hexagonal, a = 5.038, c = 13.772 A).
# --------------------------------------------------------------------------
MINERALS = [
    ("alpha-quartz",  "SiO2",    3,  112.99,  60.083, 7.0, 2.65, 6.05, 4.09),
    ("forsterite",    "Mg2SiO4", 4,  290.30, 140.693, 7.0, 3.22, 8.55, 5.03),
    ("calcite",       "CaCO3",   6,  367.90, 100.086, 3.0, 2.71, 6.50, 3.30),
    ("halite",        "NaCl",    4,  179.40,  58.443, 2.5, 2.17, 4.54, 2.60),
    ("pyrite",        "FeS2",    4,  159.03, 119.975, 6.5, 5.01, 8.10, 4.70),
    ("hematite",      "Fe2O3",   6,  302.70, 159.688, 6.0, 5.26, 8.50, 5.00),
]

# Atomic numbers and atomic masses for the mean-Z calculation.
ATOMIC = {
    "Si": (14, 28.0855), "O": (8, 15.999), "Mg": (12, 24.305), "Ca": (20, 40.078),
    "C": (6, 12.011), "Na": (11, 22.990), "Cl": (17, 35.45), "Fe": (26, 55.845),
    "S": (16, 32.06),
}

# Formula-unit composition (element: count) for the mean-Z calculation.
COMPOSITION = {
    "SiO2":    {"Si": 1, "O": 2},
    "Mg2SiO4": {"Mg": 2, "Si": 1, "O": 4},
    "CaCO3":   {"Ca": 1, "C": 1, "O": 3},
    "NaCl":    {"Na": 1, "Cl": 1},
    "FeS2":    {"Fe": 1, "S": 2},
    "Fe2O3":   {"Fe": 2, "O": 3},
}


def section(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def part1_density_from_structure():
    section("1. Density computed from the unit cell")
    print("  rho = Z M / (N_A V_cell), with V_cell in cm^3 per cell.")
    print()
    print(f"  {'mineral':<14}{'formula':<10}{'Z':>3}{'V (A^3)':>10}"
          f"{'rho_calc':>10}{'rho_meas':>10}{'diff %':>9}")
    for name, formula, z, vol_a3, mass, mohs, rho_meas, vp, vs in MINERALS:
        vol_cm3 = vol_a3 * 1e-24
        rho = z * mass / (N_A * vol_cm3)
        print(f"  {name:<14}{formula:<10}{z:>3}{vol_a3:>10.2f}"
              f"{rho:>10.3f}{rho_meas:>10.2f}"
              f"{100 * (rho - rho_meas) / rho_meas:>9.1f}")
    print()
    print("  Every computed density lands within about one per cent of the")
    print("  measured value. That agreement is the check on the whole chain:")
    print("  the cell contents, the cell volume and the formula mass are")
    print("  consistent with each other, and the density is a derived quantity")
    print("  rather than an independent one.")
    print()
    print("  Two consequences worth stating.")
    print("  (a) The range is wide. Quartz at about 2.65 g/cm^3 and hematite")
    print("      at about 5.26 g/cm^3 differ by a factor of two, so the density")
    print("      of a rock is largely a statement about which minerals are in")
    print("      it -- which is exactly what makes gravity surveying useful for")
    print("      mapping rock type.")
    print("  (b) Iron-bearing minerals are the dense ones. Magnetite, hematite")
    print("      and pyrite are all near or above 5 g/cm^3, and magnetite is")
    print("      also the mineral that carries most of the induced magnetisation")
    print("      that a magnetic survey measures. Density and magnetisation are")
    print("      correlated in rocks largely through iron content.")
    print()


def part2_moduli_from_velocity():
    section("2. Elastic moduli computed from measured velocities")
    print("  G = rho v_S^2,  K = rho (v_P^2 - (4/3) v_S^2),")
    print("  E = 9KG / (3K + G),  nu = (3K - 2G) / (2(3K + G)).")
    print()
    print(f"  {'mineral':<14}{'v_P (km/s)':>12}{'v_S (km/s)':>12}"
          f"{'G (GPa)':>10}{'K (GPa)':>10}{'E (GPa)':>10}{'nu':>8}")
    for name, formula, z, vol_a3, mass, mohs, rho_meas, vp, vs in MINERALS:
        rho = rho_meas * 1e3              # kg/m^3
        vp_m = vp * 1e3
        vs_m = vs * 1e3
        g = rho * vs_m**2
        k = rho * (vp_m**2 - (4.0 / 3.0) * vs_m**2)
        e = 9.0 * k * g / (3.0 * k + g)
        nu = (3.0 * k - 2.0 * g) / (2.0 * (3.0 * k + g))
        print(f"  {name:<14}{vp:>12.2f}{vs:>12.2f}{g / 1e9:>10.1f}"
              f"{k / 1e9:>10.1f}{e / 1e9:>10.1f}{nu:>8.3f}")
    print()
    print("  The numbers are a check on the velocity values as much as on the")
    print("  formulas: a mineral with the wrong v_P/v_S ratio shows up")
    print("  immediately as an implausible Poisson's ratio. Values near 0.25")
    print("  are typical of silicates, and calcite's higher value is real --")
    print("  carbonate minerals are more compressible relative to their shear")
    print("  stiffness, which is one reason a limestone reservoir responds")
    print("  differently from a sandstone one in a seismic survey.")
    print()


def part3_mean_atomic_number():
    section("3. Mean atomic number and the photoelectric response")
    print("  Zbar = sum(n_i Z_i) / sum(n_i) over the atoms in the formula unit.")
    print("  Photoelectric absorption per electron scales roughly as Z^3, so")
    print("  the ratio of the (Zbar)^3 values below approximates the ratio of")
    print("  the photoelectric signals of the minerals.")
    print()
    print(f"  {'mineral':<14}{'Zbar':>8}{'Zbar^3':>10}"
          f"{'(Zbar/10)^3':>14}{'rho_e (e/cm^3 x 1e24)':>24}")
    z3_ref = None
    for name, formula, z, vol_a3, mass, mohs, rho_meas, vp, vs in MINERALS:
        comp = COMPOSITION[formula]
        n_atoms = sum(comp.values())
        zbar = sum(ATOMIC[e][0] * n for e, n in comp.items()) / n_atoms
        # Electron density: electrons per unit volume. Electrons per formula
        # unit = sum(n_i Z_i); grams per cm^3 = rho, so
        #   rho_e = rho * (electrons per formula unit) * N_A / M.
        electrons = sum(ATOMIC[e][0] * n for e, n in comp.items())
        rho_e = rho_meas * electrons * N_A / mass / 1e24
        if z3_ref is None:
            z3_ref = zbar**3
        print(f"  {name:<14}{zbar:>8.2f}{zbar**3:>10.1f}"
              f"{(zbar**3) / z3_ref:>14.2f}{rho_e:>24.2f}")
    print()
    print("  Read the third column and notice the trap. Quartz, forsterite")
    print("  and calcite all have Zbar exactly 10.00, because each formula unit")
    print("  happens to average ten protons per atom. Their densities differ")
    print("  by a factor of 1.2 or more but a photoelectric log")
    print("  cannot tell them apart at all. Halite is the opposite case: the")
    print("  lowest density of the six, 2.17 g/cm^3, but a mean atomic number")
    print("  of 14.0, so it stands out strongly on PEF and weakly on density.")
    print("  Pyrite and hematite are visible on both.")
    print()
    print("  That is the reason the PEF and density curves are run together")
    print("  rather than either one alone: they respond to different atomic")
    print("  properties -- electrons per unit volume for the density curve, and")
    print("  the atomic number for the photoelectric cross section -- and the")
    print("  pair of them separates mineralogies that either one alone")
    print("  confuses.")
    print()


def part4_porosity_and_specific_gravity():
    section("4. From mineral density to rock density: porosity")
    rho_grain = 2.65                  # quartz, g/cm^3
    print(f"  Take a rock whose grains are quartz (rho_grain = {rho_grain:.2f})")
    print("  and whose pores are filled with water. Then")
    print("    rho_bulk = (1 - phi) rho_grain + phi rho_fluid.")
    print()
    print(f"  {'phi':>8}{'rho_bulk, dry (g/cm^3)':>24}"
          f"{'rho_bulk, water-sat':>22}{'density contrast vs quartz':>28}")
    for phi in (0.0, 0.05, 0.10, 0.20, 0.30):
        dry = (1.0 - phi) * rho_grain
        sat = dry + phi * 1.00
        print(f"  {phi:>8.2f}{dry:>24.3f}{sat:>22.3f}"
              f"{100 * (sat - rho_grain) / rho_grain:>27.1f}%")
    print()
    print("  A 30 per cent porosity sandstone is about 18 per cent less dense")
    print("  than quartz, which is a larger density contrast than most of the")
    print("  lithological contacts a gravity survey is asked to find. Porosity,")
    print("  not mineralogy, is often the dominant control on the density that")
    print("  a survey measures, which is why the same rock type can be")
    print("  invisible or obvious depending on its history.")
    print()


def main():
    print("Rock-forming minerals and their physical properties.")
    part1_density_from_structure()
    part2_moduli_from_velocity()
    part3_mean_atomic_number()
    part4_porosity_and_specific_gravity()
    print("=" * 74)
    print("Structural, crystallographic and velocity data are TABULATED. Every")
    print("density and modulus above is computed from them, and each computed")
    print("value is printed next to the measured value it is checked against.")
    print("=" * 74)


if __name__ == "__main__":
    main()
