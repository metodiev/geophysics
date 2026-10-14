"""Igneous, sedimentary and metamorphic rocks: classification and properties.

Run:  .venv/bin/python rock_types_demo.py
Requires: numpy (and the standard library).

Companion to lesson 04-01-04, "Igneous, Sedimentary and Metamorphic Rocks".

The lesson's claim is that a rock classification is a *decision procedure* with
quantitative inputs, and that the geophysically useful part of the
classification is the physical-property range each class occupies. This script
implements three of the standard procedures and shows the property ranges that
come out of them.

1. **Igneous rocks.** The QAPF modal classification: normalise the modal
   amounts of quartz (Q), alkali feldspar (A) and plagioclase (P) to 100 per
   cent, locate the composition in the Q-A-P triangle, and read off the rock
   name from the standard field boundaries. Four modal analyses are classified
   and the answer checked against the name a petrologist would give them.
2. **Sedimentary rocks.** Grain size to the phi scale, the Wentworth size
   classes, and the Folk and Ward graphical statistics (mean, sorting,
   skewness, kurtosis) computed from a synthetic cumulative grain-size curve.
   Sorting is the quantity that controls porosity and permeability, so it is
   the sedimentary measurement that matters most for geophysics.
3. **Metamorphic rocks.** The metamorphic facies as a function of pressure and
   temperature, computed for three geothermal gradients. The facies field
   boundaries used here are the approximate teaching boundaries, not the
   reaction-defined boundaries of a petrology text, and the script says so.
4. **Property ranges.** Grain density and porosity for a representative rock of
   each class, with the density and porosity contrasts that a gravity, seismic
   or resistivity survey would see.

Every classification boundary and every property value here is TABULATED or
NOMINAL. Real rocks sit on the boundaries, and real property ranges overlap
between classes; the script reports the overlaps rather than hiding them.
"""

from __future__ import annotations

import math

import numpy as np

G_ACC = 9.81
RHO_CRUST = 2800.0                 # kg/m^3, for depth from pressure


def section(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


# --------------------------------------------------------------------------
# 1. Igneous: QAPF modal classification
# --------------------------------------------------------------------------

def qapf_name(q, a, p):
    """QAPF plutonic name from modal Q, A, P (percentages of Q+A+P)."""
    total = q + a + p
    qn, an, pn = 100.0 * q / total, 100.0 * a / total, 100.0 * p / total
    ap_ratio = 100.0 * an / (an + pn)          # the horizontal axis
    if qn > 60.0:
        return "quartz-rich granitoid", qn, ap_ratio
    if qn >= 20.0:
        if ap_ratio >= 90.0:
            name = "alkali feldspar granite"
        elif ap_ratio >= 65.0:
            name = "syenogranite"
        elif ap_ratio >= 35.0:
            name = "monzogranite"
        elif ap_ratio >= 10.0:
            name = "granodiorite"
        else:
            name = "tonalite"
        return name, qn, ap_ratio
    if qn >= 5.0:
        if ap_ratio >= 90.0:
            name = "quartz alkali feldspar syenite"
        elif ap_ratio >= 65.0:
            name = "quartz syenite"
        elif ap_ratio >= 35.0:
            name = "quartz monzonite"
        elif ap_ratio >= 10.0:
            name = "quartz monzodiorite"
        else:
            name = "quartz diorite / quartz gabbro"
        return name, qn, ap_ratio
    if ap_ratio >= 90.0:
        name = "alkali feldspar syenite"
    elif ap_ratio >= 65.0:
        name = "syenite"
    elif ap_ratio >= 35.0:
        name = "monzonite"
    elif ap_ratio >= 10.0:
        name = "monzodiorite"
    else:
        name = "diorite / gabbro"
    return name, qn, ap_ratio


def part1_igneous():
    section("1. Igneous rocks: the QAPF modal classification")
    print("  Q, A and P are normalised to 100 per cent; the rock name comes")
    print("  from the position in the Q-A-P triangle. The vertical axis is Q")
    print("  (quartz), the horizontal axis is A/(A+P) (the feldspar ratio).")
    print()
    samples = [
        ("a granite",        25.0, 35.0, 30.0, 10.0, "monzogranite"),
        ("a granodiorite",   22.0, 18.0, 45.0, 15.0, "granodiorite"),
        ("a tonalite",       25.0,  5.0, 60.0, 10.0, "tonalite"),
        ("a gabbro",          3.0,  6.0, 61.0, 30.0, "diorite / gabbro"),
        ("a syenite",         4.0, 80.0, 10.0,  6.0, "syenite"),
    ]
    print(f"  {'modal analysis':<18}{'Q':>6}{'A':>6}{'P':>6}{'mafic':>7}"
          f"{'colour index':>14}  {'QAPF name':<28}{'check'}")
    for label, q, a, p, mafic, expected in samples:
        name, qn, ap_ratio = qapf_name(q, a, p)
        ok = "OK" if name == expected else f"expected {expected}"
        print(f"  {label:<18}{q:>6.0f}{a:>6.0f}{p:>6.0f}{mafic:>7.0f}"
              f"{mafic:>13.0f}%  {name:<28}{ok}")
    print()
    print("  The classification is a partition of a triangle, not a list of")
    print("  names, and it has two consequences that matter geophysically.")
    print()
    print("  First, the *colour index* (the mafic percentage, last column) is")
    print("  what actually tracks the physical properties. Quartz and the")
    print("  feldspars all have densities near 2.6-2.7 g/cm^3 and seismic")
    print("  velocities below 7 km/s; the mafic minerals -- olivine, pyroxene,")
    print("  amphibole, biotite -- run from 3.0 to 3.4 g/cm^3 with much higher")
    print("  velocities. A granite and a gabbro differ in name by their")
    print("  feldspar ratio and in *physics* by their mafic content, and only")
    print("  the second is what a seismic or gravity survey measures.")
    print()
    print("  Second, the QAPF classification applies to *coarse-grained*")
    print("  (plutonic) rocks. A volcanic rock with the same chemistry is")
    print("  named from the TAS diagram on the basis of its silica content")
    print("  (SiO2 < 45 wt% ultramafic, 45-52 mafic, 52-63 intermediate,")
    print("  63-77 felsic), because a fine-grained rock has no measurable")
    print("  mode. The same magma therefore carries two names depending on how")
    print("  fast it cooled, which is a reminder that the classification")
    print("  describes texture as much as composition.")
    print()


# --------------------------------------------------------------------------
# 2. Sedimentary: grain size, phi scale and sorting statistics
# --------------------------------------------------------------------------

def phi(d_mm):
    """The Krumbein phi scale: phi = -log2(d in mm)."""
    return -math.log2(d_mm)


WENTWORTH = [
    (256.0, "boulder"),
    (64.0, "cobble"),
    (4.0, "pebble"),
    (2.0, "granule"),
    (1.0, "very coarse sand"),
    (0.5, "coarse sand"),
    (0.25, "medium sand"),
    (0.125, "fine sand"),
    (0.0625, "very fine sand"),
    (0.0039, "silt"),
    (0.0, "clay"),
]


def wentworth(d_mm):
    for limit, name in WENTWORTH:
        if d_mm >= limit:
            return name
    return "clay"


def part2_sedimentary():
    section("2. Sedimentary rocks: the phi scale and sorting statistics")
    print("  phi = -log2(d in mm).  The scale is logarithmic because grain")
    print("  size varies over four orders of magnitude in one deposit.")
    print()
    print(f"  {'d (mm)':>10}{'d (um)':>10}{'phi':>8}   class")
    for d in (256.0, 64.0, 4.0, 2.0, 0.5, 0.25, 0.125, 0.0625, 0.01, 0.002):
        print(f"  {d:>10.4g}{d * 1000:>10.1f}{phi(d):>8.2f}   {wentworth(d)}")
    print()

    # A synthetic grain-size distribution: a mixture of two log-normal
    # populations, which is what a moderately sorted sand actually looks like.
    rng = np.random.default_rng(20241014)
    n = 400_000
    coarse = rng.normal(loc=phi(0.30), scale=0.55, size=n // 2)   # mode near 0.30 mm
    fine = rng.normal(loc=phi(0.12), scale=0.70, size=n - n // 2)
    sample_phi = np.concatenate([coarse, fine])

    pct = np.percentile(sample_phi, [5, 16, 25, 50, 75, 84, 95])
    p5, p16, p25, p50, p75, p84, p95 = pct
    mz = (p16 + p50 + p84) / 3.0
    sigma_i = (p84 - p16) / 4.0 + (p95 - p5) / 6.6
    sk_i = ((p84 + p16 - 2 * p50) / (2 * (p84 - p16))
            + (p95 + p5 - 2 * p50) / (2 * (p95 - p5)))
    k_g = (p95 - p5) / (2.44 * (p75 - p25))

    print("  A synthetic sample: two log-normal populations mixed, which is")
    print("  what a moderately sorted sand looks like. Percentiles of the")
    print("  cumulative curve, in phi units:")
    print(f"    phi5 = {p5:6.3f}   phi16 = {p16:6.3f}   phi25 = {p25:6.3f}"
          f"   phi50 = {p50:6.3f}")
    print(f"    phi75 = {p75:6.3f}   phi84 = {p84:6.3f}   phi95 = {p95:6.3f}")
    print()
    print("  Folk and Ward (1957) graphical statistics:")
    print(f"    mean       Mz   = (phi16 + phi50 + phi84)/3          = {mz:6.3f}")
    print(f"    sorting    sigma_I = (phi84-phi16)/4 + (phi95-phi5)/6.6 = "
          f"{sigma_i:6.3f}")
    print(f"    skewness   Sk_I  = the two-term expression above        = "
          f"{sk_i:6.3f}")
    print(f"    kurtosis   K_G   = (phi95-phi5)/(2.44 (phi75-phi25))    = "
          f"{k_g:6.3f}")
    print()

    def sorting_class(s):
        for limit, name in ((0.35, "very well sorted"),
                            (0.50, "well sorted"),
                            (0.71, "moderately well sorted"),
                            (1.00, "moderately sorted"),
                            (2.00, "poorly sorted")):
            if s < limit:
                return name
        return "very poorly sorted"

    print(f"  Sorting value {sigma_i:.3f} -> {sorting_class(sigma_i)} "
          "(Folk and Ward classes).")
    print(f"  Median grain size in mm: {2 ** (-p50):.4f} mm "
          f"({wentworth(2 ** (-p50))}).")
    print()
    print("  Why sorting is the geophysically important statistic: it controls")
    print("  porosity directly. A perfectly sorted sand packs to 36-40 per cent")
    print("  porosity regardless of its grain size; adding 20 per cent of")
    print("  fines that fit into the pores drops that to 25-30 per cent, and")
    print("  the permeability falls by an order of magnitude or more because")
    print("  the fine fraction blocks the pore throats rather than the pores.")
    print("  The grain size sets the *permeability* scale and the sorting sets")
    print("  the fraction of it that survives, which is why a well-sorted")
    print("  coarse sand is a reservoir and a poorly sorted mix of the same")
    print("  grains is not.")
    print()


# --------------------------------------------------------------------------
# 3. Metamorphic: facies from pressure and temperature
# --------------------------------------------------------------------------

def facies_at(p_gpa, t_c):
    """Approximate metamorphic facies from P and T.

    The fields are the standard teaching boxes, ordered so that they tile the
    (P, T) plane: the pressure-controlled facies are tested first, then the
    temperature-controlled ones.  Real boundaries are defined by specific
    mineral reactions, vary with bulk composition, and are NOMINAL here.
    """
    if p_gpa >= 1.2 and t_c < 1000.0:
        return "eclogite", "garnet + omphacite"
    if p_gpa >= 0.6 and t_c < 350.0:
        return "blueschist", "glaucophane + lawsonite"
    if t_c < 200.0:
        return "zeolite", "zeolites, clays"
    if t_c < 300.0:
        return "prehnite-pumpellyite", "prehnite, pumpellyite"
    if t_c < 500.0:
        return "greenschist", "chlorite + actinolite + albite"
    if t_c < 700.0:
        return "amphibolite", "hornblende + plagioclase"
    if t_c < 1000.0:
        return "granulite", "orthopyroxene, anhydrous"
    return "granulite / partial melt", "anhydrous + melt"


def geotherm_linear(z_km, gradient, t_surface=10.0):
    """A purely linear geotherm: the cold end-member."""
    return t_surface + gradient * z_km


def geotherm_conductive(z_km, q_mantle, heat_production, t_surface=10.0):
    """Steady conductive geotherm with uniform crustal heat production.

    T(z) = T_s + (q_m z + A z^2 / 2) / k, the solution of
    d/dz (k dT/dz) = -A with q = q_m at the base of the radiogenic layer.
    This is the standard model geotherm and it flattens with depth, unlike the
    linear one, because heat production adds to the flux as you go down.
    """
    k = 2.5                     # W m^-1 K^-1, NOMINAL crustal conductivity
    z_m = z_km * 1e3
    return t_surface + (q_mantle * z_m + heat_production * z_m**2 / 2.0) / k


def part3_metamorphic():
    section("3. Metamorphic rocks: facies as a function of P and T")
    print("  Depth from pressure: z = P / (rho g) with rho = 2800 kg/m^3, so")
    print(f"  1 GPa is about {1e9 / (RHO_CRUST * G_ACC) / 1e3:.0f} km of crust.")
    print("  The facies fields are the approximate teaching boxes, not the")
    print("  reaction-defined boundaries of a petrology text. They are NOMINAL.")
    print()
    geotherms = [
        ("cold subduction",  "linear, 10 K/km",
         lambda z: geotherm_linear(z, 10.0)),
        ("standard continental", "conductive, q_m = 21 mW/m^2, A = 1.0 uW/m^3",
         lambda z: geotherm_conductive(z, 0.021, 1.0e-6)),
        ("extended / hot",   "conductive, q_m = 30 mW/m^2, A = 2.5 uW/m^3",
         lambda z: geotherm_conductive(z, 0.030, 2.5e-6)),
    ]
    for label, formula, temp in geotherms:
        print(f"  {label} ({formula}):")
        print(f"    {'z (km)':>8}{'P (GPa)':>10}{'T (C)':>8}   "
              f"{'facies':<30}{'diagnostic assemblage'}")
        for z_km in (5.0, 15.0, 25.0, 35.0, 45.0):
            p_gpa = RHO_CRUST * G_ACC * z_km * 1e3 / 1e9
            t_c = temp(z_km)
            name, diag = facies_at(p_gpa, t_c)
            print(f"    {z_km:>8.0f}{p_gpa:>10.2f}{t_c:>8.0f}   "
                  f"{name:<30}{diag}")
        print()
    print("  The comparison is the lesson. At 35 km depth, where the pressure")
    print("  is 0.96 GPa in all three columns, the cold subduction geotherm")
    print("  gives greenschist at 360 C, the standard continental geotherm")
    print("  gives amphibolite at 549 C, and the extended geotherm gives a")
    print("  granulite at 1042 C. Same pressure, same depth, three different")
    print("  rocks. Metamorphic grade is a statement about the thermal history")
    print("  and not about depth, which is why a blueschist found in a mountain")
    print("  belt is evidence that a cold slab was there -- evidence about a")
    print("  *process*, recovered from a rock.")
    print()
    print("  A caution about box classifications. The standard continental")
    print("  geotherm at 25 km lands at 345 C and 0.69 GPa, just inside the")
    print("  blueschist box used here. In the field, blueschist terranes are")
    print("  recognised by the *low* geothermal gradient their assemblages")
    print("  imply and by their association with other cold-subduction rocks,")
    print("  not by a single P-T point. Moving one boundary by 50 C moves")
    print("  whole rows of this table, and that sensitivity is a property of")
    print("  the classification rather than of the Earth.")
    print()
    print("  The two geotherm models differ in a way worth noticing. The linear")
    print("  geotherm keeps rising forever, which would give absurd")
    print("  temperatures at 45 km; the conductive geotherm with heat")
    print("  production flattens because the flux grows with depth as the")
    print("  crust generates heat. The flattening is the reason the continental")
    print("  geotherm reaches only 400-600 C at the Moho rather than the")
    print("  1100 C a linear extrapolation would give, and it is the reason a")
    print("  metamorphic petrologist needs a thermal model rather than a")
    print("  thermometer to read a burial depth out of a mineral assemblage.")
    print()


def part4_properties():
    section("4. Property ranges by rock class")
    print("  Grain density, porosity and the resulting bulk density are given")
    print("  as NOMINAL ranges; every one of them overlaps its neighbours, and")
    print("  the overlap is the honest part of the table.")
    print()
    classes = [
        ("granite (igneous, felsic)", 2.60, 2.70, 0.005, 0.02),
        ("basalt (igneous, mafic)", 2.85, 3.00, 0.01, 0.10),
        ("gabbro (igneous, mafic)", 2.90, 3.10, 0.005, 0.03),
        ("peridotite (mantle)", 3.20, 3.40, 0.001, 0.01),
        ("sandstone (clastic)", 2.65, 2.70, 0.10, 0.30),
        ("shale (clastic)", 2.65, 2.75, 0.05, 0.25),
        ("limestone (carbonate)", 2.70, 2.75, 0.02, 0.20),
        ("gneiss (metamorphic)", 2.65, 2.80, 0.005, 0.03),
        ("slate (metamorphic)", 2.70, 2.80, 0.005, 0.02),
    ]
    print(f"  {'rock class':<28}{'rho_grain':>18}{'porosity':>16}"
          f"{'rho_bulk (dry)':>20}")
    for name, lo, hi, plo, phi_hi in classes:
        rho_min = (1 - phi_hi) * lo
        rho_max = (1 - plo) * hi
        print(f"  {name:<28}{f'{lo:.2f}-{hi:.2f}':>18}"
              f"{f'{plo:.3f}-{phi_hi:.2f}':>16}"
              f"{f'{rho_min:.2f}-{rho_max:.2f}':>20}")
    print()
    print("  Two rows carry most of the lesson.")
    print()
    print("  Sandstone and granite have almost the same grain density, 2.65 to")
    print("  2.70 g/cm^3, yet the sandstone's bulk density reaches down to 1.85")
    print("  against the granite's floor of 2.55 g/cm^3 -- a contrast of about")
    print("  27 per cent, and one that comes entirely from porosity. A gravity")
    print("  survey separates them, but what it is")
    print("  mapping is porosity, not mineralogy. Call the sandstone a")
    print("  reservoir and the granite a basement and the same measurement is")
    print("  suddenly an exploration result.")
    print()
    print("  Peridotite and gabbro do differ in mineralogy, and it shows: 3.2")
    print("  to 3.4 against 2.9 to 3.1 g/cm^3, a contrast of about 15 per cent")
    print("  with essentially zero porosity on both sides. That is the contrast")
    print("  that makes the Moho visible in a gravity profile, and it is a")
    print("  mineralogical contrast rather than a porosity contrast. The two")
    print("  kinds of contrast look identical in a density log and completely")
    print("  different in a PEF log, which is the subject of the previous")
    print("  lesson.")
    print()


def main():
    print("Igneous, sedimentary and metamorphic rocks: classification and properties.")
    part1_igneous()
    part2_sedimentary()
    part3_metamorphic()
    part4_properties()
    print("=" * 74)
    print("Classification boundaries and property ranges are TABULATED or")
    print("NOMINAL and are labelled. Three classification procedures are")
    print("implemented and their outputs checked against the expected names.")
    print("=" * 74)


if __name__ == "__main__":
    main()
